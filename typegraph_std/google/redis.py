from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_redis() -> Import:
    redis = HTTPRuntime("https://redis.googleapis.com/")

    renames = {
        "ErrorResponse": "_redis_1_ErrorResponse",
        "GoogleCloudRedisV1LocationMetadataIn": "_redis_2_GoogleCloudRedisV1LocationMetadataIn",
        "GoogleCloudRedisV1LocationMetadataOut": "_redis_3_GoogleCloudRedisV1LocationMetadataOut",
        "InstanceAuthStringIn": "_redis_4_InstanceAuthStringIn",
        "InstanceAuthStringOut": "_redis_5_InstanceAuthStringOut",
        "OperationIn": "_redis_6_OperationIn",
        "OperationOut": "_redis_7_OperationOut",
        "TlsCertificateIn": "_redis_8_TlsCertificateIn",
        "TlsCertificateOut": "_redis_9_TlsCertificateOut",
        "TimeOfDayIn": "_redis_10_TimeOfDayIn",
        "TimeOfDayOut": "_redis_11_TimeOfDayOut",
        "InputConfigIn": "_redis_12_InputConfigIn",
        "InputConfigOut": "_redis_13_InputConfigOut",
        "EmptyIn": "_redis_14_EmptyIn",
        "EmptyOut": "_redis_15_EmptyOut",
        "InstanceIn": "_redis_16_InstanceIn",
        "InstanceOut": "_redis_17_InstanceOut",
        "LocationIn": "_redis_18_LocationIn",
        "LocationOut": "_redis_19_LocationOut",
        "GcsDestinationIn": "_redis_20_GcsDestinationIn",
        "GcsDestinationOut": "_redis_21_GcsDestinationOut",
        "RescheduleMaintenanceRequestIn": "_redis_22_RescheduleMaintenanceRequestIn",
        "RescheduleMaintenanceRequestOut": "_redis_23_RescheduleMaintenanceRequestOut",
        "FailoverInstanceRequestIn": "_redis_24_FailoverInstanceRequestIn",
        "FailoverInstanceRequestOut": "_redis_25_FailoverInstanceRequestOut",
        "MaintenancePolicyIn": "_redis_26_MaintenancePolicyIn",
        "MaintenancePolicyOut": "_redis_27_MaintenancePolicyOut",
        "ListInstancesResponseIn": "_redis_28_ListInstancesResponseIn",
        "ListInstancesResponseOut": "_redis_29_ListInstancesResponseOut",
        "MaintenanceScheduleIn": "_redis_30_MaintenanceScheduleIn",
        "MaintenanceScheduleOut": "_redis_31_MaintenanceScheduleOut",
        "OutputConfigIn": "_redis_32_OutputConfigIn",
        "OutputConfigOut": "_redis_33_OutputConfigOut",
        "StatusIn": "_redis_34_StatusIn",
        "StatusOut": "_redis_35_StatusOut",
        "UpgradeInstanceRequestIn": "_redis_36_UpgradeInstanceRequestIn",
        "UpgradeInstanceRequestOut": "_redis_37_UpgradeInstanceRequestOut",
        "GoogleCloudRedisV1ZoneMetadataIn": "_redis_38_GoogleCloudRedisV1ZoneMetadataIn",
        "GoogleCloudRedisV1ZoneMetadataOut": "_redis_39_GoogleCloudRedisV1ZoneMetadataOut",
        "NodeInfoIn": "_redis_40_NodeInfoIn",
        "NodeInfoOut": "_redis_41_NodeInfoOut",
        "PersistenceConfigIn": "_redis_42_PersistenceConfigIn",
        "PersistenceConfigOut": "_redis_43_PersistenceConfigOut",
        "ListLocationsResponseIn": "_redis_44_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_redis_45_ListLocationsResponseOut",
        "ImportInstanceRequestIn": "_redis_46_ImportInstanceRequestIn",
        "ImportInstanceRequestOut": "_redis_47_ImportInstanceRequestOut",
        "WeeklyMaintenanceWindowIn": "_redis_48_WeeklyMaintenanceWindowIn",
        "WeeklyMaintenanceWindowOut": "_redis_49_WeeklyMaintenanceWindowOut",
        "ExportInstanceRequestIn": "_redis_50_ExportInstanceRequestIn",
        "ExportInstanceRequestOut": "_redis_51_ExportInstanceRequestOut",
        "ListOperationsResponseIn": "_redis_52_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_redis_53_ListOperationsResponseOut",
        "ReconciliationOperationMetadataIn": "_redis_54_ReconciliationOperationMetadataIn",
        "ReconciliationOperationMetadataOut": "_redis_55_ReconciliationOperationMetadataOut",
        "GcsSourceIn": "_redis_56_GcsSourceIn",
        "GcsSourceOut": "_redis_57_GcsSourceOut",
        "GoogleCloudRedisV1OperationMetadataIn": "_redis_58_GoogleCloudRedisV1OperationMetadataIn",
        "GoogleCloudRedisV1OperationMetadataOut": "_redis_59_GoogleCloudRedisV1OperationMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudRedisV1LocationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRedisV1LocationMetadataIn"])
    types["GoogleCloudRedisV1LocationMetadataOut"] = t.struct(
        {
            "availableZones": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRedisV1LocationMetadataOut"])
    types["InstanceAuthStringIn"] = t.struct(
        {"authString": t.string().optional()}
    ).named(renames["InstanceAuthStringIn"])
    types["InstanceAuthStringOut"] = t.struct(
        {
            "authString": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceAuthStringOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
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
            "createTime": t.string().optional(),
            "expireTime": t.string().optional(),
            "sha1Fingerprint": t.string().optional(),
            "cert": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TlsCertificateOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["InputConfigIn"] = t.struct(
        {"gcsSource": t.proxy(renames["GcsSourceIn"]).optional()}
    ).named(renames["InputConfigIn"])
    types["InputConfigOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GcsSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InputConfigOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["InstanceIn"] = t.struct(
        {
            "suspensionReasons": t.array(t.string()).optional(),
            "reservedIpRange": t.string().optional(),
            "redisVersion": t.string().optional(),
            "availableMaintenanceVersions": t.array(t.string()).optional(),
            "name": t.string(),
            "authorizedNetwork": t.string().optional(),
            "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]).optional(),
            "tier": t.string(),
            "secondaryIpRange": t.string().optional(),
            "connectMode": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "redisConfigs": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "memorySizeGb": t.integer(),
            "displayName": t.string().optional(),
            "maintenanceVersion": t.string().optional(),
            "authEnabled": t.boolean().optional(),
            "readReplicasMode": t.string().optional(),
            "transitEncryptionMode": t.string().optional(),
            "replicaCount": t.integer().optional(),
            "persistenceConfig": t.proxy(renames["PersistenceConfigIn"]).optional(),
            "alternativeLocationId": t.string().optional(),
            "customerManagedKey": t.string().optional(),
        }
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "suspensionReasons": t.array(t.string()).optional(),
            "maintenanceSchedule": t.proxy(
                renames["MaintenanceScheduleOut"]
            ).optional(),
            "reservedIpRange": t.string().optional(),
            "redisVersion": t.string().optional(),
            "availableMaintenanceVersions": t.array(t.string()).optional(),
            "name": t.string(),
            "authorizedNetwork": t.string().optional(),
            "maintenancePolicy": t.proxy(renames["MaintenancePolicyOut"]).optional(),
            "tier": t.string(),
            "secondaryIpRange": t.string().optional(),
            "readEndpoint": t.string().optional(),
            "connectMode": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "redisConfigs": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "persistenceIamIdentity": t.string().optional(),
            "host": t.string().optional(),
            "locationId": t.string().optional(),
            "memorySizeGb": t.integer(),
            "createTime": t.string().optional(),
            "port": t.integer().optional(),
            "displayName": t.string().optional(),
            "maintenanceVersion": t.string().optional(),
            "authEnabled": t.boolean().optional(),
            "readReplicasMode": t.string().optional(),
            "transitEncryptionMode": t.string().optional(),
            "serverCaCerts": t.array(t.proxy(renames["TlsCertificateOut"])).optional(),
            "replicaCount": t.integer().optional(),
            "persistenceConfig": t.proxy(renames["PersistenceConfigOut"]).optional(),
            "statusMessage": t.string().optional(),
            "readEndpointPort": t.integer().optional(),
            "currentLocationId": t.string().optional(),
            "nodes": t.array(t.proxy(renames["NodeInfoOut"])).optional(),
            "alternativeLocationId": t.string().optional(),
            "customerManagedKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["GcsDestinationIn"] = t.struct({"uri": t.string()}).named(
        renames["GcsDestinationIn"]
    )
    types["GcsDestinationOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GcsDestinationOut"])
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
    types["FailoverInstanceRequestIn"] = t.struct(
        {"dataProtectionMode": t.string().optional()}
    ).named(renames["FailoverInstanceRequestIn"])
    types["FailoverInstanceRequestOut"] = t.struct(
        {
            "dataProtectionMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FailoverInstanceRequestOut"])
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
    types["ListInstancesResponseIn"] = t.struct(
        {
            "instances": t.array(t.proxy(renames["InstanceIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListInstancesResponseIn"])
    types["ListInstancesResponseOut"] = t.struct(
        {
            "instances": t.array(t.proxy(renames["InstanceOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInstancesResponseOut"])
    types["MaintenanceScheduleIn"] = t.struct(
        {"canReschedule": t.boolean().optional()}
    ).named(renames["MaintenanceScheduleIn"])
    types["MaintenanceScheduleOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "scheduleDeadlineTime": t.string().optional(),
            "canReschedule": t.boolean().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceScheduleOut"])
    types["OutputConfigIn"] = t.struct(
        {"gcsDestination": t.proxy(renames["GcsDestinationIn"]).optional()}
    ).named(renames["OutputConfigIn"])
    types["OutputConfigOut"] = t.struct(
        {
            "gcsDestination": t.proxy(renames["GcsDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutputConfigOut"])
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
    types["UpgradeInstanceRequestIn"] = t.struct({"redisVersion": t.string()}).named(
        renames["UpgradeInstanceRequestIn"]
    )
    types["UpgradeInstanceRequestOut"] = t.struct(
        {
            "redisVersion": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeInstanceRequestOut"])
    types["GoogleCloudRedisV1ZoneMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRedisV1ZoneMetadataIn"])
    types["GoogleCloudRedisV1ZoneMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRedisV1ZoneMetadataOut"])
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
            "rdbSnapshotPeriod": t.string().optional(),
            "rdbNextSnapshotTime": t.string().optional(),
            "rdbSnapshotStartTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersistenceConfigOut"])
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
    types["ImportInstanceRequestIn"] = t.struct(
        {"inputConfig": t.proxy(renames["InputConfigIn"])}
    ).named(renames["ImportInstanceRequestIn"])
    types["ImportInstanceRequestOut"] = t.struct(
        {
            "inputConfig": t.proxy(renames["InputConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportInstanceRequestOut"])
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
    types["ExportInstanceRequestIn"] = t.struct(
        {"outputConfig": t.proxy(renames["OutputConfigIn"])}
    ).named(renames["ExportInstanceRequestIn"])
    types["ExportInstanceRequestOut"] = t.struct(
        {
            "outputConfig": t.proxy(renames["OutputConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportInstanceRequestOut"])
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
    types["GcsSourceIn"] = t.struct({"uri": t.string()}).named(renames["GcsSourceIn"])
    types["GcsSourceOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GcsSourceOut"])
    types["GoogleCloudRedisV1OperationMetadataIn"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "statusDetail": t.string().optional(),
            "endTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "verb": t.string().optional(),
        }
    ).named(renames["GoogleCloudRedisV1OperationMetadataIn"])
    types["GoogleCloudRedisV1OperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "statusDetail": t.string().optional(),
            "endTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRedisV1OperationMetadataOut"])

    functions = {}
    functions["projectsLocationsGet"] = redis.get(
        "v1/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = redis.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = redis.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = redis.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = redis.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesUpgrade"] = redis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesFailover"] = redis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesGetAuthString"] = redis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesRescheduleMaintenance"] = redis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesPatch"] = redis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesImport"] = redis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesList"] = redis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesExport"] = redis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesGet"] = redis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesCreate"] = redis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDelete"] = redis.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="redis", renames=renames, types=Box(types), functions=Box(functions)
    )
