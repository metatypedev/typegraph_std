from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_memcache() -> Import:
    memcache = HTTPRuntime("https://memcache.googleapis.com/")

    renames = {
        "ErrorResponse": "_memcache_1_ErrorResponse",
        "StatusIn": "_memcache_2_StatusIn",
        "StatusOut": "_memcache_3_StatusOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn": "_memcache_4_GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut": "_memcache_5_GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut",
        "UpdatePolicyIn": "_memcache_6_UpdatePolicyIn",
        "UpdatePolicyOut": "_memcache_7_UpdatePolicyOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn": "_memcache_8_GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut": "_memcache_9_GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut",
        "DenyMaintenancePeriodIn": "_memcache_10_DenyMaintenancePeriodIn",
        "DenyMaintenancePeriodOut": "_memcache_11_DenyMaintenancePeriodOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn": "_memcache_12_GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut": "_memcache_13_GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut",
        "ListOperationsResponseIn": "_memcache_14_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_memcache_15_ListOperationsResponseOut",
        "UpdateParametersRequestIn": "_memcache_16_UpdateParametersRequestIn",
        "UpdateParametersRequestOut": "_memcache_17_UpdateParametersRequestOut",
        "EmptyIn": "_memcache_18_EmptyIn",
        "EmptyOut": "_memcache_19_EmptyOut",
        "ApplyParametersRequestIn": "_memcache_20_ApplyParametersRequestIn",
        "ApplyParametersRequestOut": "_memcache_21_ApplyParametersRequestOut",
        "DateIn": "_memcache_22_DateIn",
        "DateOut": "_memcache_23_DateOut",
        "WeeklyMaintenanceWindowIn": "_memcache_24_WeeklyMaintenanceWindowIn",
        "WeeklyMaintenanceWindowOut": "_memcache_25_WeeklyMaintenanceWindowOut",
        "OperationMetadataIn": "_memcache_26_OperationMetadataIn",
        "OperationMetadataOut": "_memcache_27_OperationMetadataOut",
        "OperationIn": "_memcache_28_OperationIn",
        "OperationOut": "_memcache_29_OperationOut",
        "NodeIn": "_memcache_30_NodeIn",
        "NodeOut": "_memcache_31_NodeOut",
        "RescheduleMaintenanceRequestIn": "_memcache_32_RescheduleMaintenanceRequestIn",
        "RescheduleMaintenanceRequestOut": "_memcache_33_RescheduleMaintenanceRequestOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn": "_memcache_34_GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut": "_memcache_35_GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut",
        "WeeklyCycleIn": "_memcache_36_WeeklyCycleIn",
        "WeeklyCycleOut": "_memcache_37_WeeklyCycleOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn": "_memcache_38_GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut": "_memcache_39_GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut",
        "GoogleCloudMemcacheV1LocationMetadataIn": "_memcache_40_GoogleCloudMemcacheV1LocationMetadataIn",
        "GoogleCloudMemcacheV1LocationMetadataOut": "_memcache_41_GoogleCloudMemcacheV1LocationMetadataOut",
        "CancelOperationRequestIn": "_memcache_42_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_memcache_43_CancelOperationRequestOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn": "_memcache_44_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut": "_memcache_45_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut",
        "GoogleCloudMemcacheV1MaintenancePolicyIn": "_memcache_46_GoogleCloudMemcacheV1MaintenancePolicyIn",
        "GoogleCloudMemcacheV1MaintenancePolicyOut": "_memcache_47_GoogleCloudMemcacheV1MaintenancePolicyOut",
        "GoogleCloudMemcacheV1OperationMetadataIn": "_memcache_48_GoogleCloudMemcacheV1OperationMetadataIn",
        "GoogleCloudMemcacheV1OperationMetadataOut": "_memcache_49_GoogleCloudMemcacheV1OperationMetadataOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn": "_memcache_50_GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut": "_memcache_51_GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut",
        "MaintenanceWindowIn": "_memcache_52_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_memcache_53_MaintenanceWindowOut",
        "ScheduleIn": "_memcache_54_ScheduleIn",
        "ScheduleOut": "_memcache_55_ScheduleOut",
        "MaintenanceScheduleIn": "_memcache_56_MaintenanceScheduleIn",
        "MaintenanceScheduleOut": "_memcache_57_MaintenanceScheduleOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn": "_memcache_58_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut": "_memcache_59_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut",
        "TimeOfDayIn": "_memcache_60_TimeOfDayIn",
        "TimeOfDayOut": "_memcache_61_TimeOfDayOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn": "_memcache_62_GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut": "_memcache_63_GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut",
        "InstanceIn": "_memcache_64_InstanceIn",
        "InstanceOut": "_memcache_65_InstanceOut",
        "GoogleCloudMemcacheV1ZoneMetadataIn": "_memcache_66_GoogleCloudMemcacheV1ZoneMetadataIn",
        "GoogleCloudMemcacheV1ZoneMetadataOut": "_memcache_67_GoogleCloudMemcacheV1ZoneMetadataOut",
        "ListLocationsResponseIn": "_memcache_68_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_memcache_69_ListLocationsResponseOut",
        "DailyCycleIn": "_memcache_70_DailyCycleIn",
        "DailyCycleOut": "_memcache_71_DailyCycleOut",
        "LocationIn": "_memcache_72_LocationIn",
        "LocationOut": "_memcache_73_LocationOut",
        "ZoneMetadataIn": "_memcache_74_ZoneMetadataIn",
        "ZoneMetadataOut": "_memcache_75_ZoneMetadataOut",
        "InstanceMessageIn": "_memcache_76_InstanceMessageIn",
        "InstanceMessageOut": "_memcache_77_InstanceMessageOut",
        "ListInstancesResponseIn": "_memcache_78_ListInstancesResponseIn",
        "ListInstancesResponseOut": "_memcache_79_ListInstancesResponseOut",
        "MaintenancePolicyIn": "_memcache_80_MaintenancePolicyIn",
        "MaintenancePolicyOut": "_memcache_81_MaintenancePolicyOut",
        "NodeConfigIn": "_memcache_82_NodeConfigIn",
        "NodeConfigOut": "_memcache_83_NodeConfigOut",
        "MemcacheParametersIn": "_memcache_84_MemcacheParametersIn",
        "MemcacheParametersOut": "_memcache_85_MemcacheParametersOut",
        "LocationMetadataIn": "_memcache_86_LocationMetadataIn",
        "LocationMetadataOut": "_memcache_87_LocationMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["WeeklyMaintenanceWindowIn"] = t.struct(
        {
            "day": t.string(),
            "duration": t.string(),
            "startTime": t.proxy(renames["TimeOfDayIn"]),
        }
    ).named(renames["WeeklyMaintenanceWindowIn"])
    types["WeeklyMaintenanceWindowOut"] = t.struct(
        {
            "day": t.string(),
            "duration": t.string(),
            "startTime": t.proxy(renames["TimeOfDayOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WeeklyMaintenanceWindowOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "statusDetail": t.string().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["NodeIn"] = t.struct(
        {"parameters": t.proxy(renames["MemcacheParametersIn"]).optional()}
    ).named(renames["NodeIn"])
    types["NodeOut"] = t.struct(
        {
            "host": t.string().optional(),
            "zone": t.string().optional(),
            "port": t.integer().optional(),
            "parameters": t.proxy(renames["MemcacheParametersOut"]).optional(),
            "state": t.string().optional(),
            "nodeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeOut"])
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
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn"
    ] = t.struct(
        {
            "location": t.string().optional(),
            "nodeId": t.string().optional(),
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
            "location": t.string().optional(),
            "nodeId": t.string().optional(),
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
    types["GoogleCloudMemcacheV1MaintenancePolicyIn"] = t.struct(
        {
            "description": t.string().optional(),
            "weeklyMaintenanceWindow": t.array(
                t.proxy(renames["WeeklyMaintenanceWindowIn"])
            ),
        }
    ).named(renames["GoogleCloudMemcacheV1MaintenancePolicyIn"])
    types["GoogleCloudMemcacheV1MaintenancePolicyOut"] = t.struct(
        {
            "description": t.string().optional(),
            "weeklyMaintenanceWindow": t.array(
                t.proxy(renames["WeeklyMaintenanceWindowOut"])
            ),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMemcacheV1MaintenancePolicyOut"])
    types["GoogleCloudMemcacheV1OperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudMemcacheV1OperationMetadataIn"])
    types["GoogleCloudMemcacheV1OperationMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "statusDetail": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudMemcacheV1OperationMetadataOut"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "maintenancePolicyNames": t.struct({"_": t.string().optional()}).optional(),
            "maintenanceSettings": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn"
                ]
            ).optional(),
            "maintenanceSchedules": t.struct({"_": t.string().optional()}).optional(),
            "consumerDefinedName": t.string().optional(),
            "notificationParameters": t.struct({"_": t.string().optional()}).optional(),
            "instanceType": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "slmInstanceTemplate": t.string().optional(),
            "softwareVersions": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "maintenancePolicyNames": t.struct({"_": t.string().optional()}).optional(),
            "maintenanceSettings": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut"
                ]
            ).optional(),
            "maintenanceSchedules": t.struct({"_": t.string().optional()}).optional(),
            "provisionedResources": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut"
                    ]
                )
            ).optional(),
            "updateTime": t.string().optional(),
            "consumerDefinedName": t.string().optional(),
            "state": t.string().optional(),
            "tenantProjectId": t.string().optional(),
            "notificationParameters": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "instanceType": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "slmInstanceTemplate": t.string().optional(),
            "softwareVersions": t.struct({"_": t.string().optional()}).optional(),
            "producerMetadata": t.struct({"_": t.string().optional()}).optional(),
            "sloMetadata": t.proxy(
                renames["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut"])
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
    types["ScheduleIn"] = t.struct(
        {
            "duration": t.string().optional(),
            "startTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "day": t.string().optional(),
        }
    ).named(renames["ScheduleIn"])
    types["ScheduleOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "day": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduleOut"])
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
    types["TimeOfDayIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
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
    types["InstanceIn"] = t.struct(
        {
            "name": t.string(),
            "maintenancePolicy": t.proxy(
                renames["GoogleCloudMemcacheV1MaintenancePolicyIn"]
            ).optional(),
            "parameters": t.proxy(renames["MemcacheParametersIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "memcacheVersion": t.string().optional(),
            "nodeConfig": t.proxy(renames["NodeConfigIn"]),
            "authorizedNetwork": t.string().optional(),
            "nodeCount": t.integer(),
            "zones": t.array(t.string()).optional(),
            "instanceMessages": t.array(
                t.proxy(renames["InstanceMessageIn"])
            ).optional(),
        }
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "memcacheNodes": t.array(t.proxy(renames["NodeOut"])).optional(),
            "maintenanceSchedule": t.proxy(
                renames["MaintenanceScheduleOut"]
            ).optional(),
            "name": t.string(),
            "maintenancePolicy": t.proxy(
                renames["GoogleCloudMemcacheV1MaintenancePolicyOut"]
            ).optional(),
            "parameters": t.proxy(renames["MemcacheParametersOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "memcacheVersion": t.string().optional(),
            "updateTime": t.string().optional(),
            "discoveryEndpoint": t.string().optional(),
            "createTime": t.string().optional(),
            "nodeConfig": t.proxy(renames["NodeConfigOut"]),
            "authorizedNetwork": t.string().optional(),
            "nodeCount": t.integer(),
            "zones": t.array(t.string()).optional(),
            "instanceMessages": t.array(
                t.proxy(renames["InstanceMessageOut"])
            ).optional(),
            "state": t.string().optional(),
            "memcacheFullVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
    types["GoogleCloudMemcacheV1ZoneMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudMemcacheV1ZoneMetadataIn"])
    types["GoogleCloudMemcacheV1ZoneMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudMemcacheV1ZoneMetadataOut"])
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
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["ZoneMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ZoneMetadataIn"]
    )
    types["ZoneMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ZoneMetadataOut"])
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
            "updateTime": t.string().optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updatePolicy": t.proxy(renames["UpdatePolicyIn"]).optional(),
        }
    ).named(renames["MaintenancePolicyIn"])
    types["MaintenancePolicyOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updatePolicy": t.proxy(renames["UpdatePolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenancePolicyOut"])
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
    types["LocationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LocationMetadataIn"]
    )
    types["LocationMetadataOut"] = t.struct(
        {
            "availableZones": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationMetadataOut"])

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
    functions["projectsLocationsInstancesPatch"] = memcache.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "instanceId": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "maintenancePolicy": t.proxy(
                    renames["GoogleCloudMemcacheV1MaintenancePolicyIn"]
                ).optional(),
                "parameters": t.proxy(renames["MemcacheParametersIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "memcacheVersion": t.string().optional(),
                "nodeConfig": t.proxy(renames["NodeConfigIn"]),
                "authorizedNetwork": t.string().optional(),
                "nodeCount": t.integer(),
                "zones": t.array(t.string()).optional(),
                "instanceMessages": t.array(
                    t.proxy(renames["InstanceMessageIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDelete"] = memcache.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "instanceId": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "maintenancePolicy": t.proxy(
                    renames["GoogleCloudMemcacheV1MaintenancePolicyIn"]
                ).optional(),
                "parameters": t.proxy(renames["MemcacheParametersIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "memcacheVersion": t.string().optional(),
                "nodeConfig": t.proxy(renames["NodeConfigIn"]),
                "authorizedNetwork": t.string().optional(),
                "nodeCount": t.integer(),
                "zones": t.array(t.string()).optional(),
                "instanceMessages": t.array(
                    t.proxy(renames["InstanceMessageIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesList"] = memcache.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "instanceId": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "maintenancePolicy": t.proxy(
                    renames["GoogleCloudMemcacheV1MaintenancePolicyIn"]
                ).optional(),
                "parameters": t.proxy(renames["MemcacheParametersIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "memcacheVersion": t.string().optional(),
                "nodeConfig": t.proxy(renames["NodeConfigIn"]),
                "authorizedNetwork": t.string().optional(),
                "nodeCount": t.integer(),
                "zones": t.array(t.string()).optional(),
                "instanceMessages": t.array(
                    t.proxy(renames["InstanceMessageIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesApplyParameters"] = memcache.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "instanceId": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "maintenancePolicy": t.proxy(
                    renames["GoogleCloudMemcacheV1MaintenancePolicyIn"]
                ).optional(),
                "parameters": t.proxy(renames["MemcacheParametersIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "memcacheVersion": t.string().optional(),
                "nodeConfig": t.proxy(renames["NodeConfigIn"]),
                "authorizedNetwork": t.string().optional(),
                "nodeCount": t.integer(),
                "zones": t.array(t.string()).optional(),
                "instanceMessages": t.array(
                    t.proxy(renames["InstanceMessageIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesGet"] = memcache.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "instanceId": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "maintenancePolicy": t.proxy(
                    renames["GoogleCloudMemcacheV1MaintenancePolicyIn"]
                ).optional(),
                "parameters": t.proxy(renames["MemcacheParametersIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "memcacheVersion": t.string().optional(),
                "nodeConfig": t.proxy(renames["NodeConfigIn"]),
                "authorizedNetwork": t.string().optional(),
                "nodeCount": t.integer(),
                "zones": t.array(t.string()).optional(),
                "instanceMessages": t.array(
                    t.proxy(renames["InstanceMessageIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesRescheduleMaintenance"] = memcache.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "instanceId": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "maintenancePolicy": t.proxy(
                    renames["GoogleCloudMemcacheV1MaintenancePolicyIn"]
                ).optional(),
                "parameters": t.proxy(renames["MemcacheParametersIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "memcacheVersion": t.string().optional(),
                "nodeConfig": t.proxy(renames["NodeConfigIn"]),
                "authorizedNetwork": t.string().optional(),
                "nodeCount": t.integer(),
                "zones": t.array(t.string()).optional(),
                "instanceMessages": t.array(
                    t.proxy(renames["InstanceMessageIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesUpdateParameters"] = memcache.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "instanceId": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "maintenancePolicy": t.proxy(
                    renames["GoogleCloudMemcacheV1MaintenancePolicyIn"]
                ).optional(),
                "parameters": t.proxy(renames["MemcacheParametersIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "memcacheVersion": t.string().optional(),
                "nodeConfig": t.proxy(renames["NodeConfigIn"]),
                "authorizedNetwork": t.string().optional(),
                "nodeCount": t.integer(),
                "zones": t.array(t.string()).optional(),
                "instanceMessages": t.array(
                    t.proxy(renames["InstanceMessageIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesCreate"] = memcache.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "instanceId": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "maintenancePolicy": t.proxy(
                    renames["GoogleCloudMemcacheV1MaintenancePolicyIn"]
                ).optional(),
                "parameters": t.proxy(renames["MemcacheParametersIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "memcacheVersion": t.string().optional(),
                "nodeConfig": t.proxy(renames["NodeConfigIn"]),
                "authorizedNetwork": t.string().optional(),
                "nodeCount": t.integer(),
                "zones": t.array(t.string()).optional(),
                "instanceMessages": t.array(
                    t.proxy(renames["InstanceMessageIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = memcache.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = memcache.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = memcache.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = memcache.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="memcache", renames=renames, types=Box(types), functions=Box(functions)
    )
