from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_integrations():
    integrations = HTTPRuntime("https://integrations.googleapis.com/")

    renames = {
        "ErrorResponse": "_integrations_1_ErrorResponse",
        "EnterpriseCrmFrontendsEventbusProtoParamSpecEntryIn": "_integrations_2_EnterpriseCrmFrontendsEventbusProtoParamSpecEntryIn",
        "EnterpriseCrmFrontendsEventbusProtoParamSpecEntryOut": "_integrations_3_EnterpriseCrmFrontendsEventbusProtoParamSpecEntryOut",
        "GoogleCloudIntegrationsV1alphaCoordinateIn": "_integrations_4_GoogleCloudIntegrationsV1alphaCoordinateIn",
        "GoogleCloudIntegrationsV1alphaCoordinateOut": "_integrations_5_GoogleCloudIntegrationsV1alphaCoordinateOut",
        "GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseIn": "_integrations_6_GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseIn",
        "GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseOut": "_integrations_7_GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseOut",
        "GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsIn": "_integrations_8_GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsIn",
        "GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsOut": "_integrations_9_GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsOut",
        "EnterpriseCrmEventbusProtoEventBusPropertiesIn": "_integrations_10_EnterpriseCrmEventbusProtoEventBusPropertiesIn",
        "EnterpriseCrmEventbusProtoEventBusPropertiesOut": "_integrations_11_EnterpriseCrmEventbusProtoEventBusPropertiesOut",
        "EnterpriseCrmEventbusProtoExternalTrafficIn": "_integrations_12_EnterpriseCrmEventbusProtoExternalTrafficIn",
        "EnterpriseCrmEventbusProtoExternalTrafficOut": "_integrations_13_EnterpriseCrmEventbusProtoExternalTrafficOut",
        "EnterpriseCrmFrontendsEventbusProtoEventParametersIn": "_integrations_14_EnterpriseCrmFrontendsEventbusProtoEventParametersIn",
        "EnterpriseCrmFrontendsEventbusProtoEventParametersOut": "_integrations_15_EnterpriseCrmFrontendsEventbusProtoEventParametersOut",
        "GoogleCloudIntegrationsV1alphaTakeoverEditLockResponseIn": "_integrations_16_GoogleCloudIntegrationsV1alphaTakeoverEditLockResponseIn",
        "GoogleCloudIntegrationsV1alphaTakeoverEditLockResponseOut": "_integrations_17_GoogleCloudIntegrationsV1alphaTakeoverEditLockResponseOut",
        "EnterpriseCrmEventbusProtoCombinedConditionIn": "_integrations_18_EnterpriseCrmEventbusProtoCombinedConditionIn",
        "EnterpriseCrmEventbusProtoCombinedConditionOut": "_integrations_19_EnterpriseCrmEventbusProtoCombinedConditionOut",
        "EnterpriseCrmEventbusProtoAttributesIn": "_integrations_20_EnterpriseCrmEventbusProtoAttributesIn",
        "EnterpriseCrmEventbusProtoAttributesOut": "_integrations_21_EnterpriseCrmEventbusProtoAttributesOut",
        "GoogleCloudIntegrationsV1alphaIntParameterArrayIn": "_integrations_22_GoogleCloudIntegrationsV1alphaIntParameterArrayIn",
        "GoogleCloudIntegrationsV1alphaIntParameterArrayOut": "_integrations_23_GoogleCloudIntegrationsV1alphaIntParameterArrayOut",
        "EnterpriseCrmEventbusProtoStringFunctionIn": "_integrations_24_EnterpriseCrmEventbusProtoStringFunctionIn",
        "EnterpriseCrmEventbusProtoStringFunctionOut": "_integrations_25_EnterpriseCrmEventbusProtoStringFunctionOut",
        "GoogleCloudIntegrationsV1alphaSuccessPolicyIn": "_integrations_26_GoogleCloudIntegrationsV1alphaSuccessPolicyIn",
        "GoogleCloudIntegrationsV1alphaSuccessPolicyOut": "_integrations_27_GoogleCloudIntegrationsV1alphaSuccessPolicyOut",
        "EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotIn": "_integrations_28_EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotIn",
        "EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotOut": "_integrations_29_EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotOut",
        "EnterpriseCrmLoggingGwsSanitizeOptionsIn": "_integrations_30_EnterpriseCrmLoggingGwsSanitizeOptionsIn",
        "EnterpriseCrmLoggingGwsSanitizeOptionsOut": "_integrations_31_EnterpriseCrmLoggingGwsSanitizeOptionsOut",
        "GoogleCloudIntegrationsV1alphaAuthTokenIn": "_integrations_32_GoogleCloudIntegrationsV1alphaAuthTokenIn",
        "GoogleCloudIntegrationsV1alphaAuthTokenOut": "_integrations_33_GoogleCloudIntegrationsV1alphaAuthTokenOut",
        "GoogleCloudIntegrationsV1alphaGenerateTokenResponseIn": "_integrations_34_GoogleCloudIntegrationsV1alphaGenerateTokenResponseIn",
        "GoogleCloudIntegrationsV1alphaGenerateTokenResponseOut": "_integrations_35_GoogleCloudIntegrationsV1alphaGenerateTokenResponseOut",
        "EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryIn": "_integrations_36_EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryIn",
        "EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryOut": "_integrations_37_EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryOut",
        "EnterpriseCrmEventbusStatsDimensionsIn": "_integrations_38_EnterpriseCrmEventbusStatsDimensionsIn",
        "EnterpriseCrmEventbusStatsDimensionsOut": "_integrations_39_EnterpriseCrmEventbusStatsDimensionsOut",
        "GoogleCloudConnectorsV1EncryptionKeyIn": "_integrations_40_GoogleCloudConnectorsV1EncryptionKeyIn",
        "GoogleCloudConnectorsV1EncryptionKeyOut": "_integrations_41_GoogleCloudConnectorsV1EncryptionKeyOut",
        "GoogleCloudIntegrationsV1alphaCancelExecutionResponseIn": "_integrations_42_GoogleCloudIntegrationsV1alphaCancelExecutionResponseIn",
        "GoogleCloudIntegrationsV1alphaCancelExecutionResponseOut": "_integrations_43_GoogleCloudIntegrationsV1alphaCancelExecutionResponseOut",
        "EnterpriseCrmEventbusProtoTransformExpressionIn": "_integrations_44_EnterpriseCrmEventbusProtoTransformExpressionIn",
        "EnterpriseCrmEventbusProtoTransformExpressionOut": "_integrations_45_EnterpriseCrmEventbusProtoTransformExpressionOut",
        "GoogleCloudIntegrationsV1alphaTaskExecutionDetailsIn": "_integrations_46_GoogleCloudIntegrationsV1alphaTaskExecutionDetailsIn",
        "GoogleCloudIntegrationsV1alphaTaskExecutionDetailsOut": "_integrations_47_GoogleCloudIntegrationsV1alphaTaskExecutionDetailsOut",
        "EnterpriseCrmEventbusProtoTriggerCriteriaIn": "_integrations_48_EnterpriseCrmEventbusProtoTriggerCriteriaIn",
        "EnterpriseCrmEventbusProtoTriggerCriteriaOut": "_integrations_49_EnterpriseCrmEventbusProtoTriggerCriteriaOut",
        "EnterpriseCrmFrontendsEventbusProtoParameterEntryIn": "_integrations_50_EnterpriseCrmFrontendsEventbusProtoParameterEntryIn",
        "EnterpriseCrmFrontendsEventbusProtoParameterEntryOut": "_integrations_51_EnterpriseCrmFrontendsEventbusProtoParameterEntryOut",
        "GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestIn": "_integrations_52_GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestIn",
        "GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestOut": "_integrations_53_GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestOut",
        "EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn": "_integrations_54_EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn",
        "EnterpriseCrmFrontendsEventbusProtoWorkflowParametersOut": "_integrations_55_EnterpriseCrmFrontendsEventbusProtoWorkflowParametersOut",
        "EnterpriseCrmEventbusProtoEventExecutionSnapshotIn": "_integrations_56_EnterpriseCrmEventbusProtoEventExecutionSnapshotIn",
        "EnterpriseCrmEventbusProtoEventExecutionSnapshotOut": "_integrations_57_EnterpriseCrmEventbusProtoEventExecutionSnapshotOut",
        "GoogleCloudIntegrationsV1alphaTaskConfigIn": "_integrations_58_GoogleCloudIntegrationsV1alphaTaskConfigIn",
        "GoogleCloudIntegrationsV1alphaTaskConfigOut": "_integrations_59_GoogleCloudIntegrationsV1alphaTaskConfigOut",
        "EnterpriseCrmEventbusProtoTaskExecutionDetailsIn": "_integrations_60_EnterpriseCrmEventbusProtoTaskExecutionDetailsIn",
        "EnterpriseCrmEventbusProtoTaskExecutionDetailsOut": "_integrations_61_EnterpriseCrmEventbusProtoTaskExecutionDetailsOut",
        "EnterpriseCrmEventbusProtoIntArrayFunctionIn": "_integrations_62_EnterpriseCrmEventbusProtoIntArrayFunctionIn",
        "EnterpriseCrmEventbusProtoIntArrayFunctionOut": "_integrations_63_EnterpriseCrmEventbusProtoIntArrayFunctionOut",
        "EnterpriseCrmEventbusProtoParameterMapFieldIn": "_integrations_64_EnterpriseCrmEventbusProtoParameterMapFieldIn",
        "EnterpriseCrmEventbusProtoParameterMapFieldOut": "_integrations_65_EnterpriseCrmEventbusProtoParameterMapFieldOut",
        "EnterpriseCrmEventbusProtoTaskAlertConfigIn": "_integrations_66_EnterpriseCrmEventbusProtoTaskAlertConfigIn",
        "EnterpriseCrmEventbusProtoTaskAlertConfigOut": "_integrations_67_EnterpriseCrmEventbusProtoTaskAlertConfigOut",
        "GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponseIn": "_integrations_68_GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponseIn",
        "GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponseOut": "_integrations_69_GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponseOut",
        "EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsIn": "_integrations_70_EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsIn",
        "EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsOut": "_integrations_71_EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsOut",
        "EnterpriseCrmEventbusProtoTeardownTaskConfigIn": "_integrations_72_EnterpriseCrmEventbusProtoTeardownTaskConfigIn",
        "EnterpriseCrmEventbusProtoTeardownTaskConfigOut": "_integrations_73_EnterpriseCrmEventbusProtoTeardownTaskConfigOut",
        "GoogleCloudIntegrationsV1alphaUsernameAndPasswordIn": "_integrations_74_GoogleCloudIntegrationsV1alphaUsernameAndPasswordIn",
        "GoogleCloudIntegrationsV1alphaUsernameAndPasswordOut": "_integrations_75_GoogleCloudIntegrationsV1alphaUsernameAndPasswordOut",
        "GoogleCloudIntegrationsV1alphaCancelExecutionRequestIn": "_integrations_76_GoogleCloudIntegrationsV1alphaCancelExecutionRequestIn",
        "GoogleCloudIntegrationsV1alphaCancelExecutionRequestOut": "_integrations_77_GoogleCloudIntegrationsV1alphaCancelExecutionRequestOut",
        "EnterpriseCrmFrontendsEventbusProtoParameterMapIn": "_integrations_78_EnterpriseCrmFrontendsEventbusProtoParameterMapIn",
        "EnterpriseCrmFrontendsEventbusProtoParameterMapOut": "_integrations_79_EnterpriseCrmFrontendsEventbusProtoParameterMapOut",
        "GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseIn": "_integrations_80_GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseIn",
        "GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseOut": "_integrations_81_GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseOut",
        "EnterpriseCrmEventbusProtoStringArrayFunctionIn": "_integrations_82_EnterpriseCrmEventbusProtoStringArrayFunctionIn",
        "EnterpriseCrmEventbusProtoStringArrayFunctionOut": "_integrations_83_EnterpriseCrmEventbusProtoStringArrayFunctionOut",
        "GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsIn": "_integrations_84_GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsIn",
        "GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsOut": "_integrations_85_GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsOut",
        "EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterIn": "_integrations_86_EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterIn",
        "EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterOut": "_integrations_87_EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterOut",
        "EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionIn": "_integrations_88_EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionIn",
        "EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionOut": "_integrations_89_EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionOut",
        "GoogleCloudIntegrationsV1alphaClientCertificateIn": "_integrations_90_GoogleCloudIntegrationsV1alphaClientCertificateIn",
        "GoogleCloudIntegrationsV1alphaClientCertificateOut": "_integrations_91_GoogleCloudIntegrationsV1alphaClientCertificateOut",
        "GoogleCloudIntegrationsV1alphaJwtIn": "_integrations_92_GoogleCloudIntegrationsV1alphaJwtIn",
        "GoogleCloudIntegrationsV1alphaJwtOut": "_integrations_93_GoogleCloudIntegrationsV1alphaJwtOut",
        "EnterpriseCrmEventbusProtoJsonFunctionIn": "_integrations_94_EnterpriseCrmEventbusProtoJsonFunctionIn",
        "EnterpriseCrmEventbusProtoJsonFunctionOut": "_integrations_95_EnterpriseCrmEventbusProtoJsonFunctionOut",
        "EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayIn": "_integrations_96_EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayIn",
        "EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayOut": "_integrations_97_EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayOut",
        "GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataIn": "_integrations_98_GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataIn",
        "GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataOut": "_integrations_99_GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataOut",
        "GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowIn": "_integrations_100_GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowIn",
        "GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowOut": "_integrations_101_GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowOut",
        "GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseIn": "_integrations_102_GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseIn",
        "GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseOut": "_integrations_103_GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseOut",
        "GoogleCloudConnectorsV1LockConfigIn": "_integrations_104_GoogleCloudConnectorsV1LockConfigIn",
        "GoogleCloudConnectorsV1LockConfigOut": "_integrations_105_GoogleCloudConnectorsV1LockConfigOut",
        "EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsIn": "_integrations_106_EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsIn",
        "EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsOut": "_integrations_107_EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsOut",
        "EnterpriseCrmEventbusProtoNotificationIn": "_integrations_108_EnterpriseCrmEventbusProtoNotificationIn",
        "EnterpriseCrmEventbusProtoNotificationOut": "_integrations_109_EnterpriseCrmEventbusProtoNotificationOut",
        "GoogleCloudConnectorsV1AuthConfigSshPublicKeyIn": "_integrations_110_GoogleCloudConnectorsV1AuthConfigSshPublicKeyIn",
        "GoogleCloudConnectorsV1AuthConfigSshPublicKeyOut": "_integrations_111_GoogleCloudConnectorsV1AuthConfigSshPublicKeyOut",
        "GoogleCloudIntegrationsV1alphaNextTaskIn": "_integrations_112_GoogleCloudIntegrationsV1alphaNextTaskIn",
        "GoogleCloudIntegrationsV1alphaNextTaskOut": "_integrations_113_GoogleCloudIntegrationsV1alphaNextTaskOut",
        "EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn": "_integrations_114_EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn",
        "EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut": "_integrations_115_EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut",
        "EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageIn": "_integrations_116_EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageIn",
        "EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageOut": "_integrations_117_EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageOut",
        "EnterpriseCrmEventbusProtoStringArrayIn": "_integrations_118_EnterpriseCrmEventbusProtoStringArrayIn",
        "EnterpriseCrmEventbusProtoStringArrayOut": "_integrations_119_EnterpriseCrmEventbusProtoStringArrayOut",
        "GoogleCloudIntegrationsV1alphaResolveSuspensionRequestIn": "_integrations_120_GoogleCloudIntegrationsV1alphaResolveSuspensionRequestIn",
        "GoogleCloudIntegrationsV1alphaResolveSuspensionRequestOut": "_integrations_121_GoogleCloudIntegrationsV1alphaResolveSuspensionRequestOut",
        "EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueIn": "_integrations_122_EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueIn",
        "EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueOut": "_integrations_123_EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueOut",
        "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityIn": "_integrations_124_EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityIn",
        "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityOut": "_integrations_125_EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityOut",
        "GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn": "_integrations_126_GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn",
        "GoogleCloudIntegrationsV1alphaErrorCatcherConfigOut": "_integrations_127_GoogleCloudIntegrationsV1alphaErrorCatcherConfigOut",
        "GoogleCloudIntegrationsV1alphaExecutionDetailsIn": "_integrations_128_GoogleCloudIntegrationsV1alphaExecutionDetailsIn",
        "GoogleCloudIntegrationsV1alphaExecutionDetailsOut": "_integrations_129_GoogleCloudIntegrationsV1alphaExecutionDetailsOut",
        "EnterpriseCrmEventbusProtoBaseValueIn": "_integrations_130_EnterpriseCrmEventbusProtoBaseValueIn",
        "EnterpriseCrmEventbusProtoBaseValueOut": "_integrations_131_EnterpriseCrmEventbusProtoBaseValueOut",
        "GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigIn": "_integrations_132_GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigIn",
        "GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigOut": "_integrations_133_GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigOut",
        "GoogleCloudIntegrationsV1alphaListCertificatesResponseIn": "_integrations_134_GoogleCloudIntegrationsV1alphaListCertificatesResponseIn",
        "GoogleCloudIntegrationsV1alphaListCertificatesResponseOut": "_integrations_135_GoogleCloudIntegrationsV1alphaListCertificatesResponseOut",
        "GoogleCloudIntegrationsV1alphaCertificateIn": "_integrations_136_GoogleCloudIntegrationsV1alphaCertificateIn",
        "GoogleCloudIntegrationsV1alphaCertificateOut": "_integrations_137_GoogleCloudIntegrationsV1alphaCertificateOut",
        "EnterpriseCrmEventbusProtoValueTypeIn": "_integrations_138_EnterpriseCrmEventbusProtoValueTypeIn",
        "EnterpriseCrmEventbusProtoValueTypeOut": "_integrations_139_EnterpriseCrmEventbusProtoValueTypeOut",
        "GoogleCloudIntegrationsV1alphaAttemptStatsIn": "_integrations_140_GoogleCloudIntegrationsV1alphaAttemptStatsIn",
        "GoogleCloudIntegrationsV1alphaAttemptStatsOut": "_integrations_141_GoogleCloudIntegrationsV1alphaAttemptStatsOut",
        "GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseIn": "_integrations_142_GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseIn",
        "GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseOut": "_integrations_143_GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseOut",
        "EnterpriseCrmFrontendsEventbusProtoRollbackStrategyIn": "_integrations_144_EnterpriseCrmFrontendsEventbusProtoRollbackStrategyIn",
        "EnterpriseCrmFrontendsEventbusProtoRollbackStrategyOut": "_integrations_145_EnterpriseCrmFrontendsEventbusProtoRollbackStrategyOut",
        "GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsIn": "_integrations_146_GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsIn",
        "GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsOut": "_integrations_147_GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsOut",
        "EnterpriseCrmEventbusProtoDoubleArrayIn": "_integrations_148_EnterpriseCrmEventbusProtoDoubleArrayIn",
        "EnterpriseCrmEventbusProtoDoubleArrayOut": "_integrations_149_EnterpriseCrmEventbusProtoDoubleArrayOut",
        "GoogleCloudConnectorsV1ConnectionStatusIn": "_integrations_150_GoogleCloudConnectorsV1ConnectionStatusIn",
        "GoogleCloudConnectorsV1ConnectionStatusOut": "_integrations_151_GoogleCloudConnectorsV1ConnectionStatusOut",
        "EnterpriseCrmEventbusProtoParameterMapIn": "_integrations_152_EnterpriseCrmEventbusProtoParameterMapIn",
        "EnterpriseCrmEventbusProtoParameterMapOut": "_integrations_153_EnterpriseCrmEventbusProtoParameterMapOut",
        "GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequestIn": "_integrations_154_GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequestIn",
        "GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequestOut": "_integrations_155_GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequestOut",
        "EnterpriseCrmEventbusProtoNextTeardownTaskIn": "_integrations_156_EnterpriseCrmEventbusProtoNextTeardownTaskIn",
        "EnterpriseCrmEventbusProtoNextTeardownTaskOut": "_integrations_157_EnterpriseCrmEventbusProtoNextTeardownTaskOut",
        "GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationIn": "_integrations_158_GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationIn",
        "GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationOut": "_integrations_159_GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationOut",
        "EnterpriseCrmEventbusProtoLogSettingsIn": "_integrations_160_EnterpriseCrmEventbusProtoLogSettingsIn",
        "EnterpriseCrmEventbusProtoLogSettingsOut": "_integrations_161_EnterpriseCrmEventbusProtoLogSettingsOut",
        "EnterpriseCrmEventbusProtoIntParameterArrayIn": "_integrations_162_EnterpriseCrmEventbusProtoIntParameterArrayIn",
        "EnterpriseCrmEventbusProtoIntParameterArrayOut": "_integrations_163_EnterpriseCrmEventbusProtoIntParameterArrayOut",
        "EnterpriseCrmEventbusProtoBaseFunctionIn": "_integrations_164_EnterpriseCrmEventbusProtoBaseFunctionIn",
        "EnterpriseCrmEventbusProtoBaseFunctionOut": "_integrations_165_EnterpriseCrmEventbusProtoBaseFunctionOut",
        "GoogleCloudIntegrationsV1alphaLiftSuspensionRequestIn": "_integrations_166_GoogleCloudIntegrationsV1alphaLiftSuspensionRequestIn",
        "GoogleCloudIntegrationsV1alphaLiftSuspensionRequestOut": "_integrations_167_GoogleCloudIntegrationsV1alphaLiftSuspensionRequestOut",
        "EnterpriseCrmEventbusProtoErrorDetailIn": "_integrations_168_EnterpriseCrmEventbusProtoErrorDetailIn",
        "EnterpriseCrmEventbusProtoErrorDetailOut": "_integrations_169_EnterpriseCrmEventbusProtoErrorDetailOut",
        "GoogleCloudIntegrationsV1alphaListConnectionsResponseIn": "_integrations_170_GoogleCloudIntegrationsV1alphaListConnectionsResponseIn",
        "GoogleCloudIntegrationsV1alphaListConnectionsResponseOut": "_integrations_171_GoogleCloudIntegrationsV1alphaListConnectionsResponseOut",
        "GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestIn": "_integrations_172_GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestIn",
        "GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestOut": "_integrations_173_GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestOut",
        "EnterpriseCrmEventbusProtoTaskMetadataIn": "_integrations_174_EnterpriseCrmEventbusProtoTaskMetadataIn",
        "EnterpriseCrmEventbusProtoTaskMetadataOut": "_integrations_175_EnterpriseCrmEventbusProtoTaskMetadataOut",
        "EnterpriseCrmEventbusProtoSuccessPolicyIn": "_integrations_176_EnterpriseCrmEventbusProtoSuccessPolicyIn",
        "EnterpriseCrmEventbusProtoSuccessPolicyOut": "_integrations_177_EnterpriseCrmEventbusProtoSuccessPolicyOut",
        "GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseIn": "_integrations_178_GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseIn",
        "GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseOut": "_integrations_179_GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseOut",
        "GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequestIn": "_integrations_180_GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequestIn",
        "GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequestOut": "_integrations_181_GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequestOut",
        "EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsIn": "_integrations_182_EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsIn",
        "EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsOut": "_integrations_183_EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsOut",
        "GoogleCloudIntegrationsV1alphaSuspensionAuditIn": "_integrations_184_GoogleCloudIntegrationsV1alphaSuspensionAuditIn",
        "GoogleCloudIntegrationsV1alphaSuspensionAuditOut": "_integrations_185_GoogleCloudIntegrationsV1alphaSuspensionAuditOut",
        "EnterpriseCrmEventbusProtoNodeIdentifierIn": "_integrations_186_EnterpriseCrmEventbusProtoNodeIdentifierIn",
        "EnterpriseCrmEventbusProtoNodeIdentifierOut": "_integrations_187_EnterpriseCrmEventbusProtoNodeIdentifierOut",
        "GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerIn": "_integrations_188_GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerIn",
        "GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerOut": "_integrations_189_GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerOut",
        "EnterpriseCrmEventbusProtoEventParametersIn": "_integrations_190_EnterpriseCrmEventbusProtoEventParametersIn",
        "EnterpriseCrmEventbusProtoEventParametersOut": "_integrations_191_EnterpriseCrmEventbusProtoEventParametersOut",
        "EnterpriseCrmEventbusProtoSuspensionResolutionInfoIn": "_integrations_192_EnterpriseCrmEventbusProtoSuspensionResolutionInfoIn",
        "EnterpriseCrmEventbusProtoSuspensionResolutionInfoOut": "_integrations_193_EnterpriseCrmEventbusProtoSuspensionResolutionInfoOut",
        "GoogleCloudConnectorsV1LogConfigIn": "_integrations_194_GoogleCloudConnectorsV1LogConfigIn",
        "GoogleCloudConnectorsV1LogConfigOut": "_integrations_195_GoogleCloudConnectorsV1LogConfigOut",
        "EnterpriseCrmEventbusProtoConditionIn": "_integrations_196_EnterpriseCrmEventbusProtoConditionIn",
        "EnterpriseCrmEventbusProtoConditionOut": "_integrations_197_EnterpriseCrmEventbusProtoConditionOut",
        "EnterpriseCrmEventbusProtoConditionResultIn": "_integrations_198_EnterpriseCrmEventbusProtoConditionResultIn",
        "EnterpriseCrmEventbusProtoConditionResultOut": "_integrations_199_EnterpriseCrmEventbusProtoConditionResultOut",
        "GoogleCloudConnectorsV1NodeConfigIn": "_integrations_200_GoogleCloudConnectorsV1NodeConfigIn",
        "GoogleCloudConnectorsV1NodeConfigOut": "_integrations_201_GoogleCloudConnectorsV1NodeConfigOut",
        "EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn": "_integrations_202_EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn",
        "EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut": "_integrations_203_EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut",
        "EnterpriseCrmEventbusProtoSerializedObjectParameterIn": "_integrations_204_EnterpriseCrmEventbusProtoSerializedObjectParameterIn",
        "EnterpriseCrmEventbusProtoSerializedObjectParameterOut": "_integrations_205_EnterpriseCrmEventbusProtoSerializedObjectParameterOut",
        "GoogleCloudIntegrationsV1alphaExecutionIn": "_integrations_206_GoogleCloudIntegrationsV1alphaExecutionIn",
        "GoogleCloudIntegrationsV1alphaExecutionOut": "_integrations_207_GoogleCloudIntegrationsV1alphaExecutionOut",
        "EnterpriseCrmEventbusProtoExecutionTraceInfoIn": "_integrations_208_EnterpriseCrmEventbusProtoExecutionTraceInfoIn",
        "EnterpriseCrmEventbusProtoExecutionTraceInfoOut": "_integrations_209_EnterpriseCrmEventbusProtoExecutionTraceInfoOut",
        "GoogleCloudConnectorsV1DestinationConfigIn": "_integrations_210_GoogleCloudConnectorsV1DestinationConfigIn",
        "GoogleCloudConnectorsV1DestinationConfigOut": "_integrations_211_GoogleCloudConnectorsV1DestinationConfigOut",
        "EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoIn": "_integrations_212_EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoIn",
        "EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoOut": "_integrations_213_EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoOut",
        "EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayIn": "_integrations_214_EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayIn",
        "EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayOut": "_integrations_215_EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayOut",
        "GoogleCloudIntegrationsV1alphaPublishIntegrationVersionRequestIn": "_integrations_216_GoogleCloudIntegrationsV1alphaPublishIntegrationVersionRequestIn",
        "GoogleCloudIntegrationsV1alphaPublishIntegrationVersionRequestOut": "_integrations_217_GoogleCloudIntegrationsV1alphaPublishIntegrationVersionRequestOut",
        "GoogleCloudIntegrationsV1alphaAccessTokenIn": "_integrations_218_GoogleCloudIntegrationsV1alphaAccessTokenIn",
        "GoogleCloudIntegrationsV1alphaAccessTokenOut": "_integrations_219_GoogleCloudIntegrationsV1alphaAccessTokenOut",
        "EnterpriseCrmEventbusProtoTokenIn": "_integrations_220_EnterpriseCrmEventbusProtoTokenIn",
        "EnterpriseCrmEventbusProtoTokenOut": "_integrations_221_EnterpriseCrmEventbusProtoTokenOut",
        "EnterpriseCrmEventbusProtoFieldIn": "_integrations_222_EnterpriseCrmEventbusProtoFieldIn",
        "EnterpriseCrmEventbusProtoFieldOut": "_integrations_223_EnterpriseCrmEventbusProtoFieldOut",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIn": "_integrations_224_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIn",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleOut": "_integrations_225_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleOut",
        "EnterpriseCrmEventbusProtoFailurePolicyIn": "_integrations_226_EnterpriseCrmEventbusProtoFailurePolicyIn",
        "EnterpriseCrmEventbusProtoFailurePolicyOut": "_integrations_227_EnterpriseCrmEventbusProtoFailurePolicyOut",
        "GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestIn": "_integrations_228_GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestIn",
        "GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestOut": "_integrations_229_GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestOut",
        "EnterpriseCrmEventbusProtoParamSpecEntryConfigIn": "_integrations_230_EnterpriseCrmEventbusProtoParamSpecEntryConfigIn",
        "EnterpriseCrmEventbusProtoParamSpecEntryConfigOut": "_integrations_231_EnterpriseCrmEventbusProtoParamSpecEntryConfigOut",
        "GoogleCloudIntegrationsV1alphaIntegrationIn": "_integrations_232_GoogleCloudIntegrationsV1alphaIntegrationIn",
        "GoogleCloudIntegrationsV1alphaIntegrationOut": "_integrations_233_GoogleCloudIntegrationsV1alphaIntegrationOut",
        "EnterpriseCrmEventbusProtoAddressIn": "_integrations_234_EnterpriseCrmEventbusProtoAddressIn",
        "EnterpriseCrmEventbusProtoAddressOut": "_integrations_235_EnterpriseCrmEventbusProtoAddressOut",
        "EnterpriseCrmFrontendsEventbusProtoTaskConfigIn": "_integrations_236_EnterpriseCrmFrontendsEventbusProtoTaskConfigIn",
        "EnterpriseCrmFrontendsEventbusProtoTaskConfigOut": "_integrations_237_EnterpriseCrmFrontendsEventbusProtoTaskConfigOut",
        "GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestIn": "_integrations_238_GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestIn",
        "GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestOut": "_integrations_239_GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestOut",
        "EnterpriseCrmEventbusProtoTaskMetadataAdminIn": "_integrations_240_EnterpriseCrmEventbusProtoTaskMetadataAdminIn",
        "EnterpriseCrmEventbusProtoTaskMetadataAdminOut": "_integrations_241_EnterpriseCrmEventbusProtoTaskMetadataAdminOut",
        "GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeIn": "_integrations_242_GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeIn",
        "GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeOut": "_integrations_243_GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeOut",
        "GoogleCloudIntegrationsV1alphaExecutionSnapshotIn": "_integrations_244_GoogleCloudIntegrationsV1alphaExecutionSnapshotIn",
        "GoogleCloudIntegrationsV1alphaExecutionSnapshotOut": "_integrations_245_GoogleCloudIntegrationsV1alphaExecutionSnapshotOut",
        "GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseIn": "_integrations_246_GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseIn",
        "GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseOut": "_integrations_247_GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseOut",
        "EnterpriseCrmEventbusProtoTaskUiModuleConfigIn": "_integrations_248_EnterpriseCrmEventbusProtoTaskUiModuleConfigIn",
        "EnterpriseCrmEventbusProtoTaskUiModuleConfigOut": "_integrations_249_EnterpriseCrmEventbusProtoTaskUiModuleConfigOut",
        "GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaIn": "_integrations_250_GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaIn",
        "GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaOut": "_integrations_251_GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaOut",
        "GoogleCloudIntegrationsV1alphaDoubleParameterArrayIn": "_integrations_252_GoogleCloudIntegrationsV1alphaDoubleParameterArrayIn",
        "GoogleCloudIntegrationsV1alphaDoubleParameterArrayOut": "_integrations_253_GoogleCloudIntegrationsV1alphaDoubleParameterArrayOut",
        "GoogleCloudIntegrationsV1alphaBooleanParameterArrayIn": "_integrations_254_GoogleCloudIntegrationsV1alphaBooleanParameterArrayIn",
        "GoogleCloudIntegrationsV1alphaBooleanParameterArrayOut": "_integrations_255_GoogleCloudIntegrationsV1alphaBooleanParameterArrayOut",
        "EnterpriseCrmEventbusProtoNextTaskIn": "_integrations_256_EnterpriseCrmEventbusProtoNextTaskIn",
        "EnterpriseCrmEventbusProtoNextTaskOut": "_integrations_257_EnterpriseCrmEventbusProtoNextTaskOut",
        "EnterpriseCrmEventbusProtoEventExecutionDetailsIn": "_integrations_258_EnterpriseCrmEventbusProtoEventExecutionDetailsIn",
        "EnterpriseCrmEventbusProtoEventExecutionDetailsOut": "_integrations_259_EnterpriseCrmEventbusProtoEventExecutionDetailsOut",
        "GoogleCloudIntegrationsV1alphaSfdcChannelIn": "_integrations_260_GoogleCloudIntegrationsV1alphaSfdcChannelIn",
        "GoogleCloudIntegrationsV1alphaSfdcChannelOut": "_integrations_261_GoogleCloudIntegrationsV1alphaSfdcChannelOut",
        "GoogleCloudIntegrationsV1alphaExecuteEventResponseIn": "_integrations_262_GoogleCloudIntegrationsV1alphaExecuteEventResponseIn",
        "GoogleCloudIntegrationsV1alphaExecuteEventResponseOut": "_integrations_263_GoogleCloudIntegrationsV1alphaExecuteEventResponseOut",
        "EnterpriseCrmEventbusProtoCustomSuspensionRequestIn": "_integrations_264_EnterpriseCrmEventbusProtoCustomSuspensionRequestIn",
        "EnterpriseCrmEventbusProtoCustomSuspensionRequestOut": "_integrations_265_EnterpriseCrmEventbusProtoCustomSuspensionRequestOut",
        "EnterpriseCrmEventbusProtoIntArrayIn": "_integrations_266_EnterpriseCrmEventbusProtoIntArrayIn",
        "EnterpriseCrmEventbusProtoIntArrayOut": "_integrations_267_EnterpriseCrmEventbusProtoIntArrayOut",
        "GoogleCloudIntegrationsV1alphaCredentialIn": "_integrations_268_GoogleCloudIntegrationsV1alphaCredentialIn",
        "GoogleCloudIntegrationsV1alphaCredentialOut": "_integrations_269_GoogleCloudIntegrationsV1alphaCredentialOut",
        "EnterpriseCrmEventbusProtoProtoParameterArrayIn": "_integrations_270_EnterpriseCrmEventbusProtoProtoParameterArrayIn",
        "EnterpriseCrmEventbusProtoProtoParameterArrayOut": "_integrations_271_EnterpriseCrmEventbusProtoProtoParameterArrayOut",
        "GoogleCloudIntegrationsV1alphaFailurePolicyIn": "_integrations_272_GoogleCloudIntegrationsV1alphaFailurePolicyIn",
        "GoogleCloudIntegrationsV1alphaFailurePolicyOut": "_integrations_273_GoogleCloudIntegrationsV1alphaFailurePolicyOut",
        "EnterpriseCrmEventbusProtoBooleanArrayFunctionIn": "_integrations_274_EnterpriseCrmEventbusProtoBooleanArrayFunctionIn",
        "EnterpriseCrmEventbusProtoBooleanArrayFunctionOut": "_integrations_275_EnterpriseCrmEventbusProtoBooleanArrayFunctionOut",
        "CrmlogErrorCodeIn": "_integrations_276_CrmlogErrorCodeIn",
        "CrmlogErrorCodeOut": "_integrations_277_CrmlogErrorCodeOut",
        "EnterpriseCrmFrontendsEventbusProtoIntParameterArrayIn": "_integrations_278_EnterpriseCrmFrontendsEventbusProtoIntParameterArrayIn",
        "EnterpriseCrmFrontendsEventbusProtoIntParameterArrayOut": "_integrations_279_EnterpriseCrmFrontendsEventbusProtoIntParameterArrayOut",
        "GoogleCloudIntegrationsV1alphaTriggerConfigIn": "_integrations_280_GoogleCloudIntegrationsV1alphaTriggerConfigIn",
        "GoogleCloudIntegrationsV1alphaTriggerConfigOut": "_integrations_281_GoogleCloudIntegrationsV1alphaTriggerConfigOut",
        "EnterpriseCrmEventbusProtoConnectorsConnectionIn": "_integrations_282_EnterpriseCrmEventbusProtoConnectorsConnectionIn",
        "EnterpriseCrmEventbusProtoConnectorsConnectionOut": "_integrations_283_EnterpriseCrmEventbusProtoConnectorsConnectionOut",
        "EnterpriseCrmFrontendsEventbusProtoParameterMapFieldIn": "_integrations_284_EnterpriseCrmFrontendsEventbusProtoParameterMapFieldIn",
        "EnterpriseCrmFrontendsEventbusProtoParameterMapFieldOut": "_integrations_285_EnterpriseCrmFrontendsEventbusProtoParameterMapFieldOut",
        "EnterpriseCrmEventbusProtoMappedFieldIn": "_integrations_286_EnterpriseCrmEventbusProtoMappedFieldIn",
        "EnterpriseCrmEventbusProtoMappedFieldOut": "_integrations_287_EnterpriseCrmEventbusProtoMappedFieldOut",
        "EnterpriseCrmEventbusProtoLoopMetadataIn": "_integrations_288_EnterpriseCrmEventbusProtoLoopMetadataIn",
        "EnterpriseCrmEventbusProtoLoopMetadataOut": "_integrations_289_EnterpriseCrmEventbusProtoLoopMetadataOut",
        "EnterpriseCrmEventbusProtoFunctionTypeIn": "_integrations_290_EnterpriseCrmEventbusProtoFunctionTypeIn",
        "EnterpriseCrmEventbusProtoFunctionTypeOut": "_integrations_291_EnterpriseCrmEventbusProtoFunctionTypeOut",
        "GoogleCloudConnectorsV1AuthConfigIn": "_integrations_292_GoogleCloudConnectorsV1AuthConfigIn",
        "GoogleCloudConnectorsV1AuthConfigOut": "_integrations_293_GoogleCloudConnectorsV1AuthConfigOut",
        "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataIn": "_integrations_294_EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataIn",
        "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataOut": "_integrations_295_EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataOut",
        "GoogleCloudIntegrationsV1alphaListSuspensionsResponseIn": "_integrations_296_GoogleCloudIntegrationsV1alphaListSuspensionsResponseIn",
        "GoogleCloudIntegrationsV1alphaListSuspensionsResponseOut": "_integrations_297_GoogleCloudIntegrationsV1alphaListSuspensionsResponseOut",
        "EnterpriseCrmEventbusProtoBooleanParameterArrayIn": "_integrations_298_EnterpriseCrmEventbusProtoBooleanParameterArrayIn",
        "EnterpriseCrmEventbusProtoBooleanParameterArrayOut": "_integrations_299_EnterpriseCrmEventbusProtoBooleanParameterArrayOut",
        "GoogleCloudIntegrationsV1alphaEnumerateConnectorPlatformRegionsResponseIn": "_integrations_300_GoogleCloudIntegrationsV1alphaEnumerateConnectorPlatformRegionsResponseIn",
        "GoogleCloudIntegrationsV1alphaEnumerateConnectorPlatformRegionsResponseOut": "_integrations_301_GoogleCloudIntegrationsV1alphaEnumerateConnectorPlatformRegionsResponseOut",
        "GoogleCloudIntegrationsV1alphaSfdcInstanceIn": "_integrations_302_GoogleCloudIntegrationsV1alphaSfdcInstanceIn",
        "GoogleCloudIntegrationsV1alphaSfdcInstanceOut": "_integrations_303_GoogleCloudIntegrationsV1alphaSfdcInstanceOut",
        "GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataIn": "_integrations_304_GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataIn",
        "GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataOut": "_integrations_305_GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataOut",
        "EnterpriseCrmEventbusProtoDoubleFunctionIn": "_integrations_306_EnterpriseCrmEventbusProtoDoubleFunctionIn",
        "EnterpriseCrmEventbusProtoDoubleFunctionOut": "_integrations_307_EnterpriseCrmEventbusProtoDoubleFunctionOut",
        "GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestIn": "_integrations_308_GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestIn",
        "GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestOut": "_integrations_309_GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestOut",
        "GoogleCloudIntegrationsV1alphaServiceAccountCredentialsIn": "_integrations_310_GoogleCloudIntegrationsV1alphaServiceAccountCredentialsIn",
        "GoogleCloudIntegrationsV1alphaServiceAccountCredentialsOut": "_integrations_311_GoogleCloudIntegrationsV1alphaServiceAccountCredentialsOut",
        "GoogleCloudIntegrationsV1alphaLiftSuspensionResponseIn": "_integrations_312_GoogleCloudIntegrationsV1alphaLiftSuspensionResponseIn",
        "GoogleCloudIntegrationsV1alphaLiftSuspensionResponseOut": "_integrations_313_GoogleCloudIntegrationsV1alphaLiftSuspensionResponseOut",
        "GoogleCloudConnectorsV1ConfigVariableIn": "_integrations_314_GoogleCloudConnectorsV1ConfigVariableIn",
        "GoogleCloudConnectorsV1ConfigVariableOut": "_integrations_315_GoogleCloudConnectorsV1ConfigVariableOut",
        "GoogleCloudIntegrationsV1alphaUploadIntegrationVersionResponseIn": "_integrations_316_GoogleCloudIntegrationsV1alphaUploadIntegrationVersionResponseIn",
        "GoogleCloudIntegrationsV1alphaUploadIntegrationVersionResponseOut": "_integrations_317_GoogleCloudIntegrationsV1alphaUploadIntegrationVersionResponseOut",
        "GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseIn": "_integrations_318_GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseIn",
        "GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseOut": "_integrations_319_GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseOut",
        "EnterpriseCrmFrontendsEventbusProtoTaskEntityIn": "_integrations_320_EnterpriseCrmFrontendsEventbusProtoTaskEntityIn",
        "EnterpriseCrmFrontendsEventbusProtoTaskEntityOut": "_integrations_321_EnterpriseCrmFrontendsEventbusProtoTaskEntityOut",
        "GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseIn": "_integrations_322_GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseIn",
        "GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseOut": "_integrations_323_GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseOut",
        "GoogleCloudIntegrationsV1alphaIntegrationVersionIn": "_integrations_324_GoogleCloudIntegrationsV1alphaIntegrationVersionIn",
        "GoogleCloudIntegrationsV1alphaIntegrationVersionOut": "_integrations_325_GoogleCloudIntegrationsV1alphaIntegrationVersionOut",
        "GoogleCloudIntegrationsV1alphaParameterMapFieldIn": "_integrations_326_GoogleCloudIntegrationsV1alphaParameterMapFieldIn",
        "GoogleCloudIntegrationsV1alphaParameterMapFieldOut": "_integrations_327_GoogleCloudIntegrationsV1alphaParameterMapFieldOut",
        "GoogleCloudIntegrationsV1alphaEventParameterIn": "_integrations_328_GoogleCloudIntegrationsV1alphaEventParameterIn",
        "GoogleCloudIntegrationsV1alphaEventParameterOut": "_integrations_329_GoogleCloudIntegrationsV1alphaEventParameterOut",
        "GoogleCloudConnectorsV1AuthConfigUserPasswordIn": "_integrations_330_GoogleCloudConnectorsV1AuthConfigUserPasswordIn",
        "GoogleCloudConnectorsV1AuthConfigUserPasswordOut": "_integrations_331_GoogleCloudConnectorsV1AuthConfigUserPasswordOut",
        "GoogleCloudConnectorsV1ConnectionIn": "_integrations_332_GoogleCloudConnectorsV1ConnectionIn",
        "GoogleCloudConnectorsV1ConnectionOut": "_integrations_333_GoogleCloudConnectorsV1ConnectionOut",
        "GoogleCloudIntegrationsV1alphaPublishIntegrationVersionResponseIn": "_integrations_334_GoogleCloudIntegrationsV1alphaPublishIntegrationVersionResponseIn",
        "GoogleCloudIntegrationsV1alphaPublishIntegrationVersionResponseOut": "_integrations_335_GoogleCloudIntegrationsV1alphaPublishIntegrationVersionResponseOut",
        "GoogleCloudIntegrationsV1alphaOidcTokenIn": "_integrations_336_GoogleCloudIntegrationsV1alphaOidcTokenIn",
        "GoogleCloudIntegrationsV1alphaOidcTokenOut": "_integrations_337_GoogleCloudIntegrationsV1alphaOidcTokenOut",
        "EnterpriseCrmEventbusProtoPropertyEntryIn": "_integrations_338_EnterpriseCrmEventbusProtoPropertyEntryIn",
        "EnterpriseCrmEventbusProtoPropertyEntryOut": "_integrations_339_EnterpriseCrmEventbusProtoPropertyEntryOut",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeIn": "_integrations_340_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeIn",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeOut": "_integrations_341_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeOut",
        "GoogleCloudIntegrationsV1alphaResolveSuspensionResponseIn": "_integrations_342_GoogleCloudIntegrationsV1alphaResolveSuspensionResponseIn",
        "GoogleCloudIntegrationsV1alphaResolveSuspensionResponseOut": "_integrations_343_GoogleCloudIntegrationsV1alphaResolveSuspensionResponseOut",
        "GoogleCloudIntegrationsV1alphaParameterMapEntryIn": "_integrations_344_GoogleCloudIntegrationsV1alphaParameterMapEntryIn",
        "GoogleCloudIntegrationsV1alphaParameterMapEntryOut": "_integrations_345_GoogleCloudIntegrationsV1alphaParameterMapEntryOut",
        "GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseIn": "_integrations_346_GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseIn",
        "GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseOut": "_integrations_347_GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseOut",
        "EnterpriseCrmEventbusProtoFunctionIn": "_integrations_348_EnterpriseCrmEventbusProtoFunctionIn",
        "EnterpriseCrmEventbusProtoFunctionOut": "_integrations_349_EnterpriseCrmEventbusProtoFunctionOut",
        "EnterpriseCrmEventbusProtoTeardownIn": "_integrations_350_EnterpriseCrmEventbusProtoTeardownIn",
        "EnterpriseCrmEventbusProtoTeardownOut": "_integrations_351_EnterpriseCrmEventbusProtoTeardownOut",
        "EnterpriseCrmEventbusProtoIntFunctionIn": "_integrations_352_EnterpriseCrmEventbusProtoIntFunctionIn",
        "EnterpriseCrmEventbusProtoIntFunctionOut": "_integrations_353_EnterpriseCrmEventbusProtoIntFunctionOut",
        "EnterpriseCrmEventbusProtoProtoArrayFunctionIn": "_integrations_354_EnterpriseCrmEventbusProtoProtoArrayFunctionIn",
        "EnterpriseCrmEventbusProtoProtoArrayFunctionOut": "_integrations_355_EnterpriseCrmEventbusProtoProtoArrayFunctionOut",
        "EnterpriseCrmFrontendsEventbusProtoStringParameterArrayIn": "_integrations_356_EnterpriseCrmFrontendsEventbusProtoStringParameterArrayIn",
        "EnterpriseCrmFrontendsEventbusProtoStringParameterArrayOut": "_integrations_357_EnterpriseCrmFrontendsEventbusProtoStringParameterArrayOut",
        "EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamIn": "_integrations_358_EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamIn",
        "EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamOut": "_integrations_359_EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamOut",
        "EnterpriseCrmEventbusProtoDoubleParameterArrayIn": "_integrations_360_EnterpriseCrmEventbusProtoDoubleParameterArrayIn",
        "EnterpriseCrmEventbusProtoDoubleParameterArrayOut": "_integrations_361_EnterpriseCrmEventbusProtoDoubleParameterArrayOut",
        "GoogleCloudIntegrationsV1alphaListIntegrationsResponseIn": "_integrations_362_GoogleCloudIntegrationsV1alphaListIntegrationsResponseIn",
        "GoogleCloudIntegrationsV1alphaListIntegrationsResponseOut": "_integrations_363_GoogleCloudIntegrationsV1alphaListIntegrationsResponseOut",
        "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueIn": "_integrations_364_GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueIn",
        "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueOut": "_integrations_365_GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueOut",
        "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigIn": "_integrations_366_GoogleCloudIntegrationsV1alphaIntegrationAlertConfigIn",
        "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigOut": "_integrations_367_GoogleCloudIntegrationsV1alphaIntegrationAlertConfigOut",
        "EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditIn": "_integrations_368_EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditIn",
        "EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditOut": "_integrations_369_EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditOut",
        "GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsIn": "_integrations_370_GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsIn",
        "GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsOut": "_integrations_371_GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsOut",
        "EnterpriseCrmEventbusProtoParameterValueTypeIn": "_integrations_372_EnterpriseCrmEventbusProtoParameterValueTypeIn",
        "EnterpriseCrmEventbusProtoParameterValueTypeOut": "_integrations_373_EnterpriseCrmEventbusProtoParameterValueTypeOut",
        "EnterpriseCrmEventbusProtoWorkflowAlertConfigIn": "_integrations_374_EnterpriseCrmEventbusProtoWorkflowAlertConfigIn",
        "EnterpriseCrmEventbusProtoWorkflowAlertConfigOut": "_integrations_375_EnterpriseCrmEventbusProtoWorkflowAlertConfigOut",
        "EnterpriseCrmEventbusProtoSuspensionExpirationIn": "_integrations_376_EnterpriseCrmEventbusProtoSuspensionExpirationIn",
        "EnterpriseCrmEventbusProtoSuspensionExpirationOut": "_integrations_377_EnterpriseCrmEventbusProtoSuspensionExpirationOut",
        "EnterpriseCrmEventbusProtoSuspensionConfigIn": "_integrations_378_EnterpriseCrmEventbusProtoSuspensionConfigIn",
        "EnterpriseCrmEventbusProtoSuspensionConfigOut": "_integrations_379_EnterpriseCrmEventbusProtoSuspensionConfigOut",
        "EnterpriseCrmEventbusProtoParameterEntryIn": "_integrations_380_EnterpriseCrmEventbusProtoParameterEntryIn",
        "EnterpriseCrmEventbusProtoParameterEntryOut": "_integrations_381_EnterpriseCrmEventbusProtoParameterEntryOut",
        "EnterpriseCrmFrontendsEventbusProtoParameterMapEntryIn": "_integrations_382_EnterpriseCrmFrontendsEventbusProtoParameterMapEntryIn",
        "EnterpriseCrmFrontendsEventbusProtoParameterMapEntryOut": "_integrations_383_EnterpriseCrmFrontendsEventbusProtoParameterMapEntryOut",
        "EnterpriseCrmEventbusProtoDoubleArrayFunctionIn": "_integrations_384_EnterpriseCrmEventbusProtoDoubleArrayFunctionIn",
        "EnterpriseCrmEventbusProtoDoubleArrayFunctionOut": "_integrations_385_EnterpriseCrmEventbusProtoDoubleArrayFunctionOut",
        "EnterpriseCrmEventbusProtoParameterMapEntryIn": "_integrations_386_EnterpriseCrmEventbusProtoParameterMapEntryIn",
        "EnterpriseCrmEventbusProtoParameterMapEntryOut": "_integrations_387_EnterpriseCrmEventbusProtoParameterMapEntryOut",
        "GoogleCloudIntegrationsV1alphaCloudSchedulerConfigIn": "_integrations_388_GoogleCloudIntegrationsV1alphaCloudSchedulerConfigIn",
        "GoogleCloudIntegrationsV1alphaCloudSchedulerConfigOut": "_integrations_389_GoogleCloudIntegrationsV1alphaCloudSchedulerConfigOut",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexIn": "_integrations_390_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexIn",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexOut": "_integrations_391_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexOut",
        "GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionIn": "_integrations_392_GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionIn",
        "GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionOut": "_integrations_393_GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionOut",
        "EnterpriseCrmEventbusProtoBuganizerNotificationIn": "_integrations_394_EnterpriseCrmEventbusProtoBuganizerNotificationIn",
        "EnterpriseCrmEventbusProtoBuganizerNotificationOut": "_integrations_395_EnterpriseCrmEventbusProtoBuganizerNotificationOut",
        "GoogleCloudIntegrationsV1alphaAuthConfigIn": "_integrations_396_GoogleCloudIntegrationsV1alphaAuthConfigIn",
        "GoogleCloudIntegrationsV1alphaAuthConfigOut": "_integrations_397_GoogleCloudIntegrationsV1alphaAuthConfigOut",
        "EnterpriseCrmEventbusProtoScatterResponseIn": "_integrations_398_EnterpriseCrmEventbusProtoScatterResponseIn",
        "EnterpriseCrmEventbusProtoScatterResponseOut": "_integrations_399_EnterpriseCrmEventbusProtoScatterResponseOut",
        "GoogleCloudConnectorsV1SecretIn": "_integrations_400_GoogleCloudConnectorsV1SecretIn",
        "GoogleCloudConnectorsV1SecretOut": "_integrations_401_GoogleCloudConnectorsV1SecretOut",
        "EnterpriseCrmEventbusProtoCoordinateIn": "_integrations_402_EnterpriseCrmEventbusProtoCoordinateIn",
        "EnterpriseCrmEventbusProtoCoordinateOut": "_integrations_403_EnterpriseCrmEventbusProtoCoordinateOut",
        "GoogleCloudConnectorsV1DestinationIn": "_integrations_404_GoogleCloudConnectorsV1DestinationIn",
        "GoogleCloudConnectorsV1DestinationOut": "_integrations_405_GoogleCloudConnectorsV1DestinationOut",
        "EnterpriseCrmEventbusProtoTaskUiConfigIn": "_integrations_406_EnterpriseCrmEventbusProtoTaskUiConfigIn",
        "EnterpriseCrmEventbusProtoTaskUiConfigOut": "_integrations_407_EnterpriseCrmEventbusProtoTaskUiConfigOut",
        "EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayIn": "_integrations_408_EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayIn",
        "EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayOut": "_integrations_409_EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayOut",
        "EnterpriseCrmEventbusProtoBooleanFunctionIn": "_integrations_410_EnterpriseCrmEventbusProtoBooleanFunctionIn",
        "EnterpriseCrmEventbusProtoBooleanFunctionOut": "_integrations_411_EnterpriseCrmEventbusProtoBooleanFunctionOut",
        "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsIn": "_integrations_412_EnterpriseCrmEventbusProtoSuspensionAuthPermissionsIn",
        "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsOut": "_integrations_413_EnterpriseCrmEventbusProtoSuspensionAuthPermissionsOut",
        "EnterpriseCrmEventbusProtoStringParameterArrayIn": "_integrations_414_EnterpriseCrmEventbusProtoStringParameterArrayIn",
        "EnterpriseCrmEventbusProtoStringParameterArrayOut": "_integrations_415_EnterpriseCrmEventbusProtoStringParameterArrayOut",
        "EnterpriseCrmLoggingGwsFieldLimitsIn": "_integrations_416_EnterpriseCrmLoggingGwsFieldLimitsIn",
        "EnterpriseCrmLoggingGwsFieldLimitsOut": "_integrations_417_EnterpriseCrmLoggingGwsFieldLimitsOut",
        "GoogleCloudIntegrationsV1alphaStringParameterArrayIn": "_integrations_418_GoogleCloudIntegrationsV1alphaStringParameterArrayIn",
        "GoogleCloudIntegrationsV1alphaStringParameterArrayOut": "_integrations_419_GoogleCloudIntegrationsV1alphaStringParameterArrayOut",
        "GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseIn": "_integrations_420_GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseIn",
        "GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseOut": "_integrations_421_GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseOut",
        "EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn": "_integrations_422_EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn",
        "EnterpriseCrmFrontendsEventbusProtoTriggerConfigOut": "_integrations_423_EnterpriseCrmFrontendsEventbusProtoTriggerConfigOut",
        "GoogleCloudIntegrationsV1alphaSuspensionIn": "_integrations_424_GoogleCloudIntegrationsV1alphaSuspensionIn",
        "GoogleCloudIntegrationsV1alphaSuspensionOut": "_integrations_425_GoogleCloudIntegrationsV1alphaSuspensionOut",
        "EnterpriseCrmEventbusProtoCloudSchedulerConfigIn": "_integrations_426_EnterpriseCrmEventbusProtoCloudSchedulerConfigIn",
        "EnterpriseCrmEventbusProtoCloudSchedulerConfigOut": "_integrations_427_EnterpriseCrmEventbusProtoCloudSchedulerConfigOut",
        "GoogleCloudIntegrationsV1alphaIntegrationParameterIn": "_integrations_428_GoogleCloudIntegrationsV1alphaIntegrationParameterIn",
        "GoogleCloudIntegrationsV1alphaIntegrationParameterOut": "_integrations_429_GoogleCloudIntegrationsV1alphaIntegrationParameterOut",
        "GoogleCloudIntegrationsV1alphaRuntimeActionSchemaIn": "_integrations_430_GoogleCloudIntegrationsV1alphaRuntimeActionSchemaIn",
        "GoogleCloudIntegrationsV1alphaRuntimeActionSchemaOut": "_integrations_431_GoogleCloudIntegrationsV1alphaRuntimeActionSchemaOut",
        "GoogleProtobufEmptyIn": "_integrations_432_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_integrations_433_GoogleProtobufEmptyOut",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeIn": "_integrations_434_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeIn",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeOut": "_integrations_435_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeOut",
        "GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequestIn": "_integrations_436_GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequestIn",
        "GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequestOut": "_integrations_437_GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequestOut",
        "EnterpriseCrmEventbusProtoProtoFunctionIn": "_integrations_438_EnterpriseCrmEventbusProtoProtoFunctionIn",
        "EnterpriseCrmEventbusProtoProtoFunctionOut": "_integrations_439_EnterpriseCrmEventbusProtoProtoFunctionOut",
        "EnterpriseCrmEventbusProtoConnectorsGenericConnectorTaskConfigIn": "_integrations_440_EnterpriseCrmEventbusProtoConnectorsGenericConnectorTaskConfigIn",
        "EnterpriseCrmEventbusProtoConnectorsGenericConnectorTaskConfigOut": "_integrations_441_EnterpriseCrmEventbusProtoConnectorsGenericConnectorTaskConfigOut",
        "GoogleCloudIntegrationsV1alphaListExecutionsResponseIn": "_integrations_442_GoogleCloudIntegrationsV1alphaListExecutionsResponseIn",
        "GoogleCloudIntegrationsV1alphaListExecutionsResponseOut": "_integrations_443_GoogleCloudIntegrationsV1alphaListExecutionsResponseOut",
        "GoogleCloudIntegrationsV1alphaParameterMapIn": "_integrations_444_GoogleCloudIntegrationsV1alphaParameterMapIn",
        "GoogleCloudIntegrationsV1alphaParameterMapOut": "_integrations_445_GoogleCloudIntegrationsV1alphaParameterMapOut",
        "GoogleCloudConnectorsV1SslConfigIn": "_integrations_446_GoogleCloudConnectorsV1SslConfigIn",
        "GoogleCloudConnectorsV1SslConfigOut": "_integrations_447_GoogleCloudConnectorsV1SslConfigOut",
        "EnterpriseCrmEventbusStatsIn": "_integrations_448_EnterpriseCrmEventbusStatsIn",
        "EnterpriseCrmEventbusStatsOut": "_integrations_449_EnterpriseCrmEventbusStatsOut",
        "EnterpriseCrmEventbusProtoFieldMappingConfigIn": "_integrations_450_EnterpriseCrmEventbusProtoFieldMappingConfigIn",
        "EnterpriseCrmEventbusProtoFieldMappingConfigOut": "_integrations_451_EnterpriseCrmEventbusProtoFieldMappingConfigOut",
        "EnterpriseCrmEventbusProtoCloudKmsConfigIn": "_integrations_452_EnterpriseCrmEventbusProtoCloudKmsConfigIn",
        "EnterpriseCrmEventbusProtoCloudKmsConfigOut": "_integrations_453_EnterpriseCrmEventbusProtoCloudKmsConfigOut",
        "GoogleCloudIntegrationsV1alphaListAuthConfigsResponseIn": "_integrations_454_GoogleCloudIntegrationsV1alphaListAuthConfigsResponseIn",
        "GoogleCloudIntegrationsV1alphaListAuthConfigsResponseOut": "_integrations_455_GoogleCloudIntegrationsV1alphaListAuthConfigsResponseOut",
        "GoogleCloudIntegrationsV1alphaValueTypeIn": "_integrations_456_GoogleCloudIntegrationsV1alphaValueTypeIn",
        "GoogleCloudIntegrationsV1alphaValueTypeOut": "_integrations_457_GoogleCloudIntegrationsV1alphaValueTypeOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["EnterpriseCrmFrontendsEventbusProtoParamSpecEntryIn"] = t.struct(
        {
            "isOutput": t.boolean(),
            "protoDef": t.proxy(
                renames["EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionIn"]
            ).optional(),
            "isDeprecated": t.boolean().optional(),
            "collectionElementClassName": t.string().optional(),
            "className": t.string().optional(),
            "config": t.proxy(
                renames["EnterpriseCrmEventbusProtoParamSpecEntryConfigIn"]
            ).optional(),
            "jsonSchema": t.string().optional(),
            "key": t.string().optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn"]
            ).optional(),
            "dataType": t.string().optional(),
            "required": t.boolean().optional(),
            "validationRule": t.proxy(
                renames["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParamSpecEntryIn"])
    types["EnterpriseCrmFrontendsEventbusProtoParamSpecEntryOut"] = t.struct(
        {
            "isOutput": t.boolean(),
            "protoDef": t.proxy(
                renames["EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionOut"]
            ).optional(),
            "isDeprecated": t.boolean().optional(),
            "collectionElementClassName": t.string().optional(),
            "className": t.string().optional(),
            "config": t.proxy(
                renames["EnterpriseCrmEventbusProtoParamSpecEntryConfigOut"]
            ).optional(),
            "jsonSchema": t.string().optional(),
            "key": t.string().optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "dataType": t.string().optional(),
            "required": t.boolean().optional(),
            "validationRule": t.proxy(
                renames["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParamSpecEntryOut"])
    types["GoogleCloudIntegrationsV1alphaCoordinateIn"] = t.struct(
        {"y": t.integer(), "x": t.integer()}
    ).named(renames["GoogleCloudIntegrationsV1alphaCoordinateIn"])
    types["GoogleCloudIntegrationsV1alphaCoordinateOut"] = t.struct(
        {
            "y": t.integer(),
            "x": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCoordinateOut"])
    types["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseIn"] = t.struct(
        {"scriptId": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseIn"])
    types["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseOut"] = t.struct(
        {
            "scriptId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseOut"])
    types["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsIn"] = t.struct(
        {
            "audience": t.string().optional(),
            "subject": t.string().optional(),
            "issuer": t.string().optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsIn"])
    types["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsOut"] = t.struct(
        {
            "audience": t.string().optional(),
            "subject": t.string().optional(),
            "issuer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsOut"])
    types["EnterpriseCrmEventbusProtoEventBusPropertiesIn"] = t.struct(
        {
            "properties": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoPropertyEntryIn"])
            ).optional()
        }
    ).named(renames["EnterpriseCrmEventbusProtoEventBusPropertiesIn"])
    types["EnterpriseCrmEventbusProtoEventBusPropertiesOut"] = t.struct(
        {
            "properties": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoPropertyEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoEventBusPropertiesOut"])
    types["EnterpriseCrmEventbusProtoExternalTrafficIn"] = t.struct(
        {
            "source": t.string().optional(),
            "gcpProjectNumber": t.string().optional(),
            "location": t.string().optional(),
            "gcpProjectId": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoExternalTrafficIn"])
    types["EnterpriseCrmEventbusProtoExternalTrafficOut"] = t.struct(
        {
            "source": t.string().optional(),
            "gcpProjectNumber": t.string().optional(),
            "location": t.string().optional(),
            "gcpProjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoExternalTrafficOut"])
    types["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"] = t.struct(
        {
            "parameters": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"])
            ).optional()
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"])
    types["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"] = t.struct(
        {
            "parameters": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"])
    types["GoogleCloudIntegrationsV1alphaTakeoverEditLockResponseIn"] = t.struct(
        {
            "integrationVersion": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaIntegrationVersionIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaTakeoverEditLockResponseIn"])
    types["GoogleCloudIntegrationsV1alphaTakeoverEditLockResponseOut"] = t.struct(
        {
            "integrationVersion": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaTakeoverEditLockResponseOut"])
    types["EnterpriseCrmEventbusProtoCombinedConditionIn"] = t.struct(
        {
            "conditions": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoConditionIn"])
            ).optional()
        }
    ).named(renames["EnterpriseCrmEventbusProtoCombinedConditionIn"])
    types["EnterpriseCrmEventbusProtoCombinedConditionOut"] = t.struct(
        {
            "conditions": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoConditionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoCombinedConditionOut"])
    types["EnterpriseCrmEventbusProtoAttributesIn"] = t.struct(
        {
            "taskVisibility": t.array(t.string()).optional(),
            "logSettings": t.proxy(
                renames["EnterpriseCrmEventbusProtoLogSettingsIn"]
            ).optional(),
            "dataType": t.string().optional(),
            "searchable": t.string(),
            "isRequired": t.boolean(),
            "isSearchable": t.boolean().optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoValueTypeIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoAttributesIn"])
    types["EnterpriseCrmEventbusProtoAttributesOut"] = t.struct(
        {
            "taskVisibility": t.array(t.string()).optional(),
            "logSettings": t.proxy(
                renames["EnterpriseCrmEventbusProtoLogSettingsOut"]
            ).optional(),
            "dataType": t.string().optional(),
            "searchable": t.string(),
            "isRequired": t.boolean(),
            "isSearchable": t.boolean().optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoValueTypeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoAttributesOut"])
    types["GoogleCloudIntegrationsV1alphaIntParameterArrayIn"] = t.struct(
        {"intValues": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaIntParameterArrayIn"])
    types["GoogleCloudIntegrationsV1alphaIntParameterArrayOut"] = t.struct(
        {
            "intValues": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntParameterArrayOut"])
    types["EnterpriseCrmEventbusProtoStringFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoStringFunctionIn"])
    types["EnterpriseCrmEventbusProtoStringFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoStringFunctionOut"])
    types["GoogleCloudIntegrationsV1alphaSuccessPolicyIn"] = t.struct(
        {"finalState": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaSuccessPolicyIn"])
    types["GoogleCloudIntegrationsV1alphaSuccessPolicyOut"] = t.struct(
        {
            "finalState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSuccessPolicyOut"])
    types["EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotIn"] = t.struct(
        {
            "checkpointTaskNumber": t.string().optional(),
            "eventExecutionSnapshotMetadata": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataIn"
                ]
            ),
            "diffParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
            ).optional(),
            "taskName": t.string().optional(),
            "eventParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
            ).optional(),
            "conditionResults": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoConditionResultIn"])
            ).optional(),
            "eventExecutionSnapshotId": t.string().optional(),
            "eventExecutionInfoId": t.string().optional(),
            "snapshotTime": t.string().optional(),
            "taskExecutionDetails": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskExecutionDetailsIn"])
            ).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotIn"])
    types["EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotOut"] = t.struct(
        {
            "checkpointTaskNumber": t.string().optional(),
            "eventExecutionSnapshotMetadata": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataOut"
                ]
            ),
            "diffParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "taskName": t.string().optional(),
            "eventParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "conditionResults": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoConditionResultOut"])
            ).optional(),
            "eventExecutionSnapshotId": t.string().optional(),
            "eventExecutionInfoId": t.string().optional(),
            "snapshotTime": t.string().optional(),
            "taskExecutionDetails": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskExecutionDetailsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotOut"])
    types["EnterpriseCrmLoggingGwsSanitizeOptionsIn"] = t.struct(
        {
            "sanitizeType": t.string(),
            "isAlreadySanitized": t.boolean().optional(),
            "privacy": t.string(),
            "logType": t.array(t.string()).optional(),
        }
    ).named(renames["EnterpriseCrmLoggingGwsSanitizeOptionsIn"])
    types["EnterpriseCrmLoggingGwsSanitizeOptionsOut"] = t.struct(
        {
            "sanitizeType": t.string(),
            "isAlreadySanitized": t.boolean().optional(),
            "privacy": t.string(),
            "logType": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmLoggingGwsSanitizeOptionsOut"])
    types["GoogleCloudIntegrationsV1alphaAuthTokenIn"] = t.struct(
        {"token": t.string().optional(), "type": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaAuthTokenIn"])
    types["GoogleCloudIntegrationsV1alphaAuthTokenOut"] = t.struct(
        {
            "token": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaAuthTokenOut"])
    types["GoogleCloudIntegrationsV1alphaGenerateTokenResponseIn"] = t.struct(
        {"message": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaGenerateTokenResponseIn"])
    types["GoogleCloudIntegrationsV1alphaGenerateTokenResponseOut"] = t.struct(
        {
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaGenerateTokenResponseOut"])
    types["EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryIn"] = t.struct(
        {
            "protoDefName": t.string().optional(),
            "jsonSchema": t.string().optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn"]
            ).optional(),
            "protoDefPath": t.string().optional(),
            "key": t.string().optional(),
            "name": t.string().optional(),
            "producedBy": t.proxy(
                renames["EnterpriseCrmEventbusProtoNodeIdentifierIn"]
            ).optional(),
            "attributes": t.proxy(
                renames["EnterpriseCrmEventbusProtoAttributesIn"]
            ).optional(),
            "producer": t.string(),
            "inOutType": t.string().optional(),
            "children": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryIn"
                    ]
                )
            ).optional(),
            "isTransient": t.boolean().optional(),
            "dataType": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryIn"])
    types["EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryOut"] = t.struct(
        {
            "protoDefName": t.string().optional(),
            "jsonSchema": t.string().optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "protoDefPath": t.string().optional(),
            "key": t.string().optional(),
            "name": t.string().optional(),
            "producedBy": t.proxy(
                renames["EnterpriseCrmEventbusProtoNodeIdentifierOut"]
            ).optional(),
            "attributes": t.proxy(
                renames["EnterpriseCrmEventbusProtoAttributesOut"]
            ).optional(),
            "producer": t.string(),
            "inOutType": t.string().optional(),
            "children": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryOut"
                    ]
                )
            ).optional(),
            "isTransient": t.boolean().optional(),
            "dataType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryOut"])
    types["EnterpriseCrmEventbusStatsDimensionsIn"] = t.struct(
        {
            "enumFilterType": t.string().optional(),
            "taskNumber": t.string(),
            "warningEnumString": t.string(),
            "clientId": t.string(),
            "triggerId": t.string().optional(),
            "retryAttempt": t.string(),
            "taskName": t.string(),
            "errorEnumString": t.string(),
            "workflowId": t.string(),
            "workflowName": t.string(),
        }
    ).named(renames["EnterpriseCrmEventbusStatsDimensionsIn"])
    types["EnterpriseCrmEventbusStatsDimensionsOut"] = t.struct(
        {
            "enumFilterType": t.string().optional(),
            "taskNumber": t.string(),
            "warningEnumString": t.string(),
            "clientId": t.string(),
            "triggerId": t.string().optional(),
            "retryAttempt": t.string(),
            "taskName": t.string(),
            "errorEnumString": t.string(),
            "workflowId": t.string(),
            "workflowName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusStatsDimensionsOut"])
    types["GoogleCloudConnectorsV1EncryptionKeyIn"] = t.struct(
        {"kmsKeyName": t.string().optional(), "type": t.string().optional()}
    ).named(renames["GoogleCloudConnectorsV1EncryptionKeyIn"])
    types["GoogleCloudConnectorsV1EncryptionKeyOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1EncryptionKeyOut"])
    types["GoogleCloudIntegrationsV1alphaCancelExecutionResponseIn"] = t.struct(
        {"isCanceled": t.boolean().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaCancelExecutionResponseIn"])
    types["GoogleCloudIntegrationsV1alphaCancelExecutionResponseOut"] = t.struct(
        {
            "isCanceled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCancelExecutionResponseOut"])
    types["EnterpriseCrmEventbusProtoTransformExpressionIn"] = t.struct(
        {
            "initialValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseValueIn"]
            ).optional(),
            "transformationFunctions": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoFunctionIn"])
            ).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTransformExpressionIn"])
    types["EnterpriseCrmEventbusProtoTransformExpressionOut"] = t.struct(
        {
            "initialValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseValueOut"]
            ).optional(),
            "transformationFunctions": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoFunctionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTransformExpressionOut"])
    types["GoogleCloudIntegrationsV1alphaTaskExecutionDetailsIn"] = t.struct(
        {
            "taskNumber": t.string().optional(),
            "taskExecutionState": t.string().optional(),
            "taskAttemptStats": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaAttemptStatsIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaTaskExecutionDetailsIn"])
    types["GoogleCloudIntegrationsV1alphaTaskExecutionDetailsOut"] = t.struct(
        {
            "taskNumber": t.string().optional(),
            "taskExecutionState": t.string().optional(),
            "taskAttemptStats": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaAttemptStatsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaTaskExecutionDetailsOut"])
    types["EnterpriseCrmEventbusProtoTriggerCriteriaIn"] = t.struct(
        {
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersIn"]
            ).optional(),
            "condition": t.string(),
            "triggerCriteriaTaskImplementationClassName": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTriggerCriteriaIn"])
    types["EnterpriseCrmEventbusProtoTriggerCriteriaOut"] = t.struct(
        {
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersOut"]
            ).optional(),
            "condition": t.string(),
            "triggerCriteriaTaskImplementationClassName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTriggerCriteriaOut"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"] = t.struct(
        {
            "key": t.string().optional(),
            "dataType": t.string().optional(),
            "value": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"] = t.struct(
        {
            "key": t.string().optional(),
            "dataType": t.string().optional(),
            "value": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"])
    types["GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestIn"] = t.struct(
        {
            "triggerId": t.string(),
            "parameterEntries": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"])
            ).optional(),
            "inputParameters": t.struct({"_": t.string().optional()}).optional(),
            "scheduleTime": t.string().optional(),
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersIn"]
            ).optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestIn"])
    types["GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestOut"] = t.struct(
        {
            "triggerId": t.string(),
            "parameterEntries": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"])
            ).optional(),
            "inputParameters": t.struct({"_": t.string().optional()}).optional(),
            "scheduleTime": t.string().optional(),
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersOut"]
            ).optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestOut"])
    types["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn"] = t.struct(
        {
            "parameters": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryIn"
                    ]
                )
            ).optional()
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn"])
    types["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersOut"] = t.struct(
        {
            "parameters": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersOut"])
    types["EnterpriseCrmEventbusProtoEventExecutionSnapshotIn"] = t.struct(
        {
            "diffParams": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersIn"]
            ).optional(),
            "taskExecutionDetails": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskExecutionDetailsIn"])
            ).optional(),
            "eventExecutionInfoId": t.string().optional(),
            "checkpointTaskNumber": t.string().optional(),
            "eventParams": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersIn"]
            ).optional(),
            "taskName": t.string().optional(),
            "exceedMaxSize": t.boolean().optional(),
            "eventExecutionSnapshotMetadata": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataIn"
                ]
            ),
            "snapshotTime": t.string().optional(),
            "eventExecutionSnapshotId": t.string().optional(),
            "conditionResults": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoConditionResultIn"])
            ).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoEventExecutionSnapshotIn"])
    types["EnterpriseCrmEventbusProtoEventExecutionSnapshotOut"] = t.struct(
        {
            "diffParams": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersOut"]
            ).optional(),
            "taskExecutionDetails": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskExecutionDetailsOut"])
            ).optional(),
            "eventExecutionInfoId": t.string().optional(),
            "checkpointTaskNumber": t.string().optional(),
            "eventParams": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersOut"]
            ).optional(),
            "taskName": t.string().optional(),
            "exceedMaxSize": t.boolean().optional(),
            "eventExecutionSnapshotMetadata": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataOut"
                ]
            ),
            "snapshotTime": t.string().optional(),
            "eventExecutionSnapshotId": t.string().optional(),
            "conditionResults": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoConditionResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoEventExecutionSnapshotOut"])
    types["GoogleCloudIntegrationsV1alphaTaskConfigIn"] = t.struct(
        {
            "externalTaskType": t.string().optional(),
            "taskExecutionStrategy": t.string().optional(),
            "taskId": t.string(),
            "jsonValidationOption": t.string().optional(),
            "displayName": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCoordinateIn"]
            ).optional(),
            "synchronousCallFailurePolicy": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaFailurePolicyIn"]
            ).optional(),
            "errorCatcherId": t.string().optional(),
            "failurePolicy": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaFailurePolicyIn"]
            ).optional(),
            "task": t.string().optional(),
            "description": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "taskTemplate": t.string().optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "nextTasks": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaNextTaskIn"])
            ).optional(),
            "successPolicy": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuccessPolicyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaTaskConfigIn"])
    types["GoogleCloudIntegrationsV1alphaTaskConfigOut"] = t.struct(
        {
            "externalTaskType": t.string().optional(),
            "taskExecutionStrategy": t.string().optional(),
            "taskId": t.string(),
            "jsonValidationOption": t.string().optional(),
            "displayName": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCoordinateOut"]
            ).optional(),
            "synchronousCallFailurePolicy": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaFailurePolicyOut"]
            ).optional(),
            "errorCatcherId": t.string().optional(),
            "failurePolicy": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaFailurePolicyOut"]
            ).optional(),
            "task": t.string().optional(),
            "description": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "taskTemplate": t.string().optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "nextTasks": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaNextTaskOut"])
            ).optional(),
            "successPolicy": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuccessPolicyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaTaskConfigOut"])
    types["EnterpriseCrmEventbusProtoTaskExecutionDetailsIn"] = t.struct(
        {
            "taskExecutionState": t.string(),
            "taskNumber": t.string().optional(),
            "taskAttemptStats": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsIn"
                    ]
                )
            ),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskExecutionDetailsIn"])
    types["EnterpriseCrmEventbusProtoTaskExecutionDetailsOut"] = t.struct(
        {
            "taskExecutionState": t.string(),
            "taskNumber": t.string().optional(),
            "taskAttemptStats": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsOut"
                    ]
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskExecutionDetailsOut"])
    types["EnterpriseCrmEventbusProtoIntArrayFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoIntArrayFunctionIn"])
    types["EnterpriseCrmEventbusProtoIntArrayFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoIntArrayFunctionOut"])
    types["EnterpriseCrmEventbusProtoParameterMapFieldIn"] = t.struct(
        {
            "literalValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeIn"]
            ).optional(),
            "referenceKey": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParameterMapFieldIn"])
    types["EnterpriseCrmEventbusProtoParameterMapFieldOut"] = t.struct(
        {
            "literalValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "referenceKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParameterMapFieldOut"])
    types["EnterpriseCrmEventbusProtoTaskAlertConfigIn"] = t.struct(
        {
            "thresholdValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueIn"]
            ).optional(),
            "metricType": t.string(),
            "thresholdType": t.string().optional(),
            "clientId": t.string().optional(),
            "alertName": t.string().optional(),
            "alertDisabled": t.boolean().optional(),
            "aggregationPeriod": t.string().optional(),
            "errorEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn"]
            ),
            "numAggregationPeriods": t.integer().optional(),
            "onlyFinalAttempt": t.boolean().optional(),
            "warningEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn"]
            ),
            "durationThresholdMs": t.string().optional(),
            "playbookUrl": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskAlertConfigIn"])
    types["EnterpriseCrmEventbusProtoTaskAlertConfigOut"] = t.struct(
        {
            "thresholdValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueOut"]
            ).optional(),
            "metricType": t.string(),
            "thresholdType": t.string().optional(),
            "clientId": t.string().optional(),
            "alertName": t.string().optional(),
            "alertDisabled": t.boolean().optional(),
            "aggregationPeriod": t.string().optional(),
            "errorEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut"]
            ),
            "numAggregationPeriods": t.integer().optional(),
            "onlyFinalAttempt": t.boolean().optional(),
            "warningEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut"]
            ),
            "durationThresholdMs": t.string().optional(),
            "playbookUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskAlertConfigOut"])
    types["GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponseIn"] = t.struct(
        {"projectId": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponseIn"])
    types[
        "GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponseOut"
    ] = t.struct(
        {
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponseOut"]
    )
    types["EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsIn"] = t.struct(
        {
            "eventExecutionState": t.string().optional(),
            "eventExecutionSnapshot": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotIn"
                    ]
                )
            ).optional(),
            "networkAddress": t.string().optional(),
            "nextExecutionTime": t.string().optional(),
            "eventAttemptStats": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsIn"
                    ]
                )
            ),
            "ryeLockUnheldCount": t.integer().optional(),
            "eventRetriesFromBeginningCount": t.integer().optional(),
            "logFilePath": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsIn"])
    types["EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsOut"] = t.struct(
        {
            "eventExecutionState": t.string().optional(),
            "eventExecutionSnapshot": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotOut"
                    ]
                )
            ).optional(),
            "networkAddress": t.string().optional(),
            "nextExecutionTime": t.string().optional(),
            "eventAttemptStats": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsOut"
                    ]
                )
            ),
            "ryeLockUnheldCount": t.integer().optional(),
            "eventRetriesFromBeginningCount": t.integer().optional(),
            "logFilePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsOut"])
    types["EnterpriseCrmEventbusProtoTeardownTaskConfigIn"] = t.struct(
        {
            "creatorEmail": t.string().optional(),
            "teardownTaskImplementationClassName": t.string(),
            "properties": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventBusPropertiesIn"]
            ),
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersIn"]
            ).optional(),
            "name": t.string(),
            "nextTeardownTask": t.proxy(
                renames["EnterpriseCrmEventbusProtoNextTeardownTaskIn"]
            ),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTeardownTaskConfigIn"])
    types["EnterpriseCrmEventbusProtoTeardownTaskConfigOut"] = t.struct(
        {
            "creatorEmail": t.string().optional(),
            "teardownTaskImplementationClassName": t.string(),
            "properties": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventBusPropertiesOut"]
            ),
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersOut"]
            ).optional(),
            "name": t.string(),
            "nextTeardownTask": t.proxy(
                renames["EnterpriseCrmEventbusProtoNextTeardownTaskOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTeardownTaskConfigOut"])
    types["GoogleCloudIntegrationsV1alphaUsernameAndPasswordIn"] = t.struct(
        {"username": t.string().optional(), "password": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaUsernameAndPasswordIn"])
    types["GoogleCloudIntegrationsV1alphaUsernameAndPasswordOut"] = t.struct(
        {
            "username": t.string().optional(),
            "password": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaUsernameAndPasswordOut"])
    types["GoogleCloudIntegrationsV1alphaCancelExecutionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaCancelExecutionRequestIn"])
    types["GoogleCloudIntegrationsV1alphaCancelExecutionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaCancelExecutionRequestOut"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterMapIn"] = t.struct(
        {
            "valueType": t.string(),
            "keyType": t.string().optional(),
            "entries": t.array(
                t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoParameterMapEntryIn"]
                )
            ),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterMapIn"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterMapOut"] = t.struct(
        {
            "valueType": t.string(),
            "keyType": t.string().optional(),
            "entries": t.array(
                t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoParameterMapEntryOut"]
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterMapOut"])
    types["GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseIn"] = t.struct(
        {
            "sfdcChannels": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcChannelIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseIn"])
    types["GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseOut"] = t.struct(
        {
            "sfdcChannels": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseOut"])
    types["EnterpriseCrmEventbusProtoStringArrayFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoStringArrayFunctionIn"])
    types["EnterpriseCrmEventbusProtoStringArrayFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoStringArrayFunctionOut"])
    types["GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsIn"] = t.struct(
        {
            "clientSecret": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
            "clientId": t.string().optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsIn"])
    types["GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsOut"] = t.struct(
        {
            "clientSecret": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "clientId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsOut"])
    types["EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterIn"] = t.struct(
        {"objectValue": t.string()}
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterIn"])
    types["EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterOut"] = t.struct(
        {
            "objectValue": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterOut"])
    types["EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionIn"] = t.struct(
        {"fullName": t.string().optional(), "path": t.string().optional()}
    ).named(renames["EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionIn"])
    types["EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionOut"] = t.struct(
        {
            "fullName": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionOut"])
    types["GoogleCloudIntegrationsV1alphaClientCertificateIn"] = t.struct(
        {
            "sslCertificate": t.string().optional(),
            "passphrase": t.string().optional(),
            "encryptedPrivateKey": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaClientCertificateIn"])
    types["GoogleCloudIntegrationsV1alphaClientCertificateOut"] = t.struct(
        {
            "sslCertificate": t.string().optional(),
            "passphrase": t.string().optional(),
            "encryptedPrivateKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaClientCertificateOut"])
    types["GoogleCloudIntegrationsV1alphaJwtIn"] = t.struct(
        {
            "jwtHeader": t.string().optional(),
            "secret": t.string().optional(),
            "jwt": t.string().optional(),
            "jwtPayload": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaJwtIn"])
    types["GoogleCloudIntegrationsV1alphaJwtOut"] = t.struct(
        {
            "jwtHeader": t.string().optional(),
            "secret": t.string().optional(),
            "jwt": t.string().optional(),
            "jwtPayload": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaJwtOut"])
    types["EnterpriseCrmEventbusProtoJsonFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoJsonFunctionIn"])
    types["EnterpriseCrmEventbusProtoJsonFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoJsonFunctionOut"])
    types["EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayIn"] = t.struct(
        {"booleanValues": t.array(t.boolean())}
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayIn"])
    types["EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayOut"] = t.struct(
        {
            "booleanValues": t.array(t.boolean()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayOut"])
    types[
        "GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataIn"
    ] = t.struct(
        {
            "taskLabel": t.string().optional(),
            "task": t.string().optional(),
            "executionAttempt": t.integer().optional(),
            "taskNumber": t.string().optional(),
            "taskAttempt": t.integer().optional(),
        }
    ).named(
        renames[
            "GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataIn"
        ]
    )
    types[
        "GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataOut"
    ] = t.struct(
        {
            "taskLabel": t.string().optional(),
            "task": t.string().optional(),
            "executionAttempt": t.integer().optional(),
            "taskNumber": t.string().optional(),
            "taskAttempt": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataOut"
        ]
    )
    types["GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowIn"] = t.struct(
        {
            "clientId": t.string().optional(),
            "pkceVerifier": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "redirectUri": t.string().optional(),
            "authUri": t.string().optional(),
            "authCode": t.string().optional(),
            "enablePkce": t.boolean().optional(),
            "clientSecret": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowIn"])
    types["GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowOut"] = t.struct(
        {
            "clientId": t.string().optional(),
            "pkceVerifier": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "redirectUri": t.string().optional(),
            "authUri": t.string().optional(),
            "authCode": t.string().optional(),
            "enablePkce": t.boolean().optional(),
            "clientSecret": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowOut"])
    types[
        "GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseIn"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "integrationTemplateVersions": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionIn"
                    ]
                )
            ).optional(),
        }
    ).named(
        renames[
            "GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseIn"
        ]
    )
    types[
        "GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "integrationTemplateVersions": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseOut"
        ]
    )
    types["GoogleCloudConnectorsV1LockConfigIn"] = t.struct(
        {"reason": t.string().optional(), "locked": t.boolean().optional()}
    ).named(renames["GoogleCloudConnectorsV1LockConfigIn"])
    types["GoogleCloudConnectorsV1LockConfigOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "locked": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1LockConfigOut"])
    types[
        "EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsIn"
    ] = t.struct(
        {"endTime": t.string().optional(), "startTime": t.string().optional()}
    ).named(
        renames["EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsIn"]
    )
    types[
        "EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsOut"
    ] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsOut"]
    )
    types["EnterpriseCrmEventbusProtoNotificationIn"] = t.struct(
        {
            "escalatorQueue": t.string(),
            "pubsubTopic": t.string(),
            "emailAddress": t.proxy(renames["EnterpriseCrmEventbusProtoAddressIn"]),
            "buganizerNotification": t.proxy(
                renames["EnterpriseCrmEventbusProtoBuganizerNotificationIn"]
            ),
            "request": t.proxy(
                renames["EnterpriseCrmEventbusProtoCustomSuspensionRequestIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoNotificationIn"])
    types["EnterpriseCrmEventbusProtoNotificationOut"] = t.struct(
        {
            "escalatorQueue": t.string(),
            "pubsubTopic": t.string(),
            "emailAddress": t.proxy(renames["EnterpriseCrmEventbusProtoAddressOut"]),
            "buganizerNotification": t.proxy(
                renames["EnterpriseCrmEventbusProtoBuganizerNotificationOut"]
            ),
            "request": t.proxy(
                renames["EnterpriseCrmEventbusProtoCustomSuspensionRequestOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoNotificationOut"])
    types["GoogleCloudConnectorsV1AuthConfigSshPublicKeyIn"] = t.struct(
        {
            "certType": t.string().optional(),
            "sshClientCert": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
            "username": t.string().optional(),
            "sshClientCertPass": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigSshPublicKeyIn"])
    types["GoogleCloudConnectorsV1AuthConfigSshPublicKeyOut"] = t.struct(
        {
            "certType": t.string().optional(),
            "sshClientCert": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "username": t.string().optional(),
            "sshClientCertPass": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigSshPublicKeyOut"])
    types["GoogleCloudIntegrationsV1alphaNextTaskIn"] = t.struct(
        {
            "condition": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "taskConfigId": t.string().optional(),
            "taskId": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaNextTaskIn"])
    types["GoogleCloudIntegrationsV1alphaNextTaskOut"] = t.struct(
        {
            "condition": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "taskConfigId": t.string().optional(),
            "taskId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaNextTaskOut"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn"] = t.struct(
        {
            "stringArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoStringParameterArrayIn"]
            ),
            "intArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoIntParameterArrayIn"]
            ),
            "jsonValue": t.string(),
            "booleanArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayIn"]
            ),
            "doubleArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayIn"]
            ),
            "intValue": t.string(),
            "doubleValue": t.number(),
            "protoValue": t.struct({"_": t.string().optional()}),
            "serializedObjectValue": t.proxy(
                renames[
                    "EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterIn"
                ]
            ),
            "stringValue": t.string(),
            "booleanValue": t.boolean(),
            "protoArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayIn"]
            ),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut"] = t.struct(
        {
            "stringArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoStringParameterArrayOut"]
            ),
            "intArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoIntParameterArrayOut"]
            ),
            "jsonValue": t.string(),
            "booleanArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayOut"]
            ),
            "doubleArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayOut"]
            ),
            "intValue": t.string(),
            "doubleValue": t.number(),
            "protoValue": t.struct({"_": t.string().optional()}),
            "serializedObjectValue": t.proxy(
                renames[
                    "EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterOut"
                ]
            ),
            "stringValue": t.string(),
            "booleanValue": t.boolean(),
            "protoArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut"])
    types["EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageIn"] = t.struct(
        {
            "parameters": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParamSpecEntryIn"])
            )
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageIn"])
    types["EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageOut"] = t.struct(
        {
            "parameters": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParamSpecEntryOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageOut"])
    types["EnterpriseCrmEventbusProtoStringArrayIn"] = t.struct(
        {"values": t.array(t.string())}
    ).named(renames["EnterpriseCrmEventbusProtoStringArrayIn"])
    types["EnterpriseCrmEventbusProtoStringArrayOut"] = t.struct(
        {
            "values": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoStringArrayOut"])
    types["GoogleCloudIntegrationsV1alphaResolveSuspensionRequestIn"] = t.struct(
        {
            "suspension": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuspensionIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaResolveSuspensionRequestIn"])
    types["GoogleCloudIntegrationsV1alphaResolveSuspensionRequestOut"] = t.struct(
        {
            "suspension": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuspensionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaResolveSuspensionRequestOut"])
    types["EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueIn"] = t.struct(
        {"percentage": t.integer(), "absolute": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueIn"])
    types["EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueOut"] = t.struct(
        {
            "percentage": t.integer(),
            "absolute": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueOut"])
    types[
        "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityIn"
    ] = t.struct({"gaiaId": t.string(), "emailAddress": t.string()}).named(
        renames["EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityIn"]
    )
    types[
        "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityOut"
    ] = t.struct(
        {
            "gaiaId": t.string(),
            "emailAddress": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityOut"]
    )
    types["GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn"] = t.struct(
        {
            "errorCatcherNumber": t.string(),
            "startErrorTasks": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaNextTaskIn"])
            ),
            "label": t.string().optional(),
            "description": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCoordinateIn"]
            ).optional(),
            "errorCatcherId": t.string(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn"])
    types["GoogleCloudIntegrationsV1alphaErrorCatcherConfigOut"] = t.struct(
        {
            "errorCatcherNumber": t.string(),
            "startErrorTasks": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaNextTaskOut"])
            ),
            "label": t.string().optional(),
            "description": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCoordinateOut"]
            ).optional(),
            "errorCatcherId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigOut"])
    types["GoogleCloudIntegrationsV1alphaExecutionDetailsIn"] = t.struct(
        {
            "attemptStats": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaAttemptStatsIn"])
            ).optional(),
            "executionSnapshots": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaExecutionSnapshotIn"])
            ).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecutionDetailsIn"])
    types["GoogleCloudIntegrationsV1alphaExecutionDetailsOut"] = t.struct(
        {
            "attemptStats": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaAttemptStatsOut"])
            ).optional(),
            "executionSnapshots": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaExecutionSnapshotOut"])
            ).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecutionDetailsOut"])
    types["EnterpriseCrmEventbusProtoBaseValueIn"] = t.struct(
        {
            "baseFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoFunctionIn"]
            ).optional(),
            "literalValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeIn"]
            ).optional(),
            "referenceValue": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBaseValueIn"])
    types["EnterpriseCrmEventbusProtoBaseValueOut"] = t.struct(
        {
            "baseFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoFunctionOut"]
            ).optional(),
            "literalValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "referenceValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBaseValueOut"])
    types["GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigIn"] = t.struct(
        {
            "emailAddresses": t.array(t.string()).optional(),
            "expiration": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationIn"]
            ).optional(),
            "customMessage": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigIn"])
    types["GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigOut"] = t.struct(
        {
            "emailAddresses": t.array(t.string()).optional(),
            "expiration": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationOut"]
            ).optional(),
            "customMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigOut"])
    types["GoogleCloudIntegrationsV1alphaListCertificatesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "certificates": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaCertificateIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListCertificatesResponseIn"])
    types["GoogleCloudIntegrationsV1alphaListCertificatesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "certificates": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaCertificateOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListCertificatesResponseOut"])
    types["GoogleCloudIntegrationsV1alphaCertificateIn"] = t.struct(
        {
            "certificateStatus": t.string().optional(),
            "credentialId": t.string().optional(),
            "requestorId": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "rawCertificate": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaClientCertificateIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCertificateIn"])
    types["GoogleCloudIntegrationsV1alphaCertificateOut"] = t.struct(
        {
            "validStartTime": t.string().optional(),
            "certificateStatus": t.string().optional(),
            "credentialId": t.string().optional(),
            "requestorId": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "rawCertificate": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaClientCertificateOut"]
            ).optional(),
            "validEndTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCertificateOut"])
    types["EnterpriseCrmEventbusProtoValueTypeIn"] = t.struct(
        {
            "doubleArray": t.proxy(renames["EnterpriseCrmEventbusProtoDoubleArrayIn"]),
            "stringValue": t.string(),
            "protoValue": t.struct({"_": t.string().optional()}),
            "intValue": t.string(),
            "intArray": t.proxy(renames["EnterpriseCrmEventbusProtoIntArrayIn"]),
            "stringArray": t.proxy(renames["EnterpriseCrmEventbusProtoStringArrayIn"]),
            "doubleValue": t.number(),
            "booleanValue": t.boolean(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoValueTypeIn"])
    types["EnterpriseCrmEventbusProtoValueTypeOut"] = t.struct(
        {
            "doubleArray": t.proxy(renames["EnterpriseCrmEventbusProtoDoubleArrayOut"]),
            "stringValue": t.string(),
            "protoValue": t.struct({"_": t.string().optional()}),
            "intValue": t.string(),
            "intArray": t.proxy(renames["EnterpriseCrmEventbusProtoIntArrayOut"]),
            "stringArray": t.proxy(renames["EnterpriseCrmEventbusProtoStringArrayOut"]),
            "doubleValue": t.number(),
            "booleanValue": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoValueTypeOut"])
    types["GoogleCloudIntegrationsV1alphaAttemptStatsIn"] = t.struct(
        {"endTime": t.string().optional(), "startTime": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaAttemptStatsIn"])
    types["GoogleCloudIntegrationsV1alphaAttemptStatsOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaAttemptStatsOut"])
    types["GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseIn"] = t.struct(
        {"executionInfoIds": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseIn"])
    types["GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseOut"] = t.struct(
        {
            "executionInfoIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseOut"])
    types["EnterpriseCrmFrontendsEventbusProtoRollbackStrategyIn"] = t.struct(
        {
            "taskNumbersToRollback": t.array(t.string()),
            "parameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
            ).optional(),
            "rollbackTaskImplementationClassName": t.string(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoRollbackStrategyIn"])
    types["EnterpriseCrmFrontendsEventbusProtoRollbackStrategyOut"] = t.struct(
        {
            "taskNumbersToRollback": t.array(t.string()),
            "parameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "rollbackTaskImplementationClassName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoRollbackStrategyOut"])
    types["GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsIn"] = t.struct(
        {
            "requestType": t.string().optional(),
            "tokenEndpoint": t.string().optional(),
            "scope": t.string().optional(),
            "accessToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAccessTokenIn"]
            ).optional(),
            "tokenParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapIn"]
            ).optional(),
            "clientSecret": t.string().optional(),
            "clientId": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsIn"])
    types["GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsOut"] = t.struct(
        {
            "requestType": t.string().optional(),
            "tokenEndpoint": t.string().optional(),
            "scope": t.string().optional(),
            "accessToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAccessTokenOut"]
            ).optional(),
            "tokenParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapOut"]
            ).optional(),
            "clientSecret": t.string().optional(),
            "clientId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsOut"])
    types["EnterpriseCrmEventbusProtoDoubleArrayIn"] = t.struct(
        {"values": t.array(t.number())}
    ).named(renames["EnterpriseCrmEventbusProtoDoubleArrayIn"])
    types["EnterpriseCrmEventbusProtoDoubleArrayOut"] = t.struct(
        {
            "values": t.array(t.number()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoDoubleArrayOut"])
    types["GoogleCloudConnectorsV1ConnectionStatusIn"] = t.struct(
        {
            "status": t.string().optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1ConnectionStatusIn"])
    types["GoogleCloudConnectorsV1ConnectionStatusOut"] = t.struct(
        {
            "status": t.string().optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1ConnectionStatusOut"])
    types["EnterpriseCrmEventbusProtoParameterMapIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoParameterMapEntryIn"])
            ),
            "keyType": t.string().optional(),
            "valueType": t.string(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParameterMapIn"])
    types["EnterpriseCrmEventbusProtoParameterMapOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoParameterMapEntryOut"])
            ),
            "keyType": t.string().optional(),
            "valueType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParameterMapOut"])
    types[
        "GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequestIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequestIn"]
    )
    types[
        "GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequestOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames["GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequestOut"]
    )
    types["EnterpriseCrmEventbusProtoNextTeardownTaskIn"] = t.struct(
        {"name": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoNextTeardownTaskIn"])
    types["EnterpriseCrmEventbusProtoNextTeardownTaskOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EnterpriseCrmEventbusProtoNextTeardownTaskOut"])
    types["GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationIn"] = t.struct(
        {"remindTime": t.string().optional(), "liftWhenExpired": t.boolean().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationIn"])
    types["GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "remindTime": t.string().optional(),
            "liftWhenExpired": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationOut"])
    types["EnterpriseCrmEventbusProtoLogSettingsIn"] = t.struct(
        {
            "logFieldName": t.string().optional(),
            "seedPeriod": t.string(),
            "shorteningLimits": t.proxy(
                renames["EnterpriseCrmLoggingGwsFieldLimitsIn"]
            ).optional(),
            "seedScope": t.string(),
            "sanitizeOptions": t.proxy(
                renames["EnterpriseCrmLoggingGwsSanitizeOptionsIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoLogSettingsIn"])
    types["EnterpriseCrmEventbusProtoLogSettingsOut"] = t.struct(
        {
            "logFieldName": t.string().optional(),
            "seedPeriod": t.string(),
            "shorteningLimits": t.proxy(
                renames["EnterpriseCrmLoggingGwsFieldLimitsOut"]
            ).optional(),
            "seedScope": t.string(),
            "sanitizeOptions": t.proxy(
                renames["EnterpriseCrmLoggingGwsSanitizeOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoLogSettingsOut"])
    types["EnterpriseCrmEventbusProtoIntParameterArrayIn"] = t.struct(
        {"intValues": t.array(t.string())}
    ).named(renames["EnterpriseCrmEventbusProtoIntParameterArrayIn"])
    types["EnterpriseCrmEventbusProtoIntParameterArrayOut"] = t.struct(
        {
            "intValues": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoIntParameterArrayOut"])
    types["EnterpriseCrmEventbusProtoBaseFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoBaseFunctionIn"])
    types["EnterpriseCrmEventbusProtoBaseFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBaseFunctionOut"])
    types["GoogleCloudIntegrationsV1alphaLiftSuspensionRequestIn"] = t.struct(
        {"suspensionResult": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaLiftSuspensionRequestIn"])
    types["GoogleCloudIntegrationsV1alphaLiftSuspensionRequestOut"] = t.struct(
        {
            "suspensionResult": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaLiftSuspensionRequestOut"])
    types["EnterpriseCrmEventbusProtoErrorDetailIn"] = t.struct(
        {
            "errorCode": t.proxy(renames["CrmlogErrorCodeIn"]).optional(),
            "errorMessage": t.string().optional(),
            "severity": t.string().optional(),
            "taskNumber": t.integer().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoErrorDetailIn"])
    types["EnterpriseCrmEventbusProtoErrorDetailOut"] = t.struct(
        {
            "errorCode": t.proxy(renames["CrmlogErrorCodeOut"]).optional(),
            "errorMessage": t.string().optional(),
            "severity": t.string().optional(),
            "taskNumber": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoErrorDetailOut"])
    types["GoogleCloudIntegrationsV1alphaListConnectionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "connections": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConnectionIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListConnectionsResponseIn"])
    types["GoogleCloudIntegrationsV1alphaListConnectionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "connections": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConnectionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListConnectionsResponseOut"])
    types["GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestIn"] = t.struct(
        {
            "inputParameters": t.struct({"_": t.string().optional()}).optional(),
            "doNotPropagateError": t.boolean().optional(),
            "parameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
            ).optional(),
            "triggerId": t.string(),
            "executionId": t.string().optional(),
            "parameterEntries": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"])
            ).optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestIn"])
    types["GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestOut"] = t.struct(
        {
            "inputParameters": t.struct({"_": t.string().optional()}).optional(),
            "doNotPropagateError": t.boolean().optional(),
            "parameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "triggerId": t.string(),
            "executionId": t.string().optional(),
            "parameterEntries": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"])
            ).optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestOut"])
    types["EnterpriseCrmEventbusProtoTaskMetadataIn"] = t.struct(
        {
            "status": t.string().optional(),
            "codeSearchLink": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "defaultJsonValidationOption": t.string().optional(),
            "isDeprecated": t.boolean().optional(),
            "iconLink": t.string().optional(),
            "activeTaskName": t.string().optional(),
            "g3DocLink": t.string().optional(),
            "name": t.string().optional(),
            "externalDocMarkdown": t.string().optional(),
            "standaloneExternalDocHtml": t.string().optional(),
            "externalDocHtml": t.string().optional(),
            "category": t.string(),
            "externalCategory": t.string(),
            "externalDocLink": t.string().optional(),
            "descriptiveName": t.string().optional(),
            "docMarkdown": t.string().optional(),
            "defaultSpec": t.string().optional(),
            "description": t.string().optional(),
            "system": t.string(),
            "externalCategorySequence": t.integer().optional(),
            "admins": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskMetadataAdminIn"])
            ),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskMetadataIn"])
    types["EnterpriseCrmEventbusProtoTaskMetadataOut"] = t.struct(
        {
            "status": t.string().optional(),
            "codeSearchLink": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "defaultJsonValidationOption": t.string().optional(),
            "isDeprecated": t.boolean().optional(),
            "iconLink": t.string().optional(),
            "activeTaskName": t.string().optional(),
            "g3DocLink": t.string().optional(),
            "name": t.string().optional(),
            "externalDocMarkdown": t.string().optional(),
            "standaloneExternalDocHtml": t.string().optional(),
            "externalDocHtml": t.string().optional(),
            "category": t.string(),
            "externalCategory": t.string(),
            "externalDocLink": t.string().optional(),
            "descriptiveName": t.string().optional(),
            "docMarkdown": t.string().optional(),
            "defaultSpec": t.string().optional(),
            "description": t.string().optional(),
            "system": t.string(),
            "externalCategorySequence": t.integer().optional(),
            "admins": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskMetadataAdminOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskMetadataOut"])
    types["EnterpriseCrmEventbusProtoSuccessPolicyIn"] = t.struct(
        {"finalState": t.string().optional()}
    ).named(renames["EnterpriseCrmEventbusProtoSuccessPolicyIn"])
    types["EnterpriseCrmEventbusProtoSuccessPolicyOut"] = t.struct(
        {
            "finalState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuccessPolicyOut"])
    types[
        "GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseIn"
    ] = t.struct({"content": t.string().optional()}).named(
        renames["GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseIn"]
    )
    types[
        "GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseOut"
    ] = t.struct(
        {
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseOut"]
    )
    types["GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequestIn"] = t.struct(
        {"content": t.string().optional(), "fileFormat": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequestIn"])
    types[
        "GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequestOut"
    ] = t.struct(
        {
            "content": t.string().optional(),
            "fileFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequestOut"]
    )
    types[
        "EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsIn"
    ] = t.struct(
        {"startTime": t.string().optional(), "endTime": t.string().optional()}
    ).named(
        renames["EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsIn"]
    )
    types[
        "EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsOut"
    ] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsOut"]
    )
    types["GoogleCloudIntegrationsV1alphaSuspensionAuditIn"] = t.struct(
        {"resolver": t.string().optional(), "resolveTime": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaSuspensionAuditIn"])
    types["GoogleCloudIntegrationsV1alphaSuspensionAuditOut"] = t.struct(
        {
            "resolver": t.string().optional(),
            "resolveTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSuspensionAuditOut"])
    types["EnterpriseCrmEventbusProtoNodeIdentifierIn"] = t.struct(
        {
            "elementIdentifier": t.string().optional(),
            "elementType": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoNodeIdentifierIn"])
    types["EnterpriseCrmEventbusProtoNodeIdentifierOut"] = t.struct(
        {
            "elementIdentifier": t.string().optional(),
            "elementType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoNodeIdentifierOut"])
    types["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerIn"] = t.struct(
        {
            "jwtClaims": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsIn"]
            ).optional(),
            "clientKey": t.proxy(renames["GoogleCloudConnectorsV1SecretIn"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerIn"])
    types["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerOut"] = t.struct(
        {
            "jwtClaims": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsOut"]
            ).optional(),
            "clientKey": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerOut"])
    types["EnterpriseCrmEventbusProtoEventParametersIn"] = t.struct(
        {
            "parameters": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoParameterEntryIn"])
            ).optional()
        }
    ).named(renames["EnterpriseCrmEventbusProtoEventParametersIn"])
    types["EnterpriseCrmEventbusProtoEventParametersOut"] = t.struct(
        {
            "parameters": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoParameterEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoEventParametersOut"])
    types["EnterpriseCrmEventbusProtoSuspensionResolutionInfoIn"] = t.struct(
        {
            "createdTimestamp": t.string().optional(),
            "eventExecutionInfoId": t.string(),
            "suspensionId": t.string().optional(),
            "lastModifiedTimestamp": t.string().optional(),
            "suspensionConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionConfigIn"]
            ),
            "product": t.string().optional(),
            "workflowName": t.string(),
            "externalTraffic": t.proxy(
                renames["EnterpriseCrmEventbusProtoExternalTrafficIn"]
            ).optional(),
            "cloudKmsConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoCloudKmsConfigIn"]
            ).optional(),
            "audit": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditIn"]
            ),
            "wrappedDek": t.string().optional(),
            "clientId": t.string().optional(),
            "encryptedSuspensionResolutionInfo": t.string().optional(),
            "taskNumber": t.string(),
            "status": t.string(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionResolutionInfoIn"])
    types["EnterpriseCrmEventbusProtoSuspensionResolutionInfoOut"] = t.struct(
        {
            "createdTimestamp": t.string().optional(),
            "eventExecutionInfoId": t.string(),
            "suspensionId": t.string().optional(),
            "lastModifiedTimestamp": t.string().optional(),
            "suspensionConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionConfigOut"]
            ),
            "product": t.string().optional(),
            "workflowName": t.string(),
            "externalTraffic": t.proxy(
                renames["EnterpriseCrmEventbusProtoExternalTrafficOut"]
            ).optional(),
            "cloudKmsConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoCloudKmsConfigOut"]
            ).optional(),
            "audit": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditOut"]
            ),
            "wrappedDek": t.string().optional(),
            "clientId": t.string().optional(),
            "encryptedSuspensionResolutionInfo": t.string().optional(),
            "taskNumber": t.string(),
            "status": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionResolutionInfoOut"])
    types["GoogleCloudConnectorsV1LogConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["GoogleCloudConnectorsV1LogConfigIn"])
    types["GoogleCloudConnectorsV1LogConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1LogConfigOut"])
    types["EnterpriseCrmEventbusProtoConditionIn"] = t.struct(
        {
            "value": t.proxy(
                renames["EnterpriseCrmEventbusProtoValueTypeIn"]
            ).optional(),
            "operator": t.string().optional(),
            "eventPropertyKey": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoConditionIn"])
    types["EnterpriseCrmEventbusProtoConditionOut"] = t.struct(
        {
            "value": t.proxy(
                renames["EnterpriseCrmEventbusProtoValueTypeOut"]
            ).optional(),
            "operator": t.string().optional(),
            "eventPropertyKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoConditionOut"])
    types["EnterpriseCrmEventbusProtoConditionResultIn"] = t.struct(
        {
            "currentTaskNumber": t.string().optional(),
            "nextTaskNumber": t.string().optional(),
            "result": t.boolean().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoConditionResultIn"])
    types["EnterpriseCrmEventbusProtoConditionResultOut"] = t.struct(
        {
            "currentTaskNumber": t.string().optional(),
            "nextTaskNumber": t.string().optional(),
            "result": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoConditionResultOut"])
    types["GoogleCloudConnectorsV1NodeConfigIn"] = t.struct(
        {"maxNodeCount": t.integer().optional(), "minNodeCount": t.integer().optional()}
    ).named(renames["GoogleCloudConnectorsV1NodeConfigIn"])
    types["GoogleCloudConnectorsV1NodeConfigOut"] = t.struct(
        {
            "maxNodeCount": t.integer().optional(),
            "minNodeCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1NodeConfigOut"])
    types["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn"] = t.struct(
        {"enumStrings": t.array(t.string()), "filterType": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn"])
    types["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut"] = t.struct(
        {
            "enumStrings": t.array(t.string()),
            "filterType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut"])
    types["EnterpriseCrmEventbusProtoSerializedObjectParameterIn"] = t.struct(
        {"objectValue": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoSerializedObjectParameterIn"])
    types["EnterpriseCrmEventbusProtoSerializedObjectParameterOut"] = t.struct(
        {
            "objectValue": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSerializedObjectParameterOut"])
    types["GoogleCloudIntegrationsV1alphaExecutionIn"] = t.struct(
        {
            "requestParams": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"])
            ).optional(),
            "triggerId": t.string().optional(),
            "responseParameters": t.struct({"_": t.string().optional()}).optional(),
            "directSubExecutions": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaExecutionIn"])
            ).optional(),
            "name": t.string().optional(),
            "responseParams": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"])
            ).optional(),
            "executionMethod": t.string().optional(),
            "requestParameters": t.struct({"_": t.string().optional()}).optional(),
            "executionDetails": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaExecutionDetailsIn"]
            ).optional(),
            "eventExecutionDetails": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventExecutionDetailsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecutionIn"])
    types["GoogleCloudIntegrationsV1alphaExecutionOut"] = t.struct(
        {
            "requestParams": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"])
            ).optional(),
            "createTime": t.string().optional(),
            "triggerId": t.string().optional(),
            "responseParameters": t.struct({"_": t.string().optional()}).optional(),
            "directSubExecutions": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaExecutionOut"])
            ).optional(),
            "name": t.string().optional(),
            "responseParams": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"])
            ).optional(),
            "executionMethod": t.string().optional(),
            "requestParameters": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "executionDetails": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaExecutionDetailsOut"]
            ).optional(),
            "eventExecutionDetails": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventExecutionDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecutionOut"])
    types["EnterpriseCrmEventbusProtoExecutionTraceInfoIn"] = t.struct(
        {
            "traceId": t.string().optional(),
            "parentEventExecutionInfoId": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoExecutionTraceInfoIn"])
    types["EnterpriseCrmEventbusProtoExecutionTraceInfoOut"] = t.struct(
        {
            "traceId": t.string().optional(),
            "parentEventExecutionInfoId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoExecutionTraceInfoOut"])
    types["GoogleCloudConnectorsV1DestinationConfigIn"] = t.struct(
        {
            "key": t.string().optional(),
            "destinations": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1DestinationIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1DestinationConfigIn"])
    types["GoogleCloudConnectorsV1DestinationConfigOut"] = t.struct(
        {
            "key": t.string().optional(),
            "destinations": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1DestinationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1DestinationConfigOut"])
    types["EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "errorCode": t.proxy(renames["CrmlogErrorCodeIn"]).optional(),
            "eventExecutionDetails": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsIn"]
            ).optional(),
            "errors": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoErrorDetailIn"])
            ).optional(),
            "product": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "snapshotNumber": t.string().optional(),
            "workflowName": t.string().optional(),
            "eventExecutionInfoId": t.string().optional(),
            "clientId": t.string().optional(),
            "executionTraceInfo": t.proxy(
                renames["EnterpriseCrmEventbusProtoExecutionTraceInfoIn"]
            ).optional(),
            "responseParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
            ).optional(),
            "triggerId": t.string().optional(),
            "tenant": t.string().optional(),
            "requestParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
            ).optional(),
            "requestId": t.string().optional(),
            "workflowId": t.string(),
            "postMethod": t.string().optional(),
            "workflowRetryBackoffIntervalSeconds": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoIn"])
    types["EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "errorCode": t.proxy(renames["CrmlogErrorCodeOut"]).optional(),
            "eventExecutionDetails": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsOut"]
            ).optional(),
            "errors": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoErrorDetailOut"])
            ).optional(),
            "product": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "snapshotNumber": t.string().optional(),
            "workflowName": t.string().optional(),
            "eventExecutionInfoId": t.string().optional(),
            "clientId": t.string().optional(),
            "executionTraceInfo": t.proxy(
                renames["EnterpriseCrmEventbusProtoExecutionTraceInfoOut"]
            ).optional(),
            "responseParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "triggerId": t.string().optional(),
            "tenant": t.string().optional(),
            "requestParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "requestId": t.string().optional(),
            "workflowId": t.string(),
            "postMethod": t.string().optional(),
            "workflowRetryBackoffIntervalSeconds": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoOut"])
    types["EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayIn"] = t.struct(
        {"protoValues": t.array(t.struct({"_": t.string().optional()}))}
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayIn"])
    types["EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayOut"] = t.struct(
        {
            "protoValues": t.array(t.struct({"_": t.string().optional()})),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayOut"])
    types[
        "GoogleCloudIntegrationsV1alphaPublishIntegrationVersionRequestIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudIntegrationsV1alphaPublishIntegrationVersionRequestIn"]
    )
    types[
        "GoogleCloudIntegrationsV1alphaPublishIntegrationVersionRequestOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames["GoogleCloudIntegrationsV1alphaPublishIntegrationVersionRequestOut"]
    )
    types["GoogleCloudIntegrationsV1alphaAccessTokenIn"] = t.struct(
        {
            "accessTokenExpireTime": t.string(),
            "refreshTokenExpireTime": t.string().optional(),
            "accessToken": t.string().optional(),
            "tokenType": t.string().optional(),
            "refreshToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaAccessTokenIn"])
    types["GoogleCloudIntegrationsV1alphaAccessTokenOut"] = t.struct(
        {
            "accessTokenExpireTime": t.string(),
            "refreshTokenExpireTime": t.string().optional(),
            "accessToken": t.string().optional(),
            "tokenType": t.string().optional(),
            "refreshToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaAccessTokenOut"])
    types["EnterpriseCrmEventbusProtoTokenIn"] = t.struct(
        {"value": t.string(), "name": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoTokenIn"])
    types["EnterpriseCrmEventbusProtoTokenOut"] = t.struct(
        {
            "value": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTokenOut"])
    types["EnterpriseCrmEventbusProtoFieldIn"] = t.struct(
        {
            "referenceKey": t.string().optional(),
            "fieldType": t.string().optional(),
            "cardinality": t.string().optional(),
            "transformExpression": t.proxy(
                renames["EnterpriseCrmEventbusProtoTransformExpressionIn"]
            ).optional(),
            "protoDefPath": t.string().optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFieldIn"])
    types["EnterpriseCrmEventbusProtoFieldOut"] = t.struct(
        {
            "referenceKey": t.string().optional(),
            "fieldType": t.string().optional(),
            "cardinality": t.string().optional(),
            "transformExpression": t.proxy(
                renames["EnterpriseCrmEventbusProtoTransformExpressionOut"]
            ).optional(),
            "protoDefPath": t.string().optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFieldOut"])
    types["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIn"] = t.struct(
        {
            "intRange": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeIn"
                ]
            ),
            "doubleRange": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeIn"
                ]
            ),
            "stringRegex": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexIn"
                ]
            ),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIn"])
    types["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleOut"] = t.struct(
        {
            "intRange": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeOut"
                ]
            ),
            "doubleRange": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeOut"
                ]
            ),
            "stringRegex": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexOut"
                ]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleOut"])
    types["EnterpriseCrmEventbusProtoFailurePolicyIn"] = t.struct(
        {
            "retryStrategy": t.string().optional(),
            "intervalInSeconds": t.string(),
            "maxNumRetries": t.integer(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFailurePolicyIn"])
    types["EnterpriseCrmEventbusProtoFailurePolicyOut"] = t.struct(
        {
            "retryStrategy": t.string().optional(),
            "intervalInSeconds": t.string(),
            "maxNumRetries": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFailurePolicyOut"])
    types["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestIn"] = t.struct(
        {"scriptId": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestIn"])
    types["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestOut"] = t.struct(
        {
            "scriptId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestOut"])
    types["EnterpriseCrmEventbusProtoParamSpecEntryConfigIn"] = t.struct(
        {
            "isHidden": t.boolean().optional(),
            "hideDefaultValue": t.boolean().optional(),
            "uiPlaceholderText": t.string().optional(),
            "parameterNameOption": t.string(),
            "helpText": t.string().optional(),
            "label": t.string().optional(),
            "subSectionLabel": t.string().optional(),
            "inputDisplayOption": t.string(),
            "descriptivePhrase": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParamSpecEntryConfigIn"])
    types["EnterpriseCrmEventbusProtoParamSpecEntryConfigOut"] = t.struct(
        {
            "isHidden": t.boolean().optional(),
            "hideDefaultValue": t.boolean().optional(),
            "uiPlaceholderText": t.string().optional(),
            "parameterNameOption": t.string(),
            "helpText": t.string().optional(),
            "label": t.string().optional(),
            "subSectionLabel": t.string().optional(),
            "inputDisplayOption": t.string(),
            "descriptivePhrase": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParamSpecEntryConfigOut"])
    types["GoogleCloudIntegrationsV1alphaIntegrationIn"] = t.struct(
        {
            "name": t.string(),
            "active": t.boolean(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationIn"])
    types["GoogleCloudIntegrationsV1alphaIntegrationOut"] = t.struct(
        {
            "name": t.string(),
            "updateTime": t.string().optional(),
            "active": t.boolean(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationOut"])
    types["EnterpriseCrmEventbusProtoAddressIn"] = t.struct(
        {
            "email": t.string(),
            "tokens": t.array(t.proxy(renames["EnterpriseCrmEventbusProtoTokenIn"])),
            "name": t.string(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoAddressIn"])
    types["EnterpriseCrmEventbusProtoAddressOut"] = t.struct(
        {
            "email": t.string(),
            "tokens": t.array(t.proxy(renames["EnterpriseCrmEventbusProtoTokenOut"])),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoAddressOut"])
    types["EnterpriseCrmFrontendsEventbusProtoTaskConfigIn"] = t.struct(
        {
            "creatorEmail": t.string().optional(),
            "alertConfigs": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskAlertConfigIn"])
            ).optional(),
            "description": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "label": t.string().optional(),
            "errorCatcherId": t.string().optional(),
            "rollbackStrategy": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoRollbackStrategyIn"]
            ).optional(),
            "successPolicy": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuccessPolicyIn"]
            ).optional(),
            "incomingEdgeCount": t.integer().optional(),
            "taskNumber": t.string().optional(),
            "taskExecutionStrategy": t.string().optional(),
            "taskName": t.string().optional(),
            "taskTemplateName": t.string().optional(),
            "position": t.proxy(
                renames["EnterpriseCrmEventbusProtoCoordinateIn"]
            ).optional(),
            "createTime": t.string().optional(),
            "externalTaskType": t.string(),
            "jsonValidationOption": t.string().optional(),
            "synchronousCallFailurePolicy": t.proxy(
                renames["EnterpriseCrmEventbusProtoFailurePolicyIn"]
            ).optional(),
            "lastModifiedTime": t.string().optional(),
            "taskSpec": t.string().optional(),
            "precondition": t.string().optional(),
            "taskEntity": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoTaskEntityIn"]
            ).optional(),
            "failurePolicy": t.proxy(
                renames["EnterpriseCrmEventbusProtoFailurePolicyIn"]
            ).optional(),
            "taskType": t.string().optional(),
            "disableStrictTypeValidation": t.boolean().optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "nextTasks": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoNextTaskIn"])
            ).optional(),
            "preconditionLabel": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigIn"])
    types["EnterpriseCrmFrontendsEventbusProtoTaskConfigOut"] = t.struct(
        {
            "creatorEmail": t.string().optional(),
            "alertConfigs": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskAlertConfigOut"])
            ).optional(),
            "description": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "label": t.string().optional(),
            "errorCatcherId": t.string().optional(),
            "rollbackStrategy": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoRollbackStrategyOut"]
            ).optional(),
            "successPolicy": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuccessPolicyOut"]
            ).optional(),
            "incomingEdgeCount": t.integer().optional(),
            "taskNumber": t.string().optional(),
            "taskExecutionStrategy": t.string().optional(),
            "taskName": t.string().optional(),
            "taskTemplateName": t.string().optional(),
            "position": t.proxy(
                renames["EnterpriseCrmEventbusProtoCoordinateOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "externalTaskType": t.string(),
            "jsonValidationOption": t.string().optional(),
            "synchronousCallFailurePolicy": t.proxy(
                renames["EnterpriseCrmEventbusProtoFailurePolicyOut"]
            ).optional(),
            "lastModifiedTime": t.string().optional(),
            "taskSpec": t.string().optional(),
            "precondition": t.string().optional(),
            "taskEntity": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoTaskEntityOut"]
            ).optional(),
            "failurePolicy": t.proxy(
                renames["EnterpriseCrmEventbusProtoFailurePolicyOut"]
            ).optional(),
            "taskType": t.string().optional(),
            "disableStrictTypeValidation": t.boolean().optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "nextTasks": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoNextTaskOut"])
            ).optional(),
            "preconditionLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigOut"])
    types[
        "GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestIn"
    ] = t.struct(
        {
            "scheduledTime": t.string().optional(),
            "requestId": t.string().optional(),
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersIn"]
            ).optional(),
            "workflowName": t.string().optional(),
            "ignoreErrorIfNoActiveWorkflow": t.boolean().optional(),
            "priority": t.string().optional(),
            "resourceName": t.string().optional(),
            "testMode": t.boolean().optional(),
            "triggerId": t.string().optional(),
            "clientId": t.string().optional(),
        }
    ).named(
        renames["GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestIn"]
    )
    types[
        "GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestOut"
    ] = t.struct(
        {
            "scheduledTime": t.string().optional(),
            "requestId": t.string().optional(),
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersOut"]
            ).optional(),
            "workflowName": t.string().optional(),
            "ignoreErrorIfNoActiveWorkflow": t.boolean().optional(),
            "priority": t.string().optional(),
            "resourceName": t.string().optional(),
            "testMode": t.boolean().optional(),
            "triggerId": t.string().optional(),
            "clientId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestOut"]
    )
    types["EnterpriseCrmEventbusProtoTaskMetadataAdminIn"] = t.struct(
        {"userEmail": t.string(), "googleGroupEmail": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoTaskMetadataAdminIn"])
    types["EnterpriseCrmEventbusProtoTaskMetadataAdminOut"] = t.struct(
        {
            "userEmail": t.string(),
            "googleGroupEmail": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskMetadataAdminOut"])
    types["GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeIn"] = t.struct(
        {
            "clientSecret": t.string().optional(),
            "scope": t.string().optional(),
            "authEndpoint": t.string().optional(),
            "tokenEndpoint": t.string().optional(),
            "clientId": t.string().optional(),
            "tokenParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapIn"]
            ).optional(),
            "applyReauthPolicy": t.boolean().optional(),
            "accessToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAccessTokenIn"]
            ).optional(),
            "authCode": t.string().optional(),
            "requestType": t.string().optional(),
            "authParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeIn"])
    types["GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeOut"] = t.struct(
        {
            "clientSecret": t.string().optional(),
            "scope": t.string().optional(),
            "authEndpoint": t.string().optional(),
            "tokenEndpoint": t.string().optional(),
            "clientId": t.string().optional(),
            "tokenParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapOut"]
            ).optional(),
            "applyReauthPolicy": t.boolean().optional(),
            "accessToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAccessTokenOut"]
            ).optional(),
            "authCode": t.string().optional(),
            "requestType": t.string().optional(),
            "authParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeOut"])
    types["GoogleCloudIntegrationsV1alphaExecutionSnapshotIn"] = t.struct(
        {
            "executionSnapshotMetadata": t.proxy(
                renames[
                    "GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataIn"
                ]
            ).optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "taskExecutionDetails": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaTaskExecutionDetailsIn"])
            ).optional(),
            "checkpointTaskNumber": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecutionSnapshotIn"])
    types["GoogleCloudIntegrationsV1alphaExecutionSnapshotOut"] = t.struct(
        {
            "executionSnapshotMetadata": t.proxy(
                renames[
                    "GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataOut"
                ]
            ).optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "taskExecutionDetails": t.array(
                t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaTaskExecutionDetailsOut"]
                )
            ).optional(),
            "checkpointTaskNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecutionSnapshotOut"])
    types["GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseIn"] = t.struct(
        {
            "executionFailed": t.boolean().optional(),
            "executionId": t.string().optional(),
            "outputParameters": t.struct({"_": t.string().optional()}).optional(),
            "eventParameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
            ).optional(),
            "parameterEntries": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseIn"])
    types["GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseOut"] = t.struct(
        {
            "executionFailed": t.boolean().optional(),
            "executionId": t.string().optional(),
            "outputParameters": t.struct({"_": t.string().optional()}).optional(),
            "eventParameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "parameterEntries": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseOut"])
    types["EnterpriseCrmEventbusProtoTaskUiModuleConfigIn"] = t.struct(
        {"moduleId": t.string().optional()}
    ).named(renames["EnterpriseCrmEventbusProtoTaskUiModuleConfigIn"])
    types["EnterpriseCrmEventbusProtoTaskUiModuleConfigOut"] = t.struct(
        {
            "moduleId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskUiModuleConfigOut"])
    types["GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaIn"] = t.struct(
        {
            "arrayFieldSchema": t.string().optional(),
            "fieldSchema": t.string().optional(),
            "entity": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaIn"])
    types["GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaOut"] = t.struct(
        {
            "arrayFieldSchema": t.string().optional(),
            "fieldSchema": t.string().optional(),
            "entity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaOut"])
    types["GoogleCloudIntegrationsV1alphaDoubleParameterArrayIn"] = t.struct(
        {"doubleValues": t.array(t.number()).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaDoubleParameterArrayIn"])
    types["GoogleCloudIntegrationsV1alphaDoubleParameterArrayOut"] = t.struct(
        {
            "doubleValues": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaDoubleParameterArrayOut"])
    types["GoogleCloudIntegrationsV1alphaBooleanParameterArrayIn"] = t.struct(
        {"booleanValues": t.array(t.boolean()).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaBooleanParameterArrayIn"])
    types["GoogleCloudIntegrationsV1alphaBooleanParameterArrayOut"] = t.struct(
        {
            "booleanValues": t.array(t.boolean()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaBooleanParameterArrayOut"])
    types["EnterpriseCrmEventbusProtoNextTaskIn"] = t.struct(
        {
            "description": t.string().optional(),
            "label": t.string().optional(),
            "combinedConditions": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoCombinedConditionIn"])
            ).optional(),
            "taskNumber": t.string().optional(),
            "taskConfigId": t.string().optional(),
            "condition": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoNextTaskIn"])
    types["EnterpriseCrmEventbusProtoNextTaskOut"] = t.struct(
        {
            "description": t.string().optional(),
            "label": t.string().optional(),
            "combinedConditions": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoCombinedConditionOut"])
            ).optional(),
            "taskNumber": t.string().optional(),
            "taskConfigId": t.string().optional(),
            "condition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoNextTaskOut"])
    types["EnterpriseCrmEventbusProtoEventExecutionDetailsIn"] = t.struct(
        {
            "networkAddress": t.string().optional(),
            "nextExecutionTime": t.string().optional(),
            "eventAttemptStats": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsIn"
                    ]
                )
            ),
            "logFilePath": t.string().optional(),
            "ryeLockUnheldCount": t.integer().optional(),
            "eventExecutionState": t.string(),
            "eventExecutionSnapshot": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoEventExecutionSnapshotIn"])
            ),
            "eventRetriesFromBeginningCount": t.integer().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoEventExecutionDetailsIn"])
    types["EnterpriseCrmEventbusProtoEventExecutionDetailsOut"] = t.struct(
        {
            "networkAddress": t.string().optional(),
            "nextExecutionTime": t.string().optional(),
            "eventAttemptStats": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsOut"
                    ]
                )
            ),
            "logFilePath": t.string().optional(),
            "ryeLockUnheldCount": t.integer().optional(),
            "eventExecutionState": t.string(),
            "eventExecutionSnapshot": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoEventExecutionSnapshotOut"])
            ),
            "eventRetriesFromBeginningCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoEventExecutionDetailsOut"])
    types["GoogleCloudIntegrationsV1alphaSfdcChannelIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "isActive": t.boolean().optional(),
            "lastReplayId": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "channelTopic": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSfdcChannelIn"])
    types["GoogleCloudIntegrationsV1alphaSfdcChannelOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "isActive": t.boolean().optional(),
            "deleteTime": t.string().optional(),
            "lastReplayId": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "channelTopic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"])
    types["GoogleCloudIntegrationsV1alphaExecuteEventResponseIn"] = t.struct(
        {"executionId": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaExecuteEventResponseIn"])
    types["GoogleCloudIntegrationsV1alphaExecuteEventResponseOut"] = t.struct(
        {
            "executionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecuteEventResponseOut"])
    types["EnterpriseCrmEventbusProtoCustomSuspensionRequestIn"] = t.struct(
        {
            "postToQueueWithTriggerIdRequest": t.proxy(
                renames[
                    "GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestIn"
                ]
            ).optional(),
            "suspensionInfoEventParameterKey": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoCustomSuspensionRequestIn"])
    types["EnterpriseCrmEventbusProtoCustomSuspensionRequestOut"] = t.struct(
        {
            "postToQueueWithTriggerIdRequest": t.proxy(
                renames[
                    "GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestOut"
                ]
            ).optional(),
            "suspensionInfoEventParameterKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoCustomSuspensionRequestOut"])
    types["EnterpriseCrmEventbusProtoIntArrayIn"] = t.struct(
        {"values": t.array(t.string())}
    ).named(renames["EnterpriseCrmEventbusProtoIntArrayIn"])
    types["EnterpriseCrmEventbusProtoIntArrayOut"] = t.struct(
        {
            "values": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoIntArrayOut"])
    types["GoogleCloudIntegrationsV1alphaCredentialIn"] = t.struct(
        {
            "serviceAccountCredentials": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaServiceAccountCredentialsIn"]
            ).optional(),
            "oauth2ClientCredentials": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsIn"]
            ).optional(),
            "jwt": t.proxy(renames["GoogleCloudIntegrationsV1alphaJwtIn"]).optional(),
            "usernameAndPassword": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaUsernameAndPasswordIn"]
            ).optional(),
            "credentialType": t.string().optional(),
            "oauth2AuthorizationCode": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeIn"]
            ).optional(),
            "oauth2ResourceOwnerCredentials": t.proxy(
                renames[
                    "GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsIn"
                ]
            ).optional(),
            "authToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAuthTokenIn"]
            ).optional(),
            "oidcToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaOidcTokenIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCredentialIn"])
    types["GoogleCloudIntegrationsV1alphaCredentialOut"] = t.struct(
        {
            "serviceAccountCredentials": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaServiceAccountCredentialsOut"]
            ).optional(),
            "oauth2ClientCredentials": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsOut"]
            ).optional(),
            "jwt": t.proxy(renames["GoogleCloudIntegrationsV1alphaJwtOut"]).optional(),
            "usernameAndPassword": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaUsernameAndPasswordOut"]
            ).optional(),
            "credentialType": t.string().optional(),
            "oauth2AuthorizationCode": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeOut"]
            ).optional(),
            "oauth2ResourceOwnerCredentials": t.proxy(
                renames[
                    "GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsOut"
                ]
            ).optional(),
            "authToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAuthTokenOut"]
            ).optional(),
            "oidcToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaOidcTokenOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCredentialOut"])
    types["EnterpriseCrmEventbusProtoProtoParameterArrayIn"] = t.struct(
        {"protoValues": t.array(t.struct({"_": t.string().optional()}))}
    ).named(renames["EnterpriseCrmEventbusProtoProtoParameterArrayIn"])
    types["EnterpriseCrmEventbusProtoProtoParameterArrayOut"] = t.struct(
        {
            "protoValues": t.array(t.struct({"_": t.string().optional()})),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoProtoParameterArrayOut"])
    types["GoogleCloudIntegrationsV1alphaFailurePolicyIn"] = t.struct(
        {
            "retryStrategy": t.string().optional(),
            "maxRetries": t.integer(),
            "intervalTime": t.string(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaFailurePolicyIn"])
    types["GoogleCloudIntegrationsV1alphaFailurePolicyOut"] = t.struct(
        {
            "retryStrategy": t.string().optional(),
            "maxRetries": t.integer(),
            "intervalTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaFailurePolicyOut"])
    types["EnterpriseCrmEventbusProtoBooleanArrayFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoBooleanArrayFunctionIn"])
    types["EnterpriseCrmEventbusProtoBooleanArrayFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBooleanArrayFunctionOut"])
    types["CrmlogErrorCodeIn"] = t.struct({"commonErrorCode": t.string()}).named(
        renames["CrmlogErrorCodeIn"]
    )
    types["CrmlogErrorCodeOut"] = t.struct(
        {
            "commonErrorCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CrmlogErrorCodeOut"])
    types["EnterpriseCrmFrontendsEventbusProtoIntParameterArrayIn"] = t.struct(
        {"intValues": t.array(t.string())}
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoIntParameterArrayIn"])
    types["EnterpriseCrmFrontendsEventbusProtoIntParameterArrayOut"] = t.struct(
        {
            "intValues": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoIntParameterArrayOut"])
    types["GoogleCloudIntegrationsV1alphaTriggerConfigIn"] = t.struct(
        {
            "triggerNumber": t.string(),
            "startTasks": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaNextTaskIn"])
            ).optional(),
            "trigger": t.string().optional(),
            "errorCatcherId": t.string().optional(),
            "triggerId": t.string().optional(),
            "alertConfig": t.array(
                t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigIn"]
                )
            ).optional(),
            "description": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCoordinateIn"]
            ).optional(),
            "cloudSchedulerConfig": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCloudSchedulerConfigIn"]
            ).optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "label": t.string().optional(),
            "triggerType": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaTriggerConfigIn"])
    types["GoogleCloudIntegrationsV1alphaTriggerConfigOut"] = t.struct(
        {
            "triggerNumber": t.string(),
            "startTasks": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaNextTaskOut"])
            ).optional(),
            "trigger": t.string().optional(),
            "errorCatcherId": t.string().optional(),
            "triggerId": t.string().optional(),
            "alertConfig": t.array(
                t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigOut"]
                )
            ).optional(),
            "description": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCoordinateOut"]
            ).optional(),
            "cloudSchedulerConfig": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCloudSchedulerConfigOut"]
            ).optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "label": t.string().optional(),
            "triggerType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaTriggerConfigOut"])
    types["EnterpriseCrmEventbusProtoConnectorsConnectionIn"] = t.struct(
        {
            "serviceName": t.string().optional(),
            "connectionName": t.string().optional(),
            "connectorVersion": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoConnectorsConnectionIn"])
    types["EnterpriseCrmEventbusProtoConnectorsConnectionOut"] = t.struct(
        {
            "serviceName": t.string().optional(),
            "connectionName": t.string().optional(),
            "connectorVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoConnectorsConnectionOut"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterMapFieldIn"] = t.struct(
        {
            "referenceKey": t.string().optional(),
            "literalValue": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterMapFieldIn"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterMapFieldOut"] = t.struct(
        {
            "referenceKey": t.string().optional(),
            "literalValue": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterMapFieldOut"])
    types["EnterpriseCrmEventbusProtoMappedFieldIn"] = t.struct(
        {
            "inputField": t.proxy(
                renames["EnterpriseCrmEventbusProtoFieldIn"]
            ).optional(),
            "outputField": t.proxy(
                renames["EnterpriseCrmEventbusProtoFieldIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoMappedFieldIn"])
    types["EnterpriseCrmEventbusProtoMappedFieldOut"] = t.struct(
        {
            "inputField": t.proxy(
                renames["EnterpriseCrmEventbusProtoFieldOut"]
            ).optional(),
            "outputField": t.proxy(
                renames["EnterpriseCrmEventbusProtoFieldOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoMappedFieldOut"])
    types["EnterpriseCrmEventbusProtoLoopMetadataIn"] = t.struct(
        {
            "failureLocation": t.string().optional(),
            "currentIterationDetail": t.string().optional(),
            "currentIterationCount": t.string().optional(),
            "errorMsg": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoLoopMetadataIn"])
    types["EnterpriseCrmEventbusProtoLoopMetadataOut"] = t.struct(
        {
            "failureLocation": t.string().optional(),
            "currentIterationDetail": t.string().optional(),
            "currentIterationCount": t.string().optional(),
            "errorMsg": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoLoopMetadataOut"])
    types["EnterpriseCrmEventbusProtoFunctionTypeIn"] = t.struct(
        {
            "baseFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseFunctionIn"]
            ).optional(),
            "intFunction": t.proxy(renames["EnterpriseCrmEventbusProtoIntFunctionIn"]),
            "stringArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoStringArrayFunctionIn"]
            ),
            "protoFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoProtoFunctionIn"]
            ),
            "booleanArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoBooleanArrayFunctionIn"]
            ),
            "protoArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoProtoArrayFunctionIn"]
            ),
            "booleanFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoBooleanFunctionIn"]
            ),
            "jsonFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoJsonFunctionIn"]
            ).optional(),
            "intArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoIntArrayFunctionIn"]
            ),
            "stringFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoStringFunctionIn"]
            ),
            "doubleFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoDoubleFunctionIn"]
            ),
            "doubleArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoDoubleArrayFunctionIn"]
            ),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFunctionTypeIn"])
    types["EnterpriseCrmEventbusProtoFunctionTypeOut"] = t.struct(
        {
            "baseFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseFunctionOut"]
            ).optional(),
            "intFunction": t.proxy(renames["EnterpriseCrmEventbusProtoIntFunctionOut"]),
            "stringArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoStringArrayFunctionOut"]
            ),
            "protoFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoProtoFunctionOut"]
            ),
            "booleanArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoBooleanArrayFunctionOut"]
            ),
            "protoArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoProtoArrayFunctionOut"]
            ),
            "booleanFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoBooleanFunctionOut"]
            ),
            "jsonFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoJsonFunctionOut"]
            ).optional(),
            "intArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoIntArrayFunctionOut"]
            ),
            "stringFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoStringFunctionOut"]
            ),
            "doubleFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoDoubleFunctionOut"]
            ),
            "doubleArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoDoubleArrayFunctionOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFunctionTypeOut"])
    types["GoogleCloudConnectorsV1AuthConfigIn"] = t.struct(
        {
            "oauth2AuthCodeFlow": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowIn"]
            ).optional(),
            "sshPublicKey": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigSshPublicKeyIn"]
            ).optional(),
            "authKey": t.string().optional(),
            "oauth2ClientCredentials": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsIn"]
            ).optional(),
            "authType": t.string().optional(),
            "oauth2JwtBearer": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerIn"]
            ).optional(),
            "userPassword": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigUserPasswordIn"]
            ).optional(),
            "additionalVariables": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConfigVariableIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigIn"])
    types["GoogleCloudConnectorsV1AuthConfigOut"] = t.struct(
        {
            "oauth2AuthCodeFlow": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowOut"]
            ).optional(),
            "sshPublicKey": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigSshPublicKeyOut"]
            ).optional(),
            "authKey": t.string().optional(),
            "oauth2ClientCredentials": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsOut"]
            ).optional(),
            "authType": t.string().optional(),
            "oauth2JwtBearer": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerOut"]
            ).optional(),
            "userPassword": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigUserPasswordOut"]
            ).optional(),
            "additionalVariables": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConfigVariableOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigOut"])
    types[
        "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataIn"
    ] = t.struct(
        {
            "taskNumber": t.string().optional(),
            "taskName": t.string().optional(),
            "taskLabel": t.string().optional(),
            "taskAttemptNum": t.integer().optional(),
            "eventAttemptNum": t.integer().optional(),
        }
    ).named(
        renames[
            "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataIn"
        ]
    )
    types[
        "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataOut"
    ] = t.struct(
        {
            "taskNumber": t.string().optional(),
            "taskName": t.string().optional(),
            "taskLabel": t.string().optional(),
            "taskAttemptNum": t.integer().optional(),
            "eventAttemptNum": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataOut"
        ]
    )
    types["GoogleCloudIntegrationsV1alphaListSuspensionsResponseIn"] = t.struct(
        {
            "suspensions": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaSuspensionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListSuspensionsResponseIn"])
    types["GoogleCloudIntegrationsV1alphaListSuspensionsResponseOut"] = t.struct(
        {
            "suspensions": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaSuspensionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListSuspensionsResponseOut"])
    types["EnterpriseCrmEventbusProtoBooleanParameterArrayIn"] = t.struct(
        {"booleanValues": t.array(t.boolean())}
    ).named(renames["EnterpriseCrmEventbusProtoBooleanParameterArrayIn"])
    types["EnterpriseCrmEventbusProtoBooleanParameterArrayOut"] = t.struct(
        {
            "booleanValues": t.array(t.boolean()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBooleanParameterArrayOut"])
    types[
        "GoogleCloudIntegrationsV1alphaEnumerateConnectorPlatformRegionsResponseIn"
    ] = t.struct({"regions": t.array(t.string()).optional()}).named(
        renames[
            "GoogleCloudIntegrationsV1alphaEnumerateConnectorPlatformRegionsResponseIn"
        ]
    )
    types[
        "GoogleCloudIntegrationsV1alphaEnumerateConnectorPlatformRegionsResponseOut"
    ] = t.struct(
        {
            "regions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudIntegrationsV1alphaEnumerateConnectorPlatformRegionsResponseOut"
        ]
    )
    types["GoogleCloudIntegrationsV1alphaSfdcInstanceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "sfdcOrgId": t.string().optional(),
            "displayName": t.string().optional(),
            "authConfigId": t.array(t.string()).optional(),
            "serviceAuthority": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceIn"])
    types["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "sfdcOrgId": t.string().optional(),
            "displayName": t.string().optional(),
            "authConfigId": t.array(t.string()).optional(),
            "serviceAuthority": t.string().optional(),
            "deleteTime": t.string().optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"])
    types["GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataIn"] = t.struct(
        {
            "entities": t.array(t.string()).optional(),
            "actions": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataIn"])
    types["GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataOut"] = t.struct(
        {
            "entities": t.array(t.string()).optional(),
            "actions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataOut"])
    types["EnterpriseCrmEventbusProtoDoubleFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoDoubleFunctionIn"])
    types["EnterpriseCrmEventbusProtoDoubleFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoDoubleFunctionOut"])
    types["GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestIn"])
    types["GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestOut"])
    types["GoogleCloudIntegrationsV1alphaServiceAccountCredentialsIn"] = t.struct(
        {"scope": t.string().optional(), "serviceAccount": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaServiceAccountCredentialsIn"])
    types["GoogleCloudIntegrationsV1alphaServiceAccountCredentialsOut"] = t.struct(
        {
            "scope": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaServiceAccountCredentialsOut"])
    types["GoogleCloudIntegrationsV1alphaLiftSuspensionResponseIn"] = t.struct(
        {"eventExecutionInfoId": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaLiftSuspensionResponseIn"])
    types["GoogleCloudIntegrationsV1alphaLiftSuspensionResponseOut"] = t.struct(
        {
            "eventExecutionInfoId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaLiftSuspensionResponseOut"])
    types["GoogleCloudConnectorsV1ConfigVariableIn"] = t.struct(
        {
            "encryptionKeyValue": t.proxy(
                renames["GoogleCloudConnectorsV1EncryptionKeyIn"]
            ).optional(),
            "boolValue": t.boolean().optional(),
            "intValue": t.string().optional(),
            "key": t.string().optional(),
            "stringValue": t.string().optional(),
            "secretValue": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1ConfigVariableIn"])
    types["GoogleCloudConnectorsV1ConfigVariableOut"] = t.struct(
        {
            "encryptionKeyValue": t.proxy(
                renames["GoogleCloudConnectorsV1EncryptionKeyOut"]
            ).optional(),
            "boolValue": t.boolean().optional(),
            "intValue": t.string().optional(),
            "key": t.string().optional(),
            "stringValue": t.string().optional(),
            "secretValue": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1ConfigVariableOut"])
    types[
        "GoogleCloudIntegrationsV1alphaUploadIntegrationVersionResponseIn"
    ] = t.struct(
        {
            "integrationVersion": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaIntegrationVersionIn"]
            ).optional()
        }
    ).named(
        renames["GoogleCloudIntegrationsV1alphaUploadIntegrationVersionResponseIn"]
    )
    types[
        "GoogleCloudIntegrationsV1alphaUploadIntegrationVersionResponseOut"
    ] = t.struct(
        {
            "integrationVersion": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudIntegrationsV1alphaUploadIntegrationVersionResponseOut"]
    )
    types[
        "GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseIn"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "runtimeActionSchemas": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaRuntimeActionSchemaIn"])
            ).optional(),
        }
    ).named(
        renames["GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseIn"]
    )
    types[
        "GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "runtimeActionSchemas": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaRuntimeActionSchemaOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseOut"]
    )
    types["EnterpriseCrmFrontendsEventbusProtoTaskEntityIn"] = t.struct(
        {
            "paramSpecs": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageIn"]
            ).optional(),
            "disabledForVpcSc": t.boolean().optional(),
            "metadata": t.proxy(
                renames["EnterpriseCrmEventbusProtoTaskMetadataIn"]
            ).optional(),
            "uiConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoTaskUiConfigIn"]
            ).optional(),
            "taskType": t.string().optional(),
            "stats": t.proxy(renames["EnterpriseCrmEventbusStatsIn"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoTaskEntityIn"])
    types["EnterpriseCrmFrontendsEventbusProtoTaskEntityOut"] = t.struct(
        {
            "paramSpecs": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageOut"]
            ).optional(),
            "disabledForVpcSc": t.boolean().optional(),
            "metadata": t.proxy(
                renames["EnterpriseCrmEventbusProtoTaskMetadataOut"]
            ).optional(),
            "uiConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoTaskUiConfigOut"]
            ).optional(),
            "taskType": t.string().optional(),
            "stats": t.proxy(renames["EnterpriseCrmEventbusStatsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoTaskEntityOut"])
    types["GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseIn"] = t.struct(
        {
            "integrationVersions": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionIn"])
            ).optional(),
            "noPermission": t.boolean().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseIn"])
    types[
        "GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseOut"
    ] = t.struct(
        {
            "integrationVersions": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"])
            ).optional(),
            "noPermission": t.boolean().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseOut"]
    )
    types["GoogleCloudIntegrationsV1alphaIntegrationVersionIn"] = t.struct(
        {
            "runAsServiceAccount": t.string().optional(),
            "errorCatcherConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn"])
            ).optional(),
            "taskConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaTaskConfigIn"])
            ).optional(),
            "integrationParameters": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationParameterIn"])
            ).optional(),
            "origin": t.string().optional(),
            "triggerConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaTriggerConfigIn"])
            ).optional(),
            "triggerConfigsInternal": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn"])
            ).optional(),
            "lastModifierEmail": t.string().optional(),
            "taskConfigsInternal": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigIn"])
            ).optional(),
            "description": t.string().optional(),
            "lockHolder": t.string().optional(),
            "parentTemplateId": t.string().optional(),
            "integrationParametersInternal": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn"]
            ).optional(),
            "snapshotNumber": t.string().optional(),
            "teardown": t.proxy(
                renames["EnterpriseCrmEventbusProtoTeardownIn"]
            ).optional(),
            "userLabel": t.string().optional(),
            "databasePersistencePolicy": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionIn"])
    types["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"] = t.struct(
        {
            "runAsServiceAccount": t.string().optional(),
            "updateTime": t.string().optional(),
            "errorCatcherConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigOut"])
            ).optional(),
            "taskConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaTaskConfigOut"])
            ).optional(),
            "integrationParameters": t.array(
                t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaIntegrationParameterOut"]
                )
            ).optional(),
            "origin": t.string().optional(),
            "triggerConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaTriggerConfigOut"])
            ).optional(),
            "triggerConfigsInternal": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigOut"])
            ).optional(),
            "lastModifierEmail": t.string().optional(),
            "status": t.string().optional(),
            "taskConfigsInternal": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigOut"])
            ).optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "lockHolder": t.string().optional(),
            "parentTemplateId": t.string().optional(),
            "integrationParametersInternal": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersOut"]
            ).optional(),
            "snapshotNumber": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "teardown": t.proxy(
                renames["EnterpriseCrmEventbusProtoTeardownOut"]
            ).optional(),
            "userLabel": t.string().optional(),
            "databasePersistencePolicy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"])
    types["GoogleCloudIntegrationsV1alphaParameterMapFieldIn"] = t.struct(
        {
            "referenceKey": t.string().optional(),
            "literalValue": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaValueTypeIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaParameterMapFieldIn"])
    types["GoogleCloudIntegrationsV1alphaParameterMapFieldOut"] = t.struct(
        {
            "referenceKey": t.string().optional(),
            "literalValue": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaValueTypeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaParameterMapFieldOut"])
    types["GoogleCloudIntegrationsV1alphaEventParameterIn"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaValueTypeIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaEventParameterIn"])
    types["GoogleCloudIntegrationsV1alphaEventParameterOut"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaValueTypeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaEventParameterOut"])
    types["GoogleCloudConnectorsV1AuthConfigUserPasswordIn"] = t.struct(
        {
            "username": t.string().optional(),
            "password": t.proxy(renames["GoogleCloudConnectorsV1SecretIn"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigUserPasswordIn"])
    types["GoogleCloudConnectorsV1AuthConfigUserPasswordOut"] = t.struct(
        {
            "username": t.string().optional(),
            "password": t.proxy(renames["GoogleCloudConnectorsV1SecretOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigUserPasswordOut"])
    types["GoogleCloudConnectorsV1ConnectionIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "nodeConfig": t.proxy(
                renames["GoogleCloudConnectorsV1NodeConfigIn"]
            ).optional(),
            "suspended": t.boolean().optional(),
            "authConfig": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigIn"]
            ).optional(),
            "sslConfig": t.proxy(
                renames["GoogleCloudConnectorsV1SslConfigIn"]
            ).optional(),
            "destinationConfigs": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1DestinationConfigIn"])
            ).optional(),
            "connectorVersion": t.string(),
            "configVariables": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConfigVariableIn"])
            ).optional(),
            "lockConfig": t.proxy(
                renames["GoogleCloudConnectorsV1LockConfigIn"]
            ).optional(),
            "description": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "logConfig": t.proxy(
                renames["GoogleCloudConnectorsV1LogConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1ConnectionIn"])
    types["GoogleCloudConnectorsV1ConnectionOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "imageLocation": t.string().optional(),
            "connectionRevision": t.string().optional(),
            "nodeConfig": t.proxy(
                renames["GoogleCloudConnectorsV1NodeConfigOut"]
            ).optional(),
            "suspended": t.boolean().optional(),
            "authConfig": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOut"]
            ).optional(),
            "sslConfig": t.proxy(
                renames["GoogleCloudConnectorsV1SslConfigOut"]
            ).optional(),
            "envoyImageLocation": t.string().optional(),
            "status": t.proxy(
                renames["GoogleCloudConnectorsV1ConnectionStatusOut"]
            ).optional(),
            "name": t.string().optional(),
            "destinationConfigs": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1DestinationConfigOut"])
            ).optional(),
            "updateTime": t.string().optional(),
            "connectorVersion": t.string(),
            "configVariables": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConfigVariableOut"])
            ).optional(),
            "serviceDirectory": t.string().optional(),
            "lockConfig": t.proxy(
                renames["GoogleCloudConnectorsV1LockConfigOut"]
            ).optional(),
            "connectorVersionLaunchStage": t.string().optional(),
            "description": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "subscriptionType": t.string().optional(),
            "logConfig": t.proxy(
                renames["GoogleCloudConnectorsV1LogConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1ConnectionOut"])
    types[
        "GoogleCloudIntegrationsV1alphaPublishIntegrationVersionResponseIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudIntegrationsV1alphaPublishIntegrationVersionResponseIn"]
    )
    types[
        "GoogleCloudIntegrationsV1alphaPublishIntegrationVersionResponseOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames["GoogleCloudIntegrationsV1alphaPublishIntegrationVersionResponseOut"]
    )
    types["GoogleCloudIntegrationsV1alphaOidcTokenIn"] = t.struct(
        {
            "serviceAccountEmail": t.string().optional(),
            "audience": t.string().optional(),
            "tokenExpireTime": t.string().optional(),
            "token": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOidcTokenIn"])
    types["GoogleCloudIntegrationsV1alphaOidcTokenOut"] = t.struct(
        {
            "serviceAccountEmail": t.string().optional(),
            "audience": t.string().optional(),
            "tokenExpireTime": t.string().optional(),
            "token": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOidcTokenOut"])
    types["EnterpriseCrmEventbusProtoPropertyEntryIn"] = t.struct(
        {
            "value": t.proxy(
                renames["EnterpriseCrmEventbusProtoValueTypeIn"]
            ).optional(),
            "key": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoPropertyEntryIn"])
    types["EnterpriseCrmEventbusProtoPropertyEntryOut"] = t.struct(
        {
            "value": t.proxy(
                renames["EnterpriseCrmEventbusProtoValueTypeOut"]
            ).optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoPropertyEntryOut"])
    types[
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeIn"
    ] = t.struct({"min": t.string().optional(), "max": t.string().optional()}).named(
        renames["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeIn"]
    )
    types[
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeOut"
    ] = t.struct(
        {
            "min": t.string().optional(),
            "max": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeOut"]
    )
    types["GoogleCloudIntegrationsV1alphaResolveSuspensionResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaResolveSuspensionResponseIn"])
    types["GoogleCloudIntegrationsV1alphaResolveSuspensionResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaResolveSuspensionResponseOut"])
    types["GoogleCloudIntegrationsV1alphaParameterMapEntryIn"] = t.struct(
        {
            "key": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapFieldIn"]
            ).optional(),
            "value": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapFieldIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaParameterMapEntryIn"])
    types["GoogleCloudIntegrationsV1alphaParameterMapEntryOut"] = t.struct(
        {
            "key": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapFieldOut"]
            ).optional(),
            "value": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapFieldOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaParameterMapEntryOut"])
    types["GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "sfdcInstances": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseIn"])
    types["GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "sfdcInstances": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseOut"])
    types["EnterpriseCrmEventbusProtoFunctionIn"] = t.struct(
        {
            "functionType": t.proxy(
                renames["EnterpriseCrmEventbusProtoFunctionTypeIn"]
            ).optional(),
            "parameters": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTransformExpressionIn"])
            ).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFunctionIn"])
    types["EnterpriseCrmEventbusProtoFunctionOut"] = t.struct(
        {
            "functionType": t.proxy(
                renames["EnterpriseCrmEventbusProtoFunctionTypeOut"]
            ).optional(),
            "parameters": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTransformExpressionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFunctionOut"])
    types["EnterpriseCrmEventbusProtoTeardownIn"] = t.struct(
        {
            "teardownTaskConfigs": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTeardownTaskConfigIn"])
            )
        }
    ).named(renames["EnterpriseCrmEventbusProtoTeardownIn"])
    types["EnterpriseCrmEventbusProtoTeardownOut"] = t.struct(
        {
            "teardownTaskConfigs": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTeardownTaskConfigOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTeardownOut"])
    types["EnterpriseCrmEventbusProtoIntFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoIntFunctionIn"])
    types["EnterpriseCrmEventbusProtoIntFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoIntFunctionOut"])
    types["EnterpriseCrmEventbusProtoProtoArrayFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoProtoArrayFunctionIn"])
    types["EnterpriseCrmEventbusProtoProtoArrayFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoProtoArrayFunctionOut"])
    types["EnterpriseCrmFrontendsEventbusProtoStringParameterArrayIn"] = t.struct(
        {"stringValues": t.array(t.string())}
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoStringParameterArrayIn"])
    types["EnterpriseCrmFrontendsEventbusProtoStringParameterArrayOut"] = t.struct(
        {
            "stringValues": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoStringParameterArrayOut"])
    types["EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamIn"] = t.struct(
        {
            "scope": t.string().optional(),
            "useServiceAccountInContext": t.boolean(),
            "allowedCredentialTypes": t.array(t.string()).optional(),
            "authConfigId": t.string().optional(),
            "allowedServiceAccountInContext": t.boolean(),
        }
    ).named(renames["EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamIn"])
    types["EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamOut"] = t.struct(
        {
            "scope": t.string().optional(),
            "useServiceAccountInContext": t.boolean(),
            "allowedCredentialTypes": t.array(t.string()).optional(),
            "authConfigId": t.string().optional(),
            "allowedServiceAccountInContext": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamOut"])
    types["EnterpriseCrmEventbusProtoDoubleParameterArrayIn"] = t.struct(
        {"doubleValues": t.array(t.number())}
    ).named(renames["EnterpriseCrmEventbusProtoDoubleParameterArrayIn"])
    types["EnterpriseCrmEventbusProtoDoubleParameterArrayOut"] = t.struct(
        {
            "doubleValues": t.array(t.number()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoDoubleParameterArrayOut"])
    types["GoogleCloudIntegrationsV1alphaListIntegrationsResponseIn"] = t.struct(
        {
            "integrations": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListIntegrationsResponseIn"])
    types["GoogleCloudIntegrationsV1alphaListIntegrationsResponseOut"] = t.struct(
        {
            "integrations": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListIntegrationsResponseOut"])
    types[
        "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueIn"
    ] = t.struct(
        {"percentage": t.integer().optional(), "absolute": t.string().optional()}
    ).named(
        renames["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueIn"]
    )
    types[
        "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueOut"
    ] = t.struct(
        {
            "percentage": t.integer().optional(),
            "absolute": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueOut"]
    )
    types["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigIn"] = t.struct(
        {
            "alertThreshold": t.integer().optional(),
            "disableAlert": t.boolean().optional(),
            "thresholdValue": t.proxy(
                renames[
                    "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueIn"
                ]
            ).optional(),
            "metricType": t.string().optional(),
            "thresholdType": t.string().optional(),
            "displayName": t.string().optional(),
            "durationThreshold": t.string().optional(),
            "aggregationPeriod": t.string().optional(),
            "onlyFinalAttempt": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigIn"])
    types["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigOut"] = t.struct(
        {
            "alertThreshold": t.integer().optional(),
            "disableAlert": t.boolean().optional(),
            "thresholdValue": t.proxy(
                renames[
                    "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueOut"
                ]
            ).optional(),
            "metricType": t.string().optional(),
            "thresholdType": t.string().optional(),
            "displayName": t.string().optional(),
            "durationThreshold": t.string().optional(),
            "aggregationPeriod": t.string().optional(),
            "onlyFinalAttempt": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigOut"])
    types["EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditIn"] = t.struct(
        {"resolvedBy": t.string(), "resolvedByCpi": t.string(), "timestamp": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditIn"])
    types["EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditOut"] = t.struct(
        {
            "resolvedBy": t.string(),
            "resolvedByCpi": t.string(),
            "timestamp": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditOut"])
    types["GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsIn"] = t.struct(
        {
            "password": t.string().optional(),
            "clientSecret": t.string().optional(),
            "scope": t.string().optional(),
            "clientId": t.string().optional(),
            "tokenParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapIn"]
            ).optional(),
            "accessToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAccessTokenIn"]
            ).optional(),
            "username": t.string().optional(),
            "tokenEndpoint": t.string().optional(),
            "requestType": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsIn"])
    types["GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsOut"] = t.struct(
        {
            "password": t.string().optional(),
            "clientSecret": t.string().optional(),
            "scope": t.string().optional(),
            "clientId": t.string().optional(),
            "tokenParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapOut"]
            ).optional(),
            "accessToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAccessTokenOut"]
            ).optional(),
            "username": t.string().optional(),
            "tokenEndpoint": t.string().optional(),
            "requestType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsOut"])
    types["EnterpriseCrmEventbusProtoParameterValueTypeIn"] = t.struct(
        {
            "doubleArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoDoubleParameterArrayIn"]
            ),
            "intArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoIntParameterArrayIn"]
            ),
            "stringArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoStringParameterArrayIn"]
            ),
            "booleanValue": t.boolean(),
            "stringValue": t.string(),
            "intValue": t.string(),
            "protoValue": t.struct({"_": t.string().optional()}),
            "doubleValue": t.number(),
            "serializedObjectValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoSerializedObjectParameterIn"]
            ),
            "booleanArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoBooleanParameterArrayIn"]
            ),
            "protoArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoProtoParameterArrayIn"]
            ),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParameterValueTypeIn"])
    types["EnterpriseCrmEventbusProtoParameterValueTypeOut"] = t.struct(
        {
            "doubleArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoDoubleParameterArrayOut"]
            ),
            "intArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoIntParameterArrayOut"]
            ),
            "stringArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoStringParameterArrayOut"]
            ),
            "booleanValue": t.boolean(),
            "stringValue": t.string(),
            "intValue": t.string(),
            "protoValue": t.struct({"_": t.string().optional()}),
            "doubleValue": t.number(),
            "serializedObjectValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoSerializedObjectParameterOut"]
            ),
            "booleanArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoBooleanParameterArrayOut"]
            ),
            "protoArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoProtoParameterArrayOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParameterValueTypeOut"])
    types["EnterpriseCrmEventbusProtoWorkflowAlertConfigIn"] = t.struct(
        {
            "thresholdType": t.string().optional(),
            "errorEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn"]
            ),
            "aggregationPeriod": t.string().optional(),
            "alertDisabled": t.boolean().optional(),
            "playbookUrl": t.string().optional(),
            "alertName": t.string().optional(),
            "durationThresholdMs": t.string().optional(),
            "warningEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn"]
            ),
            "metricType": t.string(),
            "thresholdValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueIn"]
            ).optional(),
            "numAggregationPeriods": t.integer().optional(),
            "clientId": t.string().optional(),
            "onlyFinalAttempt": t.boolean().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoWorkflowAlertConfigIn"])
    types["EnterpriseCrmEventbusProtoWorkflowAlertConfigOut"] = t.struct(
        {
            "thresholdType": t.string().optional(),
            "errorEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut"]
            ),
            "aggregationPeriod": t.string().optional(),
            "alertDisabled": t.boolean().optional(),
            "playbookUrl": t.string().optional(),
            "alertName": t.string().optional(),
            "durationThresholdMs": t.string().optional(),
            "warningEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut"]
            ),
            "metricType": t.string(),
            "thresholdValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueOut"]
            ).optional(),
            "numAggregationPeriods": t.integer().optional(),
            "clientId": t.string().optional(),
            "onlyFinalAttempt": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoWorkflowAlertConfigOut"])
    types["EnterpriseCrmEventbusProtoSuspensionExpirationIn"] = t.struct(
        {
            "remindAfterMs": t.integer().optional(),
            "expireAfterMs": t.integer().optional(),
            "liftWhenExpired": t.boolean().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionExpirationIn"])
    types["EnterpriseCrmEventbusProtoSuspensionExpirationOut"] = t.struct(
        {
            "remindAfterMs": t.integer().optional(),
            "expireAfterMs": t.integer().optional(),
            "liftWhenExpired": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionExpirationOut"])
    types["EnterpriseCrmEventbusProtoSuspensionConfigIn"] = t.struct(
        {
            "customMessage": t.string().optional(),
            "suspensionExpiration": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionExpirationIn"]
            ).optional(),
            "whoMayResolve": t.array(
                t.proxy(
                    renames["EnterpriseCrmEventbusProtoSuspensionAuthPermissionsIn"]
                )
            ).optional(),
            "notifications": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoNotificationIn"])
            ),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionConfigIn"])
    types["EnterpriseCrmEventbusProtoSuspensionConfigOut"] = t.struct(
        {
            "customMessage": t.string().optional(),
            "suspensionExpiration": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionExpirationOut"]
            ).optional(),
            "whoMayResolve": t.array(
                t.proxy(
                    renames["EnterpriseCrmEventbusProtoSuspensionAuthPermissionsOut"]
                )
            ).optional(),
            "notifications": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoNotificationOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionConfigOut"])
    types["EnterpriseCrmEventbusProtoParameterEntryIn"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParameterEntryIn"])
    types["EnterpriseCrmEventbusProtoParameterEntryOut"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParameterEntryOut"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterMapEntryIn"] = t.struct(
        {
            "value": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterMapFieldIn"]
            ),
            "key": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterMapFieldIn"]
            ),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterMapEntryIn"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterMapEntryOut"] = t.struct(
        {
            "value": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterMapFieldOut"]
            ),
            "key": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterMapFieldOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterMapEntryOut"])
    types["EnterpriseCrmEventbusProtoDoubleArrayFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoDoubleArrayFunctionIn"])
    types["EnterpriseCrmEventbusProtoDoubleArrayFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoDoubleArrayFunctionOut"])
    types["EnterpriseCrmEventbusProtoParameterMapEntryIn"] = t.struct(
        {
            "value": t.proxy(renames["EnterpriseCrmEventbusProtoParameterMapFieldIn"]),
            "key": t.proxy(renames["EnterpriseCrmEventbusProtoParameterMapFieldIn"]),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParameterMapEntryIn"])
    types["EnterpriseCrmEventbusProtoParameterMapEntryOut"] = t.struct(
        {
            "value": t.proxy(renames["EnterpriseCrmEventbusProtoParameterMapFieldOut"]),
            "key": t.proxy(renames["EnterpriseCrmEventbusProtoParameterMapFieldOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParameterMapEntryOut"])
    types["GoogleCloudIntegrationsV1alphaCloudSchedulerConfigIn"] = t.struct(
        {
            "location": t.string(),
            "errorMessage": t.string().optional(),
            "serviceAccountEmail": t.string(),
            "cronTab": t.string(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCloudSchedulerConfigIn"])
    types["GoogleCloudIntegrationsV1alphaCloudSchedulerConfigOut"] = t.struct(
        {
            "location": t.string(),
            "errorMessage": t.string().optional(),
            "serviceAccountEmail": t.string(),
            "cronTab": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCloudSchedulerConfigOut"])
    types[
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexIn"
    ] = t.struct(
        {"exclusive": t.boolean().optional(), "regex": t.string().optional()}
    ).named(
        renames["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexIn"]
    )
    types[
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexOut"
    ] = t.struct(
        {
            "exclusive": t.boolean().optional(),
            "regex": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexOut"]
    )
    types["GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionIn"] = t.struct(
        {
            "parentIntegrationVersionId": t.string().optional(),
            "status": t.string().optional(),
            "errorCatcherConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn"])
            ).optional(),
            "databasePersistencePolicy": t.string().optional(),
            "userLabel": t.string().optional(),
            "lastModifierEmail": t.string().optional(),
            "triggerConfigs": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn"])
            ).optional(),
            "taskConfigs": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigIn"])
            ).optional(),
            "teardown": t.proxy(
                renames["EnterpriseCrmEventbusProtoTeardownIn"]
            ).optional(),
            "description": t.string().optional(),
            "templateParameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionIn"])
    types["GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionOut"] = t.struct(
        {
            "parentIntegrationVersionId": t.string().optional(),
            "status": t.string().optional(),
            "errorCatcherConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigOut"])
            ).optional(),
            "createTime": t.string().optional(),
            "databasePersistencePolicy": t.string().optional(),
            "userLabel": t.string().optional(),
            "lastModifierEmail": t.string().optional(),
            "triggerConfigs": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigOut"])
            ).optional(),
            "taskConfigs": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigOut"])
            ).optional(),
            "snapshotNumber": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "teardown": t.proxy(
                renames["EnterpriseCrmEventbusProtoTeardownOut"]
            ).optional(),
            "description": t.string().optional(),
            "templateParameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionOut"])
    types["EnterpriseCrmEventbusProtoBuganizerNotificationIn"] = t.struct(
        {
            "componentId": t.string().optional(),
            "templateId": t.string().optional(),
            "title": t.string().optional(),
            "assigneeEmailAddress": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBuganizerNotificationIn"])
    types["EnterpriseCrmEventbusProtoBuganizerNotificationOut"] = t.struct(
        {
            "componentId": t.string().optional(),
            "templateId": t.string().optional(),
            "title": t.string().optional(),
            "assigneeEmailAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBuganizerNotificationOut"])
    types["GoogleCloudIntegrationsV1alphaAuthConfigIn"] = t.struct(
        {
            "lastModifierEmail": t.string().optional(),
            "state": t.string().optional(),
            "credentialType": t.string().optional(),
            "validTime": t.string().optional(),
            "description": t.string().optional(),
            "encryptedCredential": t.string().optional(),
            "overrideValidTime": t.string().optional(),
            "name": t.string().optional(),
            "creatorEmail": t.string().optional(),
            "reason": t.string().optional(),
            "decryptedCredential": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCredentialIn"]
            ).optional(),
            "visibility": t.string().optional(),
            "displayName": t.string().optional(),
            "certificateId": t.string().optional(),
            "expiryNotificationDuration": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaAuthConfigIn"])
    types["GoogleCloudIntegrationsV1alphaAuthConfigOut"] = t.struct(
        {
            "lastModifierEmail": t.string().optional(),
            "state": t.string().optional(),
            "credentialType": t.string().optional(),
            "validTime": t.string().optional(),
            "description": t.string().optional(),
            "encryptedCredential": t.string().optional(),
            "overrideValidTime": t.string().optional(),
            "name": t.string().optional(),
            "creatorEmail": t.string().optional(),
            "reason": t.string().optional(),
            "decryptedCredential": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCredentialOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "visibility": t.string().optional(),
            "displayName": t.string().optional(),
            "certificateId": t.string().optional(),
            "expiryNotificationDuration": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaAuthConfigOut"])
    types["EnterpriseCrmEventbusProtoScatterResponseIn"] = t.struct(
        {
            "scatterElement": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeIn"]
            ).optional(),
            "responseParams": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoParameterEntryIn"])
            ).optional(),
            "errorMsg": t.string().optional(),
            "isSuccessful": t.boolean().optional(),
            "executionIds": t.array(t.string()).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoScatterResponseIn"])
    types["EnterpriseCrmEventbusProtoScatterResponseOut"] = t.struct(
        {
            "scatterElement": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "responseParams": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoParameterEntryOut"])
            ).optional(),
            "errorMsg": t.string().optional(),
            "isSuccessful": t.boolean().optional(),
            "executionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoScatterResponseOut"])
    types["GoogleCloudConnectorsV1SecretIn"] = t.struct(
        {"secretVersion": t.string().optional()}
    ).named(renames["GoogleCloudConnectorsV1SecretIn"])
    types["GoogleCloudConnectorsV1SecretOut"] = t.struct(
        {
            "secretVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1SecretOut"])
    types["EnterpriseCrmEventbusProtoCoordinateIn"] = t.struct(
        {"y": t.integer(), "x": t.integer()}
    ).named(renames["EnterpriseCrmEventbusProtoCoordinateIn"])
    types["EnterpriseCrmEventbusProtoCoordinateOut"] = t.struct(
        {
            "y": t.integer(),
            "x": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoCoordinateOut"])
    types["GoogleCloudConnectorsV1DestinationIn"] = t.struct(
        {
            "host": t.string().optional(),
            "port": t.integer().optional(),
            "serviceAttachment": t.string().optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1DestinationIn"])
    types["GoogleCloudConnectorsV1DestinationOut"] = t.struct(
        {
            "host": t.string().optional(),
            "port": t.integer().optional(),
            "serviceAttachment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1DestinationOut"])
    types["EnterpriseCrmEventbusProtoTaskUiConfigIn"] = t.struct(
        {
            "taskUiModuleConfigs": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskUiModuleConfigIn"])
            ).optional()
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskUiConfigIn"])
    types["EnterpriseCrmEventbusProtoTaskUiConfigOut"] = t.struct(
        {
            "taskUiModuleConfigs": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskUiModuleConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskUiConfigOut"])
    types["EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayIn"] = t.struct(
        {"doubleValues": t.array(t.number())}
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayIn"])
    types["EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayOut"] = t.struct(
        {
            "doubleValues": t.array(t.number()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayOut"])
    types["EnterpriseCrmEventbusProtoBooleanFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoBooleanFunctionIn"])
    types["EnterpriseCrmEventbusProtoBooleanFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBooleanFunctionOut"])
    types["EnterpriseCrmEventbusProtoSuspensionAuthPermissionsIn"] = t.struct(
        {
            "googleGroup": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityIn"
                ]
            ),
            "loasRole": t.string(),
            "mdbGroup": t.string(),
            "gaiaIdentity": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityIn"
                ]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionAuthPermissionsIn"])
    types["EnterpriseCrmEventbusProtoSuspensionAuthPermissionsOut"] = t.struct(
        {
            "googleGroup": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityOut"
                ]
            ),
            "loasRole": t.string(),
            "mdbGroup": t.string(),
            "gaiaIdentity": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionAuthPermissionsOut"])
    types["EnterpriseCrmEventbusProtoStringParameterArrayIn"] = t.struct(
        {"stringValues": t.array(t.string())}
    ).named(renames["EnterpriseCrmEventbusProtoStringParameterArrayIn"])
    types["EnterpriseCrmEventbusProtoStringParameterArrayOut"] = t.struct(
        {
            "stringValues": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoStringParameterArrayOut"])
    types["EnterpriseCrmLoggingGwsFieldLimitsIn"] = t.struct(
        {
            "logType": t.array(t.string()).optional(),
            "maxStringLength": t.integer().optional(),
            "shortenerType": t.string(),
            "logAction": t.string(),
            "maxArraySize": t.integer().optional(),
        }
    ).named(renames["EnterpriseCrmLoggingGwsFieldLimitsIn"])
    types["EnterpriseCrmLoggingGwsFieldLimitsOut"] = t.struct(
        {
            "logType": t.array(t.string()).optional(),
            "maxStringLength": t.integer().optional(),
            "shortenerType": t.string(),
            "logAction": t.string(),
            "maxArraySize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmLoggingGwsFieldLimitsOut"])
    types["GoogleCloudIntegrationsV1alphaStringParameterArrayIn"] = t.struct(
        {"stringValues": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaStringParameterArrayIn"])
    types["GoogleCloudIntegrationsV1alphaStringParameterArrayOut"] = t.struct(
        {
            "stringValues": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaStringParameterArrayOut"])
    types[
        "GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseIn"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "runtimeEntitySchemas": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaIn"])
            ).optional(),
        }
    ).named(
        renames["GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseIn"]
    )
    types[
        "GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "runtimeEntitySchemas": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseOut"]
    )
    types["EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn"] = t.struct(
        {
            "label": t.string().optional(),
            "triggerCriteria": t.proxy(
                renames["EnterpriseCrmEventbusProtoTriggerCriteriaIn"]
            ).optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "triggerId": t.string().optional(),
            "position": t.proxy(
                renames["EnterpriseCrmEventbusProtoCoordinateIn"]
            ).optional(),
            "enabledClients": t.array(t.string()),
            "pauseWorkflowExecutions": t.boolean().optional(),
            "startTasks": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoNextTaskIn"])
            ).optional(),
            "cloudSchedulerConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoCloudSchedulerConfigIn"]
            ),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "errorCatcherId": t.string().optional(),
            "triggerName": t.string().optional(),
            "alertConfig": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoWorkflowAlertConfigIn"])
            ).optional(),
            "description": t.string().optional(),
            "triggerNumber": t.string(),
            "triggerType": t.string(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn"])
    types["EnterpriseCrmFrontendsEventbusProtoTriggerConfigOut"] = t.struct(
        {
            "label": t.string().optional(),
            "triggerCriteria": t.proxy(
                renames["EnterpriseCrmEventbusProtoTriggerCriteriaOut"]
            ).optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "triggerId": t.string().optional(),
            "position": t.proxy(
                renames["EnterpriseCrmEventbusProtoCoordinateOut"]
            ).optional(),
            "enabledClients": t.array(t.string()),
            "pauseWorkflowExecutions": t.boolean().optional(),
            "startTasks": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoNextTaskOut"])
            ).optional(),
            "cloudSchedulerConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoCloudSchedulerConfigOut"]
            ),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "errorCatcherId": t.string().optional(),
            "triggerName": t.string().optional(),
            "alertConfig": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoWorkflowAlertConfigOut"])
            ).optional(),
            "description": t.string().optional(),
            "triggerNumber": t.string(),
            "triggerType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigOut"])
    types["GoogleCloudIntegrationsV1alphaSuspensionIn"] = t.struct(
        {
            "approvalConfig": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigIn"]
            ).optional(),
            "name": t.string().optional(),
            "eventExecutionInfoId": t.string(),
            "audit": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuspensionAuditIn"]
            ).optional(),
            "suspensionConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionConfigIn"]
            ).optional(),
            "state": t.string(),
            "integration": t.string(),
            "taskId": t.string(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSuspensionIn"])
    types["GoogleCloudIntegrationsV1alphaSuspensionOut"] = t.struct(
        {
            "approvalConfig": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigOut"]
            ).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "eventExecutionInfoId": t.string(),
            "lastModifyTime": t.string().optional(),
            "audit": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuspensionAuditOut"]
            ).optional(),
            "suspensionConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionConfigOut"]
            ).optional(),
            "state": t.string(),
            "integration": t.string(),
            "taskId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSuspensionOut"])
    types["EnterpriseCrmEventbusProtoCloudSchedulerConfigIn"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "location": t.string(),
            "cronTab": t.string(),
            "serviceAccountEmail": t.string(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoCloudSchedulerConfigIn"])
    types["EnterpriseCrmEventbusProtoCloudSchedulerConfigOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "location": t.string(),
            "cronTab": t.string(),
            "serviceAccountEmail": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoCloudSchedulerConfigOut"])
    types["GoogleCloudIntegrationsV1alphaIntegrationParameterIn"] = t.struct(
        {
            "producer": t.string().optional(),
            "isTransient": t.boolean().optional(),
            "defaultValue": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaValueTypeIn"]
            ).optional(),
            "dataType": t.string().optional(),
            "displayName": t.string().optional(),
            "searchable": t.boolean().optional(),
            "inputOutputType": t.string().optional(),
            "jsonSchema": t.string().optional(),
            "key": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationParameterIn"])
    types["GoogleCloudIntegrationsV1alphaIntegrationParameterOut"] = t.struct(
        {
            "producer": t.string().optional(),
            "isTransient": t.boolean().optional(),
            "defaultValue": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaValueTypeOut"]
            ).optional(),
            "dataType": t.string().optional(),
            "displayName": t.string().optional(),
            "searchable": t.boolean().optional(),
            "inputOutputType": t.string().optional(),
            "jsonSchema": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationParameterOut"])
    types["GoogleCloudIntegrationsV1alphaRuntimeActionSchemaIn"] = t.struct(
        {
            "inputSchema": t.string().optional(),
            "outputSchema": t.string().optional(),
            "action": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaRuntimeActionSchemaIn"])
    types["GoogleCloudIntegrationsV1alphaRuntimeActionSchemaOut"] = t.struct(
        {
            "inputSchema": t.string().optional(),
            "outputSchema": t.string().optional(),
            "action": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaRuntimeActionSchemaOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types[
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeIn"
    ] = t.struct({"min": t.number().optional(), "max": t.number().optional()}).named(
        renames["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeIn"]
    )
    types[
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeOut"
    ] = t.struct(
        {
            "min": t.number().optional(),
            "max": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeOut"]
    )
    types["GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequestIn"] = t.struct(
        {
            "appsScriptProject": t.string().optional(),
            "authConfigId": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequestIn"])
    types["GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequestOut"] = t.struct(
        {
            "appsScriptProject": t.string().optional(),
            "authConfigId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequestOut"])
    types["EnterpriseCrmEventbusProtoProtoFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoProtoFunctionIn"])
    types["EnterpriseCrmEventbusProtoProtoFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoProtoFunctionOut"])
    types[
        "EnterpriseCrmEventbusProtoConnectorsGenericConnectorTaskConfigIn"
    ] = t.struct(
        {
            "connection": t.proxy(
                renames["EnterpriseCrmEventbusProtoConnectorsConnectionIn"]
            ).optional(),
            "operation": t.string().optional(),
        }
    ).named(
        renames["EnterpriseCrmEventbusProtoConnectorsGenericConnectorTaskConfigIn"]
    )
    types[
        "EnterpriseCrmEventbusProtoConnectorsGenericConnectorTaskConfigOut"
    ] = t.struct(
        {
            "connection": t.proxy(
                renames["EnterpriseCrmEventbusProtoConnectorsConnectionOut"]
            ).optional(),
            "operation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["EnterpriseCrmEventbusProtoConnectorsGenericConnectorTaskConfigOut"]
    )
    types["GoogleCloudIntegrationsV1alphaListExecutionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "executionInfos": t.array(
                t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoIn"]
                )
            ),
            "executions": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaExecutionIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListExecutionsResponseIn"])
    types["GoogleCloudIntegrationsV1alphaListExecutionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "executionInfos": t.array(
                t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoOut"]
                )
            ),
            "executions": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaExecutionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListExecutionsResponseOut"])
    types["GoogleCloudIntegrationsV1alphaParameterMapIn"] = t.struct(
        {
            "valueType": t.string().optional(),
            "keyType": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaParameterMapEntryIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaParameterMapIn"])
    types["GoogleCloudIntegrationsV1alphaParameterMapOut"] = t.struct(
        {
            "valueType": t.string().optional(),
            "keyType": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaParameterMapEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaParameterMapOut"])
    types["GoogleCloudConnectorsV1SslConfigIn"] = t.struct(
        {
            "additionalVariables": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConfigVariableIn"])
            ).optional(),
            "clientCertType": t.string().optional(),
            "serverCertType": t.string().optional(),
            "type": t.string().optional(),
            "privateServerCertificate": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
            "clientPrivateKey": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
            "trustModel": t.string().optional(),
            "useSsl": t.boolean().optional(),
            "clientPrivateKeyPass": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
            "clientCertificate": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1SslConfigIn"])
    types["GoogleCloudConnectorsV1SslConfigOut"] = t.struct(
        {
            "additionalVariables": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConfigVariableOut"])
            ).optional(),
            "clientCertType": t.string().optional(),
            "serverCertType": t.string().optional(),
            "type": t.string().optional(),
            "privateServerCertificate": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "clientPrivateKey": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "trustModel": t.string().optional(),
            "useSsl": t.boolean().optional(),
            "clientPrivateKeyPass": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "clientCertificate": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1SslConfigOut"])
    types["EnterpriseCrmEventbusStatsIn"] = t.struct(
        {
            "durationInSeconds": t.number().optional(),
            "dimensions": t.proxy(
                renames["EnterpriseCrmEventbusStatsDimensionsIn"]
            ).optional(),
            "qps": t.number().optional(),
            "errorRate": t.number().optional(),
            "warningRate": t.number().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusStatsIn"])
    types["EnterpriseCrmEventbusStatsOut"] = t.struct(
        {
            "durationInSeconds": t.number().optional(),
            "dimensions": t.proxy(
                renames["EnterpriseCrmEventbusStatsDimensionsOut"]
            ).optional(),
            "qps": t.number().optional(),
            "errorRate": t.number().optional(),
            "warningRate": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusStatsOut"])
    types["EnterpriseCrmEventbusProtoFieldMappingConfigIn"] = t.struct(
        {
            "mappedFields": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoMappedFieldIn"])
            )
        }
    ).named(renames["EnterpriseCrmEventbusProtoFieldMappingConfigIn"])
    types["EnterpriseCrmEventbusProtoFieldMappingConfigOut"] = t.struct(
        {
            "mappedFields": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoMappedFieldOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFieldMappingConfigOut"])
    types["EnterpriseCrmEventbusProtoCloudKmsConfigIn"] = t.struct(
        {
            "locationName": t.string().optional(),
            "keyName": t.string().optional(),
            "keyRingName": t.string().optional(),
            "gcpProjectId": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "keyVersionName": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoCloudKmsConfigIn"])
    types["EnterpriseCrmEventbusProtoCloudKmsConfigOut"] = t.struct(
        {
            "locationName": t.string().optional(),
            "keyName": t.string().optional(),
            "keyRingName": t.string().optional(),
            "gcpProjectId": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "keyVersionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoCloudKmsConfigOut"])
    types["GoogleCloudIntegrationsV1alphaListAuthConfigsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "authConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaAuthConfigIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListAuthConfigsResponseIn"])
    types["GoogleCloudIntegrationsV1alphaListAuthConfigsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "authConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaAuthConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListAuthConfigsResponseOut"])
    types["GoogleCloudIntegrationsV1alphaValueTypeIn"] = t.struct(
        {
            "stringArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaStringParameterArrayIn"]
            ).optional(),
            "intArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaIntParameterArrayIn"]
            ).optional(),
            "doubleArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaDoubleParameterArrayIn"]
            ).optional(),
            "booleanValue": t.boolean().optional(),
            "jsonValue": t.string().optional(),
            "stringValue": t.string().optional(),
            "intValue": t.string().optional(),
            "doubleValue": t.number().optional(),
            "booleanArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaBooleanParameterArrayIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaValueTypeIn"])
    types["GoogleCloudIntegrationsV1alphaValueTypeOut"] = t.struct(
        {
            "stringArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaStringParameterArrayOut"]
            ).optional(),
            "intArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaIntParameterArrayOut"]
            ).optional(),
            "doubleArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaDoubleParameterArrayOut"]
            ).optional(),
            "booleanValue": t.boolean().optional(),
            "jsonValue": t.string().optional(),
            "stringValue": t.string().optional(),
            "intValue": t.string().optional(),
            "doubleValue": t.number().optional(),
            "booleanArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaBooleanParameterArrayOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaValueTypeOut"])

    functions = {}
    functions["projectsLocationsAuthConfigsDelete"] = integrations.get(
        "v1alpha/{parent}/authConfigs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListAuthConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthConfigsPatch"] = integrations.get(
        "v1alpha/{parent}/authConfigs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListAuthConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthConfigsCreate"] = integrations.get(
        "v1alpha/{parent}/authConfigs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListAuthConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthConfigsGet"] = integrations.get(
        "v1alpha/{parent}/authConfigs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListAuthConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthConfigsList"] = integrations.get(
        "v1alpha/{parent}/authConfigs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListAuthConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCertificatesGet"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaCertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsList"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConnectionsGetConnectionSchemaMetadata"
    ] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConnectionsRuntimeActionSchemasList"
    ] = integrations.get(
        "v1alpha/{parent}/runtimeActionSchemas",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConnectionsRuntimeEntitySchemasList"
    ] = integrations.get(
        "v1alpha/{parent}/runtimeEntitySchemas",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesCreate"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "sfdcOrgId": t.string().optional(),
                "displayName": t.string().optional(),
                "authConfigId": t.array(t.string()).optional(),
                "serviceAuthority": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesDelete"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "sfdcOrgId": t.string().optional(),
                "displayName": t.string().optional(),
                "authConfigId": t.array(t.string()).optional(),
                "serviceAuthority": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesList"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "sfdcOrgId": t.string().optional(),
                "displayName": t.string().optional(),
                "authConfigId": t.array(t.string()).optional(),
                "serviceAuthority": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesGet"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "sfdcOrgId": t.string().optional(),
                "displayName": t.string().optional(),
                "authConfigId": t.array(t.string()).optional(),
                "serviceAuthority": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesPatch"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "sfdcOrgId": t.string().optional(),
                "displayName": t.string().optional(),
                "authConfigId": t.array(t.string()).optional(),
                "serviceAuthority": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesSfdcChannelsGet"] = integrations.post(
        "v1alpha/{parent}/sfdcChannels",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string().optional(),
                "isActive": t.boolean().optional(),
                "lastReplayId": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "channelTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesSfdcChannelsPatch"] = integrations.post(
        "v1alpha/{parent}/sfdcChannels",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string().optional(),
                "isActive": t.boolean().optional(),
                "lastReplayId": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "channelTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesSfdcChannelsList"] = integrations.post(
        "v1alpha/{parent}/sfdcChannels",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string().optional(),
                "isActive": t.boolean().optional(),
                "lastReplayId": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "channelTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesSfdcChannelsDelete"] = integrations.post(
        "v1alpha/{parent}/sfdcChannels",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string().optional(),
                "isActive": t.boolean().optional(),
                "lastReplayId": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "channelTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesSfdcChannelsCreate"] = integrations.post(
        "v1alpha/{parent}/sfdcChannels",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string().optional(),
                "isActive": t.boolean().optional(),
                "lastReplayId": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "channelTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsSchedule"] = integrations.get(
        "v1alpha/{parent}/integrations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListIntegrationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsDelete"] = integrations.get(
        "v1alpha/{parent}/integrations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListIntegrationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsExecute"] = integrations.get(
        "v1alpha/{parent}/integrations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListIntegrationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsList"] = integrations.get(
        "v1alpha/{parent}/integrations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListIntegrationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsVersionsTakeoverEditLock"
    ] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsVersionsPatch"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsVersionsUnpublish"
    ] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsVersionsUpload"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsVersionsDelete"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsVersionsPublish"
    ] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsVersionsDownload"
    ] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsVersionsList"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsVersionsCreate"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsVersionsGet"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsExecutionsCancel"
    ] = integrations.get(
        "v1alpha/{parent}/executions",
        t.struct(
            {
                "filterParams.parameterValue": t.string().optional(),
                "filterParams.endTime": t.string().optional(),
                "filterParams.parameterPairValue": t.string().optional(),
                "filterParams.workflowName": t.string().optional(),
                "filter": t.string().optional(),
                "filterParams.startTime": t.string().optional(),
                "filterParams.parameterKey": t.string().optional(),
                "filterParams.customFilter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "refreshAcl": t.boolean().optional(),
                "filterParams.taskStatuses": t.string().optional(),
                "truncateParams": t.boolean().optional(),
                "filterParams.eventStatuses": t.string().optional(),
                "filterParams.executionId": t.string().optional(),
                "filterParams.parameterPairKey": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "filterParams.parameterType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListExecutionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsExecutionsGet"] = integrations.get(
        "v1alpha/{parent}/executions",
        t.struct(
            {
                "filterParams.parameterValue": t.string().optional(),
                "filterParams.endTime": t.string().optional(),
                "filterParams.parameterPairValue": t.string().optional(),
                "filterParams.workflowName": t.string().optional(),
                "filter": t.string().optional(),
                "filterParams.startTime": t.string().optional(),
                "filterParams.parameterKey": t.string().optional(),
                "filterParams.customFilter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "refreshAcl": t.boolean().optional(),
                "filterParams.taskStatuses": t.string().optional(),
                "truncateParams": t.boolean().optional(),
                "filterParams.eventStatuses": t.string().optional(),
                "filterParams.executionId": t.string().optional(),
                "filterParams.parameterPairKey": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "filterParams.parameterType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListExecutionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsExecutionsList"] = integrations.get(
        "v1alpha/{parent}/executions",
        t.struct(
            {
                "filterParams.parameterValue": t.string().optional(),
                "filterParams.endTime": t.string().optional(),
                "filterParams.parameterPairValue": t.string().optional(),
                "filterParams.workflowName": t.string().optional(),
                "filter": t.string().optional(),
                "filterParams.startTime": t.string().optional(),
                "filterParams.parameterKey": t.string().optional(),
                "filterParams.customFilter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "refreshAcl": t.boolean().optional(),
                "filterParams.taskStatuses": t.string().optional(),
                "truncateParams": t.boolean().optional(),
                "filterParams.eventStatuses": t.string().optional(),
                "filterParams.executionId": t.string().optional(),
                "filterParams.parameterPairKey": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "filterParams.parameterType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListExecutionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsExecutionsSuspensionsLift"
    ] = integrations.get(
        "v1alpha/{parent}/suspensions",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListSuspensionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsExecutionsSuspensionsResolve"
    ] = integrations.get(
        "v1alpha/{parent}/suspensions",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListSuspensionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsExecutionsSuspensionsList"
    ] = integrations.get(
        "v1alpha/{parent}/suspensions",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListSuspensionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsCertificatesPatch"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsCertificatesGet"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsCertificatesCreate"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsCertificatesList"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsCertificatesDelete"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationtemplatesVersionsList"
    ] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationtemplatesVersionsCreate"
    ] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationtemplatesVersionsGet"
    ] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsSfdcInstancesGet"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "sfdcOrgId": t.string().optional(),
                "displayName": t.string().optional(),
                "authConfigId": t.array(t.string()).optional(),
                "serviceAuthority": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsSfdcInstancesList"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "sfdcOrgId": t.string().optional(),
                "displayName": t.string().optional(),
                "authConfigId": t.array(t.string()).optional(),
                "serviceAuthority": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsSfdcInstancesDelete"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "sfdcOrgId": t.string().optional(),
                "displayName": t.string().optional(),
                "authConfigId": t.array(t.string()).optional(),
                "serviceAuthority": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsSfdcInstancesCreate"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "sfdcOrgId": t.string().optional(),
                "displayName": t.string().optional(),
                "authConfigId": t.array(t.string()).optional(),
                "serviceAuthority": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsSfdcInstancesPatch"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "sfdcOrgId": t.string().optional(),
                "displayName": t.string().optional(),
                "authConfigId": t.array(t.string()).optional(),
                "serviceAuthority": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsSfdcInstancesSfdcChannelsPatch"
    ] = integrations.post(
        "v1alpha/{parent}/sfdcChannels",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string().optional(),
                "isActive": t.boolean().optional(),
                "lastReplayId": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "channelTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsSfdcInstancesSfdcChannelsList"
    ] = integrations.post(
        "v1alpha/{parent}/sfdcChannels",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string().optional(),
                "isActive": t.boolean().optional(),
                "lastReplayId": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "channelTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsSfdcInstancesSfdcChannelsDelete"
    ] = integrations.post(
        "v1alpha/{parent}/sfdcChannels",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string().optional(),
                "isActive": t.boolean().optional(),
                "lastReplayId": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "channelTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsSfdcInstancesSfdcChannelsGet"
    ] = integrations.post(
        "v1alpha/{parent}/sfdcChannels",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string().optional(),
                "isActive": t.boolean().optional(),
                "lastReplayId": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "channelTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsSfdcInstancesSfdcChannelsCreate"
    ] = integrations.post(
        "v1alpha/{parent}/sfdcChannels",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string().optional(),
                "isActive": t.boolean().optional(),
                "lastReplayId": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "channelTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsAuthConfigsGet"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsAuthConfigsPatch"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsAuthConfigsList"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsAuthConfigsCreate"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsAuthConfigsDelete"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppsScriptProjectsCreate"] = integrations.post(
        "v1alpha/{parent}/appsScriptProjects:link",
        t.struct(
            {
                "parent": t.string(),
                "scriptId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppsScriptProjectsLink"] = integrations.post(
        "v1alpha/{parent}/appsScriptProjects:link",
        t.struct(
            {
                "parent": t.string(),
                "scriptId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsSchedule"] = integrations.get(
        "v1alpha/{parent}/integrations",
        t.struct(
            {
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListIntegrationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsExecuteEvent"] = integrations.get(
        "v1alpha/{parent}/integrations",
        t.struct(
            {
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListIntegrationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsDelete"] = integrations.get(
        "v1alpha/{parent}/integrations",
        t.struct(
            {
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListIntegrationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsExecute"] = integrations.get(
        "v1alpha/{parent}/integrations",
        t.struct(
            {
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListIntegrationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsList"] = integrations.get(
        "v1alpha/{parent}/integrations",
        t.struct(
            {
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListIntegrationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsDelete"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "runAsServiceAccount": t.string().optional(),
                "errorCatcherConfigs": t.array(
                    t.proxy(
                        renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn"]
                    )
                ).optional(),
                "taskConfigs": t.array(
                    t.proxy(renames["GoogleCloudIntegrationsV1alphaTaskConfigIn"])
                ).optional(),
                "integrationParameters": t.array(
                    t.proxy(
                        renames["GoogleCloudIntegrationsV1alphaIntegrationParameterIn"]
                    )
                ).optional(),
                "origin": t.string().optional(),
                "triggerConfigs": t.array(
                    t.proxy(renames["GoogleCloudIntegrationsV1alphaTriggerConfigIn"])
                ).optional(),
                "triggerConfigsInternal": t.array(
                    t.proxy(
                        renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn"]
                    )
                ).optional(),
                "lastModifierEmail": t.string().optional(),
                "taskConfigsInternal": t.array(
                    t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigIn"])
                ).optional(),
                "description": t.string().optional(),
                "lockHolder": t.string().optional(),
                "parentTemplateId": t.string().optional(),
                "integrationParametersInternal": t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn"]
                ).optional(),
                "snapshotNumber": t.string().optional(),
                "teardown": t.proxy(
                    renames["EnterpriseCrmEventbusProtoTeardownIn"]
                ).optional(),
                "userLabel": t.string().optional(),
                "databasePersistencePolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsCreate"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "runAsServiceAccount": t.string().optional(),
                "errorCatcherConfigs": t.array(
                    t.proxy(
                        renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn"]
                    )
                ).optional(),
                "taskConfigs": t.array(
                    t.proxy(renames["GoogleCloudIntegrationsV1alphaTaskConfigIn"])
                ).optional(),
                "integrationParameters": t.array(
                    t.proxy(
                        renames["GoogleCloudIntegrationsV1alphaIntegrationParameterIn"]
                    )
                ).optional(),
                "origin": t.string().optional(),
                "triggerConfigs": t.array(
                    t.proxy(renames["GoogleCloudIntegrationsV1alphaTriggerConfigIn"])
                ).optional(),
                "triggerConfigsInternal": t.array(
                    t.proxy(
                        renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn"]
                    )
                ).optional(),
                "lastModifierEmail": t.string().optional(),
                "taskConfigsInternal": t.array(
                    t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigIn"])
                ).optional(),
                "description": t.string().optional(),
                "lockHolder": t.string().optional(),
                "parentTemplateId": t.string().optional(),
                "integrationParametersInternal": t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn"]
                ).optional(),
                "snapshotNumber": t.string().optional(),
                "teardown": t.proxy(
                    renames["EnterpriseCrmEventbusProtoTeardownIn"]
                ).optional(),
                "userLabel": t.string().optional(),
                "databasePersistencePolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsIntegrationsVersionsTakeoverEditLock"
    ] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "runAsServiceAccount": t.string().optional(),
                "errorCatcherConfigs": t.array(
                    t.proxy(
                        renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn"]
                    )
                ).optional(),
                "taskConfigs": t.array(
                    t.proxy(renames["GoogleCloudIntegrationsV1alphaTaskConfigIn"])
                ).optional(),
                "integrationParameters": t.array(
                    t.proxy(
                        renames["GoogleCloudIntegrationsV1alphaIntegrationParameterIn"]
                    )
                ).optional(),
                "origin": t.string().optional(),
                "triggerConfigs": t.array(
                    t.proxy(renames["GoogleCloudIntegrationsV1alphaTriggerConfigIn"])
                ).optional(),
                "triggerConfigsInternal": t.array(
                    t.proxy(
                        renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn"]
                    )
                ).optional(),
                "lastModifierEmail": t.string().optional(),
                "taskConfigsInternal": t.array(
                    t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigIn"])
                ).optional(),
                "description": t.string().optional(),
                "lockHolder": t.string().optional(),
                "parentTemplateId": t.string().optional(),
                "integrationParametersInternal": t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn"]
                ).optional(),
                "snapshotNumber": t.string().optional(),
                "teardown": t.proxy(
                    renames["EnterpriseCrmEventbusProtoTeardownIn"]
                ).optional(),
                "userLabel": t.string().optional(),
                "databasePersistencePolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsGet"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "runAsServiceAccount": t.string().optional(),
                "errorCatcherConfigs": t.array(
                    t.proxy(
                        renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn"]
                    )
                ).optional(),
                "taskConfigs": t.array(
                    t.proxy(renames["GoogleCloudIntegrationsV1alphaTaskConfigIn"])
                ).optional(),
                "integrationParameters": t.array(
                    t.proxy(
                        renames["GoogleCloudIntegrationsV1alphaIntegrationParameterIn"]
                    )
                ).optional(),
                "origin": t.string().optional(),
                "triggerConfigs": t.array(
                    t.proxy(renames["GoogleCloudIntegrationsV1alphaTriggerConfigIn"])
                ).optional(),
                "triggerConfigsInternal": t.array(
                    t.proxy(
                        renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn"]
                    )
                ).optional(),
                "lastModifierEmail": t.string().optional(),
                "taskConfigsInternal": t.array(
                    t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigIn"])
                ).optional(),
                "description": t.string().optional(),
                "lockHolder": t.string().optional(),
                "parentTemplateId": t.string().optional(),
                "integrationParametersInternal": t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn"]
                ).optional(),
                "snapshotNumber": t.string().optional(),
                "teardown": t.proxy(
                    renames["EnterpriseCrmEventbusProtoTeardownIn"]
                ).optional(),
                "userLabel": t.string().optional(),
                "databasePersistencePolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsList"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "runAsServiceAccount": t.string().optional(),
                "errorCatcherConfigs": t.array(
                    t.proxy(
                        renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn"]
                    )
                ).optional(),
                "taskConfigs": t.array(
                    t.proxy(renames["GoogleCloudIntegrationsV1alphaTaskConfigIn"])
                ).optional(),
                "integrationParameters": t.array(
                    t.proxy(
                        renames["GoogleCloudIntegrationsV1alphaIntegrationParameterIn"]
                    )
                ).optional(),
                "origin": t.string().optional(),
                "triggerConfigs": t.array(
                    t.proxy(renames["GoogleCloudIntegrationsV1alphaTriggerConfigIn"])
                ).optional(),
                "triggerConfigsInternal": t.array(
                    t.proxy(
                        renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn"]
                    )
                ).optional(),
                "lastModifierEmail": t.string().optional(),
                "taskConfigsInternal": t.array(
                    t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigIn"])
                ).optional(),
                "description": t.string().optional(),
                "lockHolder": t.string().optional(),
                "parentTemplateId": t.string().optional(),
                "integrationParametersInternal": t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn"]
                ).optional(),
                "snapshotNumber": t.string().optional(),
                "teardown": t.proxy(
                    renames["EnterpriseCrmEventbusProtoTeardownIn"]
                ).optional(),
                "userLabel": t.string().optional(),
                "databasePersistencePolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsUpload"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "runAsServiceAccount": t.string().optional(),
                "errorCatcherConfigs": t.array(
                    t.proxy(
                        renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn"]
                    )
                ).optional(),
                "taskConfigs": t.array(
                    t.proxy(renames["GoogleCloudIntegrationsV1alphaTaskConfigIn"])
                ).optional(),
                "integrationParameters": t.array(
                    t.proxy(
                        renames["GoogleCloudIntegrationsV1alphaIntegrationParameterIn"]
                    )
                ).optional(),
                "origin": t.string().optional(),
                "triggerConfigs": t.array(
                    t.proxy(renames["GoogleCloudIntegrationsV1alphaTriggerConfigIn"])
                ).optional(),
                "triggerConfigsInternal": t.array(
                    t.proxy(
                        renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn"]
                    )
                ).optional(),
                "lastModifierEmail": t.string().optional(),
                "taskConfigsInternal": t.array(
                    t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigIn"])
                ).optional(),
                "description": t.string().optional(),
                "lockHolder": t.string().optional(),
                "parentTemplateId": t.string().optional(),
                "integrationParametersInternal": t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn"]
                ).optional(),
                "snapshotNumber": t.string().optional(),
                "teardown": t.proxy(
                    renames["EnterpriseCrmEventbusProtoTeardownIn"]
                ).optional(),
                "userLabel": t.string().optional(),
                "databasePersistencePolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsUnpublish"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "runAsServiceAccount": t.string().optional(),
                "errorCatcherConfigs": t.array(
                    t.proxy(
                        renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn"]
                    )
                ).optional(),
                "taskConfigs": t.array(
                    t.proxy(renames["GoogleCloudIntegrationsV1alphaTaskConfigIn"])
                ).optional(),
                "integrationParameters": t.array(
                    t.proxy(
                        renames["GoogleCloudIntegrationsV1alphaIntegrationParameterIn"]
                    )
                ).optional(),
                "origin": t.string().optional(),
                "triggerConfigs": t.array(
                    t.proxy(renames["GoogleCloudIntegrationsV1alphaTriggerConfigIn"])
                ).optional(),
                "triggerConfigsInternal": t.array(
                    t.proxy(
                        renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn"]
                    )
                ).optional(),
                "lastModifierEmail": t.string().optional(),
                "taskConfigsInternal": t.array(
                    t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigIn"])
                ).optional(),
                "description": t.string().optional(),
                "lockHolder": t.string().optional(),
                "parentTemplateId": t.string().optional(),
                "integrationParametersInternal": t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn"]
                ).optional(),
                "snapshotNumber": t.string().optional(),
                "teardown": t.proxy(
                    renames["EnterpriseCrmEventbusProtoTeardownIn"]
                ).optional(),
                "userLabel": t.string().optional(),
                "databasePersistencePolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsPublish"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "runAsServiceAccount": t.string().optional(),
                "errorCatcherConfigs": t.array(
                    t.proxy(
                        renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn"]
                    )
                ).optional(),
                "taskConfigs": t.array(
                    t.proxy(renames["GoogleCloudIntegrationsV1alphaTaskConfigIn"])
                ).optional(),
                "integrationParameters": t.array(
                    t.proxy(
                        renames["GoogleCloudIntegrationsV1alphaIntegrationParameterIn"]
                    )
                ).optional(),
                "origin": t.string().optional(),
                "triggerConfigs": t.array(
                    t.proxy(renames["GoogleCloudIntegrationsV1alphaTriggerConfigIn"])
                ).optional(),
                "triggerConfigsInternal": t.array(
                    t.proxy(
                        renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn"]
                    )
                ).optional(),
                "lastModifierEmail": t.string().optional(),
                "taskConfigsInternal": t.array(
                    t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigIn"])
                ).optional(),
                "description": t.string().optional(),
                "lockHolder": t.string().optional(),
                "parentTemplateId": t.string().optional(),
                "integrationParametersInternal": t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn"]
                ).optional(),
                "snapshotNumber": t.string().optional(),
                "teardown": t.proxy(
                    renames["EnterpriseCrmEventbusProtoTeardownIn"]
                ).optional(),
                "userLabel": t.string().optional(),
                "databasePersistencePolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsDownload"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "runAsServiceAccount": t.string().optional(),
                "errorCatcherConfigs": t.array(
                    t.proxy(
                        renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn"]
                    )
                ).optional(),
                "taskConfigs": t.array(
                    t.proxy(renames["GoogleCloudIntegrationsV1alphaTaskConfigIn"])
                ).optional(),
                "integrationParameters": t.array(
                    t.proxy(
                        renames["GoogleCloudIntegrationsV1alphaIntegrationParameterIn"]
                    )
                ).optional(),
                "origin": t.string().optional(),
                "triggerConfigs": t.array(
                    t.proxy(renames["GoogleCloudIntegrationsV1alphaTriggerConfigIn"])
                ).optional(),
                "triggerConfigsInternal": t.array(
                    t.proxy(
                        renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn"]
                    )
                ).optional(),
                "lastModifierEmail": t.string().optional(),
                "taskConfigsInternal": t.array(
                    t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigIn"])
                ).optional(),
                "description": t.string().optional(),
                "lockHolder": t.string().optional(),
                "parentTemplateId": t.string().optional(),
                "integrationParametersInternal": t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn"]
                ).optional(),
                "snapshotNumber": t.string().optional(),
                "teardown": t.proxy(
                    renames["EnterpriseCrmEventbusProtoTeardownIn"]
                ).optional(),
                "userLabel": t.string().optional(),
                "databasePersistencePolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsPatch"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "runAsServiceAccount": t.string().optional(),
                "errorCatcherConfigs": t.array(
                    t.proxy(
                        renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn"]
                    )
                ).optional(),
                "taskConfigs": t.array(
                    t.proxy(renames["GoogleCloudIntegrationsV1alphaTaskConfigIn"])
                ).optional(),
                "integrationParameters": t.array(
                    t.proxy(
                        renames["GoogleCloudIntegrationsV1alphaIntegrationParameterIn"]
                    )
                ).optional(),
                "origin": t.string().optional(),
                "triggerConfigs": t.array(
                    t.proxy(renames["GoogleCloudIntegrationsV1alphaTriggerConfigIn"])
                ).optional(),
                "triggerConfigsInternal": t.array(
                    t.proxy(
                        renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn"]
                    )
                ).optional(),
                "lastModifierEmail": t.string().optional(),
                "taskConfigsInternal": t.array(
                    t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigIn"])
                ).optional(),
                "description": t.string().optional(),
                "lockHolder": t.string().optional(),
                "parentTemplateId": t.string().optional(),
                "integrationParametersInternal": t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn"]
                ).optional(),
                "snapshotNumber": t.string().optional(),
                "teardown": t.proxy(
                    renames["EnterpriseCrmEventbusProtoTeardownIn"]
                ).optional(),
                "userLabel": t.string().optional(),
                "databasePersistencePolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsExecutionsList"] = integrations.get(
        "v1alpha/{parent}/executions",
        t.struct(
            {
                "filterParams.customFilter": t.string().optional(),
                "filterParams.endTime": t.string().optional(),
                "filterParams.parameterPairValue": t.string().optional(),
                "filterParams.parameterValue": t.string().optional(),
                "filterParams.parameterKey": t.string().optional(),
                "filterParams.parameterType": t.string().optional(),
                "pageToken": t.string().optional(),
                "filterParams.parameterPairKey": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "filterParams.taskStatuses": t.string().optional(),
                "filterParams.workflowName": t.string().optional(),
                "truncateParams": t.boolean().optional(),
                "filterParams.eventStatuses": t.string().optional(),
                "filterParams.startTime": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "refreshAcl": t.boolean().optional(),
                "filterParams.executionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListExecutionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsIntegrationsExecutionsSuspensionsResolve"
    ] = integrations.post(
        "v1alpha/{name}:lift",
        t.struct(
            {
                "name": t.string(),
                "suspensionResult": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaLiftSuspensionResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsIntegrationsExecutionsSuspensionsList"
    ] = integrations.post(
        "v1alpha/{name}:lift",
        t.struct(
            {
                "name": t.string(),
                "suspensionResult": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaLiftSuspensionResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsIntegrationsExecutionsSuspensionsLift"
    ] = integrations.post(
        "v1alpha/{name}:lift",
        t.struct(
            {
                "name": t.string(),
                "suspensionResult": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaLiftSuspensionResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["connectorPlatformRegionsEnumerate"] = integrations.get(
        "v1alpha/connectorPlatformRegions:enumerate",
        t.struct({"auth": t.string().optional()}),
        t.proxy(
            renames[
                "GoogleCloudIntegrationsV1alphaEnumerateConnectorPlatformRegionsResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["callbackGenerateToken"] = integrations.get(
        "v1alpha/callback:generateToken",
        t.struct(
            {
                "gcpProjectId": t.string().optional(),
                "code": t.string().optional(),
                "redirectUri": t.string().optional(),
                "state": t.string().optional(),
                "product": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaGenerateTokenResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="integrations",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
