from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_toolresults() -> Import:
    toolresults = HTTPRuntime("https://toolresults.googleapis.com/")

    renames = {
        "ErrorResponse": "_toolresults_1_ErrorResponse",
        "StepIn": "_toolresults_2_StepIn",
        "StepOut": "_toolresults_3_StepOut",
        "ThumbnailIn": "_toolresults_4_ThumbnailIn",
        "ThumbnailOut": "_toolresults_5_ThumbnailOut",
        "PublishXunitXmlFilesRequestIn": "_toolresults_6_PublishXunitXmlFilesRequestIn",
        "PublishXunitXmlFilesRequestOut": "_toolresults_7_PublishXunitXmlFilesRequestOut",
        "SkippedDetailIn": "_toolresults_8_SkippedDetailIn",
        "SkippedDetailOut": "_toolresults_9_SkippedDetailOut",
        "TestCaseReferenceIn": "_toolresults_10_TestCaseReferenceIn",
        "TestCaseReferenceOut": "_toolresults_11_TestCaseReferenceOut",
        "IosTestLoopIn": "_toolresults_12_IosTestLoopIn",
        "IosTestLoopOut": "_toolresults_13_IosTestLoopOut",
        "ListStepAccessibilityClustersResponseIn": "_toolresults_14_ListStepAccessibilityClustersResponseIn",
        "ListStepAccessibilityClustersResponseOut": "_toolresults_15_ListStepAccessibilityClustersResponseOut",
        "FailureDetailIn": "_toolresults_16_FailureDetailIn",
        "FailureDetailOut": "_toolresults_17_FailureDetailOut",
        "ListPerfSamplesResponseIn": "_toolresults_18_ListPerfSamplesResponseIn",
        "ListPerfSamplesResponseOut": "_toolresults_19_ListPerfSamplesResponseOut",
        "IosTestIn": "_toolresults_20_IosTestIn",
        "IosTestOut": "_toolresults_21_IosTestOut",
        "IosRoboTestIn": "_toolresults_22_IosRoboTestIn",
        "IosRoboTestOut": "_toolresults_23_IosRoboTestOut",
        "GraphicsStatsIn": "_toolresults_24_GraphicsStatsIn",
        "GraphicsStatsOut": "_toolresults_25_GraphicsStatsOut",
        "FailedToInstallIn": "_toolresults_26_FailedToInstallIn",
        "FailedToInstallOut": "_toolresults_27_FailedToInstallOut",
        "ToolExecutionIn": "_toolresults_28_ToolExecutionIn",
        "ToolExecutionOut": "_toolresults_29_ToolExecutionOut",
        "SpecificationIn": "_toolresults_30_SpecificationIn",
        "SpecificationOut": "_toolresults_31_SpecificationOut",
        "StepLabelsEntryIn": "_toolresults_32_StepLabelsEntryIn",
        "StepLabelsEntryOut": "_toolresults_33_StepLabelsEntryOut",
        "DurationIn": "_toolresults_34_DurationIn",
        "DurationOut": "_toolresults_35_DurationOut",
        "UsedRoboDirectiveIn": "_toolresults_36_UsedRoboDirectiveIn",
        "UsedRoboDirectiveOut": "_toolresults_37_UsedRoboDirectiveOut",
        "ScreenshotClusterIn": "_toolresults_38_ScreenshotClusterIn",
        "ScreenshotClusterOut": "_toolresults_39_ScreenshotClusterOut",
        "AvailableDeepLinksIn": "_toolresults_40_AvailableDeepLinksIn",
        "AvailableDeepLinksOut": "_toolresults_41_AvailableDeepLinksOut",
        "BlankScreenIn": "_toolresults_42_BlankScreenIn",
        "BlankScreenOut": "_toolresults_43_BlankScreenOut",
        "ToolExecutionStepIn": "_toolresults_44_ToolExecutionStepIn",
        "ToolExecutionStepOut": "_toolresults_45_ToolExecutionStepOut",
        "PerformedGoogleLoginIn": "_toolresults_46_PerformedGoogleLoginIn",
        "PerformedGoogleLoginOut": "_toolresults_47_PerformedGoogleLoginOut",
        "UIElementTooDeepIn": "_toolresults_48_UIElementTooDeepIn",
        "UIElementTooDeepOut": "_toolresults_49_UIElementTooDeepOut",
        "HistoryIn": "_toolresults_50_HistoryIn",
        "HistoryOut": "_toolresults_51_HistoryOut",
        "RegionProtoIn": "_toolresults_52_RegionProtoIn",
        "RegionProtoOut": "_toolresults_53_RegionProtoOut",
        "ListPerfSampleSeriesResponseIn": "_toolresults_54_ListPerfSampleSeriesResponseIn",
        "ListPerfSampleSeriesResponseOut": "_toolresults_55_ListPerfSampleSeriesResponseOut",
        "SuggestionProtoIn": "_toolresults_56_SuggestionProtoIn",
        "SuggestionProtoOut": "_toolresults_57_SuggestionProtoOut",
        "MergedResultIn": "_toolresults_58_MergedResultIn",
        "MergedResultOut": "_toolresults_59_MergedResultOut",
        "ScreenIn": "_toolresults_60_ScreenIn",
        "ScreenOut": "_toolresults_61_ScreenOut",
        "AndroidTestIn": "_toolresults_62_AndroidTestIn",
        "AndroidTestOut": "_toolresults_63_AndroidTestOut",
        "IosAppCrashedIn": "_toolresults_64_IosAppCrashedIn",
        "IosAppCrashedOut": "_toolresults_65_IosAppCrashedOut",
        "DeviceOutOfMemoryIn": "_toolresults_66_DeviceOutOfMemoryIn",
        "DeviceOutOfMemoryOut": "_toolresults_67_DeviceOutOfMemoryOut",
        "PerformedMonkeyActionsIn": "_toolresults_68_PerformedMonkeyActionsIn",
        "PerformedMonkeyActionsOut": "_toolresults_69_PerformedMonkeyActionsOut",
        "IosAppInfoIn": "_toolresults_70_IosAppInfoIn",
        "IosAppInfoOut": "_toolresults_71_IosAppInfoOut",
        "MultiStepIn": "_toolresults_72_MultiStepIn",
        "MultiStepOut": "_toolresults_73_MultiStepOut",
        "CPUInfoIn": "_toolresults_74_CPUInfoIn",
        "CPUInfoOut": "_toolresults_75_CPUInfoOut",
        "AppStartTimeIn": "_toolresults_76_AppStartTimeIn",
        "AppStartTimeOut": "_toolresults_77_AppStartTimeOut",
        "ProjectSettingsIn": "_toolresults_78_ProjectSettingsIn",
        "ProjectSettingsOut": "_toolresults_79_ProjectSettingsOut",
        "ListScreenshotClustersResponseIn": "_toolresults_80_ListScreenshotClustersResponseIn",
        "ListScreenshotClustersResponseOut": "_toolresults_81_ListScreenshotClustersResponseOut",
        "InAppPurchasesFoundIn": "_toolresults_82_InAppPurchasesFoundIn",
        "InAppPurchasesFoundOut": "_toolresults_83_InAppPurchasesFoundOut",
        "ToolOutputReferenceIn": "_toolresults_84_ToolOutputReferenceIn",
        "ToolOutputReferenceOut": "_toolresults_85_ToolOutputReferenceOut",
        "NonSdkApiIn": "_toolresults_86_NonSdkApiIn",
        "NonSdkApiOut": "_toolresults_87_NonSdkApiOut",
        "AndroidTestLoopIn": "_toolresults_88_AndroidTestLoopIn",
        "AndroidTestLoopOut": "_toolresults_89_AndroidTestLoopOut",
        "FileReferenceIn": "_toolresults_90_FileReferenceIn",
        "FileReferenceOut": "_toolresults_91_FileReferenceOut",
        "StatusIn": "_toolresults_92_StatusIn",
        "StatusOut": "_toolresults_93_StatusOut",
        "SuccessDetailIn": "_toolresults_94_SuccessDetailIn",
        "SuccessDetailOut": "_toolresults_95_SuccessDetailOut",
        "AndroidRoboTestIn": "_toolresults_96_AndroidRoboTestIn",
        "AndroidRoboTestOut": "_toolresults_97_AndroidRoboTestOut",
        "ListHistoriesResponseIn": "_toolresults_98_ListHistoriesResponseIn",
        "ListHistoriesResponseOut": "_toolresults_99_ListHistoriesResponseOut",
        "BatchCreatePerfSamplesRequestIn": "_toolresults_100_BatchCreatePerfSamplesRequestIn",
        "BatchCreatePerfSamplesRequestOut": "_toolresults_101_BatchCreatePerfSamplesRequestOut",
        "UsedRoboIgnoreDirectiveIn": "_toolresults_102_UsedRoboIgnoreDirectiveIn",
        "UsedRoboIgnoreDirectiveOut": "_toolresults_103_UsedRoboIgnoreDirectiveOut",
        "SuggestionClusterProtoIn": "_toolresults_104_SuggestionClusterProtoIn",
        "SuggestionClusterProtoOut": "_toolresults_105_SuggestionClusterProtoOut",
        "StepSummaryIn": "_toolresults_106_StepSummaryIn",
        "StepSummaryOut": "_toolresults_107_StepSummaryOut",
        "ExecutionIn": "_toolresults_108_ExecutionIn",
        "ExecutionOut": "_toolresults_109_ExecutionOut",
        "ListStepsResponseIn": "_toolresults_110_ListStepsResponseIn",
        "ListStepsResponseOut": "_toolresults_111_ListStepsResponseOut",
        "PrimaryStepIn": "_toolresults_112_PrimaryStepIn",
        "PrimaryStepOut": "_toolresults_113_PrimaryStepOut",
        "AndroidAppInfoIn": "_toolresults_114_AndroidAppInfoIn",
        "AndroidAppInfoOut": "_toolresults_115_AndroidAppInfoOut",
        "InsufficientCoverageIn": "_toolresults_116_InsufficientCoverageIn",
        "InsufficientCoverageOut": "_toolresults_117_InsufficientCoverageOut",
        "UpgradeInsightIn": "_toolresults_118_UpgradeInsightIn",
        "UpgradeInsightOut": "_toolresults_119_UpgradeInsightOut",
        "UnspecifiedWarningIn": "_toolresults_120_UnspecifiedWarningIn",
        "UnspecifiedWarningOut": "_toolresults_121_UnspecifiedWarningOut",
        "IndividualOutcomeIn": "_toolresults_122_IndividualOutcomeIn",
        "IndividualOutcomeOut": "_toolresults_123_IndividualOutcomeOut",
        "PerfSampleSeriesIn": "_toolresults_124_PerfSampleSeriesIn",
        "PerfSampleSeriesOut": "_toolresults_125_PerfSampleSeriesOut",
        "TestExecutionStepIn": "_toolresults_126_TestExecutionStepIn",
        "TestExecutionStepOut": "_toolresults_127_TestExecutionStepOut",
        "EnvironmentIn": "_toolresults_128_EnvironmentIn",
        "EnvironmentOut": "_toolresults_129_EnvironmentOut",
        "StackTraceIn": "_toolresults_130_StackTraceIn",
        "StackTraceOut": "_toolresults_131_StackTraceOut",
        "ImageIn": "_toolresults_132_ImageIn",
        "ImageOut": "_toolresults_133_ImageOut",
        "AnyIn": "_toolresults_134_AnyIn",
        "AnyOut": "_toolresults_135_AnyOut",
        "ListTestCasesResponseIn": "_toolresults_136_ListTestCasesResponseIn",
        "ListTestCasesResponseOut": "_toolresults_137_ListTestCasesResponseOut",
        "InconclusiveDetailIn": "_toolresults_138_InconclusiveDetailIn",
        "InconclusiveDetailOut": "_toolresults_139_InconclusiveDetailOut",
        "NativeCrashIn": "_toolresults_140_NativeCrashIn",
        "NativeCrashOut": "_toolresults_141_NativeCrashOut",
        "EncounteredLoginScreenIn": "_toolresults_142_EncounteredLoginScreenIn",
        "EncounteredLoginScreenOut": "_toolresults_143_EncounteredLoginScreenOut",
        "TimestampIn": "_toolresults_144_TimestampIn",
        "TimestampOut": "_toolresults_145_TimestampOut",
        "SafeHtmlProtoIn": "_toolresults_146_SafeHtmlProtoIn",
        "SafeHtmlProtoOut": "_toolresults_147_SafeHtmlProtoOut",
        "BatchCreatePerfSamplesResponseIn": "_toolresults_148_BatchCreatePerfSamplesResponseIn",
        "BatchCreatePerfSamplesResponseOut": "_toolresults_149_BatchCreatePerfSamplesResponseOut",
        "CrashDialogErrorIn": "_toolresults_150_CrashDialogErrorIn",
        "CrashDialogErrorOut": "_toolresults_151_CrashDialogErrorOut",
        "PendingGoogleUpdateInsightIn": "_toolresults_152_PendingGoogleUpdateInsightIn",
        "PendingGoogleUpdateInsightOut": "_toolresults_153_PendingGoogleUpdateInsightOut",
        "LauncherActivityNotFoundIn": "_toolresults_154_LauncherActivityNotFoundIn",
        "LauncherActivityNotFoundOut": "_toolresults_155_LauncherActivityNotFoundOut",
        "NonSdkApiInsightIn": "_toolresults_156_NonSdkApiInsightIn",
        "NonSdkApiInsightOut": "_toolresults_157_NonSdkApiInsightOut",
        "StartActivityNotFoundIn": "_toolresults_158_StartActivityNotFoundIn",
        "StartActivityNotFoundOut": "_toolresults_159_StartActivityNotFoundOut",
        "ListStepThumbnailsResponseIn": "_toolresults_160_ListStepThumbnailsResponseIn",
        "ListStepThumbnailsResponseOut": "_toolresults_161_ListStepThumbnailsResponseOut",
        "TestIssueIn": "_toolresults_162_TestIssueIn",
        "TestIssueOut": "_toolresults_163_TestIssueOut",
        "TestTimingIn": "_toolresults_164_TestTimingIn",
        "TestTimingOut": "_toolresults_165_TestTimingOut",
        "NonSdkApiUsageViolationIn": "_toolresults_166_NonSdkApiUsageViolationIn",
        "NonSdkApiUsageViolationOut": "_toolresults_167_NonSdkApiUsageViolationOut",
        "FatalExceptionIn": "_toolresults_168_FatalExceptionIn",
        "FatalExceptionOut": "_toolresults_169_FatalExceptionOut",
        "EncounteredNonAndroidUiWidgetScreenIn": "_toolresults_170_EncounteredNonAndroidUiWidgetScreenIn",
        "EncounteredNonAndroidUiWidgetScreenOut": "_toolresults_171_EncounteredNonAndroidUiWidgetScreenOut",
        "TestCaseIn": "_toolresults_172_TestCaseIn",
        "TestCaseOut": "_toolresults_173_TestCaseOut",
        "NonSdkApiUsageViolationReportIn": "_toolresults_174_NonSdkApiUsageViolationReportIn",
        "NonSdkApiUsageViolationReportOut": "_toolresults_175_NonSdkApiUsageViolationReportOut",
        "AndroidInstrumentationTestIn": "_toolresults_176_AndroidInstrumentationTestIn",
        "AndroidInstrumentationTestOut": "_toolresults_177_AndroidInstrumentationTestOut",
        "ANRIn": "_toolresults_178_ANRIn",
        "ANROut": "_toolresults_179_ANROut",
        "MemoryInfoIn": "_toolresults_180_MemoryInfoIn",
        "MemoryInfoOut": "_toolresults_181_MemoryInfoOut",
        "EnvironmentDimensionValueEntryIn": "_toolresults_182_EnvironmentDimensionValueEntryIn",
        "EnvironmentDimensionValueEntryOut": "_toolresults_183_EnvironmentDimensionValueEntryOut",
        "GraphicsStatsBucketIn": "_toolresults_184_GraphicsStatsBucketIn",
        "GraphicsStatsBucketOut": "_toolresults_185_GraphicsStatsBucketOut",
        "ShardSummaryIn": "_toolresults_186_ShardSummaryIn",
        "ShardSummaryOut": "_toolresults_187_ShardSummaryOut",
        "ResultsStorageIn": "_toolresults_188_ResultsStorageIn",
        "ResultsStorageOut": "_toolresults_189_ResultsStorageOut",
        "StepDimensionValueEntryIn": "_toolresults_190_StepDimensionValueEntryIn",
        "StepDimensionValueEntryOut": "_toolresults_191_StepDimensionValueEntryOut",
        "PerfEnvironmentIn": "_toolresults_192_PerfEnvironmentIn",
        "PerfEnvironmentOut": "_toolresults_193_PerfEnvironmentOut",
        "OutcomeIn": "_toolresults_194_OutcomeIn",
        "OutcomeOut": "_toolresults_195_OutcomeOut",
        "LogcatCollectionErrorIn": "_toolresults_196_LogcatCollectionErrorIn",
        "LogcatCollectionErrorOut": "_toolresults_197_LogcatCollectionErrorOut",
        "MatrixDimensionDefinitionIn": "_toolresults_198_MatrixDimensionDefinitionIn",
        "MatrixDimensionDefinitionOut": "_toolresults_199_MatrixDimensionDefinitionOut",
        "ListExecutionsResponseIn": "_toolresults_200_ListExecutionsResponseIn",
        "ListExecutionsResponseOut": "_toolresults_201_ListExecutionsResponseOut",
        "PerfSampleIn": "_toolresults_202_PerfSampleIn",
        "PerfSampleOut": "_toolresults_203_PerfSampleOut",
        "TestSuiteOverviewIn": "_toolresults_204_TestSuiteOverviewIn",
        "TestSuiteOverviewOut": "_toolresults_205_TestSuiteOverviewOut",
        "UnusedRoboDirectiveIn": "_toolresults_206_UnusedRoboDirectiveIn",
        "UnusedRoboDirectiveOut": "_toolresults_207_UnusedRoboDirectiveOut",
        "ToolExitCodeIn": "_toolresults_208_ToolExitCodeIn",
        "ToolExitCodeOut": "_toolresults_209_ToolExitCodeOut",
        "IosXcTestIn": "_toolresults_210_IosXcTestIn",
        "IosXcTestOut": "_toolresults_211_IosXcTestOut",
        "ListEnvironmentsResponseIn": "_toolresults_212_ListEnvironmentsResponseIn",
        "ListEnvironmentsResponseOut": "_toolresults_213_ListEnvironmentsResponseOut",
        "DetectedAppSplashScreenIn": "_toolresults_214_DetectedAppSplashScreenIn",
        "DetectedAppSplashScreenOut": "_toolresults_215_DetectedAppSplashScreenOut",
        "RoboScriptExecutionIn": "_toolresults_216_RoboScriptExecutionIn",
        "RoboScriptExecutionOut": "_toolresults_217_RoboScriptExecutionOut",
        "PerfMetricsSummaryIn": "_toolresults_218_PerfMetricsSummaryIn",
        "PerfMetricsSummaryOut": "_toolresults_219_PerfMetricsSummaryOut",
        "BasicPerfSampleSeriesIn": "_toolresults_220_BasicPerfSampleSeriesIn",
        "BasicPerfSampleSeriesOut": "_toolresults_221_BasicPerfSampleSeriesOut",
        "OverlappingUIElementsIn": "_toolresults_222_OverlappingUIElementsIn",
        "OverlappingUIElementsOut": "_toolresults_223_OverlappingUIElementsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["StepIn"] = t.struct(
        {
            "state": t.string().optional(),
            "name": t.string().optional(),
            "testExecutionStep": t.proxy(renames["TestExecutionStepIn"]).optional(),
            "description": t.string().optional(),
            "runDuration": t.proxy(renames["DurationIn"]).optional(),
            "labels": t.array(t.proxy(renames["StepLabelsEntryIn"])).optional(),
            "completionTime": t.proxy(renames["TimestampIn"]).optional(),
            "outcome": t.proxy(renames["OutcomeIn"]).optional(),
            "creationTime": t.proxy(renames["TimestampIn"]).optional(),
            "stepId": t.string().optional(),
            "toolExecutionStep": t.proxy(renames["ToolExecutionStepIn"]).optional(),
            "hasImages": t.boolean().optional(),
            "deviceUsageDuration": t.proxy(renames["DurationIn"]).optional(),
            "multiStep": t.proxy(renames["MultiStepIn"]).optional(),
            "dimensionValue": t.array(
                t.proxy(renames["StepDimensionValueEntryIn"])
            ).optional(),
        }
    ).named(renames["StepIn"])
    types["StepOut"] = t.struct(
        {
            "state": t.string().optional(),
            "name": t.string().optional(),
            "testExecutionStep": t.proxy(renames["TestExecutionStepOut"]).optional(),
            "description": t.string().optional(),
            "runDuration": t.proxy(renames["DurationOut"]).optional(),
            "labels": t.array(t.proxy(renames["StepLabelsEntryOut"])).optional(),
            "completionTime": t.proxy(renames["TimestampOut"]).optional(),
            "outcome": t.proxy(renames["OutcomeOut"]).optional(),
            "creationTime": t.proxy(renames["TimestampOut"]).optional(),
            "stepId": t.string().optional(),
            "toolExecutionStep": t.proxy(renames["ToolExecutionStepOut"]).optional(),
            "hasImages": t.boolean().optional(),
            "deviceUsageDuration": t.proxy(renames["DurationOut"]).optional(),
            "multiStep": t.proxy(renames["MultiStepOut"]).optional(),
            "dimensionValue": t.array(
                t.proxy(renames["StepDimensionValueEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StepOut"])
    types["ThumbnailIn"] = t.struct(
        {
            "heightPx": t.integer().optional(),
            "contentType": t.string().optional(),
            "data": t.string().optional(),
            "widthPx": t.integer().optional(),
        }
    ).named(renames["ThumbnailIn"])
    types["ThumbnailOut"] = t.struct(
        {
            "heightPx": t.integer().optional(),
            "contentType": t.string().optional(),
            "data": t.string().optional(),
            "widthPx": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThumbnailOut"])
    types["PublishXunitXmlFilesRequestIn"] = t.struct(
        {"xunitXmlFiles": t.array(t.proxy(renames["FileReferenceIn"])).optional()}
    ).named(renames["PublishXunitXmlFilesRequestIn"])
    types["PublishXunitXmlFilesRequestOut"] = t.struct(
        {
            "xunitXmlFiles": t.array(t.proxy(renames["FileReferenceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishXunitXmlFilesRequestOut"])
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
    types["TestCaseReferenceIn"] = t.struct(
        {
            "testSuiteName": t.string().optional(),
            "className": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["TestCaseReferenceIn"])
    types["TestCaseReferenceOut"] = t.struct(
        {
            "testSuiteName": t.string().optional(),
            "className": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestCaseReferenceOut"])
    types["IosTestLoopIn"] = t.struct({"bundleId": t.string().optional()}).named(
        renames["IosTestLoopIn"]
    )
    types["IosTestLoopOut"] = t.struct(
        {
            "bundleId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosTestLoopOut"])
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
    types["FailureDetailIn"] = t.struct(
        {
            "crashed": t.boolean().optional(),
            "failedRoboscript": t.boolean().optional(),
            "notInstalled": t.boolean().optional(),
            "otherNativeCrash": t.boolean().optional(),
            "deviceOutOfMemory": t.boolean().optional(),
            "timedOut": t.boolean().optional(),
            "unableToCrawl": t.boolean().optional(),
        }
    ).named(renames["FailureDetailIn"])
    types["FailureDetailOut"] = t.struct(
        {
            "crashed": t.boolean().optional(),
            "failedRoboscript": t.boolean().optional(),
            "notInstalled": t.boolean().optional(),
            "otherNativeCrash": t.boolean().optional(),
            "deviceOutOfMemory": t.boolean().optional(),
            "timedOut": t.boolean().optional(),
            "unableToCrawl": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FailureDetailOut"])
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
    types["IosTestIn"] = t.struct(
        {
            "iosAppInfo": t.proxy(renames["IosAppInfoIn"]).optional(),
            "testTimeout": t.proxy(renames["DurationIn"]).optional(),
            "iosTestLoop": t.proxy(renames["IosTestLoopIn"]).optional(),
            "iosRoboTest": t.proxy(renames["IosRoboTestIn"]).optional(),
            "iosXcTest": t.proxy(renames["IosXcTestIn"]).optional(),
        }
    ).named(renames["IosTestIn"])
    types["IosTestOut"] = t.struct(
        {
            "iosAppInfo": t.proxy(renames["IosAppInfoOut"]).optional(),
            "testTimeout": t.proxy(renames["DurationOut"]).optional(),
            "iosTestLoop": t.proxy(renames["IosTestLoopOut"]).optional(),
            "iosRoboTest": t.proxy(renames["IosRoboTestOut"]).optional(),
            "iosXcTest": t.proxy(renames["IosXcTestOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosTestOut"])
    types["IosRoboTestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["IosRoboTestIn"]
    )
    types["IosRoboTestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["IosRoboTestOut"])
    types["GraphicsStatsIn"] = t.struct(
        {
            "missedVsyncCount": t.string().optional(),
            "buckets": t.array(t.proxy(renames["GraphicsStatsBucketIn"])).optional(),
            "jankyFrames": t.string().optional(),
            "p99Millis": t.string().optional(),
            "totalFrames": t.string().optional(),
            "p90Millis": t.string().optional(),
            "slowUiThreadCount": t.string().optional(),
            "p50Millis": t.string().optional(),
            "slowBitmapUploadCount": t.string().optional(),
            "slowDrawCount": t.string().optional(),
            "p95Millis": t.string().optional(),
            "highInputLatencyCount": t.string().optional(),
        }
    ).named(renames["GraphicsStatsIn"])
    types["GraphicsStatsOut"] = t.struct(
        {
            "missedVsyncCount": t.string().optional(),
            "buckets": t.array(t.proxy(renames["GraphicsStatsBucketOut"])).optional(),
            "jankyFrames": t.string().optional(),
            "p99Millis": t.string().optional(),
            "totalFrames": t.string().optional(),
            "p90Millis": t.string().optional(),
            "slowUiThreadCount": t.string().optional(),
            "p50Millis": t.string().optional(),
            "slowBitmapUploadCount": t.string().optional(),
            "slowDrawCount": t.string().optional(),
            "p95Millis": t.string().optional(),
            "highInputLatencyCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GraphicsStatsOut"])
    types["FailedToInstallIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FailedToInstallIn"]
    )
    types["FailedToInstallOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FailedToInstallOut"])
    types["ToolExecutionIn"] = t.struct(
        {
            "toolOutputs": t.array(
                t.proxy(renames["ToolOutputReferenceIn"])
            ).optional(),
            "exitCode": t.proxy(renames["ToolExitCodeIn"]).optional(),
            "toolLogs": t.array(t.proxy(renames["FileReferenceIn"])).optional(),
            "commandLineArguments": t.array(t.string()).optional(),
        }
    ).named(renames["ToolExecutionIn"])
    types["ToolExecutionOut"] = t.struct(
        {
            "toolOutputs": t.array(
                t.proxy(renames["ToolOutputReferenceOut"])
            ).optional(),
            "exitCode": t.proxy(renames["ToolExitCodeOut"]).optional(),
            "toolLogs": t.array(t.proxy(renames["FileReferenceOut"])).optional(),
            "commandLineArguments": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ToolExecutionOut"])
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
    types["UsedRoboDirectiveIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["UsedRoboDirectiveIn"])
    types["UsedRoboDirectiveOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsedRoboDirectiveOut"])
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
    types["AvailableDeepLinksIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AvailableDeepLinksIn"]
    )
    types["AvailableDeepLinksOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AvailableDeepLinksOut"])
    types["BlankScreenIn"] = t.struct({"screenId": t.string().optional()}).named(
        renames["BlankScreenIn"]
    )
    types["BlankScreenOut"] = t.struct(
        {
            "screenId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BlankScreenOut"])
    types["ToolExecutionStepIn"] = t.struct(
        {"toolExecution": t.proxy(renames["ToolExecutionIn"]).optional()}
    ).named(renames["ToolExecutionStepIn"])
    types["ToolExecutionStepOut"] = t.struct(
        {
            "toolExecution": t.proxy(renames["ToolExecutionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ToolExecutionStepOut"])
    types["PerformedGoogleLoginIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PerformedGoogleLoginIn"]
    )
    types["PerformedGoogleLoginOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PerformedGoogleLoginOut"])
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
    types["HistoryIn"] = t.struct(
        {
            "testPlatform": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "historyId": t.string().optional(),
        }
    ).named(renames["HistoryIn"])
    types["HistoryOut"] = t.struct(
        {
            "testPlatform": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "historyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistoryOut"])
    types["RegionProtoIn"] = t.struct(
        {
            "widthPx": t.integer().optional(),
            "leftPx": t.integer().optional(),
            "heightPx": t.integer().optional(),
            "topPx": t.integer().optional(),
        }
    ).named(renames["RegionProtoIn"])
    types["RegionProtoOut"] = t.struct(
        {
            "widthPx": t.integer().optional(),
            "leftPx": t.integer().optional(),
            "heightPx": t.integer().optional(),
            "topPx": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegionProtoOut"])
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
    types["SuggestionProtoIn"] = t.struct(
        {
            "longMessage": t.proxy(renames["SafeHtmlProtoIn"]).optional(),
            "pseudoResourceId": t.string().optional(),
            "title": t.string().optional(),
            "shortMessage": t.proxy(renames["SafeHtmlProtoIn"]).optional(),
            "screenId": t.string().optional(),
            "secondaryPriority": t.number().optional(),
            "resourceName": t.string().optional(),
            "priority": t.string().optional(),
            "helpUrl": t.string().optional(),
            "region": t.proxy(renames["RegionProtoIn"]).optional(),
        }
    ).named(renames["SuggestionProtoIn"])
    types["SuggestionProtoOut"] = t.struct(
        {
            "longMessage": t.proxy(renames["SafeHtmlProtoOut"]).optional(),
            "pseudoResourceId": t.string().optional(),
            "title": t.string().optional(),
            "shortMessage": t.proxy(renames["SafeHtmlProtoOut"]).optional(),
            "screenId": t.string().optional(),
            "secondaryPriority": t.number().optional(),
            "resourceName": t.string().optional(),
            "priority": t.string().optional(),
            "helpUrl": t.string().optional(),
            "region": t.proxy(renames["RegionProtoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestionProtoOut"])
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
    types["ScreenIn"] = t.struct(
        {
            "version": t.string().optional(),
            "locale": t.string().optional(),
            "model": t.string().optional(),
            "fileReference": t.string().optional(),
        }
    ).named(renames["ScreenIn"])
    types["ScreenOut"] = t.struct(
        {
            "version": t.string().optional(),
            "locale": t.string().optional(),
            "model": t.string().optional(),
            "fileReference": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScreenOut"])
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
    types["IosAppCrashedIn"] = t.struct(
        {"stackTrace": t.proxy(renames["StackTraceIn"]).optional()}
    ).named(renames["IosAppCrashedIn"])
    types["IosAppCrashedOut"] = t.struct(
        {
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosAppCrashedOut"])
    types["DeviceOutOfMemoryIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeviceOutOfMemoryIn"]
    )
    types["DeviceOutOfMemoryOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeviceOutOfMemoryOut"])
    types["PerformedMonkeyActionsIn"] = t.struct(
        {"totalActions": t.integer().optional()}
    ).named(renames["PerformedMonkeyActionsIn"])
    types["PerformedMonkeyActionsOut"] = t.struct(
        {
            "totalActions": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerformedMonkeyActionsOut"])
    types["IosAppInfoIn"] = t.struct({"name": t.string().optional()}).named(
        renames["IosAppInfoIn"]
    )
    types["IosAppInfoOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosAppInfoOut"])
    types["MultiStepIn"] = t.struct(
        {
            "multistepNumber": t.integer().optional(),
            "primaryStepId": t.string().optional(),
            "primaryStep": t.proxy(renames["PrimaryStepIn"]).optional(),
        }
    ).named(renames["MultiStepIn"])
    types["MultiStepOut"] = t.struct(
        {
            "multistepNumber": t.integer().optional(),
            "primaryStepId": t.string().optional(),
            "primaryStep": t.proxy(renames["PrimaryStepOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultiStepOut"])
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
    types["ListScreenshotClustersResponseIn"] = t.struct(
        {"clusters": t.array(t.proxy(renames["ScreenshotClusterIn"])).optional()}
    ).named(renames["ListScreenshotClustersResponseIn"])
    types["ListScreenshotClustersResponseOut"] = t.struct(
        {
            "clusters": t.array(t.proxy(renames["ScreenshotClusterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListScreenshotClustersResponseOut"])
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
    types["NonSdkApiIn"] = t.struct(
        {
            "list": t.string().optional(),
            "exampleStackTraces": t.array(t.string()).optional(),
            "insights": t.array(t.proxy(renames["NonSdkApiInsightIn"])).optional(),
            "apiSignature": t.string().optional(),
            "invocationCount": t.integer().optional(),
        }
    ).named(renames["NonSdkApiIn"])
    types["NonSdkApiOut"] = t.struct(
        {
            "list": t.string().optional(),
            "exampleStackTraces": t.array(t.string()).optional(),
            "insights": t.array(t.proxy(renames["NonSdkApiInsightOut"])).optional(),
            "apiSignature": t.string().optional(),
            "invocationCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonSdkApiOut"])
    types["AndroidTestLoopIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AndroidTestLoopIn"]
    )
    types["AndroidTestLoopOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AndroidTestLoopOut"])
    types["FileReferenceIn"] = t.struct({"fileUri": t.string().optional()}).named(
        renames["FileReferenceIn"]
    )
    types["FileReferenceOut"] = t.struct(
        {
            "fileUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileReferenceOut"])
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
    types["SuccessDetailIn"] = t.struct(
        {"otherNativeCrash": t.boolean().optional()}
    ).named(renames["SuccessDetailIn"])
    types["SuccessDetailOut"] = t.struct(
        {
            "otherNativeCrash": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuccessDetailOut"])
    types["AndroidRoboTestIn"] = t.struct(
        {
            "maxSteps": t.integer().optional(),
            "appInitialActivity": t.string().optional(),
            "bootstrapPackageId": t.string().optional(),
            "bootstrapRunnerClass": t.string().optional(),
            "maxDepth": t.integer().optional(),
        }
    ).named(renames["AndroidRoboTestIn"])
    types["AndroidRoboTestOut"] = t.struct(
        {
            "maxSteps": t.integer().optional(),
            "appInitialActivity": t.string().optional(),
            "bootstrapPackageId": t.string().optional(),
            "bootstrapRunnerClass": t.string().optional(),
            "maxDepth": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidRoboTestOut"])
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
    types["BatchCreatePerfSamplesRequestIn"] = t.struct(
        {"perfSamples": t.array(t.proxy(renames["PerfSampleIn"])).optional()}
    ).named(renames["BatchCreatePerfSamplesRequestIn"])
    types["BatchCreatePerfSamplesRequestOut"] = t.struct(
        {
            "perfSamples": t.array(t.proxy(renames["PerfSampleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreatePerfSamplesRequestOut"])
    types["UsedRoboIgnoreDirectiveIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["UsedRoboIgnoreDirectiveIn"])
    types["UsedRoboIgnoreDirectiveOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsedRoboIgnoreDirectiveOut"])
    types["SuggestionClusterProtoIn"] = t.struct(
        {
            "suggestions": t.array(t.proxy(renames["SuggestionProtoIn"])).optional(),
            "category": t.string().optional(),
        }
    ).named(renames["SuggestionClusterProtoIn"])
    types["SuggestionClusterProtoOut"] = t.struct(
        {
            "suggestions": t.array(t.proxy(renames["SuggestionProtoOut"])).optional(),
            "category": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuggestionClusterProtoOut"])
    types["StepSummaryIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StepSummaryIn"]
    )
    types["StepSummaryOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StepSummaryOut"])
    types["ExecutionIn"] = t.struct(
        {
            "executionId": t.string().optional(),
            "completionTime": t.proxy(renames["TimestampIn"]).optional(),
            "dimensionDefinitions": t.array(
                t.proxy(renames["MatrixDimensionDefinitionIn"])
            ).optional(),
            "state": t.string().optional(),
            "specification": t.proxy(renames["SpecificationIn"]).optional(),
            "outcome": t.proxy(renames["OutcomeIn"]).optional(),
            "testExecutionMatrixId": t.string().optional(),
            "creationTime": t.proxy(renames["TimestampIn"]).optional(),
        }
    ).named(renames["ExecutionIn"])
    types["ExecutionOut"] = t.struct(
        {
            "executionId": t.string().optional(),
            "completionTime": t.proxy(renames["TimestampOut"]).optional(),
            "dimensionDefinitions": t.array(
                t.proxy(renames["MatrixDimensionDefinitionOut"])
            ).optional(),
            "state": t.string().optional(),
            "specification": t.proxy(renames["SpecificationOut"]).optional(),
            "outcome": t.proxy(renames["OutcomeOut"]).optional(),
            "testExecutionMatrixId": t.string().optional(),
            "creationTime": t.proxy(renames["TimestampOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionOut"])
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
    types["AndroidAppInfoIn"] = t.struct(
        {
            "versionCode": t.string().optional(),
            "packageName": t.string().optional(),
            "name": t.string().optional(),
            "versionName": t.string().optional(),
        }
    ).named(renames["AndroidAppInfoIn"])
    types["AndroidAppInfoOut"] = t.struct(
        {
            "versionCode": t.string().optional(),
            "packageName": t.string().optional(),
            "name": t.string().optional(),
            "versionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidAppInfoOut"])
    types["InsufficientCoverageIn"] = t.struct({"_": t.string().optional()}).named(
        renames["InsufficientCoverageIn"]
    )
    types["InsufficientCoverageOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["InsufficientCoverageOut"])
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
    types["UnspecifiedWarningIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UnspecifiedWarningIn"]
    )
    types["UnspecifiedWarningOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UnspecifiedWarningOut"])
    types["IndividualOutcomeIn"] = t.struct(
        {
            "stepId": t.string(),
            "runDuration": t.proxy(renames["DurationIn"]).optional(),
            "multistepNumber": t.integer().optional(),
            "outcomeSummary": t.string(),
        }
    ).named(renames["IndividualOutcomeIn"])
    types["IndividualOutcomeOut"] = t.struct(
        {
            "stepId": t.string(),
            "runDuration": t.proxy(renames["DurationOut"]).optional(),
            "multistepNumber": t.integer().optional(),
            "outcomeSummary": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndividualOutcomeOut"])
    types["PerfSampleSeriesIn"] = t.struct(
        {
            "basicPerfSampleSeries": t.proxy(
                renames["BasicPerfSampleSeriesIn"]
            ).optional(),
            "historyId": t.string().optional(),
            "executionId": t.string().optional(),
            "stepId": t.string().optional(),
            "projectId": t.string().optional(),
            "sampleSeriesId": t.string().optional(),
        }
    ).named(renames["PerfSampleSeriesIn"])
    types["PerfSampleSeriesOut"] = t.struct(
        {
            "basicPerfSampleSeries": t.proxy(
                renames["BasicPerfSampleSeriesOut"]
            ).optional(),
            "historyId": t.string().optional(),
            "executionId": t.string().optional(),
            "stepId": t.string().optional(),
            "projectId": t.string().optional(),
            "sampleSeriesId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerfSampleSeriesOut"])
    types["TestExecutionStepIn"] = t.struct(
        {
            "testIssues": t.array(t.proxy(renames["TestIssueIn"])).optional(),
            "testSuiteOverviews": t.array(
                t.proxy(renames["TestSuiteOverviewIn"])
            ).optional(),
            "testTiming": t.proxy(renames["TestTimingIn"]).optional(),
            "toolExecution": t.proxy(renames["ToolExecutionIn"]).optional(),
        }
    ).named(renames["TestExecutionStepIn"])
    types["TestExecutionStepOut"] = t.struct(
        {
            "testIssues": t.array(t.proxy(renames["TestIssueOut"])).optional(),
            "testSuiteOverviews": t.array(
                t.proxy(renames["TestSuiteOverviewOut"])
            ).optional(),
            "testTiming": t.proxy(renames["TestTimingOut"]).optional(),
            "toolExecution": t.proxy(renames["ToolExecutionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestExecutionStepOut"])
    types["EnvironmentIn"] = t.struct(
        {
            "executionId": t.string().optional(),
            "shardSummaries": t.array(t.proxy(renames["ShardSummaryIn"])).optional(),
            "completionTime": t.proxy(renames["TimestampIn"]).optional(),
            "environmentResult": t.proxy(renames["MergedResultIn"]).optional(),
            "historyId": t.string().optional(),
            "creationTime": t.proxy(renames["TimestampIn"]).optional(),
            "dimensionValue": t.array(
                t.proxy(renames["EnvironmentDimensionValueEntryIn"])
            ).optional(),
            "environmentId": t.string().optional(),
            "projectId": t.string().optional(),
            "displayName": t.string().optional(),
            "resultsStorage": t.proxy(renames["ResultsStorageIn"]).optional(),
        }
    ).named(renames["EnvironmentIn"])
    types["EnvironmentOut"] = t.struct(
        {
            "executionId": t.string().optional(),
            "shardSummaries": t.array(t.proxy(renames["ShardSummaryOut"])).optional(),
            "completionTime": t.proxy(renames["TimestampOut"]).optional(),
            "environmentResult": t.proxy(renames["MergedResultOut"]).optional(),
            "historyId": t.string().optional(),
            "creationTime": t.proxy(renames["TimestampOut"]).optional(),
            "dimensionValue": t.array(
                t.proxy(renames["EnvironmentDimensionValueEntryOut"])
            ).optional(),
            "environmentId": t.string().optional(),
            "projectId": t.string().optional(),
            "displayName": t.string().optional(),
            "resultsStorage": t.proxy(renames["ResultsStorageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentOut"])
    types["StackTraceIn"] = t.struct({"exception": t.string().optional()}).named(
        renames["StackTraceIn"]
    )
    types["StackTraceOut"] = t.struct(
        {
            "exception": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackTraceOut"])
    types["ImageIn"] = t.struct(
        {
            "thumbnail": t.proxy(renames["ThumbnailIn"]).optional(),
            "sourceImage": t.proxy(renames["ToolOutputReferenceIn"]).optional(),
            "stepId": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "thumbnail": t.proxy(renames["ThumbnailOut"]).optional(),
            "sourceImage": t.proxy(renames["ToolOutputReferenceOut"]).optional(),
            "stepId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
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
    types["InconclusiveDetailIn"] = t.struct(
        {
            "abortedByUser": t.boolean().optional(),
            "hasErrorLogs": t.boolean().optional(),
            "infrastructureFailure": t.boolean().optional(),
        }
    ).named(renames["InconclusiveDetailIn"])
    types["InconclusiveDetailOut"] = t.struct(
        {
            "abortedByUser": t.boolean().optional(),
            "hasErrorLogs": t.boolean().optional(),
            "infrastructureFailure": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InconclusiveDetailOut"])
    types["NativeCrashIn"] = t.struct(
        {"stackTrace": t.proxy(renames["StackTraceIn"]).optional()}
    ).named(renames["NativeCrashIn"])
    types["NativeCrashOut"] = t.struct(
        {
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NativeCrashOut"])
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
    types["SafeHtmlProtoIn"] = t.struct(
        {"privateDoNotAccessOrElseSafeHtmlWrappedValue": t.string().optional()}
    ).named(renames["SafeHtmlProtoIn"])
    types["SafeHtmlProtoOut"] = t.struct(
        {
            "privateDoNotAccessOrElseSafeHtmlWrappedValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SafeHtmlProtoOut"])
    types["BatchCreatePerfSamplesResponseIn"] = t.struct(
        {"perfSamples": t.array(t.proxy(renames["PerfSampleIn"]))}
    ).named(renames["BatchCreatePerfSamplesResponseIn"])
    types["BatchCreatePerfSamplesResponseOut"] = t.struct(
        {
            "perfSamples": t.array(t.proxy(renames["PerfSampleOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreatePerfSamplesResponseOut"])
    types["CrashDialogErrorIn"] = t.struct(
        {"crashPackage": t.string().optional()}
    ).named(renames["CrashDialogErrorIn"])
    types["CrashDialogErrorOut"] = t.struct(
        {
            "crashPackage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CrashDialogErrorOut"])
    types["PendingGoogleUpdateInsightIn"] = t.struct(
        {"nameOfGoogleLibrary": t.string().optional()}
    ).named(renames["PendingGoogleUpdateInsightIn"])
    types["PendingGoogleUpdateInsightOut"] = t.struct(
        {
            "nameOfGoogleLibrary": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PendingGoogleUpdateInsightOut"])
    types["LauncherActivityNotFoundIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LauncherActivityNotFoundIn"]
    )
    types["LauncherActivityNotFoundOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LauncherActivityNotFoundOut"])
    types["NonSdkApiInsightIn"] = t.struct(
        {
            "upgradeInsight": t.proxy(renames["UpgradeInsightIn"]).optional(),
            "exampleTraceMessages": t.array(t.string()).optional(),
            "matcherId": t.string().optional(),
            "pendingGoogleUpdateInsight": t.proxy(
                renames["PendingGoogleUpdateInsightIn"]
            ).optional(),
        }
    ).named(renames["NonSdkApiInsightIn"])
    types["NonSdkApiInsightOut"] = t.struct(
        {
            "upgradeInsight": t.proxy(renames["UpgradeInsightOut"]).optional(),
            "exampleTraceMessages": t.array(t.string()).optional(),
            "matcherId": t.string().optional(),
            "pendingGoogleUpdateInsight": t.proxy(
                renames["PendingGoogleUpdateInsightOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonSdkApiInsightOut"])
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
    types["TestIssueIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "category": t.string().optional(),
            "type": t.string().optional(),
            "warning": t.proxy(renames["AnyIn"]).optional(),
            "errorMessage": t.string().optional(),
            "stackTrace": t.proxy(renames["StackTraceIn"]).optional(),
        }
    ).named(renames["TestIssueIn"])
    types["TestIssueOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "category": t.string().optional(),
            "type": t.string().optional(),
            "warning": t.proxy(renames["AnyOut"]).optional(),
            "errorMessage": t.string().optional(),
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIssueOut"])
    types["TestTimingIn"] = t.struct(
        {"testProcessDuration": t.proxy(renames["DurationIn"]).optional()}
    ).named(renames["TestTimingIn"])
    types["TestTimingOut"] = t.struct(
        {
            "testProcessDuration": t.proxy(renames["DurationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestTimingOut"])
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
    types["FatalExceptionIn"] = t.struct(
        {"stackTrace": t.proxy(renames["StackTraceIn"]).optional()}
    ).named(renames["FatalExceptionIn"])
    types["FatalExceptionOut"] = t.struct(
        {
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FatalExceptionOut"])
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
    types["TestCaseIn"] = t.struct(
        {
            "testCaseId": t.string().optional(),
            "stackTraces": t.array(t.proxy(renames["StackTraceIn"])).optional(),
            "endTime": t.proxy(renames["TimestampIn"]).optional(),
            "skippedMessage": t.string().optional(),
            "toolOutputs": t.array(
                t.proxy(renames["ToolOutputReferenceIn"])
            ).optional(),
            "testCaseReference": t.proxy(renames["TestCaseReferenceIn"]).optional(),
            "startTime": t.proxy(renames["TimestampIn"]).optional(),
            "status": t.string().optional(),
            "elapsedTime": t.proxy(renames["DurationIn"]).optional(),
        }
    ).named(renames["TestCaseIn"])
    types["TestCaseOut"] = t.struct(
        {
            "testCaseId": t.string().optional(),
            "stackTraces": t.array(t.proxy(renames["StackTraceOut"])).optional(),
            "endTime": t.proxy(renames["TimestampOut"]).optional(),
            "skippedMessage": t.string().optional(),
            "toolOutputs": t.array(
                t.proxy(renames["ToolOutputReferenceOut"])
            ).optional(),
            "testCaseReference": t.proxy(renames["TestCaseReferenceOut"]).optional(),
            "startTime": t.proxy(renames["TimestampOut"]).optional(),
            "status": t.string().optional(),
            "elapsedTime": t.proxy(renames["DurationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestCaseOut"])
    types["NonSdkApiUsageViolationReportIn"] = t.struct(
        {
            "exampleApis": t.array(t.proxy(renames["NonSdkApiIn"])).optional(),
            "targetSdkVersion": t.integer().optional(),
            "minSdkVersion": t.integer().optional(),
            "uniqueApis": t.integer().optional(),
        }
    ).named(renames["NonSdkApiUsageViolationReportIn"])
    types["NonSdkApiUsageViolationReportOut"] = t.struct(
        {
            "exampleApis": t.array(t.proxy(renames["NonSdkApiOut"])).optional(),
            "targetSdkVersion": t.integer().optional(),
            "minSdkVersion": t.integer().optional(),
            "uniqueApis": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonSdkApiUsageViolationReportOut"])
    types["AndroidInstrumentationTestIn"] = t.struct(
        {
            "useOrchestrator": t.boolean().optional(),
            "testRunnerClass": t.string().optional(),
            "testPackageId": t.string().optional(),
            "testTargets": t.array(t.string()).optional(),
        }
    ).named(renames["AndroidInstrumentationTestIn"])
    types["AndroidInstrumentationTestOut"] = t.struct(
        {
            "useOrchestrator": t.boolean().optional(),
            "testRunnerClass": t.string().optional(),
            "testPackageId": t.string().optional(),
            "testTargets": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidInstrumentationTestOut"])
    types["ANRIn"] = t.struct(
        {"stackTrace": t.proxy(renames["StackTraceIn"]).optional()}
    ).named(renames["ANRIn"])
    types["ANROut"] = t.struct(
        {
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ANROut"])
    types["MemoryInfoIn"] = t.struct(
        {
            "memoryTotalInKibibyte": t.string().optional(),
            "memoryCapInKibibyte": t.string().optional(),
        }
    ).named(renames["MemoryInfoIn"])
    types["MemoryInfoOut"] = t.struct(
        {
            "memoryTotalInKibibyte": t.string().optional(),
            "memoryCapInKibibyte": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemoryInfoOut"])
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
    types["GraphicsStatsBucketIn"] = t.struct(
        {"renderMillis": t.string().optional(), "frameCount": t.string().optional()}
    ).named(renames["GraphicsStatsBucketIn"])
    types["GraphicsStatsBucketOut"] = t.struct(
        {
            "renderMillis": t.string().optional(),
            "frameCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GraphicsStatsBucketOut"])
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
    types["OutcomeIn"] = t.struct(
        {
            "successDetail": t.proxy(renames["SuccessDetailIn"]).optional(),
            "skippedDetail": t.proxy(renames["SkippedDetailIn"]).optional(),
            "inconclusiveDetail": t.proxy(renames["InconclusiveDetailIn"]).optional(),
            "summary": t.string().optional(),
            "failureDetail": t.proxy(renames["FailureDetailIn"]).optional(),
        }
    ).named(renames["OutcomeIn"])
    types["OutcomeOut"] = t.struct(
        {
            "successDetail": t.proxy(renames["SuccessDetailOut"]).optional(),
            "skippedDetail": t.proxy(renames["SkippedDetailOut"]).optional(),
            "inconclusiveDetail": t.proxy(renames["InconclusiveDetailOut"]).optional(),
            "summary": t.string().optional(),
            "failureDetail": t.proxy(renames["FailureDetailOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutcomeOut"])
    types["LogcatCollectionErrorIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LogcatCollectionErrorIn"]
    )
    types["LogcatCollectionErrorOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LogcatCollectionErrorOut"])
    types["MatrixDimensionDefinitionIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MatrixDimensionDefinitionIn"]
    )
    types["MatrixDimensionDefinitionOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MatrixDimensionDefinitionOut"])
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
    types["TestSuiteOverviewIn"] = t.struct(
        {
            "skippedCount": t.integer().optional(),
            "errorCount": t.integer().optional(),
            "name": t.string().optional(),
            "elapsedTime": t.proxy(renames["DurationIn"]).optional(),
            "xmlSource": t.proxy(renames["FileReferenceIn"]).optional(),
            "failureCount": t.integer().optional(),
            "flakyCount": t.integer().optional(),
            "totalCount": t.integer().optional(),
        }
    ).named(renames["TestSuiteOverviewIn"])
    types["TestSuiteOverviewOut"] = t.struct(
        {
            "skippedCount": t.integer().optional(),
            "errorCount": t.integer().optional(),
            "name": t.string().optional(),
            "elapsedTime": t.proxy(renames["DurationOut"]).optional(),
            "xmlSource": t.proxy(renames["FileReferenceOut"]).optional(),
            "failureCount": t.integer().optional(),
            "flakyCount": t.integer().optional(),
            "totalCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestSuiteOverviewOut"])
    types["UnusedRoboDirectiveIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["UnusedRoboDirectiveIn"])
    types["UnusedRoboDirectiveOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnusedRoboDirectiveOut"])
    types["ToolExitCodeIn"] = t.struct({"number": t.integer().optional()}).named(
        renames["ToolExitCodeIn"]
    )
    types["ToolExitCodeOut"] = t.struct(
        {
            "number": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ToolExitCodeOut"])
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
    types["ListEnvironmentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "historyId": t.string().optional(),
            "projectId": t.string().optional(),
            "executionId": t.string().optional(),
            "environments": t.array(t.proxy(renames["EnvironmentIn"])).optional(),
        }
    ).named(renames["ListEnvironmentsResponseIn"])
    types["ListEnvironmentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "historyId": t.string().optional(),
            "projectId": t.string().optional(),
            "executionId": t.string().optional(),
            "environments": t.array(t.proxy(renames["EnvironmentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEnvironmentsResponseOut"])
    types["DetectedAppSplashScreenIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DetectedAppSplashScreenIn"]
    )
    types["DetectedAppSplashScreenOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DetectedAppSplashScreenOut"])
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
    types["PerfMetricsSummaryIn"] = t.struct(
        {
            "appStartTime": t.proxy(renames["AppStartTimeIn"]),
            "executionId": t.string().optional(),
            "historyId": t.string().optional(),
            "perfEnvironment": t.proxy(renames["PerfEnvironmentIn"]).optional(),
            "perfMetrics": t.array(t.string()).optional(),
            "graphicsStats": t.proxy(renames["GraphicsStatsIn"]).optional(),
            "stepId": t.string().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["PerfMetricsSummaryIn"])
    types["PerfMetricsSummaryOut"] = t.struct(
        {
            "appStartTime": t.proxy(renames["AppStartTimeOut"]),
            "executionId": t.string().optional(),
            "historyId": t.string().optional(),
            "perfEnvironment": t.proxy(renames["PerfEnvironmentOut"]).optional(),
            "perfMetrics": t.array(t.string()).optional(),
            "graphicsStats": t.proxy(renames["GraphicsStatsOut"]).optional(),
            "stepId": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerfMetricsSummaryOut"])
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
    functions["projectsHistoriesGet"] = toolresults.post(
        "toolresults/v1beta3/projects/{projectId}/histories",
        t.struct(
            {
                "requestId": t.string().optional(),
                "projectId": t.string().optional(),
                "testPlatform": t.string().optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "historyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HistoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesList"] = toolresults.post(
        "toolresults/v1beta3/projects/{projectId}/histories",
        t.struct(
            {
                "requestId": t.string().optional(),
                "projectId": t.string().optional(),
                "testPlatform": t.string().optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "historyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HistoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesCreate"] = toolresults.post(
        "toolresults/v1beta3/projects/{projectId}/histories",
        t.struct(
            {
                "requestId": t.string().optional(),
                "projectId": t.string().optional(),
                "testPlatform": t.string().optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "historyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HistoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsGet"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions",
        t.struct(
            {
                "projectId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "historyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExecutionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsCreate"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions",
        t.struct(
            {
                "projectId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "historyId": t.string().optional(),
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
                "projectId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "historyId": t.string().optional(),
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
                "projectId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "historyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExecutionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsClustersGet"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/clusters",
        t.struct(
            {
                "historyId": t.string().optional(),
                "projectId": t.string().optional(),
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
                "historyId": t.string().optional(),
                "projectId": t.string().optional(),
                "executionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScreenshotClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsEnvironmentsList"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/environments/{environmentId}",
        t.struct(
            {
                "historyId": t.string(),
                "environmentId": t.string(),
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
                "historyId": t.string(),
                "environmentId": t.string(),
                "projectId": t.string(),
                "executionId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EnvironmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsPatch"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps",
        t.struct(
            {
                "projectId": t.string().optional(),
                "pageToken": t.string().optional(),
                "historyId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "executionId": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "historyId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "executionId": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "historyId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "executionId": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "historyId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "executionId": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "historyId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "executionId": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "historyId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "executionId": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "historyId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "executionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListStepsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsHistoriesExecutionsStepsPerfMetricsSummaryCreate"
    ] = toolresults.post(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfMetricsSummary",
        t.struct(
            {
                "stepId": t.string().optional(),
                "historyId": t.string().optional(),
                "projectId": t.string().optional(),
                "executionId": t.string().optional(),
                "appStartTime": t.proxy(renames["AppStartTimeIn"]),
                "perfEnvironment": t.proxy(renames["PerfEnvironmentIn"]).optional(),
                "perfMetrics": t.array(t.string()).optional(),
                "graphicsStats": t.proxy(renames["GraphicsStatsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PerfMetricsSummaryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsPerfSampleSeriesGet"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries",
        t.struct(
            {
                "filter": t.string().optional(),
                "stepId": t.string().optional(),
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPerfSampleSeriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsHistoriesExecutionsStepsPerfSampleSeriesCreate"
    ] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries",
        t.struct(
            {
                "filter": t.string().optional(),
                "stepId": t.string().optional(),
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPerfSampleSeriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsPerfSampleSeriesList"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries",
        t.struct(
            {
                "filter": t.string().optional(),
                "stepId": t.string().optional(),
                "executionId": t.string().optional(),
                "historyId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPerfSampleSeriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsHistoriesExecutionsStepsPerfSampleSeriesSamplesBatchCreate"
    ] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries/{sampleSeriesId}/samples",
        t.struct(
            {
                "executionId": t.string().optional(),
                "pageToken": t.string().optional(),
                "sampleSeriesId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "stepId": t.string().optional(),
                "historyId": t.string().optional(),
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
                "executionId": t.string().optional(),
                "pageToken": t.string().optional(),
                "sampleSeriesId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "stepId": t.string().optional(),
                "historyId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPerfSamplesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsTestCasesList"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/testCases/{testCaseId}",
        t.struct(
            {
                "stepId": t.string().optional(),
                "executionId": t.string().optional(),
                "testCaseId": t.string().optional(),
                "projectId": t.string().optional(),
                "historyId": t.string().optional(),
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
                "stepId": t.string().optional(),
                "executionId": t.string().optional(),
                "testCaseId": t.string().optional(),
                "projectId": t.string().optional(),
                "historyId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestCaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHistoriesExecutionsStepsThumbnailsList"] = toolresults.get(
        "toolresults/v1beta3/projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/thumbnails",
        t.struct(
            {
                "historyId": t.string().optional(),
                "executionId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "stepId": t.string().optional(),
                "pageToken": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListStepThumbnailsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="toolresults", renames=renames, types=types, functions=functions
    )
