from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_dataflow() -> Import:
    dataflow = HTTPRuntime("https://dataflow.googleapis.com/")

    renames = {
        "ErrorResponse": "_dataflow_1_ErrorResponse",
        "TopologyConfigIn": "_dataflow_2_TopologyConfigIn",
        "TopologyConfigOut": "_dataflow_3_TopologyConfigOut",
        "GetDebugConfigRequestIn": "_dataflow_4_GetDebugConfigRequestIn",
        "GetDebugConfigRequestOut": "_dataflow_5_GetDebugConfigRequestOut",
        "ParDoInstructionIn": "_dataflow_6_ParDoInstructionIn",
        "ParDoInstructionOut": "_dataflow_7_ParDoInstructionOut",
        "GetDebugConfigResponseIn": "_dataflow_8_GetDebugConfigResponseIn",
        "GetDebugConfigResponseOut": "_dataflow_9_GetDebugConfigResponseOut",
        "ParameterIn": "_dataflow_10_ParameterIn",
        "ParameterOut": "_dataflow_11_ParameterOut",
        "SideInputInfoIn": "_dataflow_12_SideInputInfoIn",
        "SideInputInfoOut": "_dataflow_13_SideInputInfoOut",
        "ApproximateSplitRequestIn": "_dataflow_14_ApproximateSplitRequestIn",
        "ApproximateSplitRequestOut": "_dataflow_15_ApproximateSplitRequestOut",
        "StragglerIn": "_dataflow_16_StragglerIn",
        "StragglerOut": "_dataflow_17_StragglerOut",
        "ResourceUtilizationReportIn": "_dataflow_18_ResourceUtilizationReportIn",
        "ResourceUtilizationReportOut": "_dataflow_19_ResourceUtilizationReportOut",
        "ContainerSpecIn": "_dataflow_20_ContainerSpecIn",
        "ContainerSpecOut": "_dataflow_21_ContainerSpecOut",
        "ReportWorkItemStatusResponseIn": "_dataflow_22_ReportWorkItemStatusResponseIn",
        "ReportWorkItemStatusResponseOut": "_dataflow_23_ReportWorkItemStatusResponseOut",
        "InstructionInputIn": "_dataflow_24_InstructionInputIn",
        "InstructionInputOut": "_dataflow_25_InstructionInputOut",
        "StreamingSetupTaskIn": "_dataflow_26_StreamingSetupTaskIn",
        "StreamingSetupTaskOut": "_dataflow_27_StreamingSetupTaskOut",
        "SourceGetMetadataRequestIn": "_dataflow_28_SourceGetMetadataRequestIn",
        "SourceGetMetadataRequestOut": "_dataflow_29_SourceGetMetadataRequestOut",
        "StreamLocationIn": "_dataflow_30_StreamLocationIn",
        "StreamLocationOut": "_dataflow_31_StreamLocationOut",
        "DeleteSnapshotResponseIn": "_dataflow_32_DeleteSnapshotResponseIn",
        "DeleteSnapshotResponseOut": "_dataflow_33_DeleteSnapshotResponseOut",
        "BigQueryIODetailsIn": "_dataflow_34_BigQueryIODetailsIn",
        "BigQueryIODetailsOut": "_dataflow_35_BigQueryIODetailsOut",
        "DynamicSourceSplitIn": "_dataflow_36_DynamicSourceSplitIn",
        "DynamicSourceSplitOut": "_dataflow_37_DynamicSourceSplitOut",
        "StreamingApplianceSnapshotConfigIn": "_dataflow_38_StreamingApplianceSnapshotConfigIn",
        "StreamingApplianceSnapshotConfigOut": "_dataflow_39_StreamingApplianceSnapshotConfigOut",
        "SourceOperationResponseIn": "_dataflow_40_SourceOperationResponseIn",
        "SourceOperationResponseOut": "_dataflow_41_SourceOperationResponseOut",
        "PubsubSnapshotMetadataIn": "_dataflow_42_PubsubSnapshotMetadataIn",
        "PubsubSnapshotMetadataOut": "_dataflow_43_PubsubSnapshotMetadataOut",
        "WorkItemStatusIn": "_dataflow_44_WorkItemStatusIn",
        "WorkItemStatusOut": "_dataflow_45_WorkItemStatusOut",
        "LaunchFlexTemplateRequestIn": "_dataflow_46_LaunchFlexTemplateRequestIn",
        "LaunchFlexTemplateRequestOut": "_dataflow_47_LaunchFlexTemplateRequestOut",
        "StageSourceIn": "_dataflow_48_StageSourceIn",
        "StageSourceOut": "_dataflow_49_StageSourceOut",
        "DisplayDataIn": "_dataflow_50_DisplayDataIn",
        "DisplayDataOut": "_dataflow_51_DisplayDataOut",
        "CreateJobFromTemplateRequestIn": "_dataflow_52_CreateJobFromTemplateRequestIn",
        "CreateJobFromTemplateRequestOut": "_dataflow_53_CreateJobFromTemplateRequestOut",
        "SDKInfoIn": "_dataflow_54_SDKInfoIn",
        "SDKInfoOut": "_dataflow_55_SDKInfoOut",
        "LeaseWorkItemRequestIn": "_dataflow_56_LeaseWorkItemRequestIn",
        "LeaseWorkItemRequestOut": "_dataflow_57_LeaseWorkItemRequestOut",
        "ReadInstructionIn": "_dataflow_58_ReadInstructionIn",
        "ReadInstructionOut": "_dataflow_59_ReadInstructionOut",
        "SnapshotIn": "_dataflow_60_SnapshotIn",
        "SnapshotOut": "_dataflow_61_SnapshotOut",
        "FileIODetailsIn": "_dataflow_62_FileIODetailsIn",
        "FileIODetailsOut": "_dataflow_63_FileIODetailsOut",
        "ConcatPositionIn": "_dataflow_64_ConcatPositionIn",
        "ConcatPositionOut": "_dataflow_65_ConcatPositionOut",
        "SourceGetMetadataResponseIn": "_dataflow_66_SourceGetMetadataResponseIn",
        "SourceGetMetadataResponseOut": "_dataflow_67_SourceGetMetadataResponseOut",
        "ResourceUtilizationReportResponseIn": "_dataflow_68_ResourceUtilizationReportResponseIn",
        "ResourceUtilizationReportResponseOut": "_dataflow_69_ResourceUtilizationReportResponseOut",
        "DerivedSourceIn": "_dataflow_70_DerivedSourceIn",
        "DerivedSourceOut": "_dataflow_71_DerivedSourceOut",
        "LaunchFlexTemplateParameterIn": "_dataflow_72_LaunchFlexTemplateParameterIn",
        "LaunchFlexTemplateParameterOut": "_dataflow_73_LaunchFlexTemplateParameterOut",
        "LaunchTemplateResponseIn": "_dataflow_74_LaunchTemplateResponseIn",
        "LaunchTemplateResponseOut": "_dataflow_75_LaunchTemplateResponseOut",
        "SourceSplitResponseIn": "_dataflow_76_SourceSplitResponseIn",
        "SourceSplitResponseOut": "_dataflow_77_SourceSplitResponseOut",
        "CounterMetadataIn": "_dataflow_78_CounterMetadataIn",
        "CounterMetadataOut": "_dataflow_79_CounterMetadataOut",
        "WriteInstructionIn": "_dataflow_80_WriteInstructionIn",
        "WriteInstructionOut": "_dataflow_81_WriteInstructionOut",
        "ShellTaskIn": "_dataflow_82_ShellTaskIn",
        "ShellTaskOut": "_dataflow_83_ShellTaskOut",
        "ParameterMetadataIn": "_dataflow_84_ParameterMetadataIn",
        "ParameterMetadataOut": "_dataflow_85_ParameterMetadataOut",
        "StatusIn": "_dataflow_86_StatusIn",
        "StatusOut": "_dataflow_87_StatusOut",
        "DebugOptionsIn": "_dataflow_88_DebugOptionsIn",
        "DebugOptionsOut": "_dataflow_89_DebugOptionsOut",
        "MetricUpdateIn": "_dataflow_90_MetricUpdateIn",
        "MetricUpdateOut": "_dataflow_91_MetricUpdateOut",
        "SinkIn": "_dataflow_92_SinkIn",
        "SinkOut": "_dataflow_93_SinkOut",
        "GetTemplateResponseIn": "_dataflow_94_GetTemplateResponseIn",
        "GetTemplateResponseOut": "_dataflow_95_GetTemplateResponseOut",
        "PipelineDescriptionIn": "_dataflow_96_PipelineDescriptionIn",
        "PipelineDescriptionOut": "_dataflow_97_PipelineDescriptionOut",
        "WorkerLifecycleEventIn": "_dataflow_98_WorkerLifecycleEventIn",
        "WorkerLifecycleEventOut": "_dataflow_99_WorkerLifecycleEventOut",
        "MetricShortIdIn": "_dataflow_100_MetricShortIdIn",
        "MetricShortIdOut": "_dataflow_101_MetricShortIdOut",
        "StringListIn": "_dataflow_102_StringListIn",
        "StringListOut": "_dataflow_103_StringListOut",
        "ComponentTransformIn": "_dataflow_104_ComponentTransformIn",
        "ComponentTransformOut": "_dataflow_105_ComponentTransformOut",
        "CustomSourceLocationIn": "_dataflow_106_CustomSourceLocationIn",
        "CustomSourceLocationOut": "_dataflow_107_CustomSourceLocationOut",
        "JobExecutionDetailsIn": "_dataflow_108_JobExecutionDetailsIn",
        "JobExecutionDetailsOut": "_dataflow_109_JobExecutionDetailsOut",
        "PackageIn": "_dataflow_110_PackageIn",
        "PackageOut": "_dataflow_111_PackageOut",
        "ExecutionStageSummaryIn": "_dataflow_112_ExecutionStageSummaryIn",
        "ExecutionStageSummaryOut": "_dataflow_113_ExecutionStageSummaryOut",
        "StragglerInfoIn": "_dataflow_114_StragglerInfoIn",
        "StragglerInfoOut": "_dataflow_115_StragglerInfoOut",
        "StreamingSideInputLocationIn": "_dataflow_116_StreamingSideInputLocationIn",
        "StreamingSideInputLocationOut": "_dataflow_117_StreamingSideInputLocationOut",
        "SourceSplitRequestIn": "_dataflow_118_SourceSplitRequestIn",
        "SourceSplitRequestOut": "_dataflow_119_SourceSplitRequestOut",
        "CPUTimeIn": "_dataflow_120_CPUTimeIn",
        "CPUTimeOut": "_dataflow_121_CPUTimeOut",
        "BigTableIODetailsIn": "_dataflow_122_BigTableIODetailsIn",
        "BigTableIODetailsOut": "_dataflow_123_BigTableIODetailsOut",
        "ExecutionStageStateIn": "_dataflow_124_ExecutionStageStateIn",
        "ExecutionStageStateOut": "_dataflow_125_ExecutionStageStateOut",
        "WorkerPoolIn": "_dataflow_126_WorkerPoolIn",
        "WorkerPoolOut": "_dataflow_127_WorkerPoolOut",
        "EnvironmentIn": "_dataflow_128_EnvironmentIn",
        "EnvironmentOut": "_dataflow_129_EnvironmentOut",
        "FloatingPointMeanIn": "_dataflow_130_FloatingPointMeanIn",
        "FloatingPointMeanOut": "_dataflow_131_FloatingPointMeanOut",
        "IntegerGaugeIn": "_dataflow_132_IntegerGaugeIn",
        "IntegerGaugeOut": "_dataflow_133_IntegerGaugeOut",
        "SpannerIODetailsIn": "_dataflow_134_SpannerIODetailsIn",
        "SpannerIODetailsOut": "_dataflow_135_SpannerIODetailsOut",
        "ParallelInstructionIn": "_dataflow_136_ParallelInstructionIn",
        "ParallelInstructionOut": "_dataflow_137_ParallelInstructionOut",
        "HotKeyInfoIn": "_dataflow_138_HotKeyInfoIn",
        "HotKeyInfoOut": "_dataflow_139_HotKeyInfoOut",
        "FailedLocationIn": "_dataflow_140_FailedLocationIn",
        "FailedLocationOut": "_dataflow_141_FailedLocationOut",
        "WorkerSettingsIn": "_dataflow_142_WorkerSettingsIn",
        "WorkerSettingsOut": "_dataflow_143_WorkerSettingsOut",
        "JobIn": "_dataflow_144_JobIn",
        "JobOut": "_dataflow_145_JobOut",
        "SplitInt64In": "_dataflow_146_SplitInt64In",
        "SplitInt64Out": "_dataflow_147_SplitInt64Out",
        "JobMessageIn": "_dataflow_148_JobMessageIn",
        "JobMessageOut": "_dataflow_149_JobMessageOut",
        "MultiOutputInfoIn": "_dataflow_150_MultiOutputInfoIn",
        "MultiOutputInfoOut": "_dataflow_151_MultiOutputInfoOut",
        "WorkerThreadScalingReportIn": "_dataflow_152_WorkerThreadScalingReportIn",
        "WorkerThreadScalingReportOut": "_dataflow_153_WorkerThreadScalingReportOut",
        "FloatingPointListIn": "_dataflow_154_FloatingPointListIn",
        "FloatingPointListOut": "_dataflow_155_FloatingPointListOut",
        "StreamingConfigTaskIn": "_dataflow_156_StreamingConfigTaskIn",
        "StreamingConfigTaskOut": "_dataflow_157_StreamingConfigTaskOut",
        "ProgressTimeseriesIn": "_dataflow_158_ProgressTimeseriesIn",
        "ProgressTimeseriesOut": "_dataflow_159_ProgressTimeseriesOut",
        "ComponentSourceIn": "_dataflow_160_ComponentSourceIn",
        "ComponentSourceOut": "_dataflow_161_ComponentSourceOut",
        "CounterStructuredNameAndMetadataIn": "_dataflow_162_CounterStructuredNameAndMetadataIn",
        "CounterStructuredNameAndMetadataOut": "_dataflow_163_CounterStructuredNameAndMetadataOut",
        "SendWorkerMessagesResponseIn": "_dataflow_164_SendWorkerMessagesResponseIn",
        "SendWorkerMessagesResponseOut": "_dataflow_165_SendWorkerMessagesResponseOut",
        "IntegerListIn": "_dataflow_166_IntegerListIn",
        "IntegerListOut": "_dataflow_167_IntegerListOut",
        "StragglerSummaryIn": "_dataflow_168_StragglerSummaryIn",
        "StragglerSummaryOut": "_dataflow_169_StragglerSummaryOut",
        "SourceIn": "_dataflow_170_SourceIn",
        "SourceOut": "_dataflow_171_SourceOut",
        "SdkHarnessContainerImageIn": "_dataflow_172_SdkHarnessContainerImageIn",
        "SdkHarnessContainerImageOut": "_dataflow_173_SdkHarnessContainerImageOut",
        "PositionIn": "_dataflow_174_PositionIn",
        "PositionOut": "_dataflow_175_PositionOut",
        "AutoscalingSettingsIn": "_dataflow_176_AutoscalingSettingsIn",
        "AutoscalingSettingsOut": "_dataflow_177_AutoscalingSettingsOut",
        "SourceSplitShardIn": "_dataflow_178_SourceSplitShardIn",
        "SourceSplitShardOut": "_dataflow_179_SourceSplitShardOut",
        "StructuredMessageIn": "_dataflow_180_StructuredMessageIn",
        "StructuredMessageOut": "_dataflow_181_StructuredMessageOut",
        "JobMetadataIn": "_dataflow_182_JobMetadataIn",
        "JobMetadataOut": "_dataflow_183_JobMetadataOut",
        "ComputationTopologyIn": "_dataflow_184_ComputationTopologyIn",
        "ComputationTopologyOut": "_dataflow_185_ComputationTopologyOut",
        "TemplateMetadataIn": "_dataflow_186_TemplateMetadataIn",
        "TemplateMetadataOut": "_dataflow_187_TemplateMetadataOut",
        "LaunchFlexTemplateResponseIn": "_dataflow_188_LaunchFlexTemplateResponseIn",
        "LaunchFlexTemplateResponseOut": "_dataflow_189_LaunchFlexTemplateResponseOut",
        "JobExecutionInfoIn": "_dataflow_190_JobExecutionInfoIn",
        "JobExecutionInfoOut": "_dataflow_191_JobExecutionInfoOut",
        "SendWorkerMessagesRequestIn": "_dataflow_192_SendWorkerMessagesRequestIn",
        "SendWorkerMessagesRequestOut": "_dataflow_193_SendWorkerMessagesRequestOut",
        "DiskIn": "_dataflow_194_DiskIn",
        "DiskOut": "_dataflow_195_DiskOut",
        "MapTaskIn": "_dataflow_196_MapTaskIn",
        "MapTaskOut": "_dataflow_197_MapTaskOut",
        "PointIn": "_dataflow_198_PointIn",
        "PointOut": "_dataflow_199_PointOut",
        "DatastoreIODetailsIn": "_dataflow_200_DatastoreIODetailsIn",
        "DatastoreIODetailsOut": "_dataflow_201_DatastoreIODetailsOut",
        "StageExecutionDetailsIn": "_dataflow_202_StageExecutionDetailsIn",
        "StageExecutionDetailsOut": "_dataflow_203_StageExecutionDetailsOut",
        "ApproximateReportedProgressIn": "_dataflow_204_ApproximateReportedProgressIn",
        "ApproximateReportedProgressOut": "_dataflow_205_ApproximateReportedProgressOut",
        "ReportedParallelismIn": "_dataflow_206_ReportedParallelismIn",
        "ReportedParallelismOut": "_dataflow_207_ReportedParallelismOut",
        "RuntimeEnvironmentIn": "_dataflow_208_RuntimeEnvironmentIn",
        "RuntimeEnvironmentOut": "_dataflow_209_RuntimeEnvironmentOut",
        "JobExecutionStageInfoIn": "_dataflow_210_JobExecutionStageInfoIn",
        "JobExecutionStageInfoOut": "_dataflow_211_JobExecutionStageInfoOut",
        "SendDebugCaptureResponseIn": "_dataflow_212_SendDebugCaptureResponseIn",
        "SendDebugCaptureResponseOut": "_dataflow_213_SendDebugCaptureResponseOut",
        "KeyRangeDataDiskAssignmentIn": "_dataflow_214_KeyRangeDataDiskAssignmentIn",
        "KeyRangeDataDiskAssignmentOut": "_dataflow_215_KeyRangeDataDiskAssignmentOut",
        "ReportWorkItemStatusRequestIn": "_dataflow_216_ReportWorkItemStatusRequestIn",
        "ReportWorkItemStatusRequestOut": "_dataflow_217_ReportWorkItemStatusRequestOut",
        "LeaseWorkItemResponseIn": "_dataflow_218_LeaseWorkItemResponseIn",
        "LeaseWorkItemResponseOut": "_dataflow_219_LeaseWorkItemResponseOut",
        "StreamingComputationConfigIn": "_dataflow_220_StreamingComputationConfigIn",
        "StreamingComputationConfigOut": "_dataflow_221_StreamingComputationConfigOut",
        "SdkVersionIn": "_dataflow_222_SdkVersionIn",
        "SdkVersionOut": "_dataflow_223_SdkVersionOut",
        "FlattenInstructionIn": "_dataflow_224_FlattenInstructionIn",
        "FlattenInstructionOut": "_dataflow_225_FlattenInstructionOut",
        "PartialGroupByKeyInstructionIn": "_dataflow_226_PartialGroupByKeyInstructionIn",
        "PartialGroupByKeyInstructionOut": "_dataflow_227_PartialGroupByKeyInstructionOut",
        "SnapshotJobRequestIn": "_dataflow_228_SnapshotJobRequestIn",
        "SnapshotJobRequestOut": "_dataflow_229_SnapshotJobRequestOut",
        "StreamingStragglerInfoIn": "_dataflow_230_StreamingStragglerInfoIn",
        "StreamingStragglerInfoOut": "_dataflow_231_StreamingStragglerInfoOut",
        "WorkItemIn": "_dataflow_232_WorkItemIn",
        "WorkItemOut": "_dataflow_233_WorkItemOut",
        "StepIn": "_dataflow_234_StepIn",
        "StepOut": "_dataflow_235_StepOut",
        "SeqMapTaskIn": "_dataflow_236_SeqMapTaskIn",
        "SeqMapTaskOut": "_dataflow_237_SeqMapTaskOut",
        "RuntimeUpdatableParamsIn": "_dataflow_238_RuntimeUpdatableParamsIn",
        "RuntimeUpdatableParamsOut": "_dataflow_239_RuntimeUpdatableParamsOut",
        "FlexTemplateRuntimeEnvironmentIn": "_dataflow_240_FlexTemplateRuntimeEnvironmentIn",
        "FlexTemplateRuntimeEnvironmentOut": "_dataflow_241_FlexTemplateRuntimeEnvironmentOut",
        "WorkerDetailsIn": "_dataflow_242_WorkerDetailsIn",
        "WorkerDetailsOut": "_dataflow_243_WorkerDetailsOut",
        "RuntimeMetadataIn": "_dataflow_244_RuntimeMetadataIn",
        "RuntimeMetadataOut": "_dataflow_245_RuntimeMetadataOut",
        "StageSummaryIn": "_dataflow_246_StageSummaryIn",
        "StageSummaryOut": "_dataflow_247_StageSummaryOut",
        "PubSubIODetailsIn": "_dataflow_248_PubSubIODetailsIn",
        "PubSubIODetailsOut": "_dataflow_249_PubSubIODetailsOut",
        "WorkerThreadScalingReportResponseIn": "_dataflow_250_WorkerThreadScalingReportResponseIn",
        "WorkerThreadScalingReportResponseOut": "_dataflow_251_WorkerThreadScalingReportResponseOut",
        "SourceSplitOptionsIn": "_dataflow_252_SourceSplitOptionsIn",
        "SourceSplitOptionsOut": "_dataflow_253_SourceSplitOptionsOut",
        "HotKeyDebuggingInfoIn": "_dataflow_254_HotKeyDebuggingInfoIn",
        "HotKeyDebuggingInfoOut": "_dataflow_255_HotKeyDebuggingInfoOut",
        "PubsubLocationIn": "_dataflow_256_PubsubLocationIn",
        "PubsubLocationOut": "_dataflow_257_PubsubLocationOut",
        "WorkItemServiceStateIn": "_dataflow_258_WorkItemServiceStateIn",
        "WorkItemServiceStateOut": "_dataflow_259_WorkItemServiceStateOut",
        "SourceOperationRequestIn": "_dataflow_260_SourceOperationRequestIn",
        "SourceOperationRequestOut": "_dataflow_261_SourceOperationRequestOut",
        "WorkerHealthReportResponseIn": "_dataflow_262_WorkerHealthReportResponseIn",
        "WorkerHealthReportResponseOut": "_dataflow_263_WorkerHealthReportResponseOut",
        "SourceForkIn": "_dataflow_264_SourceForkIn",
        "SourceForkOut": "_dataflow_265_SourceForkOut",
        "KeyRangeLocationIn": "_dataflow_266_KeyRangeLocationIn",
        "KeyRangeLocationOut": "_dataflow_267_KeyRangeLocationOut",
        "ListJobMessagesResponseIn": "_dataflow_268_ListJobMessagesResponseIn",
        "ListJobMessagesResponseOut": "_dataflow_269_ListJobMessagesResponseOut",
        "CounterStructuredNameIn": "_dataflow_270_CounterStructuredNameIn",
        "CounterStructuredNameOut": "_dataflow_271_CounterStructuredNameOut",
        "ListSnapshotsResponseIn": "_dataflow_272_ListSnapshotsResponseIn",
        "ListSnapshotsResponseOut": "_dataflow_273_ListSnapshotsResponseOut",
        "InstructionOutputIn": "_dataflow_274_InstructionOutputIn",
        "InstructionOutputOut": "_dataflow_275_InstructionOutputOut",
        "IntegerMeanIn": "_dataflow_276_IntegerMeanIn",
        "IntegerMeanOut": "_dataflow_277_IntegerMeanOut",
        "DataDiskAssignmentIn": "_dataflow_278_DataDiskAssignmentIn",
        "DataDiskAssignmentOut": "_dataflow_279_DataDiskAssignmentOut",
        "LaunchTemplateParametersIn": "_dataflow_280_LaunchTemplateParametersIn",
        "LaunchTemplateParametersOut": "_dataflow_281_LaunchTemplateParametersOut",
        "CounterUpdateIn": "_dataflow_282_CounterUpdateIn",
        "CounterUpdateOut": "_dataflow_283_CounterUpdateOut",
        "JobMetricsIn": "_dataflow_284_JobMetricsIn",
        "JobMetricsOut": "_dataflow_285_JobMetricsOut",
        "NameAndKindIn": "_dataflow_286_NameAndKindIn",
        "NameAndKindOut": "_dataflow_287_NameAndKindOut",
        "WorkerMessageIn": "_dataflow_288_WorkerMessageIn",
        "WorkerMessageOut": "_dataflow_289_WorkerMessageOut",
        "MountedDataDiskIn": "_dataflow_290_MountedDataDiskIn",
        "MountedDataDiskOut": "_dataflow_291_MountedDataDiskOut",
        "StreamingStageLocationIn": "_dataflow_292_StreamingStageLocationIn",
        "StreamingStageLocationOut": "_dataflow_293_StreamingStageLocationOut",
        "DistributionUpdateIn": "_dataflow_294_DistributionUpdateIn",
        "DistributionUpdateOut": "_dataflow_295_DistributionUpdateOut",
        "MemInfoIn": "_dataflow_296_MemInfoIn",
        "MemInfoOut": "_dataflow_297_MemInfoOut",
        "TransformSummaryIn": "_dataflow_298_TransformSummaryIn",
        "TransformSummaryOut": "_dataflow_299_TransformSummaryOut",
        "ApproximateProgressIn": "_dataflow_300_ApproximateProgressIn",
        "ApproximateProgressOut": "_dataflow_301_ApproximateProgressOut",
        "SendDebugCaptureRequestIn": "_dataflow_302_SendDebugCaptureRequestIn",
        "SendDebugCaptureRequestOut": "_dataflow_303_SendDebugCaptureRequestOut",
        "StreamingComputationTaskIn": "_dataflow_304_StreamingComputationTaskIn",
        "StreamingComputationTaskOut": "_dataflow_305_StreamingComputationTaskOut",
        "WorkerShutdownNoticeIn": "_dataflow_306_WorkerShutdownNoticeIn",
        "WorkerShutdownNoticeOut": "_dataflow_307_WorkerShutdownNoticeOut",
        "StreamingComputationRangesIn": "_dataflow_308_StreamingComputationRangesIn",
        "StreamingComputationRangesOut": "_dataflow_309_StreamingComputationRangesOut",
        "ListJobsResponseIn": "_dataflow_310_ListJobsResponseIn",
        "ListJobsResponseOut": "_dataflow_311_ListJobsResponseOut",
        "StateFamilyConfigIn": "_dataflow_312_StateFamilyConfigIn",
        "StateFamilyConfigOut": "_dataflow_313_StateFamilyConfigOut",
        "MetricStructuredNameIn": "_dataflow_314_MetricStructuredNameIn",
        "MetricStructuredNameOut": "_dataflow_315_MetricStructuredNameOut",
        "SourceMetadataIn": "_dataflow_316_SourceMetadataIn",
        "SourceMetadataOut": "_dataflow_317_SourceMetadataOut",
        "TaskRunnerSettingsIn": "_dataflow_318_TaskRunnerSettingsIn",
        "TaskRunnerSettingsOut": "_dataflow_319_TaskRunnerSettingsOut",
        "StragglerDebuggingInfoIn": "_dataflow_320_StragglerDebuggingInfoIn",
        "StragglerDebuggingInfoOut": "_dataflow_321_StragglerDebuggingInfoOut",
        "HistogramIn": "_dataflow_322_HistogramIn",
        "HistogramOut": "_dataflow_323_HistogramOut",
        "WorkerShutdownNoticeResponseIn": "_dataflow_324_WorkerShutdownNoticeResponseIn",
        "WorkerShutdownNoticeResponseOut": "_dataflow_325_WorkerShutdownNoticeResponseOut",
        "SeqMapTaskOutputInfoIn": "_dataflow_326_SeqMapTaskOutputInfoIn",
        "SeqMapTaskOutputInfoOut": "_dataflow_327_SeqMapTaskOutputInfoOut",
        "AutoscalingEventIn": "_dataflow_328_AutoscalingEventIn",
        "AutoscalingEventOut": "_dataflow_329_AutoscalingEventOut",
        "WorkItemDetailsIn": "_dataflow_330_WorkItemDetailsIn",
        "WorkItemDetailsOut": "_dataflow_331_WorkItemDetailsOut",
        "HotKeyDetectionIn": "_dataflow_332_HotKeyDetectionIn",
        "HotKeyDetectionOut": "_dataflow_333_HotKeyDetectionOut",
        "WorkerMessageCodeIn": "_dataflow_334_WorkerMessageCodeIn",
        "WorkerMessageCodeOut": "_dataflow_335_WorkerMessageCodeOut",
        "WorkerHealthReportIn": "_dataflow_336_WorkerHealthReportIn",
        "WorkerHealthReportOut": "_dataflow_337_WorkerHealthReportOut",
        "WorkerMessageResponseIn": "_dataflow_338_WorkerMessageResponseIn",
        "WorkerMessageResponseOut": "_dataflow_339_WorkerMessageResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TopologyConfigIn"] = t.struct(
        {
            "persistentStateVersion": t.integer().optional(),
            "forwardingKeyBits": t.integer().optional(),
            "computations": t.array(
                t.proxy(renames["ComputationTopologyIn"])
            ).optional(),
            "dataDiskAssignments": t.array(
                t.proxy(renames["DataDiskAssignmentIn"])
            ).optional(),
            "userStageToComputationNameMap": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["TopologyConfigIn"])
    types["TopologyConfigOut"] = t.struct(
        {
            "persistentStateVersion": t.integer().optional(),
            "forwardingKeyBits": t.integer().optional(),
            "computations": t.array(
                t.proxy(renames["ComputationTopologyOut"])
            ).optional(),
            "dataDiskAssignments": t.array(
                t.proxy(renames["DataDiskAssignmentOut"])
            ).optional(),
            "userStageToComputationNameMap": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TopologyConfigOut"])
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
    types["ParDoInstructionIn"] = t.struct(
        {
            "sideInputs": t.array(t.proxy(renames["SideInputInfoIn"])).optional(),
            "numOutputs": t.integer().optional(),
            "multiOutputInfos": t.array(
                t.proxy(renames["MultiOutputInfoIn"])
            ).optional(),
            "userFn": t.struct({"_": t.string().optional()}).optional(),
            "input": t.proxy(renames["InstructionInputIn"]).optional(),
        }
    ).named(renames["ParDoInstructionIn"])
    types["ParDoInstructionOut"] = t.struct(
        {
            "sideInputs": t.array(t.proxy(renames["SideInputInfoOut"])).optional(),
            "numOutputs": t.integer().optional(),
            "multiOutputInfos": t.array(
                t.proxy(renames["MultiOutputInfoOut"])
            ).optional(),
            "userFn": t.struct({"_": t.string().optional()}).optional(),
            "input": t.proxy(renames["InstructionInputOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParDoInstructionOut"])
    types["GetDebugConfigResponseIn"] = t.struct(
        {"config": t.string().optional()}
    ).named(renames["GetDebugConfigResponseIn"])
    types["GetDebugConfigResponseOut"] = t.struct(
        {
            "config": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetDebugConfigResponseOut"])
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
    types["SideInputInfoIn"] = t.struct(
        {
            "kind": t.struct({"_": t.string().optional()}).optional(),
            "sources": t.array(t.proxy(renames["SourceIn"])).optional(),
            "tag": t.string().optional(),
        }
    ).named(renames["SideInputInfoIn"])
    types["SideInputInfoOut"] = t.struct(
        {
            "kind": t.struct({"_": t.string().optional()}).optional(),
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SideInputInfoOut"])
    types["ApproximateSplitRequestIn"] = t.struct(
        {
            "position": t.proxy(renames["PositionIn"]).optional(),
            "fractionConsumed": t.number().optional(),
            "fractionOfRemainder": t.number().optional(),
        }
    ).named(renames["ApproximateSplitRequestIn"])
    types["ApproximateSplitRequestOut"] = t.struct(
        {
            "position": t.proxy(renames["PositionOut"]).optional(),
            "fractionConsumed": t.number().optional(),
            "fractionOfRemainder": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApproximateSplitRequestOut"])
    types["StragglerIn"] = t.struct(
        {
            "streamingStraggler": t.proxy(
                renames["StreamingStragglerInfoIn"]
            ).optional(),
            "batchStraggler": t.proxy(renames["StragglerInfoIn"]).optional(),
        }
    ).named(renames["StragglerIn"])
    types["StragglerOut"] = t.struct(
        {
            "streamingStraggler": t.proxy(
                renames["StreamingStragglerInfoOut"]
            ).optional(),
            "batchStraggler": t.proxy(renames["StragglerInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StragglerOut"])
    types["ResourceUtilizationReportIn"] = t.struct(
        {
            "containers": t.struct({"_": t.string().optional()}).optional(),
            "cpuTime": t.array(t.proxy(renames["CPUTimeIn"])).optional(),
            "memoryInfo": t.array(t.proxy(renames["MemInfoIn"])).optional(),
        }
    ).named(renames["ResourceUtilizationReportIn"])
    types["ResourceUtilizationReportOut"] = t.struct(
        {
            "containers": t.struct({"_": t.string().optional()}).optional(),
            "cpuTime": t.array(t.proxy(renames["CPUTimeOut"])).optional(),
            "memoryInfo": t.array(t.proxy(renames["MemInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceUtilizationReportOut"])
    types["ContainerSpecIn"] = t.struct(
        {
            "sdkInfo": t.proxy(renames["SDKInfoIn"]),
            "metadata": t.proxy(renames["TemplateMetadataIn"]).optional(),
            "imageRepositoryUsernameSecretId": t.string().optional(),
            "imageRepositoryPasswordSecretId": t.string().optional(),
            "image": t.string().optional(),
            "imageRepositoryCertPath": t.string().optional(),
            "defaultEnvironment": t.proxy(
                renames["FlexTemplateRuntimeEnvironmentIn"]
            ).optional(),
        }
    ).named(renames["ContainerSpecIn"])
    types["ContainerSpecOut"] = t.struct(
        {
            "sdkInfo": t.proxy(renames["SDKInfoOut"]),
            "metadata": t.proxy(renames["TemplateMetadataOut"]).optional(),
            "imageRepositoryUsernameSecretId": t.string().optional(),
            "imageRepositoryPasswordSecretId": t.string().optional(),
            "image": t.string().optional(),
            "imageRepositoryCertPath": t.string().optional(),
            "defaultEnvironment": t.proxy(
                renames["FlexTemplateRuntimeEnvironmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerSpecOut"])
    types["ReportWorkItemStatusResponseIn"] = t.struct(
        {
            "unifiedWorkerResponse": t.struct({"_": t.string().optional()}).optional(),
            "workItemServiceStates": t.array(
                t.proxy(renames["WorkItemServiceStateIn"])
            ).optional(),
        }
    ).named(renames["ReportWorkItemStatusResponseIn"])
    types["ReportWorkItemStatusResponseOut"] = t.struct(
        {
            "unifiedWorkerResponse": t.struct({"_": t.string().optional()}).optional(),
            "workItemServiceStates": t.array(
                t.proxy(renames["WorkItemServiceStateOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportWorkItemStatusResponseOut"])
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
    types["StreamingSetupTaskIn"] = t.struct(
        {
            "streamingComputationTopology": t.proxy(
                renames["TopologyConfigIn"]
            ).optional(),
            "snapshotConfig": t.proxy(
                renames["StreamingApplianceSnapshotConfigIn"]
            ).optional(),
            "receiveWorkPort": t.integer().optional(),
            "workerHarnessPort": t.integer().optional(),
            "drain": t.boolean().optional(),
        }
    ).named(renames["StreamingSetupTaskIn"])
    types["StreamingSetupTaskOut"] = t.struct(
        {
            "streamingComputationTopology": t.proxy(
                renames["TopologyConfigOut"]
            ).optional(),
            "snapshotConfig": t.proxy(
                renames["StreamingApplianceSnapshotConfigOut"]
            ).optional(),
            "receiveWorkPort": t.integer().optional(),
            "workerHarnessPort": t.integer().optional(),
            "drain": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingSetupTaskOut"])
    types["SourceGetMetadataRequestIn"] = t.struct(
        {"source": t.proxy(renames["SourceIn"]).optional()}
    ).named(renames["SourceGetMetadataRequestIn"])
    types["SourceGetMetadataRequestOut"] = t.struct(
        {
            "source": t.proxy(renames["SourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceGetMetadataRequestOut"])
    types["StreamLocationIn"] = t.struct(
        {
            "sideInputLocation": t.proxy(
                renames["StreamingSideInputLocationIn"]
            ).optional(),
            "streamingStageLocation": t.proxy(
                renames["StreamingStageLocationIn"]
            ).optional(),
            "customSourceLocation": t.proxy(
                renames["CustomSourceLocationIn"]
            ).optional(),
            "pubsubLocation": t.proxy(renames["PubsubLocationIn"]).optional(),
        }
    ).named(renames["StreamLocationIn"])
    types["StreamLocationOut"] = t.struct(
        {
            "sideInputLocation": t.proxy(
                renames["StreamingSideInputLocationOut"]
            ).optional(),
            "streamingStageLocation": t.proxy(
                renames["StreamingStageLocationOut"]
            ).optional(),
            "customSourceLocation": t.proxy(
                renames["CustomSourceLocationOut"]
            ).optional(),
            "pubsubLocation": t.proxy(renames["PubsubLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamLocationOut"])
    types["DeleteSnapshotResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteSnapshotResponseIn"]
    )
    types["DeleteSnapshotResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteSnapshotResponseOut"])
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
    types["StreamingApplianceSnapshotConfigIn"] = t.struct(
        {
            "importStateEndpoint": t.string().optional(),
            "snapshotId": t.string().optional(),
        }
    ).named(renames["StreamingApplianceSnapshotConfigIn"])
    types["StreamingApplianceSnapshotConfigOut"] = t.struct(
        {
            "importStateEndpoint": t.string().optional(),
            "snapshotId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingApplianceSnapshotConfigOut"])
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
    types["PubsubSnapshotMetadataIn"] = t.struct(
        {
            "topicName": t.string().optional(),
            "expireTime": t.string().optional(),
            "snapshotName": t.string().optional(),
        }
    ).named(renames["PubsubSnapshotMetadataIn"])
    types["PubsubSnapshotMetadataOut"] = t.struct(
        {
            "topicName": t.string().optional(),
            "expireTime": t.string().optional(),
            "snapshotName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubSnapshotMetadataOut"])
    types["WorkItemStatusIn"] = t.struct(
        {
            "completed": t.boolean().optional(),
            "metricUpdates": t.array(t.proxy(renames["MetricUpdateIn"])).optional(),
            "sourceFork": t.proxy(renames["SourceForkIn"]).optional(),
            "errors": t.array(t.proxy(renames["StatusIn"])).optional(),
            "reportIndex": t.string().optional(),
            "reportedProgress": t.proxy(
                renames["ApproximateReportedProgressIn"]
            ).optional(),
            "stopPosition": t.proxy(renames["PositionIn"]).optional(),
            "dynamicSourceSplit": t.proxy(renames["DynamicSourceSplitIn"]).optional(),
            "progress": t.proxy(renames["ApproximateProgressIn"]).optional(),
            "workItemId": t.string().optional(),
            "sourceOperationResponse": t.proxy(
                renames["SourceOperationResponseIn"]
            ).optional(),
            "counterUpdates": t.array(t.proxy(renames["CounterUpdateIn"])).optional(),
            "requestedLeaseDuration": t.string().optional(),
            "totalThrottlerWaitTimeSeconds": t.number().optional(),
        }
    ).named(renames["WorkItemStatusIn"])
    types["WorkItemStatusOut"] = t.struct(
        {
            "completed": t.boolean().optional(),
            "metricUpdates": t.array(t.proxy(renames["MetricUpdateOut"])).optional(),
            "sourceFork": t.proxy(renames["SourceForkOut"]).optional(),
            "errors": t.array(t.proxy(renames["StatusOut"])).optional(),
            "reportIndex": t.string().optional(),
            "reportedProgress": t.proxy(
                renames["ApproximateReportedProgressOut"]
            ).optional(),
            "stopPosition": t.proxy(renames["PositionOut"]).optional(),
            "dynamicSourceSplit": t.proxy(renames["DynamicSourceSplitOut"]).optional(),
            "progress": t.proxy(renames["ApproximateProgressOut"]).optional(),
            "workItemId": t.string().optional(),
            "sourceOperationResponse": t.proxy(
                renames["SourceOperationResponseOut"]
            ).optional(),
            "counterUpdates": t.array(t.proxy(renames["CounterUpdateOut"])).optional(),
            "requestedLeaseDuration": t.string().optional(),
            "totalThrottlerWaitTimeSeconds": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkItemStatusOut"])
    types["LaunchFlexTemplateRequestIn"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "launchParameter": t.proxy(renames["LaunchFlexTemplateParameterIn"]),
        }
    ).named(renames["LaunchFlexTemplateRequestIn"])
    types["LaunchFlexTemplateRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "launchParameter": t.proxy(renames["LaunchFlexTemplateParameterOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LaunchFlexTemplateRequestOut"])
    types["StageSourceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "originalTransformOrCollection": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "userName": t.string().optional(),
        }
    ).named(renames["StageSourceIn"])
    types["StageSourceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "originalTransformOrCollection": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "userName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StageSourceOut"])
    types["DisplayDataIn"] = t.struct(
        {
            "shortStrValue": t.string().optional(),
            "javaClassValue": t.string().optional(),
            "durationValue": t.string().optional(),
            "strValue": t.string().optional(),
            "floatValue": t.number().optional(),
            "namespace": t.string().optional(),
            "label": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "timestampValue": t.string().optional(),
            "url": t.string().optional(),
            "key": t.string().optional(),
            "int64Value": t.string().optional(),
        }
    ).named(renames["DisplayDataIn"])
    types["DisplayDataOut"] = t.struct(
        {
            "shortStrValue": t.string().optional(),
            "javaClassValue": t.string().optional(),
            "durationValue": t.string().optional(),
            "strValue": t.string().optional(),
            "floatValue": t.number().optional(),
            "namespace": t.string().optional(),
            "label": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "timestampValue": t.string().optional(),
            "url": t.string().optional(),
            "key": t.string().optional(),
            "int64Value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisplayDataOut"])
    types["CreateJobFromTemplateRequestIn"] = t.struct(
        {
            "gcsPath": t.string(),
            "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
            "jobName": t.string(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "location": t.string().optional(),
        }
    ).named(renames["CreateJobFromTemplateRequestIn"])
    types["CreateJobFromTemplateRequestOut"] = t.struct(
        {
            "gcsPath": t.string(),
            "environment": t.proxy(renames["RuntimeEnvironmentOut"]).optional(),
            "jobName": t.string(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateJobFromTemplateRequestOut"])
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
    types["LeaseWorkItemRequestIn"] = t.struct(
        {
            "workerCapabilities": t.array(t.string()).optional(),
            "location": t.string().optional(),
            "workerId": t.string().optional(),
            "unifiedWorkerRequest": t.struct({"_": t.string().optional()}).optional(),
            "workItemTypes": t.array(t.string()).optional(),
            "currentWorkerTime": t.string().optional(),
            "requestedLeaseDuration": t.string().optional(),
        }
    ).named(renames["LeaseWorkItemRequestIn"])
    types["LeaseWorkItemRequestOut"] = t.struct(
        {
            "workerCapabilities": t.array(t.string()).optional(),
            "location": t.string().optional(),
            "workerId": t.string().optional(),
            "unifiedWorkerRequest": t.struct({"_": t.string().optional()}).optional(),
            "workItemTypes": t.array(t.string()).optional(),
            "currentWorkerTime": t.string().optional(),
            "requestedLeaseDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LeaseWorkItemRequestOut"])
    types["ReadInstructionIn"] = t.struct(
        {"source": t.proxy(renames["SourceIn"]).optional()}
    ).named(renames["ReadInstructionIn"])
    types["ReadInstructionOut"] = t.struct(
        {
            "source": t.proxy(renames["SourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadInstructionOut"])
    types["SnapshotIn"] = t.struct(
        {
            "ttl": t.string().optional(),
            "pubsubMetadata": t.array(
                t.proxy(renames["PubsubSnapshotMetadataIn"])
            ).optional(),
            "diskSizeBytes": t.string().optional(),
            "state": t.string().optional(),
            "id": t.string().optional(),
            "creationTime": t.string().optional(),
            "sourceJobId": t.string().optional(),
            "projectId": t.string().optional(),
            "region": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["SnapshotIn"])
    types["SnapshotOut"] = t.struct(
        {
            "ttl": t.string().optional(),
            "pubsubMetadata": t.array(
                t.proxy(renames["PubsubSnapshotMetadataOut"])
            ).optional(),
            "diskSizeBytes": t.string().optional(),
            "state": t.string().optional(),
            "id": t.string().optional(),
            "creationTime": t.string().optional(),
            "sourceJobId": t.string().optional(),
            "projectId": t.string().optional(),
            "region": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnapshotOut"])
    types["FileIODetailsIn"] = t.struct({"filePattern": t.string().optional()}).named(
        renames["FileIODetailsIn"]
    )
    types["FileIODetailsOut"] = t.struct(
        {
            "filePattern": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileIODetailsOut"])
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
    types["SourceGetMetadataResponseIn"] = t.struct(
        {"metadata": t.proxy(renames["SourceMetadataIn"]).optional()}
    ).named(renames["SourceGetMetadataResponseIn"])
    types["SourceGetMetadataResponseOut"] = t.struct(
        {
            "metadata": t.proxy(renames["SourceMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceGetMetadataResponseOut"])
    types["ResourceUtilizationReportResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ResourceUtilizationReportResponseIn"])
    types["ResourceUtilizationReportResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResourceUtilizationReportResponseOut"])
    types["DerivedSourceIn"] = t.struct(
        {
            "derivationMode": t.string().optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
        }
    ).named(renames["DerivedSourceIn"])
    types["DerivedSourceOut"] = t.struct(
        {
            "derivationMode": t.string().optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DerivedSourceOut"])
    types["LaunchFlexTemplateParameterIn"] = t.struct(
        {
            "launchOptions": t.struct({"_": t.string().optional()}).optional(),
            "containerSpecGcsPath": t.string().optional(),
            "environment": t.proxy(
                renames["FlexTemplateRuntimeEnvironmentIn"]
            ).optional(),
            "containerSpec": t.proxy(renames["ContainerSpecIn"]).optional(),
            "update": t.boolean().optional(),
            "jobName": t.string(),
            "transformNameMappings": t.struct({"_": t.string().optional()}).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LaunchFlexTemplateParameterIn"])
    types["LaunchFlexTemplateParameterOut"] = t.struct(
        {
            "launchOptions": t.struct({"_": t.string().optional()}).optional(),
            "containerSpecGcsPath": t.string().optional(),
            "environment": t.proxy(
                renames["FlexTemplateRuntimeEnvironmentOut"]
            ).optional(),
            "containerSpec": t.proxy(renames["ContainerSpecOut"]).optional(),
            "update": t.boolean().optional(),
            "jobName": t.string(),
            "transformNameMappings": t.struct({"_": t.string().optional()}).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LaunchFlexTemplateParameterOut"])
    types["LaunchTemplateResponseIn"] = t.struct(
        {"job": t.proxy(renames["JobIn"]).optional()}
    ).named(renames["LaunchTemplateResponseIn"])
    types["LaunchTemplateResponseOut"] = t.struct(
        {
            "job": t.proxy(renames["JobOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LaunchTemplateResponseOut"])
    types["SourceSplitResponseIn"] = t.struct(
        {
            "bundles": t.array(t.proxy(renames["DerivedSourceIn"])).optional(),
            "outcome": t.string().optional(),
            "shards": t.array(t.proxy(renames["SourceSplitShardIn"])).optional(),
        }
    ).named(renames["SourceSplitResponseIn"])
    types["SourceSplitResponseOut"] = t.struct(
        {
            "bundles": t.array(t.proxy(renames["DerivedSourceOut"])).optional(),
            "outcome": t.string().optional(),
            "shards": t.array(t.proxy(renames["SourceSplitShardOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceSplitResponseOut"])
    types["CounterMetadataIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "otherUnits": t.string().optional(),
            "standardUnits": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["CounterMetadataIn"])
    types["CounterMetadataOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "otherUnits": t.string().optional(),
            "standardUnits": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CounterMetadataOut"])
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
    types["ShellTaskIn"] = t.struct(
        {"command": t.string().optional(), "exitCode": t.integer().optional()}
    ).named(renames["ShellTaskIn"])
    types["ShellTaskOut"] = t.struct(
        {
            "command": t.string().optional(),
            "exitCode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShellTaskOut"])
    types["ParameterMetadataIn"] = t.struct(
        {
            "paramType": t.string().optional(),
            "isOptional": t.boolean().optional(),
            "regexes": t.array(t.string()).optional(),
            "name": t.string(),
            "parentTriggerValues": t.array(t.string()).optional(),
            "groupName": t.string().optional(),
            "customMetadata": t.struct({"_": t.string().optional()}).optional(),
            "parentName": t.string().optional(),
            "label": t.string(),
            "helpText": t.string(),
        }
    ).named(renames["ParameterMetadataIn"])
    types["ParameterMetadataOut"] = t.struct(
        {
            "paramType": t.string().optional(),
            "isOptional": t.boolean().optional(),
            "regexes": t.array(t.string()).optional(),
            "name": t.string(),
            "parentTriggerValues": t.array(t.string()).optional(),
            "groupName": t.string().optional(),
            "customMetadata": t.struct({"_": t.string().optional()}).optional(),
            "parentName": t.string().optional(),
            "label": t.string(),
            "helpText": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParameterMetadataOut"])
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
    types["DebugOptionsIn"] = t.struct(
        {"enableHotKeyLogging": t.boolean().optional()}
    ).named(renames["DebugOptionsIn"])
    types["DebugOptionsOut"] = t.struct(
        {
            "enableHotKeyLogging": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DebugOptionsOut"])
    types["MetricUpdateIn"] = t.struct(
        {
            "internal": t.struct({"_": t.string().optional()}).optional(),
            "meanSum": t.struct({"_": t.string().optional()}).optional(),
            "gauge": t.struct({"_": t.string().optional()}).optional(),
            "distribution": t.struct({"_": t.string().optional()}).optional(),
            "name": t.proxy(renames["MetricStructuredNameIn"]).optional(),
            "cumulative": t.boolean().optional(),
            "scalar": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "updateTime": t.string().optional(),
            "meanCount": t.struct({"_": t.string().optional()}).optional(),
            "set": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["MetricUpdateIn"])
    types["MetricUpdateOut"] = t.struct(
        {
            "internal": t.struct({"_": t.string().optional()}).optional(),
            "meanSum": t.struct({"_": t.string().optional()}).optional(),
            "gauge": t.struct({"_": t.string().optional()}).optional(),
            "distribution": t.struct({"_": t.string().optional()}).optional(),
            "name": t.proxy(renames["MetricStructuredNameOut"]).optional(),
            "cumulative": t.boolean().optional(),
            "scalar": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "updateTime": t.string().optional(),
            "meanCount": t.struct({"_": t.string().optional()}).optional(),
            "set": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricUpdateOut"])
    types["SinkIn"] = t.struct(
        {
            "codec": t.struct({"_": t.string().optional()}).optional(),
            "spec": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SinkIn"])
    types["SinkOut"] = t.struct(
        {
            "codec": t.struct({"_": t.string().optional()}).optional(),
            "spec": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SinkOut"])
    types["GetTemplateResponseIn"] = t.struct(
        {
            "templateType": t.string().optional(),
            "status": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.proxy(renames["TemplateMetadataIn"]).optional(),
            "runtimeMetadata": t.proxy(renames["RuntimeMetadataIn"]).optional(),
        }
    ).named(renames["GetTemplateResponseIn"])
    types["GetTemplateResponseOut"] = t.struct(
        {
            "templateType": t.string().optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "metadata": t.proxy(renames["TemplateMetadataOut"]).optional(),
            "runtimeMetadata": t.proxy(renames["RuntimeMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetTemplateResponseOut"])
    types["PipelineDescriptionIn"] = t.struct(
        {
            "executionPipelineStage": t.array(
                t.proxy(renames["ExecutionStageSummaryIn"])
            ).optional(),
            "stepNamesHash": t.string().optional(),
            "displayData": t.array(t.proxy(renames["DisplayDataIn"])).optional(),
            "originalPipelineTransform": t.array(
                t.proxy(renames["TransformSummaryIn"])
            ).optional(),
        }
    ).named(renames["PipelineDescriptionIn"])
    types["PipelineDescriptionOut"] = t.struct(
        {
            "executionPipelineStage": t.array(
                t.proxy(renames["ExecutionStageSummaryOut"])
            ).optional(),
            "stepNamesHash": t.string().optional(),
            "displayData": t.array(t.proxy(renames["DisplayDataOut"])).optional(),
            "originalPipelineTransform": t.array(
                t.proxy(renames["TransformSummaryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PipelineDescriptionOut"])
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
    types["StringListIn"] = t.struct(
        {"elements": t.array(t.string()).optional()}
    ).named(renames["StringListIn"])
    types["StringListOut"] = t.struct(
        {
            "elements": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StringListOut"])
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
    types["CustomSourceLocationIn"] = t.struct(
        {"stateful": t.boolean().optional()}
    ).named(renames["CustomSourceLocationIn"])
    types["CustomSourceLocationOut"] = t.struct(
        {
            "stateful": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomSourceLocationOut"])
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
    types["ExecutionStageSummaryIn"] = t.struct(
        {
            "prerequisiteStage": t.array(t.string()).optional(),
            "outputSource": t.array(t.proxy(renames["StageSourceIn"])).optional(),
            "inputSource": t.array(t.proxy(renames["StageSourceIn"])).optional(),
            "componentTransform": t.array(
                t.proxy(renames["ComponentTransformIn"])
            ).optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "componentSource": t.array(
                t.proxy(renames["ComponentSourceIn"])
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ExecutionStageSummaryIn"])
    types["ExecutionStageSummaryOut"] = t.struct(
        {
            "prerequisiteStage": t.array(t.string()).optional(),
            "outputSource": t.array(t.proxy(renames["StageSourceOut"])).optional(),
            "inputSource": t.array(t.proxy(renames["StageSourceOut"])).optional(),
            "componentTransform": t.array(
                t.proxy(renames["ComponentTransformOut"])
            ).optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "componentSource": t.array(
                t.proxy(renames["ComponentSourceOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionStageSummaryOut"])
    types["StragglerInfoIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "causes": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["StragglerInfoIn"])
    types["StragglerInfoOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "causes": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StragglerInfoOut"])
    types["StreamingSideInputLocationIn"] = t.struct(
        {"stateFamily": t.string().optional(), "tag": t.string().optional()}
    ).named(renames["StreamingSideInputLocationIn"])
    types["StreamingSideInputLocationOut"] = t.struct(
        {
            "stateFamily": t.string().optional(),
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingSideInputLocationOut"])
    types["SourceSplitRequestIn"] = t.struct(
        {
            "source": t.proxy(renames["SourceIn"]).optional(),
            "options": t.proxy(renames["SourceSplitOptionsIn"]).optional(),
        }
    ).named(renames["SourceSplitRequestIn"])
    types["SourceSplitRequestOut"] = t.struct(
        {
            "source": t.proxy(renames["SourceOut"]).optional(),
            "options": t.proxy(renames["SourceSplitOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceSplitRequestOut"])
    types["CPUTimeIn"] = t.struct(
        {
            "totalMs": t.string().optional(),
            "rate": t.number().optional(),
            "timestamp": t.string().optional(),
        }
    ).named(renames["CPUTimeIn"])
    types["CPUTimeOut"] = t.struct(
        {
            "totalMs": t.string().optional(),
            "rate": t.number().optional(),
            "timestamp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CPUTimeOut"])
    types["BigTableIODetailsIn"] = t.struct(
        {
            "instanceId": t.string().optional(),
            "projectId": t.string().optional(),
            "tableId": t.string().optional(),
        }
    ).named(renames["BigTableIODetailsIn"])
    types["BigTableIODetailsOut"] = t.struct(
        {
            "instanceId": t.string().optional(),
            "projectId": t.string().optional(),
            "tableId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigTableIODetailsOut"])
    types["ExecutionStageStateIn"] = t.struct(
        {
            "currentStateTime": t.string().optional(),
            "executionStageName": t.string().optional(),
            "executionStageState": t.string().optional(),
        }
    ).named(renames["ExecutionStageStateIn"])
    types["ExecutionStageStateOut"] = t.struct(
        {
            "currentStateTime": t.string().optional(),
            "executionStageName": t.string().optional(),
            "executionStageState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionStageStateOut"])
    types["WorkerPoolIn"] = t.struct(
        {
            "workerHarnessContainerImage": t.string(),
            "dataDisks": t.array(t.proxy(renames["DiskIn"])).optional(),
            "numWorkers": t.integer().optional(),
            "diskSizeGb": t.integer().optional(),
            "defaultPackageSet": t.string().optional(),
            "machineType": t.string().optional(),
            "ipConfiguration": t.string().optional(),
            "network": t.string().optional(),
            "teardownPolicy": t.string().optional(),
            "autoscalingSettings": t.proxy(renames["AutoscalingSettingsIn"]).optional(),
            "sdkHarnessContainerImages": t.array(
                t.proxy(renames["SdkHarnessContainerImageIn"])
            ).optional(),
            "onHostMaintenance": t.string().optional(),
            "kind": t.string().optional(),
            "poolArgs": t.struct({"_": t.string().optional()}).optional(),
            "diskSourceImage": t.string().optional(),
            "zone": t.string().optional(),
            "diskType": t.string().optional(),
            "numThreadsPerWorker": t.integer().optional(),
            "subnetwork": t.string().optional(),
            "packages": t.array(t.proxy(renames["PackageIn"])).optional(),
            "taskrunnerSettings": t.proxy(renames["TaskRunnerSettingsIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["WorkerPoolIn"])
    types["WorkerPoolOut"] = t.struct(
        {
            "workerHarnessContainerImage": t.string(),
            "dataDisks": t.array(t.proxy(renames["DiskOut"])).optional(),
            "numWorkers": t.integer().optional(),
            "diskSizeGb": t.integer().optional(),
            "defaultPackageSet": t.string().optional(),
            "machineType": t.string().optional(),
            "ipConfiguration": t.string().optional(),
            "network": t.string().optional(),
            "teardownPolicy": t.string().optional(),
            "autoscalingSettings": t.proxy(
                renames["AutoscalingSettingsOut"]
            ).optional(),
            "sdkHarnessContainerImages": t.array(
                t.proxy(renames["SdkHarnessContainerImageOut"])
            ).optional(),
            "onHostMaintenance": t.string().optional(),
            "kind": t.string().optional(),
            "poolArgs": t.struct({"_": t.string().optional()}).optional(),
            "diskSourceImage": t.string().optional(),
            "zone": t.string().optional(),
            "diskType": t.string().optional(),
            "numThreadsPerWorker": t.integer().optional(),
            "subnetwork": t.string().optional(),
            "packages": t.array(t.proxy(renames["PackageOut"])).optional(),
            "taskrunnerSettings": t.proxy(renames["TaskRunnerSettingsOut"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerPoolOut"])
    types["EnvironmentIn"] = t.struct(
        {
            "internalExperiments": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccountEmail": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "sdkPipelineOptions": t.struct({"_": t.string().optional()}).optional(),
            "clusterManagerApiService": t.string().optional(),
            "workerRegion": t.string().optional(),
            "version": t.struct({"_": t.string().optional()}).optional(),
            "serviceKmsKeyName": t.string().optional(),
            "experiments": t.array(t.string()).optional(),
            "tempStoragePrefix": t.string().optional(),
            "flexResourceSchedulingGoal": t.string().optional(),
            "workerZone": t.string().optional(),
            "serviceOptions": t.array(t.string()).optional(),
            "workerPools": t.array(t.proxy(renames["WorkerPoolIn"])).optional(),
            "userAgent": t.struct({"_": t.string().optional()}).optional(),
            "dataset": t.string().optional(),
        }
    ).named(renames["EnvironmentIn"])
    types["EnvironmentOut"] = t.struct(
        {
            "shuffleMode": t.string().optional(),
            "internalExperiments": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccountEmail": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "sdkPipelineOptions": t.struct({"_": t.string().optional()}).optional(),
            "clusterManagerApiService": t.string().optional(),
            "workerRegion": t.string().optional(),
            "version": t.struct({"_": t.string().optional()}).optional(),
            "serviceKmsKeyName": t.string().optional(),
            "experiments": t.array(t.string()).optional(),
            "tempStoragePrefix": t.string().optional(),
            "flexResourceSchedulingGoal": t.string().optional(),
            "workerZone": t.string().optional(),
            "serviceOptions": t.array(t.string()).optional(),
            "workerPools": t.array(t.proxy(renames["WorkerPoolOut"])).optional(),
            "userAgent": t.struct({"_": t.string().optional()}).optional(),
            "dataset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentOut"])
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
    types["SpannerIODetailsIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "instanceId": t.string().optional(),
            "databaseId": t.string().optional(),
        }
    ).named(renames["SpannerIODetailsIn"])
    types["SpannerIODetailsOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "instanceId": t.string().optional(),
            "databaseId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpannerIODetailsOut"])
    types["ParallelInstructionIn"] = t.struct(
        {
            "read": t.proxy(renames["ReadInstructionIn"]).optional(),
            "flatten": t.proxy(renames["FlattenInstructionIn"]).optional(),
            "partialGroupByKey": t.proxy(
                renames["PartialGroupByKeyInstructionIn"]
            ).optional(),
            "name": t.string().optional(),
            "parDo": t.proxy(renames["ParDoInstructionIn"]).optional(),
            "originalName": t.string().optional(),
            "outputs": t.array(t.proxy(renames["InstructionOutputIn"])).optional(),
            "write": t.proxy(renames["WriteInstructionIn"]).optional(),
            "systemName": t.string().optional(),
        }
    ).named(renames["ParallelInstructionIn"])
    types["ParallelInstructionOut"] = t.struct(
        {
            "read": t.proxy(renames["ReadInstructionOut"]).optional(),
            "flatten": t.proxy(renames["FlattenInstructionOut"]).optional(),
            "partialGroupByKey": t.proxy(
                renames["PartialGroupByKeyInstructionOut"]
            ).optional(),
            "name": t.string().optional(),
            "parDo": t.proxy(renames["ParDoInstructionOut"]).optional(),
            "originalName": t.string().optional(),
            "outputs": t.array(t.proxy(renames["InstructionOutputOut"])).optional(),
            "write": t.proxy(renames["WriteInstructionOut"]).optional(),
            "systemName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParallelInstructionOut"])
    types["HotKeyInfoIn"] = t.struct(
        {
            "keyTruncated": t.boolean().optional(),
            "key": t.string().optional(),
            "hotKeyAge": t.string().optional(),
        }
    ).named(renames["HotKeyInfoIn"])
    types["HotKeyInfoOut"] = t.struct(
        {
            "keyTruncated": t.boolean().optional(),
            "key": t.string().optional(),
            "hotKeyAge": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HotKeyInfoOut"])
    types["FailedLocationIn"] = t.struct({"name": t.string().optional()}).named(
        renames["FailedLocationIn"]
    )
    types["FailedLocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FailedLocationOut"])
    types["WorkerSettingsIn"] = t.struct(
        {
            "servicePath": t.string().optional(),
            "shuffleServicePath": t.string().optional(),
            "reportingEnabled": t.boolean().optional(),
            "workerId": t.string().optional(),
            "tempStoragePrefix": t.string().optional(),
            "baseUrl": t.string().optional(),
        }
    ).named(renames["WorkerSettingsIn"])
    types["WorkerSettingsOut"] = t.struct(
        {
            "servicePath": t.string().optional(),
            "shuffleServicePath": t.string().optional(),
            "reportingEnabled": t.boolean().optional(),
            "workerId": t.string().optional(),
            "tempStoragePrefix": t.string().optional(),
            "baseUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerSettingsOut"])
    types["JobIn"] = t.struct(
        {
            "createdFromSnapshotId": t.string().optional(),
            "location": t.string().optional(),
            "tempFiles": t.array(t.string()).optional(),
            "projectId": t.string().optional(),
            "runtimeUpdatableParams": t.proxy(
                renames["RuntimeUpdatableParamsIn"]
            ).optional(),
            "transformNameMapping": t.struct({"_": t.string().optional()}).optional(),
            "stepsLocation": t.string().optional(),
            "id": t.string().optional(),
            "currentState": t.string().optional(),
            "type": t.string().optional(),
            "pipelineDescription": t.proxy(renames["PipelineDescriptionIn"]).optional(),
            "jobMetadata": t.proxy(renames["JobMetadataIn"]).optional(),
            "startTime": t.string().optional(),
            "replacedByJobId": t.string().optional(),
            "stageStates": t.array(
                t.proxy(renames["ExecutionStageStateIn"])
            ).optional(),
            "clientRequestId": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedState": t.string().optional(),
            "name": t.string().optional(),
            "environment": t.proxy(renames["EnvironmentIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "currentStateTime": t.string().optional(),
            "replaceJobId": t.string().optional(),
            "steps": t.array(t.proxy(renames["StepIn"])).optional(),
            "executionInfo": t.proxy(renames["JobExecutionInfoIn"]).optional(),
            "satisfiesPzs": t.boolean().optional(),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "createdFromSnapshotId": t.string().optional(),
            "location": t.string().optional(),
            "tempFiles": t.array(t.string()).optional(),
            "projectId": t.string().optional(),
            "runtimeUpdatableParams": t.proxy(
                renames["RuntimeUpdatableParamsOut"]
            ).optional(),
            "transformNameMapping": t.struct({"_": t.string().optional()}).optional(),
            "stepsLocation": t.string().optional(),
            "id": t.string().optional(),
            "currentState": t.string().optional(),
            "type": t.string().optional(),
            "pipelineDescription": t.proxy(
                renames["PipelineDescriptionOut"]
            ).optional(),
            "jobMetadata": t.proxy(renames["JobMetadataOut"]).optional(),
            "startTime": t.string().optional(),
            "replacedByJobId": t.string().optional(),
            "stageStates": t.array(
                t.proxy(renames["ExecutionStageStateOut"])
            ).optional(),
            "clientRequestId": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedState": t.string().optional(),
            "name": t.string().optional(),
            "environment": t.proxy(renames["EnvironmentOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "currentStateTime": t.string().optional(),
            "replaceJobId": t.string().optional(),
            "steps": t.array(t.proxy(renames["StepOut"])).optional(),
            "executionInfo": t.proxy(renames["JobExecutionInfoOut"]).optional(),
            "satisfiesPzs": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
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
    types["JobMessageIn"] = t.struct(
        {
            "id": t.string().optional(),
            "messageImportance": t.string().optional(),
            "messageText": t.string().optional(),
            "time": t.string().optional(),
        }
    ).named(renames["JobMessageIn"])
    types["JobMessageOut"] = t.struct(
        {
            "id": t.string().optional(),
            "messageImportance": t.string().optional(),
            "messageText": t.string().optional(),
            "time": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobMessageOut"])
    types["MultiOutputInfoIn"] = t.struct({"tag": t.string().optional()}).named(
        renames["MultiOutputInfoIn"]
    )
    types["MultiOutputInfoOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultiOutputInfoOut"])
    types["WorkerThreadScalingReportIn"] = t.struct(
        {"currentThreadCount": t.integer().optional()}
    ).named(renames["WorkerThreadScalingReportIn"])
    types["WorkerThreadScalingReportOut"] = t.struct(
        {
            "currentThreadCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerThreadScalingReportOut"])
    types["FloatingPointListIn"] = t.struct(
        {"elements": t.array(t.number()).optional()}
    ).named(renames["FloatingPointListIn"])
    types["FloatingPointListOut"] = t.struct(
        {
            "elements": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloatingPointListOut"])
    types["StreamingConfigTaskIn"] = t.struct(
        {
            "streamingComputationConfigs": t.array(
                t.proxy(renames["StreamingComputationConfigIn"])
            ).optional(),
            "maxWorkItemCommitBytes": t.string().optional(),
            "userStepToStateFamilyNameMap": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "getDataStreamChunkSizeBytes": t.string().optional(),
            "windmillServicePort": t.string().optional(),
            "windmillServiceEndpoint": t.string().optional(),
            "commitStreamChunkSizeBytes": t.string().optional(),
        }
    ).named(renames["StreamingConfigTaskIn"])
    types["StreamingConfigTaskOut"] = t.struct(
        {
            "streamingComputationConfigs": t.array(
                t.proxy(renames["StreamingComputationConfigOut"])
            ).optional(),
            "maxWorkItemCommitBytes": t.string().optional(),
            "userStepToStateFamilyNameMap": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "getDataStreamChunkSizeBytes": t.string().optional(),
            "windmillServicePort": t.string().optional(),
            "windmillServiceEndpoint": t.string().optional(),
            "commitStreamChunkSizeBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingConfigTaskOut"])
    types["ProgressTimeseriesIn"] = t.struct(
        {
            "dataPoints": t.array(t.proxy(renames["PointIn"])).optional(),
            "currentProgress": t.number().optional(),
        }
    ).named(renames["ProgressTimeseriesIn"])
    types["ProgressTimeseriesOut"] = t.struct(
        {
            "dataPoints": t.array(t.proxy(renames["PointOut"])).optional(),
            "currentProgress": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProgressTimeseriesOut"])
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
    types["IntegerListIn"] = t.struct(
        {"elements": t.array(t.proxy(renames["SplitInt64In"])).optional()}
    ).named(renames["IntegerListIn"])
    types["IntegerListOut"] = t.struct(
        {
            "elements": t.array(t.proxy(renames["SplitInt64Out"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerListOut"])
    types["StragglerSummaryIn"] = t.struct(
        {
            "totalStragglerCount": t.string().optional(),
            "stragglerCauseCount": t.struct({"_": t.string().optional()}).optional(),
            "recentStragglers": t.array(t.proxy(renames["StragglerIn"])).optional(),
        }
    ).named(renames["StragglerSummaryIn"])
    types["StragglerSummaryOut"] = t.struct(
        {
            "totalStragglerCount": t.string().optional(),
            "stragglerCauseCount": t.struct({"_": t.string().optional()}).optional(),
            "recentStragglers": t.array(t.proxy(renames["StragglerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StragglerSummaryOut"])
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
    types["SdkHarnessContainerImageIn"] = t.struct(
        {
            "useSingleCorePerContainer": t.boolean().optional(),
            "capabilities": t.array(t.string()).optional(),
            "containerImage": t.string().optional(),
            "environmentId": t.string().optional(),
        }
    ).named(renames["SdkHarnessContainerImageIn"])
    types["SdkHarnessContainerImageOut"] = t.struct(
        {
            "useSingleCorePerContainer": t.boolean().optional(),
            "capabilities": t.array(t.string()).optional(),
            "containerImage": t.string().optional(),
            "environmentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SdkHarnessContainerImageOut"])
    types["PositionIn"] = t.struct(
        {
            "shufflePosition": t.string().optional(),
            "key": t.string().optional(),
            "recordIndex": t.string().optional(),
            "byteOffset": t.string().optional(),
            "end": t.boolean().optional(),
            "concatPosition": t.proxy(renames["ConcatPositionIn"]).optional(),
        }
    ).named(renames["PositionIn"])
    types["PositionOut"] = t.struct(
        {
            "shufflePosition": t.string().optional(),
            "key": t.string().optional(),
            "recordIndex": t.string().optional(),
            "byteOffset": t.string().optional(),
            "end": t.boolean().optional(),
            "concatPosition": t.proxy(renames["ConcatPositionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PositionOut"])
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
            "parameters": t.array(t.proxy(renames["ParameterIn"])).optional(),
            "messageText": t.string().optional(),
            "messageKey": t.string().optional(),
        }
    ).named(renames["StructuredMessageIn"])
    types["StructuredMessageOut"] = t.struct(
        {
            "parameters": t.array(t.proxy(renames["ParameterOut"])).optional(),
            "messageText": t.string().optional(),
            "messageKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructuredMessageOut"])
    types["JobMetadataIn"] = t.struct(
        {
            "datastoreDetails": t.array(
                t.proxy(renames["DatastoreIODetailsIn"])
            ).optional(),
            "bigqueryDetails": t.array(
                t.proxy(renames["BigQueryIODetailsIn"])
            ).optional(),
            "pubsubDetails": t.array(t.proxy(renames["PubSubIODetailsIn"])).optional(),
            "spannerDetails": t.array(
                t.proxy(renames["SpannerIODetailsIn"])
            ).optional(),
            "fileDetails": t.array(t.proxy(renames["FileIODetailsIn"])).optional(),
            "userDisplayProperties": t.struct({"_": t.string().optional()}).optional(),
            "bigTableDetails": t.array(
                t.proxy(renames["BigTableIODetailsIn"])
            ).optional(),
            "sdkVersion": t.proxy(renames["SdkVersionIn"]).optional(),
        }
    ).named(renames["JobMetadataIn"])
    types["JobMetadataOut"] = t.struct(
        {
            "datastoreDetails": t.array(
                t.proxy(renames["DatastoreIODetailsOut"])
            ).optional(),
            "bigqueryDetails": t.array(
                t.proxy(renames["BigQueryIODetailsOut"])
            ).optional(),
            "pubsubDetails": t.array(t.proxy(renames["PubSubIODetailsOut"])).optional(),
            "spannerDetails": t.array(
                t.proxy(renames["SpannerIODetailsOut"])
            ).optional(),
            "fileDetails": t.array(t.proxy(renames["FileIODetailsOut"])).optional(),
            "userDisplayProperties": t.struct({"_": t.string().optional()}).optional(),
            "bigTableDetails": t.array(
                t.proxy(renames["BigTableIODetailsOut"])
            ).optional(),
            "sdkVersion": t.proxy(renames["SdkVersionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobMetadataOut"])
    types["ComputationTopologyIn"] = t.struct(
        {
            "keyRanges": t.array(t.proxy(renames["KeyRangeLocationIn"])).optional(),
            "stateFamilies": t.array(
                t.proxy(renames["StateFamilyConfigIn"])
            ).optional(),
            "outputs": t.array(t.proxy(renames["StreamLocationIn"])).optional(),
            "computationId": t.string().optional(),
            "inputs": t.array(t.proxy(renames["StreamLocationIn"])).optional(),
            "systemStageName": t.string().optional(),
        }
    ).named(renames["ComputationTopologyIn"])
    types["ComputationTopologyOut"] = t.struct(
        {
            "keyRanges": t.array(t.proxy(renames["KeyRangeLocationOut"])).optional(),
            "stateFamilies": t.array(
                t.proxy(renames["StateFamilyConfigOut"])
            ).optional(),
            "outputs": t.array(t.proxy(renames["StreamLocationOut"])).optional(),
            "computationId": t.string().optional(),
            "inputs": t.array(t.proxy(renames["StreamLocationOut"])).optional(),
            "systemStageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputationTopologyOut"])
    types["TemplateMetadataIn"] = t.struct(
        {
            "parameters": t.array(t.proxy(renames["ParameterMetadataIn"])).optional(),
            "name": t.string(),
            "description": t.string().optional(),
        }
    ).named(renames["TemplateMetadataIn"])
    types["TemplateMetadataOut"] = t.struct(
        {
            "parameters": t.array(t.proxy(renames["ParameterMetadataOut"])).optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TemplateMetadataOut"])
    types["LaunchFlexTemplateResponseIn"] = t.struct(
        {"job": t.proxy(renames["JobIn"]).optional()}
    ).named(renames["LaunchFlexTemplateResponseIn"])
    types["LaunchFlexTemplateResponseOut"] = t.struct(
        {
            "job": t.proxy(renames["JobOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LaunchFlexTemplateResponseOut"])
    types["JobExecutionInfoIn"] = t.struct(
        {"stages": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["JobExecutionInfoIn"])
    types["JobExecutionInfoOut"] = t.struct(
        {
            "stages": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobExecutionInfoOut"])
    types["SendWorkerMessagesRequestIn"] = t.struct(
        {
            "location": t.string().optional(),
            "workerMessages": t.array(t.proxy(renames["WorkerMessageIn"])).optional(),
        }
    ).named(renames["SendWorkerMessagesRequestIn"])
    types["SendWorkerMessagesRequestOut"] = t.struct(
        {
            "location": t.string().optional(),
            "workerMessages": t.array(t.proxy(renames["WorkerMessageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SendWorkerMessagesRequestOut"])
    types["DiskIn"] = t.struct(
        {
            "mountPoint": t.string().optional(),
            "sizeGb": t.integer().optional(),
            "diskType": t.string().optional(),
        }
    ).named(renames["DiskIn"])
    types["DiskOut"] = t.struct(
        {
            "mountPoint": t.string().optional(),
            "sizeGb": t.integer().optional(),
            "diskType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskOut"])
    types["MapTaskIn"] = t.struct(
        {
            "systemName": t.string().optional(),
            "instructions": t.array(
                t.proxy(renames["ParallelInstructionIn"])
            ).optional(),
            "stageName": t.string().optional(),
            "counterPrefix": t.string().optional(),
        }
    ).named(renames["MapTaskIn"])
    types["MapTaskOut"] = t.struct(
        {
            "systemName": t.string().optional(),
            "instructions": t.array(
                t.proxy(renames["ParallelInstructionOut"])
            ).optional(),
            "stageName": t.string().optional(),
            "counterPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MapTaskOut"])
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
    types["ApproximateReportedProgressIn"] = t.struct(
        {
            "consumedParallelism": t.proxy(renames["ReportedParallelismIn"]).optional(),
            "position": t.proxy(renames["PositionIn"]).optional(),
            "fractionConsumed": t.number().optional(),
            "remainingParallelism": t.proxy(
                renames["ReportedParallelismIn"]
            ).optional(),
        }
    ).named(renames["ApproximateReportedProgressIn"])
    types["ApproximateReportedProgressOut"] = t.struct(
        {
            "consumedParallelism": t.proxy(
                renames["ReportedParallelismOut"]
            ).optional(),
            "position": t.proxy(renames["PositionOut"]).optional(),
            "fractionConsumed": t.number().optional(),
            "remainingParallelism": t.proxy(
                renames["ReportedParallelismOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApproximateReportedProgressOut"])
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
    types["RuntimeEnvironmentIn"] = t.struct(
        {
            "numWorkers": t.integer().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "subnetwork": t.string().optional(),
            "tempLocation": t.string(),
            "additionalExperiments": t.array(t.string()).optional(),
            "workerZone": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "workerRegion": t.string(),
            "network": t.string().optional(),
            "machineType": t.string().optional(),
            "ipConfiguration": t.string().optional(),
            "bypassTempDirValidation": t.boolean().optional(),
            "enableStreamingEngine": t.boolean().optional(),
            "maxWorkers": t.integer().optional(),
            "kmsKeyName": t.string().optional(),
            "zone": t.string().optional(),
        }
    ).named(renames["RuntimeEnvironmentIn"])
    types["RuntimeEnvironmentOut"] = t.struct(
        {
            "numWorkers": t.integer().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "subnetwork": t.string().optional(),
            "tempLocation": t.string(),
            "additionalExperiments": t.array(t.string()).optional(),
            "workerZone": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "workerRegion": t.string(),
            "network": t.string().optional(),
            "machineType": t.string().optional(),
            "ipConfiguration": t.string().optional(),
            "bypassTempDirValidation": t.boolean().optional(),
            "enableStreamingEngine": t.boolean().optional(),
            "maxWorkers": t.integer().optional(),
            "kmsKeyName": t.string().optional(),
            "zone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeEnvironmentOut"])
    types["JobExecutionStageInfoIn"] = t.struct(
        {"stepName": t.array(t.string()).optional()}
    ).named(renames["JobExecutionStageInfoIn"])
    types["JobExecutionStageInfoOut"] = t.struct(
        {
            "stepName": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobExecutionStageInfoOut"])
    types["SendDebugCaptureResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SendDebugCaptureResponseIn"]
    )
    types["SendDebugCaptureResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SendDebugCaptureResponseOut"])
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
    types["ReportWorkItemStatusRequestIn"] = t.struct(
        {
            "currentWorkerTime": t.string().optional(),
            "workerId": t.string().optional(),
            "unifiedWorkerRequest": t.struct({"_": t.string().optional()}).optional(),
            "workItemStatuses": t.array(
                t.proxy(renames["WorkItemStatusIn"])
            ).optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ReportWorkItemStatusRequestIn"])
    types["ReportWorkItemStatusRequestOut"] = t.struct(
        {
            "currentWorkerTime": t.string().optional(),
            "workerId": t.string().optional(),
            "unifiedWorkerRequest": t.struct({"_": t.string().optional()}).optional(),
            "workItemStatuses": t.array(
                t.proxy(renames["WorkItemStatusOut"])
            ).optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportWorkItemStatusRequestOut"])
    types["LeaseWorkItemResponseIn"] = t.struct(
        {
            "unifiedWorkerResponse": t.struct({"_": t.string().optional()}).optional(),
            "workItems": t.array(t.proxy(renames["WorkItemIn"])).optional(),
        }
    ).named(renames["LeaseWorkItemResponseIn"])
    types["LeaseWorkItemResponseOut"] = t.struct(
        {
            "unifiedWorkerResponse": t.struct({"_": t.string().optional()}).optional(),
            "workItems": t.array(t.proxy(renames["WorkItemOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LeaseWorkItemResponseOut"])
    types["StreamingComputationConfigIn"] = t.struct(
        {
            "transformUserNameToStateFamily": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "systemName": t.string().optional(),
            "stageName": t.string().optional(),
            "instructions": t.array(
                t.proxy(renames["ParallelInstructionIn"])
            ).optional(),
            "computationId": t.string().optional(),
        }
    ).named(renames["StreamingComputationConfigIn"])
    types["StreamingComputationConfigOut"] = t.struct(
        {
            "transformUserNameToStateFamily": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "systemName": t.string().optional(),
            "stageName": t.string().optional(),
            "instructions": t.array(
                t.proxy(renames["ParallelInstructionOut"])
            ).optional(),
            "computationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingComputationConfigOut"])
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
    types["FlattenInstructionIn"] = t.struct(
        {"inputs": t.array(t.proxy(renames["InstructionInputIn"])).optional()}
    ).named(renames["FlattenInstructionIn"])
    types["FlattenInstructionOut"] = t.struct(
        {
            "inputs": t.array(t.proxy(renames["InstructionInputOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FlattenInstructionOut"])
    types["PartialGroupByKeyInstructionIn"] = t.struct(
        {
            "input": t.proxy(renames["InstructionInputIn"]).optional(),
            "valueCombiningFn": t.struct({"_": t.string().optional()}).optional(),
            "sideInputs": t.array(t.proxy(renames["SideInputInfoIn"])).optional(),
            "inputElementCodec": t.struct({"_": t.string().optional()}).optional(),
            "originalCombineValuesInputStoreName": t.string().optional(),
            "originalCombineValuesStepName": t.string().optional(),
        }
    ).named(renames["PartialGroupByKeyInstructionIn"])
    types["PartialGroupByKeyInstructionOut"] = t.struct(
        {
            "input": t.proxy(renames["InstructionInputOut"]).optional(),
            "valueCombiningFn": t.struct({"_": t.string().optional()}).optional(),
            "sideInputs": t.array(t.proxy(renames["SideInputInfoOut"])).optional(),
            "inputElementCodec": t.struct({"_": t.string().optional()}).optional(),
            "originalCombineValuesInputStoreName": t.string().optional(),
            "originalCombineValuesStepName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartialGroupByKeyInstructionOut"])
    types["SnapshotJobRequestIn"] = t.struct(
        {
            "description": t.string().optional(),
            "snapshotSources": t.boolean().optional(),
            "ttl": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["SnapshotJobRequestIn"])
    types["SnapshotJobRequestOut"] = t.struct(
        {
            "description": t.string().optional(),
            "snapshotSources": t.boolean().optional(),
            "ttl": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnapshotJobRequestOut"])
    types["StreamingStragglerInfoIn"] = t.struct(
        {
            "dataWatermarkLag": t.string().optional(),
            "systemWatermarkLag": t.string().optional(),
            "workerName": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["StreamingStragglerInfoIn"])
    types["StreamingStragglerInfoOut"] = t.struct(
        {
            "dataWatermarkLag": t.string().optional(),
            "systemWatermarkLag": t.string().optional(),
            "workerName": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingStragglerInfoOut"])
    types["WorkItemIn"] = t.struct(
        {
            "configuration": t.string().optional(),
            "shellTask": t.proxy(renames["ShellTaskIn"]).optional(),
            "jobId": t.string().optional(),
            "projectId": t.string().optional(),
            "seqMapTask": t.proxy(renames["SeqMapTaskIn"]).optional(),
            "packages": t.array(t.proxy(renames["PackageIn"])).optional(),
            "sourceOperationTask": t.proxy(
                renames["SourceOperationRequestIn"]
            ).optional(),
            "streamingComputationTask": t.proxy(
                renames["StreamingComputationTaskIn"]
            ).optional(),
            "reportStatusInterval": t.string().optional(),
            "id": t.string().optional(),
            "streamingConfigTask": t.proxy(renames["StreamingConfigTaskIn"]).optional(),
            "leaseExpireTime": t.string().optional(),
            "mapTask": t.proxy(renames["MapTaskIn"]).optional(),
            "initialReportIndex": t.string().optional(),
            "streamingSetupTask": t.proxy(renames["StreamingSetupTaskIn"]).optional(),
        }
    ).named(renames["WorkItemIn"])
    types["WorkItemOut"] = t.struct(
        {
            "configuration": t.string().optional(),
            "shellTask": t.proxy(renames["ShellTaskOut"]).optional(),
            "jobId": t.string().optional(),
            "projectId": t.string().optional(),
            "seqMapTask": t.proxy(renames["SeqMapTaskOut"]).optional(),
            "packages": t.array(t.proxy(renames["PackageOut"])).optional(),
            "sourceOperationTask": t.proxy(
                renames["SourceOperationRequestOut"]
            ).optional(),
            "streamingComputationTask": t.proxy(
                renames["StreamingComputationTaskOut"]
            ).optional(),
            "reportStatusInterval": t.string().optional(),
            "id": t.string().optional(),
            "streamingConfigTask": t.proxy(
                renames["StreamingConfigTaskOut"]
            ).optional(),
            "leaseExpireTime": t.string().optional(),
            "mapTask": t.proxy(renames["MapTaskOut"]).optional(),
            "initialReportIndex": t.string().optional(),
            "streamingSetupTask": t.proxy(renames["StreamingSetupTaskOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkItemOut"])
    types["StepIn"] = t.struct(
        {
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["StepIn"])
    types["StepOut"] = t.struct(
        {
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StepOut"])
    types["SeqMapTaskIn"] = t.struct(
        {
            "userFn": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "outputInfos": t.array(
                t.proxy(renames["SeqMapTaskOutputInfoIn"])
            ).optional(),
            "systemName": t.string().optional(),
            "stageName": t.string().optional(),
            "inputs": t.array(t.proxy(renames["SideInputInfoIn"])).optional(),
        }
    ).named(renames["SeqMapTaskIn"])
    types["SeqMapTaskOut"] = t.struct(
        {
            "userFn": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "outputInfos": t.array(
                t.proxy(renames["SeqMapTaskOutputInfoOut"])
            ).optional(),
            "systemName": t.string().optional(),
            "stageName": t.string().optional(),
            "inputs": t.array(t.proxy(renames["SideInputInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SeqMapTaskOut"])
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
    types["FlexTemplateRuntimeEnvironmentIn"] = t.struct(
        {
            "diskSizeGb": t.integer().optional(),
            "launcherMachineType": t.string().optional(),
            "stagingLocation": t.string().optional(),
            "dumpHeapOnOom": t.boolean().optional(),
            "serviceAccountEmail": t.string().optional(),
            "sdkContainerImage": t.string().optional(),
            "maxWorkers": t.integer().optional(),
            "autoscalingAlgorithm": t.string().optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "tempLocation": t.string().optional(),
            "workerZone": t.string().optional(),
            "numWorkers": t.integer().optional(),
            "ipConfiguration": t.string().optional(),
            "workerRegion": t.string().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "subnetwork": t.string().optional(),
            "enableLauncherVmSerialPortLogging": t.boolean().optional(),
            "kmsKeyName": t.string().optional(),
            "enableStreamingEngine": t.boolean().optional(),
            "zone": t.string().optional(),
            "saveHeapDumpsToGcsPath": t.string().optional(),
            "network": t.string().optional(),
            "flexrsGoal": t.string().optional(),
            "machineType": t.string().optional(),
        }
    ).named(renames["FlexTemplateRuntimeEnvironmentIn"])
    types["FlexTemplateRuntimeEnvironmentOut"] = t.struct(
        {
            "diskSizeGb": t.integer().optional(),
            "launcherMachineType": t.string().optional(),
            "stagingLocation": t.string().optional(),
            "dumpHeapOnOom": t.boolean().optional(),
            "serviceAccountEmail": t.string().optional(),
            "sdkContainerImage": t.string().optional(),
            "maxWorkers": t.integer().optional(),
            "autoscalingAlgorithm": t.string().optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "tempLocation": t.string().optional(),
            "workerZone": t.string().optional(),
            "numWorkers": t.integer().optional(),
            "ipConfiguration": t.string().optional(),
            "workerRegion": t.string().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "subnetwork": t.string().optional(),
            "enableLauncherVmSerialPortLogging": t.boolean().optional(),
            "kmsKeyName": t.string().optional(),
            "enableStreamingEngine": t.boolean().optional(),
            "zone": t.string().optional(),
            "saveHeapDumpsToGcsPath": t.string().optional(),
            "network": t.string().optional(),
            "flexrsGoal": t.string().optional(),
            "machineType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FlexTemplateRuntimeEnvironmentOut"])
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
    types["StageSummaryIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "stragglerSummary": t.proxy(renames["StragglerSummaryIn"]).optional(),
            "stageId": t.string().optional(),
            "startTime": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricUpdateIn"])).optional(),
            "progress": t.proxy(renames["ProgressTimeseriesIn"]).optional(),
        }
    ).named(renames["StageSummaryIn"])
    types["StageSummaryOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "stragglerSummary": t.proxy(renames["StragglerSummaryOut"]).optional(),
            "stageId": t.string().optional(),
            "startTime": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricUpdateOut"])).optional(),
            "progress": t.proxy(renames["ProgressTimeseriesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StageSummaryOut"])
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
    types["WorkerThreadScalingReportResponseIn"] = t.struct(
        {"recommendedThreadCount": t.integer().optional()}
    ).named(renames["WorkerThreadScalingReportResponseIn"])
    types["WorkerThreadScalingReportResponseOut"] = t.struct(
        {
            "recommendedThreadCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerThreadScalingReportResponseOut"])
    types["SourceSplitOptionsIn"] = t.struct(
        {
            "desiredShardSizeBytes": t.string().optional(),
            "desiredBundleSizeBytes": t.string().optional(),
        }
    ).named(renames["SourceSplitOptionsIn"])
    types["SourceSplitOptionsOut"] = t.struct(
        {
            "desiredShardSizeBytes": t.string().optional(),
            "desiredBundleSizeBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceSplitOptionsOut"])
    types["HotKeyDebuggingInfoIn"] = t.struct(
        {"detectedHotKeys": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["HotKeyDebuggingInfoIn"])
    types["HotKeyDebuggingInfoOut"] = t.struct(
        {
            "detectedHotKeys": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HotKeyDebuggingInfoOut"])
    types["PubsubLocationIn"] = t.struct(
        {
            "subscription": t.string().optional(),
            "withAttributes": t.boolean().optional(),
            "dropLateData": t.boolean().optional(),
            "trackingSubscription": t.string().optional(),
            "timestampLabel": t.string().optional(),
            "topic": t.string().optional(),
            "idLabel": t.string().optional(),
        }
    ).named(renames["PubsubLocationIn"])
    types["PubsubLocationOut"] = t.struct(
        {
            "subscription": t.string().optional(),
            "withAttributes": t.boolean().optional(),
            "dropLateData": t.boolean().optional(),
            "trackingSubscription": t.string().optional(),
            "timestampLabel": t.string().optional(),
            "topic": t.string().optional(),
            "idLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubLocationOut"])
    types["WorkItemServiceStateIn"] = t.struct(
        {
            "completeWorkStatus": t.proxy(renames["StatusIn"]).optional(),
            "leaseExpireTime": t.string().optional(),
            "metricShortId": t.array(t.proxy(renames["MetricShortIdIn"])).optional(),
            "reportStatusInterval": t.string().optional(),
            "suggestedStopPoint": t.proxy(renames["ApproximateProgressIn"]).optional(),
            "harnessData": t.struct({"_": t.string().optional()}).optional(),
            "hotKeyDetection": t.proxy(renames["HotKeyDetectionIn"]).optional(),
            "suggestedStopPosition": t.proxy(renames["PositionIn"]).optional(),
            "nextReportIndex": t.string().optional(),
            "splitRequest": t.proxy(renames["ApproximateSplitRequestIn"]).optional(),
        }
    ).named(renames["WorkItemServiceStateIn"])
    types["WorkItemServiceStateOut"] = t.struct(
        {
            "completeWorkStatus": t.proxy(renames["StatusOut"]).optional(),
            "leaseExpireTime": t.string().optional(),
            "metricShortId": t.array(t.proxy(renames["MetricShortIdOut"])).optional(),
            "reportStatusInterval": t.string().optional(),
            "suggestedStopPoint": t.proxy(renames["ApproximateProgressOut"]).optional(),
            "harnessData": t.struct({"_": t.string().optional()}).optional(),
            "hotKeyDetection": t.proxy(renames["HotKeyDetectionOut"]).optional(),
            "suggestedStopPosition": t.proxy(renames["PositionOut"]).optional(),
            "nextReportIndex": t.string().optional(),
            "splitRequest": t.proxy(renames["ApproximateSplitRequestOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkItemServiceStateOut"])
    types["SourceOperationRequestIn"] = t.struct(
        {
            "stageName": t.string().optional(),
            "systemName": t.string().optional(),
            "split": t.proxy(renames["SourceSplitRequestIn"]).optional(),
            "getMetadata": t.proxy(renames["SourceGetMetadataRequestIn"]).optional(),
            "originalName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SourceOperationRequestIn"])
    types["SourceOperationRequestOut"] = t.struct(
        {
            "stageName": t.string().optional(),
            "systemName": t.string().optional(),
            "split": t.proxy(renames["SourceSplitRequestOut"]).optional(),
            "getMetadata": t.proxy(renames["SourceGetMetadataRequestOut"]).optional(),
            "originalName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOperationRequestOut"])
    types["WorkerHealthReportResponseIn"] = t.struct(
        {"reportInterval": t.string().optional()}
    ).named(renames["WorkerHealthReportResponseIn"])
    types["WorkerHealthReportResponseOut"] = t.struct(
        {
            "reportInterval": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerHealthReportResponseOut"])
    types["SourceForkIn"] = t.struct(
        {
            "residualSource": t.proxy(renames["DerivedSourceIn"]).optional(),
            "residual": t.proxy(renames["SourceSplitShardIn"]).optional(),
            "primarySource": t.proxy(renames["DerivedSourceIn"]).optional(),
            "primary": t.proxy(renames["SourceSplitShardIn"]).optional(),
        }
    ).named(renames["SourceForkIn"])
    types["SourceForkOut"] = t.struct(
        {
            "residualSource": t.proxy(renames["DerivedSourceOut"]).optional(),
            "residual": t.proxy(renames["SourceSplitShardOut"]).optional(),
            "primarySource": t.proxy(renames["DerivedSourceOut"]).optional(),
            "primary": t.proxy(renames["SourceSplitShardOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceForkOut"])
    types["KeyRangeLocationIn"] = t.struct(
        {
            "deliveryEndpoint": t.string().optional(),
            "deprecatedPersistentDirectory": t.string().optional(),
            "dataDisk": t.string().optional(),
            "start": t.string().optional(),
            "end": t.string().optional(),
        }
    ).named(renames["KeyRangeLocationIn"])
    types["KeyRangeLocationOut"] = t.struct(
        {
            "deliveryEndpoint": t.string().optional(),
            "deprecatedPersistentDirectory": t.string().optional(),
            "dataDisk": t.string().optional(),
            "start": t.string().optional(),
            "end": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyRangeLocationOut"])
    types["ListJobMessagesResponseIn"] = t.struct(
        {
            "autoscalingEvents": t.array(
                t.proxy(renames["AutoscalingEventIn"])
            ).optional(),
            "jobMessages": t.array(t.proxy(renames["JobMessageIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListJobMessagesResponseIn"])
    types["ListJobMessagesResponseOut"] = t.struct(
        {
            "autoscalingEvents": t.array(
                t.proxy(renames["AutoscalingEventOut"])
            ).optional(),
            "jobMessages": t.array(t.proxy(renames["JobMessageOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobMessagesResponseOut"])
    types["CounterStructuredNameIn"] = t.struct(
        {
            "componentStepName": t.string().optional(),
            "executionStepName": t.string().optional(),
            "name": t.string().optional(),
            "workerId": t.string().optional(),
            "portion": t.string().optional(),
            "inputIndex": t.integer().optional(),
            "origin": t.string().optional(),
            "originalStepName": t.string().optional(),
            "originNamespace": t.string().optional(),
            "originalRequestingStepName": t.string().optional(),
        }
    ).named(renames["CounterStructuredNameIn"])
    types["CounterStructuredNameOut"] = t.struct(
        {
            "componentStepName": t.string().optional(),
            "executionStepName": t.string().optional(),
            "name": t.string().optional(),
            "workerId": t.string().optional(),
            "portion": t.string().optional(),
            "inputIndex": t.integer().optional(),
            "origin": t.string().optional(),
            "originalStepName": t.string().optional(),
            "originNamespace": t.string().optional(),
            "originalRequestingStepName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CounterStructuredNameOut"])
    types["ListSnapshotsResponseIn"] = t.struct(
        {"snapshots": t.array(t.proxy(renames["SnapshotIn"])).optional()}
    ).named(renames["ListSnapshotsResponseIn"])
    types["ListSnapshotsResponseOut"] = t.struct(
        {
            "snapshots": t.array(t.proxy(renames["SnapshotOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSnapshotsResponseOut"])
    types["InstructionOutputIn"] = t.struct(
        {
            "onlyCountKeyBytes": t.boolean().optional(),
            "onlyCountValueBytes": t.boolean().optional(),
            "systemName": t.string().optional(),
            "name": t.string().optional(),
            "originalName": t.string().optional(),
            "codec": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["InstructionOutputIn"])
    types["InstructionOutputOut"] = t.struct(
        {
            "onlyCountKeyBytes": t.boolean().optional(),
            "onlyCountValueBytes": t.boolean().optional(),
            "systemName": t.string().optional(),
            "name": t.string().optional(),
            "originalName": t.string().optional(),
            "codec": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstructionOutputOut"])
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
    types["LaunchTemplateParametersIn"] = t.struct(
        {
            "update": t.boolean().optional(),
            "transformNameMapping": t.struct({"_": t.string().optional()}).optional(),
            "jobName": t.string(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
        }
    ).named(renames["LaunchTemplateParametersIn"])
    types["LaunchTemplateParametersOut"] = t.struct(
        {
            "update": t.boolean().optional(),
            "transformNameMapping": t.struct({"_": t.string().optional()}).optional(),
            "jobName": t.string(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "environment": t.proxy(renames["RuntimeEnvironmentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LaunchTemplateParametersOut"])
    types["CounterUpdateIn"] = t.struct(
        {
            "floatingPointList": t.proxy(renames["FloatingPointListIn"]).optional(),
            "floatingPointMean": t.proxy(renames["FloatingPointMeanIn"]).optional(),
            "stringList": t.proxy(renames["StringListIn"]).optional(),
            "shortId": t.string().optional(),
            "integerMean": t.proxy(renames["IntegerMeanIn"]).optional(),
            "boolean": t.boolean().optional(),
            "integerGauge": t.proxy(renames["IntegerGaugeIn"]).optional(),
            "integerList": t.proxy(renames["IntegerListIn"]).optional(),
            "distribution": t.proxy(renames["DistributionUpdateIn"]).optional(),
            "internal": t.struct({"_": t.string().optional()}).optional(),
            "nameAndKind": t.proxy(renames["NameAndKindIn"]).optional(),
            "structuredNameAndMetadata": t.proxy(
                renames["CounterStructuredNameAndMetadataIn"]
            ).optional(),
            "integer": t.proxy(renames["SplitInt64In"]).optional(),
            "floatingPoint": t.number().optional(),
            "cumulative": t.boolean().optional(),
        }
    ).named(renames["CounterUpdateIn"])
    types["CounterUpdateOut"] = t.struct(
        {
            "floatingPointList": t.proxy(renames["FloatingPointListOut"]).optional(),
            "floatingPointMean": t.proxy(renames["FloatingPointMeanOut"]).optional(),
            "stringList": t.proxy(renames["StringListOut"]).optional(),
            "shortId": t.string().optional(),
            "integerMean": t.proxy(renames["IntegerMeanOut"]).optional(),
            "boolean": t.boolean().optional(),
            "integerGauge": t.proxy(renames["IntegerGaugeOut"]).optional(),
            "integerList": t.proxy(renames["IntegerListOut"]).optional(),
            "distribution": t.proxy(renames["DistributionUpdateOut"]).optional(),
            "internal": t.struct({"_": t.string().optional()}).optional(),
            "nameAndKind": t.proxy(renames["NameAndKindOut"]).optional(),
            "structuredNameAndMetadata": t.proxy(
                renames["CounterStructuredNameAndMetadataOut"]
            ).optional(),
            "integer": t.proxy(renames["SplitInt64Out"]).optional(),
            "floatingPoint": t.number().optional(),
            "cumulative": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CounterUpdateOut"])
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
    types["WorkerMessageIn"] = t.struct(
        {
            "workerThreadScalingReport": t.proxy(
                renames["WorkerThreadScalingReportIn"]
            ).optional(),
            "workerLifecycleEvent": t.proxy(
                renames["WorkerLifecycleEventIn"]
            ).optional(),
            "workerMessageCode": t.proxy(renames["WorkerMessageCodeIn"]).optional(),
            "workerHealthReport": t.proxy(renames["WorkerHealthReportIn"]).optional(),
            "time": t.string().optional(),
            "workerMetrics": t.proxy(renames["ResourceUtilizationReportIn"]).optional(),
            "workerShutdownNotice": t.proxy(
                renames["WorkerShutdownNoticeIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["WorkerMessageIn"])
    types["WorkerMessageOut"] = t.struct(
        {
            "workerThreadScalingReport": t.proxy(
                renames["WorkerThreadScalingReportOut"]
            ).optional(),
            "workerLifecycleEvent": t.proxy(
                renames["WorkerLifecycleEventOut"]
            ).optional(),
            "workerMessageCode": t.proxy(renames["WorkerMessageCodeOut"]).optional(),
            "workerHealthReport": t.proxy(renames["WorkerHealthReportOut"]).optional(),
            "time": t.string().optional(),
            "workerMetrics": t.proxy(
                renames["ResourceUtilizationReportOut"]
            ).optional(),
            "workerShutdownNotice": t.proxy(
                renames["WorkerShutdownNoticeOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerMessageOut"])
    types["MountedDataDiskIn"] = t.struct({"dataDisk": t.string().optional()}).named(
        renames["MountedDataDiskIn"]
    )
    types["MountedDataDiskOut"] = t.struct(
        {
            "dataDisk": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MountedDataDiskOut"])
    types["StreamingStageLocationIn"] = t.struct(
        {"streamId": t.string().optional()}
    ).named(renames["StreamingStageLocationIn"])
    types["StreamingStageLocationOut"] = t.struct(
        {
            "streamId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingStageLocationOut"])
    types["DistributionUpdateIn"] = t.struct(
        {
            "min": t.proxy(renames["SplitInt64In"]).optional(),
            "sumOfSquares": t.number().optional(),
            "histogram": t.proxy(renames["HistogramIn"]).optional(),
            "max": t.proxy(renames["SplitInt64In"]).optional(),
            "count": t.proxy(renames["SplitInt64In"]).optional(),
            "sum": t.proxy(renames["SplitInt64In"]).optional(),
        }
    ).named(renames["DistributionUpdateIn"])
    types["DistributionUpdateOut"] = t.struct(
        {
            "min": t.proxy(renames["SplitInt64Out"]).optional(),
            "sumOfSquares": t.number().optional(),
            "histogram": t.proxy(renames["HistogramOut"]).optional(),
            "max": t.proxy(renames["SplitInt64Out"]).optional(),
            "count": t.proxy(renames["SplitInt64Out"]).optional(),
            "sum": t.proxy(renames["SplitInt64Out"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DistributionUpdateOut"])
    types["MemInfoIn"] = t.struct(
        {
            "currentOoms": t.string().optional(),
            "totalGbMs": t.string().optional(),
            "currentRssBytes": t.string().optional(),
            "timestamp": t.string().optional(),
            "currentLimitBytes": t.string().optional(),
        }
    ).named(renames["MemInfoIn"])
    types["MemInfoOut"] = t.struct(
        {
            "currentOoms": t.string().optional(),
            "totalGbMs": t.string().optional(),
            "currentRssBytes": t.string().optional(),
            "timestamp": t.string().optional(),
            "currentLimitBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemInfoOut"])
    types["TransformSummaryIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "outputCollectionName": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "inputCollectionName": t.array(t.string()).optional(),
            "displayData": t.array(t.proxy(renames["DisplayDataIn"])).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["TransformSummaryIn"])
    types["TransformSummaryOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "outputCollectionName": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "inputCollectionName": t.array(t.string()).optional(),
            "displayData": t.array(t.proxy(renames["DisplayDataOut"])).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransformSummaryOut"])
    types["ApproximateProgressIn"] = t.struct(
        {
            "percentComplete": t.number().optional(),
            "remainingTime": t.string().optional(),
            "position": t.proxy(renames["PositionIn"]).optional(),
        }
    ).named(renames["ApproximateProgressIn"])
    types["ApproximateProgressOut"] = t.struct(
        {
            "percentComplete": t.number().optional(),
            "remainingTime": t.string().optional(),
            "position": t.proxy(renames["PositionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApproximateProgressOut"])
    types["SendDebugCaptureRequestIn"] = t.struct(
        {
            "componentId": t.string().optional(),
            "workerId": t.string().optional(),
            "data": t.string().optional(),
            "location": t.string().optional(),
            "dataFormat": t.string().optional(),
        }
    ).named(renames["SendDebugCaptureRequestIn"])
    types["SendDebugCaptureRequestOut"] = t.struct(
        {
            "componentId": t.string().optional(),
            "workerId": t.string().optional(),
            "data": t.string().optional(),
            "location": t.string().optional(),
            "dataFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SendDebugCaptureRequestOut"])
    types["StreamingComputationTaskIn"] = t.struct(
        {
            "computationRanges": t.array(
                t.proxy(renames["StreamingComputationRangesIn"])
            ).optional(),
            "taskType": t.string().optional(),
            "dataDisks": t.array(t.proxy(renames["MountedDataDiskIn"])).optional(),
        }
    ).named(renames["StreamingComputationTaskIn"])
    types["StreamingComputationTaskOut"] = t.struct(
        {
            "computationRanges": t.array(
                t.proxy(renames["StreamingComputationRangesOut"])
            ).optional(),
            "taskType": t.string().optional(),
            "dataDisks": t.array(t.proxy(renames["MountedDataDiskOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingComputationTaskOut"])
    types["WorkerShutdownNoticeIn"] = t.struct({"reason": t.string().optional()}).named(
        renames["WorkerShutdownNoticeIn"]
    )
    types["WorkerShutdownNoticeOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerShutdownNoticeOut"])
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
    types["MetricStructuredNameIn"] = t.struct(
        {
            "context": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "origin": t.string().optional(),
        }
    ).named(renames["MetricStructuredNameIn"])
    types["MetricStructuredNameOut"] = t.struct(
        {
            "context": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "origin": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricStructuredNameOut"])
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
    types["TaskRunnerSettingsIn"] = t.struct(
        {
            "commandlinesFileName": t.string().optional(),
            "streamingWorkerMainClass": t.string().optional(),
            "languageHint": t.string().optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "baseUrl": t.string().optional(),
            "logToSerialconsole": t.boolean().optional(),
            "alsologtostderr": t.boolean().optional(),
            "dataflowApiVersion": t.string().optional(),
            "vmId": t.string().optional(),
            "logDir": t.string().optional(),
            "tempStoragePrefix": t.string().optional(),
            "workflowFileName": t.string().optional(),
            "logUploadLocation": t.string().optional(),
            "taskUser": t.string().optional(),
            "parallelWorkerSettings": t.proxy(renames["WorkerSettingsIn"]).optional(),
            "taskGroup": t.string().optional(),
            "baseTaskDir": t.string().optional(),
            "harnessCommand": t.string().optional(),
            "continueOnException": t.boolean().optional(),
        }
    ).named(renames["TaskRunnerSettingsIn"])
    types["TaskRunnerSettingsOut"] = t.struct(
        {
            "commandlinesFileName": t.string().optional(),
            "streamingWorkerMainClass": t.string().optional(),
            "languageHint": t.string().optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "baseUrl": t.string().optional(),
            "logToSerialconsole": t.boolean().optional(),
            "alsologtostderr": t.boolean().optional(),
            "dataflowApiVersion": t.string().optional(),
            "vmId": t.string().optional(),
            "logDir": t.string().optional(),
            "tempStoragePrefix": t.string().optional(),
            "workflowFileName": t.string().optional(),
            "logUploadLocation": t.string().optional(),
            "taskUser": t.string().optional(),
            "parallelWorkerSettings": t.proxy(renames["WorkerSettingsOut"]).optional(),
            "taskGroup": t.string().optional(),
            "baseTaskDir": t.string().optional(),
            "harnessCommand": t.string().optional(),
            "continueOnException": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskRunnerSettingsOut"])
    types["StragglerDebuggingInfoIn"] = t.struct(
        {"hotKey": t.proxy(renames["HotKeyDebuggingInfoIn"]).optional()}
    ).named(renames["StragglerDebuggingInfoIn"])
    types["StragglerDebuggingInfoOut"] = t.struct(
        {
            "hotKey": t.proxy(renames["HotKeyDebuggingInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StragglerDebuggingInfoOut"])
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
    types["WorkerShutdownNoticeResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["WorkerShutdownNoticeResponseIn"])
    types["WorkerShutdownNoticeResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WorkerShutdownNoticeResponseOut"])
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
    types["AutoscalingEventIn"] = t.struct(
        {
            "time": t.string().optional(),
            "currentNumWorkers": t.string().optional(),
            "targetNumWorkers": t.string().optional(),
            "description": t.proxy(renames["StructuredMessageIn"]).optional(),
            "workerPool": t.string().optional(),
            "eventType": t.string().optional(),
        }
    ).named(renames["AutoscalingEventIn"])
    types["AutoscalingEventOut"] = t.struct(
        {
            "time": t.string().optional(),
            "currentNumWorkers": t.string().optional(),
            "targetNumWorkers": t.string().optional(),
            "description": t.proxy(renames["StructuredMessageOut"]).optional(),
            "workerPool": t.string().optional(),
            "eventType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoscalingEventOut"])
    types["WorkItemDetailsIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricUpdateIn"])).optional(),
            "state": t.string().optional(),
            "taskId": t.string().optional(),
            "endTime": t.string().optional(),
            "stragglerInfo": t.proxy(renames["StragglerInfoIn"]).optional(),
            "attemptId": t.string().optional(),
            "progress": t.proxy(renames["ProgressTimeseriesIn"]).optional(),
        }
    ).named(renames["WorkItemDetailsIn"])
    types["WorkItemDetailsOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricUpdateOut"])).optional(),
            "state": t.string().optional(),
            "taskId": t.string().optional(),
            "endTime": t.string().optional(),
            "stragglerInfo": t.proxy(renames["StragglerInfoOut"]).optional(),
            "attemptId": t.string().optional(),
            "progress": t.proxy(renames["ProgressTimeseriesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkItemDetailsOut"])
    types["HotKeyDetectionIn"] = t.struct(
        {
            "hotKeyAge": t.string().optional(),
            "systemName": t.string().optional(),
            "userStepName": t.string().optional(),
        }
    ).named(renames["HotKeyDetectionIn"])
    types["HotKeyDetectionOut"] = t.struct(
        {
            "hotKeyAge": t.string().optional(),
            "systemName": t.string().optional(),
            "userStepName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HotKeyDetectionOut"])
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
    types["WorkerHealthReportIn"] = t.struct(
        {
            "msg": t.string().optional(),
            "reportInterval": t.string().optional(),
            "vmStartupTime": t.string().optional(),
            "vmIsHealthy": t.boolean().optional(),
            "vmBrokenCode": t.string().optional(),
            "pods": t.array(t.struct({"_": t.string().optional()})).optional(),
            "vmIsBroken": t.boolean().optional(),
        }
    ).named(renames["WorkerHealthReportIn"])
    types["WorkerHealthReportOut"] = t.struct(
        {
            "msg": t.string().optional(),
            "reportInterval": t.string().optional(),
            "vmStartupTime": t.string().optional(),
            "vmIsHealthy": t.boolean().optional(),
            "vmBrokenCode": t.string().optional(),
            "pods": t.array(t.struct({"_": t.string().optional()})).optional(),
            "vmIsBroken": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerHealthReportOut"])
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
    functions["projectsLocationsFlexTemplatesLaunch"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/flexTemplates:launch",
        t.struct(
            {
                "location": t.string(),
                "projectId": t.string(),
                "validateOnly": t.boolean().optional(),
                "launchParameter": t.proxy(renames["LaunchFlexTemplateParameterIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LaunchFlexTemplateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSnapshotsList"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/snapshots/{snapshotId}",
        t.struct(
            {
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "snapshotId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSnapshotsDelete"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/snapshots/{snapshotId}",
        t.struct(
            {
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "snapshotId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSnapshotsGet"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/snapshots/{snapshotId}",
        t.struct(
            {
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "snapshotId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsGetExecutionDetails"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}",
        t.struct(
            {
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "view": t.string().optional(),
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
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "view": t.string().optional(),
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
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsUpdate"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}",
        t.struct(
            {
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "view": t.string().optional(),
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
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "view": t.string().optional(),
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
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "view": t.string().optional(),
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
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "view": t.string().optional(),
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
                "location": t.string().optional(),
                "startTime": t.string().optional(),
                "pageToken": t.string().optional(),
                "jobId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "endTime": t.string().optional(),
                "projectId": t.string().optional(),
                "stageId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StageExecutionDetailsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsSnapshotsList"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/snapshots",
        t.struct(
            {
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "location": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSnapshotsResponseOut"]),
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
                "workerCapabilities": t.array(t.string()).optional(),
                "workerId": t.string().optional(),
                "unifiedWorkerRequest": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "workItemTypes": t.array(t.string()).optional(),
                "currentWorkerTime": t.string().optional(),
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
                "workerCapabilities": t.array(t.string()).optional(),
                "workerId": t.string().optional(),
                "unifiedWorkerRequest": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "workItemTypes": t.array(t.string()).optional(),
                "currentWorkerTime": t.string().optional(),
                "requestedLeaseDuration": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaseWorkItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsMessagesList"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/messages",
        t.struct(
            {
                "jobId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "projectId": t.string().optional(),
                "pageToken": t.string().optional(),
                "endTime": t.string().optional(),
                "startTime": t.string().optional(),
                "location": t.string().optional(),
                "minimumImportance": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobMessagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsDebugSendCapture"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/debug/getConfig",
        t.struct(
            {
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
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
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "componentId": t.string().optional(),
                "workerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetDebugConfigResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTemplatesGet"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/templates",
        t.struct(
            {
                "location": t.string().optional(),
                "projectId": t.string(),
                "gcsPath": t.string(),
                "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
                "jobName": t.string(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
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
                "location": t.string().optional(),
                "projectId": t.string(),
                "gcsPath": t.string(),
                "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
                "jobName": t.string(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
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
                "location": t.string().optional(),
                "projectId": t.string(),
                "gcsPath": t.string(),
                "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
                "jobName": t.string(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
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
                "gcsPath": t.string().optional(),
                "dynamicTemplate.stagingLocation": t.string().optional(),
                "dynamicTemplate.gcsPath": t.string().optional(),
                "projectId": t.string(),
                "location": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "update": t.boolean().optional(),
                "transformNameMapping": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "jobName": t.string(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
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
                "gcsPath": t.string().optional(),
                "dynamicTemplate.stagingLocation": t.string().optional(),
                "dynamicTemplate.gcsPath": t.string().optional(),
                "projectId": t.string(),
                "location": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "update": t.boolean().optional(),
                "transformNameMapping": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "jobName": t.string(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
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
                "gcsPath": t.string().optional(),
                "dynamicTemplate.stagingLocation": t.string().optional(),
                "dynamicTemplate.gcsPath": t.string().optional(),
                "projectId": t.string(),
                "location": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "update": t.boolean().optional(),
                "transformNameMapping": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "jobName": t.string(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LaunchTemplateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsUpdate"] = dataflow.get(
        "v1b3/projects/{projectId}/jobs/{jobId}",
        t.struct(
            {
                "projectId": t.string().optional(),
                "view": t.string().optional(),
                "location": t.string().optional(),
                "jobId": t.string().optional(),
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
                "projectId": t.string().optional(),
                "view": t.string().optional(),
                "location": t.string().optional(),
                "jobId": t.string().optional(),
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
                "projectId": t.string().optional(),
                "view": t.string().optional(),
                "location": t.string().optional(),
                "jobId": t.string().optional(),
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
                "projectId": t.string().optional(),
                "view": t.string().optional(),
                "location": t.string().optional(),
                "jobId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsSnapshot"] = dataflow.get(
        "v1b3/projects/{projectId}/jobs/{jobId}",
        t.struct(
            {
                "projectId": t.string().optional(),
                "view": t.string().optional(),
                "location": t.string().optional(),
                "jobId": t.string().optional(),
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
                "projectId": t.string().optional(),
                "view": t.string().optional(),
                "location": t.string().optional(),
                "jobId": t.string().optional(),
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
                "projectId": t.string().optional(),
                "view": t.string().optional(),
                "location": t.string().optional(),
                "jobId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsWorkItemsReportStatus"] = dataflow.post(
        "v1b3/projects/{projectId}/jobs/{jobId}/workItems:lease",
        t.struct(
            {
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "workerCapabilities": t.array(t.string()).optional(),
                "location": t.string().optional(),
                "workerId": t.string().optional(),
                "unifiedWorkerRequest": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "workItemTypes": t.array(t.string()).optional(),
                "currentWorkerTime": t.string().optional(),
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
                "workerCapabilities": t.array(t.string()).optional(),
                "location": t.string().optional(),
                "workerId": t.string().optional(),
                "unifiedWorkerRequest": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "workItemTypes": t.array(t.string()).optional(),
                "currentWorkerTime": t.string().optional(),
                "requestedLeaseDuration": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LeaseWorkItemResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsMessagesList"] = dataflow.get(
        "v1b3/projects/{projectId}/jobs/{jobId}/messages",
        t.struct(
            {
                "location": t.string().optional(),
                "jobId": t.string().optional(),
                "projectId": t.string().optional(),
                "pageToken": t.string().optional(),
                "startTime": t.string().optional(),
                "endTime": t.string().optional(),
                "minimumImportance": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "componentId": t.string().optional(),
                "workerId": t.string().optional(),
                "data": t.string().optional(),
                "location": t.string().optional(),
                "dataFormat": t.string().optional(),
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
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "componentId": t.string().optional(),
                "workerId": t.string().optional(),
                "data": t.string().optional(),
                "location": t.string().optional(),
                "dataFormat": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SendDebugCaptureResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="dataflow", renames=renames, types=Box(types), functions=Box(functions)
    )
