from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_file() -> Import:
    file = HTTPRuntime("https://file.googleapis.com/")

    renames = {
        "ErrorResponse": "_file_1_ErrorResponse",
        "CancelOperationRequestIn": "_file_2_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_file_3_CancelOperationRequestOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn": "_file_4_GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut": "_file_5_GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn": "_file_6_GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut": "_file_7_GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn": "_file_8_GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut": "_file_9_GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut",
        "ListSnapshotsResponseIn": "_file_10_ListSnapshotsResponseIn",
        "ListSnapshotsResponseOut": "_file_11_ListSnapshotsResponseOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn": "_file_12_GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut": "_file_13_GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut",
        "WeeklyCycleIn": "_file_14_WeeklyCycleIn",
        "WeeklyCycleOut": "_file_15_WeeklyCycleOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn": "_file_16_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut": "_file_17_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn": "_file_18_GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut": "_file_19_GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut",
        "ListBackupsResponseIn": "_file_20_ListBackupsResponseIn",
        "ListBackupsResponseOut": "_file_21_ListBackupsResponseOut",
        "TimeOfDayIn": "_file_22_TimeOfDayIn",
        "TimeOfDayOut": "_file_23_TimeOfDayOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn": "_file_24_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut": "_file_25_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut",
        "MaintenanceWindowIn": "_file_26_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_file_27_MaintenanceWindowOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn": "_file_28_GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut": "_file_29_GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut",
        "MaintenancePolicyIn": "_file_30_MaintenancePolicyIn",
        "MaintenancePolicyOut": "_file_31_MaintenancePolicyOut",
        "StatusIn": "_file_32_StatusIn",
        "StatusOut": "_file_33_StatusOut",
        "LocationIn": "_file_34_LocationIn",
        "LocationOut": "_file_35_LocationOut",
        "ListOperationsResponseIn": "_file_36_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_file_37_ListOperationsResponseOut",
        "RevertInstanceRequestIn": "_file_38_RevertInstanceRequestIn",
        "RevertInstanceRequestOut": "_file_39_RevertInstanceRequestOut",
        "ScheduleIn": "_file_40_ScheduleIn",
        "ScheduleOut": "_file_41_ScheduleOut",
        "BackupIn": "_file_42_BackupIn",
        "BackupOut": "_file_43_BackupOut",
        "DateIn": "_file_44_DateIn",
        "DateOut": "_file_45_DateOut",
        "ListLocationsResponseIn": "_file_46_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_file_47_ListLocationsResponseOut",
        "DenyMaintenancePeriodIn": "_file_48_DenyMaintenancePeriodIn",
        "DenyMaintenancePeriodOut": "_file_49_DenyMaintenancePeriodOut",
        "DailyCycleIn": "_file_50_DailyCycleIn",
        "DailyCycleOut": "_file_51_DailyCycleOut",
        "EmptyIn": "_file_52_EmptyIn",
        "EmptyOut": "_file_53_EmptyOut",
        "NfsExportOptionsIn": "_file_54_NfsExportOptionsIn",
        "NfsExportOptionsOut": "_file_55_NfsExportOptionsOut",
        "OperationMetadataIn": "_file_56_OperationMetadataIn",
        "OperationMetadataOut": "_file_57_OperationMetadataOut",
        "ListInstancesResponseIn": "_file_58_ListInstancesResponseIn",
        "ListInstancesResponseOut": "_file_59_ListInstancesResponseOut",
        "InstanceIn": "_file_60_InstanceIn",
        "InstanceOut": "_file_61_InstanceOut",
        "UpdatePolicyIn": "_file_62_UpdatePolicyIn",
        "UpdatePolicyOut": "_file_63_UpdatePolicyOut",
        "RestoreInstanceRequestIn": "_file_64_RestoreInstanceRequestIn",
        "RestoreInstanceRequestOut": "_file_65_RestoreInstanceRequestOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn": "_file_66_GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut": "_file_67_GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut",
        "NetworkConfigIn": "_file_68_NetworkConfigIn",
        "NetworkConfigOut": "_file_69_NetworkConfigOut",
        "FileShareConfigIn": "_file_70_FileShareConfigIn",
        "FileShareConfigOut": "_file_71_FileShareConfigOut",
        "SnapshotIn": "_file_72_SnapshotIn",
        "SnapshotOut": "_file_73_SnapshotOut",
        "OperationIn": "_file_74_OperationIn",
        "OperationOut": "_file_75_OperationOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn"] = t.struct(
        {
            "notificationParameters": t.struct({"_": t.string().optional()}).optional(),
            "instanceType": t.string().optional(),
            "maintenanceSettings": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn"
                ]
            ).optional(),
            "consumerDefinedName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "softwareVersions": t.struct({"_": t.string().optional()}).optional(),
            "maintenanceSchedules": t.struct({"_": t.string().optional()}).optional(),
            "maintenancePolicyNames": t.struct({"_": t.string().optional()}).optional(),
            "slmInstanceTemplate": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "notificationParameters": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "tenantProjectId": t.string().optional(),
            "instanceType": t.string().optional(),
            "maintenanceSettings": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut"
                ]
            ).optional(),
            "consumerDefinedName": t.string().optional(),
            "producerMetadata": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "softwareVersions": t.struct({"_": t.string().optional()}).optional(),
            "maintenanceSchedules": t.struct({"_": t.string().optional()}).optional(),
            "maintenancePolicyNames": t.struct({"_": t.string().optional()}).optional(),
            "sloMetadata": t.proxy(
                renames["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut"]
            ).optional(),
            "slmInstanceTemplate": t.string().optional(),
            "name": t.string().optional(),
            "provisionedResources": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn"] = t.struct(
        {
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
            "tier": t.string().optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut"] = t.struct(
        {
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
            "tier": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut"])
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
    types["WeeklyCycleIn"] = t.struct(
        {"schedule": t.array(t.proxy(renames["ScheduleIn"])).optional()}
    ).named(renames["WeeklyCycleIn"])
    types["WeeklyCycleOut"] = t.struct(
        {
            "schedule": t.array(t.proxy(renames["ScheduleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WeeklyCycleOut"])
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn"
    ] = t.struct(
        {
            "maintenancePolicies": t.struct({"_": t.string().optional()}).optional(),
            "exclude": t.boolean().optional(),
            "isRollback": t.boolean().optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut"
    ] = t.struct(
        {
            "maintenancePolicies": t.struct({"_": t.string().optional()}).optional(),
            "exclude": t.boolean().optional(),
            "isRollback": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut"]
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
    types["ListBackupsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "backups": t.array(t.proxy(renames["BackupIn"])).optional(),
        }
    ).named(renames["ListBackupsResponseIn"])
    types["ListBackupsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "backups": t.array(t.proxy(renames["BackupOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBackupsResponseOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn"
    ] = t.struct(
        {
            "canReschedule": t.boolean().optional(),
            "rolloutManagementPolicy": t.string().optional(),
            "scheduleDeadlineTime": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut"
    ] = t.struct(
        {
            "canReschedule": t.boolean().optional(),
            "rolloutManagementPolicy": t.string().optional(),
            "scheduleDeadlineTime": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut"]
    )
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
    types["MaintenancePolicyIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updatePolicy": t.proxy(renames["UpdatePolicyIn"]).optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["MaintenancePolicyIn"])
    types["MaintenancePolicyOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updatePolicy": t.proxy(renames["UpdatePolicyOut"]).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenancePolicyOut"])
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
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["RevertInstanceRequestIn"] = t.struct({"targetSnapshotId": t.string()}).named(
        renames["RevertInstanceRequestIn"]
    )
    types["RevertInstanceRequestOut"] = t.struct(
        {
            "targetSnapshotId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RevertInstanceRequestOut"])
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
    types["BackupIn"] = t.struct(
        {
            "sourceFileShare": t.string().optional(),
            "sourceInstance": t.string().optional(),
            "kmsKey": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["BackupIn"])
    types["BackupOut"] = t.struct(
        {
            "satisfiesPzs": t.boolean().optional(),
            "sourceFileShare": t.string().optional(),
            "capacityGb": t.string().optional(),
            "sourceInstance": t.string().optional(),
            "kmsKey": t.string().optional(),
            "sourceInstanceTier": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "downloadBytes": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "storageBytes": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupOut"])
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
    types["DenyMaintenancePeriodIn"] = t.struct(
        {
            "time": t.proxy(renames["TimeOfDayIn"]).optional(),
            "endDate": t.proxy(renames["DateIn"]).optional(),
            "startDate": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["DenyMaintenancePeriodIn"])
    types["DenyMaintenancePeriodOut"] = t.struct(
        {
            "time": t.proxy(renames["TimeOfDayOut"]).optional(),
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DenyMaintenancePeriodOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["NfsExportOptionsIn"] = t.struct(
        {
            "anonGid": t.string().optional(),
            "anonUid": t.string().optional(),
            "squashMode": t.string().optional(),
            "accessMode": t.string().optional(),
            "ipRanges": t.array(t.string()).optional(),
        }
    ).named(renames["NfsExportOptionsIn"])
    types["NfsExportOptionsOut"] = t.struct(
        {
            "anonGid": t.string().optional(),
            "anonUid": t.string().optional(),
            "squashMode": t.string().optional(),
            "accessMode": t.string().optional(),
            "ipRanges": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NfsExportOptionsOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "statusDetail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
            "networks": t.array(t.proxy(renames["NetworkConfigIn"])).optional(),
            "etag": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "tier": t.string().optional(),
            "fileShares": t.array(t.proxy(renames["FileShareConfigIn"])).optional(),
        }
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "description": t.string().optional(),
            "networks": t.array(t.proxy(renames["NetworkConfigOut"])).optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "suspensionReasons": t.array(t.string()).optional(),
            "createTime": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "statusMessage": t.string().optional(),
            "tier": t.string().optional(),
            "fileShares": t.array(t.proxy(renames["FileShareConfigOut"])).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
    types["UpdatePolicyIn"] = t.struct(
        {
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodIn"])
            ).optional(),
            "channel": t.string().optional(),
            "window": t.proxy(renames["MaintenanceWindowIn"]).optional(),
        }
    ).named(renames["UpdatePolicyIn"])
    types["UpdatePolicyOut"] = t.struct(
        {
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodOut"])
            ).optional(),
            "channel": t.string().optional(),
            "window": t.proxy(renames["MaintenanceWindowOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdatePolicyOut"])
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
            "ipAddresses": t.array(t.string()).optional(),
            "connectMode": t.string().optional(),
            "modes": t.array(t.string()).optional(),
            "network": t.string().optional(),
            "reservedIpRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConfigOut"])
    types["FileShareConfigIn"] = t.struct(
        {
            "sourceBackup": t.string().optional(),
            "nfsExportOptions": t.array(
                t.proxy(renames["NfsExportOptionsIn"])
            ).optional(),
            "capacityGb": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["FileShareConfigIn"])
    types["FileShareConfigOut"] = t.struct(
        {
            "sourceBackup": t.string().optional(),
            "nfsExportOptions": t.array(
                t.proxy(renames["NfsExportOptionsOut"])
            ).optional(),
            "capacityGb": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileShareConfigOut"])
    types["SnapshotIn"] = t.struct(
        {
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SnapshotIn"])
    types["SnapshotOut"] = t.struct(
        {
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "filesystemUsedBytes": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnapshotOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])

    functions = {}
    functions["projectsLocationsGet"] = file.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "includeUnrevealedLocations": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
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
                "name": t.string().optional(),
                "includeUnrevealedLocations": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesList"] = file.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesGet"] = file.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesRestore"] = file.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesPatch"] = file.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesCreate"] = file.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesRevert"] = file.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDelete"] = file.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesSnapshotsPatch"] = file.get(
        "v1/{parent}/snapshots",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSnapshotsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesSnapshotsCreate"] = file.get(
        "v1/{parent}/snapshots",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSnapshotsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesSnapshotsGet"] = file.get(
        "v1/{parent}/snapshots",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSnapshotsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesSnapshotsDelete"] = file.get(
        "v1/{parent}/snapshots",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSnapshotsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesSnapshotsList"] = file.get(
        "v1/{parent}/snapshots",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSnapshotsResponseOut"]),
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
                "sourceInstance": t.string().optional(),
                "kmsKey": t.string().optional(),
                "description": t.string().optional(),
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
                "sourceFileShare": t.string().optional(),
                "sourceInstance": t.string().optional(),
                "kmsKey": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
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
                "sourceInstance": t.string().optional(),
                "kmsKey": t.string().optional(),
                "description": t.string().optional(),
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
                "sourceFileShare": t.string().optional(),
                "sourceInstance": t.string().optional(),
                "kmsKey": t.string().optional(),
                "description": t.string().optional(),
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
                "sourceFileShare": t.string().optional(),
                "sourceInstance": t.string().optional(),
                "kmsKey": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
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

    return Import(
        importer="file", renames=renames, types=Box(types), functions=Box(functions)
    )
