from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_migrationcenter() -> Import:
    migrationcenter = HTTPRuntime("https://migrationcenter.googleapis.com/")

    renames = {
        "ErrorResponse": "_migrationcenter_1_ErrorResponse",
        "ReportConfigGroupPreferenceSetAssignmentIn": "_migrationcenter_2_ReportConfigGroupPreferenceSetAssignmentIn",
        "ReportConfigGroupPreferenceSetAssignmentOut": "_migrationcenter_3_ReportConfigGroupPreferenceSetAssignmentOut",
        "ComputeEngineMigrationTargetIn": "_migrationcenter_4_ComputeEngineMigrationTargetIn",
        "ComputeEngineMigrationTargetOut": "_migrationcenter_5_ComputeEngineMigrationTargetOut",
        "OperationIn": "_migrationcenter_6_OperationIn",
        "OperationOut": "_migrationcenter_7_OperationOut",
        "ImportErrorIn": "_migrationcenter_8_ImportErrorIn",
        "ImportErrorOut": "_migrationcenter_9_ImportErrorOut",
        "BatchDeleteAssetsRequestIn": "_migrationcenter_10_BatchDeleteAssetsRequestIn",
        "BatchDeleteAssetsRequestOut": "_migrationcenter_11_BatchDeleteAssetsRequestOut",
        "StatusIn": "_migrationcenter_12_StatusIn",
        "StatusOut": "_migrationcenter_13_StatusOut",
        "UpdateAssetRequestIn": "_migrationcenter_14_UpdateAssetRequestIn",
        "UpdateAssetRequestOut": "_migrationcenter_15_UpdateAssetRequestOut",
        "InsightIn": "_migrationcenter_16_InsightIn",
        "InsightOut": "_migrationcenter_17_InsightOut",
        "NetworkAddressListIn": "_migrationcenter_18_NetworkAddressListIn",
        "NetworkAddressListOut": "_migrationcenter_19_NetworkAddressListOut",
        "ImportRowErrorIn": "_migrationcenter_20_ImportRowErrorIn",
        "ImportRowErrorOut": "_migrationcenter_21_ImportRowErrorOut",
        "AggregationIn": "_migrationcenter_22_AggregationIn",
        "AggregationOut": "_migrationcenter_23_AggregationOut",
        "FstabEntryListIn": "_migrationcenter_24_FstabEntryListIn",
        "FstabEntryListOut": "_migrationcenter_25_FstabEntryListOut",
        "AggregationResultCountIn": "_migrationcenter_26_AggregationResultCountIn",
        "AggregationResultCountOut": "_migrationcenter_27_AggregationResultCountOut",
        "ReportSummaryAssetAggregateStatsIn": "_migrationcenter_28_ReportSummaryAssetAggregateStatsIn",
        "ReportSummaryAssetAggregateStatsOut": "_migrationcenter_29_ReportSummaryAssetAggregateStatsOut",
        "ImportDataFileIn": "_migrationcenter_30_ImportDataFileIn",
        "ImportDataFileOut": "_migrationcenter_31_ImportDataFileOut",
        "PhysicalPlatformDetailsIn": "_migrationcenter_32_PhysicalPlatformDetailsIn",
        "PhysicalPlatformDetailsOut": "_migrationcenter_33_PhysicalPlatformDetailsOut",
        "DailyResourceUsageAggregationNetworkIn": "_migrationcenter_34_DailyResourceUsageAggregationNetworkIn",
        "DailyResourceUsageAggregationNetworkOut": "_migrationcenter_35_DailyResourceUsageAggregationNetworkOut",
        "AssetFrameIn": "_migrationcenter_36_AssetFrameIn",
        "AssetFrameOut": "_migrationcenter_37_AssetFrameOut",
        "AggregateAssetsValuesResponseIn": "_migrationcenter_38_AggregateAssetsValuesResponseIn",
        "AggregateAssetsValuesResponseOut": "_migrationcenter_39_AggregateAssetsValuesResponseOut",
        "PerformanceSampleIn": "_migrationcenter_40_PerformanceSampleIn",
        "PerformanceSampleOut": "_migrationcenter_41_PerformanceSampleOut",
        "RunningServiceListIn": "_migrationcenter_42_RunningServiceListIn",
        "RunningServiceListOut": "_migrationcenter_43_RunningServiceListOut",
        "ComputeEngineShapeDescriptorIn": "_migrationcenter_44_ComputeEngineShapeDescriptorIn",
        "ComputeEngineShapeDescriptorOut": "_migrationcenter_45_ComputeEngineShapeDescriptorOut",
        "ReportConfigIn": "_migrationcenter_46_ReportConfigIn",
        "ReportConfigOut": "_migrationcenter_47_ReportConfigOut",
        "NetworkConnectionListIn": "_migrationcenter_48_NetworkConnectionListIn",
        "NetworkConnectionListOut": "_migrationcenter_49_NetworkConnectionListOut",
        "BiosDetailsIn": "_migrationcenter_50_BiosDetailsIn",
        "BiosDetailsOut": "_migrationcenter_51_BiosDetailsOut",
        "PlatformDetailsIn": "_migrationcenter_52_PlatformDetailsIn",
        "PlatformDetailsOut": "_migrationcenter_53_PlatformDetailsOut",
        "ListSourcesResponseIn": "_migrationcenter_54_ListSourcesResponseIn",
        "ListSourcesResponseOut": "_migrationcenter_55_ListSourcesResponseOut",
        "ComputeEnginePreferencesIn": "_migrationcenter_56_ComputeEnginePreferencesIn",
        "ComputeEnginePreferencesOut": "_migrationcenter_57_ComputeEnginePreferencesOut",
        "ReportSummaryUtilizationChartDataIn": "_migrationcenter_58_ReportSummaryUtilizationChartDataIn",
        "ReportSummaryUtilizationChartDataOut": "_migrationcenter_59_ReportSummaryUtilizationChartDataOut",
        "VirtualMachineDiskDetailsIn": "_migrationcenter_60_VirtualMachineDiskDetailsIn",
        "VirtualMachineDiskDetailsOut": "_migrationcenter_61_VirtualMachineDiskDetailsOut",
        "MemoryUsageSampleIn": "_migrationcenter_62_MemoryUsageSampleIn",
        "MemoryUsageSampleOut": "_migrationcenter_63_MemoryUsageSampleOut",
        "ListImportDataFilesResponseIn": "_migrationcenter_64_ListImportDataFilesResponseIn",
        "ListImportDataFilesResponseOut": "_migrationcenter_65_ListImportDataFilesResponseOut",
        "ReportSummaryHistogramChartDataBucketIn": "_migrationcenter_66_ReportSummaryHistogramChartDataBucketIn",
        "ReportSummaryHistogramChartDataBucketOut": "_migrationcenter_67_ReportSummaryHistogramChartDataBucketOut",
        "NfsExportIn": "_migrationcenter_68_NfsExportIn",
        "NfsExportOut": "_migrationcenter_69_NfsExportOut",
        "NetworkConnectionIn": "_migrationcenter_70_NetworkConnectionIn",
        "NetworkConnectionOut": "_migrationcenter_71_NetworkConnectionOut",
        "DateTimeIn": "_migrationcenter_72_DateTimeIn",
        "DateTimeOut": "_migrationcenter_73_DateTimeOut",
        "ReportSummaryMachineFindingIn": "_migrationcenter_74_ReportSummaryMachineFindingIn",
        "ReportSummaryMachineFindingOut": "_migrationcenter_75_ReportSummaryMachineFindingOut",
        "DiskEntryListIn": "_migrationcenter_76_DiskEntryListIn",
        "DiskEntryListOut": "_migrationcenter_77_DiskEntryListOut",
        "DiskPartitionListIn": "_migrationcenter_78_DiskPartitionListIn",
        "DiskPartitionListOut": "_migrationcenter_79_DiskPartitionListOut",
        "AssetPerformanceDataIn": "_migrationcenter_80_AssetPerformanceDataIn",
        "AssetPerformanceDataOut": "_migrationcenter_81_AssetPerformanceDataOut",
        "NetworkAdapterListIn": "_migrationcenter_82_NetworkAdapterListIn",
        "NetworkAdapterListOut": "_migrationcenter_83_NetworkAdapterListOut",
        "ListLocationsResponseIn": "_migrationcenter_84_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_migrationcenter_85_ListLocationsResponseOut",
        "HostsEntryListIn": "_migrationcenter_86_HostsEntryListIn",
        "HostsEntryListOut": "_migrationcenter_87_HostsEntryListOut",
        "AggregationSumIn": "_migrationcenter_88_AggregationSumIn",
        "AggregationSumOut": "_migrationcenter_89_AggregationSumOut",
        "ReportSummaryChartDataIn": "_migrationcenter_90_ReportSummaryChartDataIn",
        "ReportSummaryChartDataOut": "_migrationcenter_91_ReportSummaryChartDataOut",
        "AggregationResultFrequencyIn": "_migrationcenter_92_AggregationResultFrequencyIn",
        "AggregationResultFrequencyOut": "_migrationcenter_93_AggregationResultFrequencyOut",
        "TimeZoneIn": "_migrationcenter_94_TimeZoneIn",
        "TimeZoneOut": "_migrationcenter_95_TimeZoneOut",
        "UploadFileInfoIn": "_migrationcenter_96_UploadFileInfoIn",
        "UploadFileInfoOut": "_migrationcenter_97_UploadFileInfoOut",
        "ListAssetsResponseIn": "_migrationcenter_98_ListAssetsResponseIn",
        "ListAssetsResponseOut": "_migrationcenter_99_ListAssetsResponseOut",
        "VmwareDiskConfigIn": "_migrationcenter_100_VmwareDiskConfigIn",
        "VmwareDiskConfigOut": "_migrationcenter_101_VmwareDiskConfigOut",
        "VmwarePlatformDetailsIn": "_migrationcenter_102_VmwarePlatformDetailsIn",
        "VmwarePlatformDetailsOut": "_migrationcenter_103_VmwarePlatformDetailsOut",
        "GCSPayloadInfoIn": "_migrationcenter_104_GCSPayloadInfoIn",
        "GCSPayloadInfoOut": "_migrationcenter_105_GCSPayloadInfoOut",
        "RegionPreferencesIn": "_migrationcenter_106_RegionPreferencesIn",
        "RegionPreferencesOut": "_migrationcenter_107_RegionPreferencesOut",
        "FstabEntryIn": "_migrationcenter_108_FstabEntryIn",
        "FstabEntryOut": "_migrationcenter_109_FstabEntryOut",
        "MachineSeriesIn": "_migrationcenter_110_MachineSeriesIn",
        "MachineSeriesOut": "_migrationcenter_111_MachineSeriesOut",
        "ListReportsResponseIn": "_migrationcenter_112_ListReportsResponseIn",
        "ListReportsResponseOut": "_migrationcenter_113_ListReportsResponseOut",
        "AggregateAssetsValuesRequestIn": "_migrationcenter_114_AggregateAssetsValuesRequestIn",
        "AggregateAssetsValuesRequestOut": "_migrationcenter_115_AggregateAssetsValuesRequestOut",
        "RunImportJobRequestIn": "_migrationcenter_116_RunImportJobRequestIn",
        "RunImportJobRequestOut": "_migrationcenter_117_RunImportJobRequestOut",
        "BatchUpdateAssetsResponseIn": "_migrationcenter_118_BatchUpdateAssetsResponseIn",
        "BatchUpdateAssetsResponseOut": "_migrationcenter_119_BatchUpdateAssetsResponseOut",
        "LocationIn": "_migrationcenter_120_LocationIn",
        "LocationOut": "_migrationcenter_121_LocationOut",
        "ErrorFrameIn": "_migrationcenter_122_ErrorFrameIn",
        "ErrorFrameOut": "_migrationcenter_123_ErrorFrameOut",
        "ValidationReportIn": "_migrationcenter_124_ValidationReportIn",
        "ValidationReportOut": "_migrationcenter_125_ValidationReportOut",
        "FrameViolationEntryIn": "_migrationcenter_126_FrameViolationEntryIn",
        "FrameViolationEntryOut": "_migrationcenter_127_FrameViolationEntryOut",
        "GuestInstalledApplicationListIn": "_migrationcenter_128_GuestInstalledApplicationListIn",
        "GuestInstalledApplicationListOut": "_migrationcenter_129_GuestInstalledApplicationListOut",
        "ListGroupsResponseIn": "_migrationcenter_130_ListGroupsResponseIn",
        "ListGroupsResponseOut": "_migrationcenter_131_ListGroupsResponseOut",
        "ValidateImportJobRequestIn": "_migrationcenter_132_ValidateImportJobRequestIn",
        "ValidateImportJobRequestOut": "_migrationcenter_133_ValidateImportJobRequestOut",
        "GuestRuntimeDetailsIn": "_migrationcenter_134_GuestRuntimeDetailsIn",
        "GuestRuntimeDetailsOut": "_migrationcenter_135_GuestRuntimeDetailsOut",
        "ReportIn": "_migrationcenter_136_ReportIn",
        "ReportOut": "_migrationcenter_137_ReportOut",
        "DiskEntryIn": "_migrationcenter_138_DiskEntryIn",
        "DiskEntryOut": "_migrationcenter_139_DiskEntryOut",
        "AssetListIn": "_migrationcenter_140_AssetListIn",
        "AssetListOut": "_migrationcenter_141_AssetListOut",
        "OpenFileDetailsIn": "_migrationcenter_142_OpenFileDetailsIn",
        "OpenFileDetailsOut": "_migrationcenter_143_OpenFileDetailsOut",
        "AggregationFrequencyIn": "_migrationcenter_144_AggregationFrequencyIn",
        "AggregationFrequencyOut": "_migrationcenter_145_AggregationFrequencyOut",
        "ReportSummaryHistogramChartDataIn": "_migrationcenter_146_ReportSummaryHistogramChartDataIn",
        "ReportSummaryHistogramChartDataOut": "_migrationcenter_147_ReportSummaryHistogramChartDataOut",
        "EmptyIn": "_migrationcenter_148_EmptyIn",
        "EmptyOut": "_migrationcenter_149_EmptyOut",
        "ReportSummaryIn": "_migrationcenter_150_ReportSummaryIn",
        "ReportSummaryOut": "_migrationcenter_151_ReportSummaryOut",
        "VmwareEngineMigrationTargetIn": "_migrationcenter_152_VmwareEngineMigrationTargetIn",
        "VmwareEngineMigrationTargetOut": "_migrationcenter_153_VmwareEngineMigrationTargetOut",
        "VirtualMachineNetworkDetailsIn": "_migrationcenter_154_VirtualMachineNetworkDetailsIn",
        "VirtualMachineNetworkDetailsOut": "_migrationcenter_155_VirtualMachineNetworkDetailsOut",
        "GoogleKubernetesEngineMigrationTargetIn": "_migrationcenter_156_GoogleKubernetesEngineMigrationTargetIn",
        "GoogleKubernetesEngineMigrationTargetOut": "_migrationcenter_157_GoogleKubernetesEngineMigrationTargetOut",
        "SelinuxIn": "_migrationcenter_158_SelinuxIn",
        "SelinuxOut": "_migrationcenter_159_SelinuxOut",
        "FitDescriptorIn": "_migrationcenter_160_FitDescriptorIn",
        "FitDescriptorOut": "_migrationcenter_161_FitDescriptorOut",
        "GuestInstalledApplicationIn": "_migrationcenter_162_GuestInstalledApplicationIn",
        "GuestInstalledApplicationOut": "_migrationcenter_163_GuestInstalledApplicationOut",
        "DateIn": "_migrationcenter_164_DateIn",
        "DateOut": "_migrationcenter_165_DateOut",
        "BatchUpdateAssetsRequestIn": "_migrationcenter_166_BatchUpdateAssetsRequestIn",
        "BatchUpdateAssetsRequestOut": "_migrationcenter_167_BatchUpdateAssetsRequestOut",
        "AwsEc2PlatformDetailsIn": "_migrationcenter_168_AwsEc2PlatformDetailsIn",
        "AwsEc2PlatformDetailsOut": "_migrationcenter_169_AwsEc2PlatformDetailsOut",
        "InlinePayloadInfoIn": "_migrationcenter_170_InlinePayloadInfoIn",
        "InlinePayloadInfoOut": "_migrationcenter_171_InlinePayloadInfoOut",
        "RunningServiceIn": "_migrationcenter_172_RunningServiceIn",
        "RunningServiceOut": "_migrationcenter_173_RunningServiceOut",
        "AggregationHistogramIn": "_migrationcenter_174_AggregationHistogramIn",
        "AggregationHistogramOut": "_migrationcenter_175_AggregationHistogramOut",
        "InsightListIn": "_migrationcenter_176_InsightListIn",
        "InsightListOut": "_migrationcenter_177_InsightListOut",
        "DailyResourceUsageAggregationMemoryIn": "_migrationcenter_178_DailyResourceUsageAggregationMemoryIn",
        "DailyResourceUsageAggregationMemoryOut": "_migrationcenter_179_DailyResourceUsageAggregationMemoryOut",
        "ReportSummaryMachineSeriesAllocationIn": "_migrationcenter_180_ReportSummaryMachineSeriesAllocationIn",
        "ReportSummaryMachineSeriesAllocationOut": "_migrationcenter_181_ReportSummaryMachineSeriesAllocationOut",
        "DiskPartitionIn": "_migrationcenter_182_DiskPartitionIn",
        "DiskPartitionOut": "_migrationcenter_183_DiskPartitionOut",
        "AggregationResultHistogramIn": "_migrationcenter_184_AggregationResultHistogramIn",
        "AggregationResultHistogramOut": "_migrationcenter_185_AggregationResultHistogramOut",
        "AggregationResultIn": "_migrationcenter_186_AggregationResultIn",
        "AggregationResultOut": "_migrationcenter_187_AggregationResultOut",
        "ListPreferenceSetsResponseIn": "_migrationcenter_188_ListPreferenceSetsResponseIn",
        "ListPreferenceSetsResponseOut": "_migrationcenter_189_ListPreferenceSetsResponseOut",
        "ReportSummaryChartDataDataPointIn": "_migrationcenter_190_ReportSummaryChartDataDataPointIn",
        "ReportSummaryChartDataDataPointOut": "_migrationcenter_191_ReportSummaryChartDataDataPointOut",
        "AggregationResultSumIn": "_migrationcenter_192_AggregationResultSumIn",
        "AggregationResultSumOut": "_migrationcenter_193_AggregationResultSumOut",
        "DailyResourceUsageAggregationCPUIn": "_migrationcenter_194_DailyResourceUsageAggregationCPUIn",
        "DailyResourceUsageAggregationCPUOut": "_migrationcenter_195_DailyResourceUsageAggregationCPUOut",
        "ListOperationsResponseIn": "_migrationcenter_196_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_migrationcenter_197_ListOperationsResponseOut",
        "OpenFileListIn": "_migrationcenter_198_OpenFileListIn",
        "OpenFileListOut": "_migrationcenter_199_OpenFileListOut",
        "SettingsIn": "_migrationcenter_200_SettingsIn",
        "SettingsOut": "_migrationcenter_201_SettingsOut",
        "AggregationResultHistogramBucketIn": "_migrationcenter_202_AggregationResultHistogramBucketIn",
        "AggregationResultHistogramBucketOut": "_migrationcenter_203_AggregationResultHistogramBucketOut",
        "GuestConfigDetailsIn": "_migrationcenter_204_GuestConfigDetailsIn",
        "GuestConfigDetailsOut": "_migrationcenter_205_GuestConfigDetailsOut",
        "NfsExportListIn": "_migrationcenter_206_NfsExportListIn",
        "NfsExportListOut": "_migrationcenter_207_NfsExportListOut",
        "ImportJobIn": "_migrationcenter_208_ImportJobIn",
        "ImportJobOut": "_migrationcenter_209_ImportJobOut",
        "DailyResourceUsageAggregationDiskIn": "_migrationcenter_210_DailyResourceUsageAggregationDiskIn",
        "DailyResourceUsageAggregationDiskOut": "_migrationcenter_211_DailyResourceUsageAggregationDiskOut",
        "NetworkAdapterDetailsIn": "_migrationcenter_212_NetworkAdapterDetailsIn",
        "NetworkAdapterDetailsOut": "_migrationcenter_213_NetworkAdapterDetailsOut",
        "DailyResourceUsageAggregationStatsIn": "_migrationcenter_214_DailyResourceUsageAggregationStatsIn",
        "DailyResourceUsageAggregationStatsOut": "_migrationcenter_215_DailyResourceUsageAggregationStatsOut",
        "AggregationCountIn": "_migrationcenter_216_AggregationCountIn",
        "AggregationCountOut": "_migrationcenter_217_AggregationCountOut",
        "OperationMetadataIn": "_migrationcenter_218_OperationMetadataIn",
        "OperationMetadataOut": "_migrationcenter_219_OperationMetadataOut",
        "AddAssetsToGroupRequestIn": "_migrationcenter_220_AddAssetsToGroupRequestIn",
        "AddAssetsToGroupRequestOut": "_migrationcenter_221_AddAssetsToGroupRequestOut",
        "ReportSummaryGroupFindingIn": "_migrationcenter_222_ReportSummaryGroupFindingIn",
        "ReportSummaryGroupFindingOut": "_migrationcenter_223_ReportSummaryGroupFindingOut",
        "RemoveAssetsFromGroupRequestIn": "_migrationcenter_224_RemoveAssetsFromGroupRequestIn",
        "RemoveAssetsFromGroupRequestOut": "_migrationcenter_225_RemoveAssetsFromGroupRequestOut",
        "MigrationInsightIn": "_migrationcenter_226_MigrationInsightIn",
        "MigrationInsightOut": "_migrationcenter_227_MigrationInsightOut",
        "GenericPlatformDetailsIn": "_migrationcenter_228_GenericPlatformDetailsIn",
        "GenericPlatformDetailsOut": "_migrationcenter_229_GenericPlatformDetailsOut",
        "DiskUsageSampleIn": "_migrationcenter_230_DiskUsageSampleIn",
        "DiskUsageSampleOut": "_migrationcenter_231_DiskUsageSampleOut",
        "ListReportConfigsResponseIn": "_migrationcenter_232_ListReportConfigsResponseIn",
        "ListReportConfigsResponseOut": "_migrationcenter_233_ListReportConfigsResponseOut",
        "CancelOperationRequestIn": "_migrationcenter_234_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_migrationcenter_235_CancelOperationRequestOut",
        "FramesIn": "_migrationcenter_236_FramesIn",
        "FramesOut": "_migrationcenter_237_FramesOut",
        "RuntimeNetworkInfoIn": "_migrationcenter_238_RuntimeNetworkInfoIn",
        "RuntimeNetworkInfoOut": "_migrationcenter_239_RuntimeNetworkInfoOut",
        "MachinePreferencesIn": "_migrationcenter_240_MachinePreferencesIn",
        "MachinePreferencesOut": "_migrationcenter_241_MachinePreferencesOut",
        "ListErrorFramesResponseIn": "_migrationcenter_242_ListErrorFramesResponseIn",
        "ListErrorFramesResponseOut": "_migrationcenter_243_ListErrorFramesResponseOut",
        "AssetIn": "_migrationcenter_244_AssetIn",
        "AssetOut": "_migrationcenter_245_AssetOut",
        "FileValidationReportIn": "_migrationcenter_246_FileValidationReportIn",
        "FileValidationReportOut": "_migrationcenter_247_FileValidationReportOut",
        "VirtualMachinePreferencesIn": "_migrationcenter_248_VirtualMachinePreferencesIn",
        "VirtualMachinePreferencesOut": "_migrationcenter_249_VirtualMachinePreferencesOut",
        "NetworkUsageSampleIn": "_migrationcenter_250_NetworkUsageSampleIn",
        "NetworkUsageSampleOut": "_migrationcenter_251_NetworkUsageSampleOut",
        "DailyResourceUsageAggregationIn": "_migrationcenter_252_DailyResourceUsageAggregationIn",
        "DailyResourceUsageAggregationOut": "_migrationcenter_253_DailyResourceUsageAggregationOut",
        "PreferenceSetIn": "_migrationcenter_254_PreferenceSetIn",
        "PreferenceSetOut": "_migrationcenter_255_PreferenceSetOut",
        "SourceIn": "_migrationcenter_256_SourceIn",
        "SourceOut": "_migrationcenter_257_SourceOut",
        "VirtualMachineDetailsIn": "_migrationcenter_258_VirtualMachineDetailsIn",
        "VirtualMachineDetailsOut": "_migrationcenter_259_VirtualMachineDetailsOut",
        "PayloadFileIn": "_migrationcenter_260_PayloadFileIn",
        "PayloadFileOut": "_migrationcenter_261_PayloadFileOut",
        "AzureVmPlatformDetailsIn": "_migrationcenter_262_AzureVmPlatformDetailsIn",
        "AzureVmPlatformDetailsOut": "_migrationcenter_263_AzureVmPlatformDetailsOut",
        "CpuUsageSampleIn": "_migrationcenter_264_CpuUsageSampleIn",
        "CpuUsageSampleOut": "_migrationcenter_265_CpuUsageSampleOut",
        "RunningProcessListIn": "_migrationcenter_266_RunningProcessListIn",
        "RunningProcessListOut": "_migrationcenter_267_RunningProcessListOut",
        "ReportAssetFramesResponseIn": "_migrationcenter_268_ReportAssetFramesResponseIn",
        "ReportAssetFramesResponseOut": "_migrationcenter_269_ReportAssetFramesResponseOut",
        "HostsEntryIn": "_migrationcenter_270_HostsEntryIn",
        "HostsEntryOut": "_migrationcenter_271_HostsEntryOut",
        "VirtualMachineArchitectureDetailsIn": "_migrationcenter_272_VirtualMachineArchitectureDetailsIn",
        "VirtualMachineArchitectureDetailsOut": "_migrationcenter_273_VirtualMachineArchitectureDetailsOut",
        "ListImportJobsResponseIn": "_migrationcenter_274_ListImportJobsResponseIn",
        "ListImportJobsResponseOut": "_migrationcenter_275_ListImportJobsResponseOut",
        "NetworkAddressIn": "_migrationcenter_276_NetworkAddressIn",
        "NetworkAddressOut": "_migrationcenter_277_NetworkAddressOut",
        "MoneyIn": "_migrationcenter_278_MoneyIn",
        "MoneyOut": "_migrationcenter_279_MoneyOut",
        "ReportSummaryGroupPreferenceSetFindingIn": "_migrationcenter_280_ReportSummaryGroupPreferenceSetFindingIn",
        "ReportSummaryGroupPreferenceSetFindingOut": "_migrationcenter_281_ReportSummaryGroupPreferenceSetFindingOut",
        "GuestOsDetailsIn": "_migrationcenter_282_GuestOsDetailsIn",
        "GuestOsDetailsOut": "_migrationcenter_283_GuestOsDetailsOut",
        "RunningProcessIn": "_migrationcenter_284_RunningProcessIn",
        "RunningProcessOut": "_migrationcenter_285_RunningProcessOut",
        "GroupIn": "_migrationcenter_286_GroupIn",
        "GroupOut": "_migrationcenter_287_GroupOut",
        "ExecutionReportIn": "_migrationcenter_288_ExecutionReportIn",
        "ExecutionReportOut": "_migrationcenter_289_ExecutionReportOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["ComputeEngineMigrationTargetIn"] = t.struct(
        {"shape": t.proxy(renames["ComputeEngineShapeDescriptorIn"]).optional()}
    ).named(renames["ComputeEngineMigrationTargetIn"])
    types["ComputeEngineMigrationTargetOut"] = t.struct(
        {
            "shape": t.proxy(renames["ComputeEngineShapeDescriptorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeEngineMigrationTargetOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
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
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["InsightIn"] = t.struct({"_": t.string().optional()}).named(
        renames["InsightIn"]
    )
    types["InsightOut"] = t.struct(
        {
            "migrationInsight": t.proxy(renames["MigrationInsightOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsightOut"])
    types["NetworkAddressListIn"] = t.struct(
        {"addresses": t.array(t.proxy(renames["NetworkAddressIn"])).optional()}
    ).named(renames["NetworkAddressListIn"])
    types["NetworkAddressListOut"] = t.struct(
        {
            "addresses": t.array(t.proxy(renames["NetworkAddressOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkAddressListOut"])
    types["ImportRowErrorIn"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["ImportErrorIn"])).optional(),
            "rowNumber": t.integer().optional(),
            "vmUuid": t.string().optional(),
            "vmName": t.string().optional(),
        }
    ).named(renames["ImportRowErrorIn"])
    types["ImportRowErrorOut"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["ImportErrorOut"])).optional(),
            "rowNumber": t.integer().optional(),
            "vmUuid": t.string().optional(),
            "vmName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportRowErrorOut"])
    types["AggregationIn"] = t.struct(
        {
            "frequency": t.proxy(renames["AggregationFrequencyIn"]).optional(),
            "count": t.proxy(renames["AggregationCountIn"]).optional(),
            "sum": t.proxy(renames["AggregationSumIn"]).optional(),
            "field": t.string().optional(),
            "histogram": t.proxy(renames["AggregationHistogramIn"]).optional(),
        }
    ).named(renames["AggregationIn"])
    types["AggregationOut"] = t.struct(
        {
            "frequency": t.proxy(renames["AggregationFrequencyOut"]).optional(),
            "count": t.proxy(renames["AggregationCountOut"]).optional(),
            "sum": t.proxy(renames["AggregationSumOut"]).optional(),
            "field": t.string().optional(),
            "histogram": t.proxy(renames["AggregationHistogramOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationOut"])
    types["FstabEntryListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["FstabEntryIn"])).optional()}
    ).named(renames["FstabEntryListIn"])
    types["FstabEntryListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["FstabEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FstabEntryListOut"])
    types["AggregationResultCountIn"] = t.struct({"value": t.string()}).named(
        renames["AggregationResultCountIn"]
    )
    types["AggregationResultCountOut"] = t.struct(
        {"value": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AggregationResultCountOut"])
    types["ReportSummaryAssetAggregateStatsIn"] = t.struct(
        {
            "assetAge": t.proxy(renames["ReportSummaryChartDataIn"]).optional(),
            "memoryUtilization": t.proxy(
                renames["ReportSummaryChartDataIn"]
            ).optional(),
            "coreCountHistogram": t.proxy(
                renames["ReportSummaryHistogramChartDataIn"]
            ).optional(),
            "totalMemoryBytes": t.string().optional(),
            "totalAssets": t.string().optional(),
            "totalCores": t.string().optional(),
            "storageBytesHistogram": t.proxy(
                renames["ReportSummaryHistogramChartDataIn"]
            ).optional(),
            "operatingSystem": t.proxy(renames["ReportSummaryChartDataIn"]).optional(),
            "storageUtilizationChart": t.proxy(
                renames["ReportSummaryUtilizationChartDataIn"]
            ).optional(),
            "totalStorageBytes": t.string().optional(),
            "memoryBytesHistogram": t.proxy(
                renames["ReportSummaryHistogramChartDataIn"]
            ).optional(),
            "storageUtilization": t.proxy(
                renames["ReportSummaryChartDataIn"]
            ).optional(),
            "memoryUtilizationChart": t.proxy(
                renames["ReportSummaryUtilizationChartDataIn"]
            ).optional(),
        }
    ).named(renames["ReportSummaryAssetAggregateStatsIn"])
    types["ReportSummaryAssetAggregateStatsOut"] = t.struct(
        {
            "assetAge": t.proxy(renames["ReportSummaryChartDataOut"]).optional(),
            "memoryUtilization": t.proxy(
                renames["ReportSummaryChartDataOut"]
            ).optional(),
            "coreCountHistogram": t.proxy(
                renames["ReportSummaryHistogramChartDataOut"]
            ).optional(),
            "totalMemoryBytes": t.string().optional(),
            "totalAssets": t.string().optional(),
            "totalCores": t.string().optional(),
            "storageBytesHistogram": t.proxy(
                renames["ReportSummaryHistogramChartDataOut"]
            ).optional(),
            "operatingSystem": t.proxy(renames["ReportSummaryChartDataOut"]).optional(),
            "storageUtilizationChart": t.proxy(
                renames["ReportSummaryUtilizationChartDataOut"]
            ).optional(),
            "totalStorageBytes": t.string().optional(),
            "memoryBytesHistogram": t.proxy(
                renames["ReportSummaryHistogramChartDataOut"]
            ).optional(),
            "storageUtilization": t.proxy(
                renames["ReportSummaryChartDataOut"]
            ).optional(),
            "memoryUtilizationChart": t.proxy(
                renames["ReportSummaryUtilizationChartDataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryAssetAggregateStatsOut"])
    types["ImportDataFileIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "format": t.string(),
            "uploadFileInfo": t.proxy(renames["UploadFileInfoIn"]).optional(),
        }
    ).named(renames["ImportDataFileIn"])
    types["ImportDataFileOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "format": t.string(),
            "uploadFileInfo": t.proxy(renames["UploadFileInfoOut"]).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportDataFileOut"])
    types["PhysicalPlatformDetailsIn"] = t.struct(
        {"location": t.string().optional()}
    ).named(renames["PhysicalPlatformDetailsIn"])
    types["PhysicalPlatformDetailsOut"] = t.struct(
        {
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhysicalPlatformDetailsOut"])
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
    types["AssetFrameIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "performanceSamples": t.array(
                t.proxy(renames["PerformanceSampleIn"])
            ).optional(),
            "traceToken": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "reportTime": t.string().optional(),
            "virtualMachineDetails": t.proxy(
                renames["VirtualMachineDetailsIn"]
            ).optional(),
        }
    ).named(renames["AssetFrameIn"])
    types["AssetFrameOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "performanceSamples": t.array(
                t.proxy(renames["PerformanceSampleOut"])
            ).optional(),
            "traceToken": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "reportTime": t.string().optional(),
            "virtualMachineDetails": t.proxy(
                renames["VirtualMachineDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetFrameOut"])
    types["AggregateAssetsValuesResponseIn"] = t.struct(
        {"results": t.array(t.proxy(renames["AggregationResultIn"])).optional()}
    ).named(renames["AggregateAssetsValuesResponseIn"])
    types["AggregateAssetsValuesResponseOut"] = t.struct(
        {
            "results": t.array(t.proxy(renames["AggregationResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregateAssetsValuesResponseOut"])
    types["PerformanceSampleIn"] = t.struct(
        {
            "memory": t.proxy(renames["MemoryUsageSampleIn"]).optional(),
            "sampleTime": t.string().optional(),
            "network": t.proxy(renames["NetworkUsageSampleIn"]).optional(),
            "disk": t.proxy(renames["DiskUsageSampleIn"]).optional(),
            "cpu": t.proxy(renames["CpuUsageSampleIn"]).optional(),
        }
    ).named(renames["PerformanceSampleIn"])
    types["PerformanceSampleOut"] = t.struct(
        {
            "memory": t.proxy(renames["MemoryUsageSampleOut"]).optional(),
            "sampleTime": t.string().optional(),
            "network": t.proxy(renames["NetworkUsageSampleOut"]).optional(),
            "disk": t.proxy(renames["DiskUsageSampleOut"]).optional(),
            "cpu": t.proxy(renames["CpuUsageSampleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerformanceSampleOut"])
    types["RunningServiceListIn"] = t.struct(
        {"services": t.array(t.proxy(renames["RunningServiceIn"])).optional()}
    ).named(renames["RunningServiceListIn"])
    types["RunningServiceListOut"] = t.struct(
        {
            "services": t.array(t.proxy(renames["RunningServiceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunningServiceListOut"])
    types["ComputeEngineShapeDescriptorIn"] = t.struct(
        {
            "machineType": t.string().optional(),
            "series": t.string().optional(),
            "physicalCoreCount": t.integer().optional(),
            "logicalCoreCount": t.integer().optional(),
            "memoryMb": t.integer().optional(),
        }
    ).named(renames["ComputeEngineShapeDescriptorIn"])
    types["ComputeEngineShapeDescriptorOut"] = t.struct(
        {
            "machineType": t.string().optional(),
            "series": t.string().optional(),
            "physicalCoreCount": t.integer().optional(),
            "logicalCoreCount": t.integer().optional(),
            "memoryMb": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeEngineShapeDescriptorOut"])
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
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportConfigOut"])
    types["NetworkConnectionListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["NetworkConnectionIn"])).optional()}
    ).named(renames["NetworkConnectionListIn"])
    types["NetworkConnectionListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["NetworkConnectionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConnectionListOut"])
    types["BiosDetailsIn"] = t.struct(
        {
            "smbiosUuid": t.string().optional(),
            "biosVersion": t.string().optional(),
            "biosReleaseDate": t.string().optional(),
            "biosName": t.string().optional(),
            "biosManufacturer": t.string().optional(),
        }
    ).named(renames["BiosDetailsIn"])
    types["BiosDetailsOut"] = t.struct(
        {
            "smbiosUuid": t.string().optional(),
            "biosVersion": t.string().optional(),
            "biosReleaseDate": t.string().optional(),
            "biosName": t.string().optional(),
            "biosManufacturer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BiosDetailsOut"])
    types["PlatformDetailsIn"] = t.struct(
        {
            "azureVmDetails": t.proxy(renames["AzureVmPlatformDetailsIn"]).optional(),
            "awsEc2Details": t.proxy(renames["AwsEc2PlatformDetailsIn"]).optional(),
            "vmwareDetails": t.proxy(renames["VmwarePlatformDetailsIn"]).optional(),
            "physicalDetails": t.proxy(renames["PhysicalPlatformDetailsIn"]).optional(),
            "genericDetails": t.proxy(renames["GenericPlatformDetailsIn"]).optional(),
        }
    ).named(renames["PlatformDetailsIn"])
    types["PlatformDetailsOut"] = t.struct(
        {
            "azureVmDetails": t.proxy(renames["AzureVmPlatformDetailsOut"]).optional(),
            "awsEc2Details": t.proxy(renames["AwsEc2PlatformDetailsOut"]).optional(),
            "vmwareDetails": t.proxy(renames["VmwarePlatformDetailsOut"]).optional(),
            "physicalDetails": t.proxy(
                renames["PhysicalPlatformDetailsOut"]
            ).optional(),
            "genericDetails": t.proxy(renames["GenericPlatformDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlatformDetailsOut"])
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
    types["VirtualMachineDiskDetailsIn"] = t.struct(
        {
            "hddTotalFreeBytes": t.string().optional(),
            "hddTotalCapacityBytes": t.string().optional(),
            "disks": t.proxy(renames["DiskEntryListIn"]).optional(),
            "lsblkJson": t.string().optional(),
        }
    ).named(renames["VirtualMachineDiskDetailsIn"])
    types["VirtualMachineDiskDetailsOut"] = t.struct(
        {
            "hddTotalFreeBytes": t.string().optional(),
            "hddTotalCapacityBytes": t.string().optional(),
            "disks": t.proxy(renames["DiskEntryListOut"]).optional(),
            "lsblkJson": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualMachineDiskDetailsOut"])
    types["MemoryUsageSampleIn"] = t.struct(
        {"utilizedPercentage": t.number().optional()}
    ).named(renames["MemoryUsageSampleIn"])
    types["MemoryUsageSampleOut"] = t.struct(
        {
            "utilizedPercentage": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemoryUsageSampleOut"])
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
    types["NetworkConnectionIn"] = t.struct(
        {
            "remoteIpAddress": t.string().optional(),
            "pid": t.string().optional(),
            "localPort": t.integer().optional(),
            "protocol": t.string().optional(),
            "remotePort": t.integer().optional(),
            "localIpAddress": t.string().optional(),
            "state": t.string().optional(),
            "processName": t.string().optional(),
        }
    ).named(renames["NetworkConnectionIn"])
    types["NetworkConnectionOut"] = t.struct(
        {
            "remoteIpAddress": t.string().optional(),
            "pid": t.string().optional(),
            "localPort": t.integer().optional(),
            "protocol": t.string().optional(),
            "remotePort": t.integer().optional(),
            "localIpAddress": t.string().optional(),
            "state": t.string().optional(),
            "processName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConnectionOut"])
    types["DateTimeIn"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "year": t.integer().optional(),
            "hours": t.integer().optional(),
            "utcOffset": t.string().optional(),
            "month": t.integer().optional(),
            "timeZone": t.proxy(renames["TimeZoneIn"]).optional(),
            "minutes": t.integer().optional(),
            "day": t.integer().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["DateTimeIn"])
    types["DateTimeOut"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "year": t.integer().optional(),
            "hours": t.integer().optional(),
            "utcOffset": t.string().optional(),
            "month": t.integer().optional(),
            "timeZone": t.proxy(renames["TimeZoneOut"]).optional(),
            "minutes": t.integer().optional(),
            "day": t.integer().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateTimeOut"])
    types["ReportSummaryMachineFindingIn"] = t.struct(
        {
            "allocatedRegions": t.array(t.string()).optional(),
            "machineSeriesAllocations": t.array(
                t.proxy(renames["ReportSummaryMachineSeriesAllocationIn"])
            ).optional(),
            "allocatedDiskTypes": t.array(t.string()).optional(),
            "allocatedAssetCount": t.string().optional(),
        }
    ).named(renames["ReportSummaryMachineFindingIn"])
    types["ReportSummaryMachineFindingOut"] = t.struct(
        {
            "allocatedRegions": t.array(t.string()).optional(),
            "machineSeriesAllocations": t.array(
                t.proxy(renames["ReportSummaryMachineSeriesAllocationOut"])
            ).optional(),
            "allocatedDiskTypes": t.array(t.string()).optional(),
            "allocatedAssetCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryMachineFindingOut"])
    types["DiskEntryListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["DiskEntryIn"])).optional()}
    ).named(renames["DiskEntryListIn"])
    types["DiskEntryListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["DiskEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskEntryListOut"])
    types["DiskPartitionListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["DiskPartitionIn"])).optional()}
    ).named(renames["DiskPartitionListIn"])
    types["DiskPartitionListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["DiskPartitionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskPartitionListOut"])
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
    types["HostsEntryListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["HostsEntryIn"])).optional()}
    ).named(renames["HostsEntryListIn"])
    types["HostsEntryListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["HostsEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HostsEntryListOut"])
    types["AggregationSumIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AggregationSumIn"]
    )
    types["AggregationSumOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AggregationSumOut"])
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
    types["AggregationResultFrequencyIn"] = t.struct(
        {"values": t.struct({"_": t.string().optional()})}
    ).named(renames["AggregationResultFrequencyIn"])
    types["AggregationResultFrequencyOut"] = t.struct(
        {
            "values": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationResultFrequencyOut"])
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
    types["VmwareDiskConfigIn"] = t.struct(
        {
            "rdmCompatibilityMode": t.string().optional(),
            "vmdkDiskMode": t.string().optional(),
            "shared": t.boolean().optional(),
            "backingType": t.string().optional(),
        }
    ).named(renames["VmwareDiskConfigIn"])
    types["VmwareDiskConfigOut"] = t.struct(
        {
            "rdmCompatibilityMode": t.string().optional(),
            "vmdkDiskMode": t.string().optional(),
            "shared": t.boolean().optional(),
            "backingType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareDiskConfigOut"])
    types["VmwarePlatformDetailsIn"] = t.struct(
        {
            "esxVersion": t.string().optional(),
            "osid": t.string().optional(),
            "vcenterVersion": t.string().optional(),
        }
    ).named(renames["VmwarePlatformDetailsIn"])
    types["VmwarePlatformDetailsOut"] = t.struct(
        {
            "esxVersion": t.string().optional(),
            "osid": t.string().optional(),
            "vcenterVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwarePlatformDetailsOut"])
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
    types["RegionPreferencesIn"] = t.struct(
        {"preferredRegions": t.array(t.string()).optional()}
    ).named(renames["RegionPreferencesIn"])
    types["RegionPreferencesOut"] = t.struct(
        {
            "preferredRegions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionPreferencesOut"])
    types["FstabEntryIn"] = t.struct(
        {
            "vfstype": t.string().optional(),
            "passno": t.integer().optional(),
            "mntops": t.string().optional(),
            "spec": t.string().optional(),
            "file": t.string().optional(),
            "freq": t.integer().optional(),
        }
    ).named(renames["FstabEntryIn"])
    types["FstabEntryOut"] = t.struct(
        {
            "vfstype": t.string().optional(),
            "passno": t.integer().optional(),
            "mntops": t.string().optional(),
            "spec": t.string().optional(),
            "file": t.string().optional(),
            "freq": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FstabEntryOut"])
    types["MachineSeriesIn"] = t.struct({"code": t.string().optional()}).named(
        renames["MachineSeriesIn"]
    )
    types["MachineSeriesOut"] = t.struct(
        {
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MachineSeriesOut"])
    types["ListReportsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "reports": t.array(t.proxy(renames["ReportIn"])).optional(),
        }
    ).named(renames["ListReportsResponseIn"])
    types["ListReportsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "reports": t.array(t.proxy(renames["ReportOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReportsResponseOut"])
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
    types["RunImportJobRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["RunImportJobRequestIn"])
    types["RunImportJobRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunImportJobRequestOut"])
    types["BatchUpdateAssetsResponseIn"] = t.struct(
        {"assets": t.array(t.proxy(renames["AssetIn"])).optional()}
    ).named(renames["BatchUpdateAssetsResponseIn"])
    types["BatchUpdateAssetsResponseOut"] = t.struct(
        {
            "assets": t.array(t.proxy(renames["AssetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateAssetsResponseOut"])
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["ErrorFrameIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ErrorFrameIn"]
    )
    types["ErrorFrameOut"] = t.struct(
        {
            "name": t.string().optional(),
            "ingestionTime": t.string().optional(),
            "violations": t.array(
                t.proxy(renames["FrameViolationEntryOut"])
            ).optional(),
            "originalFrame": t.proxy(renames["AssetFrameOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorFrameOut"])
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
    types["ValidateImportJobRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["ValidateImportJobRequestIn"])
    types["ValidateImportJobRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateImportJobRequestOut"])
    types["GuestRuntimeDetailsIn"] = t.struct(
        {
            "services": t.proxy(renames["RunningServiceListIn"]).optional(),
            "networkInfo": t.proxy(renames["RuntimeNetworkInfoIn"]).optional(),
            "domain": t.string().optional(),
            "installedApps": t.proxy(
                renames["GuestInstalledApplicationListIn"]
            ).optional(),
            "lastUptime": t.proxy(renames["DateIn"]).optional(),
            "machineName": t.string().optional(),
            "processes": t.proxy(renames["RunningProcessListIn"]).optional(),
            "openFileList": t.proxy(renames["OpenFileListIn"]).optional(),
        }
    ).named(renames["GuestRuntimeDetailsIn"])
    types["GuestRuntimeDetailsOut"] = t.struct(
        {
            "services": t.proxy(renames["RunningServiceListOut"]).optional(),
            "networkInfo": t.proxy(renames["RuntimeNetworkInfoOut"]).optional(),
            "domain": t.string().optional(),
            "installedApps": t.proxy(
                renames["GuestInstalledApplicationListOut"]
            ).optional(),
            "lastUptime": t.proxy(renames["DateOut"]).optional(),
            "machineName": t.string().optional(),
            "processes": t.proxy(renames["RunningProcessListOut"]).optional(),
            "openFileList": t.proxy(renames["OpenFileListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestRuntimeDetailsOut"])
    types["ReportIn"] = t.struct(
        {
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["ReportIn"])
    types["ReportOut"] = t.struct(
        {
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "summary": t.proxy(renames["ReportSummaryOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportOut"])
    types["DiskEntryIn"] = t.struct(
        {
            "hwAddress": t.string().optional(),
            "interfaceType": t.string().optional(),
            "vmwareConfig": t.proxy(renames["VmwareDiskConfigIn"]).optional(),
            "diskLabel": t.string().optional(),
            "totalCapacityBytes": t.string().optional(),
            "diskLabelType": t.string().optional(),
            "status": t.string().optional(),
            "totalFreeBytes": t.string().optional(),
            "partitions": t.proxy(renames["DiskPartitionListIn"]).optional(),
        }
    ).named(renames["DiskEntryIn"])
    types["DiskEntryOut"] = t.struct(
        {
            "hwAddress": t.string().optional(),
            "interfaceType": t.string().optional(),
            "vmwareConfig": t.proxy(renames["VmwareDiskConfigOut"]).optional(),
            "diskLabel": t.string().optional(),
            "totalCapacityBytes": t.string().optional(),
            "diskLabelType": t.string().optional(),
            "status": t.string().optional(),
            "totalFreeBytes": t.string().optional(),
            "partitions": t.proxy(renames["DiskPartitionListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskEntryOut"])
    types["AssetListIn"] = t.struct({"assetIds": t.array(t.string())}).named(
        renames["AssetListIn"]
    )
    types["AssetListOut"] = t.struct(
        {
            "assetIds": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetListOut"])
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
    types["AggregationFrequencyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AggregationFrequencyIn"]
    )
    types["AggregationFrequencyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AggregationFrequencyOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["VmwareEngineMigrationTargetIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["VmwareEngineMigrationTargetIn"])
    types["VmwareEngineMigrationTargetOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VmwareEngineMigrationTargetOut"])
    types["VirtualMachineNetworkDetailsIn"] = t.struct(
        {
            "networkAdapters": t.proxy(renames["NetworkAdapterListIn"]).optional(),
            "primaryIpAddress": t.string().optional(),
            "primaryMacAddress": t.string().optional(),
            "defaultGw": t.string().optional(),
            "publicIpAddress": t.string().optional(),
        }
    ).named(renames["VirtualMachineNetworkDetailsIn"])
    types["VirtualMachineNetworkDetailsOut"] = t.struct(
        {
            "networkAdapters": t.proxy(renames["NetworkAdapterListOut"]).optional(),
            "primaryIpAddress": t.string().optional(),
            "primaryMacAddress": t.string().optional(),
            "defaultGw": t.string().optional(),
            "publicIpAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualMachineNetworkDetailsOut"])
    types["GoogleKubernetesEngineMigrationTargetIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleKubernetesEngineMigrationTargetIn"])
    types["GoogleKubernetesEngineMigrationTargetOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleKubernetesEngineMigrationTargetOut"])
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
    types["FitDescriptorIn"] = t.struct({"fitLevel": t.string().optional()}).named(
        renames["FitDescriptorIn"]
    )
    types["FitDescriptorOut"] = t.struct(
        {
            "fitLevel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FitDescriptorOut"])
    types["GuestInstalledApplicationIn"] = t.struct(
        {
            "vendor": t.string().optional(),
            "name": t.string().optional(),
            "version": t.string().optional(),
            "path": t.string().optional(),
            "time": t.string().optional(),
        }
    ).named(renames["GuestInstalledApplicationIn"])
    types["GuestInstalledApplicationOut"] = t.struct(
        {
            "vendor": t.string().optional(),
            "name": t.string().optional(),
            "version": t.string().optional(),
            "path": t.string().optional(),
            "time": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestInstalledApplicationOut"])
    types["DateIn"] = t.struct(
        {
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["BatchUpdateAssetsRequestIn"] = t.struct(
        {"requests": t.array(t.proxy(renames["UpdateAssetRequestIn"]))}
    ).named(renames["BatchUpdateAssetsRequestIn"])
    types["BatchUpdateAssetsRequestOut"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["UpdateAssetRequestOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateAssetsRequestOut"])
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
    types["RunningServiceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "state": t.string().optional(),
            "exePath": t.string().optional(),
            "status": t.string().optional(),
            "startMode": t.string().optional(),
            "cmdline": t.string().optional(),
            "pid": t.string().optional(),
        }
    ).named(renames["RunningServiceIn"])
    types["RunningServiceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "state": t.string().optional(),
            "exePath": t.string().optional(),
            "status": t.string().optional(),
            "startMode": t.string().optional(),
            "cmdline": t.string().optional(),
            "pid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunningServiceOut"])
    types["AggregationHistogramIn"] = t.struct(
        {"lowerBounds": t.array(t.number()).optional()}
    ).named(renames["AggregationHistogramIn"])
    types["AggregationHistogramOut"] = t.struct(
        {
            "lowerBounds": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationHistogramOut"])
    types["InsightListIn"] = t.struct({"_": t.string().optional()}).named(
        renames["InsightListIn"]
    )
    types["InsightListOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "insights": t.array(t.proxy(renames["InsightOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsightListOut"])
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
    types["ReportSummaryMachineSeriesAllocationIn"] = t.struct(
        {
            "machineSeries": t.proxy(renames["MachineSeriesIn"]).optional(),
            "allocatedAssetCount": t.string().optional(),
        }
    ).named(renames["ReportSummaryMachineSeriesAllocationIn"])
    types["ReportSummaryMachineSeriesAllocationOut"] = t.struct(
        {
            "machineSeries": t.proxy(renames["MachineSeriesOut"]).optional(),
            "allocatedAssetCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryMachineSeriesAllocationOut"])
    types["DiskPartitionIn"] = t.struct(
        {
            "mountPoint": t.string().optional(),
            "type": t.string().optional(),
            "freeBytes": t.string().optional(),
            "subPartitions": t.proxy(renames["DiskPartitionListIn"]).optional(),
            "fileSystem": t.string().optional(),
            "capacityBytes": t.string().optional(),
            "uuid": t.string().optional(),
        }
    ).named(renames["DiskPartitionIn"])
    types["DiskPartitionOut"] = t.struct(
        {
            "mountPoint": t.string().optional(),
            "type": t.string().optional(),
            "freeBytes": t.string().optional(),
            "subPartitions": t.proxy(renames["DiskPartitionListOut"]).optional(),
            "fileSystem": t.string().optional(),
            "capacityBytes": t.string().optional(),
            "uuid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskPartitionOut"])
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
    types["AggregationResultIn"] = t.struct(
        {
            "count": t.proxy(renames["AggregationResultCountIn"]),
            "histogram": t.proxy(renames["AggregationResultHistogramIn"]),
            "field": t.string(),
            "sum": t.proxy(renames["AggregationResultSumIn"]),
            "frequency": t.proxy(renames["AggregationResultFrequencyIn"]),
        }
    ).named(renames["AggregationResultIn"])
    types["AggregationResultOut"] = t.struct(
        {
            "count": t.proxy(renames["AggregationResultCountOut"]),
            "histogram": t.proxy(renames["AggregationResultHistogramOut"]),
            "field": t.string(),
            "sum": t.proxy(renames["AggregationResultSumOut"]),
            "frequency": t.proxy(renames["AggregationResultFrequencyOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationResultOut"])
    types["ListPreferenceSetsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "preferenceSets": t.array(t.proxy(renames["PreferenceSetIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListPreferenceSetsResponseIn"])
    types["ListPreferenceSetsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "preferenceSets": t.array(t.proxy(renames["PreferenceSetOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPreferenceSetsResponseOut"])
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
    types["AggregationResultSumIn"] = t.struct({"value": t.number()}).named(
        renames["AggregationResultSumIn"]
    )
    types["AggregationResultSumOut"] = t.struct(
        {"value": t.number(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AggregationResultSumOut"])
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
    types["OpenFileListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["OpenFileDetailsIn"])).optional()}
    ).named(renames["OpenFileListIn"])
    types["OpenFileListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["OpenFileDetailsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OpenFileListOut"])
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
    types["GuestConfigDetailsIn"] = t.struct(
        {
            "hosts": t.proxy(renames["HostsEntryListIn"]).optional(),
            "fstab": t.proxy(renames["FstabEntryListIn"]).optional(),
            "selinux": t.proxy(renames["SelinuxIn"]).optional(),
            "nfsExports": t.proxy(renames["NfsExportListIn"]).optional(),
            "issue": t.string().optional(),
        }
    ).named(renames["GuestConfigDetailsIn"])
    types["GuestConfigDetailsOut"] = t.struct(
        {
            "hosts": t.proxy(renames["HostsEntryListOut"]).optional(),
            "fstab": t.proxy(renames["FstabEntryListOut"]).optional(),
            "selinux": t.proxy(renames["SelinuxOut"]).optional(),
            "nfsExports": t.proxy(renames["NfsExportListOut"]).optional(),
            "issue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestConfigDetailsOut"])
    types["NfsExportListIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["NfsExportIn"])).optional()}
    ).named(renames["NfsExportListIn"])
    types["NfsExportListOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["NfsExportOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NfsExportListOut"])
    types["ImportJobIn"] = t.struct(
        {
            "gcsPayload": t.proxy(renames["GCSPayloadInfoIn"]).optional(),
            "inlinePayload": t.proxy(renames["InlinePayloadInfoIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "assetSource": t.string(),
        }
    ).named(renames["ImportJobIn"])
    types["ImportJobOut"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "gcsPayload": t.proxy(renames["GCSPayloadInfoOut"]).optional(),
            "createTime": t.string().optional(),
            "inlinePayload": t.proxy(renames["InlinePayloadInfoOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "validationReport": t.proxy(renames["ValidationReportOut"]).optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "executionReport": t.proxy(renames["ExecutionReportOut"]).optional(),
            "updateTime": t.string().optional(),
            "assetSource": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportJobOut"])
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
    types["DailyResourceUsageAggregationStatsIn"] = t.struct(
        {
            "median": t.number().optional(),
            "peak": t.number().optional(),
            "average": t.number().optional(),
            "ninteyFifthPercentile": t.number().optional(),
        }
    ).named(renames["DailyResourceUsageAggregationStatsIn"])
    types["DailyResourceUsageAggregationStatsOut"] = t.struct(
        {
            "median": t.number().optional(),
            "peak": t.number().optional(),
            "average": t.number().optional(),
            "ninteyFifthPercentile": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DailyResourceUsageAggregationStatsOut"])
    types["AggregationCountIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AggregationCountIn"]
    )
    types["AggregationCountOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AggregationCountOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "statusMessage": t.string().optional(),
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["ReportSummaryGroupFindingIn"] = t.struct(
        {
            "overlappingAssetCount": t.string().optional(),
            "preferenceSetFindings": t.array(
                t.proxy(renames["ReportSummaryGroupPreferenceSetFindingIn"])
            ).optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "assetAggregateStats": t.proxy(
                renames["ReportSummaryAssetAggregateStatsIn"]
            ).optional(),
        }
    ).named(renames["ReportSummaryGroupFindingIn"])
    types["ReportSummaryGroupFindingOut"] = t.struct(
        {
            "overlappingAssetCount": t.string().optional(),
            "preferenceSetFindings": t.array(
                t.proxy(renames["ReportSummaryGroupPreferenceSetFindingOut"])
            ).optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "assetAggregateStats": t.proxy(
                renames["ReportSummaryAssetAggregateStatsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryGroupFindingOut"])
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
    types["MigrationInsightIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MigrationInsightIn"]
    )
    types["MigrationInsightOut"] = t.struct(
        {
            "computeEngineTarget": t.proxy(
                renames["ComputeEngineMigrationTargetOut"]
            ).optional(),
            "gkeTarget": t.proxy(
                renames["GoogleKubernetesEngineMigrationTargetOut"]
            ).optional(),
            "fit": t.proxy(renames["FitDescriptorOut"]).optional(),
            "vmwareEngineTarget": t.proxy(
                renames["VmwareEngineMigrationTargetOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MigrationInsightOut"])
    types["GenericPlatformDetailsIn"] = t.struct(
        {"location": t.string().optional()}
    ).named(renames["GenericPlatformDetailsIn"])
    types["GenericPlatformDetailsOut"] = t.struct(
        {
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenericPlatformDetailsOut"])
    types["DiskUsageSampleIn"] = t.struct({"averageIops": t.number().optional()}).named(
        renames["DiskUsageSampleIn"]
    )
    types["DiskUsageSampleOut"] = t.struct(
        {
            "averageIops": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskUsageSampleOut"])
    types["ListReportConfigsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "reportConfigs": t.array(t.proxy(renames["ReportConfigIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListReportConfigsResponseIn"])
    types["ListReportConfigsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "reportConfigs": t.array(t.proxy(renames["ReportConfigOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReportConfigsResponseOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["FramesIn"] = t.struct(
        {"framesData": t.array(t.proxy(renames["AssetFrameIn"])).optional()}
    ).named(renames["FramesIn"])
    types["FramesOut"] = t.struct(
        {
            "framesData": t.array(t.proxy(renames["AssetFrameOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FramesOut"])
    types["RuntimeNetworkInfoIn"] = t.struct(
        {
            "netstatTime": t.proxy(renames["DateTimeIn"]).optional(),
            "netstat": t.string().optional(),
            "connections": t.proxy(renames["NetworkConnectionListIn"]).optional(),
        }
    ).named(renames["RuntimeNetworkInfoIn"])
    types["RuntimeNetworkInfoOut"] = t.struct(
        {
            "netstatTime": t.proxy(renames["DateTimeOut"]).optional(),
            "netstat": t.string().optional(),
            "connections": t.proxy(renames["NetworkConnectionListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeNetworkInfoOut"])
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
    types["ListErrorFramesResponseIn"] = t.struct(
        {
            "errorFrames": t.array(t.proxy(renames["ErrorFrameIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListErrorFramesResponseIn"])
    types["ListErrorFramesResponseOut"] = t.struct(
        {
            "errorFrames": t.array(t.proxy(renames["ErrorFrameOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListErrorFramesResponseOut"])
    types["AssetIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["AssetIn"])
    types["AssetOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "virtualMachineDetails": t.proxy(
                renames["VirtualMachineDetailsOut"]
            ).optional(),
            "performanceData": t.proxy(renames["AssetPerformanceDataOut"]).optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "sources": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "insightList": t.proxy(renames["InsightListOut"]).optional(),
            "assignedGroups": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetOut"])
    types["FileValidationReportIn"] = t.struct(
        {
            "fileErrors": t.array(t.proxy(renames["ImportErrorIn"])).optional(),
            "fileName": t.string().optional(),
            "partialReport": t.boolean().optional(),
            "rowErrors": t.array(t.proxy(renames["ImportRowErrorIn"])).optional(),
        }
    ).named(renames["FileValidationReportIn"])
    types["FileValidationReportOut"] = t.struct(
        {
            "fileErrors": t.array(t.proxy(renames["ImportErrorOut"])).optional(),
            "fileName": t.string().optional(),
            "partialReport": t.boolean().optional(),
            "rowErrors": t.array(t.proxy(renames["ImportRowErrorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileValidationReportOut"])
    types["VirtualMachinePreferencesIn"] = t.struct(
        {
            "commitmentPlan": t.string().optional(),
            "regionPreferences": t.proxy(renames["RegionPreferencesIn"]).optional(),
            "computeEnginePreferences": t.proxy(
                renames["ComputeEnginePreferencesIn"]
            ).optional(),
            "sizingOptimizationStrategy": t.string().optional(),
        }
    ).named(renames["VirtualMachinePreferencesIn"])
    types["VirtualMachinePreferencesOut"] = t.struct(
        {
            "commitmentPlan": t.string().optional(),
            "regionPreferences": t.proxy(renames["RegionPreferencesOut"]).optional(),
            "computeEnginePreferences": t.proxy(
                renames["ComputeEnginePreferencesOut"]
            ).optional(),
            "sizingOptimizationStrategy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualMachinePreferencesOut"])
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
    types["DailyResourceUsageAggregationIn"] = t.struct(
        {
            "network": t.proxy(
                renames["DailyResourceUsageAggregationNetworkIn"]
            ).optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
            "memory": t.proxy(
                renames["DailyResourceUsageAggregationMemoryIn"]
            ).optional(),
            "cpu": t.proxy(renames["DailyResourceUsageAggregationCPUIn"]).optional(),
            "disk": t.proxy(renames["DailyResourceUsageAggregationDiskIn"]).optional(),
        }
    ).named(renames["DailyResourceUsageAggregationIn"])
    types["DailyResourceUsageAggregationOut"] = t.struct(
        {
            "network": t.proxy(
                renames["DailyResourceUsageAggregationNetworkOut"]
            ).optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "memory": t.proxy(
                renames["DailyResourceUsageAggregationMemoryOut"]
            ).optional(),
            "cpu": t.proxy(renames["DailyResourceUsageAggregationCPUOut"]).optional(),
            "disk": t.proxy(renames["DailyResourceUsageAggregationDiskOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DailyResourceUsageAggregationOut"])
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
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "virtualMachinePreferences": t.proxy(
                renames["VirtualMachinePreferencesOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PreferenceSetOut"])
    types["SourceIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "priority": t.integer().optional(),
            "isManaged": t.boolean().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "state": t.string().optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "priority": t.integer().optional(),
            "name": t.string().optional(),
            "isManaged": t.boolean().optional(),
            "pendingFrameCount": t.integer().optional(),
            "errorFrameCount": t.integer().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["VirtualMachineDetailsIn"] = t.struct(
        {
            "vcenterVmId": t.string().optional(),
            "vcenterUrl": t.string().optional(),
            "coreCount": t.integer().optional(),
            "osFamily": t.string().optional(),
            "osVersion": t.string().optional(),
            "vmNetwork": t.proxy(renames["VirtualMachineNetworkDetailsIn"]).optional(),
            "vmName": t.string().optional(),
            "createTime": t.string().optional(),
            "powerState": t.string().optional(),
            "vcenterFolder": t.string().optional(),
            "platform": t.proxy(renames["PlatformDetailsIn"]).optional(),
            "vmArchitecture": t.proxy(
                renames["VirtualMachineArchitectureDetailsIn"]
            ).optional(),
            "osName": t.string().optional(),
            "memoryMb": t.integer().optional(),
            "guestOs": t.proxy(renames["GuestOsDetailsIn"]).optional(),
            "vmUuid": t.string().optional(),
            "vmDisks": t.proxy(renames["VirtualMachineDiskDetailsIn"]).optional(),
        }
    ).named(renames["VirtualMachineDetailsIn"])
    types["VirtualMachineDetailsOut"] = t.struct(
        {
            "vcenterVmId": t.string().optional(),
            "vcenterUrl": t.string().optional(),
            "coreCount": t.integer().optional(),
            "osFamily": t.string().optional(),
            "osVersion": t.string().optional(),
            "vmNetwork": t.proxy(renames["VirtualMachineNetworkDetailsOut"]).optional(),
            "vmName": t.string().optional(),
            "createTime": t.string().optional(),
            "powerState": t.string().optional(),
            "vcenterFolder": t.string().optional(),
            "platform": t.proxy(renames["PlatformDetailsOut"]).optional(),
            "vmArchitecture": t.proxy(
                renames["VirtualMachineArchitectureDetailsOut"]
            ).optional(),
            "osName": t.string().optional(),
            "memoryMb": t.integer().optional(),
            "guestOs": t.proxy(renames["GuestOsDetailsOut"]).optional(),
            "vmUuid": t.string().optional(),
            "vmDisks": t.proxy(renames["VirtualMachineDiskDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualMachineDetailsOut"])
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
    types["CpuUsageSampleIn"] = t.struct(
        {"utilizedPercentage": t.number().optional()}
    ).named(renames["CpuUsageSampleIn"])
    types["CpuUsageSampleOut"] = t.struct(
        {
            "utilizedPercentage": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CpuUsageSampleOut"])
    types["RunningProcessListIn"] = t.struct(
        {"processes": t.array(t.proxy(renames["RunningProcessIn"])).optional()}
    ).named(renames["RunningProcessListIn"])
    types["RunningProcessListOut"] = t.struct(
        {
            "processes": t.array(t.proxy(renames["RunningProcessOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunningProcessListOut"])
    types["ReportAssetFramesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReportAssetFramesResponseIn"]
    )
    types["ReportAssetFramesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReportAssetFramesResponseOut"])
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
    types["VirtualMachineArchitectureDetailsIn"] = t.struct(
        {
            "firmware": t.string().optional(),
            "cpuManufacturer": t.string().optional(),
            "bios": t.proxy(renames["BiosDetailsIn"]).optional(),
            "vendor": t.string().optional(),
            "cpuArchitecture": t.string().optional(),
            "cpuName": t.string().optional(),
            "cpuSocketCount": t.integer().optional(),
            "cpuThreadCount": t.integer().optional(),
            "hyperthreading": t.string().optional(),
        }
    ).named(renames["VirtualMachineArchitectureDetailsIn"])
    types["VirtualMachineArchitectureDetailsOut"] = t.struct(
        {
            "firmware": t.string().optional(),
            "cpuManufacturer": t.string().optional(),
            "bios": t.proxy(renames["BiosDetailsOut"]).optional(),
            "vendor": t.string().optional(),
            "cpuArchitecture": t.string().optional(),
            "cpuName": t.string().optional(),
            "cpuSocketCount": t.integer().optional(),
            "cpuThreadCount": t.integer().optional(),
            "hyperthreading": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualMachineArchitectureDetailsOut"])
    types["ListImportJobsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "importJobs": t.array(t.proxy(renames["ImportJobIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListImportJobsResponseIn"])
    types["ListImportJobsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "importJobs": t.array(t.proxy(renames["ImportJobOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListImportJobsResponseOut"])
    types["NetworkAddressIn"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "subnetMask": t.string().optional(),
            "assignment": t.string().optional(),
            "bcast": t.string().optional(),
            "fqdn": t.string().optional(),
        }
    ).named(renames["NetworkAddressIn"])
    types["NetworkAddressOut"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "subnetMask": t.string().optional(),
            "assignment": t.string().optional(),
            "bcast": t.string().optional(),
            "fqdn": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkAddressOut"])
    types["MoneyIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "units": t.string().optional(),
            "currencyCode": t.string().optional(),
        }
    ).named(renames["MoneyIn"])
    types["MoneyOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "units": t.string().optional(),
            "currencyCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoneyOut"])
    types["ReportSummaryGroupPreferenceSetFindingIn"] = t.struct(
        {
            "monthlyCostOther": t.proxy(renames["MoneyIn"]).optional(),
            "monthlyCostNetworkEgress": t.proxy(renames["MoneyIn"]).optional(),
            "monthlyCostCompute": t.proxy(renames["MoneyIn"]).optional(),
            "machineFinding": t.proxy(
                renames["ReportSummaryMachineFindingIn"]
            ).optional(),
            "monthlyCostStorage": t.proxy(renames["MoneyIn"]).optional(),
            "preferredRegion": t.string().optional(),
            "topPriority": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "monthlyCostOsLicense": t.proxy(renames["MoneyIn"]).optional(),
            "machinePreferences": t.proxy(
                renames["VirtualMachinePreferencesIn"]
            ).optional(),
            "monthlyCostTotal": t.proxy(renames["MoneyIn"]).optional(),
            "pricingTrack": t.string().optional(),
        }
    ).named(renames["ReportSummaryGroupPreferenceSetFindingIn"])
    types["ReportSummaryGroupPreferenceSetFindingOut"] = t.struct(
        {
            "monthlyCostOther": t.proxy(renames["MoneyOut"]).optional(),
            "monthlyCostNetworkEgress": t.proxy(renames["MoneyOut"]).optional(),
            "monthlyCostCompute": t.proxy(renames["MoneyOut"]).optional(),
            "machineFinding": t.proxy(
                renames["ReportSummaryMachineFindingOut"]
            ).optional(),
            "monthlyCostStorage": t.proxy(renames["MoneyOut"]).optional(),
            "preferredRegion": t.string().optional(),
            "topPriority": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "monthlyCostOsLicense": t.proxy(renames["MoneyOut"]).optional(),
            "machinePreferences": t.proxy(
                renames["VirtualMachinePreferencesOut"]
            ).optional(),
            "monthlyCostTotal": t.proxy(renames["MoneyOut"]).optional(),
            "pricingTrack": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportSummaryGroupPreferenceSetFindingOut"])
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
    types["RunningProcessIn"] = t.struct(
        {
            "exePath": t.string().optional(),
            "user": t.string().optional(),
            "pid": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "cmdline": t.string().optional(),
        }
    ).named(renames["RunningProcessIn"])
    types["RunningProcessOut"] = t.struct(
        {
            "exePath": t.string().optional(),
            "user": t.string().optional(),
            "pid": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "cmdline": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunningProcessOut"])
    types["GroupIn"] = t.struct(
        {
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
    types["ExecutionReportIn"] = t.struct(
        {
            "executionErrors": t.proxy(renames["ValidationReportIn"]).optional(),
            "jobErrors": t.array(t.proxy(renames["ImportErrorIn"])).optional(),
            "totalRowsCount": t.integer().optional(),
            "framesReported": t.integer().optional(),
        }
    ).named(renames["ExecutionReportIn"])
    types["ExecutionReportOut"] = t.struct(
        {
            "executionErrors": t.proxy(renames["ValidationReportOut"]).optional(),
            "jobErrors": t.array(t.proxy(renames["ImportErrorOut"])).optional(),
            "totalRowsCount": t.integer().optional(),
            "framesReported": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionReportOut"])

    functions = {}
    functions["projectsLocationsGet"] = migrationcenter.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string(),
                "preferenceSet": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGetSettings"] = migrationcenter.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string(),
                "preferenceSet": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = migrationcenter.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string(),
                "preferenceSet": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsUpdateSettings"] = migrationcenter.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string(),
                "preferenceSet": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsGet"] = migrationcenter.post(
        "v1alpha1/{parent}/assets:batchUpdate",
        t.struct(
            {
                "parent": t.string(),
                "requests": t.array(t.proxy(renames["UpdateAssetRequestIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsPatch"] = migrationcenter.post(
        "v1alpha1/{parent}/assets:batchUpdate",
        t.struct(
            {
                "parent": t.string(),
                "requests": t.array(t.proxy(renames["UpdateAssetRequestIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsAggregateValues"] = migrationcenter.post(
        "v1alpha1/{parent}/assets:batchUpdate",
        t.struct(
            {
                "parent": t.string(),
                "requests": t.array(t.proxy(renames["UpdateAssetRequestIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsReportAssetFrames"] = migrationcenter.post(
        "v1alpha1/{parent}/assets:batchUpdate",
        t.struct(
            {
                "parent": t.string(),
                "requests": t.array(t.proxy(renames["UpdateAssetRequestIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsBatchDelete"] = migrationcenter.post(
        "v1alpha1/{parent}/assets:batchUpdate",
        t.struct(
            {
                "parent": t.string(),
                "requests": t.array(t.proxy(renames["UpdateAssetRequestIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsList"] = migrationcenter.post(
        "v1alpha1/{parent}/assets:batchUpdate",
        t.struct(
            {
                "parent": t.string(),
                "requests": t.array(t.proxy(renames["UpdateAssetRequestIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsDelete"] = migrationcenter.post(
        "v1alpha1/{parent}/assets:batchUpdate",
        t.struct(
            {
                "parent": t.string(),
                "requests": t.array(t.proxy(renames["UpdateAssetRequestIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAssetsBatchUpdate"] = migrationcenter.post(
        "v1alpha1/{parent}/assets:batchUpdate",
        t.struct(
            {
                "parent": t.string(),
                "requests": t.array(t.proxy(renames["UpdateAssetRequestIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateAssetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = migrationcenter.get(
        "v1alpha1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = migrationcenter.get(
        "v1alpha1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesDelete"] = migrationcenter.post(
        "v1alpha1/{parent}/sources",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "sourceId": t.string(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "priority": t.integer().optional(),
                "isManaged": t.boolean().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesList"] = migrationcenter.post(
        "v1alpha1/{parent}/sources",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "sourceId": t.string(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "priority": t.integer().optional(),
                "isManaged": t.boolean().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesPatch"] = migrationcenter.post(
        "v1alpha1/{parent}/sources",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "sourceId": t.string(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "priority": t.integer().optional(),
                "isManaged": t.boolean().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesGet"] = migrationcenter.post(
        "v1alpha1/{parent}/sources",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "sourceId": t.string(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "priority": t.integer().optional(),
                "isManaged": t.boolean().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesCreate"] = migrationcenter.post(
        "v1alpha1/{parent}/sources",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "sourceId": t.string(),
                "displayName": t.string().optional(),
                "description": t.string().optional(),
                "priority": t.integer().optional(),
                "isManaged": t.boolean().optional(),
                "type": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListErrorFramesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReportConfigsCreate"] = migrationcenter.get(
        "v1alpha1/{parent}/reportConfigs",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "parent": t.string(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListReportConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReportConfigsDelete"] = migrationcenter.get(
        "v1alpha1/{parent}/reportConfigs",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "parent": t.string(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListReportConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReportConfigsReportsDelete"] = migrationcenter.get(
        "v1alpha1/{parent}/reports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "view": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "view": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "view": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "view": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPreferenceSetsGet"] = migrationcenter.get(
        "v1alpha1/{parent}/preferenceSets",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPreferenceSetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPreferenceSetsPatch"] = migrationcenter.get(
        "v1alpha1/{parent}/preferenceSets",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPreferenceSetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPreferenceSetsDelete"] = migrationcenter.get(
        "v1alpha1/{parent}/preferenceSets",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPreferenceSetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPreferenceSetsCreate"] = migrationcenter.get(
        "v1alpha1/{parent}/preferenceSets",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPreferenceSetsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPreferenceSetsList"] = migrationcenter.get(
        "v1alpha1/{parent}/preferenceSets",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPreferenceSetsResponseOut"]),
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
    functions["projectsLocationsImportJobsImportDataFilesDelete"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ImportDataFileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImportJobsImportDataFilesList"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ImportDataFileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImportJobsImportDataFilesCreate"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ImportDataFileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImportJobsImportDataFilesGet"] = migrationcenter.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ImportDataFileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsRemoveAssets"] = migrationcenter.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
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
                "name": t.string().optional(),
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
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
                "name": t.string().optional(),
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
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
                "name": t.string().optional(),
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsDelete"] = migrationcenter.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
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
                "name": t.string().optional(),
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
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
                "name": t.string().optional(),
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="migrationcenter", renames=renames, types=types, functions=functions
    )
