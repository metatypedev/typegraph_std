from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_memcache():
    memcache = HTTPRuntime("https://memcache.googleapis.com/")

    renames = {
        "ErrorResponse": "_memcache_1_ErrorResponse",
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn": "_memcache_2_GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut": "_memcache_3_GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut",
        "OperationMetadataIn": "_memcache_4_OperationMetadataIn",
        "OperationMetadataOut": "_memcache_5_OperationMetadataOut",
        "LocationMetadataIn": "_memcache_6_LocationMetadataIn",
        "LocationMetadataOut": "_memcache_7_LocationMetadataOut",
        "TimeOfDayIn": "_memcache_8_TimeOfDayIn",
        "TimeOfDayOut": "_memcache_9_TimeOfDayOut",
        "MaintenanceWindowIn": "_memcache_10_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_memcache_11_MaintenanceWindowOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn": "_memcache_12_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut": "_memcache_13_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut",
        "MaintenanceScheduleIn": "_memcache_14_MaintenanceScheduleIn",
        "MaintenanceScheduleOut": "_memcache_15_MaintenanceScheduleOut",
        "InstanceMessageIn": "_memcache_16_InstanceMessageIn",
        "InstanceMessageOut": "_memcache_17_InstanceMessageOut",
        "NodeIn": "_memcache_18_NodeIn",
        "NodeOut": "_memcache_19_NodeOut",
        "LocationIn": "_memcache_20_LocationIn",
        "LocationOut": "_memcache_21_LocationOut",
        "GoogleCloudMemcacheV1OperationMetadataIn": "_memcache_22_GoogleCloudMemcacheV1OperationMetadataIn",
        "GoogleCloudMemcacheV1OperationMetadataOut": "_memcache_23_GoogleCloudMemcacheV1OperationMetadataOut",
        "OperationIn": "_memcache_24_OperationIn",
        "OperationOut": "_memcache_25_OperationOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn": "_memcache_26_GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut": "_memcache_27_GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn": "_memcache_28_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut": "_memcache_29_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut",
        "ListLocationsResponseIn": "_memcache_30_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_memcache_31_ListLocationsResponseOut",
        "WeeklyMaintenanceWindowIn": "_memcache_32_WeeklyMaintenanceWindowIn",
        "WeeklyMaintenanceWindowOut": "_memcache_33_WeeklyMaintenanceWindowOut",
        "NodeConfigIn": "_memcache_34_NodeConfigIn",
        "NodeConfigOut": "_memcache_35_NodeConfigOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn": "_memcache_36_GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut": "_memcache_37_GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut",
        "EmptyIn": "_memcache_38_EmptyIn",
        "EmptyOut": "_memcache_39_EmptyOut",
        "GoogleCloudMemcacheV1MaintenancePolicyIn": "_memcache_40_GoogleCloudMemcacheV1MaintenancePolicyIn",
        "GoogleCloudMemcacheV1MaintenancePolicyOut": "_memcache_41_GoogleCloudMemcacheV1MaintenancePolicyOut",
        "WeeklyCycleIn": "_memcache_42_WeeklyCycleIn",
        "WeeklyCycleOut": "_memcache_43_WeeklyCycleOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn": "_memcache_44_GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut": "_memcache_45_GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut",
        "ApplyParametersRequestIn": "_memcache_46_ApplyParametersRequestIn",
        "ApplyParametersRequestOut": "_memcache_47_ApplyParametersRequestOut",
        "InstanceIn": "_memcache_48_InstanceIn",
        "InstanceOut": "_memcache_49_InstanceOut",
        "ListInstancesResponseIn": "_memcache_50_ListInstancesResponseIn",
        "ListInstancesResponseOut": "_memcache_51_ListInstancesResponseOut",
        "RescheduleMaintenanceRequestIn": "_memcache_52_RescheduleMaintenanceRequestIn",
        "RescheduleMaintenanceRequestOut": "_memcache_53_RescheduleMaintenanceRequestOut",
        "UpdatePolicyIn": "_memcache_54_UpdatePolicyIn",
        "UpdatePolicyOut": "_memcache_55_UpdatePolicyOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn": "_memcache_56_GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut": "_memcache_57_GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut",
        "ScheduleIn": "_memcache_58_ScheduleIn",
        "ScheduleOut": "_memcache_59_ScheduleOut",
        "ListOperationsResponseIn": "_memcache_60_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_memcache_61_ListOperationsResponseOut",
        "StatusIn": "_memcache_62_StatusIn",
        "StatusOut": "_memcache_63_StatusOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn": "_memcache_64_GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut": "_memcache_65_GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut",
        "DailyCycleIn": "_memcache_66_DailyCycleIn",
        "DailyCycleOut": "_memcache_67_DailyCycleOut",
        "GoogleCloudMemcacheV1ZoneMetadataIn": "_memcache_68_GoogleCloudMemcacheV1ZoneMetadataIn",
        "GoogleCloudMemcacheV1ZoneMetadataOut": "_memcache_69_GoogleCloudMemcacheV1ZoneMetadataOut",
        "MemcacheParametersIn": "_memcache_70_MemcacheParametersIn",
        "MemcacheParametersOut": "_memcache_71_MemcacheParametersOut",
        "UpdateParametersRequestIn": "_memcache_72_UpdateParametersRequestIn",
        "UpdateParametersRequestOut": "_memcache_73_UpdateParametersRequestOut",
        "CancelOperationRequestIn": "_memcache_74_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_memcache_75_CancelOperationRequestOut",
        "DateIn": "_memcache_76_DateIn",
        "DateOut": "_memcache_77_DateOut",
        "MaintenancePolicyIn": "_memcache_78_MaintenancePolicyIn",
        "MaintenancePolicyOut": "_memcache_79_MaintenancePolicyOut",
        "GoogleCloudMemcacheV1LocationMetadataIn": "_memcache_80_GoogleCloudMemcacheV1LocationMetadataIn",
        "GoogleCloudMemcacheV1LocationMetadataOut": "_memcache_81_GoogleCloudMemcacheV1LocationMetadataOut",
        "DenyMaintenancePeriodIn": "_memcache_82_DenyMaintenancePeriodIn",
        "DenyMaintenancePeriodOut": "_memcache_83_DenyMaintenancePeriodOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn": "_memcache_84_GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut": "_memcache_85_GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut",
        "ZoneMetadataIn": "_memcache_86_ZoneMetadataIn",
        "ZoneMetadataOut": "_memcache_87_ZoneMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "statusDetail": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["LocationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LocationMetadataIn"]
    )
    types["LocationMetadataOut"] = t.struct(
        {
            "availableZones": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationMetadataOut"])
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
    types["MaintenanceScheduleIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MaintenanceScheduleIn"]
    )
    types["MaintenanceScheduleOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "scheduleDeadlineTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceScheduleOut"])
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
    types["NodeIn"] = t.struct(
        {"parameters": t.proxy(renames["MemcacheParametersIn"]).optional()}
    ).named(renames["NodeIn"])
    types["NodeOut"] = t.struct(
        {
            "parameters": t.proxy(renames["MemcacheParametersOut"]).optional(),
            "zone": t.string().optional(),
            "state": t.string().optional(),
            "nodeId": t.string().optional(),
            "port": t.integer().optional(),
            "host": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeOut"])
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["GoogleCloudMemcacheV1OperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudMemcacheV1OperationMetadataIn"])
    types["GoogleCloudMemcacheV1OperationMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "statusDetail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMemcacheV1OperationMetadataOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
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
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn"
    ] = t.struct(
        {
            "scheduleDeadlineTime": t.string().optional(),
            "startTime": t.string().optional(),
            "canReschedule": t.boolean().optional(),
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
            "scheduleDeadlineTime": t.string().optional(),
            "startTime": t.string().optional(),
            "canReschedule": t.boolean().optional(),
            "rolloutManagementPolicy": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut"]
    )
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
    types["WeeklyMaintenanceWindowIn"] = t.struct(
        {
            "day": t.string(),
            "startTime": t.proxy(renames["TimeOfDayIn"]),
            "duration": t.string(),
        }
    ).named(renames["WeeklyMaintenanceWindowIn"])
    types["WeeklyMaintenanceWindowOut"] = t.struct(
        {
            "day": t.string(),
            "startTime": t.proxy(renames["TimeOfDayOut"]),
            "duration": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WeeklyMaintenanceWindowOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["ApplyParametersRequestIn"] = t.struct(
        {"applyAll": t.boolean().optional(), "nodeIds": t.array(t.string()).optional()}
    ).named(renames["ApplyParametersRequestIn"])
    types["ApplyParametersRequestOut"] = t.struct(
        {
            "applyAll": t.boolean().optional(),
            "nodeIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplyParametersRequestOut"])
    types["InstanceIn"] = t.struct(
        {
            "name": t.string(),
            "nodeCount": t.integer(),
            "reservedIpRangeId": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "authorizedNetwork": t.string().optional(),
            "instanceMessages": t.array(
                t.proxy(renames["InstanceMessageIn"])
            ).optional(),
            "parameters": t.proxy(renames["MemcacheParametersIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "zones": t.array(t.string()).optional(),
            "memcacheVersion": t.string().optional(),
            "maintenancePolicy": t.proxy(
                renames["GoogleCloudMemcacheV1MaintenancePolicyIn"]
            ).optional(),
            "nodeConfig": t.proxy(renames["NodeConfigIn"]),
        }
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "maintenanceSchedule": t.proxy(
                renames["MaintenanceScheduleOut"]
            ).optional(),
            "name": t.string(),
            "nodeCount": t.integer(),
            "reservedIpRangeId": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "authorizedNetwork": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "memcacheFullVersion": t.string().optional(),
            "instanceMessages": t.array(
                t.proxy(renames["InstanceMessageOut"])
            ).optional(),
            "parameters": t.proxy(renames["MemcacheParametersOut"]).optional(),
            "discoveryEndpoint": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "zones": t.array(t.string()).optional(),
            "memcacheVersion": t.string().optional(),
            "maintenancePolicy": t.proxy(
                renames["GoogleCloudMemcacheV1MaintenancePolicyOut"]
            ).optional(),
            "nodeConfig": t.proxy(renames["NodeConfigOut"]),
            "memcacheNodes": t.array(t.proxy(renames["NodeOut"])).optional(),
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
    types["RescheduleMaintenanceRequestIn"] = t.struct(
        {"rescheduleType": t.string(), "scheduleTime": t.string().optional()}
    ).named(renames["RescheduleMaintenanceRequestIn"])
    types["RescheduleMaintenanceRequestOut"] = t.struct(
        {
            "rescheduleType": t.string(),
            "scheduleTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RescheduleMaintenanceRequestOut"])
    types["UpdatePolicyIn"] = t.struct(
        {
            "window": t.proxy(renames["MaintenanceWindowIn"]).optional(),
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodIn"])
            ).optional(),
            "channel": t.string().optional(),
        }
    ).named(renames["UpdatePolicyIn"])
    types["UpdatePolicyOut"] = t.struct(
        {
            "window": t.proxy(renames["MaintenanceWindowOut"]).optional(),
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodOut"])
            ).optional(),
            "channel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdatePolicyOut"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn"] = t.struct(
        {
            "maintenanceSettings": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn"
                ]
            ).optional(),
            "maintenanceSchedules": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "notificationParameters": t.struct({"_": t.string().optional()}).optional(),
            "slmInstanceTemplate": t.string().optional(),
            "instanceType": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "consumerDefinedName": t.string().optional(),
            "softwareVersions": t.struct({"_": t.string().optional()}).optional(),
            "maintenancePolicyNames": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut"] = t.struct(
        {
            "maintenanceSettings": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut"
                ]
            ).optional(),
            "maintenanceSchedules": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "notificationParameters": t.struct({"_": t.string().optional()}).optional(),
            "slmInstanceTemplate": t.string().optional(),
            "tenantProjectId": t.string().optional(),
            "instanceType": t.string().optional(),
            "updateTime": t.string().optional(),
            "producerMetadata": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "sloMetadata": t.proxy(
                renames["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut"]
            ).optional(),
            "provisionedResources": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut"
                    ]
                )
            ).optional(),
            "createTime": t.string().optional(),
            "consumerDefinedName": t.string().optional(),
            "softwareVersions": t.struct({"_": t.string().optional()}).optional(),
            "maintenancePolicyNames": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut"])
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
    types["GoogleCloudMemcacheV1ZoneMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudMemcacheV1ZoneMetadataIn"])
    types["GoogleCloudMemcacheV1ZoneMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudMemcacheV1ZoneMetadataOut"])
    types["MemcacheParametersIn"] = t.struct(
        {"params": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["MemcacheParametersIn"])
    types["MemcacheParametersOut"] = t.struct(
        {
            "id": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemcacheParametersOut"])
    types["UpdateParametersRequestIn"] = t.struct(
        {
            "parameters": t.proxy(renames["MemcacheParametersIn"]).optional(),
            "updateMask": t.string(),
        }
    ).named(renames["UpdateParametersRequestIn"])
    types["UpdateParametersRequestOut"] = t.struct(
        {
            "parameters": t.proxy(renames["MemcacheParametersOut"]).optional(),
            "updateMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateParametersRequestOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["MaintenancePolicyIn"] = t.struct(
        {
            "description": t.string().optional(),
            "updatePolicy": t.proxy(renames["UpdatePolicyIn"]).optional(),
            "name": t.string(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["MaintenancePolicyIn"])
    types["MaintenancePolicyOut"] = t.struct(
        {
            "description": t.string().optional(),
            "updatePolicy": t.proxy(renames["UpdatePolicyOut"]).optional(),
            "name": t.string(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenancePolicyOut"])
    types["GoogleCloudMemcacheV1LocationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudMemcacheV1LocationMetadataIn"])
    types["GoogleCloudMemcacheV1LocationMetadataOut"] = t.struct(
        {
            "availableZones": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMemcacheV1LocationMetadataOut"])
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
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn"
    ] = t.struct(
        {
            "perSliEligibility": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn"
                ]
            ).optional(),
            "location": t.string().optional(),
            "nodeId": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut"
    ] = t.struct(
        {
            "perSliEligibility": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut"
                ]
            ).optional(),
            "location": t.string().optional(),
            "nodeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut"]
    )
    types["ZoneMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ZoneMetadataIn"]
    )
    types["ZoneMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ZoneMetadataOut"])

    functions = {}
    functions["projectsLocationsGet"] = memcache.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = memcache.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = memcache.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = memcache.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = memcache.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesApplyParameters"] = memcache.post(
        "v1/{instance}:rescheduleMaintenance",
        t.struct(
            {
                "instance": t.string(),
                "rescheduleType": t.string(),
                "scheduleTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesCreate"] = memcache.post(
        "v1/{instance}:rescheduleMaintenance",
        t.struct(
            {
                "instance": t.string(),
                "rescheduleType": t.string(),
                "scheduleTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesUpdateParameters"] = memcache.post(
        "v1/{instance}:rescheduleMaintenance",
        t.struct(
            {
                "instance": t.string(),
                "rescheduleType": t.string(),
                "scheduleTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesList"] = memcache.post(
        "v1/{instance}:rescheduleMaintenance",
        t.struct(
            {
                "instance": t.string(),
                "rescheduleType": t.string(),
                "scheduleTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesGet"] = memcache.post(
        "v1/{instance}:rescheduleMaintenance",
        t.struct(
            {
                "instance": t.string(),
                "rescheduleType": t.string(),
                "scheduleTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDelete"] = memcache.post(
        "v1/{instance}:rescheduleMaintenance",
        t.struct(
            {
                "instance": t.string(),
                "rescheduleType": t.string(),
                "scheduleTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesPatch"] = memcache.post(
        "v1/{instance}:rescheduleMaintenance",
        t.struct(
            {
                "instance": t.string(),
                "rescheduleType": t.string(),
                "scheduleTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesRescheduleMaintenance"] = memcache.post(
        "v1/{instance}:rescheduleMaintenance",
        t.struct(
            {
                "instance": t.string(),
                "rescheduleType": t.string(),
                "scheduleTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="memcache", renames=renames, types=Box(types), functions=Box(functions)
    )
