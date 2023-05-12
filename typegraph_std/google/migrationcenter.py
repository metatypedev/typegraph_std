from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_migrationcenter() -> Import:
    migrationcenter = HTTPRuntime("https://migrationcenter.googleapis.com/")

    renames = {
        "ErrorResponse": "_migrationcenter_1_ErrorResponse",
        "AddAssetsToGroupRequestIn": "_migrationcenter_2_AddAssetsToGroupRequestIn",
        "AddAssetsToGroupRequestOut": "_migrationcenter_3_AddAssetsToGroupRequestOut",
        "ValidateImportJobRequestIn": "_migrationcenter_4_ValidateImportJobRequestIn",
        "ValidateImportJobRequestOut": "_migrationcenter_5_ValidateImportJobRequestOut",
        "ImportRowErrorIn": "_migrationcenter_6_ImportRowErrorIn",
        "ImportRowErrorOut": "_migrationcenter_7_ImportRowErrorOut",
        "VirtualMachinePreferencesIn": "_migrationcenter_8_VirtualMachinePreferencesIn",
        "VirtualMachinePreferencesOut": "_migrationcenter_9_VirtualMachinePreferencesOut",
        "DateIn": "_migrationcenter_10_DateIn",
        "DateOut": "_migrationcenter_11_DateOut",
        "NetworkAddressListIn": "_migrationcenter_12_NetworkAddressListIn",
        "NetworkAddressListOut": "_migrationcenter_13_NetworkAddressListOut",
        "ListSourcesResponseIn": "_migrationcenter_14_ListSourcesResponseIn",
        "ListSourcesResponseOut": "_migrationcenter_15_ListSourcesResponseOut",
        "InsightIn": "_migrationcenter_16_InsightIn",
        "InsightOut": "_migrationcenter_17_InsightOut",
        "ReportSummaryHistogramChartDataIn": "_migrationcenter_18_ReportSummaryHistogramChartDataIn",
        "ReportSummaryHistogramChartDataOut": "_migrationcenter_19_ReportSummaryHistogramChartDataOut",
        "VirtualMachineDiskDetailsIn": "_migrationcenter_20_VirtualMachineDiskDetailsIn",
        "VirtualMachineDiskDetailsOut": "_migrationcenter_21_VirtualMachineDiskDetailsOut",
        "ReportAssetFramesResponseIn": "_migrationcenter_22_ReportAssetFramesResponseIn",
        "ReportAssetFramesResponseOut": "_migrationcenter_23_ReportAssetFramesResponseOut",
        "AggregationResultHistogramIn": "_migrationcenter_24_AggregationResultHistogramIn",
        "AggregationResultHistogramOut": "_migrationcenter_25_AggregationResultHistogramOut",
        "FstabEntryListIn": "_migrationcenter_26_FstabEntryListIn",
        "FstabEntryListOut": "_migrationcenter_27_FstabEntryListOut",
        "VirtualMachineDetailsIn": "_migrationcenter_28_VirtualMachineDetailsIn",
        "VirtualMachineDetailsOut": "_migrationcenter_29_VirtualMachineDetailsOut",
        "BatchUpdateAssetsRequestIn": "_migrationcenter_30_BatchUpdateAssetsRequestIn",
        "BatchUpdateAssetsRequestOut": "_migrationcenter_31_BatchUpdateAssetsRequestOut",
        "RunningProcessListIn": "_migrationcenter_32_RunningProcessListIn",
        "RunningProcessListOut": "_migrationcenter_33_RunningProcessListOut",
        "AzureVmPlatformDetailsIn": "_migrationcenter_34_AzureVmPlatformDetailsIn",
        "AzureVmPlatformDetailsOut": "_migrationcenter_35_AzureVmPlatformDetailsOut",
        "MachineSeriesIn": "_migrationcenter_36_MachineSeriesIn",
        "MachineSeriesOut": "_migrationcenter_37_MachineSeriesOut",
        "AggregationCountIn": "_migrationcenter_38_AggregationCountIn",
        "AggregationCountOut": "_migrationcenter_39_AggregationCountOut",
        "OperationIn": "_migrationcenter_40_OperationIn",
        "OperationOut": "_migrationcenter_41_OperationOut",
        "DailyResourceUsageAggregationNetworkIn": "_migrationcenter_42_DailyResourceUsageAggregationNetworkIn",
        "DailyResourceUsageAggregationNetworkOut": "_migrationcenter_43_DailyResourceUsageAggregationNetworkOut",
        "AggregationSumIn": "_migrationcenter_44_AggregationSumIn",
        "AggregationSumOut": "_migrationcenter_45_AggregationSumOut",
        "ReportSummaryUtilizationChartDataIn": "_migrationcenter_46_ReportSummaryUtilizationChartDataIn",
        "ReportSummaryUtilizationChartDataOut": "_migrationcenter_47_ReportSummaryUtilizationChartDataOut",
        "ImportJobIn": "_migrationcenter_48_ImportJobIn",
        "ImportJobOut": "_migrationcenter_49_ImportJobOut",
        "UploadFileInfoIn": "_migrationcenter_50_UploadFileInfoIn",
        "UploadFileInfoOut": "_migrationcenter_51_UploadFileInfoOut",
        "GuestConfigDetailsIn": "_migrationcenter_52_GuestConfigDetailsIn",
        "GuestConfigDetailsOut": "_migrationcenter_53_GuestConfigDetailsOut",
        "DiskUsageSampleIn": "_migrationcenter_54_DiskUsageSampleIn",
        "DiskUsageSampleOut": "_migrationcenter_55_DiskUsageSampleOut",
        "NetworkAdapterDetailsIn": "_migrationcenter_56_NetworkAdapterDetailsIn",
        "NetworkAdapterDetailsOut": "_migrationcenter_57_NetworkAdapterDetailsOut",
        "AggregateAssetsValuesResponseIn": "_migrationcenter_58_AggregateAssetsValuesResponseIn",
        "AggregateAssetsValuesResponseOut": "_migrationcenter_59_AggregateAssetsValuesResponseOut",
        "ComputeEnginePreferencesIn": "_migrationcenter_60_ComputeEnginePreferencesIn",
        "ComputeEnginePreferencesOut": "_migrationcenter_61_ComputeEnginePreferencesOut",
        "ListLocationsResponseIn": "_migrationcenter_62_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_migrationcenter_63_ListLocationsResponseOut",
        "DailyResourceUsageAggregationStatsIn": "_migrationcenter_64_DailyResourceUsageAggregationStatsIn",
        "DailyResourceUsageAggregationStatsOut": "_migrationcenter_65_DailyResourceUsageAggregationStatsOut",
        "ListErrorFramesResponseIn": "_migrationcenter_66_ListErrorFramesResponseIn",
        "ListErrorFramesResponseOut": "_migrationcenter_67_ListErrorFramesResponseOut",
        "HostsEntryIn": "_migrationcenter_68_HostsEntryIn",
        "HostsEntryOut": "_migrationcenter_69_HostsEntryOut",
        "NetworkUsageSampleIn": "_migrationcenter_70_NetworkUsageSampleIn",
        "NetworkUsageSampleOut": "_migrationcenter_71_NetworkUsageSampleOut",
        "VirtualMachineArchitectureDetailsIn": "_migrationcenter_72_VirtualMachineArchitectureDetailsIn",
        "VirtualMachineArchitectureDetailsOut": "_migrationcenter_73_VirtualMachineArchitectureDetailsOut",
        "InlinePayloadInfoIn": "_migrationcenter_74_InlinePayloadInfoIn",
        "InlinePayloadInfoOut": "_migrationcenter_75_InlinePayloadInfoOut",
        "ReportSummaryChartDataIn": "_migrationcenter_76_ReportSummaryChartDataIn",
        "ReportSummaryChartDataOut": "_migrationcenter_77_ReportSummaryChartDataOut",
        "LocationIn": "_migrationcenter_78_LocationIn",
        "LocationOut": "_migrationcenter_79_LocationOut",
        "AggregationIn": "_migrationcenter_80_AggregationIn",
        "AggregationOut": "_migrationcenter_81_AggregationOut",
        "NfsExportListIn": "_migrationcenter_82_NfsExportListIn",
        "NfsExportListOut": "_migrationcenter_83_NfsExportListOut",
        "OpenFileListIn": "_migrationcenter_84_OpenFileListIn",
        "OpenFileListOut": "_migrationcenter_85_OpenFileListOut",
        "AggregationResultHistogramBucketIn": "_migrationcenter_86_AggregationResultHistogramBucketIn",
        "AggregationResultHistogramBucketOut": "_migrationcenter_87_AggregationResultHistogramBucketOut",
        "DiskEntryListIn": "_migrationcenter_88_DiskEntryListIn",
        "DiskEntryListOut": "_migrationcenter_89_DiskEntryListOut",
        "AggregationResultFrequencyIn": "_migrationcenter_90_AggregationResultFrequencyIn",
        "AggregationResultFrequencyOut": "_migrationcenter_91_AggregationResultFrequencyOut",
        "FileValidationReportIn": "_migrationcenter_92_FileValidationReportIn",
        "FileValidationReportOut": "_migrationcenter_93_FileValidationReportOut",
        "AssetListIn": "_migrationcenter_94_AssetListIn",
        "AssetListOut": "_migrationcenter_95_AssetListOut",
        "TimeZoneIn": "_migrationcenter_96_TimeZoneIn",
        "TimeZoneOut": "_migrationcenter_97_TimeZoneOut",
        "VmwarePlatformDetailsIn": "_migrationcenter_98_VmwarePlatformDetailsIn",
        "VmwarePlatformDetailsOut": "_migrationcenter_99_VmwarePlatformDetailsOut",
        "RunningServiceListIn": "_migrationcenter_100_RunningServiceListIn",
        "RunningServiceListOut": "_migrationcenter_101_RunningServiceListOut",
        "NetworkConnectionIn": "_migrationcenter_102_NetworkConnectionIn",
        "NetworkConnectionOut": "_migrationcenter_103_NetworkConnectionOut",
        "CancelOperationRequestIn": "_migrationcenter_104_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_migrationcenter_105_CancelOperationRequestOut",
        "DiskPartitionIn": "_migrationcenter_106_DiskPartitionIn",
        "DiskPartitionOut": "_migrationcenter_107_DiskPartitionOut",
        "BatchUpdateAssetsResponseIn": "_migrationcenter_108_BatchUpdateAssetsResponseIn",
        "BatchUpdateAssetsResponseOut": "_migrationcenter_109_BatchUpdateAssetsResponseOut",
        "HostsEntryListIn": "_migrationcenter_110_HostsEntryListIn",
        "HostsEntryListOut": "_migrationcenter_111_HostsEntryListOut",
        "UpdateAssetRequestIn": "_migrationcenter_112_UpdateAssetRequestIn",
        "UpdateAssetRequestOut": "_migrationcenter_113_UpdateAssetRequestOut",
        "SettingsIn": "_migrationcenter_114_SettingsIn",
        "SettingsOut": "_migrationcenter_115_SettingsOut",
        "ReportSummaryHistogramChartDataBucketIn": "_migrationcenter_116_ReportSummaryHistogramChartDataBucketIn",
        "ReportSummaryHistogramChartDataBucketOut": "_migrationcenter_117_ReportSummaryHistogramChartDataBucketOut",
        "ListAssetsResponseIn": "_migrationcenter_118_ListAssetsResponseIn",
        "ListAssetsResponseOut": "_migrationcenter_119_ListAssetsResponseOut",
        "ImportErrorIn": "_migrationcenter_120_ImportErrorIn",
        "ImportErrorOut": "_migrationcenter_121_ImportErrorOut",
        "StatusIn": "_migrationcenter_122_StatusIn",
        "StatusOut": "_migrationcenter_123_StatusOut",
        "ListReportsResponseIn": "_migrationcenter_124_ListReportsResponseIn",
        "ListReportsResponseOut": "_migrationcenter_125_ListReportsResponseOut",
        "ListImportJobsResponseIn": "_migrationcenter_126_ListImportJobsResponseIn",
        "ListImportJobsResponseOut": "_migrationcenter_127_ListImportJobsResponseOut",
        "AwsEc2PlatformDetailsIn": "_migrationcenter_128_AwsEc2PlatformDetailsIn",
        "AwsEc2PlatformDetailsOut": "_migrationcenter_129_AwsEc2PlatformDetailsOut",
        "PreferenceSetIn": "_migrationcenter_130_PreferenceSetIn",
        "PreferenceSetOut": "_migrationcenter_131_PreferenceSetOut",
        "GuestInstalledApplicationIn": "_migrationcenter_132_GuestInstalledApplicationIn",
        "GuestInstalledApplicationOut": "_migrationcenter_133_GuestInstalledApplicationOut",
        "ReportSummaryAssetAggregateStatsIn": "_migrationcenter_134_ReportSummaryAssetAggregateStatsIn",
        "ReportSummaryAssetAggregateStatsOut": "_migrationcenter_135_ReportSummaryAssetAggregateStatsOut",
        "InsightListIn": "_migrationcenter_136_InsightListIn",
        "InsightListOut": "_migrationcenter_137_InsightListOut",
        "ReportConfigIn": "_migrationcenter_138_ReportConfigIn",
        "ReportConfigOut": "_migrationcenter_139_ReportConfigOut",
        "FitDescriptorIn": "_migrationcenter_140_FitDescriptorIn",
        "FitDescriptorOut": "_migrationcenter_141_FitDescriptorOut",
        "VmwareDiskConfigIn": "_migrationcenter_142_VmwareDiskConfigIn",
        "VmwareDiskConfigOut": "_migrationcenter_143_VmwareDiskConfigOut",
        "GuestInstalledApplicationListIn": "_migrationcenter_144_GuestInstalledApplicationListIn",
        "GuestInstalledApplicationListOut": "_migrationcenter_145_GuestInstalledApplicationListOut",
        "AggregationFrequencyIn": "_migrationcenter_146_AggregationFrequencyIn",
        "AggregationFrequencyOut": "_migrationcenter_147_AggregationFrequencyOut",
        "BiosDetailsIn": "_migrationcenter_148_BiosDetailsIn",
        "BiosDetailsOut": "_migrationcenter_149_BiosDetailsOut",
        "GroupIn": "_migrationcenter_150_GroupIn",
        "GroupOut": "_migrationcenter_151_GroupOut",
        "ExecutionReportIn": "_migrationcenter_152_ExecutionReportIn",
        "ExecutionReportOut": "_migrationcenter_153_ExecutionReportOut",
        "DailyResourceUsageAggregationIn": "_migrationcenter_154_DailyResourceUsageAggregationIn",
        "DailyResourceUsageAggregationOut": "_migrationcenter_155_DailyResourceUsageAggregationOut",
        "GoogleKubernetesEngineMigrationTargetIn": "_migrationcenter_156_GoogleKubernetesEngineMigrationTargetIn",
        "GoogleKubernetesEngineMigrationTargetOut": "_migrationcenter_157_GoogleKubernetesEngineMigrationTargetOut",
        "AssetFrameIn": "_migrationcenter_158_AssetFrameIn",
        "AssetFrameOut": "_migrationcenter_159_AssetFrameOut",
        "ListImportDataFilesResponseIn": "_migrationcenter_160_ListImportDataFilesResponseIn",
        "ListImportDataFilesResponseOut": "_migrationcenter_161_ListImportDataFilesResponseOut",
        "OperationMetadataIn": "_migrationcenter_162_OperationMetadataIn",
        "OperationMetadataOut": "_migrationcenter_163_OperationMetadataOut",
        "ListGroupsResponseIn": "_migrationcenter_164_ListGroupsResponseIn",
        "ListGroupsResponseOut": "_migrationcenter_165_ListGroupsResponseOut",
        "ReportSummaryGroupFindingIn": "_migrationcenter_166_ReportSummaryGroupFindingIn",
        "ReportSummaryGroupFindingOut": "_migrationcenter_167_ReportSummaryGroupFindingOut",
        "DailyResourceUsageAggregationDiskIn": "_migrationcenter_168_DailyResourceUsageAggregationDiskIn",
        "DailyResourceUsageAggregationDiskOut": "_migrationcenter_169_DailyResourceUsageAggregationDiskOut",
        "ReportSummaryIn": "_migrationcenter_170_ReportSummaryIn",
        "ReportSummaryOut": "_migrationcenter_171_ReportSummaryOut",
        "MachinePreferencesIn": "_migrationcenter_172_MachinePreferencesIn",
        "MachinePreferencesOut": "_migrationcenter_173_MachinePreferencesOut",
        "DateTimeIn": "_migrationcenter_174_DateTimeIn",
        "DateTimeOut": "_migrationcenter_175_DateTimeOut",
        "DiskPartitionListIn": "_migrationcenter_176_DiskPartitionListIn",
        "DiskPartitionListOut": "_migrationcenter_177_DiskPartitionListOut",
        "DailyResourceUsageAggregationMemoryIn": "_migrationcenter_178_DailyResourceUsageAggregationMemoryIn",
        "DailyResourceUsageAggregationMemoryOut": "_migrationcenter_179_DailyResourceUsageAggregationMemoryOut",
        "RunImportJobRequestIn": "_migrationcenter_180_RunImportJobRequestIn",
        "RunImportJobRequestOut": "_migrationcenter_181_RunImportJobRequestOut",
        "MoneyIn": "_migrationcenter_182_MoneyIn",
        "MoneyOut": "_migrationcenter_183_MoneyOut",
        "ListReportConfigsResponseIn": "_migrationcenter_184_ListReportConfigsResponseIn",
        "ListReportConfigsResponseOut": "_migrationcenter_185_ListReportConfigsResponseOut",
        "ReportSummaryChartDataDataPointIn": "_migrationcenter_186_ReportSummaryChartDataDataPointIn",
        "ReportSummaryChartDataDataPointOut": "_migrationcenter_187_ReportSummaryChartDataDataPointOut",
        "FramesIn": "_migrationcenter_188_FramesIn",
        "FramesOut": "_migrationcenter_189_FramesOut",
        "RunningProcessIn": "_migrationcenter_190_RunningProcessIn",
        "RunningProcessOut": "_migrationcenter_191_RunningProcessOut",
        "AggregationResultCountIn": "_migrationcenter_192_AggregationResultCountIn",
        "AggregationResultCountOut": "_migrationcenter_193_AggregationResultCountOut",
        "SelinuxIn": "_migrationcenter_194_SelinuxIn",
        "SelinuxOut": "_migrationcenter_195_SelinuxOut",
        "FrameViolationEntryIn": "_migrationcenter_196_FrameViolationEntryIn",
        "FrameViolationEntryOut": "_migrationcenter_197_FrameViolationEntryOut",
        "PerformanceSampleIn": "_migrationcenter_198_PerformanceSampleIn",
        "PerformanceSampleOut": "_migrationcenter_199_PerformanceSampleOut",
        "ReportSummaryMachineFindingIn": "_migrationcenter_200_ReportSummaryMachineFindingIn",
        "ReportSummaryMachineFindingOut": "_migrationcenter_201_ReportSummaryMachineFindingOut",
        "ReportSummaryGroupPreferenceSetFindingIn": "_migrationcenter_202_ReportSummaryGroupPreferenceSetFindingIn",
        "ReportSummaryGroupPreferenceSetFindingOut": "_migrationcenter_203_ReportSummaryGroupPreferenceSetFindingOut",
        "GuestRuntimeDetailsIn": "_migrationcenter_204_GuestRuntimeDetailsIn",
        "GuestRuntimeDetailsOut": "_migrationcenter_205_GuestRuntimeDetailsOut",
        "RunningServiceIn": "_migrationcenter_206_RunningServiceIn",
        "RunningServiceOut": "_migrationcenter_207_RunningServiceOut",
        "SourceIn": "_migrationcenter_208_SourceIn",
        "SourceOut": "_migrationcenter_209_SourceOut",
        "VirtualMachineNetworkDetailsIn": "_migrationcenter_210_VirtualMachineNetworkDetailsIn",
        "VirtualMachineNetworkDetailsOut": "_migrationcenter_211_VirtualMachineNetworkDetailsOut",
        "NfsExportIn": "_migrationcenter_212_NfsExportIn",
        "NfsExportOut": "_migrationcenter_213_NfsExportOut",
        "GCSPayloadInfoIn": "_migrationcenter_214_GCSPayloadInfoIn",
        "GCSPayloadInfoOut": "_migrationcenter_215_GCSPayloadInfoOut",
        "ErrorFrameIn": "_migrationcenter_216_ErrorFrameIn",
        "ErrorFrameOut": "_migrationcenter_217_ErrorFrameOut",
        "AggregationResultSumIn": "_migrationcenter_218_AggregationResultSumIn",
        "AggregationResultSumOut": "_migrationcenter_219_AggregationResultSumOut",
        "ValidationReportIn": "_migrationcenter_220_ValidationReportIn",
        "ValidationReportOut": "_migrationcenter_221_ValidationReportOut",
        "CpuUsageSampleIn": "_migrationcenter_222_CpuUsageSampleIn",
        "CpuUsageSampleOut": "_migrationcenter_223_CpuUsageSampleOut",
        "OpenFileDetailsIn": "_migrationcenter_224_OpenFileDetailsIn",
        "OpenFileDetailsOut": "_migrationcenter_225_OpenFileDetailsOut",
        "DailyResourceUsageAggregationCPUIn": "_migrationcenter_226_DailyResourceUsageAggregationCPUIn",
        "DailyResourceUsageAggregationCPUOut": "_migrationcenter_227_DailyResourceUsageAggregationCPUOut",
        "ListPreferenceSetsResponseIn": "_migrationcenter_228_ListPreferenceSetsResponseIn",
        "ListPreferenceSetsResponseOut": "_migrationcenter_229_ListPreferenceSetsResponseOut",
        "ComputeEngineMigrationTargetIn": "_migrationcenter_230_ComputeEngineMigrationTargetIn",
        "ComputeEngineMigrationTargetOut": "_migrationcenter_231_ComputeEngineMigrationTargetOut",
        "ReportSummaryMachineSeriesAllocationIn": "_migrationcenter_232_ReportSummaryMachineSeriesAllocationIn",
        "ReportSummaryMachineSeriesAllocationOut": "_migrationcenter_233_ReportSummaryMachineSeriesAllocationOut",
        "NetworkAddressIn": "_migrationcenter_234_NetworkAddressIn",
        "NetworkAddressOut": "_migrationcenter_235_NetworkAddressOut",
        "PayloadFileIn": "_migrationcenter_236_PayloadFileIn",
        "PayloadFileOut": "_migrationcenter_237_PayloadFileOut",
        "MigrationInsightIn": "_migrationcenter_238_MigrationInsightIn",
        "MigrationInsightOut": "_migrationcenter_239_MigrationInsightOut",
        "EmptyIn": "_migrationcenter_240_EmptyIn",
        "EmptyOut": "_migrationcenter_241_EmptyOut",
        "NetworkConnectionListIn": "_migrationcenter_242_NetworkConnectionListIn",
        "NetworkConnectionListOut": "_migrationcenter_243_NetworkConnectionListOut",
        "AggregateAssetsValuesRequestIn": "_migrationcenter_244_AggregateAssetsValuesRequestIn",
        "AggregateAssetsValuesRequestOut": "_migrationcenter_245_AggregateAssetsValuesRequestOut",
        "PhysicalPlatformDetailsIn": "_migrationcenter_246_PhysicalPlatformDetailsIn",
        "PhysicalPlatformDetailsOut": "_migrationcenter_247_PhysicalPlatformDetailsOut",
        "PlatformDetailsIn": "_migrationcenter_248_PlatformDetailsIn",
        "PlatformDetailsOut": "_migrationcenter_249_PlatformDetailsOut",
        "RemoveAssetsFromGroupRequestIn": "_migrationcenter_250_RemoveAssetsFromGroupRequestIn",
        "RemoveAssetsFromGroupRequestOut": "_migrationcenter_251_RemoveAssetsFromGroupRequestOut",
        "BatchDeleteAssetsRequestIn": "_migrationcenter_252_BatchDeleteAssetsRequestIn",
        "BatchDeleteAssetsRequestOut": "_migrationcenter_253_BatchDeleteAssetsRequestOut",
        "ComputeEngineShapeDescriptorIn": "_migrationcenter_254_ComputeEngineShapeDescriptorIn",
        "ComputeEngineShapeDescriptorOut": "_migrationcenter_255_ComputeEngineShapeDescriptorOut",
        "ImportDataFileIn": "_migrationcenter_256_ImportDataFileIn",
        "ImportDataFileOut": "_migrationcenter_257_ImportDataFileOut",
        "AssetPerformanceDataIn": "_migrationcenter_258_AssetPerformanceDataIn",
        "AssetPerformanceDataOut": "_migrationcenter_259_AssetPerformanceDataOut",
        "NetworkAdapterListIn": "_migrationcenter_260_NetworkAdapterListIn",
        "NetworkAdapterListOut": "_migrationcenter_261_NetworkAdapterListOut",
        "AssetIn": "_migrationcenter_262_AssetIn",
        "AssetOut": "_migrationcenter_263_AssetOut",
        "RuntimeNetworkInfoIn": "_migrationcenter_264_RuntimeNetworkInfoIn",
        "RuntimeNetworkInfoOut": "_migrationcenter_265_RuntimeNetworkInfoOut",
        "GenericPlatformDetailsIn": "_migrationcenter_266_GenericPlatformDetailsIn",
        "GenericPlatformDetailsOut": "_migrationcenter_267_GenericPlatformDetailsOut",
        "ReportConfigGroupPreferenceSetAssignmentIn": "_migrationcenter_268_ReportConfigGroupPreferenceSetAssignmentIn",
        "ReportConfigGroupPreferenceSetAssignmentOut": "_migrationcenter_269_ReportConfigGroupPreferenceSetAssignmentOut",
        "ListOperationsResponseIn": "_migrationcenter_270_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_migrationcenter_271_ListOperationsResponseOut",
        "GuestOsDetailsIn": "_migrationcenter_272_GuestOsDetailsIn",
        "GuestOsDetailsOut": "_migrationcenter_273_GuestOsDetailsOut",
        "AggregationHistogramIn": "_migrationcenter_274_AggregationHistogramIn",
        "AggregationHistogramOut": "_migrationcenter_275_AggregationHistogramOut",
        "AggregationResultIn": "_migrationcenter_276_AggregationResultIn",
        "AggregationResultOut": "_migrationcenter_277_AggregationResultOut",
        "ReportIn": "_migrationcenter_278_ReportIn",
        "ReportOut": "_migrationcenter_279_ReportOut",
        "FstabEntryIn": "_migrationcenter_280_FstabEntryIn",
        "FstabEntryOut": "_migrationcenter_281_FstabEntryOut",
        "VmwareEngineMigrationTargetIn": "_migrationcenter_282_VmwareEngineMigrationTargetIn",
        "VmwareEngineMigrationTargetOut": "_migrationcenter_283_VmwareEngineMigrationTargetOut",
        "MemoryUsageSampleIn": "_migrationcenter_284_MemoryUsageSampleIn",
        "MemoryUsageSampleOut": "_migrationcenter_285_MemoryUsageSampleOut",
        "DiskEntryIn": "_migrationcenter_286_DiskEntryIn",
        "DiskEntryOut": "_migrationcenter_287_DiskEntryOut",
        "RegionPreferencesIn": "_migrationcenter_288_RegionPreferencesIn",
        "RegionPreferencesOut": "_migrationcenter_289_RegionPreferencesOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AddAssetsToGroupRequestIn"] = t.struct(
        {
            "allowExisting": t.boolean().optional(),
            "requestId": t.string().optional(),
            "assets": t.proxy(renames["AssetListIn"]),
        }
    ).named(renames["AddAssetsToGroupRequestIn"])
    types["AddAssetsToGroupRequestOut"] = t.struct(
        {
            "allowExisting": t.boolean().optional(),
            "requestId": t.string().optional(),
            "assets": t.proxy(renames["AssetListOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddAssetsToGroupRequestOut"])
    types["ValidateImportJobRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["ValidateImportJobRequestIn"])
    types["ValidateImportJobRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateImportJobRequestOut"])
    types["ImportRowErrorIn"] = t.struct(
        {
            "vmUuid": t.string().optional(),
            "errors": t.array(t.proxy(renames["ImportErrorIn"])).optional(),
            "rowNumber": t.integer().optional(),
            "vmName": t.string().optional(),
        }
    ).named(renames["ImportRowErrorIn"])
    types["ImportRowErrorOut"] = t.struct(
        {
            "vmUuid": t.string().optional(),
            "errors": t.array(t.proxy(renames["ImportErrorOut"])).optional(),
            "rowNumber": t.integer().optional(),
            "vmName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportRowErrorOut"])
    types["VirtualMachinePreferencesIn"] = t.struct(
        {
            "computeEnginePreferences": t.proxy(
                renames["ComputeEnginePreferencesIn"]
            ).optional(),
            "regionPreferences": t.proxy(renames["RegionPreferencesIn"]).optional(),
            "commitmentPlan": t.string().optional(),
            "sizingOptimizationStrategy": t.string().optional(),
        }
    ).named(renames["VirtualMachinePreferencesIn"])
    types["VirtualMachinePreferencesOut"] = t.struct(
        {
            "computeEnginePreferences": t.proxy(
                renames["ComputeEnginePreferencesOut"]
            ).optional(),
            "regionPreferences": t.proxy(renames["RegionPreferencesOut"]).optional(),
            "commitmentPlan": t.string().optional(),
            "sizingOptimizationStrategy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualMachinePreferencesOut"])
    types["DateIn"] = t.struct(
        {
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["NetworkAddressListIn"] = t.struct(
        {"addresses": t.array(t.proxy(renames["NetworkAddressIn"])).optional()}
    ).named(renames["NetworkAddressListIn"])
    types["NetworkAddressListOut"] = t.struct(
        {
            "addresses": t.array(t.proxy(renames["NetworkAddressOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkAddressListOut"])
    types["ListSourcesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "sources": t.array(t.proxy(renames["SourceIn"])).optional(),
        }
    ).named(renames["ListSourcesResponseIn"])
    types["ListSourcesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSourcesResponseOut"])
    types["InsightIn"] = t.struct({"_": t.string().optional()}).named(
        renames["InsightIn"]
    )
    types["InsightOut"] = t.struct(
        {
            "migrationInsight": t.proxy(renames["MigrationInsightOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsightOut"])
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
    types["VirtualMachineDiskDetailsIn"] = t.struct(
        {
            "hddTotalCapacityBytes": t.string().optional(),
            "hddTotalFreeBytes": t.string().optional(),
            "lsblkJson": t.string().optional(),
            "disks": t.proxy(renames["DiskEntryListIn"]).optional(),
        }
    ).named(renames["VirtualMachineDiskDetailsIn"])
    types["VirtualMachineDiskDetailsOut"] = t.struct(
        {
            "hddTotalCapacityBytes": t.string().optional(),
            "hddTotalFreeBytes": t.string().optional(),
            "lsblkJson": t.string().optional(),
            "disks": t.proxy(renames["DiskEntryListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualMachineDiskDetailsOut"])
    types["ReportAssetFramesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReportAssetFramesResponseIn"]
    )
    types["ReportAssetFramesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReportAssetFramesResponseOut"])
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
    types["FstabEntryListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["FstabEntryIn"])).optional()}
    ).named(renames["FstabEntryListIn"])
    types["FstabEntryListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["FstabEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FstabEntryListOut"])
    types["VirtualMachineDetailsIn"] = t.struct(
        {
            "powerState": t.string().optional(),
            "vcenterUrl": t.string().optional(),
            "createTime": t.string().optional(),
            "osFamily": t.string().optional(),
            "memoryMb": t.integer().optional(),
            "osName": t.string().optional(),
            "vmArchitecture": t.proxy(
                renames["VirtualMachineArchitectureDetailsIn"]
            ).optional(),
            "vmDisks": t.proxy(renames["VirtualMachineDiskDetailsIn"]).optional(),
            "coreCount": t.integer().optional(),
            "vmUuid": t.string().optional(),
            "guestOs": t.proxy(renames["GuestOsDetailsIn"]).optional(),
            "platform": t.proxy(renames["PlatformDetailsIn"]).optional(),
            "vcenterFolder": t.string().optional(),
            "vmNetwork": t.proxy(renames["VirtualMachineNetworkDetailsIn"]).optional(),
            "vcenterVmId": t.string().optional(),
            "vmName": t.string().optional(),
            "osVersion": t.string().optional(),
        }
    ).named(renames["VirtualMachineDetailsIn"])
    types["VirtualMachineDetailsOut"] = t.struct(
        {
            "powerState": t.string().optional(),
            "vcenterUrl": t.string().optional(),
            "createTime": t.string().optional(),
            "osFamily": t.string().optional(),
            "memoryMb": t.integer().optional(),
            "osName": t.string().optional(),
            "vmArchitecture": t.proxy(
                renames["VirtualMachineArchitectureDetailsOut"]
            ).optional(),
            "vmDisks": t.proxy(renames["VirtualMachineDiskDetailsOut"]).optional(),
            "coreCount": t.integer().optional(),
            "vmUuid": t.string().optional(),
            "guestOs": t.proxy(renames["GuestOsDetailsOut"]).optional(),
            "platform": t.proxy(renames["PlatformDetailsOut"]).optional(),
            "vcenterFolder": t.string().optional(),
            "vmNetwork": t.proxy(renames["VirtualMachineNetworkDetailsOut"]).optional(),
            "vcenterVmId": t.string().optional(),
            "vmName": t.string().optional(),
            "osVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualMachineDetailsOut"])
    types["BatchUpdateAssetsRequestIn"] = t.struct(
        {"requests": t.array(t.proxy(renames["UpdateAssetRequestIn"]))}
    ).named(renames["BatchUpdateAssetsRequestIn"])
    types["BatchUpdateAssetsRequestOut"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["UpdateAssetRequestOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateAssetsRequestOut"])
    types["RunningProcessListIn"] = t.struct(
        {"processes": t.array(t.proxy(renames["RunningProcessIn"])).optional()}
    ).named(renames["RunningProcessListIn"])
    types["RunningProcessListOut"] = t.struct(
        {
            "processes": t.array(t.proxy(renames["RunningProcessOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunningProcessListOut"])
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
    types["MachineSeriesIn"] = t.struct({"code": t.string().optional()}).named(
        renames["MachineSeriesIn"]
    )
    types["MachineSeriesOut"] = t.struct(
        {
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MachineSeriesOut"])
    types["AggregationCountIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AggregationCountIn"]
    )
    types["AggregationCountOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AggregationCountOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["AggregationSumIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AggregationSumIn"]
    )
    types["AggregationSumOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AggregationSumOut"])
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
    types["ImportJobIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "gcsPayload": t.proxy(renames["GCSPayloadInfoIn"]).optional(),
            "assetSource": t.string(),
            "inlinePayload": t.proxy(renames["InlinePayloadInfoIn"]).optional(),
        }
    ).named(renames["ImportJobIn"])
    types["ImportJobOut"] = t.struct(
        {
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "gcsPayload": t.proxy(renames["GCSPayloadInfoOut"]).optional(),
            "assetSource": t.string(),
            "completeTime": t.string().optional(),
            "executionReport": t.proxy(renames["ExecutionReportOut"]).optional(),
            "inlinePayload": t.proxy(renames["InlinePayloadInfoOut"]).optional(),
            "validationReport": t.proxy(renames["ValidationReportOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportJobOut"])
    types["UploadFileInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UploadFileInfoIn"]
    )
    types["UploadFileInfoOut"] = t.struct(
        {
            "uriExpirationTime": t.string().optional(),
            "signedUri": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadFileInfoOut"])
    types["GuestConfigDetailsIn"] = t.struct(
        {
            "issue": t.string().optional(),
            "fstab": t.proxy(renames["FstabEntryListIn"]).optional(),
            "nfsExports": t.proxy(renames["NfsExportListIn"]).optional(),
            "selinux": t.proxy(renames["SelinuxIn"]).optional(),
            "hosts": t.proxy(renames["HostsEntryListIn"]).optional(),
        }
    ).named(renames["GuestConfigDetailsIn"])
    types["GuestConfigDetailsOut"] = t.struct(
        {
            "issue": t.string().optional(),
            "fstab": t.proxy(renames["FstabEntryListOut"]).optional(),
            "nfsExports": t.proxy(renames["NfsExportListOut"]).optional(),
            "selinux": t.proxy(renames["SelinuxOut"]).optional(),
            "hosts": t.proxy(renames["HostsEntryListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestConfigDetailsOut"])
    types["DiskUsageSampleIn"] = t.struct({"averageIops": t.number().optional()}).named(
        renames["DiskUsageSampleIn"]
    )
    types["DiskUsageSampleOut"] = t.struct(
        {
            "averageIops": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskUsageSampleOut"])
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
    types["AggregateAssetsValuesResponseIn"] = t.struct(
        {"results": t.array(t.proxy(renames["AggregationResultIn"])).optional()}
    ).named(renames["AggregateAssetsValuesResponseIn"])
    types["AggregateAssetsValuesResponseOut"] = t.struct(
        {
            "results": t.array(t.proxy(renames["AggregationResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregateAssetsValuesResponseOut"])
    types["ComputeEnginePreferencesIn"] = t.struct(
        {
            "machinePreferences": t.proxy(renames["MachinePreferencesIn"]).optional(),
            "licenseType": t.string().optional(),
            "persistentDiskType": t.string().optional(),
        }
    ).named(renames["ComputeEnginePreferencesIn"])
    types["ComputeEnginePreferencesOut"] = t.struct(
        {
            "machinePreferences": t.proxy(renames["MachinePreferencesOut"]).optional(),
            "licenseType": t.string().optional(),
            "persistentDiskType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeEnginePreferencesOut"])
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
    types["DailyResourceUsageAggregationStatsIn"] = t.struct(
        {
            "ninteyFifthPercentile": t.number().optional(),
            "average": t.number().optional(),
            "peak": t.number().optional(),
            "median": t.number().optional(),
        }
    ).named(renames["DailyResourceUsageAggregationStatsIn"])
    types["DailyResourceUsageAggregationStatsOut"] = t.struct(
        {
            "ninteyFifthPercentile": t.number().optional(),
            "average": t.number().optional(),
            "peak": t.number().optional(),
            "median": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DailyResourceUsageAggregationStatsOut"])
    types["ListErrorFramesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "errorFrames": t.array(t.proxy(renames["ErrorFrameIn"])).optional(),
        }
    ).named(renames["ListErrorFramesResponseIn"])
    types["ListErrorFramesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "errorFrames": t.array(t.proxy(renames["ErrorFrameOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListErrorFramesResponseOut"])
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
    types["VirtualMachineArchitectureDetailsIn"] = t.struct(
        {
            "cpuManufacturer": t.string().optional(),
            "vendor": t.string().optional(),
            "bios": t.proxy(renames["BiosDetailsIn"]).optional(),
            "firmware": t.string().optional(),
            "cpuThreadCount": t.integer().optional(),
            "cpuName": t.string().optional(),
            "hyperthreading": t.string().optional(),
            "cpuArchitecture": t.string().optional(),
            "cpuSocketCount": t.integer().optional(),
        }
    ).named(renames["VirtualMachineArchitectureDetailsIn"])
    types["VirtualMachineArchitectureDetailsOut"] = t.struct(
        {
            "cpuManufacturer": t.string().optional(),
            "vendor": t.string().optional(),
            "bios": t.proxy(renames["BiosDetailsOut"]).optional(),
            "firmware": t.string().optional(),
            "cpuThreadCount": t.integer().optional(),
            "cpuName": t.string().optional(),
            "hyperthreading": t.string().optional(),
            "cpuArchitecture": t.string().optional(),
            "cpuSocketCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualMachineArchitectureDetailsOut"])
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
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["AggregationIn"] = t.struct(
        {
            "histogram": t.proxy(renames["AggregationHistogramIn"]).optional(),
            "sum": t.proxy(renames["AggregationSumIn"]).optional(),
            "field": t.string().optional(),
            "count": t.proxy(renames["AggregationCountIn"]).optional(),
            "frequency": t.proxy(renames["AggregationFrequencyIn"]).optional(),
        }
    ).named(renames["AggregationIn"])
    types["AggregationOut"] = t.struct(
        {
            "histogram": t.proxy(renames["AggregationHistogramOut"]).optional(),
            "sum": t.proxy(renames["AggregationSumOut"]).optional(),
            "field": t.string().optional(),
            "count": t.proxy(renames["AggregationCountOut"]).optional(),
            "frequency": t.proxy(renames["AggregationFrequencyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationOut"])
    types["NfsExportListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["NfsExportIn"])).optional()}
    ).named(renames["NfsExportListIn"])
    types["NfsExportListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["NfsExportOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NfsExportListOut"])
    types["OpenFileListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["OpenFileDetailsIn"])).optional()}
    ).named(renames["OpenFileListIn"])
    types["OpenFileListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["OpenFileDetailsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OpenFileListOut"])
    types["AggregationResultHistogramBucketIn"] = t.struct(
        {
            "lowerBound": t.number().optional(),
            "count": t.string().optional(),
            "upperBound": t.number().optional(),
        }
    ).named(renames["AggregationResultHistogramBucketIn"])
    types["AggregationResultHistogramBucketOut"] = t.struct(
        {
            "lowerBound": t.number().optional(),
            "count": t.string().optional(),
            "upperBound": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationResultHistogramBucketOut"])
    types["DiskEntryListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["DiskEntryIn"])).optional()}
    ).named(renames["DiskEntryListIn"])
    types["DiskEntryListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["DiskEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskEntryListOut"])
    types["AggregationResultFrequencyIn"] = t.struct(
        {"values": t.struct({"_": t.string().optional()})}
    ).named(renames["AggregationResultFrequencyIn"])
    types["AggregationResultFrequencyOut"] = t.struct(
        {
            "values": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationResultFrequencyOut"])
    types["FileValidationReportIn"] = t.struct(
        {
            "fileName": t.string().optional(),
            "partialReport": t.boolean().optional(),
            "rowErrors": t.array(t.proxy(renames["ImportRowErrorIn"])).optional(),
            "fileErrors": t.array(t.proxy(renames["ImportErrorIn"])).optional(),
        }
    ).named(renames["FileValidationReportIn"])
    types["FileValidationReportOut"] = t.struct(
        {
            "fileName": t.string().optional(),
            "partialReport": t.boolean().optional(),
            "rowErrors": t.array(t.proxy(renames["ImportRowErrorOut"])).optional(),
            "fileErrors": t.array(t.proxy(renames["ImportErrorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileValidationReportOut"])
    types["AssetListIn"] = t.struct({"assetIds": t.array(t.string())}).named(
        renames["AssetListIn"]
    )
    types["AssetListOut"] = t.struct(
        {
            "assetIds": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetListOut"])
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
    types["RunningServiceListIn"] = t.struct(
        {"services": t.array(t.proxy(renames["RunningServiceIn"])).optional()}
    ).named(renames["RunningServiceListIn"])
    types["RunningServiceListOut"] = t.struct(
        {
            "services": t.array(t.proxy(renames["RunningServiceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunningServiceListOut"])
    types["NetworkConnectionIn"] = t.struct(
        {
            "protocol": t.string().optional(),
            "remoteIpAddress": t.string().optional(),
            "state": t.string().optional(),
            "remotePort": t.integer().optional(),
            "pid": t.string().optional(),
            "localIpAddress": t.string().optional(),
            "localPort": t.integer().optional(),
            "processName": t.string().optional(),
        }
    ).named(renames["NetworkConnectionIn"])
    types["NetworkConnectionOut"] = t.struct(
        {
            "protocol": t.string().optional(),
            "remoteIpAddress": t.string().optional(),
            "state": t.string().optional(),
            "remotePort": t.integer().optional(),
            "pid": t.string().optional(),
            "localIpAddress": t.string().optional(),
            "localPort": t.integer().optional(),
            "processName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConnectionOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["DiskPartitionIn"] = t.struct(
        {
            "freeBytes": t.string().optional(),
            "uuid": t.string().optional(),
            "subPartitions": t.proxy(renames["DiskPartitionListIn"]).optional(),
            "mountPoint": t.string().optional(),
            "fileSystem": t.string().optional(),
            "type": t.string().optional(),
            "capacityBytes": t.string().optional(),
        }
    ).named(renames["DiskPartitionIn"])
    types["DiskPartitionOut"] = t.struct(
        {
            "freeBytes": t.string().optional(),
            "uuid": t.string().optional(),
            "subPartitions": t.proxy(renames["DiskPartitionListOut"]).optional(),
            "mountPoint": t.string().optional(),
            "fileSystem": t.string().optional(),
            "type": t.string().optional(),
            "capacityBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskPartitionOut"])
    types["BatchUpdateAssetsResponseIn"] = t.struct(
        {"assets": t.array(t.proxy(renames["AssetIn"])).optional()}
    ).named(renames["BatchUpdateAssetsResponseIn"])
    types["BatchUpdateAssetsResponseOut"] = t.struct(
        {
            "assets": t.array(t.proxy(renames["AssetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateAssetsResponseOut"])
    types["HostsEntryListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["HostsEntryIn"])).optional()}
    ).named(renames["HostsEntryListIn"])
    types["HostsEntryListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["HostsEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HostsEntryListOut"])
    types["UpdateAssetRequestIn"] = t.struct(
        {
            "updateMask": t.string(),
            "requestId": t.string().optional(),
            "asset": t.proxy(renames["AssetIn"]),
        }
    ).named(renames["UpdateAssetRequestIn"])
    types["UpdateAssetRequestOut"] = t.struct(
        {
            "updateMask": t.string(),
            "requestId": t.string().optional(),
            "asset": t.proxy(renames["AssetOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateAssetRequestOut"])
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
    types["ListAssetsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "assets": t.array(t.proxy(renames["AssetIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAssetsResponseIn"])
    types["ListAssetsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "assets": t.array(t.proxy(renames["AssetOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAssetsResponseOut"])
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
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["ListImportJobsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "importJobs": t.array(t.proxy(renames["ImportJobIn"])).optional(),
        }
    ).named(renames["ListImportJobsResponseIn"])
    types["ListImportJobsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "importJobs": t.array(t.proxy(renames["ImportJobOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListImportJobsResponseOut"])
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
            "name": t.string().optional(),
            "virtualMachinePreferences": t.proxy(
                renames["VirtualMachinePreferencesOut"]
            ).optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PreferenceSetOut"])
    types["GuestInstalledApplicationIn"] = t.struct(
        {
            "time": t.string().optional(),
            "name": t.string().optional(),
            "path": t.string().optional(),
            "vendor": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["GuestInstalledApplicationIn"])
    types["GuestInstalledApplicationOut"] = t.struct(
        {
            "time": t.string().optional(),
            "name": t.string().optional(),
            "path": t.string().optional(),
            "vendor": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestInstalledApplicationOut"])
    types["ReportSummaryAssetAggregateStatsIn"] = t.struct(
        {
            "coreCountHistogram": t.proxy(
                renames["ReportSummaryHistogramChartDataIn"]
            ).optional(),
            "memoryUtilization": t.proxy(
                renames["ReportSummaryChartDataIn"]
            ).optional(),
            "totalAssets": t.string().optional(),
            "storageUtilization": t.proxy(
                renames["ReportSummaryChartDataIn"]
            ).optional(),
            "memoryBytesHistogram": t.proxy(
                renames["ReportSummaryHistogramChartDataIn"]
            ).optional(),
            "operatingSystem": t.proxy(renames["ReportSummaryChartDataIn"]).optional(),
            "totalStorageBytes": t.string().optional(),
            "assetAge": t.proxy(renames["ReportSummaryChartDataIn"]).optional(),
            "storageUtilizationChart": t.proxy(
                renames["ReportSummaryUtilizationChartDataIn"]
            ).optional(),
            "totalCores": t.string().optional(),
            "totalMemoryBytes": t.string().optional(),
            "memoryUtilizationChart": t.proxy(
                renames["ReportSummaryUtilizationChartDataIn"]
            ).optional(),
            "storageBytesHistogram": t.proxy(
                renames["ReportSummaryHistogramChartDataIn"]
            ).optional(),
        }
    ).named(renames["ReportSummaryAssetAggregateStatsIn"])
    types["ReportSummaryAssetAggregateStatsOut"] = t.struct(
        {
            "coreCountHistogram": t.proxy(
                renames["ReportSummaryHistogramChartDataOut"]
            ).optional(),
            "memoryUtilization": t.proxy(
                renames["ReportSummaryChartDataOut"]
            ).optional(),
            "totalAssets": t.string().optional(),
            "storageUtilization": t.proxy(
                renames["ReportSummaryChartDataOut"]
            ).optional(),
            "memoryBytesHistogram": t.proxy(
                renames["ReportSummaryHistogramChartDataOut"]
            ).optional(),
            "operatingSystem": t.proxy(renames["ReportSummaryChartDataOut"]).optional(),
            "totalStorageBytes": t.string().optional(),
            "assetAge": t.proxy(renames["ReportSummaryChartDataOut"]).optional(),
            "storageUtilizationChart": t.proxy(
                renames["ReportSummaryUtilizationChartDataOut"]
            ).optional(),
            "totalCores": t.string().optional(),
            "totalMemoryBytes": t.string().optional(),
            "memoryUtilizationChart": t.proxy(
                renames["ReportSummaryUtilizationChartDataOut"]
            ).optional(),
            "storageBytesHistogram": t.proxy(
                renames["ReportSummaryHistogramChartDataOut"]
            ).optional(),
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
    types["ReportConfigIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "groupPreferencesetAssignments": t.array(
                t.proxy(renames["ReportConfigGroupPreferenceSetAssignmentIn"])
            ),
        }
    ).named(renames["ReportConfigIn"])
    types["ReportConfigOut"] = t.struct(
        {
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "groupPreferencesetAssignments": t.array(
                t.proxy(renames["ReportConfigGroupPreferenceSetAssignmentOut"])
            ),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportConfigOut"])
    types["FitDescriptorIn"] = t.struct({"fitLevel": t.string().optional()}).named(
        renames["FitDescriptorIn"]
    )
    types["FitDescriptorOut"] = t.struct(
        {
            "fitLevel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FitDescriptorOut"])
    types["VmwareDiskConfigIn"] = t.struct(
        {
            "backingType": t.string().optional(),
            "shared": t.boolean().optional(),
            "rdmCompatibilityMode": t.string().optional(),
            "vmdkDiskMode": t.string().optional(),
        }
    ).named(renames["VmwareDiskConfigIn"])
    types["VmwareDiskConfigOut"] = t.struct(
        {
            "backingType": t.string().optional(),
            "shared": t.boolean().optional(),
            "rdmCompatibilityMode": t.string().optional(),
            "vmdkDiskMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareDiskConfigOut"])
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
    types["AggregationFrequencyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AggregationFrequencyIn"]
    )
    types["AggregationFrequencyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AggregationFrequencyOut"])
    types["BiosDetailsIn"] = t.struct(
        {
            "biosManufacturer": t.string().optional(),
            "smbiosUuid": t.string().optional(),
            "biosVersion": t.string().optional(),
            "biosReleaseDate": t.string().optional(),
            "biosName": t.string().optional(),
        }
    ).named(renames["BiosDetailsIn"])
    types["BiosDetailsOut"] = t.struct(
        {
            "biosManufacturer": t.string().optional(),
            "smbiosUuid": t.string().optional(),
            "biosVersion": t.string().optional(),
            "biosReleaseDate": t.string().optional(),
            "biosName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BiosDetailsOut"])
    types["GroupIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
    types["ExecutionReportIn"] = t.struct(
        {
            "totalRowsCount": t.integer().optional(),
            "executionErrors": t.proxy(renames["ValidationReportIn"]).optional(),
            "jobErrors": t.array(t.proxy(renames["ImportErrorIn"])).optional(),
            "framesReported": t.integer().optional(),
        }
    ).named(renames["ExecutionReportIn"])
    types["ExecutionReportOut"] = t.struct(
        {
            "totalRowsCount": t.integer().optional(),
            "executionErrors": t.proxy(renames["ValidationReportOut"]).optional(),
            "jobErrors": t.array(t.proxy(renames["ImportErrorOut"])).optional(),
            "framesReported": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionReportOut"])
    types["DailyResourceUsageAggregationIn"] = t.struct(
        {
            "disk": t.proxy(renames["DailyResourceUsageAggregationDiskIn"]).optional(),
            "network": t.proxy(
                renames["DailyResourceUsageAggregationNetworkIn"]
            ).optional(),
            "cpu": t.proxy(renames["DailyResourceUsageAggregationCPUIn"]).optional(),
            "memory": t.proxy(
                renames["DailyResourceUsageAggregationMemoryIn"]
            ).optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["DailyResourceUsageAggregationIn"])
    types["DailyResourceUsageAggregationOut"] = t.struct(
        {
            "disk": t.proxy(renames["DailyResourceUsageAggregationDiskOut"]).optional(),
            "network": t.proxy(
                renames["DailyResourceUsageAggregationNetworkOut"]
            ).optional(),
            "cpu": t.proxy(renames["DailyResourceUsageAggregationCPUOut"]).optional(),
            "memory": t.proxy(
                renames["DailyResourceUsageAggregationMemoryOut"]
            ).optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DailyResourceUsageAggregationOut"])
    types["GoogleKubernetesEngineMigrationTargetIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleKubernetesEngineMigrationTargetIn"])
    types["GoogleKubernetesEngineMigrationTargetOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleKubernetesEngineMigrationTargetOut"])
    types["AssetFrameIn"] = t.struct(
        {
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "traceToken": t.string().optional(),
            "reportTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "virtualMachineDetails": t.proxy(
                renames["VirtualMachineDetailsIn"]
            ).optional(),
            "performanceSamples": t.array(
                t.proxy(renames["PerformanceSampleIn"])
            ).optional(),
        }
    ).named(renames["AssetFrameIn"])
    types["AssetFrameOut"] = t.struct(
        {
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "traceToken": t.string().optional(),
            "reportTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "virtualMachineDetails": t.proxy(
                renames["VirtualMachineDetailsOut"]
            ).optional(),
            "performanceSamples": t.array(
                t.proxy(renames["PerformanceSampleOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetFrameOut"])
    types["ListImportDataFilesResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "importDataFiles": t.array(t.proxy(renames["ImportDataFileIn"])).optional(),
        }
    ).named(renames["ListImportDataFilesResponseIn"])
    types["ListImportDataFilesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "importDataFiles": t.array(
                t.proxy(renames["ImportDataFileOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListImportDataFilesResponseOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "statusMessage": t.string().optional(),
            "target": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["ListGroupsResponseIn"] = t.struct(
        {
            "groups": t.array(t.proxy(renames["GroupIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListGroupsResponseIn"])
    types["ListGroupsResponseOut"] = t.struct(
        {
            "groups": t.array(t.proxy(renames["GroupOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGroupsResponseOut"])
    types["ReportSummaryGroupFindingIn"] = t.struct(
        {
            "preferenceSetFindings": t.array(
                t.proxy(renames["ReportSummaryGroupPreferenceSetFindingIn"])
            ).optional(),
            "displayName": t.string().optional(),
            "assetAggregateStats": t.proxy(
                renames["ReportSummaryAssetAggregateStatsIn"]
            ).optional(),
            "overlappingAssetCount": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ReportSummaryGroupFindingIn"])
    types["ReportSummaryGroupFindingOut"] = t.struct(
        {
            "preferenceSetFindings": t.array(
                t.proxy(renames["ReportSummaryGroupPreferenceSetFindingOut"])
            ).optional(),
            "displayName": t.string().optional(),
            "assetAggregateStats": t.proxy(
                renames["ReportSummaryAssetAggregateStatsOut"]
            ).optional(),
            "overlappingAssetCount": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryGroupFindingOut"])
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
    types["ReportSummaryIn"] = t.struct(
        {
            "allAssetsStats": t.proxy(
                renames["ReportSummaryAssetAggregateStatsIn"]
            ).optional(),
            "groupFindings": t.array(
                t.proxy(renames["ReportSummaryGroupFindingIn"])
            ).optional(),
        }
    ).named(renames["ReportSummaryIn"])
    types["ReportSummaryOut"] = t.struct(
        {
            "allAssetsStats": t.proxy(
                renames["ReportSummaryAssetAggregateStatsOut"]
            ).optional(),
            "groupFindings": t.array(
                t.proxy(renames["ReportSummaryGroupFindingOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryOut"])
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
    types["DateTimeIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "month": t.integer().optional(),
            "hours": t.integer().optional(),
            "year": t.integer().optional(),
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "day": t.integer().optional(),
            "utcOffset": t.string().optional(),
            "timeZone": t.proxy(renames["TimeZoneIn"]).optional(),
        }
    ).named(renames["DateTimeIn"])
    types["DateTimeOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "month": t.integer().optional(),
            "hours": t.integer().optional(),
            "year": t.integer().optional(),
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "day": t.integer().optional(),
            "utcOffset": t.string().optional(),
            "timeZone": t.proxy(renames["TimeZoneOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateTimeOut"])
    types["DiskPartitionListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["DiskPartitionIn"])).optional()}
    ).named(renames["DiskPartitionListIn"])
    types["DiskPartitionListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["DiskPartitionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskPartitionListOut"])
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
    types["RunImportJobRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["RunImportJobRequestIn"])
    types["RunImportJobRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunImportJobRequestOut"])
    types["MoneyIn"] = t.struct(
        {
            "units": t.string().optional(),
            "nanos": t.integer().optional(),
            "currencyCode": t.string().optional(),
        }
    ).named(renames["MoneyIn"])
    types["MoneyOut"] = t.struct(
        {
            "units": t.string().optional(),
            "nanos": t.integer().optional(),
            "currencyCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoneyOut"])
    types["ListReportConfigsResponseIn"] = t.struct(
        {
            "reportConfigs": t.array(t.proxy(renames["ReportConfigIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListReportConfigsResponseIn"])
    types["ListReportConfigsResponseOut"] = t.struct(
        {
            "reportConfigs": t.array(t.proxy(renames["ReportConfigOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReportConfigsResponseOut"])
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
    types["FramesIn"] = t.struct(
        {"framesData": t.array(t.proxy(renames["AssetFrameIn"])).optional()}
    ).named(renames["FramesIn"])
    types["FramesOut"] = t.struct(
        {
            "framesData": t.array(t.proxy(renames["AssetFrameOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FramesOut"])
    types["RunningProcessIn"] = t.struct(
        {
            "cmdline": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "exePath": t.string().optional(),
            "user": t.string().optional(),
            "pid": t.string().optional(),
        }
    ).named(renames["RunningProcessIn"])
    types["RunningProcessOut"] = t.struct(
        {
            "cmdline": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "exePath": t.string().optional(),
            "user": t.string().optional(),
            "pid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunningProcessOut"])
    types["AggregationResultCountIn"] = t.struct({"value": t.string()}).named(
        renames["AggregationResultCountIn"]
    )
    types["AggregationResultCountOut"] = t.struct(
        {"value": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AggregationResultCountOut"])
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
    types["FrameViolationEntryIn"] = t.struct(
        {"violation": t.string().optional(), "field": t.string().optional()}
    ).named(renames["FrameViolationEntryIn"])
    types["FrameViolationEntryOut"] = t.struct(
        {
            "violation": t.string().optional(),
            "field": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FrameViolationEntryOut"])
    types["PerformanceSampleIn"] = t.struct(
        {
            "network": t.proxy(renames["NetworkUsageSampleIn"]).optional(),
            "sampleTime": t.string().optional(),
            "cpu": t.proxy(renames["CpuUsageSampleIn"]).optional(),
            "disk": t.proxy(renames["DiskUsageSampleIn"]).optional(),
            "memory": t.proxy(renames["MemoryUsageSampleIn"]).optional(),
        }
    ).named(renames["PerformanceSampleIn"])
    types["PerformanceSampleOut"] = t.struct(
        {
            "network": t.proxy(renames["NetworkUsageSampleOut"]).optional(),
            "sampleTime": t.string().optional(),
            "cpu": t.proxy(renames["CpuUsageSampleOut"]).optional(),
            "disk": t.proxy(renames["DiskUsageSampleOut"]).optional(),
            "memory": t.proxy(renames["MemoryUsageSampleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerformanceSampleOut"])
    types["ReportSummaryMachineFindingIn"] = t.struct(
        {
            "allocatedAssetCount": t.string().optional(),
            "allocatedRegions": t.array(t.string()).optional(),
            "allocatedDiskTypes": t.array(t.string()).optional(),
            "machineSeriesAllocations": t.array(
                t.proxy(renames["ReportSummaryMachineSeriesAllocationIn"])
            ).optional(),
        }
    ).named(renames["ReportSummaryMachineFindingIn"])
    types["ReportSummaryMachineFindingOut"] = t.struct(
        {
            "allocatedAssetCount": t.string().optional(),
            "allocatedRegions": t.array(t.string()).optional(),
            "allocatedDiskTypes": t.array(t.string()).optional(),
            "machineSeriesAllocations": t.array(
                t.proxy(renames["ReportSummaryMachineSeriesAllocationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryMachineFindingOut"])
    types["ReportSummaryGroupPreferenceSetFindingIn"] = t.struct(
        {
            "machinePreferences": t.proxy(
                renames["VirtualMachinePreferencesIn"]
            ).optional(),
            "pricingTrack": t.string().optional(),
            "monthlyCostStorage": t.proxy(renames["MoneyIn"]).optional(),
            "displayName": t.string().optional(),
            "topPriority": t.string().optional(),
            "monthlyCostOsLicense": t.proxy(renames["MoneyIn"]).optional(),
            "monthlyCostTotal": t.proxy(renames["MoneyIn"]).optional(),
            "preferredRegion": t.string().optional(),
            "monthlyCostNetworkEgress": t.proxy(renames["MoneyIn"]).optional(),
            "machineFinding": t.proxy(
                renames["ReportSummaryMachineFindingIn"]
            ).optional(),
            "monthlyCostOther": t.proxy(renames["MoneyIn"]).optional(),
            "description": t.string().optional(),
            "monthlyCostCompute": t.proxy(renames["MoneyIn"]).optional(),
        }
    ).named(renames["ReportSummaryGroupPreferenceSetFindingIn"])
    types["ReportSummaryGroupPreferenceSetFindingOut"] = t.struct(
        {
            "machinePreferences": t.proxy(
                renames["VirtualMachinePreferencesOut"]
            ).optional(),
            "pricingTrack": t.string().optional(),
            "monthlyCostStorage": t.proxy(renames["MoneyOut"]).optional(),
            "displayName": t.string().optional(),
            "topPriority": t.string().optional(),
            "monthlyCostOsLicense": t.proxy(renames["MoneyOut"]).optional(),
            "monthlyCostTotal": t.proxy(renames["MoneyOut"]).optional(),
            "preferredRegion": t.string().optional(),
            "monthlyCostNetworkEgress": t.proxy(renames["MoneyOut"]).optional(),
            "machineFinding": t.proxy(
                renames["ReportSummaryMachineFindingOut"]
            ).optional(),
            "monthlyCostOther": t.proxy(renames["MoneyOut"]).optional(),
            "description": t.string().optional(),
            "monthlyCostCompute": t.proxy(renames["MoneyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryGroupPreferenceSetFindingOut"])
    types["GuestRuntimeDetailsIn"] = t.struct(
        {
            "processes": t.proxy(renames["RunningProcessListIn"]).optional(),
            "machineName": t.string().optional(),
            "openFileList": t.proxy(renames["OpenFileListIn"]).optional(),
            "networkInfo": t.proxy(renames["RuntimeNetworkInfoIn"]).optional(),
            "services": t.proxy(renames["RunningServiceListIn"]).optional(),
            "domain": t.string().optional(),
            "lastUptime": t.proxy(renames["DateIn"]).optional(),
            "installedApps": t.proxy(
                renames["GuestInstalledApplicationListIn"]
            ).optional(),
        }
    ).named(renames["GuestRuntimeDetailsIn"])
    types["GuestRuntimeDetailsOut"] = t.struct(
        {
            "processes": t.proxy(renames["RunningProcessListOut"]).optional(),
            "machineName": t.string().optional(),
            "openFileList": t.proxy(renames["OpenFileListOut"]).optional(),
            "networkInfo": t.proxy(renames["RuntimeNetworkInfoOut"]).optional(),
            "services": t.proxy(renames["RunningServiceListOut"]).optional(),
            "domain": t.string().optional(),
            "lastUptime": t.proxy(renames["DateOut"]).optional(),
            "installedApps": t.proxy(
                renames["GuestInstalledApplicationListOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestRuntimeDetailsOut"])
    types["RunningServiceIn"] = t.struct(
        {
            "state": t.string().optional(),
            "pid": t.string().optional(),
            "status": t.string().optional(),
            "name": t.string().optional(),
            "cmdline": t.string().optional(),
            "startMode": t.string().optional(),
            "exePath": t.string().optional(),
        }
    ).named(renames["RunningServiceIn"])
    types["RunningServiceOut"] = t.struct(
        {
            "state": t.string().optional(),
            "pid": t.string().optional(),
            "status": t.string().optional(),
            "name": t.string().optional(),
            "cmdline": t.string().optional(),
            "startMode": t.string().optional(),
            "exePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunningServiceOut"])
    types["SourceIn"] = t.struct(
        {
            "isManaged": t.boolean().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "priority": t.integer().optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "pendingFrameCount": t.integer().optional(),
            "state": t.string().optional(),
            "isManaged": t.boolean().optional(),
            "errorFrameCount": t.integer().optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "priority": t.integer().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["VirtualMachineNetworkDetailsIn"] = t.struct(
        {
            "publicIpAddress": t.string().optional(),
            "networkAdapters": t.proxy(renames["NetworkAdapterListIn"]).optional(),
            "primaryIpAddress": t.string().optional(),
            "defaultGw": t.string().optional(),
            "primaryMacAddress": t.string().optional(),
        }
    ).named(renames["VirtualMachineNetworkDetailsIn"])
    types["VirtualMachineNetworkDetailsOut"] = t.struct(
        {
            "publicIpAddress": t.string().optional(),
            "networkAdapters": t.proxy(renames["NetworkAdapterListOut"]).optional(),
            "primaryIpAddress": t.string().optional(),
            "defaultGw": t.string().optional(),
            "primaryMacAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualMachineNetworkDetailsOut"])
    types["NfsExportIn"] = t.struct(
        {
            "hosts": t.array(t.string()).optional(),
            "exportDirectory": t.string().optional(),
        }
    ).named(renames["NfsExportIn"])
    types["NfsExportOut"] = t.struct(
        {
            "hosts": t.array(t.string()).optional(),
            "exportDirectory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NfsExportOut"])
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
    types["ErrorFrameIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ErrorFrameIn"]
    )
    types["ErrorFrameOut"] = t.struct(
        {
            "originalFrame": t.proxy(renames["AssetFrameOut"]).optional(),
            "ingestionTime": t.string().optional(),
            "name": t.string().optional(),
            "violations": t.array(
                t.proxy(renames["FrameViolationEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorFrameOut"])
    types["AggregationResultSumIn"] = t.struct({"value": t.number()}).named(
        renames["AggregationResultSumIn"]
    )
    types["AggregationResultSumOut"] = t.struct(
        {"value": t.number(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AggregationResultSumOut"])
    types["ValidationReportIn"] = t.struct(
        {
            "fileValidations": t.array(
                t.proxy(renames["FileValidationReportIn"])
            ).optional(),
            "jobErrors": t.array(t.proxy(renames["ImportErrorIn"])).optional(),
        }
    ).named(renames["ValidationReportIn"])
    types["ValidationReportOut"] = t.struct(
        {
            "fileValidations": t.array(
                t.proxy(renames["FileValidationReportOut"])
            ).optional(),
            "jobErrors": t.array(t.proxy(renames["ImportErrorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationReportOut"])
    types["CpuUsageSampleIn"] = t.struct(
        {"utilizedPercentage": t.number().optional()}
    ).named(renames["CpuUsageSampleIn"])
    types["CpuUsageSampleOut"] = t.struct(
        {
            "utilizedPercentage": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CpuUsageSampleOut"])
    types["OpenFileDetailsIn"] = t.struct(
        {
            "filePath": t.string().optional(),
            "command": t.string().optional(),
            "user": t.string().optional(),
            "fileType": t.string().optional(),
        }
    ).named(renames["OpenFileDetailsIn"])
    types["OpenFileDetailsOut"] = t.struct(
        {
            "filePath": t.string().optional(),
            "command": t.string().optional(),
            "user": t.string().optional(),
            "fileType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OpenFileDetailsOut"])
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
    types["ListPreferenceSetsResponseIn"] = t.struct(
        {
            "preferenceSets": t.array(t.proxy(renames["PreferenceSetIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListPreferenceSetsResponseIn"])
    types["ListPreferenceSetsResponseOut"] = t.struct(
        {
            "preferenceSets": t.array(t.proxy(renames["PreferenceSetOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPreferenceSetsResponseOut"])
    types["ComputeEngineMigrationTargetIn"] = t.struct(
        {"shape": t.proxy(renames["ComputeEngineShapeDescriptorIn"]).optional()}
    ).named(renames["ComputeEngineMigrationTargetIn"])
    types["ComputeEngineMigrationTargetOut"] = t.struct(
        {
            "shape": t.proxy(renames["ComputeEngineShapeDescriptorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeEngineMigrationTargetOut"])
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
    types["NetworkAddressIn"] = t.struct(
        {
            "subnetMask": t.string().optional(),
            "bcast": t.string().optional(),
            "assignment": t.string().optional(),
            "ipAddress": t.string().optional(),
            "fqdn": t.string().optional(),
        }
    ).named(renames["NetworkAddressIn"])
    types["NetworkAddressOut"] = t.struct(
        {
            "subnetMask": t.string().optional(),
            "bcast": t.string().optional(),
            "assignment": t.string().optional(),
            "ipAddress": t.string().optional(),
            "fqdn": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkAddressOut"])
    types["PayloadFileIn"] = t.struct(
        {"data": t.string().optional(), "name": t.string().optional()}
    ).named(renames["PayloadFileIn"])
    types["PayloadFileOut"] = t.struct(
        {
            "data": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PayloadFileOut"])
    types["MigrationInsightIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MigrationInsightIn"]
    )
    types["MigrationInsightOut"] = t.struct(
        {
            "computeEngineTarget": t.proxy(
                renames["ComputeEngineMigrationTargetOut"]
            ).optional(),
            "vmwareEngineTarget": t.proxy(
                renames["VmwareEngineMigrationTargetOut"]
            ).optional(),
            "fit": t.proxy(renames["FitDescriptorOut"]).optional(),
            "gkeTarget": t.proxy(
                renames["GoogleKubernetesEngineMigrationTargetOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MigrationInsightOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["NetworkConnectionListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["NetworkConnectionIn"])).optional()}
    ).named(renames["NetworkConnectionListIn"])
    types["NetworkConnectionListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["NetworkConnectionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConnectionListOut"])
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
    types["PhysicalPlatformDetailsIn"] = t.struct(
        {"location": t.string().optional()}
    ).named(renames["PhysicalPlatformDetailsIn"])
    types["PhysicalPlatformDetailsOut"] = t.struct(
        {
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhysicalPlatformDetailsOut"])
    types["PlatformDetailsIn"] = t.struct(
        {
            "physicalDetails": t.proxy(renames["PhysicalPlatformDetailsIn"]).optional(),
            "azureVmDetails": t.proxy(renames["AzureVmPlatformDetailsIn"]).optional(),
            "awsEc2Details": t.proxy(renames["AwsEc2PlatformDetailsIn"]).optional(),
            "vmwareDetails": t.proxy(renames["VmwarePlatformDetailsIn"]).optional(),
            "genericDetails": t.proxy(renames["GenericPlatformDetailsIn"]).optional(),
        }
    ).named(renames["PlatformDetailsIn"])
    types["PlatformDetailsOut"] = t.struct(
        {
            "physicalDetails": t.proxy(
                renames["PhysicalPlatformDetailsOut"]
            ).optional(),
            "azureVmDetails": t.proxy(renames["AzureVmPlatformDetailsOut"]).optional(),
            "awsEc2Details": t.proxy(renames["AwsEc2PlatformDetailsOut"]).optional(),
            "vmwareDetails": t.proxy(renames["VmwarePlatformDetailsOut"]).optional(),
            "genericDetails": t.proxy(renames["GenericPlatformDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlatformDetailsOut"])
    types["RemoveAssetsFromGroupRequestIn"] = t.struct(
        {
            "assets": t.proxy(renames["AssetListIn"]),
            "requestId": t.string().optional(),
            "allowMissing": t.boolean().optional(),
        }
    ).named(renames["RemoveAssetsFromGroupRequestIn"])
    types["RemoveAssetsFromGroupRequestOut"] = t.struct(
        {
            "assets": t.proxy(renames["AssetListOut"]),
            "requestId": t.string().optional(),
            "allowMissing": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveAssetsFromGroupRequestOut"])
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
    types["ComputeEngineShapeDescriptorIn"] = t.struct(
        {
            "machineType": t.string().optional(),
            "series": t.string().optional(),
            "memoryMb": t.integer().optional(),
            "logicalCoreCount": t.integer().optional(),
            "physicalCoreCount": t.integer().optional(),
        }
    ).named(renames["ComputeEngineShapeDescriptorIn"])
    types["ComputeEngineShapeDescriptorOut"] = t.struct(
        {
            "machineType": t.string().optional(),
            "series": t.string().optional(),
            "memoryMb": t.integer().optional(),
            "logicalCoreCount": t.integer().optional(),
            "physicalCoreCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeEngineShapeDescriptorOut"])
    types["ImportDataFileIn"] = t.struct(
        {
            "uploadFileInfo": t.proxy(renames["UploadFileInfoIn"]).optional(),
            "format": t.string(),
            "displayName": t.string().optional(),
        }
    ).named(renames["ImportDataFileIn"])
    types["ImportDataFileOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "uploadFileInfo": t.proxy(renames["UploadFileInfoOut"]).optional(),
            "format": t.string(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportDataFileOut"])
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
    types["AssetIn"] = t.struct(
        {
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["AssetIn"])
    types["AssetOut"] = t.struct(
        {
            "name": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "sources": t.array(t.string()).optional(),
            "virtualMachineDetails": t.proxy(
                renames["VirtualMachineDetailsOut"]
            ).optional(),
            "performanceData": t.proxy(renames["AssetPerformanceDataOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "insightList": t.proxy(renames["InsightListOut"]).optional(),
            "updateTime": t.string().optional(),
            "assignedGroups": t.array(t.string()).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetOut"])
    types["RuntimeNetworkInfoIn"] = t.struct(
        {
            "connections": t.proxy(renames["NetworkConnectionListIn"]).optional(),
            "netstat": t.string().optional(),
            "netstatTime": t.proxy(renames["DateTimeIn"]).optional(),
        }
    ).named(renames["RuntimeNetworkInfoIn"])
    types["RuntimeNetworkInfoOut"] = t.struct(
        {
            "connections": t.proxy(renames["NetworkConnectionListOut"]).optional(),
            "netstat": t.string().optional(),
            "netstatTime": t.proxy(renames["DateTimeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeNetworkInfoOut"])
    types["GenericPlatformDetailsIn"] = t.struct(
        {"location": t.string().optional()}
    ).named(renames["GenericPlatformDetailsIn"])
    types["GenericPlatformDetailsOut"] = t.struct(
        {
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenericPlatformDetailsOut"])
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
    types["GuestOsDetailsIn"] = t.struct(
        {
            "config": t.proxy(renames["GuestConfigDetailsIn"]).optional(),
            "runtime": t.proxy(renames["GuestRuntimeDetailsIn"]).optional(),
        }
    ).named(renames["GuestOsDetailsIn"])
    types["GuestOsDetailsOut"] = t.struct(
        {
            "config": t.proxy(renames["GuestConfigDetailsOut"]).optional(),
            "runtime": t.proxy(renames["GuestRuntimeDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestOsDetailsOut"])
    types["AggregationHistogramIn"] = t.struct(
        {"lowerBounds": t.array(t.number()).optional()}
    ).named(renames["AggregationHistogramIn"])
    types["AggregationHistogramOut"] = t.struct(
        {
            "lowerBounds": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationHistogramOut"])
    types["AggregationResultIn"] = t.struct(
        {
            "field": t.string(),
            "count": t.proxy(renames["AggregationResultCountIn"]),
            "frequency": t.proxy(renames["AggregationResultFrequencyIn"]),
            "histogram": t.proxy(renames["AggregationResultHistogramIn"]),
            "sum": t.proxy(renames["AggregationResultSumIn"]),
        }
    ).named(renames["AggregationResultIn"])
    types["AggregationResultOut"] = t.struct(
        {
            "field": t.string(),
            "count": t.proxy(renames["AggregationResultCountOut"]),
            "frequency": t.proxy(renames["AggregationResultFrequencyOut"]),
            "histogram": t.proxy(renames["AggregationResultHistogramOut"]),
            "sum": t.proxy(renames["AggregationResultSumOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationResultOut"])
    types["ReportIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "state": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ReportIn"])
    types["ReportOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "state": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "summary": t.proxy(renames["ReportSummaryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportOut"])
    types["FstabEntryIn"] = t.struct(
        {
            "file": t.string().optional(),
            "vfstype": t.string().optional(),
            "freq": t.integer().optional(),
            "spec": t.string().optional(),
            "passno": t.integer().optional(),
            "mntops": t.string().optional(),
        }
    ).named(renames["FstabEntryIn"])
    types["FstabEntryOut"] = t.struct(
        {
            "file": t.string().optional(),
            "vfstype": t.string().optional(),
            "freq": t.integer().optional(),
            "spec": t.string().optional(),
            "passno": t.integer().optional(),
            "mntops": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FstabEntryOut"])
    types["VmwareEngineMigrationTargetIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["VmwareEngineMigrationTargetIn"])
    types["VmwareEngineMigrationTargetOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VmwareEngineMigrationTargetOut"])
    types["MemoryUsageSampleIn"] = t.struct(
        {"utilizedPercentage": t.number().optional()}
    ).named(renames["MemoryUsageSampleIn"])
    types["MemoryUsageSampleOut"] = t.struct(
        {
            "utilizedPercentage": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemoryUsageSampleOut"])
    types["DiskEntryIn"] = t.struct(
        {
            "partitions": t.proxy(renames["DiskPartitionListIn"]).optional(),
            "diskLabelType": t.string().optional(),
            "vmwareConfig": t.proxy(renames["VmwareDiskConfigIn"]).optional(),
            "totalFreeBytes": t.string().optional(),
            "hwAddress": t.string().optional(),
            "totalCapacityBytes": t.string().optional(),
            "diskLabel": t.string().optional(),
            "interfaceType": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["DiskEntryIn"])
    types["DiskEntryOut"] = t.struct(
        {
            "partitions": t.proxy(renames["DiskPartitionListOut"]).optional(),
            "diskLabelType": t.string().optional(),
            "vmwareConfig": t.proxy(renames["VmwareDiskConfigOut"]).optional(),
            "totalFreeBytes": t.string().optional(),
            "hwAddress": t.string().optional(),
            "totalCapacityBytes": t.string().optional(),
            "diskLabel": t.string().optional(),
            "interfaceType": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskEntryOut"])
    types["RegionPreferencesIn"] = t.struct(
        {"preferredRegions": t.array(t.string()).optional()}
    ).named(renames["RegionPreferencesIn"])
    types["RegionPreferencesOut"] = t.struct(
        {
            "preferredRegions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionPreferencesOut"])

    functions = {}
    functions["projectsLocationsGetSettings"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsUpdateSettings"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImportJobsDelete"] = migrationcenter.post(
        "v1alpha1/{parent}/importJobs",
        t.struct(
            {
                "parent": t.string(),
                "importJobId": t.string(),
                "requestId": t.string().optional(),
                "displayName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "gcsPayload": t.proxy(renames["GCSPayloadInfoIn"]).optional(),
                "assetSource": t.string(),
                "inlinePayload": t.proxy(renames["InlinePayloadInfoIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImportJobsGet"] = migrationcenter.post(
        "v1alpha1/{parent}/importJobs",
        t.struct(
            {
                "parent": t.string(),
                "importJobId": t.string(),
                "requestId": t.string().optional(),
                "displayName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "gcsPayload": t.proxy(renames["GCSPayloadInfoIn"]).optional(),
                "assetSource": t.string(),
                "inlinePayload": t.proxy(renames["InlinePayloadInfoIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImportJobsPatch"] = migrationcenter.post(
        "v1alpha1/{parent}/importJobs",
        t.struct(
            {
                "parent": t.string(),
                "importJobId": t.string(),
                "requestId": t.string().optional(),
                "displayName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "gcsPayload": t.proxy(renames["GCSPayloadInfoIn"]).optional(),
                "assetSource": t.string(),
                "inlinePayload": t.proxy(renames["InlinePayloadInfoIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImportJobsRun"] = migrationcenter.post(
        "v1alpha1/{parent}/importJobs",
        t.struct(
            {
                "parent": t.string(),
                "importJobId": t.string(),
                "requestId": t.string().optional(),
                "displayName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "gcsPayload": t.proxy(renames["GCSPayloadInfoIn"]).optional(),
                "assetSource": t.string(),
                "inlinePayload": t.proxy(renames["InlinePayloadInfoIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImportJobsList"] = migrationcenter.post(
        "v1alpha1/{parent}/importJobs",
        t.struct(
            {
                "parent": t.string(),
                "importJobId": t.string(),
                "requestId": t.string().optional(),
                "displayName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "gcsPayload": t.proxy(renames["GCSPayloadInfoIn"]).optional(),
                "assetSource": t.string(),
                "inlinePayload": t.proxy(renames["InlinePayloadInfoIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImportJobsValidate"] = migrationcenter.post(
        "v1alpha1/{parent}/importJobs",
        t.struct(
            {
                "parent": t.string(),
                "importJobId": t.string(),
                "requestId": t.string().optional(),
                "displayName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "gcsPayload": t.proxy(renames["GCSPayloadInfoIn"]).optional(),
                "assetSource": t.string(),
                "inlinePayload": t.proxy(renames["InlinePayloadInfoIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImportJobsCreate"] = migrationcenter.post(
        "v1alpha1/{parent}/importJobs",
        t.struct(
            {
                "parent": t.string(),
                "importJobId": t.string(),
                "requestId": t.string().optional(),
                "displayName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "gcsPayload": t.proxy(renames["GCSPayloadInfoIn"]).optional(),
                "assetSource": t.string(),
                "inlinePayload": t.proxy(renames["InlinePayloadInfoIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImportJobsImportDataFilesGet"] = migrationcenter.get(
        "v1alpha1/{parent}/importDataFiles",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListImportDataFilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImportJobsImportDataFilesCreate"] = migrationcenter.get(
        "v1alpha1/{parent}/importDataFiles",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListImportDataFilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImportJobsImportDataFilesDelete"] = migrationcenter.get(
        "v1alpha1/{parent}/importDataFiles",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListImportDataFilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImportJobsImportDataFilesList"] = migrationcenter.get(
        "v1alpha1/{parent}/importDataFiles",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListImportDataFilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPreferenceSetsList"] = migrationcenter.post(
        "v1alpha1/{parent}/preferenceSets",
        t.struct(
            {
                "requestId": t.string().optional(),
                "preferenceSetId": t.string(),
                "parent": t.string(),
                "virtualMachinePreferences": t.proxy(
                    renames["VirtualMachinePreferencesIn"]
                ).optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPreferenceSetsPatch"] = migrationcenter.post(
        "v1alpha1/{parent}/preferenceSets",
        t.struct(
            {
                "requestId": t.string().optional(),
                "preferenceSetId": t.string(),
                "parent": t.string(),
                "virtualMachinePreferences": t.proxy(
                    renames["VirtualMachinePreferencesIn"]
                ).optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPreferenceSetsGet"] = migrationcenter.post(
        "v1alpha1/{parent}/preferenceSets",
        t.struct(
            {
                "requestId": t.string().optional(),
                "preferenceSetId": t.string(),
                "parent": t.string(),
                "virtualMachinePreferences": t.proxy(
                    renames["VirtualMachinePreferencesIn"]
                ).optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPreferenceSetsDelete"] = migrationcenter.post(
        "v1alpha1/{parent}/preferenceSets",
        t.struct(
            {
                "requestId": t.string().optional(),
                "preferenceSetId": t.string(),
                "parent": t.string(),
                "virtualMachinePreferences": t.proxy(
                    renames["VirtualMachinePreferencesIn"]
                ).optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPreferenceSetsCreate"] = migrationcenter.post(
        "v1alpha1/{parent}/preferenceSets",
        t.struct(
            {
                "requestId": t.string().optional(),
                "preferenceSetId": t.string(),
                "parent": t.string(),
                "virtualMachinePreferences": t.proxy(
                    renames["VirtualMachinePreferencesIn"]
                ).optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsReportAssetFrames"] = migrationcenter.get(
        "v1alpha1/{parent}/assets",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsGet"] = migrationcenter.get(
        "v1alpha1/{parent}/assets",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsBatchUpdate"] = migrationcenter.get(
        "v1alpha1/{parent}/assets",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsAggregateValues"] = migrationcenter.get(
        "v1alpha1/{parent}/assets",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsBatchDelete"] = migrationcenter.get(
        "v1alpha1/{parent}/assets",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsPatch"] = migrationcenter.get(
        "v1alpha1/{parent}/assets",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsDelete"] = migrationcenter.get(
        "v1alpha1/{parent}/assets",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsList"] = migrationcenter.get(
        "v1alpha1/{parent}/assets",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsAddAssets"] = migrationcenter.post(
        "v1alpha1/{parent}/groups",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "groupId": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsPatch"] = migrationcenter.post(
        "v1alpha1/{parent}/groups",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "groupId": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsGet"] = migrationcenter.post(
        "v1alpha1/{parent}/groups",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "groupId": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsDelete"] = migrationcenter.post(
        "v1alpha1/{parent}/groups",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "groupId": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsList"] = migrationcenter.post(
        "v1alpha1/{parent}/groups",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "groupId": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsRemoveAssets"] = migrationcenter.post(
        "v1alpha1/{parent}/groups",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "groupId": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsCreate"] = migrationcenter.post(
        "v1alpha1/{parent}/groups",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "groupId": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
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
                "isManaged": t.boolean().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "type": t.string().optional(),
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
                "isManaged": t.boolean().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "type": t.string().optional(),
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
                "isManaged": t.boolean().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "type": t.string().optional(),
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
                "isManaged": t.boolean().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "type": t.string().optional(),
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
                "isManaged": t.boolean().optional(),
                "description": t.string().optional(),
                "displayName": t.string().optional(),
                "type": t.string().optional(),
                "priority": t.integer().optional(),
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
                "view": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
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
                "view": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListErrorFramesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReportConfigsCreate"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReportConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReportConfigsList"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReportConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReportConfigsDelete"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReportConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReportConfigsGet"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReportConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReportConfigsReportsDelete"] = migrationcenter.get(
        "v1alpha1/{parent}/reports",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReportConfigsReportsGet"] = migrationcenter.get(
        "v1alpha1/{parent}/reports",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReportConfigsReportsCreate"] = migrationcenter.get(
        "v1alpha1/{parent}/reports",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReportConfigsReportsList"] = migrationcenter.get(
        "v1alpha1/{parent}/reports",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="migrationcenter",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
