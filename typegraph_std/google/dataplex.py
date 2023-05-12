from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_dataplex() -> Import:
    dataplex = HTTPRuntime("https://dataplex.googleapis.com/")

    renames = {
        "ErrorResponse": "_dataplex_1_ErrorResponse",
        "GoogleCloudDataplexV1TriggerIn": "_dataplex_2_GoogleCloudDataplexV1TriggerIn",
        "GoogleCloudDataplexV1TriggerOut": "_dataplex_3_GoogleCloudDataplexV1TriggerOut",
        "GoogleCloudDataplexV1DataProfileResultProfileIn": "_dataplex_4_GoogleCloudDataplexV1DataProfileResultProfileIn",
        "GoogleCloudDataplexV1DataProfileResultProfileOut": "_dataplex_5_GoogleCloudDataplexV1DataProfileResultProfileOut",
        "GoogleCloudDataplexV1EnvironmentEndpointsIn": "_dataplex_6_GoogleCloudDataplexV1EnvironmentEndpointsIn",
        "GoogleCloudDataplexV1EnvironmentEndpointsOut": "_dataplex_7_GoogleCloudDataplexV1EnvironmentEndpointsOut",
        "GoogleCloudDataplexV1StorageFormatIn": "_dataplex_8_GoogleCloudDataplexV1StorageFormatIn",
        "GoogleCloudDataplexV1StorageFormatOut": "_dataplex_9_GoogleCloudDataplexV1StorageFormatOut",
        "GoogleIamV1AuditConfigIn": "_dataplex_10_GoogleIamV1AuditConfigIn",
        "GoogleIamV1AuditConfigOut": "_dataplex_11_GoogleIamV1AuditConfigOut",
        "GoogleCloudDataplexV1DataQualityDimensionResultIn": "_dataplex_12_GoogleCloudDataplexV1DataQualityDimensionResultIn",
        "GoogleCloudDataplexV1DataQualityDimensionResultOut": "_dataplex_13_GoogleCloudDataplexV1DataQualityDimensionResultOut",
        "GoogleCloudDataplexV1StorageFormatCsvOptionsIn": "_dataplex_14_GoogleCloudDataplexV1StorageFormatCsvOptionsIn",
        "GoogleCloudDataplexV1StorageFormatCsvOptionsOut": "_dataplex_15_GoogleCloudDataplexV1StorageFormatCsvOptionsOut",
        "GoogleCloudDataplexV1TriggerOnDemandIn": "_dataplex_16_GoogleCloudDataplexV1TriggerOnDemandIn",
        "GoogleCloudDataplexV1TriggerOnDemandOut": "_dataplex_17_GoogleCloudDataplexV1TriggerOnDemandOut",
        "GoogleCloudDataplexV1EnvironmentInfrastructureSpecOsImageRuntimeIn": "_dataplex_18_GoogleCloudDataplexV1EnvironmentInfrastructureSpecOsImageRuntimeIn",
        "GoogleCloudDataplexV1EnvironmentInfrastructureSpecOsImageRuntimeOut": "_dataplex_19_GoogleCloudDataplexV1EnvironmentInfrastructureSpecOsImageRuntimeOut",
        "GoogleCloudDataplexV1TaskInfrastructureSpecVpcNetworkIn": "_dataplex_20_GoogleCloudDataplexV1TaskInfrastructureSpecVpcNetworkIn",
        "GoogleCloudDataplexV1TaskInfrastructureSpecVpcNetworkOut": "_dataplex_21_GoogleCloudDataplexV1TaskInfrastructureSpecVpcNetworkOut",
        "GoogleCloudDataplexV1DiscoveryEventIn": "_dataplex_22_GoogleCloudDataplexV1DiscoveryEventIn",
        "GoogleCloudDataplexV1DiscoveryEventOut": "_dataplex_23_GoogleCloudDataplexV1DiscoveryEventOut",
        "GoogleCloudDataplexV1EnvironmentSessionStatusIn": "_dataplex_24_GoogleCloudDataplexV1EnvironmentSessionStatusIn",
        "GoogleCloudDataplexV1EnvironmentSessionStatusOut": "_dataplex_25_GoogleCloudDataplexV1EnvironmentSessionStatusOut",
        "GoogleCloudDataplexV1DataQualityRuleRegexExpectationIn": "_dataplex_26_GoogleCloudDataplexV1DataQualityRuleRegexExpectationIn",
        "GoogleCloudDataplexV1DataQualityRuleRegexExpectationOut": "_dataplex_27_GoogleCloudDataplexV1DataQualityRuleRegexExpectationOut",
        "GoogleCloudDataplexV1RunDataScanResponseIn": "_dataplex_28_GoogleCloudDataplexV1RunDataScanResponseIn",
        "GoogleCloudDataplexV1RunDataScanResponseOut": "_dataplex_29_GoogleCloudDataplexV1RunDataScanResponseOut",
        "GoogleCloudDataplexV1DataScanEventDataQualityResultIn": "_dataplex_30_GoogleCloudDataplexV1DataScanEventDataQualityResultIn",
        "GoogleCloudDataplexV1DataScanEventDataQualityResultOut": "_dataplex_31_GoogleCloudDataplexV1DataScanEventDataQualityResultOut",
        "GoogleCloudDataplexV1ListContentResponseIn": "_dataplex_32_GoogleCloudDataplexV1ListContentResponseIn",
        "GoogleCloudDataplexV1ListContentResponseOut": "_dataplex_33_GoogleCloudDataplexV1ListContentResponseOut",
        "GoogleRpcStatusIn": "_dataplex_34_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_dataplex_35_GoogleRpcStatusOut",
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoTopNValueIn": "_dataplex_36_GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoTopNValueIn",
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoTopNValueOut": "_dataplex_37_GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoTopNValueOut",
        "GoogleCloudDataplexV1TaskTriggerSpecIn": "_dataplex_38_GoogleCloudDataplexV1TaskTriggerSpecIn",
        "GoogleCloudDataplexV1TaskTriggerSpecOut": "_dataplex_39_GoogleCloudDataplexV1TaskTriggerSpecOut",
        "GoogleCloudDataplexV1DataQualityRuleUniquenessExpectationIn": "_dataplex_40_GoogleCloudDataplexV1DataQualityRuleUniquenessExpectationIn",
        "GoogleCloudDataplexV1DataQualityRuleUniquenessExpectationOut": "_dataplex_41_GoogleCloudDataplexV1DataQualityRuleUniquenessExpectationOut",
        "GoogleCloudDataplexV1ListDataAttributeBindingsResponseIn": "_dataplex_42_GoogleCloudDataplexV1ListDataAttributeBindingsResponseIn",
        "GoogleCloudDataplexV1ListDataAttributeBindingsResponseOut": "_dataplex_43_GoogleCloudDataplexV1ListDataAttributeBindingsResponseOut",
        "GoogleCloudDataplexV1ResourceAccessSpecIn": "_dataplex_44_GoogleCloudDataplexV1ResourceAccessSpecIn",
        "GoogleCloudDataplexV1ResourceAccessSpecOut": "_dataplex_45_GoogleCloudDataplexV1ResourceAccessSpecOut",
        "GoogleCloudDataplexV1ListLakesResponseIn": "_dataplex_46_GoogleCloudDataplexV1ListLakesResponseIn",
        "GoogleCloudDataplexV1ListLakesResponseOut": "_dataplex_47_GoogleCloudDataplexV1ListLakesResponseOut",
        "GoogleCloudDataplexV1EntityCompatibilityStatusCompatibilityIn": "_dataplex_48_GoogleCloudDataplexV1EntityCompatibilityStatusCompatibilityIn",
        "GoogleCloudDataplexV1EntityCompatibilityStatusCompatibilityOut": "_dataplex_49_GoogleCloudDataplexV1EntityCompatibilityStatusCompatibilityOut",
        "GoogleCloudDataplexV1TaskExecutionStatusIn": "_dataplex_50_GoogleCloudDataplexV1TaskExecutionStatusIn",
        "GoogleCloudDataplexV1TaskExecutionStatusOut": "_dataplex_51_GoogleCloudDataplexV1TaskExecutionStatusOut",
        "GoogleCloudDataplexV1AssetSecurityStatusIn": "_dataplex_52_GoogleCloudDataplexV1AssetSecurityStatusIn",
        "GoogleCloudDataplexV1AssetSecurityStatusOut": "_dataplex_53_GoogleCloudDataplexV1AssetSecurityStatusOut",
        "GoogleCloudDataplexV1ListTasksResponseIn": "_dataplex_54_GoogleCloudDataplexV1ListTasksResponseIn",
        "GoogleCloudDataplexV1ListTasksResponseOut": "_dataplex_55_GoogleCloudDataplexV1ListTasksResponseOut",
        "GoogleCloudDataplexV1DataScanEventIn": "_dataplex_56_GoogleCloudDataplexV1DataScanEventIn",
        "GoogleCloudDataplexV1DataScanEventOut": "_dataplex_57_GoogleCloudDataplexV1DataScanEventOut",
        "GoogleCloudDataplexV1ScannedDataIncrementalFieldIn": "_dataplex_58_GoogleCloudDataplexV1ScannedDataIncrementalFieldIn",
        "GoogleCloudDataplexV1ScannedDataIncrementalFieldOut": "_dataplex_59_GoogleCloudDataplexV1ScannedDataIncrementalFieldOut",
        "GoogleCloudDataplexV1SessionIn": "_dataplex_60_GoogleCloudDataplexV1SessionIn",
        "GoogleCloudDataplexV1SessionOut": "_dataplex_61_GoogleCloudDataplexV1SessionOut",
        "GoogleCloudDataplexV1TriggerScheduleIn": "_dataplex_62_GoogleCloudDataplexV1TriggerScheduleIn",
        "GoogleCloudDataplexV1TriggerScheduleOut": "_dataplex_63_GoogleCloudDataplexV1TriggerScheduleOut",
        "GoogleCloudDataplexV1DataQualityResultIn": "_dataplex_64_GoogleCloudDataplexV1DataQualityResultIn",
        "GoogleCloudDataplexV1DataQualityResultOut": "_dataplex_65_GoogleCloudDataplexV1DataQualityResultOut",
        "GoogleCloudDataplexV1ListDataScanJobsResponseIn": "_dataplex_66_GoogleCloudDataplexV1ListDataScanJobsResponseIn",
        "GoogleCloudDataplexV1ListDataScanJobsResponseOut": "_dataplex_67_GoogleCloudDataplexV1ListDataScanJobsResponseOut",
        "EmptyIn": "_dataplex_68_EmptyIn",
        "EmptyOut": "_dataplex_69_EmptyOut",
        "GoogleCloudDataplexV1StorageAccessIn": "_dataplex_70_GoogleCloudDataplexV1StorageAccessIn",
        "GoogleCloudDataplexV1StorageAccessOut": "_dataplex_71_GoogleCloudDataplexV1StorageAccessOut",
        "GoogleCloudDataplexV1ZoneDiscoverySpecIn": "_dataplex_72_GoogleCloudDataplexV1ZoneDiscoverySpecIn",
        "GoogleCloudDataplexV1ZoneDiscoverySpecOut": "_dataplex_73_GoogleCloudDataplexV1ZoneDiscoverySpecOut",
        "GoogleCloudDataplexV1EntityIn": "_dataplex_74_GoogleCloudDataplexV1EntityIn",
        "GoogleCloudDataplexV1EntityOut": "_dataplex_75_GoogleCloudDataplexV1EntityOut",
        "GoogleCloudDataplexV1TaskInfrastructureSpecContainerImageRuntimeIn": "_dataplex_76_GoogleCloudDataplexV1TaskInfrastructureSpecContainerImageRuntimeIn",
        "GoogleCloudDataplexV1TaskInfrastructureSpecContainerImageRuntimeOut": "_dataplex_77_GoogleCloudDataplexV1TaskInfrastructureSpecContainerImageRuntimeOut",
        "GoogleCloudDataplexV1ActionUnauthorizedResourceIn": "_dataplex_78_GoogleCloudDataplexV1ActionUnauthorizedResourceIn",
        "GoogleCloudDataplexV1ActionUnauthorizedResourceOut": "_dataplex_79_GoogleCloudDataplexV1ActionUnauthorizedResourceOut",
        "GoogleCloudDataplexV1ScannedDataIn": "_dataplex_80_GoogleCloudDataplexV1ScannedDataIn",
        "GoogleCloudDataplexV1ScannedDataOut": "_dataplex_81_GoogleCloudDataplexV1ScannedDataOut",
        "GoogleCloudDataplexV1DataQualityRuleRowConditionExpectationIn": "_dataplex_82_GoogleCloudDataplexV1DataQualityRuleRowConditionExpectationIn",
        "GoogleCloudDataplexV1DataQualityRuleRowConditionExpectationOut": "_dataplex_83_GoogleCloudDataplexV1DataQualityRuleRowConditionExpectationOut",
        "GoogleCloudDataplexV1AssetResourceStatusIn": "_dataplex_84_GoogleCloudDataplexV1AssetResourceStatusIn",
        "GoogleCloudDataplexV1AssetResourceStatusOut": "_dataplex_85_GoogleCloudDataplexV1AssetResourceStatusOut",
        "GoogleCloudDataplexV1DiscoveryEventEntityDetailsIn": "_dataplex_86_GoogleCloudDataplexV1DiscoveryEventEntityDetailsIn",
        "GoogleCloudDataplexV1DiscoveryEventEntityDetailsOut": "_dataplex_87_GoogleCloudDataplexV1DiscoveryEventEntityDetailsOut",
        "GoogleCloudDataplexV1ContentSqlScriptIn": "_dataplex_88_GoogleCloudDataplexV1ContentSqlScriptIn",
        "GoogleCloudDataplexV1ContentSqlScriptOut": "_dataplex_89_GoogleCloudDataplexV1ContentSqlScriptOut",
        "GoogleCloudDataplexV1DataQualityRuleRangeExpectationIn": "_dataplex_90_GoogleCloudDataplexV1DataQualityRuleRangeExpectationIn",
        "GoogleCloudDataplexV1DataQualityRuleRangeExpectationOut": "_dataplex_91_GoogleCloudDataplexV1DataQualityRuleRangeExpectationOut",
        "GoogleCloudDataplexV1DataScanIn": "_dataplex_92_GoogleCloudDataplexV1DataScanIn",
        "GoogleCloudDataplexV1DataScanOut": "_dataplex_93_GoogleCloudDataplexV1DataScanOut",
        "GoogleIamV1BindingIn": "_dataplex_94_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_dataplex_95_GoogleIamV1BindingOut",
        "GoogleCloudDataplexV1DataScanExecutionStatusIn": "_dataplex_96_GoogleCloudDataplexV1DataScanExecutionStatusIn",
        "GoogleCloudDataplexV1DataScanExecutionStatusOut": "_dataplex_97_GoogleCloudDataplexV1DataScanExecutionStatusOut",
        "GoogleCloudLocationLocationIn": "_dataplex_98_GoogleCloudLocationLocationIn",
        "GoogleCloudLocationLocationOut": "_dataplex_99_GoogleCloudLocationLocationOut",
        "GoogleCloudDataplexV1ListZonesResponseIn": "_dataplex_100_GoogleCloudDataplexV1ListZonesResponseIn",
        "GoogleCloudDataplexV1ListZonesResponseOut": "_dataplex_101_GoogleCloudDataplexV1ListZonesResponseOut",
        "GoogleCloudDataplexV1ActionFailedSecurityPolicyApplyIn": "_dataplex_102_GoogleCloudDataplexV1ActionFailedSecurityPolicyApplyIn",
        "GoogleCloudDataplexV1ActionFailedSecurityPolicyApplyOut": "_dataplex_103_GoogleCloudDataplexV1ActionFailedSecurityPolicyApplyOut",
        "GoogleCloudDataplexV1ZoneResourceSpecIn": "_dataplex_104_GoogleCloudDataplexV1ZoneResourceSpecIn",
        "GoogleCloudDataplexV1ZoneResourceSpecOut": "_dataplex_105_GoogleCloudDataplexV1ZoneResourceSpecOut",
        "GoogleCloudDataplexV1ListAssetsResponseIn": "_dataplex_106_GoogleCloudDataplexV1ListAssetsResponseIn",
        "GoogleCloudDataplexV1ListAssetsResponseOut": "_dataplex_107_GoogleCloudDataplexV1ListAssetsResponseOut",
        "GoogleIamV1SetIamPolicyRequestIn": "_dataplex_108_GoogleIamV1SetIamPolicyRequestIn",
        "GoogleIamV1SetIamPolicyRequestOut": "_dataplex_109_GoogleIamV1SetIamPolicyRequestOut",
        "GoogleCloudDataplexV1DataQualityRuleTableConditionExpectationIn": "_dataplex_110_GoogleCloudDataplexV1DataQualityRuleTableConditionExpectationIn",
        "GoogleCloudDataplexV1DataQualityRuleTableConditionExpectationOut": "_dataplex_111_GoogleCloudDataplexV1DataQualityRuleTableConditionExpectationOut",
        "GoogleCloudDataplexV1PartitionIn": "_dataplex_112_GoogleCloudDataplexV1PartitionIn",
        "GoogleCloudDataplexV1PartitionOut": "_dataplex_113_GoogleCloudDataplexV1PartitionOut",
        "GoogleCloudDataplexV1ZoneDiscoverySpecCsvOptionsIn": "_dataplex_114_GoogleCloudDataplexV1ZoneDiscoverySpecCsvOptionsIn",
        "GoogleCloudDataplexV1ZoneDiscoverySpecCsvOptionsOut": "_dataplex_115_GoogleCloudDataplexV1ZoneDiscoverySpecCsvOptionsOut",
        "GoogleIamV1AuditLogConfigIn": "_dataplex_116_GoogleIamV1AuditLogConfigIn",
        "GoogleIamV1AuditLogConfigOut": "_dataplex_117_GoogleIamV1AuditLogConfigOut",
        "GoogleCloudDataplexV1DataQualityRuleNonNullExpectationIn": "_dataplex_118_GoogleCloudDataplexV1DataQualityRuleNonNullExpectationIn",
        "GoogleCloudDataplexV1DataQualityRuleNonNullExpectationOut": "_dataplex_119_GoogleCloudDataplexV1DataQualityRuleNonNullExpectationOut",
        "GoogleCloudDataplexV1ActionMissingDataIn": "_dataplex_120_GoogleCloudDataplexV1ActionMissingDataIn",
        "GoogleCloudDataplexV1ActionMissingDataOut": "_dataplex_121_GoogleCloudDataplexV1ActionMissingDataOut",
        "GoogleCloudDataplexV1DataAttributeBindingPathIn": "_dataplex_122_GoogleCloudDataplexV1DataAttributeBindingPathIn",
        "GoogleCloudDataplexV1DataAttributeBindingPathOut": "_dataplex_123_GoogleCloudDataplexV1DataAttributeBindingPathOut",
        "GoogleCloudDataplexV1ListSessionsResponseIn": "_dataplex_124_GoogleCloudDataplexV1ListSessionsResponseIn",
        "GoogleCloudDataplexV1ListSessionsResponseOut": "_dataplex_125_GoogleCloudDataplexV1ListSessionsResponseOut",
        "GoogleCloudDataplexV1ActionInvalidDataOrganizationIn": "_dataplex_126_GoogleCloudDataplexV1ActionInvalidDataOrganizationIn",
        "GoogleCloudDataplexV1ActionInvalidDataOrganizationOut": "_dataplex_127_GoogleCloudDataplexV1ActionInvalidDataOrganizationOut",
        "GoogleCloudDataplexV1EnvironmentIn": "_dataplex_128_GoogleCloudDataplexV1EnvironmentIn",
        "GoogleCloudDataplexV1EnvironmentOut": "_dataplex_129_GoogleCloudDataplexV1EnvironmentOut",
        "GoogleCloudDataplexV1SchemaIn": "_dataplex_130_GoogleCloudDataplexV1SchemaIn",
        "GoogleCloudDataplexV1SchemaOut": "_dataplex_131_GoogleCloudDataplexV1SchemaOut",
        "GoogleCloudDataplexV1TaskIn": "_dataplex_132_GoogleCloudDataplexV1TaskIn",
        "GoogleCloudDataplexV1TaskOut": "_dataplex_133_GoogleCloudDataplexV1TaskOut",
        "GoogleCloudDataplexV1EnvironmentInfrastructureSpecComputeResourcesIn": "_dataplex_134_GoogleCloudDataplexV1EnvironmentInfrastructureSpecComputeResourcesIn",
        "GoogleCloudDataplexV1EnvironmentInfrastructureSpecComputeResourcesOut": "_dataplex_135_GoogleCloudDataplexV1EnvironmentInfrastructureSpecComputeResourcesOut",
        "GoogleCloudDataplexV1DiscoveryEventPartitionDetailsIn": "_dataplex_136_GoogleCloudDataplexV1DiscoveryEventPartitionDetailsIn",
        "GoogleCloudDataplexV1DiscoveryEventPartitionDetailsOut": "_dataplex_137_GoogleCloudDataplexV1DiscoveryEventPartitionDetailsOut",
        "GoogleCloudDataplexV1DiscoveryEventConfigDetailsIn": "_dataplex_138_GoogleCloudDataplexV1DiscoveryEventConfigDetailsIn",
        "GoogleCloudDataplexV1DiscoveryEventConfigDetailsOut": "_dataplex_139_GoogleCloudDataplexV1DiscoveryEventConfigDetailsOut",
        "GoogleCloudDataplexV1ListJobsResponseIn": "_dataplex_140_GoogleCloudDataplexV1ListJobsResponseIn",
        "GoogleCloudDataplexV1ListJobsResponseOut": "_dataplex_141_GoogleCloudDataplexV1ListJobsResponseOut",
        "GoogleCloudDataplexV1AssetDiscoveryStatusStatsIn": "_dataplex_142_GoogleCloudDataplexV1AssetDiscoveryStatusStatsIn",
        "GoogleCloudDataplexV1AssetDiscoveryStatusStatsOut": "_dataplex_143_GoogleCloudDataplexV1AssetDiscoveryStatusStatsOut",
        "GoogleCloudDataplexV1DataAttributeIn": "_dataplex_144_GoogleCloudDataplexV1DataAttributeIn",
        "GoogleCloudDataplexV1DataAttributeOut": "_dataplex_145_GoogleCloudDataplexV1DataAttributeOut",
        "GoogleCloudDataplexV1ContentIn": "_dataplex_146_GoogleCloudDataplexV1ContentIn",
        "GoogleCloudDataplexV1ContentOut": "_dataplex_147_GoogleCloudDataplexV1ContentOut",
        "GoogleCloudDataplexV1AssetDiscoverySpecCsvOptionsIn": "_dataplex_148_GoogleCloudDataplexV1AssetDiscoverySpecCsvOptionsIn",
        "GoogleCloudDataplexV1AssetDiscoverySpecCsvOptionsOut": "_dataplex_149_GoogleCloudDataplexV1AssetDiscoverySpecCsvOptionsOut",
        "GoogleCloudDataplexV1TaskExecutionSpecIn": "_dataplex_150_GoogleCloudDataplexV1TaskExecutionSpecIn",
        "GoogleCloudDataplexV1TaskExecutionSpecOut": "_dataplex_151_GoogleCloudDataplexV1TaskExecutionSpecOut",
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoStringFieldInfoIn": "_dataplex_152_GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoStringFieldInfoIn",
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoStringFieldInfoOut": "_dataplex_153_GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoStringFieldInfoOut",
        "GoogleCloudDataplexV1LakeMetastoreIn": "_dataplex_154_GoogleCloudDataplexV1LakeMetastoreIn",
        "GoogleCloudDataplexV1LakeMetastoreOut": "_dataplex_155_GoogleCloudDataplexV1LakeMetastoreOut",
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoDoubleFieldInfoIn": "_dataplex_156_GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoDoubleFieldInfoIn",
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoDoubleFieldInfoOut": "_dataplex_157_GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoDoubleFieldInfoOut",
        "GoogleCloudDataplexV1ListDataAttributesResponseIn": "_dataplex_158_GoogleCloudDataplexV1ListDataAttributesResponseIn",
        "GoogleCloudDataplexV1ListDataAttributesResponseOut": "_dataplex_159_GoogleCloudDataplexV1ListDataAttributesResponseOut",
        "GoogleCloudDataplexV1ListPartitionsResponseIn": "_dataplex_160_GoogleCloudDataplexV1ListPartitionsResponseIn",
        "GoogleCloudDataplexV1ListPartitionsResponseOut": "_dataplex_161_GoogleCloudDataplexV1ListPartitionsResponseOut",
        "GoogleCloudDataplexV1ZoneIn": "_dataplex_162_GoogleCloudDataplexV1ZoneIn",
        "GoogleCloudDataplexV1ZoneOut": "_dataplex_163_GoogleCloudDataplexV1ZoneOut",
        "GoogleIamV1TestIamPermissionsResponseIn": "_dataplex_164_GoogleIamV1TestIamPermissionsResponseIn",
        "GoogleIamV1TestIamPermissionsResponseOut": "_dataplex_165_GoogleIamV1TestIamPermissionsResponseOut",
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIn": "_dataplex_166_GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIn",
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoOut": "_dataplex_167_GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoOut",
        "GoogleCloudDataplexV1SessionEventIn": "_dataplex_168_GoogleCloudDataplexV1SessionEventIn",
        "GoogleCloudDataplexV1SessionEventOut": "_dataplex_169_GoogleCloudDataplexV1SessionEventOut",
        "GoogleCloudDataplexV1ListDataScansResponseIn": "_dataplex_170_GoogleCloudDataplexV1ListDataScansResponseIn",
        "GoogleCloudDataplexV1ListDataScansResponseOut": "_dataplex_171_GoogleCloudDataplexV1ListDataScansResponseOut",
        "GoogleIamV1PolicyIn": "_dataplex_172_GoogleIamV1PolicyIn",
        "GoogleIamV1PolicyOut": "_dataplex_173_GoogleIamV1PolicyOut",
        "GoogleCloudDataplexV1DiscoveryEventActionDetailsIn": "_dataplex_174_GoogleCloudDataplexV1DiscoveryEventActionDetailsIn",
        "GoogleCloudDataplexV1DiscoveryEventActionDetailsOut": "_dataplex_175_GoogleCloudDataplexV1DiscoveryEventActionDetailsOut",
        "GoogleCloudDataplexV1DataScanEventDataProfileResultIn": "_dataplex_176_GoogleCloudDataplexV1DataScanEventDataProfileResultIn",
        "GoogleCloudDataplexV1DataScanEventDataProfileResultOut": "_dataplex_177_GoogleCloudDataplexV1DataScanEventDataProfileResultOut",
        "GoogleCloudDataplexV1RunTaskResponseIn": "_dataplex_178_GoogleCloudDataplexV1RunTaskResponseIn",
        "GoogleCloudDataplexV1RunTaskResponseOut": "_dataplex_179_GoogleCloudDataplexV1RunTaskResponseOut",
        "GoogleCloudDataplexV1ActionInvalidDataFormatIn": "_dataplex_180_GoogleCloudDataplexV1ActionInvalidDataFormatIn",
        "GoogleCloudDataplexV1ActionInvalidDataFormatOut": "_dataplex_181_GoogleCloudDataplexV1ActionInvalidDataFormatOut",
        "GoogleCloudDataplexV1ActionMissingResourceIn": "_dataplex_182_GoogleCloudDataplexV1ActionMissingResourceIn",
        "GoogleCloudDataplexV1ActionMissingResourceOut": "_dataplex_183_GoogleCloudDataplexV1ActionMissingResourceOut",
        "GoogleCloudDataplexV1DataAttributeBindingIn": "_dataplex_184_GoogleCloudDataplexV1DataAttributeBindingIn",
        "GoogleCloudDataplexV1DataAttributeBindingOut": "_dataplex_185_GoogleCloudDataplexV1DataAttributeBindingOut",
        "GoogleCloudDataplexV1AssetDiscoveryStatusIn": "_dataplex_186_GoogleCloudDataplexV1AssetDiscoveryStatusIn",
        "GoogleCloudDataplexV1AssetDiscoveryStatusOut": "_dataplex_187_GoogleCloudDataplexV1AssetDiscoveryStatusOut",
        "GoogleCloudDataplexV1DataQualityRuleResultIn": "_dataplex_188_GoogleCloudDataplexV1DataQualityRuleResultIn",
        "GoogleCloudDataplexV1DataQualityRuleResultOut": "_dataplex_189_GoogleCloudDataplexV1DataQualityRuleResultOut",
        "GoogleCloudDataplexV1ZoneDiscoverySpecJsonOptionsIn": "_dataplex_190_GoogleCloudDataplexV1ZoneDiscoverySpecJsonOptionsIn",
        "GoogleCloudDataplexV1ZoneDiscoverySpecJsonOptionsOut": "_dataplex_191_GoogleCloudDataplexV1ZoneDiscoverySpecJsonOptionsOut",
        "GoogleCloudDataplexV1LakeIn": "_dataplex_192_GoogleCloudDataplexV1LakeIn",
        "GoogleCloudDataplexV1LakeOut": "_dataplex_193_GoogleCloudDataplexV1LakeOut",
        "GoogleCloudDataplexV1TaskInfrastructureSpecIn": "_dataplex_194_GoogleCloudDataplexV1TaskInfrastructureSpecIn",
        "GoogleCloudDataplexV1TaskInfrastructureSpecOut": "_dataplex_195_GoogleCloudDataplexV1TaskInfrastructureSpecOut",
        "GoogleCloudDataplexV1DataProfileResultProfileFieldIn": "_dataplex_196_GoogleCloudDataplexV1DataProfileResultProfileFieldIn",
        "GoogleCloudDataplexV1DataProfileResultProfileFieldOut": "_dataplex_197_GoogleCloudDataplexV1DataProfileResultProfileFieldOut",
        "GoogleCloudDataplexV1StorageFormatIcebergOptionsIn": "_dataplex_198_GoogleCloudDataplexV1StorageFormatIcebergOptionsIn",
        "GoogleCloudDataplexV1StorageFormatIcebergOptionsOut": "_dataplex_199_GoogleCloudDataplexV1StorageFormatIcebergOptionsOut",
        "GoogleCloudDataplexV1OperationMetadataIn": "_dataplex_200_GoogleCloudDataplexV1OperationMetadataIn",
        "GoogleCloudDataplexV1OperationMetadataOut": "_dataplex_201_GoogleCloudDataplexV1OperationMetadataOut",
        "GoogleCloudDataplexV1RunDataScanRequestIn": "_dataplex_202_GoogleCloudDataplexV1RunDataScanRequestIn",
        "GoogleCloudDataplexV1RunDataScanRequestOut": "_dataplex_203_GoogleCloudDataplexV1RunDataScanRequestOut",
        "GoogleCloudDataplexV1ActionIncompatibleDataSchemaIn": "_dataplex_204_GoogleCloudDataplexV1ActionIncompatibleDataSchemaIn",
        "GoogleCloudDataplexV1ActionIncompatibleDataSchemaOut": "_dataplex_205_GoogleCloudDataplexV1ActionIncompatibleDataSchemaOut",
        "GoogleCloudDataplexV1DataQualityRuleSetExpectationIn": "_dataplex_206_GoogleCloudDataplexV1DataQualityRuleSetExpectationIn",
        "GoogleCloudDataplexV1DataQualityRuleSetExpectationOut": "_dataplex_207_GoogleCloudDataplexV1DataQualityRuleSetExpectationOut",
        "GoogleCloudDataplexV1ListActionsResponseIn": "_dataplex_208_GoogleCloudDataplexV1ListActionsResponseIn",
        "GoogleCloudDataplexV1ListActionsResponseOut": "_dataplex_209_GoogleCloudDataplexV1ListActionsResponseOut",
        "GoogleCloudDataplexV1CancelJobRequestIn": "_dataplex_210_GoogleCloudDataplexV1CancelJobRequestIn",
        "GoogleCloudDataplexV1CancelJobRequestOut": "_dataplex_211_GoogleCloudDataplexV1CancelJobRequestOut",
        "GoogleCloudDataplexV1RunTaskRequestIn": "_dataplex_212_GoogleCloudDataplexV1RunTaskRequestIn",
        "GoogleCloudDataplexV1RunTaskRequestOut": "_dataplex_213_GoogleCloudDataplexV1RunTaskRequestOut",
        "GoogleCloudDataplexV1EntityCompatibilityStatusIn": "_dataplex_214_GoogleCloudDataplexV1EntityCompatibilityStatusIn",
        "GoogleCloudDataplexV1EntityCompatibilityStatusOut": "_dataplex_215_GoogleCloudDataplexV1EntityCompatibilityStatusOut",
        "GoogleTypeExprIn": "_dataplex_216_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_dataplex_217_GoogleTypeExprOut",
        "GoogleCloudDataplexV1AssetDiscoverySpecJsonOptionsIn": "_dataplex_218_GoogleCloudDataplexV1AssetDiscoverySpecJsonOptionsIn",
        "GoogleCloudDataplexV1AssetDiscoverySpecJsonOptionsOut": "_dataplex_219_GoogleCloudDataplexV1AssetDiscoverySpecJsonOptionsOut",
        "GoogleCloudDataplexV1JobEventIn": "_dataplex_220_GoogleCloudDataplexV1JobEventIn",
        "GoogleCloudDataplexV1JobEventOut": "_dataplex_221_GoogleCloudDataplexV1JobEventOut",
        "GoogleCloudDataplexV1SessionEventQueryDetailIn": "_dataplex_222_GoogleCloudDataplexV1SessionEventQueryDetailIn",
        "GoogleCloudDataplexV1SessionEventQueryDetailOut": "_dataplex_223_GoogleCloudDataplexV1SessionEventQueryDetailOut",
        "GoogleCloudDataplexV1TaskInfrastructureSpecBatchComputeResourcesIn": "_dataplex_224_GoogleCloudDataplexV1TaskInfrastructureSpecBatchComputeResourcesIn",
        "GoogleCloudDataplexV1TaskInfrastructureSpecBatchComputeResourcesOut": "_dataplex_225_GoogleCloudDataplexV1TaskInfrastructureSpecBatchComputeResourcesOut",
        "GoogleLongrunningListOperationsResponseIn": "_dataplex_226_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_dataplex_227_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudDataplexV1AssetIn": "_dataplex_228_GoogleCloudDataplexV1AssetIn",
        "GoogleCloudDataplexV1AssetOut": "_dataplex_229_GoogleCloudDataplexV1AssetOut",
        "GoogleCloudDataplexV1ListEnvironmentsResponseIn": "_dataplex_230_GoogleCloudDataplexV1ListEnvironmentsResponseIn",
        "GoogleCloudDataplexV1ListEnvironmentsResponseOut": "_dataplex_231_GoogleCloudDataplexV1ListEnvironmentsResponseOut",
        "GoogleCloudDataplexV1AssetStatusIn": "_dataplex_232_GoogleCloudDataplexV1AssetStatusIn",
        "GoogleCloudDataplexV1AssetStatusOut": "_dataplex_233_GoogleCloudDataplexV1AssetStatusOut",
        "GoogleCloudDataplexV1AssetResourceSpecIn": "_dataplex_234_GoogleCloudDataplexV1AssetResourceSpecIn",
        "GoogleCloudDataplexV1AssetResourceSpecOut": "_dataplex_235_GoogleCloudDataplexV1AssetResourceSpecOut",
        "GoogleCloudDataplexV1DataTaxonomyIn": "_dataplex_236_GoogleCloudDataplexV1DataTaxonomyIn",
        "GoogleCloudDataplexV1DataTaxonomyOut": "_dataplex_237_GoogleCloudDataplexV1DataTaxonomyOut",
        "GoogleCloudDataplexV1DataScanEventDataProfileAppliedConfigsIn": "_dataplex_238_GoogleCloudDataplexV1DataScanEventDataProfileAppliedConfigsIn",
        "GoogleCloudDataplexV1DataScanEventDataProfileAppliedConfigsOut": "_dataplex_239_GoogleCloudDataplexV1DataScanEventDataProfileAppliedConfigsOut",
        "GoogleCloudDataplexV1ListEntitiesResponseIn": "_dataplex_240_GoogleCloudDataplexV1ListEntitiesResponseIn",
        "GoogleCloudDataplexV1ListEntitiesResponseOut": "_dataplex_241_GoogleCloudDataplexV1ListEntitiesResponseOut",
        "GoogleCloudDataplexV1DataQualitySpecIn": "_dataplex_242_GoogleCloudDataplexV1DataQualitySpecIn",
        "GoogleCloudDataplexV1DataQualitySpecOut": "_dataplex_243_GoogleCloudDataplexV1DataQualitySpecOut",
        "GoogleCloudDataplexV1SchemaPartitionFieldIn": "_dataplex_244_GoogleCloudDataplexV1SchemaPartitionFieldIn",
        "GoogleCloudDataplexV1SchemaPartitionFieldOut": "_dataplex_245_GoogleCloudDataplexV1SchemaPartitionFieldOut",
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIntegerFieldInfoIn": "_dataplex_246_GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIntegerFieldInfoIn",
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIntegerFieldInfoOut": "_dataplex_247_GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIntegerFieldInfoOut",
        "GoogleCloudDataplexV1ActionInvalidDataPartitionIn": "_dataplex_248_GoogleCloudDataplexV1ActionInvalidDataPartitionIn",
        "GoogleCloudDataplexV1ActionInvalidDataPartitionOut": "_dataplex_249_GoogleCloudDataplexV1ActionInvalidDataPartitionOut",
        "GoogleCloudDataplexV1EnvironmentSessionSpecIn": "_dataplex_250_GoogleCloudDataplexV1EnvironmentSessionSpecIn",
        "GoogleCloudDataplexV1EnvironmentSessionSpecOut": "_dataplex_251_GoogleCloudDataplexV1EnvironmentSessionSpecOut",
        "GoogleCloudDataplexV1DataAccessSpecIn": "_dataplex_252_GoogleCloudDataplexV1DataAccessSpecIn",
        "GoogleCloudDataplexV1DataAccessSpecOut": "_dataplex_253_GoogleCloudDataplexV1DataAccessSpecOut",
        "GoogleCloudDataplexV1SchemaSchemaFieldIn": "_dataplex_254_GoogleCloudDataplexV1SchemaSchemaFieldIn",
        "GoogleCloudDataplexV1SchemaSchemaFieldOut": "_dataplex_255_GoogleCloudDataplexV1SchemaSchemaFieldOut",
        "GoogleCloudDataplexV1ContentNotebookIn": "_dataplex_256_GoogleCloudDataplexV1ContentNotebookIn",
        "GoogleCloudDataplexV1ContentNotebookOut": "_dataplex_257_GoogleCloudDataplexV1ContentNotebookOut",
        "GoogleCloudDataplexV1EnvironmentInfrastructureSpecIn": "_dataplex_258_GoogleCloudDataplexV1EnvironmentInfrastructureSpecIn",
        "GoogleCloudDataplexV1EnvironmentInfrastructureSpecOut": "_dataplex_259_GoogleCloudDataplexV1EnvironmentInfrastructureSpecOut",
        "GoogleCloudDataplexV1DataScanEventDataQualityAppliedConfigsIn": "_dataplex_260_GoogleCloudDataplexV1DataScanEventDataQualityAppliedConfigsIn",
        "GoogleCloudDataplexV1DataScanEventDataQualityAppliedConfigsOut": "_dataplex_261_GoogleCloudDataplexV1DataScanEventDataQualityAppliedConfigsOut",
        "GoogleCloudDataplexV1TaskNotebookTaskConfigIn": "_dataplex_262_GoogleCloudDataplexV1TaskNotebookTaskConfigIn",
        "GoogleCloudDataplexV1TaskNotebookTaskConfigOut": "_dataplex_263_GoogleCloudDataplexV1TaskNotebookTaskConfigOut",
        "GoogleCloudDataplexV1JobIn": "_dataplex_264_GoogleCloudDataplexV1JobIn",
        "GoogleCloudDataplexV1JobOut": "_dataplex_265_GoogleCloudDataplexV1JobOut",
        "GoogleCloudDataplexV1ListDataTaxonomiesResponseIn": "_dataplex_266_GoogleCloudDataplexV1ListDataTaxonomiesResponseIn",
        "GoogleCloudDataplexV1ListDataTaxonomiesResponseOut": "_dataplex_267_GoogleCloudDataplexV1ListDataTaxonomiesResponseOut",
        "GoogleCloudDataplexV1StorageFormatJsonOptionsIn": "_dataplex_268_GoogleCloudDataplexV1StorageFormatJsonOptionsIn",
        "GoogleCloudDataplexV1StorageFormatJsonOptionsOut": "_dataplex_269_GoogleCloudDataplexV1StorageFormatJsonOptionsOut",
        "GoogleCloudDataplexV1DataProfileResultIn": "_dataplex_270_GoogleCloudDataplexV1DataProfileResultIn",
        "GoogleCloudDataplexV1DataProfileResultOut": "_dataplex_271_GoogleCloudDataplexV1DataProfileResultOut",
        "GoogleCloudDataplexV1DataQualityRuleIn": "_dataplex_272_GoogleCloudDataplexV1DataQualityRuleIn",
        "GoogleCloudDataplexV1DataQualityRuleOut": "_dataplex_273_GoogleCloudDataplexV1DataQualityRuleOut",
        "GoogleLongrunningCancelOperationRequestIn": "_dataplex_274_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_dataplex_275_GoogleLongrunningCancelOperationRequestOut",
        "GoogleCloudLocationListLocationsResponseIn": "_dataplex_276_GoogleCloudLocationListLocationsResponseIn",
        "GoogleCloudLocationListLocationsResponseOut": "_dataplex_277_GoogleCloudLocationListLocationsResponseOut",
        "GoogleCloudDataplexV1ActionIn": "_dataplex_278_GoogleCloudDataplexV1ActionIn",
        "GoogleCloudDataplexV1ActionOut": "_dataplex_279_GoogleCloudDataplexV1ActionOut",
        "GoogleCloudDataplexV1DataSourceIn": "_dataplex_280_GoogleCloudDataplexV1DataSourceIn",
        "GoogleCloudDataplexV1DataSourceOut": "_dataplex_281_GoogleCloudDataplexV1DataSourceOut",
        "GoogleCloudDataplexV1DataScanJobIn": "_dataplex_282_GoogleCloudDataplexV1DataScanJobIn",
        "GoogleCloudDataplexV1DataScanJobOut": "_dataplex_283_GoogleCloudDataplexV1DataScanJobOut",
        "GoogleCloudDataplexV1LakeMetastoreStatusIn": "_dataplex_284_GoogleCloudDataplexV1LakeMetastoreStatusIn",
        "GoogleCloudDataplexV1LakeMetastoreStatusOut": "_dataplex_285_GoogleCloudDataplexV1LakeMetastoreStatusOut",
        "GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectationIn": "_dataplex_286_GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectationIn",
        "GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectationOut": "_dataplex_287_GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectationOut",
        "GoogleIamV1TestIamPermissionsRequestIn": "_dataplex_288_GoogleIamV1TestIamPermissionsRequestIn",
        "GoogleIamV1TestIamPermissionsRequestOut": "_dataplex_289_GoogleIamV1TestIamPermissionsRequestOut",
        "GoogleCloudDataplexV1DataProfileSpecIn": "_dataplex_290_GoogleCloudDataplexV1DataProfileSpecIn",
        "GoogleCloudDataplexV1DataProfileSpecOut": "_dataplex_291_GoogleCloudDataplexV1DataProfileSpecOut",
        "GoogleCloudDataplexV1TaskSparkTaskConfigIn": "_dataplex_292_GoogleCloudDataplexV1TaskSparkTaskConfigIn",
        "GoogleCloudDataplexV1TaskSparkTaskConfigOut": "_dataplex_293_GoogleCloudDataplexV1TaskSparkTaskConfigOut",
        "GoogleCloudDataplexV1DataScanExecutionSpecIn": "_dataplex_294_GoogleCloudDataplexV1DataScanExecutionSpecIn",
        "GoogleCloudDataplexV1DataScanExecutionSpecOut": "_dataplex_295_GoogleCloudDataplexV1DataScanExecutionSpecOut",
        "GoogleLongrunningOperationIn": "_dataplex_296_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_dataplex_297_GoogleLongrunningOperationOut",
        "GoogleCloudDataplexV1AssetDiscoverySpecIn": "_dataplex_298_GoogleCloudDataplexV1AssetDiscoverySpecIn",
        "GoogleCloudDataplexV1AssetDiscoverySpecOut": "_dataplex_299_GoogleCloudDataplexV1AssetDiscoverySpecOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudDataplexV1TriggerIn"] = t.struct(
        {
            "onDemand": t.proxy(
                renames["GoogleCloudDataplexV1TriggerOnDemandIn"]
            ).optional(),
            "schedule": t.proxy(
                renames["GoogleCloudDataplexV1TriggerScheduleIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TriggerIn"])
    types["GoogleCloudDataplexV1TriggerOut"] = t.struct(
        {
            "onDemand": t.proxy(
                renames["GoogleCloudDataplexV1TriggerOnDemandOut"]
            ).optional(),
            "schedule": t.proxy(
                renames["GoogleCloudDataplexV1TriggerScheduleOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TriggerOut"])
    types["GoogleCloudDataplexV1DataProfileResultProfileIn"] = t.struct(
        {
            "fields": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataProfileResultProfileFieldIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDataplexV1DataProfileResultProfileIn"])
    types["GoogleCloudDataplexV1DataProfileResultProfileOut"] = t.struct(
        {
            "fields": t.array(
                t.proxy(
                    renames["GoogleCloudDataplexV1DataProfileResultProfileFieldOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataProfileResultProfileOut"])
    types["GoogleCloudDataplexV1EnvironmentEndpointsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1EnvironmentEndpointsIn"])
    types["GoogleCloudDataplexV1EnvironmentEndpointsOut"] = t.struct(
        {
            "notebooks": t.string().optional(),
            "sql": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1EnvironmentEndpointsOut"])
    types["GoogleCloudDataplexV1StorageFormatIn"] = t.struct(
        {
            "csv": t.proxy(
                renames["GoogleCloudDataplexV1StorageFormatCsvOptionsIn"]
            ).optional(),
            "json": t.proxy(
                renames["GoogleCloudDataplexV1StorageFormatJsonOptionsIn"]
            ).optional(),
            "mimeType": t.string(),
            "iceberg": t.proxy(
                renames["GoogleCloudDataplexV1StorageFormatIcebergOptionsIn"]
            ).optional(),
            "compressionFormat": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1StorageFormatIn"])
    types["GoogleCloudDataplexV1StorageFormatOut"] = t.struct(
        {
            "csv": t.proxy(
                renames["GoogleCloudDataplexV1StorageFormatCsvOptionsOut"]
            ).optional(),
            "json": t.proxy(
                renames["GoogleCloudDataplexV1StorageFormatJsonOptionsOut"]
            ).optional(),
            "format": t.string().optional(),
            "mimeType": t.string(),
            "iceberg": t.proxy(
                renames["GoogleCloudDataplexV1StorageFormatIcebergOptionsOut"]
            ).optional(),
            "compressionFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1StorageFormatOut"])
    types["GoogleIamV1AuditConfigIn"] = t.struct(
        {
            "auditLogConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditLogConfigIn"])
            ).optional(),
            "service": t.string().optional(),
        }
    ).named(renames["GoogleIamV1AuditConfigIn"])
    types["GoogleIamV1AuditConfigOut"] = t.struct(
        {
            "auditLogConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditLogConfigOut"])
            ).optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1AuditConfigOut"])
    types["GoogleCloudDataplexV1DataQualityDimensionResultIn"] = t.struct(
        {"passed": t.boolean().optional()}
    ).named(renames["GoogleCloudDataplexV1DataQualityDimensionResultIn"])
    types["GoogleCloudDataplexV1DataQualityDimensionResultOut"] = t.struct(
        {
            "passed": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualityDimensionResultOut"])
    types["GoogleCloudDataplexV1StorageFormatCsvOptionsIn"] = t.struct(
        {
            "quote": t.string().optional(),
            "headerRows": t.integer().optional(),
            "encoding": t.string().optional(),
            "delimiter": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1StorageFormatCsvOptionsIn"])
    types["GoogleCloudDataplexV1StorageFormatCsvOptionsOut"] = t.struct(
        {
            "quote": t.string().optional(),
            "headerRows": t.integer().optional(),
            "encoding": t.string().optional(),
            "delimiter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1StorageFormatCsvOptionsOut"])
    types["GoogleCloudDataplexV1TriggerOnDemandIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1TriggerOnDemandIn"])
    types["GoogleCloudDataplexV1TriggerOnDemandOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDataplexV1TriggerOnDemandOut"])
    types[
        "GoogleCloudDataplexV1EnvironmentInfrastructureSpecOsImageRuntimeIn"
    ] = t.struct(
        {
            "pythonPackages": t.array(t.string()).optional(),
            "javaLibraries": t.array(t.string()).optional(),
            "imageVersion": t.string(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(
        renames["GoogleCloudDataplexV1EnvironmentInfrastructureSpecOsImageRuntimeIn"]
    )
    types[
        "GoogleCloudDataplexV1EnvironmentInfrastructureSpecOsImageRuntimeOut"
    ] = t.struct(
        {
            "pythonPackages": t.array(t.string()).optional(),
            "javaLibraries": t.array(t.string()).optional(),
            "imageVersion": t.string(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDataplexV1EnvironmentInfrastructureSpecOsImageRuntimeOut"]
    )
    types["GoogleCloudDataplexV1TaskInfrastructureSpecVpcNetworkIn"] = t.struct(
        {
            "network": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "subNetwork": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TaskInfrastructureSpecVpcNetworkIn"])
    types["GoogleCloudDataplexV1TaskInfrastructureSpecVpcNetworkOut"] = t.struct(
        {
            "network": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "subNetwork": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TaskInfrastructureSpecVpcNetworkOut"])
    types["GoogleCloudDataplexV1DiscoveryEventIn"] = t.struct(
        {
            "message": t.string().optional(),
            "zoneId": t.string().optional(),
            "assetId": t.string().optional(),
            "type": t.string().optional(),
            "dataLocation": t.string().optional(),
            "config": t.proxy(
                renames["GoogleCloudDataplexV1DiscoveryEventConfigDetailsIn"]
            ).optional(),
            "entity": t.proxy(
                renames["GoogleCloudDataplexV1DiscoveryEventEntityDetailsIn"]
            ).optional(),
            "action": t.proxy(
                renames["GoogleCloudDataplexV1DiscoveryEventActionDetailsIn"]
            ).optional(),
            "partition": t.proxy(
                renames["GoogleCloudDataplexV1DiscoveryEventPartitionDetailsIn"]
            ).optional(),
            "lakeId": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DiscoveryEventIn"])
    types["GoogleCloudDataplexV1DiscoveryEventOut"] = t.struct(
        {
            "message": t.string().optional(),
            "zoneId": t.string().optional(),
            "assetId": t.string().optional(),
            "type": t.string().optional(),
            "dataLocation": t.string().optional(),
            "config": t.proxy(
                renames["GoogleCloudDataplexV1DiscoveryEventConfigDetailsOut"]
            ).optional(),
            "entity": t.proxy(
                renames["GoogleCloudDataplexV1DiscoveryEventEntityDetailsOut"]
            ).optional(),
            "action": t.proxy(
                renames["GoogleCloudDataplexV1DiscoveryEventActionDetailsOut"]
            ).optional(),
            "partition": t.proxy(
                renames["GoogleCloudDataplexV1DiscoveryEventPartitionDetailsOut"]
            ).optional(),
            "lakeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DiscoveryEventOut"])
    types["GoogleCloudDataplexV1EnvironmentSessionStatusIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1EnvironmentSessionStatusIn"])
    types["GoogleCloudDataplexV1EnvironmentSessionStatusOut"] = t.struct(
        {
            "active": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1EnvironmentSessionStatusOut"])
    types["GoogleCloudDataplexV1DataQualityRuleRegexExpectationIn"] = t.struct(
        {"regex": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleRegexExpectationIn"])
    types["GoogleCloudDataplexV1DataQualityRuleRegexExpectationOut"] = t.struct(
        {
            "regex": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleRegexExpectationOut"])
    types["GoogleCloudDataplexV1RunDataScanResponseIn"] = t.struct(
        {"job": t.proxy(renames["GoogleCloudDataplexV1DataScanJobIn"]).optional()}
    ).named(renames["GoogleCloudDataplexV1RunDataScanResponseIn"])
    types["GoogleCloudDataplexV1RunDataScanResponseOut"] = t.struct(
        {
            "job": t.proxy(renames["GoogleCloudDataplexV1DataScanJobOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1RunDataScanResponseOut"])
    types["GoogleCloudDataplexV1DataScanEventDataQualityResultIn"] = t.struct(
        {
            "rowCount": t.string().optional(),
            "dimensionPassed": t.struct({"_": t.string().optional()}).optional(),
            "passed": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanEventDataQualityResultIn"])
    types["GoogleCloudDataplexV1DataScanEventDataQualityResultOut"] = t.struct(
        {
            "rowCount": t.string().optional(),
            "dimensionPassed": t.struct({"_": t.string().optional()}).optional(),
            "passed": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanEventDataQualityResultOut"])
    types["GoogleCloudDataplexV1ListContentResponseIn"] = t.struct(
        {
            "content": t.array(
                t.proxy(renames["GoogleCloudDataplexV1ContentIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListContentResponseIn"])
    types["GoogleCloudDataplexV1ListContentResponseOut"] = t.struct(
        {
            "content": t.array(
                t.proxy(renames["GoogleCloudDataplexV1ContentOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListContentResponseOut"])
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
    types[
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoTopNValueIn"
    ] = t.struct(
        {"value": t.string().optional(), "count": t.string().optional()}
    ).named(
        renames[
            "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoTopNValueIn"
        ]
    )
    types[
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoTopNValueOut"
    ] = t.struct(
        {
            "value": t.string().optional(),
            "count": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoTopNValueOut"
        ]
    )
    types["GoogleCloudDataplexV1TaskTriggerSpecIn"] = t.struct(
        {
            "type": t.string(),
            "maxRetries": t.integer().optional(),
            "disabled": t.boolean().optional(),
            "startTime": t.string().optional(),
            "schedule": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TaskTriggerSpecIn"])
    types["GoogleCloudDataplexV1TaskTriggerSpecOut"] = t.struct(
        {
            "type": t.string(),
            "maxRetries": t.integer().optional(),
            "disabled": t.boolean().optional(),
            "startTime": t.string().optional(),
            "schedule": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TaskTriggerSpecOut"])
    types["GoogleCloudDataplexV1DataQualityRuleUniquenessExpectationIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleUniquenessExpectationIn"])
    types["GoogleCloudDataplexV1DataQualityRuleUniquenessExpectationOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleUniquenessExpectationOut"])
    types["GoogleCloudDataplexV1ListDataAttributeBindingsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "dataAttributeBindings": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataAttributeBindingIn"])
            ).optional(),
            "unreachableLocations": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListDataAttributeBindingsResponseIn"])
    types["GoogleCloudDataplexV1ListDataAttributeBindingsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "dataAttributeBindings": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataAttributeBindingOut"])
            ).optional(),
            "unreachableLocations": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListDataAttributeBindingsResponseOut"])
    types["GoogleCloudDataplexV1ResourceAccessSpecIn"] = t.struct(
        {
            "writers": t.array(t.string()).optional(),
            "readers": t.array(t.string()).optional(),
            "owners": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ResourceAccessSpecIn"])
    types["GoogleCloudDataplexV1ResourceAccessSpecOut"] = t.struct(
        {
            "writers": t.array(t.string()).optional(),
            "readers": t.array(t.string()).optional(),
            "owners": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ResourceAccessSpecOut"])
    types["GoogleCloudDataplexV1ListLakesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "lakes": t.array(
                t.proxy(renames["GoogleCloudDataplexV1LakeIn"])
            ).optional(),
            "unreachableLocations": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListLakesResponseIn"])
    types["GoogleCloudDataplexV1ListLakesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "lakes": t.array(
                t.proxy(renames["GoogleCloudDataplexV1LakeOut"])
            ).optional(),
            "unreachableLocations": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListLakesResponseOut"])
    types["GoogleCloudDataplexV1EntityCompatibilityStatusCompatibilityIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1EntityCompatibilityStatusCompatibilityIn"])
    types["GoogleCloudDataplexV1EntityCompatibilityStatusCompatibilityOut"] = t.struct(
        {
            "compatible": t.boolean().optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1EntityCompatibilityStatusCompatibilityOut"])
    types["GoogleCloudDataplexV1TaskExecutionStatusIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1TaskExecutionStatusIn"])
    types["GoogleCloudDataplexV1TaskExecutionStatusOut"] = t.struct(
        {
            "latestJob": t.proxy(renames["GoogleCloudDataplexV1JobOut"]).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TaskExecutionStatusOut"])
    types["GoogleCloudDataplexV1AssetSecurityStatusIn"] = t.struct(
        {
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetSecurityStatusIn"])
    types["GoogleCloudDataplexV1AssetSecurityStatusOut"] = t.struct(
        {
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetSecurityStatusOut"])
    types["GoogleCloudDataplexV1ListTasksResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tasks": t.array(
                t.proxy(renames["GoogleCloudDataplexV1TaskIn"])
            ).optional(),
            "unreachableLocations": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListTasksResponseIn"])
    types["GoogleCloudDataplexV1ListTasksResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tasks": t.array(
                t.proxy(renames["GoogleCloudDataplexV1TaskOut"])
            ).optional(),
            "unreachableLocations": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListTasksResponseOut"])
    types["GoogleCloudDataplexV1DataScanEventIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "jobId": t.string().optional(),
            "specVersion": t.string().optional(),
            "dataProfileConfigs": t.proxy(
                renames["GoogleCloudDataplexV1DataScanEventDataProfileAppliedConfigsIn"]
            ).optional(),
            "state": t.string().optional(),
            "dataQualityConfigs": t.proxy(
                renames["GoogleCloudDataplexV1DataScanEventDataQualityAppliedConfigsIn"]
            ).optional(),
            "dataSource": t.string().optional(),
            "dataProfile": t.proxy(
                renames["GoogleCloudDataplexV1DataScanEventDataProfileResultIn"]
            ).optional(),
            "dataQuality": t.proxy(
                renames["GoogleCloudDataplexV1DataScanEventDataQualityResultIn"]
            ).optional(),
            "message": t.string().optional(),
            "scope": t.string().optional(),
            "endTime": t.string().optional(),
            "type": t.string().optional(),
            "trigger": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanEventIn"])
    types["GoogleCloudDataplexV1DataScanEventOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "jobId": t.string().optional(),
            "specVersion": t.string().optional(),
            "dataProfileConfigs": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataScanEventDataProfileAppliedConfigsOut"
                ]
            ).optional(),
            "state": t.string().optional(),
            "dataQualityConfigs": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataScanEventDataQualityAppliedConfigsOut"
                ]
            ).optional(),
            "dataSource": t.string().optional(),
            "dataProfile": t.proxy(
                renames["GoogleCloudDataplexV1DataScanEventDataProfileResultOut"]
            ).optional(),
            "dataQuality": t.proxy(
                renames["GoogleCloudDataplexV1DataScanEventDataQualityResultOut"]
            ).optional(),
            "message": t.string().optional(),
            "scope": t.string().optional(),
            "endTime": t.string().optional(),
            "type": t.string().optional(),
            "trigger": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanEventOut"])
    types["GoogleCloudDataplexV1ScannedDataIncrementalFieldIn"] = t.struct(
        {
            "start": t.string().optional(),
            "end": t.string().optional(),
            "field": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ScannedDataIncrementalFieldIn"])
    types["GoogleCloudDataplexV1ScannedDataIncrementalFieldOut"] = t.struct(
        {
            "start": t.string().optional(),
            "end": t.string().optional(),
            "field": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ScannedDataIncrementalFieldOut"])
    types["GoogleCloudDataplexV1SessionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1SessionIn"])
    types["GoogleCloudDataplexV1SessionOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "userId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1SessionOut"])
    types["GoogleCloudDataplexV1TriggerScheduleIn"] = t.struct(
        {"cron": t.string()}
    ).named(renames["GoogleCloudDataplexV1TriggerScheduleIn"])
    types["GoogleCloudDataplexV1TriggerScheduleOut"] = t.struct(
        {"cron": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDataplexV1TriggerScheduleOut"])
    types["GoogleCloudDataplexV1DataQualityResultIn"] = t.struct(
        {
            "dimensions": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataQualityDimensionResultIn"])
            ).optional(),
            "scannedData": t.proxy(
                renames["GoogleCloudDataplexV1ScannedDataIn"]
            ).optional(),
            "rowCount": t.string().optional(),
            "passed": t.boolean().optional(),
            "rules": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataQualityRuleResultIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualityResultIn"])
    types["GoogleCloudDataplexV1DataQualityResultOut"] = t.struct(
        {
            "dimensions": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataQualityDimensionResultOut"])
            ).optional(),
            "scannedData": t.proxy(
                renames["GoogleCloudDataplexV1ScannedDataOut"]
            ).optional(),
            "rowCount": t.string().optional(),
            "passed": t.boolean().optional(),
            "rules": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataQualityRuleResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualityResultOut"])
    types["GoogleCloudDataplexV1ListDataScanJobsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "dataScanJobs": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataScanJobIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListDataScanJobsResponseIn"])
    types["GoogleCloudDataplexV1ListDataScanJobsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "dataScanJobs": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataScanJobOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListDataScanJobsResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GoogleCloudDataplexV1StorageAccessIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1StorageAccessIn"])
    types["GoogleCloudDataplexV1StorageAccessOut"] = t.struct(
        {
            "read": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1StorageAccessOut"])
    types["GoogleCloudDataplexV1ZoneDiscoverySpecIn"] = t.struct(
        {
            "includePatterns": t.array(t.string()).optional(),
            "excludePatterns": t.array(t.string()).optional(),
            "jsonOptions": t.proxy(
                renames["GoogleCloudDataplexV1ZoneDiscoverySpecJsonOptionsIn"]
            ).optional(),
            "csvOptions": t.proxy(
                renames["GoogleCloudDataplexV1ZoneDiscoverySpecCsvOptionsIn"]
            ).optional(),
            "enabled": t.boolean(),
            "schedule": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ZoneDiscoverySpecIn"])
    types["GoogleCloudDataplexV1ZoneDiscoverySpecOut"] = t.struct(
        {
            "includePatterns": t.array(t.string()).optional(),
            "excludePatterns": t.array(t.string()).optional(),
            "jsonOptions": t.proxy(
                renames["GoogleCloudDataplexV1ZoneDiscoverySpecJsonOptionsOut"]
            ).optional(),
            "csvOptions": t.proxy(
                renames["GoogleCloudDataplexV1ZoneDiscoverySpecCsvOptionsOut"]
            ).optional(),
            "enabled": t.boolean(),
            "schedule": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ZoneDiscoverySpecOut"])
    types["GoogleCloudDataplexV1EntityIn"] = t.struct(
        {
            "format": t.proxy(renames["GoogleCloudDataplexV1StorageFormatIn"]),
            "id": t.string(),
            "system": t.string(),
            "description": t.string().optional(),
            "type": t.string(),
            "asset": t.string(),
            "schema": t.proxy(renames["GoogleCloudDataplexV1SchemaIn"]),
            "dataPathPattern": t.string().optional(),
            "displayName": t.string().optional(),
            "dataPath": t.string(),
            "etag": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1EntityIn"])
    types["GoogleCloudDataplexV1EntityOut"] = t.struct(
        {
            "uid": t.string().optional(),
            "format": t.proxy(renames["GoogleCloudDataplexV1StorageFormatOut"]),
            "id": t.string(),
            "access": t.proxy(
                renames["GoogleCloudDataplexV1StorageAccessOut"]
            ).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "system": t.string(),
            "description": t.string().optional(),
            "type": t.string(),
            "updateTime": t.string().optional(),
            "asset": t.string(),
            "schema": t.proxy(renames["GoogleCloudDataplexV1SchemaOut"]),
            "dataPathPattern": t.string().optional(),
            "compatibility": t.proxy(
                renames["GoogleCloudDataplexV1EntityCompatibilityStatusOut"]
            ).optional(),
            "catalogEntry": t.string().optional(),
            "displayName": t.string().optional(),
            "dataPath": t.string(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1EntityOut"])
    types[
        "GoogleCloudDataplexV1TaskInfrastructureSpecContainerImageRuntimeIn"
    ] = t.struct(
        {
            "image": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "pythonPackages": t.array(t.string()).optional(),
            "javaJars": t.array(t.string()).optional(),
        }
    ).named(
        renames["GoogleCloudDataplexV1TaskInfrastructureSpecContainerImageRuntimeIn"]
    )
    types[
        "GoogleCloudDataplexV1TaskInfrastructureSpecContainerImageRuntimeOut"
    ] = t.struct(
        {
            "image": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "pythonPackages": t.array(t.string()).optional(),
            "javaJars": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDataplexV1TaskInfrastructureSpecContainerImageRuntimeOut"]
    )
    types["GoogleCloudDataplexV1ActionUnauthorizedResourceIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1ActionUnauthorizedResourceIn"])
    types["GoogleCloudDataplexV1ActionUnauthorizedResourceOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDataplexV1ActionUnauthorizedResourceOut"])
    types["GoogleCloudDataplexV1ScannedDataIn"] = t.struct(
        {
            "incrementalField": t.proxy(
                renames["GoogleCloudDataplexV1ScannedDataIncrementalFieldIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDataplexV1ScannedDataIn"])
    types["GoogleCloudDataplexV1ScannedDataOut"] = t.struct(
        {
            "incrementalField": t.proxy(
                renames["GoogleCloudDataplexV1ScannedDataIncrementalFieldOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ScannedDataOut"])
    types["GoogleCloudDataplexV1DataQualityRuleRowConditionExpectationIn"] = t.struct(
        {"sqlExpression": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleRowConditionExpectationIn"])
    types["GoogleCloudDataplexV1DataQualityRuleRowConditionExpectationOut"] = t.struct(
        {
            "sqlExpression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleRowConditionExpectationOut"])
    types["GoogleCloudDataplexV1AssetResourceStatusIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "message": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetResourceStatusIn"])
    types["GoogleCloudDataplexV1AssetResourceStatusOut"] = t.struct(
        {
            "managedAccessIdentity": t.string().optional(),
            "updateTime": t.string().optional(),
            "message": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetResourceStatusOut"])
    types["GoogleCloudDataplexV1DiscoveryEventEntityDetailsIn"] = t.struct(
        {"type": t.string().optional(), "entity": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1DiscoveryEventEntityDetailsIn"])
    types["GoogleCloudDataplexV1DiscoveryEventEntityDetailsOut"] = t.struct(
        {
            "type": t.string().optional(),
            "entity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DiscoveryEventEntityDetailsOut"])
    types["GoogleCloudDataplexV1ContentSqlScriptIn"] = t.struct(
        {"engine": t.string()}
    ).named(renames["GoogleCloudDataplexV1ContentSqlScriptIn"])
    types["GoogleCloudDataplexV1ContentSqlScriptOut"] = t.struct(
        {"engine": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDataplexV1ContentSqlScriptOut"])
    types["GoogleCloudDataplexV1DataQualityRuleRangeExpectationIn"] = t.struct(
        {
            "maxValue": t.string().optional(),
            "strictMaxEnabled": t.boolean().optional(),
            "strictMinEnabled": t.boolean().optional(),
            "minValue": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleRangeExpectationIn"])
    types["GoogleCloudDataplexV1DataQualityRuleRangeExpectationOut"] = t.struct(
        {
            "maxValue": t.string().optional(),
            "strictMaxEnabled": t.boolean().optional(),
            "strictMinEnabled": t.boolean().optional(),
            "minValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleRangeExpectationOut"])
    types["GoogleCloudDataplexV1DataScanIn"] = t.struct(
        {
            "dataProfileSpec": t.proxy(
                renames["GoogleCloudDataplexV1DataProfileSpecIn"]
            ).optional(),
            "data": t.proxy(renames["GoogleCloudDataplexV1DataSourceIn"]),
            "dataQualitySpec": t.proxy(
                renames["GoogleCloudDataplexV1DataQualitySpecIn"]
            ).optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "executionSpec": t.proxy(
                renames["GoogleCloudDataplexV1DataScanExecutionSpecIn"]
            ).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanIn"])
    types["GoogleCloudDataplexV1DataScanOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "dataProfileSpec": t.proxy(
                renames["GoogleCloudDataplexV1DataProfileSpecOut"]
            ).optional(),
            "state": t.string().optional(),
            "data": t.proxy(renames["GoogleCloudDataplexV1DataSourceOut"]),
            "dataQualityResult": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityResultOut"]
            ).optional(),
            "dataQualitySpec": t.proxy(
                renames["GoogleCloudDataplexV1DataQualitySpecOut"]
            ).optional(),
            "name": t.string().optional(),
            "dataProfileResult": t.proxy(
                renames["GoogleCloudDataplexV1DataProfileResultOut"]
            ).optional(),
            "uid": t.string().optional(),
            "type": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "executionSpec": t.proxy(
                renames["GoogleCloudDataplexV1DataScanExecutionSpecOut"]
            ).optional(),
            "executionStatus": t.proxy(
                renames["GoogleCloudDataplexV1DataScanExecutionStatusOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanOut"])
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
    types["GoogleCloudDataplexV1DataScanExecutionStatusIn"] = t.struct(
        {
            "latestJobEndTime": t.string().optional(),
            "latestJobStartTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanExecutionStatusIn"])
    types["GoogleCloudDataplexV1DataScanExecutionStatusOut"] = t.struct(
        {
            "latestJobEndTime": t.string().optional(),
            "latestJobStartTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanExecutionStatusOut"])
    types["GoogleCloudLocationLocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["GoogleCloudLocationLocationIn"])
    types["GoogleCloudLocationLocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudLocationLocationOut"])
    types["GoogleCloudDataplexV1ListZonesResponseIn"] = t.struct(
        {
            "zones": t.array(
                t.proxy(renames["GoogleCloudDataplexV1ZoneIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListZonesResponseIn"])
    types["GoogleCloudDataplexV1ListZonesResponseOut"] = t.struct(
        {
            "zones": t.array(
                t.proxy(renames["GoogleCloudDataplexV1ZoneOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListZonesResponseOut"])
    types["GoogleCloudDataplexV1ActionFailedSecurityPolicyApplyIn"] = t.struct(
        {"asset": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1ActionFailedSecurityPolicyApplyIn"])
    types["GoogleCloudDataplexV1ActionFailedSecurityPolicyApplyOut"] = t.struct(
        {
            "asset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ActionFailedSecurityPolicyApplyOut"])
    types["GoogleCloudDataplexV1ZoneResourceSpecIn"] = t.struct(
        {"locationType": t.string()}
    ).named(renames["GoogleCloudDataplexV1ZoneResourceSpecIn"])
    types["GoogleCloudDataplexV1ZoneResourceSpecOut"] = t.struct(
        {
            "locationType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ZoneResourceSpecOut"])
    types["GoogleCloudDataplexV1ListAssetsResponseIn"] = t.struct(
        {
            "assets": t.array(
                t.proxy(renames["GoogleCloudDataplexV1AssetIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListAssetsResponseIn"])
    types["GoogleCloudDataplexV1ListAssetsResponseOut"] = t.struct(
        {
            "assets": t.array(
                t.proxy(renames["GoogleCloudDataplexV1AssetOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListAssetsResponseOut"])
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
    types["GoogleCloudDataplexV1DataQualityRuleTableConditionExpectationIn"] = t.struct(
        {"sqlExpression": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleTableConditionExpectationIn"])
    types[
        "GoogleCloudDataplexV1DataQualityRuleTableConditionExpectationOut"
    ] = t.struct(
        {
            "sqlExpression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDataplexV1DataQualityRuleTableConditionExpectationOut"]
    )
    types["GoogleCloudDataplexV1PartitionIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "location": t.string(),
            "values": t.array(t.string()),
        }
    ).named(renames["GoogleCloudDataplexV1PartitionIn"])
    types["GoogleCloudDataplexV1PartitionOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "location": t.string(),
            "values": t.array(t.string()),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1PartitionOut"])
    types["GoogleCloudDataplexV1ZoneDiscoverySpecCsvOptionsIn"] = t.struct(
        {
            "disableTypeInference": t.boolean().optional(),
            "encoding": t.string().optional(),
            "headerRows": t.integer().optional(),
            "delimiter": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ZoneDiscoverySpecCsvOptionsIn"])
    types["GoogleCloudDataplexV1ZoneDiscoverySpecCsvOptionsOut"] = t.struct(
        {
            "disableTypeInference": t.boolean().optional(),
            "encoding": t.string().optional(),
            "headerRows": t.integer().optional(),
            "delimiter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ZoneDiscoverySpecCsvOptionsOut"])
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
    types["GoogleCloudDataplexV1DataQualityRuleNonNullExpectationIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleNonNullExpectationIn"])
    types["GoogleCloudDataplexV1DataQualityRuleNonNullExpectationOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleNonNullExpectationOut"])
    types["GoogleCloudDataplexV1ActionMissingDataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1ActionMissingDataIn"])
    types["GoogleCloudDataplexV1ActionMissingDataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDataplexV1ActionMissingDataOut"])
    types["GoogleCloudDataplexV1DataAttributeBindingPathIn"] = t.struct(
        {"attributes": t.array(t.string()).optional(), "name": t.string()}
    ).named(renames["GoogleCloudDataplexV1DataAttributeBindingPathIn"])
    types["GoogleCloudDataplexV1DataAttributeBindingPathOut"] = t.struct(
        {
            "attributes": t.array(t.string()).optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataAttributeBindingPathOut"])
    types["GoogleCloudDataplexV1ListSessionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "sessions": t.array(
                t.proxy(renames["GoogleCloudDataplexV1SessionIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListSessionsResponseIn"])
    types["GoogleCloudDataplexV1ListSessionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "sessions": t.array(
                t.proxy(renames["GoogleCloudDataplexV1SessionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListSessionsResponseOut"])
    types["GoogleCloudDataplexV1ActionInvalidDataOrganizationIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1ActionInvalidDataOrganizationIn"])
    types["GoogleCloudDataplexV1ActionInvalidDataOrganizationOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDataplexV1ActionInvalidDataOrganizationOut"])
    types["GoogleCloudDataplexV1EnvironmentIn"] = t.struct(
        {
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "infrastructureSpec": t.proxy(
                renames["GoogleCloudDataplexV1EnvironmentInfrastructureSpecIn"]
            ),
            "sessionSpec": t.proxy(
                renames["GoogleCloudDataplexV1EnvironmentSessionSpecIn"]
            ).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1EnvironmentIn"])
    types["GoogleCloudDataplexV1EnvironmentOut"] = t.struct(
        {
            "endpoints": t.proxy(
                renames["GoogleCloudDataplexV1EnvironmentEndpointsOut"]
            ).optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "infrastructureSpec": t.proxy(
                renames["GoogleCloudDataplexV1EnvironmentInfrastructureSpecOut"]
            ),
            "sessionSpec": t.proxy(
                renames["GoogleCloudDataplexV1EnvironmentSessionSpecOut"]
            ).optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "uid": t.string().optional(),
            "displayName": t.string().optional(),
            "sessionStatus": t.proxy(
                renames["GoogleCloudDataplexV1EnvironmentSessionStatusOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1EnvironmentOut"])
    types["GoogleCloudDataplexV1SchemaIn"] = t.struct(
        {
            "partitionFields": t.array(
                t.proxy(renames["GoogleCloudDataplexV1SchemaPartitionFieldIn"])
            ).optional(),
            "userManaged": t.boolean(),
            "fields": t.array(
                t.proxy(renames["GoogleCloudDataplexV1SchemaSchemaFieldIn"])
            ).optional(),
            "partitionStyle": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1SchemaIn"])
    types["GoogleCloudDataplexV1SchemaOut"] = t.struct(
        {
            "partitionFields": t.array(
                t.proxy(renames["GoogleCloudDataplexV1SchemaPartitionFieldOut"])
            ).optional(),
            "userManaged": t.boolean(),
            "fields": t.array(
                t.proxy(renames["GoogleCloudDataplexV1SchemaSchemaFieldOut"])
            ).optional(),
            "partitionStyle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1SchemaOut"])
    types["GoogleCloudDataplexV1TaskIn"] = t.struct(
        {
            "triggerSpec": t.proxy(renames["GoogleCloudDataplexV1TaskTriggerSpecIn"]),
            "spark": t.proxy(
                renames["GoogleCloudDataplexV1TaskSparkTaskConfigIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "notebook": t.proxy(
                renames["GoogleCloudDataplexV1TaskNotebookTaskConfigIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "executionSpec": t.proxy(
                renames["GoogleCloudDataplexV1TaskExecutionSpecIn"]
            ),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TaskIn"])
    types["GoogleCloudDataplexV1TaskOut"] = t.struct(
        {
            "triggerSpec": t.proxy(renames["GoogleCloudDataplexV1TaskTriggerSpecOut"]),
            "spark": t.proxy(
                renames["GoogleCloudDataplexV1TaskSparkTaskConfigOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "notebook": t.proxy(
                renames["GoogleCloudDataplexV1TaskNotebookTaskConfigOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "uid": t.string().optional(),
            "updateTime": t.string().optional(),
            "executionStatus": t.proxy(
                renames["GoogleCloudDataplexV1TaskExecutionStatusOut"]
            ).optional(),
            "state": t.string().optional(),
            "executionSpec": t.proxy(
                renames["GoogleCloudDataplexV1TaskExecutionSpecOut"]
            ),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TaskOut"])
    types[
        "GoogleCloudDataplexV1EnvironmentInfrastructureSpecComputeResourcesIn"
    ] = t.struct(
        {
            "diskSizeGb": t.integer().optional(),
            "nodeCount": t.integer().optional(),
            "maxNodeCount": t.integer().optional(),
        }
    ).named(
        renames["GoogleCloudDataplexV1EnvironmentInfrastructureSpecComputeResourcesIn"]
    )
    types[
        "GoogleCloudDataplexV1EnvironmentInfrastructureSpecComputeResourcesOut"
    ] = t.struct(
        {
            "diskSizeGb": t.integer().optional(),
            "nodeCount": t.integer().optional(),
            "maxNodeCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDataplexV1EnvironmentInfrastructureSpecComputeResourcesOut"]
    )
    types["GoogleCloudDataplexV1DiscoveryEventPartitionDetailsIn"] = t.struct(
        {
            "type": t.string().optional(),
            "entity": t.string().optional(),
            "partition": t.string().optional(),
            "sampledDataLocations": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DiscoveryEventPartitionDetailsIn"])
    types["GoogleCloudDataplexV1DiscoveryEventPartitionDetailsOut"] = t.struct(
        {
            "type": t.string().optional(),
            "entity": t.string().optional(),
            "partition": t.string().optional(),
            "sampledDataLocations": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DiscoveryEventPartitionDetailsOut"])
    types["GoogleCloudDataplexV1DiscoveryEventConfigDetailsIn"] = t.struct(
        {"parameters": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudDataplexV1DiscoveryEventConfigDetailsIn"])
    types["GoogleCloudDataplexV1DiscoveryEventConfigDetailsOut"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DiscoveryEventConfigDetailsOut"])
    types["GoogleCloudDataplexV1ListJobsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "jobs": t.array(t.proxy(renames["GoogleCloudDataplexV1JobIn"])).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListJobsResponseIn"])
    types["GoogleCloudDataplexV1ListJobsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "jobs": t.array(t.proxy(renames["GoogleCloudDataplexV1JobOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListJobsResponseOut"])
    types["GoogleCloudDataplexV1AssetDiscoveryStatusStatsIn"] = t.struct(
        {
            "dataSize": t.string().optional(),
            "dataItems": t.string().optional(),
            "tables": t.string().optional(),
            "filesets": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetDiscoveryStatusStatsIn"])
    types["GoogleCloudDataplexV1AssetDiscoveryStatusStatsOut"] = t.struct(
        {
            "dataSize": t.string().optional(),
            "dataItems": t.string().optional(),
            "tables": t.string().optional(),
            "filesets": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetDiscoveryStatusStatsOut"])
    types["GoogleCloudDataplexV1DataAttributeIn"] = t.struct(
        {
            "parentId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "dataAccessSpec": t.proxy(
                renames["GoogleCloudDataplexV1DataAccessSpecIn"]
            ).optional(),
            "description": t.string().optional(),
            "etag": t.string().optional(),
            "resourceAccessSpec": t.proxy(
                renames["GoogleCloudDataplexV1ResourceAccessSpecIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataAttributeIn"])
    types["GoogleCloudDataplexV1DataAttributeOut"] = t.struct(
        {
            "parentId": t.string().optional(),
            "uid": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "dataAccessSpec": t.proxy(
                renames["GoogleCloudDataplexV1DataAccessSpecOut"]
            ).optional(),
            "description": t.string().optional(),
            "etag": t.string().optional(),
            "resourceAccessSpec": t.proxy(
                renames["GoogleCloudDataplexV1ResourceAccessSpecOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "attributeCount": t.integer().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataAttributeOut"])
    types["GoogleCloudDataplexV1ContentIn"] = t.struct(
        {
            "sqlScript": t.proxy(
                renames["GoogleCloudDataplexV1ContentSqlScriptIn"]
            ).optional(),
            "description": t.string().optional(),
            "notebook": t.proxy(
                renames["GoogleCloudDataplexV1ContentNotebookIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "path": t.string(),
            "dataText": t.string(),
        }
    ).named(renames["GoogleCloudDataplexV1ContentIn"])
    types["GoogleCloudDataplexV1ContentOut"] = t.struct(
        {
            "sqlScript": t.proxy(
                renames["GoogleCloudDataplexV1ContentSqlScriptOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "notebook": t.proxy(
                renames["GoogleCloudDataplexV1ContentNotebookOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "uid": t.string().optional(),
            "path": t.string(),
            "dataText": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ContentOut"])
    types["GoogleCloudDataplexV1AssetDiscoverySpecCsvOptionsIn"] = t.struct(
        {
            "disableTypeInference": t.boolean().optional(),
            "encoding": t.string().optional(),
            "delimiter": t.string().optional(),
            "headerRows": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetDiscoverySpecCsvOptionsIn"])
    types["GoogleCloudDataplexV1AssetDiscoverySpecCsvOptionsOut"] = t.struct(
        {
            "disableTypeInference": t.boolean().optional(),
            "encoding": t.string().optional(),
            "delimiter": t.string().optional(),
            "headerRows": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetDiscoverySpecCsvOptionsOut"])
    types["GoogleCloudDataplexV1TaskExecutionSpecIn"] = t.struct(
        {
            "args": t.struct({"_": t.string().optional()}).optional(),
            "maxJobExecutionLifetime": t.string().optional(),
            "project": t.string().optional(),
            "serviceAccount": t.string(),
            "kmsKey": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TaskExecutionSpecIn"])
    types["GoogleCloudDataplexV1TaskExecutionSpecOut"] = t.struct(
        {
            "args": t.struct({"_": t.string().optional()}).optional(),
            "maxJobExecutionLifetime": t.string().optional(),
            "project": t.string().optional(),
            "serviceAccount": t.string(),
            "kmsKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TaskExecutionSpecOut"])
    types[
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoStringFieldInfoIn"
    ] = t.struct(
        {
            "minLength": t.string().optional(),
            "maxLength": t.string().optional(),
            "averageLength": t.number().optional(),
        }
    ).named(
        renames[
            "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoStringFieldInfoIn"
        ]
    )
    types[
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoStringFieldInfoOut"
    ] = t.struct(
        {
            "minLength": t.string().optional(),
            "maxLength": t.string().optional(),
            "averageLength": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoStringFieldInfoOut"
        ]
    )
    types["GoogleCloudDataplexV1LakeMetastoreIn"] = t.struct(
        {"service": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1LakeMetastoreIn"])
    types["GoogleCloudDataplexV1LakeMetastoreOut"] = t.struct(
        {
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1LakeMetastoreOut"])
    types[
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoDoubleFieldInfoIn"
    ] = t.struct(
        {
            "min": t.number().optional(),
            "quartiles": t.array(t.number()).optional(),
            "standardDeviation": t.number().optional(),
            "average": t.number().optional(),
            "max": t.number().optional(),
        }
    ).named(
        renames[
            "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoDoubleFieldInfoIn"
        ]
    )
    types[
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoDoubleFieldInfoOut"
    ] = t.struct(
        {
            "min": t.number().optional(),
            "quartiles": t.array(t.number()).optional(),
            "standardDeviation": t.number().optional(),
            "average": t.number().optional(),
            "max": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoDoubleFieldInfoOut"
        ]
    )
    types["GoogleCloudDataplexV1ListDataAttributesResponseIn"] = t.struct(
        {
            "unreachableLocations": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "dataAttributes": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataAttributeIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListDataAttributesResponseIn"])
    types["GoogleCloudDataplexV1ListDataAttributesResponseOut"] = t.struct(
        {
            "unreachableLocations": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "dataAttributes": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataAttributeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListDataAttributesResponseOut"])
    types["GoogleCloudDataplexV1ListPartitionsResponseIn"] = t.struct(
        {
            "partitions": t.array(
                t.proxy(renames["GoogleCloudDataplexV1PartitionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListPartitionsResponseIn"])
    types["GoogleCloudDataplexV1ListPartitionsResponseOut"] = t.struct(
        {
            "partitions": t.array(
                t.proxy(renames["GoogleCloudDataplexV1PartitionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListPartitionsResponseOut"])
    types["GoogleCloudDataplexV1ZoneIn"] = t.struct(
        {
            "type": t.string(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "discoverySpec": t.proxy(
                renames["GoogleCloudDataplexV1ZoneDiscoverySpecIn"]
            ).optional(),
            "resourceSpec": t.proxy(renames["GoogleCloudDataplexV1ZoneResourceSpecIn"]),
        }
    ).named(renames["GoogleCloudDataplexV1ZoneIn"])
    types["GoogleCloudDataplexV1ZoneOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "type": t.string(),
            "state": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "discoverySpec": t.proxy(
                renames["GoogleCloudDataplexV1ZoneDiscoverySpecOut"]
            ).optional(),
            "resourceSpec": t.proxy(
                renames["GoogleCloudDataplexV1ZoneResourceSpecOut"]
            ),
            "assetStatus": t.proxy(
                renames["GoogleCloudDataplexV1AssetStatusOut"]
            ).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ZoneOut"])
    types["GoogleIamV1TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsResponseIn"])
    types["GoogleIamV1TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsResponseOut"])
    types["GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIn"] = t.struct(
        {
            "nullRatio": t.number().optional(),
            "topNValues": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoTopNValueIn"
                    ]
                )
            ).optional(),
            "stringProfile": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoStringFieldInfoIn"
                ]
            ).optional(),
            "distinctRatio": t.number().optional(),
            "integerProfile": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIntegerFieldInfoIn"
                ]
            ).optional(),
            "doubleProfile": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoDoubleFieldInfoIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIn"])
    types[
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoOut"
    ] = t.struct(
        {
            "nullRatio": t.number().optional(),
            "topNValues": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoTopNValueOut"
                    ]
                )
            ).optional(),
            "stringProfile": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoStringFieldInfoOut"
                ]
            ).optional(),
            "distinctRatio": t.number().optional(),
            "integerProfile": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIntegerFieldInfoOut"
                ]
            ).optional(),
            "doubleProfile": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoDoubleFieldInfoOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoOut"]
    )
    types["GoogleCloudDataplexV1SessionEventIn"] = t.struct(
        {
            "query": t.proxy(
                renames["GoogleCloudDataplexV1SessionEventQueryDetailIn"]
            ).optional(),
            "userId": t.string().optional(),
            "type": t.string().optional(),
            "eventSucceeded": t.boolean().optional(),
            "sessionId": t.string().optional(),
            "unassignedDuration": t.string().optional(),
            "fastStartupEnabled": t.boolean().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1SessionEventIn"])
    types["GoogleCloudDataplexV1SessionEventOut"] = t.struct(
        {
            "query": t.proxy(
                renames["GoogleCloudDataplexV1SessionEventQueryDetailOut"]
            ).optional(),
            "userId": t.string().optional(),
            "type": t.string().optional(),
            "eventSucceeded": t.boolean().optional(),
            "sessionId": t.string().optional(),
            "unassignedDuration": t.string().optional(),
            "fastStartupEnabled": t.boolean().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1SessionEventOut"])
    types["GoogleCloudDataplexV1ListDataScansResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "dataScans": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataScanIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListDataScansResponseIn"])
    types["GoogleCloudDataplexV1ListDataScansResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "dataScans": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataScanOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListDataScansResponseOut"])
    types["GoogleIamV1PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingIn"])).optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigIn"])
            ).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["GoogleIamV1PolicyIn"])
    types["GoogleIamV1PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingOut"])).optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigOut"])
            ).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1PolicyOut"])
    types["GoogleCloudDataplexV1DiscoveryEventActionDetailsIn"] = t.struct(
        {"type": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1DiscoveryEventActionDetailsIn"])
    types["GoogleCloudDataplexV1DiscoveryEventActionDetailsOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DiscoveryEventActionDetailsOut"])
    types["GoogleCloudDataplexV1DataScanEventDataProfileResultIn"] = t.struct(
        {"rowCount": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1DataScanEventDataProfileResultIn"])
    types["GoogleCloudDataplexV1DataScanEventDataProfileResultOut"] = t.struct(
        {
            "rowCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanEventDataProfileResultOut"])
    types["GoogleCloudDataplexV1RunTaskResponseIn"] = t.struct(
        {"job": t.proxy(renames["GoogleCloudDataplexV1JobIn"]).optional()}
    ).named(renames["GoogleCloudDataplexV1RunTaskResponseIn"])
    types["GoogleCloudDataplexV1RunTaskResponseOut"] = t.struct(
        {
            "job": t.proxy(renames["GoogleCloudDataplexV1JobOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1RunTaskResponseOut"])
    types["GoogleCloudDataplexV1ActionInvalidDataFormatIn"] = t.struct(
        {
            "expectedFormat": t.string().optional(),
            "sampledDataLocations": t.array(t.string()).optional(),
            "newFormat": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ActionInvalidDataFormatIn"])
    types["GoogleCloudDataplexV1ActionInvalidDataFormatOut"] = t.struct(
        {
            "expectedFormat": t.string().optional(),
            "sampledDataLocations": t.array(t.string()).optional(),
            "newFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ActionInvalidDataFormatOut"])
    types["GoogleCloudDataplexV1ActionMissingResourceIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1ActionMissingResourceIn"])
    types["GoogleCloudDataplexV1ActionMissingResourceOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDataplexV1ActionMissingResourceOut"])
    types["GoogleCloudDataplexV1DataAttributeBindingIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "attributes": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "paths": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataAttributeBindingPathIn"])
            ).optional(),
            "resource": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataAttributeBindingIn"])
    types["GoogleCloudDataplexV1DataAttributeBindingOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "attributes": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "uid": t.string().optional(),
            "displayName": t.string().optional(),
            "paths": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataAttributeBindingPathOut"])
            ).optional(),
            "resource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataAttributeBindingOut"])
    types["GoogleCloudDataplexV1AssetDiscoveryStatusIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "lastRunDuration": t.string().optional(),
            "stats": t.proxy(
                renames["GoogleCloudDataplexV1AssetDiscoveryStatusStatsIn"]
            ).optional(),
            "state": t.string().optional(),
            "lastRunTime": t.string().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetDiscoveryStatusIn"])
    types["GoogleCloudDataplexV1AssetDiscoveryStatusOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "lastRunDuration": t.string().optional(),
            "stats": t.proxy(
                renames["GoogleCloudDataplexV1AssetDiscoveryStatusStatsOut"]
            ).optional(),
            "state": t.string().optional(),
            "lastRunTime": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetDiscoveryStatusOut"])
    types["GoogleCloudDataplexV1DataQualityRuleResultIn"] = t.struct(
        {
            "rule": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityRuleIn"]
            ).optional(),
            "evaluatedCount": t.string().optional(),
            "passRatio": t.number().optional(),
            "nullCount": t.string().optional(),
            "passedCount": t.string().optional(),
            "passed": t.boolean().optional(),
            "failingRowsQuery": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleResultIn"])
    types["GoogleCloudDataplexV1DataQualityRuleResultOut"] = t.struct(
        {
            "rule": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityRuleOut"]
            ).optional(),
            "evaluatedCount": t.string().optional(),
            "passRatio": t.number().optional(),
            "nullCount": t.string().optional(),
            "passedCount": t.string().optional(),
            "passed": t.boolean().optional(),
            "failingRowsQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleResultOut"])
    types["GoogleCloudDataplexV1ZoneDiscoverySpecJsonOptionsIn"] = t.struct(
        {
            "disableTypeInference": t.boolean().optional(),
            "encoding": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ZoneDiscoverySpecJsonOptionsIn"])
    types["GoogleCloudDataplexV1ZoneDiscoverySpecJsonOptionsOut"] = t.struct(
        {
            "disableTypeInference": t.boolean().optional(),
            "encoding": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ZoneDiscoverySpecJsonOptionsOut"])
    types["GoogleCloudDataplexV1LakeIn"] = t.struct(
        {
            "metastore": t.proxy(
                renames["GoogleCloudDataplexV1LakeMetastoreIn"]
            ).optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1LakeIn"])
    types["GoogleCloudDataplexV1LakeOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "uid": t.string().optional(),
            "metastore": t.proxy(
                renames["GoogleCloudDataplexV1LakeMetastoreOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "assetStatus": t.proxy(
                renames["GoogleCloudDataplexV1AssetStatusOut"]
            ).optional(),
            "metastoreStatus": t.proxy(
                renames["GoogleCloudDataplexV1LakeMetastoreStatusOut"]
            ).optional(),
            "name": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1LakeOut"])
    types["GoogleCloudDataplexV1TaskInfrastructureSpecIn"] = t.struct(
        {
            "containerImage": t.proxy(
                renames[
                    "GoogleCloudDataplexV1TaskInfrastructureSpecContainerImageRuntimeIn"
                ]
            ).optional(),
            "vpcNetwork": t.proxy(
                renames["GoogleCloudDataplexV1TaskInfrastructureSpecVpcNetworkIn"]
            ).optional(),
            "batch": t.proxy(
                renames[
                    "GoogleCloudDataplexV1TaskInfrastructureSpecBatchComputeResourcesIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TaskInfrastructureSpecIn"])
    types["GoogleCloudDataplexV1TaskInfrastructureSpecOut"] = t.struct(
        {
            "containerImage": t.proxy(
                renames[
                    "GoogleCloudDataplexV1TaskInfrastructureSpecContainerImageRuntimeOut"
                ]
            ).optional(),
            "vpcNetwork": t.proxy(
                renames["GoogleCloudDataplexV1TaskInfrastructureSpecVpcNetworkOut"]
            ).optional(),
            "batch": t.proxy(
                renames[
                    "GoogleCloudDataplexV1TaskInfrastructureSpecBatchComputeResourcesOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TaskInfrastructureSpecOut"])
    types["GoogleCloudDataplexV1DataProfileResultProfileFieldIn"] = t.struct(
        {
            "profile": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIn"
                ]
            ).optional(),
            "name": t.string().optional(),
            "mode": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataProfileResultProfileFieldIn"])
    types["GoogleCloudDataplexV1DataProfileResultProfileFieldOut"] = t.struct(
        {
            "profile": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoOut"
                ]
            ).optional(),
            "name": t.string().optional(),
            "mode": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataProfileResultProfileFieldOut"])
    types["GoogleCloudDataplexV1StorageFormatIcebergOptionsIn"] = t.struct(
        {"metadataLocation": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1StorageFormatIcebergOptionsIn"])
    types["GoogleCloudDataplexV1StorageFormatIcebergOptionsOut"] = t.struct(
        {
            "metadataLocation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1StorageFormatIcebergOptionsOut"])
    types["GoogleCloudDataplexV1OperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1OperationMetadataIn"])
    types["GoogleCloudDataplexV1OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "statusMessage": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1OperationMetadataOut"])
    types["GoogleCloudDataplexV1RunDataScanRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1RunDataScanRequestIn"])
    types["GoogleCloudDataplexV1RunDataScanRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDataplexV1RunDataScanRequestOut"])
    types["GoogleCloudDataplexV1ActionIncompatibleDataSchemaIn"] = t.struct(
        {
            "sampledDataLocations": t.array(t.string()).optional(),
            "schemaChange": t.string().optional(),
            "existingSchema": t.string().optional(),
            "newSchema": t.string().optional(),
            "table": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ActionIncompatibleDataSchemaIn"])
    types["GoogleCloudDataplexV1ActionIncompatibleDataSchemaOut"] = t.struct(
        {
            "sampledDataLocations": t.array(t.string()).optional(),
            "schemaChange": t.string().optional(),
            "existingSchema": t.string().optional(),
            "newSchema": t.string().optional(),
            "table": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ActionIncompatibleDataSchemaOut"])
    types["GoogleCloudDataplexV1DataQualityRuleSetExpectationIn"] = t.struct(
        {"values": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleSetExpectationIn"])
    types["GoogleCloudDataplexV1DataQualityRuleSetExpectationOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleSetExpectationOut"])
    types["GoogleCloudDataplexV1ListActionsResponseIn"] = t.struct(
        {
            "actions": t.array(
                t.proxy(renames["GoogleCloudDataplexV1ActionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListActionsResponseIn"])
    types["GoogleCloudDataplexV1ListActionsResponseOut"] = t.struct(
        {
            "actions": t.array(
                t.proxy(renames["GoogleCloudDataplexV1ActionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListActionsResponseOut"])
    types["GoogleCloudDataplexV1CancelJobRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1CancelJobRequestIn"])
    types["GoogleCloudDataplexV1CancelJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDataplexV1CancelJobRequestOut"])
    types["GoogleCloudDataplexV1RunTaskRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1RunTaskRequestIn"])
    types["GoogleCloudDataplexV1RunTaskRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDataplexV1RunTaskRequestOut"])
    types["GoogleCloudDataplexV1EntityCompatibilityStatusIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1EntityCompatibilityStatusIn"])
    types["GoogleCloudDataplexV1EntityCompatibilityStatusOut"] = t.struct(
        {
            "hiveMetastore": t.proxy(
                renames[
                    "GoogleCloudDataplexV1EntityCompatibilityStatusCompatibilityOut"
                ]
            ).optional(),
            "bigquery": t.proxy(
                renames[
                    "GoogleCloudDataplexV1EntityCompatibilityStatusCompatibilityOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1EntityCompatibilityStatusOut"])
    types["GoogleTypeExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["GoogleTypeExprIn"])
    types["GoogleTypeExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeExprOut"])
    types["GoogleCloudDataplexV1AssetDiscoverySpecJsonOptionsIn"] = t.struct(
        {
            "encoding": t.string().optional(),
            "disableTypeInference": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetDiscoverySpecJsonOptionsIn"])
    types["GoogleCloudDataplexV1AssetDiscoverySpecJsonOptionsOut"] = t.struct(
        {
            "encoding": t.string().optional(),
            "disableTypeInference": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetDiscoverySpecJsonOptionsOut"])
    types["GoogleCloudDataplexV1JobEventIn"] = t.struct(
        {
            "state": t.string().optional(),
            "message": t.string().optional(),
            "service": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "type": t.string().optional(),
            "serviceJob": t.string().optional(),
            "jobId": t.string().optional(),
            "retries": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1JobEventIn"])
    types["GoogleCloudDataplexV1JobEventOut"] = t.struct(
        {
            "state": t.string().optional(),
            "message": t.string().optional(),
            "service": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "type": t.string().optional(),
            "serviceJob": t.string().optional(),
            "jobId": t.string().optional(),
            "retries": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1JobEventOut"])
    types["GoogleCloudDataplexV1SessionEventQueryDetailIn"] = t.struct(
        {
            "resultSizeBytes": t.string().optional(),
            "duration": t.string().optional(),
            "queryId": t.string().optional(),
            "queryText": t.string().optional(),
            "engine": t.string().optional(),
            "dataProcessedBytes": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1SessionEventQueryDetailIn"])
    types["GoogleCloudDataplexV1SessionEventQueryDetailOut"] = t.struct(
        {
            "resultSizeBytes": t.string().optional(),
            "duration": t.string().optional(),
            "queryId": t.string().optional(),
            "queryText": t.string().optional(),
            "engine": t.string().optional(),
            "dataProcessedBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1SessionEventQueryDetailOut"])
    types[
        "GoogleCloudDataplexV1TaskInfrastructureSpecBatchComputeResourcesIn"
    ] = t.struct(
        {
            "maxExecutorsCount": t.integer().optional(),
            "executorsCount": t.integer().optional(),
        }
    ).named(
        renames["GoogleCloudDataplexV1TaskInfrastructureSpecBatchComputeResourcesIn"]
    )
    types[
        "GoogleCloudDataplexV1TaskInfrastructureSpecBatchComputeResourcesOut"
    ] = t.struct(
        {
            "maxExecutorsCount": t.integer().optional(),
            "executorsCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDataplexV1TaskInfrastructureSpecBatchComputeResourcesOut"]
    )
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
    types["GoogleCloudDataplexV1AssetIn"] = t.struct(
        {
            "resourceSpec": t.proxy(
                renames["GoogleCloudDataplexV1AssetResourceSpecIn"]
            ),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "discoverySpec": t.proxy(
                renames["GoogleCloudDataplexV1AssetDiscoverySpecIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetIn"])
    types["GoogleCloudDataplexV1AssetOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "resourceSpec": t.proxy(
                renames["GoogleCloudDataplexV1AssetResourceSpecOut"]
            ),
            "displayName": t.string().optional(),
            "uid": t.string().optional(),
            "description": t.string().optional(),
            "discoverySpec": t.proxy(
                renames["GoogleCloudDataplexV1AssetDiscoverySpecOut"]
            ).optional(),
            "discoveryStatus": t.proxy(
                renames["GoogleCloudDataplexV1AssetDiscoveryStatusOut"]
            ).optional(),
            "resourceStatus": t.proxy(
                renames["GoogleCloudDataplexV1AssetResourceStatusOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "securityStatus": t.proxy(
                renames["GoogleCloudDataplexV1AssetSecurityStatusOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetOut"])
    types["GoogleCloudDataplexV1ListEnvironmentsResponseIn"] = t.struct(
        {
            "environments": t.array(
                t.proxy(renames["GoogleCloudDataplexV1EnvironmentIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListEnvironmentsResponseIn"])
    types["GoogleCloudDataplexV1ListEnvironmentsResponseOut"] = t.struct(
        {
            "environments": t.array(
                t.proxy(renames["GoogleCloudDataplexV1EnvironmentOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListEnvironmentsResponseOut"])
    types["GoogleCloudDataplexV1AssetStatusIn"] = t.struct(
        {
            "securityPolicyApplyingAssets": t.integer().optional(),
            "activeAssets": t.integer().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetStatusIn"])
    types["GoogleCloudDataplexV1AssetStatusOut"] = t.struct(
        {
            "securityPolicyApplyingAssets": t.integer().optional(),
            "activeAssets": t.integer().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetStatusOut"])
    types["GoogleCloudDataplexV1AssetResourceSpecIn"] = t.struct(
        {
            "type": t.string(),
            "name": t.string().optional(),
            "readAccessMode": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetResourceSpecIn"])
    types["GoogleCloudDataplexV1AssetResourceSpecOut"] = t.struct(
        {
            "type": t.string(),
            "name": t.string().optional(),
            "readAccessMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetResourceSpecOut"])
    types["GoogleCloudDataplexV1DataTaxonomyIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "etag": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataTaxonomyIn"])
    types["GoogleCloudDataplexV1DataTaxonomyOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "updateTime": t.string().optional(),
            "uid": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "attributeCount": t.integer().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataTaxonomyOut"])
    types["GoogleCloudDataplexV1DataScanEventDataProfileAppliedConfigsIn"] = t.struct(
        {
            "rowFilterApplied": t.boolean().optional(),
            "samplingPercent": t.number().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanEventDataProfileAppliedConfigsIn"])
    types["GoogleCloudDataplexV1DataScanEventDataProfileAppliedConfigsOut"] = t.struct(
        {
            "rowFilterApplied": t.boolean().optional(),
            "samplingPercent": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanEventDataProfileAppliedConfigsOut"])
    types["GoogleCloudDataplexV1ListEntitiesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDataplexV1EntityIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListEntitiesResponseIn"])
    types["GoogleCloudDataplexV1ListEntitiesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDataplexV1EntityOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListEntitiesResponseOut"])
    types["GoogleCloudDataplexV1DataQualitySpecIn"] = t.struct(
        {
            "rowFilter": t.string().optional(),
            "samplingPercent": t.number().optional(),
            "rules": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataQualityRuleIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualitySpecIn"])
    types["GoogleCloudDataplexV1DataQualitySpecOut"] = t.struct(
        {
            "rowFilter": t.string().optional(),
            "samplingPercent": t.number().optional(),
            "rules": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataQualityRuleOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualitySpecOut"])
    types["GoogleCloudDataplexV1SchemaPartitionFieldIn"] = t.struct(
        {"name": t.string(), "type": t.string()}
    ).named(renames["GoogleCloudDataplexV1SchemaPartitionFieldIn"])
    types["GoogleCloudDataplexV1SchemaPartitionFieldOut"] = t.struct(
        {
            "name": t.string(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1SchemaPartitionFieldOut"])
    types[
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIntegerFieldInfoIn"
    ] = t.struct(
        {
            "max": t.string().optional(),
            "standardDeviation": t.number().optional(),
            "average": t.number().optional(),
            "quartiles": t.array(t.string()).optional(),
            "min": t.string().optional(),
        }
    ).named(
        renames[
            "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIntegerFieldInfoIn"
        ]
    )
    types[
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIntegerFieldInfoOut"
    ] = t.struct(
        {
            "max": t.string().optional(),
            "standardDeviation": t.number().optional(),
            "average": t.number().optional(),
            "quartiles": t.array(t.string()).optional(),
            "min": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIntegerFieldInfoOut"
        ]
    )
    types["GoogleCloudDataplexV1ActionInvalidDataPartitionIn"] = t.struct(
        {"expectedStructure": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1ActionInvalidDataPartitionIn"])
    types["GoogleCloudDataplexV1ActionInvalidDataPartitionOut"] = t.struct(
        {
            "expectedStructure": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ActionInvalidDataPartitionOut"])
    types["GoogleCloudDataplexV1EnvironmentSessionSpecIn"] = t.struct(
        {
            "enableFastStartup": t.boolean().optional(),
            "maxIdleDuration": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1EnvironmentSessionSpecIn"])
    types["GoogleCloudDataplexV1EnvironmentSessionSpecOut"] = t.struct(
        {
            "enableFastStartup": t.boolean().optional(),
            "maxIdleDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1EnvironmentSessionSpecOut"])
    types["GoogleCloudDataplexV1DataAccessSpecIn"] = t.struct(
        {"readers": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudDataplexV1DataAccessSpecIn"])
    types["GoogleCloudDataplexV1DataAccessSpecOut"] = t.struct(
        {
            "readers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataAccessSpecOut"])
    types["GoogleCloudDataplexV1SchemaSchemaFieldIn"] = t.struct(
        {
            "type": t.string(),
            "description": t.string().optional(),
            "fields": t.array(
                t.proxy(renames["GoogleCloudDataplexV1SchemaSchemaFieldIn"])
            ).optional(),
            "name": t.string(),
            "mode": t.string(),
        }
    ).named(renames["GoogleCloudDataplexV1SchemaSchemaFieldIn"])
    types["GoogleCloudDataplexV1SchemaSchemaFieldOut"] = t.struct(
        {
            "type": t.string(),
            "description": t.string().optional(),
            "fields": t.array(
                t.proxy(renames["GoogleCloudDataplexV1SchemaSchemaFieldOut"])
            ).optional(),
            "name": t.string(),
            "mode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1SchemaSchemaFieldOut"])
    types["GoogleCloudDataplexV1ContentNotebookIn"] = t.struct(
        {"kernelType": t.string()}
    ).named(renames["GoogleCloudDataplexV1ContentNotebookIn"])
    types["GoogleCloudDataplexV1ContentNotebookOut"] = t.struct(
        {
            "kernelType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ContentNotebookOut"])
    types["GoogleCloudDataplexV1EnvironmentInfrastructureSpecIn"] = t.struct(
        {
            "osImage": t.proxy(
                renames[
                    "GoogleCloudDataplexV1EnvironmentInfrastructureSpecOsImageRuntimeIn"
                ]
            ),
            "compute": t.proxy(
                renames[
                    "GoogleCloudDataplexV1EnvironmentInfrastructureSpecComputeResourcesIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1EnvironmentInfrastructureSpecIn"])
    types["GoogleCloudDataplexV1EnvironmentInfrastructureSpecOut"] = t.struct(
        {
            "osImage": t.proxy(
                renames[
                    "GoogleCloudDataplexV1EnvironmentInfrastructureSpecOsImageRuntimeOut"
                ]
            ),
            "compute": t.proxy(
                renames[
                    "GoogleCloudDataplexV1EnvironmentInfrastructureSpecComputeResourcesOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1EnvironmentInfrastructureSpecOut"])
    types["GoogleCloudDataplexV1DataScanEventDataQualityAppliedConfigsIn"] = t.struct(
        {
            "rowFilterApplied": t.boolean().optional(),
            "samplingPercent": t.number().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanEventDataQualityAppliedConfigsIn"])
    types["GoogleCloudDataplexV1DataScanEventDataQualityAppliedConfigsOut"] = t.struct(
        {
            "rowFilterApplied": t.boolean().optional(),
            "samplingPercent": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanEventDataQualityAppliedConfigsOut"])
    types["GoogleCloudDataplexV1TaskNotebookTaskConfigIn"] = t.struct(
        {
            "fileUris": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "notebook": t.string(),
            "infrastructureSpec": t.proxy(
                renames["GoogleCloudDataplexV1TaskInfrastructureSpecIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TaskNotebookTaskConfigIn"])
    types["GoogleCloudDataplexV1TaskNotebookTaskConfigOut"] = t.struct(
        {
            "fileUris": t.array(t.string()).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "notebook": t.string(),
            "infrastructureSpec": t.proxy(
                renames["GoogleCloudDataplexV1TaskInfrastructureSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TaskNotebookTaskConfigOut"])
    types["GoogleCloudDataplexV1JobIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudDataplexV1JobIn"]
    )
    types["GoogleCloudDataplexV1JobOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "retryCount": t.integer().optional(),
            "endTime": t.string().optional(),
            "uid": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "service": t.string().optional(),
            "message": t.string().optional(),
            "serviceJob": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1JobOut"])
    types["GoogleCloudDataplexV1ListDataTaxonomiesResponseIn"] = t.struct(
        {
            "unreachableLocations": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "dataTaxonomies": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataTaxonomyIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListDataTaxonomiesResponseIn"])
    types["GoogleCloudDataplexV1ListDataTaxonomiesResponseOut"] = t.struct(
        {
            "unreachableLocations": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "dataTaxonomies": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataTaxonomyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListDataTaxonomiesResponseOut"])
    types["GoogleCloudDataplexV1StorageFormatJsonOptionsIn"] = t.struct(
        {"encoding": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1StorageFormatJsonOptionsIn"])
    types["GoogleCloudDataplexV1StorageFormatJsonOptionsOut"] = t.struct(
        {
            "encoding": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1StorageFormatJsonOptionsOut"])
    types["GoogleCloudDataplexV1DataProfileResultIn"] = t.struct(
        {
            "rowCount": t.string().optional(),
            "profile": t.proxy(
                renames["GoogleCloudDataplexV1DataProfileResultProfileIn"]
            ).optional(),
            "scannedData": t.proxy(
                renames["GoogleCloudDataplexV1ScannedDataIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataProfileResultIn"])
    types["GoogleCloudDataplexV1DataProfileResultOut"] = t.struct(
        {
            "rowCount": t.string().optional(),
            "profile": t.proxy(
                renames["GoogleCloudDataplexV1DataProfileResultProfileOut"]
            ).optional(),
            "scannedData": t.proxy(
                renames["GoogleCloudDataplexV1ScannedDataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataProfileResultOut"])
    types["GoogleCloudDataplexV1DataQualityRuleIn"] = t.struct(
        {
            "threshold": t.number().optional(),
            "ignoreNull": t.boolean().optional(),
            "column": t.string().optional(),
            "rangeExpectation": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityRuleRangeExpectationIn"]
            ).optional(),
            "setExpectation": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityRuleSetExpectationIn"]
            ).optional(),
            "dimension": t.string(),
            "statisticRangeExpectation": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectationIn"
                ]
            ).optional(),
            "rowConditionExpectation": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityRuleRowConditionExpectationIn"]
            ).optional(),
            "nonNullExpectation": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityRuleNonNullExpectationIn"]
            ).optional(),
            "uniquenessExpectation": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityRuleUniquenessExpectationIn"]
            ).optional(),
            "tableConditionExpectation": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataQualityRuleTableConditionExpectationIn"
                ]
            ).optional(),
            "regexExpectation": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityRuleRegexExpectationIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleIn"])
    types["GoogleCloudDataplexV1DataQualityRuleOut"] = t.struct(
        {
            "threshold": t.number().optional(),
            "ignoreNull": t.boolean().optional(),
            "column": t.string().optional(),
            "rangeExpectation": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityRuleRangeExpectationOut"]
            ).optional(),
            "setExpectation": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityRuleSetExpectationOut"]
            ).optional(),
            "dimension": t.string(),
            "statisticRangeExpectation": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectationOut"
                ]
            ).optional(),
            "rowConditionExpectation": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataQualityRuleRowConditionExpectationOut"
                ]
            ).optional(),
            "nonNullExpectation": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityRuleNonNullExpectationOut"]
            ).optional(),
            "uniquenessExpectation": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityRuleUniquenessExpectationOut"]
            ).optional(),
            "tableConditionExpectation": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataQualityRuleTableConditionExpectationOut"
                ]
            ).optional(),
            "regexExpectation": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityRuleRegexExpectationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleOut"])
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
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
    types["GoogleCloudDataplexV1ActionIn"] = t.struct(
        {
            "issue": t.string().optional(),
            "incompatibleDataSchema": t.proxy(
                renames["GoogleCloudDataplexV1ActionIncompatibleDataSchemaIn"]
            ).optional(),
            "invalidDataOrganization": t.proxy(
                renames["GoogleCloudDataplexV1ActionInvalidDataOrganizationIn"]
            ).optional(),
            "missingResource": t.proxy(
                renames["GoogleCloudDataplexV1ActionMissingResourceIn"]
            ).optional(),
            "missingData": t.proxy(
                renames["GoogleCloudDataplexV1ActionMissingDataIn"]
            ).optional(),
            "failedSecurityPolicyApply": t.proxy(
                renames["GoogleCloudDataplexV1ActionFailedSecurityPolicyApplyIn"]
            ).optional(),
            "unauthorizedResource": t.proxy(
                renames["GoogleCloudDataplexV1ActionUnauthorizedResourceIn"]
            ).optional(),
            "invalidDataPartition": t.proxy(
                renames["GoogleCloudDataplexV1ActionInvalidDataPartitionIn"]
            ).optional(),
            "category": t.string().optional(),
            "invalidDataFormat": t.proxy(
                renames["GoogleCloudDataplexV1ActionInvalidDataFormatIn"]
            ).optional(),
            "detectTime": t.string().optional(),
            "dataLocations": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ActionIn"])
    types["GoogleCloudDataplexV1ActionOut"] = t.struct(
        {
            "issue": t.string().optional(),
            "incompatibleDataSchema": t.proxy(
                renames["GoogleCloudDataplexV1ActionIncompatibleDataSchemaOut"]
            ).optional(),
            "invalidDataOrganization": t.proxy(
                renames["GoogleCloudDataplexV1ActionInvalidDataOrganizationOut"]
            ).optional(),
            "missingResource": t.proxy(
                renames["GoogleCloudDataplexV1ActionMissingResourceOut"]
            ).optional(),
            "missingData": t.proxy(
                renames["GoogleCloudDataplexV1ActionMissingDataOut"]
            ).optional(),
            "failedSecurityPolicyApply": t.proxy(
                renames["GoogleCloudDataplexV1ActionFailedSecurityPolicyApplyOut"]
            ).optional(),
            "name": t.string().optional(),
            "unauthorizedResource": t.proxy(
                renames["GoogleCloudDataplexV1ActionUnauthorizedResourceOut"]
            ).optional(),
            "invalidDataPartition": t.proxy(
                renames["GoogleCloudDataplexV1ActionInvalidDataPartitionOut"]
            ).optional(),
            "category": t.string().optional(),
            "lake": t.string().optional(),
            "invalidDataFormat": t.proxy(
                renames["GoogleCloudDataplexV1ActionInvalidDataFormatOut"]
            ).optional(),
            "zone": t.string().optional(),
            "asset": t.string().optional(),
            "detectTime": t.string().optional(),
            "dataLocations": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ActionOut"])
    types["GoogleCloudDataplexV1DataSourceIn"] = t.struct(
        {"entity": t.string().optional(), "resource": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1DataSourceIn"])
    types["GoogleCloudDataplexV1DataSourceOut"] = t.struct(
        {
            "entity": t.string().optional(),
            "resource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataSourceOut"])
    types["GoogleCloudDataplexV1DataScanJobIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1DataScanJobIn"])
    types["GoogleCloudDataplexV1DataScanJobOut"] = t.struct(
        {
            "dataProfileSpec": t.proxy(
                renames["GoogleCloudDataplexV1DataProfileSpecOut"]
            ).optional(),
            "dataQualityResult": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityResultOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "uid": t.string().optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "dataProfileResult": t.proxy(
                renames["GoogleCloudDataplexV1DataProfileResultOut"]
            ).optional(),
            "dataQualitySpec": t.proxy(
                renames["GoogleCloudDataplexV1DataQualitySpecOut"]
            ).optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanJobOut"])
    types["GoogleCloudDataplexV1LakeMetastoreStatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "updateTime": t.string().optional(),
            "endpoint": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1LakeMetastoreStatusIn"])
    types["GoogleCloudDataplexV1LakeMetastoreStatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "updateTime": t.string().optional(),
            "endpoint": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1LakeMetastoreStatusOut"])
    types["GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectationIn"] = t.struct(
        {
            "minValue": t.string().optional(),
            "maxValue": t.string().optional(),
            "statistic": t.string().optional(),
            "strictMinEnabled": t.boolean().optional(),
            "strictMaxEnabled": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectationIn"])
    types[
        "GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectationOut"
    ] = t.struct(
        {
            "minValue": t.string().optional(),
            "maxValue": t.string().optional(),
            "statistic": t.string().optional(),
            "strictMinEnabled": t.boolean().optional(),
            "strictMaxEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectationOut"]
    )
    types["GoogleIamV1TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsRequestIn"])
    types["GoogleIamV1TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsRequestOut"])
    types["GoogleCloudDataplexV1DataProfileSpecIn"] = t.struct(
        {"samplingPercent": t.number().optional(), "rowFilter": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1DataProfileSpecIn"])
    types["GoogleCloudDataplexV1DataProfileSpecOut"] = t.struct(
        {
            "samplingPercent": t.number().optional(),
            "rowFilter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataProfileSpecOut"])
    types["GoogleCloudDataplexV1TaskSparkTaskConfigIn"] = t.struct(
        {
            "sqlScript": t.string().optional(),
            "mainJarFileUri": t.string().optional(),
            "sqlScriptFile": t.string().optional(),
            "mainClass": t.string().optional(),
            "archiveUris": t.array(t.string()).optional(),
            "infrastructureSpec": t.proxy(
                renames["GoogleCloudDataplexV1TaskInfrastructureSpecIn"]
            ).optional(),
            "fileUris": t.array(t.string()).optional(),
            "pythonScriptFile": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TaskSparkTaskConfigIn"])
    types["GoogleCloudDataplexV1TaskSparkTaskConfigOut"] = t.struct(
        {
            "sqlScript": t.string().optional(),
            "mainJarFileUri": t.string().optional(),
            "sqlScriptFile": t.string().optional(),
            "mainClass": t.string().optional(),
            "archiveUris": t.array(t.string()).optional(),
            "infrastructureSpec": t.proxy(
                renames["GoogleCloudDataplexV1TaskInfrastructureSpecOut"]
            ).optional(),
            "fileUris": t.array(t.string()).optional(),
            "pythonScriptFile": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TaskSparkTaskConfigOut"])
    types["GoogleCloudDataplexV1DataScanExecutionSpecIn"] = t.struct(
        {
            "field": t.string().optional(),
            "trigger": t.proxy(renames["GoogleCloudDataplexV1TriggerIn"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanExecutionSpecIn"])
    types["GoogleCloudDataplexV1DataScanExecutionSpecOut"] = t.struct(
        {
            "field": t.string().optional(),
            "trigger": t.proxy(renames["GoogleCloudDataplexV1TriggerOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanExecutionSpecOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleCloudDataplexV1AssetDiscoverySpecIn"] = t.struct(
        {
            "excludePatterns": t.array(t.string()).optional(),
            "jsonOptions": t.proxy(
                renames["GoogleCloudDataplexV1AssetDiscoverySpecJsonOptionsIn"]
            ).optional(),
            "csvOptions": t.proxy(
                renames["GoogleCloudDataplexV1AssetDiscoverySpecCsvOptionsIn"]
            ).optional(),
            "schedule": t.string().optional(),
            "includePatterns": t.array(t.string()).optional(),
            "enabled": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetDiscoverySpecIn"])
    types["GoogleCloudDataplexV1AssetDiscoverySpecOut"] = t.struct(
        {
            "excludePatterns": t.array(t.string()).optional(),
            "jsonOptions": t.proxy(
                renames["GoogleCloudDataplexV1AssetDiscoverySpecJsonOptionsOut"]
            ).optional(),
            "csvOptions": t.proxy(
                renames["GoogleCloudDataplexV1AssetDiscoverySpecCsvOptionsOut"]
            ).optional(),
            "schedule": t.string().optional(),
            "includePatterns": t.array(t.string()).optional(),
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetDiscoverySpecOut"])

    functions = {}
    functions["projectsLocationsGet"] = dataplex.get(
        "v1/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudLocationListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = dataplex.get(
        "v1/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudLocationListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesPatch"] = dataplex.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesTestIamPermissions"] = dataplex.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesSetIamPolicy"] = dataplex.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesGet"] = dataplex.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesGetIamPolicy"] = dataplex.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesList"] = dataplex.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesCreate"] = dataplex.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesDelete"] = dataplex.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesTasksList"] = dataplex.post(
        "v1/{parent}/tasks",
        t.struct(
            {
                "taskId": t.string(),
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "triggerSpec": t.proxy(
                    renames["GoogleCloudDataplexV1TaskTriggerSpecIn"]
                ),
                "spark": t.proxy(
                    renames["GoogleCloudDataplexV1TaskSparkTaskConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "notebook": t.proxy(
                    renames["GoogleCloudDataplexV1TaskNotebookTaskConfigIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "executionSpec": t.proxy(
                    renames["GoogleCloudDataplexV1TaskExecutionSpecIn"]
                ),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesTasksDelete"] = dataplex.post(
        "v1/{parent}/tasks",
        t.struct(
            {
                "taskId": t.string(),
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "triggerSpec": t.proxy(
                    renames["GoogleCloudDataplexV1TaskTriggerSpecIn"]
                ),
                "spark": t.proxy(
                    renames["GoogleCloudDataplexV1TaskSparkTaskConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "notebook": t.proxy(
                    renames["GoogleCloudDataplexV1TaskNotebookTaskConfigIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "executionSpec": t.proxy(
                    renames["GoogleCloudDataplexV1TaskExecutionSpecIn"]
                ),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesTasksGetIamPolicy"] = dataplex.post(
        "v1/{parent}/tasks",
        t.struct(
            {
                "taskId": t.string(),
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "triggerSpec": t.proxy(
                    renames["GoogleCloudDataplexV1TaskTriggerSpecIn"]
                ),
                "spark": t.proxy(
                    renames["GoogleCloudDataplexV1TaskSparkTaskConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "notebook": t.proxy(
                    renames["GoogleCloudDataplexV1TaskNotebookTaskConfigIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "executionSpec": t.proxy(
                    renames["GoogleCloudDataplexV1TaskExecutionSpecIn"]
                ),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesTasksGet"] = dataplex.post(
        "v1/{parent}/tasks",
        t.struct(
            {
                "taskId": t.string(),
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "triggerSpec": t.proxy(
                    renames["GoogleCloudDataplexV1TaskTriggerSpecIn"]
                ),
                "spark": t.proxy(
                    renames["GoogleCloudDataplexV1TaskSparkTaskConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "notebook": t.proxy(
                    renames["GoogleCloudDataplexV1TaskNotebookTaskConfigIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "executionSpec": t.proxy(
                    renames["GoogleCloudDataplexV1TaskExecutionSpecIn"]
                ),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesTasksPatch"] = dataplex.post(
        "v1/{parent}/tasks",
        t.struct(
            {
                "taskId": t.string(),
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "triggerSpec": t.proxy(
                    renames["GoogleCloudDataplexV1TaskTriggerSpecIn"]
                ),
                "spark": t.proxy(
                    renames["GoogleCloudDataplexV1TaskSparkTaskConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "notebook": t.proxy(
                    renames["GoogleCloudDataplexV1TaskNotebookTaskConfigIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "executionSpec": t.proxy(
                    renames["GoogleCloudDataplexV1TaskExecutionSpecIn"]
                ),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesTasksSetIamPolicy"] = dataplex.post(
        "v1/{parent}/tasks",
        t.struct(
            {
                "taskId": t.string(),
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "triggerSpec": t.proxy(
                    renames["GoogleCloudDataplexV1TaskTriggerSpecIn"]
                ),
                "spark": t.proxy(
                    renames["GoogleCloudDataplexV1TaskSparkTaskConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "notebook": t.proxy(
                    renames["GoogleCloudDataplexV1TaskNotebookTaskConfigIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "executionSpec": t.proxy(
                    renames["GoogleCloudDataplexV1TaskExecutionSpecIn"]
                ),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesTasksRun"] = dataplex.post(
        "v1/{parent}/tasks",
        t.struct(
            {
                "taskId": t.string(),
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "triggerSpec": t.proxy(
                    renames["GoogleCloudDataplexV1TaskTriggerSpecIn"]
                ),
                "spark": t.proxy(
                    renames["GoogleCloudDataplexV1TaskSparkTaskConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "notebook": t.proxy(
                    renames["GoogleCloudDataplexV1TaskNotebookTaskConfigIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "executionSpec": t.proxy(
                    renames["GoogleCloudDataplexV1TaskExecutionSpecIn"]
                ),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesTasksTestIamPermissions"] = dataplex.post(
        "v1/{parent}/tasks",
        t.struct(
            {
                "taskId": t.string(),
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "triggerSpec": t.proxy(
                    renames["GoogleCloudDataplexV1TaskTriggerSpecIn"]
                ),
                "spark": t.proxy(
                    renames["GoogleCloudDataplexV1TaskSparkTaskConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "notebook": t.proxy(
                    renames["GoogleCloudDataplexV1TaskNotebookTaskConfigIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "executionSpec": t.proxy(
                    renames["GoogleCloudDataplexV1TaskExecutionSpecIn"]
                ),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesTasksCreate"] = dataplex.post(
        "v1/{parent}/tasks",
        t.struct(
            {
                "taskId": t.string(),
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "triggerSpec": t.proxy(
                    renames["GoogleCloudDataplexV1TaskTriggerSpecIn"]
                ),
                "spark": t.proxy(
                    renames["GoogleCloudDataplexV1TaskSparkTaskConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "notebook": t.proxy(
                    renames["GoogleCloudDataplexV1TaskNotebookTaskConfigIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "executionSpec": t.proxy(
                    renames["GoogleCloudDataplexV1TaskExecutionSpecIn"]
                ),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesTasksJobsCancel"] = dataplex.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDataplexV1JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesTasksJobsList"] = dataplex.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDataplexV1JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesTasksJobsGet"] = dataplex.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDataplexV1JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesContentitemsCreate"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesContentitemsGet"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesContentitemsList"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesContentitemsPatch"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesContentitemsSetIamPolicy"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesContentitemsTestIamPermissions"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesContentitemsDelete"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesContentitemsGetIamPolicy"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesGet"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesSetIamPolicy"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesDelete"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesList"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesCreate"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesTestIamPermissions"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesPatch"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesGetIamPolicy"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesActionsList"] = dataplex.get(
        "v1/{parent}/actions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1ListActionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesAssetsCreate"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesAssetsList"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesAssetsGet"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesAssetsSetIamPolicy"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesAssetsTestIamPermissions"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesAssetsDelete"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesAssetsPatch"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesAssetsGetIamPolicy"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesAssetsActionsList"] = dataplex.get(
        "v1/{parent}/actions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1ListActionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesEntitiesList"] = dataplex.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1EntityOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesEntitiesUpdate"] = dataplex.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1EntityOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesEntitiesCreate"] = dataplex.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1EntityOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesEntitiesDelete"] = dataplex.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1EntityOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesEntitiesGet"] = dataplex.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1EntityOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesEntitiesPartitionsCreate"] = dataplex.get(
        "v1/{parent}/partitions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1ListPartitionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesEntitiesPartitionsGet"] = dataplex.get(
        "v1/{parent}/partitions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1ListPartitionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesEntitiesPartitionsDelete"] = dataplex.get(
        "v1/{parent}/partitions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1ListPartitionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesEntitiesPartitionsList"] = dataplex.get(
        "v1/{parent}/partitions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1ListPartitionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesActionsList"] = dataplex.get(
        "v1/{parent}/actions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1ListActionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesEnvironmentsTestIamPermissions"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesEnvironmentsCreate"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesEnvironmentsSetIamPolicy"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesEnvironmentsGet"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesEnvironmentsList"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesEnvironmentsDelete"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesEnvironmentsPatch"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesEnvironmentsGetIamPolicy"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesEnvironmentsSessionsList"] = dataplex.get(
        "v1/{parent}/sessions",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1ListSessionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesContentGetIamPolicy"] = dataplex.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesContentList"] = dataplex.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesContentTestIamPermissions"] = dataplex.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesContentGet"] = dataplex.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesContentPatch"] = dataplex.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesContentSetIamPolicy"] = dataplex.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesContentCreate"] = dataplex.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesContentDelete"] = dataplex.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsSetIamPolicy"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsTestIamPermissions"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsGetIamPolicy"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAspectTypesTestIamPermissions"] = dataplex.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAspectTypesGetIamPolicy"] = dataplex.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAspectTypesSetIamPolicy"] = dataplex.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = dataplex.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = dataplex.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = dataplex.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = dataplex.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataScansGetIamPolicy"] = dataplex.post(
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
    functions["projectsLocationsDataScansRun"] = dataplex.post(
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
    functions["projectsLocationsDataScansList"] = dataplex.post(
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
    functions["projectsLocationsDataScansCreate"] = dataplex.post(
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
    functions["projectsLocationsDataScansSetIamPolicy"] = dataplex.post(
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
    functions["projectsLocationsDataScansDelete"] = dataplex.post(
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
    functions["projectsLocationsDataScansGet"] = dataplex.post(
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
    functions["projectsLocationsDataScansPatch"] = dataplex.post(
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
    functions["projectsLocationsDataScansTestIamPermissions"] = dataplex.post(
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
    functions["projectsLocationsDataScansJobsGet"] = dataplex.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1ListDataScanJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataScansJobsList"] = dataplex.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1ListDataScanJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataAttributeBindingsGetIamPolicy"] = dataplex.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "attributes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "paths": t.array(
                    t.proxy(renames["GoogleCloudDataplexV1DataAttributeBindingPathIn"])
                ).optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataAttributeBindingsCreate"] = dataplex.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "attributes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "paths": t.array(
                    t.proxy(renames["GoogleCloudDataplexV1DataAttributeBindingPathIn"])
                ).optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataAttributeBindingsList"] = dataplex.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "attributes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "paths": t.array(
                    t.proxy(renames["GoogleCloudDataplexV1DataAttributeBindingPathIn"])
                ).optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataAttributeBindingsGet"] = dataplex.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "attributes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "paths": t.array(
                    t.proxy(renames["GoogleCloudDataplexV1DataAttributeBindingPathIn"])
                ).optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDataAttributeBindingsTestIamPermissions"
    ] = dataplex.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "attributes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "paths": t.array(
                    t.proxy(renames["GoogleCloudDataplexV1DataAttributeBindingPathIn"])
                ).optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataAttributeBindingsDelete"] = dataplex.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "attributes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "paths": t.array(
                    t.proxy(renames["GoogleCloudDataplexV1DataAttributeBindingPathIn"])
                ).optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataAttributeBindingsSetIamPolicy"] = dataplex.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "attributes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "paths": t.array(
                    t.proxy(renames["GoogleCloudDataplexV1DataAttributeBindingPathIn"])
                ).optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataAttributeBindingsPatch"] = dataplex.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "attributes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "paths": t.array(
                    t.proxy(renames["GoogleCloudDataplexV1DataAttributeBindingPathIn"])
                ).optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesPatch"] = dataplex.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesCreate"] = dataplex.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesGetIamPolicy"] = dataplex.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesGet"] = dataplex.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesTestIamPermissions"] = dataplex.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesList"] = dataplex.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesDelete"] = dataplex.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesSetIamPolicy"] = dataplex.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesAttributesList"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesAttributesCreate"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesAttributesSetIamPolicy"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesAttributesDelete"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesAttributesGet"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDataTaxonomiesAttributesTestIamPermissions"
    ] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesAttributesPatch"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesAttributesGetIamPolicy"] = dataplex.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryTypesSetIamPolicy"] = dataplex.post(
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
    functions["projectsLocationsEntryTypesGetIamPolicy"] = dataplex.post(
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
    functions["projectsLocationsEntryTypesTestIamPermissions"] = dataplex.post(
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

    return Import(
        importer="dataplex", renames=renames, types=Box(types), functions=Box(functions)
    )
