from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_composer() -> Import:
    composer = HTTPRuntime("https://composer.googleapis.com/")

    renames = {
        "ErrorResponse": "_composer_1_ErrorResponse",
        "CidrBlockIn": "_composer_2_CidrBlockIn",
        "CidrBlockOut": "_composer_3_CidrBlockOut",
        "RecoveryConfigIn": "_composer_4_RecoveryConfigIn",
        "RecoveryConfigOut": "_composer_5_RecoveryConfigOut",
        "WebServerConfigIn": "_composer_6_WebServerConfigIn",
        "WebServerConfigOut": "_composer_7_WebServerConfigOut",
        "MasterAuthorizedNetworksConfigIn": "_composer_8_MasterAuthorizedNetworksConfigIn",
        "MasterAuthorizedNetworksConfigOut": "_composer_9_MasterAuthorizedNetworksConfigOut",
        "PrivateClusterConfigIn": "_composer_10_PrivateClusterConfigIn",
        "PrivateClusterConfigOut": "_composer_11_PrivateClusterConfigOut",
        "ScheduledSnapshotsConfigIn": "_composer_12_ScheduledSnapshotsConfigIn",
        "ScheduledSnapshotsConfigOut": "_composer_13_ScheduledSnapshotsConfigOut",
        "NetworkingConfigIn": "_composer_14_NetworkingConfigIn",
        "NetworkingConfigOut": "_composer_15_NetworkingConfigOut",
        "EncryptionConfigIn": "_composer_16_EncryptionConfigIn",
        "EncryptionConfigOut": "_composer_17_EncryptionConfigOut",
        "SaveSnapshotRequestIn": "_composer_18_SaveSnapshotRequestIn",
        "SaveSnapshotRequestOut": "_composer_19_SaveSnapshotRequestOut",
        "AllowedIpRangeIn": "_composer_20_AllowedIpRangeIn",
        "AllowedIpRangeOut": "_composer_21_AllowedIpRangeOut",
        "CheckUpgradeResponseIn": "_composer_22_CheckUpgradeResponseIn",
        "CheckUpgradeResponseOut": "_composer_23_CheckUpgradeResponseOut",
        "WebServerResourceIn": "_composer_24_WebServerResourceIn",
        "WebServerResourceOut": "_composer_25_WebServerResourceOut",
        "EnvironmentConfigIn": "_composer_26_EnvironmentConfigIn",
        "EnvironmentConfigOut": "_composer_27_EnvironmentConfigOut",
        "SchedulerResourceIn": "_composer_28_SchedulerResourceIn",
        "SchedulerResourceOut": "_composer_29_SchedulerResourceOut",
        "DateIn": "_composer_30_DateIn",
        "DateOut": "_composer_31_DateOut",
        "SaveSnapshotResponseIn": "_composer_32_SaveSnapshotResponseIn",
        "SaveSnapshotResponseOut": "_composer_33_SaveSnapshotResponseOut",
        "DatabaseConfigIn": "_composer_34_DatabaseConfigIn",
        "DatabaseConfigOut": "_composer_35_DatabaseConfigOut",
        "OperationMetadataIn": "_composer_36_OperationMetadataIn",
        "OperationMetadataOut": "_composer_37_OperationMetadataOut",
        "SoftwareConfigIn": "_composer_38_SoftwareConfigIn",
        "SoftwareConfigOut": "_composer_39_SoftwareConfigOut",
        "OperationIn": "_composer_40_OperationIn",
        "OperationOut": "_composer_41_OperationOut",
        "ListEnvironmentsResponseIn": "_composer_42_ListEnvironmentsResponseIn",
        "ListEnvironmentsResponseOut": "_composer_43_ListEnvironmentsResponseOut",
        "ImageVersionIn": "_composer_44_ImageVersionIn",
        "ImageVersionOut": "_composer_45_ImageVersionOut",
        "EmptyIn": "_composer_46_EmptyIn",
        "EmptyOut": "_composer_47_EmptyOut",
        "ListImageVersionsResponseIn": "_composer_48_ListImageVersionsResponseIn",
        "ListImageVersionsResponseOut": "_composer_49_ListImageVersionsResponseOut",
        "LoadSnapshotRequestIn": "_composer_50_LoadSnapshotRequestIn",
        "LoadSnapshotRequestOut": "_composer_51_LoadSnapshotRequestOut",
        "WorkerResourceIn": "_composer_52_WorkerResourceIn",
        "WorkerResourceOut": "_composer_53_WorkerResourceOut",
        "ListOperationsResponseIn": "_composer_54_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_composer_55_ListOperationsResponseOut",
        "WorkloadsConfigIn": "_composer_56_WorkloadsConfigIn",
        "WorkloadsConfigOut": "_composer_57_WorkloadsConfigOut",
        "MaintenanceWindowIn": "_composer_58_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_composer_59_MaintenanceWindowOut",
        "StatusIn": "_composer_60_StatusIn",
        "StatusOut": "_composer_61_StatusOut",
        "WebServerNetworkAccessControlIn": "_composer_62_WebServerNetworkAccessControlIn",
        "WebServerNetworkAccessControlOut": "_composer_63_WebServerNetworkAccessControlOut",
        "IPAllocationPolicyIn": "_composer_64_IPAllocationPolicyIn",
        "IPAllocationPolicyOut": "_composer_65_IPAllocationPolicyOut",
        "LoadSnapshotResponseIn": "_composer_66_LoadSnapshotResponseIn",
        "LoadSnapshotResponseOut": "_composer_67_LoadSnapshotResponseOut",
        "EnvironmentIn": "_composer_68_EnvironmentIn",
        "EnvironmentOut": "_composer_69_EnvironmentOut",
        "NodeConfigIn": "_composer_70_NodeConfigIn",
        "NodeConfigOut": "_composer_71_NodeConfigOut",
        "PrivateEnvironmentConfigIn": "_composer_72_PrivateEnvironmentConfigIn",
        "PrivateEnvironmentConfigOut": "_composer_73_PrivateEnvironmentConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["WebServerConfigIn"] = t.struct({"machineType": t.string().optional()}).named(
        renames["WebServerConfigIn"]
    )
    types["WebServerConfigOut"] = t.struct(
        {
            "machineType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebServerConfigOut"])
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
    types["PrivateClusterConfigIn"] = t.struct(
        {
            "masterIpv4CidrBlock": t.string().optional(),
            "enablePrivateEndpoint": t.boolean().optional(),
        }
    ).named(renames["PrivateClusterConfigIn"])
    types["PrivateClusterConfigOut"] = t.struct(
        {
            "masterIpv4CidrBlock": t.string().optional(),
            "masterIpv4ReservedRange": t.string().optional(),
            "enablePrivateEndpoint": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateClusterConfigOut"])
    types["ScheduledSnapshotsConfigIn"] = t.struct(
        {
            "timeZone": t.string().optional(),
            "enabled": t.boolean().optional(),
            "snapshotLocation": t.string().optional(),
            "snapshotCreationSchedule": t.string().optional(),
        }
    ).named(renames["ScheduledSnapshotsConfigIn"])
    types["ScheduledSnapshotsConfigOut"] = t.struct(
        {
            "timeZone": t.string().optional(),
            "enabled": t.boolean().optional(),
            "snapshotLocation": t.string().optional(),
            "snapshotCreationSchedule": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduledSnapshotsConfigOut"])
    types["NetworkingConfigIn"] = t.struct(
        {"connectionType": t.string().optional()}
    ).named(renames["NetworkingConfigIn"])
    types["NetworkingConfigOut"] = t.struct(
        {
            "connectionType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkingConfigOut"])
    types["EncryptionConfigIn"] = t.struct({"kmsKeyName": t.string().optional()}).named(
        renames["EncryptionConfigIn"]
    )
    types["EncryptionConfigOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionConfigOut"])
    types["SaveSnapshotRequestIn"] = t.struct(
        {"snapshotLocation": t.string().optional()}
    ).named(renames["SaveSnapshotRequestIn"])
    types["SaveSnapshotRequestOut"] = t.struct(
        {
            "snapshotLocation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SaveSnapshotRequestOut"])
    types["AllowedIpRangeIn"] = t.struct(
        {"description": t.string().optional(), "value": t.string().optional()}
    ).named(renames["AllowedIpRangeIn"])
    types["AllowedIpRangeOut"] = t.struct(
        {
            "description": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AllowedIpRangeOut"])
    types["CheckUpgradeResponseIn"] = t.struct(
        {
            "pypiDependencies": t.struct({"_": t.string().optional()}).optional(),
            "imageVersion": t.string().optional(),
        }
    ).named(renames["CheckUpgradeResponseIn"])
    types["CheckUpgradeResponseOut"] = t.struct(
        {
            "pypiConflictBuildLogExtract": t.string().optional(),
            "buildLogUri": t.string().optional(),
            "containsPypiModulesConflict": t.string().optional(),
            "pypiDependencies": t.struct({"_": t.string().optional()}).optional(),
            "imageVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckUpgradeResponseOut"])
    types["WebServerResourceIn"] = t.struct(
        {
            "memoryGb": t.number().optional(),
            "cpu": t.number().optional(),
            "storageGb": t.number().optional(),
        }
    ).named(renames["WebServerResourceIn"])
    types["WebServerResourceOut"] = t.struct(
        {
            "memoryGb": t.number().optional(),
            "cpu": t.number().optional(),
            "storageGb": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebServerResourceOut"])
    types["EnvironmentConfigIn"] = t.struct(
        {
            "encryptionConfig": t.proxy(renames["EncryptionConfigIn"]).optional(),
            "airflowUri": t.string().optional(),
            "nodeConfig": t.proxy(renames["NodeConfigIn"]).optional(),
            "softwareConfig": t.proxy(renames["SoftwareConfigIn"]).optional(),
            "privateEnvironmentConfig": t.proxy(
                renames["PrivateEnvironmentConfigIn"]
            ).optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowIn"]).optional(),
            "dagGcsPrefix": t.string().optional(),
            "workloadsConfig": t.proxy(renames["WorkloadsConfigIn"]).optional(),
            "nodeCount": t.integer().optional(),
            "recoveryConfig": t.proxy(renames["RecoveryConfigIn"]).optional(),
            "gkeCluster": t.string().optional(),
            "webServerNetworkAccessControl": t.proxy(
                renames["WebServerNetworkAccessControlIn"]
            ).optional(),
            "masterAuthorizedNetworksConfig": t.proxy(
                renames["MasterAuthorizedNetworksConfigIn"]
            ).optional(),
            "environmentSize": t.string().optional(),
            "databaseConfig": t.proxy(renames["DatabaseConfigIn"]).optional(),
            "webServerConfig": t.proxy(renames["WebServerConfigIn"]).optional(),
        }
    ).named(renames["EnvironmentConfigIn"])
    types["EnvironmentConfigOut"] = t.struct(
        {
            "encryptionConfig": t.proxy(renames["EncryptionConfigOut"]).optional(),
            "airflowUri": t.string().optional(),
            "nodeConfig": t.proxy(renames["NodeConfigOut"]).optional(),
            "softwareConfig": t.proxy(renames["SoftwareConfigOut"]).optional(),
            "privateEnvironmentConfig": t.proxy(
                renames["PrivateEnvironmentConfigOut"]
            ).optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowOut"]).optional(),
            "dagGcsPrefix": t.string().optional(),
            "workloadsConfig": t.proxy(renames["WorkloadsConfigOut"]).optional(),
            "nodeCount": t.integer().optional(),
            "airflowByoidUri": t.string().optional(),
            "recoveryConfig": t.proxy(renames["RecoveryConfigOut"]).optional(),
            "gkeCluster": t.string().optional(),
            "webServerNetworkAccessControl": t.proxy(
                renames["WebServerNetworkAccessControlOut"]
            ).optional(),
            "masterAuthorizedNetworksConfig": t.proxy(
                renames["MasterAuthorizedNetworksConfigOut"]
            ).optional(),
            "environmentSize": t.string().optional(),
            "databaseConfig": t.proxy(renames["DatabaseConfigOut"]).optional(),
            "webServerConfig": t.proxy(renames["WebServerConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentConfigOut"])
    types["SchedulerResourceIn"] = t.struct(
        {
            "memoryGb": t.number().optional(),
            "cpu": t.number().optional(),
            "storageGb": t.number().optional(),
            "count": t.integer().optional(),
        }
    ).named(renames["SchedulerResourceIn"])
    types["SchedulerResourceOut"] = t.struct(
        {
            "memoryGb": t.number().optional(),
            "cpu": t.number().optional(),
            "storageGb": t.number().optional(),
            "count": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchedulerResourceOut"])
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
    types["SaveSnapshotResponseIn"] = t.struct(
        {"snapshotPath": t.string().optional()}
    ).named(renames["SaveSnapshotResponseIn"])
    types["SaveSnapshotResponseOut"] = t.struct(
        {
            "snapshotPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SaveSnapshotResponseOut"])
    types["DatabaseConfigIn"] = t.struct({"machineType": t.string().optional()}).named(
        renames["DatabaseConfigIn"]
    )
    types["DatabaseConfigOut"] = t.struct(
        {
            "machineType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseConfigOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "resource": t.string().optional(),
            "operationType": t.string().optional(),
            "resourceUuid": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "resource": t.string().optional(),
            "operationType": t.string().optional(),
            "resourceUuid": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["SoftwareConfigIn"] = t.struct(
        {
            "pypiPackages": t.struct({"_": t.string().optional()}).optional(),
            "imageVersion": t.string().optional(),
            "schedulerCount": t.integer().optional(),
            "envVariables": t.struct({"_": t.string().optional()}).optional(),
            "airflowConfigOverrides": t.struct({"_": t.string().optional()}).optional(),
            "pythonVersion": t.string().optional(),
        }
    ).named(renames["SoftwareConfigIn"])
    types["SoftwareConfigOut"] = t.struct(
        {
            "pypiPackages": t.struct({"_": t.string().optional()}).optional(),
            "imageVersion": t.string().optional(),
            "schedulerCount": t.integer().optional(),
            "envVariables": t.struct({"_": t.string().optional()}).optional(),
            "airflowConfigOverrides": t.struct({"_": t.string().optional()}).optional(),
            "pythonVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SoftwareConfigOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["ListEnvironmentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "environments": t.array(t.proxy(renames["EnvironmentIn"])).optional(),
        }
    ).named(renames["ListEnvironmentsResponseIn"])
    types["ListEnvironmentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "environments": t.array(t.proxy(renames["EnvironmentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEnvironmentsResponseOut"])
    types["ImageVersionIn"] = t.struct(
        {
            "supportedPythonVersions": t.array(t.string()).optional(),
            "imageVersionId": t.string().optional(),
            "creationDisabled": t.boolean().optional(),
            "upgradeDisabled": t.boolean().optional(),
            "releaseDate": t.proxy(renames["DateIn"]).optional(),
            "isDefault": t.boolean().optional(),
        }
    ).named(renames["ImageVersionIn"])
    types["ImageVersionOut"] = t.struct(
        {
            "supportedPythonVersions": t.array(t.string()).optional(),
            "imageVersionId": t.string().optional(),
            "creationDisabled": t.boolean().optional(),
            "upgradeDisabled": t.boolean().optional(),
            "releaseDate": t.proxy(renames["DateOut"]).optional(),
            "isDefault": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageVersionOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["LoadSnapshotRequestIn"] = t.struct(
        {
            "skipEnvironmentVariablesSetting": t.boolean().optional(),
            "skipGcsDataCopying": t.boolean().optional(),
            "skipAirflowOverridesSetting": t.boolean().optional(),
            "skipPypiPackagesInstallation": t.boolean().optional(),
            "snapshotPath": t.string().optional(),
        }
    ).named(renames["LoadSnapshotRequestIn"])
    types["LoadSnapshotRequestOut"] = t.struct(
        {
            "skipEnvironmentVariablesSetting": t.boolean().optional(),
            "skipGcsDataCopying": t.boolean().optional(),
            "skipAirflowOverridesSetting": t.boolean().optional(),
            "skipPypiPackagesInstallation": t.boolean().optional(),
            "snapshotPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoadSnapshotRequestOut"])
    types["WorkerResourceIn"] = t.struct(
        {
            "memoryGb": t.number().optional(),
            "minCount": t.integer().optional(),
            "storageGb": t.number().optional(),
            "cpu": t.number().optional(),
            "maxCount": t.integer().optional(),
        }
    ).named(renames["WorkerResourceIn"])
    types["WorkerResourceOut"] = t.struct(
        {
            "memoryGb": t.number().optional(),
            "minCount": t.integer().optional(),
            "storageGb": t.number().optional(),
            "cpu": t.number().optional(),
            "maxCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerResourceOut"])
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
    types["WorkloadsConfigIn"] = t.struct(
        {
            "webServer": t.proxy(renames["WebServerResourceIn"]).optional(),
            "worker": t.proxy(renames["WorkerResourceIn"]).optional(),
            "scheduler": t.proxy(renames["SchedulerResourceIn"]).optional(),
        }
    ).named(renames["WorkloadsConfigIn"])
    types["WorkloadsConfigOut"] = t.struct(
        {
            "webServer": t.proxy(renames["WebServerResourceOut"]).optional(),
            "worker": t.proxy(renames["WorkerResourceOut"]).optional(),
            "scheduler": t.proxy(renames["SchedulerResourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkloadsConfigOut"])
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
    types["IPAllocationPolicyIn"] = t.struct(
        {
            "clusterIpv4CidrBlock": t.string().optional(),
            "servicesSecondaryRangeName": t.string().optional(),
            "clusterSecondaryRangeName": t.string().optional(),
            "servicesIpv4CidrBlock": t.string().optional(),
            "useIpAliases": t.boolean().optional(),
        }
    ).named(renames["IPAllocationPolicyIn"])
    types["IPAllocationPolicyOut"] = t.struct(
        {
            "clusterIpv4CidrBlock": t.string().optional(),
            "servicesSecondaryRangeName": t.string().optional(),
            "clusterSecondaryRangeName": t.string().optional(),
            "servicesIpv4CidrBlock": t.string().optional(),
            "useIpAliases": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IPAllocationPolicyOut"])
    types["LoadSnapshotResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LoadSnapshotResponseIn"]
    )
    types["LoadSnapshotResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LoadSnapshotResponseOut"])
    types["EnvironmentIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "uuid": t.string().optional(),
            "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["EnvironmentIn"])
    types["EnvironmentOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "uuid": t.string().optional(),
            "config": t.proxy(renames["EnvironmentConfigOut"]).optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentOut"])
    types["NodeConfigIn"] = t.struct(
        {
            "oauthScopes": t.array(t.string()).optional(),
            "enableIpMasqAgent": t.boolean().optional(),
            "serviceAccount": t.string().optional(),
            "network": t.string().optional(),
            "diskSizeGb": t.integer().optional(),
            "tags": t.array(t.string()).optional(),
            "machineType": t.string().optional(),
            "subnetwork": t.string().optional(),
            "location": t.string().optional(),
            "ipAllocationPolicy": t.proxy(renames["IPAllocationPolicyIn"]).optional(),
        }
    ).named(renames["NodeConfigIn"])
    types["NodeConfigOut"] = t.struct(
        {
            "oauthScopes": t.array(t.string()).optional(),
            "enableIpMasqAgent": t.boolean().optional(),
            "serviceAccount": t.string().optional(),
            "network": t.string().optional(),
            "diskSizeGb": t.integer().optional(),
            "tags": t.array(t.string()).optional(),
            "machineType": t.string().optional(),
            "subnetwork": t.string().optional(),
            "location": t.string().optional(),
            "ipAllocationPolicy": t.proxy(renames["IPAllocationPolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeConfigOut"])
    types["PrivateEnvironmentConfigIn"] = t.struct(
        {
            "cloudSqlIpv4CidrBlock": t.string().optional(),
            "privateClusterConfig": t.proxy(
                renames["PrivateClusterConfigIn"]
            ).optional(),
            "enablePrivateEnvironment": t.boolean().optional(),
            "webServerIpv4CidrBlock": t.string().optional(),
            "cloudComposerNetworkIpv4CidrBlock": t.string().optional(),
            "enablePrivatelyUsedPublicIps": t.boolean().optional(),
            "networkingConfig": t.proxy(renames["NetworkingConfigIn"]).optional(),
            "cloudComposerConnectionSubnetwork": t.string().optional(),
        }
    ).named(renames["PrivateEnvironmentConfigIn"])
    types["PrivateEnvironmentConfigOut"] = t.struct(
        {
            "cloudSqlIpv4CidrBlock": t.string().optional(),
            "privateClusterConfig": t.proxy(
                renames["PrivateClusterConfigOut"]
            ).optional(),
            "enablePrivateEnvironment": t.boolean().optional(),
            "cloudComposerNetworkIpv4ReservedRange": t.string().optional(),
            "webServerIpv4CidrBlock": t.string().optional(),
            "cloudComposerNetworkIpv4CidrBlock": t.string().optional(),
            "enablePrivatelyUsedPublicIps": t.boolean().optional(),
            "networkingConfig": t.proxy(renames["NetworkingConfigOut"]).optional(),
            "webServerIpv4ReservedRange": t.string().optional(),
            "cloudComposerConnectionSubnetwork": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateEnvironmentConfigOut"])

    functions = {}
    functions["projectsLocationsOperationsList"] = composer.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = composer.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = composer.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsDelete"] = composer.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "updateTime": t.string().optional(),
                "state": t.string().optional(),
                "uuid": t.string().optional(),
                "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
                "createTime": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsList"] = composer.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "updateTime": t.string().optional(),
                "state": t.string().optional(),
                "uuid": t.string().optional(),
                "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
                "createTime": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsLoadSnapshot"] = composer.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "updateTime": t.string().optional(),
                "state": t.string().optional(),
                "uuid": t.string().optional(),
                "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
                "createTime": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsGet"] = composer.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "updateTime": t.string().optional(),
                "state": t.string().optional(),
                "uuid": t.string().optional(),
                "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
                "createTime": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsCreate"] = composer.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "updateTime": t.string().optional(),
                "state": t.string().optional(),
                "uuid": t.string().optional(),
                "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
                "createTime": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsSaveSnapshot"] = composer.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "updateTime": t.string().optional(),
                "state": t.string().optional(),
                "uuid": t.string().optional(),
                "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
                "createTime": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsPatch"] = composer.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "updateTime": t.string().optional(),
                "state": t.string().optional(),
                "uuid": t.string().optional(),
                "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
                "createTime": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
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
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "includePastReleases": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListImageVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="composer", renames=renames, types=Box(types), functions=Box(functions)
    )
