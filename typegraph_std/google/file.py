from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_file():
    file = HTTPRuntime("https://file.googleapis.com/")

    renames = {
        "ErrorResponse": "_file_1_ErrorResponse",
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn": "_file_2_GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut": "_file_3_GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn": "_file_4_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut": "_file_5_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut",
        "InstanceIn": "_file_6_InstanceIn",
        "InstanceOut": "_file_7_InstanceOut",
        "BackupIn": "_file_8_BackupIn",
        "BackupOut": "_file_9_BackupOut",
        "ListBackupsResponseIn": "_file_10_ListBackupsResponseIn",
        "ListBackupsResponseOut": "_file_11_ListBackupsResponseOut",
        "DailyCycleIn": "_file_12_DailyCycleIn",
        "DailyCycleOut": "_file_13_DailyCycleOut",
        "StatusIn": "_file_14_StatusIn",
        "StatusOut": "_file_15_StatusOut",
        "NfsExportOptionsIn": "_file_16_NfsExportOptionsIn",
        "NfsExportOptionsOut": "_file_17_NfsExportOptionsOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn": "_file_18_GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut": "_file_19_GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut",
        "SnapshotIn": "_file_20_SnapshotIn",
        "SnapshotOut": "_file_21_SnapshotOut",
        "MaintenanceWindowIn": "_file_22_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_file_23_MaintenanceWindowOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn": "_file_24_GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut": "_file_25_GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut",
        "ListSnapshotsResponseIn": "_file_26_ListSnapshotsResponseIn",
        "ListSnapshotsResponseOut": "_file_27_ListSnapshotsResponseOut",
        "ListInstancesResponseIn": "_file_28_ListInstancesResponseIn",
        "ListInstancesResponseOut": "_file_29_ListInstancesResponseOut",
        "TimeOfDayIn": "_file_30_TimeOfDayIn",
        "TimeOfDayOut": "_file_31_TimeOfDayOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn": "_file_32_GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut": "_file_33_GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut",
        "FileShareConfigIn": "_file_34_FileShareConfigIn",
        "FileShareConfigOut": "_file_35_FileShareConfigOut",
        "ListLocationsResponseIn": "_file_36_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_file_37_ListLocationsResponseOut",
        "ListOperationsResponseIn": "_file_38_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_file_39_ListOperationsResponseOut",
        "NetworkConfigIn": "_file_40_NetworkConfigIn",
        "NetworkConfigOut": "_file_41_NetworkConfigOut",
        "DateIn": "_file_42_DateIn",
        "DateOut": "_file_43_DateOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn": "_file_44_GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut": "_file_45_GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut",
        "MaintenancePolicyIn": "_file_46_MaintenancePolicyIn",
        "MaintenancePolicyOut": "_file_47_MaintenancePolicyOut",
        "ScheduleIn": "_file_48_ScheduleIn",
        "ScheduleOut": "_file_49_ScheduleOut",
        "OperationMetadataIn": "_file_50_OperationMetadataIn",
        "OperationMetadataOut": "_file_51_OperationMetadataOut",
        "RevertInstanceRequestIn": "_file_52_RevertInstanceRequestIn",
        "RevertInstanceRequestOut": "_file_53_RevertInstanceRequestOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn": "_file_54_GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut": "_file_55_GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut",
        "CancelOperationRequestIn": "_file_56_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_file_57_CancelOperationRequestOut",
        "DenyMaintenancePeriodIn": "_file_58_DenyMaintenancePeriodIn",
        "DenyMaintenancePeriodOut": "_file_59_DenyMaintenancePeriodOut",
        "RestoreInstanceRequestIn": "_file_60_RestoreInstanceRequestIn",
        "RestoreInstanceRequestOut": "_file_61_RestoreInstanceRequestOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn": "_file_62_GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut": "_file_63_GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut",
        "UpdatePolicyIn": "_file_64_UpdatePolicyIn",
        "UpdatePolicyOut": "_file_65_UpdatePolicyOut",
        "OperationIn": "_file_66_OperationIn",
        "OperationOut": "_file_67_OperationOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn": "_file_68_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut": "_file_69_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut",
        "WeeklyCycleIn": "_file_70_WeeklyCycleIn",
        "WeeklyCycleOut": "_file_71_WeeklyCycleOut",
        "EmptyIn": "_file_72_EmptyIn",
        "EmptyOut": "_file_73_EmptyOut",
        "LocationIn": "_file_74_LocationIn",
        "LocationOut": "_file_75_LocationOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn"
    ] = t.struct(
        {
            "startTime": t.string().optional(),
            "scheduleDeadlineTime": t.string().optional(),
            "rolloutManagementPolicy": t.string().optional(),
            "endTime": t.string().optional(),
            "canReschedule": t.boolean().optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut"
    ] = t.struct(
        {
            "startTime": t.string().optional(),
            "scheduleDeadlineTime": t.string().optional(),
            "rolloutManagementPolicy": t.string().optional(),
            "endTime": t.string().optional(),
            "canReschedule": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut"]
    )
    types["InstanceIn"] = t.struct(
        {
            "fileShares": t.array(t.proxy(renames["FileShareConfigIn"])).optional(),
            "etag": t.string().optional(),
            "description": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "networks": t.array(t.proxy(renames["NetworkConfigIn"])).optional(),
            "tier": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "fileShares": t.array(t.proxy(renames["FileShareConfigOut"])).optional(),
            "suspensionReasons": t.array(t.string()).optional(),
            "etag": t.string().optional(),
            "description": t.string().optional(),
            "statusMessage": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "createTime": t.string().optional(),
            "networks": t.array(t.proxy(renames["NetworkConfigOut"])).optional(),
            "tier": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
    types["BackupIn"] = t.struct(
        {
            "sourceInstance": t.string().optional(),
            "kmsKey": t.string().optional(),
            "description": t.string().optional(),
            "sourceFileShare": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["BackupIn"])
    types["BackupOut"] = t.struct(
        {
            "downloadBytes": t.string().optional(),
            "sourceInstanceTier": t.string().optional(),
            "sourceInstance": t.string().optional(),
            "state": t.string().optional(),
            "capacityGb": t.string().optional(),
            "name": t.string().optional(),
            "kmsKey": t.string().optional(),
            "storageBytes": t.string().optional(),
            "description": t.string().optional(),
            "sourceFileShare": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "satisfiesPzs": t.boolean().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupOut"])
    types["ListBackupsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "backups": t.array(t.proxy(renames["BackupIn"])).optional(),
        }
    ).named(renames["ListBackupsResponseIn"])
    types["ListBackupsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "backups": t.array(t.proxy(renames["BackupOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBackupsResponseOut"])
    types["DailyCycleIn"] = t.struct(
        {
            "duration": t.string().optional(),
            "startTime": t.proxy(renames["TimeOfDayIn"]).optional(),
        }
    ).named(renames["DailyCycleIn"])
    types["DailyCycleOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DailyCycleOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["NfsExportOptionsIn"] = t.struct(
        {
            "anonGid": t.string().optional(),
            "squashMode": t.string().optional(),
            "anonUid": t.string().optional(),
            "ipRanges": t.array(t.string()).optional(),
            "accessMode": t.string().optional(),
        }
    ).named(renames["NfsExportOptionsIn"])
    types["NfsExportOptionsOut"] = t.struct(
        {
            "anonGid": t.string().optional(),
            "squashMode": t.string().optional(),
            "anonUid": t.string().optional(),
            "ipRanges": t.array(t.string()).optional(),
            "accessMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NfsExportOptionsOut"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn"] = t.struct(
        {
            "tier": t.string().optional(),
            "nodes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn"
                    ]
                )
            ).optional(),
            "perSliEligibility": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut"] = t.struct(
        {
            "tier": t.string().optional(),
            "nodes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut"
                    ]
                )
            ).optional(),
            "perSliEligibility": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut"])
    types["SnapshotIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["SnapshotIn"])
    types["SnapshotOut"] = t.struct(
        {
            "name": t.string().optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "filesystemUsedBytes": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnapshotOut"])
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
    types["ListSnapshotsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "snapshots": t.array(t.proxy(renames["SnapshotIn"])).optional(),
        }
    ).named(renames["ListSnapshotsResponseIn"])
    types["ListSnapshotsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "snapshots": t.array(t.proxy(renames["SnapshotOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSnapshotsResponseOut"])
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
    types["TimeOfDayIn"] = t.struct(
        {
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
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
    types["FileShareConfigIn"] = t.struct(
        {
            "capacityGb": t.string().optional(),
            "name": t.string().optional(),
            "nfsExportOptions": t.array(
                t.proxy(renames["NfsExportOptionsIn"])
            ).optional(),
            "sourceBackup": t.string().optional(),
        }
    ).named(renames["FileShareConfigIn"])
    types["FileShareConfigOut"] = t.struct(
        {
            "capacityGb": t.string().optional(),
            "name": t.string().optional(),
            "nfsExportOptions": t.array(
                t.proxy(renames["NfsExportOptionsOut"])
            ).optional(),
            "sourceBackup": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileShareConfigOut"])
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
    types["NetworkConfigIn"] = t.struct(
        {
            "network": t.string().optional(),
            "reservedIpRange": t.string().optional(),
            "connectMode": t.string().optional(),
            "modes": t.array(t.string()).optional(),
        }
    ).named(renames["NetworkConfigIn"])
    types["NetworkConfigOut"] = t.struct(
        {
            "network": t.string().optional(),
            "ipAddresses": t.array(t.string()).optional(),
            "reservedIpRange": t.string().optional(),
            "connectMode": t.string().optional(),
            "modes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConfigOut"])
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
    types["MaintenancePolicyIn"] = t.struct(
        {
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "updatePolicy": t.proxy(renames["UpdatePolicyIn"]).optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["MaintenancePolicyIn"])
    types["MaintenancePolicyOut"] = t.struct(
        {
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "updatePolicy": t.proxy(renames["UpdatePolicyOut"]).optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenancePolicyOut"])
    types["ScheduleIn"] = t.struct(
        {
            "day": t.string().optional(),
            "duration": t.string().optional(),
            "startTime": t.proxy(renames["TimeOfDayIn"]).optional(),
        }
    ).named(renames["ScheduleIn"])
    types["ScheduleOut"] = t.struct(
        {
            "day": t.string().optional(),
            "duration": t.string().optional(),
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduleOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "statusDetail": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["RestoreInstanceRequestIn"] = t.struct(
        {"fileShare": t.string(), "sourceBackup": t.string().optional()}
    ).named(renames["RestoreInstanceRequestIn"])
    types["RestoreInstanceRequestOut"] = t.struct(
        {
            "fileShare": t.string(),
            "sourceBackup": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreInstanceRequestOut"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn"] = t.struct(
        {
            "maintenanceSchedules": t.struct({"_": t.string().optional()}).optional(),
            "maintenancePolicyNames": t.struct({"_": t.string().optional()}).optional(),
            "softwareVersions": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "consumerDefinedName": t.string().optional(),
            "maintenanceSettings": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn"
                ]
            ).optional(),
            "instanceType": t.string().optional(),
            "notificationParameters": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "slmInstanceTemplate": t.string().optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut"] = t.struct(
        {
            "provisionedResources": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut"
                    ]
                )
            ).optional(),
            "maintenanceSchedules": t.struct({"_": t.string().optional()}).optional(),
            "producerMetadata": t.struct({"_": t.string().optional()}).optional(),
            "maintenancePolicyNames": t.struct({"_": t.string().optional()}).optional(),
            "softwareVersions": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "consumerDefinedName": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "maintenanceSettings": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut"
                ]
            ).optional(),
            "state": t.string().optional(),
            "instanceType": t.string().optional(),
            "notificationParameters": t.struct({"_": t.string().optional()}).optional(),
            "sloMetadata": t.proxy(
                renames["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "tenantProjectId": t.string().optional(),
            "slmInstanceTemplate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut"])
    types["UpdatePolicyIn"] = t.struct(
        {
            "channel": t.string().optional(),
            "window": t.proxy(renames["MaintenanceWindowIn"]).optional(),
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodIn"])
            ).optional(),
        }
    ).named(renames["UpdatePolicyIn"])
    types["UpdatePolicyOut"] = t.struct(
        {
            "channel": t.string().optional(),
            "window": t.proxy(renames["MaintenanceWindowOut"]).optional(),
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdatePolicyOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["WeeklyCycleIn"] = t.struct(
        {"schedule": t.array(t.proxy(renames["ScheduleIn"])).optional()}
    ).named(renames["WeeklyCycleIn"])
    types["WeeklyCycleOut"] = t.struct(
        {
            "schedule": t.array(t.proxy(renames["ScheduleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WeeklyCycleOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])

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
    functions["projectsLocationsOperationsCancel"] = file.get(
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
    functions["projectsLocationsOperationsDelete"] = file.get(
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
    functions["projectsLocationsInstancesDelete"] = file.post(
        "v1/{name}:restore",
        t.struct(
            {
                "name": t.string(),
                "fileShare": t.string(),
                "sourceBackup": t.string().optional(),
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
                "fileShare": t.string(),
                "sourceBackup": t.string().optional(),
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
                "fileShare": t.string(),
                "sourceBackup": t.string().optional(),
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
                "fileShare": t.string(),
                "sourceBackup": t.string().optional(),
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
                "fileShare": t.string(),
                "sourceBackup": t.string().optional(),
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
                "fileShare": t.string(),
                "sourceBackup": t.string().optional(),
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
                "fileShare": t.string(),
                "sourceBackup": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesSnapshotsGet"] = file.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesSnapshotsPatch"] = file.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesSnapshotsCreate"] = file.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesSnapshotsList"] = file.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesSnapshotsDelete"] = file.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
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
                "sourceInstance": t.string().optional(),
                "kmsKey": t.string().optional(),
                "description": t.string().optional(),
                "sourceFileShare": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
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
                "sourceInstance": t.string().optional(),
                "kmsKey": t.string().optional(),
                "description": t.string().optional(),
                "sourceFileShare": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
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
                "sourceInstance": t.string().optional(),
                "kmsKey": t.string().optional(),
                "description": t.string().optional(),
                "sourceFileShare": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
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
                "sourceInstance": t.string().optional(),
                "kmsKey": t.string().optional(),
                "description": t.string().optional(),
                "sourceFileShare": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
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
                "sourceInstance": t.string().optional(),
                "kmsKey": t.string().optional(),
                "description": t.string().optional(),
                "sourceFileShare": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="file", renames=renames, types=Box(types), functions=Box(functions)
    )
