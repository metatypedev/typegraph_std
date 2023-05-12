from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_integrations() -> Import:
    integrations = HTTPRuntime("https://integrations.googleapis.com/")

    renames = {
        "ErrorResponse": "_integrations_1_ErrorResponse",
        "GoogleCloudIntegrationsV1alphaCancelExecutionResponseIn": "_integrations_2_GoogleCloudIntegrationsV1alphaCancelExecutionResponseIn",
        "GoogleCloudIntegrationsV1alphaCancelExecutionResponseOut": "_integrations_3_GoogleCloudIntegrationsV1alphaCancelExecutionResponseOut",
        "GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestIn": "_integrations_4_GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestIn",
        "GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestOut": "_integrations_5_GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestOut",
        "GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn": "_integrations_6_GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn",
        "GoogleCloudIntegrationsV1alphaErrorCatcherConfigOut": "_integrations_7_GoogleCloudIntegrationsV1alphaErrorCatcherConfigOut",
        "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigIn": "_integrations_8_GoogleCloudIntegrationsV1alphaIntegrationAlertConfigIn",
        "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigOut": "_integrations_9_GoogleCloudIntegrationsV1alphaIntegrationAlertConfigOut",
        "EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageIn": "_integrations_10_EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageIn",
        "EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageOut": "_integrations_11_EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageOut",
        "GoogleCloudIntegrationsV1alphaAttemptStatsIn": "_integrations_12_GoogleCloudIntegrationsV1alphaAttemptStatsIn",
        "GoogleCloudIntegrationsV1alphaAttemptStatsOut": "_integrations_13_GoogleCloudIntegrationsV1alphaAttemptStatsOut",
        "GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataIn": "_integrations_14_GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataIn",
        "GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataOut": "_integrations_15_GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataOut",
        "GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaIn": "_integrations_16_GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaIn",
        "GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaOut": "_integrations_17_GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaOut",
        "EnterpriseCrmEventbusProtoTaskUiModuleConfigIn": "_integrations_18_EnterpriseCrmEventbusProtoTaskUiModuleConfigIn",
        "EnterpriseCrmEventbusProtoTaskUiModuleConfigOut": "_integrations_19_EnterpriseCrmEventbusProtoTaskUiModuleConfigOut",
        "EnterpriseCrmEventbusProtoEventParametersIn": "_integrations_20_EnterpriseCrmEventbusProtoEventParametersIn",
        "EnterpriseCrmEventbusProtoEventParametersOut": "_integrations_21_EnterpriseCrmEventbusProtoEventParametersOut",
        "GoogleCloudIntegrationsV1alphaIntParameterArrayIn": "_integrations_22_GoogleCloudIntegrationsV1alphaIntParameterArrayIn",
        "GoogleCloudIntegrationsV1alphaIntParameterArrayOut": "_integrations_23_GoogleCloudIntegrationsV1alphaIntParameterArrayOut",
        "EnterpriseCrmEventbusProtoSuspensionConfigIn": "_integrations_24_EnterpriseCrmEventbusProtoSuspensionConfigIn",
        "EnterpriseCrmEventbusProtoSuspensionConfigOut": "_integrations_25_EnterpriseCrmEventbusProtoSuspensionConfigOut",
        "GoogleCloudConnectorsV1ConnectionStatusIn": "_integrations_26_GoogleCloudConnectorsV1ConnectionStatusIn",
        "GoogleCloudConnectorsV1ConnectionStatusOut": "_integrations_27_GoogleCloudConnectorsV1ConnectionStatusOut",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeIn": "_integrations_28_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeIn",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeOut": "_integrations_29_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRangeOut",
        "GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseIn": "_integrations_30_GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseIn",
        "GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseOut": "_integrations_31_GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseOut",
        "EnterpriseCrmFrontendsEventbusProtoStringParameterArrayIn": "_integrations_32_EnterpriseCrmFrontendsEventbusProtoStringParameterArrayIn",
        "EnterpriseCrmFrontendsEventbusProtoStringParameterArrayOut": "_integrations_33_EnterpriseCrmFrontendsEventbusProtoStringParameterArrayOut",
        "EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayIn": "_integrations_34_EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayIn",
        "EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayOut": "_integrations_35_EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayOut",
        "GoogleCloudConnectorsV1AuthConfigIn": "_integrations_36_GoogleCloudConnectorsV1AuthConfigIn",
        "GoogleCloudConnectorsV1AuthConfigOut": "_integrations_37_GoogleCloudConnectorsV1AuthConfigOut",
        "EnterpriseCrmEventbusProtoConditionIn": "_integrations_38_EnterpriseCrmEventbusProtoConditionIn",
        "EnterpriseCrmEventbusProtoConditionOut": "_integrations_39_EnterpriseCrmEventbusProtoConditionOut",
        "GoogleCloudIntegrationsV1alphaSfdcChannelIn": "_integrations_40_GoogleCloudIntegrationsV1alphaSfdcChannelIn",
        "GoogleCloudIntegrationsV1alphaSfdcChannelOut": "_integrations_41_GoogleCloudIntegrationsV1alphaSfdcChannelOut",
        "GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseIn": "_integrations_42_GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseIn",
        "GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseOut": "_integrations_43_GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseOut",
        "EnterpriseCrmFrontendsEventbusProtoTaskEntityIn": "_integrations_44_EnterpriseCrmFrontendsEventbusProtoTaskEntityIn",
        "EnterpriseCrmFrontendsEventbusProtoTaskEntityOut": "_integrations_45_EnterpriseCrmFrontendsEventbusProtoTaskEntityOut",
        "EnterpriseCrmEventbusProtoErrorDetailIn": "_integrations_46_EnterpriseCrmEventbusProtoErrorDetailIn",
        "EnterpriseCrmEventbusProtoErrorDetailOut": "_integrations_47_EnterpriseCrmEventbusProtoErrorDetailOut",
        "GoogleCloudIntegrationsV1alphaIntegrationParameterIn": "_integrations_48_GoogleCloudIntegrationsV1alphaIntegrationParameterIn",
        "GoogleCloudIntegrationsV1alphaIntegrationParameterOut": "_integrations_49_GoogleCloudIntegrationsV1alphaIntegrationParameterOut",
        "EnterpriseCrmEventbusProtoStringArrayFunctionIn": "_integrations_50_EnterpriseCrmEventbusProtoStringArrayFunctionIn",
        "EnterpriseCrmEventbusProtoStringArrayFunctionOut": "_integrations_51_EnterpriseCrmEventbusProtoStringArrayFunctionOut",
        "EnterpriseCrmEventbusProtoTaskMetadataIn": "_integrations_52_EnterpriseCrmEventbusProtoTaskMetadataIn",
        "EnterpriseCrmEventbusProtoTaskMetadataOut": "_integrations_53_EnterpriseCrmEventbusProtoTaskMetadataOut",
        "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataIn": "_integrations_54_EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataIn",
        "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataOut": "_integrations_55_EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataOut",
        "EnterpriseCrmEventbusProtoFunctionIn": "_integrations_56_EnterpriseCrmEventbusProtoFunctionIn",
        "EnterpriseCrmEventbusProtoFunctionOut": "_integrations_57_EnterpriseCrmEventbusProtoFunctionOut",
        "GoogleCloudIntegrationsV1alphaSuspensionIn": "_integrations_58_GoogleCloudIntegrationsV1alphaSuspensionIn",
        "GoogleCloudIntegrationsV1alphaSuspensionOut": "_integrations_59_GoogleCloudIntegrationsV1alphaSuspensionOut",
        "EnterpriseCrmEventbusProtoCustomSuspensionRequestIn": "_integrations_60_EnterpriseCrmEventbusProtoCustomSuspensionRequestIn",
        "EnterpriseCrmEventbusProtoCustomSuspensionRequestOut": "_integrations_61_EnterpriseCrmEventbusProtoCustomSuspensionRequestOut",
        "CrmlogErrorCodeIn": "_integrations_62_CrmlogErrorCodeIn",
        "CrmlogErrorCodeOut": "_integrations_63_CrmlogErrorCodeOut",
        "EnterpriseCrmEventbusProtoNextTeardownTaskIn": "_integrations_64_EnterpriseCrmEventbusProtoNextTeardownTaskIn",
        "EnterpriseCrmEventbusProtoNextTeardownTaskOut": "_integrations_65_EnterpriseCrmEventbusProtoNextTeardownTaskOut",
        "EnterpriseCrmEventbusProtoCloudKmsConfigIn": "_integrations_66_EnterpriseCrmEventbusProtoCloudKmsConfigIn",
        "EnterpriseCrmEventbusProtoCloudKmsConfigOut": "_integrations_67_EnterpriseCrmEventbusProtoCloudKmsConfigOut",
        "GoogleCloudIntegrationsV1alphaIntegrationVersionIn": "_integrations_68_GoogleCloudIntegrationsV1alphaIntegrationVersionIn",
        "GoogleCloudIntegrationsV1alphaIntegrationVersionOut": "_integrations_69_GoogleCloudIntegrationsV1alphaIntegrationVersionOut",
        "EnterpriseCrmFrontendsEventbusProtoParameterMapIn": "_integrations_70_EnterpriseCrmFrontendsEventbusProtoParameterMapIn",
        "EnterpriseCrmFrontendsEventbusProtoParameterMapOut": "_integrations_71_EnterpriseCrmFrontendsEventbusProtoParameterMapOut",
        "GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestIn": "_integrations_72_GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestIn",
        "GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestOut": "_integrations_73_GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestOut",
        "GoogleCloudIntegrationsV1alphaTaskConfigIn": "_integrations_74_GoogleCloudIntegrationsV1alphaTaskConfigIn",
        "GoogleCloudIntegrationsV1alphaTaskConfigOut": "_integrations_75_GoogleCloudIntegrationsV1alphaTaskConfigOut",
        "GoogleCloudIntegrationsV1alphaPublishIntegrationVersionResponseIn": "_integrations_76_GoogleCloudIntegrationsV1alphaPublishIntegrationVersionResponseIn",
        "GoogleCloudIntegrationsV1alphaPublishIntegrationVersionResponseOut": "_integrations_77_GoogleCloudIntegrationsV1alphaPublishIntegrationVersionResponseOut",
        "EnterpriseCrmEventbusProtoPropertyEntryIn": "_integrations_78_EnterpriseCrmEventbusProtoPropertyEntryIn",
        "EnterpriseCrmEventbusProtoPropertyEntryOut": "_integrations_79_EnterpriseCrmEventbusProtoPropertyEntryOut",
        "GoogleCloudIntegrationsV1alphaListSuspensionsResponseIn": "_integrations_80_GoogleCloudIntegrationsV1alphaListSuspensionsResponseIn",
        "GoogleCloudIntegrationsV1alphaListSuspensionsResponseOut": "_integrations_81_GoogleCloudIntegrationsV1alphaListSuspensionsResponseOut",
        "GoogleCloudIntegrationsV1alphaEnumerateConnectorPlatformRegionsResponseIn": "_integrations_82_GoogleCloudIntegrationsV1alphaEnumerateConnectorPlatformRegionsResponseIn",
        "GoogleCloudIntegrationsV1alphaEnumerateConnectorPlatformRegionsResponseOut": "_integrations_83_GoogleCloudIntegrationsV1alphaEnumerateConnectorPlatformRegionsResponseOut",
        "EnterpriseCrmEventbusProtoParameterMapIn": "_integrations_84_EnterpriseCrmEventbusProtoParameterMapIn",
        "EnterpriseCrmEventbusProtoParameterMapOut": "_integrations_85_EnterpriseCrmEventbusProtoParameterMapOut",
        "EnterpriseCrmEventbusProtoStringParameterArrayIn": "_integrations_86_EnterpriseCrmEventbusProtoStringParameterArrayIn",
        "EnterpriseCrmEventbusProtoStringParameterArrayOut": "_integrations_87_EnterpriseCrmEventbusProtoStringParameterArrayOut",
        "EnterpriseCrmEventbusProtoParameterMapEntryIn": "_integrations_88_EnterpriseCrmEventbusProtoParameterMapEntryIn",
        "EnterpriseCrmEventbusProtoParameterMapEntryOut": "_integrations_89_EnterpriseCrmEventbusProtoParameterMapEntryOut",
        "GoogleCloudIntegrationsV1alphaValueTypeIn": "_integrations_90_GoogleCloudIntegrationsV1alphaValueTypeIn",
        "GoogleCloudIntegrationsV1alphaValueTypeOut": "_integrations_91_GoogleCloudIntegrationsV1alphaValueTypeOut",
        "EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotIn": "_integrations_92_EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotIn",
        "EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotOut": "_integrations_93_EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotOut",
        "EnterpriseCrmEventbusProtoExternalTrafficIn": "_integrations_94_EnterpriseCrmEventbusProtoExternalTrafficIn",
        "EnterpriseCrmEventbusProtoExternalTrafficOut": "_integrations_95_EnterpriseCrmEventbusProtoExternalTrafficOut",
        "EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionIn": "_integrations_96_EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionIn",
        "EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionOut": "_integrations_97_EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionOut",
        "EnterpriseCrmEventbusProtoJsonFunctionIn": "_integrations_98_EnterpriseCrmEventbusProtoJsonFunctionIn",
        "EnterpriseCrmEventbusProtoJsonFunctionOut": "_integrations_99_EnterpriseCrmEventbusProtoJsonFunctionOut",
        "EnterpriseCrmEventbusProtoTaskUiConfigIn": "_integrations_100_EnterpriseCrmEventbusProtoTaskUiConfigIn",
        "EnterpriseCrmEventbusProtoTaskUiConfigOut": "_integrations_101_EnterpriseCrmEventbusProtoTaskUiConfigOut",
        "GoogleCloudIntegrationsV1alphaTakeoverEditLockResponseIn": "_integrations_102_GoogleCloudIntegrationsV1alphaTakeoverEditLockResponseIn",
        "GoogleCloudIntegrationsV1alphaTakeoverEditLockResponseOut": "_integrations_103_GoogleCloudIntegrationsV1alphaTakeoverEditLockResponseOut",
        "GoogleCloudIntegrationsV1alphaSuccessPolicyIn": "_integrations_104_GoogleCloudIntegrationsV1alphaSuccessPolicyIn",
        "GoogleCloudIntegrationsV1alphaSuccessPolicyOut": "_integrations_105_GoogleCloudIntegrationsV1alphaSuccessPolicyOut",
        "GoogleCloudIntegrationsV1alphaAuthTokenIn": "_integrations_106_GoogleCloudIntegrationsV1alphaAuthTokenIn",
        "GoogleCloudIntegrationsV1alphaAuthTokenOut": "_integrations_107_GoogleCloudIntegrationsV1alphaAuthTokenOut",
        "EnterpriseCrmEventbusProtoTriggerCriteriaIn": "_integrations_108_EnterpriseCrmEventbusProtoTriggerCriteriaIn",
        "EnterpriseCrmEventbusProtoTriggerCriteriaOut": "_integrations_109_EnterpriseCrmEventbusProtoTriggerCriteriaOut",
        "GoogleCloudIntegrationsV1alphaResolveSuspensionRequestIn": "_integrations_110_GoogleCloudIntegrationsV1alphaResolveSuspensionRequestIn",
        "GoogleCloudIntegrationsV1alphaResolveSuspensionRequestOut": "_integrations_111_GoogleCloudIntegrationsV1alphaResolveSuspensionRequestOut",
        "EnterpriseCrmEventbusProtoProtoFunctionIn": "_integrations_112_EnterpriseCrmEventbusProtoProtoFunctionIn",
        "EnterpriseCrmEventbusProtoProtoFunctionOut": "_integrations_113_EnterpriseCrmEventbusProtoProtoFunctionOut",
        "EnterpriseCrmEventbusProtoEventExecutionSnapshotIn": "_integrations_114_EnterpriseCrmEventbusProtoEventExecutionSnapshotIn",
        "EnterpriseCrmEventbusProtoEventExecutionSnapshotOut": "_integrations_115_EnterpriseCrmEventbusProtoEventExecutionSnapshotOut",
        "EnterpriseCrmEventbusProtoSuspensionExpirationIn": "_integrations_116_EnterpriseCrmEventbusProtoSuspensionExpirationIn",
        "EnterpriseCrmEventbusProtoSuspensionExpirationOut": "_integrations_117_EnterpriseCrmEventbusProtoSuspensionExpirationOut",
        "GoogleCloudIntegrationsV1alphaOidcTokenIn": "_integrations_118_GoogleCloudIntegrationsV1alphaOidcTokenIn",
        "GoogleCloudIntegrationsV1alphaOidcTokenOut": "_integrations_119_GoogleCloudIntegrationsV1alphaOidcTokenOut",
        "EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoIn": "_integrations_120_EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoIn",
        "EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoOut": "_integrations_121_EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoOut",
        "GoogleCloudIntegrationsV1alphaNextTaskIn": "_integrations_122_GoogleCloudIntegrationsV1alphaNextTaskIn",
        "GoogleCloudIntegrationsV1alphaNextTaskOut": "_integrations_123_GoogleCloudIntegrationsV1alphaNextTaskOut",
        "EnterpriseCrmEventbusProtoNodeIdentifierIn": "_integrations_124_EnterpriseCrmEventbusProtoNodeIdentifierIn",
        "EnterpriseCrmEventbusProtoNodeIdentifierOut": "_integrations_125_EnterpriseCrmEventbusProtoNodeIdentifierOut",
        "GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseIn": "_integrations_126_GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseIn",
        "GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseOut": "_integrations_127_GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseOut",
        "EnterpriseCrmEventbusProtoEventExecutionDetailsIn": "_integrations_128_EnterpriseCrmEventbusProtoEventExecutionDetailsIn",
        "EnterpriseCrmEventbusProtoEventExecutionDetailsOut": "_integrations_129_EnterpriseCrmEventbusProtoEventExecutionDetailsOut",
        "EnterpriseCrmEventbusProtoDoubleArrayIn": "_integrations_130_EnterpriseCrmEventbusProtoDoubleArrayIn",
        "EnterpriseCrmEventbusProtoDoubleArrayOut": "_integrations_131_EnterpriseCrmEventbusProtoDoubleArrayOut",
        "EnterpriseCrmEventbusStatsIn": "_integrations_132_EnterpriseCrmEventbusStatsIn",
        "EnterpriseCrmEventbusStatsOut": "_integrations_133_EnterpriseCrmEventbusStatsOut",
        "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsIn": "_integrations_134_EnterpriseCrmEventbusProtoSuspensionAuthPermissionsIn",
        "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsOut": "_integrations_135_EnterpriseCrmEventbusProtoSuspensionAuthPermissionsOut",
        "GoogleCloudIntegrationsV1alphaGenerateTokenResponseIn": "_integrations_136_GoogleCloudIntegrationsV1alphaGenerateTokenResponseIn",
        "GoogleCloudIntegrationsV1alphaGenerateTokenResponseOut": "_integrations_137_GoogleCloudIntegrationsV1alphaGenerateTokenResponseOut",
        "GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigIn": "_integrations_138_GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigIn",
        "GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigOut": "_integrations_139_GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigOut",
        "GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsIn": "_integrations_140_GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsIn",
        "GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsOut": "_integrations_141_GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsOut",
        "EnterpriseCrmEventbusProtoTeardownIn": "_integrations_142_EnterpriseCrmEventbusProtoTeardownIn",
        "EnterpriseCrmEventbusProtoTeardownOut": "_integrations_143_EnterpriseCrmEventbusProtoTeardownOut",
        "EnterpriseCrmEventbusProtoProtoArrayFunctionIn": "_integrations_144_EnterpriseCrmEventbusProtoProtoArrayFunctionIn",
        "EnterpriseCrmEventbusProtoProtoArrayFunctionOut": "_integrations_145_EnterpriseCrmEventbusProtoProtoArrayFunctionOut",
        "EnterpriseCrmEventbusProtoCloudSchedulerConfigIn": "_integrations_146_EnterpriseCrmEventbusProtoCloudSchedulerConfigIn",
        "EnterpriseCrmEventbusProtoCloudSchedulerConfigOut": "_integrations_147_EnterpriseCrmEventbusProtoCloudSchedulerConfigOut",
        "GoogleCloudConnectorsV1DestinationIn": "_integrations_148_GoogleCloudConnectorsV1DestinationIn",
        "GoogleCloudConnectorsV1DestinationOut": "_integrations_149_GoogleCloudConnectorsV1DestinationOut",
        "GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsIn": "_integrations_150_GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsIn",
        "GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsOut": "_integrations_151_GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsOut",
        "GoogleCloudIntegrationsV1alphaParameterMapIn": "_integrations_152_GoogleCloudIntegrationsV1alphaParameterMapIn",
        "GoogleCloudIntegrationsV1alphaParameterMapOut": "_integrations_153_GoogleCloudIntegrationsV1alphaParameterMapOut",
        "GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionIn": "_integrations_154_GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionIn",
        "GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionOut": "_integrations_155_GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionOut",
        "GoogleCloudIntegrationsV1alphaCloudSchedulerConfigIn": "_integrations_156_GoogleCloudIntegrationsV1alphaCloudSchedulerConfigIn",
        "GoogleCloudIntegrationsV1alphaCloudSchedulerConfigOut": "_integrations_157_GoogleCloudIntegrationsV1alphaCloudSchedulerConfigOut",
        "EnterpriseCrmEventbusProtoParameterEntryIn": "_integrations_158_EnterpriseCrmEventbusProtoParameterEntryIn",
        "EnterpriseCrmEventbusProtoParameterEntryOut": "_integrations_159_EnterpriseCrmEventbusProtoParameterEntryOut",
        "EnterpriseCrmEventbusProtoTeardownTaskConfigIn": "_integrations_160_EnterpriseCrmEventbusProtoTeardownTaskConfigIn",
        "EnterpriseCrmEventbusProtoTeardownTaskConfigOut": "_integrations_161_EnterpriseCrmEventbusProtoTeardownTaskConfigOut",
        "GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseIn": "_integrations_162_GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseIn",
        "GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseOut": "_integrations_163_GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseOut",
        "GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequestIn": "_integrations_164_GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequestIn",
        "GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequestOut": "_integrations_165_GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequestOut",
        "GoogleCloudIntegrationsV1alphaPublishIntegrationVersionRequestIn": "_integrations_166_GoogleCloudIntegrationsV1alphaPublishIntegrationVersionRequestIn",
        "GoogleCloudIntegrationsV1alphaPublishIntegrationVersionRequestOut": "_integrations_167_GoogleCloudIntegrationsV1alphaPublishIntegrationVersionRequestOut",
        "EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsIn": "_integrations_168_EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsIn",
        "EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsOut": "_integrations_169_EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsOut",
        "EnterpriseCrmEventbusProtoBaseValueIn": "_integrations_170_EnterpriseCrmEventbusProtoBaseValueIn",
        "EnterpriseCrmEventbusProtoBaseValueOut": "_integrations_171_EnterpriseCrmEventbusProtoBaseValueOut",
        "GoogleCloudConnectorsV1DestinationConfigIn": "_integrations_172_GoogleCloudConnectorsV1DestinationConfigIn",
        "GoogleCloudConnectorsV1DestinationConfigOut": "_integrations_173_GoogleCloudConnectorsV1DestinationConfigOut",
        "GoogleCloudConnectorsV1LockConfigIn": "_integrations_174_GoogleCloudConnectorsV1LockConfigIn",
        "GoogleCloudConnectorsV1LockConfigOut": "_integrations_175_GoogleCloudConnectorsV1LockConfigOut",
        "EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn": "_integrations_176_EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn",
        "EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut": "_integrations_177_EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut",
        "EnterpriseCrmEventbusProtoFunctionTypeIn": "_integrations_178_EnterpriseCrmEventbusProtoFunctionTypeIn",
        "EnterpriseCrmEventbusProtoFunctionTypeOut": "_integrations_179_EnterpriseCrmEventbusProtoFunctionTypeOut",
        "EnterpriseCrmEventbusStatsDimensionsIn": "_integrations_180_EnterpriseCrmEventbusStatsDimensionsIn",
        "EnterpriseCrmEventbusStatsDimensionsOut": "_integrations_181_EnterpriseCrmEventbusStatsDimensionsOut",
        "GoogleCloudConnectorsV1NodeConfigIn": "_integrations_182_GoogleCloudConnectorsV1NodeConfigIn",
        "GoogleCloudConnectorsV1NodeConfigOut": "_integrations_183_GoogleCloudConnectorsV1NodeConfigOut",
        "EnterpriseCrmEventbusProtoNextTaskIn": "_integrations_184_EnterpriseCrmEventbusProtoNextTaskIn",
        "EnterpriseCrmEventbusProtoNextTaskOut": "_integrations_185_EnterpriseCrmEventbusProtoNextTaskOut",
        "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueIn": "_integrations_186_GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueIn",
        "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueOut": "_integrations_187_GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueOut",
        "GoogleCloudIntegrationsV1alphaClientCertificateIn": "_integrations_188_GoogleCloudIntegrationsV1alphaClientCertificateIn",
        "GoogleCloudIntegrationsV1alphaClientCertificateOut": "_integrations_189_GoogleCloudIntegrationsV1alphaClientCertificateOut",
        "GoogleCloudIntegrationsV1alphaCredentialIn": "_integrations_190_GoogleCloudIntegrationsV1alphaCredentialIn",
        "GoogleCloudIntegrationsV1alphaCredentialOut": "_integrations_191_GoogleCloudIntegrationsV1alphaCredentialOut",
        "EnterpriseCrmEventbusProtoConditionResultIn": "_integrations_192_EnterpriseCrmEventbusProtoConditionResultIn",
        "EnterpriseCrmEventbusProtoConditionResultOut": "_integrations_193_EnterpriseCrmEventbusProtoConditionResultOut",
        "GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponseIn": "_integrations_194_GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponseIn",
        "GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponseOut": "_integrations_195_GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponseOut",
        "GoogleCloudIntegrationsV1alphaListCertificatesResponseIn": "_integrations_196_GoogleCloudIntegrationsV1alphaListCertificatesResponseIn",
        "GoogleCloudIntegrationsV1alphaListCertificatesResponseOut": "_integrations_197_GoogleCloudIntegrationsV1alphaListCertificatesResponseOut",
        "EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueIn": "_integrations_198_EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueIn",
        "EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueOut": "_integrations_199_EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueOut",
        "GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequestIn": "_integrations_200_GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequestIn",
        "GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequestOut": "_integrations_201_GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequestOut",
        "EnterpriseCrmEventbusProtoBooleanArrayFunctionIn": "_integrations_202_EnterpriseCrmEventbusProtoBooleanArrayFunctionIn",
        "EnterpriseCrmEventbusProtoBooleanArrayFunctionOut": "_integrations_203_EnterpriseCrmEventbusProtoBooleanArrayFunctionOut",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeIn": "_integrations_204_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeIn",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeOut": "_integrations_205_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRangeOut",
        "EnterpriseCrmLoggingGwsSanitizeOptionsIn": "_integrations_206_EnterpriseCrmLoggingGwsSanitizeOptionsIn",
        "EnterpriseCrmLoggingGwsSanitizeOptionsOut": "_integrations_207_EnterpriseCrmLoggingGwsSanitizeOptionsOut",
        "EnterpriseCrmEventbusProtoTransformExpressionIn": "_integrations_208_EnterpriseCrmEventbusProtoTransformExpressionIn",
        "EnterpriseCrmEventbusProtoTransformExpressionOut": "_integrations_209_EnterpriseCrmEventbusProtoTransformExpressionOut",
        "GoogleCloudIntegrationsV1alphaTaskExecutionDetailsIn": "_integrations_210_GoogleCloudIntegrationsV1alphaTaskExecutionDetailsIn",
        "GoogleCloudIntegrationsV1alphaTaskExecutionDetailsOut": "_integrations_211_GoogleCloudIntegrationsV1alphaTaskExecutionDetailsOut",
        "EnterpriseCrmEventbusProtoLoopMetadataIn": "_integrations_212_EnterpriseCrmEventbusProtoLoopMetadataIn",
        "EnterpriseCrmEventbusProtoLoopMetadataOut": "_integrations_213_EnterpriseCrmEventbusProtoLoopMetadataOut",
        "EnterpriseCrmEventbusProtoProtoParameterArrayIn": "_integrations_214_EnterpriseCrmEventbusProtoProtoParameterArrayIn",
        "EnterpriseCrmEventbusProtoProtoParameterArrayOut": "_integrations_215_EnterpriseCrmEventbusProtoProtoParameterArrayOut",
        "GoogleCloudIntegrationsV1alphaCertificateIn": "_integrations_216_GoogleCloudIntegrationsV1alphaCertificateIn",
        "GoogleCloudIntegrationsV1alphaCertificateOut": "_integrations_217_GoogleCloudIntegrationsV1alphaCertificateOut",
        "EnterpriseCrmEventbusProtoLogSettingsIn": "_integrations_218_EnterpriseCrmEventbusProtoLogSettingsIn",
        "EnterpriseCrmEventbusProtoLogSettingsOut": "_integrations_219_EnterpriseCrmEventbusProtoLogSettingsOut",
        "EnterpriseCrmFrontendsEventbusProtoParameterEntryIn": "_integrations_220_EnterpriseCrmFrontendsEventbusProtoParameterEntryIn",
        "EnterpriseCrmFrontendsEventbusProtoParameterEntryOut": "_integrations_221_EnterpriseCrmFrontendsEventbusProtoParameterEntryOut",
        "EnterpriseCrmEventbusProtoBuganizerNotificationIn": "_integrations_222_EnterpriseCrmEventbusProtoBuganizerNotificationIn",
        "EnterpriseCrmEventbusProtoBuganizerNotificationOut": "_integrations_223_EnterpriseCrmEventbusProtoBuganizerNotificationOut",
        "EnterpriseCrmEventbusProtoTaskExecutionDetailsIn": "_integrations_224_EnterpriseCrmEventbusProtoTaskExecutionDetailsIn",
        "EnterpriseCrmEventbusProtoTaskExecutionDetailsOut": "_integrations_225_EnterpriseCrmEventbusProtoTaskExecutionDetailsOut",
        "EnterpriseCrmEventbusProtoTokenIn": "_integrations_226_EnterpriseCrmEventbusProtoTokenIn",
        "EnterpriseCrmEventbusProtoTokenOut": "_integrations_227_EnterpriseCrmEventbusProtoTokenOut",
        "GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseIn": "_integrations_228_GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseIn",
        "GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseOut": "_integrations_229_GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseOut",
        "EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsIn": "_integrations_230_EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsIn",
        "EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsOut": "_integrations_231_EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStatsOut",
        "GoogleCloudConnectorsV1ConnectionIn": "_integrations_232_GoogleCloudConnectorsV1ConnectionIn",
        "GoogleCloudConnectorsV1ConnectionOut": "_integrations_233_GoogleCloudConnectorsV1ConnectionOut",
        "EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn": "_integrations_234_EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn",
        "EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut": "_integrations_235_EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut",
        "GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeIn": "_integrations_236_GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeIn",
        "GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeOut": "_integrations_237_GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeOut",
        "GoogleCloudIntegrationsV1alphaListConnectionsResponseIn": "_integrations_238_GoogleCloudIntegrationsV1alphaListConnectionsResponseIn",
        "GoogleCloudIntegrationsV1alphaListConnectionsResponseOut": "_integrations_239_GoogleCloudIntegrationsV1alphaListConnectionsResponseOut",
        "GoogleCloudIntegrationsV1alphaExecutionDetailsIn": "_integrations_240_GoogleCloudIntegrationsV1alphaExecutionDetailsIn",
        "GoogleCloudIntegrationsV1alphaExecutionDetailsOut": "_integrations_241_GoogleCloudIntegrationsV1alphaExecutionDetailsOut",
        "EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayIn": "_integrations_242_EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayIn",
        "EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayOut": "_integrations_243_EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayOut",
        "GoogleCloudConnectorsV1ConfigVariableIn": "_integrations_244_GoogleCloudConnectorsV1ConfigVariableIn",
        "GoogleCloudConnectorsV1ConfigVariableOut": "_integrations_245_GoogleCloudConnectorsV1ConfigVariableOut",
        "GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsIn": "_integrations_246_GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsIn",
        "GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsOut": "_integrations_247_GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsOut",
        "GoogleCloudIntegrationsV1alphaTriggerConfigIn": "_integrations_248_GoogleCloudIntegrationsV1alphaTriggerConfigIn",
        "GoogleCloudIntegrationsV1alphaTriggerConfigOut": "_integrations_249_GoogleCloudIntegrationsV1alphaTriggerConfigOut",
        "GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestIn": "_integrations_250_GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestIn",
        "GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestOut": "_integrations_251_GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestOut",
        "EnterpriseCrmEventbusProtoConnectorsConnectionIn": "_integrations_252_EnterpriseCrmEventbusProtoConnectorsConnectionIn",
        "EnterpriseCrmEventbusProtoConnectorsConnectionOut": "_integrations_253_EnterpriseCrmEventbusProtoConnectorsConnectionOut",
        "GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsIn": "_integrations_254_GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsIn",
        "GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsOut": "_integrations_255_GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsOut",
        "EnterpriseCrmEventbusProtoParameterValueTypeIn": "_integrations_256_EnterpriseCrmEventbusProtoParameterValueTypeIn",
        "EnterpriseCrmEventbusProtoParameterValueTypeOut": "_integrations_257_EnterpriseCrmEventbusProtoParameterValueTypeOut",
        "EnterpriseCrmEventbusProtoCoordinateIn": "_integrations_258_EnterpriseCrmEventbusProtoCoordinateIn",
        "EnterpriseCrmEventbusProtoCoordinateOut": "_integrations_259_EnterpriseCrmEventbusProtoCoordinateOut",
        "EnterpriseCrmEventbusProtoBaseFunctionIn": "_integrations_260_EnterpriseCrmEventbusProtoBaseFunctionIn",
        "EnterpriseCrmEventbusProtoBaseFunctionOut": "_integrations_261_EnterpriseCrmEventbusProtoBaseFunctionOut",
        "EnterpriseCrmEventbusProtoParamSpecEntryConfigIn": "_integrations_262_EnterpriseCrmEventbusProtoParamSpecEntryConfigIn",
        "EnterpriseCrmEventbusProtoParamSpecEntryConfigOut": "_integrations_263_EnterpriseCrmEventbusProtoParamSpecEntryConfigOut",
        "GoogleProtobufEmptyIn": "_integrations_264_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_integrations_265_GoogleProtobufEmptyOut",
        "EnterpriseCrmEventbusProtoFieldIn": "_integrations_266_EnterpriseCrmEventbusProtoFieldIn",
        "EnterpriseCrmEventbusProtoFieldOut": "_integrations_267_EnterpriseCrmEventbusProtoFieldOut",
        "EnterpriseCrmEventbusProtoIntArrayFunctionIn": "_integrations_268_EnterpriseCrmEventbusProtoIntArrayFunctionIn",
        "EnterpriseCrmEventbusProtoIntArrayFunctionOut": "_integrations_269_EnterpriseCrmEventbusProtoIntArrayFunctionOut",
        "EnterpriseCrmEventbusProtoIntParameterArrayIn": "_integrations_270_EnterpriseCrmEventbusProtoIntParameterArrayIn",
        "EnterpriseCrmEventbusProtoIntParameterArrayOut": "_integrations_271_EnterpriseCrmEventbusProtoIntParameterArrayOut",
        "GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataIn": "_integrations_272_GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataIn",
        "GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataOut": "_integrations_273_GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataOut",
        "GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseIn": "_integrations_274_GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseIn",
        "GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseOut": "_integrations_275_GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseOut",
        "GoogleCloudIntegrationsV1alphaIntegrationIn": "_integrations_276_GoogleCloudIntegrationsV1alphaIntegrationIn",
        "GoogleCloudIntegrationsV1alphaIntegrationOut": "_integrations_277_GoogleCloudIntegrationsV1alphaIntegrationOut",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexIn": "_integrations_278_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexIn",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexOut": "_integrations_279_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexOut",
        "EnterpriseCrmEventbusProtoStringFunctionIn": "_integrations_280_EnterpriseCrmEventbusProtoStringFunctionIn",
        "EnterpriseCrmEventbusProtoStringFunctionOut": "_integrations_281_EnterpriseCrmEventbusProtoStringFunctionOut",
        "EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn": "_integrations_282_EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn",
        "EnterpriseCrmFrontendsEventbusProtoWorkflowParametersOut": "_integrations_283_EnterpriseCrmFrontendsEventbusProtoWorkflowParametersOut",
        "GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestIn": "_integrations_284_GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestIn",
        "GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestOut": "_integrations_285_GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestOut",
        "GoogleCloudIntegrationsV1alphaSuspensionAuditIn": "_integrations_286_GoogleCloudIntegrationsV1alphaSuspensionAuditIn",
        "GoogleCloudIntegrationsV1alphaSuspensionAuditOut": "_integrations_287_GoogleCloudIntegrationsV1alphaSuspensionAuditOut",
        "EnterpriseCrmEventbusProtoParameterMapFieldIn": "_integrations_288_EnterpriseCrmEventbusProtoParameterMapFieldIn",
        "EnterpriseCrmEventbusProtoParameterMapFieldOut": "_integrations_289_EnterpriseCrmEventbusProtoParameterMapFieldOut",
        "GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseIn": "_integrations_290_GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseIn",
        "GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseOut": "_integrations_291_GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseOut",
        "GoogleCloudIntegrationsV1alphaUploadIntegrationVersionResponseIn": "_integrations_292_GoogleCloudIntegrationsV1alphaUploadIntegrationVersionResponseIn",
        "GoogleCloudIntegrationsV1alphaUploadIntegrationVersionResponseOut": "_integrations_293_GoogleCloudIntegrationsV1alphaUploadIntegrationVersionResponseOut",
        "GoogleCloudConnectorsV1SecretIn": "_integrations_294_GoogleCloudConnectorsV1SecretIn",
        "GoogleCloudConnectorsV1SecretOut": "_integrations_295_GoogleCloudConnectorsV1SecretOut",
        "GoogleCloudIntegrationsV1alphaRuntimeActionSchemaIn": "_integrations_296_GoogleCloudIntegrationsV1alphaRuntimeActionSchemaIn",
        "GoogleCloudIntegrationsV1alphaRuntimeActionSchemaOut": "_integrations_297_GoogleCloudIntegrationsV1alphaRuntimeActionSchemaOut",
        "GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseIn": "_integrations_298_GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseIn",
        "GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseOut": "_integrations_299_GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseOut",
        "EnterpriseCrmEventbusProtoDoubleParameterArrayIn": "_integrations_300_EnterpriseCrmEventbusProtoDoubleParameterArrayIn",
        "EnterpriseCrmEventbusProtoDoubleParameterArrayOut": "_integrations_301_EnterpriseCrmEventbusProtoDoubleParameterArrayOut",
        "EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterIn": "_integrations_302_EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterIn",
        "EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterOut": "_integrations_303_EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterOut",
        "GoogleCloudConnectorsV1AuthConfigUserPasswordIn": "_integrations_304_GoogleCloudConnectorsV1AuthConfigUserPasswordIn",
        "GoogleCloudConnectorsV1AuthConfigUserPasswordOut": "_integrations_305_GoogleCloudConnectorsV1AuthConfigUserPasswordOut",
        "EnterpriseCrmFrontendsEventbusProtoIntParameterArrayIn": "_integrations_306_EnterpriseCrmFrontendsEventbusProtoIntParameterArrayIn",
        "EnterpriseCrmFrontendsEventbusProtoIntParameterArrayOut": "_integrations_307_EnterpriseCrmFrontendsEventbusProtoIntParameterArrayOut",
        "EnterpriseCrmFrontendsEventbusProtoParameterMapFieldIn": "_integrations_308_EnterpriseCrmFrontendsEventbusProtoParameterMapFieldIn",
        "EnterpriseCrmFrontendsEventbusProtoParameterMapFieldOut": "_integrations_309_EnterpriseCrmFrontendsEventbusProtoParameterMapFieldOut",
        "GoogleCloudIntegrationsV1alphaParameterMapFieldIn": "_integrations_310_GoogleCloudIntegrationsV1alphaParameterMapFieldIn",
        "GoogleCloudIntegrationsV1alphaParameterMapFieldOut": "_integrations_311_GoogleCloudIntegrationsV1alphaParameterMapFieldOut",
        "GoogleCloudIntegrationsV1alphaResolveSuspensionResponseIn": "_integrations_312_GoogleCloudIntegrationsV1alphaResolveSuspensionResponseIn",
        "GoogleCloudIntegrationsV1alphaResolveSuspensionResponseOut": "_integrations_313_GoogleCloudIntegrationsV1alphaResolveSuspensionResponseOut",
        "EnterpriseCrmEventbusProtoTaskAlertConfigIn": "_integrations_314_EnterpriseCrmEventbusProtoTaskAlertConfigIn",
        "EnterpriseCrmEventbusProtoTaskAlertConfigOut": "_integrations_315_EnterpriseCrmEventbusProtoTaskAlertConfigOut",
        "EnterpriseCrmEventbusProtoBooleanParameterArrayIn": "_integrations_316_EnterpriseCrmEventbusProtoBooleanParameterArrayIn",
        "EnterpriseCrmEventbusProtoBooleanParameterArrayOut": "_integrations_317_EnterpriseCrmEventbusProtoBooleanParameterArrayOut",
        "GoogleCloudConnectorsV1SslConfigIn": "_integrations_318_GoogleCloudConnectorsV1SslConfigIn",
        "GoogleCloudConnectorsV1SslConfigOut": "_integrations_319_GoogleCloudConnectorsV1SslConfigOut",
        "GoogleCloudConnectorsV1LogConfigIn": "_integrations_320_GoogleCloudConnectorsV1LogConfigIn",
        "GoogleCloudConnectorsV1LogConfigOut": "_integrations_321_GoogleCloudConnectorsV1LogConfigOut",
        "EnterpriseCrmEventbusProtoStringArrayIn": "_integrations_322_EnterpriseCrmEventbusProtoStringArrayIn",
        "EnterpriseCrmEventbusProtoStringArrayOut": "_integrations_323_EnterpriseCrmEventbusProtoStringArrayOut",
        "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityIn": "_integrations_324_EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityIn",
        "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityOut": "_integrations_325_EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityOut",
        "GoogleCloudIntegrationsV1alphaParameterMapEntryIn": "_integrations_326_GoogleCloudIntegrationsV1alphaParameterMapEntryIn",
        "GoogleCloudIntegrationsV1alphaParameterMapEntryOut": "_integrations_327_GoogleCloudIntegrationsV1alphaParameterMapEntryOut",
        "EnterpriseCrmEventbusProtoSuspensionResolutionInfoIn": "_integrations_328_EnterpriseCrmEventbusProtoSuspensionResolutionInfoIn",
        "EnterpriseCrmEventbusProtoSuspensionResolutionInfoOut": "_integrations_329_EnterpriseCrmEventbusProtoSuspensionResolutionInfoOut",
        "GoogleCloudIntegrationsV1alphaListExecutionsResponseIn": "_integrations_330_GoogleCloudIntegrationsV1alphaListExecutionsResponseIn",
        "GoogleCloudIntegrationsV1alphaListExecutionsResponseOut": "_integrations_331_GoogleCloudIntegrationsV1alphaListExecutionsResponseOut",
        "EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditIn": "_integrations_332_EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditIn",
        "EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditOut": "_integrations_333_EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditOut",
        "GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestIn": "_integrations_334_GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestIn",
        "GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestOut": "_integrations_335_GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestOut",
        "GoogleCloudIntegrationsV1alphaExecutionIn": "_integrations_336_GoogleCloudIntegrationsV1alphaExecutionIn",
        "GoogleCloudIntegrationsV1alphaExecutionOut": "_integrations_337_GoogleCloudIntegrationsV1alphaExecutionOut",
        "EnterpriseCrmEventbusProtoSerializedObjectParameterIn": "_integrations_338_EnterpriseCrmEventbusProtoSerializedObjectParameterIn",
        "EnterpriseCrmEventbusProtoSerializedObjectParameterOut": "_integrations_339_EnterpriseCrmEventbusProtoSerializedObjectParameterOut",
        "GoogleCloudIntegrationsV1alphaListIntegrationsResponseIn": "_integrations_340_GoogleCloudIntegrationsV1alphaListIntegrationsResponseIn",
        "GoogleCloudIntegrationsV1alphaListIntegrationsResponseOut": "_integrations_341_GoogleCloudIntegrationsV1alphaListIntegrationsResponseOut",
        "EnterpriseCrmEventbusProtoExecutionTraceInfoIn": "_integrations_342_EnterpriseCrmEventbusProtoExecutionTraceInfoIn",
        "EnterpriseCrmEventbusProtoExecutionTraceInfoOut": "_integrations_343_EnterpriseCrmEventbusProtoExecutionTraceInfoOut",
        "GoogleCloudIntegrationsV1alphaLiftSuspensionResponseIn": "_integrations_344_GoogleCloudIntegrationsV1alphaLiftSuspensionResponseIn",
        "GoogleCloudIntegrationsV1alphaLiftSuspensionResponseOut": "_integrations_345_GoogleCloudIntegrationsV1alphaLiftSuspensionResponseOut",
        "GoogleCloudIntegrationsV1alphaJwtIn": "_integrations_346_GoogleCloudIntegrationsV1alphaJwtIn",
        "GoogleCloudIntegrationsV1alphaJwtOut": "_integrations_347_GoogleCloudIntegrationsV1alphaJwtOut",
        "EnterpriseCrmEventbusProtoIntArrayIn": "_integrations_348_EnterpriseCrmEventbusProtoIntArrayIn",
        "EnterpriseCrmEventbusProtoIntArrayOut": "_integrations_349_EnterpriseCrmEventbusProtoIntArrayOut",
        "GoogleCloudConnectorsV1AuthConfigSshPublicKeyIn": "_integrations_350_GoogleCloudConnectorsV1AuthConfigSshPublicKeyIn",
        "GoogleCloudConnectorsV1AuthConfigSshPublicKeyOut": "_integrations_351_GoogleCloudConnectorsV1AuthConfigSshPublicKeyOut",
        "GoogleCloudIntegrationsV1alphaListAuthConfigsResponseIn": "_integrations_352_GoogleCloudIntegrationsV1alphaListAuthConfigsResponseIn",
        "GoogleCloudIntegrationsV1alphaListAuthConfigsResponseOut": "_integrations_353_GoogleCloudIntegrationsV1alphaListAuthConfigsResponseOut",
        "EnterpriseCrmEventbusProtoSuccessPolicyIn": "_integrations_354_EnterpriseCrmEventbusProtoSuccessPolicyIn",
        "EnterpriseCrmEventbusProtoSuccessPolicyOut": "_integrations_355_EnterpriseCrmEventbusProtoSuccessPolicyOut",
        "EnterpriseCrmFrontendsEventbusProtoEventParametersIn": "_integrations_356_EnterpriseCrmFrontendsEventbusProtoEventParametersIn",
        "EnterpriseCrmFrontendsEventbusProtoEventParametersOut": "_integrations_357_EnterpriseCrmFrontendsEventbusProtoEventParametersOut",
        "GoogleCloudIntegrationsV1alphaLiftSuspensionRequestIn": "_integrations_358_GoogleCloudIntegrationsV1alphaLiftSuspensionRequestIn",
        "GoogleCloudIntegrationsV1alphaLiftSuspensionRequestOut": "_integrations_359_GoogleCloudIntegrationsV1alphaLiftSuspensionRequestOut",
        "EnterpriseCrmEventbusProtoDoubleArrayFunctionIn": "_integrations_360_EnterpriseCrmEventbusProtoDoubleArrayFunctionIn",
        "EnterpriseCrmEventbusProtoDoubleArrayFunctionOut": "_integrations_361_EnterpriseCrmEventbusProtoDoubleArrayFunctionOut",
        "EnterpriseCrmFrontendsEventbusProtoRollbackStrategyIn": "_integrations_362_EnterpriseCrmFrontendsEventbusProtoRollbackStrategyIn",
        "EnterpriseCrmFrontendsEventbusProtoRollbackStrategyOut": "_integrations_363_EnterpriseCrmFrontendsEventbusProtoRollbackStrategyOut",
        "EnterpriseCrmEventbusProtoFieldMappingConfigIn": "_integrations_364_EnterpriseCrmEventbusProtoFieldMappingConfigIn",
        "EnterpriseCrmEventbusProtoFieldMappingConfigOut": "_integrations_365_EnterpriseCrmEventbusProtoFieldMappingConfigOut",
        "GoogleCloudIntegrationsV1alphaExecutionSnapshotIn": "_integrations_366_GoogleCloudIntegrationsV1alphaExecutionSnapshotIn",
        "GoogleCloudIntegrationsV1alphaExecutionSnapshotOut": "_integrations_367_GoogleCloudIntegrationsV1alphaExecutionSnapshotOut",
        "EnterpriseCrmEventbusProtoBooleanFunctionIn": "_integrations_368_EnterpriseCrmEventbusProtoBooleanFunctionIn",
        "EnterpriseCrmEventbusProtoBooleanFunctionOut": "_integrations_369_EnterpriseCrmEventbusProtoBooleanFunctionOut",
        "EnterpriseCrmFrontendsEventbusProtoParamSpecEntryIn": "_integrations_370_EnterpriseCrmFrontendsEventbusProtoParamSpecEntryIn",
        "EnterpriseCrmFrontendsEventbusProtoParamSpecEntryOut": "_integrations_371_EnterpriseCrmFrontendsEventbusProtoParamSpecEntryOut",
        "EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayIn": "_integrations_372_EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayIn",
        "EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayOut": "_integrations_373_EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayOut",
        "GoogleCloudIntegrationsV1alphaStringParameterArrayIn": "_integrations_374_GoogleCloudIntegrationsV1alphaStringParameterArrayIn",
        "GoogleCloudIntegrationsV1alphaStringParameterArrayOut": "_integrations_375_GoogleCloudIntegrationsV1alphaStringParameterArrayOut",
        "GoogleCloudIntegrationsV1alphaSfdcInstanceIn": "_integrations_376_GoogleCloudIntegrationsV1alphaSfdcInstanceIn",
        "GoogleCloudIntegrationsV1alphaSfdcInstanceOut": "_integrations_377_GoogleCloudIntegrationsV1alphaSfdcInstanceOut",
        "EnterpriseCrmEventbusProtoCombinedConditionIn": "_integrations_378_EnterpriseCrmEventbusProtoCombinedConditionIn",
        "EnterpriseCrmEventbusProtoCombinedConditionOut": "_integrations_379_EnterpriseCrmEventbusProtoCombinedConditionOut",
        "GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerIn": "_integrations_380_GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerIn",
        "GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerOut": "_integrations_381_GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerOut",
        "EnterpriseCrmEventbusProtoAddressIn": "_integrations_382_EnterpriseCrmEventbusProtoAddressIn",
        "EnterpriseCrmEventbusProtoAddressOut": "_integrations_383_EnterpriseCrmEventbusProtoAddressOut",
        "EnterpriseCrmEventbusProtoMappedFieldIn": "_integrations_384_EnterpriseCrmEventbusProtoMappedFieldIn",
        "EnterpriseCrmEventbusProtoMappedFieldOut": "_integrations_385_EnterpriseCrmEventbusProtoMappedFieldOut",
        "GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationIn": "_integrations_386_GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationIn",
        "GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationOut": "_integrations_387_GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationOut",
        "EnterpriseCrmEventbusProtoConnectorsGenericConnectorTaskConfigIn": "_integrations_388_EnterpriseCrmEventbusProtoConnectorsGenericConnectorTaskConfigIn",
        "EnterpriseCrmEventbusProtoConnectorsGenericConnectorTaskConfigOut": "_integrations_389_EnterpriseCrmEventbusProtoConnectorsGenericConnectorTaskConfigOut",
        "EnterpriseCrmEventbusProtoDoubleFunctionIn": "_integrations_390_EnterpriseCrmEventbusProtoDoubleFunctionIn",
        "EnterpriseCrmEventbusProtoDoubleFunctionOut": "_integrations_391_EnterpriseCrmEventbusProtoDoubleFunctionOut",
        "EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamIn": "_integrations_392_EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamIn",
        "EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamOut": "_integrations_393_EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamOut",
        "GoogleCloudIntegrationsV1alphaAuthConfigIn": "_integrations_394_GoogleCloudIntegrationsV1alphaAuthConfigIn",
        "GoogleCloudIntegrationsV1alphaAuthConfigOut": "_integrations_395_GoogleCloudIntegrationsV1alphaAuthConfigOut",
        "EnterpriseCrmEventbusProtoWorkflowAlertConfigIn": "_integrations_396_EnterpriseCrmEventbusProtoWorkflowAlertConfigIn",
        "EnterpriseCrmEventbusProtoWorkflowAlertConfigOut": "_integrations_397_EnterpriseCrmEventbusProtoWorkflowAlertConfigOut",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIn": "_integrations_398_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIn",
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleOut": "_integrations_399_EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleOut",
        "GoogleCloudIntegrationsV1alphaBooleanParameterArrayIn": "_integrations_400_GoogleCloudIntegrationsV1alphaBooleanParameterArrayIn",
        "GoogleCloudIntegrationsV1alphaBooleanParameterArrayOut": "_integrations_401_GoogleCloudIntegrationsV1alphaBooleanParameterArrayOut",
        "EnterpriseCrmEventbusProtoFailurePolicyIn": "_integrations_402_EnterpriseCrmEventbusProtoFailurePolicyIn",
        "EnterpriseCrmEventbusProtoFailurePolicyOut": "_integrations_403_EnterpriseCrmEventbusProtoFailurePolicyOut",
        "EnterpriseCrmLoggingGwsFieldLimitsIn": "_integrations_404_EnterpriseCrmLoggingGwsFieldLimitsIn",
        "EnterpriseCrmLoggingGwsFieldLimitsOut": "_integrations_405_EnterpriseCrmLoggingGwsFieldLimitsOut",
        "GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseIn": "_integrations_406_GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseIn",
        "GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseOut": "_integrations_407_GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseOut",
        "GoogleCloudIntegrationsV1alphaFailurePolicyIn": "_integrations_408_GoogleCloudIntegrationsV1alphaFailurePolicyIn",
        "GoogleCloudIntegrationsV1alphaFailurePolicyOut": "_integrations_409_GoogleCloudIntegrationsV1alphaFailurePolicyOut",
        "GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowIn": "_integrations_410_GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowIn",
        "GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowOut": "_integrations_411_GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowOut",
        "EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn": "_integrations_412_EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn",
        "EnterpriseCrmFrontendsEventbusProtoTriggerConfigOut": "_integrations_413_EnterpriseCrmFrontendsEventbusProtoTriggerConfigOut",
        "EnterpriseCrmEventbusProtoScatterResponseIn": "_integrations_414_EnterpriseCrmEventbusProtoScatterResponseIn",
        "EnterpriseCrmEventbusProtoScatterResponseOut": "_integrations_415_EnterpriseCrmEventbusProtoScatterResponseOut",
        "GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequestIn": "_integrations_416_GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequestIn",
        "GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequestOut": "_integrations_417_GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequestOut",
        "EnterpriseCrmEventbusProtoNotificationIn": "_integrations_418_EnterpriseCrmEventbusProtoNotificationIn",
        "EnterpriseCrmEventbusProtoNotificationOut": "_integrations_419_EnterpriseCrmEventbusProtoNotificationOut",
        "GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseIn": "_integrations_420_GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseIn",
        "GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseOut": "_integrations_421_GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseOut",
        "EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsIn": "_integrations_422_EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsIn",
        "EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsOut": "_integrations_423_EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsOut",
        "EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryIn": "_integrations_424_EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryIn",
        "EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryOut": "_integrations_425_EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryOut",
        "EnterpriseCrmEventbusProtoTaskMetadataAdminIn": "_integrations_426_EnterpriseCrmEventbusProtoTaskMetadataAdminIn",
        "EnterpriseCrmEventbusProtoTaskMetadataAdminOut": "_integrations_427_EnterpriseCrmEventbusProtoTaskMetadataAdminOut",
        "EnterpriseCrmEventbusProtoEventBusPropertiesIn": "_integrations_428_EnterpriseCrmEventbusProtoEventBusPropertiesIn",
        "EnterpriseCrmEventbusProtoEventBusPropertiesOut": "_integrations_429_EnterpriseCrmEventbusProtoEventBusPropertiesOut",
        "GoogleCloudIntegrationsV1alphaUsernameAndPasswordIn": "_integrations_430_GoogleCloudIntegrationsV1alphaUsernameAndPasswordIn",
        "GoogleCloudIntegrationsV1alphaUsernameAndPasswordOut": "_integrations_431_GoogleCloudIntegrationsV1alphaUsernameAndPasswordOut",
        "GoogleCloudIntegrationsV1alphaCoordinateIn": "_integrations_432_GoogleCloudIntegrationsV1alphaCoordinateIn",
        "GoogleCloudIntegrationsV1alphaCoordinateOut": "_integrations_433_GoogleCloudIntegrationsV1alphaCoordinateOut",
        "GoogleCloudIntegrationsV1alphaDoubleParameterArrayIn": "_integrations_434_GoogleCloudIntegrationsV1alphaDoubleParameterArrayIn",
        "GoogleCloudIntegrationsV1alphaDoubleParameterArrayOut": "_integrations_435_GoogleCloudIntegrationsV1alphaDoubleParameterArrayOut",
        "EnterpriseCrmFrontendsEventbusProtoParameterMapEntryIn": "_integrations_436_EnterpriseCrmFrontendsEventbusProtoParameterMapEntryIn",
        "EnterpriseCrmFrontendsEventbusProtoParameterMapEntryOut": "_integrations_437_EnterpriseCrmFrontendsEventbusProtoParameterMapEntryOut",
        "GoogleCloudIntegrationsV1alphaServiceAccountCredentialsIn": "_integrations_438_GoogleCloudIntegrationsV1alphaServiceAccountCredentialsIn",
        "GoogleCloudIntegrationsV1alphaServiceAccountCredentialsOut": "_integrations_439_GoogleCloudIntegrationsV1alphaServiceAccountCredentialsOut",
        "EnterpriseCrmEventbusProtoAttributesIn": "_integrations_440_EnterpriseCrmEventbusProtoAttributesIn",
        "EnterpriseCrmEventbusProtoAttributesOut": "_integrations_441_EnterpriseCrmEventbusProtoAttributesOut",
        "EnterpriseCrmEventbusProtoIntFunctionIn": "_integrations_442_EnterpriseCrmEventbusProtoIntFunctionIn",
        "EnterpriseCrmEventbusProtoIntFunctionOut": "_integrations_443_EnterpriseCrmEventbusProtoIntFunctionOut",
        "EnterpriseCrmEventbusProtoValueTypeIn": "_integrations_444_EnterpriseCrmEventbusProtoValueTypeIn",
        "EnterpriseCrmEventbusProtoValueTypeOut": "_integrations_445_EnterpriseCrmEventbusProtoValueTypeOut",
        "GoogleCloudIntegrationsV1alphaCancelExecutionRequestIn": "_integrations_446_GoogleCloudIntegrationsV1alphaCancelExecutionRequestIn",
        "GoogleCloudIntegrationsV1alphaCancelExecutionRequestOut": "_integrations_447_GoogleCloudIntegrationsV1alphaCancelExecutionRequestOut",
        "EnterpriseCrmFrontendsEventbusProtoTaskConfigIn": "_integrations_448_EnterpriseCrmFrontendsEventbusProtoTaskConfigIn",
        "EnterpriseCrmFrontendsEventbusProtoTaskConfigOut": "_integrations_449_EnterpriseCrmFrontendsEventbusProtoTaskConfigOut",
        "GoogleCloudIntegrationsV1alphaEventParameterIn": "_integrations_450_GoogleCloudIntegrationsV1alphaEventParameterIn",
        "GoogleCloudIntegrationsV1alphaEventParameterOut": "_integrations_451_GoogleCloudIntegrationsV1alphaEventParameterOut",
        "GoogleCloudIntegrationsV1alphaAccessTokenIn": "_integrations_452_GoogleCloudIntegrationsV1alphaAccessTokenIn",
        "GoogleCloudIntegrationsV1alphaAccessTokenOut": "_integrations_453_GoogleCloudIntegrationsV1alphaAccessTokenOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudIntegrationsV1alphaCancelExecutionResponseIn"] = t.struct(
        {"isCanceled": t.boolean().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaCancelExecutionResponseIn"])
    types["GoogleCloudIntegrationsV1alphaCancelExecutionResponseOut"] = t.struct(
        {
            "isCanceled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCancelExecutionResponseOut"])
    types["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestIn"] = t.struct(
        {"scriptId": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestIn"])
    types["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestOut"] = t.struct(
        {
            "scriptId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequestOut"])
    types["GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn"] = t.struct(
        {
            "errorCatcherNumber": t.string(),
            "label": t.string().optional(),
            "errorCatcherId": t.string(),
            "startErrorTasks": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaNextTaskIn"])
            ),
            "position": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCoordinateIn"]
            ).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn"])
    types["GoogleCloudIntegrationsV1alphaErrorCatcherConfigOut"] = t.struct(
        {
            "errorCatcherNumber": t.string(),
            "label": t.string().optional(),
            "errorCatcherId": t.string(),
            "startErrorTasks": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaNextTaskOut"])
            ),
            "position": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCoordinateOut"]
            ).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigOut"])
    types["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigIn"] = t.struct(
        {
            "thresholdValue": t.proxy(
                renames[
                    "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueIn"
                ]
            ).optional(),
            "disableAlert": t.boolean().optional(),
            "onlyFinalAttempt": t.boolean().optional(),
            "metricType": t.string().optional(),
            "durationThreshold": t.string().optional(),
            "aggregationPeriod": t.string().optional(),
            "alertThreshold": t.integer().optional(),
            "thresholdType": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigIn"])
    types["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigOut"] = t.struct(
        {
            "thresholdValue": t.proxy(
                renames[
                    "GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValueOut"
                ]
            ).optional(),
            "disableAlert": t.boolean().optional(),
            "onlyFinalAttempt": t.boolean().optional(),
            "metricType": t.string().optional(),
            "durationThreshold": t.string().optional(),
            "aggregationPeriod": t.string().optional(),
            "alertThreshold": t.integer().optional(),
            "thresholdType": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigOut"])
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
    types["GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaIn"] = t.struct(
        {
            "entity": t.string().optional(),
            "arrayFieldSchema": t.string().optional(),
            "fieldSchema": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaIn"])
    types["GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaOut"] = t.struct(
        {
            "entity": t.string().optional(),
            "arrayFieldSchema": t.string().optional(),
            "fieldSchema": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaRuntimeEntitySchemaOut"])
    types["EnterpriseCrmEventbusProtoTaskUiModuleConfigIn"] = t.struct(
        {"moduleId": t.string().optional()}
    ).named(renames["EnterpriseCrmEventbusProtoTaskUiModuleConfigIn"])
    types["EnterpriseCrmEventbusProtoTaskUiModuleConfigOut"] = t.struct(
        {
            "moduleId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskUiModuleConfigOut"])
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
    types["GoogleCloudIntegrationsV1alphaIntParameterArrayIn"] = t.struct(
        {"intValues": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaIntParameterArrayIn"])
    types["GoogleCloudIntegrationsV1alphaIntParameterArrayOut"] = t.struct(
        {
            "intValues": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntParameterArrayOut"])
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
    types["GoogleCloudConnectorsV1ConnectionStatusIn"] = t.struct(
        {
            "description": t.string().optional(),
            "state": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1ConnectionStatusIn"])
    types["GoogleCloudConnectorsV1ConnectionStatusOut"] = t.struct(
        {
            "description": t.string().optional(),
            "state": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1ConnectionStatusOut"])
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
    types["EnterpriseCrmFrontendsEventbusProtoStringParameterArrayIn"] = t.struct(
        {"stringValues": t.array(t.string())}
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoStringParameterArrayIn"])
    types["EnterpriseCrmFrontendsEventbusProtoStringParameterArrayOut"] = t.struct(
        {
            "stringValues": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoStringParameterArrayOut"])
    types["EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayIn"] = t.struct(
        {"doubleValues": t.array(t.number())}
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayIn"])
    types["EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayOut"] = t.struct(
        {
            "doubleValues": t.array(t.number()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayOut"])
    types["GoogleCloudConnectorsV1AuthConfigIn"] = t.struct(
        {
            "oauth2AuthCodeFlow": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowIn"]
            ).optional(),
            "authKey": t.string().optional(),
            "oauth2ClientCredentials": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsIn"]
            ).optional(),
            "sshPublicKey": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigSshPublicKeyIn"]
            ).optional(),
            "userPassword": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigUserPasswordIn"]
            ).optional(),
            "additionalVariables": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConfigVariableIn"])
            ).optional(),
            "authType": t.string().optional(),
            "oauth2JwtBearer": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigIn"])
    types["GoogleCloudConnectorsV1AuthConfigOut"] = t.struct(
        {
            "oauth2AuthCodeFlow": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowOut"]
            ).optional(),
            "authKey": t.string().optional(),
            "oauth2ClientCredentials": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentialsOut"]
            ).optional(),
            "sshPublicKey": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigSshPublicKeyOut"]
            ).optional(),
            "userPassword": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigUserPasswordOut"]
            ).optional(),
            "additionalVariables": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConfigVariableOut"])
            ).optional(),
            "authType": t.string().optional(),
            "oauth2JwtBearer": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigOut"])
    types["EnterpriseCrmEventbusProtoConditionIn"] = t.struct(
        {
            "operator": t.string().optional(),
            "value": t.proxy(
                renames["EnterpriseCrmEventbusProtoValueTypeIn"]
            ).optional(),
            "eventPropertyKey": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoConditionIn"])
    types["EnterpriseCrmEventbusProtoConditionOut"] = t.struct(
        {
            "operator": t.string().optional(),
            "value": t.proxy(
                renames["EnterpriseCrmEventbusProtoValueTypeOut"]
            ).optional(),
            "eventPropertyKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoConditionOut"])
    types["GoogleCloudIntegrationsV1alphaSfdcChannelIn"] = t.struct(
        {
            "description": t.string().optional(),
            "channelTopic": t.string().optional(),
            "lastReplayId": t.string().optional(),
            "displayName": t.string().optional(),
            "isActive": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSfdcChannelIn"])
    types["GoogleCloudIntegrationsV1alphaSfdcChannelOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "deleteTime": t.string().optional(),
            "channelTopic": t.string().optional(),
            "lastReplayId": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "isActive": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"])
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
    types["EnterpriseCrmFrontendsEventbusProtoTaskEntityIn"] = t.struct(
        {
            "uiConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoTaskUiConfigIn"]
            ).optional(),
            "paramSpecs": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageIn"]
            ).optional(),
            "stats": t.proxy(renames["EnterpriseCrmEventbusStatsIn"]).optional(),
            "taskType": t.string().optional(),
            "metadata": t.proxy(
                renames["EnterpriseCrmEventbusProtoTaskMetadataIn"]
            ).optional(),
            "disabledForVpcSc": t.boolean().optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoTaskEntityIn"])
    types["EnterpriseCrmFrontendsEventbusProtoTaskEntityOut"] = t.struct(
        {
            "uiConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoTaskUiConfigOut"]
            ).optional(),
            "paramSpecs": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParamSpecsMessageOut"]
            ).optional(),
            "stats": t.proxy(renames["EnterpriseCrmEventbusStatsOut"]).optional(),
            "taskType": t.string().optional(),
            "metadata": t.proxy(
                renames["EnterpriseCrmEventbusProtoTaskMetadataOut"]
            ).optional(),
            "disabledForVpcSc": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoTaskEntityOut"])
    types["EnterpriseCrmEventbusProtoErrorDetailIn"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "severity": t.string().optional(),
            "taskNumber": t.integer().optional(),
            "errorCode": t.proxy(renames["CrmlogErrorCodeIn"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoErrorDetailIn"])
    types["EnterpriseCrmEventbusProtoErrorDetailOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "severity": t.string().optional(),
            "taskNumber": t.integer().optional(),
            "errorCode": t.proxy(renames["CrmlogErrorCodeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoErrorDetailOut"])
    types["GoogleCloudIntegrationsV1alphaIntegrationParameterIn"] = t.struct(
        {
            "searchable": t.boolean().optional(),
            "inputOutputType": t.string().optional(),
            "defaultValue": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaValueTypeIn"]
            ).optional(),
            "producer": t.string().optional(),
            "jsonSchema": t.string().optional(),
            "dataType": t.string().optional(),
            "key": t.string().optional(),
            "displayName": t.string().optional(),
            "isTransient": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationParameterIn"])
    types["GoogleCloudIntegrationsV1alphaIntegrationParameterOut"] = t.struct(
        {
            "searchable": t.boolean().optional(),
            "inputOutputType": t.string().optional(),
            "defaultValue": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaValueTypeOut"]
            ).optional(),
            "producer": t.string().optional(),
            "jsonSchema": t.string().optional(),
            "dataType": t.string().optional(),
            "key": t.string().optional(),
            "displayName": t.string().optional(),
            "isTransient": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationParameterOut"])
    types["EnterpriseCrmEventbusProtoStringArrayFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoStringArrayFunctionIn"])
    types["EnterpriseCrmEventbusProtoStringArrayFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoStringArrayFunctionOut"])
    types["EnterpriseCrmEventbusProtoTaskMetadataIn"] = t.struct(
        {
            "description": t.string().optional(),
            "externalCategory": t.string(),
            "admins": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskMetadataAdminIn"])
            ),
            "externalDocMarkdown": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "standaloneExternalDocHtml": t.string().optional(),
            "defaultJsonValidationOption": t.string().optional(),
            "category": t.string(),
            "isDeprecated": t.boolean().optional(),
            "iconLink": t.string().optional(),
            "descriptiveName": t.string().optional(),
            "status": t.string().optional(),
            "externalDocHtml": t.string().optional(),
            "activeTaskName": t.string().optional(),
            "externalCategorySequence": t.integer().optional(),
            "g3DocLink": t.string().optional(),
            "externalDocLink": t.string().optional(),
            "defaultSpec": t.string().optional(),
            "system": t.string(),
            "codeSearchLink": t.string().optional(),
            "name": t.string().optional(),
            "docMarkdown": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskMetadataIn"])
    types["EnterpriseCrmEventbusProtoTaskMetadataOut"] = t.struct(
        {
            "description": t.string().optional(),
            "externalCategory": t.string(),
            "admins": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskMetadataAdminOut"])
            ),
            "externalDocMarkdown": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "standaloneExternalDocHtml": t.string().optional(),
            "defaultJsonValidationOption": t.string().optional(),
            "category": t.string(),
            "isDeprecated": t.boolean().optional(),
            "iconLink": t.string().optional(),
            "descriptiveName": t.string().optional(),
            "status": t.string().optional(),
            "externalDocHtml": t.string().optional(),
            "activeTaskName": t.string().optional(),
            "externalCategorySequence": t.integer().optional(),
            "g3DocLink": t.string().optional(),
            "externalDocLink": t.string().optional(),
            "defaultSpec": t.string().optional(),
            "system": t.string(),
            "codeSearchLink": t.string().optional(),
            "name": t.string().optional(),
            "docMarkdown": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskMetadataOut"])
    types[
        "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataIn"
    ] = t.struct(
        {
            "taskLabel": t.string().optional(),
            "eventAttemptNum": t.integer().optional(),
            "taskName": t.string().optional(),
            "taskAttemptNum": t.integer().optional(),
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
            "taskLabel": t.string().optional(),
            "eventAttemptNum": t.integer().optional(),
            "taskName": t.string().optional(),
            "taskAttemptNum": t.integer().optional(),
            "taskNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataOut"
        ]
    )
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
    types["GoogleCloudIntegrationsV1alphaSuspensionIn"] = t.struct(
        {
            "eventExecutionInfoId": t.string(),
            "integration": t.string(),
            "name": t.string().optional(),
            "approvalConfig": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigIn"]
            ).optional(),
            "audit": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuspensionAuditIn"]
            ).optional(),
            "taskId": t.string(),
            "suspensionConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionConfigIn"]
            ).optional(),
            "state": t.string(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSuspensionIn"])
    types["GoogleCloudIntegrationsV1alphaSuspensionOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "eventExecutionInfoId": t.string(),
            "integration": t.string(),
            "name": t.string().optional(),
            "approvalConfig": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigOut"]
            ).optional(),
            "lastModifyTime": t.string().optional(),
            "audit": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuspensionAuditOut"]
            ).optional(),
            "taskId": t.string(),
            "suspensionConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionConfigOut"]
            ).optional(),
            "state": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSuspensionOut"])
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
    types["CrmlogErrorCodeIn"] = t.struct({"commonErrorCode": t.string()}).named(
        renames["CrmlogErrorCodeIn"]
    )
    types["CrmlogErrorCodeOut"] = t.struct(
        {
            "commonErrorCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CrmlogErrorCodeOut"])
    types["EnterpriseCrmEventbusProtoNextTeardownTaskIn"] = t.struct(
        {"name": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoNextTeardownTaskIn"])
    types["EnterpriseCrmEventbusProtoNextTeardownTaskOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EnterpriseCrmEventbusProtoNextTeardownTaskOut"])
    types["EnterpriseCrmEventbusProtoCloudKmsConfigIn"] = t.struct(
        {
            "gcpProjectId": t.string().optional(),
            "keyVersionName": t.string().optional(),
            "keyName": t.string().optional(),
            "keyRingName": t.string().optional(),
            "locationName": t.string().optional(),
            "serviceAccount": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoCloudKmsConfigIn"])
    types["EnterpriseCrmEventbusProtoCloudKmsConfigOut"] = t.struct(
        {
            "gcpProjectId": t.string().optional(),
            "keyVersionName": t.string().optional(),
            "keyName": t.string().optional(),
            "keyRingName": t.string().optional(),
            "locationName": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoCloudKmsConfigOut"])
    types["GoogleCloudIntegrationsV1alphaIntegrationVersionIn"] = t.struct(
        {
            "taskConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaTaskConfigIn"])
            ).optional(),
            "runAsServiceAccount": t.string().optional(),
            "integrationParametersInternal": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn"]
            ).optional(),
            "integrationParameters": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationParameterIn"])
            ).optional(),
            "origin": t.string().optional(),
            "taskConfigsInternal": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigIn"])
            ).optional(),
            "teardown": t.proxy(
                renames["EnterpriseCrmEventbusProtoTeardownIn"]
            ).optional(),
            "errorCatcherConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn"])
            ).optional(),
            "lockHolder": t.string().optional(),
            "snapshotNumber": t.string().optional(),
            "triggerConfigsInternal": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn"])
            ).optional(),
            "parentTemplateId": t.string().optional(),
            "databasePersistencePolicy": t.string().optional(),
            "triggerConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaTriggerConfigIn"])
            ).optional(),
            "userLabel": t.string().optional(),
            "lastModifierEmail": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionIn"])
    types["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"] = t.struct(
        {
            "taskConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaTaskConfigOut"])
            ).optional(),
            "name": t.string().optional(),
            "status": t.string().optional(),
            "runAsServiceAccount": t.string().optional(),
            "integrationParametersInternal": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersOut"]
            ).optional(),
            "integrationParameters": t.array(
                t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaIntegrationParameterOut"]
                )
            ).optional(),
            "state": t.string().optional(),
            "origin": t.string().optional(),
            "taskConfigsInternal": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigOut"])
            ).optional(),
            "teardown": t.proxy(
                renames["EnterpriseCrmEventbusProtoTeardownOut"]
            ).optional(),
            "errorCatcherConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigOut"])
            ).optional(),
            "lockHolder": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "snapshotNumber": t.string().optional(),
            "triggerConfigsInternal": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigOut"])
            ).optional(),
            "parentTemplateId": t.string().optional(),
            "databasePersistencePolicy": t.string().optional(),
            "triggerConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaTriggerConfigOut"])
            ).optional(),
            "userLabel": t.string().optional(),
            "lastModifierEmail": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterMapIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoParameterMapEntryIn"]
                )
            ),
            "keyType": t.string().optional(),
            "valueType": t.string(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterMapIn"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterMapOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoParameterMapEntryOut"]
                )
            ),
            "keyType": t.string().optional(),
            "valueType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterMapOut"])
    types["GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestIn"] = t.struct(
        {
            "scheduleTime": t.string().optional(),
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersIn"]
            ).optional(),
            "requestId": t.string().optional(),
            "inputParameters": t.struct({"_": t.string().optional()}).optional(),
            "triggerId": t.string().optional(),
            "parameterEntries": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestIn"])
    types["GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestOut"] = t.struct(
        {
            "scheduleTime": t.string().optional(),
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersOut"]
            ).optional(),
            "requestId": t.string().optional(),
            "inputParameters": t.struct({"_": t.string().optional()}).optional(),
            "triggerId": t.string().optional(),
            "parameterEntries": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequestOut"])
    types["GoogleCloudIntegrationsV1alphaTaskConfigIn"] = t.struct(
        {
            "jsonValidationOption": t.string().optional(),
            "externalTaskType": t.string().optional(),
            "taskTemplate": t.string().optional(),
            "task": t.string().optional(),
            "synchronousCallFailurePolicy": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaFailurePolicyIn"]
            ).optional(),
            "errorCatcherId": t.string().optional(),
            "description": t.string().optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "taskExecutionStrategy": t.string().optional(),
            "displayName": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "nextTasks": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaNextTaskIn"])
            ).optional(),
            "successPolicy": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuccessPolicyIn"]
            ).optional(),
            "taskId": t.string(),
            "position": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCoordinateIn"]
            ).optional(),
            "failurePolicy": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaFailurePolicyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaTaskConfigIn"])
    types["GoogleCloudIntegrationsV1alphaTaskConfigOut"] = t.struct(
        {
            "jsonValidationOption": t.string().optional(),
            "externalTaskType": t.string().optional(),
            "taskTemplate": t.string().optional(),
            "task": t.string().optional(),
            "synchronousCallFailurePolicy": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaFailurePolicyOut"]
            ).optional(),
            "errorCatcherId": t.string().optional(),
            "description": t.string().optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "taskExecutionStrategy": t.string().optional(),
            "displayName": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "nextTasks": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaNextTaskOut"])
            ).optional(),
            "successPolicy": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuccessPolicyOut"]
            ).optional(),
            "taskId": t.string(),
            "position": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCoordinateOut"]
            ).optional(),
            "failurePolicy": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaFailurePolicyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaTaskConfigOut"])
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
    types["EnterpriseCrmEventbusProtoParameterMapIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoParameterMapEntryIn"])
            ),
            "valueType": t.string(),
            "keyType": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParameterMapIn"])
    types["EnterpriseCrmEventbusProtoParameterMapOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoParameterMapEntryOut"])
            ),
            "valueType": t.string(),
            "keyType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParameterMapOut"])
    types["EnterpriseCrmEventbusProtoStringParameterArrayIn"] = t.struct(
        {"stringValues": t.array(t.string())}
    ).named(renames["EnterpriseCrmEventbusProtoStringParameterArrayIn"])
    types["EnterpriseCrmEventbusProtoStringParameterArrayOut"] = t.struct(
        {
            "stringValues": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoStringParameterArrayOut"])
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
    types["GoogleCloudIntegrationsV1alphaValueTypeIn"] = t.struct(
        {
            "jsonValue": t.string().optional(),
            "doubleArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaDoubleParameterArrayIn"]
            ).optional(),
            "stringArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaStringParameterArrayIn"]
            ).optional(),
            "stringValue": t.string().optional(),
            "booleanArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaBooleanParameterArrayIn"]
            ).optional(),
            "booleanValue": t.boolean().optional(),
            "doubleValue": t.number().optional(),
            "intValue": t.string().optional(),
            "intArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaIntParameterArrayIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaValueTypeIn"])
    types["GoogleCloudIntegrationsV1alphaValueTypeOut"] = t.struct(
        {
            "jsonValue": t.string().optional(),
            "doubleArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaDoubleParameterArrayOut"]
            ).optional(),
            "stringArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaStringParameterArrayOut"]
            ).optional(),
            "stringValue": t.string().optional(),
            "booleanArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaBooleanParameterArrayOut"]
            ).optional(),
            "booleanValue": t.boolean().optional(),
            "doubleValue": t.number().optional(),
            "intValue": t.string().optional(),
            "intArray": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaIntParameterArrayOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaValueTypeOut"])
    types["EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotIn"] = t.struct(
        {
            "snapshotTime": t.string().optional(),
            "eventExecutionSnapshotId": t.string().optional(),
            "taskExecutionDetails": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskExecutionDetailsIn"])
            ).optional(),
            "eventExecutionSnapshotMetadata": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataIn"
                ]
            ),
            "eventExecutionInfoId": t.string().optional(),
            "taskName": t.string().optional(),
            "eventParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
            ).optional(),
            "conditionResults": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoConditionResultIn"])
            ).optional(),
            "diffParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
            ).optional(),
            "checkpointTaskNumber": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotIn"])
    types["EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotOut"] = t.struct(
        {
            "snapshotTime": t.string().optional(),
            "eventExecutionSnapshotId": t.string().optional(),
            "taskExecutionDetails": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskExecutionDetailsOut"])
            ).optional(),
            "eventExecutionSnapshotMetadata": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataOut"
                ]
            ),
            "eventExecutionInfoId": t.string().optional(),
            "taskName": t.string().optional(),
            "eventParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "conditionResults": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoConditionResultOut"])
            ).optional(),
            "diffParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "checkpointTaskNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotOut"])
    types["EnterpriseCrmEventbusProtoExternalTrafficIn"] = t.struct(
        {
            "source": t.string().optional(),
            "gcpProjectId": t.string().optional(),
            "gcpProjectNumber": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoExternalTrafficIn"])
    types["EnterpriseCrmEventbusProtoExternalTrafficOut"] = t.struct(
        {
            "source": t.string().optional(),
            "gcpProjectId": t.string().optional(),
            "gcpProjectNumber": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoExternalTrafficOut"])
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
    types["EnterpriseCrmEventbusProtoJsonFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoJsonFunctionIn"])
    types["EnterpriseCrmEventbusProtoJsonFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoJsonFunctionOut"])
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
    types["GoogleCloudIntegrationsV1alphaSuccessPolicyIn"] = t.struct(
        {"finalState": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaSuccessPolicyIn"])
    types["GoogleCloudIntegrationsV1alphaSuccessPolicyOut"] = t.struct(
        {
            "finalState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSuccessPolicyOut"])
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
    types["EnterpriseCrmEventbusProtoProtoFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoProtoFunctionIn"])
    types["EnterpriseCrmEventbusProtoProtoFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoProtoFunctionOut"])
    types["EnterpriseCrmEventbusProtoEventExecutionSnapshotIn"] = t.struct(
        {
            "checkpointTaskNumber": t.string().optional(),
            "taskName": t.string().optional(),
            "taskExecutionDetails": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskExecutionDetailsIn"])
            ).optional(),
            "conditionResults": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoConditionResultIn"])
            ).optional(),
            "eventParams": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersIn"]
            ).optional(),
            "diffParams": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersIn"]
            ).optional(),
            "eventExecutionInfoId": t.string().optional(),
            "snapshotTime": t.string().optional(),
            "eventExecutionSnapshotMetadata": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataIn"
                ]
            ),
            "eventExecutionSnapshotId": t.string().optional(),
            "exceedMaxSize": t.boolean().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoEventExecutionSnapshotIn"])
    types["EnterpriseCrmEventbusProtoEventExecutionSnapshotOut"] = t.struct(
        {
            "checkpointTaskNumber": t.string().optional(),
            "taskName": t.string().optional(),
            "taskExecutionDetails": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskExecutionDetailsOut"])
            ).optional(),
            "conditionResults": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoConditionResultOut"])
            ).optional(),
            "eventParams": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersOut"]
            ).optional(),
            "diffParams": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersOut"]
            ).optional(),
            "eventExecutionInfoId": t.string().optional(),
            "snapshotTime": t.string().optional(),
            "eventExecutionSnapshotMetadata": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadataOut"
                ]
            ),
            "eventExecutionSnapshotId": t.string().optional(),
            "exceedMaxSize": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoEventExecutionSnapshotOut"])
    types["EnterpriseCrmEventbusProtoSuspensionExpirationIn"] = t.struct(
        {
            "expireAfterMs": t.integer().optional(),
            "liftWhenExpired": t.boolean().optional(),
            "remindAfterMs": t.integer().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionExpirationIn"])
    types["EnterpriseCrmEventbusProtoSuspensionExpirationOut"] = t.struct(
        {
            "expireAfterMs": t.integer().optional(),
            "liftWhenExpired": t.boolean().optional(),
            "remindAfterMs": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionExpirationOut"])
    types["GoogleCloudIntegrationsV1alphaOidcTokenIn"] = t.struct(
        {
            "serviceAccountEmail": t.string().optional(),
            "tokenExpireTime": t.string().optional(),
            "token": t.string().optional(),
            "audience": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOidcTokenIn"])
    types["GoogleCloudIntegrationsV1alphaOidcTokenOut"] = t.struct(
        {
            "serviceAccountEmail": t.string().optional(),
            "tokenExpireTime": t.string().optional(),
            "token": t.string().optional(),
            "audience": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOidcTokenOut"])
    types["EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoIn"] = t.struct(
        {
            "workflowId": t.string(),
            "createTime": t.string().optional(),
            "eventExecutionDetails": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsIn"]
            ).optional(),
            "clientId": t.string().optional(),
            "requestId": t.string().optional(),
            "errorCode": t.proxy(renames["CrmlogErrorCodeIn"]).optional(),
            "lastModifiedTime": t.string().optional(),
            "executionTraceInfo": t.proxy(
                renames["EnterpriseCrmEventbusProtoExecutionTraceInfoIn"]
            ).optional(),
            "workflowName": t.string().optional(),
            "tenant": t.string().optional(),
            "triggerId": t.string().optional(),
            "postMethod": t.string().optional(),
            "workflowRetryBackoffIntervalSeconds": t.string().optional(),
            "requestParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
            ).optional(),
            "product": t.string().optional(),
            "responseParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
            ).optional(),
            "errors": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoErrorDetailIn"])
            ).optional(),
            "eventExecutionInfoId": t.string().optional(),
            "snapshotNumber": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoIn"])
    types["EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoOut"] = t.struct(
        {
            "workflowId": t.string(),
            "createTime": t.string().optional(),
            "eventExecutionDetails": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsOut"]
            ).optional(),
            "clientId": t.string().optional(),
            "requestId": t.string().optional(),
            "errorCode": t.proxy(renames["CrmlogErrorCodeOut"]).optional(),
            "lastModifiedTime": t.string().optional(),
            "executionTraceInfo": t.proxy(
                renames["EnterpriseCrmEventbusProtoExecutionTraceInfoOut"]
            ).optional(),
            "workflowName": t.string().optional(),
            "tenant": t.string().optional(),
            "triggerId": t.string().optional(),
            "postMethod": t.string().optional(),
            "workflowRetryBackoffIntervalSeconds": t.string().optional(),
            "requestParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "product": t.string().optional(),
            "responseParams": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "errors": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoErrorDetailOut"])
            ).optional(),
            "eventExecutionInfoId": t.string().optional(),
            "snapshotNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoOut"])
    types["GoogleCloudIntegrationsV1alphaNextTaskIn"] = t.struct(
        {
            "taskConfigId": t.string().optional(),
            "taskId": t.string().optional(),
            "description": t.string().optional(),
            "condition": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaNextTaskIn"])
    types["GoogleCloudIntegrationsV1alphaNextTaskOut"] = t.struct(
        {
            "taskConfigId": t.string().optional(),
            "taskId": t.string().optional(),
            "description": t.string().optional(),
            "condition": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaNextTaskOut"])
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
    types["EnterpriseCrmEventbusProtoEventExecutionDetailsIn"] = t.struct(
        {
            "eventAttemptStats": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsIn"
                    ]
                )
            ),
            "eventExecutionSnapshot": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoEventExecutionSnapshotIn"])
            ),
            "networkAddress": t.string().optional(),
            "eventExecutionState": t.string(),
            "eventRetriesFromBeginningCount": t.integer().optional(),
            "nextExecutionTime": t.string().optional(),
            "logFilePath": t.string().optional(),
            "ryeLockUnheldCount": t.integer().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoEventExecutionDetailsIn"])
    types["EnterpriseCrmEventbusProtoEventExecutionDetailsOut"] = t.struct(
        {
            "eventAttemptStats": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsOut"
                    ]
                )
            ),
            "eventExecutionSnapshot": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoEventExecutionSnapshotOut"])
            ),
            "networkAddress": t.string().optional(),
            "eventExecutionState": t.string(),
            "eventRetriesFromBeginningCount": t.integer().optional(),
            "nextExecutionTime": t.string().optional(),
            "logFilePath": t.string().optional(),
            "ryeLockUnheldCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoEventExecutionDetailsOut"])
    types["EnterpriseCrmEventbusProtoDoubleArrayIn"] = t.struct(
        {"values": t.array(t.number())}
    ).named(renames["EnterpriseCrmEventbusProtoDoubleArrayIn"])
    types["EnterpriseCrmEventbusProtoDoubleArrayOut"] = t.struct(
        {
            "values": t.array(t.number()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoDoubleArrayOut"])
    types["EnterpriseCrmEventbusStatsIn"] = t.struct(
        {
            "qps": t.number().optional(),
            "errorRate": t.number().optional(),
            "durationInSeconds": t.number().optional(),
            "dimensions": t.proxy(
                renames["EnterpriseCrmEventbusStatsDimensionsIn"]
            ).optional(),
            "warningRate": t.number().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusStatsIn"])
    types["EnterpriseCrmEventbusStatsOut"] = t.struct(
        {
            "qps": t.number().optional(),
            "errorRate": t.number().optional(),
            "durationInSeconds": t.number().optional(),
            "dimensions": t.proxy(
                renames["EnterpriseCrmEventbusStatsDimensionsOut"]
            ).optional(),
            "warningRate": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusStatsOut"])
    types["EnterpriseCrmEventbusProtoSuspensionAuthPermissionsIn"] = t.struct(
        {
            "googleGroup": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityIn"
                ]
            ),
            "gaiaIdentity": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityIn"
                ]
            ).optional(),
            "loasRole": t.string(),
            "mdbGroup": t.string(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionAuthPermissionsIn"])
    types["EnterpriseCrmEventbusProtoSuspensionAuthPermissionsOut"] = t.struct(
        {
            "googleGroup": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityOut"
                ]
            ),
            "gaiaIdentity": t.proxy(
                renames[
                    "EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentityOut"
                ]
            ).optional(),
            "loasRole": t.string(),
            "mdbGroup": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionAuthPermissionsOut"])
    types["GoogleCloudIntegrationsV1alphaGenerateTokenResponseIn"] = t.struct(
        {"message": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaGenerateTokenResponseIn"])
    types["GoogleCloudIntegrationsV1alphaGenerateTokenResponseOut"] = t.struct(
        {
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaGenerateTokenResponseOut"])
    types["GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigIn"] = t.struct(
        {
            "expiration": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationIn"]
            ).optional(),
            "customMessage": t.string().optional(),
            "emailAddresses": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigIn"])
    types["GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigOut"] = t.struct(
        {
            "expiration": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalExpirationOut"]
            ).optional(),
            "customMessage": t.string().optional(),
            "emailAddresses": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSuspensionApprovalConfigOut"])
    types["GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsIn"] = t.struct(
        {
            "clientId": t.string().optional(),
            "requestType": t.string().optional(),
            "scope": t.string().optional(),
            "accessToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAccessTokenIn"]
            ).optional(),
            "clientSecret": t.string().optional(),
            "password": t.string().optional(),
            "username": t.string().optional(),
            "tokenEndpoint": t.string().optional(),
            "tokenParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsIn"])
    types["GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsOut"] = t.struct(
        {
            "clientId": t.string().optional(),
            "requestType": t.string().optional(),
            "scope": t.string().optional(),
            "accessToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAccessTokenOut"]
            ).optional(),
            "clientSecret": t.string().optional(),
            "password": t.string().optional(),
            "username": t.string().optional(),
            "tokenEndpoint": t.string().optional(),
            "tokenParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentialsOut"])
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
    types["EnterpriseCrmEventbusProtoProtoArrayFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoProtoArrayFunctionIn"])
    types["EnterpriseCrmEventbusProtoProtoArrayFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoProtoArrayFunctionOut"])
    types["EnterpriseCrmEventbusProtoCloudSchedulerConfigIn"] = t.struct(
        {
            "location": t.string(),
            "serviceAccountEmail": t.string(),
            "errorMessage": t.string().optional(),
            "cronTab": t.string(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoCloudSchedulerConfigIn"])
    types["EnterpriseCrmEventbusProtoCloudSchedulerConfigOut"] = t.struct(
        {
            "location": t.string(),
            "serviceAccountEmail": t.string(),
            "errorMessage": t.string().optional(),
            "cronTab": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoCloudSchedulerConfigOut"])
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
    types["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsIn"] = t.struct(
        {
            "subject": t.string().optional(),
            "audience": t.string().optional(),
            "issuer": t.string().optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsIn"])
    types["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsOut"] = t.struct(
        {
            "subject": t.string().optional(),
            "audience": t.string().optional(),
            "issuer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaimsOut"])
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
    types["GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionIn"] = t.struct(
        {
            "databasePersistencePolicy": t.string().optional(),
            "description": t.string().optional(),
            "templateParameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersIn"]
            ).optional(),
            "triggerConfigs": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn"])
            ).optional(),
            "parentIntegrationVersionId": t.string().optional(),
            "lastModifierEmail": t.string().optional(),
            "status": t.string().optional(),
            "userLabel": t.string().optional(),
            "teardown": t.proxy(
                renames["EnterpriseCrmEventbusProtoTeardownIn"]
            ).optional(),
            "errorCatcherConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigIn"])
            ).optional(),
            "taskConfigs": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionIn"])
    types["GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionOut"] = t.struct(
        {
            "snapshotNumber": t.string().optional(),
            "databasePersistencePolicy": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "templateParameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParametersOut"]
            ).optional(),
            "triggerConfigs": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigOut"])
            ).optional(),
            "parentIntegrationVersionId": t.string().optional(),
            "lastModifierEmail": t.string().optional(),
            "createTime": t.string().optional(),
            "status": t.string().optional(),
            "userLabel": t.string().optional(),
            "teardown": t.proxy(
                renames["EnterpriseCrmEventbusProtoTeardownOut"]
            ).optional(),
            "errorCatcherConfigs": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaErrorCatcherConfigOut"])
            ).optional(),
            "taskConfigs": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionOut"])
    types["GoogleCloudIntegrationsV1alphaCloudSchedulerConfigIn"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "serviceAccountEmail": t.string(),
            "location": t.string(),
            "cronTab": t.string(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCloudSchedulerConfigIn"])
    types["GoogleCloudIntegrationsV1alphaCloudSchedulerConfigOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "serviceAccountEmail": t.string(),
            "location": t.string(),
            "cronTab": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCloudSchedulerConfigOut"])
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
    types["EnterpriseCrmEventbusProtoTeardownTaskConfigIn"] = t.struct(
        {
            "properties": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventBusPropertiesIn"]
            ),
            "name": t.string(),
            "teardownTaskImplementationClassName": t.string(),
            "creatorEmail": t.string().optional(),
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
            "properties": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventBusPropertiesOut"]
            ),
            "name": t.string(),
            "teardownTaskImplementationClassName": t.string(),
            "creatorEmail": t.string().optional(),
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersOut"]
            ).optional(),
            "nextTeardownTask": t.proxy(
                renames["EnterpriseCrmEventbusProtoNextTeardownTaskOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTeardownTaskConfigOut"])
    types["GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseIn"] = t.struct(
        {"executionInfoIds": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseIn"])
    types["GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseOut"] = t.struct(
        {
            "executionInfoIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseOut"])
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
    types["EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsIn"] = t.struct(
        {
            "logFilePath": t.string().optional(),
            "eventExecutionSnapshot": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotIn"
                    ]
                )
            ).optional(),
            "networkAddress": t.string().optional(),
            "eventExecutionState": t.string().optional(),
            "eventAttemptStats": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsIn"
                    ]
                )
            ),
            "ryeLockUnheldCount": t.integer().optional(),
            "eventRetriesFromBeginningCount": t.integer().optional(),
            "nextExecutionTime": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsIn"])
    types["EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsOut"] = t.struct(
        {
            "logFilePath": t.string().optional(),
            "eventExecutionSnapshot": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshotOut"
                    ]
                )
            ).optional(),
            "networkAddress": t.string().optional(),
            "eventExecutionState": t.string().optional(),
            "eventAttemptStats": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStatsOut"
                    ]
                )
            ),
            "ryeLockUnheldCount": t.integer().optional(),
            "eventRetriesFromBeginningCount": t.integer().optional(),
            "nextExecutionTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionDetailsOut"])
    types["EnterpriseCrmEventbusProtoBaseValueIn"] = t.struct(
        {
            "literalValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeIn"]
            ).optional(),
            "baseFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoFunctionIn"]
            ).optional(),
            "referenceValue": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBaseValueIn"])
    types["EnterpriseCrmEventbusProtoBaseValueOut"] = t.struct(
        {
            "literalValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "baseFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoFunctionOut"]
            ).optional(),
            "referenceValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBaseValueOut"])
    types["GoogleCloudConnectorsV1DestinationConfigIn"] = t.struct(
        {
            "destinations": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1DestinationIn"])
            ).optional(),
            "key": t.string().optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1DestinationConfigIn"])
    types["GoogleCloudConnectorsV1DestinationConfigOut"] = t.struct(
        {
            "destinations": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1DestinationOut"])
            ).optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1DestinationConfigOut"])
    types["GoogleCloudConnectorsV1LockConfigIn"] = t.struct(
        {"locked": t.boolean().optional(), "reason": t.string().optional()}
    ).named(renames["GoogleCloudConnectorsV1LockConfigIn"])
    types["GoogleCloudConnectorsV1LockConfigOut"] = t.struct(
        {
            "locked": t.boolean().optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1LockConfigOut"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn"] = t.struct(
        {
            "doubleValue": t.number(),
            "protoArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayIn"]
            ),
            "intValue": t.string(),
            "serializedObjectValue": t.proxy(
                renames[
                    "EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterIn"
                ]
            ),
            "doubleArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayIn"]
            ),
            "protoValue": t.struct({"_": t.string().optional()}),
            "intArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoIntParameterArrayIn"]
            ),
            "booleanArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayIn"]
            ),
            "jsonValue": t.string(),
            "stringArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoStringParameterArrayIn"]
            ),
            "booleanValue": t.boolean(),
            "stringValue": t.string(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut"] = t.struct(
        {
            "doubleValue": t.number(),
            "protoArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayOut"]
            ),
            "intValue": t.string(),
            "serializedObjectValue": t.proxy(
                renames[
                    "EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterOut"
                ]
            ),
            "doubleArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoDoubleParameterArrayOut"]
            ),
            "protoValue": t.struct({"_": t.string().optional()}),
            "intArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoIntParameterArrayOut"]
            ),
            "booleanArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayOut"]
            ),
            "jsonValue": t.string(),
            "stringArray": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoStringParameterArrayOut"]
            ),
            "booleanValue": t.boolean(),
            "stringValue": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut"])
    types["EnterpriseCrmEventbusProtoFunctionTypeIn"] = t.struct(
        {
            "doubleFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoDoubleFunctionIn"]
            ),
            "booleanArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoBooleanArrayFunctionIn"]
            ),
            "stringFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoStringFunctionIn"]
            ),
            "intArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoIntArrayFunctionIn"]
            ),
            "protoFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoProtoFunctionIn"]
            ),
            "intFunction": t.proxy(renames["EnterpriseCrmEventbusProtoIntFunctionIn"]),
            "doubleArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoDoubleArrayFunctionIn"]
            ),
            "protoArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoProtoArrayFunctionIn"]
            ),
            "baseFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseFunctionIn"]
            ).optional(),
            "stringArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoStringArrayFunctionIn"]
            ),
            "jsonFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoJsonFunctionIn"]
            ).optional(),
            "booleanFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoBooleanFunctionIn"]
            ),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFunctionTypeIn"])
    types["EnterpriseCrmEventbusProtoFunctionTypeOut"] = t.struct(
        {
            "doubleFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoDoubleFunctionOut"]
            ),
            "booleanArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoBooleanArrayFunctionOut"]
            ),
            "stringFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoStringFunctionOut"]
            ),
            "intArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoIntArrayFunctionOut"]
            ),
            "protoFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoProtoFunctionOut"]
            ),
            "intFunction": t.proxy(renames["EnterpriseCrmEventbusProtoIntFunctionOut"]),
            "doubleArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoDoubleArrayFunctionOut"]
            ),
            "protoArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoProtoArrayFunctionOut"]
            ),
            "baseFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseFunctionOut"]
            ).optional(),
            "stringArrayFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoStringArrayFunctionOut"]
            ),
            "jsonFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoJsonFunctionOut"]
            ).optional(),
            "booleanFunction": t.proxy(
                renames["EnterpriseCrmEventbusProtoBooleanFunctionOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFunctionTypeOut"])
    types["EnterpriseCrmEventbusStatsDimensionsIn"] = t.struct(
        {
            "clientId": t.string(),
            "enumFilterType": t.string().optional(),
            "workflowName": t.string(),
            "taskNumber": t.string(),
            "errorEnumString": t.string(),
            "workflowId": t.string(),
            "retryAttempt": t.string(),
            "triggerId": t.string().optional(),
            "warningEnumString": t.string(),
            "taskName": t.string(),
        }
    ).named(renames["EnterpriseCrmEventbusStatsDimensionsIn"])
    types["EnterpriseCrmEventbusStatsDimensionsOut"] = t.struct(
        {
            "clientId": t.string(),
            "enumFilterType": t.string().optional(),
            "workflowName": t.string(),
            "taskNumber": t.string(),
            "errorEnumString": t.string(),
            "workflowId": t.string(),
            "retryAttempt": t.string(),
            "triggerId": t.string().optional(),
            "warningEnumString": t.string(),
            "taskName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusStatsDimensionsOut"])
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
    types["EnterpriseCrmEventbusProtoNextTaskIn"] = t.struct(
        {
            "condition": t.string().optional(),
            "combinedConditions": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoCombinedConditionIn"])
            ).optional(),
            "taskConfigId": t.string().optional(),
            "taskNumber": t.string().optional(),
            "label": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoNextTaskIn"])
    types["EnterpriseCrmEventbusProtoNextTaskOut"] = t.struct(
        {
            "condition": t.string().optional(),
            "combinedConditions": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoCombinedConditionOut"])
            ).optional(),
            "taskConfigId": t.string().optional(),
            "taskNumber": t.string().optional(),
            "label": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoNextTaskOut"])
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
    types["GoogleCloudIntegrationsV1alphaCredentialIn"] = t.struct(
        {
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
            "jwt": t.proxy(renames["GoogleCloudIntegrationsV1alphaJwtIn"]).optional(),
            "oidcToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaOidcTokenIn"]
            ).optional(),
            "usernameAndPassword": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaUsernameAndPasswordIn"]
            ).optional(),
            "serviceAccountCredentials": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaServiceAccountCredentialsIn"]
            ).optional(),
            "oauth2ClientCredentials": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsIn"]
            ).optional(),
            "credentialType": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCredentialIn"])
    types["GoogleCloudIntegrationsV1alphaCredentialOut"] = t.struct(
        {
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
            "jwt": t.proxy(renames["GoogleCloudIntegrationsV1alphaJwtOut"]).optional(),
            "oidcToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaOidcTokenOut"]
            ).optional(),
            "usernameAndPassword": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaUsernameAndPasswordOut"]
            ).optional(),
            "serviceAccountCredentials": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaServiceAccountCredentialsOut"]
            ).optional(),
            "oauth2ClientCredentials": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsOut"]
            ).optional(),
            "credentialType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCredentialOut"])
    types["EnterpriseCrmEventbusProtoConditionResultIn"] = t.struct(
        {
            "nextTaskNumber": t.string().optional(),
            "result": t.boolean().optional(),
            "currentTaskNumber": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoConditionResultIn"])
    types["EnterpriseCrmEventbusProtoConditionResultOut"] = t.struct(
        {
            "nextTaskNumber": t.string().optional(),
            "result": t.boolean().optional(),
            "currentTaskNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoConditionResultOut"])
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
        "GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequestIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequestIn"]
    )
    types[
        "GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequestOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames["GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequestOut"]
    )
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
    types["EnterpriseCrmLoggingGwsSanitizeOptionsIn"] = t.struct(
        {
            "logType": t.array(t.string()).optional(),
            "isAlreadySanitized": t.boolean().optional(),
            "privacy": t.string(),
            "sanitizeType": t.string(),
        }
    ).named(renames["EnterpriseCrmLoggingGwsSanitizeOptionsIn"])
    types["EnterpriseCrmLoggingGwsSanitizeOptionsOut"] = t.struct(
        {
            "logType": t.array(t.string()).optional(),
            "isAlreadySanitized": t.boolean().optional(),
            "privacy": t.string(),
            "sanitizeType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmLoggingGwsSanitizeOptionsOut"])
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
            "taskExecutionState": t.string().optional(),
            "taskAttemptStats": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaAttemptStatsIn"])
            ).optional(),
            "taskNumber": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaTaskExecutionDetailsIn"])
    types["GoogleCloudIntegrationsV1alphaTaskExecutionDetailsOut"] = t.struct(
        {
            "taskExecutionState": t.string().optional(),
            "taskAttemptStats": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaAttemptStatsOut"])
            ).optional(),
            "taskNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaTaskExecutionDetailsOut"])
    types["EnterpriseCrmEventbusProtoLoopMetadataIn"] = t.struct(
        {
            "currentIterationDetail": t.string().optional(),
            "failureLocation": t.string().optional(),
            "currentIterationCount": t.string().optional(),
            "errorMsg": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoLoopMetadataIn"])
    types["EnterpriseCrmEventbusProtoLoopMetadataOut"] = t.struct(
        {
            "currentIterationDetail": t.string().optional(),
            "failureLocation": t.string().optional(),
            "currentIterationCount": t.string().optional(),
            "errorMsg": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoLoopMetadataOut"])
    types["EnterpriseCrmEventbusProtoProtoParameterArrayIn"] = t.struct(
        {"protoValues": t.array(t.struct({"_": t.string().optional()}))}
    ).named(renames["EnterpriseCrmEventbusProtoProtoParameterArrayIn"])
    types["EnterpriseCrmEventbusProtoProtoParameterArrayOut"] = t.struct(
        {
            "protoValues": t.array(t.struct({"_": t.string().optional()})),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoProtoParameterArrayOut"])
    types["GoogleCloudIntegrationsV1alphaCertificateIn"] = t.struct(
        {
            "rawCertificate": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaClientCertificateIn"]
            ).optional(),
            "credentialId": t.string().optional(),
            "certificateStatus": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "requestorId": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCertificateIn"])
    types["GoogleCloudIntegrationsV1alphaCertificateOut"] = t.struct(
        {
            "rawCertificate": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaClientCertificateOut"]
            ).optional(),
            "name": t.string().optional(),
            "credentialId": t.string().optional(),
            "certificateStatus": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "validStartTime": t.string().optional(),
            "validEndTime": t.string().optional(),
            "requestorId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaCertificateOut"])
    types["EnterpriseCrmEventbusProtoLogSettingsIn"] = t.struct(
        {
            "seedScope": t.string(),
            "sanitizeOptions": t.proxy(
                renames["EnterpriseCrmLoggingGwsSanitizeOptionsIn"]
            ).optional(),
            "seedPeriod": t.string(),
            "logFieldName": t.string().optional(),
            "shorteningLimits": t.proxy(
                renames["EnterpriseCrmLoggingGwsFieldLimitsIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoLogSettingsIn"])
    types["EnterpriseCrmEventbusProtoLogSettingsOut"] = t.struct(
        {
            "seedScope": t.string(),
            "sanitizeOptions": t.proxy(
                renames["EnterpriseCrmLoggingGwsSanitizeOptionsOut"]
            ).optional(),
            "seedPeriod": t.string(),
            "logFieldName": t.string().optional(),
            "shorteningLimits": t.proxy(
                renames["EnterpriseCrmLoggingGwsFieldLimitsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoLogSettingsOut"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"] = t.struct(
        {
            "value": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn"]
            ).optional(),
            "key": t.string().optional(),
            "dataType": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"])
    types["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"] = t.struct(
        {
            "value": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "key": t.string().optional(),
            "dataType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"])
    types["EnterpriseCrmEventbusProtoBuganizerNotificationIn"] = t.struct(
        {
            "assigneeEmailAddress": t.string().optional(),
            "componentId": t.string().optional(),
            "title": t.string().optional(),
            "templateId": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBuganizerNotificationIn"])
    types["EnterpriseCrmEventbusProtoBuganizerNotificationOut"] = t.struct(
        {
            "assigneeEmailAddress": t.string().optional(),
            "componentId": t.string().optional(),
            "title": t.string().optional(),
            "templateId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBuganizerNotificationOut"])
    types["EnterpriseCrmEventbusProtoTaskExecutionDetailsIn"] = t.struct(
        {
            "taskNumber": t.string().optional(),
            "taskExecutionState": t.string(),
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
            "taskNumber": t.string().optional(),
            "taskExecutionState": t.string(),
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
    types["GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "integrationVersions": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionIn"])
            ).optional(),
            "noPermission": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseIn"])
    types[
        "GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "integrationVersions": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaIntegrationVersionOut"])
            ).optional(),
            "noPermission": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseOut"]
    )
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
    types["GoogleCloudConnectorsV1ConnectionIn"] = t.struct(
        {
            "description": t.string().optional(),
            "suspended": t.boolean().optional(),
            "lockConfig": t.proxy(
                renames["GoogleCloudConnectorsV1LockConfigIn"]
            ).optional(),
            "nodeConfig": t.proxy(
                renames["GoogleCloudConnectorsV1NodeConfigIn"]
            ).optional(),
            "destinationConfigs": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1DestinationConfigIn"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "logConfig": t.proxy(
                renames["GoogleCloudConnectorsV1LogConfigIn"]
            ).optional(),
            "sslConfig": t.proxy(
                renames["GoogleCloudConnectorsV1SslConfigIn"]
            ).optional(),
            "serviceAccount": t.string().optional(),
            "connectorVersion": t.string(),
            "authConfig": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigIn"]
            ).optional(),
            "configVariables": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConfigVariableIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1ConnectionIn"])
    types["GoogleCloudConnectorsV1ConnectionOut"] = t.struct(
        {
            "description": t.string().optional(),
            "suspended": t.boolean().optional(),
            "lockConfig": t.proxy(
                renames["GoogleCloudConnectorsV1LockConfigOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "nodeConfig": t.proxy(
                renames["GoogleCloudConnectorsV1NodeConfigOut"]
            ).optional(),
            "subscriptionType": t.string().optional(),
            "destinationConfigs": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1DestinationConfigOut"])
            ).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "serviceDirectory": t.string().optional(),
            "logConfig": t.proxy(
                renames["GoogleCloudConnectorsV1LogConfigOut"]
            ).optional(),
            "sslConfig": t.proxy(
                renames["GoogleCloudConnectorsV1SslConfigOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "envoyImageLocation": t.string().optional(),
            "connectorVersion": t.string(),
            "connectorVersionLaunchStage": t.string().optional(),
            "authConfig": t.proxy(
                renames["GoogleCloudConnectorsV1AuthConfigOut"]
            ).optional(),
            "status": t.proxy(
                renames["GoogleCloudConnectorsV1ConnectionStatusOut"]
            ).optional(),
            "imageLocation": t.string().optional(),
            "configVariables": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConfigVariableOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1ConnectionOut"])
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
    types["GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeIn"] = t.struct(
        {
            "tokenEndpoint": t.string().optional(),
            "scope": t.string().optional(),
            "authParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapIn"]
            ).optional(),
            "accessToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAccessTokenIn"]
            ).optional(),
            "applyReauthPolicy": t.boolean().optional(),
            "requestType": t.string().optional(),
            "clientId": t.string().optional(),
            "clientSecret": t.string().optional(),
            "tokenParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapIn"]
            ).optional(),
            "authCode": t.string().optional(),
            "authEndpoint": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeIn"])
    types["GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeOut"] = t.struct(
        {
            "tokenEndpoint": t.string().optional(),
            "scope": t.string().optional(),
            "authParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapOut"]
            ).optional(),
            "accessToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAccessTokenOut"]
            ).optional(),
            "applyReauthPolicy": t.boolean().optional(),
            "requestType": t.string().optional(),
            "clientId": t.string().optional(),
            "clientSecret": t.string().optional(),
            "tokenParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapOut"]
            ).optional(),
            "authCode": t.string().optional(),
            "authEndpoint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCodeOut"])
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
    types["GoogleCloudIntegrationsV1alphaExecutionDetailsIn"] = t.struct(
        {
            "state": t.string().optional(),
            "attemptStats": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaAttemptStatsIn"])
            ).optional(),
            "executionSnapshots": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaExecutionSnapshotIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecutionDetailsIn"])
    types["GoogleCloudIntegrationsV1alphaExecutionDetailsOut"] = t.struct(
        {
            "state": t.string().optional(),
            "attemptStats": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaAttemptStatsOut"])
            ).optional(),
            "executionSnapshots": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaExecutionSnapshotOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecutionDetailsOut"])
    types["EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayIn"] = t.struct(
        {"protoValues": t.array(t.struct({"_": t.string().optional()}))}
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayIn"])
    types["EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayOut"] = t.struct(
        {
            "protoValues": t.array(t.struct({"_": t.string().optional()})),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoProtoParameterArrayOut"])
    types["GoogleCloudConnectorsV1ConfigVariableIn"] = t.struct(
        {
            "secretValue": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
            "key": t.string().optional(),
            "stringValue": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "intValue": t.string().optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1ConfigVariableIn"])
    types["GoogleCloudConnectorsV1ConfigVariableOut"] = t.struct(
        {
            "secretValue": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "key": t.string().optional(),
            "stringValue": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "intValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1ConfigVariableOut"])
    types["GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsIn"] = t.struct(
        {
            "accessToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAccessTokenIn"]
            ).optional(),
            "tokenParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapIn"]
            ).optional(),
            "clientSecret": t.string().optional(),
            "scope": t.string().optional(),
            "requestType": t.string().optional(),
            "clientId": t.string().optional(),
            "tokenEndpoint": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsIn"])
    types["GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsOut"] = t.struct(
        {
            "accessToken": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaAccessTokenOut"]
            ).optional(),
            "tokenParams": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaParameterMapOut"]
            ).optional(),
            "clientSecret": t.string().optional(),
            "scope": t.string().optional(),
            "requestType": t.string().optional(),
            "clientId": t.string().optional(),
            "tokenEndpoint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaOAuth2ClientCredentialsOut"])
    types["GoogleCloudIntegrationsV1alphaTriggerConfigIn"] = t.struct(
        {
            "triggerType": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCoordinateIn"]
            ).optional(),
            "startTasks": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaNextTaskIn"])
            ).optional(),
            "errorCatcherId": t.string().optional(),
            "triggerId": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "cloudSchedulerConfig": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCloudSchedulerConfigIn"]
            ).optional(),
            "triggerNumber": t.string(),
            "alertConfig": t.array(
                t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigIn"]
                )
            ).optional(),
            "label": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaTriggerConfigIn"])
    types["GoogleCloudIntegrationsV1alphaTriggerConfigOut"] = t.struct(
        {
            "triggerType": t.string().optional(),
            "position": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCoordinateOut"]
            ).optional(),
            "startTasks": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaNextTaskOut"])
            ).optional(),
            "errorCatcherId": t.string().optional(),
            "triggerId": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "cloudSchedulerConfig": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCloudSchedulerConfigOut"]
            ).optional(),
            "triggerNumber": t.string(),
            "alertConfig": t.array(
                t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaIntegrationAlertConfigOut"]
                )
            ).optional(),
            "label": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaTriggerConfigOut"])
    types[
        "GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestIn"
    ] = t.struct(
        {
            "scheduledTime": t.string().optional(),
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersIn"]
            ).optional(),
            "resourceName": t.string().optional(),
            "workflowName": t.string().optional(),
            "triggerId": t.string().optional(),
            "requestId": t.string().optional(),
            "ignoreErrorIfNoActiveWorkflow": t.boolean().optional(),
            "clientId": t.string().optional(),
            "testMode": t.boolean().optional(),
            "priority": t.string().optional(),
        }
    ).named(
        renames["GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestIn"]
    )
    types[
        "GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestOut"
    ] = t.struct(
        {
            "scheduledTime": t.string().optional(),
            "parameters": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventParametersOut"]
            ).optional(),
            "resourceName": t.string().optional(),
            "workflowName": t.string().optional(),
            "triggerId": t.string().optional(),
            "requestId": t.string().optional(),
            "ignoreErrorIfNoActiveWorkflow": t.boolean().optional(),
            "clientId": t.string().optional(),
            "testMode": t.boolean().optional(),
            "priority": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequestOut"]
    )
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
    types["EnterpriseCrmEventbusProtoParameterValueTypeIn"] = t.struct(
        {
            "booleanArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoBooleanParameterArrayIn"]
            ),
            "serializedObjectValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoSerializedObjectParameterIn"]
            ),
            "stringValue": t.string(),
            "doubleValue": t.number(),
            "intValue": t.string(),
            "protoValue": t.struct({"_": t.string().optional()}),
            "stringArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoStringParameterArrayIn"]
            ),
            "doubleArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoDoubleParameterArrayIn"]
            ),
            "booleanValue": t.boolean(),
            "intArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoIntParameterArrayIn"]
            ),
            "protoArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoProtoParameterArrayIn"]
            ),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParameterValueTypeIn"])
    types["EnterpriseCrmEventbusProtoParameterValueTypeOut"] = t.struct(
        {
            "booleanArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoBooleanParameterArrayOut"]
            ),
            "serializedObjectValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoSerializedObjectParameterOut"]
            ),
            "stringValue": t.string(),
            "doubleValue": t.number(),
            "intValue": t.string(),
            "protoValue": t.struct({"_": t.string().optional()}),
            "stringArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoStringParameterArrayOut"]
            ),
            "doubleArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoDoubleParameterArrayOut"]
            ),
            "booleanValue": t.boolean(),
            "intArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoIntParameterArrayOut"]
            ),
            "protoArray": t.proxy(
                renames["EnterpriseCrmEventbusProtoProtoParameterArrayOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParameterValueTypeOut"])
    types["EnterpriseCrmEventbusProtoCoordinateIn"] = t.struct(
        {"x": t.integer(), "y": t.integer()}
    ).named(renames["EnterpriseCrmEventbusProtoCoordinateIn"])
    types["EnterpriseCrmEventbusProtoCoordinateOut"] = t.struct(
        {
            "x": t.integer(),
            "y": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoCoordinateOut"])
    types["EnterpriseCrmEventbusProtoBaseFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoBaseFunctionIn"])
    types["EnterpriseCrmEventbusProtoBaseFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBaseFunctionOut"])
    types["EnterpriseCrmEventbusProtoParamSpecEntryConfigIn"] = t.struct(
        {
            "subSectionLabel": t.string().optional(),
            "label": t.string().optional(),
            "hideDefaultValue": t.boolean().optional(),
            "descriptivePhrase": t.string().optional(),
            "parameterNameOption": t.string(),
            "helpText": t.string().optional(),
            "isHidden": t.boolean().optional(),
            "inputDisplayOption": t.string(),
            "uiPlaceholderText": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParamSpecEntryConfigIn"])
    types["EnterpriseCrmEventbusProtoParamSpecEntryConfigOut"] = t.struct(
        {
            "subSectionLabel": t.string().optional(),
            "label": t.string().optional(),
            "hideDefaultValue": t.boolean().optional(),
            "descriptivePhrase": t.string().optional(),
            "parameterNameOption": t.string(),
            "helpText": t.string().optional(),
            "isHidden": t.boolean().optional(),
            "inputDisplayOption": t.string(),
            "uiPlaceholderText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoParamSpecEntryConfigOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["EnterpriseCrmEventbusProtoFieldIn"] = t.struct(
        {
            "fieldType": t.string().optional(),
            "protoDefPath": t.string().optional(),
            "transformExpression": t.proxy(
                renames["EnterpriseCrmEventbusProtoTransformExpressionIn"]
            ).optional(),
            "referenceKey": t.string().optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeIn"]
            ).optional(),
            "cardinality": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFieldIn"])
    types["EnterpriseCrmEventbusProtoFieldOut"] = t.struct(
        {
            "fieldType": t.string().optional(),
            "protoDefPath": t.string().optional(),
            "transformExpression": t.proxy(
                renames["EnterpriseCrmEventbusProtoTransformExpressionOut"]
            ).optional(),
            "referenceKey": t.string().optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "cardinality": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoFieldOut"])
    types["EnterpriseCrmEventbusProtoIntArrayFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoIntArrayFunctionIn"])
    types["EnterpriseCrmEventbusProtoIntArrayFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoIntArrayFunctionOut"])
    types["EnterpriseCrmEventbusProtoIntParameterArrayIn"] = t.struct(
        {"intValues": t.array(t.string())}
    ).named(renames["EnterpriseCrmEventbusProtoIntParameterArrayIn"])
    types["EnterpriseCrmEventbusProtoIntParameterArrayOut"] = t.struct(
        {
            "intValues": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoIntParameterArrayOut"])
    types[
        "GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataIn"
    ] = t.struct(
        {
            "executionAttempt": t.integer().optional(),
            "taskLabel": t.string().optional(),
            "task": t.string().optional(),
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
            "executionAttempt": t.integer().optional(),
            "taskLabel": t.string().optional(),
            "task": t.string().optional(),
            "taskNumber": t.string().optional(),
            "taskAttempt": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataOut"
        ]
    )
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
    types["GoogleCloudIntegrationsV1alphaIntegrationIn"] = t.struct(
        {
            "name": t.string(),
            "description": t.string().optional(),
            "active": t.boolean(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationIn"])
    types["GoogleCloudIntegrationsV1alphaIntegrationOut"] = t.struct(
        {
            "name": t.string(),
            "description": t.string().optional(),
            "active": t.boolean(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaIntegrationOut"])
    types[
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexIn"
    ] = t.struct(
        {"regex": t.string().optional(), "exclusive": t.boolean().optional()}
    ).named(
        renames["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexIn"]
    )
    types[
        "EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexOut"
    ] = t.struct(
        {
            "regex": t.string().optional(),
            "exclusive": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegexOut"]
    )
    types["EnterpriseCrmEventbusProtoStringFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoStringFunctionIn"])
    types["EnterpriseCrmEventbusProtoStringFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoStringFunctionOut"])
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
    types["GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestIn"])
    types["GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaTakeoverEditLockRequestOut"])
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
    types["GoogleCloudConnectorsV1SecretIn"] = t.struct(
        {"secretVersion": t.string().optional()}
    ).named(renames["GoogleCloudConnectorsV1SecretIn"])
    types["GoogleCloudConnectorsV1SecretOut"] = t.struct(
        {
            "secretVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1SecretOut"])
    types["GoogleCloudIntegrationsV1alphaRuntimeActionSchemaIn"] = t.struct(
        {
            "inputSchema": t.string().optional(),
            "action": t.string().optional(),
            "outputSchema": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaRuntimeActionSchemaIn"])
    types["GoogleCloudIntegrationsV1alphaRuntimeActionSchemaOut"] = t.struct(
        {
            "inputSchema": t.string().optional(),
            "action": t.string().optional(),
            "outputSchema": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaRuntimeActionSchemaOut"])
    types["GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseIn"] = t.struct(
        {
            "outputParameters": t.struct({"_": t.string().optional()}).optional(),
            "executionId": t.string().optional(),
            "executionFailed": t.boolean().optional(),
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
            "outputParameters": t.struct({"_": t.string().optional()}).optional(),
            "executionId": t.string().optional(),
            "executionFailed": t.boolean().optional(),
            "eventParameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "parameterEntries": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseOut"])
    types["EnterpriseCrmEventbusProtoDoubleParameterArrayIn"] = t.struct(
        {"doubleValues": t.array(t.number())}
    ).named(renames["EnterpriseCrmEventbusProtoDoubleParameterArrayIn"])
    types["EnterpriseCrmEventbusProtoDoubleParameterArrayOut"] = t.struct(
        {
            "doubleValues": t.array(t.number()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoDoubleParameterArrayOut"])
    types["EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterIn"] = t.struct(
        {"objectValue": t.string()}
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterIn"])
    types["EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterOut"] = t.struct(
        {
            "objectValue": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameterOut"])
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
    types["EnterpriseCrmFrontendsEventbusProtoIntParameterArrayIn"] = t.struct(
        {"intValues": t.array(t.string())}
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoIntParameterArrayIn"])
    types["EnterpriseCrmFrontendsEventbusProtoIntParameterArrayOut"] = t.struct(
        {
            "intValues": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoIntParameterArrayOut"])
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
    types["GoogleCloudIntegrationsV1alphaResolveSuspensionResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaResolveSuspensionResponseIn"])
    types["GoogleCloudIntegrationsV1alphaResolveSuspensionResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaResolveSuspensionResponseOut"])
    types["EnterpriseCrmEventbusProtoTaskAlertConfigIn"] = t.struct(
        {
            "alertName": t.string().optional(),
            "aggregationPeriod": t.string().optional(),
            "errorEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn"]
            ),
            "thresholdType": t.string().optional(),
            "playbookUrl": t.string().optional(),
            "numAggregationPeriods": t.integer().optional(),
            "metricType": t.string(),
            "onlyFinalAttempt": t.boolean().optional(),
            "alertDisabled": t.boolean().optional(),
            "thresholdValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueIn"]
            ).optional(),
            "clientId": t.string().optional(),
            "warningEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn"]
            ),
            "durationThresholdMs": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskAlertConfigIn"])
    types["EnterpriseCrmEventbusProtoTaskAlertConfigOut"] = t.struct(
        {
            "alertName": t.string().optional(),
            "aggregationPeriod": t.string().optional(),
            "errorEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut"]
            ),
            "thresholdType": t.string().optional(),
            "playbookUrl": t.string().optional(),
            "numAggregationPeriods": t.integer().optional(),
            "metricType": t.string(),
            "onlyFinalAttempt": t.boolean().optional(),
            "alertDisabled": t.boolean().optional(),
            "thresholdValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueOut"]
            ).optional(),
            "clientId": t.string().optional(),
            "warningEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut"]
            ),
            "durationThresholdMs": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoTaskAlertConfigOut"])
    types["EnterpriseCrmEventbusProtoBooleanParameterArrayIn"] = t.struct(
        {"booleanValues": t.array(t.boolean())}
    ).named(renames["EnterpriseCrmEventbusProtoBooleanParameterArrayIn"])
    types["EnterpriseCrmEventbusProtoBooleanParameterArrayOut"] = t.struct(
        {
            "booleanValues": t.array(t.boolean()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBooleanParameterArrayOut"])
    types["GoogleCloudConnectorsV1SslConfigIn"] = t.struct(
        {
            "clientCertificate": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
            "clientPrivateKeyPass": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
            "useSsl": t.boolean().optional(),
            "clientCertType": t.string().optional(),
            "serverCertType": t.string().optional(),
            "trustModel": t.string().optional(),
            "additionalVariables": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConfigVariableIn"])
            ).optional(),
            "privateServerCertificate": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
            "clientPrivateKey": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1SslConfigIn"])
    types["GoogleCloudConnectorsV1SslConfigOut"] = t.struct(
        {
            "clientCertificate": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "clientPrivateKeyPass": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "useSsl": t.boolean().optional(),
            "clientCertType": t.string().optional(),
            "serverCertType": t.string().optional(),
            "trustModel": t.string().optional(),
            "additionalVariables": t.array(
                t.proxy(renames["GoogleCloudConnectorsV1ConfigVariableOut"])
            ).optional(),
            "privateServerCertificate": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "clientPrivateKey": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1SslConfigOut"])
    types["GoogleCloudConnectorsV1LogConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["GoogleCloudConnectorsV1LogConfigIn"])
    types["GoogleCloudConnectorsV1LogConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1LogConfigOut"])
    types["EnterpriseCrmEventbusProtoStringArrayIn"] = t.struct(
        {"values": t.array(t.string())}
    ).named(renames["EnterpriseCrmEventbusProtoStringArrayIn"])
    types["EnterpriseCrmEventbusProtoStringArrayOut"] = t.struct(
        {
            "values": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoStringArrayOut"])
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
    types["EnterpriseCrmEventbusProtoSuspensionResolutionInfoIn"] = t.struct(
        {
            "cloudKmsConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoCloudKmsConfigIn"]
            ).optional(),
            "taskNumber": t.string(),
            "audit": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditIn"]
            ),
            "createdTimestamp": t.string().optional(),
            "eventExecutionInfoId": t.string(),
            "suspensionConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionConfigIn"]
            ),
            "suspensionId": t.string().optional(),
            "encryptedSuspensionResolutionInfo": t.string().optional(),
            "lastModifiedTimestamp": t.string().optional(),
            "wrappedDek": t.string().optional(),
            "clientId": t.string().optional(),
            "product": t.string().optional(),
            "workflowName": t.string(),
            "externalTraffic": t.proxy(
                renames["EnterpriseCrmEventbusProtoExternalTrafficIn"]
            ).optional(),
            "status": t.string(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionResolutionInfoIn"])
    types["EnterpriseCrmEventbusProtoSuspensionResolutionInfoOut"] = t.struct(
        {
            "cloudKmsConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoCloudKmsConfigOut"]
            ).optional(),
            "taskNumber": t.string(),
            "audit": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditOut"]
            ),
            "createdTimestamp": t.string().optional(),
            "eventExecutionInfoId": t.string(),
            "suspensionConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuspensionConfigOut"]
            ),
            "suspensionId": t.string().optional(),
            "encryptedSuspensionResolutionInfo": t.string().optional(),
            "lastModifiedTimestamp": t.string().optional(),
            "wrappedDek": t.string().optional(),
            "clientId": t.string().optional(),
            "product": t.string().optional(),
            "workflowName": t.string(),
            "externalTraffic": t.proxy(
                renames["EnterpriseCrmEventbusProtoExternalTrafficOut"]
            ).optional(),
            "status": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionResolutionInfoOut"])
    types["GoogleCloudIntegrationsV1alphaListExecutionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "executions": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaExecutionIn"])
            ).optional(),
            "executionInfos": t.array(
                t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoIn"]
                )
            ),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListExecutionsResponseIn"])
    types["GoogleCloudIntegrationsV1alphaListExecutionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "executions": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaExecutionOut"])
            ).optional(),
            "executionInfos": t.array(
                t.proxy(
                    renames["EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoOut"]
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaListExecutionsResponseOut"])
    types["EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditIn"] = t.struct(
        {"resolvedBy": t.string(), "timestamp": t.string(), "resolvedByCpi": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditIn"])
    types["EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditOut"] = t.struct(
        {
            "resolvedBy": t.string(),
            "timestamp": t.string(),
            "resolvedByCpi": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuspensionResolutionInfoAuditOut"])
    types["GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestIn"] = t.struct(
        {
            "parameterEntries": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"])
            ).optional(),
            "triggerId": t.string(),
            "parameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersIn"]
            ).optional(),
            "inputParameters": t.struct({"_": t.string().optional()}).optional(),
            "doNotPropagateError": t.boolean().optional(),
            "executionId": t.string().optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestIn"])
    types["GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestOut"] = t.struct(
        {
            "parameterEntries": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"])
            ).optional(),
            "triggerId": t.string(),
            "parameters": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoEventParametersOut"]
            ).optional(),
            "inputParameters": t.struct({"_": t.string().optional()}).optional(),
            "doNotPropagateError": t.boolean().optional(),
            "executionId": t.string().optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequestOut"])
    types["GoogleCloudIntegrationsV1alphaExecutionIn"] = t.struct(
        {
            "requestParameters": t.struct({"_": t.string().optional()}).optional(),
            "directSubExecutions": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaExecutionIn"])
            ).optional(),
            "executionMethod": t.string().optional(),
            "requestParams": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"])
            ).optional(),
            "name": t.string().optional(),
            "responseParameters": t.struct({"_": t.string().optional()}).optional(),
            "triggerId": t.string().optional(),
            "responseParams": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryIn"])
            ).optional(),
            "eventExecutionDetails": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventExecutionDetailsIn"]
            ).optional(),
            "executionDetails": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaExecutionDetailsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecutionIn"])
    types["GoogleCloudIntegrationsV1alphaExecutionOut"] = t.struct(
        {
            "requestParameters": t.struct({"_": t.string().optional()}).optional(),
            "directSubExecutions": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaExecutionOut"])
            ).optional(),
            "updateTime": t.string().optional(),
            "executionMethod": t.string().optional(),
            "requestParams": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"])
            ).optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "responseParameters": t.struct({"_": t.string().optional()}).optional(),
            "triggerId": t.string().optional(),
            "responseParams": t.array(
                t.proxy(renames["EnterpriseCrmFrontendsEventbusProtoParameterEntryOut"])
            ).optional(),
            "eventExecutionDetails": t.proxy(
                renames["EnterpriseCrmEventbusProtoEventExecutionDetailsOut"]
            ).optional(),
            "executionDetails": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaExecutionDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecutionOut"])
    types["EnterpriseCrmEventbusProtoSerializedObjectParameterIn"] = t.struct(
        {"objectValue": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoSerializedObjectParameterIn"])
    types["EnterpriseCrmEventbusProtoSerializedObjectParameterOut"] = t.struct(
        {
            "objectValue": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSerializedObjectParameterOut"])
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
    types["GoogleCloudIntegrationsV1alphaLiftSuspensionResponseIn"] = t.struct(
        {"eventExecutionInfoId": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaLiftSuspensionResponseIn"])
    types["GoogleCloudIntegrationsV1alphaLiftSuspensionResponseOut"] = t.struct(
        {
            "eventExecutionInfoId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaLiftSuspensionResponseOut"])
    types["GoogleCloudIntegrationsV1alphaJwtIn"] = t.struct(
        {
            "secret": t.string().optional(),
            "jwtPayload": t.string().optional(),
            "jwtHeader": t.string().optional(),
            "jwt": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaJwtIn"])
    types["GoogleCloudIntegrationsV1alphaJwtOut"] = t.struct(
        {
            "secret": t.string().optional(),
            "jwtPayload": t.string().optional(),
            "jwtHeader": t.string().optional(),
            "jwt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaJwtOut"])
    types["EnterpriseCrmEventbusProtoIntArrayIn"] = t.struct(
        {"values": t.array(t.string())}
    ).named(renames["EnterpriseCrmEventbusProtoIntArrayIn"])
    types["EnterpriseCrmEventbusProtoIntArrayOut"] = t.struct(
        {
            "values": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoIntArrayOut"])
    types["GoogleCloudConnectorsV1AuthConfigSshPublicKeyIn"] = t.struct(
        {
            "sshClientCertPass": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
            "sshClientCert": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
            "username": t.string().optional(),
            "certType": t.string().optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigSshPublicKeyIn"])
    types["GoogleCloudConnectorsV1AuthConfigSshPublicKeyOut"] = t.struct(
        {
            "sshClientCertPass": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "sshClientCert": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "username": t.string().optional(),
            "certType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigSshPublicKeyOut"])
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
    types["EnterpriseCrmEventbusProtoSuccessPolicyIn"] = t.struct(
        {"finalState": t.string().optional()}
    ).named(renames["EnterpriseCrmEventbusProtoSuccessPolicyIn"])
    types["EnterpriseCrmEventbusProtoSuccessPolicyOut"] = t.struct(
        {
            "finalState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoSuccessPolicyOut"])
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
    types["GoogleCloudIntegrationsV1alphaLiftSuspensionRequestIn"] = t.struct(
        {"suspensionResult": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaLiftSuspensionRequestIn"])
    types["GoogleCloudIntegrationsV1alphaLiftSuspensionRequestOut"] = t.struct(
        {
            "suspensionResult": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaLiftSuspensionRequestOut"])
    types["EnterpriseCrmEventbusProtoDoubleArrayFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoDoubleArrayFunctionIn"])
    types["EnterpriseCrmEventbusProtoDoubleArrayFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoDoubleArrayFunctionOut"])
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
    types["GoogleCloudIntegrationsV1alphaExecutionSnapshotIn"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "executionSnapshotMetadata": t.proxy(
                renames[
                    "GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataIn"
                ]
            ).optional(),
            "taskExecutionDetails": t.array(
                t.proxy(renames["GoogleCloudIntegrationsV1alphaTaskExecutionDetailsIn"])
            ).optional(),
            "checkpointTaskNumber": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecutionSnapshotIn"])
    types["GoogleCloudIntegrationsV1alphaExecutionSnapshotOut"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "executionSnapshotMetadata": t.proxy(
                renames[
                    "GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadataOut"
                ]
            ).optional(),
            "taskExecutionDetails": t.array(
                t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaTaskExecutionDetailsOut"]
                )
            ).optional(),
            "checkpointTaskNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaExecutionSnapshotOut"])
    types["EnterpriseCrmEventbusProtoBooleanFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoBooleanFunctionIn"])
    types["EnterpriseCrmEventbusProtoBooleanFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoBooleanFunctionOut"])
    types["EnterpriseCrmFrontendsEventbusProtoParamSpecEntryIn"] = t.struct(
        {
            "protoDef": t.proxy(
                renames["EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionIn"]
            ).optional(),
            "jsonSchema": t.string().optional(),
            "key": t.string().optional(),
            "className": t.string().optional(),
            "isDeprecated": t.boolean().optional(),
            "config": t.proxy(
                renames["EnterpriseCrmEventbusProtoParamSpecEntryConfigIn"]
            ).optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn"]
            ).optional(),
            "validationRule": t.proxy(
                renames["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIn"]
            ).optional(),
            "dataType": t.string().optional(),
            "collectionElementClassName": t.string().optional(),
            "required": t.boolean().optional(),
            "isOutput": t.boolean(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParamSpecEntryIn"])
    types["EnterpriseCrmFrontendsEventbusProtoParamSpecEntryOut"] = t.struct(
        {
            "protoDef": t.proxy(
                renames["EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinitionOut"]
            ).optional(),
            "jsonSchema": t.string().optional(),
            "key": t.string().optional(),
            "className": t.string().optional(),
            "isDeprecated": t.boolean().optional(),
            "config": t.proxy(
                renames["EnterpriseCrmEventbusProtoParamSpecEntryConfigOut"]
            ).optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "validationRule": t.proxy(
                renames["EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleOut"]
            ).optional(),
            "dataType": t.string().optional(),
            "collectionElementClassName": t.string().optional(),
            "required": t.boolean().optional(),
            "isOutput": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoParamSpecEntryOut"])
    types["EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayIn"] = t.struct(
        {"booleanValues": t.array(t.boolean())}
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayIn"])
    types["EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayOut"] = t.struct(
        {
            "booleanValues": t.array(t.boolean()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoBooleanParameterArrayOut"])
    types["GoogleCloudIntegrationsV1alphaStringParameterArrayIn"] = t.struct(
        {"stringValues": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaStringParameterArrayIn"])
    types["GoogleCloudIntegrationsV1alphaStringParameterArrayOut"] = t.struct(
        {
            "stringValues": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaStringParameterArrayOut"])
    types["GoogleCloudIntegrationsV1alphaSfdcInstanceIn"] = t.struct(
        {
            "description": t.string().optional(),
            "serviceAuthority": t.string().optional(),
            "sfdcOrgId": t.string().optional(),
            "displayName": t.string().optional(),
            "authConfigId": t.array(t.string()).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceIn"])
    types["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "deleteTime": t.string().optional(),
            "serviceAuthority": t.string().optional(),
            "sfdcOrgId": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "authConfigId": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"])
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
    types["EnterpriseCrmEventbusProtoAddressIn"] = t.struct(
        {
            "tokens": t.array(t.proxy(renames["EnterpriseCrmEventbusProtoTokenIn"])),
            "name": t.string(),
            "email": t.string(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoAddressIn"])
    types["EnterpriseCrmEventbusProtoAddressOut"] = t.struct(
        {
            "tokens": t.array(t.proxy(renames["EnterpriseCrmEventbusProtoTokenOut"])),
            "name": t.string(),
            "email": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoAddressOut"])
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
    types[
        "EnterpriseCrmEventbusProtoConnectorsGenericConnectorTaskConfigIn"
    ] = t.struct(
        {
            "operation": t.string().optional(),
            "connection": t.proxy(
                renames["EnterpriseCrmEventbusProtoConnectorsConnectionIn"]
            ).optional(),
        }
    ).named(
        renames["EnterpriseCrmEventbusProtoConnectorsGenericConnectorTaskConfigIn"]
    )
    types[
        "EnterpriseCrmEventbusProtoConnectorsGenericConnectorTaskConfigOut"
    ] = t.struct(
        {
            "operation": t.string().optional(),
            "connection": t.proxy(
                renames["EnterpriseCrmEventbusProtoConnectorsConnectionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["EnterpriseCrmEventbusProtoConnectorsGenericConnectorTaskConfigOut"]
    )
    types["EnterpriseCrmEventbusProtoDoubleFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoDoubleFunctionIn"])
    types["EnterpriseCrmEventbusProtoDoubleFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoDoubleFunctionOut"])
    types["EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamIn"] = t.struct(
        {
            "scope": t.string().optional(),
            "allowedServiceAccountInContext": t.boolean(),
            "allowedCredentialTypes": t.array(t.string()).optional(),
            "authConfigId": t.string().optional(),
            "useServiceAccountInContext": t.boolean(),
        }
    ).named(renames["EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamIn"])
    types["EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamOut"] = t.struct(
        {
            "scope": t.string().optional(),
            "allowedServiceAccountInContext": t.boolean(),
            "allowedCredentialTypes": t.array(t.string()).optional(),
            "authConfigId": t.string().optional(),
            "useServiceAccountInContext": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusAuthconfigAuthConfigTaskParamOut"])
    types["GoogleCloudIntegrationsV1alphaAuthConfigIn"] = t.struct(
        {
            "visibility": t.string().optional(),
            "decryptedCredential": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCredentialIn"]
            ).optional(),
            "creatorEmail": t.string().optional(),
            "state": t.string().optional(),
            "expiryNotificationDuration": t.array(t.string()).optional(),
            "validTime": t.string().optional(),
            "credentialType": t.string().optional(),
            "displayName": t.string().optional(),
            "overrideValidTime": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "lastModifierEmail": t.string().optional(),
            "reason": t.string().optional(),
            "certificateId": t.string().optional(),
            "encryptedCredential": t.string().optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaAuthConfigIn"])
    types["GoogleCloudIntegrationsV1alphaAuthConfigOut"] = t.struct(
        {
            "visibility": t.string().optional(),
            "updateTime": t.string().optional(),
            "decryptedCredential": t.proxy(
                renames["GoogleCloudIntegrationsV1alphaCredentialOut"]
            ).optional(),
            "creatorEmail": t.string().optional(),
            "state": t.string().optional(),
            "expiryNotificationDuration": t.array(t.string()).optional(),
            "validTime": t.string().optional(),
            "credentialType": t.string().optional(),
            "displayName": t.string().optional(),
            "overrideValidTime": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "lastModifierEmail": t.string().optional(),
            "reason": t.string().optional(),
            "certificateId": t.string().optional(),
            "encryptedCredential": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaAuthConfigOut"])
    types["EnterpriseCrmEventbusProtoWorkflowAlertConfigIn"] = t.struct(
        {
            "warningEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn"]
            ),
            "errorEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListIn"]
            ),
            "numAggregationPeriods": t.integer().optional(),
            "alertName": t.string().optional(),
            "metricType": t.string(),
            "aggregationPeriod": t.string().optional(),
            "onlyFinalAttempt": t.boolean().optional(),
            "playbookUrl": t.string().optional(),
            "thresholdType": t.string().optional(),
            "alertDisabled": t.boolean().optional(),
            "durationThresholdMs": t.string().optional(),
            "clientId": t.string().optional(),
            "thresholdValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoWorkflowAlertConfigIn"])
    types["EnterpriseCrmEventbusProtoWorkflowAlertConfigOut"] = t.struct(
        {
            "warningEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut"]
            ),
            "errorEnumList": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumListOut"]
            ),
            "numAggregationPeriods": t.integer().optional(),
            "alertName": t.string().optional(),
            "metricType": t.string(),
            "aggregationPeriod": t.string().optional(),
            "onlyFinalAttempt": t.boolean().optional(),
            "playbookUrl": t.string().optional(),
            "thresholdType": t.string().optional(),
            "alertDisabled": t.boolean().optional(),
            "durationThresholdMs": t.string().optional(),
            "clientId": t.string().optional(),
            "thresholdValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValueOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoWorkflowAlertConfigOut"])
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
    types["GoogleCloudIntegrationsV1alphaBooleanParameterArrayIn"] = t.struct(
        {"booleanValues": t.array(t.boolean()).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaBooleanParameterArrayIn"])
    types["GoogleCloudIntegrationsV1alphaBooleanParameterArrayOut"] = t.struct(
        {
            "booleanValues": t.array(t.boolean()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaBooleanParameterArrayOut"])
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
    types["EnterpriseCrmLoggingGwsFieldLimitsIn"] = t.struct(
        {
            "maxArraySize": t.integer().optional(),
            "logType": t.array(t.string()).optional(),
            "logAction": t.string(),
            "shortenerType": t.string(),
            "maxStringLength": t.integer().optional(),
        }
    ).named(renames["EnterpriseCrmLoggingGwsFieldLimitsIn"])
    types["EnterpriseCrmLoggingGwsFieldLimitsOut"] = t.struct(
        {
            "maxArraySize": t.integer().optional(),
            "logType": t.array(t.string()).optional(),
            "logAction": t.string(),
            "shortenerType": t.string(),
            "maxStringLength": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmLoggingGwsFieldLimitsOut"])
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
    types["GoogleCloudIntegrationsV1alphaFailurePolicyIn"] = t.struct(
        {
            "maxRetries": t.integer(),
            "retryStrategy": t.string().optional(),
            "intervalTime": t.string(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaFailurePolicyIn"])
    types["GoogleCloudIntegrationsV1alphaFailurePolicyOut"] = t.struct(
        {
            "maxRetries": t.integer(),
            "retryStrategy": t.string().optional(),
            "intervalTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaFailurePolicyOut"])
    types["GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowIn"] = t.struct(
        {
            "authCode": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "clientSecret": t.proxy(
                renames["GoogleCloudConnectorsV1SecretIn"]
            ).optional(),
            "pkceVerifier": t.string().optional(),
            "clientId": t.string().optional(),
            "redirectUri": t.string().optional(),
            "enablePkce": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowIn"])
    types["GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowOut"] = t.struct(
        {
            "authCode": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "clientSecret": t.proxy(
                renames["GoogleCloudConnectorsV1SecretOut"]
            ).optional(),
            "pkceVerifier": t.string().optional(),
            "clientId": t.string().optional(),
            "redirectUri": t.string().optional(),
            "enablePkce": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowOut"])
    types["EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn"] = t.struct(
        {
            "triggerNumber": t.string(),
            "pauseWorkflowExecutions": t.boolean().optional(),
            "startTasks": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoNextTaskIn"])
            ).optional(),
            "errorCatcherId": t.string().optional(),
            "position": t.proxy(
                renames["EnterpriseCrmEventbusProtoCoordinateIn"]
            ).optional(),
            "triggerCriteria": t.proxy(
                renames["EnterpriseCrmEventbusProtoTriggerCriteriaIn"]
            ).optional(),
            "triggerType": t.string(),
            "enabledClients": t.array(t.string()),
            "nextTasksExecutionPolicy": t.string().optional(),
            "description": t.string().optional(),
            "triggerId": t.string().optional(),
            "label": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "cloudSchedulerConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoCloudSchedulerConfigIn"]
            ),
            "alertConfig": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoWorkflowAlertConfigIn"])
            ).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigIn"])
    types["EnterpriseCrmFrontendsEventbusProtoTriggerConfigOut"] = t.struct(
        {
            "triggerNumber": t.string(),
            "pauseWorkflowExecutions": t.boolean().optional(),
            "startTasks": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoNextTaskOut"])
            ).optional(),
            "errorCatcherId": t.string().optional(),
            "position": t.proxy(
                renames["EnterpriseCrmEventbusProtoCoordinateOut"]
            ).optional(),
            "triggerCriteria": t.proxy(
                renames["EnterpriseCrmEventbusProtoTriggerCriteriaOut"]
            ).optional(),
            "triggerType": t.string(),
            "enabledClients": t.array(t.string()),
            "nextTasksExecutionPolicy": t.string().optional(),
            "description": t.string().optional(),
            "triggerId": t.string().optional(),
            "label": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "cloudSchedulerConfig": t.proxy(
                renames["EnterpriseCrmEventbusProtoCloudSchedulerConfigOut"]
            ),
            "alertConfig": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoWorkflowAlertConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoTriggerConfigOut"])
    types["EnterpriseCrmEventbusProtoScatterResponseIn"] = t.struct(
        {
            "scatterElement": t.proxy(
                renames["EnterpriseCrmEventbusProtoParameterValueTypeIn"]
            ).optional(),
            "responseParams": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoParameterEntryIn"])
            ).optional(),
            "errorMsg": t.string().optional(),
            "executionIds": t.array(t.string()).optional(),
            "isSuccessful": t.boolean().optional(),
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
            "executionIds": t.array(t.string()).optional(),
            "isSuccessful": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoScatterResponseOut"])
    types["GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequestIn"] = t.struct(
        {"fileFormat": t.string().optional(), "content": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequestIn"])
    types[
        "GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequestOut"
    ] = t.struct(
        {
            "fileFormat": t.string().optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequestOut"]
    )
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
    types["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseIn"] = t.struct(
        {"scriptId": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseIn"])
    types["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseOut"] = t.struct(
        {
            "scriptId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseOut"])
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
    types["EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryIn"] = t.struct(
        {
            "attributes": t.proxy(
                renames["EnterpriseCrmEventbusProtoAttributesIn"]
            ).optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeIn"]
            ).optional(),
            "inOutType": t.string().optional(),
            "dataType": t.string().optional(),
            "isTransient": t.boolean().optional(),
            "jsonSchema": t.string().optional(),
            "producer": t.string(),
            "children": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryIn"
                    ]
                )
            ).optional(),
            "key": t.string().optional(),
            "protoDefName": t.string().optional(),
            "name": t.string().optional(),
            "producedBy": t.proxy(
                renames["EnterpriseCrmEventbusProtoNodeIdentifierIn"]
            ).optional(),
            "protoDefPath": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryIn"])
    types["EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryOut"] = t.struct(
        {
            "attributes": t.proxy(
                renames["EnterpriseCrmEventbusProtoAttributesOut"]
            ).optional(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoParameterValueTypeOut"]
            ).optional(),
            "inOutType": t.string().optional(),
            "dataType": t.string().optional(),
            "isTransient": t.boolean().optional(),
            "jsonSchema": t.string().optional(),
            "producer": t.string(),
            "children": t.array(
                t.proxy(
                    renames[
                        "EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryOut"
                    ]
                )
            ).optional(),
            "key": t.string().optional(),
            "protoDefName": t.string().optional(),
            "name": t.string().optional(),
            "producedBy": t.proxy(
                renames["EnterpriseCrmEventbusProtoNodeIdentifierOut"]
            ).optional(),
            "protoDefPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntryOut"])
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
    types["GoogleCloudIntegrationsV1alphaDoubleParameterArrayIn"] = t.struct(
        {"doubleValues": t.array(t.number()).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaDoubleParameterArrayIn"])
    types["GoogleCloudIntegrationsV1alphaDoubleParameterArrayOut"] = t.struct(
        {
            "doubleValues": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaDoubleParameterArrayOut"])
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
    types["EnterpriseCrmEventbusProtoAttributesIn"] = t.struct(
        {
            "dataType": t.string().optional(),
            "taskVisibility": t.array(t.string()).optional(),
            "isRequired": t.boolean(),
            "isSearchable": t.boolean().optional(),
            "searchable": t.string(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoValueTypeIn"]
            ).optional(),
            "logSettings": t.proxy(
                renames["EnterpriseCrmEventbusProtoLogSettingsIn"]
            ).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoAttributesIn"])
    types["EnterpriseCrmEventbusProtoAttributesOut"] = t.struct(
        {
            "dataType": t.string().optional(),
            "taskVisibility": t.array(t.string()).optional(),
            "isRequired": t.boolean(),
            "isSearchable": t.boolean().optional(),
            "searchable": t.string(),
            "defaultValue": t.proxy(
                renames["EnterpriseCrmEventbusProtoValueTypeOut"]
            ).optional(),
            "logSettings": t.proxy(
                renames["EnterpriseCrmEventbusProtoLogSettingsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoAttributesOut"])
    types["EnterpriseCrmEventbusProtoIntFunctionIn"] = t.struct(
        {"functionName": t.string()}
    ).named(renames["EnterpriseCrmEventbusProtoIntFunctionIn"])
    types["EnterpriseCrmEventbusProtoIntFunctionOut"] = t.struct(
        {
            "functionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoIntFunctionOut"])
    types["EnterpriseCrmEventbusProtoValueTypeIn"] = t.struct(
        {
            "doubleValue": t.number(),
            "intValue": t.string(),
            "stringValue": t.string(),
            "doubleArray": t.proxy(renames["EnterpriseCrmEventbusProtoDoubleArrayIn"]),
            "stringArray": t.proxy(renames["EnterpriseCrmEventbusProtoStringArrayIn"]),
            "intArray": t.proxy(renames["EnterpriseCrmEventbusProtoIntArrayIn"]),
            "protoValue": t.struct({"_": t.string().optional()}),
            "booleanValue": t.boolean(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoValueTypeIn"])
    types["EnterpriseCrmEventbusProtoValueTypeOut"] = t.struct(
        {
            "doubleValue": t.number(),
            "intValue": t.string(),
            "stringValue": t.string(),
            "doubleArray": t.proxy(renames["EnterpriseCrmEventbusProtoDoubleArrayOut"]),
            "stringArray": t.proxy(renames["EnterpriseCrmEventbusProtoStringArrayOut"]),
            "intArray": t.proxy(renames["EnterpriseCrmEventbusProtoIntArrayOut"]),
            "protoValue": t.struct({"_": t.string().optional()}),
            "booleanValue": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmEventbusProtoValueTypeOut"])
    types["GoogleCloudIntegrationsV1alphaCancelExecutionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaCancelExecutionRequestIn"])
    types["GoogleCloudIntegrationsV1alphaCancelExecutionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudIntegrationsV1alphaCancelExecutionRequestOut"])
    types["EnterpriseCrmFrontendsEventbusProtoTaskConfigIn"] = t.struct(
        {
            "position": t.proxy(
                renames["EnterpriseCrmEventbusProtoCoordinateIn"]
            ).optional(),
            "taskEntity": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoTaskEntityIn"]
            ).optional(),
            "taskExecutionStrategy": t.string().optional(),
            "alertConfigs": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskAlertConfigIn"])
            ).optional(),
            "precondition": t.string().optional(),
            "label": t.string().optional(),
            "externalTaskType": t.string(),
            "failurePolicy": t.proxy(
                renames["EnterpriseCrmEventbusProtoFailurePolicyIn"]
            ).optional(),
            "createTime": t.string().optional(),
            "disableStrictTypeValidation": t.boolean().optional(),
            "creatorEmail": t.string().optional(),
            "jsonValidationOption": t.string().optional(),
            "rollbackStrategy": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoRollbackStrategyIn"]
            ).optional(),
            "taskTemplateName": t.string().optional(),
            "nextTasks": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoNextTaskIn"])
            ).optional(),
            "preconditionLabel": t.string().optional(),
            "successPolicy": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuccessPolicyIn"]
            ).optional(),
            "description": t.string().optional(),
            "incomingEdgeCount": t.integer().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "taskNumber": t.string().optional(),
            "taskName": t.string().optional(),
            "taskType": t.string().optional(),
            "taskSpec": t.string().optional(),
            "synchronousCallFailurePolicy": t.proxy(
                renames["EnterpriseCrmEventbusProtoFailurePolicyIn"]
            ).optional(),
            "errorCatcherId": t.string().optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigIn"])
    types["EnterpriseCrmFrontendsEventbusProtoTaskConfigOut"] = t.struct(
        {
            "position": t.proxy(
                renames["EnterpriseCrmEventbusProtoCoordinateOut"]
            ).optional(),
            "taskEntity": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoTaskEntityOut"]
            ).optional(),
            "taskExecutionStrategy": t.string().optional(),
            "alertConfigs": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoTaskAlertConfigOut"])
            ).optional(),
            "precondition": t.string().optional(),
            "label": t.string().optional(),
            "externalTaskType": t.string(),
            "failurePolicy": t.proxy(
                renames["EnterpriseCrmEventbusProtoFailurePolicyOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "disableStrictTypeValidation": t.boolean().optional(),
            "creatorEmail": t.string().optional(),
            "jsonValidationOption": t.string().optional(),
            "rollbackStrategy": t.proxy(
                renames["EnterpriseCrmFrontendsEventbusProtoRollbackStrategyOut"]
            ).optional(),
            "taskTemplateName": t.string().optional(),
            "nextTasks": t.array(
                t.proxy(renames["EnterpriseCrmEventbusProtoNextTaskOut"])
            ).optional(),
            "preconditionLabel": t.string().optional(),
            "successPolicy": t.proxy(
                renames["EnterpriseCrmEventbusProtoSuccessPolicyOut"]
            ).optional(),
            "description": t.string().optional(),
            "incomingEdgeCount": t.integer().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "nextTasksExecutionPolicy": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "taskNumber": t.string().optional(),
            "taskName": t.string().optional(),
            "taskType": t.string().optional(),
            "taskSpec": t.string().optional(),
            "synchronousCallFailurePolicy": t.proxy(
                renames["EnterpriseCrmEventbusProtoFailurePolicyOut"]
            ).optional(),
            "errorCatcherId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseCrmFrontendsEventbusProtoTaskConfigOut"])
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
    types["GoogleCloudIntegrationsV1alphaAccessTokenIn"] = t.struct(
        {
            "accessToken": t.string().optional(),
            "refreshToken": t.string().optional(),
            "refreshTokenExpireTime": t.string().optional(),
            "tokenType": t.string().optional(),
            "accessTokenExpireTime": t.string(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaAccessTokenIn"])
    types["GoogleCloudIntegrationsV1alphaAccessTokenOut"] = t.struct(
        {
            "accessToken": t.string().optional(),
            "refreshToken": t.string().optional(),
            "refreshTokenExpireTime": t.string().optional(),
            "tokenType": t.string().optional(),
            "accessTokenExpireTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudIntegrationsV1alphaAccessTokenOut"])

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
                "code": t.string().optional(),
                "gcpProjectId": t.string().optional(),
                "redirectUri": t.string().optional(),
                "product": t.string().optional(),
                "state": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaGenerateTokenResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesPatch"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesGet"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesList"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesCreate"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesDelete"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesSfdcChannelsDelete"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "channelTopic": t.string().optional(),
                "lastReplayId": t.string().optional(),
                "displayName": t.string().optional(),
                "isActive": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesSfdcChannelsCreate"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "channelTopic": t.string().optional(),
                "lastReplayId": t.string().optional(),
                "displayName": t.string().optional(),
                "isActive": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesSfdcChannelsList"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "channelTopic": t.string().optional(),
                "lastReplayId": t.string().optional(),
                "displayName": t.string().optional(),
                "isActive": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesSfdcChannelsGet"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "channelTopic": t.string().optional(),
                "lastReplayId": t.string().optional(),
                "displayName": t.string().optional(),
                "isActive": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSfdcInstancesSfdcChannelsPatch"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "channelTopic": t.string().optional(),
                "lastReplayId": t.string().optional(),
                "displayName": t.string().optional(),
                "isActive": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationtemplatesVersionsCreate"
    ] = integrations.get(
        "v1alpha/{parent}/versions",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationtemplatesVersionsGet"
    ] = integrations.get(
        "v1alpha/{parent}/versions",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationtemplatesVersionsList"
    ] = integrations.get(
        "v1alpha/{parent}/versions",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsCertificatesList"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "rawCertificate": t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaClientCertificateIn"]
                ).optional(),
                "credentialId": t.string().optional(),
                "certificateStatus": t.string().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "requestorId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaCertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsCertificatesGet"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "rawCertificate": t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaClientCertificateIn"]
                ).optional(),
                "credentialId": t.string().optional(),
                "certificateStatus": t.string().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "requestorId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaCertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsCertificatesCreate"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "rawCertificate": t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaClientCertificateIn"]
                ).optional(),
                "credentialId": t.string().optional(),
                "certificateStatus": t.string().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "requestorId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaCertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsCertificatesDelete"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "rawCertificate": t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaClientCertificateIn"]
                ).optional(),
                "credentialId": t.string().optional(),
                "certificateStatus": t.string().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "requestorId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaCertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsCertificatesPatch"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "rawCertificate": t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaClientCertificateIn"]
                ).optional(),
                "credentialId": t.string().optional(),
                "certificateStatus": t.string().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "requestorId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaCertificateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsAuthConfigsGet"] = integrations.get(
        "v1alpha/{parent}/authConfigs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListAuthConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsDelete"] = integrations.get(
        "v1alpha/{parent}/integrations",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListIntegrationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsSchedule"] = integrations.get(
        "v1alpha/{parent}/integrations",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
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
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
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
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListIntegrationsResponseOut"]),
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
        "projectsLocationsProductsIntegrationsExecutionsSuspensionsResolve"
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
        "projectsLocationsProductsIntegrationsExecutionsSuspensionsList"
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
        "projectsLocationsProductsIntegrationsExecutionsSuspensionsLift"
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
        "projectsLocationsProductsIntegrationsVersionsPublish"
    ] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsVersionsDownload"
    ] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsIntegrationsVersionsGet"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsVersionsUnpublish"
    ] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsVersionsPatch"
    ] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsVersionsList"
    ] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsVersionsUpload"
    ] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsVersionsTakeoverEditLock"
    ] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsVersionsCreate"
    ] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsIntegrationsVersionsDelete"
    ] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsSfdcInstancesPatch"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsSfdcInstancesDelete"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsSfdcInstancesCreate"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsSfdcInstancesList"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProductsSfdcInstancesGet"] = integrations.get(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaSfdcInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsSfdcInstancesSfdcChannelsList"
    ] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsSfdcInstancesSfdcChannelsPatch"
    ] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsSfdcInstancesSfdcChannelsGet"
    ] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsSfdcInstancesSfdcChannelsCreate"
    ] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProductsSfdcInstancesSfdcChannelsDelete"
    ] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
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
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "filter": t.string().optional(),
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
    functions["projectsLocationsAuthConfigsGet"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "clientCertificate.encryptedPrivateKey": t.string().optional(),
                "clientCertificate.passphrase": t.string().optional(),
                "name": t.string().optional(),
                "clientCertificate.sslCertificate": t.string().optional(),
                "visibility": t.string().optional(),
                "decryptedCredential": t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaCredentialIn"]
                ).optional(),
                "creatorEmail": t.string().optional(),
                "state": t.string().optional(),
                "expiryNotificationDuration": t.array(t.string()).optional(),
                "validTime": t.string().optional(),
                "credentialType": t.string().optional(),
                "displayName": t.string().optional(),
                "overrideValidTime": t.string().optional(),
                "description": t.string().optional(),
                "lastModifierEmail": t.string().optional(),
                "reason": t.string().optional(),
                "certificateId": t.string().optional(),
                "encryptedCredential": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaAuthConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthConfigsList"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "clientCertificate.encryptedPrivateKey": t.string().optional(),
                "clientCertificate.passphrase": t.string().optional(),
                "name": t.string().optional(),
                "clientCertificate.sslCertificate": t.string().optional(),
                "visibility": t.string().optional(),
                "decryptedCredential": t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaCredentialIn"]
                ).optional(),
                "creatorEmail": t.string().optional(),
                "state": t.string().optional(),
                "expiryNotificationDuration": t.array(t.string()).optional(),
                "validTime": t.string().optional(),
                "credentialType": t.string().optional(),
                "displayName": t.string().optional(),
                "overrideValidTime": t.string().optional(),
                "description": t.string().optional(),
                "lastModifierEmail": t.string().optional(),
                "reason": t.string().optional(),
                "certificateId": t.string().optional(),
                "encryptedCredential": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaAuthConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthConfigsCreate"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "clientCertificate.encryptedPrivateKey": t.string().optional(),
                "clientCertificate.passphrase": t.string().optional(),
                "name": t.string().optional(),
                "clientCertificate.sslCertificate": t.string().optional(),
                "visibility": t.string().optional(),
                "decryptedCredential": t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaCredentialIn"]
                ).optional(),
                "creatorEmail": t.string().optional(),
                "state": t.string().optional(),
                "expiryNotificationDuration": t.array(t.string()).optional(),
                "validTime": t.string().optional(),
                "credentialType": t.string().optional(),
                "displayName": t.string().optional(),
                "overrideValidTime": t.string().optional(),
                "description": t.string().optional(),
                "lastModifierEmail": t.string().optional(),
                "reason": t.string().optional(),
                "certificateId": t.string().optional(),
                "encryptedCredential": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaAuthConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthConfigsDelete"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "clientCertificate.encryptedPrivateKey": t.string().optional(),
                "clientCertificate.passphrase": t.string().optional(),
                "name": t.string().optional(),
                "clientCertificate.sslCertificate": t.string().optional(),
                "visibility": t.string().optional(),
                "decryptedCredential": t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaCredentialIn"]
                ).optional(),
                "creatorEmail": t.string().optional(),
                "state": t.string().optional(),
                "expiryNotificationDuration": t.array(t.string()).optional(),
                "validTime": t.string().optional(),
                "credentialType": t.string().optional(),
                "displayName": t.string().optional(),
                "overrideValidTime": t.string().optional(),
                "description": t.string().optional(),
                "lastModifierEmail": t.string().optional(),
                "reason": t.string().optional(),
                "certificateId": t.string().optional(),
                "encryptedCredential": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaAuthConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthConfigsPatch"] = integrations.patch(
        "v1alpha/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "clientCertificate.encryptedPrivateKey": t.string().optional(),
                "clientCertificate.passphrase": t.string().optional(),
                "name": t.string().optional(),
                "clientCertificate.sslCertificate": t.string().optional(),
                "visibility": t.string().optional(),
                "decryptedCredential": t.proxy(
                    renames["GoogleCloudIntegrationsV1alphaCredentialIn"]
                ).optional(),
                "creatorEmail": t.string().optional(),
                "state": t.string().optional(),
                "expiryNotificationDuration": t.array(t.string()).optional(),
                "validTime": t.string().optional(),
                "credentialType": t.string().optional(),
                "displayName": t.string().optional(),
                "overrideValidTime": t.string().optional(),
                "description": t.string().optional(),
                "lastModifierEmail": t.string().optional(),
                "reason": t.string().optional(),
                "certificateId": t.string().optional(),
                "encryptedCredential": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaAuthConfigOut"]),
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
    functions["projectsLocationsIntegrationsDelete"] = integrations.get(
        "v1alpha/{parent}/integrations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListIntegrationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsSchedule"] = integrations.get(
        "v1alpha/{parent}/integrations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudIntegrationsV1alphaListIntegrationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsExecutionsList"] = integrations.get(
        "v1alpha/{parent}/executions",
        t.struct(
            {
                "filterParams.parameterPairValue": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filterParams.endTime": t.string().optional(),
                "filterParams.parameterPairKey": t.string().optional(),
                "filterParams.taskStatuses": t.string().optional(),
                "filterParams.eventStatuses": t.string().optional(),
                "orderBy": t.string().optional(),
                "filterParams.startTime": t.string().optional(),
                "filter": t.string().optional(),
                "filterParams.executionId": t.string().optional(),
                "filterParams.parameterValue": t.string().optional(),
                "filterParams.parameterKey": t.string().optional(),
                "refreshAcl": t.boolean().optional(),
                "filterParams.customFilter": t.string().optional(),
                "truncateParams": t.boolean().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filterParams.parameterType": t.string().optional(),
                "filterParams.workflowName": t.string().optional(),
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
    functions["projectsLocationsIntegrationsVersionsPublish"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsGet"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsIntegrationsVersionsTakeoverEditLock"
    ] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsUpload"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsDownload"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsUnpublish"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsCreate"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsList"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsPatch"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsIntegrationsVersionsDelete"] = integrations.delete(
        "v1alpha/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="integrations",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
