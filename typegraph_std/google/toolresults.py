from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_toolresults():
    toolresults = HTTPRuntime("https://toolresults.googleapis.com/")

    renames = {
        "ErrorResponse": "_toolresults_1_ErrorResponse",
        "IosTestIn": "_toolresults_2_IosTestIn",
        "IosTestOut": "_toolresults_3_IosTestOut",
        "RegionProtoIn": "_toolresults_4_RegionProtoIn",
        "RegionProtoOut": "_toolresults_5_RegionProtoOut",
        "SpecificationIn": "_toolresults_6_SpecificationIn",
        "SpecificationOut": "_toolresults_7_SpecificationOut",
        "PerfEnvironmentIn": "_toolresults_8_PerfEnvironmentIn",
        "PerfEnvironmentOut": "_toolresults_9_PerfEnvironmentOut",
        "TestTimingIn": "_toolresults_10_TestTimingIn",
        "TestTimingOut": "_toolresults_11_TestTimingOut",
        "ShardSummaryIn": "_toolresults_12_ShardSummaryIn",
        "ShardSummaryOut": "_toolresults_13_ShardSummaryOut",
        "ToolExecutionIn": "_toolresults_14_ToolExecutionIn",
        "ToolExecutionOut": "_toolresults_15_ToolExecutionOut",
        "SkippedDetailIn": "_toolresults_16_SkippedDetailIn",
        "SkippedDetailOut": "_toolresults_17_SkippedDetailOut",
        "UIElementTooDeepIn": "_toolresults_18_UIElementTooDeepIn",
        "UIElementTooDeepOut": "_toolresults_19_UIElementTooDeepOut",
        "AndroidRoboTestIn": "_toolresults_20_AndroidRoboTestIn",
        "AndroidRoboTestOut": "_toolresults_21_AndroidRoboTestOut",
        "InconclusiveDetailIn": "_toolresults_22_InconclusiveDetailIn",
        "InconclusiveDetailOut": "_toolresults_23_InconclusiveDetailOut",
        "FileReferenceIn": "_toolresults_24_FileReferenceIn",
        "FileReferenceOut": "_toolresults_25_FileReferenceOut",
        "DurationIn": "_toolresults_26_DurationIn",
        "DurationOut": "_toolresults_27_DurationOut",
        "PerformedGoogleLoginIn": "_toolresults_28_PerformedGoogleLoginIn",
        "PerformedGoogleLoginOut": "_toolresults_29_PerformedGoogleLoginOut",
        "PerformedMonkeyActionsIn": "_toolresults_30_PerformedMonkeyActionsIn",
        "PerformedMonkeyActionsOut": "_toolresults_31_PerformedMonkeyActionsOut",
        "StepLabelsEntryIn": "_toolresults_32_StepLabelsEntryIn",
        "StepLabelsEntryOut": "_toolresults_33_StepLabelsEntryOut",
        "AvailableDeepLinksIn": "_toolresults_34_AvailableDeepLinksIn",
        "AvailableDeepLinksOut": "_toolresults_35_AvailableDeepLinksOut",
        "ListScreenshotClustersResponseIn": "_toolresults_36_ListScreenshotClustersResponseIn",
        "ListScreenshotClustersResponseOut": "_toolresults_37_ListScreenshotClustersResponseOut",
        "IosRoboTestIn": "_toolresults_38_IosRoboTestIn",
        "IosRoboTestOut": "_toolresults_39_IosRoboTestOut",
        "PendingGoogleUpdateInsightIn": "_toolresults_40_PendingGoogleUpdateInsightIn",
        "PendingGoogleUpdateInsightOut": "_toolresults_41_PendingGoogleUpdateInsightOut",
        "StepSummaryIn": "_toolresults_42_StepSummaryIn",
        "StepSummaryOut": "_toolresults_43_StepSummaryOut",
        "UpgradeInsightIn": "_toolresults_44_UpgradeInsightIn",
        "UpgradeInsightOut": "_toolresults_45_UpgradeInsightOut",
        "ToolExitCodeIn": "_toolresults_46_ToolExitCodeIn",
        "ToolExitCodeOut": "_toolresults_47_ToolExitCodeOut",
        "ANRIn": "_toolresults_48_ANRIn",
        "ANROut": "_toolresults_49_ANROut",
        "ScreenIn": "_toolresults_50_ScreenIn",
        "ScreenOut": "_toolresults_51_ScreenOut",
        "AnyIn": "_toolresults_52_AnyIn",
        "AnyOut": "_toolresults_53_AnyOut",
        "StepDimensionValueEntryIn": "_toolresults_54_StepDimensionValueEntryIn",
        "StepDimensionValueEntryOut": "_toolresults_55_StepDimensionValueEntryOut",
        "DeviceOutOfMemoryIn": "_toolresults_56_DeviceOutOfMemoryIn",
        "DeviceOutOfMemoryOut": "_toolresults_57_DeviceOutOfMemoryOut",
        "AndroidInstrumentationTestIn": "_toolresults_58_AndroidInstrumentationTestIn",
        "AndroidInstrumentationTestOut": "_toolresults_59_AndroidInstrumentationTestOut",
        "ToolOutputReferenceIn": "_toolresults_60_ToolOutputReferenceIn",
        "ToolOutputReferenceOut": "_toolresults_61_ToolOutputReferenceOut",
        "ListEnvironmentsResponseIn": "_toolresults_62_ListEnvironmentsResponseIn",
        "ListEnvironmentsResponseOut": "_toolresults_63_ListEnvironmentsResponseOut",
        "ListPerfSampleSeriesResponseIn": "_toolresults_64_ListPerfSampleSeriesResponseIn",
        "ListPerfSampleSeriesResponseOut": "_toolresults_65_ListPerfSampleSeriesResponseOut",
        "EncounteredLoginScreenIn": "_toolresults_66_EncounteredLoginScreenIn",
        "EncounteredLoginScreenOut": "_toolresults_67_EncounteredLoginScreenOut",
        "DetectedAppSplashScreenIn": "_toolresults_68_DetectedAppSplashScreenIn",
        "DetectedAppSplashScreenOut": "_toolresults_69_DetectedAppSplashScreenOut",
        "PerfSampleIn": "_toolresults_70_PerfSampleIn",
        "PerfSampleOut": "_toolresults_71_PerfSampleOut",
        "StepIn": "_toolresults_72_StepIn",
        "StepOut": "_toolresults_73_StepOut",
        "ProjectSettingsIn": "_toolresults_74_ProjectSettingsIn",
        "ProjectSettingsOut": "_toolresults_75_ProjectSettingsOut",
        "ListStepThumbnailsResponseIn": "_toolresults_76_ListStepThumbnailsResponseIn",
        "ListStepThumbnailsResponseOut": "_toolresults_77_ListStepThumbnailsResponseOut",
        "TestCaseReferenceIn": "_toolresults_78_TestCaseReferenceIn",
        "TestCaseReferenceOut": "_toolresults_79_TestCaseReferenceOut",
        "StackTraceIn": "_toolresults_80_StackTraceIn",
        "StackTraceOut": "_toolresults_81_StackTraceOut",
        "FailedToInstallIn": "_toolresults_82_FailedToInstallIn",
        "FailedToInstallOut": "_toolresults_83_FailedToInstallOut",
        "RoboScriptExecutionIn": "_toolresults_84_RoboScriptExecutionIn",
        "RoboScriptExecutionOut": "_toolresults_85_RoboScriptExecutionOut",
        "MultiStepIn": "_toolresults_86_MultiStepIn",
        "MultiStepOut": "_toolresults_87_MultiStepOut",
        "MemoryInfoIn": "_toolresults_88_MemoryInfoIn",
        "MemoryInfoOut": "_toolresults_89_MemoryInfoOut",
        "UsedRoboDirectiveIn": "_toolresults_90_UsedRoboDirectiveIn",
        "UsedRoboDirectiveOut": "_toolresults_91_UsedRoboDirectiveOut",
        "IosTestLoopIn": "_toolresults_92_IosTestLoopIn",
        "IosTestLoopOut": "_toolresults_93_IosTestLoopOut",
        "NonSdkApiUsageViolationIn": "_toolresults_94_NonSdkApiUsageViolationIn",
        "NonSdkApiUsageViolationOut": "_toolresults_95_NonSdkApiUsageViolationOut",
        "InsufficientCoverageIn": "_toolresults_96_InsufficientCoverageIn",
        "InsufficientCoverageOut": "_toolresults_97_InsufficientCoverageOut",
        "UsedRoboIgnoreDirectiveIn": "_toolresults_98_UsedRoboIgnoreDirectiveIn",
        "UsedRoboIgnoreDirectiveOut": "_toolresults_99_UsedRoboIgnoreDirectiveOut",
        "ThumbnailIn": "_toolresults_100_ThumbnailIn",
        "ThumbnailOut": "_toolresults_101_ThumbnailOut",
        "AndroidTestLoopIn": "_toolresults_102_AndroidTestLoopIn",
        "AndroidTestLoopOut": "_toolresults_103_AndroidTestLoopOut",
        "BasicPerfSampleSeriesIn": "_toolresults_104_BasicPerfSampleSeriesIn",
        "BasicPerfSampleSeriesOut": "_toolresults_105_BasicPerfSampleSeriesOut",
        "EncounteredNonAndroidUiWidgetScreenIn": "_toolresults_106_EncounteredNonAndroidUiWidgetScreenIn",
        "EncounteredNonAndroidUiWidgetScreenOut": "_toolresults_107_EncounteredNonAndroidUiWidgetScreenOut",
        "ListExecutionsResponseIn": "_toolresults_108_ListExecutionsResponseIn",
        "ListExecutionsResponseOut": "_toolresults_109_ListExecutionsResponseOut",
        "TestSuiteOverviewIn": "_toolresults_110_TestSuiteOverviewIn",
        "TestSuiteOverviewOut": "_toolresults_111_TestSuiteOverviewOut",
        "ImageIn": "_toolresults_112_ImageIn",
        "ImageOut": "_toolresults_113_ImageOut",
        "SuggestionProtoIn": "_toolresults_114_SuggestionProtoIn",
        "SuggestionProtoOut": "_toolresults_115_SuggestionProtoOut",
        "EnvironmentIn": "_toolresults_116_EnvironmentIn",
        "EnvironmentOut": "_toolresults_117_EnvironmentOut",
        "PerfSampleSeriesIn": "_toolresults_118_PerfSampleSeriesIn",
        "PerfSampleSeriesOut": "_toolresults_119_PerfSampleSeriesOut",
        "FatalExceptionIn": "_toolresults_120_FatalExceptionIn",
        "FatalExceptionOut": "_toolresults_121_FatalExceptionOut",
        "OverlappingUIElementsIn": "_toolresults_122_OverlappingUIElementsIn",
        "OverlappingUIElementsOut": "_toolresults_123_OverlappingUIElementsOut",
        "BatchCreatePerfSamplesRequestIn": "_toolresults_124_BatchCreatePerfSamplesRequestIn",
        "BatchCreatePerfSamplesRequestOut": "_toolresults_125_BatchCreatePerfSamplesRequestOut",
        "NonSdkApiUsageViolationReportIn": "_toolresults_126_NonSdkApiUsageViolationReportIn",
        "NonSdkApiUsageViolationReportOut": "_toolresults_127_NonSdkApiUsageViolationReportOut",
        "ListStepAccessibilityClustersResponseIn": "_toolresults_128_ListStepAccessibilityClustersResponseIn",
        "ListStepAccessibilityClustersResponseOut": "_toolresults_129_ListStepAccessibilityClustersResponseOut",
        "BatchCreatePerfSamplesResponseIn": "_toolresults_130_BatchCreatePerfSamplesResponseIn",
        "BatchCreatePerfSamplesResponseOut": "_toolresults_131_BatchCreatePerfSamplesResponseOut",
        "InAppPurchasesFoundIn": "_toolresults_132_InAppPurchasesFoundIn",
        "InAppPurchasesFoundOut": "_toolresults_133_InAppPurchasesFoundOut",
        "SafeHtmlProtoIn": "_toolresults_134_SafeHtmlProtoIn",
        "SafeHtmlProtoOut": "_toolresults_135_SafeHtmlProtoOut",
        "IndividualOutcomeIn": "_toolresults_136_IndividualOutcomeIn",
        "IndividualOutcomeOut": "_toolresults_137_IndividualOutcomeOut",
        "HistoryIn": "_toolresults_138_HistoryIn",
        "HistoryOut": "_toolresults_139_HistoryOut",
        "TestCaseIn": "_toolresults_140_TestCaseIn",
        "TestCaseOut": "_toolresults_141_TestCaseOut",
        "MergedResultIn": "_toolresults_142_MergedResultIn",
        "MergedResultOut": "_toolresults_143_MergedResultOut",
        "CPUInfoIn": "_toolresults_144_CPUInfoIn",
        "CPUInfoOut": "_toolresults_145_CPUInfoOut",
        "ListPerfSamplesResponseIn": "_toolresults_146_ListPerfSamplesResponseIn",
        "ListPerfSamplesResponseOut": "_toolresults_147_ListPerfSamplesResponseOut",
        "IosAppCrashedIn": "_toolresults_148_IosAppCrashedIn",
        "IosAppCrashedOut": "_toolresults_149_IosAppCrashedOut",
        "IosAppInfoIn": "_toolresults_150_IosAppInfoIn",
        "IosAppInfoOut": "_toolresults_151_IosAppInfoOut",
        "OutcomeIn": "_toolresults_152_OutcomeIn",
        "OutcomeOut": "_toolresults_153_OutcomeOut",
        "PerfMetricsSummaryIn": "_toolresults_154_PerfMetricsSummaryIn",
        "PerfMetricsSummaryOut": "_toolresults_155_PerfMetricsSummaryOut",
        "ScreenshotClusterIn": "_toolresults_156_ScreenshotClusterIn",
        "ScreenshotClusterOut": "_toolresults_157_ScreenshotClusterOut",
        "ResultsStorageIn": "_toolresults_158_ResultsStorageIn",
        "ResultsStorageOut": "_toolresults_159_ResultsStorageOut",
        "LogcatCollectionErrorIn": "_toolresults_160_LogcatCollectionErrorIn",
        "LogcatCollectionErrorOut": "_toolresults_161_LogcatCollectionErrorOut",
        "CrashDialogErrorIn": "_toolresults_162_CrashDialogErrorIn",
        "CrashDialogErrorOut": "_toolresults_163_CrashDialogErrorOut",
        "StartActivityNotFoundIn": "_toolresults_164_StartActivityNotFoundIn",
        "StartActivityNotFoundOut": "_toolresults_165_StartActivityNotFoundOut",
        "NonSdkApiIn": "_toolresults_166_NonSdkApiIn",
        "NonSdkApiOut": "_toolresults_167_NonSdkApiOut",
        "SuccessDetailIn": "_toolresults_168_SuccessDetailIn",
        "SuccessDetailOut": "_toolresults_169_SuccessDetailOut",
        "ListHistoriesResponseIn": "_toolresults_170_ListHistoriesResponseIn",
        "ListHistoriesResponseOut": "_toolresults_171_ListHistoriesResponseOut",
        "UnusedRoboDirectiveIn": "_toolresults_172_UnusedRoboDirectiveIn",
        "UnusedRoboDirectiveOut": "_toolresults_173_UnusedRoboDirectiveOut",
        "GraphicsStatsBucketIn": "_toolresults_174_GraphicsStatsBucketIn",
        "GraphicsStatsBucketOut": "_toolresults_175_GraphicsStatsBucketOut",
        "TestExecutionStepIn": "_toolresults_176_TestExecutionStepIn",
        "TestExecutionStepOut": "_toolresults_177_TestExecutionStepOut",
        "ToolExecutionStepIn": "_toolresults_178_ToolExecutionStepIn",
        "ToolExecutionStepOut": "_toolresults_179_ToolExecutionStepOut",
        "LauncherActivityNotFoundIn": "_toolresults_180_LauncherActivityNotFoundIn",
        "LauncherActivityNotFoundOut": "_toolresults_181_LauncherActivityNotFoundOut",
        "TestIssueIn": "_toolresults_182_TestIssueIn",
        "TestIssueOut": "_toolresults_183_TestIssueOut",
        "BlankScreenIn": "_toolresults_184_BlankScreenIn",
        "BlankScreenOut": "_toolresults_185_BlankScreenOut",
        "NativeCrashIn": "_toolresults_186_NativeCrashIn",
        "NativeCrashOut": "_toolresults_187_NativeCrashOut",
        "ListTestCasesResponseIn": "_toolresults_188_ListTestCasesResponseIn",
        "ListTestCasesResponseOut": "_toolresults_189_ListTestCasesResponseOut",
        "MatrixDimensionDefinitionIn": "_toolresults_190_MatrixDimensionDefinitionIn",
        "MatrixDimensionDefinitionOut": "_toolresults_191_MatrixDimensionDefinitionOut",
        "AndroidAppInfoIn": "_toolresults_192_AndroidAppInfoIn",
        "AndroidAppInfoOut": "_toolresults_193_AndroidAppInfoOut",
        "IosXcTestIn": "_toolresults_194_IosXcTestIn",
        "IosXcTestOut": "_toolresults_195_IosXcTestOut",
        "FailureDetailIn": "_toolresults_196_FailureDetailIn",
        "FailureDetailOut": "_toolresults_197_FailureDetailOut",
        "StatusIn": "_toolresults_198_StatusIn",
        "StatusOut": "_toolresults_199_StatusOut",
        "AndroidTestIn": "_toolresults_200_AndroidTestIn",
        "AndroidTestOut": "_toolresults_201_AndroidTestOut",
        "PublishXunitXmlFilesRequestIn": "_toolresults_202_PublishXunitXmlFilesRequestIn",
        "PublishXunitXmlFilesRequestOut": "_toolresults_203_PublishXunitXmlFilesRequestOut",
        "SuggestionClusterProtoIn": "_toolresults_204_SuggestionClusterProtoIn",
        "SuggestionClusterProtoOut": "_toolresults_205_SuggestionClusterProtoOut",
        "UnspecifiedWarningIn": "_toolresults_206_UnspecifiedWarningIn",
        "UnspecifiedWarningOut": "_toolresults_207_UnspecifiedWarningOut",
        "ExecutionIn": "_toolresults_208_ExecutionIn",
        "ExecutionOut": "_toolresults_209_ExecutionOut",
        "PrimaryStepIn": "_toolresults_210_PrimaryStepIn",
        "PrimaryStepOut": "_toolresults_211_PrimaryStepOut",
        "NonSdkApiInsightIn": "_toolresults_212_NonSdkApiInsightIn",
        "NonSdkApiInsightOut": "_toolresults_213_NonSdkApiInsightOut",
        "TimestampIn": "_toolresults_214_TimestampIn",
        "TimestampOut": "_toolresults_215_TimestampOut",
        "ListStepsResponseIn": "_toolresults_216_ListStepsResponseIn",
        "ListStepsResponseOut": "_toolresults_217_ListStepsResponseOut",
        "EnvironmentDimensionValueEntryIn": "_toolresults_218_EnvironmentDimensionValueEntryIn",
        "EnvironmentDimensionValueEntryOut": "_toolresults_219_EnvironmentDimensionValueEntryOut",
        "GraphicsStatsIn": "_toolresults_220_GraphicsStatsIn",
        "GraphicsStatsOut": "_toolresults_221_GraphicsStatsOut",
        "AppStartTimeIn": "_toolresults_222_AppStartTimeIn",
        "AppStartTimeOut": "_toolresults_223_AppStartTimeOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["IosTestIn"] = t.struct(
        {
            "iosRoboTest": t.proxy(renames["IosRoboTestIn"]).optional(),
            "iosTestLoop": t.proxy(renames["IosTestLoopIn"]).optional(),
            "iosXcTest": t.proxy(renames["IosXcTestIn"]).optional(),
            "testTimeout": t.proxy(renames["DurationIn"]).optional(),
            "iosAppInfo": t.proxy(renames["IosAppInfoIn"]).optional(),
        }
    ).named(renames["IosTestIn"])
    types["IosTestOut"] = t.struct(
        {
            "iosRoboTest": t.proxy(renames["IosRoboTestOut"]).optional(),
            "iosTestLoop": t.proxy(renames["IosTestLoopOut"]).optional(),
            "iosXcTest": t.proxy(renames["IosXcTestOut"]).optional(),
            "testTimeout": t.proxy(renames["DurationOut"]).optional(),
            "iosAppInfo": t.proxy(renames["IosAppInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosTestOut"])
    types["RegionProtoIn"] = t.struct(
        {
            "leftPx": t.integer().optional(),
            "topPx": t.integer().optional(),
            "widthPx": t.integer().optional(),
            "heightPx": t.integer().optional(),
        }
    ).named(renames["RegionProtoIn"])
    types["RegionProtoOut"] = t.struct(
        {
            "leftPx": t.integer().optional(),
            "topPx": t.integer().optional(),
            "widthPx": t.integer().optional(),
            "heightPx": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionProtoOut"])
    types["SpecificationIn"] = t.struct(
        {
            "iosTest": t.proxy(renames["IosTestIn"]).optional(),
            "androidTest": t.proxy(renames["AndroidTestIn"]).optional(),
        }
    ).named(renames["SpecificationIn"])
    types["SpecificationOut"] = t.struct(
        {
            "iosTest": t.proxy(renames["IosTestOut"]).optional(),
            "androidTest": t.proxy(renames["AndroidTestOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpecificationOut"])
    types["PerfEnvironmentIn"] = t.struct(
        {
            "memoryInfo": t.proxy(renames["MemoryInfoIn"]).optional(),
            "cpuInfo": t.proxy(renames["CPUInfoIn"]).optional(),
        }
    ).named(renames["PerfEnvironmentIn"])
    types["PerfEnvironmentOut"] = t.struct(
        {
            "memoryInfo": t.proxy(renames["MemoryInfoOut"]).optional(),
            "cpuInfo": t.proxy(renames["CPUInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerfEnvironmentOut"])
    types["TestTimingIn"] = t.struct(
        {"testProcessDuration": t.proxy(renames["DurationIn"]).optional()}
    ).named(renames["TestTimingIn"])
    types["TestTimingOut"] = t.struct(
        {
            "testProcessDuration": t.proxy(renames["DurationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestTimingOut"])
    types["ShardSummaryIn"] = t.struct(
        {
            "runs": t.array(t.proxy(renames["StepSummaryIn"])).optional(),
            "shardResult": t.proxy(renames["MergedResultIn"]).optional(),
        }
    ).named(renames["ShardSummaryIn"])
    types["ShardSummaryOut"] = t.struct(
        {
            "runs": t.array(t.proxy(renames["StepSummaryOut"])).optional(),
            "shardResult": t.proxy(renames["MergedResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShardSummaryOut"])
    types["ToolExecutionIn"] = t.struct(
        {
            "commandLineArguments": t.array(t.string()).optional(),
            "exitCode": t.proxy(renames["ToolExitCodeIn"]).optional(),
            "toolOutputs": t.array(
                t.proxy(renames["ToolOutputReferenceIn"])
            ).optional(),
            "toolLogs": t.array(t.proxy(renames["FileReferenceIn"])).optional(),
        }
    ).named(renames["ToolExecutionIn"])
    types["ToolExecutionOut"] = t.struct(
        {
            "commandLineArguments": t.array(t.string()).optional(),
            "exitCode": t.proxy(renames["ToolExitCodeOut"]).optional(),
            "toolOutputs": t.array(
                t.proxy(renames["ToolOutputReferenceOut"])
            ).optional(),
            "toolLogs": t.array(t.proxy(renames["FileReferenceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ToolExecutionOut"])
    types["SkippedDetailIn"] = t.struct(
        {
            "incompatibleArchitecture": t.boolean().optional(),
            "incompatibleAppVersion": t.boolean().optional(),
            "incompatibleDevice": t.boolean().optional(),
        }
    ).named(renames["SkippedDetailIn"])
    types["SkippedDetailOut"] = t.struct(
        {
            "incompatibleArchitecture": t.boolean().optional(),
            "incompatibleAppVersion": t.boolean().optional(),
            "incompatibleDevice": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SkippedDetailOut"])
    types["UIElementTooDeepIn"] = t.struct(
        {
            "depth": t.integer().optional(),
            "screenId": t.string().optional(),
            "screenStateId": t.string().optional(),
        }
    ).named(renames["UIElementTooDeepIn"])
    types["UIElementTooDeepOut"] = t.struct(
        {
            "depth": t.integer().optional(),
            "screenId": t.string().optional(),
            "screenStateId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UIElementTooDeepOut"])
    types["AndroidRoboTestIn"] = t.struct(
        {
            "appInitialActivity": t.string().optional(),
            "bootstrapPackageId": t.string().optional(),
            "bootstrapRunnerClass": t.string().optional(),
            "maxDepth": t.integer().optional(),
            "maxSteps": t.integer().optional(),
        }
    ).named(renames["AndroidRoboTestIn"])
    types["AndroidRoboTestOut"] = t.struct(
        {
            "appInitialActivity": t.string().optional(),
            "bootstrapPackageId": t.string().optional(),
            "bootstrapRunnerClass": t.string().optional(),
            "maxDepth": t.integer().optional(),
            "maxSteps": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidRoboTestOut"])
    types["InconclusiveDetailIn"] = t.struct(
        {
            "hasErrorLogs": t.boolean().optional(),
            "abortedByUser": t.boolean().optional(),
            "infrastructureFailure": t.boolean().optional(),
        }
    ).named(renames["InconclusiveDetailIn"])
    types["InconclusiveDetailOut"] = t.struct(
        {
            "hasErrorLogs": t.boolean().optional(),
            "abortedByUser": t.boolean().optional(),
            "infrastructureFailure": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InconclusiveDetailOut"])
    types["FileReferenceIn"] = t.struct({"fileUri": t.string().optional()}).named(
        renames["FileReferenceIn"]
    )
    types["FileReferenceOut"] = t.struct(
        {
            "fileUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileReferenceOut"])
    types["DurationIn"] = t.struct(
        {"seconds": t.string().optional(), "nanos": t.integer().optional()}
    ).named(renames["DurationIn"])
    types["DurationOut"] = t.struct(
        {
            "seconds": t.string().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DurationOut"])
    types["PerformedGoogleLoginIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PerformedGoogleLoginIn"]
    )
    types["PerformedGoogleLoginOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PerformedGoogleLoginOut"])
    types["PerformedMonkeyActionsIn"] = t.struct(
        {"totalActions": t.integer().optional()}
    ).named(renames["PerformedMonkeyActionsIn"])
    types["PerformedMonkeyActionsOut"] = t.struct(
        {
            "totalActions": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerformedMonkeyActionsOut"])
    types["StepLabelsEntryIn"] = t.struct(
        {"value": t.string(), "key": t.string()}
    ).named(renames["StepLabelsEntryIn"])
    types["StepLabelsEntryOut"] = t.struct(
        {
            "value": t.string(),
            "key": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StepLabelsEntryOut"])
    types["AvailableDeepLinksIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AvailableDeepLinksIn"]
    )
    types["AvailableDeepLinksOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AvailableDeepLinksOut"])
    types["ListScreenshotClustersResponseIn"] = t.struct(
        {"clusters": t.array(t.proxy(renames["ScreenshotClusterIn"])).optional()}
    ).named(renames["ListScreenshotClustersResponseIn"])
    types["ListScreenshotClustersResponseOut"] = t.struct(
        {
            "clusters": t.array(t.proxy(renames["ScreenshotClusterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListScreenshotClustersResponseOut"])
    types["IosRoboTestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["IosRoboTestIn"]
    )
    types["IosRoboTestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["IosRoboTestOut"])
    types["PendingGoogleUpdateInsightIn"] = t.struct(
        {"nameOfGoogleLibrary": t.string().optional()}
    ).named(renames["PendingGoogleUpdateInsightIn"])
    types["PendingGoogleUpdateInsightOut"] = t.struct(
        {
            "nameOfGoogleLibrary": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PendingGoogleUpdateInsightOut"])
    types["StepSummaryIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StepSummaryIn"]
    )
    types["StepSummaryOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StepSummaryOut"])
    types["UpgradeInsightIn"] = t.struct(
        {
            "packageName": t.string().optional(),
            "upgradeToVersion": t.string().optional(),
        }
    ).named(renames["UpgradeInsightIn"])
    types["UpgradeInsightOut"] = t.struct(
        {
            "packageName": t.string().optional(),
            "upgradeToVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeInsightOut"])
    types["ToolExitCodeIn"] = t.struct({"number": t.integer().optional()}).named(
        renames["ToolExitCodeIn"]
    )
    types["ToolExitCodeOut"] = t.struct(
        {
            "number": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ToolExitCodeOut"])
    types["ANRIn"] = t.struct(
        {"stackTrace": t.proxy(renames["StackTraceIn"]).optional()}
    ).named(renames["ANRIn"])
    types["ANROut"] = t.struct(
        {
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ANROut"])
    types["ScreenIn"] = t.struct(
        {
            "fileReference": t.string().optional(),
            "version": t.string().optional(),
            "locale": t.string().optional(),
            "model": t.string().optional(),
        }
    ).named(renames["ScreenIn"])
    types["ScreenOut"] = t.struct(
        {
            "fileReference": t.string().optional(),
            "version": t.string().optional(),
            "locale": t.string().optional(),
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScreenOut"])
    types["AnyIn"] = t.struct(
        {"typeUrl": t.string().optional(), "value": t.string().optional()}
    ).named(renames["AnyIn"])
    types["AnyOut"] = t.struct(
        {
            "typeUrl": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnyOut"])
    types["StepDimensionValueEntryIn"] = t.struct(
        {"key": t.string(), "value": t.string()}
    ).named(renames["StepDimensionValueEntryIn"])
    types["StepDimensionValueEntryOut"] = t.struct(
        {
            "key": t.string(),
            "value": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StepDimensionValueEntryOut"])
    types["DeviceOutOfMemoryIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeviceOutOfMemoryIn"]
    )
    types["DeviceOutOfMemoryOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeviceOutOfMemoryOut"])
    types["AndroidInstrumentationTestIn"] = t.struct(
        {
            "testTargets": t.array(t.string()).optional(),
            "testPackageId": t.string().optional(),
            "useOrchestrator": t.boolean().optional(),
            "testRunnerClass": t.string().optional(),
        }
    ).named(renames["AndroidInstrumentationTestIn"])
    types["AndroidInstrumentationTestOut"] = t.struct(
        {
            "testTargets": t.array(t.string()).optional(),
            "testPackageId": t.string().optional(),
            "useOrchestrator": t.boolean().optional(),
            "testRunnerClass": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidInstrumentationTestOut"])
    types["ToolOutputReferenceIn"] = t.struct(
        {
            "creationTime": t.proxy(renames["TimestampIn"]).optional(),
            "output": t.proxy(renames["FileReferenceIn"]).optional(),
            "testCase": t.proxy(renames["TestCaseReferenceIn"]).optional(),
        }
    ).named(renames["ToolOutputReferenceIn"])
    types["ToolOutputReferenceOut"] = t.struct(
        {
            "creationTime": t.proxy(renames["TimestampOut"]).optional(),
            "output": t.proxy(renames["FileReferenceOut"]).optional(),
            "testCase": t.proxy(renames["TestCaseReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ToolOutputReferenceOut"])
    types["ListEnvironmentsResponseIn"] = t.struct(
        {
            "historyId": t.string().optional(),
            "executionId": t.string().optional(),
            "projectId": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "environments": t.array(t.proxy(renames["EnvironmentIn"])).optional(),
        }
    ).named(renames["ListEnvironmentsResponseIn"])
    types["ListEnvironmentsResponseOut"] = t.struct(
        {
            "historyId": t.string().optional(),
            "executionId": t.string().optional(),
            "projectId": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "environments": t.array(t.proxy(renames["EnvironmentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEnvironmentsResponseOut"])
    types["ListPerfSampleSeriesResponseIn"] = t.struct(
        {"perfSampleSeries": t.array(t.proxy(renames["PerfSampleSeriesIn"])).optional()}
    ).named(renames["ListPerfSampleSeriesResponseIn"])
    types["ListPerfSampleSeriesResponseOut"] = t.struct(
        {
            "perfSampleSeries": t.array(
                t.proxy(renames["PerfSampleSeriesOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPerfSampleSeriesResponseOut"])
    types["EncounteredLoginScreenIn"] = t.struct(
        {
            "distinctScreens": t.integer().optional(),
            "screenIds": t.array(t.string()).optional(),
        }
    ).named(renames["EncounteredLoginScreenIn"])
    types["EncounteredLoginScreenOut"] = t.struct(
        {
            "distinctScreens": t.integer().optional(),
            "screenIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncounteredLoginScreenOut"])
    types["DetectedAppSplashScreenIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DetectedAppSplashScreenIn"]
    )
    types["DetectedAppSplashScreenOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DetectedAppSplashScreenOut"])
    types["PerfSampleIn"] = t.struct(
        {
            "sampleTime": t.proxy(renames["TimestampIn"]).optional(),
            "value": t.number().optional(),
        }
    ).named(renames["PerfSampleIn"])
    types["PerfSampleOut"] = t.struct(
        {
            "sampleTime": t.proxy(renames["TimestampOut"]).optional(),
            "value": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerfSampleOut"])
    types["StepIn"] = t.struct(
        {
            "creationTime": t.proxy(renames["TimestampIn"]).optional(),
            "multiStep": t.proxy(renames["MultiStepIn"]).optional(),
            "stepId": t.string().optional(),
            "testExecutionStep": t.proxy(renames["TestExecutionStepIn"]).optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "outcome": t.proxy(renames["OutcomeIn"]).optional(),
            "labels": t.array(t.proxy(renames["StepLabelsEntryIn"])).optional(),
            "dimensionValue": t.array(
                t.proxy(renames["StepDimensionValueEntryIn"])
            ).optional(),
            "hasImages": t.boolean().optional(),
            "runDuration": t.proxy(renames["DurationIn"]).optional(),
            "deviceUsageDuration": t.proxy(renames["DurationIn"]).optional(),
            "completionTime": t.proxy(renames["TimestampIn"]).optional(),
            "toolExecutionStep": t.proxy(renames["ToolExecutionStepIn"]).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["StepIn"])
    types["StepOut"] = t.struct(
        {
            "creationTime": t.proxy(renames["TimestampOut"]).optional(),
            "multiStep": t.proxy(renames["MultiStepOut"]).optional(),
            "stepId": t.string().optional(),
            "testExecutionStep": t.proxy(renames["TestExecutionStepOut"]).optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "outcome": t.proxy(renames["OutcomeOut"]).optional(),
            "labels": t.array(t.proxy(renames["StepLabelsEntryOut"])).optional(),
            "dimensionValue": t.array(
                t.proxy(renames["StepDimensionValueEntryOut"])
            ).optional(),
            "hasImages": t.boolean().optional(),
            "runDuration": t.proxy(renames["DurationOut"]).optional(),
            "deviceUsageDuration": t.proxy(renames["DurationOut"]).optional(),
            "completionTime": t.proxy(renames["TimestampOut"]).optional(),
            "toolExecutionStep": t.proxy(renames["ToolExecutionStepOut"]).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StepOut"])
    types["ProjectSettingsIn"] = t.struct(
        {"name": t.string().optional(), "defaultBucket": t.string().optional()}
    ).named(renames["ProjectSettingsIn"])
    types["ProjectSettingsOut"] = t.struct(
        {
            "name": t.string().optional(),
            "defaultBucket": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectSettingsOut"])
    types["ListStepThumbnailsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "thumbnails": t.array(t.proxy(renames["ImageIn"])).optional(),
        }
    ).named(renames["ListStepThumbnailsResponseIn"])
    types["ListStepThumbnailsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "thumbnails": t.array(t.proxy(renames["ImageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListStepThumbnailsResponseOut"])
    types["TestCaseReferenceIn"] = t.struct(
        {
            "className": t.string().optional(),
            "testSuiteName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["TestCaseReferenceIn"])
    types["TestCaseReferenceOut"] = t.struct(
        {
            "className": t.string().optional(),
            "testSuiteName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestCaseReferenceOut"])
    types["StackTraceIn"] = t.struct({"exception": t.string().optional()}).named(
        renames["StackTraceIn"]
    )
    types["StackTraceOut"] = t.struct(
        {
            "exception": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackTraceOut"])
    types["FailedToInstallIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FailedToInstallIn"]
    )
    types["FailedToInstallOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FailedToInstallOut"])
    types["RoboScriptExecutionIn"] = t.struct(
        {
            "totalActions": t.integer().optional(),
            "successfulActions": t.integer().optional(),
        }
    ).named(renames["RoboScriptExecutionIn"])
    types["RoboScriptExecutionOut"] = t.struct(
        {
            "totalActions": t.integer().optional(),
            "successfulActions": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RoboScriptExecutionOut"])
    types["MultiStepIn"] = t.struct(
        {
            "primaryStep": t.proxy(renames["PrimaryStepIn"]).optional(),
            "multistepNumber": t.integer().optional(),
            "primaryStepId": t.string().optional(),
        }
    ).named(renames["MultiStepIn"])
    types["MultiStepOut"] = t.struct(
        {
            "primaryStep": t.proxy(renames["PrimaryStepOut"]).optional(),
            "multistepNumber": t.integer().optional(),
            "primaryStepId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultiStepOut"])
    types["MemoryInfoIn"] = t.struct(
        {
            "memoryCapInKibibyte": t.string().optional(),
            "memoryTotalInKibibyte": t.string().optional(),
        }
    ).named(renames["MemoryInfoIn"])
    types["MemoryInfoOut"] = t.struct(
        {
            "memoryCapInKibibyte": t.string().optional(),
            "memoryTotalInKibibyte": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemoryInfoOut"])
    types["UsedRoboDirectiveIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["UsedRoboDirectiveIn"])
    types["UsedRoboDirectiveOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsedRoboDirectiveOut"])
    types["IosTestLoopIn"] = t.struct({"bundleId": t.string().optional()}).named(
        renames["IosTestLoopIn"]
    )
    types["IosTestLoopOut"] = t.struct(
        {
            "bundleId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosTestLoopOut"])
    types["NonSdkApiUsageViolationIn"] = t.struct(
        {
            "apiSignatures": t.array(t.string()).optional(),
            "uniqueApis": t.integer().optional(),
        }
    ).named(renames["NonSdkApiUsageViolationIn"])
    types["NonSdkApiUsageViolationOut"] = t.struct(
        {
            "apiSignatures": t.array(t.string()).optional(),
            "uniqueApis": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonSdkApiUsageViolationOut"])
    types["InsufficientCoverageIn"] = t.struct({"_": t.string().optional()}).named(
        renames["InsufficientCoverageIn"]
    )
    types["InsufficientCoverageOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["InsufficientCoverageOut"])
    types["UsedRoboIgnoreDirectiveIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["UsedRoboIgnoreDirectiveIn"])
    types["UsedRoboIgnoreDirectiveOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsedRoboIgnoreDirectiveOut"])
    types["ThumbnailIn"] = t.struct(
        {
            "data": t.string().optional(),
            "heightPx": t.integer().optional(),
            "widthPx": t.integer().optional(),
            "contentType": t.string().optional(),
        }
    ).named(renames["ThumbnailIn"])
    types["ThumbnailOut"] = t.struct(
        {
            "data": t.string().optional(),
            "heightPx": t.integer().optional(),
            "widthPx": t.integer().optional(),
            "contentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThumbnailOut"])
    types["AndroidTestLoopIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AndroidTestLoopIn"]
    )
    types["AndroidTestLoopOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AndroidTestLoopOut"])
    types["BasicPerfSampleSeriesIn"] = t.struct(
        {
            "perfMetricType": t.string(),
            "sampleSeriesLabel": t.string(),
            "perfUnit": t.string(),
        }
    ).named(renames["BasicPerfSampleSeriesIn"])
    types["BasicPerfSampleSeriesOut"] = t.struct(
        {
            "perfMetricType": t.string(),
            "sampleSeriesLabel": t.string(),
            "perfUnit": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicPerfSampleSeriesOut"])
    types["EncounteredNonAndroidUiWidgetScreenIn"] = t.struct(
        {
            "screenIds": t.array(t.string()).optional(),
            "distinctScreens": t.integer().optional(),
        }
    ).named(renames["EncounteredNonAndroidUiWidgetScreenIn"])
    types["EncounteredNonAndroidUiWidgetScreenOut"] = t.struct(
        {
            "screenIds": t.array(t.string()).optional(),
            "distinctScreens": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncounteredNonAndroidUiWidgetScreenOut"])
    types["ListExecutionsResponseIn"] = t.struct(
        {
            "executions": t.array(t.proxy(renames["ExecutionIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListExecutionsResponseIn"])
    types["ListExecutionsResponseOut"] = t.struct(
        {
            "executions": t.array(t.proxy(renames["ExecutionOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListExecutionsResponseOut"])
    types["TestSuiteOverviewIn"] = t.struct(
        {
            "totalCount": t.integer().optional(),
            "elapsedTime": t.proxy(renames["DurationIn"]).optional(),
            "failureCount": t.integer().optional(),
            "skippedCount": t.integer().optional(),
            "errorCount": t.integer().optional(),
            "xmlSource": t.proxy(renames["FileReferenceIn"]).optional(),
            "flakyCount": t.integer().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["TestSuiteOverviewIn"])
    types["TestSuiteOverviewOut"] = t.struct(
        {
            "totalCount": t.integer().optional(),
            "elapsedTime": t.proxy(renames["DurationOut"]).optional(),
            "failureCount": t.integer().optional(),
            "skippedCount": t.integer().optional(),
            "errorCount": t.integer().optional(),
            "xmlSource": t.proxy(renames["FileReferenceOut"]).optional(),
            "flakyCount": t.integer().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestSuiteOverviewOut"])
    types["ImageIn"] = t.struct(
        {
            "stepId": t.string().optional(),
            "thumbnail": t.proxy(renames["ThumbnailIn"]).optional(),
            "sourceImage": t.proxy(renames["ToolOutputReferenceIn"]).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "stepId": t.string().optional(),
            "thumbnail": t.proxy(renames["ThumbnailOut"]).optional(),
            "sourceImage": t.proxy(renames["ToolOutputReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["SuggestionProtoIn"] = t.struct(
        {
            "helpUrl": t.string().optional(),
            "region": t.proxy(renames["RegionProtoIn"]).optional(),
            "title": t.string().optional(),
            "secondaryPriority": t.number().optional(),
            "priority": t.string().optional(),
            "pseudoResourceId": t.string().optional(),
            "shortMessage": t.proxy(renames["SafeHtmlProtoIn"]).optional(),
            "screenId": t.string().optional(),
            "resourceName": t.string().optional(),
            "longMessage": t.proxy(renames["SafeHtmlProtoIn"]).optional(),
        }
    ).named(renames["SuggestionProtoIn"])
    types["SuggestionProtoOut"] = t.struct(
        {
            "helpUrl": t.string().optional(),
            "region": t.proxy(renames["RegionProtoOut"]).optional(),
            "title": t.string().optional(),
            "secondaryPriority": t.number().optional(),
            "priority": t.string().optional(),
            "pseudoResourceId": t.string().optional(),
            "shortMessage": t.proxy(renames["SafeHtmlProtoOut"]).optional(),
            "screenId": t.string().optional(),
            "resourceName": t.string().optional(),
            "longMessage": t.proxy(renames["SafeHtmlProtoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestionProtoOut"])
    types["EnvironmentIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "completionTime": t.proxy(renames["TimestampIn"]).optional(),
            "environmentResult": t.proxy(renames["MergedResultIn"]).optional(),
            "resultsStorage": t.proxy(renames["ResultsStorageIn"]).optional(),
            "executionId": t.string().optional(),
            "shardSummaries": t.array(t.proxy(renames["ShardSummaryIn"])).optional(),
            "environmentId": t.string().optional(),
            "creationTime": t.proxy(renames["TimestampIn"]).optional(),
            "historyId": t.string().optional(),
            "displayName": t.string().optional(),
            "dimensionValue": t.array(
                t.proxy(renames["EnvironmentDimensionValueEntryIn"])
            ).optional(),
        }
    ).named(renames["EnvironmentIn"])
    types["EnvironmentOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "completionTime": t.proxy(renames["TimestampOut"]).optional(),
            "environmentResult": t.proxy(renames["MergedResultOut"]).optional(),
            "resultsStorage": t.proxy(renames["ResultsStorageOut"]).optional(),
            "executionId": t.string().optional(),
            "shardSummaries": t.array(t.proxy(renames["ShardSummaryOut"])).optional(),
            "environmentId": t.string().optional(),
            "creationTime": t.proxy(renames["TimestampOut"]).optional(),
            "historyId": t.string().optional(),
            "displayName": t.string().optional(),
            "dimensionValue": t.array(
                t.proxy(renames["EnvironmentDimensionValueEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentOut"])
    types["PerfSampleSeriesIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "basicPerfSampleSeries": t.proxy(
                renames["BasicPerfSampleSeriesIn"]
            ).optional(),
            "sampleSeriesId": t.string().optional(),
            "stepId": t.string().optional(),
            "historyId": t.string().optional(),
            "executionId": t.string().optional(),
        }
    ).named(renames["PerfSampleSeriesIn"])
    types["PerfSampleSeriesOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "basicPerfSampleSeries": t.proxy(
                renames["BasicPerfSampleSeriesOut"]
            ).optional(),
            "sampleSeriesId": t.string().optional(),
            "stepId": t.string().optional(),
            "historyId": t.string().optional(),
            "executionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerfSampleSeriesOut"])
    types["FatalExceptionIn"] = t.struct(
        {"stackTrace": t.proxy(renames["StackTraceIn"]).optional()}
    ).named(renames["FatalExceptionIn"])
    types["FatalExceptionOut"] = t.struct(
        {
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FatalExceptionOut"])
    types["OverlappingUIElementsIn"] = t.struct(
        {
            "resourceName": t.array(t.string()).optional(),
            "screenId": t.string().optional(),
        }
    ).named(renames["OverlappingUIElementsIn"])
    types["OverlappingUIElementsOut"] = t.struct(
        {
            "resourceName": t.array(t.string()).optional(),
            "screenId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OverlappingUIElementsOut"])
    types["BatchCreatePerfSamplesRequestIn"] = t.struct(
        {"perfSamples": t.array(t.proxy(renames["PerfSampleIn"])).optional()}
    ).named(renames["BatchCreatePerfSamplesRequestIn"])
    types["BatchCreatePerfSamplesRequestOut"] = t.struct(
        {
            "perfSamples": t.array(t.proxy(renames["PerfSampleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreatePerfSamplesRequestOut"])
    types["NonSdkApiUsageViolationReportIn"] = t.struct(
        {
            "minSdkVersion": t.integer().optional(),
            "uniqueApis": t.integer().optional(),
            "exampleApis": t.array(t.proxy(renames["NonSdkApiIn"])).optional(),
            "targetSdkVersion": t.integer().optional(),
        }
    ).named(renames["NonSdkApiUsageViolationReportIn"])
    types["NonSdkApiUsageViolationReportOut"] = t.struct(
        {
            "minSdkVersion": t.integer().optional(),
            "uniqueApis": t.integer().optional(),
            "exampleApis": t.array(t.proxy(renames["NonSdkApiOut"])).optional(),
            "targetSdkVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonSdkApiUsageViolationReportOut"])
    types["ListStepAccessibilityClustersResponseIn"] = t.struct(
        {
            "name": t.string().optional(),
            "clusters": t.array(
                t.proxy(renames["SuggestionClusterProtoIn"])
            ).optional(),
        }
    ).named(renames["ListStepAccessibilityClustersResponseIn"])
    types["ListStepAccessibilityClustersResponseOut"] = t.struct(
        {
            "name": t.string().optional(),
            "clusters": t.array(
                t.proxy(renames["SuggestionClusterProtoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListStepAccessibilityClustersResponseOut"])
    types["BatchCreatePerfSamplesResponseIn"] = t.struct(
        {"perfSamples": t.array(t.proxy(renames["PerfSampleIn"]))}
    ).named(renames["BatchCreatePerfSamplesResponseIn"])
    types["BatchCreatePerfSamplesResponseOut"] = t.struct(
        {
            "perfSamples": t.array(t.proxy(renames["PerfSampleOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreatePerfSamplesResponseOut"])
    types["InAppPurchasesFoundIn"] = t.struct(
        {
            "inAppPurchasesFlowsExplored": t.integer().optional(),
            "inAppPurchasesFlowsStarted": t.integer().optional(),
        }
    ).named(renames["InAppPurchasesFoundIn"])
    types["InAppPurchasesFoundOut"] = t.struct(
        {
            "inAppPurchasesFlowsExplored": t.integer().optional(),
            "inAppPurchasesFlowsStarted": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InAppPurchasesFoundOut"])
    types["SafeHtmlProtoIn"] = t.struct(
        {"privateDoNotAccessOrElseSafeHtmlWrappedValue": t.string().optional()}
    ).named(renames["SafeHtmlProtoIn"])
    types["SafeHtmlProtoOut"] = t.struct(
        {
            "privateDoNotAccessOrElseSafeHtmlWrappedValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SafeHtmlProtoOut"])
    types["IndividualOutcomeIn"] = t.struct(
        {
            "runDuration": t.proxy(renames["DurationIn"]).optional(),
            "multistepNumber": t.integer().optional(),
            "stepId": t.string(),
            "outcomeSummary": t.string(),
        }
    ).named(renames["IndividualOutcomeIn"])
    types["IndividualOutcomeOut"] = t.struct(
        {
            "runDuration": t.proxy(renames["DurationOut"]).optional(),
            "multistepNumber": t.integer().optional(),
            "stepId": t.string(),
            "outcomeSummary": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndividualOutcomeOut"])
    types["HistoryIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "historyId": t.string().optional(),
            "testPlatform": t.string().optional(),
        }
    ).named(renames["HistoryIn"])
    types["HistoryOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "historyId": t.string().optional(),
            "testPlatform": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistoryOut"])
    types["TestCaseIn"] = t.struct(
        {
            "stackTraces": t.array(t.proxy(renames["StackTraceIn"])).optional(),
            "testCaseReference": t.proxy(renames["TestCaseReferenceIn"]).optional(),
            "elapsedTime": t.proxy(renames["DurationIn"]).optional(),
            "testCaseId": t.string().optional(),
            "skippedMessage": t.string().optional(),
            "toolOutputs": t.array(
                t.proxy(renames["ToolOutputReferenceIn"])
            ).optional(),
            "startTime": t.proxy(renames["TimestampIn"]).optional(),
            "status": t.string().optional(),
            "endTime": t.proxy(renames["TimestampIn"]).optional(),
        }
    ).named(renames["TestCaseIn"])
    types["TestCaseOut"] = t.struct(
        {
            "stackTraces": t.array(t.proxy(renames["StackTraceOut"])).optional(),
            "testCaseReference": t.proxy(renames["TestCaseReferenceOut"]).optional(),
            "elapsedTime": t.proxy(renames["DurationOut"]).optional(),
            "testCaseId": t.string().optional(),
            "skippedMessage": t.string().optional(),
            "toolOutputs": t.array(
                t.proxy(renames["ToolOutputReferenceOut"])
            ).optional(),
            "startTime": t.proxy(renames["TimestampOut"]).optional(),
            "status": t.string().optional(),
            "endTime": t.proxy(renames["TimestampOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestCaseOut"])
    types["MergedResultIn"] = t.struct(
        {
            "state": t.string().optional(),
            "outcome": t.proxy(renames["OutcomeIn"]).optional(),
            "testSuiteOverviews": t.array(
                t.proxy(renames["TestSuiteOverviewIn"])
            ).optional(),
        }
    ).named(renames["MergedResultIn"])
    types["MergedResultOut"] = t.struct(
        {
            "state": t.string().optional(),
            "outcome": t.proxy(renames["OutcomeOut"]).optional(),
            "testSuiteOverviews": t.array(
                t.proxy(renames["TestSuiteOverviewOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MergedResultOut"])
    types["CPUInfoIn"] = t.struct(
        {
            "numberOfCores": t.integer().optional(),
            "cpuProcessor": t.string().optional(),
            "cpuSpeedInGhz": t.number().optional(),
        }
    ).named(renames["CPUInfoIn"])
    types["CPUInfoOut"] = t.struct(
        {
            "numberOfCores": t.integer().optional(),
            "cpuProcessor": t.string().optional(),
            "cpuSpeedInGhz": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CPUInfoOut"])
    types["ListPerfSamplesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "perfSamples": t.array(t.proxy(renames["PerfSampleIn"])),
        }
    ).named(renames["ListPerfSamplesResponseIn"])
    types["ListPerfSamplesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "perfSamples": t.array(t.proxy(renames["PerfSampleOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPerfSamplesResponseOut"])
    types["IosAppCrashedIn"] = t.struct(
        {"stackTrace": t.proxy(renames["StackTraceIn"]).optional()}
    ).named(renames["IosAppCrashedIn"])
    types["IosAppCrashedOut"] = t.struct(
        {
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosAppCrashedOut"])
    types["IosAppInfoIn"] = t.struct({"name": t.string().optional()}).named(
        renames["IosAppInfoIn"]
    )
    types["IosAppInfoOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosAppInfoOut"])
    types["OutcomeIn"] = t.struct(
        {
            "failureDetail": t.proxy(renames["FailureDetailIn"]).optional(),
            "skippedDetail": t.proxy(renames["SkippedDetailIn"]).optional(),
            "successDetail": t.proxy(renames["SuccessDetailIn"]).optional(),
            "inconclusiveDetail": t.proxy(renames["InconclusiveDetailIn"]).optional(),
            "summary": t.string().optional(),
        }
    ).named(renames["OutcomeIn"])
    types["OutcomeOut"] = t.struct(
        {
            "failureDetail": t.proxy(renames["FailureDetailOut"]).optional(),
            "skippedDetail": t.proxy(renames["SkippedDetailOut"]).optional(),
            "successDetail": t.proxy(renames["SuccessDetailOut"]).optional(),
            "inconclusiveDetail": t.proxy(renames["InconclusiveDetailOut"]).optional(),
            "summary": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutcomeOut"])
    types["PerfMetricsSummaryIn"] = t.struct(
        {
            "appStartTime": t.proxy(renames["AppStartTimeIn"]),
            "projectId": t.string().optional(),
            "stepId": t.string().optional(),
            "executionId": t.string().optional(),
            "historyId": t.string().optional(),
            "perfEnvironment": t.proxy(renames["PerfEnvironmentIn"]).optional(),
            "graphicsStats": t.proxy(renames["GraphicsStatsIn"]).optional(),
            "perfMetrics": t.array(t.string()).optional(),
        }
    ).named(renames["PerfMetricsSummaryIn"])
    types["PerfMetricsSummaryOut"] = t.struct(
        {
            "appStartTime": t.proxy(renames["AppStartTimeOut"]),
            "projectId": t.string().optional(),
            "stepId": t.string().optional(),
            "executionId": t.string().optional(),
            "historyId": t.string().optional(),
            "perfEnvironment": t.proxy(renames["PerfEnvironmentOut"]).optional(),
            "graphicsStats": t.proxy(renames["GraphicsStatsOut"]).optional(),
            "perfMetrics": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerfMetricsSummaryOut"])
    types["ScreenshotClusterIn"] = t.struct(
        {
            "screens": t.array(t.proxy(renames["ScreenIn"])).optional(),
            "activity": t.string().optional(),
            "keyScreen": t.proxy(renames["ScreenIn"]).optional(),
            "clusterId": t.string().optional(),
        }
    ).named(renames["ScreenshotClusterIn"])
    types["ScreenshotClusterOut"] = t.struct(
        {
            "screens": t.array(t.proxy(renames["ScreenOut"])).optional(),
            "activity": t.string().optional(),
            "keyScreen": t.proxy(renames["ScreenOut"]).optional(),
            "clusterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScreenshotClusterOut"])
    types["ResultsStorageIn"] = t.struct(
        {
            "xunitXmlFile": t.proxy(renames["FileReferenceIn"]).optional(),
            "resultsStoragePath": t.proxy(renames["FileReferenceIn"]).optional(),
        }
    ).named(renames["ResultsStorageIn"])
    types["ResultsStorageOut"] = t.struct(
        {
            "xunitXmlFile": t.proxy(renames["FileReferenceOut"]).optional(),
            "resultsStoragePath": t.proxy(renames["FileReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultsStorageOut"])
    types["LogcatCollectionErrorIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LogcatCollectionErrorIn"]
    )
    types["LogcatCollectionErrorOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LogcatCollectionErrorOut"])
    types["CrashDialogErrorIn"] = t.struct(
        {"crashPackage": t.string().optional()}
    ).named(renames["CrashDialogErrorIn"])
    types["CrashDialogErrorOut"] = t.struct(
        {
            "crashPackage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CrashDialogErrorOut"])
    types["StartActivityNotFoundIn"] = t.struct(
        {"action": t.string(), "uri": t.string()}
    ).named(renames["StartActivityNotFoundIn"])
    types["StartActivityNotFoundOut"] = t.struct(
        {
            "action": t.string(),
            "uri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartActivityNotFoundOut"])
    types["NonSdkApiIn"] = t.struct(
        {
            "apiSignature": t.string().optional(),
            "insights": t.array(t.proxy(renames["NonSdkApiInsightIn"])).optional(),
            "exampleStackTraces": t.array(t.string()).optional(),
            "list": t.string().optional(),
            "invocationCount": t.integer().optional(),
        }
    ).named(renames["NonSdkApiIn"])
    types["NonSdkApiOut"] = t.struct(
        {
            "apiSignature": t.string().optional(),
            "insights": t.array(t.proxy(renames["NonSdkApiInsightOut"])).optional(),
            "exampleStackTraces": t.array(t.string()).optional(),
            "list": t.string().optional(),
            "invocationCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonSdkApiOut"])
    types["SuccessDetailIn"] = t.struct(
        {"otherNativeCrash": t.boolean().optional()}
    ).named(renames["SuccessDetailIn"])
    types["SuccessDetailOut"] = t.struct(
        {
            "otherNativeCrash": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuccessDetailOut"])
    types["ListHistoriesResponseIn"] = t.struct(
        {
            "histories": t.array(t.proxy(renames["HistoryIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListHistoriesResponseIn"])
    types["ListHistoriesResponseOut"] = t.struct(
        {
            "histories": t.array(t.proxy(renames["HistoryOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListHistoriesResponseOut"])
    types["UnusedRoboDirectiveIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["UnusedRoboDirectiveIn"])
    types["UnusedRoboDirectiveOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnusedRoboDirectiveOut"])
    types["GraphicsStatsBucketIn"] = t.struct(
        {"frameCount": t.string().optional(), "renderMillis": t.string().optional()}
    ).named(renames["GraphicsStatsBucketIn"])
    types["GraphicsStatsBucketOut"] = t.struct(
        {
            "frameCount": t.string().optional(),
            "renderMillis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GraphicsStatsBucketOut"])
    types["TestExecutionStepIn"] = t.struct(
        {
            "testIssues": t.array(t.proxy(renames["TestIssueIn"])).optional(),
            "toolExecution": t.proxy(renames["ToolExecutionIn"]).optional(),
            "testTiming": t.proxy(renames["TestTimingIn"]).optional(),
            "testSuiteOverviews": t.array(
                t.proxy(renames["TestSuiteOverviewIn"])
            ).optional(),
        }
    ).named(renames["TestExecutionStepIn"])
    types["TestExecutionStepOut"] = t.struct(
        {
            "testIssues": t.array(t.proxy(renames["TestIssueOut"])).optional(),
            "toolExecution": t.proxy(renames["ToolExecutionOut"]).optional(),
            "testTiming": t.proxy(renames["TestTimingOut"]).optional(),
            "testSuiteOverviews": t.array(
                t.proxy(renames["TestSuiteOverviewOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestExecutionStepOut"])
    types["ToolExecutionStepIn"] = t.struct(
        {"toolExecution": t.proxy(renames["ToolExecutionIn"]).optional()}
    ).named(renames["ToolExecutionStepIn"])
    types["ToolExecutionStepOut"] = t.struct(
        {
            "toolExecution": t.proxy(renames["ToolExecutionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ToolExecutionStepOut"])
    types["LauncherActivityNotFoundIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LauncherActivityNotFoundIn"]
    )
    types["LauncherActivityNotFoundOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LauncherActivityNotFoundOut"])
    types["TestIssueIn"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "stackTrace": t.proxy(renames["StackTraceIn"]).optional(),
            "warning": t.proxy(renames["AnyIn"]).optional(),
            "category": t.string().optional(),
            "type": t.string().optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["TestIssueIn"])
    types["TestIssueOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "warning": t.proxy(renames["AnyOut"]).optional(),
            "category": t.string().optional(),
            "type": t.string().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIssueOut"])
    types["BlankScreenIn"] = t.struct({"screenId": t.string().optional()}).named(
        renames["BlankScreenIn"]
    )
    types["BlankScreenOut"] = t.struct(
        {
            "screenId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BlankScreenOut"])
    types["NativeCrashIn"] = t.struct(
        {"stackTrace": t.proxy(renames["StackTraceIn"]).optional()}
    ).named(renames["NativeCrashIn"])
    types["NativeCrashOut"] = t.struct(
        {
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NativeCrashOut"])
    types["ListTestCasesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string(),
            "testCases": t.array(t.proxy(renames["TestCaseIn"])).optional(),
        }
    ).named(renames["ListTestCasesResponseIn"])
    types["ListTestCasesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string(),
            "testCases": t.array(t.proxy(renames["TestCaseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTestCasesResponseOut"])
    types["MatrixDimensionDefinitionIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MatrixDimensionDefinitionIn"]
    )
    types["MatrixDimensionDefinitionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MatrixDimensionDefinitionOut"])
    types["AndroidAppInfoIn"] = t.struct(
        {
            "versionName": t.string().optional(),
            "packageName": t.string().optional(),
            "name": t.string().optional(),
            "versionCode": t.string().optional(),
        }
    ).named(renames["AndroidAppInfoIn"])
    types["AndroidAppInfoOut"] = t.struct(
        {
            "versionName": t.string().optional(),
            "packageName": t.string().optional(),
            "name": t.string().optional(),
            "versionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidAppInfoOut"])
    types["IosXcTestIn"] = t.struct(
        {"xcodeVersion": t.string().optional(), "bundleId": t.string().optional()}
    ).named(renames["IosXcTestIn"])
    types["IosXcTestOut"] = t.struct(
        {
            "xcodeVersion": t.string().optional(),
            "bundleId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosXcTestOut"])
    types["FailureDetailIn"] = t.struct(
        {
            "unableToCrawl": t.boolean().optional(),
            "timedOut": t.boolean().optional(),
            "notInstalled": t.boolean().optional(),
            "deviceOutOfMemory": t.boolean().optional(),
            "failedRoboscript": t.boolean().optional(),
            "otherNativeCrash": t.boolean().optional(),
            "crashed": t.boolean().optional(),
        }
    ).named(renames["FailureDetailIn"])
    types["FailureDetailOut"] = t.struct(
        {
            "unableToCrawl": t.boolean().optional(),
            "timedOut": t.boolean().optional(),
            "notInstalled": t.boolean().optional(),
            "deviceOutOfMemory": t.boolean().optional(),
            "failedRoboscript": t.boolean().optional(),
            "otherNativeCrash": t.boolean().optional(),
            "crashed": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FailureDetailOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["AndroidTestIn"] = t.struct(
        {
            "androidAppInfo": t.proxy(renames["AndroidAppInfoIn"]).optional(),
            "androidInstrumentationTest": t.proxy(
                renames["AndroidInstrumentationTestIn"]
            ).optional(),
            "androidRoboTest": t.proxy(renames["AndroidRoboTestIn"]).optional(),
            "androidTestLoop": t.proxy(renames["AndroidTestLoopIn"]).optional(),
            "testTimeout": t.proxy(renames["DurationIn"]).optional(),
        }
    ).named(renames["AndroidTestIn"])
    types["AndroidTestOut"] = t.struct(
        {
            "androidAppInfo": t.proxy(renames["AndroidAppInfoOut"]).optional(),
            "androidInstrumentationTest": t.proxy(
                renames["AndroidInstrumentationTestOut"]
            ).optional(),
            "androidRoboTest": t.proxy(renames["AndroidRoboTestOut"]).optional(),
            "androidTestLoop": t.proxy(renames["AndroidTestLoopOut"]).optional(),
            "testTimeout": t.proxy(renames["DurationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidTestOut"])
    types["PublishXunitXmlFilesRequestIn"] = t.struct(
        {"xunitXmlFiles": t.array(t.proxy(renames["FileReferenceIn"])).optional()}
    ).named(renames["PublishXunitXmlFilesRequestIn"])
    types["PublishXunitXmlFilesRequestOut"] = t.struct(
        {
            "xunitXmlFiles": t.array(t.proxy(renames["FileReferenceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishXunitXmlFilesRequestOut"])
    types["SuggestionClusterProtoIn"] = t.struct(
        {
            "category": t.string().optional(),
            "suggestions": t.array(t.proxy(renames["SuggestionProtoIn"])).optional(),
        }
    ).named(renames["SuggestionClusterProtoIn"])
    types["SuggestionClusterProtoOut"] = t.struct(
        {
            "category": t.string().optional(),
            "suggestions": t.array(t.proxy(renames["SuggestionProtoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestionClusterProtoOut"])
    types["UnspecifiedWarningIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UnspecifiedWarningIn"]
    )
    types["UnspecifiedWarningOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UnspecifiedWarningOut"])
    types["ExecutionIn"] = t.struct(
        {
            "state": t.string().optional(),
            "testExecutionMatrixId": t.string().optional(),
            "completionTime": t.proxy(renames["TimestampIn"]).optional(),
            "specification": t.proxy(renames["SpecificationIn"]).optional(),
            "creationTime": t.proxy(renames["TimestampIn"]).optional(),
            "dimensionDefinitions": t.array(
                t.proxy(renames["MatrixDimensionDefinitionIn"])
            ).optional(),
            "executionId": t.string().optional(),
            "outcome": t.proxy(renames["OutcomeIn"]).optional(),
        }
    ).named(renames["ExecutionIn"])
    types["ExecutionOut"] = t.struct(
        {
            "state": t.string().optional(),
            "testExecutionMatrixId": t.string().optional(),
            "completionTime": t.proxy(renames["TimestampOut"]).optional(),
            "specification": t.proxy(renames["SpecificationOut"]).optional(),
            "creationTime": t.proxy(renames["TimestampOut"]).optional(),
            "dimensionDefinitions": t.array(
                t.proxy(renames["MatrixDimensionDefinitionOut"])
            ).optional(),
            "executionId": t.string().optional(),
            "outcome": t.proxy(renames["OutcomeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionOut"])
    types["PrimaryStepIn"] = t.struct(
        {
            "individualOutcome": t.array(
                t.proxy(renames["IndividualOutcomeIn"])
            ).optional(),
            "rollUp": t.string().optional(),
        }
    ).named(renames["PrimaryStepIn"])
    types["PrimaryStepOut"] = t.struct(
        {
            "individualOutcome": t.array(
                t.proxy(renames["IndividualOutcomeOut"])
            ).optional(),
            "rollUp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrimaryStepOut"])
    types["NonSdkApiInsightIn"] = t.struct(
        {
            "pendingGoogleUpdateInsight": t.proxy(
                renames["PendingGoogleUpdateInsightIn"]
            ).optional(),
            "exampleTraceMessages": t.array(t.string()).optional(),
            "upgradeInsight": t.proxy(renames["UpgradeInsightIn"]).optional(),
            "matcherId": t.string().optional(),
        }
    ).named(renames["NonSdkApiInsightIn"])
    types["NonSdkApiInsightOut"] = t.struct(
        {
            "pendingGoogleUpdateInsight": t.proxy(
                renames["PendingGoogleUpdateInsightOut"]
            ).optional(),
            "exampleTraceMessages": t.array(t.string()).optional(),
            "upgradeInsight": t.proxy(renames["UpgradeInsightOut"]).optional(),
            "matcherId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonSdkApiInsightOut"])
    types["TimestampIn"] = t.struct(
        {"nanos": t.integer().optional(), "seconds": t.string().optional()}
    ).named(renames["TimestampIn"])
    types["TimestampOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "seconds": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimestampOut"])
    types["ListStepsResponseIn"] = t.struct(
        {
            "steps": t.array(t.proxy(renames["StepIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListStepsResponseIn"])
    types["ListStepsResponseOut"] = t.struct(
        {
            "steps": t.array(t.proxy(renames["StepOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListStepsResponseOut"])
    types["EnvironmentDimensionValueEntryIn"] = t.struct(
        {"value": t.string(), "key": t.string()}
    ).named(renames["EnvironmentDimensionValueEntryIn"])
    types["EnvironmentDimensionValueEntryOut"] = t.struct(
        {
            "value": t.string(),
            "key": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentDimensionValueEntryOut"])
    types["GraphicsStatsIn"] = t.struct(
        {
            "highInputLatencyCount": t.string().optional(),
            "slowUiThreadCount": t.string().optional(),
            "p90Millis": t.string().optional(),
            "slowBitmapUploadCount": t.string().optional(),
            "p99Millis": t.string().optional(),
            "jankyFrames": t.string().optional(),
            "buckets": t.array(t.proxy(renames["GraphicsStatsBucketIn"])).optional(),
            "p95Millis": t.string().optional(),
            "missedVsyncCount": t.string().optional(),
            "slowDrawCount": t.string().optional(),
            "p50Millis": t.string().optional(),
            "totalFrames": t.string().optional(),
        }
    ).named(renames["GraphicsStatsIn"])
    types["GraphicsStatsOut"] = t.struct(
        {
            "highInputLatencyCount": t.string().optional(),
            "slowUiThreadCount": t.string().optional(),
            "p90Millis": t.string().optional(),
            "slowBitmapUploadCount": t.string().optional(),
            "p99Millis": t.string().optional(),
            "jankyFrames": t.string().optional(),
            "buckets": t.array(t.proxy(renames["GraphicsStatsBucketOut"])).optional(),
            "p95Millis": t.string().optional(),
            "missedVsyncCount": t.string().optional(),
            "slowDrawCount": t.string().optional(),
            "p50Millis": t.string().optional(),
            "totalFrames": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GraphicsStatsOut"])
    types["AppStartTimeIn"] = t.struct(
        {
            "fullyDrawnTime": t.proxy(renames["DurationIn"]).optional(),
            "initialDisplayTime": t.proxy(renames["DurationIn"]).optional(),
        }
    ).named(renames["AppStartTimeIn"])
    types["AppStartTimeOut"] = t.struct(
        {
            "fullyDrawnTime": t.proxy(renames["DurationOut"]).optional(),
            "initialDisplayTime": t.proxy(renames["DurationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppStartTimeOut"])

    functions = {}
    functions["projectsInitializeSettings"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/settings",
        t.struct({"projectId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ProjectSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetSettings"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/settings",
        t.struct({"projectId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ProjectSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesList"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}",
        t.struct(
            {
                "historyId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HistoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesCreate"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}",
        t.struct(
            {
                "historyId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HistoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesGet"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}",
        t.struct(
            {
                "historyId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HistoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsList"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}",
        t.struct(
            {
                "historyId": t.string().optional(),
                "executionId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecutionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsCreate"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}",
        t.struct(
            {
                "historyId": t.string().optional(),
                "executionId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecutionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsPatch"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}",
        t.struct(
            {
                "historyId": t.string().optional(),
                "executionId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecutionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsGet"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}",
        t.struct(
            {
                "historyId": t.string().optional(),
                "executionId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecutionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsClustersGet"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/clusters",
        t.struct(
            {
                "projectId": t.string().optional(),
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScreenshotClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsClustersList"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/clusters",
        t.struct(
            {
                "projectId": t.string().optional(),
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScreenshotClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsPatch"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps",
        t.struct(
            {
                "projectId": t.string().optional(),
                "historyId": t.string().optional(),
                "pageToken": t.string().optional(),
                "executionId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListStepsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsHistoriesExecutionsStepsAccessibilityClusters"
    ] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps",
        t.struct(
            {
                "projectId": t.string().optional(),
                "historyId": t.string().optional(),
                "pageToken": t.string().optional(),
                "executionId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListStepsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsPublishXunitXmlFiles"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps",
        t.struct(
            {
                "projectId": t.string().optional(),
                "historyId": t.string().optional(),
                "pageToken": t.string().optional(),
                "executionId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListStepsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsCreate"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps",
        t.struct(
            {
                "projectId": t.string().optional(),
                "historyId": t.string().optional(),
                "pageToken": t.string().optional(),
                "executionId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListStepsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsHistoriesExecutionsStepsGetPerfMetricsSummary"
    ] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps",
        t.struct(
            {
                "projectId": t.string().optional(),
                "historyId": t.string().optional(),
                "pageToken": t.string().optional(),
                "executionId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListStepsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsGet"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps",
        t.struct(
            {
                "projectId": t.string().optional(),
                "historyId": t.string().optional(),
                "pageToken": t.string().optional(),
                "executionId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListStepsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsList"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps",
        t.struct(
            {
                "projectId": t.string().optional(),
                "historyId": t.string().optional(),
                "pageToken": t.string().optional(),
                "executionId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListStepsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsThumbnailsList"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/thumbnails",
        t.struct(
            {
                "stepId": t.string().optional(),
                "executionId": t.string().optional(),
                "projectId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "historyId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListStepThumbnailsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsHistoriesExecutionsStepsPerfMetricsSummaryCreate"
    ] = toolresults.post(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfMetricsSummary",
        t.struct(
            {
                "historyId": t.string().optional(),
                "stepId": t.string().optional(),
                "executionId": t.string().optional(),
                "projectId": t.string().optional(),
                "appStartTime": t.proxy(renames["AppStartTimeIn"]),
                "perfEnvironment": t.proxy(renames["PerfEnvironmentIn"]).optional(),
                "graphicsStats": t.proxy(renames["GraphicsStatsIn"]).optional(),
                "perfMetrics": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PerfMetricsSummaryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsPerfSampleSeriesList"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries/{sampleSeriesId}",
        t.struct(
            {
                "executionId": t.string().optional(),
                "stepId": t.string().optional(),
                "sampleSeriesId": t.string().optional(),
                "historyId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PerfSampleSeriesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsHistoriesExecutionsStepsPerfSampleSeriesCreate"
    ] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries/{sampleSeriesId}",
        t.struct(
            {
                "executionId": t.string().optional(),
                "stepId": t.string().optional(),
                "sampleSeriesId": t.string().optional(),
                "historyId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PerfSampleSeriesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsPerfSampleSeriesGet"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries/{sampleSeriesId}",
        t.struct(
            {
                "executionId": t.string().optional(),
                "stepId": t.string().optional(),
                "sampleSeriesId": t.string().optional(),
                "historyId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PerfSampleSeriesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsHistoriesExecutionsStepsPerfSampleSeriesSamplesBatchCreate"
    ] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries/{sampleSeriesId}/samples",
        t.struct(
            {
                "historyId": t.string().optional(),
                "sampleSeriesId": t.string().optional(),
                "projectId": t.string().optional(),
                "executionId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "stepId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPerfSamplesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsHistoriesExecutionsStepsPerfSampleSeriesSamplesList"
    ] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries/{sampleSeriesId}/samples",
        t.struct(
            {
                "historyId": t.string().optional(),
                "sampleSeriesId": t.string().optional(),
                "projectId": t.string().optional(),
                "executionId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "stepId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPerfSamplesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsTestCasesGet"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/testCases",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "historyId": t.string().optional(),
                "pageToken": t.string().optional(),
                "stepId": t.string().optional(),
                "executionId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTestCasesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsTestCasesList"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/testCases",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "historyId": t.string().optional(),
                "pageToken": t.string().optional(),
                "stepId": t.string().optional(),
                "executionId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTestCasesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsEnvironmentsGet"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/environments",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "historyId": t.string(),
                "pageToken": t.string().optional(),
                "executionId": t.string(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEnvironmentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsEnvironmentsList"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/environments",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "historyId": t.string(),
                "pageToken": t.string().optional(),
                "executionId": t.string(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEnvironmentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="toolresults",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
