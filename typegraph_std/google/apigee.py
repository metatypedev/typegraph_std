from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_apigee() -> Import:
    apigee = HTTPRuntime("https://apigee.googleapis.com/")

    renames = {
        "ErrorResponse": "_apigee_1_ErrorResponse",
        "GoogleCloudApigeeV1AccessIn": "_apigee_2_GoogleCloudApigeeV1AccessIn",
        "GoogleCloudApigeeV1AccessOut": "_apigee_3_GoogleCloudApigeeV1AccessOut",
        "GoogleCloudApigeeV1KeyValueEntryIn": "_apigee_4_GoogleCloudApigeeV1KeyValueEntryIn",
        "GoogleCloudApigeeV1KeyValueEntryOut": "_apigee_5_GoogleCloudApigeeV1KeyValueEntryOut",
        "GoogleCloudApigeeV1QueryTimeSeriesStatsResponseIn": "_apigee_6_GoogleCloudApigeeV1QueryTimeSeriesStatsResponseIn",
        "GoogleCloudApigeeV1QueryTimeSeriesStatsResponseOut": "_apigee_7_GoogleCloudApigeeV1QueryTimeSeriesStatsResponseOut",
        "GoogleIamV1AuditConfigIn": "_apigee_8_GoogleIamV1AuditConfigIn",
        "GoogleIamV1AuditConfigOut": "_apigee_9_GoogleIamV1AuditConfigOut",
        "GoogleCloudApigeeV1PropertiesIn": "_apigee_10_GoogleCloudApigeeV1PropertiesIn",
        "GoogleCloudApigeeV1PropertiesOut": "_apigee_11_GoogleCloudApigeeV1PropertiesOut",
        "GoogleCloudApigeeV1AccessSetIn": "_apigee_12_GoogleCloudApigeeV1AccessSetIn",
        "GoogleCloudApigeeV1AccessSetOut": "_apigee_13_GoogleCloudApigeeV1AccessSetOut",
        "GoogleCloudApigeeV1DateRangeIn": "_apigee_14_GoogleCloudApigeeV1DateRangeIn",
        "GoogleCloudApigeeV1DateRangeOut": "_apigee_15_GoogleCloudApigeeV1DateRangeOut",
        "GoogleCloudApigeeV1CreditDeveloperBalanceRequestIn": "_apigee_16_GoogleCloudApigeeV1CreditDeveloperBalanceRequestIn",
        "GoogleCloudApigeeV1CreditDeveloperBalanceRequestOut": "_apigee_17_GoogleCloudApigeeV1CreditDeveloperBalanceRequestOut",
        "GoogleCloudApigeeV1TraceSamplingConfigIn": "_apigee_18_GoogleCloudApigeeV1TraceSamplingConfigIn",
        "GoogleCloudApigeeV1TraceSamplingConfigOut": "_apigee_19_GoogleCloudApigeeV1TraceSamplingConfigOut",
        "GoogleIamV1TestIamPermissionsRequestIn": "_apigee_20_GoogleIamV1TestIamPermissionsRequestIn",
        "GoogleIamV1TestIamPermissionsRequestOut": "_apigee_21_GoogleIamV1TestIamPermissionsRequestOut",
        "GoogleCloudApigeeV1MonetizationConfigIn": "_apigee_22_GoogleCloudApigeeV1MonetizationConfigIn",
        "GoogleCloudApigeeV1MonetizationConfigOut": "_apigee_23_GoogleCloudApigeeV1MonetizationConfigOut",
        "GoogleCloudApigeeV1SyncAuthorizationIn": "_apigee_24_GoogleCloudApigeeV1SyncAuthorizationIn",
        "GoogleCloudApigeeV1SyncAuthorizationOut": "_apigee_25_GoogleCloudApigeeV1SyncAuthorizationOut",
        "GoogleCloudApigeeV1ReferenceConfigIn": "_apigee_26_GoogleCloudApigeeV1ReferenceConfigIn",
        "GoogleCloudApigeeV1ReferenceConfigOut": "_apigee_27_GoogleCloudApigeeV1ReferenceConfigOut",
        "GoogleCloudApigeeV1DeploymentIn": "_apigee_28_GoogleCloudApigeeV1DeploymentIn",
        "GoogleCloudApigeeV1DeploymentOut": "_apigee_29_GoogleCloudApigeeV1DeploymentOut",
        "GoogleCloudApigeeV1DeploymentConfigIn": "_apigee_30_GoogleCloudApigeeV1DeploymentConfigIn",
        "GoogleCloudApigeeV1DeploymentConfigOut": "_apigee_31_GoogleCloudApigeeV1DeploymentConfigOut",
        "GoogleCloudApigeeV1ListEndpointAttachmentsResponseIn": "_apigee_32_GoogleCloudApigeeV1ListEndpointAttachmentsResponseIn",
        "GoogleCloudApigeeV1ListEndpointAttachmentsResponseOut": "_apigee_33_GoogleCloudApigeeV1ListEndpointAttachmentsResponseOut",
        "GoogleCloudApigeeV1ApiCategoryIn": "_apigee_34_GoogleCloudApigeeV1ApiCategoryIn",
        "GoogleCloudApigeeV1ApiCategoryOut": "_apigee_35_GoogleCloudApigeeV1ApiCategoryOut",
        "GoogleCloudApigeeV1GenerateUploadUrlResponseIn": "_apigee_36_GoogleCloudApigeeV1GenerateUploadUrlResponseIn",
        "GoogleCloudApigeeV1GenerateUploadUrlResponseOut": "_apigee_37_GoogleCloudApigeeV1GenerateUploadUrlResponseOut",
        "GoogleCloudApigeeV1TargetServerConfigIn": "_apigee_38_GoogleCloudApigeeV1TargetServerConfigIn",
        "GoogleCloudApigeeV1TargetServerConfigOut": "_apigee_39_GoogleCloudApigeeV1TargetServerConfigOut",
        "GoogleCloudApigeeV1ListRatePlansResponseIn": "_apigee_40_GoogleCloudApigeeV1ListRatePlansResponseIn",
        "GoogleCloudApigeeV1ListRatePlansResponseOut": "_apigee_41_GoogleCloudApigeeV1ListRatePlansResponseOut",
        "GoogleCloudApigeeV1OperationMetadataIn": "_apigee_42_GoogleCloudApigeeV1OperationMetadataIn",
        "GoogleCloudApigeeV1OperationMetadataOut": "_apigee_43_GoogleCloudApigeeV1OperationMetadataOut",
        "GoogleCloudApigeeV1DatastoreIn": "_apigee_44_GoogleCloudApigeeV1DatastoreIn",
        "GoogleCloudApigeeV1DatastoreOut": "_apigee_45_GoogleCloudApigeeV1DatastoreOut",
        "GoogleCloudApigeeV1ApiProxyIn": "_apigee_46_GoogleCloudApigeeV1ApiProxyIn",
        "GoogleCloudApigeeV1ApiProxyOut": "_apigee_47_GoogleCloudApigeeV1ApiProxyOut",
        "GoogleCloudApigeeV1OptimizedStatsNodeIn": "_apigee_48_GoogleCloudApigeeV1OptimizedStatsNodeIn",
        "GoogleCloudApigeeV1OptimizedStatsNodeOut": "_apigee_49_GoogleCloudApigeeV1OptimizedStatsNodeOut",
        "GoogleCloudApigeeV1ResourceFilesIn": "_apigee_50_GoogleCloudApigeeV1ResourceFilesIn",
        "GoogleCloudApigeeV1ResourceFilesOut": "_apigee_51_GoogleCloudApigeeV1ResourceFilesOut",
        "GoogleCloudApigeeV1CertInfoIn": "_apigee_52_GoogleCloudApigeeV1CertInfoIn",
        "GoogleCloudApigeeV1CertInfoOut": "_apigee_53_GoogleCloudApigeeV1CertInfoOut",
        "GoogleCloudApigeeV1RevenueShareRangeIn": "_apigee_54_GoogleCloudApigeeV1RevenueShareRangeIn",
        "GoogleCloudApigeeV1RevenueShareRangeOut": "_apigee_55_GoogleCloudApigeeV1RevenueShareRangeOut",
        "GoogleRpcPreconditionFailureViolationIn": "_apigee_56_GoogleRpcPreconditionFailureViolationIn",
        "GoogleRpcPreconditionFailureViolationOut": "_apigee_57_GoogleRpcPreconditionFailureViolationOut",
        "GoogleCloudApigeeV1ListDebugSessionsResponseIn": "_apigee_58_GoogleCloudApigeeV1ListDebugSessionsResponseIn",
        "GoogleCloudApigeeV1ListDebugSessionsResponseOut": "_apigee_59_GoogleCloudApigeeV1ListDebugSessionsResponseOut",
        "GoogleCloudApigeeV1ListApiProxiesResponseIn": "_apigee_60_GoogleCloudApigeeV1ListApiProxiesResponseIn",
        "GoogleCloudApigeeV1ListApiProxiesResponseOut": "_apigee_61_GoogleCloudApigeeV1ListApiProxiesResponseOut",
        "GoogleCloudApigeeV1MetadataIn": "_apigee_62_GoogleCloudApigeeV1MetadataIn",
        "GoogleCloudApigeeV1MetadataOut": "_apigee_63_GoogleCloudApigeeV1MetadataOut",
        "GoogleCloudApigeeV1FlowHookIn": "_apigee_64_GoogleCloudApigeeV1FlowHookIn",
        "GoogleCloudApigeeV1FlowHookOut": "_apigee_65_GoogleCloudApigeeV1FlowHookOut",
        "GoogleCloudApigeeV1ScoreComponentIn": "_apigee_66_GoogleCloudApigeeV1ScoreComponentIn",
        "GoogleCloudApigeeV1ScoreComponentOut": "_apigee_67_GoogleCloudApigeeV1ScoreComponentOut",
        "GoogleCloudApigeeV1DeploymentGroupConfigIn": "_apigee_68_GoogleCloudApigeeV1DeploymentGroupConfigIn",
        "GoogleCloudApigeeV1DeploymentGroupConfigOut": "_apigee_69_GoogleCloudApigeeV1DeploymentGroupConfigOut",
        "GoogleCloudApigeeV1DeploymentChangeReportRoutingConflictIn": "_apigee_70_GoogleCloudApigeeV1DeploymentChangeReportRoutingConflictIn",
        "GoogleCloudApigeeV1DeploymentChangeReportRoutingConflictOut": "_apigee_71_GoogleCloudApigeeV1DeploymentChangeReportRoutingConflictOut",
        "GoogleCloudApigeeV1QueryTimeSeriesStatsRequestIn": "_apigee_72_GoogleCloudApigeeV1QueryTimeSeriesStatsRequestIn",
        "GoogleCloudApigeeV1QueryTimeSeriesStatsRequestOut": "_apigee_73_GoogleCloudApigeeV1QueryTimeSeriesStatsRequestOut",
        "GoogleCloudApigeeV1EndpointAttachmentIn": "_apigee_74_GoogleCloudApigeeV1EndpointAttachmentIn",
        "GoogleCloudApigeeV1EndpointAttachmentOut": "_apigee_75_GoogleCloudApigeeV1EndpointAttachmentOut",
        "GoogleCloudApigeeV1ListInstanceAttachmentsResponseIn": "_apigee_76_GoogleCloudApigeeV1ListInstanceAttachmentsResponseIn",
        "GoogleCloudApigeeV1ListInstanceAttachmentsResponseOut": "_apigee_77_GoogleCloudApigeeV1ListInstanceAttachmentsResponseOut",
        "GoogleCloudApigeeV1ListAppsResponseIn": "_apigee_78_GoogleCloudApigeeV1ListAppsResponseIn",
        "GoogleCloudApigeeV1ListAppsResponseOut": "_apigee_79_GoogleCloudApigeeV1ListAppsResponseOut",
        "GoogleCloudApigeeV1ApiProductIn": "_apigee_80_GoogleCloudApigeeV1ApiProductIn",
        "GoogleCloudApigeeV1ApiProductOut": "_apigee_81_GoogleCloudApigeeV1ApiProductOut",
        "GoogleCloudApigeeV1SecurityReportQueryMetricIn": "_apigee_82_GoogleCloudApigeeV1SecurityReportQueryMetricIn",
        "GoogleCloudApigeeV1SecurityReportQueryMetricOut": "_apigee_83_GoogleCloudApigeeV1SecurityReportQueryMetricOut",
        "GoogleCloudApigeeV1ListInstancesResponseIn": "_apigee_84_GoogleCloudApigeeV1ListInstancesResponseIn",
        "GoogleCloudApigeeV1ListInstancesResponseOut": "_apigee_85_GoogleCloudApigeeV1ListInstancesResponseOut",
        "GoogleCloudApigeeV1AppIn": "_apigee_86_GoogleCloudApigeeV1AppIn",
        "GoogleCloudApigeeV1AppOut": "_apigee_87_GoogleCloudApigeeV1AppOut",
        "GoogleTypeMoneyIn": "_apigee_88_GoogleTypeMoneyIn",
        "GoogleTypeMoneyOut": "_apigee_89_GoogleTypeMoneyOut",
        "GoogleCloudApigeeV1SecurityReportQueryIn": "_apigee_90_GoogleCloudApigeeV1SecurityReportQueryIn",
        "GoogleCloudApigeeV1SecurityReportQueryOut": "_apigee_91_GoogleCloudApigeeV1SecurityReportQueryOut",
        "GoogleCloudApigeeV1AdvancedApiOpsConfigIn": "_apigee_92_GoogleCloudApigeeV1AdvancedApiOpsConfigIn",
        "GoogleCloudApigeeV1AdvancedApiOpsConfigOut": "_apigee_93_GoogleCloudApigeeV1AdvancedApiOpsConfigOut",
        "GoogleCloudApigeeV1CustomReportIn": "_apigee_94_GoogleCloudApigeeV1CustomReportIn",
        "GoogleCloudApigeeV1CustomReportOut": "_apigee_95_GoogleCloudApigeeV1CustomReportOut",
        "GoogleCloudApigeeV1DatastoreConfigIn": "_apigee_96_GoogleCloudApigeeV1DatastoreConfigIn",
        "GoogleCloudApigeeV1DatastoreConfigOut": "_apigee_97_GoogleCloudApigeeV1DatastoreConfigOut",
        "GoogleCloudApigeeV1ListDataCollectorsResponseIn": "_apigee_98_GoogleCloudApigeeV1ListDataCollectorsResponseIn",
        "GoogleCloudApigeeV1ListDataCollectorsResponseOut": "_apigee_99_GoogleCloudApigeeV1ListDataCollectorsResponseOut",
        "GoogleCloudApigeeV1ListCustomReportsResponseIn": "_apigee_100_GoogleCloudApigeeV1ListCustomReportsResponseIn",
        "GoogleCloudApigeeV1ListCustomReportsResponseOut": "_apigee_101_GoogleCloudApigeeV1ListCustomReportsResponseOut",
        "GoogleCloudApigeeV1CommonNameConfigIn": "_apigee_102_GoogleCloudApigeeV1CommonNameConfigIn",
        "GoogleCloudApigeeV1CommonNameConfigOut": "_apigee_103_GoogleCloudApigeeV1CommonNameConfigOut",
        "GoogleCloudApigeeV1SecurityReportResultViewIn": "_apigee_104_GoogleCloudApigeeV1SecurityReportResultViewIn",
        "GoogleCloudApigeeV1SecurityReportResultViewOut": "_apigee_105_GoogleCloudApigeeV1SecurityReportResultViewOut",
        "GoogleCloudApigeeV1InstanceIn": "_apigee_106_GoogleCloudApigeeV1InstanceIn",
        "GoogleCloudApigeeV1InstanceOut": "_apigee_107_GoogleCloudApigeeV1InstanceOut",
        "GoogleCloudApigeeV1StatsEnvironmentStatsIn": "_apigee_108_GoogleCloudApigeeV1StatsEnvironmentStatsIn",
        "GoogleCloudApigeeV1StatsEnvironmentStatsOut": "_apigee_109_GoogleCloudApigeeV1StatsEnvironmentStatsOut",
        "GoogleCloudApigeeV1QuotaIn": "_apigee_110_GoogleCloudApigeeV1QuotaIn",
        "GoogleCloudApigeeV1QuotaOut": "_apigee_111_GoogleCloudApigeeV1QuotaOut",
        "GoogleCloudApigeeV1EnvironmentGroupConfigIn": "_apigee_112_GoogleCloudApigeeV1EnvironmentGroupConfigIn",
        "GoogleCloudApigeeV1EnvironmentGroupConfigOut": "_apigee_113_GoogleCloudApigeeV1EnvironmentGroupConfigOut",
        "GoogleCloudApigeeV1QueryMetricIn": "_apigee_114_GoogleCloudApigeeV1QueryMetricIn",
        "GoogleCloudApigeeV1QueryMetricOut": "_apigee_115_GoogleCloudApigeeV1QueryMetricOut",
        "GoogleCloudApigeeV1AsyncQueryResultViewIn": "_apigee_116_GoogleCloudApigeeV1AsyncQueryResultViewIn",
        "GoogleCloudApigeeV1AsyncQueryResultViewOut": "_apigee_117_GoogleCloudApigeeV1AsyncQueryResultViewOut",
        "GoogleCloudApigeeV1ListKeyValueEntriesResponseIn": "_apigee_118_GoogleCloudApigeeV1ListKeyValueEntriesResponseIn",
        "GoogleCloudApigeeV1ListKeyValueEntriesResponseOut": "_apigee_119_GoogleCloudApigeeV1ListKeyValueEntriesResponseOut",
        "GoogleCloudApigeeV1QueryTimeSeriesStatsResponseSequenceIn": "_apigee_120_GoogleCloudApigeeV1QueryTimeSeriesStatsResponseSequenceIn",
        "GoogleCloudApigeeV1QueryTimeSeriesStatsResponseSequenceOut": "_apigee_121_GoogleCloudApigeeV1QueryTimeSeriesStatsResponseSequenceOut",
        "GoogleCloudApigeeV1ListEnvironmentGroupsResponseIn": "_apigee_122_GoogleCloudApigeeV1ListEnvironmentGroupsResponseIn",
        "GoogleCloudApigeeV1ListEnvironmentGroupsResponseOut": "_apigee_123_GoogleCloudApigeeV1ListEnvironmentGroupsResponseOut",
        "GoogleCloudApigeeV1ListHybridIssuersResponseIn": "_apigee_124_GoogleCloudApigeeV1ListHybridIssuersResponseIn",
        "GoogleCloudApigeeV1ListHybridIssuersResponseOut": "_apigee_125_GoogleCloudApigeeV1ListHybridIssuersResponseOut",
        "GoogleCloudApigeeV1AliasRevisionConfigIn": "_apigee_126_GoogleCloudApigeeV1AliasRevisionConfigIn",
        "GoogleCloudApigeeV1AliasRevisionConfigOut": "_apigee_127_GoogleCloudApigeeV1AliasRevisionConfigOut",
        "GoogleCloudApigeeV1SessionIn": "_apigee_128_GoogleCloudApigeeV1SessionIn",
        "GoogleCloudApigeeV1SessionOut": "_apigee_129_GoogleCloudApigeeV1SessionOut",
        "GoogleCloudApigeeV1ListEnvironmentResourcesResponseIn": "_apigee_130_GoogleCloudApigeeV1ListEnvironmentResourcesResponseIn",
        "GoogleCloudApigeeV1ListEnvironmentResourcesResponseOut": "_apigee_131_GoogleCloudApigeeV1ListEnvironmentResourcesResponseOut",
        "GoogleCloudApigeeV1AttributeIn": "_apigee_132_GoogleCloudApigeeV1AttributeIn",
        "GoogleCloudApigeeV1AttributeOut": "_apigee_133_GoogleCloudApigeeV1AttributeOut",
        "GoogleCloudApigeeV1DataCollectorConfigIn": "_apigee_134_GoogleCloudApigeeV1DataCollectorConfigIn",
        "GoogleCloudApigeeV1DataCollectorConfigOut": "_apigee_135_GoogleCloudApigeeV1DataCollectorConfigOut",
        "GoogleCloudApigeeV1NodeConfigIn": "_apigee_136_GoogleCloudApigeeV1NodeConfigIn",
        "GoogleCloudApigeeV1NodeConfigOut": "_apigee_137_GoogleCloudApigeeV1NodeConfigOut",
        "GoogleCloudApigeeV1OperationGroupIn": "_apigee_138_GoogleCloudApigeeV1OperationGroupIn",
        "GoogleCloudApigeeV1OperationGroupOut": "_apigee_139_GoogleCloudApigeeV1OperationGroupOut",
        "GoogleCloudApigeeV1KeystoreIn": "_apigee_140_GoogleCloudApigeeV1KeystoreIn",
        "GoogleCloudApigeeV1KeystoreOut": "_apigee_141_GoogleCloudApigeeV1KeystoreOut",
        "GoogleCloudApigeeV1ComputeEnvironmentScoresResponseIn": "_apigee_142_GoogleCloudApigeeV1ComputeEnvironmentScoresResponseIn",
        "GoogleCloudApigeeV1ComputeEnvironmentScoresResponseOut": "_apigee_143_GoogleCloudApigeeV1ComputeEnvironmentScoresResponseOut",
        "GoogleProtobufEmptyIn": "_apigee_144_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_apigee_145_GoogleProtobufEmptyOut",
        "GoogleCloudApigeeV1ListDeveloperSubscriptionsResponseIn": "_apigee_146_GoogleCloudApigeeV1ListDeveloperSubscriptionsResponseIn",
        "GoogleCloudApigeeV1ListDeveloperSubscriptionsResponseOut": "_apigee_147_GoogleCloudApigeeV1ListDeveloperSubscriptionsResponseOut",
        "GoogleCloudApigeeV1ReportPropertyIn": "_apigee_148_GoogleCloudApigeeV1ReportPropertyIn",
        "GoogleCloudApigeeV1ReportPropertyOut": "_apigee_149_GoogleCloudApigeeV1ReportPropertyOut",
        "GoogleCloudApigeeV1RuntimeTraceConfigIn": "_apigee_150_GoogleCloudApigeeV1RuntimeTraceConfigIn",
        "GoogleCloudApigeeV1RuntimeTraceConfigOut": "_apigee_151_GoogleCloudApigeeV1RuntimeTraceConfigOut",
        "GoogleCloudApigeeV1KeyValueMapIn": "_apigee_152_GoogleCloudApigeeV1KeyValueMapIn",
        "GoogleCloudApigeeV1KeyValueMapOut": "_apigee_153_GoogleCloudApigeeV1KeyValueMapOut",
        "GoogleCloudApigeeV1EnvironmentGroupIn": "_apigee_154_GoogleCloudApigeeV1EnvironmentGroupIn",
        "GoogleCloudApigeeV1EnvironmentGroupOut": "_apigee_155_GoogleCloudApigeeV1EnvironmentGroupOut",
        "GoogleCloudApigeeV1DataCollectorIn": "_apigee_156_GoogleCloudApigeeV1DataCollectorIn",
        "GoogleCloudApigeeV1DataCollectorOut": "_apigee_157_GoogleCloudApigeeV1DataCollectorOut",
        "GoogleCloudApigeeV1QueryTabularStatsRequestIn": "_apigee_158_GoogleCloudApigeeV1QueryTabularStatsRequestIn",
        "GoogleCloudApigeeV1QueryTabularStatsRequestOut": "_apigee_159_GoogleCloudApigeeV1QueryTabularStatsRequestOut",
        "GoogleCloudApigeeV1InstanceAttachmentIn": "_apigee_160_GoogleCloudApigeeV1InstanceAttachmentIn",
        "GoogleCloudApigeeV1InstanceAttachmentOut": "_apigee_161_GoogleCloudApigeeV1InstanceAttachmentOut",
        "GoogleCloudApigeeV1MetricIn": "_apigee_162_GoogleCloudApigeeV1MetricIn",
        "GoogleCloudApigeeV1MetricOut": "_apigee_163_GoogleCloudApigeeV1MetricOut",
        "GoogleCloudApigeeV1CanaryEvaluationMetricLabelsIn": "_apigee_164_GoogleCloudApigeeV1CanaryEvaluationMetricLabelsIn",
        "GoogleCloudApigeeV1CanaryEvaluationMetricLabelsOut": "_apigee_165_GoogleCloudApigeeV1CanaryEvaluationMetricLabelsOut",
        "GoogleCloudApigeeV1AsyncQueryResultIn": "_apigee_166_GoogleCloudApigeeV1AsyncQueryResultIn",
        "GoogleCloudApigeeV1AsyncQueryResultOut": "_apigee_167_GoogleCloudApigeeV1AsyncQueryResultOut",
        "GoogleRpcStatusIn": "_apigee_168_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_apigee_169_GoogleRpcStatusOut",
        "GoogleCloudApigeeV1ServiceIssuersMappingIn": "_apigee_170_GoogleCloudApigeeV1ServiceIssuersMappingIn",
        "GoogleCloudApigeeV1ServiceIssuersMappingOut": "_apigee_171_GoogleCloudApigeeV1ServiceIssuersMappingOut",
        "GoogleCloudApigeeV1OperationMetadataProgressIn": "_apigee_172_GoogleCloudApigeeV1OperationMetadataProgressIn",
        "GoogleCloudApigeeV1OperationMetadataProgressOut": "_apigee_173_GoogleCloudApigeeV1OperationMetadataProgressOut",
        "GoogleCloudApigeeV1TestDatastoreResponseIn": "_apigee_174_GoogleCloudApigeeV1TestDatastoreResponseIn",
        "GoogleCloudApigeeV1TestDatastoreResponseOut": "_apigee_175_GoogleCloudApigeeV1TestDatastoreResponseOut",
        "GoogleCloudApigeeV1ApiCategoryDataIn": "_apigee_176_GoogleCloudApigeeV1ApiCategoryDataIn",
        "GoogleCloudApigeeV1ApiCategoryDataOut": "_apigee_177_GoogleCloudApigeeV1ApiCategoryDataOut",
        "GoogleCloudApigeeV1GraphQLOperationConfigIn": "_apigee_178_GoogleCloudApigeeV1GraphQLOperationConfigIn",
        "GoogleCloudApigeeV1GraphQLOperationConfigOut": "_apigee_179_GoogleCloudApigeeV1GraphQLOperationConfigOut",
        "GoogleTypeExprIn": "_apigee_180_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_apigee_181_GoogleTypeExprOut",
        "GoogleCloudApigeeV1ReportInstanceStatusRequestIn": "_apigee_182_GoogleCloudApigeeV1ReportInstanceStatusRequestIn",
        "GoogleCloudApigeeV1ReportInstanceStatusRequestOut": "_apigee_183_GoogleCloudApigeeV1ReportInstanceStatusRequestOut",
        "GoogleCloudApigeeV1CredentialIn": "_apigee_184_GoogleCloudApigeeV1CredentialIn",
        "GoogleCloudApigeeV1CredentialOut": "_apigee_185_GoogleCloudApigeeV1CredentialOut",
        "GoogleCloudApigeeV1SharedFlowIn": "_apigee_186_GoogleCloudApigeeV1SharedFlowIn",
        "GoogleCloudApigeeV1SharedFlowOut": "_apigee_187_GoogleCloudApigeeV1SharedFlowOut",
        "GoogleCloudApigeeV1DebugMaskIn": "_apigee_188_GoogleCloudApigeeV1DebugMaskIn",
        "GoogleCloudApigeeV1DebugMaskOut": "_apigee_189_GoogleCloudApigeeV1DebugMaskOut",
        "GoogleLongrunningOperationIn": "_apigee_190_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_apigee_191_GoogleLongrunningOperationOut",
        "GoogleCloudApigeeV1GraphQLOperationIn": "_apigee_192_GoogleCloudApigeeV1GraphQLOperationIn",
        "GoogleCloudApigeeV1GraphQLOperationOut": "_apigee_193_GoogleCloudApigeeV1GraphQLOperationOut",
        "GoogleCloudApigeeV1CertificateIn": "_apigee_194_GoogleCloudApigeeV1CertificateIn",
        "GoogleCloudApigeeV1CertificateOut": "_apigee_195_GoogleCloudApigeeV1CertificateOut",
        "GoogleCloudApigeeV1AccessGetIn": "_apigee_196_GoogleCloudApigeeV1AccessGetIn",
        "GoogleCloudApigeeV1AccessGetOut": "_apigee_197_GoogleCloudApigeeV1AccessGetOut",
        "GoogleCloudApigeeV1DebugSessionTransactionIn": "_apigee_198_GoogleCloudApigeeV1DebugSessionTransactionIn",
        "GoogleCloudApigeeV1DebugSessionTransactionOut": "_apigee_199_GoogleCloudApigeeV1DebugSessionTransactionOut",
        "GoogleCloudApigeeV1RevisionStatusIn": "_apigee_200_GoogleCloudApigeeV1RevisionStatusIn",
        "GoogleCloudApigeeV1RevisionStatusOut": "_apigee_201_GoogleCloudApigeeV1RevisionStatusOut",
        "GoogleCloudApigeeV1ResourceConfigIn": "_apigee_202_GoogleCloudApigeeV1ResourceConfigIn",
        "GoogleCloudApigeeV1ResourceConfigOut": "_apigee_203_GoogleCloudApigeeV1ResourceConfigOut",
        "GoogleCloudApigeeV1ApiSecurityConfigIn": "_apigee_204_GoogleCloudApigeeV1ApiSecurityConfigIn",
        "GoogleCloudApigeeV1ApiSecurityConfigOut": "_apigee_205_GoogleCloudApigeeV1ApiSecurityConfigOut",
        "GoogleCloudApigeeV1SecurityProfileIn": "_apigee_206_GoogleCloudApigeeV1SecurityProfileIn",
        "GoogleCloudApigeeV1SecurityProfileOut": "_apigee_207_GoogleCloudApigeeV1SecurityProfileOut",
        "GoogleCloudApigeeV1EndpointChainingRuleIn": "_apigee_208_GoogleCloudApigeeV1EndpointChainingRuleIn",
        "GoogleCloudApigeeV1EndpointChainingRuleOut": "_apigee_209_GoogleCloudApigeeV1EndpointChainingRuleOut",
        "GoogleCloudApigeeV1ScoreComponentRecommendationActionActionContextIn": "_apigee_210_GoogleCloudApigeeV1ScoreComponentRecommendationActionActionContextIn",
        "GoogleCloudApigeeV1ScoreComponentRecommendationActionActionContextOut": "_apigee_211_GoogleCloudApigeeV1ScoreComponentRecommendationActionActionContextOut",
        "GoogleCloudApigeeV1SchemaSchemaElementIn": "_apigee_212_GoogleCloudApigeeV1SchemaSchemaElementIn",
        "GoogleCloudApigeeV1SchemaSchemaElementOut": "_apigee_213_GoogleCloudApigeeV1SchemaSchemaElementOut",
        "GoogleCloudApigeeV1RuntimeConfigIn": "_apigee_214_GoogleCloudApigeeV1RuntimeConfigIn",
        "GoogleCloudApigeeV1RuntimeConfigOut": "_apigee_215_GoogleCloudApigeeV1RuntimeConfigOut",
        "GoogleCloudApigeeV1PointIn": "_apigee_216_GoogleCloudApigeeV1PointIn",
        "GoogleCloudApigeeV1PointOut": "_apigee_217_GoogleCloudApigeeV1PointOut",
        "GoogleCloudApigeeV1ApiProductRefIn": "_apigee_218_GoogleCloudApigeeV1ApiProductRefIn",
        "GoogleCloudApigeeV1ApiProductRefOut": "_apigee_219_GoogleCloudApigeeV1ApiProductRefOut",
        "GoogleCloudApigeeV1SecurityReportIn": "_apigee_220_GoogleCloudApigeeV1SecurityReportIn",
        "GoogleCloudApigeeV1SecurityReportOut": "_apigee_221_GoogleCloudApigeeV1SecurityReportOut",
        "GoogleCloudApigeeV1ArchiveDeploymentIn": "_apigee_222_GoogleCloudApigeeV1ArchiveDeploymentIn",
        "GoogleCloudApigeeV1ArchiveDeploymentOut": "_apigee_223_GoogleCloudApigeeV1ArchiveDeploymentOut",
        "GoogleCloudApigeeV1CustomReportMetricIn": "_apigee_224_GoogleCloudApigeeV1CustomReportMetricIn",
        "GoogleCloudApigeeV1CustomReportMetricOut": "_apigee_225_GoogleCloudApigeeV1CustomReportMetricOut",
        "GoogleCloudApigeeV1RuntimeTraceSamplingConfigIn": "_apigee_226_GoogleCloudApigeeV1RuntimeTraceSamplingConfigIn",
        "GoogleCloudApigeeV1RuntimeTraceSamplingConfigOut": "_apigee_227_GoogleCloudApigeeV1RuntimeTraceSamplingConfigOut",
        "GoogleIamV1BindingIn": "_apigee_228_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_apigee_229_GoogleIamV1BindingOut",
        "GoogleCloudApigeeV1ResourceFileIn": "_apigee_230_GoogleCloudApigeeV1ResourceFileIn",
        "GoogleCloudApigeeV1ResourceFileOut": "_apigee_231_GoogleCloudApigeeV1ResourceFileOut",
        "GoogleCloudApigeeV1KeyAliasReferenceIn": "_apigee_232_GoogleCloudApigeeV1KeyAliasReferenceIn",
        "GoogleCloudApigeeV1KeyAliasReferenceOut": "_apigee_233_GoogleCloudApigeeV1KeyAliasReferenceOut",
        "GoogleLongrunningListOperationsResponseIn": "_apigee_234_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_apigee_235_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudApigeeV1DeploymentChangeReportRoutingChangeIn": "_apigee_236_GoogleCloudApigeeV1DeploymentChangeReportRoutingChangeIn",
        "GoogleCloudApigeeV1DeploymentChangeReportRoutingChangeOut": "_apigee_237_GoogleCloudApigeeV1DeploymentChangeReportRoutingChangeOut",
        "GoogleIamV1PolicyIn": "_apigee_238_GoogleIamV1PolicyIn",
        "GoogleIamV1PolicyOut": "_apigee_239_GoogleIamV1PolicyOut",
        "GoogleCloudApigeeV1ResultIn": "_apigee_240_GoogleCloudApigeeV1ResultIn",
        "GoogleCloudApigeeV1ResultOut": "_apigee_241_GoogleCloudApigeeV1ResultOut",
        "GoogleTypeIntervalIn": "_apigee_242_GoogleTypeIntervalIn",
        "GoogleTypeIntervalOut": "_apigee_243_GoogleTypeIntervalOut",
        "GoogleCloudApigeeV1QueryMetadataIn": "_apigee_244_GoogleCloudApigeeV1QueryMetadataIn",
        "GoogleCloudApigeeV1QueryMetadataOut": "_apigee_245_GoogleCloudApigeeV1QueryMetadataOut",
        "GoogleCloudApigeeV1SecurityProfileEnvironmentIn": "_apigee_246_GoogleCloudApigeeV1SecurityProfileEnvironmentIn",
        "GoogleCloudApigeeV1SecurityProfileEnvironmentOut": "_apigee_247_GoogleCloudApigeeV1SecurityProfileEnvironmentOut",
        "GoogleCloudApigeeV1IntegrationConfigIn": "_apigee_248_GoogleCloudApigeeV1IntegrationConfigIn",
        "GoogleCloudApigeeV1IntegrationConfigOut": "_apigee_249_GoogleCloudApigeeV1IntegrationConfigOut",
        "GoogleCloudApigeeV1OperationIn": "_apigee_250_GoogleCloudApigeeV1OperationIn",
        "GoogleCloudApigeeV1OperationOut": "_apigee_251_GoogleCloudApigeeV1OperationOut",
        "GoogleCloudApigeeV1SecurityReportMetadataIn": "_apigee_252_GoogleCloudApigeeV1SecurityReportMetadataIn",
        "GoogleCloudApigeeV1SecurityReportMetadataOut": "_apigee_253_GoogleCloudApigeeV1SecurityReportMetadataOut",
        "GoogleCloudApigeeV1ReportInstanceStatusResponseIn": "_apigee_254_GoogleCloudApigeeV1ReportInstanceStatusResponseIn",
        "GoogleCloudApigeeV1ReportInstanceStatusResponseOut": "_apigee_255_GoogleCloudApigeeV1ReportInstanceStatusResponseOut",
        "GoogleCloudApigeeV1TlsInfoIn": "_apigee_256_GoogleCloudApigeeV1TlsInfoIn",
        "GoogleCloudApigeeV1TlsInfoOut": "_apigee_257_GoogleCloudApigeeV1TlsInfoOut",
        "GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponseIn": "_apigee_258_GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponseIn",
        "GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponseOut": "_apigee_259_GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponseOut",
        "GoogleCloudApigeeV1TlsInfoCommonNameIn": "_apigee_260_GoogleCloudApigeeV1TlsInfoCommonNameIn",
        "GoogleCloudApigeeV1TlsInfoCommonNameOut": "_apigee_261_GoogleCloudApigeeV1TlsInfoCommonNameOut",
        "GoogleCloudApigeeV1GetSyncAuthorizationRequestIn": "_apigee_262_GoogleCloudApigeeV1GetSyncAuthorizationRequestIn",
        "GoogleCloudApigeeV1GetSyncAuthorizationRequestOut": "_apigee_263_GoogleCloudApigeeV1GetSyncAuthorizationRequestOut",
        "GoogleCloudApigeeV1ScoreIn": "_apigee_264_GoogleCloudApigeeV1ScoreIn",
        "GoogleCloudApigeeV1ScoreOut": "_apigee_265_GoogleCloudApigeeV1ScoreOut",
        "GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRouteIn": "_apigee_266_GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRouteIn",
        "GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRouteOut": "_apigee_267_GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRouteOut",
        "GoogleCloudApigeeV1DebugSessionIn": "_apigee_268_GoogleCloudApigeeV1DebugSessionIn",
        "GoogleCloudApigeeV1DebugSessionOut": "_apigee_269_GoogleCloudApigeeV1DebugSessionOut",
        "GoogleCloudApigeeV1ListSecurityProfilesResponseIn": "_apigee_270_GoogleCloudApigeeV1ListSecurityProfilesResponseIn",
        "GoogleCloudApigeeV1ListSecurityProfilesResponseOut": "_apigee_271_GoogleCloudApigeeV1ListSecurityProfilesResponseOut",
        "GoogleCloudApigeeV1SecurityReportResultMetadataIn": "_apigee_272_GoogleCloudApigeeV1SecurityReportResultMetadataIn",
        "GoogleCloudApigeeV1SecurityReportResultMetadataOut": "_apigee_273_GoogleCloudApigeeV1SecurityReportResultMetadataOut",
        "GoogleCloudApigeeV1EnvironmentGroupAttachmentIn": "_apigee_274_GoogleCloudApigeeV1EnvironmentGroupAttachmentIn",
        "GoogleCloudApigeeV1EnvironmentGroupAttachmentOut": "_apigee_275_GoogleCloudApigeeV1EnvironmentGroupAttachmentOut",
        "GoogleCloudApigeeV1SecurityIncidentIn": "_apigee_276_GoogleCloudApigeeV1SecurityIncidentIn",
        "GoogleCloudApigeeV1SecurityIncidentOut": "_apigee_277_GoogleCloudApigeeV1SecurityIncidentOut",
        "GoogleCloudApigeeV1ConfigVersionIn": "_apigee_278_GoogleCloudApigeeV1ConfigVersionIn",
        "GoogleCloudApigeeV1ConfigVersionOut": "_apigee_279_GoogleCloudApigeeV1ConfigVersionOut",
        "GoogleCloudApigeeV1ApiProxyRevisionIn": "_apigee_280_GoogleCloudApigeeV1ApiProxyRevisionIn",
        "GoogleCloudApigeeV1ApiProxyRevisionOut": "_apigee_281_GoogleCloudApigeeV1ApiProxyRevisionOut",
        "GoogleCloudApigeeV1SchemaIn": "_apigee_282_GoogleCloudApigeeV1SchemaIn",
        "GoogleCloudApigeeV1SchemaOut": "_apigee_283_GoogleCloudApigeeV1SchemaOut",
        "GoogleIamV1TestIamPermissionsResponseIn": "_apigee_284_GoogleIamV1TestIamPermissionsResponseIn",
        "GoogleIamV1TestIamPermissionsResponseOut": "_apigee_285_GoogleIamV1TestIamPermissionsResponseOut",
        "GoogleCloudApigeeV1RatePlanIn": "_apigee_286_GoogleCloudApigeeV1RatePlanIn",
        "GoogleCloudApigeeV1RatePlanOut": "_apigee_287_GoogleCloudApigeeV1RatePlanOut",
        "GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilterIn": "_apigee_288_GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilterIn",
        "GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilterOut": "_apigee_289_GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilterOut",
        "GoogleCloudApigeeV1OptimizedStatsIn": "_apigee_290_GoogleCloudApigeeV1OptimizedStatsIn",
        "GoogleCloudApigeeV1OptimizedStatsOut": "_apigee_291_GoogleCloudApigeeV1OptimizedStatsOut",
        "GoogleCloudApigeeV1ListSecurityReportsResponseIn": "_apigee_292_GoogleCloudApigeeV1ListSecurityReportsResponseIn",
        "GoogleCloudApigeeV1ListSecurityReportsResponseOut": "_apigee_293_GoogleCloudApigeeV1ListSecurityReportsResponseOut",
        "GoogleCloudApigeeV1TargetServerIn": "_apigee_294_GoogleCloudApigeeV1TargetServerIn",
        "GoogleCloudApigeeV1TargetServerOut": "_apigee_295_GoogleCloudApigeeV1TargetServerOut",
        "GoogleCloudApigeeV1ListDatastoresResponseIn": "_apigee_296_GoogleCloudApigeeV1ListDatastoresResponseIn",
        "GoogleCloudApigeeV1ListDatastoresResponseOut": "_apigee_297_GoogleCloudApigeeV1ListDatastoresResponseOut",
        "GoogleCloudApigeeV1RuntimeTraceConfigOverrideIn": "_apigee_298_GoogleCloudApigeeV1RuntimeTraceConfigOverrideIn",
        "GoogleCloudApigeeV1RuntimeTraceConfigOverrideOut": "_apigee_299_GoogleCloudApigeeV1RuntimeTraceConfigOverrideOut",
        "GoogleCloudApigeeV1ExportIn": "_apigee_300_GoogleCloudApigeeV1ExportIn",
        "GoogleCloudApigeeV1ExportOut": "_apigee_301_GoogleCloudApigeeV1ExportOut",
        "GoogleCloudApigeeV1DeveloperBalanceIn": "_apigee_302_GoogleCloudApigeeV1DeveloperBalanceIn",
        "GoogleCloudApigeeV1DeveloperBalanceOut": "_apigee_303_GoogleCloudApigeeV1DeveloperBalanceOut",
        "GoogleIamV1AuditLogConfigIn": "_apigee_304_GoogleIamV1AuditLogConfigIn",
        "GoogleIamV1AuditLogConfigOut": "_apigee_305_GoogleIamV1AuditLogConfigOut",
        "GoogleCloudApigeeV1InstanceDeploymentStatusIn": "_apigee_306_GoogleCloudApigeeV1InstanceDeploymentStatusIn",
        "GoogleCloudApigeeV1InstanceDeploymentStatusOut": "_apigee_307_GoogleCloudApigeeV1InstanceDeploymentStatusOut",
        "GoogleCloudApigeeV1TraceConfigOverrideIn": "_apigee_308_GoogleCloudApigeeV1TraceConfigOverrideIn",
        "GoogleCloudApigeeV1TraceConfigOverrideOut": "_apigee_309_GoogleCloudApigeeV1TraceConfigOverrideOut",
        "GoogleCloudApigeeV1DeveloperAppIn": "_apigee_310_GoogleCloudApigeeV1DeveloperAppIn",
        "GoogleCloudApigeeV1DeveloperAppOut": "_apigee_311_GoogleCloudApigeeV1DeveloperAppOut",
        "GoogleCloudApigeeV1GraphQLOperationGroupIn": "_apigee_312_GoogleCloudApigeeV1GraphQLOperationGroupIn",
        "GoogleCloudApigeeV1GraphQLOperationGroupOut": "_apigee_313_GoogleCloudApigeeV1GraphQLOperationGroupOut",
        "GoogleCloudApigeeV1ListSharedFlowsResponseIn": "_apigee_314_GoogleCloudApigeeV1ListSharedFlowsResponseIn",
        "GoogleCloudApigeeV1ListSharedFlowsResponseOut": "_apigee_315_GoogleCloudApigeeV1ListSharedFlowsResponseOut",
        "GoogleCloudApigeeV1EnvironmentIn": "_apigee_316_GoogleCloudApigeeV1EnvironmentIn",
        "GoogleCloudApigeeV1EnvironmentOut": "_apigee_317_GoogleCloudApigeeV1EnvironmentOut",
        "GoogleCloudApigeeV1QueryTabularStatsResponseIn": "_apigee_318_GoogleCloudApigeeV1QueryTabularStatsResponseIn",
        "GoogleCloudApigeeV1QueryTabularStatsResponseOut": "_apigee_319_GoogleCloudApigeeV1QueryTabularStatsResponseOut",
        "GoogleApiHttpBodyIn": "_apigee_320_GoogleApiHttpBodyIn",
        "GoogleApiHttpBodyOut": "_apigee_321_GoogleApiHttpBodyOut",
        "GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseURLInfoIn": "_apigee_322_GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseURLInfoIn",
        "GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseURLInfoOut": "_apigee_323_GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseURLInfoOut",
        "GoogleCloudApigeeV1ActivateNatAddressRequestIn": "_apigee_324_GoogleCloudApigeeV1ActivateNatAddressRequestIn",
        "GoogleCloudApigeeV1ActivateNatAddressRequestOut": "_apigee_325_GoogleCloudApigeeV1ActivateNatAddressRequestOut",
        "GoogleCloudApigeeV1IngressConfigIn": "_apigee_326_GoogleCloudApigeeV1IngressConfigIn",
        "GoogleCloudApigeeV1IngressConfigOut": "_apigee_327_GoogleCloudApigeeV1IngressConfigOut",
        "GoogleCloudApigeeV1DeploymentChangeReportIn": "_apigee_328_GoogleCloudApigeeV1DeploymentChangeReportIn",
        "GoogleCloudApigeeV1DeploymentChangeReportOut": "_apigee_329_GoogleCloudApigeeV1DeploymentChangeReportOut",
        "GoogleCloudApigeeV1SharedFlowRevisionIn": "_apigee_330_GoogleCloudApigeeV1SharedFlowRevisionIn",
        "GoogleCloudApigeeV1SharedFlowRevisionOut": "_apigee_331_GoogleCloudApigeeV1SharedFlowRevisionOut",
        "GoogleCloudApigeeV1ListExportsResponseIn": "_apigee_332_GoogleCloudApigeeV1ListExportsResponseIn",
        "GoogleCloudApigeeV1ListExportsResponseOut": "_apigee_333_GoogleCloudApigeeV1ListExportsResponseOut",
        "GoogleCloudApigeeV1UpdateErrorIn": "_apigee_334_GoogleCloudApigeeV1UpdateErrorIn",
        "GoogleCloudApigeeV1UpdateErrorOut": "_apigee_335_GoogleCloudApigeeV1UpdateErrorOut",
        "GoogleCloudApigeeV1NatAddressIn": "_apigee_336_GoogleCloudApigeeV1NatAddressIn",
        "GoogleCloudApigeeV1NatAddressOut": "_apigee_337_GoogleCloudApigeeV1NatAddressOut",
        "EdgeConfigstoreBundleBadBundleIn": "_apigee_338_EdgeConfigstoreBundleBadBundleIn",
        "EdgeConfigstoreBundleBadBundleOut": "_apigee_339_EdgeConfigstoreBundleBadBundleOut",
        "GoogleCloudApigeeV1SecurityProfileEnvironmentAssociationIn": "_apigee_340_GoogleCloudApigeeV1SecurityProfileEnvironmentAssociationIn",
        "GoogleCloudApigeeV1SecurityProfileEnvironmentAssociationOut": "_apigee_341_GoogleCloudApigeeV1SecurityProfileEnvironmentAssociationOut",
        "GoogleCloudApigeeV1RateRangeIn": "_apigee_342_GoogleCloudApigeeV1RateRangeIn",
        "GoogleCloudApigeeV1RateRangeOut": "_apigee_343_GoogleCloudApigeeV1RateRangeOut",
        "GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseIn": "_apigee_344_GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseIn",
        "GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseOut": "_apigee_345_GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseOut",
        "GoogleCloudApigeeV1KeystoreConfigIn": "_apigee_346_GoogleCloudApigeeV1KeystoreConfigIn",
        "GoogleCloudApigeeV1KeystoreConfigOut": "_apigee_347_GoogleCloudApigeeV1KeystoreConfigOut",
        "GoogleCloudApigeeV1DeleteResponseIn": "_apigee_348_GoogleCloudApigeeV1DeleteResponseIn",
        "GoogleCloudApigeeV1DeleteResponseOut": "_apigee_349_GoogleCloudApigeeV1DeleteResponseOut",
        "GoogleCloudApigeeV1AddonsConfigIn": "_apigee_350_GoogleCloudApigeeV1AddonsConfigIn",
        "GoogleCloudApigeeV1AddonsConfigOut": "_apigee_351_GoogleCloudApigeeV1AddonsConfigOut",
        "GoogleCloudApigeeV1DeveloperBalanceWalletIn": "_apigee_352_GoogleCloudApigeeV1DeveloperBalanceWalletIn",
        "GoogleCloudApigeeV1DeveloperBalanceWalletOut": "_apigee_353_GoogleCloudApigeeV1DeveloperBalanceWalletOut",
        "GoogleCloudApigeeV1ResourceStatusIn": "_apigee_354_GoogleCloudApigeeV1ResourceStatusIn",
        "GoogleCloudApigeeV1ResourceStatusOut": "_apigee_355_GoogleCloudApigeeV1ResourceStatusOut",
        "GoogleCloudApigeeV1DimensionMetricIn": "_apigee_356_GoogleCloudApigeeV1DimensionMetricIn",
        "GoogleCloudApigeeV1DimensionMetricOut": "_apigee_357_GoogleCloudApigeeV1DimensionMetricOut",
        "GoogleCloudApigeeV1GenerateDownloadUrlResponseIn": "_apigee_358_GoogleCloudApigeeV1GenerateDownloadUrlResponseIn",
        "GoogleCloudApigeeV1GenerateDownloadUrlResponseOut": "_apigee_359_GoogleCloudApigeeV1GenerateDownloadUrlResponseOut",
        "GoogleCloudApigeeV1DeveloperMonetizationConfigIn": "_apigee_360_GoogleCloudApigeeV1DeveloperMonetizationConfigIn",
        "GoogleCloudApigeeV1DeveloperMonetizationConfigOut": "_apigee_361_GoogleCloudApigeeV1DeveloperMonetizationConfigOut",
        "GoogleCloudApigeeV1ListDeveloperAppsResponseIn": "_apigee_362_GoogleCloudApigeeV1ListDeveloperAppsResponseIn",
        "GoogleCloudApigeeV1ListDeveloperAppsResponseOut": "_apigee_363_GoogleCloudApigeeV1ListDeveloperAppsResponseOut",
        "GoogleCloudApigeeV1FlowHookConfigIn": "_apigee_364_GoogleCloudApigeeV1FlowHookConfigIn",
        "GoogleCloudApigeeV1FlowHookConfigOut": "_apigee_365_GoogleCloudApigeeV1FlowHookConfigOut",
        "GoogleCloudApigeeV1ListTraceConfigOverridesResponseIn": "_apigee_366_GoogleCloudApigeeV1ListTraceConfigOverridesResponseIn",
        "GoogleCloudApigeeV1ListTraceConfigOverridesResponseOut": "_apigee_367_GoogleCloudApigeeV1ListTraceConfigOverridesResponseOut",
        "GoogleCloudApigeeV1QueryIn": "_apigee_368_GoogleCloudApigeeV1QueryIn",
        "GoogleCloudApigeeV1QueryOut": "_apigee_369_GoogleCloudApigeeV1QueryOut",
        "GoogleCloudApigeeV1ScoreComponentRecommendationActionIn": "_apigee_370_GoogleCloudApigeeV1ScoreComponentRecommendationActionIn",
        "GoogleCloudApigeeV1ScoreComponentRecommendationActionOut": "_apigee_371_GoogleCloudApigeeV1ScoreComponentRecommendationActionOut",
        "GoogleCloudApigeeV1DeveloperIn": "_apigee_372_GoogleCloudApigeeV1DeveloperIn",
        "GoogleCloudApigeeV1DeveloperOut": "_apigee_373_GoogleCloudApigeeV1DeveloperOut",
        "GoogleIamV1SetIamPolicyRequestIn": "_apigee_374_GoogleIamV1SetIamPolicyRequestIn",
        "GoogleIamV1SetIamPolicyRequestOut": "_apigee_375_GoogleIamV1SetIamPolicyRequestOut",
        "GoogleCloudApigeeV1MetricAggregationIn": "_apigee_376_GoogleCloudApigeeV1MetricAggregationIn",
        "GoogleCloudApigeeV1MetricAggregationOut": "_apigee_377_GoogleCloudApigeeV1MetricAggregationOut",
        "GoogleCloudApigeeV1StatsHostStatsIn": "_apigee_378_GoogleCloudApigeeV1StatsHostStatsIn",
        "GoogleCloudApigeeV1StatsHostStatsOut": "_apigee_379_GoogleCloudApigeeV1StatsHostStatsOut",
        "GoogleCloudApigeeV1OrganizationProjectMappingIn": "_apigee_380_GoogleCloudApigeeV1OrganizationProjectMappingIn",
        "GoogleCloudApigeeV1OrganizationProjectMappingOut": "_apigee_381_GoogleCloudApigeeV1OrganizationProjectMappingOut",
        "GoogleCloudApigeeV1ListDeploymentsResponseIn": "_apigee_382_GoogleCloudApigeeV1ListDeploymentsResponseIn",
        "GoogleCloudApigeeV1ListDeploymentsResponseOut": "_apigee_383_GoogleCloudApigeeV1ListDeploymentsResponseOut",
        "GoogleCloudApigeeV1ListAsyncQueriesResponseIn": "_apigee_384_GoogleCloudApigeeV1ListAsyncQueriesResponseIn",
        "GoogleCloudApigeeV1ListAsyncQueriesResponseOut": "_apigee_385_GoogleCloudApigeeV1ListAsyncQueriesResponseOut",
        "GoogleCloudApigeeV1OptimizedStatsResponseIn": "_apigee_386_GoogleCloudApigeeV1OptimizedStatsResponseIn",
        "GoogleCloudApigeeV1OptimizedStatsResponseOut": "_apigee_387_GoogleCloudApigeeV1OptimizedStatsResponseOut",
        "GoogleCloudApigeeV1SubscriptionIn": "_apigee_388_GoogleCloudApigeeV1SubscriptionIn",
        "GoogleCloudApigeeV1SubscriptionOut": "_apigee_389_GoogleCloudApigeeV1SubscriptionOut",
        "GoogleCloudApigeeV1ExportRequestIn": "_apigee_390_GoogleCloudApigeeV1ExportRequestIn",
        "GoogleCloudApigeeV1ExportRequestOut": "_apigee_391_GoogleCloudApigeeV1ExportRequestOut",
        "GoogleCloudApigeeV1ListSecurityProfileRevisionsResponseIn": "_apigee_392_GoogleCloudApigeeV1ListSecurityProfileRevisionsResponseIn",
        "GoogleCloudApigeeV1ListSecurityProfileRevisionsResponseOut": "_apigee_393_GoogleCloudApigeeV1ListSecurityProfileRevisionsResponseOut",
        "GoogleCloudApigeeV1TlsInfoConfigIn": "_apigee_394_GoogleCloudApigeeV1TlsInfoConfigIn",
        "GoogleCloudApigeeV1TlsInfoConfigOut": "_apigee_395_GoogleCloudApigeeV1TlsInfoConfigOut",
        "GoogleCloudApigeeV1EnvironmentConfigIn": "_apigee_396_GoogleCloudApigeeV1EnvironmentConfigIn",
        "GoogleCloudApigeeV1EnvironmentConfigOut": "_apigee_397_GoogleCloudApigeeV1EnvironmentConfigOut",
        "GoogleCloudApigeeV1AliasIn": "_apigee_398_GoogleCloudApigeeV1AliasIn",
        "GoogleCloudApigeeV1AliasOut": "_apigee_399_GoogleCloudApigeeV1AliasOut",
        "GoogleCloudApigeeV1PropertyIn": "_apigee_400_GoogleCloudApigeeV1PropertyIn",
        "GoogleCloudApigeeV1PropertyOut": "_apigee_401_GoogleCloudApigeeV1PropertyOut",
        "GoogleCloudApigeeV1ListArchiveDeploymentsResponseIn": "_apigee_402_GoogleCloudApigeeV1ListArchiveDeploymentsResponseIn",
        "GoogleCloudApigeeV1ListArchiveDeploymentsResponseOut": "_apigee_403_GoogleCloudApigeeV1ListArchiveDeploymentsResponseOut",
        "GoogleCloudApigeeV1GenerateUploadUrlRequestIn": "_apigee_404_GoogleCloudApigeeV1GenerateUploadUrlRequestIn",
        "GoogleCloudApigeeV1GenerateUploadUrlRequestOut": "_apigee_405_GoogleCloudApigeeV1GenerateUploadUrlRequestOut",
        "GoogleCloudApigeeV1GenerateDownloadUrlRequestIn": "_apigee_406_GoogleCloudApigeeV1GenerateDownloadUrlRequestIn",
        "GoogleCloudApigeeV1GenerateDownloadUrlRequestOut": "_apigee_407_GoogleCloudApigeeV1GenerateDownloadUrlRequestOut",
        "GoogleCloudApigeeV1ListNatAddressesResponseIn": "_apigee_408_GoogleCloudApigeeV1ListNatAddressesResponseIn",
        "GoogleCloudApigeeV1ListNatAddressesResponseOut": "_apigee_409_GoogleCloudApigeeV1ListNatAddressesResponseOut",
        "GoogleCloudApigeeV1AccessRemoveIn": "_apigee_410_GoogleCloudApigeeV1AccessRemoveIn",
        "GoogleCloudApigeeV1AccessRemoveOut": "_apigee_411_GoogleCloudApigeeV1AccessRemoveOut",
        "GoogleCloudApigeeV1ListApiCategoriesResponseIn": "_apigee_412_GoogleCloudApigeeV1ListApiCategoriesResponseIn",
        "GoogleCloudApigeeV1ListApiCategoriesResponseOut": "_apigee_413_GoogleCloudApigeeV1ListApiCategoriesResponseOut",
        "GoogleCloudApigeeV1StatsIn": "_apigee_414_GoogleCloudApigeeV1StatsIn",
        "GoogleCloudApigeeV1StatsOut": "_apigee_415_GoogleCloudApigeeV1StatsOut",
        "GoogleCloudApigeeV1ListOfDevelopersResponseIn": "_apigee_416_GoogleCloudApigeeV1ListOfDevelopersResponseIn",
        "GoogleCloudApigeeV1ListOfDevelopersResponseOut": "_apigee_417_GoogleCloudApigeeV1ListOfDevelopersResponseOut",
        "GoogleCloudApigeeV1DeleteCustomReportResponseIn": "_apigee_418_GoogleCloudApigeeV1DeleteCustomReportResponseIn",
        "GoogleCloudApigeeV1DeleteCustomReportResponseOut": "_apigee_419_GoogleCloudApigeeV1DeleteCustomReportResponseOut",
        "GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentIn": "_apigee_420_GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentIn",
        "GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentOut": "_apigee_421_GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentOut",
        "GoogleCloudApigeeV1ListSecurityIncidentsResponseIn": "_apigee_422_GoogleCloudApigeeV1ListSecurityIncidentsResponseIn",
        "GoogleCloudApigeeV1ListSecurityIncidentsResponseOut": "_apigee_423_GoogleCloudApigeeV1ListSecurityIncidentsResponseOut",
        "GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRevisionIn": "_apigee_424_GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRevisionIn",
        "GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRevisionOut": "_apigee_425_GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRevisionOut",
        "GoogleCloudApigeeV1OperationConfigIn": "_apigee_426_GoogleCloudApigeeV1OperationConfigIn",
        "GoogleCloudApigeeV1OperationConfigOut": "_apigee_427_GoogleCloudApigeeV1OperationConfigOut",
        "EdgeConfigstoreBundleBadBundleViolationIn": "_apigee_428_EdgeConfigstoreBundleBadBundleViolationIn",
        "EdgeConfigstoreBundleBadBundleViolationOut": "_apigee_429_EdgeConfigstoreBundleBadBundleViolationOut",
        "GoogleCloudApigeeV1AdjustDeveloperBalanceRequestIn": "_apigee_430_GoogleCloudApigeeV1AdjustDeveloperBalanceRequestIn",
        "GoogleCloudApigeeV1AdjustDeveloperBalanceRequestOut": "_apigee_431_GoogleCloudApigeeV1AdjustDeveloperBalanceRequestOut",
        "GoogleCloudApigeeV1CanaryEvaluationIn": "_apigee_432_GoogleCloudApigeeV1CanaryEvaluationIn",
        "GoogleCloudApigeeV1CanaryEvaluationOut": "_apigee_433_GoogleCloudApigeeV1CanaryEvaluationOut",
        "GoogleCloudApigeeV1AsyncQueryIn": "_apigee_434_GoogleCloudApigeeV1AsyncQueryIn",
        "GoogleCloudApigeeV1AsyncQueryOut": "_apigee_435_GoogleCloudApigeeV1AsyncQueryOut",
        "GoogleCloudApigeeV1ListApiProductsResponseIn": "_apigee_436_GoogleCloudApigeeV1ListApiProductsResponseIn",
        "GoogleCloudApigeeV1ListApiProductsResponseOut": "_apigee_437_GoogleCloudApigeeV1ListApiProductsResponseOut",
        "GoogleCloudApigeeV1ConnectorsPlatformConfigIn": "_apigee_438_GoogleCloudApigeeV1ConnectorsPlatformConfigIn",
        "GoogleCloudApigeeV1ConnectorsPlatformConfigOut": "_apigee_439_GoogleCloudApigeeV1ConnectorsPlatformConfigOut",
        "GoogleCloudApigeeV1RoutingRuleIn": "_apigee_440_GoogleCloudApigeeV1RoutingRuleIn",
        "GoogleCloudApigeeV1RoutingRuleOut": "_apigee_441_GoogleCloudApigeeV1RoutingRuleOut",
        "GoogleCloudApigeeV1DeveloperSubscriptionIn": "_apigee_442_GoogleCloudApigeeV1DeveloperSubscriptionIn",
        "GoogleCloudApigeeV1DeveloperSubscriptionOut": "_apigee_443_GoogleCloudApigeeV1DeveloperSubscriptionOut",
        "GoogleCloudApigeeV1ComputeEnvironmentScoresRequestIn": "_apigee_444_GoogleCloudApigeeV1ComputeEnvironmentScoresRequestIn",
        "GoogleCloudApigeeV1ComputeEnvironmentScoresRequestOut": "_apigee_445_GoogleCloudApigeeV1ComputeEnvironmentScoresRequestOut",
        "GoogleCloudApigeeV1SecurityProfileScoringConfigIn": "_apigee_446_GoogleCloudApigeeV1SecurityProfileScoringConfigIn",
        "GoogleCloudApigeeV1SecurityProfileScoringConfigOut": "_apigee_447_GoogleCloudApigeeV1SecurityProfileScoringConfigOut",
        "GoogleCloudApigeeV1EntityMetadataIn": "_apigee_448_GoogleCloudApigeeV1EntityMetadataIn",
        "GoogleCloudApigeeV1EntityMetadataOut": "_apigee_449_GoogleCloudApigeeV1EntityMetadataOut",
        "GoogleCloudApigeeV1ScoreComponentRecommendationIn": "_apigee_450_GoogleCloudApigeeV1ScoreComponentRecommendationIn",
        "GoogleCloudApigeeV1ScoreComponentRecommendationOut": "_apigee_451_GoogleCloudApigeeV1ScoreComponentRecommendationOut",
        "GoogleCloudApigeeV1ListOrganizationsResponseIn": "_apigee_452_GoogleCloudApigeeV1ListOrganizationsResponseIn",
        "GoogleCloudApigeeV1ListOrganizationsResponseOut": "_apigee_453_GoogleCloudApigeeV1ListOrganizationsResponseOut",
        "GoogleCloudApigeeV1ProvisionOrganizationRequestIn": "_apigee_454_GoogleCloudApigeeV1ProvisionOrganizationRequestIn",
        "GoogleCloudApigeeV1ProvisionOrganizationRequestOut": "_apigee_455_GoogleCloudApigeeV1ProvisionOrganizationRequestOut",
        "GoogleCloudApigeeV1SchemaSchemaPropertyIn": "_apigee_456_GoogleCloudApigeeV1SchemaSchemaPropertyIn",
        "GoogleCloudApigeeV1SchemaSchemaPropertyOut": "_apigee_457_GoogleCloudApigeeV1SchemaSchemaPropertyOut",
        "GoogleCloudApigeeV1SetAddonsRequestIn": "_apigee_458_GoogleCloudApigeeV1SetAddonsRequestIn",
        "GoogleCloudApigeeV1SetAddonsRequestOut": "_apigee_459_GoogleCloudApigeeV1SetAddonsRequestOut",
        "GoogleCloudApigeeV1TraceConfigIn": "_apigee_460_GoogleCloudApigeeV1TraceConfigIn",
        "GoogleCloudApigeeV1TraceConfigOut": "_apigee_461_GoogleCloudApigeeV1TraceConfigOut",
        "GoogleCloudApigeeV1ExpireDeveloperSubscriptionRequestIn": "_apigee_462_GoogleCloudApigeeV1ExpireDeveloperSubscriptionRequestIn",
        "GoogleCloudApigeeV1ExpireDeveloperSubscriptionRequestOut": "_apigee_463_GoogleCloudApigeeV1ExpireDeveloperSubscriptionRequestOut",
        "GoogleCloudApigeeV1PodStatusIn": "_apigee_464_GoogleCloudApigeeV1PodStatusIn",
        "GoogleCloudApigeeV1PodStatusOut": "_apigee_465_GoogleCloudApigeeV1PodStatusOut",
        "GoogleCloudApigeeV1AttributesIn": "_apigee_466_GoogleCloudApigeeV1AttributesIn",
        "GoogleCloudApigeeV1AttributesOut": "_apigee_467_GoogleCloudApigeeV1AttributesOut",
        "GoogleCloudApigeeV1ApiSecurityRuntimeConfigIn": "_apigee_468_GoogleCloudApigeeV1ApiSecurityRuntimeConfigIn",
        "GoogleCloudApigeeV1ApiSecurityRuntimeConfigOut": "_apigee_469_GoogleCloudApigeeV1ApiSecurityRuntimeConfigOut",
        "GoogleRpcPreconditionFailureIn": "_apigee_470_GoogleRpcPreconditionFailureIn",
        "GoogleRpcPreconditionFailureOut": "_apigee_471_GoogleRpcPreconditionFailureOut",
        "GoogleCloudApigeeV1OrganizationIn": "_apigee_472_GoogleCloudApigeeV1OrganizationIn",
        "GoogleCloudApigeeV1OrganizationOut": "_apigee_473_GoogleCloudApigeeV1OrganizationOut",
        "GoogleCloudApigeeV1DeveloperAppKeyIn": "_apigee_474_GoogleCloudApigeeV1DeveloperAppKeyIn",
        "GoogleCloudApigeeV1DeveloperAppKeyOut": "_apigee_475_GoogleCloudApigeeV1DeveloperAppKeyOut",
        "GoogleCloudApigeeV1ReferenceIn": "_apigee_476_GoogleCloudApigeeV1ReferenceIn",
        "GoogleCloudApigeeV1ReferenceOut": "_apigee_477_GoogleCloudApigeeV1ReferenceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudApigeeV1AccessIn"] = t.struct(
        {
            "Set": t.proxy(renames["GoogleCloudApigeeV1AccessSetIn"]),
            "Get": t.proxy(renames["GoogleCloudApigeeV1AccessGetIn"]),
            "Remove": t.proxy(renames["GoogleCloudApigeeV1AccessRemoveIn"]),
        }
    ).named(renames["GoogleCloudApigeeV1AccessIn"])
    types["GoogleCloudApigeeV1AccessOut"] = t.struct(
        {
            "Set": t.proxy(renames["GoogleCloudApigeeV1AccessSetOut"]),
            "Get": t.proxy(renames["GoogleCloudApigeeV1AccessGetOut"]),
            "Remove": t.proxy(renames["GoogleCloudApigeeV1AccessRemoveOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AccessOut"])
    types["GoogleCloudApigeeV1KeyValueEntryIn"] = t.struct(
        {"value": t.string(), "name": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1KeyValueEntryIn"])
    types["GoogleCloudApigeeV1KeyValueEntryOut"] = t.struct(
        {
            "value": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1KeyValueEntryOut"])
    types["GoogleCloudApigeeV1QueryTimeSeriesStatsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "values": t.array(
                t.proxy(
                    renames["GoogleCloudApigeeV1QueryTimeSeriesStatsResponseSequenceIn"]
                )
            ).optional(),
            "columns": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryTimeSeriesStatsResponseIn"])
    types["GoogleCloudApigeeV1QueryTimeSeriesStatsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "values": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudApigeeV1QueryTimeSeriesStatsResponseSequenceOut"
                    ]
                )
            ).optional(),
            "columns": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryTimeSeriesStatsResponseOut"])
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
    types["GoogleCloudApigeeV1AccessSetIn"] = t.struct(
        {"name": t.string(), "value": t.string(), "success": t.boolean()}
    ).named(renames["GoogleCloudApigeeV1AccessSetIn"])
    types["GoogleCloudApigeeV1AccessSetOut"] = t.struct(
        {
            "name": t.string(),
            "value": t.string(),
            "success": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AccessSetOut"])
    types["GoogleCloudApigeeV1DateRangeIn"] = t.struct(
        {"end": t.string(), "start": t.string()}
    ).named(renames["GoogleCloudApigeeV1DateRangeIn"])
    types["GoogleCloudApigeeV1DateRangeOut"] = t.struct(
        {
            "end": t.string(),
            "start": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DateRangeOut"])
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
    types["GoogleIamV1TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsRequestIn"])
    types["GoogleIamV1TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsRequestOut"])
    types["GoogleCloudApigeeV1MonetizationConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["GoogleCloudApigeeV1MonetizationConfigIn"])
    types["GoogleCloudApigeeV1MonetizationConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1MonetizationConfigOut"])
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
    types["GoogleCloudApigeeV1ReferenceConfigIn"] = t.struct(
        {"name": t.string().optional(), "resourceName": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1ReferenceConfigIn"])
    types["GoogleCloudApigeeV1ReferenceConfigOut"] = t.struct(
        {
            "name": t.string().optional(),
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ReferenceConfigOut"])
    types["GoogleCloudApigeeV1DeploymentIn"] = t.struct(
        {
            "deployStartTime": t.string().optional(),
            "environment": t.string().optional(),
            "instances": t.array(
                t.proxy(renames["GoogleCloudApigeeV1InstanceDeploymentStatusIn"])
            ).optional(),
            "errors": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "state": t.string().optional(),
            "apiProxy": t.string().optional(),
            "routeConflicts": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudApigeeV1DeploymentChangeReportRoutingConflictIn"
                    ]
                )
            ).optional(),
            "serviceAccount": t.string().optional(),
            "revision": t.string().optional(),
            "pods": t.array(
                t.proxy(renames["GoogleCloudApigeeV1PodStatusIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentIn"])
    types["GoogleCloudApigeeV1DeploymentOut"] = t.struct(
        {
            "deployStartTime": t.string().optional(),
            "environment": t.string().optional(),
            "instances": t.array(
                t.proxy(renames["GoogleCloudApigeeV1InstanceDeploymentStatusOut"])
            ).optional(),
            "errors": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "state": t.string().optional(),
            "apiProxy": t.string().optional(),
            "routeConflicts": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudApigeeV1DeploymentChangeReportRoutingConflictOut"
                    ]
                )
            ).optional(),
            "serviceAccount": t.string().optional(),
            "revision": t.string().optional(),
            "pods": t.array(
                t.proxy(renames["GoogleCloudApigeeV1PodStatusOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentOut"])
    types["GoogleCloudApigeeV1DeploymentConfigIn"] = t.struct(
        {
            "basePath": t.string().optional(),
            "uid": t.string().optional(),
            "deploymentGroups": t.array(t.string()).optional(),
            "serviceAccount": t.string().optional(),
            "endpoints": t.struct({"_": t.string().optional()}).optional(),
            "location": t.string().optional(),
            "proxyUid": t.string().optional(),
            "name": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentConfigIn"])
    types["GoogleCloudApigeeV1DeploymentConfigOut"] = t.struct(
        {
            "basePath": t.string().optional(),
            "uid": t.string().optional(),
            "deploymentGroups": t.array(t.string()).optional(),
            "serviceAccount": t.string().optional(),
            "endpoints": t.struct({"_": t.string().optional()}).optional(),
            "location": t.string().optional(),
            "proxyUid": t.string().optional(),
            "name": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentConfigOut"])
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
    types["GoogleCloudApigeeV1ApiCategoryIn"] = t.struct(
        {
            "data": t.proxy(renames["GoogleCloudApigeeV1ApiCategoryDataIn"]).optional(),
            "status": t.string().optional(),
            "errorCode": t.string().optional(),
            "requestId": t.string().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ApiCategoryIn"])
    types["GoogleCloudApigeeV1ApiCategoryOut"] = t.struct(
        {
            "data": t.proxy(
                renames["GoogleCloudApigeeV1ApiCategoryDataOut"]
            ).optional(),
            "status": t.string().optional(),
            "errorCode": t.string().optional(),
            "requestId": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ApiCategoryOut"])
    types["GoogleCloudApigeeV1GenerateUploadUrlResponseIn"] = t.struct(
        {"uploadUri": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1GenerateUploadUrlResponseIn"])
    types["GoogleCloudApigeeV1GenerateUploadUrlResponseOut"] = t.struct(
        {
            "uploadUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1GenerateUploadUrlResponseOut"])
    types["GoogleCloudApigeeV1TargetServerConfigIn"] = t.struct(
        {
            "tlsInfo": t.proxy(
                renames["GoogleCloudApigeeV1TlsInfoConfigIn"]
            ).optional(),
            "enabled": t.boolean().optional(),
            "name": t.string().optional(),
            "protocol": t.string().optional(),
            "host": t.string().optional(),
            "port": t.integer().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1TargetServerConfigIn"])
    types["GoogleCloudApigeeV1TargetServerConfigOut"] = t.struct(
        {
            "tlsInfo": t.proxy(
                renames["GoogleCloudApigeeV1TlsInfoConfigOut"]
            ).optional(),
            "enabled": t.boolean().optional(),
            "name": t.string().optional(),
            "protocol": t.string().optional(),
            "host": t.string().optional(),
            "port": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1TargetServerConfigOut"])
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
    types["GoogleCloudApigeeV1OperationMetadataIn"] = t.struct(
        {
            "state": t.string(),
            "warnings": t.array(t.string()).optional(),
            "targetResourceName": t.string().optional(),
            "progress": t.proxy(
                renames["GoogleCloudApigeeV1OperationMetadataProgressIn"]
            ).optional(),
            "operationType": t.string(),
        }
    ).named(renames["GoogleCloudApigeeV1OperationMetadataIn"])
    types["GoogleCloudApigeeV1OperationMetadataOut"] = t.struct(
        {
            "state": t.string(),
            "warnings": t.array(t.string()).optional(),
            "targetResourceName": t.string().optional(),
            "progress": t.proxy(
                renames["GoogleCloudApigeeV1OperationMetadataProgressOut"]
            ).optional(),
            "operationType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OperationMetadataOut"])
    types["GoogleCloudApigeeV1DatastoreIn"] = t.struct(
        {
            "datastoreConfig": t.proxy(
                renames["GoogleCloudApigeeV1DatastoreConfigIn"]
            ).optional(),
            "targetType": t.string().optional(),
            "displayName": t.string(),
        }
    ).named(renames["GoogleCloudApigeeV1DatastoreIn"])
    types["GoogleCloudApigeeV1DatastoreOut"] = t.struct(
        {
            "datastoreConfig": t.proxy(
                renames["GoogleCloudApigeeV1DatastoreConfigOut"]
            ).optional(),
            "lastUpdateTime": t.string().optional(),
            "targetType": t.string().optional(),
            "createTime": t.string().optional(),
            "self": t.string().optional(),
            "displayName": t.string(),
            "org": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DatastoreOut"])
    types["GoogleCloudApigeeV1ApiProxyIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudApigeeV1ApiProxyIn"])
    types["GoogleCloudApigeeV1ApiProxyOut"] = t.struct(
        {
            "readOnly": t.boolean().optional(),
            "name": t.string().optional(),
            "latestRevisionId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "apiProxyType": t.string().optional(),
            "metaData": t.proxy(
                renames["GoogleCloudApigeeV1EntityMetadataOut"]
            ).optional(),
            "revision": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ApiProxyOut"])
    types["GoogleCloudApigeeV1OptimizedStatsNodeIn"] = t.struct(
        {"data": t.array(t.struct({"_": t.string().optional()}))}
    ).named(renames["GoogleCloudApigeeV1OptimizedStatsNodeIn"])
    types["GoogleCloudApigeeV1OptimizedStatsNodeOut"] = t.struct(
        {
            "data": t.array(t.struct({"_": t.string().optional()})),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OptimizedStatsNodeOut"])
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
    types["GoogleCloudApigeeV1CertInfoIn"] = t.struct(
        {
            "subject": t.string().optional(),
            "isValid": t.string().optional(),
            "issuer": t.string().optional(),
            "basicConstraints": t.string().optional(),
            "publicKey": t.string().optional(),
            "validFrom": t.string().optional(),
            "serialNumber": t.string().optional(),
            "expiryDate": t.string().optional(),
            "subjectAlternativeNames": t.array(t.string()).optional(),
            "version": t.integer().optional(),
            "sigAlgName": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1CertInfoIn"])
    types["GoogleCloudApigeeV1CertInfoOut"] = t.struct(
        {
            "subject": t.string().optional(),
            "isValid": t.string().optional(),
            "issuer": t.string().optional(),
            "basicConstraints": t.string().optional(),
            "publicKey": t.string().optional(),
            "validFrom": t.string().optional(),
            "serialNumber": t.string().optional(),
            "expiryDate": t.string().optional(),
            "subjectAlternativeNames": t.array(t.string()).optional(),
            "version": t.integer().optional(),
            "sigAlgName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1CertInfoOut"])
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
    types["GoogleRpcPreconditionFailureViolationIn"] = t.struct(
        {
            "description": t.string().optional(),
            "subject": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleRpcPreconditionFailureViolationIn"])
    types["GoogleRpcPreconditionFailureViolationOut"] = t.struct(
        {
            "description": t.string().optional(),
            "subject": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcPreconditionFailureViolationOut"])
    types["GoogleCloudApigeeV1ListDebugSessionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "sessions": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SessionIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListDebugSessionsResponseIn"])
    types["GoogleCloudApigeeV1ListDebugSessionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "sessions": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SessionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListDebugSessionsResponseOut"])
    types["GoogleCloudApigeeV1ListApiProxiesResponseIn"] = t.struct(
        {"proxies": t.array(t.proxy(renames["GoogleCloudApigeeV1ApiProxyIn"]))}
    ).named(renames["GoogleCloudApigeeV1ListApiProxiesResponseIn"])
    types["GoogleCloudApigeeV1ListApiProxiesResponseOut"] = t.struct(
        {
            "proxies": t.array(t.proxy(renames["GoogleCloudApigeeV1ApiProxyOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListApiProxiesResponseOut"])
    types["GoogleCloudApigeeV1MetadataIn"] = t.struct(
        {
            "errors": t.array(t.string()).optional(),
            "notices": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1MetadataIn"])
    types["GoogleCloudApigeeV1MetadataOut"] = t.struct(
        {
            "errors": t.array(t.string()).optional(),
            "notices": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1MetadataOut"])
    types["GoogleCloudApigeeV1FlowHookIn"] = t.struct(
        {
            "description": t.string().optional(),
            "continueOnError": t.boolean().optional(),
            "sharedFlow": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1FlowHookIn"])
    types["GoogleCloudApigeeV1FlowHookOut"] = t.struct(
        {
            "description": t.string().optional(),
            "continueOnError": t.boolean().optional(),
            "sharedFlow": t.string().optional(),
            "flowHookPoint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1FlowHookOut"])
    types["GoogleCloudApigeeV1ScoreComponentIn"] = t.struct(
        {
            "score": t.integer().optional(),
            "calculateTime": t.string().optional(),
            "scorePath": t.string().optional(),
            "recommendations": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ScoreComponentRecommendationIn"])
            ).optional(),
            "dataCaptureTime": t.string().optional(),
            "drilldownPaths": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ScoreComponentIn"])
    types["GoogleCloudApigeeV1ScoreComponentOut"] = t.struct(
        {
            "score": t.integer().optional(),
            "calculateTime": t.string().optional(),
            "scorePath": t.string().optional(),
            "recommendations": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ScoreComponentRecommendationOut"])
            ).optional(),
            "dataCaptureTime": t.string().optional(),
            "drilldownPaths": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ScoreComponentOut"])
    types["GoogleCloudApigeeV1DeploymentGroupConfigIn"] = t.struct(
        {
            "name": t.string().optional(),
            "revisionId": t.string().optional(),
            "deploymentGroupType": t.string().optional(),
            "uid": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentGroupConfigIn"])
    types["GoogleCloudApigeeV1DeploymentGroupConfigOut"] = t.struct(
        {
            "name": t.string().optional(),
            "revisionId": t.string().optional(),
            "deploymentGroupType": t.string().optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentGroupConfigOut"])
    types["GoogleCloudApigeeV1DeploymentChangeReportRoutingConflictIn"] = t.struct(
        {
            "description": t.string().optional(),
            "environmentGroup": t.string().optional(),
            "conflictingDeployment": t.proxy(
                renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingConflictIn"])
    types["GoogleCloudApigeeV1DeploymentChangeReportRoutingConflictOut"] = t.struct(
        {
            "description": t.string().optional(),
            "environmentGroup": t.string().optional(),
            "conflictingDeployment": t.proxy(
                renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingConflictOut"])
    types["GoogleCloudApigeeV1QueryTimeSeriesStatsRequestIn"] = t.struct(
        {
            "timeRange": t.proxy(renames["GoogleTypeIntervalIn"]),
            "timestampOrder": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "pageToken": t.string().optional(),
            "filter": t.string().optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1MetricAggregationIn"])
            ),
            "pageSize": t.integer().optional(),
            "windowSize": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryTimeSeriesStatsRequestIn"])
    types["GoogleCloudApigeeV1QueryTimeSeriesStatsRequestOut"] = t.struct(
        {
            "timeRange": t.proxy(renames["GoogleTypeIntervalOut"]),
            "timestampOrder": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "pageToken": t.string().optional(),
            "filter": t.string().optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1MetricAggregationOut"])
            ),
            "pageSize": t.integer().optional(),
            "windowSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryTimeSeriesStatsRequestOut"])
    types["GoogleCloudApigeeV1EndpointAttachmentIn"] = t.struct(
        {
            "name": t.string().optional(),
            "location": t.string(),
            "serviceAttachment": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1EndpointAttachmentIn"])
    types["GoogleCloudApigeeV1EndpointAttachmentOut"] = t.struct(
        {
            "state": t.string().optional(),
            "connectionState": t.string().optional(),
            "name": t.string().optional(),
            "location": t.string(),
            "host": t.string().optional(),
            "serviceAttachment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1EndpointAttachmentOut"])
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
    types["GoogleCloudApigeeV1ListAppsResponseIn"] = t.struct(
        {"app": t.array(t.proxy(renames["GoogleCloudApigeeV1AppIn"]))}
    ).named(renames["GoogleCloudApigeeV1ListAppsResponseIn"])
    types["GoogleCloudApigeeV1ListAppsResponseOut"] = t.struct(
        {
            "app": t.array(t.proxy(renames["GoogleCloudApigeeV1AppOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListAppsResponseOut"])
    types["GoogleCloudApigeeV1ApiProductIn"] = t.struct(
        {
            "description": t.string().optional(),
            "apiResources": t.array(t.string()).optional(),
            "scopes": t.array(t.string()).optional(),
            "lastModifiedAt": t.string().optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
            ).optional(),
            "approvalType": t.string().optional(),
            "quotaCounterScope": t.string().optional(),
            "operationGroup": t.proxy(
                renames["GoogleCloudApigeeV1OperationGroupIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "graphqlOperationGroup": t.proxy(
                renames["GoogleCloudApigeeV1GraphQLOperationGroupIn"]
            ).optional(),
            "name": t.string().optional(),
            "proxies": t.array(t.string()).optional(),
            "createdAt": t.string().optional(),
            "quotaInterval": t.string().optional(),
            "environments": t.array(t.string()).optional(),
            "quotaTimeUnit": t.string().optional(),
            "quota": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ApiProductIn"])
    types["GoogleCloudApigeeV1ApiProductOut"] = t.struct(
        {
            "description": t.string().optional(),
            "apiResources": t.array(t.string()).optional(),
            "scopes": t.array(t.string()).optional(),
            "lastModifiedAt": t.string().optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeOut"])
            ).optional(),
            "approvalType": t.string().optional(),
            "quotaCounterScope": t.string().optional(),
            "operationGroup": t.proxy(
                renames["GoogleCloudApigeeV1OperationGroupOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "graphqlOperationGroup": t.proxy(
                renames["GoogleCloudApigeeV1GraphQLOperationGroupOut"]
            ).optional(),
            "name": t.string().optional(),
            "proxies": t.array(t.string()).optional(),
            "createdAt": t.string().optional(),
            "quotaInterval": t.string().optional(),
            "environments": t.array(t.string()).optional(),
            "quotaTimeUnit": t.string().optional(),
            "quota": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ApiProductOut"])
    types["GoogleCloudApigeeV1SecurityReportQueryMetricIn"] = t.struct(
        {
            "operator": t.string().optional(),
            "name": t.string(),
            "value": t.string().optional(),
            "aggregationFunction": t.string().optional(),
            "alias": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityReportQueryMetricIn"])
    types["GoogleCloudApigeeV1SecurityReportQueryMetricOut"] = t.struct(
        {
            "operator": t.string().optional(),
            "name": t.string(),
            "value": t.string().optional(),
            "aggregationFunction": t.string().optional(),
            "alias": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityReportQueryMetricOut"])
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
    types["GoogleCloudApigeeV1AppIn"] = t.struct(
        {
            "callbackUrl": t.string().optional(),
            "name": t.string().optional(),
            "companyName": t.string().optional(),
            "status": t.string().optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
            ).optional(),
            "keyExpiresIn": t.string().optional(),
            "appId": t.string().optional(),
            "developerId": t.string().optional(),
            "apiProducts": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ApiProductRefIn"])
            ).optional(),
            "scopes": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AppIn"])
    types["GoogleCloudApigeeV1AppOut"] = t.struct(
        {
            "callbackUrl": t.string().optional(),
            "name": t.string().optional(),
            "companyName": t.string().optional(),
            "status": t.string().optional(),
            "lastModifiedAt": t.string().optional(),
            "createdAt": t.string().optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeOut"])
            ).optional(),
            "keyExpiresIn": t.string().optional(),
            "appId": t.string().optional(),
            "developerId": t.string().optional(),
            "apiProducts": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ApiProductRefOut"])
            ).optional(),
            "scopes": t.array(t.string()).optional(),
            "credentials": t.array(
                t.proxy(renames["GoogleCloudApigeeV1CredentialOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AppOut"])
    types["GoogleTypeMoneyIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "currencyCode": t.string().optional(),
            "units": t.string().optional(),
        }
    ).named(renames["GoogleTypeMoneyIn"])
    types["GoogleTypeMoneyOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "currencyCode": t.string().optional(),
            "units": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeMoneyOut"])
    types["GoogleCloudApigeeV1SecurityReportQueryIn"] = t.struct(
        {
            "reportDefinitionId": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "filter": t.string().optional(),
            "limit": t.integer().optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SecurityReportQueryMetricIn"])
            ).optional(),
            "timeRange": t.struct({"_": t.string().optional()}),
            "mimeType": t.string().optional(),
            "groupByTimeUnit": t.string().optional(),
            "csvDelimiter": t.string().optional(),
            "envgroupHostname": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityReportQueryIn"])
    types["GoogleCloudApigeeV1SecurityReportQueryOut"] = t.struct(
        {
            "reportDefinitionId": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "filter": t.string().optional(),
            "limit": t.integer().optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SecurityReportQueryMetricOut"])
            ).optional(),
            "timeRange": t.struct({"_": t.string().optional()}),
            "mimeType": t.string().optional(),
            "groupByTimeUnit": t.string().optional(),
            "csvDelimiter": t.string().optional(),
            "envgroupHostname": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityReportQueryOut"])
    types["GoogleCloudApigeeV1AdvancedApiOpsConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["GoogleCloudApigeeV1AdvancedApiOpsConfigIn"])
    types["GoogleCloudApigeeV1AdvancedApiOpsConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AdvancedApiOpsConfigOut"])
    types["GoogleCloudApigeeV1CustomReportIn"] = t.struct(
        {
            "dimensions": t.array(t.string()).optional(),
            "sortByCols": t.array(t.string()).optional(),
            "sortOrder": t.string().optional(),
            "chartType": t.string().optional(),
            "toTime": t.string().optional(),
            "timeUnit": t.string().optional(),
            "filter": t.string().optional(),
            "fromTime": t.string().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ReportPropertyIn"])
            ).optional(),
            "offset": t.string().optional(),
            "displayName": t.string().optional(),
            "limit": t.string().optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1CustomReportMetricIn"])
            ),
            "name": t.string(),
            "tags": t.array(t.string()).optional(),
            "topk": t.string().optional(),
            "comments": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1CustomReportIn"])
    types["GoogleCloudApigeeV1CustomReportOut"] = t.struct(
        {
            "organization": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "sortByCols": t.array(t.string()).optional(),
            "environment": t.string().optional(),
            "sortOrder": t.string().optional(),
            "lastModifiedAt": t.string().optional(),
            "chartType": t.string().optional(),
            "toTime": t.string().optional(),
            "timeUnit": t.string().optional(),
            "filter": t.string().optional(),
            "fromTime": t.string().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ReportPropertyOut"])
            ).optional(),
            "offset": t.string().optional(),
            "displayName": t.string().optional(),
            "lastViewedAt": t.string().optional(),
            "limit": t.string().optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1CustomReportMetricOut"])
            ),
            "name": t.string(),
            "tags": t.array(t.string()).optional(),
            "createdAt": t.string().optional(),
            "topk": t.string().optional(),
            "comments": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1CustomReportOut"])
    types["GoogleCloudApigeeV1DatastoreConfigIn"] = t.struct(
        {
            "path": t.string().optional(),
            "datasetName": t.string().optional(),
            "bucketName": t.string().optional(),
            "tablePrefix": t.string().optional(),
            "projectId": t.string(),
        }
    ).named(renames["GoogleCloudApigeeV1DatastoreConfigIn"])
    types["GoogleCloudApigeeV1DatastoreConfigOut"] = t.struct(
        {
            "path": t.string().optional(),
            "datasetName": t.string().optional(),
            "bucketName": t.string().optional(),
            "tablePrefix": t.string().optional(),
            "projectId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DatastoreConfigOut"])
    types["GoogleCloudApigeeV1ListDataCollectorsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "dataCollectors": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DataCollectorIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListDataCollectorsResponseIn"])
    types["GoogleCloudApigeeV1ListDataCollectorsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "dataCollectors": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DataCollectorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListDataCollectorsResponseOut"])
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
    types["GoogleCloudApigeeV1CommonNameConfigIn"] = t.struct(
        {"name": t.string(), "matchWildCards": t.boolean()}
    ).named(renames["GoogleCloudApigeeV1CommonNameConfigIn"])
    types["GoogleCloudApigeeV1CommonNameConfigOut"] = t.struct(
        {
            "name": t.string(),
            "matchWildCards": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1CommonNameConfigOut"])
    types["GoogleCloudApigeeV1SecurityReportResultViewIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "error": t.string().optional(),
            "rows": t.array(t.struct({"_": t.string().optional()})).optional(),
            "metadata": t.proxy(
                renames["GoogleCloudApigeeV1SecurityReportMetadataIn"]
            ).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityReportResultViewIn"])
    types["GoogleCloudApigeeV1SecurityReportResultViewOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "rows": t.array(t.struct({"_": t.string().optional()})).optional(),
            "metadata": t.proxy(
                renames["GoogleCloudApigeeV1SecurityReportMetadataOut"]
            ).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityReportResultViewOut"])
    types["GoogleCloudApigeeV1InstanceIn"] = t.struct(
        {
            "name": t.string(),
            "peeringCidrRange": t.string().optional(),
            "consumerAcceptList": t.array(t.string()).optional(),
            "location": t.string(),
            "displayName": t.string().optional(),
            "diskEncryptionKeyName": t.string().optional(),
            "ipRange": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1InstanceIn"])
    types["GoogleCloudApigeeV1InstanceOut"] = t.struct(
        {
            "name": t.string(),
            "peeringCidrRange": t.string().optional(),
            "consumerAcceptList": t.array(t.string()).optional(),
            "serviceAttachment": t.string().optional(),
            "location": t.string(),
            "state": t.string().optional(),
            "lastModifiedAt": t.string().optional(),
            "displayName": t.string().optional(),
            "diskEncryptionKeyName": t.string().optional(),
            "port": t.string().optional(),
            "ipRange": t.string().optional(),
            "runtimeVersion": t.string().optional(),
            "description": t.string().optional(),
            "createdAt": t.string().optional(),
            "host": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1InstanceOut"])
    types["GoogleCloudApigeeV1StatsEnvironmentStatsIn"] = t.struct(
        {
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1MetricIn"])
            ).optional(),
            "dimensions": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DimensionMetricIn"])
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1StatsEnvironmentStatsIn"])
    types["GoogleCloudApigeeV1StatsEnvironmentStatsOut"] = t.struct(
        {
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1MetricOut"])
            ).optional(),
            "dimensions": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DimensionMetricOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1StatsEnvironmentStatsOut"])
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
    types["GoogleCloudApigeeV1EnvironmentGroupConfigIn"] = t.struct(
        {
            "name": t.string().optional(),
            "endpointChainingRules": t.array(
                t.proxy(renames["GoogleCloudApigeeV1EndpointChainingRuleIn"])
            ).optional(),
            "routingRules": t.array(
                t.proxy(renames["GoogleCloudApigeeV1RoutingRuleIn"])
            ).optional(),
            "hostnames": t.array(t.string()).optional(),
            "uid": t.string().optional(),
            "revisionId": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1EnvironmentGroupConfigIn"])
    types["GoogleCloudApigeeV1EnvironmentGroupConfigOut"] = t.struct(
        {
            "name": t.string().optional(),
            "endpointChainingRules": t.array(
                t.proxy(renames["GoogleCloudApigeeV1EndpointChainingRuleOut"])
            ).optional(),
            "routingRules": t.array(
                t.proxy(renames["GoogleCloudApigeeV1RoutingRuleOut"])
            ).optional(),
            "hostnames": t.array(t.string()).optional(),
            "uid": t.string().optional(),
            "revisionId": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1EnvironmentGroupConfigOut"])
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
    types["GoogleCloudApigeeV1AsyncQueryResultViewIn"] = t.struct(
        {
            "rows": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "state": t.string().optional(),
            "error": t.string().optional(),
            "metadata": t.proxy(
                renames["GoogleCloudApigeeV1QueryMetadataIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AsyncQueryResultViewIn"])
    types["GoogleCloudApigeeV1AsyncQueryResultViewOut"] = t.struct(
        {
            "rows": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.proxy(
                renames["GoogleCloudApigeeV1QueryMetadataOut"]
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AsyncQueryResultViewOut"])
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
    types["GoogleCloudApigeeV1QueryTimeSeriesStatsResponseSequenceIn"] = t.struct(
        {
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "points": t.array(
                t.array(t.struct({"_": t.string().optional()}))
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryTimeSeriesStatsResponseSequenceIn"])
    types["GoogleCloudApigeeV1QueryTimeSeriesStatsResponseSequenceOut"] = t.struct(
        {
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "points": t.array(
                t.array(t.struct({"_": t.string().optional()}))
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryTimeSeriesStatsResponseSequenceOut"])
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
    types["GoogleCloudApigeeV1AliasRevisionConfigIn"] = t.struct(
        {
            "type": t.string(),
            "name": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AliasRevisionConfigIn"])
    types["GoogleCloudApigeeV1AliasRevisionConfigOut"] = t.struct(
        {
            "type": t.string(),
            "name": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AliasRevisionConfigOut"])
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
    types["GoogleCloudApigeeV1AttributeIn"] = t.struct(
        {"value": t.string().optional(), "name": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1AttributeIn"])
    types["GoogleCloudApigeeV1AttributeOut"] = t.struct(
        {
            "value": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AttributeOut"])
    types["GoogleCloudApigeeV1DataCollectorConfigIn"] = t.struct(
        {"type": t.string().optional(), "name": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1DataCollectorConfigIn"])
    types["GoogleCloudApigeeV1DataCollectorConfigOut"] = t.struct(
        {
            "type": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DataCollectorConfigOut"])
    types["GoogleCloudApigeeV1NodeConfigIn"] = t.struct(
        {"maxNodeCount": t.string().optional(), "minNodeCount": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1NodeConfigIn"])
    types["GoogleCloudApigeeV1NodeConfigOut"] = t.struct(
        {
            "maxNodeCount": t.string().optional(),
            "minNodeCount": t.string().optional(),
            "currentAggregateNodeCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1NodeConfigOut"])
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
    types["GoogleCloudApigeeV1ComputeEnvironmentScoresResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "scores": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ScoreIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ComputeEnvironmentScoresResponseIn"])
    types["GoogleCloudApigeeV1ComputeEnvironmentScoresResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "scores": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ScoreOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ComputeEnvironmentScoresResponseOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudApigeeV1ListDeveloperSubscriptionsResponseIn"] = t.struct(
        {
            "developerSubscriptions": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DeveloperSubscriptionIn"])
            ).optional(),
            "nextStartKey": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListDeveloperSubscriptionsResponseIn"])
    types["GoogleCloudApigeeV1ListDeveloperSubscriptionsResponseOut"] = t.struct(
        {
            "developerSubscriptions": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DeveloperSubscriptionOut"])
            ).optional(),
            "nextStartKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListDeveloperSubscriptionsResponseOut"])
    types["GoogleCloudApigeeV1ReportPropertyIn"] = t.struct(
        {
            "value": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
            ).optional(),
            "property": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ReportPropertyIn"])
    types["GoogleCloudApigeeV1ReportPropertyOut"] = t.struct(
        {
            "value": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeOut"])
            ).optional(),
            "property": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ReportPropertyOut"])
    types["GoogleCloudApigeeV1RuntimeTraceConfigIn"] = t.struct(
        {
            "samplingConfig": t.proxy(
                renames["GoogleCloudApigeeV1RuntimeTraceSamplingConfigIn"]
            ).optional(),
            "revisionId": t.string().optional(),
            "overrides": t.array(
                t.proxy(renames["GoogleCloudApigeeV1RuntimeTraceConfigOverrideIn"])
            ).optional(),
            "revisionCreateTime": t.string().optional(),
            "name": t.string().optional(),
            "exporter": t.string().optional(),
            "endpoint": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RuntimeTraceConfigIn"])
    types["GoogleCloudApigeeV1RuntimeTraceConfigOut"] = t.struct(
        {
            "samplingConfig": t.proxy(
                renames["GoogleCloudApigeeV1RuntimeTraceSamplingConfigOut"]
            ).optional(),
            "revisionId": t.string().optional(),
            "overrides": t.array(
                t.proxy(renames["GoogleCloudApigeeV1RuntimeTraceConfigOverrideOut"])
            ).optional(),
            "revisionCreateTime": t.string().optional(),
            "name": t.string().optional(),
            "exporter": t.string().optional(),
            "endpoint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RuntimeTraceConfigOut"])
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
    types["GoogleCloudApigeeV1EnvironmentGroupIn"] = t.struct(
        {"hostnames": t.array(t.string()), "name": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1EnvironmentGroupIn"])
    types["GoogleCloudApigeeV1EnvironmentGroupOut"] = t.struct(
        {
            "lastModifiedAt": t.string().optional(),
            "hostnames": t.array(t.string()),
            "state": t.string().optional(),
            "createdAt": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1EnvironmentGroupOut"])
    types["GoogleCloudApigeeV1DataCollectorIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DataCollectorIn"])
    types["GoogleCloudApigeeV1DataCollectorOut"] = t.struct(
        {
            "description": t.string().optional(),
            "createdAt": t.string().optional(),
            "name": t.string().optional(),
            "lastModifiedAt": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DataCollectorOut"])
    types["GoogleCloudApigeeV1QueryTabularStatsRequestIn"] = t.struct(
        {
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1MetricAggregationIn"])
            ),
            "pageSize": t.integer().optional(),
            "filter": t.string().optional(),
            "dimensions": t.array(t.string()),
            "pageToken": t.string().optional(),
            "timeRange": t.proxy(renames["GoogleTypeIntervalIn"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryTabularStatsRequestIn"])
    types["GoogleCloudApigeeV1QueryTabularStatsRequestOut"] = t.struct(
        {
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1MetricAggregationOut"])
            ),
            "pageSize": t.integer().optional(),
            "filter": t.string().optional(),
            "dimensions": t.array(t.string()),
            "pageToken": t.string().optional(),
            "timeRange": t.proxy(renames["GoogleTypeIntervalOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryTabularStatsRequestOut"])
    types["GoogleCloudApigeeV1InstanceAttachmentIn"] = t.struct(
        {"environment": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1InstanceAttachmentIn"])
    types["GoogleCloudApigeeV1InstanceAttachmentOut"] = t.struct(
        {
            "createdAt": t.string().optional(),
            "environment": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1InstanceAttachmentOut"])
    types["GoogleCloudApigeeV1MetricIn"] = t.struct(
        {
            "values": t.array(t.struct({"_": t.string().optional()})).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1MetricIn"])
    types["GoogleCloudApigeeV1MetricOut"] = t.struct(
        {
            "values": t.array(t.struct({"_": t.string().optional()})).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1MetricOut"])
    types["GoogleCloudApigeeV1CanaryEvaluationMetricLabelsIn"] = t.struct(
        {
            "env": t.string().optional(),
            "location": t.string(),
            "instance_id": t.string(),
        }
    ).named(renames["GoogleCloudApigeeV1CanaryEvaluationMetricLabelsIn"])
    types["GoogleCloudApigeeV1CanaryEvaluationMetricLabelsOut"] = t.struct(
        {
            "env": t.string().optional(),
            "location": t.string(),
            "instance_id": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1CanaryEvaluationMetricLabelsOut"])
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
    types["GoogleCloudApigeeV1ServiceIssuersMappingIn"] = t.struct(
        {"service": t.string().optional(), "emailIds": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudApigeeV1ServiceIssuersMappingIn"])
    types["GoogleCloudApigeeV1ServiceIssuersMappingOut"] = t.struct(
        {
            "service": t.string().optional(),
            "emailIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ServiceIssuersMappingOut"])
    types["GoogleCloudApigeeV1OperationMetadataProgressIn"] = t.struct(
        {
            "state": t.string().optional(),
            "percentDone": t.integer().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OperationMetadataProgressIn"])
    types["GoogleCloudApigeeV1OperationMetadataProgressOut"] = t.struct(
        {
            "state": t.string().optional(),
            "percentDone": t.integer().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OperationMetadataProgressOut"])
    types["GoogleCloudApigeeV1TestDatastoreResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1TestDatastoreResponseIn"])
    types["GoogleCloudApigeeV1TestDatastoreResponseOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1TestDatastoreResponseOut"])
    types["GoogleCloudApigeeV1ApiCategoryDataIn"] = t.struct(
        {
            "id": t.string().optional(),
            "updateTime": t.string().optional(),
            "gcpResource": t.string().optional(),
            "siteId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ApiCategoryDataIn"])
    types["GoogleCloudApigeeV1ApiCategoryDataOut"] = t.struct(
        {
            "id": t.string().optional(),
            "updateTime": t.string().optional(),
            "gcpResource": t.string().optional(),
            "siteId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ApiCategoryDataOut"])
    types["GoogleCloudApigeeV1GraphQLOperationConfigIn"] = t.struct(
        {
            "apiSource": t.string(),
            "quota": t.proxy(renames["GoogleCloudApigeeV1QuotaIn"]).optional(),
            "operations": t.array(
                t.proxy(renames["GoogleCloudApigeeV1GraphQLOperationIn"])
            ),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1GraphQLOperationConfigIn"])
    types["GoogleCloudApigeeV1GraphQLOperationConfigOut"] = t.struct(
        {
            "apiSource": t.string(),
            "quota": t.proxy(renames["GoogleCloudApigeeV1QuotaOut"]).optional(),
            "operations": t.array(
                t.proxy(renames["GoogleCloudApigeeV1GraphQLOperationOut"])
            ),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1GraphQLOperationConfigOut"])
    types["GoogleTypeExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleTypeExprIn"])
    types["GoogleTypeExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeExprOut"])
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
    types["GoogleCloudApigeeV1CredentialIn"] = t.struct(
        {
            "consumerSecret": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
            ).optional(),
            "status": t.string().optional(),
            "issuedAt": t.string().optional(),
            "consumerKey": t.string().optional(),
            "expiresAt": t.string().optional(),
            "apiProducts": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ApiProductRefIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1CredentialIn"])
    types["GoogleCloudApigeeV1CredentialOut"] = t.struct(
        {
            "consumerSecret": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeOut"])
            ).optional(),
            "status": t.string().optional(),
            "issuedAt": t.string().optional(),
            "consumerKey": t.string().optional(),
            "expiresAt": t.string().optional(),
            "apiProducts": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ApiProductRefOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1CredentialOut"])
    types["GoogleCloudApigeeV1SharedFlowIn"] = t.struct(
        {
            "revision": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "metaData": t.proxy(
                renames["GoogleCloudApigeeV1EntityMetadataIn"]
            ).optional(),
            "latestRevisionId": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SharedFlowIn"])
    types["GoogleCloudApigeeV1SharedFlowOut"] = t.struct(
        {
            "revision": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "metaData": t.proxy(
                renames["GoogleCloudApigeeV1EntityMetadataOut"]
            ).optional(),
            "latestRevisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SharedFlowOut"])
    types["GoogleCloudApigeeV1DebugMaskIn"] = t.struct(
        {
            "requestJSONPaths": t.array(t.string()).optional(),
            "requestXPaths": t.array(t.string()).optional(),
            "variables": t.array(t.string()).optional(),
            "responseJSONPaths": t.array(t.string()).optional(),
            "namespaces": t.struct({"_": t.string().optional()}).optional(),
            "faultXPaths": t.array(t.string()).optional(),
            "responseXPaths": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "faultJSONPaths": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DebugMaskIn"])
    types["GoogleCloudApigeeV1DebugMaskOut"] = t.struct(
        {
            "requestJSONPaths": t.array(t.string()).optional(),
            "requestXPaths": t.array(t.string()).optional(),
            "variables": t.array(t.string()).optional(),
            "responseJSONPaths": t.array(t.string()).optional(),
            "namespaces": t.struct({"_": t.string().optional()}).optional(),
            "faultXPaths": t.array(t.string()).optional(),
            "responseXPaths": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "faultJSONPaths": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DebugMaskOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleCloudApigeeV1GraphQLOperationIn"] = t.struct(
        {"operationTypes": t.array(t.string()), "operation": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1GraphQLOperationIn"])
    types["GoogleCloudApigeeV1GraphQLOperationOut"] = t.struct(
        {
            "operationTypes": t.array(t.string()),
            "operation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1GraphQLOperationOut"])
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
    types["GoogleCloudApigeeV1AccessGetIn"] = t.struct(
        {"value": t.string(), "name": t.string()}
    ).named(renames["GoogleCloudApigeeV1AccessGetIn"])
    types["GoogleCloudApigeeV1AccessGetOut"] = t.struct(
        {
            "value": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AccessGetOut"])
    types["GoogleCloudApigeeV1DebugSessionTransactionIn"] = t.struct(
        {
            "completed": t.boolean().optional(),
            "point": t.array(t.proxy(renames["GoogleCloudApigeeV1PointIn"])).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DebugSessionTransactionIn"])
    types["GoogleCloudApigeeV1DebugSessionTransactionOut"] = t.struct(
        {
            "completed": t.boolean().optional(),
            "point": t.array(
                t.proxy(renames["GoogleCloudApigeeV1PointOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DebugSessionTransactionOut"])
    types["GoogleCloudApigeeV1RevisionStatusIn"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "jsonSpec": t.string().optional(),
            "errors": t.array(
                t.proxy(renames["GoogleCloudApigeeV1UpdateErrorIn"])
            ).optional(),
            "replicas": t.integer().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RevisionStatusIn"])
    types["GoogleCloudApigeeV1RevisionStatusOut"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "jsonSpec": t.string().optional(),
            "errors": t.array(
                t.proxy(renames["GoogleCloudApigeeV1UpdateErrorOut"])
            ).optional(),
            "replicas": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RevisionStatusOut"])
    types["GoogleCloudApigeeV1ResourceConfigIn"] = t.struct(
        {"location": t.string().optional(), "name": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1ResourceConfigIn"])
    types["GoogleCloudApigeeV1ResourceConfigOut"] = t.struct(
        {
            "location": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ResourceConfigOut"])
    types["GoogleCloudApigeeV1ApiSecurityConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["GoogleCloudApigeeV1ApiSecurityConfigIn"])
    types["GoogleCloudApigeeV1ApiSecurityConfigOut"] = t.struct(
        {
            "expiresAt": t.string().optional(),
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ApiSecurityConfigOut"])
    types["GoogleCloudApigeeV1SecurityProfileIn"] = t.struct(
        {
            "environments": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SecurityProfileEnvironmentIn"])
            ).optional(),
            "scoringConfigs": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SecurityProfileScoringConfigIn"])
            ).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityProfileIn"])
    types["GoogleCloudApigeeV1SecurityProfileOut"] = t.struct(
        {
            "environments": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SecurityProfileEnvironmentOut"])
            ).optional(),
            "scoringConfigs": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SecurityProfileScoringConfigOut"])
            ).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "maxScore": t.integer().optional(),
            "revisionPublishTime": t.string().optional(),
            "revisionUpdateTime": t.string().optional(),
            "minScore": t.integer().optional(),
            "revisionId": t.string().optional(),
            "revisionCreateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityProfileOut"])
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
    types["GoogleCloudApigeeV1RuntimeConfigIn"] = t.struct(
        {
            "traceBucket": t.string().optional(),
            "name": t.string().optional(),
            "analyticsBucket": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RuntimeConfigIn"])
    types["GoogleCloudApigeeV1RuntimeConfigOut"] = t.struct(
        {
            "traceBucket": t.string().optional(),
            "name": t.string().optional(),
            "tenantProjectId": t.string().optional(),
            "analyticsBucket": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RuntimeConfigOut"])
    types["GoogleCloudApigeeV1PointIn"] = t.struct(
        {
            "results": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ResultIn"])
            ).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1PointIn"])
    types["GoogleCloudApigeeV1PointOut"] = t.struct(
        {
            "results": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ResultOut"])
            ).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1PointOut"])
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
    types["GoogleCloudApigeeV1SecurityReportIn"] = t.struct(
        {
            "created": t.string().optional(),
            "executionTime": t.string().optional(),
            "reportDefinitionId": t.string().optional(),
            "resultRows": t.string().optional(),
            "self": t.string().optional(),
            "state": t.string().optional(),
            "displayName": t.string().optional(),
            "queryParams": t.proxy(
                renames["GoogleCloudApigeeV1SecurityReportMetadataIn"]
            ).optional(),
            "result": t.proxy(
                renames["GoogleCloudApigeeV1SecurityReportResultMetadataIn"]
            ).optional(),
            "envgroupHostname": t.string().optional(),
            "error": t.string().optional(),
            "resultFileSize": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityReportIn"])
    types["GoogleCloudApigeeV1SecurityReportOut"] = t.struct(
        {
            "created": t.string().optional(),
            "executionTime": t.string().optional(),
            "reportDefinitionId": t.string().optional(),
            "resultRows": t.string().optional(),
            "self": t.string().optional(),
            "state": t.string().optional(),
            "displayName": t.string().optional(),
            "queryParams": t.proxy(
                renames["GoogleCloudApigeeV1SecurityReportMetadataOut"]
            ).optional(),
            "result": t.proxy(
                renames["GoogleCloudApigeeV1SecurityReportResultMetadataOut"]
            ).optional(),
            "envgroupHostname": t.string().optional(),
            "updated": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "resultFileSize": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityReportOut"])
    types["GoogleCloudApigeeV1ArchiveDeploymentIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "gcsUri": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ArchiveDeploymentIn"])
    types["GoogleCloudApigeeV1ArchiveDeploymentOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "updatedAt": t.string().optional(),
            "gcsUri": t.string().optional(),
            "operation": t.string().optional(),
            "createdAt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ArchiveDeploymentOut"])
    types["GoogleCloudApigeeV1CustomReportMetricIn"] = t.struct(
        {"name": t.string().optional(), "function": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1CustomReportMetricIn"])
    types["GoogleCloudApigeeV1CustomReportMetricOut"] = t.struct(
        {
            "name": t.string().optional(),
            "function": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1CustomReportMetricOut"])
    types["GoogleCloudApigeeV1RuntimeTraceSamplingConfigIn"] = t.struct(
        {"samplingRate": t.number().optional(), "sampler": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1RuntimeTraceSamplingConfigIn"])
    types["GoogleCloudApigeeV1RuntimeTraceSamplingConfigOut"] = t.struct(
        {
            "samplingRate": t.number().optional(),
            "sampler": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RuntimeTraceSamplingConfigOut"])
    types["GoogleIamV1BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIamV1BindingIn"])
    types["GoogleIamV1BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingOut"])
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
    types["GoogleCloudApigeeV1DeploymentChangeReportRoutingChangeIn"] = t.struct(
        {
            "description": t.string().optional(),
            "environmentGroup": t.string().optional(),
            "shouldSequenceRollout": t.boolean().optional(),
            "fromDeployment": t.proxy(
                renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentIn"]
            ).optional(),
            "toDeployment": t.proxy(
                renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingChangeIn"])
    types["GoogleCloudApigeeV1DeploymentChangeReportRoutingChangeOut"] = t.struct(
        {
            "description": t.string().optional(),
            "environmentGroup": t.string().optional(),
            "shouldSequenceRollout": t.boolean().optional(),
            "fromDeployment": t.proxy(
                renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentOut"]
            ).optional(),
            "toDeployment": t.proxy(
                renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingChangeOut"])
    types["GoogleIamV1PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingIn"])).optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigIn"])
            ).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["GoogleIamV1PolicyIn"])
    types["GoogleIamV1PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingOut"])).optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigOut"])
            ).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1PolicyOut"])
    types["GoogleCloudApigeeV1ResultIn"] = t.struct(
        {
            "reasonPhrase": t.string().optional(),
            "statusCode": t.string().optional(),
            "accessList": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AccessIn"])
            ).optional(),
            "uRI": t.string().optional(),
            "content": t.string().optional(),
            "headers": t.array(
                t.proxy(renames["GoogleCloudApigeeV1PropertyIn"])
            ).optional(),
            "properties": t.proxy(
                renames["GoogleCloudApigeeV1PropertiesIn"]
            ).optional(),
            "verb": t.string().optional(),
            "timestamp": t.string().optional(),
            "ActionResult": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ResultIn"])
    types["GoogleCloudApigeeV1ResultOut"] = t.struct(
        {
            "reasonPhrase": t.string().optional(),
            "statusCode": t.string().optional(),
            "accessList": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AccessOut"])
            ).optional(),
            "uRI": t.string().optional(),
            "content": t.string().optional(),
            "headers": t.array(
                t.proxy(renames["GoogleCloudApigeeV1PropertyOut"])
            ).optional(),
            "properties": t.proxy(
                renames["GoogleCloudApigeeV1PropertiesOut"]
            ).optional(),
            "verb": t.string().optional(),
            "timestamp": t.string().optional(),
            "ActionResult": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ResultOut"])
    types["GoogleTypeIntervalIn"] = t.struct(
        {"startTime": t.string().optional(), "endTime": t.string().optional()}
    ).named(renames["GoogleTypeIntervalIn"])
    types["GoogleTypeIntervalOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeIntervalOut"])
    types["GoogleCloudApigeeV1QueryMetadataIn"] = t.struct(
        {
            "dimensions": t.array(t.string()).optional(),
            "outputFormat": t.string().optional(),
            "endTimestamp": t.string().optional(),
            "startTimestamp": t.string().optional(),
            "timeUnit": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryMetadataIn"])
    types["GoogleCloudApigeeV1QueryMetadataOut"] = t.struct(
        {
            "dimensions": t.array(t.string()).optional(),
            "outputFormat": t.string().optional(),
            "endTimestamp": t.string().optional(),
            "startTimestamp": t.string().optional(),
            "timeUnit": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryMetadataOut"])
    types["GoogleCloudApigeeV1SecurityProfileEnvironmentIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1SecurityProfileEnvironmentIn"])
    types["GoogleCloudApigeeV1SecurityProfileEnvironmentOut"] = t.struct(
        {
            "attachTime": t.string().optional(),
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityProfileEnvironmentOut"])
    types["GoogleCloudApigeeV1IntegrationConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["GoogleCloudApigeeV1IntegrationConfigIn"])
    types["GoogleCloudApigeeV1IntegrationConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1IntegrationConfigOut"])
    types["GoogleCloudApigeeV1OperationIn"] = t.struct(
        {"resource": t.string(), "methods": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudApigeeV1OperationIn"])
    types["GoogleCloudApigeeV1OperationOut"] = t.struct(
        {
            "resource": t.string(),
            "methods": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OperationOut"])
    types["GoogleCloudApigeeV1SecurityReportMetadataIn"] = t.struct(
        {
            "metrics": t.array(t.string()).optional(),
            "timeUnit": t.string().optional(),
            "endTimestamp": t.string().optional(),
            "mimeType": t.string().optional(),
            "startTimestamp": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityReportMetadataIn"])
    types["GoogleCloudApigeeV1SecurityReportMetadataOut"] = t.struct(
        {
            "metrics": t.array(t.string()).optional(),
            "timeUnit": t.string().optional(),
            "endTimestamp": t.string().optional(),
            "mimeType": t.string().optional(),
            "startTimestamp": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityReportMetadataOut"])
    types["GoogleCloudApigeeV1ReportInstanceStatusResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1ReportInstanceStatusResponseIn"])
    types["GoogleCloudApigeeV1ReportInstanceStatusResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudApigeeV1ReportInstanceStatusResponseOut"])
    types["GoogleCloudApigeeV1TlsInfoIn"] = t.struct(
        {
            "commonName": t.proxy(
                renames["GoogleCloudApigeeV1TlsInfoCommonNameIn"]
            ).optional(),
            "protocols": t.array(t.string()).optional(),
            "ciphers": t.array(t.string()).optional(),
            "enabled": t.boolean(),
            "keyStore": t.string(),
            "trustStore": t.string().optional(),
            "ignoreValidationErrors": t.boolean().optional(),
            "keyAlias": t.string(),
            "clientAuthEnabled": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1TlsInfoIn"])
    types["GoogleCloudApigeeV1TlsInfoOut"] = t.struct(
        {
            "commonName": t.proxy(
                renames["GoogleCloudApigeeV1TlsInfoCommonNameOut"]
            ).optional(),
            "protocols": t.array(t.string()).optional(),
            "ciphers": t.array(t.string()).optional(),
            "enabled": t.boolean(),
            "keyStore": t.string(),
            "trustStore": t.string().optional(),
            "ignoreValidationErrors": t.boolean().optional(),
            "keyAlias": t.string(),
            "clientAuthEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1TlsInfoOut"])
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
    types["GoogleCloudApigeeV1TlsInfoCommonNameIn"] = t.struct(
        {"wildcardMatch": t.boolean().optional(), "value": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1TlsInfoCommonNameIn"])
    types["GoogleCloudApigeeV1TlsInfoCommonNameOut"] = t.struct(
        {
            "wildcardMatch": t.boolean().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1TlsInfoCommonNameOut"])
    types["GoogleCloudApigeeV1GetSyncAuthorizationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1GetSyncAuthorizationRequestIn"])
    types["GoogleCloudApigeeV1GetSyncAuthorizationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudApigeeV1GetSyncAuthorizationRequestOut"])
    types["GoogleCloudApigeeV1ScoreIn"] = t.struct(
        {
            "component": t.proxy(
                renames["GoogleCloudApigeeV1ScoreComponentIn"]
            ).optional(),
            "subcomponents": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ScoreComponentIn"])
            ).optional(),
            "timeRange": t.proxy(renames["GoogleTypeIntervalIn"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ScoreIn"])
    types["GoogleCloudApigeeV1ScoreOut"] = t.struct(
        {
            "component": t.proxy(
                renames["GoogleCloudApigeeV1ScoreComponentOut"]
            ).optional(),
            "subcomponents": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ScoreComponentOut"])
            ).optional(),
            "timeRange": t.proxy(renames["GoogleTypeIntervalOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ScoreOut"])
    types["GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRouteIn"] = t.struct(
        {
            "percentage": t.integer().optional(),
            "basepath": t.string().optional(),
            "envgroup": t.string().optional(),
            "environment": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRouteIn"])
    types["GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRouteOut"] = t.struct(
        {
            "percentage": t.integer().optional(),
            "basepath": t.string().optional(),
            "envgroup": t.string().optional(),
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRouteOut"])
    types["GoogleCloudApigeeV1DebugSessionIn"] = t.struct(
        {
            "tracesize": t.integer().optional(),
            "count": t.integer().optional(),
            "filter": t.string().optional(),
            "validity": t.integer().optional(),
            "name": t.string().optional(),
            "timeout": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DebugSessionIn"])
    types["GoogleCloudApigeeV1DebugSessionOut"] = t.struct(
        {
            "tracesize": t.integer().optional(),
            "count": t.integer().optional(),
            "filter": t.string().optional(),
            "validity": t.integer().optional(),
            "name": t.string().optional(),
            "timeout": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DebugSessionOut"])
    types["GoogleCloudApigeeV1ListSecurityProfilesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "securityProfiles": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SecurityProfileIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListSecurityProfilesResponseIn"])
    types["GoogleCloudApigeeV1ListSecurityProfilesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "securityProfiles": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SecurityProfileOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListSecurityProfilesResponseOut"])
    types["GoogleCloudApigeeV1SecurityReportResultMetadataIn"] = t.struct(
        {"self": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1SecurityReportResultMetadataIn"])
    types["GoogleCloudApigeeV1SecurityReportResultMetadataOut"] = t.struct(
        {
            "self": t.string().optional(),
            "expires": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityReportResultMetadataOut"])
    types["GoogleCloudApigeeV1EnvironmentGroupAttachmentIn"] = t.struct(
        {"name": t.string().optional(), "environment": t.string()}
    ).named(renames["GoogleCloudApigeeV1EnvironmentGroupAttachmentIn"])
    types["GoogleCloudApigeeV1EnvironmentGroupAttachmentOut"] = t.struct(
        {
            "name": t.string().optional(),
            "environment": t.string(),
            "createdAt": t.string().optional(),
            "environmentGroupId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1EnvironmentGroupAttachmentOut"])
    types["GoogleCloudApigeeV1SecurityIncidentIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "trafficCount": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityIncidentIn"])
    types["GoogleCloudApigeeV1SecurityIncidentOut"] = t.struct(
        {
            "detectionTypes": t.array(t.string()).optional(),
            "riskLevel": t.string().optional(),
            "firstDetectedTime": t.string().optional(),
            "displayName": t.string().optional(),
            "trafficCount": t.string().optional(),
            "lastDetectedTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SecurityIncidentOut"])
    types["GoogleCloudApigeeV1ConfigVersionIn"] = t.struct(
        {"majorVersion": t.integer().optional(), "minorVersion": t.integer().optional()}
    ).named(renames["GoogleCloudApigeeV1ConfigVersionIn"])
    types["GoogleCloudApigeeV1ConfigVersionOut"] = t.struct(
        {
            "majorVersion": t.integer().optional(),
            "minorVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ConfigVersionOut"])
    types["GoogleCloudApigeeV1ApiProxyRevisionIn"] = t.struct(
        {
            "entityMetaDataAsProperties": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "resources": t.array(t.string()).optional(),
            "teams": t.array(t.string()).optional(),
            "integrationEndpoints": t.array(t.string()).optional(),
            "revision": t.string().optional(),
            "sharedFlows": t.array(t.string()).optional(),
            "resourceFiles": t.proxy(
                renames["GoogleCloudApigeeV1ResourceFilesIn"]
            ).optional(),
            "type": t.string().optional(),
            "spec": t.string().optional(),
            "contextInfo": t.string().optional(),
            "proxies": t.array(t.string()).optional(),
            "targets": t.array(t.string()).optional(),
            "policies": t.array(t.string()).optional(),
            "basepaths": t.array(t.string()).optional(),
            "proxyEndpoints": t.array(t.string()).optional(),
            "lastModifiedAt": t.string().optional(),
            "displayName": t.string().optional(),
            "targetEndpoints": t.array(t.string()).optional(),
            "targetServers": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "configurationVersion": t.proxy(
                renames["GoogleCloudApigeeV1ConfigVersionIn"]
            ).optional(),
            "description": t.string().optional(),
            "createdAt": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ApiProxyRevisionIn"])
    types["GoogleCloudApigeeV1ApiProxyRevisionOut"] = t.struct(
        {
            "entityMetaDataAsProperties": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "resources": t.array(t.string()).optional(),
            "teams": t.array(t.string()).optional(),
            "integrationEndpoints": t.array(t.string()).optional(),
            "revision": t.string().optional(),
            "sharedFlows": t.array(t.string()).optional(),
            "resourceFiles": t.proxy(
                renames["GoogleCloudApigeeV1ResourceFilesOut"]
            ).optional(),
            "archive": t.string().optional(),
            "type": t.string().optional(),
            "spec": t.string().optional(),
            "contextInfo": t.string().optional(),
            "proxies": t.array(t.string()).optional(),
            "targets": t.array(t.string()).optional(),
            "policies": t.array(t.string()).optional(),
            "basepaths": t.array(t.string()).optional(),
            "proxyEndpoints": t.array(t.string()).optional(),
            "lastModifiedAt": t.string().optional(),
            "displayName": t.string().optional(),
            "targetEndpoints": t.array(t.string()).optional(),
            "targetServers": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "configurationVersion": t.proxy(
                renames["GoogleCloudApigeeV1ConfigVersionOut"]
            ).optional(),
            "description": t.string().optional(),
            "createdAt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ApiProxyRevisionOut"])
    types["GoogleCloudApigeeV1SchemaIn"] = t.struct(
        {
            "meta": t.array(t.string()).optional(),
            "dimensions": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SchemaSchemaElementIn"])
            ).optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SchemaSchemaElementIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SchemaIn"])
    types["GoogleCloudApigeeV1SchemaOut"] = t.struct(
        {
            "meta": t.array(t.string()).optional(),
            "dimensions": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SchemaSchemaElementOut"])
            ).optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SchemaSchemaElementOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SchemaOut"])
    types["GoogleIamV1TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsResponseIn"])
    types["GoogleIamV1TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsResponseOut"])
    types["GoogleCloudApigeeV1RatePlanIn"] = t.struct(
        {
            "revenueShareRates": t.array(
                t.proxy(renames["GoogleCloudApigeeV1RevenueShareRangeIn"])
            ).optional(),
            "revenueShareType": t.string().optional(),
            "fixedRecurringFee": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
            "paymentFundingModel": t.string().optional(),
            "fixedFeeFrequency": t.integer().optional(),
            "currencyCode": t.string().optional(),
            "consumptionPricingType": t.string().optional(),
            "startTime": t.string().optional(),
            "setupFee": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
            "state": t.string().optional(),
            "displayName": t.string().optional(),
            "billingPeriod": t.string().optional(),
            "apiproduct": t.string().optional(),
            "description": t.string().optional(),
            "endTime": t.string().optional(),
            "consumptionPricingRates": t.array(
                t.proxy(renames["GoogleCloudApigeeV1RateRangeIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RatePlanIn"])
    types["GoogleCloudApigeeV1RatePlanOut"] = t.struct(
        {
            "revenueShareRates": t.array(
                t.proxy(renames["GoogleCloudApigeeV1RevenueShareRangeOut"])
            ).optional(),
            "revenueShareType": t.string().optional(),
            "lastModifiedAt": t.string().optional(),
            "fixedRecurringFee": t.proxy(renames["GoogleTypeMoneyOut"]).optional(),
            "paymentFundingModel": t.string().optional(),
            "fixedFeeFrequency": t.integer().optional(),
            "currencyCode": t.string().optional(),
            "consumptionPricingType": t.string().optional(),
            "startTime": t.string().optional(),
            "setupFee": t.proxy(renames["GoogleTypeMoneyOut"]).optional(),
            "state": t.string().optional(),
            "displayName": t.string().optional(),
            "createdAt": t.string().optional(),
            "billingPeriod": t.string().optional(),
            "name": t.string().optional(),
            "apiproduct": t.string().optional(),
            "description": t.string().optional(),
            "endTime": t.string().optional(),
            "consumptionPricingRates": t.array(
                t.proxy(renames["GoogleCloudApigeeV1RateRangeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RatePlanOut"])
    types["GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilterIn"] = t.struct(
        {"scorePath": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilterIn"])
    types["GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilterOut"] = t.struct(
        {
            "scorePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilterOut"])
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
    types["GoogleCloudApigeeV1TargetServerIn"] = t.struct(
        {
            "sSLInfo": t.proxy(renames["GoogleCloudApigeeV1TlsInfoIn"]).optional(),
            "host": t.string(),
            "description": t.string().optional(),
            "port": t.integer(),
            "isEnabled": t.boolean().optional(),
            "protocol": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["GoogleCloudApigeeV1TargetServerIn"])
    types["GoogleCloudApigeeV1TargetServerOut"] = t.struct(
        {
            "sSLInfo": t.proxy(renames["GoogleCloudApigeeV1TlsInfoOut"]).optional(),
            "host": t.string(),
            "description": t.string().optional(),
            "port": t.integer(),
            "isEnabled": t.boolean().optional(),
            "protocol": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1TargetServerOut"])
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
    types["GoogleCloudApigeeV1RuntimeTraceConfigOverrideIn"] = t.struct(
        {
            "name": t.string().optional(),
            "revisionCreateTime": t.string().optional(),
            "revisionId": t.string().optional(),
            "apiProxy": t.string().optional(),
            "uid": t.string().optional(),
            "samplingConfig": t.proxy(
                renames["GoogleCloudApigeeV1RuntimeTraceSamplingConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RuntimeTraceConfigOverrideIn"])
    types["GoogleCloudApigeeV1RuntimeTraceConfigOverrideOut"] = t.struct(
        {
            "name": t.string().optional(),
            "revisionCreateTime": t.string().optional(),
            "revisionId": t.string().optional(),
            "apiProxy": t.string().optional(),
            "uid": t.string().optional(),
            "samplingConfig": t.proxy(
                renames["GoogleCloudApigeeV1RuntimeTraceSamplingConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RuntimeTraceConfigOverrideOut"])
    types["GoogleCloudApigeeV1ExportIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "datastoreName": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ExportIn"])
    types["GoogleCloudApigeeV1ExportOut"] = t.struct(
        {
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "description": t.string().optional(),
            "self": t.string().optional(),
            "name": t.string().optional(),
            "datastoreName": t.string().optional(),
            "executionTime": t.string().optional(),
            "updated": t.string().optional(),
            "created": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ExportOut"])
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
    types["GoogleIamV1AuditLogConfigIn"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
        }
    ).named(renames["GoogleIamV1AuditLogConfigIn"])
    types["GoogleIamV1AuditLogConfigOut"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1AuditLogConfigOut"])
    types["GoogleCloudApigeeV1InstanceDeploymentStatusIn"] = t.struct(
        {
            "deployedRevisions": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRevisionIn"
                    ]
                )
            ).optional(),
            "instance": t.string().optional(),
            "deployedRoutes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRouteIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1InstanceDeploymentStatusIn"])
    types["GoogleCloudApigeeV1InstanceDeploymentStatusOut"] = t.struct(
        {
            "deployedRevisions": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRevisionOut"
                    ]
                )
            ).optional(),
            "instance": t.string().optional(),
            "deployedRoutes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRouteOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1InstanceDeploymentStatusOut"])
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
    types["GoogleCloudApigeeV1DeveloperAppIn"] = t.struct(
        {
            "status": t.string().optional(),
            "developerId": t.string().optional(),
            "appId": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
            ).optional(),
            "appFamily": t.string().optional(),
            "callbackUrl": t.string().optional(),
            "name": t.string().optional(),
            "keyExpiresIn": t.string().optional(),
            "apiProducts": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeveloperAppIn"])
    types["GoogleCloudApigeeV1DeveloperAppOut"] = t.struct(
        {
            "status": t.string().optional(),
            "developerId": t.string().optional(),
            "lastModifiedAt": t.string().optional(),
            "createdAt": t.string().optional(),
            "appId": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeOut"])
            ).optional(),
            "appFamily": t.string().optional(),
            "callbackUrl": t.string().optional(),
            "name": t.string().optional(),
            "credentials": t.array(
                t.proxy(renames["GoogleCloudApigeeV1CredentialOut"])
            ).optional(),
            "keyExpiresIn": t.string().optional(),
            "apiProducts": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeveloperAppOut"])
    types["GoogleCloudApigeeV1GraphQLOperationGroupIn"] = t.struct(
        {
            "operationConfigs": t.array(
                t.proxy(renames["GoogleCloudApigeeV1GraphQLOperationConfigIn"])
            ),
            "operationConfigType": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1GraphQLOperationGroupIn"])
    types["GoogleCloudApigeeV1GraphQLOperationGroupOut"] = t.struct(
        {
            "operationConfigs": t.array(
                t.proxy(renames["GoogleCloudApigeeV1GraphQLOperationConfigOut"])
            ),
            "operationConfigType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1GraphQLOperationGroupOut"])
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
    types["GoogleCloudApigeeV1EnvironmentIn"] = t.struct(
        {
            "forwardProxyUri": t.string().optional(),
            "nodeConfig": t.proxy(
                renames["GoogleCloudApigeeV1NodeConfigIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "apiProxyType": t.string().optional(),
            "deploymentType": t.string().optional(),
            "name": t.string(),
            "properties": t.proxy(
                renames["GoogleCloudApigeeV1PropertiesIn"]
            ).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1EnvironmentIn"])
    types["GoogleCloudApigeeV1EnvironmentOut"] = t.struct(
        {
            "lastModifiedAt": t.string().optional(),
            "forwardProxyUri": t.string().optional(),
            "nodeConfig": t.proxy(
                renames["GoogleCloudApigeeV1NodeConfigOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "apiProxyType": t.string().optional(),
            "deploymentType": t.string().optional(),
            "createdAt": t.string().optional(),
            "name": t.string(),
            "properties": t.proxy(
                renames["GoogleCloudApigeeV1PropertiesOut"]
            ).optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1EnvironmentOut"])
    types["GoogleCloudApigeeV1QueryTabularStatsResponseIn"] = t.struct(
        {
            "values": t.array(
                t.array(t.struct({"_": t.string().optional()}))
            ).optional(),
            "columns": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryTabularStatsResponseIn"])
    types["GoogleCloudApigeeV1QueryTabularStatsResponseOut"] = t.struct(
        {
            "values": t.array(
                t.array(t.struct({"_": t.string().optional()}))
            ).optional(),
            "columns": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryTabularStatsResponseOut"])
    types["GoogleApiHttpBodyIn"] = t.struct(
        {
            "data": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "contentType": t.string().optional(),
        }
    ).named(renames["GoogleApiHttpBodyIn"])
    types["GoogleApiHttpBodyOut"] = t.struct(
        {
            "data": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "contentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApiHttpBodyOut"])
    types["GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseURLInfoIn"] = t.struct(
        {
            "md5": t.string().optional(),
            "uri": t.string().optional(),
            "sizeBytes": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseURLInfoIn"])
    types["GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseURLInfoOut"] = t.struct(
        {
            "md5": t.string().optional(),
            "uri": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseURLInfoOut"])
    types["GoogleCloudApigeeV1ActivateNatAddressRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1ActivateNatAddressRequestIn"])
    types["GoogleCloudApigeeV1ActivateNatAddressRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudApigeeV1ActivateNatAddressRequestOut"])
    types["GoogleCloudApigeeV1IngressConfigIn"] = t.struct(
        {
            "name": t.string().optional(),
            "revisionCreateTime": t.string().optional(),
            "uid": t.string().optional(),
            "revisionId": t.string().optional(),
            "environmentGroups": t.array(
                t.proxy(renames["GoogleCloudApigeeV1EnvironmentGroupConfigIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1IngressConfigIn"])
    types["GoogleCloudApigeeV1IngressConfigOut"] = t.struct(
        {
            "name": t.string().optional(),
            "revisionCreateTime": t.string().optional(),
            "uid": t.string().optional(),
            "revisionId": t.string().optional(),
            "environmentGroups": t.array(
                t.proxy(renames["GoogleCloudApigeeV1EnvironmentGroupConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1IngressConfigOut"])
    types["GoogleCloudApigeeV1DeploymentChangeReportIn"] = t.struct(
        {
            "routingChanges": t.array(
                t.proxy(
                    renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingChangeIn"]
                )
            ).optional(),
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
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentChangeReportIn"])
    types["GoogleCloudApigeeV1DeploymentChangeReportOut"] = t.struct(
        {
            "routingChanges": t.array(
                t.proxy(
                    renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingChangeOut"]
                )
            ).optional(),
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
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentChangeReportOut"])
    types["GoogleCloudApigeeV1SharedFlowRevisionIn"] = t.struct(
        {
            "contextInfo": t.string().optional(),
            "revision": t.string().optional(),
            "resourceFiles": t.proxy(
                renames["GoogleCloudApigeeV1ResourceFilesIn"]
            ).optional(),
            "lastModifiedAt": t.string().optional(),
            "resources": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "policies": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "sharedFlows": t.array(t.string()).optional(),
            "entityMetaDataAsProperties": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "createdAt": t.string().optional(),
            "configurationVersion": t.proxy(
                renames["GoogleCloudApigeeV1ConfigVersionIn"]
            ).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SharedFlowRevisionIn"])
    types["GoogleCloudApigeeV1SharedFlowRevisionOut"] = t.struct(
        {
            "contextInfo": t.string().optional(),
            "revision": t.string().optional(),
            "resourceFiles": t.proxy(
                renames["GoogleCloudApigeeV1ResourceFilesOut"]
            ).optional(),
            "lastModifiedAt": t.string().optional(),
            "resources": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "policies": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "sharedFlows": t.array(t.string()).optional(),
            "entityMetaDataAsProperties": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "createdAt": t.string().optional(),
            "configurationVersion": t.proxy(
                renames["GoogleCloudApigeeV1ConfigVersionOut"]
            ).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SharedFlowRevisionOut"])
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
    types["GoogleCloudApigeeV1UpdateErrorIn"] = t.struct(
        {
            "resource": t.string().optional(),
            "type": t.string().optional(),
            "code": t.string().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1UpdateErrorIn"])
    types["GoogleCloudApigeeV1UpdateErrorOut"] = t.struct(
        {
            "resource": t.string().optional(),
            "type": t.string().optional(),
            "code": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1UpdateErrorOut"])
    types["GoogleCloudApigeeV1NatAddressIn"] = t.struct({"name": t.string()}).named(
        renames["GoogleCloudApigeeV1NatAddressIn"]
    )
    types["GoogleCloudApigeeV1NatAddressOut"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1NatAddressOut"])
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
    types["GoogleCloudApigeeV1RateRangeIn"] = t.struct(
        {
            "end": t.string().optional(),
            "fee": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
            "start": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RateRangeIn"])
    types["GoogleCloudApigeeV1RateRangeOut"] = t.struct(
        {
            "end": t.string().optional(),
            "fee": t.proxy(renames["GoogleTypeMoneyOut"]).optional(),
            "start": t.string().optional(),
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
    types["GoogleCloudApigeeV1DeleteResponseIn"] = t.struct(
        {
            "message": t.string().optional(),
            "gcpResource": t.string().optional(),
            "status": t.string().optional(),
            "requestId": t.string().optional(),
            "errorCode": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeleteResponseIn"])
    types["GoogleCloudApigeeV1DeleteResponseOut"] = t.struct(
        {
            "message": t.string().optional(),
            "gcpResource": t.string().optional(),
            "status": t.string().optional(),
            "requestId": t.string().optional(),
            "errorCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeleteResponseOut"])
    types["GoogleCloudApigeeV1AddonsConfigIn"] = t.struct(
        {
            "apiSecurityConfig": t.proxy(
                renames["GoogleCloudApigeeV1ApiSecurityConfigIn"]
            ).optional(),
            "integrationConfig": t.proxy(
                renames["GoogleCloudApigeeV1IntegrationConfigIn"]
            ).optional(),
            "monetizationConfig": t.proxy(
                renames["GoogleCloudApigeeV1MonetizationConfigIn"]
            ).optional(),
            "advancedApiOpsConfig": t.proxy(
                renames["GoogleCloudApigeeV1AdvancedApiOpsConfigIn"]
            ).optional(),
            "connectorsPlatformConfig": t.proxy(
                renames["GoogleCloudApigeeV1ConnectorsPlatformConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AddonsConfigIn"])
    types["GoogleCloudApigeeV1AddonsConfigOut"] = t.struct(
        {
            "apiSecurityConfig": t.proxy(
                renames["GoogleCloudApigeeV1ApiSecurityConfigOut"]
            ).optional(),
            "integrationConfig": t.proxy(
                renames["GoogleCloudApigeeV1IntegrationConfigOut"]
            ).optional(),
            "monetizationConfig": t.proxy(
                renames["GoogleCloudApigeeV1MonetizationConfigOut"]
            ).optional(),
            "advancedApiOpsConfig": t.proxy(
                renames["GoogleCloudApigeeV1AdvancedApiOpsConfigOut"]
            ).optional(),
            "connectorsPlatformConfig": t.proxy(
                renames["GoogleCloudApigeeV1ConnectorsPlatformConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AddonsConfigOut"])
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
            "uid": t.string().optional(),
            "totalReplicas": t.integer().optional(),
            "resource": t.string().optional(),
            "revisions": t.array(
                t.proxy(renames["GoogleCloudApigeeV1RevisionStatusIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ResourceStatusIn"])
    types["GoogleCloudApigeeV1ResourceStatusOut"] = t.struct(
        {
            "uid": t.string().optional(),
            "totalReplicas": t.integer().optional(),
            "resource": t.string().optional(),
            "revisions": t.array(
                t.proxy(renames["GoogleCloudApigeeV1RevisionStatusOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ResourceStatusOut"])
    types["GoogleCloudApigeeV1DimensionMetricIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1MetricIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DimensionMetricIn"])
    types["GoogleCloudApigeeV1DimensionMetricOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1MetricOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DimensionMetricOut"])
    types["GoogleCloudApigeeV1GenerateDownloadUrlResponseIn"] = t.struct(
        {"downloadUri": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1GenerateDownloadUrlResponseIn"])
    types["GoogleCloudApigeeV1GenerateDownloadUrlResponseOut"] = t.struct(
        {
            "downloadUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1GenerateDownloadUrlResponseOut"])
    types["GoogleCloudApigeeV1DeveloperMonetizationConfigIn"] = t.struct(
        {"billingType": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1DeveloperMonetizationConfigIn"])
    types["GoogleCloudApigeeV1DeveloperMonetizationConfigOut"] = t.struct(
        {
            "billingType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeveloperMonetizationConfigOut"])
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
    types["GoogleCloudApigeeV1FlowHookConfigIn"] = t.struct(
        {
            "continueOnError": t.boolean().optional(),
            "name": t.string().optional(),
            "sharedFlowName": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1FlowHookConfigIn"])
    types["GoogleCloudApigeeV1FlowHookConfigOut"] = t.struct(
        {
            "continueOnError": t.boolean().optional(),
            "name": t.string().optional(),
            "sharedFlowName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1FlowHookConfigOut"])
    types["GoogleCloudApigeeV1ListTraceConfigOverridesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "traceConfigOverrides": t.array(
                t.proxy(renames["GoogleCloudApigeeV1TraceConfigOverrideIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListTraceConfigOverridesResponseIn"])
    types["GoogleCloudApigeeV1ListTraceConfigOverridesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "traceConfigOverrides": t.array(
                t.proxy(renames["GoogleCloudApigeeV1TraceConfigOverrideOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListTraceConfigOverridesResponseOut"])
    types["GoogleCloudApigeeV1QueryIn"] = t.struct(
        {
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1QueryMetricIn"])
            ).optional(),
            "outputFormat": t.string().optional(),
            "name": t.string().optional(),
            "csvDelimiter": t.string().optional(),
            "timeRange": t.struct({"_": t.string().optional()}),
            "filter": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "reportDefinitionId": t.string().optional(),
            "envgroupHostname": t.string().optional(),
            "limit": t.integer().optional(),
            "groupByTimeUnit": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryIn"])
    types["GoogleCloudApigeeV1QueryOut"] = t.struct(
        {
            "metrics": t.array(
                t.proxy(renames["GoogleCloudApigeeV1QueryMetricOut"])
            ).optional(),
            "outputFormat": t.string().optional(),
            "name": t.string().optional(),
            "csvDelimiter": t.string().optional(),
            "timeRange": t.struct({"_": t.string().optional()}),
            "filter": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "reportDefinitionId": t.string().optional(),
            "envgroupHostname": t.string().optional(),
            "limit": t.integer().optional(),
            "groupByTimeUnit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1QueryOut"])
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
    types["GoogleCloudApigeeV1DeveloperIn"] = t.struct(
        {
            "userName": t.string(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
            ).optional(),
            "email": t.string(),
            "accessType": t.string().optional(),
            "firstName": t.string(),
            "appFamily": t.string().optional(),
            "apps": t.array(t.string()).optional(),
            "lastName": t.string(),
            "developerId": t.string().optional(),
            "companies": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeveloperIn"])
    types["GoogleCloudApigeeV1DeveloperOut"] = t.struct(
        {
            "userName": t.string(),
            "organizationName": t.string().optional(),
            "lastModifiedAt": t.string().optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeOut"])
            ).optional(),
            "createdAt": t.string().optional(),
            "email": t.string(),
            "status": t.string().optional(),
            "accessType": t.string().optional(),
            "firstName": t.string(),
            "appFamily": t.string().optional(),
            "apps": t.array(t.string()).optional(),
            "lastName": t.string(),
            "developerId": t.string().optional(),
            "companies": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeveloperOut"])
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
    types["GoogleCloudApigeeV1MetricAggregationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "aggregation": t.string().optional(),
            "order": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1MetricAggregationIn"])
    types["GoogleCloudApigeeV1MetricAggregationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "aggregation": t.string().optional(),
            "order": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1MetricAggregationOut"])
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
    types["GoogleCloudApigeeV1OrganizationProjectMappingIn"] = t.struct(
        {
            "organization": t.string().optional(),
            "projectIds": t.array(t.string()).optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OrganizationProjectMappingIn"])
    types["GoogleCloudApigeeV1OrganizationProjectMappingOut"] = t.struct(
        {
            "organization": t.string().optional(),
            "projectIds": t.array(t.string()).optional(),
            "location": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OrganizationProjectMappingOut"])
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
    types["GoogleCloudApigeeV1OptimizedStatsResponseIn"] = t.struct(
        {
            "metaData": t.proxy(renames["GoogleCloudApigeeV1MetadataIn"]).optional(),
            "stats": t.proxy(
                renames["GoogleCloudApigeeV1OptimizedStatsNodeIn"]
            ).optional(),
            "resultTruncated": t.boolean().optional(),
            "TimeUnit": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OptimizedStatsResponseIn"])
    types["GoogleCloudApigeeV1OptimizedStatsResponseOut"] = t.struct(
        {
            "metaData": t.proxy(renames["GoogleCloudApigeeV1MetadataOut"]).optional(),
            "stats": t.proxy(
                renames["GoogleCloudApigeeV1OptimizedStatsNodeOut"]
            ).optional(),
            "resultTruncated": t.boolean().optional(),
            "TimeUnit": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OptimizedStatsResponseOut"])
    types["GoogleCloudApigeeV1SubscriptionIn"] = t.struct(
        {"name": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1SubscriptionIn"])
    types["GoogleCloudApigeeV1SubscriptionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SubscriptionOut"])
    types["GoogleCloudApigeeV1ExportRequestIn"] = t.struct(
        {
            "datastoreName": t.string(),
            "csvDelimiter": t.string().optional(),
            "name": t.string(),
            "dateRange": t.proxy(renames["GoogleCloudApigeeV1DateRangeIn"]),
            "description": t.string().optional(),
            "outputFormat": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ExportRequestIn"])
    types["GoogleCloudApigeeV1ExportRequestOut"] = t.struct(
        {
            "datastoreName": t.string(),
            "csvDelimiter": t.string().optional(),
            "name": t.string(),
            "dateRange": t.proxy(renames["GoogleCloudApigeeV1DateRangeOut"]),
            "description": t.string().optional(),
            "outputFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ExportRequestOut"])
    types["GoogleCloudApigeeV1ListSecurityProfileRevisionsResponseIn"] = t.struct(
        {
            "securityProfiles": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SecurityProfileIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListSecurityProfileRevisionsResponseIn"])
    types["GoogleCloudApigeeV1ListSecurityProfileRevisionsResponseOut"] = t.struct(
        {
            "securityProfiles": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SecurityProfileOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListSecurityProfileRevisionsResponseOut"])
    types["GoogleCloudApigeeV1TlsInfoConfigIn"] = t.struct(
        {
            "trustStore": t.string().optional(),
            "ignoreValidationErrors": t.boolean().optional(),
            "enabled": t.boolean().optional(),
            "commonName": t.proxy(
                renames["GoogleCloudApigeeV1CommonNameConfigIn"]
            ).optional(),
            "keyAlias": t.string().optional(),
            "keyAliasReference": t.proxy(
                renames["GoogleCloudApigeeV1KeyAliasReferenceIn"]
            ).optional(),
            "ciphers": t.array(t.string()).optional(),
            "protocols": t.array(t.string()).optional(),
            "clientAuthEnabled": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1TlsInfoConfigIn"])
    types["GoogleCloudApigeeV1TlsInfoConfigOut"] = t.struct(
        {
            "trustStore": t.string().optional(),
            "ignoreValidationErrors": t.boolean().optional(),
            "enabled": t.boolean().optional(),
            "commonName": t.proxy(
                renames["GoogleCloudApigeeV1CommonNameConfigOut"]
            ).optional(),
            "keyAlias": t.string().optional(),
            "keyAliasReference": t.proxy(
                renames["GoogleCloudApigeeV1KeyAliasReferenceOut"]
            ).optional(),
            "ciphers": t.array(t.string()).optional(),
            "protocols": t.array(t.string()).optional(),
            "clientAuthEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1TlsInfoConfigOut"])
    types["GoogleCloudApigeeV1EnvironmentConfigIn"] = t.struct(
        {
            "keystores": t.array(
                t.proxy(renames["GoogleCloudApigeeV1KeystoreConfigIn"])
            ).optional(),
            "sequenceNumber": t.string().optional(),
            "provider": t.string().optional(),
            "gatewayConfigLocation": t.string().optional(),
            "debugMask": t.proxy(renames["GoogleCloudApigeeV1DebugMaskIn"]).optional(),
            "name": t.string().optional(),
            "revisionId": t.string().optional(),
            "traceConfig": t.proxy(
                renames["GoogleCloudApigeeV1RuntimeTraceConfigIn"]
            ).optional(),
            "arcConfigLocation": t.string().optional(),
            "deployments": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DeploymentConfigIn"])
            ).optional(),
            "targets": t.array(
                t.proxy(renames["GoogleCloudApigeeV1TargetServerConfigIn"])
            ).optional(),
            "pubsubTopic": t.string().optional(),
            "uid": t.string().optional(),
            "createTime": t.string().optional(),
            "resources": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ResourceConfigIn"])
            ).optional(),
            "forwardProxyUri": t.string().optional(),
            "deploymentGroups": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DeploymentGroupConfigIn"])
            ).optional(),
            "featureFlags": t.struct({"_": t.string().optional()}).optional(),
            "dataCollectors": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DataCollectorConfigIn"])
            ).optional(),
            "flowhooks": t.array(
                t.proxy(renames["GoogleCloudApigeeV1FlowHookConfigIn"])
            ).optional(),
            "resourceReferences": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ReferenceConfigIn"])
            ).optional(),
            "envScopedRevisionId": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1EnvironmentConfigIn"])
    types["GoogleCloudApigeeV1EnvironmentConfigOut"] = t.struct(
        {
            "keystores": t.array(
                t.proxy(renames["GoogleCloudApigeeV1KeystoreConfigOut"])
            ).optional(),
            "sequenceNumber": t.string().optional(),
            "provider": t.string().optional(),
            "gatewayConfigLocation": t.string().optional(),
            "debugMask": t.proxy(renames["GoogleCloudApigeeV1DebugMaskOut"]).optional(),
            "name": t.string().optional(),
            "revisionId": t.string().optional(),
            "traceConfig": t.proxy(
                renames["GoogleCloudApigeeV1RuntimeTraceConfigOut"]
            ).optional(),
            "arcConfigLocation": t.string().optional(),
            "deployments": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DeploymentConfigOut"])
            ).optional(),
            "targets": t.array(
                t.proxy(renames["GoogleCloudApigeeV1TargetServerConfigOut"])
            ).optional(),
            "pubsubTopic": t.string().optional(),
            "uid": t.string().optional(),
            "createTime": t.string().optional(),
            "resources": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ResourceConfigOut"])
            ).optional(),
            "forwardProxyUri": t.string().optional(),
            "deploymentGroups": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DeploymentGroupConfigOut"])
            ).optional(),
            "featureFlags": t.struct({"_": t.string().optional()}).optional(),
            "dataCollectors": t.array(
                t.proxy(renames["GoogleCloudApigeeV1DataCollectorConfigOut"])
            ).optional(),
            "flowhooks": t.array(
                t.proxy(renames["GoogleCloudApigeeV1FlowHookConfigOut"])
            ).optional(),
            "resourceReferences": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ReferenceConfigOut"])
            ).optional(),
            "envScopedRevisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1EnvironmentConfigOut"])
    types["GoogleCloudApigeeV1AliasIn"] = t.struct(
        {
            "alias": t.string().optional(),
            "certsInfo": t.proxy(
                renames["GoogleCloudApigeeV1CertificateIn"]
            ).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AliasIn"])
    types["GoogleCloudApigeeV1AliasOut"] = t.struct(
        {
            "alias": t.string().optional(),
            "certsInfo": t.proxy(
                renames["GoogleCloudApigeeV1CertificateOut"]
            ).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AliasOut"])
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
    types["GoogleCloudApigeeV1ListArchiveDeploymentsResponseIn"] = t.struct(
        {
            "archiveDeployments": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ArchiveDeploymentIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListArchiveDeploymentsResponseIn"])
    types["GoogleCloudApigeeV1ListArchiveDeploymentsResponseOut"] = t.struct(
        {
            "archiveDeployments": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ArchiveDeploymentOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListArchiveDeploymentsResponseOut"])
    types["GoogleCloudApigeeV1GenerateUploadUrlRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1GenerateUploadUrlRequestIn"])
    types["GoogleCloudApigeeV1GenerateUploadUrlRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudApigeeV1GenerateUploadUrlRequestOut"])
    types["GoogleCloudApigeeV1GenerateDownloadUrlRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1GenerateDownloadUrlRequestIn"])
    types["GoogleCloudApigeeV1GenerateDownloadUrlRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudApigeeV1GenerateDownloadUrlRequestOut"])
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
    types["GoogleCloudApigeeV1ListApiCategoriesResponseIn"] = t.struct(
        {
            "status": t.string().optional(),
            "message": t.string().optional(),
            "errorCode": t.string().optional(),
            "requestId": t.string().optional(),
            "data": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ApiCategoryDataIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListApiCategoriesResponseIn"])
    types["GoogleCloudApigeeV1ListApiCategoriesResponseOut"] = t.struct(
        {
            "status": t.string().optional(),
            "message": t.string().optional(),
            "errorCode": t.string().optional(),
            "requestId": t.string().optional(),
            "data": t.array(
                t.proxy(renames["GoogleCloudApigeeV1ApiCategoryDataOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListApiCategoriesResponseOut"])
    types["GoogleCloudApigeeV1StatsIn"] = t.struct(
        {
            "environments": t.array(
                t.proxy(renames["GoogleCloudApigeeV1StatsEnvironmentStatsIn"])
            ).optional(),
            "hosts": t.array(
                t.proxy(renames["GoogleCloudApigeeV1StatsHostStatsIn"])
            ).optional(),
            "metaData": t.proxy(renames["GoogleCloudApigeeV1MetadataIn"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1StatsIn"])
    types["GoogleCloudApigeeV1StatsOut"] = t.struct(
        {
            "environments": t.array(
                t.proxy(renames["GoogleCloudApigeeV1StatsEnvironmentStatsOut"])
            ).optional(),
            "hosts": t.array(
                t.proxy(renames["GoogleCloudApigeeV1StatsHostStatsOut"])
            ).optional(),
            "metaData": t.proxy(renames["GoogleCloudApigeeV1MetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1StatsOut"])
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
    types["GoogleCloudApigeeV1DeleteCustomReportResponseIn"] = t.struct(
        {"message": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1DeleteCustomReportResponseIn"])
    types["GoogleCloudApigeeV1DeleteCustomReportResponseOut"] = t.struct(
        {
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeleteCustomReportResponseOut"])
    types["GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentIn"] = t.struct(
        {
            "environment": t.string().optional(),
            "revision": t.string().optional(),
            "apiProxy": t.string().optional(),
            "basepath": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentIn"])
    types["GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "revision": t.string().optional(),
            "apiProxy": t.string().optional(),
            "basepath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeploymentChangeReportRoutingDeploymentOut"])
    types["GoogleCloudApigeeV1ListSecurityIncidentsResponseIn"] = t.struct(
        {
            "securityIncidents": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SecurityIncidentIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListSecurityIncidentsResponseIn"])
    types["GoogleCloudApigeeV1ListSecurityIncidentsResponseOut"] = t.struct(
        {
            "securityIncidents": t.array(
                t.proxy(renames["GoogleCloudApigeeV1SecurityIncidentOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ListSecurityIncidentsResponseOut"])
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
    types["GoogleCloudApigeeV1OperationConfigIn"] = t.struct(
        {
            "quota": t.proxy(renames["GoogleCloudApigeeV1QuotaIn"]).optional(),
            "apiSource": t.string(),
            "operations": t.array(
                t.proxy(renames["GoogleCloudApigeeV1OperationIn"])
            ).optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OperationConfigIn"])
    types["GoogleCloudApigeeV1OperationConfigOut"] = t.struct(
        {
            "quota": t.proxy(renames["GoogleCloudApigeeV1QuotaOut"]).optional(),
            "apiSource": t.string(),
            "operations": t.array(
                t.proxy(renames["GoogleCloudApigeeV1OperationOut"])
            ).optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OperationConfigOut"])
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
    types["GoogleCloudApigeeV1AdjustDeveloperBalanceRequestIn"] = t.struct(
        {"adjustment": t.proxy(renames["GoogleTypeMoneyIn"]).optional()}
    ).named(renames["GoogleCloudApigeeV1AdjustDeveloperBalanceRequestIn"])
    types["GoogleCloudApigeeV1AdjustDeveloperBalanceRequestOut"] = t.struct(
        {
            "adjustment": t.proxy(renames["GoogleTypeMoneyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AdjustDeveloperBalanceRequestOut"])
    types["GoogleCloudApigeeV1CanaryEvaluationIn"] = t.struct(
        {
            "metricLabels": t.proxy(
                renames["GoogleCloudApigeeV1CanaryEvaluationMetricLabelsIn"]
            ),
            "endTime": t.string(),
            "control": t.string(),
            "startTime": t.string(),
            "treatment": t.string(),
        }
    ).named(renames["GoogleCloudApigeeV1CanaryEvaluationIn"])
    types["GoogleCloudApigeeV1CanaryEvaluationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "metricLabels": t.proxy(
                renames["GoogleCloudApigeeV1CanaryEvaluationMetricLabelsOut"]
            ),
            "endTime": t.string(),
            "verdict": t.string().optional(),
            "control": t.string(),
            "startTime": t.string(),
            "treatment": t.string(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1CanaryEvaluationOut"])
    types["GoogleCloudApigeeV1AsyncQueryIn"] = t.struct(
        {
            "result": t.proxy(
                renames["GoogleCloudApigeeV1AsyncQueryResultIn"]
            ).optional(),
            "resultFileSize": t.string().optional(),
            "envgroupHostname": t.string().optional(),
            "reportDefinitionId": t.string().optional(),
            "self": t.string().optional(),
            "error": t.string().optional(),
            "name": t.string().optional(),
            "created": t.string().optional(),
            "updated": t.string().optional(),
            "resultRows": t.string().optional(),
            "executionTime": t.string().optional(),
            "state": t.string().optional(),
            "queryParams": t.proxy(
                renames["GoogleCloudApigeeV1QueryMetadataIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AsyncQueryIn"])
    types["GoogleCloudApigeeV1AsyncQueryOut"] = t.struct(
        {
            "result": t.proxy(
                renames["GoogleCloudApigeeV1AsyncQueryResultOut"]
            ).optional(),
            "resultFileSize": t.string().optional(),
            "envgroupHostname": t.string().optional(),
            "reportDefinitionId": t.string().optional(),
            "self": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "created": t.string().optional(),
            "updated": t.string().optional(),
            "resultRows": t.string().optional(),
            "executionTime": t.string().optional(),
            "state": t.string().optional(),
            "queryParams": t.proxy(
                renames["GoogleCloudApigeeV1QueryMetadataOut"]
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1AsyncQueryOut"])
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
    types["GoogleCloudApigeeV1RoutingRuleIn"] = t.struct(
        {
            "receiver": t.string().optional(),
            "basepath": t.string().optional(),
            "envGroupRevision": t.string().optional(),
            "otherTargets": t.array(t.string()).optional(),
            "deploymentGroup": t.string().optional(),
            "updateTime": t.string().optional(),
            "environment": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RoutingRuleIn"])
    types["GoogleCloudApigeeV1RoutingRuleOut"] = t.struct(
        {
            "receiver": t.string().optional(),
            "basepath": t.string().optional(),
            "envGroupRevision": t.string().optional(),
            "otherTargets": t.array(t.string()).optional(),
            "deploymentGroup": t.string().optional(),
            "updateTime": t.string().optional(),
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1RoutingRuleOut"])
    types["GoogleCloudApigeeV1DeveloperSubscriptionIn"] = t.struct(
        {
            "apiproduct": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeveloperSubscriptionIn"])
    types["GoogleCloudApigeeV1DeveloperSubscriptionOut"] = t.struct(
        {
            "createdAt": t.string().optional(),
            "apiproduct": t.string().optional(),
            "name": t.string().optional(),
            "startTime": t.string().optional(),
            "lastModifiedAt": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeveloperSubscriptionOut"])
    types["GoogleCloudApigeeV1ComputeEnvironmentScoresRequestIn"] = t.struct(
        {
            "timeRange": t.proxy(renames["GoogleTypeIntervalIn"]),
            "pageSize": t.integer().optional(),
            "filters": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilterIn"
                    ]
                )
            ).optional(),
            "pageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ComputeEnvironmentScoresRequestIn"])
    types["GoogleCloudApigeeV1ComputeEnvironmentScoresRequestOut"] = t.struct(
        {
            "timeRange": t.proxy(renames["GoogleTypeIntervalOut"]),
            "pageSize": t.integer().optional(),
            "filters": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilterOut"
                    ]
                )
            ).optional(),
            "pageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ComputeEnvironmentScoresRequestOut"])
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
    types["GoogleCloudApigeeV1ScoreComponentRecommendationIn"] = t.struct(
        {
            "actions": t.array(
                t.proxy(
                    renames["GoogleCloudApigeeV1ScoreComponentRecommendationActionIn"]
                )
            ).optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "impact": t.integer().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ScoreComponentRecommendationIn"])
    types["GoogleCloudApigeeV1ScoreComponentRecommendationOut"] = t.struct(
        {
            "actions": t.array(
                t.proxy(
                    renames["GoogleCloudApigeeV1ScoreComponentRecommendationActionOut"]
                )
            ).optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "impact": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ScoreComponentRecommendationOut"])
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
    types["GoogleCloudApigeeV1ProvisionOrganizationRequestIn"] = t.struct(
        {
            "runtimeLocation": t.string().optional(),
            "analyticsRegion": t.string().optional(),
            "authorizedNetwork": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ProvisionOrganizationRequestIn"])
    types["GoogleCloudApigeeV1ProvisionOrganizationRequestOut"] = t.struct(
        {
            "runtimeLocation": t.string().optional(),
            "analyticsRegion": t.string().optional(),
            "authorizedNetwork": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ProvisionOrganizationRequestOut"])
    types["GoogleCloudApigeeV1SchemaSchemaPropertyIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "type": t.string().optional(),
            "custom": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SchemaSchemaPropertyIn"])
    types["GoogleCloudApigeeV1SchemaSchemaPropertyOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "type": t.string().optional(),
            "custom": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SchemaSchemaPropertyOut"])
    types["GoogleCloudApigeeV1SetAddonsRequestIn"] = t.struct(
        {"addonsConfig": t.proxy(renames["GoogleCloudApigeeV1AddonsConfigIn"])}
    ).named(renames["GoogleCloudApigeeV1SetAddonsRequestIn"])
    types["GoogleCloudApigeeV1SetAddonsRequestOut"] = t.struct(
        {
            "addonsConfig": t.proxy(renames["GoogleCloudApigeeV1AddonsConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1SetAddonsRequestOut"])
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
    types["GoogleCloudApigeeV1ExpireDeveloperSubscriptionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudApigeeV1ExpireDeveloperSubscriptionRequestIn"])
    types["GoogleCloudApigeeV1ExpireDeveloperSubscriptionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudApigeeV1ExpireDeveloperSubscriptionRequestOut"])
    types["GoogleCloudApigeeV1PodStatusIn"] = t.struct(
        {
            "statusCode": t.string().optional(),
            "podStatus": t.string().optional(),
            "deploymentTime": t.string().optional(),
            "deploymentStatusTime": t.string().optional(),
            "statusCodeDetails": t.string().optional(),
            "podName": t.string().optional(),
            "deploymentStatus": t.string().optional(),
            "appVersion": t.string().optional(),
            "podStatusTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1PodStatusIn"])
    types["GoogleCloudApigeeV1PodStatusOut"] = t.struct(
        {
            "statusCode": t.string().optional(),
            "podStatus": t.string().optional(),
            "deploymentTime": t.string().optional(),
            "deploymentStatusTime": t.string().optional(),
            "statusCodeDetails": t.string().optional(),
            "podName": t.string().optional(),
            "deploymentStatus": t.string().optional(),
            "appVersion": t.string().optional(),
            "podStatusTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1PodStatusOut"])
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
    types["GoogleCloudApigeeV1ApiSecurityRuntimeConfigIn"] = t.struct(
        {
            "name": t.string().optional(),
            "revisionId": t.string().optional(),
            "location": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "uid": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ApiSecurityRuntimeConfigIn"])
    types["GoogleCloudApigeeV1ApiSecurityRuntimeConfigOut"] = t.struct(
        {
            "name": t.string().optional(),
            "revisionId": t.string().optional(),
            "location": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ApiSecurityRuntimeConfigOut"])
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
    types["GoogleCloudApigeeV1OrganizationIn"] = t.struct(
        {
            "apiConsumerDataEncryptionKeyName": t.string().optional(),
            "customerName": t.string().optional(),
            "type": t.string().optional(),
            "attributes": t.array(t.string()).optional(),
            "properties": t.proxy(
                renames["GoogleCloudApigeeV1PropertiesIn"]
            ).optional(),
            "addonsConfig": t.proxy(
                renames["GoogleCloudApigeeV1AddonsConfigIn"]
            ).optional(),
            "portalDisabled": t.boolean().optional(),
            "controlPlaneEncryptionKeyName": t.string().optional(),
            "analyticsRegion": t.string(),
            "apiConsumerDataLocation": t.string().optional(),
            "description": t.string().optional(),
            "runtimeDatabaseEncryptionKeyName": t.string().optional(),
            "billingType": t.string().optional(),
            "displayName": t.string().optional(),
            "runtimeType": t.string(),
            "authorizedNetwork": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OrganizationIn"])
    types["GoogleCloudApigeeV1OrganizationOut"] = t.struct(
        {
            "apiConsumerDataEncryptionKeyName": t.string().optional(),
            "name": t.string().optional(),
            "customerName": t.string().optional(),
            "type": t.string().optional(),
            "lastModifiedAt": t.string().optional(),
            "attributes": t.array(t.string()).optional(),
            "state": t.string().optional(),
            "createdAt": t.string().optional(),
            "properties": t.proxy(
                renames["GoogleCloudApigeeV1PropertiesOut"]
            ).optional(),
            "caCertificate": t.string().optional(),
            "addonsConfig": t.proxy(
                renames["GoogleCloudApigeeV1AddonsConfigOut"]
            ).optional(),
            "portalDisabled": t.boolean().optional(),
            "controlPlaneEncryptionKeyName": t.string().optional(),
            "analyticsRegion": t.string(),
            "apiConsumerDataLocation": t.string().optional(),
            "description": t.string().optional(),
            "expiresAt": t.string().optional(),
            "subscriptionType": t.string().optional(),
            "runtimeDatabaseEncryptionKeyName": t.string().optional(),
            "projectId": t.string().optional(),
            "billingType": t.string().optional(),
            "displayName": t.string().optional(),
            "apigeeProjectId": t.string().optional(),
            "environments": t.array(t.string()).optional(),
            "runtimeType": t.string(),
            "authorizedNetwork": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1OrganizationOut"])
    types["GoogleCloudApigeeV1DeveloperAppKeyIn"] = t.struct(
        {
            "apiProducts": t.array(t.struct({"_": t.string().optional()})).optional(),
            "expiresAt": t.string().optional(),
            "expiresInSeconds": t.string().optional(),
            "issuedAt": t.string().optional(),
            "consumerSecret": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "consumerKey": t.string().optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeveloperAppKeyIn"])
    types["GoogleCloudApigeeV1DeveloperAppKeyOut"] = t.struct(
        {
            "apiProducts": t.array(t.struct({"_": t.string().optional()})).optional(),
            "expiresAt": t.string().optional(),
            "expiresInSeconds": t.string().optional(),
            "issuedAt": t.string().optional(),
            "consumerSecret": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "consumerKey": t.string().optional(),
            "attributes": t.array(
                t.proxy(renames["GoogleCloudApigeeV1AttributeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1DeveloperAppKeyOut"])
    types["GoogleCloudApigeeV1ReferenceIn"] = t.struct(
        {
            "refers": t.string(),
            "name": t.string(),
            "resourceType": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ReferenceIn"])
    types["GoogleCloudApigeeV1ReferenceOut"] = t.struct(
        {
            "refers": t.string(),
            "name": t.string(),
            "resourceType": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudApigeeV1ReferenceOut"])

    functions = {}
    functions["hybridIssuersList"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ListHybridIssuersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsProvisionOrganization"] = apigee.post(
        "v1/{project}:provisionOrganization",
        t.struct(
            {
                "project": t.string(),
                "runtimeLocation": t.string().optional(),
                "analyticsRegion": t.string().optional(),
                "authorizedNetwork": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGetProjectMapping"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1RuntimeConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGet"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1RuntimeConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDelete"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1RuntimeConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsCreate"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1RuntimeConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsList"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1RuntimeConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGetSyncAuthorization"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1RuntimeConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGetDeployedIngressConfig"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1RuntimeConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSetAddons"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1RuntimeConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSetSyncAuthorization"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1RuntimeConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsUpdate"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1RuntimeConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGetRuntimeConfig"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1RuntimeConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvgroupsGet"] = apigee.post(
        "v1/{parent}/envgroups",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "hostnames": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvgroupsDelete"] = apigee.post(
        "v1/{parent}/envgroups",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "hostnames": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvgroupsGetDeployedIngressConfig"] = apigee.post(
        "v1/{parent}/envgroups",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "hostnames": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvgroupsPatch"] = apigee.post(
        "v1/{parent}/envgroups",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "hostnames": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvgroupsList"] = apigee.post(
        "v1/{parent}/envgroups",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "hostnames": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvgroupsCreate"] = apigee.post(
        "v1/{parent}/envgroups",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "hostnames": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvgroupsAttachmentsList"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1EnvironmentGroupAttachmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvgroupsAttachmentsDelete"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1EnvironmentGroupAttachmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvgroupsAttachmentsCreate"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1EnvironmentGroupAttachmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvgroupsAttachmentsGet"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1EnvironmentGroupAttachmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsHostStatsGet"] = apigee.get(
        "v1/{name}",
        t.struct(
            {
                "tzo": t.string().optional(),
                "sort": t.string().optional(),
                "select": t.string().optional(),
                "sortby": t.string().optional(),
                "topk": t.string().optional(),
                "limit": t.string().optional(),
                "filter": t.string().optional(),
                "envgroupHostname": t.string(),
                "realtime": t.boolean().optional(),
                "tsAscending": t.boolean().optional(),
                "timeUnit": t.string().optional(),
                "name": t.string(),
                "timeRange": t.string().optional(),
                "accuracy": t.string().optional(),
                "offset": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1StatsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAttributes"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersGetBalance"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersCreate"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersGetMonetizationConfig"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersList"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersUpdateMonetizationConfig"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersGet"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersUpdate"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersSetDeveloperStatus"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersDelete"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsAttributes"] = apigee.get(
        "v1/{parent}/apps",
        t.struct(
            {
                "startKey": t.string().optional(),
                "count": t.string().optional(),
                "shallowExpand": t.boolean().optional(),
                "expand": t.boolean().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListDeveloperAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsGet"] = apigee.get(
        "v1/{parent}/apps",
        t.struct(
            {
                "startKey": t.string().optional(),
                "count": t.string().optional(),
                "shallowExpand": t.boolean().optional(),
                "expand": t.boolean().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListDeveloperAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsCreate"] = apigee.get(
        "v1/{parent}/apps",
        t.struct(
            {
                "startKey": t.string().optional(),
                "count": t.string().optional(),
                "shallowExpand": t.boolean().optional(),
                "expand": t.boolean().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListDeveloperAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsDevelopersAppsGenerateKeyPairOrUpdateDeveloperAppStatus"
    ] = apigee.get(
        "v1/{parent}/apps",
        t.struct(
            {
                "startKey": t.string().optional(),
                "count": t.string().optional(),
                "shallowExpand": t.boolean().optional(),
                "expand": t.boolean().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListDeveloperAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsDelete"] = apigee.get(
        "v1/{parent}/apps",
        t.struct(
            {
                "startKey": t.string().optional(),
                "count": t.string().optional(),
                "shallowExpand": t.boolean().optional(),
                "expand": t.boolean().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListDeveloperAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsUpdate"] = apigee.get(
        "v1/{parent}/apps",
        t.struct(
            {
                "startKey": t.string().optional(),
                "count": t.string().optional(),
                "shallowExpand": t.boolean().optional(),
                "expand": t.boolean().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListDeveloperAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsList"] = apigee.get(
        "v1/{parent}/apps",
        t.struct(
            {
                "startKey": t.string().optional(),
                "count": t.string().optional(),
                "shallowExpand": t.boolean().optional(),
                "expand": t.boolean().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListDeveloperAppsResponseOut"]),
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
    functions[
        "organizationsDevelopersAppsAttributesUpdateDeveloperAppAttribute"
    ] = apigee.get(
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
    functions["organizationsDevelopersAppsKeysDelete"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperAppKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsKeysReplaceDeveloperAppKey"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperAppKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsKeysCreate"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperAppKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsKeysUpdateDeveloperAppKey"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperAppKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsKeysGet"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperAppKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersAppsKeysCreateCreate"] = apigee.post(
        "v1/{parent}/keys/create",
        t.struct(
            {
                "parent": t.string().optional(),
                "apiProducts": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "expiresAt": t.string().optional(),
                "expiresInSeconds": t.string().optional(),
                "issuedAt": t.string().optional(),
                "consumerSecret": t.string().optional(),
                "scopes": t.array(t.string()).optional(),
                "status": t.string().optional(),
                "consumerKey": t.string().optional(),
                "attributes": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1AttributeIn"])
                ).optional(),
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
    functions["organizationsDevelopersSubscriptionsList"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperSubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersSubscriptionsExpire"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperSubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersSubscriptionsCreate"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperSubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersSubscriptionsGet"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperSubscriptionOut"]),
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
    functions["organizationsDevelopersBalanceAdjust"] = apigee.post(
        "v1/{name}:credit",
        t.struct(
            {
                "name": t.string(),
                "transactionAmount": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
                "transactionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperBalanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDevelopersBalanceCredit"] = apigee.post(
        "v1/{name}:credit",
        t.struct(
            {
                "name": t.string(),
                "transactionAmount": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
                "transactionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeveloperBalanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsHostQueriesGetResult"] = apigee.get(
        "v1/{parent}/hostQueries",
        t.struct(
            {
                "dataset": t.string().optional(),
                "submittedBy": t.string().optional(),
                "parent": t.string(),
                "from": t.string().optional(),
                "to": t.string().optional(),
                "status": t.string().optional(),
                "inclQueriesWithoutReport": t.string().optional(),
                "envgroupHostname": t.string(),
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
                "dataset": t.string().optional(),
                "submittedBy": t.string().optional(),
                "parent": t.string(),
                "from": t.string().optional(),
                "to": t.string().optional(),
                "status": t.string().optional(),
                "inclQueriesWithoutReport": t.string().optional(),
                "envgroupHostname": t.string(),
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
                "dataset": t.string().optional(),
                "submittedBy": t.string().optional(),
                "parent": t.string(),
                "from": t.string().optional(),
                "to": t.string().optional(),
                "status": t.string().optional(),
                "inclQueriesWithoutReport": t.string().optional(),
                "envgroupHostname": t.string(),
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
                "dataset": t.string().optional(),
                "submittedBy": t.string().optional(),
                "parent": t.string(),
                "from": t.string().optional(),
                "to": t.string().optional(),
                "status": t.string().optional(),
                "inclQueriesWithoutReport": t.string().optional(),
                "envgroupHostname": t.string(),
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
                "dataset": t.string().optional(),
                "submittedBy": t.string().optional(),
                "parent": t.string(),
                "from": t.string().optional(),
                "to": t.string().optional(),
                "status": t.string().optional(),
                "inclQueriesWithoutReport": t.string().optional(),
                "envgroupHostname": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListAsyncQueriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAppsGet"] = apigee.get(
        "v1/{parent}/apps",
        t.struct(
            {
                "rows": t.string().optional(),
                "parent": t.string(),
                "status": t.string().optional(),
                "keyStatus": t.string().optional(),
                "startKey": t.string().optional(),
                "includeCred": t.boolean().optional(),
                "apiProduct": t.string().optional(),
                "apptype": t.string().optional(),
                "expand": t.boolean().optional(),
                "ids": t.string().optional(),
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
                "rows": t.string().optional(),
                "parent": t.string(),
                "status": t.string().optional(),
                "keyStatus": t.string().optional(),
                "startKey": t.string().optional(),
                "includeCred": t.boolean().optional(),
                "apiProduct": t.string().optional(),
                "apptype": t.string().optional(),
                "expand": t.boolean().optional(),
                "ids": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisGet"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ApiProxyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisList"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ApiProxyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisPatch"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ApiProxyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisCreate"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ApiProxyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisDelete"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ApiProxyOut"]),
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
    functions["organizationsApisKeyvaluemapsEntriesList"] = apigee.post(
        "v1/{parent}/entries",
        t.struct(
            {
                "parent": t.string(),
                "value": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1KeyValueEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisKeyvaluemapsEntriesGet"] = apigee.post(
        "v1/{parent}/entries",
        t.struct(
            {
                "parent": t.string(),
                "value": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1KeyValueEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisKeyvaluemapsEntriesDelete"] = apigee.post(
        "v1/{parent}/entries",
        t.struct(
            {
                "parent": t.string(),
                "value": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1KeyValueEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisKeyvaluemapsEntriesCreate"] = apigee.post(
        "v1/{parent}/entries",
        t.struct(
            {
                "parent": t.string(),
                "value": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1KeyValueEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisRevisionsGet"] = apigee.post(
        "v1/{name}",
        t.struct(
            {
                "validate": t.boolean().optional(),
                "name": t.string(),
                "data": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ApiProxyRevisionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisRevisionsDelete"] = apigee.post(
        "v1/{name}",
        t.struct(
            {
                "validate": t.boolean().optional(),
                "name": t.string(),
                "data": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ApiProxyRevisionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApisRevisionsUpdateApiProxyRevision"] = apigee.post(
        "v1/{name}",
        t.struct(
            {
                "validate": t.boolean().optional(),
                "name": t.string(),
                "data": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ApiProxyRevisionOut"]),
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
    functions["organizationsSharedflowsCreate"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1SharedFlowOut"]),
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
    functions["organizationsSharedflowsGet"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1SharedFlowOut"]),
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
    functions["organizationsSharedflowsRevisionsDelete"] = apigee.post(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "validate": t.boolean().optional(),
                "data": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1SharedFlowRevisionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSharedflowsRevisionsGet"] = apigee.post(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "validate": t.boolean().optional(),
                "data": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1SharedFlowRevisionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsSharedflowsRevisionsUpdateSharedFlowRevision"
    ] = apigee.post(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "validate": t.boolean().optional(),
                "data": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1SharedFlowRevisionOut"]),
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
    functions["organizationsEndpointAttachmentsGet"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEndpointAttachmentsList"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEndpointAttachmentsCreate"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEndpointAttachmentsDelete"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
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
    functions["organizationsHostSecurityReportsCreate"] = apigee.get(
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
    functions["organizationsInstancesPatch"] = apigee.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string(),
                "peeringCidrRange": t.string().optional(),
                "consumerAcceptList": t.array(t.string()).optional(),
                "location": t.string(),
                "displayName": t.string().optional(),
                "diskEncryptionKeyName": t.string().optional(),
                "ipRange": t.string().optional(),
                "description": t.string().optional(),
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
                "name": t.string(),
                "peeringCidrRange": t.string().optional(),
                "consumerAcceptList": t.array(t.string()).optional(),
                "location": t.string(),
                "displayName": t.string().optional(),
                "diskEncryptionKeyName": t.string().optional(),
                "ipRange": t.string().optional(),
                "description": t.string().optional(),
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
                "name": t.string(),
                "peeringCidrRange": t.string().optional(),
                "consumerAcceptList": t.array(t.string()).optional(),
                "location": t.string(),
                "displayName": t.string().optional(),
                "diskEncryptionKeyName": t.string().optional(),
                "ipRange": t.string().optional(),
                "description": t.string().optional(),
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
                "name": t.string(),
                "peeringCidrRange": t.string().optional(),
                "consumerAcceptList": t.array(t.string()).optional(),
                "location": t.string(),
                "displayName": t.string().optional(),
                "diskEncryptionKeyName": t.string().optional(),
                "ipRange": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesDelete"] = apigee.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string(),
                "peeringCidrRange": t.string().optional(),
                "consumerAcceptList": t.array(t.string()).optional(),
                "location": t.string(),
                "displayName": t.string().optional(),
                "diskEncryptionKeyName": t.string().optional(),
                "ipRange": t.string().optional(),
                "description": t.string().optional(),
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
                "name": t.string(),
                "peeringCidrRange": t.string().optional(),
                "consumerAcceptList": t.array(t.string()).optional(),
                "location": t.string(),
                "displayName": t.string().optional(),
                "diskEncryptionKeyName": t.string().optional(),
                "ipRange": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesCanaryevaluationsGet"] = apigee.post(
        "v1/{parent}/canaryevaluations",
        t.struct(
            {
                "parent": t.string(),
                "metricLabels": t.proxy(
                    renames["GoogleCloudApigeeV1CanaryEvaluationMetricLabelsIn"]
                ),
                "endTime": t.string(),
                "control": t.string(),
                "startTime": t.string(),
                "treatment": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesCanaryevaluationsCreate"] = apigee.post(
        "v1/{parent}/canaryevaluations",
        t.struct(
            {
                "parent": t.string(),
                "metricLabels": t.proxy(
                    renames["GoogleCloudApigeeV1CanaryEvaluationMetricLabelsIn"]
                ),
                "endTime": t.string(),
                "control": t.string(),
                "startTime": t.string(),
                "treatment": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesNatAddressesGet"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesNatAddressesList"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesNatAddressesCreate"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesNatAddressesActivate"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesNatAddressesDelete"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesAttachmentsCreate"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1InstanceAttachmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesAttachmentsList"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1InstanceAttachmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesAttachmentsDelete"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1InstanceAttachmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInstancesAttachmentsGet"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1InstanceAttachmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsOptimizedHostStatsGet"] = apigee.get(
        "v1/{name}",
        t.struct(
            {
                "timeUnit": t.string().optional(),
                "limit": t.string().optional(),
                "realtime": t.boolean().optional(),
                "name": t.string(),
                "offset": t.string().optional(),
                "tzo": t.string().optional(),
                "sort": t.string().optional(),
                "envgroupHostname": t.string(),
                "timeRange": t.string(),
                "sortby": t.string().optional(),
                "accuracy": t.string().optional(),
                "topk": t.string().optional(),
                "filter": t.string().optional(),
                "select": t.string(),
                "tsAscending": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1OptimizedStatsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSecurityProfilesList"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1SecurityProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSecurityProfilesListRevisions"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1SecurityProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSecurityProfilesGet"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1SecurityProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSecurityProfilesEnvironmentsCreate"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsSecurityProfilesEnvironmentsComputeEnvironmentScores"
    ] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSecurityProfilesEnvironmentsDelete"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSitesApicategoriesDelete"] = apigee.get(
        "v1/{parent}/apicategories",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ListApiCategoriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSitesApicategoriesCreate"] = apigee.get(
        "v1/{parent}/apicategories",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ListApiCategoriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSitesApicategoriesGet"] = apigee.get(
        "v1/{parent}/apicategories",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ListApiCategoriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSitesApicategoriesPatch"] = apigee.get(
        "v1/{parent}/apicategories",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ListApiCategoriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSitesApicategoriesList"] = apigee.get(
        "v1/{parent}/apicategories",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ListApiCategoriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDatacollectorsCreate"] = apigee.get(
        "v1/{parent}/datacollectors",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListDataCollectorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDatacollectorsGet"] = apigee.get(
        "v1/{parent}/datacollectors",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListDataCollectorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDatacollectorsDelete"] = apigee.get(
        "v1/{parent}/datacollectors",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListDataCollectorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDatacollectorsPatch"] = apigee.get(
        "v1/{parent}/datacollectors",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListDataCollectorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDatacollectorsList"] = apigee.get(
        "v1/{parent}/datacollectors",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListDataCollectorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsOperationsGet"] = apigee.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsAttributes"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ApiProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsCreate"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ApiProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsList"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ApiProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsUpdate"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ApiProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsGet"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ApiProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsDelete"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ApiProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsApiproductsAttributesUpdateApiProductAttribute"
    ] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1AttributeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsAttributesList"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1AttributeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsAttributesGet"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1AttributeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsAttributesDelete"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1AttributeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsRateplansDelete"] = apigee.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "revenueShareRates": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1RevenueShareRangeIn"])
                ).optional(),
                "revenueShareType": t.string().optional(),
                "fixedRecurringFee": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
                "paymentFundingModel": t.string().optional(),
                "fixedFeeFrequency": t.integer().optional(),
                "currencyCode": t.string().optional(),
                "consumptionPricingType": t.string().optional(),
                "startTime": t.string().optional(),
                "setupFee": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
                "state": t.string().optional(),
                "displayName": t.string().optional(),
                "billingPeriod": t.string().optional(),
                "apiproduct": t.string().optional(),
                "description": t.string().optional(),
                "endTime": t.string().optional(),
                "consumptionPricingRates": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1RateRangeIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1RatePlanOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsRateplansCreate"] = apigee.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "revenueShareRates": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1RevenueShareRangeIn"])
                ).optional(),
                "revenueShareType": t.string().optional(),
                "fixedRecurringFee": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
                "paymentFundingModel": t.string().optional(),
                "fixedFeeFrequency": t.integer().optional(),
                "currencyCode": t.string().optional(),
                "consumptionPricingType": t.string().optional(),
                "startTime": t.string().optional(),
                "setupFee": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
                "state": t.string().optional(),
                "displayName": t.string().optional(),
                "billingPeriod": t.string().optional(),
                "apiproduct": t.string().optional(),
                "description": t.string().optional(),
                "endTime": t.string().optional(),
                "consumptionPricingRates": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1RateRangeIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1RatePlanOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsRateplansList"] = apigee.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "revenueShareRates": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1RevenueShareRangeIn"])
                ).optional(),
                "revenueShareType": t.string().optional(),
                "fixedRecurringFee": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
                "paymentFundingModel": t.string().optional(),
                "fixedFeeFrequency": t.integer().optional(),
                "currencyCode": t.string().optional(),
                "consumptionPricingType": t.string().optional(),
                "startTime": t.string().optional(),
                "setupFee": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
                "state": t.string().optional(),
                "displayName": t.string().optional(),
                "billingPeriod": t.string().optional(),
                "apiproduct": t.string().optional(),
                "description": t.string().optional(),
                "endTime": t.string().optional(),
                "consumptionPricingRates": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1RateRangeIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1RatePlanOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsRateplansGet"] = apigee.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "revenueShareRates": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1RevenueShareRangeIn"])
                ).optional(),
                "revenueShareType": t.string().optional(),
                "fixedRecurringFee": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
                "paymentFundingModel": t.string().optional(),
                "fixedFeeFrequency": t.integer().optional(),
                "currencyCode": t.string().optional(),
                "consumptionPricingType": t.string().optional(),
                "startTime": t.string().optional(),
                "setupFee": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
                "state": t.string().optional(),
                "displayName": t.string().optional(),
                "billingPeriod": t.string().optional(),
                "apiproduct": t.string().optional(),
                "description": t.string().optional(),
                "endTime": t.string().optional(),
                "consumptionPricingRates": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1RateRangeIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1RatePlanOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsApiproductsRateplansUpdate"] = apigee.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "revenueShareRates": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1RevenueShareRangeIn"])
                ).optional(),
                "revenueShareType": t.string().optional(),
                "fixedRecurringFee": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
                "paymentFundingModel": t.string().optional(),
                "fixedFeeFrequency": t.integer().optional(),
                "currencyCode": t.string().optional(),
                "consumptionPricingType": t.string().optional(),
                "startTime": t.string().optional(),
                "setupFee": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
                "state": t.string().optional(),
                "displayName": t.string().optional(),
                "billingPeriod": t.string().optional(),
                "apiproduct": t.string().optional(),
                "description": t.string().optional(),
                "endTime": t.string().optional(),
                "consumptionPricingRates": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1RateRangeIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1RatePlanOut"]),
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
    functions["organizationsReportsGet"] = apigee.post(
        "v1/{parent}/reports",
        t.struct(
            {
                "parent": t.string(),
                "dimensions": t.array(t.string()).optional(),
                "sortByCols": t.array(t.string()).optional(),
                "sortOrder": t.string().optional(),
                "chartType": t.string().optional(),
                "toTime": t.string().optional(),
                "timeUnit": t.string().optional(),
                "filter": t.string().optional(),
                "fromTime": t.string().optional(),
                "properties": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1ReportPropertyIn"])
                ).optional(),
                "offset": t.string().optional(),
                "displayName": t.string().optional(),
                "limit": t.string().optional(),
                "metrics": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1CustomReportMetricIn"])
                ),
                "name": t.string(),
                "tags": t.array(t.string()).optional(),
                "topk": t.string().optional(),
                "comments": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1CustomReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsReportsList"] = apigee.post(
        "v1/{parent}/reports",
        t.struct(
            {
                "parent": t.string(),
                "dimensions": t.array(t.string()).optional(),
                "sortByCols": t.array(t.string()).optional(),
                "sortOrder": t.string().optional(),
                "chartType": t.string().optional(),
                "toTime": t.string().optional(),
                "timeUnit": t.string().optional(),
                "filter": t.string().optional(),
                "fromTime": t.string().optional(),
                "properties": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1ReportPropertyIn"])
                ).optional(),
                "offset": t.string().optional(),
                "displayName": t.string().optional(),
                "limit": t.string().optional(),
                "metrics": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1CustomReportMetricIn"])
                ),
                "name": t.string(),
                "tags": t.array(t.string()).optional(),
                "topk": t.string().optional(),
                "comments": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1CustomReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsReportsDelete"] = apigee.post(
        "v1/{parent}/reports",
        t.struct(
            {
                "parent": t.string(),
                "dimensions": t.array(t.string()).optional(),
                "sortByCols": t.array(t.string()).optional(),
                "sortOrder": t.string().optional(),
                "chartType": t.string().optional(),
                "toTime": t.string().optional(),
                "timeUnit": t.string().optional(),
                "filter": t.string().optional(),
                "fromTime": t.string().optional(),
                "properties": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1ReportPropertyIn"])
                ).optional(),
                "offset": t.string().optional(),
                "displayName": t.string().optional(),
                "limit": t.string().optional(),
                "metrics": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1CustomReportMetricIn"])
                ),
                "name": t.string(),
                "tags": t.array(t.string()).optional(),
                "topk": t.string().optional(),
                "comments": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1CustomReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsReportsUpdate"] = apigee.post(
        "v1/{parent}/reports",
        t.struct(
            {
                "parent": t.string(),
                "dimensions": t.array(t.string()).optional(),
                "sortByCols": t.array(t.string()).optional(),
                "sortOrder": t.string().optional(),
                "chartType": t.string().optional(),
                "toTime": t.string().optional(),
                "timeUnit": t.string().optional(),
                "filter": t.string().optional(),
                "fromTime": t.string().optional(),
                "properties": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1ReportPropertyIn"])
                ).optional(),
                "offset": t.string().optional(),
                "displayName": t.string().optional(),
                "limit": t.string().optional(),
                "metrics": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1CustomReportMetricIn"])
                ),
                "name": t.string(),
                "tags": t.array(t.string()).optional(),
                "topk": t.string().optional(),
                "comments": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1CustomReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsReportsCreate"] = apigee.post(
        "v1/{parent}/reports",
        t.struct(
            {
                "parent": t.string(),
                "dimensions": t.array(t.string()).optional(),
                "sortByCols": t.array(t.string()).optional(),
                "sortOrder": t.string().optional(),
                "chartType": t.string().optional(),
                "toTime": t.string().optional(),
                "timeUnit": t.string().optional(),
                "filter": t.string().optional(),
                "fromTime": t.string().optional(),
                "properties": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1ReportPropertyIn"])
                ).optional(),
                "offset": t.string().optional(),
                "displayName": t.string().optional(),
                "limit": t.string().optional(),
                "metrics": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1CustomReportMetricIn"])
                ),
                "name": t.string(),
                "tags": t.array(t.string()).optional(),
                "topk": t.string().optional(),
                "comments": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1CustomReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsGet"] = apigee.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsGetDebugmask"] = apigee.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsModifyEnvironment"] = apigee.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsGetIamPolicy"] = apigee.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsUpdateTraceConfig"] = apigee.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsUpdate"] = apigee.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsCreate"] = apigee.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsSubscribe"] = apigee.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsUnsubscribe"] = apigee.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsGetApiSecurityRuntimeConfig"] = apigee.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsUpdateDebugmask"] = apigee.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsUpdateEnvironment"] = apigee.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsGetDeployedConfig"] = apigee.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsSetIamPolicy"] = apigee.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsGetTraceConfig"] = apigee.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsDelete"] = apigee.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsTestIamPermissions"] = apigee.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsAnalyticsExportsGet"] = apigee.get(
        "v1/{parent}/analytics/exports",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ListExportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsAnalyticsExportsCreate"] = apigee.get(
        "v1/{parent}/analytics/exports",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ListExportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsAnalyticsExportsList"] = apigee.get(
        "v1/{parent}/analytics/exports",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ListExportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsAnalyticsAdminGetSchemav2"] = apigee.get(
        "v1/{name}",
        t.struct(
            {
                "disableCache": t.boolean().optional(),
                "type": t.string(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1SchemaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsKeyvaluemapsCreate"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1KeyValueMapOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsKeyvaluemapsDelete"] = apigee.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1KeyValueMapOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsKeyvaluemapsEntriesList"] = apigee.post(
        "v1/{parent}/entries",
        t.struct(
            {
                "parent": t.string(),
                "value": t.string(),
                "name": t.string().optional(),
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
                "value": t.string(),
                "name": t.string().optional(),
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
                "value": t.string(),
                "name": t.string().optional(),
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
                "value": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1KeyValueEntryOut"]),
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
    functions["organizationsEnvironmentsQueriesList"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1AsyncQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsQueriesGetResulturl"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1AsyncQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsQueriesGetResult"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1AsyncQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsQueriesCreate"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1AsyncQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsQueriesGet"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1AsyncQueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsResourcefilesGet"] = apigee.post(
        "v1/{parent}/resourcefiles",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string(),
                "type": t.string(),
                "data": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
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
                "parent": t.string(),
                "name": t.string(),
                "type": t.string(),
                "data": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
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
                "parent": t.string(),
                "name": t.string(),
                "type": t.string(),
                "data": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
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
                "parent": t.string(),
                "name": t.string(),
                "type": t.string(),
                "data": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ResourceFileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsEnvironmentsResourcefilesListEnvironmentResources"
    ] = apigee.post(
        "v1/{parent}/resourcefiles",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string(),
                "type": t.string(),
                "data": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
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
                "parent": t.string(),
                "name": t.string(),
                "type": t.string(),
                "data": t.string().optional(),
                "extensions": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "contentType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ResourceFileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsTraceConfigOverridesPatch"] = apigee.post(
        "v1/{parent}/overrides",
        t.struct(
            {
                "parent": t.string(),
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
    functions["organizationsEnvironmentsTraceConfigOverridesGet"] = apigee.post(
        "v1/{parent}/overrides",
        t.struct(
            {
                "parent": t.string(),
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
    functions["organizationsEnvironmentsTraceConfigOverridesList"] = apigee.post(
        "v1/{parent}/overrides",
        t.struct(
            {
                "parent": t.string(),
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
    functions["organizationsEnvironmentsTraceConfigOverridesDelete"] = apigee.post(
        "v1/{parent}/overrides",
        t.struct(
            {
                "parent": t.string(),
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
    functions["organizationsEnvironmentsTraceConfigOverridesCreate"] = apigee.post(
        "v1/{parent}/overrides",
        t.struct(
            {
                "parent": t.string(),
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
    functions["organizationsEnvironmentsOptimizedStatsGet"] = apigee.get(
        "v1/{name}",
        t.struct(
            {
                "select": t.string(),
                "tzo": t.string().optional(),
                "realtime": t.boolean().optional(),
                "topk": t.string().optional(),
                "limit": t.string().optional(),
                "accuracy": t.string().optional(),
                "filter": t.string().optional(),
                "sortby": t.string().optional(),
                "name": t.string(),
                "timeUnit": t.string().optional(),
                "aggTable": t.string().optional(),
                "timeRange": t.string(),
                "sonar": t.boolean().optional(),
                "offset": t.string().optional(),
                "tsAscending": t.boolean().optional(),
                "sort": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1OptimizedStatsOut"]),
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
                "name": t.string(),
                "override": t.boolean().optional(),
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
                "name": t.string(),
                "override": t.boolean().optional(),
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
                "name": t.string(),
                "override": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsDeploymentsList"] = apigee.get(
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
    functions["organizationsEnvironmentsSecurityStatsQueryTabularStats"] = apigee.post(
        "v1/{orgenv}/securityStats:queryTimeSeriesStats",
        t.struct(
            {
                "orgenv": t.string(),
                "timeRange": t.proxy(renames["GoogleTypeIntervalIn"]),
                "timestampOrder": t.string().optional(),
                "dimensions": t.array(t.string()).optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "metrics": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1MetricAggregationIn"])
                ),
                "pageSize": t.integer().optional(),
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
                "timeRange": t.proxy(renames["GoogleTypeIntervalIn"]),
                "timestampOrder": t.string().optional(),
                "dimensions": t.array(t.string()).optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "metrics": t.array(
                    t.proxy(renames["GoogleCloudApigeeV1MetricAggregationIn"])
                ),
                "pageSize": t.integer().optional(),
                "windowSize": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1QueryTimeSeriesStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsReferencesDelete"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ReferenceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsReferencesUpdate"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ReferenceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsReferencesCreate"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ReferenceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsReferencesGet"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1ReferenceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsApisRevisionsGetDeployments"] = apigee.delete(
        "v1/{name}/deployments",
        t.struct(
            {
                "name": t.string(),
                "sequencedRollout": t.boolean().optional(),
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
                "name": t.string(),
                "sequencedRollout": t.boolean().optional(),
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
                "name": t.string(),
                "sequencedRollout": t.boolean().optional(),
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
                "override": t.boolean().optional(),
                "name": t.string().optional(),
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
                "override": t.boolean().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1DeploymentChangeReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsApisRevisionsDebugsessionsCreate"] = apigee.get(
        "v1/{parent}/debugsessions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListDebugSessionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsEnvironmentsApisRevisionsDebugsessionsDeleteData"
    ] = apigee.get(
        "v1/{parent}/debugsessions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListDebugSessionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsApisRevisionsDebugsessionsGet"] = apigee.get(
        "v1/{parent}/debugsessions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListDebugSessionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsApisRevisionsDebugsessionsList"] = apigee.get(
        "v1/{parent}/debugsessions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListDebugSessionsResponseOut"]),
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
    functions["organizationsEnvironmentsKeystoresDelete"] = apigee.post(
        "v1/{parent}/keystores",
        t.struct(
            {"name": t.string(), "parent": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["GoogleCloudApigeeV1KeystoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsKeystoresGet"] = apigee.post(
        "v1/{parent}/keystores",
        t.struct(
            {"name": t.string(), "parent": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["GoogleCloudApigeeV1KeystoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsKeystoresCreate"] = apigee.post(
        "v1/{parent}/keystores",
        t.struct(
            {"name": t.string(), "parent": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["GoogleCloudApigeeV1KeystoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsKeystoresAliasesGet"] = apigee.get(
        "v1/{name}/certificate",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleApiHttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsKeystoresAliasesDelete"] = apigee.get(
        "v1/{name}/certificate",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleApiHttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsKeystoresAliasesCsr"] = apigee.get(
        "v1/{name}/certificate",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleApiHttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsKeystoresAliasesCreate"] = apigee.get(
        "v1/{name}/certificate",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleApiHttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsKeystoresAliasesUpdate"] = apigee.get(
        "v1/{name}/certificate",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleApiHttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsKeystoresAliasesGetCertificate"] = apigee.get(
        "v1/{name}/certificate",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleApiHttpBodyOut"]),
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
    functions[
        "organizationsEnvironmentsFlowhooksDetachSharedFlowFromFlowHook"
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
    functions["organizationsEnvironmentsSecurityIncidentsGet"] = apigee.get(
        "v1/{parent}/securityIncidents",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1ListSecurityIncidentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsTargetserversUpdate"] = apigee.post(
        "v1/{parent}/targetservers",
        t.struct(
            {
                "name": t.string(),
                "parent": t.string(),
                "sSLInfo": t.proxy(renames["GoogleCloudApigeeV1TlsInfoIn"]).optional(),
                "host": t.string(),
                "description": t.string().optional(),
                "port": t.integer(),
                "isEnabled": t.boolean().optional(),
                "protocol": t.string().optional(),
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
                "name": t.string(),
                "parent": t.string(),
                "sSLInfo": t.proxy(renames["GoogleCloudApigeeV1TlsInfoIn"]).optional(),
                "host": t.string(),
                "description": t.string().optional(),
                "port": t.integer(),
                "isEnabled": t.boolean().optional(),
                "protocol": t.string().optional(),
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
                "name": t.string(),
                "parent": t.string(),
                "sSLInfo": t.proxy(renames["GoogleCloudApigeeV1TlsInfoIn"]).optional(),
                "host": t.string(),
                "description": t.string().optional(),
                "port": t.integer(),
                "isEnabled": t.boolean().optional(),
                "protocol": t.string().optional(),
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
                "name": t.string(),
                "parent": t.string(),
                "sSLInfo": t.proxy(renames["GoogleCloudApigeeV1TlsInfoIn"]).optional(),
                "host": t.string(),
                "description": t.string().optional(),
                "port": t.integer(),
                "isEnabled": t.boolean().optional(),
                "protocol": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1TargetServerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsArchiveDeploymentsGet"] = apigee.post(
        "v1/{name}:generateDownloadUrl",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1GenerateDownloadUrlResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsArchiveDeploymentsCreate"] = apigee.post(
        "v1/{name}:generateDownloadUrl",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1GenerateDownloadUrlResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsEnvironmentsArchiveDeploymentsGenerateUploadUrl"
    ] = apigee.post(
        "v1/{name}:generateDownloadUrl",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1GenerateDownloadUrlResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsArchiveDeploymentsDelete"] = apigee.post(
        "v1/{name}:generateDownloadUrl",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1GenerateDownloadUrlResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsArchiveDeploymentsPatch"] = apigee.post(
        "v1/{name}:generateDownloadUrl",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1GenerateDownloadUrlResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsArchiveDeploymentsList"] = apigee.post(
        "v1/{name}:generateDownloadUrl",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1GenerateDownloadUrlResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsEnvironmentsArchiveDeploymentsGenerateDownloadUrl"
    ] = apigee.post(
        "v1/{name}:generateDownloadUrl",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1GenerateDownloadUrlResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsStatsGet"] = apigee.get(
        "v1/{name}",
        t.struct(
            {
                "tsAscending": t.boolean().optional(),
                "timeRange": t.string().optional(),
                "sortby": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string(),
                "aggTable": t.string().optional(),
                "realtime": t.boolean().optional(),
                "sort": t.string().optional(),
                "select": t.string().optional(),
                "limit": t.string().optional(),
                "topk": t.string().optional(),
                "accuracy": t.string().optional(),
                "tzo": t.string().optional(),
                "sonar": t.boolean().optional(),
                "offset": t.string().optional(),
                "timeUnit": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1StatsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsSecurityReportsList"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleApiHttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsSecurityReportsGetResultView"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleApiHttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsSecurityReportsGet"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleApiHttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsSecurityReportsCreate"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleApiHttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsEnvironmentsSecurityReportsGetResult"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleApiHttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsKeyvaluemapsDelete"] = apigee.post(
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
    functions["organizationsKeyvaluemapsCreate"] = apigee.post(
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
    functions["organizationsKeyvaluemapsEntriesDelete"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1KeyValueEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsKeyvaluemapsEntriesCreate"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1KeyValueEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsKeyvaluemapsEntriesList"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1KeyValueEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsKeyvaluemapsEntriesGet"] = apigee.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudApigeeV1KeyValueEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAnalyticsDatastoresCreate"] = apigee.post(
        "v1/{parent}/analytics/datastores:test",
        t.struct(
            {
                "parent": t.string(),
                "datastoreConfig": t.proxy(
                    renames["GoogleCloudApigeeV1DatastoreConfigIn"]
                ).optional(),
                "targetType": t.string().optional(),
                "displayName": t.string(),
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
                "datastoreConfig": t.proxy(
                    renames["GoogleCloudApigeeV1DatastoreConfigIn"]
                ).optional(),
                "targetType": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1TestDatastoreResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsAnalyticsDatastoresUpdate"] = apigee.post(
        "v1/{parent}/analytics/datastores:test",
        t.struct(
            {
                "parent": t.string(),
                "datastoreConfig": t.proxy(
                    renames["GoogleCloudApigeeV1DatastoreConfigIn"]
                ).optional(),
                "targetType": t.string().optional(),
                "displayName": t.string(),
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
                "datastoreConfig": t.proxy(
                    renames["GoogleCloudApigeeV1DatastoreConfigIn"]
                ).optional(),
                "targetType": t.string().optional(),
                "displayName": t.string(),
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
                "datastoreConfig": t.proxy(
                    renames["GoogleCloudApigeeV1DatastoreConfigIn"]
                ).optional(),
                "targetType": t.string().optional(),
                "displayName": t.string(),
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
                "datastoreConfig": t.proxy(
                    renames["GoogleCloudApigeeV1DatastoreConfigIn"]
                ).optional(),
                "targetType": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudApigeeV1TestDatastoreResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="apigee", renames=renames, types=types, functions=functions)
