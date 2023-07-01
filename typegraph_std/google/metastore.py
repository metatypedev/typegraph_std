from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_metastore():
    metastore = HTTPRuntime("https://metastore.googleapis.com/")

    renames = {
        "ErrorResponse": "_metastore_1_ErrorResponse",
        "LocationMetadataIn": "_metastore_2_LocationMetadataIn",
        "LocationMetadataOut": "_metastore_3_LocationMetadataOut",
        "ListOperationsResponseIn": "_metastore_4_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_metastore_5_ListOperationsResponseOut",
        "TestIamPermissionsResponseIn": "_metastore_6_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_metastore_7_TestIamPermissionsResponseOut",
        "EmptyIn": "_metastore_8_EmptyIn",
        "EmptyOut": "_metastore_9_EmptyOut",
        "MetadataManagementActivityIn": "_metastore_10_MetadataManagementActivityIn",
        "MetadataManagementActivityOut": "_metastore_11_MetadataManagementActivityOut",
        "MoveTableToDatabaseRequestIn": "_metastore_12_MoveTableToDatabaseRequestIn",
        "MoveTableToDatabaseRequestOut": "_metastore_13_MoveTableToDatabaseRequestOut",
        "ListLocationsResponseIn": "_metastore_14_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_metastore_15_ListLocationsResponseOut",
        "RestoreIn": "_metastore_16_RestoreIn",
        "RestoreOut": "_metastore_17_RestoreOut",
        "NetworkConfigIn": "_metastore_18_NetworkConfigIn",
        "NetworkConfigOut": "_metastore_19_NetworkConfigOut",
        "ExprIn": "_metastore_20_ExprIn",
        "ExprOut": "_metastore_21_ExprOut",
        "MetadataImportIn": "_metastore_22_MetadataImportIn",
        "MetadataImportOut": "_metastore_23_MetadataImportOut",
        "MoveTableToDatabaseResponseIn": "_metastore_24_MoveTableToDatabaseResponseIn",
        "MoveTableToDatabaseResponseOut": "_metastore_25_MoveTableToDatabaseResponseOut",
        "ServiceIn": "_metastore_26_ServiceIn",
        "ServiceOut": "_metastore_27_ServiceOut",
        "BindingIn": "_metastore_28_BindingIn",
        "BindingOut": "_metastore_29_BindingOut",
        "EncryptionConfigIn": "_metastore_30_EncryptionConfigIn",
        "EncryptionConfigOut": "_metastore_31_EncryptionConfigOut",
        "BackendMetastoreIn": "_metastore_32_BackendMetastoreIn",
        "BackendMetastoreOut": "_metastore_33_BackendMetastoreOut",
        "LocationIn": "_metastore_34_LocationIn",
        "LocationOut": "_metastore_35_LocationOut",
        "KerberosConfigIn": "_metastore_36_KerberosConfigIn",
        "KerberosConfigOut": "_metastore_37_KerberosConfigOut",
        "OperationMetadataIn": "_metastore_38_OperationMetadataIn",
        "OperationMetadataOut": "_metastore_39_OperationMetadataOut",
        "FederationIn": "_metastore_40_FederationIn",
        "FederationOut": "_metastore_41_FederationOut",
        "TestIamPermissionsRequestIn": "_metastore_42_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_metastore_43_TestIamPermissionsRequestOut",
        "MetadataExportIn": "_metastore_44_MetadataExportIn",
        "MetadataExportOut": "_metastore_45_MetadataExportOut",
        "AuditConfigIn": "_metastore_46_AuditConfigIn",
        "AuditConfigOut": "_metastore_47_AuditConfigOut",
        "ListServicesResponseIn": "_metastore_48_ListServicesResponseIn",
        "ListServicesResponseOut": "_metastore_49_ListServicesResponseOut",
        "DatabaseDumpIn": "_metastore_50_DatabaseDumpIn",
        "DatabaseDumpOut": "_metastore_51_DatabaseDumpOut",
        "SecretIn": "_metastore_52_SecretIn",
        "SecretOut": "_metastore_53_SecretOut",
        "ListFederationsResponseIn": "_metastore_54_ListFederationsResponseIn",
        "ListFederationsResponseOut": "_metastore_55_ListFederationsResponseOut",
        "HiveMetastoreVersionIn": "_metastore_56_HiveMetastoreVersionIn",
        "HiveMetastoreVersionOut": "_metastore_57_HiveMetastoreVersionOut",
        "MaintenanceWindowIn": "_metastore_58_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_metastore_59_MaintenanceWindowOut",
        "AuxiliaryVersionConfigIn": "_metastore_60_AuxiliaryVersionConfigIn",
        "AuxiliaryVersionConfigOut": "_metastore_61_AuxiliaryVersionConfigOut",
        "PolicyIn": "_metastore_62_PolicyIn",
        "PolicyOut": "_metastore_63_PolicyOut",
        "AlterMetadataResourceLocationResponseIn": "_metastore_64_AlterMetadataResourceLocationResponseIn",
        "AlterMetadataResourceLocationResponseOut": "_metastore_65_AlterMetadataResourceLocationResponseOut",
        "TelemetryConfigIn": "_metastore_66_TelemetryConfigIn",
        "TelemetryConfigOut": "_metastore_67_TelemetryConfigOut",
        "HiveMetastoreConfigIn": "_metastore_68_HiveMetastoreConfigIn",
        "HiveMetastoreConfigOut": "_metastore_69_HiveMetastoreConfigOut",
        "SetIamPolicyRequestIn": "_metastore_70_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_metastore_71_SetIamPolicyRequestOut",
        "ListBackupsResponseIn": "_metastore_72_ListBackupsResponseIn",
        "ListBackupsResponseOut": "_metastore_73_ListBackupsResponseOut",
        "AuditLogConfigIn": "_metastore_74_AuditLogConfigIn",
        "AuditLogConfigOut": "_metastore_75_AuditLogConfigOut",
        "AlterMetadataResourceLocationRequestIn": "_metastore_76_AlterMetadataResourceLocationRequestIn",
        "AlterMetadataResourceLocationRequestOut": "_metastore_77_AlterMetadataResourceLocationRequestOut",
        "ExportMetadataRequestIn": "_metastore_78_ExportMetadataRequestIn",
        "ExportMetadataRequestOut": "_metastore_79_ExportMetadataRequestOut",
        "StatusIn": "_metastore_80_StatusIn",
        "StatusOut": "_metastore_81_StatusOut",
        "ConsumerIn": "_metastore_82_ConsumerIn",
        "ConsumerOut": "_metastore_83_ConsumerOut",
        "OperationIn": "_metastore_84_OperationIn",
        "OperationOut": "_metastore_85_OperationOut",
        "CancelOperationRequestIn": "_metastore_86_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_metastore_87_CancelOperationRequestOut",
        "ScalingConfigIn": "_metastore_88_ScalingConfigIn",
        "ScalingConfigOut": "_metastore_89_ScalingConfigOut",
        "QueryMetadataResponseIn": "_metastore_90_QueryMetadataResponseIn",
        "QueryMetadataResponseOut": "_metastore_91_QueryMetadataResponseOut",
        "BackupIn": "_metastore_92_BackupIn",
        "BackupOut": "_metastore_93_BackupOut",
        "RestoreServiceRequestIn": "_metastore_94_RestoreServiceRequestIn",
        "RestoreServiceRequestOut": "_metastore_95_RestoreServiceRequestOut",
        "ErrorDetailsIn": "_metastore_96_ErrorDetailsIn",
        "ErrorDetailsOut": "_metastore_97_ErrorDetailsOut",
        "QueryMetadataRequestIn": "_metastore_98_QueryMetadataRequestIn",
        "QueryMetadataRequestOut": "_metastore_99_QueryMetadataRequestOut",
        "ListMetadataImportsResponseIn": "_metastore_100_ListMetadataImportsResponseIn",
        "ListMetadataImportsResponseOut": "_metastore_101_ListMetadataImportsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["MoveTableToDatabaseRequestIn"] = t.struct(
        {"dbName": t.string(), "tableName": t.string(), "destinationDbName": t.string()}
    ).named(renames["MoveTableToDatabaseRequestIn"])
    types["MoveTableToDatabaseRequestOut"] = t.struct(
        {
            "dbName": t.string(),
            "tableName": t.string(),
            "destinationDbName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveTableToDatabaseRequestOut"])
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
    types["RestoreIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RestoreIn"]
    )
    types["RestoreOut"] = t.struct(
        {
            "details": t.string().optional(),
            "backup": t.string().optional(),
            "type": t.string().optional(),
            "state": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreOut"])
    types["NetworkConfigIn"] = t.struct(
        {"consumers": t.array(t.proxy(renames["ConsumerIn"])).optional()}
    ).named(renames["NetworkConfigIn"])
    types["NetworkConfigOut"] = t.struct(
        {
            "consumers": t.array(t.proxy(renames["ConsumerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConfigOut"])
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["MetadataImportIn"] = t.struct(
        {
            "name": t.string().optional(),
            "databaseDump": t.proxy(renames["DatabaseDumpIn"]).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["MetadataImportIn"])
    types["MetadataImportOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "databaseDump": t.proxy(renames["DatabaseDumpOut"]).optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataImportOut"])
    types["MoveTableToDatabaseResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["MoveTableToDatabaseResponseIn"])
    types["MoveTableToDatabaseResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MoveTableToDatabaseResponseOut"])
    types["ServiceIn"] = t.struct(
        {
            "hiveMetastoreConfig": t.proxy(renames["HiveMetastoreConfigIn"]).optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowIn"]).optional(),
            "name": t.string().optional(),
            "port": t.integer().optional(),
            "network": t.string().optional(),
            "tier": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
            "telemetryConfig": t.proxy(renames["TelemetryConfigIn"]).optional(),
            "releaseChannel": t.string().optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigIn"]).optional(),
            "scalingConfig": t.proxy(renames["ScalingConfigIn"]).optional(),
            "databaseType": t.string().optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "hiveMetastoreConfig": t.proxy(
                renames["HiveMetastoreConfigOut"]
            ).optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowOut"]).optional(),
            "stateMessage": t.string().optional(),
            "name": t.string().optional(),
            "endpointUri": t.string().optional(),
            "port": t.integer().optional(),
            "network": t.string().optional(),
            "state": t.string().optional(),
            "tier": t.string().optional(),
            "artifactGcsUri": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadataManagementActivity": t.proxy(
                renames["MetadataManagementActivityOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "networkConfig": t.proxy(renames["NetworkConfigOut"]).optional(),
            "createTime": t.string().optional(),
            "uid": t.string().optional(),
            "telemetryConfig": t.proxy(renames["TelemetryConfigOut"]).optional(),
            "releaseChannel": t.string().optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigOut"]).optional(),
            "scalingConfig": t.proxy(renames["ScalingConfigOut"]).optional(),
            "databaseType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
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
    types["EncryptionConfigIn"] = t.struct({"kmsKey": t.string().optional()}).named(
        renames["EncryptionConfigIn"]
    )
    types["EncryptionConfigOut"] = t.struct(
        {
            "kmsKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionConfigOut"])
    types["BackendMetastoreIn"] = t.struct(
        {"metastoreType": t.string().optional(), "name": t.string().optional()}
    ).named(renames["BackendMetastoreIn"])
    types["BackendMetastoreOut"] = t.struct(
        {
            "metastoreType": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendMetastoreOut"])
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["KerberosConfigIn"] = t.struct(
        {
            "principal": t.string().optional(),
            "krb5ConfigGcsUri": t.string().optional(),
            "keytab": t.proxy(renames["SecretIn"]).optional(),
        }
    ).named(renames["KerberosConfigIn"])
    types["KerberosConfigOut"] = t.struct(
        {
            "principal": t.string().optional(),
            "krb5ConfigGcsUri": t.string().optional(),
            "keytab": t.proxy(renames["SecretOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KerberosConfigOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "statusMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["FederationIn"] = t.struct(
        {
            "backendMetastores": t.struct({"_": t.string().optional()}).optional(),
            "version": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["FederationIn"])
    types["FederationOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "backendMetastores": t.struct({"_": t.string().optional()}).optional(),
            "version": t.string().optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "uid": t.string().optional(),
            "name": t.string().optional(),
            "endpointUri": t.string().optional(),
            "stateMessage": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FederationOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["MetadataExportIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MetadataExportIn"]
    )
    types["MetadataExportOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "databaseDumpType": t.string().optional(),
            "destinationGcsUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataExportOut"])
    types["AuditConfigIn"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])
    types["ListServicesResponseIn"] = t.struct(
        {
            "services": t.array(t.proxy(renames["ServiceIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListServicesResponseIn"])
    types["ListServicesResponseOut"] = t.struct(
        {
            "services": t.array(t.proxy(renames["ServiceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServicesResponseOut"])
    types["DatabaseDumpIn"] = t.struct(
        {
            "type": t.string().optional(),
            "gcsUri": t.string().optional(),
            "databaseType": t.string().optional(),
            "sourceDatabase": t.string().optional(),
        }
    ).named(renames["DatabaseDumpIn"])
    types["DatabaseDumpOut"] = t.struct(
        {
            "type": t.string().optional(),
            "gcsUri": t.string().optional(),
            "databaseType": t.string().optional(),
            "sourceDatabase": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseDumpOut"])
    types["SecretIn"] = t.struct({"cloudSecret": t.string().optional()}).named(
        renames["SecretIn"]
    )
    types["SecretOut"] = t.struct(
        {
            "cloudSecret": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretOut"])
    types["ListFederationsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "federations": t.array(t.proxy(renames["FederationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListFederationsResponseIn"])
    types["ListFederationsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "federations": t.array(t.proxy(renames["FederationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFederationsResponseOut"])
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
    types["MaintenanceWindowIn"] = t.struct(
        {"dayOfWeek": t.string().optional(), "hourOfDay": t.integer().optional()}
    ).named(renames["MaintenanceWindowIn"])
    types["MaintenanceWindowOut"] = t.struct(
        {
            "dayOfWeek": t.string().optional(),
            "hourOfDay": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceWindowOut"])
    types["AuxiliaryVersionConfigIn"] = t.struct(
        {
            "version": t.string().optional(),
            "configOverrides": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["AuxiliaryVersionConfigIn"])
    types["AuxiliaryVersionConfigOut"] = t.struct(
        {
            "networkConfig": t.proxy(renames["NetworkConfigOut"]).optional(),
            "version": t.string().optional(),
            "configOverrides": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuxiliaryVersionConfigOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["AlterMetadataResourceLocationResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AlterMetadataResourceLocationResponseIn"])
    types["AlterMetadataResourceLocationResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AlterMetadataResourceLocationResponseOut"])
    types["TelemetryConfigIn"] = t.struct({"logFormat": t.string().optional()}).named(
        renames["TelemetryConfigIn"]
    )
    types["TelemetryConfigOut"] = t.struct(
        {
            "logFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TelemetryConfigOut"])
    types["HiveMetastoreConfigIn"] = t.struct(
        {
            "kerberosConfig": t.proxy(renames["KerberosConfigIn"]).optional(),
            "endpointProtocol": t.string().optional(),
            "configOverrides": t.struct({"_": t.string().optional()}).optional(),
            "auxiliaryVersions": t.struct({"_": t.string().optional()}).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["HiveMetastoreConfigIn"])
    types["HiveMetastoreConfigOut"] = t.struct(
        {
            "kerberosConfig": t.proxy(renames["KerberosConfigOut"]).optional(),
            "endpointProtocol": t.string().optional(),
            "configOverrides": t.struct({"_": t.string().optional()}).optional(),
            "auxiliaryVersions": t.struct({"_": t.string().optional()}).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HiveMetastoreConfigOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyIn"]).optional(),
            "updateMask": t.string().optional(),
        }
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
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
    types["AuditLogConfigIn"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
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
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["ScalingConfigIn"] = t.struct(
        {"instanceSize": t.string().optional(), "scalingFactor": t.number().optional()}
    ).named(renames["ScalingConfigIn"])
    types["ScalingConfigOut"] = t.struct(
        {
            "instanceSize": t.string().optional(),
            "scalingFactor": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScalingConfigOut"])
    types["QueryMetadataResponseIn"] = t.struct(
        {"resultManifestUri": t.string().optional()}
    ).named(renames["QueryMetadataResponseIn"])
    types["QueryMetadataResponseOut"] = t.struct(
        {
            "resultManifestUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryMetadataResponseOut"])
    types["BackupIn"] = t.struct(
        {"description": t.string().optional(), "name": t.string().optional()}
    ).named(renames["BackupIn"])
    types["BackupOut"] = t.struct(
        {
            "description": t.string().optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "restoringServices": t.array(t.string()).optional(),
            "serviceRevision": t.proxy(renames["ServiceOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupOut"])
    types["RestoreServiceRequestIn"] = t.struct(
        {
            "backup": t.string(),
            "restoreType": t.string().optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["RestoreServiceRequestIn"])
    types["RestoreServiceRequestOut"] = t.struct(
        {
            "backup": t.string(),
            "restoreType": t.string().optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreServiceRequestOut"])
    types["ErrorDetailsIn"] = t.struct(
        {"details": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["ErrorDetailsIn"])
    types["ErrorDetailsOut"] = t.struct(
        {
            "details": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorDetailsOut"])
    types["QueryMetadataRequestIn"] = t.struct({"query": t.string()}).named(
        renames["QueryMetadataRequestIn"]
    )
    types["QueryMetadataRequestOut"] = t.struct(
        {"query": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["QueryMetadataRequestOut"])
    types["ListMetadataImportsResponseIn"] = t.struct(
        {
            "metadataImports": t.array(t.proxy(renames["MetadataImportIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListMetadataImportsResponseIn"])
    types["ListMetadataImportsResponseOut"] = t.struct(
        {
            "metadataImports": t.array(
                t.proxy(renames["MetadataImportOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMetadataImportsResponseOut"])

    functions = {}
    functions["projectsLocationsGet"] = metastore.get(
        "v1/{name}/locations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = metastore.get(
        "v1/{name}/locations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesGetIamPolicy"] = metastore.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesList"] = metastore.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesMoveTableToDatabase"] = metastore.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesQueryMetadata"] = metastore.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesPatch"] = metastore.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesDelete"] = metastore.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesAlterLocation"] = metastore.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesExportMetadata"] = metastore.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesRestore"] = metastore.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesCreate"] = metastore.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesTestIamPermissions"] = metastore.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesGet"] = metastore.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesSetIamPolicy"] = metastore.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesBackupsGetIamPolicy"] = metastore.get(
        "v1/{parent}/backups",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBackupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesBackupsCreate"] = metastore.get(
        "v1/{parent}/backups",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBackupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesBackupsDelete"] = metastore.get(
        "v1/{parent}/backups",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBackupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesBackupsGet"] = metastore.get(
        "v1/{parent}/backups",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBackupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesBackupsSetIamPolicy"] = metastore.get(
        "v1/{parent}/backups",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBackupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesBackupsList"] = metastore.get(
        "v1/{parent}/backups",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBackupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesMetadataImportsPatch"] = metastore.get(
        "v1/{parent}/metadataImports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMetadataImportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesMetadataImportsCreate"] = metastore.get(
        "v1/{parent}/metadataImports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMetadataImportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesMetadataImportsGet"] = metastore.get(
        "v1/{parent}/metadataImports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMetadataImportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesMetadataImportsList"] = metastore.get(
        "v1/{parent}/metadataImports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMetadataImportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsTestIamPermissions"] = metastore.get(
        "v1/{parent}/federations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFederationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsCreate"] = metastore.get(
        "v1/{parent}/federations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFederationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsDelete"] = metastore.get(
        "v1/{parent}/federations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFederationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsGetIamPolicy"] = metastore.get(
        "v1/{parent}/federations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFederationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsGet"] = metastore.get(
        "v1/{parent}/federations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFederationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsSetIamPolicy"] = metastore.get(
        "v1/{parent}/federations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFederationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsPatch"] = metastore.get(
        "v1/{parent}/federations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFederationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsList"] = metastore.get(
        "v1/{parent}/federations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFederationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = metastore.post(
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
    functions["projectsLocationsOperationsList"] = metastore.post(
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
    functions["projectsLocationsOperationsDelete"] = metastore.post(
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
    functions["projectsLocationsOperationsCancel"] = metastore.post(
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
        importer="metastore",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
