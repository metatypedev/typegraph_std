from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_integrations() -> Import:
    integrations = HTTPRuntime("https://integrations.googleapis.com/")

    renames = {
        "ErrorResponse": "_integrations_1_ErrorResponse",
        "GoogleCloudIntegrationsV1alphaPublishIntegrationVersionResponseIn": "_integrations_2_GoogleCloudIntegrationsV1alphaPublishIntegrationVersionResponseIn",
        "GoogleCloudIntegrationsV1alphaPublishIntegrationVersionResponseOut": "_integrations_3_GoogleCloudIntegrationsV1alphaPublishIntegrationVersionResponseOut",
        "EnterpriseCrmEventbusProtoSuspensionExpirationIn": "_integrations_4_EnterpriseCrmEventbusProtoSuspensionExpirationIn",
        "EnterpriseCrmEventbusProtoSuspensionExpirationOut": "_integrations_5_EnterpriseCrmEventbusProtoSuspensionExpirationOut",
        "GoogleCloudIntegrationsV1alphaSfdcInstanceIn": "_integrations_6_GoogleCloudIntegrationsV1alphaSfdcInstanceIn",
        "GoogleCloudIntegrationsV1alphaSfdcInstanceOut": "_integrations_7_GoogleCloudIntegrationsV1alphaSfdcInstanceOut",
        "EnterpriseCrmEventbusProtoStringFunctionIn": "_integrations_8_EnterpriseCrmEventbusProtoStringFunctionIn",
        "EnterpriseCrmEventbusProtoStringFunctionOut": "_integrations_9_EnterpriseCrmEventbusProtoStringFunctionOut",
        "GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestIn": "_integrations_10_GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestIn",
        "GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestOut": "_integrations_11_GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestOut",
        "GoogleCloudIntegrationsV1alphaSuccessPolicyIn": "_integrations_12_GoogleCloudIntegrationsV1alphaSuccessPolicyIn",
        "GoogleCloudIntegrationsV1alphaSuccessPolicyOut": "_integrations_13_GoogleCloudIntegrationsV1alphaSuccessPolicyOut",
        "EnterpriseCrmFrontendsEventbusProtoParamSpecEntryIn": "_integrations_14_EnterpriseCrmFrontendsEventbusProtoParamSpecEntryIn",
        "EnterpriseCrmFrontendsEventbusProtoParamSpecEntryOut": "_integrations_15_EnterpriseCrmFrontendsEventbusProtoParamSpecEntryOut",
        "EnterpriseCrmEventbusProtoTokenIn": "_integrations_16_EnterpriseCrmEventbusProtoTokenIn",
        "EnterpriseCrmEventbusProtoTokenOut": "_integrations_17_EnterpriseCrmEventbusProtoTokenOut",
        "GoogleCloudIntegrationsV1alphaTriggerConfigIn": "_integrations_18_GoogleCloudIntegrationsV1alphaTriggerConfigIn",
        "GoogleCloudIntegrationsV1alphaTriggerConfigOut": "_integrations_19_GoogleCloudIntegrationsV1alphaTriggerConfigOut",
        "EnterpriseCrmEventbusProtoFailurePolicyIn": "_integrations_20_EnterpriseCrmEventbusProtoFailurePolicyIn",
        "EnterpriseCrmEventbusProtoFailurePolicyOut": "_integrations_21_EnterpriseCrmEventbusProtoFailurePolicyOut",
        "GoogleCloudIntegrationsV1alphaNextTaskIn": "_integrations_22_GoogleCloudIntegrationsV1alphaNextTaskIn",
        "GoogleCloudIntegrationsV1alphaNextTaskOut": "_integrations_23_GoogleCloudIntegrationsV1alphaNextTaskOut",
        "EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterIn": "_integrations_24_EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterIn",
        "EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterOut": "_integrations_25_EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterOut",
        "EnterpriseCrmEventbusProtoIntArrayIn": "_integrations_26_EnterpriseCrmEventbusProtoIntArrayIn",
        "EnterpriseCrmEventbusProtoIntArrayOut": "_integrations_27_EnterpriseCrmEventbusProtoIntArrayOut",
        "GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequestIn": "_integrations_28_GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequestIn",
        "GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequestOut": "_integrations_29_GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequestOut",
        "GoogleCloudIntegrationsV1alphaIntParameterArrayIn": "_integrations_30_GoogleCloudIntegrationsV1alphaIntParameterArrayIn",
        "GoogleCloudIntegrationsV1alphaIntParameterArrayOut": "_integrations_31_GoogleCloudIntegrationsV1alphaIntParameterArrayOut",
        "GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerIn": "_integrations_32_GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerIn",
        "GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerOut": "_integrations_33_GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerOut",
        "EnterpriseCrmEventbusProtoConditionIn": "_integrations_34_EnterpriseCrmEventbusProtoConditionIn",
        "EnterpriseCrmEventbusProtoConditionOut": "_integrations_35_EnterpriseCrmEventbusProtoConditionOut",
        "EnterpriseCrmLoggingGwsSanitizeOptionsIn": "_integrations_36_EnterpriseCrmLoggingGwsSanitizeOptionsIn",
        "EnterpriseCrmLoggingGwsSanitizeOptionsOut": "_integrations_37_EnterpriseCrmLoggingGwsSanitizeOptionsOut",
        "GoogleCloudIntegrationsV1alphaRuntimeActionSchemaIn": "_integrations_38_GoogleCloudIntegrationsV1alphaRuntimeActionSchemaIn",
        "GoogleCloudIntegrationsV1alphaRuntimeActionSchemaOut": "_integrations_39_GoogleCloudIntegrationsV1alphaRuntimeActionSchemaOut",
        "GoogleCloudIntegrationsV1alphaEventParameterIn": "_integrations_40_GoogleCloudIntegrationsV1alphaEventParameterIn",
        "GoogleCloudIntegrationsV1alphaEventParameterOut": "_integrations_41_GoogleCloudIntegrationsV1alphaEventParameterOut",
        "EnterpriseCrmEventbusProtoLoopMetadataIn": "_integrations_42_EnterpriseCrmEventbusProtoLoopMetadataIn",
        "EnterpriseCrmEventbusProtoLoopMetadataOut": "_integrations_43_EnterpriseCrmEventbusProtoLoopMetadataOut",
        "GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationIn": "_integrations_44_GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationIn",
        "GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationOut": "_integrations_45_GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationOut",
        "GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseIn": "_integrations_46_GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseIn",
        "GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseOut": "_integrations_47_GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseOut",
        "EnterpriseCrmEventbusProtoStringArrayIn": "_integrations_48_EnterpriseCrmEventbusProtoStringArrayIn",
        "EnterpriseCrmEventbusProtoStringArrayOut": "_integrations_49_EnterpriseCrmEventbusProtoStringArrayOut",
        "EnterpriseCrmEventbusProtoBaseValueIn": "_integrations_50_EnterpriseCrmEventbusProtoBaseValueIn",
        "EnterpriseCrmEventbusProtoBaseValueOut": "_integrations_51_EnterpriseCrmEventbusProtoBaseValueOut",
        "EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionIn": "_integrations_52_EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionIn",
        "EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionOut": "_integrations_53_EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionOut",
        "GoogleCloudIntegrationsV1alphaIntegrationParameterIn": "_integrations_54_GoogleCloudIntegrationsV1alphaIntegrationParameterIn",
        "GoogleCloudIntegrationsV1alphaIntegrationParameterOut": "_integrations_55_GoogleCloudIntegrationsV1alphaIntegrationParameterOut",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeIn": "_integrations_56_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeIn",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeOut": "_integrations_57_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeOut",
        "GoogleCloudIntegrationsV1alphaAuthTokenIn": "_integrations_58_GoogleCloudIntegrationsV1alphaAuthTokenIn",
        "GoogleCloudIntegrationsV1alphaAuthTokenOut": "_integrations_59_GoogleCloudIntegrationsV1alphaAuthTokenOut",
        "EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn": "_integrations_60_EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn",
        "EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut": "_integrations_61_EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut",
        "EnterpriseCrmEventbusProtoParamSpecEntryConfigIn": "_integrations_62_EnterpriseCrmEventbusProtoParamSpecEntryConfigIn",
        "EnterpriseCrmEventbusProtoParamSpecEntryConfigOut": "_integrations_63_EnterpriseCrmEventbusProtoParamSpecEntryConfigOut",
        "GoogleCloudIntegrationsV1alphaAttemptStatsIn": "_integrations_64_GoogleCloudIntegrationsV1alphaAttemptStatsIn",
        "GoogleCloudIntegrationsV1alphaAttemptStatsOut": "_integrations_65_GoogleCloudIntegrationsV1alphaAttemptStatsOut",
        "GoogleCloudConnectorsV1ConnectionIn": "_integrations_66_GoogleCloudConnectorsV1ConnectionIn",
        "GoogleCloudConnectorsV1ConnectionOut": "_integrations_67_GoogleCloudConnectorsV1ConnectionOut",
        "GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseIn": "_integrations_68_GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseIn",
        "GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseOut": "_integrations_69_GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseOut",
        "EnterpriseCrmEventbusProtoMappedFieldIn": "_integrations_70_EnterpriseCrmEventbusProtoMappedFieldIn",
        "EnterpriseCrmEventbusProtoMappedFieldOut": "_integrations_71_EnterpriseCrmEventbusProtoMappedFieldOut",
        "GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseIn": "_integrations_72_GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseIn",
        "GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseOut": "_integrations_73_GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseOut",
        "EnterpriseCrmEventbusProtoEventParametersIn": "_integrations_74_EnterpriseCrmEventbusProtoEventParametersIn",
        "EnterpriseCrmEventbusProtoEventParametersOut": "_integrations_75_EnterpriseCrmEventbusProtoEventParametersOut",
        "GoogleCloudIntegrationsV1alphaListConnectionsResponseIn": "_integrations_76_GoogleCloudIntegrationsV1alphaListConnectionsResponseIn",
        "GoogleCloudIntegrationsV1alphaListConnectionsResponseOut": "_integrations_77_GoogleCloudIntegrationsV1alphaListConnectionsResponseOut",
        "GoogleCloudIntegrationsV1alphaClientCertificateIn": "_integrations_78_GoogleCloudIntegrationsV1alphaClientCertificateIn",
        "GoogleCloudIntegrationsV1alphaClientCertificateOut": "_integrations_79_GoogleCloudIntegrationsV1alphaClientCertificateOut",
        "EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayIn": "_integrations_80_EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayIn",
        "EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayOut": "_integrations_81_EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayOut",
        "GoogleCloudIntegrationsV1alphaOidcTokenIn": "_integrations_82_GoogleCloudIntegrationsV1alphaOidcTokenIn",
        "GoogleCloudIntegrationsV1alphaOidcTokenOut": "_integrations_83_GoogleCloudIntegrationsV1alphaOidcTokenOut",
        "EnterpriseCrmEventbusProtoParameterMapFieldIn": "_integrations_84_EnterpriseCrmEventbusProtoParameterMapFieldIn",
        "EnterpriseCrmEventbusProtoParameterMapFieldOut": "_integrations_85_EnterpriseCrmEventbusProtoParameterMapFieldOut",
        "GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestIn": "_integrations_86_GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestIn",
        "GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestOut": "_integrations_87_GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestOut",
        "GoogleCloudConnectorsV1AuthConfigIn": "_integrations_88_GoogleCloudConnectorsV1AuthConfigIn",
        "GoogleCloudConnectorsV1AuthConfigOut": "_integrations_89_GoogleCloudConnectorsV1AuthConfigOut",
        "EnterpriseCrmEventbusProtoIntParameterArrayIn": "_integrations_90_EnterpriseCrmEventbusProtoIntParameterArrayIn",
        "EnterpriseCrmEventbusProtoIntParameterArrayOut": "_integrations_91_EnterpriseCrmEventbusProtoIntParameterArrayOut",
        "GoogleCloudIntegrationsV1alphaListCertificatesResponseIn": "_integrations_92_GoogleCloudIntegrationsV1alphaListCertificatesResponseIn",
        "GoogleCloudIntegrationsV1alphaListCertificatesResponseOut": "_integrations_93_GoogleCloudIntegrationsV1alphaListCertificatesResponseOut",
        "EnterpriseCrmEventbusProtoIntFunctionIn": "_integrations_94_EnterpriseCrmEventbusProtoIntFunctionIn",
        "EnterpriseCrmEventbusProtoIntFunctionOut": "_integrations_95_EnterpriseCrmEventbusProtoIntFunctionOut",
        "GoogleCloudIntegrationsV1alphaParameterMapEntryIn": "_integrations_96_GoogleCloudIntegrationsV1alphaParameterMapEntryIn",
        "GoogleCloudIntegrationsV1alphaParameterMapEntryOut": "_integrations_97_GoogleCloudIntegrationsV1alphaParameterMapEntryOut",
        "EnterpriseCrmEventbusProtoBooleanParameterArrayIn": "_integrations_98_EnterpriseCrmEventbusProtoBooleanParameterArrayIn",
        "EnterpriseCrmEventbusProtoBooleanParameterArrayOut": "_integrations_99_EnterpriseCrmEventbusProtoBooleanParameterArrayOut",
        "GoogleCloudIntegrationsV1alphaExecutionDetailsIn": "_integrations_100_GoogleCloudIntegrationsV1alphaExecutionDetailsIn",
        "GoogleCloudIntegrationsV1alphaExecutionDetailsOut": "_integrations_101_GoogleCloudIntegrationsV1alphaExecutionDetailsOut",
        "GoogleCloudIntegrationsV1alphaCancelExecutionResponseIn": "_integrations_102_GoogleCloudIntegrationsV1alphaCancelExecutionResponseIn",
        "GoogleCloudIntegrationsV1alphaCancelExecutionResponseOut": "_integrations_103_GoogleCloudIntegrationsV1alphaCancelExecutionResponseOut",
        "EnterpriseCrmEventbusProtoStringParameterArrayIn": "_integrations_104_EnterpriseCrmEventbusProtoStringParameterArrayIn",
        "EnterpriseCrmEventbusProtoStringParameterArrayOut": "_integrations_105_EnterpriseCrmEventbusProtoStringParameterArrayOut",
        "EnterpriseCrmEventbusProtoExecutionTraceInfoIn": "_integrations_106_EnterpriseCrmEventbusProtoExecutionTraceInfoIn",
        "EnterpriseCrmEventbusProtoExecutionTraceInfoOut": "_integrations_107_EnterpriseCrmEventbusProtoExecutionTraceInfoOut",
        "EnterpriseCrmEventbusProtoNextTaskIn": "_integrations_108_EnterpriseCrmEventbusProtoNextTaskIn",
        "EnterpriseCrmEventbusProtoNextTaskOut": "_integrations_109_EnterpriseCrmEventbusProtoNextTaskOut",
        "EnterpriseCrmEventbusProtoProtoArrayFunctionIn": "_integrations_110_EnterpriseCrmEventbusProtoProtoArrayFunctionIn",
        "EnterpriseCrmEventbusProtoProtoArrayFunctionOut": "_integrations_111_EnterpriseCrmEventbusProtoProtoArrayFunctionOut",
        "EnterpriseCrmEventbusProtoConditionResultIn": "_integrations_112_EnterpriseCrmEventbusProtoConditionResultIn",
        "EnterpriseCrmEventbusProtoConditionResultOut": "_integrations_113_EnterpriseCrmEventbusProtoConditionResultOut",
        "GoogleCloudIntegrationsV1alphaAuthConfigIn": "_integrations_114_GoogleCloudIntegrationsV1alphaAuthConfigIn",
        "GoogleCloudIntegrationsV1alphaAuthConfigOut": "_integrations_115_GoogleCloudIntegrationsV1alphaAuthConfigOut",
        "GoogleCloudConnectorsV1SecretIn": "_integrations_116_GoogleCloudConnectorsV1SecretIn",
        "GoogleCloudConnectorsV1SecretOut": "_integrations_117_GoogleCloudConnectorsV1SecretOut",
        "GoogleCloudConnectorsV1ConnectionStatusIn": "_integrations_118_GoogleCloudConnectorsV1ConnectionStatusIn",
        "GoogleCloudConnectorsV1ConnectionStatusOut": "_integrations_119_GoogleCloudConnectorsV1ConnectionStatusOut",
        "GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionIn": "_integrations_120_GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionIn",
        "GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionOut": "_integrations_121_GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionOut",
        "EnterpriseCrmEventbusProtoTaskExecutionDetailsIn": "_integrations_122_EnterpriseCrmEventbusProtoTaskExecutionDetailsIn",
        "EnterpriseCrmEventbusProtoTaskExecutionDetailsOut": "_integrations_123_EnterpriseCrmEventbusProtoTaskExecutionDetailsOut",
        "EnterpriseCrmFrontendsEventbusProtoEventParametersIn": "_integrations_124_EnterpriseCrmFrontendsEventbusProtoEventParametersIn",
        "EnterpriseCrmFrontendsEventbusProtoEventParametersOut": "_integrations_125_EnterpriseCrmFrontendsEventbusProtoEventParametersOut",
        "EnterpriseCrmEventbusProtoJsonFunctionIn": "_integrations_126_EnterpriseCrmEventbusProtoJsonFunctionIn",
        "EnterpriseCrmEventbusProtoJsonFunctionOut": "_integrations_127_EnterpriseCrmEventbusProtoJsonFunctionOut",
        "GoogleCloudIntegrationsV1alphaTaskExecutionDetailsIn": "_integrations_128_GoogleCloudIntegrationsV1alphaTaskExecutionDetailsIn",
        "GoogleCloudIntegrationsV1alphaTaskExecutionDetailsOut": "_integrations_129_GoogleCloudIntegrationsV1alphaTaskExecutionDetailsOut",
        "EnterpriseCrmEventbusProtoValueTypeIn": "_integrations_130_EnterpriseCrmEventbusProtoValueTypeIn",
        "EnterpriseCrmEventbusProtoValueTypeOut": "_integrations_131_EnterpriseCrmEventbusProtoValueTypeOut",
        "EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryIn": "_integrations_132_EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryIn",
        "EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryOut": "_integrations_133_EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryOut",
        "EnterpriseCrmEventbusProtoNodeIdentifierIn": "_integrations_134_EnterpriseCrmEventbusProtoNodeIdentifierIn",
        "EnterpriseCrmEventbusProtoNodeIdentifierOut": "_integrations_135_EnterpriseCrmEventbusProtoNodeIdentifierOut",
        "EnterpriseCrmEventbusProtoBooleanFunctionIn": "_integrations_136_EnterpriseCrmEventbusProtoBooleanFunctionIn",
        "EnterpriseCrmEventbusProtoBooleanFunctionOut": "_integrations_137_EnterpriseCrmEventbusProtoBooleanFunctionOut",
        "GoogleCloudIntegrationsV1alphaLiftSuspensionResponseIn": "_integrations_138_GoogleCloudIntegrationsV1alphaLiftSuspensionResponseIn",
        "GoogleCloudIntegrationsV1alphaLiftSuspensionResponseOut": "_integrations_139_GoogleCloudIntegrationsV1alphaLiftSuspensionResponseOut",
        "EnterpriseCrmEventbusProtoBaseFunctionIn": "_integrations_140_EnterpriseCrmEventbusProtoBaseFunctionIn",
        "EnterpriseCrmEventbusProtoBaseFunctionOut": "_integrations_141_EnterpriseCrmEventbusProtoBaseFunctionOut",
        "EnterpriseCrmEventbusProtoNextTeardownTaskIn": "_integrations_142_EnterpriseCrmEventbusProtoNextTeardownTaskIn",
        "EnterpriseCrmEventbusProtoNextTeardownTaskOut": "_integrations_143_EnterpriseCrmEventbusProtoNextTeardownTaskOut",
        "GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponseIn": "_integrations_144_GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponseIn",
        "GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponseOut": "_integrations_145_GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponseOut",
        "GoogleCloudIntegrationsV1alphaResolveSuspensionResponseIn": "_integrations_146_GoogleCloudIntegrationsV1alphaResolveSuspensionResponseIn",
        "GoogleCloudIntegrationsV1alphaResolveSuspensionResponseOut": "_integrations_147_GoogleCloudIntegrationsV1alphaResolveSuspensionResponseOut",
        "GoogleCloudIntegrationsV1alphaValueTypeIn": "_integrations_148_GoogleCloudIntegrationsV1alphaValueTypeIn",
        "GoogleCloudIntegrationsV1alphaValueTypeOut": "_integrations_149_GoogleCloudIntegrationsV1alphaValueTypeOut",
        "EnterpriseCrmEventbusProtoWorkflowAlertConfigIn": "_integrations_150_EnterpriseCrmEventbusProtoWorkflowAlertConfigIn",
        "EnterpriseCrmEventbusProtoWorkflowAlertConfigOut": "_integrations_151_EnterpriseCrmEventbusProtoWorkflowAlertConfigOut",
        "GoogleCloudIntegrationsV1alphaCancelExecutionRequestIn": "_integrations_152_GoogleCloudIntegrationsV1alphaCancelExecutionRequestIn",
        "GoogleCloudIntegrationsV1alphaCancelExecutionRequestOut": "_integrations_153_GoogleCloudIntegrationsV1alphaCancelExecutionRequestOut",
        "GoogleCloudIntegrationsV1alphaDoubleParameterArrayIn": "_integrations_154_GoogleCloudIntegrationsV1alphaDoubleParameterArrayIn",
        "GoogleCloudIntegrationsV1alphaDoubleParameterArrayOut": "_integrations_155_GoogleCloudIntegrationsV1alphaDoubleParameterArrayOut",
        "EnterpriseCrmEventbusProtoEventBusPropertiesIn": "_integrations_156_EnterpriseCrmEventbusProtoEventBusPropertiesIn",
        "EnterpriseCrmEventbusProtoEventBusPropertiesOut": "_integrations_157_EnterpriseCrmEventbusProtoEventBusPropertiesOut",
        "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityIn": "_integrations_158_EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityIn",
        "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityOut": "_integrations_159_EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityOut",
        "GoogleCloudIntegrationsV1alphaResolveSuspensionRequestIn": "_integrations_160_GoogleCloudIntegrationsV1alphaResolveSuspensionRequestIn",
        "GoogleCloudIntegrationsV1alphaResolveSuspensionRequestOut": "_integrations_161_GoogleCloudIntegrationsV1alphaResolveSuspensionRequestOut",
        "EnterpriseCrmEventbusProtoCloudSchedulerConfigIn": "_integrations_162_EnterpriseCrmEventbusProtoCloudSchedulerConfigIn",
        "EnterpriseCrmEventbusProtoCloudSchedulerConfigOut": "_integrations_163_EnterpriseCrmEventbusProtoCloudSchedulerConfigOut",
        "EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamIn": "_integrations_164_EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamIn",
        "EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamOut": "_integrations_165_EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamOut",
        "EnterpriseCrmEventbusProtoScatterResponseIn": "_integrations_166_EnterpriseCrmEventbusProtoScatterResponseIn",
        "EnterpriseCrmEventbusProtoScatterResponseOut": "_integrations_167_EnterpriseCrmEventbusProtoScatterResponseOut",
        "EnterpriseCrmEventbusProtoDoubleParameterArrayIn": "_integrations_168_EnterpriseCrmEventbusProtoDoubleParameterArrayIn",
        "EnterpriseCrmEventbusProtoDoubleParameterArrayOut": "_integrations_169_EnterpriseCrmEventbusProtoDoubleParameterArrayOut",
        "GoogleCloudConnectorsV1LogConfigIn": "_integrations_170_GoogleCloudConnectorsV1LogConfigIn",
        "GoogleCloudConnectorsV1LogConfigOut": "_integrations_171_GoogleCloudConnectorsV1LogConfigOut",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeIn": "_integrations_172_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeIn",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeOut": "_integrations_173_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeOut",
        "GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestIn": "_integrations_174_GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestIn",
        "GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestOut": "_integrations_175_GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestOut",
        "GoogleCloudConnectorsV1AuthConfigSshPublicKeyIn": "_integrations_176_GoogleCloudConnectorsV1AuthConfigSshPublicKeyIn",
        "GoogleCloudConnectorsV1AuthConfigSshPublicKeyOut": "_integrations_177_GoogleCloudConnectorsV1AuthConfigSshPublicKeyOut",
        "GoogleCloudIntegrationsV1alphaCredentialIn": "_integrations_178_GoogleCloudIntegrationsV1alphaCredentialIn",
        "GoogleCloudIntegrationsV1alphaCredentialOut": "_integrations_179_GoogleCloudIntegrationsV1alphaCredentialOut",
        "EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsIn": "_integrations_180_EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsIn",
        "EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsOut": "_integrations_181_EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsOut",
        "EnterpriseCrmEventbusProtoTaskMetadataAdminIn": "_integrations_182_EnterpriseCrmEventbusProtoTaskMetadataAdminIn",
        "EnterpriseCrmEventbusProtoTaskMetadataAdminOut": "_integrations_183_EnterpriseCrmEventbusProtoTaskMetadataAdminOut",
        "EnterpriseCrmFrontendsEventbusProtoTaskEntityIn": "_integrations_184_EnterpriseCrmFrontendsEventbusProtoTaskEntityIn",
        "EnterpriseCrmFrontendsEventbusProtoTaskEntityOut": "_integrations_185_EnterpriseCrmFrontendsEventbusProtoTaskEntityOut",
        "EnterpriseCrmEventbusProtoBooleanArrayFunctionIn": "_integrations_186_EnterpriseCrmEventbusProtoBooleanArrayFunctionIn",
        "EnterpriseCrmEventbusProtoBooleanArrayFunctionOut": "_integrations_187_EnterpriseCrmEventbusProtoBooleanArrayFunctionOut",
        "GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseIn": "_integrations_188_GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseIn",
        "GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseOut": "_integrations_189_GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseOut",
        "EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn": "_integrations_190_EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn",
        "EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut": "_integrations_191_EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut",
        "EnterpriseCrmEventbusProtoTaskAlertConfigIn": "_integrations_192_EnterpriseCrmEventbusProtoTaskAlertConfigIn",
        "EnterpriseCrmEventbusProtoTaskAlertConfigOut": "_integrations_193_EnterpriseCrmEventbusProtoTaskAlertConfigOut",
        "EnterpriseCrmEventbusProtoExternalTrafficIn": "_integrations_194_EnterpriseCrmEventbusProtoExternalTrafficIn",
        "EnterpriseCrmEventbusProtoExternalTrafficOut": "_integrations_195_EnterpriseCrmEventbusProtoExternalTrafficOut",
        "EnterpriseCrmFrontendsEventbusProtoTaskConfigIn": "_integrations_196_EnterpriseCrmFrontendsEventbusProtoTaskConfigIn",
        "EnterpriseCrmFrontendsEventbusProtoTaskConfigOut": "_integrations_197_EnterpriseCrmFrontendsEventbusProtoTaskConfigOut",
        "EnterpriseCrmEventbusProtoProtoFunctionIn": "_integrations_198_EnterpriseCrmEventbusProtoProtoFunctionIn",
        "EnterpriseCrmEventbusProtoProtoFunctionOut": "_integrations_199_EnterpriseCrmEventbusProtoProtoFunctionOut",
        "EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn": "_integrations_200_EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn",
        "EnterpriseCrmFrontendsEventbusProtoTriggerConfigOut": "_integrations_201_EnterpriseCrmFrontendsEventbusProtoTriggerConfigOut",
        "EnterpriseCrmEventbusProtoCustomSuspensionRequestIn": "_integrations_202_EnterpriseCrmEventbusProtoCustomSuspensionRequestIn",
        "EnterpriseCrmEventbusProtoCustomSuspensionRequestOut": "_integrations_203_EnterpriseCrmEventbusProtoCustomSuspensionRequestOut",
        "EnterpriseCrmEventbusProtoAttributesIn": "_integrations_204_EnterpriseCrmEventbusProtoAttributesIn",
        "EnterpriseCrmEventbusProtoAttributesOut": "_integrations_205_EnterpriseCrmEventbusProtoAttributesOut",
        "GoogleCloudIntegrationsV1alphaPublishIntegrationVersionRequestIn": "_integrations_206_GoogleCloudIntegrationsV1alphaPublishIntegrationVersionRequestIn",
        "GoogleCloudIntegrationsV1alphaPublishIntegrationVersionRequestOut": "_integrations_207_GoogleCloudIntegrationsV1alphaPublishIntegrationVersionRequestOut",
        "GoogleCloudIntegrationsV1alphaGenerateTokenResponseIn": "_integrations_208_GoogleCloudIntegrationsV1alphaGenerateTokenResponseIn",
        "GoogleCloudIntegrationsV1alphaGenerateTokenResponseOut": "_integrations_209_GoogleCloudIntegrationsV1alphaGenerateTokenResponseOut",
        "GoogleCloudIntegrationsV1alphaTaskConfigIn": "_integrations_210_GoogleCloudIntegrationsV1alphaTaskConfigIn",
        "GoogleCloudIntegrationsV1alphaTaskConfigOut": "_integrations_211_GoogleCloudIntegrationsV1alphaTaskConfigOut",
        "GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseIn": "_integrations_212_GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseIn",
        "GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseOut": "_integrations_213_GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseOut",
        "GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn": "_integrations_214_GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn",
        "GoogleCloudIntegrationsV1alphaErrorCatcherConfigOut": "_integrations_215_GoogleCloudIntegrationsV1alphaErrorCatcherConfigOut",
        "GoogleCloudIntegrationsV1alphaAccessTokenIn": "_integrations_216_GoogleCloudIntegrationsV1alphaAccessTokenIn",
        "GoogleCloudIntegrationsV1alphaAccessTokenOut": "_integrations_217_GoogleCloudIntegrationsV1alphaAccessTokenOut",
        "EnterpriseCrmFrontendsEventbusProtoRollbackStrategyIn": "_integrations_218_EnterpriseCrmFrontendsEventbusProtoRollbackStrategyIn",
        "EnterpriseCrmFrontendsEventbusProtoRollbackStrategyOut": "_integrations_219_EnterpriseCrmFrontendsEventbusProtoRollbackStrategyOut",
        "EnterpriseCrmEventbusProtoNotificationIn": "_integrations_220_EnterpriseCrmEventbusProtoNotificationIn",
        "EnterpriseCrmEventbusProtoNotificationOut": "_integrations_221_EnterpriseCrmEventbusProtoNotificationOut",
        "GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseIn": "_integrations_222_GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseIn",
        "GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseOut": "_integrations_223_GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseOut",
        "GoogleCloudIntegrationsV1alphaUploadIntegrationVersionResponseIn": "_integrations_224_GoogleCloudIntegrationsV1alphaUploadIntegrationVersionResponseIn",
        "GoogleCloudIntegrationsV1alphaUploadIntegrationVersionResponseOut": "_integrations_225_GoogleCloudIntegrationsV1alphaUploadIntegrationVersionResponseOut",
        "EnterpriseCrmEventbusProtoSuccessPolicyIn": "_integrations_226_EnterpriseCrmEventbusProtoSuccessPolicyIn",
        "EnterpriseCrmEventbusProtoSuccessPolicyOut": "_integrations_227_EnterpriseCrmEventbusProtoSuccessPolicyOut",
        "EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayIn": "_integrations_228_EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayIn",
        "EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayOut": "_integrations_229_EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayOut",
        "EnterpriseCrmEventbusStatsDimensionsIn": "_integrations_230_EnterpriseCrmEventbusStatsDimensionsIn",
        "EnterpriseCrmEventbusStatsDimensionsOut": "_integrations_231_EnterpriseCrmEventbusStatsDimensionsOut",
        "GoogleCloudIntegrationsV1alphaListAuthConfigsResponseIn": "_integrations_232_GoogleCloudIntegrationsV1alphaListAuthConfigsResponseIn",
        "GoogleCloudIntegrationsV1alphaListAuthConfigsResponseOut": "_integrations_233_GoogleCloudIntegrationsV1alphaListAuthConfigsResponseOut",
        "EnterpriseCrmEventbusProtoErrorDetailIn": "_integrations_234_EnterpriseCrmEventbusProtoErrorDetailIn",
        "EnterpriseCrmEventbusProtoErrorDetailOut": "_integrations_235_EnterpriseCrmEventbusProtoErrorDetailOut",
        "GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseIn": "_integrations_236_GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseIn",
        "GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseOut": "_integrations_237_GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseOut",
        "EnterpriseCrmEventbusProtoBuganizerNotificationIn": "_integrations_238_EnterpriseCrmEventbusProtoBuganizerNotificationIn",
        "EnterpriseCrmEventbusProtoBuganizerNotificationOut": "_integrations_239_EnterpriseCrmEventbusProtoBuganizerNotificationOut",
        "EnterpriseCrmEventbusProtoEventExecutionDetailsIn": "_integrations_240_EnterpriseCrmEventbusProtoEventExecutionDetailsIn",
        "EnterpriseCrmEventbusProtoEventExecutionDetailsOut": "_integrations_241_EnterpriseCrmEventbusProtoEventExecutionDetailsOut",
        "GoogleCloudIntegrationsV1alphaListSuspensionsResponseIn": "_integrations_242_GoogleCloudIntegrationsV1alphaListSuspensionsResponseIn",
        "GoogleCloudIntegrationsV1alphaListSuspensionsResponseOut": "_integrations_243_GoogleCloudIntegrationsV1alphaListSuspensionsResponseOut",
        "GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaIn": "_integrations_244_GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaIn",
        "GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaOut": "_integrations_245_GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaOut",
        "EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoIn": "_integrations_246_EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoIn",
        "EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoOut": "_integrations_247_EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoOut",
        "EnterpriseCrmEventbusProtoTriggerCriteriaIn": "_integrations_248_EnterpriseCrmEventbusProtoTriggerCriteriaIn",
        "EnterpriseCrmEventbusProtoTriggerCriteriaOut": "_integrations_249_EnterpriseCrmEventbusProtoTriggerCriteriaOut",
        "EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsIn": "_integrations_250_EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsIn",
        "EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsOut": "_integrations_251_EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsOut",
        "EnterpriseCrmEventbusProtoCombinedConditionIn": "_integrations_252_EnterpriseCrmEventbusProtoCombinedConditionIn",
        "EnterpriseCrmEventbusProtoCombinedConditionOut": "_integrations_253_EnterpriseCrmEventbusProtoCombinedConditionOut",
        "GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestIn": "_integrations_254_GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestIn",
        "GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestOut": "_integrations_255_GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestOut",
        "EnterpriseCrmEventbusProtoParameterEntryIn": "_integrations_256_EnterpriseCrmEventbusProtoParameterEntryIn",
        "EnterpriseCrmEventbusProtoParameterEntryOut": "_integrations_257_EnterpriseCrmEventbusProtoParameterEntryOut",
        "EnterpriseCrmEventbusProtoCoordinateIn": "_integrations_258_EnterpriseCrmEventbusProtoCoordinateIn",
        "EnterpriseCrmEventbusProtoCoordinateOut": "_integrations_259_EnterpriseCrmEventbusProtoCoordinateOut",
        "GoogleCloudIntegrationsV1alphaCloudSchedulerConfigIn": "_integrations_260_GoogleCloudIntegrationsV1alphaCloudSchedulerConfigIn",
        "GoogleCloudIntegrationsV1alphaCloudSchedulerConfigOut": "_integrations_261_GoogleCloudIntegrationsV1alphaCloudSchedulerConfigOut",
        "EnterpriseCrmFrontendsEventbusProtoParameterMapFieldIn": "_integrations_262_EnterpriseCrmFrontendsEventbusProtoParameterMapFieldIn",
        "EnterpriseCrmFrontendsEventbusProtoParameterMapFieldOut": "_integrations_263_EnterpriseCrmFrontendsEventbusProtoParameterMapFieldOut",
        "EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageIn": "_integrations_264_EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageIn",
        "EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageOut": "_integrations_265_EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageOut",
        "EnterpriseCrmEventbusProtoDoubleArrayFunctionIn": "_integrations_266_EnterpriseCrmEventbusProtoDoubleArrayFunctionIn",
        "EnterpriseCrmEventbusProtoDoubleArrayFunctionOut": "_integrations_267_EnterpriseCrmEventbusProtoDoubleArrayFunctionOut",
        "GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeIn": "_integrations_268_GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeIn",
        "GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeOut": "_integrations_269_GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeOut",
        "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsIn": "_integrations_270_EnterpriseCrmEventbusProtoSuspensionAuthPermissionsIn",
        "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsOut": "_integrations_271_EnterpriseCrmEventbusProtoSuspensionAuthPermissionsOut",
        "EnterpriseCrmEventbusProtoParameterMapIn": "_integrations_272_EnterpriseCrmEventbusProtoParameterMapIn",
        "EnterpriseCrmEventbusProtoParameterMapOut": "_integrations_273_EnterpriseCrmEventbusProtoParameterMapOut",
        "GoogleCloudIntegrationsV1alphaParameterMapIn": "_integrations_274_GoogleCloudIntegrationsV1alphaParameterMapIn",
        "GoogleCloudIntegrationsV1alphaParameterMapOut": "_integrations_275_GoogleCloudIntegrationsV1alphaParameterMapOut",
        "GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequestIn": "_integrations_276_GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequestIn",
        "GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequestOut": "_integrations_277_GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequestOut",
        "EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotIn": "_integrations_278_EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotIn",
        "EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotOut": "_integrations_279_EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotOut",
        "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueIn": "_integrations_280_GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueIn",
        "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueOut": "_integrations_281_GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueOut",
        "EnterpriseCrmEventbusProtoIntArrayFunctionIn": "_integrations_282_EnterpriseCrmEventbusProtoIntArrayFunctionIn",
        "EnterpriseCrmEventbusProtoIntArrayFunctionOut": "_integrations_283_EnterpriseCrmEventbusProtoIntArrayFunctionOut",
        "EnterpriseCrmFrontendsEventbusProtoIntParameterArrayIn": "_integrations_284_EnterpriseCrmFrontendsEventbusProtoIntParameterArrayIn",
        "EnterpriseCrmFrontendsEventbusProtoIntParameterArrayOut": "_integrations_285_EnterpriseCrmFrontendsEventbusProtoIntParameterArrayOut",
        "GoogleCloudConnectorsV1ConfigVariableIn": "_integrations_286_GoogleCloudConnectorsV1ConfigVariableIn",
        "GoogleCloudConnectorsV1ConfigVariableOut": "_integrations_287_GoogleCloudConnectorsV1ConfigVariableOut",
        "GoogleCloudIntegrationsV1alphaLiftSuspensionRequestIn": "_integrations_288_GoogleCloudIntegrationsV1alphaLiftSuspensionRequestIn",
        "GoogleCloudIntegrationsV1alphaLiftSuspensionRequestOut": "_integrations_289_GoogleCloudIntegrationsV1alphaLiftSuspensionRequestOut",
        "GoogleCloudIntegrationsV1alphaSfdcChannelIn": "_integrations_290_GoogleCloudIntegrationsV1alphaSfdcChannelIn",
        "GoogleCloudIntegrationsV1alphaSfdcChannelOut": "_integrations_291_GoogleCloudIntegrationsV1alphaSfdcChannelOut",
        "EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditIn": "_integrations_292_EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditIn",
        "EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditOut": "_integrations_293_EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditOut",
        "EnterpriseCrmEventbusProtoLogSettingsIn": "_integrations_294_EnterpriseCrmEventbusProtoLogSettingsIn",
        "EnterpriseCrmEventbusProtoLogSettingsOut": "_integrations_295_EnterpriseCrmEventbusProtoLogSettingsOut",
        "EnterpriseCrmLoggingGwsFieldLimitsIn": "_integrations_296_EnterpriseCrmLoggingGwsFieldLimitsIn",
        "EnterpriseCrmLoggingGwsFieldLimitsOut": "_integrations_297_EnterpriseCrmLoggingGwsFieldLimitsOut",
        "GoogleCloudConnectorsV1AuthConfigUserPasswordIn": "_integrations_298_GoogleCloudConnectorsV1AuthConfigUserPasswordIn",
        "GoogleCloudConnectorsV1AuthConfigUserPasswordOut": "_integrations_299_GoogleCloudConnectorsV1AuthConfigUserPasswordOut",
        "EnterpriseCrmFrontendsEventbusProtoStringParameterArrayIn": "_integrations_300_EnterpriseCrmFrontendsEventbusProtoStringParameterArrayIn",
        "EnterpriseCrmFrontendsEventbusProtoStringParameterArrayOut": "_integrations_301_EnterpriseCrmFrontendsEventbusProtoStringParameterArrayOut",
        "GoogleCloudIntegrationsV1alphaSuspensionIn": "_integrations_302_GoogleCloudIntegrationsV1alphaSuspensionIn",
        "GoogleCloudIntegrationsV1alphaSuspensionOut": "_integrations_303_GoogleCloudIntegrationsV1alphaSuspensionOut",
        "GoogleCloudIntegrationsV1alphaExecutionSnapshotIn": "_integrations_304_GoogleCloudIntegrationsV1alphaExecutionSnapshotIn",
        "GoogleCloudIntegrationsV1alphaExecutionSnapshotOut": "_integrations_305_GoogleCloudIntegrationsV1alphaExecutionSnapshotOut",
        "EnterpriseCrmEventbusProtoTaskUiModuleConfigIn": "_integrations_306_EnterpriseCrmEventbusProtoTaskUiModuleConfigIn",
        "EnterpriseCrmEventbusProtoTaskUiModuleConfigOut": "_integrations_307_EnterpriseCrmEventbusProtoTaskUiModuleConfigOut",
        "EnterpriseCrmEventbusProtoFieldIn": "_integrations_308_EnterpriseCrmEventbusProtoFieldIn",
        "EnterpriseCrmEventbusProtoFieldOut": "_integrations_309_EnterpriseCrmEventbusProtoFieldOut",
        "EnterpriseCrmEventbusProtoSuspensionResolutionInfoIn": "_integrations_310_EnterpriseCrmEventbusProtoSuspensionResolutionInfoIn",
        "EnterpriseCrmEventbusProtoSuspensionResolutionInfoOut": "_integrations_311_EnterpriseCrmEventbusProtoSuspensionResolutionInfoOut",
        "EnterpriseCrmEventbusProtoEventExecutionSnapshotIn": "_integrations_312_EnterpriseCrmEventbusProtoEventExecutionSnapshotIn",
        "EnterpriseCrmEventbusProtoEventExecutionSnapshotOut": "_integrations_313_EnterpriseCrmEventbusProtoEventExecutionSnapshotOut",
        "GoogleCloudIntegrationsV1alphaJwtIn": "_integrations_314_GoogleCloudIntegrationsV1alphaJwtIn",
        "GoogleCloudIntegrationsV1alphaJwtOut": "_integrations_315_GoogleCloudIntegrationsV1alphaJwtOut",
        "GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseIn": "_integrations_316_GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseIn",
        "GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseOut": "_integrations_317_GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseOut",
        "GoogleCloudIntegrationsV1alphaListExecutionsResponseIn": "_integrations_318_GoogleCloudIntegrationsV1alphaListExecutionsResponseIn",
        "GoogleCloudIntegrationsV1alphaListExecutionsResponseOut": "_integrations_319_GoogleCloudIntegrationsV1alphaListExecutionsResponseOut",
        "EnterpriseCrmEventbusProtoAddressIn": "_integrations_320_EnterpriseCrmEventbusProtoAddressIn",
        "EnterpriseCrmEventbusProtoAddressOut": "_integrations_321_EnterpriseCrmEventbusProtoAddressOut",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexIn": "_integrations_322_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexIn",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexOut": "_integrations_323_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexOut",
        "GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsIn": "_integrations_324_GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsIn",
        "GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsOut": "_integrations_325_GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsOut",
        "EnterpriseCrmFrontendsEventbusProtoParameterEntryIn": "_integrations_326_EnterpriseCrmFrontendsEventbusProtoParameterEntryIn",
        "EnterpriseCrmFrontendsEventbusProtoParameterEntryOut": "_integrations_327_EnterpriseCrmFrontendsEventbusProtoParameterEntryOut",
        "GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestIn": "_integrations_328_GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestIn",
        "GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestOut": "_integrations_329_GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestOut",
        "EnterpriseCrmEventbusProtoParameterValueTypeIn": "_integrations_330_EnterpriseCrmEventbusProtoParameterValueTypeIn",
        "EnterpriseCrmEventbusProtoParameterValueTypeOut": "_integrations_331_EnterpriseCrmEventbusProtoParameterValueTypeOut",
        "GoogleCloudConnectorsV1LockConfigIn": "_integrations_332_GoogleCloudConnectorsV1LockConfigIn",
        "GoogleCloudConnectorsV1LockConfigOut": "_integrations_333_GoogleCloudConnectorsV1LockConfigOut",
        "GoogleCloudIntegrationsV1alphaCertificateIn": "_integrations_334_GoogleCloudIntegrationsV1alphaCertificateIn",
        "GoogleCloudIntegrationsV1alphaCertificateOut": "_integrations_335_GoogleCloudIntegrationsV1alphaCertificateOut",
        "EnterpriseCrmEventbusProtoTransformExpressionIn": "_integrations_336_EnterpriseCrmEventbusProtoTransformExpressionIn",
        "EnterpriseCrmEventbusProtoTransformExpressionOut": "_integrations_337_EnterpriseCrmEventbusProtoTransformExpressionOut",
        "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataIn": "_integrations_338_EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataIn",
        "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataOut": "_integrations_339_EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataOut",
        "EnterpriseCrmEventbusProtoFunctionTypeIn": "_integrations_340_EnterpriseCrmEventbusProtoFunctionTypeIn",
        "EnterpriseCrmEventbusProtoFunctionTypeOut": "_integrations_341_EnterpriseCrmEventbusProtoFunctionTypeOut",
        "GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataIn": "_integrations_342_GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataIn",
        "GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataOut": "_integrations_343_GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataOut",
        "EnterpriseCrmFrontendsEventbusProtoParameterMapIn": "_integrations_344_EnterpriseCrmFrontendsEventbusProtoParameterMapIn",
        "EnterpriseCrmFrontendsEventbusProtoParameterMapOut": "_integrations_345_EnterpriseCrmFrontendsEventbusProtoParameterMapOut",
        "GoogleCloudIntegrationsV1alphaExecutionIn": "_integrations_346_GoogleCloudIntegrationsV1alphaExecutionIn",
        "GoogleCloudIntegrationsV1alphaExecutionOut": "_integrations_347_GoogleCloudIntegrationsV1alphaExecutionOut",
        "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigIn": "_integrations_348_GoogleCloudIntegrationsV1alphaIntegrationAlertConfigIn",
        "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigOut": "_integrations_349_GoogleCloudIntegrationsV1alphaIntegrationAlertConfigOut",
        "GoogleCloudIntegrationsV1alphaCoordinateIn": "_integrations_350_GoogleCloudIntegrationsV1alphaCoordinateIn",
        "GoogleCloudIntegrationsV1alphaCoordinateOut": "_integrations_351_GoogleCloudIntegrationsV1alphaCoordinateOut",
        "GoogleCloudIntegrationsV1alphaIntegrationIn": "_integrations_352_GoogleCloudIntegrationsV1alphaIntegrationIn",
        "GoogleCloudIntegrationsV1alphaIntegrationOut": "_integrations_353_GoogleCloudIntegrationsV1alphaIntegrationOut",
        "EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueIn": "_integrations_354_EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueIn",
        "EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueOut": "_integrations_355_EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueOut",
        "GoogleCloudIntegrationsV1alphaStringParameterArrayIn": "_integrations_356_GoogleCloudIntegrationsV1alphaStringParameterArrayIn",
        "GoogleCloudIntegrationsV1alphaStringParameterArrayOut": "_integrations_357_GoogleCloudIntegrationsV1alphaStringParameterArrayOut",
        "GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigIn": "_integrations_358_GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigIn",
        "GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigOut": "_integrations_359_GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigOut",
        "EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayIn": "_integrations_360_EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayIn",
        "EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayOut": "_integrations_361_EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayOut",
        "EnterpriseCrmEventbusProtoParameterMapEntryIn": "_integrations_362_EnterpriseCrmEventbusProtoParameterMapEntryIn",
        "EnterpriseCrmEventbusProtoParameterMapEntryOut": "_integrations_363_EnterpriseCrmEventbusProtoParameterMapEntryOut",
        "GoogleCloudIntegrationsV1alphaServiceAccountCredentialsIn": "_integrations_364_GoogleCloudIntegrationsV1alphaServiceAccountCredentialsIn",
        "GoogleCloudIntegrationsV1alphaServiceAccountCredentialsOut": "_integrations_365_GoogleCloudIntegrationsV1alphaServiceAccountCredentialsOut",
        "EnterpriseCrmFrontendsEventbusProtoParameterMapEntryIn": "_integrations_366_EnterpriseCrmFrontendsEventbusProtoParameterMapEntryIn",
        "EnterpriseCrmFrontendsEventbusProtoParameterMapEntryOut": "_integrations_367_EnterpriseCrmFrontendsEventbusProtoParameterMapEntryOut",
        "EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsIn": "_integrations_368_EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsIn",
        "EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsOut": "_integrations_369_EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsOut",
        "EnterpriseCrmEventbusProtoCloudKmsConfigIn": "_integrations_370_EnterpriseCrmEventbusProtoCloudKmsConfigIn",
        "EnterpriseCrmEventbusProtoCloudKmsConfigOut": "_integrations_371_EnterpriseCrmEventbusProtoCloudKmsConfigOut",
        "GoogleCloudIntegrationsV1alphaBooleanParameterArrayIn": "_integrations_372_GoogleCloudIntegrationsV1alphaBooleanParameterArrayIn",
        "GoogleCloudIntegrationsV1alphaBooleanParameterArrayOut": "_integrations_373_GoogleCloudIntegrationsV1alphaBooleanParameterArrayOut",
        "EnterpriseCrmEventbusStatsIn": "_integrations_374_EnterpriseCrmEventbusStatsIn",
        "EnterpriseCrmEventbusStatsOut": "_integrations_375_EnterpriseCrmEventbusStatsOut",
        "EnterpriseCrmEventbusProtoTaskMetadataIn": "_integrations_376_EnterpriseCrmEventbusProtoTaskMetadataIn",
        "EnterpriseCrmEventbusProtoTaskMetadataOut": "_integrations_377_EnterpriseCrmEventbusProtoTaskMetadataOut",
        "GoogleCloudIntegrationsV1alphaUsernameAndPasswordIn": "_integrations_378_GoogleCloudIntegrationsV1alphaUsernameAndPasswordIn",
        "GoogleCloudIntegrationsV1alphaUsernameAndPasswordOut": "_integrations_379_GoogleCloudIntegrationsV1alphaUsernameAndPasswordOut",
        "GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsIn": "_integrations_380_GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsIn",
        "GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsOut": "_integrations_381_GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsOut",
        "EnterpriseCrmEventbusProtoConnectorsConnectionIn": "_integrations_382_EnterpriseCrmEventbusProtoConnectorsConnectionIn",
        "EnterpriseCrmEventbusProtoConnectorsConnectionOut": "_integrations_383_EnterpriseCrmEventbusProtoConnectorsConnectionOut",
        "GoogleCloudIntegrationsV1alphaParameterMapFieldIn": "_integrations_384_GoogleCloudIntegrationsV1alphaParameterMapFieldIn",
        "GoogleCloudIntegrationsV1alphaParameterMapFieldOut": "_integrations_385_GoogleCloudIntegrationsV1alphaParameterMapFieldOut",
        "EnterpriseCrmEventbusProtoTaskUiConfigIn": "_integrations_386_EnterpriseCrmEventbusProtoTaskUiConfigIn",
        "EnterpriseCrmEventbusProtoTaskUiConfigOut": "_integrations_387_EnterpriseCrmEventbusProtoTaskUiConfigOut",
        "EnterpriseCrmEventbusProtoSerializedObjectParameterIn": "_integrations_388_EnterpriseCrmEventbusProtoSerializedObjectParameterIn",
        "EnterpriseCrmEventbusProtoSerializedObjectParameterOut": "_integrations_389_EnterpriseCrmEventbusProtoSerializedObjectParameterOut",
        "EnterpriseCrmEventbusProtoDoubleFunctionIn": "_integrations_390_EnterpriseCrmEventbusProtoDoubleFunctionIn",
        "EnterpriseCrmEventbusProtoDoubleFunctionOut": "_integrations_391_EnterpriseCrmEventbusProtoDoubleFunctionOut",
        "GoogleCloudConnectorsV1DestinationConfigIn": "_integrations_392_GoogleCloudConnectorsV1DestinationConfigIn",
        "GoogleCloudConnectorsV1DestinationConfigOut": "_integrations_393_GoogleCloudConnectorsV1DestinationConfigOut",
        "GoogleCloudIntegrationsV1alphaFailurePolicyIn": "_integrations_394_GoogleCloudIntegrationsV1alphaFailurePolicyIn",
        "GoogleCloudIntegrationsV1alphaFailurePolicyOut": "_integrations_395_GoogleCloudIntegrationsV1alphaFailurePolicyOut",
        "GoogleCloudIntegrationsV1alphaListIntegrationsResponseIn": "_integrations_396_GoogleCloudIntegrationsV1alphaListIntegrationsResponseIn",
        "GoogleCloudIntegrationsV1alphaListIntegrationsResponseOut": "_integrations_397_GoogleCloudIntegrationsV1alphaListIntegrationsResponseOut",
        "GoogleCloudIntegrationsV1alphaSuspensionAuditIn": "_integrations_398_GoogleCloudIntegrationsV1alphaSuspensionAuditIn",
        "GoogleCloudIntegrationsV1alphaSuspensionAuditOut": "_integrations_399_GoogleCloudIntegrationsV1alphaSuspensionAuditOut",
        "GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsIn": "_integrations_400_GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsIn",
        "GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsOut": "_integrations_401_GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsOut",
        "GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseIn": "_integrations_402_GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseIn",
        "GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseOut": "_integrations_403_GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseOut",
        "GoogleCloudConnectorsV1SslConfigIn": "_integrations_404_GoogleCloudConnectorsV1SslConfigIn",
        "GoogleCloudConnectorsV1SslConfigOut": "_integrations_405_GoogleCloudConnectorsV1SslConfigOut",
        "EnterpriseCrmEventbusProtoPropertyEntryIn": "_integrations_406_EnterpriseCrmEventbusProtoPropertyEntryIn",
        "EnterpriseCrmEventbusProtoPropertyEntryOut": "_integrations_407_EnterpriseCrmEventbusProtoPropertyEntryOut",
        "GoogleCloudConnectorsV1DestinationIn": "_integrations_408_GoogleCloudConnectorsV1DestinationIn",
        "GoogleCloudConnectorsV1DestinationOut": "_integrations_409_GoogleCloudConnectorsV1DestinationOut",
        "EnterpriseCrmEventbusProtoSuspensionConfigIn": "_integrations_410_EnterpriseCrmEventbusProtoSuspensionConfigIn",
        "EnterpriseCrmEventbusProtoSuspensionConfigOut": "_integrations_411_EnterpriseCrmEventbusProtoSuspensionConfigOut",
        "GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseIn": "_integrations_412_GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseIn",
        "GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseOut": "_integrations_413_GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseOut",
        "EnterpriseCrmEventbusProtoProtoParameterArrayIn": "_integrations_414_EnterpriseCrmEventbusProtoProtoParameterArrayIn",
        "EnterpriseCrmEventbusProtoProtoParameterArrayOut": "_integrations_415_EnterpriseCrmEventbusProtoProtoParameterArrayOut",
        "GoogleCloudIntegrationsV1alphaEnumerateConnectorPlatformRegionsResponseIn": "_integrations_416_GoogleCloudIntegrationsV1alphaEnumerateConnectorPlatformRegionsResponseIn",
        "GoogleCloudIntegrationsV1alphaEnumerateConnectorPlatformRegionsResponseOut": "_integrations_417_GoogleCloudIntegrationsV1alphaEnumerateConnectorPlatformRegionsResponseOut",
        "EnterpriseCrmEventbusProtoTeardownIn": "_integrations_418_EnterpriseCrmEventbusProtoTeardownIn",
        "EnterpriseCrmEventbusProtoTeardownOut": "_integrations_419_EnterpriseCrmEventbusProtoTeardownOut",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIn": "_integrations_420_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIn",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleOut": "_integrations_421_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleOut",
        "GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequestIn": "_integrations_422_GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequestIn",
        "GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequestOut": "_integrations_423_GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequestOut",
        "EnterpriseCrmEventbusProtoTeardownTaskConfigIn": "_integrations_424_EnterpriseCrmEventbusProtoTeardownTaskConfigIn",
        "EnterpriseCrmEventbusProtoTeardownTaskConfigOut": "_integrations_425_EnterpriseCrmEventbusProtoTeardownTaskConfigOut",
        "CrmlogErrorCodeIn": "_integrations_426_CrmlogErrorCodeIn",
        "CrmlogErrorCodeOut": "_integrations_427_CrmlogErrorCodeOut",
        "GoogleCloudIntegrationsV1alphaIntegrationVersionIn": "_integrations_428_GoogleCloudIntegrationsV1alphaIntegrationVersionIn",
        "GoogleCloudIntegrationsV1alphaIntegrationVersionOut": "_integrations_429_GoogleCloudIntegrationsV1alphaIntegrationVersionOut",
        "EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn": "_integrations_430_EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn",
        "EnterpriseCrmFrontendsEventbusProtoWorkflowParametersOut": "_integrations_431_EnterpriseCrmFrontendsEventbusProtoWorkflowParametersOut",
        "EnterpriseCrmEventbusProtoDoubleArrayIn": "_integrations_432_EnterpriseCrmEventbusProtoDoubleArrayIn",
        "EnterpriseCrmEventbusProtoDoubleArrayOut": "_integrations_433_EnterpriseCrmEventbusProtoDoubleArrayOut",
        "EnterpriseCrmEventbusProtoFunctionIn": "_integrations_434_EnterpriseCrmEventbusProtoFunctionIn",
        "EnterpriseCrmEventbusProtoFunctionOut": "_integrations_435_EnterpriseCrmEventbusProtoFunctionOut",
        "GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataIn": "_integrations_436_GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataIn",
        "GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataOut": "_integrations_437_GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataOut",
        "EnterpriseCrmEventbusProtoFieldMappingConfigIn": "_integrations_438_EnterpriseCrmEventbusProtoFieldMappingConfigIn",
        "EnterpriseCrmEventbusProtoFieldMappingConfigOut": "_integrations_439_EnterpriseCrmEventbusProtoFieldMappingConfigOut",
        "GoogleCloudConnectorsV1NodeConfigIn": "_integrations_440_GoogleCloudConnectorsV1NodeConfigIn",
        "GoogleCloudConnectorsV1NodeConfigOut": "_integrations_441_GoogleCloudConnectorsV1NodeConfigOut",
        "GoogleCloudIntegrationsV1alphaTakeoverEditLockResponseIn": "_integrations_442_GoogleCloudIntegrationsV1alphaTakeoverEditLockResponseIn",
        "GoogleCloudIntegrationsV1alphaTakeoverEditLockResponseOut": "_integrations_443_GoogleCloudIntegrationsV1alphaTakeoverEditLockResponseOut",
        "GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsIn": "_integrations_444_GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsIn",
        "GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsOut": "_integrations_445_GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsOut",
        "GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowIn": "_integrations_446_GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowIn",
        "GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowOut": "_integrations_447_GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowOut",
        "EnterpriseCrmEventbusProtoStringArrayFunctionIn": "_integrations_448_EnterpriseCrmEventbusProtoStringArrayFunctionIn",
        "EnterpriseCrmEventbusProtoStringArrayFunctionOut": "_integrations_449_EnterpriseCrmEventbusProtoStringArrayFunctionOut",
        "GoogleProtobufEmptyIn": "_integrations_450_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_integrations_451_GoogleProtobufEmptyOut",
        "EnterpriseCrmEventbusProtoConnectorsGenericConnectorTaskConfigIn": "_integrations_452_EnterpriseCrmEventbusProtoConnectorsGenericConnectorTaskConfigIn",
        "EnterpriseCrmEventbusProtoConnectorsGenericConnectorTaskConfigOut": "_integrations_453_EnterpriseCrmEventbusProtoConnectorsGenericConnectorTaskConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["EnterpriseCrmEventbusProtoSuspensionExpirationIn"] = t.struct(
        {
            "expireAfterMs": t.integer().optional(),
            "remindAfterMs": t.integer().optional(),
            "liftWhenExpired": t.boolean().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionExpirationIn"])
    types["EnterpriseCrmEventbusProtoSuspensionExpirationOut"] = t.struct(
        {
            "expireAfterMs": t.integer().optional(),
            "remindAfterMs": t.integer().optional(),
            "liftWhenExpired": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionExpirationOut"])
    types["GoogleCloudIntegrationsV1alphaSfdcInstanceIn"] = t.struct(
        {
            "authConfigId": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "sfdcOrgId": t.string().optional(),
            "serviceAuthority": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceIn"])
    types["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"] = t.struct(
        {
            "authConfigId": t.array(t.string()).optional(),
            "deleteTime": t.string().optional(),
            "name": t.string().optional(),
            "sfdcOrgId": t.string().optional(),
            "updateTime": t.string().optional(),
            "serviceAuthority": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"])
    types["EnterpriseCrmEventbusProtoStringFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoStringFunctionIn"])
    types["EnterpriseCrmEventbusProtoStringFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoStringFunctionOut"])
    types["GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestIn"] = t.struct(
        {
            "requestId": t.string().optional(),
            "scheduleTime": t.string().optional(),
            "parameterEntries": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"])
            ).optional(),
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersIn"]
            ).optional(),
            "triggerId": t.string().optional(),
            "inputParameters": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestIn"])
    types["GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "scheduleTime": t.string().optional(),
            "parameterEntries": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"])
            ).optional(),
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersOut"]
            ).optional(),
            "triggerId": t.string().optional(),
            "inputParameters": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestOut"])
    types["GoogleCloudIntegrationsV1alphaSuccessPolicyIn"] = t.struct(
        {"finalState": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaSuccessPolicyIn"])
    types["GoogleCloudIntegrationsV1alphaSuccessPolicyOut"] = t.struct(
        {
            "finalState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSuccessPolicyOut"])
    types["EnterpriseCrmFrontendsEventbusProtoParamSpecEntryIn"] = t.struct(
        {
            "isDeprecated": t.boolean().optional(),
            "collectionElementClassName": t.string().optional(),
            "required": t.boolean().optional(),
            "jsonSchema": t.string().optional(),
            "dataType": t.string().optional(),
            "protoDef": t.proxy(
                renames["EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionIn"]
            ).optional(),
            "key": t.string().optional(),
            "className": t.string().optional(),
            "config": t.proxy(
                renames["EnterpriseCrmEventbusProtoParamSpecEntryConfigIn"]
            ).optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn"]
            ).optional(),
            "validationRule": t.proxy(
                renames["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIn"]
            ).optional(),
            "isOutput": t.boolean(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParamSpecEntryIn"])
    types["EnterpriseCrmFrontendsEventbusProtoParamSpecEntryOut"] = t.struct(
        {
            "isDeprecated": t.boolean().optional(),
            "collectionElementClassName": t.string().optional(),
            "required": t.boolean().optional(),
            "jsonSchema": t.string().optional(),
            "dataType": t.string().optional(),
            "protoDef": t.proxy(
                renames["EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionOut"]
            ).optional(),
            "key": t.string().optional(),
            "className": t.string().optional(),
            "config": t.proxy(
                renames["EnterpriseCrmEventbusProtoParamSpecEntryConfigOut"]
            ).optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "validationRule": t.proxy(
                renames["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleOut"]
            ).optional(),
            "isOutput": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParamSpecEntryOut"])
    types["EnterpriseCrmEventbusProtoTokenIn"] = t.struct(
        {"name": t.string(), "value": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoTokenIn"])
    types["EnterpriseCrmEventbusProtoTokenOut"] = t.struct(
        {
            "name": t.string(),
            "value": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTokenOut"])
    types["GoogleCloudIntegrationsV1alphaTriggerConfigIn"] = t.struct(
        {
            "startTasks": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaNextTaskIn"])
            ).optional(),
            "description": t.string().optional(),
            "alertConfig": t.array(
                t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigIn"]
                )
            ).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "cloudSchedulerConfig": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCloudSchedulerConfigIn"]
            ).optional(),
            "triggerNumber": t.string(),
            "errorCatcherId": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCoordinateIn"]
            ).optional(),
            "triggerId": t.string().optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "label": t.string().optional(),
            "triggerType": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaTriggerConfigIn"])
    types["GoogleCloudIntegrationsV1alphaTriggerConfigOut"] = t.struct(
        {
            "startTasks": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaNextTaskOut"])
            ).optional(),
            "description": t.string().optional(),
            "alertConfig": t.array(
                t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigOut"]
                )
            ).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "cloudSchedulerConfig": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCloudSchedulerConfigOut"]
            ).optional(),
            "triggerNumber": t.string(),
            "errorCatcherId": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCoordinateOut"]
            ).optional(),
            "triggerId": t.string().optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "label": t.string().optional(),
            "triggerType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaTriggerConfigOut"])
    types["EnterpriseCrmEventbusProtoFailurePolicyIn"] = t.struct(
        {
            "maxNumRetries": t.integer(),
            "retryStrategy": t.string().optional(),
            "intervalInSeconds": t.string(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFailurePolicyIn"])
    types["EnterpriseCrmEventbusProtoFailurePolicyOut"] = t.struct(
        {
            "maxNumRetries": t.integer(),
            "retryStrategy": t.string().optional(),
            "intervalInSeconds": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFailurePolicyOut"])
    types["GoogleCloudIntegrationsV1alphaNextTaskIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "condition": t.string().optional(),
            "taskId": t.string().optional(),
            "taskConfigId": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaNextTaskIn"])
    types["GoogleCloudIntegrationsV1alphaNextTaskOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "condition": t.string().optional(),
            "taskId": t.string().optional(),
            "taskConfigId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaNextTaskOut"])
    types["EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterIn"] = t.struct(
        {"objectValue": t.string()}
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterIn"])
    types["EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterOut"] = t.struct(
        {
            "objectValue": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterOut"])
    types["EnterpriseCrmEventbusProtoIntArrayIn"] = t.struct(
        {"values": t.array(t.string())}
    ).named(renames["EnterpriseCrmEventbusProtoIntArrayIn"])
    types["EnterpriseCrmEventbusProtoIntArrayOut"] = t.struct(
        {
            "values": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoIntArrayOut"])
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
    types["GoogleCloudIntegrationsV1alphaIntParameterArrayIn"] = t.struct(
        {"intValues": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaIntParameterArrayIn"])
    types["GoogleCloudIntegrationsV1alphaIntParameterArrayOut"] = t.struct(
        {
            "intValues": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntParameterArrayOut"])
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
    types["EnterpriseCrmLoggingGwsSanitizeOptionsIn"] = t.struct(
        {
            "isAlreadySanitized": t.boolean().optional(),
            "privacy": t.string(),
            "sanitizeType": t.string(),
            "logType": t.array(t.string()).optional(),
        }
    ).named(renames["EnterpriseCrmLoggingGwsSanitizeOptionsIn"])
    types["EnterpriseCrmLoggingGwsSanitizeOptionsOut"] = t.struct(
        {
            "isAlreadySanitized": t.boolean().optional(),
            "privacy": t.string(),
            "sanitizeType": t.string(),
            "logType": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmLoggingGwsSanitizeOptionsOut"])
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
    types["EnterpriseCrmEventbusProtoLoopMetadataIn"] = t.struct(
        {
            "currentIterationCount": t.string().optional(),
            "errorMsg": t.string().optional(),
            "currentIterationDetail": t.string().optional(),
            "failureLocation": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoLoopMetadataIn"])
    types["EnterpriseCrmEventbusProtoLoopMetadataOut"] = t.struct(
        {
            "currentIterationCount": t.string().optional(),
            "errorMsg": t.string().optional(),
            "currentIterationDetail": t.string().optional(),
            "failureLocation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoLoopMetadataOut"])
    types["GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationIn"] = t.struct(
        {"liftWhenExpired": t.boolean().optional(), "remindTime": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationIn"])
    types["GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "liftWhenExpired": t.boolean().optional(),
            "remindTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationOut"])
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
    types["EnterpriseCrmEventbusProtoStringArrayIn"] = t.struct(
        {"values": t.array(t.string())}
    ).named(renames["EnterpriseCrmEventbusProtoStringArrayIn"])
    types["EnterpriseCrmEventbusProtoStringArrayOut"] = t.struct(
        {
            "values": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoStringArrayOut"])
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
    types["GoogleCloudIntegrationsV1alphaIntegrationParameterIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "dataType": t.string().optional(),
            "searchable": t.boolean().optional(),
            "producer": t.string().optional(),
            "defaultValue": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaValueTypeIn"]
            ).optional(),
            "isTransient": t.boolean().optional(),
            "jsonSchema": t.string().optional(),
            "inputOutputType": t.string().optional(),
            "key": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationParameterIn"])
    types["GoogleCloudIntegrationsV1alphaIntegrationParameterOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "dataType": t.string().optional(),
            "searchable": t.boolean().optional(),
            "producer": t.string().optional(),
            "defaultValue": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaValueTypeOut"]
            ).optional(),
            "isTransient": t.boolean().optional(),
            "jsonSchema": t.string().optional(),
            "inputOutputType": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationParameterOut"])
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
    types["EnterpriseCrmEventbusProtoParamSpecEntryConfigIn"] = t.struct(
        {
            "parameterNameOption": t.string(),
            "subSectionLabel": t.string().optional(),
            "uiPlaceholderText": t.string().optional(),
            "helpText": t.string().optional(),
            "hideDefaultValue": t.boolean().optional(),
            "isHidden": t.boolean().optional(),
            "label": t.string().optional(),
            "inputDisplayOption": t.string(),
            "descriptivePhrase": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParamSpecEntryConfigIn"])
    types["EnterpriseCrmEventbusProtoParamSpecEntryConfigOut"] = t.struct(
        {
            "parameterNameOption": t.string(),
            "subSectionLabel": t.string().optional(),
            "uiPlaceholderText": t.string().optional(),
            "helpText": t.string().optional(),
            "hideDefaultValue": t.boolean().optional(),
            "isHidden": t.boolean().optional(),
            "label": t.string().optional(),
            "inputDisplayOption": t.string(),
            "descriptivePhrase": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParamSpecEntryConfigOut"])
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
    types["GoogleCloudConnectorsV1ConnectionIn"] = t.struct(
        {
            "sslConfig": t.proxy(
                renames["GoogleCloudConnectorsV1SslConfigIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "destinationConfigs": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1DestinationConfigIn"])
            ).optional(),
            "description": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "nodeConfig": t.proxy(
                renames["GoogleCloudConnectorsV1NodeConfigIn"]
            ).optional(),
            "logConfig": t.proxy(
                renames["GoogleCloudConnectorsV1LogConfigIn"]
            ).optional(),
            "authConfig": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigIn"]
            ).optional(),
            "suspended": t.boolean().optional(),
            "connectorVersion": t.string(),
            "configVariables": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConfigVariableIn"])
            ).optional(),
            "lockConfig": t.proxy(
                renames["GoogleCloudConnectorsV1LockConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1ConnectionIn"])
    types["GoogleCloudConnectorsV1ConnectionOut"] = t.struct(
        {
            "status": t.proxy(
                renames["GoogleCloudConnectorsV1ConnectionStatusOut"]
            ).optional(),
            "name": t.string().optional(),
            "sslConfig": t.proxy(
                renames["GoogleCloudConnectorsV1SslConfigOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "serviceDirectory": t.string().optional(),
            "destinationConfigs": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1DestinationConfigOut"])
            ).optional(),
            "description": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "updateTime": t.string().optional(),
            "nodeConfig": t.proxy(
                renames["GoogleCloudConnectorsV1NodeConfigOut"]
            ).optional(),
            "logConfig": t.proxy(
                renames["GoogleCloudConnectorsV1LogConfigOut"]
            ).optional(),
            "authConfig": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOut"]
            ).optional(),
            "envoyImageLocation": t.string().optional(),
            "imageLocation": t.string().optional(),
            "suspended": t.boolean().optional(),
            "connectorVersion": t.string(),
            "subscriptionType": t.string().optional(),
            "configVariables": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConfigVariableOut"])
            ).optional(),
            "lockConfig": t.proxy(
                renames["GoogleCloudConnectorsV1LockConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1ConnectionOut"])
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
    types["GoogleCloudIntegrationsV1alphaClientCertificateIn"] = t.struct(
        {
            "encryptedPrivateKey": t.string().optional(),
            "sslCertificate": t.string().optional(),
            "passphrase": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaClientCertificateIn"])
    types["GoogleCloudIntegrationsV1alphaClientCertificateOut"] = t.struct(
        {
            "encryptedPrivateKey": t.string().optional(),
            "sslCertificate": t.string().optional(),
            "passphrase": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaClientCertificateOut"])
    types["EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayIn"] = t.struct(
        {"booleanValues": t.array(t.boolean())}
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayIn"])
    types["EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayOut"] = t.struct(
        {
            "booleanValues": t.array(t.boolean()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayOut"])
    types["GoogleCloudIntegrationsV1alphaOidcTokenIn"] = t.struct(
        {
            "audience": t.string().optional(),
            "tokenExpireTime": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "token": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOidcTokenIn"])
    types["GoogleCloudIntegrationsV1alphaOidcTokenOut"] = t.struct(
        {
            "audience": t.string().optional(),
            "tokenExpireTime": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "token": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOidcTokenOut"])
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
    types["GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestIn"] = t.struct(
        {
            "parameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
            ).optional(),
            "executionId": t.string().optional(),
            "parameterEntries": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"])
            ).optional(),
            "inputParameters": t.struct({"_": t.string().optional()}).optional(),
            "triggerId": t.string(),
            "doNotPropagateError": t.boolean().optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestIn"])
    types["GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestOut"] = t.struct(
        {
            "parameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "executionId": t.string().optional(),
            "parameterEntries": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"])
            ).optional(),
            "inputParameters": t.struct({"_": t.string().optional()}).optional(),
            "triggerId": t.string(),
            "doNotPropagateError": t.boolean().optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestOut"])
    types["GoogleCloudConnectorsV1AuthConfigIn"] = t.struct(
        {
            "userPassword": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigUserPasswordIn"]
            ).optional(),
            "oauth2AuthCodeFlow": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowIn"]
            ).optional(),
            "authKey": t.string().optional(),
            "additionalVariables": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConfigVariableIn"])
            ).optional(),
            "oauth2JwtBearer": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerIn"]
            ).optional(),
            "authType": t.string().optional(),
            "sshPublicKey": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigSshPublicKeyIn"]
            ).optional(),
            "oauth2ClientCredentials": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigIn"])
    types["GoogleCloudConnectorsV1AuthConfigOut"] = t.struct(
        {
            "userPassword": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigUserPasswordOut"]
            ).optional(),
            "oauth2AuthCodeFlow": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowOut"]
            ).optional(),
            "authKey": t.string().optional(),
            "additionalVariables": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConfigVariableOut"])
            ).optional(),
            "oauth2JwtBearer": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerOut"]
            ).optional(),
            "authType": t.string().optional(),
            "sshPublicKey": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigSshPublicKeyOut"]
            ).optional(),
            "oauth2ClientCredentials": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigOut"])
    types["EnterpriseCrmEventbusProtoIntParameterArrayIn"] = t.struct(
        {"intValues": t.array(t.string())}
    ).named(renames["EnterpriseCrmEventbusProtoIntParameterArrayIn"])
    types["EnterpriseCrmEventbusProtoIntParameterArrayOut"] = t.struct(
        {
            "intValues": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoIntParameterArrayOut"])
    types["GoogleCloudIntegrationsV1alphaListCertificatesResponseIn"] = t.struct(
        {
            "certificates": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaCertificateIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListCertificatesResponseIn"])
    types["GoogleCloudIntegrationsV1alphaListCertificatesResponseOut"] = t.struct(
        {
            "certificates": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaCertificateOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListCertificatesResponseOut"])
    types["EnterpriseCrmEventbusProtoIntFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoIntFunctionIn"])
    types["EnterpriseCrmEventbusProtoIntFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoIntFunctionOut"])
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
    types["EnterpriseCrmEventbusProtoBooleanParameterArrayIn"] = t.struct(
        {"booleanValues": t.array(t.boolean())}
    ).named(renames["EnterpriseCrmEventbusProtoBooleanParameterArrayIn"])
    types["EnterpriseCrmEventbusProtoBooleanParameterArrayOut"] = t.struct(
        {
            "booleanValues": t.array(t.boolean()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBooleanParameterArrayOut"])
    types["GoogleCloudIntegrationsV1alphaExecutionDetailsIn"] = t.struct(
        {
            "state": t.string().optional(),
            "executionSnapshots": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaExecutionSnapshotIn"])
            ).optional(),
            "attemptStats": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaAttemptStatsIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecutionDetailsIn"])
    types["GoogleCloudIntegrationsV1alphaExecutionDetailsOut"] = t.struct(
        {
            "state": t.string().optional(),
            "executionSnapshots": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaExecutionSnapshotOut"])
            ).optional(),
            "attemptStats": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaAttemptStatsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecutionDetailsOut"])
    types["GoogleCloudIntegrationsV1alphaCancelExecutionResponseIn"] = t.struct(
        {"isCanceled": t.boolean().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaCancelExecutionResponseIn"])
    types["GoogleCloudIntegrationsV1alphaCancelExecutionResponseOut"] = t.struct(
        {
            "isCanceled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCancelExecutionResponseOut"])
    types["EnterpriseCrmEventbusProtoStringParameterArrayIn"] = t.struct(
        {"stringValues": t.array(t.string())}
    ).named(renames["EnterpriseCrmEventbusProtoStringParameterArrayIn"])
    types["EnterpriseCrmEventbusProtoStringParameterArrayOut"] = t.struct(
        {
            "stringValues": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoStringParameterArrayOut"])
    types["EnterpriseCrmEventbusProtoExecutionTraceInfoIn"] = t.struct(
        {
            "parentEventExecutionInfoId": t.string().optional(),
            "traceId": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoExecutionTraceInfoIn"])
    types["EnterpriseCrmEventbusProtoExecutionTraceInfoOut"] = t.struct(
        {
            "parentEventExecutionInfoId": t.string().optional(),
            "traceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoExecutionTraceInfoOut"])
    types["EnterpriseCrmEventbusProtoNextTaskIn"] = t.struct(
        {
            "taskNumber": t.string().optional(),
            "label": t.string().optional(),
            "combinedConditions": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoCombinedConditionIn"])
            ).optional(),
            "description": t.string().optional(),
            "taskConfigId": t.string().optional(),
            "condition": t.string().optional(),
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
            "taskConfigId": t.string().optional(),
            "condition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoNextTaskOut"])
    types["EnterpriseCrmEventbusProtoProtoArrayFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoProtoArrayFunctionIn"])
    types["EnterpriseCrmEventbusProtoProtoArrayFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoProtoArrayFunctionOut"])
    types["EnterpriseCrmEventbusProtoConditionResultIn"] = t.struct(
        {
            "currentTaskNumber": t.string().optional(),
            "result": t.boolean().optional(),
            "nextTaskNumber": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoConditionResultIn"])
    types["EnterpriseCrmEventbusProtoConditionResultOut"] = t.struct(
        {
            "currentTaskNumber": t.string().optional(),
            "result": t.boolean().optional(),
            "nextTaskNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoConditionResultOut"])
    types["GoogleCloudIntegrationsV1alphaAuthConfigIn"] = t.struct(
        {
            "credentialType": t.string().optional(),
            "overrideValidTime": t.string().optional(),
            "name": t.string().optional(),
            "reason": t.string().optional(),
            "expiryNotificationDuration": t.array(t.string()).optional(),
            "creatorEmail": t.string().optional(),
            "encryptedCredential": t.string().optional(),
            "decryptedCredential": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCredentialIn"]
            ).optional(),
            "description": t.string().optional(),
            "visibility": t.string().optional(),
            "lastModifierEmail": t.string().optional(),
            "validTime": t.string().optional(),
            "state": t.string().optional(),
            "displayName": t.string().optional(),
            "certificateId": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaAuthConfigIn"])
    types["GoogleCloudIntegrationsV1alphaAuthConfigOut"] = t.struct(
        {
            "credentialType": t.string().optional(),
            "overrideValidTime": t.string().optional(),
            "name": t.string().optional(),
            "reason": t.string().optional(),
            "expiryNotificationDuration": t.array(t.string()).optional(),
            "creatorEmail": t.string().optional(),
            "encryptedCredential": t.string().optional(),
            "decryptedCredential": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCredentialOut"]
            ).optional(),
            "description": t.string().optional(),
            "visibility": t.string().optional(),
            "lastModifierEmail": t.string().optional(),
            "updateTime": t.string().optional(),
            "validTime": t.string().optional(),
            "state": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "certificateId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaAuthConfigOut"])
    types["GoogleCloudConnectorsV1SecretIn"] = t.struct(
        {"secretVersion": t.string().optional()}
    ).named(renames["GoogleCloudConnectorsV1SecretIn"])
    types["GoogleCloudConnectorsV1SecretOut"] = t.struct(
        {
            "secretVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1SecretOut"])
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
    types["GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionIn"] = t.struct(
        {
            "teardown": t.proxy(
                renames["EnterpriseCrmEventbusProtoTeardownIn"]
            ).optional(),
            "parentIntegrationVersionId": t.string().optional(),
            "description": t.string().optional(),
            "lastModifierEmail": t.string().optional(),
            "userLabel": t.string().optional(),
            "triggerConfigs": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn"])
            ).optional(),
            "databasePersistencePolicy": t.string().optional(),
            "errorCatcherConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn"])
            ).optional(),
            "taskConfigs": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigIn"])
            ).optional(),
            "templateParameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn"]
            ).optional(),
            "status": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionIn"])
    types["GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "teardown": t.proxy(
                renames["EnterpriseCrmEventbusProtoTeardownOut"]
            ).optional(),
            "name": t.string().optional(),
            "parentIntegrationVersionId": t.string().optional(),
            "description": t.string().optional(),
            "lastModifierEmail": t.string().optional(),
            "userLabel": t.string().optional(),
            "triggerConfigs": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigOut"])
            ).optional(),
            "databasePersistencePolicy": t.string().optional(),
            "updateTime": t.string().optional(),
            "errorCatcherConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigOut"])
            ).optional(),
            "taskConfigs": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigOut"])
            ).optional(),
            "templateParameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersOut"]
            ).optional(),
            "status": t.string().optional(),
            "snapshotNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionOut"])
    types["EnterpriseCrmEventbusProtoTaskExecutionDetailsIn"] = t.struct(
        {
            "taskAttemptStats": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsIn"
                    ]
                )
            ),
            "taskExecutionState": t.string(),
            "taskNumber": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskExecutionDetailsIn"])
    types["EnterpriseCrmEventbusProtoTaskExecutionDetailsOut"] = t.struct(
        {
            "taskAttemptStats": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsOut"
                    ]
                )
            ),
            "taskExecutionState": t.string(),
            "taskNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskExecutionDetailsOut"])
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
    types["EnterpriseCrmEventbusProtoJsonFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoJsonFunctionIn"])
    types["EnterpriseCrmEventbusProtoJsonFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoJsonFunctionOut"])
    types["GoogleCloudIntegrationsV1alphaTaskExecutionDetailsIn"] = t.struct(
        {
            "taskAttemptStats": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaAttemptStatsIn"])
            ).optional(),
            "taskNumber": t.string().optional(),
            "taskExecutionState": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaTaskExecutionDetailsIn"])
    types["GoogleCloudIntegrationsV1alphaTaskExecutionDetailsOut"] = t.struct(
        {
            "taskAttemptStats": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaAttemptStatsOut"])
            ).optional(),
            "taskNumber": t.string().optional(),
            "taskExecutionState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaTaskExecutionDetailsOut"])
    types["EnterpriseCrmEventbusProtoValueTypeIn"] = t.struct(
        {
            "protoValue": t.struct({"_": t.string().optional()}),
            "doubleArray": t.proxy(renames["EnterpriseCrmEventbusProtoDoubleArrayIn"]),
            "intArray": t.proxy(renames["EnterpriseCrmEventbusProtoIntArrayIn"]),
            "stringValue": t.string(),
            "stringArray": t.proxy(renames["EnterpriseCrmEventbusProtoStringArrayIn"]),
            "intValue": t.string(),
            "booleanValue": t.boolean(),
            "doubleValue": t.number(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoValueTypeIn"])
    types["EnterpriseCrmEventbusProtoValueTypeOut"] = t.struct(
        {
            "protoValue": t.struct({"_": t.string().optional()}),
            "doubleArray": t.proxy(renames["EnterpriseCrmEventbusProtoDoubleArrayOut"]),
            "intArray": t.proxy(renames["EnterpriseCrmEventbusProtoIntArrayOut"]),
            "stringValue": t.string(),
            "stringArray": t.proxy(renames["EnterpriseCrmEventbusProtoStringArrayOut"]),
            "intValue": t.string(),
            "booleanValue": t.boolean(),
            "doubleValue": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoValueTypeOut"])
    types["EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryIn"] = t.struct(
        {
            "inOutType": t.string().optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn"]
            ).optional(),
            "isTransient": t.boolean().optional(),
            "attributes": t.proxy(
                renames["EnterpriseCrmEventbusProtoAttributesIn"]
            ).optional(),
            "dataType": t.string().optional(),
            "protoDefName": t.string().optional(),
            "name": t.string().optional(),
            "producer": t.string(),
            "children": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryIn"
                    ]
                )
            ).optional(),
            "protoDefPath": t.string().optional(),
            "producedBy": t.proxy(
                renames["EnterpriseCrmEventbusProtoNodeIdentifierIn"]
            ).optional(),
            "jsonSchema": t.string().optional(),
            "key": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryIn"])
    types["EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryOut"] = t.struct(
        {
            "inOutType": t.string().optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "isTransient": t.boolean().optional(),
            "attributes": t.proxy(
                renames["EnterpriseCrmEventbusProtoAttributesOut"]
            ).optional(),
            "dataType": t.string().optional(),
            "protoDefName": t.string().optional(),
            "name": t.string().optional(),
            "producer": t.string(),
            "children": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryOut"
                    ]
                )
            ).optional(),
            "protoDefPath": t.string().optional(),
            "producedBy": t.proxy(
                renames["EnterpriseCrmEventbusProtoNodeIdentifierOut"]
            ).optional(),
            "jsonSchema": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryOut"])
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
    types["EnterpriseCrmEventbusProtoBooleanFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoBooleanFunctionIn"])
    types["EnterpriseCrmEventbusProtoBooleanFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBooleanFunctionOut"])
    types["GoogleCloudIntegrationsV1alphaLiftSuspensionResponseIn"] = t.struct(
        {"eventExecutionInfoId": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaLiftSuspensionResponseIn"])
    types["GoogleCloudIntegrationsV1alphaLiftSuspensionResponseOut"] = t.struct(
        {
            "eventExecutionInfoId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaLiftSuspensionResponseOut"])
    types["EnterpriseCrmEventbusProtoBaseFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoBaseFunctionIn"])
    types["EnterpriseCrmEventbusProtoBaseFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBaseFunctionOut"])
    types["EnterpriseCrmEventbusProtoNextTeardownTaskIn"] = t.struct(
        {"name": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoNextTeardownTaskIn"])
    types["EnterpriseCrmEventbusProtoNextTeardownTaskOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EnterpriseCrmEventbusProtoNextTeardownTaskOut"])
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
    types["GoogleCloudIntegrationsV1alphaResolveSuspensionResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaResolveSuspensionResponseIn"])
    types["GoogleCloudIntegrationsV1alphaResolveSuspensionResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaResolveSuspensionResponseOut"])
    types["GoogleCloudIntegrationsV1alphaValueTypeIn"] = t.struct(
        {
            "doubleValue": t.number().optional(),
            "booleanValue": t.boolean().optional(),
            "booleanArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaBooleanParameterArrayIn"]
            ).optional(),
            "doubleArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaDoubleParameterArrayIn"]
            ).optional(),
            "stringValue": t.string().optional(),
            "stringArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaStringParameterArrayIn"]
            ).optional(),
            "intValue": t.string().optional(),
            "intArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaIntParameterArrayIn"]
            ).optional(),
            "jsonValue": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaValueTypeIn"])
    types["GoogleCloudIntegrationsV1alphaValueTypeOut"] = t.struct(
        {
            "doubleValue": t.number().optional(),
            "booleanValue": t.boolean().optional(),
            "booleanArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaBooleanParameterArrayOut"]
            ).optional(),
            "doubleArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaDoubleParameterArrayOut"]
            ).optional(),
            "stringValue": t.string().optional(),
            "stringArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaStringParameterArrayOut"]
            ).optional(),
            "intValue": t.string().optional(),
            "intArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaIntParameterArrayOut"]
            ).optional(),
            "jsonValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaValueTypeOut"])
    types["EnterpriseCrmEventbusProtoWorkflowAlertConfigIn"] = t.struct(
        {
            "metricType": t.string(),
            "thresholdValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueIn"]
            ).optional(),
            "aggregationPeriod": t.string().optional(),
            "numAggregationPeriods": t.integer().optional(),
            "clientId": t.string().optional(),
            "onlyFinalAttempt": t.boolean().optional(),
            "playbookUrl": t.string().optional(),
            "alertName": t.string().optional(),
            "thresholdType": t.string().optional(),
            "durationThresholdMs": t.string().optional(),
            "warningEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn"]
            ),
            "alertDisabled": t.boolean().optional(),
            "errorEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn"]
            ),
        }
    ).named(renames["EnterpriseCrmEventbusProtoWorkflowAlertConfigIn"])
    types["EnterpriseCrmEventbusProtoWorkflowAlertConfigOut"] = t.struct(
        {
            "metricType": t.string(),
            "thresholdValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueOut"]
            ).optional(),
            "aggregationPeriod": t.string().optional(),
            "numAggregationPeriods": t.integer().optional(),
            "clientId": t.string().optional(),
            "onlyFinalAttempt": t.boolean().optional(),
            "playbookUrl": t.string().optional(),
            "alertName": t.string().optional(),
            "thresholdType": t.string().optional(),
            "durationThresholdMs": t.string().optional(),
            "warningEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut"]
            ),
            "alertDisabled": t.boolean().optional(),
            "errorEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoWorkflowAlertConfigOut"])
    types["GoogleCloudIntegrationsV1alphaCancelExecutionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaCancelExecutionRequestIn"])
    types["GoogleCloudIntegrationsV1alphaCancelExecutionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaCancelExecutionRequestOut"])
    types["GoogleCloudIntegrationsV1alphaDoubleParameterArrayIn"] = t.struct(
        {"doubleValues": t.array(t.number()).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaDoubleParameterArrayIn"])
    types["GoogleCloudIntegrationsV1alphaDoubleParameterArrayOut"] = t.struct(
        {
            "doubleValues": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaDoubleParameterArrayOut"])
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
    types["EnterpriseCrmEventbusProtoCloudSchedulerConfigIn"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "serviceAccountEmail": t.string(),
            "cronTab": t.string(),
            "location": t.string(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoCloudSchedulerConfigIn"])
    types["EnterpriseCrmEventbusProtoCloudSchedulerConfigOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "serviceAccountEmail": t.string(),
            "cronTab": t.string(),
            "location": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoCloudSchedulerConfigOut"])
    types["EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamIn"] = t.struct(
        {
            "authConfigId": t.string().optional(),
            "scope": t.string().optional(),
            "allowedCredentialTypes": t.array(t.string()).optional(),
            "allowedServiceAccountInContext": t.boolean(),
            "useServiceAccountInContext": t.boolean(),
        }
    ).named(renames["EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamIn"])
    types["EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamOut"] = t.struct(
        {
            "authConfigId": t.string().optional(),
            "scope": t.string().optional(),
            "allowedCredentialTypes": t.array(t.string()).optional(),
            "allowedServiceAccountInContext": t.boolean(),
            "useServiceAccountInContext": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamOut"])
    types["EnterpriseCrmEventbusProtoScatterResponseIn"] = t.struct(
        {
            "isSuccessful": t.boolean().optional(),
            "responseParams": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoParameterEntryIn"])
            ).optional(),
            "executionIds": t.array(t.string()).optional(),
            "scatterElement": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeIn"]
            ).optional(),
            "errorMsg": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoScatterResponseIn"])
    types["EnterpriseCrmEventbusProtoScatterResponseOut"] = t.struct(
        {
            "isSuccessful": t.boolean().optional(),
            "responseParams": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoParameterEntryOut"])
            ).optional(),
            "executionIds": t.array(t.string()).optional(),
            "scatterElement": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "errorMsg": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoScatterResponseOut"])
    types["EnterpriseCrmEventbusProtoDoubleParameterArrayIn"] = t.struct(
        {"doubleValues": t.array(t.number())}
    ).named(renames["EnterpriseCrmEventbusProtoDoubleParameterArrayIn"])
    types["EnterpriseCrmEventbusProtoDoubleParameterArrayOut"] = t.struct(
        {
            "doubleValues": t.array(t.number()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoDoubleParameterArrayOut"])
    types["GoogleCloudConnectorsV1LogConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["GoogleCloudConnectorsV1LogConfigIn"])
    types["GoogleCloudConnectorsV1LogConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1LogConfigOut"])
    types[
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeIn"
    ] = t.struct({"max": t.string().optional(), "min": t.string().optional()}).named(
        renames["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeIn"]
    )
    types[
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeOut"
    ] = t.struct(
        {
            "max": t.string().optional(),
            "min": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeOut"]
    )
    types["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestIn"] = t.struct(
        {"scriptId": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestIn"])
    types["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestOut"] = t.struct(
        {
            "scriptId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestOut"])
    types["GoogleCloudConnectorsV1AuthConfigSshPublicKeyIn"] = t.struct(
        {
            "username": t.string().optional(),
            "certType": t.string().optional(),
            "sshClientCertPass": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
            "sshClientCert": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigSshPublicKeyIn"])
    types["GoogleCloudConnectorsV1AuthConfigSshPublicKeyOut"] = t.struct(
        {
            "username": t.string().optional(),
            "certType": t.string().optional(),
            "sshClientCertPass": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "sshClientCert": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigSshPublicKeyOut"])
    types["GoogleCloudIntegrationsV1alphaCredentialIn"] = t.struct(
        {
            "serviceAccountCredentials": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaServiceAccountCredentialsIn"]
            ).optional(),
            "usernameAndPassword": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaUsernameAndPasswordIn"]
            ).optional(),
            "oidcToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaOidcTokenIn"]
            ).optional(),
            "oauth2ClientCredentials": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsIn"]
            ).optional(),
            "authToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAuthTokenIn"]
            ).optional(),
            "oauth2ResourceOwnerCredentials": t.proxy(
                renames[
                    "GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsIn"
                ]
            ).optional(),
            "jwt": t.proxy(renames["GoogleCloudIntegrationsV1alphaJwtIn"]).optional(),
            "oauth2AuthorizationCode": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeIn"]
            ).optional(),
            "credentialType": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCredentialIn"])
    types["GoogleCloudIntegrationsV1alphaCredentialOut"] = t.struct(
        {
            "serviceAccountCredentials": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaServiceAccountCredentialsOut"]
            ).optional(),
            "usernameAndPassword": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaUsernameAndPasswordOut"]
            ).optional(),
            "oidcToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaOidcTokenOut"]
            ).optional(),
            "oauth2ClientCredentials": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsOut"]
            ).optional(),
            "authToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAuthTokenOut"]
            ).optional(),
            "oauth2ResourceOwnerCredentials": t.proxy(
                renames[
                    "GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsOut"
                ]
            ).optional(),
            "jwt": t.proxy(renames["GoogleCloudIntegrationsV1alphaJwtOut"]).optional(),
            "oauth2AuthorizationCode": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeOut"]
            ).optional(),
            "credentialType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCredentialOut"])
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
    types["EnterpriseCrmFrontendsEventbusProtoTaskEntityIn"] = t.struct(
        {
            "taskType": t.string().optional(),
            "stats": t.proxy(renames["EnterpriseCrmEventbusStatsIn"]).optional(),
            "metadata": t.proxy(
                renames["EnterpriseCrmEventbusProtoTaskMetadataIn"]
            ).optional(),
            "disabledForVpcSc": t.boolean().optional(),
            "paramSpecs": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageIn"]
            ).optional(),
            "uiConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoTaskUiConfigIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoTaskEntityIn"])
    types["EnterpriseCrmFrontendsEventbusProtoTaskEntityOut"] = t.struct(
        {
            "taskType": t.string().optional(),
            "stats": t.proxy(renames["EnterpriseCrmEventbusStatsOut"]).optional(),
            "metadata": t.proxy(
                renames["EnterpriseCrmEventbusProtoTaskMetadataOut"]
            ).optional(),
            "disabledForVpcSc": t.boolean().optional(),
            "paramSpecs": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageOut"]
            ).optional(),
            "uiConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoTaskUiConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoTaskEntityOut"])
    types["EnterpriseCrmEventbusProtoBooleanArrayFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoBooleanArrayFunctionIn"])
    types["EnterpriseCrmEventbusProtoBooleanArrayFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBooleanArrayFunctionOut"])
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
    types["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn"] = t.struct(
        {
            "stringArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoStringParameterArrayIn"]
            ),
            "serializedObjectValue": t.proxy(
                renames[
                    "EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterIn"
                ]
            ),
            "intArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoIntParameterArrayIn"]
            ),
            "intValue": t.string(),
            "doubleArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayIn"]
            ),
            "jsonValue": t.string(),
            "protoValue": t.struct({"_": t.string().optional()}),
            "stringValue": t.string(),
            "booleanValue": t.boolean(),
            "booleanArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayIn"]
            ),
            "protoArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayIn"]
            ),
            "doubleValue": t.number(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut"] = t.struct(
        {
            "stringArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoStringParameterArrayOut"]
            ),
            "serializedObjectValue": t.proxy(
                renames[
                    "EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterOut"
                ]
            ),
            "intArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoIntParameterArrayOut"]
            ),
            "intValue": t.string(),
            "doubleArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayOut"]
            ),
            "jsonValue": t.string(),
            "protoValue": t.struct({"_": t.string().optional()}),
            "stringValue": t.string(),
            "booleanValue": t.boolean(),
            "booleanArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayOut"]
            ),
            "protoArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayOut"]
            ),
            "doubleValue": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut"])
    types["EnterpriseCrmEventbusProtoTaskAlertConfigIn"] = t.struct(
        {
            "thresholdValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueIn"]
            ).optional(),
            "playbookUrl": t.string().optional(),
            "alertName": t.string().optional(),
            "durationThresholdMs": t.string().optional(),
            "clientId": t.string().optional(),
            "alertDisabled": t.boolean().optional(),
            "thresholdType": t.string().optional(),
            "numAggregationPeriods": t.integer().optional(),
            "onlyFinalAttempt": t.boolean().optional(),
            "warningEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn"]
            ),
            "metricType": t.string(),
            "aggregationPeriod": t.string().optional(),
            "errorEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn"]
            ),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskAlertConfigIn"])
    types["EnterpriseCrmEventbusProtoTaskAlertConfigOut"] = t.struct(
        {
            "thresholdValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueOut"]
            ).optional(),
            "playbookUrl": t.string().optional(),
            "alertName": t.string().optional(),
            "durationThresholdMs": t.string().optional(),
            "clientId": t.string().optional(),
            "alertDisabled": t.boolean().optional(),
            "thresholdType": t.string().optional(),
            "numAggregationPeriods": t.integer().optional(),
            "onlyFinalAttempt": t.boolean().optional(),
            "warningEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut"]
            ),
            "metricType": t.string(),
            "aggregationPeriod": t.string().optional(),
            "errorEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskAlertConfigOut"])
    types["EnterpriseCrmEventbusProtoExternalTrafficIn"] = t.struct(
        {
            "gcpProjectId": t.string().optional(),
            "source": t.string().optional(),
            "location": t.string().optional(),
            "gcpProjectNumber": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoExternalTrafficIn"])
    types["EnterpriseCrmEventbusProtoExternalTrafficOut"] = t.struct(
        {
            "gcpProjectId": t.string().optional(),
            "source": t.string().optional(),
            "location": t.string().optional(),
            "gcpProjectNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoExternalTrafficOut"])
    types["EnterpriseCrmFrontendsEventbusProtoTaskConfigIn"] = t.struct(
        {
            "successPolicy": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuccessPolicyIn"]
            ).optional(),
            "errorCatcherId": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "incomingEdgeCount": t.integer().optional(),
            "label": t.string().optional(),
            "preconditionLabel": t.string().optional(),
            "nextTasks": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoNextTaskIn"])
            ).optional(),
            "jsonValidationOption": t.string().optional(),
            "taskNumber": t.string().optional(),
            "taskExecutionStrategy": t.string().optional(),
            "synchronousCallFailurePolicy": t.proxy(
                renames["EnterpriseCrmEventbusProtoFailurePolicyIn"]
            ).optional(),
            "rollbackStrategy": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoRollbackStrategyIn"]
            ).optional(),
            "lastModifiedTime": t.string().optional(),
            "creatorEmail": t.string().optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "taskName": t.string().optional(),
            "disableStrictTypeValidation": t.boolean().optional(),
            "taskSpec": t.string().optional(),
            "alertConfigs": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskAlertConfigIn"])
            ).optional(),
            "taskType": t.string().optional(),
            "taskEntity": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoTaskEntityIn"]
            ).optional(),
            "failurePolicy": t.proxy(
                renames["EnterpriseCrmEventbusProtoFailurePolicyIn"]
            ).optional(),
            "taskTemplateName": t.string().optional(),
            "position": t.proxy(
                renames["EnterpriseCrmEventbusProtoCoordinateIn"]
            ).optional(),
            "precondition": t.string().optional(),
            "externalTaskType": t.string(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigIn"])
    types["EnterpriseCrmFrontendsEventbusProtoTaskConfigOut"] = t.struct(
        {
            "successPolicy": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuccessPolicyOut"]
            ).optional(),
            "errorCatcherId": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "incomingEdgeCount": t.integer().optional(),
            "label": t.string().optional(),
            "preconditionLabel": t.string().optional(),
            "nextTasks": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoNextTaskOut"])
            ).optional(),
            "jsonValidationOption": t.string().optional(),
            "taskNumber": t.string().optional(),
            "taskExecutionStrategy": t.string().optional(),
            "synchronousCallFailurePolicy": t.proxy(
                renames["EnterpriseCrmEventbusProtoFailurePolicyOut"]
            ).optional(),
            "rollbackStrategy": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoRollbackStrategyOut"]
            ).optional(),
            "lastModifiedTime": t.string().optional(),
            "creatorEmail": t.string().optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "taskName": t.string().optional(),
            "disableStrictTypeValidation": t.boolean().optional(),
            "taskSpec": t.string().optional(),
            "alertConfigs": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskAlertConfigOut"])
            ).optional(),
            "taskType": t.string().optional(),
            "taskEntity": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoTaskEntityOut"]
            ).optional(),
            "failurePolicy": t.proxy(
                renames["EnterpriseCrmEventbusProtoFailurePolicyOut"]
            ).optional(),
            "taskTemplateName": t.string().optional(),
            "position": t.proxy(
                renames["EnterpriseCrmEventbusProtoCoordinateOut"]
            ).optional(),
            "precondition": t.string().optional(),
            "externalTaskType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigOut"])
    types["EnterpriseCrmEventbusProtoProtoFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoProtoFunctionIn"])
    types["EnterpriseCrmEventbusProtoProtoFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoProtoFunctionOut"])
    types["EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn"] = t.struct(
        {
            "triggerId": t.string().optional(),
            "description": t.string().optional(),
            "label": t.string().optional(),
            "enabledClients": t.array(t.string()),
            "cloudSchedulerConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoCloudSchedulerConfigIn"]
            ),
            "pauseWorkflowExecutions": t.boolean().optional(),
            "triggerNumber": t.string(),
            "alertConfig": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoWorkflowAlertConfigIn"])
            ).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "startTasks": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoNextTaskIn"])
            ).optional(),
            "triggerCriteria": t.proxy(
                renames["EnterpriseCrmEventbusProtoTriggerCriteriaIn"]
            ).optional(),
            "triggerType": t.string(),
            "position": t.proxy(
                renames["EnterpriseCrmEventbusProtoCoordinateIn"]
            ).optional(),
            "errorCatcherId": t.string().optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn"])
    types["EnterpriseCrmFrontendsEventbusProtoTriggerConfigOut"] = t.struct(
        {
            "triggerId": t.string().optional(),
            "description": t.string().optional(),
            "label": t.string().optional(),
            "enabledClients": t.array(t.string()),
            "cloudSchedulerConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoCloudSchedulerConfigOut"]
            ),
            "pauseWorkflowExecutions": t.boolean().optional(),
            "triggerNumber": t.string(),
            "alertConfig": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoWorkflowAlertConfigOut"])
            ).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "startTasks": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoNextTaskOut"])
            ).optional(),
            "triggerCriteria": t.proxy(
                renames["EnterpriseCrmEventbusProtoTriggerCriteriaOut"]
            ).optional(),
            "triggerType": t.string(),
            "position": t.proxy(
                renames["EnterpriseCrmEventbusProtoCoordinateOut"]
            ).optional(),
            "errorCatcherId": t.string().optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigOut"])
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
    types["EnterpriseCrmEventbusProtoAttributesIn"] = t.struct(
        {
            "searchable": t.string(),
            "taskVisibility": t.array(t.string()).optional(),
            "isSearchable": t.boolean().optional(),
            "dataType": t.string().optional(),
            "logSettings": t.proxy(
                renames["EnterpriseCrmEventbusProtoLogSettingsIn"]
            ).optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoValueTypeIn"]
            ).optional(),
            "isRequired": t.boolean(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoAttributesIn"])
    types["EnterpriseCrmEventbusProtoAttributesOut"] = t.struct(
        {
            "searchable": t.string(),
            "taskVisibility": t.array(t.string()).optional(),
            "isSearchable": t.boolean().optional(),
            "dataType": t.string().optional(),
            "logSettings": t.proxy(
                renames["EnterpriseCrmEventbusProtoLogSettingsOut"]
            ).optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoValueTypeOut"]
            ).optional(),
            "isRequired": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoAttributesOut"])
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
    types["GoogleCloudIntegrationsV1alphaGenerateTokenResponseIn"] = t.struct(
        {"message": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaGenerateTokenResponseIn"])
    types["GoogleCloudIntegrationsV1alphaGenerateTokenResponseOut"] = t.struct(
        {
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaGenerateTokenResponseOut"])
    types["GoogleCloudIntegrationsV1alphaTaskConfigIn"] = t.struct(
        {
            "synchronousCallFailurePolicy": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaFailurePolicyIn"]
            ).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "failurePolicy": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaFailurePolicyIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "jsonValidationOption": t.string().optional(),
            "successPolicy": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuccessPolicyIn"]
            ).optional(),
            "description": t.string().optional(),
            "taskExecutionStrategy": t.string().optional(),
            "taskTemplate": t.string().optional(),
            "task": t.string().optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCoordinateIn"]
            ).optional(),
            "externalTaskType": t.string().optional(),
            "nextTasks": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaNextTaskIn"])
            ).optional(),
            "errorCatcherId": t.string().optional(),
            "taskId": t.string(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaTaskConfigIn"])
    types["GoogleCloudIntegrationsV1alphaTaskConfigOut"] = t.struct(
        {
            "synchronousCallFailurePolicy": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaFailurePolicyOut"]
            ).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "failurePolicy": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaFailurePolicyOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "jsonValidationOption": t.string().optional(),
            "successPolicy": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuccessPolicyOut"]
            ).optional(),
            "description": t.string().optional(),
            "taskExecutionStrategy": t.string().optional(),
            "taskTemplate": t.string().optional(),
            "task": t.string().optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCoordinateOut"]
            ).optional(),
            "externalTaskType": t.string().optional(),
            "nextTasks": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaNextTaskOut"])
            ).optional(),
            "errorCatcherId": t.string().optional(),
            "taskId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaTaskConfigOut"])
    types["GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseIn"] = t.struct(
        {"executionInfoIds": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseIn"])
    types["GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseOut"] = t.struct(
        {
            "executionInfoIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseOut"])
    types["GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn"] = t.struct(
        {
            "errorCatcherNumber": t.string(),
            "errorCatcherId": t.string(),
            "description": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCoordinateIn"]
            ).optional(),
            "startErrorTasks": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaNextTaskIn"])
            ),
            "label": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn"])
    types["GoogleCloudIntegrationsV1alphaErrorCatcherConfigOut"] = t.struct(
        {
            "errorCatcherNumber": t.string(),
            "errorCatcherId": t.string(),
            "description": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCoordinateOut"]
            ).optional(),
            "startErrorTasks": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaNextTaskOut"])
            ),
            "label": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigOut"])
    types["GoogleCloudIntegrationsV1alphaAccessTokenIn"] = t.struct(
        {
            "refreshToken": t.string().optional(),
            "refreshTokenExpireTime": t.string().optional(),
            "tokenType": t.string().optional(),
            "accessToken": t.string().optional(),
            "accessTokenExpireTime": t.string(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaAccessTokenIn"])
    types["GoogleCloudIntegrationsV1alphaAccessTokenOut"] = t.struct(
        {
            "refreshToken": t.string().optional(),
            "refreshTokenExpireTime": t.string().optional(),
            "tokenType": t.string().optional(),
            "accessToken": t.string().optional(),
            "accessTokenExpireTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaAccessTokenOut"])
    types["EnterpriseCrmFrontendsEventbusProtoRollbackStrategyIn"] = t.struct(
        {
            "parameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
            ).optional(),
            "rollbackTaskImplementationClassName": t.string(),
            "taskNumbersToRollback": t.array(t.string()),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoRollbackStrategyIn"])
    types["EnterpriseCrmFrontendsEventbusProtoRollbackStrategyOut"] = t.struct(
        {
            "parameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "rollbackTaskImplementationClassName": t.string(),
            "taskNumbersToRollback": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoRollbackStrategyOut"])
    types["EnterpriseCrmEventbusProtoNotificationIn"] = t.struct(
        {
            "pubsubTopic": t.string(),
            "buganizerNotification": t.proxy(
                renames["EnterpriseCrmEventbusProtoBuganizerNotificationIn"]
            ),
            "emailAddress": t.proxy(renames["EnterpriseCrmEventbusProtoAddressIn"]),
            "request": t.proxy(
                renames["EnterpriseCrmEventbusProtoCustomSuspensionRequestIn"]
            ).optional(),
            "escalatorQueue": t.string(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoNotificationIn"])
    types["EnterpriseCrmEventbusProtoNotificationOut"] = t.struct(
        {
            "pubsubTopic": t.string(),
            "buganizerNotification": t.proxy(
                renames["EnterpriseCrmEventbusProtoBuganizerNotificationOut"]
            ),
            "emailAddress": t.proxy(renames["EnterpriseCrmEventbusProtoAddressOut"]),
            "request": t.proxy(
                renames["EnterpriseCrmEventbusProtoCustomSuspensionRequestOut"]
            ).optional(),
            "escalatorQueue": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoNotificationOut"])
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
    types["EnterpriseCrmEventbusProtoSuccessPolicyIn"] = t.struct(
        {"finalState": t.string().optional()}
    ).named(renames["EnterpriseCrmEventbusProtoSuccessPolicyIn"])
    types["EnterpriseCrmEventbusProtoSuccessPolicyOut"] = t.struct(
        {
            "finalState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuccessPolicyOut"])
    types["EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayIn"] = t.struct(
        {"protoValues": t.array(t.struct({"_": t.string().optional()}))}
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayIn"])
    types["EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayOut"] = t.struct(
        {
            "protoValues": t.array(t.struct({"_": t.string().optional()})),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayOut"])
    types["EnterpriseCrmEventbusStatsDimensionsIn"] = t.struct(
        {
            "workflowId": t.string(),
            "taskName": t.string(),
            "warningEnumString": t.string(),
            "taskNumber": t.string(),
            "errorEnumString": t.string(),
            "enumFilterType": t.string().optional(),
            "triggerId": t.string().optional(),
            "workflowName": t.string(),
            "clientId": t.string(),
            "retryAttempt": t.string(),
        }
    ).named(renames["EnterpriseCrmEventbusStatsDimensionsIn"])
    types["EnterpriseCrmEventbusStatsDimensionsOut"] = t.struct(
        {
            "workflowId": t.string(),
            "taskName": t.string(),
            "warningEnumString": t.string(),
            "taskNumber": t.string(),
            "errorEnumString": t.string(),
            "enumFilterType": t.string().optional(),
            "triggerId": t.string().optional(),
            "workflowName": t.string(),
            "clientId": t.string(),
            "retryAttempt": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusStatsDimensionsOut"])
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
    types["EnterpriseCrmEventbusProtoErrorDetailIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "errorMessage": t.string().optional(),
            "errorCode": t.proxy(renames["CrmlogErrorCodeIn"]).optional(),
            "taskNumber": t.integer().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoErrorDetailIn"])
    types["EnterpriseCrmEventbusProtoErrorDetailOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "errorMessage": t.string().optional(),
            "errorCode": t.proxy(renames["CrmlogErrorCodeOut"]).optional(),
            "taskNumber": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoErrorDetailOut"])
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
    types["EnterpriseCrmEventbusProtoBuganizerNotificationIn"] = t.struct(
        {
            "assigneeEmailAddress": t.string().optional(),
            "title": t.string().optional(),
            "templateId": t.string().optional(),
            "componentId": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBuganizerNotificationIn"])
    types["EnterpriseCrmEventbusProtoBuganizerNotificationOut"] = t.struct(
        {
            "assigneeEmailAddress": t.string().optional(),
            "title": t.string().optional(),
            "templateId": t.string().optional(),
            "componentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBuganizerNotificationOut"])
    types["EnterpriseCrmEventbusProtoEventExecutionDetailsIn"] = t.struct(
        {
            "eventExecutionSnapshot": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoEventExecutionSnapshotIn"])
            ),
            "logFilePath": t.string().optional(),
            "nextExecutionTime": t.string().optional(),
            "eventAttemptStats": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsIn"
                    ]
                )
            ),
            "ryeLockUnheldCount": t.integer().optional(),
            "networkAddress": t.string().optional(),
            "eventRetriesFromBeginningCount": t.integer().optional(),
            "eventExecutionState": t.string(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoEventExecutionDetailsIn"])
    types["EnterpriseCrmEventbusProtoEventExecutionDetailsOut"] = t.struct(
        {
            "eventExecutionSnapshot": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoEventExecutionSnapshotOut"])
            ),
            "logFilePath": t.string().optional(),
            "nextExecutionTime": t.string().optional(),
            "eventAttemptStats": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsOut"
                    ]
                )
            ),
            "ryeLockUnheldCount": t.integer().optional(),
            "networkAddress": t.string().optional(),
            "eventRetriesFromBeginningCount": t.integer().optional(),
            "eventExecutionState": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoEventExecutionDetailsOut"])
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
    types["GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaIn"] = t.struct(
        {
            "arrayFieldSchema": t.string().optional(),
            "entity": t.string().optional(),
            "fieldSchema": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaIn"])
    types["GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaOut"] = t.struct(
        {
            "arrayFieldSchema": t.string().optional(),
            "entity": t.string().optional(),
            "fieldSchema": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaOut"])
    types["EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoIn"] = t.struct(
        {
            "executionTraceInfo": t.proxy(
                renames["EnterpriseCrmEventbusProtoExecutionTraceInfoIn"]
            ).optional(),
            "workflowId": t.string(),
            "eventExecutionInfoId": t.string().optional(),
            "workflowRetryBackoffIntervalSeconds": t.string().optional(),
            "workflowName": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "createTime": t.string().optional(),
            "responseParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
            ).optional(),
            "errors": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoErrorDetailIn"])
            ).optional(),
            "eventExecutionDetails": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsIn"]
            ).optional(),
            "triggerId": t.string().optional(),
            "postMethod": t.string().optional(),
            "tenant": t.string().optional(),
            "requestParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
            ).optional(),
            "errorCode": t.proxy(renames["CrmlogErrorCodeIn"]).optional(),
            "product": t.string().optional(),
            "snapshotNumber": t.string().optional(),
            "clientId": t.string().optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoIn"])
    types["EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoOut"] = t.struct(
        {
            "executionTraceInfo": t.proxy(
                renames["EnterpriseCrmEventbusProtoExecutionTraceInfoOut"]
            ).optional(),
            "workflowId": t.string(),
            "eventExecutionInfoId": t.string().optional(),
            "workflowRetryBackoffIntervalSeconds": t.string().optional(),
            "workflowName": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "createTime": t.string().optional(),
            "responseParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "errors": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoErrorDetailOut"])
            ).optional(),
            "eventExecutionDetails": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsOut"]
            ).optional(),
            "triggerId": t.string().optional(),
            "postMethod": t.string().optional(),
            "tenant": t.string().optional(),
            "requestParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "errorCode": t.proxy(renames["CrmlogErrorCodeOut"]).optional(),
            "product": t.string().optional(),
            "snapshotNumber": t.string().optional(),
            "clientId": t.string().optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoOut"])
    types["EnterpriseCrmEventbusProtoTriggerCriteriaIn"] = t.struct(
        {
            "condition": t.string(),
            "triggerCriteriaTaskImplementationClassName": t.string().optional(),
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTriggerCriteriaIn"])
    types["EnterpriseCrmEventbusProtoTriggerCriteriaOut"] = t.struct(
        {
            "condition": t.string(),
            "triggerCriteriaTaskImplementationClassName": t.string().optional(),
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTriggerCriteriaOut"])
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
    types["GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestIn"])
    types["GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestOut"])
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
    types["GoogleCloudIntegrationsV1alphaCloudSchedulerConfigIn"] = t.struct(
        {
            "location": t.string(),
            "errorMessage": t.string().optional(),
            "cronTab": t.string(),
            "serviceAccountEmail": t.string(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCloudSchedulerConfigIn"])
    types["GoogleCloudIntegrationsV1alphaCloudSchedulerConfigOut"] = t.struct(
        {
            "location": t.string(),
            "errorMessage": t.string().optional(),
            "cronTab": t.string(),
            "serviceAccountEmail": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCloudSchedulerConfigOut"])
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
    types["EnterpriseCrmEventbusProtoDoubleArrayFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoDoubleArrayFunctionIn"])
    types["EnterpriseCrmEventbusProtoDoubleArrayFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoDoubleArrayFunctionOut"])
    types["GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeIn"] = t.struct(
        {
            "accessToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAccessTokenIn"]
            ).optional(),
            "authParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapIn"]
            ).optional(),
            "authCode": t.string().optional(),
            "requestType": t.string().optional(),
            "clientId": t.string().optional(),
            "tokenEndpoint": t.string().optional(),
            "applyReauthPolicy": t.boolean().optional(),
            "clientSecret": t.string().optional(),
            "tokenParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapIn"]
            ).optional(),
            "authEndpoint": t.string().optional(),
            "scope": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeIn"])
    types["GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeOut"] = t.struct(
        {
            "accessToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAccessTokenOut"]
            ).optional(),
            "authParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapOut"]
            ).optional(),
            "authCode": t.string().optional(),
            "requestType": t.string().optional(),
            "clientId": t.string().optional(),
            "tokenEndpoint": t.string().optional(),
            "applyReauthPolicy": t.boolean().optional(),
            "clientSecret": t.string().optional(),
            "tokenParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapOut"]
            ).optional(),
            "authEndpoint": t.string().optional(),
            "scope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeOut"])
    types["EnterpriseCrmEventbusProtoSuspensionAuthPermissionsIn"] = t.struct(
        {
            "loasRole": t.string(),
            "gaiaIdentity": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityIn"
                ]
            ).optional(),
            "mdbGroup": t.string(),
            "googleGroup": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityIn"
                ]
            ),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionAuthPermissionsIn"])
    types["EnterpriseCrmEventbusProtoSuspensionAuthPermissionsOut"] = t.struct(
        {
            "loasRole": t.string(),
            "gaiaIdentity": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityOut"
                ]
            ).optional(),
            "mdbGroup": t.string(),
            "googleGroup": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityOut"
                ]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionAuthPermissionsOut"])
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
    types["GoogleCloudIntegrationsV1alphaParameterMapIn"] = t.struct(
        {
            "valueType": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaParameterMapEntryIn"])
            ).optional(),
            "keyType": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaParameterMapIn"])
    types["GoogleCloudIntegrationsV1alphaParameterMapOut"] = t.struct(
        {
            "valueType": t.string().optional(),
            "entries": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaParameterMapEntryOut"])
            ).optional(),
            "keyType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaParameterMapOut"])
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
    types["EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotIn"] = t.struct(
        {
            "eventParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
            ).optional(),
            "taskName": t.string().optional(),
            "eventExecutionInfoId": t.string().optional(),
            "conditionResults": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoConditionResultIn"])
            ).optional(),
            "diffParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
            ).optional(),
            "eventExecutionSnapshotId": t.string().optional(),
            "checkpointTaskNumber": t.string().optional(),
            "snapshotTime": t.string().optional(),
            "eventExecutionSnapshotMetadata": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataIn"
                ]
            ),
            "taskExecutionDetails": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskExecutionDetailsIn"])
            ).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotIn"])
    types["EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotOut"] = t.struct(
        {
            "eventParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "taskName": t.string().optional(),
            "eventExecutionInfoId": t.string().optional(),
            "conditionResults": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoConditionResultOut"])
            ).optional(),
            "diffParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "eventExecutionSnapshotId": t.string().optional(),
            "checkpointTaskNumber": t.string().optional(),
            "snapshotTime": t.string().optional(),
            "eventExecutionSnapshotMetadata": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataOut"
                ]
            ),
            "taskExecutionDetails": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskExecutionDetailsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotOut"])
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
    types["EnterpriseCrmEventbusProtoIntArrayFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoIntArrayFunctionIn"])
    types["EnterpriseCrmEventbusProtoIntArrayFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoIntArrayFunctionOut"])
    types["EnterpriseCrmFrontendsEventbusProtoIntParameterArrayIn"] = t.struct(
        {"intValues": t.array(t.string())}
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoIntParameterArrayIn"])
    types["EnterpriseCrmFrontendsEventbusProtoIntParameterArrayOut"] = t.struct(
        {
            "intValues": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoIntParameterArrayOut"])
    types["GoogleCloudConnectorsV1ConfigVariableIn"] = t.struct(
        {
            "stringValue": t.string().optional(),
            "intValue": t.string().optional(),
            "secretValue": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
            "boolValue": t.boolean().optional(),
            "key": t.string().optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1ConfigVariableIn"])
    types["GoogleCloudConnectorsV1ConfigVariableOut"] = t.struct(
        {
            "stringValue": t.string().optional(),
            "intValue": t.string().optional(),
            "secretValue": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "boolValue": t.boolean().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1ConfigVariableOut"])
    types["GoogleCloudIntegrationsV1alphaLiftSuspensionRequestIn"] = t.struct(
        {"suspensionResult": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaLiftSuspensionRequestIn"])
    types["GoogleCloudIntegrationsV1alphaLiftSuspensionRequestOut"] = t.struct(
        {
            "suspensionResult": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaLiftSuspensionRequestOut"])
    types["GoogleCloudIntegrationsV1alphaSfdcChannelIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "channelTopic": t.string().optional(),
            "name": t.string().optional(),
            "lastReplayId": t.string().optional(),
            "description": t.string().optional(),
            "isActive": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSfdcChannelIn"])
    types["GoogleCloudIntegrationsV1alphaSfdcChannelOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "channelTopic": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "lastReplayId": t.string().optional(),
            "updateTime": t.string().optional(),
            "deleteTime": t.string().optional(),
            "description": t.string().optional(),
            "isActive": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"])
    types["EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditIn"] = t.struct(
        {"resolvedByCpi": t.string(), "resolvedBy": t.string(), "timestamp": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditIn"])
    types["EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditOut"] = t.struct(
        {
            "resolvedByCpi": t.string(),
            "resolvedBy": t.string(),
            "timestamp": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditOut"])
    types["EnterpriseCrmEventbusProtoLogSettingsIn"] = t.struct(
        {
            "seedScope": t.string(),
            "seedPeriod": t.string(),
            "sanitizeOptions": t.proxy(
                renames["EnterpriseCrmLoggingGwsSanitizeOptionsIn"]
            ).optional(),
            "logFieldName": t.string().optional(),
            "shorteningLimits": t.proxy(
                renames["EnterpriseCrmLoggingGwsFieldLimitsIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoLogSettingsIn"])
    types["EnterpriseCrmEventbusProtoLogSettingsOut"] = t.struct(
        {
            "seedScope": t.string(),
            "seedPeriod": t.string(),
            "sanitizeOptions": t.proxy(
                renames["EnterpriseCrmLoggingGwsSanitizeOptionsOut"]
            ).optional(),
            "logFieldName": t.string().optional(),
            "shorteningLimits": t.proxy(
                renames["EnterpriseCrmLoggingGwsFieldLimitsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoLogSettingsOut"])
    types["EnterpriseCrmLoggingGwsFieldLimitsIn"] = t.struct(
        {
            "logAction": t.string(),
            "maxStringLength": t.integer().optional(),
            "maxArraySize": t.integer().optional(),
            "logType": t.array(t.string()).optional(),
            "shortenerType": t.string(),
        }
    ).named(renames["EnterpriseCrmLoggingGwsFieldLimitsIn"])
    types["EnterpriseCrmLoggingGwsFieldLimitsOut"] = t.struct(
        {
            "logAction": t.string(),
            "maxStringLength": t.integer().optional(),
            "maxArraySize": t.integer().optional(),
            "logType": t.array(t.string()).optional(),
            "shortenerType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmLoggingGwsFieldLimitsOut"])
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
    types["EnterpriseCrmFrontendsEventbusProtoStringParameterArrayIn"] = t.struct(
        {"stringValues": t.array(t.string())}
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoStringParameterArrayIn"])
    types["EnterpriseCrmFrontendsEventbusProtoStringParameterArrayOut"] = t.struct(
        {
            "stringValues": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoStringParameterArrayOut"])
    types["GoogleCloudIntegrationsV1alphaSuspensionIn"] = t.struct(
        {
            "taskId": t.string(),
            "suspensionConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionConfigIn"]
            ).optional(),
            "audit": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuspensionAuditIn"]
            ).optional(),
            "name": t.string().optional(),
            "integration": t.string(),
            "state": t.string(),
            "approvalConfig": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigIn"]
            ).optional(),
            "eventExecutionInfoId": t.string(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSuspensionIn"])
    types["GoogleCloudIntegrationsV1alphaSuspensionOut"] = t.struct(
        {
            "taskId": t.string(),
            "suspensionConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionConfigOut"]
            ).optional(),
            "audit": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuspensionAuditOut"]
            ).optional(),
            "lastModifyTime": t.string().optional(),
            "name": t.string().optional(),
            "integration": t.string(),
            "state": t.string(),
            "approvalConfig": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigOut"]
            ).optional(),
            "eventExecutionInfoId": t.string(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSuspensionOut"])
    types["GoogleCloudIntegrationsV1alphaExecutionSnapshotIn"] = t.struct(
        {
            "taskExecutionDetails": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaTaskExecutionDetailsIn"])
            ).optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "executionSnapshotMetadata": t.proxy(
                renames[
                    "GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataIn"
                ]
            ).optional(),
            "checkpointTaskNumber": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecutionSnapshotIn"])
    types["GoogleCloudIntegrationsV1alphaExecutionSnapshotOut"] = t.struct(
        {
            "taskExecutionDetails": t.array(
                t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaTaskExecutionDetailsOut"]
                )
            ).optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "executionSnapshotMetadata": t.proxy(
                renames[
                    "GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataOut"
                ]
            ).optional(),
            "checkpointTaskNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecutionSnapshotOut"])
    types["EnterpriseCrmEventbusProtoTaskUiModuleConfigIn"] = t.struct(
        {"moduleId": t.string().optional()}
    ).named(renames["EnterpriseCrmEventbusProtoTaskUiModuleConfigIn"])
    types["EnterpriseCrmEventbusProtoTaskUiModuleConfigOut"] = t.struct(
        {
            "moduleId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskUiModuleConfigOut"])
    types["EnterpriseCrmEventbusProtoFieldIn"] = t.struct(
        {
            "referenceKey": t.string().optional(),
            "fieldType": t.string().optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeIn"]
            ).optional(),
            "cardinality": t.string().optional(),
            "protoDefPath": t.string().optional(),
            "transformExpression": t.proxy(
                renames["EnterpriseCrmEventbusProtoTransformExpressionIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFieldIn"])
    types["EnterpriseCrmEventbusProtoFieldOut"] = t.struct(
        {
            "referenceKey": t.string().optional(),
            "fieldType": t.string().optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "cardinality": t.string().optional(),
            "protoDefPath": t.string().optional(),
            "transformExpression": t.proxy(
                renames["EnterpriseCrmEventbusProtoTransformExpressionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFieldOut"])
    types["EnterpriseCrmEventbusProtoSuspensionResolutionInfoIn"] = t.struct(
        {
            "createdTimestamp": t.string().optional(),
            "encryptedSuspensionResolutionInfo": t.string().optional(),
            "status": t.string(),
            "clientId": t.string().optional(),
            "product": t.string().optional(),
            "suspensionConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionConfigIn"]
            ),
            "wrappedDek": t.string().optional(),
            "suspensionId": t.string().optional(),
            "externalTraffic": t.proxy(
                renames["EnterpriseCrmEventbusProtoExternalTrafficIn"]
            ).optional(),
            "lastModifiedTimestamp": t.string().optional(),
            "audit": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditIn"]
            ),
            "eventExecutionInfoId": t.string(),
            "workflowName": t.string(),
            "taskNumber": t.string(),
            "cloudKmsConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoCloudKmsConfigIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionResolutionInfoIn"])
    types["EnterpriseCrmEventbusProtoSuspensionResolutionInfoOut"] = t.struct(
        {
            "createdTimestamp": t.string().optional(),
            "encryptedSuspensionResolutionInfo": t.string().optional(),
            "status": t.string(),
            "clientId": t.string().optional(),
            "product": t.string().optional(),
            "suspensionConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionConfigOut"]
            ),
            "wrappedDek": t.string().optional(),
            "suspensionId": t.string().optional(),
            "externalTraffic": t.proxy(
                renames["EnterpriseCrmEventbusProtoExternalTrafficOut"]
            ).optional(),
            "lastModifiedTimestamp": t.string().optional(),
            "audit": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditOut"]
            ),
            "eventExecutionInfoId": t.string(),
            "workflowName": t.string(),
            "taskNumber": t.string(),
            "cloudKmsConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoCloudKmsConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionResolutionInfoOut"])
    types["EnterpriseCrmEventbusProtoEventExecutionSnapshotIn"] = t.struct(
        {
            "conditionResults": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoConditionResultIn"])
            ).optional(),
            "exceedMaxSize": t.boolean().optional(),
            "eventExecutionSnapshotId": t.string().optional(),
            "snapshotTime": t.string().optional(),
            "eventExecutionSnapshotMetadata": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataIn"
                ]
            ),
            "taskExecutionDetails": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskExecutionDetailsIn"])
            ).optional(),
            "checkpointTaskNumber": t.string().optional(),
            "eventExecutionInfoId": t.string().optional(),
            "taskName": t.string().optional(),
            "eventParams": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersIn"]
            ).optional(),
            "diffParams": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoEventExecutionSnapshotIn"])
    types["EnterpriseCrmEventbusProtoEventExecutionSnapshotOut"] = t.struct(
        {
            "conditionResults": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoConditionResultOut"])
            ).optional(),
            "exceedMaxSize": t.boolean().optional(),
            "eventExecutionSnapshotId": t.string().optional(),
            "snapshotTime": t.string().optional(),
            "eventExecutionSnapshotMetadata": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataOut"
                ]
            ),
            "taskExecutionDetails": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskExecutionDetailsOut"])
            ).optional(),
            "checkpointTaskNumber": t.string().optional(),
            "eventExecutionInfoId": t.string().optional(),
            "taskName": t.string().optional(),
            "eventParams": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersOut"]
            ).optional(),
            "diffParams": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoEventExecutionSnapshotOut"])
    types["GoogleCloudIntegrationsV1alphaJwtIn"] = t.struct(
        {
            "jwtHeader": t.string().optional(),
            "jwt": t.string().optional(),
            "secret": t.string().optional(),
            "jwtPayload": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaJwtIn"])
    types["GoogleCloudIntegrationsV1alphaJwtOut"] = t.struct(
        {
            "jwtHeader": t.string().optional(),
            "jwt": t.string().optional(),
            "secret": t.string().optional(),
            "jwtPayload": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaJwtOut"])
    types["GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseIn"] = t.struct(
        {
            "executionFailed": t.boolean().optional(),
            "executionId": t.string().optional(),
            "outputParameters": t.struct({"_": t.string().optional()}).optional(),
            "parameterEntries": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"])
            ).optional(),
            "eventParameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseIn"])
    types["GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseOut"] = t.struct(
        {
            "executionFailed": t.boolean().optional(),
            "executionId": t.string().optional(),
            "outputParameters": t.struct({"_": t.string().optional()}).optional(),
            "parameterEntries": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"])
            ).optional(),
            "eventParameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseOut"])
    types["GoogleCloudIntegrationsV1alphaListExecutionsResponseIn"] = t.struct(
        {
            "executionInfos": t.array(
                t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoIn"]
                )
            ),
            "nextPageToken": t.string().optional(),
            "executions": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaExecutionIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListExecutionsResponseIn"])
    types["GoogleCloudIntegrationsV1alphaListExecutionsResponseOut"] = t.struct(
        {
            "executionInfos": t.array(
                t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoOut"]
                )
            ),
            "nextPageToken": t.string().optional(),
            "executions": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaExecutionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListExecutionsResponseOut"])
    types["EnterpriseCrmEventbusProtoAddressIn"] = t.struct(
        {
            "tokens": t.array(t.proxy(renames["EnterpriseCrmEventbusProtoTokenIn"])),
            "email": t.string(),
            "name": t.string(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoAddressIn"])
    types["EnterpriseCrmEventbusProtoAddressOut"] = t.struct(
        {
            "tokens": t.array(t.proxy(renames["EnterpriseCrmEventbusProtoTokenOut"])),
            "email": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoAddressOut"])
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
    types["GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsIn"] = t.struct(
        {
            "accessToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAccessTokenIn"]
            ).optional(),
            "requestType": t.string().optional(),
            "clientId": t.string().optional(),
            "tokenParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapIn"]
            ).optional(),
            "scope": t.string().optional(),
            "tokenEndpoint": t.string().optional(),
            "clientSecret": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsIn"])
    types["GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsOut"] = t.struct(
        {
            "accessToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAccessTokenOut"]
            ).optional(),
            "requestType": t.string().optional(),
            "clientId": t.string().optional(),
            "tokenParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapOut"]
            ).optional(),
            "scope": t.string().optional(),
            "tokenEndpoint": t.string().optional(),
            "clientSecret": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsOut"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"] = t.struct(
        {
            "value": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn"]
            ).optional(),
            "dataType": t.string().optional(),
            "key": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"] = t.struct(
        {
            "value": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "dataType": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"])
    types[
        "GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestIn"
    ] = t.struct(
        {
            "workflowName": t.string().optional(),
            "priority": t.string().optional(),
            "requestId": t.string().optional(),
            "ignoreErrorIfNoActiveWorkflow": t.boolean().optional(),
            "resourceName": t.string().optional(),
            "scheduledTime": t.string().optional(),
            "triggerId": t.string().optional(),
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersIn"]
            ).optional(),
            "testMode": t.boolean().optional(),
            "clientId": t.string().optional(),
        }
    ).named(
        renames["GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestIn"]
    )
    types[
        "GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestOut"
    ] = t.struct(
        {
            "workflowName": t.string().optional(),
            "priority": t.string().optional(),
            "requestId": t.string().optional(),
            "ignoreErrorIfNoActiveWorkflow": t.boolean().optional(),
            "resourceName": t.string().optional(),
            "scheduledTime": t.string().optional(),
            "triggerId": t.string().optional(),
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersOut"]
            ).optional(),
            "testMode": t.boolean().optional(),
            "clientId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestOut"]
    )
    types["EnterpriseCrmEventbusProtoParameterValueTypeIn"] = t.struct(
        {
            "serializedObjectValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoSerializedObjectParameterIn"]
            ),
            "intValue": t.string(),
            "booleanArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoBooleanParameterArrayIn"]
            ),
            "intArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoIntParameterArrayIn"]
            ),
            "stringArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoStringParameterArrayIn"]
            ),
            "protoArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoProtoParameterArrayIn"]
            ),
            "doubleArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoDoubleParameterArrayIn"]
            ),
            "stringValue": t.string(),
            "booleanValue": t.boolean(),
            "protoValue": t.struct({"_": t.string().optional()}),
            "doubleValue": t.number(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParameterValueTypeIn"])
    types["EnterpriseCrmEventbusProtoParameterValueTypeOut"] = t.struct(
        {
            "serializedObjectValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoSerializedObjectParameterOut"]
            ),
            "intValue": t.string(),
            "booleanArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoBooleanParameterArrayOut"]
            ),
            "intArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoIntParameterArrayOut"]
            ),
            "stringArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoStringParameterArrayOut"]
            ),
            "protoArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoProtoParameterArrayOut"]
            ),
            "doubleArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoDoubleParameterArrayOut"]
            ),
            "stringValue": t.string(),
            "booleanValue": t.boolean(),
            "protoValue": t.struct({"_": t.string().optional()}),
            "doubleValue": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParameterValueTypeOut"])
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
    types["GoogleCloudIntegrationsV1alphaCertificateIn"] = t.struct(
        {
            "certificateStatus": t.string().optional(),
            "credentialId": t.string().optional(),
            "description": t.string().optional(),
            "rawCertificate": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaClientCertificateIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "requestorId": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCertificateIn"])
    types["GoogleCloudIntegrationsV1alphaCertificateOut"] = t.struct(
        {
            "validEndTime": t.string().optional(),
            "certificateStatus": t.string().optional(),
            "name": t.string().optional(),
            "credentialId": t.string().optional(),
            "description": t.string().optional(),
            "rawCertificate": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaClientCertificateOut"]
            ).optional(),
            "validStartTime": t.string().optional(),
            "displayName": t.string().optional(),
            "requestorId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCertificateOut"])
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
    types[
        "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataIn"
    ] = t.struct(
        {
            "taskAttemptNum": t.integer().optional(),
            "eventAttemptNum": t.integer().optional(),
            "taskLabel": t.string().optional(),
            "taskName": t.string().optional(),
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
            "taskAttemptNum": t.integer().optional(),
            "eventAttemptNum": t.integer().optional(),
            "taskLabel": t.string().optional(),
            "taskName": t.string().optional(),
            "taskNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataOut"
        ]
    )
    types["EnterpriseCrmEventbusProtoFunctionTypeIn"] = t.struct(
        {
            "stringArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoStringArrayFunctionIn"]
            ),
            "booleanFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoBooleanFunctionIn"]
            ),
            "protoArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoProtoArrayFunctionIn"]
            ),
            "doubleArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoDoubleArrayFunctionIn"]
            ),
            "protoFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoProtoFunctionIn"]
            ),
            "stringFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoStringFunctionIn"]
            ),
            "jsonFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoJsonFunctionIn"]
            ).optional(),
            "intArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoIntArrayFunctionIn"]
            ),
            "booleanArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoBooleanArrayFunctionIn"]
            ),
            "doubleFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoDoubleFunctionIn"]
            ),
            "intFunction": t.proxy(renames["EnterpriseCrmEventbusProtoIntFunctionIn"]),
            "baseFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseFunctionIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFunctionTypeIn"])
    types["EnterpriseCrmEventbusProtoFunctionTypeOut"] = t.struct(
        {
            "stringArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoStringArrayFunctionOut"]
            ),
            "booleanFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoBooleanFunctionOut"]
            ),
            "protoArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoProtoArrayFunctionOut"]
            ),
            "doubleArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoDoubleArrayFunctionOut"]
            ),
            "protoFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoProtoFunctionOut"]
            ),
            "stringFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoStringFunctionOut"]
            ),
            "jsonFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoJsonFunctionOut"]
            ).optional(),
            "intArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoIntArrayFunctionOut"]
            ),
            "booleanArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoBooleanArrayFunctionOut"]
            ),
            "doubleFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoDoubleFunctionOut"]
            ),
            "intFunction": t.proxy(renames["EnterpriseCrmEventbusProtoIntFunctionOut"]),
            "baseFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseFunctionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFunctionTypeOut"])
    types["GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataIn"] = t.struct(
        {
            "actions": t.array(t.string()).optional(),
            "entities": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataIn"])
    types["GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataOut"] = t.struct(
        {
            "actions": t.array(t.string()).optional(),
            "entities": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataOut"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterMapIn"] = t.struct(
        {
            "keyType": t.string().optional(),
            "valueType": t.string(),
            "entries": t.array(
                t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoParameterMapEntryIn"]
                )
            ),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterMapIn"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterMapOut"] = t.struct(
        {
            "keyType": t.string().optional(),
            "valueType": t.string(),
            "entries": t.array(
                t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoParameterMapEntryOut"]
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterMapOut"])
    types["GoogleCloudIntegrationsV1alphaExecutionIn"] = t.struct(
        {
            "responseParams": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"])
            ).optional(),
            "requestParameters": t.struct({"_": t.string().optional()}).optional(),
            "triggerId": t.string().optional(),
            "directSubExecutions": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaExecutionIn"])
            ).optional(),
            "requestParams": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"])
            ).optional(),
            "executionMethod": t.string().optional(),
            "responseParameters": t.struct({"_": t.string().optional()}).optional(),
            "executionDetails": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaExecutionDetailsIn"]
            ).optional(),
            "eventExecutionDetails": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventExecutionDetailsIn"]
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecutionIn"])
    types["GoogleCloudIntegrationsV1alphaExecutionOut"] = t.struct(
        {
            "responseParams": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"])
            ).optional(),
            "updateTime": t.string().optional(),
            "requestParameters": t.struct({"_": t.string().optional()}).optional(),
            "triggerId": t.string().optional(),
            "directSubExecutions": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaExecutionOut"])
            ).optional(),
            "createTime": t.string().optional(),
            "requestParams": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"])
            ).optional(),
            "executionMethod": t.string().optional(),
            "responseParameters": t.struct({"_": t.string().optional()}).optional(),
            "executionDetails": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaExecutionDetailsOut"]
            ).optional(),
            "eventExecutionDetails": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventExecutionDetailsOut"]
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecutionOut"])
    types["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigIn"] = t.struct(
        {
            "thresholdType": t.string().optional(),
            "disableAlert": t.boolean().optional(),
            "onlyFinalAttempt": t.boolean().optional(),
            "durationThreshold": t.string().optional(),
            "displayName": t.string().optional(),
            "aggregationPeriod": t.string().optional(),
            "alertThreshold": t.integer().optional(),
            "thresholdValue": t.proxy(
                renames[
                    "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueIn"
                ]
            ).optional(),
            "metricType": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigIn"])
    types["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigOut"] = t.struct(
        {
            "thresholdType": t.string().optional(),
            "disableAlert": t.boolean().optional(),
            "onlyFinalAttempt": t.boolean().optional(),
            "durationThreshold": t.string().optional(),
            "displayName": t.string().optional(),
            "aggregationPeriod": t.string().optional(),
            "alertThreshold": t.integer().optional(),
            "thresholdValue": t.proxy(
                renames[
                    "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueOut"
                ]
            ).optional(),
            "metricType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigOut"])
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
            "name": t.string(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationOut"])
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
    types["GoogleCloudIntegrationsV1alphaStringParameterArrayIn"] = t.struct(
        {"stringValues": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaStringParameterArrayIn"])
    types["GoogleCloudIntegrationsV1alphaStringParameterArrayOut"] = t.struct(
        {
            "stringValues": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaStringParameterArrayOut"])
    types["GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigIn"] = t.struct(
        {
            "emailAddresses": t.array(t.string()).optional(),
            "customMessage": t.string().optional(),
            "expiration": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigIn"])
    types["GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigOut"] = t.struct(
        {
            "emailAddresses": t.array(t.string()).optional(),
            "customMessage": t.string().optional(),
            "expiration": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigOut"])
    types["EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayIn"] = t.struct(
        {"doubleValues": t.array(t.number())}
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayIn"])
    types["EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayOut"] = t.struct(
        {
            "doubleValues": t.array(t.number()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayOut"])
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
    types["EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsIn"] = t.struct(
        {
            "networkAddress": t.string().optional(),
            "ryeLockUnheldCount": t.integer().optional(),
            "eventAttemptStats": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsIn"
                    ]
                )
            ),
            "eventRetriesFromBeginningCount": t.integer().optional(),
            "eventExecutionState": t.string().optional(),
            "eventExecutionSnapshot": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotIn"
                    ]
                )
            ).optional(),
            "logFilePath": t.string().optional(),
            "nextExecutionTime": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsIn"])
    types["EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsOut"] = t.struct(
        {
            "networkAddress": t.string().optional(),
            "ryeLockUnheldCount": t.integer().optional(),
            "eventAttemptStats": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsOut"
                    ]
                )
            ),
            "eventRetriesFromBeginningCount": t.integer().optional(),
            "eventExecutionState": t.string().optional(),
            "eventExecutionSnapshot": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotOut"
                    ]
                )
            ).optional(),
            "logFilePath": t.string().optional(),
            "nextExecutionTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsOut"])
    types["EnterpriseCrmEventbusProtoCloudKmsConfigIn"] = t.struct(
        {
            "locationName": t.string().optional(),
            "gcpProjectId": t.string().optional(),
            "keyVersionName": t.string().optional(),
            "keyName": t.string().optional(),
            "keyRingName": t.string().optional(),
            "serviceAccount": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoCloudKmsConfigIn"])
    types["EnterpriseCrmEventbusProtoCloudKmsConfigOut"] = t.struct(
        {
            "locationName": t.string().optional(),
            "gcpProjectId": t.string().optional(),
            "keyVersionName": t.string().optional(),
            "keyName": t.string().optional(),
            "keyRingName": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoCloudKmsConfigOut"])
    types["GoogleCloudIntegrationsV1alphaBooleanParameterArrayIn"] = t.struct(
        {"booleanValues": t.array(t.boolean()).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaBooleanParameterArrayIn"])
    types["GoogleCloudIntegrationsV1alphaBooleanParameterArrayOut"] = t.struct(
        {
            "booleanValues": t.array(t.boolean()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaBooleanParameterArrayOut"])
    types["EnterpriseCrmEventbusStatsIn"] = t.struct(
        {
            "durationInSeconds": t.number().optional(),
            "dimensions": t.proxy(
                renames["EnterpriseCrmEventbusStatsDimensionsIn"]
            ).optional(),
            "warningRate": t.number().optional(),
            "errorRate": t.number().optional(),
            "qps": t.number().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusStatsIn"])
    types["EnterpriseCrmEventbusStatsOut"] = t.struct(
        {
            "durationInSeconds": t.number().optional(),
            "dimensions": t.proxy(
                renames["EnterpriseCrmEventbusStatsDimensionsOut"]
            ).optional(),
            "warningRate": t.number().optional(),
            "errorRate": t.number().optional(),
            "qps": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusStatsOut"])
    types["EnterpriseCrmEventbusProtoTaskMetadataIn"] = t.struct(
        {
            "defaultJsonValidationOption": t.string().optional(),
            "name": t.string().optional(),
            "system": t.string(),
            "admins": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskMetadataAdminIn"])
            ),
            "status": t.string().optional(),
            "externalDocLink": t.string().optional(),
            "externalDocMarkdown": t.string().optional(),
            "codeSearchLink": t.string().optional(),
            "descriptiveName": t.string().optional(),
            "externalCategory": t.string(),
            "docMarkdown": t.string().optional(),
            "externalCategorySequence": t.integer().optional(),
            "activeTaskName": t.string().optional(),
            "isDeprecated": t.boolean().optional(),
            "iconLink": t.string().optional(),
            "externalDocHtml": t.string().optional(),
            "standaloneExternalDocHtml": t.string().optional(),
            "description": t.string().optional(),
            "defaultSpec": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "category": t.string(),
            "g3DocLink": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskMetadataIn"])
    types["EnterpriseCrmEventbusProtoTaskMetadataOut"] = t.struct(
        {
            "defaultJsonValidationOption": t.string().optional(),
            "name": t.string().optional(),
            "system": t.string(),
            "admins": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskMetadataAdminOut"])
            ),
            "status": t.string().optional(),
            "externalDocLink": t.string().optional(),
            "externalDocMarkdown": t.string().optional(),
            "codeSearchLink": t.string().optional(),
            "descriptiveName": t.string().optional(),
            "externalCategory": t.string(),
            "docMarkdown": t.string().optional(),
            "externalCategorySequence": t.integer().optional(),
            "activeTaskName": t.string().optional(),
            "isDeprecated": t.boolean().optional(),
            "iconLink": t.string().optional(),
            "externalDocHtml": t.string().optional(),
            "standaloneExternalDocHtml": t.string().optional(),
            "description": t.string().optional(),
            "defaultSpec": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "category": t.string(),
            "g3DocLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskMetadataOut"])
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
    types["EnterpriseCrmEventbusProtoConnectorsConnectionIn"] = t.struct(
        {
            "serviceName": t.string().optional(),
            "connectorVersion": t.string().optional(),
            "connectionName": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoConnectorsConnectionIn"])
    types["EnterpriseCrmEventbusProtoConnectorsConnectionOut"] = t.struct(
        {
            "serviceName": t.string().optional(),
            "connectorVersion": t.string().optional(),
            "connectionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoConnectorsConnectionOut"])
    types["GoogleCloudIntegrationsV1alphaParameterMapFieldIn"] = t.struct(
        {
            "literalValue": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaValueTypeIn"]
            ).optional(),
            "referenceKey": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaParameterMapFieldIn"])
    types["GoogleCloudIntegrationsV1alphaParameterMapFieldOut"] = t.struct(
        {
            "literalValue": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaValueTypeOut"]
            ).optional(),
            "referenceKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaParameterMapFieldOut"])
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
    types["EnterpriseCrmEventbusProtoSerializedObjectParameterIn"] = t.struct(
        {"objectValue": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoSerializedObjectParameterIn"])
    types["EnterpriseCrmEventbusProtoSerializedObjectParameterOut"] = t.struct(
        {
            "objectValue": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSerializedObjectParameterOut"])
    types["EnterpriseCrmEventbusProtoDoubleFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoDoubleFunctionIn"])
    types["EnterpriseCrmEventbusProtoDoubleFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoDoubleFunctionOut"])
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
    types["GoogleCloudIntegrationsV1alphaFailurePolicyIn"] = t.struct(
        {
            "intervalTime": t.string(),
            "maxRetries": t.integer(),
            "retryStrategy": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaFailurePolicyIn"])
    types["GoogleCloudIntegrationsV1alphaFailurePolicyOut"] = t.struct(
        {
            "intervalTime": t.string(),
            "maxRetries": t.integer(),
            "retryStrategy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaFailurePolicyOut"])
    types["GoogleCloudIntegrationsV1alphaListIntegrationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "integrations": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListIntegrationsResponseIn"])
    types["GoogleCloudIntegrationsV1alphaListIntegrationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "integrations": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListIntegrationsResponseOut"])
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
    types["GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsIn"] = t.struct(
        {
            "username": t.string().optional(),
            "tokenEndpoint": t.string().optional(),
            "tokenParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapIn"]
            ).optional(),
            "scope": t.string().optional(),
            "requestType": t.string().optional(),
            "password": t.string().optional(),
            "accessToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAccessTokenIn"]
            ).optional(),
            "clientSecret": t.string().optional(),
            "clientId": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsIn"])
    types["GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsOut"] = t.struct(
        {
            "username": t.string().optional(),
            "tokenEndpoint": t.string().optional(),
            "tokenParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapOut"]
            ).optional(),
            "scope": t.string().optional(),
            "requestType": t.string().optional(),
            "password": t.string().optional(),
            "accessToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAccessTokenOut"]
            ).optional(),
            "clientSecret": t.string().optional(),
            "clientId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsOut"])
    types["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseIn"] = t.struct(
        {"scriptId": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseIn"])
    types["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseOut"] = t.struct(
        {
            "scriptId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseOut"])
    types["GoogleCloudConnectorsV1SslConfigIn"] = t.struct(
        {
            "clientCertificate": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
            "additionalVariables": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConfigVariableIn"])
            ).optional(),
            "privateServerCertificate": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
            "useSsl": t.boolean().optional(),
            "type": t.string().optional(),
            "clientPrivateKeyPass": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
            "trustModel": t.string().optional(),
            "serverCertType": t.string().optional(),
            "clientPrivateKey": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
            "clientCertType": t.string().optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1SslConfigIn"])
    types["GoogleCloudConnectorsV1SslConfigOut"] = t.struct(
        {
            "clientCertificate": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "additionalVariables": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConfigVariableOut"])
            ).optional(),
            "privateServerCertificate": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "useSsl": t.boolean().optional(),
            "type": t.string().optional(),
            "clientPrivateKeyPass": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "trustModel": t.string().optional(),
            "serverCertType": t.string().optional(),
            "clientPrivateKey": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "clientCertType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1SslConfigOut"])
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
    types["EnterpriseCrmEventbusProtoSuspensionConfigIn"] = t.struct(
        {
            "suspensionExpiration": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionExpirationIn"]
            ).optional(),
            "whoMayResolve": t.array(
                t.proxy(
                    renames["EnterpriseCrmEventbusProtoSuspensionAuthPermissionsIn"]
                )
            ).optional(),
            "customMessage": t.string().optional(),
            "notifications": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoNotificationIn"])
            ),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionConfigIn"])
    types["EnterpriseCrmEventbusProtoSuspensionConfigOut"] = t.struct(
        {
            "suspensionExpiration": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionExpirationOut"]
            ).optional(),
            "whoMayResolve": t.array(
                t.proxy(
                    renames["EnterpriseCrmEventbusProtoSuspensionAuthPermissionsOut"]
                )
            ).optional(),
            "customMessage": t.string().optional(),
            "notifications": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoNotificationOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionConfigOut"])
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
    types["EnterpriseCrmEventbusProtoProtoParameterArrayIn"] = t.struct(
        {"protoValues": t.array(t.struct({"_": t.string().optional()}))}
    ).named(renames["EnterpriseCrmEventbusProtoProtoParameterArrayIn"])
    types["EnterpriseCrmEventbusProtoProtoParameterArrayOut"] = t.struct(
        {
            "protoValues": t.array(t.struct({"_": t.string().optional()})),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoProtoParameterArrayOut"])
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
    types["EnterpriseCrmEventbusProtoTeardownTaskConfigIn"] = t.struct(
        {
            "name": t.string(),
            "teardownTaskImplementationClassName": t.string(),
            "creatorEmail": t.string().optional(),
            "properties": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventBusPropertiesIn"]
            ),
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersIn"]
            ).optional(),
            "nextTeardownTask": t.proxy(
                renames["EnterpriseCrmEventbusProtoNextTeardownTaskIn"]
            ),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTeardownTaskConfigIn"])
    types["EnterpriseCrmEventbusProtoTeardownTaskConfigOut"] = t.struct(
        {
            "name": t.string(),
            "teardownTaskImplementationClassName": t.string(),
            "creatorEmail": t.string().optional(),
            "properties": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventBusPropertiesOut"]
            ),
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersOut"]
            ).optional(),
            "nextTeardownTask": t.proxy(
                renames["EnterpriseCrmEventbusProtoNextTeardownTaskOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTeardownTaskConfigOut"])
    types["CrmlogErrorCodeIn"] = t.struct({"commonErrorCode": t.string()}).named(
        renames["CrmlogErrorCodeIn"]
    )
    types["CrmlogErrorCodeOut"] = t.struct(
        {
            "commonErrorCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CrmlogErrorCodeOut"])
    types["GoogleCloudIntegrationsV1alphaIntegrationVersionIn"] = t.struct(
        {
            "origin": t.string().optional(),
            "userLabel": t.string().optional(),
            "teardown": t.proxy(
                renames["EnterpriseCrmEventbusProtoTeardownIn"]
            ).optional(),
            "parentTemplateId": t.string().optional(),
            "description": t.string().optional(),
            "integrationParameters": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationParameterIn"])
            ).optional(),
            "runAsServiceAccount": t.string().optional(),
            "triggerConfigsInternal": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn"])
            ).optional(),
            "taskConfigsInternal": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigIn"])
            ).optional(),
            "errorCatcherConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn"])
            ).optional(),
            "integrationParametersInternal": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn"]
            ).optional(),
            "taskConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaTaskConfigIn"])
            ).optional(),
            "databasePersistencePolicy": t.string().optional(),
            "snapshotNumber": t.string().optional(),
            "triggerConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaTriggerConfigIn"])
            ).optional(),
            "lastModifierEmail": t.string().optional(),
            "lockHolder": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionIn"])
    types["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"] = t.struct(
        {
            "origin": t.string().optional(),
            "userLabel": t.string().optional(),
            "teardown": t.proxy(
                renames["EnterpriseCrmEventbusProtoTeardownOut"]
            ).optional(),
            "parentTemplateId": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "integrationParameters": t.array(
                t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaIntegrationParameterOut"]
                )
            ).optional(),
            "runAsServiceAccount": t.string().optional(),
            "updateTime": t.string().optional(),
            "triggerConfigsInternal": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigOut"])
            ).optional(),
            "taskConfigsInternal": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigOut"])
            ).optional(),
            "errorCatcherConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigOut"])
            ).optional(),
            "integrationParametersInternal": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersOut"]
            ).optional(),
            "taskConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaTaskConfigOut"])
            ).optional(),
            "state": t.string().optional(),
            "databasePersistencePolicy": t.string().optional(),
            "snapshotNumber": t.string().optional(),
            "status": t.string().optional(),
            "triggerConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaTriggerConfigOut"])
            ).optional(),
            "lastModifierEmail": t.string().optional(),
            "name": t.string().optional(),
            "lockHolder": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"])
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
    types["EnterpriseCrmEventbusProtoDoubleArrayIn"] = t.struct(
        {"values": t.array(t.number())}
    ).named(renames["EnterpriseCrmEventbusProtoDoubleArrayIn"])
    types["EnterpriseCrmEventbusProtoDoubleArrayOut"] = t.struct(
        {
            "values": t.array(t.number()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoDoubleArrayOut"])
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
    types[
        "GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataIn"
    ] = t.struct(
        {
            "taskNumber": t.string().optional(),
            "taskAttempt": t.integer().optional(),
            "taskLabel": t.string().optional(),
            "task": t.string().optional(),
            "executionAttempt": t.integer().optional(),
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
            "taskNumber": t.string().optional(),
            "taskAttempt": t.integer().optional(),
            "taskLabel": t.string().optional(),
            "task": t.string().optional(),
            "executionAttempt": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataOut"
        ]
    )
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
    types["GoogleCloudConnectorsV1NodeConfigIn"] = t.struct(
        {"minNodeCount": t.integer().optional(), "maxNodeCount": t.integer().optional()}
    ).named(renames["GoogleCloudConnectorsV1NodeConfigIn"])
    types["GoogleCloudConnectorsV1NodeConfigOut"] = t.struct(
        {
            "minNodeCount": t.integer().optional(),
            "maxNodeCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1NodeConfigOut"])
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
    types["GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowIn"] = t.struct(
        {
            "clientId": t.string().optional(),
            "enablePkce": t.boolean().optional(),
            "authCode": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "pkceVerifier": t.string().optional(),
            "clientSecret": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
            "redirectUri": t.string().optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowIn"])
    types["GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowOut"] = t.struct(
        {
            "clientId": t.string().optional(),
            "enablePkce": t.boolean().optional(),
            "authCode": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "pkceVerifier": t.string().optional(),
            "clientSecret": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "redirectUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowOut"])
    types["EnterpriseCrmEventbusProtoStringArrayFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoStringArrayFunctionIn"])
    types["EnterpriseCrmEventbusProtoStringArrayFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoStringArrayFunctionOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
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

    functions = {}
    functions["projectsLocationsSfdcInstancesGet"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "authConfigId": t.array(t.string()).optional(),
                "sfdcOrgId": t.string().optional(),
                "serviceAuthority": t.string().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesCreate"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "authConfigId": t.array(t.string()).optional(),
                "sfdcOrgId": t.string().optional(),
                "serviceAuthority": t.string().optional(),
                "description": t.string().optional(),
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
                "authConfigId": t.array(t.string()).optional(),
                "sfdcOrgId": t.string().optional(),
                "serviceAuthority": t.string().optional(),
                "description": t.string().optional(),
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
                "authConfigId": t.array(t.string()).optional(),
                "sfdcOrgId": t.string().optional(),
                "serviceAuthority": t.string().optional(),
                "description": t.string().optional(),
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
                "authConfigId": t.array(t.string()).optional(),
                "sfdcOrgId": t.string().optional(),
                "serviceAuthority": t.string().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesSfdcChannelsPatch"] = integrations.get(
        "v1alpha/{parent}/sfdcChannels",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesSfdcChannelsDelete"] = integrations.get(
        "v1alpha/{parent}/sfdcChannels",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesSfdcChannelsCreate"] = integrations.get(
        "v1alpha/{parent}/sfdcChannels",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesSfdcChannelsGet"] = integrations.get(
        "v1alpha/{parent}/sfdcChannels",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesSfdcChannelsList"] = integrations.get(
        "v1alpha/{parent}/sfdcChannels",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseOut"]),
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
    functions["projectsLocationsProductsAuthConfigsDelete"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaAuthConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsAuthConfigsList"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaAuthConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsAuthConfigsPatch"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaAuthConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsAuthConfigsCreate"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaAuthConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsAuthConfigsGet"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaAuthConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsSfdcInstancesPatch"] = integrations.post(
        "v1alpha/{parent}/sfdcInstances",
        t.struct(
            {
                "parent": t.string(),
                "authConfigId": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "sfdcOrgId": t.string().optional(),
                "serviceAuthority": t.string().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsSfdcInstancesGet"] = integrations.post(
        "v1alpha/{parent}/sfdcInstances",
        t.struct(
            {
                "parent": t.string(),
                "authConfigId": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "sfdcOrgId": t.string().optional(),
                "serviceAuthority": t.string().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsSfdcInstancesList"] = integrations.post(
        "v1alpha/{parent}/sfdcInstances",
        t.struct(
            {
                "parent": t.string(),
                "authConfigId": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "sfdcOrgId": t.string().optional(),
                "serviceAuthority": t.string().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsSfdcInstancesDelete"] = integrations.post(
        "v1alpha/{parent}/sfdcInstances",
        t.struct(
            {
                "parent": t.string(),
                "authConfigId": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "sfdcOrgId": t.string().optional(),
                "serviceAuthority": t.string().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsSfdcInstancesCreate"] = integrations.post(
        "v1alpha/{parent}/sfdcInstances",
        t.struct(
            {
                "parent": t.string(),
                "authConfigId": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "sfdcOrgId": t.string().optional(),
                "serviceAuthority": t.string().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsSfdcInstancesSfdcChannelsPatch"
    ] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsSfdcInstancesSfdcChannelsCreate"
    ] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsSfdcInstancesSfdcChannelsDelete"
    ] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsSfdcInstancesSfdcChannelsList"
    ] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsSfdcInstancesSfdcChannelsGet"
    ] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsCertificatesList"] = integrations.post(
        "v1alpha/{parent}/certificates",
        t.struct(
            {
                "parent": t.string(),
                "certificateStatus": t.string().optional(),
                "credentialId": t.string().optional(),
                "description": t.string().optional(),
                "rawCertificate": t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaClientCertificateIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "requestorId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaCertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsCertificatesPatch"] = integrations.post(
        "v1alpha/{parent}/certificates",
        t.struct(
            {
                "parent": t.string(),
                "certificateStatus": t.string().optional(),
                "credentialId": t.string().optional(),
                "description": t.string().optional(),
                "rawCertificate": t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaClientCertificateIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "requestorId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaCertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsCertificatesGet"] = integrations.post(
        "v1alpha/{parent}/certificates",
        t.struct(
            {
                "parent": t.string(),
                "certificateStatus": t.string().optional(),
                "credentialId": t.string().optional(),
                "description": t.string().optional(),
                "rawCertificate": t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaClientCertificateIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "requestorId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaCertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsCertificatesDelete"] = integrations.post(
        "v1alpha/{parent}/certificates",
        t.struct(
            {
                "parent": t.string(),
                "certificateStatus": t.string().optional(),
                "credentialId": t.string().optional(),
                "description": t.string().optional(),
                "rawCertificate": t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaClientCertificateIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "requestorId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaCertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsCertificatesCreate"] = integrations.post(
        "v1alpha/{parent}/certificates",
        t.struct(
            {
                "parent": t.string(),
                "certificateStatus": t.string().optional(),
                "credentialId": t.string().optional(),
                "description": t.string().optional(),
                "rawCertificate": t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaClientCertificateIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "requestorId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaCertificateOut"]),
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
    functions["projectsLocationsProductsIntegrationsSchedule"] = integrations.delete(
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
    functions[
        "projectsLocationsProductsIntegrationsExecutionsCancel"
    ] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaExecutionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsExecutionsList"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaExecutionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsExecutionsGet"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaExecutionOut"]),
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
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListSuspensionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsVersionsPatch"] = integrations.get(
        "v1alpha/{parent}/versions",
        t.struct(
            {
                "fieldMask": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsVersionsCreate"] = integrations.get(
        "v1alpha/{parent}/versions",
        t.struct(
            {
                "fieldMask": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsVersionsPublish"
    ] = integrations.get(
        "v1alpha/{parent}/versions",
        t.struct(
            {
                "fieldMask": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsVersionsUnpublish"
    ] = integrations.get(
        "v1alpha/{parent}/versions",
        t.struct(
            {
                "fieldMask": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsVersionsDelete"] = integrations.get(
        "v1alpha/{parent}/versions",
        t.struct(
            {
                "fieldMask": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsVersionsTakeoverEditLock"
    ] = integrations.get(
        "v1alpha/{parent}/versions",
        t.struct(
            {
                "fieldMask": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsVersionsGet"] = integrations.get(
        "v1alpha/{parent}/versions",
        t.struct(
            {
                "fieldMask": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsVersionsDownload"
    ] = integrations.get(
        "v1alpha/{parent}/versions",
        t.struct(
            {
                "fieldMask": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsVersionsUpload"] = integrations.get(
        "v1alpha/{parent}/versions",
        t.struct(
            {
                "fieldMask": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsVersionsList"] = integrations.get(
        "v1alpha/{parent}/versions",
        t.struct(
            {
                "fieldMask": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConnectionsGetConnectionSchemaMetadata"
    ] = integrations.get(
        "v1alpha/{parent}/connections",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsList"] = integrations.get(
        "v1alpha/{parent}/connections",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListConnectionsResponseOut"]),
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
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
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
    functions["projectsLocationsIntegrationsList"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsExecute"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsSchedule"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsDelete"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsPatch"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsCreate"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsIntegrationsVersionsTakeoverEditLock"
    ] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsList"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsDownload"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsUpload"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsUnpublish"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsDelete"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsPublish"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsGet"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsExecutionsList"] = integrations.get(
        "v1alpha/{parent}/executions",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "filterParams.taskStatuses": t.string().optional(),
                "filterParams.startTime": t.string().optional(),
                "filterParams.endTime": t.string().optional(),
                "filterParams.workflowName": t.string().optional(),
                "filterParams.customFilter": t.string().optional(),
                "truncateParams": t.boolean().optional(),
                "filterParams.parameterValue": t.string().optional(),
                "filterParams.parameterKey": t.string().optional(),
                "filterParams.parameterPairKey": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filterParams.parameterType": t.string().optional(),
                "refreshAcl": t.boolean().optional(),
                "filterParams.parameterPairValue": t.string().optional(),
                "filterParams.eventStatuses": t.string().optional(),
                "filterParams.executionId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListExecutionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsIntegrationsExecutionsSuspensionsLift"
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
        "projectsLocationsIntegrationsExecutionsSuspensionsList"
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
        "projectsLocationsIntegrationsExecutionsSuspensionsResolve"
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
    functions["projectsLocationsCertificatesGet"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaCertificateOut"]),
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
    functions["projectsLocationsAuthConfigsList"] = integrations.get(
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
    functions["projectsLocationsAuthConfigsPatch"] = integrations.get(
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
                "state": t.string().optional(),
                "code": t.string().optional(),
                "gcpProjectId": t.string().optional(),
                "redirectUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaGenerateTokenResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="integrations", renames=renames, types=types, functions=functions
    )
