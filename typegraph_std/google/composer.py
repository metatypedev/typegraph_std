from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_composer() -> Import:
    composer = HTTPRuntime("https://composer.googleapis.com/")

    renames = {
        "ErrorResponse": "_composer_1_ErrorResponse",
        "SoftwareConfigIn": "_composer_2_SoftwareConfigIn",
        "SoftwareConfigOut": "_composer_3_SoftwareConfigOut",
        "EnvironmentConfigIn": "_composer_4_EnvironmentConfigIn",
        "EnvironmentConfigOut": "_composer_5_EnvironmentConfigOut",
        "ImageVersionIn": "_composer_6_ImageVersionIn",
        "ImageVersionOut": "_composer_7_ImageVersionOut",
        "IPAllocationPolicyIn": "_composer_8_IPAllocationPolicyIn",
        "IPAllocationPolicyOut": "_composer_9_IPAllocationPolicyOut",
        "SchedulerResourceIn": "_composer_10_SchedulerResourceIn",
        "SchedulerResourceOut": "_composer_11_SchedulerResourceOut",
        "PrivateClusterConfigIn": "_composer_12_PrivateClusterConfigIn",
        "PrivateClusterConfigOut": "_composer_13_PrivateClusterConfigOut",
        "SaveSnapshotResponseIn": "_composer_14_SaveSnapshotResponseIn",
        "SaveSnapshotResponseOut": "_composer_15_SaveSnapshotResponseOut",
        "WebServerResourceIn": "_composer_16_WebServerResourceIn",
        "WebServerResourceOut": "_composer_17_WebServerResourceOut",
        "ListOperationsResponseIn": "_composer_18_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_composer_19_ListOperationsResponseOut",
        "EncryptionConfigIn": "_composer_20_EncryptionConfigIn",
        "EncryptionConfigOut": "_composer_21_EncryptionConfigOut",
        "MaintenanceWindowIn": "_composer_22_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_composer_23_MaintenanceWindowOut",
        "SaveSnapshotRequestIn": "_composer_24_SaveSnapshotRequestIn",
        "SaveSnapshotRequestOut": "_composer_25_SaveSnapshotRequestOut",
        "AllowedIpRangeIn": "_composer_26_AllowedIpRangeIn",
        "AllowedIpRangeOut": "_composer_27_AllowedIpRangeOut",
        "WebServerConfigIn": "_composer_28_WebServerConfigIn",
        "WebServerConfigOut": "_composer_29_WebServerConfigOut",
        "ScheduledSnapshotsConfigIn": "_composer_30_ScheduledSnapshotsConfigIn",
        "ScheduledSnapshotsConfigOut": "_composer_31_ScheduledSnapshotsConfigOut",
        "NetworkingConfigIn": "_composer_32_NetworkingConfigIn",
        "NetworkingConfigOut": "_composer_33_NetworkingConfigOut",
        "LoadSnapshotResponseIn": "_composer_34_LoadSnapshotResponseIn",
        "LoadSnapshotResponseOut": "_composer_35_LoadSnapshotResponseOut",
        "StatusIn": "_composer_36_StatusIn",
        "StatusOut": "_composer_37_StatusOut",
        "DatabaseConfigIn": "_composer_38_DatabaseConfigIn",
        "DatabaseConfigOut": "_composer_39_DatabaseConfigOut",
        "RecoveryConfigIn": "_composer_40_RecoveryConfigIn",
        "RecoveryConfigOut": "_composer_41_RecoveryConfigOut",
        "MasterAuthorizedNetworksConfigIn": "_composer_42_MasterAuthorizedNetworksConfigIn",
        "MasterAuthorizedNetworksConfigOut": "_composer_43_MasterAuthorizedNetworksConfigOut",
        "EmptyIn": "_composer_44_EmptyIn",
        "EmptyOut": "_composer_45_EmptyOut",
        "WorkerResourceIn": "_composer_46_WorkerResourceIn",
        "WorkerResourceOut": "_composer_47_WorkerResourceOut",
        "DateIn": "_composer_48_DateIn",
        "DateOut": "_composer_49_DateOut",
        "CidrBlockIn": "_composer_50_CidrBlockIn",
        "CidrBlockOut": "_composer_51_CidrBlockOut",
        "EnvironmentIn": "_composer_52_EnvironmentIn",
        "EnvironmentOut": "_composer_53_EnvironmentOut",
        "CheckUpgradeResponseIn": "_composer_54_CheckUpgradeResponseIn",
        "CheckUpgradeResponseOut": "_composer_55_CheckUpgradeResponseOut",
        "OperationMetadataIn": "_composer_56_OperationMetadataIn",
        "OperationMetadataOut": "_composer_57_OperationMetadataOut",
        "LoadSnapshotRequestIn": "_composer_58_LoadSnapshotRequestIn",
        "LoadSnapshotRequestOut": "_composer_59_LoadSnapshotRequestOut",
        "PrivateEnvironmentConfigIn": "_composer_60_PrivateEnvironmentConfigIn",
        "PrivateEnvironmentConfigOut": "_composer_61_PrivateEnvironmentConfigOut",
        "ListEnvironmentsResponseIn": "_composer_62_ListEnvironmentsResponseIn",
        "ListEnvironmentsResponseOut": "_composer_63_ListEnvironmentsResponseOut",
        "NodeConfigIn": "_composer_64_NodeConfigIn",
        "NodeConfigOut": "_composer_65_NodeConfigOut",
        "ListImageVersionsResponseIn": "_composer_66_ListImageVersionsResponseIn",
        "ListImageVersionsResponseOut": "_composer_67_ListImageVersionsResponseOut",
        "OperationIn": "_composer_68_OperationIn",
        "OperationOut": "_composer_69_OperationOut",
        "WebServerNetworkAccessControlIn": "_composer_70_WebServerNetworkAccessControlIn",
        "WebServerNetworkAccessControlOut": "_composer_71_WebServerNetworkAccessControlOut",
        "WorkloadsConfigIn": "_composer_72_WorkloadsConfigIn",
        "WorkloadsConfigOut": "_composer_73_WorkloadsConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SoftwareConfigIn"] = t.struct(
        {
            "airflowConfigOverrides": t.struct({"_": t.string().optional()}).optional(),
            "imageVersion": t.string().optional(),
            "pythonVersion": t.string().optional(),
            "envVariables": t.struct({"_": t.string().optional()}).optional(),
            "pypiPackages": t.struct({"_": t.string().optional()}).optional(),
            "schedulerCount": t.integer().optional(),
        }
    ).named(renames["SoftwareConfigIn"])
    types["SoftwareConfigOut"] = t.struct(
        {
            "airflowConfigOverrides": t.struct({"_": t.string().optional()}).optional(),
            "imageVersion": t.string().optional(),
            "pythonVersion": t.string().optional(),
            "envVariables": t.struct({"_": t.string().optional()}).optional(),
            "pypiPackages": t.struct({"_": t.string().optional()}).optional(),
            "schedulerCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SoftwareConfigOut"])
    types["EnvironmentConfigIn"] = t.struct(
        {
            "dagGcsPrefix": t.string().optional(),
            "nodeCount": t.integer().optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowIn"]).optional(),
            "databaseConfig": t.proxy(renames["DatabaseConfigIn"]).optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigIn"]).optional(),
            "environmentSize": t.string().optional(),
            "nodeConfig": t.proxy(renames["NodeConfigIn"]).optional(),
            "webServerNetworkAccessControl": t.proxy(
                renames["WebServerNetworkAccessControlIn"]
            ).optional(),
            "masterAuthorizedNetworksConfig": t.proxy(
                renames["MasterAuthorizedNetworksConfigIn"]
            ).optional(),
            "gkeCluster": t.string().optional(),
            "softwareConfig": t.proxy(renames["SoftwareConfigIn"]).optional(),
            "webServerConfig": t.proxy(renames["WebServerConfigIn"]).optional(),
            "recoveryConfig": t.proxy(renames["RecoveryConfigIn"]).optional(),
            "workloadsConfig": t.proxy(renames["WorkloadsConfigIn"]).optional(),
            "airflowUri": t.string().optional(),
            "privateEnvironmentConfig": t.proxy(
                renames["PrivateEnvironmentConfigIn"]
            ).optional(),
        }
    ).named(renames["EnvironmentConfigIn"])
    types["EnvironmentConfigOut"] = t.struct(
        {
            "dagGcsPrefix": t.string().optional(),
            "airflowByoidUri": t.string().optional(),
            "nodeCount": t.integer().optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowOut"]).optional(),
            "databaseConfig": t.proxy(renames["DatabaseConfigOut"]).optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigOut"]).optional(),
            "environmentSize": t.string().optional(),
            "nodeConfig": t.proxy(renames["NodeConfigOut"]).optional(),
            "webServerNetworkAccessControl": t.proxy(
                renames["WebServerNetworkAccessControlOut"]
            ).optional(),
            "masterAuthorizedNetworksConfig": t.proxy(
                renames["MasterAuthorizedNetworksConfigOut"]
            ).optional(),
            "gkeCluster": t.string().optional(),
            "softwareConfig": t.proxy(renames["SoftwareConfigOut"]).optional(),
            "webServerConfig": t.proxy(renames["WebServerConfigOut"]).optional(),
            "recoveryConfig": t.proxy(renames["RecoveryConfigOut"]).optional(),
            "workloadsConfig": t.proxy(renames["WorkloadsConfigOut"]).optional(),
            "airflowUri": t.string().optional(),
            "privateEnvironmentConfig": t.proxy(
                renames["PrivateEnvironmentConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentConfigOut"])
    types["ImageVersionIn"] = t.struct(
        {
            "isDefault": t.boolean().optional(),
            "releaseDate": t.proxy(renames["DateIn"]).optional(),
            "creationDisabled": t.boolean().optional(),
            "upgradeDisabled": t.boolean().optional(),
            "imageVersionId": t.string().optional(),
            "supportedPythonVersions": t.array(t.string()).optional(),
        }
    ).named(renames["ImageVersionIn"])
    types["ImageVersionOut"] = t.struct(
        {
            "isDefault": t.boolean().optional(),
            "releaseDate": t.proxy(renames["DateOut"]).optional(),
            "creationDisabled": t.boolean().optional(),
            "upgradeDisabled": t.boolean().optional(),
            "imageVersionId": t.string().optional(),
            "supportedPythonVersions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageVersionOut"])
    types["IPAllocationPolicyIn"] = t.struct(
        {
            "clusterIpv4CidrBlock": t.string().optional(),
            "clusterSecondaryRangeName": t.string().optional(),
            "useIpAliases": t.boolean().optional(),
            "servicesIpv4CidrBlock": t.string().optional(),
            "servicesSecondaryRangeName": t.string().optional(),
        }
    ).named(renames["IPAllocationPolicyIn"])
    types["IPAllocationPolicyOut"] = t.struct(
        {
            "clusterIpv4CidrBlock": t.string().optional(),
            "clusterSecondaryRangeName": t.string().optional(),
            "useIpAliases": t.boolean().optional(),
            "servicesIpv4CidrBlock": t.string().optional(),
            "servicesSecondaryRangeName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IPAllocationPolicyOut"])
    types["SchedulerResourceIn"] = t.struct(
        {
            "cpu": t.number().optional(),
            "storageGb": t.number().optional(),
            "count": t.integer().optional(),
            "memoryGb": t.number().optional(),
        }
    ).named(renames["SchedulerResourceIn"])
    types["SchedulerResourceOut"] = t.struct(
        {
            "cpu": t.number().optional(),
            "storageGb": t.number().optional(),
            "count": t.integer().optional(),
            "memoryGb": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchedulerResourceOut"])
    types["PrivateClusterConfigIn"] = t.struct(
        {
            "masterIpv4CidrBlock": t.string().optional(),
            "enablePrivateEndpoint": t.boolean().optional(),
        }
    ).named(renames["PrivateClusterConfigIn"])
    types["PrivateClusterConfigOut"] = t.struct(
        {
            "masterIpv4CidrBlock": t.string().optional(),
            "enablePrivateEndpoint": t.boolean().optional(),
            "masterIpv4ReservedRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateClusterConfigOut"])
    types["SaveSnapshotResponseIn"] = t.struct(
        {"snapshotPath": t.string().optional()}
    ).named(renames["SaveSnapshotResponseIn"])
    types["SaveSnapshotResponseOut"] = t.struct(
        {
            "snapshotPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SaveSnapshotResponseOut"])
    types["WebServerResourceIn"] = t.struct(
        {
            "storageGb": t.number().optional(),
            "memoryGb": t.number().optional(),
            "cpu": t.number().optional(),
        }
    ).named(renames["WebServerResourceIn"])
    types["WebServerResourceOut"] = t.struct(
        {
            "storageGb": t.number().optional(),
            "memoryGb": t.number().optional(),
            "cpu": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebServerResourceOut"])
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
    types["EncryptionConfigIn"] = t.struct({"kmsKeyName": t.string().optional()}).named(
        renames["EncryptionConfigIn"]
    )
    types["EncryptionConfigOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionConfigOut"])
    types["MaintenanceWindowIn"] = t.struct(
        {"recurrence": t.string(), "endTime": t.string(), "startTime": t.string()}
    ).named(renames["MaintenanceWindowIn"])
    types["MaintenanceWindowOut"] = t.struct(
        {
            "recurrence": t.string(),
            "endTime": t.string(),
            "startTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceWindowOut"])
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
    types["WebServerConfigIn"] = t.struct({"machineType": t.string().optional()}).named(
        renames["WebServerConfigIn"]
    )
    types["WebServerConfigOut"] = t.struct(
        {
            "machineType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebServerConfigOut"])
    types["ScheduledSnapshotsConfigIn"] = t.struct(
        {
            "snapshotLocation": t.string().optional(),
            "snapshotCreationSchedule": t.string().optional(),
            "enabled": t.boolean().optional(),
            "timeZone": t.string().optional(),
        }
    ).named(renames["ScheduledSnapshotsConfigIn"])
    types["ScheduledSnapshotsConfigOut"] = t.struct(
        {
            "snapshotLocation": t.string().optional(),
            "snapshotCreationSchedule": t.string().optional(),
            "enabled": t.boolean().optional(),
            "timeZone": t.string().optional(),
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
    types["LoadSnapshotResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LoadSnapshotResponseIn"]
    )
    types["LoadSnapshotResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LoadSnapshotResponseOut"])
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
    types["DatabaseConfigIn"] = t.struct({"machineType": t.string().optional()}).named(
        renames["DatabaseConfigIn"]
    )
    types["DatabaseConfigOut"] = t.struct(
        {
            "machineType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseConfigOut"])
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
    types["MasterAuthorizedNetworksConfigIn"] = t.struct(
        {
            "cidrBlocks": t.array(t.proxy(renames["CidrBlockIn"])).optional(),
            "enabled": t.boolean().optional(),
        }
    ).named(renames["MasterAuthorizedNetworksConfigIn"])
    types["MasterAuthorizedNetworksConfigOut"] = t.struct(
        {
            "cidrBlocks": t.array(t.proxy(renames["CidrBlockOut"])).optional(),
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MasterAuthorizedNetworksConfigOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["WorkerResourceIn"] = t.struct(
        {
            "memoryGb": t.number().optional(),
            "cpu": t.number().optional(),
            "maxCount": t.integer().optional(),
            "storageGb": t.number().optional(),
            "minCount": t.integer().optional(),
        }
    ).named(renames["WorkerResourceIn"])
    types["WorkerResourceOut"] = t.struct(
        {
            "memoryGb": t.number().optional(),
            "cpu": t.number().optional(),
            "maxCount": t.integer().optional(),
            "storageGb": t.number().optional(),
            "minCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerResourceOut"])
    types["DateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["CidrBlockIn"] = t.struct(
        {"cidrBlock": t.string().optional(), "displayName": t.string().optional()}
    ).named(renames["CidrBlockIn"])
    types["CidrBlockOut"] = t.struct(
        {
            "cidrBlock": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CidrBlockOut"])
    types["EnvironmentIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "uuid": t.string().optional(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
        }
    ).named(renames["EnvironmentIn"])
    types["EnvironmentOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "uuid": t.string().optional(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "config": t.proxy(renames["EnvironmentConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentOut"])
    types["CheckUpgradeResponseIn"] = t.struct(
        {
            "pypiDependencies": t.struct({"_": t.string().optional()}).optional(),
            "imageVersion": t.string().optional(),
        }
    ).named(renames["CheckUpgradeResponseIn"])
    types["CheckUpgradeResponseOut"] = t.struct(
        {
            "pypiDependencies": t.struct({"_": t.string().optional()}).optional(),
            "pypiConflictBuildLogExtract": t.string().optional(),
            "imageVersion": t.string().optional(),
            "containsPypiModulesConflict": t.string().optional(),
            "buildLogUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckUpgradeResponseOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "resourceUuid": t.string().optional(),
            "state": t.string().optional(),
            "resource": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "operationType": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "resourceUuid": t.string().optional(),
            "state": t.string().optional(),
            "resource": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "operationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["LoadSnapshotRequestIn"] = t.struct(
        {
            "skipAirflowOverridesSetting": t.boolean().optional(),
            "skipEnvironmentVariablesSetting": t.boolean().optional(),
            "skipGcsDataCopying": t.boolean().optional(),
            "snapshotPath": t.string().optional(),
            "skipPypiPackagesInstallation": t.boolean().optional(),
        }
    ).named(renames["LoadSnapshotRequestIn"])
    types["LoadSnapshotRequestOut"] = t.struct(
        {
            "skipAirflowOverridesSetting": t.boolean().optional(),
            "skipEnvironmentVariablesSetting": t.boolean().optional(),
            "skipGcsDataCopying": t.boolean().optional(),
            "snapshotPath": t.string().optional(),
            "skipPypiPackagesInstallation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoadSnapshotRequestOut"])
    types["PrivateEnvironmentConfigIn"] = t.struct(
        {
            "cloudComposerNetworkIpv4CidrBlock": t.string().optional(),
            "networkingConfig": t.proxy(renames["NetworkingConfigIn"]).optional(),
            "cloudSqlIpv4CidrBlock": t.string().optional(),
            "privateClusterConfig": t.proxy(
                renames["PrivateClusterConfigIn"]
            ).optional(),
            "webServerIpv4CidrBlock": t.string().optional(),
            "cloudComposerConnectionSubnetwork": t.string().optional(),
            "enablePrivateEnvironment": t.boolean().optional(),
            "enablePrivatelyUsedPublicIps": t.boolean().optional(),
        }
    ).named(renames["PrivateEnvironmentConfigIn"])
    types["PrivateEnvironmentConfigOut"] = t.struct(
        {
            "cloudComposerNetworkIpv4ReservedRange": t.string().optional(),
            "webServerIpv4ReservedRange": t.string().optional(),
            "cloudComposerNetworkIpv4CidrBlock": t.string().optional(),
            "networkingConfig": t.proxy(renames["NetworkingConfigOut"]).optional(),
            "cloudSqlIpv4CidrBlock": t.string().optional(),
            "privateClusterConfig": t.proxy(
                renames["PrivateClusterConfigOut"]
            ).optional(),
            "webServerIpv4CidrBlock": t.string().optional(),
            "cloudComposerConnectionSubnetwork": t.string().optional(),
            "enablePrivateEnvironment": t.boolean().optional(),
            "enablePrivatelyUsedPublicIps": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateEnvironmentConfigOut"])
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
    types["NodeConfigIn"] = t.struct(
        {
            "diskSizeGb": t.integer().optional(),
            "location": t.string().optional(),
            "ipAllocationPolicy": t.proxy(renames["IPAllocationPolicyIn"]).optional(),
            "network": t.string().optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "tags": t.array(t.string()).optional(),
            "subnetwork": t.string().optional(),
            "machineType": t.string().optional(),
            "enableIpMasqAgent": t.boolean().optional(),
            "serviceAccount": t.string().optional(),
        }
    ).named(renames["NodeConfigIn"])
    types["NodeConfigOut"] = t.struct(
        {
            "diskSizeGb": t.integer().optional(),
            "location": t.string().optional(),
            "ipAllocationPolicy": t.proxy(renames["IPAllocationPolicyOut"]).optional(),
            "network": t.string().optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "tags": t.array(t.string()).optional(),
            "subnetwork": t.string().optional(),
            "machineType": t.string().optional(),
            "enableIpMasqAgent": t.boolean().optional(),
            "serviceAccount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeConfigOut"])
    types["ListImageVersionsResponseIn"] = t.struct(
        {
            "imageVersions": t.array(t.proxy(renames["ImageVersionIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListImageVersionsResponseIn"])
    types["ListImageVersionsResponseOut"] = t.struct(
        {
            "imageVersions": t.array(t.proxy(renames["ImageVersionOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListImageVersionsResponseOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
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

    functions = {}
    functions["projectsLocationsImageVersionsList"] = composer.get(
        "v1/{parent}/imageVersions",
        t.struct(
            {
                "includePastReleases": t.boolean().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListImageVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = composer.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = composer.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = composer.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsList"] = composer.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "createTime": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "uuid": t.string().optional(),
                "state": t.string().optional(),
                "updateTime": t.string().optional(),
                "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
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
                "updateMask": t.string(),
                "name": t.string().optional(),
                "createTime": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "uuid": t.string().optional(),
                "state": t.string().optional(),
                "updateTime": t.string().optional(),
                "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
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
                "updateMask": t.string(),
                "name": t.string().optional(),
                "createTime": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "uuid": t.string().optional(),
                "state": t.string().optional(),
                "updateTime": t.string().optional(),
                "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsDelete"] = composer.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "createTime": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "uuid": t.string().optional(),
                "state": t.string().optional(),
                "updateTime": t.string().optional(),
                "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
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
                "updateMask": t.string(),
                "name": t.string().optional(),
                "createTime": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "uuid": t.string().optional(),
                "state": t.string().optional(),
                "updateTime": t.string().optional(),
                "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
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
                "updateMask": t.string(),
                "name": t.string().optional(),
                "createTime": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "uuid": t.string().optional(),
                "state": t.string().optional(),
                "updateTime": t.string().optional(),
                "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
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
                "updateMask": t.string(),
                "name": t.string().optional(),
                "createTime": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "uuid": t.string().optional(),
                "state": t.string().optional(),
                "updateTime": t.string().optional(),
                "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="composer", renames=renames, types=Box(types), functions=Box(functions)
    )
