from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_migrationcenter() -> Import:
    migrationcenter = HTTPRuntime("https://migrationcenter.googleapis.com/")

    renames = {
        "ErrorResponse": "_migrationcenter_1_ErrorResponse",
        "PerformanceSampleIn": "_migrationcenter_2_PerformanceSampleIn",
        "PerformanceSampleOut": "_migrationcenter_3_PerformanceSampleOut",
        "VirtualMachineDiskDetailsIn": "_migrationcenter_4_VirtualMachineDiskDetailsIn",
        "VirtualMachineDiskDetailsOut": "_migrationcenter_5_VirtualMachineDiskDetailsOut",
        "NetworkAdapterDetailsIn": "_migrationcenter_6_NetworkAdapterDetailsIn",
        "NetworkAdapterDetailsOut": "_migrationcenter_7_NetworkAdapterDetailsOut",
        "FrameViolationEntryIn": "_migrationcenter_8_FrameViolationEntryIn",
        "FrameViolationEntryOut": "_migrationcenter_9_FrameViolationEntryOut",
        "InlinePayloadInfoIn": "_migrationcenter_10_InlinePayloadInfoIn",
        "InlinePayloadInfoOut": "_migrationcenter_11_InlinePayloadInfoOut",
        "FileValidationReportIn": "_migrationcenter_12_FileValidationReportIn",
        "FileValidationReportOut": "_migrationcenter_13_FileValidationReportOut",
        "GuestInstalledApplicationIn": "_migrationcenter_14_GuestInstalledApplicationIn",
        "GuestInstalledApplicationOut": "_migrationcenter_15_GuestInstalledApplicationOut",
        "ListReportConfigsResponseIn": "_migrationcenter_16_ListReportConfigsResponseIn",
        "ListReportConfigsResponseOut": "_migrationcenter_17_ListReportConfigsResponseOut",
        "FramesIn": "_migrationcenter_18_FramesIn",
        "FramesOut": "_migrationcenter_19_FramesOut",
        "ValidationReportIn": "_migrationcenter_20_ValidationReportIn",
        "ValidationReportOut": "_migrationcenter_21_ValidationReportOut",
        "FstabEntryIn": "_migrationcenter_22_FstabEntryIn",
        "FstabEntryOut": "_migrationcenter_23_FstabEntryOut",
        "UploadFileInfoIn": "_migrationcenter_24_UploadFileInfoIn",
        "UploadFileInfoOut": "_migrationcenter_25_UploadFileInfoOut",
        "ExecutionReportIn": "_migrationcenter_26_ExecutionReportIn",
        "ExecutionReportOut": "_migrationcenter_27_ExecutionReportOut",
        "MigrationInsightIn": "_migrationcenter_28_MigrationInsightIn",
        "MigrationInsightOut": "_migrationcenter_29_MigrationInsightOut",
        "AggregateAssetsValuesResponseIn": "_migrationcenter_30_AggregateAssetsValuesResponseIn",
        "AggregateAssetsValuesResponseOut": "_migrationcenter_31_AggregateAssetsValuesResponseOut",
        "AggregationSumIn": "_migrationcenter_32_AggregationSumIn",
        "AggregationSumOut": "_migrationcenter_33_AggregationSumOut",
        "NetworkConnectionIn": "_migrationcenter_34_NetworkConnectionIn",
        "NetworkConnectionOut": "_migrationcenter_35_NetworkConnectionOut",
        "NfsExportListIn": "_migrationcenter_36_NfsExportListIn",
        "NfsExportListOut": "_migrationcenter_37_NfsExportListOut",
        "VirtualMachinePreferencesIn": "_migrationcenter_38_VirtualMachinePreferencesIn",
        "VirtualMachinePreferencesOut": "_migrationcenter_39_VirtualMachinePreferencesOut",
        "PhysicalPlatformDetailsIn": "_migrationcenter_40_PhysicalPlatformDetailsIn",
        "PhysicalPlatformDetailsOut": "_migrationcenter_41_PhysicalPlatformDetailsOut",
        "CancelOperationRequestIn": "_migrationcenter_42_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_migrationcenter_43_CancelOperationRequestOut",
        "ListErrorFramesResponseIn": "_migrationcenter_44_ListErrorFramesResponseIn",
        "ListErrorFramesResponseOut": "_migrationcenter_45_ListErrorFramesResponseOut",
        "DiskPartitionListIn": "_migrationcenter_46_DiskPartitionListIn",
        "DiskPartitionListOut": "_migrationcenter_47_DiskPartitionListOut",
        "BiosDetailsIn": "_migrationcenter_48_BiosDetailsIn",
        "BiosDetailsOut": "_migrationcenter_49_BiosDetailsOut",
        "GCSPayloadInfoIn": "_migrationcenter_50_GCSPayloadInfoIn",
        "GCSPayloadInfoOut": "_migrationcenter_51_GCSPayloadInfoOut",
        "ReportSummaryUtilizationChartDataIn": "_migrationcenter_52_ReportSummaryUtilizationChartDataIn",
        "ReportSummaryUtilizationChartDataOut": "_migrationcenter_53_ReportSummaryUtilizationChartDataOut",
        "ReportSummaryChartDataIn": "_migrationcenter_54_ReportSummaryChartDataIn",
        "ReportSummaryChartDataOut": "_migrationcenter_55_ReportSummaryChartDataOut",
        "MachinePreferencesIn": "_migrationcenter_56_MachinePreferencesIn",
        "MachinePreferencesOut": "_migrationcenter_57_MachinePreferencesOut",
        "SourceIn": "_migrationcenter_58_SourceIn",
        "SourceOut": "_migrationcenter_59_SourceOut",
        "RunningServiceListIn": "_migrationcenter_60_RunningServiceListIn",
        "RunningServiceListOut": "_migrationcenter_61_RunningServiceListOut",
        "ListReportsResponseIn": "_migrationcenter_62_ListReportsResponseIn",
        "ListReportsResponseOut": "_migrationcenter_63_ListReportsResponseOut",
        "ListLocationsResponseIn": "_migrationcenter_64_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_migrationcenter_65_ListLocationsResponseOut",
        "ReportSummaryIn": "_migrationcenter_66_ReportSummaryIn",
        "ReportSummaryOut": "_migrationcenter_67_ReportSummaryOut",
        "RunningServiceIn": "_migrationcenter_68_RunningServiceIn",
        "RunningServiceOut": "_migrationcenter_69_RunningServiceOut",
        "UpdateAssetRequestIn": "_migrationcenter_70_UpdateAssetRequestIn",
        "UpdateAssetRequestOut": "_migrationcenter_71_UpdateAssetRequestOut",
        "ListImportJobsResponseIn": "_migrationcenter_72_ListImportJobsResponseIn",
        "ListImportJobsResponseOut": "_migrationcenter_73_ListImportJobsResponseOut",
        "GuestConfigDetailsIn": "_migrationcenter_74_GuestConfigDetailsIn",
        "GuestConfigDetailsOut": "_migrationcenter_75_GuestConfigDetailsOut",
        "SettingsIn": "_migrationcenter_76_SettingsIn",
        "SettingsOut": "_migrationcenter_77_SettingsOut",
        "NetworkConnectionListIn": "_migrationcenter_78_NetworkConnectionListIn",
        "NetworkConnectionListOut": "_migrationcenter_79_NetworkConnectionListOut",
        "OperationIn": "_migrationcenter_80_OperationIn",
        "OperationOut": "_migrationcenter_81_OperationOut",
        "ReportConfigIn": "_migrationcenter_82_ReportConfigIn",
        "ReportConfigOut": "_migrationcenter_83_ReportConfigOut",
        "BatchUpdateAssetsRequestIn": "_migrationcenter_84_BatchUpdateAssetsRequestIn",
        "BatchUpdateAssetsRequestOut": "_migrationcenter_85_BatchUpdateAssetsRequestOut",
        "FitDescriptorIn": "_migrationcenter_86_FitDescriptorIn",
        "FitDescriptorOut": "_migrationcenter_87_FitDescriptorOut",
        "ListSourcesResponseIn": "_migrationcenter_88_ListSourcesResponseIn",
        "ListSourcesResponseOut": "_migrationcenter_89_ListSourcesResponseOut",
        "AzureVmPlatformDetailsIn": "_migrationcenter_90_AzureVmPlatformDetailsIn",
        "AzureVmPlatformDetailsOut": "_migrationcenter_91_AzureVmPlatformDetailsOut",
        "ReportSummaryChartDataDataPointIn": "_migrationcenter_92_ReportSummaryChartDataDataPointIn",
        "ReportSummaryChartDataDataPointOut": "_migrationcenter_93_ReportSummaryChartDataDataPointOut",
        "ReportIn": "_migrationcenter_94_ReportIn",
        "ReportOut": "_migrationcenter_95_ReportOut",
        "CpuUsageSampleIn": "_migrationcenter_96_CpuUsageSampleIn",
        "CpuUsageSampleOut": "_migrationcenter_97_CpuUsageSampleOut",
        "GuestInstalledApplicationListIn": "_migrationcenter_98_GuestInstalledApplicationListIn",
        "GuestInstalledApplicationListOut": "_migrationcenter_99_GuestInstalledApplicationListOut",
        "AggregationResultIn": "_migrationcenter_100_AggregationResultIn",
        "AggregationResultOut": "_migrationcenter_101_AggregationResultOut",
        "AggregationResultSumIn": "_migrationcenter_102_AggregationResultSumIn",
        "AggregationResultSumOut": "_migrationcenter_103_AggregationResultSumOut",
        "MachineSeriesIn": "_migrationcenter_104_MachineSeriesIn",
        "MachineSeriesOut": "_migrationcenter_105_MachineSeriesOut",
        "RuntimeNetworkInfoIn": "_migrationcenter_106_RuntimeNetworkInfoIn",
        "RuntimeNetworkInfoOut": "_migrationcenter_107_RuntimeNetworkInfoOut",
        "EmptyIn": "_migrationcenter_108_EmptyIn",
        "EmptyOut": "_migrationcenter_109_EmptyOut",
        "ImportJobIn": "_migrationcenter_110_ImportJobIn",
        "ImportJobOut": "_migrationcenter_111_ImportJobOut",
        "ValidateImportJobRequestIn": "_migrationcenter_112_ValidateImportJobRequestIn",
        "ValidateImportJobRequestOut": "_migrationcenter_113_ValidateImportJobRequestOut",
        "ReportSummaryHistogramChartDataIn": "_migrationcenter_114_ReportSummaryHistogramChartDataIn",
        "ReportSummaryHistogramChartDataOut": "_migrationcenter_115_ReportSummaryHistogramChartDataOut",
        "MoneyIn": "_migrationcenter_116_MoneyIn",
        "MoneyOut": "_migrationcenter_117_MoneyOut",
        "OperationMetadataIn": "_migrationcenter_118_OperationMetadataIn",
        "OperationMetadataOut": "_migrationcenter_119_OperationMetadataOut",
        "StatusIn": "_migrationcenter_120_StatusIn",
        "StatusOut": "_migrationcenter_121_StatusOut",
        "ReportSummaryAssetAggregateStatsIn": "_migrationcenter_122_ReportSummaryAssetAggregateStatsIn",
        "ReportSummaryAssetAggregateStatsOut": "_migrationcenter_123_ReportSummaryAssetAggregateStatsOut",
        "DateTimeIn": "_migrationcenter_124_DateTimeIn",
        "DateTimeOut": "_migrationcenter_125_DateTimeOut",
        "ReportSummaryMachineFindingIn": "_migrationcenter_126_ReportSummaryMachineFindingIn",
        "ReportSummaryMachineFindingOut": "_migrationcenter_127_ReportSummaryMachineFindingOut",
        "VmwareEngineMigrationTargetIn": "_migrationcenter_128_VmwareEngineMigrationTargetIn",
        "VmwareEngineMigrationTargetOut": "_migrationcenter_129_VmwareEngineMigrationTargetOut",
        "ListPreferenceSetsResponseIn": "_migrationcenter_130_ListPreferenceSetsResponseIn",
        "ListPreferenceSetsResponseOut": "_migrationcenter_131_ListPreferenceSetsResponseOut",
        "HostsEntryIn": "_migrationcenter_132_HostsEntryIn",
        "HostsEntryOut": "_migrationcenter_133_HostsEntryOut",
        "AggregationIn": "_migrationcenter_134_AggregationIn",
        "AggregationOut": "_migrationcenter_135_AggregationOut",
        "AssetFrameIn": "_migrationcenter_136_AssetFrameIn",
        "AssetFrameOut": "_migrationcenter_137_AssetFrameOut",
        "AggregationResultHistogramIn": "_migrationcenter_138_AggregationResultHistogramIn",
        "AggregationResultHistogramOut": "_migrationcenter_139_AggregationResultHistogramOut",
        "InsightIn": "_migrationcenter_140_InsightIn",
        "InsightOut": "_migrationcenter_141_InsightOut",
        "DailyResourceUsageAggregationStatsIn": "_migrationcenter_142_DailyResourceUsageAggregationStatsIn",
        "DailyResourceUsageAggregationStatsOut": "_migrationcenter_143_DailyResourceUsageAggregationStatsOut",
        "DailyResourceUsageAggregationIn": "_migrationcenter_144_DailyResourceUsageAggregationIn",
        "DailyResourceUsageAggregationOut": "_migrationcenter_145_DailyResourceUsageAggregationOut",
        "AggregationResultFrequencyIn": "_migrationcenter_146_AggregationResultFrequencyIn",
        "AggregationResultFrequencyOut": "_migrationcenter_147_AggregationResultFrequencyOut",
        "InsightListIn": "_migrationcenter_148_InsightListIn",
        "InsightListOut": "_migrationcenter_149_InsightListOut",
        "AssetPerformanceDataIn": "_migrationcenter_150_AssetPerformanceDataIn",
        "AssetPerformanceDataOut": "_migrationcenter_151_AssetPerformanceDataOut",
        "AssetIn": "_migrationcenter_152_AssetIn",
        "AssetOut": "_migrationcenter_153_AssetOut",
        "AwsEc2PlatformDetailsIn": "_migrationcenter_154_AwsEc2PlatformDetailsIn",
        "AwsEc2PlatformDetailsOut": "_migrationcenter_155_AwsEc2PlatformDetailsOut",
        "GoogleKubernetesEngineMigrationTargetIn": "_migrationcenter_156_GoogleKubernetesEngineMigrationTargetIn",
        "GoogleKubernetesEngineMigrationTargetOut": "_migrationcenter_157_GoogleKubernetesEngineMigrationTargetOut",
        "AggregationResultCountIn": "_migrationcenter_158_AggregationResultCountIn",
        "AggregationResultCountOut": "_migrationcenter_159_AggregationResultCountOut",
        "BatchDeleteAssetsRequestIn": "_migrationcenter_160_BatchDeleteAssetsRequestIn",
        "BatchDeleteAssetsRequestOut": "_migrationcenter_161_BatchDeleteAssetsRequestOut",
        "ListGroupsResponseIn": "_migrationcenter_162_ListGroupsResponseIn",
        "ListGroupsResponseOut": "_migrationcenter_163_ListGroupsResponseOut",
        "ErrorFrameIn": "_migrationcenter_164_ErrorFrameIn",
        "ErrorFrameOut": "_migrationcenter_165_ErrorFrameOut",
        "OpenFileListIn": "_migrationcenter_166_OpenFileListIn",
        "OpenFileListOut": "_migrationcenter_167_OpenFileListOut",
        "GenericPlatformDetailsIn": "_migrationcenter_168_GenericPlatformDetailsIn",
        "GenericPlatformDetailsOut": "_migrationcenter_169_GenericPlatformDetailsOut",
        "VirtualMachineDetailsIn": "_migrationcenter_170_VirtualMachineDetailsIn",
        "VirtualMachineDetailsOut": "_migrationcenter_171_VirtualMachineDetailsOut",
        "PlatformDetailsIn": "_migrationcenter_172_PlatformDetailsIn",
        "PlatformDetailsOut": "_migrationcenter_173_PlatformDetailsOut",
        "ReportAssetFramesResponseIn": "_migrationcenter_174_ReportAssetFramesResponseIn",
        "ReportAssetFramesResponseOut": "_migrationcenter_175_ReportAssetFramesResponseOut",
        "RemoveAssetsFromGroupRequestIn": "_migrationcenter_176_RemoveAssetsFromGroupRequestIn",
        "RemoveAssetsFromGroupRequestOut": "_migrationcenter_177_RemoveAssetsFromGroupRequestOut",
        "AssetListIn": "_migrationcenter_178_AssetListIn",
        "AssetListOut": "_migrationcenter_179_AssetListOut",
        "GuestOsDetailsIn": "_migrationcenter_180_GuestOsDetailsIn",
        "GuestOsDetailsOut": "_migrationcenter_181_GuestOsDetailsOut",
        "ReportSummaryHistogramChartDataBucketIn": "_migrationcenter_182_ReportSummaryHistogramChartDataBucketIn",
        "ReportSummaryHistogramChartDataBucketOut": "_migrationcenter_183_ReportSummaryHistogramChartDataBucketOut",
        "FstabEntryListIn": "_migrationcenter_184_FstabEntryListIn",
        "FstabEntryListOut": "_migrationcenter_185_FstabEntryListOut",
        "DiskEntryIn": "_migrationcenter_186_DiskEntryIn",
        "DiskEntryOut": "_migrationcenter_187_DiskEntryOut",
        "RunningProcessListIn": "_migrationcenter_188_RunningProcessListIn",
        "RunningProcessListOut": "_migrationcenter_189_RunningProcessListOut",
        "ComputeEngineMigrationTargetIn": "_migrationcenter_190_ComputeEngineMigrationTargetIn",
        "ComputeEngineMigrationTargetOut": "_migrationcenter_191_ComputeEngineMigrationTargetOut",
        "NfsExportIn": "_migrationcenter_192_NfsExportIn",
        "NfsExportOut": "_migrationcenter_193_NfsExportOut",
        "VirtualMachineNetworkDetailsIn": "_migrationcenter_194_VirtualMachineNetworkDetailsIn",
        "VirtualMachineNetworkDetailsOut": "_migrationcenter_195_VirtualMachineNetworkDetailsOut",
        "ImportErrorIn": "_migrationcenter_196_ImportErrorIn",
        "ImportErrorOut": "_migrationcenter_197_ImportErrorOut",
        "NetworkAddressIn": "_migrationcenter_198_NetworkAddressIn",
        "NetworkAddressOut": "_migrationcenter_199_NetworkAddressOut",
        "DiskPartitionIn": "_migrationcenter_200_DiskPartitionIn",
        "DiskPartitionOut": "_migrationcenter_201_DiskPartitionOut",
        "RegionPreferencesIn": "_migrationcenter_202_RegionPreferencesIn",
        "RegionPreferencesOut": "_migrationcenter_203_RegionPreferencesOut",
        "ImportDataFileIn": "_migrationcenter_204_ImportDataFileIn",
        "ImportDataFileOut": "_migrationcenter_205_ImportDataFileOut",
        "DailyResourceUsageAggregationNetworkIn": "_migrationcenter_206_DailyResourceUsageAggregationNetworkIn",
        "DailyResourceUsageAggregationNetworkOut": "_migrationcenter_207_DailyResourceUsageAggregationNetworkOut",
        "HostsEntryListIn": "_migrationcenter_208_HostsEntryListIn",
        "HostsEntryListOut": "_migrationcenter_209_HostsEntryListOut",
        "ComputeEngineShapeDescriptorIn": "_migrationcenter_210_ComputeEngineShapeDescriptorIn",
        "ComputeEngineShapeDescriptorOut": "_migrationcenter_211_ComputeEngineShapeDescriptorOut",
        "AddAssetsToGroupRequestIn": "_migrationcenter_212_AddAssetsToGroupRequestIn",
        "AddAssetsToGroupRequestOut": "_migrationcenter_213_AddAssetsToGroupRequestOut",
        "DailyResourceUsageAggregationDiskIn": "_migrationcenter_214_DailyResourceUsageAggregationDiskIn",
        "DailyResourceUsageAggregationDiskOut": "_migrationcenter_215_DailyResourceUsageAggregationDiskOut",
        "ReportSummaryMachineSeriesAllocationIn": "_migrationcenter_216_ReportSummaryMachineSeriesAllocationIn",
        "ReportSummaryMachineSeriesAllocationOut": "_migrationcenter_217_ReportSummaryMachineSeriesAllocationOut",
        "OpenFileDetailsIn": "_migrationcenter_218_OpenFileDetailsIn",
        "OpenFileDetailsOut": "_migrationcenter_219_OpenFileDetailsOut",
        "GroupIn": "_migrationcenter_220_GroupIn",
        "GroupOut": "_migrationcenter_221_GroupOut",
        "DailyResourceUsageAggregationCPUIn": "_migrationcenter_222_DailyResourceUsageAggregationCPUIn",
        "DailyResourceUsageAggregationCPUOut": "_migrationcenter_223_DailyResourceUsageAggregationCPUOut",
        "ListOperationsResponseIn": "_migrationcenter_224_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_migrationcenter_225_ListOperationsResponseOut",
        "ReportConfigGroupPreferenceSetAssignmentIn": "_migrationcenter_226_ReportConfigGroupPreferenceSetAssignmentIn",
        "ReportConfigGroupPreferenceSetAssignmentOut": "_migrationcenter_227_ReportConfigGroupPreferenceSetAssignmentOut",
        "ComputeEnginePreferencesIn": "_migrationcenter_228_ComputeEnginePreferencesIn",
        "ComputeEnginePreferencesOut": "_migrationcenter_229_ComputeEnginePreferencesOut",
        "NetworkUsageSampleIn": "_migrationcenter_230_NetworkUsageSampleIn",
        "NetworkUsageSampleOut": "_migrationcenter_231_NetworkUsageSampleOut",
        "VmwareDiskConfigIn": "_migrationcenter_232_VmwareDiskConfigIn",
        "VmwareDiskConfigOut": "_migrationcenter_233_VmwareDiskConfigOut",
        "GuestRuntimeDetailsIn": "_migrationcenter_234_GuestRuntimeDetailsIn",
        "GuestRuntimeDetailsOut": "_migrationcenter_235_GuestRuntimeDetailsOut",
        "DiskUsageSampleIn": "_migrationcenter_236_DiskUsageSampleIn",
        "DiskUsageSampleOut": "_migrationcenter_237_DiskUsageSampleOut",
        "ImportRowErrorIn": "_migrationcenter_238_ImportRowErrorIn",
        "ImportRowErrorOut": "_migrationcenter_239_ImportRowErrorOut",
        "BatchUpdateAssetsResponseIn": "_migrationcenter_240_BatchUpdateAssetsResponseIn",
        "BatchUpdateAssetsResponseOut": "_migrationcenter_241_BatchUpdateAssetsResponseOut",
        "DateIn": "_migrationcenter_242_DateIn",
        "DateOut": "_migrationcenter_243_DateOut",
        "LocationIn": "_migrationcenter_244_LocationIn",
        "LocationOut": "_migrationcenter_245_LocationOut",
        "PayloadFileIn": "_migrationcenter_246_PayloadFileIn",
        "PayloadFileOut": "_migrationcenter_247_PayloadFileOut",
        "DailyResourceUsageAggregationMemoryIn": "_migrationcenter_248_DailyResourceUsageAggregationMemoryIn",
        "DailyResourceUsageAggregationMemoryOut": "_migrationcenter_249_DailyResourceUsageAggregationMemoryOut",
        "ListAssetsResponseIn": "_migrationcenter_250_ListAssetsResponseIn",
        "ListAssetsResponseOut": "_migrationcenter_251_ListAssetsResponseOut",
        "RunningProcessIn": "_migrationcenter_252_RunningProcessIn",
        "RunningProcessOut": "_migrationcenter_253_RunningProcessOut",
        "PreferenceSetIn": "_migrationcenter_254_PreferenceSetIn",
        "PreferenceSetOut": "_migrationcenter_255_PreferenceSetOut",
        "ListImportDataFilesResponseIn": "_migrationcenter_256_ListImportDataFilesResponseIn",
        "ListImportDataFilesResponseOut": "_migrationcenter_257_ListImportDataFilesResponseOut",
        "AggregationFrequencyIn": "_migrationcenter_258_AggregationFrequencyIn",
        "AggregationFrequencyOut": "_migrationcenter_259_AggregationFrequencyOut",
        "RunImportJobRequestIn": "_migrationcenter_260_RunImportJobRequestIn",
        "RunImportJobRequestOut": "_migrationcenter_261_RunImportJobRequestOut",
        "AggregationHistogramIn": "_migrationcenter_262_AggregationHistogramIn",
        "AggregationHistogramOut": "_migrationcenter_263_AggregationHistogramOut",
        "SelinuxIn": "_migrationcenter_264_SelinuxIn",
        "SelinuxOut": "_migrationcenter_265_SelinuxOut",
        "ReportSummaryGroupPreferenceSetFindingIn": "_migrationcenter_266_ReportSummaryGroupPreferenceSetFindingIn",
        "ReportSummaryGroupPreferenceSetFindingOut": "_migrationcenter_267_ReportSummaryGroupPreferenceSetFindingOut",
        "ReportSummaryGroupFindingIn": "_migrationcenter_268_ReportSummaryGroupFindingIn",
        "ReportSummaryGroupFindingOut": "_migrationcenter_269_ReportSummaryGroupFindingOut",
        "NetworkAddressListIn": "_migrationcenter_270_NetworkAddressListIn",
        "NetworkAddressListOut": "_migrationcenter_271_NetworkAddressListOut",
        "NetworkAdapterListIn": "_migrationcenter_272_NetworkAdapterListIn",
        "NetworkAdapterListOut": "_migrationcenter_273_NetworkAdapterListOut",
        "DiskEntryListIn": "_migrationcenter_274_DiskEntryListIn",
        "DiskEntryListOut": "_migrationcenter_275_DiskEntryListOut",
        "VmwarePlatformDetailsIn": "_migrationcenter_276_VmwarePlatformDetailsIn",
        "VmwarePlatformDetailsOut": "_migrationcenter_277_VmwarePlatformDetailsOut",
        "MemoryUsageSampleIn": "_migrationcenter_278_MemoryUsageSampleIn",
        "MemoryUsageSampleOut": "_migrationcenter_279_MemoryUsageSampleOut",
        "AggregationCountIn": "_migrationcenter_280_AggregationCountIn",
        "AggregationCountOut": "_migrationcenter_281_AggregationCountOut",
        "AggregateAssetsValuesRequestIn": "_migrationcenter_282_AggregateAssetsValuesRequestIn",
        "AggregateAssetsValuesRequestOut": "_migrationcenter_283_AggregateAssetsValuesRequestOut",
        "AggregationResultHistogramBucketIn": "_migrationcenter_284_AggregationResultHistogramBucketIn",
        "AggregationResultHistogramBucketOut": "_migrationcenter_285_AggregationResultHistogramBucketOut",
        "VirtualMachineArchitectureDetailsIn": "_migrationcenter_286_VirtualMachineArchitectureDetailsIn",
        "VirtualMachineArchitectureDetailsOut": "_migrationcenter_287_VirtualMachineArchitectureDetailsOut",
        "TimeZoneIn": "_migrationcenter_288_TimeZoneIn",
        "TimeZoneOut": "_migrationcenter_289_TimeZoneOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["PerformanceSampleIn"] = t.struct(
        {
            "sampleTime": t.string().optional(),
            "cpu": t.proxy(renames["CpuUsageSampleIn"]).optional(),
            "network": t.proxy(renames["NetworkUsageSampleIn"]).optional(),
            "disk": t.proxy(renames["DiskUsageSampleIn"]).optional(),
            "memory": t.proxy(renames["MemoryUsageSampleIn"]).optional(),
        }
    ).named(renames["PerformanceSampleIn"])
    types["PerformanceSampleOut"] = t.struct(
        {
            "sampleTime": t.string().optional(),
            "cpu": t.proxy(renames["CpuUsageSampleOut"]).optional(),
            "network": t.proxy(renames["NetworkUsageSampleOut"]).optional(),
            "disk": t.proxy(renames["DiskUsageSampleOut"]).optional(),
            "memory": t.proxy(renames["MemoryUsageSampleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerformanceSampleOut"])
    types["VirtualMachineDiskDetailsIn"] = t.struct(
        {
            "hddTotalFreeBytes": t.string().optional(),
            "disks": t.proxy(renames["DiskEntryListIn"]).optional(),
            "lsblkJson": t.string().optional(),
            "hddTotalCapacityBytes": t.string().optional(),
        }
    ).named(renames["VirtualMachineDiskDetailsIn"])
    types["VirtualMachineDiskDetailsOut"] = t.struct(
        {
            "hddTotalFreeBytes": t.string().optional(),
            "disks": t.proxy(renames["DiskEntryListOut"]).optional(),
            "lsblkJson": t.string().optional(),
            "hddTotalCapacityBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualMachineDiskDetailsOut"])
    types["NetworkAdapterDetailsIn"] = t.struct(
        {
            "macAddress": t.string().optional(),
            "addresses": t.proxy(renames["NetworkAddressListIn"]).optional(),
            "adapterType": t.string().optional(),
        }
    ).named(renames["NetworkAdapterDetailsIn"])
    types["NetworkAdapterDetailsOut"] = t.struct(
        {
            "macAddress": t.string().optional(),
            "addresses": t.proxy(renames["NetworkAddressListOut"]).optional(),
            "adapterType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkAdapterDetailsOut"])
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
    types["InlinePayloadInfoIn"] = t.struct(
        {
            "payload": t.array(t.proxy(renames["PayloadFileIn"])).optional(),
            "format": t.string().optional(),
        }
    ).named(renames["InlinePayloadInfoIn"])
    types["InlinePayloadInfoOut"] = t.struct(
        {
            "payload": t.array(t.proxy(renames["PayloadFileOut"])).optional(),
            "format": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InlinePayloadInfoOut"])
    types["FileValidationReportIn"] = t.struct(
        {
            "fileName": t.string().optional(),
            "rowErrors": t.array(t.proxy(renames["ImportRowErrorIn"])).optional(),
            "partialReport": t.boolean().optional(),
            "fileErrors": t.array(t.proxy(renames["ImportErrorIn"])).optional(),
        }
    ).named(renames["FileValidationReportIn"])
    types["FileValidationReportOut"] = t.struct(
        {
            "fileName": t.string().optional(),
            "rowErrors": t.array(t.proxy(renames["ImportRowErrorOut"])).optional(),
            "partialReport": t.boolean().optional(),
            "fileErrors": t.array(t.proxy(renames["ImportErrorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileValidationReportOut"])
    types["GuestInstalledApplicationIn"] = t.struct(
        {
            "version": t.string().optional(),
            "time": t.string().optional(),
            "name": t.string().optional(),
            "path": t.string().optional(),
            "vendor": t.string().optional(),
        }
    ).named(renames["GuestInstalledApplicationIn"])
    types["GuestInstalledApplicationOut"] = t.struct(
        {
            "version": t.string().optional(),
            "time": t.string().optional(),
            "name": t.string().optional(),
            "path": t.string().optional(),
            "vendor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestInstalledApplicationOut"])
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
    types["FramesIn"] = t.struct(
        {"framesData": t.array(t.proxy(renames["AssetFrameIn"])).optional()}
    ).named(renames["FramesIn"])
    types["FramesOut"] = t.struct(
        {
            "framesData": t.array(t.proxy(renames["AssetFrameOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FramesOut"])
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
    types["FstabEntryIn"] = t.struct(
        {
            "file": t.string().optional(),
            "spec": t.string().optional(),
            "mntops": t.string().optional(),
            "freq": t.integer().optional(),
            "passno": t.integer().optional(),
            "vfstype": t.string().optional(),
        }
    ).named(renames["FstabEntryIn"])
    types["FstabEntryOut"] = t.struct(
        {
            "file": t.string().optional(),
            "spec": t.string().optional(),
            "mntops": t.string().optional(),
            "freq": t.integer().optional(),
            "passno": t.integer().optional(),
            "vfstype": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FstabEntryOut"])
    types["UploadFileInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadFileInfoIn"]
    )
    types["UploadFileInfoOut"] = t.struct(
        {
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "signedUri": t.string().optional(),
            "uriExpirationTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadFileInfoOut"])
    types["ExecutionReportIn"] = t.struct(
        {
            "framesReported": t.integer().optional(),
            "totalRowsCount": t.integer().optional(),
            "executionErrors": t.proxy(renames["ValidationReportIn"]).optional(),
            "jobErrors": t.array(t.proxy(renames["ImportErrorIn"])).optional(),
        }
    ).named(renames["ExecutionReportIn"])
    types["ExecutionReportOut"] = t.struct(
        {
            "framesReported": t.integer().optional(),
            "totalRowsCount": t.integer().optional(),
            "executionErrors": t.proxy(renames["ValidationReportOut"]).optional(),
            "jobErrors": t.array(t.proxy(renames["ImportErrorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionReportOut"])
    types["MigrationInsightIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MigrationInsightIn"]
    )
    types["MigrationInsightOut"] = t.struct(
        {
            "vmwareEngineTarget": t.proxy(
                renames["VmwareEngineMigrationTargetOut"]
            ).optional(),
            "gkeTarget": t.proxy(
                renames["GoogleKubernetesEngineMigrationTargetOut"]
            ).optional(),
            "fit": t.proxy(renames["FitDescriptorOut"]).optional(),
            "computeEngineTarget": t.proxy(
                renames["ComputeEngineMigrationTargetOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MigrationInsightOut"])
    types["AggregateAssetsValuesResponseIn"] = t.struct(
        {"results": t.array(t.proxy(renames["AggregationResultIn"])).optional()}
    ).named(renames["AggregateAssetsValuesResponseIn"])
    types["AggregateAssetsValuesResponseOut"] = t.struct(
        {
            "results": t.array(t.proxy(renames["AggregationResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregateAssetsValuesResponseOut"])
    types["AggregationSumIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AggregationSumIn"]
    )
    types["AggregationSumOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AggregationSumOut"])
    types["NetworkConnectionIn"] = t.struct(
        {
            "localPort": t.integer().optional(),
            "state": t.string().optional(),
            "remoteIpAddress": t.string().optional(),
            "processName": t.string().optional(),
            "localIpAddress": t.string().optional(),
            "remotePort": t.integer().optional(),
            "protocol": t.string().optional(),
            "pid": t.string().optional(),
        }
    ).named(renames["NetworkConnectionIn"])
    types["NetworkConnectionOut"] = t.struct(
        {
            "localPort": t.integer().optional(),
            "state": t.string().optional(),
            "remoteIpAddress": t.string().optional(),
            "processName": t.string().optional(),
            "localIpAddress": t.string().optional(),
            "remotePort": t.integer().optional(),
            "protocol": t.string().optional(),
            "pid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConnectionOut"])
    types["NfsExportListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["NfsExportIn"])).optional()}
    ).named(renames["NfsExportListIn"])
    types["NfsExportListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["NfsExportOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NfsExportListOut"])
    types["VirtualMachinePreferencesIn"] = t.struct(
        {
            "regionPreferences": t.proxy(renames["RegionPreferencesIn"]).optional(),
            "sizingOptimizationStrategy": t.string().optional(),
            "computeEnginePreferences": t.proxy(
                renames["ComputeEnginePreferencesIn"]
            ).optional(),
            "commitmentPlan": t.string().optional(),
        }
    ).named(renames["VirtualMachinePreferencesIn"])
    types["VirtualMachinePreferencesOut"] = t.struct(
        {
            "regionPreferences": t.proxy(renames["RegionPreferencesOut"]).optional(),
            "sizingOptimizationStrategy": t.string().optional(),
            "computeEnginePreferences": t.proxy(
                renames["ComputeEnginePreferencesOut"]
            ).optional(),
            "commitmentPlan": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualMachinePreferencesOut"])
    types["PhysicalPlatformDetailsIn"] = t.struct(
        {"location": t.string().optional()}
    ).named(renames["PhysicalPlatformDetailsIn"])
    types["PhysicalPlatformDetailsOut"] = t.struct(
        {
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhysicalPlatformDetailsOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["ListErrorFramesResponseIn"] = t.struct(
        {
            "errorFrames": t.array(t.proxy(renames["ErrorFrameIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListErrorFramesResponseIn"])
    types["ListErrorFramesResponseOut"] = t.struct(
        {
            "errorFrames": t.array(t.proxy(renames["ErrorFrameOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListErrorFramesResponseOut"])
    types["DiskPartitionListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["DiskPartitionIn"])).optional()}
    ).named(renames["DiskPartitionListIn"])
    types["DiskPartitionListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["DiskPartitionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskPartitionListOut"])
    types["BiosDetailsIn"] = t.struct(
        {
            "biosManufacturer": t.string().optional(),
            "biosVersion": t.string().optional(),
            "biosReleaseDate": t.string().optional(),
            "smbiosUuid": t.string().optional(),
            "biosName": t.string().optional(),
        }
    ).named(renames["BiosDetailsIn"])
    types["BiosDetailsOut"] = t.struct(
        {
            "biosManufacturer": t.string().optional(),
            "biosVersion": t.string().optional(),
            "biosReleaseDate": t.string().optional(),
            "smbiosUuid": t.string().optional(),
            "biosName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BiosDetailsOut"])
    types["GCSPayloadInfoIn"] = t.struct(
        {"path": t.string().optional(), "format": t.string().optional()}
    ).named(renames["GCSPayloadInfoIn"])
    types["GCSPayloadInfoOut"] = t.struct(
        {
            "path": t.string().optional(),
            "format": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GCSPayloadInfoOut"])
    types["ReportSummaryUtilizationChartDataIn"] = t.struct(
        {"used": t.string().optional(), "free": t.string().optional()}
    ).named(renames["ReportSummaryUtilizationChartDataIn"])
    types["ReportSummaryUtilizationChartDataOut"] = t.struct(
        {
            "used": t.string().optional(),
            "free": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryUtilizationChartDataOut"])
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
    types["SourceIn"] = t.struct(
        {
            "description": t.string().optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "isManaged": t.boolean().optional(),
            "priority": t.integer().optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "type": t.string().optional(),
            "pendingFrameCount": t.integer().optional(),
            "displayName": t.string().optional(),
            "errorFrameCount": t.integer().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "isManaged": t.boolean().optional(),
            "priority": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["RunningServiceListIn"] = t.struct(
        {"services": t.array(t.proxy(renames["RunningServiceIn"])).optional()}
    ).named(renames["RunningServiceListIn"])
    types["RunningServiceListOut"] = t.struct(
        {
            "services": t.array(t.proxy(renames["RunningServiceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunningServiceListOut"])
    types["ListReportsResponseIn"] = t.struct(
        {
            "reports": t.array(t.proxy(renames["ReportIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListReportsResponseIn"])
    types["ListReportsResponseOut"] = t.struct(
        {
            "reports": t.array(t.proxy(renames["ReportOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReportsResponseOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
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
    types["RunningServiceIn"] = t.struct(
        {
            "exePath": t.string().optional(),
            "state": t.string().optional(),
            "startMode": t.string().optional(),
            "status": t.string().optional(),
            "name": t.string().optional(),
            "cmdline": t.string().optional(),
            "pid": t.string().optional(),
        }
    ).named(renames["RunningServiceIn"])
    types["RunningServiceOut"] = t.struct(
        {
            "exePath": t.string().optional(),
            "state": t.string().optional(),
            "startMode": t.string().optional(),
            "status": t.string().optional(),
            "name": t.string().optional(),
            "cmdline": t.string().optional(),
            "pid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunningServiceOut"])
    types["UpdateAssetRequestIn"] = t.struct(
        {
            "asset": t.proxy(renames["AssetIn"]),
            "updateMask": t.string(),
            "requestId": t.string().optional(),
        }
    ).named(renames["UpdateAssetRequestIn"])
    types["UpdateAssetRequestOut"] = t.struct(
        {
            "asset": t.proxy(renames["AssetOut"]),
            "updateMask": t.string(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateAssetRequestOut"])
    types["ListImportJobsResponseIn"] = t.struct(
        {
            "importJobs": t.array(t.proxy(renames["ImportJobIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListImportJobsResponseIn"])
    types["ListImportJobsResponseOut"] = t.struct(
        {
            "importJobs": t.array(t.proxy(renames["ImportJobOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListImportJobsResponseOut"])
    types["GuestConfigDetailsIn"] = t.struct(
        {
            "issue": t.string().optional(),
            "hosts": t.proxy(renames["HostsEntryListIn"]).optional(),
            "nfsExports": t.proxy(renames["NfsExportListIn"]).optional(),
            "selinux": t.proxy(renames["SelinuxIn"]).optional(),
            "fstab": t.proxy(renames["FstabEntryListIn"]).optional(),
        }
    ).named(renames["GuestConfigDetailsIn"])
    types["GuestConfigDetailsOut"] = t.struct(
        {
            "issue": t.string().optional(),
            "hosts": t.proxy(renames["HostsEntryListOut"]).optional(),
            "nfsExports": t.proxy(renames["NfsExportListOut"]).optional(),
            "selinux": t.proxy(renames["SelinuxOut"]).optional(),
            "fstab": t.proxy(renames["FstabEntryListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestConfigDetailsOut"])
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
    types["NetworkConnectionListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["NetworkConnectionIn"])).optional()}
    ).named(renames["NetworkConnectionListIn"])
    types["NetworkConnectionListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["NetworkConnectionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConnectionListOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["ReportConfigIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "groupPreferencesetAssignments": t.array(
                t.proxy(renames["ReportConfigGroupPreferenceSetAssignmentIn"])
            ),
            "description": t.string().optional(),
        }
    ).named(renames["ReportConfigIn"])
    types["ReportConfigOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "groupPreferencesetAssignments": t.array(
                t.proxy(renames["ReportConfigGroupPreferenceSetAssignmentOut"])
            ),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportConfigOut"])
    types["BatchUpdateAssetsRequestIn"] = t.struct(
        {"requests": t.array(t.proxy(renames["UpdateAssetRequestIn"]))}
    ).named(renames["BatchUpdateAssetsRequestIn"])
    types["BatchUpdateAssetsRequestOut"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["UpdateAssetRequestOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateAssetsRequestOut"])
    types["FitDescriptorIn"] = t.struct({"fitLevel": t.string().optional()}).named(
        renames["FitDescriptorIn"]
    )
    types["FitDescriptorOut"] = t.struct(
        {
            "fitLevel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FitDescriptorOut"])
    types["ListSourcesResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "sources": t.array(t.proxy(renames["SourceIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListSourcesResponseIn"])
    types["ListSourcesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSourcesResponseOut"])
    types["AzureVmPlatformDetailsIn"] = t.struct(
        {
            "provisioningState": t.string().optional(),
            "location": t.string().optional(),
            "machineTypeLabel": t.string().optional(),
        }
    ).named(renames["AzureVmPlatformDetailsIn"])
    types["AzureVmPlatformDetailsOut"] = t.struct(
        {
            "provisioningState": t.string().optional(),
            "location": t.string().optional(),
            "machineTypeLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AzureVmPlatformDetailsOut"])
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
    types["ReportIn"] = t.struct(
        {
            "state": t.string().optional(),
            "description": t.string().optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["ReportIn"])
    types["ReportOut"] = t.struct(
        {
            "state": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "summary": t.proxy(renames["ReportSummaryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportOut"])
    types["CpuUsageSampleIn"] = t.struct(
        {"utilizedPercentage": t.number().optional()}
    ).named(renames["CpuUsageSampleIn"])
    types["CpuUsageSampleOut"] = t.struct(
        {
            "utilizedPercentage": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CpuUsageSampleOut"])
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
    types["AggregationResultIn"] = t.struct(
        {
            "field": t.string(),
            "sum": t.proxy(renames["AggregationResultSumIn"]),
            "histogram": t.proxy(renames["AggregationResultHistogramIn"]),
            "frequency": t.proxy(renames["AggregationResultFrequencyIn"]),
            "count": t.proxy(renames["AggregationResultCountIn"]),
        }
    ).named(renames["AggregationResultIn"])
    types["AggregationResultOut"] = t.struct(
        {
            "field": t.string(),
            "sum": t.proxy(renames["AggregationResultSumOut"]),
            "histogram": t.proxy(renames["AggregationResultHistogramOut"]),
            "frequency": t.proxy(renames["AggregationResultFrequencyOut"]),
            "count": t.proxy(renames["AggregationResultCountOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationResultOut"])
    types["AggregationResultSumIn"] = t.struct({"value": t.number()}).named(
        renames["AggregationResultSumIn"]
    )
    types["AggregationResultSumOut"] = t.struct(
        {"value": t.number(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AggregationResultSumOut"])
    types["MachineSeriesIn"] = t.struct({"code": t.string().optional()}).named(
        renames["MachineSeriesIn"]
    )
    types["MachineSeriesOut"] = t.struct(
        {
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MachineSeriesOut"])
    types["RuntimeNetworkInfoIn"] = t.struct(
        {
            "connections": t.proxy(renames["NetworkConnectionListIn"]).optional(),
            "netstatTime": t.proxy(renames["DateTimeIn"]).optional(),
            "netstat": t.string().optional(),
        }
    ).named(renames["RuntimeNetworkInfoIn"])
    types["RuntimeNetworkInfoOut"] = t.struct(
        {
            "connections": t.proxy(renames["NetworkConnectionListOut"]).optional(),
            "netstatTime": t.proxy(renames["DateTimeOut"]).optional(),
            "netstat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeNetworkInfoOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ImportJobIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "assetSource": t.string(),
            "inlinePayload": t.proxy(renames["InlinePayloadInfoIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "gcsPayload": t.proxy(renames["GCSPayloadInfoIn"]).optional(),
        }
    ).named(renames["ImportJobIn"])
    types["ImportJobOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "assetSource": t.string(),
            "inlinePayload": t.proxy(renames["InlinePayloadInfoOut"]).optional(),
            "completeTime": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "gcsPayload": t.proxy(renames["GCSPayloadInfoOut"]).optional(),
            "validationReport": t.proxy(renames["ValidationReportOut"]).optional(),
            "executionReport": t.proxy(renames["ExecutionReportOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportJobOut"])
    types["ValidateImportJobRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["ValidateImportJobRequestIn"])
    types["ValidateImportJobRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateImportJobRequestOut"])
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
    types["MoneyIn"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "units": t.string().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["MoneyIn"])
    types["MoneyOut"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "units": t.string().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoneyOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "statusMessage": t.string().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["ReportSummaryAssetAggregateStatsIn"] = t.struct(
        {
            "totalMemoryBytes": t.string().optional(),
            "coreCountHistogram": t.proxy(
                renames["ReportSummaryHistogramChartDataIn"]
            ).optional(),
            "totalStorageBytes": t.string().optional(),
            "assetAge": t.proxy(renames["ReportSummaryChartDataIn"]).optional(),
            "storageUtilization": t.proxy(
                renames["ReportSummaryChartDataIn"]
            ).optional(),
            "memoryBytesHistogram": t.proxy(
                renames["ReportSummaryHistogramChartDataIn"]
            ).optional(),
            "storageUtilizationChart": t.proxy(
                renames["ReportSummaryUtilizationChartDataIn"]
            ).optional(),
            "operatingSystem": t.proxy(renames["ReportSummaryChartDataIn"]).optional(),
            "memoryUtilization": t.proxy(
                renames["ReportSummaryChartDataIn"]
            ).optional(),
            "storageBytesHistogram": t.proxy(
                renames["ReportSummaryHistogramChartDataIn"]
            ).optional(),
            "memoryUtilizationChart": t.proxy(
                renames["ReportSummaryUtilizationChartDataIn"]
            ).optional(),
            "totalCores": t.string().optional(),
            "totalAssets": t.string().optional(),
        }
    ).named(renames["ReportSummaryAssetAggregateStatsIn"])
    types["ReportSummaryAssetAggregateStatsOut"] = t.struct(
        {
            "totalMemoryBytes": t.string().optional(),
            "coreCountHistogram": t.proxy(
                renames["ReportSummaryHistogramChartDataOut"]
            ).optional(),
            "totalStorageBytes": t.string().optional(),
            "assetAge": t.proxy(renames["ReportSummaryChartDataOut"]).optional(),
            "storageUtilization": t.proxy(
                renames["ReportSummaryChartDataOut"]
            ).optional(),
            "memoryBytesHistogram": t.proxy(
                renames["ReportSummaryHistogramChartDataOut"]
            ).optional(),
            "storageUtilizationChart": t.proxy(
                renames["ReportSummaryUtilizationChartDataOut"]
            ).optional(),
            "operatingSystem": t.proxy(renames["ReportSummaryChartDataOut"]).optional(),
            "memoryUtilization": t.proxy(
                renames["ReportSummaryChartDataOut"]
            ).optional(),
            "storageBytesHistogram": t.proxy(
                renames["ReportSummaryHistogramChartDataOut"]
            ).optional(),
            "memoryUtilizationChart": t.proxy(
                renames["ReportSummaryUtilizationChartDataOut"]
            ).optional(),
            "totalCores": t.string().optional(),
            "totalAssets": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryAssetAggregateStatsOut"])
    types["DateTimeIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "hours": t.integer().optional(),
            "day": t.integer().optional(),
            "utcOffset": t.string().optional(),
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
            "minutes": t.integer().optional(),
            "timeZone": t.proxy(renames["TimeZoneIn"]).optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["DateTimeIn"])
    types["DateTimeOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "hours": t.integer().optional(),
            "day": t.integer().optional(),
            "utcOffset": t.string().optional(),
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
            "minutes": t.integer().optional(),
            "timeZone": t.proxy(renames["TimeZoneOut"]).optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateTimeOut"])
    types["ReportSummaryMachineFindingIn"] = t.struct(
        {
            "allocatedRegions": t.array(t.string()).optional(),
            "machineSeriesAllocations": t.array(
                t.proxy(renames["ReportSummaryMachineSeriesAllocationIn"])
            ).optional(),
            "allocatedAssetCount": t.string().optional(),
            "allocatedDiskTypes": t.array(t.string()).optional(),
        }
    ).named(renames["ReportSummaryMachineFindingIn"])
    types["ReportSummaryMachineFindingOut"] = t.struct(
        {
            "allocatedRegions": t.array(t.string()).optional(),
            "machineSeriesAllocations": t.array(
                t.proxy(renames["ReportSummaryMachineSeriesAllocationOut"])
            ).optional(),
            "allocatedAssetCount": t.string().optional(),
            "allocatedDiskTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryMachineFindingOut"])
    types["VmwareEngineMigrationTargetIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["VmwareEngineMigrationTargetIn"])
    types["VmwareEngineMigrationTargetOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VmwareEngineMigrationTargetOut"])
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
    types["HostsEntryIn"] = t.struct(
        {"ip": t.string().optional(), "hostNames": t.array(t.string()).optional()}
    ).named(renames["HostsEntryIn"])
    types["HostsEntryOut"] = t.struct(
        {
            "ip": t.string().optional(),
            "hostNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HostsEntryOut"])
    types["AggregationIn"] = t.struct(
        {
            "histogram": t.proxy(renames["AggregationHistogramIn"]).optional(),
            "sum": t.proxy(renames["AggregationSumIn"]).optional(),
            "field": t.string().optional(),
            "frequency": t.proxy(renames["AggregationFrequencyIn"]).optional(),
            "count": t.proxy(renames["AggregationCountIn"]).optional(),
        }
    ).named(renames["AggregationIn"])
    types["AggregationOut"] = t.struct(
        {
            "histogram": t.proxy(renames["AggregationHistogramOut"]).optional(),
            "sum": t.proxy(renames["AggregationSumOut"]).optional(),
            "field": t.string().optional(),
            "frequency": t.proxy(renames["AggregationFrequencyOut"]).optional(),
            "count": t.proxy(renames["AggregationCountOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationOut"])
    types["AssetFrameIn"] = t.struct(
        {
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "virtualMachineDetails": t.proxy(
                renames["VirtualMachineDetailsIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "reportTime": t.string().optional(),
            "performanceSamples": t.array(
                t.proxy(renames["PerformanceSampleIn"])
            ).optional(),
            "traceToken": t.string().optional(),
        }
    ).named(renames["AssetFrameIn"])
    types["AssetFrameOut"] = t.struct(
        {
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "virtualMachineDetails": t.proxy(
                renames["VirtualMachineDetailsOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "reportTime": t.string().optional(),
            "performanceSamples": t.array(
                t.proxy(renames["PerformanceSampleOut"])
            ).optional(),
            "traceToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetFrameOut"])
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
    types["InsightIn"] = t.struct({"_": t.string().optional()}).named(
        renames["InsightIn"]
    )
    types["InsightOut"] = t.struct(
        {
            "migrationInsight": t.proxy(renames["MigrationInsightOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsightOut"])
    types["DailyResourceUsageAggregationStatsIn"] = t.struct(
        {
            "peak": t.number().optional(),
            "average": t.number().optional(),
            "median": t.number().optional(),
            "ninteyFifthPercentile": t.number().optional(),
        }
    ).named(renames["DailyResourceUsageAggregationStatsIn"])
    types["DailyResourceUsageAggregationStatsOut"] = t.struct(
        {
            "peak": t.number().optional(),
            "average": t.number().optional(),
            "median": t.number().optional(),
            "ninteyFifthPercentile": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DailyResourceUsageAggregationStatsOut"])
    types["DailyResourceUsageAggregationIn"] = t.struct(
        {
            "disk": t.proxy(renames["DailyResourceUsageAggregationDiskIn"]).optional(),
            "network": t.proxy(
                renames["DailyResourceUsageAggregationNetworkIn"]
            ).optional(),
            "cpu": t.proxy(renames["DailyResourceUsageAggregationCPUIn"]).optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
            "memory": t.proxy(
                renames["DailyResourceUsageAggregationMemoryIn"]
            ).optional(),
        }
    ).named(renames["DailyResourceUsageAggregationIn"])
    types["DailyResourceUsageAggregationOut"] = t.struct(
        {
            "disk": t.proxy(renames["DailyResourceUsageAggregationDiskOut"]).optional(),
            "network": t.proxy(
                renames["DailyResourceUsageAggregationNetworkOut"]
            ).optional(),
            "cpu": t.proxy(renames["DailyResourceUsageAggregationCPUOut"]).optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "memory": t.proxy(
                renames["DailyResourceUsageAggregationMemoryOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DailyResourceUsageAggregationOut"])
    types["AggregationResultFrequencyIn"] = t.struct(
        {"values": t.struct({"_": t.string().optional()})}
    ).named(renames["AggregationResultFrequencyIn"])
    types["AggregationResultFrequencyOut"] = t.struct(
        {
            "values": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationResultFrequencyOut"])
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
    types["AssetIn"] = t.struct(
        {
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["AssetIn"])
    types["AssetOut"] = t.struct(
        {
            "sources": t.array(t.string()).optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "virtualMachineDetails": t.proxy(
                renames["VirtualMachineDetailsOut"]
            ).optional(),
            "assignedGroups": t.array(t.string()).optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "performanceData": t.proxy(renames["AssetPerformanceDataOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "insightList": t.proxy(renames["InsightListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetOut"])
    types["AwsEc2PlatformDetailsIn"] = t.struct(
        {"location": t.string().optional(), "machineTypeLabel": t.string().optional()}
    ).named(renames["AwsEc2PlatformDetailsIn"])
    types["AwsEc2PlatformDetailsOut"] = t.struct(
        {
            "location": t.string().optional(),
            "machineTypeLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AwsEc2PlatformDetailsOut"])
    types["GoogleKubernetesEngineMigrationTargetIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleKubernetesEngineMigrationTargetIn"])
    types["GoogleKubernetesEngineMigrationTargetOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleKubernetesEngineMigrationTargetOut"])
    types["AggregationResultCountIn"] = t.struct({"value": t.string()}).named(
        renames["AggregationResultCountIn"]
    )
    types["AggregationResultCountOut"] = t.struct(
        {"value": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AggregationResultCountOut"])
    types["BatchDeleteAssetsRequestIn"] = t.struct(
        {"allowMissing": t.boolean().optional(), "names": t.array(t.string())}
    ).named(renames["BatchDeleteAssetsRequestIn"])
    types["BatchDeleteAssetsRequestOut"] = t.struct(
        {
            "allowMissing": t.boolean().optional(),
            "names": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeleteAssetsRequestOut"])
    types["ListGroupsResponseIn"] = t.struct(
        {
            "groups": t.array(t.proxy(renames["GroupIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListGroupsResponseIn"])
    types["ListGroupsResponseOut"] = t.struct(
        {
            "groups": t.array(t.proxy(renames["GroupOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGroupsResponseOut"])
    types["ErrorFrameIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ErrorFrameIn"]
    )
    types["ErrorFrameOut"] = t.struct(
        {
            "violations": t.array(
                t.proxy(renames["FrameViolationEntryOut"])
            ).optional(),
            "ingestionTime": t.string().optional(),
            "originalFrame": t.proxy(renames["AssetFrameOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorFrameOut"])
    types["OpenFileListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["OpenFileDetailsIn"])).optional()}
    ).named(renames["OpenFileListIn"])
    types["OpenFileListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["OpenFileDetailsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OpenFileListOut"])
    types["GenericPlatformDetailsIn"] = t.struct(
        {"location": t.string().optional()}
    ).named(renames["GenericPlatformDetailsIn"])
    types["GenericPlatformDetailsOut"] = t.struct(
        {
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenericPlatformDetailsOut"])
    types["VirtualMachineDetailsIn"] = t.struct(
        {
            "vmName": t.string().optional(),
            "memoryMb": t.integer().optional(),
            "osVersion": t.string().optional(),
            "vmNetwork": t.proxy(renames["VirtualMachineNetworkDetailsIn"]).optional(),
            "osName": t.string().optional(),
            "createTime": t.string().optional(),
            "vmDisks": t.proxy(renames["VirtualMachineDiskDetailsIn"]).optional(),
            "osFamily": t.string().optional(),
            "vmArchitecture": t.proxy(
                renames["VirtualMachineArchitectureDetailsIn"]
            ).optional(),
            "powerState": t.string().optional(),
            "guestOs": t.proxy(renames["GuestOsDetailsIn"]).optional(),
            "coreCount": t.integer().optional(),
            "vcenterUrl": t.string().optional(),
            "vcenterFolder": t.string().optional(),
            "vcenterVmId": t.string().optional(),
            "vmUuid": t.string().optional(),
            "platform": t.proxy(renames["PlatformDetailsIn"]).optional(),
        }
    ).named(renames["VirtualMachineDetailsIn"])
    types["VirtualMachineDetailsOut"] = t.struct(
        {
            "vmName": t.string().optional(),
            "memoryMb": t.integer().optional(),
            "osVersion": t.string().optional(),
            "vmNetwork": t.proxy(renames["VirtualMachineNetworkDetailsOut"]).optional(),
            "osName": t.string().optional(),
            "createTime": t.string().optional(),
            "vmDisks": t.proxy(renames["VirtualMachineDiskDetailsOut"]).optional(),
            "osFamily": t.string().optional(),
            "vmArchitecture": t.proxy(
                renames["VirtualMachineArchitectureDetailsOut"]
            ).optional(),
            "powerState": t.string().optional(),
            "guestOs": t.proxy(renames["GuestOsDetailsOut"]).optional(),
            "coreCount": t.integer().optional(),
            "vcenterUrl": t.string().optional(),
            "vcenterFolder": t.string().optional(),
            "vcenterVmId": t.string().optional(),
            "vmUuid": t.string().optional(),
            "platform": t.proxy(renames["PlatformDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualMachineDetailsOut"])
    types["PlatformDetailsIn"] = t.struct(
        {
            "awsEc2Details": t.proxy(renames["AwsEc2PlatformDetailsIn"]).optional(),
            "physicalDetails": t.proxy(renames["PhysicalPlatformDetailsIn"]).optional(),
            "genericDetails": t.proxy(renames["GenericPlatformDetailsIn"]).optional(),
            "vmwareDetails": t.proxy(renames["VmwarePlatformDetailsIn"]).optional(),
            "azureVmDetails": t.proxy(renames["AzureVmPlatformDetailsIn"]).optional(),
        }
    ).named(renames["PlatformDetailsIn"])
    types["PlatformDetailsOut"] = t.struct(
        {
            "awsEc2Details": t.proxy(renames["AwsEc2PlatformDetailsOut"]).optional(),
            "physicalDetails": t.proxy(
                renames["PhysicalPlatformDetailsOut"]
            ).optional(),
            "genericDetails": t.proxy(renames["GenericPlatformDetailsOut"]).optional(),
            "vmwareDetails": t.proxy(renames["VmwarePlatformDetailsOut"]).optional(),
            "azureVmDetails": t.proxy(renames["AzureVmPlatformDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlatformDetailsOut"])
    types["ReportAssetFramesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReportAssetFramesResponseIn"]
    )
    types["ReportAssetFramesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReportAssetFramesResponseOut"])
    types["RemoveAssetsFromGroupRequestIn"] = t.struct(
        {
            "allowMissing": t.boolean().optional(),
            "assets": t.proxy(renames["AssetListIn"]),
            "requestId": t.string().optional(),
        }
    ).named(renames["RemoveAssetsFromGroupRequestIn"])
    types["RemoveAssetsFromGroupRequestOut"] = t.struct(
        {
            "allowMissing": t.boolean().optional(),
            "assets": t.proxy(renames["AssetListOut"]),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveAssetsFromGroupRequestOut"])
    types["AssetListIn"] = t.struct({"assetIds": t.array(t.string())}).named(
        renames["AssetListIn"]
    )
    types["AssetListOut"] = t.struct(
        {
            "assetIds": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetListOut"])
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
    types["ReportSummaryHistogramChartDataBucketIn"] = t.struct(
        {
            "upperBound": t.string().optional(),
            "lowerBound": t.string().optional(),
            "count": t.string().optional(),
        }
    ).named(renames["ReportSummaryHistogramChartDataBucketIn"])
    types["ReportSummaryHistogramChartDataBucketOut"] = t.struct(
        {
            "upperBound": t.string().optional(),
            "lowerBound": t.string().optional(),
            "count": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryHistogramChartDataBucketOut"])
    types["FstabEntryListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["FstabEntryIn"])).optional()}
    ).named(renames["FstabEntryListIn"])
    types["FstabEntryListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["FstabEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FstabEntryListOut"])
    types["DiskEntryIn"] = t.struct(
        {
            "interfaceType": t.string().optional(),
            "vmwareConfig": t.proxy(renames["VmwareDiskConfigIn"]).optional(),
            "diskLabelType": t.string().optional(),
            "hwAddress": t.string().optional(),
            "partitions": t.proxy(renames["DiskPartitionListIn"]).optional(),
            "diskLabel": t.string().optional(),
            "totalCapacityBytes": t.string().optional(),
            "totalFreeBytes": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["DiskEntryIn"])
    types["DiskEntryOut"] = t.struct(
        {
            "interfaceType": t.string().optional(),
            "vmwareConfig": t.proxy(renames["VmwareDiskConfigOut"]).optional(),
            "diskLabelType": t.string().optional(),
            "hwAddress": t.string().optional(),
            "partitions": t.proxy(renames["DiskPartitionListOut"]).optional(),
            "diskLabel": t.string().optional(),
            "totalCapacityBytes": t.string().optional(),
            "totalFreeBytes": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskEntryOut"])
    types["RunningProcessListIn"] = t.struct(
        {"processes": t.array(t.proxy(renames["RunningProcessIn"])).optional()}
    ).named(renames["RunningProcessListIn"])
    types["RunningProcessListOut"] = t.struct(
        {
            "processes": t.array(t.proxy(renames["RunningProcessOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunningProcessListOut"])
    types["ComputeEngineMigrationTargetIn"] = t.struct(
        {"shape": t.proxy(renames["ComputeEngineShapeDescriptorIn"]).optional()}
    ).named(renames["ComputeEngineMigrationTargetIn"])
    types["ComputeEngineMigrationTargetOut"] = t.struct(
        {
            "shape": t.proxy(renames["ComputeEngineShapeDescriptorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeEngineMigrationTargetOut"])
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
    types["VirtualMachineNetworkDetailsIn"] = t.struct(
        {
            "publicIpAddress": t.string().optional(),
            "primaryIpAddress": t.string().optional(),
            "networkAdapters": t.proxy(renames["NetworkAdapterListIn"]).optional(),
            "primaryMacAddress": t.string().optional(),
            "defaultGw": t.string().optional(),
        }
    ).named(renames["VirtualMachineNetworkDetailsIn"])
    types["VirtualMachineNetworkDetailsOut"] = t.struct(
        {
            "publicIpAddress": t.string().optional(),
            "primaryIpAddress": t.string().optional(),
            "networkAdapters": t.proxy(renames["NetworkAdapterListOut"]).optional(),
            "primaryMacAddress": t.string().optional(),
            "defaultGw": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualMachineNetworkDetailsOut"])
    types["ImportErrorIn"] = t.struct(
        {"errorDetails": t.string().optional(), "severity": t.string().optional()}
    ).named(renames["ImportErrorIn"])
    types["ImportErrorOut"] = t.struct(
        {
            "errorDetails": t.string().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportErrorOut"])
    types["NetworkAddressIn"] = t.struct(
        {
            "assignment": t.string().optional(),
            "bcast": t.string().optional(),
            "subnetMask": t.string().optional(),
            "ipAddress": t.string().optional(),
            "fqdn": t.string().optional(),
        }
    ).named(renames["NetworkAddressIn"])
    types["NetworkAddressOut"] = t.struct(
        {
            "assignment": t.string().optional(),
            "bcast": t.string().optional(),
            "subnetMask": t.string().optional(),
            "ipAddress": t.string().optional(),
            "fqdn": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkAddressOut"])
    types["DiskPartitionIn"] = t.struct(
        {
            "capacityBytes": t.string().optional(),
            "uuid": t.string().optional(),
            "subPartitions": t.proxy(renames["DiskPartitionListIn"]).optional(),
            "type": t.string().optional(),
            "freeBytes": t.string().optional(),
            "mountPoint": t.string().optional(),
            "fileSystem": t.string().optional(),
        }
    ).named(renames["DiskPartitionIn"])
    types["DiskPartitionOut"] = t.struct(
        {
            "capacityBytes": t.string().optional(),
            "uuid": t.string().optional(),
            "subPartitions": t.proxy(renames["DiskPartitionListOut"]).optional(),
            "type": t.string().optional(),
            "freeBytes": t.string().optional(),
            "mountPoint": t.string().optional(),
            "fileSystem": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskPartitionOut"])
    types["RegionPreferencesIn"] = t.struct(
        {"preferredRegions": t.array(t.string()).optional()}
    ).named(renames["RegionPreferencesIn"])
    types["RegionPreferencesOut"] = t.struct(
        {
            "preferredRegions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionPreferencesOut"])
    types["ImportDataFileIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "uploadFileInfo": t.proxy(renames["UploadFileInfoIn"]).optional(),
            "format": t.string(),
        }
    ).named(renames["ImportDataFileIn"])
    types["ImportDataFileOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "uploadFileInfo": t.proxy(renames["UploadFileInfoOut"]).optional(),
            "state": t.string().optional(),
            "format": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportDataFileOut"])
    types["DailyResourceUsageAggregationNetworkIn"] = t.struct(
        {
            "ingressBps": t.proxy(
                renames["DailyResourceUsageAggregationStatsIn"]
            ).optional(),
            "egressBps": t.proxy(
                renames["DailyResourceUsageAggregationStatsIn"]
            ).optional(),
        }
    ).named(renames["DailyResourceUsageAggregationNetworkIn"])
    types["DailyResourceUsageAggregationNetworkOut"] = t.struct(
        {
            "ingressBps": t.proxy(
                renames["DailyResourceUsageAggregationStatsOut"]
            ).optional(),
            "egressBps": t.proxy(
                renames["DailyResourceUsageAggregationStatsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DailyResourceUsageAggregationNetworkOut"])
    types["HostsEntryListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["HostsEntryIn"])).optional()}
    ).named(renames["HostsEntryListIn"])
    types["HostsEntryListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["HostsEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HostsEntryListOut"])
    types["ComputeEngineShapeDescriptorIn"] = t.struct(
        {
            "memoryMb": t.integer().optional(),
            "physicalCoreCount": t.integer().optional(),
            "logicalCoreCount": t.integer().optional(),
            "machineType": t.string().optional(),
            "series": t.string().optional(),
        }
    ).named(renames["ComputeEngineShapeDescriptorIn"])
    types["ComputeEngineShapeDescriptorOut"] = t.struct(
        {
            "memoryMb": t.integer().optional(),
            "physicalCoreCount": t.integer().optional(),
            "logicalCoreCount": t.integer().optional(),
            "machineType": t.string().optional(),
            "series": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeEngineShapeDescriptorOut"])
    types["AddAssetsToGroupRequestIn"] = t.struct(
        {
            "requestId": t.string().optional(),
            "allowExisting": t.boolean().optional(),
            "assets": t.proxy(renames["AssetListIn"]),
        }
    ).named(renames["AddAssetsToGroupRequestIn"])
    types["AddAssetsToGroupRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "allowExisting": t.boolean().optional(),
            "assets": t.proxy(renames["AssetListOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddAssetsToGroupRequestOut"])
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
    types["OpenFileDetailsIn"] = t.struct(
        {
            "user": t.string().optional(),
            "filePath": t.string().optional(),
            "command": t.string().optional(),
            "fileType": t.string().optional(),
        }
    ).named(renames["OpenFileDetailsIn"])
    types["OpenFileDetailsOut"] = t.struct(
        {
            "user": t.string().optional(),
            "filePath": t.string().optional(),
            "command": t.string().optional(),
            "fileType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OpenFileDetailsOut"])
    types["GroupIn"] = t.struct(
        {
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
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
    types["ReportConfigGroupPreferenceSetAssignmentIn"] = t.struct(
        {"group": t.string(), "preferenceSet": t.string()}
    ).named(renames["ReportConfigGroupPreferenceSetAssignmentIn"])
    types["ReportConfigGroupPreferenceSetAssignmentOut"] = t.struct(
        {
            "group": t.string(),
            "preferenceSet": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportConfigGroupPreferenceSetAssignmentOut"])
    types["ComputeEnginePreferencesIn"] = t.struct(
        {
            "licenseType": t.string().optional(),
            "machinePreferences": t.proxy(renames["MachinePreferencesIn"]).optional(),
            "persistentDiskType": t.string().optional(),
        }
    ).named(renames["ComputeEnginePreferencesIn"])
    types["ComputeEnginePreferencesOut"] = t.struct(
        {
            "licenseType": t.string().optional(),
            "machinePreferences": t.proxy(renames["MachinePreferencesOut"]).optional(),
            "persistentDiskType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeEnginePreferencesOut"])
    types["NetworkUsageSampleIn"] = t.struct(
        {
            "averageEgressBps": t.number().optional(),
            "averageIngressBps": t.number().optional(),
        }
    ).named(renames["NetworkUsageSampleIn"])
    types["NetworkUsageSampleOut"] = t.struct(
        {
            "averageEgressBps": t.number().optional(),
            "averageIngressBps": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkUsageSampleOut"])
    types["VmwareDiskConfigIn"] = t.struct(
        {
            "vmdkDiskMode": t.string().optional(),
            "rdmCompatibilityMode": t.string().optional(),
            "shared": t.boolean().optional(),
            "backingType": t.string().optional(),
        }
    ).named(renames["VmwareDiskConfigIn"])
    types["VmwareDiskConfigOut"] = t.struct(
        {
            "vmdkDiskMode": t.string().optional(),
            "rdmCompatibilityMode": t.string().optional(),
            "shared": t.boolean().optional(),
            "backingType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareDiskConfigOut"])
    types["GuestRuntimeDetailsIn"] = t.struct(
        {
            "lastUptime": t.proxy(renames["DateIn"]).optional(),
            "domain": t.string().optional(),
            "machineName": t.string().optional(),
            "processes": t.proxy(renames["RunningProcessListIn"]).optional(),
            "networkInfo": t.proxy(renames["RuntimeNetworkInfoIn"]).optional(),
            "services": t.proxy(renames["RunningServiceListIn"]).optional(),
            "openFileList": t.proxy(renames["OpenFileListIn"]).optional(),
            "installedApps": t.proxy(
                renames["GuestInstalledApplicationListIn"]
            ).optional(),
        }
    ).named(renames["GuestRuntimeDetailsIn"])
    types["GuestRuntimeDetailsOut"] = t.struct(
        {
            "lastUptime": t.proxy(renames["DateOut"]).optional(),
            "domain": t.string().optional(),
            "machineName": t.string().optional(),
            "processes": t.proxy(renames["RunningProcessListOut"]).optional(),
            "networkInfo": t.proxy(renames["RuntimeNetworkInfoOut"]).optional(),
            "services": t.proxy(renames["RunningServiceListOut"]).optional(),
            "openFileList": t.proxy(renames["OpenFileListOut"]).optional(),
            "installedApps": t.proxy(
                renames["GuestInstalledApplicationListOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestRuntimeDetailsOut"])
    types["DiskUsageSampleIn"] = t.struct({"averageIops": t.number().optional()}).named(
        renames["DiskUsageSampleIn"]
    )
    types["DiskUsageSampleOut"] = t.struct(
        {
            "averageIops": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskUsageSampleOut"])
    types["ImportRowErrorIn"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["ImportErrorIn"])).optional(),
            "vmUuid": t.string().optional(),
            "rowNumber": t.integer().optional(),
            "vmName": t.string().optional(),
        }
    ).named(renames["ImportRowErrorIn"])
    types["ImportRowErrorOut"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["ImportErrorOut"])).optional(),
            "vmUuid": t.string().optional(),
            "rowNumber": t.integer().optional(),
            "vmName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportRowErrorOut"])
    types["BatchUpdateAssetsResponseIn"] = t.struct(
        {"assets": t.array(t.proxy(renames["AssetIn"])).optional()}
    ).named(renames["BatchUpdateAssetsResponseIn"])
    types["BatchUpdateAssetsResponseOut"] = t.struct(
        {
            "assets": t.array(t.proxy(renames["AssetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateAssetsResponseOut"])
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
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["ListAssetsResponseIn"] = t.struct(
        {
            "assets": t.array(t.proxy(renames["AssetIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAssetsResponseIn"])
    types["ListAssetsResponseOut"] = t.struct(
        {
            "assets": t.array(t.proxy(renames["AssetOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAssetsResponseOut"])
    types["RunningProcessIn"] = t.struct(
        {
            "pid": t.string().optional(),
            "user": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "exePath": t.string().optional(),
            "cmdline": t.string().optional(),
        }
    ).named(renames["RunningProcessIn"])
    types["RunningProcessOut"] = t.struct(
        {
            "pid": t.string().optional(),
            "user": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "exePath": t.string().optional(),
            "cmdline": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunningProcessOut"])
    types["PreferenceSetIn"] = t.struct(
        {
            "virtualMachinePreferences": t.proxy(
                renames["VirtualMachinePreferencesIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["PreferenceSetIn"])
    types["PreferenceSetOut"] = t.struct(
        {
            "virtualMachinePreferences": t.proxy(
                renames["VirtualMachinePreferencesOut"]
            ).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PreferenceSetOut"])
    types["ListImportDataFilesResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "importDataFiles": t.array(t.proxy(renames["ImportDataFileIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListImportDataFilesResponseIn"])
    types["ListImportDataFilesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "importDataFiles": t.array(
                t.proxy(renames["ImportDataFileOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListImportDataFilesResponseOut"])
    types["AggregationFrequencyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AggregationFrequencyIn"]
    )
    types["AggregationFrequencyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AggregationFrequencyOut"])
    types["RunImportJobRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["RunImportJobRequestIn"])
    types["RunImportJobRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunImportJobRequestOut"])
    types["AggregationHistogramIn"] = t.struct(
        {"lowerBounds": t.array(t.number()).optional()}
    ).named(renames["AggregationHistogramIn"])
    types["AggregationHistogramOut"] = t.struct(
        {
            "lowerBounds": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationHistogramOut"])
    types["SelinuxIn"] = t.struct(
        {"mode": t.string().optional(), "enabled": t.boolean().optional()}
    ).named(renames["SelinuxIn"])
    types["SelinuxOut"] = t.struct(
        {
            "mode": t.string().optional(),
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SelinuxOut"])
    types["ReportSummaryGroupPreferenceSetFindingIn"] = t.struct(
        {
            "description": t.string().optional(),
            "monthlyCostOsLicense": t.proxy(renames["MoneyIn"]).optional(),
            "monthlyCostTotal": t.proxy(renames["MoneyIn"]).optional(),
            "monthlyCostOther": t.proxy(renames["MoneyIn"]).optional(),
            "monthlyCostCompute": t.proxy(renames["MoneyIn"]).optional(),
            "monthlyCostStorage": t.proxy(renames["MoneyIn"]).optional(),
            "monthlyCostNetworkEgress": t.proxy(renames["MoneyIn"]).optional(),
            "displayName": t.string().optional(),
            "machinePreferences": t.proxy(
                renames["VirtualMachinePreferencesIn"]
            ).optional(),
            "topPriority": t.string().optional(),
            "pricingTrack": t.string().optional(),
            "machineFinding": t.proxy(
                renames["ReportSummaryMachineFindingIn"]
            ).optional(),
            "preferredRegion": t.string().optional(),
        }
    ).named(renames["ReportSummaryGroupPreferenceSetFindingIn"])
    types["ReportSummaryGroupPreferenceSetFindingOut"] = t.struct(
        {
            "description": t.string().optional(),
            "monthlyCostOsLicense": t.proxy(renames["MoneyOut"]).optional(),
            "monthlyCostTotal": t.proxy(renames["MoneyOut"]).optional(),
            "monthlyCostOther": t.proxy(renames["MoneyOut"]).optional(),
            "monthlyCostCompute": t.proxy(renames["MoneyOut"]).optional(),
            "monthlyCostStorage": t.proxy(renames["MoneyOut"]).optional(),
            "monthlyCostNetworkEgress": t.proxy(renames["MoneyOut"]).optional(),
            "displayName": t.string().optional(),
            "machinePreferences": t.proxy(
                renames["VirtualMachinePreferencesOut"]
            ).optional(),
            "topPriority": t.string().optional(),
            "pricingTrack": t.string().optional(),
            "machineFinding": t.proxy(
                renames["ReportSummaryMachineFindingOut"]
            ).optional(),
            "preferredRegion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryGroupPreferenceSetFindingOut"])
    types["ReportSummaryGroupFindingIn"] = t.struct(
        {
            "assetAggregateStats": t.proxy(
                renames["ReportSummaryAssetAggregateStatsIn"]
            ).optional(),
            "preferenceSetFindings": t.array(
                t.proxy(renames["ReportSummaryGroupPreferenceSetFindingIn"])
            ).optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "overlappingAssetCount": t.string().optional(),
        }
    ).named(renames["ReportSummaryGroupFindingIn"])
    types["ReportSummaryGroupFindingOut"] = t.struct(
        {
            "assetAggregateStats": t.proxy(
                renames["ReportSummaryAssetAggregateStatsOut"]
            ).optional(),
            "preferenceSetFindings": t.array(
                t.proxy(renames["ReportSummaryGroupPreferenceSetFindingOut"])
            ).optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "overlappingAssetCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryGroupFindingOut"])
    types["NetworkAddressListIn"] = t.struct(
        {"addresses": t.array(t.proxy(renames["NetworkAddressIn"])).optional()}
    ).named(renames["NetworkAddressListIn"])
    types["NetworkAddressListOut"] = t.struct(
        {
            "addresses": t.array(t.proxy(renames["NetworkAddressOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkAddressListOut"])
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
    types["DiskEntryListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["DiskEntryIn"])).optional()}
    ).named(renames["DiskEntryListIn"])
    types["DiskEntryListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["DiskEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskEntryListOut"])
    types["VmwarePlatformDetailsIn"] = t.struct(
        {
            "osid": t.string().optional(),
            "vcenterVersion": t.string().optional(),
            "esxVersion": t.string().optional(),
        }
    ).named(renames["VmwarePlatformDetailsIn"])
    types["VmwarePlatformDetailsOut"] = t.struct(
        {
            "osid": t.string().optional(),
            "vcenterVersion": t.string().optional(),
            "esxVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwarePlatformDetailsOut"])
    types["MemoryUsageSampleIn"] = t.struct(
        {"utilizedPercentage": t.number().optional()}
    ).named(renames["MemoryUsageSampleIn"])
    types["MemoryUsageSampleOut"] = t.struct(
        {
            "utilizedPercentage": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemoryUsageSampleOut"])
    types["AggregationCountIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AggregationCountIn"]
    )
    types["AggregationCountOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AggregationCountOut"])
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
    types["VirtualMachineArchitectureDetailsIn"] = t.struct(
        {
            "cpuManufacturer": t.string().optional(),
            "vendor": t.string().optional(),
            "cpuName": t.string().optional(),
            "hyperthreading": t.string().optional(),
            "cpuArchitecture": t.string().optional(),
            "cpuSocketCount": t.integer().optional(),
            "cpuThreadCount": t.integer().optional(),
            "bios": t.proxy(renames["BiosDetailsIn"]).optional(),
            "firmware": t.string().optional(),
        }
    ).named(renames["VirtualMachineArchitectureDetailsIn"])
    types["VirtualMachineArchitectureDetailsOut"] = t.struct(
        {
            "cpuManufacturer": t.string().optional(),
            "vendor": t.string().optional(),
            "cpuName": t.string().optional(),
            "hyperthreading": t.string().optional(),
            "cpuArchitecture": t.string().optional(),
            "cpuSocketCount": t.integer().optional(),
            "cpuThreadCount": t.integer().optional(),
            "bios": t.proxy(renames["BiosDetailsOut"]).optional(),
            "firmware": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualMachineArchitectureDetailsOut"])
    types["TimeZoneIn"] = t.struct(
        {"id": t.string().optional(), "version": t.string().optional()}
    ).named(renames["TimeZoneIn"])
    types["TimeZoneOut"] = t.struct(
        {
            "id": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeZoneOut"])

    functions = {}
    functions["projectsLocationsGet"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsUpdateSettings"] = migrationcenter.get(
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
    functions["projectsLocationsAssetsList"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsDelete"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsBatchDelete"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsReportAssetFrames"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsAggregateValues"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsBatchUpdate"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsPatch"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsGet"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsDelete"] = migrationcenter.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsAddAssets"] = migrationcenter.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsGet"] = migrationcenter.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsList"] = migrationcenter.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsCreate"] = migrationcenter.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsRemoveAssets"] = migrationcenter.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsPatch"] = migrationcenter.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPreferenceSetsCreate"] = migrationcenter.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string(),
                "name": t.string().optional(),
                "virtualMachinePreferences": t.proxy(
                    renames["VirtualMachinePreferencesIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPreferenceSetsGet"] = migrationcenter.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string(),
                "name": t.string().optional(),
                "virtualMachinePreferences": t.proxy(
                    renames["VirtualMachinePreferencesIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPreferenceSetsList"] = migrationcenter.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string(),
                "name": t.string().optional(),
                "virtualMachinePreferences": t.proxy(
                    renames["VirtualMachinePreferencesIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPreferenceSetsDelete"] = migrationcenter.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string(),
                "name": t.string().optional(),
                "virtualMachinePreferences": t.proxy(
                    renames["VirtualMachinePreferencesIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPreferenceSetsPatch"] = migrationcenter.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string(),
                "name": t.string().optional(),
                "virtualMachinePreferences": t.proxy(
                    renames["VirtualMachinePreferencesIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = migrationcenter.post(
        "v1alpha1/{name}:cancel",
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
    functions["projectsLocationsOperationsList"] = migrationcenter.post(
        "v1alpha1/{name}:cancel",
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
    functions["projectsLocationsOperationsGet"] = migrationcenter.post(
        "v1alpha1/{name}:cancel",
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
    functions["projectsLocationsOperationsCancel"] = migrationcenter.post(
        "v1alpha1/{name}:cancel",
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
        "projectsLocationsImportJobsImportDataFilesCreate"
    ] = migrationcenter.delete(
        "v1alpha1/{name}",
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
    functions["projectsLocationsImportJobsImportDataFilesGet"] = migrationcenter.delete(
        "v1alpha1/{name}",
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
        "projectsLocationsImportJobsImportDataFilesList"
    ] = migrationcenter.delete(
        "v1alpha1/{name}",
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
    ] = migrationcenter.delete(
        "v1alpha1/{name}",
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
    functions["projectsLocationsReportConfigsCreate"] = migrationcenter.delete(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReportConfigsGet"] = migrationcenter.delete(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReportConfigsList"] = migrationcenter.delete(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReportConfigsDelete"] = migrationcenter.delete(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReportConfigsReportsList"] = migrationcenter.delete(
        "v1alpha1/{name}",
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
    functions["projectsLocationsReportConfigsReportsCreate"] = migrationcenter.delete(
        "v1alpha1/{name}",
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
    functions["projectsLocationsReportConfigsReportsGet"] = migrationcenter.delete(
        "v1alpha1/{name}",
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
    functions["projectsLocationsReportConfigsReportsDelete"] = migrationcenter.delete(
        "v1alpha1/{name}",
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
    functions["projectsLocationsSourcesGet"] = migrationcenter.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "requestId": t.string().optional(),
                "description": t.string().optional(),
                "type": t.string().optional(),
                "displayName": t.string().optional(),
                "isManaged": t.boolean().optional(),
                "priority": t.integer().optional(),
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
                "updateMask": t.string(),
                "name": t.string().optional(),
                "requestId": t.string().optional(),
                "description": t.string().optional(),
                "type": t.string().optional(),
                "displayName": t.string().optional(),
                "isManaged": t.boolean().optional(),
                "priority": t.integer().optional(),
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
                "updateMask": t.string(),
                "name": t.string().optional(),
                "requestId": t.string().optional(),
                "description": t.string().optional(),
                "type": t.string().optional(),
                "displayName": t.string().optional(),
                "isManaged": t.boolean().optional(),
                "priority": t.integer().optional(),
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
                "updateMask": t.string(),
                "name": t.string().optional(),
                "requestId": t.string().optional(),
                "description": t.string().optional(),
                "type": t.string().optional(),
                "displayName": t.string().optional(),
                "isManaged": t.boolean().optional(),
                "priority": t.integer().optional(),
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
                "updateMask": t.string(),
                "name": t.string().optional(),
                "requestId": t.string().optional(),
                "description": t.string().optional(),
                "type": t.string().optional(),
                "displayName": t.string().optional(),
                "isManaged": t.boolean().optional(),
                "priority": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesErrorFramesList"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ErrorFrameOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesErrorFramesGet"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ErrorFrameOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="migrationcenter",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
