from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_toolresults() -> Import:
    toolresults = HTTPRuntime("https://toolresults.googleapis.com/")

    renames = {
        "ErrorResponse": "_toolresults_1_ErrorResponse",
        "FailedToInstallIn": "_toolresults_2_FailedToInstallIn",
        "FailedToInstallOut": "_toolresults_3_FailedToInstallOut",
        "ListPerfSamplesResponseIn": "_toolresults_4_ListPerfSamplesResponseIn",
        "ListPerfSamplesResponseOut": "_toolresults_5_ListPerfSamplesResponseOut",
        "EnvironmentDimensionValueEntryIn": "_toolresults_6_EnvironmentDimensionValueEntryIn",
        "EnvironmentDimensionValueEntryOut": "_toolresults_7_EnvironmentDimensionValueEntryOut",
        "AndroidTestIn": "_toolresults_8_AndroidTestIn",
        "AndroidTestOut": "_toolresults_9_AndroidTestOut",
        "PerfEnvironmentIn": "_toolresults_10_PerfEnvironmentIn",
        "PerfEnvironmentOut": "_toolresults_11_PerfEnvironmentOut",
        "IosAppInfoIn": "_toolresults_12_IosAppInfoIn",
        "IosAppInfoOut": "_toolresults_13_IosAppInfoOut",
        "UpgradeInsightIn": "_toolresults_14_UpgradeInsightIn",
        "UpgradeInsightOut": "_toolresults_15_UpgradeInsightOut",
        "FatalExceptionIn": "_toolresults_16_FatalExceptionIn",
        "FatalExceptionOut": "_toolresults_17_FatalExceptionOut",
        "PerfMetricsSummaryIn": "_toolresults_18_PerfMetricsSummaryIn",
        "PerfMetricsSummaryOut": "_toolresults_19_PerfMetricsSummaryOut",
        "InsufficientCoverageIn": "_toolresults_20_InsufficientCoverageIn",
        "InsufficientCoverageOut": "_toolresults_21_InsufficientCoverageOut",
        "StepLabelsEntryIn": "_toolresults_22_StepLabelsEntryIn",
        "StepLabelsEntryOut": "_toolresults_23_StepLabelsEntryOut",
        "StepIn": "_toolresults_24_StepIn",
        "StepOut": "_toolresults_25_StepOut",
        "TestCaseIn": "_toolresults_26_TestCaseIn",
        "TestCaseOut": "_toolresults_27_TestCaseOut",
        "SuggestionProtoIn": "_toolresults_28_SuggestionProtoIn",
        "SuggestionProtoOut": "_toolresults_29_SuggestionProtoOut",
        "ProjectSettingsIn": "_toolresults_30_ProjectSettingsIn",
        "ProjectSettingsOut": "_toolresults_31_ProjectSettingsOut",
        "IndividualOutcomeIn": "_toolresults_32_IndividualOutcomeIn",
        "IndividualOutcomeOut": "_toolresults_33_IndividualOutcomeOut",
        "IosTestLoopIn": "_toolresults_34_IosTestLoopIn",
        "IosTestLoopOut": "_toolresults_35_IosTestLoopOut",
        "StartActivityNotFoundIn": "_toolresults_36_StartActivityNotFoundIn",
        "StartActivityNotFoundOut": "_toolresults_37_StartActivityNotFoundOut",
        "ThumbnailIn": "_toolresults_38_ThumbnailIn",
        "ThumbnailOut": "_toolresults_39_ThumbnailOut",
        "OutcomeIn": "_toolresults_40_OutcomeIn",
        "OutcomeOut": "_toolresults_41_OutcomeOut",
        "ToolExecutionIn": "_toolresults_42_ToolExecutionIn",
        "ToolExecutionOut": "_toolresults_43_ToolExecutionOut",
        "BatchCreatePerfSamplesResponseIn": "_toolresults_44_BatchCreatePerfSamplesResponseIn",
        "BatchCreatePerfSamplesResponseOut": "_toolresults_45_BatchCreatePerfSamplesResponseOut",
        "ToolExecutionStepIn": "_toolresults_46_ToolExecutionStepIn",
        "ToolExecutionStepOut": "_toolresults_47_ToolExecutionStepOut",
        "ListPerfSampleSeriesResponseIn": "_toolresults_48_ListPerfSampleSeriesResponseIn",
        "ListPerfSampleSeriesResponseOut": "_toolresults_49_ListPerfSampleSeriesResponseOut",
        "EncounteredNonAndroidUiWidgetScreenIn": "_toolresults_50_EncounteredNonAndroidUiWidgetScreenIn",
        "EncounteredNonAndroidUiWidgetScreenOut": "_toolresults_51_EncounteredNonAndroidUiWidgetScreenOut",
        "UnusedRoboDirectiveIn": "_toolresults_52_UnusedRoboDirectiveIn",
        "UnusedRoboDirectiveOut": "_toolresults_53_UnusedRoboDirectiveOut",
        "ScreenshotClusterIn": "_toolresults_54_ScreenshotClusterIn",
        "ScreenshotClusterOut": "_toolresults_55_ScreenshotClusterOut",
        "IosXcTestIn": "_toolresults_56_IosXcTestIn",
        "IosXcTestOut": "_toolresults_57_IosXcTestOut",
        "BatchCreatePerfSamplesRequestIn": "_toolresults_58_BatchCreatePerfSamplesRequestIn",
        "BatchCreatePerfSamplesRequestOut": "_toolresults_59_BatchCreatePerfSamplesRequestOut",
        "ImageIn": "_toolresults_60_ImageIn",
        "ImageOut": "_toolresults_61_ImageOut",
        "NonSdkApiUsageViolationReportIn": "_toolresults_62_NonSdkApiUsageViolationReportIn",
        "NonSdkApiUsageViolationReportOut": "_toolresults_63_NonSdkApiUsageViolationReportOut",
        "TestSuiteOverviewIn": "_toolresults_64_TestSuiteOverviewIn",
        "TestSuiteOverviewOut": "_toolresults_65_TestSuiteOverviewOut",
        "NonSdkApiUsageViolationIn": "_toolresults_66_NonSdkApiUsageViolationIn",
        "NonSdkApiUsageViolationOut": "_toolresults_67_NonSdkApiUsageViolationOut",
        "RoboScriptExecutionIn": "_toolresults_68_RoboScriptExecutionIn",
        "RoboScriptExecutionOut": "_toolresults_69_RoboScriptExecutionOut",
        "UsedRoboDirectiveIn": "_toolresults_70_UsedRoboDirectiveIn",
        "UsedRoboDirectiveOut": "_toolresults_71_UsedRoboDirectiveOut",
        "ANRIn": "_toolresults_72_ANRIn",
        "ANROut": "_toolresults_73_ANROut",
        "PerfSampleSeriesIn": "_toolresults_74_PerfSampleSeriesIn",
        "PerfSampleSeriesOut": "_toolresults_75_PerfSampleSeriesOut",
        "TimestampIn": "_toolresults_76_TimestampIn",
        "TimestampOut": "_toolresults_77_TimestampOut",
        "FailureDetailIn": "_toolresults_78_FailureDetailIn",
        "FailureDetailOut": "_toolresults_79_FailureDetailOut",
        "DetectedAppSplashScreenIn": "_toolresults_80_DetectedAppSplashScreenIn",
        "DetectedAppSplashScreenOut": "_toolresults_81_DetectedAppSplashScreenOut",
        "IosTestIn": "_toolresults_82_IosTestIn",
        "IosTestOut": "_toolresults_83_IosTestOut",
        "LauncherActivityNotFoundIn": "_toolresults_84_LauncherActivityNotFoundIn",
        "LauncherActivityNotFoundOut": "_toolresults_85_LauncherActivityNotFoundOut",
        "InconclusiveDetailIn": "_toolresults_86_InconclusiveDetailIn",
        "InconclusiveDetailOut": "_toolresults_87_InconclusiveDetailOut",
        "ScreenIn": "_toolresults_88_ScreenIn",
        "ScreenOut": "_toolresults_89_ScreenOut",
        "NonSdkApiInsightIn": "_toolresults_90_NonSdkApiInsightIn",
        "NonSdkApiInsightOut": "_toolresults_91_NonSdkApiInsightOut",
        "EnvironmentIn": "_toolresults_92_EnvironmentIn",
        "EnvironmentOut": "_toolresults_93_EnvironmentOut",
        "AndroidAppInfoIn": "_toolresults_94_AndroidAppInfoIn",
        "AndroidAppInfoOut": "_toolresults_95_AndroidAppInfoOut",
        "AppStartTimeIn": "_toolresults_96_AppStartTimeIn",
        "AppStartTimeOut": "_toolresults_97_AppStartTimeOut",
        "ListStepThumbnailsResponseIn": "_toolresults_98_ListStepThumbnailsResponseIn",
        "ListStepThumbnailsResponseOut": "_toolresults_99_ListStepThumbnailsResponseOut",
        "IosAppCrashedIn": "_toolresults_100_IosAppCrashedIn",
        "IosAppCrashedOut": "_toolresults_101_IosAppCrashedOut",
        "UIElementTooDeepIn": "_toolresults_102_UIElementTooDeepIn",
        "UIElementTooDeepOut": "_toolresults_103_UIElementTooDeepOut",
        "MergedResultIn": "_toolresults_104_MergedResultIn",
        "MergedResultOut": "_toolresults_105_MergedResultOut",
        "SuccessDetailIn": "_toolresults_106_SuccessDetailIn",
        "SuccessDetailOut": "_toolresults_107_SuccessDetailOut",
        "SuggestionClusterProtoIn": "_toolresults_108_SuggestionClusterProtoIn",
        "SuggestionClusterProtoOut": "_toolresults_109_SuggestionClusterProtoOut",
        "PendingGoogleUpdateInsightIn": "_toolresults_110_PendingGoogleUpdateInsightIn",
        "PendingGoogleUpdateInsightOut": "_toolresults_111_PendingGoogleUpdateInsightOut",
        "UnspecifiedWarningIn": "_toolresults_112_UnspecifiedWarningIn",
        "UnspecifiedWarningOut": "_toolresults_113_UnspecifiedWarningOut",
        "BasicPerfSampleSeriesIn": "_toolresults_114_BasicPerfSampleSeriesIn",
        "BasicPerfSampleSeriesOut": "_toolresults_115_BasicPerfSampleSeriesOut",
        "SpecificationIn": "_toolresults_116_SpecificationIn",
        "SpecificationOut": "_toolresults_117_SpecificationOut",
        "ExecutionIn": "_toolresults_118_ExecutionIn",
        "ExecutionOut": "_toolresults_119_ExecutionOut",
        "StatusIn": "_toolresults_120_StatusIn",
        "StatusOut": "_toolresults_121_StatusOut",
        "StepDimensionValueEntryIn": "_toolresults_122_StepDimensionValueEntryIn",
        "StepDimensionValueEntryOut": "_toolresults_123_StepDimensionValueEntryOut",
        "CPUInfoIn": "_toolresults_124_CPUInfoIn",
        "CPUInfoOut": "_toolresults_125_CPUInfoOut",
        "OverlappingUIElementsIn": "_toolresults_126_OverlappingUIElementsIn",
        "OverlappingUIElementsOut": "_toolresults_127_OverlappingUIElementsOut",
        "AndroidRoboTestIn": "_toolresults_128_AndroidRoboTestIn",
        "AndroidRoboTestOut": "_toolresults_129_AndroidRoboTestOut",
        "ListExecutionsResponseIn": "_toolresults_130_ListExecutionsResponseIn",
        "ListExecutionsResponseOut": "_toolresults_131_ListExecutionsResponseOut",
        "IosRoboTestIn": "_toolresults_132_IosRoboTestIn",
        "IosRoboTestOut": "_toolresults_133_IosRoboTestOut",
        "GraphicsStatsBucketIn": "_toolresults_134_GraphicsStatsBucketIn",
        "GraphicsStatsBucketOut": "_toolresults_135_GraphicsStatsBucketOut",
        "TestIssueIn": "_toolresults_136_TestIssueIn",
        "TestIssueOut": "_toolresults_137_TestIssueOut",
        "PrimaryStepIn": "_toolresults_138_PrimaryStepIn",
        "PrimaryStepOut": "_toolresults_139_PrimaryStepOut",
        "ShardSummaryIn": "_toolresults_140_ShardSummaryIn",
        "ShardSummaryOut": "_toolresults_141_ShardSummaryOut",
        "MatrixDimensionDefinitionIn": "_toolresults_142_MatrixDimensionDefinitionIn",
        "MatrixDimensionDefinitionOut": "_toolresults_143_MatrixDimensionDefinitionOut",
        "EncounteredLoginScreenIn": "_toolresults_144_EncounteredLoginScreenIn",
        "EncounteredLoginScreenOut": "_toolresults_145_EncounteredLoginScreenOut",
        "PerformedGoogleLoginIn": "_toolresults_146_PerformedGoogleLoginIn",
        "PerformedGoogleLoginOut": "_toolresults_147_PerformedGoogleLoginOut",
        "ListEnvironmentsResponseIn": "_toolresults_148_ListEnvironmentsResponseIn",
        "ListEnvironmentsResponseOut": "_toolresults_149_ListEnvironmentsResponseOut",
        "MultiStepIn": "_toolresults_150_MultiStepIn",
        "MultiStepOut": "_toolresults_151_MultiStepOut",
        "AvailableDeepLinksIn": "_toolresults_152_AvailableDeepLinksIn",
        "AvailableDeepLinksOut": "_toolresults_153_AvailableDeepLinksOut",
        "AndroidTestLoopIn": "_toolresults_154_AndroidTestLoopIn",
        "AndroidTestLoopOut": "_toolresults_155_AndroidTestLoopOut",
        "TestCaseReferenceIn": "_toolresults_156_TestCaseReferenceIn",
        "TestCaseReferenceOut": "_toolresults_157_TestCaseReferenceOut",
        "BlankScreenIn": "_toolresults_158_BlankScreenIn",
        "BlankScreenOut": "_toolresults_159_BlankScreenOut",
        "InAppPurchasesFoundIn": "_toolresults_160_InAppPurchasesFoundIn",
        "InAppPurchasesFoundOut": "_toolresults_161_InAppPurchasesFoundOut",
        "ListScreenshotClustersResponseIn": "_toolresults_162_ListScreenshotClustersResponseIn",
        "ListScreenshotClustersResponseOut": "_toolresults_163_ListScreenshotClustersResponseOut",
        "NonSdkApiIn": "_toolresults_164_NonSdkApiIn",
        "NonSdkApiOut": "_toolresults_165_NonSdkApiOut",
        "StackTraceIn": "_toolresults_166_StackTraceIn",
        "StackTraceOut": "_toolresults_167_StackTraceOut",
        "TestExecutionStepIn": "_toolresults_168_TestExecutionStepIn",
        "TestExecutionStepOut": "_toolresults_169_TestExecutionStepOut",
        "ToolOutputReferenceIn": "_toolresults_170_ToolOutputReferenceIn",
        "ToolOutputReferenceOut": "_toolresults_171_ToolOutputReferenceOut",
        "StepSummaryIn": "_toolresults_172_StepSummaryIn",
        "StepSummaryOut": "_toolresults_173_StepSummaryOut",
        "ResultsStorageIn": "_toolresults_174_ResultsStorageIn",
        "ResultsStorageOut": "_toolresults_175_ResultsStorageOut",
        "MemoryInfoIn": "_toolresults_176_MemoryInfoIn",
        "MemoryInfoOut": "_toolresults_177_MemoryInfoOut",
        "DeviceOutOfMemoryIn": "_toolresults_178_DeviceOutOfMemoryIn",
        "DeviceOutOfMemoryOut": "_toolresults_179_DeviceOutOfMemoryOut",
        "ListTestCasesResponseIn": "_toolresults_180_ListTestCasesResponseIn",
        "ListTestCasesResponseOut": "_toolresults_181_ListTestCasesResponseOut",
        "LogcatCollectionErrorIn": "_toolresults_182_LogcatCollectionErrorIn",
        "LogcatCollectionErrorOut": "_toolresults_183_LogcatCollectionErrorOut",
        "ToolExitCodeIn": "_toolresults_184_ToolExitCodeIn",
        "ToolExitCodeOut": "_toolresults_185_ToolExitCodeOut",
        "GraphicsStatsIn": "_toolresults_186_GraphicsStatsIn",
        "GraphicsStatsOut": "_toolresults_187_GraphicsStatsOut",
        "HistoryIn": "_toolresults_188_HistoryIn",
        "HistoryOut": "_toolresults_189_HistoryOut",
        "ListStepsResponseIn": "_toolresults_190_ListStepsResponseIn",
        "ListStepsResponseOut": "_toolresults_191_ListStepsResponseOut",
        "AndroidInstrumentationTestIn": "_toolresults_192_AndroidInstrumentationTestIn",
        "AndroidInstrumentationTestOut": "_toolresults_193_AndroidInstrumentationTestOut",
        "ListStepAccessibilityClustersResponseIn": "_toolresults_194_ListStepAccessibilityClustersResponseIn",
        "ListStepAccessibilityClustersResponseOut": "_toolresults_195_ListStepAccessibilityClustersResponseOut",
        "PerfSampleIn": "_toolresults_196_PerfSampleIn",
        "PerfSampleOut": "_toolresults_197_PerfSampleOut",
        "CrashDialogErrorIn": "_toolresults_198_CrashDialogErrorIn",
        "CrashDialogErrorOut": "_toolresults_199_CrashDialogErrorOut",
        "FileReferenceIn": "_toolresults_200_FileReferenceIn",
        "FileReferenceOut": "_toolresults_201_FileReferenceOut",
        "AnyIn": "_toolresults_202_AnyIn",
        "AnyOut": "_toolresults_203_AnyOut",
        "DurationIn": "_toolresults_204_DurationIn",
        "DurationOut": "_toolresults_205_DurationOut",
        "NativeCrashIn": "_toolresults_206_NativeCrashIn",
        "NativeCrashOut": "_toolresults_207_NativeCrashOut",
        "RegionProtoIn": "_toolresults_208_RegionProtoIn",
        "RegionProtoOut": "_toolresults_209_RegionProtoOut",
        "SafeHtmlProtoIn": "_toolresults_210_SafeHtmlProtoIn",
        "SafeHtmlProtoOut": "_toolresults_211_SafeHtmlProtoOut",
        "PublishXunitXmlFilesRequestIn": "_toolresults_212_PublishXunitXmlFilesRequestIn",
        "PublishXunitXmlFilesRequestOut": "_toolresults_213_PublishXunitXmlFilesRequestOut",
        "PerformedMonkeyActionsIn": "_toolresults_214_PerformedMonkeyActionsIn",
        "PerformedMonkeyActionsOut": "_toolresults_215_PerformedMonkeyActionsOut",
        "ListHistoriesResponseIn": "_toolresults_216_ListHistoriesResponseIn",
        "ListHistoriesResponseOut": "_toolresults_217_ListHistoriesResponseOut",
        "SkippedDetailIn": "_toolresults_218_SkippedDetailIn",
        "SkippedDetailOut": "_toolresults_219_SkippedDetailOut",
        "TestTimingIn": "_toolresults_220_TestTimingIn",
        "TestTimingOut": "_toolresults_221_TestTimingOut",
        "UsedRoboIgnoreDirectiveIn": "_toolresults_222_UsedRoboIgnoreDirectiveIn",
        "UsedRoboIgnoreDirectiveOut": "_toolresults_223_UsedRoboIgnoreDirectiveOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["FailedToInstallIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FailedToInstallIn"]
    )
    types["FailedToInstallOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FailedToInstallOut"])
    types["ListPerfSamplesResponseIn"] = t.struct(
        {
            "perfSamples": t.array(t.proxy(renames["PerfSampleIn"])),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListPerfSamplesResponseIn"])
    types["ListPerfSamplesResponseOut"] = t.struct(
        {
            "perfSamples": t.array(t.proxy(renames["PerfSampleOut"])),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPerfSamplesResponseOut"])
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
    types["AndroidTestIn"] = t.struct(
        {
            "androidRoboTest": t.proxy(renames["AndroidRoboTestIn"]).optional(),
            "androidAppInfo": t.proxy(renames["AndroidAppInfoIn"]).optional(),
            "androidTestLoop": t.proxy(renames["AndroidTestLoopIn"]).optional(),
            "androidInstrumentationTest": t.proxy(
                renames["AndroidInstrumentationTestIn"]
            ).optional(),
            "testTimeout": t.proxy(renames["DurationIn"]).optional(),
        }
    ).named(renames["AndroidTestIn"])
    types["AndroidTestOut"] = t.struct(
        {
            "androidRoboTest": t.proxy(renames["AndroidRoboTestOut"]).optional(),
            "androidAppInfo": t.proxy(renames["AndroidAppInfoOut"]).optional(),
            "androidTestLoop": t.proxy(renames["AndroidTestLoopOut"]).optional(),
            "androidInstrumentationTest": t.proxy(
                renames["AndroidInstrumentationTestOut"]
            ).optional(),
            "testTimeout": t.proxy(renames["DurationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidTestOut"])
    types["PerfEnvironmentIn"] = t.struct(
        {
            "cpuInfo": t.proxy(renames["CPUInfoIn"]).optional(),
            "memoryInfo": t.proxy(renames["MemoryInfoIn"]).optional(),
        }
    ).named(renames["PerfEnvironmentIn"])
    types["PerfEnvironmentOut"] = t.struct(
        {
            "cpuInfo": t.proxy(renames["CPUInfoOut"]).optional(),
            "memoryInfo": t.proxy(renames["MemoryInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerfEnvironmentOut"])
    types["IosAppInfoIn"] = t.struct({"name": t.string().optional()}).named(
        renames["IosAppInfoIn"]
    )
    types["IosAppInfoOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosAppInfoOut"])
    types["UpgradeInsightIn"] = t.struct(
        {
            "upgradeToVersion": t.string().optional(),
            "packageName": t.string().optional(),
        }
    ).named(renames["UpgradeInsightIn"])
    types["UpgradeInsightOut"] = t.struct(
        {
            "upgradeToVersion": t.string().optional(),
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeInsightOut"])
    types["FatalExceptionIn"] = t.struct(
        {"stackTrace": t.proxy(renames["StackTraceIn"]).optional()}
    ).named(renames["FatalExceptionIn"])
    types["FatalExceptionOut"] = t.struct(
        {
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FatalExceptionOut"])
    types["PerfMetricsSummaryIn"] = t.struct(
        {
            "stepId": t.string().optional(),
            "historyId": t.string().optional(),
            "perfMetrics": t.array(t.string()).optional(),
            "perfEnvironment": t.proxy(renames["PerfEnvironmentIn"]).optional(),
            "appStartTime": t.proxy(renames["AppStartTimeIn"]),
            "projectId": t.string().optional(),
            "executionId": t.string().optional(),
            "graphicsStats": t.proxy(renames["GraphicsStatsIn"]).optional(),
        }
    ).named(renames["PerfMetricsSummaryIn"])
    types["PerfMetricsSummaryOut"] = t.struct(
        {
            "stepId": t.string().optional(),
            "historyId": t.string().optional(),
            "perfMetrics": t.array(t.string()).optional(),
            "perfEnvironment": t.proxy(renames["PerfEnvironmentOut"]).optional(),
            "appStartTime": t.proxy(renames["AppStartTimeOut"]),
            "projectId": t.string().optional(),
            "executionId": t.string().optional(),
            "graphicsStats": t.proxy(renames["GraphicsStatsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerfMetricsSummaryOut"])
    types["InsufficientCoverageIn"] = t.struct({"_": t.string().optional()}).named(
        renames["InsufficientCoverageIn"]
    )
    types["InsufficientCoverageOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["InsufficientCoverageOut"])
    types["StepLabelsEntryIn"] = t.struct(
        {"key": t.string(), "value": t.string()}
    ).named(renames["StepLabelsEntryIn"])
    types["StepLabelsEntryOut"] = t.struct(
        {
            "key": t.string(),
            "value": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StepLabelsEntryOut"])
    types["StepIn"] = t.struct(
        {
            "stepId": t.string().optional(),
            "labels": t.array(t.proxy(renames["StepLabelsEntryIn"])).optional(),
            "hasImages": t.boolean().optional(),
            "creationTime": t.proxy(renames["TimestampIn"]).optional(),
            "outcome": t.proxy(renames["OutcomeIn"]).optional(),
            "name": t.string().optional(),
            "multiStep": t.proxy(renames["MultiStepIn"]).optional(),
            "completionTime": t.proxy(renames["TimestampIn"]).optional(),
            "dimensionValue": t.array(
                t.proxy(renames["StepDimensionValueEntryIn"])
            ).optional(),
            "runDuration": t.proxy(renames["DurationIn"]).optional(),
            "description": t.string().optional(),
            "toolExecutionStep": t.proxy(renames["ToolExecutionStepIn"]).optional(),
            "testExecutionStep": t.proxy(renames["TestExecutionStepIn"]).optional(),
            "state": t.string().optional(),
            "deviceUsageDuration": t.proxy(renames["DurationIn"]).optional(),
        }
    ).named(renames["StepIn"])
    types["StepOut"] = t.struct(
        {
            "stepId": t.string().optional(),
            "labels": t.array(t.proxy(renames["StepLabelsEntryOut"])).optional(),
            "hasImages": t.boolean().optional(),
            "creationTime": t.proxy(renames["TimestampOut"]).optional(),
            "outcome": t.proxy(renames["OutcomeOut"]).optional(),
            "name": t.string().optional(),
            "multiStep": t.proxy(renames["MultiStepOut"]).optional(),
            "completionTime": t.proxy(renames["TimestampOut"]).optional(),
            "dimensionValue": t.array(
                t.proxy(renames["StepDimensionValueEntryOut"])
            ).optional(),
            "runDuration": t.proxy(renames["DurationOut"]).optional(),
            "description": t.string().optional(),
            "toolExecutionStep": t.proxy(renames["ToolExecutionStepOut"]).optional(),
            "testExecutionStep": t.proxy(renames["TestExecutionStepOut"]).optional(),
            "state": t.string().optional(),
            "deviceUsageDuration": t.proxy(renames["DurationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StepOut"])
    types["TestCaseIn"] = t.struct(
        {
            "stackTraces": t.array(t.proxy(renames["StackTraceIn"])).optional(),
            "skippedMessage": t.string().optional(),
            "startTime": t.proxy(renames["TimestampIn"]).optional(),
            "status": t.string().optional(),
            "testCaseReference": t.proxy(renames["TestCaseReferenceIn"]).optional(),
            "elapsedTime": t.proxy(renames["DurationIn"]).optional(),
            "endTime": t.proxy(renames["TimestampIn"]).optional(),
            "testCaseId": t.string().optional(),
            "toolOutputs": t.array(
                t.proxy(renames["ToolOutputReferenceIn"])
            ).optional(),
        }
    ).named(renames["TestCaseIn"])
    types["TestCaseOut"] = t.struct(
        {
            "stackTraces": t.array(t.proxy(renames["StackTraceOut"])).optional(),
            "skippedMessage": t.string().optional(),
            "startTime": t.proxy(renames["TimestampOut"]).optional(),
            "status": t.string().optional(),
            "testCaseReference": t.proxy(renames["TestCaseReferenceOut"]).optional(),
            "elapsedTime": t.proxy(renames["DurationOut"]).optional(),
            "endTime": t.proxy(renames["TimestampOut"]).optional(),
            "testCaseId": t.string().optional(),
            "toolOutputs": t.array(
                t.proxy(renames["ToolOutputReferenceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestCaseOut"])
    types["SuggestionProtoIn"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "longMessage": t.proxy(renames["SafeHtmlProtoIn"]).optional(),
            "secondaryPriority": t.number().optional(),
            "screenId": t.string().optional(),
            "pseudoResourceId": t.string().optional(),
            "region": t.proxy(renames["RegionProtoIn"]).optional(),
            "shortMessage": t.proxy(renames["SafeHtmlProtoIn"]).optional(),
            "priority": t.string().optional(),
            "title": t.string().optional(),
            "helpUrl": t.string().optional(),
        }
    ).named(renames["SuggestionProtoIn"])
    types["SuggestionProtoOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "longMessage": t.proxy(renames["SafeHtmlProtoOut"]).optional(),
            "secondaryPriority": t.number().optional(),
            "screenId": t.string().optional(),
            "pseudoResourceId": t.string().optional(),
            "region": t.proxy(renames["RegionProtoOut"]).optional(),
            "shortMessage": t.proxy(renames["SafeHtmlProtoOut"]).optional(),
            "priority": t.string().optional(),
            "title": t.string().optional(),
            "helpUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestionProtoOut"])
    types["ProjectSettingsIn"] = t.struct(
        {"defaultBucket": t.string().optional(), "name": t.string().optional()}
    ).named(renames["ProjectSettingsIn"])
    types["ProjectSettingsOut"] = t.struct(
        {
            "defaultBucket": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectSettingsOut"])
    types["IndividualOutcomeIn"] = t.struct(
        {
            "outcomeSummary": t.string(),
            "runDuration": t.proxy(renames["DurationIn"]).optional(),
            "stepId": t.string(),
            "multistepNumber": t.integer().optional(),
        }
    ).named(renames["IndividualOutcomeIn"])
    types["IndividualOutcomeOut"] = t.struct(
        {
            "outcomeSummary": t.string(),
            "runDuration": t.proxy(renames["DurationOut"]).optional(),
            "stepId": t.string(),
            "multistepNumber": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndividualOutcomeOut"])
    types["IosTestLoopIn"] = t.struct({"bundleId": t.string().optional()}).named(
        renames["IosTestLoopIn"]
    )
    types["IosTestLoopOut"] = t.struct(
        {
            "bundleId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosTestLoopOut"])
    types["StartActivityNotFoundIn"] = t.struct(
        {"uri": t.string(), "action": t.string()}
    ).named(renames["StartActivityNotFoundIn"])
    types["StartActivityNotFoundOut"] = t.struct(
        {
            "uri": t.string(),
            "action": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartActivityNotFoundOut"])
    types["ThumbnailIn"] = t.struct(
        {
            "widthPx": t.integer().optional(),
            "data": t.string().optional(),
            "heightPx": t.integer().optional(),
            "contentType": t.string().optional(),
        }
    ).named(renames["ThumbnailIn"])
    types["ThumbnailOut"] = t.struct(
        {
            "widthPx": t.integer().optional(),
            "data": t.string().optional(),
            "heightPx": t.integer().optional(),
            "contentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThumbnailOut"])
    types["OutcomeIn"] = t.struct(
        {
            "skippedDetail": t.proxy(renames["SkippedDetailIn"]).optional(),
            "successDetail": t.proxy(renames["SuccessDetailIn"]).optional(),
            "summary": t.string().optional(),
            "inconclusiveDetail": t.proxy(renames["InconclusiveDetailIn"]).optional(),
            "failureDetail": t.proxy(renames["FailureDetailIn"]).optional(),
        }
    ).named(renames["OutcomeIn"])
    types["OutcomeOut"] = t.struct(
        {
            "skippedDetail": t.proxy(renames["SkippedDetailOut"]).optional(),
            "successDetail": t.proxy(renames["SuccessDetailOut"]).optional(),
            "summary": t.string().optional(),
            "inconclusiveDetail": t.proxy(renames["InconclusiveDetailOut"]).optional(),
            "failureDetail": t.proxy(renames["FailureDetailOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutcomeOut"])
    types["ToolExecutionIn"] = t.struct(
        {
            "exitCode": t.proxy(renames["ToolExitCodeIn"]).optional(),
            "toolLogs": t.array(t.proxy(renames["FileReferenceIn"])).optional(),
            "toolOutputs": t.array(
                t.proxy(renames["ToolOutputReferenceIn"])
            ).optional(),
            "commandLineArguments": t.array(t.string()).optional(),
        }
    ).named(renames["ToolExecutionIn"])
    types["ToolExecutionOut"] = t.struct(
        {
            "exitCode": t.proxy(renames["ToolExitCodeOut"]).optional(),
            "toolLogs": t.array(t.proxy(renames["FileReferenceOut"])).optional(),
            "toolOutputs": t.array(
                t.proxy(renames["ToolOutputReferenceOut"])
            ).optional(),
            "commandLineArguments": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ToolExecutionOut"])
    types["BatchCreatePerfSamplesResponseIn"] = t.struct(
        {"perfSamples": t.array(t.proxy(renames["PerfSampleIn"]))}
    ).named(renames["BatchCreatePerfSamplesResponseIn"])
    types["BatchCreatePerfSamplesResponseOut"] = t.struct(
        {
            "perfSamples": t.array(t.proxy(renames["PerfSampleOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreatePerfSamplesResponseOut"])
    types["ToolExecutionStepIn"] = t.struct(
        {"toolExecution": t.proxy(renames["ToolExecutionIn"]).optional()}
    ).named(renames["ToolExecutionStepIn"])
    types["ToolExecutionStepOut"] = t.struct(
        {
            "toolExecution": t.proxy(renames["ToolExecutionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ToolExecutionStepOut"])
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
    types["EncounteredNonAndroidUiWidgetScreenIn"] = t.struct(
        {
            "distinctScreens": t.integer().optional(),
            "screenIds": t.array(t.string()).optional(),
        }
    ).named(renames["EncounteredNonAndroidUiWidgetScreenIn"])
    types["EncounteredNonAndroidUiWidgetScreenOut"] = t.struct(
        {
            "distinctScreens": t.integer().optional(),
            "screenIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncounteredNonAndroidUiWidgetScreenOut"])
    types["UnusedRoboDirectiveIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["UnusedRoboDirectiveIn"])
    types["UnusedRoboDirectiveOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnusedRoboDirectiveOut"])
    types["ScreenshotClusterIn"] = t.struct(
        {
            "keyScreen": t.proxy(renames["ScreenIn"]).optional(),
            "clusterId": t.string().optional(),
            "activity": t.string().optional(),
            "screens": t.array(t.proxy(renames["ScreenIn"])).optional(),
        }
    ).named(renames["ScreenshotClusterIn"])
    types["ScreenshotClusterOut"] = t.struct(
        {
            "keyScreen": t.proxy(renames["ScreenOut"]).optional(),
            "clusterId": t.string().optional(),
            "activity": t.string().optional(),
            "screens": t.array(t.proxy(renames["ScreenOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScreenshotClusterOut"])
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
    types["BatchCreatePerfSamplesRequestIn"] = t.struct(
        {"perfSamples": t.array(t.proxy(renames["PerfSampleIn"])).optional()}
    ).named(renames["BatchCreatePerfSamplesRequestIn"])
    types["BatchCreatePerfSamplesRequestOut"] = t.struct(
        {
            "perfSamples": t.array(t.proxy(renames["PerfSampleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreatePerfSamplesRequestOut"])
    types["ImageIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "stepId": t.string().optional(),
            "thumbnail": t.proxy(renames["ThumbnailIn"]).optional(),
            "sourceImage": t.proxy(renames["ToolOutputReferenceIn"]).optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "stepId": t.string().optional(),
            "thumbnail": t.proxy(renames["ThumbnailOut"]).optional(),
            "sourceImage": t.proxy(renames["ToolOutputReferenceOut"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["NonSdkApiUsageViolationReportIn"] = t.struct(
        {
            "targetSdkVersion": t.integer().optional(),
            "exampleApis": t.array(t.proxy(renames["NonSdkApiIn"])).optional(),
            "minSdkVersion": t.integer().optional(),
            "uniqueApis": t.integer().optional(),
        }
    ).named(renames["NonSdkApiUsageViolationReportIn"])
    types["NonSdkApiUsageViolationReportOut"] = t.struct(
        {
            "targetSdkVersion": t.integer().optional(),
            "exampleApis": t.array(t.proxy(renames["NonSdkApiOut"])).optional(),
            "minSdkVersion": t.integer().optional(),
            "uniqueApis": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonSdkApiUsageViolationReportOut"])
    types["TestSuiteOverviewIn"] = t.struct(
        {
            "totalCount": t.integer().optional(),
            "xmlSource": t.proxy(renames["FileReferenceIn"]).optional(),
            "skippedCount": t.integer().optional(),
            "flakyCount": t.integer().optional(),
            "name": t.string().optional(),
            "failureCount": t.integer().optional(),
            "elapsedTime": t.proxy(renames["DurationIn"]).optional(),
            "errorCount": t.integer().optional(),
        }
    ).named(renames["TestSuiteOverviewIn"])
    types["TestSuiteOverviewOut"] = t.struct(
        {
            "totalCount": t.integer().optional(),
            "xmlSource": t.proxy(renames["FileReferenceOut"]).optional(),
            "skippedCount": t.integer().optional(),
            "flakyCount": t.integer().optional(),
            "name": t.string().optional(),
            "failureCount": t.integer().optional(),
            "elapsedTime": t.proxy(renames["DurationOut"]).optional(),
            "errorCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestSuiteOverviewOut"])
    types["NonSdkApiUsageViolationIn"] = t.struct(
        {
            "uniqueApis": t.integer().optional(),
            "apiSignatures": t.array(t.string()).optional(),
        }
    ).named(renames["NonSdkApiUsageViolationIn"])
    types["NonSdkApiUsageViolationOut"] = t.struct(
        {
            "uniqueApis": t.integer().optional(),
            "apiSignatures": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonSdkApiUsageViolationOut"])
    types["RoboScriptExecutionIn"] = t.struct(
        {
            "successfulActions": t.integer().optional(),
            "totalActions": t.integer().optional(),
        }
    ).named(renames["RoboScriptExecutionIn"])
    types["RoboScriptExecutionOut"] = t.struct(
        {
            "successfulActions": t.integer().optional(),
            "totalActions": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RoboScriptExecutionOut"])
    types["UsedRoboDirectiveIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["UsedRoboDirectiveIn"])
    types["UsedRoboDirectiveOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsedRoboDirectiveOut"])
    types["ANRIn"] = t.struct(
        {"stackTrace": t.proxy(renames["StackTraceIn"]).optional()}
    ).named(renames["ANRIn"])
    types["ANROut"] = t.struct(
        {
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ANROut"])
    types["PerfSampleSeriesIn"] = t.struct(
        {
            "basicPerfSampleSeries": t.proxy(
                renames["BasicPerfSampleSeriesIn"]
            ).optional(),
            "executionId": t.string().optional(),
            "projectId": t.string().optional(),
            "sampleSeriesId": t.string().optional(),
            "stepId": t.string().optional(),
            "historyId": t.string().optional(),
        }
    ).named(renames["PerfSampleSeriesIn"])
    types["PerfSampleSeriesOut"] = t.struct(
        {
            "basicPerfSampleSeries": t.proxy(
                renames["BasicPerfSampleSeriesOut"]
            ).optional(),
            "executionId": t.string().optional(),
            "projectId": t.string().optional(),
            "sampleSeriesId": t.string().optional(),
            "stepId": t.string().optional(),
            "historyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerfSampleSeriesOut"])
    types["TimestampIn"] = t.struct(
        {"seconds": t.string().optional(), "nanos": t.integer().optional()}
    ).named(renames["TimestampIn"])
    types["TimestampOut"] = t.struct(
        {
            "seconds": t.string().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimestampOut"])
    types["FailureDetailIn"] = t.struct(
        {
            "unableToCrawl": t.boolean().optional(),
            "notInstalled": t.boolean().optional(),
            "otherNativeCrash": t.boolean().optional(),
            "crashed": t.boolean().optional(),
            "failedRoboscript": t.boolean().optional(),
            "deviceOutOfMemory": t.boolean().optional(),
            "timedOut": t.boolean().optional(),
        }
    ).named(renames["FailureDetailIn"])
    types["FailureDetailOut"] = t.struct(
        {
            "unableToCrawl": t.boolean().optional(),
            "notInstalled": t.boolean().optional(),
            "otherNativeCrash": t.boolean().optional(),
            "crashed": t.boolean().optional(),
            "failedRoboscript": t.boolean().optional(),
            "deviceOutOfMemory": t.boolean().optional(),
            "timedOut": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FailureDetailOut"])
    types["DetectedAppSplashScreenIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DetectedAppSplashScreenIn"]
    )
    types["DetectedAppSplashScreenOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DetectedAppSplashScreenOut"])
    types["IosTestIn"] = t.struct(
        {
            "testTimeout": t.proxy(renames["DurationIn"]).optional(),
            "iosRoboTest": t.proxy(renames["IosRoboTestIn"]).optional(),
            "iosAppInfo": t.proxy(renames["IosAppInfoIn"]).optional(),
            "iosXcTest": t.proxy(renames["IosXcTestIn"]).optional(),
            "iosTestLoop": t.proxy(renames["IosTestLoopIn"]).optional(),
        }
    ).named(renames["IosTestIn"])
    types["IosTestOut"] = t.struct(
        {
            "testTimeout": t.proxy(renames["DurationOut"]).optional(),
            "iosRoboTest": t.proxy(renames["IosRoboTestOut"]).optional(),
            "iosAppInfo": t.proxy(renames["IosAppInfoOut"]).optional(),
            "iosXcTest": t.proxy(renames["IosXcTestOut"]).optional(),
            "iosTestLoop": t.proxy(renames["IosTestLoopOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosTestOut"])
    types["LauncherActivityNotFoundIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LauncherActivityNotFoundIn"]
    )
    types["LauncherActivityNotFoundOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LauncherActivityNotFoundOut"])
    types["InconclusiveDetailIn"] = t.struct(
        {
            "infrastructureFailure": t.boolean().optional(),
            "abortedByUser": t.boolean().optional(),
            "hasErrorLogs": t.boolean().optional(),
        }
    ).named(renames["InconclusiveDetailIn"])
    types["InconclusiveDetailOut"] = t.struct(
        {
            "infrastructureFailure": t.boolean().optional(),
            "abortedByUser": t.boolean().optional(),
            "hasErrorLogs": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InconclusiveDetailOut"])
    types["ScreenIn"] = t.struct(
        {
            "version": t.string().optional(),
            "locale": t.string().optional(),
            "fileReference": t.string().optional(),
            "model": t.string().optional(),
        }
    ).named(renames["ScreenIn"])
    types["ScreenOut"] = t.struct(
        {
            "version": t.string().optional(),
            "locale": t.string().optional(),
            "fileReference": t.string().optional(),
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScreenOut"])
    types["NonSdkApiInsightIn"] = t.struct(
        {
            "exampleTraceMessages": t.array(t.string()).optional(),
            "pendingGoogleUpdateInsight": t.proxy(
                renames["PendingGoogleUpdateInsightIn"]
            ).optional(),
            "matcherId": t.string().optional(),
            "upgradeInsight": t.proxy(renames["UpgradeInsightIn"]).optional(),
        }
    ).named(renames["NonSdkApiInsightIn"])
    types["NonSdkApiInsightOut"] = t.struct(
        {
            "exampleTraceMessages": t.array(t.string()).optional(),
            "pendingGoogleUpdateInsight": t.proxy(
                renames["PendingGoogleUpdateInsightOut"]
            ).optional(),
            "matcherId": t.string().optional(),
            "upgradeInsight": t.proxy(renames["UpgradeInsightOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonSdkApiInsightOut"])
    types["EnvironmentIn"] = t.struct(
        {
            "creationTime": t.proxy(renames["TimestampIn"]).optional(),
            "shardSummaries": t.array(t.proxy(renames["ShardSummaryIn"])).optional(),
            "environmentId": t.string().optional(),
            "completionTime": t.proxy(renames["TimestampIn"]).optional(),
            "executionId": t.string().optional(),
            "historyId": t.string().optional(),
            "environmentResult": t.proxy(renames["MergedResultIn"]).optional(),
            "displayName": t.string().optional(),
            "projectId": t.string().optional(),
            "resultsStorage": t.proxy(renames["ResultsStorageIn"]).optional(),
            "dimensionValue": t.array(
                t.proxy(renames["EnvironmentDimensionValueEntryIn"])
            ).optional(),
        }
    ).named(renames["EnvironmentIn"])
    types["EnvironmentOut"] = t.struct(
        {
            "creationTime": t.proxy(renames["TimestampOut"]).optional(),
            "shardSummaries": t.array(t.proxy(renames["ShardSummaryOut"])).optional(),
            "environmentId": t.string().optional(),
            "completionTime": t.proxy(renames["TimestampOut"]).optional(),
            "executionId": t.string().optional(),
            "historyId": t.string().optional(),
            "environmentResult": t.proxy(renames["MergedResultOut"]).optional(),
            "displayName": t.string().optional(),
            "projectId": t.string().optional(),
            "resultsStorage": t.proxy(renames["ResultsStorageOut"]).optional(),
            "dimensionValue": t.array(
                t.proxy(renames["EnvironmentDimensionValueEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentOut"])
    types["AndroidAppInfoIn"] = t.struct(
        {
            "versionName": t.string().optional(),
            "name": t.string().optional(),
            "packageName": t.string().optional(),
            "versionCode": t.string().optional(),
        }
    ).named(renames["AndroidAppInfoIn"])
    types["AndroidAppInfoOut"] = t.struct(
        {
            "versionName": t.string().optional(),
            "name": t.string().optional(),
            "packageName": t.string().optional(),
            "versionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidAppInfoOut"])
    types["AppStartTimeIn"] = t.struct(
        {
            "initialDisplayTime": t.proxy(renames["DurationIn"]).optional(),
            "fullyDrawnTime": t.proxy(renames["DurationIn"]).optional(),
        }
    ).named(renames["AppStartTimeIn"])
    types["AppStartTimeOut"] = t.struct(
        {
            "initialDisplayTime": t.proxy(renames["DurationOut"]).optional(),
            "fullyDrawnTime": t.proxy(renames["DurationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppStartTimeOut"])
    types["ListStepThumbnailsResponseIn"] = t.struct(
        {
            "thumbnails": t.array(t.proxy(renames["ImageIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListStepThumbnailsResponseIn"])
    types["ListStepThumbnailsResponseOut"] = t.struct(
        {
            "thumbnails": t.array(t.proxy(renames["ImageOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListStepThumbnailsResponseOut"])
    types["IosAppCrashedIn"] = t.struct(
        {"stackTrace": t.proxy(renames["StackTraceIn"]).optional()}
    ).named(renames["IosAppCrashedIn"])
    types["IosAppCrashedOut"] = t.struct(
        {
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosAppCrashedOut"])
    types["UIElementTooDeepIn"] = t.struct(
        {
            "depth": t.integer().optional(),
            "screenStateId": t.string().optional(),
            "screenId": t.string().optional(),
        }
    ).named(renames["UIElementTooDeepIn"])
    types["UIElementTooDeepOut"] = t.struct(
        {
            "depth": t.integer().optional(),
            "screenStateId": t.string().optional(),
            "screenId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UIElementTooDeepOut"])
    types["MergedResultIn"] = t.struct(
        {
            "outcome": t.proxy(renames["OutcomeIn"]).optional(),
            "state": t.string().optional(),
            "testSuiteOverviews": t.array(
                t.proxy(renames["TestSuiteOverviewIn"])
            ).optional(),
        }
    ).named(renames["MergedResultIn"])
    types["MergedResultOut"] = t.struct(
        {
            "outcome": t.proxy(renames["OutcomeOut"]).optional(),
            "state": t.string().optional(),
            "testSuiteOverviews": t.array(
                t.proxy(renames["TestSuiteOverviewOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MergedResultOut"])
    types["SuccessDetailIn"] = t.struct(
        {"otherNativeCrash": t.boolean().optional()}
    ).named(renames["SuccessDetailIn"])
    types["SuccessDetailOut"] = t.struct(
        {
            "otherNativeCrash": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuccessDetailOut"])
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
    types["PendingGoogleUpdateInsightIn"] = t.struct(
        {"nameOfGoogleLibrary": t.string().optional()}
    ).named(renames["PendingGoogleUpdateInsightIn"])
    types["PendingGoogleUpdateInsightOut"] = t.struct(
        {
            "nameOfGoogleLibrary": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PendingGoogleUpdateInsightOut"])
    types["UnspecifiedWarningIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UnspecifiedWarningIn"]
    )
    types["UnspecifiedWarningOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UnspecifiedWarningOut"])
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
    types["SpecificationIn"] = t.struct(
        {
            "androidTest": t.proxy(renames["AndroidTestIn"]).optional(),
            "iosTest": t.proxy(renames["IosTestIn"]).optional(),
        }
    ).named(renames["SpecificationIn"])
    types["SpecificationOut"] = t.struct(
        {
            "androidTest": t.proxy(renames["AndroidTestOut"]).optional(),
            "iosTest": t.proxy(renames["IosTestOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpecificationOut"])
    types["ExecutionIn"] = t.struct(
        {
            "completionTime": t.proxy(renames["TimestampIn"]).optional(),
            "specification": t.proxy(renames["SpecificationIn"]).optional(),
            "dimensionDefinitions": t.array(
                t.proxy(renames["MatrixDimensionDefinitionIn"])
            ).optional(),
            "executionId": t.string().optional(),
            "testExecutionMatrixId": t.string().optional(),
            "outcome": t.proxy(renames["OutcomeIn"]).optional(),
            "creationTime": t.proxy(renames["TimestampIn"]).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["ExecutionIn"])
    types["ExecutionOut"] = t.struct(
        {
            "completionTime": t.proxy(renames["TimestampOut"]).optional(),
            "specification": t.proxy(renames["SpecificationOut"]).optional(),
            "dimensionDefinitions": t.array(
                t.proxy(renames["MatrixDimensionDefinitionOut"])
            ).optional(),
            "executionId": t.string().optional(),
            "testExecutionMatrixId": t.string().optional(),
            "outcome": t.proxy(renames["OutcomeOut"]).optional(),
            "creationTime": t.proxy(renames["TimestampOut"]).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionOut"])
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
    types["CPUInfoIn"] = t.struct(
        {
            "cpuSpeedInGhz": t.number().optional(),
            "numberOfCores": t.integer().optional(),
            "cpuProcessor": t.string().optional(),
        }
    ).named(renames["CPUInfoIn"])
    types["CPUInfoOut"] = t.struct(
        {
            "cpuSpeedInGhz": t.number().optional(),
            "numberOfCores": t.integer().optional(),
            "cpuProcessor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CPUInfoOut"])
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
    types["AndroidRoboTestIn"] = t.struct(
        {
            "maxDepth": t.integer().optional(),
            "bootstrapPackageId": t.string().optional(),
            "appInitialActivity": t.string().optional(),
            "maxSteps": t.integer().optional(),
            "bootstrapRunnerClass": t.string().optional(),
        }
    ).named(renames["AndroidRoboTestIn"])
    types["AndroidRoboTestOut"] = t.struct(
        {
            "maxDepth": t.integer().optional(),
            "bootstrapPackageId": t.string().optional(),
            "appInitialActivity": t.string().optional(),
            "maxSteps": t.integer().optional(),
            "bootstrapRunnerClass": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidRoboTestOut"])
    types["ListExecutionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "executions": t.array(t.proxy(renames["ExecutionIn"])).optional(),
        }
    ).named(renames["ListExecutionsResponseIn"])
    types["ListExecutionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "executions": t.array(t.proxy(renames["ExecutionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListExecutionsResponseOut"])
    types["IosRoboTestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["IosRoboTestIn"]
    )
    types["IosRoboTestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["IosRoboTestOut"])
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
    types["TestIssueIn"] = t.struct(
        {
            "category": t.string().optional(),
            "type": t.string().optional(),
            "errorMessage": t.string().optional(),
            "warning": t.proxy(renames["AnyIn"]).optional(),
            "stackTrace": t.proxy(renames["StackTraceIn"]).optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["TestIssueIn"])
    types["TestIssueOut"] = t.struct(
        {
            "category": t.string().optional(),
            "type": t.string().optional(),
            "errorMessage": t.string().optional(),
            "warning": t.proxy(renames["AnyOut"]).optional(),
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIssueOut"])
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
    types["ShardSummaryIn"] = t.struct(
        {
            "shardResult": t.proxy(renames["MergedResultIn"]).optional(),
            "runs": t.array(t.proxy(renames["StepSummaryIn"])).optional(),
        }
    ).named(renames["ShardSummaryIn"])
    types["ShardSummaryOut"] = t.struct(
        {
            "shardResult": t.proxy(renames["MergedResultOut"]).optional(),
            "runs": t.array(t.proxy(renames["StepSummaryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShardSummaryOut"])
    types["MatrixDimensionDefinitionIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MatrixDimensionDefinitionIn"]
    )
    types["MatrixDimensionDefinitionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MatrixDimensionDefinitionOut"])
    types["EncounteredLoginScreenIn"] = t.struct(
        {
            "screenIds": t.array(t.string()).optional(),
            "distinctScreens": t.integer().optional(),
        }
    ).named(renames["EncounteredLoginScreenIn"])
    types["EncounteredLoginScreenOut"] = t.struct(
        {
            "screenIds": t.array(t.string()).optional(),
            "distinctScreens": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncounteredLoginScreenOut"])
    types["PerformedGoogleLoginIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PerformedGoogleLoginIn"]
    )
    types["PerformedGoogleLoginOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PerformedGoogleLoginOut"])
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
    types["MultiStepIn"] = t.struct(
        {
            "primaryStepId": t.string().optional(),
            "primaryStep": t.proxy(renames["PrimaryStepIn"]).optional(),
            "multistepNumber": t.integer().optional(),
        }
    ).named(renames["MultiStepIn"])
    types["MultiStepOut"] = t.struct(
        {
            "primaryStepId": t.string().optional(),
            "primaryStep": t.proxy(renames["PrimaryStepOut"]).optional(),
            "multistepNumber": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultiStepOut"])
    types["AvailableDeepLinksIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AvailableDeepLinksIn"]
    )
    types["AvailableDeepLinksOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AvailableDeepLinksOut"])
    types["AndroidTestLoopIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AndroidTestLoopIn"]
    )
    types["AndroidTestLoopOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AndroidTestLoopOut"])
    types["TestCaseReferenceIn"] = t.struct(
        {
            "testSuiteName": t.string().optional(),
            "name": t.string().optional(),
            "className": t.string().optional(),
        }
    ).named(renames["TestCaseReferenceIn"])
    types["TestCaseReferenceOut"] = t.struct(
        {
            "testSuiteName": t.string().optional(),
            "name": t.string().optional(),
            "className": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestCaseReferenceOut"])
    types["BlankScreenIn"] = t.struct({"screenId": t.string().optional()}).named(
        renames["BlankScreenIn"]
    )
    types["BlankScreenOut"] = t.struct(
        {
            "screenId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BlankScreenOut"])
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
    types["ListScreenshotClustersResponseIn"] = t.struct(
        {"clusters": t.array(t.proxy(renames["ScreenshotClusterIn"])).optional()}
    ).named(renames["ListScreenshotClustersResponseIn"])
    types["ListScreenshotClustersResponseOut"] = t.struct(
        {
            "clusters": t.array(t.proxy(renames["ScreenshotClusterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListScreenshotClustersResponseOut"])
    types["NonSdkApiIn"] = t.struct(
        {
            "list": t.string().optional(),
            "insights": t.array(t.proxy(renames["NonSdkApiInsightIn"])).optional(),
            "exampleStackTraces": t.array(t.string()).optional(),
            "invocationCount": t.integer().optional(),
            "apiSignature": t.string().optional(),
        }
    ).named(renames["NonSdkApiIn"])
    types["NonSdkApiOut"] = t.struct(
        {
            "list": t.string().optional(),
            "insights": t.array(t.proxy(renames["NonSdkApiInsightOut"])).optional(),
            "exampleStackTraces": t.array(t.string()).optional(),
            "invocationCount": t.integer().optional(),
            "apiSignature": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonSdkApiOut"])
    types["StackTraceIn"] = t.struct({"exception": t.string().optional()}).named(
        renames["StackTraceIn"]
    )
    types["StackTraceOut"] = t.struct(
        {
            "exception": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackTraceOut"])
    types["TestExecutionStepIn"] = t.struct(
        {
            "testTiming": t.proxy(renames["TestTimingIn"]).optional(),
            "testIssues": t.array(t.proxy(renames["TestIssueIn"])).optional(),
            "testSuiteOverviews": t.array(
                t.proxy(renames["TestSuiteOverviewIn"])
            ).optional(),
            "toolExecution": t.proxy(renames["ToolExecutionIn"]).optional(),
        }
    ).named(renames["TestExecutionStepIn"])
    types["TestExecutionStepOut"] = t.struct(
        {
            "testTiming": t.proxy(renames["TestTimingOut"]).optional(),
            "testIssues": t.array(t.proxy(renames["TestIssueOut"])).optional(),
            "testSuiteOverviews": t.array(
                t.proxy(renames["TestSuiteOverviewOut"])
            ).optional(),
            "toolExecution": t.proxy(renames["ToolExecutionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestExecutionStepOut"])
    types["ToolOutputReferenceIn"] = t.struct(
        {
            "output": t.proxy(renames["FileReferenceIn"]).optional(),
            "creationTime": t.proxy(renames["TimestampIn"]).optional(),
            "testCase": t.proxy(renames["TestCaseReferenceIn"]).optional(),
        }
    ).named(renames["ToolOutputReferenceIn"])
    types["ToolOutputReferenceOut"] = t.struct(
        {
            "output": t.proxy(renames["FileReferenceOut"]).optional(),
            "creationTime": t.proxy(renames["TimestampOut"]).optional(),
            "testCase": t.proxy(renames["TestCaseReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ToolOutputReferenceOut"])
    types["StepSummaryIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StepSummaryIn"]
    )
    types["StepSummaryOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StepSummaryOut"])
    types["ResultsStorageIn"] = t.struct(
        {
            "resultsStoragePath": t.proxy(renames["FileReferenceIn"]).optional(),
            "xunitXmlFile": t.proxy(renames["FileReferenceIn"]).optional(),
        }
    ).named(renames["ResultsStorageIn"])
    types["ResultsStorageOut"] = t.struct(
        {
            "resultsStoragePath": t.proxy(renames["FileReferenceOut"]).optional(),
            "xunitXmlFile": t.proxy(renames["FileReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultsStorageOut"])
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
    types["DeviceOutOfMemoryIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeviceOutOfMemoryIn"]
    )
    types["DeviceOutOfMemoryOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeviceOutOfMemoryOut"])
    types["ListTestCasesResponseIn"] = t.struct(
        {
            "testCases": t.array(t.proxy(renames["TestCaseIn"])).optional(),
            "nextPageToken": t.string(),
        }
    ).named(renames["ListTestCasesResponseIn"])
    types["ListTestCasesResponseOut"] = t.struct(
        {
            "testCases": t.array(t.proxy(renames["TestCaseOut"])).optional(),
            "nextPageToken": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTestCasesResponseOut"])
    types["LogcatCollectionErrorIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LogcatCollectionErrorIn"]
    )
    types["LogcatCollectionErrorOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LogcatCollectionErrorOut"])
    types["ToolExitCodeIn"] = t.struct({"number": t.integer().optional()}).named(
        renames["ToolExitCodeIn"]
    )
    types["ToolExitCodeOut"] = t.struct(
        {
            "number": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ToolExitCodeOut"])
    types["GraphicsStatsIn"] = t.struct(
        {
            "totalFrames": t.string().optional(),
            "p90Millis": t.string().optional(),
            "slowBitmapUploadCount": t.string().optional(),
            "p99Millis": t.string().optional(),
            "slowDrawCount": t.string().optional(),
            "p95Millis": t.string().optional(),
            "p50Millis": t.string().optional(),
            "buckets": t.array(t.proxy(renames["GraphicsStatsBucketIn"])).optional(),
            "slowUiThreadCount": t.string().optional(),
            "jankyFrames": t.string().optional(),
            "missedVsyncCount": t.string().optional(),
            "highInputLatencyCount": t.string().optional(),
        }
    ).named(renames["GraphicsStatsIn"])
    types["GraphicsStatsOut"] = t.struct(
        {
            "totalFrames": t.string().optional(),
            "p90Millis": t.string().optional(),
            "slowBitmapUploadCount": t.string().optional(),
            "p99Millis": t.string().optional(),
            "slowDrawCount": t.string().optional(),
            "p95Millis": t.string().optional(),
            "p50Millis": t.string().optional(),
            "buckets": t.array(t.proxy(renames["GraphicsStatsBucketOut"])).optional(),
            "slowUiThreadCount": t.string().optional(),
            "jankyFrames": t.string().optional(),
            "missedVsyncCount": t.string().optional(),
            "highInputLatencyCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GraphicsStatsOut"])
    types["HistoryIn"] = t.struct(
        {
            "name": t.string().optional(),
            "testPlatform": t.string().optional(),
            "historyId": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["HistoryIn"])
    types["HistoryOut"] = t.struct(
        {
            "name": t.string().optional(),
            "testPlatform": t.string().optional(),
            "historyId": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistoryOut"])
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
    types["ListStepAccessibilityClustersResponseIn"] = t.struct(
        {
            "clusters": t.array(
                t.proxy(renames["SuggestionClusterProtoIn"])
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ListStepAccessibilityClustersResponseIn"])
    types["ListStepAccessibilityClustersResponseOut"] = t.struct(
        {
            "clusters": t.array(
                t.proxy(renames["SuggestionClusterProtoOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListStepAccessibilityClustersResponseOut"])
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
    types["CrashDialogErrorIn"] = t.struct(
        {"crashPackage": t.string().optional()}
    ).named(renames["CrashDialogErrorIn"])
    types["CrashDialogErrorOut"] = t.struct(
        {
            "crashPackage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CrashDialogErrorOut"])
    types["FileReferenceIn"] = t.struct({"fileUri": t.string().optional()}).named(
        renames["FileReferenceIn"]
    )
    types["FileReferenceOut"] = t.struct(
        {
            "fileUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileReferenceOut"])
    types["AnyIn"] = t.struct(
        {"value": t.string().optional(), "typeUrl": t.string().optional()}
    ).named(renames["AnyIn"])
    types["AnyOut"] = t.struct(
        {
            "value": t.string().optional(),
            "typeUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnyOut"])
    types["DurationIn"] = t.struct(
        {"nanos": t.integer().optional(), "seconds": t.string().optional()}
    ).named(renames["DurationIn"])
    types["DurationOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "seconds": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DurationOut"])
    types["NativeCrashIn"] = t.struct(
        {"stackTrace": t.proxy(renames["StackTraceIn"]).optional()}
    ).named(renames["NativeCrashIn"])
    types["NativeCrashOut"] = t.struct(
        {
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NativeCrashOut"])
    types["RegionProtoIn"] = t.struct(
        {
            "widthPx": t.integer().optional(),
            "topPx": t.integer().optional(),
            "heightPx": t.integer().optional(),
            "leftPx": t.integer().optional(),
        }
    ).named(renames["RegionProtoIn"])
    types["RegionProtoOut"] = t.struct(
        {
            "widthPx": t.integer().optional(),
            "topPx": t.integer().optional(),
            "heightPx": t.integer().optional(),
            "leftPx": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionProtoOut"])
    types["SafeHtmlProtoIn"] = t.struct(
        {"privateDoNotAccessOrElseSafeHtmlWrappedValue": t.string().optional()}
    ).named(renames["SafeHtmlProtoIn"])
    types["SafeHtmlProtoOut"] = t.struct(
        {
            "privateDoNotAccessOrElseSafeHtmlWrappedValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SafeHtmlProtoOut"])
    types["PublishXunitXmlFilesRequestIn"] = t.struct(
        {"xunitXmlFiles": t.array(t.proxy(renames["FileReferenceIn"])).optional()}
    ).named(renames["PublishXunitXmlFilesRequestIn"])
    types["PublishXunitXmlFilesRequestOut"] = t.struct(
        {
            "xunitXmlFiles": t.array(t.proxy(renames["FileReferenceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishXunitXmlFilesRequestOut"])
    types["PerformedMonkeyActionsIn"] = t.struct(
        {"totalActions": t.integer().optional()}
    ).named(renames["PerformedMonkeyActionsIn"])
    types["PerformedMonkeyActionsOut"] = t.struct(
        {
            "totalActions": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerformedMonkeyActionsOut"])
    types["ListHistoriesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "histories": t.array(t.proxy(renames["HistoryIn"])).optional(),
        }
    ).named(renames["ListHistoriesResponseIn"])
    types["ListHistoriesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "histories": t.array(t.proxy(renames["HistoryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListHistoriesResponseOut"])
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
    types["TestTimingIn"] = t.struct(
        {"testProcessDuration": t.proxy(renames["DurationIn"]).optional()}
    ).named(renames["TestTimingIn"])
    types["TestTimingOut"] = t.struct(
        {
            "testProcessDuration": t.proxy(renames["DurationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestTimingOut"])
    types["UsedRoboIgnoreDirectiveIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["UsedRoboIgnoreDirectiveIn"])
    types["UsedRoboIgnoreDirectiveOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsedRoboIgnoreDirectiveOut"])

    functions = {}
    functions["projectsGetSettings"] = toolresults.post(
        "toolresults/v1beta3/projects/{projectId}:initializeSettings",
        t.struct({"projectId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ProjectSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInitializeSettings"] = toolresults.post(
        "toolresults/v1beta3/projects/{projectId}:initializeSettings",
        t.struct({"projectId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ProjectSettingsOut"]),
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
    functions["projectsHistoriesExecutionsCreate"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "historyId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExecutionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsPatch"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "historyId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExecutionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsGet"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "historyId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExecutionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsList"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "historyId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExecutionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsEnvironmentsList"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/environments/{environmentId}",
        t.struct(
            {
                "projectId": t.string(),
                "historyId": t.string(),
                "environmentId": t.string(),
                "executionId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsEnvironmentsGet"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/environments/{environmentId}",
        t.struct(
            {
                "projectId": t.string(),
                "historyId": t.string(),
                "environmentId": t.string(),
                "executionId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsList"] = toolresults.post(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}:publishXunitXmlFiles",
        t.struct(
            {
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
                "stepId": t.string().optional(),
                "projectId": t.string().optional(),
                "xunitXmlFiles": t.array(
                    t.proxy(renames["FileReferenceIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StepOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsCreate"] = toolresults.post(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}:publishXunitXmlFiles",
        t.struct(
            {
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
                "stepId": t.string().optional(),
                "projectId": t.string().optional(),
                "xunitXmlFiles": t.array(
                    t.proxy(renames["FileReferenceIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StepOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsHistoriesExecutionsStepsAccessibilityClusters"
    ] = toolresults.post(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}:publishXunitXmlFiles",
        t.struct(
            {
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
                "stepId": t.string().optional(),
                "projectId": t.string().optional(),
                "xunitXmlFiles": t.array(
                    t.proxy(renames["FileReferenceIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StepOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsGet"] = toolresults.post(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}:publishXunitXmlFiles",
        t.struct(
            {
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
                "stepId": t.string().optional(),
                "projectId": t.string().optional(),
                "xunitXmlFiles": t.array(
                    t.proxy(renames["FileReferenceIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StepOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsPatch"] = toolresults.post(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}:publishXunitXmlFiles",
        t.struct(
            {
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
                "stepId": t.string().optional(),
                "projectId": t.string().optional(),
                "xunitXmlFiles": t.array(
                    t.proxy(renames["FileReferenceIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StepOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsHistoriesExecutionsStepsGetPerfMetricsSummary"
    ] = toolresults.post(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}:publishXunitXmlFiles",
        t.struct(
            {
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
                "stepId": t.string().optional(),
                "projectId": t.string().optional(),
                "xunitXmlFiles": t.array(
                    t.proxy(renames["FileReferenceIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StepOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsHistoriesExecutionsStepsPublishXunitXmlFiles"
    ] = toolresults.post(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}:publishXunitXmlFiles",
        t.struct(
            {
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
                "stepId": t.string().optional(),
                "projectId": t.string().optional(),
                "xunitXmlFiles": t.array(
                    t.proxy(renames["FileReferenceIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StepOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsTestCasesList"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/testCases/{testCaseId}",
        t.struct(
            {
                "testCaseId": t.string().optional(),
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
                "projectId": t.string().optional(),
                "stepId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestCaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsTestCasesGet"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/testCases/{testCaseId}",
        t.struct(
            {
                "testCaseId": t.string().optional(),
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
                "projectId": t.string().optional(),
                "stepId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestCaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsHistoriesExecutionsStepsPerfMetricsSummaryCreate"
    ] = toolresults.post(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfMetricsSummary",
        t.struct(
            {
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
                "stepId": t.string().optional(),
                "projectId": t.string().optional(),
                "perfMetrics": t.array(t.string()).optional(),
                "perfEnvironment": t.proxy(renames["PerfEnvironmentIn"]).optional(),
                "appStartTime": t.proxy(renames["AppStartTimeIn"]),
                "graphicsStats": t.proxy(renames["GraphicsStatsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PerfMetricsSummaryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsThumbnailsList"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/thumbnails",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "projectId": t.string().optional(),
                "historyId": t.string().optional(),
                "stepId": t.string().optional(),
                "executionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListStepThumbnailsResponseOut"]),
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
                "historyId": t.string().optional(),
                "projectId": t.string().optional(),
                "sampleSeriesId": t.string().optional(),
                "stepId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PerfSampleSeriesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsPerfSampleSeriesList"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries/{sampleSeriesId}",
        t.struct(
            {
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
                "projectId": t.string().optional(),
                "sampleSeriesId": t.string().optional(),
                "stepId": t.string().optional(),
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
                "historyId": t.string().optional(),
                "projectId": t.string().optional(),
                "sampleSeriesId": t.string().optional(),
                "stepId": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "historyId": t.string().optional(),
                "sampleSeriesId": t.string().optional(),
                "stepId": t.string().optional(),
                "pageToken": t.string().optional(),
                "executionId": t.string().optional(),
                "projectId": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "historyId": t.string().optional(),
                "sampleSeriesId": t.string().optional(),
                "stepId": t.string().optional(),
                "pageToken": t.string().optional(),
                "executionId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPerfSamplesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsClustersGet"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/clusters",
        t.struct(
            {
                "projectId": t.string().optional(),
                "historyId": t.string().optional(),
                "executionId": t.string().optional(),
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
                "historyId": t.string().optional(),
                "executionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScreenshotClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="toolresults",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
