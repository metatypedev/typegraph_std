from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_dataflow() -> Import:
    dataflow = HTTPRuntime("https://dataflow.googleapis.com/")

    renames = {
        "ErrorResponse": "_dataflow_1_ErrorResponse",
        "JobExecutionInfoIn": "_dataflow_2_JobExecutionInfoIn",
        "JobExecutionInfoOut": "_dataflow_3_JobExecutionInfoOut",
        "ListSnapshotsResponseIn": "_dataflow_4_ListSnapshotsResponseIn",
        "ListSnapshotsResponseOut": "_dataflow_5_ListSnapshotsResponseOut",
        "FloatingPointMeanIn": "_dataflow_6_FloatingPointMeanIn",
        "FloatingPointMeanOut": "_dataflow_7_FloatingPointMeanOut",
        "DatastoreIODetailsIn": "_dataflow_8_DatastoreIODetailsIn",
        "DatastoreIODetailsOut": "_dataflow_9_DatastoreIODetailsOut",
        "SendWorkerMessagesRequestIn": "_dataflow_10_SendWorkerMessagesRequestIn",
        "SendWorkerMessagesRequestOut": "_dataflow_11_SendWorkerMessagesRequestOut",
        "LaunchFlexTemplateRequestIn": "_dataflow_12_LaunchFlexTemplateRequestIn",
        "LaunchFlexTemplateRequestOut": "_dataflow_13_LaunchFlexTemplateRequestOut",
        "SnapshotIn": "_dataflow_14_SnapshotIn",
        "SnapshotOut": "_dataflow_15_SnapshotOut",
        "DerivedSourceIn": "_dataflow_16_DerivedSourceIn",
        "DerivedSourceOut": "_dataflow_17_DerivedSourceOut",
        "StreamingStragglerInfoIn": "_dataflow_18_StreamingStragglerInfoIn",
        "StreamingStragglerInfoOut": "_dataflow_19_StreamingStragglerInfoOut",
        "SourceSplitRequestIn": "_dataflow_20_SourceSplitRequestIn",
        "SourceSplitRequestOut": "_dataflow_21_SourceSplitRequestOut",
        "WorkerHealthReportIn": "_dataflow_22_WorkerHealthReportIn",
        "WorkerHealthReportOut": "_dataflow_23_WorkerHealthReportOut",
        "FailedLocationIn": "_dataflow_24_FailedLocationIn",
        "FailedLocationOut": "_dataflow_25_FailedLocationOut",
        "SideInputInfoIn": "_dataflow_26_SideInputInfoIn",
        "SideInputInfoOut": "_dataflow_27_SideInputInfoOut",
        "ListJobMessagesResponseIn": "_dataflow_28_ListJobMessagesResponseIn",
        "ListJobMessagesResponseOut": "_dataflow_29_ListJobMessagesResponseOut",
        "ReportedParallelismIn": "_dataflow_30_ReportedParallelismIn",
        "ReportedParallelismOut": "_dataflow_31_ReportedParallelismOut",
        "NameAndKindIn": "_dataflow_32_NameAndKindIn",
        "NameAndKindOut": "_dataflow_33_NameAndKindOut",
        "JobMetricsIn": "_dataflow_34_JobMetricsIn",
        "JobMetricsOut": "_dataflow_35_JobMetricsOut",
        "StreamLocationIn": "_dataflow_36_StreamLocationIn",
        "StreamLocationOut": "_dataflow_37_StreamLocationOut",
        "CounterMetadataIn": "_dataflow_38_CounterMetadataIn",
        "CounterMetadataOut": "_dataflow_39_CounterMetadataOut",
        "ApproximateProgressIn": "_dataflow_40_ApproximateProgressIn",
        "ApproximateProgressOut": "_dataflow_41_ApproximateProgressOut",
        "ResourceUtilizationReportResponseIn": "_dataflow_42_ResourceUtilizationReportResponseIn",
        "ResourceUtilizationReportResponseOut": "_dataflow_43_ResourceUtilizationReportResponseOut",
        "MountedDataDiskIn": "_dataflow_44_MountedDataDiskIn",
        "MountedDataDiskOut": "_dataflow_45_MountedDataDiskOut",
        "IntegerListIn": "_dataflow_46_IntegerListIn",
        "IntegerListOut": "_dataflow_47_IntegerListOut",
        "ParallelInstructionIn": "_dataflow_48_ParallelInstructionIn",
        "ParallelInstructionOut": "_dataflow_49_ParallelInstructionOut",
        "MetricUpdateIn": "_dataflow_50_MetricUpdateIn",
        "MetricUpdateOut": "_dataflow_51_MetricUpdateOut",
        "LaunchTemplateResponseIn": "_dataflow_52_LaunchTemplateResponseIn",
        "LaunchTemplateResponseOut": "_dataflow_53_LaunchTemplateResponseOut",
        "StragglerInfoIn": "_dataflow_54_StragglerInfoIn",
        "StragglerInfoOut": "_dataflow_55_StragglerInfoOut",
        "SplitInt64In": "_dataflow_56_SplitInt64In",
        "SplitInt64Out": "_dataflow_57_SplitInt64Out",
        "LeaseWorkItemRequestIn": "_dataflow_58_LeaseWorkItemRequestIn",
        "LeaseWorkItemRequestOut": "_dataflow_59_LeaseWorkItemRequestOut",
        "StringListIn": "_dataflow_60_StringListIn",
        "StringListOut": "_dataflow_61_StringListOut",
        "ApproximateSplitRequestIn": "_dataflow_62_ApproximateSplitRequestIn",
        "ApproximateSplitRequestOut": "_dataflow_63_ApproximateSplitRequestOut",
        "CPUTimeIn": "_dataflow_64_CPUTimeIn",
        "CPUTimeOut": "_dataflow_65_CPUTimeOut",
        "FloatingPointListIn": "_dataflow_66_FloatingPointListIn",
        "FloatingPointListOut": "_dataflow_67_FloatingPointListOut",
        "WorkerMessageResponseIn": "_dataflow_68_WorkerMessageResponseIn",
        "WorkerMessageResponseOut": "_dataflow_69_WorkerMessageResponseOut",
        "MultiOutputInfoIn": "_dataflow_70_MultiOutputInfoIn",
        "MultiOutputInfoOut": "_dataflow_71_MultiOutputInfoOut",
        "ComponentTransformIn": "_dataflow_72_ComponentTransformIn",
        "ComponentTransformOut": "_dataflow_73_ComponentTransformOut",
        "ParameterIn": "_dataflow_74_ParameterIn",
        "ParameterOut": "_dataflow_75_ParameterOut",
        "GetDebugConfigResponseIn": "_dataflow_76_GetDebugConfigResponseIn",
        "GetDebugConfigResponseOut": "_dataflow_77_GetDebugConfigResponseOut",
        "WorkerThreadScalingReportIn": "_dataflow_78_WorkerThreadScalingReportIn",
        "WorkerThreadScalingReportOut": "_dataflow_79_WorkerThreadScalingReportOut",
        "ComputationTopologyIn": "_dataflow_80_ComputationTopologyIn",
        "ComputationTopologyOut": "_dataflow_81_ComputationTopologyOut",
        "ExecutionStageSummaryIn": "_dataflow_82_ExecutionStageSummaryIn",
        "ExecutionStageSummaryOut": "_dataflow_83_ExecutionStageSummaryOut",
        "SourceSplitOptionsIn": "_dataflow_84_SourceSplitOptionsIn",
        "SourceSplitOptionsOut": "_dataflow_85_SourceSplitOptionsOut",
        "DeleteSnapshotResponseIn": "_dataflow_86_DeleteSnapshotResponseIn",
        "DeleteSnapshotResponseOut": "_dataflow_87_DeleteSnapshotResponseOut",
        "SnapshotJobRequestIn": "_dataflow_88_SnapshotJobRequestIn",
        "SnapshotJobRequestOut": "_dataflow_89_SnapshotJobRequestOut",
        "WorkerShutdownNoticeIn": "_dataflow_90_WorkerShutdownNoticeIn",
        "WorkerShutdownNoticeOut": "_dataflow_91_WorkerShutdownNoticeOut",
        "DataDiskAssignmentIn": "_dataflow_92_DataDiskAssignmentIn",
        "DataDiskAssignmentOut": "_dataflow_93_DataDiskAssignmentOut",
        "GetTemplateResponseIn": "_dataflow_94_GetTemplateResponseIn",
        "GetTemplateResponseOut": "_dataflow_95_GetTemplateResponseOut",
        "EnvironmentIn": "_dataflow_96_EnvironmentIn",
        "EnvironmentOut": "_dataflow_97_EnvironmentOut",
        "WorkerMessageCodeIn": "_dataflow_98_WorkerMessageCodeIn",
        "WorkerMessageCodeOut": "_dataflow_99_WorkerMessageCodeOut",
        "ReportWorkItemStatusRequestIn": "_dataflow_100_ReportWorkItemStatusRequestIn",
        "ReportWorkItemStatusRequestOut": "_dataflow_101_ReportWorkItemStatusRequestOut",
        "ParameterMetadataIn": "_dataflow_102_ParameterMetadataIn",
        "ParameterMetadataOut": "_dataflow_103_ParameterMetadataOut",
        "StepIn": "_dataflow_104_StepIn",
        "StepOut": "_dataflow_105_StepOut",
        "SourceOperationRequestIn": "_dataflow_106_SourceOperationRequestIn",
        "SourceOperationRequestOut": "_dataflow_107_SourceOperationRequestOut",
        "LaunchFlexTemplateResponseIn": "_dataflow_108_LaunchFlexTemplateResponseIn",
        "LaunchFlexTemplateResponseOut": "_dataflow_109_LaunchFlexTemplateResponseOut",
        "WorkerShutdownNoticeResponseIn": "_dataflow_110_WorkerShutdownNoticeResponseIn",
        "WorkerShutdownNoticeResponseOut": "_dataflow_111_WorkerShutdownNoticeResponseOut",
        "CreateJobFromTemplateRequestIn": "_dataflow_112_CreateJobFromTemplateRequestIn",
        "CreateJobFromTemplateRequestOut": "_dataflow_113_CreateJobFromTemplateRequestOut",
        "PipelineDescriptionIn": "_dataflow_114_PipelineDescriptionIn",
        "PipelineDescriptionOut": "_dataflow_115_PipelineDescriptionOut",
        "ContainerSpecIn": "_dataflow_116_ContainerSpecIn",
        "ContainerSpecOut": "_dataflow_117_ContainerSpecOut",
        "TopologyConfigIn": "_dataflow_118_TopologyConfigIn",
        "TopologyConfigOut": "_dataflow_119_TopologyConfigOut",
        "SdkVersionIn": "_dataflow_120_SdkVersionIn",
        "SdkVersionOut": "_dataflow_121_SdkVersionOut",
        "ReadInstructionIn": "_dataflow_122_ReadInstructionIn",
        "ReadInstructionOut": "_dataflow_123_ReadInstructionOut",
        "MapTaskIn": "_dataflow_124_MapTaskIn",
        "MapTaskOut": "_dataflow_125_MapTaskOut",
        "SpannerIODetailsIn": "_dataflow_126_SpannerIODetailsIn",
        "SpannerIODetailsOut": "_dataflow_127_SpannerIODetailsOut",
        "SourceSplitResponseIn": "_dataflow_128_SourceSplitResponseIn",
        "SourceSplitResponseOut": "_dataflow_129_SourceSplitResponseOut",
        "KeyRangeLocationIn": "_dataflow_130_KeyRangeLocationIn",
        "KeyRangeLocationOut": "_dataflow_131_KeyRangeLocationOut",
        "TransformSummaryIn": "_dataflow_132_TransformSummaryIn",
        "TransformSummaryOut": "_dataflow_133_TransformSummaryOut",
        "SendDebugCaptureResponseIn": "_dataflow_134_SendDebugCaptureResponseIn",
        "SendDebugCaptureResponseOut": "_dataflow_135_SendDebugCaptureResponseOut",
        "BigQueryIODetailsIn": "_dataflow_136_BigQueryIODetailsIn",
        "BigQueryIODetailsOut": "_dataflow_137_BigQueryIODetailsOut",
        "ResourceUtilizationReportIn": "_dataflow_138_ResourceUtilizationReportIn",
        "ResourceUtilizationReportOut": "_dataflow_139_ResourceUtilizationReportOut",
        "CounterStructuredNameIn": "_dataflow_140_CounterStructuredNameIn",
        "CounterStructuredNameOut": "_dataflow_141_CounterStructuredNameOut",
        "ApproximateReportedProgressIn": "_dataflow_142_ApproximateReportedProgressIn",
        "ApproximateReportedProgressOut": "_dataflow_143_ApproximateReportedProgressOut",
        "PubsubSnapshotMetadataIn": "_dataflow_144_PubsubSnapshotMetadataIn",
        "PubsubSnapshotMetadataOut": "_dataflow_145_PubsubSnapshotMetadataOut",
        "MetricShortIdIn": "_dataflow_146_MetricShortIdIn",
        "MetricShortIdOut": "_dataflow_147_MetricShortIdOut",
        "WriteInstructionIn": "_dataflow_148_WriteInstructionIn",
        "WriteInstructionOut": "_dataflow_149_WriteInstructionOut",
        "ConcatPositionIn": "_dataflow_150_ConcatPositionIn",
        "ConcatPositionOut": "_dataflow_151_ConcatPositionOut",
        "ListJobsResponseIn": "_dataflow_152_ListJobsResponseIn",
        "ListJobsResponseOut": "_dataflow_153_ListJobsResponseOut",
        "HotKeyDetectionIn": "_dataflow_154_HotKeyDetectionIn",
        "HotKeyDetectionOut": "_dataflow_155_HotKeyDetectionOut",
        "DiskIn": "_dataflow_156_DiskIn",
        "DiskOut": "_dataflow_157_DiskOut",
        "SourceSplitShardIn": "_dataflow_158_SourceSplitShardIn",
        "SourceSplitShardOut": "_dataflow_159_SourceSplitShardOut",
        "StructuredMessageIn": "_dataflow_160_StructuredMessageIn",
        "StructuredMessageOut": "_dataflow_161_StructuredMessageOut",
        "FlattenInstructionIn": "_dataflow_162_FlattenInstructionIn",
        "FlattenInstructionOut": "_dataflow_163_FlattenInstructionOut",
        "FlexTemplateRuntimeEnvironmentIn": "_dataflow_164_FlexTemplateRuntimeEnvironmentIn",
        "FlexTemplateRuntimeEnvironmentOut": "_dataflow_165_FlexTemplateRuntimeEnvironmentOut",
        "TaskRunnerSettingsIn": "_dataflow_166_TaskRunnerSettingsIn",
        "TaskRunnerSettingsOut": "_dataflow_167_TaskRunnerSettingsOut",
        "PubsubLocationIn": "_dataflow_168_PubsubLocationIn",
        "PubsubLocationOut": "_dataflow_169_PubsubLocationOut",
        "SinkIn": "_dataflow_170_SinkIn",
        "SinkOut": "_dataflow_171_SinkOut",
        "StragglerDebuggingInfoIn": "_dataflow_172_StragglerDebuggingInfoIn",
        "StragglerDebuggingInfoOut": "_dataflow_173_StragglerDebuggingInfoOut",
        "SeqMapTaskOutputInfoIn": "_dataflow_174_SeqMapTaskOutputInfoIn",
        "SeqMapTaskOutputInfoOut": "_dataflow_175_SeqMapTaskOutputInfoOut",
        "SourceOperationResponseIn": "_dataflow_176_SourceOperationResponseIn",
        "SourceOperationResponseOut": "_dataflow_177_SourceOperationResponseOut",
        "WorkerMessageIn": "_dataflow_178_WorkerMessageIn",
        "WorkerMessageOut": "_dataflow_179_WorkerMessageOut",
        "StageSummaryIn": "_dataflow_180_StageSummaryIn",
        "StageSummaryOut": "_dataflow_181_StageSummaryOut",
        "DistributionUpdateIn": "_dataflow_182_DistributionUpdateIn",
        "DistributionUpdateOut": "_dataflow_183_DistributionUpdateOut",
        "PositionIn": "_dataflow_184_PositionIn",
        "PositionOut": "_dataflow_185_PositionOut",
        "JobIn": "_dataflow_186_JobIn",
        "JobOut": "_dataflow_187_JobOut",
        "LaunchTemplateParametersIn": "_dataflow_188_LaunchTemplateParametersIn",
        "LaunchTemplateParametersOut": "_dataflow_189_LaunchTemplateParametersOut",
        "JobExecutionDetailsIn": "_dataflow_190_JobExecutionDetailsIn",
        "JobExecutionDetailsOut": "_dataflow_191_JobExecutionDetailsOut",
        "ShellTaskIn": "_dataflow_192_ShellTaskIn",
        "ShellTaskOut": "_dataflow_193_ShellTaskOut",
        "AutoscalingSettingsIn": "_dataflow_194_AutoscalingSettingsIn",
        "AutoscalingSettingsOut": "_dataflow_195_AutoscalingSettingsOut",
        "BigTableIODetailsIn": "_dataflow_196_BigTableIODetailsIn",
        "BigTableIODetailsOut": "_dataflow_197_BigTableIODetailsOut",
        "StateFamilyConfigIn": "_dataflow_198_StateFamilyConfigIn",
        "StateFamilyConfigOut": "_dataflow_199_StateFamilyConfigOut",
        "WorkerLifecycleEventIn": "_dataflow_200_WorkerLifecycleEventIn",
        "WorkerLifecycleEventOut": "_dataflow_201_WorkerLifecycleEventOut",
        "CustomSourceLocationIn": "_dataflow_202_CustomSourceLocationIn",
        "CustomSourceLocationOut": "_dataflow_203_CustomSourceLocationOut",
        "SourceIn": "_dataflow_204_SourceIn",
        "SourceOut": "_dataflow_205_SourceOut",
        "WorkItemStatusIn": "_dataflow_206_WorkItemStatusIn",
        "WorkItemStatusOut": "_dataflow_207_WorkItemStatusOut",
        "PackageIn": "_dataflow_208_PackageIn",
        "PackageOut": "_dataflow_209_PackageOut",
        "ExecutionStageStateIn": "_dataflow_210_ExecutionStageStateIn",
        "ExecutionStageStateOut": "_dataflow_211_ExecutionStageStateOut",
        "StreamingConfigTaskIn": "_dataflow_212_StreamingConfigTaskIn",
        "StreamingConfigTaskOut": "_dataflow_213_StreamingConfigTaskOut",
        "InstructionInputIn": "_dataflow_214_InstructionInputIn",
        "InstructionInputOut": "_dataflow_215_InstructionInputOut",
        "StatusIn": "_dataflow_216_StatusIn",
        "StatusOut": "_dataflow_217_StatusOut",
        "WorkItemDetailsIn": "_dataflow_218_WorkItemDetailsIn",
        "WorkItemDetailsOut": "_dataflow_219_WorkItemDetailsOut",
        "PartialGroupByKeyInstructionIn": "_dataflow_220_PartialGroupByKeyInstructionIn",
        "PartialGroupByKeyInstructionOut": "_dataflow_221_PartialGroupByKeyInstructionOut",
        "WorkItemIn": "_dataflow_222_WorkItemIn",
        "WorkItemOut": "_dataflow_223_WorkItemOut",
        "LaunchFlexTemplateParameterIn": "_dataflow_224_LaunchFlexTemplateParameterIn",
        "LaunchFlexTemplateParameterOut": "_dataflow_225_LaunchFlexTemplateParameterOut",
        "StreamingSetupTaskIn": "_dataflow_226_StreamingSetupTaskIn",
        "StreamingSetupTaskOut": "_dataflow_227_StreamingSetupTaskOut",
        "StageExecutionDetailsIn": "_dataflow_228_StageExecutionDetailsIn",
        "StageExecutionDetailsOut": "_dataflow_229_StageExecutionDetailsOut",
        "MemInfoIn": "_dataflow_230_MemInfoIn",
        "MemInfoOut": "_dataflow_231_MemInfoOut",
        "StreamingStageLocationIn": "_dataflow_232_StreamingStageLocationIn",
        "StreamingStageLocationOut": "_dataflow_233_StreamingStageLocationOut",
        "JobMessageIn": "_dataflow_234_JobMessageIn",
        "JobMessageOut": "_dataflow_235_JobMessageOut",
        "ReportWorkItemStatusResponseIn": "_dataflow_236_ReportWorkItemStatusResponseIn",
        "ReportWorkItemStatusResponseOut": "_dataflow_237_ReportWorkItemStatusResponseOut",
        "TemplateMetadataIn": "_dataflow_238_TemplateMetadataIn",
        "TemplateMetadataOut": "_dataflow_239_TemplateMetadataOut",
        "JobExecutionStageInfoIn": "_dataflow_240_JobExecutionStageInfoIn",
        "JobExecutionStageInfoOut": "_dataflow_241_JobExecutionStageInfoOut",
        "CounterStructuredNameAndMetadataIn": "_dataflow_242_CounterStructuredNameAndMetadataIn",
        "CounterStructuredNameAndMetadataOut": "_dataflow_243_CounterStructuredNameAndMetadataOut",
        "MetricStructuredNameIn": "_dataflow_244_MetricStructuredNameIn",
        "MetricStructuredNameOut": "_dataflow_245_MetricStructuredNameOut",
        "SendWorkerMessagesResponseIn": "_dataflow_246_SendWorkerMessagesResponseIn",
        "SendWorkerMessagesResponseOut": "_dataflow_247_SendWorkerMessagesResponseOut",
        "IntegerGaugeIn": "_dataflow_248_IntegerGaugeIn",
        "IntegerGaugeOut": "_dataflow_249_IntegerGaugeOut",
        "HistogramIn": "_dataflow_250_HistogramIn",
        "HistogramOut": "_dataflow_251_HistogramOut",
        "SdkHarnessContainerImageIn": "_dataflow_252_SdkHarnessContainerImageIn",
        "SdkHarnessContainerImageOut": "_dataflow_253_SdkHarnessContainerImageOut",
        "RuntimeUpdatableParamsIn": "_dataflow_254_RuntimeUpdatableParamsIn",
        "RuntimeUpdatableParamsOut": "_dataflow_255_RuntimeUpdatableParamsOut",
        "SendDebugCaptureRequestIn": "_dataflow_256_SendDebugCaptureRequestIn",
        "SendDebugCaptureRequestOut": "_dataflow_257_SendDebugCaptureRequestOut",
        "HotKeyInfoIn": "_dataflow_258_HotKeyInfoIn",
        "HotKeyInfoOut": "_dataflow_259_HotKeyInfoOut",
        "AutoscalingEventIn": "_dataflow_260_AutoscalingEventIn",
        "AutoscalingEventOut": "_dataflow_261_AutoscalingEventOut",
        "IntegerMeanIn": "_dataflow_262_IntegerMeanIn",
        "IntegerMeanOut": "_dataflow_263_IntegerMeanOut",
        "StageSourceIn": "_dataflow_264_StageSourceIn",
        "StageSourceOut": "_dataflow_265_StageSourceOut",
        "StreamingApplianceSnapshotConfigIn": "_dataflow_266_StreamingApplianceSnapshotConfigIn",
        "StreamingApplianceSnapshotConfigOut": "_dataflow_267_StreamingApplianceSnapshotConfigOut",
        "DisplayDataIn": "_dataflow_268_DisplayDataIn",
        "DisplayDataOut": "_dataflow_269_DisplayDataOut",
        "StreamingSideInputLocationIn": "_dataflow_270_StreamingSideInputLocationIn",
        "StreamingSideInputLocationOut": "_dataflow_271_StreamingSideInputLocationOut",
        "StragglerIn": "_dataflow_272_StragglerIn",
        "StragglerOut": "_dataflow_273_StragglerOut",
        "DynamicSourceSplitIn": "_dataflow_274_DynamicSourceSplitIn",
        "DynamicSourceSplitOut": "_dataflow_275_DynamicSourceSplitOut",
        "StreamingComputationTaskIn": "_dataflow_276_StreamingComputationTaskIn",
        "StreamingComputationTaskOut": "_dataflow_277_StreamingComputationTaskOut",
        "WorkerHealthReportResponseIn": "_dataflow_278_WorkerHealthReportResponseIn",
        "WorkerHealthReportResponseOut": "_dataflow_279_WorkerHealthReportResponseOut",
        "SourceGetMetadataRequestIn": "_dataflow_280_SourceGetMetadataRequestIn",
        "SourceGetMetadataRequestOut": "_dataflow_281_SourceGetMetadataRequestOut",
        "InstructionOutputIn": "_dataflow_282_InstructionOutputIn",
        "InstructionOutputOut": "_dataflow_283_InstructionOutputOut",
        "PointIn": "_dataflow_284_PointIn",
        "PointOut": "_dataflow_285_PointOut",
        "StreamingComputationRangesIn": "_dataflow_286_StreamingComputationRangesIn",
        "StreamingComputationRangesOut": "_dataflow_287_StreamingComputationRangesOut",
        "LeaseWorkItemResponseIn": "_dataflow_288_LeaseWorkItemResponseIn",
        "LeaseWorkItemResponseOut": "_dataflow_289_LeaseWorkItemResponseOut",
        "SourceForkIn": "_dataflow_290_SourceForkIn",
        "SourceForkOut": "_dataflow_291_SourceForkOut",
        "SDKInfoIn": "_dataflow_292_SDKInfoIn",
        "SDKInfoOut": "_dataflow_293_SDKInfoOut",
        "GetDebugConfigRequestIn": "_dataflow_294_GetDebugConfigRequestIn",
        "GetDebugConfigRequestOut": "_dataflow_295_GetDebugConfigRequestOut",
        "FileIODetailsIn": "_dataflow_296_FileIODetailsIn",
        "FileIODetailsOut": "_dataflow_297_FileIODetailsOut",
        "WorkerPoolIn": "_dataflow_298_WorkerPoolIn",
        "WorkerPoolOut": "_dataflow_299_WorkerPoolOut",
        "SourceMetadataIn": "_dataflow_300_SourceMetadataIn",
        "SourceMetadataOut": "_dataflow_301_SourceMetadataOut",
        "RuntimeEnvironmentIn": "_dataflow_302_RuntimeEnvironmentIn",
        "RuntimeEnvironmentOut": "_dataflow_303_RuntimeEnvironmentOut",
        "CounterUpdateIn": "_dataflow_304_CounterUpdateIn",
        "CounterUpdateOut": "_dataflow_305_CounterUpdateOut",
        "WorkerDetailsIn": "_dataflow_306_WorkerDetailsIn",
        "WorkerDetailsOut": "_dataflow_307_WorkerDetailsOut",
        "SeqMapTaskIn": "_dataflow_308_SeqMapTaskIn",
        "SeqMapTaskOut": "_dataflow_309_SeqMapTaskOut",
        "WorkItemServiceStateIn": "_dataflow_310_WorkItemServiceStateIn",
        "WorkItemServiceStateOut": "_dataflow_311_WorkItemServiceStateOut",
        "ComponentSourceIn": "_dataflow_312_ComponentSourceIn",
        "ComponentSourceOut": "_dataflow_313_ComponentSourceOut",
        "WorkerSettingsIn": "_dataflow_314_WorkerSettingsIn",
        "WorkerSettingsOut": "_dataflow_315_WorkerSettingsOut",
        "KeyRangeDataDiskAssignmentIn": "_dataflow_316_KeyRangeDataDiskAssignmentIn",
        "KeyRangeDataDiskAssignmentOut": "_dataflow_317_KeyRangeDataDiskAssignmentOut",
        "StragglerSummaryIn": "_dataflow_318_StragglerSummaryIn",
        "StragglerSummaryOut": "_dataflow_319_StragglerSummaryOut",
        "HotKeyDebuggingInfoIn": "_dataflow_320_HotKeyDebuggingInfoIn",
        "HotKeyDebuggingInfoOut": "_dataflow_321_HotKeyDebuggingInfoOut",
        "ProgressTimeseriesIn": "_dataflow_322_ProgressTimeseriesIn",
        "ProgressTimeseriesOut": "_dataflow_323_ProgressTimeseriesOut",
        "StreamingComputationConfigIn": "_dataflow_324_StreamingComputationConfigIn",
        "StreamingComputationConfigOut": "_dataflow_325_StreamingComputationConfigOut",
        "DebugOptionsIn": "_dataflow_326_DebugOptionsIn",
        "DebugOptionsOut": "_dataflow_327_DebugOptionsOut",
        "RuntimeMetadataIn": "_dataflow_328_RuntimeMetadataIn",
        "RuntimeMetadataOut": "_dataflow_329_RuntimeMetadataOut",
        "JobMetadataIn": "_dataflow_330_JobMetadataIn",
        "JobMetadataOut": "_dataflow_331_JobMetadataOut",
        "SourceGetMetadataResponseIn": "_dataflow_332_SourceGetMetadataResponseIn",
        "SourceGetMetadataResponseOut": "_dataflow_333_SourceGetMetadataResponseOut",
        "WorkerThreadScalingReportResponseIn": "_dataflow_334_WorkerThreadScalingReportResponseIn",
        "WorkerThreadScalingReportResponseOut": "_dataflow_335_WorkerThreadScalingReportResponseOut",
        "PubSubIODetailsIn": "_dataflow_336_PubSubIODetailsIn",
        "PubSubIODetailsOut": "_dataflow_337_PubSubIODetailsOut",
        "ParDoInstructionIn": "_dataflow_338_ParDoInstructionIn",
        "ParDoInstructionOut": "_dataflow_339_ParDoInstructionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["JobExecutionInfoIn"] = t.struct(
        {"stages": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["JobExecutionInfoIn"])
    types["JobExecutionInfoOut"] = t.struct(
        {
            "stages": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobExecutionInfoOut"])
    types["ListSnapshotsResponseIn"] = t.struct(
        {"snapshots": t.array(t.proxy(renames["SnapshotIn"])).optional()}
    ).named(renames["ListSnapshotsResponseIn"])
    types["ListSnapshotsResponseOut"] = t.struct(
        {
            "snapshots": t.array(t.proxy(renames["SnapshotOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSnapshotsResponseOut"])
    types["FloatingPointMeanIn"] = t.struct(
        {
            "count": t.proxy(renames["SplitInt64In"]).optional(),
            "sum": t.number().optional(),
        }
    ).named(renames["FloatingPointMeanIn"])
    types["FloatingPointMeanOut"] = t.struct(
        {
            "count": t.proxy(renames["SplitInt64Out"]).optional(),
            "sum": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloatingPointMeanOut"])
    types["DatastoreIODetailsIn"] = t.struct(
        {"namespace": t.string().optional(), "projectId": t.string().optional()}
    ).named(renames["DatastoreIODetailsIn"])
    types["DatastoreIODetailsOut"] = t.struct(
        {
            "namespace": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatastoreIODetailsOut"])
    types["SendWorkerMessagesRequestIn"] = t.struct(
        {
            "workerMessages": t.array(t.proxy(renames["WorkerMessageIn"])).optional(),
            "location": t.string().optional(),
        }
    ).named(renames["SendWorkerMessagesRequestIn"])
    types["SendWorkerMessagesRequestOut"] = t.struct(
        {
            "workerMessages": t.array(t.proxy(renames["WorkerMessageOut"])).optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SendWorkerMessagesRequestOut"])
    types["LaunchFlexTemplateRequestIn"] = t.struct(
        {
            "launchParameter": t.proxy(renames["LaunchFlexTemplateParameterIn"]),
            "validateOnly": t.boolean().optional(),
        }
    ).named(renames["LaunchFlexTemplateRequestIn"])
    types["LaunchFlexTemplateRequestOut"] = t.struct(
        {
            "launchParameter": t.proxy(renames["LaunchFlexTemplateParameterOut"]),
            "validateOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LaunchFlexTemplateRequestOut"])
    types["SnapshotIn"] = t.struct(
        {
            "sourceJobId": t.string().optional(),
            "region": t.string().optional(),
            "creationTime": t.string().optional(),
            "state": t.string().optional(),
            "description": t.string().optional(),
            "diskSizeBytes": t.string().optional(),
            "projectId": t.string().optional(),
            "ttl": t.string().optional(),
            "pubsubMetadata": t.array(
                t.proxy(renames["PubsubSnapshotMetadataIn"])
            ).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["SnapshotIn"])
    types["SnapshotOut"] = t.struct(
        {
            "sourceJobId": t.string().optional(),
            "region": t.string().optional(),
            "creationTime": t.string().optional(),
            "state": t.string().optional(),
            "description": t.string().optional(),
            "diskSizeBytes": t.string().optional(),
            "projectId": t.string().optional(),
            "ttl": t.string().optional(),
            "pubsubMetadata": t.array(
                t.proxy(renames["PubsubSnapshotMetadataOut"])
            ).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnapshotOut"])
    types["DerivedSourceIn"] = t.struct(
        {
            "source": t.proxy(renames["SourceIn"]).optional(),
            "derivationMode": t.string().optional(),
        }
    ).named(renames["DerivedSourceIn"])
    types["DerivedSourceOut"] = t.struct(
        {
            "source": t.proxy(renames["SourceOut"]).optional(),
            "derivationMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DerivedSourceOut"])
    types["StreamingStragglerInfoIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "dataWatermarkLag": t.string().optional(),
            "endTime": t.string().optional(),
            "workerName": t.string().optional(),
            "systemWatermarkLag": t.string().optional(),
        }
    ).named(renames["StreamingStragglerInfoIn"])
    types["StreamingStragglerInfoOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "dataWatermarkLag": t.string().optional(),
            "endTime": t.string().optional(),
            "workerName": t.string().optional(),
            "systemWatermarkLag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingStragglerInfoOut"])
    types["SourceSplitRequestIn"] = t.struct(
        {
            "options": t.proxy(renames["SourceSplitOptionsIn"]).optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
        }
    ).named(renames["SourceSplitRequestIn"])
    types["SourceSplitRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["SourceSplitOptionsOut"]).optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceSplitRequestOut"])
    types["WorkerHealthReportIn"] = t.struct(
        {
            "vmIsHealthy": t.boolean().optional(),
            "pods": t.array(t.struct({"_": t.string().optional()})).optional(),
            "vmStartupTime": t.string().optional(),
            "vmIsBroken": t.boolean().optional(),
            "vmBrokenCode": t.string().optional(),
            "msg": t.string().optional(),
            "reportInterval": t.string().optional(),
        }
    ).named(renames["WorkerHealthReportIn"])
    types["WorkerHealthReportOut"] = t.struct(
        {
            "vmIsHealthy": t.boolean().optional(),
            "pods": t.array(t.struct({"_": t.string().optional()})).optional(),
            "vmStartupTime": t.string().optional(),
            "vmIsBroken": t.boolean().optional(),
            "vmBrokenCode": t.string().optional(),
            "msg": t.string().optional(),
            "reportInterval": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerHealthReportOut"])
    types["FailedLocationIn"] = t.struct({"name": t.string().optional()}).named(
        renames["FailedLocationIn"]
    )
    types["FailedLocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FailedLocationOut"])
    types["SideInputInfoIn"] = t.struct(
        {
            "kind": t.struct({"_": t.string().optional()}).optional(),
            "tag": t.string().optional(),
            "sources": t.array(t.proxy(renames["SourceIn"])).optional(),
        }
    ).named(renames["SideInputInfoIn"])
    types["SideInputInfoOut"] = t.struct(
        {
            "kind": t.struct({"_": t.string().optional()}).optional(),
            "tag": t.string().optional(),
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SideInputInfoOut"])
    types["ListJobMessagesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "autoscalingEvents": t.array(
                t.proxy(renames["AutoscalingEventIn"])
            ).optional(),
            "jobMessages": t.array(t.proxy(renames["JobMessageIn"])).optional(),
        }
    ).named(renames["ListJobMessagesResponseIn"])
    types["ListJobMessagesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "autoscalingEvents": t.array(
                t.proxy(renames["AutoscalingEventOut"])
            ).optional(),
            "jobMessages": t.array(t.proxy(renames["JobMessageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobMessagesResponseOut"])
    types["ReportedParallelismIn"] = t.struct(
        {"isInfinite": t.boolean().optional(), "value": t.number().optional()}
    ).named(renames["ReportedParallelismIn"])
    types["ReportedParallelismOut"] = t.struct(
        {
            "isInfinite": t.boolean().optional(),
            "value": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportedParallelismOut"])
    types["NameAndKindIn"] = t.struct(
        {"kind": t.string().optional(), "name": t.string().optional()}
    ).named(renames["NameAndKindIn"])
    types["NameAndKindOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NameAndKindOut"])
    types["JobMetricsIn"] = t.struct(
        {
            "metricTime": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricUpdateIn"])).optional(),
        }
    ).named(renames["JobMetricsIn"])
    types["JobMetricsOut"] = t.struct(
        {
            "metricTime": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricUpdateOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobMetricsOut"])
    types["StreamLocationIn"] = t.struct(
        {
            "pubsubLocation": t.proxy(renames["PubsubLocationIn"]).optional(),
            "customSourceLocation": t.proxy(
                renames["CustomSourceLocationIn"]
            ).optional(),
            "streamingStageLocation": t.proxy(
                renames["StreamingStageLocationIn"]
            ).optional(),
            "sideInputLocation": t.proxy(
                renames["StreamingSideInputLocationIn"]
            ).optional(),
        }
    ).named(renames["StreamLocationIn"])
    types["StreamLocationOut"] = t.struct(
        {
            "pubsubLocation": t.proxy(renames["PubsubLocationOut"]).optional(),
            "customSourceLocation": t.proxy(
                renames["CustomSourceLocationOut"]
            ).optional(),
            "streamingStageLocation": t.proxy(
                renames["StreamingStageLocationOut"]
            ).optional(),
            "sideInputLocation": t.proxy(
                renames["StreamingSideInputLocationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamLocationOut"])
    types["CounterMetadataIn"] = t.struct(
        {
            "otherUnits": t.string().optional(),
            "description": t.string().optional(),
            "standardUnits": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["CounterMetadataIn"])
    types["CounterMetadataOut"] = t.struct(
        {
            "otherUnits": t.string().optional(),
            "description": t.string().optional(),
            "standardUnits": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CounterMetadataOut"])
    types["ApproximateProgressIn"] = t.struct(
        {
            "position": t.proxy(renames["PositionIn"]).optional(),
            "remainingTime": t.string().optional(),
            "percentComplete": t.number().optional(),
        }
    ).named(renames["ApproximateProgressIn"])
    types["ApproximateProgressOut"] = t.struct(
        {
            "position": t.proxy(renames["PositionOut"]).optional(),
            "remainingTime": t.string().optional(),
            "percentComplete": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApproximateProgressOut"])
    types["ResourceUtilizationReportResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ResourceUtilizationReportResponseIn"])
    types["ResourceUtilizationReportResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResourceUtilizationReportResponseOut"])
    types["MountedDataDiskIn"] = t.struct({"dataDisk": t.string().optional()}).named(
        renames["MountedDataDiskIn"]
    )
    types["MountedDataDiskOut"] = t.struct(
        {
            "dataDisk": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MountedDataDiskOut"])
    types["IntegerListIn"] = t.struct(
        {"elements": t.array(t.proxy(renames["SplitInt64In"])).optional()}
    ).named(renames["IntegerListIn"])
    types["IntegerListOut"] = t.struct(
        {
            "elements": t.array(t.proxy(renames["SplitInt64Out"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerListOut"])
    types["ParallelInstructionIn"] = t.struct(
        {
            "flatten": t.proxy(renames["FlattenInstructionIn"]).optional(),
            "parDo": t.proxy(renames["ParDoInstructionIn"]).optional(),
            "write": t.proxy(renames["WriteInstructionIn"]).optional(),
            "name": t.string().optional(),
            "partialGroupByKey": t.proxy(
                renames["PartialGroupByKeyInstructionIn"]
            ).optional(),
            "read": t.proxy(renames["ReadInstructionIn"]).optional(),
            "originalName": t.string().optional(),
            "outputs": t.array(t.proxy(renames["InstructionOutputIn"])).optional(),
            "systemName": t.string().optional(),
        }
    ).named(renames["ParallelInstructionIn"])
    types["ParallelInstructionOut"] = t.struct(
        {
            "flatten": t.proxy(renames["FlattenInstructionOut"]).optional(),
            "parDo": t.proxy(renames["ParDoInstructionOut"]).optional(),
            "write": t.proxy(renames["WriteInstructionOut"]).optional(),
            "name": t.string().optional(),
            "partialGroupByKey": t.proxy(
                renames["PartialGroupByKeyInstructionOut"]
            ).optional(),
            "read": t.proxy(renames["ReadInstructionOut"]).optional(),
            "originalName": t.string().optional(),
            "outputs": t.array(t.proxy(renames["InstructionOutputOut"])).optional(),
            "systemName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParallelInstructionOut"])
    types["MetricUpdateIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "meanSum": t.struct({"_": t.string().optional()}).optional(),
            "distribution": t.struct({"_": t.string().optional()}).optional(),
            "gauge": t.struct({"_": t.string().optional()}).optional(),
            "set": t.struct({"_": t.string().optional()}).optional(),
            "cumulative": t.boolean().optional(),
            "name": t.proxy(renames["MetricStructuredNameIn"]).optional(),
            "kind": t.string().optional(),
            "scalar": t.struct({"_": t.string().optional()}).optional(),
            "meanCount": t.struct({"_": t.string().optional()}).optional(),
            "internal": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["MetricUpdateIn"])
    types["MetricUpdateOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "meanSum": t.struct({"_": t.string().optional()}).optional(),
            "distribution": t.struct({"_": t.string().optional()}).optional(),
            "gauge": t.struct({"_": t.string().optional()}).optional(),
            "set": t.struct({"_": t.string().optional()}).optional(),
            "cumulative": t.boolean().optional(),
            "name": t.proxy(renames["MetricStructuredNameOut"]).optional(),
            "kind": t.string().optional(),
            "scalar": t.struct({"_": t.string().optional()}).optional(),
            "meanCount": t.struct({"_": t.string().optional()}).optional(),
            "internal": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricUpdateOut"])
    types["LaunchTemplateResponseIn"] = t.struct(
        {"job": t.proxy(renames["JobIn"]).optional()}
    ).named(renames["LaunchTemplateResponseIn"])
    types["LaunchTemplateResponseOut"] = t.struct(
        {
            "job": t.proxy(renames["JobOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LaunchTemplateResponseOut"])
    types["StragglerInfoIn"] = t.struct(
        {
            "causes": t.struct({"_": t.string().optional()}).optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["StragglerInfoIn"])
    types["StragglerInfoOut"] = t.struct(
        {
            "causes": t.struct({"_": t.string().optional()}).optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StragglerInfoOut"])
    types["SplitInt64In"] = t.struct(
        {"lowBits": t.integer().optional(), "highBits": t.integer().optional()}
    ).named(renames["SplitInt64In"])
    types["SplitInt64Out"] = t.struct(
        {
            "lowBits": t.integer().optional(),
            "highBits": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SplitInt64Out"])
    types["LeaseWorkItemRequestIn"] = t.struct(
        {
            "workItemTypes": t.array(t.string()).optional(),
            "requestedLeaseDuration": t.string().optional(),
            "workerId": t.string().optional(),
            "currentWorkerTime": t.string().optional(),
            "location": t.string().optional(),
            "unifiedWorkerRequest": t.struct({"_": t.string().optional()}).optional(),
            "workerCapabilities": t.array(t.string()).optional(),
        }
    ).named(renames["LeaseWorkItemRequestIn"])
    types["LeaseWorkItemRequestOut"] = t.struct(
        {
            "workItemTypes": t.array(t.string()).optional(),
            "requestedLeaseDuration": t.string().optional(),
            "workerId": t.string().optional(),
            "currentWorkerTime": t.string().optional(),
            "location": t.string().optional(),
            "unifiedWorkerRequest": t.struct({"_": t.string().optional()}).optional(),
            "workerCapabilities": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LeaseWorkItemRequestOut"])
    types["StringListIn"] = t.struct(
        {"elements": t.array(t.string()).optional()}
    ).named(renames["StringListIn"])
    types["StringListOut"] = t.struct(
        {
            "elements": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StringListOut"])
    types["ApproximateSplitRequestIn"] = t.struct(
        {
            "fractionConsumed": t.number().optional(),
            "position": t.proxy(renames["PositionIn"]).optional(),
            "fractionOfRemainder": t.number().optional(),
        }
    ).named(renames["ApproximateSplitRequestIn"])
    types["ApproximateSplitRequestOut"] = t.struct(
        {
            "fractionConsumed": t.number().optional(),
            "position": t.proxy(renames["PositionOut"]).optional(),
            "fractionOfRemainder": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApproximateSplitRequestOut"])
    types["CPUTimeIn"] = t.struct(
        {
            "totalMs": t.string().optional(),
            "timestamp": t.string().optional(),
            "rate": t.number().optional(),
        }
    ).named(renames["CPUTimeIn"])
    types["CPUTimeOut"] = t.struct(
        {
            "totalMs": t.string().optional(),
            "timestamp": t.string().optional(),
            "rate": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CPUTimeOut"])
    types["FloatingPointListIn"] = t.struct(
        {"elements": t.array(t.number()).optional()}
    ).named(renames["FloatingPointListIn"])
    types["FloatingPointListOut"] = t.struct(
        {
            "elements": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloatingPointListOut"])
    types["WorkerMessageResponseIn"] = t.struct(
        {
            "workerShutdownNoticeResponse": t.proxy(
                renames["WorkerShutdownNoticeResponseIn"]
            ).optional(),
            "workerHealthReportResponse": t.proxy(
                renames["WorkerHealthReportResponseIn"]
            ).optional(),
            "workerMetricsResponse": t.proxy(
                renames["ResourceUtilizationReportResponseIn"]
            ).optional(),
            "workerThreadScalingReportResponse": t.proxy(
                renames["WorkerThreadScalingReportResponseIn"]
            ).optional(),
        }
    ).named(renames["WorkerMessageResponseIn"])
    types["WorkerMessageResponseOut"] = t.struct(
        {
            "workerShutdownNoticeResponse": t.proxy(
                renames["WorkerShutdownNoticeResponseOut"]
            ).optional(),
            "workerHealthReportResponse": t.proxy(
                renames["WorkerHealthReportResponseOut"]
            ).optional(),
            "workerMetricsResponse": t.proxy(
                renames["ResourceUtilizationReportResponseOut"]
            ).optional(),
            "workerThreadScalingReportResponse": t.proxy(
                renames["WorkerThreadScalingReportResponseOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerMessageResponseOut"])
    types["MultiOutputInfoIn"] = t.struct({"tag": t.string().optional()}).named(
        renames["MultiOutputInfoIn"]
    )
    types["MultiOutputInfoOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultiOutputInfoOut"])
    types["ComponentTransformIn"] = t.struct(
        {
            "name": t.string().optional(),
            "originalTransform": t.string().optional(),
            "userName": t.string().optional(),
        }
    ).named(renames["ComponentTransformIn"])
    types["ComponentTransformOut"] = t.struct(
        {
            "name": t.string().optional(),
            "originalTransform": t.string().optional(),
            "userName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComponentTransformOut"])
    types["ParameterIn"] = t.struct(
        {
            "value": t.struct({"_": t.string().optional()}).optional(),
            "key": t.string().optional(),
        }
    ).named(renames["ParameterIn"])
    types["ParameterOut"] = t.struct(
        {
            "value": t.struct({"_": t.string().optional()}).optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParameterOut"])
    types["GetDebugConfigResponseIn"] = t.struct(
        {"config": t.string().optional()}
    ).named(renames["GetDebugConfigResponseIn"])
    types["GetDebugConfigResponseOut"] = t.struct(
        {
            "config": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetDebugConfigResponseOut"])
    types["WorkerThreadScalingReportIn"] = t.struct(
        {"currentThreadCount": t.integer().optional()}
    ).named(renames["WorkerThreadScalingReportIn"])
    types["WorkerThreadScalingReportOut"] = t.struct(
        {
            "currentThreadCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerThreadScalingReportOut"])
    types["ComputationTopologyIn"] = t.struct(
        {
            "computationId": t.string().optional(),
            "outputs": t.array(t.proxy(renames["StreamLocationIn"])).optional(),
            "keyRanges": t.array(t.proxy(renames["KeyRangeLocationIn"])).optional(),
            "systemStageName": t.string().optional(),
            "stateFamilies": t.array(
                t.proxy(renames["StateFamilyConfigIn"])
            ).optional(),
            "inputs": t.array(t.proxy(renames["StreamLocationIn"])).optional(),
        }
    ).named(renames["ComputationTopologyIn"])
    types["ComputationTopologyOut"] = t.struct(
        {
            "computationId": t.string().optional(),
            "outputs": t.array(t.proxy(renames["StreamLocationOut"])).optional(),
            "keyRanges": t.array(t.proxy(renames["KeyRangeLocationOut"])).optional(),
            "systemStageName": t.string().optional(),
            "stateFamilies": t.array(
                t.proxy(renames["StateFamilyConfigOut"])
            ).optional(),
            "inputs": t.array(t.proxy(renames["StreamLocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputationTopologyOut"])
    types["ExecutionStageSummaryIn"] = t.struct(
        {
            "prerequisiteStage": t.array(t.string()).optional(),
            "componentTransform": t.array(
                t.proxy(renames["ComponentTransformIn"])
            ).optional(),
            "outputSource": t.array(t.proxy(renames["StageSourceIn"])).optional(),
            "componentSource": t.array(
                t.proxy(renames["ComponentSourceIn"])
            ).optional(),
            "inputSource": t.array(t.proxy(renames["StageSourceIn"])).optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ExecutionStageSummaryIn"])
    types["ExecutionStageSummaryOut"] = t.struct(
        {
            "prerequisiteStage": t.array(t.string()).optional(),
            "componentTransform": t.array(
                t.proxy(renames["ComponentTransformOut"])
            ).optional(),
            "outputSource": t.array(t.proxy(renames["StageSourceOut"])).optional(),
            "componentSource": t.array(
                t.proxy(renames["ComponentSourceOut"])
            ).optional(),
            "inputSource": t.array(t.proxy(renames["StageSourceOut"])).optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionStageSummaryOut"])
    types["SourceSplitOptionsIn"] = t.struct(
        {
            "desiredBundleSizeBytes": t.string().optional(),
            "desiredShardSizeBytes": t.string().optional(),
        }
    ).named(renames["SourceSplitOptionsIn"])
    types["SourceSplitOptionsOut"] = t.struct(
        {
            "desiredBundleSizeBytes": t.string().optional(),
            "desiredShardSizeBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceSplitOptionsOut"])
    types["DeleteSnapshotResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteSnapshotResponseIn"]
    )
    types["DeleteSnapshotResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteSnapshotResponseOut"])
    types["SnapshotJobRequestIn"] = t.struct(
        {
            "snapshotSources": t.boolean().optional(),
            "ttl": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["SnapshotJobRequestIn"])
    types["SnapshotJobRequestOut"] = t.struct(
        {
            "snapshotSources": t.boolean().optional(),
            "ttl": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnapshotJobRequestOut"])
    types["WorkerShutdownNoticeIn"] = t.struct({"reason": t.string().optional()}).named(
        renames["WorkerShutdownNoticeIn"]
    )
    types["WorkerShutdownNoticeOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerShutdownNoticeOut"])
    types["DataDiskAssignmentIn"] = t.struct(
        {
            "vmInstance": t.string().optional(),
            "dataDisks": t.array(t.string()).optional(),
        }
    ).named(renames["DataDiskAssignmentIn"])
    types["DataDiskAssignmentOut"] = t.struct(
        {
            "vmInstance": t.string().optional(),
            "dataDisks": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataDiskAssignmentOut"])
    types["GetTemplateResponseIn"] = t.struct(
        {
            "status": t.proxy(renames["StatusIn"]).optional(),
            "runtimeMetadata": t.proxy(renames["RuntimeMetadataIn"]).optional(),
            "templateType": t.string().optional(),
            "metadata": t.proxy(renames["TemplateMetadataIn"]).optional(),
        }
    ).named(renames["GetTemplateResponseIn"])
    types["GetTemplateResponseOut"] = t.struct(
        {
            "status": t.proxy(renames["StatusOut"]).optional(),
            "runtimeMetadata": t.proxy(renames["RuntimeMetadataOut"]).optional(),
            "templateType": t.string().optional(),
            "metadata": t.proxy(renames["TemplateMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetTemplateResponseOut"])
    types["EnvironmentIn"] = t.struct(
        {
            "clusterManagerApiService": t.string().optional(),
            "experiments": t.array(t.string()).optional(),
            "workerZone": t.string().optional(),
            "sdkPipelineOptions": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccountEmail": t.string().optional(),
            "dataset": t.string().optional(),
            "flexResourceSchedulingGoal": t.string().optional(),
            "workerPools": t.array(t.proxy(renames["WorkerPoolIn"])).optional(),
            "internalExperiments": t.struct({"_": t.string().optional()}).optional(),
            "tempStoragePrefix": t.string().optional(),
            "serviceKmsKeyName": t.string().optional(),
            "workerRegion": t.string().optional(),
            "serviceOptions": t.array(t.string()).optional(),
            "version": t.struct({"_": t.string().optional()}).optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "userAgent": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["EnvironmentIn"])
    types["EnvironmentOut"] = t.struct(
        {
            "shuffleMode": t.string().optional(),
            "clusterManagerApiService": t.string().optional(),
            "experiments": t.array(t.string()).optional(),
            "workerZone": t.string().optional(),
            "sdkPipelineOptions": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccountEmail": t.string().optional(),
            "dataset": t.string().optional(),
            "flexResourceSchedulingGoal": t.string().optional(),
            "workerPools": t.array(t.proxy(renames["WorkerPoolOut"])).optional(),
            "internalExperiments": t.struct({"_": t.string().optional()}).optional(),
            "tempStoragePrefix": t.string().optional(),
            "serviceKmsKeyName": t.string().optional(),
            "workerRegion": t.string().optional(),
            "serviceOptions": t.array(t.string()).optional(),
            "version": t.struct({"_": t.string().optional()}).optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "userAgent": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentOut"])
    types["WorkerMessageCodeIn"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "code": t.string().optional(),
        }
    ).named(renames["WorkerMessageCodeIn"])
    types["WorkerMessageCodeOut"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerMessageCodeOut"])
    types["ReportWorkItemStatusRequestIn"] = t.struct(
        {
            "unifiedWorkerRequest": t.struct({"_": t.string().optional()}).optional(),
            "workItemStatuses": t.array(
                t.proxy(renames["WorkItemStatusIn"])
            ).optional(),
            "currentWorkerTime": t.string().optional(),
            "workerId": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ReportWorkItemStatusRequestIn"])
    types["ReportWorkItemStatusRequestOut"] = t.struct(
        {
            "unifiedWorkerRequest": t.struct({"_": t.string().optional()}).optional(),
            "workItemStatuses": t.array(
                t.proxy(renames["WorkItemStatusOut"])
            ).optional(),
            "currentWorkerTime": t.string().optional(),
            "workerId": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportWorkItemStatusRequestOut"])
    types["ParameterMetadataIn"] = t.struct(
        {
            "label": t.string(),
            "paramType": t.string().optional(),
            "regexes": t.array(t.string()).optional(),
            "helpText": t.string(),
            "customMetadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "parentName": t.string().optional(),
            "parentTriggerValues": t.array(t.string()).optional(),
            "groupName": t.string().optional(),
            "isOptional": t.boolean().optional(),
        }
    ).named(renames["ParameterMetadataIn"])
    types["ParameterMetadataOut"] = t.struct(
        {
            "label": t.string(),
            "paramType": t.string().optional(),
            "regexes": t.array(t.string()).optional(),
            "helpText": t.string(),
            "customMetadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "parentName": t.string().optional(),
            "parentTriggerValues": t.array(t.string()).optional(),
            "groupName": t.string().optional(),
            "isOptional": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParameterMetadataOut"])
    types["StepIn"] = t.struct(
        {
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["StepIn"])
    types["StepOut"] = t.struct(
        {
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StepOut"])
    types["SourceOperationRequestIn"] = t.struct(
        {
            "split": t.proxy(renames["SourceSplitRequestIn"]).optional(),
            "originalName": t.string().optional(),
            "stageName": t.string().optional(),
            "systemName": t.string().optional(),
            "getMetadata": t.proxy(renames["SourceGetMetadataRequestIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SourceOperationRequestIn"])
    types["SourceOperationRequestOut"] = t.struct(
        {
            "split": t.proxy(renames["SourceSplitRequestOut"]).optional(),
            "originalName": t.string().optional(),
            "stageName": t.string().optional(),
            "systemName": t.string().optional(),
            "getMetadata": t.proxy(renames["SourceGetMetadataRequestOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOperationRequestOut"])
    types["LaunchFlexTemplateResponseIn"] = t.struct(
        {"job": t.proxy(renames["JobIn"]).optional()}
    ).named(renames["LaunchFlexTemplateResponseIn"])
    types["LaunchFlexTemplateResponseOut"] = t.struct(
        {
            "job": t.proxy(renames["JobOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LaunchFlexTemplateResponseOut"])
    types["WorkerShutdownNoticeResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["WorkerShutdownNoticeResponseIn"])
    types["WorkerShutdownNoticeResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WorkerShutdownNoticeResponseOut"])
    types["CreateJobFromTemplateRequestIn"] = t.struct(
        {
            "gcsPath": t.string(),
            "location": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
            "jobName": t.string(),
        }
    ).named(renames["CreateJobFromTemplateRequestIn"])
    types["CreateJobFromTemplateRequestOut"] = t.struct(
        {
            "gcsPath": t.string(),
            "location": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "environment": t.proxy(renames["RuntimeEnvironmentOut"]).optional(),
            "jobName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateJobFromTemplateRequestOut"])
    types["PipelineDescriptionIn"] = t.struct(
        {
            "displayData": t.array(t.proxy(renames["DisplayDataIn"])).optional(),
            "originalPipelineTransform": t.array(
                t.proxy(renames["TransformSummaryIn"])
            ).optional(),
            "stepNamesHash": t.string().optional(),
            "executionPipelineStage": t.array(
                t.proxy(renames["ExecutionStageSummaryIn"])
            ).optional(),
        }
    ).named(renames["PipelineDescriptionIn"])
    types["PipelineDescriptionOut"] = t.struct(
        {
            "displayData": t.array(t.proxy(renames["DisplayDataOut"])).optional(),
            "originalPipelineTransform": t.array(
                t.proxy(renames["TransformSummaryOut"])
            ).optional(),
            "stepNamesHash": t.string().optional(),
            "executionPipelineStage": t.array(
                t.proxy(renames["ExecutionStageSummaryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PipelineDescriptionOut"])
    types["ContainerSpecIn"] = t.struct(
        {
            "imageRepositoryPasswordSecretId": t.string().optional(),
            "imageRepositoryUsernameSecretId": t.string().optional(),
            "image": t.string().optional(),
            "metadata": t.proxy(renames["TemplateMetadataIn"]).optional(),
            "imageRepositoryCertPath": t.string().optional(),
            "sdkInfo": t.proxy(renames["SDKInfoIn"]),
            "defaultEnvironment": t.proxy(
                renames["FlexTemplateRuntimeEnvironmentIn"]
            ).optional(),
        }
    ).named(renames["ContainerSpecIn"])
    types["ContainerSpecOut"] = t.struct(
        {
            "imageRepositoryPasswordSecretId": t.string().optional(),
            "imageRepositoryUsernameSecretId": t.string().optional(),
            "image": t.string().optional(),
            "metadata": t.proxy(renames["TemplateMetadataOut"]).optional(),
            "imageRepositoryCertPath": t.string().optional(),
            "sdkInfo": t.proxy(renames["SDKInfoOut"]),
            "defaultEnvironment": t.proxy(
                renames["FlexTemplateRuntimeEnvironmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerSpecOut"])
    types["TopologyConfigIn"] = t.struct(
        {
            "computations": t.array(
                t.proxy(renames["ComputationTopologyIn"])
            ).optional(),
            "dataDiskAssignments": t.array(
                t.proxy(renames["DataDiskAssignmentIn"])
            ).optional(),
            "userStageToComputationNameMap": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "persistentStateVersion": t.integer().optional(),
            "forwardingKeyBits": t.integer().optional(),
        }
    ).named(renames["TopologyConfigIn"])
    types["TopologyConfigOut"] = t.struct(
        {
            "computations": t.array(
                t.proxy(renames["ComputationTopologyOut"])
            ).optional(),
            "dataDiskAssignments": t.array(
                t.proxy(renames["DataDiskAssignmentOut"])
            ).optional(),
            "userStageToComputationNameMap": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "persistentStateVersion": t.integer().optional(),
            "forwardingKeyBits": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TopologyConfigOut"])
    types["SdkVersionIn"] = t.struct(
        {
            "versionDisplayName": t.string().optional(),
            "sdkSupportStatus": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["SdkVersionIn"])
    types["SdkVersionOut"] = t.struct(
        {
            "versionDisplayName": t.string().optional(),
            "sdkSupportStatus": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SdkVersionOut"])
    types["ReadInstructionIn"] = t.struct(
        {"source": t.proxy(renames["SourceIn"]).optional()}
    ).named(renames["ReadInstructionIn"])
    types["ReadInstructionOut"] = t.struct(
        {
            "source": t.proxy(renames["SourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadInstructionOut"])
    types["MapTaskIn"] = t.struct(
        {
            "counterPrefix": t.string().optional(),
            "instructions": t.array(
                t.proxy(renames["ParallelInstructionIn"])
            ).optional(),
            "systemName": t.string().optional(),
            "stageName": t.string().optional(),
        }
    ).named(renames["MapTaskIn"])
    types["MapTaskOut"] = t.struct(
        {
            "counterPrefix": t.string().optional(),
            "instructions": t.array(
                t.proxy(renames["ParallelInstructionOut"])
            ).optional(),
            "systemName": t.string().optional(),
            "stageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MapTaskOut"])
    types["SpannerIODetailsIn"] = t.struct(
        {
            "instanceId": t.string().optional(),
            "databaseId": t.string().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["SpannerIODetailsIn"])
    types["SpannerIODetailsOut"] = t.struct(
        {
            "instanceId": t.string().optional(),
            "databaseId": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpannerIODetailsOut"])
    types["SourceSplitResponseIn"] = t.struct(
        {
            "outcome": t.string().optional(),
            "bundles": t.array(t.proxy(renames["DerivedSourceIn"])).optional(),
            "shards": t.array(t.proxy(renames["SourceSplitShardIn"])).optional(),
        }
    ).named(renames["SourceSplitResponseIn"])
    types["SourceSplitResponseOut"] = t.struct(
        {
            "outcome": t.string().optional(),
            "bundles": t.array(t.proxy(renames["DerivedSourceOut"])).optional(),
            "shards": t.array(t.proxy(renames["SourceSplitShardOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceSplitResponseOut"])
    types["KeyRangeLocationIn"] = t.struct(
        {
            "end": t.string().optional(),
            "dataDisk": t.string().optional(),
            "deprecatedPersistentDirectory": t.string().optional(),
            "deliveryEndpoint": t.string().optional(),
            "start": t.string().optional(),
        }
    ).named(renames["KeyRangeLocationIn"])
    types["KeyRangeLocationOut"] = t.struct(
        {
            "end": t.string().optional(),
            "dataDisk": t.string().optional(),
            "deprecatedPersistentDirectory": t.string().optional(),
            "deliveryEndpoint": t.string().optional(),
            "start": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyRangeLocationOut"])
    types["TransformSummaryIn"] = t.struct(
        {
            "outputCollectionName": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "displayData": t.array(t.proxy(renames["DisplayDataIn"])).optional(),
            "inputCollectionName": t.array(t.string()).optional(),
        }
    ).named(renames["TransformSummaryIn"])
    types["TransformSummaryOut"] = t.struct(
        {
            "outputCollectionName": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "displayData": t.array(t.proxy(renames["DisplayDataOut"])).optional(),
            "inputCollectionName": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransformSummaryOut"])
    types["SendDebugCaptureResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SendDebugCaptureResponseIn"]
    )
    types["SendDebugCaptureResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SendDebugCaptureResponseOut"])
    types["BigQueryIODetailsIn"] = t.struct(
        {
            "table": t.string().optional(),
            "query": t.string().optional(),
            "projectId": t.string().optional(),
            "dataset": t.string().optional(),
        }
    ).named(renames["BigQueryIODetailsIn"])
    types["BigQueryIODetailsOut"] = t.struct(
        {
            "table": t.string().optional(),
            "query": t.string().optional(),
            "projectId": t.string().optional(),
            "dataset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryIODetailsOut"])
    types["ResourceUtilizationReportIn"] = t.struct(
        {
            "cpuTime": t.array(t.proxy(renames["CPUTimeIn"])).optional(),
            "memoryInfo": t.array(t.proxy(renames["MemInfoIn"])).optional(),
            "containers": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ResourceUtilizationReportIn"])
    types["ResourceUtilizationReportOut"] = t.struct(
        {
            "cpuTime": t.array(t.proxy(renames["CPUTimeOut"])).optional(),
            "memoryInfo": t.array(t.proxy(renames["MemInfoOut"])).optional(),
            "containers": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceUtilizationReportOut"])
    types["CounterStructuredNameIn"] = t.struct(
        {
            "portion": t.string().optional(),
            "inputIndex": t.integer().optional(),
            "origin": t.string().optional(),
            "originNamespace": t.string().optional(),
            "executionStepName": t.string().optional(),
            "originalStepName": t.string().optional(),
            "workerId": t.string().optional(),
            "originalRequestingStepName": t.string().optional(),
            "name": t.string().optional(),
            "componentStepName": t.string().optional(),
        }
    ).named(renames["CounterStructuredNameIn"])
    types["CounterStructuredNameOut"] = t.struct(
        {
            "portion": t.string().optional(),
            "inputIndex": t.integer().optional(),
            "origin": t.string().optional(),
            "originNamespace": t.string().optional(),
            "executionStepName": t.string().optional(),
            "originalStepName": t.string().optional(),
            "workerId": t.string().optional(),
            "originalRequestingStepName": t.string().optional(),
            "name": t.string().optional(),
            "componentStepName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CounterStructuredNameOut"])
    types["ApproximateReportedProgressIn"] = t.struct(
        {
            "remainingParallelism": t.proxy(
                renames["ReportedParallelismIn"]
            ).optional(),
            "consumedParallelism": t.proxy(renames["ReportedParallelismIn"]).optional(),
            "fractionConsumed": t.number().optional(),
            "position": t.proxy(renames["PositionIn"]).optional(),
        }
    ).named(renames["ApproximateReportedProgressIn"])
    types["ApproximateReportedProgressOut"] = t.struct(
        {
            "remainingParallelism": t.proxy(
                renames["ReportedParallelismOut"]
            ).optional(),
            "consumedParallelism": t.proxy(
                renames["ReportedParallelismOut"]
            ).optional(),
            "fractionConsumed": t.number().optional(),
            "position": t.proxy(renames["PositionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApproximateReportedProgressOut"])
    types["PubsubSnapshotMetadataIn"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "snapshotName": t.string().optional(),
            "topicName": t.string().optional(),
        }
    ).named(renames["PubsubSnapshotMetadataIn"])
    types["PubsubSnapshotMetadataOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "snapshotName": t.string().optional(),
            "topicName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubSnapshotMetadataOut"])
    types["MetricShortIdIn"] = t.struct(
        {"metricIndex": t.integer().optional(), "shortId": t.string().optional()}
    ).named(renames["MetricShortIdIn"])
    types["MetricShortIdOut"] = t.struct(
        {
            "metricIndex": t.integer().optional(),
            "shortId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricShortIdOut"])
    types["WriteInstructionIn"] = t.struct(
        {
            "sink": t.proxy(renames["SinkIn"]).optional(),
            "input": t.proxy(renames["InstructionInputIn"]).optional(),
        }
    ).named(renames["WriteInstructionIn"])
    types["WriteInstructionOut"] = t.struct(
        {
            "sink": t.proxy(renames["SinkOut"]).optional(),
            "input": t.proxy(renames["InstructionInputOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteInstructionOut"])
    types["ConcatPositionIn"] = t.struct(
        {
            "position": t.proxy(renames["PositionIn"]).optional(),
            "index": t.integer().optional(),
        }
    ).named(renames["ConcatPositionIn"])
    types["ConcatPositionOut"] = t.struct(
        {
            "position": t.proxy(renames["PositionOut"]).optional(),
            "index": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConcatPositionOut"])
    types["ListJobsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "failedLocation": t.array(t.proxy(renames["FailedLocationIn"])).optional(),
            "jobs": t.array(t.proxy(renames["JobIn"])).optional(),
        }
    ).named(renames["ListJobsResponseIn"])
    types["ListJobsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "failedLocation": t.array(t.proxy(renames["FailedLocationOut"])).optional(),
            "jobs": t.array(t.proxy(renames["JobOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobsResponseOut"])
    types["HotKeyDetectionIn"] = t.struct(
        {
            "hotKeyAge": t.string().optional(),
            "userStepName": t.string().optional(),
            "systemName": t.string().optional(),
        }
    ).named(renames["HotKeyDetectionIn"])
    types["HotKeyDetectionOut"] = t.struct(
        {
            "hotKeyAge": t.string().optional(),
            "userStepName": t.string().optional(),
            "systemName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HotKeyDetectionOut"])
    types["DiskIn"] = t.struct(
        {
            "sizeGb": t.integer().optional(),
            "mountPoint": t.string().optional(),
            "diskType": t.string().optional(),
        }
    ).named(renames["DiskIn"])
    types["DiskOut"] = t.struct(
        {
            "sizeGb": t.integer().optional(),
            "mountPoint": t.string().optional(),
            "diskType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskOut"])
    types["SourceSplitShardIn"] = t.struct(
        {
            "source": t.proxy(renames["SourceIn"]).optional(),
            "derivationMode": t.string().optional(),
        }
    ).named(renames["SourceSplitShardIn"])
    types["SourceSplitShardOut"] = t.struct(
        {
            "source": t.proxy(renames["SourceOut"]).optional(),
            "derivationMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceSplitShardOut"])
    types["StructuredMessageIn"] = t.struct(
        {
            "messageKey": t.string().optional(),
            "messageText": t.string().optional(),
            "parameters": t.array(t.proxy(renames["ParameterIn"])).optional(),
        }
    ).named(renames["StructuredMessageIn"])
    types["StructuredMessageOut"] = t.struct(
        {
            "messageKey": t.string().optional(),
            "messageText": t.string().optional(),
            "parameters": t.array(t.proxy(renames["ParameterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructuredMessageOut"])
    types["FlattenInstructionIn"] = t.struct(
        {"inputs": t.array(t.proxy(renames["InstructionInputIn"])).optional()}
    ).named(renames["FlattenInstructionIn"])
    types["FlattenInstructionOut"] = t.struct(
        {
            "inputs": t.array(t.proxy(renames["InstructionInputOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FlattenInstructionOut"])
    types["FlexTemplateRuntimeEnvironmentIn"] = t.struct(
        {
            "enableStreamingEngine": t.boolean().optional(),
            "launcherMachineType": t.string().optional(),
            "stagingLocation": t.string().optional(),
            "machineType": t.string().optional(),
            "maxWorkers": t.integer().optional(),
            "network": t.string().optional(),
            "workerZone": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "autoscalingAlgorithm": t.string().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccountEmail": t.string().optional(),
            "dumpHeapOnOom": t.boolean().optional(),
            "tempLocation": t.string().optional(),
            "subnetwork": t.string().optional(),
            "flexrsGoal": t.string().optional(),
            "enableLauncherVmSerialPortLogging": t.boolean().optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "ipConfiguration": t.string().optional(),
            "workerRegion": t.string().optional(),
            "saveHeapDumpsToGcsPath": t.string().optional(),
            "diskSizeGb": t.integer().optional(),
            "numWorkers": t.integer().optional(),
            "zone": t.string().optional(),
            "sdkContainerImage": t.string().optional(),
        }
    ).named(renames["FlexTemplateRuntimeEnvironmentIn"])
    types["FlexTemplateRuntimeEnvironmentOut"] = t.struct(
        {
            "enableStreamingEngine": t.boolean().optional(),
            "launcherMachineType": t.string().optional(),
            "stagingLocation": t.string().optional(),
            "machineType": t.string().optional(),
            "maxWorkers": t.integer().optional(),
            "network": t.string().optional(),
            "workerZone": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "autoscalingAlgorithm": t.string().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccountEmail": t.string().optional(),
            "dumpHeapOnOom": t.boolean().optional(),
            "tempLocation": t.string().optional(),
            "subnetwork": t.string().optional(),
            "flexrsGoal": t.string().optional(),
            "enableLauncherVmSerialPortLogging": t.boolean().optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "ipConfiguration": t.string().optional(),
            "workerRegion": t.string().optional(),
            "saveHeapDumpsToGcsPath": t.string().optional(),
            "diskSizeGb": t.integer().optional(),
            "numWorkers": t.integer().optional(),
            "zone": t.string().optional(),
            "sdkContainerImage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FlexTemplateRuntimeEnvironmentOut"])
    types["TaskRunnerSettingsIn"] = t.struct(
        {
            "streamingWorkerMainClass": t.string().optional(),
            "vmId": t.string().optional(),
            "logDir": t.string().optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "baseTaskDir": t.string().optional(),
            "taskGroup": t.string().optional(),
            "logToSerialconsole": t.boolean().optional(),
            "languageHint": t.string().optional(),
            "parallelWorkerSettings": t.proxy(renames["WorkerSettingsIn"]).optional(),
            "workflowFileName": t.string().optional(),
            "taskUser": t.string().optional(),
            "harnessCommand": t.string().optional(),
            "alsologtostderr": t.boolean().optional(),
            "continueOnException": t.boolean().optional(),
            "dataflowApiVersion": t.string().optional(),
            "logUploadLocation": t.string().optional(),
            "commandlinesFileName": t.string().optional(),
            "baseUrl": t.string().optional(),
            "tempStoragePrefix": t.string().optional(),
        }
    ).named(renames["TaskRunnerSettingsIn"])
    types["TaskRunnerSettingsOut"] = t.struct(
        {
            "streamingWorkerMainClass": t.string().optional(),
            "vmId": t.string().optional(),
            "logDir": t.string().optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "baseTaskDir": t.string().optional(),
            "taskGroup": t.string().optional(),
            "logToSerialconsole": t.boolean().optional(),
            "languageHint": t.string().optional(),
            "parallelWorkerSettings": t.proxy(renames["WorkerSettingsOut"]).optional(),
            "workflowFileName": t.string().optional(),
            "taskUser": t.string().optional(),
            "harnessCommand": t.string().optional(),
            "alsologtostderr": t.boolean().optional(),
            "continueOnException": t.boolean().optional(),
            "dataflowApiVersion": t.string().optional(),
            "logUploadLocation": t.string().optional(),
            "commandlinesFileName": t.string().optional(),
            "baseUrl": t.string().optional(),
            "tempStoragePrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskRunnerSettingsOut"])
    types["PubsubLocationIn"] = t.struct(
        {
            "dropLateData": t.boolean().optional(),
            "withAttributes": t.boolean().optional(),
            "idLabel": t.string().optional(),
            "subscription": t.string().optional(),
            "trackingSubscription": t.string().optional(),
            "timestampLabel": t.string().optional(),
            "topic": t.string().optional(),
        }
    ).named(renames["PubsubLocationIn"])
    types["PubsubLocationOut"] = t.struct(
        {
            "dropLateData": t.boolean().optional(),
            "withAttributes": t.boolean().optional(),
            "idLabel": t.string().optional(),
            "subscription": t.string().optional(),
            "trackingSubscription": t.string().optional(),
            "timestampLabel": t.string().optional(),
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubLocationOut"])
    types["SinkIn"] = t.struct(
        {
            "spec": t.struct({"_": t.string().optional()}).optional(),
            "codec": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SinkIn"])
    types["SinkOut"] = t.struct(
        {
            "spec": t.struct({"_": t.string().optional()}).optional(),
            "codec": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SinkOut"])
    types["StragglerDebuggingInfoIn"] = t.struct(
        {"hotKey": t.proxy(renames["HotKeyDebuggingInfoIn"]).optional()}
    ).named(renames["StragglerDebuggingInfoIn"])
    types["StragglerDebuggingInfoOut"] = t.struct(
        {
            "hotKey": t.proxy(renames["HotKeyDebuggingInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StragglerDebuggingInfoOut"])
    types["SeqMapTaskOutputInfoIn"] = t.struct(
        {"tag": t.string().optional(), "sink": t.proxy(renames["SinkIn"]).optional()}
    ).named(renames["SeqMapTaskOutputInfoIn"])
    types["SeqMapTaskOutputInfoOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "sink": t.proxy(renames["SinkOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SeqMapTaskOutputInfoOut"])
    types["SourceOperationResponseIn"] = t.struct(
        {
            "getMetadata": t.proxy(renames["SourceGetMetadataResponseIn"]).optional(),
            "split": t.proxy(renames["SourceSplitResponseIn"]).optional(),
        }
    ).named(renames["SourceOperationResponseIn"])
    types["SourceOperationResponseOut"] = t.struct(
        {
            "getMetadata": t.proxy(renames["SourceGetMetadataResponseOut"]).optional(),
            "split": t.proxy(renames["SourceSplitResponseOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOperationResponseOut"])
    types["WorkerMessageIn"] = t.struct(
        {
            "workerShutdownNotice": t.proxy(
                renames["WorkerShutdownNoticeIn"]
            ).optional(),
            "workerThreadScalingReport": t.proxy(
                renames["WorkerThreadScalingReportIn"]
            ).optional(),
            "workerHealthReport": t.proxy(renames["WorkerHealthReportIn"]).optional(),
            "workerLifecycleEvent": t.proxy(
                renames["WorkerLifecycleEventIn"]
            ).optional(),
            "time": t.string().optional(),
            "workerMessageCode": t.proxy(renames["WorkerMessageCodeIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "workerMetrics": t.proxy(renames["ResourceUtilizationReportIn"]).optional(),
        }
    ).named(renames["WorkerMessageIn"])
    types["WorkerMessageOut"] = t.struct(
        {
            "workerShutdownNotice": t.proxy(
                renames["WorkerShutdownNoticeOut"]
            ).optional(),
            "workerThreadScalingReport": t.proxy(
                renames["WorkerThreadScalingReportOut"]
            ).optional(),
            "workerHealthReport": t.proxy(renames["WorkerHealthReportOut"]).optional(),
            "workerLifecycleEvent": t.proxy(
                renames["WorkerLifecycleEventOut"]
            ).optional(),
            "time": t.string().optional(),
            "workerMessageCode": t.proxy(renames["WorkerMessageCodeOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "workerMetrics": t.proxy(
                renames["ResourceUtilizationReportOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerMessageOut"])
    types["StageSummaryIn"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["MetricUpdateIn"])).optional(),
            "progress": t.proxy(renames["ProgressTimeseriesIn"]).optional(),
            "stragglerSummary": t.proxy(renames["StragglerSummaryIn"]).optional(),
            "endTime": t.string().optional(),
            "stageId": t.string().optional(),
            "startTime": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["StageSummaryIn"])
    types["StageSummaryOut"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["MetricUpdateOut"])).optional(),
            "progress": t.proxy(renames["ProgressTimeseriesOut"]).optional(),
            "stragglerSummary": t.proxy(renames["StragglerSummaryOut"]).optional(),
            "endTime": t.string().optional(),
            "stageId": t.string().optional(),
            "startTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StageSummaryOut"])
    types["DistributionUpdateIn"] = t.struct(
        {
            "max": t.proxy(renames["SplitInt64In"]).optional(),
            "histogram": t.proxy(renames["HistogramIn"]).optional(),
            "min": t.proxy(renames["SplitInt64In"]).optional(),
            "sum": t.proxy(renames["SplitInt64In"]).optional(),
            "count": t.proxy(renames["SplitInt64In"]).optional(),
            "sumOfSquares": t.number().optional(),
        }
    ).named(renames["DistributionUpdateIn"])
    types["DistributionUpdateOut"] = t.struct(
        {
            "max": t.proxy(renames["SplitInt64Out"]).optional(),
            "histogram": t.proxy(renames["HistogramOut"]).optional(),
            "min": t.proxy(renames["SplitInt64Out"]).optional(),
            "sum": t.proxy(renames["SplitInt64Out"]).optional(),
            "count": t.proxy(renames["SplitInt64Out"]).optional(),
            "sumOfSquares": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DistributionUpdateOut"])
    types["PositionIn"] = t.struct(
        {
            "key": t.string().optional(),
            "concatPosition": t.proxy(renames["ConcatPositionIn"]).optional(),
            "shufflePosition": t.string().optional(),
            "byteOffset": t.string().optional(),
            "recordIndex": t.string().optional(),
            "end": t.boolean().optional(),
        }
    ).named(renames["PositionIn"])
    types["PositionOut"] = t.struct(
        {
            "key": t.string().optional(),
            "concatPosition": t.proxy(renames["ConcatPositionOut"]).optional(),
            "shufflePosition": t.string().optional(),
            "byteOffset": t.string().optional(),
            "recordIndex": t.string().optional(),
            "end": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PositionOut"])
    types["JobIn"] = t.struct(
        {
            "stageStates": t.array(
                t.proxy(renames["ExecutionStageStateIn"])
            ).optional(),
            "startTime": t.string().optional(),
            "name": t.string().optional(),
            "currentStateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "clientRequestId": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "createdFromSnapshotId": t.string().optional(),
            "executionInfo": t.proxy(renames["JobExecutionInfoIn"]).optional(),
            "replaceJobId": t.string().optional(),
            "id": t.string().optional(),
            "tempFiles": t.array(t.string()).optional(),
            "projectId": t.string().optional(),
            "transformNameMapping": t.struct({"_": t.string().optional()}).optional(),
            "requestedState": t.string().optional(),
            "environment": t.proxy(renames["EnvironmentIn"]).optional(),
            "runtimeUpdatableParams": t.proxy(
                renames["RuntimeUpdatableParamsIn"]
            ).optional(),
            "type": t.string().optional(),
            "pipelineDescription": t.proxy(renames["PipelineDescriptionIn"]).optional(),
            "currentState": t.string().optional(),
            "location": t.string().optional(),
            "steps": t.array(t.proxy(renames["StepIn"])).optional(),
            "replacedByJobId": t.string().optional(),
            "jobMetadata": t.proxy(renames["JobMetadataIn"]).optional(),
            "stepsLocation": t.string().optional(),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "stageStates": t.array(
                t.proxy(renames["ExecutionStageStateOut"])
            ).optional(),
            "startTime": t.string().optional(),
            "name": t.string().optional(),
            "currentStateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "clientRequestId": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "createdFromSnapshotId": t.string().optional(),
            "executionInfo": t.proxy(renames["JobExecutionInfoOut"]).optional(),
            "replaceJobId": t.string().optional(),
            "id": t.string().optional(),
            "tempFiles": t.array(t.string()).optional(),
            "projectId": t.string().optional(),
            "transformNameMapping": t.struct({"_": t.string().optional()}).optional(),
            "requestedState": t.string().optional(),
            "environment": t.proxy(renames["EnvironmentOut"]).optional(),
            "runtimeUpdatableParams": t.proxy(
                renames["RuntimeUpdatableParamsOut"]
            ).optional(),
            "type": t.string().optional(),
            "pipelineDescription": t.proxy(
                renames["PipelineDescriptionOut"]
            ).optional(),
            "currentState": t.string().optional(),
            "location": t.string().optional(),
            "steps": t.array(t.proxy(renames["StepOut"])).optional(),
            "replacedByJobId": t.string().optional(),
            "jobMetadata": t.proxy(renames["JobMetadataOut"]).optional(),
            "stepsLocation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
    types["LaunchTemplateParametersIn"] = t.struct(
        {
            "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "update": t.boolean().optional(),
            "jobName": t.string(),
            "transformNameMapping": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LaunchTemplateParametersIn"])
    types["LaunchTemplateParametersOut"] = t.struct(
        {
            "environment": t.proxy(renames["RuntimeEnvironmentOut"]).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "update": t.boolean().optional(),
            "jobName": t.string(),
            "transformNameMapping": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LaunchTemplateParametersOut"])
    types["JobExecutionDetailsIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "stages": t.array(t.proxy(renames["StageSummaryIn"])).optional(),
        }
    ).named(renames["JobExecutionDetailsIn"])
    types["JobExecutionDetailsOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "stages": t.array(t.proxy(renames["StageSummaryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobExecutionDetailsOut"])
    types["ShellTaskIn"] = t.struct(
        {"exitCode": t.integer().optional(), "command": t.string().optional()}
    ).named(renames["ShellTaskIn"])
    types["ShellTaskOut"] = t.struct(
        {
            "exitCode": t.integer().optional(),
            "command": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShellTaskOut"])
    types["AutoscalingSettingsIn"] = t.struct(
        {"algorithm": t.string().optional(), "maxNumWorkers": t.integer().optional()}
    ).named(renames["AutoscalingSettingsIn"])
    types["AutoscalingSettingsOut"] = t.struct(
        {
            "algorithm": t.string().optional(),
            "maxNumWorkers": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoscalingSettingsOut"])
    types["BigTableIODetailsIn"] = t.struct(
        {
            "instanceId": t.string().optional(),
            "tableId": t.string().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["BigTableIODetailsIn"])
    types["BigTableIODetailsOut"] = t.struct(
        {
            "instanceId": t.string().optional(),
            "tableId": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigTableIODetailsOut"])
    types["StateFamilyConfigIn"] = t.struct(
        {"isRead": t.boolean().optional(), "stateFamily": t.string().optional()}
    ).named(renames["StateFamilyConfigIn"])
    types["StateFamilyConfigOut"] = t.struct(
        {
            "isRead": t.boolean().optional(),
            "stateFamily": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StateFamilyConfigOut"])
    types["WorkerLifecycleEventIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "event": t.string().optional(),
            "containerStartTime": t.string().optional(),
        }
    ).named(renames["WorkerLifecycleEventIn"])
    types["WorkerLifecycleEventOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "event": t.string().optional(),
            "containerStartTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerLifecycleEventOut"])
    types["CustomSourceLocationIn"] = t.struct(
        {"stateful": t.boolean().optional()}
    ).named(renames["CustomSourceLocationIn"])
    types["CustomSourceLocationOut"] = t.struct(
        {
            "stateful": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomSourceLocationOut"])
    types["SourceIn"] = t.struct(
        {
            "baseSpecs": t.array(t.struct({"_": t.string().optional()})).optional(),
            "codec": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.proxy(renames["SourceMetadataIn"]).optional(),
            "doesNotNeedSplitting": t.boolean().optional(),
            "spec": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "baseSpecs": t.array(t.struct({"_": t.string().optional()})).optional(),
            "codec": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.proxy(renames["SourceMetadataOut"]).optional(),
            "doesNotNeedSplitting": t.boolean().optional(),
            "spec": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["WorkItemStatusIn"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["StatusIn"])).optional(),
            "completed": t.boolean().optional(),
            "dynamicSourceSplit": t.proxy(renames["DynamicSourceSplitIn"]).optional(),
            "sourceFork": t.proxy(renames["SourceForkIn"]).optional(),
            "metricUpdates": t.array(t.proxy(renames["MetricUpdateIn"])).optional(),
            "reportedProgress": t.proxy(
                renames["ApproximateReportedProgressIn"]
            ).optional(),
            "sourceOperationResponse": t.proxy(
                renames["SourceOperationResponseIn"]
            ).optional(),
            "workItemId": t.string().optional(),
            "totalThrottlerWaitTimeSeconds": t.number().optional(),
            "progress": t.proxy(renames["ApproximateProgressIn"]).optional(),
            "requestedLeaseDuration": t.string().optional(),
            "reportIndex": t.string().optional(),
            "stopPosition": t.proxy(renames["PositionIn"]).optional(),
            "counterUpdates": t.array(t.proxy(renames["CounterUpdateIn"])).optional(),
        }
    ).named(renames["WorkItemStatusIn"])
    types["WorkItemStatusOut"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["StatusOut"])).optional(),
            "completed": t.boolean().optional(),
            "dynamicSourceSplit": t.proxy(renames["DynamicSourceSplitOut"]).optional(),
            "sourceFork": t.proxy(renames["SourceForkOut"]).optional(),
            "metricUpdates": t.array(t.proxy(renames["MetricUpdateOut"])).optional(),
            "reportedProgress": t.proxy(
                renames["ApproximateReportedProgressOut"]
            ).optional(),
            "sourceOperationResponse": t.proxy(
                renames["SourceOperationResponseOut"]
            ).optional(),
            "workItemId": t.string().optional(),
            "totalThrottlerWaitTimeSeconds": t.number().optional(),
            "progress": t.proxy(renames["ApproximateProgressOut"]).optional(),
            "requestedLeaseDuration": t.string().optional(),
            "reportIndex": t.string().optional(),
            "stopPosition": t.proxy(renames["PositionOut"]).optional(),
            "counterUpdates": t.array(t.proxy(renames["CounterUpdateOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkItemStatusOut"])
    types["PackageIn"] = t.struct(
        {"name": t.string().optional(), "location": t.string().optional()}
    ).named(renames["PackageIn"])
    types["PackageOut"] = t.struct(
        {
            "name": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageOut"])
    types["ExecutionStageStateIn"] = t.struct(
        {
            "executionStageState": t.string().optional(),
            "executionStageName": t.string().optional(),
            "currentStateTime": t.string().optional(),
        }
    ).named(renames["ExecutionStageStateIn"])
    types["ExecutionStageStateOut"] = t.struct(
        {
            "executionStageState": t.string().optional(),
            "executionStageName": t.string().optional(),
            "currentStateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionStageStateOut"])
    types["StreamingConfigTaskIn"] = t.struct(
        {
            "userStepToStateFamilyNameMap": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "commitStreamChunkSizeBytes": t.string().optional(),
            "getDataStreamChunkSizeBytes": t.string().optional(),
            "windmillServiceEndpoint": t.string().optional(),
            "maxWorkItemCommitBytes": t.string().optional(),
            "streamingComputationConfigs": t.array(
                t.proxy(renames["StreamingComputationConfigIn"])
            ).optional(),
            "windmillServicePort": t.string().optional(),
        }
    ).named(renames["StreamingConfigTaskIn"])
    types["StreamingConfigTaskOut"] = t.struct(
        {
            "userStepToStateFamilyNameMap": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "commitStreamChunkSizeBytes": t.string().optional(),
            "getDataStreamChunkSizeBytes": t.string().optional(),
            "windmillServiceEndpoint": t.string().optional(),
            "maxWorkItemCommitBytes": t.string().optional(),
            "streamingComputationConfigs": t.array(
                t.proxy(renames["StreamingComputationConfigOut"])
            ).optional(),
            "windmillServicePort": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingConfigTaskOut"])
    types["InstructionInputIn"] = t.struct(
        {
            "outputNum": t.integer().optional(),
            "producerInstructionIndex": t.integer().optional(),
        }
    ).named(renames["InstructionInputIn"])
    types["InstructionInputOut"] = t.struct(
        {
            "outputNum": t.integer().optional(),
            "producerInstructionIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstructionInputOut"])
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
    types["WorkItemDetailsIn"] = t.struct(
        {
            "attemptId": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricUpdateIn"])).optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "taskId": t.string().optional(),
            "progress": t.proxy(renames["ProgressTimeseriesIn"]).optional(),
            "stragglerInfo": t.proxy(renames["StragglerInfoIn"]).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["WorkItemDetailsIn"])
    types["WorkItemDetailsOut"] = t.struct(
        {
            "attemptId": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricUpdateOut"])).optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "taskId": t.string().optional(),
            "progress": t.proxy(renames["ProgressTimeseriesOut"]).optional(),
            "stragglerInfo": t.proxy(renames["StragglerInfoOut"]).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkItemDetailsOut"])
    types["PartialGroupByKeyInstructionIn"] = t.struct(
        {
            "valueCombiningFn": t.struct({"_": t.string().optional()}).optional(),
            "originalCombineValuesStepName": t.string().optional(),
            "sideInputs": t.array(t.proxy(renames["SideInputInfoIn"])).optional(),
            "input": t.proxy(renames["InstructionInputIn"]).optional(),
            "inputElementCodec": t.struct({"_": t.string().optional()}).optional(),
            "originalCombineValuesInputStoreName": t.string().optional(),
        }
    ).named(renames["PartialGroupByKeyInstructionIn"])
    types["PartialGroupByKeyInstructionOut"] = t.struct(
        {
            "valueCombiningFn": t.struct({"_": t.string().optional()}).optional(),
            "originalCombineValuesStepName": t.string().optional(),
            "sideInputs": t.array(t.proxy(renames["SideInputInfoOut"])).optional(),
            "input": t.proxy(renames["InstructionInputOut"]).optional(),
            "inputElementCodec": t.struct({"_": t.string().optional()}).optional(),
            "originalCombineValuesInputStoreName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartialGroupByKeyInstructionOut"])
    types["WorkItemIn"] = t.struct(
        {
            "reportStatusInterval": t.string().optional(),
            "shellTask": t.proxy(renames["ShellTaskIn"]).optional(),
            "streamingConfigTask": t.proxy(renames["StreamingConfigTaskIn"]).optional(),
            "packages": t.array(t.proxy(renames["PackageIn"])).optional(),
            "leaseExpireTime": t.string().optional(),
            "mapTask": t.proxy(renames["MapTaskIn"]).optional(),
            "sourceOperationTask": t.proxy(
                renames["SourceOperationRequestIn"]
            ).optional(),
            "projectId": t.string().optional(),
            "jobId": t.string().optional(),
            "streamingSetupTask": t.proxy(renames["StreamingSetupTaskIn"]).optional(),
            "configuration": t.string().optional(),
            "seqMapTask": t.proxy(renames["SeqMapTaskIn"]).optional(),
            "streamingComputationTask": t.proxy(
                renames["StreamingComputationTaskIn"]
            ).optional(),
            "id": t.string().optional(),
            "initialReportIndex": t.string().optional(),
        }
    ).named(renames["WorkItemIn"])
    types["WorkItemOut"] = t.struct(
        {
            "reportStatusInterval": t.string().optional(),
            "shellTask": t.proxy(renames["ShellTaskOut"]).optional(),
            "streamingConfigTask": t.proxy(
                renames["StreamingConfigTaskOut"]
            ).optional(),
            "packages": t.array(t.proxy(renames["PackageOut"])).optional(),
            "leaseExpireTime": t.string().optional(),
            "mapTask": t.proxy(renames["MapTaskOut"]).optional(),
            "sourceOperationTask": t.proxy(
                renames["SourceOperationRequestOut"]
            ).optional(),
            "projectId": t.string().optional(),
            "jobId": t.string().optional(),
            "streamingSetupTask": t.proxy(renames["StreamingSetupTaskOut"]).optional(),
            "configuration": t.string().optional(),
            "seqMapTask": t.proxy(renames["SeqMapTaskOut"]).optional(),
            "streamingComputationTask": t.proxy(
                renames["StreamingComputationTaskOut"]
            ).optional(),
            "id": t.string().optional(),
            "initialReportIndex": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkItemOut"])
    types["LaunchFlexTemplateParameterIn"] = t.struct(
        {
            "launchOptions": t.struct({"_": t.string().optional()}).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "containerSpecGcsPath": t.string().optional(),
            "environment": t.proxy(
                renames["FlexTemplateRuntimeEnvironmentIn"]
            ).optional(),
            "update": t.boolean().optional(),
            "jobName": t.string(),
            "transformNameMappings": t.struct({"_": t.string().optional()}).optional(),
            "containerSpec": t.proxy(renames["ContainerSpecIn"]).optional(),
        }
    ).named(renames["LaunchFlexTemplateParameterIn"])
    types["LaunchFlexTemplateParameterOut"] = t.struct(
        {
            "launchOptions": t.struct({"_": t.string().optional()}).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "containerSpecGcsPath": t.string().optional(),
            "environment": t.proxy(
                renames["FlexTemplateRuntimeEnvironmentOut"]
            ).optional(),
            "update": t.boolean().optional(),
            "jobName": t.string(),
            "transformNameMappings": t.struct({"_": t.string().optional()}).optional(),
            "containerSpec": t.proxy(renames["ContainerSpecOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LaunchFlexTemplateParameterOut"])
    types["StreamingSetupTaskIn"] = t.struct(
        {
            "streamingComputationTopology": t.proxy(
                renames["TopologyConfigIn"]
            ).optional(),
            "receiveWorkPort": t.integer().optional(),
            "workerHarnessPort": t.integer().optional(),
            "snapshotConfig": t.proxy(
                renames["StreamingApplianceSnapshotConfigIn"]
            ).optional(),
            "drain": t.boolean().optional(),
        }
    ).named(renames["StreamingSetupTaskIn"])
    types["StreamingSetupTaskOut"] = t.struct(
        {
            "streamingComputationTopology": t.proxy(
                renames["TopologyConfigOut"]
            ).optional(),
            "receiveWorkPort": t.integer().optional(),
            "workerHarnessPort": t.integer().optional(),
            "snapshotConfig": t.proxy(
                renames["StreamingApplianceSnapshotConfigOut"]
            ).optional(),
            "drain": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingSetupTaskOut"])
    types["StageExecutionDetailsIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "workers": t.array(t.proxy(renames["WorkerDetailsIn"])).optional(),
        }
    ).named(renames["StageExecutionDetailsIn"])
    types["StageExecutionDetailsOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "workers": t.array(t.proxy(renames["WorkerDetailsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StageExecutionDetailsOut"])
    types["MemInfoIn"] = t.struct(
        {
            "totalGbMs": t.string().optional(),
            "timestamp": t.string().optional(),
            "currentLimitBytes": t.string().optional(),
            "currentOoms": t.string().optional(),
            "currentRssBytes": t.string().optional(),
        }
    ).named(renames["MemInfoIn"])
    types["MemInfoOut"] = t.struct(
        {
            "totalGbMs": t.string().optional(),
            "timestamp": t.string().optional(),
            "currentLimitBytes": t.string().optional(),
            "currentOoms": t.string().optional(),
            "currentRssBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemInfoOut"])
    types["StreamingStageLocationIn"] = t.struct(
        {"streamId": t.string().optional()}
    ).named(renames["StreamingStageLocationIn"])
    types["StreamingStageLocationOut"] = t.struct(
        {
            "streamId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingStageLocationOut"])
    types["JobMessageIn"] = t.struct(
        {
            "id": t.string().optional(),
            "messageText": t.string().optional(),
            "messageImportance": t.string().optional(),
            "time": t.string().optional(),
        }
    ).named(renames["JobMessageIn"])
    types["JobMessageOut"] = t.struct(
        {
            "id": t.string().optional(),
            "messageText": t.string().optional(),
            "messageImportance": t.string().optional(),
            "time": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobMessageOut"])
    types["ReportWorkItemStatusResponseIn"] = t.struct(
        {
            "workItemServiceStates": t.array(
                t.proxy(renames["WorkItemServiceStateIn"])
            ).optional(),
            "unifiedWorkerResponse": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ReportWorkItemStatusResponseIn"])
    types["ReportWorkItemStatusResponseOut"] = t.struct(
        {
            "workItemServiceStates": t.array(
                t.proxy(renames["WorkItemServiceStateOut"])
            ).optional(),
            "unifiedWorkerResponse": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportWorkItemStatusResponseOut"])
    types["TemplateMetadataIn"] = t.struct(
        {
            "description": t.string().optional(),
            "parameters": t.array(t.proxy(renames["ParameterMetadataIn"])).optional(),
            "name": t.string(),
        }
    ).named(renames["TemplateMetadataIn"])
    types["TemplateMetadataOut"] = t.struct(
        {
            "description": t.string().optional(),
            "parameters": t.array(t.proxy(renames["ParameterMetadataOut"])).optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TemplateMetadataOut"])
    types["JobExecutionStageInfoIn"] = t.struct(
        {"stepName": t.array(t.string()).optional()}
    ).named(renames["JobExecutionStageInfoIn"])
    types["JobExecutionStageInfoOut"] = t.struct(
        {
            "stepName": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobExecutionStageInfoOut"])
    types["CounterStructuredNameAndMetadataIn"] = t.struct(
        {
            "metadata": t.proxy(renames["CounterMetadataIn"]).optional(),
            "name": t.proxy(renames["CounterStructuredNameIn"]).optional(),
        }
    ).named(renames["CounterStructuredNameAndMetadataIn"])
    types["CounterStructuredNameAndMetadataOut"] = t.struct(
        {
            "metadata": t.proxy(renames["CounterMetadataOut"]).optional(),
            "name": t.proxy(renames["CounterStructuredNameOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CounterStructuredNameAndMetadataOut"])
    types["MetricStructuredNameIn"] = t.struct(
        {
            "name": t.string().optional(),
            "origin": t.string().optional(),
            "context": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["MetricStructuredNameIn"])
    types["MetricStructuredNameOut"] = t.struct(
        {
            "name": t.string().optional(),
            "origin": t.string().optional(),
            "context": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricStructuredNameOut"])
    types["SendWorkerMessagesResponseIn"] = t.struct(
        {
            "workerMessageResponses": t.array(
                t.proxy(renames["WorkerMessageResponseIn"])
            ).optional()
        }
    ).named(renames["SendWorkerMessagesResponseIn"])
    types["SendWorkerMessagesResponseOut"] = t.struct(
        {
            "workerMessageResponses": t.array(
                t.proxy(renames["WorkerMessageResponseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SendWorkerMessagesResponseOut"])
    types["IntegerGaugeIn"] = t.struct(
        {
            "timestamp": t.string().optional(),
            "value": t.proxy(renames["SplitInt64In"]).optional(),
        }
    ).named(renames["IntegerGaugeIn"])
    types["IntegerGaugeOut"] = t.struct(
        {
            "timestamp": t.string().optional(),
            "value": t.proxy(renames["SplitInt64Out"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerGaugeOut"])
    types["HistogramIn"] = t.struct(
        {
            "bucketCounts": t.array(t.string()).optional(),
            "firstBucketOffset": t.integer().optional(),
        }
    ).named(renames["HistogramIn"])
    types["HistogramOut"] = t.struct(
        {
            "bucketCounts": t.array(t.string()).optional(),
            "firstBucketOffset": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistogramOut"])
    types["SdkHarnessContainerImageIn"] = t.struct(
        {
            "capabilities": t.array(t.string()).optional(),
            "containerImage": t.string().optional(),
            "environmentId": t.string().optional(),
            "useSingleCorePerContainer": t.boolean().optional(),
        }
    ).named(renames["SdkHarnessContainerImageIn"])
    types["SdkHarnessContainerImageOut"] = t.struct(
        {
            "capabilities": t.array(t.string()).optional(),
            "containerImage": t.string().optional(),
            "environmentId": t.string().optional(),
            "useSingleCorePerContainer": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SdkHarnessContainerImageOut"])
    types["RuntimeUpdatableParamsIn"] = t.struct(
        {
            "minNumWorkers": t.integer().optional(),
            "maxNumWorkers": t.integer().optional(),
        }
    ).named(renames["RuntimeUpdatableParamsIn"])
    types["RuntimeUpdatableParamsOut"] = t.struct(
        {
            "minNumWorkers": t.integer().optional(),
            "maxNumWorkers": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeUpdatableParamsOut"])
    types["SendDebugCaptureRequestIn"] = t.struct(
        {
            "dataFormat": t.string().optional(),
            "location": t.string().optional(),
            "workerId": t.string().optional(),
            "data": t.string().optional(),
            "componentId": t.string().optional(),
        }
    ).named(renames["SendDebugCaptureRequestIn"])
    types["SendDebugCaptureRequestOut"] = t.struct(
        {
            "dataFormat": t.string().optional(),
            "location": t.string().optional(),
            "workerId": t.string().optional(),
            "data": t.string().optional(),
            "componentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SendDebugCaptureRequestOut"])
    types["HotKeyInfoIn"] = t.struct(
        {
            "hotKeyAge": t.string().optional(),
            "key": t.string().optional(),
            "keyTruncated": t.boolean().optional(),
        }
    ).named(renames["HotKeyInfoIn"])
    types["HotKeyInfoOut"] = t.struct(
        {
            "hotKeyAge": t.string().optional(),
            "key": t.string().optional(),
            "keyTruncated": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HotKeyInfoOut"])
    types["AutoscalingEventIn"] = t.struct(
        {
            "description": t.proxy(renames["StructuredMessageIn"]).optional(),
            "eventType": t.string().optional(),
            "currentNumWorkers": t.string().optional(),
            "targetNumWorkers": t.string().optional(),
            "workerPool": t.string().optional(),
            "time": t.string().optional(),
        }
    ).named(renames["AutoscalingEventIn"])
    types["AutoscalingEventOut"] = t.struct(
        {
            "description": t.proxy(renames["StructuredMessageOut"]).optional(),
            "eventType": t.string().optional(),
            "currentNumWorkers": t.string().optional(),
            "targetNumWorkers": t.string().optional(),
            "workerPool": t.string().optional(),
            "time": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoscalingEventOut"])
    types["IntegerMeanIn"] = t.struct(
        {
            "count": t.proxy(renames["SplitInt64In"]).optional(),
            "sum": t.proxy(renames["SplitInt64In"]).optional(),
        }
    ).named(renames["IntegerMeanIn"])
    types["IntegerMeanOut"] = t.struct(
        {
            "count": t.proxy(renames["SplitInt64Out"]).optional(),
            "sum": t.proxy(renames["SplitInt64Out"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerMeanOut"])
    types["StageSourceIn"] = t.struct(
        {
            "userName": t.string().optional(),
            "originalTransformOrCollection": t.string().optional(),
            "name": t.string().optional(),
            "sizeBytes": t.string().optional(),
        }
    ).named(renames["StageSourceIn"])
    types["StageSourceOut"] = t.struct(
        {
            "userName": t.string().optional(),
            "originalTransformOrCollection": t.string().optional(),
            "name": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StageSourceOut"])
    types["StreamingApplianceSnapshotConfigIn"] = t.struct(
        {
            "snapshotId": t.string().optional(),
            "importStateEndpoint": t.string().optional(),
        }
    ).named(renames["StreamingApplianceSnapshotConfigIn"])
    types["StreamingApplianceSnapshotConfigOut"] = t.struct(
        {
            "snapshotId": t.string().optional(),
            "importStateEndpoint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingApplianceSnapshotConfigOut"])
    types["DisplayDataIn"] = t.struct(
        {
            "label": t.string().optional(),
            "shortStrValue": t.string().optional(),
            "namespace": t.string().optional(),
            "durationValue": t.string().optional(),
            "javaClassValue": t.string().optional(),
            "key": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "url": t.string().optional(),
            "floatValue": t.number().optional(),
            "strValue": t.string().optional(),
            "timestampValue": t.string().optional(),
            "int64Value": t.string().optional(),
        }
    ).named(renames["DisplayDataIn"])
    types["DisplayDataOut"] = t.struct(
        {
            "label": t.string().optional(),
            "shortStrValue": t.string().optional(),
            "namespace": t.string().optional(),
            "durationValue": t.string().optional(),
            "javaClassValue": t.string().optional(),
            "key": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "url": t.string().optional(),
            "floatValue": t.number().optional(),
            "strValue": t.string().optional(),
            "timestampValue": t.string().optional(),
            "int64Value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisplayDataOut"])
    types["StreamingSideInputLocationIn"] = t.struct(
        {"tag": t.string().optional(), "stateFamily": t.string().optional()}
    ).named(renames["StreamingSideInputLocationIn"])
    types["StreamingSideInputLocationOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "stateFamily": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingSideInputLocationOut"])
    types["StragglerIn"] = t.struct(
        {
            "batchStraggler": t.proxy(renames["StragglerInfoIn"]).optional(),
            "streamingStraggler": t.proxy(
                renames["StreamingStragglerInfoIn"]
            ).optional(),
        }
    ).named(renames["StragglerIn"])
    types["StragglerOut"] = t.struct(
        {
            "batchStraggler": t.proxy(renames["StragglerInfoOut"]).optional(),
            "streamingStraggler": t.proxy(
                renames["StreamingStragglerInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StragglerOut"])
    types["DynamicSourceSplitIn"] = t.struct(
        {
            "primary": t.proxy(renames["DerivedSourceIn"]).optional(),
            "residual": t.proxy(renames["DerivedSourceIn"]).optional(),
        }
    ).named(renames["DynamicSourceSplitIn"])
    types["DynamicSourceSplitOut"] = t.struct(
        {
            "primary": t.proxy(renames["DerivedSourceOut"]).optional(),
            "residual": t.proxy(renames["DerivedSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicSourceSplitOut"])
    types["StreamingComputationTaskIn"] = t.struct(
        {
            "computationRanges": t.array(
                t.proxy(renames["StreamingComputationRangesIn"])
            ).optional(),
            "dataDisks": t.array(t.proxy(renames["MountedDataDiskIn"])).optional(),
            "taskType": t.string().optional(),
        }
    ).named(renames["StreamingComputationTaskIn"])
    types["StreamingComputationTaskOut"] = t.struct(
        {
            "computationRanges": t.array(
                t.proxy(renames["StreamingComputationRangesOut"])
            ).optional(),
            "dataDisks": t.array(t.proxy(renames["MountedDataDiskOut"])).optional(),
            "taskType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingComputationTaskOut"])
    types["WorkerHealthReportResponseIn"] = t.struct(
        {"reportInterval": t.string().optional()}
    ).named(renames["WorkerHealthReportResponseIn"])
    types["WorkerHealthReportResponseOut"] = t.struct(
        {
            "reportInterval": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerHealthReportResponseOut"])
    types["SourceGetMetadataRequestIn"] = t.struct(
        {"source": t.proxy(renames["SourceIn"]).optional()}
    ).named(renames["SourceGetMetadataRequestIn"])
    types["SourceGetMetadataRequestOut"] = t.struct(
        {
            "source": t.proxy(renames["SourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceGetMetadataRequestOut"])
    types["InstructionOutputIn"] = t.struct(
        {
            "onlyCountValueBytes": t.boolean().optional(),
            "codec": t.struct({"_": t.string().optional()}).optional(),
            "originalName": t.string().optional(),
            "systemName": t.string().optional(),
            "name": t.string().optional(),
            "onlyCountKeyBytes": t.boolean().optional(),
        }
    ).named(renames["InstructionOutputIn"])
    types["InstructionOutputOut"] = t.struct(
        {
            "onlyCountValueBytes": t.boolean().optional(),
            "codec": t.struct({"_": t.string().optional()}).optional(),
            "originalName": t.string().optional(),
            "systemName": t.string().optional(),
            "name": t.string().optional(),
            "onlyCountKeyBytes": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstructionOutputOut"])
    types["PointIn"] = t.struct(
        {"time": t.string().optional(), "value": t.number().optional()}
    ).named(renames["PointIn"])
    types["PointOut"] = t.struct(
        {
            "time": t.string().optional(),
            "value": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PointOut"])
    types["StreamingComputationRangesIn"] = t.struct(
        {
            "rangeAssignments": t.array(
                t.proxy(renames["KeyRangeDataDiskAssignmentIn"])
            ).optional(),
            "computationId": t.string().optional(),
        }
    ).named(renames["StreamingComputationRangesIn"])
    types["StreamingComputationRangesOut"] = t.struct(
        {
            "rangeAssignments": t.array(
                t.proxy(renames["KeyRangeDataDiskAssignmentOut"])
            ).optional(),
            "computationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingComputationRangesOut"])
    types["LeaseWorkItemResponseIn"] = t.struct(
        {
            "workItems": t.array(t.proxy(renames["WorkItemIn"])).optional(),
            "unifiedWorkerResponse": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LeaseWorkItemResponseIn"])
    types["LeaseWorkItemResponseOut"] = t.struct(
        {
            "workItems": t.array(t.proxy(renames["WorkItemOut"])).optional(),
            "unifiedWorkerResponse": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LeaseWorkItemResponseOut"])
    types["SourceForkIn"] = t.struct(
        {
            "primary": t.proxy(renames["SourceSplitShardIn"]).optional(),
            "residualSource": t.proxy(renames["DerivedSourceIn"]).optional(),
            "primarySource": t.proxy(renames["DerivedSourceIn"]).optional(),
            "residual": t.proxy(renames["SourceSplitShardIn"]).optional(),
        }
    ).named(renames["SourceForkIn"])
    types["SourceForkOut"] = t.struct(
        {
            "primary": t.proxy(renames["SourceSplitShardOut"]).optional(),
            "residualSource": t.proxy(renames["DerivedSourceOut"]).optional(),
            "primarySource": t.proxy(renames["DerivedSourceOut"]).optional(),
            "residual": t.proxy(renames["SourceSplitShardOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceForkOut"])
    types["SDKInfoIn"] = t.struct(
        {"version": t.string().optional(), "language": t.string()}
    ).named(renames["SDKInfoIn"])
    types["SDKInfoOut"] = t.struct(
        {
            "version": t.string().optional(),
            "language": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SDKInfoOut"])
    types["GetDebugConfigRequestIn"] = t.struct(
        {
            "workerId": t.string().optional(),
            "componentId": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["GetDebugConfigRequestIn"])
    types["GetDebugConfigRequestOut"] = t.struct(
        {
            "workerId": t.string().optional(),
            "componentId": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetDebugConfigRequestOut"])
    types["FileIODetailsIn"] = t.struct({"filePattern": t.string().optional()}).named(
        renames["FileIODetailsIn"]
    )
    types["FileIODetailsOut"] = t.struct(
        {
            "filePattern": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileIODetailsOut"])
    types["WorkerPoolIn"] = t.struct(
        {
            "dataDisks": t.array(t.proxy(renames["DiskIn"])).optional(),
            "defaultPackageSet": t.string().optional(),
            "zone": t.string().optional(),
            "autoscalingSettings": t.proxy(renames["AutoscalingSettingsIn"]).optional(),
            "onHostMaintenance": t.string().optional(),
            "numThreadsPerWorker": t.integer().optional(),
            "workerHarnessContainerImage": t.string(),
            "packages": t.array(t.proxy(renames["PackageIn"])).optional(),
            "ipConfiguration": t.string().optional(),
            "poolArgs": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "sdkHarnessContainerImages": t.array(
                t.proxy(renames["SdkHarnessContainerImageIn"])
            ).optional(),
            "network": t.string().optional(),
            "numWorkers": t.integer().optional(),
            "diskSourceImage": t.string().optional(),
            "diskType": t.string().optional(),
            "machineType": t.string().optional(),
            "teardownPolicy": t.string().optional(),
            "taskrunnerSettings": t.proxy(renames["TaskRunnerSettingsIn"]).optional(),
            "diskSizeGb": t.integer().optional(),
            "subnetwork": t.string().optional(),
        }
    ).named(renames["WorkerPoolIn"])
    types["WorkerPoolOut"] = t.struct(
        {
            "dataDisks": t.array(t.proxy(renames["DiskOut"])).optional(),
            "defaultPackageSet": t.string().optional(),
            "zone": t.string().optional(),
            "autoscalingSettings": t.proxy(
                renames["AutoscalingSettingsOut"]
            ).optional(),
            "onHostMaintenance": t.string().optional(),
            "numThreadsPerWorker": t.integer().optional(),
            "workerHarnessContainerImage": t.string(),
            "packages": t.array(t.proxy(renames["PackageOut"])).optional(),
            "ipConfiguration": t.string().optional(),
            "poolArgs": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "sdkHarnessContainerImages": t.array(
                t.proxy(renames["SdkHarnessContainerImageOut"])
            ).optional(),
            "network": t.string().optional(),
            "numWorkers": t.integer().optional(),
            "diskSourceImage": t.string().optional(),
            "diskType": t.string().optional(),
            "machineType": t.string().optional(),
            "teardownPolicy": t.string().optional(),
            "taskrunnerSettings": t.proxy(renames["TaskRunnerSettingsOut"]).optional(),
            "diskSizeGb": t.integer().optional(),
            "subnetwork": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerPoolOut"])
    types["SourceMetadataIn"] = t.struct(
        {
            "infinite": t.boolean().optional(),
            "estimatedSizeBytes": t.string().optional(),
            "producesSortedKeys": t.boolean().optional(),
        }
    ).named(renames["SourceMetadataIn"])
    types["SourceMetadataOut"] = t.struct(
        {
            "infinite": t.boolean().optional(),
            "estimatedSizeBytes": t.string().optional(),
            "producesSortedKeys": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceMetadataOut"])
    types["RuntimeEnvironmentIn"] = t.struct(
        {
            "enableStreamingEngine": t.boolean().optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "machineType": t.string().optional(),
            "workerRegion": t.string(),
            "workerZone": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "maxWorkers": t.integer().optional(),
            "tempLocation": t.string(),
            "zone": t.string().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "subnetwork": t.string().optional(),
            "numWorkers": t.integer().optional(),
            "ipConfiguration": t.string().optional(),
            "bypassTempDirValidation": t.boolean().optional(),
            "network": t.string().optional(),
        }
    ).named(renames["RuntimeEnvironmentIn"])
    types["RuntimeEnvironmentOut"] = t.struct(
        {
            "enableStreamingEngine": t.boolean().optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "machineType": t.string().optional(),
            "workerRegion": t.string(),
            "workerZone": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "maxWorkers": t.integer().optional(),
            "tempLocation": t.string(),
            "zone": t.string().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "subnetwork": t.string().optional(),
            "numWorkers": t.integer().optional(),
            "ipConfiguration": t.string().optional(),
            "bypassTempDirValidation": t.boolean().optional(),
            "network": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeEnvironmentOut"])
    types["CounterUpdateIn"] = t.struct(
        {
            "floatingPointMean": t.proxy(renames["FloatingPointMeanIn"]).optional(),
            "boolean": t.boolean().optional(),
            "integerMean": t.proxy(renames["IntegerMeanIn"]).optional(),
            "shortId": t.string().optional(),
            "distribution": t.proxy(renames["DistributionUpdateIn"]).optional(),
            "stringList": t.proxy(renames["StringListIn"]).optional(),
            "cumulative": t.boolean().optional(),
            "floatingPoint": t.number().optional(),
            "internal": t.struct({"_": t.string().optional()}).optional(),
            "integerGauge": t.proxy(renames["IntegerGaugeIn"]).optional(),
            "nameAndKind": t.proxy(renames["NameAndKindIn"]).optional(),
            "integerList": t.proxy(renames["IntegerListIn"]).optional(),
            "integer": t.proxy(renames["SplitInt64In"]).optional(),
            "floatingPointList": t.proxy(renames["FloatingPointListIn"]).optional(),
            "structuredNameAndMetadata": t.proxy(
                renames["CounterStructuredNameAndMetadataIn"]
            ).optional(),
        }
    ).named(renames["CounterUpdateIn"])
    types["CounterUpdateOut"] = t.struct(
        {
            "floatingPointMean": t.proxy(renames["FloatingPointMeanOut"]).optional(),
            "boolean": t.boolean().optional(),
            "integerMean": t.proxy(renames["IntegerMeanOut"]).optional(),
            "shortId": t.string().optional(),
            "distribution": t.proxy(renames["DistributionUpdateOut"]).optional(),
            "stringList": t.proxy(renames["StringListOut"]).optional(),
            "cumulative": t.boolean().optional(),
            "floatingPoint": t.number().optional(),
            "internal": t.struct({"_": t.string().optional()}).optional(),
            "integerGauge": t.proxy(renames["IntegerGaugeOut"]).optional(),
            "nameAndKind": t.proxy(renames["NameAndKindOut"]).optional(),
            "integerList": t.proxy(renames["IntegerListOut"]).optional(),
            "integer": t.proxy(renames["SplitInt64Out"]).optional(),
            "floatingPointList": t.proxy(renames["FloatingPointListOut"]).optional(),
            "structuredNameAndMetadata": t.proxy(
                renames["CounterStructuredNameAndMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CounterUpdateOut"])
    types["WorkerDetailsIn"] = t.struct(
        {
            "workItems": t.array(t.proxy(renames["WorkItemDetailsIn"])).optional(),
            "workerName": t.string().optional(),
        }
    ).named(renames["WorkerDetailsIn"])
    types["WorkerDetailsOut"] = t.struct(
        {
            "workItems": t.array(t.proxy(renames["WorkItemDetailsOut"])).optional(),
            "workerName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerDetailsOut"])
    types["SeqMapTaskIn"] = t.struct(
        {
            "inputs": t.array(t.proxy(renames["SideInputInfoIn"])).optional(),
            "stageName": t.string().optional(),
            "name": t.string().optional(),
            "systemName": t.string().optional(),
            "userFn": t.struct({"_": t.string().optional()}).optional(),
            "outputInfos": t.array(
                t.proxy(renames["SeqMapTaskOutputInfoIn"])
            ).optional(),
        }
    ).named(renames["SeqMapTaskIn"])
    types["SeqMapTaskOut"] = t.struct(
        {
            "inputs": t.array(t.proxy(renames["SideInputInfoOut"])).optional(),
            "stageName": t.string().optional(),
            "name": t.string().optional(),
            "systemName": t.string().optional(),
            "userFn": t.struct({"_": t.string().optional()}).optional(),
            "outputInfos": t.array(
                t.proxy(renames["SeqMapTaskOutputInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SeqMapTaskOut"])
    types["WorkItemServiceStateIn"] = t.struct(
        {
            "harnessData": t.struct({"_": t.string().optional()}).optional(),
            "metricShortId": t.array(t.proxy(renames["MetricShortIdIn"])).optional(),
            "leaseExpireTime": t.string().optional(),
            "nextReportIndex": t.string().optional(),
            "hotKeyDetection": t.proxy(renames["HotKeyDetectionIn"]).optional(),
            "suggestedStopPoint": t.proxy(renames["ApproximateProgressIn"]).optional(),
            "completeWorkStatus": t.proxy(renames["StatusIn"]).optional(),
            "suggestedStopPosition": t.proxy(renames["PositionIn"]).optional(),
            "splitRequest": t.proxy(renames["ApproximateSplitRequestIn"]).optional(),
            "reportStatusInterval": t.string().optional(),
        }
    ).named(renames["WorkItemServiceStateIn"])
    types["WorkItemServiceStateOut"] = t.struct(
        {
            "harnessData": t.struct({"_": t.string().optional()}).optional(),
            "metricShortId": t.array(t.proxy(renames["MetricShortIdOut"])).optional(),
            "leaseExpireTime": t.string().optional(),
            "nextReportIndex": t.string().optional(),
            "hotKeyDetection": t.proxy(renames["HotKeyDetectionOut"]).optional(),
            "suggestedStopPoint": t.proxy(renames["ApproximateProgressOut"]).optional(),
            "completeWorkStatus": t.proxy(renames["StatusOut"]).optional(),
            "suggestedStopPosition": t.proxy(renames["PositionOut"]).optional(),
            "splitRequest": t.proxy(renames["ApproximateSplitRequestOut"]).optional(),
            "reportStatusInterval": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkItemServiceStateOut"])
    types["ComponentSourceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "originalTransformOrCollection": t.string().optional(),
            "userName": t.string().optional(),
        }
    ).named(renames["ComponentSourceIn"])
    types["ComponentSourceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "originalTransformOrCollection": t.string().optional(),
            "userName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComponentSourceOut"])
    types["WorkerSettingsIn"] = t.struct(
        {
            "shuffleServicePath": t.string().optional(),
            "servicePath": t.string().optional(),
            "reportingEnabled": t.boolean().optional(),
            "workerId": t.string().optional(),
            "baseUrl": t.string().optional(),
            "tempStoragePrefix": t.string().optional(),
        }
    ).named(renames["WorkerSettingsIn"])
    types["WorkerSettingsOut"] = t.struct(
        {
            "shuffleServicePath": t.string().optional(),
            "servicePath": t.string().optional(),
            "reportingEnabled": t.boolean().optional(),
            "workerId": t.string().optional(),
            "baseUrl": t.string().optional(),
            "tempStoragePrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerSettingsOut"])
    types["KeyRangeDataDiskAssignmentIn"] = t.struct(
        {
            "end": t.string().optional(),
            "dataDisk": t.string().optional(),
            "start": t.string().optional(),
        }
    ).named(renames["KeyRangeDataDiskAssignmentIn"])
    types["KeyRangeDataDiskAssignmentOut"] = t.struct(
        {
            "end": t.string().optional(),
            "dataDisk": t.string().optional(),
            "start": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyRangeDataDiskAssignmentOut"])
    types["StragglerSummaryIn"] = t.struct(
        {
            "stragglerCauseCount": t.struct({"_": t.string().optional()}).optional(),
            "totalStragglerCount": t.string().optional(),
            "recentStragglers": t.array(t.proxy(renames["StragglerIn"])).optional(),
        }
    ).named(renames["StragglerSummaryIn"])
    types["StragglerSummaryOut"] = t.struct(
        {
            "stragglerCauseCount": t.struct({"_": t.string().optional()}).optional(),
            "totalStragglerCount": t.string().optional(),
            "recentStragglers": t.array(t.proxy(renames["StragglerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StragglerSummaryOut"])
    types["HotKeyDebuggingInfoIn"] = t.struct(
        {"detectedHotKeys": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["HotKeyDebuggingInfoIn"])
    types["HotKeyDebuggingInfoOut"] = t.struct(
        {
            "detectedHotKeys": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HotKeyDebuggingInfoOut"])
    types["ProgressTimeseriesIn"] = t.struct(
        {
            "currentProgress": t.number().optional(),
            "dataPoints": t.array(t.proxy(renames["PointIn"])).optional(),
        }
    ).named(renames["ProgressTimeseriesIn"])
    types["ProgressTimeseriesOut"] = t.struct(
        {
            "currentProgress": t.number().optional(),
            "dataPoints": t.array(t.proxy(renames["PointOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProgressTimeseriesOut"])
    types["StreamingComputationConfigIn"] = t.struct(
        {
            "transformUserNameToStateFamily": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "instructions": t.array(
                t.proxy(renames["ParallelInstructionIn"])
            ).optional(),
            "stageName": t.string().optional(),
            "computationId": t.string().optional(),
            "systemName": t.string().optional(),
        }
    ).named(renames["StreamingComputationConfigIn"])
    types["StreamingComputationConfigOut"] = t.struct(
        {
            "transformUserNameToStateFamily": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "instructions": t.array(
                t.proxy(renames["ParallelInstructionOut"])
            ).optional(),
            "stageName": t.string().optional(),
            "computationId": t.string().optional(),
            "systemName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingComputationConfigOut"])
    types["DebugOptionsIn"] = t.struct(
        {"enableHotKeyLogging": t.boolean().optional()}
    ).named(renames["DebugOptionsIn"])
    types["DebugOptionsOut"] = t.struct(
        {
            "enableHotKeyLogging": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DebugOptionsOut"])
    types["RuntimeMetadataIn"] = t.struct(
        {
            "sdkInfo": t.proxy(renames["SDKInfoIn"]).optional(),
            "parameters": t.array(t.proxy(renames["ParameterMetadataIn"])).optional(),
        }
    ).named(renames["RuntimeMetadataIn"])
    types["RuntimeMetadataOut"] = t.struct(
        {
            "sdkInfo": t.proxy(renames["SDKInfoOut"]).optional(),
            "parameters": t.array(t.proxy(renames["ParameterMetadataOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeMetadataOut"])
    types["JobMetadataIn"] = t.struct(
        {
            "bigTableDetails": t.array(
                t.proxy(renames["BigTableIODetailsIn"])
            ).optional(),
            "fileDetails": t.array(t.proxy(renames["FileIODetailsIn"])).optional(),
            "pubsubDetails": t.array(t.proxy(renames["PubSubIODetailsIn"])).optional(),
            "bigqueryDetails": t.array(
                t.proxy(renames["BigQueryIODetailsIn"])
            ).optional(),
            "sdkVersion": t.proxy(renames["SdkVersionIn"]).optional(),
            "spannerDetails": t.array(
                t.proxy(renames["SpannerIODetailsIn"])
            ).optional(),
            "userDisplayProperties": t.struct({"_": t.string().optional()}).optional(),
            "datastoreDetails": t.array(
                t.proxy(renames["DatastoreIODetailsIn"])
            ).optional(),
        }
    ).named(renames["JobMetadataIn"])
    types["JobMetadataOut"] = t.struct(
        {
            "bigTableDetails": t.array(
                t.proxy(renames["BigTableIODetailsOut"])
            ).optional(),
            "fileDetails": t.array(t.proxy(renames["FileIODetailsOut"])).optional(),
            "pubsubDetails": t.array(t.proxy(renames["PubSubIODetailsOut"])).optional(),
            "bigqueryDetails": t.array(
                t.proxy(renames["BigQueryIODetailsOut"])
            ).optional(),
            "sdkVersion": t.proxy(renames["SdkVersionOut"]).optional(),
            "spannerDetails": t.array(
                t.proxy(renames["SpannerIODetailsOut"])
            ).optional(),
            "userDisplayProperties": t.struct({"_": t.string().optional()}).optional(),
            "datastoreDetails": t.array(
                t.proxy(renames["DatastoreIODetailsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobMetadataOut"])
    types["SourceGetMetadataResponseIn"] = t.struct(
        {"metadata": t.proxy(renames["SourceMetadataIn"]).optional()}
    ).named(renames["SourceGetMetadataResponseIn"])
    types["SourceGetMetadataResponseOut"] = t.struct(
        {
            "metadata": t.proxy(renames["SourceMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceGetMetadataResponseOut"])
    types["WorkerThreadScalingReportResponseIn"] = t.struct(
        {"recommendedThreadCount": t.integer().optional()}
    ).named(renames["WorkerThreadScalingReportResponseIn"])
    types["WorkerThreadScalingReportResponseOut"] = t.struct(
        {
            "recommendedThreadCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerThreadScalingReportResponseOut"])
    types["PubSubIODetailsIn"] = t.struct(
        {"topic": t.string().optional(), "subscription": t.string().optional()}
    ).named(renames["PubSubIODetailsIn"])
    types["PubSubIODetailsOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "subscription": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubSubIODetailsOut"])
    types["ParDoInstructionIn"] = t.struct(
        {
            "multiOutputInfos": t.array(
                t.proxy(renames["MultiOutputInfoIn"])
            ).optional(),
            "userFn": t.struct({"_": t.string().optional()}).optional(),
            "input": t.proxy(renames["InstructionInputIn"]).optional(),
            "numOutputs": t.integer().optional(),
            "sideInputs": t.array(t.proxy(renames["SideInputInfoIn"])).optional(),
        }
    ).named(renames["ParDoInstructionIn"])
    types["ParDoInstructionOut"] = t.struct(
        {
            "multiOutputInfos": t.array(
                t.proxy(renames["MultiOutputInfoOut"])
            ).optional(),
            "userFn": t.struct({"_": t.string().optional()}).optional(),
            "input": t.proxy(renames["InstructionInputOut"]).optional(),
            "numOutputs": t.integer().optional(),
            "sideInputs": t.array(t.proxy(renames["SideInputInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParDoInstructionOut"])

    functions = {}
    functions["projectsWorkerMessages"] = dataflow.delete(
        "v1b3/projects/{projectId}/snapshots",
        t.struct(
            {
                "projectId": t.string().optional(),
                "snapshotId": t.string().optional(),
                "location": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeleteSnapshotResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDeleteSnapshots"] = dataflow.delete(
        "v1b3/projects/{projectId}/snapshots",
        t.struct(
            {
                "projectId": t.string().optional(),
                "snapshotId": t.string().optional(),
                "location": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeleteSnapshotResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnapshotsList"] = dataflow.get(
        "v1b3/projects/{projectId}/snapshots/{snapshotId}",
        t.struct(
            {
                "snapshotId": t.string().optional(),
                "projectId": t.string().optional(),
                "location": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnapshotsGet"] = dataflow.get(
        "v1b3/projects/{projectId}/snapshots/{snapshotId}",
        t.struct(
            {
                "snapshotId": t.string().optional(),
                "projectId": t.string().optional(),
                "location": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTemplatesGet"] = dataflow.post(
        "v1b3/projects/{projectId}/templates:launch",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "gcsPath": t.string().optional(),
                "dynamicTemplate.stagingLocation": t.string().optional(),
                "location": t.string().optional(),
                "projectId": t.string(),
                "dynamicTemplate.gcsPath": t.string().optional(),
                "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "update": t.boolean().optional(),
                "jobName": t.string(),
                "transformNameMapping": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LaunchTemplateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTemplatesCreate"] = dataflow.post(
        "v1b3/projects/{projectId}/templates:launch",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "gcsPath": t.string().optional(),
                "dynamicTemplate.stagingLocation": t.string().optional(),
                "location": t.string().optional(),
                "projectId": t.string(),
                "dynamicTemplate.gcsPath": t.string().optional(),
                "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "update": t.boolean().optional(),
                "jobName": t.string(),
                "transformNameMapping": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LaunchTemplateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTemplatesLaunch"] = dataflow.post(
        "v1b3/projects/{projectId}/templates:launch",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "gcsPath": t.string().optional(),
                "dynamicTemplate.stagingLocation": t.string().optional(),
                "location": t.string().optional(),
                "projectId": t.string(),
                "dynamicTemplate.gcsPath": t.string().optional(),
                "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "update": t.boolean().optional(),
                "jobName": t.string(),
                "transformNameMapping": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LaunchTemplateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsCreate"] = dataflow.get(
        "v1b3/projects/{projectId}/jobs/{jobId}/metrics",
        t.struct(
            {
                "jobId": t.string().optional(),
                "startTime": t.string().optional(),
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobMetricsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsList"] = dataflow.get(
        "v1b3/projects/{projectId}/jobs/{jobId}/metrics",
        t.struct(
            {
                "jobId": t.string().optional(),
                "startTime": t.string().optional(),
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobMetricsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsAggregated"] = dataflow.get(
        "v1b3/projects/{projectId}/jobs/{jobId}/metrics",
        t.struct(
            {
                "jobId": t.string().optional(),
                "startTime": t.string().optional(),
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobMetricsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsUpdate"] = dataflow.get(
        "v1b3/projects/{projectId}/jobs/{jobId}/metrics",
        t.struct(
            {
                "jobId": t.string().optional(),
                "startTime": t.string().optional(),
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobMetricsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsGet"] = dataflow.get(
        "v1b3/projects/{projectId}/jobs/{jobId}/metrics",
        t.struct(
            {
                "jobId": t.string().optional(),
                "startTime": t.string().optional(),
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobMetricsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsSnapshot"] = dataflow.get(
        "v1b3/projects/{projectId}/jobs/{jobId}/metrics",
        t.struct(
            {
                "jobId": t.string().optional(),
                "startTime": t.string().optional(),
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobMetricsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsGetMetrics"] = dataflow.get(
        "v1b3/projects/{projectId}/jobs/{jobId}/metrics",
        t.struct(
            {
                "jobId": t.string().optional(),
                "startTime": t.string().optional(),
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobMetricsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsWorkItemsLease"] = dataflow.post(
        "v1b3/projects/{projectId}/jobs/{jobId}/workItems:reportStatus",
        t.struct(
            {
                "jobId": t.string().optional(),
                "projectId": t.string().optional(),
                "unifiedWorkerRequest": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "workItemStatuses": t.array(
                    t.proxy(renames["WorkItemStatusIn"])
                ).optional(),
                "currentWorkerTime": t.string().optional(),
                "workerId": t.string().optional(),
                "location": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportWorkItemStatusResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsWorkItemsReportStatus"] = dataflow.post(
        "v1b3/projects/{projectId}/jobs/{jobId}/workItems:reportStatus",
        t.struct(
            {
                "jobId": t.string().optional(),
                "projectId": t.string().optional(),
                "unifiedWorkerRequest": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "workItemStatuses": t.array(
                    t.proxy(renames["WorkItemStatusIn"])
                ).optional(),
                "currentWorkerTime": t.string().optional(),
                "workerId": t.string().optional(),
                "location": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportWorkItemStatusResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsDebugSendCapture"] = dataflow.post(
        "v1b3/projects/{projectId}/jobs/{jobId}/debug/getConfig",
        t.struct(
            {
                "jobId": t.string().optional(),
                "projectId": t.string().optional(),
                "workerId": t.string().optional(),
                "componentId": t.string().optional(),
                "location": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetDebugConfigResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsDebugGetConfig"] = dataflow.post(
        "v1b3/projects/{projectId}/jobs/{jobId}/debug/getConfig",
        t.struct(
            {
                "jobId": t.string().optional(),
                "projectId": t.string().optional(),
                "workerId": t.string().optional(),
                "componentId": t.string().optional(),
                "location": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetDebugConfigResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsMessagesList"] = dataflow.get(
        "v1b3/projects/{projectId}/jobs/{jobId}/messages",
        t.struct(
            {
                "minimumImportance": t.string().optional(),
                "pageSize": t.integer().optional(),
                "projectId": t.string().optional(),
                "location": t.string().optional(),
                "startTime": t.string().optional(),
                "endTime": t.string().optional(),
                "pageToken": t.string().optional(),
                "jobId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobMessagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkerMessages"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/WorkerMessages",
        t.struct(
            {
                "projectId": t.string().optional(),
                "location": t.string().optional(),
                "workerMessages": t.array(
                    t.proxy(renames["WorkerMessageIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SendWorkerMessagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFlexTemplatesLaunch"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/flexTemplates:launch",
        t.struct(
            {
                "location": t.string(),
                "projectId": t.string(),
                "launchParameter": t.proxy(renames["LaunchFlexTemplateParameterIn"]),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LaunchFlexTemplateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTemplatesGet"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/templates:launch",
        t.struct(
            {
                "location": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "projectId": t.string(),
                "dynamicTemplate.stagingLocation": t.string().optional(),
                "dynamicTemplate.gcsPath": t.string().optional(),
                "gcsPath": t.string().optional(),
                "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "update": t.boolean().optional(),
                "jobName": t.string(),
                "transformNameMapping": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LaunchTemplateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTemplatesCreate"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/templates:launch",
        t.struct(
            {
                "location": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "projectId": t.string(),
                "dynamicTemplate.stagingLocation": t.string().optional(),
                "dynamicTemplate.gcsPath": t.string().optional(),
                "gcsPath": t.string().optional(),
                "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "update": t.boolean().optional(),
                "jobName": t.string(),
                "transformNameMapping": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LaunchTemplateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTemplatesLaunch"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/templates:launch",
        t.struct(
            {
                "location": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "projectId": t.string(),
                "dynamicTemplate.stagingLocation": t.string().optional(),
                "dynamicTemplate.gcsPath": t.string().optional(),
                "gcsPath": t.string().optional(),
                "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "update": t.boolean().optional(),
                "jobName": t.string(),
                "transformNameMapping": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LaunchTemplateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsUpdate"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/metrics",
        t.struct(
            {
                "location": t.string().optional(),
                "startTime": t.string().optional(),
                "jobId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobMetricsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsGet"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/metrics",
        t.struct(
            {
                "location": t.string().optional(),
                "startTime": t.string().optional(),
                "jobId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobMetricsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsSnapshot"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/metrics",
        t.struct(
            {
                "location": t.string().optional(),
                "startTime": t.string().optional(),
                "jobId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobMetricsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsGetExecutionDetails"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/metrics",
        t.struct(
            {
                "location": t.string().optional(),
                "startTime": t.string().optional(),
                "jobId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobMetricsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsCreate"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/metrics",
        t.struct(
            {
                "location": t.string().optional(),
                "startTime": t.string().optional(),
                "jobId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobMetricsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsList"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/metrics",
        t.struct(
            {
                "location": t.string().optional(),
                "startTime": t.string().optional(),
                "jobId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobMetricsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsGetMetrics"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/metrics",
        t.struct(
            {
                "location": t.string().optional(),
                "startTime": t.string().optional(),
                "jobId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobMetricsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsSnapshotsList"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/snapshots",
        t.struct(
            {
                "jobId": t.string().optional(),
                "projectId": t.string().optional(),
                "location": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSnapshotsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsStagesGetExecutionDetails"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/stages/{stageId}/executionDetails",
        t.struct(
            {
                "projectId": t.string().optional(),
                "startTime": t.string().optional(),
                "location": t.string().optional(),
                "stageId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "endTime": t.string().optional(),
                "jobId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StageExecutionDetailsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsDebugSendCapture"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/debug/getConfig",
        t.struct(
            {
                "location": t.string().optional(),
                "jobId": t.string().optional(),
                "projectId": t.string().optional(),
                "workerId": t.string().optional(),
                "componentId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetDebugConfigResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsDebugGetConfig"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/debug/getConfig",
        t.struct(
            {
                "location": t.string().optional(),
                "jobId": t.string().optional(),
                "projectId": t.string().optional(),
                "workerId": t.string().optional(),
                "componentId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetDebugConfigResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsMessagesList"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/messages",
        t.struct(
            {
                "minimumImportance": t.string().optional(),
                "projectId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "startTime": t.string().optional(),
                "pageToken": t.string().optional(),
                "endTime": t.string().optional(),
                "location": t.string().optional(),
                "jobId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobMessagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsWorkItemsReportStatus"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/workItems:lease",
        t.struct(
            {
                "location": t.string().optional(),
                "jobId": t.string().optional(),
                "projectId": t.string().optional(),
                "workItemTypes": t.array(t.string()).optional(),
                "requestedLeaseDuration": t.string().optional(),
                "workerId": t.string().optional(),
                "currentWorkerTime": t.string().optional(),
                "unifiedWorkerRequest": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "workerCapabilities": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaseWorkItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsWorkItemsLease"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/workItems:lease",
        t.struct(
            {
                "location": t.string().optional(),
                "jobId": t.string().optional(),
                "projectId": t.string().optional(),
                "workItemTypes": t.array(t.string()).optional(),
                "requestedLeaseDuration": t.string().optional(),
                "workerId": t.string().optional(),
                "currentWorkerTime": t.string().optional(),
                "unifiedWorkerRequest": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "workerCapabilities": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaseWorkItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSnapshotsDelete"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/snapshots",
        t.struct(
            {
                "location": t.string().optional(),
                "jobId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSnapshotsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSnapshotsGet"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/snapshots",
        t.struct(
            {
                "location": t.string().optional(),
                "jobId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSnapshotsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSnapshotsList"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/snapshots",
        t.struct(
            {
                "location": t.string().optional(),
                "jobId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSnapshotsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="dataflow", renames=renames, types=types, functions=functions
    )
