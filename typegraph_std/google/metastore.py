from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_metastore() -> Import:
    metastore = HTTPRuntime("https://metastore.googleapis.com/")

    renames = {
        "ErrorResponse": "_metastore_1_ErrorResponse",
        "CancelOperationRequestIn": "_metastore_2_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_metastore_3_CancelOperationRequestOut",
        "NetworkConfigIn": "_metastore_4_NetworkConfigIn",
        "NetworkConfigOut": "_metastore_5_NetworkConfigOut",
        "ErrorDetailsIn": "_metastore_6_ErrorDetailsIn",
        "ErrorDetailsOut": "_metastore_7_ErrorDetailsOut",
        "ListMetadataImportsResponseIn": "_metastore_8_ListMetadataImportsResponseIn",
        "ListMetadataImportsResponseOut": "_metastore_9_ListMetadataImportsResponseOut",
        "HiveMetastoreConfigIn": "_metastore_10_HiveMetastoreConfigIn",
        "HiveMetastoreConfigOut": "_metastore_11_HiveMetastoreConfigOut",
        "ScalingConfigIn": "_metastore_12_ScalingConfigIn",
        "ScalingConfigOut": "_metastore_13_ScalingConfigOut",
        "StatusIn": "_metastore_14_StatusIn",
        "StatusOut": "_metastore_15_StatusOut",
        "SetIamPolicyRequestIn": "_metastore_16_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_metastore_17_SetIamPolicyRequestOut",
        "ListFederationsResponseIn": "_metastore_18_ListFederationsResponseIn",
        "ListFederationsResponseOut": "_metastore_19_ListFederationsResponseOut",
        "TestIamPermissionsRequestIn": "_metastore_20_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_metastore_21_TestIamPermissionsRequestOut",
        "MoveTableToDatabaseResponseIn": "_metastore_22_MoveTableToDatabaseResponseIn",
        "MoveTableToDatabaseResponseOut": "_metastore_23_MoveTableToDatabaseResponseOut",
        "AuditLogConfigIn": "_metastore_24_AuditLogConfigIn",
        "AuditLogConfigOut": "_metastore_25_AuditLogConfigOut",
        "AuditConfigIn": "_metastore_26_AuditConfigIn",
        "AuditConfigOut": "_metastore_27_AuditConfigOut",
        "ListOperationsResponseIn": "_metastore_28_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_metastore_29_ListOperationsResponseOut",
        "ExportMetadataRequestIn": "_metastore_30_ExportMetadataRequestIn",
        "ExportMetadataRequestOut": "_metastore_31_ExportMetadataRequestOut",
        "KerberosConfigIn": "_metastore_32_KerberosConfigIn",
        "KerberosConfigOut": "_metastore_33_KerberosConfigOut",
        "MaintenanceWindowIn": "_metastore_34_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_metastore_35_MaintenanceWindowOut",
        "OperationMetadataIn": "_metastore_36_OperationMetadataIn",
        "OperationMetadataOut": "_metastore_37_OperationMetadataOut",
        "AuxiliaryVersionConfigIn": "_metastore_38_AuxiliaryVersionConfigIn",
        "AuxiliaryVersionConfigOut": "_metastore_39_AuxiliaryVersionConfigOut",
        "ListServicesResponseIn": "_metastore_40_ListServicesResponseIn",
        "ListServicesResponseOut": "_metastore_41_ListServicesResponseOut",
        "QueryMetadataResponseIn": "_metastore_42_QueryMetadataResponseIn",
        "QueryMetadataResponseOut": "_metastore_43_QueryMetadataResponseOut",
        "EncryptionConfigIn": "_metastore_44_EncryptionConfigIn",
        "EncryptionConfigOut": "_metastore_45_EncryptionConfigOut",
        "OperationIn": "_metastore_46_OperationIn",
        "OperationOut": "_metastore_47_OperationOut",
        "RestoreIn": "_metastore_48_RestoreIn",
        "RestoreOut": "_metastore_49_RestoreOut",
        "PolicyIn": "_metastore_50_PolicyIn",
        "PolicyOut": "_metastore_51_PolicyOut",
        "AlterMetadataResourceLocationRequestIn": "_metastore_52_AlterMetadataResourceLocationRequestIn",
        "AlterMetadataResourceLocationRequestOut": "_metastore_53_AlterMetadataResourceLocationRequestOut",
        "SecretIn": "_metastore_54_SecretIn",
        "SecretOut": "_metastore_55_SecretOut",
        "ConsumerIn": "_metastore_56_ConsumerIn",
        "ConsumerOut": "_metastore_57_ConsumerOut",
        "BackupIn": "_metastore_58_BackupIn",
        "BackupOut": "_metastore_59_BackupOut",
        "BackendMetastoreIn": "_metastore_60_BackendMetastoreIn",
        "BackendMetastoreOut": "_metastore_61_BackendMetastoreOut",
        "MoveTableToDatabaseRequestIn": "_metastore_62_MoveTableToDatabaseRequestIn",
        "MoveTableToDatabaseRequestOut": "_metastore_63_MoveTableToDatabaseRequestOut",
        "LocationMetadataIn": "_metastore_64_LocationMetadataIn",
        "LocationMetadataOut": "_metastore_65_LocationMetadataOut",
        "ListLocationsResponseIn": "_metastore_66_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_metastore_67_ListLocationsResponseOut",
        "AlterMetadataResourceLocationResponseIn": "_metastore_68_AlterMetadataResourceLocationResponseIn",
        "AlterMetadataResourceLocationResponseOut": "_metastore_69_AlterMetadataResourceLocationResponseOut",
        "ListBackupsResponseIn": "_metastore_70_ListBackupsResponseIn",
        "ListBackupsResponseOut": "_metastore_71_ListBackupsResponseOut",
        "LocationIn": "_metastore_72_LocationIn",
        "LocationOut": "_metastore_73_LocationOut",
        "QueryMetadataRequestIn": "_metastore_74_QueryMetadataRequestIn",
        "QueryMetadataRequestOut": "_metastore_75_QueryMetadataRequestOut",
        "BindingIn": "_metastore_76_BindingIn",
        "BindingOut": "_metastore_77_BindingOut",
        "DatabaseDumpIn": "_metastore_78_DatabaseDumpIn",
        "DatabaseDumpOut": "_metastore_79_DatabaseDumpOut",
        "MetadataExportIn": "_metastore_80_MetadataExportIn",
        "MetadataExportOut": "_metastore_81_MetadataExportOut",
        "EmptyIn": "_metastore_82_EmptyIn",
        "EmptyOut": "_metastore_83_EmptyOut",
        "HiveMetastoreVersionIn": "_metastore_84_HiveMetastoreVersionIn",
        "HiveMetastoreVersionOut": "_metastore_85_HiveMetastoreVersionOut",
        "ServiceIn": "_metastore_86_ServiceIn",
        "ServiceOut": "_metastore_87_ServiceOut",
        "TelemetryConfigIn": "_metastore_88_TelemetryConfigIn",
        "TelemetryConfigOut": "_metastore_89_TelemetryConfigOut",
        "MetadataManagementActivityIn": "_metastore_90_MetadataManagementActivityIn",
        "MetadataManagementActivityOut": "_metastore_91_MetadataManagementActivityOut",
        "FederationIn": "_metastore_92_FederationIn",
        "FederationOut": "_metastore_93_FederationOut",
        "TestIamPermissionsResponseIn": "_metastore_94_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_metastore_95_TestIamPermissionsResponseOut",
        "ExprIn": "_metastore_96_ExprIn",
        "ExprOut": "_metastore_97_ExprOut",
        "RestoreServiceRequestIn": "_metastore_98_RestoreServiceRequestIn",
        "RestoreServiceRequestOut": "_metastore_99_RestoreServiceRequestOut",
        "MetadataImportIn": "_metastore_100_MetadataImportIn",
        "MetadataImportOut": "_metastore_101_MetadataImportOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["NetworkConfigIn"] = t.struct(
        {"consumers": t.array(t.proxy(renames["ConsumerIn"])).optional()}
    ).named(renames["NetworkConfigIn"])
    types["NetworkConfigOut"] = t.struct(
        {
            "consumers": t.array(t.proxy(renames["ConsumerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConfigOut"])
    types["ErrorDetailsIn"] = t.struct(
        {"details": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["ErrorDetailsIn"])
    types["ErrorDetailsOut"] = t.struct(
        {
            "details": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorDetailsOut"])
    types["ListMetadataImportsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "metadataImports": t.array(t.proxy(renames["MetadataImportIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListMetadataImportsResponseIn"])
    types["ListMetadataImportsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "metadataImports": t.array(
                t.proxy(renames["MetadataImportOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMetadataImportsResponseOut"])
    types["HiveMetastoreConfigIn"] = t.struct(
        {
            "version": t.string().optional(),
            "configOverrides": t.struct({"_": t.string().optional()}).optional(),
            "kerberosConfig": t.proxy(renames["KerberosConfigIn"]).optional(),
            "auxiliaryVersions": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["HiveMetastoreConfigIn"])
    types["HiveMetastoreConfigOut"] = t.struct(
        {
            "version": t.string().optional(),
            "configOverrides": t.struct({"_": t.string().optional()}).optional(),
            "kerberosConfig": t.proxy(renames["KerberosConfigOut"]).optional(),
            "auxiliaryVersions": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HiveMetastoreConfigOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["MoveTableToDatabaseResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["MoveTableToDatabaseResponseIn"])
    types["MoveTableToDatabaseResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MoveTableToDatabaseResponseOut"])
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
    types["ExportMetadataRequestIn"] = t.struct(
        {
            "destinationGcsFolder": t.string().optional(),
            "requestId": t.string().optional(),
            "databaseDumpType": t.string().optional(),
        }
    ).named(renames["ExportMetadataRequestIn"])
    types["ExportMetadataRequestOut"] = t.struct(
        {
            "destinationGcsFolder": t.string().optional(),
            "requestId": t.string().optional(),
            "databaseDumpType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportMetadataRequestOut"])
    types["KerberosConfigIn"] = t.struct(
        {
            "keytab": t.proxy(renames["SecretIn"]).optional(),
            "krb5ConfigGcsUri": t.string().optional(),
            "principal": t.string().optional(),
        }
    ).named(renames["KerberosConfigIn"])
    types["KerberosConfigOut"] = t.struct(
        {
            "keytab": t.proxy(renames["SecretOut"]).optional(),
            "krb5ConfigGcsUri": t.string().optional(),
            "principal": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KerberosConfigOut"])
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
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "requestedCancellation": t.boolean().optional(),
            "statusMessage": t.string().optional(),
            "apiVersion": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["AuxiliaryVersionConfigIn"] = t.struct(
        {
            "configOverrides": t.struct({"_": t.string().optional()}).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["AuxiliaryVersionConfigIn"])
    types["AuxiliaryVersionConfigOut"] = t.struct(
        {
            "configOverrides": t.struct({"_": t.string().optional()}).optional(),
            "version": t.string().optional(),
            "networkConfig": t.proxy(renames["NetworkConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuxiliaryVersionConfigOut"])
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
    types["QueryMetadataResponseIn"] = t.struct(
        {"resultManifestUri": t.string().optional()}
    ).named(renames["QueryMetadataResponseIn"])
    types["QueryMetadataResponseOut"] = t.struct(
        {
            "resultManifestUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryMetadataResponseOut"])
    types["EncryptionConfigIn"] = t.struct({"kmsKey": t.string().optional()}).named(
        renames["EncryptionConfigIn"]
    )
    types["EncryptionConfigOut"] = t.struct(
        {
            "kmsKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionConfigOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["RestoreIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RestoreIn"]
    )
    types["RestoreOut"] = t.struct(
        {
            "backup": t.string().optional(),
            "startTime": t.string().optional(),
            "type": t.string().optional(),
            "details": t.string().optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreOut"])
    types["PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["SecretIn"] = t.struct({"cloudSecret": t.string().optional()}).named(
        renames["SecretIn"]
    )
    types["SecretOut"] = t.struct(
        {
            "cloudSecret": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretOut"])
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
    types["BackupIn"] = t.struct(
        {"name": t.string().optional(), "description": t.string().optional()}
    ).named(renames["BackupIn"])
    types["BackupOut"] = t.struct(
        {
            "restoringServices": t.array(t.string()).optional(),
            "serviceRevision": t.proxy(renames["ServiceOut"]).optional(),
            "endTime": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupOut"])
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
    types["AlterMetadataResourceLocationResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AlterMetadataResourceLocationResponseIn"])
    types["AlterMetadataResourceLocationResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AlterMetadataResourceLocationResponseOut"])
    types["ListBackupsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "backups": t.array(t.proxy(renames["BackupIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListBackupsResponseIn"])
    types["ListBackupsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "backups": t.array(t.proxy(renames["BackupOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBackupsResponseOut"])
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["QueryMetadataRequestIn"] = t.struct({"query": t.string()}).named(
        renames["QueryMetadataRequestIn"]
    )
    types["QueryMetadataRequestOut"] = t.struct(
        {"query": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["QueryMetadataRequestOut"])
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
    types["DatabaseDumpIn"] = t.struct(
        {
            "gcsUri": t.string().optional(),
            "type": t.string().optional(),
            "sourceDatabase": t.string().optional(),
            "databaseType": t.string().optional(),
        }
    ).named(renames["DatabaseDumpIn"])
    types["DatabaseDumpOut"] = t.struct(
        {
            "gcsUri": t.string().optional(),
            "type": t.string().optional(),
            "sourceDatabase": t.string().optional(),
            "databaseType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseDumpOut"])
    types["MetadataExportIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MetadataExportIn"]
    )
    types["MetadataExportOut"] = t.struct(
        {
            "destinationGcsUri": t.string().optional(),
            "startTime": t.string().optional(),
            "databaseDumpType": t.string().optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataExportOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["ServiceIn"] = t.struct(
        {
            "scalingConfig": t.proxy(renames["ScalingConfigIn"]).optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigIn"]).optional(),
            "port": t.integer().optional(),
            "hiveMetastoreConfig": t.proxy(renames["HiveMetastoreConfigIn"]).optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowIn"]).optional(),
            "telemetryConfig": t.proxy(renames["TelemetryConfigIn"]).optional(),
            "name": t.string().optional(),
            "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
            "databaseType": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "network": t.string().optional(),
            "releaseChannel": t.string().optional(),
            "tier": t.string().optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "scalingConfig": t.proxy(renames["ScalingConfigOut"]).optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigOut"]).optional(),
            "port": t.integer().optional(),
            "metadataManagementActivity": t.proxy(
                renames["MetadataManagementActivityOut"]
            ).optional(),
            "hiveMetastoreConfig": t.proxy(
                renames["HiveMetastoreConfigOut"]
            ).optional(),
            "state": t.string().optional(),
            "stateMessage": t.string().optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowOut"]).optional(),
            "artifactGcsUri": t.string().optional(),
            "telemetryConfig": t.proxy(renames["TelemetryConfigOut"]).optional(),
            "name": t.string().optional(),
            "networkConfig": t.proxy(renames["NetworkConfigOut"]).optional(),
            "databaseType": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "network": t.string().optional(),
            "uid": t.string().optional(),
            "releaseChannel": t.string().optional(),
            "tier": t.string().optional(),
            "updateTime": t.string().optional(),
            "endpointUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
    types["TelemetryConfigIn"] = t.struct({"logFormat": t.string().optional()}).named(
        renames["TelemetryConfigIn"]
    )
    types["TelemetryConfigOut"] = t.struct(
        {
            "logFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TelemetryConfigOut"])
    types["MetadataManagementActivityIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["MetadataManagementActivityIn"])
    types["MetadataManagementActivityOut"] = t.struct(
        {
            "metadataExports": t.array(
                t.proxy(renames["MetadataExportOut"])
            ).optional(),
            "restores": t.array(t.proxy(renames["RestoreOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataManagementActivityOut"])
    types["FederationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "version": t.string().optional(),
            "backendMetastores": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["FederationIn"])
    types["FederationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "version": t.string().optional(),
            "state": t.string().optional(),
            "endpointUri": t.string().optional(),
            "backendMetastores": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "uid": t.string().optional(),
            "createTime": t.string().optional(),
            "stateMessage": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FederationOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["RestoreServiceRequestIn"] = t.struct(
        {
            "restoreType": t.string().optional(),
            "backup": t.string(),
            "requestId": t.string().optional(),
        }
    ).named(renames["RestoreServiceRequestIn"])
    types["RestoreServiceRequestOut"] = t.struct(
        {
            "restoreType": t.string().optional(),
            "backup": t.string(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreServiceRequestOut"])
    types["MetadataImportIn"] = t.struct(
        {
            "databaseDump": t.proxy(renames["DatabaseDumpIn"]).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["MetadataImportIn"])
    types["MetadataImportOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "databaseDump": t.proxy(renames["DatabaseDumpOut"]).optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "endTime": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataImportOut"])

    functions = {}
    functions["projectsLocationsGet"] = metastore.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
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
    functions["projectsLocationsServicesList"] = metastore.post(
        "v1/{service}:exportMetadata",
        t.struct(
            {
                "service": t.string(),
                "destinationGcsFolder": t.string().optional(),
                "requestId": t.string().optional(),
                "databaseDumpType": t.string().optional(),
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
                "destinationGcsFolder": t.string().optional(),
                "requestId": t.string().optional(),
                "databaseDumpType": t.string().optional(),
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
                "destinationGcsFolder": t.string().optional(),
                "requestId": t.string().optional(),
                "databaseDumpType": t.string().optional(),
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
                "destinationGcsFolder": t.string().optional(),
                "requestId": t.string().optional(),
                "databaseDumpType": t.string().optional(),
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
                "destinationGcsFolder": t.string().optional(),
                "requestId": t.string().optional(),
                "databaseDumpType": t.string().optional(),
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
                "destinationGcsFolder": t.string().optional(),
                "requestId": t.string().optional(),
                "databaseDumpType": t.string().optional(),
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
                "destinationGcsFolder": t.string().optional(),
                "requestId": t.string().optional(),
                "databaseDumpType": t.string().optional(),
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
                "destinationGcsFolder": t.string().optional(),
                "requestId": t.string().optional(),
                "databaseDumpType": t.string().optional(),
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
                "destinationGcsFolder": t.string().optional(),
                "requestId": t.string().optional(),
                "databaseDumpType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesPatch"] = metastore.post(
        "v1/{service}:exportMetadata",
        t.struct(
            {
                "service": t.string(),
                "destinationGcsFolder": t.string().optional(),
                "requestId": t.string().optional(),
                "databaseDumpType": t.string().optional(),
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
                "destinationGcsFolder": t.string().optional(),
                "requestId": t.string().optional(),
                "databaseDumpType": t.string().optional(),
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
                "destinationGcsFolder": t.string().optional(),
                "requestId": t.string().optional(),
                "databaseDumpType": t.string().optional(),
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
                "destinationGcsFolder": t.string().optional(),
                "requestId": t.string().optional(),
                "databaseDumpType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesBackupsList"] = metastore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesBackupsSetIamPolicy"] = metastore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesBackupsDelete"] = metastore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesBackupsGetIamPolicy"] = metastore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesBackupsCreate"] = metastore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesBackupsGet"] = metastore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesMetadataImportsCreate"] = metastore.get(
        "v1/{parent}/metadataImports",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMetadataImportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServicesMetadataImportsPatch"] = metastore.get(
        "v1/{parent}/metadataImports",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMetadataImportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsPatch"] = metastore.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsGet"] = metastore.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsSetIamPolicy"] = metastore.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsCreate"] = metastore.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsList"] = metastore.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsGetIamPolicy"] = metastore.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsDelete"] = metastore.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFederationsTestIamPermissions"] = metastore.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="metastore",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
