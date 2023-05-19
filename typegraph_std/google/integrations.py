from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_integrations() -> Import:
    integrations = HTTPRuntime("https://integrations.googleapis.com/")

    renames = {
        "ErrorResponse": "_integrations_1_ErrorResponse",
        "GoogleCloudIntegrationsV1alphaValueTypeIn": "_integrations_2_GoogleCloudIntegrationsV1alphaValueTypeIn",
        "GoogleCloudIntegrationsV1alphaValueTypeOut": "_integrations_3_GoogleCloudIntegrationsV1alphaValueTypeOut",
        "GoogleCloudIntegrationsV1alphaSfdcInstanceIn": "_integrations_4_GoogleCloudIntegrationsV1alphaSfdcInstanceIn",
        "GoogleCloudIntegrationsV1alphaSfdcInstanceOut": "_integrations_5_GoogleCloudIntegrationsV1alphaSfdcInstanceOut",
        "EnterpriseCrmEventbusProtoValueTypeIn": "_integrations_6_EnterpriseCrmEventbusProtoValueTypeIn",
        "EnterpriseCrmEventbusProtoValueTypeOut": "_integrations_7_EnterpriseCrmEventbusProtoValueTypeOut",
        "EnterpriseCrmEventbusProtoIntArrayIn": "_integrations_8_EnterpriseCrmEventbusProtoIntArrayIn",
        "EnterpriseCrmEventbusProtoIntArrayOut": "_integrations_9_EnterpriseCrmEventbusProtoIntArrayOut",
        "EnterpriseCrmFrontendsEventbusProtoTaskEntityIn": "_integrations_10_EnterpriseCrmFrontendsEventbusProtoTaskEntityIn",
        "EnterpriseCrmFrontendsEventbusProtoTaskEntityOut": "_integrations_11_EnterpriseCrmFrontendsEventbusProtoTaskEntityOut",
        "GoogleCloudConnectorsV1AuthConfigSshPublicKeyIn": "_integrations_12_GoogleCloudConnectorsV1AuthConfigSshPublicKeyIn",
        "GoogleCloudConnectorsV1AuthConfigSshPublicKeyOut": "_integrations_13_GoogleCloudConnectorsV1AuthConfigSshPublicKeyOut",
        "GoogleCloudIntegrationsV1alphaServiceAccountCredentialsIn": "_integrations_14_GoogleCloudIntegrationsV1alphaServiceAccountCredentialsIn",
        "GoogleCloudIntegrationsV1alphaServiceAccountCredentialsOut": "_integrations_15_GoogleCloudIntegrationsV1alphaServiceAccountCredentialsOut",
        "GoogleCloudIntegrationsV1alphaSuspensionIn": "_integrations_16_GoogleCloudIntegrationsV1alphaSuspensionIn",
        "GoogleCloudIntegrationsV1alphaSuspensionOut": "_integrations_17_GoogleCloudIntegrationsV1alphaSuspensionOut",
        "EnterpriseCrmFrontendsEventbusProtoParameterMapIn": "_integrations_18_EnterpriseCrmFrontendsEventbusProtoParameterMapIn",
        "EnterpriseCrmFrontendsEventbusProtoParameterMapOut": "_integrations_19_EnterpriseCrmFrontendsEventbusProtoParameterMapOut",
        "GoogleCloudIntegrationsV1alphaCancelExecutionRequestIn": "_integrations_20_GoogleCloudIntegrationsV1alphaCancelExecutionRequestIn",
        "GoogleCloudIntegrationsV1alphaCancelExecutionRequestOut": "_integrations_21_GoogleCloudIntegrationsV1alphaCancelExecutionRequestOut",
        "EnterpriseCrmEventbusProtoAttributesIn": "_integrations_22_EnterpriseCrmEventbusProtoAttributesIn",
        "EnterpriseCrmEventbusProtoAttributesOut": "_integrations_23_EnterpriseCrmEventbusProtoAttributesOut",
        "EnterpriseCrmEventbusProtoSuspensionConfigIn": "_integrations_24_EnterpriseCrmEventbusProtoSuspensionConfigIn",
        "EnterpriseCrmEventbusProtoSuspensionConfigOut": "_integrations_25_EnterpriseCrmEventbusProtoSuspensionConfigOut",
        "EnterpriseCrmEventbusProtoNextTeardownTaskIn": "_integrations_26_EnterpriseCrmEventbusProtoNextTeardownTaskIn",
        "EnterpriseCrmEventbusProtoNextTeardownTaskOut": "_integrations_27_EnterpriseCrmEventbusProtoNextTeardownTaskOut",
        "GoogleCloudIntegrationsV1alphaListCertificatesResponseIn": "_integrations_28_GoogleCloudIntegrationsV1alphaListCertificatesResponseIn",
        "GoogleCloudIntegrationsV1alphaListCertificatesResponseOut": "_integrations_29_GoogleCloudIntegrationsV1alphaListCertificatesResponseOut",
        "EnterpriseCrmEventbusProtoJsonFunctionIn": "_integrations_30_EnterpriseCrmEventbusProtoJsonFunctionIn",
        "EnterpriseCrmEventbusProtoJsonFunctionOut": "_integrations_31_EnterpriseCrmEventbusProtoJsonFunctionOut",
        "GoogleCloudIntegrationsV1alphaNextTaskIn": "_integrations_32_GoogleCloudIntegrationsV1alphaNextTaskIn",
        "GoogleCloudIntegrationsV1alphaNextTaskOut": "_integrations_33_GoogleCloudIntegrationsV1alphaNextTaskOut",
        "EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageIn": "_integrations_34_EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageIn",
        "EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageOut": "_integrations_35_EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageOut",
        "GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequestIn": "_integrations_36_GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequestIn",
        "GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequestOut": "_integrations_37_GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequestOut",
        "GoogleCloudIntegrationsV1alphaResolveSuspensionRequestIn": "_integrations_38_GoogleCloudIntegrationsV1alphaResolveSuspensionRequestIn",
        "GoogleCloudIntegrationsV1alphaResolveSuspensionRequestOut": "_integrations_39_GoogleCloudIntegrationsV1alphaResolveSuspensionRequestOut",
        "GoogleCloudIntegrationsV1alphaOidcTokenIn": "_integrations_40_GoogleCloudIntegrationsV1alphaOidcTokenIn",
        "GoogleCloudIntegrationsV1alphaOidcTokenOut": "_integrations_41_GoogleCloudIntegrationsV1alphaOidcTokenOut",
        "GoogleCloudIntegrationsV1alphaFailurePolicyIn": "_integrations_42_GoogleCloudIntegrationsV1alphaFailurePolicyIn",
        "GoogleCloudIntegrationsV1alphaFailurePolicyOut": "_integrations_43_GoogleCloudIntegrationsV1alphaFailurePolicyOut",
        "GoogleProtobufEmptyIn": "_integrations_44_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_integrations_45_GoogleProtobufEmptyOut",
        "EnterpriseCrmEventbusProtoWorkflowAlertConfigIn": "_integrations_46_EnterpriseCrmEventbusProtoWorkflowAlertConfigIn",
        "EnterpriseCrmEventbusProtoWorkflowAlertConfigOut": "_integrations_47_EnterpriseCrmEventbusProtoWorkflowAlertConfigOut",
        "EnterpriseCrmEventbusProtoLogSettingsIn": "_integrations_48_EnterpriseCrmEventbusProtoLogSettingsIn",
        "EnterpriseCrmEventbusProtoLogSettingsOut": "_integrations_49_EnterpriseCrmEventbusProtoLogSettingsOut",
        "EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsIn": "_integrations_50_EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsIn",
        "EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsOut": "_integrations_51_EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsOut",
        "EnterpriseCrmEventbusProtoBaseFunctionIn": "_integrations_52_EnterpriseCrmEventbusProtoBaseFunctionIn",
        "EnterpriseCrmEventbusProtoBaseFunctionOut": "_integrations_53_EnterpriseCrmEventbusProtoBaseFunctionOut",
        "EnterpriseCrmFrontendsEventbusProtoParameterEntryIn": "_integrations_54_EnterpriseCrmFrontendsEventbusProtoParameterEntryIn",
        "EnterpriseCrmFrontendsEventbusProtoParameterEntryOut": "_integrations_55_EnterpriseCrmFrontendsEventbusProtoParameterEntryOut",
        "GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeIn": "_integrations_56_GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeIn",
        "GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeOut": "_integrations_57_GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeOut",
        "GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowIn": "_integrations_58_GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowIn",
        "GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowOut": "_integrations_59_GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowOut",
        "EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayIn": "_integrations_60_EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayIn",
        "EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayOut": "_integrations_61_EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayOut",
        "GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn": "_integrations_62_GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn",
        "GoogleCloudIntegrationsV1alphaErrorCatcherConfigOut": "_integrations_63_GoogleCloudIntegrationsV1alphaErrorCatcherConfigOut",
        "EnterpriseCrmEventbusProtoConditionIn": "_integrations_64_EnterpriseCrmEventbusProtoConditionIn",
        "EnterpriseCrmEventbusProtoConditionOut": "_integrations_65_EnterpriseCrmEventbusProtoConditionOut",
        "EnterpriseCrmEventbusProtoTaskExecutionDetailsIn": "_integrations_66_EnterpriseCrmEventbusProtoTaskExecutionDetailsIn",
        "EnterpriseCrmEventbusProtoTaskExecutionDetailsOut": "_integrations_67_EnterpriseCrmEventbusProtoTaskExecutionDetailsOut",
        "GoogleCloudIntegrationsV1alphaCancelExecutionResponseIn": "_integrations_68_GoogleCloudIntegrationsV1alphaCancelExecutionResponseIn",
        "GoogleCloudIntegrationsV1alphaCancelExecutionResponseOut": "_integrations_69_GoogleCloudIntegrationsV1alphaCancelExecutionResponseOut",
        "GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseIn": "_integrations_70_GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseIn",
        "GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseOut": "_integrations_71_GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseOut",
        "EnterpriseCrmEventbusProtoIntParameterArrayIn": "_integrations_72_EnterpriseCrmEventbusProtoIntParameterArrayIn",
        "EnterpriseCrmEventbusProtoIntParameterArrayOut": "_integrations_73_EnterpriseCrmEventbusProtoIntParameterArrayOut",
        "GoogleCloudIntegrationsV1alphaListConnectionsResponseIn": "_integrations_74_GoogleCloudIntegrationsV1alphaListConnectionsResponseIn",
        "GoogleCloudIntegrationsV1alphaListConnectionsResponseOut": "_integrations_75_GoogleCloudIntegrationsV1alphaListConnectionsResponseOut",
        "EnterpriseCrmEventbusStatsIn": "_integrations_76_EnterpriseCrmEventbusStatsIn",
        "EnterpriseCrmEventbusStatsOut": "_integrations_77_EnterpriseCrmEventbusStatsOut",
        "CrmlogErrorCodeIn": "_integrations_78_CrmlogErrorCodeIn",
        "CrmlogErrorCodeOut": "_integrations_79_CrmlogErrorCodeOut",
        "GoogleCloudConnectorsV1SecretIn": "_integrations_80_GoogleCloudConnectorsV1SecretIn",
        "GoogleCloudConnectorsV1SecretOut": "_integrations_81_GoogleCloudConnectorsV1SecretOut",
        "EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsIn": "_integrations_82_EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsIn",
        "EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsOut": "_integrations_83_EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsOut",
        "EnterpriseCrmEventbusProtoBaseValueIn": "_integrations_84_EnterpriseCrmEventbusProtoBaseValueIn",
        "EnterpriseCrmEventbusProtoBaseValueOut": "_integrations_85_EnterpriseCrmEventbusProtoBaseValueOut",
        "GoogleCloudConnectorsV1ConnectionStatusIn": "_integrations_86_GoogleCloudConnectorsV1ConnectionStatusIn",
        "GoogleCloudConnectorsV1ConnectionStatusOut": "_integrations_87_GoogleCloudConnectorsV1ConnectionStatusOut",
        "GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataIn": "_integrations_88_GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataIn",
        "GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataOut": "_integrations_89_GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataOut",
        "EnterpriseCrmFrontendsEventbusProtoEventParametersIn": "_integrations_90_EnterpriseCrmFrontendsEventbusProtoEventParametersIn",
        "EnterpriseCrmFrontendsEventbusProtoEventParametersOut": "_integrations_91_EnterpriseCrmFrontendsEventbusProtoEventParametersOut",
        "EnterpriseCrmEventbusProtoProtoArrayFunctionIn": "_integrations_92_EnterpriseCrmEventbusProtoProtoArrayFunctionIn",
        "EnterpriseCrmEventbusProtoProtoArrayFunctionOut": "_integrations_93_EnterpriseCrmEventbusProtoProtoArrayFunctionOut",
        "GoogleCloudConnectorsV1DestinationIn": "_integrations_94_GoogleCloudConnectorsV1DestinationIn",
        "GoogleCloudConnectorsV1DestinationOut": "_integrations_95_GoogleCloudConnectorsV1DestinationOut",
        "GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerIn": "_integrations_96_GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerIn",
        "GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerOut": "_integrations_97_GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerOut",
        "GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaIn": "_integrations_98_GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaIn",
        "GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaOut": "_integrations_99_GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaOut",
        "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueIn": "_integrations_100_GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueIn",
        "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueOut": "_integrations_101_GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueOut",
        "GoogleCloudConnectorsV1LogConfigIn": "_integrations_102_GoogleCloudConnectorsV1LogConfigIn",
        "GoogleCloudConnectorsV1LogConfigOut": "_integrations_103_GoogleCloudConnectorsV1LogConfigOut",
        "EnterpriseCrmEventbusProtoTaskMetadataAdminIn": "_integrations_104_EnterpriseCrmEventbusProtoTaskMetadataAdminIn",
        "EnterpriseCrmEventbusProtoTaskMetadataAdminOut": "_integrations_105_EnterpriseCrmEventbusProtoTaskMetadataAdminOut",
        "EnterpriseCrmEventbusProtoConditionResultIn": "_integrations_106_EnterpriseCrmEventbusProtoConditionResultIn",
        "EnterpriseCrmEventbusProtoConditionResultOut": "_integrations_107_EnterpriseCrmEventbusProtoConditionResultOut",
        "GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestIn": "_integrations_108_GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestIn",
        "GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestOut": "_integrations_109_GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestOut",
        "EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterIn": "_integrations_110_EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterIn",
        "EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterOut": "_integrations_111_EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterOut",
        "EnterpriseCrmEventbusProtoEventExecutionSnapshotIn": "_integrations_112_EnterpriseCrmEventbusProtoEventExecutionSnapshotIn",
        "EnterpriseCrmEventbusProtoEventExecutionSnapshotOut": "_integrations_113_EnterpriseCrmEventbusProtoEventExecutionSnapshotOut",
        "GoogleCloudIntegrationsV1alphaEnumerateConnectorPlatformRegionsResponseIn": "_integrations_114_GoogleCloudIntegrationsV1alphaEnumerateConnectorPlatformRegionsResponseIn",
        "GoogleCloudIntegrationsV1alphaEnumerateConnectorPlatformRegionsResponseOut": "_integrations_115_GoogleCloudIntegrationsV1alphaEnumerateConnectorPlatformRegionsResponseOut",
        "EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn": "_integrations_116_EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn",
        "EnterpriseCrmFrontendsEventbusProtoTriggerConfigOut": "_integrations_117_EnterpriseCrmFrontendsEventbusProtoTriggerConfigOut",
        "EnterpriseCrmEventbusProtoLoopMetadataIn": "_integrations_118_EnterpriseCrmEventbusProtoLoopMetadataIn",
        "EnterpriseCrmEventbusProtoLoopMetadataOut": "_integrations_119_EnterpriseCrmEventbusProtoLoopMetadataOut",
        "GoogleCloudIntegrationsV1alphaResolveSuspensionResponseIn": "_integrations_120_GoogleCloudIntegrationsV1alphaResolveSuspensionResponseIn",
        "GoogleCloudIntegrationsV1alphaResolveSuspensionResponseOut": "_integrations_121_GoogleCloudIntegrationsV1alphaResolveSuspensionResponseOut",
        "GoogleCloudIntegrationsV1alphaCertificateIn": "_integrations_122_GoogleCloudIntegrationsV1alphaCertificateIn",
        "GoogleCloudIntegrationsV1alphaCertificateOut": "_integrations_123_GoogleCloudIntegrationsV1alphaCertificateOut",
        "EnterpriseCrmEventbusProtoSuccessPolicyIn": "_integrations_124_EnterpriseCrmEventbusProtoSuccessPolicyIn",
        "EnterpriseCrmEventbusProtoSuccessPolicyOut": "_integrations_125_EnterpriseCrmEventbusProtoSuccessPolicyOut",
        "GoogleCloudIntegrationsV1alphaIntParameterArrayIn": "_integrations_126_GoogleCloudIntegrationsV1alphaIntParameterArrayIn",
        "GoogleCloudIntegrationsV1alphaIntParameterArrayOut": "_integrations_127_GoogleCloudIntegrationsV1alphaIntParameterArrayOut",
        "EnterpriseCrmEventbusProtoSuspensionResolutionInfoIn": "_integrations_128_EnterpriseCrmEventbusProtoSuspensionResolutionInfoIn",
        "EnterpriseCrmEventbusProtoSuspensionResolutionInfoOut": "_integrations_129_EnterpriseCrmEventbusProtoSuspensionResolutionInfoOut",
        "GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationIn": "_integrations_130_GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationIn",
        "GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationOut": "_integrations_131_GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationOut",
        "GoogleCloudIntegrationsV1alphaExecutionDetailsIn": "_integrations_132_GoogleCloudIntegrationsV1alphaExecutionDetailsIn",
        "GoogleCloudIntegrationsV1alphaExecutionDetailsOut": "_integrations_133_GoogleCloudIntegrationsV1alphaExecutionDetailsOut",
        "GoogleCloudIntegrationsV1alphaTaskExecutionDetailsIn": "_integrations_134_GoogleCloudIntegrationsV1alphaTaskExecutionDetailsIn",
        "GoogleCloudIntegrationsV1alphaTaskExecutionDetailsOut": "_integrations_135_GoogleCloudIntegrationsV1alphaTaskExecutionDetailsOut",
        "EnterpriseCrmLoggingGwsFieldLimitsIn": "_integrations_136_EnterpriseCrmLoggingGwsFieldLimitsIn",
        "EnterpriseCrmLoggingGwsFieldLimitsOut": "_integrations_137_EnterpriseCrmLoggingGwsFieldLimitsOut",
        "GoogleCloudIntegrationsV1alphaIntegrationParameterIn": "_integrations_138_GoogleCloudIntegrationsV1alphaIntegrationParameterIn",
        "GoogleCloudIntegrationsV1alphaIntegrationParameterOut": "_integrations_139_GoogleCloudIntegrationsV1alphaIntegrationParameterOut",
        "EnterpriseCrmEventbusProtoTaskUiModuleConfigIn": "_integrations_140_EnterpriseCrmEventbusProtoTaskUiModuleConfigIn",
        "EnterpriseCrmEventbusProtoTaskUiModuleConfigOut": "_integrations_141_EnterpriseCrmEventbusProtoTaskUiModuleConfigOut",
        "EnterpriseCrmEventbusProtoStringArrayIn": "_integrations_142_EnterpriseCrmEventbusProtoStringArrayIn",
        "EnterpriseCrmEventbusProtoStringArrayOut": "_integrations_143_EnterpriseCrmEventbusProtoStringArrayOut",
        "EnterpriseCrmEventbusProtoTaskUiConfigIn": "_integrations_144_EnterpriseCrmEventbusProtoTaskUiConfigIn",
        "EnterpriseCrmEventbusProtoTaskUiConfigOut": "_integrations_145_EnterpriseCrmEventbusProtoTaskUiConfigOut",
        "EnterpriseCrmEventbusProtoDoubleArrayIn": "_integrations_146_EnterpriseCrmEventbusProtoDoubleArrayIn",
        "EnterpriseCrmEventbusProtoDoubleArrayOut": "_integrations_147_EnterpriseCrmEventbusProtoDoubleArrayOut",
        "EnterpriseCrmEventbusProtoMappedFieldIn": "_integrations_148_EnterpriseCrmEventbusProtoMappedFieldIn",
        "EnterpriseCrmEventbusProtoMappedFieldOut": "_integrations_149_EnterpriseCrmEventbusProtoMappedFieldOut",
        "GoogleCloudIntegrationsV1alphaRuntimeActionSchemaIn": "_integrations_150_GoogleCloudIntegrationsV1alphaRuntimeActionSchemaIn",
        "GoogleCloudIntegrationsV1alphaRuntimeActionSchemaOut": "_integrations_151_GoogleCloudIntegrationsV1alphaRuntimeActionSchemaOut",
        "EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionIn": "_integrations_152_EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionIn",
        "EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionOut": "_integrations_153_EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionOut",
        "EnterpriseCrmEventbusProtoTeardownTaskConfigIn": "_integrations_154_EnterpriseCrmEventbusProtoTeardownTaskConfigIn",
        "EnterpriseCrmEventbusProtoTeardownTaskConfigOut": "_integrations_155_EnterpriseCrmEventbusProtoTeardownTaskConfigOut",
        "EnterpriseCrmEventbusProtoCloudKmsConfigIn": "_integrations_156_EnterpriseCrmEventbusProtoCloudKmsConfigIn",
        "EnterpriseCrmEventbusProtoCloudKmsConfigOut": "_integrations_157_EnterpriseCrmEventbusProtoCloudKmsConfigOut",
        "EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryIn": "_integrations_158_EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryIn",
        "EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryOut": "_integrations_159_EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryOut",
        "EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn": "_integrations_160_EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn",
        "EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut": "_integrations_161_EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut",
        "GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseIn": "_integrations_162_GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseIn",
        "GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseOut": "_integrations_163_GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseOut",
        "EnterpriseCrmEventbusProtoParameterMapIn": "_integrations_164_EnterpriseCrmEventbusProtoParameterMapIn",
        "EnterpriseCrmEventbusProtoParameterMapOut": "_integrations_165_EnterpriseCrmEventbusProtoParameterMapOut",
        "GoogleCloudIntegrationsV1alphaTaskConfigIn": "_integrations_166_GoogleCloudIntegrationsV1alphaTaskConfigIn",
        "GoogleCloudIntegrationsV1alphaTaskConfigOut": "_integrations_167_GoogleCloudIntegrationsV1alphaTaskConfigOut",
        "EnterpriseCrmEventbusProtoAddressIn": "_integrations_168_EnterpriseCrmEventbusProtoAddressIn",
        "EnterpriseCrmEventbusProtoAddressOut": "_integrations_169_EnterpriseCrmEventbusProtoAddressOut",
        "EnterpriseCrmEventbusProtoStringArrayFunctionIn": "_integrations_170_EnterpriseCrmEventbusProtoStringArrayFunctionIn",
        "EnterpriseCrmEventbusProtoStringArrayFunctionOut": "_integrations_171_EnterpriseCrmEventbusProtoStringArrayFunctionOut",
        "EnterpriseCrmEventbusProtoBuganizerNotificationIn": "_integrations_172_EnterpriseCrmEventbusProtoBuganizerNotificationIn",
        "EnterpriseCrmEventbusProtoBuganizerNotificationOut": "_integrations_173_EnterpriseCrmEventbusProtoBuganizerNotificationOut",
        "GoogleCloudIntegrationsV1alphaJwtIn": "_integrations_174_GoogleCloudIntegrationsV1alphaJwtIn",
        "GoogleCloudIntegrationsV1alphaJwtOut": "_integrations_175_GoogleCloudIntegrationsV1alphaJwtOut",
        "GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseIn": "_integrations_176_GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseIn",
        "GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseOut": "_integrations_177_GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseOut",
        "GoogleCloudIntegrationsV1alphaExecutionSnapshotIn": "_integrations_178_GoogleCloudIntegrationsV1alphaExecutionSnapshotIn",
        "GoogleCloudIntegrationsV1alphaExecutionSnapshotOut": "_integrations_179_GoogleCloudIntegrationsV1alphaExecutionSnapshotOut",
        "GoogleCloudIntegrationsV1alphaCredentialIn": "_integrations_180_GoogleCloudIntegrationsV1alphaCredentialIn",
        "GoogleCloudIntegrationsV1alphaCredentialOut": "_integrations_181_GoogleCloudIntegrationsV1alphaCredentialOut",
        "GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataIn": "_integrations_182_GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataIn",
        "GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataOut": "_integrations_183_GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataOut",
        "GoogleCloudIntegrationsV1alphaParameterMapIn": "_integrations_184_GoogleCloudIntegrationsV1alphaParameterMapIn",
        "GoogleCloudIntegrationsV1alphaParameterMapOut": "_integrations_185_GoogleCloudIntegrationsV1alphaParameterMapOut",
        "GoogleCloudIntegrationsV1alphaStringParameterArrayIn": "_integrations_186_GoogleCloudIntegrationsV1alphaStringParameterArrayIn",
        "GoogleCloudIntegrationsV1alphaStringParameterArrayOut": "_integrations_187_GoogleCloudIntegrationsV1alphaStringParameterArrayOut",
        "EnterpriseCrmEventbusProtoPropertyEntryIn": "_integrations_188_EnterpriseCrmEventbusProtoPropertyEntryIn",
        "EnterpriseCrmEventbusProtoPropertyEntryOut": "_integrations_189_EnterpriseCrmEventbusProtoPropertyEntryOut",
        "GoogleCloudConnectorsV1NodeConfigIn": "_integrations_190_GoogleCloudConnectorsV1NodeConfigIn",
        "GoogleCloudConnectorsV1NodeConfigOut": "_integrations_191_GoogleCloudConnectorsV1NodeConfigOut",
        "EnterpriseCrmEventbusProtoTriggerCriteriaIn": "_integrations_192_EnterpriseCrmEventbusProtoTriggerCriteriaIn",
        "EnterpriseCrmEventbusProtoTriggerCriteriaOut": "_integrations_193_EnterpriseCrmEventbusProtoTriggerCriteriaOut",
        "EnterpriseCrmEventbusProtoFunctionTypeIn": "_integrations_194_EnterpriseCrmEventbusProtoFunctionTypeIn",
        "EnterpriseCrmEventbusProtoFunctionTypeOut": "_integrations_195_EnterpriseCrmEventbusProtoFunctionTypeOut",
        "GoogleCloudIntegrationsV1alphaIntegrationIn": "_integrations_196_GoogleCloudIntegrationsV1alphaIntegrationIn",
        "GoogleCloudIntegrationsV1alphaIntegrationOut": "_integrations_197_GoogleCloudIntegrationsV1alphaIntegrationOut",
        "GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsIn": "_integrations_198_GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsIn",
        "GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsOut": "_integrations_199_GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsOut",
        "EnterpriseCrmEventbusProtoTeardownIn": "_integrations_200_EnterpriseCrmEventbusProtoTeardownIn",
        "EnterpriseCrmEventbusProtoTeardownOut": "_integrations_201_EnterpriseCrmEventbusProtoTeardownOut",
        "EnterpriseCrmEventbusProtoExecutionTraceInfoIn": "_integrations_202_EnterpriseCrmEventbusProtoExecutionTraceInfoIn",
        "EnterpriseCrmEventbusProtoExecutionTraceInfoOut": "_integrations_203_EnterpriseCrmEventbusProtoExecutionTraceInfoOut",
        "GoogleCloudIntegrationsV1alphaAccessTokenIn": "_integrations_204_GoogleCloudIntegrationsV1alphaAccessTokenIn",
        "GoogleCloudIntegrationsV1alphaAccessTokenOut": "_integrations_205_GoogleCloudIntegrationsV1alphaAccessTokenOut",
        "EnterpriseCrmEventbusProtoNextTaskIn": "_integrations_206_EnterpriseCrmEventbusProtoNextTaskIn",
        "EnterpriseCrmEventbusProtoNextTaskOut": "_integrations_207_EnterpriseCrmEventbusProtoNextTaskOut",
        "EnterpriseCrmEventbusStatsDimensionsIn": "_integrations_208_EnterpriseCrmEventbusStatsDimensionsIn",
        "EnterpriseCrmEventbusStatsDimensionsOut": "_integrations_209_EnterpriseCrmEventbusStatsDimensionsOut",
        "EnterpriseCrmEventbusProtoParameterEntryIn": "_integrations_210_EnterpriseCrmEventbusProtoParameterEntryIn",
        "EnterpriseCrmEventbusProtoParameterEntryOut": "_integrations_211_EnterpriseCrmEventbusProtoParameterEntryOut",
        "EnterpriseCrmEventbusProtoIntFunctionIn": "_integrations_212_EnterpriseCrmEventbusProtoIntFunctionIn",
        "EnterpriseCrmEventbusProtoIntFunctionOut": "_integrations_213_EnterpriseCrmEventbusProtoIntFunctionOut",
        "GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseIn": "_integrations_214_GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseIn",
        "GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseOut": "_integrations_215_GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseOut",
        "EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamIn": "_integrations_216_EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamIn",
        "EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamOut": "_integrations_217_EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamOut",
        "EnterpriseCrmEventbusProtoTransformExpressionIn": "_integrations_218_EnterpriseCrmEventbusProtoTransformExpressionIn",
        "EnterpriseCrmEventbusProtoTransformExpressionOut": "_integrations_219_EnterpriseCrmEventbusProtoTransformExpressionOut",
        "GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestIn": "_integrations_220_GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestIn",
        "GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestOut": "_integrations_221_GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestOut",
        "GoogleCloudIntegrationsV1alphaListSuspensionsResponseIn": "_integrations_222_GoogleCloudIntegrationsV1alphaListSuspensionsResponseIn",
        "GoogleCloudIntegrationsV1alphaListSuspensionsResponseOut": "_integrations_223_GoogleCloudIntegrationsV1alphaListSuspensionsResponseOut",
        "EnterpriseCrmEventbusProtoBooleanFunctionIn": "_integrations_224_EnterpriseCrmEventbusProtoBooleanFunctionIn",
        "EnterpriseCrmEventbusProtoBooleanFunctionOut": "_integrations_225_EnterpriseCrmEventbusProtoBooleanFunctionOut",
        "GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigIn": "_integrations_226_GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigIn",
        "GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigOut": "_integrations_227_GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigOut",
        "EnterpriseCrmEventbusProtoCoordinateIn": "_integrations_228_EnterpriseCrmEventbusProtoCoordinateIn",
        "EnterpriseCrmEventbusProtoCoordinateOut": "_integrations_229_EnterpriseCrmEventbusProtoCoordinateOut",
        "GoogleCloudIntegrationsV1alphaCoordinateIn": "_integrations_230_GoogleCloudIntegrationsV1alphaCoordinateIn",
        "GoogleCloudIntegrationsV1alphaCoordinateOut": "_integrations_231_GoogleCloudIntegrationsV1alphaCoordinateOut",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeIn": "_integrations_232_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeIn",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeOut": "_integrations_233_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeOut",
        "GoogleCloudIntegrationsV1alphaLiftSuspensionResponseIn": "_integrations_234_GoogleCloudIntegrationsV1alphaLiftSuspensionResponseIn",
        "GoogleCloudIntegrationsV1alphaLiftSuspensionResponseOut": "_integrations_235_GoogleCloudIntegrationsV1alphaLiftSuspensionResponseOut",
        "GoogleCloudIntegrationsV1alphaUsernameAndPasswordIn": "_integrations_236_GoogleCloudIntegrationsV1alphaUsernameAndPasswordIn",
        "GoogleCloudIntegrationsV1alphaUsernameAndPasswordOut": "_integrations_237_GoogleCloudIntegrationsV1alphaUsernameAndPasswordOut",
        "GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseIn": "_integrations_238_GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseIn",
        "GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseOut": "_integrations_239_GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseOut",
        "GoogleCloudIntegrationsV1alphaEventParameterIn": "_integrations_240_GoogleCloudIntegrationsV1alphaEventParameterIn",
        "GoogleCloudIntegrationsV1alphaEventParameterOut": "_integrations_241_GoogleCloudIntegrationsV1alphaEventParameterOut",
        "EnterpriseCrmEventbusProtoDoubleArrayFunctionIn": "_integrations_242_EnterpriseCrmEventbusProtoDoubleArrayFunctionIn",
        "EnterpriseCrmEventbusProtoDoubleArrayFunctionOut": "_integrations_243_EnterpriseCrmEventbusProtoDoubleArrayFunctionOut",
        "EnterpriseCrmEventbusProtoTaskMetadataIn": "_integrations_244_EnterpriseCrmEventbusProtoTaskMetadataIn",
        "EnterpriseCrmEventbusProtoTaskMetadataOut": "_integrations_245_EnterpriseCrmEventbusProtoTaskMetadataOut",
        "EnterpriseCrmEventbusProtoParameterValueTypeIn": "_integrations_246_EnterpriseCrmEventbusProtoParameterValueTypeIn",
        "EnterpriseCrmEventbusProtoParameterValueTypeOut": "_integrations_247_EnterpriseCrmEventbusProtoParameterValueTypeOut",
        "EnterpriseCrmFrontendsEventbusProtoParamSpecEntryIn": "_integrations_248_EnterpriseCrmFrontendsEventbusProtoParamSpecEntryIn",
        "EnterpriseCrmFrontendsEventbusProtoParamSpecEntryOut": "_integrations_249_EnterpriseCrmFrontendsEventbusProtoParamSpecEntryOut",
        "EnterpriseCrmEventbusProtoDoubleFunctionIn": "_integrations_250_EnterpriseCrmEventbusProtoDoubleFunctionIn",
        "EnterpriseCrmEventbusProtoDoubleFunctionOut": "_integrations_251_EnterpriseCrmEventbusProtoDoubleFunctionOut",
        "GoogleCloudConnectorsV1AuthConfigUserPasswordIn": "_integrations_252_GoogleCloudConnectorsV1AuthConfigUserPasswordIn",
        "GoogleCloudConnectorsV1AuthConfigUserPasswordOut": "_integrations_253_GoogleCloudConnectorsV1AuthConfigUserPasswordOut",
        "GoogleCloudIntegrationsV1alphaLiftSuspensionRequestIn": "_integrations_254_GoogleCloudIntegrationsV1alphaLiftSuspensionRequestIn",
        "GoogleCloudIntegrationsV1alphaLiftSuspensionRequestOut": "_integrations_255_GoogleCloudIntegrationsV1alphaLiftSuspensionRequestOut",
        "EnterpriseCrmEventbusProtoParameterMapFieldIn": "_integrations_256_EnterpriseCrmEventbusProtoParameterMapFieldIn",
        "EnterpriseCrmEventbusProtoParameterMapFieldOut": "_integrations_257_EnterpriseCrmEventbusProtoParameterMapFieldOut",
        "EnterpriseCrmFrontendsEventbusProtoStringParameterArrayIn": "_integrations_258_EnterpriseCrmFrontendsEventbusProtoStringParameterArrayIn",
        "EnterpriseCrmFrontendsEventbusProtoStringParameterArrayOut": "_integrations_259_EnterpriseCrmFrontendsEventbusProtoStringParameterArrayOut",
        "GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestIn": "_integrations_260_GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestIn",
        "GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestOut": "_integrations_261_GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestOut",
        "EnterpriseCrmEventbusProtoTaskAlertConfigIn": "_integrations_262_EnterpriseCrmEventbusProtoTaskAlertConfigIn",
        "EnterpriseCrmEventbusProtoTaskAlertConfigOut": "_integrations_263_EnterpriseCrmEventbusProtoTaskAlertConfigOut",
        "EnterpriseCrmEventbusProtoSerializedObjectParameterIn": "_integrations_264_EnterpriseCrmEventbusProtoSerializedObjectParameterIn",
        "EnterpriseCrmEventbusProtoSerializedObjectParameterOut": "_integrations_265_EnterpriseCrmEventbusProtoSerializedObjectParameterOut",
        "GoogleCloudIntegrationsV1alphaTriggerConfigIn": "_integrations_266_GoogleCloudIntegrationsV1alphaTriggerConfigIn",
        "GoogleCloudIntegrationsV1alphaTriggerConfigOut": "_integrations_267_GoogleCloudIntegrationsV1alphaTriggerConfigOut",
        "GoogleCloudIntegrationsV1alphaListExecutionsResponseIn": "_integrations_268_GoogleCloudIntegrationsV1alphaListExecutionsResponseIn",
        "GoogleCloudIntegrationsV1alphaListExecutionsResponseOut": "_integrations_269_GoogleCloudIntegrationsV1alphaListExecutionsResponseOut",
        "EnterpriseCrmEventbusProtoSuspensionExpirationIn": "_integrations_270_EnterpriseCrmEventbusProtoSuspensionExpirationIn",
        "EnterpriseCrmEventbusProtoSuspensionExpirationOut": "_integrations_271_EnterpriseCrmEventbusProtoSuspensionExpirationOut",
        "EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn": "_integrations_272_EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn",
        "EnterpriseCrmFrontendsEventbusProtoWorkflowParametersOut": "_integrations_273_EnterpriseCrmFrontendsEventbusProtoWorkflowParametersOut",
        "GoogleCloudIntegrationsV1alphaParameterMapFieldIn": "_integrations_274_GoogleCloudIntegrationsV1alphaParameterMapFieldIn",
        "GoogleCloudIntegrationsV1alphaParameterMapFieldOut": "_integrations_275_GoogleCloudIntegrationsV1alphaParameterMapFieldOut",
        "EnterpriseCrmEventbusProtoEventBusPropertiesIn": "_integrations_276_EnterpriseCrmEventbusProtoEventBusPropertiesIn",
        "EnterpriseCrmEventbusProtoEventBusPropertiesOut": "_integrations_277_EnterpriseCrmEventbusProtoEventBusPropertiesOut",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeIn": "_integrations_278_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeIn",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeOut": "_integrations_279_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeOut",
        "GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseIn": "_integrations_280_GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseIn",
        "GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseOut": "_integrations_281_GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseOut",
        "GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestIn": "_integrations_282_GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestIn",
        "GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestOut": "_integrations_283_GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestOut",
        "EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotIn": "_integrations_284_EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotIn",
        "EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotOut": "_integrations_285_EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotOut",
        "EnterpriseCrmEventbusProtoDoubleParameterArrayIn": "_integrations_286_EnterpriseCrmEventbusProtoDoubleParameterArrayIn",
        "EnterpriseCrmEventbusProtoDoubleParameterArrayOut": "_integrations_287_EnterpriseCrmEventbusProtoDoubleParameterArrayOut",
        "GoogleCloudConnectorsV1ConfigVariableIn": "_integrations_288_GoogleCloudConnectorsV1ConfigVariableIn",
        "GoogleCloudConnectorsV1ConfigVariableOut": "_integrations_289_GoogleCloudConnectorsV1ConfigVariableOut",
        "EnterpriseCrmEventbusProtoConnectorsConnectionIn": "_integrations_290_EnterpriseCrmEventbusProtoConnectorsConnectionIn",
        "EnterpriseCrmEventbusProtoConnectorsConnectionOut": "_integrations_291_EnterpriseCrmEventbusProtoConnectorsConnectionOut",
        "EnterpriseCrmEventbusProtoEventExecutionDetailsIn": "_integrations_292_EnterpriseCrmEventbusProtoEventExecutionDetailsIn",
        "EnterpriseCrmEventbusProtoEventExecutionDetailsOut": "_integrations_293_EnterpriseCrmEventbusProtoEventExecutionDetailsOut",
        "GoogleCloudIntegrationsV1alphaPublishIntegrationVersionRequestIn": "_integrations_294_GoogleCloudIntegrationsV1alphaPublishIntegrationVersionRequestIn",
        "GoogleCloudIntegrationsV1alphaPublishIntegrationVersionRequestOut": "_integrations_295_GoogleCloudIntegrationsV1alphaPublishIntegrationVersionRequestOut",
        "GoogleCloudConnectorsV1AuthConfigIn": "_integrations_296_GoogleCloudConnectorsV1AuthConfigIn",
        "GoogleCloudConnectorsV1AuthConfigOut": "_integrations_297_GoogleCloudConnectorsV1AuthConfigOut",
        "GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsIn": "_integrations_298_GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsIn",
        "GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsOut": "_integrations_299_GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsOut",
        "EnterpriseCrmEventbusProtoTokenIn": "_integrations_300_EnterpriseCrmEventbusProtoTokenIn",
        "EnterpriseCrmEventbusProtoTokenOut": "_integrations_301_EnterpriseCrmEventbusProtoTokenOut",
        "GoogleCloudIntegrationsV1alphaBooleanParameterArrayIn": "_integrations_302_GoogleCloudIntegrationsV1alphaBooleanParameterArrayIn",
        "GoogleCloudIntegrationsV1alphaBooleanParameterArrayOut": "_integrations_303_GoogleCloudIntegrationsV1alphaBooleanParameterArrayOut",
        "GoogleCloudIntegrationsV1alphaAuthConfigIn": "_integrations_304_GoogleCloudIntegrationsV1alphaAuthConfigIn",
        "GoogleCloudIntegrationsV1alphaAuthConfigOut": "_integrations_305_GoogleCloudIntegrationsV1alphaAuthConfigOut",
        "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataIn": "_integrations_306_EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataIn",
        "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataOut": "_integrations_307_EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataOut",
        "GoogleCloudConnectorsV1DestinationConfigIn": "_integrations_308_GoogleCloudConnectorsV1DestinationConfigIn",
        "GoogleCloudConnectorsV1DestinationConfigOut": "_integrations_309_GoogleCloudConnectorsV1DestinationConfigOut",
        "EnterpriseCrmEventbusProtoStringParameterArrayIn": "_integrations_310_EnterpriseCrmEventbusProtoStringParameterArrayIn",
        "EnterpriseCrmEventbusProtoStringParameterArrayOut": "_integrations_311_EnterpriseCrmEventbusProtoStringParameterArrayOut",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIn": "_integrations_312_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIn",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleOut": "_integrations_313_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleOut",
        "EnterpriseCrmEventbusProtoErrorDetailIn": "_integrations_314_EnterpriseCrmEventbusProtoErrorDetailIn",
        "EnterpriseCrmEventbusProtoErrorDetailOut": "_integrations_315_EnterpriseCrmEventbusProtoErrorDetailOut",
        "EnterpriseCrmEventbusProtoCloudSchedulerConfigIn": "_integrations_316_EnterpriseCrmEventbusProtoCloudSchedulerConfigIn",
        "EnterpriseCrmEventbusProtoCloudSchedulerConfigOut": "_integrations_317_EnterpriseCrmEventbusProtoCloudSchedulerConfigOut",
        "GoogleCloudIntegrationsV1alphaDoubleParameterArrayIn": "_integrations_318_GoogleCloudIntegrationsV1alphaDoubleParameterArrayIn",
        "GoogleCloudIntegrationsV1alphaDoubleParameterArrayOut": "_integrations_319_GoogleCloudIntegrationsV1alphaDoubleParameterArrayOut",
        "GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestIn": "_integrations_320_GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestIn",
        "GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestOut": "_integrations_321_GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestOut",
        "EnterpriseCrmEventbusProtoBooleanParameterArrayIn": "_integrations_322_EnterpriseCrmEventbusProtoBooleanParameterArrayIn",
        "EnterpriseCrmEventbusProtoBooleanParameterArrayOut": "_integrations_323_EnterpriseCrmEventbusProtoBooleanParameterArrayOut",
        "GoogleCloudIntegrationsV1alphaSuccessPolicyIn": "_integrations_324_GoogleCloudIntegrationsV1alphaSuccessPolicyIn",
        "GoogleCloudIntegrationsV1alphaSuccessPolicyOut": "_integrations_325_GoogleCloudIntegrationsV1alphaSuccessPolicyOut",
        "GoogleCloudIntegrationsV1alphaCloudSchedulerConfigIn": "_integrations_326_GoogleCloudIntegrationsV1alphaCloudSchedulerConfigIn",
        "GoogleCloudIntegrationsV1alphaCloudSchedulerConfigOut": "_integrations_327_GoogleCloudIntegrationsV1alphaCloudSchedulerConfigOut",
        "EnterpriseCrmEventbusProtoCombinedConditionIn": "_integrations_328_EnterpriseCrmEventbusProtoCombinedConditionIn",
        "EnterpriseCrmEventbusProtoCombinedConditionOut": "_integrations_329_EnterpriseCrmEventbusProtoCombinedConditionOut",
        "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityIn": "_integrations_330_EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityIn",
        "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityOut": "_integrations_331_EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityOut",
        "GoogleCloudConnectorsV1LockConfigIn": "_integrations_332_GoogleCloudConnectorsV1LockConfigIn",
        "GoogleCloudConnectorsV1LockConfigOut": "_integrations_333_GoogleCloudConnectorsV1LockConfigOut",
        "EnterpriseCrmFrontendsEventbusProtoParameterMapEntryIn": "_integrations_334_EnterpriseCrmFrontendsEventbusProtoParameterMapEntryIn",
        "EnterpriseCrmFrontendsEventbusProtoParameterMapEntryOut": "_integrations_335_EnterpriseCrmFrontendsEventbusProtoParameterMapEntryOut",
        "EnterpriseCrmLoggingGwsSanitizeOptionsIn": "_integrations_336_EnterpriseCrmLoggingGwsSanitizeOptionsIn",
        "EnterpriseCrmLoggingGwsSanitizeOptionsOut": "_integrations_337_EnterpriseCrmLoggingGwsSanitizeOptionsOut",
        "GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponseIn": "_integrations_338_GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponseIn",
        "GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponseOut": "_integrations_339_GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponseOut",
        "EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueIn": "_integrations_340_EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueIn",
        "EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueOut": "_integrations_341_EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueOut",
        "GoogleCloudIntegrationsV1alphaSuspensionAuditIn": "_integrations_342_GoogleCloudIntegrationsV1alphaSuspensionAuditIn",
        "GoogleCloudIntegrationsV1alphaSuspensionAuditOut": "_integrations_343_GoogleCloudIntegrationsV1alphaSuspensionAuditOut",
        "EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayIn": "_integrations_344_EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayIn",
        "EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayOut": "_integrations_345_EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayOut",
        "GoogleCloudConnectorsV1ConnectionIn": "_integrations_346_GoogleCloudConnectorsV1ConnectionIn",
        "GoogleCloudConnectorsV1ConnectionOut": "_integrations_347_GoogleCloudConnectorsV1ConnectionOut",
        "EnterpriseCrmEventbusProtoNodeIdentifierIn": "_integrations_348_EnterpriseCrmEventbusProtoNodeIdentifierIn",
        "EnterpriseCrmEventbusProtoNodeIdentifierOut": "_integrations_349_EnterpriseCrmEventbusProtoNodeIdentifierOut",
        "GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsIn": "_integrations_350_GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsIn",
        "GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsOut": "_integrations_351_GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsOut",
        "EnterpriseCrmEventbusProtoEventParametersIn": "_integrations_352_EnterpriseCrmEventbusProtoEventParametersIn",
        "EnterpriseCrmEventbusProtoEventParametersOut": "_integrations_353_EnterpriseCrmEventbusProtoEventParametersOut",
        "GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseIn": "_integrations_354_GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseIn",
        "GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseOut": "_integrations_355_GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseOut",
        "GoogleCloudIntegrationsV1alphaGenerateTokenResponseIn": "_integrations_356_GoogleCloudIntegrationsV1alphaGenerateTokenResponseIn",
        "GoogleCloudIntegrationsV1alphaGenerateTokenResponseOut": "_integrations_357_GoogleCloudIntegrationsV1alphaGenerateTokenResponseOut",
        "EnterpriseCrmEventbusProtoProtoParameterArrayIn": "_integrations_358_EnterpriseCrmEventbusProtoProtoParameterArrayIn",
        "EnterpriseCrmEventbusProtoProtoParameterArrayOut": "_integrations_359_EnterpriseCrmEventbusProtoProtoParameterArrayOut",
        "GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionIn": "_integrations_360_GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionIn",
        "GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionOut": "_integrations_361_GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionOut",
        "GoogleCloudIntegrationsV1alphaExecutionIn": "_integrations_362_GoogleCloudIntegrationsV1alphaExecutionIn",
        "GoogleCloudIntegrationsV1alphaExecutionOut": "_integrations_363_GoogleCloudIntegrationsV1alphaExecutionOut",
        "GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequestIn": "_integrations_364_GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequestIn",
        "GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequestOut": "_integrations_365_GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequestOut",
        "EnterpriseCrmFrontendsEventbusProtoTaskConfigIn": "_integrations_366_EnterpriseCrmFrontendsEventbusProtoTaskConfigIn",
        "EnterpriseCrmFrontendsEventbusProtoTaskConfigOut": "_integrations_367_EnterpriseCrmFrontendsEventbusProtoTaskConfigOut",
        "GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseIn": "_integrations_368_GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseIn",
        "GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseOut": "_integrations_369_GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseOut",
        "GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequestIn": "_integrations_370_GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequestIn",
        "GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequestOut": "_integrations_371_GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequestOut",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexIn": "_integrations_372_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexIn",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexOut": "_integrations_373_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexOut",
        "EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayIn": "_integrations_374_EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayIn",
        "EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayOut": "_integrations_375_EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayOut",
        "EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn": "_integrations_376_EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn",
        "EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut": "_integrations_377_EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut",
        "EnterpriseCrmEventbusProtoFieldMappingConfigIn": "_integrations_378_EnterpriseCrmEventbusProtoFieldMappingConfigIn",
        "EnterpriseCrmEventbusProtoFieldMappingConfigOut": "_integrations_379_EnterpriseCrmEventbusProtoFieldMappingConfigOut",
        "GoogleCloudConnectorsV1SslConfigIn": "_integrations_380_GoogleCloudConnectorsV1SslConfigIn",
        "GoogleCloudConnectorsV1SslConfigOut": "_integrations_381_GoogleCloudConnectorsV1SslConfigOut",
        "EnterpriseCrmFrontendsEventbusProtoIntParameterArrayIn": "_integrations_382_EnterpriseCrmFrontendsEventbusProtoIntParameterArrayIn",
        "EnterpriseCrmFrontendsEventbusProtoIntParameterArrayOut": "_integrations_383_EnterpriseCrmFrontendsEventbusProtoIntParameterArrayOut",
        "EnterpriseCrmEventbusProtoExternalTrafficIn": "_integrations_384_EnterpriseCrmEventbusProtoExternalTrafficIn",
        "EnterpriseCrmEventbusProtoExternalTrafficOut": "_integrations_385_EnterpriseCrmEventbusProtoExternalTrafficOut",
        "GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsIn": "_integrations_386_GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsIn",
        "GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsOut": "_integrations_387_GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsOut",
        "GoogleCloudIntegrationsV1alphaListAuthConfigsResponseIn": "_integrations_388_GoogleCloudIntegrationsV1alphaListAuthConfigsResponseIn",
        "GoogleCloudIntegrationsV1alphaListAuthConfigsResponseOut": "_integrations_389_GoogleCloudIntegrationsV1alphaListAuthConfigsResponseOut",
        "GoogleCloudIntegrationsV1alphaSfdcChannelIn": "_integrations_390_GoogleCloudIntegrationsV1alphaSfdcChannelIn",
        "GoogleCloudIntegrationsV1alphaSfdcChannelOut": "_integrations_391_GoogleCloudIntegrationsV1alphaSfdcChannelOut",
        "EnterpriseCrmEventbusProtoConnectorsGenericConnectorTaskConfigIn": "_integrations_392_EnterpriseCrmEventbusProtoConnectorsGenericConnectorTaskConfigIn",
        "EnterpriseCrmEventbusProtoConnectorsGenericConnectorTaskConfigOut": "_integrations_393_EnterpriseCrmEventbusProtoConnectorsGenericConnectorTaskConfigOut",
        "GoogleCloudIntegrationsV1alphaAttemptStatsIn": "_integrations_394_GoogleCloudIntegrationsV1alphaAttemptStatsIn",
        "GoogleCloudIntegrationsV1alphaAttemptStatsOut": "_integrations_395_GoogleCloudIntegrationsV1alphaAttemptStatsOut",
        "GoogleCloudIntegrationsV1alphaClientCertificateIn": "_integrations_396_GoogleCloudIntegrationsV1alphaClientCertificateIn",
        "GoogleCloudIntegrationsV1alphaClientCertificateOut": "_integrations_397_GoogleCloudIntegrationsV1alphaClientCertificateOut",
        "EnterpriseCrmEventbusProtoParamSpecEntryConfigIn": "_integrations_398_EnterpriseCrmEventbusProtoParamSpecEntryConfigIn",
        "EnterpriseCrmEventbusProtoParamSpecEntryConfigOut": "_integrations_399_EnterpriseCrmEventbusProtoParamSpecEntryConfigOut",
        "EnterpriseCrmEventbusProtoScatterResponseIn": "_integrations_400_EnterpriseCrmEventbusProtoScatterResponseIn",
        "EnterpriseCrmEventbusProtoScatterResponseOut": "_integrations_401_EnterpriseCrmEventbusProtoScatterResponseOut",
        "GoogleCloudIntegrationsV1alphaParameterMapEntryIn": "_integrations_402_GoogleCloudIntegrationsV1alphaParameterMapEntryIn",
        "GoogleCloudIntegrationsV1alphaParameterMapEntryOut": "_integrations_403_GoogleCloudIntegrationsV1alphaParameterMapEntryOut",
        "GoogleCloudIntegrationsV1alphaIntegrationVersionIn": "_integrations_404_GoogleCloudIntegrationsV1alphaIntegrationVersionIn",
        "GoogleCloudIntegrationsV1alphaIntegrationVersionOut": "_integrations_405_GoogleCloudIntegrationsV1alphaIntegrationVersionOut",
        "EnterpriseCrmFrontendsEventbusProtoParameterMapFieldIn": "_integrations_406_EnterpriseCrmFrontendsEventbusProtoParameterMapFieldIn",
        "EnterpriseCrmFrontendsEventbusProtoParameterMapFieldOut": "_integrations_407_EnterpriseCrmFrontendsEventbusProtoParameterMapFieldOut",
        "EnterpriseCrmEventbusProtoNotificationIn": "_integrations_408_EnterpriseCrmEventbusProtoNotificationIn",
        "EnterpriseCrmEventbusProtoNotificationOut": "_integrations_409_EnterpriseCrmEventbusProtoNotificationOut",
        "EnterpriseCrmEventbusProtoParameterMapEntryIn": "_integrations_410_EnterpriseCrmEventbusProtoParameterMapEntryIn",
        "EnterpriseCrmEventbusProtoParameterMapEntryOut": "_integrations_411_EnterpriseCrmEventbusProtoParameterMapEntryOut",
        "GoogleCloudIntegrationsV1alphaPublishIntegrationVersionResponseIn": "_integrations_412_GoogleCloudIntegrationsV1alphaPublishIntegrationVersionResponseIn",
        "GoogleCloudIntegrationsV1alphaPublishIntegrationVersionResponseOut": "_integrations_413_GoogleCloudIntegrationsV1alphaPublishIntegrationVersionResponseOut",
        "GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseIn": "_integrations_414_GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseIn",
        "GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseOut": "_integrations_415_GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseOut",
        "GoogleCloudIntegrationsV1alphaListIntegrationsResponseIn": "_integrations_416_GoogleCloudIntegrationsV1alphaListIntegrationsResponseIn",
        "GoogleCloudIntegrationsV1alphaListIntegrationsResponseOut": "_integrations_417_GoogleCloudIntegrationsV1alphaListIntegrationsResponseOut",
        "EnterpriseCrmEventbusProtoFieldIn": "_integrations_418_EnterpriseCrmEventbusProtoFieldIn",
        "EnterpriseCrmEventbusProtoFieldOut": "_integrations_419_EnterpriseCrmEventbusProtoFieldOut",
        "EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsIn": "_integrations_420_EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsIn",
        "EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsOut": "_integrations_421_EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsOut",
        "GoogleCloudIntegrationsV1alphaAuthTokenIn": "_integrations_422_GoogleCloudIntegrationsV1alphaAuthTokenIn",
        "GoogleCloudIntegrationsV1alphaAuthTokenOut": "_integrations_423_GoogleCloudIntegrationsV1alphaAuthTokenOut",
        "EnterpriseCrmEventbusProtoCustomSuspensionRequestIn": "_integrations_424_EnterpriseCrmEventbusProtoCustomSuspensionRequestIn",
        "EnterpriseCrmEventbusProtoCustomSuspensionRequestOut": "_integrations_425_EnterpriseCrmEventbusProtoCustomSuspensionRequestOut",
        "EnterpriseCrmEventbusProtoProtoFunctionIn": "_integrations_426_EnterpriseCrmEventbusProtoProtoFunctionIn",
        "EnterpriseCrmEventbusProtoProtoFunctionOut": "_integrations_427_EnterpriseCrmEventbusProtoProtoFunctionOut",
        "EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditIn": "_integrations_428_EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditIn",
        "EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditOut": "_integrations_429_EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditOut",
        "EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoIn": "_integrations_430_EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoIn",
        "EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoOut": "_integrations_431_EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoOut",
        "EnterpriseCrmEventbusProtoBooleanArrayFunctionIn": "_integrations_432_EnterpriseCrmEventbusProtoBooleanArrayFunctionIn",
        "EnterpriseCrmEventbusProtoBooleanArrayFunctionOut": "_integrations_433_EnterpriseCrmEventbusProtoBooleanArrayFunctionOut",
        "EnterpriseCrmEventbusProtoFailurePolicyIn": "_integrations_434_EnterpriseCrmEventbusProtoFailurePolicyIn",
        "EnterpriseCrmEventbusProtoFailurePolicyOut": "_integrations_435_EnterpriseCrmEventbusProtoFailurePolicyOut",
        "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigIn": "_integrations_436_GoogleCloudIntegrationsV1alphaIntegrationAlertConfigIn",
        "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigOut": "_integrations_437_GoogleCloudIntegrationsV1alphaIntegrationAlertConfigOut",
        "GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseIn": "_integrations_438_GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseIn",
        "GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseOut": "_integrations_439_GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseOut",
        "GoogleCloudIntegrationsV1alphaUploadIntegrationVersionResponseIn": "_integrations_440_GoogleCloudIntegrationsV1alphaUploadIntegrationVersionResponseIn",
        "GoogleCloudIntegrationsV1alphaUploadIntegrationVersionResponseOut": "_integrations_441_GoogleCloudIntegrationsV1alphaUploadIntegrationVersionResponseOut",
        "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsIn": "_integrations_442_EnterpriseCrmEventbusProtoSuspensionAuthPermissionsIn",
        "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsOut": "_integrations_443_EnterpriseCrmEventbusProtoSuspensionAuthPermissionsOut",
        "EnterpriseCrmEventbusProtoFunctionIn": "_integrations_444_EnterpriseCrmEventbusProtoFunctionIn",
        "EnterpriseCrmEventbusProtoFunctionOut": "_integrations_445_EnterpriseCrmEventbusProtoFunctionOut",
        "EnterpriseCrmEventbusProtoStringFunctionIn": "_integrations_446_EnterpriseCrmEventbusProtoStringFunctionIn",
        "EnterpriseCrmEventbusProtoStringFunctionOut": "_integrations_447_EnterpriseCrmEventbusProtoStringFunctionOut",
        "GoogleCloudIntegrationsV1alphaTakeoverEditLockResponseIn": "_integrations_448_GoogleCloudIntegrationsV1alphaTakeoverEditLockResponseIn",
        "GoogleCloudIntegrationsV1alphaTakeoverEditLockResponseOut": "_integrations_449_GoogleCloudIntegrationsV1alphaTakeoverEditLockResponseOut",
        "EnterpriseCrmFrontendsEventbusProtoRollbackStrategyIn": "_integrations_450_EnterpriseCrmFrontendsEventbusProtoRollbackStrategyIn",
        "EnterpriseCrmFrontendsEventbusProtoRollbackStrategyOut": "_integrations_451_EnterpriseCrmFrontendsEventbusProtoRollbackStrategyOut",
        "EnterpriseCrmEventbusProtoIntArrayFunctionIn": "_integrations_452_EnterpriseCrmEventbusProtoIntArrayFunctionIn",
        "EnterpriseCrmEventbusProtoIntArrayFunctionOut": "_integrations_453_EnterpriseCrmEventbusProtoIntArrayFunctionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudIntegrationsV1alphaValueTypeIn"] = t.struct(
        {
            "stringValue": t.string().optional(),
            "booleanValue": t.boolean().optional(),
            "doubleValue": t.number().optional(),
            "intArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaIntParameterArrayIn"]
            ).optional(),
            "doubleArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaDoubleParameterArrayIn"]
            ).optional(),
            "booleanArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaBooleanParameterArrayIn"]
            ).optional(),
            "intValue": t.string().optional(),
            "stringArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaStringParameterArrayIn"]
            ).optional(),
            "jsonValue": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaValueTypeIn"])
    types["GoogleCloudIntegrationsV1alphaValueTypeOut"] = t.struct(
        {
            "stringValue": t.string().optional(),
            "booleanValue": t.boolean().optional(),
            "doubleValue": t.number().optional(),
            "intArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaIntParameterArrayOut"]
            ).optional(),
            "doubleArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaDoubleParameterArrayOut"]
            ).optional(),
            "booleanArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaBooleanParameterArrayOut"]
            ).optional(),
            "intValue": t.string().optional(),
            "stringArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaStringParameterArrayOut"]
            ).optional(),
            "jsonValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaValueTypeOut"])
    types["GoogleCloudIntegrationsV1alphaSfdcInstanceIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "sfdcOrgId": t.string().optional(),
            "authConfigId": t.array(t.string()).optional(),
            "serviceAuthority": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceIn"])
    types["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "deleteTime": t.string().optional(),
            "sfdcOrgId": t.string().optional(),
            "authConfigId": t.array(t.string()).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "serviceAuthority": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"])
    types["EnterpriseCrmEventbusProtoValueTypeIn"] = t.struct(
        {
            "protoValue": t.struct({"_": t.string().optional()}),
            "stringValue": t.string(),
            "booleanValue": t.boolean(),
            "intArray": t.proxy(renames["EnterpriseCrmEventbusProtoIntArrayIn"]),
            "doubleValue": t.number(),
            "intValue": t.string(),
            "stringArray": t.proxy(renames["EnterpriseCrmEventbusProtoStringArrayIn"]),
            "doubleArray": t.proxy(renames["EnterpriseCrmEventbusProtoDoubleArrayIn"]),
        }
    ).named(renames["EnterpriseCrmEventbusProtoValueTypeIn"])
    types["EnterpriseCrmEventbusProtoValueTypeOut"] = t.struct(
        {
            "protoValue": t.struct({"_": t.string().optional()}),
            "stringValue": t.string(),
            "booleanValue": t.boolean(),
            "intArray": t.proxy(renames["EnterpriseCrmEventbusProtoIntArrayOut"]),
            "doubleValue": t.number(),
            "intValue": t.string(),
            "stringArray": t.proxy(renames["EnterpriseCrmEventbusProtoStringArrayOut"]),
            "doubleArray": t.proxy(renames["EnterpriseCrmEventbusProtoDoubleArrayOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoValueTypeOut"])
    types["EnterpriseCrmEventbusProtoIntArrayIn"] = t.struct(
        {"values": t.array(t.string())}
    ).named(renames["EnterpriseCrmEventbusProtoIntArrayIn"])
    types["EnterpriseCrmEventbusProtoIntArrayOut"] = t.struct(
        {
            "values": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoIntArrayOut"])
    types["EnterpriseCrmFrontendsEventbusProtoTaskEntityIn"] = t.struct(
        {
            "stats": t.proxy(renames["EnterpriseCrmEventbusStatsIn"]).optional(),
            "uiConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoTaskUiConfigIn"]
            ).optional(),
            "metadata": t.proxy(
                renames["EnterpriseCrmEventbusProtoTaskMetadataIn"]
            ).optional(),
            "paramSpecs": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageIn"]
            ).optional(),
            "disabledForVpcSc": t.boolean().optional(),
            "taskType": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoTaskEntityIn"])
    types["EnterpriseCrmFrontendsEventbusProtoTaskEntityOut"] = t.struct(
        {
            "stats": t.proxy(renames["EnterpriseCrmEventbusStatsOut"]).optional(),
            "uiConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoTaskUiConfigOut"]
            ).optional(),
            "metadata": t.proxy(
                renames["EnterpriseCrmEventbusProtoTaskMetadataOut"]
            ).optional(),
            "paramSpecs": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageOut"]
            ).optional(),
            "disabledForVpcSc": t.boolean().optional(),
            "taskType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoTaskEntityOut"])
    types["GoogleCloudConnectorsV1AuthConfigSshPublicKeyIn"] = t.struct(
        {
            "certType": t.string().optional(),
            "sshClientCertPass": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
            "sshClientCert": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
            "username": t.string().optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigSshPublicKeyIn"])
    types["GoogleCloudConnectorsV1AuthConfigSshPublicKeyOut"] = t.struct(
        {
            "certType": t.string().optional(),
            "sshClientCertPass": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "sshClientCert": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "username": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigSshPublicKeyOut"])
    types["GoogleCloudIntegrationsV1alphaServiceAccountCredentialsIn"] = t.struct(
        {"serviceAccount": t.string().optional(), "scope": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaServiceAccountCredentialsIn"])
    types["GoogleCloudIntegrationsV1alphaServiceAccountCredentialsOut"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "scope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaServiceAccountCredentialsOut"])
    types["GoogleCloudIntegrationsV1alphaSuspensionIn"] = t.struct(
        {
            "eventExecutionInfoId": t.string(),
            "approvalConfig": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigIn"]
            ).optional(),
            "audit": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuspensionAuditIn"]
            ).optional(),
            "taskId": t.string(),
            "name": t.string().optional(),
            "integration": t.string(),
            "state": t.string(),
            "suspensionConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSuspensionIn"])
    types["GoogleCloudIntegrationsV1alphaSuspensionOut"] = t.struct(
        {
            "eventExecutionInfoId": t.string(),
            "approvalConfig": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigOut"]
            ).optional(),
            "audit": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuspensionAuditOut"]
            ).optional(),
            "taskId": t.string(),
            "name": t.string().optional(),
            "integration": t.string(),
            "lastModifyTime": t.string().optional(),
            "state": t.string(),
            "suspensionConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionConfigOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSuspensionOut"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterMapIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoParameterMapEntryIn"]
                )
            ),
            "valueType": t.string(),
            "keyType": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterMapIn"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterMapOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoParameterMapEntryOut"]
                )
            ),
            "valueType": t.string(),
            "keyType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterMapOut"])
    types["GoogleCloudIntegrationsV1alphaCancelExecutionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaCancelExecutionRequestIn"])
    types["GoogleCloudIntegrationsV1alphaCancelExecutionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaCancelExecutionRequestOut"])
    types["EnterpriseCrmEventbusProtoAttributesIn"] = t.struct(
        {
            "taskVisibility": t.array(t.string()).optional(),
            "dataType": t.string().optional(),
            "isRequired": t.boolean(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoValueTypeIn"]
            ).optional(),
            "logSettings": t.proxy(
                renames["EnterpriseCrmEventbusProtoLogSettingsIn"]
            ).optional(),
            "searchable": t.string(),
            "isSearchable": t.boolean().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoAttributesIn"])
    types["EnterpriseCrmEventbusProtoAttributesOut"] = t.struct(
        {
            "taskVisibility": t.array(t.string()).optional(),
            "dataType": t.string().optional(),
            "isRequired": t.boolean(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoValueTypeOut"]
            ).optional(),
            "logSettings": t.proxy(
                renames["EnterpriseCrmEventbusProtoLogSettingsOut"]
            ).optional(),
            "searchable": t.string(),
            "isSearchable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoAttributesOut"])
    types["EnterpriseCrmEventbusProtoSuspensionConfigIn"] = t.struct(
        {
            "whoMayResolve": t.array(
                t.proxy(
                    renames["EnterpriseCrmEventbusProtoSuspensionAuthPermissionsIn"]
                )
            ).optional(),
            "suspensionExpiration": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionExpirationIn"]
            ).optional(),
            "customMessage": t.string().optional(),
            "notifications": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoNotificationIn"])
            ),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionConfigIn"])
    types["EnterpriseCrmEventbusProtoSuspensionConfigOut"] = t.struct(
        {
            "whoMayResolve": t.array(
                t.proxy(
                    renames["EnterpriseCrmEventbusProtoSuspensionAuthPermissionsOut"]
                )
            ).optional(),
            "suspensionExpiration": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionExpirationOut"]
            ).optional(),
            "customMessage": t.string().optional(),
            "notifications": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoNotificationOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionConfigOut"])
    types["EnterpriseCrmEventbusProtoNextTeardownTaskIn"] = t.struct(
        {"name": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoNextTeardownTaskIn"])
    types["EnterpriseCrmEventbusProtoNextTeardownTaskOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EnterpriseCrmEventbusProtoNextTeardownTaskOut"])
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
    types["EnterpriseCrmEventbusProtoJsonFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoJsonFunctionIn"])
    types["EnterpriseCrmEventbusProtoJsonFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoJsonFunctionOut"])
    types["GoogleCloudIntegrationsV1alphaNextTaskIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "condition": t.string().optional(),
            "description": t.string().optional(),
            "taskId": t.string().optional(),
            "taskConfigId": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaNextTaskIn"])
    types["GoogleCloudIntegrationsV1alphaNextTaskOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "condition": t.string().optional(),
            "description": t.string().optional(),
            "taskId": t.string().optional(),
            "taskConfigId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaNextTaskOut"])
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
    types["GoogleCloudIntegrationsV1alphaOidcTokenIn"] = t.struct(
        {
            "tokenExpireTime": t.string().optional(),
            "token": t.string().optional(),
            "audience": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOidcTokenIn"])
    types["GoogleCloudIntegrationsV1alphaOidcTokenOut"] = t.struct(
        {
            "tokenExpireTime": t.string().optional(),
            "token": t.string().optional(),
            "audience": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOidcTokenOut"])
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
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["EnterpriseCrmEventbusProtoWorkflowAlertConfigIn"] = t.struct(
        {
            "clientId": t.string().optional(),
            "thresholdType": t.string().optional(),
            "warningEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn"]
            ),
            "alertName": t.string().optional(),
            "errorEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn"]
            ),
            "numAggregationPeriods": t.integer().optional(),
            "onlyFinalAttempt": t.boolean().optional(),
            "durationThresholdMs": t.string().optional(),
            "thresholdValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueIn"]
            ).optional(),
            "aggregationPeriod": t.string().optional(),
            "alertDisabled": t.boolean().optional(),
            "metricType": t.string(),
            "playbookUrl": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoWorkflowAlertConfigIn"])
    types["EnterpriseCrmEventbusProtoWorkflowAlertConfigOut"] = t.struct(
        {
            "clientId": t.string().optional(),
            "thresholdType": t.string().optional(),
            "warningEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut"]
            ),
            "alertName": t.string().optional(),
            "errorEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut"]
            ),
            "numAggregationPeriods": t.integer().optional(),
            "onlyFinalAttempt": t.boolean().optional(),
            "durationThresholdMs": t.string().optional(),
            "thresholdValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueOut"]
            ).optional(),
            "aggregationPeriod": t.string().optional(),
            "alertDisabled": t.boolean().optional(),
            "metricType": t.string(),
            "playbookUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoWorkflowAlertConfigOut"])
    types["EnterpriseCrmEventbusProtoLogSettingsIn"] = t.struct(
        {
            "sanitizeOptions": t.proxy(
                renames["EnterpriseCrmLoggingGwsSanitizeOptionsIn"]
            ).optional(),
            "seedPeriod": t.string(),
            "logFieldName": t.string().optional(),
            "seedScope": t.string(),
            "shorteningLimits": t.proxy(
                renames["EnterpriseCrmLoggingGwsFieldLimitsIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoLogSettingsIn"])
    types["EnterpriseCrmEventbusProtoLogSettingsOut"] = t.struct(
        {
            "sanitizeOptions": t.proxy(
                renames["EnterpriseCrmLoggingGwsSanitizeOptionsOut"]
            ).optional(),
            "seedPeriod": t.string(),
            "logFieldName": t.string().optional(),
            "seedScope": t.string(),
            "shorteningLimits": t.proxy(
                renames["EnterpriseCrmLoggingGwsFieldLimitsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoLogSettingsOut"])
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
    types["EnterpriseCrmEventbusProtoBaseFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoBaseFunctionIn"])
    types["EnterpriseCrmEventbusProtoBaseFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBaseFunctionOut"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"] = t.struct(
        {
            "dataType": t.string().optional(),
            "value": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn"]
            ).optional(),
            "key": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"] = t.struct(
        {
            "dataType": t.string().optional(),
            "value": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"])
    types["GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeIn"] = t.struct(
        {
            "tokenParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapIn"]
            ).optional(),
            "applyReauthPolicy": t.boolean().optional(),
            "requestType": t.string().optional(),
            "authParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapIn"]
            ).optional(),
            "clientId": t.string().optional(),
            "accessToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAccessTokenIn"]
            ).optional(),
            "authEndpoint": t.string().optional(),
            "clientSecret": t.string().optional(),
            "authCode": t.string().optional(),
            "tokenEndpoint": t.string().optional(),
            "scope": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeIn"])
    types["GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeOut"] = t.struct(
        {
            "tokenParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapOut"]
            ).optional(),
            "applyReauthPolicy": t.boolean().optional(),
            "requestType": t.string().optional(),
            "authParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapOut"]
            ).optional(),
            "clientId": t.string().optional(),
            "accessToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAccessTokenOut"]
            ).optional(),
            "authEndpoint": t.string().optional(),
            "clientSecret": t.string().optional(),
            "authCode": t.string().optional(),
            "tokenEndpoint": t.string().optional(),
            "scope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeOut"])
    types["GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowIn"] = t.struct(
        {
            "pkceVerifier": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "authCode": t.string().optional(),
            "enablePkce": t.boolean().optional(),
            "clientId": t.string().optional(),
            "redirectUri": t.string().optional(),
            "clientSecret": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowIn"])
    types["GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowOut"] = t.struct(
        {
            "pkceVerifier": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "authCode": t.string().optional(),
            "enablePkce": t.boolean().optional(),
            "clientId": t.string().optional(),
            "redirectUri": t.string().optional(),
            "clientSecret": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowOut"])
    types["EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayIn"] = t.struct(
        {"doubleValues": t.array(t.number())}
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayIn"])
    types["EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayOut"] = t.struct(
        {
            "doubleValues": t.array(t.number()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayOut"])
    types["GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn"] = t.struct(
        {
            "errorCatcherNumber": t.string(),
            "description": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCoordinateIn"]
            ).optional(),
            "errorCatcherId": t.string(),
            "startErrorTasks": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaNextTaskIn"])
            ),
            "label": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn"])
    types["GoogleCloudIntegrationsV1alphaErrorCatcherConfigOut"] = t.struct(
        {
            "errorCatcherNumber": t.string(),
            "description": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCoordinateOut"]
            ).optional(),
            "errorCatcherId": t.string(),
            "startErrorTasks": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaNextTaskOut"])
            ),
            "label": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigOut"])
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
    types["GoogleCloudIntegrationsV1alphaCancelExecutionResponseIn"] = t.struct(
        {"isCanceled": t.boolean().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaCancelExecutionResponseIn"])
    types["GoogleCloudIntegrationsV1alphaCancelExecutionResponseOut"] = t.struct(
        {
            "isCanceled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCancelExecutionResponseOut"])
    types["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseIn"] = t.struct(
        {"scriptId": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseIn"])
    types["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseOut"] = t.struct(
        {
            "scriptId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseOut"])
    types["EnterpriseCrmEventbusProtoIntParameterArrayIn"] = t.struct(
        {"intValues": t.array(t.string())}
    ).named(renames["EnterpriseCrmEventbusProtoIntParameterArrayIn"])
    types["EnterpriseCrmEventbusProtoIntParameterArrayOut"] = t.struct(
        {
            "intValues": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoIntParameterArrayOut"])
    types["GoogleCloudIntegrationsV1alphaListConnectionsResponseIn"] = t.struct(
        {
            "connections": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConnectionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListConnectionsResponseIn"])
    types["GoogleCloudIntegrationsV1alphaListConnectionsResponseOut"] = t.struct(
        {
            "connections": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConnectionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListConnectionsResponseOut"])
    types["EnterpriseCrmEventbusStatsIn"] = t.struct(
        {
            "durationInSeconds": t.number().optional(),
            "errorRate": t.number().optional(),
            "dimensions": t.proxy(
                renames["EnterpriseCrmEventbusStatsDimensionsIn"]
            ).optional(),
            "warningRate": t.number().optional(),
            "qps": t.number().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusStatsIn"])
    types["EnterpriseCrmEventbusStatsOut"] = t.struct(
        {
            "durationInSeconds": t.number().optional(),
            "errorRate": t.number().optional(),
            "dimensions": t.proxy(
                renames["EnterpriseCrmEventbusStatsDimensionsOut"]
            ).optional(),
            "warningRate": t.number().optional(),
            "qps": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusStatsOut"])
    types["CrmlogErrorCodeIn"] = t.struct({"commonErrorCode": t.string()}).named(
        renames["CrmlogErrorCodeIn"]
    )
    types["CrmlogErrorCodeOut"] = t.struct(
        {
            "commonErrorCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CrmlogErrorCodeOut"])
    types["GoogleCloudConnectorsV1SecretIn"] = t.struct(
        {"secretVersion": t.string().optional()}
    ).named(renames["GoogleCloudConnectorsV1SecretIn"])
    types["GoogleCloudConnectorsV1SecretOut"] = t.struct(
        {
            "secretVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1SecretOut"])
    types[
        "EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsIn"
    ] = t.struct(
        {"startTime": t.string().optional(), "endTime": t.string().optional()}
    ).named(
        renames["EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsIn"]
    )
    types[
        "EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsOut"
    ] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsOut"]
    )
    types["EnterpriseCrmEventbusProtoBaseValueIn"] = t.struct(
        {
            "referenceValue": t.string().optional(),
            "literalValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeIn"]
            ).optional(),
            "baseFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoFunctionIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBaseValueIn"])
    types["EnterpriseCrmEventbusProtoBaseValueOut"] = t.struct(
        {
            "referenceValue": t.string().optional(),
            "literalValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "baseFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoFunctionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBaseValueOut"])
    types["GoogleCloudConnectorsV1ConnectionStatusIn"] = t.struct(
        {
            "state": t.string().optional(),
            "description": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1ConnectionStatusIn"])
    types["GoogleCloudConnectorsV1ConnectionStatusOut"] = t.struct(
        {
            "state": t.string().optional(),
            "description": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1ConnectionStatusOut"])
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
    types["EnterpriseCrmEventbusProtoProtoArrayFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoProtoArrayFunctionIn"])
    types["EnterpriseCrmEventbusProtoProtoArrayFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoProtoArrayFunctionOut"])
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
    types["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerIn"] = t.struct(
        {
            "clientKey": t.proxy(renames["GoogleCloudConnectorsV1SecretIn"]).optional(),
            "jwtClaims": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerIn"])
    types["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerOut"] = t.struct(
        {
            "clientKey": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "jwtClaims": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerOut"])
    types["GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaIn"] = t.struct(
        {
            "entity": t.string().optional(),
            "fieldSchema": t.string().optional(),
            "arrayFieldSchema": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaIn"])
    types["GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaOut"] = t.struct(
        {
            "entity": t.string().optional(),
            "fieldSchema": t.string().optional(),
            "arrayFieldSchema": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaOut"])
    types[
        "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueIn"
    ] = t.struct(
        {"absolute": t.string().optional(), "percentage": t.integer().optional()}
    ).named(
        renames["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueIn"]
    )
    types[
        "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueOut"
    ] = t.struct(
        {
            "absolute": t.string().optional(),
            "percentage": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueOut"]
    )
    types["GoogleCloudConnectorsV1LogConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["GoogleCloudConnectorsV1LogConfigIn"])
    types["GoogleCloudConnectorsV1LogConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1LogConfigOut"])
    types["EnterpriseCrmEventbusProtoTaskMetadataAdminIn"] = t.struct(
        {"googleGroupEmail": t.string(), "userEmail": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoTaskMetadataAdminIn"])
    types["EnterpriseCrmEventbusProtoTaskMetadataAdminOut"] = t.struct(
        {
            "googleGroupEmail": t.string(),
            "userEmail": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskMetadataAdminOut"])
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
    types[
        "GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestIn"
    ] = t.struct(
        {
            "clientId": t.string().optional(),
            "ignoreErrorIfNoActiveWorkflow": t.boolean().optional(),
            "workflowName": t.string().optional(),
            "triggerId": t.string().optional(),
            "scheduledTime": t.string().optional(),
            "resourceName": t.string().optional(),
            "requestId": t.string().optional(),
            "testMode": t.boolean().optional(),
            "priority": t.string().optional(),
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersIn"]
            ).optional(),
        }
    ).named(
        renames["GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestIn"]
    )
    types[
        "GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestOut"
    ] = t.struct(
        {
            "clientId": t.string().optional(),
            "ignoreErrorIfNoActiveWorkflow": t.boolean().optional(),
            "workflowName": t.string().optional(),
            "triggerId": t.string().optional(),
            "scheduledTime": t.string().optional(),
            "resourceName": t.string().optional(),
            "requestId": t.string().optional(),
            "testMode": t.boolean().optional(),
            "priority": t.string().optional(),
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestOut"]
    )
    types["EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterIn"] = t.struct(
        {"objectValue": t.string()}
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterIn"])
    types["EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterOut"] = t.struct(
        {
            "objectValue": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterOut"])
    types["EnterpriseCrmEventbusProtoEventExecutionSnapshotIn"] = t.struct(
        {
            "conditionResults": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoConditionResultIn"])
            ).optional(),
            "taskExecutionDetails": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskExecutionDetailsIn"])
            ).optional(),
            "diffParams": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersIn"]
            ).optional(),
            "snapshotTime": t.string().optional(),
            "taskName": t.string().optional(),
            "exceedMaxSize": t.boolean().optional(),
            "eventParams": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersIn"]
            ).optional(),
            "eventExecutionInfoId": t.string().optional(),
            "checkpointTaskNumber": t.string().optional(),
            "eventExecutionSnapshotMetadata": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataIn"
                ]
            ),
            "eventExecutionSnapshotId": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoEventExecutionSnapshotIn"])
    types["EnterpriseCrmEventbusProtoEventExecutionSnapshotOut"] = t.struct(
        {
            "conditionResults": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoConditionResultOut"])
            ).optional(),
            "taskExecutionDetails": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskExecutionDetailsOut"])
            ).optional(),
            "diffParams": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersOut"]
            ).optional(),
            "snapshotTime": t.string().optional(),
            "taskName": t.string().optional(),
            "exceedMaxSize": t.boolean().optional(),
            "eventParams": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersOut"]
            ).optional(),
            "eventExecutionInfoId": t.string().optional(),
            "checkpointTaskNumber": t.string().optional(),
            "eventExecutionSnapshotMetadata": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataOut"
                ]
            ),
            "eventExecutionSnapshotId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoEventExecutionSnapshotOut"])
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
    types["EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn"] = t.struct(
        {
            "triggerType": t.string(),
            "label": t.string().optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "position": t.proxy(
                renames["EnterpriseCrmEventbusProtoCoordinateIn"]
            ).optional(),
            "pauseWorkflowExecutions": t.boolean().optional(),
            "triggerId": t.string().optional(),
            "alertConfig": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoWorkflowAlertConfigIn"])
            ).optional(),
            "enabledClients": t.array(t.string()),
            "cloudSchedulerConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoCloudSchedulerConfigIn"]
            ),
            "errorCatcherId": t.string().optional(),
            "startTasks": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoNextTaskIn"])
            ).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "triggerNumber": t.string(),
            "triggerCriteria": t.proxy(
                renames["EnterpriseCrmEventbusProtoTriggerCriteriaIn"]
            ).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn"])
    types["EnterpriseCrmFrontendsEventbusProtoTriggerConfigOut"] = t.struct(
        {
            "triggerType": t.string(),
            "label": t.string().optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "position": t.proxy(
                renames["EnterpriseCrmEventbusProtoCoordinateOut"]
            ).optional(),
            "pauseWorkflowExecutions": t.boolean().optional(),
            "triggerId": t.string().optional(),
            "alertConfig": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoWorkflowAlertConfigOut"])
            ).optional(),
            "enabledClients": t.array(t.string()),
            "cloudSchedulerConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoCloudSchedulerConfigOut"]
            ),
            "errorCatcherId": t.string().optional(),
            "startTasks": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoNextTaskOut"])
            ).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "triggerNumber": t.string(),
            "triggerCriteria": t.proxy(
                renames["EnterpriseCrmEventbusProtoTriggerCriteriaOut"]
            ).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigOut"])
    types["EnterpriseCrmEventbusProtoLoopMetadataIn"] = t.struct(
        {
            "currentIterationCount": t.string().optional(),
            "failureLocation": t.string().optional(),
            "currentIterationDetail": t.string().optional(),
            "errorMsg": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoLoopMetadataIn"])
    types["EnterpriseCrmEventbusProtoLoopMetadataOut"] = t.struct(
        {
            "currentIterationCount": t.string().optional(),
            "failureLocation": t.string().optional(),
            "currentIterationDetail": t.string().optional(),
            "errorMsg": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoLoopMetadataOut"])
    types["GoogleCloudIntegrationsV1alphaResolveSuspensionResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaResolveSuspensionResponseIn"])
    types["GoogleCloudIntegrationsV1alphaResolveSuspensionResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaResolveSuspensionResponseOut"])
    types["GoogleCloudIntegrationsV1alphaCertificateIn"] = t.struct(
        {
            "credentialId": t.string().optional(),
            "description": t.string().optional(),
            "certificateStatus": t.string().optional(),
            "displayName": t.string().optional(),
            "rawCertificate": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaClientCertificateIn"]
            ).optional(),
            "requestorId": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCertificateIn"])
    types["GoogleCloudIntegrationsV1alphaCertificateOut"] = t.struct(
        {
            "credentialId": t.string().optional(),
            "validStartTime": t.string().optional(),
            "validEndTime": t.string().optional(),
            "description": t.string().optional(),
            "certificateStatus": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "rawCertificate": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaClientCertificateOut"]
            ).optional(),
            "requestorId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCertificateOut"])
    types["EnterpriseCrmEventbusProtoSuccessPolicyIn"] = t.struct(
        {"finalState": t.string().optional()}
    ).named(renames["EnterpriseCrmEventbusProtoSuccessPolicyIn"])
    types["EnterpriseCrmEventbusProtoSuccessPolicyOut"] = t.struct(
        {
            "finalState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuccessPolicyOut"])
    types["GoogleCloudIntegrationsV1alphaIntParameterArrayIn"] = t.struct(
        {"intValues": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaIntParameterArrayIn"])
    types["GoogleCloudIntegrationsV1alphaIntParameterArrayOut"] = t.struct(
        {
            "intValues": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntParameterArrayOut"])
    types["EnterpriseCrmEventbusProtoSuspensionResolutionInfoIn"] = t.struct(
        {
            "clientId": t.string().optional(),
            "audit": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditIn"]
            ),
            "eventExecutionInfoId": t.string(),
            "lastModifiedTimestamp": t.string().optional(),
            "externalTraffic": t.proxy(
                renames["EnterpriseCrmEventbusProtoExternalTrafficIn"]
            ).optional(),
            "wrappedDek": t.string().optional(),
            "createdTimestamp": t.string().optional(),
            "cloudKmsConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoCloudKmsConfigIn"]
            ).optional(),
            "suspensionId": t.string().optional(),
            "status": t.string(),
            "encryptedSuspensionResolutionInfo": t.string().optional(),
            "suspensionConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionConfigIn"]
            ),
            "product": t.string().optional(),
            "taskNumber": t.string(),
            "workflowName": t.string(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionResolutionInfoIn"])
    types["EnterpriseCrmEventbusProtoSuspensionResolutionInfoOut"] = t.struct(
        {
            "clientId": t.string().optional(),
            "audit": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditOut"]
            ),
            "eventExecutionInfoId": t.string(),
            "lastModifiedTimestamp": t.string().optional(),
            "externalTraffic": t.proxy(
                renames["EnterpriseCrmEventbusProtoExternalTrafficOut"]
            ).optional(),
            "wrappedDek": t.string().optional(),
            "createdTimestamp": t.string().optional(),
            "cloudKmsConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoCloudKmsConfigOut"]
            ).optional(),
            "suspensionId": t.string().optional(),
            "status": t.string(),
            "encryptedSuspensionResolutionInfo": t.string().optional(),
            "suspensionConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionConfigOut"]
            ),
            "product": t.string().optional(),
            "taskNumber": t.string(),
            "workflowName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionResolutionInfoOut"])
    types["GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationIn"] = t.struct(
        {"remindTime": t.string().optional(), "liftWhenExpired": t.boolean().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationIn"])
    types["GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationOut"] = t.struct(
        {
            "remindTime": t.string().optional(),
            "liftWhenExpired": t.boolean().optional(),
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationOut"])
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
    types["GoogleCloudIntegrationsV1alphaTaskExecutionDetailsIn"] = t.struct(
        {
            "taskExecutionState": t.string().optional(),
            "taskNumber": t.string().optional(),
            "taskAttemptStats": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaAttemptStatsIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaTaskExecutionDetailsIn"])
    types["GoogleCloudIntegrationsV1alphaTaskExecutionDetailsOut"] = t.struct(
        {
            "taskExecutionState": t.string().optional(),
            "taskNumber": t.string().optional(),
            "taskAttemptStats": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaAttemptStatsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaTaskExecutionDetailsOut"])
    types["EnterpriseCrmLoggingGwsFieldLimitsIn"] = t.struct(
        {
            "maxStringLength": t.integer().optional(),
            "logType": t.array(t.string()).optional(),
            "shortenerType": t.string(),
            "maxArraySize": t.integer().optional(),
            "logAction": t.string(),
        }
    ).named(renames["EnterpriseCrmLoggingGwsFieldLimitsIn"])
    types["EnterpriseCrmLoggingGwsFieldLimitsOut"] = t.struct(
        {
            "maxStringLength": t.integer().optional(),
            "logType": t.array(t.string()).optional(),
            "shortenerType": t.string(),
            "maxArraySize": t.integer().optional(),
            "logAction": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmLoggingGwsFieldLimitsOut"])
    types["GoogleCloudIntegrationsV1alphaIntegrationParameterIn"] = t.struct(
        {
            "dataType": t.string().optional(),
            "inputOutputType": t.string().optional(),
            "displayName": t.string().optional(),
            "isTransient": t.boolean().optional(),
            "jsonSchema": t.string().optional(),
            "searchable": t.boolean().optional(),
            "key": t.string().optional(),
            "defaultValue": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaValueTypeIn"]
            ).optional(),
            "producer": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationParameterIn"])
    types["GoogleCloudIntegrationsV1alphaIntegrationParameterOut"] = t.struct(
        {
            "dataType": t.string().optional(),
            "inputOutputType": t.string().optional(),
            "displayName": t.string().optional(),
            "isTransient": t.boolean().optional(),
            "jsonSchema": t.string().optional(),
            "searchable": t.boolean().optional(),
            "key": t.string().optional(),
            "defaultValue": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaValueTypeOut"]
            ).optional(),
            "producer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationParameterOut"])
    types["EnterpriseCrmEventbusProtoTaskUiModuleConfigIn"] = t.struct(
        {"moduleId": t.string().optional()}
    ).named(renames["EnterpriseCrmEventbusProtoTaskUiModuleConfigIn"])
    types["EnterpriseCrmEventbusProtoTaskUiModuleConfigOut"] = t.struct(
        {
            "moduleId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskUiModuleConfigOut"])
    types["EnterpriseCrmEventbusProtoStringArrayIn"] = t.struct(
        {"values": t.array(t.string())}
    ).named(renames["EnterpriseCrmEventbusProtoStringArrayIn"])
    types["EnterpriseCrmEventbusProtoStringArrayOut"] = t.struct(
        {
            "values": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoStringArrayOut"])
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
    types["EnterpriseCrmEventbusProtoDoubleArrayIn"] = t.struct(
        {"values": t.array(t.number())}
    ).named(renames["EnterpriseCrmEventbusProtoDoubleArrayIn"])
    types["EnterpriseCrmEventbusProtoDoubleArrayOut"] = t.struct(
        {
            "values": t.array(t.number()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoDoubleArrayOut"])
    types["EnterpriseCrmEventbusProtoMappedFieldIn"] = t.struct(
        {
            "outputField": t.proxy(
                renames["EnterpriseCrmEventbusProtoFieldIn"]
            ).optional(),
            "inputField": t.proxy(
                renames["EnterpriseCrmEventbusProtoFieldIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoMappedFieldIn"])
    types["EnterpriseCrmEventbusProtoMappedFieldOut"] = t.struct(
        {
            "outputField": t.proxy(
                renames["EnterpriseCrmEventbusProtoFieldOut"]
            ).optional(),
            "inputField": t.proxy(
                renames["EnterpriseCrmEventbusProtoFieldOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoMappedFieldOut"])
    types["GoogleCloudIntegrationsV1alphaRuntimeActionSchemaIn"] = t.struct(
        {
            "action": t.string().optional(),
            "inputSchema": t.string().optional(),
            "outputSchema": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaRuntimeActionSchemaIn"])
    types["GoogleCloudIntegrationsV1alphaRuntimeActionSchemaOut"] = t.struct(
        {
            "action": t.string().optional(),
            "inputSchema": t.string().optional(),
            "outputSchema": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaRuntimeActionSchemaOut"])
    types["EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionIn"] = t.struct(
        {"path": t.string().optional(), "fullName": t.string().optional()}
    ).named(renames["EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionIn"])
    types["EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionOut"] = t.struct(
        {
            "path": t.string().optional(),
            "fullName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionOut"])
    types["EnterpriseCrmEventbusProtoTeardownTaskConfigIn"] = t.struct(
        {
            "name": t.string(),
            "teardownTaskImplementationClassName": t.string(),
            "creatorEmail": t.string().optional(),
            "nextTeardownTask": t.proxy(
                renames["EnterpriseCrmEventbusProtoNextTeardownTaskIn"]
            ),
            "properties": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventBusPropertiesIn"]
            ),
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTeardownTaskConfigIn"])
    types["EnterpriseCrmEventbusProtoTeardownTaskConfigOut"] = t.struct(
        {
            "name": t.string(),
            "teardownTaskImplementationClassName": t.string(),
            "creatorEmail": t.string().optional(),
            "nextTeardownTask": t.proxy(
                renames["EnterpriseCrmEventbusProtoNextTeardownTaskOut"]
            ),
            "properties": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventBusPropertiesOut"]
            ),
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTeardownTaskConfigOut"])
    types["EnterpriseCrmEventbusProtoCloudKmsConfigIn"] = t.struct(
        {
            "keyName": t.string().optional(),
            "gcpProjectId": t.string().optional(),
            "locationName": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "keyRingName": t.string().optional(),
            "keyVersionName": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoCloudKmsConfigIn"])
    types["EnterpriseCrmEventbusProtoCloudKmsConfigOut"] = t.struct(
        {
            "keyName": t.string().optional(),
            "gcpProjectId": t.string().optional(),
            "locationName": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "keyRingName": t.string().optional(),
            "keyVersionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoCloudKmsConfigOut"])
    types["EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryIn"] = t.struct(
        {
            "key": t.string().optional(),
            "protoDefName": t.string().optional(),
            "producedBy": t.proxy(
                renames["EnterpriseCrmEventbusProtoNodeIdentifierIn"]
            ).optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn"]
            ).optional(),
            "dataType": t.string().optional(),
            "isTransient": t.boolean().optional(),
            "jsonSchema": t.string().optional(),
            "producer": t.string(),
            "inOutType": t.string().optional(),
            "name": t.string().optional(),
            "children": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryIn"
                    ]
                )
            ).optional(),
            "attributes": t.proxy(
                renames["EnterpriseCrmEventbusProtoAttributesIn"]
            ).optional(),
            "protoDefPath": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryIn"])
    types["EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryOut"] = t.struct(
        {
            "key": t.string().optional(),
            "protoDefName": t.string().optional(),
            "producedBy": t.proxy(
                renames["EnterpriseCrmEventbusProtoNodeIdentifierOut"]
            ).optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "dataType": t.string().optional(),
            "isTransient": t.boolean().optional(),
            "jsonSchema": t.string().optional(),
            "producer": t.string(),
            "inOutType": t.string().optional(),
            "name": t.string().optional(),
            "children": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryOut"
                    ]
                )
            ).optional(),
            "attributes": t.proxy(
                renames["EnterpriseCrmEventbusProtoAttributesOut"]
            ).optional(),
            "protoDefPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryOut"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn"] = t.struct(
        {
            "doubleArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayIn"]
            ),
            "booleanValue": t.boolean(),
            "serializedObjectValue": t.proxy(
                renames[
                    "EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterIn"
                ]
            ),
            "stringArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoStringParameterArrayIn"]
            ),
            "intArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoIntParameterArrayIn"]
            ),
            "doubleValue": t.number(),
            "protoValue": t.struct({"_": t.string().optional()}),
            "intValue": t.string(),
            "stringValue": t.string(),
            "booleanArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayIn"]
            ),
            "jsonValue": t.string(),
            "protoArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayIn"]
            ),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut"] = t.struct(
        {
            "doubleArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayOut"]
            ),
            "booleanValue": t.boolean(),
            "serializedObjectValue": t.proxy(
                renames[
                    "EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterOut"
                ]
            ),
            "stringArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoStringParameterArrayOut"]
            ),
            "intArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoIntParameterArrayOut"]
            ),
            "doubleValue": t.number(),
            "protoValue": t.struct({"_": t.string().optional()}),
            "intValue": t.string(),
            "stringValue": t.string(),
            "booleanArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayOut"]
            ),
            "jsonValue": t.string(),
            "protoArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut"])
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
    types["EnterpriseCrmEventbusProtoParameterMapIn"] = t.struct(
        {
            "valueType": t.string(),
            "entries": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoParameterMapEntryIn"])
            ),
            "keyType": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParameterMapIn"])
    types["EnterpriseCrmEventbusProtoParameterMapOut"] = t.struct(
        {
            "valueType": t.string(),
            "entries": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoParameterMapEntryOut"])
            ),
            "keyType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParameterMapOut"])
    types["GoogleCloudIntegrationsV1alphaTaskConfigIn"] = t.struct(
        {
            "nextTasks": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaNextTaskIn"])
            ).optional(),
            "task": t.string().optional(),
            "errorCatcherId": t.string().optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCoordinateIn"]
            ).optional(),
            "taskId": t.string(),
            "taskExecutionStrategy": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "failurePolicy": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaFailurePolicyIn"]
            ).optional(),
            "externalTaskType": t.string().optional(),
            "successPolicy": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuccessPolicyIn"]
            ).optional(),
            "description": t.string().optional(),
            "taskTemplate": t.string().optional(),
            "jsonValidationOption": t.string().optional(),
            "synchronousCallFailurePolicy": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaFailurePolicyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaTaskConfigIn"])
    types["GoogleCloudIntegrationsV1alphaTaskConfigOut"] = t.struct(
        {
            "nextTasks": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaNextTaskOut"])
            ).optional(),
            "task": t.string().optional(),
            "errorCatcherId": t.string().optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCoordinateOut"]
            ).optional(),
            "taskId": t.string(),
            "taskExecutionStrategy": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "failurePolicy": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaFailurePolicyOut"]
            ).optional(),
            "externalTaskType": t.string().optional(),
            "successPolicy": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuccessPolicyOut"]
            ).optional(),
            "description": t.string().optional(),
            "taskTemplate": t.string().optional(),
            "jsonValidationOption": t.string().optional(),
            "synchronousCallFailurePolicy": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaFailurePolicyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaTaskConfigOut"])
    types["EnterpriseCrmEventbusProtoAddressIn"] = t.struct(
        {
            "name": t.string(),
            "tokens": t.array(t.proxy(renames["EnterpriseCrmEventbusProtoTokenIn"])),
            "email": t.string(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoAddressIn"])
    types["EnterpriseCrmEventbusProtoAddressOut"] = t.struct(
        {
            "name": t.string(),
            "tokens": t.array(t.proxy(renames["EnterpriseCrmEventbusProtoTokenOut"])),
            "email": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoAddressOut"])
    types["EnterpriseCrmEventbusProtoStringArrayFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoStringArrayFunctionIn"])
    types["EnterpriseCrmEventbusProtoStringArrayFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoStringArrayFunctionOut"])
    types["EnterpriseCrmEventbusProtoBuganizerNotificationIn"] = t.struct(
        {
            "componentId": t.string().optional(),
            "assigneeEmailAddress": t.string().optional(),
            "title": t.string().optional(),
            "templateId": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBuganizerNotificationIn"])
    types["EnterpriseCrmEventbusProtoBuganizerNotificationOut"] = t.struct(
        {
            "componentId": t.string().optional(),
            "assigneeEmailAddress": t.string().optional(),
            "title": t.string().optional(),
            "templateId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBuganizerNotificationOut"])
    types["GoogleCloudIntegrationsV1alphaJwtIn"] = t.struct(
        {
            "jwt": t.string().optional(),
            "jwtPayload": t.string().optional(),
            "secret": t.string().optional(),
            "jwtHeader": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaJwtIn"])
    types["GoogleCloudIntegrationsV1alphaJwtOut"] = t.struct(
        {
            "jwt": t.string().optional(),
            "jwtPayload": t.string().optional(),
            "secret": t.string().optional(),
            "jwtHeader": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaJwtOut"])
    types[
        "GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseIn"
    ] = t.struct(
        {
            "runtimeEntitySchemas": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseIn"]
    )
    types[
        "GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseOut"
    ] = t.struct(
        {
            "runtimeEntitySchemas": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseOut"]
    )
    types["GoogleCloudIntegrationsV1alphaExecutionSnapshotIn"] = t.struct(
        {
            "checkpointTaskNumber": t.string().optional(),
            "executionSnapshotMetadata": t.proxy(
                renames[
                    "GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataIn"
                ]
            ).optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "taskExecutionDetails": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaTaskExecutionDetailsIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecutionSnapshotIn"])
    types["GoogleCloudIntegrationsV1alphaExecutionSnapshotOut"] = t.struct(
        {
            "checkpointTaskNumber": t.string().optional(),
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
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecutionSnapshotOut"])
    types["GoogleCloudIntegrationsV1alphaCredentialIn"] = t.struct(
        {
            "oauth2ClientCredentials": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsIn"]
            ).optional(),
            "serviceAccountCredentials": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaServiceAccountCredentialsIn"]
            ).optional(),
            "oauth2ResourceOwnerCredentials": t.proxy(
                renames[
                    "GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsIn"
                ]
            ).optional(),
            "oidcToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaOidcTokenIn"]
            ).optional(),
            "jwt": t.proxy(renames["GoogleCloudIntegrationsV1alphaJwtIn"]).optional(),
            "credentialType": t.string().optional(),
            "usernameAndPassword": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaUsernameAndPasswordIn"]
            ).optional(),
            "authToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAuthTokenIn"]
            ).optional(),
            "oauth2AuthorizationCode": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCredentialIn"])
    types["GoogleCloudIntegrationsV1alphaCredentialOut"] = t.struct(
        {
            "oauth2ClientCredentials": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsOut"]
            ).optional(),
            "serviceAccountCredentials": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaServiceAccountCredentialsOut"]
            ).optional(),
            "oauth2ResourceOwnerCredentials": t.proxy(
                renames[
                    "GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsOut"
                ]
            ).optional(),
            "oidcToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaOidcTokenOut"]
            ).optional(),
            "jwt": t.proxy(renames["GoogleCloudIntegrationsV1alphaJwtOut"]).optional(),
            "credentialType": t.string().optional(),
            "usernameAndPassword": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaUsernameAndPasswordOut"]
            ).optional(),
            "authToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAuthTokenOut"]
            ).optional(),
            "oauth2AuthorizationCode": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCredentialOut"])
    types[
        "GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataIn"
    ] = t.struct(
        {
            "taskAttempt": t.integer().optional(),
            "taskNumber": t.string().optional(),
            "executionAttempt": t.integer().optional(),
            "taskLabel": t.string().optional(),
            "task": t.string().optional(),
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
            "taskAttempt": t.integer().optional(),
            "taskNumber": t.string().optional(),
            "executionAttempt": t.integer().optional(),
            "taskLabel": t.string().optional(),
            "task": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataOut"
        ]
    )
    types["GoogleCloudIntegrationsV1alphaParameterMapIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaParameterMapEntryIn"])
            ).optional(),
            "valueType": t.string().optional(),
            "keyType": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaParameterMapIn"])
    types["GoogleCloudIntegrationsV1alphaParameterMapOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaParameterMapEntryOut"])
            ).optional(),
            "valueType": t.string().optional(),
            "keyType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaParameterMapOut"])
    types["GoogleCloudIntegrationsV1alphaStringParameterArrayIn"] = t.struct(
        {"stringValues": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaStringParameterArrayIn"])
    types["GoogleCloudIntegrationsV1alphaStringParameterArrayOut"] = t.struct(
        {
            "stringValues": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaStringParameterArrayOut"])
    types["EnterpriseCrmEventbusProtoPropertyEntryIn"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.proxy(
                renames["EnterpriseCrmEventbusProtoValueTypeIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoPropertyEntryIn"])
    types["EnterpriseCrmEventbusProtoPropertyEntryOut"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.proxy(
                renames["EnterpriseCrmEventbusProtoValueTypeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoPropertyEntryOut"])
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
    types["EnterpriseCrmEventbusProtoTriggerCriteriaIn"] = t.struct(
        {
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersIn"]
            ).optional(),
            "triggerCriteriaTaskImplementationClassName": t.string().optional(),
            "condition": t.string(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTriggerCriteriaIn"])
    types["EnterpriseCrmEventbusProtoTriggerCriteriaOut"] = t.struct(
        {
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersOut"]
            ).optional(),
            "triggerCriteriaTaskImplementationClassName": t.string().optional(),
            "condition": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTriggerCriteriaOut"])
    types["EnterpriseCrmEventbusProtoFunctionTypeIn"] = t.struct(
        {
            "intArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoIntArrayFunctionIn"]
            ),
            "stringArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoStringArrayFunctionIn"]
            ),
            "doubleFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoDoubleFunctionIn"]
            ),
            "booleanArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoBooleanArrayFunctionIn"]
            ),
            "stringFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoStringFunctionIn"]
            ),
            "protoArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoProtoArrayFunctionIn"]
            ),
            "intFunction": t.proxy(renames["EnterpriseCrmEventbusProtoIntFunctionIn"]),
            "protoFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoProtoFunctionIn"]
            ),
            "baseFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseFunctionIn"]
            ).optional(),
            "booleanFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoBooleanFunctionIn"]
            ),
            "jsonFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoJsonFunctionIn"]
            ).optional(),
            "doubleArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoDoubleArrayFunctionIn"]
            ),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFunctionTypeIn"])
    types["EnterpriseCrmEventbusProtoFunctionTypeOut"] = t.struct(
        {
            "intArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoIntArrayFunctionOut"]
            ),
            "stringArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoStringArrayFunctionOut"]
            ),
            "doubleFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoDoubleFunctionOut"]
            ),
            "booleanArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoBooleanArrayFunctionOut"]
            ),
            "stringFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoStringFunctionOut"]
            ),
            "protoArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoProtoArrayFunctionOut"]
            ),
            "intFunction": t.proxy(renames["EnterpriseCrmEventbusProtoIntFunctionOut"]),
            "protoFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoProtoFunctionOut"]
            ),
            "baseFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseFunctionOut"]
            ).optional(),
            "booleanFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoBooleanFunctionOut"]
            ),
            "jsonFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoJsonFunctionOut"]
            ).optional(),
            "doubleArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoDoubleArrayFunctionOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFunctionTypeOut"])
    types["GoogleCloudIntegrationsV1alphaIntegrationIn"] = t.struct(
        {
            "active": t.boolean(),
            "name": t.string(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationIn"])
    types["GoogleCloudIntegrationsV1alphaIntegrationOut"] = t.struct(
        {
            "active": t.boolean(),
            "updateTime": t.string().optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationOut"])
    types["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsIn"] = t.struct(
        {
            "issuer": t.string().optional(),
            "audience": t.string().optional(),
            "subject": t.string().optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsIn"])
    types["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsOut"] = t.struct(
        {
            "issuer": t.string().optional(),
            "audience": t.string().optional(),
            "subject": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsOut"])
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
    types["GoogleCloudIntegrationsV1alphaAccessTokenIn"] = t.struct(
        {
            "refreshToken": t.string().optional(),
            "accessToken": t.string().optional(),
            "tokenType": t.string().optional(),
            "accessTokenExpireTime": t.string(),
            "refreshTokenExpireTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaAccessTokenIn"])
    types["GoogleCloudIntegrationsV1alphaAccessTokenOut"] = t.struct(
        {
            "refreshToken": t.string().optional(),
            "accessToken": t.string().optional(),
            "tokenType": t.string().optional(),
            "accessTokenExpireTime": t.string(),
            "refreshTokenExpireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaAccessTokenOut"])
    types["EnterpriseCrmEventbusProtoNextTaskIn"] = t.struct(
        {
            "taskNumber": t.string().optional(),
            "label": t.string().optional(),
            "combinedConditions": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoCombinedConditionIn"])
            ).optional(),
            "description": t.string().optional(),
            "condition": t.string().optional(),
            "taskConfigId": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoNextTaskIn"])
    types["EnterpriseCrmEventbusProtoNextTaskOut"] = t.struct(
        {
            "taskNumber": t.string().optional(),
            "label": t.string().optional(),
            "combinedConditions": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoCombinedConditionOut"])
            ).optional(),
            "description": t.string().optional(),
            "condition": t.string().optional(),
            "taskConfigId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoNextTaskOut"])
    types["EnterpriseCrmEventbusStatsDimensionsIn"] = t.struct(
        {
            "triggerId": t.string().optional(),
            "enumFilterType": t.string().optional(),
            "taskNumber": t.string(),
            "workflowId": t.string(),
            "clientId": t.string(),
            "errorEnumString": t.string(),
            "retryAttempt": t.string(),
            "warningEnumString": t.string(),
            "workflowName": t.string(),
            "taskName": t.string(),
        }
    ).named(renames["EnterpriseCrmEventbusStatsDimensionsIn"])
    types["EnterpriseCrmEventbusStatsDimensionsOut"] = t.struct(
        {
            "triggerId": t.string().optional(),
            "enumFilterType": t.string().optional(),
            "taskNumber": t.string(),
            "workflowId": t.string(),
            "clientId": t.string(),
            "errorEnumString": t.string(),
            "retryAttempt": t.string(),
            "warningEnumString": t.string(),
            "workflowName": t.string(),
            "taskName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusStatsDimensionsOut"])
    types["EnterpriseCrmEventbusProtoParameterEntryIn"] = t.struct(
        {
            "value": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeIn"]
            ).optional(),
            "key": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParameterEntryIn"])
    types["EnterpriseCrmEventbusProtoParameterEntryOut"] = t.struct(
        {
            "value": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParameterEntryOut"])
    types["EnterpriseCrmEventbusProtoIntFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoIntFunctionIn"])
    types["EnterpriseCrmEventbusProtoIntFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoIntFunctionOut"])
    types["GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseIn"] = t.struct(
        {
            "sfdcInstances": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseIn"])
    types["GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseOut"] = t.struct(
        {
            "sfdcInstances": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseOut"])
    types["EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamIn"] = t.struct(
        {
            "allowedServiceAccountInContext": t.boolean(),
            "scope": t.string().optional(),
            "authConfigId": t.string().optional(),
            "allowedCredentialTypes": t.array(t.string()).optional(),
            "useServiceAccountInContext": t.boolean(),
        }
    ).named(renames["EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamIn"])
    types["EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamOut"] = t.struct(
        {
            "allowedServiceAccountInContext": t.boolean(),
            "scope": t.string().optional(),
            "authConfigId": t.string().optional(),
            "allowedCredentialTypes": t.array(t.string()).optional(),
            "useServiceAccountInContext": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamOut"])
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
    types["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestIn"] = t.struct(
        {"scriptId": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestIn"])
    types["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestOut"] = t.struct(
        {
            "scriptId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestOut"])
    types["GoogleCloudIntegrationsV1alphaListSuspensionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "suspensions": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaSuspensionIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListSuspensionsResponseIn"])
    types["GoogleCloudIntegrationsV1alphaListSuspensionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "suspensions": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaSuspensionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListSuspensionsResponseOut"])
    types["EnterpriseCrmEventbusProtoBooleanFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoBooleanFunctionIn"])
    types["EnterpriseCrmEventbusProtoBooleanFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBooleanFunctionOut"])
    types["GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigIn"] = t.struct(
        {
            "customMessage": t.string().optional(),
            "expiration": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationIn"]
            ).optional(),
            "emailAddresses": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigIn"])
    types["GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigOut"] = t.struct(
        {
            "customMessage": t.string().optional(),
            "expiration": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationOut"]
            ).optional(),
            "emailAddresses": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigOut"])
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
    types["GoogleCloudIntegrationsV1alphaLiftSuspensionResponseIn"] = t.struct(
        {"eventExecutionInfoId": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaLiftSuspensionResponseIn"])
    types["GoogleCloudIntegrationsV1alphaLiftSuspensionResponseOut"] = t.struct(
        {
            "eventExecutionInfoId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaLiftSuspensionResponseOut"])
    types["GoogleCloudIntegrationsV1alphaUsernameAndPasswordIn"] = t.struct(
        {"password": t.string().optional(), "username": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaUsernameAndPasswordIn"])
    types["GoogleCloudIntegrationsV1alphaUsernameAndPasswordOut"] = t.struct(
        {
            "password": t.string().optional(),
            "username": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaUsernameAndPasswordOut"])
    types[
        "GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseIn"
    ] = t.struct(
        {
            "runtimeActionSchemas": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaRuntimeActionSchemaIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseIn"]
    )
    types[
        "GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseOut"
    ] = t.struct(
        {
            "runtimeActionSchemas": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaRuntimeActionSchemaOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseOut"]
    )
    types["GoogleCloudIntegrationsV1alphaEventParameterIn"] = t.struct(
        {
            "value": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaValueTypeIn"]
            ).optional(),
            "key": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaEventParameterIn"])
    types["GoogleCloudIntegrationsV1alphaEventParameterOut"] = t.struct(
        {
            "value": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaValueTypeOut"]
            ).optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaEventParameterOut"])
    types["EnterpriseCrmEventbusProtoDoubleArrayFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoDoubleArrayFunctionIn"])
    types["EnterpriseCrmEventbusProtoDoubleArrayFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoDoubleArrayFunctionOut"])
    types["EnterpriseCrmEventbusProtoTaskMetadataIn"] = t.struct(
        {
            "docMarkdown": t.string().optional(),
            "system": t.string(),
            "status": t.string().optional(),
            "isDeprecated": t.boolean().optional(),
            "defaultSpec": t.string().optional(),
            "externalDocLink": t.string().optional(),
            "externalDocHtml": t.string().optional(),
            "activeTaskName": t.string().optional(),
            "iconLink": t.string().optional(),
            "externalCategory": t.string(),
            "g3DocLink": t.string().optional(),
            "admins": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskMetadataAdminIn"])
            ),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "descriptiveName": t.string().optional(),
            "category": t.string(),
            "codeSearchLink": t.string().optional(),
            "externalDocMarkdown": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "standaloneExternalDocHtml": t.string().optional(),
            "defaultJsonValidationOption": t.string().optional(),
            "externalCategorySequence": t.integer().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskMetadataIn"])
    types["EnterpriseCrmEventbusProtoTaskMetadataOut"] = t.struct(
        {
            "docMarkdown": t.string().optional(),
            "system": t.string(),
            "status": t.string().optional(),
            "isDeprecated": t.boolean().optional(),
            "defaultSpec": t.string().optional(),
            "externalDocLink": t.string().optional(),
            "externalDocHtml": t.string().optional(),
            "activeTaskName": t.string().optional(),
            "iconLink": t.string().optional(),
            "externalCategory": t.string(),
            "g3DocLink": t.string().optional(),
            "admins": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskMetadataAdminOut"])
            ),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "descriptiveName": t.string().optional(),
            "category": t.string(),
            "codeSearchLink": t.string().optional(),
            "externalDocMarkdown": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "standaloneExternalDocHtml": t.string().optional(),
            "defaultJsonValidationOption": t.string().optional(),
            "externalCategorySequence": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskMetadataOut"])
    types["EnterpriseCrmEventbusProtoParameterValueTypeIn"] = t.struct(
        {
            "protoArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoProtoParameterArrayIn"]
            ),
            "booleanValue": t.boolean(),
            "stringArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoStringParameterArrayIn"]
            ),
            "protoValue": t.struct({"_": t.string().optional()}),
            "intArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoIntParameterArrayIn"]
            ),
            "stringValue": t.string(),
            "booleanArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoBooleanParameterArrayIn"]
            ),
            "serializedObjectValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoSerializedObjectParameterIn"]
            ),
            "intValue": t.string(),
            "doubleArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoDoubleParameterArrayIn"]
            ),
            "doubleValue": t.number(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParameterValueTypeIn"])
    types["EnterpriseCrmEventbusProtoParameterValueTypeOut"] = t.struct(
        {
            "protoArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoProtoParameterArrayOut"]
            ),
            "booleanValue": t.boolean(),
            "stringArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoStringParameterArrayOut"]
            ),
            "protoValue": t.struct({"_": t.string().optional()}),
            "intArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoIntParameterArrayOut"]
            ),
            "stringValue": t.string(),
            "booleanArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoBooleanParameterArrayOut"]
            ),
            "serializedObjectValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoSerializedObjectParameterOut"]
            ),
            "intValue": t.string(),
            "doubleArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoDoubleParameterArrayOut"]
            ),
            "doubleValue": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParameterValueTypeOut"])
    types["EnterpriseCrmFrontendsEventbusProtoParamSpecEntryIn"] = t.struct(
        {
            "validationRule": t.proxy(
                renames["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIn"]
            ).optional(),
            "key": t.string().optional(),
            "required": t.boolean().optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn"]
            ).optional(),
            "isDeprecated": t.boolean().optional(),
            "dataType": t.string().optional(),
            "isOutput": t.boolean(),
            "collectionElementClassName": t.string().optional(),
            "className": t.string().optional(),
            "jsonSchema": t.string().optional(),
            "protoDef": t.proxy(
                renames["EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionIn"]
            ).optional(),
            "config": t.proxy(
                renames["EnterpriseCrmEventbusProtoParamSpecEntryConfigIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParamSpecEntryIn"])
    types["EnterpriseCrmFrontendsEventbusProtoParamSpecEntryOut"] = t.struct(
        {
            "validationRule": t.proxy(
                renames["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleOut"]
            ).optional(),
            "key": t.string().optional(),
            "required": t.boolean().optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "isDeprecated": t.boolean().optional(),
            "dataType": t.string().optional(),
            "isOutput": t.boolean(),
            "collectionElementClassName": t.string().optional(),
            "className": t.string().optional(),
            "jsonSchema": t.string().optional(),
            "protoDef": t.proxy(
                renames["EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionOut"]
            ).optional(),
            "config": t.proxy(
                renames["EnterpriseCrmEventbusProtoParamSpecEntryConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParamSpecEntryOut"])
    types["EnterpriseCrmEventbusProtoDoubleFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoDoubleFunctionIn"])
    types["EnterpriseCrmEventbusProtoDoubleFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoDoubleFunctionOut"])
    types["GoogleCloudConnectorsV1AuthConfigUserPasswordIn"] = t.struct(
        {
            "password": t.proxy(renames["GoogleCloudConnectorsV1SecretIn"]).optional(),
            "username": t.string().optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigUserPasswordIn"])
    types["GoogleCloudConnectorsV1AuthConfigUserPasswordOut"] = t.struct(
        {
            "password": t.proxy(renames["GoogleCloudConnectorsV1SecretOut"]).optional(),
            "username": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigUserPasswordOut"])
    types["GoogleCloudIntegrationsV1alphaLiftSuspensionRequestIn"] = t.struct(
        {"suspensionResult": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaLiftSuspensionRequestIn"])
    types["GoogleCloudIntegrationsV1alphaLiftSuspensionRequestOut"] = t.struct(
        {
            "suspensionResult": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaLiftSuspensionRequestOut"])
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
    types["EnterpriseCrmFrontendsEventbusProtoStringParameterArrayIn"] = t.struct(
        {"stringValues": t.array(t.string())}
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoStringParameterArrayIn"])
    types["EnterpriseCrmFrontendsEventbusProtoStringParameterArrayOut"] = t.struct(
        {
            "stringValues": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoStringParameterArrayOut"])
    types["GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestIn"] = t.struct(
        {
            "doNotPropagateError": t.boolean().optional(),
            "requestId": t.string().optional(),
            "parameterEntries": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"])
            ).optional(),
            "inputParameters": t.struct({"_": t.string().optional()}).optional(),
            "triggerId": t.string(),
            "executionId": t.string().optional(),
            "parameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestIn"])
    types["GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestOut"] = t.struct(
        {
            "doNotPropagateError": t.boolean().optional(),
            "requestId": t.string().optional(),
            "parameterEntries": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"])
            ).optional(),
            "inputParameters": t.struct({"_": t.string().optional()}).optional(),
            "triggerId": t.string(),
            "executionId": t.string().optional(),
            "parameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestOut"])
    types["EnterpriseCrmEventbusProtoTaskAlertConfigIn"] = t.struct(
        {
            "alertName": t.string().optional(),
            "aggregationPeriod": t.string().optional(),
            "alertDisabled": t.boolean().optional(),
            "thresholdType": t.string().optional(),
            "warningEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn"]
            ),
            "numAggregationPeriods": t.integer().optional(),
            "durationThresholdMs": t.string().optional(),
            "onlyFinalAttempt": t.boolean().optional(),
            "clientId": t.string().optional(),
            "errorEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn"]
            ),
            "playbookUrl": t.string().optional(),
            "thresholdValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueIn"]
            ).optional(),
            "metricType": t.string(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskAlertConfigIn"])
    types["EnterpriseCrmEventbusProtoTaskAlertConfigOut"] = t.struct(
        {
            "alertName": t.string().optional(),
            "aggregationPeriod": t.string().optional(),
            "alertDisabled": t.boolean().optional(),
            "thresholdType": t.string().optional(),
            "warningEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut"]
            ),
            "numAggregationPeriods": t.integer().optional(),
            "durationThresholdMs": t.string().optional(),
            "onlyFinalAttempt": t.boolean().optional(),
            "clientId": t.string().optional(),
            "errorEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut"]
            ),
            "playbookUrl": t.string().optional(),
            "thresholdValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueOut"]
            ).optional(),
            "metricType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskAlertConfigOut"])
    types["EnterpriseCrmEventbusProtoSerializedObjectParameterIn"] = t.struct(
        {"objectValue": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoSerializedObjectParameterIn"])
    types["EnterpriseCrmEventbusProtoSerializedObjectParameterOut"] = t.struct(
        {
            "objectValue": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSerializedObjectParameterOut"])
    types["GoogleCloudIntegrationsV1alphaTriggerConfigIn"] = t.struct(
        {
            "description": t.string().optional(),
            "triggerType": t.string().optional(),
            "label": t.string().optional(),
            "alertConfig": t.array(
                t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigIn"]
                )
            ).optional(),
            "errorCatcherId": t.string().optional(),
            "triggerId": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCoordinateIn"]
            ).optional(),
            "cloudSchedulerConfig": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCloudSchedulerConfigIn"]
            ).optional(),
            "triggerNumber": t.string(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "startTasks": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaNextTaskIn"])
            ).optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaTriggerConfigIn"])
    types["GoogleCloudIntegrationsV1alphaTriggerConfigOut"] = t.struct(
        {
            "description": t.string().optional(),
            "triggerType": t.string().optional(),
            "label": t.string().optional(),
            "alertConfig": t.array(
                t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigOut"]
                )
            ).optional(),
            "errorCatcherId": t.string().optional(),
            "triggerId": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCoordinateOut"]
            ).optional(),
            "cloudSchedulerConfig": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCloudSchedulerConfigOut"]
            ).optional(),
            "triggerNumber": t.string(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "startTasks": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaNextTaskOut"])
            ).optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaTriggerConfigOut"])
    types["GoogleCloudIntegrationsV1alphaListExecutionsResponseIn"] = t.struct(
        {
            "executions": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaExecutionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "executionInfos": t.array(
                t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoIn"]
                )
            ),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListExecutionsResponseIn"])
    types["GoogleCloudIntegrationsV1alphaListExecutionsResponseOut"] = t.struct(
        {
            "executions": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaExecutionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "executionInfos": t.array(
                t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoOut"]
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListExecutionsResponseOut"])
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
    types[
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeIn"
    ] = t.struct({"max": t.number().optional(), "min": t.number().optional()}).named(
        renames["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeIn"]
    )
    types[
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeOut"
    ] = t.struct(
        {
            "max": t.number().optional(),
            "min": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeOut"]
    )
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
    types["GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestIn"])
    types["GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestOut"])
    types["EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotIn"] = t.struct(
        {
            "checkpointTaskNumber": t.string().optional(),
            "eventParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
            ).optional(),
            "eventExecutionSnapshotMetadata": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataIn"
                ]
            ),
            "taskExecutionDetails": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskExecutionDetailsIn"])
            ).optional(),
            "eventExecutionSnapshotId": t.string().optional(),
            "diffParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
            ).optional(),
            "conditionResults": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoConditionResultIn"])
            ).optional(),
            "snapshotTime": t.string().optional(),
            "taskName": t.string().optional(),
            "eventExecutionInfoId": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotIn"])
    types["EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotOut"] = t.struct(
        {
            "checkpointTaskNumber": t.string().optional(),
            "eventParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "eventExecutionSnapshotMetadata": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataOut"
                ]
            ),
            "taskExecutionDetails": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskExecutionDetailsOut"])
            ).optional(),
            "eventExecutionSnapshotId": t.string().optional(),
            "diffParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "conditionResults": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoConditionResultOut"])
            ).optional(),
            "snapshotTime": t.string().optional(),
            "taskName": t.string().optional(),
            "eventExecutionInfoId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotOut"])
    types["EnterpriseCrmEventbusProtoDoubleParameterArrayIn"] = t.struct(
        {"doubleValues": t.array(t.number())}
    ).named(renames["EnterpriseCrmEventbusProtoDoubleParameterArrayIn"])
    types["EnterpriseCrmEventbusProtoDoubleParameterArrayOut"] = t.struct(
        {
            "doubleValues": t.array(t.number()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoDoubleParameterArrayOut"])
    types["GoogleCloudConnectorsV1ConfigVariableIn"] = t.struct(
        {
            "stringValue": t.string().optional(),
            "secretValue": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
            "intValue": t.string().optional(),
            "key": t.string().optional(),
            "boolValue": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1ConfigVariableIn"])
    types["GoogleCloudConnectorsV1ConfigVariableOut"] = t.struct(
        {
            "stringValue": t.string().optional(),
            "secretValue": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "intValue": t.string().optional(),
            "key": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1ConfigVariableOut"])
    types["EnterpriseCrmEventbusProtoConnectorsConnectionIn"] = t.struct(
        {
            "connectionName": t.string().optional(),
            "serviceName": t.string().optional(),
            "connectorVersion": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoConnectorsConnectionIn"])
    types["EnterpriseCrmEventbusProtoConnectorsConnectionOut"] = t.struct(
        {
            "connectionName": t.string().optional(),
            "serviceName": t.string().optional(),
            "connectorVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoConnectorsConnectionOut"])
    types["EnterpriseCrmEventbusProtoEventExecutionDetailsIn"] = t.struct(
        {
            "eventExecutionSnapshot": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoEventExecutionSnapshotIn"])
            ),
            "logFilePath": t.string().optional(),
            "nextExecutionTime": t.string().optional(),
            "ryeLockUnheldCount": t.integer().optional(),
            "networkAddress": t.string().optional(),
            "eventRetriesFromBeginningCount": t.integer().optional(),
            "eventExecutionState": t.string(),
            "eventAttemptStats": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsIn"
                    ]
                )
            ),
        }
    ).named(renames["EnterpriseCrmEventbusProtoEventExecutionDetailsIn"])
    types["EnterpriseCrmEventbusProtoEventExecutionDetailsOut"] = t.struct(
        {
            "eventExecutionSnapshot": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoEventExecutionSnapshotOut"])
            ),
            "logFilePath": t.string().optional(),
            "nextExecutionTime": t.string().optional(),
            "ryeLockUnheldCount": t.integer().optional(),
            "networkAddress": t.string().optional(),
            "eventRetriesFromBeginningCount": t.integer().optional(),
            "eventExecutionState": t.string(),
            "eventAttemptStats": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsOut"
                    ]
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoEventExecutionDetailsOut"])
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
    types["GoogleCloudConnectorsV1AuthConfigIn"] = t.struct(
        {
            "sshPublicKey": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigSshPublicKeyIn"]
            ).optional(),
            "userPassword": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigUserPasswordIn"]
            ).optional(),
            "additionalVariables": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConfigVariableIn"])
            ).optional(),
            "oauth2JwtBearer": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerIn"]
            ).optional(),
            "oauth2ClientCredentials": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsIn"]
            ).optional(),
            "authKey": t.string().optional(),
            "oauth2AuthCodeFlow": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowIn"]
            ).optional(),
            "authType": t.string().optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigIn"])
    types["GoogleCloudConnectorsV1AuthConfigOut"] = t.struct(
        {
            "sshPublicKey": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigSshPublicKeyOut"]
            ).optional(),
            "userPassword": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigUserPasswordOut"]
            ).optional(),
            "additionalVariables": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConfigVariableOut"])
            ).optional(),
            "oauth2JwtBearer": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerOut"]
            ).optional(),
            "oauth2ClientCredentials": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsOut"]
            ).optional(),
            "authKey": t.string().optional(),
            "oauth2AuthCodeFlow": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowOut"]
            ).optional(),
            "authType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigOut"])
    types["GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsIn"] = t.struct(
        {
            "clientId": t.string().optional(),
            "clientSecret": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsIn"])
    types["GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsOut"] = t.struct(
        {
            "clientId": t.string().optional(),
            "clientSecret": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsOut"])
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
    types["GoogleCloudIntegrationsV1alphaBooleanParameterArrayIn"] = t.struct(
        {"booleanValues": t.array(t.boolean()).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaBooleanParameterArrayIn"])
    types["GoogleCloudIntegrationsV1alphaBooleanParameterArrayOut"] = t.struct(
        {
            "booleanValues": t.array(t.boolean()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaBooleanParameterArrayOut"])
    types["GoogleCloudIntegrationsV1alphaAuthConfigIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "state": t.string().optional(),
            "encryptedCredential": t.string().optional(),
            "lastModifierEmail": t.string().optional(),
            "validTime": t.string().optional(),
            "expiryNotificationDuration": t.array(t.string()).optional(),
            "reason": t.string().optional(),
            "overrideValidTime": t.string().optional(),
            "credentialType": t.string().optional(),
            "visibility": t.string().optional(),
            "description": t.string().optional(),
            "creatorEmail": t.string().optional(),
            "decryptedCredential": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCredentialIn"]
            ).optional(),
            "name": t.string().optional(),
            "certificateId": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaAuthConfigIn"])
    types["GoogleCloudIntegrationsV1alphaAuthConfigOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "state": t.string().optional(),
            "encryptedCredential": t.string().optional(),
            "lastModifierEmail": t.string().optional(),
            "validTime": t.string().optional(),
            "expiryNotificationDuration": t.array(t.string()).optional(),
            "reason": t.string().optional(),
            "overrideValidTime": t.string().optional(),
            "credentialType": t.string().optional(),
            "visibility": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "creatorEmail": t.string().optional(),
            "decryptedCredential": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCredentialOut"]
            ).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "certificateId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaAuthConfigOut"])
    types[
        "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataIn"
    ] = t.struct(
        {
            "taskName": t.string().optional(),
            "taskLabel": t.string().optional(),
            "taskAttemptNum": t.integer().optional(),
            "eventAttemptNum": t.integer().optional(),
            "taskNumber": t.string().optional(),
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
            "taskName": t.string().optional(),
            "taskLabel": t.string().optional(),
            "taskAttemptNum": t.integer().optional(),
            "eventAttemptNum": t.integer().optional(),
            "taskNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataOut"
        ]
    )
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
    types["EnterpriseCrmEventbusProtoStringParameterArrayIn"] = t.struct(
        {"stringValues": t.array(t.string())}
    ).named(renames["EnterpriseCrmEventbusProtoStringParameterArrayIn"])
    types["EnterpriseCrmEventbusProtoStringParameterArrayOut"] = t.struct(
        {
            "stringValues": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoStringParameterArrayOut"])
    types["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIn"] = t.struct(
        {
            "stringRegex": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexIn"
                ]
            ),
            "doubleRange": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeIn"
                ]
            ),
            "intRange": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeIn"
                ]
            ),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIn"])
    types["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleOut"] = t.struct(
        {
            "stringRegex": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexOut"
                ]
            ),
            "doubleRange": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeOut"
                ]
            ),
            "intRange": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeOut"
                ]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleOut"])
    types["EnterpriseCrmEventbusProtoErrorDetailIn"] = t.struct(
        {
            "taskNumber": t.integer().optional(),
            "errorCode": t.proxy(renames["CrmlogErrorCodeIn"]).optional(),
            "errorMessage": t.string().optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoErrorDetailIn"])
    types["EnterpriseCrmEventbusProtoErrorDetailOut"] = t.struct(
        {
            "taskNumber": t.integer().optional(),
            "errorCode": t.proxy(renames["CrmlogErrorCodeOut"]).optional(),
            "errorMessage": t.string().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoErrorDetailOut"])
    types["EnterpriseCrmEventbusProtoCloudSchedulerConfigIn"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "serviceAccountEmail": t.string(),
            "location": t.string(),
            "cronTab": t.string(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoCloudSchedulerConfigIn"])
    types["EnterpriseCrmEventbusProtoCloudSchedulerConfigOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "serviceAccountEmail": t.string(),
            "location": t.string(),
            "cronTab": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoCloudSchedulerConfigOut"])
    types["GoogleCloudIntegrationsV1alphaDoubleParameterArrayIn"] = t.struct(
        {"doubleValues": t.array(t.number()).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaDoubleParameterArrayIn"])
    types["GoogleCloudIntegrationsV1alphaDoubleParameterArrayOut"] = t.struct(
        {
            "doubleValues": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaDoubleParameterArrayOut"])
    types["GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestIn"] = t.struct(
        {
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersIn"]
            ).optional(),
            "parameterEntries": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"])
            ).optional(),
            "requestId": t.string().optional(),
            "triggerId": t.string().optional(),
            "scheduleTime": t.string().optional(),
            "inputParameters": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestIn"])
    types["GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestOut"] = t.struct(
        {
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersOut"]
            ).optional(),
            "parameterEntries": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"])
            ).optional(),
            "requestId": t.string().optional(),
            "triggerId": t.string().optional(),
            "scheduleTime": t.string().optional(),
            "inputParameters": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestOut"])
    types["EnterpriseCrmEventbusProtoBooleanParameterArrayIn"] = t.struct(
        {"booleanValues": t.array(t.boolean())}
    ).named(renames["EnterpriseCrmEventbusProtoBooleanParameterArrayIn"])
    types["EnterpriseCrmEventbusProtoBooleanParameterArrayOut"] = t.struct(
        {
            "booleanValues": t.array(t.boolean()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBooleanParameterArrayOut"])
    types["GoogleCloudIntegrationsV1alphaSuccessPolicyIn"] = t.struct(
        {"finalState": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaSuccessPolicyIn"])
    types["GoogleCloudIntegrationsV1alphaSuccessPolicyOut"] = t.struct(
        {
            "finalState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSuccessPolicyOut"])
    types["GoogleCloudIntegrationsV1alphaCloudSchedulerConfigIn"] = t.struct(
        {
            "serviceAccountEmail": t.string(),
            "cronTab": t.string(),
            "errorMessage": t.string().optional(),
            "location": t.string(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCloudSchedulerConfigIn"])
    types["GoogleCloudIntegrationsV1alphaCloudSchedulerConfigOut"] = t.struct(
        {
            "serviceAccountEmail": t.string(),
            "cronTab": t.string(),
            "errorMessage": t.string().optional(),
            "location": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCloudSchedulerConfigOut"])
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
    types[
        "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityIn"
    ] = t.struct({"emailAddress": t.string(), "gaiaId": t.string()}).named(
        renames["EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityIn"]
    )
    types[
        "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityOut"
    ] = t.struct(
        {
            "emailAddress": t.string(),
            "gaiaId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityOut"]
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
    types["EnterpriseCrmLoggingGwsSanitizeOptionsIn"] = t.struct(
        {
            "logType": t.array(t.string()).optional(),
            "isAlreadySanitized": t.boolean().optional(),
            "sanitizeType": t.string(),
            "privacy": t.string(),
        }
    ).named(renames["EnterpriseCrmLoggingGwsSanitizeOptionsIn"])
    types["EnterpriseCrmLoggingGwsSanitizeOptionsOut"] = t.struct(
        {
            "logType": t.array(t.string()).optional(),
            "isAlreadySanitized": t.boolean().optional(),
            "sanitizeType": t.string(),
            "privacy": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmLoggingGwsSanitizeOptionsOut"])
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
    types["GoogleCloudIntegrationsV1alphaSuspensionAuditIn"] = t.struct(
        {"resolveTime": t.string().optional(), "resolver": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaSuspensionAuditIn"])
    types["GoogleCloudIntegrationsV1alphaSuspensionAuditOut"] = t.struct(
        {
            "resolveTime": t.string().optional(),
            "resolver": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSuspensionAuditOut"])
    types["EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayIn"] = t.struct(
        {"booleanValues": t.array(t.boolean())}
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayIn"])
    types["EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayOut"] = t.struct(
        {
            "booleanValues": t.array(t.boolean()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayOut"])
    types["GoogleCloudConnectorsV1ConnectionIn"] = t.struct(
        {
            "sslConfig": t.proxy(
                renames["GoogleCloudConnectorsV1SslConfigIn"]
            ).optional(),
            "logConfig": t.proxy(
                renames["GoogleCloudConnectorsV1LogConfigIn"]
            ).optional(),
            "serviceAccount": t.string().optional(),
            "nodeConfig": t.proxy(
                renames["GoogleCloudConnectorsV1NodeConfigIn"]
            ).optional(),
            "authConfig": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigIn"]
            ).optional(),
            "destinationConfigs": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1DestinationConfigIn"])
            ).optional(),
            "suspended": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "configVariables": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConfigVariableIn"])
            ).optional(),
            "connectorVersion": t.string(),
            "lockConfig": t.proxy(
                renames["GoogleCloudConnectorsV1LockConfigIn"]
            ).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1ConnectionIn"])
    types["GoogleCloudConnectorsV1ConnectionOut"] = t.struct(
        {
            "sslConfig": t.proxy(
                renames["GoogleCloudConnectorsV1SslConfigOut"]
            ).optional(),
            "status": t.proxy(
                renames["GoogleCloudConnectorsV1ConnectionStatusOut"]
            ).optional(),
            "logConfig": t.proxy(
                renames["GoogleCloudConnectorsV1LogConfigOut"]
            ).optional(),
            "serviceAccount": t.string().optional(),
            "createTime": t.string().optional(),
            "nodeConfig": t.proxy(
                renames["GoogleCloudConnectorsV1NodeConfigOut"]
            ).optional(),
            "connectorVersionLaunchStage": t.string().optional(),
            "subscriptionType": t.string().optional(),
            "authConfig": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOut"]
            ).optional(),
            "destinationConfigs": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1DestinationConfigOut"])
            ).optional(),
            "suspended": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "envoyImageLocation": t.string().optional(),
            "configVariables": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConfigVariableOut"])
            ).optional(),
            "serviceDirectory": t.string().optional(),
            "imageLocation": t.string().optional(),
            "connectorVersion": t.string(),
            "lockConfig": t.proxy(
                renames["GoogleCloudConnectorsV1LockConfigOut"]
            ).optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1ConnectionOut"])
    types["EnterpriseCrmEventbusProtoNodeIdentifierIn"] = t.struct(
        {
            "elementType": t.string().optional(),
            "elementIdentifier": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoNodeIdentifierIn"])
    types["EnterpriseCrmEventbusProtoNodeIdentifierOut"] = t.struct(
        {
            "elementType": t.string().optional(),
            "elementIdentifier": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoNodeIdentifierOut"])
    types["GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsIn"] = t.struct(
        {
            "clientId": t.string().optional(),
            "clientSecret": t.string().optional(),
            "accessToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAccessTokenIn"]
            ).optional(),
            "requestType": t.string().optional(),
            "tokenParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapIn"]
            ).optional(),
            "tokenEndpoint": t.string().optional(),
            "scope": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsIn"])
    types["GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsOut"] = t.struct(
        {
            "clientId": t.string().optional(),
            "clientSecret": t.string().optional(),
            "accessToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAccessTokenOut"]
            ).optional(),
            "requestType": t.string().optional(),
            "tokenParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapOut"]
            ).optional(),
            "tokenEndpoint": t.string().optional(),
            "scope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsOut"])
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
    types["GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseIn"] = t.struct(
        {
            "integrationVersions": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "noPermission": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseIn"])
    types[
        "GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseOut"
    ] = t.struct(
        {
            "integrationVersions": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "noPermission": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseOut"]
    )
    types["GoogleCloudIntegrationsV1alphaGenerateTokenResponseIn"] = t.struct(
        {"message": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaGenerateTokenResponseIn"])
    types["GoogleCloudIntegrationsV1alphaGenerateTokenResponseOut"] = t.struct(
        {
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaGenerateTokenResponseOut"])
    types["EnterpriseCrmEventbusProtoProtoParameterArrayIn"] = t.struct(
        {"protoValues": t.array(t.struct({"_": t.string().optional()}))}
    ).named(renames["EnterpriseCrmEventbusProtoProtoParameterArrayIn"])
    types["EnterpriseCrmEventbusProtoProtoParameterArrayOut"] = t.struct(
        {
            "protoValues": t.array(t.struct({"_": t.string().optional()})),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoProtoParameterArrayOut"])
    types["GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionIn"] = t.struct(
        {
            "triggerConfigs": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn"])
            ).optional(),
            "description": t.string().optional(),
            "userLabel": t.string().optional(),
            "errorCatcherConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn"])
            ).optional(),
            "lastModifierEmail": t.string().optional(),
            "teardown": t.proxy(
                renames["EnterpriseCrmEventbusProtoTeardownIn"]
            ).optional(),
            "parentIntegrationVersionId": t.string().optional(),
            "taskConfigs": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigIn"])
            ).optional(),
            "databasePersistencePolicy": t.string().optional(),
            "templateParameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn"]
            ).optional(),
            "status": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionIn"])
    types["GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionOut"] = t.struct(
        {
            "triggerConfigs": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigOut"])
            ).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "userLabel": t.string().optional(),
            "updateTime": t.string().optional(),
            "errorCatcherConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigOut"])
            ).optional(),
            "lastModifierEmail": t.string().optional(),
            "teardown": t.proxy(
                renames["EnterpriseCrmEventbusProtoTeardownOut"]
            ).optional(),
            "parentIntegrationVersionId": t.string().optional(),
            "snapshotNumber": t.string().optional(),
            "taskConfigs": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigOut"])
            ).optional(),
            "databasePersistencePolicy": t.string().optional(),
            "templateParameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersOut"]
            ).optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionOut"])
    types["GoogleCloudIntegrationsV1alphaExecutionIn"] = t.struct(
        {
            "name": t.string().optional(),
            "triggerId": t.string().optional(),
            "directSubExecutions": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaExecutionIn"])
            ).optional(),
            "eventExecutionDetails": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventExecutionDetailsIn"]
            ).optional(),
            "responseParameters": t.struct({"_": t.string().optional()}).optional(),
            "responseParams": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"])
            ).optional(),
            "executionMethod": t.string().optional(),
            "requestParams": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"])
            ).optional(),
            "requestParameters": t.struct({"_": t.string().optional()}).optional(),
            "executionDetails": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaExecutionDetailsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecutionIn"])
    types["GoogleCloudIntegrationsV1alphaExecutionOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "triggerId": t.string().optional(),
            "directSubExecutions": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaExecutionOut"])
            ).optional(),
            "eventExecutionDetails": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventExecutionDetailsOut"]
            ).optional(),
            "responseParameters": t.struct({"_": t.string().optional()}).optional(),
            "responseParams": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"])
            ).optional(),
            "executionMethod": t.string().optional(),
            "requestParams": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"])
            ).optional(),
            "requestParameters": t.struct({"_": t.string().optional()}).optional(),
            "executionDetails": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaExecutionDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecutionOut"])
    types["GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequestIn"] = t.struct(
        {
            "authConfigId": t.string().optional(),
            "appsScriptProject": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequestIn"])
    types["GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequestOut"] = t.struct(
        {
            "authConfigId": t.string().optional(),
            "appsScriptProject": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequestOut"])
    types["EnterpriseCrmFrontendsEventbusProtoTaskConfigIn"] = t.struct(
        {
            "preconditionLabel": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "taskType": t.string().optional(),
            "position": t.proxy(
                renames["EnterpriseCrmEventbusProtoCoordinateIn"]
            ).optional(),
            "taskTemplateName": t.string().optional(),
            "taskName": t.string().optional(),
            "creatorEmail": t.string().optional(),
            "nextTasks": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoNextTaskIn"])
            ).optional(),
            "errorCatcherId": t.string().optional(),
            "rollbackStrategy": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoRollbackStrategyIn"]
            ).optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "externalTaskType": t.string(),
            "taskEntity": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoTaskEntityIn"]
            ).optional(),
            "createTime": t.string().optional(),
            "taskExecutionStrategy": t.string().optional(),
            "successPolicy": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuccessPolicyIn"]
            ).optional(),
            "failurePolicy": t.proxy(
                renames["EnterpriseCrmEventbusProtoFailurePolicyIn"]
            ).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "taskSpec": t.string().optional(),
            "disableStrictTypeValidation": t.boolean().optional(),
            "synchronousCallFailurePolicy": t.proxy(
                renames["EnterpriseCrmEventbusProtoFailurePolicyIn"]
            ).optional(),
            "alertConfigs": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskAlertConfigIn"])
            ).optional(),
            "label": t.string().optional(),
            "taskNumber": t.string().optional(),
            "description": t.string().optional(),
            "jsonValidationOption": t.string().optional(),
            "precondition": t.string().optional(),
            "incomingEdgeCount": t.integer().optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigIn"])
    types["EnterpriseCrmFrontendsEventbusProtoTaskConfigOut"] = t.struct(
        {
            "preconditionLabel": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "taskType": t.string().optional(),
            "position": t.proxy(
                renames["EnterpriseCrmEventbusProtoCoordinateOut"]
            ).optional(),
            "taskTemplateName": t.string().optional(),
            "taskName": t.string().optional(),
            "creatorEmail": t.string().optional(),
            "nextTasks": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoNextTaskOut"])
            ).optional(),
            "errorCatcherId": t.string().optional(),
            "rollbackStrategy": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoRollbackStrategyOut"]
            ).optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "externalTaskType": t.string(),
            "taskEntity": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoTaskEntityOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "taskExecutionStrategy": t.string().optional(),
            "successPolicy": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuccessPolicyOut"]
            ).optional(),
            "failurePolicy": t.proxy(
                renames["EnterpriseCrmEventbusProtoFailurePolicyOut"]
            ).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "taskSpec": t.string().optional(),
            "disableStrictTypeValidation": t.boolean().optional(),
            "synchronousCallFailurePolicy": t.proxy(
                renames["EnterpriseCrmEventbusProtoFailurePolicyOut"]
            ).optional(),
            "alertConfigs": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskAlertConfigOut"])
            ).optional(),
            "label": t.string().optional(),
            "taskNumber": t.string().optional(),
            "description": t.string().optional(),
            "jsonValidationOption": t.string().optional(),
            "precondition": t.string().optional(),
            "incomingEdgeCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigOut"])
    types["GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseIn"] = t.struct(
        {"executionInfoIds": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseIn"])
    types["GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseOut"] = t.struct(
        {
            "executionInfoIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseOut"])
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
    types["EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayIn"] = t.struct(
        {"protoValues": t.array(t.struct({"_": t.string().optional()}))}
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayIn"])
    types["EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayOut"] = t.struct(
        {
            "protoValues": t.array(t.struct({"_": t.string().optional()})),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayOut"])
    types["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn"] = t.struct(
        {"filterType": t.string(), "enumStrings": t.array(t.string())}
    ).named(renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn"])
    types["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut"] = t.struct(
        {
            "filterType": t.string(),
            "enumStrings": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut"])
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
    types["GoogleCloudConnectorsV1SslConfigIn"] = t.struct(
        {
            "clientPrivateKeyPass": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
            "privateServerCertificate": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
            "clientPrivateKey": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
            "type": t.string().optional(),
            "useSsl": t.boolean().optional(),
            "trustModel": t.string().optional(),
            "additionalVariables": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConfigVariableIn"])
            ).optional(),
            "clientCertType": t.string().optional(),
            "serverCertType": t.string().optional(),
            "clientCertificate": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1SslConfigIn"])
    types["GoogleCloudConnectorsV1SslConfigOut"] = t.struct(
        {
            "clientPrivateKeyPass": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "privateServerCertificate": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "clientPrivateKey": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "type": t.string().optional(),
            "useSsl": t.boolean().optional(),
            "trustModel": t.string().optional(),
            "additionalVariables": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConfigVariableOut"])
            ).optional(),
            "clientCertType": t.string().optional(),
            "serverCertType": t.string().optional(),
            "clientCertificate": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1SslConfigOut"])
    types["EnterpriseCrmFrontendsEventbusProtoIntParameterArrayIn"] = t.struct(
        {"intValues": t.array(t.string())}
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoIntParameterArrayIn"])
    types["EnterpriseCrmFrontendsEventbusProtoIntParameterArrayOut"] = t.struct(
        {
            "intValues": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoIntParameterArrayOut"])
    types["EnterpriseCrmEventbusProtoExternalTrafficIn"] = t.struct(
        {
            "gcpProjectNumber": t.string().optional(),
            "source": t.string().optional(),
            "gcpProjectId": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoExternalTrafficIn"])
    types["EnterpriseCrmEventbusProtoExternalTrafficOut"] = t.struct(
        {
            "gcpProjectNumber": t.string().optional(),
            "source": t.string().optional(),
            "gcpProjectId": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoExternalTrafficOut"])
    types["GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsIn"] = t.struct(
        {
            "accessToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAccessTokenIn"]
            ).optional(),
            "clientSecret": t.string().optional(),
            "clientId": t.string().optional(),
            "tokenEndpoint": t.string().optional(),
            "requestType": t.string().optional(),
            "scope": t.string().optional(),
            "password": t.string().optional(),
            "tokenParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapIn"]
            ).optional(),
            "username": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsIn"])
    types["GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsOut"] = t.struct(
        {
            "accessToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAccessTokenOut"]
            ).optional(),
            "clientSecret": t.string().optional(),
            "clientId": t.string().optional(),
            "tokenEndpoint": t.string().optional(),
            "requestType": t.string().optional(),
            "scope": t.string().optional(),
            "password": t.string().optional(),
            "tokenParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapOut"]
            ).optional(),
            "username": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsOut"])
    types["GoogleCloudIntegrationsV1alphaListAuthConfigsResponseIn"] = t.struct(
        {
            "authConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaAuthConfigIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListAuthConfigsResponseIn"])
    types["GoogleCloudIntegrationsV1alphaListAuthConfigsResponseOut"] = t.struct(
        {
            "authConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaAuthConfigOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListAuthConfigsResponseOut"])
    types["GoogleCloudIntegrationsV1alphaSfdcChannelIn"] = t.struct(
        {
            "lastReplayId": t.string().optional(),
            "channelTopic": t.string().optional(),
            "isActive": t.boolean().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSfdcChannelIn"])
    types["GoogleCloudIntegrationsV1alphaSfdcChannelOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "lastReplayId": t.string().optional(),
            "channelTopic": t.string().optional(),
            "isActive": t.boolean().optional(),
            "deleteTime": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"])
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
    types["GoogleCloudIntegrationsV1alphaClientCertificateIn"] = t.struct(
        {
            "encryptedPrivateKey": t.string().optional(),
            "passphrase": t.string().optional(),
            "sslCertificate": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaClientCertificateIn"])
    types["GoogleCloudIntegrationsV1alphaClientCertificateOut"] = t.struct(
        {
            "encryptedPrivateKey": t.string().optional(),
            "passphrase": t.string().optional(),
            "sslCertificate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaClientCertificateOut"])
    types["EnterpriseCrmEventbusProtoParamSpecEntryConfigIn"] = t.struct(
        {
            "hideDefaultValue": t.boolean().optional(),
            "subSectionLabel": t.string().optional(),
            "parameterNameOption": t.string(),
            "inputDisplayOption": t.string(),
            "label": t.string().optional(),
            "uiPlaceholderText": t.string().optional(),
            "isHidden": t.boolean().optional(),
            "helpText": t.string().optional(),
            "descriptivePhrase": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParamSpecEntryConfigIn"])
    types["EnterpriseCrmEventbusProtoParamSpecEntryConfigOut"] = t.struct(
        {
            "hideDefaultValue": t.boolean().optional(),
            "subSectionLabel": t.string().optional(),
            "parameterNameOption": t.string(),
            "inputDisplayOption": t.string(),
            "label": t.string().optional(),
            "uiPlaceholderText": t.string().optional(),
            "isHidden": t.boolean().optional(),
            "helpText": t.string().optional(),
            "descriptivePhrase": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParamSpecEntryConfigOut"])
    types["EnterpriseCrmEventbusProtoScatterResponseIn"] = t.struct(
        {
            "scatterElement": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeIn"]
            ).optional(),
            "isSuccessful": t.boolean().optional(),
            "executionIds": t.array(t.string()).optional(),
            "responseParams": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoParameterEntryIn"])
            ).optional(),
            "errorMsg": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoScatterResponseIn"])
    types["EnterpriseCrmEventbusProtoScatterResponseOut"] = t.struct(
        {
            "scatterElement": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "isSuccessful": t.boolean().optional(),
            "executionIds": t.array(t.string()).optional(),
            "responseParams": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoParameterEntryOut"])
            ).optional(),
            "errorMsg": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoScatterResponseOut"])
    types["GoogleCloudIntegrationsV1alphaParameterMapEntryIn"] = t.struct(
        {
            "value": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapFieldIn"]
            ).optional(),
            "key": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapFieldIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaParameterMapEntryIn"])
    types["GoogleCloudIntegrationsV1alphaParameterMapEntryOut"] = t.struct(
        {
            "value": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapFieldOut"]
            ).optional(),
            "key": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapFieldOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaParameterMapEntryOut"])
    types["GoogleCloudIntegrationsV1alphaIntegrationVersionIn"] = t.struct(
        {
            "runAsServiceAccount": t.string().optional(),
            "errorCatcherConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn"])
            ).optional(),
            "snapshotNumber": t.string().optional(),
            "teardown": t.proxy(
                renames["EnterpriseCrmEventbusProtoTeardownIn"]
            ).optional(),
            "triggerConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaTriggerConfigIn"])
            ).optional(),
            "parentTemplateId": t.string().optional(),
            "databasePersistencePolicy": t.string().optional(),
            "userLabel": t.string().optional(),
            "integrationParameters": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationParameterIn"])
            ).optional(),
            "taskConfigsInternal": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigIn"])
            ).optional(),
            "lockHolder": t.string().optional(),
            "origin": t.string().optional(),
            "triggerConfigsInternal": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn"])
            ).optional(),
            "description": t.string().optional(),
            "lastModifierEmail": t.string().optional(),
            "integrationParametersInternal": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn"]
            ).optional(),
            "taskConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaTaskConfigIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionIn"])
    types["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"] = t.struct(
        {
            "runAsServiceAccount": t.string().optional(),
            "errorCatcherConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigOut"])
            ).optional(),
            "status": t.string().optional(),
            "state": t.string().optional(),
            "snapshotNumber": t.string().optional(),
            "teardown": t.proxy(
                renames["EnterpriseCrmEventbusProtoTeardownOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "triggerConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaTriggerConfigOut"])
            ).optional(),
            "createTime": t.string().optional(),
            "parentTemplateId": t.string().optional(),
            "databasePersistencePolicy": t.string().optional(),
            "userLabel": t.string().optional(),
            "integrationParameters": t.array(
                t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaIntegrationParameterOut"]
                )
            ).optional(),
            "taskConfigsInternal": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigOut"])
            ).optional(),
            "lockHolder": t.string().optional(),
            "origin": t.string().optional(),
            "triggerConfigsInternal": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigOut"])
            ).optional(),
            "description": t.string().optional(),
            "lastModifierEmail": t.string().optional(),
            "integrationParametersInternal": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersOut"]
            ).optional(),
            "taskConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaTaskConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterMapFieldIn"] = t.struct(
        {
            "literalValue": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn"]
            ).optional(),
            "referenceKey": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterMapFieldIn"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterMapFieldOut"] = t.struct(
        {
            "literalValue": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "referenceKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterMapFieldOut"])
    types["EnterpriseCrmEventbusProtoNotificationIn"] = t.struct(
        {
            "escalatorQueue": t.string(),
            "buganizerNotification": t.proxy(
                renames["EnterpriseCrmEventbusProtoBuganizerNotificationIn"]
            ),
            "pubsubTopic": t.string(),
            "request": t.proxy(
                renames["EnterpriseCrmEventbusProtoCustomSuspensionRequestIn"]
            ).optional(),
            "emailAddress": t.proxy(renames["EnterpriseCrmEventbusProtoAddressIn"]),
        }
    ).named(renames["EnterpriseCrmEventbusProtoNotificationIn"])
    types["EnterpriseCrmEventbusProtoNotificationOut"] = t.struct(
        {
            "escalatorQueue": t.string(),
            "buganizerNotification": t.proxy(
                renames["EnterpriseCrmEventbusProtoBuganizerNotificationOut"]
            ),
            "pubsubTopic": t.string(),
            "request": t.proxy(
                renames["EnterpriseCrmEventbusProtoCustomSuspensionRequestOut"]
            ).optional(),
            "emailAddress": t.proxy(renames["EnterpriseCrmEventbusProtoAddressOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoNotificationOut"])
    types["EnterpriseCrmEventbusProtoParameterMapEntryIn"] = t.struct(
        {
            "key": t.proxy(renames["EnterpriseCrmEventbusProtoParameterMapFieldIn"]),
            "value": t.proxy(renames["EnterpriseCrmEventbusProtoParameterMapFieldIn"]),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParameterMapEntryIn"])
    types["EnterpriseCrmEventbusProtoParameterMapEntryOut"] = t.struct(
        {
            "key": t.proxy(renames["EnterpriseCrmEventbusProtoParameterMapFieldOut"]),
            "value": t.proxy(renames["EnterpriseCrmEventbusProtoParameterMapFieldOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParameterMapEntryOut"])
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
    types["GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "sfdcChannels": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcChannelIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseIn"])
    types["GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "sfdcChannels": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseOut"])
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
    types["EnterpriseCrmEventbusProtoFieldIn"] = t.struct(
        {
            "referenceKey": t.string().optional(),
            "protoDefPath": t.string().optional(),
            "fieldType": t.string().optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeIn"]
            ).optional(),
            "transformExpression": t.proxy(
                renames["EnterpriseCrmEventbusProtoTransformExpressionIn"]
            ).optional(),
            "cardinality": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFieldIn"])
    types["EnterpriseCrmEventbusProtoFieldOut"] = t.struct(
        {
            "referenceKey": t.string().optional(),
            "protoDefPath": t.string().optional(),
            "fieldType": t.string().optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "transformExpression": t.proxy(
                renames["EnterpriseCrmEventbusProtoTransformExpressionOut"]
            ).optional(),
            "cardinality": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFieldOut"])
    types["EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsIn"] = t.struct(
        {
            "ryeLockUnheldCount": t.integer().optional(),
            "eventExecutionState": t.string().optional(),
            "nextExecutionTime": t.string().optional(),
            "logFilePath": t.string().optional(),
            "eventAttemptStats": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsIn"
                    ]
                )
            ),
            "networkAddress": t.string().optional(),
            "eventExecutionSnapshot": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotIn"
                    ]
                )
            ).optional(),
            "eventRetriesFromBeginningCount": t.integer().optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsIn"])
    types["EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsOut"] = t.struct(
        {
            "ryeLockUnheldCount": t.integer().optional(),
            "eventExecutionState": t.string().optional(),
            "nextExecutionTime": t.string().optional(),
            "logFilePath": t.string().optional(),
            "eventAttemptStats": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsOut"
                    ]
                )
            ),
            "networkAddress": t.string().optional(),
            "eventExecutionSnapshot": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotOut"
                    ]
                )
            ).optional(),
            "eventRetriesFromBeginningCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsOut"])
    types["GoogleCloudIntegrationsV1alphaAuthTokenIn"] = t.struct(
        {"type": t.string().optional(), "token": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaAuthTokenIn"])
    types["GoogleCloudIntegrationsV1alphaAuthTokenOut"] = t.struct(
        {
            "type": t.string().optional(),
            "token": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaAuthTokenOut"])
    types["EnterpriseCrmEventbusProtoCustomSuspensionRequestIn"] = t.struct(
        {
            "suspensionInfoEventParameterKey": t.string().optional(),
            "postToQueueWithTriggerIdRequest": t.proxy(
                renames[
                    "GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestIn"
                ]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoCustomSuspensionRequestIn"])
    types["EnterpriseCrmEventbusProtoCustomSuspensionRequestOut"] = t.struct(
        {
            "suspensionInfoEventParameterKey": t.string().optional(),
            "postToQueueWithTriggerIdRequest": t.proxy(
                renames[
                    "GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoCustomSuspensionRequestOut"])
    types["EnterpriseCrmEventbusProtoProtoFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoProtoFunctionIn"])
    types["EnterpriseCrmEventbusProtoProtoFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoProtoFunctionOut"])
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
    types["EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoIn"] = t.struct(
        {
            "workflowName": t.string().optional(),
            "postMethod": t.string().optional(),
            "executionTraceInfo": t.proxy(
                renames["EnterpriseCrmEventbusProtoExecutionTraceInfoIn"]
            ).optional(),
            "requestParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
            ).optional(),
            "snapshotNumber": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "workflowId": t.string(),
            "workflowRetryBackoffIntervalSeconds": t.string().optional(),
            "tenant": t.string().optional(),
            "responseParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
            ).optional(),
            "triggerId": t.string().optional(),
            "errors": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoErrorDetailIn"])
            ).optional(),
            "errorCode": t.proxy(renames["CrmlogErrorCodeIn"]).optional(),
            "requestId": t.string().optional(),
            "clientId": t.string().optional(),
            "eventExecutionInfoId": t.string().optional(),
            "createTime": t.string().optional(),
            "product": t.string().optional(),
            "eventExecutionDetails": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoIn"])
    types["EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoOut"] = t.struct(
        {
            "workflowName": t.string().optional(),
            "postMethod": t.string().optional(),
            "executionTraceInfo": t.proxy(
                renames["EnterpriseCrmEventbusProtoExecutionTraceInfoOut"]
            ).optional(),
            "requestParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "snapshotNumber": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "workflowId": t.string(),
            "workflowRetryBackoffIntervalSeconds": t.string().optional(),
            "tenant": t.string().optional(),
            "responseParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "triggerId": t.string().optional(),
            "errors": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoErrorDetailOut"])
            ).optional(),
            "errorCode": t.proxy(renames["CrmlogErrorCodeOut"]).optional(),
            "requestId": t.string().optional(),
            "clientId": t.string().optional(),
            "eventExecutionInfoId": t.string().optional(),
            "createTime": t.string().optional(),
            "product": t.string().optional(),
            "eventExecutionDetails": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoOut"])
    types["EnterpriseCrmEventbusProtoBooleanArrayFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoBooleanArrayFunctionIn"])
    types["EnterpriseCrmEventbusProtoBooleanArrayFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBooleanArrayFunctionOut"])
    types["EnterpriseCrmEventbusProtoFailurePolicyIn"] = t.struct(
        {
            "retryStrategy": t.string().optional(),
            "maxNumRetries": t.integer(),
            "intervalInSeconds": t.string(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFailurePolicyIn"])
    types["EnterpriseCrmEventbusProtoFailurePolicyOut"] = t.struct(
        {
            "retryStrategy": t.string().optional(),
            "maxNumRetries": t.integer(),
            "intervalInSeconds": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFailurePolicyOut"])
    types["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigIn"] = t.struct(
        {
            "disableAlert": t.boolean().optional(),
            "metricType": t.string().optional(),
            "onlyFinalAttempt": t.boolean().optional(),
            "durationThreshold": t.string().optional(),
            "thresholdType": t.string().optional(),
            "displayName": t.string().optional(),
            "thresholdValue": t.proxy(
                renames[
                    "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueIn"
                ]
            ).optional(),
            "aggregationPeriod": t.string().optional(),
            "alertThreshold": t.integer().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigIn"])
    types["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigOut"] = t.struct(
        {
            "disableAlert": t.boolean().optional(),
            "metricType": t.string().optional(),
            "onlyFinalAttempt": t.boolean().optional(),
            "durationThreshold": t.string().optional(),
            "thresholdType": t.string().optional(),
            "displayName": t.string().optional(),
            "thresholdValue": t.proxy(
                renames[
                    "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueOut"
                ]
            ).optional(),
            "aggregationPeriod": t.string().optional(),
            "alertThreshold": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigOut"])
    types["GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseIn"] = t.struct(
        {
            "outputParameters": t.struct({"_": t.string().optional()}).optional(),
            "parameterEntries": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"])
            ).optional(),
            "executionId": t.string().optional(),
            "executionFailed": t.boolean().optional(),
            "eventParameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseIn"])
    types["GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseOut"] = t.struct(
        {
            "outputParameters": t.struct({"_": t.string().optional()}).optional(),
            "parameterEntries": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"])
            ).optional(),
            "executionId": t.string().optional(),
            "executionFailed": t.boolean().optional(),
            "eventParameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseOut"])
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
    types["EnterpriseCrmEventbusProtoSuspensionAuthPermissionsIn"] = t.struct(
        {
            "mdbGroup": t.string(),
            "loasRole": t.string(),
            "gaiaIdentity": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityIn"
                ]
            ).optional(),
            "googleGroup": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityIn"
                ]
            ),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionAuthPermissionsIn"])
    types["EnterpriseCrmEventbusProtoSuspensionAuthPermissionsOut"] = t.struct(
        {
            "mdbGroup": t.string(),
            "loasRole": t.string(),
            "gaiaIdentity": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityOut"
                ]
            ).optional(),
            "googleGroup": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityOut"
                ]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionAuthPermissionsOut"])
    types["EnterpriseCrmEventbusProtoFunctionIn"] = t.struct(
        {
            "parameters": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTransformExpressionIn"])
            ).optional(),
            "functionType": t.proxy(
                renames["EnterpriseCrmEventbusProtoFunctionTypeIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFunctionIn"])
    types["EnterpriseCrmEventbusProtoFunctionOut"] = t.struct(
        {
            "parameters": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTransformExpressionOut"])
            ).optional(),
            "functionType": t.proxy(
                renames["EnterpriseCrmEventbusProtoFunctionTypeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFunctionOut"])
    types["EnterpriseCrmEventbusProtoStringFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoStringFunctionIn"])
    types["EnterpriseCrmEventbusProtoStringFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoStringFunctionOut"])
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
    types["EnterpriseCrmFrontendsEventbusProtoRollbackStrategyIn"] = t.struct(
        {
            "rollbackTaskImplementationClassName": t.string(),
            "taskNumbersToRollback": t.array(t.string()),
            "parameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoRollbackStrategyIn"])
    types["EnterpriseCrmFrontendsEventbusProtoRollbackStrategyOut"] = t.struct(
        {
            "rollbackTaskImplementationClassName": t.string(),
            "taskNumbersToRollback": t.array(t.string()),
            "parameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoRollbackStrategyOut"])
    types["EnterpriseCrmEventbusProtoIntArrayFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoIntArrayFunctionIn"])
    types["EnterpriseCrmEventbusProtoIntArrayFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoIntArrayFunctionOut"])

    functions = {}
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
                "product": t.string().optional(),
                "redirectUri": t.string().optional(),
                "gcpProjectId": t.string().optional(),
                "state": t.string().optional(),
                "code": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaGenerateTokenResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesCreate"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "sfdcOrgId": t.string().optional(),
                "authConfigId": t.array(t.string()).optional(),
                "serviceAuthority": t.string().optional(),
                "displayName": t.string().optional(),
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
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "sfdcOrgId": t.string().optional(),
                "authConfigId": t.array(t.string()).optional(),
                "serviceAuthority": t.string().optional(),
                "displayName": t.string().optional(),
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
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "sfdcOrgId": t.string().optional(),
                "authConfigId": t.array(t.string()).optional(),
                "serviceAuthority": t.string().optional(),
                "displayName": t.string().optional(),
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
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "sfdcOrgId": t.string().optional(),
                "authConfigId": t.array(t.string()).optional(),
                "serviceAuthority": t.string().optional(),
                "displayName": t.string().optional(),
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
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "sfdcOrgId": t.string().optional(),
                "authConfigId": t.array(t.string()).optional(),
                "serviceAuthority": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesSfdcChannelsCreate"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesSfdcChannelsList"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesSfdcChannelsPatch"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesSfdcChannelsGet"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesSfdcChannelsDelete"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppsScriptProjectsLink"] = integrations.post(
        "v1alpha/{parent}/appsScriptProjects",
        t.struct(
            {
                "parent": t.string(),
                "authConfigId": t.string().optional(),
                "appsScriptProject": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppsScriptProjectsCreate"] = integrations.post(
        "v1alpha/{parent}/appsScriptProjects",
        t.struct(
            {
                "parent": t.string(),
                "authConfigId": t.string().optional(),
                "appsScriptProject": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthConfigsList"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaAuthConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthConfigsCreate"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaAuthConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthConfigsPatch"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaAuthConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthConfigsDelete"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaAuthConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthConfigsGet"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaAuthConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsDelete"] = integrations.post(
        "v1alpha/{name}:execute",
        t.struct(
            {
                "name": t.string(),
                "doNotPropagateError": t.boolean().optional(),
                "requestId": t.string().optional(),
                "parameterEntries": t.array(
                    t.proxy(
                        renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"]
                    )
                ).optional(),
                "inputParameters": t.struct({"_": t.string().optional()}).optional(),
                "triggerId": t.string(),
                "executionId": t.string().optional(),
                "parameters": t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsSchedule"] = integrations.post(
        "v1alpha/{name}:execute",
        t.struct(
            {
                "name": t.string(),
                "doNotPropagateError": t.boolean().optional(),
                "requestId": t.string().optional(),
                "parameterEntries": t.array(
                    t.proxy(
                        renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"]
                    )
                ).optional(),
                "inputParameters": t.struct({"_": t.string().optional()}).optional(),
                "triggerId": t.string(),
                "executionId": t.string().optional(),
                "parameters": t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsList"] = integrations.post(
        "v1alpha/{name}:execute",
        t.struct(
            {
                "name": t.string(),
                "doNotPropagateError": t.boolean().optional(),
                "requestId": t.string().optional(),
                "parameterEntries": t.array(
                    t.proxy(
                        renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"]
                    )
                ).optional(),
                "inputParameters": t.struct({"_": t.string().optional()}).optional(),
                "triggerId": t.string(),
                "executionId": t.string().optional(),
                "parameters": t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsExecute"] = integrations.post(
        "v1alpha/{name}:execute",
        t.struct(
            {
                "name": t.string(),
                "doNotPropagateError": t.boolean().optional(),
                "requestId": t.string().optional(),
                "parameterEntries": t.array(
                    t.proxy(
                        renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"]
                    )
                ).optional(),
                "inputParameters": t.struct({"_": t.string().optional()}).optional(),
                "triggerId": t.string(),
                "executionId": t.string().optional(),
                "parameters": t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsExecutionsList"] = integrations.get(
        "v1alpha/{parent}/executions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filterParams.parameterKey": t.string().optional(),
                "filterParams.parameterPairKey": t.string().optional(),
                "truncateParams": t.boolean().optional(),
                "filterParams.parameterPairValue": t.string().optional(),
                "filterParams.parameterValue": t.string().optional(),
                "filterParams.endTime": t.string().optional(),
                "filterParams.customFilter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filterParams.taskStatuses": t.string().optional(),
                "refreshAcl": t.boolean().optional(),
                "filterParams.parameterType": t.string().optional(),
                "filterParams.executionId": t.string().optional(),
                "filterParams.workflowName": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "filterParams.eventStatuses": t.string().optional(),
                "filterParams.startTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListExecutionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsIntegrationsExecutionsSuspensionsLift"
    ] = integrations.get(
        "v1alpha/{parent}/suspensions",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListSuspensionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsIntegrationsExecutionsSuspensionsResolve"
    ] = integrations.get(
        "v1alpha/{parent}/suspensions",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListSuspensionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsIntegrationsExecutionsSuspensionsList"
    ] = integrations.get(
        "v1alpha/{parent}/suspensions",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListSuspensionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsList"] = integrations.get(
        "v1alpha/{name}:download",
        t.struct(
            {
                "name": t.string(),
                "fileFormat": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsCreate"] = integrations.get(
        "v1alpha/{name}:download",
        t.struct(
            {
                "name": t.string(),
                "fileFormat": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsPublish"] = integrations.get(
        "v1alpha/{name}:download",
        t.struct(
            {
                "name": t.string(),
                "fileFormat": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsIntegrationsVersionsTakeoverEditLock"
    ] = integrations.get(
        "v1alpha/{name}:download",
        t.struct(
            {
                "name": t.string(),
                "fileFormat": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsPatch"] = integrations.get(
        "v1alpha/{name}:download",
        t.struct(
            {
                "name": t.string(),
                "fileFormat": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsGet"] = integrations.get(
        "v1alpha/{name}:download",
        t.struct(
            {
                "name": t.string(),
                "fileFormat": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsUnpublish"] = integrations.get(
        "v1alpha/{name}:download",
        t.struct(
            {
                "name": t.string(),
                "fileFormat": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsDelete"] = integrations.get(
        "v1alpha/{name}:download",
        t.struct(
            {
                "name": t.string(),
                "fileFormat": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsUpload"] = integrations.get(
        "v1alpha/{name}:download",
        t.struct(
            {
                "name": t.string(),
                "fileFormat": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsDownload"] = integrations.get(
        "v1alpha/{name}:download",
        t.struct(
            {
                "name": t.string(),
                "fileFormat": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsAuthConfigsGet"] = integrations.get(
        "v1alpha/{parent}/authConfigs",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListAuthConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsAuthConfigsCreate"] = integrations.get(
        "v1alpha/{parent}/authConfigs",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListAuthConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsAuthConfigsPatch"] = integrations.get(
        "v1alpha/{parent}/authConfigs",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListAuthConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsAuthConfigsDelete"] = integrations.get(
        "v1alpha/{parent}/authConfigs",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListAuthConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsAuthConfigsList"] = integrations.get(
        "v1alpha/{parent}/authConfigs",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListAuthConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsSchedule"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsExecute"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsList"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsDelete"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsExecutionsGet"] = integrations.post(
        "v1alpha/{name}:cancel",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaCancelExecutionResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsExecutionsList"
    ] = integrations.post(
        "v1alpha/{name}:cancel",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaCancelExecutionResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsExecutionsCancel"
    ] = integrations.post(
        "v1alpha/{name}:cancel",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaCancelExecutionResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsExecutionsSuspensionsList"
    ] = integrations.post(
        "v1alpha/{name}:resolve",
        t.struct(
            {
                "name": t.string(),
                "suspension": t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaSuspensionIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaResolveSuspensionResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsExecutionsSuspensionsLift"
    ] = integrations.post(
        "v1alpha/{name}:resolve",
        t.struct(
            {
                "name": t.string(),
                "suspension": t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaSuspensionIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaResolveSuspensionResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsExecutionsSuspensionsResolve"
    ] = integrations.post(
        "v1alpha/{name}:resolve",
        t.struct(
            {
                "name": t.string(),
                "suspension": t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaSuspensionIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaResolveSuspensionResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsVersionsPublish"
    ] = integrations.post(
        "v1alpha/{name}:unpublish",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsVersionsPatch"] = integrations.post(
        "v1alpha/{name}:unpublish",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsVersionsList"] = integrations.post(
        "v1alpha/{name}:unpublish",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsVersionsDownload"
    ] = integrations.post(
        "v1alpha/{name}:unpublish",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsVersionsCreate"
    ] = integrations.post(
        "v1alpha/{name}:unpublish",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsVersionsUpload"
    ] = integrations.post(
        "v1alpha/{name}:unpublish",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsVersionsTakeoverEditLock"
    ] = integrations.post(
        "v1alpha/{name}:unpublish",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsVersionsDelete"
    ] = integrations.post(
        "v1alpha/{name}:unpublish",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsVersionsGet"] = integrations.post(
        "v1alpha/{name}:unpublish",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsVersionsUnpublish"
    ] = integrations.post(
        "v1alpha/{name}:unpublish",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsSfdcInstancesList"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsSfdcInstancesPatch"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsSfdcInstancesCreate"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsSfdcInstancesGet"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsSfdcInstancesDelete"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
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
                "lastReplayId": t.string().optional(),
                "channelTopic": t.string().optional(),
                "isActive": t.boolean().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
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
                "lastReplayId": t.string().optional(),
                "channelTopic": t.string().optional(),
                "isActive": t.boolean().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
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
                "lastReplayId": t.string().optional(),
                "channelTopic": t.string().optional(),
                "isActive": t.boolean().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
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
                "lastReplayId": t.string().optional(),
                "channelTopic": t.string().optional(),
                "isActive": t.boolean().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
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
                "lastReplayId": t.string().optional(),
                "channelTopic": t.string().optional(),
                "isActive": t.boolean().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsCertificatesDelete"] = integrations.get(
        "v1alpha/{parent}/certificates",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListCertificatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsCertificatesCreate"] = integrations.get(
        "v1alpha/{parent}/certificates",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListCertificatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsCertificatesPatch"] = integrations.get(
        "v1alpha/{parent}/certificates",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListCertificatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsCertificatesGet"] = integrations.get(
        "v1alpha/{parent}/certificates",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListCertificatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsCertificatesList"] = integrations.get(
        "v1alpha/{parent}/certificates",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListCertificatesResponseOut"]),
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
        "projectsLocationsProductsIntegrationtemplatesVersionsList"
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
        "projectsLocationsConnectionsRuntimeEntitySchemasList"
    ] = integrations.get(
        "v1alpha/{parent}/runtimeEntitySchemas",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConnectionsRuntimeActionSchemasList"
    ] = integrations.get(
        "v1alpha/{parent}/runtimeActionSchemas",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseOut"]
        ),
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

    return Import(
        importer="integrations",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
