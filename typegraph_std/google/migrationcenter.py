from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_migrationcenter():
    migrationcenter = HTTPRuntime("https://migrationcenter.googleapis.com/")

    renames = {
        "ErrorResponse": "_migrationcenter_1_ErrorResponse",
        "MoneyIn": "_migrationcenter_2_MoneyIn",
        "MoneyOut": "_migrationcenter_3_MoneyOut",
        "DiskEntryIn": "_migrationcenter_4_DiskEntryIn",
        "DiskEntryOut": "_migrationcenter_5_DiskEntryOut",
        "AggregationCountIn": "_migrationcenter_6_AggregationCountIn",
        "AggregationCountOut": "_migrationcenter_7_AggregationCountOut",
        "ListLocationsResponseIn": "_migrationcenter_8_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_migrationcenter_9_ListLocationsResponseOut",
        "AssetFrameIn": "_migrationcenter_10_AssetFrameIn",
        "AssetFrameOut": "_migrationcenter_11_AssetFrameOut",
        "HostsEntryIn": "_migrationcenter_12_HostsEntryIn",
        "HostsEntryOut": "_migrationcenter_13_HostsEntryOut",
        "VmwarePlatformDetailsIn": "_migrationcenter_14_VmwarePlatformDetailsIn",
        "VmwarePlatformDetailsOut": "_migrationcenter_15_VmwarePlatformDetailsOut",
        "ComputeEngineShapeDescriptorIn": "_migrationcenter_16_ComputeEngineShapeDescriptorIn",
        "ComputeEngineShapeDescriptorOut": "_migrationcenter_17_ComputeEngineShapeDescriptorOut",
        "GuestConfigDetailsIn": "_migrationcenter_18_GuestConfigDetailsIn",
        "GuestConfigDetailsOut": "_migrationcenter_19_GuestConfigDetailsOut",
        "ReportSummaryHistogramChartDataBucketIn": "_migrationcenter_20_ReportSummaryHistogramChartDataBucketIn",
        "ReportSummaryHistogramChartDataBucketOut": "_migrationcenter_21_ReportSummaryHistogramChartDataBucketOut",
        "ListAssetsResponseIn": "_migrationcenter_22_ListAssetsResponseIn",
        "ListAssetsResponseOut": "_migrationcenter_23_ListAssetsResponseOut",
        "OpenFileListIn": "_migrationcenter_24_OpenFileListIn",
        "OpenFileListOut": "_migrationcenter_25_OpenFileListOut",
        "RunningServiceListIn": "_migrationcenter_26_RunningServiceListIn",
        "RunningServiceListOut": "_migrationcenter_27_RunningServiceListOut",
        "GuestInstalledApplicationIn": "_migrationcenter_28_GuestInstalledApplicationIn",
        "GuestInstalledApplicationOut": "_migrationcenter_29_GuestInstalledApplicationOut",
        "ReportSummaryAssetAggregateStatsIn": "_migrationcenter_30_ReportSummaryAssetAggregateStatsIn",
        "ReportSummaryAssetAggregateStatsOut": "_migrationcenter_31_ReportSummaryAssetAggregateStatsOut",
        "InsightListIn": "_migrationcenter_32_InsightListIn",
        "InsightListOut": "_migrationcenter_33_InsightListOut",
        "ReportSummaryGroupPreferenceSetFindingIn": "_migrationcenter_34_ReportSummaryGroupPreferenceSetFindingIn",
        "ReportSummaryGroupPreferenceSetFindingOut": "_migrationcenter_35_ReportSummaryGroupPreferenceSetFindingOut",
        "AggregationResultFrequencyIn": "_migrationcenter_36_AggregationResultFrequencyIn",
        "AggregationResultFrequencyOut": "_migrationcenter_37_AggregationResultFrequencyOut",
        "NetworkConnectionListIn": "_migrationcenter_38_NetworkConnectionListIn",
        "NetworkConnectionListOut": "_migrationcenter_39_NetworkConnectionListOut",
        "ImportRowErrorIn": "_migrationcenter_40_ImportRowErrorIn",
        "ImportRowErrorOut": "_migrationcenter_41_ImportRowErrorOut",
        "AggregationSumIn": "_migrationcenter_42_AggregationSumIn",
        "AggregationSumOut": "_migrationcenter_43_AggregationSumOut",
        "AwsEc2PlatformDetailsIn": "_migrationcenter_44_AwsEc2PlatformDetailsIn",
        "AwsEc2PlatformDetailsOut": "_migrationcenter_45_AwsEc2PlatformDetailsOut",
        "DailyResourceUsageAggregationIn": "_migrationcenter_46_DailyResourceUsageAggregationIn",
        "DailyResourceUsageAggregationOut": "_migrationcenter_47_DailyResourceUsageAggregationOut",
        "AggregationResultIn": "_migrationcenter_48_AggregationResultIn",
        "AggregationResultOut": "_migrationcenter_49_AggregationResultOut",
        "PayloadFileIn": "_migrationcenter_50_PayloadFileIn",
        "PayloadFileOut": "_migrationcenter_51_PayloadFileOut",
        "DiskPartitionListIn": "_migrationcenter_52_DiskPartitionListIn",
        "DiskPartitionListOut": "_migrationcenter_53_DiskPartitionListOut",
        "UploadFileInfoIn": "_migrationcenter_54_UploadFileInfoIn",
        "UploadFileInfoOut": "_migrationcenter_55_UploadFileInfoOut",
        "GoogleKubernetesEngineMigrationTargetIn": "_migrationcenter_56_GoogleKubernetesEngineMigrationTargetIn",
        "GoogleKubernetesEngineMigrationTargetOut": "_migrationcenter_57_GoogleKubernetesEngineMigrationTargetOut",
        "GCSPayloadInfoIn": "_migrationcenter_58_GCSPayloadInfoIn",
        "GCSPayloadInfoOut": "_migrationcenter_59_GCSPayloadInfoOut",
        "ReportConfigIn": "_migrationcenter_60_ReportConfigIn",
        "ReportConfigOut": "_migrationcenter_61_ReportConfigOut",
        "StatusIn": "_migrationcenter_62_StatusIn",
        "StatusOut": "_migrationcenter_63_StatusOut",
        "AggregationResultHistogramBucketIn": "_migrationcenter_64_AggregationResultHistogramBucketIn",
        "AggregationResultHistogramBucketOut": "_migrationcenter_65_AggregationResultHistogramBucketOut",
        "MachineSeriesIn": "_migrationcenter_66_MachineSeriesIn",
        "MachineSeriesOut": "_migrationcenter_67_MachineSeriesOut",
        "ListImportJobsResponseIn": "_migrationcenter_68_ListImportJobsResponseIn",
        "ListImportJobsResponseOut": "_migrationcenter_69_ListImportJobsResponseOut",
        "VmwareEnginePreferencesIn": "_migrationcenter_70_VmwareEnginePreferencesIn",
        "VmwareEnginePreferencesOut": "_migrationcenter_71_VmwareEnginePreferencesOut",
        "VirtualMachineDetailsIn": "_migrationcenter_72_VirtualMachineDetailsIn",
        "VirtualMachineDetailsOut": "_migrationcenter_73_VirtualMachineDetailsOut",
        "FstabEntryListIn": "_migrationcenter_74_FstabEntryListIn",
        "FstabEntryListOut": "_migrationcenter_75_FstabEntryListOut",
        "NetworkUsageSampleIn": "_migrationcenter_76_NetworkUsageSampleIn",
        "NetworkUsageSampleOut": "_migrationcenter_77_NetworkUsageSampleOut",
        "DiskPartitionIn": "_migrationcenter_78_DiskPartitionIn",
        "DiskPartitionOut": "_migrationcenter_79_DiskPartitionOut",
        "SourceIn": "_migrationcenter_80_SourceIn",
        "SourceOut": "_migrationcenter_81_SourceOut",
        "ReportSummarySoleTenantNodeAllocationIn": "_migrationcenter_82_ReportSummarySoleTenantNodeAllocationIn",
        "ReportSummarySoleTenantNodeAllocationOut": "_migrationcenter_83_ReportSummarySoleTenantNodeAllocationOut",
        "ErrorFrameIn": "_migrationcenter_84_ErrorFrameIn",
        "ErrorFrameOut": "_migrationcenter_85_ErrorFrameOut",
        "ListImportDataFilesResponseIn": "_migrationcenter_86_ListImportDataFilesResponseIn",
        "ListImportDataFilesResponseOut": "_migrationcenter_87_ListImportDataFilesResponseOut",
        "NetworkConnectionIn": "_migrationcenter_88_NetworkConnectionIn",
        "NetworkConnectionOut": "_migrationcenter_89_NetworkConnectionOut",
        "ReportAssetFramesResponseIn": "_migrationcenter_90_ReportAssetFramesResponseIn",
        "ReportAssetFramesResponseOut": "_migrationcenter_91_ReportAssetFramesResponseOut",
        "NetworkAddressListIn": "_migrationcenter_92_NetworkAddressListIn",
        "NetworkAddressListOut": "_migrationcenter_93_NetworkAddressListOut",
        "ReportSummaryMachineFindingIn": "_migrationcenter_94_ReportSummaryMachineFindingIn",
        "ReportSummaryMachineFindingOut": "_migrationcenter_95_ReportSummaryMachineFindingOut",
        "OperationIn": "_migrationcenter_96_OperationIn",
        "OperationOut": "_migrationcenter_97_OperationOut",
        "ReportSummaryIn": "_migrationcenter_98_ReportSummaryIn",
        "ReportSummaryOut": "_migrationcenter_99_ReportSummaryOut",
        "EmptyIn": "_migrationcenter_100_EmptyIn",
        "EmptyOut": "_migrationcenter_101_EmptyOut",
        "RuntimeNetworkInfoIn": "_migrationcenter_102_RuntimeNetworkInfoIn",
        "RuntimeNetworkInfoOut": "_migrationcenter_103_RuntimeNetworkInfoOut",
        "BiosDetailsIn": "_migrationcenter_104_BiosDetailsIn",
        "BiosDetailsOut": "_migrationcenter_105_BiosDetailsOut",
        "RunningProcessIn": "_migrationcenter_106_RunningProcessIn",
        "RunningProcessOut": "_migrationcenter_107_RunningProcessOut",
        "ListOperationsResponseIn": "_migrationcenter_108_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_migrationcenter_109_ListOperationsResponseOut",
        "AggregationHistogramIn": "_migrationcenter_110_AggregationHistogramIn",
        "AggregationHistogramOut": "_migrationcenter_111_AggregationHistogramOut",
        "RunningProcessListIn": "_migrationcenter_112_RunningProcessListIn",
        "RunningProcessListOut": "_migrationcenter_113_RunningProcessListOut",
        "InsightIn": "_migrationcenter_114_InsightIn",
        "InsightOut": "_migrationcenter_115_InsightOut",
        "ReportSummaryGroupFindingIn": "_migrationcenter_116_ReportSummaryGroupFindingIn",
        "ReportSummaryGroupFindingOut": "_migrationcenter_117_ReportSummaryGroupFindingOut",
        "OperationMetadataIn": "_migrationcenter_118_OperationMetadataIn",
        "OperationMetadataOut": "_migrationcenter_119_OperationMetadataOut",
        "AssetPerformanceDataIn": "_migrationcenter_120_AssetPerformanceDataIn",
        "AssetPerformanceDataOut": "_migrationcenter_121_AssetPerformanceDataOut",
        "ComputeEngineMigrationTargetIn": "_migrationcenter_122_ComputeEngineMigrationTargetIn",
        "ComputeEngineMigrationTargetOut": "_migrationcenter_123_ComputeEngineMigrationTargetOut",
        "HostsEntryListIn": "_migrationcenter_124_HostsEntryListIn",
        "HostsEntryListOut": "_migrationcenter_125_HostsEntryListOut",
        "SoleTenancyPreferencesIn": "_migrationcenter_126_SoleTenancyPreferencesIn",
        "SoleTenancyPreferencesOut": "_migrationcenter_127_SoleTenancyPreferencesOut",
        "DateIn": "_migrationcenter_128_DateIn",
        "DateOut": "_migrationcenter_129_DateOut",
        "CpuUsageSampleIn": "_migrationcenter_130_CpuUsageSampleIn",
        "CpuUsageSampleOut": "_migrationcenter_131_CpuUsageSampleOut",
        "DateTimeIn": "_migrationcenter_132_DateTimeIn",
        "DateTimeOut": "_migrationcenter_133_DateTimeOut",
        "MigrationInsightIn": "_migrationcenter_134_MigrationInsightIn",
        "MigrationInsightOut": "_migrationcenter_135_MigrationInsightOut",
        "MachinePreferencesIn": "_migrationcenter_136_MachinePreferencesIn",
        "MachinePreferencesOut": "_migrationcenter_137_MachinePreferencesOut",
        "AssetIn": "_migrationcenter_138_AssetIn",
        "AssetOut": "_migrationcenter_139_AssetOut",
        "VirtualMachineArchitectureDetailsIn": "_migrationcenter_140_VirtualMachineArchitectureDetailsIn",
        "VirtualMachineArchitectureDetailsOut": "_migrationcenter_141_VirtualMachineArchitectureDetailsOut",
        "ReportSummaryChartDataDataPointIn": "_migrationcenter_142_ReportSummaryChartDataDataPointIn",
        "ReportSummaryChartDataDataPointOut": "_migrationcenter_143_ReportSummaryChartDataDataPointOut",
        "VmwareDiskConfigIn": "_migrationcenter_144_VmwareDiskConfigIn",
        "VmwareDiskConfigOut": "_migrationcenter_145_VmwareDiskConfigOut",
        "ListReportConfigsResponseIn": "_migrationcenter_146_ListReportConfigsResponseIn",
        "ListReportConfigsResponseOut": "_migrationcenter_147_ListReportConfigsResponseOut",
        "RegionPreferencesIn": "_migrationcenter_148_RegionPreferencesIn",
        "RegionPreferencesOut": "_migrationcenter_149_RegionPreferencesOut",
        "VirtualMachineDiskDetailsIn": "_migrationcenter_150_VirtualMachineDiskDetailsIn",
        "VirtualMachineDiskDetailsOut": "_migrationcenter_151_VirtualMachineDiskDetailsOut",
        "SettingsIn": "_migrationcenter_152_SettingsIn",
        "SettingsOut": "_migrationcenter_153_SettingsOut",
        "ReportSummarySoleTenantFindingIn": "_migrationcenter_154_ReportSummarySoleTenantFindingIn",
        "ReportSummarySoleTenantFindingOut": "_migrationcenter_155_ReportSummarySoleTenantFindingOut",
        "DailyResourceUsageAggregationCPUIn": "_migrationcenter_156_DailyResourceUsageAggregationCPUIn",
        "DailyResourceUsageAggregationCPUOut": "_migrationcenter_157_DailyResourceUsageAggregationCPUOut",
        "AggregationIn": "_migrationcenter_158_AggregationIn",
        "AggregationOut": "_migrationcenter_159_AggregationOut",
        "NfsExportIn": "_migrationcenter_160_NfsExportIn",
        "NfsExportOut": "_migrationcenter_161_NfsExportOut",
        "NetworkAdapterDetailsIn": "_migrationcenter_162_NetworkAdapterDetailsIn",
        "NetworkAdapterDetailsOut": "_migrationcenter_163_NetworkAdapterDetailsOut",
        "ReportSummaryMachineSeriesAllocationIn": "_migrationcenter_164_ReportSummaryMachineSeriesAllocationIn",
        "ReportSummaryMachineSeriesAllocationOut": "_migrationcenter_165_ReportSummaryMachineSeriesAllocationOut",
        "ReportConfigGroupPreferenceSetAssignmentIn": "_migrationcenter_166_ReportConfigGroupPreferenceSetAssignmentIn",
        "ReportConfigGroupPreferenceSetAssignmentOut": "_migrationcenter_167_ReportConfigGroupPreferenceSetAssignmentOut",
        "GuestOsDetailsIn": "_migrationcenter_168_GuestOsDetailsIn",
        "GuestOsDetailsOut": "_migrationcenter_169_GuestOsDetailsOut",
        "BatchUpdateAssetsRequestIn": "_migrationcenter_170_BatchUpdateAssetsRequestIn",
        "BatchUpdateAssetsRequestOut": "_migrationcenter_171_BatchUpdateAssetsRequestOut",
        "DailyResourceUsageAggregationStatsIn": "_migrationcenter_172_DailyResourceUsageAggregationStatsIn",
        "DailyResourceUsageAggregationStatsOut": "_migrationcenter_173_DailyResourceUsageAggregationStatsOut",
        "LocationIn": "_migrationcenter_174_LocationIn",
        "LocationOut": "_migrationcenter_175_LocationOut",
        "NfsExportListIn": "_migrationcenter_176_NfsExportListIn",
        "NfsExportListOut": "_migrationcenter_177_NfsExportListOut",
        "BatchUpdateAssetsResponseIn": "_migrationcenter_178_BatchUpdateAssetsResponseIn",
        "BatchUpdateAssetsResponseOut": "_migrationcenter_179_BatchUpdateAssetsResponseOut",
        "MemoryUsageSampleIn": "_migrationcenter_180_MemoryUsageSampleIn",
        "MemoryUsageSampleOut": "_migrationcenter_181_MemoryUsageSampleOut",
        "AggregationResultHistogramIn": "_migrationcenter_182_AggregationResultHistogramIn",
        "AggregationResultHistogramOut": "_migrationcenter_183_AggregationResultHistogramOut",
        "GroupIn": "_migrationcenter_184_GroupIn",
        "GroupOut": "_migrationcenter_185_GroupOut",
        "ListPreferenceSetsResponseIn": "_migrationcenter_186_ListPreferenceSetsResponseIn",
        "ListPreferenceSetsResponseOut": "_migrationcenter_187_ListPreferenceSetsResponseOut",
        "PreferenceSetIn": "_migrationcenter_188_PreferenceSetIn",
        "PreferenceSetOut": "_migrationcenter_189_PreferenceSetOut",
        "RunImportJobRequestIn": "_migrationcenter_190_RunImportJobRequestIn",
        "RunImportJobRequestOut": "_migrationcenter_191_RunImportJobRequestOut",
        "FileValidationReportIn": "_migrationcenter_192_FileValidationReportIn",
        "FileValidationReportOut": "_migrationcenter_193_FileValidationReportOut",
        "ValidationReportIn": "_migrationcenter_194_ValidationReportIn",
        "ValidationReportOut": "_migrationcenter_195_ValidationReportOut",
        "AddAssetsToGroupRequestIn": "_migrationcenter_196_AddAssetsToGroupRequestIn",
        "AddAssetsToGroupRequestOut": "_migrationcenter_197_AddAssetsToGroupRequestOut",
        "AggregationFrequencyIn": "_migrationcenter_198_AggregationFrequencyIn",
        "AggregationFrequencyOut": "_migrationcenter_199_AggregationFrequencyOut",
        "NetworkAdapterListIn": "_migrationcenter_200_NetworkAdapterListIn",
        "NetworkAdapterListOut": "_migrationcenter_201_NetworkAdapterListOut",
        "VirtualMachineNetworkDetailsIn": "_migrationcenter_202_VirtualMachineNetworkDetailsIn",
        "VirtualMachineNetworkDetailsOut": "_migrationcenter_203_VirtualMachineNetworkDetailsOut",
        "CancelOperationRequestIn": "_migrationcenter_204_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_migrationcenter_205_CancelOperationRequestOut",
        "BatchDeleteAssetsRequestIn": "_migrationcenter_206_BatchDeleteAssetsRequestIn",
        "BatchDeleteAssetsRequestOut": "_migrationcenter_207_BatchDeleteAssetsRequestOut",
        "AggregateAssetsValuesResponseIn": "_migrationcenter_208_AggregateAssetsValuesResponseIn",
        "AggregateAssetsValuesResponseOut": "_migrationcenter_209_AggregateAssetsValuesResponseOut",
        "ValidateImportJobRequestIn": "_migrationcenter_210_ValidateImportJobRequestIn",
        "ValidateImportJobRequestOut": "_migrationcenter_211_ValidateImportJobRequestOut",
        "DailyResourceUsageAggregationDiskIn": "_migrationcenter_212_DailyResourceUsageAggregationDiskIn",
        "DailyResourceUsageAggregationDiskOut": "_migrationcenter_213_DailyResourceUsageAggregationDiskOut",
        "ListErrorFramesResponseIn": "_migrationcenter_214_ListErrorFramesResponseIn",
        "ListErrorFramesResponseOut": "_migrationcenter_215_ListErrorFramesResponseOut",
        "ImportDataFileIn": "_migrationcenter_216_ImportDataFileIn",
        "ImportDataFileOut": "_migrationcenter_217_ImportDataFileOut",
        "VirtualMachinePreferencesIn": "_migrationcenter_218_VirtualMachinePreferencesIn",
        "VirtualMachinePreferencesOut": "_migrationcenter_219_VirtualMachinePreferencesOut",
        "ReportSummaryVMWareNodeAllocationIn": "_migrationcenter_220_ReportSummaryVMWareNodeAllocationIn",
        "ReportSummaryVMWareNodeAllocationOut": "_migrationcenter_221_ReportSummaryVMWareNodeAllocationOut",
        "FitDescriptorIn": "_migrationcenter_222_FitDescriptorIn",
        "FitDescriptorOut": "_migrationcenter_223_FitDescriptorOut",
        "AggregateAssetsValuesRequestIn": "_migrationcenter_224_AggregateAssetsValuesRequestIn",
        "AggregateAssetsValuesRequestOut": "_migrationcenter_225_AggregateAssetsValuesRequestOut",
        "VmwareEngineMigrationTargetIn": "_migrationcenter_226_VmwareEngineMigrationTargetIn",
        "VmwareEngineMigrationTargetOut": "_migrationcenter_227_VmwareEngineMigrationTargetOut",
        "TimeZoneIn": "_migrationcenter_228_TimeZoneIn",
        "TimeZoneOut": "_migrationcenter_229_TimeZoneOut",
        "RemoveAssetsFromGroupRequestIn": "_migrationcenter_230_RemoveAssetsFromGroupRequestIn",
        "RemoveAssetsFromGroupRequestOut": "_migrationcenter_231_RemoveAssetsFromGroupRequestOut",
        "NetworkAddressIn": "_migrationcenter_232_NetworkAddressIn",
        "NetworkAddressOut": "_migrationcenter_233_NetworkAddressOut",
        "ReportSummaryHistogramChartDataIn": "_migrationcenter_234_ReportSummaryHistogramChartDataIn",
        "ReportSummaryHistogramChartDataOut": "_migrationcenter_235_ReportSummaryHistogramChartDataOut",
        "ImportErrorIn": "_migrationcenter_236_ImportErrorIn",
        "ImportErrorOut": "_migrationcenter_237_ImportErrorOut",
        "DailyResourceUsageAggregationMemoryIn": "_migrationcenter_238_DailyResourceUsageAggregationMemoryIn",
        "DailyResourceUsageAggregationMemoryOut": "_migrationcenter_239_DailyResourceUsageAggregationMemoryOut",
        "PhysicalPlatformDetailsIn": "_migrationcenter_240_PhysicalPlatformDetailsIn",
        "PhysicalPlatformDetailsOut": "_migrationcenter_241_PhysicalPlatformDetailsOut",
        "AggregationResultSumIn": "_migrationcenter_242_AggregationResultSumIn",
        "AggregationResultSumOut": "_migrationcenter_243_AggregationResultSumOut",
        "ReportSummaryUtilizationChartDataIn": "_migrationcenter_244_ReportSummaryUtilizationChartDataIn",
        "ReportSummaryUtilizationChartDataOut": "_migrationcenter_245_ReportSummaryUtilizationChartDataOut",
        "FrameViolationEntryIn": "_migrationcenter_246_FrameViolationEntryIn",
        "FrameViolationEntryOut": "_migrationcenter_247_FrameViolationEntryOut",
        "PlatformDetailsIn": "_migrationcenter_248_PlatformDetailsIn",
        "PlatformDetailsOut": "_migrationcenter_249_PlatformDetailsOut",
        "ImportJobIn": "_migrationcenter_250_ImportJobIn",
        "ImportJobOut": "_migrationcenter_251_ImportJobOut",
        "AzureVmPlatformDetailsIn": "_migrationcenter_252_AzureVmPlatformDetailsIn",
        "AzureVmPlatformDetailsOut": "_migrationcenter_253_AzureVmPlatformDetailsOut",
        "ListGroupsResponseIn": "_migrationcenter_254_ListGroupsResponseIn",
        "ListGroupsResponseOut": "_migrationcenter_255_ListGroupsResponseOut",
        "ReportIn": "_migrationcenter_256_ReportIn",
        "ReportOut": "_migrationcenter_257_ReportOut",
        "DiskUsageSampleIn": "_migrationcenter_258_DiskUsageSampleIn",
        "DiskUsageSampleOut": "_migrationcenter_259_DiskUsageSampleOut",
        "ReportSummaryVMWareEngineFindingIn": "_migrationcenter_260_ReportSummaryVMWareEngineFindingIn",
        "ReportSummaryVMWareEngineFindingOut": "_migrationcenter_261_ReportSummaryVMWareEngineFindingOut",
        "DiskEntryListIn": "_migrationcenter_262_DiskEntryListIn",
        "DiskEntryListOut": "_migrationcenter_263_DiskEntryListOut",
        "SoleTenantNodeTypeIn": "_migrationcenter_264_SoleTenantNodeTypeIn",
        "SoleTenantNodeTypeOut": "_migrationcenter_265_SoleTenantNodeTypeOut",
        "GuestInstalledApplicationListIn": "_migrationcenter_266_GuestInstalledApplicationListIn",
        "GuestInstalledApplicationListOut": "_migrationcenter_267_GuestInstalledApplicationListOut",
        "ComputeEnginePreferencesIn": "_migrationcenter_268_ComputeEnginePreferencesIn",
        "ComputeEnginePreferencesOut": "_migrationcenter_269_ComputeEnginePreferencesOut",
        "UpdateAssetRequestIn": "_migrationcenter_270_UpdateAssetRequestIn",
        "UpdateAssetRequestOut": "_migrationcenter_271_UpdateAssetRequestOut",
        "ComputeStorageDescriptorIn": "_migrationcenter_272_ComputeStorageDescriptorIn",
        "ComputeStorageDescriptorOut": "_migrationcenter_273_ComputeStorageDescriptorOut",
        "ReportSummaryVMWareNodeIn": "_migrationcenter_274_ReportSummaryVMWareNodeIn",
        "ReportSummaryVMWareNodeOut": "_migrationcenter_275_ReportSummaryVMWareNodeOut",
        "AssetListIn": "_migrationcenter_276_AssetListIn",
        "AssetListOut": "_migrationcenter_277_AssetListOut",
        "RunningServiceIn": "_migrationcenter_278_RunningServiceIn",
        "RunningServiceOut": "_migrationcenter_279_RunningServiceOut",
        "FramesIn": "_migrationcenter_280_FramesIn",
        "FramesOut": "_migrationcenter_281_FramesOut",
        "ExecutionReportIn": "_migrationcenter_282_ExecutionReportIn",
        "ExecutionReportOut": "_migrationcenter_283_ExecutionReportOut",
        "SelinuxIn": "_migrationcenter_284_SelinuxIn",
        "SelinuxOut": "_migrationcenter_285_SelinuxOut",
        "ReportSummaryChartDataIn": "_migrationcenter_286_ReportSummaryChartDataIn",
        "ReportSummaryChartDataOut": "_migrationcenter_287_ReportSummaryChartDataOut",
        "OpenFileDetailsIn": "_migrationcenter_288_OpenFileDetailsIn",
        "OpenFileDetailsOut": "_migrationcenter_289_OpenFileDetailsOut",
        "GenericPlatformDetailsIn": "_migrationcenter_290_GenericPlatformDetailsIn",
        "GenericPlatformDetailsOut": "_migrationcenter_291_GenericPlatformDetailsOut",
        "InlinePayloadInfoIn": "_migrationcenter_292_InlinePayloadInfoIn",
        "InlinePayloadInfoOut": "_migrationcenter_293_InlinePayloadInfoOut",
        "GuestRuntimeDetailsIn": "_migrationcenter_294_GuestRuntimeDetailsIn",
        "GuestRuntimeDetailsOut": "_migrationcenter_295_GuestRuntimeDetailsOut",
        "ListSourcesResponseIn": "_migrationcenter_296_ListSourcesResponseIn",
        "ListSourcesResponseOut": "_migrationcenter_297_ListSourcesResponseOut",
        "AggregationResultCountIn": "_migrationcenter_298_AggregationResultCountIn",
        "AggregationResultCountOut": "_migrationcenter_299_AggregationResultCountOut",
        "PerformanceSampleIn": "_migrationcenter_300_PerformanceSampleIn",
        "PerformanceSampleOut": "_migrationcenter_301_PerformanceSampleOut",
        "FstabEntryIn": "_migrationcenter_302_FstabEntryIn",
        "FstabEntryOut": "_migrationcenter_303_FstabEntryOut",
        "DailyResourceUsageAggregationNetworkIn": "_migrationcenter_304_DailyResourceUsageAggregationNetworkIn",
        "DailyResourceUsageAggregationNetworkOut": "_migrationcenter_305_DailyResourceUsageAggregationNetworkOut",
        "ListReportsResponseIn": "_migrationcenter_306_ListReportsResponseIn",
        "ListReportsResponseOut": "_migrationcenter_307_ListReportsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["MoneyIn"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "nanos": t.integer().optional(),
            "units": t.string().optional(),
        }
    ).named(renames["MoneyIn"])
    types["MoneyOut"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "nanos": t.integer().optional(),
            "units": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoneyOut"])
    types["DiskEntryIn"] = t.struct(
        {
            "diskLabelType": t.string().optional(),
            "totalFreeBytes": t.string().optional(),
            "diskLabel": t.string().optional(),
            "interfaceType": t.string().optional(),
            "totalCapacityBytes": t.string().optional(),
            "status": t.string().optional(),
            "partitions": t.proxy(renames["DiskPartitionListIn"]).optional(),
            "hwAddress": t.string().optional(),
            "vmwareConfig": t.proxy(renames["VmwareDiskConfigIn"]).optional(),
        }
    ).named(renames["DiskEntryIn"])
    types["DiskEntryOut"] = t.struct(
        {
            "diskLabelType": t.string().optional(),
            "totalFreeBytes": t.string().optional(),
            "diskLabel": t.string().optional(),
            "interfaceType": t.string().optional(),
            "totalCapacityBytes": t.string().optional(),
            "status": t.string().optional(),
            "partitions": t.proxy(renames["DiskPartitionListOut"]).optional(),
            "hwAddress": t.string().optional(),
            "vmwareConfig": t.proxy(renames["VmwareDiskConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskEntryOut"])
    types["AggregationCountIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AggregationCountIn"]
    )
    types["AggregationCountOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AggregationCountOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["AssetFrameIn"] = t.struct(
        {
            "reportTime": t.string().optional(),
            "virtualMachineDetails": t.proxy(
                renames["VirtualMachineDetailsIn"]
            ).optional(),
            "traceToken": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "performanceSamples": t.array(
                t.proxy(renames["PerformanceSampleIn"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["AssetFrameIn"])
    types["AssetFrameOut"] = t.struct(
        {
            "reportTime": t.string().optional(),
            "virtualMachineDetails": t.proxy(
                renames["VirtualMachineDetailsOut"]
            ).optional(),
            "traceToken": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "performanceSamples": t.array(
                t.proxy(renames["PerformanceSampleOut"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetFrameOut"])
    types["HostsEntryIn"] = t.struct(
        {"hostNames": t.array(t.string()).optional(), "ip": t.string().optional()}
    ).named(renames["HostsEntryIn"])
    types["HostsEntryOut"] = t.struct(
        {
            "hostNames": t.array(t.string()).optional(),
            "ip": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HostsEntryOut"])
    types["VmwarePlatformDetailsIn"] = t.struct(
        {
            "vcenterVersion": t.string().optional(),
            "esxVersion": t.string().optional(),
            "osid": t.string().optional(),
        }
    ).named(renames["VmwarePlatformDetailsIn"])
    types["VmwarePlatformDetailsOut"] = t.struct(
        {
            "vcenterVersion": t.string().optional(),
            "esxVersion": t.string().optional(),
            "osid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwarePlatformDetailsOut"])
    types["ComputeEngineShapeDescriptorIn"] = t.struct(
        {
            "machineType": t.string().optional(),
            "logicalCoreCount": t.integer().optional(),
            "physicalCoreCount": t.integer().optional(),
            "storage": t.array(
                t.proxy(renames["ComputeStorageDescriptorIn"])
            ).optional(),
            "memoryMb": t.integer().optional(),
            "series": t.string().optional(),
        }
    ).named(renames["ComputeEngineShapeDescriptorIn"])
    types["ComputeEngineShapeDescriptorOut"] = t.struct(
        {
            "machineType": t.string().optional(),
            "logicalCoreCount": t.integer().optional(),
            "physicalCoreCount": t.integer().optional(),
            "storage": t.array(
                t.proxy(renames["ComputeStorageDescriptorOut"])
            ).optional(),
            "memoryMb": t.integer().optional(),
            "series": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeEngineShapeDescriptorOut"])
    types["GuestConfigDetailsIn"] = t.struct(
        {
            "issue": t.string().optional(),
            "nfsExports": t.proxy(renames["NfsExportListIn"]).optional(),
            "hosts": t.proxy(renames["HostsEntryListIn"]).optional(),
            "fstab": t.proxy(renames["FstabEntryListIn"]).optional(),
            "selinux": t.proxy(renames["SelinuxIn"]).optional(),
        }
    ).named(renames["GuestConfigDetailsIn"])
    types["GuestConfigDetailsOut"] = t.struct(
        {
            "issue": t.string().optional(),
            "nfsExports": t.proxy(renames["NfsExportListOut"]).optional(),
            "hosts": t.proxy(renames["HostsEntryListOut"]).optional(),
            "fstab": t.proxy(renames["FstabEntryListOut"]).optional(),
            "selinux": t.proxy(renames["SelinuxOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestConfigDetailsOut"])
    types["ReportSummaryHistogramChartDataBucketIn"] = t.struct(
        {
            "count": t.string().optional(),
            "upperBound": t.string().optional(),
            "lowerBound": t.string().optional(),
        }
    ).named(renames["ReportSummaryHistogramChartDataBucketIn"])
    types["ReportSummaryHistogramChartDataBucketOut"] = t.struct(
        {
            "count": t.string().optional(),
            "upperBound": t.string().optional(),
            "lowerBound": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryHistogramChartDataBucketOut"])
    types["ListAssetsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assets": t.array(t.proxy(renames["AssetIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListAssetsResponseIn"])
    types["ListAssetsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assets": t.array(t.proxy(renames["AssetOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAssetsResponseOut"])
    types["OpenFileListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["OpenFileDetailsIn"])).optional()}
    ).named(renames["OpenFileListIn"])
    types["OpenFileListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["OpenFileDetailsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OpenFileListOut"])
    types["RunningServiceListIn"] = t.struct(
        {"services": t.array(t.proxy(renames["RunningServiceIn"])).optional()}
    ).named(renames["RunningServiceListIn"])
    types["RunningServiceListOut"] = t.struct(
        {
            "services": t.array(t.proxy(renames["RunningServiceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunningServiceListOut"])
    types["GuestInstalledApplicationIn"] = t.struct(
        {
            "version": t.string().optional(),
            "time": t.string().optional(),
            "name": t.string().optional(),
            "vendor": t.string().optional(),
            "path": t.string().optional(),
        }
    ).named(renames["GuestInstalledApplicationIn"])
    types["GuestInstalledApplicationOut"] = t.struct(
        {
            "version": t.string().optional(),
            "time": t.string().optional(),
            "name": t.string().optional(),
            "vendor": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestInstalledApplicationOut"])
    types["ReportSummaryAssetAggregateStatsIn"] = t.struct(
        {
            "operatingSystem": t.proxy(renames["ReportSummaryChartDataIn"]).optional(),
            "memoryUtilization": t.proxy(
                renames["ReportSummaryChartDataIn"]
            ).optional(),
            "storageUtilization": t.proxy(
                renames["ReportSummaryChartDataIn"]
            ).optional(),
            "storageUtilizationChart": t.proxy(
                renames["ReportSummaryUtilizationChartDataIn"]
            ).optional(),
            "memoryUtilizationChart": t.proxy(
                renames["ReportSummaryUtilizationChartDataIn"]
            ).optional(),
            "storageBytesHistogram": t.proxy(
                renames["ReportSummaryHistogramChartDataIn"]
            ).optional(),
            "memoryBytesHistogram": t.proxy(
                renames["ReportSummaryHistogramChartDataIn"]
            ).optional(),
            "totalAssets": t.string().optional(),
            "coreCountHistogram": t.proxy(
                renames["ReportSummaryHistogramChartDataIn"]
            ).optional(),
            "totalStorageBytes": t.string().optional(),
            "totalMemoryBytes": t.string().optional(),
            "assetAge": t.proxy(renames["ReportSummaryChartDataIn"]).optional(),
            "totalCores": t.string().optional(),
        }
    ).named(renames["ReportSummaryAssetAggregateStatsIn"])
    types["ReportSummaryAssetAggregateStatsOut"] = t.struct(
        {
            "operatingSystem": t.proxy(renames["ReportSummaryChartDataOut"]).optional(),
            "memoryUtilization": t.proxy(
                renames["ReportSummaryChartDataOut"]
            ).optional(),
            "storageUtilization": t.proxy(
                renames["ReportSummaryChartDataOut"]
            ).optional(),
            "storageUtilizationChart": t.proxy(
                renames["ReportSummaryUtilizationChartDataOut"]
            ).optional(),
            "memoryUtilizationChart": t.proxy(
                renames["ReportSummaryUtilizationChartDataOut"]
            ).optional(),
            "storageBytesHistogram": t.proxy(
                renames["ReportSummaryHistogramChartDataOut"]
            ).optional(),
            "memoryBytesHistogram": t.proxy(
                renames["ReportSummaryHistogramChartDataOut"]
            ).optional(),
            "totalAssets": t.string().optional(),
            "coreCountHistogram": t.proxy(
                renames["ReportSummaryHistogramChartDataOut"]
            ).optional(),
            "totalStorageBytes": t.string().optional(),
            "totalMemoryBytes": t.string().optional(),
            "assetAge": t.proxy(renames["ReportSummaryChartDataOut"]).optional(),
            "totalCores": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryAssetAggregateStatsOut"])
    types["InsightListIn"] = t.struct({"_": t.string().optional()}).named(
        renames["InsightListIn"]
    )
    types["InsightListOut"] = t.struct(
        {
            "insights": t.array(t.proxy(renames["InsightOut"])).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsightListOut"])
    types["ReportSummaryGroupPreferenceSetFindingIn"] = t.struct(
        {
            "preferredRegion": t.string().optional(),
            "monthlyCostTotal": t.proxy(renames["MoneyIn"]).optional(),
            "displayName": t.string().optional(),
            "monthlyCostOsLicense": t.proxy(renames["MoneyIn"]).optional(),
            "soleTenantFinding": t.proxy(
                renames["ReportSummarySoleTenantFindingIn"]
            ).optional(),
            "monthlyCostStorage": t.proxy(renames["MoneyIn"]).optional(),
            "monthlyCostNetworkEgress": t.proxy(renames["MoneyIn"]).optional(),
            "monthlyCostOther": t.proxy(renames["MoneyIn"]).optional(),
            "description": t.string().optional(),
            "monthlyCostCompute": t.proxy(renames["MoneyIn"]).optional(),
            "machinePreferences": t.proxy(
                renames["VirtualMachinePreferencesIn"]
            ).optional(),
            "pricingTrack": t.string().optional(),
            "vmwareEngineFinding": t.proxy(
                renames["ReportSummaryVMWareEngineFindingIn"]
            ).optional(),
            "machineFinding": t.proxy(
                renames["ReportSummaryMachineFindingIn"]
            ).optional(),
            "topPriority": t.string().optional(),
        }
    ).named(renames["ReportSummaryGroupPreferenceSetFindingIn"])
    types["ReportSummaryGroupPreferenceSetFindingOut"] = t.struct(
        {
            "preferredRegion": t.string().optional(),
            "monthlyCostTotal": t.proxy(renames["MoneyOut"]).optional(),
            "displayName": t.string().optional(),
            "monthlyCostOsLicense": t.proxy(renames["MoneyOut"]).optional(),
            "soleTenantFinding": t.proxy(
                renames["ReportSummarySoleTenantFindingOut"]
            ).optional(),
            "monthlyCostStorage": t.proxy(renames["MoneyOut"]).optional(),
            "monthlyCostNetworkEgress": t.proxy(renames["MoneyOut"]).optional(),
            "monthlyCostOther": t.proxy(renames["MoneyOut"]).optional(),
            "description": t.string().optional(),
            "monthlyCostCompute": t.proxy(renames["MoneyOut"]).optional(),
            "machinePreferences": t.proxy(
                renames["VirtualMachinePreferencesOut"]
            ).optional(),
            "pricingTrack": t.string().optional(),
            "vmwareEngineFinding": t.proxy(
                renames["ReportSummaryVMWareEngineFindingOut"]
            ).optional(),
            "machineFinding": t.proxy(
                renames["ReportSummaryMachineFindingOut"]
            ).optional(),
            "topPriority": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryGroupPreferenceSetFindingOut"])
    types["AggregationResultFrequencyIn"] = t.struct(
        {"values": t.struct({"_": t.string().optional()})}
    ).named(renames["AggregationResultFrequencyIn"])
    types["AggregationResultFrequencyOut"] = t.struct(
        {
            "values": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationResultFrequencyOut"])
    types["NetworkConnectionListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["NetworkConnectionIn"])).optional()}
    ).named(renames["NetworkConnectionListIn"])
    types["NetworkConnectionListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["NetworkConnectionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConnectionListOut"])
    types["ImportRowErrorIn"] = t.struct(
        {
            "rowNumber": t.integer().optional(),
            "errors": t.array(t.proxy(renames["ImportErrorIn"])).optional(),
            "vmUuid": t.string().optional(),
            "vmName": t.string().optional(),
        }
    ).named(renames["ImportRowErrorIn"])
    types["ImportRowErrorOut"] = t.struct(
        {
            "rowNumber": t.integer().optional(),
            "errors": t.array(t.proxy(renames["ImportErrorOut"])).optional(),
            "vmUuid": t.string().optional(),
            "vmName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportRowErrorOut"])
    types["AggregationSumIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AggregationSumIn"]
    )
    types["AggregationSumOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AggregationSumOut"])
    types["AwsEc2PlatformDetailsIn"] = t.struct(
        {"machineTypeLabel": t.string().optional(), "location": t.string().optional()}
    ).named(renames["AwsEc2PlatformDetailsIn"])
    types["AwsEc2PlatformDetailsOut"] = t.struct(
        {
            "machineTypeLabel": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AwsEc2PlatformDetailsOut"])
    types["DailyResourceUsageAggregationIn"] = t.struct(
        {
            "cpu": t.proxy(renames["DailyResourceUsageAggregationCPUIn"]).optional(),
            "memory": t.proxy(
                renames["DailyResourceUsageAggregationMemoryIn"]
            ).optional(),
            "disk": t.proxy(renames["DailyResourceUsageAggregationDiskIn"]).optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
            "network": t.proxy(
                renames["DailyResourceUsageAggregationNetworkIn"]
            ).optional(),
        }
    ).named(renames["DailyResourceUsageAggregationIn"])
    types["DailyResourceUsageAggregationOut"] = t.struct(
        {
            "cpu": t.proxy(renames["DailyResourceUsageAggregationCPUOut"]).optional(),
            "memory": t.proxy(
                renames["DailyResourceUsageAggregationMemoryOut"]
            ).optional(),
            "disk": t.proxy(renames["DailyResourceUsageAggregationDiskOut"]).optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "network": t.proxy(
                renames["DailyResourceUsageAggregationNetworkOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DailyResourceUsageAggregationOut"])
    types["AggregationResultIn"] = t.struct(
        {
            "histogram": t.proxy(renames["AggregationResultHistogramIn"]),
            "count": t.proxy(renames["AggregationResultCountIn"]),
            "field": t.string(),
            "frequency": t.proxy(renames["AggregationResultFrequencyIn"]),
            "sum": t.proxy(renames["AggregationResultSumIn"]),
        }
    ).named(renames["AggregationResultIn"])
    types["AggregationResultOut"] = t.struct(
        {
            "histogram": t.proxy(renames["AggregationResultHistogramOut"]),
            "count": t.proxy(renames["AggregationResultCountOut"]),
            "field": t.string(),
            "frequency": t.proxy(renames["AggregationResultFrequencyOut"]),
            "sum": t.proxy(renames["AggregationResultSumOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationResultOut"])
    types["PayloadFileIn"] = t.struct(
        {"name": t.string().optional(), "data": t.string().optional()}
    ).named(renames["PayloadFileIn"])
    types["PayloadFileOut"] = t.struct(
        {
            "name": t.string().optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PayloadFileOut"])
    types["DiskPartitionListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["DiskPartitionIn"])).optional()}
    ).named(renames["DiskPartitionListIn"])
    types["DiskPartitionListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["DiskPartitionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskPartitionListOut"])
    types["UploadFileInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadFileInfoIn"]
    )
    types["UploadFileInfoOut"] = t.struct(
        {
            "signedUri": t.string().optional(),
            "uriExpirationTime": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadFileInfoOut"])
    types["GoogleKubernetesEngineMigrationTargetIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleKubernetesEngineMigrationTargetIn"])
    types["GoogleKubernetesEngineMigrationTargetOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleKubernetesEngineMigrationTargetOut"])
    types["GCSPayloadInfoIn"] = t.struct(
        {"format": t.string().optional(), "path": t.string().optional()}
    ).named(renames["GCSPayloadInfoIn"])
    types["GCSPayloadInfoOut"] = t.struct(
        {
            "format": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GCSPayloadInfoOut"])
    types["ReportConfigIn"] = t.struct(
        {
            "groupPreferencesetAssignments": t.array(
                t.proxy(renames["ReportConfigGroupPreferenceSetAssignmentIn"])
            ),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["ReportConfigIn"])
    types["ReportConfigOut"] = t.struct(
        {
            "groupPreferencesetAssignments": t.array(
                t.proxy(renames["ReportConfigGroupPreferenceSetAssignmentOut"])
            ),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportConfigOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["AggregationResultHistogramBucketIn"] = t.struct(
        {
            "upperBound": t.number().optional(),
            "count": t.string().optional(),
            "lowerBound": t.number().optional(),
        }
    ).named(renames["AggregationResultHistogramBucketIn"])
    types["AggregationResultHistogramBucketOut"] = t.struct(
        {
            "upperBound": t.number().optional(),
            "count": t.string().optional(),
            "lowerBound": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationResultHistogramBucketOut"])
    types["MachineSeriesIn"] = t.struct({"code": t.string().optional()}).named(
        renames["MachineSeriesIn"]
    )
    types["MachineSeriesOut"] = t.struct(
        {
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MachineSeriesOut"])
    types["ListImportJobsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "importJobs": t.array(t.proxy(renames["ImportJobIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListImportJobsResponseIn"])
    types["ListImportJobsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "importJobs": t.array(t.proxy(renames["ImportJobOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListImportJobsResponseOut"])
    types["VmwareEnginePreferencesIn"] = t.struct(
        {
            "memoryOvercommitRatio": t.number().optional(),
            "storageDeduplicationCompressionRatio": t.number().optional(),
            "cpuOvercommitRatio": t.number().optional(),
            "commitmentPlan": t.string().optional(),
        }
    ).named(renames["VmwareEnginePreferencesIn"])
    types["VmwareEnginePreferencesOut"] = t.struct(
        {
            "memoryOvercommitRatio": t.number().optional(),
            "storageDeduplicationCompressionRatio": t.number().optional(),
            "cpuOvercommitRatio": t.number().optional(),
            "commitmentPlan": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareEnginePreferencesOut"])
    types["VirtualMachineDetailsIn"] = t.struct(
        {
            "vmName": t.string().optional(),
            "vmArchitecture": t.proxy(
                renames["VirtualMachineArchitectureDetailsIn"]
            ).optional(),
            "memoryMb": t.integer().optional(),
            "vmNetwork": t.proxy(renames["VirtualMachineNetworkDetailsIn"]).optional(),
            "platform": t.proxy(renames["PlatformDetailsIn"]).optional(),
            "coreCount": t.integer().optional(),
            "vmUuid": t.string().optional(),
            "vcenterFolder": t.string().optional(),
            "createTime": t.string().optional(),
            "osFamily": t.string().optional(),
            "osVersion": t.string().optional(),
            "guestOs": t.proxy(renames["GuestOsDetailsIn"]).optional(),
            "osName": t.string().optional(),
            "powerState": t.string().optional(),
            "vcenterVmId": t.string().optional(),
            "vcenterUrl": t.string().optional(),
            "vmDisks": t.proxy(renames["VirtualMachineDiskDetailsIn"]).optional(),
        }
    ).named(renames["VirtualMachineDetailsIn"])
    types["VirtualMachineDetailsOut"] = t.struct(
        {
            "vmName": t.string().optional(),
            "vmArchitecture": t.proxy(
                renames["VirtualMachineArchitectureDetailsOut"]
            ).optional(),
            "memoryMb": t.integer().optional(),
            "vmNetwork": t.proxy(renames["VirtualMachineNetworkDetailsOut"]).optional(),
            "platform": t.proxy(renames["PlatformDetailsOut"]).optional(),
            "coreCount": t.integer().optional(),
            "vmUuid": t.string().optional(),
            "vcenterFolder": t.string().optional(),
            "createTime": t.string().optional(),
            "osFamily": t.string().optional(),
            "osVersion": t.string().optional(),
            "guestOs": t.proxy(renames["GuestOsDetailsOut"]).optional(),
            "osName": t.string().optional(),
            "powerState": t.string().optional(),
            "vcenterVmId": t.string().optional(),
            "vcenterUrl": t.string().optional(),
            "vmDisks": t.proxy(renames["VirtualMachineDiskDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualMachineDetailsOut"])
    types["FstabEntryListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["FstabEntryIn"])).optional()}
    ).named(renames["FstabEntryListIn"])
    types["FstabEntryListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["FstabEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FstabEntryListOut"])
    types["NetworkUsageSampleIn"] = t.struct(
        {
            "averageIngressBps": t.number().optional(),
            "averageEgressBps": t.number().optional(),
        }
    ).named(renames["NetworkUsageSampleIn"])
    types["NetworkUsageSampleOut"] = t.struct(
        {
            "averageIngressBps": t.number().optional(),
            "averageEgressBps": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkUsageSampleOut"])
    types["DiskPartitionIn"] = t.struct(
        {
            "uuid": t.string().optional(),
            "fileSystem": t.string().optional(),
            "freeBytes": t.string().optional(),
            "subPartitions": t.proxy(renames["DiskPartitionListIn"]).optional(),
            "type": t.string().optional(),
            "mountPoint": t.string().optional(),
            "capacityBytes": t.string().optional(),
        }
    ).named(renames["DiskPartitionIn"])
    types["DiskPartitionOut"] = t.struct(
        {
            "uuid": t.string().optional(),
            "fileSystem": t.string().optional(),
            "freeBytes": t.string().optional(),
            "subPartitions": t.proxy(renames["DiskPartitionListOut"]).optional(),
            "type": t.string().optional(),
            "mountPoint": t.string().optional(),
            "capacityBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskPartitionOut"])
    types["SourceIn"] = t.struct(
        {
            "isManaged": t.boolean().optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "priority": t.integer().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "isManaged": t.boolean().optional(),
            "type": t.string().optional(),
            "pendingFrameCount": t.integer().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "priority": t.integer().optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "errorFrameCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["ReportSummarySoleTenantNodeAllocationIn"] = t.struct(
        {
            "node": t.proxy(renames["SoleTenantNodeTypeIn"]).optional(),
            "allocatedAssetCount": t.string().optional(),
            "nodeCount": t.string().optional(),
        }
    ).named(renames["ReportSummarySoleTenantNodeAllocationIn"])
    types["ReportSummarySoleTenantNodeAllocationOut"] = t.struct(
        {
            "node": t.proxy(renames["SoleTenantNodeTypeOut"]).optional(),
            "allocatedAssetCount": t.string().optional(),
            "nodeCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummarySoleTenantNodeAllocationOut"])
    types["ErrorFrameIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ErrorFrameIn"]
    )
    types["ErrorFrameOut"] = t.struct(
        {
            "ingestionTime": t.string().optional(),
            "name": t.string().optional(),
            "originalFrame": t.proxy(renames["AssetFrameOut"]).optional(),
            "violations": t.array(
                t.proxy(renames["FrameViolationEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorFrameOut"])
    types["ListImportDataFilesResponseIn"] = t.struct(
        {
            "importDataFiles": t.array(t.proxy(renames["ImportDataFileIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListImportDataFilesResponseIn"])
    types["ListImportDataFilesResponseOut"] = t.struct(
        {
            "importDataFiles": t.array(
                t.proxy(renames["ImportDataFileOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListImportDataFilesResponseOut"])
    types["NetworkConnectionIn"] = t.struct(
        {
            "pid": t.string().optional(),
            "protocol": t.string().optional(),
            "state": t.string().optional(),
            "localPort": t.integer().optional(),
            "processName": t.string().optional(),
            "remoteIpAddress": t.string().optional(),
            "localIpAddress": t.string().optional(),
            "remotePort": t.integer().optional(),
        }
    ).named(renames["NetworkConnectionIn"])
    types["NetworkConnectionOut"] = t.struct(
        {
            "pid": t.string().optional(),
            "protocol": t.string().optional(),
            "state": t.string().optional(),
            "localPort": t.integer().optional(),
            "processName": t.string().optional(),
            "remoteIpAddress": t.string().optional(),
            "localIpAddress": t.string().optional(),
            "remotePort": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConnectionOut"])
    types["ReportAssetFramesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReportAssetFramesResponseIn"]
    )
    types["ReportAssetFramesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReportAssetFramesResponseOut"])
    types["NetworkAddressListIn"] = t.struct(
        {"addresses": t.array(t.proxy(renames["NetworkAddressIn"])).optional()}
    ).named(renames["NetworkAddressListIn"])
    types["NetworkAddressListOut"] = t.struct(
        {
            "addresses": t.array(t.proxy(renames["NetworkAddressOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkAddressListOut"])
    types["ReportSummaryMachineFindingIn"] = t.struct(
        {
            "allocatedDiskTypes": t.array(t.string()).optional(),
            "allocatedAssetCount": t.string().optional(),
            "machineSeriesAllocations": t.array(
                t.proxy(renames["ReportSummaryMachineSeriesAllocationIn"])
            ).optional(),
            "allocatedRegions": t.array(t.string()).optional(),
        }
    ).named(renames["ReportSummaryMachineFindingIn"])
    types["ReportSummaryMachineFindingOut"] = t.struct(
        {
            "allocatedDiskTypes": t.array(t.string()).optional(),
            "allocatedAssetCount": t.string().optional(),
            "machineSeriesAllocations": t.array(
                t.proxy(renames["ReportSummaryMachineSeriesAllocationOut"])
            ).optional(),
            "allocatedRegions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryMachineFindingOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["ReportSummaryIn"] = t.struct(
        {
            "groupFindings": t.array(
                t.proxy(renames["ReportSummaryGroupFindingIn"])
            ).optional(),
            "allAssetsStats": t.proxy(
                renames["ReportSummaryAssetAggregateStatsIn"]
            ).optional(),
        }
    ).named(renames["ReportSummaryIn"])
    types["ReportSummaryOut"] = t.struct(
        {
            "groupFindings": t.array(
                t.proxy(renames["ReportSummaryGroupFindingOut"])
            ).optional(),
            "allAssetsStats": t.proxy(
                renames["ReportSummaryAssetAggregateStatsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["RuntimeNetworkInfoIn"] = t.struct(
        {
            "netstat": t.string().optional(),
            "connections": t.proxy(renames["NetworkConnectionListIn"]).optional(),
            "netstatTime": t.proxy(renames["DateTimeIn"]).optional(),
        }
    ).named(renames["RuntimeNetworkInfoIn"])
    types["RuntimeNetworkInfoOut"] = t.struct(
        {
            "netstat": t.string().optional(),
            "connections": t.proxy(renames["NetworkConnectionListOut"]).optional(),
            "netstatTime": t.proxy(renames["DateTimeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeNetworkInfoOut"])
    types["BiosDetailsIn"] = t.struct(
        {
            "smbiosUuid": t.string().optional(),
            "biosName": t.string().optional(),
            "biosVersion": t.string().optional(),
            "biosReleaseDate": t.string().optional(),
            "biosManufacturer": t.string().optional(),
        }
    ).named(renames["BiosDetailsIn"])
    types["BiosDetailsOut"] = t.struct(
        {
            "smbiosUuid": t.string().optional(),
            "biosName": t.string().optional(),
            "biosVersion": t.string().optional(),
            "biosReleaseDate": t.string().optional(),
            "biosManufacturer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BiosDetailsOut"])
    types["RunningProcessIn"] = t.struct(
        {
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "user": t.string().optional(),
            "cmdline": t.string().optional(),
            "exePath": t.string().optional(),
            "pid": t.string().optional(),
        }
    ).named(renames["RunningProcessIn"])
    types["RunningProcessOut"] = t.struct(
        {
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "user": t.string().optional(),
            "cmdline": t.string().optional(),
            "exePath": t.string().optional(),
            "pid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunningProcessOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["AggregationHistogramIn"] = t.struct(
        {"lowerBounds": t.array(t.number()).optional()}
    ).named(renames["AggregationHistogramIn"])
    types["AggregationHistogramOut"] = t.struct(
        {
            "lowerBounds": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationHistogramOut"])
    types["RunningProcessListIn"] = t.struct(
        {"processes": t.array(t.proxy(renames["RunningProcessIn"])).optional()}
    ).named(renames["RunningProcessListIn"])
    types["RunningProcessListOut"] = t.struct(
        {
            "processes": t.array(t.proxy(renames["RunningProcessOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunningProcessListOut"])
    types["InsightIn"] = t.struct({"_": t.string().optional()}).named(
        renames["InsightIn"]
    )
    types["InsightOut"] = t.struct(
        {
            "migrationInsight": t.proxy(renames["MigrationInsightOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsightOut"])
    types["ReportSummaryGroupFindingIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "preferenceSetFindings": t.array(
                t.proxy(renames["ReportSummaryGroupPreferenceSetFindingIn"])
            ).optional(),
            "assetAggregateStats": t.proxy(
                renames["ReportSummaryAssetAggregateStatsIn"]
            ).optional(),
            "overlappingAssetCount": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ReportSummaryGroupFindingIn"])
    types["ReportSummaryGroupFindingOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "preferenceSetFindings": t.array(
                t.proxy(renames["ReportSummaryGroupPreferenceSetFindingOut"])
            ).optional(),
            "assetAggregateStats": t.proxy(
                renames["ReportSummaryAssetAggregateStatsOut"]
            ).optional(),
            "overlappingAssetCount": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryGroupFindingOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "statusMessage": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["AssetPerformanceDataIn"] = t.struct(
        {
            "dailyResourceUsageAggregations": t.array(
                t.proxy(renames["DailyResourceUsageAggregationIn"])
            ).optional()
        }
    ).named(renames["AssetPerformanceDataIn"])
    types["AssetPerformanceDataOut"] = t.struct(
        {
            "dailyResourceUsageAggregations": t.array(
                t.proxy(renames["DailyResourceUsageAggregationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetPerformanceDataOut"])
    types["ComputeEngineMigrationTargetIn"] = t.struct(
        {"shape": t.proxy(renames["ComputeEngineShapeDescriptorIn"]).optional()}
    ).named(renames["ComputeEngineMigrationTargetIn"])
    types["ComputeEngineMigrationTargetOut"] = t.struct(
        {
            "shape": t.proxy(renames["ComputeEngineShapeDescriptorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeEngineMigrationTargetOut"])
    types["HostsEntryListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["HostsEntryIn"])).optional()}
    ).named(renames["HostsEntryListIn"])
    types["HostsEntryListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["HostsEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HostsEntryListOut"])
    types["SoleTenancyPreferencesIn"] = t.struct(
        {
            "hostMaintenancePolicy": t.string().optional(),
            "commitmentPlan": t.string().optional(),
            "nodeTypes": t.array(t.proxy(renames["SoleTenantNodeTypeIn"])).optional(),
            "cpuOvercommitRatio": t.number().optional(),
        }
    ).named(renames["SoleTenancyPreferencesIn"])
    types["SoleTenancyPreferencesOut"] = t.struct(
        {
            "hostMaintenancePolicy": t.string().optional(),
            "commitmentPlan": t.string().optional(),
            "nodeTypes": t.array(t.proxy(renames["SoleTenantNodeTypeOut"])).optional(),
            "cpuOvercommitRatio": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SoleTenancyPreferencesOut"])
    types["DateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["CpuUsageSampleIn"] = t.struct(
        {"utilizedPercentage": t.number().optional()}
    ).named(renames["CpuUsageSampleIn"])
    types["CpuUsageSampleOut"] = t.struct(
        {
            "utilizedPercentage": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CpuUsageSampleOut"])
    types["DateTimeIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "day": t.integer().optional(),
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
            "utcOffset": t.string().optional(),
            "timeZone": t.proxy(renames["TimeZoneIn"]).optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["DateTimeIn"])
    types["DateTimeOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "day": t.integer().optional(),
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
            "utcOffset": t.string().optional(),
            "timeZone": t.proxy(renames["TimeZoneOut"]).optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateTimeOut"])
    types["MigrationInsightIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MigrationInsightIn"]
    )
    types["MigrationInsightOut"] = t.struct(
        {
            "fit": t.proxy(renames["FitDescriptorOut"]).optional(),
            "computeEngineTarget": t.proxy(
                renames["ComputeEngineMigrationTargetOut"]
            ).optional(),
            "vmwareEngineTarget": t.proxy(
                renames["VmwareEngineMigrationTargetOut"]
            ).optional(),
            "gkeTarget": t.proxy(
                renames["GoogleKubernetesEngineMigrationTargetOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MigrationInsightOut"])
    types["MachinePreferencesIn"] = t.struct(
        {
            "allowedMachineSeries": t.array(
                t.proxy(renames["MachineSeriesIn"])
            ).optional()
        }
    ).named(renames["MachinePreferencesIn"])
    types["MachinePreferencesOut"] = t.struct(
        {
            "allowedMachineSeries": t.array(
                t.proxy(renames["MachineSeriesOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MachinePreferencesOut"])
    types["AssetIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["AssetIn"])
    types["AssetOut"] = t.struct(
        {
            "virtualMachineDetails": t.proxy(
                renames["VirtualMachineDetailsOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "sources": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "insightList": t.proxy(renames["InsightListOut"]).optional(),
            "assignedGroups": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "performanceData": t.proxy(renames["AssetPerformanceDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetOut"])
    types["VirtualMachineArchitectureDetailsIn"] = t.struct(
        {
            "vendor": t.string().optional(),
            "firmware": t.string().optional(),
            "cpuArchitecture": t.string().optional(),
            "cpuManufacturer": t.string().optional(),
            "bios": t.proxy(renames["BiosDetailsIn"]).optional(),
            "cpuName": t.string().optional(),
            "cpuThreadCount": t.integer().optional(),
            "cpuSocketCount": t.integer().optional(),
            "hyperthreading": t.string().optional(),
        }
    ).named(renames["VirtualMachineArchitectureDetailsIn"])
    types["VirtualMachineArchitectureDetailsOut"] = t.struct(
        {
            "vendor": t.string().optional(),
            "firmware": t.string().optional(),
            "cpuArchitecture": t.string().optional(),
            "cpuManufacturer": t.string().optional(),
            "bios": t.proxy(renames["BiosDetailsOut"]).optional(),
            "cpuName": t.string().optional(),
            "cpuThreadCount": t.integer().optional(),
            "cpuSocketCount": t.integer().optional(),
            "hyperthreading": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualMachineArchitectureDetailsOut"])
    types["ReportSummaryChartDataDataPointIn"] = t.struct(
        {"label": t.string().optional(), "value": t.number().optional()}
    ).named(renames["ReportSummaryChartDataDataPointIn"])
    types["ReportSummaryChartDataDataPointOut"] = t.struct(
        {
            "label": t.string().optional(),
            "value": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryChartDataDataPointOut"])
    types["VmwareDiskConfigIn"] = t.struct(
        {
            "shared": t.boolean().optional(),
            "vmdkDiskMode": t.string().optional(),
            "rdmCompatibilityMode": t.string().optional(),
            "backingType": t.string().optional(),
        }
    ).named(renames["VmwareDiskConfigIn"])
    types["VmwareDiskConfigOut"] = t.struct(
        {
            "shared": t.boolean().optional(),
            "vmdkDiskMode": t.string().optional(),
            "rdmCompatibilityMode": t.string().optional(),
            "backingType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareDiskConfigOut"])
    types["ListReportConfigsResponseIn"] = t.struct(
        {
            "reportConfigs": t.array(t.proxy(renames["ReportConfigIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListReportConfigsResponseIn"])
    types["ListReportConfigsResponseOut"] = t.struct(
        {
            "reportConfigs": t.array(t.proxy(renames["ReportConfigOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReportConfigsResponseOut"])
    types["RegionPreferencesIn"] = t.struct(
        {"preferredRegions": t.array(t.string()).optional()}
    ).named(renames["RegionPreferencesIn"])
    types["RegionPreferencesOut"] = t.struct(
        {
            "preferredRegions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionPreferencesOut"])
    types["VirtualMachineDiskDetailsIn"] = t.struct(
        {
            "lsblkJson": t.string().optional(),
            "hddTotalCapacityBytes": t.string().optional(),
            "disks": t.proxy(renames["DiskEntryListIn"]).optional(),
            "hddTotalFreeBytes": t.string().optional(),
        }
    ).named(renames["VirtualMachineDiskDetailsIn"])
    types["VirtualMachineDiskDetailsOut"] = t.struct(
        {
            "lsblkJson": t.string().optional(),
            "hddTotalCapacityBytes": t.string().optional(),
            "disks": t.proxy(renames["DiskEntryListOut"]).optional(),
            "hddTotalFreeBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualMachineDiskDetailsOut"])
    types["SettingsIn"] = t.struct({"preferenceSet": t.string().optional()}).named(
        renames["SettingsIn"]
    )
    types["SettingsOut"] = t.struct(
        {
            "name": t.string().optional(),
            "preferenceSet": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettingsOut"])
    types["ReportSummarySoleTenantFindingIn"] = t.struct(
        {
            "allocatedAssetCount": t.string().optional(),
            "nodeAllocations": t.array(
                t.proxy(renames["ReportSummarySoleTenantNodeAllocationIn"])
            ).optional(),
            "allocatedRegions": t.array(t.string()).optional(),
        }
    ).named(renames["ReportSummarySoleTenantFindingIn"])
    types["ReportSummarySoleTenantFindingOut"] = t.struct(
        {
            "allocatedAssetCount": t.string().optional(),
            "nodeAllocations": t.array(
                t.proxy(renames["ReportSummarySoleTenantNodeAllocationOut"])
            ).optional(),
            "allocatedRegions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummarySoleTenantFindingOut"])
    types["DailyResourceUsageAggregationCPUIn"] = t.struct(
        {
            "utilizationPercentage": t.proxy(
                renames["DailyResourceUsageAggregationStatsIn"]
            ).optional()
        }
    ).named(renames["DailyResourceUsageAggregationCPUIn"])
    types["DailyResourceUsageAggregationCPUOut"] = t.struct(
        {
            "utilizationPercentage": t.proxy(
                renames["DailyResourceUsageAggregationStatsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DailyResourceUsageAggregationCPUOut"])
    types["AggregationIn"] = t.struct(
        {
            "sum": t.proxy(renames["AggregationSumIn"]).optional(),
            "count": t.proxy(renames["AggregationCountIn"]).optional(),
            "frequency": t.proxy(renames["AggregationFrequencyIn"]).optional(),
            "histogram": t.proxy(renames["AggregationHistogramIn"]).optional(),
            "field": t.string().optional(),
        }
    ).named(renames["AggregationIn"])
    types["AggregationOut"] = t.struct(
        {
            "sum": t.proxy(renames["AggregationSumOut"]).optional(),
            "count": t.proxy(renames["AggregationCountOut"]).optional(),
            "frequency": t.proxy(renames["AggregationFrequencyOut"]).optional(),
            "histogram": t.proxy(renames["AggregationHistogramOut"]).optional(),
            "field": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationOut"])
    types["NfsExportIn"] = t.struct(
        {
            "exportDirectory": t.string().optional(),
            "hosts": t.array(t.string()).optional(),
        }
    ).named(renames["NfsExportIn"])
    types["NfsExportOut"] = t.struct(
        {
            "exportDirectory": t.string().optional(),
            "hosts": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NfsExportOut"])
    types["NetworkAdapterDetailsIn"] = t.struct(
        {
            "adapterType": t.string().optional(),
            "addresses": t.proxy(renames["NetworkAddressListIn"]).optional(),
            "macAddress": t.string().optional(),
        }
    ).named(renames["NetworkAdapterDetailsIn"])
    types["NetworkAdapterDetailsOut"] = t.struct(
        {
            "adapterType": t.string().optional(),
            "addresses": t.proxy(renames["NetworkAddressListOut"]).optional(),
            "macAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkAdapterDetailsOut"])
    types["ReportSummaryMachineSeriesAllocationIn"] = t.struct(
        {
            "allocatedAssetCount": t.string().optional(),
            "machineSeries": t.proxy(renames["MachineSeriesIn"]).optional(),
        }
    ).named(renames["ReportSummaryMachineSeriesAllocationIn"])
    types["ReportSummaryMachineSeriesAllocationOut"] = t.struct(
        {
            "allocatedAssetCount": t.string().optional(),
            "machineSeries": t.proxy(renames["MachineSeriesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryMachineSeriesAllocationOut"])
    types["ReportConfigGroupPreferenceSetAssignmentIn"] = t.struct(
        {"preferenceSet": t.string(), "group": t.string()}
    ).named(renames["ReportConfigGroupPreferenceSetAssignmentIn"])
    types["ReportConfigGroupPreferenceSetAssignmentOut"] = t.struct(
        {
            "preferenceSet": t.string(),
            "group": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportConfigGroupPreferenceSetAssignmentOut"])
    types["GuestOsDetailsIn"] = t.struct(
        {
            "runtime": t.proxy(renames["GuestRuntimeDetailsIn"]).optional(),
            "config": t.proxy(renames["GuestConfigDetailsIn"]).optional(),
        }
    ).named(renames["GuestOsDetailsIn"])
    types["GuestOsDetailsOut"] = t.struct(
        {
            "runtime": t.proxy(renames["GuestRuntimeDetailsOut"]).optional(),
            "config": t.proxy(renames["GuestConfigDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestOsDetailsOut"])
    types["BatchUpdateAssetsRequestIn"] = t.struct(
        {"requests": t.array(t.proxy(renames["UpdateAssetRequestIn"]))}
    ).named(renames["BatchUpdateAssetsRequestIn"])
    types["BatchUpdateAssetsRequestOut"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["UpdateAssetRequestOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateAssetsRequestOut"])
    types["DailyResourceUsageAggregationStatsIn"] = t.struct(
        {
            "ninteyFifthPercentile": t.number().optional(),
            "peak": t.number().optional(),
            "median": t.number().optional(),
            "average": t.number().optional(),
        }
    ).named(renames["DailyResourceUsageAggregationStatsIn"])
    types["DailyResourceUsageAggregationStatsOut"] = t.struct(
        {
            "ninteyFifthPercentile": t.number().optional(),
            "peak": t.number().optional(),
            "median": t.number().optional(),
            "average": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DailyResourceUsageAggregationStatsOut"])
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["NfsExportListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["NfsExportIn"])).optional()}
    ).named(renames["NfsExportListIn"])
    types["NfsExportListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["NfsExportOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NfsExportListOut"])
    types["BatchUpdateAssetsResponseIn"] = t.struct(
        {"assets": t.array(t.proxy(renames["AssetIn"])).optional()}
    ).named(renames["BatchUpdateAssetsResponseIn"])
    types["BatchUpdateAssetsResponseOut"] = t.struct(
        {
            "assets": t.array(t.proxy(renames["AssetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateAssetsResponseOut"])
    types["MemoryUsageSampleIn"] = t.struct(
        {"utilizedPercentage": t.number().optional()}
    ).named(renames["MemoryUsageSampleIn"])
    types["MemoryUsageSampleOut"] = t.struct(
        {
            "utilizedPercentage": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemoryUsageSampleOut"])
    types["AggregationResultHistogramIn"] = t.struct(
        {
            "buckets": t.array(
                t.proxy(renames["AggregationResultHistogramBucketIn"])
            ).optional()
        }
    ).named(renames["AggregationResultHistogramIn"])
    types["AggregationResultHistogramOut"] = t.struct(
        {
            "buckets": t.array(
                t.proxy(renames["AggregationResultHistogramBucketOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationResultHistogramOut"])
    types["GroupIn"] = t.struct(
        {
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
    types["ListPreferenceSetsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "preferenceSets": t.array(t.proxy(renames["PreferenceSetIn"])).optional(),
        }
    ).named(renames["ListPreferenceSetsResponseIn"])
    types["ListPreferenceSetsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "preferenceSets": t.array(t.proxy(renames["PreferenceSetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPreferenceSetsResponseOut"])
    types["PreferenceSetIn"] = t.struct(
        {
            "virtualMachinePreferences": t.proxy(
                renames["VirtualMachinePreferencesIn"]
            ).optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["PreferenceSetIn"])
    types["PreferenceSetOut"] = t.struct(
        {
            "virtualMachinePreferences": t.proxy(
                renames["VirtualMachinePreferencesOut"]
            ).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PreferenceSetOut"])
    types["RunImportJobRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["RunImportJobRequestIn"])
    types["RunImportJobRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunImportJobRequestOut"])
    types["FileValidationReportIn"] = t.struct(
        {
            "rowErrors": t.array(t.proxy(renames["ImportRowErrorIn"])).optional(),
            "fileErrors": t.array(t.proxy(renames["ImportErrorIn"])).optional(),
            "partialReport": t.boolean().optional(),
            "fileName": t.string().optional(),
        }
    ).named(renames["FileValidationReportIn"])
    types["FileValidationReportOut"] = t.struct(
        {
            "rowErrors": t.array(t.proxy(renames["ImportRowErrorOut"])).optional(),
            "fileErrors": t.array(t.proxy(renames["ImportErrorOut"])).optional(),
            "partialReport": t.boolean().optional(),
            "fileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileValidationReportOut"])
    types["ValidationReportIn"] = t.struct(
        {
            "jobErrors": t.array(t.proxy(renames["ImportErrorIn"])).optional(),
            "fileValidations": t.array(
                t.proxy(renames["FileValidationReportIn"])
            ).optional(),
        }
    ).named(renames["ValidationReportIn"])
    types["ValidationReportOut"] = t.struct(
        {
            "jobErrors": t.array(t.proxy(renames["ImportErrorOut"])).optional(),
            "fileValidations": t.array(
                t.proxy(renames["FileValidationReportOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationReportOut"])
    types["AddAssetsToGroupRequestIn"] = t.struct(
        {
            "assets": t.proxy(renames["AssetListIn"]),
            "allowExisting": t.boolean().optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["AddAssetsToGroupRequestIn"])
    types["AddAssetsToGroupRequestOut"] = t.struct(
        {
            "assets": t.proxy(renames["AssetListOut"]),
            "allowExisting": t.boolean().optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddAssetsToGroupRequestOut"])
    types["AggregationFrequencyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AggregationFrequencyIn"]
    )
    types["AggregationFrequencyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AggregationFrequencyOut"])
    types["NetworkAdapterListIn"] = t.struct(
        {
            "networkAdapters": t.array(
                t.proxy(renames["NetworkAdapterDetailsIn"])
            ).optional()
        }
    ).named(renames["NetworkAdapterListIn"])
    types["NetworkAdapterListOut"] = t.struct(
        {
            "networkAdapters": t.array(
                t.proxy(renames["NetworkAdapterDetailsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkAdapterListOut"])
    types["VirtualMachineNetworkDetailsIn"] = t.struct(
        {
            "networkAdapters": t.proxy(renames["NetworkAdapterListIn"]).optional(),
            "primaryMacAddress": t.string().optional(),
            "publicIpAddress": t.string().optional(),
            "defaultGw": t.string().optional(),
            "primaryIpAddress": t.string().optional(),
        }
    ).named(renames["VirtualMachineNetworkDetailsIn"])
    types["VirtualMachineNetworkDetailsOut"] = t.struct(
        {
            "networkAdapters": t.proxy(renames["NetworkAdapterListOut"]).optional(),
            "primaryMacAddress": t.string().optional(),
            "publicIpAddress": t.string().optional(),
            "defaultGw": t.string().optional(),
            "primaryIpAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualMachineNetworkDetailsOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["BatchDeleteAssetsRequestIn"] = t.struct(
        {"names": t.array(t.string()), "allowMissing": t.boolean().optional()}
    ).named(renames["BatchDeleteAssetsRequestIn"])
    types["BatchDeleteAssetsRequestOut"] = t.struct(
        {
            "names": t.array(t.string()),
            "allowMissing": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeleteAssetsRequestOut"])
    types["AggregateAssetsValuesResponseIn"] = t.struct(
        {"results": t.array(t.proxy(renames["AggregationResultIn"])).optional()}
    ).named(renames["AggregateAssetsValuesResponseIn"])
    types["AggregateAssetsValuesResponseOut"] = t.struct(
        {
            "results": t.array(t.proxy(renames["AggregationResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregateAssetsValuesResponseOut"])
    types["ValidateImportJobRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["ValidateImportJobRequestIn"])
    types["ValidateImportJobRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateImportJobRequestOut"])
    types["DailyResourceUsageAggregationDiskIn"] = t.struct(
        {"iops": t.proxy(renames["DailyResourceUsageAggregationStatsIn"]).optional()}
    ).named(renames["DailyResourceUsageAggregationDiskIn"])
    types["DailyResourceUsageAggregationDiskOut"] = t.struct(
        {
            "iops": t.proxy(
                renames["DailyResourceUsageAggregationStatsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DailyResourceUsageAggregationDiskOut"])
    types["ListErrorFramesResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "errorFrames": t.array(t.proxy(renames["ErrorFrameIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListErrorFramesResponseIn"])
    types["ListErrorFramesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "errorFrames": t.array(t.proxy(renames["ErrorFrameOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListErrorFramesResponseOut"])
    types["ImportDataFileIn"] = t.struct(
        {
            "format": t.string(),
            "displayName": t.string().optional(),
            "uploadFileInfo": t.proxy(renames["UploadFileInfoIn"]).optional(),
        }
    ).named(renames["ImportDataFileIn"])
    types["ImportDataFileOut"] = t.struct(
        {
            "format": t.string(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "uploadFileInfo": t.proxy(renames["UploadFileInfoOut"]).optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportDataFileOut"])
    types["VirtualMachinePreferencesIn"] = t.struct(
        {
            "vmwareEnginePreferences": t.proxy(
                renames["VmwareEnginePreferencesIn"]
            ).optional(),
            "sizingOptimizationStrategy": t.string().optional(),
            "computeEnginePreferences": t.proxy(
                renames["ComputeEnginePreferencesIn"]
            ).optional(),
            "regionPreferences": t.proxy(renames["RegionPreferencesIn"]).optional(),
            "soleTenancyPreferences": t.proxy(
                renames["SoleTenancyPreferencesIn"]
            ).optional(),
            "commitmentPlan": t.string().optional(),
            "targetProduct": t.string().optional(),
        }
    ).named(renames["VirtualMachinePreferencesIn"])
    types["VirtualMachinePreferencesOut"] = t.struct(
        {
            "vmwareEnginePreferences": t.proxy(
                renames["VmwareEnginePreferencesOut"]
            ).optional(),
            "sizingOptimizationStrategy": t.string().optional(),
            "computeEnginePreferences": t.proxy(
                renames["ComputeEnginePreferencesOut"]
            ).optional(),
            "regionPreferences": t.proxy(renames["RegionPreferencesOut"]).optional(),
            "soleTenancyPreferences": t.proxy(
                renames["SoleTenancyPreferencesOut"]
            ).optional(),
            "commitmentPlan": t.string().optional(),
            "targetProduct": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualMachinePreferencesOut"])
    types["ReportSummaryVMWareNodeAllocationIn"] = t.struct(
        {
            "allocatedAssetCount": t.string().optional(),
            "nodeCount": t.string().optional(),
            "vmwareNode": t.proxy(renames["ReportSummaryVMWareNodeIn"]).optional(),
        }
    ).named(renames["ReportSummaryVMWareNodeAllocationIn"])
    types["ReportSummaryVMWareNodeAllocationOut"] = t.struct(
        {
            "allocatedAssetCount": t.string().optional(),
            "nodeCount": t.string().optional(),
            "vmwareNode": t.proxy(renames["ReportSummaryVMWareNodeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryVMWareNodeAllocationOut"])
    types["FitDescriptorIn"] = t.struct({"fitLevel": t.string().optional()}).named(
        renames["FitDescriptorIn"]
    )
    types["FitDescriptorOut"] = t.struct(
        {
            "fitLevel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FitDescriptorOut"])
    types["AggregateAssetsValuesRequestIn"] = t.struct(
        {
            "aggregations": t.array(t.proxy(renames["AggregationIn"])).optional(),
            "filter": t.string().optional(),
        }
    ).named(renames["AggregateAssetsValuesRequestIn"])
    types["AggregateAssetsValuesRequestOut"] = t.struct(
        {
            "aggregations": t.array(t.proxy(renames["AggregationOut"])).optional(),
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregateAssetsValuesRequestOut"])
    types["VmwareEngineMigrationTargetIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["VmwareEngineMigrationTargetIn"])
    types["VmwareEngineMigrationTargetOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VmwareEngineMigrationTargetOut"])
    types["TimeZoneIn"] = t.struct(
        {"version": t.string().optional(), "id": t.string().optional()}
    ).named(renames["TimeZoneIn"])
    types["TimeZoneOut"] = t.struct(
        {
            "version": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeZoneOut"])
    types["RemoveAssetsFromGroupRequestIn"] = t.struct(
        {
            "requestId": t.string().optional(),
            "allowMissing": t.boolean().optional(),
            "assets": t.proxy(renames["AssetListIn"]),
        }
    ).named(renames["RemoveAssetsFromGroupRequestIn"])
    types["RemoveAssetsFromGroupRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "allowMissing": t.boolean().optional(),
            "assets": t.proxy(renames["AssetListOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveAssetsFromGroupRequestOut"])
    types["NetworkAddressIn"] = t.struct(
        {
            "bcast": t.string().optional(),
            "subnetMask": t.string().optional(),
            "assignment": t.string().optional(),
            "fqdn": t.string().optional(),
            "ipAddress": t.string().optional(),
        }
    ).named(renames["NetworkAddressIn"])
    types["NetworkAddressOut"] = t.struct(
        {
            "bcast": t.string().optional(),
            "subnetMask": t.string().optional(),
            "assignment": t.string().optional(),
            "fqdn": t.string().optional(),
            "ipAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkAddressOut"])
    types["ReportSummaryHistogramChartDataIn"] = t.struct(
        {
            "buckets": t.array(
                t.proxy(renames["ReportSummaryHistogramChartDataBucketIn"])
            ).optional()
        }
    ).named(renames["ReportSummaryHistogramChartDataIn"])
    types["ReportSummaryHistogramChartDataOut"] = t.struct(
        {
            "buckets": t.array(
                t.proxy(renames["ReportSummaryHistogramChartDataBucketOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryHistogramChartDataOut"])
    types["ImportErrorIn"] = t.struct(
        {"severity": t.string().optional(), "errorDetails": t.string().optional()}
    ).named(renames["ImportErrorIn"])
    types["ImportErrorOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "errorDetails": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportErrorOut"])
    types["DailyResourceUsageAggregationMemoryIn"] = t.struct(
        {
            "utilizationPercentage": t.proxy(
                renames["DailyResourceUsageAggregationStatsIn"]
            ).optional()
        }
    ).named(renames["DailyResourceUsageAggregationMemoryIn"])
    types["DailyResourceUsageAggregationMemoryOut"] = t.struct(
        {
            "utilizationPercentage": t.proxy(
                renames["DailyResourceUsageAggregationStatsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DailyResourceUsageAggregationMemoryOut"])
    types["PhysicalPlatformDetailsIn"] = t.struct(
        {"location": t.string().optional()}
    ).named(renames["PhysicalPlatformDetailsIn"])
    types["PhysicalPlatformDetailsOut"] = t.struct(
        {
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhysicalPlatformDetailsOut"])
    types["AggregationResultSumIn"] = t.struct({"value": t.number()}).named(
        renames["AggregationResultSumIn"]
    )
    types["AggregationResultSumOut"] = t.struct(
        {"value": t.number(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AggregationResultSumOut"])
    types["ReportSummaryUtilizationChartDataIn"] = t.struct(
        {"free": t.string().optional(), "used": t.string().optional()}
    ).named(renames["ReportSummaryUtilizationChartDataIn"])
    types["ReportSummaryUtilizationChartDataOut"] = t.struct(
        {
            "free": t.string().optional(),
            "used": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryUtilizationChartDataOut"])
    types["FrameViolationEntryIn"] = t.struct(
        {"field": t.string().optional(), "violation": t.string().optional()}
    ).named(renames["FrameViolationEntryIn"])
    types["FrameViolationEntryOut"] = t.struct(
        {
            "field": t.string().optional(),
            "violation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FrameViolationEntryOut"])
    types["PlatformDetailsIn"] = t.struct(
        {
            "genericDetails": t.proxy(renames["GenericPlatformDetailsIn"]).optional(),
            "azureVmDetails": t.proxy(renames["AzureVmPlatformDetailsIn"]).optional(),
            "vmwareDetails": t.proxy(renames["VmwarePlatformDetailsIn"]).optional(),
            "awsEc2Details": t.proxy(renames["AwsEc2PlatformDetailsIn"]).optional(),
            "physicalDetails": t.proxy(renames["PhysicalPlatformDetailsIn"]).optional(),
        }
    ).named(renames["PlatformDetailsIn"])
    types["PlatformDetailsOut"] = t.struct(
        {
            "genericDetails": t.proxy(renames["GenericPlatformDetailsOut"]).optional(),
            "azureVmDetails": t.proxy(renames["AzureVmPlatformDetailsOut"]).optional(),
            "vmwareDetails": t.proxy(renames["VmwarePlatformDetailsOut"]).optional(),
            "awsEc2Details": t.proxy(renames["AwsEc2PlatformDetailsOut"]).optional(),
            "physicalDetails": t.proxy(
                renames["PhysicalPlatformDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlatformDetailsOut"])
    types["ImportJobIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "assetSource": t.string(),
            "inlinePayload": t.proxy(renames["InlinePayloadInfoIn"]).optional(),
            "gcsPayload": t.proxy(renames["GCSPayloadInfoIn"]).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["ImportJobIn"])
    types["ImportJobOut"] = t.struct(
        {
            "executionReport": t.proxy(renames["ExecutionReportOut"]).optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "validationReport": t.proxy(renames["ValidationReportOut"]).optional(),
            "createTime": t.string().optional(),
            "assetSource": t.string(),
            "inlinePayload": t.proxy(renames["InlinePayloadInfoOut"]).optional(),
            "completeTime": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "gcsPayload": t.proxy(renames["GCSPayloadInfoOut"]).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportJobOut"])
    types["AzureVmPlatformDetailsIn"] = t.struct(
        {
            "provisioningState": t.string().optional(),
            "machineTypeLabel": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["AzureVmPlatformDetailsIn"])
    types["AzureVmPlatformDetailsOut"] = t.struct(
        {
            "provisioningState": t.string().optional(),
            "machineTypeLabel": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AzureVmPlatformDetailsOut"])
    types["ListGroupsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "groups": t.array(t.proxy(renames["GroupIn"])).optional(),
        }
    ).named(renames["ListGroupsResponseIn"])
    types["ListGroupsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "groups": t.array(t.proxy(renames["GroupOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGroupsResponseOut"])
    types["ReportIn"] = t.struct(
        {
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["ReportIn"])
    types["ReportOut"] = t.struct(
        {
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "createTime": t.string().optional(),
            "summary": t.proxy(renames["ReportSummaryOut"]).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportOut"])
    types["DiskUsageSampleIn"] = t.struct({"averageIops": t.number().optional()}).named(
        renames["DiskUsageSampleIn"]
    )
    types["DiskUsageSampleOut"] = t.struct(
        {
            "averageIops": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskUsageSampleOut"])
    types["ReportSummaryVMWareEngineFindingIn"] = t.struct(
        {
            "allocatedRegions": t.array(t.string()).optional(),
            "nodeAllocations": t.array(
                t.proxy(renames["ReportSummaryVMWareNodeAllocationIn"])
            ).optional(),
            "allocatedAssetCount": t.string().optional(),
        }
    ).named(renames["ReportSummaryVMWareEngineFindingIn"])
    types["ReportSummaryVMWareEngineFindingOut"] = t.struct(
        {
            "allocatedRegions": t.array(t.string()).optional(),
            "nodeAllocations": t.array(
                t.proxy(renames["ReportSummaryVMWareNodeAllocationOut"])
            ).optional(),
            "allocatedAssetCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryVMWareEngineFindingOut"])
    types["DiskEntryListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["DiskEntryIn"])).optional()}
    ).named(renames["DiskEntryListIn"])
    types["DiskEntryListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["DiskEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskEntryListOut"])
    types["SoleTenantNodeTypeIn"] = t.struct({"nodeName": t.string().optional()}).named(
        renames["SoleTenantNodeTypeIn"]
    )
    types["SoleTenantNodeTypeOut"] = t.struct(
        {
            "nodeName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SoleTenantNodeTypeOut"])
    types["GuestInstalledApplicationListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["GuestInstalledApplicationIn"])).optional()}
    ).named(renames["GuestInstalledApplicationListIn"])
    types["GuestInstalledApplicationListOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["GuestInstalledApplicationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestInstalledApplicationListOut"])
    types["ComputeEnginePreferencesIn"] = t.struct(
        {
            "machinePreferences": t.proxy(renames["MachinePreferencesIn"]).optional(),
            "persistentDiskType": t.string().optional(),
            "licenseType": t.string().optional(),
        }
    ).named(renames["ComputeEnginePreferencesIn"])
    types["ComputeEnginePreferencesOut"] = t.struct(
        {
            "machinePreferences": t.proxy(renames["MachinePreferencesOut"]).optional(),
            "persistentDiskType": t.string().optional(),
            "licenseType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeEnginePreferencesOut"])
    types["UpdateAssetRequestIn"] = t.struct(
        {
            "asset": t.proxy(renames["AssetIn"]),
            "requestId": t.string().optional(),
            "updateMask": t.string(),
        }
    ).named(renames["UpdateAssetRequestIn"])
    types["UpdateAssetRequestOut"] = t.struct(
        {
            "asset": t.proxy(renames["AssetOut"]),
            "requestId": t.string().optional(),
            "updateMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateAssetRequestOut"])
    types["ComputeStorageDescriptorIn"] = t.struct(
        {"type": t.string().optional(), "sizeGb": t.integer().optional()}
    ).named(renames["ComputeStorageDescriptorIn"])
    types["ComputeStorageDescriptorOut"] = t.struct(
        {
            "type": t.string().optional(),
            "sizeGb": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeStorageDescriptorOut"])
    types["ReportSummaryVMWareNodeIn"] = t.struct(
        {"code": t.string().optional()}
    ).named(renames["ReportSummaryVMWareNodeIn"])
    types["ReportSummaryVMWareNodeOut"] = t.struct(
        {
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryVMWareNodeOut"])
    types["AssetListIn"] = t.struct({"assetIds": t.array(t.string())}).named(
        renames["AssetListIn"]
    )
    types["AssetListOut"] = t.struct(
        {
            "assetIds": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetListOut"])
    types["RunningServiceIn"] = t.struct(
        {
            "cmdline": t.string().optional(),
            "state": t.string().optional(),
            "status": t.string().optional(),
            "exePath": t.string().optional(),
            "name": t.string().optional(),
            "pid": t.string().optional(),
            "startMode": t.string().optional(),
        }
    ).named(renames["RunningServiceIn"])
    types["RunningServiceOut"] = t.struct(
        {
            "cmdline": t.string().optional(),
            "state": t.string().optional(),
            "status": t.string().optional(),
            "exePath": t.string().optional(),
            "name": t.string().optional(),
            "pid": t.string().optional(),
            "startMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunningServiceOut"])
    types["FramesIn"] = t.struct(
        {"framesData": t.array(t.proxy(renames["AssetFrameIn"])).optional()}
    ).named(renames["FramesIn"])
    types["FramesOut"] = t.struct(
        {
            "framesData": t.array(t.proxy(renames["AssetFrameOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FramesOut"])
    types["ExecutionReportIn"] = t.struct(
        {
            "executionErrors": t.proxy(renames["ValidationReportIn"]).optional(),
            "jobErrors": t.array(t.proxy(renames["ImportErrorIn"])).optional(),
            "framesReported": t.integer().optional(),
            "totalRowsCount": t.integer().optional(),
        }
    ).named(renames["ExecutionReportIn"])
    types["ExecutionReportOut"] = t.struct(
        {
            "executionErrors": t.proxy(renames["ValidationReportOut"]).optional(),
            "jobErrors": t.array(t.proxy(renames["ImportErrorOut"])).optional(),
            "framesReported": t.integer().optional(),
            "totalRowsCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionReportOut"])
    types["SelinuxIn"] = t.struct(
        {"enabled": t.boolean().optional(), "mode": t.string().optional()}
    ).named(renames["SelinuxIn"])
    types["SelinuxOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "mode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SelinuxOut"])
    types["ReportSummaryChartDataIn"] = t.struct(
        {
            "dataPoints": t.array(
                t.proxy(renames["ReportSummaryChartDataDataPointIn"])
            ).optional()
        }
    ).named(renames["ReportSummaryChartDataIn"])
    types["ReportSummaryChartDataOut"] = t.struct(
        {
            "dataPoints": t.array(
                t.proxy(renames["ReportSummaryChartDataDataPointOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryChartDataOut"])
    types["OpenFileDetailsIn"] = t.struct(
        {
            "command": t.string().optional(),
            "user": t.string().optional(),
            "filePath": t.string().optional(),
            "fileType": t.string().optional(),
        }
    ).named(renames["OpenFileDetailsIn"])
    types["OpenFileDetailsOut"] = t.struct(
        {
            "command": t.string().optional(),
            "user": t.string().optional(),
            "filePath": t.string().optional(),
            "fileType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OpenFileDetailsOut"])
    types["GenericPlatformDetailsIn"] = t.struct(
        {"location": t.string().optional()}
    ).named(renames["GenericPlatformDetailsIn"])
    types["GenericPlatformDetailsOut"] = t.struct(
        {
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenericPlatformDetailsOut"])
    types["InlinePayloadInfoIn"] = t.struct(
        {
            "format": t.string().optional(),
            "payload": t.array(t.proxy(renames["PayloadFileIn"])).optional(),
        }
    ).named(renames["InlinePayloadInfoIn"])
    types["InlinePayloadInfoOut"] = t.struct(
        {
            "format": t.string().optional(),
            "payload": t.array(t.proxy(renames["PayloadFileOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InlinePayloadInfoOut"])
    types["GuestRuntimeDetailsIn"] = t.struct(
        {
            "services": t.proxy(renames["RunningServiceListIn"]).optional(),
            "lastUptime": t.proxy(renames["DateIn"]).optional(),
            "machineName": t.string().optional(),
            "domain": t.string().optional(),
            "openFileList": t.proxy(renames["OpenFileListIn"]).optional(),
            "networkInfo": t.proxy(renames["RuntimeNetworkInfoIn"]).optional(),
            "installedApps": t.proxy(
                renames["GuestInstalledApplicationListIn"]
            ).optional(),
            "processes": t.proxy(renames["RunningProcessListIn"]).optional(),
        }
    ).named(renames["GuestRuntimeDetailsIn"])
    types["GuestRuntimeDetailsOut"] = t.struct(
        {
            "services": t.proxy(renames["RunningServiceListOut"]).optional(),
            "lastUptime": t.proxy(renames["DateOut"]).optional(),
            "machineName": t.string().optional(),
            "domain": t.string().optional(),
            "openFileList": t.proxy(renames["OpenFileListOut"]).optional(),
            "networkInfo": t.proxy(renames["RuntimeNetworkInfoOut"]).optional(),
            "installedApps": t.proxy(
                renames["GuestInstalledApplicationListOut"]
            ).optional(),
            "processes": t.proxy(renames["RunningProcessListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestRuntimeDetailsOut"])
    types["ListSourcesResponseIn"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["SourceIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListSourcesResponseIn"])
    types["ListSourcesResponseOut"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSourcesResponseOut"])
    types["AggregationResultCountIn"] = t.struct({"value": t.string()}).named(
        renames["AggregationResultCountIn"]
    )
    types["AggregationResultCountOut"] = t.struct(
        {"value": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AggregationResultCountOut"])
    types["PerformanceSampleIn"] = t.struct(
        {
            "network": t.proxy(renames["NetworkUsageSampleIn"]).optional(),
            "sampleTime": t.string(),
            "memory": t.proxy(renames["MemoryUsageSampleIn"]).optional(),
            "disk": t.proxy(renames["DiskUsageSampleIn"]).optional(),
            "cpu": t.proxy(renames["CpuUsageSampleIn"]).optional(),
        }
    ).named(renames["PerformanceSampleIn"])
    types["PerformanceSampleOut"] = t.struct(
        {
            "network": t.proxy(renames["NetworkUsageSampleOut"]).optional(),
            "sampleTime": t.string(),
            "memory": t.proxy(renames["MemoryUsageSampleOut"]).optional(),
            "disk": t.proxy(renames["DiskUsageSampleOut"]).optional(),
            "cpu": t.proxy(renames["CpuUsageSampleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerformanceSampleOut"])
    types["FstabEntryIn"] = t.struct(
        {
            "vfstype": t.string().optional(),
            "freq": t.integer().optional(),
            "mntops": t.string().optional(),
            "passno": t.integer().optional(),
            "spec": t.string().optional(),
            "file": t.string().optional(),
        }
    ).named(renames["FstabEntryIn"])
    types["FstabEntryOut"] = t.struct(
        {
            "vfstype": t.string().optional(),
            "freq": t.integer().optional(),
            "mntops": t.string().optional(),
            "passno": t.integer().optional(),
            "spec": t.string().optional(),
            "file": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FstabEntryOut"])
    types["DailyResourceUsageAggregationNetworkIn"] = t.struct(
        {
            "egressBps": t.proxy(
                renames["DailyResourceUsageAggregationStatsIn"]
            ).optional(),
            "ingressBps": t.proxy(
                renames["DailyResourceUsageAggregationStatsIn"]
            ).optional(),
        }
    ).named(renames["DailyResourceUsageAggregationNetworkIn"])
    types["DailyResourceUsageAggregationNetworkOut"] = t.struct(
        {
            "egressBps": t.proxy(
                renames["DailyResourceUsageAggregationStatsOut"]
            ).optional(),
            "ingressBps": t.proxy(
                renames["DailyResourceUsageAggregationStatsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DailyResourceUsageAggregationNetworkOut"])
    types["ListReportsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "reports": t.array(t.proxy(renames["ReportIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListReportsResponseIn"])
    types["ListReportsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "reports": t.array(t.proxy(renames["ReportOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReportsResponseOut"])

    functions = {}
    functions["projectsLocationsUpdateSettings"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGetSettings"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPreferenceSetsCreate"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["PreferenceSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPreferenceSetsDelete"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["PreferenceSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPreferenceSetsList"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["PreferenceSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPreferenceSetsPatch"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["PreferenceSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPreferenceSetsGet"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["PreferenceSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImportJobsValidate"] = migrationcenter.post(
        "v1alpha1/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImportJobsGet"] = migrationcenter.post(
        "v1alpha1/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImportJobsDelete"] = migrationcenter.post(
        "v1alpha1/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImportJobsList"] = migrationcenter.post(
        "v1alpha1/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImportJobsCreate"] = migrationcenter.post(
        "v1alpha1/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImportJobsPatch"] = migrationcenter.post(
        "v1alpha1/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImportJobsRun"] = migrationcenter.post(
        "v1alpha1/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsImportJobsImportDataFilesDelete"
    ] = migrationcenter.post(
        "v1alpha1/{parent}/importDataFiles",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "importDataFileId": t.string(),
                "format": t.string(),
                "displayName": t.string().optional(),
                "uploadFileInfo": t.proxy(renames["UploadFileInfoIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImportJobsImportDataFilesGet"] = migrationcenter.post(
        "v1alpha1/{parent}/importDataFiles",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "importDataFileId": t.string(),
                "format": t.string(),
                "displayName": t.string().optional(),
                "uploadFileInfo": t.proxy(renames["UploadFileInfoIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImportJobsImportDataFilesList"] = migrationcenter.post(
        "v1alpha1/{parent}/importDataFiles",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "importDataFileId": t.string(),
                "format": t.string(),
                "displayName": t.string().optional(),
                "uploadFileInfo": t.proxy(renames["UploadFileInfoIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsImportJobsImportDataFilesCreate"
    ] = migrationcenter.post(
        "v1alpha1/{parent}/importDataFiles",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "importDataFileId": t.string(),
                "format": t.string(),
                "displayName": t.string().optional(),
                "uploadFileInfo": t.proxy(renames["UploadFileInfoIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = migrationcenter.get(
        "v1alpha1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = migrationcenter.get(
        "v1alpha1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = migrationcenter.get(
        "v1alpha1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = migrationcenter.get(
        "v1alpha1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsList"] = migrationcenter.delete(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsReportAssetFrames"] = migrationcenter.delete(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsPatch"] = migrationcenter.delete(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsBatchDelete"] = migrationcenter.delete(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsGet"] = migrationcenter.delete(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsBatchUpdate"] = migrationcenter.delete(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsAggregateValues"] = migrationcenter.delete(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsDelete"] = migrationcenter.delete(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsAddAssets"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsList"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsRemoveAssets"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsCreate"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsPatch"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsDelete"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsGet"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesGet"] = migrationcenter.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string(),
                "isManaged": t.boolean().optional(),
                "type": t.string().optional(),
                "displayName": t.string().optional(),
                "priority": t.integer().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesDelete"] = migrationcenter.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string(),
                "isManaged": t.boolean().optional(),
                "type": t.string().optional(),
                "displayName": t.string().optional(),
                "priority": t.integer().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesCreate"] = migrationcenter.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string(),
                "isManaged": t.boolean().optional(),
                "type": t.string().optional(),
                "displayName": t.string().optional(),
                "priority": t.integer().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesList"] = migrationcenter.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string(),
                "isManaged": t.boolean().optional(),
                "type": t.string().optional(),
                "displayName": t.string().optional(),
                "priority": t.integer().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesPatch"] = migrationcenter.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string(),
                "isManaged": t.boolean().optional(),
                "type": t.string().optional(),
                "displayName": t.string().optional(),
                "priority": t.integer().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesErrorFramesGet"] = migrationcenter.get(
        "v1alpha1/{parent}/errorFrames",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListErrorFramesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesErrorFramesList"] = migrationcenter.get(
        "v1alpha1/{parent}/errorFrames",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListErrorFramesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReportConfigsDelete"] = migrationcenter.get(
        "v1alpha1/{parent}/reportConfigs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListReportConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReportConfigsGet"] = migrationcenter.get(
        "v1alpha1/{parent}/reportConfigs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListReportConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReportConfigsCreate"] = migrationcenter.get(
        "v1alpha1/{parent}/reportConfigs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListReportConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReportConfigsList"] = migrationcenter.get(
        "v1alpha1/{parent}/reportConfigs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListReportConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReportConfigsReportsList"] = migrationcenter.post(
        "v1alpha1/{parent}/reports",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "reportId": t.string(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "type": t.string().optional(),
                "state": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReportConfigsReportsDelete"] = migrationcenter.post(
        "v1alpha1/{parent}/reports",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "reportId": t.string(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "type": t.string().optional(),
                "state": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReportConfigsReportsGet"] = migrationcenter.post(
        "v1alpha1/{parent}/reports",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "reportId": t.string(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "type": t.string().optional(),
                "state": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReportConfigsReportsCreate"] = migrationcenter.post(
        "v1alpha1/{parent}/reports",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "reportId": t.string(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "type": t.string().optional(),
                "state": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="migrationcenter",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
