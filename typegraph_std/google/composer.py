from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_composer() -> Import:
    composer = HTTPRuntime("https://composer.googleapis.com/")

    renames = {
        "ErrorResponse": "_composer_1_ErrorResponse",
        "WebServerResourceIn": "_composer_2_WebServerResourceIn",
        "WebServerResourceOut": "_composer_3_WebServerResourceOut",
        "OperationMetadataIn": "_composer_4_OperationMetadataIn",
        "OperationMetadataOut": "_composer_5_OperationMetadataOut",
        "LoadSnapshotRequestIn": "_composer_6_LoadSnapshotRequestIn",
        "LoadSnapshotRequestOut": "_composer_7_LoadSnapshotRequestOut",
        "NodeConfigIn": "_composer_8_NodeConfigIn",
        "NodeConfigOut": "_composer_9_NodeConfigOut",
        "PrivateEnvironmentConfigIn": "_composer_10_PrivateEnvironmentConfigIn",
        "PrivateEnvironmentConfigOut": "_composer_11_PrivateEnvironmentConfigOut",
        "CheckUpgradeResponseIn": "_composer_12_CheckUpgradeResponseIn",
        "CheckUpgradeResponseOut": "_composer_13_CheckUpgradeResponseOut",
        "SaveSnapshotResponseIn": "_composer_14_SaveSnapshotResponseIn",
        "SaveSnapshotResponseOut": "_composer_15_SaveSnapshotResponseOut",
        "SoftwareConfigIn": "_composer_16_SoftwareConfigIn",
        "SoftwareConfigOut": "_composer_17_SoftwareConfigOut",
        "LoadSnapshotResponseIn": "_composer_18_LoadSnapshotResponseIn",
        "LoadSnapshotResponseOut": "_composer_19_LoadSnapshotResponseOut",
        "EnvironmentConfigIn": "_composer_20_EnvironmentConfigIn",
        "EnvironmentConfigOut": "_composer_21_EnvironmentConfigOut",
        "WebServerConfigIn": "_composer_22_WebServerConfigIn",
        "WebServerConfigOut": "_composer_23_WebServerConfigOut",
        "ListEnvironmentsResponseIn": "_composer_24_ListEnvironmentsResponseIn",
        "ListEnvironmentsResponseOut": "_composer_25_ListEnvironmentsResponseOut",
        "WorkloadsConfigIn": "_composer_26_WorkloadsConfigIn",
        "WorkloadsConfigOut": "_composer_27_WorkloadsConfigOut",
        "StatusIn": "_composer_28_StatusIn",
        "StatusOut": "_composer_29_StatusOut",
        "DatabaseConfigIn": "_composer_30_DatabaseConfigIn",
        "DatabaseConfigOut": "_composer_31_DatabaseConfigOut",
        "CidrBlockIn": "_composer_32_CidrBlockIn",
        "CidrBlockOut": "_composer_33_CidrBlockOut",
        "AllowedIpRangeIn": "_composer_34_AllowedIpRangeIn",
        "AllowedIpRangeOut": "_composer_35_AllowedIpRangeOut",
        "ListOperationsResponseIn": "_composer_36_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_composer_37_ListOperationsResponseOut",
        "MasterAuthorizedNetworksConfigIn": "_composer_38_MasterAuthorizedNetworksConfigIn",
        "MasterAuthorizedNetworksConfigOut": "_composer_39_MasterAuthorizedNetworksConfigOut",
        "WorkerResourceIn": "_composer_40_WorkerResourceIn",
        "WorkerResourceOut": "_composer_41_WorkerResourceOut",
        "ListImageVersionsResponseIn": "_composer_42_ListImageVersionsResponseIn",
        "ListImageVersionsResponseOut": "_composer_43_ListImageVersionsResponseOut",
        "RecoveryConfigIn": "_composer_44_RecoveryConfigIn",
        "RecoveryConfigOut": "_composer_45_RecoveryConfigOut",
        "DateIn": "_composer_46_DateIn",
        "DateOut": "_composer_47_DateOut",
        "EncryptionConfigIn": "_composer_48_EncryptionConfigIn",
        "EncryptionConfigOut": "_composer_49_EncryptionConfigOut",
        "MaintenanceWindowIn": "_composer_50_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_composer_51_MaintenanceWindowOut",
        "NetworkingConfigIn": "_composer_52_NetworkingConfigIn",
        "NetworkingConfigOut": "_composer_53_NetworkingConfigOut",
        "IPAllocationPolicyIn": "_composer_54_IPAllocationPolicyIn",
        "IPAllocationPolicyOut": "_composer_55_IPAllocationPolicyOut",
        "EnvironmentIn": "_composer_56_EnvironmentIn",
        "EnvironmentOut": "_composer_57_EnvironmentOut",
        "WebServerNetworkAccessControlIn": "_composer_58_WebServerNetworkAccessControlIn",
        "WebServerNetworkAccessControlOut": "_composer_59_WebServerNetworkAccessControlOut",
        "SaveSnapshotRequestIn": "_composer_60_SaveSnapshotRequestIn",
        "SaveSnapshotRequestOut": "_composer_61_SaveSnapshotRequestOut",
        "OperationIn": "_composer_62_OperationIn",
        "OperationOut": "_composer_63_OperationOut",
        "ScheduledSnapshotsConfigIn": "_composer_64_ScheduledSnapshotsConfigIn",
        "ScheduledSnapshotsConfigOut": "_composer_65_ScheduledSnapshotsConfigOut",
        "SchedulerResourceIn": "_composer_66_SchedulerResourceIn",
        "SchedulerResourceOut": "_composer_67_SchedulerResourceOut",
        "PrivateClusterConfigIn": "_composer_68_PrivateClusterConfigIn",
        "PrivateClusterConfigOut": "_composer_69_PrivateClusterConfigOut",
        "EmptyIn": "_composer_70_EmptyIn",
        "EmptyOut": "_composer_71_EmptyOut",
        "ImageVersionIn": "_composer_72_ImageVersionIn",
        "ImageVersionOut": "_composer_73_ImageVersionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["WebServerResourceIn"] = t.struct(
        {
            "cpu": t.number().optional(),
            "memoryGb": t.number().optional(),
            "storageGb": t.number().optional(),
        }
    ).named(renames["WebServerResourceIn"])
    types["WebServerResourceOut"] = t.struct(
        {
            "cpu": t.number().optional(),
            "memoryGb": t.number().optional(),
            "storageGb": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebServerResourceOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "resourceUuid": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "resource": t.string().optional(),
            "state": t.string().optional(),
            "operationType": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "resourceUuid": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "resource": t.string().optional(),
            "state": t.string().optional(),
            "operationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["LoadSnapshotRequestIn"] = t.struct(
        {
            "skipPypiPackagesInstallation": t.boolean().optional(),
            "skipGcsDataCopying": t.boolean().optional(),
            "skipAirflowOverridesSetting": t.boolean().optional(),
            "snapshotPath": t.string().optional(),
            "skipEnvironmentVariablesSetting": t.boolean().optional(),
        }
    ).named(renames["LoadSnapshotRequestIn"])
    types["LoadSnapshotRequestOut"] = t.struct(
        {
            "skipPypiPackagesInstallation": t.boolean().optional(),
            "skipGcsDataCopying": t.boolean().optional(),
            "skipAirflowOverridesSetting": t.boolean().optional(),
            "snapshotPath": t.string().optional(),
            "skipEnvironmentVariablesSetting": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoadSnapshotRequestOut"])
    types["NodeConfigIn"] = t.struct(
        {
            "location": t.string().optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "subnetwork": t.string().optional(),
            "diskSizeGb": t.integer().optional(),
            "ipAllocationPolicy": t.proxy(renames["IPAllocationPolicyIn"]).optional(),
            "machineType": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "network": t.string().optional(),
            "enableIpMasqAgent": t.boolean().optional(),
            "serviceAccount": t.string().optional(),
        }
    ).named(renames["NodeConfigIn"])
    types["NodeConfigOut"] = t.struct(
        {
            "location": t.string().optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "subnetwork": t.string().optional(),
            "diskSizeGb": t.integer().optional(),
            "ipAllocationPolicy": t.proxy(renames["IPAllocationPolicyOut"]).optional(),
            "machineType": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "network": t.string().optional(),
            "enableIpMasqAgent": t.boolean().optional(),
            "serviceAccount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeConfigOut"])
    types["PrivateEnvironmentConfigIn"] = t.struct(
        {
            "cloudComposerConnectionSubnetwork": t.string().optional(),
            "cloudComposerNetworkIpv4CidrBlock": t.string().optional(),
            "privateClusterConfig": t.proxy(
                renames["PrivateClusterConfigIn"]
            ).optional(),
            "webServerIpv4CidrBlock": t.string().optional(),
            "enablePrivatelyUsedPublicIps": t.boolean().optional(),
            "enablePrivateEnvironment": t.boolean().optional(),
            "cloudSqlIpv4CidrBlock": t.string().optional(),
            "networkingConfig": t.proxy(renames["NetworkingConfigIn"]).optional(),
        }
    ).named(renames["PrivateEnvironmentConfigIn"])
    types["PrivateEnvironmentConfigOut"] = t.struct(
        {
            "cloudComposerConnectionSubnetwork": t.string().optional(),
            "cloudComposerNetworkIpv4ReservedRange": t.string().optional(),
            "cloudComposerNetworkIpv4CidrBlock": t.string().optional(),
            "privateClusterConfig": t.proxy(
                renames["PrivateClusterConfigOut"]
            ).optional(),
            "webServerIpv4CidrBlock": t.string().optional(),
            "enablePrivatelyUsedPublicIps": t.boolean().optional(),
            "enablePrivateEnvironment": t.boolean().optional(),
            "cloudSqlIpv4CidrBlock": t.string().optional(),
            "webServerIpv4ReservedRange": t.string().optional(),
            "networkingConfig": t.proxy(renames["NetworkingConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateEnvironmentConfigOut"])
    types["CheckUpgradeResponseIn"] = t.struct(
        {
            "imageVersion": t.string().optional(),
            "pypiDependencies": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["CheckUpgradeResponseIn"])
    types["CheckUpgradeResponseOut"] = t.struct(
        {
            "imageVersion": t.string().optional(),
            "pypiConflictBuildLogExtract": t.string().optional(),
            "containsPypiModulesConflict": t.string().optional(),
            "pypiDependencies": t.struct({"_": t.string().optional()}).optional(),
            "buildLogUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckUpgradeResponseOut"])
    types["SaveSnapshotResponseIn"] = t.struct(
        {"snapshotPath": t.string().optional()}
    ).named(renames["SaveSnapshotResponseIn"])
    types["SaveSnapshotResponseOut"] = t.struct(
        {
            "snapshotPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SaveSnapshotResponseOut"])
    types["SoftwareConfigIn"] = t.struct(
        {
            "airflowConfigOverrides": t.struct({"_": t.string().optional()}).optional(),
            "pythonVersion": t.string().optional(),
            "schedulerCount": t.integer().optional(),
            "pypiPackages": t.struct({"_": t.string().optional()}).optional(),
            "imageVersion": t.string().optional(),
            "envVariables": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SoftwareConfigIn"])
    types["SoftwareConfigOut"] = t.struct(
        {
            "airflowConfigOverrides": t.struct({"_": t.string().optional()}).optional(),
            "pythonVersion": t.string().optional(),
            "schedulerCount": t.integer().optional(),
            "pypiPackages": t.struct({"_": t.string().optional()}).optional(),
            "imageVersion": t.string().optional(),
            "envVariables": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SoftwareConfigOut"])
    types["LoadSnapshotResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LoadSnapshotResponseIn"]
    )
    types["LoadSnapshotResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LoadSnapshotResponseOut"])
    types["EnvironmentConfigIn"] = t.struct(
        {
            "nodeCount": t.integer().optional(),
            "masterAuthorizedNetworksConfig": t.proxy(
                renames["MasterAuthorizedNetworksConfigIn"]
            ).optional(),
            "softwareConfig": t.proxy(renames["SoftwareConfigIn"]).optional(),
            "dagGcsPrefix": t.string().optional(),
            "webServerConfig": t.proxy(renames["WebServerConfigIn"]).optional(),
            "databaseConfig": t.proxy(renames["DatabaseConfigIn"]).optional(),
            "webServerNetworkAccessControl": t.proxy(
                renames["WebServerNetworkAccessControlIn"]
            ).optional(),
            "privateEnvironmentConfig": t.proxy(
                renames["PrivateEnvironmentConfigIn"]
            ).optional(),
            "recoveryConfig": t.proxy(renames["RecoveryConfigIn"]).optional(),
            "workloadsConfig": t.proxy(renames["WorkloadsConfigIn"]).optional(),
            "gkeCluster": t.string().optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowIn"]).optional(),
            "nodeConfig": t.proxy(renames["NodeConfigIn"]).optional(),
            "airflowUri": t.string().optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigIn"]).optional(),
            "environmentSize": t.string().optional(),
        }
    ).named(renames["EnvironmentConfigIn"])
    types["EnvironmentConfigOut"] = t.struct(
        {
            "nodeCount": t.integer().optional(),
            "masterAuthorizedNetworksConfig": t.proxy(
                renames["MasterAuthorizedNetworksConfigOut"]
            ).optional(),
            "softwareConfig": t.proxy(renames["SoftwareConfigOut"]).optional(),
            "dagGcsPrefix": t.string().optional(),
            "webServerConfig": t.proxy(renames["WebServerConfigOut"]).optional(),
            "databaseConfig": t.proxy(renames["DatabaseConfigOut"]).optional(),
            "webServerNetworkAccessControl": t.proxy(
                renames["WebServerNetworkAccessControlOut"]
            ).optional(),
            "privateEnvironmentConfig": t.proxy(
                renames["PrivateEnvironmentConfigOut"]
            ).optional(),
            "airflowByoidUri": t.string().optional(),
            "recoveryConfig": t.proxy(renames["RecoveryConfigOut"]).optional(),
            "workloadsConfig": t.proxy(renames["WorkloadsConfigOut"]).optional(),
            "gkeCluster": t.string().optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowOut"]).optional(),
            "nodeConfig": t.proxy(renames["NodeConfigOut"]).optional(),
            "airflowUri": t.string().optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigOut"]).optional(),
            "environmentSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentConfigOut"])
    types["WebServerConfigIn"] = t.struct({"machineType": t.string().optional()}).named(
        renames["WebServerConfigIn"]
    )
    types["WebServerConfigOut"] = t.struct(
        {
            "machineType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebServerConfigOut"])
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
    types["WorkloadsConfigIn"] = t.struct(
        {
            "webServer": t.proxy(renames["WebServerResourceIn"]).optional(),
            "scheduler": t.proxy(renames["SchedulerResourceIn"]).optional(),
            "worker": t.proxy(renames["WorkerResourceIn"]).optional(),
        }
    ).named(renames["WorkloadsConfigIn"])
    types["WorkloadsConfigOut"] = t.struct(
        {
            "webServer": t.proxy(renames["WebServerResourceOut"]).optional(),
            "scheduler": t.proxy(renames["SchedulerResourceOut"]).optional(),
            "worker": t.proxy(renames["WorkerResourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkloadsConfigOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
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
    types["WorkerResourceIn"] = t.struct(
        {
            "maxCount": t.integer().optional(),
            "storageGb": t.number().optional(),
            "memoryGb": t.number().optional(),
            "minCount": t.integer().optional(),
            "cpu": t.number().optional(),
        }
    ).named(renames["WorkerResourceIn"])
    types["WorkerResourceOut"] = t.struct(
        {
            "maxCount": t.integer().optional(),
            "storageGb": t.number().optional(),
            "memoryGb": t.number().optional(),
            "minCount": t.integer().optional(),
            "cpu": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkerResourceOut"])
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
    types["NetworkingConfigIn"] = t.struct(
        {"connectionType": t.string().optional()}
    ).named(renames["NetworkingConfigIn"])
    types["NetworkingConfigOut"] = t.struct(
        {
            "connectionType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkingConfigOut"])
    types["IPAllocationPolicyIn"] = t.struct(
        {
            "useIpAliases": t.boolean().optional(),
            "clusterIpv4CidrBlock": t.string().optional(),
            "servicesSecondaryRangeName": t.string().optional(),
            "servicesIpv4CidrBlock": t.string().optional(),
            "clusterSecondaryRangeName": t.string().optional(),
        }
    ).named(renames["IPAllocationPolicyIn"])
    types["IPAllocationPolicyOut"] = t.struct(
        {
            "useIpAliases": t.boolean().optional(),
            "clusterIpv4CidrBlock": t.string().optional(),
            "servicesSecondaryRangeName": t.string().optional(),
            "servicesIpv4CidrBlock": t.string().optional(),
            "clusterSecondaryRangeName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IPAllocationPolicyOut"])
    types["EnvironmentIn"] = t.struct(
        {
            "state": t.string().optional(),
            "uuid": t.string().optional(),
            "config": t.proxy(renames["EnvironmentConfigIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["EnvironmentIn"])
    types["EnvironmentOut"] = t.struct(
        {
            "state": t.string().optional(),
            "uuid": t.string().optional(),
            "config": t.proxy(renames["EnvironmentConfigOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentOut"])
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
    types["SaveSnapshotRequestIn"] = t.struct(
        {"snapshotLocation": t.string().optional()}
    ).named(renames["SaveSnapshotRequestIn"])
    types["SaveSnapshotRequestOut"] = t.struct(
        {
            "snapshotLocation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SaveSnapshotRequestOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["ScheduledSnapshotsConfigIn"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "snapshotLocation": t.string().optional(),
            "timeZone": t.string().optional(),
            "snapshotCreationSchedule": t.string().optional(),
        }
    ).named(renames["ScheduledSnapshotsConfigIn"])
    types["ScheduledSnapshotsConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "snapshotLocation": t.string().optional(),
            "timeZone": t.string().optional(),
            "snapshotCreationSchedule": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduledSnapshotsConfigOut"])
    types["SchedulerResourceIn"] = t.struct(
        {
            "memoryGb": t.number().optional(),
            "storageGb": t.number().optional(),
            "cpu": t.number().optional(),
            "count": t.integer().optional(),
        }
    ).named(renames["SchedulerResourceIn"])
    types["SchedulerResourceOut"] = t.struct(
        {
            "memoryGb": t.number().optional(),
            "storageGb": t.number().optional(),
            "cpu": t.number().optional(),
            "count": t.integer().optional(),
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
            "masterIpv4ReservedRange": t.string().optional(),
            "masterIpv4CidrBlock": t.string().optional(),
            "enablePrivateEndpoint": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateClusterConfigOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ImageVersionIn"] = t.struct(
        {
            "releaseDate": t.proxy(renames["DateIn"]).optional(),
            "isDefault": t.boolean().optional(),
            "imageVersionId": t.string().optional(),
            "creationDisabled": t.boolean().optional(),
            "supportedPythonVersions": t.array(t.string()).optional(),
            "upgradeDisabled": t.boolean().optional(),
        }
    ).named(renames["ImageVersionIn"])
    types["ImageVersionOut"] = t.struct(
        {
            "releaseDate": t.proxy(renames["DateOut"]).optional(),
            "isDefault": t.boolean().optional(),
            "imageVersionId": t.string().optional(),
            "creationDisabled": t.boolean().optional(),
            "supportedPythonVersions": t.array(t.string()).optional(),
            "upgradeDisabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageVersionOut"])

    functions = {}
    functions["projectsLocationsOperationsDelete"] = composer.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = composer.get(
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
    functions["projectsLocationsImageVersionsList"] = composer.get(
        "v1/{parent}/imageVersions",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "includePastReleases": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListImageVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsCreate"] = composer.get(
        "v1/{parent}/environments",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEnvironmentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsPatch"] = composer.get(
        "v1/{parent}/environments",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEnvironmentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsSaveSnapshot"] = composer.get(
        "v1/{parent}/environments",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEnvironmentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsLoadSnapshot"] = composer.get(
        "v1/{parent}/environments",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEnvironmentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsGet"] = composer.get(
        "v1/{parent}/environments",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEnvironmentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsDelete"] = composer.get(
        "v1/{parent}/environments",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEnvironmentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnvironmentsList"] = composer.get(
        "v1/{parent}/environments",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEnvironmentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="composer", renames=renames, types=types, functions=functions
    )
