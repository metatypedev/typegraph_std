from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_dataflow():
    dataflow = HTTPRuntime("https://dataflow.googleapis.com/")

    renames = {
        "ErrorResponse": "_dataflow_1_ErrorResponse",
        "LaunchTemplateParametersIn": "_dataflow_2_LaunchTemplateParametersIn",
        "LaunchTemplateParametersOut": "_dataflow_3_LaunchTemplateParametersOut",
        "IntegerListIn": "_dataflow_4_IntegerListIn",
        "IntegerListOut": "_dataflow_5_IntegerListOut",
        "GetDebugConfigRequestIn": "_dataflow_6_GetDebugConfigRequestIn",
        "GetDebugConfigRequestOut": "_dataflow_7_GetDebugConfigRequestOut",
        "StageSourceIn": "_dataflow_8_StageSourceIn",
        "StageSourceOut": "_dataflow_9_StageSourceOut",
        "SendDebugCaptureResponseIn": "_dataflow_10_SendDebugCaptureResponseIn",
        "SendDebugCaptureResponseOut": "_dataflow_11_SendDebugCaptureResponseOut",
        "IntegerMeanIn": "_dataflow_12_IntegerMeanIn",
        "IntegerMeanOut": "_dataflow_13_IntegerMeanOut",
        "SnapshotIn": "_dataflow_14_SnapshotIn",
        "SnapshotOut": "_dataflow_15_SnapshotOut",
        "WorkerMessageCodeIn": "_dataflow_16_WorkerMessageCodeIn",
        "WorkerMessageCodeOut": "_dataflow_17_WorkerMessageCodeOut",
        "DisplayDataIn": "_dataflow_18_DisplayDataIn",
        "DisplayDataOut": "_dataflow_19_DisplayDataOut",
        "InstructionOutputIn": "_dataflow_20_InstructionOutputIn",
        "InstructionOutputOut": "_dataflow_21_InstructionOutputOut",
        "StringListIn": "_dataflow_22_StringListIn",
        "StringListOut": "_dataflow_23_StringListOut",
        "JobExecutionInfoIn": "_dataflow_24_JobExecutionInfoIn",
        "JobExecutionInfoOut": "_dataflow_25_JobExecutionInfoOut",
        "SDKInfoIn": "_dataflow_26_SDKInfoIn",
        "SDKInfoOut": "_dataflow_27_SDKInfoOut",
        "StreamingComputationConfigIn": "_dataflow_28_StreamingComputationConfigIn",
        "StreamingComputationConfigOut": "_dataflow_29_StreamingComputationConfigOut",
        "FileIODetailsIn": "_dataflow_30_FileIODetailsIn",
        "FileIODetailsOut": "_dataflow_31_FileIODetailsOut",
        "MountedDataDiskIn": "_dataflow_32_MountedDataDiskIn",
        "MountedDataDiskOut": "_dataflow_33_MountedDataDiskOut",
        "CreateJobFromTemplateRequestIn": "_dataflow_34_CreateJobFromTemplateRequestIn",
        "CreateJobFromTemplateRequestOut": "_dataflow_35_CreateJobFromTemplateRequestOut",
        "CounterMetadataIn": "_dataflow_36_CounterMetadataIn",
        "CounterMetadataOut": "_dataflow_37_CounterMetadataOut",
        "ExecutionStageSummaryIn": "_dataflow_38_ExecutionStageSummaryIn",
        "ExecutionStageSummaryOut": "_dataflow_39_ExecutionStageSummaryOut",
        "SeqMapTaskOutputInfoIn": "_dataflow_40_SeqMapTaskOutputInfoIn",
        "SeqMapTaskOutputInfoOut": "_dataflow_41_SeqMapTaskOutputInfoOut",
        "ApproximateReportedProgressIn": "_dataflow_42_ApproximateReportedProgressIn",
        "ApproximateReportedProgressOut": "_dataflow_43_ApproximateReportedProgressOut",
        "LeaseWorkItemResponseIn": "_dataflow_44_LeaseWorkItemResponseIn",
        "LeaseWorkItemResponseOut": "_dataflow_45_LeaseWorkItemResponseOut",
        "SourceMetadataIn": "_dataflow_46_SourceMetadataIn",
        "SourceMetadataOut": "_dataflow_47_SourceMetadataOut",
        "WorkItemStatusIn": "_dataflow_48_WorkItemStatusIn",
        "WorkItemStatusOut": "_dataflow_49_WorkItemStatusOut",
        "SplitInt64In": "_dataflow_50_SplitInt64In",
        "SplitInt64Out": "_dataflow_51_SplitInt64Out",
        "StepIn": "_dataflow_52_StepIn",
        "StepOut": "_dataflow_53_StepOut",
        "KeyRangeLocationIn": "_dataflow_54_KeyRangeLocationIn",
        "KeyRangeLocationOut": "_dataflow_55_KeyRangeLocationOut",
        "ReportedParallelismIn": "_dataflow_56_ReportedParallelismIn",
        "ReportedParallelismOut": "_dataflow_57_ReportedParallelismOut",
        "MetricShortIdIn": "_dataflow_58_MetricShortIdIn",
        "MetricShortIdOut": "_dataflow_59_MetricShortIdOut",
        "ComponentTransformIn": "_dataflow_60_ComponentTransformIn",
        "ComponentTransformOut": "_dataflow_61_ComponentTransformOut",
        "AutoscalingSettingsIn": "_dataflow_62_AutoscalingSettingsIn",
        "AutoscalingSettingsOut": "_dataflow_63_AutoscalingSettingsOut",
        "StatusIn": "_dataflow_64_StatusIn",
        "StatusOut": "_dataflow_65_StatusOut",
        "PipelineDescriptionIn": "_dataflow_66_PipelineDescriptionIn",
        "PipelineDescriptionOut": "_dataflow_67_PipelineDescriptionOut",
        "StageSummaryIn": "_dataflow_68_StageSummaryIn",
        "StageSummaryOut": "_dataflow_69_StageSummaryOut",
        "HotKeyDebuggingInfoIn": "_dataflow_70_HotKeyDebuggingInfoIn",
        "HotKeyDebuggingInfoOut": "_dataflow_71_HotKeyDebuggingInfoOut",
        "WorkerMessageResponseIn": "_dataflow_72_WorkerMessageResponseIn",
        "WorkerMessageResponseOut": "_dataflow_73_WorkerMessageResponseOut",
        "HotKeyInfoIn": "_dataflow_74_HotKeyInfoIn",
        "HotKeyInfoOut": "_dataflow_75_HotKeyInfoOut",
        "DebugOptionsIn": "_dataflow_76_DebugOptionsIn",
        "DebugOptionsOut": "_dataflow_77_DebugOptionsOut",
        "StreamingSideInputLocationIn": "_dataflow_78_StreamingSideInputLocationIn",
        "StreamingSideInputLocationOut": "_dataflow_79_StreamingSideInputLocationOut",
        "MetricStructuredNameIn": "_dataflow_80_MetricStructuredNameIn",
        "MetricStructuredNameOut": "_dataflow_81_MetricStructuredNameOut",
        "SourceSplitOptionsIn": "_dataflow_82_SourceSplitOptionsIn",
        "SourceSplitOptionsOut": "_dataflow_83_SourceSplitOptionsOut",
        "TaskRunnerSettingsIn": "_dataflow_84_TaskRunnerSettingsIn",
        "TaskRunnerSettingsOut": "_dataflow_85_TaskRunnerSettingsOut",
        "RuntimeUpdatableParamsIn": "_dataflow_86_RuntimeUpdatableParamsIn",
        "RuntimeUpdatableParamsOut": "_dataflow_87_RuntimeUpdatableParamsOut",
        "JobMetricsIn": "_dataflow_88_JobMetricsIn",
        "JobMetricsOut": "_dataflow_89_JobMetricsOut",
        "DistributionUpdateIn": "_dataflow_90_DistributionUpdateIn",
        "DistributionUpdateOut": "_dataflow_91_DistributionUpdateOut",
        "SdkVersionIn": "_dataflow_92_SdkVersionIn",
        "SdkVersionOut": "_dataflow_93_SdkVersionOut",
        "WorkerDetailsIn": "_dataflow_94_WorkerDetailsIn",
        "WorkerDetailsOut": "_dataflow_95_WorkerDetailsOut",
        "ParameterIn": "_dataflow_96_ParameterIn",
        "ParameterOut": "_dataflow_97_ParameterOut",
        "DataDiskAssignmentIn": "_dataflow_98_DataDiskAssignmentIn",
        "DataDiskAssignmentOut": "_dataflow_99_DataDiskAssignmentOut",
        "JobExecutionDetailsIn": "_dataflow_100_JobExecutionDetailsIn",
        "JobExecutionDetailsOut": "_dataflow_101_JobExecutionDetailsOut",
        "ComponentSourceIn": "_dataflow_102_ComponentSourceIn",
        "ComponentSourceOut": "_dataflow_103_ComponentSourceOut",
        "WorkerLifecycleEventIn": "_dataflow_104_WorkerLifecycleEventIn",
        "WorkerLifecycleEventOut": "_dataflow_105_WorkerLifecycleEventOut",
        "SourceSplitShardIn": "_dataflow_106_SourceSplitShardIn",
        "SourceSplitShardOut": "_dataflow_107_SourceSplitShardOut",
        "SourceGetMetadataRequestIn": "_dataflow_108_SourceGetMetadataRequestIn",
        "SourceGetMetadataRequestOut": "_dataflow_109_SourceGetMetadataRequestOut",
        "SourceSplitResponseIn": "_dataflow_110_SourceSplitResponseIn",
        "SourceSplitResponseOut": "_dataflow_111_SourceSplitResponseOut",
        "DatastoreIODetailsIn": "_dataflow_112_DatastoreIODetailsIn",
        "DatastoreIODetailsOut": "_dataflow_113_DatastoreIODetailsOut",
        "CounterStructuredNameAndMetadataIn": "_dataflow_114_CounterStructuredNameAndMetadataIn",
        "CounterStructuredNameAndMetadataOut": "_dataflow_115_CounterStructuredNameAndMetadataOut",
        "ComputationTopologyIn": "_dataflow_116_ComputationTopologyIn",
        "ComputationTopologyOut": "_dataflow_117_ComputationTopologyOut",
        "PubsubSnapshotMetadataIn": "_dataflow_118_PubsubSnapshotMetadataIn",
        "PubsubSnapshotMetadataOut": "_dataflow_119_PubsubSnapshotMetadataOut",
        "CounterUpdateIn": "_dataflow_120_CounterUpdateIn",
        "CounterUpdateOut": "_dataflow_121_CounterUpdateOut",
        "TransformSummaryIn": "_dataflow_122_TransformSummaryIn",
        "TransformSummaryOut": "_dataflow_123_TransformSummaryOut",
        "SendDebugCaptureRequestIn": "_dataflow_124_SendDebugCaptureRequestIn",
        "SendDebugCaptureRequestOut": "_dataflow_125_SendDebugCaptureRequestOut",
        "CPUTimeIn": "_dataflow_126_CPUTimeIn",
        "CPUTimeOut": "_dataflow_127_CPUTimeOut",
        "HistogramIn": "_dataflow_128_HistogramIn",
        "HistogramOut": "_dataflow_129_HistogramOut",
        "StreamingStragglerInfoIn": "_dataflow_130_StreamingStragglerInfoIn",
        "StreamingStragglerInfoOut": "_dataflow_131_StreamingStragglerInfoOut",
        "LeaseWorkItemRequestIn": "_dataflow_132_LeaseWorkItemRequestIn",
        "LeaseWorkItemRequestOut": "_dataflow_133_LeaseWorkItemRequestOut",
        "TopologyConfigIn": "_dataflow_134_TopologyConfigIn",
        "TopologyConfigOut": "_dataflow_135_TopologyConfigOut",
        "TemplateMetadataIn": "_dataflow_136_TemplateMetadataIn",
        "TemplateMetadataOut": "_dataflow_137_TemplateMetadataOut",
        "InstructionInputIn": "_dataflow_138_InstructionInputIn",
        "InstructionInputOut": "_dataflow_139_InstructionInputOut",
        "ApproximateSplitRequestIn": "_dataflow_140_ApproximateSplitRequestIn",
        "ApproximateSplitRequestOut": "_dataflow_141_ApproximateSplitRequestOut",
        "CustomSourceLocationIn": "_dataflow_142_CustomSourceLocationIn",
        "CustomSourceLocationOut": "_dataflow_143_CustomSourceLocationOut",
        "SourceOperationResponseIn": "_dataflow_144_SourceOperationResponseIn",
        "SourceOperationResponseOut": "_dataflow_145_SourceOperationResponseOut",
        "StreamingStageLocationIn": "_dataflow_146_StreamingStageLocationIn",
        "StreamingStageLocationOut": "_dataflow_147_StreamingStageLocationOut",
        "FloatingPointListIn": "_dataflow_148_FloatingPointListIn",
        "FloatingPointListOut": "_dataflow_149_FloatingPointListOut",
        "StragglerInfoIn": "_dataflow_150_StragglerInfoIn",
        "StragglerInfoOut": "_dataflow_151_StragglerInfoOut",
        "FlattenInstructionIn": "_dataflow_152_FlattenInstructionIn",
        "FlattenInstructionOut": "_dataflow_153_FlattenInstructionOut",
        "ListJobMessagesResponseIn": "_dataflow_154_ListJobMessagesResponseIn",
        "ListJobMessagesResponseOut": "_dataflow_155_ListJobMessagesResponseOut",
        "LaunchTemplateResponseIn": "_dataflow_156_LaunchTemplateResponseIn",
        "LaunchTemplateResponseOut": "_dataflow_157_LaunchTemplateResponseOut",
        "LaunchFlexTemplateParameterIn": "_dataflow_158_LaunchFlexTemplateParameterIn",
        "LaunchFlexTemplateParameterOut": "_dataflow_159_LaunchFlexTemplateParameterOut",
        "NameAndKindIn": "_dataflow_160_NameAndKindIn",
        "NameAndKindOut": "_dataflow_161_NameAndKindOut",
        "BigTableIODetailsIn": "_dataflow_162_BigTableIODetailsIn",
        "BigTableIODetailsOut": "_dataflow_163_BigTableIODetailsOut",
        "FloatingPointMeanIn": "_dataflow_164_FloatingPointMeanIn",
        "FloatingPointMeanOut": "_dataflow_165_FloatingPointMeanOut",
        "ConcatPositionIn": "_dataflow_166_ConcatPositionIn",
        "ConcatPositionOut": "_dataflow_167_ConcatPositionOut",
        "SourceIn": "_dataflow_168_SourceIn",
        "SourceOut": "_dataflow_169_SourceOut",
        "StreamLocationIn": "_dataflow_170_StreamLocationIn",
        "StreamLocationOut": "_dataflow_171_StreamLocationOut",
        "BigQueryIODetailsIn": "_dataflow_172_BigQueryIODetailsIn",
        "BigQueryIODetailsOut": "_dataflow_173_BigQueryIODetailsOut",
        "MultiOutputInfoIn": "_dataflow_174_MultiOutputInfoIn",
        "MultiOutputInfoOut": "_dataflow_175_MultiOutputInfoOut",
        "SourceOperationRequestIn": "_dataflow_176_SourceOperationRequestIn",
        "SourceOperationRequestOut": "_dataflow_177_SourceOperationRequestOut",
        "IntegerGaugeIn": "_dataflow_178_IntegerGaugeIn",
        "IntegerGaugeOut": "_dataflow_179_IntegerGaugeOut",
        "ParameterMetadataEnumOptionIn": "_dataflow_180_ParameterMetadataEnumOptionIn",
        "ParameterMetadataEnumOptionOut": "_dataflow_181_ParameterMetadataEnumOptionOut",
        "PointIn": "_dataflow_182_PointIn",
        "PointOut": "_dataflow_183_PointOut",
        "PositionIn": "_dataflow_184_PositionIn",
        "PositionOut": "_dataflow_185_PositionOut",
        "SideInputInfoIn": "_dataflow_186_SideInputInfoIn",
        "SideInputInfoOut": "_dataflow_187_SideInputInfoOut",
        "StragglerDebuggingInfoIn": "_dataflow_188_StragglerDebuggingInfoIn",
        "StragglerDebuggingInfoOut": "_dataflow_189_StragglerDebuggingInfoOut",
        "ContainerSpecIn": "_dataflow_190_ContainerSpecIn",
        "ContainerSpecOut": "_dataflow_191_ContainerSpecOut",
        "MapTaskIn": "_dataflow_192_MapTaskIn",
        "MapTaskOut": "_dataflow_193_MapTaskOut",
        "RuntimeEnvironmentIn": "_dataflow_194_RuntimeEnvironmentIn",
        "RuntimeEnvironmentOut": "_dataflow_195_RuntimeEnvironmentOut",
        "SendWorkerMessagesResponseIn": "_dataflow_196_SendWorkerMessagesResponseIn",
        "SendWorkerMessagesResponseOut": "_dataflow_197_SendWorkerMessagesResponseOut",
        "JobExecutionStageInfoIn": "_dataflow_198_JobExecutionStageInfoIn",
        "JobExecutionStageInfoOut": "_dataflow_199_JobExecutionStageInfoOut",
        "SnapshotJobRequestIn": "_dataflow_200_SnapshotJobRequestIn",
        "SnapshotJobRequestOut": "_dataflow_201_SnapshotJobRequestOut",
        "PubsubLocationIn": "_dataflow_202_PubsubLocationIn",
        "PubsubLocationOut": "_dataflow_203_PubsubLocationOut",
        "FlexTemplateRuntimeEnvironmentIn": "_dataflow_204_FlexTemplateRuntimeEnvironmentIn",
        "FlexTemplateRuntimeEnvironmentOut": "_dataflow_205_FlexTemplateRuntimeEnvironmentOut",
        "WorkerHealthReportIn": "_dataflow_206_WorkerHealthReportIn",
        "WorkerHealthReportOut": "_dataflow_207_WorkerHealthReportOut",
        "PubSubIODetailsIn": "_dataflow_208_PubSubIODetailsIn",
        "PubSubIODetailsOut": "_dataflow_209_PubSubIODetailsOut",
        "StreamingComputationRangesIn": "_dataflow_210_StreamingComputationRangesIn",
        "StreamingComputationRangesOut": "_dataflow_211_StreamingComputationRangesOut",
        "WorkItemDetailsIn": "_dataflow_212_WorkItemDetailsIn",
        "WorkItemDetailsOut": "_dataflow_213_WorkItemDetailsOut",
        "SourceGetMetadataResponseIn": "_dataflow_214_SourceGetMetadataResponseIn",
        "SourceGetMetadataResponseOut": "_dataflow_215_SourceGetMetadataResponseOut",
        "StreamingApplianceSnapshotConfigIn": "_dataflow_216_StreamingApplianceSnapshotConfigIn",
        "StreamingApplianceSnapshotConfigOut": "_dataflow_217_StreamingApplianceSnapshotConfigOut",
        "ShellTaskIn": "_dataflow_218_ShellTaskIn",
        "ShellTaskOut": "_dataflow_219_ShellTaskOut",
        "RuntimeMetadataIn": "_dataflow_220_RuntimeMetadataIn",
        "RuntimeMetadataOut": "_dataflow_221_RuntimeMetadataOut",
        "KeyRangeDataDiskAssignmentIn": "_dataflow_222_KeyRangeDataDiskAssignmentIn",
        "KeyRangeDataDiskAssignmentOut": "_dataflow_223_KeyRangeDataDiskAssignmentOut",
        "ReportWorkItemStatusRequestIn": "_dataflow_224_ReportWorkItemStatusRequestIn",
        "ReportWorkItemStatusRequestOut": "_dataflow_225_ReportWorkItemStatusRequestOut",
        "EnvironmentIn": "_dataflow_226_EnvironmentIn",
        "EnvironmentOut": "_dataflow_227_EnvironmentOut",
        "GetDebugConfigResponseIn": "_dataflow_228_GetDebugConfigResponseIn",
        "GetDebugConfigResponseOut": "_dataflow_229_GetDebugConfigResponseOut",
        "LaunchFlexTemplateResponseIn": "_dataflow_230_LaunchFlexTemplateResponseIn",
        "LaunchFlexTemplateResponseOut": "_dataflow_231_LaunchFlexTemplateResponseOut",
        "SendWorkerMessagesRequestIn": "_dataflow_232_SendWorkerMessagesRequestIn",
        "SendWorkerMessagesRequestOut": "_dataflow_233_SendWorkerMessagesRequestOut",
        "ResourceUtilizationReportResponseIn": "_dataflow_234_ResourceUtilizationReportResponseIn",
        "ResourceUtilizationReportResponseOut": "_dataflow_235_ResourceUtilizationReportResponseOut",
        "WorkerPoolIn": "_dataflow_236_WorkerPoolIn",
        "WorkerPoolOut": "_dataflow_237_WorkerPoolOut",
        "ParallelInstructionIn": "_dataflow_238_ParallelInstructionIn",
        "ParallelInstructionOut": "_dataflow_239_ParallelInstructionOut",
        "FailedLocationIn": "_dataflow_240_FailedLocationIn",
        "FailedLocationOut": "_dataflow_241_FailedLocationOut",
        "WorkerThreadScalingReportIn": "_dataflow_242_WorkerThreadScalingReportIn",
        "WorkerThreadScalingReportOut": "_dataflow_243_WorkerThreadScalingReportOut",
        "ResourceUtilizationReportIn": "_dataflow_244_ResourceUtilizationReportIn",
        "ResourceUtilizationReportOut": "_dataflow_245_ResourceUtilizationReportOut",
        "StageExecutionDetailsIn": "_dataflow_246_StageExecutionDetailsIn",
        "StageExecutionDetailsOut": "_dataflow_247_StageExecutionDetailsOut",
        "ApproximateProgressIn": "_dataflow_248_ApproximateProgressIn",
        "ApproximateProgressOut": "_dataflow_249_ApproximateProgressOut",
        "SdkHarnessContainerImageIn": "_dataflow_250_SdkHarnessContainerImageIn",
        "SdkHarnessContainerImageOut": "_dataflow_251_SdkHarnessContainerImageOut",
        "WorkItemIn": "_dataflow_252_WorkItemIn",
        "WorkItemOut": "_dataflow_253_WorkItemOut",
        "StreamingSetupTaskIn": "_dataflow_254_StreamingSetupTaskIn",
        "StreamingSetupTaskOut": "_dataflow_255_StreamingSetupTaskOut",
        "ListSnapshotsResponseIn": "_dataflow_256_ListSnapshotsResponseIn",
        "ListSnapshotsResponseOut": "_dataflow_257_ListSnapshotsResponseOut",
        "SpannerIODetailsIn": "_dataflow_258_SpannerIODetailsIn",
        "SpannerIODetailsOut": "_dataflow_259_SpannerIODetailsOut",
        "StructuredMessageIn": "_dataflow_260_StructuredMessageIn",
        "StructuredMessageOut": "_dataflow_261_StructuredMessageOut",
        "StragglerIn": "_dataflow_262_StragglerIn",
        "StragglerOut": "_dataflow_263_StragglerOut",
        "StateFamilyConfigIn": "_dataflow_264_StateFamilyConfigIn",
        "StateFamilyConfigOut": "_dataflow_265_StateFamilyConfigOut",
        "SourceForkIn": "_dataflow_266_SourceForkIn",
        "SourceForkOut": "_dataflow_267_SourceForkOut",
        "SinkIn": "_dataflow_268_SinkIn",
        "SinkOut": "_dataflow_269_SinkOut",
        "DerivedSourceIn": "_dataflow_270_DerivedSourceIn",
        "DerivedSourceOut": "_dataflow_271_DerivedSourceOut",
        "MemInfoIn": "_dataflow_272_MemInfoIn",
        "MemInfoOut": "_dataflow_273_MemInfoOut",
        "AutoscalingEventIn": "_dataflow_274_AutoscalingEventIn",
        "AutoscalingEventOut": "_dataflow_275_AutoscalingEventOut",
        "CounterStructuredNameIn": "_dataflow_276_CounterStructuredNameIn",
        "CounterStructuredNameOut": "_dataflow_277_CounterStructuredNameOut",
        "StreamingComputationTaskIn": "_dataflow_278_StreamingComputationTaskIn",
        "StreamingComputationTaskOut": "_dataflow_279_StreamingComputationTaskOut",
        "DeleteSnapshotResponseIn": "_dataflow_280_DeleteSnapshotResponseIn",
        "DeleteSnapshotResponseOut": "_dataflow_281_DeleteSnapshotResponseOut",
        "ParDoInstructionIn": "_dataflow_282_ParDoInstructionIn",
        "ParDoInstructionOut": "_dataflow_283_ParDoInstructionOut",
        "WorkerShutdownNoticeResponseIn": "_dataflow_284_WorkerShutdownNoticeResponseIn",
        "WorkerShutdownNoticeResponseOut": "_dataflow_285_WorkerShutdownNoticeResponseOut",
        "MetricUpdateIn": "_dataflow_286_MetricUpdateIn",
        "MetricUpdateOut": "_dataflow_287_MetricUpdateOut",
        "WriteInstructionIn": "_dataflow_288_WriteInstructionIn",
        "WriteInstructionOut": "_dataflow_289_WriteInstructionOut",
        "ExecutionStageStateIn": "_dataflow_290_ExecutionStageStateIn",
        "ExecutionStageStateOut": "_dataflow_291_ExecutionStageStateOut",
        "WorkerHealthReportResponseIn": "_dataflow_292_WorkerHealthReportResponseIn",
        "WorkerHealthReportResponseOut": "_dataflow_293_WorkerHealthReportResponseOut",
        "ParameterMetadataIn": "_dataflow_294_ParameterMetadataIn",
        "ParameterMetadataOut": "_dataflow_295_ParameterMetadataOut",
        "ReportWorkItemStatusResponseIn": "_dataflow_296_ReportWorkItemStatusResponseIn",
        "ReportWorkItemStatusResponseOut": "_dataflow_297_ReportWorkItemStatusResponseOut",
        "PartialGroupByKeyInstructionIn": "_dataflow_298_PartialGroupByKeyInstructionIn",
        "PartialGroupByKeyInstructionOut": "_dataflow_299_PartialGroupByKeyInstructionOut",
        "DynamicSourceSplitIn": "_dataflow_300_DynamicSourceSplitIn",
        "DynamicSourceSplitOut": "_dataflow_301_DynamicSourceSplitOut",
        "GetTemplateResponseIn": "_dataflow_302_GetTemplateResponseIn",
        "GetTemplateResponseOut": "_dataflow_303_GetTemplateResponseOut",
        "StreamingConfigTaskIn": "_dataflow_304_StreamingConfigTaskIn",
        "StreamingConfigTaskOut": "_dataflow_305_StreamingConfigTaskOut",
        "WorkerMessageIn": "_dataflow_306_WorkerMessageIn",
        "WorkerMessageOut": "_dataflow_307_WorkerMessageOut",
        "JobMessageIn": "_dataflow_308_JobMessageIn",
        "JobMessageOut": "_dataflow_309_JobMessageOut",
        "SourceSplitRequestIn": "_dataflow_310_SourceSplitRequestIn",
        "SourceSplitRequestOut": "_dataflow_311_SourceSplitRequestOut",
        "WorkItemServiceStateIn": "_dataflow_312_WorkItemServiceStateIn",
        "WorkItemServiceStateOut": "_dataflow_313_WorkItemServiceStateOut",
        "ProgressTimeseriesIn": "_dataflow_314_ProgressTimeseriesIn",
        "ProgressTimeseriesOut": "_dataflow_315_ProgressTimeseriesOut",
        "WorkerSettingsIn": "_dataflow_316_WorkerSettingsIn",
        "WorkerSettingsOut": "_dataflow_317_WorkerSettingsOut",
        "WorkerShutdownNoticeIn": "_dataflow_318_WorkerShutdownNoticeIn",
        "WorkerShutdownNoticeOut": "_dataflow_319_WorkerShutdownNoticeOut",
        "SeqMapTaskIn": "_dataflow_320_SeqMapTaskIn",
        "SeqMapTaskOut": "_dataflow_321_SeqMapTaskOut",
        "JobIn": "_dataflow_322_JobIn",
        "JobOut": "_dataflow_323_JobOut",
        "HotKeyDetectionIn": "_dataflow_324_HotKeyDetectionIn",
        "HotKeyDetectionOut": "_dataflow_325_HotKeyDetectionOut",
        "LaunchFlexTemplateRequestIn": "_dataflow_326_LaunchFlexTemplateRequestIn",
        "LaunchFlexTemplateRequestOut": "_dataflow_327_LaunchFlexTemplateRequestOut",
        "ListJobsResponseIn": "_dataflow_328_ListJobsResponseIn",
        "ListJobsResponseOut": "_dataflow_329_ListJobsResponseOut",
        "StragglerSummaryIn": "_dataflow_330_StragglerSummaryIn",
        "StragglerSummaryOut": "_dataflow_331_StragglerSummaryOut",
        "JobMetadataIn": "_dataflow_332_JobMetadataIn",
        "JobMetadataOut": "_dataflow_333_JobMetadataOut",
        "ReadInstructionIn": "_dataflow_334_ReadInstructionIn",
        "ReadInstructionOut": "_dataflow_335_ReadInstructionOut",
        "DiskIn": "_dataflow_336_DiskIn",
        "DiskOut": "_dataflow_337_DiskOut",
        "PackageIn": "_dataflow_338_PackageIn",
        "PackageOut": "_dataflow_339_PackageOut",
        "WorkerThreadScalingReportResponseIn": "_dataflow_340_WorkerThreadScalingReportResponseIn",
        "WorkerThreadScalingReportResponseOut": "_dataflow_341_WorkerThreadScalingReportResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["LaunchTemplateParametersIn"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "jobName": t.string(),
            "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
            "transformNameMapping": t.struct({"_": t.string().optional()}).optional(),
            "update": t.boolean().optional(),
        }
    ).named(renames["LaunchTemplateParametersIn"])
    types["LaunchTemplateParametersOut"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "jobName": t.string(),
            "environment": t.proxy(renames["RuntimeEnvironmentOut"]).optional(),
            "transformNameMapping": t.struct({"_": t.string().optional()}).optional(),
            "update": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LaunchTemplateParametersOut"])
    types["IntegerListIn"] = t.struct(
        {"elements": t.array(t.proxy(renames["SplitInt64In"])).optional()}
    ).named(renames["IntegerListIn"])
    types["IntegerListOut"] = t.struct(
        {
            "elements": t.array(t.proxy(renames["SplitInt64Out"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntegerListOut"])
    types["GetDebugConfigRequestIn"] = t.struct(
        {
            "componentId": t.string().optional(),
            "location": t.string().optional(),
            "workerId": t.string().optional(),
        }
    ).named(renames["GetDebugConfigRequestIn"])
    types["GetDebugConfigRequestOut"] = t.struct(
        {
            "componentId": t.string().optional(),
            "location": t.string().optional(),
            "workerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetDebugConfigRequestOut"])
    types["StageSourceIn"] = t.struct(
        {
            "sizeBytes": t.string().optional(),
            "userName": t.string().optional(),
            "originalTransformOrCollection": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["StageSourceIn"])
    types["StageSourceOut"] = t.struct(
        {
            "sizeBytes": t.string().optional(),
            "userName": t.string().optional(),
            "originalTransformOrCollection": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StageSourceOut"])
    types["SendDebugCaptureResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SendDebugCaptureResponseIn"]
    )
    types["SendDebugCaptureResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SendDebugCaptureResponseOut"])
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
    types["SnapshotIn"] = t.struct(
        {
            "ttl": t.string().optional(),
            "creationTime": t.string().optional(),
            "projectId": t.string().optional(),
            "state": t.string().optional(),
            "pubsubMetadata": t.array(
                t.proxy(renames["PubsubSnapshotMetadataIn"])
            ).optional(),
            "description": t.string().optional(),
            "diskSizeBytes": t.string().optional(),
            "region": t.string().optional(),
            "id": t.string().optional(),
            "sourceJobId": t.string().optional(),
        }
    ).named(renames["SnapshotIn"])
    types["SnapshotOut"] = t.struct(
        {
            "ttl": t.string().optional(),
            "creationTime": t.string().optional(),
            "projectId": t.string().optional(),
            "state": t.string().optional(),
            "pubsubMetadata": t.array(
                t.proxy(renames["PubsubSnapshotMetadataOut"])
            ).optional(),
            "description": t.string().optional(),
            "diskSizeBytes": t.string().optional(),
            "region": t.string().optional(),
            "id": t.string().optional(),
            "sourceJobId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnapshotOut"])
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
            "boolValue": t.boolean().optional(),
            "namespace": t.string().optional(),
            "durationValue": t.string().optional(),
            "shortStrValue": t.string().optional(),
            "int64Value": t.string().optional(),
            "floatValue": t.number().optional(),
            "javaClassValue": t.string().optional(),
            "timestampValue": t.string().optional(),
            "strValue": t.string().optional(),
            "url": t.string().optional(),
            "key": t.string().optional(),
            "label": t.string().optional(),
        }
    ).named(renames["DisplayDataIn"])
    types["DisplayDataOut"] = t.struct(
        {
            "boolValue": t.boolean().optional(),
            "namespace": t.string().optional(),
            "durationValue": t.string().optional(),
            "shortStrValue": t.string().optional(),
            "int64Value": t.string().optional(),
            "floatValue": t.number().optional(),
            "javaClassValue": t.string().optional(),
            "timestampValue": t.string().optional(),
            "strValue": t.string().optional(),
            "url": t.string().optional(),
            "key": t.string().optional(),
            "label": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisplayDataOut"])
    types["InstructionOutputIn"] = t.struct(
        {
            "systemName": t.string().optional(),
            "onlyCountValueBytes": t.boolean().optional(),
            "originalName": t.string().optional(),
            "onlyCountKeyBytes": t.boolean().optional(),
            "name": t.string().optional(),
            "codec": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["InstructionOutputIn"])
    types["InstructionOutputOut"] = t.struct(
        {
            "systemName": t.string().optional(),
            "onlyCountValueBytes": t.boolean().optional(),
            "originalName": t.string().optional(),
            "onlyCountKeyBytes": t.boolean().optional(),
            "name": t.string().optional(),
            "codec": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstructionOutputOut"])
    types["StringListIn"] = t.struct(
        {"elements": t.array(t.string()).optional()}
    ).named(renames["StringListIn"])
    types["StringListOut"] = t.struct(
        {
            "elements": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StringListOut"])
    types["JobExecutionInfoIn"] = t.struct(
        {"stages": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["JobExecutionInfoIn"])
    types["JobExecutionInfoOut"] = t.struct(
        {
            "stages": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobExecutionInfoOut"])
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
    types["StreamingComputationConfigIn"] = t.struct(
        {
            "stageName": t.string().optional(),
            "computationId": t.string().optional(),
            "instructions": t.array(
                t.proxy(renames["ParallelInstructionIn"])
            ).optional(),
            "transformUserNameToStateFamily": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "systemName": t.string().optional(),
        }
    ).named(renames["StreamingComputationConfigIn"])
    types["StreamingComputationConfigOut"] = t.struct(
        {
            "stageName": t.string().optional(),
            "computationId": t.string().optional(),
            "instructions": t.array(
                t.proxy(renames["ParallelInstructionOut"])
            ).optional(),
            "transformUserNameToStateFamily": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "systemName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingComputationConfigOut"])
    types["FileIODetailsIn"] = t.struct({"filePattern": t.string().optional()}).named(
        renames["FileIODetailsIn"]
    )
    types["FileIODetailsOut"] = t.struct(
        {
            "filePattern": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileIODetailsOut"])
    types["MountedDataDiskIn"] = t.struct({"dataDisk": t.string().optional()}).named(
        renames["MountedDataDiskIn"]
    )
    types["MountedDataDiskOut"] = t.struct(
        {
            "dataDisk": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MountedDataDiskOut"])
    types["CreateJobFromTemplateRequestIn"] = t.struct(
        {
            "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
            "location": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "jobName": t.string(),
            "gcsPath": t.string(),
        }
    ).named(renames["CreateJobFromTemplateRequestIn"])
    types["CreateJobFromTemplateRequestOut"] = t.struct(
        {
            "environment": t.proxy(renames["RuntimeEnvironmentOut"]).optional(),
            "location": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "jobName": t.string(),
            "gcsPath": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateJobFromTemplateRequestOut"])
    types["CounterMetadataIn"] = t.struct(
        {
            "otherUnits": t.string().optional(),
            "kind": t.string().optional(),
            "description": t.string().optional(),
            "standardUnits": t.string().optional(),
        }
    ).named(renames["CounterMetadataIn"])
    types["CounterMetadataOut"] = t.struct(
        {
            "otherUnits": t.string().optional(),
            "kind": t.string().optional(),
            "description": t.string().optional(),
            "standardUnits": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CounterMetadataOut"])
    types["ExecutionStageSummaryIn"] = t.struct(
        {
            "componentSource": t.array(
                t.proxy(renames["ComponentSourceIn"])
            ).optional(),
            "name": t.string().optional(),
            "componentTransform": t.array(
                t.proxy(renames["ComponentTransformIn"])
            ).optional(),
            "outputSource": t.array(t.proxy(renames["StageSourceIn"])).optional(),
            "prerequisiteStage": t.array(t.string()).optional(),
            "inputSource": t.array(t.proxy(renames["StageSourceIn"])).optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ExecutionStageSummaryIn"])
    types["ExecutionStageSummaryOut"] = t.struct(
        {
            "componentSource": t.array(
                t.proxy(renames["ComponentSourceOut"])
            ).optional(),
            "name": t.string().optional(),
            "componentTransform": t.array(
                t.proxy(renames["ComponentTransformOut"])
            ).optional(),
            "outputSource": t.array(t.proxy(renames["StageSourceOut"])).optional(),
            "prerequisiteStage": t.array(t.string()).optional(),
            "inputSource": t.array(t.proxy(renames["StageSourceOut"])).optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionStageSummaryOut"])
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
    types["ApproximateReportedProgressIn"] = t.struct(
        {
            "consumedParallelism": t.proxy(renames["ReportedParallelismIn"]).optional(),
            "position": t.proxy(renames["PositionIn"]).optional(),
            "remainingParallelism": t.proxy(
                renames["ReportedParallelismIn"]
            ).optional(),
            "fractionConsumed": t.number().optional(),
        }
    ).named(renames["ApproximateReportedProgressIn"])
    types["ApproximateReportedProgressOut"] = t.struct(
        {
            "consumedParallelism": t.proxy(
                renames["ReportedParallelismOut"]
            ).optional(),
            "position": t.proxy(renames["PositionOut"]).optional(),
            "remainingParallelism": t.proxy(
                renames["ReportedParallelismOut"]
            ).optional(),
            "fractionConsumed": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApproximateReportedProgressOut"])
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
    types["SourceMetadataIn"] = t.struct(
        {
            "estimatedSizeBytes": t.string().optional(),
            "infinite": t.boolean().optional(),
            "producesSortedKeys": t.boolean().optional(),
        }
    ).named(renames["SourceMetadataIn"])
    types["SourceMetadataOut"] = t.struct(
        {
            "estimatedSizeBytes": t.string().optional(),
            "infinite": t.boolean().optional(),
            "producesSortedKeys": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceMetadataOut"])
    types["WorkItemStatusIn"] = t.struct(
        {
            "metricUpdates": t.array(t.proxy(renames["MetricUpdateIn"])).optional(),
            "sourceFork": t.proxy(renames["SourceForkIn"]).optional(),
            "reportIndex": t.string().optional(),
            "counterUpdates": t.array(t.proxy(renames["CounterUpdateIn"])).optional(),
            "progress": t.proxy(renames["ApproximateProgressIn"]).optional(),
            "totalThrottlerWaitTimeSeconds": t.number().optional(),
            "workItemId": t.string().optional(),
            "dynamicSourceSplit": t.proxy(renames["DynamicSourceSplitIn"]).optional(),
            "stopPosition": t.proxy(renames["PositionIn"]).optional(),
            "completed": t.boolean().optional(),
            "errors": t.array(t.proxy(renames["StatusIn"])).optional(),
            "requestedLeaseDuration": t.string().optional(),
            "sourceOperationResponse": t.proxy(
                renames["SourceOperationResponseIn"]
            ).optional(),
            "reportedProgress": t.proxy(
                renames["ApproximateReportedProgressIn"]
            ).optional(),
        }
    ).named(renames["WorkItemStatusIn"])
    types["WorkItemStatusOut"] = t.struct(
        {
            "metricUpdates": t.array(t.proxy(renames["MetricUpdateOut"])).optional(),
            "sourceFork": t.proxy(renames["SourceForkOut"]).optional(),
            "reportIndex": t.string().optional(),
            "counterUpdates": t.array(t.proxy(renames["CounterUpdateOut"])).optional(),
            "progress": t.proxy(renames["ApproximateProgressOut"]).optional(),
            "totalThrottlerWaitTimeSeconds": t.number().optional(),
            "workItemId": t.string().optional(),
            "dynamicSourceSplit": t.proxy(renames["DynamicSourceSplitOut"]).optional(),
            "stopPosition": t.proxy(renames["PositionOut"]).optional(),
            "completed": t.boolean().optional(),
            "errors": t.array(t.proxy(renames["StatusOut"])).optional(),
            "requestedLeaseDuration": t.string().optional(),
            "sourceOperationResponse": t.proxy(
                renames["SourceOperationResponseOut"]
            ).optional(),
            "reportedProgress": t.proxy(
                renames["ApproximateReportedProgressOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkItemStatusOut"])
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
    types["KeyRangeLocationIn"] = t.struct(
        {
            "start": t.string().optional(),
            "end": t.string().optional(),
            "deprecatedPersistentDirectory": t.string().optional(),
            "deliveryEndpoint": t.string().optional(),
            "dataDisk": t.string().optional(),
        }
    ).named(renames["KeyRangeLocationIn"])
    types["KeyRangeLocationOut"] = t.struct(
        {
            "start": t.string().optional(),
            "end": t.string().optional(),
            "deprecatedPersistentDirectory": t.string().optional(),
            "deliveryEndpoint": t.string().optional(),
            "dataDisk": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyRangeLocationOut"])
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
    types["PipelineDescriptionIn"] = t.struct(
        {
            "stepNamesHash": t.string().optional(),
            "executionPipelineStage": t.array(
                t.proxy(renames["ExecutionStageSummaryIn"])
            ).optional(),
            "displayData": t.array(t.proxy(renames["DisplayDataIn"])).optional(),
            "originalPipelineTransform": t.array(
                t.proxy(renames["TransformSummaryIn"])
            ).optional(),
        }
    ).named(renames["PipelineDescriptionIn"])
    types["PipelineDescriptionOut"] = t.struct(
        {
            "stepNamesHash": t.string().optional(),
            "executionPipelineStage": t.array(
                t.proxy(renames["ExecutionStageSummaryOut"])
            ).optional(),
            "displayData": t.array(t.proxy(renames["DisplayDataOut"])).optional(),
            "originalPipelineTransform": t.array(
                t.proxy(renames["TransformSummaryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PipelineDescriptionOut"])
    types["StageSummaryIn"] = t.struct(
        {
            "stragglerSummary": t.proxy(renames["StragglerSummaryIn"]).optional(),
            "startTime": t.string().optional(),
            "state": t.string().optional(),
            "stageId": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricUpdateIn"])).optional(),
            "endTime": t.string().optional(),
            "progress": t.proxy(renames["ProgressTimeseriesIn"]).optional(),
        }
    ).named(renames["StageSummaryIn"])
    types["StageSummaryOut"] = t.struct(
        {
            "stragglerSummary": t.proxy(renames["StragglerSummaryOut"]).optional(),
            "startTime": t.string().optional(),
            "state": t.string().optional(),
            "stageId": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricUpdateOut"])).optional(),
            "endTime": t.string().optional(),
            "progress": t.proxy(renames["ProgressTimeseriesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StageSummaryOut"])
    types["HotKeyDebuggingInfoIn"] = t.struct(
        {"detectedHotKeys": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["HotKeyDebuggingInfoIn"])
    types["HotKeyDebuggingInfoOut"] = t.struct(
        {
            "detectedHotKeys": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HotKeyDebuggingInfoOut"])
    types["WorkerMessageResponseIn"] = t.struct(
        {
            "workerThreadScalingReportResponse": t.proxy(
                renames["WorkerThreadScalingReportResponseIn"]
            ).optional(),
            "workerHealthReportResponse": t.proxy(
                renames["WorkerHealthReportResponseIn"]
            ).optional(),
            "workerShutdownNoticeResponse": t.proxy(
                renames["WorkerShutdownNoticeResponseIn"]
            ).optional(),
            "workerMetricsResponse": t.proxy(
                renames["ResourceUtilizationReportResponseIn"]
            ).optional(),
        }
    ).named(renames["WorkerMessageResponseIn"])
    types["WorkerMessageResponseOut"] = t.struct(
        {
            "workerThreadScalingReportResponse": t.proxy(
                renames["WorkerThreadScalingReportResponseOut"]
            ).optional(),
            "workerHealthReportResponse": t.proxy(
                renames["WorkerHealthReportResponseOut"]
            ).optional(),
            "workerShutdownNoticeResponse": t.proxy(
                renames["WorkerShutdownNoticeResponseOut"]
            ).optional(),
            "workerMetricsResponse": t.proxy(
                renames["ResourceUtilizationReportResponseOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerMessageResponseOut"])
    types["HotKeyInfoIn"] = t.struct(
        {
            "hotKeyAge": t.string().optional(),
            "keyTruncated": t.boolean().optional(),
            "key": t.string().optional(),
        }
    ).named(renames["HotKeyInfoIn"])
    types["HotKeyInfoOut"] = t.struct(
        {
            "hotKeyAge": t.string().optional(),
            "keyTruncated": t.boolean().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HotKeyInfoOut"])
    types["DebugOptionsIn"] = t.struct(
        {"enableHotKeyLogging": t.boolean().optional()}
    ).named(renames["DebugOptionsIn"])
    types["DebugOptionsOut"] = t.struct(
        {
            "enableHotKeyLogging": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DebugOptionsOut"])
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
    types["TaskRunnerSettingsIn"] = t.struct(
        {
            "alsologtostderr": t.boolean().optional(),
            "languageHint": t.string().optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "taskUser": t.string().optional(),
            "tempStoragePrefix": t.string().optional(),
            "vmId": t.string().optional(),
            "taskGroup": t.string().optional(),
            "logUploadLocation": t.string().optional(),
            "baseTaskDir": t.string().optional(),
            "workflowFileName": t.string().optional(),
            "dataflowApiVersion": t.string().optional(),
            "logToSerialconsole": t.boolean().optional(),
            "continueOnException": t.boolean().optional(),
            "harnessCommand": t.string().optional(),
            "parallelWorkerSettings": t.proxy(renames["WorkerSettingsIn"]).optional(),
            "commandlinesFileName": t.string().optional(),
            "logDir": t.string().optional(),
            "streamingWorkerMainClass": t.string().optional(),
            "baseUrl": t.string().optional(),
        }
    ).named(renames["TaskRunnerSettingsIn"])
    types["TaskRunnerSettingsOut"] = t.struct(
        {
            "alsologtostderr": t.boolean().optional(),
            "languageHint": t.string().optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "taskUser": t.string().optional(),
            "tempStoragePrefix": t.string().optional(),
            "vmId": t.string().optional(),
            "taskGroup": t.string().optional(),
            "logUploadLocation": t.string().optional(),
            "baseTaskDir": t.string().optional(),
            "workflowFileName": t.string().optional(),
            "dataflowApiVersion": t.string().optional(),
            "logToSerialconsole": t.boolean().optional(),
            "continueOnException": t.boolean().optional(),
            "harnessCommand": t.string().optional(),
            "parallelWorkerSettings": t.proxy(renames["WorkerSettingsOut"]).optional(),
            "commandlinesFileName": t.string().optional(),
            "logDir": t.string().optional(),
            "streamingWorkerMainClass": t.string().optional(),
            "baseUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskRunnerSettingsOut"])
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
    types["DistributionUpdateIn"] = t.struct(
        {
            "histogram": t.proxy(renames["HistogramIn"]).optional(),
            "count": t.proxy(renames["SplitInt64In"]).optional(),
            "max": t.proxy(renames["SplitInt64In"]).optional(),
            "min": t.proxy(renames["SplitInt64In"]).optional(),
            "sum": t.proxy(renames["SplitInt64In"]).optional(),
            "sumOfSquares": t.number().optional(),
        }
    ).named(renames["DistributionUpdateIn"])
    types["DistributionUpdateOut"] = t.struct(
        {
            "histogram": t.proxy(renames["HistogramOut"]).optional(),
            "count": t.proxy(renames["SplitInt64Out"]).optional(),
            "max": t.proxy(renames["SplitInt64Out"]).optional(),
            "min": t.proxy(renames["SplitInt64Out"]).optional(),
            "sum": t.proxy(renames["SplitInt64Out"]).optional(),
            "sumOfSquares": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DistributionUpdateOut"])
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
    types["ComponentSourceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "userName": t.string().optional(),
            "originalTransformOrCollection": t.string().optional(),
        }
    ).named(renames["ComponentSourceIn"])
    types["ComponentSourceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "userName": t.string().optional(),
            "originalTransformOrCollection": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComponentSourceOut"])
    types["WorkerLifecycleEventIn"] = t.struct(
        {
            "containerStartTime": t.string().optional(),
            "event": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["WorkerLifecycleEventIn"])
    types["WorkerLifecycleEventOut"] = t.struct(
        {
            "containerStartTime": t.string().optional(),
            "event": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerLifecycleEventOut"])
    types["SourceSplitShardIn"] = t.struct(
        {
            "derivationMode": t.string().optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
        }
    ).named(renames["SourceSplitShardIn"])
    types["SourceSplitShardOut"] = t.struct(
        {
            "derivationMode": t.string().optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceSplitShardOut"])
    types["SourceGetMetadataRequestIn"] = t.struct(
        {"source": t.proxy(renames["SourceIn"]).optional()}
    ).named(renames["SourceGetMetadataRequestIn"])
    types["SourceGetMetadataRequestOut"] = t.struct(
        {
            "source": t.proxy(renames["SourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceGetMetadataRequestOut"])
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
    types["ComputationTopologyIn"] = t.struct(
        {
            "outputs": t.array(t.proxy(renames["StreamLocationIn"])).optional(),
            "computationId": t.string().optional(),
            "systemStageName": t.string().optional(),
            "stateFamilies": t.array(
                t.proxy(renames["StateFamilyConfigIn"])
            ).optional(),
            "keyRanges": t.array(t.proxy(renames["KeyRangeLocationIn"])).optional(),
            "inputs": t.array(t.proxy(renames["StreamLocationIn"])).optional(),
        }
    ).named(renames["ComputationTopologyIn"])
    types["ComputationTopologyOut"] = t.struct(
        {
            "outputs": t.array(t.proxy(renames["StreamLocationOut"])).optional(),
            "computationId": t.string().optional(),
            "systemStageName": t.string().optional(),
            "stateFamilies": t.array(
                t.proxy(renames["StateFamilyConfigOut"])
            ).optional(),
            "keyRanges": t.array(t.proxy(renames["KeyRangeLocationOut"])).optional(),
            "inputs": t.array(t.proxy(renames["StreamLocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputationTopologyOut"])
    types["PubsubSnapshotMetadataIn"] = t.struct(
        {
            "snapshotName": t.string().optional(),
            "expireTime": t.string().optional(),
            "topicName": t.string().optional(),
        }
    ).named(renames["PubsubSnapshotMetadataIn"])
    types["PubsubSnapshotMetadataOut"] = t.struct(
        {
            "snapshotName": t.string().optional(),
            "expireTime": t.string().optional(),
            "topicName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubSnapshotMetadataOut"])
    types["CounterUpdateIn"] = t.struct(
        {
            "floatingPointList": t.proxy(renames["FloatingPointListIn"]).optional(),
            "boolean": t.boolean().optional(),
            "structuredNameAndMetadata": t.proxy(
                renames["CounterStructuredNameAndMetadataIn"]
            ).optional(),
            "nameAndKind": t.proxy(renames["NameAndKindIn"]).optional(),
            "stringList": t.proxy(renames["StringListIn"]).optional(),
            "distribution": t.proxy(renames["DistributionUpdateIn"]).optional(),
            "shortId": t.string().optional(),
            "floatingPoint": t.number().optional(),
            "cumulative": t.boolean().optional(),
            "internal": t.struct({"_": t.string().optional()}).optional(),
            "integerGauge": t.proxy(renames["IntegerGaugeIn"]).optional(),
            "integerList": t.proxy(renames["IntegerListIn"]).optional(),
            "integerMean": t.proxy(renames["IntegerMeanIn"]).optional(),
            "integer": t.proxy(renames["SplitInt64In"]).optional(),
            "floatingPointMean": t.proxy(renames["FloatingPointMeanIn"]).optional(),
        }
    ).named(renames["CounterUpdateIn"])
    types["CounterUpdateOut"] = t.struct(
        {
            "floatingPointList": t.proxy(renames["FloatingPointListOut"]).optional(),
            "boolean": t.boolean().optional(),
            "structuredNameAndMetadata": t.proxy(
                renames["CounterStructuredNameAndMetadataOut"]
            ).optional(),
            "nameAndKind": t.proxy(renames["NameAndKindOut"]).optional(),
            "stringList": t.proxy(renames["StringListOut"]).optional(),
            "distribution": t.proxy(renames["DistributionUpdateOut"]).optional(),
            "shortId": t.string().optional(),
            "floatingPoint": t.number().optional(),
            "cumulative": t.boolean().optional(),
            "internal": t.struct({"_": t.string().optional()}).optional(),
            "integerGauge": t.proxy(renames["IntegerGaugeOut"]).optional(),
            "integerList": t.proxy(renames["IntegerListOut"]).optional(),
            "integerMean": t.proxy(renames["IntegerMeanOut"]).optional(),
            "integer": t.proxy(renames["SplitInt64Out"]).optional(),
            "floatingPointMean": t.proxy(renames["FloatingPointMeanOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CounterUpdateOut"])
    types["TransformSummaryIn"] = t.struct(
        {
            "outputCollectionName": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "inputCollectionName": t.array(t.string()).optional(),
            "displayData": t.array(t.proxy(renames["DisplayDataIn"])).optional(),
        }
    ).named(renames["TransformSummaryIn"])
    types["TransformSummaryOut"] = t.struct(
        {
            "outputCollectionName": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "inputCollectionName": t.array(t.string()).optional(),
            "displayData": t.array(t.proxy(renames["DisplayDataOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransformSummaryOut"])
    types["SendDebugCaptureRequestIn"] = t.struct(
        {
            "dataFormat": t.string().optional(),
            "workerId": t.string().optional(),
            "data": t.string().optional(),
            "location": t.string().optional(),
            "componentId": t.string().optional(),
        }
    ).named(renames["SendDebugCaptureRequestIn"])
    types["SendDebugCaptureRequestOut"] = t.struct(
        {
            "dataFormat": t.string().optional(),
            "workerId": t.string().optional(),
            "data": t.string().optional(),
            "location": t.string().optional(),
            "componentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SendDebugCaptureRequestOut"])
    types["CPUTimeIn"] = t.struct(
        {
            "rate": t.number().optional(),
            "timestamp": t.string().optional(),
            "totalMs": t.string().optional(),
        }
    ).named(renames["CPUTimeIn"])
    types["CPUTimeOut"] = t.struct(
        {
            "rate": t.number().optional(),
            "timestamp": t.string().optional(),
            "totalMs": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CPUTimeOut"])
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
    types["StreamingStragglerInfoIn"] = t.struct(
        {
            "dataWatermarkLag": t.string().optional(),
            "systemWatermarkLag": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "workerName": t.string().optional(),
        }
    ).named(renames["StreamingStragglerInfoIn"])
    types["StreamingStragglerInfoOut"] = t.struct(
        {
            "dataWatermarkLag": t.string().optional(),
            "systemWatermarkLag": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "workerName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingStragglerInfoOut"])
    types["LeaseWorkItemRequestIn"] = t.struct(
        {
            "workerCapabilities": t.array(t.string()).optional(),
            "workItemTypes": t.array(t.string()).optional(),
            "requestedLeaseDuration": t.string().optional(),
            "location": t.string().optional(),
            "workerId": t.string().optional(),
            "unifiedWorkerRequest": t.struct({"_": t.string().optional()}).optional(),
            "currentWorkerTime": t.string().optional(),
        }
    ).named(renames["LeaseWorkItemRequestIn"])
    types["LeaseWorkItemRequestOut"] = t.struct(
        {
            "workerCapabilities": t.array(t.string()).optional(),
            "workItemTypes": t.array(t.string()).optional(),
            "requestedLeaseDuration": t.string().optional(),
            "location": t.string().optional(),
            "workerId": t.string().optional(),
            "unifiedWorkerRequest": t.struct({"_": t.string().optional()}).optional(),
            "currentWorkerTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LeaseWorkItemRequestOut"])
    types["TopologyConfigIn"] = t.struct(
        {
            "userStageToComputationNameMap": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "dataDiskAssignments": t.array(
                t.proxy(renames["DataDiskAssignmentIn"])
            ).optional(),
            "computations": t.array(
                t.proxy(renames["ComputationTopologyIn"])
            ).optional(),
            "forwardingKeyBits": t.integer().optional(),
            "persistentStateVersion": t.integer().optional(),
        }
    ).named(renames["TopologyConfigIn"])
    types["TopologyConfigOut"] = t.struct(
        {
            "userStageToComputationNameMap": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "dataDiskAssignments": t.array(
                t.proxy(renames["DataDiskAssignmentOut"])
            ).optional(),
            "computations": t.array(
                t.proxy(renames["ComputationTopologyOut"])
            ).optional(),
            "forwardingKeyBits": t.integer().optional(),
            "persistentStateVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TopologyConfigOut"])
    types["TemplateMetadataIn"] = t.struct(
        {
            "name": t.string(),
            "parameters": t.array(t.proxy(renames["ParameterMetadataIn"])).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["TemplateMetadataIn"])
    types["TemplateMetadataOut"] = t.struct(
        {
            "name": t.string(),
            "parameters": t.array(t.proxy(renames["ParameterMetadataOut"])).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TemplateMetadataOut"])
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
    types["ApproximateSplitRequestIn"] = t.struct(
        {
            "fractionOfRemainder": t.number().optional(),
            "position": t.proxy(renames["PositionIn"]).optional(),
            "fractionConsumed": t.number().optional(),
        }
    ).named(renames["ApproximateSplitRequestIn"])
    types["ApproximateSplitRequestOut"] = t.struct(
        {
            "fractionOfRemainder": t.number().optional(),
            "position": t.proxy(renames["PositionOut"]).optional(),
            "fractionConsumed": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApproximateSplitRequestOut"])
    types["CustomSourceLocationIn"] = t.struct(
        {"stateful": t.boolean().optional()}
    ).named(renames["CustomSourceLocationIn"])
    types["CustomSourceLocationOut"] = t.struct(
        {
            "stateful": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomSourceLocationOut"])
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
    types["StreamingStageLocationIn"] = t.struct(
        {"streamId": t.string().optional()}
    ).named(renames["StreamingStageLocationIn"])
    types["StreamingStageLocationOut"] = t.struct(
        {
            "streamId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingStageLocationOut"])
    types["FloatingPointListIn"] = t.struct(
        {"elements": t.array(t.number()).optional()}
    ).named(renames["FloatingPointListIn"])
    types["FloatingPointListOut"] = t.struct(
        {
            "elements": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloatingPointListOut"])
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
    types["FlattenInstructionIn"] = t.struct(
        {"inputs": t.array(t.proxy(renames["InstructionInputIn"])).optional()}
    ).named(renames["FlattenInstructionIn"])
    types["FlattenInstructionOut"] = t.struct(
        {
            "inputs": t.array(t.proxy(renames["InstructionInputOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FlattenInstructionOut"])
    types["ListJobMessagesResponseIn"] = t.struct(
        {
            "jobMessages": t.array(t.proxy(renames["JobMessageIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "autoscalingEvents": t.array(
                t.proxy(renames["AutoscalingEventIn"])
            ).optional(),
        }
    ).named(renames["ListJobMessagesResponseIn"])
    types["ListJobMessagesResponseOut"] = t.struct(
        {
            "jobMessages": t.array(t.proxy(renames["JobMessageOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "autoscalingEvents": t.array(
                t.proxy(renames["AutoscalingEventOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobMessagesResponseOut"])
    types["LaunchTemplateResponseIn"] = t.struct(
        {"job": t.proxy(renames["JobIn"]).optional()}
    ).named(renames["LaunchTemplateResponseIn"])
    types["LaunchTemplateResponseOut"] = t.struct(
        {
            "job": t.proxy(renames["JobOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LaunchTemplateResponseOut"])
    types["LaunchFlexTemplateParameterIn"] = t.struct(
        {
            "transformNameMappings": t.struct({"_": t.string().optional()}).optional(),
            "launchOptions": t.struct({"_": t.string().optional()}).optional(),
            "containerSpec": t.proxy(renames["ContainerSpecIn"]).optional(),
            "environment": t.proxy(
                renames["FlexTemplateRuntimeEnvironmentIn"]
            ).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "containerSpecGcsPath": t.string().optional(),
            "update": t.boolean().optional(),
            "jobName": t.string(),
        }
    ).named(renames["LaunchFlexTemplateParameterIn"])
    types["LaunchFlexTemplateParameterOut"] = t.struct(
        {
            "transformNameMappings": t.struct({"_": t.string().optional()}).optional(),
            "launchOptions": t.struct({"_": t.string().optional()}).optional(),
            "containerSpec": t.proxy(renames["ContainerSpecOut"]).optional(),
            "environment": t.proxy(
                renames["FlexTemplateRuntimeEnvironmentOut"]
            ).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "containerSpecGcsPath": t.string().optional(),
            "update": t.boolean().optional(),
            "jobName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LaunchFlexTemplateParameterOut"])
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
    types["ConcatPositionIn"] = t.struct(
        {
            "index": t.integer().optional(),
            "position": t.proxy(renames["PositionIn"]).optional(),
        }
    ).named(renames["ConcatPositionIn"])
    types["ConcatPositionOut"] = t.struct(
        {
            "index": t.integer().optional(),
            "position": t.proxy(renames["PositionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConcatPositionOut"])
    types["SourceIn"] = t.struct(
        {
            "codec": t.struct({"_": t.string().optional()}).optional(),
            "baseSpecs": t.array(t.struct({"_": t.string().optional()})).optional(),
            "spec": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.proxy(renames["SourceMetadataIn"]).optional(),
            "doesNotNeedSplitting": t.boolean().optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "codec": t.struct({"_": t.string().optional()}).optional(),
            "baseSpecs": t.array(t.struct({"_": t.string().optional()})).optional(),
            "spec": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.proxy(renames["SourceMetadataOut"]).optional(),
            "doesNotNeedSplitting": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["StreamLocationIn"] = t.struct(
        {
            "streamingStageLocation": t.proxy(
                renames["StreamingStageLocationIn"]
            ).optional(),
            "pubsubLocation": t.proxy(renames["PubsubLocationIn"]).optional(),
            "sideInputLocation": t.proxy(
                renames["StreamingSideInputLocationIn"]
            ).optional(),
            "customSourceLocation": t.proxy(
                renames["CustomSourceLocationIn"]
            ).optional(),
        }
    ).named(renames["StreamLocationIn"])
    types["StreamLocationOut"] = t.struct(
        {
            "streamingStageLocation": t.proxy(
                renames["StreamingStageLocationOut"]
            ).optional(),
            "pubsubLocation": t.proxy(renames["PubsubLocationOut"]).optional(),
            "sideInputLocation": t.proxy(
                renames["StreamingSideInputLocationOut"]
            ).optional(),
            "customSourceLocation": t.proxy(
                renames["CustomSourceLocationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamLocationOut"])
    types["BigQueryIODetailsIn"] = t.struct(
        {
            "query": t.string().optional(),
            "dataset": t.string().optional(),
            "projectId": t.string().optional(),
            "table": t.string().optional(),
        }
    ).named(renames["BigQueryIODetailsIn"])
    types["BigQueryIODetailsOut"] = t.struct(
        {
            "query": t.string().optional(),
            "dataset": t.string().optional(),
            "projectId": t.string().optional(),
            "table": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryIODetailsOut"])
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
            "split": t.proxy(renames["SourceSplitRequestIn"]).optional(),
            "getMetadata": t.proxy(renames["SourceGetMetadataRequestIn"]).optional(),
            "originalName": t.string().optional(),
            "name": t.string().optional(),
            "stageName": t.string().optional(),
        }
    ).named(renames["SourceOperationRequestIn"])
    types["SourceOperationRequestOut"] = t.struct(
        {
            "systemName": t.string().optional(),
            "split": t.proxy(renames["SourceSplitRequestOut"]).optional(),
            "getMetadata": t.proxy(renames["SourceGetMetadataRequestOut"]).optional(),
            "originalName": t.string().optional(),
            "name": t.string().optional(),
            "stageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOperationRequestOut"])
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
    types["ParameterMetadataEnumOptionIn"] = t.struct(
        {
            "label": t.string().optional(),
            "description": t.string().optional(),
            "value": t.string(),
        }
    ).named(renames["ParameterMetadataEnumOptionIn"])
    types["ParameterMetadataEnumOptionOut"] = t.struct(
        {
            "label": t.string().optional(),
            "description": t.string().optional(),
            "value": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParameterMetadataEnumOptionOut"])
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
    types["PositionIn"] = t.struct(
        {
            "byteOffset": t.string().optional(),
            "concatPosition": t.proxy(renames["ConcatPositionIn"]).optional(),
            "end": t.boolean().optional(),
            "recordIndex": t.string().optional(),
            "key": t.string().optional(),
            "shufflePosition": t.string().optional(),
        }
    ).named(renames["PositionIn"])
    types["PositionOut"] = t.struct(
        {
            "byteOffset": t.string().optional(),
            "concatPosition": t.proxy(renames["ConcatPositionOut"]).optional(),
            "end": t.boolean().optional(),
            "recordIndex": t.string().optional(),
            "key": t.string().optional(),
            "shufflePosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PositionOut"])
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
    types["StragglerDebuggingInfoIn"] = t.struct(
        {"hotKey": t.proxy(renames["HotKeyDebuggingInfoIn"]).optional()}
    ).named(renames["StragglerDebuggingInfoIn"])
    types["StragglerDebuggingInfoOut"] = t.struct(
        {
            "hotKey": t.proxy(renames["HotKeyDebuggingInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StragglerDebuggingInfoOut"])
    types["ContainerSpecIn"] = t.struct(
        {
            "metadata": t.proxy(renames["TemplateMetadataIn"]).optional(),
            "imageRepositoryPasswordSecretId": t.string().optional(),
            "imageRepositoryCertPath": t.string().optional(),
            "image": t.string().optional(),
            "sdkInfo": t.proxy(renames["SDKInfoIn"]),
            "imageRepositoryUsernameSecretId": t.string().optional(),
            "defaultEnvironment": t.proxy(
                renames["FlexTemplateRuntimeEnvironmentIn"]
            ).optional(),
        }
    ).named(renames["ContainerSpecIn"])
    types["ContainerSpecOut"] = t.struct(
        {
            "metadata": t.proxy(renames["TemplateMetadataOut"]).optional(),
            "imageRepositoryPasswordSecretId": t.string().optional(),
            "imageRepositoryCertPath": t.string().optional(),
            "image": t.string().optional(),
            "sdkInfo": t.proxy(renames["SDKInfoOut"]),
            "imageRepositoryUsernameSecretId": t.string().optional(),
            "defaultEnvironment": t.proxy(
                renames["FlexTemplateRuntimeEnvironmentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerSpecOut"])
    types["MapTaskIn"] = t.struct(
        {
            "stageName": t.string().optional(),
            "systemName": t.string().optional(),
            "counterPrefix": t.string().optional(),
            "instructions": t.array(
                t.proxy(renames["ParallelInstructionIn"])
            ).optional(),
        }
    ).named(renames["MapTaskIn"])
    types["MapTaskOut"] = t.struct(
        {
            "stageName": t.string().optional(),
            "systemName": t.string().optional(),
            "counterPrefix": t.string().optional(),
            "instructions": t.array(
                t.proxy(renames["ParallelInstructionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MapTaskOut"])
    types["RuntimeEnvironmentIn"] = t.struct(
        {
            "workerZone": t.string().optional(),
            "bypassTempDirValidation": t.boolean().optional(),
            "machineType": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "network": t.string().optional(),
            "workerRegion": t.string(),
            "maxWorkers": t.integer().optional(),
            "subnetwork": t.string().optional(),
            "tempLocation": t.string(),
            "enableStreamingEngine": t.boolean().optional(),
            "numWorkers": t.integer().optional(),
            "zone": t.string().optional(),
            "ipConfiguration": t.string().optional(),
            "kmsKeyName": t.string().optional(),
        }
    ).named(renames["RuntimeEnvironmentIn"])
    types["RuntimeEnvironmentOut"] = t.struct(
        {
            "workerZone": t.string().optional(),
            "bypassTempDirValidation": t.boolean().optional(),
            "machineType": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "network": t.string().optional(),
            "workerRegion": t.string(),
            "maxWorkers": t.integer().optional(),
            "subnetwork": t.string().optional(),
            "tempLocation": t.string(),
            "enableStreamingEngine": t.boolean().optional(),
            "numWorkers": t.integer().optional(),
            "zone": t.string().optional(),
            "ipConfiguration": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeEnvironmentOut"])
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
    types["JobExecutionStageInfoIn"] = t.struct(
        {"stepName": t.array(t.string()).optional()}
    ).named(renames["JobExecutionStageInfoIn"])
    types["JobExecutionStageInfoOut"] = t.struct(
        {
            "stepName": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobExecutionStageInfoOut"])
    types["SnapshotJobRequestIn"] = t.struct(
        {
            "location": t.string().optional(),
            "snapshotSources": t.boolean().optional(),
            "description": t.string().optional(),
            "ttl": t.string().optional(),
        }
    ).named(renames["SnapshotJobRequestIn"])
    types["SnapshotJobRequestOut"] = t.struct(
        {
            "location": t.string().optional(),
            "snapshotSources": t.boolean().optional(),
            "description": t.string().optional(),
            "ttl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnapshotJobRequestOut"])
    types["PubsubLocationIn"] = t.struct(
        {
            "subscription": t.string().optional(),
            "trackingSubscription": t.string().optional(),
            "timestampLabel": t.string().optional(),
            "dynamicDestinations": t.boolean().optional(),
            "topic": t.string().optional(),
            "dropLateData": t.boolean().optional(),
            "idLabel": t.string().optional(),
            "withAttributes": t.boolean().optional(),
        }
    ).named(renames["PubsubLocationIn"])
    types["PubsubLocationOut"] = t.struct(
        {
            "subscription": t.string().optional(),
            "trackingSubscription": t.string().optional(),
            "timestampLabel": t.string().optional(),
            "dynamicDestinations": t.boolean().optional(),
            "topic": t.string().optional(),
            "dropLateData": t.boolean().optional(),
            "idLabel": t.string().optional(),
            "withAttributes": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubLocationOut"])
    types["FlexTemplateRuntimeEnvironmentIn"] = t.struct(
        {
            "saveHeapDumpsToGcsPath": t.string().optional(),
            "dumpHeapOnOom": t.boolean().optional(),
            "workerRegion": t.string().optional(),
            "maxWorkers": t.integer().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "network": t.string().optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "subnetwork": t.string().optional(),
            "flexrsGoal": t.string().optional(),
            "enableLauncherVmSerialPortLogging": t.boolean().optional(),
            "tempLocation": t.string().optional(),
            "enableStreamingEngine": t.boolean().optional(),
            "launcherMachineType": t.string().optional(),
            "zone": t.string().optional(),
            "diskSizeGb": t.integer().optional(),
            "numWorkers": t.integer().optional(),
            "stagingLocation": t.string().optional(),
            "machineType": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "autoscalingAlgorithm": t.string().optional(),
            "sdkContainerImage": t.string().optional(),
            "ipConfiguration": t.string().optional(),
            "workerZone": t.string().optional(),
            "kmsKeyName": t.string().optional(),
        }
    ).named(renames["FlexTemplateRuntimeEnvironmentIn"])
    types["FlexTemplateRuntimeEnvironmentOut"] = t.struct(
        {
            "saveHeapDumpsToGcsPath": t.string().optional(),
            "dumpHeapOnOom": t.boolean().optional(),
            "workerRegion": t.string().optional(),
            "maxWorkers": t.integer().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "network": t.string().optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "subnetwork": t.string().optional(),
            "flexrsGoal": t.string().optional(),
            "enableLauncherVmSerialPortLogging": t.boolean().optional(),
            "tempLocation": t.string().optional(),
            "enableStreamingEngine": t.boolean().optional(),
            "launcherMachineType": t.string().optional(),
            "zone": t.string().optional(),
            "diskSizeGb": t.integer().optional(),
            "numWorkers": t.integer().optional(),
            "stagingLocation": t.string().optional(),
            "machineType": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "autoscalingAlgorithm": t.string().optional(),
            "sdkContainerImage": t.string().optional(),
            "ipConfiguration": t.string().optional(),
            "workerZone": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FlexTemplateRuntimeEnvironmentOut"])
    types["WorkerHealthReportIn"] = t.struct(
        {
            "vmStartupTime": t.string().optional(),
            "pods": t.array(t.struct({"_": t.string().optional()})).optional(),
            "vmIsBroken": t.boolean().optional(),
            "vmIsHealthy": t.boolean().optional(),
            "msg": t.string().optional(),
            "reportInterval": t.string().optional(),
            "vmBrokenCode": t.string().optional(),
        }
    ).named(renames["WorkerHealthReportIn"])
    types["WorkerHealthReportOut"] = t.struct(
        {
            "vmStartupTime": t.string().optional(),
            "pods": t.array(t.struct({"_": t.string().optional()})).optional(),
            "vmIsBroken": t.boolean().optional(),
            "vmIsHealthy": t.boolean().optional(),
            "msg": t.string().optional(),
            "reportInterval": t.string().optional(),
            "vmBrokenCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerHealthReportOut"])
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
    types["WorkItemDetailsIn"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["MetricUpdateIn"])).optional(),
            "progress": t.proxy(renames["ProgressTimeseriesIn"]).optional(),
            "stragglerInfo": t.proxy(renames["StragglerInfoIn"]).optional(),
            "taskId": t.string().optional(),
            "state": t.string().optional(),
            "startTime": t.string().optional(),
            "attemptId": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["WorkItemDetailsIn"])
    types["WorkItemDetailsOut"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["MetricUpdateOut"])).optional(),
            "progress": t.proxy(renames["ProgressTimeseriesOut"]).optional(),
            "stragglerInfo": t.proxy(renames["StragglerInfoOut"]).optional(),
            "taskId": t.string().optional(),
            "state": t.string().optional(),
            "startTime": t.string().optional(),
            "attemptId": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkItemDetailsOut"])
    types["SourceGetMetadataResponseIn"] = t.struct(
        {"metadata": t.proxy(renames["SourceMetadataIn"]).optional()}
    ).named(renames["SourceGetMetadataResponseIn"])
    types["SourceGetMetadataResponseOut"] = t.struct(
        {
            "metadata": t.proxy(renames["SourceMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceGetMetadataResponseOut"])
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
            "unifiedWorkerRequest": t.struct({"_": t.string().optional()}).optional(),
            "location": t.string().optional(),
            "currentWorkerTime": t.string().optional(),
            "workItemStatuses": t.array(
                t.proxy(renames["WorkItemStatusIn"])
            ).optional(),
            "workerId": t.string().optional(),
        }
    ).named(renames["ReportWorkItemStatusRequestIn"])
    types["ReportWorkItemStatusRequestOut"] = t.struct(
        {
            "unifiedWorkerRequest": t.struct({"_": t.string().optional()}).optional(),
            "location": t.string().optional(),
            "currentWorkerTime": t.string().optional(),
            "workItemStatuses": t.array(
                t.proxy(renames["WorkItemStatusOut"])
            ).optional(),
            "workerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportWorkItemStatusRequestOut"])
    types["EnvironmentIn"] = t.struct(
        {
            "serviceKmsKeyName": t.string().optional(),
            "tempStoragePrefix": t.string().optional(),
            "experiments": t.array(t.string()).optional(),
            "workerRegion": t.string().optional(),
            "clusterManagerApiService": t.string().optional(),
            "internalExperiments": t.struct({"_": t.string().optional()}).optional(),
            "dataset": t.string().optional(),
            "flexResourceSchedulingGoal": t.string().optional(),
            "userAgent": t.struct({"_": t.string().optional()}).optional(),
            "sdkPipelineOptions": t.struct({"_": t.string().optional()}).optional(),
            "version": t.struct({"_": t.string().optional()}).optional(),
            "serviceOptions": t.array(t.string()).optional(),
            "serviceAccountEmail": t.string().optional(),
            "workerZone": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsIn"]).optional(),
            "workerPools": t.array(t.proxy(renames["WorkerPoolIn"])).optional(),
        }
    ).named(renames["EnvironmentIn"])
    types["EnvironmentOut"] = t.struct(
        {
            "serviceKmsKeyName": t.string().optional(),
            "tempStoragePrefix": t.string().optional(),
            "experiments": t.array(t.string()).optional(),
            "workerRegion": t.string().optional(),
            "clusterManagerApiService": t.string().optional(),
            "internalExperiments": t.struct({"_": t.string().optional()}).optional(),
            "dataset": t.string().optional(),
            "flexResourceSchedulingGoal": t.string().optional(),
            "userAgent": t.struct({"_": t.string().optional()}).optional(),
            "sdkPipelineOptions": t.struct({"_": t.string().optional()}).optional(),
            "version": t.struct({"_": t.string().optional()}).optional(),
            "serviceOptions": t.array(t.string()).optional(),
            "serviceAccountEmail": t.string().optional(),
            "workerZone": t.string().optional(),
            "debugOptions": t.proxy(renames["DebugOptionsOut"]).optional(),
            "shuffleMode": t.string().optional(),
            "workerPools": t.array(t.proxy(renames["WorkerPoolOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentOut"])
    types["GetDebugConfigResponseIn"] = t.struct(
        {"config": t.string().optional()}
    ).named(renames["GetDebugConfigResponseIn"])
    types["GetDebugConfigResponseOut"] = t.struct(
        {
            "config": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetDebugConfigResponseOut"])
    types["LaunchFlexTemplateResponseIn"] = t.struct(
        {"job": t.proxy(renames["JobIn"]).optional()}
    ).named(renames["LaunchFlexTemplateResponseIn"])
    types["LaunchFlexTemplateResponseOut"] = t.struct(
        {
            "job": t.proxy(renames["JobOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LaunchFlexTemplateResponseOut"])
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
    types["ResourceUtilizationReportResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ResourceUtilizationReportResponseIn"])
    types["ResourceUtilizationReportResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResourceUtilizationReportResponseOut"])
    types["WorkerPoolIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "numThreadsPerWorker": t.integer().optional(),
            "defaultPackageSet": t.string().optional(),
            "teardownPolicy": t.string().optional(),
            "workerHarnessContainerImage": t.string(),
            "taskrunnerSettings": t.proxy(renames["TaskRunnerSettingsIn"]).optional(),
            "numWorkers": t.integer().optional(),
            "ipConfiguration": t.string().optional(),
            "subnetwork": t.string().optional(),
            "zone": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "onHostMaintenance": t.string().optional(),
            "diskSizeGb": t.integer().optional(),
            "packages": t.array(t.proxy(renames["PackageIn"])).optional(),
            "sdkHarnessContainerImages": t.array(
                t.proxy(renames["SdkHarnessContainerImageIn"])
            ).optional(),
            "machineType": t.string().optional(),
            "diskSourceImage": t.string().optional(),
            "network": t.string().optional(),
            "poolArgs": t.struct({"_": t.string().optional()}).optional(),
            "autoscalingSettings": t.proxy(renames["AutoscalingSettingsIn"]).optional(),
            "diskType": t.string().optional(),
            "dataDisks": t.array(t.proxy(renames["DiskIn"])).optional(),
        }
    ).named(renames["WorkerPoolIn"])
    types["WorkerPoolOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "numThreadsPerWorker": t.integer().optional(),
            "defaultPackageSet": t.string().optional(),
            "teardownPolicy": t.string().optional(),
            "workerHarnessContainerImage": t.string(),
            "taskrunnerSettings": t.proxy(renames["TaskRunnerSettingsOut"]).optional(),
            "numWorkers": t.integer().optional(),
            "ipConfiguration": t.string().optional(),
            "subnetwork": t.string().optional(),
            "zone": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "onHostMaintenance": t.string().optional(),
            "diskSizeGb": t.integer().optional(),
            "packages": t.array(t.proxy(renames["PackageOut"])).optional(),
            "sdkHarnessContainerImages": t.array(
                t.proxy(renames["SdkHarnessContainerImageOut"])
            ).optional(),
            "machineType": t.string().optional(),
            "diskSourceImage": t.string().optional(),
            "network": t.string().optional(),
            "poolArgs": t.struct({"_": t.string().optional()}).optional(),
            "autoscalingSettings": t.proxy(
                renames["AutoscalingSettingsOut"]
            ).optional(),
            "diskType": t.string().optional(),
            "dataDisks": t.array(t.proxy(renames["DiskOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerPoolOut"])
    types["ParallelInstructionIn"] = t.struct(
        {
            "name": t.string().optional(),
            "flatten": t.proxy(renames["FlattenInstructionIn"]).optional(),
            "outputs": t.array(t.proxy(renames["InstructionOutputIn"])).optional(),
            "partialGroupByKey": t.proxy(
                renames["PartialGroupByKeyInstructionIn"]
            ).optional(),
            "parDo": t.proxy(renames["ParDoInstructionIn"]).optional(),
            "originalName": t.string().optional(),
            "read": t.proxy(renames["ReadInstructionIn"]).optional(),
            "systemName": t.string().optional(),
            "write": t.proxy(renames["WriteInstructionIn"]).optional(),
        }
    ).named(renames["ParallelInstructionIn"])
    types["ParallelInstructionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "flatten": t.proxy(renames["FlattenInstructionOut"]).optional(),
            "outputs": t.array(t.proxy(renames["InstructionOutputOut"])).optional(),
            "partialGroupByKey": t.proxy(
                renames["PartialGroupByKeyInstructionOut"]
            ).optional(),
            "parDo": t.proxy(renames["ParDoInstructionOut"]).optional(),
            "originalName": t.string().optional(),
            "read": t.proxy(renames["ReadInstructionOut"]).optional(),
            "systemName": t.string().optional(),
            "write": t.proxy(renames["WriteInstructionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParallelInstructionOut"])
    types["FailedLocationIn"] = t.struct({"name": t.string().optional()}).named(
        renames["FailedLocationIn"]
    )
    types["FailedLocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FailedLocationOut"])
    types["WorkerThreadScalingReportIn"] = t.struct(
        {"currentThreadCount": t.integer().optional()}
    ).named(renames["WorkerThreadScalingReportIn"])
    types["WorkerThreadScalingReportOut"] = t.struct(
        {
            "currentThreadCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerThreadScalingReportOut"])
    types["ResourceUtilizationReportIn"] = t.struct(
        {
            "containers": t.struct({"_": t.string().optional()}).optional(),
            "memoryInfo": t.array(t.proxy(renames["MemInfoIn"])).optional(),
            "cpuTime": t.array(t.proxy(renames["CPUTimeIn"])).optional(),
        }
    ).named(renames["ResourceUtilizationReportIn"])
    types["ResourceUtilizationReportOut"] = t.struct(
        {
            "containers": t.struct({"_": t.string().optional()}).optional(),
            "memoryInfo": t.array(t.proxy(renames["MemInfoOut"])).optional(),
            "cpuTime": t.array(t.proxy(renames["CPUTimeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceUtilizationReportOut"])
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
    types["WorkItemIn"] = t.struct(
        {
            "packages": t.array(t.proxy(renames["PackageIn"])).optional(),
            "mapTask": t.proxy(renames["MapTaskIn"]).optional(),
            "streamingConfigTask": t.proxy(renames["StreamingConfigTaskIn"]).optional(),
            "id": t.string().optional(),
            "reportStatusInterval": t.string().optional(),
            "streamingComputationTask": t.proxy(
                renames["StreamingComputationTaskIn"]
            ).optional(),
            "shellTask": t.proxy(renames["ShellTaskIn"]).optional(),
            "initialReportIndex": t.string().optional(),
            "jobId": t.string().optional(),
            "streamingSetupTask": t.proxy(renames["StreamingSetupTaskIn"]).optional(),
            "configuration": t.string().optional(),
            "projectId": t.string().optional(),
            "seqMapTask": t.proxy(renames["SeqMapTaskIn"]).optional(),
            "sourceOperationTask": t.proxy(
                renames["SourceOperationRequestIn"]
            ).optional(),
            "leaseExpireTime": t.string().optional(),
        }
    ).named(renames["WorkItemIn"])
    types["WorkItemOut"] = t.struct(
        {
            "packages": t.array(t.proxy(renames["PackageOut"])).optional(),
            "mapTask": t.proxy(renames["MapTaskOut"]).optional(),
            "streamingConfigTask": t.proxy(
                renames["StreamingConfigTaskOut"]
            ).optional(),
            "id": t.string().optional(),
            "reportStatusInterval": t.string().optional(),
            "streamingComputationTask": t.proxy(
                renames["StreamingComputationTaskOut"]
            ).optional(),
            "shellTask": t.proxy(renames["ShellTaskOut"]).optional(),
            "initialReportIndex": t.string().optional(),
            "jobId": t.string().optional(),
            "streamingSetupTask": t.proxy(renames["StreamingSetupTaskOut"]).optional(),
            "configuration": t.string().optional(),
            "projectId": t.string().optional(),
            "seqMapTask": t.proxy(renames["SeqMapTaskOut"]).optional(),
            "sourceOperationTask": t.proxy(
                renames["SourceOperationRequestOut"]
            ).optional(),
            "leaseExpireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkItemOut"])
    types["StreamingSetupTaskIn"] = t.struct(
        {
            "drain": t.boolean().optional(),
            "receiveWorkPort": t.integer().optional(),
            "workerHarnessPort": t.integer().optional(),
            "snapshotConfig": t.proxy(
                renames["StreamingApplianceSnapshotConfigIn"]
            ).optional(),
            "streamingComputationTopology": t.proxy(
                renames["TopologyConfigIn"]
            ).optional(),
        }
    ).named(renames["StreamingSetupTaskIn"])
    types["StreamingSetupTaskOut"] = t.struct(
        {
            "drain": t.boolean().optional(),
            "receiveWorkPort": t.integer().optional(),
            "workerHarnessPort": t.integer().optional(),
            "snapshotConfig": t.proxy(
                renames["StreamingApplianceSnapshotConfigOut"]
            ).optional(),
            "streamingComputationTopology": t.proxy(
                renames["TopologyConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingSetupTaskOut"])
    types["ListSnapshotsResponseIn"] = t.struct(
        {"snapshots": t.array(t.proxy(renames["SnapshotIn"])).optional()}
    ).named(renames["ListSnapshotsResponseIn"])
    types["ListSnapshotsResponseOut"] = t.struct(
        {
            "snapshots": t.array(t.proxy(renames["SnapshotOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSnapshotsResponseOut"])
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
    types["StateFamilyConfigIn"] = t.struct(
        {"stateFamily": t.string().optional(), "isRead": t.boolean().optional()}
    ).named(renames["StateFamilyConfigIn"])
    types["StateFamilyConfigOut"] = t.struct(
        {
            "stateFamily": t.string().optional(),
            "isRead": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StateFamilyConfigOut"])
    types["SourceForkIn"] = t.struct(
        {
            "primarySource": t.proxy(renames["DerivedSourceIn"]).optional(),
            "primary": t.proxy(renames["SourceSplitShardIn"]).optional(),
            "residualSource": t.proxy(renames["DerivedSourceIn"]).optional(),
            "residual": t.proxy(renames["SourceSplitShardIn"]).optional(),
        }
    ).named(renames["SourceForkIn"])
    types["SourceForkOut"] = t.struct(
        {
            "primarySource": t.proxy(renames["DerivedSourceOut"]).optional(),
            "primary": t.proxy(renames["SourceSplitShardOut"]).optional(),
            "residualSource": t.proxy(renames["DerivedSourceOut"]).optional(),
            "residual": t.proxy(renames["SourceSplitShardOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceForkOut"])
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
    types["MemInfoIn"] = t.struct(
        {
            "currentLimitBytes": t.string().optional(),
            "currentRssBytes": t.string().optional(),
            "totalGbMs": t.string().optional(),
            "currentOoms": t.string().optional(),
            "timestamp": t.string().optional(),
        }
    ).named(renames["MemInfoIn"])
    types["MemInfoOut"] = t.struct(
        {
            "currentLimitBytes": t.string().optional(),
            "currentRssBytes": t.string().optional(),
            "totalGbMs": t.string().optional(),
            "currentOoms": t.string().optional(),
            "timestamp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemInfoOut"])
    types["AutoscalingEventIn"] = t.struct(
        {
            "workerPool": t.string().optional(),
            "eventType": t.string().optional(),
            "currentNumWorkers": t.string().optional(),
            "targetNumWorkers": t.string().optional(),
            "description": t.proxy(renames["StructuredMessageIn"]).optional(),
            "time": t.string().optional(),
        }
    ).named(renames["AutoscalingEventIn"])
    types["AutoscalingEventOut"] = t.struct(
        {
            "workerPool": t.string().optional(),
            "eventType": t.string().optional(),
            "currentNumWorkers": t.string().optional(),
            "targetNumWorkers": t.string().optional(),
            "description": t.proxy(renames["StructuredMessageOut"]).optional(),
            "time": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoscalingEventOut"])
    types["CounterStructuredNameIn"] = t.struct(
        {
            "componentStepName": t.string().optional(),
            "portion": t.string().optional(),
            "inputIndex": t.integer().optional(),
            "workerId": t.string().optional(),
            "executionStepName": t.string().optional(),
            "originalRequestingStepName": t.string().optional(),
            "name": t.string().optional(),
            "origin": t.string().optional(),
            "originNamespace": t.string().optional(),
            "originalStepName": t.string().optional(),
        }
    ).named(renames["CounterStructuredNameIn"])
    types["CounterStructuredNameOut"] = t.struct(
        {
            "componentStepName": t.string().optional(),
            "portion": t.string().optional(),
            "inputIndex": t.integer().optional(),
            "workerId": t.string().optional(),
            "executionStepName": t.string().optional(),
            "originalRequestingStepName": t.string().optional(),
            "name": t.string().optional(),
            "origin": t.string().optional(),
            "originNamespace": t.string().optional(),
            "originalStepName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CounterStructuredNameOut"])
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
    types["DeleteSnapshotResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteSnapshotResponseIn"]
    )
    types["DeleteSnapshotResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteSnapshotResponseOut"])
    types["ParDoInstructionIn"] = t.struct(
        {
            "sideInputs": t.array(t.proxy(renames["SideInputInfoIn"])).optional(),
            "multiOutputInfos": t.array(
                t.proxy(renames["MultiOutputInfoIn"])
            ).optional(),
            "input": t.proxy(renames["InstructionInputIn"]).optional(),
            "numOutputs": t.integer().optional(),
            "userFn": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ParDoInstructionIn"])
    types["ParDoInstructionOut"] = t.struct(
        {
            "sideInputs": t.array(t.proxy(renames["SideInputInfoOut"])).optional(),
            "multiOutputInfos": t.array(
                t.proxy(renames["MultiOutputInfoOut"])
            ).optional(),
            "input": t.proxy(renames["InstructionInputOut"]).optional(),
            "numOutputs": t.integer().optional(),
            "userFn": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParDoInstructionOut"])
    types["WorkerShutdownNoticeResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["WorkerShutdownNoticeResponseIn"])
    types["WorkerShutdownNoticeResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WorkerShutdownNoticeResponseOut"])
    types["MetricUpdateIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "cumulative": t.boolean().optional(),
            "gauge": t.struct({"_": t.string().optional()}).optional(),
            "set": t.struct({"_": t.string().optional()}).optional(),
            "meanSum": t.struct({"_": t.string().optional()}).optional(),
            "meanCount": t.struct({"_": t.string().optional()}).optional(),
            "distribution": t.struct({"_": t.string().optional()}).optional(),
            "name": t.proxy(renames["MetricStructuredNameIn"]).optional(),
            "updateTime": t.string().optional(),
            "scalar": t.struct({"_": t.string().optional()}).optional(),
            "internal": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["MetricUpdateIn"])
    types["MetricUpdateOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "cumulative": t.boolean().optional(),
            "gauge": t.struct({"_": t.string().optional()}).optional(),
            "set": t.struct({"_": t.string().optional()}).optional(),
            "meanSum": t.struct({"_": t.string().optional()}).optional(),
            "meanCount": t.struct({"_": t.string().optional()}).optional(),
            "distribution": t.struct({"_": t.string().optional()}).optional(),
            "name": t.proxy(renames["MetricStructuredNameOut"]).optional(),
            "updateTime": t.string().optional(),
            "scalar": t.struct({"_": t.string().optional()}).optional(),
            "internal": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricUpdateOut"])
    types["WriteInstructionIn"] = t.struct(
        {
            "input": t.proxy(renames["InstructionInputIn"]).optional(),
            "sink": t.proxy(renames["SinkIn"]).optional(),
        }
    ).named(renames["WriteInstructionIn"])
    types["WriteInstructionOut"] = t.struct(
        {
            "input": t.proxy(renames["InstructionInputOut"]).optional(),
            "sink": t.proxy(renames["SinkOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteInstructionOut"])
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
    types["WorkerHealthReportResponseIn"] = t.struct(
        {"reportInterval": t.string().optional()}
    ).named(renames["WorkerHealthReportResponseIn"])
    types["WorkerHealthReportResponseOut"] = t.struct(
        {
            "reportInterval": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerHealthReportResponseOut"])
    types["ParameterMetadataIn"] = t.struct(
        {
            "paramType": t.string().optional(),
            "regexes": t.array(t.string()).optional(),
            "groupName": t.string().optional(),
            "parentTriggerValues": t.array(t.string()).optional(),
            "isOptional": t.boolean().optional(),
            "customMetadata": t.struct({"_": t.string().optional()}).optional(),
            "parentName": t.string().optional(),
            "name": t.string(),
            "helpText": t.string(),
            "enumOptions": t.array(
                t.proxy(renames["ParameterMetadataEnumOptionIn"])
            ).optional(),
            "label": t.string(),
        }
    ).named(renames["ParameterMetadataIn"])
    types["ParameterMetadataOut"] = t.struct(
        {
            "paramType": t.string().optional(),
            "regexes": t.array(t.string()).optional(),
            "groupName": t.string().optional(),
            "parentTriggerValues": t.array(t.string()).optional(),
            "isOptional": t.boolean().optional(),
            "customMetadata": t.struct({"_": t.string().optional()}).optional(),
            "parentName": t.string().optional(),
            "name": t.string(),
            "helpText": t.string(),
            "enumOptions": t.array(
                t.proxy(renames["ParameterMetadataEnumOptionOut"])
            ).optional(),
            "label": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParameterMetadataOut"])
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
    types["PartialGroupByKeyInstructionIn"] = t.struct(
        {
            "input": t.proxy(renames["InstructionInputIn"]).optional(),
            "valueCombiningFn": t.struct({"_": t.string().optional()}).optional(),
            "originalCombineValuesInputStoreName": t.string().optional(),
            "originalCombineValuesStepName": t.string().optional(),
            "sideInputs": t.array(t.proxy(renames["SideInputInfoIn"])).optional(),
            "inputElementCodec": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PartialGroupByKeyInstructionIn"])
    types["PartialGroupByKeyInstructionOut"] = t.struct(
        {
            "input": t.proxy(renames["InstructionInputOut"]).optional(),
            "valueCombiningFn": t.struct({"_": t.string().optional()}).optional(),
            "originalCombineValuesInputStoreName": t.string().optional(),
            "originalCombineValuesStepName": t.string().optional(),
            "sideInputs": t.array(t.proxy(renames["SideInputInfoOut"])).optional(),
            "inputElementCodec": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartialGroupByKeyInstructionOut"])
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
    types["GetTemplateResponseIn"] = t.struct(
        {
            "runtimeMetadata": t.proxy(renames["RuntimeMetadataIn"]).optional(),
            "status": t.proxy(renames["StatusIn"]).optional(),
            "templateType": t.string().optional(),
            "metadata": t.proxy(renames["TemplateMetadataIn"]).optional(),
        }
    ).named(renames["GetTemplateResponseIn"])
    types["GetTemplateResponseOut"] = t.struct(
        {
            "runtimeMetadata": t.proxy(renames["RuntimeMetadataOut"]).optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "templateType": t.string().optional(),
            "metadata": t.proxy(renames["TemplateMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetTemplateResponseOut"])
    types["StreamingConfigTaskIn"] = t.struct(
        {
            "windmillServiceEndpoint": t.string().optional(),
            "getDataStreamChunkSizeBytes": t.string().optional(),
            "streamingComputationConfigs": t.array(
                t.proxy(renames["StreamingComputationConfigIn"])
            ).optional(),
            "maxWorkItemCommitBytes": t.string().optional(),
            "windmillServicePort": t.string().optional(),
            "userStepToStateFamilyNameMap": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "commitStreamChunkSizeBytes": t.string().optional(),
        }
    ).named(renames["StreamingConfigTaskIn"])
    types["StreamingConfigTaskOut"] = t.struct(
        {
            "windmillServiceEndpoint": t.string().optional(),
            "getDataStreamChunkSizeBytes": t.string().optional(),
            "streamingComputationConfigs": t.array(
                t.proxy(renames["StreamingComputationConfigOut"])
            ).optional(),
            "maxWorkItemCommitBytes": t.string().optional(),
            "windmillServicePort": t.string().optional(),
            "userStepToStateFamilyNameMap": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "commitStreamChunkSizeBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingConfigTaskOut"])
    types["WorkerMessageIn"] = t.struct(
        {
            "workerThreadScalingReport": t.proxy(
                renames["WorkerThreadScalingReportIn"]
            ).optional(),
            "workerMetrics": t.proxy(renames["ResourceUtilizationReportIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "workerHealthReport": t.proxy(renames["WorkerHealthReportIn"]).optional(),
            "time": t.string().optional(),
            "workerMessageCode": t.proxy(renames["WorkerMessageCodeIn"]).optional(),
            "workerShutdownNotice": t.proxy(
                renames["WorkerShutdownNoticeIn"]
            ).optional(),
            "workerLifecycleEvent": t.proxy(
                renames["WorkerLifecycleEventIn"]
            ).optional(),
        }
    ).named(renames["WorkerMessageIn"])
    types["WorkerMessageOut"] = t.struct(
        {
            "workerThreadScalingReport": t.proxy(
                renames["WorkerThreadScalingReportOut"]
            ).optional(),
            "workerMetrics": t.proxy(
                renames["ResourceUtilizationReportOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "workerHealthReport": t.proxy(renames["WorkerHealthReportOut"]).optional(),
            "time": t.string().optional(),
            "workerMessageCode": t.proxy(renames["WorkerMessageCodeOut"]).optional(),
            "workerShutdownNotice": t.proxy(
                renames["WorkerShutdownNoticeOut"]
            ).optional(),
            "workerLifecycleEvent": t.proxy(
                renames["WorkerLifecycleEventOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerMessageOut"])
    types["JobMessageIn"] = t.struct(
        {
            "messageImportance": t.string().optional(),
            "messageText": t.string().optional(),
            "time": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["JobMessageIn"])
    types["JobMessageOut"] = t.struct(
        {
            "messageImportance": t.string().optional(),
            "messageText": t.string().optional(),
            "time": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobMessageOut"])
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
    types["WorkItemServiceStateIn"] = t.struct(
        {
            "reportStatusInterval": t.string().optional(),
            "leaseExpireTime": t.string().optional(),
            "suggestedStopPosition": t.proxy(renames["PositionIn"]).optional(),
            "hotKeyDetection": t.proxy(renames["HotKeyDetectionIn"]).optional(),
            "metricShortId": t.array(t.proxy(renames["MetricShortIdIn"])).optional(),
            "harnessData": t.struct({"_": t.string().optional()}).optional(),
            "splitRequest": t.proxy(renames["ApproximateSplitRequestIn"]).optional(),
            "completeWorkStatus": t.proxy(renames["StatusIn"]).optional(),
            "nextReportIndex": t.string().optional(),
            "suggestedStopPoint": t.proxy(renames["ApproximateProgressIn"]).optional(),
        }
    ).named(renames["WorkItemServiceStateIn"])
    types["WorkItemServiceStateOut"] = t.struct(
        {
            "reportStatusInterval": t.string().optional(),
            "leaseExpireTime": t.string().optional(),
            "suggestedStopPosition": t.proxy(renames["PositionOut"]).optional(),
            "hotKeyDetection": t.proxy(renames["HotKeyDetectionOut"]).optional(),
            "metricShortId": t.array(t.proxy(renames["MetricShortIdOut"])).optional(),
            "harnessData": t.struct({"_": t.string().optional()}).optional(),
            "splitRequest": t.proxy(renames["ApproximateSplitRequestOut"]).optional(),
            "completeWorkStatus": t.proxy(renames["StatusOut"]).optional(),
            "nextReportIndex": t.string().optional(),
            "suggestedStopPoint": t.proxy(renames["ApproximateProgressOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkItemServiceStateOut"])
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
    types["WorkerSettingsIn"] = t.struct(
        {
            "baseUrl": t.string().optional(),
            "servicePath": t.string().optional(),
            "workerId": t.string().optional(),
            "shuffleServicePath": t.string().optional(),
            "reportingEnabled": t.boolean().optional(),
            "tempStoragePrefix": t.string().optional(),
        }
    ).named(renames["WorkerSettingsIn"])
    types["WorkerSettingsOut"] = t.struct(
        {
            "baseUrl": t.string().optional(),
            "servicePath": t.string().optional(),
            "workerId": t.string().optional(),
            "shuffleServicePath": t.string().optional(),
            "reportingEnabled": t.boolean().optional(),
            "tempStoragePrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerSettingsOut"])
    types["WorkerShutdownNoticeIn"] = t.struct({"reason": t.string().optional()}).named(
        renames["WorkerShutdownNoticeIn"]
    )
    types["WorkerShutdownNoticeOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerShutdownNoticeOut"])
    types["SeqMapTaskIn"] = t.struct(
        {
            "name": t.string().optional(),
            "inputs": t.array(t.proxy(renames["SideInputInfoIn"])).optional(),
            "systemName": t.string().optional(),
            "userFn": t.struct({"_": t.string().optional()}).optional(),
            "stageName": t.string().optional(),
            "outputInfos": t.array(
                t.proxy(renames["SeqMapTaskOutputInfoIn"])
            ).optional(),
        }
    ).named(renames["SeqMapTaskIn"])
    types["SeqMapTaskOut"] = t.struct(
        {
            "name": t.string().optional(),
            "inputs": t.array(t.proxy(renames["SideInputInfoOut"])).optional(),
            "systemName": t.string().optional(),
            "userFn": t.struct({"_": t.string().optional()}).optional(),
            "stageName": t.string().optional(),
            "outputInfos": t.array(
                t.proxy(renames["SeqMapTaskOutputInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SeqMapTaskOut"])
    types["JobIn"] = t.struct(
        {
            "clientRequestId": t.string().optional(),
            "pipelineDescription": t.proxy(renames["PipelineDescriptionIn"]).optional(),
            "currentStateTime": t.string().optional(),
            "steps": t.array(t.proxy(renames["StepIn"])).optional(),
            "createTime": t.string().optional(),
            "createdFromSnapshotId": t.string().optional(),
            "jobMetadata": t.proxy(renames["JobMetadataIn"]).optional(),
            "transformNameMapping": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "stepsLocation": t.string().optional(),
            "environment": t.proxy(renames["EnvironmentIn"]).optional(),
            "executionInfo": t.proxy(renames["JobExecutionInfoIn"]).optional(),
            "requestedState": t.string().optional(),
            "replacedByJobId": t.string().optional(),
            "replaceJobId": t.string().optional(),
            "tempFiles": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "stageStates": t.array(
                t.proxy(renames["ExecutionStageStateIn"])
            ).optional(),
            "projectId": t.string().optional(),
            "startTime": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "location": t.string().optional(),
            "runtimeUpdatableParams": t.proxy(
                renames["RuntimeUpdatableParamsIn"]
            ).optional(),
            "currentState": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "clientRequestId": t.string().optional(),
            "pipelineDescription": t.proxy(
                renames["PipelineDescriptionOut"]
            ).optional(),
            "currentStateTime": t.string().optional(),
            "steps": t.array(t.proxy(renames["StepOut"])).optional(),
            "createTime": t.string().optional(),
            "createdFromSnapshotId": t.string().optional(),
            "jobMetadata": t.proxy(renames["JobMetadataOut"]).optional(),
            "transformNameMapping": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "stepsLocation": t.string().optional(),
            "environment": t.proxy(renames["EnvironmentOut"]).optional(),
            "executionInfo": t.proxy(renames["JobExecutionInfoOut"]).optional(),
            "requestedState": t.string().optional(),
            "replacedByJobId": t.string().optional(),
            "replaceJobId": t.string().optional(),
            "tempFiles": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "stageStates": t.array(
                t.proxy(renames["ExecutionStageStateOut"])
            ).optional(),
            "projectId": t.string().optional(),
            "startTime": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "location": t.string().optional(),
            "runtimeUpdatableParams": t.proxy(
                renames["RuntimeUpdatableParamsOut"]
            ).optional(),
            "currentState": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
    types["HotKeyDetectionIn"] = t.struct(
        {
            "userStepName": t.string().optional(),
            "systemName": t.string().optional(),
            "hotKeyAge": t.string().optional(),
        }
    ).named(renames["HotKeyDetectionIn"])
    types["HotKeyDetectionOut"] = t.struct(
        {
            "userStepName": t.string().optional(),
            "systemName": t.string().optional(),
            "hotKeyAge": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HotKeyDetectionOut"])
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
    types["StragglerSummaryIn"] = t.struct(
        {
            "recentStragglers": t.array(t.proxy(renames["StragglerIn"])).optional(),
            "totalStragglerCount": t.string().optional(),
            "stragglerCauseCount": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["StragglerSummaryIn"])
    types["StragglerSummaryOut"] = t.struct(
        {
            "recentStragglers": t.array(t.proxy(renames["StragglerOut"])).optional(),
            "totalStragglerCount": t.string().optional(),
            "stragglerCauseCount": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StragglerSummaryOut"])
    types["JobMetadataIn"] = t.struct(
        {
            "spannerDetails": t.array(
                t.proxy(renames["SpannerIODetailsIn"])
            ).optional(),
            "sdkVersion": t.proxy(renames["SdkVersionIn"]).optional(),
            "datastoreDetails": t.array(
                t.proxy(renames["DatastoreIODetailsIn"])
            ).optional(),
            "userDisplayProperties": t.struct({"_": t.string().optional()}).optional(),
            "fileDetails": t.array(t.proxy(renames["FileIODetailsIn"])).optional(),
            "bigTableDetails": t.array(
                t.proxy(renames["BigTableIODetailsIn"])
            ).optional(),
            "pubsubDetails": t.array(t.proxy(renames["PubSubIODetailsIn"])).optional(),
            "bigqueryDetails": t.array(
                t.proxy(renames["BigQueryIODetailsIn"])
            ).optional(),
        }
    ).named(renames["JobMetadataIn"])
    types["JobMetadataOut"] = t.struct(
        {
            "spannerDetails": t.array(
                t.proxy(renames["SpannerIODetailsOut"])
            ).optional(),
            "sdkVersion": t.proxy(renames["SdkVersionOut"]).optional(),
            "datastoreDetails": t.array(
                t.proxy(renames["DatastoreIODetailsOut"])
            ).optional(),
            "userDisplayProperties": t.struct({"_": t.string().optional()}).optional(),
            "fileDetails": t.array(t.proxy(renames["FileIODetailsOut"])).optional(),
            "bigTableDetails": t.array(
                t.proxy(renames["BigTableIODetailsOut"])
            ).optional(),
            "pubsubDetails": t.array(t.proxy(renames["PubSubIODetailsOut"])).optional(),
            "bigqueryDetails": t.array(
                t.proxy(renames["BigQueryIODetailsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobMetadataOut"])
    types["ReadInstructionIn"] = t.struct(
        {"source": t.proxy(renames["SourceIn"]).optional()}
    ).named(renames["ReadInstructionIn"])
    types["ReadInstructionOut"] = t.struct(
        {
            "source": t.proxy(renames["SourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadInstructionOut"])
    types["DiskIn"] = t.struct(
        {
            "diskType": t.string().optional(),
            "mountPoint": t.string().optional(),
            "sizeGb": t.integer().optional(),
        }
    ).named(renames["DiskIn"])
    types["DiskOut"] = t.struct(
        {
            "diskType": t.string().optional(),
            "mountPoint": t.string().optional(),
            "sizeGb": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskOut"])
    types["PackageIn"] = t.struct(
        {"location": t.string().optional(), "name": t.string().optional()}
    ).named(renames["PackageIn"])
    types["PackageOut"] = t.struct(
        {
            "location": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageOut"])
    types["WorkerThreadScalingReportResponseIn"] = t.struct(
        {"recommendedThreadCount": t.integer().optional()}
    ).named(renames["WorkerThreadScalingReportResponseIn"])
    types["WorkerThreadScalingReportResponseOut"] = t.struct(
        {
            "recommendedThreadCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerThreadScalingReportResponseOut"])

    functions = {}
    functions["projectsWorkerMessages"] = dataflow.delete(
        "v1b3/projects/{projectId}/snapshots",
        t.struct(
            {
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "snapshotId": t.string().optional(),
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
                "projectId": t.string().optional(),
                "snapshotId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeleteSnapshotResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTemplatesLaunch"] = dataflow.get(
        "v1b3/projects/{projectId}/templates:get",
        t.struct(
            {
                "gcsPath": t.string(),
                "view": t.string().optional(),
                "projectId": t.string(),
                "location": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetTemplateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTemplatesCreate"] = dataflow.get(
        "v1b3/projects/{projectId}/templates:get",
        t.struct(
            {
                "gcsPath": t.string(),
                "view": t.string().optional(),
                "projectId": t.string(),
                "location": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetTemplateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTemplatesGet"] = dataflow.get(
        "v1b3/projects/{projectId}/templates:get",
        t.struct(
            {
                "gcsPath": t.string(),
                "view": t.string().optional(),
                "projectId": t.string(),
                "location": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetTemplateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnapshotsList"] = dataflow.get(
        "v1b3/projects/{projectId}/snapshots/{snapshotId}",
        t.struct(
            {
                "location": t.string().optional(),
                "snapshotId": t.string().optional(),
                "projectId": t.string().optional(),
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
                "location": t.string().optional(),
                "snapshotId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnapshotOut"]),
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
    functions["projectsLocationsTemplatesGet"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/templates:launch",
        t.struct(
            {
                "dynamicTemplate.stagingLocation": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "projectId": t.string(),
                "dynamicTemplate.gcsPath": t.string().optional(),
                "gcsPath": t.string().optional(),
                "location": t.string().optional(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "jobName": t.string(),
                "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
                "transformNameMapping": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "update": t.boolean().optional(),
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
                "dynamicTemplate.stagingLocation": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "projectId": t.string(),
                "dynamicTemplate.gcsPath": t.string().optional(),
                "gcsPath": t.string().optional(),
                "location": t.string().optional(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "jobName": t.string(),
                "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
                "transformNameMapping": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "update": t.boolean().optional(),
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
                "dynamicTemplate.stagingLocation": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "projectId": t.string(),
                "dynamicTemplate.gcsPath": t.string().optional(),
                "gcsPath": t.string().optional(),
                "location": t.string().optional(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "jobName": t.string(),
                "environment": t.proxy(renames["RuntimeEnvironmentIn"]).optional(),
                "transformNameMapping": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "update": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LaunchTemplateResponseOut"]),
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
    functions["projectsLocationsFlexTemplatesLaunch"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/flexTemplates:launch",
        t.struct(
            {
                "projectId": t.string(),
                "location": t.string(),
                "validateOnly": t.boolean().optional(),
                "launchParameter": t.proxy(renames["LaunchFlexTemplateParameterIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LaunchFlexTemplateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsSnapshot"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/jobs",
        t.struct(
            {
                "location": t.string().optional(),
                "replaceJobId": t.string().optional(),
                "view": t.string().optional(),
                "projectId": t.string().optional(),
                "clientRequestId": t.string().optional(),
                "pipelineDescription": t.proxy(
                    renames["PipelineDescriptionIn"]
                ).optional(),
                "currentStateTime": t.string().optional(),
                "steps": t.array(t.proxy(renames["StepIn"])).optional(),
                "createTime": t.string().optional(),
                "createdFromSnapshotId": t.string().optional(),
                "jobMetadata": t.proxy(renames["JobMetadataIn"]).optional(),
                "transformNameMapping": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "name": t.string().optional(),
                "type": t.string().optional(),
                "stepsLocation": t.string().optional(),
                "environment": t.proxy(renames["EnvironmentIn"]).optional(),
                "executionInfo": t.proxy(renames["JobExecutionInfoIn"]).optional(),
                "requestedState": t.string().optional(),
                "replacedByJobId": t.string().optional(),
                "tempFiles": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "stageStates": t.array(
                    t.proxy(renames["ExecutionStageStateIn"])
                ).optional(),
                "startTime": t.string().optional(),
                "satisfiesPzs": t.boolean().optional(),
                "runtimeUpdatableParams": t.proxy(
                    renames["RuntimeUpdatableParamsIn"]
                ).optional(),
                "currentState": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsGet"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/jobs",
        t.struct(
            {
                "location": t.string().optional(),
                "replaceJobId": t.string().optional(),
                "view": t.string().optional(),
                "projectId": t.string().optional(),
                "clientRequestId": t.string().optional(),
                "pipelineDescription": t.proxy(
                    renames["PipelineDescriptionIn"]
                ).optional(),
                "currentStateTime": t.string().optional(),
                "steps": t.array(t.proxy(renames["StepIn"])).optional(),
                "createTime": t.string().optional(),
                "createdFromSnapshotId": t.string().optional(),
                "jobMetadata": t.proxy(renames["JobMetadataIn"]).optional(),
                "transformNameMapping": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "name": t.string().optional(),
                "type": t.string().optional(),
                "stepsLocation": t.string().optional(),
                "environment": t.proxy(renames["EnvironmentIn"]).optional(),
                "executionInfo": t.proxy(renames["JobExecutionInfoIn"]).optional(),
                "requestedState": t.string().optional(),
                "replacedByJobId": t.string().optional(),
                "tempFiles": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "stageStates": t.array(
                    t.proxy(renames["ExecutionStageStateIn"])
                ).optional(),
                "startTime": t.string().optional(),
                "satisfiesPzs": t.boolean().optional(),
                "runtimeUpdatableParams": t.proxy(
                    renames["RuntimeUpdatableParamsIn"]
                ).optional(),
                "currentState": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsUpdate"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/jobs",
        t.struct(
            {
                "location": t.string().optional(),
                "replaceJobId": t.string().optional(),
                "view": t.string().optional(),
                "projectId": t.string().optional(),
                "clientRequestId": t.string().optional(),
                "pipelineDescription": t.proxy(
                    renames["PipelineDescriptionIn"]
                ).optional(),
                "currentStateTime": t.string().optional(),
                "steps": t.array(t.proxy(renames["StepIn"])).optional(),
                "createTime": t.string().optional(),
                "createdFromSnapshotId": t.string().optional(),
                "jobMetadata": t.proxy(renames["JobMetadataIn"]).optional(),
                "transformNameMapping": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "name": t.string().optional(),
                "type": t.string().optional(),
                "stepsLocation": t.string().optional(),
                "environment": t.proxy(renames["EnvironmentIn"]).optional(),
                "executionInfo": t.proxy(renames["JobExecutionInfoIn"]).optional(),
                "requestedState": t.string().optional(),
                "replacedByJobId": t.string().optional(),
                "tempFiles": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "stageStates": t.array(
                    t.proxy(renames["ExecutionStageStateIn"])
                ).optional(),
                "startTime": t.string().optional(),
                "satisfiesPzs": t.boolean().optional(),
                "runtimeUpdatableParams": t.proxy(
                    renames["RuntimeUpdatableParamsIn"]
                ).optional(),
                "currentState": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsList"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/jobs",
        t.struct(
            {
                "location": t.string().optional(),
                "replaceJobId": t.string().optional(),
                "view": t.string().optional(),
                "projectId": t.string().optional(),
                "clientRequestId": t.string().optional(),
                "pipelineDescription": t.proxy(
                    renames["PipelineDescriptionIn"]
                ).optional(),
                "currentStateTime": t.string().optional(),
                "steps": t.array(t.proxy(renames["StepIn"])).optional(),
                "createTime": t.string().optional(),
                "createdFromSnapshotId": t.string().optional(),
                "jobMetadata": t.proxy(renames["JobMetadataIn"]).optional(),
                "transformNameMapping": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "name": t.string().optional(),
                "type": t.string().optional(),
                "stepsLocation": t.string().optional(),
                "environment": t.proxy(renames["EnvironmentIn"]).optional(),
                "executionInfo": t.proxy(renames["JobExecutionInfoIn"]).optional(),
                "requestedState": t.string().optional(),
                "replacedByJobId": t.string().optional(),
                "tempFiles": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "stageStates": t.array(
                    t.proxy(renames["ExecutionStageStateIn"])
                ).optional(),
                "startTime": t.string().optional(),
                "satisfiesPzs": t.boolean().optional(),
                "runtimeUpdatableParams": t.proxy(
                    renames["RuntimeUpdatableParamsIn"]
                ).optional(),
                "currentState": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsGetMetrics"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/jobs",
        t.struct(
            {
                "location": t.string().optional(),
                "replaceJobId": t.string().optional(),
                "view": t.string().optional(),
                "projectId": t.string().optional(),
                "clientRequestId": t.string().optional(),
                "pipelineDescription": t.proxy(
                    renames["PipelineDescriptionIn"]
                ).optional(),
                "currentStateTime": t.string().optional(),
                "steps": t.array(t.proxy(renames["StepIn"])).optional(),
                "createTime": t.string().optional(),
                "createdFromSnapshotId": t.string().optional(),
                "jobMetadata": t.proxy(renames["JobMetadataIn"]).optional(),
                "transformNameMapping": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "name": t.string().optional(),
                "type": t.string().optional(),
                "stepsLocation": t.string().optional(),
                "environment": t.proxy(renames["EnvironmentIn"]).optional(),
                "executionInfo": t.proxy(renames["JobExecutionInfoIn"]).optional(),
                "requestedState": t.string().optional(),
                "replacedByJobId": t.string().optional(),
                "tempFiles": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "stageStates": t.array(
                    t.proxy(renames["ExecutionStageStateIn"])
                ).optional(),
                "startTime": t.string().optional(),
                "satisfiesPzs": t.boolean().optional(),
                "runtimeUpdatableParams": t.proxy(
                    renames["RuntimeUpdatableParamsIn"]
                ).optional(),
                "currentState": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsGetExecutionDetails"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/jobs",
        t.struct(
            {
                "location": t.string().optional(),
                "replaceJobId": t.string().optional(),
                "view": t.string().optional(),
                "projectId": t.string().optional(),
                "clientRequestId": t.string().optional(),
                "pipelineDescription": t.proxy(
                    renames["PipelineDescriptionIn"]
                ).optional(),
                "currentStateTime": t.string().optional(),
                "steps": t.array(t.proxy(renames["StepIn"])).optional(),
                "createTime": t.string().optional(),
                "createdFromSnapshotId": t.string().optional(),
                "jobMetadata": t.proxy(renames["JobMetadataIn"]).optional(),
                "transformNameMapping": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "name": t.string().optional(),
                "type": t.string().optional(),
                "stepsLocation": t.string().optional(),
                "environment": t.proxy(renames["EnvironmentIn"]).optional(),
                "executionInfo": t.proxy(renames["JobExecutionInfoIn"]).optional(),
                "requestedState": t.string().optional(),
                "replacedByJobId": t.string().optional(),
                "tempFiles": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "stageStates": t.array(
                    t.proxy(renames["ExecutionStageStateIn"])
                ).optional(),
                "startTime": t.string().optional(),
                "satisfiesPzs": t.boolean().optional(),
                "runtimeUpdatableParams": t.proxy(
                    renames["RuntimeUpdatableParamsIn"]
                ).optional(),
                "currentState": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsCreate"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/jobs",
        t.struct(
            {
                "location": t.string().optional(),
                "replaceJobId": t.string().optional(),
                "view": t.string().optional(),
                "projectId": t.string().optional(),
                "clientRequestId": t.string().optional(),
                "pipelineDescription": t.proxy(
                    renames["PipelineDescriptionIn"]
                ).optional(),
                "currentStateTime": t.string().optional(),
                "steps": t.array(t.proxy(renames["StepIn"])).optional(),
                "createTime": t.string().optional(),
                "createdFromSnapshotId": t.string().optional(),
                "jobMetadata": t.proxy(renames["JobMetadataIn"]).optional(),
                "transformNameMapping": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "name": t.string().optional(),
                "type": t.string().optional(),
                "stepsLocation": t.string().optional(),
                "environment": t.proxy(renames["EnvironmentIn"]).optional(),
                "executionInfo": t.proxy(renames["JobExecutionInfoIn"]).optional(),
                "requestedState": t.string().optional(),
                "replacedByJobId": t.string().optional(),
                "tempFiles": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "stageStates": t.array(
                    t.proxy(renames["ExecutionStageStateIn"])
                ).optional(),
                "startTime": t.string().optional(),
                "satisfiesPzs": t.boolean().optional(),
                "runtimeUpdatableParams": t.proxy(
                    renames["RuntimeUpdatableParamsIn"]
                ).optional(),
                "currentState": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsDebugGetConfig"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/debug/sendCapture",
        t.struct(
            {
                "projectId": t.string().optional(),
                "location": t.string().optional(),
                "jobId": t.string().optional(),
                "dataFormat": t.string().optional(),
                "workerId": t.string().optional(),
                "data": t.string().optional(),
                "componentId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SendDebugCaptureResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsDebugSendCapture"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/debug/sendCapture",
        t.struct(
            {
                "projectId": t.string().optional(),
                "location": t.string().optional(),
                "jobId": t.string().optional(),
                "dataFormat": t.string().optional(),
                "workerId": t.string().optional(),
                "data": t.string().optional(),
                "componentId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SendDebugCaptureResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsStagesGetExecutionDetails"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/stages/{stageId}/executionDetails",
        t.struct(
            {
                "location": t.string().optional(),
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "pageToken": t.string().optional(),
                "stageId": t.string().optional(),
                "startTime": t.string().optional(),
                "pageSize": t.integer().optional(),
                "endTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StageExecutionDetailsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsWorkItemsLease"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/workItems:reportStatus",
        t.struct(
            {
                "location": t.string().optional(),
                "jobId": t.string().optional(),
                "projectId": t.string().optional(),
                "unifiedWorkerRequest": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "currentWorkerTime": t.string().optional(),
                "workItemStatuses": t.array(
                    t.proxy(renames["WorkItemStatusIn"])
                ).optional(),
                "workerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportWorkItemStatusResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsWorkItemsReportStatus"] = dataflow.post(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/workItems:reportStatus",
        t.struct(
            {
                "location": t.string().optional(),
                "jobId": t.string().optional(),
                "projectId": t.string().optional(),
                "unifiedWorkerRequest": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "currentWorkerTime": t.string().optional(),
                "workItemStatuses": t.array(
                    t.proxy(renames["WorkItemStatusIn"])
                ).optional(),
                "workerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportWorkItemStatusResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsMessagesList"] = dataflow.get(
        "v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/messages",
        t.struct(
            {
                "endTime": t.string().optional(),
                "startTime": t.string().optional(),
                "minimumImportance": t.string().optional(),
                "pageSize": t.integer().optional(),
                "jobId": t.string().optional(),
                "projectId": t.string().optional(),
                "location": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobMessagesResponseOut"]),
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
    functions["projectsJobsGet"] = dataflow.get(
        "v1b3/projects/{projectId}/jobs",
        t.struct(
            {
                "location": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "filter": t.string().optional(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsCreate"] = dataflow.get(
        "v1b3/projects/{projectId}/jobs",
        t.struct(
            {
                "location": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "filter": t.string().optional(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsAggregated"] = dataflow.get(
        "v1b3/projects/{projectId}/jobs",
        t.struct(
            {
                "location": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "filter": t.string().optional(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsUpdate"] = dataflow.get(
        "v1b3/projects/{projectId}/jobs",
        t.struct(
            {
                "location": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "filter": t.string().optional(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsGetMetrics"] = dataflow.get(
        "v1b3/projects/{projectId}/jobs",
        t.struct(
            {
                "location": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "filter": t.string().optional(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsSnapshot"] = dataflow.get(
        "v1b3/projects/{projectId}/jobs",
        t.struct(
            {
                "location": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "filter": t.string().optional(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsList"] = dataflow.get(
        "v1b3/projects/{projectId}/jobs",
        t.struct(
            {
                "location": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "filter": t.string().optional(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobsWorkItemsLease"] = dataflow.post(
        "v1b3/projects/{projectId}/jobs/{jobId}/workItems:reportStatus",
        t.struct(
            {
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "unifiedWorkerRequest": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "location": t.string().optional(),
                "currentWorkerTime": t.string().optional(),
                "workItemStatuses": t.array(
                    t.proxy(renames["WorkItemStatusIn"])
                ).optional(),
                "workerId": t.string().optional(),
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
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "unifiedWorkerRequest": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "location": t.string().optional(),
                "currentWorkerTime": t.string().optional(),
                "workItemStatuses": t.array(
                    t.proxy(renames["WorkItemStatusIn"])
                ).optional(),
                "workerId": t.string().optional(),
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
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "componentId": t.string().optional(),
                "location": t.string().optional(),
                "workerId": t.string().optional(),
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
                "projectId": t.string().optional(),
                "jobId": t.string().optional(),
                "componentId": t.string().optional(),
                "location": t.string().optional(),
                "workerId": t.string().optional(),
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
                "startTime": t.string().optional(),
                "jobId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "location": t.string().optional(),
                "endTime": t.string().optional(),
                "projectId": t.string().optional(),
                "minimumImportance": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobMessagesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="dataflow", renames=renames, types=Box(types), functions=Box(functions)
    )
