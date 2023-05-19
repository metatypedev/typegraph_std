from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_dataflow() -> Import:
    dataflow = HTTPRuntime("https://dataflow.googleapis.com/")

    renames = {
        "ErrorResponse": "_dataflow_1_ErrorResponse",
        "ReportedParallelismIn": "_dataflow_2_ReportedParallelismIn",
        "ReportedParallelismOut": "_dataflow_3_ReportedParallelismOut",
        "DynamicSourceSplitIn": "_dataflow_4_DynamicSourceSplitIn",
        "DynamicSourceSplitOut": "_dataflow_5_DynamicSourceSplitOut",
        "WorkItemIn": "_dataflow_6_WorkItemIn",
        "WorkItemOut": "_dataflow_7_WorkItemOut",
        "TemplateMetadataIn": "_dataflow_8_TemplateMetadataIn",
        "TemplateMetadataOut": "_dataflow_9_TemplateMetadataOut",
        "DatastoreIODetailsIn": "_dataflow_10_DatastoreIODetailsIn",
        "DatastoreIODetailsOut": "_dataflow_11_DatastoreIODetailsOut",
        "WorkerShutdownNoticeResponseIn": "_dataflow_12_WorkerShutdownNoticeResponseIn",
        "WorkerShutdownNoticeResponseOut": "_dataflow_13_WorkerShutdownNoticeResponseOut",
        "WriteInstructionIn": "_dataflow_14_WriteInstructionIn",
        "WriteInstructionOut": "_dataflow_15_WriteInstructionOut",
        "KeyRangeLocationIn": "_dataflow_16_KeyRangeLocationIn",
        "KeyRangeLocationOut": "_dataflow_17_KeyRangeLocationOut",
        "WorkerPoolIn": "_dataflow_18_WorkerPoolIn",
        "WorkerPoolOut": "_dataflow_19_WorkerPoolOut",
        "ContainerSpecIn": "_dataflow_20_ContainerSpecIn",
        "ContainerSpecOut": "_dataflow_21_ContainerSpecOut",
        "ParameterMetadataIn": "_dataflow_22_ParameterMetadataIn",
        "ParameterMetadataOut": "_dataflow_23_ParameterMetadataOut",
        "StragglerDebuggingInfoIn": "_dataflow_24_StragglerDebuggingInfoIn",
        "StragglerDebuggingInfoOut": "_dataflow_25_StragglerDebuggingInfoOut",
        "CounterMetadataIn": "_dataflow_26_CounterMetadataIn",
        "CounterMetadataOut": "_dataflow_27_CounterMetadataOut",
        "LaunchFlexTemplateResponseIn": "_dataflow_28_LaunchFlexTemplateResponseIn",
        "LaunchFlexTemplateResponseOut": "_dataflow_29_LaunchFlexTemplateResponseOut",
        "FloatingPointMeanIn": "_dataflow_30_FloatingPointMeanIn",
        "FloatingPointMeanOut": "_dataflow_31_FloatingPointMeanOut",
        "StageExecutionDetailsIn": "_dataflow_32_StageExecutionDetailsIn",
        "StageExecutionDetailsOut": "_dataflow_33_StageExecutionDetailsOut",
        "StreamingComputationTaskIn": "_dataflow_34_StreamingComputationTaskIn",
        "StreamingComputationTaskOut": "_dataflow_35_StreamingComputationTaskOut",
        "TransformSummaryIn": "_dataflow_36_TransformSummaryIn",
        "TransformSummaryOut": "_dataflow_37_TransformSummaryOut",
        "StragglerInfoIn": "_dataflow_38_StragglerInfoIn",
        "StragglerInfoOut": "_dataflow_39_StragglerInfoOut",
        "InstructionOutputIn": "_dataflow_40_InstructionOutputIn",
        "InstructionOutputOut": "_dataflow_41_InstructionOutputOut",
        "WorkerSettingsIn": "_dataflow_42_WorkerSettingsIn",
        "WorkerSettingsOut": "_dataflow_43_WorkerSettingsOut",
        "WorkItemServiceStateIn": "_dataflow_44_WorkItemServiceStateIn",
        "WorkItemServiceStateOut": "_dataflow_45_WorkItemServiceStateOut",
        "DebugOptionsIn": "_dataflow_46_DebugOptionsIn",
        "DebugOptionsOut": "_dataflow_47_DebugOptionsOut",
        "FlexTemplateRuntimeEnvironmentIn": "_dataflow_48_FlexTemplateRuntimeEnvironmentIn",
        "FlexTemplateRuntimeEnvironmentOut": "_dataflow_49_FlexTemplateRuntimeEnvironmentOut",
        "StreamingSetupTaskIn": "_dataflow_50_StreamingSetupTaskIn",
        "StreamingSetupTaskOut": "_dataflow_51_StreamingSetupTaskOut",
        "SeqMapTaskIn": "_dataflow_52_SeqMapTaskIn",
        "SeqMapTaskOut": "_dataflow_53_SeqMapTaskOut",
        "StreamingSideInputLocationIn": "_dataflow_54_StreamingSideInputLocationIn",
        "StreamingSideInputLocationOut": "_dataflow_55_StreamingSideInputLocationOut",
        "DeleteSnapshotResponseIn": "_dataflow_56_DeleteSnapshotResponseIn",
        "DeleteSnapshotResponseOut": "_dataflow_57_DeleteSnapshotResponseOut",
        "CounterStructuredNameIn": "_dataflow_58_CounterStructuredNameIn",
        "CounterStructuredNameOut": "_dataflow_59_CounterStructuredNameOut",
        "ShellTaskIn": "_dataflow_60_ShellTaskIn",
        "ShellTaskOut": "_dataflow_61_ShellTaskOut",
        "MultiOutputInfoIn": "_dataflow_62_MultiOutputInfoIn",
        "MultiOutputInfoOut": "_dataflow_63_MultiOutputInfoOut",
        "SourceOperationRequestIn": "_dataflow_64_SourceOperationRequestIn",
        "SourceOperationRequestOut": "_dataflow_65_SourceOperationRequestOut",
        "LeaseWorkItemResponseIn": "_dataflow_66_LeaseWorkItemResponseIn",
        "LeaseWorkItemResponseOut": "_dataflow_67_LeaseWorkItemResponseOut",
        "SdkHarnessContainerImageIn": "_dataflow_68_SdkHarnessContainerImageIn",
        "SdkHarnessContainerImageOut": "_dataflow_69_SdkHarnessContainerImageOut",
        "StragglerSummaryIn": "_dataflow_70_StragglerSummaryIn",
        "StragglerSummaryOut": "_dataflow_71_StragglerSummaryOut",
        "ListJobsResponseIn": "_dataflow_72_ListJobsResponseIn",
        "ListJobsResponseOut": "_dataflow_73_ListJobsResponseOut",
        "RuntimeEnvironmentIn": "_dataflow_74_RuntimeEnvironmentIn",
        "RuntimeEnvironmentOut": "_dataflow_75_RuntimeEnvironmentOut",
        "ResourceUtilizationReportResponseIn": "_dataflow_76_ResourceUtilizationReportResponseIn",
        "ResourceUtilizationReportResponseOut": "_dataflow_77_ResourceUtilizationReportResponseOut",
        "WorkerMessageIn": "_dataflow_78_WorkerMessageIn",
        "WorkerMessageOut": "_dataflow_79_WorkerMessageOut",
        "RuntimeMetadataIn": "_dataflow_80_RuntimeMetadataIn",
        "RuntimeMetadataOut": "_dataflow_81_RuntimeMetadataOut",
        "SideInputInfoIn": "_dataflow_82_SideInputInfoIn",
        "SideInputInfoOut": "_dataflow_83_SideInputInfoOut",
        "JobIn": "_dataflow_84_JobIn",
        "JobOut": "_dataflow_85_JobOut",
        "StreamingComputationRangesIn": "_dataflow_86_StreamingComputationRangesIn",
        "StreamingComputationRangesOut": "_dataflow_87_StreamingComputationRangesOut",
        "MemInfoIn": "_dataflow_88_MemInfoIn",
        "MemInfoOut": "_dataflow_89_MemInfoOut",
        "SourceSplitOptionsIn": "_dataflow_90_SourceSplitOptionsIn",
        "SourceSplitOptionsOut": "_dataflow_91_SourceSplitOptionsOut",
        "DataDiskAssignmentIn": "_dataflow_92_DataDiskAssignmentIn",
        "DataDiskAssignmentOut": "_dataflow_93_DataDiskAssignmentOut",
        "SourceGetMetadataResponseIn": "_dataflow_94_SourceGetMetadataResponseIn",
        "SourceGetMetadataResponseOut": "_dataflow_95_SourceGetMetadataResponseOut",
        "StructuredMessageIn": "_dataflow_96_StructuredMessageIn",
        "StructuredMessageOut": "_dataflow_97_StructuredMessageOut",
        "SourceSplitResponseIn": "_dataflow_98_SourceSplitResponseIn",
        "SourceSplitResponseOut": "_dataflow_99_SourceSplitResponseOut",
        "WorkerHealthReportResponseIn": "_dataflow_100_WorkerHealthReportResponseIn",
        "WorkerHealthReportResponseOut": "_dataflow_101_WorkerHealthReportResponseOut",
        "ParallelInstructionIn": "_dataflow_102_ParallelInstructionIn",
        "ParallelInstructionOut": "_dataflow_103_ParallelInstructionOut",
        "StragglerIn": "_dataflow_104_StragglerIn",
        "StragglerOut": "_dataflow_105_StragglerOut",
        "CreateJobFromTemplateRequestIn": "_dataflow_106_CreateJobFromTemplateRequestIn",
        "CreateJobFromTemplateRequestOut": "_dataflow_107_CreateJobFromTemplateRequestOut",
        "DerivedSourceIn": "_dataflow_108_DerivedSourceIn",
        "DerivedSourceOut": "_dataflow_109_DerivedSourceOut",
        "ApproximateReportedProgressIn": "_dataflow_110_ApproximateReportedProgressIn",
        "ApproximateReportedProgressOut": "_dataflow_111_ApproximateReportedProgressOut",
        "StreamingApplianceSnapshotConfigIn": "_dataflow_112_StreamingApplianceSnapshotConfigIn",
        "StreamingApplianceSnapshotConfigOut": "_dataflow_113_StreamingApplianceSnapshotConfigOut",
        "HistogramIn": "_dataflow_114_HistogramIn",
        "HistogramOut": "_dataflow_115_HistogramOut",
        "PipelineDescriptionIn": "_dataflow_116_PipelineDescriptionIn",
        "PipelineDescriptionOut": "_dataflow_117_PipelineDescriptionOut",
        "ComponentSourceIn": "_dataflow_118_ComponentSourceIn",
        "ComponentSourceOut": "_dataflow_119_ComponentSourceOut",
        "InstructionInputIn": "_dataflow_120_InstructionInputIn",
        "InstructionInputOut": "_dataflow_121_InstructionInputOut",
        "SdkVersionIn": "_dataflow_122_SdkVersionIn",
        "SdkVersionOut": "_dataflow_123_SdkVersionOut",
        "DistributionUpdateIn": "_dataflow_124_DistributionUpdateIn",
        "DistributionUpdateOut": "_dataflow_125_DistributionUpdateOut",
        "LaunchTemplateParametersIn": "_dataflow_126_LaunchTemplateParametersIn",
        "LaunchTemplateParametersOut": "_dataflow_127_LaunchTemplateParametersOut",
        "CounterStructuredNameAndMetadataIn": "_dataflow_128_CounterStructuredNameAndMetadataIn",
        "CounterStructuredNameAndMetadataOut": "_dataflow_129_CounterStructuredNameAndMetadataOut",
        "ParameterIn": "_dataflow_130_ParameterIn",
        "ParameterOut": "_dataflow_131_ParameterOut",
        "CPUTimeIn": "_dataflow_132_CPUTimeIn",
        "CPUTimeOut": "_dataflow_133_CPUTimeOut",
        "StageSourceIn": "_dataflow_134_StageSourceIn",
        "StageSourceOut": "_dataflow_135_StageSourceOut",
        "SourceGetMetadataRequestIn": "_dataflow_136_SourceGetMetadataRequestIn",
        "SourceGetMetadataRequestOut": "_dataflow_137_SourceGetMetadataRequestOut",
        "StreamingComputationConfigIn": "_dataflow_138_StreamingComputationConfigIn",
        "StreamingComputationConfigOut": "_dataflow_139_StreamingComputationConfigOut",
        "AutoscalingEventIn": "_dataflow_140_AutoscalingEventIn",
        "AutoscalingEventOut": "_dataflow_141_AutoscalingEventOut",
        "JobMessageIn": "_dataflow_142_JobMessageIn",
        "JobMessageOut": "_dataflow_143_JobMessageOut",
        "PointIn": "_dataflow_144_PointIn",
        "PointOut": "_dataflow_145_PointOut",
        "SnapshotIn": "_dataflow_146_SnapshotIn",
        "SnapshotOut": "_dataflow_147_SnapshotOut",
        "RuntimeUpdatableParamsIn": "_dataflow_148_RuntimeUpdatableParamsIn",
        "RuntimeUpdatableParamsOut": "_dataflow_149_RuntimeUpdatableParamsOut",
        "PubsubLocationIn": "_dataflow_150_PubsubLocationIn",
        "PubsubLocationOut": "_dataflow_151_PubsubLocationOut",
        "FileIODetailsIn": "_dataflow_152_FileIODetailsIn",
        "FileIODetailsOut": "_dataflow_153_FileIODetailsOut",
        "StatusIn": "_dataflow_154_StatusIn",
        "StatusOut": "_dataflow_155_StatusOut",
        "ProgressTimeseriesIn": "_dataflow_156_ProgressTimeseriesIn",
        "ProgressTimeseriesOut": "_dataflow_157_ProgressTimeseriesOut",
        "SendDebugCaptureRequestIn": "_dataflow_158_SendDebugCaptureRequestIn",
        "SendDebugCaptureRequestOut": "_dataflow_159_SendDebugCaptureRequestOut",
        "GetTemplateResponseIn": "_dataflow_160_GetTemplateResponseIn",
        "GetTemplateResponseOut": "_dataflow_161_GetTemplateResponseOut",
        "SendWorkerMessagesResponseIn": "_dataflow_162_SendWorkerMessagesResponseIn",
        "SendWorkerMessagesResponseOut": "_dataflow_163_SendWorkerMessagesResponseOut",
        "IntegerMeanIn": "_dataflow_164_IntegerMeanIn",
        "IntegerMeanOut": "_dataflow_165_IntegerMeanOut",
        "TopologyConfigIn": "_dataflow_166_TopologyConfigIn",
        "TopologyConfigOut": "_dataflow_167_TopologyConfigOut",
        "HotKeyDebuggingInfoIn": "_dataflow_168_HotKeyDebuggingInfoIn",
        "HotKeyDebuggingInfoOut": "_dataflow_169_HotKeyDebuggingInfoOut",
        "HotKeyDetectionIn": "_dataflow_170_HotKeyDetectionIn",
        "HotKeyDetectionOut": "_dataflow_171_HotKeyDetectionOut",
        "PubSubIODetailsIn": "_dataflow_172_PubSubIODetailsIn",
        "PubSubIODetailsOut": "_dataflow_173_PubSubIODetailsOut",
        "MountedDataDiskIn": "_dataflow_174_MountedDataDiskIn",
        "MountedDataDiskOut": "_dataflow_175_MountedDataDiskOut",
        "MapTaskIn": "_dataflow_176_MapTaskIn",
        "MapTaskOut": "_dataflow_177_MapTaskOut",
        "SDKInfoIn": "_dataflow_178_SDKInfoIn",
        "SDKInfoOut": "_dataflow_179_SDKInfoOut",
        "StageSummaryIn": "_dataflow_180_StageSummaryIn",
        "StageSummaryOut": "_dataflow_181_StageSummaryOut",
        "ReportWorkItemStatusResponseIn": "_dataflow_182_ReportWorkItemStatusResponseIn",
        "ReportWorkItemStatusResponseOut": "_dataflow_183_ReportWorkItemStatusResponseOut",
        "WorkItemStatusIn": "_dataflow_184_WorkItemStatusIn",
        "WorkItemStatusOut": "_dataflow_185_WorkItemStatusOut",
        "LaunchFlexTemplateParameterIn": "_dataflow_186_LaunchFlexTemplateParameterIn",
        "LaunchFlexTemplateParameterOut": "_dataflow_187_LaunchFlexTemplateParameterOut",
        "ConcatPositionIn": "_dataflow_188_ConcatPositionIn",
        "ConcatPositionOut": "_dataflow_189_ConcatPositionOut",
        "ParDoInstructionIn": "_dataflow_190_ParDoInstructionIn",
        "ParDoInstructionOut": "_dataflow_191_ParDoInstructionOut",
        "LaunchFlexTemplateRequestIn": "_dataflow_192_LaunchFlexTemplateRequestIn",
        "LaunchFlexTemplateRequestOut": "_dataflow_193_LaunchFlexTemplateRequestOut",
        "StreamingStageLocationIn": "_dataflow_194_StreamingStageLocationIn",
        "StreamingStageLocationOut": "_dataflow_195_StreamingStageLocationOut",
        "PackageIn": "_dataflow_196_PackageIn",
        "PackageOut": "_dataflow_197_PackageOut",
        "CustomSourceLocationIn": "_dataflow_198_CustomSourceLocationIn",
        "CustomSourceLocationOut": "_dataflow_199_CustomSourceLocationOut",
        "KeyRangeDataDiskAssignmentIn": "_dataflow_200_KeyRangeDataDiskAssignmentIn",
        "KeyRangeDataDiskAssignmentOut": "_dataflow_201_KeyRangeDataDiskAssignmentOut",
        "MetricStructuredNameIn": "_dataflow_202_MetricStructuredNameIn",
        "MetricStructuredNameOut": "_dataflow_203_MetricStructuredNameOut",
        "JobMetadataIn": "_dataflow_204_JobMetadataIn",
        "JobMetadataOut": "_dataflow_205_JobMetadataOut",
        "IntegerGaugeIn": "_dataflow_206_IntegerGaugeIn",
        "IntegerGaugeOut": "_dataflow_207_IntegerGaugeOut",
        "ComputationTopologyIn": "_dataflow_208_ComputationTopologyIn",
        "ComputationTopologyOut": "_dataflow_209_ComputationTopologyOut",
        "IntegerListIn": "_dataflow_210_IntegerListIn",
        "IntegerListOut": "_dataflow_211_IntegerListOut",
        "ApproximateProgressIn": "_dataflow_212_ApproximateProgressIn",
        "ApproximateProgressOut": "_dataflow_213_ApproximateProgressOut",
        "MetricShortIdIn": "_dataflow_214_MetricShortIdIn",
        "MetricShortIdOut": "_dataflow_215_MetricShortIdOut",
        "SinkIn": "_dataflow_216_SinkIn",
        "SinkOut": "_dataflow_217_SinkOut",
        "CounterUpdateIn": "_dataflow_218_CounterUpdateIn",
        "CounterUpdateOut": "_dataflow_219_CounterUpdateOut",
        "TaskRunnerSettingsIn": "_dataflow_220_TaskRunnerSettingsIn",
        "TaskRunnerSettingsOut": "_dataflow_221_TaskRunnerSettingsOut",
        "StateFamilyConfigIn": "_dataflow_222_StateFamilyConfigIn",
        "StateFamilyConfigOut": "_dataflow_223_StateFamilyConfigOut",
        "LeaseWorkItemRequestIn": "_dataflow_224_LeaseWorkItemRequestIn",
        "LeaseWorkItemRequestOut": "_dataflow_225_LeaseWorkItemRequestOut",
        "SendWorkerMessagesRequestIn": "_dataflow_226_SendWorkerMessagesRequestIn",
        "SendWorkerMessagesRequestOut": "_dataflow_227_SendWorkerMessagesRequestOut",
        "StepIn": "_dataflow_228_StepIn",
        "StepOut": "_dataflow_229_StepOut",
        "StringListIn": "_dataflow_230_StringListIn",
        "StringListOut": "_dataflow_231_StringListOut",
        "FloatingPointListIn": "_dataflow_232_FloatingPointListIn",
        "FloatingPointListOut": "_dataflow_233_FloatingPointListOut",
        "WorkerThreadScalingReportResponseIn": "_dataflow_234_WorkerThreadScalingReportResponseIn",
        "WorkerThreadScalingReportResponseOut": "_dataflow_235_WorkerThreadScalingReportResponseOut",
        "LaunchTemplateResponseIn": "_dataflow_236_LaunchTemplateResponseIn",
        "LaunchTemplateResponseOut": "_dataflow_237_LaunchTemplateResponseOut",
        "SplitInt64In": "_dataflow_238_SplitInt64In",
        "SplitInt64Out": "_dataflow_239_SplitInt64Out",
        "ListSnapshotsResponseIn": "_dataflow_240_ListSnapshotsResponseIn",
        "ListSnapshotsResponseOut": "_dataflow_241_ListSnapshotsResponseOut",
        "FailedLocationIn": "_dataflow_242_FailedLocationIn",
        "FailedLocationOut": "_dataflow_243_FailedLocationOut",
        "ExecutionStageStateIn": "_dataflow_244_ExecutionStageStateIn",
        "ExecutionStageStateOut": "_dataflow_245_ExecutionStageStateOut",
        "ReportWorkItemStatusRequestIn": "_dataflow_246_ReportWorkItemStatusRequestIn",
        "ReportWorkItemStatusRequestOut": "_dataflow_247_ReportWorkItemStatusRequestOut",
        "StreamLocationIn": "_dataflow_248_StreamLocationIn",
        "StreamLocationOut": "_dataflow_249_StreamLocationOut",
        "HotKeyInfoIn": "_dataflow_250_HotKeyInfoIn",
        "HotKeyInfoOut": "_dataflow_251_HotKeyInfoOut",
        "PubsubSnapshotMetadataIn": "_dataflow_252_PubsubSnapshotMetadataIn",
        "PubsubSnapshotMetadataOut": "_dataflow_253_PubsubSnapshotMetadataOut",
        "WorkerMessageResponseIn": "_dataflow_254_WorkerMessageResponseIn",
        "WorkerMessageResponseOut": "_dataflow_255_WorkerMessageResponseOut",
        "JobExecutionDetailsIn": "_dataflow_256_JobExecutionDetailsIn",
        "JobExecutionDetailsOut": "_dataflow_257_JobExecutionDetailsOut",
        "FlattenInstructionIn": "_dataflow_258_FlattenInstructionIn",
        "FlattenInstructionOut": "_dataflow_259_FlattenInstructionOut",
        "BigQueryIODetailsIn": "_dataflow_260_BigQueryIODetailsIn",
        "BigQueryIODetailsOut": "_dataflow_261_BigQueryIODetailsOut",
        "ComponentTransformIn": "_dataflow_262_ComponentTransformIn",
        "ComponentTransformOut": "_dataflow_263_ComponentTransformOut",
        "DiskIn": "_dataflow_264_DiskIn",
        "DiskOut": "_dataflow_265_DiskOut",
        "WorkerLifecycleEventIn": "_dataflow_266_WorkerLifecycleEventIn",
        "WorkerLifecycleEventOut": "_dataflow_267_WorkerLifecycleEventOut",
        "StreamingConfigTaskIn": "_dataflow_268_StreamingConfigTaskIn",
        "StreamingConfigTaskOut": "_dataflow_269_StreamingConfigTaskOut",
        "WorkerThreadScalingReportIn": "_dataflow_270_WorkerThreadScalingReportIn",
        "WorkerThreadScalingReportOut": "_dataflow_271_WorkerThreadScalingReportOut",
        "BigTableIODetailsIn": "_dataflow_272_BigTableIODetailsIn",
        "BigTableIODetailsOut": "_dataflow_273_BigTableIODetailsOut",
        "ExecutionStageSummaryIn": "_dataflow_274_ExecutionStageSummaryIn",
        "ExecutionStageSummaryOut": "_dataflow_275_ExecutionStageSummaryOut",
        "JobExecutionStageInfoIn": "_dataflow_276_JobExecutionStageInfoIn",
        "JobExecutionStageInfoOut": "_dataflow_277_JobExecutionStageInfoOut",
        "WorkItemDetailsIn": "_dataflow_278_WorkItemDetailsIn",
        "WorkItemDetailsOut": "_dataflow_279_WorkItemDetailsOut",
        "WorkerMessageCodeIn": "_dataflow_280_WorkerMessageCodeIn",
        "WorkerMessageCodeOut": "_dataflow_281_WorkerMessageCodeOut",
        "DisplayDataIn": "_dataflow_282_DisplayDataIn",
        "DisplayDataOut": "_dataflow_283_DisplayDataOut",
        "WorkerDetailsIn": "_dataflow_284_WorkerDetailsIn",
        "WorkerDetailsOut": "_dataflow_285_WorkerDetailsOut",
        "ApproximateSplitRequestIn": "_dataflow_286_ApproximateSplitRequestIn",
        "ApproximateSplitRequestOut": "_dataflow_287_ApproximateSplitRequestOut",
        "SourceForkIn": "_dataflow_288_SourceForkIn",
        "SourceForkOut": "_dataflow_289_SourceForkOut",
        "SpannerIODetailsIn": "_dataflow_290_SpannerIODetailsIn",
        "SpannerIODetailsOut": "_dataflow_291_SpannerIODetailsOut",
        "JobMetricsIn": "_dataflow_292_JobMetricsIn",
        "JobMetricsOut": "_dataflow_293_JobMetricsOut",
        "SourceSplitRequestIn": "_dataflow_294_SourceSplitRequestIn",
        "SourceSplitRequestOut": "_dataflow_295_SourceSplitRequestOut",
        "SourceIn": "_dataflow_296_SourceIn",
        "SourceOut": "_dataflow_297_SourceOut",
        "ResourceUtilizationReportIn": "_dataflow_298_ResourceUtilizationReportIn",
        "ResourceUtilizationReportOut": "_dataflow_299_ResourceUtilizationReportOut",
        "SourceOperationResponseIn": "_dataflow_300_SourceOperationResponseIn",
        "SourceOperationResponseOut": "_dataflow_301_SourceOperationResponseOut",
        "SnapshotJobRequestIn": "_dataflow_302_SnapshotJobRequestIn",
        "SnapshotJobRequestOut": "_dataflow_303_SnapshotJobRequestOut",
        "WorkerHealthReportIn": "_dataflow_304_WorkerHealthReportIn",
        "WorkerHealthReportOut": "_dataflow_305_WorkerHealthReportOut",
        "SendDebugCaptureResponseIn": "_dataflow_306_SendDebugCaptureResponseIn",
        "SendDebugCaptureResponseOut": "_dataflow_307_SendDebugCaptureResponseOut",
        "SourceMetadataIn": "_dataflow_308_SourceMetadataIn",
        "SourceMetadataOut": "_dataflow_309_SourceMetadataOut",
        "StreamingStragglerInfoIn": "_dataflow_310_StreamingStragglerInfoIn",
        "StreamingStragglerInfoOut": "_dataflow_311_StreamingStragglerInfoOut",
        "JobExecutionInfoIn": "_dataflow_312_JobExecutionInfoIn",
        "JobExecutionInfoOut": "_dataflow_313_JobExecutionInfoOut",
        "MetricUpdateIn": "_dataflow_314_MetricUpdateIn",
        "MetricUpdateOut": "_dataflow_315_MetricUpdateOut",
        "GetDebugConfigRequestIn": "_dataflow_316_GetDebugConfigRequestIn",
        "GetDebugConfigRequestOut": "_dataflow_317_GetDebugConfigRequestOut",
        "EnvironmentIn": "_dataflow_318_EnvironmentIn",
        "EnvironmentOut": "_dataflow_319_EnvironmentOut",
        "PositionIn": "_dataflow_320_PositionIn",
        "PositionOut": "_dataflow_321_PositionOut",
        "NameAndKindIn": "_dataflow_322_NameAndKindIn",
        "NameAndKindOut": "_dataflow_323_NameAndKindOut",
        "WorkerShutdownNoticeIn": "_dataflow_324_WorkerShutdownNoticeIn",
        "WorkerShutdownNoticeOut": "_dataflow_325_WorkerShutdownNoticeOut",
        "GetDebugConfigResponseIn": "_dataflow_326_GetDebugConfigResponseIn",
        "GetDebugConfigResponseOut": "_dataflow_327_GetDebugConfigResponseOut",
        "SourceSplitShardIn": "_dataflow_328_SourceSplitShardIn",
        "SourceSplitShardOut": "_dataflow_329_SourceSplitShardOut",
        "ListJobMessagesResponseIn": "_dataflow_330_ListJobMessagesResponseIn",
        "ListJobMessagesResponseOut": "_dataflow_331_ListJobMessagesResponseOut",
        "ReadInstructionIn": "_dataflow_332_ReadInstructionIn",
        "ReadInstructionOut": "_dataflow_333_ReadInstructionOut",
        "PartialGroupByKeyInstructionIn": "_dataflow_334_PartialGroupByKeyInstructionIn",
        "PartialGroupByKeyInstructionOut": "_dataflow_335_PartialGroupByKeyInstructionOut",
        "AutoscalingSettingsIn": "_dataflow_336_AutoscalingSettingsIn",
        "AutoscalingSettingsOut": "_dataflow_337_AutoscalingSettingsOut",
        "SeqMapTaskOutputInfoIn": "_dataflow_338_SeqMapTaskOutputInfoIn",
        "SeqMapTaskOutputInfoOut": "_dataflow_339_SeqMapTaskOutputInfoOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ReportedParallelismIn"] = t.struct(
        {"value": t.number().optional(), "isInfinite": t.boolean().optional()}
    ).named(renames["ReportedParallelismIn"])
    types["ReportedParallelismOut"] = t.struct(
        {
            "value": t.number().optional(),
            "isInfinite": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportedParallelismOut"])
    types["DynamicSourceSplitIn"] = t.struct(
        {
            "residual": t.proxy(renames["DerivedSourceIn"]).optional(),
            "primary": t.proxy(renames["DerivedSourceIn"]).optional(),
        }
    ).named(renames["DynamicSourceSplitIn"])
    types["DynamicSourceSplitOut"] = t.struct(
        {
            "residual": t.proxy(renames["DerivedSourceOut"]).optional(),
            "primary": t.proxy(renames["DerivedSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicSourceSplitOut"])
    types["WorkItemIn"] = t.struct(
        {
            "configuration": t.string().optional(),
            "packages": t.array(t.proxy(renames["PackageIn"])).optional(),
            "mapTask": t.proxy(renames["MapTaskIn"]).optional(),
            "leaseExpireTime": t.string().optional(),
            "streamingComputationTask": t.proxy(
                renames["StreamingComputationTaskIn"]
            ).optional(),
            "sourceOperationTask": t.proxy(
                renames["SourceOperationRequestIn"]
            ).optional(),
            "projectId": t.string().optional(),
            "shellTask": t.proxy(renames["ShellTaskIn"]).optional(),
            "initialReportIndex": t.string().optional(),
            "seqMapTask": t.proxy(renames["SeqMapTaskIn"]).optional(),
            "streamingSetupTask": t.proxy(renames["StreamingSetupTaskIn"]).optional(),
            "reportStatusInterval": t.string().optional(),
            "jobId": t.string().optional(),
            "streamingConfigTask": t.proxy(renames["StreamingConfigTaskIn"]).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["WorkItemIn"])
    types["WorkItemOut"] = t.struct(
        {
            "configuration": t.string().optional(),
            "packages": t.array(t.proxy(renames["PackageOut"])).optional(),
            "mapTask": t.proxy(renames["MapTaskOut"]).optional(),
            "leaseExpireTime": t.string().optional(),
            "streamingComputationTask": t.proxy(
                renames["StreamingComputationTaskOut"]
            ).optional(),
            "sourceOperationTask": t.proxy(
                renames["SourceOperationRequestOut"]
            ).optional(),
            "projectId": t.string().optional(),
            "shellTask": t.proxy(renames["ShellTaskOut"]).optional(),
            "initialReportIndex": t.string().optional(),
            "seqMapTask": t.proxy(renames["SeqMapTaskOut"]).optional(),
            "streamingSetupTask": t.proxy(renames["StreamingSetupTaskOut"]).optional(),
            "reportStatusInterval": t.string().optional(),
            "jobId": t.string().optional(),
            "streamingConfigTask": t.proxy(
                renames["StreamingConfigTaskOut"]
            ).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkItemOut"])
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
    types["DatastoreIODetailsIn"] = t.struct(
        {"projectId": t.string().optional(), "namespace": t.string().optional()}
    ).named(renames["DatastoreIODetailsIn"])
    types["DatastoreIODetailsOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "namespace": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatastoreIODetailsOut"])
    types["WorkerShutdownNoticeResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["WorkerShutdownNoticeResponseIn"])
    types["WorkerShutdownNoticeResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WorkerShutdownNoticeResponseOut"])
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
    types["KeyRangeLocationIn"] = t.struct(
        {
            "deliveryEndpoint": t.string().optional(),
            "end": t.string().optional(),
            "start": t.string().optional(),
            "dataDisk": t.string().optional(),
            "deprecatedPersistentDirectory": t.string().optional(),
        }
    ).named(renames["KeyRangeLocationIn"])
    types["KeyRangeLocationOut"] = t.struct(
        {
            "deliveryEndpoint": t.string().optional(),
            "end": t.string().optional(),
            "start": t.string().optional(),
            "dataDisk": t.string().optional(),
            "deprecatedPersistentDirectory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyRangeLocationOut"])
    types["WorkerPoolIn"] = t.struct(
        {
            "diskSizeGb": t.integer().optional(),
            "teardownPolicy": t.string().optional(),
            "diskSourceImage": t.string().optional(),
            "onHostMaintenance": t.string().optional(),
            "zone": t.string().optional(),
            "subnetwork": t.string().optional(),
            "ipConfiguration": t.string().optional(),
            "machineType": t.string().optional(),
            "taskrunnerSettings": t.proxy(renames["TaskRunnerSettingsIn"]).optional(),
            "kind": t.string().optional(),
            "numThreadsPerWorker": t.integer().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "packages": t.array(t.proxy(renames["PackageIn"])).optional(),
            "poolArgs": t.struct({"_": t.string().optional()}).optional(),
            "dataDisks": t.array(t.proxy(renames["DiskIn"])).optional(),
            "autoscalingSettings": t.proxy(renames["AutoscalingSettingsIn"]).optional(),
            "numWorkers": t.integer().optional(),
            "workerHarnessContainerImage": t.string(),
            "network": t.string().optional(),
            "defaultPackageSet": t.string().optional(),
            "diskType": t.string().optional(),
            "sdkHarnessContainerImages": t.array(
                t.proxy(renames["SdkHarnessContainerImageIn"])
            ).optional(),
        }
    ).named(renames["WorkerPoolIn"])
    types["WorkerPoolOut"] = t.struct(
        {
            "diskSizeGb": t.integer().optional(),
            "teardownPolicy": t.string().optional(),
            "diskSourceImage": t.string().optional(),
            "onHostMaintenance": t.string().optional(),
            "zone": t.string().optional(),
            "subnetwork": t.string().optional(),
            "ipConfiguration": t.string().optional(),
            "machineType": t.string().optional(),
            "taskrunnerSettings": t.proxy(renames["TaskRunnerSettingsOut"]).optional(),
            "kind": t.string().optional(),
            "numThreadsPerWorker": t.integer().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "packages": t.array(t.proxy(renames["PackageOut"])).optional(),
            "poolArgs": t.struct({"_": t.string().optional()}).optional(),
            "dataDisks": t.array(t.proxy(renames["DiskOut"])).optional(),
            "autoscalingSettings": t.proxy(
                renames["AutoscalingSettingsOut"]
            ).optional(),
            "numWorkers": t.integer().optional(),
            "workerHarnessContainerImage": t.string(),
            "network": t.string().optional(),
            "defaultPackageSet": t.string().optional(),
            "diskType": t.string().optional(),
            "sdkHarnessContainerImages": t.array(
                t.proxy(renames["SdkHarnessContainerImageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerPoolOut"])
    types["ContainerSpecIn"] = t.struct(
        {
            "sdkInfo": t.proxy(renames["SDKInfoIn"]),
            "imageRepositoryPasswordSecretId": t.string().optional(),
            "metadata": t.proxy(renames["TemplateMetadataIn"]).optional(),
            "defaultEnvironment": t.proxy(
                renames["FlexTemplateRuntimeEnvironmentIn"]
            ).optional(),
            "imageRepositoryCertPath": t.string().optional(),
            "image": t.string().optional(),
            "imageRepositoryUsernameSecretId": t.string().optional(),
        }
    ).named(renames["ContainerSpecIn"])
    types["ContainerSpecOut"] = t.struct(
        {
            "sdkInfo": t.proxy(renames["SDKInfoOut"]),
            "imageRepositoryPasswordSecretId": t.string().optional(),
            "metadata": t.proxy(renames["TemplateMetadataOut"]).optional(),
            "defaultEnvironment": t.proxy(
                renames["FlexTemplateRuntimeEnvironmentOut"]
            ).optional(),
            "imageRepositoryCertPath": t.string().optional(),
            "image": t.string().optional(),
            "imageRepositoryUsernameSecretId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerSpecOut"])
    types["ParameterMetadataIn"] = t.struct(
        {
            "paramType": t.string().optional(),
            "groupName": t.string().optional(),
            "helpText": t.string(),
            "customMetadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "parentTriggerValues": t.array(t.string()).optional(),
            "parentName": t.string().optional(),
            "regexes": t.array(t.string()).optional(),
            "isOptional": t.boolean().optional(),
            "label": t.string(),
        }
    ).named(renames["ParameterMetadataIn"])
    types["ParameterMetadataOut"] = t.struct(
        {
            "paramType": t.string().optional(),
            "groupName": t.string().optional(),
            "helpText": t.string(),
            "customMetadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "parentTriggerValues": t.array(t.string()).optional(),
            "parentName": t.string().optional(),
            "regexes": t.array(t.string()).optional(),
            "isOptional": t.boolean().optional(),
            "label": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParameterMetadataOut"])
    types["StragglerDebuggingInfoIn"] = t.struct(
        {"hotKey": t.proxy(renames["HotKeyDebuggingInfoIn"]).optional()}
    ).named(renames["StragglerDebuggingInfoIn"])
    types["StragglerDebuggingInfoOut"] = t.struct(
        {
            "hotKey": t.proxy(renames["HotKeyDebuggingInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StragglerDebuggingInfoOut"])
    types["CounterMetadataIn"] = t.struct(
        {
            "standardUnits": t.string().optional(),
            "kind": t.string().optional(),
            "description": t.string().optional(),
            "otherUnits": t.string().optional(),
        }
    ).named(renames["CounterMetadataIn"])
    types["CounterMetadataOut"] = t.struct(
        {
            "standardUnits": t.string().optional(),
            "kind": t.string().optional(),
            "description": t.string().optional(),
            "otherUnits": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CounterMetadataOut"])
    types["LaunchFlexTemplateResponseIn"] = t.struct(
        {"job": t.proxy(renames["JobIn"]).optional()}
    ).named(renames["LaunchFlexTemplateResponseIn"])
    types["LaunchFlexTemplateResponseOut"] = t.struct(
        {
            "job": t.proxy(renames["JobOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LaunchFlexTemplateResponseOut"])
    types["FloatingPointMeanIn"] = t.struct(
        {
            "sum": t.number().optional(),
            "count": t.proxy(renames["SplitInt64In"]).optional(),
        }
    ).named(renames["FloatingPointMeanIn"])
    types["FloatingPointMeanOut"] = t.struct(
        {
            "sum": t.number().optional(),
            "count": t.proxy(renames["SplitInt64Out"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloatingPointMeanOut"])
    types["StageExecutionDetailsIn"] = t.struct(
        {
            "workers": t.array(t.proxy(renames["WorkerDetailsIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["StageExecutionDetailsIn"])
    types["StageExecutionDetailsOut"] = t.struct(
        {
            "workers": t.array(t.proxy(renames["WorkerDetailsOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StageExecutionDetailsOut"])
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
    types["TransformSummaryIn"] = t.struct(
        {
            "outputCollectionName": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "displayData": t.array(t.proxy(renames["DisplayDataIn"])).optional(),
            "inputCollectionName": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["TransformSummaryIn"])
    types["TransformSummaryOut"] = t.struct(
        {
            "outputCollectionName": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "displayData": t.array(t.proxy(renames["DisplayDataOut"])).optional(),
            "inputCollectionName": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransformSummaryOut"])
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
    types["InstructionOutputIn"] = t.struct(
        {
            "onlyCountValueBytes": t.boolean().optional(),
            "codec": t.struct({"_": t.string().optional()}).optional(),
            "onlyCountKeyBytes": t.boolean().optional(),
            "systemName": t.string().optional(),
            "name": t.string().optional(),
            "originalName": t.string().optional(),
        }
    ).named(renames["InstructionOutputIn"])
    types["InstructionOutputOut"] = t.struct(
        {
            "onlyCountValueBytes": t.boolean().optional(),
            "codec": t.struct({"_": t.string().optional()}).optional(),
            "onlyCountKeyBytes": t.boolean().optional(),
            "systemName": t.string().optional(),
            "name": t.string().optional(),
            "originalName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstructionOutputOut"])
    types["WorkerSettingsIn"] = t.struct(
        {
            "workerId": t.string().optional(),
            "baseUrl": t.string().optional(),
            "servicePath": t.string().optional(),
            "reportingEnabled": t.boolean().optional(),
            "shuffleServicePath": t.string().optional(),
            "tempStoragePrefix": t.string().optional(),
        }
    ).named(renames["WorkerSettingsIn"])
    types["WorkerSettingsOut"] = t.struct(
        {
            "workerId": t.string().optional(),
            "baseUrl": t.string().optional(),
            "servicePath": t.string().optional(),
            "reportingEnabled": t.boolean().optional(),
            "shuffleServicePath": t.string().optional(),
            "tempStoragePrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerSettingsOut"])
    types["WorkItemServiceStateIn"] = t.struct(
        {
            "harnessData": t.struct({"_": t.string().optional()}).optional(),
            "suggestedStopPosition": t.proxy(renames["PositionIn"]).optional(),
            "nextReportIndex": t.string().optional(),
            "reportStatusInterval": t.string().optional(),
            "hotKeyDetection": t.proxy(renames["HotKeyDetectionIn"]).optional(),
            "completeWorkStatus": t.proxy(renames["StatusIn"]).optional(),
            "splitRequest": t.proxy(renames["ApproximateSplitRequestIn"]).optional(),
            "suggestedStopPoint": t.proxy(renames["ApproximateProgressIn"]).optional(),
            "metricShortId": t.array(t.proxy(renames["MetricShortIdIn"])).optional(),
            "leaseExpireTime": t.string().optional(),
        }
    ).named(renames["WorkItemServiceStateIn"])
    types["WorkItemServiceStateOut"] = t.struct(
        {
            "harnessData": t.struct({"_": t.string().optional()}).optional(),
            "suggestedStopPosition": t.proxy(renames["PositionOut"]).optional(),
            "nextReportIndex": t.string().optional(),
            "reportStatusInterval": t.string().optional(),
            "hotKeyDetection": t.proxy(renames["HotKeyDetectionOut"]).optional(),
            "completeWorkStatus": t.proxy(renames["StatusOut"]).optional(),
            "splitRequest": t.proxy(renames["ApproximateSplitRequestOut"]).optional(),
            "suggestedStopPoint": t.proxy(renames["ApproximateProgressOut"]).optional(),
            "metricShortId": t.array(t.proxy(renames["MetricShortIdOut"])).optional(),
            "leaseExpireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkItemServiceStateOut"])
    types["DebugOptionsIn"] = t.struct(
        {"enableHotKeyLogging": t.boolean().optional()}
    ).named(renames["DebugOptionsIn"])
    types["DebugOptionsOut"] = t.struct(
        {
            "enableHotKeyLogging": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DebugOptionsOut"])
    types["FlexTemplateRuntimeEnvironmentIn"] = t.struct(
        {
            "autoscalingAlgorithm": t.string().optional(),
            "maxWorkers": t.integer().optional(),
            "flexrsGoal": t.string().optional(),
            "zone": t.string().optional(),
            "workerZone": t.string().optional(),
            "subnetwork": t.string().optional(),
            "sdkContainerImage": t.string().optional(),
            "saveHeapDumpsToGcsPath": t.string().optional(),
            "diskSizeGb": t.integer().optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "stagingLocation": t.string().optional(),
            "numWorkers": t.integer().optional(),
            "serviceAccountEmail": t.string().optional(),
            "workerRegion": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "ipConfiguration": t.string().optional(),
            "tempLocation": t.string().optional(),
            "launcherMachineType": t.string().optional(),
            "machineType": t.string().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "dumpHeapOnOom": t.boolean().optional(),
            "enableLauncherVmSerialPortLogging": t.boolean().optional(),
            "network": t.string().optional(),
            "enableStreamingEngine": t.boolean().optional(),
        }
    ).named(renames["FlexTemplateRuntimeEnvironmentIn"])
    types["FlexTemplateRuntimeEnvironmentOut"] = t.struct(
        {
            "autoscalingAlgorithm": t.string().optional(),
            "maxWorkers": t.integer().optional(),
            "flexrsGoal": t.string().optional(),
            "zone": t.string().optional(),
            "workerZone": t.string().optional(),
            "subnetwork": t.string().optional(),
            "sdkContainerImage": t.string().optional(),
            "saveHeapDumpsToGcsPath": t.string().optional(),
            "diskSizeGb": t.integer().optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "stagingLocation": t.string().optional(),
            "numWorkers": t.integer().optional(),
            "serviceAccountEmail": t.string().optional(),
            "workerRegion": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "ipConfiguration": t.string().optional(),
            "tempLocation": t.string().optional(),
            "launcherMachineType": t.string().optional(),
            "machineType": t.string().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "dumpHeapOnOom": t.boolean().optional(),
            "enableLauncherVmSerialPortLogging": t.boolean().optional(),
            "network": t.string().optional(),
            "enableStreamingEngine": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FlexTemplateRuntimeEnvironmentOut"])
    types["StreamingSetupTaskIn"] = t.struct(
        {
            "receiveWorkPort": t.integer().optional(),
            "streamingComputationTopology": t.proxy(
                renames["TopologyConfigIn"]
            ).optional(),
            "workerHarnessPort": t.integer().optional(),
            "snapshotConfig": t.proxy(
                renames["StreamingApplianceSnapshotConfigIn"]
            ).optional(),
            "drain": t.boolean().optional(),
        }
    ).named(renames["StreamingSetupTaskIn"])
    types["StreamingSetupTaskOut"] = t.struct(
        {
            "receiveWorkPort": t.integer().optional(),
            "streamingComputationTopology": t.proxy(
                renames["TopologyConfigOut"]
            ).optional(),
            "workerHarnessPort": t.integer().optional(),
            "snapshotConfig": t.proxy(
                renames["StreamingApplianceSnapshotConfigOut"]
            ).optional(),
            "drain": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingSetupTaskOut"])
    types["SeqMapTaskIn"] = t.struct(
        {
            "outputInfos": t.array(
                t.proxy(renames["SeqMapTaskOutputInfoIn"])
            ).optional(),
            "systemName": t.string().optional(),
            "name": t.string().optional(),
            "inputs": t.array(t.proxy(renames["SideInputInfoIn"])).optional(),
            "userFn": t.struct({"_": t.string().optional()}).optional(),
            "stageName": t.string().optional(),
        }
    ).named(renames["SeqMapTaskIn"])
    types["SeqMapTaskOut"] = t.struct(
        {
            "outputInfos": t.array(
                t.proxy(renames["SeqMapTaskOutputInfoOut"])
            ).optional(),
            "systemName": t.string().optional(),
            "name": t.string().optional(),
            "inputs": t.array(t.proxy(renames["SideInputInfoOut"])).optional(),
            "userFn": t.struct({"_": t.string().optional()}).optional(),
            "stageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SeqMapTaskOut"])
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
    types["DeleteSnapshotResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteSnapshotResponseIn"]
    )
    types["DeleteSnapshotResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteSnapshotResponseOut"])
    types["CounterStructuredNameIn"] = t.struct(
        {
            "componentStepName": t.string().optional(),
            "originalStepName": t.string().optional(),
            "originNamespace": t.string().optional(),
            "name": t.string().optional(),
            "workerId": t.string().optional(),
            "originalRequestingStepName": t.string().optional(),
            "executionStepName": t.string().optional(),
            "origin": t.string().optional(),
            "portion": t.string().optional(),
            "inputIndex": t.integer().optional(),
        }
    ).named(renames["CounterStructuredNameIn"])
    types["CounterStructuredNameOut"] = t.struct(
        {
            "componentStepName": t.string().optional(),
            "originalStepName": t.string().optional(),
            "originNamespace": t.string().optional(),
            "name": t.string().optional(),
            "workerId": t.string().optional(),
            "originalRequestingStepName": t.string().optional(),
            "executionStepName": t.string().optional(),
            "origin": t.string().optional(),
            "portion": t.string().optional(),
            "inputIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CounterStructuredNameOut"])
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
    types["MultiOutputInfoIn"] = t.struct({"tag": t.string().optional()}).named(
        renames["MultiOutputInfoIn"]
    )
    types["MultiOutputInfoOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultiOutputInfoOut"])
    types["SourceOperationRequestIn"] = t.struct(
        {
            "systemName": t.string().optional(),
            "name": t.string().optional(),
            "stageName": t.string().optional(),
            "split": t.proxy(renames["SourceSplitRequestIn"]).optional(),
            "originalName": t.string().optional(),
            "getMetadata": t.proxy(renames["SourceGetMetadataRequestIn"]).optional(),
        }
    ).named(renames["SourceOperationRequestIn"])
    types["SourceOperationRequestOut"] = t.struct(
        {
            "systemName": t.string().optional(),
            "name": t.string().optional(),
            "stageName": t.string().optional(),
            "split": t.proxy(renames["SourceSplitRequestOut"]).optional(),
            "originalName": t.string().optional(),
            "getMetadata": t.proxy(renames["SourceGetMetadataRequestOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOperationRequestOut"])
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
    types["SdkHarnessContainerImageIn"] = t.struct(
        {
            "containerImage": t.string().optional(),
            "useSingleCorePerContainer": t.boolean().optional(),
            "environmentId": t.string().optional(),
            "capabilities": t.array(t.string()).optional(),
        }
    ).named(renames["SdkHarnessContainerImageIn"])
    types["SdkHarnessContainerImageOut"] = t.struct(
        {
            "containerImage": t.string().optional(),
            "useSingleCorePerContainer": t.boolean().optional(),
            "environmentId": t.string().optional(),
            "capabilities": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SdkHarnessContainerImageOut"])
    types["StragglerSummaryIn"] = t.struct(
        {
            "stragglerCauseCount": t.struct({"_": t.string().optional()}).optional(),
            "recentStragglers": t.array(t.proxy(renames["StragglerIn"])).optional(),
            "totalStragglerCount": t.string().optional(),
        }
    ).named(renames["StragglerSummaryIn"])
    types["StragglerSummaryOut"] = t.struct(
        {
            "stragglerCauseCount": t.struct({"_": t.string().optional()}).optional(),
            "recentStragglers": t.array(t.proxy(renames["StragglerOut"])).optional(),
            "totalStragglerCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StragglerSummaryOut"])
    types["ListJobsResponseIn"] = t.struct(
        {
            "jobs": t.array(t.proxy(renames["JobIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "failedLocation": t.array(t.proxy(renames["FailedLocationIn"])).optional(),
        }
    ).named(renames["ListJobsResponseIn"])
    types["ListJobsResponseOut"] = t.struct(
        {
            "jobs": t.array(t.proxy(renames["JobOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "failedLocation": t.array(t.proxy(renames["FailedLocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobsResponseOut"])
    types["RuntimeEnvironmentIn"] = t.struct(
        {
            "bypassTempDirValidation": t.boolean().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "enableStreamingEngine": t.boolean().optional(),
            "numWorkers": t.integer().optional(),
            "tempLocation": t.string(),
            "additionalExperiments": t.array(t.string()).optional(),
            "zone": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "machineType": t.string().optional(),
            "subnetwork": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "workerRegion": t.string(),
            "workerZone": t.string().optional(),
            "ipConfiguration": t.string().optional(),
            "network": t.string().optional(),
            "maxWorkers": t.integer().optional(),
        }
    ).named(renames["RuntimeEnvironmentIn"])
    types["RuntimeEnvironmentOut"] = t.struct(
        {
            "bypassTempDirValidation": t.boolean().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "enableStreamingEngine": t.boolean().optional(),
            "numWorkers": t.integer().optional(),
            "tempLocation": t.string(),
            "additionalExperiments": t.array(t.string()).optional(),
            "zone": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "machineType": t.string().optional(),
            "subnetwork": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "workerRegion": t.string(),
            "workerZone": t.string().optional(),
            "ipConfiguration": t.string().optional(),
            "network": t.string().optional(),
            "maxWorkers": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeEnvironmentOut"])
    types["ResourceUtilizationReportResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ResourceUtilizationReportResponseIn"])
    types["ResourceUtilizationReportResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResourceUtilizationReportResponseOut"])
    types["WorkerMessageIn"] = t.struct(
        {
            "workerHealthReport": t.proxy(renames["WorkerHealthReportIn"]).optional(),
            "workerLifecycleEvent": t.proxy(
                renames["WorkerLifecycleEventIn"]
            ).optional(),
            "workerShutdownNotice": t.proxy(
                renames["WorkerShutdownNoticeIn"]
            ).optional(),
            "workerMetrics": t.proxy(renames["ResourceUtilizationReportIn"]).optional(),
            "workerThreadScalingReport": t.proxy(
                renames["WorkerThreadScalingReportIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "workerMessageCode": t.proxy(renames["WorkerMessageCodeIn"]).optional(),
            "time": t.string().optional(),
        }
    ).named(renames["WorkerMessageIn"])
    types["WorkerMessageOut"] = t.struct(
        {
            "workerHealthReport": t.proxy(renames["WorkerHealthReportOut"]).optional(),
            "workerLifecycleEvent": t.proxy(
                renames["WorkerLifecycleEventOut"]
            ).optional(),
            "workerShutdownNotice": t.proxy(
                renames["WorkerShutdownNoticeOut"]
            ).optional(),
            "workerMetrics": t.proxy(
                renames["ResourceUtilizationReportOut"]
            ).optional(),
            "workerThreadScalingReport": t.proxy(
                renames["WorkerThreadScalingReportOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "workerMessageCode": t.proxy(renames["WorkerMessageCodeOut"]).optional(),
            "time": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerMessageOut"])
    types["RuntimeMetadataIn"] = t.struct(
        {
            "parameters": t.array(t.proxy(renames["ParameterMetadataIn"])).optional(),
            "sdkInfo": t.proxy(renames["SDKInfoIn"]).optional(),
        }
    ).named(renames["RuntimeMetadataIn"])
    types["RuntimeMetadataOut"] = t.struct(
        {
            "parameters": t.array(t.proxy(renames["ParameterMetadataOut"])).optional(),
            "sdkInfo": t.proxy(renames["SDKInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeMetadataOut"])
    types["SideInputInfoIn"] = t.struct(
        {
            "tag": t.string().optional(),
            "sources": t.array(t.proxy(renames["SourceIn"])).optional(),
            "kind": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SideInputInfoIn"])
    types["SideInputInfoOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "kind": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SideInputInfoOut"])
    types["JobIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "replaceJobId": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "requestedState": t.string().optional(),
            "jobMetadata": t.proxy(renames["JobMetadataIn"]).optional(),
            "stepsLocation": t.string().optional(),
            "runtimeUpdatableParams": t.proxy(
                renames["RuntimeUpdatableParamsIn"]
            ).optional(),
            "steps": t.array(t.proxy(renames["StepIn"])).optional(),
            "tempFiles": t.array(t.string()).optional(),
            "environment": t.proxy(renames["EnvironmentIn"]).optional(),
            "projectId": t.string().optional(),
            "stageStates": t.array(
                t.proxy(renames["ExecutionStageStateIn"])
            ).optional(),
            "createdFromSnapshotId": t.string().optional(),
            "currentStateTime": t.string().optional(),
            "currentState": t.string().optional(),
            "location": t.string().optional(),
            "type": t.string().optional(),
            "createTime": t.string().optional(),
            "clientRequestId": t.string().optional(),
            "pipelineDescription": t.proxy(renames["PipelineDescriptionIn"]).optional(),
            "executionInfo": t.proxy(renames["JobExecutionInfoIn"]).optional(),
            "replacedByJobId": t.string().optional(),
            "startTime": t.string().optional(),
            "transformNameMapping": t.struct({"_": t.string().optional()}).optional(),
            "satisfiesPzs": t.boolean().optional(),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "replaceJobId": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "requestedState": t.string().optional(),
            "jobMetadata": t.proxy(renames["JobMetadataOut"]).optional(),
            "stepsLocation": t.string().optional(),
            "runtimeUpdatableParams": t.proxy(
                renames["RuntimeUpdatableParamsOut"]
            ).optional(),
            "steps": t.array(t.proxy(renames["StepOut"])).optional(),
            "tempFiles": t.array(t.string()).optional(),
            "environment": t.proxy(renames["EnvironmentOut"]).optional(),
            "projectId": t.string().optional(),
            "stageStates": t.array(
                t.proxy(renames["ExecutionStageStateOut"])
            ).optional(),
            "createdFromSnapshotId": t.string().optional(),
            "currentStateTime": t.string().optional(),
            "currentState": t.string().optional(),
            "location": t.string().optional(),
            "type": t.string().optional(),
            "createTime": t.string().optional(),
            "clientRequestId": t.string().optional(),
            "pipelineDescription": t.proxy(
                renames["PipelineDescriptionOut"]
            ).optional(),
            "executionInfo": t.proxy(renames["JobExecutionInfoOut"]).optional(),
            "replacedByJobId": t.string().optional(),
            "startTime": t.string().optional(),
            "transformNameMapping": t.struct({"_": t.string().optional()}).optional(),
            "satisfiesPzs": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
    types["StreamingComputationRangesIn"] = t.struct(
        {
            "computationId": t.string().optional(),
            "rangeAssignments": t.array(
                t.proxy(renames["KeyRangeDataDiskAssignmentIn"])
            ).optional(),
        }
    ).named(renames["StreamingComputationRangesIn"])
    types["StreamingComputationRangesOut"] = t.struct(
        {
            "computationId": t.string().optional(),
            "rangeAssignments": t.array(
                t.proxy(renames["KeyRangeDataDiskAssignmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingComputationRangesOut"])
    types["MemInfoIn"] = t.struct(
        {
            "timestamp": t.string().optional(),
            "currentOoms": t.string().optional(),
            "totalGbMs": t.string().optional(),
            "currentRssBytes": t.string().optional(),
            "currentLimitBytes": t.string().optional(),
        }
    ).named(renames["MemInfoIn"])
    types["MemInfoOut"] = t.struct(
        {
            "timestamp": t.string().optional(),
            "currentOoms": t.string().optional(),
            "totalGbMs": t.string().optional(),
            "currentRssBytes": t.string().optional(),
            "currentLimitBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemInfoOut"])
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
    types["DataDiskAssignmentIn"] = t.struct(
        {
            "dataDisks": t.array(t.string()).optional(),
            "vmInstance": t.string().optional(),
        }
    ).named(renames["DataDiskAssignmentIn"])
    types["DataDiskAssignmentOut"] = t.struct(
        {
            "dataDisks": t.array(t.string()).optional(),
            "vmInstance": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataDiskAssignmentOut"])
    types["SourceGetMetadataResponseIn"] = t.struct(
        {"metadata": t.proxy(renames["SourceMetadataIn"]).optional()}
    ).named(renames["SourceGetMetadataResponseIn"])
    types["SourceGetMetadataResponseOut"] = t.struct(
        {
            "metadata": t.proxy(renames["SourceMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceGetMetadataResponseOut"])
    types["StructuredMessageIn"] = t.struct(
        {
            "messageText": t.string().optional(),
            "messageKey": t.string().optional(),
            "parameters": t.array(t.proxy(renames["ParameterIn"])).optional(),
        }
    ).named(renames["StructuredMessageIn"])
    types["StructuredMessageOut"] = t.struct(
        {
            "messageText": t.string().optional(),
            "messageKey": t.string().optional(),
            "parameters": t.array(t.proxy(renames["ParameterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructuredMessageOut"])
    types["SourceSplitResponseIn"] = t.struct(
        {
            "shards": t.array(t.proxy(renames["SourceSplitShardIn"])).optional(),
            "outcome": t.string().optional(),
            "bundles": t.array(t.proxy(renames["DerivedSourceIn"])).optional(),
        }
    ).named(renames["SourceSplitResponseIn"])
    types["SourceSplitResponseOut"] = t.struct(
        {
            "shards": t.array(t.proxy(renames["SourceSplitShardOut"])).optional(),
            "outcome": t.string().optional(),
            "bundles": t.array(t.proxy(renames["DerivedSourceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceSplitResponseOut"])
    types["WorkerHealthReportResponseIn"] = t.struct(
        {"reportInterval": t.string().optional()}
    ).named(renames["WorkerHealthReportResponseIn"])
    types["WorkerHealthReportResponseOut"] = t.struct(
        {
            "reportInterval": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerHealthReportResponseOut"])
    types["ParallelInstructionIn"] = t.struct(
        {
            "originalName": t.string().optional(),
            "read": t.proxy(renames["ReadInstructionIn"]).optional(),
            "partialGroupByKey": t.proxy(
                renames["PartialGroupByKeyInstructionIn"]
            ).optional(),
            "systemName": t.string().optional(),
            "parDo": t.proxy(renames["ParDoInstructionIn"]).optional(),
            "name": t.string().optional(),
            "write": t.proxy(renames["WriteInstructionIn"]).optional(),
            "flatten": t.proxy(renames["FlattenInstructionIn"]).optional(),
            "outputs": t.array(t.proxy(renames["InstructionOutputIn"])).optional(),
        }
    ).named(renames["ParallelInstructionIn"])
    types["ParallelInstructionOut"] = t.struct(
        {
            "originalName": t.string().optional(),
            "read": t.proxy(renames["ReadInstructionOut"]).optional(),
            "partialGroupByKey": t.proxy(
                renames["PartialGroupByKeyInstructionOut"]
            ).optional(),
            "systemName": t.string().optional(),
            "parDo": t.proxy(renames["ParDoInstructionOut"]).optional(),
            "name": t.string().optional(),
            "write": t.proxy(renames["WriteInstructionOut"]).optional(),
            "flatten": t.proxy(renames["FlattenInstructionOut"]).optional(),
            "outputs": t.array(t.proxy(renames["InstructionOutputOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParallelInstructionOut"])
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
    types["CreateJobFromTemplateRequestIn"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "location": t.string().optional(),
            "jobName": t.string(),
            "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
            "gcsPath": t.string(),
        }
    ).named(renames["CreateJobFromTemplateRequestIn"])
    types["CreateJobFromTemplateRequestOut"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "location": t.string().optional(),
            "jobName": t.string(),
            "environment": t.proxy(renames["RuntimeEnvironmentOut"]).optional(),
            "gcsPath": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateJobFromTemplateRequestOut"])
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
    types["ApproximateReportedProgressIn"] = t.struct(
        {
            "remainingParallelism": t.proxy(
                renames["ReportedParallelismIn"]
            ).optional(),
            "position": t.proxy(renames["PositionIn"]).optional(),
            "consumedParallelism": t.proxy(renames["ReportedParallelismIn"]).optional(),
            "fractionConsumed": t.number().optional(),
        }
    ).named(renames["ApproximateReportedProgressIn"])
    types["ApproximateReportedProgressOut"] = t.struct(
        {
            "remainingParallelism": t.proxy(
                renames["ReportedParallelismOut"]
            ).optional(),
            "position": t.proxy(renames["PositionOut"]).optional(),
            "consumedParallelism": t.proxy(
                renames["ReportedParallelismOut"]
            ).optional(),
            "fractionConsumed": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApproximateReportedProgressOut"])
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
    types["HistogramIn"] = t.struct(
        {
            "firstBucketOffset": t.integer().optional(),
            "bucketCounts": t.array(t.string()).optional(),
        }
    ).named(renames["HistogramIn"])
    types["HistogramOut"] = t.struct(
        {
            "firstBucketOffset": t.integer().optional(),
            "bucketCounts": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistogramOut"])
    types["PipelineDescriptionIn"] = t.struct(
        {
            "executionPipelineStage": t.array(
                t.proxy(renames["ExecutionStageSummaryIn"])
            ).optional(),
            "originalPipelineTransform": t.array(
                t.proxy(renames["TransformSummaryIn"])
            ).optional(),
            "displayData": t.array(t.proxy(renames["DisplayDataIn"])).optional(),
            "stepNamesHash": t.string().optional(),
        }
    ).named(renames["PipelineDescriptionIn"])
    types["PipelineDescriptionOut"] = t.struct(
        {
            "executionPipelineStage": t.array(
                t.proxy(renames["ExecutionStageSummaryOut"])
            ).optional(),
            "originalPipelineTransform": t.array(
                t.proxy(renames["TransformSummaryOut"])
            ).optional(),
            "displayData": t.array(t.proxy(renames["DisplayDataOut"])).optional(),
            "stepNamesHash": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PipelineDescriptionOut"])
    types["ComponentSourceIn"] = t.struct(
        {
            "originalTransformOrCollection": t.string().optional(),
            "name": t.string().optional(),
            "userName": t.string().optional(),
        }
    ).named(renames["ComponentSourceIn"])
    types["ComponentSourceOut"] = t.struct(
        {
            "originalTransformOrCollection": t.string().optional(),
            "name": t.string().optional(),
            "userName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComponentSourceOut"])
    types["InstructionInputIn"] = t.struct(
        {
            "producerInstructionIndex": t.integer().optional(),
            "outputNum": t.integer().optional(),
        }
    ).named(renames["InstructionInputIn"])
    types["InstructionInputOut"] = t.struct(
        {
            "producerInstructionIndex": t.integer().optional(),
            "outputNum": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstructionInputOut"])
    types["SdkVersionIn"] = t.struct(
        {
            "sdkSupportStatus": t.string().optional(),
            "version": t.string().optional(),
            "versionDisplayName": t.string().optional(),
        }
    ).named(renames["SdkVersionIn"])
    types["SdkVersionOut"] = t.struct(
        {
            "sdkSupportStatus": t.string().optional(),
            "version": t.string().optional(),
            "versionDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SdkVersionOut"])
    types["DistributionUpdateIn"] = t.struct(
        {
            "sumOfSquares": t.number().optional(),
            "histogram": t.proxy(renames["HistogramIn"]).optional(),
            "max": t.proxy(renames["SplitInt64In"]).optional(),
            "count": t.proxy(renames["SplitInt64In"]).optional(),
            "min": t.proxy(renames["SplitInt64In"]).optional(),
            "sum": t.proxy(renames["SplitInt64In"]).optional(),
        }
    ).named(renames["DistributionUpdateIn"])
    types["DistributionUpdateOut"] = t.struct(
        {
            "sumOfSquares": t.number().optional(),
            "histogram": t.proxy(renames["HistogramOut"]).optional(),
            "max": t.proxy(renames["SplitInt64Out"]).optional(),
            "count": t.proxy(renames["SplitInt64Out"]).optional(),
            "min": t.proxy(renames["SplitInt64Out"]).optional(),
            "sum": t.proxy(renames["SplitInt64Out"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DistributionUpdateOut"])
    types["LaunchTemplateParametersIn"] = t.struct(
        {
            "transformNameMapping": t.struct({"_": t.string().optional()}).optional(),
            "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
            "jobName": t.string(),
            "update": t.boolean().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LaunchTemplateParametersIn"])
    types["LaunchTemplateParametersOut"] = t.struct(
        {
            "transformNameMapping": t.struct({"_": t.string().optional()}).optional(),
            "environment": t.proxy(renames["RuntimeEnvironmentOut"]).optional(),
            "jobName": t.string(),
            "update": t.boolean().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LaunchTemplateParametersOut"])
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
    types["ParameterIn"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ParameterIn"])
    types["ParameterOut"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParameterOut"])
    types["CPUTimeIn"] = t.struct(
        {
            "timestamp": t.string().optional(),
            "rate": t.number().optional(),
            "totalMs": t.string().optional(),
        }
    ).named(renames["CPUTimeIn"])
    types["CPUTimeOut"] = t.struct(
        {
            "timestamp": t.string().optional(),
            "rate": t.number().optional(),
            "totalMs": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CPUTimeOut"])
    types["StageSourceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "userName": t.string().optional(),
            "originalTransformOrCollection": t.string().optional(),
        }
    ).named(renames["StageSourceIn"])
    types["StageSourceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "userName": t.string().optional(),
            "originalTransformOrCollection": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StageSourceOut"])
    types["SourceGetMetadataRequestIn"] = t.struct(
        {"source": t.proxy(renames["SourceIn"]).optional()}
    ).named(renames["SourceGetMetadataRequestIn"])
    types["SourceGetMetadataRequestOut"] = t.struct(
        {
            "source": t.proxy(renames["SourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceGetMetadataRequestOut"])
    types["StreamingComputationConfigIn"] = t.struct(
        {
            "stageName": t.string().optional(),
            "instructions": t.array(
                t.proxy(renames["ParallelInstructionIn"])
            ).optional(),
            "computationId": t.string().optional(),
            "transformUserNameToStateFamily": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "systemName": t.string().optional(),
        }
    ).named(renames["StreamingComputationConfigIn"])
    types["StreamingComputationConfigOut"] = t.struct(
        {
            "stageName": t.string().optional(),
            "instructions": t.array(
                t.proxy(renames["ParallelInstructionOut"])
            ).optional(),
            "computationId": t.string().optional(),
            "transformUserNameToStateFamily": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "systemName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingComputationConfigOut"])
    types["AutoscalingEventIn"] = t.struct(
        {
            "eventType": t.string().optional(),
            "workerPool": t.string().optional(),
            "currentNumWorkers": t.string().optional(),
            "targetNumWorkers": t.string().optional(),
            "time": t.string().optional(),
            "description": t.proxy(renames["StructuredMessageIn"]).optional(),
        }
    ).named(renames["AutoscalingEventIn"])
    types["AutoscalingEventOut"] = t.struct(
        {
            "eventType": t.string().optional(),
            "workerPool": t.string().optional(),
            "currentNumWorkers": t.string().optional(),
            "targetNumWorkers": t.string().optional(),
            "time": t.string().optional(),
            "description": t.proxy(renames["StructuredMessageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoscalingEventOut"])
    types["JobMessageIn"] = t.struct(
        {
            "messageText": t.string().optional(),
            "time": t.string().optional(),
            "id": t.string().optional(),
            "messageImportance": t.string().optional(),
        }
    ).named(renames["JobMessageIn"])
    types["JobMessageOut"] = t.struct(
        {
            "messageText": t.string().optional(),
            "time": t.string().optional(),
            "id": t.string().optional(),
            "messageImportance": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobMessageOut"])
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
    types["SnapshotIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "id": t.string().optional(),
            "sourceJobId": t.string().optional(),
            "diskSizeBytes": t.string().optional(),
            "ttl": t.string().optional(),
            "creationTime": t.string().optional(),
            "pubsubMetadata": t.array(
                t.proxy(renames["PubsubSnapshotMetadataIn"])
            ).optional(),
            "state": t.string().optional(),
            "region": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["SnapshotIn"])
    types["SnapshotOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "id": t.string().optional(),
            "sourceJobId": t.string().optional(),
            "diskSizeBytes": t.string().optional(),
            "ttl": t.string().optional(),
            "creationTime": t.string().optional(),
            "pubsubMetadata": t.array(
                t.proxy(renames["PubsubSnapshotMetadataOut"])
            ).optional(),
            "state": t.string().optional(),
            "region": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnapshotOut"])
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
    types["PubsubLocationIn"] = t.struct(
        {
            "subscription": t.string().optional(),
            "idLabel": t.string().optional(),
            "withAttributes": t.boolean().optional(),
            "trackingSubscription": t.string().optional(),
            "timestampLabel": t.string().optional(),
            "dropLateData": t.boolean().optional(),
            "topic": t.string().optional(),
        }
    ).named(renames["PubsubLocationIn"])
    types["PubsubLocationOut"] = t.struct(
        {
            "subscription": t.string().optional(),
            "idLabel": t.string().optional(),
            "withAttributes": t.boolean().optional(),
            "trackingSubscription": t.string().optional(),
            "timestampLabel": t.string().optional(),
            "dropLateData": t.boolean().optional(),
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubLocationOut"])
    types["FileIODetailsIn"] = t.struct({"filePattern": t.string().optional()}).named(
        renames["FileIODetailsIn"]
    )
    types["FileIODetailsOut"] = t.struct(
        {
            "filePattern": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileIODetailsOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["SendDebugCaptureRequestIn"] = t.struct(
        {
            "data": t.string().optional(),
            "componentId": t.string().optional(),
            "workerId": t.string().optional(),
            "dataFormat": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["SendDebugCaptureRequestIn"])
    types["SendDebugCaptureRequestOut"] = t.struct(
        {
            "data": t.string().optional(),
            "componentId": t.string().optional(),
            "workerId": t.string().optional(),
            "dataFormat": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SendDebugCaptureRequestOut"])
    types["GetTemplateResponseIn"] = t.struct(
        {
            "status": t.proxy(renames["StatusIn"]).optional(),
            "templateType": t.string().optional(),
            "runtimeMetadata": t.proxy(renames["RuntimeMetadataIn"]).optional(),
            "metadata": t.proxy(renames["TemplateMetadataIn"]).optional(),
        }
    ).named(renames["GetTemplateResponseIn"])
    types["GetTemplateResponseOut"] = t.struct(
        {
            "status": t.proxy(renames["StatusOut"]).optional(),
            "templateType": t.string().optional(),
            "runtimeMetadata": t.proxy(renames["RuntimeMetadataOut"]).optional(),
            "metadata": t.proxy(renames["TemplateMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetTemplateResponseOut"])
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
    types["IntegerMeanIn"] = t.struct(
        {
            "sum": t.proxy(renames["SplitInt64In"]).optional(),
            "count": t.proxy(renames["SplitInt64In"]).optional(),
        }
    ).named(renames["IntegerMeanIn"])
    types["IntegerMeanOut"] = t.struct(
        {
            "sum": t.proxy(renames["SplitInt64Out"]).optional(),
            "count": t.proxy(renames["SplitInt64Out"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerMeanOut"])
    types["TopologyConfigIn"] = t.struct(
        {
            "persistentStateVersion": t.integer().optional(),
            "forwardingKeyBits": t.integer().optional(),
            "userStageToComputationNameMap": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "dataDiskAssignments": t.array(
                t.proxy(renames["DataDiskAssignmentIn"])
            ).optional(),
            "computations": t.array(
                t.proxy(renames["ComputationTopologyIn"])
            ).optional(),
        }
    ).named(renames["TopologyConfigIn"])
    types["TopologyConfigOut"] = t.struct(
        {
            "persistentStateVersion": t.integer().optional(),
            "forwardingKeyBits": t.integer().optional(),
            "userStageToComputationNameMap": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "dataDiskAssignments": t.array(
                t.proxy(renames["DataDiskAssignmentOut"])
            ).optional(),
            "computations": t.array(
                t.proxy(renames["ComputationTopologyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TopologyConfigOut"])
    types["HotKeyDebuggingInfoIn"] = t.struct(
        {"detectedHotKeys": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["HotKeyDebuggingInfoIn"])
    types["HotKeyDebuggingInfoOut"] = t.struct(
        {
            "detectedHotKeys": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HotKeyDebuggingInfoOut"])
    types["HotKeyDetectionIn"] = t.struct(
        {
            "userStepName": t.string().optional(),
            "hotKeyAge": t.string().optional(),
            "systemName": t.string().optional(),
        }
    ).named(renames["HotKeyDetectionIn"])
    types["HotKeyDetectionOut"] = t.struct(
        {
            "userStepName": t.string().optional(),
            "hotKeyAge": t.string().optional(),
            "systemName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HotKeyDetectionOut"])
    types["PubSubIODetailsIn"] = t.struct(
        {"subscription": t.string().optional(), "topic": t.string().optional()}
    ).named(renames["PubSubIODetailsIn"])
    types["PubSubIODetailsOut"] = t.struct(
        {
            "subscription": t.string().optional(),
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubSubIODetailsOut"])
    types["MountedDataDiskIn"] = t.struct({"dataDisk": t.string().optional()}).named(
        renames["MountedDataDiskIn"]
    )
    types["MountedDataDiskOut"] = t.struct(
        {
            "dataDisk": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MountedDataDiskOut"])
    types["MapTaskIn"] = t.struct(
        {
            "systemName": t.string().optional(),
            "stageName": t.string().optional(),
            "counterPrefix": t.string().optional(),
            "instructions": t.array(
                t.proxy(renames["ParallelInstructionIn"])
            ).optional(),
        }
    ).named(renames["MapTaskIn"])
    types["MapTaskOut"] = t.struct(
        {
            "systemName": t.string().optional(),
            "stageName": t.string().optional(),
            "counterPrefix": t.string().optional(),
            "instructions": t.array(
                t.proxy(renames["ParallelInstructionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MapTaskOut"])
    types["SDKInfoIn"] = t.struct(
        {"language": t.string(), "version": t.string().optional()}
    ).named(renames["SDKInfoIn"])
    types["SDKInfoOut"] = t.struct(
        {
            "language": t.string(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SDKInfoOut"])
    types["StageSummaryIn"] = t.struct(
        {
            "stageId": t.string().optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricUpdateIn"])).optional(),
            "progress": t.proxy(renames["ProgressTimeseriesIn"]).optional(),
            "stragglerSummary": t.proxy(renames["StragglerSummaryIn"]).optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["StageSummaryIn"])
    types["StageSummaryOut"] = t.struct(
        {
            "stageId": t.string().optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricUpdateOut"])).optional(),
            "progress": t.proxy(renames["ProgressTimeseriesOut"]).optional(),
            "stragglerSummary": t.proxy(renames["StragglerSummaryOut"]).optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StageSummaryOut"])
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
    types["WorkItemStatusIn"] = t.struct(
        {
            "progress": t.proxy(renames["ApproximateProgressIn"]).optional(),
            "sourceFork": t.proxy(renames["SourceForkIn"]).optional(),
            "totalThrottlerWaitTimeSeconds": t.number().optional(),
            "counterUpdates": t.array(t.proxy(renames["CounterUpdateIn"])).optional(),
            "reportIndex": t.string().optional(),
            "workItemId": t.string().optional(),
            "dynamicSourceSplit": t.proxy(renames["DynamicSourceSplitIn"]).optional(),
            "requestedLeaseDuration": t.string().optional(),
            "metricUpdates": t.array(t.proxy(renames["MetricUpdateIn"])).optional(),
            "completed": t.boolean().optional(),
            "stopPosition": t.proxy(renames["PositionIn"]).optional(),
            "errors": t.array(t.proxy(renames["StatusIn"])).optional(),
            "reportedProgress": t.proxy(
                renames["ApproximateReportedProgressIn"]
            ).optional(),
            "sourceOperationResponse": t.proxy(
                renames["SourceOperationResponseIn"]
            ).optional(),
        }
    ).named(renames["WorkItemStatusIn"])
    types["WorkItemStatusOut"] = t.struct(
        {
            "progress": t.proxy(renames["ApproximateProgressOut"]).optional(),
            "sourceFork": t.proxy(renames["SourceForkOut"]).optional(),
            "totalThrottlerWaitTimeSeconds": t.number().optional(),
            "counterUpdates": t.array(t.proxy(renames["CounterUpdateOut"])).optional(),
            "reportIndex": t.string().optional(),
            "workItemId": t.string().optional(),
            "dynamicSourceSplit": t.proxy(renames["DynamicSourceSplitOut"]).optional(),
            "requestedLeaseDuration": t.string().optional(),
            "metricUpdates": t.array(t.proxy(renames["MetricUpdateOut"])).optional(),
            "completed": t.boolean().optional(),
            "stopPosition": t.proxy(renames["PositionOut"]).optional(),
            "errors": t.array(t.proxy(renames["StatusOut"])).optional(),
            "reportedProgress": t.proxy(
                renames["ApproximateReportedProgressOut"]
            ).optional(),
            "sourceOperationResponse": t.proxy(
                renames["SourceOperationResponseOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkItemStatusOut"])
    types["LaunchFlexTemplateParameterIn"] = t.struct(
        {
            "containerSpecGcsPath": t.string().optional(),
            "jobName": t.string(),
            "transformNameMappings": t.struct({"_": t.string().optional()}).optional(),
            "environment": t.proxy(
                renames["FlexTemplateRuntimeEnvironmentIn"]
            ).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "update": t.boolean().optional(),
            "launchOptions": t.struct({"_": t.string().optional()}).optional(),
            "containerSpec": t.proxy(renames["ContainerSpecIn"]).optional(),
        }
    ).named(renames["LaunchFlexTemplateParameterIn"])
    types["LaunchFlexTemplateParameterOut"] = t.struct(
        {
            "containerSpecGcsPath": t.string().optional(),
            "jobName": t.string(),
            "transformNameMappings": t.struct({"_": t.string().optional()}).optional(),
            "environment": t.proxy(
                renames["FlexTemplateRuntimeEnvironmentOut"]
            ).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "update": t.boolean().optional(),
            "launchOptions": t.struct({"_": t.string().optional()}).optional(),
            "containerSpec": t.proxy(renames["ContainerSpecOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LaunchFlexTemplateParameterOut"])
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
    types["ParDoInstructionIn"] = t.struct(
        {
            "multiOutputInfos": t.array(
                t.proxy(renames["MultiOutputInfoIn"])
            ).optional(),
            "sideInputs": t.array(t.proxy(renames["SideInputInfoIn"])).optional(),
            "numOutputs": t.integer().optional(),
            "userFn": t.struct({"_": t.string().optional()}).optional(),
            "input": t.proxy(renames["InstructionInputIn"]).optional(),
        }
    ).named(renames["ParDoInstructionIn"])
    types["ParDoInstructionOut"] = t.struct(
        {
            "multiOutputInfos": t.array(
                t.proxy(renames["MultiOutputInfoOut"])
            ).optional(),
            "sideInputs": t.array(t.proxy(renames["SideInputInfoOut"])).optional(),
            "numOutputs": t.integer().optional(),
            "userFn": t.struct({"_": t.string().optional()}).optional(),
            "input": t.proxy(renames["InstructionInputOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParDoInstructionOut"])
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
    types["StreamingStageLocationIn"] = t.struct(
        {"streamId": t.string().optional()}
    ).named(renames["StreamingStageLocationIn"])
    types["StreamingStageLocationOut"] = t.struct(
        {
            "streamId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingStageLocationOut"])
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
    types["CustomSourceLocationIn"] = t.struct(
        {"stateful": t.boolean().optional()}
    ).named(renames["CustomSourceLocationIn"])
    types["CustomSourceLocationOut"] = t.struct(
        {
            "stateful": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomSourceLocationOut"])
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
    types["MetricStructuredNameIn"] = t.struct(
        {
            "name": t.string().optional(),
            "context": t.struct({"_": t.string().optional()}).optional(),
            "origin": t.string().optional(),
        }
    ).named(renames["MetricStructuredNameIn"])
    types["MetricStructuredNameOut"] = t.struct(
        {
            "name": t.string().optional(),
            "context": t.struct({"_": t.string().optional()}).optional(),
            "origin": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricStructuredNameOut"])
    types["JobMetadataIn"] = t.struct(
        {
            "userDisplayProperties": t.struct({"_": t.string().optional()}).optional(),
            "datastoreDetails": t.array(
                t.proxy(renames["DatastoreIODetailsIn"])
            ).optional(),
            "bigTableDetails": t.array(
                t.proxy(renames["BigTableIODetailsIn"])
            ).optional(),
            "sdkVersion": t.proxy(renames["SdkVersionIn"]).optional(),
            "spannerDetails": t.array(
                t.proxy(renames["SpannerIODetailsIn"])
            ).optional(),
            "pubsubDetails": t.array(t.proxy(renames["PubSubIODetailsIn"])).optional(),
            "bigqueryDetails": t.array(
                t.proxy(renames["BigQueryIODetailsIn"])
            ).optional(),
            "fileDetails": t.array(t.proxy(renames["FileIODetailsIn"])).optional(),
        }
    ).named(renames["JobMetadataIn"])
    types["JobMetadataOut"] = t.struct(
        {
            "userDisplayProperties": t.struct({"_": t.string().optional()}).optional(),
            "datastoreDetails": t.array(
                t.proxy(renames["DatastoreIODetailsOut"])
            ).optional(),
            "bigTableDetails": t.array(
                t.proxy(renames["BigTableIODetailsOut"])
            ).optional(),
            "sdkVersion": t.proxy(renames["SdkVersionOut"]).optional(),
            "spannerDetails": t.array(
                t.proxy(renames["SpannerIODetailsOut"])
            ).optional(),
            "pubsubDetails": t.array(t.proxy(renames["PubSubIODetailsOut"])).optional(),
            "bigqueryDetails": t.array(
                t.proxy(renames["BigQueryIODetailsOut"])
            ).optional(),
            "fileDetails": t.array(t.proxy(renames["FileIODetailsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobMetadataOut"])
    types["IntegerGaugeIn"] = t.struct(
        {
            "value": t.proxy(renames["SplitInt64In"]).optional(),
            "timestamp": t.string().optional(),
        }
    ).named(renames["IntegerGaugeIn"])
    types["IntegerGaugeOut"] = t.struct(
        {
            "value": t.proxy(renames["SplitInt64Out"]).optional(),
            "timestamp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerGaugeOut"])
    types["ComputationTopologyIn"] = t.struct(
        {
            "inputs": t.array(t.proxy(renames["StreamLocationIn"])).optional(),
            "outputs": t.array(t.proxy(renames["StreamLocationIn"])).optional(),
            "systemStageName": t.string().optional(),
            "stateFamilies": t.array(
                t.proxy(renames["StateFamilyConfigIn"])
            ).optional(),
            "keyRanges": t.array(t.proxy(renames["KeyRangeLocationIn"])).optional(),
            "computationId": t.string().optional(),
        }
    ).named(renames["ComputationTopologyIn"])
    types["ComputationTopologyOut"] = t.struct(
        {
            "inputs": t.array(t.proxy(renames["StreamLocationOut"])).optional(),
            "outputs": t.array(t.proxy(renames["StreamLocationOut"])).optional(),
            "systemStageName": t.string().optional(),
            "stateFamilies": t.array(
                t.proxy(renames["StateFamilyConfigOut"])
            ).optional(),
            "keyRanges": t.array(t.proxy(renames["KeyRangeLocationOut"])).optional(),
            "computationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputationTopologyOut"])
    types["IntegerListIn"] = t.struct(
        {"elements": t.array(t.proxy(renames["SplitInt64In"])).optional()}
    ).named(renames["IntegerListIn"])
    types["IntegerListOut"] = t.struct(
        {
            "elements": t.array(t.proxy(renames["SplitInt64Out"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerListOut"])
    types["ApproximateProgressIn"] = t.struct(
        {
            "percentComplete": t.number().optional(),
            "position": t.proxy(renames["PositionIn"]).optional(),
            "remainingTime": t.string().optional(),
        }
    ).named(renames["ApproximateProgressIn"])
    types["ApproximateProgressOut"] = t.struct(
        {
            "percentComplete": t.number().optional(),
            "position": t.proxy(renames["PositionOut"]).optional(),
            "remainingTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApproximateProgressOut"])
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
    types["CounterUpdateIn"] = t.struct(
        {
            "integerList": t.proxy(renames["IntegerListIn"]).optional(),
            "integer": t.proxy(renames["SplitInt64In"]).optional(),
            "floatingPoint": t.number().optional(),
            "floatingPointMean": t.proxy(renames["FloatingPointMeanIn"]).optional(),
            "floatingPointList": t.proxy(renames["FloatingPointListIn"]).optional(),
            "internal": t.struct({"_": t.string().optional()}).optional(),
            "structuredNameAndMetadata": t.proxy(
                renames["CounterStructuredNameAndMetadataIn"]
            ).optional(),
            "distribution": t.proxy(renames["DistributionUpdateIn"]).optional(),
            "boolean": t.boolean().optional(),
            "shortId": t.string().optional(),
            "integerGauge": t.proxy(renames["IntegerGaugeIn"]).optional(),
            "nameAndKind": t.proxy(renames["NameAndKindIn"]).optional(),
            "integerMean": t.proxy(renames["IntegerMeanIn"]).optional(),
            "stringList": t.proxy(renames["StringListIn"]).optional(),
            "cumulative": t.boolean().optional(),
        }
    ).named(renames["CounterUpdateIn"])
    types["CounterUpdateOut"] = t.struct(
        {
            "integerList": t.proxy(renames["IntegerListOut"]).optional(),
            "integer": t.proxy(renames["SplitInt64Out"]).optional(),
            "floatingPoint": t.number().optional(),
            "floatingPointMean": t.proxy(renames["FloatingPointMeanOut"]).optional(),
            "floatingPointList": t.proxy(renames["FloatingPointListOut"]).optional(),
            "internal": t.struct({"_": t.string().optional()}).optional(),
            "structuredNameAndMetadata": t.proxy(
                renames["CounterStructuredNameAndMetadataOut"]
            ).optional(),
            "distribution": t.proxy(renames["DistributionUpdateOut"]).optional(),
            "boolean": t.boolean().optional(),
            "shortId": t.string().optional(),
            "integerGauge": t.proxy(renames["IntegerGaugeOut"]).optional(),
            "nameAndKind": t.proxy(renames["NameAndKindOut"]).optional(),
            "integerMean": t.proxy(renames["IntegerMeanOut"]).optional(),
            "stringList": t.proxy(renames["StringListOut"]).optional(),
            "cumulative": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CounterUpdateOut"])
    types["TaskRunnerSettingsIn"] = t.struct(
        {
            "logDir": t.string().optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "streamingWorkerMainClass": t.string().optional(),
            "harnessCommand": t.string().optional(),
            "workflowFileName": t.string().optional(),
            "languageHint": t.string().optional(),
            "continueOnException": t.boolean().optional(),
            "vmId": t.string().optional(),
            "taskGroup": t.string().optional(),
            "commandlinesFileName": t.string().optional(),
            "alsologtostderr": t.boolean().optional(),
            "taskUser": t.string().optional(),
            "logToSerialconsole": t.boolean().optional(),
            "tempStoragePrefix": t.string().optional(),
            "parallelWorkerSettings": t.proxy(renames["WorkerSettingsIn"]).optional(),
            "logUploadLocation": t.string().optional(),
            "baseUrl": t.string().optional(),
            "dataflowApiVersion": t.string().optional(),
            "baseTaskDir": t.string().optional(),
        }
    ).named(renames["TaskRunnerSettingsIn"])
    types["TaskRunnerSettingsOut"] = t.struct(
        {
            "logDir": t.string().optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "streamingWorkerMainClass": t.string().optional(),
            "harnessCommand": t.string().optional(),
            "workflowFileName": t.string().optional(),
            "languageHint": t.string().optional(),
            "continueOnException": t.boolean().optional(),
            "vmId": t.string().optional(),
            "taskGroup": t.string().optional(),
            "commandlinesFileName": t.string().optional(),
            "alsologtostderr": t.boolean().optional(),
            "taskUser": t.string().optional(),
            "logToSerialconsole": t.boolean().optional(),
            "tempStoragePrefix": t.string().optional(),
            "parallelWorkerSettings": t.proxy(renames["WorkerSettingsOut"]).optional(),
            "logUploadLocation": t.string().optional(),
            "baseUrl": t.string().optional(),
            "dataflowApiVersion": t.string().optional(),
            "baseTaskDir": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskRunnerSettingsOut"])
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
    types["LeaseWorkItemRequestIn"] = t.struct(
        {
            "location": t.string().optional(),
            "workerId": t.string().optional(),
            "currentWorkerTime": t.string().optional(),
            "workerCapabilities": t.array(t.string()).optional(),
            "workItemTypes": t.array(t.string()).optional(),
            "unifiedWorkerRequest": t.struct({"_": t.string().optional()}).optional(),
            "requestedLeaseDuration": t.string().optional(),
        }
    ).named(renames["LeaseWorkItemRequestIn"])
    types["LeaseWorkItemRequestOut"] = t.struct(
        {
            "location": t.string().optional(),
            "workerId": t.string().optional(),
            "currentWorkerTime": t.string().optional(),
            "workerCapabilities": t.array(t.string()).optional(),
            "workItemTypes": t.array(t.string()).optional(),
            "unifiedWorkerRequest": t.struct({"_": t.string().optional()}).optional(),
            "requestedLeaseDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LeaseWorkItemRequestOut"])
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
    types["StringListIn"] = t.struct(
        {"elements": t.array(t.string()).optional()}
    ).named(renames["StringListIn"])
    types["StringListOut"] = t.struct(
        {
            "elements": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StringListOut"])
    types["FloatingPointListIn"] = t.struct(
        {"elements": t.array(t.number()).optional()}
    ).named(renames["FloatingPointListIn"])
    types["FloatingPointListOut"] = t.struct(
        {
            "elements": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloatingPointListOut"])
    types["WorkerThreadScalingReportResponseIn"] = t.struct(
        {"recommendedThreadCount": t.integer().optional()}
    ).named(renames["WorkerThreadScalingReportResponseIn"])
    types["WorkerThreadScalingReportResponseOut"] = t.struct(
        {
            "recommendedThreadCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerThreadScalingReportResponseOut"])
    types["LaunchTemplateResponseIn"] = t.struct(
        {"job": t.proxy(renames["JobIn"]).optional()}
    ).named(renames["LaunchTemplateResponseIn"])
    types["LaunchTemplateResponseOut"] = t.struct(
        {
            "job": t.proxy(renames["JobOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LaunchTemplateResponseOut"])
    types["SplitInt64In"] = t.struct(
        {"highBits": t.integer().optional(), "lowBits": t.integer().optional()}
    ).named(renames["SplitInt64In"])
    types["SplitInt64Out"] = t.struct(
        {
            "highBits": t.integer().optional(),
            "lowBits": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SplitInt64Out"])
    types["ListSnapshotsResponseIn"] = t.struct(
        {"snapshots": t.array(t.proxy(renames["SnapshotIn"])).optional()}
    ).named(renames["ListSnapshotsResponseIn"])
    types["ListSnapshotsResponseOut"] = t.struct(
        {
            "snapshots": t.array(t.proxy(renames["SnapshotOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSnapshotsResponseOut"])
    types["FailedLocationIn"] = t.struct({"name": t.string().optional()}).named(
        renames["FailedLocationIn"]
    )
    types["FailedLocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FailedLocationOut"])
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
    types["ReportWorkItemStatusRequestIn"] = t.struct(
        {
            "currentWorkerTime": t.string().optional(),
            "workerId": t.string().optional(),
            "location": t.string().optional(),
            "workItemStatuses": t.array(
                t.proxy(renames["WorkItemStatusIn"])
            ).optional(),
            "unifiedWorkerRequest": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ReportWorkItemStatusRequestIn"])
    types["ReportWorkItemStatusRequestOut"] = t.struct(
        {
            "currentWorkerTime": t.string().optional(),
            "workerId": t.string().optional(),
            "location": t.string().optional(),
            "workItemStatuses": t.array(
                t.proxy(renames["WorkItemStatusOut"])
            ).optional(),
            "unifiedWorkerRequest": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportWorkItemStatusRequestOut"])
    types["StreamLocationIn"] = t.struct(
        {
            "customSourceLocation": t.proxy(
                renames["CustomSourceLocationIn"]
            ).optional(),
            "streamingStageLocation": t.proxy(
                renames["StreamingStageLocationIn"]
            ).optional(),
            "sideInputLocation": t.proxy(
                renames["StreamingSideInputLocationIn"]
            ).optional(),
            "pubsubLocation": t.proxy(renames["PubsubLocationIn"]).optional(),
        }
    ).named(renames["StreamLocationIn"])
    types["StreamLocationOut"] = t.struct(
        {
            "customSourceLocation": t.proxy(
                renames["CustomSourceLocationOut"]
            ).optional(),
            "streamingStageLocation": t.proxy(
                renames["StreamingStageLocationOut"]
            ).optional(),
            "sideInputLocation": t.proxy(
                renames["StreamingSideInputLocationOut"]
            ).optional(),
            "pubsubLocation": t.proxy(renames["PubsubLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamLocationOut"])
    types["HotKeyInfoIn"] = t.struct(
        {
            "key": t.string().optional(),
            "hotKeyAge": t.string().optional(),
            "keyTruncated": t.boolean().optional(),
        }
    ).named(renames["HotKeyInfoIn"])
    types["HotKeyInfoOut"] = t.struct(
        {
            "key": t.string().optional(),
            "hotKeyAge": t.string().optional(),
            "keyTruncated": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HotKeyInfoOut"])
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
    types["WorkerMessageResponseIn"] = t.struct(
        {
            "workerShutdownNoticeResponse": t.proxy(
                renames["WorkerShutdownNoticeResponseIn"]
            ).optional(),
            "workerThreadScalingReportResponse": t.proxy(
                renames["WorkerThreadScalingReportResponseIn"]
            ).optional(),
            "workerMetricsResponse": t.proxy(
                renames["ResourceUtilizationReportResponseIn"]
            ).optional(),
            "workerHealthReportResponse": t.proxy(
                renames["WorkerHealthReportResponseIn"]
            ).optional(),
        }
    ).named(renames["WorkerMessageResponseIn"])
    types["WorkerMessageResponseOut"] = t.struct(
        {
            "workerShutdownNoticeResponse": t.proxy(
                renames["WorkerShutdownNoticeResponseOut"]
            ).optional(),
            "workerThreadScalingReportResponse": t.proxy(
                renames["WorkerThreadScalingReportResponseOut"]
            ).optional(),
            "workerMetricsResponse": t.proxy(
                renames["ResourceUtilizationReportResponseOut"]
            ).optional(),
            "workerHealthReportResponse": t.proxy(
                renames["WorkerHealthReportResponseOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerMessageResponseOut"])
    types["JobExecutionDetailsIn"] = t.struct(
        {
            "stages": t.array(t.proxy(renames["StageSummaryIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["JobExecutionDetailsIn"])
    types["JobExecutionDetailsOut"] = t.struct(
        {
            "stages": t.array(t.proxy(renames["StageSummaryOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobExecutionDetailsOut"])
    types["FlattenInstructionIn"] = t.struct(
        {"inputs": t.array(t.proxy(renames["InstructionInputIn"])).optional()}
    ).named(renames["FlattenInstructionIn"])
    types["FlattenInstructionOut"] = t.struct(
        {
            "inputs": t.array(t.proxy(renames["InstructionInputOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FlattenInstructionOut"])
    types["BigQueryIODetailsIn"] = t.struct(
        {
            "dataset": t.string().optional(),
            "query": t.string().optional(),
            "table": t.string().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["BigQueryIODetailsIn"])
    types["BigQueryIODetailsOut"] = t.struct(
        {
            "dataset": t.string().optional(),
            "query": t.string().optional(),
            "table": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryIODetailsOut"])
    types["ComponentTransformIn"] = t.struct(
        {
            "originalTransform": t.string().optional(),
            "userName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ComponentTransformIn"])
    types["ComponentTransformOut"] = t.struct(
        {
            "originalTransform": t.string().optional(),
            "userName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComponentTransformOut"])
    types["DiskIn"] = t.struct(
        {
            "diskType": t.string().optional(),
            "sizeGb": t.integer().optional(),
            "mountPoint": t.string().optional(),
        }
    ).named(renames["DiskIn"])
    types["DiskOut"] = t.struct(
        {
            "diskType": t.string().optional(),
            "sizeGb": t.integer().optional(),
            "mountPoint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskOut"])
    types["WorkerLifecycleEventIn"] = t.struct(
        {
            "containerStartTime": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "event": t.string().optional(),
        }
    ).named(renames["WorkerLifecycleEventIn"])
    types["WorkerLifecycleEventOut"] = t.struct(
        {
            "containerStartTime": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "event": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerLifecycleEventOut"])
    types["StreamingConfigTaskIn"] = t.struct(
        {
            "userStepToStateFamilyNameMap": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "maxWorkItemCommitBytes": t.string().optional(),
            "windmillServicePort": t.string().optional(),
            "windmillServiceEndpoint": t.string().optional(),
            "getDataStreamChunkSizeBytes": t.string().optional(),
            "commitStreamChunkSizeBytes": t.string().optional(),
            "streamingComputationConfigs": t.array(
                t.proxy(renames["StreamingComputationConfigIn"])
            ).optional(),
        }
    ).named(renames["StreamingConfigTaskIn"])
    types["StreamingConfigTaskOut"] = t.struct(
        {
            "userStepToStateFamilyNameMap": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "maxWorkItemCommitBytes": t.string().optional(),
            "windmillServicePort": t.string().optional(),
            "windmillServiceEndpoint": t.string().optional(),
            "getDataStreamChunkSizeBytes": t.string().optional(),
            "commitStreamChunkSizeBytes": t.string().optional(),
            "streamingComputationConfigs": t.array(
                t.proxy(renames["StreamingComputationConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingConfigTaskOut"])
    types["WorkerThreadScalingReportIn"] = t.struct(
        {"currentThreadCount": t.integer().optional()}
    ).named(renames["WorkerThreadScalingReportIn"])
    types["WorkerThreadScalingReportOut"] = t.struct(
        {
            "currentThreadCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerThreadScalingReportOut"])
    types["BigTableIODetailsIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "instanceId": t.string().optional(),
            "tableId": t.string().optional(),
        }
    ).named(renames["BigTableIODetailsIn"])
    types["BigTableIODetailsOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "instanceId": t.string().optional(),
            "tableId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigTableIODetailsOut"])
    types["ExecutionStageSummaryIn"] = t.struct(
        {
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "outputSource": t.array(t.proxy(renames["StageSourceIn"])).optional(),
            "prerequisiteStage": t.array(t.string()).optional(),
            "componentSource": t.array(
                t.proxy(renames["ComponentSourceIn"])
            ).optional(),
            "id": t.string().optional(),
            "componentTransform": t.array(
                t.proxy(renames["ComponentTransformIn"])
            ).optional(),
            "inputSource": t.array(t.proxy(renames["StageSourceIn"])).optional(),
        }
    ).named(renames["ExecutionStageSummaryIn"])
    types["ExecutionStageSummaryOut"] = t.struct(
        {
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "outputSource": t.array(t.proxy(renames["StageSourceOut"])).optional(),
            "prerequisiteStage": t.array(t.string()).optional(),
            "componentSource": t.array(
                t.proxy(renames["ComponentSourceOut"])
            ).optional(),
            "id": t.string().optional(),
            "componentTransform": t.array(
                t.proxy(renames["ComponentTransformOut"])
            ).optional(),
            "inputSource": t.array(t.proxy(renames["StageSourceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionStageSummaryOut"])
    types["JobExecutionStageInfoIn"] = t.struct(
        {"stepName": t.array(t.string()).optional()}
    ).named(renames["JobExecutionStageInfoIn"])
    types["JobExecutionStageInfoOut"] = t.struct(
        {
            "stepName": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobExecutionStageInfoOut"])
    types["WorkItemDetailsIn"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["MetricUpdateIn"])).optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "progress": t.proxy(renames["ProgressTimeseriesIn"]).optional(),
            "startTime": t.string().optional(),
            "attemptId": t.string().optional(),
            "stragglerInfo": t.proxy(renames["StragglerInfoIn"]).optional(),
            "taskId": t.string().optional(),
        }
    ).named(renames["WorkItemDetailsIn"])
    types["WorkItemDetailsOut"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["MetricUpdateOut"])).optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "progress": t.proxy(renames["ProgressTimeseriesOut"]).optional(),
            "startTime": t.string().optional(),
            "attemptId": t.string().optional(),
            "stragglerInfo": t.proxy(renames["StragglerInfoOut"]).optional(),
            "taskId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkItemDetailsOut"])
    types["WorkerMessageCodeIn"] = t.struct(
        {
            "code": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["WorkerMessageCodeIn"])
    types["WorkerMessageCodeOut"] = t.struct(
        {
            "code": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerMessageCodeOut"])
    types["DisplayDataIn"] = t.struct(
        {
            "label": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "timestampValue": t.string().optional(),
            "strValue": t.string().optional(),
            "durationValue": t.string().optional(),
            "javaClassValue": t.string().optional(),
            "int64Value": t.string().optional(),
            "shortStrValue": t.string().optional(),
            "namespace": t.string().optional(),
            "floatValue": t.number().optional(),
            "key": t.string().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["DisplayDataIn"])
    types["DisplayDataOut"] = t.struct(
        {
            "label": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "timestampValue": t.string().optional(),
            "strValue": t.string().optional(),
            "durationValue": t.string().optional(),
            "javaClassValue": t.string().optional(),
            "int64Value": t.string().optional(),
            "shortStrValue": t.string().optional(),
            "namespace": t.string().optional(),
            "floatValue": t.number().optional(),
            "key": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisplayDataOut"])
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
    types["SourceForkIn"] = t.struct(
        {
            "primary": t.proxy(renames["SourceSplitShardIn"]).optional(),
            "primarySource": t.proxy(renames["DerivedSourceIn"]).optional(),
            "residualSource": t.proxy(renames["DerivedSourceIn"]).optional(),
            "residual": t.proxy(renames["SourceSplitShardIn"]).optional(),
        }
    ).named(renames["SourceForkIn"])
    types["SourceForkOut"] = t.struct(
        {
            "primary": t.proxy(renames["SourceSplitShardOut"]).optional(),
            "primarySource": t.proxy(renames["DerivedSourceOut"]).optional(),
            "residualSource": t.proxy(renames["DerivedSourceOut"]).optional(),
            "residual": t.proxy(renames["SourceSplitShardOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceForkOut"])
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
    types["JobMetricsIn"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["MetricUpdateIn"])).optional(),
            "metricTime": t.string().optional(),
        }
    ).named(renames["JobMetricsIn"])
    types["JobMetricsOut"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["MetricUpdateOut"])).optional(),
            "metricTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobMetricsOut"])
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
    types["SourceIn"] = t.struct(
        {
            "metadata": t.proxy(renames["SourceMetadataIn"]).optional(),
            "spec": t.struct({"_": t.string().optional()}).optional(),
            "baseSpecs": t.array(t.struct({"_": t.string().optional()})).optional(),
            "doesNotNeedSplitting": t.boolean().optional(),
            "codec": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "metadata": t.proxy(renames["SourceMetadataOut"]).optional(),
            "spec": t.struct({"_": t.string().optional()}).optional(),
            "baseSpecs": t.array(t.struct({"_": t.string().optional()})).optional(),
            "doesNotNeedSplitting": t.boolean().optional(),
            "codec": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["ResourceUtilizationReportIn"] = t.struct(
        {
            "memoryInfo": t.array(t.proxy(renames["MemInfoIn"])).optional(),
            "containers": t.struct({"_": t.string().optional()}).optional(),
            "cpuTime": t.array(t.proxy(renames["CPUTimeIn"])).optional(),
        }
    ).named(renames["ResourceUtilizationReportIn"])
    types["ResourceUtilizationReportOut"] = t.struct(
        {
            "memoryInfo": t.array(t.proxy(renames["MemInfoOut"])).optional(),
            "containers": t.struct({"_": t.string().optional()}).optional(),
            "cpuTime": t.array(t.proxy(renames["CPUTimeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceUtilizationReportOut"])
    types["SourceOperationResponseIn"] = t.struct(
        {
            "split": t.proxy(renames["SourceSplitResponseIn"]).optional(),
            "getMetadata": t.proxy(renames["SourceGetMetadataResponseIn"]).optional(),
        }
    ).named(renames["SourceOperationResponseIn"])
    types["SourceOperationResponseOut"] = t.struct(
        {
            "split": t.proxy(renames["SourceSplitResponseOut"]).optional(),
            "getMetadata": t.proxy(renames["SourceGetMetadataResponseOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOperationResponseOut"])
    types["SnapshotJobRequestIn"] = t.struct(
        {
            "description": t.string().optional(),
            "ttl": t.string().optional(),
            "location": t.string().optional(),
            "snapshotSources": t.boolean().optional(),
        }
    ).named(renames["SnapshotJobRequestIn"])
    types["SnapshotJobRequestOut"] = t.struct(
        {
            "description": t.string().optional(),
            "ttl": t.string().optional(),
            "location": t.string().optional(),
            "snapshotSources": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnapshotJobRequestOut"])
    types["WorkerHealthReportIn"] = t.struct(
        {
            "vmStartupTime": t.string().optional(),
            "vmIsHealthy": t.boolean().optional(),
            "reportInterval": t.string().optional(),
            "vmBrokenCode": t.string().optional(),
            "pods": t.array(t.struct({"_": t.string().optional()})).optional(),
            "msg": t.string().optional(),
            "vmIsBroken": t.boolean().optional(),
        }
    ).named(renames["WorkerHealthReportIn"])
    types["WorkerHealthReportOut"] = t.struct(
        {
            "vmStartupTime": t.string().optional(),
            "vmIsHealthy": t.boolean().optional(),
            "reportInterval": t.string().optional(),
            "vmBrokenCode": t.string().optional(),
            "pods": t.array(t.struct({"_": t.string().optional()})).optional(),
            "msg": t.string().optional(),
            "vmIsBroken": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerHealthReportOut"])
    types["SendDebugCaptureResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SendDebugCaptureResponseIn"]
    )
    types["SendDebugCaptureResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SendDebugCaptureResponseOut"])
    types["SourceMetadataIn"] = t.struct(
        {
            "infinite": t.boolean().optional(),
            "producesSortedKeys": t.boolean().optional(),
            "estimatedSizeBytes": t.string().optional(),
        }
    ).named(renames["SourceMetadataIn"])
    types["SourceMetadataOut"] = t.struct(
        {
            "infinite": t.boolean().optional(),
            "producesSortedKeys": t.boolean().optional(),
            "estimatedSizeBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceMetadataOut"])
    types["StreamingStragglerInfoIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "workerName": t.string().optional(),
            "dataWatermarkLag": t.string().optional(),
            "systemWatermarkLag": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["StreamingStragglerInfoIn"])
    types["StreamingStragglerInfoOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "workerName": t.string().optional(),
            "dataWatermarkLag": t.string().optional(),
            "systemWatermarkLag": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingStragglerInfoOut"])
    types["JobExecutionInfoIn"] = t.struct(
        {"stages": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["JobExecutionInfoIn"])
    types["JobExecutionInfoOut"] = t.struct(
        {
            "stages": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobExecutionInfoOut"])
    types["MetricUpdateIn"] = t.struct(
        {
            "cumulative": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "name": t.proxy(renames["MetricStructuredNameIn"]).optional(),
            "meanSum": t.struct({"_": t.string().optional()}).optional(),
            "scalar": t.struct({"_": t.string().optional()}).optional(),
            "internal": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "set": t.struct({"_": t.string().optional()}).optional(),
            "gauge": t.struct({"_": t.string().optional()}).optional(),
            "meanCount": t.struct({"_": t.string().optional()}).optional(),
            "distribution": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["MetricUpdateIn"])
    types["MetricUpdateOut"] = t.struct(
        {
            "cumulative": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "name": t.proxy(renames["MetricStructuredNameOut"]).optional(),
            "meanSum": t.struct({"_": t.string().optional()}).optional(),
            "scalar": t.struct({"_": t.string().optional()}).optional(),
            "internal": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "set": t.struct({"_": t.string().optional()}).optional(),
            "gauge": t.struct({"_": t.string().optional()}).optional(),
            "meanCount": t.struct({"_": t.string().optional()}).optional(),
            "distribution": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricUpdateOut"])
    types["GetDebugConfigRequestIn"] = t.struct(
        {
            "location": t.string().optional(),
            "componentId": t.string().optional(),
            "workerId": t.string().optional(),
        }
    ).named(renames["GetDebugConfigRequestIn"])
    types["GetDebugConfigRequestOut"] = t.struct(
        {
            "location": t.string().optional(),
            "componentId": t.string().optional(),
            "workerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetDebugConfigRequestOut"])
    types["EnvironmentIn"] = t.struct(
        {
            "serviceOptions": t.array(t.string()).optional(),
            "userAgent": t.struct({"_": t.string().optional()}).optional(),
            "flexResourceSchedulingGoal": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "workerPools": t.array(t.proxy(renames["WorkerPoolIn"])).optional(),
            "internalExperiments": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccountEmail": t.string().optional(),
            "dataset": t.string().optional(),
            "clusterManagerApiService": t.string().optional(),
            "version": t.struct({"_": t.string().optional()}).optional(),
            "workerRegion": t.string().optional(),
            "serviceKmsKeyName": t.string().optional(),
            "workerZone": t.string().optional(),
            "sdkPipelineOptions": t.struct({"_": t.string().optional()}).optional(),
            "tempStoragePrefix": t.string().optional(),
            "experiments": t.array(t.string()).optional(),
        }
    ).named(renames["EnvironmentIn"])
    types["EnvironmentOut"] = t.struct(
        {
            "serviceOptions": t.array(t.string()).optional(),
            "userAgent": t.struct({"_": t.string().optional()}).optional(),
            "flexResourceSchedulingGoal": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "workerPools": t.array(t.proxy(renames["WorkerPoolOut"])).optional(),
            "internalExperiments": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccountEmail": t.string().optional(),
            "dataset": t.string().optional(),
            "clusterManagerApiService": t.string().optional(),
            "version": t.struct({"_": t.string().optional()}).optional(),
            "workerRegion": t.string().optional(),
            "shuffleMode": t.string().optional(),
            "serviceKmsKeyName": t.string().optional(),
            "workerZone": t.string().optional(),
            "sdkPipelineOptions": t.struct({"_": t.string().optional()}).optional(),
            "tempStoragePrefix": t.string().optional(),
            "experiments": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentOut"])
    types["PositionIn"] = t.struct(
        {
            "recordIndex": t.string().optional(),
            "byteOffset": t.string().optional(),
            "key": t.string().optional(),
            "concatPosition": t.proxy(renames["ConcatPositionIn"]).optional(),
            "end": t.boolean().optional(),
            "shufflePosition": t.string().optional(),
        }
    ).named(renames["PositionIn"])
    types["PositionOut"] = t.struct(
        {
            "recordIndex": t.string().optional(),
            "byteOffset": t.string().optional(),
            "key": t.string().optional(),
            "concatPosition": t.proxy(renames["ConcatPositionOut"]).optional(),
            "end": t.boolean().optional(),
            "shufflePosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PositionOut"])
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
    types["WorkerShutdownNoticeIn"] = t.struct({"reason": t.string().optional()}).named(
        renames["WorkerShutdownNoticeIn"]
    )
    types["WorkerShutdownNoticeOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerShutdownNoticeOut"])
    types["GetDebugConfigResponseIn"] = t.struct(
        {"config": t.string().optional()}
    ).named(renames["GetDebugConfigResponseIn"])
    types["GetDebugConfigResponseOut"] = t.struct(
        {
            "config": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetDebugConfigResponseOut"])
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
    types["ListJobMessagesResponseIn"] = t.struct(
        {
            "jobMessages": t.array(t.proxy(renames["JobMessageIn"])).optional(),
            "autoscalingEvents": t.array(
                t.proxy(renames["AutoscalingEventIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListJobMessagesResponseIn"])
    types["ListJobMessagesResponseOut"] = t.struct(
        {
            "jobMessages": t.array(t.proxy(renames["JobMessageOut"])).optional(),
            "autoscalingEvents": t.array(
                t.proxy(renames["AutoscalingEventOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobMessagesResponseOut"])
    types["ReadInstructionIn"] = t.struct(
        {"source": t.proxy(renames["SourceIn"]).optional()}
    ).named(renames["ReadInstructionIn"])
    types["ReadInstructionOut"] = t.struct(
        {
            "source": t.proxy(renames["SourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadInstructionOut"])
    types["PartialGroupByKeyInstructionIn"] = t.struct(
        {
            "originalCombineValuesInputStoreName": t.string().optional(),
            "inputElementCodec": t.struct({"_": t.string().optional()}).optional(),
            "sideInputs": t.array(t.proxy(renames["SideInputInfoIn"])).optional(),
            "originalCombineValuesStepName": t.string().optional(),
            "input": t.proxy(renames["InstructionInputIn"]).optional(),
            "valueCombiningFn": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PartialGroupByKeyInstructionIn"])
    types["PartialGroupByKeyInstructionOut"] = t.struct(
        {
            "originalCombineValuesInputStoreName": t.string().optional(),
            "inputElementCodec": t.struct({"_": t.string().optional()}).optional(),
            "sideInputs": t.array(t.proxy(renames["SideInputInfoOut"])).optional(),
            "originalCombineValuesStepName": t.string().optional(),
            "input": t.proxy(renames["InstructionInputOut"]).optional(),
            "valueCombiningFn": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartialGroupByKeyInstructionOut"])
    types["AutoscalingSettingsIn"] = t.struct(
        {"maxNumWorkers": t.integer().optional(), "algorithm": t.string().optional()}
    ).named(renames["AutoscalingSettingsIn"])
    types["AutoscalingSettingsOut"] = t.struct(
        {
            "maxNumWorkers": t.integer().optional(),
            "algorithm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoscalingSettingsOut"])
    types["SeqMapTaskOutputInfoIn"] = t.struct(
        {"sink": t.proxy(renames["SinkIn"]).optional(), "tag": t.string().optional()}
    ).named(renames["SeqMapTaskOutputInfoIn"])
    types["SeqMapTaskOutputInfoOut"] = t.struct(
        {
            "sink": t.proxy(renames["SinkOut"]).optional(),
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SeqMapTaskOutputInfoOut"])

    functions = {}
    functions["projectsWorkerMessages"] = dataflow.delete(
        "v1b3/projects/{projectId}/snapshots",
        t.struct(
            {
                "location": t.string().optional(),
                "snapshotId": t.string().optional(),
                "projectId": t.string().optional(),
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
                "location": t.string().optional(),
                "snapshotId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeleteSnapshotResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsSnapshot"] = dataflow.get(
        "v1b3/projects/{projectId}/jobs/{jobId}",
        t.struct(
            {
                "location": t.string().optional(),
                "jobId": t.string().optional(),
                "view": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsCreate"] = dataflow.get(
        "v1b3/projects/{projectId}/jobs/{jobId}",
        t.struct(
            {
                "location": t.string().optional(),
                "jobId": t.string().optional(),
                "view": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsUpdate"] = dataflow.get(
        "v1b3/projects/{projectId}/jobs/{jobId}",
        t.struct(
            {
                "location": t.string().optional(),
                "jobId": t.string().optional(),
                "view": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsAggregated"] = dataflow.get(
        "v1b3/projects/{projectId}/jobs/{jobId}",
        t.struct(
            {
                "location": t.string().optional(),
                "jobId": t.string().optional(),
                "view": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsGetMetrics"] = dataflow.get(
        "v1b3/projects/{projectId}/jobs/{jobId}",
        t.struct(
            {
                "location": t.string().optional(),
                "jobId": t.string().optional(),
                "view": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsList"] = dataflow.get(
        "v1b3/projects/{projectId}/jobs/{jobId}",
        t.struct(
            {
                "location": t.string().optional(),
                "jobId": t.string().optional(),
                "view": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsGet"] = dataflow.get(
        "v1b3/projects/{projectId}/jobs/{jobId}",
        t.struct(
            {
                "location": t.string().optional(),
                "jobId": t.string().optional(),
                "view": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsMessagesList"] = dataflow.get(
        "v1b3/projects/{projectId}/jobs/{jobId}/messages",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "projectId": t.string().optional(),
                "location": t.string().optional(),
                "jobId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "endTime": t.string().optional(),
                "startTime": t.string().optional(),
                "minimumImportance": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobMessagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsDebugGetConfig"] = dataflow.post(
        "v1b3/projects/{projectId}/jobs/{jobId}/debug/sendCapture",
        t.struct(
            {
                "jobId": t.string().optional(),
                "projectId": t.string().optional(),
                "data": t.string().optional(),
                "componentId": t.string().optional(),
                "workerId": t.string().optional(),
                "dataFormat": t.string().optional(),
                "location": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SendDebugCaptureResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsDebugSendCapture"] = dataflow.post(
        "v1b3/projects/{projectId}/jobs/{jobId}/debug/sendCapture",
        t.struct(
            {
                "jobId": t.string().optional(),
                "projectId": t.string().optional(),
                "data": t.string().optional(),
                "componentId": t.string().optional(),
                "workerId": t.string().optional(),
                "dataFormat": t.string().optional(),
                "location": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SendDebugCaptureResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsWorkItemsReportStatus"] = dataflow.post(
        "v1b3/projects/{projectId}/jobs/{jobId}/workItems:lease",
        t.struct(
            {
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "location": t.string().optional(),
                "workerId": t.string().optional(),
                "currentWorkerTime": t.string().optional(),
                "workerCapabilities": t.array(t.string()).optional(),
                "workItemTypes": t.array(t.string()).optional(),
                "unifiedWorkerRequest": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "requestedLeaseDuration": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaseWorkItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsWorkItemsLease"] = dataflow.post(
        "v1b3/projects/{projectId}/jobs/{jobId}/workItems:lease",
        t.struct(
            {
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "location": t.string().optional(),
                "workerId": t.string().optional(),
                "currentWorkerTime": t.string().optional(),
                "workerCapabilities": t.array(t.string()).optional(),
                "workItemTypes": t.array(t.string()).optional(),
                "unifiedWorkerRequest": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "requestedLeaseDuration": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaseWorkItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkerMessages"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/WorkerMessages",
        t.struct(
            {
                "location": t.string().optional(),
                "projectId": t.string().optional(),
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
    functions["projectsLocationsJobsUpdate"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}",
        t.struct(
            {
                "view": t.string().optional(),
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsList"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}",
        t.struct(
            {
                "view": t.string().optional(),
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsGetMetrics"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}",
        t.struct(
            {
                "view": t.string().optional(),
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsSnapshot"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}",
        t.struct(
            {
                "view": t.string().optional(),
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsCreate"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}",
        t.struct(
            {
                "view": t.string().optional(),
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsGetExecutionDetails"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}",
        t.struct(
            {
                "view": t.string().optional(),
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsGet"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}",
        t.struct(
            {
                "view": t.string().optional(),
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsStagesGetExecutionDetails"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/stages/{stageId}/executionDetails",
        t.struct(
            {
                "projectId": t.string().optional(),
                "stageId": t.string().optional(),
                "jobId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "endTime": t.string().optional(),
                "location": t.string().optional(),
                "startTime": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StageExecutionDetailsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsMessagesList"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/messages",
        t.struct(
            {
                "endTime": t.string().optional(),
                "projectId": t.string().optional(),
                "location": t.string().optional(),
                "pageSize": t.integer().optional(),
                "minimumImportance": t.string().optional(),
                "jobId": t.string().optional(),
                "pageToken": t.string().optional(),
                "startTime": t.string().optional(),
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
                "projectId": t.string().optional(),
                "location": t.string().optional(),
                "jobId": t.string().optional(),
                "workerId": t.string().optional(),
                "currentWorkerTime": t.string().optional(),
                "workerCapabilities": t.array(t.string()).optional(),
                "workItemTypes": t.array(t.string()).optional(),
                "unifiedWorkerRequest": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "requestedLeaseDuration": t.string().optional(),
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
                "projectId": t.string().optional(),
                "location": t.string().optional(),
                "jobId": t.string().optional(),
                "workerId": t.string().optional(),
                "currentWorkerTime": t.string().optional(),
                "workerCapabilities": t.array(t.string()).optional(),
                "workItemTypes": t.array(t.string()).optional(),
                "unifiedWorkerRequest": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "requestedLeaseDuration": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaseWorkItemResponseOut"]),
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
    functions["projectsLocationsJobsDebugSendCapture"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/debug/getConfig",
        t.struct(
            {
                "jobId": t.string().optional(),
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "componentId": t.string().optional(),
                "workerId": t.string().optional(),
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
                "jobId": t.string().optional(),
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "componentId": t.string().optional(),
                "workerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetDebugConfigResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSnapshotsList"] = dataflow.delete(
        "v1b3/projects/{projectId}/locations/{location}/snapshots/{snapshotId}",
        t.struct(
            {
                "projectId": t.string().optional(),
                "location": t.string().optional(),
                "snapshotId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeleteSnapshotResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSnapshotsGet"] = dataflow.delete(
        "v1b3/projects/{projectId}/locations/{location}/snapshots/{snapshotId}",
        t.struct(
            {
                "projectId": t.string().optional(),
                "location": t.string().optional(),
                "snapshotId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeleteSnapshotResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSnapshotsDelete"] = dataflow.delete(
        "v1b3/projects/{projectId}/locations/{location}/snapshots/{snapshotId}",
        t.struct(
            {
                "projectId": t.string().optional(),
                "location": t.string().optional(),
                "snapshotId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeleteSnapshotResponseOut"]),
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
        "v1b3/projects/{projectId}/locations/{location}/templates",
        t.struct(
            {
                "projectId": t.string(),
                "location": t.string().optional(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "jobName": t.string(),
                "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
                "gcsPath": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTemplatesLaunch"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/templates",
        t.struct(
            {
                "projectId": t.string(),
                "location": t.string().optional(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "jobName": t.string(),
                "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
                "gcsPath": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTemplatesCreate"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/templates",
        t.struct(
            {
                "projectId": t.string(),
                "location": t.string().optional(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "jobName": t.string(),
                "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
                "gcsPath": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnapshotsGet"] = dataflow.get(
        "v1b3/projects/{projectId}/snapshots",
        t.struct(
            {
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSnapshotsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnapshotsList"] = dataflow.get(
        "v1b3/projects/{projectId}/snapshots",
        t.struct(
            {
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSnapshotsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTemplatesCreate"] = dataflow.post(
        "v1b3/projects/{projectId}/templates:launch",
        t.struct(
            {
                "dynamicTemplate.gcsPath": t.string().optional(),
                "projectId": t.string(),
                "location": t.string().optional(),
                "dynamicTemplate.stagingLocation": t.string().optional(),
                "gcsPath": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "transformNameMapping": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
                "jobName": t.string(),
                "update": t.boolean().optional(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LaunchTemplateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTemplatesGet"] = dataflow.post(
        "v1b3/projects/{projectId}/templates:launch",
        t.struct(
            {
                "dynamicTemplate.gcsPath": t.string().optional(),
                "projectId": t.string(),
                "location": t.string().optional(),
                "dynamicTemplate.stagingLocation": t.string().optional(),
                "gcsPath": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "transformNameMapping": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
                "jobName": t.string(),
                "update": t.boolean().optional(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
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
                "dynamicTemplate.gcsPath": t.string().optional(),
                "projectId": t.string(),
                "location": t.string().optional(),
                "dynamicTemplate.stagingLocation": t.string().optional(),
                "gcsPath": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "transformNameMapping": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
                "jobName": t.string(),
                "update": t.boolean().optional(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LaunchTemplateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="dataflow", renames=renames, types=Box(types), functions=Box(functions)
    )
