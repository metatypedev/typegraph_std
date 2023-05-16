from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_toolresults() -> Import:
    toolresults = HTTPRuntime("https://toolresults.googleapis.com/")

    renames = {
        "ErrorResponse": "_toolresults_1_ErrorResponse",
        "UsedRoboIgnoreDirectiveIn": "_toolresults_2_UsedRoboIgnoreDirectiveIn",
        "UsedRoboIgnoreDirectiveOut": "_toolresults_3_UsedRoboIgnoreDirectiveOut",
        "PerfEnvironmentIn": "_toolresults_4_PerfEnvironmentIn",
        "PerfEnvironmentOut": "_toolresults_5_PerfEnvironmentOut",
        "TestIssueIn": "_toolresults_6_TestIssueIn",
        "TestIssueOut": "_toolresults_7_TestIssueOut",
        "ListPerfSamplesResponseIn": "_toolresults_8_ListPerfSamplesResponseIn",
        "ListPerfSamplesResponseOut": "_toolresults_9_ListPerfSamplesResponseOut",
        "ListStepsResponseIn": "_toolresults_10_ListStepsResponseIn",
        "ListStepsResponseOut": "_toolresults_11_ListStepsResponseOut",
        "TestCaseIn": "_toolresults_12_TestCaseIn",
        "TestCaseOut": "_toolresults_13_TestCaseOut",
        "NonSdkApiInsightIn": "_toolresults_14_NonSdkApiInsightIn",
        "NonSdkApiInsightOut": "_toolresults_15_NonSdkApiInsightOut",
        "ToolExecutionStepIn": "_toolresults_16_ToolExecutionStepIn",
        "ToolExecutionStepOut": "_toolresults_17_ToolExecutionStepOut",
        "EncounteredNonAndroidUiWidgetScreenIn": "_toolresults_18_EncounteredNonAndroidUiWidgetScreenIn",
        "EncounteredNonAndroidUiWidgetScreenOut": "_toolresults_19_EncounteredNonAndroidUiWidgetScreenOut",
        "LogcatCollectionErrorIn": "_toolresults_20_LogcatCollectionErrorIn",
        "LogcatCollectionErrorOut": "_toolresults_21_LogcatCollectionErrorOut",
        "IosXcTestIn": "_toolresults_22_IosXcTestIn",
        "IosXcTestOut": "_toolresults_23_IosXcTestOut",
        "ListTestCasesResponseIn": "_toolresults_24_ListTestCasesResponseIn",
        "ListTestCasesResponseOut": "_toolresults_25_ListTestCasesResponseOut",
        "AvailableDeepLinksIn": "_toolresults_26_AvailableDeepLinksIn",
        "AvailableDeepLinksOut": "_toolresults_27_AvailableDeepLinksOut",
        "EncounteredLoginScreenIn": "_toolresults_28_EncounteredLoginScreenIn",
        "EncounteredLoginScreenOut": "_toolresults_29_EncounteredLoginScreenOut",
        "SuccessDetailIn": "_toolresults_30_SuccessDetailIn",
        "SuccessDetailOut": "_toolresults_31_SuccessDetailOut",
        "AnyIn": "_toolresults_32_AnyIn",
        "AnyOut": "_toolresults_33_AnyOut",
        "StepSummaryIn": "_toolresults_34_StepSummaryIn",
        "StepSummaryOut": "_toolresults_35_StepSummaryOut",
        "PublishXunitXmlFilesRequestIn": "_toolresults_36_PublishXunitXmlFilesRequestIn",
        "PublishXunitXmlFilesRequestOut": "_toolresults_37_PublishXunitXmlFilesRequestOut",
        "GraphicsStatsIn": "_toolresults_38_GraphicsStatsIn",
        "GraphicsStatsOut": "_toolresults_39_GraphicsStatsOut",
        "StartActivityNotFoundIn": "_toolresults_40_StartActivityNotFoundIn",
        "StartActivityNotFoundOut": "_toolresults_41_StartActivityNotFoundOut",
        "PerfSampleSeriesIn": "_toolresults_42_PerfSampleSeriesIn",
        "PerfSampleSeriesOut": "_toolresults_43_PerfSampleSeriesOut",
        "ExecutionIn": "_toolresults_44_ExecutionIn",
        "ExecutionOut": "_toolresults_45_ExecutionOut",
        "UIElementTooDeepIn": "_toolresults_46_UIElementTooDeepIn",
        "UIElementTooDeepOut": "_toolresults_47_UIElementTooDeepOut",
        "ToolExitCodeIn": "_toolresults_48_ToolExitCodeIn",
        "ToolExitCodeOut": "_toolresults_49_ToolExitCodeOut",
        "UsedRoboDirectiveIn": "_toolresults_50_UsedRoboDirectiveIn",
        "UsedRoboDirectiveOut": "_toolresults_51_UsedRoboDirectiveOut",
        "IosRoboTestIn": "_toolresults_52_IosRoboTestIn",
        "IosRoboTestOut": "_toolresults_53_IosRoboTestOut",
        "UnspecifiedWarningIn": "_toolresults_54_UnspecifiedWarningIn",
        "UnspecifiedWarningOut": "_toolresults_55_UnspecifiedWarningOut",
        "AndroidAppInfoIn": "_toolresults_56_AndroidAppInfoIn",
        "AndroidAppInfoOut": "_toolresults_57_AndroidAppInfoOut",
        "BatchCreatePerfSamplesRequestIn": "_toolresults_58_BatchCreatePerfSamplesRequestIn",
        "BatchCreatePerfSamplesRequestOut": "_toolresults_59_BatchCreatePerfSamplesRequestOut",
        "NonSdkApiIn": "_toolresults_60_NonSdkApiIn",
        "NonSdkApiOut": "_toolresults_61_NonSdkApiOut",
        "OverlappingUIElementsIn": "_toolresults_62_OverlappingUIElementsIn",
        "OverlappingUIElementsOut": "_toolresults_63_OverlappingUIElementsOut",
        "PerfSampleIn": "_toolresults_64_PerfSampleIn",
        "PerfSampleOut": "_toolresults_65_PerfSampleOut",
        "FatalExceptionIn": "_toolresults_66_FatalExceptionIn",
        "FatalExceptionOut": "_toolresults_67_FatalExceptionOut",
        "ListStepAccessibilityClustersResponseIn": "_toolresults_68_ListStepAccessibilityClustersResponseIn",
        "ListStepAccessibilityClustersResponseOut": "_toolresults_69_ListStepAccessibilityClustersResponseOut",
        "InconclusiveDetailIn": "_toolresults_70_InconclusiveDetailIn",
        "InconclusiveDetailOut": "_toolresults_71_InconclusiveDetailOut",
        "StepIn": "_toolresults_72_StepIn",
        "StepOut": "_toolresults_73_StepOut",
        "StepLabelsEntryIn": "_toolresults_74_StepLabelsEntryIn",
        "StepLabelsEntryOut": "_toolresults_75_StepLabelsEntryOut",
        "StatusIn": "_toolresults_76_StatusIn",
        "StatusOut": "_toolresults_77_StatusOut",
        "IosTestIn": "_toolresults_78_IosTestIn",
        "IosTestOut": "_toolresults_79_IosTestOut",
        "MatrixDimensionDefinitionIn": "_toolresults_80_MatrixDimensionDefinitionIn",
        "MatrixDimensionDefinitionOut": "_toolresults_81_MatrixDimensionDefinitionOut",
        "NativeCrashIn": "_toolresults_82_NativeCrashIn",
        "NativeCrashOut": "_toolresults_83_NativeCrashOut",
        "IosAppInfoIn": "_toolresults_84_IosAppInfoIn",
        "IosAppInfoOut": "_toolresults_85_IosAppInfoOut",
        "AppStartTimeIn": "_toolresults_86_AppStartTimeIn",
        "AppStartTimeOut": "_toolresults_87_AppStartTimeOut",
        "SafeHtmlProtoIn": "_toolresults_88_SafeHtmlProtoIn",
        "SafeHtmlProtoOut": "_toolresults_89_SafeHtmlProtoOut",
        "ProjectSettingsIn": "_toolresults_90_ProjectSettingsIn",
        "ProjectSettingsOut": "_toolresults_91_ProjectSettingsOut",
        "IndividualOutcomeIn": "_toolresults_92_IndividualOutcomeIn",
        "IndividualOutcomeOut": "_toolresults_93_IndividualOutcomeOut",
        "ResultsStorageIn": "_toolresults_94_ResultsStorageIn",
        "ResultsStorageOut": "_toolresults_95_ResultsStorageOut",
        "AndroidTestIn": "_toolresults_96_AndroidTestIn",
        "AndroidTestOut": "_toolresults_97_AndroidTestOut",
        "EnvironmentIn": "_toolresults_98_EnvironmentIn",
        "EnvironmentOut": "_toolresults_99_EnvironmentOut",
        "ANRIn": "_toolresults_100_ANRIn",
        "ANROut": "_toolresults_101_ANROut",
        "CPUInfoIn": "_toolresults_102_CPUInfoIn",
        "CPUInfoOut": "_toolresults_103_CPUInfoOut",
        "TestExecutionStepIn": "_toolresults_104_TestExecutionStepIn",
        "TestExecutionStepOut": "_toolresults_105_TestExecutionStepOut",
        "ToolOutputReferenceIn": "_toolresults_106_ToolOutputReferenceIn",
        "ToolOutputReferenceOut": "_toolresults_107_ToolOutputReferenceOut",
        "GraphicsStatsBucketIn": "_toolresults_108_GraphicsStatsBucketIn",
        "GraphicsStatsBucketOut": "_toolresults_109_GraphicsStatsBucketOut",
        "InsufficientCoverageIn": "_toolresults_110_InsufficientCoverageIn",
        "InsufficientCoverageOut": "_toolresults_111_InsufficientCoverageOut",
        "InAppPurchasesFoundIn": "_toolresults_112_InAppPurchasesFoundIn",
        "InAppPurchasesFoundOut": "_toolresults_113_InAppPurchasesFoundOut",
        "LauncherActivityNotFoundIn": "_toolresults_114_LauncherActivityNotFoundIn",
        "LauncherActivityNotFoundOut": "_toolresults_115_LauncherActivityNotFoundOut",
        "PrimaryStepIn": "_toolresults_116_PrimaryStepIn",
        "PrimaryStepOut": "_toolresults_117_PrimaryStepOut",
        "AndroidInstrumentationTestIn": "_toolresults_118_AndroidInstrumentationTestIn",
        "AndroidInstrumentationTestOut": "_toolresults_119_AndroidInstrumentationTestOut",
        "PerformedMonkeyActionsIn": "_toolresults_120_PerformedMonkeyActionsIn",
        "PerformedMonkeyActionsOut": "_toolresults_121_PerformedMonkeyActionsOut",
        "TimestampIn": "_toolresults_122_TimestampIn",
        "TimestampOut": "_toolresults_123_TimestampOut",
        "SuggestionProtoIn": "_toolresults_124_SuggestionProtoIn",
        "SuggestionProtoOut": "_toolresults_125_SuggestionProtoOut",
        "ListHistoriesResponseIn": "_toolresults_126_ListHistoriesResponseIn",
        "ListHistoriesResponseOut": "_toolresults_127_ListHistoriesResponseOut",
        "FileReferenceIn": "_toolresults_128_FileReferenceIn",
        "FileReferenceOut": "_toolresults_129_FileReferenceOut",
        "UnusedRoboDirectiveIn": "_toolresults_130_UnusedRoboDirectiveIn",
        "UnusedRoboDirectiveOut": "_toolresults_131_UnusedRoboDirectiveOut",
        "RegionProtoIn": "_toolresults_132_RegionProtoIn",
        "RegionProtoOut": "_toolresults_133_RegionProtoOut",
        "IosTestLoopIn": "_toolresults_134_IosTestLoopIn",
        "IosTestLoopOut": "_toolresults_135_IosTestLoopOut",
        "ImageIn": "_toolresults_136_ImageIn",
        "ImageOut": "_toolresults_137_ImageOut",
        "ListScreenshotClustersResponseIn": "_toolresults_138_ListScreenshotClustersResponseIn",
        "ListScreenshotClustersResponseOut": "_toolresults_139_ListScreenshotClustersResponseOut",
        "UpgradeInsightIn": "_toolresults_140_UpgradeInsightIn",
        "UpgradeInsightOut": "_toolresults_141_UpgradeInsightOut",
        "MergedResultIn": "_toolresults_142_MergedResultIn",
        "MergedResultOut": "_toolresults_143_MergedResultOut",
        "FailureDetailIn": "_toolresults_144_FailureDetailIn",
        "FailureDetailOut": "_toolresults_145_FailureDetailOut",
        "AndroidRoboTestIn": "_toolresults_146_AndroidRoboTestIn",
        "AndroidRoboTestOut": "_toolresults_147_AndroidRoboTestOut",
        "SpecificationIn": "_toolresults_148_SpecificationIn",
        "SpecificationOut": "_toolresults_149_SpecificationOut",
        "AndroidTestLoopIn": "_toolresults_150_AndroidTestLoopIn",
        "AndroidTestLoopOut": "_toolresults_151_AndroidTestLoopOut",
        "MultiStepIn": "_toolresults_152_MultiStepIn",
        "MultiStepOut": "_toolresults_153_MultiStepOut",
        "StepDimensionValueEntryIn": "_toolresults_154_StepDimensionValueEntryIn",
        "StepDimensionValueEntryOut": "_toolresults_155_StepDimensionValueEntryOut",
        "NonSdkApiUsageViolationIn": "_toolresults_156_NonSdkApiUsageViolationIn",
        "NonSdkApiUsageViolationOut": "_toolresults_157_NonSdkApiUsageViolationOut",
        "RoboScriptExecutionIn": "_toolresults_158_RoboScriptExecutionIn",
        "RoboScriptExecutionOut": "_toolresults_159_RoboScriptExecutionOut",
        "ListExecutionsResponseIn": "_toolresults_160_ListExecutionsResponseIn",
        "ListExecutionsResponseOut": "_toolresults_161_ListExecutionsResponseOut",
        "BatchCreatePerfSamplesResponseIn": "_toolresults_162_BatchCreatePerfSamplesResponseIn",
        "BatchCreatePerfSamplesResponseOut": "_toolresults_163_BatchCreatePerfSamplesResponseOut",
        "PerformedGoogleLoginIn": "_toolresults_164_PerformedGoogleLoginIn",
        "PerformedGoogleLoginOut": "_toolresults_165_PerformedGoogleLoginOut",
        "PerfMetricsSummaryIn": "_toolresults_166_PerfMetricsSummaryIn",
        "PerfMetricsSummaryOut": "_toolresults_167_PerfMetricsSummaryOut",
        "ScreenshotClusterIn": "_toolresults_168_ScreenshotClusterIn",
        "ScreenshotClusterOut": "_toolresults_169_ScreenshotClusterOut",
        "ToolExecutionIn": "_toolresults_170_ToolExecutionIn",
        "ToolExecutionOut": "_toolresults_171_ToolExecutionOut",
        "TestCaseReferenceIn": "_toolresults_172_TestCaseReferenceIn",
        "TestCaseReferenceOut": "_toolresults_173_TestCaseReferenceOut",
        "ListStepThumbnailsResponseIn": "_toolresults_174_ListStepThumbnailsResponseIn",
        "ListStepThumbnailsResponseOut": "_toolresults_175_ListStepThumbnailsResponseOut",
        "HistoryIn": "_toolresults_176_HistoryIn",
        "HistoryOut": "_toolresults_177_HistoryOut",
        "BasicPerfSampleSeriesIn": "_toolresults_178_BasicPerfSampleSeriesIn",
        "BasicPerfSampleSeriesOut": "_toolresults_179_BasicPerfSampleSeriesOut",
        "ScreenIn": "_toolresults_180_ScreenIn",
        "ScreenOut": "_toolresults_181_ScreenOut",
        "ThumbnailIn": "_toolresults_182_ThumbnailIn",
        "ThumbnailOut": "_toolresults_183_ThumbnailOut",
        "SkippedDetailIn": "_toolresults_184_SkippedDetailIn",
        "SkippedDetailOut": "_toolresults_185_SkippedDetailOut",
        "FailedToInstallIn": "_toolresults_186_FailedToInstallIn",
        "FailedToInstallOut": "_toolresults_187_FailedToInstallOut",
        "DurationIn": "_toolresults_188_DurationIn",
        "DurationOut": "_toolresults_189_DurationOut",
        "BlankScreenIn": "_toolresults_190_BlankScreenIn",
        "BlankScreenOut": "_toolresults_191_BlankScreenOut",
        "ShardSummaryIn": "_toolresults_192_ShardSummaryIn",
        "ShardSummaryOut": "_toolresults_193_ShardSummaryOut",
        "ListEnvironmentsResponseIn": "_toolresults_194_ListEnvironmentsResponseIn",
        "ListEnvironmentsResponseOut": "_toolresults_195_ListEnvironmentsResponseOut",
        "NonSdkApiUsageViolationReportIn": "_toolresults_196_NonSdkApiUsageViolationReportIn",
        "NonSdkApiUsageViolationReportOut": "_toolresults_197_NonSdkApiUsageViolationReportOut",
        "PendingGoogleUpdateInsightIn": "_toolresults_198_PendingGoogleUpdateInsightIn",
        "PendingGoogleUpdateInsightOut": "_toolresults_199_PendingGoogleUpdateInsightOut",
        "IosAppCrashedIn": "_toolresults_200_IosAppCrashedIn",
        "IosAppCrashedOut": "_toolresults_201_IosAppCrashedOut",
        "EnvironmentDimensionValueEntryIn": "_toolresults_202_EnvironmentDimensionValueEntryIn",
        "EnvironmentDimensionValueEntryOut": "_toolresults_203_EnvironmentDimensionValueEntryOut",
        "MemoryInfoIn": "_toolresults_204_MemoryInfoIn",
        "MemoryInfoOut": "_toolresults_205_MemoryInfoOut",
        "CrashDialogErrorIn": "_toolresults_206_CrashDialogErrorIn",
        "CrashDialogErrorOut": "_toolresults_207_CrashDialogErrorOut",
        "TestTimingIn": "_toolresults_208_TestTimingIn",
        "TestTimingOut": "_toolresults_209_TestTimingOut",
        "TestSuiteOverviewIn": "_toolresults_210_TestSuiteOverviewIn",
        "TestSuiteOverviewOut": "_toolresults_211_TestSuiteOverviewOut",
        "DetectedAppSplashScreenIn": "_toolresults_212_DetectedAppSplashScreenIn",
        "DetectedAppSplashScreenOut": "_toolresults_213_DetectedAppSplashScreenOut",
        "SuggestionClusterProtoIn": "_toolresults_214_SuggestionClusterProtoIn",
        "SuggestionClusterProtoOut": "_toolresults_215_SuggestionClusterProtoOut",
        "ListPerfSampleSeriesResponseIn": "_toolresults_216_ListPerfSampleSeriesResponseIn",
        "ListPerfSampleSeriesResponseOut": "_toolresults_217_ListPerfSampleSeriesResponseOut",
        "StackTraceIn": "_toolresults_218_StackTraceIn",
        "StackTraceOut": "_toolresults_219_StackTraceOut",
        "OutcomeIn": "_toolresults_220_OutcomeIn",
        "OutcomeOut": "_toolresults_221_OutcomeOut",
        "DeviceOutOfMemoryIn": "_toolresults_222_DeviceOutOfMemoryIn",
        "DeviceOutOfMemoryOut": "_toolresults_223_DeviceOutOfMemoryOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["UsedRoboIgnoreDirectiveIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["UsedRoboIgnoreDirectiveIn"])
    types["UsedRoboIgnoreDirectiveOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsedRoboIgnoreDirectiveOut"])
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
    types["TestIssueIn"] = t.struct(
        {
            "category": t.string().optional(),
            "type": t.string().optional(),
            "warning": t.proxy(renames["AnyIn"]).optional(),
            "severity": t.string().optional(),
            "errorMessage": t.string().optional(),
            "stackTrace": t.proxy(renames["StackTraceIn"]).optional(),
        }
    ).named(renames["TestIssueIn"])
    types["TestIssueOut"] = t.struct(
        {
            "category": t.string().optional(),
            "type": t.string().optional(),
            "warning": t.proxy(renames["AnyOut"]).optional(),
            "severity": t.string().optional(),
            "errorMessage": t.string().optional(),
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIssueOut"])
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
    types["ListStepsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "steps": t.array(t.proxy(renames["StepIn"])).optional(),
        }
    ).named(renames["ListStepsResponseIn"])
    types["ListStepsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "steps": t.array(t.proxy(renames["StepOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListStepsResponseOut"])
    types["TestCaseIn"] = t.struct(
        {
            "stackTraces": t.array(t.proxy(renames["StackTraceIn"])).optional(),
            "skippedMessage": t.string().optional(),
            "testCaseReference": t.proxy(renames["TestCaseReferenceIn"]).optional(),
            "elapsedTime": t.proxy(renames["DurationIn"]).optional(),
            "toolOutputs": t.array(
                t.proxy(renames["ToolOutputReferenceIn"])
            ).optional(),
            "status": t.string().optional(),
            "testCaseId": t.string().optional(),
            "endTime": t.proxy(renames["TimestampIn"]).optional(),
            "startTime": t.proxy(renames["TimestampIn"]).optional(),
        }
    ).named(renames["TestCaseIn"])
    types["TestCaseOut"] = t.struct(
        {
            "stackTraces": t.array(t.proxy(renames["StackTraceOut"])).optional(),
            "skippedMessage": t.string().optional(),
            "testCaseReference": t.proxy(renames["TestCaseReferenceOut"]).optional(),
            "elapsedTime": t.proxy(renames["DurationOut"]).optional(),
            "toolOutputs": t.array(
                t.proxy(renames["ToolOutputReferenceOut"])
            ).optional(),
            "status": t.string().optional(),
            "testCaseId": t.string().optional(),
            "endTime": t.proxy(renames["TimestampOut"]).optional(),
            "startTime": t.proxy(renames["TimestampOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestCaseOut"])
    types["NonSdkApiInsightIn"] = t.struct(
        {
            "exampleTraceMessages": t.array(t.string()).optional(),
            "upgradeInsight": t.proxy(renames["UpgradeInsightIn"]).optional(),
            "matcherId": t.string().optional(),
            "pendingGoogleUpdateInsight": t.proxy(
                renames["PendingGoogleUpdateInsightIn"]
            ).optional(),
        }
    ).named(renames["NonSdkApiInsightIn"])
    types["NonSdkApiInsightOut"] = t.struct(
        {
            "exampleTraceMessages": t.array(t.string()).optional(),
            "upgradeInsight": t.proxy(renames["UpgradeInsightOut"]).optional(),
            "matcherId": t.string().optional(),
            "pendingGoogleUpdateInsight": t.proxy(
                renames["PendingGoogleUpdateInsightOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonSdkApiInsightOut"])
    types["ToolExecutionStepIn"] = t.struct(
        {"toolExecution": t.proxy(renames["ToolExecutionIn"]).optional()}
    ).named(renames["ToolExecutionStepIn"])
    types["ToolExecutionStepOut"] = t.struct(
        {
            "toolExecution": t.proxy(renames["ToolExecutionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ToolExecutionStepOut"])
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
    types["LogcatCollectionErrorIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LogcatCollectionErrorIn"]
    )
    types["LogcatCollectionErrorOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LogcatCollectionErrorOut"])
    types["IosXcTestIn"] = t.struct(
        {"bundleId": t.string().optional(), "xcodeVersion": t.string().optional()}
    ).named(renames["IosXcTestIn"])
    types["IosXcTestOut"] = t.struct(
        {
            "bundleId": t.string().optional(),
            "xcodeVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosXcTestOut"])
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
    types["AvailableDeepLinksIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AvailableDeepLinksIn"]
    )
    types["AvailableDeepLinksOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AvailableDeepLinksOut"])
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
    types["SuccessDetailIn"] = t.struct(
        {"otherNativeCrash": t.boolean().optional()}
    ).named(renames["SuccessDetailIn"])
    types["SuccessDetailOut"] = t.struct(
        {
            "otherNativeCrash": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuccessDetailOut"])
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
    types["StepSummaryIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StepSummaryIn"]
    )
    types["StepSummaryOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StepSummaryOut"])
    types["PublishXunitXmlFilesRequestIn"] = t.struct(
        {"xunitXmlFiles": t.array(t.proxy(renames["FileReferenceIn"])).optional()}
    ).named(renames["PublishXunitXmlFilesRequestIn"])
    types["PublishXunitXmlFilesRequestOut"] = t.struct(
        {
            "xunitXmlFiles": t.array(t.proxy(renames["FileReferenceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishXunitXmlFilesRequestOut"])
    types["GraphicsStatsIn"] = t.struct(
        {
            "slowUiThreadCount": t.string().optional(),
            "slowBitmapUploadCount": t.string().optional(),
            "missedVsyncCount": t.string().optional(),
            "p99Millis": t.string().optional(),
            "totalFrames": t.string().optional(),
            "buckets": t.array(t.proxy(renames["GraphicsStatsBucketIn"])).optional(),
            "p95Millis": t.string().optional(),
            "highInputLatencyCount": t.string().optional(),
            "slowDrawCount": t.string().optional(),
            "jankyFrames": t.string().optional(),
            "p90Millis": t.string().optional(),
            "p50Millis": t.string().optional(),
        }
    ).named(renames["GraphicsStatsIn"])
    types["GraphicsStatsOut"] = t.struct(
        {
            "slowUiThreadCount": t.string().optional(),
            "slowBitmapUploadCount": t.string().optional(),
            "missedVsyncCount": t.string().optional(),
            "p99Millis": t.string().optional(),
            "totalFrames": t.string().optional(),
            "buckets": t.array(t.proxy(renames["GraphicsStatsBucketOut"])).optional(),
            "p95Millis": t.string().optional(),
            "highInputLatencyCount": t.string().optional(),
            "slowDrawCount": t.string().optional(),
            "jankyFrames": t.string().optional(),
            "p90Millis": t.string().optional(),
            "p50Millis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GraphicsStatsOut"])
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
    types["PerfSampleSeriesIn"] = t.struct(
        {
            "basicPerfSampleSeries": t.proxy(
                renames["BasicPerfSampleSeriesIn"]
            ).optional(),
            "executionId": t.string().optional(),
            "historyId": t.string().optional(),
            "stepId": t.string().optional(),
            "sampleSeriesId": t.string().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["PerfSampleSeriesIn"])
    types["PerfSampleSeriesOut"] = t.struct(
        {
            "basicPerfSampleSeries": t.proxy(
                renames["BasicPerfSampleSeriesOut"]
            ).optional(),
            "executionId": t.string().optional(),
            "historyId": t.string().optional(),
            "stepId": t.string().optional(),
            "sampleSeriesId": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerfSampleSeriesOut"])
    types["ExecutionIn"] = t.struct(
        {
            "specification": t.proxy(renames["SpecificationIn"]).optional(),
            "executionId": t.string().optional(),
            "creationTime": t.proxy(renames["TimestampIn"]).optional(),
            "state": t.string().optional(),
            "completionTime": t.proxy(renames["TimestampIn"]).optional(),
            "outcome": t.proxy(renames["OutcomeIn"]).optional(),
            "testExecutionMatrixId": t.string().optional(),
            "dimensionDefinitions": t.array(
                t.proxy(renames["MatrixDimensionDefinitionIn"])
            ).optional(),
        }
    ).named(renames["ExecutionIn"])
    types["ExecutionOut"] = t.struct(
        {
            "specification": t.proxy(renames["SpecificationOut"]).optional(),
            "executionId": t.string().optional(),
            "creationTime": t.proxy(renames["TimestampOut"]).optional(),
            "state": t.string().optional(),
            "completionTime": t.proxy(renames["TimestampOut"]).optional(),
            "outcome": t.proxy(renames["OutcomeOut"]).optional(),
            "testExecutionMatrixId": t.string().optional(),
            "dimensionDefinitions": t.array(
                t.proxy(renames["MatrixDimensionDefinitionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionOut"])
    types["UIElementTooDeepIn"] = t.struct(
        {
            "screenId": t.string().optional(),
            "depth": t.integer().optional(),
            "screenStateId": t.string().optional(),
        }
    ).named(renames["UIElementTooDeepIn"])
    types["UIElementTooDeepOut"] = t.struct(
        {
            "screenId": t.string().optional(),
            "depth": t.integer().optional(),
            "screenStateId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UIElementTooDeepOut"])
    types["ToolExitCodeIn"] = t.struct({"number": t.integer().optional()}).named(
        renames["ToolExitCodeIn"]
    )
    types["ToolExitCodeOut"] = t.struct(
        {
            "number": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ToolExitCodeOut"])
    types["UsedRoboDirectiveIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["UsedRoboDirectiveIn"])
    types["UsedRoboDirectiveOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsedRoboDirectiveOut"])
    types["IosRoboTestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["IosRoboTestIn"]
    )
    types["IosRoboTestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["IosRoboTestOut"])
    types["UnspecifiedWarningIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UnspecifiedWarningIn"]
    )
    types["UnspecifiedWarningOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UnspecifiedWarningOut"])
    types["AndroidAppInfoIn"] = t.struct(
        {
            "name": t.string().optional(),
            "versionCode": t.string().optional(),
            "versionName": t.string().optional(),
            "packageName": t.string().optional(),
        }
    ).named(renames["AndroidAppInfoIn"])
    types["AndroidAppInfoOut"] = t.struct(
        {
            "name": t.string().optional(),
            "versionCode": t.string().optional(),
            "versionName": t.string().optional(),
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidAppInfoOut"])
    types["BatchCreatePerfSamplesRequestIn"] = t.struct(
        {"perfSamples": t.array(t.proxy(renames["PerfSampleIn"])).optional()}
    ).named(renames["BatchCreatePerfSamplesRequestIn"])
    types["BatchCreatePerfSamplesRequestOut"] = t.struct(
        {
            "perfSamples": t.array(t.proxy(renames["PerfSampleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreatePerfSamplesRequestOut"])
    types["NonSdkApiIn"] = t.struct(
        {
            "invocationCount": t.integer().optional(),
            "list": t.string().optional(),
            "insights": t.array(t.proxy(renames["NonSdkApiInsightIn"])).optional(),
            "apiSignature": t.string().optional(),
            "exampleStackTraces": t.array(t.string()).optional(),
        }
    ).named(renames["NonSdkApiIn"])
    types["NonSdkApiOut"] = t.struct(
        {
            "invocationCount": t.integer().optional(),
            "list": t.string().optional(),
            "insights": t.array(t.proxy(renames["NonSdkApiInsightOut"])).optional(),
            "apiSignature": t.string().optional(),
            "exampleStackTraces": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonSdkApiOut"])
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
    types["PerfSampleIn"] = t.struct(
        {
            "value": t.number().optional(),
            "sampleTime": t.proxy(renames["TimestampIn"]).optional(),
        }
    ).named(renames["PerfSampleIn"])
    types["PerfSampleOut"] = t.struct(
        {
            "value": t.number().optional(),
            "sampleTime": t.proxy(renames["TimestampOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerfSampleOut"])
    types["FatalExceptionIn"] = t.struct(
        {"stackTrace": t.proxy(renames["StackTraceIn"]).optional()}
    ).named(renames["FatalExceptionIn"])
    types["FatalExceptionOut"] = t.struct(
        {
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FatalExceptionOut"])
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
    types["InconclusiveDetailIn"] = t.struct(
        {
            "abortedByUser": t.boolean().optional(),
            "infrastructureFailure": t.boolean().optional(),
            "hasErrorLogs": t.boolean().optional(),
        }
    ).named(renames["InconclusiveDetailIn"])
    types["InconclusiveDetailOut"] = t.struct(
        {
            "abortedByUser": t.boolean().optional(),
            "infrastructureFailure": t.boolean().optional(),
            "hasErrorLogs": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InconclusiveDetailOut"])
    types["StepIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["StepLabelsEntryIn"])).optional(),
            "state": t.string().optional(),
            "description": t.string().optional(),
            "hasImages": t.boolean().optional(),
            "creationTime": t.proxy(renames["TimestampIn"]).optional(),
            "stepId": t.string().optional(),
            "completionTime": t.proxy(renames["TimestampIn"]).optional(),
            "dimensionValue": t.array(
                t.proxy(renames["StepDimensionValueEntryIn"])
            ).optional(),
            "deviceUsageDuration": t.proxy(renames["DurationIn"]).optional(),
            "runDuration": t.proxy(renames["DurationIn"]).optional(),
            "toolExecutionStep": t.proxy(renames["ToolExecutionStepIn"]).optional(),
            "outcome": t.proxy(renames["OutcomeIn"]).optional(),
            "testExecutionStep": t.proxy(renames["TestExecutionStepIn"]).optional(),
            "multiStep": t.proxy(renames["MultiStepIn"]).optional(),
        }
    ).named(renames["StepIn"])
    types["StepOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["StepLabelsEntryOut"])).optional(),
            "state": t.string().optional(),
            "description": t.string().optional(),
            "hasImages": t.boolean().optional(),
            "creationTime": t.proxy(renames["TimestampOut"]).optional(),
            "stepId": t.string().optional(),
            "completionTime": t.proxy(renames["TimestampOut"]).optional(),
            "dimensionValue": t.array(
                t.proxy(renames["StepDimensionValueEntryOut"])
            ).optional(),
            "deviceUsageDuration": t.proxy(renames["DurationOut"]).optional(),
            "runDuration": t.proxy(renames["DurationOut"]).optional(),
            "toolExecutionStep": t.proxy(renames["ToolExecutionStepOut"]).optional(),
            "outcome": t.proxy(renames["OutcomeOut"]).optional(),
            "testExecutionStep": t.proxy(renames["TestExecutionStepOut"]).optional(),
            "multiStep": t.proxy(renames["MultiStepOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StepOut"])
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
    types["IosTestIn"] = t.struct(
        {
            "iosXcTest": t.proxy(renames["IosXcTestIn"]).optional(),
            "iosRoboTest": t.proxy(renames["IosRoboTestIn"]).optional(),
            "testTimeout": t.proxy(renames["DurationIn"]).optional(),
            "iosTestLoop": t.proxy(renames["IosTestLoopIn"]).optional(),
            "iosAppInfo": t.proxy(renames["IosAppInfoIn"]).optional(),
        }
    ).named(renames["IosTestIn"])
    types["IosTestOut"] = t.struct(
        {
            "iosXcTest": t.proxy(renames["IosXcTestOut"]).optional(),
            "iosRoboTest": t.proxy(renames["IosRoboTestOut"]).optional(),
            "testTimeout": t.proxy(renames["DurationOut"]).optional(),
            "iosTestLoop": t.proxy(renames["IosTestLoopOut"]).optional(),
            "iosAppInfo": t.proxy(renames["IosAppInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosTestOut"])
    types["MatrixDimensionDefinitionIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MatrixDimensionDefinitionIn"]
    )
    types["MatrixDimensionDefinitionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MatrixDimensionDefinitionOut"])
    types["NativeCrashIn"] = t.struct(
        {"stackTrace": t.proxy(renames["StackTraceIn"]).optional()}
    ).named(renames["NativeCrashIn"])
    types["NativeCrashOut"] = t.struct(
        {
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NativeCrashOut"])
    types["IosAppInfoIn"] = t.struct({"name": t.string().optional()}).named(
        renames["IosAppInfoIn"]
    )
    types["IosAppInfoOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosAppInfoOut"])
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
    types["SafeHtmlProtoIn"] = t.struct(
        {"privateDoNotAccessOrElseSafeHtmlWrappedValue": t.string().optional()}
    ).named(renames["SafeHtmlProtoIn"])
    types["SafeHtmlProtoOut"] = t.struct(
        {
            "privateDoNotAccessOrElseSafeHtmlWrappedValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SafeHtmlProtoOut"])
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
            "runDuration": t.proxy(renames["DurationIn"]).optional(),
            "stepId": t.string(),
            "multistepNumber": t.integer().optional(),
            "outcomeSummary": t.string(),
        }
    ).named(renames["IndividualOutcomeIn"])
    types["IndividualOutcomeOut"] = t.struct(
        {
            "runDuration": t.proxy(renames["DurationOut"]).optional(),
            "stepId": t.string(),
            "multistepNumber": t.integer().optional(),
            "outcomeSummary": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndividualOutcomeOut"])
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
    types["AndroidTestIn"] = t.struct(
        {
            "androidTestLoop": t.proxy(renames["AndroidTestLoopIn"]).optional(),
            "androidAppInfo": t.proxy(renames["AndroidAppInfoIn"]).optional(),
            "androidRoboTest": t.proxy(renames["AndroidRoboTestIn"]).optional(),
            "testTimeout": t.proxy(renames["DurationIn"]).optional(),
            "androidInstrumentationTest": t.proxy(
                renames["AndroidInstrumentationTestIn"]
            ).optional(),
        }
    ).named(renames["AndroidTestIn"])
    types["AndroidTestOut"] = t.struct(
        {
            "androidTestLoop": t.proxy(renames["AndroidTestLoopOut"]).optional(),
            "androidAppInfo": t.proxy(renames["AndroidAppInfoOut"]).optional(),
            "androidRoboTest": t.proxy(renames["AndroidRoboTestOut"]).optional(),
            "testTimeout": t.proxy(renames["DurationOut"]).optional(),
            "androidInstrumentationTest": t.proxy(
                renames["AndroidInstrumentationTestOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidTestOut"])
    types["EnvironmentIn"] = t.struct(
        {
            "dimensionValue": t.array(
                t.proxy(renames["EnvironmentDimensionValueEntryIn"])
            ).optional(),
            "displayName": t.string().optional(),
            "shardSummaries": t.array(t.proxy(renames["ShardSummaryIn"])).optional(),
            "resultsStorage": t.proxy(renames["ResultsStorageIn"]).optional(),
            "environmentId": t.string().optional(),
            "historyId": t.string().optional(),
            "projectId": t.string().optional(),
            "completionTime": t.proxy(renames["TimestampIn"]).optional(),
            "executionId": t.string().optional(),
            "creationTime": t.proxy(renames["TimestampIn"]).optional(),
            "environmentResult": t.proxy(renames["MergedResultIn"]).optional(),
        }
    ).named(renames["EnvironmentIn"])
    types["EnvironmentOut"] = t.struct(
        {
            "dimensionValue": t.array(
                t.proxy(renames["EnvironmentDimensionValueEntryOut"])
            ).optional(),
            "displayName": t.string().optional(),
            "shardSummaries": t.array(t.proxy(renames["ShardSummaryOut"])).optional(),
            "resultsStorage": t.proxy(renames["ResultsStorageOut"]).optional(),
            "environmentId": t.string().optional(),
            "historyId": t.string().optional(),
            "projectId": t.string().optional(),
            "completionTime": t.proxy(renames["TimestampOut"]).optional(),
            "executionId": t.string().optional(),
            "creationTime": t.proxy(renames["TimestampOut"]).optional(),
            "environmentResult": t.proxy(renames["MergedResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentOut"])
    types["ANRIn"] = t.struct(
        {"stackTrace": t.proxy(renames["StackTraceIn"]).optional()}
    ).named(renames["ANRIn"])
    types["ANROut"] = t.struct(
        {
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ANROut"])
    types["CPUInfoIn"] = t.struct(
        {
            "cpuSpeedInGhz": t.number().optional(),
            "cpuProcessor": t.string().optional(),
            "numberOfCores": t.integer().optional(),
        }
    ).named(renames["CPUInfoIn"])
    types["CPUInfoOut"] = t.struct(
        {
            "cpuSpeedInGhz": t.number().optional(),
            "cpuProcessor": t.string().optional(),
            "numberOfCores": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CPUInfoOut"])
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
            "creationTime": t.proxy(renames["TimestampIn"]).optional(),
            "testCase": t.proxy(renames["TestCaseReferenceIn"]).optional(),
            "output": t.proxy(renames["FileReferenceIn"]).optional(),
        }
    ).named(renames["ToolOutputReferenceIn"])
    types["ToolOutputReferenceOut"] = t.struct(
        {
            "creationTime": t.proxy(renames["TimestampOut"]).optional(),
            "testCase": t.proxy(renames["TestCaseReferenceOut"]).optional(),
            "output": t.proxy(renames["FileReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ToolOutputReferenceOut"])
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
    types["InsufficientCoverageIn"] = t.struct({"_": t.string().optional()}).named(
        renames["InsufficientCoverageIn"]
    )
    types["InsufficientCoverageOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["InsufficientCoverageOut"])
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
    types["LauncherActivityNotFoundIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LauncherActivityNotFoundIn"]
    )
    types["LauncherActivityNotFoundOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LauncherActivityNotFoundOut"])
    types["PrimaryStepIn"] = t.struct(
        {
            "rollUp": t.string().optional(),
            "individualOutcome": t.array(
                t.proxy(renames["IndividualOutcomeIn"])
            ).optional(),
        }
    ).named(renames["PrimaryStepIn"])
    types["PrimaryStepOut"] = t.struct(
        {
            "rollUp": t.string().optional(),
            "individualOutcome": t.array(
                t.proxy(renames["IndividualOutcomeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrimaryStepOut"])
    types["AndroidInstrumentationTestIn"] = t.struct(
        {
            "testRunnerClass": t.string().optional(),
            "useOrchestrator": t.boolean().optional(),
            "testTargets": t.array(t.string()).optional(),
            "testPackageId": t.string().optional(),
        }
    ).named(renames["AndroidInstrumentationTestIn"])
    types["AndroidInstrumentationTestOut"] = t.struct(
        {
            "testRunnerClass": t.string().optional(),
            "useOrchestrator": t.boolean().optional(),
            "testTargets": t.array(t.string()).optional(),
            "testPackageId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidInstrumentationTestOut"])
    types["PerformedMonkeyActionsIn"] = t.struct(
        {"totalActions": t.integer().optional()}
    ).named(renames["PerformedMonkeyActionsIn"])
    types["PerformedMonkeyActionsOut"] = t.struct(
        {
            "totalActions": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerformedMonkeyActionsOut"])
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
    types["SuggestionProtoIn"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "priority": t.string().optional(),
            "helpUrl": t.string().optional(),
            "region": t.proxy(renames["RegionProtoIn"]).optional(),
            "pseudoResourceId": t.string().optional(),
            "title": t.string().optional(),
            "longMessage": t.proxy(renames["SafeHtmlProtoIn"]).optional(),
            "shortMessage": t.proxy(renames["SafeHtmlProtoIn"]).optional(),
            "screenId": t.string().optional(),
            "secondaryPriority": t.number().optional(),
        }
    ).named(renames["SuggestionProtoIn"])
    types["SuggestionProtoOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "priority": t.string().optional(),
            "helpUrl": t.string().optional(),
            "region": t.proxy(renames["RegionProtoOut"]).optional(),
            "pseudoResourceId": t.string().optional(),
            "title": t.string().optional(),
            "longMessage": t.proxy(renames["SafeHtmlProtoOut"]).optional(),
            "shortMessage": t.proxy(renames["SafeHtmlProtoOut"]).optional(),
            "screenId": t.string().optional(),
            "secondaryPriority": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestionProtoOut"])
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
    types["FileReferenceIn"] = t.struct({"fileUri": t.string().optional()}).named(
        renames["FileReferenceIn"]
    )
    types["FileReferenceOut"] = t.struct(
        {
            "fileUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileReferenceOut"])
    types["UnusedRoboDirectiveIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["UnusedRoboDirectiveIn"])
    types["UnusedRoboDirectiveOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnusedRoboDirectiveOut"])
    types["RegionProtoIn"] = t.struct(
        {
            "heightPx": t.integer().optional(),
            "leftPx": t.integer().optional(),
            "widthPx": t.integer().optional(),
            "topPx": t.integer().optional(),
        }
    ).named(renames["RegionProtoIn"])
    types["RegionProtoOut"] = t.struct(
        {
            "heightPx": t.integer().optional(),
            "leftPx": t.integer().optional(),
            "widthPx": t.integer().optional(),
            "topPx": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionProtoOut"])
    types["IosTestLoopIn"] = t.struct({"bundleId": t.string().optional()}).named(
        renames["IosTestLoopIn"]
    )
    types["IosTestLoopOut"] = t.struct(
        {
            "bundleId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosTestLoopOut"])
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
    types["ListScreenshotClustersResponseIn"] = t.struct(
        {"clusters": t.array(t.proxy(renames["ScreenshotClusterIn"])).optional()}
    ).named(renames["ListScreenshotClustersResponseIn"])
    types["ListScreenshotClustersResponseOut"] = t.struct(
        {
            "clusters": t.array(t.proxy(renames["ScreenshotClusterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListScreenshotClustersResponseOut"])
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
    types["MergedResultIn"] = t.struct(
        {
            "testSuiteOverviews": t.array(
                t.proxy(renames["TestSuiteOverviewIn"])
            ).optional(),
            "outcome": t.proxy(renames["OutcomeIn"]).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["MergedResultIn"])
    types["MergedResultOut"] = t.struct(
        {
            "testSuiteOverviews": t.array(
                t.proxy(renames["TestSuiteOverviewOut"])
            ).optional(),
            "outcome": t.proxy(renames["OutcomeOut"]).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MergedResultOut"])
    types["FailureDetailIn"] = t.struct(
        {
            "deviceOutOfMemory": t.boolean().optional(),
            "crashed": t.boolean().optional(),
            "unableToCrawl": t.boolean().optional(),
            "timedOut": t.boolean().optional(),
            "notInstalled": t.boolean().optional(),
            "failedRoboscript": t.boolean().optional(),
            "otherNativeCrash": t.boolean().optional(),
        }
    ).named(renames["FailureDetailIn"])
    types["FailureDetailOut"] = t.struct(
        {
            "deviceOutOfMemory": t.boolean().optional(),
            "crashed": t.boolean().optional(),
            "unableToCrawl": t.boolean().optional(),
            "timedOut": t.boolean().optional(),
            "notInstalled": t.boolean().optional(),
            "failedRoboscript": t.boolean().optional(),
            "otherNativeCrash": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FailureDetailOut"])
    types["AndroidRoboTestIn"] = t.struct(
        {
            "bootstrapPackageId": t.string().optional(),
            "bootstrapRunnerClass": t.string().optional(),
            "maxDepth": t.integer().optional(),
            "maxSteps": t.integer().optional(),
            "appInitialActivity": t.string().optional(),
        }
    ).named(renames["AndroidRoboTestIn"])
    types["AndroidRoboTestOut"] = t.struct(
        {
            "bootstrapPackageId": t.string().optional(),
            "bootstrapRunnerClass": t.string().optional(),
            "maxDepth": t.integer().optional(),
            "maxSteps": t.integer().optional(),
            "appInitialActivity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidRoboTestOut"])
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
    types["AndroidTestLoopIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AndroidTestLoopIn"]
    )
    types["AndroidTestLoopOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AndroidTestLoopOut"])
    types["MultiStepIn"] = t.struct(
        {
            "primaryStepId": t.string().optional(),
            "multistepNumber": t.integer().optional(),
            "primaryStep": t.proxy(renames["PrimaryStepIn"]).optional(),
        }
    ).named(renames["MultiStepIn"])
    types["MultiStepOut"] = t.struct(
        {
            "primaryStepId": t.string().optional(),
            "multistepNumber": t.integer().optional(),
            "primaryStep": t.proxy(renames["PrimaryStepOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultiStepOut"])
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
    types["BatchCreatePerfSamplesResponseIn"] = t.struct(
        {"perfSamples": t.array(t.proxy(renames["PerfSampleIn"]))}
    ).named(renames["BatchCreatePerfSamplesResponseIn"])
    types["BatchCreatePerfSamplesResponseOut"] = t.struct(
        {
            "perfSamples": t.array(t.proxy(renames["PerfSampleOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreatePerfSamplesResponseOut"])
    types["PerformedGoogleLoginIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PerformedGoogleLoginIn"]
    )
    types["PerformedGoogleLoginOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PerformedGoogleLoginOut"])
    types["PerfMetricsSummaryIn"] = t.struct(
        {
            "executionId": t.string().optional(),
            "perfMetrics": t.array(t.string()).optional(),
            "appStartTime": t.proxy(renames["AppStartTimeIn"]),
            "perfEnvironment": t.proxy(renames["PerfEnvironmentIn"]).optional(),
            "graphicsStats": t.proxy(renames["GraphicsStatsIn"]).optional(),
            "stepId": t.string().optional(),
            "historyId": t.string().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["PerfMetricsSummaryIn"])
    types["PerfMetricsSummaryOut"] = t.struct(
        {
            "executionId": t.string().optional(),
            "perfMetrics": t.array(t.string()).optional(),
            "appStartTime": t.proxy(renames["AppStartTimeOut"]),
            "perfEnvironment": t.proxy(renames["PerfEnvironmentOut"]).optional(),
            "graphicsStats": t.proxy(renames["GraphicsStatsOut"]).optional(),
            "stepId": t.string().optional(),
            "historyId": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerfMetricsSummaryOut"])
    types["ScreenshotClusterIn"] = t.struct(
        {
            "activity": t.string().optional(),
            "keyScreen": t.proxy(renames["ScreenIn"]).optional(),
            "screens": t.array(t.proxy(renames["ScreenIn"])).optional(),
            "clusterId": t.string().optional(),
        }
    ).named(renames["ScreenshotClusterIn"])
    types["ScreenshotClusterOut"] = t.struct(
        {
            "activity": t.string().optional(),
            "keyScreen": t.proxy(renames["ScreenOut"]).optional(),
            "screens": t.array(t.proxy(renames["ScreenOut"])).optional(),
            "clusterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScreenshotClusterOut"])
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
    types["HistoryIn"] = t.struct(
        {
            "name": t.string().optional(),
            "testPlatform": t.string().optional(),
            "displayName": t.string().optional(),
            "historyId": t.string().optional(),
        }
    ).named(renames["HistoryIn"])
    types["HistoryOut"] = t.struct(
        {
            "name": t.string().optional(),
            "testPlatform": t.string().optional(),
            "displayName": t.string().optional(),
            "historyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistoryOut"])
    types["BasicPerfSampleSeriesIn"] = t.struct(
        {
            "perfUnit": t.string(),
            "perfMetricType": t.string(),
            "sampleSeriesLabel": t.string(),
        }
    ).named(renames["BasicPerfSampleSeriesIn"])
    types["BasicPerfSampleSeriesOut"] = t.struct(
        {
            "perfUnit": t.string(),
            "perfMetricType": t.string(),
            "sampleSeriesLabel": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicPerfSampleSeriesOut"])
    types["ScreenIn"] = t.struct(
        {
            "locale": t.string().optional(),
            "model": t.string().optional(),
            "version": t.string().optional(),
            "fileReference": t.string().optional(),
        }
    ).named(renames["ScreenIn"])
    types["ScreenOut"] = t.struct(
        {
            "locale": t.string().optional(),
            "model": t.string().optional(),
            "version": t.string().optional(),
            "fileReference": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScreenOut"])
    types["ThumbnailIn"] = t.struct(
        {
            "contentType": t.string().optional(),
            "widthPx": t.integer().optional(),
            "data": t.string().optional(),
            "heightPx": t.integer().optional(),
        }
    ).named(renames["ThumbnailIn"])
    types["ThumbnailOut"] = t.struct(
        {
            "contentType": t.string().optional(),
            "widthPx": t.integer().optional(),
            "data": t.string().optional(),
            "heightPx": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThumbnailOut"])
    types["SkippedDetailIn"] = t.struct(
        {
            "incompatibleDevice": t.boolean().optional(),
            "incompatibleAppVersion": t.boolean().optional(),
            "incompatibleArchitecture": t.boolean().optional(),
        }
    ).named(renames["SkippedDetailIn"])
    types["SkippedDetailOut"] = t.struct(
        {
            "incompatibleDevice": t.boolean().optional(),
            "incompatibleAppVersion": t.boolean().optional(),
            "incompatibleArchitecture": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SkippedDetailOut"])
    types["FailedToInstallIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FailedToInstallIn"]
    )
    types["FailedToInstallOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FailedToInstallOut"])
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
    types["BlankScreenIn"] = t.struct({"screenId": t.string().optional()}).named(
        renames["BlankScreenIn"]
    )
    types["BlankScreenOut"] = t.struct(
        {
            "screenId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BlankScreenOut"])
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
    types["ListEnvironmentsResponseIn"] = t.struct(
        {
            "executionId": t.string().optional(),
            "projectId": t.string().optional(),
            "environments": t.array(t.proxy(renames["EnvironmentIn"])).optional(),
            "historyId": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListEnvironmentsResponseIn"])
    types["ListEnvironmentsResponseOut"] = t.struct(
        {
            "executionId": t.string().optional(),
            "projectId": t.string().optional(),
            "environments": t.array(t.proxy(renames["EnvironmentOut"])).optional(),
            "historyId": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEnvironmentsResponseOut"])
    types["NonSdkApiUsageViolationReportIn"] = t.struct(
        {
            "exampleApis": t.array(t.proxy(renames["NonSdkApiIn"])).optional(),
            "minSdkVersion": t.integer().optional(),
            "uniqueApis": t.integer().optional(),
            "targetSdkVersion": t.integer().optional(),
        }
    ).named(renames["NonSdkApiUsageViolationReportIn"])
    types["NonSdkApiUsageViolationReportOut"] = t.struct(
        {
            "exampleApis": t.array(t.proxy(renames["NonSdkApiOut"])).optional(),
            "minSdkVersion": t.integer().optional(),
            "uniqueApis": t.integer().optional(),
            "targetSdkVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonSdkApiUsageViolationReportOut"])
    types["PendingGoogleUpdateInsightIn"] = t.struct(
        {"nameOfGoogleLibrary": t.string().optional()}
    ).named(renames["PendingGoogleUpdateInsightIn"])
    types["PendingGoogleUpdateInsightOut"] = t.struct(
        {
            "nameOfGoogleLibrary": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PendingGoogleUpdateInsightOut"])
    types["IosAppCrashedIn"] = t.struct(
        {"stackTrace": t.proxy(renames["StackTraceIn"]).optional()}
    ).named(renames["IosAppCrashedIn"])
    types["IosAppCrashedOut"] = t.struct(
        {
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosAppCrashedOut"])
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
    types["CrashDialogErrorIn"] = t.struct(
        {"crashPackage": t.string().optional()}
    ).named(renames["CrashDialogErrorIn"])
    types["CrashDialogErrorOut"] = t.struct(
        {
            "crashPackage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CrashDialogErrorOut"])
    types["TestTimingIn"] = t.struct(
        {"testProcessDuration": t.proxy(renames["DurationIn"]).optional()}
    ).named(renames["TestTimingIn"])
    types["TestTimingOut"] = t.struct(
        {
            "testProcessDuration": t.proxy(renames["DurationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestTimingOut"])
    types["TestSuiteOverviewIn"] = t.struct(
        {
            "elapsedTime": t.proxy(renames["DurationIn"]).optional(),
            "flakyCount": t.integer().optional(),
            "xmlSource": t.proxy(renames["FileReferenceIn"]).optional(),
            "errorCount": t.integer().optional(),
            "failureCount": t.integer().optional(),
            "totalCount": t.integer().optional(),
            "name": t.string().optional(),
            "skippedCount": t.integer().optional(),
        }
    ).named(renames["TestSuiteOverviewIn"])
    types["TestSuiteOverviewOut"] = t.struct(
        {
            "elapsedTime": t.proxy(renames["DurationOut"]).optional(),
            "flakyCount": t.integer().optional(),
            "xmlSource": t.proxy(renames["FileReferenceOut"]).optional(),
            "errorCount": t.integer().optional(),
            "failureCount": t.integer().optional(),
            "totalCount": t.integer().optional(),
            "name": t.string().optional(),
            "skippedCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestSuiteOverviewOut"])
    types["DetectedAppSplashScreenIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DetectedAppSplashScreenIn"]
    )
    types["DetectedAppSplashScreenOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DetectedAppSplashScreenOut"])
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
    types["StackTraceIn"] = t.struct({"exception": t.string().optional()}).named(
        renames["StackTraceIn"]
    )
    types["StackTraceOut"] = t.struct(
        {
            "exception": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackTraceOut"])
    types["OutcomeIn"] = t.struct(
        {
            "skippedDetail": t.proxy(renames["SkippedDetailIn"]).optional(),
            "summary": t.string().optional(),
            "inconclusiveDetail": t.proxy(renames["InconclusiveDetailIn"]).optional(),
            "failureDetail": t.proxy(renames["FailureDetailIn"]).optional(),
            "successDetail": t.proxy(renames["SuccessDetailIn"]).optional(),
        }
    ).named(renames["OutcomeIn"])
    types["OutcomeOut"] = t.struct(
        {
            "skippedDetail": t.proxy(renames["SkippedDetailOut"]).optional(),
            "summary": t.string().optional(),
            "inconclusiveDetail": t.proxy(renames["InconclusiveDetailOut"]).optional(),
            "failureDetail": t.proxy(renames["FailureDetailOut"]).optional(),
            "successDetail": t.proxy(renames["SuccessDetailOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutcomeOut"])
    types["DeviceOutOfMemoryIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeviceOutOfMemoryIn"]
    )
    types["DeviceOutOfMemoryOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeviceOutOfMemoryOut"])

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
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
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
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
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
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
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
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecutionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsPublishXunitXmlFiles"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfMetricsSummary",
        t.struct(
            {
                "projectId": t.string().optional(),
                "stepId": t.string().optional(),
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PerfMetricsSummaryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsHistoriesExecutionsStepsAccessibilityClusters"
    ] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfMetricsSummary",
        t.struct(
            {
                "projectId": t.string().optional(),
                "stepId": t.string().optional(),
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PerfMetricsSummaryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsPatch"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfMetricsSummary",
        t.struct(
            {
                "projectId": t.string().optional(),
                "stepId": t.string().optional(),
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PerfMetricsSummaryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsCreate"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfMetricsSummary",
        t.struct(
            {
                "projectId": t.string().optional(),
                "stepId": t.string().optional(),
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PerfMetricsSummaryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsGet"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfMetricsSummary",
        t.struct(
            {
                "projectId": t.string().optional(),
                "stepId": t.string().optional(),
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PerfMetricsSummaryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsList"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfMetricsSummary",
        t.struct(
            {
                "projectId": t.string().optional(),
                "stepId": t.string().optional(),
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PerfMetricsSummaryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsHistoriesExecutionsStepsGetPerfMetricsSummary"
    ] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfMetricsSummary",
        t.struct(
            {
                "projectId": t.string().optional(),
                "stepId": t.string().optional(),
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
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
                "stepId": t.string().optional(),
                "pageToken": t.string().optional(),
                "historyId": t.string().optional(),
                "projectId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "executionId": t.string().optional(),
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
                "executionId": t.string().optional(),
                "projectId": t.string().optional(),
                "stepId": t.string().optional(),
                "perfMetrics": t.array(t.string()).optional(),
                "appStartTime": t.proxy(renames["AppStartTimeIn"]),
                "perfEnvironment": t.proxy(renames["PerfEnvironmentIn"]).optional(),
                "graphicsStats": t.proxy(renames["GraphicsStatsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PerfMetricsSummaryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsHistoriesExecutionsStepsPerfSampleSeriesList"
    ] = toolresults.post(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries",
        t.struct(
            {
                "historyId": t.string().optional(),
                "stepId": t.string().optional(),
                "projectId": t.string().optional(),
                "executionId": t.string().optional(),
                "basicPerfSampleSeries": t.proxy(
                    renames["BasicPerfSampleSeriesIn"]
                ).optional(),
                "sampleSeriesId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PerfSampleSeriesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsPerfSampleSeriesGet"] = toolresults.post(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries",
        t.struct(
            {
                "historyId": t.string().optional(),
                "stepId": t.string().optional(),
                "projectId": t.string().optional(),
                "executionId": t.string().optional(),
                "basicPerfSampleSeries": t.proxy(
                    renames["BasicPerfSampleSeriesIn"]
                ).optional(),
                "sampleSeriesId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PerfSampleSeriesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsHistoriesExecutionsStepsPerfSampleSeriesCreate"
    ] = toolresults.post(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries",
        t.struct(
            {
                "historyId": t.string().optional(),
                "stepId": t.string().optional(),
                "projectId": t.string().optional(),
                "executionId": t.string().optional(),
                "basicPerfSampleSeries": t.proxy(
                    renames["BasicPerfSampleSeriesIn"]
                ).optional(),
                "sampleSeriesId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PerfSampleSeriesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsHistoriesExecutionsStepsPerfSampleSeriesSamplesList"
    ] = toolresults.post(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries/{sampleSeriesId}/samples:batchCreate",
        t.struct(
            {
                "executionId": t.string().optional(),
                "sampleSeriesId": t.string().optional(),
                "historyId": t.string().optional(),
                "stepId": t.string().optional(),
                "projectId": t.string().optional(),
                "perfSamples": t.array(t.proxy(renames["PerfSampleIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchCreatePerfSamplesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsHistoriesExecutionsStepsPerfSampleSeriesSamplesBatchCreate"
    ] = toolresults.post(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries/{sampleSeriesId}/samples:batchCreate",
        t.struct(
            {
                "executionId": t.string().optional(),
                "sampleSeriesId": t.string().optional(),
                "historyId": t.string().optional(),
                "stepId": t.string().optional(),
                "projectId": t.string().optional(),
                "perfSamples": t.array(t.proxy(renames["PerfSampleIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchCreatePerfSamplesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsTestCasesGet"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/testCases",
        t.struct(
            {
                "stepId": t.string().optional(),
                "projectId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "historyId": t.string().optional(),
                "executionId": t.string().optional(),
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
                "stepId": t.string().optional(),
                "projectId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "historyId": t.string().optional(),
                "executionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTestCasesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsClustersList"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/clusters/{clusterId}",
        t.struct(
            {
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScreenshotClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsClustersGet"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/clusters/{clusterId}",
        t.struct(
            {
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScreenshotClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsEnvironmentsList"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/environments/{environmentId}",
        t.struct(
            {
                "environmentId": t.string(),
                "historyId": t.string(),
                "projectId": t.string(),
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
                "environmentId": t.string(),
                "historyId": t.string(),
                "projectId": t.string(),
                "executionId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="toolresults",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
