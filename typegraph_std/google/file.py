from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_file() -> Import:
    file = HTTPRuntime("https://file.googleapis.com/")

    renames = {
        "ErrorResponse": "_file_1_ErrorResponse",
        "DateIn": "_file_2_DateIn",
        "DateOut": "_file_3_DateOut",
        "RevertInstanceRequestIn": "_file_4_RevertInstanceRequestIn",
        "RevertInstanceRequestOut": "_file_5_RevertInstanceRequestOut",
        "ListBackupsResponseIn": "_file_6_ListBackupsResponseIn",
        "ListBackupsResponseOut": "_file_7_ListBackupsResponseOut",
        "NfsExportOptionsIn": "_file_8_NfsExportOptionsIn",
        "NfsExportOptionsOut": "_file_9_NfsExportOptionsOut",
        "EmptyIn": "_file_10_EmptyIn",
        "EmptyOut": "_file_11_EmptyOut",
        "ListLocationsResponseIn": "_file_12_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_file_13_ListLocationsResponseOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn": "_file_14_GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut": "_file_15_GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn": "_file_16_GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut": "_file_17_GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut",
        "TimeOfDayIn": "_file_18_TimeOfDayIn",
        "TimeOfDayOut": "_file_19_TimeOfDayOut",
        "UpdatePolicyIn": "_file_20_UpdatePolicyIn",
        "UpdatePolicyOut": "_file_21_UpdatePolicyOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn": "_file_22_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut": "_file_23_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut",
        "OperationMetadataIn": "_file_24_OperationMetadataIn",
        "OperationMetadataOut": "_file_25_OperationMetadataOut",
        "DailyCycleIn": "_file_26_DailyCycleIn",
        "DailyCycleOut": "_file_27_DailyCycleOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn": "_file_28_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut": "_file_29_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut",
        "WeeklyCycleIn": "_file_30_WeeklyCycleIn",
        "WeeklyCycleOut": "_file_31_WeeklyCycleOut",
        "ScheduleIn": "_file_32_ScheduleIn",
        "ScheduleOut": "_file_33_ScheduleOut",
        "BackupIn": "_file_34_BackupIn",
        "BackupOut": "_file_35_BackupOut",
        "ListSnapshotsResponseIn": "_file_36_ListSnapshotsResponseIn",
        "ListSnapshotsResponseOut": "_file_37_ListSnapshotsResponseOut",
        "MaintenanceWindowIn": "_file_38_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_file_39_MaintenanceWindowOut",
        "ListOperationsResponseIn": "_file_40_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_file_41_ListOperationsResponseOut",
        "MaintenancePolicyIn": "_file_42_MaintenancePolicyIn",
        "MaintenancePolicyOut": "_file_43_MaintenancePolicyOut",
        "SnapshotIn": "_file_44_SnapshotIn",
        "SnapshotOut": "_file_45_SnapshotOut",
        "LocationIn": "_file_46_LocationIn",
        "LocationOut": "_file_47_LocationOut",
        "NetworkConfigIn": "_file_48_NetworkConfigIn",
        "NetworkConfigOut": "_file_49_NetworkConfigOut",
        "DenyMaintenancePeriodIn": "_file_50_DenyMaintenancePeriodIn",
        "DenyMaintenancePeriodOut": "_file_51_DenyMaintenancePeriodOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn": "_file_52_GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut": "_file_53_GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut",
        "FileShareConfigIn": "_file_54_FileShareConfigIn",
        "FileShareConfigOut": "_file_55_FileShareConfigOut",
        "StatusIn": "_file_56_StatusIn",
        "StatusOut": "_file_57_StatusOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn": "_file_58_GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut": "_file_59_GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut",
        "ListInstancesResponseIn": "_file_60_ListInstancesResponseIn",
        "ListInstancesResponseOut": "_file_61_ListInstancesResponseOut",
        "InstanceIn": "_file_62_InstanceIn",
        "InstanceOut": "_file_63_InstanceOut",
        "RestoreInstanceRequestIn": "_file_64_RestoreInstanceRequestIn",
        "RestoreInstanceRequestOut": "_file_65_RestoreInstanceRequestOut",
        "OperationIn": "_file_66_OperationIn",
        "OperationOut": "_file_67_OperationOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn": "_file_68_GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut": "_file_69_GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut",
        "CancelOperationRequestIn": "_file_70_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_file_71_CancelOperationRequestOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn": "_file_72_GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut": "_file_73_GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn": "_file_74_GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut": "_file_75_GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["RevertInstanceRequestIn"] = t.struct({"targetSnapshotId": t.string()}).named(
        renames["RevertInstanceRequestIn"]
    )
    types["RevertInstanceRequestOut"] = t.struct(
        {
            "targetSnapshotId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevertInstanceRequestOut"])
    types["ListBackupsResponseIn"] = t.struct(
        {
            "backups": t.array(t.proxy(renames["BackupIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListBackupsResponseIn"])
    types["ListBackupsResponseOut"] = t.struct(
        {
            "backups": t.array(t.proxy(renames["BackupOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBackupsResponseOut"])
    types["NfsExportOptionsIn"] = t.struct(
        {
            "anonGid": t.string().optional(),
            "ipRanges": t.array(t.string()).optional(),
            "accessMode": t.string().optional(),
            "squashMode": t.string().optional(),
            "anonUid": t.string().optional(),
        }
    ).named(renames["NfsExportOptionsIn"])
    types["NfsExportOptionsOut"] = t.struct(
        {
            "anonGid": t.string().optional(),
            "ipRanges": t.array(t.string()).optional(),
            "accessMode": t.string().optional(),
            "squashMode": t.string().optional(),
            "anonUid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NfsExportOptionsOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
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
    types["TimeOfDayIn"] = t.struct(
        {
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["UpdatePolicyIn"] = t.struct(
        {
            "window": t.proxy(renames["MaintenanceWindowIn"]).optional(),
            "channel": t.string().optional(),
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodIn"])
            ).optional(),
        }
    ).named(renames["UpdatePolicyIn"])
    types["UpdatePolicyOut"] = t.struct(
        {
            "window": t.proxy(renames["MaintenanceWindowOut"]).optional(),
            "channel": t.string().optional(),
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdatePolicyOut"])
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn"
    ] = t.struct(
        {
            "isRollback": t.boolean().optional(),
            "exclude": t.boolean().optional(),
            "maintenancePolicies": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut"
    ] = t.struct(
        {
            "isRollback": t.boolean().optional(),
            "exclude": t.boolean().optional(),
            "maintenancePolicies": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut"]
    )
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "statusDetail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn"
    ] = t.struct(
        {
            "rolloutManagementPolicy": t.string().optional(),
            "startTime": t.string().optional(),
            "scheduleDeadlineTime": t.string().optional(),
            "canReschedule": t.boolean().optional(),
            "endTime": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut"
    ] = t.struct(
        {
            "rolloutManagementPolicy": t.string().optional(),
            "startTime": t.string().optional(),
            "scheduleDeadlineTime": t.string().optional(),
            "canReschedule": t.boolean().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut"]
    )
    types["WeeklyCycleIn"] = t.struct(
        {"schedule": t.array(t.proxy(renames["ScheduleIn"])).optional()}
    ).named(renames["WeeklyCycleIn"])
    types["WeeklyCycleOut"] = t.struct(
        {
            "schedule": t.array(t.proxy(renames["ScheduleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WeeklyCycleOut"])
    types["ScheduleIn"] = t.struct(
        {
            "startTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "duration": t.string().optional(),
            "day": t.string().optional(),
        }
    ).named(renames["ScheduleIn"])
    types["ScheduleOut"] = t.struct(
        {
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "duration": t.string().optional(),
            "day": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduleOut"])
    types["BackupIn"] = t.struct(
        {
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "kmsKey": t.string().optional(),
            "sourceFileShare": t.string().optional(),
            "sourceInstance": t.string().optional(),
        }
    ).named(renames["BackupIn"])
    types["BackupOut"] = t.struct(
        {
            "sourceInstanceTier": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "satisfiesPzs": t.boolean().optional(),
            "kmsKey": t.string().optional(),
            "storageBytes": t.string().optional(),
            "sourceFileShare": t.string().optional(),
            "downloadBytes": t.string().optional(),
            "capacityGb": t.string().optional(),
            "createTime": t.string().optional(),
            "sourceInstance": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupOut"])
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
    types["MaintenanceWindowIn"] = t.struct(
        {
            "dailyCycle": t.proxy(renames["DailyCycleIn"]).optional(),
            "weeklyCycle": t.proxy(renames["WeeklyCycleIn"]).optional(),
        }
    ).named(renames["MaintenanceWindowIn"])
    types["MaintenanceWindowOut"] = t.struct(
        {
            "dailyCycle": t.proxy(renames["DailyCycleOut"]).optional(),
            "weeklyCycle": t.proxy(renames["WeeklyCycleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceWindowOut"])
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
    types["MaintenancePolicyIn"] = t.struct(
        {
            "name": t.string(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "updatePolicy": t.proxy(renames["UpdatePolicyIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["MaintenancePolicyIn"])
    types["MaintenancePolicyOut"] = t.struct(
        {
            "name": t.string(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "updatePolicy": t.proxy(renames["UpdatePolicyOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenancePolicyOut"])
    types["SnapshotIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["SnapshotIn"])
    types["SnapshotOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "filesystemUsedBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnapshotOut"])
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["NetworkConfigIn"] = t.struct(
        {
            "modes": t.array(t.string()).optional(),
            "network": t.string().optional(),
            "reservedIpRange": t.string().optional(),
            "connectMode": t.string().optional(),
        }
    ).named(renames["NetworkConfigIn"])
    types["NetworkConfigOut"] = t.struct(
        {
            "ipAddresses": t.array(t.string()).optional(),
            "modes": t.array(t.string()).optional(),
            "network": t.string().optional(),
            "reservedIpRange": t.string().optional(),
            "connectMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConfigOut"])
    types["DenyMaintenancePeriodIn"] = t.struct(
        {
            "time": t.proxy(renames["TimeOfDayIn"]).optional(),
            "startDate": t.proxy(renames["DateIn"]).optional(),
            "endDate": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["DenyMaintenancePeriodIn"])
    types["DenyMaintenancePeriodOut"] = t.struct(
        {
            "time": t.proxy(renames["TimeOfDayOut"]).optional(),
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DenyMaintenancePeriodOut"])
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn"
    ] = t.struct(
        {"resourceType": t.string().optional(), "resourceUrl": t.string().optional()}
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut"
    ] = t.struct(
        {
            "resourceType": t.string().optional(),
            "resourceUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut"]
    )
    types["FileShareConfigIn"] = t.struct(
        {
            "sourceBackup": t.string().optional(),
            "capacityGb": t.string().optional(),
            "name": t.string().optional(),
            "nfsExportOptions": t.array(
                t.proxy(renames["NfsExportOptionsIn"])
            ).optional(),
        }
    ).named(renames["FileShareConfigIn"])
    types["FileShareConfigOut"] = t.struct(
        {
            "sourceBackup": t.string().optional(),
            "capacityGb": t.string().optional(),
            "name": t.string().optional(),
            "nfsExportOptions": t.array(
                t.proxy(renames["NfsExportOptionsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileShareConfigOut"])
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
    types["ListInstancesResponseIn"] = t.struct(
        {
            "instances": t.array(t.proxy(renames["InstanceIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListInstancesResponseIn"])
    types["ListInstancesResponseOut"] = t.struct(
        {
            "instances": t.array(t.proxy(renames["InstanceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInstancesResponseOut"])
    types["InstanceIn"] = t.struct(
        {
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "fileShares": t.array(t.proxy(renames["FileShareConfigIn"])).optional(),
            "tier": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "networks": t.array(t.proxy(renames["NetworkConfigIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "suspensionReasons": t.array(t.string()).optional(),
            "statusMessage": t.string().optional(),
            "description": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "fileShares": t.array(t.proxy(renames["FileShareConfigOut"])).optional(),
            "tier": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "networks": t.array(t.proxy(renames["NetworkConfigOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
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
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn"
    ] = t.struct(
        {
            "location": t.string().optional(),
            "perSliEligibility": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn"
                ]
            ).optional(),
            "nodeId": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut"
    ] = t.struct(
        {
            "location": t.string().optional(),
            "perSliEligibility": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut"
                ]
            ).optional(),
            "nodeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut"]
    )
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn"] = t.struct(
        {
            "softwareVersions": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "slmInstanceTemplate": t.string().optional(),
            "maintenanceSettings": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn"
                ]
            ).optional(),
            "maintenanceSchedules": t.struct({"_": t.string().optional()}).optional(),
            "notificationParameters": t.struct({"_": t.string().optional()}).optional(),
            "consumerDefinedName": t.string().optional(),
            "name": t.string().optional(),
            "maintenancePolicyNames": t.struct({"_": t.string().optional()}).optional(),
            "instanceType": t.string().optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut"] = t.struct(
        {
            "producerMetadata": t.struct({"_": t.string().optional()}).optional(),
            "softwareVersions": t.struct({"_": t.string().optional()}).optional(),
            "provisionedResources": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut"
                    ]
                )
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "slmInstanceTemplate": t.string().optional(),
            "maintenanceSettings": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut"
                ]
            ).optional(),
            "updateTime": t.string().optional(),
            "maintenanceSchedules": t.struct({"_": t.string().optional()}).optional(),
            "notificationParameters": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "consumerDefinedName": t.string().optional(),
            "tenantProjectId": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "maintenancePolicyNames": t.struct({"_": t.string().optional()}).optional(),
            "sloMetadata": t.proxy(
                renames["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut"]
            ).optional(),
            "instanceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut"])

    functions = {}
    functions["projectsLocationsGet"] = file.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "includeUnrevealedLocations": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = file.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "includeUnrevealedLocations": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupsList"] = file.post(
        "v1/{parent}/backups",
        t.struct(
            {
                "parent": t.string(),
                "backupId": t.string(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "kmsKey": t.string().optional(),
                "sourceFileShare": t.string().optional(),
                "sourceInstance": t.string().optional(),
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
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "kmsKey": t.string().optional(),
                "sourceFileShare": t.string().optional(),
                "sourceInstance": t.string().optional(),
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
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "kmsKey": t.string().optional(),
                "sourceFileShare": t.string().optional(),
                "sourceInstance": t.string().optional(),
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
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "kmsKey": t.string().optional(),
                "sourceFileShare": t.string().optional(),
                "sourceInstance": t.string().optional(),
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
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "kmsKey": t.string().optional(),
                "sourceFileShare": t.string().optional(),
                "sourceInstance": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = file.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = file.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = file.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = file.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
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
    functions["projectsLocationsInstancesSnapshotsDelete"] = file.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesSnapshotsCreate"] = file.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesSnapshotsList"] = file.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesSnapshotsPatch"] = file.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesSnapshotsGet"] = file.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="file", renames=renames, types=Box(types), functions=Box(functions)
    )
