from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_testing() -> Import:
    testing = HTTPRuntime("https://testing.googleapis.com/")

    renames = {
        "ErrorResponse": "_testing_1_ErrorResponse",
        "ShardingOptionIn": "_testing_2_ShardingOptionIn",
        "ShardingOptionOut": "_testing_3_ShardingOptionOut",
        "TestExecutionIn": "_testing_4_TestExecutionIn",
        "TestExecutionOut": "_testing_5_TestExecutionOut",
        "AndroidDeviceListIn": "_testing_6_AndroidDeviceListIn",
        "AndroidDeviceListOut": "_testing_7_AndroidDeviceListOut",
        "LocaleIn": "_testing_8_LocaleIn",
        "LocaleOut": "_testing_9_LocaleOut",
        "AndroidTestLoopIn": "_testing_10_AndroidTestLoopIn",
        "AndroidTestLoopOut": "_testing_11_AndroidTestLoopOut",
        "AppBundleIn": "_testing_12_AppBundleIn",
        "AppBundleOut": "_testing_13_AppBundleOut",
        "FileReferenceIn": "_testing_14_FileReferenceIn",
        "FileReferenceOut": "_testing_15_FileReferenceOut",
        "NetworkConfigurationCatalogIn": "_testing_16_NetworkConfigurationCatalogIn",
        "NetworkConfigurationCatalogOut": "_testing_17_NetworkConfigurationCatalogOut",
        "PerAndroidVersionInfoIn": "_testing_18_PerAndroidVersionInfoIn",
        "PerAndroidVersionInfoOut": "_testing_19_PerAndroidVersionInfoOut",
        "IosDeviceFileIn": "_testing_20_IosDeviceFileIn",
        "IosDeviceFileOut": "_testing_21_IosDeviceFileOut",
        "SmartShardingIn": "_testing_22_SmartShardingIn",
        "SmartShardingOut": "_testing_23_SmartShardingOut",
        "OrientationIn": "_testing_24_OrientationIn",
        "OrientationOut": "_testing_25_OrientationOut",
        "ShardIn": "_testing_26_ShardIn",
        "ShardOut": "_testing_27_ShardOut",
        "AndroidInstrumentationTestIn": "_testing_28_AndroidInstrumentationTestIn",
        "AndroidInstrumentationTestOut": "_testing_29_AndroidInstrumentationTestOut",
        "ApkDetailIn": "_testing_30_ApkDetailIn",
        "ApkDetailOut": "_testing_31_ApkDetailOut",
        "ProvidedSoftwareCatalogIn": "_testing_32_ProvidedSoftwareCatalogIn",
        "ProvidedSoftwareCatalogOut": "_testing_33_ProvidedSoftwareCatalogOut",
        "SystraceSetupIn": "_testing_34_SystraceSetupIn",
        "SystraceSetupOut": "_testing_35_SystraceSetupOut",
        "ResultStorageIn": "_testing_36_ResultStorageIn",
        "ResultStorageOut": "_testing_37_ResultStorageOut",
        "TestEnvironmentCatalogIn": "_testing_38_TestEnvironmentCatalogIn",
        "TestEnvironmentCatalogOut": "_testing_39_TestEnvironmentCatalogOut",
        "IosDeviceListIn": "_testing_40_IosDeviceListIn",
        "IosDeviceListOut": "_testing_41_IosDeviceListOut",
        "TestSpecificationIn": "_testing_42_TestSpecificationIn",
        "TestSpecificationOut": "_testing_43_TestSpecificationOut",
        "AndroidVersionIn": "_testing_44_AndroidVersionIn",
        "AndroidVersionOut": "_testing_45_AndroidVersionOut",
        "IosRuntimeConfigurationIn": "_testing_46_IosRuntimeConfigurationIn",
        "IosRuntimeConfigurationOut": "_testing_47_IosRuntimeConfigurationOut",
        "ClientInfoDetailIn": "_testing_48_ClientInfoDetailIn",
        "ClientInfoDetailOut": "_testing_49_ClientInfoDetailOut",
        "ClientInfoIn": "_testing_50_ClientInfoIn",
        "ClientInfoOut": "_testing_51_ClientInfoOut",
        "CancelTestMatrixResponseIn": "_testing_52_CancelTestMatrixResponseIn",
        "CancelTestMatrixResponseOut": "_testing_53_CancelTestMatrixResponseOut",
        "EnvironmentVariableIn": "_testing_54_EnvironmentVariableIn",
        "EnvironmentVariableOut": "_testing_55_EnvironmentVariableOut",
        "TrafficRuleIn": "_testing_56_TrafficRuleIn",
        "TrafficRuleOut": "_testing_57_TrafficRuleOut",
        "EnvironmentIn": "_testing_58_EnvironmentIn",
        "EnvironmentOut": "_testing_59_EnvironmentOut",
        "AccountIn": "_testing_60_AccountIn",
        "AccountOut": "_testing_61_AccountOut",
        "IosTestSetupIn": "_testing_62_IosTestSetupIn",
        "IosTestSetupOut": "_testing_63_IosTestSetupOut",
        "TestDetailsIn": "_testing_64_TestDetailsIn",
        "TestDetailsOut": "_testing_65_TestDetailsOut",
        "LauncherActivityIntentIn": "_testing_66_LauncherActivityIntentIn",
        "LauncherActivityIntentOut": "_testing_67_LauncherActivityIntentOut",
        "IosModelIn": "_testing_68_IosModelIn",
        "IosModelOut": "_testing_69_IosModelOut",
        "DistributionIn": "_testing_70_DistributionIn",
        "DistributionOut": "_testing_71_DistributionOut",
        "AndroidMatrixIn": "_testing_72_AndroidMatrixIn",
        "AndroidMatrixOut": "_testing_73_AndroidMatrixOut",
        "PerIosVersionInfoIn": "_testing_74_PerIosVersionInfoIn",
        "PerIosVersionInfoOut": "_testing_75_PerIosVersionInfoOut",
        "EnvironmentMatrixIn": "_testing_76_EnvironmentMatrixIn",
        "EnvironmentMatrixOut": "_testing_77_EnvironmentMatrixOut",
        "DateIn": "_testing_78_DateIn",
        "DateOut": "_testing_79_DateOut",
        "RegularFileIn": "_testing_80_RegularFileIn",
        "RegularFileOut": "_testing_81_RegularFileOut",
        "StartActivityIntentIn": "_testing_82_StartActivityIntentIn",
        "StartActivityIntentOut": "_testing_83_StartActivityIntentOut",
        "IosDeviceIn": "_testing_84_IosDeviceIn",
        "IosDeviceOut": "_testing_85_IosDeviceOut",
        "AndroidDeviceIn": "_testing_86_AndroidDeviceIn",
        "AndroidDeviceOut": "_testing_87_AndroidDeviceOut",
        "ToolResultsStepIn": "_testing_88_ToolResultsStepIn",
        "ToolResultsStepOut": "_testing_89_ToolResultsStepOut",
        "GoogleCloudStorageIn": "_testing_90_GoogleCloudStorageIn",
        "GoogleCloudStorageOut": "_testing_91_GoogleCloudStorageOut",
        "DeviceFileIn": "_testing_92_DeviceFileIn",
        "DeviceFileOut": "_testing_93_DeviceFileOut",
        "ObbFileIn": "_testing_94_ObbFileIn",
        "ObbFileOut": "_testing_95_ObbFileOut",
        "AndroidModelIn": "_testing_96_AndroidModelIn",
        "AndroidModelOut": "_testing_97_AndroidModelOut",
        "IosXcTestIn": "_testing_98_IosXcTestIn",
        "IosXcTestOut": "_testing_99_IosXcTestOut",
        "RoboStartingIntentIn": "_testing_100_RoboStartingIntentIn",
        "RoboStartingIntentOut": "_testing_101_RoboStartingIntentOut",
        "DeviceIpBlockIn": "_testing_102_DeviceIpBlockIn",
        "DeviceIpBlockOut": "_testing_103_DeviceIpBlockOut",
        "GetApkDetailsResponseIn": "_testing_104_GetApkDetailsResponseIn",
        "GetApkDetailsResponseOut": "_testing_105_GetApkDetailsResponseOut",
        "ApkIn": "_testing_106_ApkIn",
        "ApkOut": "_testing_107_ApkOut",
        "ApkManifestIn": "_testing_108_ApkManifestIn",
        "ApkManifestOut": "_testing_109_ApkManifestOut",
        "TestTargetsForShardIn": "_testing_110_TestTargetsForShardIn",
        "TestTargetsForShardOut": "_testing_111_TestTargetsForShardOut",
        "DeviceIpBlockCatalogIn": "_testing_112_DeviceIpBlockCatalogIn",
        "DeviceIpBlockCatalogOut": "_testing_113_DeviceIpBlockCatalogOut",
        "TestSetupIn": "_testing_114_TestSetupIn",
        "TestSetupOut": "_testing_115_TestSetupOut",
        "UniformShardingIn": "_testing_116_UniformShardingIn",
        "UniformShardingOut": "_testing_117_UniformShardingOut",
        "ManualShardingIn": "_testing_118_ManualShardingIn",
        "ManualShardingOut": "_testing_119_ManualShardingOut",
        "TestMatrixIn": "_testing_120_TestMatrixIn",
        "TestMatrixOut": "_testing_121_TestMatrixOut",
        "RoboDirectiveIn": "_testing_122_RoboDirectiveIn",
        "RoboDirectiveOut": "_testing_123_RoboDirectiveOut",
        "AndroidRuntimeConfigurationIn": "_testing_124_AndroidRuntimeConfigurationIn",
        "AndroidRuntimeConfigurationOut": "_testing_125_AndroidRuntimeConfigurationOut",
        "IosTestLoopIn": "_testing_126_IosTestLoopIn",
        "IosTestLoopOut": "_testing_127_IosTestLoopOut",
        "GoogleAutoIn": "_testing_128_GoogleAutoIn",
        "GoogleAutoOut": "_testing_129_GoogleAutoOut",
        "ToolResultsExecutionIn": "_testing_130_ToolResultsExecutionIn",
        "ToolResultsExecutionOut": "_testing_131_ToolResultsExecutionOut",
        "AndroidDeviceCatalogIn": "_testing_132_AndroidDeviceCatalogIn",
        "AndroidDeviceCatalogOut": "_testing_133_AndroidDeviceCatalogOut",
        "NetworkConfigurationIn": "_testing_134_NetworkConfigurationIn",
        "NetworkConfigurationOut": "_testing_135_NetworkConfigurationOut",
        "IosDeviceCatalogIn": "_testing_136_IosDeviceCatalogIn",
        "IosDeviceCatalogOut": "_testing_137_IosDeviceCatalogOut",
        "MetadataIn": "_testing_138_MetadataIn",
        "MetadataOut": "_testing_139_MetadataOut",
        "XcodeVersionIn": "_testing_140_XcodeVersionIn",
        "XcodeVersionOut": "_testing_141_XcodeVersionOut",
        "IosVersionIn": "_testing_142_IosVersionIn",
        "IosVersionOut": "_testing_143_IosVersionOut",
        "IntentFilterIn": "_testing_144_IntentFilterIn",
        "IntentFilterOut": "_testing_145_IntentFilterOut",
        "ToolResultsHistoryIn": "_testing_146_ToolResultsHistoryIn",
        "ToolResultsHistoryOut": "_testing_147_ToolResultsHistoryOut",
        "AndroidRoboTestIn": "_testing_148_AndroidRoboTestIn",
        "AndroidRoboTestOut": "_testing_149_AndroidRoboTestOut",
        "UsesFeatureIn": "_testing_150_UsesFeatureIn",
        "UsesFeatureOut": "_testing_151_UsesFeatureOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ShardingOptionIn"] = t.struct(
        {
            "manualSharding": t.proxy(renames["ManualShardingIn"]).optional(),
            "smartSharding": t.proxy(renames["SmartShardingIn"]).optional(),
            "uniformSharding": t.proxy(renames["UniformShardingIn"]).optional(),
        }
    ).named(renames["ShardingOptionIn"])
    types["ShardingOptionOut"] = t.struct(
        {
            "manualSharding": t.proxy(renames["ManualShardingOut"]).optional(),
            "smartSharding": t.proxy(renames["SmartShardingOut"]).optional(),
            "uniformSharding": t.proxy(renames["UniformShardingOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShardingOptionOut"])
    types["TestExecutionIn"] = t.struct(
        {
            "state": t.string().optional(),
            "testSpecification": t.proxy(renames["TestSpecificationIn"]).optional(),
            "timestamp": t.string().optional(),
            "toolResultsStep": t.proxy(renames["ToolResultsStepIn"]).optional(),
            "matrixId": t.string().optional(),
            "environment": t.proxy(renames["EnvironmentIn"]).optional(),
            "shard": t.proxy(renames["ShardIn"]).optional(),
            "id": t.string().optional(),
            "testDetails": t.proxy(renames["TestDetailsIn"]).optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["TestExecutionIn"])
    types["TestExecutionOut"] = t.struct(
        {
            "state": t.string().optional(),
            "testSpecification": t.proxy(renames["TestSpecificationOut"]).optional(),
            "timestamp": t.string().optional(),
            "toolResultsStep": t.proxy(renames["ToolResultsStepOut"]).optional(),
            "matrixId": t.string().optional(),
            "environment": t.proxy(renames["EnvironmentOut"]).optional(),
            "shard": t.proxy(renames["ShardOut"]).optional(),
            "id": t.string().optional(),
            "testDetails": t.proxy(renames["TestDetailsOut"]).optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestExecutionOut"])
    types["AndroidDeviceListIn"] = t.struct(
        {"androidDevices": t.array(t.proxy(renames["AndroidDeviceIn"]))}
    ).named(renames["AndroidDeviceListIn"])
    types["AndroidDeviceListOut"] = t.struct(
        {
            "androidDevices": t.array(t.proxy(renames["AndroidDeviceOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidDeviceListOut"])
    types["LocaleIn"] = t.struct(
        {
            "name": t.string().optional(),
            "region": t.string().optional(),
            "id": t.string().optional(),
            "tags": t.array(t.string()).optional(),
        }
    ).named(renames["LocaleIn"])
    types["LocaleOut"] = t.struct(
        {
            "name": t.string().optional(),
            "region": t.string().optional(),
            "id": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocaleOut"])
    types["AndroidTestLoopIn"] = t.struct(
        {
            "appBundle": t.proxy(renames["AppBundleIn"]).optional(),
            "scenarioLabels": t.array(t.string()).optional(),
            "appPackageId": t.string().optional(),
            "appApk": t.proxy(renames["FileReferenceIn"]).optional(),
            "scenarios": t.array(t.integer()).optional(),
        }
    ).named(renames["AndroidTestLoopIn"])
    types["AndroidTestLoopOut"] = t.struct(
        {
            "appBundle": t.proxy(renames["AppBundleOut"]).optional(),
            "scenarioLabels": t.array(t.string()).optional(),
            "appPackageId": t.string().optional(),
            "appApk": t.proxy(renames["FileReferenceOut"]).optional(),
            "scenarios": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidTestLoopOut"])
    types["AppBundleIn"] = t.struct(
        {"bundleLocation": t.proxy(renames["FileReferenceIn"]).optional()}
    ).named(renames["AppBundleIn"])
    types["AppBundleOut"] = t.struct(
        {
            "bundleLocation": t.proxy(renames["FileReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppBundleOut"])
    types["FileReferenceIn"] = t.struct({"gcsPath": t.string().optional()}).named(
        renames["FileReferenceIn"]
    )
    types["FileReferenceOut"] = t.struct(
        {
            "gcsPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileReferenceOut"])
    types["NetworkConfigurationCatalogIn"] = t.struct(
        {"configurations": t.array(t.proxy(renames["NetworkConfigurationIn"]))}
    ).named(renames["NetworkConfigurationCatalogIn"])
    types["NetworkConfigurationCatalogOut"] = t.struct(
        {
            "configurations": t.array(t.proxy(renames["NetworkConfigurationOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConfigurationCatalogOut"])
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
    types["SmartShardingIn"] = t.struct(
        {"targetedShardDuration": t.string().optional()}
    ).named(renames["SmartShardingIn"])
    types["SmartShardingOut"] = t.struct(
        {
            "targetedShardDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SmartShardingOut"])
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
    types["ShardIn"] = t.struct(
        {
            "numShards": t.integer().optional(),
            "testTargetsForShard": t.proxy(renames["TestTargetsForShardIn"]).optional(),
            "shardIndex": t.integer().optional(),
        }
    ).named(renames["ShardIn"])
    types["ShardOut"] = t.struct(
        {
            "numShards": t.integer().optional(),
            "testTargetsForShard": t.proxy(
                renames["TestTargetsForShardOut"]
            ).optional(),
            "shardIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShardOut"])
    types["AndroidInstrumentationTestIn"] = t.struct(
        {
            "testApk": t.proxy(renames["FileReferenceIn"]),
            "testTargets": t.array(t.string()).optional(),
            "appBundle": t.proxy(renames["AppBundleIn"]).optional(),
            "appPackageId": t.string().optional(),
            "testRunnerClass": t.string().optional(),
            "testPackageId": t.string().optional(),
            "orchestratorOption": t.string().optional(),
            "shardingOption": t.proxy(renames["ShardingOptionIn"]).optional(),
            "appApk": t.proxy(renames["FileReferenceIn"]).optional(),
        }
    ).named(renames["AndroidInstrumentationTestIn"])
    types["AndroidInstrumentationTestOut"] = t.struct(
        {
            "testApk": t.proxy(renames["FileReferenceOut"]),
            "testTargets": t.array(t.string()).optional(),
            "appBundle": t.proxy(renames["AppBundleOut"]).optional(),
            "appPackageId": t.string().optional(),
            "testRunnerClass": t.string().optional(),
            "testPackageId": t.string().optional(),
            "orchestratorOption": t.string().optional(),
            "shardingOption": t.proxy(renames["ShardingOptionOut"]).optional(),
            "appApk": t.proxy(renames["FileReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidInstrumentationTestOut"])
    types["ApkDetailIn"] = t.struct(
        {"apkManifest": t.proxy(renames["ApkManifestIn"])}
    ).named(renames["ApkDetailIn"])
    types["ApkDetailOut"] = t.struct(
        {
            "apkManifest": t.proxy(renames["ApkManifestOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApkDetailOut"])
    types["ProvidedSoftwareCatalogIn"] = t.struct(
        {
            "androidxOrchestratorVersion": t.string().optional(),
            "orchestratorVersion": t.string().optional(),
        }
    ).named(renames["ProvidedSoftwareCatalogIn"])
    types["ProvidedSoftwareCatalogOut"] = t.struct(
        {
            "androidxOrchestratorVersion": t.string().optional(),
            "orchestratorVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProvidedSoftwareCatalogOut"])
    types["SystraceSetupIn"] = t.struct(
        {"durationSeconds": t.integer().optional()}
    ).named(renames["SystraceSetupIn"])
    types["SystraceSetupOut"] = t.struct(
        {
            "durationSeconds": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystraceSetupOut"])
    types["ResultStorageIn"] = t.struct(
        {
            "resultsUrl": t.string().optional(),
            "toolResultsExecution": t.proxy(
                renames["ToolResultsExecutionIn"]
            ).optional(),
            "googleCloudStorage": t.proxy(renames["GoogleCloudStorageIn"]),
            "toolResultsHistory": t.proxy(renames["ToolResultsHistoryIn"]).optional(),
        }
    ).named(renames["ResultStorageIn"])
    types["ResultStorageOut"] = t.struct(
        {
            "resultsUrl": t.string().optional(),
            "toolResultsExecution": t.proxy(
                renames["ToolResultsExecutionOut"]
            ).optional(),
            "googleCloudStorage": t.proxy(renames["GoogleCloudStorageOut"]),
            "toolResultsHistory": t.proxy(renames["ToolResultsHistoryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultStorageOut"])
    types["TestEnvironmentCatalogIn"] = t.struct(
        {
            "androidDeviceCatalog": t.proxy(
                renames["AndroidDeviceCatalogIn"]
            ).optional(),
            "iosDeviceCatalog": t.proxy(renames["IosDeviceCatalogIn"]).optional(),
            "deviceIpBlockCatalog": t.proxy(
                renames["DeviceIpBlockCatalogIn"]
            ).optional(),
            "softwareCatalog": t.proxy(renames["ProvidedSoftwareCatalogIn"]).optional(),
            "networkConfigurationCatalog": t.proxy(
                renames["NetworkConfigurationCatalogIn"]
            ).optional(),
        }
    ).named(renames["TestEnvironmentCatalogIn"])
    types["TestEnvironmentCatalogOut"] = t.struct(
        {
            "androidDeviceCatalog": t.proxy(
                renames["AndroidDeviceCatalogOut"]
            ).optional(),
            "iosDeviceCatalog": t.proxy(renames["IosDeviceCatalogOut"]).optional(),
            "deviceIpBlockCatalog": t.proxy(
                renames["DeviceIpBlockCatalogOut"]
            ).optional(),
            "softwareCatalog": t.proxy(
                renames["ProvidedSoftwareCatalogOut"]
            ).optional(),
            "networkConfigurationCatalog": t.proxy(
                renames["NetworkConfigurationCatalogOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestEnvironmentCatalogOut"])
    types["IosDeviceListIn"] = t.struct(
        {"iosDevices": t.array(t.proxy(renames["IosDeviceIn"]))}
    ).named(renames["IosDeviceListIn"])
    types["IosDeviceListOut"] = t.struct(
        {
            "iosDevices": t.array(t.proxy(renames["IosDeviceOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosDeviceListOut"])
    types["TestSpecificationIn"] = t.struct(
        {
            "androidTestLoop": t.proxy(renames["AndroidTestLoopIn"]).optional(),
            "disablePerformanceMetrics": t.boolean().optional(),
            "iosXcTest": t.proxy(renames["IosXcTestIn"]).optional(),
            "iosTestLoop": t.proxy(renames["IosTestLoopIn"]).optional(),
            "testTimeout": t.string().optional(),
            "androidRoboTest": t.proxy(renames["AndroidRoboTestIn"]).optional(),
            "iosTestSetup": t.proxy(renames["IosTestSetupIn"]).optional(),
            "testSetup": t.proxy(renames["TestSetupIn"]).optional(),
            "disableVideoRecording": t.boolean().optional(),
            "androidInstrumentationTest": t.proxy(
                renames["AndroidInstrumentationTestIn"]
            ).optional(),
        }
    ).named(renames["TestSpecificationIn"])
    types["TestSpecificationOut"] = t.struct(
        {
            "androidTestLoop": t.proxy(renames["AndroidTestLoopOut"]).optional(),
            "disablePerformanceMetrics": t.boolean().optional(),
            "iosXcTest": t.proxy(renames["IosXcTestOut"]).optional(),
            "iosTestLoop": t.proxy(renames["IosTestLoopOut"]).optional(),
            "testTimeout": t.string().optional(),
            "androidRoboTest": t.proxy(renames["AndroidRoboTestOut"]).optional(),
            "iosTestSetup": t.proxy(renames["IosTestSetupOut"]).optional(),
            "testSetup": t.proxy(renames["TestSetupOut"]).optional(),
            "disableVideoRecording": t.boolean().optional(),
            "androidInstrumentationTest": t.proxy(
                renames["AndroidInstrumentationTestOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestSpecificationOut"])
    types["AndroidVersionIn"] = t.struct(
        {
            "versionString": t.string().optional(),
            "id": t.string().optional(),
            "releaseDate": t.proxy(renames["DateIn"]).optional(),
            "codeName": t.string().optional(),
            "apiLevel": t.integer().optional(),
            "tags": t.array(t.string()).optional(),
            "distribution": t.proxy(renames["DistributionIn"]).optional(),
        }
    ).named(renames["AndroidVersionIn"])
    types["AndroidVersionOut"] = t.struct(
        {
            "versionString": t.string().optional(),
            "id": t.string().optional(),
            "releaseDate": t.proxy(renames["DateOut"]).optional(),
            "codeName": t.string().optional(),
            "apiLevel": t.integer().optional(),
            "tags": t.array(t.string()).optional(),
            "distribution": t.proxy(renames["DistributionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidVersionOut"])
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
    types["CancelTestMatrixResponseIn"] = t.struct(
        {"testState": t.string().optional()}
    ).named(renames["CancelTestMatrixResponseIn"])
    types["CancelTestMatrixResponseOut"] = t.struct(
        {
            "testState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CancelTestMatrixResponseOut"])
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
    types["TrafficRuleIn"] = t.struct(
        {
            "burst": t.number().optional(),
            "delay": t.string().optional(),
            "bandwidth": t.number().optional(),
            "packetDuplicationRatio": t.number().optional(),
            "packetLossRatio": t.number().optional(),
        }
    ).named(renames["TrafficRuleIn"])
    types["TrafficRuleOut"] = t.struct(
        {
            "burst": t.number().optional(),
            "delay": t.string().optional(),
            "bandwidth": t.number().optional(),
            "packetDuplicationRatio": t.number().optional(),
            "packetLossRatio": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrafficRuleOut"])
    types["EnvironmentIn"] = t.struct(
        {
            "iosDevice": t.proxy(renames["IosDeviceIn"]).optional(),
            "androidDevice": t.proxy(renames["AndroidDeviceIn"]).optional(),
        }
    ).named(renames["EnvironmentIn"])
    types["EnvironmentOut"] = t.struct(
        {
            "iosDevice": t.proxy(renames["IosDeviceOut"]).optional(),
            "androidDevice": t.proxy(renames["AndroidDeviceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentOut"])
    types["AccountIn"] = t.struct(
        {"googleAuto": t.proxy(renames["GoogleAutoIn"]).optional()}
    ).named(renames["AccountIn"])
    types["AccountOut"] = t.struct(
        {
            "googleAuto": t.proxy(renames["GoogleAutoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountOut"])
    types["IosTestSetupIn"] = t.struct(
        {
            "networkProfile": t.string().optional(),
            "additionalIpas": t.array(t.proxy(renames["FileReferenceIn"])).optional(),
            "pushFiles": t.array(t.proxy(renames["IosDeviceFileIn"])).optional(),
            "pullDirectories": t.array(t.proxy(renames["IosDeviceFileIn"])).optional(),
        }
    ).named(renames["IosTestSetupIn"])
    types["IosTestSetupOut"] = t.struct(
        {
            "networkProfile": t.string().optional(),
            "additionalIpas": t.array(t.proxy(renames["FileReferenceOut"])).optional(),
            "pushFiles": t.array(t.proxy(renames["IosDeviceFileOut"])).optional(),
            "pullDirectories": t.array(t.proxy(renames["IosDeviceFileOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosTestSetupOut"])
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
    types["LauncherActivityIntentIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LauncherActivityIntentIn"]
    )
    types["LauncherActivityIntentOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LauncherActivityIntentOut"])
    types["IosModelIn"] = t.struct(
        {
            "id": t.string().optional(),
            "screenX": t.integer().optional(),
            "tags": t.array(t.string()).optional(),
            "formFactor": t.string().optional(),
            "screenY": t.integer().optional(),
            "deviceCapabilities": t.array(t.string()).optional(),
            "perVersionInfo": t.array(
                t.proxy(renames["PerIosVersionInfoIn"])
            ).optional(),
            "name": t.string().optional(),
            "screenDensity": t.integer().optional(),
            "supportedVersionIds": t.array(t.string()).optional(),
        }
    ).named(renames["IosModelIn"])
    types["IosModelOut"] = t.struct(
        {
            "id": t.string().optional(),
            "screenX": t.integer().optional(),
            "tags": t.array(t.string()).optional(),
            "formFactor": t.string().optional(),
            "screenY": t.integer().optional(),
            "deviceCapabilities": t.array(t.string()).optional(),
            "perVersionInfo": t.array(
                t.proxy(renames["PerIosVersionInfoOut"])
            ).optional(),
            "name": t.string().optional(),
            "screenDensity": t.integer().optional(),
            "supportedVersionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosModelOut"])
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
    types["AndroidMatrixIn"] = t.struct(
        {
            "orientations": t.array(t.string()),
            "androidModelIds": t.array(t.string()),
            "androidVersionIds": t.array(t.string()),
            "locales": t.array(t.string()),
        }
    ).named(renames["AndroidMatrixIn"])
    types["AndroidMatrixOut"] = t.struct(
        {
            "orientations": t.array(t.string()),
            "androidModelIds": t.array(t.string()),
            "androidVersionIds": t.array(t.string()),
            "locales": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidMatrixOut"])
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
    types["EnvironmentMatrixIn"] = t.struct(
        {
            "androidMatrix": t.proxy(renames["AndroidMatrixIn"]).optional(),
            "androidDeviceList": t.proxy(renames["AndroidDeviceListIn"]).optional(),
            "iosDeviceList": t.proxy(renames["IosDeviceListIn"]).optional(),
        }
    ).named(renames["EnvironmentMatrixIn"])
    types["EnvironmentMatrixOut"] = t.struct(
        {
            "androidMatrix": t.proxy(renames["AndroidMatrixOut"]).optional(),
            "androidDeviceList": t.proxy(renames["AndroidDeviceListOut"]).optional(),
            "iosDeviceList": t.proxy(renames["IosDeviceListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentMatrixOut"])
    types["DateIn"] = t.struct(
        {
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "month": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["RegularFileIn"] = t.struct(
        {"devicePath": t.string(), "content": t.proxy(renames["FileReferenceIn"])}
    ).named(renames["RegularFileIn"])
    types["RegularFileOut"] = t.struct(
        {
            "devicePath": t.string(),
            "content": t.proxy(renames["FileReferenceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegularFileOut"])
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
    types["IosDeviceIn"] = t.struct(
        {
            "iosModelId": t.string(),
            "iosVersionId": t.string(),
            "orientation": t.string(),
            "locale": t.string(),
        }
    ).named(renames["IosDeviceIn"])
    types["IosDeviceOut"] = t.struct(
        {
            "iosModelId": t.string(),
            "iosVersionId": t.string(),
            "orientation": t.string(),
            "locale": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosDeviceOut"])
    types["AndroidDeviceIn"] = t.struct(
        {
            "androidVersionId": t.string(),
            "orientation": t.string(),
            "androidModelId": t.string(),
            "locale": t.string(),
        }
    ).named(renames["AndroidDeviceIn"])
    types["AndroidDeviceOut"] = t.struct(
        {
            "androidVersionId": t.string(),
            "orientation": t.string(),
            "androidModelId": t.string(),
            "locale": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidDeviceOut"])
    types["ToolResultsStepIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "executionId": t.string().optional(),
            "stepId": t.string().optional(),
            "historyId": t.string().optional(),
        }
    ).named(renames["ToolResultsStepIn"])
    types["ToolResultsStepOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "executionId": t.string().optional(),
            "stepId": t.string().optional(),
            "historyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ToolResultsStepOut"])
    types["GoogleCloudStorageIn"] = t.struct({"gcsPath": t.string()}).named(
        renames["GoogleCloudStorageIn"]
    )
    types["GoogleCloudStorageOut"] = t.struct(
        {"gcsPath": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudStorageOut"])
    types["DeviceFileIn"] = t.struct(
        {
            "obbFile": t.proxy(renames["ObbFileIn"]).optional(),
            "regularFile": t.proxy(renames["RegularFileIn"]).optional(),
        }
    ).named(renames["DeviceFileIn"])
    types["DeviceFileOut"] = t.struct(
        {
            "obbFile": t.proxy(renames["ObbFileOut"]).optional(),
            "regularFile": t.proxy(renames["RegularFileOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceFileOut"])
    types["ObbFileIn"] = t.struct(
        {"obbFileName": t.string(), "obb": t.proxy(renames["FileReferenceIn"])}
    ).named(renames["ObbFileIn"])
    types["ObbFileOut"] = t.struct(
        {
            "obbFileName": t.string(),
            "obb": t.proxy(renames["FileReferenceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObbFileOut"])
    types["AndroidModelIn"] = t.struct(
        {
            "screenDensity": t.integer().optional(),
            "name": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
            "id": t.string().optional(),
            "perVersionInfo": t.array(
                t.proxy(renames["PerAndroidVersionInfoIn"])
            ).optional(),
            "supportedAbis": t.array(t.string()).optional(),
            "screenX": t.integer().optional(),
            "codename": t.string().optional(),
            "form": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "lowFpsVideoRecording": t.boolean().optional(),
            "supportedVersionIds": t.array(t.string()).optional(),
            "brand": t.string().optional(),
            "screenY": t.integer().optional(),
            "manufacturer": t.string().optional(),
            "formFactor": t.string().optional(),
        }
    ).named(renames["AndroidModelIn"])
    types["AndroidModelOut"] = t.struct(
        {
            "screenDensity": t.integer().optional(),
            "name": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
            "id": t.string().optional(),
            "perVersionInfo": t.array(
                t.proxy(renames["PerAndroidVersionInfoOut"])
            ).optional(),
            "supportedAbis": t.array(t.string()).optional(),
            "screenX": t.integer().optional(),
            "codename": t.string().optional(),
            "form": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "lowFpsVideoRecording": t.boolean().optional(),
            "supportedVersionIds": t.array(t.string()).optional(),
            "brand": t.string().optional(),
            "screenY": t.integer().optional(),
            "manufacturer": t.string().optional(),
            "formFactor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidModelOut"])
    types["IosXcTestIn"] = t.struct(
        {
            "testsZip": t.proxy(renames["FileReferenceIn"]),
            "testSpecialEntitlements": t.boolean().optional(),
            "xcodeVersion": t.string().optional(),
            "xctestrun": t.proxy(renames["FileReferenceIn"]).optional(),
            "appBundleId": t.string().optional(),
        }
    ).named(renames["IosXcTestIn"])
    types["IosXcTestOut"] = t.struct(
        {
            "testsZip": t.proxy(renames["FileReferenceOut"]),
            "testSpecialEntitlements": t.boolean().optional(),
            "xcodeVersion": t.string().optional(),
            "xctestrun": t.proxy(renames["FileReferenceOut"]).optional(),
            "appBundleId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosXcTestOut"])
    types["RoboStartingIntentIn"] = t.struct(
        {
            "launcherActivity": t.proxy(renames["LauncherActivityIntentIn"]).optional(),
            "startActivity": t.proxy(renames["StartActivityIntentIn"]).optional(),
            "timeout": t.string().optional(),
        }
    ).named(renames["RoboStartingIntentIn"])
    types["RoboStartingIntentOut"] = t.struct(
        {
            "launcherActivity": t.proxy(
                renames["LauncherActivityIntentOut"]
            ).optional(),
            "startActivity": t.proxy(renames["StartActivityIntentOut"]).optional(),
            "timeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RoboStartingIntentOut"])
    types["DeviceIpBlockIn"] = t.struct(
        {
            "form": t.string().optional(),
            "addedDate": t.proxy(renames["DateIn"]).optional(),
            "block": t.string().optional(),
        }
    ).named(renames["DeviceIpBlockIn"])
    types["DeviceIpBlockOut"] = t.struct(
        {
            "form": t.string().optional(),
            "addedDate": t.proxy(renames["DateOut"]).optional(),
            "block": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceIpBlockOut"])
    types["GetApkDetailsResponseIn"] = t.struct(
        {"apkDetail": t.proxy(renames["ApkDetailIn"]).optional()}
    ).named(renames["GetApkDetailsResponseIn"])
    types["GetApkDetailsResponseOut"] = t.struct(
        {
            "apkDetail": t.proxy(renames["ApkDetailOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetApkDetailsResponseOut"])
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
    types["ApkManifestIn"] = t.struct(
        {
            "metadata": t.array(t.proxy(renames["MetadataIn"])).optional(),
            "targetSdkVersion": t.integer().optional(),
            "maxSdkVersion": t.integer().optional(),
            "minSdkVersion": t.integer().optional(),
            "usesPermission": t.array(t.string()).optional(),
            "applicationLabel": t.string().optional(),
            "usesFeature": t.array(t.proxy(renames["UsesFeatureIn"])).optional(),
            "packageName": t.string().optional(),
            "intentFilters": t.array(t.proxy(renames["IntentFilterIn"])),
            "versionCode": t.string().optional(),
            "versionName": t.string().optional(),
        }
    ).named(renames["ApkManifestIn"])
    types["ApkManifestOut"] = t.struct(
        {
            "metadata": t.array(t.proxy(renames["MetadataOut"])).optional(),
            "targetSdkVersion": t.integer().optional(),
            "maxSdkVersion": t.integer().optional(),
            "minSdkVersion": t.integer().optional(),
            "usesPermission": t.array(t.string()).optional(),
            "applicationLabel": t.string().optional(),
            "usesFeature": t.array(t.proxy(renames["UsesFeatureOut"])).optional(),
            "packageName": t.string().optional(),
            "intentFilters": t.array(t.proxy(renames["IntentFilterOut"])),
            "versionCode": t.string().optional(),
            "versionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApkManifestOut"])
    types["TestTargetsForShardIn"] = t.struct(
        {"testTargets": t.array(t.string()).optional()}
    ).named(renames["TestTargetsForShardIn"])
    types["TestTargetsForShardOut"] = t.struct(
        {
            "testTargets": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestTargetsForShardOut"])
    types["DeviceIpBlockCatalogIn"] = t.struct(
        {"ipBlocks": t.array(t.proxy(renames["DeviceIpBlockIn"])).optional()}
    ).named(renames["DeviceIpBlockCatalogIn"])
    types["DeviceIpBlockCatalogOut"] = t.struct(
        {
            "ipBlocks": t.array(t.proxy(renames["DeviceIpBlockOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceIpBlockCatalogOut"])
    types["TestSetupIn"] = t.struct(
        {
            "directoriesToPull": t.array(t.string()).optional(),
            "networkProfile": t.string().optional(),
            "account": t.proxy(renames["AccountIn"]).optional(),
            "dontAutograntPermissions": t.boolean().optional(),
            "filesToPush": t.array(t.proxy(renames["DeviceFileIn"])).optional(),
            "environmentVariables": t.array(
                t.proxy(renames["EnvironmentVariableIn"])
            ).optional(),
            "systrace": t.proxy(renames["SystraceSetupIn"]).optional(),
            "additionalApks": t.array(t.proxy(renames["ApkIn"])).optional(),
        }
    ).named(renames["TestSetupIn"])
    types["TestSetupOut"] = t.struct(
        {
            "directoriesToPull": t.array(t.string()).optional(),
            "networkProfile": t.string().optional(),
            "account": t.proxy(renames["AccountOut"]).optional(),
            "dontAutograntPermissions": t.boolean().optional(),
            "filesToPush": t.array(t.proxy(renames["DeviceFileOut"])).optional(),
            "environmentVariables": t.array(
                t.proxy(renames["EnvironmentVariableOut"])
            ).optional(),
            "systrace": t.proxy(renames["SystraceSetupOut"]).optional(),
            "additionalApks": t.array(t.proxy(renames["ApkOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestSetupOut"])
    types["UniformShardingIn"] = t.struct({"numShards": t.integer()}).named(
        renames["UniformShardingIn"]
    )
    types["UniformShardingOut"] = t.struct(
        {
            "numShards": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UniformShardingOut"])
    types["ManualShardingIn"] = t.struct(
        {"testTargetsForShard": t.array(t.proxy(renames["TestTargetsForShardIn"]))}
    ).named(renames["ManualShardingIn"])
    types["ManualShardingOut"] = t.struct(
        {
            "testTargetsForShard": t.array(t.proxy(renames["TestTargetsForShardOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManualShardingOut"])
    types["TestMatrixIn"] = t.struct(
        {
            "testExecutions": t.array(t.proxy(renames["TestExecutionIn"])).optional(),
            "outcomeSummary": t.string().optional(),
            "flakyTestAttempts": t.integer().optional(),
            "testSpecification": t.proxy(renames["TestSpecificationIn"]),
            "timestamp": t.string().optional(),
            "resultStorage": t.proxy(renames["ResultStorageIn"]),
            "projectId": t.string().optional(),
            "testMatrixId": t.string().optional(),
            "invalidMatrixDetails": t.string().optional(),
            "state": t.string().optional(),
            "failFast": t.boolean().optional(),
            "clientInfo": t.proxy(renames["ClientInfoIn"]).optional(),
            "environmentMatrix": t.proxy(renames["EnvironmentMatrixIn"]),
        }
    ).named(renames["TestMatrixIn"])
    types["TestMatrixOut"] = t.struct(
        {
            "testExecutions": t.array(t.proxy(renames["TestExecutionOut"])).optional(),
            "outcomeSummary": t.string().optional(),
            "flakyTestAttempts": t.integer().optional(),
            "testSpecification": t.proxy(renames["TestSpecificationOut"]),
            "timestamp": t.string().optional(),
            "resultStorage": t.proxy(renames["ResultStorageOut"]),
            "projectId": t.string().optional(),
            "testMatrixId": t.string().optional(),
            "invalidMatrixDetails": t.string().optional(),
            "state": t.string().optional(),
            "failFast": t.boolean().optional(),
            "clientInfo": t.proxy(renames["ClientInfoOut"]).optional(),
            "environmentMatrix": t.proxy(renames["EnvironmentMatrixOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestMatrixOut"])
    types["RoboDirectiveIn"] = t.struct(
        {
            "actionType": t.string(),
            "resourceName": t.string(),
            "inputText": t.string().optional(),
        }
    ).named(renames["RoboDirectiveIn"])
    types["RoboDirectiveOut"] = t.struct(
        {
            "actionType": t.string(),
            "resourceName": t.string(),
            "inputText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RoboDirectiveOut"])
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
    types["IosTestLoopIn"] = t.struct(
        {
            "appIpa": t.proxy(renames["FileReferenceIn"]),
            "scenarios": t.array(t.integer()).optional(),
            "appBundleId": t.string().optional(),
        }
    ).named(renames["IosTestLoopIn"])
    types["IosTestLoopOut"] = t.struct(
        {
            "appIpa": t.proxy(renames["FileReferenceOut"]),
            "scenarios": t.array(t.integer()).optional(),
            "appBundleId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosTestLoopOut"])
    types["GoogleAutoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleAutoIn"]
    )
    types["GoogleAutoOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAutoOut"])
    types["ToolResultsExecutionIn"] = t.struct(
        {
            "executionId": t.string().optional(),
            "projectId": t.string().optional(),
            "historyId": t.string().optional(),
        }
    ).named(renames["ToolResultsExecutionIn"])
    types["ToolResultsExecutionOut"] = t.struct(
        {
            "executionId": t.string().optional(),
            "projectId": t.string().optional(),
            "historyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ToolResultsExecutionOut"])
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
    types["IosDeviceCatalogIn"] = t.struct(
        {
            "versions": t.array(t.proxy(renames["IosVersionIn"])).optional(),
            "xcodeVersions": t.array(t.proxy(renames["XcodeVersionIn"])).optional(),
            "models": t.array(t.proxy(renames["IosModelIn"])).optional(),
            "runtimeConfiguration": t.proxy(
                renames["IosRuntimeConfigurationIn"]
            ).optional(),
        }
    ).named(renames["IosDeviceCatalogIn"])
    types["IosDeviceCatalogOut"] = t.struct(
        {
            "versions": t.array(t.proxy(renames["IosVersionOut"])).optional(),
            "xcodeVersions": t.array(t.proxy(renames["XcodeVersionOut"])).optional(),
            "models": t.array(t.proxy(renames["IosModelOut"])).optional(),
            "runtimeConfiguration": t.proxy(
                renames["IosRuntimeConfigurationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosDeviceCatalogOut"])
    types["MetadataIn"] = t.struct(
        {"name": t.string().optional(), "value": t.string().optional()}
    ).named(renames["MetadataIn"])
    types["MetadataOut"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["XcodeVersionIn"] = t.struct(
        {"version": t.string().optional(), "tags": t.array(t.string()).optional()}
    ).named(renames["XcodeVersionIn"])
    types["XcodeVersionOut"] = t.struct(
        {
            "version": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["XcodeVersionOut"])
    types["IosVersionIn"] = t.struct(
        {
            "tags": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "majorVersion": t.integer().optional(),
            "supportedXcodeVersionIds": t.array(t.string()).optional(),
            "minorVersion": t.integer().optional(),
        }
    ).named(renames["IosVersionIn"])
    types["IosVersionOut"] = t.struct(
        {
            "tags": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "majorVersion": t.integer().optional(),
            "supportedXcodeVersionIds": t.array(t.string()).optional(),
            "minorVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosVersionOut"])
    types["IntentFilterIn"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "actionNames": t.array(t.string()).optional(),
            "categoryNames": t.array(t.string()).optional(),
        }
    ).named(renames["IntentFilterIn"])
    types["IntentFilterOut"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "actionNames": t.array(t.string()).optional(),
            "categoryNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntentFilterOut"])
    types["ToolResultsHistoryIn"] = t.struct(
        {"historyId": t.string(), "projectId": t.string()}
    ).named(renames["ToolResultsHistoryIn"])
    types["ToolResultsHistoryOut"] = t.struct(
        {
            "historyId": t.string(),
            "projectId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ToolResultsHistoryOut"])
    types["AndroidRoboTestIn"] = t.struct(
        {
            "maxDepth": t.integer().optional(),
            "appInitialActivity": t.string().optional(),
            "appBundle": t.proxy(renames["AppBundleIn"]).optional(),
            "appApk": t.proxy(renames["FileReferenceIn"]).optional(),
            "roboMode": t.string().optional(),
            "appPackageId": t.string().optional(),
            "roboScript": t.proxy(renames["FileReferenceIn"]).optional(),
            "roboDirectives": t.array(t.proxy(renames["RoboDirectiveIn"])).optional(),
            "startingIntents": t.array(
                t.proxy(renames["RoboStartingIntentIn"])
            ).optional(),
            "maxSteps": t.integer().optional(),
        }
    ).named(renames["AndroidRoboTestIn"])
    types["AndroidRoboTestOut"] = t.struct(
        {
            "maxDepth": t.integer().optional(),
            "appInitialActivity": t.string().optional(),
            "appBundle": t.proxy(renames["AppBundleOut"]).optional(),
            "appApk": t.proxy(renames["FileReferenceOut"]).optional(),
            "roboMode": t.string().optional(),
            "appPackageId": t.string().optional(),
            "roboScript": t.proxy(renames["FileReferenceOut"]).optional(),
            "roboDirectives": t.array(t.proxy(renames["RoboDirectiveOut"])).optional(),
            "startingIntents": t.array(
                t.proxy(renames["RoboStartingIntentOut"])
            ).optional(),
            "maxSteps": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidRoboTestOut"])
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

    functions = {}
    functions["applicationDetailServiceGetApkDetails"] = testing.post(
        "v1/applicationDetailService/getApkDetails",
        t.struct({"gcsPath": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GetApkDetailsResponseOut"]),
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
    functions["projectsTestMatricesCreate"] = testing.get(
        "v1/projects/{projectId}/testMatrices/{testMatrixId}",
        t.struct(
            {
                "testMatrixId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestMatrixOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTestMatricesCancel"] = testing.get(
        "v1/projects/{projectId}/testMatrices/{testMatrixId}",
        t.struct(
            {
                "testMatrixId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestMatrixOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTestMatricesGet"] = testing.get(
        "v1/projects/{projectId}/testMatrices/{testMatrixId}",
        t.struct(
            {
                "testMatrixId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestMatrixOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="testing", renames=renames, types=Box(types), functions=Box(functions)
    )
