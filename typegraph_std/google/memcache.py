from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_memcache() -> Import:
    memcache = HTTPRuntime("https://memcache.googleapis.com/")

    renames = {
        "ErrorResponse": "_memcache_1_ErrorResponse",
        "ZoneMetadataIn": "_memcache_2_ZoneMetadataIn",
        "ZoneMetadataOut": "_memcache_3_ZoneMetadataOut",
        "ListOperationsResponseIn": "_memcache_4_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_memcache_5_ListOperationsResponseOut",
        "GoogleCloudMemcacheV1ZoneMetadataIn": "_memcache_6_GoogleCloudMemcacheV1ZoneMetadataIn",
        "GoogleCloudMemcacheV1ZoneMetadataOut": "_memcache_7_GoogleCloudMemcacheV1ZoneMetadataOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn": "_memcache_8_GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut": "_memcache_9_GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn": "_memcache_10_GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut": "_memcache_11_GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut",
        "NodeIn": "_memcache_12_NodeIn",
        "NodeOut": "_memcache_13_NodeOut",
        "ApplyParametersRequestIn": "_memcache_14_ApplyParametersRequestIn",
        "ApplyParametersRequestOut": "_memcache_15_ApplyParametersRequestOut",
        "ScheduleIn": "_memcache_16_ScheduleIn",
        "ScheduleOut": "_memcache_17_ScheduleOut",
        "MemcacheParametersIn": "_memcache_18_MemcacheParametersIn",
        "MemcacheParametersOut": "_memcache_19_MemcacheParametersOut",
        "NodeConfigIn": "_memcache_20_NodeConfigIn",
        "NodeConfigOut": "_memcache_21_NodeConfigOut",
        "WeeklyCycleIn": "_memcache_22_WeeklyCycleIn",
        "WeeklyCycleOut": "_memcache_23_WeeklyCycleOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn": "_memcache_24_GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut": "_memcache_25_GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn": "_memcache_26_GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut": "_memcache_27_GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut",
        "MaintenanceScheduleIn": "_memcache_28_MaintenanceScheduleIn",
        "MaintenanceScheduleOut": "_memcache_29_MaintenanceScheduleOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn": "_memcache_30_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut": "_memcache_31_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut",
        "DailyCycleIn": "_memcache_32_DailyCycleIn",
        "DailyCycleOut": "_memcache_33_DailyCycleOut",
        "GoogleCloudMemcacheV1OperationMetadataIn": "_memcache_34_GoogleCloudMemcacheV1OperationMetadataIn",
        "GoogleCloudMemcacheV1OperationMetadataOut": "_memcache_35_GoogleCloudMemcacheV1OperationMetadataOut",
        "ListLocationsResponseIn": "_memcache_36_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_memcache_37_ListLocationsResponseOut",
        "EmptyIn": "_memcache_38_EmptyIn",
        "EmptyOut": "_memcache_39_EmptyOut",
        "LocationMetadataIn": "_memcache_40_LocationMetadataIn",
        "LocationMetadataOut": "_memcache_41_LocationMetadataOut",
        "UpdateParametersRequestIn": "_memcache_42_UpdateParametersRequestIn",
        "UpdateParametersRequestOut": "_memcache_43_UpdateParametersRequestOut",
        "GoogleCloudMemcacheV1LocationMetadataIn": "_memcache_44_GoogleCloudMemcacheV1LocationMetadataIn",
        "GoogleCloudMemcacheV1LocationMetadataOut": "_memcache_45_GoogleCloudMemcacheV1LocationMetadataOut",
        "CancelOperationRequestIn": "_memcache_46_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_memcache_47_CancelOperationRequestOut",
        "DenyMaintenancePeriodIn": "_memcache_48_DenyMaintenancePeriodIn",
        "DenyMaintenancePeriodOut": "_memcache_49_DenyMaintenancePeriodOut",
        "TimeOfDayIn": "_memcache_50_TimeOfDayIn",
        "TimeOfDayOut": "_memcache_51_TimeOfDayOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn": "_memcache_52_GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut": "_memcache_53_GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut",
        "GoogleCloudMemcacheV1MaintenancePolicyIn": "_memcache_54_GoogleCloudMemcacheV1MaintenancePolicyIn",
        "GoogleCloudMemcacheV1MaintenancePolicyOut": "_memcache_55_GoogleCloudMemcacheV1MaintenancePolicyOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn": "_memcache_56_GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut": "_memcache_57_GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn": "_memcache_58_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut": "_memcache_59_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut",
        "DateIn": "_memcache_60_DateIn",
        "DateOut": "_memcache_61_DateOut",
        "LocationIn": "_memcache_62_LocationIn",
        "LocationOut": "_memcache_63_LocationOut",
        "OperationIn": "_memcache_64_OperationIn",
        "OperationOut": "_memcache_65_OperationOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn": "_memcache_66_GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut": "_memcache_67_GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut",
        "UpdatePolicyIn": "_memcache_68_UpdatePolicyIn",
        "UpdatePolicyOut": "_memcache_69_UpdatePolicyOut",
        "InstanceMessageIn": "_memcache_70_InstanceMessageIn",
        "InstanceMessageOut": "_memcache_71_InstanceMessageOut",
        "RescheduleMaintenanceRequestIn": "_memcache_72_RescheduleMaintenanceRequestIn",
        "RescheduleMaintenanceRequestOut": "_memcache_73_RescheduleMaintenanceRequestOut",
        "WeeklyMaintenanceWindowIn": "_memcache_74_WeeklyMaintenanceWindowIn",
        "WeeklyMaintenanceWindowOut": "_memcache_75_WeeklyMaintenanceWindowOut",
        "StatusIn": "_memcache_76_StatusIn",
        "StatusOut": "_memcache_77_StatusOut",
        "MaintenanceWindowIn": "_memcache_78_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_memcache_79_MaintenanceWindowOut",
        "OperationMetadataIn": "_memcache_80_OperationMetadataIn",
        "OperationMetadataOut": "_memcache_81_OperationMetadataOut",
        "InstanceIn": "_memcache_82_InstanceIn",
        "InstanceOut": "_memcache_83_InstanceOut",
        "ListInstancesResponseIn": "_memcache_84_ListInstancesResponseIn",
        "ListInstancesResponseOut": "_memcache_85_ListInstancesResponseOut",
        "MaintenancePolicyIn": "_memcache_86_MaintenancePolicyIn",
        "MaintenancePolicyOut": "_memcache_87_MaintenancePolicyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ZoneMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ZoneMetadataIn"]
    )
    types["ZoneMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ZoneMetadataOut"])
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
    types["GoogleCloudMemcacheV1ZoneMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudMemcacheV1ZoneMetadataIn"])
    types["GoogleCloudMemcacheV1ZoneMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudMemcacheV1ZoneMetadataOut"])
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
    types["GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn"] = t.struct(
        {
            "consumerDefinedName": t.string().optional(),
            "slmInstanceTemplate": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "instanceType": t.string().optional(),
            "maintenancePolicyNames": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "maintenanceSchedules": t.struct({"_": t.string().optional()}).optional(),
            "maintenanceSettings": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn"
                ]
            ).optional(),
            "notificationParameters": t.struct({"_": t.string().optional()}).optional(),
            "softwareVersions": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut"] = t.struct(
        {
            "consumerDefinedName": t.string().optional(),
            "producerMetadata": t.struct({"_": t.string().optional()}).optional(),
            "slmInstanceTemplate": t.string().optional(),
            "provisionedResources": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut"
                    ]
                )
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "instanceType": t.string().optional(),
            "sloMetadata": t.proxy(
                renames["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut"]
            ).optional(),
            "maintenancePolicyNames": t.struct({"_": t.string().optional()}).optional(),
            "tenantProjectId": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "maintenanceSchedules": t.struct({"_": t.string().optional()}).optional(),
            "maintenanceSettings": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut"
                ]
            ).optional(),
            "notificationParameters": t.struct({"_": t.string().optional()}).optional(),
            "softwareVersions": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut"])
    types["NodeIn"] = t.struct(
        {"parameters": t.proxy(renames["MemcacheParametersIn"]).optional()}
    ).named(renames["NodeIn"])
    types["NodeOut"] = t.struct(
        {
            "parameters": t.proxy(renames["MemcacheParametersOut"]).optional(),
            "state": t.string().optional(),
            "nodeId": t.string().optional(),
            "host": t.string().optional(),
            "zone": t.string().optional(),
            "port": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeOut"])
    types["ApplyParametersRequestIn"] = t.struct(
        {"nodeIds": t.array(t.string()).optional(), "applyAll": t.boolean().optional()}
    ).named(renames["ApplyParametersRequestIn"])
    types["ApplyParametersRequestOut"] = t.struct(
        {
            "nodeIds": t.array(t.string()).optional(),
            "applyAll": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplyParametersRequestOut"])
    types["ScheduleIn"] = t.struct(
        {
            "duration": t.string().optional(),
            "day": t.string().optional(),
            "startTime": t.proxy(renames["TimeOfDayIn"]).optional(),
        }
    ).named(renames["ScheduleIn"])
    types["ScheduleOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "day": t.string().optional(),
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduleOut"])
    types["MemcacheParametersIn"] = t.struct(
        {"params": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["MemcacheParametersIn"])
    types["MemcacheParametersOut"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemcacheParametersOut"])
    types["NodeConfigIn"] = t.struct(
        {"memorySizeMb": t.integer(), "cpuCount": t.integer()}
    ).named(renames["NodeConfigIn"])
    types["NodeConfigOut"] = t.struct(
        {
            "memorySizeMb": t.integer(),
            "cpuCount": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeConfigOut"])
    types["WeeklyCycleIn"] = t.struct(
        {"schedule": t.array(t.proxy(renames["ScheduleIn"])).optional()}
    ).named(renames["WeeklyCycleIn"])
    types["WeeklyCycleOut"] = t.struct(
        {
            "schedule": t.array(t.proxy(renames["ScheduleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WeeklyCycleOut"])
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
    types["MaintenanceScheduleIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MaintenanceScheduleIn"]
    )
    types["MaintenanceScheduleOut"] = t.struct(
        {
            "scheduleDeadlineTime": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceScheduleOut"])
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn"
    ] = t.struct(
        {
            "canReschedule": t.boolean().optional(),
            "startTime": t.string().optional(),
            "scheduleDeadlineTime": t.string().optional(),
            "rolloutManagementPolicy": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut"
    ] = t.struct(
        {
            "canReschedule": t.boolean().optional(),
            "startTime": t.string().optional(),
            "scheduleDeadlineTime": t.string().optional(),
            "rolloutManagementPolicy": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut"]
    )
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
    types["GoogleCloudMemcacheV1OperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudMemcacheV1OperationMetadataIn"])
    types["GoogleCloudMemcacheV1OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "statusDetail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMemcacheV1OperationMetadataOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["LocationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LocationMetadataIn"]
    )
    types["LocationMetadataOut"] = t.struct(
        {
            "availableZones": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationMetadataOut"])
    types["UpdateParametersRequestIn"] = t.struct(
        {
            "updateMask": t.string(),
            "parameters": t.proxy(renames["MemcacheParametersIn"]).optional(),
        }
    ).named(renames["UpdateParametersRequestIn"])
    types["UpdateParametersRequestOut"] = t.struct(
        {
            "updateMask": t.string(),
            "parameters": t.proxy(renames["MemcacheParametersOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateParametersRequestOut"])
    types["GoogleCloudMemcacheV1LocationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudMemcacheV1LocationMetadataIn"])
    types["GoogleCloudMemcacheV1LocationMetadataOut"] = t.struct(
        {
            "availableZones": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMemcacheV1LocationMetadataOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["TimeOfDayIn"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn"] = t.struct(
        {"eligible": t.boolean().optional(), "reason": t.string().optional()}
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn"])
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut"
    ] = t.struct(
        {
            "eligible": t.boolean().optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut"]
    )
    types["GoogleCloudMemcacheV1MaintenancePolicyIn"] = t.struct(
        {
            "weeklyMaintenanceWindow": t.array(
                t.proxy(renames["WeeklyMaintenanceWindowIn"])
            ),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudMemcacheV1MaintenancePolicyIn"])
    types["GoogleCloudMemcacheV1MaintenancePolicyOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "weeklyMaintenanceWindow": t.array(
                t.proxy(renames["WeeklyMaintenanceWindowOut"])
            ),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMemcacheV1MaintenancePolicyOut"])
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
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn"
    ] = t.struct(
        {
            "isRollback": t.boolean().optional(),
            "maintenancePolicies": t.struct({"_": t.string().optional()}).optional(),
            "exclude": t.boolean().optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut"
    ] = t.struct(
        {
            "isRollback": t.boolean().optional(),
            "maintenancePolicies": t.struct({"_": t.string().optional()}).optional(),
            "exclude": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut"]
    )
    types["DateIn"] = t.struct(
        {
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["UpdatePolicyIn"] = t.struct(
        {
            "channel": t.string().optional(),
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodIn"])
            ).optional(),
            "window": t.proxy(renames["MaintenanceWindowIn"]).optional(),
        }
    ).named(renames["UpdatePolicyIn"])
    types["UpdatePolicyOut"] = t.struct(
        {
            "channel": t.string().optional(),
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodOut"])
            ).optional(),
            "window": t.proxy(renames["MaintenanceWindowOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdatePolicyOut"])
    types["InstanceMessageIn"] = t.struct(
        {"code": t.string().optional(), "message": t.string().optional()}
    ).named(renames["InstanceMessageIn"])
    types["InstanceMessageOut"] = t.struct(
        {
            "code": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceMessageOut"])
    types["RescheduleMaintenanceRequestIn"] = t.struct(
        {"scheduleTime": t.string().optional(), "rescheduleType": t.string()}
    ).named(renames["RescheduleMaintenanceRequestIn"])
    types["RescheduleMaintenanceRequestOut"] = t.struct(
        {
            "scheduleTime": t.string().optional(),
            "rescheduleType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RescheduleMaintenanceRequestOut"])
    types["WeeklyMaintenanceWindowIn"] = t.struct(
        {
            "startTime": t.proxy(renames["TimeOfDayIn"]),
            "day": t.string(),
            "duration": t.string(),
        }
    ).named(renames["WeeklyMaintenanceWindowIn"])
    types["WeeklyMaintenanceWindowOut"] = t.struct(
        {
            "startTime": t.proxy(renames["TimeOfDayOut"]),
            "day": t.string(),
            "duration": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WeeklyMaintenanceWindowOut"])
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
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "statusDetail": t.string().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["InstanceIn"] = t.struct(
        {
            "zones": t.array(t.string()).optional(),
            "nodeConfig": t.proxy(renames["NodeConfigIn"]),
            "displayName": t.string().optional(),
            "nodeCount": t.integer(),
            "name": t.string(),
            "memcacheVersion": t.string().optional(),
            "maintenancePolicy": t.proxy(
                renames["GoogleCloudMemcacheV1MaintenancePolicyIn"]
            ).optional(),
            "authorizedNetwork": t.string().optional(),
            "parameters": t.proxy(renames["MemcacheParametersIn"]).optional(),
            "instanceMessages": t.array(
                t.proxy(renames["InstanceMessageIn"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "zones": t.array(t.string()).optional(),
            "nodeConfig": t.proxy(renames["NodeConfigOut"]),
            "displayName": t.string().optional(),
            "memcacheFullVersion": t.string().optional(),
            "nodeCount": t.integer(),
            "memcacheNodes": t.array(t.proxy(renames["NodeOut"])).optional(),
            "name": t.string(),
            "memcacheVersion": t.string().optional(),
            "maintenancePolicy": t.proxy(
                renames["GoogleCloudMemcacheV1MaintenancePolicyOut"]
            ).optional(),
            "maintenanceSchedule": t.proxy(
                renames["MaintenanceScheduleOut"]
            ).optional(),
            "authorizedNetwork": t.string().optional(),
            "parameters": t.proxy(renames["MemcacheParametersOut"]).optional(),
            "instanceMessages": t.array(
                t.proxy(renames["InstanceMessageOut"])
            ).optional(),
            "state": t.string().optional(),
            "discoveryEndpoint": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
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
    types["MaintenancePolicyIn"] = t.struct(
        {
            "name": t.string(),
            "updatePolicy": t.proxy(renames["UpdatePolicyIn"]).optional(),
            "state": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["MaintenancePolicyIn"])
    types["MaintenancePolicyOut"] = t.struct(
        {
            "name": t.string(),
            "updatePolicy": t.proxy(renames["UpdatePolicyOut"]).optional(),
            "state": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenancePolicyOut"])

    functions = {}
    functions["projectsLocationsGet"] = memcache.get(
        "v1/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = memcache.get(
        "v1/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = memcache.post(
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
    functions["projectsLocationsOperationsList"] = memcache.post(
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
    functions["projectsLocationsOperationsDelete"] = memcache.post(
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
    functions["projectsLocationsOperationsCancel"] = memcache.post(
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
    functions["projectsLocationsInstancesRescheduleMaintenance"] = memcache.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesPatch"] = memcache.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesCreate"] = memcache.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesGet"] = memcache.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDelete"] = memcache.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesApplyParameters"] = memcache.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesUpdateParameters"] = memcache.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesList"] = memcache.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="memcache", renames=renames, types=types, functions=functions
    )
