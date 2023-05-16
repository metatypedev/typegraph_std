from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_metastore() -> Import:
    metastore = HTTPRuntime("https://metastore.googleapis.com/")

    renames = {
        "ErrorResponse": "_metastore_1_ErrorResponse",
        "AuditConfigIn": "_metastore_2_AuditConfigIn",
        "AuditConfigOut": "_metastore_3_AuditConfigOut",
        "MaintenanceWindowIn": "_metastore_4_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_metastore_5_MaintenanceWindowOut",
        "ExportMetadataRequestIn": "_metastore_6_ExportMetadataRequestIn",
        "ExportMetadataRequestOut": "_metastore_7_ExportMetadataRequestOut",
        "DatabaseDumpIn": "_metastore_8_DatabaseDumpIn",
        "DatabaseDumpOut": "_metastore_9_DatabaseDumpOut",
        "RestoreServiceRequestIn": "_metastore_10_RestoreServiceRequestIn",
        "RestoreServiceRequestOut": "_metastore_11_RestoreServiceRequestOut",
        "MetadataExportIn": "_metastore_12_MetadataExportIn",
        "MetadataExportOut": "_metastore_13_MetadataExportOut",
        "TestIamPermissionsRequestIn": "_metastore_14_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_metastore_15_TestIamPermissionsRequestOut",
        "EmptyIn": "_metastore_16_EmptyIn",
        "EmptyOut": "_metastore_17_EmptyOut",
        "ListLocationsResponseIn": "_metastore_18_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_metastore_19_ListLocationsResponseOut",
        "HiveMetastoreConfigIn": "_metastore_20_HiveMetastoreConfigIn",
        "HiveMetastoreConfigOut": "_metastore_21_HiveMetastoreConfigOut",
        "AlterMetadataResourceLocationRequestIn": "_metastore_22_AlterMetadataResourceLocationRequestIn",
        "AlterMetadataResourceLocationRequestOut": "_metastore_23_AlterMetadataResourceLocationRequestOut",
        "ServiceIn": "_metastore_24_ServiceIn",
        "ServiceOut": "_metastore_25_ServiceOut",
        "AlterMetadataResourceLocationResponseIn": "_metastore_26_AlterMetadataResourceLocationResponseIn",
        "AlterMetadataResourceLocationResponseOut": "_metastore_27_AlterMetadataResourceLocationResponseOut",
        "ListFederationsResponseIn": "_metastore_28_ListFederationsResponseIn",
        "ListFederationsResponseOut": "_metastore_29_ListFederationsResponseOut",
        "ListBackupsResponseIn": "_metastore_30_ListBackupsResponseIn",
        "ListBackupsResponseOut": "_metastore_31_ListBackupsResponseOut",
        "OperationMetadataIn": "_metastore_32_OperationMetadataIn",
        "OperationMetadataOut": "_metastore_33_OperationMetadataOut",
        "ListServicesResponseIn": "_metastore_34_ListServicesResponseIn",
        "ListServicesResponseOut": "_metastore_35_ListServicesResponseOut",
        "SetIamPolicyRequestIn": "_metastore_36_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_metastore_37_SetIamPolicyRequestOut",
        "StatusIn": "_metastore_38_StatusIn",
        "StatusOut": "_metastore_39_StatusOut",
        "PolicyIn": "_metastore_40_PolicyIn",
        "PolicyOut": "_metastore_41_PolicyOut",
        "ScalingConfigIn": "_metastore_42_ScalingConfigIn",
        "ScalingConfigOut": "_metastore_43_ScalingConfigOut",
        "LocationIn": "_metastore_44_LocationIn",
        "LocationOut": "_metastore_45_LocationOut",
        "BackendMetastoreIn": "_metastore_46_BackendMetastoreIn",
        "BackendMetastoreOut": "_metastore_47_BackendMetastoreOut",
        "OperationIn": "_metastore_48_OperationIn",
        "OperationOut": "_metastore_49_OperationOut",
        "KerberosConfigIn": "_metastore_50_KerberosConfigIn",
        "KerberosConfigOut": "_metastore_51_KerberosConfigOut",
        "MoveTableToDatabaseResponseIn": "_metastore_52_MoveTableToDatabaseResponseIn",
        "MoveTableToDatabaseResponseOut": "_metastore_53_MoveTableToDatabaseResponseOut",
        "AuditLogConfigIn": "_metastore_54_AuditLogConfigIn",
        "AuditLogConfigOut": "_metastore_55_AuditLogConfigOut",
        "SecretIn": "_metastore_56_SecretIn",
        "SecretOut": "_metastore_57_SecretOut",
        "MoveTableToDatabaseRequestIn": "_metastore_58_MoveTableToDatabaseRequestIn",
        "MoveTableToDatabaseRequestOut": "_metastore_59_MoveTableToDatabaseRequestOut",
        "ListOperationsResponseIn": "_metastore_60_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_metastore_61_ListOperationsResponseOut",
        "QueryMetadataRequestIn": "_metastore_62_QueryMetadataRequestIn",
        "QueryMetadataRequestOut": "_metastore_63_QueryMetadataRequestOut",
        "MetadataImportIn": "_metastore_64_MetadataImportIn",
        "MetadataImportOut": "_metastore_65_MetadataImportOut",
        "TestIamPermissionsResponseIn": "_metastore_66_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_metastore_67_TestIamPermissionsResponseOut",
        "ListMetadataImportsResponseIn": "_metastore_68_ListMetadataImportsResponseIn",
        "ListMetadataImportsResponseOut": "_metastore_69_ListMetadataImportsResponseOut",
        "NetworkConfigIn": "_metastore_70_NetworkConfigIn",
        "NetworkConfigOut": "_metastore_71_NetworkConfigOut",
        "FederationIn": "_metastore_72_FederationIn",
        "FederationOut": "_metastore_73_FederationOut",
        "RestoreIn": "_metastore_74_RestoreIn",
        "RestoreOut": "_metastore_75_RestoreOut",
        "LocationMetadataIn": "_metastore_76_LocationMetadataIn",
        "LocationMetadataOut": "_metastore_77_LocationMetadataOut",
        "TelemetryConfigIn": "_metastore_78_TelemetryConfigIn",
        "TelemetryConfigOut": "_metastore_79_TelemetryConfigOut",
        "EncryptionConfigIn": "_metastore_80_EncryptionConfigIn",
        "EncryptionConfigOut": "_metastore_81_EncryptionConfigOut",
        "AuxiliaryVersionConfigIn": "_metastore_82_AuxiliaryVersionConfigIn",
        "AuxiliaryVersionConfigOut": "_metastore_83_AuxiliaryVersionConfigOut",
        "QueryMetadataResponseIn": "_metastore_84_QueryMetadataResponseIn",
        "QueryMetadataResponseOut": "_metastore_85_QueryMetadataResponseOut",
        "ErrorDetailsIn": "_metastore_86_ErrorDetailsIn",
        "ErrorDetailsOut": "_metastore_87_ErrorDetailsOut",
        "BackupIn": "_metastore_88_BackupIn",
        "BackupOut": "_metastore_89_BackupOut",
        "HiveMetastoreVersionIn": "_metastore_90_HiveMetastoreVersionIn",
        "HiveMetastoreVersionOut": "_metastore_91_HiveMetastoreVersionOut",
        "ExprIn": "_metastore_92_ExprIn",
        "ExprOut": "_metastore_93_ExprOut",
        "MetadataManagementActivityIn": "_metastore_94_MetadataManagementActivityIn",
        "MetadataManagementActivityOut": "_metastore_95_MetadataManagementActivityOut",
        "ConsumerIn": "_metastore_96_ConsumerIn",
        "ConsumerOut": "_metastore_97_ConsumerOut",
        "BindingIn": "_metastore_98_BindingIn",
        "BindingOut": "_metastore_99_BindingOut",
        "CancelOperationRequestIn": "_metastore_100_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_metastore_101_CancelOperationRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AuditConfigIn"] = t.struct(
        {
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
            "service": t.string().optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])
    types["MaintenanceWindowIn"] = t.struct(
        {"hourOfDay": t.integer().optional(), "dayOfWeek": t.string().optional()}
    ).named(renames["MaintenanceWindowIn"])
    types["MaintenanceWindowOut"] = t.struct(
        {
            "hourOfDay": t.integer().optional(),
            "dayOfWeek": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceWindowOut"])
    types["ExportMetadataRequestIn"] = t.struct(
        {
            "destinationGcsFolder": t.string().optional(),
            "databaseDumpType": t.string().optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["ExportMetadataRequestIn"])
    types["ExportMetadataRequestOut"] = t.struct(
        {
            "destinationGcsFolder": t.string().optional(),
            "databaseDumpType": t.string().optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportMetadataRequestOut"])
    types["DatabaseDumpIn"] = t.struct(
        {
            "type": t.string().optional(),
            "databaseType": t.string().optional(),
            "gcsUri": t.string().optional(),
            "sourceDatabase": t.string().optional(),
        }
    ).named(renames["DatabaseDumpIn"])
    types["DatabaseDumpOut"] = t.struct(
        {
            "type": t.string().optional(),
            "databaseType": t.string().optional(),
            "gcsUri": t.string().optional(),
            "sourceDatabase": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseDumpOut"])
    types["RestoreServiceRequestIn"] = t.struct(
        {
            "requestId": t.string().optional(),
            "backup": t.string(),
            "restoreType": t.string().optional(),
        }
    ).named(renames["RestoreServiceRequestIn"])
    types["RestoreServiceRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "backup": t.string(),
            "restoreType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreServiceRequestOut"])
    types["MetadataExportIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MetadataExportIn"]
    )
    types["MetadataExportOut"] = t.struct(
        {
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "destinationGcsUri": t.string().optional(),
            "databaseDumpType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataExportOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["HiveMetastoreConfigIn"] = t.struct(
        {
            "kerberosConfig": t.proxy(renames["KerberosConfigIn"]).optional(),
            "configOverrides": t.struct({"_": t.string().optional()}).optional(),
            "auxiliaryVersions": t.struct({"_": t.string().optional()}).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["HiveMetastoreConfigIn"])
    types["HiveMetastoreConfigOut"] = t.struct(
        {
            "kerberosConfig": t.proxy(renames["KerberosConfigOut"]).optional(),
            "configOverrides": t.struct({"_": t.string().optional()}).optional(),
            "auxiliaryVersions": t.struct({"_": t.string().optional()}).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HiveMetastoreConfigOut"])
    types["AlterMetadataResourceLocationRequestIn"] = t.struct(
        {"locationUri": t.string(), "resourceName": t.string()}
    ).named(renames["AlterMetadataResourceLocationRequestIn"])
    types["AlterMetadataResourceLocationRequestOut"] = t.struct(
        {
            "locationUri": t.string(),
            "resourceName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlterMetadataResourceLocationRequestOut"])
    types["ServiceIn"] = t.struct(
        {
            "telemetryConfig": t.proxy(renames["TelemetryConfigIn"]).optional(),
            "scalingConfig": t.proxy(renames["ScalingConfigIn"]).optional(),
            "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "databaseType": t.string().optional(),
            "tier": t.string().optional(),
            "name": t.string().optional(),
            "port": t.integer().optional(),
            "releaseChannel": t.string().optional(),
            "network": t.string().optional(),
            "hiveMetastoreConfig": t.proxy(renames["HiveMetastoreConfigIn"]).optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigIn"]).optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowIn"]).optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "telemetryConfig": t.proxy(renames["TelemetryConfigOut"]).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "scalingConfig": t.proxy(renames["ScalingConfigOut"]).optional(),
            "endpointUri": t.string().optional(),
            "networkConfig": t.proxy(renames["NetworkConfigOut"]).optional(),
            "artifactGcsUri": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "databaseType": t.string().optional(),
            "tier": t.string().optional(),
            "uid": t.string().optional(),
            "name": t.string().optional(),
            "metadataManagementActivity": t.proxy(
                renames["MetadataManagementActivityOut"]
            ).optional(),
            "port": t.integer().optional(),
            "releaseChannel": t.string().optional(),
            "network": t.string().optional(),
            "hiveMetastoreConfig": t.proxy(
                renames["HiveMetastoreConfigOut"]
            ).optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigOut"]).optional(),
            "state": t.string().optional(),
            "stateMessage": t.string().optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
    types["AlterMetadataResourceLocationResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AlterMetadataResourceLocationResponseIn"])
    types["AlterMetadataResourceLocationResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AlterMetadataResourceLocationResponseOut"])
    types["ListFederationsResponseIn"] = t.struct(
        {
            "federations": t.array(t.proxy(renames["FederationIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListFederationsResponseIn"])
    types["ListFederationsResponseOut"] = t.struct(
        {
            "federations": t.array(t.proxy(renames["FederationOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFederationsResponseOut"])
    types["ListBackupsResponseIn"] = t.struct(
        {
            "backups": t.array(t.proxy(renames["BackupIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListBackupsResponseIn"])
    types["ListBackupsResponseOut"] = t.struct(
        {
            "backups": t.array(t.proxy(renames["BackupOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBackupsResponseOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "statusMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["ListServicesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "services": t.array(t.proxy(renames["ServiceIn"])).optional(),
        }
    ).named(renames["ListServicesResponseIn"])
    types["ListServicesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "services": t.array(t.proxy(renames["ServiceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServicesResponseOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["PolicyIn"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ScalingConfigIn"] = t.struct(
        {"scalingFactor": t.number().optional(), "instanceSize": t.string().optional()}
    ).named(renames["ScalingConfigIn"])
    types["ScalingConfigOut"] = t.struct(
        {
            "scalingFactor": t.number().optional(),
            "instanceSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScalingConfigOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["BackendMetastoreIn"] = t.struct(
        {"name": t.string().optional(), "metastoreType": t.string().optional()}
    ).named(renames["BackendMetastoreIn"])
    types["BackendMetastoreOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metastoreType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendMetastoreOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["KerberosConfigIn"] = t.struct(
        {
            "krb5ConfigGcsUri": t.string().optional(),
            "principal": t.string().optional(),
            "keytab": t.proxy(renames["SecretIn"]).optional(),
        }
    ).named(renames["KerberosConfigIn"])
    types["KerberosConfigOut"] = t.struct(
        {
            "krb5ConfigGcsUri": t.string().optional(),
            "principal": t.string().optional(),
            "keytab": t.proxy(renames["SecretOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KerberosConfigOut"])
    types["MoveTableToDatabaseResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["MoveTableToDatabaseResponseIn"])
    types["MoveTableToDatabaseResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MoveTableToDatabaseResponseOut"])
    types["AuditLogConfigIn"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
    types["SecretIn"] = t.struct({"cloudSecret": t.string().optional()}).named(
        renames["SecretIn"]
    )
    types["SecretOut"] = t.struct(
        {
            "cloudSecret": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretOut"])
    types["MoveTableToDatabaseRequestIn"] = t.struct(
        {"dbName": t.string(), "destinationDbName": t.string(), "tableName": t.string()}
    ).named(renames["MoveTableToDatabaseRequestIn"])
    types["MoveTableToDatabaseRequestOut"] = t.struct(
        {
            "dbName": t.string(),
            "destinationDbName": t.string(),
            "tableName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveTableToDatabaseRequestOut"])
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
    types["QueryMetadataRequestIn"] = t.struct({"query": t.string()}).named(
        renames["QueryMetadataRequestIn"]
    )
    types["QueryMetadataRequestOut"] = t.struct(
        {"query": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["QueryMetadataRequestOut"])
    types["MetadataImportIn"] = t.struct(
        {
            "name": t.string().optional(),
            "description": t.string().optional(),
            "databaseDump": t.proxy(renames["DatabaseDumpIn"]).optional(),
        }
    ).named(renames["MetadataImportIn"])
    types["MetadataImportOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "databaseDump": t.proxy(renames["DatabaseDumpOut"]).optional(),
            "updateTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataImportOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["ListMetadataImportsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "metadataImports": t.array(t.proxy(renames["MetadataImportIn"])).optional(),
        }
    ).named(renames["ListMetadataImportsResponseIn"])
    types["ListMetadataImportsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "metadataImports": t.array(
                t.proxy(renames["MetadataImportOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMetadataImportsResponseOut"])
    types["NetworkConfigIn"] = t.struct(
        {"consumers": t.array(t.proxy(renames["ConsumerIn"])).optional()}
    ).named(renames["NetworkConfigIn"])
    types["NetworkConfigOut"] = t.struct(
        {
            "consumers": t.array(t.proxy(renames["ConsumerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConfigOut"])
    types["FederationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "version": t.string().optional(),
            "backendMetastores": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["FederationIn"])
    types["FederationOut"] = t.struct(
        {
            "uid": t.string().optional(),
            "name": t.string().optional(),
            "endpointUri": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "version": t.string().optional(),
            "state": t.string().optional(),
            "stateMessage": t.string().optional(),
            "backendMetastores": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FederationOut"])
    types["RestoreIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RestoreIn"]
    )
    types["RestoreOut"] = t.struct(
        {
            "type": t.string().optional(),
            "details": t.string().optional(),
            "backup": t.string().optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreOut"])
    types["LocationMetadataIn"] = t.struct(
        {
            "supportedHiveMetastoreVersions": t.array(
                t.proxy(renames["HiveMetastoreVersionIn"])
            ).optional()
        }
    ).named(renames["LocationMetadataIn"])
    types["LocationMetadataOut"] = t.struct(
        {
            "supportedHiveMetastoreVersions": t.array(
                t.proxy(renames["HiveMetastoreVersionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationMetadataOut"])
    types["TelemetryConfigIn"] = t.struct({"logFormat": t.string().optional()}).named(
        renames["TelemetryConfigIn"]
    )
    types["TelemetryConfigOut"] = t.struct(
        {
            "logFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TelemetryConfigOut"])
    types["EncryptionConfigIn"] = t.struct({"kmsKey": t.string().optional()}).named(
        renames["EncryptionConfigIn"]
    )
    types["EncryptionConfigOut"] = t.struct(
        {
            "kmsKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionConfigOut"])
    types["AuxiliaryVersionConfigIn"] = t.struct(
        {
            "configOverrides": t.struct({"_": t.string().optional()}).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["AuxiliaryVersionConfigIn"])
    types["AuxiliaryVersionConfigOut"] = t.struct(
        {
            "networkConfig": t.proxy(renames["NetworkConfigOut"]).optional(),
            "configOverrides": t.struct({"_": t.string().optional()}).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuxiliaryVersionConfigOut"])
    types["QueryMetadataResponseIn"] = t.struct(
        {"resultManifestUri": t.string().optional()}
    ).named(renames["QueryMetadataResponseIn"])
    types["QueryMetadataResponseOut"] = t.struct(
        {
            "resultManifestUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryMetadataResponseOut"])
    types["ErrorDetailsIn"] = t.struct(
        {"details": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["ErrorDetailsIn"])
    types["ErrorDetailsOut"] = t.struct(
        {
            "details": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorDetailsOut"])
    types["BackupIn"] = t.struct(
        {"description": t.string().optional(), "name": t.string().optional()}
    ).named(renames["BackupIn"])
    types["BackupOut"] = t.struct(
        {
            "restoringServices": t.array(t.string()).optional(),
            "createTime": t.string().optional(),
            "serviceRevision": t.proxy(renames["ServiceOut"]).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupOut"])
    types["HiveMetastoreVersionIn"] = t.struct(
        {"version": t.string().optional(), "isDefault": t.boolean().optional()}
    ).named(renames["HiveMetastoreVersionIn"])
    types["HiveMetastoreVersionOut"] = t.struct(
        {
            "version": t.string().optional(),
            "isDefault": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HiveMetastoreVersionOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["MetadataManagementActivityIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["MetadataManagementActivityIn"])
    types["MetadataManagementActivityOut"] = t.struct(
        {
            "restores": t.array(t.proxy(renames["RestoreOut"])).optional(),
            "metadataExports": t.array(
                t.proxy(renames["MetadataExportOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataManagementActivityOut"])
    types["ConsumerIn"] = t.struct({"subnetwork": t.string().optional()}).named(
        renames["ConsumerIn"]
    )
    types["ConsumerOut"] = t.struct(
        {
            "endpointUri": t.string().optional(),
            "subnetwork": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsumerOut"])
    types["BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])

    functions = {}
    functions["projectsLocationsList"] = metastore.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = metastore.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsPatch"] = metastore.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsList"] = metastore.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsCreate"] = metastore.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsGet"] = metastore.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsSetIamPolicy"] = metastore.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsTestIamPermissions"] = metastore.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsGetIamPolicy"] = metastore.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsDelete"] = metastore.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesList"] = metastore.post(
        "v1/{service}:queryMetadata",
        t.struct(
            {"service": t.string(), "query": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesTestIamPermissions"] = metastore.post(
        "v1/{service}:queryMetadata",
        t.struct(
            {"service": t.string(), "query": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesMoveTableToDatabase"] = metastore.post(
        "v1/{service}:queryMetadata",
        t.struct(
            {"service": t.string(), "query": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesAlterLocation"] = metastore.post(
        "v1/{service}:queryMetadata",
        t.struct(
            {"service": t.string(), "query": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesSetIamPolicy"] = metastore.post(
        "v1/{service}:queryMetadata",
        t.struct(
            {"service": t.string(), "query": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesPatch"] = metastore.post(
        "v1/{service}:queryMetadata",
        t.struct(
            {"service": t.string(), "query": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesExportMetadata"] = metastore.post(
        "v1/{service}:queryMetadata",
        t.struct(
            {"service": t.string(), "query": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesGetIamPolicy"] = metastore.post(
        "v1/{service}:queryMetadata",
        t.struct(
            {"service": t.string(), "query": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesRestore"] = metastore.post(
        "v1/{service}:queryMetadata",
        t.struct(
            {"service": t.string(), "query": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesCreate"] = metastore.post(
        "v1/{service}:queryMetadata",
        t.struct(
            {"service": t.string(), "query": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesDelete"] = metastore.post(
        "v1/{service}:queryMetadata",
        t.struct(
            {"service": t.string(), "query": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesGet"] = metastore.post(
        "v1/{service}:queryMetadata",
        t.struct(
            {"service": t.string(), "query": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesQueryMetadata"] = metastore.post(
        "v1/{service}:queryMetadata",
        t.struct(
            {"service": t.string(), "query": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesMetadataImportsGet"] = metastore.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "databaseDump": t.proxy(renames["DatabaseDumpIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesMetadataImportsCreate"] = metastore.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "databaseDump": t.proxy(renames["DatabaseDumpIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesMetadataImportsList"] = metastore.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "databaseDump": t.proxy(renames["DatabaseDumpIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesMetadataImportsPatch"] = metastore.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "databaseDump": t.proxy(renames["DatabaseDumpIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesBackupsList"] = metastore.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesBackupsGetIamPolicy"] = metastore.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesBackupsGet"] = metastore.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesBackupsCreate"] = metastore.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesBackupsSetIamPolicy"] = metastore.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesBackupsDelete"] = metastore.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = metastore.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = metastore.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = metastore.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = metastore.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="metastore",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
