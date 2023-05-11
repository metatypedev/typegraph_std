from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_file() -> Import:
    file = HTTPRuntime("https://file.googleapis.com/")

    renames = {
        "ErrorResponse": "_file_1_ErrorResponse",
        "DateIn": "_file_2_DateIn",
        "DateOut": "_file_3_DateOut",
        "StatusIn": "_file_4_StatusIn",
        "StatusOut": "_file_5_StatusOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn": "_file_6_GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut": "_file_7_GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut",
        "WeeklyCycleIn": "_file_8_WeeklyCycleIn",
        "WeeklyCycleOut": "_file_9_WeeklyCycleOut",
        "BackupIn": "_file_10_BackupIn",
        "BackupOut": "_file_11_BackupOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn": "_file_12_GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut": "_file_13_GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut",
        "OperationIn": "_file_14_OperationIn",
        "OperationOut": "_file_15_OperationOut",
        "UpdatePolicyIn": "_file_16_UpdatePolicyIn",
        "UpdatePolicyOut": "_file_17_UpdatePolicyOut",
        "EmptyIn": "_file_18_EmptyIn",
        "EmptyOut": "_file_19_EmptyOut",
        "ListOperationsResponseIn": "_file_20_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_file_21_ListOperationsResponseOut",
        "ListBackupsResponseIn": "_file_22_ListBackupsResponseIn",
        "ListBackupsResponseOut": "_file_23_ListBackupsResponseOut",
        "DenyMaintenancePeriodIn": "_file_24_DenyMaintenancePeriodIn",
        "DenyMaintenancePeriodOut": "_file_25_DenyMaintenancePeriodOut",
        "ListLocationsResponseIn": "_file_26_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_file_27_ListLocationsResponseOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn": "_file_28_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut": "_file_29_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut",
        "NfsExportOptionsIn": "_file_30_NfsExportOptionsIn",
        "NfsExportOptionsOut": "_file_31_NfsExportOptionsOut",
        "LocationIn": "_file_32_LocationIn",
        "LocationOut": "_file_33_LocationOut",
        "SnapshotIn": "_file_34_SnapshotIn",
        "SnapshotOut": "_file_35_SnapshotOut",
        "RestoreInstanceRequestIn": "_file_36_RestoreInstanceRequestIn",
        "RestoreInstanceRequestOut": "_file_37_RestoreInstanceRequestOut",
        "DailyCycleIn": "_file_38_DailyCycleIn",
        "DailyCycleOut": "_file_39_DailyCycleOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn": "_file_40_GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut": "_file_41_GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut",
        "ListInstancesResponseIn": "_file_42_ListInstancesResponseIn",
        "ListInstancesResponseOut": "_file_43_ListInstancesResponseOut",
        "InstanceIn": "_file_44_InstanceIn",
        "InstanceOut": "_file_45_InstanceOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn": "_file_46_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut": "_file_47_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn": "_file_48_GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut": "_file_49_GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut",
        "RevertInstanceRequestIn": "_file_50_RevertInstanceRequestIn",
        "RevertInstanceRequestOut": "_file_51_RevertInstanceRequestOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn": "_file_52_GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut": "_file_53_GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut",
        "MaintenanceWindowIn": "_file_54_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_file_55_MaintenanceWindowOut",
        "NetworkConfigIn": "_file_56_NetworkConfigIn",
        "NetworkConfigOut": "_file_57_NetworkConfigOut",
        "MaintenancePolicyIn": "_file_58_MaintenancePolicyIn",
        "MaintenancePolicyOut": "_file_59_MaintenancePolicyOut",
        "ListSnapshotsResponseIn": "_file_60_ListSnapshotsResponseIn",
        "ListSnapshotsResponseOut": "_file_61_ListSnapshotsResponseOut",
        "CancelOperationRequestIn": "_file_62_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_file_63_CancelOperationRequestOut",
        "OperationMetadataIn": "_file_64_OperationMetadataIn",
        "OperationMetadataOut": "_file_65_OperationMetadataOut",
        "TimeOfDayIn": "_file_66_TimeOfDayIn",
        "TimeOfDayOut": "_file_67_TimeOfDayOut",
        "ScheduleIn": "_file_68_ScheduleIn",
        "ScheduleOut": "_file_69_ScheduleOut",
        "FileShareConfigIn": "_file_70_FileShareConfigIn",
        "FileShareConfigOut": "_file_71_FileShareConfigOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn": "_file_72_GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut": "_file_73_GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn": "_file_74_GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut": "_file_75_GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["DateIn"] = t.struct(
        {
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn"] = t.struct(
        {
            "instanceType": t.string().optional(),
            "maintenanceSettings": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn"
                ]
            ).optional(),
            "maintenanceSchedules": t.struct({"_": t.string().optional()}).optional(),
            "maintenancePolicyNames": t.struct({"_": t.string().optional()}).optional(),
            "softwareVersions": t.struct({"_": t.string().optional()}).optional(),
            "consumerDefinedName": t.string().optional(),
            "name": t.string().optional(),
            "slmInstanceTemplate": t.string().optional(),
            "notificationParameters": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "instanceType": t.string().optional(),
            "state": t.string().optional(),
            "provisionedResources": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut"
                    ]
                )
            ).optional(),
            "tenantProjectId": t.string().optional(),
            "maintenanceSettings": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut"
                ]
            ).optional(),
            "createTime": t.string().optional(),
            "maintenanceSchedules": t.struct({"_": t.string().optional()}).optional(),
            "maintenancePolicyNames": t.struct({"_": t.string().optional()}).optional(),
            "sloMetadata": t.proxy(
                renames["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut"]
            ).optional(),
            "softwareVersions": t.struct({"_": t.string().optional()}).optional(),
            "consumerDefinedName": t.string().optional(),
            "name": t.string().optional(),
            "slmInstanceTemplate": t.string().optional(),
            "notificationParameters": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "producerMetadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut"])
    types["WeeklyCycleIn"] = t.struct(
        {"schedule": t.array(t.proxy(renames["ScheduleIn"])).optional()}
    ).named(renames["WeeklyCycleIn"])
    types["WeeklyCycleOut"] = t.struct(
        {
            "schedule": t.array(t.proxy(renames["ScheduleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WeeklyCycleOut"])
    types["BackupIn"] = t.struct(
        {
            "sourceFileShare": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "kmsKey": t.string().optional(),
            "sourceInstance": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["BackupIn"])
    types["BackupOut"] = t.struct(
        {
            "state": t.string().optional(),
            "storageBytes": t.string().optional(),
            "sourceFileShare": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "satisfiesPzs": t.boolean().optional(),
            "createTime": t.string().optional(),
            "sourceInstanceTier": t.string().optional(),
            "kmsKey": t.string().optional(),
            "downloadBytes": t.string().optional(),
            "sourceInstance": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "capacityGb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupOut"])
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn"
    ] = t.struct(
        {"resourceUrl": t.string().optional(), "resourceType": t.string().optional()}
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut"
    ] = t.struct(
        {
            "resourceUrl": t.string().optional(),
            "resourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut"]
    )
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["UpdatePolicyIn"] = t.struct(
        {
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodIn"])
            ).optional(),
            "window": t.proxy(renames["MaintenanceWindowIn"]).optional(),
            "channel": t.string().optional(),
        }
    ).named(renames["UpdatePolicyIn"])
    types["UpdatePolicyOut"] = t.struct(
        {
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodOut"])
            ).optional(),
            "window": t.proxy(renames["MaintenanceWindowOut"]).optional(),
            "channel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdatePolicyOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["ListBackupsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "backups": t.array(t.proxy(renames["BackupIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListBackupsResponseIn"])
    types["ListBackupsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "backups": t.array(t.proxy(renames["BackupOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBackupsResponseOut"])
    types["DenyMaintenancePeriodIn"] = t.struct(
        {
            "endDate": t.proxy(renames["DateIn"]).optional(),
            "time": t.proxy(renames["TimeOfDayIn"]).optional(),
            "startDate": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["DenyMaintenancePeriodIn"])
    types["DenyMaintenancePeriodOut"] = t.struct(
        {
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "time": t.proxy(renames["TimeOfDayOut"]).optional(),
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DenyMaintenancePeriodOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn"
    ] = t.struct(
        {
            "exclude": t.boolean().optional(),
            "isRollback": t.boolean().optional(),
            "maintenancePolicies": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut"
    ] = t.struct(
        {
            "exclude": t.boolean().optional(),
            "isRollback": t.boolean().optional(),
            "maintenancePolicies": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut"]
    )
    types["NfsExportOptionsIn"] = t.struct(
        {
            "anonUid": t.string().optional(),
            "accessMode": t.string().optional(),
            "anonGid": t.string().optional(),
            "squashMode": t.string().optional(),
            "ipRanges": t.array(t.string()).optional(),
        }
    ).named(renames["NfsExportOptionsIn"])
    types["NfsExportOptionsOut"] = t.struct(
        {
            "anonUid": t.string().optional(),
            "accessMode": t.string().optional(),
            "anonGid": t.string().optional(),
            "squashMode": t.string().optional(),
            "ipRanges": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NfsExportOptionsOut"])
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["SnapshotIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["SnapshotIn"])
    types["SnapshotOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "filesystemUsedBytes": t.string().optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnapshotOut"])
    types["RestoreInstanceRequestIn"] = t.struct(
        {"sourceBackup": t.string().optional(), "fileShare": t.string()}
    ).named(renames["RestoreInstanceRequestIn"])
    types["RestoreInstanceRequestOut"] = t.struct(
        {
            "sourceBackup": t.string().optional(),
            "fileShare": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreInstanceRequestOut"])
    types["DailyCycleIn"] = t.struct(
        {
            "startTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "duration": t.string().optional(),
        }
    ).named(renames["DailyCycleIn"])
    types["DailyCycleOut"] = t.struct(
        {
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "duration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DailyCycleOut"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn"] = t.struct(
        {
            "perSliEligibility": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn"
                ]
            ).optional(),
            "tier": t.string().optional(),
            "nodes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut"] = t.struct(
        {
            "perSliEligibility": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut"
                ]
            ).optional(),
            "tier": t.string().optional(),
            "nodes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut"])
    types["ListInstancesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "instances": t.array(t.proxy(renames["InstanceIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListInstancesResponseIn"])
    types["ListInstancesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "instances": t.array(t.proxy(renames["InstanceOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInstancesResponseOut"])
    types["InstanceIn"] = t.struct(
        {
            "description": t.string().optional(),
            "fileShares": t.array(t.proxy(renames["FileShareConfigIn"])).optional(),
            "kmsKeyName": t.string().optional(),
            "tier": t.string().optional(),
            "etag": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "networks": t.array(t.proxy(renames["NetworkConfigIn"])).optional(),
        }
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "fileShares": t.array(t.proxy(renames["FileShareConfigOut"])).optional(),
            "kmsKeyName": t.string().optional(),
            "tier": t.string().optional(),
            "etag": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "networks": t.array(t.proxy(renames["NetworkConfigOut"])).optional(),
            "satisfiesPzs": t.boolean().optional(),
            "suspensionReasons": t.array(t.string()).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn"
    ] = t.struct(
        {
            "endTime": t.string().optional(),
            "scheduleDeadlineTime": t.string().optional(),
            "canReschedule": t.boolean().optional(),
            "startTime": t.string().optional(),
            "rolloutManagementPolicy": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut"
    ] = t.struct(
        {
            "endTime": t.string().optional(),
            "scheduleDeadlineTime": t.string().optional(),
            "canReschedule": t.boolean().optional(),
            "startTime": t.string().optional(),
            "rolloutManagementPolicy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn"
    ] = t.struct(
        {
            "nodeId": t.string().optional(),
            "location": t.string().optional(),
            "perSliEligibility": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn"
                ]
            ).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut"
    ] = t.struct(
        {
            "nodeId": t.string().optional(),
            "location": t.string().optional(),
            "perSliEligibility": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut"]
    )
    types["RevertInstanceRequestIn"] = t.struct({"targetSnapshotId": t.string()}).named(
        renames["RevertInstanceRequestIn"]
    )
    types["RevertInstanceRequestOut"] = t.struct(
        {
            "targetSnapshotId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevertInstanceRequestOut"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn"] = t.struct(
        {"reason": t.string().optional(), "eligible": t.boolean().optional()}
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn"])
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut"
    ] = t.struct(
        {
            "reason": t.string().optional(),
            "eligible": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut"]
    )
    types["MaintenanceWindowIn"] = t.struct(
        {
            "weeklyCycle": t.proxy(renames["WeeklyCycleIn"]).optional(),
            "dailyCycle": t.proxy(renames["DailyCycleIn"]).optional(),
        }
    ).named(renames["MaintenanceWindowIn"])
    types["MaintenanceWindowOut"] = t.struct(
        {
            "weeklyCycle": t.proxy(renames["WeeklyCycleOut"]).optional(),
            "dailyCycle": t.proxy(renames["DailyCycleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceWindowOut"])
    types["NetworkConfigIn"] = t.struct(
        {
            "connectMode": t.string().optional(),
            "modes": t.array(t.string()).optional(),
            "network": t.string().optional(),
            "reservedIpRange": t.string().optional(),
        }
    ).named(renames["NetworkConfigIn"])
    types["NetworkConfigOut"] = t.struct(
        {
            "connectMode": t.string().optional(),
            "modes": t.array(t.string()).optional(),
            "network": t.string().optional(),
            "reservedIpRange": t.string().optional(),
            "ipAddresses": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConfigOut"])
    types["MaintenancePolicyIn"] = t.struct(
        {
            "name": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "updatePolicy": t.proxy(renames["UpdatePolicyIn"]).optional(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["MaintenancePolicyIn"])
    types["MaintenancePolicyOut"] = t.struct(
        {
            "name": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "updatePolicy": t.proxy(renames["UpdatePolicyOut"]).optional(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenancePolicyOut"])
    types["ListSnapshotsResponseIn"] = t.struct(
        {
            "snapshots": t.array(t.proxy(renames["SnapshotIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListSnapshotsResponseIn"])
    types["ListSnapshotsResponseOut"] = t.struct(
        {
            "snapshots": t.array(t.proxy(renames["SnapshotOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSnapshotsResponseOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "verb": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "statusDetail": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["ScheduleIn"] = t.struct(
        {
            "day": t.string().optional(),
            "startTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "duration": t.string().optional(),
        }
    ).named(renames["ScheduleIn"])
    types["ScheduleOut"] = t.struct(
        {
            "day": t.string().optional(),
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "duration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduleOut"])
    types["FileShareConfigIn"] = t.struct(
        {
            "capacityGb": t.string().optional(),
            "name": t.string().optional(),
            "sourceBackup": t.string().optional(),
            "nfsExportOptions": t.array(
                t.proxy(renames["NfsExportOptionsIn"])
            ).optional(),
        }
    ).named(renames["FileShareConfigIn"])
    types["FileShareConfigOut"] = t.struct(
        {
            "capacityGb": t.string().optional(),
            "name": t.string().optional(),
            "sourceBackup": t.string().optional(),
            "nfsExportOptions": t.array(
                t.proxy(renames["NfsExportOptionsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileShareConfigOut"])
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn"
    ] = t.struct(
        {"eligibilities": t.struct({"_": t.string().optional()}).optional()}
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut"
    ] = t.struct(
        {
            "eligibilities": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut"
        ]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn"
    ] = t.struct({"values": t.array(t.string()).optional()}).named(
        renames[
            "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn"
        ]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut"
    ] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut"
        ]
    )

    functions = {}
    functions["projectsLocationsList"] = file.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = file.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDelete"] = file.post(
        "v1/{name}:restore",
        t.struct(
            {
                "name": t.string(),
                "sourceBackup": t.string().optional(),
                "fileShare": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesList"] = file.post(
        "v1/{name}:restore",
        t.struct(
            {
                "name": t.string(),
                "sourceBackup": t.string().optional(),
                "fileShare": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesRevert"] = file.post(
        "v1/{name}:restore",
        t.struct(
            {
                "name": t.string(),
                "sourceBackup": t.string().optional(),
                "fileShare": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesPatch"] = file.post(
        "v1/{name}:restore",
        t.struct(
            {
                "name": t.string(),
                "sourceBackup": t.string().optional(),
                "fileShare": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesGet"] = file.post(
        "v1/{name}:restore",
        t.struct(
            {
                "name": t.string(),
                "sourceBackup": t.string().optional(),
                "fileShare": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesCreate"] = file.post(
        "v1/{name}:restore",
        t.struct(
            {
                "name": t.string(),
                "sourceBackup": t.string().optional(),
                "fileShare": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesRestore"] = file.post(
        "v1/{name}:restore",
        t.struct(
            {
                "name": t.string(),
                "sourceBackup": t.string().optional(),
                "fileShare": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesSnapshotsPatch"] = file.post(
        "v1/{parent}/snapshots",
        t.struct(
            {
                "snapshotId": t.string(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesSnapshotsList"] = file.post(
        "v1/{parent}/snapshots",
        t.struct(
            {
                "snapshotId": t.string(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesSnapshotsDelete"] = file.post(
        "v1/{parent}/snapshots",
        t.struct(
            {
                "snapshotId": t.string(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesSnapshotsGet"] = file.post(
        "v1/{parent}/snapshots",
        t.struct(
            {
                "snapshotId": t.string(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesSnapshotsCreate"] = file.post(
        "v1/{parent}/snapshots",
        t.struct(
            {
                "snapshotId": t.string(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupsList"] = file.post(
        "v1/{parent}/backups",
        t.struct(
            {
                "parent": t.string(),
                "backupId": t.string(),
                "sourceFileShare": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "kmsKey": t.string().optional(),
                "sourceInstance": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupsPatch"] = file.post(
        "v1/{parent}/backups",
        t.struct(
            {
                "parent": t.string(),
                "backupId": t.string(),
                "sourceFileShare": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "kmsKey": t.string().optional(),
                "sourceInstance": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupsDelete"] = file.post(
        "v1/{parent}/backups",
        t.struct(
            {
                "parent": t.string(),
                "backupId": t.string(),
                "sourceFileShare": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "kmsKey": t.string().optional(),
                "sourceInstance": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupsGet"] = file.post(
        "v1/{parent}/backups",
        t.struct(
            {
                "parent": t.string(),
                "backupId": t.string(),
                "sourceFileShare": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "kmsKey": t.string().optional(),
                "sourceInstance": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupsCreate"] = file.post(
        "v1/{parent}/backups",
        t.struct(
            {
                "parent": t.string(),
                "backupId": t.string(),
                "sourceFileShare": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "kmsKey": t.string().optional(),
                "sourceInstance": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = file.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = file.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = file.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = file.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="file", renames=renames, types=types, functions=functions)
