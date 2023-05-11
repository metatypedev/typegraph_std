from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_redis() -> Import:
    redis = HTTPRuntime("https://redis.googleapis.com/")

    renames = {
        "ErrorResponse": "_redis_1_ErrorResponse",
        "EmptyIn": "_redis_2_EmptyIn",
        "EmptyOut": "_redis_3_EmptyOut",
        "MaintenanceScheduleIn": "_redis_4_MaintenanceScheduleIn",
        "MaintenanceScheduleOut": "_redis_5_MaintenanceScheduleOut",
        "ImportInstanceRequestIn": "_redis_6_ImportInstanceRequestIn",
        "ImportInstanceRequestOut": "_redis_7_ImportInstanceRequestOut",
        "TimeOfDayIn": "_redis_8_TimeOfDayIn",
        "TimeOfDayOut": "_redis_9_TimeOfDayOut",
        "ExportInstanceRequestIn": "_redis_10_ExportInstanceRequestIn",
        "ExportInstanceRequestOut": "_redis_11_ExportInstanceRequestOut",
        "StatusIn": "_redis_12_StatusIn",
        "StatusOut": "_redis_13_StatusOut",
        "MaintenancePolicyIn": "_redis_14_MaintenancePolicyIn",
        "MaintenancePolicyOut": "_redis_15_MaintenancePolicyOut",
        "InstanceAuthStringIn": "_redis_16_InstanceAuthStringIn",
        "InstanceAuthStringOut": "_redis_17_InstanceAuthStringOut",
        "NodeInfoIn": "_redis_18_NodeInfoIn",
        "NodeInfoOut": "_redis_19_NodeInfoOut",
        "UpgradeInstanceRequestIn": "_redis_20_UpgradeInstanceRequestIn",
        "UpgradeInstanceRequestOut": "_redis_21_UpgradeInstanceRequestOut",
        "OutputConfigIn": "_redis_22_OutputConfigIn",
        "OutputConfigOut": "_redis_23_OutputConfigOut",
        "FailoverInstanceRequestIn": "_redis_24_FailoverInstanceRequestIn",
        "FailoverInstanceRequestOut": "_redis_25_FailoverInstanceRequestOut",
        "InstanceIn": "_redis_26_InstanceIn",
        "InstanceOut": "_redis_27_InstanceOut",
        "TlsCertificateIn": "_redis_28_TlsCertificateIn",
        "TlsCertificateOut": "_redis_29_TlsCertificateOut",
        "GoogleCloudRedisV1ZoneMetadataIn": "_redis_30_GoogleCloudRedisV1ZoneMetadataIn",
        "GoogleCloudRedisV1ZoneMetadataOut": "_redis_31_GoogleCloudRedisV1ZoneMetadataOut",
        "GoogleCloudRedisV1LocationMetadataIn": "_redis_32_GoogleCloudRedisV1LocationMetadataIn",
        "GoogleCloudRedisV1LocationMetadataOut": "_redis_33_GoogleCloudRedisV1LocationMetadataOut",
        "LocationIn": "_redis_34_LocationIn",
        "LocationOut": "_redis_35_LocationOut",
        "GcsDestinationIn": "_redis_36_GcsDestinationIn",
        "GcsDestinationOut": "_redis_37_GcsDestinationOut",
        "GcsSourceIn": "_redis_38_GcsSourceIn",
        "GcsSourceOut": "_redis_39_GcsSourceOut",
        "ListInstancesResponseIn": "_redis_40_ListInstancesResponseIn",
        "ListInstancesResponseOut": "_redis_41_ListInstancesResponseOut",
        "ListLocationsResponseIn": "_redis_42_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_redis_43_ListLocationsResponseOut",
        "PersistenceConfigIn": "_redis_44_PersistenceConfigIn",
        "PersistenceConfigOut": "_redis_45_PersistenceConfigOut",
        "InputConfigIn": "_redis_46_InputConfigIn",
        "InputConfigOut": "_redis_47_InputConfigOut",
        "OperationIn": "_redis_48_OperationIn",
        "OperationOut": "_redis_49_OperationOut",
        "RescheduleMaintenanceRequestIn": "_redis_50_RescheduleMaintenanceRequestIn",
        "RescheduleMaintenanceRequestOut": "_redis_51_RescheduleMaintenanceRequestOut",
        "ReconciliationOperationMetadataIn": "_redis_52_ReconciliationOperationMetadataIn",
        "ReconciliationOperationMetadataOut": "_redis_53_ReconciliationOperationMetadataOut",
        "WeeklyMaintenanceWindowIn": "_redis_54_WeeklyMaintenanceWindowIn",
        "WeeklyMaintenanceWindowOut": "_redis_55_WeeklyMaintenanceWindowOut",
        "ListOperationsResponseIn": "_redis_56_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_redis_57_ListOperationsResponseOut",
        "GoogleCloudRedisV1OperationMetadataIn": "_redis_58_GoogleCloudRedisV1OperationMetadataIn",
        "GoogleCloudRedisV1OperationMetadataOut": "_redis_59_GoogleCloudRedisV1OperationMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["MaintenanceScheduleIn"] = t.struct(
        {"canReschedule": t.boolean().optional()}
    ).named(renames["MaintenanceScheduleIn"])
    types["MaintenanceScheduleOut"] = t.struct(
        {
            "scheduleDeadlineTime": t.string().optional(),
            "startTime": t.string().optional(),
            "canReschedule": t.boolean().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceScheduleOut"])
    types["ImportInstanceRequestIn"] = t.struct(
        {"inputConfig": t.proxy(renames["InputConfigIn"])}
    ).named(renames["ImportInstanceRequestIn"])
    types["ImportInstanceRequestOut"] = t.struct(
        {
            "inputConfig": t.proxy(renames["InputConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportInstanceRequestOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["ExportInstanceRequestIn"] = t.struct(
        {"outputConfig": t.proxy(renames["OutputConfigIn"])}
    ).named(renames["ExportInstanceRequestIn"])
    types["ExportInstanceRequestOut"] = t.struct(
        {
            "outputConfig": t.proxy(renames["OutputConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportInstanceRequestOut"])
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
    types["MaintenancePolicyIn"] = t.struct(
        {
            "description": t.string().optional(),
            "weeklyMaintenanceWindow": t.array(
                t.proxy(renames["WeeklyMaintenanceWindowIn"])
            ).optional(),
        }
    ).named(renames["MaintenancePolicyIn"])
    types["MaintenancePolicyOut"] = t.struct(
        {
            "description": t.string().optional(),
            "weeklyMaintenanceWindow": t.array(
                t.proxy(renames["WeeklyMaintenanceWindowOut"])
            ).optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenancePolicyOut"])
    types["InstanceAuthStringIn"] = t.struct(
        {"authString": t.string().optional()}
    ).named(renames["InstanceAuthStringIn"])
    types["InstanceAuthStringOut"] = t.struct(
        {
            "authString": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceAuthStringOut"])
    types["NodeInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["NodeInfoIn"]
    )
    types["NodeInfoOut"] = t.struct(
        {
            "zone": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeInfoOut"])
    types["UpgradeInstanceRequestIn"] = t.struct({"redisVersion": t.string()}).named(
        renames["UpgradeInstanceRequestIn"]
    )
    types["UpgradeInstanceRequestOut"] = t.struct(
        {
            "redisVersion": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeInstanceRequestOut"])
    types["OutputConfigIn"] = t.struct(
        {"gcsDestination": t.proxy(renames["GcsDestinationIn"]).optional()}
    ).named(renames["OutputConfigIn"])
    types["OutputConfigOut"] = t.struct(
        {
            "gcsDestination": t.proxy(renames["GcsDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutputConfigOut"])
    types["FailoverInstanceRequestIn"] = t.struct(
        {"dataProtectionMode": t.string().optional()}
    ).named(renames["FailoverInstanceRequestIn"])
    types["FailoverInstanceRequestOut"] = t.struct(
        {
            "dataProtectionMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FailoverInstanceRequestOut"])
    types["InstanceIn"] = t.struct(
        {
            "alternativeLocationId": t.string().optional(),
            "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]).optional(),
            "authEnabled": t.boolean().optional(),
            "availableMaintenanceVersions": t.array(t.string()).optional(),
            "redisVersion": t.string().optional(),
            "transitEncryptionMode": t.string().optional(),
            "suspensionReasons": t.array(t.string()).optional(),
            "tier": t.string(),
            "authorizedNetwork": t.string().optional(),
            "displayName": t.string().optional(),
            "reservedIpRange": t.string().optional(),
            "memorySizeGb": t.integer(),
            "maintenanceVersion": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "redisConfigs": t.struct({"_": t.string().optional()}).optional(),
            "persistenceConfig": t.proxy(renames["PersistenceConfigIn"]).optional(),
            "replicaCount": t.integer().optional(),
            "locationId": t.string().optional(),
            "customerManagedKey": t.string().optional(),
            "readReplicasMode": t.string().optional(),
            "name": t.string(),
            "secondaryIpRange": t.string().optional(),
            "connectMode": t.string().optional(),
        }
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "alternativeLocationId": t.string().optional(),
            "readEndpointPort": t.integer().optional(),
            "maintenancePolicy": t.proxy(renames["MaintenancePolicyOut"]).optional(),
            "state": t.string().optional(),
            "authEnabled": t.boolean().optional(),
            "availableMaintenanceVersions": t.array(t.string()).optional(),
            "redisVersion": t.string().optional(),
            "transitEncryptionMode": t.string().optional(),
            "suspensionReasons": t.array(t.string()).optional(),
            "tier": t.string(),
            "authorizedNetwork": t.string().optional(),
            "persistenceIamIdentity": t.string().optional(),
            "displayName": t.string().optional(),
            "reservedIpRange": t.string().optional(),
            "statusMessage": t.string().optional(),
            "currentLocationId": t.string().optional(),
            "serverCaCerts": t.array(t.proxy(renames["TlsCertificateOut"])).optional(),
            "nodes": t.array(t.proxy(renames["NodeInfoOut"])).optional(),
            "host": t.string().optional(),
            "readEndpoint": t.string().optional(),
            "memorySizeGb": t.integer(),
            "maintenanceVersion": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "redisConfigs": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "persistenceConfig": t.proxy(renames["PersistenceConfigOut"]).optional(),
            "replicaCount": t.integer().optional(),
            "locationId": t.string().optional(),
            "customerManagedKey": t.string().optional(),
            "readReplicasMode": t.string().optional(),
            "name": t.string(),
            "maintenanceSchedule": t.proxy(
                renames["MaintenanceScheduleOut"]
            ).optional(),
            "port": t.integer().optional(),
            "secondaryIpRange": t.string().optional(),
            "connectMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
    types["TlsCertificateIn"] = t.struct(
        {
            "cert": t.string().optional(),
            "sha1Fingerprint": t.string().optional(),
            "serialNumber": t.string().optional(),
        }
    ).named(renames["TlsCertificateIn"])
    types["TlsCertificateOut"] = t.struct(
        {
            "cert": t.string().optional(),
            "expireTime": t.string().optional(),
            "createTime": t.string().optional(),
            "sha1Fingerprint": t.string().optional(),
            "serialNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TlsCertificateOut"])
    types["GoogleCloudRedisV1ZoneMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRedisV1ZoneMetadataIn"])
    types["GoogleCloudRedisV1ZoneMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRedisV1ZoneMetadataOut"])
    types["GoogleCloudRedisV1LocationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRedisV1LocationMetadataIn"])
    types["GoogleCloudRedisV1LocationMetadataOut"] = t.struct(
        {
            "availableZones": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRedisV1LocationMetadataOut"])
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["GcsDestinationIn"] = t.struct({"uri": t.string()}).named(
        renames["GcsDestinationIn"]
    )
    types["GcsDestinationOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GcsDestinationOut"])
    types["GcsSourceIn"] = t.struct({"uri": t.string()}).named(renames["GcsSourceIn"])
    types["GcsSourceOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GcsSourceOut"])
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
    types["PersistenceConfigIn"] = t.struct(
        {
            "persistenceMode": t.string().optional(),
            "rdbSnapshotPeriod": t.string().optional(),
            "rdbSnapshotStartTime": t.string().optional(),
        }
    ).named(renames["PersistenceConfigIn"])
    types["PersistenceConfigOut"] = t.struct(
        {
            "persistenceMode": t.string().optional(),
            "rdbNextSnapshotTime": t.string().optional(),
            "rdbSnapshotPeriod": t.string().optional(),
            "rdbSnapshotStartTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersistenceConfigOut"])
    types["InputConfigIn"] = t.struct(
        {"gcsSource": t.proxy(renames["GcsSourceIn"]).optional()}
    ).named(renames["InputConfigIn"])
    types["InputConfigOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GcsSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InputConfigOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["ReconciliationOperationMetadataIn"] = t.struct(
        {
            "exclusiveAction": t.string().optional(),
            "deleteResource": t.boolean().optional(),
        }
    ).named(renames["ReconciliationOperationMetadataIn"])
    types["ReconciliationOperationMetadataOut"] = t.struct(
        {
            "exclusiveAction": t.string().optional(),
            "deleteResource": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReconciliationOperationMetadataOut"])
    types["WeeklyMaintenanceWindowIn"] = t.struct(
        {"startTime": t.proxy(renames["TimeOfDayIn"]), "day": t.string()}
    ).named(renames["WeeklyMaintenanceWindowIn"])
    types["WeeklyMaintenanceWindowOut"] = t.struct(
        {
            "startTime": t.proxy(renames["TimeOfDayOut"]),
            "duration": t.string().optional(),
            "day": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WeeklyMaintenanceWindowOut"])
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
    types["GoogleCloudRedisV1OperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "statusDetail": t.string().optional(),
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudRedisV1OperationMetadataIn"])
    types["GoogleCloudRedisV1OperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "statusDetail": t.string().optional(),
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRedisV1OperationMetadataOut"])

    functions = {}
    functions["projectsLocationsGet"] = redis.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = redis.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = redis.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = redis.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = redis.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = redis.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesExport"] = redis.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesRescheduleMaintenance"] = redis.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesUpgrade"] = redis.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesFailover"] = redis.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesPatch"] = redis.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesGetAuthString"] = redis.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDelete"] = redis.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesImport"] = redis.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesGet"] = redis.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesCreate"] = redis.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesList"] = redis.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="redis", renames=renames, types=types, functions=functions)
