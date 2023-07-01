from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_dataplex():
    dataplex = HTTPRuntime("https://dataplex.googleapis.com/")

    renames = {
        "ErrorResponse": "_dataplex_1_ErrorResponse",
        "GoogleCloudDataplexV1DataTaxonomyIn": "_dataplex_2_GoogleCloudDataplexV1DataTaxonomyIn",
        "GoogleCloudDataplexV1DataTaxonomyOut": "_dataplex_3_GoogleCloudDataplexV1DataTaxonomyOut",
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoTopNValueIn": "_dataplex_4_GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoTopNValueIn",
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoTopNValueOut": "_dataplex_5_GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoTopNValueOut",
        "GoogleCloudDataplexV1DataProfileResultIn": "_dataplex_6_GoogleCloudDataplexV1DataProfileResultIn",
        "GoogleCloudDataplexV1DataProfileResultOut": "_dataplex_7_GoogleCloudDataplexV1DataProfileResultOut",
        "GoogleCloudDataplexV1ContentNotebookIn": "_dataplex_8_GoogleCloudDataplexV1ContentNotebookIn",
        "GoogleCloudDataplexV1ContentNotebookOut": "_dataplex_9_GoogleCloudDataplexV1ContentNotebookOut",
        "GoogleCloudDataplexV1DataScanExecutionSpecIn": "_dataplex_10_GoogleCloudDataplexV1DataScanExecutionSpecIn",
        "GoogleCloudDataplexV1DataScanExecutionSpecOut": "_dataplex_11_GoogleCloudDataplexV1DataScanExecutionSpecOut",
        "GoogleCloudDataplexV1AssetStatusIn": "_dataplex_12_GoogleCloudDataplexV1AssetStatusIn",
        "GoogleCloudDataplexV1AssetStatusOut": "_dataplex_13_GoogleCloudDataplexV1AssetStatusOut",
        "GoogleCloudDataplexV1ListEntitiesResponseIn": "_dataplex_14_GoogleCloudDataplexV1ListEntitiesResponseIn",
        "GoogleCloudDataplexV1ListEntitiesResponseOut": "_dataplex_15_GoogleCloudDataplexV1ListEntitiesResponseOut",
        "GoogleCloudDataplexV1ListContentResponseIn": "_dataplex_16_GoogleCloudDataplexV1ListContentResponseIn",
        "GoogleCloudDataplexV1ListContentResponseOut": "_dataplex_17_GoogleCloudDataplexV1ListContentResponseOut",
        "GoogleCloudDataplexV1ListLakesResponseIn": "_dataplex_18_GoogleCloudDataplexV1ListLakesResponseIn",
        "GoogleCloudDataplexV1ListLakesResponseOut": "_dataplex_19_GoogleCloudDataplexV1ListLakesResponseOut",
        "GoogleCloudDataplexV1ActionInvalidDataOrganizationIn": "_dataplex_20_GoogleCloudDataplexV1ActionInvalidDataOrganizationIn",
        "GoogleCloudDataplexV1ActionInvalidDataOrganizationOut": "_dataplex_21_GoogleCloudDataplexV1ActionInvalidDataOrganizationOut",
        "GoogleCloudDataplexV1RunDataScanRequestIn": "_dataplex_22_GoogleCloudDataplexV1RunDataScanRequestIn",
        "GoogleCloudDataplexV1RunDataScanRequestOut": "_dataplex_23_GoogleCloudDataplexV1RunDataScanRequestOut",
        "GoogleCloudDataplexV1DataProfileSpecIn": "_dataplex_24_GoogleCloudDataplexV1DataProfileSpecIn",
        "GoogleCloudDataplexV1DataProfileSpecOut": "_dataplex_25_GoogleCloudDataplexV1DataProfileSpecOut",
        "GoogleCloudDataplexV1ListDataScansResponseIn": "_dataplex_26_GoogleCloudDataplexV1ListDataScansResponseIn",
        "GoogleCloudDataplexV1ListDataScansResponseOut": "_dataplex_27_GoogleCloudDataplexV1ListDataScansResponseOut",
        "GoogleCloudDataplexV1ListDataScanJobsResponseIn": "_dataplex_28_GoogleCloudDataplexV1ListDataScanJobsResponseIn",
        "GoogleCloudDataplexV1ListDataScanJobsResponseOut": "_dataplex_29_GoogleCloudDataplexV1ListDataScanJobsResponseOut",
        "GoogleCloudDataplexV1DiscoveryEventPartitionDetailsIn": "_dataplex_30_GoogleCloudDataplexV1DiscoveryEventPartitionDetailsIn",
        "GoogleCloudDataplexV1DiscoveryEventPartitionDetailsOut": "_dataplex_31_GoogleCloudDataplexV1DiscoveryEventPartitionDetailsOut",
        "GoogleCloudDataplexV1EnvironmentInfrastructureSpecOsImageRuntimeIn": "_dataplex_32_GoogleCloudDataplexV1EnvironmentInfrastructureSpecOsImageRuntimeIn",
        "GoogleCloudDataplexV1EnvironmentInfrastructureSpecOsImageRuntimeOut": "_dataplex_33_GoogleCloudDataplexV1EnvironmentInfrastructureSpecOsImageRuntimeOut",
        "GoogleCloudDataplexV1ListActionsResponseIn": "_dataplex_34_GoogleCloudDataplexV1ListActionsResponseIn",
        "GoogleCloudDataplexV1ListActionsResponseOut": "_dataplex_35_GoogleCloudDataplexV1ListActionsResponseOut",
        "GoogleCloudDataplexV1DiscoveryEventIn": "_dataplex_36_GoogleCloudDataplexV1DiscoveryEventIn",
        "GoogleCloudDataplexV1DiscoveryEventOut": "_dataplex_37_GoogleCloudDataplexV1DiscoveryEventOut",
        "GoogleCloudDataplexV1DataAccessSpecIn": "_dataplex_38_GoogleCloudDataplexV1DataAccessSpecIn",
        "GoogleCloudDataplexV1DataAccessSpecOut": "_dataplex_39_GoogleCloudDataplexV1DataAccessSpecOut",
        "GoogleCloudDataplexV1SessionIn": "_dataplex_40_GoogleCloudDataplexV1SessionIn",
        "GoogleCloudDataplexV1SessionOut": "_dataplex_41_GoogleCloudDataplexV1SessionOut",
        "GoogleCloudDataplexV1ZoneDiscoverySpecCsvOptionsIn": "_dataplex_42_GoogleCloudDataplexV1ZoneDiscoverySpecCsvOptionsIn",
        "GoogleCloudDataplexV1ZoneDiscoverySpecCsvOptionsOut": "_dataplex_43_GoogleCloudDataplexV1ZoneDiscoverySpecCsvOptionsOut",
        "GoogleCloudDataplexV1ListAssetsResponseIn": "_dataplex_44_GoogleCloudDataplexV1ListAssetsResponseIn",
        "GoogleCloudDataplexV1ListAssetsResponseOut": "_dataplex_45_GoogleCloudDataplexV1ListAssetsResponseOut",
        "GoogleCloudDataplexV1DataScanEventPostScanActionsResultIn": "_dataplex_46_GoogleCloudDataplexV1DataScanEventPostScanActionsResultIn",
        "GoogleCloudDataplexV1DataScanEventPostScanActionsResultOut": "_dataplex_47_GoogleCloudDataplexV1DataScanEventPostScanActionsResultOut",
        "GoogleCloudDataplexV1EnvironmentSessionStatusIn": "_dataplex_48_GoogleCloudDataplexV1EnvironmentSessionStatusIn",
        "GoogleCloudDataplexV1EnvironmentSessionStatusOut": "_dataplex_49_GoogleCloudDataplexV1EnvironmentSessionStatusOut",
        "GoogleCloudDataplexV1DataAttributeIn": "_dataplex_50_GoogleCloudDataplexV1DataAttributeIn",
        "GoogleCloudDataplexV1DataAttributeOut": "_dataplex_51_GoogleCloudDataplexV1DataAttributeOut",
        "GoogleCloudDataplexV1DiscoveryEventActionDetailsIn": "_dataplex_52_GoogleCloudDataplexV1DiscoveryEventActionDetailsIn",
        "GoogleCloudDataplexV1DiscoveryEventActionDetailsOut": "_dataplex_53_GoogleCloudDataplexV1DiscoveryEventActionDetailsOut",
        "GoogleCloudDataplexV1AssetResourceSpecIn": "_dataplex_54_GoogleCloudDataplexV1AssetResourceSpecIn",
        "GoogleCloudDataplexV1AssetResourceSpecOut": "_dataplex_55_GoogleCloudDataplexV1AssetResourceSpecOut",
        "GoogleCloudDataplexV1AssetIn": "_dataplex_56_GoogleCloudDataplexV1AssetIn",
        "GoogleCloudDataplexV1AssetOut": "_dataplex_57_GoogleCloudDataplexV1AssetOut",
        "GoogleLongrunningOperationIn": "_dataplex_58_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_dataplex_59_GoogleLongrunningOperationOut",
        "GoogleCloudDataplexV1AssetDiscoverySpecJsonOptionsIn": "_dataplex_60_GoogleCloudDataplexV1AssetDiscoverySpecJsonOptionsIn",
        "GoogleCloudDataplexV1AssetDiscoverySpecJsonOptionsOut": "_dataplex_61_GoogleCloudDataplexV1AssetDiscoverySpecJsonOptionsOut",
        "GoogleCloudDataplexV1AssetSecurityStatusIn": "_dataplex_62_GoogleCloudDataplexV1AssetSecurityStatusIn",
        "GoogleCloudDataplexV1AssetSecurityStatusOut": "_dataplex_63_GoogleCloudDataplexV1AssetSecurityStatusOut",
        "GoogleCloudDataplexV1ActionInvalidDataFormatIn": "_dataplex_64_GoogleCloudDataplexV1ActionInvalidDataFormatIn",
        "GoogleCloudDataplexV1ActionInvalidDataFormatOut": "_dataplex_65_GoogleCloudDataplexV1ActionInvalidDataFormatOut",
        "GoogleCloudDataplexV1ScannedDataIn": "_dataplex_66_GoogleCloudDataplexV1ScannedDataIn",
        "GoogleCloudDataplexV1ScannedDataOut": "_dataplex_67_GoogleCloudDataplexV1ScannedDataOut",
        "GoogleCloudDataplexV1ListJobsResponseIn": "_dataplex_68_GoogleCloudDataplexV1ListJobsResponseIn",
        "GoogleCloudDataplexV1ListJobsResponseOut": "_dataplex_69_GoogleCloudDataplexV1ListJobsResponseOut",
        "GoogleCloudDataplexV1ActionMissingResourceIn": "_dataplex_70_GoogleCloudDataplexV1ActionMissingResourceIn",
        "GoogleCloudDataplexV1ActionMissingResourceOut": "_dataplex_71_GoogleCloudDataplexV1ActionMissingResourceOut",
        "GoogleCloudDataplexV1AssetDiscoveryStatusStatsIn": "_dataplex_72_GoogleCloudDataplexV1AssetDiscoveryStatusStatsIn",
        "GoogleCloudDataplexV1AssetDiscoveryStatusStatsOut": "_dataplex_73_GoogleCloudDataplexV1AssetDiscoveryStatusStatsOut",
        "GoogleCloudDataplexV1LakeMetastoreStatusIn": "_dataplex_74_GoogleCloudDataplexV1LakeMetastoreStatusIn",
        "GoogleCloudDataplexV1LakeMetastoreStatusOut": "_dataplex_75_GoogleCloudDataplexV1LakeMetastoreStatusOut",
        "GoogleCloudDataplexV1TaskSparkTaskConfigIn": "_dataplex_76_GoogleCloudDataplexV1TaskSparkTaskConfigIn",
        "GoogleCloudDataplexV1TaskSparkTaskConfigOut": "_dataplex_77_GoogleCloudDataplexV1TaskSparkTaskConfigOut",
        "GoogleCloudDataplexV1JobEventIn": "_dataplex_78_GoogleCloudDataplexV1JobEventIn",
        "GoogleCloudDataplexV1JobEventOut": "_dataplex_79_GoogleCloudDataplexV1JobEventOut",
        "GoogleCloudDataplexV1ListEnvironmentsResponseIn": "_dataplex_80_GoogleCloudDataplexV1ListEnvironmentsResponseIn",
        "GoogleCloudDataplexV1ListEnvironmentsResponseOut": "_dataplex_81_GoogleCloudDataplexV1ListEnvironmentsResponseOut",
        "GoogleCloudDataplexV1ZoneDiscoverySpecIn": "_dataplex_82_GoogleCloudDataplexV1ZoneDiscoverySpecIn",
        "GoogleCloudDataplexV1ZoneDiscoverySpecOut": "_dataplex_83_GoogleCloudDataplexV1ZoneDiscoverySpecOut",
        "GoogleCloudDataplexV1OperationMetadataIn": "_dataplex_84_GoogleCloudDataplexV1OperationMetadataIn",
        "GoogleCloudDataplexV1OperationMetadataOut": "_dataplex_85_GoogleCloudDataplexV1OperationMetadataOut",
        "GoogleCloudDataplexV1DataAttributeBindingIn": "_dataplex_86_GoogleCloudDataplexV1DataAttributeBindingIn",
        "GoogleCloudDataplexV1DataAttributeBindingOut": "_dataplex_87_GoogleCloudDataplexV1DataAttributeBindingOut",
        "GoogleCloudDataplexV1DataQualityRuleUniquenessExpectationIn": "_dataplex_88_GoogleCloudDataplexV1DataQualityRuleUniquenessExpectationIn",
        "GoogleCloudDataplexV1DataQualityRuleUniquenessExpectationOut": "_dataplex_89_GoogleCloudDataplexV1DataQualityRuleUniquenessExpectationOut",
        "GoogleCloudDataplexV1DataQualityRuleRegexExpectationIn": "_dataplex_90_GoogleCloudDataplexV1DataQualityRuleRegexExpectationIn",
        "GoogleCloudDataplexV1DataQualityRuleRegexExpectationOut": "_dataplex_91_GoogleCloudDataplexV1DataQualityRuleRegexExpectationOut",
        "GoogleCloudDataplexV1DiscoveryEventEntityDetailsIn": "_dataplex_92_GoogleCloudDataplexV1DiscoveryEventEntityDetailsIn",
        "GoogleCloudDataplexV1DiscoveryEventEntityDetailsOut": "_dataplex_93_GoogleCloudDataplexV1DiscoveryEventEntityDetailsOut",
        "GoogleCloudDataplexV1EntityIn": "_dataplex_94_GoogleCloudDataplexV1EntityIn",
        "GoogleCloudDataplexV1EntityOut": "_dataplex_95_GoogleCloudDataplexV1EntityOut",
        "GoogleCloudDataplexV1AssetDiscoveryStatusIn": "_dataplex_96_GoogleCloudDataplexV1AssetDiscoveryStatusIn",
        "GoogleCloudDataplexV1AssetDiscoveryStatusOut": "_dataplex_97_GoogleCloudDataplexV1AssetDiscoveryStatusOut",
        "GoogleCloudDataplexV1DataQualityRuleSetExpectationIn": "_dataplex_98_GoogleCloudDataplexV1DataQualityRuleSetExpectationIn",
        "GoogleCloudDataplexV1DataQualityRuleSetExpectationOut": "_dataplex_99_GoogleCloudDataplexV1DataQualityRuleSetExpectationOut",
        "GoogleCloudDataplexV1EnvironmentIn": "_dataplex_100_GoogleCloudDataplexV1EnvironmentIn",
        "GoogleCloudDataplexV1EnvironmentOut": "_dataplex_101_GoogleCloudDataplexV1EnvironmentOut",
        "GoogleCloudDataplexV1DataScanEventDataQualityAppliedConfigsIn": "_dataplex_102_GoogleCloudDataplexV1DataScanEventDataQualityAppliedConfigsIn",
        "GoogleCloudDataplexV1DataScanEventDataQualityAppliedConfigsOut": "_dataplex_103_GoogleCloudDataplexV1DataScanEventDataQualityAppliedConfigsOut",
        "GoogleCloudDataplexV1ZoneResourceSpecIn": "_dataplex_104_GoogleCloudDataplexV1ZoneResourceSpecIn",
        "GoogleCloudDataplexV1ZoneResourceSpecOut": "_dataplex_105_GoogleCloudDataplexV1ZoneResourceSpecOut",
        "EmptyIn": "_dataplex_106_EmptyIn",
        "EmptyOut": "_dataplex_107_EmptyOut",
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIn": "_dataplex_108_GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIn",
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoOut": "_dataplex_109_GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoOut",
        "GoogleCloudDataplexV1LakeIn": "_dataplex_110_GoogleCloudDataplexV1LakeIn",
        "GoogleCloudDataplexV1LakeOut": "_dataplex_111_GoogleCloudDataplexV1LakeOut",
        "GoogleCloudDataplexV1DiscoveryEventConfigDetailsIn": "_dataplex_112_GoogleCloudDataplexV1DiscoveryEventConfigDetailsIn",
        "GoogleCloudDataplexV1DiscoveryEventConfigDetailsOut": "_dataplex_113_GoogleCloudDataplexV1DiscoveryEventConfigDetailsOut",
        "GoogleCloudDataplexV1DataScanEventDataQualityResultIn": "_dataplex_114_GoogleCloudDataplexV1DataScanEventDataQualityResultIn",
        "GoogleCloudDataplexV1DataScanEventDataQualityResultOut": "_dataplex_115_GoogleCloudDataplexV1DataScanEventDataQualityResultOut",
        "GoogleCloudDataplexV1PartitionIn": "_dataplex_116_GoogleCloudDataplexV1PartitionIn",
        "GoogleCloudDataplexV1PartitionOut": "_dataplex_117_GoogleCloudDataplexV1PartitionOut",
        "GoogleCloudDataplexV1DataProfileResultProfileIn": "_dataplex_118_GoogleCloudDataplexV1DataProfileResultProfileIn",
        "GoogleCloudDataplexV1DataProfileResultProfileOut": "_dataplex_119_GoogleCloudDataplexV1DataProfileResultProfileOut",
        "GoogleCloudDataplexV1TaskExecutionSpecIn": "_dataplex_120_GoogleCloudDataplexV1TaskExecutionSpecIn",
        "GoogleCloudDataplexV1TaskExecutionSpecOut": "_dataplex_121_GoogleCloudDataplexV1TaskExecutionSpecOut",
        "GoogleCloudDataplexV1SessionEventQueryDetailIn": "_dataplex_122_GoogleCloudDataplexV1SessionEventQueryDetailIn",
        "GoogleCloudDataplexV1SessionEventQueryDetailOut": "_dataplex_123_GoogleCloudDataplexV1SessionEventQueryDetailOut",
        "GoogleCloudDataplexV1TaskNotebookTaskConfigIn": "_dataplex_124_GoogleCloudDataplexV1TaskNotebookTaskConfigIn",
        "GoogleCloudDataplexV1TaskNotebookTaskConfigOut": "_dataplex_125_GoogleCloudDataplexV1TaskNotebookTaskConfigOut",
        "GoogleCloudDataplexV1DataScanEventIn": "_dataplex_126_GoogleCloudDataplexV1DataScanEventIn",
        "GoogleCloudDataplexV1DataScanEventOut": "_dataplex_127_GoogleCloudDataplexV1DataScanEventOut",
        "GoogleCloudDataplexV1TriggerOnDemandIn": "_dataplex_128_GoogleCloudDataplexV1TriggerOnDemandIn",
        "GoogleCloudDataplexV1TriggerOnDemandOut": "_dataplex_129_GoogleCloudDataplexV1TriggerOnDemandOut",
        "GoogleCloudDataplexV1ActionFailedSecurityPolicyApplyIn": "_dataplex_130_GoogleCloudDataplexV1ActionFailedSecurityPolicyApplyIn",
        "GoogleCloudDataplexV1ActionFailedSecurityPolicyApplyOut": "_dataplex_131_GoogleCloudDataplexV1ActionFailedSecurityPolicyApplyOut",
        "GoogleCloudDataplexV1DataScanJobIn": "_dataplex_132_GoogleCloudDataplexV1DataScanJobIn",
        "GoogleCloudDataplexV1DataScanJobOut": "_dataplex_133_GoogleCloudDataplexV1DataScanJobOut",
        "GoogleIamV1SetIamPolicyRequestIn": "_dataplex_134_GoogleIamV1SetIamPolicyRequestIn",
        "GoogleIamV1SetIamPolicyRequestOut": "_dataplex_135_GoogleIamV1SetIamPolicyRequestOut",
        "GoogleCloudDataplexV1ZoneIn": "_dataplex_136_GoogleCloudDataplexV1ZoneIn",
        "GoogleCloudDataplexV1ZoneOut": "_dataplex_137_GoogleCloudDataplexV1ZoneOut",
        "GoogleCloudDataplexV1TriggerIn": "_dataplex_138_GoogleCloudDataplexV1TriggerIn",
        "GoogleCloudDataplexV1TriggerOut": "_dataplex_139_GoogleCloudDataplexV1TriggerOut",
        "GoogleCloudDataplexV1ZoneDiscoverySpecJsonOptionsIn": "_dataplex_140_GoogleCloudDataplexV1ZoneDiscoverySpecJsonOptionsIn",
        "GoogleCloudDataplexV1ZoneDiscoverySpecJsonOptionsOut": "_dataplex_141_GoogleCloudDataplexV1ZoneDiscoverySpecJsonOptionsOut",
        "GoogleCloudDataplexV1ActionUnauthorizedResourceIn": "_dataplex_142_GoogleCloudDataplexV1ActionUnauthorizedResourceIn",
        "GoogleCloudDataplexV1ActionUnauthorizedResourceOut": "_dataplex_143_GoogleCloudDataplexV1ActionUnauthorizedResourceOut",
        "GoogleCloudDataplexV1ListTasksResponseIn": "_dataplex_144_GoogleCloudDataplexV1ListTasksResponseIn",
        "GoogleCloudDataplexV1ListTasksResponseOut": "_dataplex_145_GoogleCloudDataplexV1ListTasksResponseOut",
        "GoogleCloudDataplexV1EnvironmentSessionSpecIn": "_dataplex_146_GoogleCloudDataplexV1EnvironmentSessionSpecIn",
        "GoogleCloudDataplexV1EnvironmentSessionSpecOut": "_dataplex_147_GoogleCloudDataplexV1EnvironmentSessionSpecOut",
        "GoogleCloudDataplexV1DataScanEventDataProfileResultIn": "_dataplex_148_GoogleCloudDataplexV1DataScanEventDataProfileResultIn",
        "GoogleCloudDataplexV1DataScanEventDataProfileResultOut": "_dataplex_149_GoogleCloudDataplexV1DataScanEventDataProfileResultOut",
        "GoogleCloudDataplexV1DataQualityRuleTableConditionExpectationIn": "_dataplex_150_GoogleCloudDataplexV1DataQualityRuleTableConditionExpectationIn",
        "GoogleCloudDataplexV1DataQualityRuleTableConditionExpectationOut": "_dataplex_151_GoogleCloudDataplexV1DataQualityRuleTableConditionExpectationOut",
        "GoogleCloudDataplexV1TaskInfrastructureSpecContainerImageRuntimeIn": "_dataplex_152_GoogleCloudDataplexV1TaskInfrastructureSpecContainerImageRuntimeIn",
        "GoogleCloudDataplexV1TaskInfrastructureSpecContainerImageRuntimeOut": "_dataplex_153_GoogleCloudDataplexV1TaskInfrastructureSpecContainerImageRuntimeOut",
        "GoogleCloudDataplexV1DataProfileSpecSelectedFieldsIn": "_dataplex_154_GoogleCloudDataplexV1DataProfileSpecSelectedFieldsIn",
        "GoogleCloudDataplexV1DataProfileSpecSelectedFieldsOut": "_dataplex_155_GoogleCloudDataplexV1DataProfileSpecSelectedFieldsOut",
        "GoogleCloudDataplexV1ContentSqlScriptIn": "_dataplex_156_GoogleCloudDataplexV1ContentSqlScriptIn",
        "GoogleCloudDataplexV1ContentSqlScriptOut": "_dataplex_157_GoogleCloudDataplexV1ContentSqlScriptOut",
        "GoogleCloudDataplexV1StorageAccessIn": "_dataplex_158_GoogleCloudDataplexV1StorageAccessIn",
        "GoogleCloudDataplexV1StorageAccessOut": "_dataplex_159_GoogleCloudDataplexV1StorageAccessOut",
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIntegerFieldInfoIn": "_dataplex_160_GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIntegerFieldInfoIn",
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIntegerFieldInfoOut": "_dataplex_161_GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIntegerFieldInfoOut",
        "GoogleCloudDataplexV1DataSourceIn": "_dataplex_162_GoogleCloudDataplexV1DataSourceIn",
        "GoogleCloudDataplexV1DataSourceOut": "_dataplex_163_GoogleCloudDataplexV1DataSourceOut",
        "GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectationIn": "_dataplex_164_GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectationIn",
        "GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectationOut": "_dataplex_165_GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectationOut",
        "GoogleCloudDataplexV1DataQualityRuleResultIn": "_dataplex_166_GoogleCloudDataplexV1DataQualityRuleResultIn",
        "GoogleCloudDataplexV1DataQualityRuleResultOut": "_dataplex_167_GoogleCloudDataplexV1DataQualityRuleResultOut",
        "GoogleCloudDataplexV1JobIn": "_dataplex_168_GoogleCloudDataplexV1JobIn",
        "GoogleCloudDataplexV1JobOut": "_dataplex_169_GoogleCloudDataplexV1JobOut",
        "GoogleCloudDataplexV1RunTaskResponseIn": "_dataplex_170_GoogleCloudDataplexV1RunTaskResponseIn",
        "GoogleCloudDataplexV1RunTaskResponseOut": "_dataplex_171_GoogleCloudDataplexV1RunTaskResponseOut",
        "GoogleCloudDataplexV1ListPartitionsResponseIn": "_dataplex_172_GoogleCloudDataplexV1ListPartitionsResponseIn",
        "GoogleCloudDataplexV1ListPartitionsResponseOut": "_dataplex_173_GoogleCloudDataplexV1ListPartitionsResponseOut",
        "GoogleIamV1TestIamPermissionsResponseIn": "_dataplex_174_GoogleIamV1TestIamPermissionsResponseIn",
        "GoogleIamV1TestIamPermissionsResponseOut": "_dataplex_175_GoogleIamV1TestIamPermissionsResponseOut",
        "GoogleCloudDataplexV1ActionIncompatibleDataSchemaIn": "_dataplex_176_GoogleCloudDataplexV1ActionIncompatibleDataSchemaIn",
        "GoogleCloudDataplexV1ActionIncompatibleDataSchemaOut": "_dataplex_177_GoogleCloudDataplexV1ActionIncompatibleDataSchemaOut",
        "GoogleCloudDataplexV1SchemaSchemaFieldIn": "_dataplex_178_GoogleCloudDataplexV1SchemaSchemaFieldIn",
        "GoogleCloudDataplexV1SchemaSchemaFieldOut": "_dataplex_179_GoogleCloudDataplexV1SchemaSchemaFieldOut",
        "GoogleCloudDataplexV1ListDataAttributesResponseIn": "_dataplex_180_GoogleCloudDataplexV1ListDataAttributesResponseIn",
        "GoogleCloudDataplexV1ListDataAttributesResponseOut": "_dataplex_181_GoogleCloudDataplexV1ListDataAttributesResponseOut",
        "GoogleIamV1BindingIn": "_dataplex_182_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_dataplex_183_GoogleIamV1BindingOut",
        "GoogleCloudDataplexV1DataAttributeBindingPathIn": "_dataplex_184_GoogleCloudDataplexV1DataAttributeBindingPathIn",
        "GoogleCloudDataplexV1DataAttributeBindingPathOut": "_dataplex_185_GoogleCloudDataplexV1DataAttributeBindingPathOut",
        "GoogleCloudDataplexV1TaskIn": "_dataplex_186_GoogleCloudDataplexV1TaskIn",
        "GoogleCloudDataplexV1TaskOut": "_dataplex_187_GoogleCloudDataplexV1TaskOut",
        "GoogleLongrunningListOperationsResponseIn": "_dataplex_188_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_dataplex_189_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudDataplexV1CancelJobRequestIn": "_dataplex_190_GoogleCloudDataplexV1CancelJobRequestIn",
        "GoogleCloudDataplexV1CancelJobRequestOut": "_dataplex_191_GoogleCloudDataplexV1CancelJobRequestOut",
        "GoogleCloudDataplexV1RunTaskRequestIn": "_dataplex_192_GoogleCloudDataplexV1RunTaskRequestIn",
        "GoogleCloudDataplexV1RunTaskRequestOut": "_dataplex_193_GoogleCloudDataplexV1RunTaskRequestOut",
        "GoogleCloudDataplexV1DataScanExecutionStatusIn": "_dataplex_194_GoogleCloudDataplexV1DataScanExecutionStatusIn",
        "GoogleCloudDataplexV1DataScanExecutionStatusOut": "_dataplex_195_GoogleCloudDataplexV1DataScanExecutionStatusOut",
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoStringFieldInfoIn": "_dataplex_196_GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoStringFieldInfoIn",
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoStringFieldInfoOut": "_dataplex_197_GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoStringFieldInfoOut",
        "GoogleCloudDataplexV1DataQualityRuleRowConditionExpectationIn": "_dataplex_198_GoogleCloudDataplexV1DataQualityRuleRowConditionExpectationIn",
        "GoogleCloudDataplexV1DataQualityRuleRowConditionExpectationOut": "_dataplex_199_GoogleCloudDataplexV1DataQualityRuleRowConditionExpectationOut",
        "GoogleCloudDataplexV1AssetDiscoverySpecIn": "_dataplex_200_GoogleCloudDataplexV1AssetDiscoverySpecIn",
        "GoogleCloudDataplexV1AssetDiscoverySpecOut": "_dataplex_201_GoogleCloudDataplexV1AssetDiscoverySpecOut",
        "GoogleCloudDataplexV1AssetResourceStatusIn": "_dataplex_202_GoogleCloudDataplexV1AssetResourceStatusIn",
        "GoogleCloudDataplexV1AssetResourceStatusOut": "_dataplex_203_GoogleCloudDataplexV1AssetResourceStatusOut",
        "GoogleIamV1PolicyIn": "_dataplex_204_GoogleIamV1PolicyIn",
        "GoogleIamV1PolicyOut": "_dataplex_205_GoogleIamV1PolicyOut",
        "GoogleCloudDataplexV1DataQualityRuleRangeExpectationIn": "_dataplex_206_GoogleCloudDataplexV1DataQualityRuleRangeExpectationIn",
        "GoogleCloudDataplexV1DataQualityRuleRangeExpectationOut": "_dataplex_207_GoogleCloudDataplexV1DataQualityRuleRangeExpectationOut",
        "GoogleCloudDataplexV1ListZonesResponseIn": "_dataplex_208_GoogleCloudDataplexV1ListZonesResponseIn",
        "GoogleCloudDataplexV1ListZonesResponseOut": "_dataplex_209_GoogleCloudDataplexV1ListZonesResponseOut",
        "GoogleCloudDataplexV1TaskTriggerSpecIn": "_dataplex_210_GoogleCloudDataplexV1TaskTriggerSpecIn",
        "GoogleCloudDataplexV1TaskTriggerSpecOut": "_dataplex_211_GoogleCloudDataplexV1TaskTriggerSpecOut",
        "GoogleCloudDataplexV1AssetDiscoverySpecCsvOptionsIn": "_dataplex_212_GoogleCloudDataplexV1AssetDiscoverySpecCsvOptionsIn",
        "GoogleCloudDataplexV1AssetDiscoverySpecCsvOptionsOut": "_dataplex_213_GoogleCloudDataplexV1AssetDiscoverySpecCsvOptionsOut",
        "GoogleCloudDataplexV1ListDataAttributeBindingsResponseIn": "_dataplex_214_GoogleCloudDataplexV1ListDataAttributeBindingsResponseIn",
        "GoogleCloudDataplexV1ListDataAttributeBindingsResponseOut": "_dataplex_215_GoogleCloudDataplexV1ListDataAttributeBindingsResponseOut",
        "GoogleCloudDataplexV1ActionMissingDataIn": "_dataplex_216_GoogleCloudDataplexV1ActionMissingDataIn",
        "GoogleCloudDataplexV1ActionMissingDataOut": "_dataplex_217_GoogleCloudDataplexV1ActionMissingDataOut",
        "GoogleCloudDataplexV1EnvironmentEndpointsIn": "_dataplex_218_GoogleCloudDataplexV1EnvironmentEndpointsIn",
        "GoogleCloudDataplexV1EnvironmentEndpointsOut": "_dataplex_219_GoogleCloudDataplexV1EnvironmentEndpointsOut",
        "GoogleIamV1TestIamPermissionsRequestIn": "_dataplex_220_GoogleIamV1TestIamPermissionsRequestIn",
        "GoogleIamV1TestIamPermissionsRequestOut": "_dataplex_221_GoogleIamV1TestIamPermissionsRequestOut",
        "GoogleTypeExprIn": "_dataplex_222_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_dataplex_223_GoogleTypeExprOut",
        "GoogleIamV1AuditConfigIn": "_dataplex_224_GoogleIamV1AuditConfigIn",
        "GoogleIamV1AuditConfigOut": "_dataplex_225_GoogleIamV1AuditConfigOut",
        "GoogleCloudDataplexV1StorageFormatJsonOptionsIn": "_dataplex_226_GoogleCloudDataplexV1StorageFormatJsonOptionsIn",
        "GoogleCloudDataplexV1StorageFormatJsonOptionsOut": "_dataplex_227_GoogleCloudDataplexV1StorageFormatJsonOptionsOut",
        "GoogleCloudDataplexV1ListSessionsResponseIn": "_dataplex_228_GoogleCloudDataplexV1ListSessionsResponseIn",
        "GoogleCloudDataplexV1ListSessionsResponseOut": "_dataplex_229_GoogleCloudDataplexV1ListSessionsResponseOut",
        "GoogleCloudDataplexV1DataScanEventDataProfileAppliedConfigsIn": "_dataplex_230_GoogleCloudDataplexV1DataScanEventDataProfileAppliedConfigsIn",
        "GoogleCloudDataplexV1DataScanEventDataProfileAppliedConfigsOut": "_dataplex_231_GoogleCloudDataplexV1DataScanEventDataProfileAppliedConfigsOut",
        "GoogleCloudDataplexV1SchemaIn": "_dataplex_232_GoogleCloudDataplexV1SchemaIn",
        "GoogleCloudDataplexV1SchemaOut": "_dataplex_233_GoogleCloudDataplexV1SchemaOut",
        "GoogleCloudDataplexV1ScannedDataIncrementalFieldIn": "_dataplex_234_GoogleCloudDataplexV1ScannedDataIncrementalFieldIn",
        "GoogleCloudDataplexV1ScannedDataIncrementalFieldOut": "_dataplex_235_GoogleCloudDataplexV1ScannedDataIncrementalFieldOut",
        "GoogleCloudDataplexV1DataScanIn": "_dataplex_236_GoogleCloudDataplexV1DataScanIn",
        "GoogleCloudDataplexV1DataScanOut": "_dataplex_237_GoogleCloudDataplexV1DataScanOut",
        "GoogleCloudLocationListLocationsResponseIn": "_dataplex_238_GoogleCloudLocationListLocationsResponseIn",
        "GoogleCloudLocationListLocationsResponseOut": "_dataplex_239_GoogleCloudLocationListLocationsResponseOut",
        "GoogleCloudLocationLocationIn": "_dataplex_240_GoogleCloudLocationLocationIn",
        "GoogleCloudLocationLocationOut": "_dataplex_241_GoogleCloudLocationLocationOut",
        "GoogleCloudDataplexV1DataQualitySpecIn": "_dataplex_242_GoogleCloudDataplexV1DataQualitySpecIn",
        "GoogleCloudDataplexV1DataQualitySpecOut": "_dataplex_243_GoogleCloudDataplexV1DataQualitySpecOut",
        "GoogleCloudDataplexV1StorageFormatCsvOptionsIn": "_dataplex_244_GoogleCloudDataplexV1StorageFormatCsvOptionsIn",
        "GoogleCloudDataplexV1StorageFormatCsvOptionsOut": "_dataplex_245_GoogleCloudDataplexV1StorageFormatCsvOptionsOut",
        "GoogleCloudDataplexV1EnvironmentInfrastructureSpecComputeResourcesIn": "_dataplex_246_GoogleCloudDataplexV1EnvironmentInfrastructureSpecComputeResourcesIn",
        "GoogleCloudDataplexV1EnvironmentInfrastructureSpecComputeResourcesOut": "_dataplex_247_GoogleCloudDataplexV1EnvironmentInfrastructureSpecComputeResourcesOut",
        "GoogleCloudDataplexV1EnvironmentInfrastructureSpecIn": "_dataplex_248_GoogleCloudDataplexV1EnvironmentInfrastructureSpecIn",
        "GoogleCloudDataplexV1EnvironmentInfrastructureSpecOut": "_dataplex_249_GoogleCloudDataplexV1EnvironmentInfrastructureSpecOut",
        "GoogleCloudDataplexV1DataQualityResultIn": "_dataplex_250_GoogleCloudDataplexV1DataQualityResultIn",
        "GoogleCloudDataplexV1DataQualityResultOut": "_dataplex_251_GoogleCloudDataplexV1DataQualityResultOut",
        "GoogleCloudDataplexV1ActionInvalidDataPartitionIn": "_dataplex_252_GoogleCloudDataplexV1ActionInvalidDataPartitionIn",
        "GoogleCloudDataplexV1ActionInvalidDataPartitionOut": "_dataplex_253_GoogleCloudDataplexV1ActionInvalidDataPartitionOut",
        "GoogleCloudDataplexV1TriggerScheduleIn": "_dataplex_254_GoogleCloudDataplexV1TriggerScheduleIn",
        "GoogleCloudDataplexV1TriggerScheduleOut": "_dataplex_255_GoogleCloudDataplexV1TriggerScheduleOut",
        "GoogleCloudDataplexV1TaskInfrastructureSpecBatchComputeResourcesIn": "_dataplex_256_GoogleCloudDataplexV1TaskInfrastructureSpecBatchComputeResourcesIn",
        "GoogleCloudDataplexV1TaskInfrastructureSpecBatchComputeResourcesOut": "_dataplex_257_GoogleCloudDataplexV1TaskInfrastructureSpecBatchComputeResourcesOut",
        "GoogleCloudDataplexV1TaskInfrastructureSpecIn": "_dataplex_258_GoogleCloudDataplexV1TaskInfrastructureSpecIn",
        "GoogleCloudDataplexV1TaskInfrastructureSpecOut": "_dataplex_259_GoogleCloudDataplexV1TaskInfrastructureSpecOut",
        "GoogleIamV1AuditLogConfigIn": "_dataplex_260_GoogleIamV1AuditLogConfigIn",
        "GoogleIamV1AuditLogConfigOut": "_dataplex_261_GoogleIamV1AuditLogConfigOut",
        "GoogleCloudDataplexV1DataScanEventPostScanActionsResultBigQueryExportResultIn": "_dataplex_262_GoogleCloudDataplexV1DataScanEventPostScanActionsResultBigQueryExportResultIn",
        "GoogleCloudDataplexV1DataScanEventPostScanActionsResultBigQueryExportResultOut": "_dataplex_263_GoogleCloudDataplexV1DataScanEventPostScanActionsResultBigQueryExportResultOut",
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoDoubleFieldInfoIn": "_dataplex_264_GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoDoubleFieldInfoIn",
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoDoubleFieldInfoOut": "_dataplex_265_GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoDoubleFieldInfoOut",
        "GoogleCloudDataplexV1RunDataScanResponseIn": "_dataplex_266_GoogleCloudDataplexV1RunDataScanResponseIn",
        "GoogleCloudDataplexV1RunDataScanResponseOut": "_dataplex_267_GoogleCloudDataplexV1RunDataScanResponseOut",
        "GoogleCloudDataplexV1DataProfileResultProfileFieldIn": "_dataplex_268_GoogleCloudDataplexV1DataProfileResultProfileFieldIn",
        "GoogleCloudDataplexV1DataProfileResultProfileFieldOut": "_dataplex_269_GoogleCloudDataplexV1DataProfileResultProfileFieldOut",
        "GoogleCloudDataplexV1DataQualityDimensionResultIn": "_dataplex_270_GoogleCloudDataplexV1DataQualityDimensionResultIn",
        "GoogleCloudDataplexV1DataQualityDimensionResultOut": "_dataplex_271_GoogleCloudDataplexV1DataQualityDimensionResultOut",
        "GoogleCloudDataplexV1TaskInfrastructureSpecVpcNetworkIn": "_dataplex_272_GoogleCloudDataplexV1TaskInfrastructureSpecVpcNetworkIn",
        "GoogleCloudDataplexV1TaskInfrastructureSpecVpcNetworkOut": "_dataplex_273_GoogleCloudDataplexV1TaskInfrastructureSpecVpcNetworkOut",
        "GoogleCloudDataplexV1DataQualityRuleNonNullExpectationIn": "_dataplex_274_GoogleCloudDataplexV1DataQualityRuleNonNullExpectationIn",
        "GoogleCloudDataplexV1DataQualityRuleNonNullExpectationOut": "_dataplex_275_GoogleCloudDataplexV1DataQualityRuleNonNullExpectationOut",
        "GoogleCloudDataplexV1ContentIn": "_dataplex_276_GoogleCloudDataplexV1ContentIn",
        "GoogleCloudDataplexV1ContentOut": "_dataplex_277_GoogleCloudDataplexV1ContentOut",
        "GoogleCloudDataplexV1ActionIn": "_dataplex_278_GoogleCloudDataplexV1ActionIn",
        "GoogleCloudDataplexV1ActionOut": "_dataplex_279_GoogleCloudDataplexV1ActionOut",
        "GoogleCloudDataplexV1EntityCompatibilityStatusIn": "_dataplex_280_GoogleCloudDataplexV1EntityCompatibilityStatusIn",
        "GoogleCloudDataplexV1EntityCompatibilityStatusOut": "_dataplex_281_GoogleCloudDataplexV1EntityCompatibilityStatusOut",
        "GoogleCloudDataplexV1SchemaPartitionFieldIn": "_dataplex_282_GoogleCloudDataplexV1SchemaPartitionFieldIn",
        "GoogleCloudDataplexV1SchemaPartitionFieldOut": "_dataplex_283_GoogleCloudDataplexV1SchemaPartitionFieldOut",
        "GoogleCloudDataplexV1TaskExecutionStatusIn": "_dataplex_284_GoogleCloudDataplexV1TaskExecutionStatusIn",
        "GoogleCloudDataplexV1TaskExecutionStatusOut": "_dataplex_285_GoogleCloudDataplexV1TaskExecutionStatusOut",
        "GoogleCloudDataplexV1SessionEventIn": "_dataplex_286_GoogleCloudDataplexV1SessionEventIn",
        "GoogleCloudDataplexV1SessionEventOut": "_dataplex_287_GoogleCloudDataplexV1SessionEventOut",
        "GoogleCloudDataplexV1StorageFormatIn": "_dataplex_288_GoogleCloudDataplexV1StorageFormatIn",
        "GoogleCloudDataplexV1StorageFormatOut": "_dataplex_289_GoogleCloudDataplexV1StorageFormatOut",
        "GoogleRpcStatusIn": "_dataplex_290_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_dataplex_291_GoogleRpcStatusOut",
        "GoogleCloudDataplexV1ListDataTaxonomiesResponseIn": "_dataplex_292_GoogleCloudDataplexV1ListDataTaxonomiesResponseIn",
        "GoogleCloudDataplexV1ListDataTaxonomiesResponseOut": "_dataplex_293_GoogleCloudDataplexV1ListDataTaxonomiesResponseOut",
        "GoogleCloudDataplexV1ResourceAccessSpecIn": "_dataplex_294_GoogleCloudDataplexV1ResourceAccessSpecIn",
        "GoogleCloudDataplexV1ResourceAccessSpecOut": "_dataplex_295_GoogleCloudDataplexV1ResourceAccessSpecOut",
        "GoogleCloudDataplexV1DataQualityRuleIn": "_dataplex_296_GoogleCloudDataplexV1DataQualityRuleIn",
        "GoogleCloudDataplexV1DataQualityRuleOut": "_dataplex_297_GoogleCloudDataplexV1DataQualityRuleOut",
        "GoogleCloudDataplexV1LakeMetastoreIn": "_dataplex_298_GoogleCloudDataplexV1LakeMetastoreIn",
        "GoogleCloudDataplexV1LakeMetastoreOut": "_dataplex_299_GoogleCloudDataplexV1LakeMetastoreOut",
        "GoogleLongrunningCancelOperationRequestIn": "_dataplex_300_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_dataplex_301_GoogleLongrunningCancelOperationRequestOut",
        "GoogleCloudDataplexV1StorageFormatIcebergOptionsIn": "_dataplex_302_GoogleCloudDataplexV1StorageFormatIcebergOptionsIn",
        "GoogleCloudDataplexV1StorageFormatIcebergOptionsOut": "_dataplex_303_GoogleCloudDataplexV1StorageFormatIcebergOptionsOut",
        "GoogleCloudDataplexV1EntityCompatibilityStatusCompatibilityIn": "_dataplex_304_GoogleCloudDataplexV1EntityCompatibilityStatusCompatibilityIn",
        "GoogleCloudDataplexV1EntityCompatibilityStatusCompatibilityOut": "_dataplex_305_GoogleCloudDataplexV1EntityCompatibilityStatusCompatibilityOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudDataplexV1DataTaxonomyIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "etag": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataTaxonomyIn"])
    types["GoogleCloudDataplexV1DataTaxonomyOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "etag": t.string().optional(),
            "attributeCount": t.integer().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "uid": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataTaxonomyOut"])
    types[
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoTopNValueIn"
    ] = t.struct(
        {
            "value": t.string().optional(),
            "ratio": t.number().optional(),
            "count": t.string().optional(),
        }
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
            "ratio": t.number().optional(),
            "count": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoTopNValueOut"
        ]
    )
    types["GoogleCloudDataplexV1DataProfileResultIn"] = t.struct(
        {
            "scannedData": t.proxy(
                renames["GoogleCloudDataplexV1ScannedDataIn"]
            ).optional(),
            "rowCount": t.string().optional(),
            "profile": t.proxy(
                renames["GoogleCloudDataplexV1DataProfileResultProfileIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataProfileResultIn"])
    types["GoogleCloudDataplexV1DataProfileResultOut"] = t.struct(
        {
            "scannedData": t.proxy(
                renames["GoogleCloudDataplexV1ScannedDataOut"]
            ).optional(),
            "rowCount": t.string().optional(),
            "profile": t.proxy(
                renames["GoogleCloudDataplexV1DataProfileResultProfileOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataProfileResultOut"])
    types["GoogleCloudDataplexV1ContentNotebookIn"] = t.struct(
        {"kernelType": t.string()}
    ).named(renames["GoogleCloudDataplexV1ContentNotebookIn"])
    types["GoogleCloudDataplexV1ContentNotebookOut"] = t.struct(
        {
            "kernelType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ContentNotebookOut"])
    types["GoogleCloudDataplexV1DataScanExecutionSpecIn"] = t.struct(
        {
            "trigger": t.proxy(renames["GoogleCloudDataplexV1TriggerIn"]).optional(),
            "field": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanExecutionSpecIn"])
    types["GoogleCloudDataplexV1DataScanExecutionSpecOut"] = t.struct(
        {
            "trigger": t.proxy(renames["GoogleCloudDataplexV1TriggerOut"]).optional(),
            "field": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanExecutionSpecOut"])
    types["GoogleCloudDataplexV1AssetStatusIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "activeAssets": t.integer().optional(),
            "securityPolicyApplyingAssets": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetStatusIn"])
    types["GoogleCloudDataplexV1AssetStatusOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "activeAssets": t.integer().optional(),
            "securityPolicyApplyingAssets": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetStatusOut"])
    types["GoogleCloudDataplexV1ListEntitiesResponseIn"] = t.struct(
        {
            "entities": t.array(
                t.proxy(renames["GoogleCloudDataplexV1EntityIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListEntitiesResponseIn"])
    types["GoogleCloudDataplexV1ListEntitiesResponseOut"] = t.struct(
        {
            "entities": t.array(
                t.proxy(renames["GoogleCloudDataplexV1EntityOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListEntitiesResponseOut"])
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
    types["GoogleCloudDataplexV1ListLakesResponseIn"] = t.struct(
        {
            "lakes": t.array(
                t.proxy(renames["GoogleCloudDataplexV1LakeIn"])
            ).optional(),
            "unreachableLocations": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListLakesResponseIn"])
    types["GoogleCloudDataplexV1ListLakesResponseOut"] = t.struct(
        {
            "lakes": t.array(
                t.proxy(renames["GoogleCloudDataplexV1LakeOut"])
            ).optional(),
            "unreachableLocations": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListLakesResponseOut"])
    types["GoogleCloudDataplexV1ActionInvalidDataOrganizationIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1ActionInvalidDataOrganizationIn"])
    types["GoogleCloudDataplexV1ActionInvalidDataOrganizationOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDataplexV1ActionInvalidDataOrganizationOut"])
    types["GoogleCloudDataplexV1RunDataScanRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1RunDataScanRequestIn"])
    types["GoogleCloudDataplexV1RunDataScanRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDataplexV1RunDataScanRequestOut"])
    types["GoogleCloudDataplexV1DataProfileSpecIn"] = t.struct(
        {
            "excludeFields": t.proxy(
                renames["GoogleCloudDataplexV1DataProfileSpecSelectedFieldsIn"]
            ).optional(),
            "includeFields": t.proxy(
                renames["GoogleCloudDataplexV1DataProfileSpecSelectedFieldsIn"]
            ).optional(),
            "rowFilter": t.string().optional(),
            "samplingPercent": t.number().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataProfileSpecIn"])
    types["GoogleCloudDataplexV1DataProfileSpecOut"] = t.struct(
        {
            "excludeFields": t.proxy(
                renames["GoogleCloudDataplexV1DataProfileSpecSelectedFieldsOut"]
            ).optional(),
            "includeFields": t.proxy(
                renames["GoogleCloudDataplexV1DataProfileSpecSelectedFieldsOut"]
            ).optional(),
            "rowFilter": t.string().optional(),
            "samplingPercent": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataProfileSpecOut"])
    types["GoogleCloudDataplexV1ListDataScansResponseIn"] = t.struct(
        {
            "dataScans": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataScanIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListDataScansResponseIn"])
    types["GoogleCloudDataplexV1ListDataScansResponseOut"] = t.struct(
        {
            "dataScans": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataScanOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListDataScansResponseOut"])
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
    types["GoogleCloudDataplexV1DiscoveryEventPartitionDetailsIn"] = t.struct(
        {
            "sampledDataLocations": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "partition": t.string().optional(),
            "entity": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DiscoveryEventPartitionDetailsIn"])
    types["GoogleCloudDataplexV1DiscoveryEventPartitionDetailsOut"] = t.struct(
        {
            "sampledDataLocations": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "partition": t.string().optional(),
            "entity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DiscoveryEventPartitionDetailsOut"])
    types[
        "GoogleCloudDataplexV1EnvironmentInfrastructureSpecOsImageRuntimeIn"
    ] = t.struct(
        {
            "imageVersion": t.string(),
            "javaLibraries": t.array(t.string()).optional(),
            "pythonPackages": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(
        renames["GoogleCloudDataplexV1EnvironmentInfrastructureSpecOsImageRuntimeIn"]
    )
    types[
        "GoogleCloudDataplexV1EnvironmentInfrastructureSpecOsImageRuntimeOut"
    ] = t.struct(
        {
            "imageVersion": t.string(),
            "javaLibraries": t.array(t.string()).optional(),
            "pythonPackages": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDataplexV1EnvironmentInfrastructureSpecOsImageRuntimeOut"]
    )
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
    types["GoogleCloudDataplexV1DiscoveryEventIn"] = t.struct(
        {
            "dataLocation": t.string().optional(),
            "assetId": t.string().optional(),
            "lakeId": t.string().optional(),
            "entity": t.proxy(
                renames["GoogleCloudDataplexV1DiscoveryEventEntityDetailsIn"]
            ).optional(),
            "zoneId": t.string().optional(),
            "message": t.string().optional(),
            "config": t.proxy(
                renames["GoogleCloudDataplexV1DiscoveryEventConfigDetailsIn"]
            ).optional(),
            "type": t.string().optional(),
            "action": t.proxy(
                renames["GoogleCloudDataplexV1DiscoveryEventActionDetailsIn"]
            ).optional(),
            "partition": t.proxy(
                renames["GoogleCloudDataplexV1DiscoveryEventPartitionDetailsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DiscoveryEventIn"])
    types["GoogleCloudDataplexV1DiscoveryEventOut"] = t.struct(
        {
            "dataLocation": t.string().optional(),
            "assetId": t.string().optional(),
            "lakeId": t.string().optional(),
            "entity": t.proxy(
                renames["GoogleCloudDataplexV1DiscoveryEventEntityDetailsOut"]
            ).optional(),
            "zoneId": t.string().optional(),
            "message": t.string().optional(),
            "config": t.proxy(
                renames["GoogleCloudDataplexV1DiscoveryEventConfigDetailsOut"]
            ).optional(),
            "type": t.string().optional(),
            "action": t.proxy(
                renames["GoogleCloudDataplexV1DiscoveryEventActionDetailsOut"]
            ).optional(),
            "partition": t.proxy(
                renames["GoogleCloudDataplexV1DiscoveryEventPartitionDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DiscoveryEventOut"])
    types["GoogleCloudDataplexV1DataAccessSpecIn"] = t.struct(
        {"readers": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudDataplexV1DataAccessSpecIn"])
    types["GoogleCloudDataplexV1DataAccessSpecOut"] = t.struct(
        {
            "readers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataAccessSpecOut"])
    types["GoogleCloudDataplexV1SessionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1SessionIn"])
    types["GoogleCloudDataplexV1SessionOut"] = t.struct(
        {
            "userId": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1SessionOut"])
    types["GoogleCloudDataplexV1ZoneDiscoverySpecCsvOptionsIn"] = t.struct(
        {
            "encoding": t.string().optional(),
            "disableTypeInference": t.boolean().optional(),
            "delimiter": t.string().optional(),
            "headerRows": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ZoneDiscoverySpecCsvOptionsIn"])
    types["GoogleCloudDataplexV1ZoneDiscoverySpecCsvOptionsOut"] = t.struct(
        {
            "encoding": t.string().optional(),
            "disableTypeInference": t.boolean().optional(),
            "delimiter": t.string().optional(),
            "headerRows": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ZoneDiscoverySpecCsvOptionsOut"])
    types["GoogleCloudDataplexV1ListAssetsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assets": t.array(
                t.proxy(renames["GoogleCloudDataplexV1AssetIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListAssetsResponseIn"])
    types["GoogleCloudDataplexV1ListAssetsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assets": t.array(
                t.proxy(renames["GoogleCloudDataplexV1AssetOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListAssetsResponseOut"])
    types["GoogleCloudDataplexV1DataScanEventPostScanActionsResultIn"] = t.struct(
        {
            "bigqueryExportResult": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataScanEventPostScanActionsResultBigQueryExportResultIn"
                ]
            ).optional()
        }
    ).named(renames["GoogleCloudDataplexV1DataScanEventPostScanActionsResultIn"])
    types["GoogleCloudDataplexV1DataScanEventPostScanActionsResultOut"] = t.struct(
        {
            "bigqueryExportResult": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataScanEventPostScanActionsResultBigQueryExportResultOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanEventPostScanActionsResultOut"])
    types["GoogleCloudDataplexV1EnvironmentSessionStatusIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1EnvironmentSessionStatusIn"])
    types["GoogleCloudDataplexV1EnvironmentSessionStatusOut"] = t.struct(
        {
            "active": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1EnvironmentSessionStatusOut"])
    types["GoogleCloudDataplexV1DataAttributeIn"] = t.struct(
        {
            "parentId": t.string().optional(),
            "displayName": t.string().optional(),
            "etag": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "dataAccessSpec": t.proxy(
                renames["GoogleCloudDataplexV1DataAccessSpecIn"]
            ).optional(),
            "resourceAccessSpec": t.proxy(
                renames["GoogleCloudDataplexV1ResourceAccessSpecIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataAttributeIn"])
    types["GoogleCloudDataplexV1DataAttributeOut"] = t.struct(
        {
            "parentId": t.string().optional(),
            "displayName": t.string().optional(),
            "uid": t.string().optional(),
            "createTime": t.string().optional(),
            "etag": t.string().optional(),
            "attributeCount": t.integer().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "dataAccessSpec": t.proxy(
                renames["GoogleCloudDataplexV1DataAccessSpecOut"]
            ).optional(),
            "resourceAccessSpec": t.proxy(
                renames["GoogleCloudDataplexV1ResourceAccessSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataAttributeOut"])
    types["GoogleCloudDataplexV1DiscoveryEventActionDetailsIn"] = t.struct(
        {"type": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1DiscoveryEventActionDetailsIn"])
    types["GoogleCloudDataplexV1DiscoveryEventActionDetailsOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DiscoveryEventActionDetailsOut"])
    types["GoogleCloudDataplexV1AssetResourceSpecIn"] = t.struct(
        {
            "type": t.string(),
            "readAccessMode": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetResourceSpecIn"])
    types["GoogleCloudDataplexV1AssetResourceSpecOut"] = t.struct(
        {
            "type": t.string(),
            "readAccessMode": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetResourceSpecOut"])
    types["GoogleCloudDataplexV1AssetIn"] = t.struct(
        {
            "discoverySpec": t.proxy(
                renames["GoogleCloudDataplexV1AssetDiscoverySpecIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "resourceSpec": t.proxy(
                renames["GoogleCloudDataplexV1AssetResourceSpecIn"]
            ),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetIn"])
    types["GoogleCloudDataplexV1AssetOut"] = t.struct(
        {
            "discoverySpec": t.proxy(
                renames["GoogleCloudDataplexV1AssetDiscoverySpecOut"]
            ).optional(),
            "uid": t.string().optional(),
            "securityStatus": t.proxy(
                renames["GoogleCloudDataplexV1AssetSecurityStatusOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "resourceSpec": t.proxy(
                renames["GoogleCloudDataplexV1AssetResourceSpecOut"]
            ),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "discoveryStatus": t.proxy(
                renames["GoogleCloudDataplexV1AssetDiscoveryStatusOut"]
            ).optional(),
            "resourceStatus": t.proxy(
                renames["GoogleCloudDataplexV1AssetResourceStatusOut"]
            ).optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleCloudDataplexV1AssetDiscoverySpecJsonOptionsIn"] = t.struct(
        {
            "disableTypeInference": t.boolean().optional(),
            "encoding": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetDiscoverySpecJsonOptionsIn"])
    types["GoogleCloudDataplexV1AssetDiscoverySpecJsonOptionsOut"] = t.struct(
        {
            "disableTypeInference": t.boolean().optional(),
            "encoding": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetDiscoverySpecJsonOptionsOut"])
    types["GoogleCloudDataplexV1AssetSecurityStatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetSecurityStatusIn"])
    types["GoogleCloudDataplexV1AssetSecurityStatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetSecurityStatusOut"])
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
    types["GoogleCloudDataplexV1ListJobsResponseIn"] = t.struct(
        {
            "jobs": t.array(t.proxy(renames["GoogleCloudDataplexV1JobIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListJobsResponseIn"])
    types["GoogleCloudDataplexV1ListJobsResponseOut"] = t.struct(
        {
            "jobs": t.array(t.proxy(renames["GoogleCloudDataplexV1JobOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListJobsResponseOut"])
    types["GoogleCloudDataplexV1ActionMissingResourceIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1ActionMissingResourceIn"])
    types["GoogleCloudDataplexV1ActionMissingResourceOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDataplexV1ActionMissingResourceOut"])
    types["GoogleCloudDataplexV1AssetDiscoveryStatusStatsIn"] = t.struct(
        {
            "tables": t.string().optional(),
            "dataSize": t.string().optional(),
            "dataItems": t.string().optional(),
            "filesets": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetDiscoveryStatusStatsIn"])
    types["GoogleCloudDataplexV1AssetDiscoveryStatusStatsOut"] = t.struct(
        {
            "tables": t.string().optional(),
            "dataSize": t.string().optional(),
            "dataItems": t.string().optional(),
            "filesets": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetDiscoveryStatusStatsOut"])
    types["GoogleCloudDataplexV1LakeMetastoreStatusIn"] = t.struct(
        {
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "message": t.string().optional(),
            "endpoint": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1LakeMetastoreStatusIn"])
    types["GoogleCloudDataplexV1LakeMetastoreStatusOut"] = t.struct(
        {
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "message": t.string().optional(),
            "endpoint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1LakeMetastoreStatusOut"])
    types["GoogleCloudDataplexV1TaskSparkTaskConfigIn"] = t.struct(
        {
            "sqlScript": t.string().optional(),
            "archiveUris": t.array(t.string()).optional(),
            "infrastructureSpec": t.proxy(
                renames["GoogleCloudDataplexV1TaskInfrastructureSpecIn"]
            ).optional(),
            "fileUris": t.array(t.string()).optional(),
            "mainJarFileUri": t.string().optional(),
            "pythonScriptFile": t.string().optional(),
            "mainClass": t.string().optional(),
            "sqlScriptFile": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TaskSparkTaskConfigIn"])
    types["GoogleCloudDataplexV1TaskSparkTaskConfigOut"] = t.struct(
        {
            "sqlScript": t.string().optional(),
            "archiveUris": t.array(t.string()).optional(),
            "infrastructureSpec": t.proxy(
                renames["GoogleCloudDataplexV1TaskInfrastructureSpecOut"]
            ).optional(),
            "fileUris": t.array(t.string()).optional(),
            "mainJarFileUri": t.string().optional(),
            "pythonScriptFile": t.string().optional(),
            "mainClass": t.string().optional(),
            "sqlScriptFile": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TaskSparkTaskConfigOut"])
    types["GoogleCloudDataplexV1JobEventIn"] = t.struct(
        {
            "serviceJob": t.string().optional(),
            "jobId": t.string().optional(),
            "message": t.string().optional(),
            "state": t.string().optional(),
            "executionTrigger": t.string().optional(),
            "startTime": t.string().optional(),
            "retries": t.integer().optional(),
            "type": t.string().optional(),
            "service": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1JobEventIn"])
    types["GoogleCloudDataplexV1JobEventOut"] = t.struct(
        {
            "serviceJob": t.string().optional(),
            "jobId": t.string().optional(),
            "message": t.string().optional(),
            "state": t.string().optional(),
            "executionTrigger": t.string().optional(),
            "startTime": t.string().optional(),
            "retries": t.integer().optional(),
            "type": t.string().optional(),
            "service": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1JobEventOut"])
    types["GoogleCloudDataplexV1ListEnvironmentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "environments": t.array(
                t.proxy(renames["GoogleCloudDataplexV1EnvironmentIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListEnvironmentsResponseIn"])
    types["GoogleCloudDataplexV1ListEnvironmentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "environments": t.array(
                t.proxy(renames["GoogleCloudDataplexV1EnvironmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListEnvironmentsResponseOut"])
    types["GoogleCloudDataplexV1ZoneDiscoverySpecIn"] = t.struct(
        {
            "enabled": t.boolean(),
            "includePatterns": t.array(t.string()).optional(),
            "csvOptions": t.proxy(
                renames["GoogleCloudDataplexV1ZoneDiscoverySpecCsvOptionsIn"]
            ).optional(),
            "excludePatterns": t.array(t.string()).optional(),
            "schedule": t.string().optional(),
            "jsonOptions": t.proxy(
                renames["GoogleCloudDataplexV1ZoneDiscoverySpecJsonOptionsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ZoneDiscoverySpecIn"])
    types["GoogleCloudDataplexV1ZoneDiscoverySpecOut"] = t.struct(
        {
            "enabled": t.boolean(),
            "includePatterns": t.array(t.string()).optional(),
            "csvOptions": t.proxy(
                renames["GoogleCloudDataplexV1ZoneDiscoverySpecCsvOptionsOut"]
            ).optional(),
            "excludePatterns": t.array(t.string()).optional(),
            "schedule": t.string().optional(),
            "jsonOptions": t.proxy(
                renames["GoogleCloudDataplexV1ZoneDiscoverySpecJsonOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ZoneDiscoverySpecOut"])
    types["GoogleCloudDataplexV1OperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1OperationMetadataIn"])
    types["GoogleCloudDataplexV1OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "statusMessage": t.string().optional(),
            "apiVersion": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1OperationMetadataOut"])
    types["GoogleCloudDataplexV1DataAttributeBindingIn"] = t.struct(
        {
            "description": t.string().optional(),
            "resource": t.string().optional(),
            "displayName": t.string().optional(),
            "etag": t.string().optional(),
            "paths": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataAttributeBindingPathIn"])
            ).optional(),
            "attributes": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataAttributeBindingIn"])
    types["GoogleCloudDataplexV1DataAttributeBindingOut"] = t.struct(
        {
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "resource": t.string().optional(),
            "displayName": t.string().optional(),
            "etag": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "paths": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataAttributeBindingPathOut"])
            ).optional(),
            "attributes": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataAttributeBindingOut"])
    types["GoogleCloudDataplexV1DataQualityRuleUniquenessExpectationIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleUniquenessExpectationIn"])
    types["GoogleCloudDataplexV1DataQualityRuleUniquenessExpectationOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleUniquenessExpectationOut"])
    types["GoogleCloudDataplexV1DataQualityRuleRegexExpectationIn"] = t.struct(
        {"regex": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleRegexExpectationIn"])
    types["GoogleCloudDataplexV1DataQualityRuleRegexExpectationOut"] = t.struct(
        {
            "regex": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleRegexExpectationOut"])
    types["GoogleCloudDataplexV1DiscoveryEventEntityDetailsIn"] = t.struct(
        {"entity": t.string().optional(), "type": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1DiscoveryEventEntityDetailsIn"])
    types["GoogleCloudDataplexV1DiscoveryEventEntityDetailsOut"] = t.struct(
        {
            "entity": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DiscoveryEventEntityDetailsOut"])
    types["GoogleCloudDataplexV1EntityIn"] = t.struct(
        {
            "schema": t.proxy(renames["GoogleCloudDataplexV1SchemaIn"]),
            "type": t.string(),
            "format": t.proxy(renames["GoogleCloudDataplexV1StorageFormatIn"]),
            "dataPath": t.string(),
            "description": t.string().optional(),
            "asset": t.string(),
            "system": t.string(),
            "dataPathPattern": t.string().optional(),
            "id": t.string(),
            "displayName": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1EntityIn"])
    types["GoogleCloudDataplexV1EntityOut"] = t.struct(
        {
            "schema": t.proxy(renames["GoogleCloudDataplexV1SchemaOut"]),
            "compatibility": t.proxy(
                renames["GoogleCloudDataplexV1EntityCompatibilityStatusOut"]
            ).optional(),
            "name": t.string().optional(),
            "type": t.string(),
            "format": t.proxy(renames["GoogleCloudDataplexV1StorageFormatOut"]),
            "dataPath": t.string(),
            "description": t.string().optional(),
            "asset": t.string(),
            "catalogEntry": t.string().optional(),
            "system": t.string(),
            "createTime": t.string().optional(),
            "access": t.proxy(
                renames["GoogleCloudDataplexV1StorageAccessOut"]
            ).optional(),
            "dataPathPattern": t.string().optional(),
            "uid": t.string().optional(),
            "id": t.string(),
            "displayName": t.string().optional(),
            "etag": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1EntityOut"])
    types["GoogleCloudDataplexV1AssetDiscoveryStatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "updateTime": t.string().optional(),
            "lastRunDuration": t.string().optional(),
            "state": t.string().optional(),
            "lastRunTime": t.string().optional(),
            "stats": t.proxy(
                renames["GoogleCloudDataplexV1AssetDiscoveryStatusStatsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetDiscoveryStatusIn"])
    types["GoogleCloudDataplexV1AssetDiscoveryStatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "updateTime": t.string().optional(),
            "lastRunDuration": t.string().optional(),
            "state": t.string().optional(),
            "lastRunTime": t.string().optional(),
            "stats": t.proxy(
                renames["GoogleCloudDataplexV1AssetDiscoveryStatusStatsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetDiscoveryStatusOut"])
    types["GoogleCloudDataplexV1DataQualityRuleSetExpectationIn"] = t.struct(
        {"values": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleSetExpectationIn"])
    types["GoogleCloudDataplexV1DataQualityRuleSetExpectationOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleSetExpectationOut"])
    types["GoogleCloudDataplexV1EnvironmentIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "infrastructureSpec": t.proxy(
                renames["GoogleCloudDataplexV1EnvironmentInfrastructureSpecIn"]
            ),
            "sessionSpec": t.proxy(
                renames["GoogleCloudDataplexV1EnvironmentSessionSpecIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1EnvironmentIn"])
    types["GoogleCloudDataplexV1EnvironmentOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "sessionStatus": t.proxy(
                renames["GoogleCloudDataplexV1EnvironmentSessionStatusOut"]
            ).optional(),
            "description": t.string().optional(),
            "endpoints": t.proxy(
                renames["GoogleCloudDataplexV1EnvironmentEndpointsOut"]
            ).optional(),
            "infrastructureSpec": t.proxy(
                renames["GoogleCloudDataplexV1EnvironmentInfrastructureSpecOut"]
            ),
            "sessionSpec": t.proxy(
                renames["GoogleCloudDataplexV1EnvironmentSessionSpecOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "uid": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1EnvironmentOut"])
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
    types["GoogleCloudDataplexV1ZoneResourceSpecIn"] = t.struct(
        {"locationType": t.string()}
    ).named(renames["GoogleCloudDataplexV1ZoneResourceSpecIn"])
    types["GoogleCloudDataplexV1ZoneResourceSpecOut"] = t.struct(
        {
            "locationType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ZoneResourceSpecOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIn"] = t.struct(
        {
            "topNValues": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoTopNValueIn"
                    ]
                )
            ).optional(),
            "nullRatio": t.number().optional(),
            "doubleProfile": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoDoubleFieldInfoIn"
                ]
            ).optional(),
            "integerProfile": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIntegerFieldInfoIn"
                ]
            ).optional(),
            "distinctRatio": t.number().optional(),
            "stringProfile": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoStringFieldInfoIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIn"])
    types[
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoOut"
    ] = t.struct(
        {
            "topNValues": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoTopNValueOut"
                    ]
                )
            ).optional(),
            "nullRatio": t.number().optional(),
            "doubleProfile": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoDoubleFieldInfoOut"
                ]
            ).optional(),
            "integerProfile": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIntegerFieldInfoOut"
                ]
            ).optional(),
            "distinctRatio": t.number().optional(),
            "stringProfile": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoStringFieldInfoOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoOut"]
    )
    types["GoogleCloudDataplexV1LakeIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "metastore": t.proxy(
                renames["GoogleCloudDataplexV1LakeMetastoreIn"]
            ).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1LakeIn"])
    types["GoogleCloudDataplexV1LakeOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "assetStatus": t.proxy(
                renames["GoogleCloudDataplexV1AssetStatusOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "uid": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "metastore": t.proxy(
                renames["GoogleCloudDataplexV1LakeMetastoreOut"]
            ).optional(),
            "metastoreStatus": t.proxy(
                renames["GoogleCloudDataplexV1LakeMetastoreStatusOut"]
            ).optional(),
            "state": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1LakeOut"])
    types["GoogleCloudDataplexV1DiscoveryEventConfigDetailsIn"] = t.struct(
        {"parameters": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudDataplexV1DiscoveryEventConfigDetailsIn"])
    types["GoogleCloudDataplexV1DiscoveryEventConfigDetailsOut"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DiscoveryEventConfigDetailsOut"])
    types["GoogleCloudDataplexV1DataScanEventDataQualityResultIn"] = t.struct(
        {
            "rowCount": t.string().optional(),
            "passed": t.boolean().optional(),
            "dimensionPassed": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanEventDataQualityResultIn"])
    types["GoogleCloudDataplexV1DataScanEventDataQualityResultOut"] = t.struct(
        {
            "rowCount": t.string().optional(),
            "passed": t.boolean().optional(),
            "dimensionPassed": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanEventDataQualityResultOut"])
    types["GoogleCloudDataplexV1PartitionIn"] = t.struct(
        {
            "values": t.array(t.string()),
            "etag": t.string().optional(),
            "location": t.string(),
        }
    ).named(renames["GoogleCloudDataplexV1PartitionIn"])
    types["GoogleCloudDataplexV1PartitionOut"] = t.struct(
        {
            "values": t.array(t.string()),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "location": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1PartitionOut"])
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
    types["GoogleCloudDataplexV1TaskExecutionSpecIn"] = t.struct(
        {
            "serviceAccount": t.string(),
            "args": t.struct({"_": t.string().optional()}).optional(),
            "project": t.string().optional(),
            "maxJobExecutionLifetime": t.string().optional(),
            "kmsKey": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TaskExecutionSpecIn"])
    types["GoogleCloudDataplexV1TaskExecutionSpecOut"] = t.struct(
        {
            "serviceAccount": t.string(),
            "args": t.struct({"_": t.string().optional()}).optional(),
            "project": t.string().optional(),
            "maxJobExecutionLifetime": t.string().optional(),
            "kmsKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TaskExecutionSpecOut"])
    types["GoogleCloudDataplexV1SessionEventQueryDetailIn"] = t.struct(
        {
            "engine": t.string().optional(),
            "resultSizeBytes": t.string().optional(),
            "duration": t.string().optional(),
            "dataProcessedBytes": t.string().optional(),
            "queryId": t.string().optional(),
            "queryText": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1SessionEventQueryDetailIn"])
    types["GoogleCloudDataplexV1SessionEventQueryDetailOut"] = t.struct(
        {
            "engine": t.string().optional(),
            "resultSizeBytes": t.string().optional(),
            "duration": t.string().optional(),
            "dataProcessedBytes": t.string().optional(),
            "queryId": t.string().optional(),
            "queryText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1SessionEventQueryDetailOut"])
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
    types["GoogleCloudDataplexV1DataScanEventIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "trigger": t.string().optional(),
            "jobId": t.string().optional(),
            "dataSource": t.string().optional(),
            "dataProfileConfigs": t.proxy(
                renames["GoogleCloudDataplexV1DataScanEventDataProfileAppliedConfigsIn"]
            ).optional(),
            "dataQuality": t.proxy(
                renames["GoogleCloudDataplexV1DataScanEventDataQualityResultIn"]
            ).optional(),
            "dataProfile": t.proxy(
                renames["GoogleCloudDataplexV1DataScanEventDataProfileResultIn"]
            ).optional(),
            "scope": t.string().optional(),
            "specVersion": t.string().optional(),
            "postScanActionsResult": t.proxy(
                renames["GoogleCloudDataplexV1DataScanEventPostScanActionsResultIn"]
            ).optional(),
            "message": t.string().optional(),
            "dataQualityConfigs": t.proxy(
                renames["GoogleCloudDataplexV1DataScanEventDataQualityAppliedConfigsIn"]
            ).optional(),
            "startTime": t.string().optional(),
            "state": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanEventIn"])
    types["GoogleCloudDataplexV1DataScanEventOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "trigger": t.string().optional(),
            "jobId": t.string().optional(),
            "dataSource": t.string().optional(),
            "dataProfileConfigs": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataScanEventDataProfileAppliedConfigsOut"
                ]
            ).optional(),
            "dataQuality": t.proxy(
                renames["GoogleCloudDataplexV1DataScanEventDataQualityResultOut"]
            ).optional(),
            "dataProfile": t.proxy(
                renames["GoogleCloudDataplexV1DataScanEventDataProfileResultOut"]
            ).optional(),
            "scope": t.string().optional(),
            "specVersion": t.string().optional(),
            "postScanActionsResult": t.proxy(
                renames["GoogleCloudDataplexV1DataScanEventPostScanActionsResultOut"]
            ).optional(),
            "message": t.string().optional(),
            "dataQualityConfigs": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataScanEventDataQualityAppliedConfigsOut"
                ]
            ).optional(),
            "startTime": t.string().optional(),
            "state": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanEventOut"])
    types["GoogleCloudDataplexV1TriggerOnDemandIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1TriggerOnDemandIn"])
    types["GoogleCloudDataplexV1TriggerOnDemandOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDataplexV1TriggerOnDemandOut"])
    types["GoogleCloudDataplexV1ActionFailedSecurityPolicyApplyIn"] = t.struct(
        {"asset": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1ActionFailedSecurityPolicyApplyIn"])
    types["GoogleCloudDataplexV1ActionFailedSecurityPolicyApplyOut"] = t.struct(
        {
            "asset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ActionFailedSecurityPolicyApplyOut"])
    types["GoogleCloudDataplexV1DataScanJobIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1DataScanJobIn"])
    types["GoogleCloudDataplexV1DataScanJobOut"] = t.struct(
        {
            "dataQualityResult": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityResultOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "dataProfileSpec": t.proxy(
                renames["GoogleCloudDataplexV1DataProfileSpecOut"]
            ).optional(),
            "uid": t.string().optional(),
            "dataProfileResult": t.proxy(
                renames["GoogleCloudDataplexV1DataProfileResultOut"]
            ).optional(),
            "type": t.string().optional(),
            "dataQualitySpec": t.proxy(
                renames["GoogleCloudDataplexV1DataQualitySpecOut"]
            ).optional(),
            "endTime": t.string().optional(),
            "message": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanJobOut"])
    types["GoogleIamV1SetIamPolicyRequestIn"] = t.struct(
        {
            "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
            "updateMask": t.string().optional(),
        }
    ).named(renames["GoogleIamV1SetIamPolicyRequestIn"])
    types["GoogleIamV1SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["GoogleIamV1PolicyOut"]).optional(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1SetIamPolicyRequestOut"])
    types["GoogleCloudDataplexV1ZoneIn"] = t.struct(
        {
            "discoverySpec": t.proxy(
                renames["GoogleCloudDataplexV1ZoneDiscoverySpecIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "resourceSpec": t.proxy(renames["GoogleCloudDataplexV1ZoneResourceSpecIn"]),
            "type": t.string(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ZoneIn"])
    types["GoogleCloudDataplexV1ZoneOut"] = t.struct(
        {
            "discoverySpec": t.proxy(
                renames["GoogleCloudDataplexV1ZoneDiscoverySpecOut"]
            ).optional(),
            "assetStatus": t.proxy(
                renames["GoogleCloudDataplexV1AssetStatusOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "resourceSpec": t.proxy(
                renames["GoogleCloudDataplexV1ZoneResourceSpecOut"]
            ),
            "createTime": t.string().optional(),
            "type": t.string(),
            "updateTime": t.string().optional(),
            "uid": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ZoneOut"])
    types["GoogleCloudDataplexV1TriggerIn"] = t.struct(
        {
            "schedule": t.proxy(
                renames["GoogleCloudDataplexV1TriggerScheduleIn"]
            ).optional(),
            "onDemand": t.proxy(
                renames["GoogleCloudDataplexV1TriggerOnDemandIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TriggerIn"])
    types["GoogleCloudDataplexV1TriggerOut"] = t.struct(
        {
            "schedule": t.proxy(
                renames["GoogleCloudDataplexV1TriggerScheduleOut"]
            ).optional(),
            "onDemand": t.proxy(
                renames["GoogleCloudDataplexV1TriggerOnDemandOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TriggerOut"])
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
    types["GoogleCloudDataplexV1ActionUnauthorizedResourceIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1ActionUnauthorizedResourceIn"])
    types["GoogleCloudDataplexV1ActionUnauthorizedResourceOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDataplexV1ActionUnauthorizedResourceOut"])
    types["GoogleCloudDataplexV1ListTasksResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachableLocations": t.array(t.string()).optional(),
            "tasks": t.array(
                t.proxy(renames["GoogleCloudDataplexV1TaskIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListTasksResponseIn"])
    types["GoogleCloudDataplexV1ListTasksResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachableLocations": t.array(t.string()).optional(),
            "tasks": t.array(
                t.proxy(renames["GoogleCloudDataplexV1TaskOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListTasksResponseOut"])
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
    types["GoogleCloudDataplexV1DataScanEventDataProfileResultIn"] = t.struct(
        {"rowCount": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1DataScanEventDataProfileResultIn"])
    types["GoogleCloudDataplexV1DataScanEventDataProfileResultOut"] = t.struct(
        {
            "rowCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanEventDataProfileResultOut"])
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
    types[
        "GoogleCloudDataplexV1TaskInfrastructureSpecContainerImageRuntimeIn"
    ] = t.struct(
        {
            "javaJars": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "pythonPackages": t.array(t.string()).optional(),
            "image": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudDataplexV1TaskInfrastructureSpecContainerImageRuntimeIn"]
    )
    types[
        "GoogleCloudDataplexV1TaskInfrastructureSpecContainerImageRuntimeOut"
    ] = t.struct(
        {
            "javaJars": t.array(t.string()).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "pythonPackages": t.array(t.string()).optional(),
            "image": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDataplexV1TaskInfrastructureSpecContainerImageRuntimeOut"]
    )
    types["GoogleCloudDataplexV1DataProfileSpecSelectedFieldsIn"] = t.struct(
        {"fieldNames": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudDataplexV1DataProfileSpecSelectedFieldsIn"])
    types["GoogleCloudDataplexV1DataProfileSpecSelectedFieldsOut"] = t.struct(
        {
            "fieldNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataProfileSpecSelectedFieldsOut"])
    types["GoogleCloudDataplexV1ContentSqlScriptIn"] = t.struct(
        {"engine": t.string()}
    ).named(renames["GoogleCloudDataplexV1ContentSqlScriptIn"])
    types["GoogleCloudDataplexV1ContentSqlScriptOut"] = t.struct(
        {"engine": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDataplexV1ContentSqlScriptOut"])
    types["GoogleCloudDataplexV1StorageAccessIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1StorageAccessIn"])
    types["GoogleCloudDataplexV1StorageAccessOut"] = t.struct(
        {
            "read": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1StorageAccessOut"])
    types[
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIntegerFieldInfoIn"
    ] = t.struct(
        {
            "quartiles": t.array(t.string()).optional(),
            "max": t.string().optional(),
            "average": t.number().optional(),
            "standardDeviation": t.number().optional(),
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
            "quartiles": t.array(t.string()).optional(),
            "max": t.string().optional(),
            "average": t.number().optional(),
            "standardDeviation": t.number().optional(),
            "min": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIntegerFieldInfoOut"
        ]
    )
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
    types["GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectationIn"] = t.struct(
        {
            "strictMaxEnabled": t.boolean().optional(),
            "maxValue": t.string().optional(),
            "minValue": t.string().optional(),
            "statistic": t.string().optional(),
            "strictMinEnabled": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectationIn"])
    types[
        "GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectationOut"
    ] = t.struct(
        {
            "strictMaxEnabled": t.boolean().optional(),
            "maxValue": t.string().optional(),
            "minValue": t.string().optional(),
            "statistic": t.string().optional(),
            "strictMinEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectationOut"]
    )
    types["GoogleCloudDataplexV1DataQualityRuleResultIn"] = t.struct(
        {
            "failingRowsQuery": t.string().optional(),
            "passed": t.boolean().optional(),
            "evaluatedCount": t.string().optional(),
            "nullCount": t.string().optional(),
            "passedCount": t.string().optional(),
            "passRatio": t.number().optional(),
            "rule": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityRuleIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleResultIn"])
    types["GoogleCloudDataplexV1DataQualityRuleResultOut"] = t.struct(
        {
            "failingRowsQuery": t.string().optional(),
            "passed": t.boolean().optional(),
            "evaluatedCount": t.string().optional(),
            "nullCount": t.string().optional(),
            "passedCount": t.string().optional(),
            "passRatio": t.number().optional(),
            "rule": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityRuleOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleResultOut"])
    types["GoogleCloudDataplexV1JobIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudDataplexV1JobIn"]
    )
    types["GoogleCloudDataplexV1JobOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "name": t.string().optional(),
            "endTime": t.string().optional(),
            "uid": t.string().optional(),
            "executionSpec": t.proxy(
                renames["GoogleCloudDataplexV1TaskExecutionSpecOut"]
            ).optional(),
            "serviceJob": t.string().optional(),
            "state": t.string().optional(),
            "retryCount": t.integer().optional(),
            "message": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "service": t.string().optional(),
            "trigger": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1JobOut"])
    types["GoogleCloudDataplexV1RunTaskResponseIn"] = t.struct(
        {"job": t.proxy(renames["GoogleCloudDataplexV1JobIn"]).optional()}
    ).named(renames["GoogleCloudDataplexV1RunTaskResponseIn"])
    types["GoogleCloudDataplexV1RunTaskResponseOut"] = t.struct(
        {
            "job": t.proxy(renames["GoogleCloudDataplexV1JobOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1RunTaskResponseOut"])
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
    types["GoogleIamV1TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsResponseIn"])
    types["GoogleIamV1TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsResponseOut"])
    types["GoogleCloudDataplexV1ActionIncompatibleDataSchemaIn"] = t.struct(
        {
            "table": t.string().optional(),
            "newSchema": t.string().optional(),
            "existingSchema": t.string().optional(),
            "sampledDataLocations": t.array(t.string()).optional(),
            "schemaChange": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ActionIncompatibleDataSchemaIn"])
    types["GoogleCloudDataplexV1ActionIncompatibleDataSchemaOut"] = t.struct(
        {
            "table": t.string().optional(),
            "newSchema": t.string().optional(),
            "existingSchema": t.string().optional(),
            "sampledDataLocations": t.array(t.string()).optional(),
            "schemaChange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ActionIncompatibleDataSchemaOut"])
    types["GoogleCloudDataplexV1SchemaSchemaFieldIn"] = t.struct(
        {
            "mode": t.string(),
            "description": t.string().optional(),
            "fields": t.array(
                t.proxy(renames["GoogleCloudDataplexV1SchemaSchemaFieldIn"])
            ).optional(),
            "name": t.string(),
            "type": t.string(),
        }
    ).named(renames["GoogleCloudDataplexV1SchemaSchemaFieldIn"])
    types["GoogleCloudDataplexV1SchemaSchemaFieldOut"] = t.struct(
        {
            "mode": t.string(),
            "description": t.string().optional(),
            "fields": t.array(
                t.proxy(renames["GoogleCloudDataplexV1SchemaSchemaFieldOut"])
            ).optional(),
            "name": t.string(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1SchemaSchemaFieldOut"])
    types["GoogleCloudDataplexV1ListDataAttributesResponseIn"] = t.struct(
        {
            "unreachableLocations": t.array(t.string()).optional(),
            "dataAttributes": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataAttributeIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListDataAttributesResponseIn"])
    types["GoogleCloudDataplexV1ListDataAttributesResponseOut"] = t.struct(
        {
            "unreachableLocations": t.array(t.string()).optional(),
            "dataAttributes": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataAttributeOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListDataAttributesResponseOut"])
    types["GoogleIamV1BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingIn"])
    types["GoogleIamV1BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingOut"])
    types["GoogleCloudDataplexV1DataAttributeBindingPathIn"] = t.struct(
        {"name": t.string(), "attributes": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudDataplexV1DataAttributeBindingPathIn"])
    types["GoogleCloudDataplexV1DataAttributeBindingPathOut"] = t.struct(
        {
            "name": t.string(),
            "attributes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataAttributeBindingPathOut"])
    types["GoogleCloudDataplexV1TaskIn"] = t.struct(
        {
            "executionSpec": t.proxy(
                renames["GoogleCloudDataplexV1TaskExecutionSpecIn"]
            ),
            "displayName": t.string().optional(),
            "triggerSpec": t.proxy(renames["GoogleCloudDataplexV1TaskTriggerSpecIn"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "notebook": t.proxy(
                renames["GoogleCloudDataplexV1TaskNotebookTaskConfigIn"]
            ).optional(),
            "spark": t.proxy(
                renames["GoogleCloudDataplexV1TaskSparkTaskConfigIn"]
            ).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TaskIn"])
    types["GoogleCloudDataplexV1TaskOut"] = t.struct(
        {
            "executionSpec": t.proxy(
                renames["GoogleCloudDataplexV1TaskExecutionSpecOut"]
            ),
            "displayName": t.string().optional(),
            "triggerSpec": t.proxy(renames["GoogleCloudDataplexV1TaskTriggerSpecOut"]),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "notebook": t.proxy(
                renames["GoogleCloudDataplexV1TaskNotebookTaskConfigOut"]
            ).optional(),
            "executionStatus": t.proxy(
                renames["GoogleCloudDataplexV1TaskExecutionStatusOut"]
            ).optional(),
            "name": t.string().optional(),
            "uid": t.string().optional(),
            "updateTime": t.string().optional(),
            "spark": t.proxy(
                renames["GoogleCloudDataplexV1TaskSparkTaskConfigOut"]
            ).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TaskOut"])
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
    types["GoogleCloudDataplexV1CancelJobRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1CancelJobRequestIn"])
    types["GoogleCloudDataplexV1CancelJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDataplexV1CancelJobRequestOut"])
    types["GoogleCloudDataplexV1RunTaskRequestIn"] = t.struct(
        {
            "args": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1RunTaskRequestIn"])
    types["GoogleCloudDataplexV1RunTaskRequestOut"] = t.struct(
        {
            "args": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1RunTaskRequestOut"])
    types["GoogleCloudDataplexV1DataScanExecutionStatusIn"] = t.struct(
        {
            "latestJobStartTime": t.string().optional(),
            "latestJobEndTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanExecutionStatusIn"])
    types["GoogleCloudDataplexV1DataScanExecutionStatusOut"] = t.struct(
        {
            "latestJobStartTime": t.string().optional(),
            "latestJobEndTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanExecutionStatusOut"])
    types[
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoStringFieldInfoIn"
    ] = t.struct(
        {
            "maxLength": t.string().optional(),
            "averageLength": t.number().optional(),
            "minLength": t.string().optional(),
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
            "maxLength": t.string().optional(),
            "averageLength": t.number().optional(),
            "minLength": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoStringFieldInfoOut"
        ]
    )
    types["GoogleCloudDataplexV1DataQualityRuleRowConditionExpectationIn"] = t.struct(
        {"sqlExpression": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleRowConditionExpectationIn"])
    types["GoogleCloudDataplexV1DataQualityRuleRowConditionExpectationOut"] = t.struct(
        {
            "sqlExpression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleRowConditionExpectationOut"])
    types["GoogleCloudDataplexV1AssetDiscoverySpecIn"] = t.struct(
        {
            "excludePatterns": t.array(t.string()).optional(),
            "includePatterns": t.array(t.string()).optional(),
            "schedule": t.string().optional(),
            "enabled": t.boolean().optional(),
            "jsonOptions": t.proxy(
                renames["GoogleCloudDataplexV1AssetDiscoverySpecJsonOptionsIn"]
            ).optional(),
            "csvOptions": t.proxy(
                renames["GoogleCloudDataplexV1AssetDiscoverySpecCsvOptionsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetDiscoverySpecIn"])
    types["GoogleCloudDataplexV1AssetDiscoverySpecOut"] = t.struct(
        {
            "excludePatterns": t.array(t.string()).optional(),
            "includePatterns": t.array(t.string()).optional(),
            "schedule": t.string().optional(),
            "enabled": t.boolean().optional(),
            "jsonOptions": t.proxy(
                renames["GoogleCloudDataplexV1AssetDiscoverySpecJsonOptionsOut"]
            ).optional(),
            "csvOptions": t.proxy(
                renames["GoogleCloudDataplexV1AssetDiscoverySpecCsvOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetDiscoverySpecOut"])
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
    types["GoogleIamV1PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigIn"])
            ).optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingIn"])).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["GoogleIamV1PolicyIn"])
    types["GoogleIamV1PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigOut"])
            ).optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingOut"])).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1PolicyOut"])
    types["GoogleCloudDataplexV1DataQualityRuleRangeExpectationIn"] = t.struct(
        {
            "maxValue": t.string().optional(),
            "minValue": t.string().optional(),
            "strictMinEnabled": t.boolean().optional(),
            "strictMaxEnabled": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleRangeExpectationIn"])
    types["GoogleCloudDataplexV1DataQualityRuleRangeExpectationOut"] = t.struct(
        {
            "maxValue": t.string().optional(),
            "minValue": t.string().optional(),
            "strictMinEnabled": t.boolean().optional(),
            "strictMaxEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleRangeExpectationOut"])
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
    types["GoogleCloudDataplexV1TaskTriggerSpecIn"] = t.struct(
        {
            "schedule": t.string().optional(),
            "disabled": t.boolean().optional(),
            "maxRetries": t.integer().optional(),
            "startTime": t.string().optional(),
            "type": t.string(),
        }
    ).named(renames["GoogleCloudDataplexV1TaskTriggerSpecIn"])
    types["GoogleCloudDataplexV1TaskTriggerSpecOut"] = t.struct(
        {
            "schedule": t.string().optional(),
            "disabled": t.boolean().optional(),
            "maxRetries": t.integer().optional(),
            "startTime": t.string().optional(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TaskTriggerSpecOut"])
    types["GoogleCloudDataplexV1AssetDiscoverySpecCsvOptionsIn"] = t.struct(
        {
            "disableTypeInference": t.boolean().optional(),
            "headerRows": t.integer().optional(),
            "delimiter": t.string().optional(),
            "encoding": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetDiscoverySpecCsvOptionsIn"])
    types["GoogleCloudDataplexV1AssetDiscoverySpecCsvOptionsOut"] = t.struct(
        {
            "disableTypeInference": t.boolean().optional(),
            "headerRows": t.integer().optional(),
            "delimiter": t.string().optional(),
            "encoding": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1AssetDiscoverySpecCsvOptionsOut"])
    types["GoogleCloudDataplexV1ListDataAttributeBindingsResponseIn"] = t.struct(
        {
            "dataAttributeBindings": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataAttributeBindingIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachableLocations": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListDataAttributeBindingsResponseIn"])
    types["GoogleCloudDataplexV1ListDataAttributeBindingsResponseOut"] = t.struct(
        {
            "dataAttributeBindings": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataAttributeBindingOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachableLocations": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListDataAttributeBindingsResponseOut"])
    types["GoogleCloudDataplexV1ActionMissingDataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1ActionMissingDataIn"])
    types["GoogleCloudDataplexV1ActionMissingDataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDataplexV1ActionMissingDataOut"])
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
    types["GoogleIamV1TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsRequestIn"])
    types["GoogleIamV1TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsRequestOut"])
    types["GoogleTypeExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["GoogleTypeExprIn"])
    types["GoogleTypeExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeExprOut"])
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
    types["GoogleCloudDataplexV1StorageFormatJsonOptionsIn"] = t.struct(
        {"encoding": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1StorageFormatJsonOptionsIn"])
    types["GoogleCloudDataplexV1StorageFormatJsonOptionsOut"] = t.struct(
        {
            "encoding": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1StorageFormatJsonOptionsOut"])
    types["GoogleCloudDataplexV1ListSessionsResponseIn"] = t.struct(
        {
            "sessions": t.array(
                t.proxy(renames["GoogleCloudDataplexV1SessionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListSessionsResponseIn"])
    types["GoogleCloudDataplexV1ListSessionsResponseOut"] = t.struct(
        {
            "sessions": t.array(
                t.proxy(renames["GoogleCloudDataplexV1SessionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListSessionsResponseOut"])
    types["GoogleCloudDataplexV1DataScanEventDataProfileAppliedConfigsIn"] = t.struct(
        {
            "rowFilterApplied": t.boolean().optional(),
            "columnFilterApplied": t.boolean().optional(),
            "samplingPercent": t.number().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanEventDataProfileAppliedConfigsIn"])
    types["GoogleCloudDataplexV1DataScanEventDataProfileAppliedConfigsOut"] = t.struct(
        {
            "rowFilterApplied": t.boolean().optional(),
            "columnFilterApplied": t.boolean().optional(),
            "samplingPercent": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanEventDataProfileAppliedConfigsOut"])
    types["GoogleCloudDataplexV1SchemaIn"] = t.struct(
        {
            "userManaged": t.boolean(),
            "partitionFields": t.array(
                t.proxy(renames["GoogleCloudDataplexV1SchemaPartitionFieldIn"])
            ).optional(),
            "fields": t.array(
                t.proxy(renames["GoogleCloudDataplexV1SchemaSchemaFieldIn"])
            ).optional(),
            "partitionStyle": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1SchemaIn"])
    types["GoogleCloudDataplexV1SchemaOut"] = t.struct(
        {
            "userManaged": t.boolean(),
            "partitionFields": t.array(
                t.proxy(renames["GoogleCloudDataplexV1SchemaPartitionFieldOut"])
            ).optional(),
            "fields": t.array(
                t.proxy(renames["GoogleCloudDataplexV1SchemaSchemaFieldOut"])
            ).optional(),
            "partitionStyle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1SchemaOut"])
    types["GoogleCloudDataplexV1ScannedDataIncrementalFieldIn"] = t.struct(
        {
            "field": t.string().optional(),
            "start": t.string().optional(),
            "end": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ScannedDataIncrementalFieldIn"])
    types["GoogleCloudDataplexV1ScannedDataIncrementalFieldOut"] = t.struct(
        {
            "field": t.string().optional(),
            "start": t.string().optional(),
            "end": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ScannedDataIncrementalFieldOut"])
    types["GoogleCloudDataplexV1DataScanIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "executionSpec": t.proxy(
                renames["GoogleCloudDataplexV1DataScanExecutionSpecIn"]
            ).optional(),
            "data": t.proxy(renames["GoogleCloudDataplexV1DataSourceIn"]),
            "dataQualitySpec": t.proxy(
                renames["GoogleCloudDataplexV1DataQualitySpecIn"]
            ).optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "dataProfileSpec": t.proxy(
                renames["GoogleCloudDataplexV1DataProfileSpecIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanIn"])
    types["GoogleCloudDataplexV1DataScanOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "executionSpec": t.proxy(
                renames["GoogleCloudDataplexV1DataScanExecutionSpecOut"]
            ).optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "data": t.proxy(renames["GoogleCloudDataplexV1DataSourceOut"]),
            "dataQualitySpec": t.proxy(
                renames["GoogleCloudDataplexV1DataQualitySpecOut"]
            ).optional(),
            "type": t.string().optional(),
            "dataProfileResult": t.proxy(
                renames["GoogleCloudDataplexV1DataProfileResultOut"]
            ).optional(),
            "description": t.string().optional(),
            "executionStatus": t.proxy(
                renames["GoogleCloudDataplexV1DataScanExecutionStatusOut"]
            ).optional(),
            "uid": t.string().optional(),
            "state": t.string().optional(),
            "displayName": t.string().optional(),
            "dataQualityResult": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityResultOut"]
            ).optional(),
            "dataProfileSpec": t.proxy(
                renames["GoogleCloudDataplexV1DataProfileSpecOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataScanOut"])
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
    types["GoogleCloudLocationLocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudLocationLocationIn"])
    types["GoogleCloudLocationLocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudLocationLocationOut"])
    types["GoogleCloudDataplexV1DataQualitySpecIn"] = t.struct(
        {
            "rules": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataQualityRuleIn"])
            ).optional(),
            "samplingPercent": t.number().optional(),
            "rowFilter": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualitySpecIn"])
    types["GoogleCloudDataplexV1DataQualitySpecOut"] = t.struct(
        {
            "rules": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataQualityRuleOut"])
            ).optional(),
            "samplingPercent": t.number().optional(),
            "rowFilter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualitySpecOut"])
    types["GoogleCloudDataplexV1StorageFormatCsvOptionsIn"] = t.struct(
        {
            "quote": t.string().optional(),
            "delimiter": t.string().optional(),
            "headerRows": t.integer().optional(),
            "encoding": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1StorageFormatCsvOptionsIn"])
    types["GoogleCloudDataplexV1StorageFormatCsvOptionsOut"] = t.struct(
        {
            "quote": t.string().optional(),
            "delimiter": t.string().optional(),
            "headerRows": t.integer().optional(),
            "encoding": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1StorageFormatCsvOptionsOut"])
    types[
        "GoogleCloudDataplexV1EnvironmentInfrastructureSpecComputeResourcesIn"
    ] = t.struct(
        {
            "nodeCount": t.integer().optional(),
            "diskSizeGb": t.integer().optional(),
            "maxNodeCount": t.integer().optional(),
        }
    ).named(
        renames["GoogleCloudDataplexV1EnvironmentInfrastructureSpecComputeResourcesIn"]
    )
    types[
        "GoogleCloudDataplexV1EnvironmentInfrastructureSpecComputeResourcesOut"
    ] = t.struct(
        {
            "nodeCount": t.integer().optional(),
            "diskSizeGb": t.integer().optional(),
            "maxNodeCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDataplexV1EnvironmentInfrastructureSpecComputeResourcesOut"]
    )
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
    types["GoogleCloudDataplexV1DataQualityResultIn"] = t.struct(
        {
            "scannedData": t.proxy(
                renames["GoogleCloudDataplexV1ScannedDataIn"]
            ).optional(),
            "rules": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataQualityRuleResultIn"])
            ).optional(),
            "rowCount": t.string().optional(),
            "dimensions": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataQualityDimensionResultIn"])
            ).optional(),
            "passed": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualityResultIn"])
    types["GoogleCloudDataplexV1DataQualityResultOut"] = t.struct(
        {
            "scannedData": t.proxy(
                renames["GoogleCloudDataplexV1ScannedDataOut"]
            ).optional(),
            "rules": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataQualityRuleResultOut"])
            ).optional(),
            "rowCount": t.string().optional(),
            "dimensions": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataQualityDimensionResultOut"])
            ).optional(),
            "passed": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualityResultOut"])
    types["GoogleCloudDataplexV1ActionInvalidDataPartitionIn"] = t.struct(
        {"expectedStructure": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1ActionInvalidDataPartitionIn"])
    types["GoogleCloudDataplexV1ActionInvalidDataPartitionOut"] = t.struct(
        {
            "expectedStructure": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ActionInvalidDataPartitionOut"])
    types["GoogleCloudDataplexV1TriggerScheduleIn"] = t.struct(
        {"cron": t.string()}
    ).named(renames["GoogleCloudDataplexV1TriggerScheduleIn"])
    types["GoogleCloudDataplexV1TriggerScheduleOut"] = t.struct(
        {"cron": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDataplexV1TriggerScheduleOut"])
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
    types["GoogleCloudDataplexV1TaskInfrastructureSpecIn"] = t.struct(
        {
            "vpcNetwork": t.proxy(
                renames["GoogleCloudDataplexV1TaskInfrastructureSpecVpcNetworkIn"]
            ).optional(),
            "containerImage": t.proxy(
                renames[
                    "GoogleCloudDataplexV1TaskInfrastructureSpecContainerImageRuntimeIn"
                ]
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
            "vpcNetwork": t.proxy(
                renames["GoogleCloudDataplexV1TaskInfrastructureSpecVpcNetworkOut"]
            ).optional(),
            "containerImage": t.proxy(
                renames[
                    "GoogleCloudDataplexV1TaskInfrastructureSpecContainerImageRuntimeOut"
                ]
            ).optional(),
            "batch": t.proxy(
                renames[
                    "GoogleCloudDataplexV1TaskInfrastructureSpecBatchComputeResourcesOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TaskInfrastructureSpecOut"])
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
    types[
        "GoogleCloudDataplexV1DataScanEventPostScanActionsResultBigQueryExportResultIn"
    ] = t.struct(
        {"message": t.string().optional(), "state": t.string().optional()}
    ).named(
        renames[
            "GoogleCloudDataplexV1DataScanEventPostScanActionsResultBigQueryExportResultIn"
        ]
    )
    types[
        "GoogleCloudDataplexV1DataScanEventPostScanActionsResultBigQueryExportResultOut"
    ] = t.struct(
        {
            "message": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDataplexV1DataScanEventPostScanActionsResultBigQueryExportResultOut"
        ]
    )
    types[
        "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoDoubleFieldInfoIn"
    ] = t.struct(
        {
            "max": t.number().optional(),
            "min": t.number().optional(),
            "average": t.number().optional(),
            "standardDeviation": t.number().optional(),
            "quartiles": t.array(t.number()).optional(),
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
            "max": t.number().optional(),
            "min": t.number().optional(),
            "average": t.number().optional(),
            "standardDeviation": t.number().optional(),
            "quartiles": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoDoubleFieldInfoOut"
        ]
    )
    types["GoogleCloudDataplexV1RunDataScanResponseIn"] = t.struct(
        {"job": t.proxy(renames["GoogleCloudDataplexV1DataScanJobIn"]).optional()}
    ).named(renames["GoogleCloudDataplexV1RunDataScanResponseIn"])
    types["GoogleCloudDataplexV1RunDataScanResponseOut"] = t.struct(
        {
            "job": t.proxy(renames["GoogleCloudDataplexV1DataScanJobOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1RunDataScanResponseOut"])
    types["GoogleCloudDataplexV1DataProfileResultProfileFieldIn"] = t.struct(
        {
            "mode": t.string().optional(),
            "type": t.string().optional(),
            "profile": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIn"
                ]
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataProfileResultProfileFieldIn"])
    types["GoogleCloudDataplexV1DataProfileResultProfileFieldOut"] = t.struct(
        {
            "mode": t.string().optional(),
            "type": t.string().optional(),
            "profile": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoOut"
                ]
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataProfileResultProfileFieldOut"])
    types["GoogleCloudDataplexV1DataQualityDimensionResultIn"] = t.struct(
        {"passed": t.boolean().optional()}
    ).named(renames["GoogleCloudDataplexV1DataQualityDimensionResultIn"])
    types["GoogleCloudDataplexV1DataQualityDimensionResultOut"] = t.struct(
        {
            "passed": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualityDimensionResultOut"])
    types["GoogleCloudDataplexV1TaskInfrastructureSpecVpcNetworkIn"] = t.struct(
        {
            "subNetwork": t.string().optional(),
            "network": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TaskInfrastructureSpecVpcNetworkIn"])
    types["GoogleCloudDataplexV1TaskInfrastructureSpecVpcNetworkOut"] = t.struct(
        {
            "subNetwork": t.string().optional(),
            "network": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1TaskInfrastructureSpecVpcNetworkOut"])
    types["GoogleCloudDataplexV1DataQualityRuleNonNullExpectationIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleNonNullExpectationIn"])
    types["GoogleCloudDataplexV1DataQualityRuleNonNullExpectationOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleNonNullExpectationOut"])
    types["GoogleCloudDataplexV1ContentIn"] = t.struct(
        {
            "notebook": t.proxy(
                renames["GoogleCloudDataplexV1ContentNotebookIn"]
            ).optional(),
            "path": t.string(),
            "description": t.string().optional(),
            "sqlScript": t.proxy(
                renames["GoogleCloudDataplexV1ContentSqlScriptIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "dataText": t.string(),
        }
    ).named(renames["GoogleCloudDataplexV1ContentIn"])
    types["GoogleCloudDataplexV1ContentOut"] = t.struct(
        {
            "notebook": t.proxy(
                renames["GoogleCloudDataplexV1ContentNotebookOut"]
            ).optional(),
            "path": t.string(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "sqlScript": t.proxy(
                renames["GoogleCloudDataplexV1ContentSqlScriptOut"]
            ).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "dataText": t.string(),
            "uid": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ContentOut"])
    types["GoogleCloudDataplexV1ActionIn"] = t.struct(
        {
            "failedSecurityPolicyApply": t.proxy(
                renames["GoogleCloudDataplexV1ActionFailedSecurityPolicyApplyIn"]
            ).optional(),
            "missingData": t.proxy(
                renames["GoogleCloudDataplexV1ActionMissingDataIn"]
            ).optional(),
            "incompatibleDataSchema": t.proxy(
                renames["GoogleCloudDataplexV1ActionIncompatibleDataSchemaIn"]
            ).optional(),
            "detectTime": t.string().optional(),
            "issue": t.string().optional(),
            "unauthorizedResource": t.proxy(
                renames["GoogleCloudDataplexV1ActionUnauthorizedResourceIn"]
            ).optional(),
            "invalidDataOrganization": t.proxy(
                renames["GoogleCloudDataplexV1ActionInvalidDataOrganizationIn"]
            ).optional(),
            "invalidDataPartition": t.proxy(
                renames["GoogleCloudDataplexV1ActionInvalidDataPartitionIn"]
            ).optional(),
            "category": t.string().optional(),
            "invalidDataFormat": t.proxy(
                renames["GoogleCloudDataplexV1ActionInvalidDataFormatIn"]
            ).optional(),
            "dataLocations": t.array(t.string()).optional(),
            "missingResource": t.proxy(
                renames["GoogleCloudDataplexV1ActionMissingResourceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ActionIn"])
    types["GoogleCloudDataplexV1ActionOut"] = t.struct(
        {
            "failedSecurityPolicyApply": t.proxy(
                renames["GoogleCloudDataplexV1ActionFailedSecurityPolicyApplyOut"]
            ).optional(),
            "missingData": t.proxy(
                renames["GoogleCloudDataplexV1ActionMissingDataOut"]
            ).optional(),
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "incompatibleDataSchema": t.proxy(
                renames["GoogleCloudDataplexV1ActionIncompatibleDataSchemaOut"]
            ).optional(),
            "detectTime": t.string().optional(),
            "issue": t.string().optional(),
            "unauthorizedResource": t.proxy(
                renames["GoogleCloudDataplexV1ActionUnauthorizedResourceOut"]
            ).optional(),
            "invalidDataOrganization": t.proxy(
                renames["GoogleCloudDataplexV1ActionInvalidDataOrganizationOut"]
            ).optional(),
            "asset": t.string().optional(),
            "invalidDataPartition": t.proxy(
                renames["GoogleCloudDataplexV1ActionInvalidDataPartitionOut"]
            ).optional(),
            "category": t.string().optional(),
            "invalidDataFormat": t.proxy(
                renames["GoogleCloudDataplexV1ActionInvalidDataFormatOut"]
            ).optional(),
            "dataLocations": t.array(t.string()).optional(),
            "missingResource": t.proxy(
                renames["GoogleCloudDataplexV1ActionMissingResourceOut"]
            ).optional(),
            "lake": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ActionOut"])
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
    types["GoogleCloudDataplexV1SchemaPartitionFieldIn"] = t.struct(
        {"type": t.string(), "name": t.string()}
    ).named(renames["GoogleCloudDataplexV1SchemaPartitionFieldIn"])
    types["GoogleCloudDataplexV1SchemaPartitionFieldOut"] = t.struct(
        {
            "type": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1SchemaPartitionFieldOut"])
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
    types["GoogleCloudDataplexV1SessionEventIn"] = t.struct(
        {
            "query": t.proxy(
                renames["GoogleCloudDataplexV1SessionEventQueryDetailIn"]
            ).optional(),
            "eventSucceeded": t.boolean().optional(),
            "userId": t.string().optional(),
            "unassignedDuration": t.string().optional(),
            "fastStartupEnabled": t.boolean().optional(),
            "sessionId": t.string().optional(),
            "message": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleCloudDataplexV1SessionEventIn"])
    types["GoogleCloudDataplexV1SessionEventOut"] = t.struct(
        {
            "query": t.proxy(
                renames["GoogleCloudDataplexV1SessionEventQueryDetailOut"]
            ).optional(),
            "eventSucceeded": t.boolean().optional(),
            "userId": t.string().optional(),
            "unassignedDuration": t.string().optional(),
            "fastStartupEnabled": t.boolean().optional(),
            "sessionId": t.string().optional(),
            "message": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1SessionEventOut"])
    types["GoogleCloudDataplexV1StorageFormatIn"] = t.struct(
        {
            "compressionFormat": t.string().optional(),
            "iceberg": t.proxy(
                renames["GoogleCloudDataplexV1StorageFormatIcebergOptionsIn"]
            ).optional(),
            "mimeType": t.string(),
            "csv": t.proxy(
                renames["GoogleCloudDataplexV1StorageFormatCsvOptionsIn"]
            ).optional(),
            "json": t.proxy(
                renames["GoogleCloudDataplexV1StorageFormatJsonOptionsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1StorageFormatIn"])
    types["GoogleCloudDataplexV1StorageFormatOut"] = t.struct(
        {
            "format": t.string().optional(),
            "compressionFormat": t.string().optional(),
            "iceberg": t.proxy(
                renames["GoogleCloudDataplexV1StorageFormatIcebergOptionsOut"]
            ).optional(),
            "mimeType": t.string(),
            "csv": t.proxy(
                renames["GoogleCloudDataplexV1StorageFormatCsvOptionsOut"]
            ).optional(),
            "json": t.proxy(
                renames["GoogleCloudDataplexV1StorageFormatJsonOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1StorageFormatOut"])
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
    types["GoogleCloudDataplexV1ListDataTaxonomiesResponseIn"] = t.struct(
        {
            "dataTaxonomies": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataTaxonomyIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachableLocations": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListDataTaxonomiesResponseIn"])
    types["GoogleCloudDataplexV1ListDataTaxonomiesResponseOut"] = t.struct(
        {
            "dataTaxonomies": t.array(
                t.proxy(renames["GoogleCloudDataplexV1DataTaxonomyOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachableLocations": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ListDataTaxonomiesResponseOut"])
    types["GoogleCloudDataplexV1ResourceAccessSpecIn"] = t.struct(
        {
            "readers": t.array(t.string()).optional(),
            "owners": t.array(t.string()).optional(),
            "writers": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ResourceAccessSpecIn"])
    types["GoogleCloudDataplexV1ResourceAccessSpecOut"] = t.struct(
        {
            "readers": t.array(t.string()).optional(),
            "owners": t.array(t.string()).optional(),
            "writers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1ResourceAccessSpecOut"])
    types["GoogleCloudDataplexV1DataQualityRuleIn"] = t.struct(
        {
            "name": t.string().optional(),
            "statisticRangeExpectation": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectationIn"
                ]
            ).optional(),
            "tableConditionExpectation": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataQualityRuleTableConditionExpectationIn"
                ]
            ).optional(),
            "setExpectation": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityRuleSetExpectationIn"]
            ).optional(),
            "dimension": t.string(),
            "description": t.string().optional(),
            "ignoreNull": t.boolean().optional(),
            "nonNullExpectation": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityRuleNonNullExpectationIn"]
            ).optional(),
            "regexExpectation": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityRuleRegexExpectationIn"]
            ).optional(),
            "column": t.string().optional(),
            "rowConditionExpectation": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityRuleRowConditionExpectationIn"]
            ).optional(),
            "uniquenessExpectation": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityRuleUniquenessExpectationIn"]
            ).optional(),
            "threshold": t.number().optional(),
            "rangeExpectation": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityRuleRangeExpectationIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleIn"])
    types["GoogleCloudDataplexV1DataQualityRuleOut"] = t.struct(
        {
            "name": t.string().optional(),
            "statisticRangeExpectation": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectationOut"
                ]
            ).optional(),
            "tableConditionExpectation": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataQualityRuleTableConditionExpectationOut"
                ]
            ).optional(),
            "setExpectation": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityRuleSetExpectationOut"]
            ).optional(),
            "dimension": t.string(),
            "description": t.string().optional(),
            "ignoreNull": t.boolean().optional(),
            "nonNullExpectation": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityRuleNonNullExpectationOut"]
            ).optional(),
            "regexExpectation": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityRuleRegexExpectationOut"]
            ).optional(),
            "column": t.string().optional(),
            "rowConditionExpectation": t.proxy(
                renames[
                    "GoogleCloudDataplexV1DataQualityRuleRowConditionExpectationOut"
                ]
            ).optional(),
            "uniquenessExpectation": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityRuleUniquenessExpectationOut"]
            ).optional(),
            "threshold": t.number().optional(),
            "rangeExpectation": t.proxy(
                renames["GoogleCloudDataplexV1DataQualityRuleRangeExpectationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1DataQualityRuleOut"])
    types["GoogleCloudDataplexV1LakeMetastoreIn"] = t.struct(
        {"service": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1LakeMetastoreIn"])
    types["GoogleCloudDataplexV1LakeMetastoreOut"] = t.struct(
        {
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1LakeMetastoreOut"])
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
    types["GoogleCloudDataplexV1StorageFormatIcebergOptionsIn"] = t.struct(
        {"metadataLocation": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1StorageFormatIcebergOptionsIn"])
    types["GoogleCloudDataplexV1StorageFormatIcebergOptionsOut"] = t.struct(
        {
            "metadataLocation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1StorageFormatIcebergOptionsOut"])
    types["GoogleCloudDataplexV1EntityCompatibilityStatusCompatibilityIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDataplexV1EntityCompatibilityStatusCompatibilityIn"])
    types["GoogleCloudDataplexV1EntityCompatibilityStatusCompatibilityOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "compatible": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDataplexV1EntityCompatibilityStatusCompatibilityOut"])

    functions = {}
    functions["projectsLocationsGet"] = dataplex.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudLocationListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAspectTypesGetIamPolicy"] = dataplex.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
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
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
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
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesGetIamPolicy"] = dataplex.post(
        "v1/{parent}/lakes",
        t.struct(
            {
                "parent": t.string(),
                "lakeId": t.string(),
                "validateOnly": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "metastore": t.proxy(
                    renames["GoogleCloudDataplexV1LakeMetastoreIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesList"] = dataplex.post(
        "v1/{parent}/lakes",
        t.struct(
            {
                "parent": t.string(),
                "lakeId": t.string(),
                "validateOnly": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "metastore": t.proxy(
                    renames["GoogleCloudDataplexV1LakeMetastoreIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesSetIamPolicy"] = dataplex.post(
        "v1/{parent}/lakes",
        t.struct(
            {
                "parent": t.string(),
                "lakeId": t.string(),
                "validateOnly": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "metastore": t.proxy(
                    renames["GoogleCloudDataplexV1LakeMetastoreIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesGet"] = dataplex.post(
        "v1/{parent}/lakes",
        t.struct(
            {
                "parent": t.string(),
                "lakeId": t.string(),
                "validateOnly": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "metastore": t.proxy(
                    renames["GoogleCloudDataplexV1LakeMetastoreIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesTestIamPermissions"] = dataplex.post(
        "v1/{parent}/lakes",
        t.struct(
            {
                "parent": t.string(),
                "lakeId": t.string(),
                "validateOnly": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "metastore": t.proxy(
                    renames["GoogleCloudDataplexV1LakeMetastoreIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesPatch"] = dataplex.post(
        "v1/{parent}/lakes",
        t.struct(
            {
                "parent": t.string(),
                "lakeId": t.string(),
                "validateOnly": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "metastore": t.proxy(
                    renames["GoogleCloudDataplexV1LakeMetastoreIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesDelete"] = dataplex.post(
        "v1/{parent}/lakes",
        t.struct(
            {
                "parent": t.string(),
                "lakeId": t.string(),
                "validateOnly": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "metastore": t.proxy(
                    renames["GoogleCloudDataplexV1LakeMetastoreIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesCreate"] = dataplex.post(
        "v1/{parent}/lakes",
        t.struct(
            {
                "parent": t.string(),
                "lakeId": t.string(),
                "validateOnly": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "metastore": t.proxy(
                    renames["GoogleCloudDataplexV1LakeMetastoreIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesEnvironmentsTestIamPermissions"] = dataplex.get(
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
    functions["projectsLocationsLakesEnvironmentsPatch"] = dataplex.get(
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
    functions["projectsLocationsLakesEnvironmentsGet"] = dataplex.get(
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
    functions["projectsLocationsLakesEnvironmentsCreate"] = dataplex.get(
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
    functions["projectsLocationsLakesEnvironmentsDelete"] = dataplex.get(
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
    functions["projectsLocationsLakesEnvironmentsSetIamPolicy"] = dataplex.get(
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
    functions["projectsLocationsLakesEnvironmentsList"] = dataplex.get(
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
    functions["projectsLocationsLakesEnvironmentsGetIamPolicy"] = dataplex.get(
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
    functions["projectsLocationsLakesEnvironmentsSessionsList"] = dataplex.get(
        "v1/{parent}/sessions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1ListSessionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesContentCreate"] = dataplex.post(
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
    functions["projectsLocationsLakesContentList"] = dataplex.post(
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
    functions["projectsLocationsLakesContentGet"] = dataplex.post(
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
    functions["projectsLocationsLakesContentSetIamPolicy"] = dataplex.post(
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
    functions["projectsLocationsLakesContentPatch"] = dataplex.post(
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
    functions["projectsLocationsLakesContentDelete"] = dataplex.post(
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
    functions["projectsLocationsLakesContentGetIamPolicy"] = dataplex.post(
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
    functions["projectsLocationsLakesContentTestIamPermissions"] = dataplex.post(
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
    functions["projectsLocationsLakesTasksPatch"] = dataplex.post(
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
    functions["projectsLocationsLakesTasksGetIamPolicy"] = dataplex.post(
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
    functions["projectsLocationsLakesTasksDelete"] = dataplex.post(
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
    functions["projectsLocationsLakesTasksGet"] = dataplex.post(
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
    functions["projectsLocationsLakesTasksCreate"] = dataplex.post(
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
    functions["projectsLocationsLakesTasksSetIamPolicy"] = dataplex.post(
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
    functions["projectsLocationsLakesTasksRun"] = dataplex.post(
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
    functions["projectsLocationsLakesTasksList"] = dataplex.post(
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
    functions["projectsLocationsLakesTasksTestIamPermissions"] = dataplex.post(
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
    functions["projectsLocationsLakesTasksJobsList"] = dataplex.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDataplexV1JobOut"]),
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
    functions["projectsLocationsLakesTasksJobsGet"] = dataplex.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDataplexV1JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesDelete"] = dataplex.get(
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
    functions["projectsLocationsLakesZonesTestIamPermissions"] = dataplex.get(
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
    functions["projectsLocationsLakesZonesSetIamPolicy"] = dataplex.get(
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
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
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
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
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
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
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
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
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
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesEntitiesGet"] = dataplex.delete(
        "v1/{name}",
        t.struct(
            {"etag": t.string(), "name": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesEntitiesList"] = dataplex.delete(
        "v1/{name}",
        t.struct(
            {"etag": t.string(), "name": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesEntitiesUpdate"] = dataplex.delete(
        "v1/{name}",
        t.struct(
            {"etag": t.string(), "name": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesEntitiesCreate"] = dataplex.delete(
        "v1/{name}",
        t.struct(
            {"etag": t.string(), "name": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesEntitiesDelete"] = dataplex.delete(
        "v1/{name}",
        t.struct(
            {"etag": t.string(), "name": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesEntitiesPartitionsDelete"] = dataplex.get(
        "v1/{parent}/partitions",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
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
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1ListPartitionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesEntitiesPartitionsCreate"] = dataplex.get(
        "v1/{parent}/partitions",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
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
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1ListPartitionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesAssetsTestIamPermissions"] = dataplex.get(
        "v1/{parent}/assets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesAssetsDelete"] = dataplex.get(
        "v1/{parent}/assets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesAssetsGetIamPolicy"] = dataplex.get(
        "v1/{parent}/assets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesAssetsGet"] = dataplex.get(
        "v1/{parent}/assets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesAssetsPatch"] = dataplex.get(
        "v1/{parent}/assets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesAssetsCreate"] = dataplex.get(
        "v1/{parent}/assets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesAssetsSetIamPolicy"] = dataplex.get(
        "v1/{parent}/assets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesAssetsList"] = dataplex.get(
        "v1/{parent}/assets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesAssetsActionsList"] = dataplex.get(
        "v1/{parent}/actions",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1ListActionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsLakesZonesActionsList"] = dataplex.get(
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
    functions["projectsLocationsLakesActionsList"] = dataplex.get(
        "v1/{parent}/actions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1ListActionsResponseOut"]),
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
    functions["projectsLocationsOperationsGet"] = dataplex.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = dataplex.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = dataplex.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = dataplex.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataScansSetIamPolicy"] = dataplex.post(
        "v1/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1RunDataScanResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataScansGet"] = dataplex.post(
        "v1/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1RunDataScanResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataScansTestIamPermissions"] = dataplex.post(
        "v1/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1RunDataScanResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataScansDelete"] = dataplex.post(
        "v1/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1RunDataScanResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataScansPatch"] = dataplex.post(
        "v1/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1RunDataScanResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataScansList"] = dataplex.post(
        "v1/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1RunDataScanResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataScansGetIamPolicy"] = dataplex.post(
        "v1/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1RunDataScanResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataScansCreate"] = dataplex.post(
        "v1/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1RunDataScanResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataScansRun"] = dataplex.post(
        "v1/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1RunDataScanResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataScansJobsGet"] = dataplex.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
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
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDataplexV1ListDataScanJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataAttributeBindingsList"] = dataplex.get(
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
    functions["projectsLocationsDataAttributeBindingsSetIamPolicy"] = dataplex.get(
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
    functions["projectsLocationsDataAttributeBindingsGet"] = dataplex.get(
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
    functions["projectsLocationsDataAttributeBindingsPatch"] = dataplex.get(
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
        "projectsLocationsDataAttributeBindingsTestIamPermissions"
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
    functions["projectsLocationsDataAttributeBindingsCreate"] = dataplex.get(
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
    functions["projectsLocationsDataAttributeBindingsDelete"] = dataplex.get(
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
    functions["projectsLocationsDataAttributeBindingsGetIamPolicy"] = dataplex.get(
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
    functions["projectsLocationsDataTaxonomiesGetIamPolicy"] = dataplex.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesGet"] = dataplex.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesPatch"] = dataplex.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesList"] = dataplex.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesTestIamPermissions"] = dataplex.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesCreate"] = dataplex.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesSetIamPolicy"] = dataplex.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesDelete"] = dataplex.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesAttributesList"] = dataplex.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesAttributesDelete"] = dataplex.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesAttributesCreate"] = dataplex.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesAttributesGet"] = dataplex.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesAttributesPatch"] = dataplex.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsDataTaxonomiesAttributesTestIamPermissions"
    ] = dataplex.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesAttributesGetIamPolicy"] = dataplex.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataTaxonomiesAttributesSetIamPolicy"] = dataplex.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsGetIamPolicy"] = dataplex.post(
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
    functions["projectsLocationsEntryGroupsSetIamPolicy"] = dataplex.post(
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
    functions["projectsLocationsEntryGroupsTestIamPermissions"] = dataplex.post(
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
