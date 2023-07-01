from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_testing():
    testing = HTTPRuntime("https://testing.googleapis.com/")

    renames = {
        "ErrorResponse": "_testing_1_ErrorResponse",
        "TrafficRuleIn": "_testing_2_TrafficRuleIn",
        "TrafficRuleOut": "_testing_3_TrafficRuleOut",
        "ManualShardingIn": "_testing_4_ManualShardingIn",
        "ManualShardingOut": "_testing_5_ManualShardingOut",
        "DateIn": "_testing_6_DateIn",
        "DateOut": "_testing_7_DateOut",
        "ProvidedSoftwareCatalogIn": "_testing_8_ProvidedSoftwareCatalogIn",
        "ProvidedSoftwareCatalogOut": "_testing_9_ProvidedSoftwareCatalogOut",
        "AppBundleIn": "_testing_10_AppBundleIn",
        "AppBundleOut": "_testing_11_AppBundleOut",
        "ToolResultsStepIn": "_testing_12_ToolResultsStepIn",
        "ToolResultsStepOut": "_testing_13_ToolResultsStepOut",
        "MetadataIn": "_testing_14_MetadataIn",
        "MetadataOut": "_testing_15_MetadataOut",
        "ServiceIn": "_testing_16_ServiceIn",
        "ServiceOut": "_testing_17_ServiceOut",
        "EnvironmentMatrixIn": "_testing_18_EnvironmentMatrixIn",
        "EnvironmentMatrixOut": "_testing_19_EnvironmentMatrixOut",
        "ShardingOptionIn": "_testing_20_ShardingOptionIn",
        "ShardingOptionOut": "_testing_21_ShardingOptionOut",
        "TestExecutionIn": "_testing_22_TestExecutionIn",
        "TestExecutionOut": "_testing_23_TestExecutionOut",
        "IosTestLoopIn": "_testing_24_IosTestLoopIn",
        "IosTestLoopOut": "_testing_25_IosTestLoopOut",
        "AndroidDeviceIn": "_testing_26_AndroidDeviceIn",
        "AndroidDeviceOut": "_testing_27_AndroidDeviceOut",
        "RoboStartingIntentIn": "_testing_28_RoboStartingIntentIn",
        "RoboStartingIntentOut": "_testing_29_RoboStartingIntentOut",
        "DeviceFileIn": "_testing_30_DeviceFileIn",
        "DeviceFileOut": "_testing_31_DeviceFileOut",
        "ToolResultsHistoryIn": "_testing_32_ToolResultsHistoryIn",
        "ToolResultsHistoryOut": "_testing_33_ToolResultsHistoryOut",
        "IosXcTestIn": "_testing_34_IosXcTestIn",
        "IosXcTestOut": "_testing_35_IosXcTestOut",
        "IntentFilterIn": "_testing_36_IntentFilterIn",
        "IntentFilterOut": "_testing_37_IntentFilterOut",
        "EnvironmentVariableIn": "_testing_38_EnvironmentVariableIn",
        "EnvironmentVariableOut": "_testing_39_EnvironmentVariableOut",
        "StartActivityIntentIn": "_testing_40_StartActivityIntentIn",
        "StartActivityIntentOut": "_testing_41_StartActivityIntentOut",
        "DeviceIpBlockIn": "_testing_42_DeviceIpBlockIn",
        "DeviceIpBlockOut": "_testing_43_DeviceIpBlockOut",
        "DeviceIpBlockCatalogIn": "_testing_44_DeviceIpBlockCatalogIn",
        "DeviceIpBlockCatalogOut": "_testing_45_DeviceIpBlockCatalogOut",
        "TestMatrixIn": "_testing_46_TestMatrixIn",
        "TestMatrixOut": "_testing_47_TestMatrixOut",
        "IosDeviceCatalogIn": "_testing_48_IosDeviceCatalogIn",
        "IosDeviceCatalogOut": "_testing_49_IosDeviceCatalogOut",
        "UsesFeatureIn": "_testing_50_UsesFeatureIn",
        "UsesFeatureOut": "_testing_51_UsesFeatureOut",
        "ToolResultsExecutionIn": "_testing_52_ToolResultsExecutionIn",
        "ToolResultsExecutionOut": "_testing_53_ToolResultsExecutionOut",
        "IosModelIn": "_testing_54_IosModelIn",
        "IosModelOut": "_testing_55_IosModelOut",
        "GoogleAutoIn": "_testing_56_GoogleAutoIn",
        "GoogleAutoOut": "_testing_57_GoogleAutoOut",
        "IosRuntimeConfigurationIn": "_testing_58_IosRuntimeConfigurationIn",
        "IosRuntimeConfigurationOut": "_testing_59_IosRuntimeConfigurationOut",
        "IosDeviceIn": "_testing_60_IosDeviceIn",
        "IosDeviceOut": "_testing_61_IosDeviceOut",
        "XcodeVersionIn": "_testing_62_XcodeVersionIn",
        "XcodeVersionOut": "_testing_63_XcodeVersionOut",
        "TestEnvironmentCatalogIn": "_testing_64_TestEnvironmentCatalogIn",
        "TestEnvironmentCatalogOut": "_testing_65_TestEnvironmentCatalogOut",
        "NetworkConfigurationCatalogIn": "_testing_66_NetworkConfigurationCatalogIn",
        "NetworkConfigurationCatalogOut": "_testing_67_NetworkConfigurationCatalogOut",
        "LauncherActivityIntentIn": "_testing_68_LauncherActivityIntentIn",
        "LauncherActivityIntentOut": "_testing_69_LauncherActivityIntentOut",
        "ObbFileIn": "_testing_70_ObbFileIn",
        "ObbFileOut": "_testing_71_ObbFileOut",
        "AndroidTestLoopIn": "_testing_72_AndroidTestLoopIn",
        "AndroidTestLoopOut": "_testing_73_AndroidTestLoopOut",
        "ApkIn": "_testing_74_ApkIn",
        "ApkOut": "_testing_75_ApkOut",
        "SystraceSetupIn": "_testing_76_SystraceSetupIn",
        "SystraceSetupOut": "_testing_77_SystraceSetupOut",
        "UniformShardingIn": "_testing_78_UniformShardingIn",
        "UniformShardingOut": "_testing_79_UniformShardingOut",
        "CancelTestMatrixResponseIn": "_testing_80_CancelTestMatrixResponseIn",
        "CancelTestMatrixResponseOut": "_testing_81_CancelTestMatrixResponseOut",
        "AndroidInstrumentationTestIn": "_testing_82_AndroidInstrumentationTestIn",
        "AndroidInstrumentationTestOut": "_testing_83_AndroidInstrumentationTestOut",
        "EnvironmentIn": "_testing_84_EnvironmentIn",
        "EnvironmentOut": "_testing_85_EnvironmentOut",
        "AndroidDeviceCatalogIn": "_testing_86_AndroidDeviceCatalogIn",
        "AndroidDeviceCatalogOut": "_testing_87_AndroidDeviceCatalogOut",
        "AndroidRuntimeConfigurationIn": "_testing_88_AndroidRuntimeConfigurationIn",
        "AndroidRuntimeConfigurationOut": "_testing_89_AndroidRuntimeConfigurationOut",
        "TestSetupIn": "_testing_90_TestSetupIn",
        "TestSetupOut": "_testing_91_TestSetupOut",
        "ApkManifestIn": "_testing_92_ApkManifestIn",
        "ApkManifestOut": "_testing_93_ApkManifestOut",
        "TestDetailsIn": "_testing_94_TestDetailsIn",
        "TestDetailsOut": "_testing_95_TestDetailsOut",
        "AndroidDeviceListIn": "_testing_96_AndroidDeviceListIn",
        "AndroidDeviceListOut": "_testing_97_AndroidDeviceListOut",
        "AndroidModelIn": "_testing_98_AndroidModelIn",
        "AndroidModelOut": "_testing_99_AndroidModelOut",
        "FileReferenceIn": "_testing_100_FileReferenceIn",
        "FileReferenceOut": "_testing_101_FileReferenceOut",
        "AndroidRoboTestIn": "_testing_102_AndroidRoboTestIn",
        "AndroidRoboTestOut": "_testing_103_AndroidRoboTestOut",
        "SmartShardingIn": "_testing_104_SmartShardingIn",
        "SmartShardingOut": "_testing_105_SmartShardingOut",
        "AndroidVersionIn": "_testing_106_AndroidVersionIn",
        "AndroidVersionOut": "_testing_107_AndroidVersionOut",
        "ShardIn": "_testing_108_ShardIn",
        "ShardOut": "_testing_109_ShardOut",
        "DistributionIn": "_testing_110_DistributionIn",
        "DistributionOut": "_testing_111_DistributionOut",
        "NoActivityIntentIn": "_testing_112_NoActivityIntentIn",
        "NoActivityIntentOut": "_testing_113_NoActivityIntentOut",
        "RoboDirectiveIn": "_testing_114_RoboDirectiveIn",
        "RoboDirectiveOut": "_testing_115_RoboDirectiveOut",
        "PerIosVersionInfoIn": "_testing_116_PerIosVersionInfoIn",
        "PerIosVersionInfoOut": "_testing_117_PerIosVersionInfoOut",
        "OrientationIn": "_testing_118_OrientationIn",
        "OrientationOut": "_testing_119_OrientationOut",
        "LocaleIn": "_testing_120_LocaleIn",
        "LocaleOut": "_testing_121_LocaleOut",
        "GetApkDetailsResponseIn": "_testing_122_GetApkDetailsResponseIn",
        "GetApkDetailsResponseOut": "_testing_123_GetApkDetailsResponseOut",
        "AndroidMatrixIn": "_testing_124_AndroidMatrixIn",
        "AndroidMatrixOut": "_testing_125_AndroidMatrixOut",
        "IosDeviceFileIn": "_testing_126_IosDeviceFileIn",
        "IosDeviceFileOut": "_testing_127_IosDeviceFileOut",
        "TestTargetsForShardIn": "_testing_128_TestTargetsForShardIn",
        "TestTargetsForShardOut": "_testing_129_TestTargetsForShardOut",
        "TestSpecificationIn": "_testing_130_TestSpecificationIn",
        "TestSpecificationOut": "_testing_131_TestSpecificationOut",
        "PerAndroidVersionInfoIn": "_testing_132_PerAndroidVersionInfoIn",
        "PerAndroidVersionInfoOut": "_testing_133_PerAndroidVersionInfoOut",
        "ClientInfoIn": "_testing_134_ClientInfoIn",
        "ClientInfoOut": "_testing_135_ClientInfoOut",
        "IosVersionIn": "_testing_136_IosVersionIn",
        "IosVersionOut": "_testing_137_IosVersionOut",
        "IosDeviceListIn": "_testing_138_IosDeviceListIn",
        "IosDeviceListOut": "_testing_139_IosDeviceListOut",
        "ClientInfoDetailIn": "_testing_140_ClientInfoDetailIn",
        "ClientInfoDetailOut": "_testing_141_ClientInfoDetailOut",
        "ResultStorageIn": "_testing_142_ResultStorageIn",
        "ResultStorageOut": "_testing_143_ResultStorageOut",
        "IosTestSetupIn": "_testing_144_IosTestSetupIn",
        "IosTestSetupOut": "_testing_145_IosTestSetupOut",
        "ApkDetailIn": "_testing_146_ApkDetailIn",
        "ApkDetailOut": "_testing_147_ApkDetailOut",
        "AccountIn": "_testing_148_AccountIn",
        "AccountOut": "_testing_149_AccountOut",
        "GoogleCloudStorageIn": "_testing_150_GoogleCloudStorageIn",
        "GoogleCloudStorageOut": "_testing_151_GoogleCloudStorageOut",
        "NetworkConfigurationIn": "_testing_152_NetworkConfigurationIn",
        "NetworkConfigurationOut": "_testing_153_NetworkConfigurationOut",
        "RegularFileIn": "_testing_154_RegularFileIn",
        "RegularFileOut": "_testing_155_RegularFileOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TrafficRuleIn"] = t.struct(
        {
            "delay": t.string().optional(),
            "packetDuplicationRatio": t.number().optional(),
            "bandwidth": t.number().optional(),
            "burst": t.number().optional(),
            "packetLossRatio": t.number().optional(),
        }
    ).named(renames["TrafficRuleIn"])
    types["TrafficRuleOut"] = t.struct(
        {
            "delay": t.string().optional(),
            "packetDuplicationRatio": t.number().optional(),
            "bandwidth": t.number().optional(),
            "burst": t.number().optional(),
            "packetLossRatio": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrafficRuleOut"])
    types["ManualShardingIn"] = t.struct(
        {"testTargetsForShard": t.array(t.proxy(renames["TestTargetsForShardIn"]))}
    ).named(renames["ManualShardingIn"])
    types["ManualShardingOut"] = t.struct(
        {
            "testTargetsForShard": t.array(t.proxy(renames["TestTargetsForShardOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManualShardingOut"])
    types["DateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["ProvidedSoftwareCatalogIn"] = t.struct(
        {
            "orchestratorVersion": t.string().optional(),
            "androidxOrchestratorVersion": t.string().optional(),
        }
    ).named(renames["ProvidedSoftwareCatalogIn"])
    types["ProvidedSoftwareCatalogOut"] = t.struct(
        {
            "orchestratorVersion": t.string().optional(),
            "androidxOrchestratorVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProvidedSoftwareCatalogOut"])
    types["AppBundleIn"] = t.struct(
        {"bundleLocation": t.proxy(renames["FileReferenceIn"]).optional()}
    ).named(renames["AppBundleIn"])
    types["AppBundleOut"] = t.struct(
        {
            "bundleLocation": t.proxy(renames["FileReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppBundleOut"])
    types["ToolResultsStepIn"] = t.struct(
        {
            "historyId": t.string().optional(),
            "projectId": t.string().optional(),
            "executionId": t.string().optional(),
            "stepId": t.string().optional(),
        }
    ).named(renames["ToolResultsStepIn"])
    types["ToolResultsStepOut"] = t.struct(
        {
            "historyId": t.string().optional(),
            "projectId": t.string().optional(),
            "executionId": t.string().optional(),
            "stepId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ToolResultsStepOut"])
    types["MetadataIn"] = t.struct(
        {"value": t.string().optional(), "name": t.string().optional()}
    ).named(renames["MetadataIn"])
    types["MetadataOut"] = t.struct(
        {
            "value": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["ServiceIn"] = t.struct(
        {
            "intentFilter": t.array(t.proxy(renames["IntentFilterIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "intentFilter": t.array(t.proxy(renames["IntentFilterOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
    types["EnvironmentMatrixIn"] = t.struct(
        {
            "androidMatrix": t.proxy(renames["AndroidMatrixIn"]).optional(),
            "iosDeviceList": t.proxy(renames["IosDeviceListIn"]).optional(),
            "androidDeviceList": t.proxy(renames["AndroidDeviceListIn"]).optional(),
        }
    ).named(renames["EnvironmentMatrixIn"])
    types["EnvironmentMatrixOut"] = t.struct(
        {
            "androidMatrix": t.proxy(renames["AndroidMatrixOut"]).optional(),
            "iosDeviceList": t.proxy(renames["IosDeviceListOut"]).optional(),
            "androidDeviceList": t.proxy(renames["AndroidDeviceListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentMatrixOut"])
    types["ShardingOptionIn"] = t.struct(
        {
            "smartSharding": t.proxy(renames["SmartShardingIn"]).optional(),
            "manualSharding": t.proxy(renames["ManualShardingIn"]).optional(),
            "uniformSharding": t.proxy(renames["UniformShardingIn"]).optional(),
        }
    ).named(renames["ShardingOptionIn"])
    types["ShardingOptionOut"] = t.struct(
        {
            "smartSharding": t.proxy(renames["SmartShardingOut"]).optional(),
            "manualSharding": t.proxy(renames["ManualShardingOut"]).optional(),
            "uniformSharding": t.proxy(renames["UniformShardingOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShardingOptionOut"])
    types["TestExecutionIn"] = t.struct(
        {
            "state": t.string().optional(),
            "projectId": t.string().optional(),
            "toolResultsStep": t.proxy(renames["ToolResultsStepIn"]).optional(),
            "environment": t.proxy(renames["EnvironmentIn"]).optional(),
            "matrixId": t.string().optional(),
            "id": t.string().optional(),
            "shard": t.proxy(renames["ShardIn"]).optional(),
            "timestamp": t.string().optional(),
            "testDetails": t.proxy(renames["TestDetailsIn"]).optional(),
            "testSpecification": t.proxy(renames["TestSpecificationIn"]).optional(),
        }
    ).named(renames["TestExecutionIn"])
    types["TestExecutionOut"] = t.struct(
        {
            "state": t.string().optional(),
            "projectId": t.string().optional(),
            "toolResultsStep": t.proxy(renames["ToolResultsStepOut"]).optional(),
            "environment": t.proxy(renames["EnvironmentOut"]).optional(),
            "matrixId": t.string().optional(),
            "id": t.string().optional(),
            "shard": t.proxy(renames["ShardOut"]).optional(),
            "timestamp": t.string().optional(),
            "testDetails": t.proxy(renames["TestDetailsOut"]).optional(),
            "testSpecification": t.proxy(renames["TestSpecificationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestExecutionOut"])
    types["IosTestLoopIn"] = t.struct(
        {
            "appBundleId": t.string().optional(),
            "appIpa": t.proxy(renames["FileReferenceIn"]),
            "scenarios": t.array(t.integer()).optional(),
        }
    ).named(renames["IosTestLoopIn"])
    types["IosTestLoopOut"] = t.struct(
        {
            "appBundleId": t.string().optional(),
            "appIpa": t.proxy(renames["FileReferenceOut"]),
            "scenarios": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosTestLoopOut"])
    types["AndroidDeviceIn"] = t.struct(
        {
            "locale": t.string(),
            "androidModelId": t.string(),
            "orientation": t.string(),
            "androidVersionId": t.string(),
        }
    ).named(renames["AndroidDeviceIn"])
    types["AndroidDeviceOut"] = t.struct(
        {
            "locale": t.string(),
            "androidModelId": t.string(),
            "orientation": t.string(),
            "androidVersionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidDeviceOut"])
    types["RoboStartingIntentIn"] = t.struct(
        {
            "timeout": t.string().optional(),
            "startActivity": t.proxy(renames["StartActivityIntentIn"]).optional(),
            "launcherActivity": t.proxy(renames["LauncherActivityIntentIn"]).optional(),
            "noActivity": t.proxy(renames["NoActivityIntentIn"]).optional(),
        }
    ).named(renames["RoboStartingIntentIn"])
    types["RoboStartingIntentOut"] = t.struct(
        {
            "timeout": t.string().optional(),
            "startActivity": t.proxy(renames["StartActivityIntentOut"]).optional(),
            "launcherActivity": t.proxy(
                renames["LauncherActivityIntentOut"]
            ).optional(),
            "noActivity": t.proxy(renames["NoActivityIntentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RoboStartingIntentOut"])
    types["DeviceFileIn"] = t.struct(
        {
            "regularFile": t.proxy(renames["RegularFileIn"]).optional(),
            "obbFile": t.proxy(renames["ObbFileIn"]).optional(),
        }
    ).named(renames["DeviceFileIn"])
    types["DeviceFileOut"] = t.struct(
        {
            "regularFile": t.proxy(renames["RegularFileOut"]).optional(),
            "obbFile": t.proxy(renames["ObbFileOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceFileOut"])
    types["ToolResultsHistoryIn"] = t.struct(
        {"projectId": t.string(), "historyId": t.string()}
    ).named(renames["ToolResultsHistoryIn"])
    types["ToolResultsHistoryOut"] = t.struct(
        {
            "projectId": t.string(),
            "historyId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ToolResultsHistoryOut"])
    types["IosXcTestIn"] = t.struct(
        {
            "xctestrun": t.proxy(renames["FileReferenceIn"]).optional(),
            "appBundleId": t.string().optional(),
            "testSpecialEntitlements": t.boolean().optional(),
            "xcodeVersion": t.string().optional(),
            "testsZip": t.proxy(renames["FileReferenceIn"]),
        }
    ).named(renames["IosXcTestIn"])
    types["IosXcTestOut"] = t.struct(
        {
            "xctestrun": t.proxy(renames["FileReferenceOut"]).optional(),
            "appBundleId": t.string().optional(),
            "testSpecialEntitlements": t.boolean().optional(),
            "xcodeVersion": t.string().optional(),
            "testsZip": t.proxy(renames["FileReferenceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosXcTestOut"])
    types["IntentFilterIn"] = t.struct(
        {
            "actionNames": t.array(t.string()).optional(),
            "mimeType": t.string().optional(),
            "categoryNames": t.array(t.string()).optional(),
        }
    ).named(renames["IntentFilterIn"])
    types["IntentFilterOut"] = t.struct(
        {
            "actionNames": t.array(t.string()).optional(),
            "mimeType": t.string().optional(),
            "categoryNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntentFilterOut"])
    types["EnvironmentVariableIn"] = t.struct(
        {"key": t.string().optional(), "value": t.string().optional()}
    ).named(renames["EnvironmentVariableIn"])
    types["EnvironmentVariableOut"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentVariableOut"])
    types["StartActivityIntentIn"] = t.struct(
        {
            "categories": t.array(t.string()).optional(),
            "action": t.string().optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["StartActivityIntentIn"])
    types["StartActivityIntentOut"] = t.struct(
        {
            "categories": t.array(t.string()).optional(),
            "action": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartActivityIntentOut"])
    types["DeviceIpBlockIn"] = t.struct(
        {
            "addedDate": t.proxy(renames["DateIn"]).optional(),
            "block": t.string().optional(),
            "form": t.string().optional(),
        }
    ).named(renames["DeviceIpBlockIn"])
    types["DeviceIpBlockOut"] = t.struct(
        {
            "addedDate": t.proxy(renames["DateOut"]).optional(),
            "block": t.string().optional(),
            "form": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceIpBlockOut"])
    types["DeviceIpBlockCatalogIn"] = t.struct(
        {"ipBlocks": t.array(t.proxy(renames["DeviceIpBlockIn"])).optional()}
    ).named(renames["DeviceIpBlockCatalogIn"])
    types["DeviceIpBlockCatalogOut"] = t.struct(
        {
            "ipBlocks": t.array(t.proxy(renames["DeviceIpBlockOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceIpBlockCatalogOut"])
    types["TestMatrixIn"] = t.struct(
        {
            "invalidMatrixDetails": t.string().optional(),
            "testMatrixId": t.string().optional(),
            "environmentMatrix": t.proxy(renames["EnvironmentMatrixIn"]),
            "failFast": t.boolean().optional(),
            "flakyTestAttempts": t.integer().optional(),
            "timestamp": t.string().optional(),
            "outcomeSummary": t.string().optional(),
            "testSpecification": t.proxy(renames["TestSpecificationIn"]),
            "testExecutions": t.array(t.proxy(renames["TestExecutionIn"])).optional(),
            "clientInfo": t.proxy(renames["ClientInfoIn"]).optional(),
            "state": t.string().optional(),
            "resultStorage": t.proxy(renames["ResultStorageIn"]),
            "projectId": t.string().optional(),
        }
    ).named(renames["TestMatrixIn"])
    types["TestMatrixOut"] = t.struct(
        {
            "invalidMatrixDetails": t.string().optional(),
            "testMatrixId": t.string().optional(),
            "environmentMatrix": t.proxy(renames["EnvironmentMatrixOut"]),
            "failFast": t.boolean().optional(),
            "flakyTestAttempts": t.integer().optional(),
            "timestamp": t.string().optional(),
            "outcomeSummary": t.string().optional(),
            "testSpecification": t.proxy(renames["TestSpecificationOut"]),
            "testExecutions": t.array(t.proxy(renames["TestExecutionOut"])).optional(),
            "clientInfo": t.proxy(renames["ClientInfoOut"]).optional(),
            "state": t.string().optional(),
            "resultStorage": t.proxy(renames["ResultStorageOut"]),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestMatrixOut"])
    types["IosDeviceCatalogIn"] = t.struct(
        {
            "runtimeConfiguration": t.proxy(
                renames["IosRuntimeConfigurationIn"]
            ).optional(),
            "xcodeVersions": t.array(t.proxy(renames["XcodeVersionIn"])).optional(),
            "models": t.array(t.proxy(renames["IosModelIn"])).optional(),
            "versions": t.array(t.proxy(renames["IosVersionIn"])).optional(),
        }
    ).named(renames["IosDeviceCatalogIn"])
    types["IosDeviceCatalogOut"] = t.struct(
        {
            "runtimeConfiguration": t.proxy(
                renames["IosRuntimeConfigurationOut"]
            ).optional(),
            "xcodeVersions": t.array(t.proxy(renames["XcodeVersionOut"])).optional(),
            "models": t.array(t.proxy(renames["IosModelOut"])).optional(),
            "versions": t.array(t.proxy(renames["IosVersionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosDeviceCatalogOut"])
    types["UsesFeatureIn"] = t.struct(
        {"name": t.string().optional(), "isRequired": t.boolean().optional()}
    ).named(renames["UsesFeatureIn"])
    types["UsesFeatureOut"] = t.struct(
        {
            "name": t.string().optional(),
            "isRequired": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsesFeatureOut"])
    types["ToolResultsExecutionIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "executionId": t.string().optional(),
            "historyId": t.string().optional(),
        }
    ).named(renames["ToolResultsExecutionIn"])
    types["ToolResultsExecutionOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "executionId": t.string().optional(),
            "historyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ToolResultsExecutionOut"])
    types["IosModelIn"] = t.struct(
        {
            "name": t.string().optional(),
            "supportedVersionIds": t.array(t.string()).optional(),
            "screenY": t.integer().optional(),
            "screenX": t.integer().optional(),
            "formFactor": t.string().optional(),
            "deviceCapabilities": t.array(t.string()).optional(),
            "screenDensity": t.integer().optional(),
            "perVersionInfo": t.array(
                t.proxy(renames["PerIosVersionInfoIn"])
            ).optional(),
            "id": t.string().optional(),
            "tags": t.array(t.string()).optional(),
        }
    ).named(renames["IosModelIn"])
    types["IosModelOut"] = t.struct(
        {
            "name": t.string().optional(),
            "supportedVersionIds": t.array(t.string()).optional(),
            "screenY": t.integer().optional(),
            "screenX": t.integer().optional(),
            "formFactor": t.string().optional(),
            "deviceCapabilities": t.array(t.string()).optional(),
            "screenDensity": t.integer().optional(),
            "perVersionInfo": t.array(
                t.proxy(renames["PerIosVersionInfoOut"])
            ).optional(),
            "id": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosModelOut"])
    types["GoogleAutoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleAutoIn"]
    )
    types["GoogleAutoOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAutoOut"])
    types["IosRuntimeConfigurationIn"] = t.struct(
        {
            "orientations": t.array(t.proxy(renames["OrientationIn"])).optional(),
            "locales": t.array(t.proxy(renames["LocaleIn"])).optional(),
        }
    ).named(renames["IosRuntimeConfigurationIn"])
    types["IosRuntimeConfigurationOut"] = t.struct(
        {
            "orientations": t.array(t.proxy(renames["OrientationOut"])).optional(),
            "locales": t.array(t.proxy(renames["LocaleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosRuntimeConfigurationOut"])
    types["IosDeviceIn"] = t.struct(
        {
            "locale": t.string(),
            "orientation": t.string(),
            "iosVersionId": t.string(),
            "iosModelId": t.string(),
        }
    ).named(renames["IosDeviceIn"])
    types["IosDeviceOut"] = t.struct(
        {
            "locale": t.string(),
            "orientation": t.string(),
            "iosVersionId": t.string(),
            "iosModelId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosDeviceOut"])
    types["XcodeVersionIn"] = t.struct(
        {"tags": t.array(t.string()).optional(), "version": t.string().optional()}
    ).named(renames["XcodeVersionIn"])
    types["XcodeVersionOut"] = t.struct(
        {
            "tags": t.array(t.string()).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["XcodeVersionOut"])
    types["TestEnvironmentCatalogIn"] = t.struct(
        {
            "iosDeviceCatalog": t.proxy(renames["IosDeviceCatalogIn"]).optional(),
            "androidDeviceCatalog": t.proxy(
                renames["AndroidDeviceCatalogIn"]
            ).optional(),
            "softwareCatalog": t.proxy(renames["ProvidedSoftwareCatalogIn"]).optional(),
            "networkConfigurationCatalog": t.proxy(
                renames["NetworkConfigurationCatalogIn"]
            ).optional(),
            "deviceIpBlockCatalog": t.proxy(
                renames["DeviceIpBlockCatalogIn"]
            ).optional(),
        }
    ).named(renames["TestEnvironmentCatalogIn"])
    types["TestEnvironmentCatalogOut"] = t.struct(
        {
            "iosDeviceCatalog": t.proxy(renames["IosDeviceCatalogOut"]).optional(),
            "androidDeviceCatalog": t.proxy(
                renames["AndroidDeviceCatalogOut"]
            ).optional(),
            "softwareCatalog": t.proxy(
                renames["ProvidedSoftwareCatalogOut"]
            ).optional(),
            "networkConfigurationCatalog": t.proxy(
                renames["NetworkConfigurationCatalogOut"]
            ).optional(),
            "deviceIpBlockCatalog": t.proxy(
                renames["DeviceIpBlockCatalogOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestEnvironmentCatalogOut"])
    types["NetworkConfigurationCatalogIn"] = t.struct(
        {"configurations": t.array(t.proxy(renames["NetworkConfigurationIn"]))}
    ).named(renames["NetworkConfigurationCatalogIn"])
    types["NetworkConfigurationCatalogOut"] = t.struct(
        {
            "configurations": t.array(t.proxy(renames["NetworkConfigurationOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConfigurationCatalogOut"])
    types["LauncherActivityIntentIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LauncherActivityIntentIn"]
    )
    types["LauncherActivityIntentOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LauncherActivityIntentOut"])
    types["ObbFileIn"] = t.struct(
        {"obb": t.proxy(renames["FileReferenceIn"]), "obbFileName": t.string()}
    ).named(renames["ObbFileIn"])
    types["ObbFileOut"] = t.struct(
        {
            "obb": t.proxy(renames["FileReferenceOut"]),
            "obbFileName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObbFileOut"])
    types["AndroidTestLoopIn"] = t.struct(
        {
            "appApk": t.proxy(renames["FileReferenceIn"]).optional(),
            "appBundle": t.proxy(renames["AppBundleIn"]).optional(),
            "appPackageId": t.string().optional(),
            "scenarios": t.array(t.integer()).optional(),
            "scenarioLabels": t.array(t.string()).optional(),
        }
    ).named(renames["AndroidTestLoopIn"])
    types["AndroidTestLoopOut"] = t.struct(
        {
            "appApk": t.proxy(renames["FileReferenceOut"]).optional(),
            "appBundle": t.proxy(renames["AppBundleOut"]).optional(),
            "appPackageId": t.string().optional(),
            "scenarios": t.array(t.integer()).optional(),
            "scenarioLabels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidTestLoopOut"])
    types["ApkIn"] = t.struct(
        {
            "packageName": t.string().optional(),
            "location": t.proxy(renames["FileReferenceIn"]).optional(),
        }
    ).named(renames["ApkIn"])
    types["ApkOut"] = t.struct(
        {
            "packageName": t.string().optional(),
            "location": t.proxy(renames["FileReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApkOut"])
    types["SystraceSetupIn"] = t.struct(
        {"durationSeconds": t.integer().optional()}
    ).named(renames["SystraceSetupIn"])
    types["SystraceSetupOut"] = t.struct(
        {
            "durationSeconds": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystraceSetupOut"])
    types["UniformShardingIn"] = t.struct({"numShards": t.integer()}).named(
        renames["UniformShardingIn"]
    )
    types["UniformShardingOut"] = t.struct(
        {
            "numShards": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UniformShardingOut"])
    types["CancelTestMatrixResponseIn"] = t.struct(
        {"testState": t.string().optional()}
    ).named(renames["CancelTestMatrixResponseIn"])
    types["CancelTestMatrixResponseOut"] = t.struct(
        {
            "testState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CancelTestMatrixResponseOut"])
    types["AndroidInstrumentationTestIn"] = t.struct(
        {
            "testPackageId": t.string().optional(),
            "testRunnerClass": t.string().optional(),
            "testApk": t.proxy(renames["FileReferenceIn"]),
            "orchestratorOption": t.string().optional(),
            "appBundle": t.proxy(renames["AppBundleIn"]).optional(),
            "testTargets": t.array(t.string()).optional(),
            "appApk": t.proxy(renames["FileReferenceIn"]).optional(),
            "shardingOption": t.proxy(renames["ShardingOptionIn"]).optional(),
            "appPackageId": t.string().optional(),
        }
    ).named(renames["AndroidInstrumentationTestIn"])
    types["AndroidInstrumentationTestOut"] = t.struct(
        {
            "testPackageId": t.string().optional(),
            "testRunnerClass": t.string().optional(),
            "testApk": t.proxy(renames["FileReferenceOut"]),
            "orchestratorOption": t.string().optional(),
            "appBundle": t.proxy(renames["AppBundleOut"]).optional(),
            "testTargets": t.array(t.string()).optional(),
            "appApk": t.proxy(renames["FileReferenceOut"]).optional(),
            "shardingOption": t.proxy(renames["ShardingOptionOut"]).optional(),
            "appPackageId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidInstrumentationTestOut"])
    types["EnvironmentIn"] = t.struct(
        {
            "androidDevice": t.proxy(renames["AndroidDeviceIn"]).optional(),
            "iosDevice": t.proxy(renames["IosDeviceIn"]).optional(),
        }
    ).named(renames["EnvironmentIn"])
    types["EnvironmentOut"] = t.struct(
        {
            "androidDevice": t.proxy(renames["AndroidDeviceOut"]).optional(),
            "iosDevice": t.proxy(renames["IosDeviceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentOut"])
    types["AndroidDeviceCatalogIn"] = t.struct(
        {
            "models": t.array(t.proxy(renames["AndroidModelIn"])).optional(),
            "runtimeConfiguration": t.proxy(
                renames["AndroidRuntimeConfigurationIn"]
            ).optional(),
            "versions": t.array(t.proxy(renames["AndroidVersionIn"])).optional(),
        }
    ).named(renames["AndroidDeviceCatalogIn"])
    types["AndroidDeviceCatalogOut"] = t.struct(
        {
            "models": t.array(t.proxy(renames["AndroidModelOut"])).optional(),
            "runtimeConfiguration": t.proxy(
                renames["AndroidRuntimeConfigurationOut"]
            ).optional(),
            "versions": t.array(t.proxy(renames["AndroidVersionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidDeviceCatalogOut"])
    types["AndroidRuntimeConfigurationIn"] = t.struct(
        {
            "orientations": t.array(t.proxy(renames["OrientationIn"])).optional(),
            "locales": t.array(t.proxy(renames["LocaleIn"])).optional(),
        }
    ).named(renames["AndroidRuntimeConfigurationIn"])
    types["AndroidRuntimeConfigurationOut"] = t.struct(
        {
            "orientations": t.array(t.proxy(renames["OrientationOut"])).optional(),
            "locales": t.array(t.proxy(renames["LocaleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidRuntimeConfigurationOut"])
    types["TestSetupIn"] = t.struct(
        {
            "filesToPush": t.array(t.proxy(renames["DeviceFileIn"])).optional(),
            "additionalApks": t.array(t.proxy(renames["ApkIn"])).optional(),
            "networkProfile": t.string().optional(),
            "dontAutograntPermissions": t.boolean().optional(),
            "account": t.proxy(renames["AccountIn"]).optional(),
            "environmentVariables": t.array(
                t.proxy(renames["EnvironmentVariableIn"])
            ).optional(),
            "systrace": t.proxy(renames["SystraceSetupIn"]).optional(),
            "directoriesToPull": t.array(t.string()).optional(),
        }
    ).named(renames["TestSetupIn"])
    types["TestSetupOut"] = t.struct(
        {
            "filesToPush": t.array(t.proxy(renames["DeviceFileOut"])).optional(),
            "additionalApks": t.array(t.proxy(renames["ApkOut"])).optional(),
            "networkProfile": t.string().optional(),
            "dontAutograntPermissions": t.boolean().optional(),
            "account": t.proxy(renames["AccountOut"]).optional(),
            "environmentVariables": t.array(
                t.proxy(renames["EnvironmentVariableOut"])
            ).optional(),
            "systrace": t.proxy(renames["SystraceSetupOut"]).optional(),
            "directoriesToPull": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestSetupOut"])
    types["ApkManifestIn"] = t.struct(
        {
            "services": t.array(t.proxy(renames["ServiceIn"])).optional(),
            "applicationLabel": t.string().optional(),
            "usesPermission": t.array(t.string()).optional(),
            "targetSdkVersion": t.integer().optional(),
            "maxSdkVersion": t.integer().optional(),
            "packageName": t.string().optional(),
            "metadata": t.array(t.proxy(renames["MetadataIn"])).optional(),
            "intentFilters": t.array(t.proxy(renames["IntentFilterIn"])),
            "versionCode": t.string().optional(),
            "minSdkVersion": t.integer().optional(),
            "usesFeature": t.array(t.proxy(renames["UsesFeatureIn"])).optional(),
            "versionName": t.string().optional(),
        }
    ).named(renames["ApkManifestIn"])
    types["ApkManifestOut"] = t.struct(
        {
            "services": t.array(t.proxy(renames["ServiceOut"])).optional(),
            "applicationLabel": t.string().optional(),
            "usesPermission": t.array(t.string()).optional(),
            "targetSdkVersion": t.integer().optional(),
            "maxSdkVersion": t.integer().optional(),
            "packageName": t.string().optional(),
            "metadata": t.array(t.proxy(renames["MetadataOut"])).optional(),
            "intentFilters": t.array(t.proxy(renames["IntentFilterOut"])),
            "versionCode": t.string().optional(),
            "minSdkVersion": t.integer().optional(),
            "usesFeature": t.array(t.proxy(renames["UsesFeatureOut"])).optional(),
            "versionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApkManifestOut"])
    types["TestDetailsIn"] = t.struct(
        {
            "progressMessages": t.array(t.string()).optional(),
            "errorMessage": t.string().optional(),
        }
    ).named(renames["TestDetailsIn"])
    types["TestDetailsOut"] = t.struct(
        {
            "progressMessages": t.array(t.string()).optional(),
            "errorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestDetailsOut"])
    types["AndroidDeviceListIn"] = t.struct(
        {"androidDevices": t.array(t.proxy(renames["AndroidDeviceIn"]))}
    ).named(renames["AndroidDeviceListIn"])
    types["AndroidDeviceListOut"] = t.struct(
        {
            "androidDevices": t.array(t.proxy(renames["AndroidDeviceOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidDeviceListOut"])
    types["AndroidModelIn"] = t.struct(
        {
            "lowFpsVideoRecording": t.boolean().optional(),
            "thumbnailUrl": t.string().optional(),
            "form": t.string().optional(),
            "perVersionInfo": t.array(
                t.proxy(renames["PerAndroidVersionInfoIn"])
            ).optional(),
            "manufacturer": t.string().optional(),
            "formFactor": t.string().optional(),
            "brand": t.string().optional(),
            "codename": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "supportedAbis": t.array(t.string()).optional(),
            "screenY": t.integer().optional(),
            "supportedVersionIds": t.array(t.string()).optional(),
            "screenX": t.integer().optional(),
            "screenDensity": t.integer().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["AndroidModelIn"])
    types["AndroidModelOut"] = t.struct(
        {
            "lowFpsVideoRecording": t.boolean().optional(),
            "thumbnailUrl": t.string().optional(),
            "form": t.string().optional(),
            "perVersionInfo": t.array(
                t.proxy(renames["PerAndroidVersionInfoOut"])
            ).optional(),
            "manufacturer": t.string().optional(),
            "formFactor": t.string().optional(),
            "brand": t.string().optional(),
            "codename": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "supportedAbis": t.array(t.string()).optional(),
            "screenY": t.integer().optional(),
            "supportedVersionIds": t.array(t.string()).optional(),
            "screenX": t.integer().optional(),
            "screenDensity": t.integer().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidModelOut"])
    types["FileReferenceIn"] = t.struct({"gcsPath": t.string().optional()}).named(
        renames["FileReferenceIn"]
    )
    types["FileReferenceOut"] = t.struct(
        {
            "gcsPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileReferenceOut"])
    types["AndroidRoboTestIn"] = t.struct(
        {
            "roboScript": t.proxy(renames["FileReferenceIn"]).optional(),
            "maxDepth": t.integer().optional(),
            "appPackageId": t.string().optional(),
            "roboMode": t.string().optional(),
            "appInitialActivity": t.string().optional(),
            "appApk": t.proxy(renames["FileReferenceIn"]).optional(),
            "roboDirectives": t.array(t.proxy(renames["RoboDirectiveIn"])).optional(),
            "startingIntents": t.array(
                t.proxy(renames["RoboStartingIntentIn"])
            ).optional(),
            "appBundle": t.proxy(renames["AppBundleIn"]).optional(),
            "maxSteps": t.integer().optional(),
        }
    ).named(renames["AndroidRoboTestIn"])
    types["AndroidRoboTestOut"] = t.struct(
        {
            "roboScript": t.proxy(renames["FileReferenceOut"]).optional(),
            "maxDepth": t.integer().optional(),
            "appPackageId": t.string().optional(),
            "roboMode": t.string().optional(),
            "appInitialActivity": t.string().optional(),
            "appApk": t.proxy(renames["FileReferenceOut"]).optional(),
            "roboDirectives": t.array(t.proxy(renames["RoboDirectiveOut"])).optional(),
            "startingIntents": t.array(
                t.proxy(renames["RoboStartingIntentOut"])
            ).optional(),
            "appBundle": t.proxy(renames["AppBundleOut"]).optional(),
            "maxSteps": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidRoboTestOut"])
    types["SmartShardingIn"] = t.struct(
        {"targetedShardDuration": t.string().optional()}
    ).named(renames["SmartShardingIn"])
    types["SmartShardingOut"] = t.struct(
        {
            "targetedShardDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SmartShardingOut"])
    types["AndroidVersionIn"] = t.struct(
        {
            "codeName": t.string().optional(),
            "id": t.string().optional(),
            "distribution": t.proxy(renames["DistributionIn"]).optional(),
            "versionString": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "releaseDate": t.proxy(renames["DateIn"]).optional(),
            "apiLevel": t.integer().optional(),
        }
    ).named(renames["AndroidVersionIn"])
    types["AndroidVersionOut"] = t.struct(
        {
            "codeName": t.string().optional(),
            "id": t.string().optional(),
            "distribution": t.proxy(renames["DistributionOut"]).optional(),
            "versionString": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "releaseDate": t.proxy(renames["DateOut"]).optional(),
            "apiLevel": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidVersionOut"])
    types["ShardIn"] = t.struct({"_": t.string().optional()}).named(renames["ShardIn"])
    types["ShardOut"] = t.struct(
        {
            "testTargetsForShard": t.proxy(
                renames["TestTargetsForShardOut"]
            ).optional(),
            "shardIndex": t.integer().optional(),
            "estimatedShardDuration": t.string().optional(),
            "numShards": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShardOut"])
    types["DistributionIn"] = t.struct(
        {"measurementTime": t.string().optional(), "marketShare": t.number().optional()}
    ).named(renames["DistributionIn"])
    types["DistributionOut"] = t.struct(
        {
            "measurementTime": t.string().optional(),
            "marketShare": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DistributionOut"])
    types["NoActivityIntentIn"] = t.struct({"_": t.string().optional()}).named(
        renames["NoActivityIntentIn"]
    )
    types["NoActivityIntentOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["NoActivityIntentOut"])
    types["RoboDirectiveIn"] = t.struct(
        {
            "inputText": t.string().optional(),
            "resourceName": t.string(),
            "actionType": t.string(),
        }
    ).named(renames["RoboDirectiveIn"])
    types["RoboDirectiveOut"] = t.struct(
        {
            "inputText": t.string().optional(),
            "resourceName": t.string(),
            "actionType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RoboDirectiveOut"])
    types["PerIosVersionInfoIn"] = t.struct(
        {"deviceCapacity": t.string().optional(), "versionId": t.string().optional()}
    ).named(renames["PerIosVersionInfoIn"])
    types["PerIosVersionInfoOut"] = t.struct(
        {
            "deviceCapacity": t.string().optional(),
            "versionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerIosVersionInfoOut"])
    types["OrientationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "id": t.string().optional(),
            "tags": t.array(t.string()).optional(),
        }
    ).named(renames["OrientationIn"])
    types["OrientationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "id": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrientationOut"])
    types["LocaleIn"] = t.struct(
        {
            "region": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "tags": t.array(t.string()).optional(),
        }
    ).named(renames["LocaleIn"])
    types["LocaleOut"] = t.struct(
        {
            "region": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocaleOut"])
    types["GetApkDetailsResponseIn"] = t.struct(
        {"apkDetail": t.proxy(renames["ApkDetailIn"]).optional()}
    ).named(renames["GetApkDetailsResponseIn"])
    types["GetApkDetailsResponseOut"] = t.struct(
        {
            "apkDetail": t.proxy(renames["ApkDetailOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetApkDetailsResponseOut"])
    types["AndroidMatrixIn"] = t.struct(
        {
            "androidVersionIds": t.array(t.string()),
            "locales": t.array(t.string()),
            "androidModelIds": t.array(t.string()),
            "orientations": t.array(t.string()),
        }
    ).named(renames["AndroidMatrixIn"])
    types["AndroidMatrixOut"] = t.struct(
        {
            "androidVersionIds": t.array(t.string()),
            "locales": t.array(t.string()),
            "androidModelIds": t.array(t.string()),
            "orientations": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidMatrixOut"])
    types["IosDeviceFileIn"] = t.struct(
        {
            "bundleId": t.string().optional(),
            "content": t.proxy(renames["FileReferenceIn"]).optional(),
            "devicePath": t.string().optional(),
        }
    ).named(renames["IosDeviceFileIn"])
    types["IosDeviceFileOut"] = t.struct(
        {
            "bundleId": t.string().optional(),
            "content": t.proxy(renames["FileReferenceOut"]).optional(),
            "devicePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosDeviceFileOut"])
    types["TestTargetsForShardIn"] = t.struct(
        {"testTargets": t.array(t.string()).optional()}
    ).named(renames["TestTargetsForShardIn"])
    types["TestTargetsForShardOut"] = t.struct(
        {
            "testTargets": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestTargetsForShardOut"])
    types["TestSpecificationIn"] = t.struct(
        {
            "disableVideoRecording": t.boolean().optional(),
            "iosXcTest": t.proxy(renames["IosXcTestIn"]).optional(),
            "androidTestLoop": t.proxy(renames["AndroidTestLoopIn"]).optional(),
            "androidRoboTest": t.proxy(renames["AndroidRoboTestIn"]).optional(),
            "testTimeout": t.string().optional(),
            "iosTestLoop": t.proxy(renames["IosTestLoopIn"]).optional(),
            "testSetup": t.proxy(renames["TestSetupIn"]).optional(),
            "iosTestSetup": t.proxy(renames["IosTestSetupIn"]).optional(),
            "disablePerformanceMetrics": t.boolean().optional(),
            "androidInstrumentationTest": t.proxy(
                renames["AndroidInstrumentationTestIn"]
            ).optional(),
        }
    ).named(renames["TestSpecificationIn"])
    types["TestSpecificationOut"] = t.struct(
        {
            "disableVideoRecording": t.boolean().optional(),
            "iosXcTest": t.proxy(renames["IosXcTestOut"]).optional(),
            "androidTestLoop": t.proxy(renames["AndroidTestLoopOut"]).optional(),
            "androidRoboTest": t.proxy(renames["AndroidRoboTestOut"]).optional(),
            "testTimeout": t.string().optional(),
            "iosTestLoop": t.proxy(renames["IosTestLoopOut"]).optional(),
            "testSetup": t.proxy(renames["TestSetupOut"]).optional(),
            "iosTestSetup": t.proxy(renames["IosTestSetupOut"]).optional(),
            "disablePerformanceMetrics": t.boolean().optional(),
            "androidInstrumentationTest": t.proxy(
                renames["AndroidInstrumentationTestOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestSpecificationOut"])
    types["PerAndroidVersionInfoIn"] = t.struct(
        {"deviceCapacity": t.string().optional(), "versionId": t.string().optional()}
    ).named(renames["PerAndroidVersionInfoIn"])
    types["PerAndroidVersionInfoOut"] = t.struct(
        {
            "deviceCapacity": t.string().optional(),
            "versionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerAndroidVersionInfoOut"])
    types["ClientInfoIn"] = t.struct(
        {
            "name": t.string(),
            "clientInfoDetails": t.array(
                t.proxy(renames["ClientInfoDetailIn"])
            ).optional(),
        }
    ).named(renames["ClientInfoIn"])
    types["ClientInfoOut"] = t.struct(
        {
            "name": t.string(),
            "clientInfoDetails": t.array(
                t.proxy(renames["ClientInfoDetailOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientInfoOut"])
    types["IosVersionIn"] = t.struct(
        {
            "minorVersion": t.integer().optional(),
            "majorVersion": t.integer().optional(),
            "tags": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "supportedXcodeVersionIds": t.array(t.string()).optional(),
        }
    ).named(renames["IosVersionIn"])
    types["IosVersionOut"] = t.struct(
        {
            "minorVersion": t.integer().optional(),
            "majorVersion": t.integer().optional(),
            "tags": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "supportedXcodeVersionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosVersionOut"])
    types["IosDeviceListIn"] = t.struct(
        {"iosDevices": t.array(t.proxy(renames["IosDeviceIn"]))}
    ).named(renames["IosDeviceListIn"])
    types["IosDeviceListOut"] = t.struct(
        {
            "iosDevices": t.array(t.proxy(renames["IosDeviceOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosDeviceListOut"])
    types["ClientInfoDetailIn"] = t.struct(
        {"key": t.string(), "value": t.string()}
    ).named(renames["ClientInfoDetailIn"])
    types["ClientInfoDetailOut"] = t.struct(
        {
            "key": t.string(),
            "value": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientInfoDetailOut"])
    types["ResultStorageIn"] = t.struct(
        {
            "resultsUrl": t.string().optional(),
            "googleCloudStorage": t.proxy(renames["GoogleCloudStorageIn"]),
            "toolResultsHistory": t.proxy(renames["ToolResultsHistoryIn"]).optional(),
            "toolResultsExecution": t.proxy(
                renames["ToolResultsExecutionIn"]
            ).optional(),
        }
    ).named(renames["ResultStorageIn"])
    types["ResultStorageOut"] = t.struct(
        {
            "resultsUrl": t.string().optional(),
            "googleCloudStorage": t.proxy(renames["GoogleCloudStorageOut"]),
            "toolResultsHistory": t.proxy(renames["ToolResultsHistoryOut"]).optional(),
            "toolResultsExecution": t.proxy(
                renames["ToolResultsExecutionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultStorageOut"])
    types["IosTestSetupIn"] = t.struct(
        {
            "pushFiles": t.array(t.proxy(renames["IosDeviceFileIn"])).optional(),
            "pullDirectories": t.array(t.proxy(renames["IosDeviceFileIn"])).optional(),
            "networkProfile": t.string().optional(),
            "additionalIpas": t.array(t.proxy(renames["FileReferenceIn"])).optional(),
        }
    ).named(renames["IosTestSetupIn"])
    types["IosTestSetupOut"] = t.struct(
        {
            "pushFiles": t.array(t.proxy(renames["IosDeviceFileOut"])).optional(),
            "pullDirectories": t.array(t.proxy(renames["IosDeviceFileOut"])).optional(),
            "networkProfile": t.string().optional(),
            "additionalIpas": t.array(t.proxy(renames["FileReferenceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosTestSetupOut"])
    types["ApkDetailIn"] = t.struct(
        {"apkManifest": t.proxy(renames["ApkManifestIn"])}
    ).named(renames["ApkDetailIn"])
    types["ApkDetailOut"] = t.struct(
        {
            "apkManifest": t.proxy(renames["ApkManifestOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApkDetailOut"])
    types["AccountIn"] = t.struct(
        {"googleAuto": t.proxy(renames["GoogleAutoIn"]).optional()}
    ).named(renames["AccountIn"])
    types["AccountOut"] = t.struct(
        {
            "googleAuto": t.proxy(renames["GoogleAutoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountOut"])
    types["GoogleCloudStorageIn"] = t.struct({"gcsPath": t.string()}).named(
        renames["GoogleCloudStorageIn"]
    )
    types["GoogleCloudStorageOut"] = t.struct(
        {"gcsPath": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudStorageOut"])
    types["NetworkConfigurationIn"] = t.struct(
        {
            "upRule": t.proxy(renames["TrafficRuleIn"]).optional(),
            "downRule": t.proxy(renames["TrafficRuleIn"]).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["NetworkConfigurationIn"])
    types["NetworkConfigurationOut"] = t.struct(
        {
            "upRule": t.proxy(renames["TrafficRuleOut"]).optional(),
            "downRule": t.proxy(renames["TrafficRuleOut"]).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConfigurationOut"])
    types["RegularFileIn"] = t.struct(
        {"content": t.proxy(renames["FileReferenceIn"]), "devicePath": t.string()}
    ).named(renames["RegularFileIn"])
    types["RegularFileOut"] = t.struct(
        {
            "content": t.proxy(renames["FileReferenceOut"]),
            "devicePath": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegularFileOut"])

    functions = {}
    functions["applicationDetailServiceGetApkDetails"] = testing.post(
        "v1/applicationDetailService/getApkDetails",
        t.struct({"gcsPath": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GetApkDetailsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTestMatricesCreate"] = testing.post(
        "v1/projects/{projectId}/testMatrices/{testMatrixId}:cancel",
        t.struct(
            {
                "testMatrixId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CancelTestMatrixResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTestMatricesGet"] = testing.post(
        "v1/projects/{projectId}/testMatrices/{testMatrixId}:cancel",
        t.struct(
            {
                "testMatrixId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CancelTestMatrixResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTestMatricesCancel"] = testing.post(
        "v1/projects/{projectId}/testMatrices/{testMatrixId}:cancel",
        t.struct(
            {
                "testMatrixId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CancelTestMatrixResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["testEnvironmentCatalogGet"] = testing.get(
        "v1/testEnvironmentCatalog/{environmentType}",
        t.struct(
            {
                "environmentType": t.string(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestEnvironmentCatalogOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="testing", renames=renames, types=Box(types), functions=Box(functions)
    )
