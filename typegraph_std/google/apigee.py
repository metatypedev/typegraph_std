from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_apigee():
    apigee = HTTPRuntime("https://apigee.googleapis.com/")

    renames = {
        "ErrorResponse": "_apigee_1_ErrorResponse",
        "GoogleCloudApigeeV1GraphQLOperationConfigIn": "_apigee_2_GoogleCloudApigeeV1GraphQLOperationConfigIn",
        "GoogleCloudApigeeV1GraphQLOperationConfigOut": "_apigee_3_GoogleCloudApigeeV1GraphQLOperationConfigOut",
        "GoogleCloudApigeeV1AppGroupAppKeyIn": "_apigee_4_GoogleCloudApigeeV1AppGroupAppKeyIn",
        "GoogleCloudApigeeV1AppGroupAppKeyOut": "_apigee_5_GoogleCloudApigeeV1AppGroupAppKeyOut",
        "GoogleCloudApigeeV1ResourceFilesIn": "_apigee_6_GoogleCloudApigeeV1ResourceFilesIn",
        "GoogleCloudApigeeV1ResourceFilesOut": "_apigee_7_GoogleCloudApigeeV1ResourceFilesOut",
        "GoogleCloudApigeeV1RatePlanIn": "_apigee_8_GoogleCloudApigeeV1RatePlanIn",
        "GoogleCloudApigeeV1RatePlanOut": "_apigee_9_GoogleCloudApigeeV1RatePlanOut",
        "GoogleCloudApigeeV1ApiProductIn": "_apigee_10_GoogleCloudApigeeV1ApiProductIn",
        "GoogleCloudApigeeV1ApiProductOut": "_apigee_11_GoogleCloudApigeeV1ApiProductOut",
        "GoogleRpcPreconditionFailureIn": "_apigee_12_GoogleRpcPreconditionFailureIn",
        "GoogleRpcPreconditionFailureOut": "_apigee_13_GoogleRpcPreconditionFailureOut",
        "GoogleCloudApigeeV1PropertiesIn": "_apigee_14_GoogleCloudApigeeV1PropertiesIn",
        "GoogleCloudApigeeV1PropertiesOut": "_apigee_15_GoogleCloudApigeeV1PropertiesOut",
        "GoogleCloudApigeeV1DeleteResponseIn": "_apigee_16_GoogleCloudApigeeV1DeleteResponseIn",
        "GoogleCloudApigeeV1DeleteResponseOut": "_apigee_17_GoogleCloudApigeeV1DeleteResponseOut",
        "GoogleCloudApigeeV1SecurityReportResultMetadataIn": "_apigee_18_GoogleCloudApigeeV1SecurityReportResultMetadataIn",
        "GoogleCloudApigeeV1SecurityReportResultMetadataOut": "_apigee_19_GoogleCloudApigeeV1SecurityReportResultMetadataOut",
        "GoogleCloudApigeeV1CertInfoIn": "_apigee_20_GoogleCloudApigeeV1CertInfoIn",
        "GoogleCloudApigeeV1CertInfoOut": "_apigee_21_GoogleCloudApigeeV1CertInfoOut",
        "GoogleCloudApigeeV1SessionIn": "_apigee_22_GoogleCloudApigeeV1SessionIn",
        "GoogleCloudApigeeV1SessionOut": "_apigee_23_GoogleCloudApigeeV1SessionOut",
        "GoogleRpcPreconditionFailureViolationIn": "_apigee_24_GoogleRpcPreconditionFailureViolationIn",
        "GoogleRpcPreconditionFailureViolationOut": "_apigee_25_GoogleRpcPreconditionFailureViolationOut",
        "GoogleCloudApigeeV1EntityMetadataIn": "_apigee_26_GoogleCloudApigeeV1EntityMetadataIn",
        "GoogleCloudApigeeV1EntityMetadataOut": "_apigee_27_GoogleCloudApigeeV1EntityMetadataOut",
        "GoogleCloudApigeeV1ListSharedFlowsResponseIn": "_apigee_28_GoogleCloudApigeeV1ListSharedFlowsResponseIn",
        "GoogleCloudApigeeV1ListSharedFlowsResponseOut": "_apigee_29_GoogleCloudApigeeV1ListSharedFlowsResponseOut",
        "GoogleCloudApigeeV1SharedFlowRevisionIn": "_apigee_30_GoogleCloudApigeeV1SharedFlowRevisionIn",
        "GoogleCloudApigeeV1SharedFlowRevisionOut": "_apigee_31_GoogleCloudApigeeV1SharedFlowRevisionOut",
        "GoogleCloudApigeeV1KeyValueMapIn": "_apigee_32_GoogleCloudApigeeV1KeyValueMapIn",
        "GoogleCloudApigeeV1KeyValueMapOut": "_apigee_33_GoogleCloudApigeeV1KeyValueMapOut",
        "GoogleCloudApigeeV1ListKeyValueEntriesResponseIn": "_apigee_34_GoogleCloudApigeeV1ListKeyValueEntriesResponseIn",
        "GoogleCloudApigeeV1ListKeyValueEntriesResponseOut": "_apigee_35_GoogleCloudApigeeV1ListKeyValueEntriesResponseOut",
        "GoogleCloudApigeeV1AddonsConfigIn": "_apigee_36_GoogleCloudApigeeV1AddonsConfigIn",
        "GoogleCloudApigeeV1AddonsConfigOut": "_apigee_37_GoogleCloudApigeeV1AddonsConfigOut",
        "GoogleCloudApigeeV1ResultIn": "_apigee_38_GoogleCloudApigeeV1ResultIn",
        "GoogleCloudApigeeV1ResultOut": "_apigee_39_GoogleCloudApigeeV1ResultOut",
        "GoogleIamV1AuditConfigIn": "_apigee_40_GoogleIamV1AuditConfigIn",
        "GoogleIamV1AuditConfigOut": "_apigee_41_GoogleIamV1AuditConfigOut",
        "GoogleCloudApigeeV1OperationMetadataProgressIn": "_apigee_42_GoogleCloudApigeeV1OperationMetadataProgressIn",
        "GoogleCloudApigeeV1OperationMetadataProgressOut": "_apigee_43_GoogleCloudApigeeV1OperationMetadataProgressOut",
        "GoogleIamV1TestIamPermissionsResponseIn": "_apigee_44_GoogleIamV1TestIamPermissionsResponseIn",
        "GoogleIamV1TestIamPermissionsResponseOut": "_apigee_45_GoogleIamV1TestIamPermissionsResponseOut",
        "GoogleCloudApigeeV1DataCollectorIn": "_apigee_46_GoogleCloudApigeeV1DataCollectorIn",
        "GoogleCloudApigeeV1DataCollectorOut": "_apigee_47_GoogleCloudApigeeV1DataCollectorOut",
        "GoogleCloudApigeeV1ListCustomReportsResponseIn": "_apigee_48_GoogleCloudApigeeV1ListCustomReportsResponseIn",
        "GoogleCloudApigeeV1ListCustomReportsResponseOut": "_apigee_49_GoogleCloudApigeeV1ListCustomReportsResponseOut",
        "GoogleCloudApigeeV1QueryTimeSeriesStatsResponseIn": "_apigee_50_GoogleCloudApigeeV1QueryTimeSeriesStatsResponseIn",
        "GoogleCloudApigeeV1QueryTimeSeriesStatsResponseOut": "_apigee_51_GoogleCloudApigeeV1QueryTimeSeriesStatsResponseOut",
        "GoogleCloudApigeeV1SecurityProfileScoringConfigIn": "_apigee_52_GoogleCloudApigeeV1SecurityProfileScoringConfigIn",
        "GoogleCloudApigeeV1SecurityProfileScoringConfigOut": "_apigee_53_GoogleCloudApigeeV1SecurityProfileScoringConfigOut",
        "GoogleCloudApigeeV1KeystoreIn": "_apigee_54_GoogleCloudApigeeV1KeystoreIn",
        "GoogleCloudApigeeV1KeystoreOut": "_apigee_55_GoogleCloudApigeeV1KeystoreOut",
        "GoogleCloudApigeeV1AppGroupAppIn": "_apigee_56_GoogleCloudApigeeV1AppGroupAppIn",
        "GoogleCloudApigeeV1AppGroupAppOut": "_apigee_57_GoogleCloudApigeeV1AppGroupAppOut",
        "GoogleCloudApigeeV1EnvironmentConfigIn": "_apigee_58_GoogleCloudApigeeV1EnvironmentConfigIn",
        "GoogleCloudApigeeV1EnvironmentConfigOut": "_apigee_59_GoogleCloudApigeeV1EnvironmentConfigOut",
        "GoogleCloudApigeeV1ListEnvironmentGroupsResponseIn": "_apigee_60_GoogleCloudApigeeV1ListEnvironmentGroupsResponseIn",
        "GoogleCloudApigeeV1ListEnvironmentGroupsResponseOut": "_apigee_61_GoogleCloudApigeeV1ListEnvironmentGroupsResponseOut",
        "GoogleCloudApigeeV1UpdateErrorIn": "_apigee_62_GoogleCloudApigeeV1UpdateErrorIn",
        "GoogleCloudApigeeV1UpdateErrorOut": "_apigee_63_GoogleCloudApigeeV1UpdateErrorOut",
        "GoogleCloudApigeeV1TestDatastoreResponseIn": "_apigee_64_GoogleCloudApigeeV1TestDatastoreResponseIn",
        "GoogleCloudApigeeV1TestDatastoreResponseOut": "_apigee_65_GoogleCloudApigeeV1TestDatastoreResponseOut",
        "GoogleCloudApigeeV1DeveloperSubscriptionIn": "_apigee_66_GoogleCloudApigeeV1DeveloperSubscriptionIn",
        "GoogleCloudApigeeV1DeveloperSubscriptionOut": "_apigee_67_GoogleCloudApigeeV1DeveloperSubscriptionOut",
        "GoogleCloudApigeeV1ApiProxyRevisionIn": "_apigee_68_GoogleCloudApigeeV1ApiProxyRevisionIn",
        "GoogleCloudApigeeV1ApiProxyRevisionOut": "_apigee_69_GoogleCloudApigeeV1ApiProxyRevisionOut",
        "GoogleCloudApigeeV1CredentialIn": "_apigee_70_GoogleCloudApigeeV1CredentialIn",
        "GoogleCloudApigeeV1CredentialOut": "_apigee_71_GoogleCloudApigeeV1CredentialOut",
        "GoogleCloudApigeeV1ListNatAddressesResponseIn": "_apigee_72_GoogleCloudApigeeV1ListNatAddressesResponseIn",
        "GoogleCloudApigeeV1ListNatAddressesResponseOut": "_apigee_73_GoogleCloudApigeeV1ListNatAddressesResponseOut",
        "GoogleCloudApigeeV1CustomReportIn": "_apigee_74_GoogleCloudApigeeV1CustomReportIn",
        "GoogleCloudApigeeV1CustomReportOut": "_apigee_75_GoogleCloudApigeeV1CustomReportOut",
        "GoogleLongrunningOperationIn": "_apigee_76_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_apigee_77_GoogleLongrunningOperationOut",
        "GoogleTypeMoneyIn": "_apigee_78_GoogleTypeMoneyIn",
        "GoogleTypeMoneyOut": "_apigee_79_GoogleTypeMoneyOut",
        "GoogleCloudApigeeV1DebugSessionTransactionIn": "_apigee_80_GoogleCloudApigeeV1DebugSessionTransactionIn",
        "GoogleCloudApigeeV1DebugSessionTransactionOut": "_apigee_81_GoogleCloudApigeeV1DebugSessionTransactionOut",
        "GoogleCloudApigeeV1ListEndpointAttachmentsResponseIn": "_apigee_82_GoogleCloudApigeeV1ListEndpointAttachmentsResponseIn",
        "GoogleCloudApigeeV1ListEndpointAttachmentsResponseOut": "_apigee_83_GoogleCloudApigeeV1ListEndpointAttachmentsResponseOut",
        "GoogleCloudApigeeV1QueryTimeSeriesStatsResponseSequenceIn": "_apigee_84_GoogleCloudApigeeV1QueryTimeSeriesStatsResponseSequenceIn",
        "GoogleCloudApigeeV1QueryTimeSeriesStatsResponseSequenceOut": "_apigee_85_GoogleCloudApigeeV1QueryTimeSeriesStatsResponseSequenceOut",
        "GoogleCloudApigeeV1SyncAuthorizationIn": "_apigee_86_GoogleCloudApigeeV1SyncAuthorizationIn",
        "GoogleCloudApigeeV1SyncAuthorizationOut": "_apigee_87_GoogleCloudApigeeV1SyncAuthorizationOut",
        "GoogleCloudApigeeV1SecurityReportIn": "_apigee_88_GoogleCloudApigeeV1SecurityReportIn",
        "GoogleCloudApigeeV1SecurityReportOut": "_apigee_89_GoogleCloudApigeeV1SecurityReportOut",
        "GoogleCloudApigeeV1InstanceAttachmentIn": "_apigee_90_GoogleCloudApigeeV1InstanceAttachmentIn",
        "GoogleCloudApigeeV1InstanceAttachmentOut": "_apigee_91_GoogleCloudApigeeV1InstanceAttachmentOut",
        "GoogleCloudApigeeV1GenerateUploadUrlRequestIn": "_apigee_92_GoogleCloudApigeeV1GenerateUploadUrlRequestIn",
        "GoogleCloudApigeeV1GenerateUploadUrlRequestOut": "_apigee_93_GoogleCloudApigeeV1GenerateUploadUrlRequestOut",
        "GoogleCloudApigeeV1ListSecurityIncidentsResponseIn": "_apigee_94_GoogleCloudApigeeV1ListSecurityIncidentsResponseIn",
        "GoogleCloudApigeeV1ListSecurityIncidentsResponseOut": "_apigee_95_GoogleCloudApigeeV1ListSecurityIncidentsResponseOut",
        "GoogleCloudApigeeV1DeveloperBalanceWalletIn": "_apigee_96_GoogleCloudApigeeV1DeveloperBalanceWalletIn",
        "GoogleCloudApigeeV1DeveloperBalanceWalletOut": "_apigee_97_GoogleCloudApigeeV1DeveloperBalanceWalletOut",
        "GoogleCloudApigeeV1ResourceStatusIn": "_apigee_98_GoogleCloudApigeeV1ResourceStatusIn",
        "GoogleCloudApigeeV1ResourceStatusOut": "_apigee_99_GoogleCloudApigeeV1ResourceStatusOut",
        "GoogleCloudApigeeV1TraceConfigIn": "_apigee_100_GoogleCloudApigeeV1TraceConfigIn",
        "GoogleCloudApigeeV1TraceConfigOut": "_apigee_101_GoogleCloudApigeeV1TraceConfigOut",
        "GoogleCloudApigeeV1MonetizationConfigIn": "_apigee_102_GoogleCloudApigeeV1MonetizationConfigIn",
        "GoogleCloudApigeeV1MonetizationConfigOut": "_apigee_103_GoogleCloudApigeeV1MonetizationConfigOut",
        "GoogleCloudApigeeV1ListDeveloperSubscriptionsResponseIn": "_apigee_104_GoogleCloudApigeeV1ListDeveloperSubscriptionsResponseIn",
        "GoogleCloudApigeeV1ListDeveloperSubscriptionsResponseOut": "_apigee_105_GoogleCloudApigeeV1ListDeveloperSubscriptionsResponseOut",
        "GoogleCloudApigeeV1TargetServerIn": "_apigee_106_GoogleCloudApigeeV1TargetServerIn",
        "GoogleCloudApigeeV1TargetServerOut": "_apigee_107_GoogleCloudApigeeV1TargetServerOut",
        "GoogleCloudApigeeV1ReportPropertyIn": "_apigee_108_GoogleCloudApigeeV1ReportPropertyIn",
        "GoogleCloudApigeeV1ReportPropertyOut": "_apigee_109_GoogleCloudApigeeV1ReportPropertyOut",
        "GoogleCloudApigeeV1EndpointChainingRuleIn": "_apigee_110_GoogleCloudApigeeV1EndpointChainingRuleIn",
        "GoogleCloudApigeeV1EndpointChainingRuleOut": "_apigee_111_GoogleCloudApigeeV1EndpointChainingRuleOut",
        "GoogleCloudApigeeV1SharedFlowIn": "_apigee_112_GoogleCloudApigeeV1SharedFlowIn",
        "GoogleCloudApigeeV1SharedFlowOut": "_apigee_113_GoogleCloudApigeeV1SharedFlowOut",
        "GoogleCloudApigeeV1ListApiCategoriesResponseIn": "_apigee_114_GoogleCloudApigeeV1ListApiCategoriesResponseIn",
        "GoogleCloudApigeeV1ListApiCategoriesResponseOut": "_apigee_115_GoogleCloudApigeeV1ListApiCategoriesResponseOut",
        "GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRouteIn": "_apigee_116_GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRouteIn",
        "GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRouteOut": "_apigee_117_GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRouteOut",
        "GoogleCloudApigeeV1QueryTabularStatsRequestIn": "_apigee_118_GoogleCloudApigeeV1QueryTabularStatsRequestIn",
        "GoogleCloudApigeeV1QueryTabularStatsRequestOut": "_apigee_119_GoogleCloudApigeeV1QueryTabularStatsRequestOut",
        "GoogleCloudApigeeV1DatastoreConfigIn": "_apigee_120_GoogleCloudApigeeV1DatastoreConfigIn",
        "GoogleCloudApigeeV1DatastoreConfigOut": "_apigee_121_GoogleCloudApigeeV1DatastoreConfigOut",
        "GoogleCloudApigeeV1StatsIn": "_apigee_122_GoogleCloudApigeeV1StatsIn",
        "GoogleCloudApigeeV1StatsOut": "_apigee_123_GoogleCloudApigeeV1StatsOut",
        "GoogleCloudApigeeV1RoutingRuleIn": "_apigee_124_GoogleCloudApigeeV1RoutingRuleIn",
        "GoogleCloudApigeeV1RoutingRuleOut": "_apigee_125_GoogleCloudApigeeV1RoutingRuleOut",
        "GoogleCloudApigeeV1OperationIn": "_apigee_126_GoogleCloudApigeeV1OperationIn",
        "GoogleCloudApigeeV1OperationOut": "_apigee_127_GoogleCloudApigeeV1OperationOut",
        "GoogleCloudApigeeV1ListEnvironmentResourcesResponseIn": "_apigee_128_GoogleCloudApigeeV1ListEnvironmentResourcesResponseIn",
        "GoogleCloudApigeeV1ListEnvironmentResourcesResponseOut": "_apigee_129_GoogleCloudApigeeV1ListEnvironmentResourcesResponseOut",
        "GoogleLongrunningListOperationsResponseIn": "_apigee_130_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_apigee_131_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudApigeeV1ActivateNatAddressRequestIn": "_apigee_132_GoogleCloudApigeeV1ActivateNatAddressRequestIn",
        "GoogleCloudApigeeV1ActivateNatAddressRequestOut": "_apigee_133_GoogleCloudApigeeV1ActivateNatAddressRequestOut",
        "GoogleCloudApigeeV1ListDeploymentsResponseIn": "_apigee_134_GoogleCloudApigeeV1ListDeploymentsResponseIn",
        "GoogleCloudApigeeV1ListDeploymentsResponseOut": "_apigee_135_GoogleCloudApigeeV1ListDeploymentsResponseOut",
        "GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseURLInfoIn": "_apigee_136_GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseURLInfoIn",
        "GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseURLInfoOut": "_apigee_137_GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseURLInfoOut",
        "GoogleCloudApigeeV1ListAppsResponseIn": "_apigee_138_GoogleCloudApigeeV1ListAppsResponseIn",
        "GoogleCloudApigeeV1ListAppsResponseOut": "_apigee_139_GoogleCloudApigeeV1ListAppsResponseOut",
        "GoogleCloudApigeeV1TraceSamplingConfigIn": "_apigee_140_GoogleCloudApigeeV1TraceSamplingConfigIn",
        "GoogleCloudApigeeV1TraceSamplingConfigOut": "_apigee_141_GoogleCloudApigeeV1TraceSamplingConfigOut",
        "GoogleCloudApigeeV1ExportIn": "_apigee_142_GoogleCloudApigeeV1ExportIn",
        "GoogleCloudApigeeV1ExportOut": "_apigee_143_GoogleCloudApigeeV1ExportOut",
        "GoogleCloudApigeeV1AliasRevisionConfigIn": "_apigee_144_GoogleCloudApigeeV1AliasRevisionConfigIn",
        "GoogleCloudApigeeV1AliasRevisionConfigOut": "_apigee_145_GoogleCloudApigeeV1AliasRevisionConfigOut",
        "GoogleCloudApigeeV1DeploymentConfigIn": "_apigee_146_GoogleCloudApigeeV1DeploymentConfigIn",
        "GoogleCloudApigeeV1DeploymentConfigOut": "_apigee_147_GoogleCloudApigeeV1DeploymentConfigOut",
        "GoogleCloudApigeeV1KeyAliasReferenceIn": "_apigee_148_GoogleCloudApigeeV1KeyAliasReferenceIn",
        "GoogleCloudApigeeV1KeyAliasReferenceOut": "_apigee_149_GoogleCloudApigeeV1KeyAliasReferenceOut",
        "GoogleCloudApigeeV1ListExportsResponseIn": "_apigee_150_GoogleCloudApigeeV1ListExportsResponseIn",
        "GoogleCloudApigeeV1ListExportsResponseOut": "_apigee_151_GoogleCloudApigeeV1ListExportsResponseOut",
        "GoogleCloudApigeeV1SchemaIn": "_apigee_152_GoogleCloudApigeeV1SchemaIn",
        "GoogleCloudApigeeV1SchemaOut": "_apigee_153_GoogleCloudApigeeV1SchemaOut",
        "GoogleCloudApigeeV1CertificateIn": "_apigee_154_GoogleCloudApigeeV1CertificateIn",
        "GoogleCloudApigeeV1CertificateOut": "_apigee_155_GoogleCloudApigeeV1CertificateOut",
        "GoogleCloudApigeeV1DeveloperMonetizationConfigIn": "_apigee_156_GoogleCloudApigeeV1DeveloperMonetizationConfigIn",
        "GoogleCloudApigeeV1DeveloperMonetizationConfigOut": "_apigee_157_GoogleCloudApigeeV1DeveloperMonetizationConfigOut",
        "GoogleCloudApigeeV1ArchiveDeploymentIn": "_apigee_158_GoogleCloudApigeeV1ArchiveDeploymentIn",
        "GoogleCloudApigeeV1ArchiveDeploymentOut": "_apigee_159_GoogleCloudApigeeV1ArchiveDeploymentOut",
        "GoogleCloudApigeeV1MetadataIn": "_apigee_160_GoogleCloudApigeeV1MetadataIn",
        "GoogleCloudApigeeV1MetadataOut": "_apigee_161_GoogleCloudApigeeV1MetadataOut",
        "GoogleCloudApigeeV1MetricIn": "_apigee_162_GoogleCloudApigeeV1MetricIn",
        "GoogleCloudApigeeV1MetricOut": "_apigee_163_GoogleCloudApigeeV1MetricOut",
        "GoogleCloudApigeeV1InstanceDeploymentStatusIn": "_apigee_164_GoogleCloudApigeeV1InstanceDeploymentStatusIn",
        "GoogleCloudApigeeV1InstanceDeploymentStatusOut": "_apigee_165_GoogleCloudApigeeV1InstanceDeploymentStatusOut",
        "GoogleCloudApigeeV1AccessIn": "_apigee_166_GoogleCloudApigeeV1AccessIn",
        "GoogleCloudApigeeV1AccessOut": "_apigee_167_GoogleCloudApigeeV1AccessOut",
        "GoogleCloudApigeeV1CreditDeveloperBalanceRequestIn": "_apigee_168_GoogleCloudApigeeV1CreditDeveloperBalanceRequestIn",
        "GoogleCloudApigeeV1CreditDeveloperBalanceRequestOut": "_apigee_169_GoogleCloudApigeeV1CreditDeveloperBalanceRequestOut",
        "GoogleCloudApigeeV1ApiSecurityRuntimeConfigIn": "_apigee_170_GoogleCloudApigeeV1ApiSecurityRuntimeConfigIn",
        "GoogleCloudApigeeV1ApiSecurityRuntimeConfigOut": "_apigee_171_GoogleCloudApigeeV1ApiSecurityRuntimeConfigOut",
        "GoogleCloudApigeeV1ListInstancesResponseIn": "_apigee_172_GoogleCloudApigeeV1ListInstancesResponseIn",
        "GoogleCloudApigeeV1ListInstancesResponseOut": "_apigee_173_GoogleCloudApigeeV1ListInstancesResponseOut",
        "GoogleCloudApigeeV1OrganizationProjectMappingIn": "_apigee_174_GoogleCloudApigeeV1OrganizationProjectMappingIn",
        "GoogleCloudApigeeV1OrganizationProjectMappingOut": "_apigee_175_GoogleCloudApigeeV1OrganizationProjectMappingOut",
        "GoogleCloudApigeeV1TraceConfigOverrideIn": "_apigee_176_GoogleCloudApigeeV1TraceConfigOverrideIn",
        "GoogleCloudApigeeV1TraceConfigOverrideOut": "_apigee_177_GoogleCloudApigeeV1TraceConfigOverrideOut",
        "GoogleCloudApigeeV1SecurityReportResultViewIn": "_apigee_178_GoogleCloudApigeeV1SecurityReportResultViewIn",
        "GoogleCloudApigeeV1SecurityReportResultViewOut": "_apigee_179_GoogleCloudApigeeV1SecurityReportResultViewOut",
        "GoogleCloudApigeeV1GraphQLOperationIn": "_apigee_180_GoogleCloudApigeeV1GraphQLOperationIn",
        "GoogleCloudApigeeV1GraphQLOperationOut": "_apigee_181_GoogleCloudApigeeV1GraphQLOperationOut",
        "GoogleCloudApigeeV1GenerateDownloadUrlResponseIn": "_apigee_182_GoogleCloudApigeeV1GenerateDownloadUrlResponseIn",
        "GoogleCloudApigeeV1GenerateDownloadUrlResponseOut": "_apigee_183_GoogleCloudApigeeV1GenerateDownloadUrlResponseOut",
        "GoogleCloudApigeeV1AsyncQueryResultIn": "_apigee_184_GoogleCloudApigeeV1AsyncQueryResultIn",
        "GoogleCloudApigeeV1AsyncQueryResultOut": "_apigee_185_GoogleCloudApigeeV1AsyncQueryResultOut",
        "GoogleCloudApigeeV1ScoreComponentRecommendationIn": "_apigee_186_GoogleCloudApigeeV1ScoreComponentRecommendationIn",
        "GoogleCloudApigeeV1ScoreComponentRecommendationOut": "_apigee_187_GoogleCloudApigeeV1ScoreComponentRecommendationOut",
        "GoogleCloudApigeeV1ComputeEnvironmentScoresRequestIn": "_apigee_188_GoogleCloudApigeeV1ComputeEnvironmentScoresRequestIn",
        "GoogleCloudApigeeV1ComputeEnvironmentScoresRequestOut": "_apigee_189_GoogleCloudApigeeV1ComputeEnvironmentScoresRequestOut",
        "GoogleTypeIntervalIn": "_apigee_190_GoogleTypeIntervalIn",
        "GoogleTypeIntervalOut": "_apigee_191_GoogleTypeIntervalOut",
        "GoogleCloudApigeeV1DataCollectorConfigIn": "_apigee_192_GoogleCloudApigeeV1DataCollectorConfigIn",
        "GoogleCloudApigeeV1DataCollectorConfigOut": "_apigee_193_GoogleCloudApigeeV1DataCollectorConfigOut",
        "GoogleCloudApigeeV1EnvironmentIn": "_apigee_194_GoogleCloudApigeeV1EnvironmentIn",
        "GoogleCloudApigeeV1EnvironmentOut": "_apigee_195_GoogleCloudApigeeV1EnvironmentOut",
        "GoogleCloudApigeeV1ListAsyncQueriesResponseIn": "_apigee_196_GoogleCloudApigeeV1ListAsyncQueriesResponseIn",
        "GoogleCloudApigeeV1ListAsyncQueriesResponseOut": "_apigee_197_GoogleCloudApigeeV1ListAsyncQueriesResponseOut",
        "GoogleCloudApigeeV1ListSecurityReportsResponseIn": "_apigee_198_GoogleCloudApigeeV1ListSecurityReportsResponseIn",
        "GoogleCloudApigeeV1ListSecurityReportsResponseOut": "_apigee_199_GoogleCloudApigeeV1ListSecurityReportsResponseOut",
        "GoogleIamV1TestIamPermissionsRequestIn": "_apigee_200_GoogleIamV1TestIamPermissionsRequestIn",
        "GoogleIamV1TestIamPermissionsRequestOut": "_apigee_201_GoogleIamV1TestIamPermissionsRequestOut",
        "GoogleCloudApigeeV1OptimizedStatsIn": "_apigee_202_GoogleCloudApigeeV1OptimizedStatsIn",
        "GoogleCloudApigeeV1OptimizedStatsOut": "_apigee_203_GoogleCloudApigeeV1OptimizedStatsOut",
        "GoogleCloudApigeeV1DeveloperBalanceIn": "_apigee_204_GoogleCloudApigeeV1DeveloperBalanceIn",
        "GoogleCloudApigeeV1DeveloperBalanceOut": "_apigee_205_GoogleCloudApigeeV1DeveloperBalanceOut",
        "GoogleCloudApigeeV1PropertyIn": "_apigee_206_GoogleCloudApigeeV1PropertyIn",
        "GoogleCloudApigeeV1PropertyOut": "_apigee_207_GoogleCloudApigeeV1PropertyOut",
        "GoogleCloudApigeeV1PointIn": "_apigee_208_GoogleCloudApigeeV1PointIn",
        "GoogleCloudApigeeV1PointOut": "_apigee_209_GoogleCloudApigeeV1PointOut",
        "GoogleCloudApigeeV1GetSyncAuthorizationRequestIn": "_apigee_210_GoogleCloudApigeeV1GetSyncAuthorizationRequestIn",
        "GoogleCloudApigeeV1GetSyncAuthorizationRequestOut": "_apigee_211_GoogleCloudApigeeV1GetSyncAuthorizationRequestOut",
        "GoogleCloudApigeeV1AsyncQueryIn": "_apigee_212_GoogleCloudApigeeV1AsyncQueryIn",
        "GoogleCloudApigeeV1AsyncQueryOut": "_apigee_213_GoogleCloudApigeeV1AsyncQueryOut",
        "GoogleCloudApigeeV1ScoreComponentIn": "_apigee_214_GoogleCloudApigeeV1ScoreComponentIn",
        "GoogleCloudApigeeV1ScoreComponentOut": "_apigee_215_GoogleCloudApigeeV1ScoreComponentOut",
        "GoogleIamV1BindingIn": "_apigee_216_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_apigee_217_GoogleIamV1BindingOut",
        "GoogleCloudApigeeV1SecurityReportQueryIn": "_apigee_218_GoogleCloudApigeeV1SecurityReportQueryIn",
        "GoogleCloudApigeeV1SecurityReportQueryOut": "_apigee_219_GoogleCloudApigeeV1SecurityReportQueryOut",
        "GoogleCloudApigeeV1QueryTabularStatsResponseIn": "_apigee_220_GoogleCloudApigeeV1QueryTabularStatsResponseIn",
        "GoogleCloudApigeeV1QueryTabularStatsResponseOut": "_apigee_221_GoogleCloudApigeeV1QueryTabularStatsResponseOut",
        "GoogleCloudApigeeV1RuntimeConfigIn": "_apigee_222_GoogleCloudApigeeV1RuntimeConfigIn",
        "GoogleCloudApigeeV1RuntimeConfigOut": "_apigee_223_GoogleCloudApigeeV1RuntimeConfigOut",
        "GoogleCloudApigeeV1ListInstanceAttachmentsResponseIn": "_apigee_224_GoogleCloudApigeeV1ListInstanceAttachmentsResponseIn",
        "GoogleCloudApigeeV1ListInstanceAttachmentsResponseOut": "_apigee_225_GoogleCloudApigeeV1ListInstanceAttachmentsResponseOut",
        "GoogleCloudApigeeV1EnvironmentGroupIn": "_apigee_226_GoogleCloudApigeeV1EnvironmentGroupIn",
        "GoogleCloudApigeeV1EnvironmentGroupOut": "_apigee_227_GoogleCloudApigeeV1EnvironmentGroupOut",
        "GoogleCloudApigeeV1InstanceIn": "_apigee_228_GoogleCloudApigeeV1InstanceIn",
        "GoogleCloudApigeeV1InstanceOut": "_apigee_229_GoogleCloudApigeeV1InstanceOut",
        "GoogleCloudApigeeV1AsyncQueryResultViewIn": "_apigee_230_GoogleCloudApigeeV1AsyncQueryResultViewIn",
        "GoogleCloudApigeeV1AsyncQueryResultViewOut": "_apigee_231_GoogleCloudApigeeV1AsyncQueryResultViewOut",
        "GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentIn": "_apigee_232_GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentIn",
        "GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentOut": "_apigee_233_GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentOut",
        "GoogleCloudApigeeV1NatAddressIn": "_apigee_234_GoogleCloudApigeeV1NatAddressIn",
        "GoogleCloudApigeeV1NatAddressOut": "_apigee_235_GoogleCloudApigeeV1NatAddressOut",
        "GoogleCloudApigeeV1ExpireDeveloperSubscriptionRequestIn": "_apigee_236_GoogleCloudApigeeV1ExpireDeveloperSubscriptionRequestIn",
        "GoogleCloudApigeeV1ExpireDeveloperSubscriptionRequestOut": "_apigee_237_GoogleCloudApigeeV1ExpireDeveloperSubscriptionRequestOut",
        "GoogleCloudApigeeV1ConnectorsPlatformConfigIn": "_apigee_238_GoogleCloudApigeeV1ConnectorsPlatformConfigIn",
        "GoogleCloudApigeeV1ConnectorsPlatformConfigOut": "_apigee_239_GoogleCloudApigeeV1ConnectorsPlatformConfigOut",
        "GoogleCloudApigeeV1CanaryEvaluationMetricLabelsIn": "_apigee_240_GoogleCloudApigeeV1CanaryEvaluationMetricLabelsIn",
        "GoogleCloudApigeeV1CanaryEvaluationMetricLabelsOut": "_apigee_241_GoogleCloudApigeeV1CanaryEvaluationMetricLabelsOut",
        "GoogleCloudApigeeV1EnvironmentGroupConfigIn": "_apigee_242_GoogleCloudApigeeV1EnvironmentGroupConfigIn",
        "GoogleCloudApigeeV1EnvironmentGroupConfigOut": "_apigee_243_GoogleCloudApigeeV1EnvironmentGroupConfigOut",
        "GoogleCloudApigeeV1RateRangeIn": "_apigee_244_GoogleCloudApigeeV1RateRangeIn",
        "GoogleCloudApigeeV1RateRangeOut": "_apigee_245_GoogleCloudApigeeV1RateRangeOut",
        "GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseIn": "_apigee_246_GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseIn",
        "GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseOut": "_apigee_247_GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseOut",
        "GoogleCloudApigeeV1OptimizedStatsNodeIn": "_apigee_248_GoogleCloudApigeeV1OptimizedStatsNodeIn",
        "GoogleCloudApigeeV1OptimizedStatsNodeOut": "_apigee_249_GoogleCloudApigeeV1OptimizedStatsNodeOut",
        "GoogleCloudApigeeV1StatsHostStatsIn": "_apigee_250_GoogleCloudApigeeV1StatsHostStatsIn",
        "GoogleCloudApigeeV1StatsHostStatsOut": "_apigee_251_GoogleCloudApigeeV1StatsHostStatsOut",
        "GoogleCloudApigeeV1GraphQLOperationGroupIn": "_apigee_252_GoogleCloudApigeeV1GraphQLOperationGroupIn",
        "GoogleCloudApigeeV1GraphQLOperationGroupOut": "_apigee_253_GoogleCloudApigeeV1GraphQLOperationGroupOut",
        "GoogleCloudApigeeV1ScoreComponentRecommendationActionActionContextIn": "_apigee_254_GoogleCloudApigeeV1ScoreComponentRecommendationActionActionContextIn",
        "GoogleCloudApigeeV1ScoreComponentRecommendationActionActionContextOut": "_apigee_255_GoogleCloudApigeeV1ScoreComponentRecommendationActionActionContextOut",
        "GoogleCloudApigeeV1EnvironmentGroupAttachmentIn": "_apigee_256_GoogleCloudApigeeV1EnvironmentGroupAttachmentIn",
        "GoogleCloudApigeeV1EnvironmentGroupAttachmentOut": "_apigee_257_GoogleCloudApigeeV1EnvironmentGroupAttachmentOut",
        "GoogleCloudApigeeV1ListOfDevelopersResponseIn": "_apigee_258_GoogleCloudApigeeV1ListOfDevelopersResponseIn",
        "GoogleCloudApigeeV1ListOfDevelopersResponseOut": "_apigee_259_GoogleCloudApigeeV1ListOfDevelopersResponseOut",
        "GoogleCloudApigeeV1StatsEnvironmentStatsIn": "_apigee_260_GoogleCloudApigeeV1StatsEnvironmentStatsIn",
        "GoogleCloudApigeeV1StatsEnvironmentStatsOut": "_apigee_261_GoogleCloudApigeeV1StatsEnvironmentStatsOut",
        "GoogleCloudApigeeV1PodStatusIn": "_apigee_262_GoogleCloudApigeeV1PodStatusIn",
        "GoogleCloudApigeeV1PodStatusOut": "_apigee_263_GoogleCloudApigeeV1PodStatusOut",
        "GoogleCloudApigeeV1TlsInfoIn": "_apigee_264_GoogleCloudApigeeV1TlsInfoIn",
        "GoogleCloudApigeeV1TlsInfoOut": "_apigee_265_GoogleCloudApigeeV1TlsInfoOut",
        "GoogleCloudApigeeV1ListHybridIssuersResponseIn": "_apigee_266_GoogleCloudApigeeV1ListHybridIssuersResponseIn",
        "GoogleCloudApigeeV1ListHybridIssuersResponseOut": "_apigee_267_GoogleCloudApigeeV1ListHybridIssuersResponseOut",
        "GoogleCloudApigeeV1FlowHookConfigIn": "_apigee_268_GoogleCloudApigeeV1FlowHookConfigIn",
        "GoogleCloudApigeeV1FlowHookConfigOut": "_apigee_269_GoogleCloudApigeeV1FlowHookConfigOut",
        "GoogleCloudApigeeV1DeploymentChangeReportIn": "_apigee_270_GoogleCloudApigeeV1DeploymentChangeReportIn",
        "GoogleCloudApigeeV1DeploymentChangeReportOut": "_apigee_271_GoogleCloudApigeeV1DeploymentChangeReportOut",
        "GoogleCloudApigeeV1OptimizedStatsResponseIn": "_apigee_272_GoogleCloudApigeeV1OptimizedStatsResponseIn",
        "GoogleCloudApigeeV1OptimizedStatsResponseOut": "_apigee_273_GoogleCloudApigeeV1OptimizedStatsResponseOut",
        "GoogleCloudApigeeV1SecurityReportMetadataIn": "_apigee_274_GoogleCloudApigeeV1SecurityReportMetadataIn",
        "GoogleCloudApigeeV1SecurityReportMetadataOut": "_apigee_275_GoogleCloudApigeeV1SecurityReportMetadataOut",
        "GoogleCloudApigeeV1OperationMetadataIn": "_apigee_276_GoogleCloudApigeeV1OperationMetadataIn",
        "GoogleCloudApigeeV1OperationMetadataOut": "_apigee_277_GoogleCloudApigeeV1OperationMetadataOut",
        "GoogleCloudApigeeV1TlsInfoConfigIn": "_apigee_278_GoogleCloudApigeeV1TlsInfoConfigIn",
        "GoogleCloudApigeeV1TlsInfoConfigOut": "_apigee_279_GoogleCloudApigeeV1TlsInfoConfigOut",
        "GoogleCloudApigeeV1OperationGroupIn": "_apigee_280_GoogleCloudApigeeV1OperationGroupIn",
        "GoogleCloudApigeeV1OperationGroupOut": "_apigee_281_GoogleCloudApigeeV1OperationGroupOut",
        "GoogleCloudApigeeV1SecurityProfileEnvironmentIn": "_apigee_282_GoogleCloudApigeeV1SecurityProfileEnvironmentIn",
        "GoogleCloudApigeeV1SecurityProfileEnvironmentOut": "_apigee_283_GoogleCloudApigeeV1SecurityProfileEnvironmentOut",
        "GoogleCloudApigeeV1ReportInstanceStatusResponseIn": "_apigee_284_GoogleCloudApigeeV1ReportInstanceStatusResponseIn",
        "GoogleCloudApigeeV1ReportInstanceStatusResponseOut": "_apigee_285_GoogleCloudApigeeV1ReportInstanceStatusResponseOut",
        "GoogleCloudApigeeV1AccessSetIn": "_apigee_286_GoogleCloudApigeeV1AccessSetIn",
        "GoogleCloudApigeeV1AccessSetOut": "_apigee_287_GoogleCloudApigeeV1AccessSetOut",
        "GoogleApiHttpBodyIn": "_apigee_288_GoogleApiHttpBodyIn",
        "GoogleApiHttpBodyOut": "_apigee_289_GoogleApiHttpBodyOut",
        "GoogleCloudApigeeV1ListDataCollectorsResponseIn": "_apigee_290_GoogleCloudApigeeV1ListDataCollectorsResponseIn",
        "GoogleCloudApigeeV1ListDataCollectorsResponseOut": "_apigee_291_GoogleCloudApigeeV1ListDataCollectorsResponseOut",
        "GoogleCloudApigeeV1SchemaSchemaElementIn": "_apigee_292_GoogleCloudApigeeV1SchemaSchemaElementIn",
        "GoogleCloudApigeeV1SchemaSchemaElementOut": "_apigee_293_GoogleCloudApigeeV1SchemaSchemaElementOut",
        "GoogleCloudApigeeV1GenerateDownloadUrlRequestIn": "_apigee_294_GoogleCloudApigeeV1GenerateDownloadUrlRequestIn",
        "GoogleCloudApigeeV1GenerateDownloadUrlRequestOut": "_apigee_295_GoogleCloudApigeeV1GenerateDownloadUrlRequestOut",
        "GoogleCloudApigeeV1ListArchiveDeploymentsResponseIn": "_apigee_296_GoogleCloudApigeeV1ListArchiveDeploymentsResponseIn",
        "GoogleCloudApigeeV1ListArchiveDeploymentsResponseOut": "_apigee_297_GoogleCloudApigeeV1ListArchiveDeploymentsResponseOut",
        "GoogleCloudApigeeV1GenerateUploadUrlResponseIn": "_apigee_298_GoogleCloudApigeeV1GenerateUploadUrlResponseIn",
        "GoogleCloudApigeeV1GenerateUploadUrlResponseOut": "_apigee_299_GoogleCloudApigeeV1GenerateUploadUrlResponseOut",
        "GoogleCloudApigeeV1ConfigVersionIn": "_apigee_300_GoogleCloudApigeeV1ConfigVersionIn",
        "GoogleCloudApigeeV1ConfigVersionOut": "_apigee_301_GoogleCloudApigeeV1ConfigVersionOut",
        "GoogleIamV1PolicyIn": "_apigee_302_GoogleIamV1PolicyIn",
        "GoogleIamV1PolicyOut": "_apigee_303_GoogleIamV1PolicyOut",
        "GoogleCloudApigeeV1ApiProxyIn": "_apigee_304_GoogleCloudApigeeV1ApiProxyIn",
        "GoogleCloudApigeeV1ApiProxyOut": "_apigee_305_GoogleCloudApigeeV1ApiProxyOut",
        "GoogleCloudApigeeV1ListSecurityProfilesResponseIn": "_apigee_306_GoogleCloudApigeeV1ListSecurityProfilesResponseIn",
        "GoogleCloudApigeeV1ListSecurityProfilesResponseOut": "_apigee_307_GoogleCloudApigeeV1ListSecurityProfilesResponseOut",
        "GoogleCloudApigeeV1AliasIn": "_apigee_308_GoogleCloudApigeeV1AliasIn",
        "GoogleCloudApigeeV1AliasOut": "_apigee_309_GoogleCloudApigeeV1AliasOut",
        "GoogleCloudApigeeV1AppIn": "_apigee_310_GoogleCloudApigeeV1AppIn",
        "GoogleCloudApigeeV1AppOut": "_apigee_311_GoogleCloudApigeeV1AppOut",
        "GoogleCloudApigeeV1ScoreIn": "_apigee_312_GoogleCloudApigeeV1ScoreIn",
        "GoogleCloudApigeeV1ScoreOut": "_apigee_313_GoogleCloudApigeeV1ScoreOut",
        "GoogleCloudApigeeV1DeploymentChangeReportRoutingChangeIn": "_apigee_314_GoogleCloudApigeeV1DeploymentChangeReportRoutingChangeIn",
        "GoogleCloudApigeeV1DeploymentChangeReportRoutingChangeOut": "_apigee_315_GoogleCloudApigeeV1DeploymentChangeReportRoutingChangeOut",
        "GoogleCloudApigeeV1SchemaSchemaPropertyIn": "_apigee_316_GoogleCloudApigeeV1SchemaSchemaPropertyIn",
        "GoogleCloudApigeeV1SchemaSchemaPropertyOut": "_apigee_317_GoogleCloudApigeeV1SchemaSchemaPropertyOut",
        "GoogleCloudApigeeV1SecurityProfileIn": "_apigee_318_GoogleCloudApigeeV1SecurityProfileIn",
        "GoogleCloudApigeeV1SecurityProfileOut": "_apigee_319_GoogleCloudApigeeV1SecurityProfileOut",
        "GoogleCloudApigeeV1MetricAggregationIn": "_apigee_320_GoogleCloudApigeeV1MetricAggregationIn",
        "GoogleCloudApigeeV1MetricAggregationOut": "_apigee_321_GoogleCloudApigeeV1MetricAggregationOut",
        "GoogleCloudApigeeV1DeleteCustomReportResponseIn": "_apigee_322_GoogleCloudApigeeV1DeleteCustomReportResponseIn",
        "GoogleCloudApigeeV1DeleteCustomReportResponseOut": "_apigee_323_GoogleCloudApigeeV1DeleteCustomReportResponseOut",
        "GoogleCloudApigeeV1ListTraceConfigOverridesResponseIn": "_apigee_324_GoogleCloudApigeeV1ListTraceConfigOverridesResponseIn",
        "GoogleCloudApigeeV1ListTraceConfigOverridesResponseOut": "_apigee_325_GoogleCloudApigeeV1ListTraceConfigOverridesResponseOut",
        "GoogleCloudApigeeV1QueryIn": "_apigee_326_GoogleCloudApigeeV1QueryIn",
        "GoogleCloudApigeeV1QueryOut": "_apigee_327_GoogleCloudApigeeV1QueryOut",
        "GoogleCloudApigeeV1CommonNameConfigIn": "_apigee_328_GoogleCloudApigeeV1CommonNameConfigIn",
        "GoogleCloudApigeeV1CommonNameConfigOut": "_apigee_329_GoogleCloudApigeeV1CommonNameConfigOut",
        "GoogleIamV1SetIamPolicyRequestIn": "_apigee_330_GoogleIamV1SetIamPolicyRequestIn",
        "GoogleIamV1SetIamPolicyRequestOut": "_apigee_331_GoogleIamV1SetIamPolicyRequestOut",
        "GoogleCloudApigeeV1CanaryEvaluationIn": "_apigee_332_GoogleCloudApigeeV1CanaryEvaluationIn",
        "GoogleCloudApigeeV1CanaryEvaluationOut": "_apigee_333_GoogleCloudApigeeV1CanaryEvaluationOut",
        "GoogleCloudApigeeV1DeveloperAppKeyIn": "_apigee_334_GoogleCloudApigeeV1DeveloperAppKeyIn",
        "GoogleCloudApigeeV1DeveloperAppKeyOut": "_apigee_335_GoogleCloudApigeeV1DeveloperAppKeyOut",
        "GoogleCloudApigeeV1DimensionMetricIn": "_apigee_336_GoogleCloudApigeeV1DimensionMetricIn",
        "GoogleCloudApigeeV1DimensionMetricOut": "_apigee_337_GoogleCloudApigeeV1DimensionMetricOut",
        "GoogleCloudApigeeV1AdvancedApiOpsConfigIn": "_apigee_338_GoogleCloudApigeeV1AdvancedApiOpsConfigIn",
        "GoogleCloudApigeeV1AdvancedApiOpsConfigOut": "_apigee_339_GoogleCloudApigeeV1AdvancedApiOpsConfigOut",
        "GoogleCloudApigeeV1QueryMetadataIn": "_apigee_340_GoogleCloudApigeeV1QueryMetadataIn",
        "GoogleCloudApigeeV1QueryMetadataOut": "_apigee_341_GoogleCloudApigeeV1QueryMetadataOut",
        "GoogleCloudApigeeV1EndpointAttachmentIn": "_apigee_342_GoogleCloudApigeeV1EndpointAttachmentIn",
        "GoogleCloudApigeeV1EndpointAttachmentOut": "_apigee_343_GoogleCloudApigeeV1EndpointAttachmentOut",
        "GoogleCloudApigeeV1TargetServerConfigIn": "_apigee_344_GoogleCloudApigeeV1TargetServerConfigIn",
        "GoogleCloudApigeeV1TargetServerConfigOut": "_apigee_345_GoogleCloudApigeeV1TargetServerConfigOut",
        "GoogleRpcStatusIn": "_apigee_346_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_apigee_347_GoogleRpcStatusOut",
        "GoogleCloudApigeeV1SecurityReportQueryMetricIn": "_apigee_348_GoogleCloudApigeeV1SecurityReportQueryMetricIn",
        "GoogleCloudApigeeV1SecurityReportQueryMetricOut": "_apigee_349_GoogleCloudApigeeV1SecurityReportQueryMetricOut",
        "GoogleCloudApigeeV1RevisionStatusIn": "_apigee_350_GoogleCloudApigeeV1RevisionStatusIn",
        "GoogleCloudApigeeV1RevisionStatusOut": "_apigee_351_GoogleCloudApigeeV1RevisionStatusOut",
        "GoogleCloudApigeeV1ReportInstanceStatusRequestIn": "_apigee_352_GoogleCloudApigeeV1ReportInstanceStatusRequestIn",
        "GoogleCloudApigeeV1ReportInstanceStatusRequestOut": "_apigee_353_GoogleCloudApigeeV1ReportInstanceStatusRequestOut",
        "GoogleCloudApigeeV1ScoreComponentRecommendationActionIn": "_apigee_354_GoogleCloudApigeeV1ScoreComponentRecommendationActionIn",
        "GoogleCloudApigeeV1ScoreComponentRecommendationActionOut": "_apigee_355_GoogleCloudApigeeV1ScoreComponentRecommendationActionOut",
        "GoogleCloudApigeeV1SubscriptionIn": "_apigee_356_GoogleCloudApigeeV1SubscriptionIn",
        "GoogleCloudApigeeV1SubscriptionOut": "_apigee_357_GoogleCloudApigeeV1SubscriptionOut",
        "GoogleCloudApigeeV1FlowHookIn": "_apigee_358_GoogleCloudApigeeV1FlowHookIn",
        "GoogleCloudApigeeV1FlowHookOut": "_apigee_359_GoogleCloudApigeeV1FlowHookOut",
        "GoogleCloudApigeeV1ListSecurityProfileRevisionsResponseIn": "_apigee_360_GoogleCloudApigeeV1ListSecurityProfileRevisionsResponseIn",
        "GoogleCloudApigeeV1ListSecurityProfileRevisionsResponseOut": "_apigee_361_GoogleCloudApigeeV1ListSecurityProfileRevisionsResponseOut",
        "GoogleCloudApigeeV1ProvisionOrganizationRequestIn": "_apigee_362_GoogleCloudApigeeV1ProvisionOrganizationRequestIn",
        "GoogleCloudApigeeV1ProvisionOrganizationRequestOut": "_apigee_363_GoogleCloudApigeeV1ProvisionOrganizationRequestOut",
        "GoogleCloudApigeeV1SetAddonsRequestIn": "_apigee_364_GoogleCloudApigeeV1SetAddonsRequestIn",
        "GoogleCloudApigeeV1SetAddonsRequestOut": "_apigee_365_GoogleCloudApigeeV1SetAddonsRequestOut",
        "GoogleCloudApigeeV1ListDatastoresResponseIn": "_apigee_366_GoogleCloudApigeeV1ListDatastoresResponseIn",
        "GoogleCloudApigeeV1ListDatastoresResponseOut": "_apigee_367_GoogleCloudApigeeV1ListDatastoresResponseOut",
        "GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilterIn": "_apigee_368_GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilterIn",
        "GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilterOut": "_apigee_369_GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilterOut",
        "GoogleCloudApigeeV1RuntimeTraceConfigIn": "_apigee_370_GoogleCloudApigeeV1RuntimeTraceConfigIn",
        "GoogleCloudApigeeV1RuntimeTraceConfigOut": "_apigee_371_GoogleCloudApigeeV1RuntimeTraceConfigOut",
        "GoogleCloudApigeeV1AccessRemoveIn": "_apigee_372_GoogleCloudApigeeV1AccessRemoveIn",
        "GoogleCloudApigeeV1AccessRemoveOut": "_apigee_373_GoogleCloudApigeeV1AccessRemoveOut",
        "GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponseIn": "_apigee_374_GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponseIn",
        "GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponseOut": "_apigee_375_GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponseOut",
        "GoogleCloudApigeeV1RuntimeTraceConfigOverrideIn": "_apigee_376_GoogleCloudApigeeV1RuntimeTraceConfigOverrideIn",
        "GoogleCloudApigeeV1RuntimeTraceConfigOverrideOut": "_apigee_377_GoogleCloudApigeeV1RuntimeTraceConfigOverrideOut",
        "GoogleCloudApigeeV1QuotaIn": "_apigee_378_GoogleCloudApigeeV1QuotaIn",
        "GoogleCloudApigeeV1QuotaOut": "_apigee_379_GoogleCloudApigeeV1QuotaOut",
        "GoogleCloudApigeeV1SecurityProfileEnvironmentAssociationIn": "_apigee_380_GoogleCloudApigeeV1SecurityProfileEnvironmentAssociationIn",
        "GoogleCloudApigeeV1SecurityProfileEnvironmentAssociationOut": "_apigee_381_GoogleCloudApigeeV1SecurityProfileEnvironmentAssociationOut",
        "GoogleCloudApigeeV1AppGroupIn": "_apigee_382_GoogleCloudApigeeV1AppGroupIn",
        "GoogleCloudApigeeV1AppGroupOut": "_apigee_383_GoogleCloudApigeeV1AppGroupOut",
        "GoogleCloudApigeeV1SecurityIncidentIn": "_apigee_384_GoogleCloudApigeeV1SecurityIncidentIn",
        "GoogleCloudApigeeV1SecurityIncidentOut": "_apigee_385_GoogleCloudApigeeV1SecurityIncidentOut",
        "GoogleCloudApigeeV1RevenueShareRangeIn": "_apigee_386_GoogleCloudApigeeV1RevenueShareRangeIn",
        "GoogleCloudApigeeV1RevenueShareRangeOut": "_apigee_387_GoogleCloudApigeeV1RevenueShareRangeOut",
        "GoogleCloudApigeeV1APIProductAssociationIn": "_apigee_388_GoogleCloudApigeeV1APIProductAssociationIn",
        "GoogleCloudApigeeV1APIProductAssociationOut": "_apigee_389_GoogleCloudApigeeV1APIProductAssociationOut",
        "GoogleCloudApigeeV1QueryTimeSeriesStatsRequestIn": "_apigee_390_GoogleCloudApigeeV1QueryTimeSeriesStatsRequestIn",
        "GoogleCloudApigeeV1QueryTimeSeriesStatsRequestOut": "_apigee_391_GoogleCloudApigeeV1QueryTimeSeriesStatsRequestOut",
        "GoogleCloudApigeeV1ComputeEnvironmentScoresResponseIn": "_apigee_392_GoogleCloudApigeeV1ComputeEnvironmentScoresResponseIn",
        "GoogleCloudApigeeV1ComputeEnvironmentScoresResponseOut": "_apigee_393_GoogleCloudApigeeV1ComputeEnvironmentScoresResponseOut",
        "GoogleProtobufEmptyIn": "_apigee_394_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_apigee_395_GoogleProtobufEmptyOut",
        "GoogleCloudApigeeV1AttributeIn": "_apigee_396_GoogleCloudApigeeV1AttributeIn",
        "GoogleCloudApigeeV1AttributeOut": "_apigee_397_GoogleCloudApigeeV1AttributeOut",
        "GoogleCloudApigeeV1ApiSecurityConfigIn": "_apigee_398_GoogleCloudApigeeV1ApiSecurityConfigIn",
        "GoogleCloudApigeeV1ApiSecurityConfigOut": "_apigee_399_GoogleCloudApigeeV1ApiSecurityConfigOut",
        "GoogleCloudApigeeV1ResourceFileIn": "_apigee_400_GoogleCloudApigeeV1ResourceFileIn",
        "GoogleCloudApigeeV1ResourceFileOut": "_apigee_401_GoogleCloudApigeeV1ResourceFileOut",
        "GoogleCloudApigeeV1ListAppGroupsResponseIn": "_apigee_402_GoogleCloudApigeeV1ListAppGroupsResponseIn",
        "GoogleCloudApigeeV1ListAppGroupsResponseOut": "_apigee_403_GoogleCloudApigeeV1ListAppGroupsResponseOut",
        "GoogleCloudApigeeV1KeyValueEntryIn": "_apigee_404_GoogleCloudApigeeV1KeyValueEntryIn",
        "GoogleCloudApigeeV1KeyValueEntryOut": "_apigee_405_GoogleCloudApigeeV1KeyValueEntryOut",
        "GoogleCloudApigeeV1ReferenceIn": "_apigee_406_GoogleCloudApigeeV1ReferenceIn",
        "GoogleCloudApigeeV1ReferenceOut": "_apigee_407_GoogleCloudApigeeV1ReferenceOut",
        "GoogleCloudApigeeV1AdjustDeveloperBalanceRequestIn": "_apigee_408_GoogleCloudApigeeV1AdjustDeveloperBalanceRequestIn",
        "GoogleCloudApigeeV1AdjustDeveloperBalanceRequestOut": "_apigee_409_GoogleCloudApigeeV1AdjustDeveloperBalanceRequestOut",
        "GoogleCloudApigeeV1ApiProductRefIn": "_apigee_410_GoogleCloudApigeeV1ApiProductRefIn",
        "GoogleCloudApigeeV1ApiProductRefOut": "_apigee_411_GoogleCloudApigeeV1ApiProductRefOut",
        "GoogleIamV1AuditLogConfigIn": "_apigee_412_GoogleIamV1AuditLogConfigIn",
        "GoogleIamV1AuditLogConfigOut": "_apigee_413_GoogleIamV1AuditLogConfigOut",
        "GoogleCloudApigeeV1NodeConfigIn": "_apigee_414_GoogleCloudApigeeV1NodeConfigIn",
        "GoogleCloudApigeeV1NodeConfigOut": "_apigee_415_GoogleCloudApigeeV1NodeConfigOut",
        "GoogleCloudApigeeV1DatastoreIn": "_apigee_416_GoogleCloudApigeeV1DatastoreIn",
        "GoogleCloudApigeeV1DatastoreOut": "_apigee_417_GoogleCloudApigeeV1DatastoreOut",
        "GoogleCloudApigeeV1OrganizationIn": "_apigee_418_GoogleCloudApigeeV1OrganizationIn",
        "GoogleCloudApigeeV1OrganizationOut": "_apigee_419_GoogleCloudApigeeV1OrganizationOut",
        "GoogleTypeExprIn": "_apigee_420_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_apigee_421_GoogleTypeExprOut",
        "GoogleCloudApigeeV1QueryMetricIn": "_apigee_422_GoogleCloudApigeeV1QueryMetricIn",
        "GoogleCloudApigeeV1QueryMetricOut": "_apigee_423_GoogleCloudApigeeV1QueryMetricOut",
        "GoogleCloudApigeeV1ListApiProxiesResponseIn": "_apigee_424_GoogleCloudApigeeV1ListApiProxiesResponseIn",
        "GoogleCloudApigeeV1ListApiProxiesResponseOut": "_apigee_425_GoogleCloudApigeeV1ListApiProxiesResponseOut",
        "GoogleCloudApigeeV1UpdateAppGroupAppKeyRequestIn": "_apigee_426_GoogleCloudApigeeV1UpdateAppGroupAppKeyRequestIn",
        "GoogleCloudApigeeV1UpdateAppGroupAppKeyRequestOut": "_apigee_427_GoogleCloudApigeeV1UpdateAppGroupAppKeyRequestOut",
        "GoogleCloudApigeeV1KeystoreConfigIn": "_apigee_428_GoogleCloudApigeeV1KeystoreConfigIn",
        "GoogleCloudApigeeV1KeystoreConfigOut": "_apigee_429_GoogleCloudApigeeV1KeystoreConfigOut",
        "GoogleCloudApigeeV1CustomReportMetricIn": "_apigee_430_GoogleCloudApigeeV1CustomReportMetricIn",
        "GoogleCloudApigeeV1CustomReportMetricOut": "_apigee_431_GoogleCloudApigeeV1CustomReportMetricOut",
        "GoogleCloudApigeeV1DeploymentGroupConfigIn": "_apigee_432_GoogleCloudApigeeV1DeploymentGroupConfigIn",
        "GoogleCloudApigeeV1DeploymentGroupConfigOut": "_apigee_433_GoogleCloudApigeeV1DeploymentGroupConfigOut",
        "GoogleCloudApigeeV1IntegrationConfigIn": "_apigee_434_GoogleCloudApigeeV1IntegrationConfigIn",
        "GoogleCloudApigeeV1IntegrationConfigOut": "_apigee_435_GoogleCloudApigeeV1IntegrationConfigOut",
        "GoogleCloudApigeeV1DeveloperIn": "_apigee_436_GoogleCloudApigeeV1DeveloperIn",
        "GoogleCloudApigeeV1DeveloperOut": "_apigee_437_GoogleCloudApigeeV1DeveloperOut",
        "GoogleCloudApigeeV1ServiceIssuersMappingIn": "_apigee_438_GoogleCloudApigeeV1ServiceIssuersMappingIn",
        "GoogleCloudApigeeV1ServiceIssuersMappingOut": "_apigee_439_GoogleCloudApigeeV1ServiceIssuersMappingOut",
        "GoogleCloudApigeeV1ApiCategoryIn": "_apigee_440_GoogleCloudApigeeV1ApiCategoryIn",
        "GoogleCloudApigeeV1ApiCategoryOut": "_apigee_441_GoogleCloudApigeeV1ApiCategoryOut",
        "GoogleCloudApigeeV1ResourceConfigIn": "_apigee_442_GoogleCloudApigeeV1ResourceConfigIn",
        "GoogleCloudApigeeV1ResourceConfigOut": "_apigee_443_GoogleCloudApigeeV1ResourceConfigOut",
        "GoogleCloudApigeeV1ListOrganizationsResponseIn": "_apigee_444_GoogleCloudApigeeV1ListOrganizationsResponseIn",
        "GoogleCloudApigeeV1ListOrganizationsResponseOut": "_apigee_445_GoogleCloudApigeeV1ListOrganizationsResponseOut",
        "EdgeConfigstoreBundleBadBundleIn": "_apigee_446_EdgeConfigstoreBundleBadBundleIn",
        "EdgeConfigstoreBundleBadBundleOut": "_apigee_447_EdgeConfigstoreBundleBadBundleOut",
        "GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRevisionIn": "_apigee_448_GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRevisionIn",
        "GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRevisionOut": "_apigee_449_GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRevisionOut",
        "GoogleCloudApigeeV1ListAppGroupAppsResponseIn": "_apigee_450_GoogleCloudApigeeV1ListAppGroupAppsResponseIn",
        "GoogleCloudApigeeV1ListAppGroupAppsResponseOut": "_apigee_451_GoogleCloudApigeeV1ListAppGroupAppsResponseOut",
        "GoogleCloudApigeeV1ListApiProductsResponseIn": "_apigee_452_GoogleCloudApigeeV1ListApiProductsResponseIn",
        "GoogleCloudApigeeV1ListApiProductsResponseOut": "_apigee_453_GoogleCloudApigeeV1ListApiProductsResponseOut",
        "GoogleCloudApigeeV1IngressConfigIn": "_apigee_454_GoogleCloudApigeeV1IngressConfigIn",
        "GoogleCloudApigeeV1IngressConfigOut": "_apigee_455_GoogleCloudApigeeV1IngressConfigOut",
        "GoogleCloudApigeeV1ReferenceConfigIn": "_apigee_456_GoogleCloudApigeeV1ReferenceConfigIn",
        "GoogleCloudApigeeV1ReferenceConfigOut": "_apigee_457_GoogleCloudApigeeV1ReferenceConfigOut",
        "GoogleCloudApigeeV1ExportRequestIn": "_apigee_458_GoogleCloudApigeeV1ExportRequestIn",
        "GoogleCloudApigeeV1ExportRequestOut": "_apigee_459_GoogleCloudApigeeV1ExportRequestOut",
        "EdgeConfigstoreBundleBadBundleViolationIn": "_apigee_460_EdgeConfigstoreBundleBadBundleViolationIn",
        "EdgeConfigstoreBundleBadBundleViolationOut": "_apigee_461_EdgeConfigstoreBundleBadBundleViolationOut",
        "GoogleCloudApigeeV1ListDeveloperAppsResponseIn": "_apigee_462_GoogleCloudApigeeV1ListDeveloperAppsResponseIn",
        "GoogleCloudApigeeV1ListDeveloperAppsResponseOut": "_apigee_463_GoogleCloudApigeeV1ListDeveloperAppsResponseOut",
        "GoogleCloudApigeeV1OperationConfigIn": "_apigee_464_GoogleCloudApigeeV1OperationConfigIn",
        "GoogleCloudApigeeV1OperationConfigOut": "_apigee_465_GoogleCloudApigeeV1OperationConfigOut",
        "GoogleCloudApigeeV1DateRangeIn": "_apigee_466_GoogleCloudApigeeV1DateRangeIn",
        "GoogleCloudApigeeV1DateRangeOut": "_apigee_467_GoogleCloudApigeeV1DateRangeOut",
        "GoogleCloudApigeeV1DeveloperAppIn": "_apigee_468_GoogleCloudApigeeV1DeveloperAppIn",
        "GoogleCloudApigeeV1DeveloperAppOut": "_apigee_469_GoogleCloudApigeeV1DeveloperAppOut",
        "GoogleCloudApigeeV1AccessGetIn": "_apigee_470_GoogleCloudApigeeV1AccessGetIn",
        "GoogleCloudApigeeV1AccessGetOut": "_apigee_471_GoogleCloudApigeeV1AccessGetOut",
        "GoogleCloudApigeeV1DeploymentChangeReportRoutingConflictIn": "_apigee_472_GoogleCloudApigeeV1DeploymentChangeReportRoutingConflictIn",
        "GoogleCloudApigeeV1DeploymentChangeReportRoutingConflictOut": "_apigee_473_GoogleCloudApigeeV1DeploymentChangeReportRoutingConflictOut",
        "GoogleCloudApigeeV1DebugSessionIn": "_apigee_474_GoogleCloudApigeeV1DebugSessionIn",
        "GoogleCloudApigeeV1DebugSessionOut": "_apigee_475_GoogleCloudApigeeV1DebugSessionOut",
        "GoogleCloudApigeeV1ListDebugSessionsResponseIn": "_apigee_476_GoogleCloudApigeeV1ListDebugSessionsResponseIn",
        "GoogleCloudApigeeV1ListDebugSessionsResponseOut": "_apigee_477_GoogleCloudApigeeV1ListDebugSessionsResponseOut",
        "GoogleCloudApigeeV1AttributesIn": "_apigee_478_GoogleCloudApigeeV1AttributesIn",
        "GoogleCloudApigeeV1AttributesOut": "_apigee_479_GoogleCloudApigeeV1AttributesOut",
        "GoogleCloudApigeeV1RuntimeTraceSamplingConfigIn": "_apigee_480_GoogleCloudApigeeV1RuntimeTraceSamplingConfigIn",
        "GoogleCloudApigeeV1RuntimeTraceSamplingConfigOut": "_apigee_481_GoogleCloudApigeeV1RuntimeTraceSamplingConfigOut",
        "GoogleCloudApigeeV1DeploymentIn": "_apigee_482_GoogleCloudApigeeV1DeploymentIn",
        "GoogleCloudApigeeV1DeploymentOut": "_apigee_483_GoogleCloudApigeeV1DeploymentOut",
        "GoogleCloudApigeeV1ListRatePlansResponseIn": "_apigee_484_GoogleCloudApigeeV1ListRatePlansResponseIn",
        "GoogleCloudApigeeV1ListRatePlansResponseOut": "_apigee_485_GoogleCloudApigeeV1ListRatePlansResponseOut",
        "GoogleCloudApigeeV1ApiCategoryDataIn": "_apigee_486_GoogleCloudApigeeV1ApiCategoryDataIn",
        "GoogleCloudApigeeV1ApiCategoryDataOut": "_apigee_487_GoogleCloudApigeeV1ApiCategoryDataOut",
        "GoogleCloudApigeeV1DebugMaskIn": "_apigee_488_GoogleCloudApigeeV1DebugMaskIn",
        "GoogleCloudApigeeV1DebugMaskOut": "_apigee_489_GoogleCloudApigeeV1DebugMaskOut",
        "GoogleCloudApigeeV1TlsInfoCommonNameIn": "_apigee_490_GoogleCloudApigeeV1TlsInfoCommonNameIn",
        "GoogleCloudApigeeV1TlsInfoCommonNameOut": "_apigee_491_GoogleCloudApigeeV1TlsInfoCommonNameOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudApigeeV1GraphQLOperationConfigIn"] = t.struct(
        {
            "apiSource": t.string(),
            "quota": t.proxy(renames["GoogleCloudApigeeV1QuotaIn"]).optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
            ).optional(),
            "operations": t.array(
                t.proxy(renames["GoogleCloudApigeeV1GraphQLOperationIn"])
            ),
        }
    ).named(renames["GoogleCloudApigeeV1GraphQLOperationConfigIn"])
    types["GoogleCloudApigeeV1GraphQLOperationConfigOut"] = t.struct(
        {
            "apiSource": t.string(),
            "quota": t.proxy(renames["GoogleCloudApigeeV1QuotaOut"]).optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeOut"])
            ).optional(),
            "operations": t.array(
                t.proxy(renames["GoogleCloudApigeeV1GraphQLOperationOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1GraphQLOperationConfigOut"])
    types["GoogleCloudApigeeV1AppGroupAppKeyIn"] = t.struct(
        {
            "status": t.string().optional(),
            "consumerKey": t.string().optional(),
            "consumerSecret": t.string().optional(),
            "expiresInSeconds": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AppGroupAppKeyIn"])
    types["GoogleCloudApigeeV1AppGroupAppKeyOut"] = t.struct(
        {
            "issuedAt": t.string().optional(),
            "status": t.string().optional(),
            "consumerKey": t.string().optional(),
            "expiresAt": t.string().optional(),
            "consumerSecret": t.string().optional(),
            "expiresInSeconds": t.string().optional(),
            "apiProducts": t.array(
                t.proxy(renames["GoogleCloudApigeeV1APIProductAssociationOut"])
            ).optional(),
            "scopes": t.array(t.string()).optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AppGroupAppKeyOut"])
    types["GoogleCloudApigeeV1ResourceFilesIn"] = t.struct(
        {
            "resourceFile": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ResourceFileIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudApigeeV1ResourceFilesIn"])
    types["GoogleCloudApigeeV1ResourceFilesOut"] = t.struct(
        {
            "resourceFile": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ResourceFileOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ResourceFilesOut"])
    types["GoogleCloudApigeeV1RatePlanIn"] = t.struct(
        {
            "billingPeriod": t.string().optional(),
            "consumptionPricingType": t.string().optional(),
            "currencyCode": t.string().optional(),
            "description": t.string().optional(),
            "revenueShareRates": t.array(
                t.proxy(renames["GoogleCloudApigeeV1RevenueShareRangeIn"])
            ).optional(),
            "apiproduct": t.string().optional(),
            "fixedRecurringFee": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
            "paymentFundingModel": t.string().optional(),
            "revenueShareType": t.string().optional(),
            "setupFee": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
            "state": t.string().optional(),
            "fixedFeeFrequency": t.integer().optional(),
            "startTime": t.string().optional(),
            "displayName": t.string().optional(),
            "consumptionPricingRates": t.array(
                t.proxy(renames["GoogleCloudApigeeV1RateRangeIn"])
            ).optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RatePlanIn"])
    types["GoogleCloudApigeeV1RatePlanOut"] = t.struct(
        {
            "lastModifiedAt": t.string().optional(),
            "createdAt": t.string().optional(),
            "billingPeriod": t.string().optional(),
            "consumptionPricingType": t.string().optional(),
            "currencyCode": t.string().optional(),
            "description": t.string().optional(),
            "revenueShareRates": t.array(
                t.proxy(renames["GoogleCloudApigeeV1RevenueShareRangeOut"])
            ).optional(),
            "apiproduct": t.string().optional(),
            "fixedRecurringFee": t.proxy(renames["GoogleTypeMoneyOut"]).optional(),
            "paymentFundingModel": t.string().optional(),
            "revenueShareType": t.string().optional(),
            "setupFee": t.proxy(renames["GoogleTypeMoneyOut"]).optional(),
            "state": t.string().optional(),
            "fixedFeeFrequency": t.integer().optional(),
            "startTime": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "consumptionPricingRates": t.array(
                t.proxy(renames["GoogleCloudApigeeV1RateRangeOut"])
            ).optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RatePlanOut"])
    types["GoogleCloudApigeeV1ApiProductIn"] = t.struct(
        {
            "createdAt": t.string().optional(),
            "operationGroup": t.proxy(
                renames["GoogleCloudApigeeV1OperationGroupIn"]
            ).optional(),
            "apiResources": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "quotaCounterScope": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "quota": t.string().optional(),
            "displayName": t.string().optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
            ).optional(),
            "graphqlOperationGroup": t.proxy(
                renames["GoogleCloudApigeeV1GraphQLOperationGroupIn"]
            ).optional(),
            "quotaTimeUnit": t.string().optional(),
            "quotaInterval": t.string().optional(),
            "environments": t.array(t.string()).optional(),
            "lastModifiedAt": t.string().optional(),
            "approvalType": t.string().optional(),
            "proxies": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ApiProductIn"])
    types["GoogleCloudApigeeV1ApiProductOut"] = t.struct(
        {
            "createdAt": t.string().optional(),
            "operationGroup": t.proxy(
                renames["GoogleCloudApigeeV1OperationGroupOut"]
            ).optional(),
            "apiResources": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "quotaCounterScope": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "quota": t.string().optional(),
            "displayName": t.string().optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeOut"])
            ).optional(),
            "graphqlOperationGroup": t.proxy(
                renames["GoogleCloudApigeeV1GraphQLOperationGroupOut"]
            ).optional(),
            "quotaTimeUnit": t.string().optional(),
            "quotaInterval": t.string().optional(),
            "environments": t.array(t.string()).optional(),
            "lastModifiedAt": t.string().optional(),
            "approvalType": t.string().optional(),
            "proxies": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ApiProductOut"])
    types["GoogleRpcPreconditionFailureIn"] = t.struct(
        {
            "violations": t.array(
                t.proxy(renames["GoogleRpcPreconditionFailureViolationIn"])
            ).optional()
        }
    ).named(renames["GoogleRpcPreconditionFailureIn"])
    types["GoogleRpcPreconditionFailureOut"] = t.struct(
        {
            "violations": t.array(
                t.proxy(renames["GoogleRpcPreconditionFailureViolationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcPreconditionFailureOut"])
    types["GoogleCloudApigeeV1PropertiesIn"] = t.struct(
        {
            "property": t.array(
                t.proxy(renames["GoogleCloudApigeeV1PropertyIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudApigeeV1PropertiesIn"])
    types["GoogleCloudApigeeV1PropertiesOut"] = t.struct(
        {
            "property": t.array(
                t.proxy(renames["GoogleCloudApigeeV1PropertyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1PropertiesOut"])
    types["GoogleCloudApigeeV1DeleteResponseIn"] = t.struct(
        {
            "status": t.string().optional(),
            "message": t.string().optional(),
            "gcpResource": t.string().optional(),
            "errorCode": t.string().optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeleteResponseIn"])
    types["GoogleCloudApigeeV1DeleteResponseOut"] = t.struct(
        {
            "status": t.string().optional(),
            "message": t.string().optional(),
            "gcpResource": t.string().optional(),
            "errorCode": t.string().optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeleteResponseOut"])
    types["GoogleCloudApigeeV1SecurityReportResultMetadataIn"] = t.struct(
        {"self": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1SecurityReportResultMetadataIn"])
    types["GoogleCloudApigeeV1SecurityReportResultMetadataOut"] = t.struct(
        {
            "expires": t.string().optional(),
            "self": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityReportResultMetadataOut"])
    types["GoogleCloudApigeeV1CertInfoIn"] = t.struct(
        {
            "issuer": t.string().optional(),
            "serialNumber": t.string().optional(),
            "basicConstraints": t.string().optional(),
            "expiryDate": t.string().optional(),
            "subject": t.string().optional(),
            "isValid": t.string().optional(),
            "version": t.integer().optional(),
            "validFrom": t.string().optional(),
            "sigAlgName": t.string().optional(),
            "subjectAlternativeNames": t.array(t.string()).optional(),
            "publicKey": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1CertInfoIn"])
    types["GoogleCloudApigeeV1CertInfoOut"] = t.struct(
        {
            "issuer": t.string().optional(),
            "serialNumber": t.string().optional(),
            "basicConstraints": t.string().optional(),
            "expiryDate": t.string().optional(),
            "subject": t.string().optional(),
            "isValid": t.string().optional(),
            "version": t.integer().optional(),
            "validFrom": t.string().optional(),
            "sigAlgName": t.string().optional(),
            "subjectAlternativeNames": t.array(t.string()).optional(),
            "publicKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1CertInfoOut"])
    types["GoogleCloudApigeeV1SessionIn"] = t.struct(
        {"timestampMs": t.string().optional(), "id": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1SessionIn"])
    types["GoogleCloudApigeeV1SessionOut"] = t.struct(
        {
            "timestampMs": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SessionOut"])
    types["GoogleRpcPreconditionFailureViolationIn"] = t.struct(
        {
            "subject": t.string().optional(),
            "type": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleRpcPreconditionFailureViolationIn"])
    types["GoogleRpcPreconditionFailureViolationOut"] = t.struct(
        {
            "subject": t.string().optional(),
            "type": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcPreconditionFailureViolationOut"])
    types["GoogleCloudApigeeV1EntityMetadataIn"] = t.struct(
        {
            "lastModifiedAt": t.string().optional(),
            "createdAt": t.string().optional(),
            "subType": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1EntityMetadataIn"])
    types["GoogleCloudApigeeV1EntityMetadataOut"] = t.struct(
        {
            "lastModifiedAt": t.string().optional(),
            "createdAt": t.string().optional(),
            "subType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1EntityMetadataOut"])
    types["GoogleCloudApigeeV1ListSharedFlowsResponseIn"] = t.struct(
        {"sharedFlows": t.array(t.proxy(renames["GoogleCloudApigeeV1SharedFlowIn"]))}
    ).named(renames["GoogleCloudApigeeV1ListSharedFlowsResponseIn"])
    types["GoogleCloudApigeeV1ListSharedFlowsResponseOut"] = t.struct(
        {
            "sharedFlows": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SharedFlowOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListSharedFlowsResponseOut"])
    types["GoogleCloudApigeeV1SharedFlowRevisionIn"] = t.struct(
        {
            "configurationVersion": t.proxy(
                renames["GoogleCloudApigeeV1ConfigVersionIn"]
            ).optional(),
            "contextInfo": t.string().optional(),
            "sharedFlows": t.array(t.string()).optional(),
            "createdAt": t.string().optional(),
            "description": t.string().optional(),
            "resourceFiles": t.proxy(
                renames["GoogleCloudApigeeV1ResourceFilesIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "revision": t.string().optional(),
            "name": t.string().optional(),
            "lastModifiedAt": t.string().optional(),
            "type": t.string().optional(),
            "policies": t.array(t.string()).optional(),
            "resources": t.array(t.string()).optional(),
            "entityMetaDataAsProperties": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SharedFlowRevisionIn"])
    types["GoogleCloudApigeeV1SharedFlowRevisionOut"] = t.struct(
        {
            "configurationVersion": t.proxy(
                renames["GoogleCloudApigeeV1ConfigVersionOut"]
            ).optional(),
            "contextInfo": t.string().optional(),
            "sharedFlows": t.array(t.string()).optional(),
            "createdAt": t.string().optional(),
            "description": t.string().optional(),
            "resourceFiles": t.proxy(
                renames["GoogleCloudApigeeV1ResourceFilesOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "revision": t.string().optional(),
            "name": t.string().optional(),
            "lastModifiedAt": t.string().optional(),
            "type": t.string().optional(),
            "policies": t.array(t.string()).optional(),
            "resources": t.array(t.string()).optional(),
            "entityMetaDataAsProperties": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SharedFlowRevisionOut"])
    types["GoogleCloudApigeeV1KeyValueMapIn"] = t.struct(
        {"name": t.string(), "encrypted": t.boolean()}
    ).named(renames["GoogleCloudApigeeV1KeyValueMapIn"])
    types["GoogleCloudApigeeV1KeyValueMapOut"] = t.struct(
        {
            "name": t.string(),
            "encrypted": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1KeyValueMapOut"])
    types["GoogleCloudApigeeV1ListKeyValueEntriesResponseIn"] = t.struct(
        {
            "keyValueEntries": t.array(
                t.proxy(renames["GoogleCloudApigeeV1KeyValueEntryIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListKeyValueEntriesResponseIn"])
    types["GoogleCloudApigeeV1ListKeyValueEntriesResponseOut"] = t.struct(
        {
            "keyValueEntries": t.array(
                t.proxy(renames["GoogleCloudApigeeV1KeyValueEntryOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListKeyValueEntriesResponseOut"])
    types["GoogleCloudApigeeV1AddonsConfigIn"] = t.struct(
        {
            "monetizationConfig": t.proxy(
                renames["GoogleCloudApigeeV1MonetizationConfigIn"]
            ).optional(),
            "connectorsPlatformConfig": t.proxy(
                renames["GoogleCloudApigeeV1ConnectorsPlatformConfigIn"]
            ).optional(),
            "apiSecurityConfig": t.proxy(
                renames["GoogleCloudApigeeV1ApiSecurityConfigIn"]
            ).optional(),
            "integrationConfig": t.proxy(
                renames["GoogleCloudApigeeV1IntegrationConfigIn"]
            ).optional(),
            "advancedApiOpsConfig": t.proxy(
                renames["GoogleCloudApigeeV1AdvancedApiOpsConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AddonsConfigIn"])
    types["GoogleCloudApigeeV1AddonsConfigOut"] = t.struct(
        {
            "monetizationConfig": t.proxy(
                renames["GoogleCloudApigeeV1MonetizationConfigOut"]
            ).optional(),
            "connectorsPlatformConfig": t.proxy(
                renames["GoogleCloudApigeeV1ConnectorsPlatformConfigOut"]
            ).optional(),
            "apiSecurityConfig": t.proxy(
                renames["GoogleCloudApigeeV1ApiSecurityConfigOut"]
            ).optional(),
            "integrationConfig": t.proxy(
                renames["GoogleCloudApigeeV1IntegrationConfigOut"]
            ).optional(),
            "advancedApiOpsConfig": t.proxy(
                renames["GoogleCloudApigeeV1AdvancedApiOpsConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AddonsConfigOut"])
    types["GoogleCloudApigeeV1ResultIn"] = t.struct(
        {
            "uRI": t.string().optional(),
            "reasonPhrase": t.string().optional(),
            "statusCode": t.string().optional(),
            "properties": t.proxy(
                renames["GoogleCloudApigeeV1PropertiesIn"]
            ).optional(),
            "verb": t.string().optional(),
            "accessList": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AccessIn"])
            ).optional(),
            "headers": t.array(
                t.proxy(renames["GoogleCloudApigeeV1PropertyIn"])
            ).optional(),
            "ActionResult": t.string().optional(),
            "content": t.string().optional(),
            "timestamp": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ResultIn"])
    types["GoogleCloudApigeeV1ResultOut"] = t.struct(
        {
            "uRI": t.string().optional(),
            "reasonPhrase": t.string().optional(),
            "statusCode": t.string().optional(),
            "properties": t.proxy(
                renames["GoogleCloudApigeeV1PropertiesOut"]
            ).optional(),
            "verb": t.string().optional(),
            "accessList": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AccessOut"])
            ).optional(),
            "headers": t.array(
                t.proxy(renames["GoogleCloudApigeeV1PropertyOut"])
            ).optional(),
            "ActionResult": t.string().optional(),
            "content": t.string().optional(),
            "timestamp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ResultOut"])
    types["GoogleIamV1AuditConfigIn"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditLogConfigIn"])
            ).optional(),
        }
    ).named(renames["GoogleIamV1AuditConfigIn"])
    types["GoogleIamV1AuditConfigOut"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditLogConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1AuditConfigOut"])
    types["GoogleCloudApigeeV1OperationMetadataProgressIn"] = t.struct(
        {
            "description": t.string().optional(),
            "percentDone": t.integer().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OperationMetadataProgressIn"])
    types["GoogleCloudApigeeV1OperationMetadataProgressOut"] = t.struct(
        {
            "description": t.string().optional(),
            "percentDone": t.integer().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OperationMetadataProgressOut"])
    types["GoogleIamV1TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsResponseIn"])
    types["GoogleIamV1TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsResponseOut"])
    types["GoogleCloudApigeeV1DataCollectorIn"] = t.struct(
        {
            "type": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DataCollectorIn"])
    types["GoogleCloudApigeeV1DataCollectorOut"] = t.struct(
        {
            "lastModifiedAt": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "createdAt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DataCollectorOut"])
    types["GoogleCloudApigeeV1ListCustomReportsResponseIn"] = t.struct(
        {"qualifier": t.array(t.proxy(renames["GoogleCloudApigeeV1CustomReportIn"]))}
    ).named(renames["GoogleCloudApigeeV1ListCustomReportsResponseIn"])
    types["GoogleCloudApigeeV1ListCustomReportsResponseOut"] = t.struct(
        {
            "qualifier": t.array(
                t.proxy(renames["GoogleCloudApigeeV1CustomReportOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListCustomReportsResponseOut"])
    types["GoogleCloudApigeeV1QueryTimeSeriesStatsResponseIn"] = t.struct(
        {
            "values": t.array(
                t.proxy(
                    renames["GoogleCloudApigeeV1QueryTimeSeriesStatsResponseSequenceIn"]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
            "columns": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryTimeSeriesStatsResponseIn"])
    types["GoogleCloudApigeeV1QueryTimeSeriesStatsResponseOut"] = t.struct(
        {
            "values": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudApigeeV1QueryTimeSeriesStatsResponseSequenceOut"
                    ]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
            "columns": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryTimeSeriesStatsResponseOut"])
    types["GoogleCloudApigeeV1SecurityProfileScoringConfigIn"] = t.struct(
        {
            "scorePath": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityProfileScoringConfigIn"])
    types["GoogleCloudApigeeV1SecurityProfileScoringConfigOut"] = t.struct(
        {
            "scorePath": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityProfileScoringConfigOut"])
    types["GoogleCloudApigeeV1KeystoreIn"] = t.struct({"name": t.string()}).named(
        renames["GoogleCloudApigeeV1KeystoreIn"]
    )
    types["GoogleCloudApigeeV1KeystoreOut"] = t.struct(
        {
            "name": t.string(),
            "aliases": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1KeystoreOut"])
    types["GoogleCloudApigeeV1AppGroupAppIn"] = t.struct(
        {
            "name": t.string().optional(),
            "appGroup": t.string().optional(),
            "callbackUrl": t.string().optional(),
            "apiProducts": t.array(t.string()).optional(),
            "keyExpiresIn": t.string().optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
            ).optional(),
            "status": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "appId": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AppGroupAppIn"])
    types["GoogleCloudApigeeV1AppGroupAppOut"] = t.struct(
        {
            "createdAt": t.string().optional(),
            "name": t.string().optional(),
            "appGroup": t.string().optional(),
            "callbackUrl": t.string().optional(),
            "apiProducts": t.array(t.string()).optional(),
            "keyExpiresIn": t.string().optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeOut"])
            ).optional(),
            "status": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "credentials": t.array(
                t.proxy(renames["GoogleCloudApigeeV1CredentialOut"])
            ).optional(),
            "appId": t.string().optional(),
            "lastModifiedAt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AppGroupAppOut"])
    types["GoogleCloudApigeeV1EnvironmentConfigIn"] = t.struct(
        {
            "featureFlags": t.struct({"_": t.string().optional()}).optional(),
            "pubsubTopic": t.string().optional(),
            "debugMask": t.proxy(renames["GoogleCloudApigeeV1DebugMaskIn"]).optional(),
            "forwardProxyUri": t.string().optional(),
            "resourceReferences": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ReferenceConfigIn"])
            ).optional(),
            "keystores": t.array(
                t.proxy(renames["GoogleCloudApigeeV1KeystoreConfigIn"])
            ).optional(),
            "resources": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ResourceConfigIn"])
            ).optional(),
            "uid": t.string().optional(),
            "flowhooks": t.array(
                t.proxy(renames["GoogleCloudApigeeV1FlowHookConfigIn"])
            ).optional(),
            "arcConfigLocation": t.string().optional(),
            "createTime": t.string().optional(),
            "provider": t.string().optional(),
            "dataCollectors": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DataCollectorConfigIn"])
            ).optional(),
            "revisionId": t.string().optional(),
            "name": t.string().optional(),
            "envScopedRevisionId": t.string().optional(),
            "deployments": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DeploymentConfigIn"])
            ).optional(),
            "deploymentGroups": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DeploymentGroupConfigIn"])
            ).optional(),
            "targets": t.array(
                t.proxy(renames["GoogleCloudApigeeV1TargetServerConfigIn"])
            ).optional(),
            "sequenceNumber": t.string().optional(),
            "traceConfig": t.proxy(
                renames["GoogleCloudApigeeV1RuntimeTraceConfigIn"]
            ).optional(),
            "gatewayConfigLocation": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1EnvironmentConfigIn"])
    types["GoogleCloudApigeeV1EnvironmentConfigOut"] = t.struct(
        {
            "featureFlags": t.struct({"_": t.string().optional()}).optional(),
            "pubsubTopic": t.string().optional(),
            "debugMask": t.proxy(renames["GoogleCloudApigeeV1DebugMaskOut"]).optional(),
            "forwardProxyUri": t.string().optional(),
            "resourceReferences": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ReferenceConfigOut"])
            ).optional(),
            "keystores": t.array(
                t.proxy(renames["GoogleCloudApigeeV1KeystoreConfigOut"])
            ).optional(),
            "resources": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ResourceConfigOut"])
            ).optional(),
            "uid": t.string().optional(),
            "flowhooks": t.array(
                t.proxy(renames["GoogleCloudApigeeV1FlowHookConfigOut"])
            ).optional(),
            "arcConfigLocation": t.string().optional(),
            "createTime": t.string().optional(),
            "provider": t.string().optional(),
            "dataCollectors": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DataCollectorConfigOut"])
            ).optional(),
            "revisionId": t.string().optional(),
            "name": t.string().optional(),
            "envScopedRevisionId": t.string().optional(),
            "deployments": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DeploymentConfigOut"])
            ).optional(),
            "deploymentGroups": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DeploymentGroupConfigOut"])
            ).optional(),
            "targets": t.array(
                t.proxy(renames["GoogleCloudApigeeV1TargetServerConfigOut"])
            ).optional(),
            "sequenceNumber": t.string().optional(),
            "traceConfig": t.proxy(
                renames["GoogleCloudApigeeV1RuntimeTraceConfigOut"]
            ).optional(),
            "gatewayConfigLocation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1EnvironmentConfigOut"])
    types["GoogleCloudApigeeV1ListEnvironmentGroupsResponseIn"] = t.struct(
        {
            "environmentGroups": t.array(
                t.proxy(renames["GoogleCloudApigeeV1EnvironmentGroupIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListEnvironmentGroupsResponseIn"])
    types["GoogleCloudApigeeV1ListEnvironmentGroupsResponseOut"] = t.struct(
        {
            "environmentGroups": t.array(
                t.proxy(renames["GoogleCloudApigeeV1EnvironmentGroupOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListEnvironmentGroupsResponseOut"])
    types["GoogleCloudApigeeV1UpdateErrorIn"] = t.struct(
        {
            "code": t.string().optional(),
            "resource": t.string().optional(),
            "type": t.string().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1UpdateErrorIn"])
    types["GoogleCloudApigeeV1UpdateErrorOut"] = t.struct(
        {
            "code": t.string().optional(),
            "resource": t.string().optional(),
            "type": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1UpdateErrorOut"])
    types["GoogleCloudApigeeV1TestDatastoreResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1TestDatastoreResponseIn"])
    types["GoogleCloudApigeeV1TestDatastoreResponseOut"] = t.struct(
        {
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1TestDatastoreResponseOut"])
    types["GoogleCloudApigeeV1DeveloperSubscriptionIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "apiproduct": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeveloperSubscriptionIn"])
    types["GoogleCloudApigeeV1DeveloperSubscriptionOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "apiproduct": t.string().optional(),
            "createdAt": t.string().optional(),
            "endTime": t.string().optional(),
            "name": t.string().optional(),
            "lastModifiedAt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeveloperSubscriptionOut"])
    types["GoogleCloudApigeeV1ApiProxyRevisionIn"] = t.struct(
        {
            "basepaths": t.array(t.string()).optional(),
            "proxies": t.array(t.string()).optional(),
            "targets": t.array(t.string()).optional(),
            "resources": t.array(t.string()).optional(),
            "spec": t.string().optional(),
            "policies": t.array(t.string()).optional(),
            "resourceFiles": t.proxy(
                renames["GoogleCloudApigeeV1ResourceFilesIn"]
            ).optional(),
            "configurationVersion": t.proxy(
                renames["GoogleCloudApigeeV1ConfigVersionIn"]
            ).optional(),
            "lastModifiedAt": t.string().optional(),
            "targetEndpoints": t.array(t.string()).optional(),
            "integrationEndpoints": t.array(t.string()).optional(),
            "revision": t.string().optional(),
            "entityMetaDataAsProperties": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "displayName": t.string().optional(),
            "targetServers": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "sharedFlows": t.array(t.string()).optional(),
            "proxyEndpoints": t.array(t.string()).optional(),
            "createdAt": t.string().optional(),
            "name": t.string().optional(),
            "teams": t.array(t.string()).optional(),
            "contextInfo": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ApiProxyRevisionIn"])
    types["GoogleCloudApigeeV1ApiProxyRevisionOut"] = t.struct(
        {
            "basepaths": t.array(t.string()).optional(),
            "proxies": t.array(t.string()).optional(),
            "targets": t.array(t.string()).optional(),
            "resources": t.array(t.string()).optional(),
            "spec": t.string().optional(),
            "policies": t.array(t.string()).optional(),
            "resourceFiles": t.proxy(
                renames["GoogleCloudApigeeV1ResourceFilesOut"]
            ).optional(),
            "configurationVersion": t.proxy(
                renames["GoogleCloudApigeeV1ConfigVersionOut"]
            ).optional(),
            "lastModifiedAt": t.string().optional(),
            "targetEndpoints": t.array(t.string()).optional(),
            "integrationEndpoints": t.array(t.string()).optional(),
            "revision": t.string().optional(),
            "entityMetaDataAsProperties": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "displayName": t.string().optional(),
            "targetServers": t.array(t.string()).optional(),
            "archive": t.string().optional(),
            "type": t.string().optional(),
            "sharedFlows": t.array(t.string()).optional(),
            "proxyEndpoints": t.array(t.string()).optional(),
            "createdAt": t.string().optional(),
            "name": t.string().optional(),
            "teams": t.array(t.string()).optional(),
            "contextInfo": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ApiProxyRevisionOut"])
    types["GoogleCloudApigeeV1CredentialIn"] = t.struct(
        {
            "expiresAt": t.string().optional(),
            "consumerSecret": t.string().optional(),
            "apiProducts": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ApiProductRefIn"])
            ).optional(),
            "issuedAt": t.string().optional(),
            "consumerKey": t.string().optional(),
            "status": t.string().optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
            ).optional(),
            "scopes": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1CredentialIn"])
    types["GoogleCloudApigeeV1CredentialOut"] = t.struct(
        {
            "expiresAt": t.string().optional(),
            "consumerSecret": t.string().optional(),
            "apiProducts": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ApiProductRefOut"])
            ).optional(),
            "issuedAt": t.string().optional(),
            "consumerKey": t.string().optional(),
            "status": t.string().optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeOut"])
            ).optional(),
            "scopes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1CredentialOut"])
    types["GoogleCloudApigeeV1ListNatAddressesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "natAddresses": t.array(
                t.proxy(renames["GoogleCloudApigeeV1NatAddressIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListNatAddressesResponseIn"])
    types["GoogleCloudApigeeV1ListNatAddressesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "natAddresses": t.array(
                t.proxy(renames["GoogleCloudApigeeV1NatAddressOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListNatAddressesResponseOut"])
    types["GoogleCloudApigeeV1CustomReportIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "offset": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "name": t.string(),
            "filter": t.string().optional(),
            "limit": t.string().optional(),
            "sortOrder": t.string().optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1CustomReportMetricIn"])
            ),
            "dimensions": t.array(t.string()).optional(),
            "timeUnit": t.string().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ReportPropertyIn"])
            ).optional(),
            "chartType": t.string().optional(),
            "toTime": t.string().optional(),
            "fromTime": t.string().optional(),
            "sortByCols": t.array(t.string()).optional(),
            "comments": t.array(t.string()).optional(),
            "topk": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1CustomReportIn"])
    types["GoogleCloudApigeeV1CustomReportOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "offset": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "lastModifiedAt": t.string().optional(),
            "name": t.string(),
            "createdAt": t.string().optional(),
            "filter": t.string().optional(),
            "limit": t.string().optional(),
            "sortOrder": t.string().optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1CustomReportMetricOut"])
            ),
            "environment": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "timeUnit": t.string().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ReportPropertyOut"])
            ).optional(),
            "lastViewedAt": t.string().optional(),
            "chartType": t.string().optional(),
            "toTime": t.string().optional(),
            "fromTime": t.string().optional(),
            "sortByCols": t.array(t.string()).optional(),
            "organization": t.string().optional(),
            "comments": t.array(t.string()).optional(),
            "topk": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1CustomReportOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleTypeMoneyIn"] = t.struct(
        {
            "units": t.string().optional(),
            "nanos": t.integer().optional(),
            "currencyCode": t.string().optional(),
        }
    ).named(renames["GoogleTypeMoneyIn"])
    types["GoogleTypeMoneyOut"] = t.struct(
        {
            "units": t.string().optional(),
            "nanos": t.integer().optional(),
            "currencyCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeMoneyOut"])
    types["GoogleCloudApigeeV1DebugSessionTransactionIn"] = t.struct(
        {
            "point": t.array(t.proxy(renames["GoogleCloudApigeeV1PointIn"])).optional(),
            "completed": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DebugSessionTransactionIn"])
    types["GoogleCloudApigeeV1DebugSessionTransactionOut"] = t.struct(
        {
            "point": t.array(
                t.proxy(renames["GoogleCloudApigeeV1PointOut"])
            ).optional(),
            "completed": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DebugSessionTransactionOut"])
    types["GoogleCloudApigeeV1ListEndpointAttachmentsResponseIn"] = t.struct(
        {
            "endpointAttachments": t.array(
                t.proxy(renames["GoogleCloudApigeeV1EndpointAttachmentIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListEndpointAttachmentsResponseIn"])
    types["GoogleCloudApigeeV1ListEndpointAttachmentsResponseOut"] = t.struct(
        {
            "endpointAttachments": t.array(
                t.proxy(renames["GoogleCloudApigeeV1EndpointAttachmentOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListEndpointAttachmentsResponseOut"])
    types["GoogleCloudApigeeV1QueryTimeSeriesStatsResponseSequenceIn"] = t.struct(
        {
            "points": t.array(
                t.array(t.struct({"_": t.string().optional()}))
            ).optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryTimeSeriesStatsResponseSequenceIn"])
    types["GoogleCloudApigeeV1QueryTimeSeriesStatsResponseSequenceOut"] = t.struct(
        {
            "points": t.array(
                t.array(t.struct({"_": t.string().optional()}))
            ).optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryTimeSeriesStatsResponseSequenceOut"])
    types["GoogleCloudApigeeV1SyncAuthorizationIn"] = t.struct(
        {"etag": t.string().optional(), "identities": t.array(t.string())}
    ).named(renames["GoogleCloudApigeeV1SyncAuthorizationIn"])
    types["GoogleCloudApigeeV1SyncAuthorizationOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "identities": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SyncAuthorizationOut"])
    types["GoogleCloudApigeeV1SecurityReportIn"] = t.struct(
        {
            "resultFileSize": t.string().optional(),
            "state": t.string().optional(),
            "error": t.string().optional(),
            "reportDefinitionId": t.string().optional(),
            "resultRows": t.string().optional(),
            "displayName": t.string().optional(),
            "self": t.string().optional(),
            "envgroupHostname": t.string().optional(),
            "created": t.string().optional(),
            "queryParams": t.proxy(
                renames["GoogleCloudApigeeV1SecurityReportMetadataIn"]
            ).optional(),
            "result": t.proxy(
                renames["GoogleCloudApigeeV1SecurityReportResultMetadataIn"]
            ).optional(),
            "executionTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityReportIn"])
    types["GoogleCloudApigeeV1SecurityReportOut"] = t.struct(
        {
            "resultFileSize": t.string().optional(),
            "updated": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "reportDefinitionId": t.string().optional(),
            "resultRows": t.string().optional(),
            "displayName": t.string().optional(),
            "self": t.string().optional(),
            "envgroupHostname": t.string().optional(),
            "created": t.string().optional(),
            "queryParams": t.proxy(
                renames["GoogleCloudApigeeV1SecurityReportMetadataOut"]
            ).optional(),
            "result": t.proxy(
                renames["GoogleCloudApigeeV1SecurityReportResultMetadataOut"]
            ).optional(),
            "executionTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityReportOut"])
    types["GoogleCloudApigeeV1InstanceAttachmentIn"] = t.struct(
        {"environment": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1InstanceAttachmentIn"])
    types["GoogleCloudApigeeV1InstanceAttachmentOut"] = t.struct(
        {
            "name": t.string().optional(),
            "environment": t.string().optional(),
            "createdAt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1InstanceAttachmentOut"])
    types["GoogleCloudApigeeV1GenerateUploadUrlRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1GenerateUploadUrlRequestIn"])
    types["GoogleCloudApigeeV1GenerateUploadUrlRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudApigeeV1GenerateUploadUrlRequestOut"])
    types["GoogleCloudApigeeV1ListSecurityIncidentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "securityIncidents": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SecurityIncidentIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListSecurityIncidentsResponseIn"])
    types["GoogleCloudApigeeV1ListSecurityIncidentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "securityIncidents": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SecurityIncidentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListSecurityIncidentsResponseOut"])
    types["GoogleCloudApigeeV1DeveloperBalanceWalletIn"] = t.struct(
        {"balance": t.proxy(renames["GoogleTypeMoneyIn"]).optional()}
    ).named(renames["GoogleCloudApigeeV1DeveloperBalanceWalletIn"])
    types["GoogleCloudApigeeV1DeveloperBalanceWalletOut"] = t.struct(
        {
            "balance": t.proxy(renames["GoogleTypeMoneyOut"]).optional(),
            "lastCreditTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeveloperBalanceWalletOut"])
    types["GoogleCloudApigeeV1ResourceStatusIn"] = t.struct(
        {
            "resource": t.string().optional(),
            "uid": t.string().optional(),
            "revisions": t.array(
                t.proxy(renames["GoogleCloudApigeeV1RevisionStatusIn"])
            ).optional(),
            "totalReplicas": t.integer().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ResourceStatusIn"])
    types["GoogleCloudApigeeV1ResourceStatusOut"] = t.struct(
        {
            "resource": t.string().optional(),
            "uid": t.string().optional(),
            "revisions": t.array(
                t.proxy(renames["GoogleCloudApigeeV1RevisionStatusOut"])
            ).optional(),
            "totalReplicas": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ResourceStatusOut"])
    types["GoogleCloudApigeeV1TraceConfigIn"] = t.struct(
        {
            "exporter": t.string(),
            "samplingConfig": t.proxy(
                renames["GoogleCloudApigeeV1TraceSamplingConfigIn"]
            ).optional(),
            "endpoint": t.string(),
        }
    ).named(renames["GoogleCloudApigeeV1TraceConfigIn"])
    types["GoogleCloudApigeeV1TraceConfigOut"] = t.struct(
        {
            "exporter": t.string(),
            "samplingConfig": t.proxy(
                renames["GoogleCloudApigeeV1TraceSamplingConfigOut"]
            ).optional(),
            "endpoint": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1TraceConfigOut"])
    types["GoogleCloudApigeeV1MonetizationConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["GoogleCloudApigeeV1MonetizationConfigIn"])
    types["GoogleCloudApigeeV1MonetizationConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1MonetizationConfigOut"])
    types["GoogleCloudApigeeV1ListDeveloperSubscriptionsResponseIn"] = t.struct(
        {
            "nextStartKey": t.string().optional(),
            "developerSubscriptions": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DeveloperSubscriptionIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListDeveloperSubscriptionsResponseIn"])
    types["GoogleCloudApigeeV1ListDeveloperSubscriptionsResponseOut"] = t.struct(
        {
            "nextStartKey": t.string().optional(),
            "developerSubscriptions": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DeveloperSubscriptionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListDeveloperSubscriptionsResponseOut"])
    types["GoogleCloudApigeeV1TargetServerIn"] = t.struct(
        {
            "sSLInfo": t.proxy(renames["GoogleCloudApigeeV1TlsInfoIn"]).optional(),
            "isEnabled": t.boolean().optional(),
            "port": t.integer(),
            "name": t.string(),
            "description": t.string().optional(),
            "protocol": t.string().optional(),
            "host": t.string(),
        }
    ).named(renames["GoogleCloudApigeeV1TargetServerIn"])
    types["GoogleCloudApigeeV1TargetServerOut"] = t.struct(
        {
            "sSLInfo": t.proxy(renames["GoogleCloudApigeeV1TlsInfoOut"]).optional(),
            "isEnabled": t.boolean().optional(),
            "port": t.integer(),
            "name": t.string(),
            "description": t.string().optional(),
            "protocol": t.string().optional(),
            "host": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1TargetServerOut"])
    types["GoogleCloudApigeeV1ReportPropertyIn"] = t.struct(
        {
            "property": t.string().optional(),
            "value": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ReportPropertyIn"])
    types["GoogleCloudApigeeV1ReportPropertyOut"] = t.struct(
        {
            "property": t.string().optional(),
            "value": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ReportPropertyOut"])
    types["GoogleCloudApigeeV1EndpointChainingRuleIn"] = t.struct(
        {
            "deploymentGroup": t.string().optional(),
            "proxyIds": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1EndpointChainingRuleIn"])
    types["GoogleCloudApigeeV1EndpointChainingRuleOut"] = t.struct(
        {
            "deploymentGroup": t.string().optional(),
            "proxyIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1EndpointChainingRuleOut"])
    types["GoogleCloudApigeeV1SharedFlowIn"] = t.struct(
        {
            "latestRevisionId": t.string().optional(),
            "name": t.string().optional(),
            "metaData": t.proxy(
                renames["GoogleCloudApigeeV1EntityMetadataIn"]
            ).optional(),
            "revision": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SharedFlowIn"])
    types["GoogleCloudApigeeV1SharedFlowOut"] = t.struct(
        {
            "latestRevisionId": t.string().optional(),
            "name": t.string().optional(),
            "metaData": t.proxy(
                renames["GoogleCloudApigeeV1EntityMetadataOut"]
            ).optional(),
            "revision": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SharedFlowOut"])
    types["GoogleCloudApigeeV1ListApiCategoriesResponseIn"] = t.struct(
        {
            "status": t.string().optional(),
            "requestId": t.string().optional(),
            "message": t.string().optional(),
            "data": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ApiCategoryDataIn"])
            ).optional(),
            "errorCode": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListApiCategoriesResponseIn"])
    types["GoogleCloudApigeeV1ListApiCategoriesResponseOut"] = t.struct(
        {
            "status": t.string().optional(),
            "requestId": t.string().optional(),
            "message": t.string().optional(),
            "data": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ApiCategoryDataOut"])
            ).optional(),
            "errorCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListApiCategoriesResponseOut"])
    types["GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRouteIn"] = t.struct(
        {
            "envgroup": t.string().optional(),
            "basepath": t.string().optional(),
            "environment": t.string().optional(),
            "percentage": t.integer().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRouteIn"])
    types["GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRouteOut"] = t.struct(
        {
            "envgroup": t.string().optional(),
            "basepath": t.string().optional(),
            "environment": t.string().optional(),
            "percentage": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRouteOut"])
    types["GoogleCloudApigeeV1QueryTabularStatsRequestIn"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "timeRange": t.proxy(renames["GoogleTypeIntervalIn"]).optional(),
            "dimensions": t.array(t.string()),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1MetricAggregationIn"])
            ),
            "pageToken": t.string().optional(),
            "filter": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryTabularStatsRequestIn"])
    types["GoogleCloudApigeeV1QueryTabularStatsRequestOut"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "timeRange": t.proxy(renames["GoogleTypeIntervalOut"]).optional(),
            "dimensions": t.array(t.string()),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1MetricAggregationOut"])
            ),
            "pageToken": t.string().optional(),
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryTabularStatsRequestOut"])
    types["GoogleCloudApigeeV1DatastoreConfigIn"] = t.struct(
        {
            "projectId": t.string(),
            "bucketName": t.string().optional(),
            "tablePrefix": t.string().optional(),
            "datasetName": t.string().optional(),
            "path": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DatastoreConfigIn"])
    types["GoogleCloudApigeeV1DatastoreConfigOut"] = t.struct(
        {
            "projectId": t.string(),
            "bucketName": t.string().optional(),
            "tablePrefix": t.string().optional(),
            "datasetName": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DatastoreConfigOut"])
    types["GoogleCloudApigeeV1StatsIn"] = t.struct(
        {
            "hosts": t.array(
                t.proxy(renames["GoogleCloudApigeeV1StatsHostStatsIn"])
            ).optional(),
            "environments": t.array(
                t.proxy(renames["GoogleCloudApigeeV1StatsEnvironmentStatsIn"])
            ).optional(),
            "metaData": t.proxy(renames["GoogleCloudApigeeV1MetadataIn"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1StatsIn"])
    types["GoogleCloudApigeeV1StatsOut"] = t.struct(
        {
            "hosts": t.array(
                t.proxy(renames["GoogleCloudApigeeV1StatsHostStatsOut"])
            ).optional(),
            "environments": t.array(
                t.proxy(renames["GoogleCloudApigeeV1StatsEnvironmentStatsOut"])
            ).optional(),
            "metaData": t.proxy(renames["GoogleCloudApigeeV1MetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1StatsOut"])
    types["GoogleCloudApigeeV1RoutingRuleIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "envGroupRevision": t.string().optional(),
            "otherTargets": t.array(t.string()).optional(),
            "environment": t.string().optional(),
            "deploymentGroup": t.string().optional(),
            "receiver": t.string().optional(),
            "basepath": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RoutingRuleIn"])
    types["GoogleCloudApigeeV1RoutingRuleOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "envGroupRevision": t.string().optional(),
            "otherTargets": t.array(t.string()).optional(),
            "environment": t.string().optional(),
            "deploymentGroup": t.string().optional(),
            "receiver": t.string().optional(),
            "basepath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RoutingRuleOut"])
    types["GoogleCloudApigeeV1OperationIn"] = t.struct(
        {"methods": t.array(t.string()).optional(), "resource": t.string()}
    ).named(renames["GoogleCloudApigeeV1OperationIn"])
    types["GoogleCloudApigeeV1OperationOut"] = t.struct(
        {
            "methods": t.array(t.string()).optional(),
            "resource": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OperationOut"])
    types["GoogleCloudApigeeV1ListEnvironmentResourcesResponseIn"] = t.struct(
        {
            "resourceFile": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ResourceFileIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudApigeeV1ListEnvironmentResourcesResponseIn"])
    types["GoogleCloudApigeeV1ListEnvironmentResourcesResponseOut"] = t.struct(
        {
            "resourceFile": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ResourceFileOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListEnvironmentResourcesResponseOut"])
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
    types["GoogleCloudApigeeV1ActivateNatAddressRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1ActivateNatAddressRequestIn"])
    types["GoogleCloudApigeeV1ActivateNatAddressRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudApigeeV1ActivateNatAddressRequestOut"])
    types["GoogleCloudApigeeV1ListDeploymentsResponseIn"] = t.struct(
        {
            "deployments": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DeploymentIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudApigeeV1ListDeploymentsResponseIn"])
    types["GoogleCloudApigeeV1ListDeploymentsResponseOut"] = t.struct(
        {
            "deployments": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DeploymentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListDeploymentsResponseOut"])
    types["GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseURLInfoIn"] = t.struct(
        {
            "md5": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseURLInfoIn"])
    types["GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseURLInfoOut"] = t.struct(
        {
            "md5": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseURLInfoOut"])
    types["GoogleCloudApigeeV1ListAppsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "app": t.array(t.proxy(renames["GoogleCloudApigeeV1AppIn"])),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListAppsResponseIn"])
    types["GoogleCloudApigeeV1ListAppsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "app": t.array(t.proxy(renames["GoogleCloudApigeeV1AppOut"])),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListAppsResponseOut"])
    types["GoogleCloudApigeeV1TraceSamplingConfigIn"] = t.struct(
        {"sampler": t.string().optional(), "samplingRate": t.number().optional()}
    ).named(renames["GoogleCloudApigeeV1TraceSamplingConfigIn"])
    types["GoogleCloudApigeeV1TraceSamplingConfigOut"] = t.struct(
        {
            "sampler": t.string().optional(),
            "samplingRate": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1TraceSamplingConfigOut"])
    types["GoogleCloudApigeeV1ExportIn"] = t.struct(
        {
            "name": t.string().optional(),
            "datastoreName": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ExportIn"])
    types["GoogleCloudApigeeV1ExportOut"] = t.struct(
        {
            "name": t.string().optional(),
            "executionTime": t.string().optional(),
            "state": t.string().optional(),
            "self": t.string().optional(),
            "created": t.string().optional(),
            "datastoreName": t.string().optional(),
            "description": t.string().optional(),
            "updated": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ExportOut"])
    types["GoogleCloudApigeeV1AliasRevisionConfigIn"] = t.struct(
        {
            "location": t.string().optional(),
            "type": t.string(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AliasRevisionConfigIn"])
    types["GoogleCloudApigeeV1AliasRevisionConfigOut"] = t.struct(
        {
            "location": t.string().optional(),
            "type": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AliasRevisionConfigOut"])
    types["GoogleCloudApigeeV1DeploymentConfigIn"] = t.struct(
        {
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "proxyUid": t.string().optional(),
            "deploymentGroups": t.array(t.string()).optional(),
            "basePath": t.string().optional(),
            "location": t.string().optional(),
            "name": t.string().optional(),
            "endpoints": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccount": t.string().optional(),
            "uid": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentConfigIn"])
    types["GoogleCloudApigeeV1DeploymentConfigOut"] = t.struct(
        {
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "proxyUid": t.string().optional(),
            "deploymentGroups": t.array(t.string()).optional(),
            "basePath": t.string().optional(),
            "location": t.string().optional(),
            "name": t.string().optional(),
            "endpoints": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccount": t.string().optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentConfigOut"])
    types["GoogleCloudApigeeV1KeyAliasReferenceIn"] = t.struct(
        {"reference": t.string().optional(), "aliasId": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1KeyAliasReferenceIn"])
    types["GoogleCloudApigeeV1KeyAliasReferenceOut"] = t.struct(
        {
            "reference": t.string().optional(),
            "aliasId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1KeyAliasReferenceOut"])
    types["GoogleCloudApigeeV1ListExportsResponseIn"] = t.struct(
        {"exports": t.array(t.proxy(renames["GoogleCloudApigeeV1ExportIn"])).optional()}
    ).named(renames["GoogleCloudApigeeV1ListExportsResponseIn"])
    types["GoogleCloudApigeeV1ListExportsResponseOut"] = t.struct(
        {
            "exports": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ExportOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListExportsResponseOut"])
    types["GoogleCloudApigeeV1SchemaIn"] = t.struct(
        {
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SchemaSchemaElementIn"])
            ).optional(),
            "meta": t.array(t.string()).optional(),
            "dimensions": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SchemaSchemaElementIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SchemaIn"])
    types["GoogleCloudApigeeV1SchemaOut"] = t.struct(
        {
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SchemaSchemaElementOut"])
            ).optional(),
            "meta": t.array(t.string()).optional(),
            "dimensions": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SchemaSchemaElementOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SchemaOut"])
    types["GoogleCloudApigeeV1CertificateIn"] = t.struct(
        {
            "certInfo": t.array(
                t.proxy(renames["GoogleCloudApigeeV1CertInfoIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudApigeeV1CertificateIn"])
    types["GoogleCloudApigeeV1CertificateOut"] = t.struct(
        {
            "certInfo": t.array(
                t.proxy(renames["GoogleCloudApigeeV1CertInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1CertificateOut"])
    types["GoogleCloudApigeeV1DeveloperMonetizationConfigIn"] = t.struct(
        {"billingType": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1DeveloperMonetizationConfigIn"])
    types["GoogleCloudApigeeV1DeveloperMonetizationConfigOut"] = t.struct(
        {
            "billingType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeveloperMonetizationConfigOut"])
    types["GoogleCloudApigeeV1ArchiveDeploymentIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "gcsUri": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ArchiveDeploymentIn"])
    types["GoogleCloudApigeeV1ArchiveDeploymentOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "gcsUri": t.string().optional(),
            "updatedAt": t.string().optional(),
            "createdAt": t.string().optional(),
            "operation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ArchiveDeploymentOut"])
    types["GoogleCloudApigeeV1MetadataIn"] = t.struct(
        {
            "notices": t.array(t.string()).optional(),
            "errors": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1MetadataIn"])
    types["GoogleCloudApigeeV1MetadataOut"] = t.struct(
        {
            "notices": t.array(t.string()).optional(),
            "errors": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1MetadataOut"])
    types["GoogleCloudApigeeV1MetricIn"] = t.struct(
        {
            "name": t.string().optional(),
            "values": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1MetricIn"])
    types["GoogleCloudApigeeV1MetricOut"] = t.struct(
        {
            "name": t.string().optional(),
            "values": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1MetricOut"])
    types["GoogleCloudApigeeV1InstanceDeploymentStatusIn"] = t.struct(
        {
            "deployedRoutes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRouteIn"
                    ]
                )
            ).optional(),
            "instance": t.string().optional(),
            "deployedRevisions": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRevisionIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1InstanceDeploymentStatusIn"])
    types["GoogleCloudApigeeV1InstanceDeploymentStatusOut"] = t.struct(
        {
            "deployedRoutes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRouteOut"
                    ]
                )
            ).optional(),
            "instance": t.string().optional(),
            "deployedRevisions": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRevisionOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1InstanceDeploymentStatusOut"])
    types["GoogleCloudApigeeV1AccessIn"] = t.struct(
        {
            "Get": t.proxy(renames["GoogleCloudApigeeV1AccessGetIn"]),
            "Set": t.proxy(renames["GoogleCloudApigeeV1AccessSetIn"]),
            "Remove": t.proxy(renames["GoogleCloudApigeeV1AccessRemoveIn"]),
        }
    ).named(renames["GoogleCloudApigeeV1AccessIn"])
    types["GoogleCloudApigeeV1AccessOut"] = t.struct(
        {
            "Get": t.proxy(renames["GoogleCloudApigeeV1AccessGetOut"]),
            "Set": t.proxy(renames["GoogleCloudApigeeV1AccessSetOut"]),
            "Remove": t.proxy(renames["GoogleCloudApigeeV1AccessRemoveOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AccessOut"])
    types["GoogleCloudApigeeV1CreditDeveloperBalanceRequestIn"] = t.struct(
        {
            "transactionAmount": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
            "transactionId": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1CreditDeveloperBalanceRequestIn"])
    types["GoogleCloudApigeeV1CreditDeveloperBalanceRequestOut"] = t.struct(
        {
            "transactionAmount": t.proxy(renames["GoogleTypeMoneyOut"]).optional(),
            "transactionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1CreditDeveloperBalanceRequestOut"])
    types["GoogleCloudApigeeV1ApiSecurityRuntimeConfigIn"] = t.struct(
        {
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "uid": t.string().optional(),
            "revisionId": t.string().optional(),
            "location": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ApiSecurityRuntimeConfigIn"])
    types["GoogleCloudApigeeV1ApiSecurityRuntimeConfigOut"] = t.struct(
        {
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "uid": t.string().optional(),
            "revisionId": t.string().optional(),
            "location": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ApiSecurityRuntimeConfigOut"])
    types["GoogleCloudApigeeV1ListInstancesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "instances": t.array(
                t.proxy(renames["GoogleCloudApigeeV1InstanceIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListInstancesResponseIn"])
    types["GoogleCloudApigeeV1ListInstancesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "instances": t.array(
                t.proxy(renames["GoogleCloudApigeeV1InstanceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListInstancesResponseOut"])
    types["GoogleCloudApigeeV1OrganizationProjectMappingIn"] = t.struct(
        {
            "organization": t.string().optional(),
            "projectId": t.string().optional(),
            "projectIds": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OrganizationProjectMappingIn"])
    types["GoogleCloudApigeeV1OrganizationProjectMappingOut"] = t.struct(
        {
            "organization": t.string().optional(),
            "projectId": t.string().optional(),
            "projectIds": t.array(t.string()).optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OrganizationProjectMappingOut"])
    types["GoogleCloudApigeeV1TraceConfigOverrideIn"] = t.struct(
        {
            "name": t.string().optional(),
            "apiProxy": t.string().optional(),
            "samplingConfig": t.proxy(
                renames["GoogleCloudApigeeV1TraceSamplingConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1TraceConfigOverrideIn"])
    types["GoogleCloudApigeeV1TraceConfigOverrideOut"] = t.struct(
        {
            "name": t.string().optional(),
            "apiProxy": t.string().optional(),
            "samplingConfig": t.proxy(
                renames["GoogleCloudApigeeV1TraceSamplingConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1TraceConfigOverrideOut"])
    types["GoogleCloudApigeeV1SecurityReportResultViewIn"] = t.struct(
        {
            "rows": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.string().optional(),
            "state": t.string().optional(),
            "metadata": t.proxy(
                renames["GoogleCloudApigeeV1SecurityReportMetadataIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityReportResultViewIn"])
    types["GoogleCloudApigeeV1SecurityReportResultViewOut"] = t.struct(
        {
            "rows": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "state": t.string().optional(),
            "metadata": t.proxy(
                renames["GoogleCloudApigeeV1SecurityReportMetadataOut"]
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityReportResultViewOut"])
    types["GoogleCloudApigeeV1GraphQLOperationIn"] = t.struct(
        {"operation": t.string().optional(), "operationTypes": t.array(t.string())}
    ).named(renames["GoogleCloudApigeeV1GraphQLOperationIn"])
    types["GoogleCloudApigeeV1GraphQLOperationOut"] = t.struct(
        {
            "operation": t.string().optional(),
            "operationTypes": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1GraphQLOperationOut"])
    types["GoogleCloudApigeeV1GenerateDownloadUrlResponseIn"] = t.struct(
        {"downloadUri": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1GenerateDownloadUrlResponseIn"])
    types["GoogleCloudApigeeV1GenerateDownloadUrlResponseOut"] = t.struct(
        {
            "downloadUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1GenerateDownloadUrlResponseOut"])
    types["GoogleCloudApigeeV1AsyncQueryResultIn"] = t.struct(
        {"self": t.string().optional(), "expires": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1AsyncQueryResultIn"])
    types["GoogleCloudApigeeV1AsyncQueryResultOut"] = t.struct(
        {
            "self": t.string().optional(),
            "expires": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AsyncQueryResultOut"])
    types["GoogleCloudApigeeV1ScoreComponentRecommendationIn"] = t.struct(
        {
            "impact": t.integer().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "actions": t.array(
                t.proxy(
                    renames["GoogleCloudApigeeV1ScoreComponentRecommendationActionIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ScoreComponentRecommendationIn"])
    types["GoogleCloudApigeeV1ScoreComponentRecommendationOut"] = t.struct(
        {
            "impact": t.integer().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "actions": t.array(
                t.proxy(
                    renames["GoogleCloudApigeeV1ScoreComponentRecommendationActionOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ScoreComponentRecommendationOut"])
    types["GoogleCloudApigeeV1ComputeEnvironmentScoresRequestIn"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "filters": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilterIn"
                    ]
                )
            ).optional(),
            "pageToken": t.string().optional(),
            "timeRange": t.proxy(renames["GoogleTypeIntervalIn"]),
        }
    ).named(renames["GoogleCloudApigeeV1ComputeEnvironmentScoresRequestIn"])
    types["GoogleCloudApigeeV1ComputeEnvironmentScoresRequestOut"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "filters": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilterOut"
                    ]
                )
            ).optional(),
            "pageToken": t.string().optional(),
            "timeRange": t.proxy(renames["GoogleTypeIntervalOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ComputeEnvironmentScoresRequestOut"])
    types["GoogleTypeIntervalIn"] = t.struct(
        {"endTime": t.string().optional(), "startTime": t.string().optional()}
    ).named(renames["GoogleTypeIntervalIn"])
    types["GoogleTypeIntervalOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeIntervalOut"])
    types["GoogleCloudApigeeV1DataCollectorConfigIn"] = t.struct(
        {"name": t.string().optional(), "type": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1DataCollectorConfigIn"])
    types["GoogleCloudApigeeV1DataCollectorConfigOut"] = t.struct(
        {
            "name": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DataCollectorConfigOut"])
    types["GoogleCloudApigeeV1EnvironmentIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "forwardProxyUri": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string(),
            "nodeConfig": t.proxy(
                renames["GoogleCloudApigeeV1NodeConfigIn"]
            ).optional(),
            "deploymentType": t.string().optional(),
            "properties": t.proxy(
                renames["GoogleCloudApigeeV1PropertiesIn"]
            ).optional(),
            "apiProxyType": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1EnvironmentIn"])
    types["GoogleCloudApigeeV1EnvironmentOut"] = t.struct(
        {
            "state": t.string().optional(),
            "displayName": t.string().optional(),
            "createdAt": t.string().optional(),
            "forwardProxyUri": t.string().optional(),
            "description": t.string().optional(),
            "lastModifiedAt": t.string().optional(),
            "name": t.string(),
            "nodeConfig": t.proxy(
                renames["GoogleCloudApigeeV1NodeConfigOut"]
            ).optional(),
            "deploymentType": t.string().optional(),
            "properties": t.proxy(
                renames["GoogleCloudApigeeV1PropertiesOut"]
            ).optional(),
            "apiProxyType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1EnvironmentOut"])
    types["GoogleCloudApigeeV1ListAsyncQueriesResponseIn"] = t.struct(
        {
            "queries": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AsyncQueryIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudApigeeV1ListAsyncQueriesResponseIn"])
    types["GoogleCloudApigeeV1ListAsyncQueriesResponseOut"] = t.struct(
        {
            "queries": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AsyncQueryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListAsyncQueriesResponseOut"])
    types["GoogleCloudApigeeV1ListSecurityReportsResponseIn"] = t.struct(
        {
            "securityReports": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SecurityReportIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListSecurityReportsResponseIn"])
    types["GoogleCloudApigeeV1ListSecurityReportsResponseOut"] = t.struct(
        {
            "securityReports": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SecurityReportOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListSecurityReportsResponseOut"])
    types["GoogleIamV1TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsRequestIn"])
    types["GoogleIamV1TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsRequestOut"])
    types["GoogleCloudApigeeV1OptimizedStatsIn"] = t.struct(
        {
            "Response": t.proxy(
                renames["GoogleCloudApigeeV1OptimizedStatsResponseIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudApigeeV1OptimizedStatsIn"])
    types["GoogleCloudApigeeV1OptimizedStatsOut"] = t.struct(
        {
            "Response": t.proxy(
                renames["GoogleCloudApigeeV1OptimizedStatsResponseOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OptimizedStatsOut"])
    types["GoogleCloudApigeeV1DeveloperBalanceIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1DeveloperBalanceIn"])
    types["GoogleCloudApigeeV1DeveloperBalanceOut"] = t.struct(
        {
            "wallets": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DeveloperBalanceWalletOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeveloperBalanceOut"])
    types["GoogleCloudApigeeV1PropertyIn"] = t.struct(
        {"name": t.string().optional(), "value": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1PropertyIn"])
    types["GoogleCloudApigeeV1PropertyOut"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1PropertyOut"])
    types["GoogleCloudApigeeV1PointIn"] = t.struct(
        {
            "id": t.string().optional(),
            "results": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ResultIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1PointIn"])
    types["GoogleCloudApigeeV1PointOut"] = t.struct(
        {
            "id": t.string().optional(),
            "results": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1PointOut"])
    types["GoogleCloudApigeeV1GetSyncAuthorizationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1GetSyncAuthorizationRequestIn"])
    types["GoogleCloudApigeeV1GetSyncAuthorizationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudApigeeV1GetSyncAuthorizationRequestOut"])
    types["GoogleCloudApigeeV1AsyncQueryIn"] = t.struct(
        {
            "self": t.string().optional(),
            "error": t.string().optional(),
            "name": t.string().optional(),
            "envgroupHostname": t.string().optional(),
            "queryParams": t.proxy(
                renames["GoogleCloudApigeeV1QueryMetadataIn"]
            ).optional(),
            "created": t.string().optional(),
            "executionTime": t.string().optional(),
            "state": t.string().optional(),
            "resultRows": t.string().optional(),
            "result": t.proxy(
                renames["GoogleCloudApigeeV1AsyncQueryResultIn"]
            ).optional(),
            "resultFileSize": t.string().optional(),
            "updated": t.string().optional(),
            "reportDefinitionId": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AsyncQueryIn"])
    types["GoogleCloudApigeeV1AsyncQueryOut"] = t.struct(
        {
            "self": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "envgroupHostname": t.string().optional(),
            "queryParams": t.proxy(
                renames["GoogleCloudApigeeV1QueryMetadataOut"]
            ).optional(),
            "created": t.string().optional(),
            "executionTime": t.string().optional(),
            "state": t.string().optional(),
            "resultRows": t.string().optional(),
            "result": t.proxy(
                renames["GoogleCloudApigeeV1AsyncQueryResultOut"]
            ).optional(),
            "resultFileSize": t.string().optional(),
            "updated": t.string().optional(),
            "reportDefinitionId": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AsyncQueryOut"])
    types["GoogleCloudApigeeV1ScoreComponentIn"] = t.struct(
        {
            "scorePath": t.string().optional(),
            "recommendations": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ScoreComponentRecommendationIn"])
            ).optional(),
            "drilldownPaths": t.array(t.string()).optional(),
            "score": t.integer().optional(),
            "calculateTime": t.string().optional(),
            "dataCaptureTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ScoreComponentIn"])
    types["GoogleCloudApigeeV1ScoreComponentOut"] = t.struct(
        {
            "scorePath": t.string().optional(),
            "recommendations": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ScoreComponentRecommendationOut"])
            ).optional(),
            "drilldownPaths": t.array(t.string()).optional(),
            "score": t.integer().optional(),
            "calculateTime": t.string().optional(),
            "dataCaptureTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ScoreComponentOut"])
    types["GoogleIamV1BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["GoogleIamV1BindingIn"])
    types["GoogleIamV1BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingOut"])
    types["GoogleCloudApigeeV1SecurityReportQueryIn"] = t.struct(
        {
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SecurityReportQueryMetricIn"])
            ).optional(),
            "mimeType": t.string().optional(),
            "reportDefinitionId": t.string().optional(),
            "timeRange": t.struct({"_": t.string().optional()}),
            "displayName": t.string().optional(),
            "limit": t.integer().optional(),
            "groupByTimeUnit": t.string().optional(),
            "csvDelimiter": t.string().optional(),
            "filter": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "envgroupHostname": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityReportQueryIn"])
    types["GoogleCloudApigeeV1SecurityReportQueryOut"] = t.struct(
        {
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SecurityReportQueryMetricOut"])
            ).optional(),
            "mimeType": t.string().optional(),
            "reportDefinitionId": t.string().optional(),
            "timeRange": t.struct({"_": t.string().optional()}),
            "displayName": t.string().optional(),
            "limit": t.integer().optional(),
            "groupByTimeUnit": t.string().optional(),
            "csvDelimiter": t.string().optional(),
            "filter": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "envgroupHostname": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityReportQueryOut"])
    types["GoogleCloudApigeeV1QueryTabularStatsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "values": t.array(
                t.array(t.struct({"_": t.string().optional()}))
            ).optional(),
            "columns": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryTabularStatsResponseIn"])
    types["GoogleCloudApigeeV1QueryTabularStatsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "values": t.array(
                t.array(t.struct({"_": t.string().optional()}))
            ).optional(),
            "columns": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryTabularStatsResponseOut"])
    types["GoogleCloudApigeeV1RuntimeConfigIn"] = t.struct(
        {
            "traceBucket": t.string().optional(),
            "analyticsBucket": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RuntimeConfigIn"])
    types["GoogleCloudApigeeV1RuntimeConfigOut"] = t.struct(
        {
            "traceBucket": t.string().optional(),
            "analyticsBucket": t.string().optional(),
            "name": t.string().optional(),
            "tenantProjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RuntimeConfigOut"])
    types["GoogleCloudApigeeV1ListInstanceAttachmentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "attachments": t.array(
                t.proxy(renames["GoogleCloudApigeeV1InstanceAttachmentIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListInstanceAttachmentsResponseIn"])
    types["GoogleCloudApigeeV1ListInstanceAttachmentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "attachments": t.array(
                t.proxy(renames["GoogleCloudApigeeV1InstanceAttachmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListInstanceAttachmentsResponseOut"])
    types["GoogleCloudApigeeV1EnvironmentGroupIn"] = t.struct(
        {"name": t.string().optional(), "hostnames": t.array(t.string())}
    ).named(renames["GoogleCloudApigeeV1EnvironmentGroupIn"])
    types["GoogleCloudApigeeV1EnvironmentGroupOut"] = t.struct(
        {
            "name": t.string().optional(),
            "hostnames": t.array(t.string()),
            "state": t.string().optional(),
            "lastModifiedAt": t.string().optional(),
            "createdAt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1EnvironmentGroupOut"])
    types["GoogleCloudApigeeV1InstanceIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "diskEncryptionKeyName": t.string().optional(),
            "consumerAcceptList": t.array(t.string()).optional(),
            "peeringCidrRange": t.string().optional(),
            "location": t.string(),
            "description": t.string().optional(),
            "name": t.string(),
            "ipRange": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1InstanceIn"])
    types["GoogleCloudApigeeV1InstanceOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "port": t.string().optional(),
            "diskEncryptionKeyName": t.string().optional(),
            "consumerAcceptList": t.array(t.string()).optional(),
            "serviceAttachment": t.string().optional(),
            "lastModifiedAt": t.string().optional(),
            "peeringCidrRange": t.string().optional(),
            "location": t.string(),
            "host": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string(),
            "ipRange": t.string().optional(),
            "state": t.string().optional(),
            "createdAt": t.string().optional(),
            "runtimeVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1InstanceOut"])
    types["GoogleCloudApigeeV1AsyncQueryResultViewIn"] = t.struct(
        {
            "state": t.string().optional(),
            "rows": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "metadata": t.proxy(
                renames["GoogleCloudApigeeV1QueryMetadataIn"]
            ).optional(),
            "error": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AsyncQueryResultViewIn"])
    types["GoogleCloudApigeeV1AsyncQueryResultViewOut"] = t.struct(
        {
            "state": t.string().optional(),
            "rows": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "metadata": t.proxy(
                renames["GoogleCloudApigeeV1QueryMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AsyncQueryResultViewOut"])
    types["GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentIn"] = t.struct(
        {
            "basepath": t.string().optional(),
            "apiProxy": t.string().optional(),
            "revision": t.string().optional(),
            "environment": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentIn"])
    types["GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentOut"] = t.struct(
        {
            "basepath": t.string().optional(),
            "apiProxy": t.string().optional(),
            "revision": t.string().optional(),
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentOut"])
    types["GoogleCloudApigeeV1NatAddressIn"] = t.struct({"name": t.string()}).named(
        renames["GoogleCloudApigeeV1NatAddressIn"]
    )
    types["GoogleCloudApigeeV1NatAddressOut"] = t.struct(
        {
            "name": t.string(),
            "ipAddress": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1NatAddressOut"])
    types["GoogleCloudApigeeV1ExpireDeveloperSubscriptionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1ExpireDeveloperSubscriptionRequestIn"])
    types["GoogleCloudApigeeV1ExpireDeveloperSubscriptionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudApigeeV1ExpireDeveloperSubscriptionRequestOut"])
    types["GoogleCloudApigeeV1ConnectorsPlatformConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["GoogleCloudApigeeV1ConnectorsPlatformConfigIn"])
    types["GoogleCloudApigeeV1ConnectorsPlatformConfigOut"] = t.struct(
        {
            "expiresAt": t.string().optional(),
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ConnectorsPlatformConfigOut"])
    types["GoogleCloudApigeeV1CanaryEvaluationMetricLabelsIn"] = t.struct(
        {
            "instance_id": t.string(),
            "location": t.string(),
            "env": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1CanaryEvaluationMetricLabelsIn"])
    types["GoogleCloudApigeeV1CanaryEvaluationMetricLabelsOut"] = t.struct(
        {
            "instance_id": t.string(),
            "location": t.string(),
            "env": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1CanaryEvaluationMetricLabelsOut"])
    types["GoogleCloudApigeeV1EnvironmentGroupConfigIn"] = t.struct(
        {
            "hostnames": t.array(t.string()).optional(),
            "uid": t.string().optional(),
            "endpointChainingRules": t.array(
                t.proxy(renames["GoogleCloudApigeeV1EndpointChainingRuleIn"])
            ).optional(),
            "routingRules": t.array(
                t.proxy(renames["GoogleCloudApigeeV1RoutingRuleIn"])
            ).optional(),
            "revisionId": t.string().optional(),
            "name": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1EnvironmentGroupConfigIn"])
    types["GoogleCloudApigeeV1EnvironmentGroupConfigOut"] = t.struct(
        {
            "hostnames": t.array(t.string()).optional(),
            "uid": t.string().optional(),
            "endpointChainingRules": t.array(
                t.proxy(renames["GoogleCloudApigeeV1EndpointChainingRuleOut"])
            ).optional(),
            "routingRules": t.array(
                t.proxy(renames["GoogleCloudApigeeV1RoutingRuleOut"])
            ).optional(),
            "revisionId": t.string().optional(),
            "name": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1EnvironmentGroupConfigOut"])
    types["GoogleCloudApigeeV1RateRangeIn"] = t.struct(
        {
            "fee": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
            "start": t.string().optional(),
            "end": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RateRangeIn"])
    types["GoogleCloudApigeeV1RateRangeOut"] = t.struct(
        {
            "fee": t.proxy(renames["GoogleTypeMoneyOut"]).optional(),
            "start": t.string().optional(),
            "end": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RateRangeOut"])
    types["GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseIn"] = t.struct(
        {
            "urls": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseURLInfoIn"
                    ]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseIn"])
    types["GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseOut"] = t.struct(
        {
            "urls": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseURLInfoOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseOut"])
    types["GoogleCloudApigeeV1OptimizedStatsNodeIn"] = t.struct(
        {"data": t.array(t.struct({"_": t.string().optional()}))}
    ).named(renames["GoogleCloudApigeeV1OptimizedStatsNodeIn"])
    types["GoogleCloudApigeeV1OptimizedStatsNodeOut"] = t.struct(
        {
            "data": t.array(t.struct({"_": t.string().optional()})),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OptimizedStatsNodeOut"])
    types["GoogleCloudApigeeV1StatsHostStatsIn"] = t.struct(
        {
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1MetricIn"])
            ).optional(),
            "name": t.string().optional(),
            "dimensions": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DimensionMetricIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1StatsHostStatsIn"])
    types["GoogleCloudApigeeV1StatsHostStatsOut"] = t.struct(
        {
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1MetricOut"])
            ).optional(),
            "name": t.string().optional(),
            "dimensions": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DimensionMetricOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1StatsHostStatsOut"])
    types["GoogleCloudApigeeV1GraphQLOperationGroupIn"] = t.struct(
        {
            "operationConfigType": t.string().optional(),
            "operationConfigs": t.array(
                t.proxy(renames["GoogleCloudApigeeV1GraphQLOperationConfigIn"])
            ),
        }
    ).named(renames["GoogleCloudApigeeV1GraphQLOperationGroupIn"])
    types["GoogleCloudApigeeV1GraphQLOperationGroupOut"] = t.struct(
        {
            "operationConfigType": t.string().optional(),
            "operationConfigs": t.array(
                t.proxy(renames["GoogleCloudApigeeV1GraphQLOperationConfigOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1GraphQLOperationGroupOut"])
    types[
        "GoogleCloudApigeeV1ScoreComponentRecommendationActionActionContextIn"
    ] = t.struct({"documentationLink": t.string().optional()}).named(
        renames["GoogleCloudApigeeV1ScoreComponentRecommendationActionActionContextIn"]
    )
    types[
        "GoogleCloudApigeeV1ScoreComponentRecommendationActionActionContextOut"
    ] = t.struct(
        {
            "documentationLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudApigeeV1ScoreComponentRecommendationActionActionContextOut"]
    )
    types["GoogleCloudApigeeV1EnvironmentGroupAttachmentIn"] = t.struct(
        {"name": t.string().optional(), "environment": t.string()}
    ).named(renames["GoogleCloudApigeeV1EnvironmentGroupAttachmentIn"])
    types["GoogleCloudApigeeV1EnvironmentGroupAttachmentOut"] = t.struct(
        {
            "environmentGroupId": t.string().optional(),
            "name": t.string().optional(),
            "createdAt": t.string().optional(),
            "environment": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1EnvironmentGroupAttachmentOut"])
    types["GoogleCloudApigeeV1ListOfDevelopersResponseIn"] = t.struct(
        {
            "developer": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DeveloperIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudApigeeV1ListOfDevelopersResponseIn"])
    types["GoogleCloudApigeeV1ListOfDevelopersResponseOut"] = t.struct(
        {
            "developer": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DeveloperOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListOfDevelopersResponseOut"])
    types["GoogleCloudApigeeV1StatsEnvironmentStatsIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1MetricIn"])
            ).optional(),
            "dimensions": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DimensionMetricIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1StatsEnvironmentStatsIn"])
    types["GoogleCloudApigeeV1StatsEnvironmentStatsOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1MetricOut"])
            ).optional(),
            "dimensions": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DimensionMetricOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1StatsEnvironmentStatsOut"])
    types["GoogleCloudApigeeV1PodStatusIn"] = t.struct(
        {
            "deploymentStatus": t.string().optional(),
            "podName": t.string().optional(),
            "deploymentStatusTime": t.string().optional(),
            "statusCodeDetails": t.string().optional(),
            "statusCode": t.string().optional(),
            "podStatus": t.string().optional(),
            "podStatusTime": t.string().optional(),
            "appVersion": t.string().optional(),
            "deploymentTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1PodStatusIn"])
    types["GoogleCloudApigeeV1PodStatusOut"] = t.struct(
        {
            "deploymentStatus": t.string().optional(),
            "podName": t.string().optional(),
            "deploymentStatusTime": t.string().optional(),
            "statusCodeDetails": t.string().optional(),
            "statusCode": t.string().optional(),
            "podStatus": t.string().optional(),
            "podStatusTime": t.string().optional(),
            "appVersion": t.string().optional(),
            "deploymentTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1PodStatusOut"])
    types["GoogleCloudApigeeV1TlsInfoIn"] = t.struct(
        {
            "ignoreValidationErrors": t.boolean().optional(),
            "enabled": t.boolean(),
            "keyStore": t.string(),
            "commonName": t.proxy(
                renames["GoogleCloudApigeeV1TlsInfoCommonNameIn"]
            ).optional(),
            "ciphers": t.array(t.string()).optional(),
            "trustStore": t.string().optional(),
            "keyAlias": t.string(),
            "clientAuthEnabled": t.boolean().optional(),
            "protocols": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1TlsInfoIn"])
    types["GoogleCloudApigeeV1TlsInfoOut"] = t.struct(
        {
            "ignoreValidationErrors": t.boolean().optional(),
            "enabled": t.boolean(),
            "keyStore": t.string(),
            "commonName": t.proxy(
                renames["GoogleCloudApigeeV1TlsInfoCommonNameOut"]
            ).optional(),
            "ciphers": t.array(t.string()).optional(),
            "trustStore": t.string().optional(),
            "keyAlias": t.string(),
            "clientAuthEnabled": t.boolean().optional(),
            "protocols": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1TlsInfoOut"])
    types["GoogleCloudApigeeV1ListHybridIssuersResponseIn"] = t.struct(
        {
            "issuers": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ServiceIssuersMappingIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudApigeeV1ListHybridIssuersResponseIn"])
    types["GoogleCloudApigeeV1ListHybridIssuersResponseOut"] = t.struct(
        {
            "issuers": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ServiceIssuersMappingOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListHybridIssuersResponseOut"])
    types["GoogleCloudApigeeV1FlowHookConfigIn"] = t.struct(
        {
            "continueOnError": t.boolean().optional(),
            "sharedFlowName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1FlowHookConfigIn"])
    types["GoogleCloudApigeeV1FlowHookConfigOut"] = t.struct(
        {
            "continueOnError": t.boolean().optional(),
            "sharedFlowName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1FlowHookConfigOut"])
    types["GoogleCloudApigeeV1DeploymentChangeReportIn"] = t.struct(
        {
            "validationErrors": t.proxy(
                renames["GoogleRpcPreconditionFailureIn"]
            ).optional(),
            "routingConflicts": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudApigeeV1DeploymentChangeReportRoutingConflictIn"
                    ]
                )
            ).optional(),
            "routingChanges": t.array(
                t.proxy(
                    renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingChangeIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentChangeReportIn"])
    types["GoogleCloudApigeeV1DeploymentChangeReportOut"] = t.struct(
        {
            "validationErrors": t.proxy(
                renames["GoogleRpcPreconditionFailureOut"]
            ).optional(),
            "routingConflicts": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudApigeeV1DeploymentChangeReportRoutingConflictOut"
                    ]
                )
            ).optional(),
            "routingChanges": t.array(
                t.proxy(
                    renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingChangeOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentChangeReportOut"])
    types["GoogleCloudApigeeV1OptimizedStatsResponseIn"] = t.struct(
        {
            "resultTruncated": t.boolean().optional(),
            "metaData": t.proxy(renames["GoogleCloudApigeeV1MetadataIn"]).optional(),
            "TimeUnit": t.array(t.string()).optional(),
            "stats": t.proxy(
                renames["GoogleCloudApigeeV1OptimizedStatsNodeIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OptimizedStatsResponseIn"])
    types["GoogleCloudApigeeV1OptimizedStatsResponseOut"] = t.struct(
        {
            "resultTruncated": t.boolean().optional(),
            "metaData": t.proxy(renames["GoogleCloudApigeeV1MetadataOut"]).optional(),
            "TimeUnit": t.array(t.string()).optional(),
            "stats": t.proxy(
                renames["GoogleCloudApigeeV1OptimizedStatsNodeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OptimizedStatsResponseOut"])
    types["GoogleCloudApigeeV1SecurityReportMetadataIn"] = t.struct(
        {
            "endTimestamp": t.string().optional(),
            "mimeType": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "metrics": t.array(t.string()).optional(),
            "timeUnit": t.string().optional(),
            "startTimestamp": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityReportMetadataIn"])
    types["GoogleCloudApigeeV1SecurityReportMetadataOut"] = t.struct(
        {
            "endTimestamp": t.string().optional(),
            "mimeType": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "metrics": t.array(t.string()).optional(),
            "timeUnit": t.string().optional(),
            "startTimestamp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityReportMetadataOut"])
    types["GoogleCloudApigeeV1OperationMetadataIn"] = t.struct(
        {
            "targetResourceName": t.string().optional(),
            "warnings": t.array(t.string()).optional(),
            "progress": t.proxy(
                renames["GoogleCloudApigeeV1OperationMetadataProgressIn"]
            ).optional(),
            "operationType": t.string(),
            "state": t.string(),
        }
    ).named(renames["GoogleCloudApigeeV1OperationMetadataIn"])
    types["GoogleCloudApigeeV1OperationMetadataOut"] = t.struct(
        {
            "targetResourceName": t.string().optional(),
            "warnings": t.array(t.string()).optional(),
            "progress": t.proxy(
                renames["GoogleCloudApigeeV1OperationMetadataProgressOut"]
            ).optional(),
            "operationType": t.string(),
            "state": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OperationMetadataOut"])
    types["GoogleCloudApigeeV1TlsInfoConfigIn"] = t.struct(
        {
            "commonName": t.proxy(
                renames["GoogleCloudApigeeV1CommonNameConfigIn"]
            ).optional(),
            "enabled": t.boolean().optional(),
            "clientAuthEnabled": t.boolean().optional(),
            "keyAlias": t.string().optional(),
            "keyAliasReference": t.proxy(
                renames["GoogleCloudApigeeV1KeyAliasReferenceIn"]
            ).optional(),
            "protocols": t.array(t.string()).optional(),
            "ignoreValidationErrors": t.boolean().optional(),
            "ciphers": t.array(t.string()).optional(),
            "trustStore": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1TlsInfoConfigIn"])
    types["GoogleCloudApigeeV1TlsInfoConfigOut"] = t.struct(
        {
            "commonName": t.proxy(
                renames["GoogleCloudApigeeV1CommonNameConfigOut"]
            ).optional(),
            "enabled": t.boolean().optional(),
            "clientAuthEnabled": t.boolean().optional(),
            "keyAlias": t.string().optional(),
            "keyAliasReference": t.proxy(
                renames["GoogleCloudApigeeV1KeyAliasReferenceOut"]
            ).optional(),
            "protocols": t.array(t.string()).optional(),
            "ignoreValidationErrors": t.boolean().optional(),
            "ciphers": t.array(t.string()).optional(),
            "trustStore": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1TlsInfoConfigOut"])
    types["GoogleCloudApigeeV1OperationGroupIn"] = t.struct(
        {
            "operationConfigType": t.string().optional(),
            "operationConfigs": t.array(
                t.proxy(renames["GoogleCloudApigeeV1OperationConfigIn"])
            ),
        }
    ).named(renames["GoogleCloudApigeeV1OperationGroupIn"])
    types["GoogleCloudApigeeV1OperationGroupOut"] = t.struct(
        {
            "operationConfigType": t.string().optional(),
            "operationConfigs": t.array(
                t.proxy(renames["GoogleCloudApigeeV1OperationConfigOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OperationGroupOut"])
    types["GoogleCloudApigeeV1SecurityProfileEnvironmentIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1SecurityProfileEnvironmentIn"])
    types["GoogleCloudApigeeV1SecurityProfileEnvironmentOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "attachTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityProfileEnvironmentOut"])
    types["GoogleCloudApigeeV1ReportInstanceStatusResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1ReportInstanceStatusResponseIn"])
    types["GoogleCloudApigeeV1ReportInstanceStatusResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudApigeeV1ReportInstanceStatusResponseOut"])
    types["GoogleCloudApigeeV1AccessSetIn"] = t.struct(
        {"success": t.boolean(), "name": t.string(), "value": t.string()}
    ).named(renames["GoogleCloudApigeeV1AccessSetIn"])
    types["GoogleCloudApigeeV1AccessSetOut"] = t.struct(
        {
            "success": t.boolean(),
            "name": t.string(),
            "value": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AccessSetOut"])
    types["GoogleApiHttpBodyIn"] = t.struct(
        {
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "contentType": t.string().optional(),
            "data": t.string().optional(),
        }
    ).named(renames["GoogleApiHttpBodyIn"])
    types["GoogleApiHttpBodyOut"] = t.struct(
        {
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "contentType": t.string().optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApiHttpBodyOut"])
    types["GoogleCloudApigeeV1ListDataCollectorsResponseIn"] = t.struct(
        {
            "dataCollectors": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DataCollectorIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListDataCollectorsResponseIn"])
    types["GoogleCloudApigeeV1ListDataCollectorsResponseOut"] = t.struct(
        {
            "dataCollectors": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DataCollectorOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListDataCollectorsResponseOut"])
    types["GoogleCloudApigeeV1SchemaSchemaElementIn"] = t.struct(
        {
            "properties": t.proxy(
                renames["GoogleCloudApigeeV1SchemaSchemaPropertyIn"]
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SchemaSchemaElementIn"])
    types["GoogleCloudApigeeV1SchemaSchemaElementOut"] = t.struct(
        {
            "properties": t.proxy(
                renames["GoogleCloudApigeeV1SchemaSchemaPropertyOut"]
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SchemaSchemaElementOut"])
    types["GoogleCloudApigeeV1GenerateDownloadUrlRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1GenerateDownloadUrlRequestIn"])
    types["GoogleCloudApigeeV1GenerateDownloadUrlRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudApigeeV1GenerateDownloadUrlRequestOut"])
    types["GoogleCloudApigeeV1ListArchiveDeploymentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "archiveDeployments": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ArchiveDeploymentIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListArchiveDeploymentsResponseIn"])
    types["GoogleCloudApigeeV1ListArchiveDeploymentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "archiveDeployments": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ArchiveDeploymentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListArchiveDeploymentsResponseOut"])
    types["GoogleCloudApigeeV1GenerateUploadUrlResponseIn"] = t.struct(
        {"uploadUri": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1GenerateUploadUrlResponseIn"])
    types["GoogleCloudApigeeV1GenerateUploadUrlResponseOut"] = t.struct(
        {
            "uploadUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1GenerateUploadUrlResponseOut"])
    types["GoogleCloudApigeeV1ConfigVersionIn"] = t.struct(
        {"minorVersion": t.integer().optional(), "majorVersion": t.integer().optional()}
    ).named(renames["GoogleCloudApigeeV1ConfigVersionIn"])
    types["GoogleCloudApigeeV1ConfigVersionOut"] = t.struct(
        {
            "minorVersion": t.integer().optional(),
            "majorVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ConfigVersionOut"])
    types["GoogleIamV1PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingIn"])).optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigIn"])
            ).optional(),
        }
    ).named(renames["GoogleIamV1PolicyIn"])
    types["GoogleIamV1PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingOut"])).optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1PolicyOut"])
    types["GoogleCloudApigeeV1ApiProxyIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudApigeeV1ApiProxyIn"])
    types["GoogleCloudApigeeV1ApiProxyOut"] = t.struct(
        {
            "readOnly": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metaData": t.proxy(
                renames["GoogleCloudApigeeV1EntityMetadataOut"]
            ).optional(),
            "name": t.string().optional(),
            "latestRevisionId": t.string().optional(),
            "revision": t.array(t.string()).optional(),
            "apiProxyType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ApiProxyOut"])
    types["GoogleCloudApigeeV1ListSecurityProfilesResponseIn"] = t.struct(
        {
            "securityProfiles": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SecurityProfileIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListSecurityProfilesResponseIn"])
    types["GoogleCloudApigeeV1ListSecurityProfilesResponseOut"] = t.struct(
        {
            "securityProfiles": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SecurityProfileOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListSecurityProfilesResponseOut"])
    types["GoogleCloudApigeeV1AliasIn"] = t.struct(
        {
            "type": t.string().optional(),
            "certsInfo": t.proxy(
                renames["GoogleCloudApigeeV1CertificateIn"]
            ).optional(),
            "alias": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AliasIn"])
    types["GoogleCloudApigeeV1AliasOut"] = t.struct(
        {
            "type": t.string().optional(),
            "certsInfo": t.proxy(
                renames["GoogleCloudApigeeV1CertificateOut"]
            ).optional(),
            "alias": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AliasOut"])
    types["GoogleCloudApigeeV1AppIn"] = t.struct(
        {
            "scopes": t.array(t.string()).optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
            ).optional(),
            "name": t.string().optional(),
            "callbackUrl": t.string().optional(),
            "keyExpiresIn": t.string().optional(),
            "companyName": t.string().optional(),
            "status": t.string().optional(),
            "appGroup": t.string().optional(),
            "appId": t.string().optional(),
            "developerId": t.string().optional(),
            "apiProducts": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ApiProductRefIn"])
            ).optional(),
            "developerEmail": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AppIn"])
    types["GoogleCloudApigeeV1AppOut"] = t.struct(
        {
            "createdAt": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "lastModifiedAt": t.string().optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeOut"])
            ).optional(),
            "name": t.string().optional(),
            "callbackUrl": t.string().optional(),
            "credentials": t.array(
                t.proxy(renames["GoogleCloudApigeeV1CredentialOut"])
            ).optional(),
            "keyExpiresIn": t.string().optional(),
            "companyName": t.string().optional(),
            "status": t.string().optional(),
            "appGroup": t.string().optional(),
            "appId": t.string().optional(),
            "developerId": t.string().optional(),
            "apiProducts": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ApiProductRefOut"])
            ).optional(),
            "developerEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AppOut"])
    types["GoogleCloudApigeeV1ScoreIn"] = t.struct(
        {
            "timeRange": t.proxy(renames["GoogleTypeIntervalIn"]).optional(),
            "component": t.proxy(
                renames["GoogleCloudApigeeV1ScoreComponentIn"]
            ).optional(),
            "subcomponents": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ScoreComponentIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ScoreIn"])
    types["GoogleCloudApigeeV1ScoreOut"] = t.struct(
        {
            "timeRange": t.proxy(renames["GoogleTypeIntervalOut"]).optional(),
            "component": t.proxy(
                renames["GoogleCloudApigeeV1ScoreComponentOut"]
            ).optional(),
            "subcomponents": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ScoreComponentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ScoreOut"])
    types["GoogleCloudApigeeV1DeploymentChangeReportRoutingChangeIn"] = t.struct(
        {
            "environmentGroup": t.string().optional(),
            "description": t.string().optional(),
            "fromDeployment": t.proxy(
                renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentIn"]
            ).optional(),
            "toDeployment": t.proxy(
                renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentIn"]
            ).optional(),
            "shouldSequenceRollout": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingChangeIn"])
    types["GoogleCloudApigeeV1DeploymentChangeReportRoutingChangeOut"] = t.struct(
        {
            "environmentGroup": t.string().optional(),
            "description": t.string().optional(),
            "fromDeployment": t.proxy(
                renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentOut"]
            ).optional(),
            "toDeployment": t.proxy(
                renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentOut"]
            ).optional(),
            "shouldSequenceRollout": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingChangeOut"])
    types["GoogleCloudApigeeV1SchemaSchemaPropertyIn"] = t.struct(
        {
            "custom": t.string().optional(),
            "type": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SchemaSchemaPropertyIn"])
    types["GoogleCloudApigeeV1SchemaSchemaPropertyOut"] = t.struct(
        {
            "custom": t.string().optional(),
            "type": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SchemaSchemaPropertyOut"])
    types["GoogleCloudApigeeV1SecurityProfileIn"] = t.struct(
        {
            "scoringConfigs": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SecurityProfileScoringConfigIn"])
            ).optional(),
            "description": t.string().optional(),
            "environments": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SecurityProfileEnvironmentIn"])
            ).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityProfileIn"])
    types["GoogleCloudApigeeV1SecurityProfileOut"] = t.struct(
        {
            "scoringConfigs": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SecurityProfileScoringConfigOut"])
            ).optional(),
            "description": t.string().optional(),
            "revisionUpdateTime": t.string().optional(),
            "minScore": t.integer().optional(),
            "environments": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SecurityProfileEnvironmentOut"])
            ).optional(),
            "revisionCreateTime": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "maxScore": t.integer().optional(),
            "revisionId": t.string().optional(),
            "revisionPublishTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityProfileOut"])
    types["GoogleCloudApigeeV1MetricAggregationIn"] = t.struct(
        {
            "order": t.string().optional(),
            "aggregation": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1MetricAggregationIn"])
    types["GoogleCloudApigeeV1MetricAggregationOut"] = t.struct(
        {
            "order": t.string().optional(),
            "aggregation": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1MetricAggregationOut"])
    types["GoogleCloudApigeeV1DeleteCustomReportResponseIn"] = t.struct(
        {"message": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1DeleteCustomReportResponseIn"])
    types["GoogleCloudApigeeV1DeleteCustomReportResponseOut"] = t.struct(
        {
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeleteCustomReportResponseOut"])
    types["GoogleCloudApigeeV1ListTraceConfigOverridesResponseIn"] = t.struct(
        {
            "traceConfigOverrides": t.array(
                t.proxy(renames["GoogleCloudApigeeV1TraceConfigOverrideIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListTraceConfigOverridesResponseIn"])
    types["GoogleCloudApigeeV1ListTraceConfigOverridesResponseOut"] = t.struct(
        {
            "traceConfigOverrides": t.array(
                t.proxy(renames["GoogleCloudApigeeV1TraceConfigOverrideOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListTraceConfigOverridesResponseOut"])
    types["GoogleCloudApigeeV1QueryIn"] = t.struct(
        {
            "timeRange": t.struct({"_": t.string().optional()}),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1QueryMetricIn"])
            ).optional(),
            "name": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "filter": t.string().optional(),
            "groupByTimeUnit": t.string().optional(),
            "envgroupHostname": t.string().optional(),
            "limit": t.integer().optional(),
            "outputFormat": t.string().optional(),
            "csvDelimiter": t.string().optional(),
            "reportDefinitionId": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryIn"])
    types["GoogleCloudApigeeV1QueryOut"] = t.struct(
        {
            "timeRange": t.struct({"_": t.string().optional()}),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1QueryMetricOut"])
            ).optional(),
            "name": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "filter": t.string().optional(),
            "groupByTimeUnit": t.string().optional(),
            "envgroupHostname": t.string().optional(),
            "limit": t.integer().optional(),
            "outputFormat": t.string().optional(),
            "csvDelimiter": t.string().optional(),
            "reportDefinitionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryOut"])
    types["GoogleCloudApigeeV1CommonNameConfigIn"] = t.struct(
        {"matchWildCards": t.boolean(), "name": t.string()}
    ).named(renames["GoogleCloudApigeeV1CommonNameConfigIn"])
    types["GoogleCloudApigeeV1CommonNameConfigOut"] = t.struct(
        {
            "matchWildCards": t.boolean(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1CommonNameConfigOut"])
    types["GoogleIamV1SetIamPolicyRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
        }
    ).named(renames["GoogleIamV1SetIamPolicyRequestIn"])
    types["GoogleIamV1SetIamPolicyRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["GoogleIamV1PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1SetIamPolicyRequestOut"])
    types["GoogleCloudApigeeV1CanaryEvaluationIn"] = t.struct(
        {
            "startTime": t.string(),
            "treatment": t.string(),
            "metricLabels": t.proxy(
                renames["GoogleCloudApigeeV1CanaryEvaluationMetricLabelsIn"]
            ),
            "control": t.string(),
            "endTime": t.string(),
        }
    ).named(renames["GoogleCloudApigeeV1CanaryEvaluationIn"])
    types["GoogleCloudApigeeV1CanaryEvaluationOut"] = t.struct(
        {
            "startTime": t.string(),
            "treatment": t.string(),
            "metricLabels": t.proxy(
                renames["GoogleCloudApigeeV1CanaryEvaluationMetricLabelsOut"]
            ),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "verdict": t.string().optional(),
            "control": t.string(),
            "endTime": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1CanaryEvaluationOut"])
    types["GoogleCloudApigeeV1DeveloperAppKeyIn"] = t.struct(
        {
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
            ).optional(),
            "consumerSecret": t.string().optional(),
            "apiProducts": t.array(t.struct({"_": t.string().optional()})).optional(),
            "status": t.string().optional(),
            "expiresAt": t.string().optional(),
            "expiresInSeconds": t.string().optional(),
            "consumerKey": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "issuedAt": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeveloperAppKeyIn"])
    types["GoogleCloudApigeeV1DeveloperAppKeyOut"] = t.struct(
        {
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeOut"])
            ).optional(),
            "consumerSecret": t.string().optional(),
            "apiProducts": t.array(t.struct({"_": t.string().optional()})).optional(),
            "status": t.string().optional(),
            "expiresAt": t.string().optional(),
            "expiresInSeconds": t.string().optional(),
            "consumerKey": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "issuedAt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeveloperAppKeyOut"])
    types["GoogleCloudApigeeV1DimensionMetricIn"] = t.struct(
        {
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1MetricIn"])
            ).optional(),
            "individualNames": t.array(t.string()).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DimensionMetricIn"])
    types["GoogleCloudApigeeV1DimensionMetricOut"] = t.struct(
        {
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1MetricOut"])
            ).optional(),
            "individualNames": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DimensionMetricOut"])
    types["GoogleCloudApigeeV1AdvancedApiOpsConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["GoogleCloudApigeeV1AdvancedApiOpsConfigIn"])
    types["GoogleCloudApigeeV1AdvancedApiOpsConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AdvancedApiOpsConfigOut"])
    types["GoogleCloudApigeeV1QueryMetadataIn"] = t.struct(
        {
            "outputFormat": t.string().optional(),
            "timeUnit": t.string().optional(),
            "startTimestamp": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "endTimestamp": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryMetadataIn"])
    types["GoogleCloudApigeeV1QueryMetadataOut"] = t.struct(
        {
            "outputFormat": t.string().optional(),
            "timeUnit": t.string().optional(),
            "startTimestamp": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "endTimestamp": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryMetadataOut"])
    types["GoogleCloudApigeeV1EndpointAttachmentIn"] = t.struct(
        {
            "location": t.string(),
            "name": t.string().optional(),
            "serviceAttachment": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1EndpointAttachmentIn"])
    types["GoogleCloudApigeeV1EndpointAttachmentOut"] = t.struct(
        {
            "host": t.string().optional(),
            "location": t.string(),
            "name": t.string().optional(),
            "connectionState": t.string().optional(),
            "state": t.string().optional(),
            "serviceAttachment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1EndpointAttachmentOut"])
    types["GoogleCloudApigeeV1TargetServerConfigIn"] = t.struct(
        {
            "port": t.integer().optional(),
            "host": t.string().optional(),
            "enabled": t.boolean().optional(),
            "protocol": t.string().optional(),
            "tlsInfo": t.proxy(
                renames["GoogleCloudApigeeV1TlsInfoConfigIn"]
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1TargetServerConfigIn"])
    types["GoogleCloudApigeeV1TargetServerConfigOut"] = t.struct(
        {
            "port": t.integer().optional(),
            "host": t.string().optional(),
            "enabled": t.boolean().optional(),
            "protocol": t.string().optional(),
            "tlsInfo": t.proxy(
                renames["GoogleCloudApigeeV1TlsInfoConfigOut"]
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1TargetServerConfigOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleCloudApigeeV1SecurityReportQueryMetricIn"] = t.struct(
        {
            "aggregationFunction": t.string().optional(),
            "value": t.string().optional(),
            "operator": t.string().optional(),
            "name": t.string(),
            "alias": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityReportQueryMetricIn"])
    types["GoogleCloudApigeeV1SecurityReportQueryMetricOut"] = t.struct(
        {
            "aggregationFunction": t.string().optional(),
            "value": t.string().optional(),
            "operator": t.string().optional(),
            "name": t.string(),
            "alias": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityReportQueryMetricOut"])
    types["GoogleCloudApigeeV1RevisionStatusIn"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "replicas": t.integer().optional(),
            "jsonSpec": t.string().optional(),
            "errors": t.array(
                t.proxy(renames["GoogleCloudApigeeV1UpdateErrorIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RevisionStatusIn"])
    types["GoogleCloudApigeeV1RevisionStatusOut"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "replicas": t.integer().optional(),
            "jsonSpec": t.string().optional(),
            "errors": t.array(
                t.proxy(renames["GoogleCloudApigeeV1UpdateErrorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RevisionStatusOut"])
    types["GoogleCloudApigeeV1ReportInstanceStatusRequestIn"] = t.struct(
        {
            "instanceUid": t.string().optional(),
            "reportTime": t.string().optional(),
            "resources": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ResourceStatusIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ReportInstanceStatusRequestIn"])
    types["GoogleCloudApigeeV1ReportInstanceStatusRequestOut"] = t.struct(
        {
            "instanceUid": t.string().optional(),
            "reportTime": t.string().optional(),
            "resources": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ResourceStatusOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ReportInstanceStatusRequestOut"])
    types["GoogleCloudApigeeV1ScoreComponentRecommendationActionIn"] = t.struct(
        {
            "actionContext": t.proxy(
                renames[
                    "GoogleCloudApigeeV1ScoreComponentRecommendationActionActionContextIn"
                ]
            ).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ScoreComponentRecommendationActionIn"])
    types["GoogleCloudApigeeV1ScoreComponentRecommendationActionOut"] = t.struct(
        {
            "actionContext": t.proxy(
                renames[
                    "GoogleCloudApigeeV1ScoreComponentRecommendationActionActionContextOut"
                ]
            ).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ScoreComponentRecommendationActionOut"])
    types["GoogleCloudApigeeV1SubscriptionIn"] = t.struct(
        {"name": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1SubscriptionIn"])
    types["GoogleCloudApigeeV1SubscriptionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SubscriptionOut"])
    types["GoogleCloudApigeeV1FlowHookIn"] = t.struct(
        {
            "sharedFlow": t.string().optional(),
            "continueOnError": t.boolean().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1FlowHookIn"])
    types["GoogleCloudApigeeV1FlowHookOut"] = t.struct(
        {
            "flowHookPoint": t.string().optional(),
            "sharedFlow": t.string().optional(),
            "continueOnError": t.boolean().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1FlowHookOut"])
    types["GoogleCloudApigeeV1ListSecurityProfileRevisionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "securityProfiles": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SecurityProfileIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListSecurityProfileRevisionsResponseIn"])
    types["GoogleCloudApigeeV1ListSecurityProfileRevisionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "securityProfiles": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SecurityProfileOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListSecurityProfileRevisionsResponseOut"])
    types["GoogleCloudApigeeV1ProvisionOrganizationRequestIn"] = t.struct(
        {
            "runtimeLocation": t.string().optional(),
            "authorizedNetwork": t.string().optional(),
            "analyticsRegion": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ProvisionOrganizationRequestIn"])
    types["GoogleCloudApigeeV1ProvisionOrganizationRequestOut"] = t.struct(
        {
            "runtimeLocation": t.string().optional(),
            "authorizedNetwork": t.string().optional(),
            "analyticsRegion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ProvisionOrganizationRequestOut"])
    types["GoogleCloudApigeeV1SetAddonsRequestIn"] = t.struct(
        {"addonsConfig": t.proxy(renames["GoogleCloudApigeeV1AddonsConfigIn"])}
    ).named(renames["GoogleCloudApigeeV1SetAddonsRequestIn"])
    types["GoogleCloudApigeeV1SetAddonsRequestOut"] = t.struct(
        {
            "addonsConfig": t.proxy(renames["GoogleCloudApigeeV1AddonsConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SetAddonsRequestOut"])
    types["GoogleCloudApigeeV1ListDatastoresResponseIn"] = t.struct(
        {
            "datastores": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DatastoreIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudApigeeV1ListDatastoresResponseIn"])
    types["GoogleCloudApigeeV1ListDatastoresResponseOut"] = t.struct(
        {
            "datastores": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DatastoreOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListDatastoresResponseOut"])
    types["GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilterIn"] = t.struct(
        {"scorePath": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilterIn"])
    types["GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilterOut"] = t.struct(
        {
            "scorePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilterOut"])
    types["GoogleCloudApigeeV1RuntimeTraceConfigIn"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "endpoint": t.string().optional(),
            "samplingConfig": t.proxy(
                renames["GoogleCloudApigeeV1RuntimeTraceSamplingConfigIn"]
            ).optional(),
            "name": t.string().optional(),
            "overrides": t.array(
                t.proxy(renames["GoogleCloudApigeeV1RuntimeTraceConfigOverrideIn"])
            ).optional(),
            "exporter": t.string().optional(),
            "revisionCreateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RuntimeTraceConfigIn"])
    types["GoogleCloudApigeeV1RuntimeTraceConfigOut"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "endpoint": t.string().optional(),
            "samplingConfig": t.proxy(
                renames["GoogleCloudApigeeV1RuntimeTraceSamplingConfigOut"]
            ).optional(),
            "name": t.string().optional(),
            "overrides": t.array(
                t.proxy(renames["GoogleCloudApigeeV1RuntimeTraceConfigOverrideOut"])
            ).optional(),
            "exporter": t.string().optional(),
            "revisionCreateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RuntimeTraceConfigOut"])
    types["GoogleCloudApigeeV1AccessRemoveIn"] = t.struct(
        {"name": t.string(), "success": t.boolean()}
    ).named(renames["GoogleCloudApigeeV1AccessRemoveIn"])
    types["GoogleCloudApigeeV1AccessRemoveOut"] = t.struct(
        {
            "name": t.string(),
            "success": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AccessRemoveOut"])
    types["GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponseIn"] = t.struct(
        {
            "environmentGroupAttachments": t.array(
                t.proxy(renames["GoogleCloudApigeeV1EnvironmentGroupAttachmentIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponseIn"])
    types["GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponseOut"] = t.struct(
        {
            "environmentGroupAttachments": t.array(
                t.proxy(renames["GoogleCloudApigeeV1EnvironmentGroupAttachmentOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponseOut"])
    types["GoogleCloudApigeeV1RuntimeTraceConfigOverrideIn"] = t.struct(
        {
            "revisionCreateTime": t.string().optional(),
            "uid": t.string().optional(),
            "samplingConfig": t.proxy(
                renames["GoogleCloudApigeeV1RuntimeTraceSamplingConfigIn"]
            ).optional(),
            "name": t.string().optional(),
            "revisionId": t.string().optional(),
            "apiProxy": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RuntimeTraceConfigOverrideIn"])
    types["GoogleCloudApigeeV1RuntimeTraceConfigOverrideOut"] = t.struct(
        {
            "revisionCreateTime": t.string().optional(),
            "uid": t.string().optional(),
            "samplingConfig": t.proxy(
                renames["GoogleCloudApigeeV1RuntimeTraceSamplingConfigOut"]
            ).optional(),
            "name": t.string().optional(),
            "revisionId": t.string().optional(),
            "apiProxy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RuntimeTraceConfigOverrideOut"])
    types["GoogleCloudApigeeV1QuotaIn"] = t.struct(
        {"interval": t.string(), "timeUnit": t.string().optional(), "limit": t.string()}
    ).named(renames["GoogleCloudApigeeV1QuotaIn"])
    types["GoogleCloudApigeeV1QuotaOut"] = t.struct(
        {
            "interval": t.string(),
            "timeUnit": t.string().optional(),
            "limit": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QuotaOut"])
    types["GoogleCloudApigeeV1SecurityProfileEnvironmentAssociationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "securityProfileRevisionId": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityProfileEnvironmentAssociationIn"])
    types["GoogleCloudApigeeV1SecurityProfileEnvironmentAssociationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "securityProfileRevisionId": t.string().optional(),
            "attachTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityProfileEnvironmentAssociationOut"])
    types["GoogleCloudApigeeV1AppGroupIn"] = t.struct(
        {
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
            ).optional(),
            "status": t.string().optional(),
            "name": t.string().optional(),
            "channelId": t.string().optional(),
            "displayName": t.string().optional(),
            "channelUri": t.string().optional(),
            "organization": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AppGroupIn"])
    types["GoogleCloudApigeeV1AppGroupOut"] = t.struct(
        {
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeOut"])
            ).optional(),
            "appGroupId": t.string().optional(),
            "lastModifiedAt": t.string().optional(),
            "status": t.string().optional(),
            "createdAt": t.string().optional(),
            "name": t.string().optional(),
            "channelId": t.string().optional(),
            "displayName": t.string().optional(),
            "channelUri": t.string().optional(),
            "organization": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AppGroupOut"])
    types["GoogleCloudApigeeV1SecurityIncidentIn"] = t.struct(
        {
            "trafficCount": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityIncidentIn"])
    types["GoogleCloudApigeeV1SecurityIncidentOut"] = t.struct(
        {
            "riskLevel": t.string().optional(),
            "lastDetectedTime": t.string().optional(),
            "detectionTypes": t.array(t.string()).optional(),
            "trafficCount": t.string().optional(),
            "firstDetectedTime": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityIncidentOut"])
    types["GoogleCloudApigeeV1RevenueShareRangeIn"] = t.struct(
        {
            "start": t.string().optional(),
            "end": t.string().optional(),
            "sharePercentage": t.number().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RevenueShareRangeIn"])
    types["GoogleCloudApigeeV1RevenueShareRangeOut"] = t.struct(
        {
            "start": t.string().optional(),
            "end": t.string().optional(),
            "sharePercentage": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RevenueShareRangeOut"])
    types["GoogleCloudApigeeV1APIProductAssociationIn"] = t.struct(
        {"apiproduct": t.string().optional(), "status": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1APIProductAssociationIn"])
    types["GoogleCloudApigeeV1APIProductAssociationOut"] = t.struct(
        {
            "apiproduct": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1APIProductAssociationOut"])
    types["GoogleCloudApigeeV1QueryTimeSeriesStatsRequestIn"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "timeRange": t.proxy(renames["GoogleTypeIntervalIn"]),
            "timestampOrder": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "filter": t.string().optional(),
            "pageToken": t.string().optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1MetricAggregationIn"])
            ),
            "windowSize": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryTimeSeriesStatsRequestIn"])
    types["GoogleCloudApigeeV1QueryTimeSeriesStatsRequestOut"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "timeRange": t.proxy(renames["GoogleTypeIntervalOut"]),
            "timestampOrder": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "filter": t.string().optional(),
            "pageToken": t.string().optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1MetricAggregationOut"])
            ),
            "windowSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryTimeSeriesStatsRequestOut"])
    types["GoogleCloudApigeeV1ComputeEnvironmentScoresResponseIn"] = t.struct(
        {
            "scores": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ScoreIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ComputeEnvironmentScoresResponseIn"])
    types["GoogleCloudApigeeV1ComputeEnvironmentScoresResponseOut"] = t.struct(
        {
            "scores": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ScoreOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ComputeEnvironmentScoresResponseOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudApigeeV1AttributeIn"] = t.struct(
        {"name": t.string().optional(), "value": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1AttributeIn"])
    types["GoogleCloudApigeeV1AttributeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AttributeOut"])
    types["GoogleCloudApigeeV1ApiSecurityConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["GoogleCloudApigeeV1ApiSecurityConfigIn"])
    types["GoogleCloudApigeeV1ApiSecurityConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "expiresAt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ApiSecurityConfigOut"])
    types["GoogleCloudApigeeV1ResourceFileIn"] = t.struct(
        {"name": t.string().optional(), "type": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1ResourceFileIn"])
    types["GoogleCloudApigeeV1ResourceFileOut"] = t.struct(
        {
            "name": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ResourceFileOut"])
    types["GoogleCloudApigeeV1ListAppGroupsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "appGroups": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AppGroupIn"])
            ).optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListAppGroupsResponseIn"])
    types["GoogleCloudApigeeV1ListAppGroupsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "appGroups": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AppGroupOut"])
            ).optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListAppGroupsResponseOut"])
    types["GoogleCloudApigeeV1KeyValueEntryIn"] = t.struct(
        {"name": t.string().optional(), "value": t.string()}
    ).named(renames["GoogleCloudApigeeV1KeyValueEntryIn"])
    types["GoogleCloudApigeeV1KeyValueEntryOut"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1KeyValueEntryOut"])
    types["GoogleCloudApigeeV1ReferenceIn"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "name": t.string(),
            "refers": t.string(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ReferenceIn"])
    types["GoogleCloudApigeeV1ReferenceOut"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "name": t.string(),
            "refers": t.string(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ReferenceOut"])
    types["GoogleCloudApigeeV1AdjustDeveloperBalanceRequestIn"] = t.struct(
        {"adjustment": t.proxy(renames["GoogleTypeMoneyIn"]).optional()}
    ).named(renames["GoogleCloudApigeeV1AdjustDeveloperBalanceRequestIn"])
    types["GoogleCloudApigeeV1AdjustDeveloperBalanceRequestOut"] = t.struct(
        {
            "adjustment": t.proxy(renames["GoogleTypeMoneyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AdjustDeveloperBalanceRequestOut"])
    types["GoogleCloudApigeeV1ApiProductRefIn"] = t.struct(
        {"apiproduct": t.string().optional(), "status": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1ApiProductRefIn"])
    types["GoogleCloudApigeeV1ApiProductRefOut"] = t.struct(
        {
            "apiproduct": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ApiProductRefOut"])
    types["GoogleIamV1AuditLogConfigIn"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIamV1AuditLogConfigIn"])
    types["GoogleIamV1AuditLogConfigOut"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1AuditLogConfigOut"])
    types["GoogleCloudApigeeV1NodeConfigIn"] = t.struct(
        {"maxNodeCount": t.string().optional(), "minNodeCount": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1NodeConfigIn"])
    types["GoogleCloudApigeeV1NodeConfigOut"] = t.struct(
        {
            "currentAggregateNodeCount": t.string().optional(),
            "maxNodeCount": t.string().optional(),
            "minNodeCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1NodeConfigOut"])
    types["GoogleCloudApigeeV1DatastoreIn"] = t.struct(
        {
            "targetType": t.string().optional(),
            "displayName": t.string(),
            "datastoreConfig": t.proxy(
                renames["GoogleCloudApigeeV1DatastoreConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DatastoreIn"])
    types["GoogleCloudApigeeV1DatastoreOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "org": t.string().optional(),
            "targetType": t.string().optional(),
            "displayName": t.string(),
            "self": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "datastoreConfig": t.proxy(
                renames["GoogleCloudApigeeV1DatastoreConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DatastoreOut"])
    types["GoogleCloudApigeeV1OrganizationIn"] = t.struct(
        {
            "controlPlaneEncryptionKeyName": t.string().optional(),
            "attributes": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "apiConsumerDataLocation": t.string().optional(),
            "runtimeType": t.string(),
            "runtimeDatabaseEncryptionKeyName": t.string().optional(),
            "authorizedNetwork": t.string().optional(),
            "apiConsumerDataEncryptionKeyName": t.string().optional(),
            "analyticsRegion": t.string(),
            "portalDisabled": t.boolean().optional(),
            "billingType": t.string().optional(),
            "properties": t.proxy(
                renames["GoogleCloudApigeeV1PropertiesIn"]
            ).optional(),
            "addonsConfig": t.proxy(
                renames["GoogleCloudApigeeV1AddonsConfigIn"]
            ).optional(),
            "customerName": t.string().optional(),
            "type": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OrganizationIn"])
    types["GoogleCloudApigeeV1OrganizationOut"] = t.struct(
        {
            "state": t.string().optional(),
            "environments": t.array(t.string()).optional(),
            "controlPlaneEncryptionKeyName": t.string().optional(),
            "caCertificate": t.string().optional(),
            "attributes": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "expiresAt": t.string().optional(),
            "name": t.string().optional(),
            "apiConsumerDataLocation": t.string().optional(),
            "lastModifiedAt": t.string().optional(),
            "runtimeType": t.string(),
            "subscriptionType": t.string().optional(),
            "runtimeDatabaseEncryptionKeyName": t.string().optional(),
            "authorizedNetwork": t.string().optional(),
            "createdAt": t.string().optional(),
            "apiConsumerDataEncryptionKeyName": t.string().optional(),
            "analyticsRegion": t.string(),
            "portalDisabled": t.boolean().optional(),
            "billingType": t.string().optional(),
            "apigeeProjectId": t.string().optional(),
            "properties": t.proxy(
                renames["GoogleCloudApigeeV1PropertiesOut"]
            ).optional(),
            "addonsConfig": t.proxy(
                renames["GoogleCloudApigeeV1AddonsConfigOut"]
            ).optional(),
            "customerName": t.string().optional(),
            "type": t.string().optional(),
            "description": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OrganizationOut"])
    types["GoogleTypeExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleTypeExprIn"])
    types["GoogleTypeExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeExprOut"])
    types["GoogleCloudApigeeV1QueryMetricIn"] = t.struct(
        {
            "name": t.string(),
            "value": t.string().optional(),
            "alias": t.string().optional(),
            "operator": t.string().optional(),
            "function": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryMetricIn"])
    types["GoogleCloudApigeeV1QueryMetricOut"] = t.struct(
        {
            "name": t.string(),
            "value": t.string().optional(),
            "alias": t.string().optional(),
            "operator": t.string().optional(),
            "function": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryMetricOut"])
    types["GoogleCloudApigeeV1ListApiProxiesResponseIn"] = t.struct(
        {"proxies": t.array(t.proxy(renames["GoogleCloudApigeeV1ApiProxyIn"]))}
    ).named(renames["GoogleCloudApigeeV1ListApiProxiesResponseIn"])
    types["GoogleCloudApigeeV1ListApiProxiesResponseOut"] = t.struct(
        {
            "proxies": t.array(t.proxy(renames["GoogleCloudApigeeV1ApiProxyOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListApiProxiesResponseOut"])
    types["GoogleCloudApigeeV1UpdateAppGroupAppKeyRequestIn"] = t.struct(
        {
            "apiProducts": t.array(t.string()).optional(),
            "appGroupAppKey": t.proxy(
                renames["GoogleCloudApigeeV1AppGroupAppKeyIn"]
            ).optional(),
            "action": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1UpdateAppGroupAppKeyRequestIn"])
    types["GoogleCloudApigeeV1UpdateAppGroupAppKeyRequestOut"] = t.struct(
        {
            "apiProducts": t.array(t.string()).optional(),
            "appGroupAppKey": t.proxy(
                renames["GoogleCloudApigeeV1AppGroupAppKeyOut"]
            ).optional(),
            "action": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1UpdateAppGroupAppKeyRequestOut"])
    types["GoogleCloudApigeeV1KeystoreConfigIn"] = t.struct(
        {
            "aliases": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AliasRevisionConfigIn"])
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1KeystoreConfigIn"])
    types["GoogleCloudApigeeV1KeystoreConfigOut"] = t.struct(
        {
            "aliases": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AliasRevisionConfigOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1KeystoreConfigOut"])
    types["GoogleCloudApigeeV1CustomReportMetricIn"] = t.struct(
        {"function": t.string().optional(), "name": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1CustomReportMetricIn"])
    types["GoogleCloudApigeeV1CustomReportMetricOut"] = t.struct(
        {
            "function": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1CustomReportMetricOut"])
    types["GoogleCloudApigeeV1DeploymentGroupConfigIn"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "name": t.string().optional(),
            "uid": t.string().optional(),
            "deploymentGroupType": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentGroupConfigIn"])
    types["GoogleCloudApigeeV1DeploymentGroupConfigOut"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "name": t.string().optional(),
            "uid": t.string().optional(),
            "deploymentGroupType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentGroupConfigOut"])
    types["GoogleCloudApigeeV1IntegrationConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["GoogleCloudApigeeV1IntegrationConfigIn"])
    types["GoogleCloudApigeeV1IntegrationConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1IntegrationConfigOut"])
    types["GoogleCloudApigeeV1DeveloperIn"] = t.struct(
        {
            "email": t.string(),
            "companies": t.array(t.string()).optional(),
            "userName": t.string(),
            "firstName": t.string(),
            "lastName": t.string(),
            "appFamily": t.string().optional(),
            "accessType": t.string().optional(),
            "developerId": t.string().optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
            ).optional(),
            "apps": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeveloperIn"])
    types["GoogleCloudApigeeV1DeveloperOut"] = t.struct(
        {
            "email": t.string(),
            "companies": t.array(t.string()).optional(),
            "userName": t.string(),
            "firstName": t.string(),
            "status": t.string().optional(),
            "lastName": t.string(),
            "appFamily": t.string().optional(),
            "accessType": t.string().optional(),
            "createdAt": t.string().optional(),
            "lastModifiedAt": t.string().optional(),
            "developerId": t.string().optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeOut"])
            ).optional(),
            "apps": t.array(t.string()).optional(),
            "organizationName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeveloperOut"])
    types["GoogleCloudApigeeV1ServiceIssuersMappingIn"] = t.struct(
        {"emailIds": t.array(t.string()).optional(), "service": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1ServiceIssuersMappingIn"])
    types["GoogleCloudApigeeV1ServiceIssuersMappingOut"] = t.struct(
        {
            "emailIds": t.array(t.string()).optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ServiceIssuersMappingOut"])
    types["GoogleCloudApigeeV1ApiCategoryIn"] = t.struct(
        {
            "status": t.string().optional(),
            "message": t.string().optional(),
            "data": t.proxy(renames["GoogleCloudApigeeV1ApiCategoryDataIn"]).optional(),
            "errorCode": t.string().optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ApiCategoryIn"])
    types["GoogleCloudApigeeV1ApiCategoryOut"] = t.struct(
        {
            "status": t.string().optional(),
            "message": t.string().optional(),
            "data": t.proxy(
                renames["GoogleCloudApigeeV1ApiCategoryDataOut"]
            ).optional(),
            "errorCode": t.string().optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ApiCategoryOut"])
    types["GoogleCloudApigeeV1ResourceConfigIn"] = t.struct(
        {"name": t.string().optional(), "location": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1ResourceConfigIn"])
    types["GoogleCloudApigeeV1ResourceConfigOut"] = t.struct(
        {
            "name": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ResourceConfigOut"])
    types["GoogleCloudApigeeV1ListOrganizationsResponseIn"] = t.struct(
        {
            "organizations": t.array(
                t.proxy(renames["GoogleCloudApigeeV1OrganizationProjectMappingIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudApigeeV1ListOrganizationsResponseIn"])
    types["GoogleCloudApigeeV1ListOrganizationsResponseOut"] = t.struct(
        {
            "organizations": t.array(
                t.proxy(renames["GoogleCloudApigeeV1OrganizationProjectMappingOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListOrganizationsResponseOut"])
    types["EdgeConfigstoreBundleBadBundleIn"] = t.struct(
        {
            "violations": t.array(
                t.proxy(renames["EdgeConfigstoreBundleBadBundleViolationIn"])
            ).optional()
        }
    ).named(renames["EdgeConfigstoreBundleBadBundleIn"])
    types["EdgeConfigstoreBundleBadBundleOut"] = t.struct(
        {
            "violations": t.array(
                t.proxy(renames["EdgeConfigstoreBundleBadBundleViolationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EdgeConfigstoreBundleBadBundleOut"])
    types["GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRevisionIn"] = t.struct(
        {"revision": t.string().optional(), "percentage": t.integer().optional()}
    ).named(renames["GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRevisionIn"])
    types["GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRevisionOut"] = t.struct(
        {
            "revision": t.string().optional(),
            "percentage": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRevisionOut"])
    types["GoogleCloudApigeeV1ListAppGroupAppsResponseIn"] = t.struct(
        {
            "appGroupApps": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AppGroupAppIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListAppGroupAppsResponseIn"])
    types["GoogleCloudApigeeV1ListAppGroupAppsResponseOut"] = t.struct(
        {
            "appGroupApps": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AppGroupAppOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListAppGroupAppsResponseOut"])
    types["GoogleCloudApigeeV1ListApiProductsResponseIn"] = t.struct(
        {
            "apiProduct": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ApiProductIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudApigeeV1ListApiProductsResponseIn"])
    types["GoogleCloudApigeeV1ListApiProductsResponseOut"] = t.struct(
        {
            "apiProduct": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ApiProductOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListApiProductsResponseOut"])
    types["GoogleCloudApigeeV1IngressConfigIn"] = t.struct(
        {
            "environmentGroups": t.array(
                t.proxy(renames["GoogleCloudApigeeV1EnvironmentGroupConfigIn"])
            ).optional(),
            "revisionCreateTime": t.string().optional(),
            "revisionId": t.string().optional(),
            "uid": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1IngressConfigIn"])
    types["GoogleCloudApigeeV1IngressConfigOut"] = t.struct(
        {
            "environmentGroups": t.array(
                t.proxy(renames["GoogleCloudApigeeV1EnvironmentGroupConfigOut"])
            ).optional(),
            "revisionCreateTime": t.string().optional(),
            "revisionId": t.string().optional(),
            "uid": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1IngressConfigOut"])
    types["GoogleCloudApigeeV1ReferenceConfigIn"] = t.struct(
        {"resourceName": t.string().optional(), "name": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1ReferenceConfigIn"])
    types["GoogleCloudApigeeV1ReferenceConfigOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ReferenceConfigOut"])
    types["GoogleCloudApigeeV1ExportRequestIn"] = t.struct(
        {
            "csvDelimiter": t.string().optional(),
            "dateRange": t.proxy(renames["GoogleCloudApigeeV1DateRangeIn"]),
            "description": t.string().optional(),
            "outputFormat": t.string().optional(),
            "datastoreName": t.string(),
            "name": t.string(),
        }
    ).named(renames["GoogleCloudApigeeV1ExportRequestIn"])
    types["GoogleCloudApigeeV1ExportRequestOut"] = t.struct(
        {
            "csvDelimiter": t.string().optional(),
            "dateRange": t.proxy(renames["GoogleCloudApigeeV1DateRangeOut"]),
            "description": t.string().optional(),
            "outputFormat": t.string().optional(),
            "datastoreName": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ExportRequestOut"])
    types["EdgeConfigstoreBundleBadBundleViolationIn"] = t.struct(
        {"description": t.string().optional(), "filename": t.string().optional()}
    ).named(renames["EdgeConfigstoreBundleBadBundleViolationIn"])
    types["EdgeConfigstoreBundleBadBundleViolationOut"] = t.struct(
        {
            "description": t.string().optional(),
            "filename": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EdgeConfigstoreBundleBadBundleViolationOut"])
    types["GoogleCloudApigeeV1ListDeveloperAppsResponseIn"] = t.struct(
        {
            "app": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DeveloperAppIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudApigeeV1ListDeveloperAppsResponseIn"])
    types["GoogleCloudApigeeV1ListDeveloperAppsResponseOut"] = t.struct(
        {
            "app": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DeveloperAppOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListDeveloperAppsResponseOut"])
    types["GoogleCloudApigeeV1OperationConfigIn"] = t.struct(
        {
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
            ).optional(),
            "apiSource": t.string(),
            "operations": t.array(
                t.proxy(renames["GoogleCloudApigeeV1OperationIn"])
            ).optional(),
            "quota": t.proxy(renames["GoogleCloudApigeeV1QuotaIn"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OperationConfigIn"])
    types["GoogleCloudApigeeV1OperationConfigOut"] = t.struct(
        {
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeOut"])
            ).optional(),
            "apiSource": t.string(),
            "operations": t.array(
                t.proxy(renames["GoogleCloudApigeeV1OperationOut"])
            ).optional(),
            "quota": t.proxy(renames["GoogleCloudApigeeV1QuotaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OperationConfigOut"])
    types["GoogleCloudApigeeV1DateRangeIn"] = t.struct(
        {"start": t.string(), "end": t.string()}
    ).named(renames["GoogleCloudApigeeV1DateRangeIn"])
    types["GoogleCloudApigeeV1DateRangeOut"] = t.struct(
        {
            "start": t.string(),
            "end": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DateRangeOut"])
    types["GoogleCloudApigeeV1DeveloperAppIn"] = t.struct(
        {
            "keyExpiresIn": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "appId": t.string().optional(),
            "developerId": t.string().optional(),
            "appFamily": t.string().optional(),
            "name": t.string().optional(),
            "callbackUrl": t.string().optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
            ).optional(),
            "apiProducts": t.array(t.string()).optional(),
            "status": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeveloperAppIn"])
    types["GoogleCloudApigeeV1DeveloperAppOut"] = t.struct(
        {
            "keyExpiresIn": t.string().optional(),
            "credentials": t.array(
                t.proxy(renames["GoogleCloudApigeeV1CredentialOut"])
            ).optional(),
            "scopes": t.array(t.string()).optional(),
            "appId": t.string().optional(),
            "lastModifiedAt": t.string().optional(),
            "developerId": t.string().optional(),
            "appFamily": t.string().optional(),
            "createdAt": t.string().optional(),
            "name": t.string().optional(),
            "callbackUrl": t.string().optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeOut"])
            ).optional(),
            "apiProducts": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeveloperAppOut"])
    types["GoogleCloudApigeeV1AccessGetIn"] = t.struct(
        {"name": t.string(), "value": t.string()}
    ).named(renames["GoogleCloudApigeeV1AccessGetIn"])
    types["GoogleCloudApigeeV1AccessGetOut"] = t.struct(
        {
            "name": t.string(),
            "value": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AccessGetOut"])
    types["GoogleCloudApigeeV1DeploymentChangeReportRoutingConflictIn"] = t.struct(
        {
            "environmentGroup": t.string().optional(),
            "conflictingDeployment": t.proxy(
                renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentIn"]
            ).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingConflictIn"])
    types["GoogleCloudApigeeV1DeploymentChangeReportRoutingConflictOut"] = t.struct(
        {
            "environmentGroup": t.string().optional(),
            "conflictingDeployment": t.proxy(
                renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentOut"]
            ).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingConflictOut"])
    types["GoogleCloudApigeeV1DebugSessionIn"] = t.struct(
        {
            "filter": t.string().optional(),
            "count": t.integer().optional(),
            "timeout": t.string().optional(),
            "name": t.string().optional(),
            "tracesize": t.integer().optional(),
            "validity": t.integer().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DebugSessionIn"])
    types["GoogleCloudApigeeV1DebugSessionOut"] = t.struct(
        {
            "filter": t.string().optional(),
            "count": t.integer().optional(),
            "timeout": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "tracesize": t.integer().optional(),
            "validity": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DebugSessionOut"])
    types["GoogleCloudApigeeV1ListDebugSessionsResponseIn"] = t.struct(
        {
            "sessions": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SessionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListDebugSessionsResponseIn"])
    types["GoogleCloudApigeeV1ListDebugSessionsResponseOut"] = t.struct(
        {
            "sessions": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SessionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListDebugSessionsResponseOut"])
    types["GoogleCloudApigeeV1AttributesIn"] = t.struct(
        {
            "attribute": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudApigeeV1AttributesIn"])
    types["GoogleCloudApigeeV1AttributesOut"] = t.struct(
        {
            "attribute": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AttributesOut"])
    types["GoogleCloudApigeeV1RuntimeTraceSamplingConfigIn"] = t.struct(
        {"sampler": t.string().optional(), "samplingRate": t.number().optional()}
    ).named(renames["GoogleCloudApigeeV1RuntimeTraceSamplingConfigIn"])
    types["GoogleCloudApigeeV1RuntimeTraceSamplingConfigOut"] = t.struct(
        {
            "sampler": t.string().optional(),
            "samplingRate": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RuntimeTraceSamplingConfigOut"])
    types["GoogleCloudApigeeV1DeploymentIn"] = t.struct(
        {
            "instances": t.array(
                t.proxy(renames["GoogleCloudApigeeV1InstanceDeploymentStatusIn"])
            ).optional(),
            "serviceAccount": t.string().optional(),
            "errors": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "state": t.string().optional(),
            "routeConflicts": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudApigeeV1DeploymentChangeReportRoutingConflictIn"
                    ]
                )
            ).optional(),
            "pods": t.array(
                t.proxy(renames["GoogleCloudApigeeV1PodStatusIn"])
            ).optional(),
            "revision": t.string().optional(),
            "apiProxy": t.string().optional(),
            "deployStartTime": t.string().optional(),
            "environment": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentIn"])
    types["GoogleCloudApigeeV1DeploymentOut"] = t.struct(
        {
            "instances": t.array(
                t.proxy(renames["GoogleCloudApigeeV1InstanceDeploymentStatusOut"])
            ).optional(),
            "serviceAccount": t.string().optional(),
            "errors": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "state": t.string().optional(),
            "routeConflicts": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudApigeeV1DeploymentChangeReportRoutingConflictOut"
                    ]
                )
            ).optional(),
            "pods": t.array(
                t.proxy(renames["GoogleCloudApigeeV1PodStatusOut"])
            ).optional(),
            "revision": t.string().optional(),
            "apiProxy": t.string().optional(),
            "deployStartTime": t.string().optional(),
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentOut"])
    types["GoogleCloudApigeeV1ListRatePlansResponseIn"] = t.struct(
        {
            "ratePlans": t.array(
                t.proxy(renames["GoogleCloudApigeeV1RatePlanIn"])
            ).optional(),
            "nextStartKey": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListRatePlansResponseIn"])
    types["GoogleCloudApigeeV1ListRatePlansResponseOut"] = t.struct(
        {
            "ratePlans": t.array(
                t.proxy(renames["GoogleCloudApigeeV1RatePlanOut"])
            ).optional(),
            "nextStartKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListRatePlansResponseOut"])
    types["GoogleCloudApigeeV1ApiCategoryDataIn"] = t.struct(
        {
            "siteId": t.string().optional(),
            "gcpResource": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ApiCategoryDataIn"])
    types["GoogleCloudApigeeV1ApiCategoryDataOut"] = t.struct(
        {
            "siteId": t.string().optional(),
            "gcpResource": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ApiCategoryDataOut"])
    types["GoogleCloudApigeeV1DebugMaskIn"] = t.struct(
        {
            "name": t.string().optional(),
            "faultJSONPaths": t.array(t.string()).optional(),
            "variables": t.array(t.string()).optional(),
            "requestXPaths": t.array(t.string()).optional(),
            "namespaces": t.struct({"_": t.string().optional()}).optional(),
            "faultXPaths": t.array(t.string()).optional(),
            "requestJSONPaths": t.array(t.string()).optional(),
            "responseJSONPaths": t.array(t.string()).optional(),
            "responseXPaths": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DebugMaskIn"])
    types["GoogleCloudApigeeV1DebugMaskOut"] = t.struct(
        {
            "name": t.string().optional(),
            "faultJSONPaths": t.array(t.string()).optional(),
            "variables": t.array(t.string()).optional(),
            "requestXPaths": t.array(t.string()).optional(),
            "namespaces": t.struct({"_": t.string().optional()}).optional(),
            "faultXPaths": t.array(t.string()).optional(),
            "requestJSONPaths": t.array(t.string()).optional(),
            "responseJSONPaths": t.array(t.string()).optional(),
            "responseXPaths": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DebugMaskOut"])
    types["GoogleCloudApigeeV1TlsInfoCommonNameIn"] = t.struct(
        {"value": t.string().optional(), "wildcardMatch": t.boolean().optional()}
    ).named(renames["GoogleCloudApigeeV1TlsInfoCommonNameIn"])
    types["GoogleCloudApigeeV1TlsInfoCommonNameOut"] = t.struct(
        {
            "value": t.string().optional(),
            "wildcardMatch": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1TlsInfoCommonNameOut"])

    functions = {}
    functions["hybridIssuersList"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ListHybridIssuersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGetDeployedIngressConfig"] = apigee.post(
        "v1/{name}:setSyncAuthorization",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "identities": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1SyncAuthorizationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGetSyncAuthorization"] = apigee.post(
        "v1/{name}:setSyncAuthorization",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "identities": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1SyncAuthorizationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGetRuntimeConfig"] = apigee.post(
        "v1/{name}:setSyncAuthorization",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "identities": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1SyncAuthorizationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGetProjectMapping"] = apigee.post(
        "v1/{name}:setSyncAuthorization",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "identities": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1SyncAuthorizationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsUpdate"] = apigee.post(
        "v1/{name}:setSyncAuthorization",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "identities": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1SyncAuthorizationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsCreate"] = apigee.post(
        "v1/{name}:setSyncAuthorization",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "identities": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1SyncAuthorizationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDelete"] = apigee.post(
        "v1/{name}:setSyncAuthorization",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "identities": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1SyncAuthorizationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsList"] = apigee.post(
        "v1/{name}:setSyncAuthorization",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "identities": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1SyncAuthorizationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGet"] = apigee.post(
        "v1/{name}:setSyncAuthorization",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "identities": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1SyncAuthorizationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSetAddons"] = apigee.post(
        "v1/{name}:setSyncAuthorization",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "identities": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1SyncAuthorizationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSetSyncAuthorization"] = apigee.post(
        "v1/{name}:setSyncAuthorization",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "identities": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1SyncAuthorizationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsOperationsGet"] = apigee.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsOperationsList"] = apigee.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsKeyvaluemapsCreate"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1KeyValueMapOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsKeyvaluemapsDelete"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1KeyValueMapOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsKeyvaluemapsEntriesGet"] = apigee.post(
        "v1/{parent}/entries",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "value": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1KeyValueEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsKeyvaluemapsEntriesList"] = apigee.post(
        "v1/{parent}/entries",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "value": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1KeyValueEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsKeyvaluemapsEntriesDelete"] = apigee.post(
        "v1/{parent}/entries",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "value": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1KeyValueEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsKeyvaluemapsEntriesCreate"] = apigee.post(
        "v1/{parent}/entries",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "value": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1KeyValueEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvgroupsList"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvgroupsGet"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvgroupsGetDeployedIngressConfig"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvgroupsPatch"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvgroupsCreate"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvgroupsDelete"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvgroupsAttachmentsList"] = apigee.post(
        "v1/{parent}/attachments",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "environment": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvgroupsAttachmentsGet"] = apigee.post(
        "v1/{parent}/attachments",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "environment": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvgroupsAttachmentsDelete"] = apigee.post(
        "v1/{parent}/attachments",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "environment": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvgroupsAttachmentsCreate"] = apigee.post(
        "v1/{parent}/attachments",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "environment": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisList"] = apigee.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ApiProxyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisDelete"] = apigee.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ApiProxyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisGet"] = apigee.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ApiProxyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisCreate"] = apigee.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ApiProxyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisPatch"] = apigee.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ApiProxyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisKeyvaluemapsDelete"] = apigee.post(
        "v1/{parent}/keyvaluemaps",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string(),
                "encrypted": t.boolean(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1KeyValueMapOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisKeyvaluemapsCreate"] = apigee.post(
        "v1/{parent}/keyvaluemaps",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string(),
                "encrypted": t.boolean(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1KeyValueMapOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisKeyvaluemapsEntriesDelete"] = apigee.get(
        "v1/{parent}/entries",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListKeyValueEntriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisKeyvaluemapsEntriesCreate"] = apigee.get(
        "v1/{parent}/entries",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListKeyValueEntriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisKeyvaluemapsEntriesGet"] = apigee.get(
        "v1/{parent}/entries",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListKeyValueEntriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisKeyvaluemapsEntriesList"] = apigee.get(
        "v1/{parent}/entries",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListKeyValueEntriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisDeploymentsList"] = apigee.get(
        "v1/{parent}/deployments",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisRevisionsUpdateApiProxyRevision"] = apigee.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "format": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleApiHttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisRevisionsDelete"] = apigee.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "format": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleApiHttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisRevisionsGet"] = apigee.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "format": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleApiHttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisRevisionsDeploymentsList"] = apigee.get(
        "v1/{parent}/deployments",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSitesApicategoriesCreate"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ApiCategoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSitesApicategoriesList"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ApiCategoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSitesApicategoriesDelete"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ApiCategoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSitesApicategoriesPatch"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ApiCategoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSitesApicategoriesGet"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ApiCategoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAnalyticsDatastoresUpdate"] = apigee.post(
        "v1/{parent}/analytics/datastores:test",
        t.struct(
            {
                "parent": t.string(),
                "targetType": t.string().optional(),
                "displayName": t.string(),
                "datastoreConfig": t.proxy(
                    renames["GoogleCloudApigeeV1DatastoreConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1TestDatastoreResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAnalyticsDatastoresDelete"] = apigee.post(
        "v1/{parent}/analytics/datastores:test",
        t.struct(
            {
                "parent": t.string(),
                "targetType": t.string().optional(),
                "displayName": t.string(),
                "datastoreConfig": t.proxy(
                    renames["GoogleCloudApigeeV1DatastoreConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1TestDatastoreResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAnalyticsDatastoresGet"] = apigee.post(
        "v1/{parent}/analytics/datastores:test",
        t.struct(
            {
                "parent": t.string(),
                "targetType": t.string().optional(),
                "displayName": t.string(),
                "datastoreConfig": t.proxy(
                    renames["GoogleCloudApigeeV1DatastoreConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1TestDatastoreResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAnalyticsDatastoresList"] = apigee.post(
        "v1/{parent}/analytics/datastores:test",
        t.struct(
            {
                "parent": t.string(),
                "targetType": t.string().optional(),
                "displayName": t.string(),
                "datastoreConfig": t.proxy(
                    renames["GoogleCloudApigeeV1DatastoreConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1TestDatastoreResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAnalyticsDatastoresCreate"] = apigee.post(
        "v1/{parent}/analytics/datastores:test",
        t.struct(
            {
                "parent": t.string(),
                "targetType": t.string().optional(),
                "displayName": t.string(),
                "datastoreConfig": t.proxy(
                    renames["GoogleCloudApigeeV1DatastoreConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1TestDatastoreResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAnalyticsDatastoresTest"] = apigee.post(
        "v1/{parent}/analytics/datastores:test",
        t.struct(
            {
                "parent": t.string(),
                "targetType": t.string().optional(),
                "displayName": t.string(),
                "datastoreConfig": t.proxy(
                    renames["GoogleCloudApigeeV1DatastoreConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1TestDatastoreResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsUpdateDebugmask"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsCreate"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsSubscribe"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsSetIamPolicy"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsUpdateEnvironment"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsGetDeployedConfig"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsGetDebugmask"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsUpdateTraceConfig"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsTestIamPermissions"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsGetIamPolicy"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsGetTraceConfig"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsGetApiSecurityRuntimeConfig"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsDelete"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsModifyEnvironment"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsUnsubscribe"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsUpdate"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsGet"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsEnvironmentsResourcefilesListEnvironmentResources"
    ] = apigee.post(
        "v1/{parent}/resourcefiles",
        t.struct(
            {
                "type": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "data": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ResourceFileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsResourcefilesUpdate"] = apigee.post(
        "v1/{parent}/resourcefiles",
        t.struct(
            {
                "type": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "data": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ResourceFileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsResourcefilesList"] = apigee.post(
        "v1/{parent}/resourcefiles",
        t.struct(
            {
                "type": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "data": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ResourceFileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsResourcefilesGet"] = apigee.post(
        "v1/{parent}/resourcefiles",
        t.struct(
            {
                "type": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "data": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ResourceFileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsResourcefilesDelete"] = apigee.post(
        "v1/{parent}/resourcefiles",
        t.struct(
            {
                "type": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "data": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ResourceFileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsResourcefilesCreate"] = apigee.post(
        "v1/{parent}/resourcefiles",
        t.struct(
            {
                "type": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "data": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ResourceFileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsEnvironmentsFlowhooksDetachSharedFlowFromFlowHook"
    ] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1FlowHookOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsEnvironmentsFlowhooksAttachSharedFlowToFlowHook"
    ] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1FlowHookOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsFlowhooksGet"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1FlowHookOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsTraceConfigOverridesGet"] = apigee.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "apiProxy": t.string().optional(),
                "samplingConfig": t.proxy(
                    renames["GoogleCloudApigeeV1TraceSamplingConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1TraceConfigOverrideOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsTraceConfigOverridesList"] = apigee.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "apiProxy": t.string().optional(),
                "samplingConfig": t.proxy(
                    renames["GoogleCloudApigeeV1TraceSamplingConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1TraceConfigOverrideOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsTraceConfigOverridesDelete"] = apigee.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "apiProxy": t.string().optional(),
                "samplingConfig": t.proxy(
                    renames["GoogleCloudApigeeV1TraceSamplingConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1TraceConfigOverrideOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsTraceConfigOverridesCreate"] = apigee.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "apiProxy": t.string().optional(),
                "samplingConfig": t.proxy(
                    renames["GoogleCloudApigeeV1TraceSamplingConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1TraceConfigOverrideOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsTraceConfigOverridesPatch"] = apigee.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "apiProxy": t.string().optional(),
                "samplingConfig": t.proxy(
                    renames["GoogleCloudApigeeV1TraceSamplingConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1TraceConfigOverrideOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsTargetserversUpdate"] = apigee.post(
        "v1/{parent}/targetservers",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string(),
                "sSLInfo": t.proxy(renames["GoogleCloudApigeeV1TlsInfoIn"]).optional(),
                "isEnabled": t.boolean().optional(),
                "port": t.integer(),
                "description": t.string().optional(),
                "protocol": t.string().optional(),
                "host": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1TargetServerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsTargetserversGet"] = apigee.post(
        "v1/{parent}/targetservers",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string(),
                "sSLInfo": t.proxy(renames["GoogleCloudApigeeV1TlsInfoIn"]).optional(),
                "isEnabled": t.boolean().optional(),
                "port": t.integer(),
                "description": t.string().optional(),
                "protocol": t.string().optional(),
                "host": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1TargetServerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsTargetserversDelete"] = apigee.post(
        "v1/{parent}/targetservers",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string(),
                "sSLInfo": t.proxy(renames["GoogleCloudApigeeV1TlsInfoIn"]).optional(),
                "isEnabled": t.boolean().optional(),
                "port": t.integer(),
                "description": t.string().optional(),
                "protocol": t.string().optional(),
                "host": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1TargetServerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsTargetserversCreate"] = apigee.post(
        "v1/{parent}/targetservers",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string(),
                "sSLInfo": t.proxy(renames["GoogleCloudApigeeV1TlsInfoIn"]).optional(),
                "isEnabled": t.boolean().optional(),
                "port": t.integer(),
                "description": t.string().optional(),
                "protocol": t.string().optional(),
                "host": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1TargetServerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsKeystoresCreate"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1KeystoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsKeystoresGet"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1KeystoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsKeystoresDelete"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1KeystoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsKeystoresAliasesUpdate"] = apigee.post(
        "v1/{parent}/aliases",
        t.struct(
            {
                "format": t.string(),
                "ignoreExpiryValidation": t.boolean().optional(),
                "alias": t.string().optional(),
                "parent": t.string(),
                "_password": t.string().optional(),
                "ignoreNewlineValidation": t.boolean().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "data": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1AliasOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsKeystoresAliasesGetCertificate"] = apigee.post(
        "v1/{parent}/aliases",
        t.struct(
            {
                "format": t.string(),
                "ignoreExpiryValidation": t.boolean().optional(),
                "alias": t.string().optional(),
                "parent": t.string(),
                "_password": t.string().optional(),
                "ignoreNewlineValidation": t.boolean().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "data": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1AliasOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsKeystoresAliasesDelete"] = apigee.post(
        "v1/{parent}/aliases",
        t.struct(
            {
                "format": t.string(),
                "ignoreExpiryValidation": t.boolean().optional(),
                "alias": t.string().optional(),
                "parent": t.string(),
                "_password": t.string().optional(),
                "ignoreNewlineValidation": t.boolean().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "data": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1AliasOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsKeystoresAliasesCsr"] = apigee.post(
        "v1/{parent}/aliases",
        t.struct(
            {
                "format": t.string(),
                "ignoreExpiryValidation": t.boolean().optional(),
                "alias": t.string().optional(),
                "parent": t.string(),
                "_password": t.string().optional(),
                "ignoreNewlineValidation": t.boolean().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "data": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1AliasOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsKeystoresAliasesGet"] = apigee.post(
        "v1/{parent}/aliases",
        t.struct(
            {
                "format": t.string(),
                "ignoreExpiryValidation": t.boolean().optional(),
                "alias": t.string().optional(),
                "parent": t.string(),
                "_password": t.string().optional(),
                "ignoreNewlineValidation": t.boolean().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "data": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1AliasOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsKeystoresAliasesCreate"] = apigee.post(
        "v1/{parent}/aliases",
        t.struct(
            {
                "format": t.string(),
                "ignoreExpiryValidation": t.boolean().optional(),
                "alias": t.string().optional(),
                "parent": t.string(),
                "_password": t.string().optional(),
                "ignoreNewlineValidation": t.boolean().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "data": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1AliasOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsQueriesGet"] = apigee.post(
        "v1/{parent}/queries",
        t.struct(
            {
                "parent": t.string(),
                "timeRange": t.struct({"_": t.string().optional()}),
                "metrics": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1QueryMetricIn"])
                ).optional(),
                "name": t.string().optional(),
                "dimensions": t.array(t.string()).optional(),
                "filter": t.string().optional(),
                "groupByTimeUnit": t.string().optional(),
                "envgroupHostname": t.string().optional(),
                "limit": t.integer().optional(),
                "outputFormat": t.string().optional(),
                "csvDelimiter": t.string().optional(),
                "reportDefinitionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1AsyncQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsQueriesGetResulturl"] = apigee.post(
        "v1/{parent}/queries",
        t.struct(
            {
                "parent": t.string(),
                "timeRange": t.struct({"_": t.string().optional()}),
                "metrics": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1QueryMetricIn"])
                ).optional(),
                "name": t.string().optional(),
                "dimensions": t.array(t.string()).optional(),
                "filter": t.string().optional(),
                "groupByTimeUnit": t.string().optional(),
                "envgroupHostname": t.string().optional(),
                "limit": t.integer().optional(),
                "outputFormat": t.string().optional(),
                "csvDelimiter": t.string().optional(),
                "reportDefinitionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1AsyncQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsQueriesGetResult"] = apigee.post(
        "v1/{parent}/queries",
        t.struct(
            {
                "parent": t.string(),
                "timeRange": t.struct({"_": t.string().optional()}),
                "metrics": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1QueryMetricIn"])
                ).optional(),
                "name": t.string().optional(),
                "dimensions": t.array(t.string()).optional(),
                "filter": t.string().optional(),
                "groupByTimeUnit": t.string().optional(),
                "envgroupHostname": t.string().optional(),
                "limit": t.integer().optional(),
                "outputFormat": t.string().optional(),
                "csvDelimiter": t.string().optional(),
                "reportDefinitionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1AsyncQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsQueriesList"] = apigee.post(
        "v1/{parent}/queries",
        t.struct(
            {
                "parent": t.string(),
                "timeRange": t.struct({"_": t.string().optional()}),
                "metrics": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1QueryMetricIn"])
                ).optional(),
                "name": t.string().optional(),
                "dimensions": t.array(t.string()).optional(),
                "filter": t.string().optional(),
                "groupByTimeUnit": t.string().optional(),
                "envgroupHostname": t.string().optional(),
                "limit": t.integer().optional(),
                "outputFormat": t.string().optional(),
                "csvDelimiter": t.string().optional(),
                "reportDefinitionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1AsyncQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsQueriesCreate"] = apigee.post(
        "v1/{parent}/queries",
        t.struct(
            {
                "parent": t.string(),
                "timeRange": t.struct({"_": t.string().optional()}),
                "metrics": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1QueryMetricIn"])
                ).optional(),
                "name": t.string().optional(),
                "dimensions": t.array(t.string()).optional(),
                "filter": t.string().optional(),
                "groupByTimeUnit": t.string().optional(),
                "envgroupHostname": t.string().optional(),
                "limit": t.integer().optional(),
                "outputFormat": t.string().optional(),
                "csvDelimiter": t.string().optional(),
                "reportDefinitionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1AsyncQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsApisRevisionsGetDeployments"] = apigee.delete(
        "v1/{name}/deployments",
        t.struct(
            {
                "sequencedRollout": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsApisRevisionsDeploy"] = apigee.delete(
        "v1/{name}/deployments",
        t.struct(
            {
                "sequencedRollout": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsApisRevisionsUndeploy"] = apigee.delete(
        "v1/{name}/deployments",
        t.struct(
            {
                "sequencedRollout": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsEnvironmentsApisRevisionsDeploymentsGenerateUndeployChangeReport"
    ] = apigee.post(
        "v1/{name}/deployments:generateDeployChangeReport",
        t.struct(
            {
                "name": t.string().optional(),
                "override": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeploymentChangeReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsEnvironmentsApisRevisionsDeploymentsGenerateDeployChangeReport"
    ] = apigee.post(
        "v1/{name}/deployments:generateDeployChangeReport",
        t.struct(
            {
                "name": t.string().optional(),
                "override": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeploymentChangeReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsEnvironmentsApisRevisionsDebugsessionsDeleteData"
    ] = apigee.post(
        "v1/{parent}/debugsessions",
        t.struct(
            {
                "timeout": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "count": t.integer().optional(),
                "name": t.string().optional(),
                "tracesize": t.integer().optional(),
                "validity": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DebugSessionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsApisRevisionsDebugsessionsList"] = apigee.post(
        "v1/{parent}/debugsessions",
        t.struct(
            {
                "timeout": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "count": t.integer().optional(),
                "name": t.string().optional(),
                "tracesize": t.integer().optional(),
                "validity": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DebugSessionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsApisRevisionsDebugsessionsGet"] = apigee.post(
        "v1/{parent}/debugsessions",
        t.struct(
            {
                "timeout": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "count": t.integer().optional(),
                "name": t.string().optional(),
                "tracesize": t.integer().optional(),
                "validity": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DebugSessionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsEnvironmentsApisRevisionsDebugsessionsCreate"
    ] = apigee.post(
        "v1/{parent}/debugsessions",
        t.struct(
            {
                "timeout": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "count": t.integer().optional(),
                "name": t.string().optional(),
                "tracesize": t.integer().optional(),
                "validity": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DebugSessionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsEnvironmentsApisRevisionsDebugsessionsDataGet"
    ] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DebugSessionTransactionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsApisDeploymentsList"] = apigee.get(
        "v1/{parent}/deployments",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsKeyvaluemapsDelete"] = apigee.post(
        "v1/{parent}/keyvaluemaps",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string(),
                "encrypted": t.boolean(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1KeyValueMapOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsKeyvaluemapsCreate"] = apigee.post(
        "v1/{parent}/keyvaluemaps",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string(),
                "encrypted": t.boolean(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1KeyValueMapOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsKeyvaluemapsEntriesList"] = apigee.post(
        "v1/{parent}/entries",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "value": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1KeyValueEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsKeyvaluemapsEntriesDelete"] = apigee.post(
        "v1/{parent}/entries",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "value": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1KeyValueEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsKeyvaluemapsEntriesGet"] = apigee.post(
        "v1/{parent}/entries",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "value": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1KeyValueEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsKeyvaluemapsEntriesCreate"] = apigee.post(
        "v1/{parent}/entries",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "value": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1KeyValueEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsSecurityReportsCreate"] = apigee.get(
        "v1/{parent}/securityReports",
        t.struct(
            {
                "to": t.string().optional(),
                "from": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "status": t.string().optional(),
                "submittedBy": t.string().optional(),
                "parent": t.string(),
                "dataset": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListSecurityReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsSecurityReportsGetResultView"] = apigee.get(
        "v1/{parent}/securityReports",
        t.struct(
            {
                "to": t.string().optional(),
                "from": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "status": t.string().optional(),
                "submittedBy": t.string().optional(),
                "parent": t.string(),
                "dataset": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListSecurityReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsSecurityReportsGet"] = apigee.get(
        "v1/{parent}/securityReports",
        t.struct(
            {
                "to": t.string().optional(),
                "from": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "status": t.string().optional(),
                "submittedBy": t.string().optional(),
                "parent": t.string(),
                "dataset": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListSecurityReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsSecurityReportsGetResult"] = apigee.get(
        "v1/{parent}/securityReports",
        t.struct(
            {
                "to": t.string().optional(),
                "from": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "status": t.string().optional(),
                "submittedBy": t.string().optional(),
                "parent": t.string(),
                "dataset": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListSecurityReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsSecurityReportsList"] = apigee.get(
        "v1/{parent}/securityReports",
        t.struct(
            {
                "to": t.string().optional(),
                "from": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "status": t.string().optional(),
                "submittedBy": t.string().optional(),
                "parent": t.string(),
                "dataset": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListSecurityReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsEnvironmentsArchiveDeploymentsGenerateDownloadUrl"
    ] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsArchiveDeploymentsGet"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsArchiveDeploymentsPatch"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsArchiveDeploymentsCreate"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsArchiveDeploymentsList"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsEnvironmentsArchiveDeploymentsGenerateUploadUrl"
    ] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsArchiveDeploymentsDelete"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsSharedflowsDeploymentsList"] = apigee.get(
        "v1/{parent}/deployments",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsSharedflowsRevisionsUndeploy"] = apigee.post(
        "v1/{name}/deployments",
        t.struct(
            {
                "serviceAccount": t.string().optional(),
                "override": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsEnvironmentsSharedflowsRevisionsGetDeployments"
    ] = apigee.post(
        "v1/{name}/deployments",
        t.struct(
            {
                "serviceAccount": t.string().optional(),
                "override": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsSharedflowsRevisionsDeploy"] = apigee.post(
        "v1/{name}/deployments",
        t.struct(
            {
                "serviceAccount": t.string().optional(),
                "override": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsStatsGet"] = apigee.get(
        "v1/{name}",
        t.struct(
            {
                "timeUnit": t.string().optional(),
                "timeRange": t.string().optional(),
                "realtime": t.boolean().optional(),
                "tzo": t.string().optional(),
                "limit": t.string().optional(),
                "tsAscending": t.boolean().optional(),
                "sort": t.string().optional(),
                "offset": t.string().optional(),
                "accuracy": t.string().optional(),
                "select": t.string().optional(),
                "filter": t.string().optional(),
                "topk": t.string().optional(),
                "name": t.string(),
                "sortby": t.string().optional(),
                "sonar": t.boolean().optional(),
                "aggTable": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1StatsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsAnalyticsExportsList"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ExportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsAnalyticsExportsCreate"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ExportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsAnalyticsExportsGet"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ExportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsAnalyticsAdminGetSchemav2"] = apigee.get(
        "v1/{name}",
        t.struct(
            {
                "disableCache": t.boolean().optional(),
                "name": t.string(),
                "type": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1SchemaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsSecurityStatsQueryTabularStats"] = apigee.post(
        "v1/{orgenv}/securityStats:queryTimeSeriesStats",
        t.struct(
            {
                "orgenv": t.string(),
                "pageSize": t.integer().optional(),
                "timeRange": t.proxy(renames["GoogleTypeIntervalIn"]),
                "timestampOrder": t.string().optional(),
                "dimensions": t.array(t.string()).optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "metrics": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1MetricAggregationIn"])
                ),
                "windowSize": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1QueryTimeSeriesStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsEnvironmentsSecurityStatsQueryTimeSeriesStats"
    ] = apigee.post(
        "v1/{orgenv}/securityStats:queryTimeSeriesStats",
        t.struct(
            {
                "orgenv": t.string(),
                "pageSize": t.integer().optional(),
                "timeRange": t.proxy(renames["GoogleTypeIntervalIn"]),
                "timestampOrder": t.string().optional(),
                "dimensions": t.array(t.string()).optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "metrics": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1MetricAggregationIn"])
                ),
                "windowSize": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1QueryTimeSeriesStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsOptimizedStatsGet"] = apigee.get(
        "v1/{name}",
        t.struct(
            {
                "sortby": t.string().optional(),
                "limit": t.string().optional(),
                "select": t.string(),
                "realtime": t.boolean().optional(),
                "filter": t.string().optional(),
                "name": t.string(),
                "tzo": t.string().optional(),
                "tsAscending": t.boolean().optional(),
                "accuracy": t.string().optional(),
                "aggTable": t.string().optional(),
                "timeRange": t.string(),
                "sonar": t.boolean().optional(),
                "timeUnit": t.string().optional(),
                "offset": t.string().optional(),
                "topk": t.string().optional(),
                "sort": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1OptimizedStatsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsDeploymentsList"] = apigee.get(
        "v1/{parent}/deployments",
        t.struct(
            {
                "sharedFlows": t.boolean().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsReferencesGet"] = apigee.post(
        "v1/{parent}/references",
        t.struct(
            {
                "parent": t.string(),
                "resourceType": t.string().optional(),
                "name": t.string(),
                "refers": t.string(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ReferenceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsReferencesDelete"] = apigee.post(
        "v1/{parent}/references",
        t.struct(
            {
                "parent": t.string(),
                "resourceType": t.string().optional(),
                "name": t.string(),
                "refers": t.string(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ReferenceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsReferencesUpdate"] = apigee.post(
        "v1/{parent}/references",
        t.struct(
            {
                "parent": t.string(),
                "resourceType": t.string().optional(),
                "name": t.string(),
                "refers": t.string(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ReferenceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsReferencesCreate"] = apigee.post(
        "v1/{parent}/references",
        t.struct(
            {
                "parent": t.string(),
                "resourceType": t.string().optional(),
                "name": t.string(),
                "refers": t.string(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ReferenceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsSecurityIncidentsGet"] = apigee.get(
        "v1/{parent}/securityIncidents",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListSecurityIncidentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsSecurityIncidentsList"] = apigee.get(
        "v1/{parent}/securityIncidents",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListSecurityIncidentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsCachesDelete"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsHostSecurityReportsCreate"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1SecurityReportResultViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsHostSecurityReportsList"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1SecurityReportResultViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsHostSecurityReportsGetResult"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1SecurityReportResultViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsHostSecurityReportsGet"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1SecurityReportResultViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsHostSecurityReportsGetResultView"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1SecurityReportResultViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersGet"] = apigee.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "email": t.string(),
                "companies": t.array(t.string()).optional(),
                "userName": t.string(),
                "firstName": t.string(),
                "lastName": t.string(),
                "appFamily": t.string().optional(),
                "accessType": t.string().optional(),
                "developerId": t.string().optional(),
                "attributes": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
                ).optional(),
                "apps": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersGetBalance"] = apigee.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "email": t.string(),
                "companies": t.array(t.string()).optional(),
                "userName": t.string(),
                "firstName": t.string(),
                "lastName": t.string(),
                "appFamily": t.string().optional(),
                "accessType": t.string().optional(),
                "developerId": t.string().optional(),
                "attributes": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
                ).optional(),
                "apps": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersSetDeveloperStatus"] = apigee.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "email": t.string(),
                "companies": t.array(t.string()).optional(),
                "userName": t.string(),
                "firstName": t.string(),
                "lastName": t.string(),
                "appFamily": t.string().optional(),
                "accessType": t.string().optional(),
                "developerId": t.string().optional(),
                "attributes": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
                ).optional(),
                "apps": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersList"] = apigee.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "email": t.string(),
                "companies": t.array(t.string()).optional(),
                "userName": t.string(),
                "firstName": t.string(),
                "lastName": t.string(),
                "appFamily": t.string().optional(),
                "accessType": t.string().optional(),
                "developerId": t.string().optional(),
                "attributes": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
                ).optional(),
                "apps": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersUpdateMonetizationConfig"] = apigee.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "email": t.string(),
                "companies": t.array(t.string()).optional(),
                "userName": t.string(),
                "firstName": t.string(),
                "lastName": t.string(),
                "appFamily": t.string().optional(),
                "accessType": t.string().optional(),
                "developerId": t.string().optional(),
                "attributes": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
                ).optional(),
                "apps": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersDelete"] = apigee.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "email": t.string(),
                "companies": t.array(t.string()).optional(),
                "userName": t.string(),
                "firstName": t.string(),
                "lastName": t.string(),
                "appFamily": t.string().optional(),
                "accessType": t.string().optional(),
                "developerId": t.string().optional(),
                "attributes": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
                ).optional(),
                "apps": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersGetMonetizationConfig"] = apigee.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "email": t.string(),
                "companies": t.array(t.string()).optional(),
                "userName": t.string(),
                "firstName": t.string(),
                "lastName": t.string(),
                "appFamily": t.string().optional(),
                "accessType": t.string().optional(),
                "developerId": t.string().optional(),
                "attributes": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
                ).optional(),
                "apps": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAttributes"] = apigee.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "email": t.string(),
                "companies": t.array(t.string()).optional(),
                "userName": t.string(),
                "firstName": t.string(),
                "lastName": t.string(),
                "appFamily": t.string().optional(),
                "accessType": t.string().optional(),
                "developerId": t.string().optional(),
                "attributes": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
                ).optional(),
                "apps": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersCreate"] = apigee.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "email": t.string(),
                "companies": t.array(t.string()).optional(),
                "userName": t.string(),
                "firstName": t.string(),
                "lastName": t.string(),
                "appFamily": t.string().optional(),
                "accessType": t.string().optional(),
                "developerId": t.string().optional(),
                "attributes": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
                ).optional(),
                "apps": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersUpdate"] = apigee.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "email": t.string(),
                "companies": t.array(t.string()).optional(),
                "userName": t.string(),
                "firstName": t.string(),
                "lastName": t.string(),
                "appFamily": t.string().optional(),
                "accessType": t.string().optional(),
                "developerId": t.string().optional(),
                "attributes": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
                ).optional(),
                "apps": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAttributesDelete"] = apigee.post(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "value": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1AttributeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAttributesList"] = apigee.post(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "value": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1AttributeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAttributesGet"] = apigee.post(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "value": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1AttributeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsDevelopersAttributesUpdateDeveloperAttribute"
    ] = apigee.post(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "value": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1AttributeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsUpdate"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsAttributes"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsDevelopersAppsGenerateKeyPairOrUpdateDeveloperAppStatus"
    ] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsList"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsGet"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsCreate"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsDelete"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsKeysGet"] = apigee.post(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "action": t.string().optional(),
                "attributes": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
                ).optional(),
                "consumerSecret": t.string().optional(),
                "apiProducts": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "status": t.string().optional(),
                "expiresAt": t.string().optional(),
                "expiresInSeconds": t.string().optional(),
                "consumerKey": t.string().optional(),
                "scopes": t.array(t.string()).optional(),
                "issuedAt": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperAppKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsKeysCreate"] = apigee.post(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "action": t.string().optional(),
                "attributes": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
                ).optional(),
                "consumerSecret": t.string().optional(),
                "apiProducts": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "status": t.string().optional(),
                "expiresAt": t.string().optional(),
                "expiresInSeconds": t.string().optional(),
                "consumerKey": t.string().optional(),
                "scopes": t.array(t.string()).optional(),
                "issuedAt": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperAppKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsKeysDelete"] = apigee.post(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "action": t.string().optional(),
                "attributes": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
                ).optional(),
                "consumerSecret": t.string().optional(),
                "apiProducts": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "status": t.string().optional(),
                "expiresAt": t.string().optional(),
                "expiresInSeconds": t.string().optional(),
                "consumerKey": t.string().optional(),
                "scopes": t.array(t.string()).optional(),
                "issuedAt": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperAppKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsKeysReplaceDeveloperAppKey"] = apigee.post(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "action": t.string().optional(),
                "attributes": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
                ).optional(),
                "consumerSecret": t.string().optional(),
                "apiProducts": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "status": t.string().optional(),
                "expiresAt": t.string().optional(),
                "expiresInSeconds": t.string().optional(),
                "consumerKey": t.string().optional(),
                "scopes": t.array(t.string()).optional(),
                "issuedAt": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperAppKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsKeysUpdateDeveloperAppKey"] = apigee.post(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "action": t.string().optional(),
                "attributes": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
                ).optional(),
                "consumerSecret": t.string().optional(),
                "apiProducts": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "status": t.string().optional(),
                "expiresAt": t.string().optional(),
                "expiresInSeconds": t.string().optional(),
                "consumerKey": t.string().optional(),
                "scopes": t.array(t.string()).optional(),
                "issuedAt": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperAppKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsKeysCreateCreate"] = apigee.post(
        "v1/{parent}/keys/create",
        t.struct(
            {
                "parent": t.string().optional(),
                "attributes": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
                ).optional(),
                "consumerSecret": t.string().optional(),
                "apiProducts": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "status": t.string().optional(),
                "expiresAt": t.string().optional(),
                "expiresInSeconds": t.string().optional(),
                "consumerKey": t.string().optional(),
                "scopes": t.array(t.string()).optional(),
                "issuedAt": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperAppKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsDevelopersAppsKeysApiproductsUpdateDeveloperAppKeyApiProduct"
    ] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperAppKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsKeysApiproductsDelete"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperAppKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsDevelopersAppsAttributesUpdateDeveloperAppAttribute"
    ] = apigee.get(
        "v1/{parent}/attributes",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1AttributesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsAttributesDelete"] = apigee.get(
        "v1/{parent}/attributes",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1AttributesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsAttributesGet"] = apigee.get(
        "v1/{parent}/attributes",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1AttributesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsAttributesList"] = apigee.get(
        "v1/{parent}/attributes",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1AttributesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersSubscriptionsList"] = apigee.post(
        "v1/{parent}/subscriptions",
        t.struct(
            {
                "parent": t.string(),
                "startTime": t.string().optional(),
                "apiproduct": t.string().optional(),
                "endTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperSubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersSubscriptionsGet"] = apigee.post(
        "v1/{parent}/subscriptions",
        t.struct(
            {
                "parent": t.string(),
                "startTime": t.string().optional(),
                "apiproduct": t.string().optional(),
                "endTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperSubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersSubscriptionsExpire"] = apigee.post(
        "v1/{parent}/subscriptions",
        t.struct(
            {
                "parent": t.string(),
                "startTime": t.string().optional(),
                "apiproduct": t.string().optional(),
                "endTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperSubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersSubscriptionsCreate"] = apigee.post(
        "v1/{parent}/subscriptions",
        t.struct(
            {
                "parent": t.string(),
                "startTime": t.string().optional(),
                "apiproduct": t.string().optional(),
                "endTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperSubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersBalanceCredit"] = apigee.post(
        "v1/{name}:adjust",
        t.struct(
            {
                "name": t.string(),
                "adjustment": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperBalanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersBalanceAdjust"] = apigee.post(
        "v1/{name}:adjust",
        t.struct(
            {
                "name": t.string(),
                "adjustment": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperBalanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsHostStatsGet"] = apigee.get(
        "v1/{name}",
        t.struct(
            {
                "sort": t.string().optional(),
                "name": t.string(),
                "timeRange": t.string().optional(),
                "accuracy": t.string().optional(),
                "envgroupHostname": t.string(),
                "realtime": t.boolean().optional(),
                "limit": t.string().optional(),
                "tzo": t.string().optional(),
                "select": t.string().optional(),
                "topk": t.string().optional(),
                "sortby": t.string().optional(),
                "timeUnit": t.string().optional(),
                "filter": t.string().optional(),
                "tsAscending": t.boolean().optional(),
                "offset": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1StatsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsHostQueriesGetResult"] = apigee.get(
        "v1/{parent}/hostQueries",
        t.struct(
            {
                "from": t.string().optional(),
                "to": t.string().optional(),
                "status": t.string().optional(),
                "envgroupHostname": t.string(),
                "parent": t.string(),
                "dataset": t.string().optional(),
                "inclQueriesWithoutReport": t.string().optional(),
                "submittedBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListAsyncQueriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsHostQueriesCreate"] = apigee.get(
        "v1/{parent}/hostQueries",
        t.struct(
            {
                "from": t.string().optional(),
                "to": t.string().optional(),
                "status": t.string().optional(),
                "envgroupHostname": t.string(),
                "parent": t.string(),
                "dataset": t.string().optional(),
                "inclQueriesWithoutReport": t.string().optional(),
                "submittedBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListAsyncQueriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsHostQueriesGetResultView"] = apigee.get(
        "v1/{parent}/hostQueries",
        t.struct(
            {
                "from": t.string().optional(),
                "to": t.string().optional(),
                "status": t.string().optional(),
                "envgroupHostname": t.string(),
                "parent": t.string(),
                "dataset": t.string().optional(),
                "inclQueriesWithoutReport": t.string().optional(),
                "submittedBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListAsyncQueriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsHostQueriesGet"] = apigee.get(
        "v1/{parent}/hostQueries",
        t.struct(
            {
                "from": t.string().optional(),
                "to": t.string().optional(),
                "status": t.string().optional(),
                "envgroupHostname": t.string(),
                "parent": t.string(),
                "dataset": t.string().optional(),
                "inclQueriesWithoutReport": t.string().optional(),
                "submittedBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListAsyncQueriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsHostQueriesList"] = apigee.get(
        "v1/{parent}/hostQueries",
        t.struct(
            {
                "from": t.string().optional(),
                "to": t.string().optional(),
                "status": t.string().optional(),
                "envgroupHostname": t.string(),
                "parent": t.string(),
                "dataset": t.string().optional(),
                "inclQueriesWithoutReport": t.string().optional(),
                "submittedBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListAsyncQueriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDeploymentsList"] = apigee.get(
        "v1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "sharedFlows": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAppsGet"] = apigee.get(
        "v1/{parent}/apps",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "startKey": t.string().optional(),
                "apiProduct": t.string().optional(),
                "expand": t.boolean().optional(),
                "keyStatus": t.string().optional(),
                "ids": t.string().optional(),
                "pageToken": t.string().optional(),
                "rows": t.string().optional(),
                "apptype": t.string().optional(),
                "includeCred": t.boolean().optional(),
                "status": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAppsList"] = apigee.get(
        "v1/{parent}/apps",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "startKey": t.string().optional(),
                "apiProduct": t.string().optional(),
                "expand": t.boolean().optional(),
                "keyStatus": t.string().optional(),
                "ids": t.string().optional(),
                "pageToken": t.string().optional(),
                "rows": t.string().optional(),
                "apptype": t.string().optional(),
                "includeCred": t.boolean().optional(),
                "status": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAppgroupsList"] = apigee.post(
        "v1/{parent}/appgroups",
        t.struct(
            {
                "parent": t.string(),
                "attributes": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
                ).optional(),
                "status": t.string().optional(),
                "name": t.string().optional(),
                "channelId": t.string().optional(),
                "displayName": t.string().optional(),
                "channelUri": t.string().optional(),
                "organization": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1AppGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAppgroupsUpdate"] = apigee.post(
        "v1/{parent}/appgroups",
        t.struct(
            {
                "parent": t.string(),
                "attributes": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
                ).optional(),
                "status": t.string().optional(),
                "name": t.string().optional(),
                "channelId": t.string().optional(),
                "displayName": t.string().optional(),
                "channelUri": t.string().optional(),
                "organization": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1AppGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAppgroupsDelete"] = apigee.post(
        "v1/{parent}/appgroups",
        t.struct(
            {
                "parent": t.string(),
                "attributes": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
                ).optional(),
                "status": t.string().optional(),
                "name": t.string().optional(),
                "channelId": t.string().optional(),
                "displayName": t.string().optional(),
                "channelUri": t.string().optional(),
                "organization": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1AppGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAppgroupsGet"] = apigee.post(
        "v1/{parent}/appgroups",
        t.struct(
            {
                "parent": t.string(),
                "attributes": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
                ).optional(),
                "status": t.string().optional(),
                "name": t.string().optional(),
                "channelId": t.string().optional(),
                "displayName": t.string().optional(),
                "channelUri": t.string().optional(),
                "organization": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1AppGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAppgroupsCreate"] = apigee.post(
        "v1/{parent}/appgroups",
        t.struct(
            {
                "parent": t.string(),
                "attributes": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
                ).optional(),
                "status": t.string().optional(),
                "name": t.string().optional(),
                "channelId": t.string().optional(),
                "displayName": t.string().optional(),
                "channelUri": t.string().optional(),
                "organization": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1AppGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAppgroupsAppsList"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1AppGroupAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAppgroupsAppsGet"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1AppGroupAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAppgroupsAppsCreate"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1AppGroupAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAppgroupsAppsUpdate"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1AppGroupAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAppgroupsAppsDelete"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1AppGroupAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAppgroupsAppsKeysDelete"] = apigee.post(
        "v1/{parent}/keys",
        t.struct(
            {
                "parent": t.string(),
                "status": t.string().optional(),
                "consumerKey": t.string().optional(),
                "consumerSecret": t.string().optional(),
                "expiresInSeconds": t.string().optional(),
                "scopes": t.array(t.string()).optional(),
                "attributes": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1AppGroupAppKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAppgroupsAppsKeysGet"] = apigee.post(
        "v1/{parent}/keys",
        t.struct(
            {
                "parent": t.string(),
                "status": t.string().optional(),
                "consumerKey": t.string().optional(),
                "consumerSecret": t.string().optional(),
                "expiresInSeconds": t.string().optional(),
                "scopes": t.array(t.string()).optional(),
                "attributes": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1AppGroupAppKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAppgroupsAppsKeysUpdateAppGroupAppKey"] = apigee.post(
        "v1/{parent}/keys",
        t.struct(
            {
                "parent": t.string(),
                "status": t.string().optional(),
                "consumerKey": t.string().optional(),
                "consumerSecret": t.string().optional(),
                "expiresInSeconds": t.string().optional(),
                "scopes": t.array(t.string()).optional(),
                "attributes": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1AppGroupAppKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAppgroupsAppsKeysCreate"] = apigee.post(
        "v1/{parent}/keys",
        t.struct(
            {
                "parent": t.string(),
                "status": t.string().optional(),
                "consumerKey": t.string().optional(),
                "consumerSecret": t.string().optional(),
                "expiresInSeconds": t.string().optional(),
                "scopes": t.array(t.string()).optional(),
                "attributes": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1AppGroupAppKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsAppgroupsAppsKeysApiproductsUpdateAppGroupAppKeyApiProduct"
    ] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1AppGroupAppKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAppgroupsAppsKeysApiproductsDelete"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1AppGroupAppKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDatacollectorsList"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDatacollectorsCreate"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDatacollectorsGet"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDatacollectorsPatch"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDatacollectorsDelete"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSecurityProfilesList"] = apigee.get(
        "v1/{name}:listRevisions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListSecurityProfileRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSecurityProfilesGet"] = apigee.get(
        "v1/{name}:listRevisions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListSecurityProfileRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSecurityProfilesListRevisions"] = apigee.get(
        "v1/{name}:listRevisions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListSecurityProfileRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSecurityProfilesEnvironmentsDelete"] = apigee.post(
        "v1/{profileEnvironment}:computeEnvironmentScores",
        t.struct(
            {
                "profileEnvironment": t.string(),
                "pageSize": t.integer().optional(),
                "filters": t.array(
                    t.proxy(
                        renames[
                            "GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilterIn"
                        ]
                    )
                ).optional(),
                "pageToken": t.string().optional(),
                "timeRange": t.proxy(renames["GoogleTypeIntervalIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ComputeEnvironmentScoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSecurityProfilesEnvironmentsCreate"] = apigee.post(
        "v1/{profileEnvironment}:computeEnvironmentScores",
        t.struct(
            {
                "profileEnvironment": t.string(),
                "pageSize": t.integer().optional(),
                "filters": t.array(
                    t.proxy(
                        renames[
                            "GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilterIn"
                        ]
                    )
                ).optional(),
                "pageToken": t.string().optional(),
                "timeRange": t.proxy(renames["GoogleTypeIntervalIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ComputeEnvironmentScoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsSecurityProfilesEnvironmentsComputeEnvironmentScores"
    ] = apigee.post(
        "v1/{profileEnvironment}:computeEnvironmentScores",
        t.struct(
            {
                "profileEnvironment": t.string(),
                "pageSize": t.integer().optional(),
                "filters": t.array(
                    t.proxy(
                        renames[
                            "GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilterIn"
                        ]
                    )
                ).optional(),
                "pageToken": t.string().optional(),
                "timeRange": t.proxy(renames["GoogleTypeIntervalIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ComputeEnvironmentScoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesDelete"] = apigee.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string().optional(),
                "diskEncryptionKeyName": t.string().optional(),
                "consumerAcceptList": t.array(t.string()).optional(),
                "peeringCidrRange": t.string().optional(),
                "location": t.string(),
                "description": t.string().optional(),
                "name": t.string(),
                "ipRange": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesPatch"] = apigee.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string().optional(),
                "diskEncryptionKeyName": t.string().optional(),
                "consumerAcceptList": t.array(t.string()).optional(),
                "peeringCidrRange": t.string().optional(),
                "location": t.string(),
                "description": t.string().optional(),
                "name": t.string(),
                "ipRange": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesReportStatus"] = apigee.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string().optional(),
                "diskEncryptionKeyName": t.string().optional(),
                "consumerAcceptList": t.array(t.string()).optional(),
                "peeringCidrRange": t.string().optional(),
                "location": t.string(),
                "description": t.string().optional(),
                "name": t.string(),
                "ipRange": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesGet"] = apigee.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string().optional(),
                "diskEncryptionKeyName": t.string().optional(),
                "consumerAcceptList": t.array(t.string()).optional(),
                "peeringCidrRange": t.string().optional(),
                "location": t.string(),
                "description": t.string().optional(),
                "name": t.string(),
                "ipRange": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesList"] = apigee.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string().optional(),
                "diskEncryptionKeyName": t.string().optional(),
                "consumerAcceptList": t.array(t.string()).optional(),
                "peeringCidrRange": t.string().optional(),
                "location": t.string(),
                "description": t.string().optional(),
                "name": t.string(),
                "ipRange": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesCreate"] = apigee.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string().optional(),
                "diskEncryptionKeyName": t.string().optional(),
                "consumerAcceptList": t.array(t.string()).optional(),
                "peeringCidrRange": t.string().optional(),
                "location": t.string(),
                "description": t.string().optional(),
                "name": t.string(),
                "ipRange": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesNatAddressesCreate"] = apigee.post(
        "v1/{name}:activate",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesNatAddressesDelete"] = apigee.post(
        "v1/{name}:activate",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesNatAddressesGet"] = apigee.post(
        "v1/{name}:activate",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesNatAddressesList"] = apigee.post(
        "v1/{name}:activate",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesNatAddressesActivate"] = apigee.post(
        "v1/{name}:activate",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesCanaryevaluationsCreate"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1CanaryEvaluationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesCanaryevaluationsGet"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1CanaryEvaluationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesAttachmentsDelete"] = apigee.post(
        "v1/{parent}/attachments",
        t.struct(
            {
                "parent": t.string(),
                "environment": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesAttachmentsGet"] = apigee.post(
        "v1/{parent}/attachments",
        t.struct(
            {
                "parent": t.string(),
                "environment": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesAttachmentsList"] = apigee.post(
        "v1/{parent}/attachments",
        t.struct(
            {
                "parent": t.string(),
                "environment": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesAttachmentsCreate"] = apigee.post(
        "v1/{parent}/attachments",
        t.struct(
            {
                "parent": t.string(),
                "environment": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSharedflowsList"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1SharedFlowOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSharedflowsDelete"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1SharedFlowOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSharedflowsCreate"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1SharedFlowOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSharedflowsGet"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1SharedFlowOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSharedflowsRevisionsUpdateSharedFlowRevision"] = apigee.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "format": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleApiHttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSharedflowsRevisionsDelete"] = apigee.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "format": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleApiHttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSharedflowsRevisionsGet"] = apigee.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "format": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleApiHttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSharedflowsRevisionsDeploymentsList"] = apigee.get(
        "v1/{parent}/deployments",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSharedflowsDeploymentsList"] = apigee.get(
        "v1/{parent}/deployments",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsReportsCreate"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeleteCustomReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsReportsList"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeleteCustomReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsReportsGet"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeleteCustomReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsReportsUpdate"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeleteCustomReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsReportsDelete"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeleteCustomReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEndpointAttachmentsGet"] = apigee.post(
        "v1/{parent}/endpointAttachments",
        t.struct(
            {
                "parent": t.string(),
                "endpointAttachmentId": t.string().optional(),
                "location": t.string(),
                "name": t.string().optional(),
                "serviceAttachment": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEndpointAttachmentsDelete"] = apigee.post(
        "v1/{parent}/endpointAttachments",
        t.struct(
            {
                "parent": t.string(),
                "endpointAttachmentId": t.string().optional(),
                "location": t.string(),
                "name": t.string().optional(),
                "serviceAttachment": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEndpointAttachmentsList"] = apigee.post(
        "v1/{parent}/endpointAttachments",
        t.struct(
            {
                "parent": t.string(),
                "endpointAttachmentId": t.string().optional(),
                "location": t.string(),
                "name": t.string().optional(),
                "serviceAttachment": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEndpointAttachmentsCreate"] = apigee.post(
        "v1/{parent}/endpointAttachments",
        t.struct(
            {
                "parent": t.string(),
                "endpointAttachmentId": t.string().optional(),
                "location": t.string(),
                "name": t.string().optional(),
                "serviceAttachment": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsList"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ApiProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsUpdate"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ApiProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsAttributes"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ApiProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsCreate"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ApiProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsDelete"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ApiProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsGet"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ApiProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsAttributesDelete"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1AttributeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsApiproductsAttributesUpdateApiProductAttribute"
    ] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1AttributeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsAttributesList"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1AttributeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsAttributesGet"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1AttributeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsRateplansUpdate"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1RatePlanOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsRateplansList"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1RatePlanOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsRateplansDelete"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1RatePlanOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsRateplansCreate"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1RatePlanOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsRateplansGet"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1RatePlanOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsOptimizedHostStatsGet"] = apigee.get(
        "v1/{name}",
        t.struct(
            {
                "sort": t.string().optional(),
                "offset": t.string().optional(),
                "timeUnit": t.string().optional(),
                "topk": t.string().optional(),
                "limit": t.string().optional(),
                "name": t.string(),
                "select": t.string(),
                "sortby": t.string().optional(),
                "timeRange": t.string(),
                "filter": t.string().optional(),
                "tzo": t.string().optional(),
                "accuracy": t.string().optional(),
                "realtime": t.boolean().optional(),
                "tsAscending": t.boolean().optional(),
                "envgroupHostname": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1OptimizedStatsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsProvisionOrganization"] = apigee.post(
        "v1/{project}:provisionOrganization",
        t.struct(
            {
                "project": t.string(),
                "runtimeLocation": t.string().optional(),
                "authorizedNetwork": t.string().optional(),
                "analyticsRegion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="apigee", renames=renames, types=Box(types), functions=Box(functions)
    )
