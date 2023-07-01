from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_redis():
    redis = HTTPRuntime("https://redis.googleapis.com/")

    renames = {
        "ErrorResponse": "_redis_1_ErrorResponse",
        "ListInstancesResponseIn": "_redis_2_ListInstancesResponseIn",
        "ListInstancesResponseOut": "_redis_3_ListInstancesResponseOut",
        "StatusIn": "_redis_4_StatusIn",
        "StatusOut": "_redis_5_StatusOut",
        "GcsDestinationIn": "_redis_6_GcsDestinationIn",
        "GcsDestinationOut": "_redis_7_GcsDestinationOut",
        "GoogleCloudRedisV1OperationMetadataIn": "_redis_8_GoogleCloudRedisV1OperationMetadataIn",
        "GoogleCloudRedisV1OperationMetadataOut": "_redis_9_GoogleCloudRedisV1OperationMetadataOut",
        "InputConfigIn": "_redis_10_InputConfigIn",
        "InputConfigOut": "_redis_11_InputConfigOut",
        "GoogleCloudRedisV1LocationMetadataIn": "_redis_12_GoogleCloudRedisV1LocationMetadataIn",
        "GoogleCloudRedisV1LocationMetadataOut": "_redis_13_GoogleCloudRedisV1LocationMetadataOut",
        "NodeInfoIn": "_redis_14_NodeInfoIn",
        "NodeInfoOut": "_redis_15_NodeInfoOut",
        "LocationIn": "_redis_16_LocationIn",
        "LocationOut": "_redis_17_LocationOut",
        "MaintenancePolicyIn": "_redis_18_MaintenancePolicyIn",
        "MaintenancePolicyOut": "_redis_19_MaintenancePolicyOut",
        "OutputConfigIn": "_redis_20_OutputConfigIn",
        "OutputConfigOut": "_redis_21_OutputConfigOut",
        "GoogleCloudRedisV1ZoneMetadataIn": "_redis_22_GoogleCloudRedisV1ZoneMetadataIn",
        "GoogleCloudRedisV1ZoneMetadataOut": "_redis_23_GoogleCloudRedisV1ZoneMetadataOut",
        "FailoverInstanceRequestIn": "_redis_24_FailoverInstanceRequestIn",
        "FailoverInstanceRequestOut": "_redis_25_FailoverInstanceRequestOut",
        "EmptyIn": "_redis_26_EmptyIn",
        "EmptyOut": "_redis_27_EmptyOut",
        "GcsSourceIn": "_redis_28_GcsSourceIn",
        "GcsSourceOut": "_redis_29_GcsSourceOut",
        "ListLocationsResponseIn": "_redis_30_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_redis_31_ListLocationsResponseOut",
        "PersistenceConfigIn": "_redis_32_PersistenceConfigIn",
        "PersistenceConfigOut": "_redis_33_PersistenceConfigOut",
        "TlsCertificateIn": "_redis_34_TlsCertificateIn",
        "TlsCertificateOut": "_redis_35_TlsCertificateOut",
        "MaintenanceScheduleIn": "_redis_36_MaintenanceScheduleIn",
        "MaintenanceScheduleOut": "_redis_37_MaintenanceScheduleOut",
        "ImportInstanceRequestIn": "_redis_38_ImportInstanceRequestIn",
        "ImportInstanceRequestOut": "_redis_39_ImportInstanceRequestOut",
        "ReconciliationOperationMetadataIn": "_redis_40_ReconciliationOperationMetadataIn",
        "ReconciliationOperationMetadataOut": "_redis_41_ReconciliationOperationMetadataOut",
        "ExportInstanceRequestIn": "_redis_42_ExportInstanceRequestIn",
        "ExportInstanceRequestOut": "_redis_43_ExportInstanceRequestOut",
        "RescheduleMaintenanceRequestIn": "_redis_44_RescheduleMaintenanceRequestIn",
        "RescheduleMaintenanceRequestOut": "_redis_45_RescheduleMaintenanceRequestOut",
        "ListOperationsResponseIn": "_redis_46_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_redis_47_ListOperationsResponseOut",
        "InstanceAuthStringIn": "_redis_48_InstanceAuthStringIn",
        "InstanceAuthStringOut": "_redis_49_InstanceAuthStringOut",
        "WeeklyMaintenanceWindowIn": "_redis_50_WeeklyMaintenanceWindowIn",
        "WeeklyMaintenanceWindowOut": "_redis_51_WeeklyMaintenanceWindowOut",
        "TimeOfDayIn": "_redis_52_TimeOfDayIn",
        "TimeOfDayOut": "_redis_53_TimeOfDayOut",
        "InstanceIn": "_redis_54_InstanceIn",
        "InstanceOut": "_redis_55_InstanceOut",
        "UpgradeInstanceRequestIn": "_redis_56_UpgradeInstanceRequestIn",
        "UpgradeInstanceRequestOut": "_redis_57_UpgradeInstanceRequestOut",
        "OperationIn": "_redis_58_OperationIn",
        "OperationOut": "_redis_59_OperationOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ListInstancesResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "instances": t.array(t.proxy(renames["InstanceIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListInstancesResponseIn"])
    types["ListInstancesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "instances": t.array(t.proxy(renames["InstanceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInstancesResponseOut"])
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
    types["GcsDestinationIn"] = t.struct({"uri": t.string()}).named(
        renames["GcsDestinationIn"]
    )
    types["GcsDestinationOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GcsDestinationOut"])
    types["GoogleCloudRedisV1OperationMetadataIn"] = t.struct(
        {
            "cancelRequested": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "statusDetail": t.string().optional(),
        }
    ).named(renames["GoogleCloudRedisV1OperationMetadataIn"])
    types["GoogleCloudRedisV1OperationMetadataOut"] = t.struct(
        {
            "cancelRequested": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "statusDetail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRedisV1OperationMetadataOut"])
    types["InputConfigIn"] = t.struct(
        {"gcsSource": t.proxy(renames["GcsSourceIn"]).optional()}
    ).named(renames["InputConfigIn"])
    types["InputConfigOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GcsSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InputConfigOut"])
    types["GoogleCloudRedisV1LocationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRedisV1LocationMetadataIn"])
    types["GoogleCloudRedisV1LocationMetadataOut"] = t.struct(
        {
            "availableZones": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRedisV1LocationMetadataOut"])
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
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["MaintenancePolicyIn"] = t.struct(
        {
            "weeklyMaintenanceWindow": t.array(
                t.proxy(renames["WeeklyMaintenanceWindowIn"])
            ).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["MaintenancePolicyIn"])
    types["MaintenancePolicyOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "weeklyMaintenanceWindow": t.array(
                t.proxy(renames["WeeklyMaintenanceWindowOut"])
            ).optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenancePolicyOut"])
    types["OutputConfigIn"] = t.struct(
        {"gcsDestination": t.proxy(renames["GcsDestinationIn"]).optional()}
    ).named(renames["OutputConfigIn"])
    types["OutputConfigOut"] = t.struct(
        {
            "gcsDestination": t.proxy(renames["GcsDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutputConfigOut"])
    types["GoogleCloudRedisV1ZoneMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRedisV1ZoneMetadataIn"])
    types["GoogleCloudRedisV1ZoneMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRedisV1ZoneMetadataOut"])
    types["FailoverInstanceRequestIn"] = t.struct(
        {"dataProtectionMode": t.string().optional()}
    ).named(renames["FailoverInstanceRequestIn"])
    types["FailoverInstanceRequestOut"] = t.struct(
        {
            "dataProtectionMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FailoverInstanceRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GcsSourceIn"] = t.struct({"uri": t.string()}).named(renames["GcsSourceIn"])
    types["GcsSourceOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GcsSourceOut"])
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
            "rdbSnapshotPeriod": t.string().optional(),
            "rdbSnapshotStartTime": t.string().optional(),
            "persistenceMode": t.string().optional(),
        }
    ).named(renames["PersistenceConfigIn"])
    types["PersistenceConfigOut"] = t.struct(
        {
            "rdbNextSnapshotTime": t.string().optional(),
            "rdbSnapshotPeriod": t.string().optional(),
            "rdbSnapshotStartTime": t.string().optional(),
            "persistenceMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersistenceConfigOut"])
    types["TlsCertificateIn"] = t.struct(
        {
            "serialNumber": t.string().optional(),
            "sha1Fingerprint": t.string().optional(),
            "cert": t.string().optional(),
        }
    ).named(renames["TlsCertificateIn"])
    types["TlsCertificateOut"] = t.struct(
        {
            "serialNumber": t.string().optional(),
            "sha1Fingerprint": t.string().optional(),
            "createTime": t.string().optional(),
            "cert": t.string().optional(),
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TlsCertificateOut"])
    types["MaintenanceScheduleIn"] = t.struct(
        {"canReschedule": t.boolean().optional()}
    ).named(renames["MaintenanceScheduleIn"])
    types["MaintenanceScheduleOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "canReschedule": t.boolean().optional(),
            "scheduleDeadlineTime": t.string().optional(),
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
    types["ExportInstanceRequestIn"] = t.struct(
        {"outputConfig": t.proxy(renames["OutputConfigIn"])}
    ).named(renames["ExportInstanceRequestIn"])
    types["ExportInstanceRequestOut"] = t.struct(
        {
            "outputConfig": t.proxy(renames["OutputConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportInstanceRequestOut"])
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
    types["InstanceAuthStringIn"] = t.struct(
        {"authString": t.string().optional()}
    ).named(renames["InstanceAuthStringIn"])
    types["InstanceAuthStringOut"] = t.struct(
        {
            "authString": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceAuthStringOut"])
    types["WeeklyMaintenanceWindowIn"] = t.struct(
        {"day": t.string(), "startTime": t.proxy(renames["TimeOfDayIn"])}
    ).named(renames["WeeklyMaintenanceWindowIn"])
    types["WeeklyMaintenanceWindowOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "day": t.string(),
            "startTime": t.proxy(renames["TimeOfDayOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WeeklyMaintenanceWindowOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["InstanceIn"] = t.struct(
        {
            "name": t.string(),
            "authorizedNetwork": t.string().optional(),
            "locationId": t.string().optional(),
            "alternativeLocationId": t.string().optional(),
            "maintenanceVersion": t.string().optional(),
            "redisVersion": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "connectMode": t.string().optional(),
            "secondaryIpRange": t.string().optional(),
            "persistenceConfig": t.proxy(renames["PersistenceConfigIn"]).optional(),
            "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]).optional(),
            "memorySizeGb": t.integer(),
            "displayName": t.string().optional(),
            "readReplicasMode": t.string().optional(),
            "authEnabled": t.boolean().optional(),
            "availableMaintenanceVersions": t.array(t.string()).optional(),
            "redisConfigs": t.struct({"_": t.string().optional()}).optional(),
            "suspensionReasons": t.array(t.string()).optional(),
            "replicaCount": t.integer().optional(),
            "reservedIpRange": t.string().optional(),
            "tier": t.string(),
            "transitEncryptionMode": t.string().optional(),
            "customerManagedKey": t.string().optional(),
        }
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "name": t.string(),
            "authorizedNetwork": t.string().optional(),
            "locationId": t.string().optional(),
            "alternativeLocationId": t.string().optional(),
            "maintenanceVersion": t.string().optional(),
            "redisVersion": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "connectMode": t.string().optional(),
            "serverCaCerts": t.array(t.proxy(renames["TlsCertificateOut"])).optional(),
            "port": t.integer().optional(),
            "secondaryIpRange": t.string().optional(),
            "persistenceConfig": t.proxy(renames["PersistenceConfigOut"]).optional(),
            "nodes": t.array(t.proxy(renames["NodeInfoOut"])).optional(),
            "maintenancePolicy": t.proxy(renames["MaintenancePolicyOut"]).optional(),
            "memorySizeGb": t.integer(),
            "host": t.string().optional(),
            "displayName": t.string().optional(),
            "readReplicasMode": t.string().optional(),
            "readEndpointPort": t.integer().optional(),
            "maintenanceSchedule": t.proxy(
                renames["MaintenanceScheduleOut"]
            ).optional(),
            "state": t.string().optional(),
            "statusMessage": t.string().optional(),
            "authEnabled": t.boolean().optional(),
            "currentLocationId": t.string().optional(),
            "availableMaintenanceVersions": t.array(t.string()).optional(),
            "redisConfigs": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "suspensionReasons": t.array(t.string()).optional(),
            "persistenceIamIdentity": t.string().optional(),
            "replicaCount": t.integer().optional(),
            "readEndpoint": t.string().optional(),
            "reservedIpRange": t.string().optional(),
            "tier": t.string(),
            "transitEncryptionMode": t.string().optional(),
            "customerManagedKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
    types["UpgradeInstanceRequestIn"] = t.struct({"redisVersion": t.string()}).named(
        renames["UpgradeInstanceRequestIn"]
    )
    types["UpgradeInstanceRequestOut"] = t.struct(
        {
            "redisVersion": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeInstanceRequestOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])

    functions = {}
    functions["projectsLocationsGet"] = redis.get(
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
    functions["projectsLocationsList"] = redis.get(
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
    functions["projectsLocationsOperationsDelete"] = redis.post(
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
    functions["projectsLocationsInstancesCreate"] = redis.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesFailover"] = redis.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesRescheduleMaintenance"] = redis.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesGetAuthString"] = redis.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesUpgrade"] = redis.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesImport"] = redis.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesPatch"] = redis.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesExport"] = redis.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesList"] = redis.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDelete"] = redis.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesGet"] = redis.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="redis", renames=renames, types=Box(types), functions=Box(functions)
    )
