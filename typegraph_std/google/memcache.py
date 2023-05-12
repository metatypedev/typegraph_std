from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_memcache() -> Import:
    memcache = HTTPRuntime("https://memcache.googleapis.com/")

    renames = {
        "ErrorResponse": "_memcache_1_ErrorResponse",
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn": "_memcache_2_GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut": "_memcache_3_GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut",
        "MaintenancePolicyIn": "_memcache_4_MaintenancePolicyIn",
        "MaintenancePolicyOut": "_memcache_5_MaintenancePolicyOut",
        "InstanceIn": "_memcache_6_InstanceIn",
        "InstanceOut": "_memcache_7_InstanceOut",
        "GoogleCloudMemcacheV1LocationMetadataIn": "_memcache_8_GoogleCloudMemcacheV1LocationMetadataIn",
        "GoogleCloudMemcacheV1LocationMetadataOut": "_memcache_9_GoogleCloudMemcacheV1LocationMetadataOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn": "_memcache_10_GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut": "_memcache_11_GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut",
        "GoogleCloudMemcacheV1ZoneMetadataIn": "_memcache_12_GoogleCloudMemcacheV1ZoneMetadataIn",
        "GoogleCloudMemcacheV1ZoneMetadataOut": "_memcache_13_GoogleCloudMemcacheV1ZoneMetadataOut",
        "WeeklyMaintenanceWindowIn": "_memcache_14_WeeklyMaintenanceWindowIn",
        "WeeklyMaintenanceWindowOut": "_memcache_15_WeeklyMaintenanceWindowOut",
        "UpdatePolicyIn": "_memcache_16_UpdatePolicyIn",
        "UpdatePolicyOut": "_memcache_17_UpdatePolicyOut",
        "GoogleCloudMemcacheV1MaintenancePolicyIn": "_memcache_18_GoogleCloudMemcacheV1MaintenancePolicyIn",
        "GoogleCloudMemcacheV1MaintenancePolicyOut": "_memcache_19_GoogleCloudMemcacheV1MaintenancePolicyOut",
        "DateIn": "_memcache_20_DateIn",
        "DateOut": "_memcache_21_DateOut",
        "MaintenanceWindowIn": "_memcache_22_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_memcache_23_MaintenanceWindowOut",
        "RescheduleMaintenanceRequestIn": "_memcache_24_RescheduleMaintenanceRequestIn",
        "RescheduleMaintenanceRequestOut": "_memcache_25_RescheduleMaintenanceRequestOut",
        "TimeOfDayIn": "_memcache_26_TimeOfDayIn",
        "TimeOfDayOut": "_memcache_27_TimeOfDayOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn": "_memcache_28_GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut": "_memcache_29_GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut",
        "ListOperationsResponseIn": "_memcache_30_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_memcache_31_ListOperationsResponseOut",
        "EmptyIn": "_memcache_32_EmptyIn",
        "EmptyOut": "_memcache_33_EmptyOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn": "_memcache_34_GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut": "_memcache_35_GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut",
        "WeeklyCycleIn": "_memcache_36_WeeklyCycleIn",
        "WeeklyCycleOut": "_memcache_37_WeeklyCycleOut",
        "ScheduleIn": "_memcache_38_ScheduleIn",
        "ScheduleOut": "_memcache_39_ScheduleOut",
        "NodeIn": "_memcache_40_NodeIn",
        "NodeOut": "_memcache_41_NodeOut",
        "ListInstancesResponseIn": "_memcache_42_ListInstancesResponseIn",
        "ListInstancesResponseOut": "_memcache_43_ListInstancesResponseOut",
        "OperationMetadataIn": "_memcache_44_OperationMetadataIn",
        "OperationMetadataOut": "_memcache_45_OperationMetadataOut",
        "ApplyParametersRequestIn": "_memcache_46_ApplyParametersRequestIn",
        "ApplyParametersRequestOut": "_memcache_47_ApplyParametersRequestOut",
        "DailyCycleIn": "_memcache_48_DailyCycleIn",
        "DailyCycleOut": "_memcache_49_DailyCycleOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn": "_memcache_50_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut": "_memcache_51_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut",
        "GoogleCloudMemcacheV1OperationMetadataIn": "_memcache_52_GoogleCloudMemcacheV1OperationMetadataIn",
        "GoogleCloudMemcacheV1OperationMetadataOut": "_memcache_53_GoogleCloudMemcacheV1OperationMetadataOut",
        "ListLocationsResponseIn": "_memcache_54_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_memcache_55_ListLocationsResponseOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn": "_memcache_56_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut": "_memcache_57_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut",
        "UpdateParametersRequestIn": "_memcache_58_UpdateParametersRequestIn",
        "UpdateParametersRequestOut": "_memcache_59_UpdateParametersRequestOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn": "_memcache_60_GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut": "_memcache_61_GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut",
        "NodeConfigIn": "_memcache_62_NodeConfigIn",
        "NodeConfigOut": "_memcache_63_NodeConfigOut",
        "LocationMetadataIn": "_memcache_64_LocationMetadataIn",
        "LocationMetadataOut": "_memcache_65_LocationMetadataOut",
        "MaintenanceScheduleIn": "_memcache_66_MaintenanceScheduleIn",
        "MaintenanceScheduleOut": "_memcache_67_MaintenanceScheduleOut",
        "OperationIn": "_memcache_68_OperationIn",
        "OperationOut": "_memcache_69_OperationOut",
        "CancelOperationRequestIn": "_memcache_70_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_memcache_71_CancelOperationRequestOut",
        "LocationIn": "_memcache_72_LocationIn",
        "LocationOut": "_memcache_73_LocationOut",
        "DenyMaintenancePeriodIn": "_memcache_74_DenyMaintenancePeriodIn",
        "DenyMaintenancePeriodOut": "_memcache_75_DenyMaintenancePeriodOut",
        "ZoneMetadataIn": "_memcache_76_ZoneMetadataIn",
        "ZoneMetadataOut": "_memcache_77_ZoneMetadataOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn": "_memcache_78_GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut": "_memcache_79_GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn": "_memcache_80_GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut": "_memcache_81_GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut",
        "InstanceMessageIn": "_memcache_82_InstanceMessageIn",
        "InstanceMessageOut": "_memcache_83_InstanceMessageOut",
        "MemcacheParametersIn": "_memcache_84_MemcacheParametersIn",
        "MemcacheParametersOut": "_memcache_85_MemcacheParametersOut",
        "StatusIn": "_memcache_86_StatusIn",
        "StatusOut": "_memcache_87_StatusOut",
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
    types["MaintenancePolicyIn"] = t.struct(
        {
            "state": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updatePolicy": t.proxy(renames["UpdatePolicyIn"]).optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["MaintenancePolicyIn"])
    types["MaintenancePolicyOut"] = t.struct(
        {
            "state": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updatePolicy": t.proxy(renames["UpdatePolicyOut"]).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenancePolicyOut"])
    types["InstanceIn"] = t.struct(
        {
            "memcacheVersion": t.string().optional(),
            "name": t.string(),
            "displayName": t.string().optional(),
            "parameters": t.proxy(renames["MemcacheParametersIn"]).optional(),
            "nodeConfig": t.proxy(renames["NodeConfigIn"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "instanceMessages": t.array(
                t.proxy(renames["InstanceMessageIn"])
            ).optional(),
            "nodeCount": t.integer(),
            "zones": t.array(t.string()).optional(),
            "authorizedNetwork": t.string().optional(),
            "maintenancePolicy": t.proxy(
                renames["GoogleCloudMemcacheV1MaintenancePolicyIn"]
            ).optional(),
        }
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "memcacheVersion": t.string().optional(),
            "maintenanceSchedule": t.proxy(
                renames["MaintenanceScheduleOut"]
            ).optional(),
            "name": t.string(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "memcacheFullVersion": t.string().optional(),
            "parameters": t.proxy(renames["MemcacheParametersOut"]).optional(),
            "updateTime": t.string().optional(),
            "nodeConfig": t.proxy(renames["NodeConfigOut"]),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "memcacheNodes": t.array(t.proxy(renames["NodeOut"])).optional(),
            "instanceMessages": t.array(
                t.proxy(renames["InstanceMessageOut"])
            ).optional(),
            "nodeCount": t.integer(),
            "zones": t.array(t.string()).optional(),
            "authorizedNetwork": t.string().optional(),
            "maintenancePolicy": t.proxy(
                renames["GoogleCloudMemcacheV1MaintenancePolicyOut"]
            ).optional(),
            "discoveryEndpoint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
    types["GoogleCloudMemcacheV1LocationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudMemcacheV1LocationMetadataIn"])
    types["GoogleCloudMemcacheV1LocationMetadataOut"] = t.struct(
        {
            "availableZones": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMemcacheV1LocationMetadataOut"])
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
    types["GoogleCloudMemcacheV1ZoneMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudMemcacheV1ZoneMetadataIn"])
    types["GoogleCloudMemcacheV1ZoneMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudMemcacheV1ZoneMetadataOut"])
    types["WeeklyMaintenanceWindowIn"] = t.struct(
        {
            "duration": t.string(),
            "startTime": t.proxy(renames["TimeOfDayIn"]),
            "day": t.string(),
        }
    ).named(renames["WeeklyMaintenanceWindowIn"])
    types["WeeklyMaintenanceWindowOut"] = t.struct(
        {
            "duration": t.string(),
            "startTime": t.proxy(renames["TimeOfDayOut"]),
            "day": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WeeklyMaintenanceWindowOut"])
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
            "weeklyMaintenanceWindow": t.array(
                t.proxy(renames["WeeklyMaintenanceWindowOut"])
            ),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMemcacheV1MaintenancePolicyOut"])
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
    types["TimeOfDayIn"] = t.struct(
        {
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
            "hours": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
            "hours": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn"] = t.struct(
        {
            "instanceType": t.string().optional(),
            "notificationParameters": t.struct({"_": t.string().optional()}).optional(),
            "softwareVersions": t.struct({"_": t.string().optional()}).optional(),
            "maintenanceSchedules": t.struct({"_": t.string().optional()}).optional(),
            "consumerDefinedName": t.string().optional(),
            "maintenanceSettings": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn"
                ]
            ).optional(),
            "maintenancePolicyNames": t.struct({"_": t.string().optional()}).optional(),
            "slmInstanceTemplate": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut"] = t.struct(
        {
            "instanceType": t.string().optional(),
            "notificationParameters": t.struct({"_": t.string().optional()}).optional(),
            "tenantProjectId": t.string().optional(),
            "softwareVersions": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "producerMetadata": t.struct({"_": t.string().optional()}).optional(),
            "maintenanceSchedules": t.struct({"_": t.string().optional()}).optional(),
            "consumerDefinedName": t.string().optional(),
            "createTime": t.string().optional(),
            "maintenanceSettings": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut"
                ]
            ).optional(),
            "updateTime": t.string().optional(),
            "provisionedResources": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut"
                    ]
                )
            ).optional(),
            "maintenancePolicyNames": t.struct({"_": t.string().optional()}).optional(),
            "slmInstanceTemplate": t.string().optional(),
            "name": t.string().optional(),
            "sloMetadata": t.proxy(
                renames["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
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
    types["ScheduleIn"] = t.struct(
        {
            "startTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "day": t.string().optional(),
            "duration": t.string().optional(),
        }
    ).named(renames["ScheduleIn"])
    types["ScheduleOut"] = t.struct(
        {
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "day": t.string().optional(),
            "duration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduleOut"])
    types["NodeIn"] = t.struct(
        {"parameters": t.proxy(renames["MemcacheParametersIn"]).optional()}
    ).named(renames["NodeIn"])
    types["NodeOut"] = t.struct(
        {
            "port": t.integer().optional(),
            "state": t.string().optional(),
            "parameters": t.proxy(renames["MemcacheParametersOut"]).optional(),
            "host": t.string().optional(),
            "zone": t.string().optional(),
            "nodeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeOut"])
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
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "target": t.string().optional(),
            "statusDetail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn"
    ] = t.struct(
        {
            "scheduleDeadlineTime": t.string().optional(),
            "startTime": t.string().optional(),
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
            "scheduleDeadlineTime": t.string().optional(),
            "startTime": t.string().optional(),
            "rolloutManagementPolicy": t.string().optional(),
            "endTime": t.string().optional(),
            "canReschedule": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut"]
    )
    types["GoogleCloudMemcacheV1OperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudMemcacheV1OperationMetadataIn"])
    types["GoogleCloudMemcacheV1OperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "statusDetail": t.string().optional(),
            "endTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMemcacheV1OperationMetadataOut"])
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
    types["NodeConfigIn"] = t.struct(
        {"cpuCount": t.integer(), "memorySizeMb": t.integer()}
    ).named(renames["NodeConfigIn"])
    types["NodeConfigOut"] = t.struct(
        {
            "cpuCount": t.integer(),
            "memorySizeMb": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeConfigOut"])
    types["LocationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LocationMetadataIn"]
    )
    types["LocationMetadataOut"] = t.struct(
        {
            "availableZones": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationMetadataOut"])
    types["MaintenanceScheduleIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MaintenanceScheduleIn"]
    )
    types["MaintenanceScheduleOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "scheduleDeadlineTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceScheduleOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["DenyMaintenancePeriodIn"] = t.struct(
        {
            "endDate": t.proxy(renames["DateIn"]).optional(),
            "startDate": t.proxy(renames["DateIn"]).optional(),
            "time": t.proxy(renames["TimeOfDayIn"]).optional(),
        }
    ).named(renames["DenyMaintenancePeriodIn"])
    types["DenyMaintenancePeriodOut"] = t.struct(
        {
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "time": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DenyMaintenancePeriodOut"])
    types["ZoneMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ZoneMetadataIn"]
    )
    types["ZoneMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ZoneMetadataOut"])
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
    types["InstanceMessageIn"] = t.struct(
        {"message": t.string().optional(), "code": t.string().optional()}
    ).named(renames["InstanceMessageIn"])
    types["InstanceMessageOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceMessageOut"])
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

    functions = {}
    functions["projectsLocationsList"] = memcache.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = memcache.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesApplyParameters"] = memcache.patch(
        "v1/{name}:updateParameters",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "parameters": t.proxy(renames["MemcacheParametersIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesList"] = memcache.patch(
        "v1/{name}:updateParameters",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "parameters": t.proxy(renames["MemcacheParametersIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDelete"] = memcache.patch(
        "v1/{name}:updateParameters",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "parameters": t.proxy(renames["MemcacheParametersIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesPatch"] = memcache.patch(
        "v1/{name}:updateParameters",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "parameters": t.proxy(renames["MemcacheParametersIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesRescheduleMaintenance"] = memcache.patch(
        "v1/{name}:updateParameters",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "parameters": t.proxy(renames["MemcacheParametersIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesCreate"] = memcache.patch(
        "v1/{name}:updateParameters",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "parameters": t.proxy(renames["MemcacheParametersIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesGet"] = memcache.patch(
        "v1/{name}:updateParameters",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "parameters": t.proxy(renames["MemcacheParametersIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesUpdateParameters"] = memcache.patch(
        "v1/{name}:updateParameters",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "parameters": t.proxy(renames["MemcacheParametersIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = memcache.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = memcache.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = memcache.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = memcache.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="memcache", renames=renames, types=Box(types), functions=Box(functions)
    )
