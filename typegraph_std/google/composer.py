from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_composer():
    composer = HTTPRuntime("https://composer.googleapis.com/")

    renames = {
        "ErrorResponse": "_composer_1_ErrorResponse",
        "LoadSnapshotResponseIn": "_composer_2_LoadSnapshotResponseIn",
        "LoadSnapshotResponseOut": "_composer_3_LoadSnapshotResponseOut",
        "CidrBlockIn": "_composer_4_CidrBlockIn",
        "CidrBlockOut": "_composer_5_CidrBlockOut",
        "ListImageVersionsResponseIn": "_composer_6_ListImageVersionsResponseIn",
        "ListImageVersionsResponseOut": "_composer_7_ListImageVersionsResponseOut",
        "PollAirflowCommandRequestIn": "_composer_8_PollAirflowCommandRequestIn",
        "PollAirflowCommandRequestOut": "_composer_9_PollAirflowCommandRequestOut",
        "WebServerConfigIn": "_composer_10_WebServerConfigIn",
        "WebServerConfigOut": "_composer_11_WebServerConfigOut",
        "SaveSnapshotRequestIn": "_composer_12_SaveSnapshotRequestIn",
        "SaveSnapshotRequestOut": "_composer_13_SaveSnapshotRequestOut",
        "EncryptionConfigIn": "_composer_14_EncryptionConfigIn",
        "EncryptionConfigOut": "_composer_15_EncryptionConfigOut",
        "LoadSnapshotRequestIn": "_composer_16_LoadSnapshotRequestIn",
        "LoadSnapshotRequestOut": "_composer_17_LoadSnapshotRequestOut",
        "ExecuteAirflowCommandRequestIn": "_composer_18_ExecuteAirflowCommandRequestIn",
        "ExecuteAirflowCommandRequestOut": "_composer_19_ExecuteAirflowCommandRequestOut",
        "IPAllocationPolicyIn": "_composer_20_IPAllocationPolicyIn",
        "IPAllocationPolicyOut": "_composer_21_IPAllocationPolicyOut",
        "SoftwareConfigIn": "_composer_22_SoftwareConfigIn",
        "SoftwareConfigOut": "_composer_23_SoftwareConfigOut",
        "NodeConfigIn": "_composer_24_NodeConfigIn",
        "NodeConfigOut": "_composer_25_NodeConfigOut",
        "ImageVersionIn": "_composer_26_ImageVersionIn",
        "ImageVersionOut": "_composer_27_ImageVersionOut",
        "ExitInfoIn": "_composer_28_ExitInfoIn",
        "ExitInfoOut": "_composer_29_ExitInfoOut",
        "DatabaseFailoverResponseIn": "_composer_30_DatabaseFailoverResponseIn",
        "DatabaseFailoverResponseOut": "_composer_31_DatabaseFailoverResponseOut",
        "PollAirflowCommandResponseIn": "_composer_32_PollAirflowCommandResponseIn",
        "PollAirflowCommandResponseOut": "_composer_33_PollAirflowCommandResponseOut",
        "FetchDatabasePropertiesResponseIn": "_composer_34_FetchDatabasePropertiesResponseIn",
        "FetchDatabasePropertiesResponseOut": "_composer_35_FetchDatabasePropertiesResponseOut",
        "WebServerResourceIn": "_composer_36_WebServerResourceIn",
        "WebServerResourceOut": "_composer_37_WebServerResourceOut",
        "DateIn": "_composer_38_DateIn",
        "DateOut": "_composer_39_DateOut",
        "DatabaseFailoverRequestIn": "_composer_40_DatabaseFailoverRequestIn",
        "DatabaseFailoverRequestOut": "_composer_41_DatabaseFailoverRequestOut",
        "CheckUpgradeResponseIn": "_composer_42_CheckUpgradeResponseIn",
        "CheckUpgradeResponseOut": "_composer_43_CheckUpgradeResponseOut",
        "OperationIn": "_composer_44_OperationIn",
        "OperationOut": "_composer_45_OperationOut",
        "RecoveryConfigIn": "_composer_46_RecoveryConfigIn",
        "RecoveryConfigOut": "_composer_47_RecoveryConfigOut",
        "ExecuteAirflowCommandResponseIn": "_composer_48_ExecuteAirflowCommandResponseIn",
        "ExecuteAirflowCommandResponseOut": "_composer_49_ExecuteAirflowCommandResponseOut",
        "EnvironmentConfigIn": "_composer_50_EnvironmentConfigIn",
        "EnvironmentConfigOut": "_composer_51_EnvironmentConfigOut",
        "ListEnvironmentsResponseIn": "_composer_52_ListEnvironmentsResponseIn",
        "ListEnvironmentsResponseOut": "_composer_53_ListEnvironmentsResponseOut",
        "WebServerNetworkAccessControlIn": "_composer_54_WebServerNetworkAccessControlIn",
        "WebServerNetworkAccessControlOut": "_composer_55_WebServerNetworkAccessControlOut",
        "WorkerResourceIn": "_composer_56_WorkerResourceIn",
        "WorkerResourceOut": "_composer_57_WorkerResourceOut",
        "WorkloadsConfigIn": "_composer_58_WorkloadsConfigIn",
        "WorkloadsConfigOut": "_composer_59_WorkloadsConfigOut",
        "StopAirflowCommandRequestIn": "_composer_60_StopAirflowCommandRequestIn",
        "StopAirflowCommandRequestOut": "_composer_61_StopAirflowCommandRequestOut",
        "LineIn": "_composer_62_LineIn",
        "LineOut": "_composer_63_LineOut",
        "SchedulerResourceIn": "_composer_64_SchedulerResourceIn",
        "SchedulerResourceOut": "_composer_65_SchedulerResourceOut",
        "MasterAuthorizedNetworksConfigIn": "_composer_66_MasterAuthorizedNetworksConfigIn",
        "MasterAuthorizedNetworksConfigOut": "_composer_67_MasterAuthorizedNetworksConfigOut",
        "NetworkingConfigIn": "_composer_68_NetworkingConfigIn",
        "NetworkingConfigOut": "_composer_69_NetworkingConfigOut",
        "MaintenanceWindowIn": "_composer_70_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_composer_71_MaintenanceWindowOut",
        "PrivateEnvironmentConfigIn": "_composer_72_PrivateEnvironmentConfigIn",
        "PrivateEnvironmentConfigOut": "_composer_73_PrivateEnvironmentConfigOut",
        "StatusIn": "_composer_74_StatusIn",
        "StatusOut": "_composer_75_StatusOut",
        "ListOperationsResponseIn": "_composer_76_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_composer_77_ListOperationsResponseOut",
        "AllowedIpRangeIn": "_composer_78_AllowedIpRangeIn",
        "AllowedIpRangeOut": "_composer_79_AllowedIpRangeOut",
        "DatabaseConfigIn": "_composer_80_DatabaseConfigIn",
        "DatabaseConfigOut": "_composer_81_DatabaseConfigOut",
        "SaveSnapshotResponseIn": "_composer_82_SaveSnapshotResponseIn",
        "SaveSnapshotResponseOut": "_composer_83_SaveSnapshotResponseOut",
        "EmptyIn": "_composer_84_EmptyIn",
        "EmptyOut": "_composer_85_EmptyOut",
        "OperationMetadataIn": "_composer_86_OperationMetadataIn",
        "OperationMetadataOut": "_composer_87_OperationMetadataOut",
        "EnvironmentIn": "_composer_88_EnvironmentIn",
        "EnvironmentOut": "_composer_89_EnvironmentOut",
        "ScheduledSnapshotsConfigIn": "_composer_90_ScheduledSnapshotsConfigIn",
        "ScheduledSnapshotsConfigOut": "_composer_91_ScheduledSnapshotsConfigOut",
        "StopAirflowCommandResponseIn": "_composer_92_StopAirflowCommandResponseIn",
        "StopAirflowCommandResponseOut": "_composer_93_StopAirflowCommandResponseOut",
        "PrivateClusterConfigIn": "_composer_94_PrivateClusterConfigIn",
        "PrivateClusterConfigOut": "_composer_95_PrivateClusterConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["LoadSnapshotResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LoadSnapshotResponseIn"]
    )
    types["LoadSnapshotResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LoadSnapshotResponseOut"])
    types["CidrBlockIn"] = t.struct(
        {"displayName": t.string().optional(), "cidrBlock": t.string().optional()}
    ).named(renames["CidrBlockIn"])
    types["CidrBlockOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "cidrBlock": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CidrBlockOut"])
    types["ListImageVersionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "imageVersions": t.array(t.proxy(renames["ImageVersionIn"])).optional(),
        }
    ).named(renames["ListImageVersionsResponseIn"])
    types["ListImageVersionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "imageVersions": t.array(t.proxy(renames["ImageVersionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListImageVersionsResponseOut"])
    types["PollAirflowCommandRequestIn"] = t.struct(
        {
            "pod": t.string().optional(),
            "executionId": t.string().optional(),
            "nextLineNumber": t.integer().optional(),
            "podNamespace": t.string().optional(),
        }
    ).named(renames["PollAirflowCommandRequestIn"])
    types["PollAirflowCommandRequestOut"] = t.struct(
        {
            "pod": t.string().optional(),
            "executionId": t.string().optional(),
            "nextLineNumber": t.integer().optional(),
            "podNamespace": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PollAirflowCommandRequestOut"])
    types["WebServerConfigIn"] = t.struct({"machineType": t.string().optional()}).named(
        renames["WebServerConfigIn"]
    )
    types["WebServerConfigOut"] = t.struct(
        {
            "machineType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebServerConfigOut"])
    types["SaveSnapshotRequestIn"] = t.struct(
        {"snapshotLocation": t.string().optional()}
    ).named(renames["SaveSnapshotRequestIn"])
    types["SaveSnapshotRequestOut"] = t.struct(
        {
            "snapshotLocation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SaveSnapshotRequestOut"])
    types["EncryptionConfigIn"] = t.struct({"kmsKeyName": t.string().optional()}).named(
        renames["EncryptionConfigIn"]
    )
    types["EncryptionConfigOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionConfigOut"])
    types["LoadSnapshotRequestIn"] = t.struct(
        {
            "skipPypiPackagesInstallation": t.boolean().optional(),
            "skipAirflowOverridesSetting": t.boolean().optional(),
            "snapshotPath": t.string().optional(),
            "skipGcsDataCopying": t.boolean().optional(),
            "skipEnvironmentVariablesSetting": t.boolean().optional(),
        }
    ).named(renames["LoadSnapshotRequestIn"])
    types["LoadSnapshotRequestOut"] = t.struct(
        {
            "skipPypiPackagesInstallation": t.boolean().optional(),
            "skipAirflowOverridesSetting": t.boolean().optional(),
            "snapshotPath": t.string().optional(),
            "skipGcsDataCopying": t.boolean().optional(),
            "skipEnvironmentVariablesSetting": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoadSnapshotRequestOut"])
    types["ExecuteAirflowCommandRequestIn"] = t.struct(
        {
            "command": t.string().optional(),
            "subcommand": t.string().optional(),
            "parameters": t.array(t.string()).optional(),
        }
    ).named(renames["ExecuteAirflowCommandRequestIn"])
    types["ExecuteAirflowCommandRequestOut"] = t.struct(
        {
            "command": t.string().optional(),
            "subcommand": t.string().optional(),
            "parameters": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteAirflowCommandRequestOut"])
    types["IPAllocationPolicyIn"] = t.struct(
        {
            "servicesSecondaryRangeName": t.string().optional(),
            "clusterSecondaryRangeName": t.string().optional(),
            "servicesIpv4CidrBlock": t.string().optional(),
            "clusterIpv4CidrBlock": t.string().optional(),
            "useIpAliases": t.boolean().optional(),
        }
    ).named(renames["IPAllocationPolicyIn"])
    types["IPAllocationPolicyOut"] = t.struct(
        {
            "servicesSecondaryRangeName": t.string().optional(),
            "clusterSecondaryRangeName": t.string().optional(),
            "servicesIpv4CidrBlock": t.string().optional(),
            "clusterIpv4CidrBlock": t.string().optional(),
            "useIpAliases": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IPAllocationPolicyOut"])
    types["SoftwareConfigIn"] = t.struct(
        {
            "pypiPackages": t.struct({"_": t.string().optional()}).optional(),
            "schedulerCount": t.integer().optional(),
            "airflowConfigOverrides": t.struct({"_": t.string().optional()}).optional(),
            "imageVersion": t.string().optional(),
            "pythonVersion": t.string().optional(),
            "envVariables": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SoftwareConfigIn"])
    types["SoftwareConfigOut"] = t.struct(
        {
            "pypiPackages": t.struct({"_": t.string().optional()}).optional(),
            "schedulerCount": t.integer().optional(),
            "airflowConfigOverrides": t.struct({"_": t.string().optional()}).optional(),
            "imageVersion": t.string().optional(),
            "pythonVersion": t.string().optional(),
            "envVariables": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SoftwareConfigOut"])
    types["NodeConfigIn"] = t.struct(
        {
            "subnetwork": t.string().optional(),
            "location": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "network": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "enableIpMasqAgent": t.boolean().optional(),
            "machineType": t.string().optional(),
            "ipAllocationPolicy": t.proxy(renames["IPAllocationPolicyIn"]).optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "diskSizeGb": t.integer().optional(),
        }
    ).named(renames["NodeConfigIn"])
    types["NodeConfigOut"] = t.struct(
        {
            "subnetwork": t.string().optional(),
            "location": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "network": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "enableIpMasqAgent": t.boolean().optional(),
            "machineType": t.string().optional(),
            "ipAllocationPolicy": t.proxy(renames["IPAllocationPolicyOut"]).optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "diskSizeGb": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeConfigOut"])
    types["ImageVersionIn"] = t.struct(
        {
            "upgradeDisabled": t.boolean().optional(),
            "creationDisabled": t.boolean().optional(),
            "supportedPythonVersions": t.array(t.string()).optional(),
            "releaseDate": t.proxy(renames["DateIn"]).optional(),
            "isDefault": t.boolean().optional(),
            "imageVersionId": t.string().optional(),
        }
    ).named(renames["ImageVersionIn"])
    types["ImageVersionOut"] = t.struct(
        {
            "upgradeDisabled": t.boolean().optional(),
            "creationDisabled": t.boolean().optional(),
            "supportedPythonVersions": t.array(t.string()).optional(),
            "releaseDate": t.proxy(renames["DateOut"]).optional(),
            "isDefault": t.boolean().optional(),
            "imageVersionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageVersionOut"])
    types["ExitInfoIn"] = t.struct(
        {"error": t.string().optional(), "exitCode": t.integer().optional()}
    ).named(renames["ExitInfoIn"])
    types["ExitInfoOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "exitCode": t.integer().optional(),
        }
    ).named(renames["ExitInfoOut"])
    types["DatabaseFailoverResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DatabaseFailoverResponseIn"]
    )
    types["DatabaseFailoverResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DatabaseFailoverResponseOut"])
    types["PollAirflowCommandResponseIn"] = t.struct(
        {
            "outputEnd": t.boolean().optional(),
            "exitInfo": t.proxy(renames["ExitInfoIn"]).optional(),
            "output": t.array(t.proxy(renames["LineIn"])).optional(),
        }
    ).named(renames["PollAirflowCommandResponseIn"])
    types["PollAirflowCommandResponseOut"] = t.struct(
        {
            "outputEnd": t.boolean().optional(),
            "exitInfo": t.proxy(renames["ExitInfoOut"]).optional(),
            "output": t.array(t.proxy(renames["LineOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PollAirflowCommandResponseOut"])
    types["FetchDatabasePropertiesResponseIn"] = t.struct(
        {
            "secondaryGceZone": t.string().optional(),
            "primaryGceZone": t.string().optional(),
            "isFailoverReplicaAvailable": t.boolean().optional(),
        }
    ).named(renames["FetchDatabasePropertiesResponseIn"])
    types["FetchDatabasePropertiesResponseOut"] = t.struct(
        {
            "secondaryGceZone": t.string().optional(),
            "primaryGceZone": t.string().optional(),
            "isFailoverReplicaAvailable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchDatabasePropertiesResponseOut"])
    types["WebServerResourceIn"] = t.struct(
        {
            "storageGb": t.number().optional(),
            "cpu": t.number().optional(),
            "memoryGb": t.number().optional(),
        }
    ).named(renames["WebServerResourceIn"])
    types["WebServerResourceOut"] = t.struct(
        {
            "storageGb": t.number().optional(),
            "cpu": t.number().optional(),
            "memoryGb": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebServerResourceOut"])
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
    types["DatabaseFailoverRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DatabaseFailoverRequestIn"]
    )
    types["DatabaseFailoverRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DatabaseFailoverRequestOut"])
    types["CheckUpgradeResponseIn"] = t.struct(
        {
            "pypiDependencies": t.struct({"_": t.string().optional()}).optional(),
            "imageVersion": t.string().optional(),
        }
    ).named(renames["CheckUpgradeResponseIn"])
    types["CheckUpgradeResponseOut"] = t.struct(
        {
            "pypiDependencies": t.struct({"_": t.string().optional()}).optional(),
            "imageVersion": t.string().optional(),
            "containsPypiModulesConflict": t.string().optional(),
            "pypiConflictBuildLogExtract": t.string().optional(),
            "buildLogUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckUpgradeResponseOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["RecoveryConfigIn"] = t.struct(
        {
            "scheduledSnapshotsConfig": t.proxy(
                renames["ScheduledSnapshotsConfigIn"]
            ).optional()
        }
    ).named(renames["RecoveryConfigIn"])
    types["RecoveryConfigOut"] = t.struct(
        {
            "scheduledSnapshotsConfig": t.proxy(
                renames["ScheduledSnapshotsConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecoveryConfigOut"])
    types["ExecuteAirflowCommandResponseIn"] = t.struct(
        {
            "executionId": t.string().optional(),
            "error": t.string().optional(),
            "podNamespace": t.string().optional(),
            "pod": t.string().optional(),
        }
    ).named(renames["ExecuteAirflowCommandResponseIn"])
    types["ExecuteAirflowCommandResponseOut"] = t.struct(
        {
            "executionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "podNamespace": t.string().optional(),
            "pod": t.string().optional(),
        }
    ).named(renames["ExecuteAirflowCommandResponseOut"])
    types["EnvironmentConfigIn"] = t.struct(
        {
            "databaseConfig": t.proxy(renames["DatabaseConfigIn"]).optional(),
            "privateEnvironmentConfig": t.proxy(
                renames["PrivateEnvironmentConfigIn"]
            ).optional(),
            "resilienceMode": t.string().optional(),
            "masterAuthorizedNetworksConfig": t.proxy(
                renames["MasterAuthorizedNetworksConfigIn"]
            ).optional(),
            "nodeCount": t.integer().optional(),
            "webServerConfig": t.proxy(renames["WebServerConfigIn"]).optional(),
            "recoveryConfig": t.proxy(renames["RecoveryConfigIn"]).optional(),
            "workloadsConfig": t.proxy(renames["WorkloadsConfigIn"]).optional(),
            "gkeCluster": t.string().optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigIn"]).optional(),
            "dagGcsPrefix": t.string().optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowIn"]).optional(),
            "softwareConfig": t.proxy(renames["SoftwareConfigIn"]).optional(),
            "nodeConfig": t.proxy(renames["NodeConfigIn"]).optional(),
            "webServerNetworkAccessControl": t.proxy(
                renames["WebServerNetworkAccessControlIn"]
            ).optional(),
            "airflowUri": t.string().optional(),
            "environmentSize": t.string().optional(),
        }
    ).named(renames["EnvironmentConfigIn"])
    types["EnvironmentConfigOut"] = t.struct(
        {
            "databaseConfig": t.proxy(renames["DatabaseConfigOut"]).optional(),
            "privateEnvironmentConfig": t.proxy(
                renames["PrivateEnvironmentConfigOut"]
            ).optional(),
            "resilienceMode": t.string().optional(),
            "masterAuthorizedNetworksConfig": t.proxy(
                renames["MasterAuthorizedNetworksConfigOut"]
            ).optional(),
            "nodeCount": t.integer().optional(),
            "webServerConfig": t.proxy(renames["WebServerConfigOut"]).optional(),
            "recoveryConfig": t.proxy(renames["RecoveryConfigOut"]).optional(),
            "workloadsConfig": t.proxy(renames["WorkloadsConfigOut"]).optional(),
            "gkeCluster": t.string().optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigOut"]).optional(),
            "dagGcsPrefix": t.string().optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowOut"]).optional(),
            "airflowByoidUri": t.string().optional(),
            "softwareConfig": t.proxy(renames["SoftwareConfigOut"]).optional(),
            "nodeConfig": t.proxy(renames["NodeConfigOut"]).optional(),
            "webServerNetworkAccessControl": t.proxy(
                renames["WebServerNetworkAccessControlOut"]
            ).optional(),
            "airflowUri": t.string().optional(),
            "environmentSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentConfigOut"])
    types["ListEnvironmentsResponseIn"] = t.struct(
        {
            "environments": t.array(t.proxy(renames["EnvironmentIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListEnvironmentsResponseIn"])
    types["ListEnvironmentsResponseOut"] = t.struct(
        {
            "environments": t.array(t.proxy(renames["EnvironmentOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEnvironmentsResponseOut"])
    types["WebServerNetworkAccessControlIn"] = t.struct(
        {"allowedIpRanges": t.array(t.proxy(renames["AllowedIpRangeIn"])).optional()}
    ).named(renames["WebServerNetworkAccessControlIn"])
    types["WebServerNetworkAccessControlOut"] = t.struct(
        {
            "allowedIpRanges": t.array(
                t.proxy(renames["AllowedIpRangeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebServerNetworkAccessControlOut"])
    types["WorkerResourceIn"] = t.struct(
        {
            "cpu": t.number().optional(),
            "memoryGb": t.number().optional(),
            "minCount": t.integer().optional(),
            "maxCount": t.integer().optional(),
            "storageGb": t.number().optional(),
        }
    ).named(renames["WorkerResourceIn"])
    types["WorkerResourceOut"] = t.struct(
        {
            "cpu": t.number().optional(),
            "memoryGb": t.number().optional(),
            "minCount": t.integer().optional(),
            "maxCount": t.integer().optional(),
            "storageGb": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerResourceOut"])
    types["WorkloadsConfigIn"] = t.struct(
        {
            "worker": t.proxy(renames["WorkerResourceIn"]).optional(),
            "scheduler": t.proxy(renames["SchedulerResourceIn"]).optional(),
            "webServer": t.proxy(renames["WebServerResourceIn"]).optional(),
        }
    ).named(renames["WorkloadsConfigIn"])
    types["WorkloadsConfigOut"] = t.struct(
        {
            "worker": t.proxy(renames["WorkerResourceOut"]).optional(),
            "scheduler": t.proxy(renames["SchedulerResourceOut"]).optional(),
            "webServer": t.proxy(renames["WebServerResourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkloadsConfigOut"])
    types["StopAirflowCommandRequestIn"] = t.struct(
        {
            "force": t.boolean().optional(),
            "pod": t.string().optional(),
            "executionId": t.string().optional(),
            "podNamespace": t.string().optional(),
        }
    ).named(renames["StopAirflowCommandRequestIn"])
    types["StopAirflowCommandRequestOut"] = t.struct(
        {
            "force": t.boolean().optional(),
            "pod": t.string().optional(),
            "executionId": t.string().optional(),
            "podNamespace": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StopAirflowCommandRequestOut"])
    types["LineIn"] = t.struct(
        {"lineNumber": t.integer().optional(), "content": t.string().optional()}
    ).named(renames["LineIn"])
    types["LineOut"] = t.struct(
        {
            "lineNumber": t.integer().optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LineOut"])
    types["SchedulerResourceIn"] = t.struct(
        {
            "cpu": t.number().optional(),
            "count": t.integer().optional(),
            "memoryGb": t.number().optional(),
            "storageGb": t.number().optional(),
        }
    ).named(renames["SchedulerResourceIn"])
    types["SchedulerResourceOut"] = t.struct(
        {
            "cpu": t.number().optional(),
            "count": t.integer().optional(),
            "memoryGb": t.number().optional(),
            "storageGb": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchedulerResourceOut"])
    types["MasterAuthorizedNetworksConfigIn"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "cidrBlocks": t.array(t.proxy(renames["CidrBlockIn"])).optional(),
        }
    ).named(renames["MasterAuthorizedNetworksConfigIn"])
    types["MasterAuthorizedNetworksConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "cidrBlocks": t.array(t.proxy(renames["CidrBlockOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MasterAuthorizedNetworksConfigOut"])
    types["NetworkingConfigIn"] = t.struct(
        {"connectionType": t.string().optional()}
    ).named(renames["NetworkingConfigIn"])
    types["NetworkingConfigOut"] = t.struct(
        {
            "connectionType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkingConfigOut"])
    types["MaintenanceWindowIn"] = t.struct(
        {"startTime": t.string(), "recurrence": t.string(), "endTime": t.string()}
    ).named(renames["MaintenanceWindowIn"])
    types["MaintenanceWindowOut"] = t.struct(
        {
            "startTime": t.string(),
            "recurrence": t.string(),
            "endTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceWindowOut"])
    types["PrivateEnvironmentConfigIn"] = t.struct(
        {
            "cloudComposerConnectionSubnetwork": t.string().optional(),
            "cloudSqlIpv4CidrBlock": t.string().optional(),
            "networkingConfig": t.proxy(renames["NetworkingConfigIn"]).optional(),
            "cloudComposerNetworkIpv4CidrBlock": t.string().optional(),
            "enablePrivatelyUsedPublicIps": t.boolean().optional(),
            "privateClusterConfig": t.proxy(
                renames["PrivateClusterConfigIn"]
            ).optional(),
            "enablePrivateEnvironment": t.boolean().optional(),
            "webServerIpv4CidrBlock": t.string().optional(),
        }
    ).named(renames["PrivateEnvironmentConfigIn"])
    types["PrivateEnvironmentConfigOut"] = t.struct(
        {
            "cloudComposerConnectionSubnetwork": t.string().optional(),
            "cloudSqlIpv4CidrBlock": t.string().optional(),
            "networkingConfig": t.proxy(renames["NetworkingConfigOut"]).optional(),
            "cloudComposerNetworkIpv4CidrBlock": t.string().optional(),
            "enablePrivatelyUsedPublicIps": t.boolean().optional(),
            "privateClusterConfig": t.proxy(
                renames["PrivateClusterConfigOut"]
            ).optional(),
            "enablePrivateEnvironment": t.boolean().optional(),
            "cloudComposerNetworkIpv4ReservedRange": t.string().optional(),
            "webServerIpv4CidrBlock": t.string().optional(),
            "webServerIpv4ReservedRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateEnvironmentConfigOut"])
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
    types["ListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["AllowedIpRangeIn"] = t.struct(
        {"value": t.string().optional(), "description": t.string().optional()}
    ).named(renames["AllowedIpRangeIn"])
    types["AllowedIpRangeOut"] = t.struct(
        {
            "value": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AllowedIpRangeOut"])
    types["DatabaseConfigIn"] = t.struct({"machineType": t.string().optional()}).named(
        renames["DatabaseConfigIn"]
    )
    types["DatabaseConfigOut"] = t.struct(
        {
            "machineType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseConfigOut"])
    types["SaveSnapshotResponseIn"] = t.struct(
        {"snapshotPath": t.string().optional()}
    ).named(renames["SaveSnapshotResponseIn"])
    types["SaveSnapshotResponseOut"] = t.struct(
        {
            "snapshotPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SaveSnapshotResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "operationType": t.string().optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "resourceUuid": t.string().optional(),
            "resource": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "operationType": t.string().optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "resourceUuid": t.string().optional(),
            "resource": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["EnvironmentIn"] = t.struct(
        {
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "uuid": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
        }
    ).named(renames["EnvironmentIn"])
    types["EnvironmentOut"] = t.struct(
        {
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "uuid": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "config": t.proxy(renames["EnvironmentConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentOut"])
    types["ScheduledSnapshotsConfigIn"] = t.struct(
        {
            "snapshotLocation": t.string().optional(),
            "timeZone": t.string().optional(),
            "enabled": t.boolean().optional(),
            "snapshotCreationSchedule": t.string().optional(),
        }
    ).named(renames["ScheduledSnapshotsConfigIn"])
    types["ScheduledSnapshotsConfigOut"] = t.struct(
        {
            "snapshotLocation": t.string().optional(),
            "timeZone": t.string().optional(),
            "enabled": t.boolean().optional(),
            "snapshotCreationSchedule": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduledSnapshotsConfigOut"])
    types["StopAirflowCommandResponseIn"] = t.struct(
        {"output": t.array(t.string()).optional(), "isDone": t.boolean().optional()}
    ).named(renames["StopAirflowCommandResponseIn"])
    types["StopAirflowCommandResponseOut"] = t.struct(
        {
            "output": t.array(t.string()).optional(),
            "isDone": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StopAirflowCommandResponseOut"])
    types["PrivateClusterConfigIn"] = t.struct(
        {
            "masterIpv4CidrBlock": t.string().optional(),
            "enablePrivateEndpoint": t.boolean().optional(),
        }
    ).named(renames["PrivateClusterConfigIn"])
    types["PrivateClusterConfigOut"] = t.struct(
        {
            "masterIpv4ReservedRange": t.string().optional(),
            "masterIpv4CidrBlock": t.string().optional(),
            "enablePrivateEndpoint": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateClusterConfigOut"])

    functions = {}
    functions["projectsLocationsEnvironmentsList"] = composer.post(
        "v1/{parent}/environments",
        t.struct(
            {
                "parent": t.string().optional(),
                "state": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "uuid": t.string().optional(),
                "createTime": t.string().optional(),
                "updateTime": t.string().optional(),
                "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsDelete"] = composer.post(
        "v1/{parent}/environments",
        t.struct(
            {
                "parent": t.string().optional(),
                "state": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "uuid": t.string().optional(),
                "createTime": t.string().optional(),
                "updateTime": t.string().optional(),
                "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsExecuteAirflowCommand"] = composer.post(
        "v1/{parent}/environments",
        t.struct(
            {
                "parent": t.string().optional(),
                "state": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "uuid": t.string().optional(),
                "createTime": t.string().optional(),
                "updateTime": t.string().optional(),
                "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsLoadSnapshot"] = composer.post(
        "v1/{parent}/environments",
        t.struct(
            {
                "parent": t.string().optional(),
                "state": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "uuid": t.string().optional(),
                "createTime": t.string().optional(),
                "updateTime": t.string().optional(),
                "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsStopAirflowCommand"] = composer.post(
        "v1/{parent}/environments",
        t.struct(
            {
                "parent": t.string().optional(),
                "state": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "uuid": t.string().optional(),
                "createTime": t.string().optional(),
                "updateTime": t.string().optional(),
                "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsPatch"] = composer.post(
        "v1/{parent}/environments",
        t.struct(
            {
                "parent": t.string().optional(),
                "state": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "uuid": t.string().optional(),
                "createTime": t.string().optional(),
                "updateTime": t.string().optional(),
                "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsPollAirflowCommand"] = composer.post(
        "v1/{parent}/environments",
        t.struct(
            {
                "parent": t.string().optional(),
                "state": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "uuid": t.string().optional(),
                "createTime": t.string().optional(),
                "updateTime": t.string().optional(),
                "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsGet"] = composer.post(
        "v1/{parent}/environments",
        t.struct(
            {
                "parent": t.string().optional(),
                "state": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "uuid": t.string().optional(),
                "createTime": t.string().optional(),
                "updateTime": t.string().optional(),
                "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsSaveSnapshot"] = composer.post(
        "v1/{parent}/environments",
        t.struct(
            {
                "parent": t.string().optional(),
                "state": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "uuid": t.string().optional(),
                "createTime": t.string().optional(),
                "updateTime": t.string().optional(),
                "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsDatabaseFailover"] = composer.post(
        "v1/{parent}/environments",
        t.struct(
            {
                "parent": t.string().optional(),
                "state": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "uuid": t.string().optional(),
                "createTime": t.string().optional(),
                "updateTime": t.string().optional(),
                "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsFetchDatabaseProperties"] = composer.post(
        "v1/{parent}/environments",
        t.struct(
            {
                "parent": t.string().optional(),
                "state": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "uuid": t.string().optional(),
                "createTime": t.string().optional(),
                "updateTime": t.string().optional(),
                "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsCreate"] = composer.post(
        "v1/{parent}/environments",
        t.struct(
            {
                "parent": t.string().optional(),
                "state": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "uuid": t.string().optional(),
                "createTime": t.string().optional(),
                "updateTime": t.string().optional(),
                "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImageVersionsList"] = composer.get(
        "v1/{parent}/imageVersions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "includePastReleases": t.boolean().optional(),
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListImageVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = composer.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = composer.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = composer.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="composer", renames=renames, types=Box(types), functions=Box(functions)
    )
