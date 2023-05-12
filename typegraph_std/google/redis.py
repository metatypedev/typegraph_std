from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_redis() -> Import:
    redis = HTTPRuntime("https://redis.googleapis.com/")

    renames = {
        "ErrorResponse": "_redis_1_ErrorResponse",
        "NodeInfoIn": "_redis_2_NodeInfoIn",
        "NodeInfoOut": "_redis_3_NodeInfoOut",
        "TimeOfDayIn": "_redis_4_TimeOfDayIn",
        "TimeOfDayOut": "_redis_5_TimeOfDayOut",
        "GoogleCloudRedisV1LocationMetadataIn": "_redis_6_GoogleCloudRedisV1LocationMetadataIn",
        "GoogleCloudRedisV1LocationMetadataOut": "_redis_7_GoogleCloudRedisV1LocationMetadataOut",
        "ListLocationsResponseIn": "_redis_8_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_redis_9_ListLocationsResponseOut",
        "FailoverInstanceRequestIn": "_redis_10_FailoverInstanceRequestIn",
        "FailoverInstanceRequestOut": "_redis_11_FailoverInstanceRequestOut",
        "ListOperationsResponseIn": "_redis_12_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_redis_13_ListOperationsResponseOut",
        "GoogleCloudRedisV1ZoneMetadataIn": "_redis_14_GoogleCloudRedisV1ZoneMetadataIn",
        "GoogleCloudRedisV1ZoneMetadataOut": "_redis_15_GoogleCloudRedisV1ZoneMetadataOut",
        "InputConfigIn": "_redis_16_InputConfigIn",
        "InputConfigOut": "_redis_17_InputConfigOut",
        "GoogleCloudRedisV1OperationMetadataIn": "_redis_18_GoogleCloudRedisV1OperationMetadataIn",
        "GoogleCloudRedisV1OperationMetadataOut": "_redis_19_GoogleCloudRedisV1OperationMetadataOut",
        "InstanceIn": "_redis_20_InstanceIn",
        "InstanceOut": "_redis_21_InstanceOut",
        "ImportInstanceRequestIn": "_redis_22_ImportInstanceRequestIn",
        "ImportInstanceRequestOut": "_redis_23_ImportInstanceRequestOut",
        "RescheduleMaintenanceRequestIn": "_redis_24_RescheduleMaintenanceRequestIn",
        "RescheduleMaintenanceRequestOut": "_redis_25_RescheduleMaintenanceRequestOut",
        "TlsCertificateIn": "_redis_26_TlsCertificateIn",
        "TlsCertificateOut": "_redis_27_TlsCertificateOut",
        "OutputConfigIn": "_redis_28_OutputConfigIn",
        "OutputConfigOut": "_redis_29_OutputConfigOut",
        "ReconciliationOperationMetadataIn": "_redis_30_ReconciliationOperationMetadataIn",
        "ReconciliationOperationMetadataOut": "_redis_31_ReconciliationOperationMetadataOut",
        "UpgradeInstanceRequestIn": "_redis_32_UpgradeInstanceRequestIn",
        "UpgradeInstanceRequestOut": "_redis_33_UpgradeInstanceRequestOut",
        "OperationIn": "_redis_34_OperationIn",
        "OperationOut": "_redis_35_OperationOut",
        "ListInstancesResponseIn": "_redis_36_ListInstancesResponseIn",
        "ListInstancesResponseOut": "_redis_37_ListInstancesResponseOut",
        "EmptyIn": "_redis_38_EmptyIn",
        "EmptyOut": "_redis_39_EmptyOut",
        "InstanceAuthStringIn": "_redis_40_InstanceAuthStringIn",
        "InstanceAuthStringOut": "_redis_41_InstanceAuthStringOut",
        "ExportInstanceRequestIn": "_redis_42_ExportInstanceRequestIn",
        "ExportInstanceRequestOut": "_redis_43_ExportInstanceRequestOut",
        "GcsDestinationIn": "_redis_44_GcsDestinationIn",
        "GcsDestinationOut": "_redis_45_GcsDestinationOut",
        "GcsSourceIn": "_redis_46_GcsSourceIn",
        "GcsSourceOut": "_redis_47_GcsSourceOut",
        "MaintenanceScheduleIn": "_redis_48_MaintenanceScheduleIn",
        "MaintenanceScheduleOut": "_redis_49_MaintenanceScheduleOut",
        "LocationIn": "_redis_50_LocationIn",
        "LocationOut": "_redis_51_LocationOut",
        "PersistenceConfigIn": "_redis_52_PersistenceConfigIn",
        "PersistenceConfigOut": "_redis_53_PersistenceConfigOut",
        "MaintenancePolicyIn": "_redis_54_MaintenancePolicyIn",
        "MaintenancePolicyOut": "_redis_55_MaintenancePolicyOut",
        "WeeklyMaintenanceWindowIn": "_redis_56_WeeklyMaintenanceWindowIn",
        "WeeklyMaintenanceWindowOut": "_redis_57_WeeklyMaintenanceWindowOut",
        "StatusIn": "_redis_58_StatusIn",
        "StatusOut": "_redis_59_StatusOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["NodeInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["NodeInfoIn"]
    )
    types["NodeInfoOut"] = t.struct(
        {
            "id": t.string().optional(),
            "zone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeInfoOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
            "seconds": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
            "seconds": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["GoogleCloudRedisV1LocationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRedisV1LocationMetadataIn"])
    types["GoogleCloudRedisV1LocationMetadataOut"] = t.struct(
        {
            "availableZones": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRedisV1LocationMetadataOut"])
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
    types["FailoverInstanceRequestIn"] = t.struct(
        {"dataProtectionMode": t.string().optional()}
    ).named(renames["FailoverInstanceRequestIn"])
    types["FailoverInstanceRequestOut"] = t.struct(
        {
            "dataProtectionMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FailoverInstanceRequestOut"])
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
    types["GoogleCloudRedisV1ZoneMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudRedisV1ZoneMetadataIn"])
    types["GoogleCloudRedisV1ZoneMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudRedisV1ZoneMetadataOut"])
    types["InputConfigIn"] = t.struct(
        {"gcsSource": t.proxy(renames["GcsSourceIn"]).optional()}
    ).named(renames["InputConfigIn"])
    types["InputConfigOut"] = t.struct(
        {
            "gcsSource": t.proxy(renames["GcsSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InputConfigOut"])
    types["GoogleCloudRedisV1OperationMetadataIn"] = t.struct(
        {
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "statusDetail": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudRedisV1OperationMetadataIn"])
    types["GoogleCloudRedisV1OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "statusDetail": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRedisV1OperationMetadataOut"])
    types["InstanceIn"] = t.struct(
        {
            "secondaryIpRange": t.string().optional(),
            "persistenceConfig": t.proxy(renames["PersistenceConfigIn"]).optional(),
            "suspensionReasons": t.array(t.string()).optional(),
            "connectMode": t.string().optional(),
            "maintenanceVersion": t.string().optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "replicaCount": t.integer().optional(),
            "availableMaintenanceVersions": t.array(t.string()).optional(),
            "readReplicasMode": t.string().optional(),
            "redisConfigs": t.struct({"_": t.string().optional()}).optional(),
            "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]).optional(),
            "customerManagedKey": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "reservedIpRange": t.string().optional(),
            "alternativeLocationId": t.string().optional(),
            "name": t.string(),
            "transitEncryptionMode": t.string().optional(),
            "redisVersion": t.string().optional(),
            "tier": t.string(),
            "authEnabled": t.boolean().optional(),
            "authorizedNetwork": t.string().optional(),
            "memorySizeGb": t.integer(),
        }
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "secondaryIpRange": t.string().optional(),
            "port": t.integer().optional(),
            "persistenceConfig": t.proxy(renames["PersistenceConfigOut"]).optional(),
            "suspensionReasons": t.array(t.string()).optional(),
            "readEndpoint": t.string().optional(),
            "connectMode": t.string().optional(),
            "persistenceIamIdentity": t.string().optional(),
            "maintenanceVersion": t.string().optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "replicaCount": t.integer().optional(),
            "statusMessage": t.string().optional(),
            "maintenanceSchedule": t.proxy(
                renames["MaintenanceScheduleOut"]
            ).optional(),
            "availableMaintenanceVersions": t.array(t.string()).optional(),
            "readReplicasMode": t.string().optional(),
            "redisConfigs": t.struct({"_": t.string().optional()}).optional(),
            "host": t.string().optional(),
            "maintenancePolicy": t.proxy(renames["MaintenancePolicyOut"]).optional(),
            "customerManagedKey": t.string().optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "serverCaCerts": t.array(t.proxy(renames["TlsCertificateOut"])).optional(),
            "reservedIpRange": t.string().optional(),
            "alternativeLocationId": t.string().optional(),
            "name": t.string(),
            "nodes": t.array(t.proxy(renames["NodeInfoOut"])).optional(),
            "transitEncryptionMode": t.string().optional(),
            "redisVersion": t.string().optional(),
            "tier": t.string(),
            "createTime": t.string().optional(),
            "readEndpointPort": t.integer().optional(),
            "currentLocationId": t.string().optional(),
            "authEnabled": t.boolean().optional(),
            "authorizedNetwork": t.string().optional(),
            "memorySizeGb": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
    types["ImportInstanceRequestIn"] = t.struct(
        {"inputConfig": t.proxy(renames["InputConfigIn"])}
    ).named(renames["ImportInstanceRequestIn"])
    types["ImportInstanceRequestOut"] = t.struct(
        {
            "inputConfig": t.proxy(renames["InputConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportInstanceRequestOut"])
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
            "sha1Fingerprint": t.string().optional(),
            "expireTime": t.string().optional(),
            "createTime": t.string().optional(),
            "serialNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TlsCertificateOut"])
    types["OutputConfigIn"] = t.struct(
        {"gcsDestination": t.proxy(renames["GcsDestinationIn"]).optional()}
    ).named(renames["OutputConfigIn"])
    types["OutputConfigOut"] = t.struct(
        {
            "gcsDestination": t.proxy(renames["GcsDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutputConfigOut"])
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
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["InstanceAuthStringIn"] = t.struct(
        {"authString": t.string().optional()}
    ).named(renames["InstanceAuthStringIn"])
    types["InstanceAuthStringOut"] = t.struct(
        {
            "authString": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceAuthStringOut"])
    types["ExportInstanceRequestIn"] = t.struct(
        {"outputConfig": t.proxy(renames["OutputConfigIn"])}
    ).named(renames["ExportInstanceRequestIn"])
    types["ExportInstanceRequestOut"] = t.struct(
        {
            "outputConfig": t.proxy(renames["OutputConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportInstanceRequestOut"])
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
    types["MaintenanceScheduleIn"] = t.struct(
        {"canReschedule": t.boolean().optional()}
    ).named(renames["MaintenanceScheduleIn"])
    types["MaintenanceScheduleOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "canReschedule": t.boolean().optional(),
            "endTime": t.string().optional(),
            "scheduleDeadlineTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceScheduleOut"])
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["PersistenceConfigIn"] = t.struct(
        {
            "rdbSnapshotStartTime": t.string().optional(),
            "rdbSnapshotPeriod": t.string().optional(),
            "persistenceMode": t.string().optional(),
        }
    ).named(renames["PersistenceConfigIn"])
    types["PersistenceConfigOut"] = t.struct(
        {
            "rdbSnapshotStartTime": t.string().optional(),
            "rdbNextSnapshotTime": t.string().optional(),
            "rdbSnapshotPeriod": t.string().optional(),
            "persistenceMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersistenceConfigOut"])
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
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "weeklyMaintenanceWindow": t.array(
                t.proxy(renames["WeeklyMaintenanceWindowOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenancePolicyOut"])
    types["WeeklyMaintenanceWindowIn"] = t.struct(
        {"startTime": t.proxy(renames["TimeOfDayIn"]), "day": t.string()}
    ).named(renames["WeeklyMaintenanceWindowIn"])
    types["WeeklyMaintenanceWindowOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "startTime": t.proxy(renames["TimeOfDayOut"]),
            "day": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WeeklyMaintenanceWindowOut"])
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
    functions["projectsLocationsGet"] = redis.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesGet"] = redis.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "instanceId": t.string(),
                "secondaryIpRange": t.string().optional(),
                "persistenceConfig": t.proxy(renames["PersistenceConfigIn"]).optional(),
                "suspensionReasons": t.array(t.string()).optional(),
                "connectMode": t.string().optional(),
                "maintenanceVersion": t.string().optional(),
                "displayName": t.string().optional(),
                "locationId": t.string().optional(),
                "replicaCount": t.integer().optional(),
                "availableMaintenanceVersions": t.array(t.string()).optional(),
                "readReplicasMode": t.string().optional(),
                "redisConfigs": t.struct({"_": t.string().optional()}).optional(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]).optional(),
                "customerManagedKey": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "reservedIpRange": t.string().optional(),
                "alternativeLocationId": t.string().optional(),
                "name": t.string(),
                "transitEncryptionMode": t.string().optional(),
                "redisVersion": t.string().optional(),
                "tier": t.string(),
                "authEnabled": t.boolean().optional(),
                "authorizedNetwork": t.string().optional(),
                "memorySizeGb": t.integer(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesFailover"] = redis.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "instanceId": t.string(),
                "secondaryIpRange": t.string().optional(),
                "persistenceConfig": t.proxy(renames["PersistenceConfigIn"]).optional(),
                "suspensionReasons": t.array(t.string()).optional(),
                "connectMode": t.string().optional(),
                "maintenanceVersion": t.string().optional(),
                "displayName": t.string().optional(),
                "locationId": t.string().optional(),
                "replicaCount": t.integer().optional(),
                "availableMaintenanceVersions": t.array(t.string()).optional(),
                "readReplicasMode": t.string().optional(),
                "redisConfigs": t.struct({"_": t.string().optional()}).optional(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]).optional(),
                "customerManagedKey": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "reservedIpRange": t.string().optional(),
                "alternativeLocationId": t.string().optional(),
                "name": t.string(),
                "transitEncryptionMode": t.string().optional(),
                "redisVersion": t.string().optional(),
                "tier": t.string(),
                "authEnabled": t.boolean().optional(),
                "authorizedNetwork": t.string().optional(),
                "memorySizeGb": t.integer(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesGetAuthString"] = redis.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "instanceId": t.string(),
                "secondaryIpRange": t.string().optional(),
                "persistenceConfig": t.proxy(renames["PersistenceConfigIn"]).optional(),
                "suspensionReasons": t.array(t.string()).optional(),
                "connectMode": t.string().optional(),
                "maintenanceVersion": t.string().optional(),
                "displayName": t.string().optional(),
                "locationId": t.string().optional(),
                "replicaCount": t.integer().optional(),
                "availableMaintenanceVersions": t.array(t.string()).optional(),
                "readReplicasMode": t.string().optional(),
                "redisConfigs": t.struct({"_": t.string().optional()}).optional(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]).optional(),
                "customerManagedKey": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "reservedIpRange": t.string().optional(),
                "alternativeLocationId": t.string().optional(),
                "name": t.string(),
                "transitEncryptionMode": t.string().optional(),
                "redisVersion": t.string().optional(),
                "tier": t.string(),
                "authEnabled": t.boolean().optional(),
                "authorizedNetwork": t.string().optional(),
                "memorySizeGb": t.integer(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesRescheduleMaintenance"] = redis.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "instanceId": t.string(),
                "secondaryIpRange": t.string().optional(),
                "persistenceConfig": t.proxy(renames["PersistenceConfigIn"]).optional(),
                "suspensionReasons": t.array(t.string()).optional(),
                "connectMode": t.string().optional(),
                "maintenanceVersion": t.string().optional(),
                "displayName": t.string().optional(),
                "locationId": t.string().optional(),
                "replicaCount": t.integer().optional(),
                "availableMaintenanceVersions": t.array(t.string()).optional(),
                "readReplicasMode": t.string().optional(),
                "redisConfigs": t.struct({"_": t.string().optional()}).optional(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]).optional(),
                "customerManagedKey": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "reservedIpRange": t.string().optional(),
                "alternativeLocationId": t.string().optional(),
                "name": t.string(),
                "transitEncryptionMode": t.string().optional(),
                "redisVersion": t.string().optional(),
                "tier": t.string(),
                "authEnabled": t.boolean().optional(),
                "authorizedNetwork": t.string().optional(),
                "memorySizeGb": t.integer(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDelete"] = redis.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "instanceId": t.string(),
                "secondaryIpRange": t.string().optional(),
                "persistenceConfig": t.proxy(renames["PersistenceConfigIn"]).optional(),
                "suspensionReasons": t.array(t.string()).optional(),
                "connectMode": t.string().optional(),
                "maintenanceVersion": t.string().optional(),
                "displayName": t.string().optional(),
                "locationId": t.string().optional(),
                "replicaCount": t.integer().optional(),
                "availableMaintenanceVersions": t.array(t.string()).optional(),
                "readReplicasMode": t.string().optional(),
                "redisConfigs": t.struct({"_": t.string().optional()}).optional(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]).optional(),
                "customerManagedKey": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "reservedIpRange": t.string().optional(),
                "alternativeLocationId": t.string().optional(),
                "name": t.string(),
                "transitEncryptionMode": t.string().optional(),
                "redisVersion": t.string().optional(),
                "tier": t.string(),
                "authEnabled": t.boolean().optional(),
                "authorizedNetwork": t.string().optional(),
                "memorySizeGb": t.integer(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesPatch"] = redis.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "instanceId": t.string(),
                "secondaryIpRange": t.string().optional(),
                "persistenceConfig": t.proxy(renames["PersistenceConfigIn"]).optional(),
                "suspensionReasons": t.array(t.string()).optional(),
                "connectMode": t.string().optional(),
                "maintenanceVersion": t.string().optional(),
                "displayName": t.string().optional(),
                "locationId": t.string().optional(),
                "replicaCount": t.integer().optional(),
                "availableMaintenanceVersions": t.array(t.string()).optional(),
                "readReplicasMode": t.string().optional(),
                "redisConfigs": t.struct({"_": t.string().optional()}).optional(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]).optional(),
                "customerManagedKey": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "reservedIpRange": t.string().optional(),
                "alternativeLocationId": t.string().optional(),
                "name": t.string(),
                "transitEncryptionMode": t.string().optional(),
                "redisVersion": t.string().optional(),
                "tier": t.string(),
                "authEnabled": t.boolean().optional(),
                "authorizedNetwork": t.string().optional(),
                "memorySizeGb": t.integer(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesUpgrade"] = redis.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "instanceId": t.string(),
                "secondaryIpRange": t.string().optional(),
                "persistenceConfig": t.proxy(renames["PersistenceConfigIn"]).optional(),
                "suspensionReasons": t.array(t.string()).optional(),
                "connectMode": t.string().optional(),
                "maintenanceVersion": t.string().optional(),
                "displayName": t.string().optional(),
                "locationId": t.string().optional(),
                "replicaCount": t.integer().optional(),
                "availableMaintenanceVersions": t.array(t.string()).optional(),
                "readReplicasMode": t.string().optional(),
                "redisConfigs": t.struct({"_": t.string().optional()}).optional(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]).optional(),
                "customerManagedKey": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "reservedIpRange": t.string().optional(),
                "alternativeLocationId": t.string().optional(),
                "name": t.string(),
                "transitEncryptionMode": t.string().optional(),
                "redisVersion": t.string().optional(),
                "tier": t.string(),
                "authEnabled": t.boolean().optional(),
                "authorizedNetwork": t.string().optional(),
                "memorySizeGb": t.integer(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesList"] = redis.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "instanceId": t.string(),
                "secondaryIpRange": t.string().optional(),
                "persistenceConfig": t.proxy(renames["PersistenceConfigIn"]).optional(),
                "suspensionReasons": t.array(t.string()).optional(),
                "connectMode": t.string().optional(),
                "maintenanceVersion": t.string().optional(),
                "displayName": t.string().optional(),
                "locationId": t.string().optional(),
                "replicaCount": t.integer().optional(),
                "availableMaintenanceVersions": t.array(t.string()).optional(),
                "readReplicasMode": t.string().optional(),
                "redisConfigs": t.struct({"_": t.string().optional()}).optional(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]).optional(),
                "customerManagedKey": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "reservedIpRange": t.string().optional(),
                "alternativeLocationId": t.string().optional(),
                "name": t.string(),
                "transitEncryptionMode": t.string().optional(),
                "redisVersion": t.string().optional(),
                "tier": t.string(),
                "authEnabled": t.boolean().optional(),
                "authorizedNetwork": t.string().optional(),
                "memorySizeGb": t.integer(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesImport"] = redis.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "instanceId": t.string(),
                "secondaryIpRange": t.string().optional(),
                "persistenceConfig": t.proxy(renames["PersistenceConfigIn"]).optional(),
                "suspensionReasons": t.array(t.string()).optional(),
                "connectMode": t.string().optional(),
                "maintenanceVersion": t.string().optional(),
                "displayName": t.string().optional(),
                "locationId": t.string().optional(),
                "replicaCount": t.integer().optional(),
                "availableMaintenanceVersions": t.array(t.string()).optional(),
                "readReplicasMode": t.string().optional(),
                "redisConfigs": t.struct({"_": t.string().optional()}).optional(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]).optional(),
                "customerManagedKey": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "reservedIpRange": t.string().optional(),
                "alternativeLocationId": t.string().optional(),
                "name": t.string(),
                "transitEncryptionMode": t.string().optional(),
                "redisVersion": t.string().optional(),
                "tier": t.string(),
                "authEnabled": t.boolean().optional(),
                "authorizedNetwork": t.string().optional(),
                "memorySizeGb": t.integer(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesExport"] = redis.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "instanceId": t.string(),
                "secondaryIpRange": t.string().optional(),
                "persistenceConfig": t.proxy(renames["PersistenceConfigIn"]).optional(),
                "suspensionReasons": t.array(t.string()).optional(),
                "connectMode": t.string().optional(),
                "maintenanceVersion": t.string().optional(),
                "displayName": t.string().optional(),
                "locationId": t.string().optional(),
                "replicaCount": t.integer().optional(),
                "availableMaintenanceVersions": t.array(t.string()).optional(),
                "readReplicasMode": t.string().optional(),
                "redisConfigs": t.struct({"_": t.string().optional()}).optional(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]).optional(),
                "customerManagedKey": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "reservedIpRange": t.string().optional(),
                "alternativeLocationId": t.string().optional(),
                "name": t.string(),
                "transitEncryptionMode": t.string().optional(),
                "redisVersion": t.string().optional(),
                "tier": t.string(),
                "authEnabled": t.boolean().optional(),
                "authorizedNetwork": t.string().optional(),
                "memorySizeGb": t.integer(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesCreate"] = redis.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "instanceId": t.string(),
                "secondaryIpRange": t.string().optional(),
                "persistenceConfig": t.proxy(renames["PersistenceConfigIn"]).optional(),
                "suspensionReasons": t.array(t.string()).optional(),
                "connectMode": t.string().optional(),
                "maintenanceVersion": t.string().optional(),
                "displayName": t.string().optional(),
                "locationId": t.string().optional(),
                "replicaCount": t.integer().optional(),
                "availableMaintenanceVersions": t.array(t.string()).optional(),
                "readReplicasMode": t.string().optional(),
                "redisConfigs": t.struct({"_": t.string().optional()}).optional(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]).optional(),
                "customerManagedKey": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "reservedIpRange": t.string().optional(),
                "alternativeLocationId": t.string().optional(),
                "name": t.string(),
                "transitEncryptionMode": t.string().optional(),
                "redisVersion": t.string().optional(),
                "tier": t.string(),
                "authEnabled": t.boolean().optional(),
                "authorizedNetwork": t.string().optional(),
                "memorySizeGb": t.integer(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = redis.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = redis.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = redis.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = redis.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="redis", renames=renames, types=Box(types), functions=Box(functions)
    )
