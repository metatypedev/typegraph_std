from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_metastore() -> Import:
    metastore = HTTPRuntime("https://metastore.googleapis.com/")

    renames = {
        "ErrorResponse": "_metastore_1_ErrorResponse",
        "ListLocationsResponseIn": "_metastore_2_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_metastore_3_ListLocationsResponseOut",
        "PolicyIn": "_metastore_4_PolicyIn",
        "PolicyOut": "_metastore_5_PolicyOut",
        "MetadataImportIn": "_metastore_6_MetadataImportIn",
        "MetadataImportOut": "_metastore_7_MetadataImportOut",
        "ListFederationsResponseIn": "_metastore_8_ListFederationsResponseIn",
        "ListFederationsResponseOut": "_metastore_9_ListFederationsResponseOut",
        "QueryMetadataRequestIn": "_metastore_10_QueryMetadataRequestIn",
        "QueryMetadataRequestOut": "_metastore_11_QueryMetadataRequestOut",
        "EncryptionConfigIn": "_metastore_12_EncryptionConfigIn",
        "EncryptionConfigOut": "_metastore_13_EncryptionConfigOut",
        "ConsumerIn": "_metastore_14_ConsumerIn",
        "ConsumerOut": "_metastore_15_ConsumerOut",
        "CancelOperationRequestIn": "_metastore_16_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_metastore_17_CancelOperationRequestOut",
        "ExportMetadataRequestIn": "_metastore_18_ExportMetadataRequestIn",
        "ExportMetadataRequestOut": "_metastore_19_ExportMetadataRequestOut",
        "BackupIn": "_metastore_20_BackupIn",
        "BackupOut": "_metastore_21_BackupOut",
        "ExprIn": "_metastore_22_ExprIn",
        "ExprOut": "_metastore_23_ExprOut",
        "DatabaseDumpIn": "_metastore_24_DatabaseDumpIn",
        "DatabaseDumpOut": "_metastore_25_DatabaseDumpOut",
        "StatusIn": "_metastore_26_StatusIn",
        "StatusOut": "_metastore_27_StatusOut",
        "AuditLogConfigIn": "_metastore_28_AuditLogConfigIn",
        "AuditLogConfigOut": "_metastore_29_AuditLogConfigOut",
        "ListMetadataImportsResponseIn": "_metastore_30_ListMetadataImportsResponseIn",
        "ListMetadataImportsResponseOut": "_metastore_31_ListMetadataImportsResponseOut",
        "MetadataManagementActivityIn": "_metastore_32_MetadataManagementActivityIn",
        "MetadataManagementActivityOut": "_metastore_33_MetadataManagementActivityOut",
        "RestoreIn": "_metastore_34_RestoreIn",
        "RestoreOut": "_metastore_35_RestoreOut",
        "MoveTableToDatabaseRequestIn": "_metastore_36_MoveTableToDatabaseRequestIn",
        "MoveTableToDatabaseRequestOut": "_metastore_37_MoveTableToDatabaseRequestOut",
        "BindingIn": "_metastore_38_BindingIn",
        "BindingOut": "_metastore_39_BindingOut",
        "ListBackupsResponseIn": "_metastore_40_ListBackupsResponseIn",
        "ListBackupsResponseOut": "_metastore_41_ListBackupsResponseOut",
        "AlterMetadataResourceLocationResponseIn": "_metastore_42_AlterMetadataResourceLocationResponseIn",
        "AlterMetadataResourceLocationResponseOut": "_metastore_43_AlterMetadataResourceLocationResponseOut",
        "AuxiliaryVersionConfigIn": "_metastore_44_AuxiliaryVersionConfigIn",
        "AuxiliaryVersionConfigOut": "_metastore_45_AuxiliaryVersionConfigOut",
        "TestIamPermissionsResponseIn": "_metastore_46_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_metastore_47_TestIamPermissionsResponseOut",
        "HiveMetastoreVersionIn": "_metastore_48_HiveMetastoreVersionIn",
        "HiveMetastoreVersionOut": "_metastore_49_HiveMetastoreVersionOut",
        "FederationIn": "_metastore_50_FederationIn",
        "FederationOut": "_metastore_51_FederationOut",
        "AuditConfigIn": "_metastore_52_AuditConfigIn",
        "AuditConfigOut": "_metastore_53_AuditConfigOut",
        "BackendMetastoreIn": "_metastore_54_BackendMetastoreIn",
        "BackendMetastoreOut": "_metastore_55_BackendMetastoreOut",
        "RestoreServiceRequestIn": "_metastore_56_RestoreServiceRequestIn",
        "RestoreServiceRequestOut": "_metastore_57_RestoreServiceRequestOut",
        "MaintenanceWindowIn": "_metastore_58_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_metastore_59_MaintenanceWindowOut",
        "EmptyIn": "_metastore_60_EmptyIn",
        "EmptyOut": "_metastore_61_EmptyOut",
        "MoveTableToDatabaseResponseIn": "_metastore_62_MoveTableToDatabaseResponseIn",
        "MoveTableToDatabaseResponseOut": "_metastore_63_MoveTableToDatabaseResponseOut",
        "ServiceIn": "_metastore_64_ServiceIn",
        "ServiceOut": "_metastore_65_ServiceOut",
        "SecretIn": "_metastore_66_SecretIn",
        "SecretOut": "_metastore_67_SecretOut",
        "NetworkConfigIn": "_metastore_68_NetworkConfigIn",
        "NetworkConfigOut": "_metastore_69_NetworkConfigOut",
        "KerberosConfigIn": "_metastore_70_KerberosConfigIn",
        "KerberosConfigOut": "_metastore_71_KerberosConfigOut",
        "LocationMetadataIn": "_metastore_72_LocationMetadataIn",
        "LocationMetadataOut": "_metastore_73_LocationMetadataOut",
        "OperationIn": "_metastore_74_OperationIn",
        "OperationOut": "_metastore_75_OperationOut",
        "MetadataExportIn": "_metastore_76_MetadataExportIn",
        "MetadataExportOut": "_metastore_77_MetadataExportOut",
        "LocationIn": "_metastore_78_LocationIn",
        "LocationOut": "_metastore_79_LocationOut",
        "QueryMetadataResponseIn": "_metastore_80_QueryMetadataResponseIn",
        "QueryMetadataResponseOut": "_metastore_81_QueryMetadataResponseOut",
        "ScalingConfigIn": "_metastore_82_ScalingConfigIn",
        "ScalingConfigOut": "_metastore_83_ScalingConfigOut",
        "SetIamPolicyRequestIn": "_metastore_84_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_metastore_85_SetIamPolicyRequestOut",
        "ListServicesResponseIn": "_metastore_86_ListServicesResponseIn",
        "ListServicesResponseOut": "_metastore_87_ListServicesResponseOut",
        "HiveMetastoreConfigIn": "_metastore_88_HiveMetastoreConfigIn",
        "HiveMetastoreConfigOut": "_metastore_89_HiveMetastoreConfigOut",
        "TestIamPermissionsRequestIn": "_metastore_90_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_metastore_91_TestIamPermissionsRequestOut",
        "AlterMetadataResourceLocationRequestIn": "_metastore_92_AlterMetadataResourceLocationRequestIn",
        "AlterMetadataResourceLocationRequestOut": "_metastore_93_AlterMetadataResourceLocationRequestOut",
        "TelemetryConfigIn": "_metastore_94_TelemetryConfigIn",
        "TelemetryConfigOut": "_metastore_95_TelemetryConfigOut",
        "OperationMetadataIn": "_metastore_96_OperationMetadataIn",
        "OperationMetadataOut": "_metastore_97_OperationMetadataOut",
        "ListOperationsResponseIn": "_metastore_98_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_metastore_99_ListOperationsResponseOut",
        "ErrorDetailsIn": "_metastore_100_ErrorDetailsIn",
        "ErrorDetailsOut": "_metastore_101_ErrorDetailsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["MetadataImportIn"] = t.struct(
        {
            "description": t.string().optional(),
            "databaseDump": t.proxy(renames["DatabaseDumpIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["MetadataImportIn"])
    types["MetadataImportOut"] = t.struct(
        {
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "databaseDump": t.proxy(renames["DatabaseDumpOut"]).optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataImportOut"])
    types["ListFederationsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "federations": t.array(t.proxy(renames["FederationIn"])).optional(),
        }
    ).named(renames["ListFederationsResponseIn"])
    types["ListFederationsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "federations": t.array(t.proxy(renames["FederationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFederationsResponseOut"])
    types["QueryMetadataRequestIn"] = t.struct({"query": t.string()}).named(
        renames["QueryMetadataRequestIn"]
    )
    types["QueryMetadataRequestOut"] = t.struct(
        {"query": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["QueryMetadataRequestOut"])
    types["EncryptionConfigIn"] = t.struct({"kmsKey": t.string().optional()}).named(
        renames["EncryptionConfigIn"]
    )
    types["EncryptionConfigOut"] = t.struct(
        {
            "kmsKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionConfigOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["ExportMetadataRequestIn"] = t.struct(
        {
            "requestId": t.string().optional(),
            "databaseDumpType": t.string().optional(),
            "destinationGcsFolder": t.string().optional(),
        }
    ).named(renames["ExportMetadataRequestIn"])
    types["ExportMetadataRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "databaseDumpType": t.string().optional(),
            "destinationGcsFolder": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportMetadataRequestOut"])
    types["BackupIn"] = t.struct(
        {"name": t.string().optional(), "description": t.string().optional()}
    ).named(renames["BackupIn"])
    types["BackupOut"] = t.struct(
        {
            "serviceRevision": t.proxy(renames["ServiceOut"]).optional(),
            "endTime": t.string().optional(),
            "restoringServices": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["DatabaseDumpIn"] = t.struct(
        {
            "sourceDatabase": t.string().optional(),
            "gcsUri": t.string().optional(),
            "databaseType": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["DatabaseDumpIn"])
    types["DatabaseDumpOut"] = t.struct(
        {
            "sourceDatabase": t.string().optional(),
            "gcsUri": t.string().optional(),
            "databaseType": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseDumpOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["RestoreIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RestoreIn"]
    )
    types["RestoreOut"] = t.struct(
        {
            "backup": t.string().optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "type": t.string().optional(),
            "startTime": t.string().optional(),
            "details": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreOut"])
    types["MoveTableToDatabaseRequestIn"] = t.struct(
        {"destinationDbName": t.string(), "tableName": t.string(), "dbName": t.string()}
    ).named(renames["MoveTableToDatabaseRequestIn"])
    types["MoveTableToDatabaseRequestOut"] = t.struct(
        {
            "destinationDbName": t.string(),
            "tableName": t.string(),
            "dbName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveTableToDatabaseRequestOut"])
    types["BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
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
    types["AlterMetadataResourceLocationResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AlterMetadataResourceLocationResponseIn"])
    types["AlterMetadataResourceLocationResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AlterMetadataResourceLocationResponseOut"])
    types["AuxiliaryVersionConfigIn"] = t.struct(
        {
            "version": t.string().optional(),
            "configOverrides": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["AuxiliaryVersionConfigIn"])
    types["AuxiliaryVersionConfigOut"] = t.struct(
        {
            "version": t.string().optional(),
            "networkConfig": t.proxy(renames["NetworkConfigOut"]).optional(),
            "configOverrides": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuxiliaryVersionConfigOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
            "backendMetastores": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "stateMessage": t.string().optional(),
            "state": t.string().optional(),
            "endpointUri": t.string().optional(),
            "version": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "uid": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FederationOut"])
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
    types["RestoreServiceRequestIn"] = t.struct(
        {
            "requestId": t.string().optional(),
            "restoreType": t.string().optional(),
            "backup": t.string(),
        }
    ).named(renames["RestoreServiceRequestIn"])
    types["RestoreServiceRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "restoreType": t.string().optional(),
            "backup": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreServiceRequestOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["MoveTableToDatabaseResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["MoveTableToDatabaseResponseIn"])
    types["MoveTableToDatabaseResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MoveTableToDatabaseResponseOut"])
    types["ServiceIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "databaseType": t.string().optional(),
            "network": t.string().optional(),
            "hiveMetastoreConfig": t.proxy(renames["HiveMetastoreConfigIn"]).optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigIn"]).optional(),
            "releaseChannel": t.string().optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowIn"]).optional(),
            "name": t.string().optional(),
            "tier": t.string().optional(),
            "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
            "scalingConfig": t.proxy(renames["ScalingConfigIn"]).optional(),
            "port": t.integer().optional(),
            "telemetryConfig": t.proxy(renames["TelemetryConfigIn"]).optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "stateMessage": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadataManagementActivity": t.proxy(
                renames["MetadataManagementActivityOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "databaseType": t.string().optional(),
            "network": t.string().optional(),
            "createTime": t.string().optional(),
            "hiveMetastoreConfig": t.proxy(
                renames["HiveMetastoreConfigOut"]
            ).optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigOut"]).optional(),
            "releaseChannel": t.string().optional(),
            "uid": t.string().optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowOut"]).optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "tier": t.string().optional(),
            "networkConfig": t.proxy(renames["NetworkConfigOut"]).optional(),
            "scalingConfig": t.proxy(renames["ScalingConfigOut"]).optional(),
            "port": t.integer().optional(),
            "artifactGcsUri": t.string().optional(),
            "telemetryConfig": t.proxy(renames["TelemetryConfigOut"]).optional(),
            "endpointUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
    types["SecretIn"] = t.struct({"cloudSecret": t.string().optional()}).named(
        renames["SecretIn"]
    )
    types["SecretOut"] = t.struct(
        {
            "cloudSecret": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretOut"])
    types["NetworkConfigIn"] = t.struct(
        {"consumers": t.array(t.proxy(renames["ConsumerIn"])).optional()}
    ).named(renames["NetworkConfigIn"])
    types["NetworkConfigOut"] = t.struct(
        {
            "consumers": t.array(t.proxy(renames["ConsumerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConfigOut"])
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
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["MetadataExportIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MetadataExportIn"]
    )
    types["MetadataExportOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "databaseDumpType": t.string().optional(),
            "state": t.string().optional(),
            "startTime": t.string().optional(),
            "destinationGcsUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataExportOut"])
    types["LocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["QueryMetadataResponseIn"] = t.struct(
        {"resultManifestUri": t.string().optional()}
    ).named(renames["QueryMetadataResponseIn"])
    types["QueryMetadataResponseOut"] = t.struct(
        {
            "resultManifestUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryMetadataResponseOut"])
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
    types["ListServicesResponseIn"] = t.struct(
        {
            "services": t.array(t.proxy(renames["ServiceIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListServicesResponseIn"])
    types["ListServicesResponseOut"] = t.struct(
        {
            "services": t.array(t.proxy(renames["ServiceOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServicesResponseOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["AlterMetadataResourceLocationRequestIn"] = t.struct(
        {"resourceName": t.string(), "locationUri": t.string()}
    ).named(renames["AlterMetadataResourceLocationRequestIn"])
    types["AlterMetadataResourceLocationRequestOut"] = t.struct(
        {
            "resourceName": t.string(),
            "locationUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlterMetadataResourceLocationRequestOut"])
    types["TelemetryConfigIn"] = t.struct({"logFormat": t.string().optional()}).named(
        renames["TelemetryConfigIn"]
    )
    types["TelemetryConfigOut"] = t.struct(
        {
            "logFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TelemetryConfigOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["ErrorDetailsIn"] = t.struct(
        {"details": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["ErrorDetailsIn"])
    types["ErrorDetailsOut"] = t.struct(
        {
            "details": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorDetailsOut"])

    functions = {}
    functions["projectsLocationsGet"] = metastore.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesPatch"] = metastore.post(
        "v1/{service}:exportMetadata",
        t.struct(
            {
                "service": t.string(),
                "requestId": t.string().optional(),
                "databaseDumpType": t.string().optional(),
                "destinationGcsFolder": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesMoveTableToDatabase"] = metastore.post(
        "v1/{service}:exportMetadata",
        t.struct(
            {
                "service": t.string(),
                "requestId": t.string().optional(),
                "databaseDumpType": t.string().optional(),
                "destinationGcsFolder": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesQueryMetadata"] = metastore.post(
        "v1/{service}:exportMetadata",
        t.struct(
            {
                "service": t.string(),
                "requestId": t.string().optional(),
                "databaseDumpType": t.string().optional(),
                "destinationGcsFolder": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesGetIamPolicy"] = metastore.post(
        "v1/{service}:exportMetadata",
        t.struct(
            {
                "service": t.string(),
                "requestId": t.string().optional(),
                "databaseDumpType": t.string().optional(),
                "destinationGcsFolder": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesAlterLocation"] = metastore.post(
        "v1/{service}:exportMetadata",
        t.struct(
            {
                "service": t.string(),
                "requestId": t.string().optional(),
                "databaseDumpType": t.string().optional(),
                "destinationGcsFolder": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesCreate"] = metastore.post(
        "v1/{service}:exportMetadata",
        t.struct(
            {
                "service": t.string(),
                "requestId": t.string().optional(),
                "databaseDumpType": t.string().optional(),
                "destinationGcsFolder": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesList"] = metastore.post(
        "v1/{service}:exportMetadata",
        t.struct(
            {
                "service": t.string(),
                "requestId": t.string().optional(),
                "databaseDumpType": t.string().optional(),
                "destinationGcsFolder": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesSetIamPolicy"] = metastore.post(
        "v1/{service}:exportMetadata",
        t.struct(
            {
                "service": t.string(),
                "requestId": t.string().optional(),
                "databaseDumpType": t.string().optional(),
                "destinationGcsFolder": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesRestore"] = metastore.post(
        "v1/{service}:exportMetadata",
        t.struct(
            {
                "service": t.string(),
                "requestId": t.string().optional(),
                "databaseDumpType": t.string().optional(),
                "destinationGcsFolder": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesGet"] = metastore.post(
        "v1/{service}:exportMetadata",
        t.struct(
            {
                "service": t.string(),
                "requestId": t.string().optional(),
                "databaseDumpType": t.string().optional(),
                "destinationGcsFolder": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesDelete"] = metastore.post(
        "v1/{service}:exportMetadata",
        t.struct(
            {
                "service": t.string(),
                "requestId": t.string().optional(),
                "databaseDumpType": t.string().optional(),
                "destinationGcsFolder": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesTestIamPermissions"] = metastore.post(
        "v1/{service}:exportMetadata",
        t.struct(
            {
                "service": t.string(),
                "requestId": t.string().optional(),
                "databaseDumpType": t.string().optional(),
                "destinationGcsFolder": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesExportMetadata"] = metastore.post(
        "v1/{service}:exportMetadata",
        t.struct(
            {
                "service": t.string(),
                "requestId": t.string().optional(),
                "databaseDumpType": t.string().optional(),
                "destinationGcsFolder": t.string().optional(),
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
                "name": t.string(),
                "requestId": t.string().optional(),
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
                "name": t.string(),
                "requestId": t.string().optional(),
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
                "name": t.string(),
                "requestId": t.string().optional(),
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
                "name": t.string(),
                "requestId": t.string().optional(),
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
                "name": t.string(),
                "requestId": t.string().optional(),
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
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesMetadataImportsCreate"] = metastore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MetadataImportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesMetadataImportsList"] = metastore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MetadataImportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesMetadataImportsPatch"] = metastore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MetadataImportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesMetadataImportsGet"] = metastore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MetadataImportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsDelete"] = metastore.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsList"] = metastore.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsPatch"] = metastore.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsTestIamPermissions"] = metastore.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsGet"] = metastore.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsSetIamPolicy"] = metastore.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsCreate"] = metastore.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsGetIamPolicy"] = metastore.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = metastore.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="metastore", renames=renames, types=types, functions=functions
    )
