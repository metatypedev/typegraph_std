from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_sqladmin() -> Import:
    sqladmin = HTTPRuntime("https://sqladmin.googleapis.com/")

    renames = {
        "ErrorResponse": "_sqladmin_1_ErrorResponse",
        "AdvancedMachineFeaturesIn": "_sqladmin_2_AdvancedMachineFeaturesIn",
        "AdvancedMachineFeaturesOut": "_sqladmin_3_AdvancedMachineFeaturesOut",
        "BinLogCoordinatesIn": "_sqladmin_4_BinLogCoordinatesIn",
        "BinLogCoordinatesOut": "_sqladmin_5_BinLogCoordinatesOut",
        "DiskEncryptionConfigurationIn": "_sqladmin_6_DiskEncryptionConfigurationIn",
        "DiskEncryptionConfigurationOut": "_sqladmin_7_DiskEncryptionConfigurationOut",
        "SslCertsInsertRequestIn": "_sqladmin_8_SslCertsInsertRequestIn",
        "SslCertsInsertRequestOut": "_sqladmin_9_SslCertsInsertRequestOut",
        "PasswordStatusIn": "_sqladmin_10_PasswordStatusIn",
        "PasswordStatusOut": "_sqladmin_11_PasswordStatusOut",
        "InstancesRotateServerCaRequestIn": "_sqladmin_12_InstancesRotateServerCaRequestIn",
        "InstancesRotateServerCaRequestOut": "_sqladmin_13_InstancesRotateServerCaRequestOut",
        "SslCertsInsertResponseIn": "_sqladmin_14_SslCertsInsertResponseIn",
        "SslCertsInsertResponseOut": "_sqladmin_15_SslCertsInsertResponseOut",
        "InstancesListResponseIn": "_sqladmin_16_InstancesListResponseIn",
        "InstancesListResponseOut": "_sqladmin_17_InstancesListResponseOut",
        "InstanceReferenceIn": "_sqladmin_18_InstanceReferenceIn",
        "InstanceReferenceOut": "_sqladmin_19_InstanceReferenceOut",
        "DiskEncryptionStatusIn": "_sqladmin_20_DiskEncryptionStatusIn",
        "DiskEncryptionStatusOut": "_sqladmin_21_DiskEncryptionStatusOut",
        "ReplicaConfigurationIn": "_sqladmin_22_ReplicaConfigurationIn",
        "ReplicaConfigurationOut": "_sqladmin_23_ReplicaConfigurationOut",
        "BackupConfigurationIn": "_sqladmin_24_BackupConfigurationIn",
        "BackupConfigurationOut": "_sqladmin_25_BackupConfigurationOut",
        "ImportContextIn": "_sqladmin_26_ImportContextIn",
        "ImportContextOut": "_sqladmin_27_ImportContextOut",
        "SslCertsListResponseIn": "_sqladmin_28_SslCertsListResponseIn",
        "SslCertsListResponseOut": "_sqladmin_29_SslCertsListResponseOut",
        "BackupRunIn": "_sqladmin_30_BackupRunIn",
        "BackupRunOut": "_sqladmin_31_BackupRunOut",
        "DemoteMasterMySqlReplicaConfigurationIn": "_sqladmin_32_DemoteMasterMySqlReplicaConfigurationIn",
        "DemoteMasterMySqlReplicaConfigurationOut": "_sqladmin_33_DemoteMasterMySqlReplicaConfigurationOut",
        "DemoteMasterConfigurationIn": "_sqladmin_34_DemoteMasterConfigurationIn",
        "DemoteMasterConfigurationOut": "_sqladmin_35_DemoteMasterConfigurationOut",
        "UserIn": "_sqladmin_36_UserIn",
        "UserOut": "_sqladmin_37_UserOut",
        "TiersListResponseIn": "_sqladmin_38_TiersListResponseIn",
        "TiersListResponseOut": "_sqladmin_39_TiersListResponseOut",
        "SqlInstancesVerifyExternalSyncSettingsResponseIn": "_sqladmin_40_SqlInstancesVerifyExternalSyncSettingsResponseIn",
        "SqlInstancesVerifyExternalSyncSettingsResponseOut": "_sqladmin_41_SqlInstancesVerifyExternalSyncSettingsResponseOut",
        "MySqlSyncConfigIn": "_sqladmin_42_MySqlSyncConfigIn",
        "MySqlSyncConfigOut": "_sqladmin_43_MySqlSyncConfigOut",
        "OnPremisesConfigurationIn": "_sqladmin_44_OnPremisesConfigurationIn",
        "OnPremisesConfigurationOut": "_sqladmin_45_OnPremisesConfigurationOut",
        "InstancesDemoteMasterRequestIn": "_sqladmin_46_InstancesDemoteMasterRequestIn",
        "InstancesDemoteMasterRequestOut": "_sqladmin_47_InstancesDemoteMasterRequestOut",
        "OperationIn": "_sqladmin_48_OperationIn",
        "OperationOut": "_sqladmin_49_OperationOut",
        "PasswordValidationPolicyIn": "_sqladmin_50_PasswordValidationPolicyIn",
        "PasswordValidationPolicyOut": "_sqladmin_51_PasswordValidationPolicyOut",
        "OperationMetadataIn": "_sqladmin_52_OperationMetadataIn",
        "OperationMetadataOut": "_sqladmin_53_OperationMetadataOut",
        "InstancesImportRequestIn": "_sqladmin_54_InstancesImportRequestIn",
        "InstancesImportRequestOut": "_sqladmin_55_InstancesImportRequestOut",
        "PerformDiskShrinkContextIn": "_sqladmin_56_PerformDiskShrinkContextIn",
        "PerformDiskShrinkContextOut": "_sqladmin_57_PerformDiskShrinkContextOut",
        "SqlExternalSyncSettingErrorIn": "_sqladmin_58_SqlExternalSyncSettingErrorIn",
        "SqlExternalSyncSettingErrorOut": "_sqladmin_59_SqlExternalSyncSettingErrorOut",
        "SslCertsCreateEphemeralRequestIn": "_sqladmin_60_SslCertsCreateEphemeralRequestIn",
        "SslCertsCreateEphemeralRequestOut": "_sqladmin_61_SslCertsCreateEphemeralRequestOut",
        "DatabasesListResponseIn": "_sqladmin_62_DatabasesListResponseIn",
        "DatabasesListResponseOut": "_sqladmin_63_DatabasesListResponseOut",
        "InstancesCloneRequestIn": "_sqladmin_64_InstancesCloneRequestIn",
        "InstancesCloneRequestOut": "_sqladmin_65_InstancesCloneRequestOut",
        "RescheduleIn": "_sqladmin_66_RescheduleIn",
        "RescheduleOut": "_sqladmin_67_RescheduleOut",
        "BackupRunsListResponseIn": "_sqladmin_68_BackupRunsListResponseIn",
        "BackupRunsListResponseOut": "_sqladmin_69_BackupRunsListResponseOut",
        "DemoteMasterContextIn": "_sqladmin_70_DemoteMasterContextIn",
        "DemoteMasterContextOut": "_sqladmin_71_DemoteMasterContextOut",
        "SslCertDetailIn": "_sqladmin_72_SslCertDetailIn",
        "SslCertDetailOut": "_sqladmin_73_SslCertDetailOut",
        "InstancesRestoreBackupRequestIn": "_sqladmin_74_InstancesRestoreBackupRequestIn",
        "InstancesRestoreBackupRequestOut": "_sqladmin_75_InstancesRestoreBackupRequestOut",
        "GenerateEphemeralCertRequestIn": "_sqladmin_76_GenerateEphemeralCertRequestIn",
        "GenerateEphemeralCertRequestOut": "_sqladmin_77_GenerateEphemeralCertRequestOut",
        "TierIn": "_sqladmin_78_TierIn",
        "TierOut": "_sqladmin_79_TierOut",
        "FailoverContextIn": "_sqladmin_80_FailoverContextIn",
        "FailoverContextOut": "_sqladmin_81_FailoverContextOut",
        "SyncFlagsIn": "_sqladmin_82_SyncFlagsIn",
        "SyncFlagsOut": "_sqladmin_83_SyncFlagsOut",
        "FlagIn": "_sqladmin_84_FlagIn",
        "FlagOut": "_sqladmin_85_FlagOut",
        "SslCertIn": "_sqladmin_86_SslCertIn",
        "SslCertOut": "_sqladmin_87_SslCertOut",
        "OperationErrorsIn": "_sqladmin_88_OperationErrorsIn",
        "OperationErrorsOut": "_sqladmin_89_OperationErrorsOut",
        "BackupContextIn": "_sqladmin_90_BackupContextIn",
        "BackupContextOut": "_sqladmin_91_BackupContextOut",
        "InstancesListServerCasResponseIn": "_sqladmin_92_InstancesListServerCasResponseIn",
        "InstancesListServerCasResponseOut": "_sqladmin_93_InstancesListServerCasResponseOut",
        "InsightsConfigIn": "_sqladmin_94_InsightsConfigIn",
        "InsightsConfigOut": "_sqladmin_95_InsightsConfigOut",
        "SqlServerUserDetailsIn": "_sqladmin_96_SqlServerUserDetailsIn",
        "SqlServerUserDetailsOut": "_sqladmin_97_SqlServerUserDetailsOut",
        "MaintenanceWindowIn": "_sqladmin_98_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_sqladmin_99_MaintenanceWindowOut",
        "DatabaseIn": "_sqladmin_100_DatabaseIn",
        "DatabaseOut": "_sqladmin_101_DatabaseOut",
        "IpMappingIn": "_sqladmin_102_IpMappingIn",
        "IpMappingOut": "_sqladmin_103_IpMappingOut",
        "UserPasswordValidationPolicyIn": "_sqladmin_104_UserPasswordValidationPolicyIn",
        "UserPasswordValidationPolicyOut": "_sqladmin_105_UserPasswordValidationPolicyOut",
        "BackupRetentionSettingsIn": "_sqladmin_106_BackupRetentionSettingsIn",
        "BackupRetentionSettingsOut": "_sqladmin_107_BackupRetentionSettingsOut",
        "UsersListResponseIn": "_sqladmin_108_UsersListResponseIn",
        "UsersListResponseOut": "_sqladmin_109_UsersListResponseOut",
        "InstancesFailoverRequestIn": "_sqladmin_110_InstancesFailoverRequestIn",
        "InstancesFailoverRequestOut": "_sqladmin_111_InstancesFailoverRequestOut",
        "InstancesTruncateLogRequestIn": "_sqladmin_112_InstancesTruncateLogRequestIn",
        "InstancesTruncateLogRequestOut": "_sqladmin_113_InstancesTruncateLogRequestOut",
        "DenyMaintenancePeriodIn": "_sqladmin_114_DenyMaintenancePeriodIn",
        "DenyMaintenancePeriodOut": "_sqladmin_115_DenyMaintenancePeriodOut",
        "SqlInstancesStartExternalSyncRequestIn": "_sqladmin_116_SqlInstancesStartExternalSyncRequestIn",
        "SqlInstancesStartExternalSyncRequestOut": "_sqladmin_117_SqlInstancesStartExternalSyncRequestOut",
        "CloneContextIn": "_sqladmin_118_CloneContextIn",
        "CloneContextOut": "_sqladmin_119_CloneContextOut",
        "SqlOutOfDiskReportIn": "_sqladmin_120_SqlOutOfDiskReportIn",
        "SqlOutOfDiskReportOut": "_sqladmin_121_SqlOutOfDiskReportOut",
        "MySqlReplicaConfigurationIn": "_sqladmin_122_MySqlReplicaConfigurationIn",
        "MySqlReplicaConfigurationOut": "_sqladmin_123_MySqlReplicaConfigurationOut",
        "ConnectSettingsIn": "_sqladmin_124_ConnectSettingsIn",
        "ConnectSettingsOut": "_sqladmin_125_ConnectSettingsOut",
        "InstancesExportRequestIn": "_sqladmin_126_InstancesExportRequestIn",
        "InstancesExportRequestOut": "_sqladmin_127_InstancesExportRequestOut",
        "ApiWarningIn": "_sqladmin_128_ApiWarningIn",
        "ApiWarningOut": "_sqladmin_129_ApiWarningOut",
        "SqlServerDatabaseDetailsIn": "_sqladmin_130_SqlServerDatabaseDetailsIn",
        "SqlServerDatabaseDetailsOut": "_sqladmin_131_SqlServerDatabaseDetailsOut",
        "IpConfigurationIn": "_sqladmin_132_IpConfigurationIn",
        "IpConfigurationOut": "_sqladmin_133_IpConfigurationOut",
        "SqlInstancesRescheduleMaintenanceRequestBodyIn": "_sqladmin_134_SqlInstancesRescheduleMaintenanceRequestBodyIn",
        "SqlInstancesRescheduleMaintenanceRequestBodyOut": "_sqladmin_135_SqlInstancesRescheduleMaintenanceRequestBodyOut",
        "DatabaseFlagsIn": "_sqladmin_136_DatabaseFlagsIn",
        "DatabaseFlagsOut": "_sqladmin_137_DatabaseFlagsOut",
        "SqlServerAuditConfigIn": "_sqladmin_138_SqlServerAuditConfigIn",
        "SqlServerAuditConfigOut": "_sqladmin_139_SqlServerAuditConfigOut",
        "LocationPreferenceIn": "_sqladmin_140_LocationPreferenceIn",
        "LocationPreferenceOut": "_sqladmin_141_LocationPreferenceOut",
        "GenerateEphemeralCertResponseIn": "_sqladmin_142_GenerateEphemeralCertResponseIn",
        "GenerateEphemeralCertResponseOut": "_sqladmin_143_GenerateEphemeralCertResponseOut",
        "SqlScheduledMaintenanceIn": "_sqladmin_144_SqlScheduledMaintenanceIn",
        "SqlScheduledMaintenanceOut": "_sqladmin_145_SqlScheduledMaintenanceOut",
        "RotateServerCaContextIn": "_sqladmin_146_RotateServerCaContextIn",
        "RotateServerCaContextOut": "_sqladmin_147_RotateServerCaContextOut",
        "SqlActiveDirectoryConfigIn": "_sqladmin_148_SqlActiveDirectoryConfigIn",
        "SqlActiveDirectoryConfigOut": "_sqladmin_149_SqlActiveDirectoryConfigOut",
        "SqlInstancesResetReplicaSizeRequestIn": "_sqladmin_150_SqlInstancesResetReplicaSizeRequestIn",
        "SqlInstancesResetReplicaSizeRequestOut": "_sqladmin_151_SqlInstancesResetReplicaSizeRequestOut",
        "RestoreBackupContextIn": "_sqladmin_152_RestoreBackupContextIn",
        "RestoreBackupContextOut": "_sqladmin_153_RestoreBackupContextOut",
        "FlagsListResponseIn": "_sqladmin_154_FlagsListResponseIn",
        "FlagsListResponseOut": "_sqladmin_155_FlagsListResponseOut",
        "AclEntryIn": "_sqladmin_156_AclEntryIn",
        "AclEntryOut": "_sqladmin_157_AclEntryOut",
        "OperationsListResponseIn": "_sqladmin_158_OperationsListResponseIn",
        "OperationsListResponseOut": "_sqladmin_159_OperationsListResponseOut",
        "SettingsIn": "_sqladmin_160_SettingsIn",
        "SettingsOut": "_sqladmin_161_SettingsOut",
        "SqlInstancesVerifyExternalSyncSettingsRequestIn": "_sqladmin_162_SqlInstancesVerifyExternalSyncSettingsRequestIn",
        "SqlInstancesVerifyExternalSyncSettingsRequestOut": "_sqladmin_163_SqlInstancesVerifyExternalSyncSettingsRequestOut",
        "DatabaseInstanceIn": "_sqladmin_164_DatabaseInstanceIn",
        "DatabaseInstanceOut": "_sqladmin_165_DatabaseInstanceOut",
        "ExportContextIn": "_sqladmin_166_ExportContextIn",
        "ExportContextOut": "_sqladmin_167_ExportContextOut",
        "OperationErrorIn": "_sqladmin_168_OperationErrorIn",
        "OperationErrorOut": "_sqladmin_169_OperationErrorOut",
        "TruncateLogContextIn": "_sqladmin_170_TruncateLogContextIn",
        "TruncateLogContextOut": "_sqladmin_171_TruncateLogContextOut",
        "SqlInstancesGetDiskShrinkConfigResponseIn": "_sqladmin_172_SqlInstancesGetDiskShrinkConfigResponseIn",
        "SqlInstancesGetDiskShrinkConfigResponseOut": "_sqladmin_173_SqlInstancesGetDiskShrinkConfigResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AdvancedMachineFeaturesIn"] = t.struct(
        {"threadsPerCore": t.integer().optional()}
    ).named(renames["AdvancedMachineFeaturesIn"])
    types["AdvancedMachineFeaturesOut"] = t.struct(
        {
            "threadsPerCore": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvancedMachineFeaturesOut"])
    types["BinLogCoordinatesIn"] = t.struct(
        {
            "binLogFileName": t.string().optional(),
            "kind": t.string().optional(),
            "binLogPosition": t.string().optional(),
        }
    ).named(renames["BinLogCoordinatesIn"])
    types["BinLogCoordinatesOut"] = t.struct(
        {
            "binLogFileName": t.string().optional(),
            "kind": t.string().optional(),
            "binLogPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BinLogCoordinatesOut"])
    types["DiskEncryptionConfigurationIn"] = t.struct(
        {"kmsKeyName": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["DiskEncryptionConfigurationIn"])
    types["DiskEncryptionConfigurationOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskEncryptionConfigurationOut"])
    types["SslCertsInsertRequestIn"] = t.struct(
        {"commonName": t.string().optional()}
    ).named(renames["SslCertsInsertRequestIn"])
    types["SslCertsInsertRequestOut"] = t.struct(
        {
            "commonName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SslCertsInsertRequestOut"])
    types["PasswordStatusIn"] = t.struct(
        {
            "passwordExpirationTime": t.string().optional(),
            "locked": t.boolean().optional(),
        }
    ).named(renames["PasswordStatusIn"])
    types["PasswordStatusOut"] = t.struct(
        {
            "passwordExpirationTime": t.string().optional(),
            "locked": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PasswordStatusOut"])
    types["InstancesRotateServerCaRequestIn"] = t.struct(
        {
            "rotateServerCaContext": t.proxy(
                renames["RotateServerCaContextIn"]
            ).optional()
        }
    ).named(renames["InstancesRotateServerCaRequestIn"])
    types["InstancesRotateServerCaRequestOut"] = t.struct(
        {
            "rotateServerCaContext": t.proxy(
                renames["RotateServerCaContextOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesRotateServerCaRequestOut"])
    types["SslCertsInsertResponseIn"] = t.struct(
        {
            "operation": t.proxy(renames["OperationIn"]).optional(),
            "serverCaCert": t.proxy(renames["SslCertIn"]).optional(),
            "clientCert": t.proxy(renames["SslCertDetailIn"]).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["SslCertsInsertResponseIn"])
    types["SslCertsInsertResponseOut"] = t.struct(
        {
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "serverCaCert": t.proxy(renames["SslCertOut"]).optional(),
            "clientCert": t.proxy(renames["SslCertDetailOut"]).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SslCertsInsertResponseOut"])
    types["InstancesListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "warnings": t.array(t.proxy(renames["ApiWarningIn"])).optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["DatabaseInstanceIn"])).optional(),
        }
    ).named(renames["InstancesListResponseIn"])
    types["InstancesListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "warnings": t.array(t.proxy(renames["ApiWarningOut"])).optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["DatabaseInstanceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesListResponseOut"])
    types["InstanceReferenceIn"] = t.struct(
        {
            "region": t.string().optional(),
            "name": t.string().optional(),
            "project": t.string().optional(),
        }
    ).named(renames["InstanceReferenceIn"])
    types["InstanceReferenceOut"] = t.struct(
        {
            "region": t.string().optional(),
            "name": t.string().optional(),
            "project": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceReferenceOut"])
    types["DiskEncryptionStatusIn"] = t.struct(
        {"kmsKeyVersionName": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["DiskEncryptionStatusIn"])
    types["DiskEncryptionStatusOut"] = t.struct(
        {
            "kmsKeyVersionName": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskEncryptionStatusOut"])
    types["ReplicaConfigurationIn"] = t.struct(
        {
            "mysqlReplicaConfiguration": t.proxy(
                renames["MySqlReplicaConfigurationIn"]
            ).optional(),
            "failoverTarget": t.boolean().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ReplicaConfigurationIn"])
    types["ReplicaConfigurationOut"] = t.struct(
        {
            "mysqlReplicaConfiguration": t.proxy(
                renames["MySqlReplicaConfigurationOut"]
            ).optional(),
            "failoverTarget": t.boolean().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplicaConfigurationOut"])
    types["BackupConfigurationIn"] = t.struct(
        {
            "replicationLogArchivingEnabled": t.boolean().optional(),
            "pointInTimeRecoveryEnabled": t.boolean().optional(),
            "location": t.string().optional(),
            "kind": t.string().optional(),
            "enabled": t.boolean().optional(),
            "backupRetentionSettings": t.proxy(
                renames["BackupRetentionSettingsIn"]
            ).optional(),
            "startTime": t.string().optional(),
            "binaryLogEnabled": t.boolean().optional(),
            "transactionLogRetentionDays": t.integer().optional(),
        }
    ).named(renames["BackupConfigurationIn"])
    types["BackupConfigurationOut"] = t.struct(
        {
            "replicationLogArchivingEnabled": t.boolean().optional(),
            "pointInTimeRecoveryEnabled": t.boolean().optional(),
            "location": t.string().optional(),
            "kind": t.string().optional(),
            "enabled": t.boolean().optional(),
            "backupRetentionSettings": t.proxy(
                renames["BackupRetentionSettingsOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "binaryLogEnabled": t.boolean().optional(),
            "transactionLogRetentionDays": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupConfigurationOut"])
    types["ImportContextIn"] = t.struct(
        {
            "csvImportOptions": t.struct(
                {
                    "fieldsTerminatedBy": t.string().optional(),
                    "columns": t.array(t.string()).optional(),
                    "quoteCharacter": t.string().optional(),
                    "escapeCharacter": t.string().optional(),
                    "table": t.string().optional(),
                    "linesTerminatedBy": t.string().optional(),
                }
            ).optional(),
            "fileType": t.string().optional(),
            "importUser": t.string().optional(),
            "database": t.string().optional(),
            "uri": t.string().optional(),
            "bakImportOptions": t.struct(
                {
                    "encryptionOptions": t.struct(
                        {
                            "certPath": t.string().optional(),
                            "pvkPath": t.string().optional(),
                            "pvkPassword": t.string().optional(),
                        }
                    ),
                    "striped": t.boolean().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ImportContextIn"])
    types["ImportContextOut"] = t.struct(
        {
            "csvImportOptions": t.struct(
                {
                    "fieldsTerminatedBy": t.string().optional(),
                    "columns": t.array(t.string()).optional(),
                    "quoteCharacter": t.string().optional(),
                    "escapeCharacter": t.string().optional(),
                    "table": t.string().optional(),
                    "linesTerminatedBy": t.string().optional(),
                }
            ).optional(),
            "fileType": t.string().optional(),
            "importUser": t.string().optional(),
            "database": t.string().optional(),
            "uri": t.string().optional(),
            "bakImportOptions": t.struct(
                {
                    "encryptionOptions": t.struct(
                        {
                            "certPath": t.string().optional(),
                            "pvkPath": t.string().optional(),
                            "pvkPassword": t.string().optional(),
                        }
                    ),
                    "striped": t.boolean().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportContextOut"])
    types["SslCertsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["SslCertIn"])).optional(),
        }
    ).named(renames["SslCertsListResponseIn"])
    types["SslCertsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["SslCertOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SslCertsListResponseOut"])
    types["BackupRunIn"] = t.struct(
        {
            "diskEncryptionStatus": t.proxy(
                renames["DiskEncryptionStatusIn"]
            ).optional(),
            "type": t.string().optional(),
            "enqueuedTime": t.string().optional(),
            "location": t.string().optional(),
            "backupKind": t.string().optional(),
            "kind": t.string().optional(),
            "startTime": t.string().optional(),
            "timeZone": t.string().optional(),
            "description": t.string().optional(),
            "windowStartTime": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["OperationErrorIn"]).optional(),
            "endTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "diskEncryptionConfiguration": t.proxy(
                renames["DiskEncryptionConfigurationIn"]
            ).optional(),
            "id": t.string().optional(),
            "instance": t.string().optional(),
        }
    ).named(renames["BackupRunIn"])
    types["BackupRunOut"] = t.struct(
        {
            "diskEncryptionStatus": t.proxy(
                renames["DiskEncryptionStatusOut"]
            ).optional(),
            "type": t.string().optional(),
            "enqueuedTime": t.string().optional(),
            "location": t.string().optional(),
            "backupKind": t.string().optional(),
            "kind": t.string().optional(),
            "startTime": t.string().optional(),
            "timeZone": t.string().optional(),
            "description": t.string().optional(),
            "windowStartTime": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "endTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "diskEncryptionConfiguration": t.proxy(
                renames["DiskEncryptionConfigurationOut"]
            ).optional(),
            "id": t.string().optional(),
            "instance": t.string().optional(),
        }
    ).named(renames["BackupRunOut"])
    types["DemoteMasterMySqlReplicaConfigurationIn"] = t.struct(
        {
            "password": t.string().optional(),
            "username": t.string().optional(),
            "kind": t.string().optional(),
            "caCertificate": t.string().optional(),
            "clientKey": t.string().optional(),
            "clientCertificate": t.string().optional(),
        }
    ).named(renames["DemoteMasterMySqlReplicaConfigurationIn"])
    types["DemoteMasterMySqlReplicaConfigurationOut"] = t.struct(
        {
            "password": t.string().optional(),
            "username": t.string().optional(),
            "kind": t.string().optional(),
            "caCertificate": t.string().optional(),
            "clientKey": t.string().optional(),
            "clientCertificate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DemoteMasterMySqlReplicaConfigurationOut"])
    types["DemoteMasterConfigurationIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "mysqlReplicaConfiguration": t.proxy(
                renames["DemoteMasterMySqlReplicaConfigurationIn"]
            ).optional(),
        }
    ).named(renames["DemoteMasterConfigurationIn"])
    types["DemoteMasterConfigurationOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "mysqlReplicaConfiguration": t.proxy(
                renames["DemoteMasterMySqlReplicaConfigurationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DemoteMasterConfigurationOut"])
    types["UserIn"] = t.struct(
        {
            "project": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "sqlserverUserDetails": t.proxy(renames["SqlServerUserDetailsIn"]),
            "etag": t.string().optional(),
            "host": t.string().optional(),
            "type": t.string().optional(),
            "passwordPolicy": t.proxy(
                renames["UserPasswordValidationPolicyIn"]
            ).optional(),
            "password": t.string().optional(),
            "dualPasswordType": t.string().optional(),
            "instance": t.string().optional(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "project": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "sqlserverUserDetails": t.proxy(renames["SqlServerUserDetailsOut"]),
            "etag": t.string().optional(),
            "host": t.string().optional(),
            "type": t.string().optional(),
            "passwordPolicy": t.proxy(
                renames["UserPasswordValidationPolicyOut"]
            ).optional(),
            "password": t.string().optional(),
            "dualPasswordType": t.string().optional(),
            "instance": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["TiersListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["TierIn"])).optional(),
        }
    ).named(renames["TiersListResponseIn"])
    types["TiersListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["TierOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TiersListResponseOut"])
    types["SqlInstancesVerifyExternalSyncSettingsResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "warnings": t.array(
                t.proxy(renames["SqlExternalSyncSettingErrorIn"])
            ).optional(),
            "errors": t.array(
                t.proxy(renames["SqlExternalSyncSettingErrorIn"])
            ).optional(),
        }
    ).named(renames["SqlInstancesVerifyExternalSyncSettingsResponseIn"])
    types["SqlInstancesVerifyExternalSyncSettingsResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "warnings": t.array(
                t.proxy(renames["SqlExternalSyncSettingErrorOut"])
            ).optional(),
            "errors": t.array(
                t.proxy(renames["SqlExternalSyncSettingErrorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlInstancesVerifyExternalSyncSettingsResponseOut"])
    types["MySqlSyncConfigIn"] = t.struct(
        {"initialSyncFlags": t.array(t.proxy(renames["SyncFlagsIn"])).optional()}
    ).named(renames["MySqlSyncConfigIn"])
    types["MySqlSyncConfigOut"] = t.struct(
        {
            "initialSyncFlags": t.array(t.proxy(renames["SyncFlagsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MySqlSyncConfigOut"])
    types["OnPremisesConfigurationIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "password": t.string().optional(),
            "username": t.string().optional(),
            "clientKey": t.string().optional(),
            "hostPort": t.string().optional(),
            "sourceInstance": t.proxy(renames["InstanceReferenceIn"]).optional(),
            "clientCertificate": t.string().optional(),
            "dumpFilePath": t.string().optional(),
            "caCertificate": t.string().optional(),
        }
    ).named(renames["OnPremisesConfigurationIn"])
    types["OnPremisesConfigurationOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "password": t.string().optional(),
            "username": t.string().optional(),
            "clientKey": t.string().optional(),
            "hostPort": t.string().optional(),
            "sourceInstance": t.proxy(renames["InstanceReferenceOut"]).optional(),
            "clientCertificate": t.string().optional(),
            "dumpFilePath": t.string().optional(),
            "caCertificate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OnPremisesConfigurationOut"])
    types["InstancesDemoteMasterRequestIn"] = t.struct(
        {"demoteMasterContext": t.proxy(renames["DemoteMasterContextIn"]).optional()}
    ).named(renames["InstancesDemoteMasterRequestIn"])
    types["InstancesDemoteMasterRequestOut"] = t.struct(
        {
            "demoteMasterContext": t.proxy(
                renames["DemoteMasterContextOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesDemoteMasterRequestOut"])
    types["OperationIn"] = t.struct(
        {
            "backupContext": t.proxy(renames["BackupContextIn"]).optional(),
            "exportContext": t.proxy(renames["ExportContextIn"]).optional(),
            "importContext": t.proxy(renames["ImportContextIn"]).optional(),
            "insertTime": t.string().optional(),
            "targetId": t.string().optional(),
            "kind": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["OperationErrorsIn"]).optional(),
            "name": t.string().optional(),
            "operationType": t.string().optional(),
            "startTime": t.string().optional(),
            "status": t.string().optional(),
            "targetProject": t.string().optional(),
            "selfLink": t.string().optional(),
            "targetLink": t.string(),
            "user": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "backupContext": t.proxy(renames["BackupContextOut"]).optional(),
            "exportContext": t.proxy(renames["ExportContextOut"]).optional(),
            "importContext": t.proxy(renames["ImportContextOut"]).optional(),
            "insertTime": t.string().optional(),
            "targetId": t.string().optional(),
            "kind": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "operationType": t.string().optional(),
            "startTime": t.string().optional(),
            "status": t.string().optional(),
            "targetProject": t.string().optional(),
            "selfLink": t.string().optional(),
            "targetLink": t.string(),
            "user": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["PasswordValidationPolicyIn"] = t.struct(
        {
            "enablePasswordPolicy": t.boolean().optional(),
            "reuseInterval": t.integer().optional(),
            "complexity": t.string().optional(),
            "minLength": t.integer().optional(),
            "disallowUsernameSubstring": t.boolean().optional(),
            "passwordChangeInterval": t.string().optional(),
        }
    ).named(renames["PasswordValidationPolicyIn"])
    types["PasswordValidationPolicyOut"] = t.struct(
        {
            "enablePasswordPolicy": t.boolean().optional(),
            "reuseInterval": t.integer().optional(),
            "complexity": t.string().optional(),
            "minLength": t.integer().optional(),
            "disallowUsernameSubstring": t.boolean().optional(),
            "passwordChangeInterval": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PasswordValidationPolicyOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "statusDetail": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["InstancesImportRequestIn"] = t.struct(
        {"importContext": t.proxy(renames["ImportContextIn"]).optional()}
    ).named(renames["InstancesImportRequestIn"])
    types["InstancesImportRequestOut"] = t.struct(
        {
            "importContext": t.proxy(renames["ImportContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesImportRequestOut"])
    types["PerformDiskShrinkContextIn"] = t.struct(
        {"targetSizeGb": t.string().optional()}
    ).named(renames["PerformDiskShrinkContextIn"])
    types["PerformDiskShrinkContextOut"] = t.struct(
        {
            "targetSizeGb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerformDiskShrinkContextOut"])
    types["SqlExternalSyncSettingErrorIn"] = t.struct(
        {
            "type": t.string().optional(),
            "detail": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["SqlExternalSyncSettingErrorIn"])
    types["SqlExternalSyncSettingErrorOut"] = t.struct(
        {
            "type": t.string().optional(),
            "detail": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlExternalSyncSettingErrorOut"])
    types["SslCertsCreateEphemeralRequestIn"] = t.struct(
        {"access_token": t.string().optional(), "public_key": t.string().optional()}
    ).named(renames["SslCertsCreateEphemeralRequestIn"])
    types["SslCertsCreateEphemeralRequestOut"] = t.struct(
        {
            "access_token": t.string().optional(),
            "public_key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SslCertsCreateEphemeralRequestOut"])
    types["DatabasesListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["DatabaseIn"])).optional(),
        }
    ).named(renames["DatabasesListResponseIn"])
    types["DatabasesListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["DatabaseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabasesListResponseOut"])
    types["InstancesCloneRequestIn"] = t.struct(
        {"cloneContext": t.proxy(renames["CloneContextIn"]).optional()}
    ).named(renames["InstancesCloneRequestIn"])
    types["InstancesCloneRequestOut"] = t.struct(
        {
            "cloneContext": t.proxy(renames["CloneContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesCloneRequestOut"])
    types["RescheduleIn"] = t.struct(
        {"scheduleTime": t.string().optional(), "rescheduleType": t.string()}
    ).named(renames["RescheduleIn"])
    types["RescheduleOut"] = t.struct(
        {
            "scheduleTime": t.string().optional(),
            "rescheduleType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RescheduleOut"])
    types["BackupRunsListResponseIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["BackupRunIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["BackupRunsListResponseIn"])
    types["BackupRunsListResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["BackupRunOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupRunsListResponseOut"])
    types["DemoteMasterContextIn"] = t.struct(
        {
            "replicaConfiguration": t.proxy(
                renames["DemoteMasterConfigurationIn"]
            ).optional(),
            "kind": t.string().optional(),
            "verifyGtidConsistency": t.boolean().optional(),
            "skipReplicationSetup": t.boolean().optional(),
            "masterInstanceName": t.string().optional(),
        }
    ).named(renames["DemoteMasterContextIn"])
    types["DemoteMasterContextOut"] = t.struct(
        {
            "replicaConfiguration": t.proxy(
                renames["DemoteMasterConfigurationOut"]
            ).optional(),
            "kind": t.string().optional(),
            "verifyGtidConsistency": t.boolean().optional(),
            "skipReplicationSetup": t.boolean().optional(),
            "masterInstanceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DemoteMasterContextOut"])
    types["SslCertDetailIn"] = t.struct(
        {
            "certInfo": t.proxy(renames["SslCertIn"]).optional(),
            "certPrivateKey": t.string().optional(),
        }
    ).named(renames["SslCertDetailIn"])
    types["SslCertDetailOut"] = t.struct(
        {
            "certInfo": t.proxy(renames["SslCertOut"]).optional(),
            "certPrivateKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SslCertDetailOut"])
    types["InstancesRestoreBackupRequestIn"] = t.struct(
        {"restoreBackupContext": t.proxy(renames["RestoreBackupContextIn"]).optional()}
    ).named(renames["InstancesRestoreBackupRequestIn"])
    types["InstancesRestoreBackupRequestOut"] = t.struct(
        {
            "restoreBackupContext": t.proxy(
                renames["RestoreBackupContextOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesRestoreBackupRequestOut"])
    types["GenerateEphemeralCertRequestIn"] = t.struct(
        {
            "access_token": t.string().optional(),
            "validDuration": t.string().optional(),
            "public_key": t.string().optional(),
            "readTime": t.string().optional(),
        }
    ).named(renames["GenerateEphemeralCertRequestIn"])
    types["GenerateEphemeralCertRequestOut"] = t.struct(
        {
            "access_token": t.string().optional(),
            "validDuration": t.string().optional(),
            "public_key": t.string().optional(),
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateEphemeralCertRequestOut"])
    types["TierIn"] = t.struct(
        {
            "tier": t.string().optional(),
            "region": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "RAM": t.string().optional(),
            "DiskQuota": t.string().optional(),
        }
    ).named(renames["TierIn"])
    types["TierOut"] = t.struct(
        {
            "tier": t.string().optional(),
            "region": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "RAM": t.string().optional(),
            "DiskQuota": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TierOut"])
    types["FailoverContextIn"] = t.struct(
        {"kind": t.string().optional(), "settingsVersion": t.string().optional()}
    ).named(renames["FailoverContextIn"])
    types["FailoverContextOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "settingsVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FailoverContextOut"])
    types["SyncFlagsIn"] = t.struct(
        {"name": t.string().optional(), "value": t.string().optional()}
    ).named(renames["SyncFlagsIn"])
    types["SyncFlagsOut"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SyncFlagsOut"])
    types["FlagIn"] = t.struct(
        {
            "appliesTo": t.array(t.string()).optional(),
            "inBeta": t.boolean().optional(),
            "maxValue": t.string().optional(),
            "allowedStringValues": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "allowedIntValues": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "requiresRestart": t.boolean().optional(),
            "minValue": t.string().optional(),
        }
    ).named(renames["FlagIn"])
    types["FlagOut"] = t.struct(
        {
            "appliesTo": t.array(t.string()).optional(),
            "inBeta": t.boolean().optional(),
            "maxValue": t.string().optional(),
            "allowedStringValues": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "allowedIntValues": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "requiresRestart": t.boolean().optional(),
            "minValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FlagOut"])
    types["SslCertIn"] = t.struct(
        {
            "commonName": t.string().optional(),
            "expirationTime": t.string().optional(),
            "kind": t.string().optional(),
            "instance": t.string().optional(),
            "selfLink": t.string().optional(),
            "certSerialNumber": t.string().optional(),
            "cert": t.string().optional(),
            "createTime": t.string().optional(),
            "sha1Fingerprint": t.string().optional(),
        }
    ).named(renames["SslCertIn"])
    types["SslCertOut"] = t.struct(
        {
            "commonName": t.string().optional(),
            "expirationTime": t.string().optional(),
            "kind": t.string().optional(),
            "instance": t.string().optional(),
            "selfLink": t.string().optional(),
            "certSerialNumber": t.string().optional(),
            "cert": t.string().optional(),
            "createTime": t.string().optional(),
            "sha1Fingerprint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SslCertOut"])
    types["OperationErrorsIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "errors": t.array(t.proxy(renames["OperationErrorIn"])).optional(),
        }
    ).named(renames["OperationErrorsIn"])
    types["OperationErrorsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "errors": t.array(t.proxy(renames["OperationErrorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationErrorsOut"])
    types["BackupContextIn"] = t.struct(
        {"backupId": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["BackupContextIn"])
    types["BackupContextOut"] = t.struct(
        {
            "backupId": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupContextOut"])
    types["InstancesListServerCasResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "activeVersion": t.string(),
            "certs": t.array(t.proxy(renames["SslCertIn"])).optional(),
        }
    ).named(renames["InstancesListServerCasResponseIn"])
    types["InstancesListServerCasResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "activeVersion": t.string(),
            "certs": t.array(t.proxy(renames["SslCertOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesListServerCasResponseOut"])
    types["InsightsConfigIn"] = t.struct(
        {
            "recordApplicationTags": t.boolean().optional(),
            "recordClientAddress": t.boolean().optional(),
            "queryInsightsEnabled": t.boolean().optional(),
            "queryStringLength": t.integer().optional(),
            "queryPlansPerMinute": t.integer().optional(),
        }
    ).named(renames["InsightsConfigIn"])
    types["InsightsConfigOut"] = t.struct(
        {
            "recordApplicationTags": t.boolean().optional(),
            "recordClientAddress": t.boolean().optional(),
            "queryInsightsEnabled": t.boolean().optional(),
            "queryStringLength": t.integer().optional(),
            "queryPlansPerMinute": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsightsConfigOut"])
    types["SqlServerUserDetailsIn"] = t.struct(
        {
            "serverRoles": t.array(t.string()).optional(),
            "disabled": t.boolean().optional(),
        }
    ).named(renames["SqlServerUserDetailsIn"])
    types["SqlServerUserDetailsOut"] = t.struct(
        {
            "serverRoles": t.array(t.string()).optional(),
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlServerUserDetailsOut"])
    types["MaintenanceWindowIn"] = t.struct(
        {
            "hour": t.integer().optional(),
            "updateTrack": t.string().optional(),
            "kind": t.string().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["MaintenanceWindowIn"])
    types["MaintenanceWindowOut"] = t.struct(
        {
            "hour": t.integer().optional(),
            "updateTrack": t.string().optional(),
            "kind": t.string().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceWindowOut"])
    types["DatabaseIn"] = t.struct(
        {
            "instance": t.string().optional(),
            "charset": t.string().optional(),
            "etag": t.string().optional(),
            "project": t.string().optional(),
            "sqlserverDatabaseDetails": t.proxy(renames["SqlServerDatabaseDetailsIn"]),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "collation": t.string().optional(),
            "selfLink": t.string().optional(),
        }
    ).named(renames["DatabaseIn"])
    types["DatabaseOut"] = t.struct(
        {
            "instance": t.string().optional(),
            "charset": t.string().optional(),
            "etag": t.string().optional(),
            "project": t.string().optional(),
            "sqlserverDatabaseDetails": t.proxy(renames["SqlServerDatabaseDetailsOut"]),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "collation": t.string().optional(),
            "selfLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseOut"])
    types["IpMappingIn"] = t.struct(
        {
            "timeToRetire": t.string().optional(),
            "type": t.string().optional(),
            "ipAddress": t.string().optional(),
        }
    ).named(renames["IpMappingIn"])
    types["IpMappingOut"] = t.struct(
        {
            "timeToRetire": t.string().optional(),
            "type": t.string().optional(),
            "ipAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IpMappingOut"])
    types["UserPasswordValidationPolicyIn"] = t.struct(
        {
            "allowedFailedAttempts": t.integer().optional(),
            "enableFailedAttemptsCheck": t.boolean().optional(),
            "passwordExpirationDuration": t.string().optional(),
            "enablePasswordVerification": t.boolean().optional(),
        }
    ).named(renames["UserPasswordValidationPolicyIn"])
    types["UserPasswordValidationPolicyOut"] = t.struct(
        {
            "allowedFailedAttempts": t.integer().optional(),
            "enableFailedAttemptsCheck": t.boolean().optional(),
            "status": t.proxy(renames["PasswordStatusOut"]).optional(),
            "passwordExpirationDuration": t.string().optional(),
            "enablePasswordVerification": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserPasswordValidationPolicyOut"])
    types["BackupRetentionSettingsIn"] = t.struct(
        {
            "retainedBackups": t.integer().optional(),
            "retentionUnit": t.string().optional(),
        }
    ).named(renames["BackupRetentionSettingsIn"])
    types["BackupRetentionSettingsOut"] = t.struct(
        {
            "retainedBackups": t.integer().optional(),
            "retentionUnit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupRetentionSettingsOut"])
    types["UsersListResponseIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["UserIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["UsersListResponseIn"])
    types["UsersListResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["UserOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsersListResponseOut"])
    types["InstancesFailoverRequestIn"] = t.struct(
        {"failoverContext": t.proxy(renames["FailoverContextIn"]).optional()}
    ).named(renames["InstancesFailoverRequestIn"])
    types["InstancesFailoverRequestOut"] = t.struct(
        {
            "failoverContext": t.proxy(renames["FailoverContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesFailoverRequestOut"])
    types["InstancesTruncateLogRequestIn"] = t.struct(
        {"truncateLogContext": t.proxy(renames["TruncateLogContextIn"]).optional()}
    ).named(renames["InstancesTruncateLogRequestIn"])
    types["InstancesTruncateLogRequestOut"] = t.struct(
        {
            "truncateLogContext": t.proxy(renames["TruncateLogContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesTruncateLogRequestOut"])
    types["DenyMaintenancePeriodIn"] = t.struct(
        {
            "startDate": t.string().optional(),
            "time": t.string().optional(),
            "endDate": t.string().optional(),
        }
    ).named(renames["DenyMaintenancePeriodIn"])
    types["DenyMaintenancePeriodOut"] = t.struct(
        {
            "startDate": t.string().optional(),
            "time": t.string().optional(),
            "endDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DenyMaintenancePeriodOut"])
    types["SqlInstancesStartExternalSyncRequestIn"] = t.struct(
        {
            "mysqlSyncConfig": t.proxy(renames["MySqlSyncConfigIn"]).optional(),
            "skipVerification": t.boolean().optional(),
            "syncMode": t.string().optional(),
        }
    ).named(renames["SqlInstancesStartExternalSyncRequestIn"])
    types["SqlInstancesStartExternalSyncRequestOut"] = t.struct(
        {
            "mysqlSyncConfig": t.proxy(renames["MySqlSyncConfigOut"]).optional(),
            "skipVerification": t.boolean().optional(),
            "syncMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlInstancesStartExternalSyncRequestOut"])
    types["CloneContextIn"] = t.struct(
        {
            "pitrTimestampMs": t.string().optional(),
            "preferredZone": t.string().optional(),
            "kind": t.string().optional(),
            "binLogCoordinates": t.proxy(renames["BinLogCoordinatesIn"]).optional(),
            "databaseNames": t.array(t.string()).optional(),
            "allocatedIpRange": t.string().optional(),
            "pointInTime": t.string().optional(),
            "destinationInstanceName": t.string().optional(),
        }
    ).named(renames["CloneContextIn"])
    types["CloneContextOut"] = t.struct(
        {
            "pitrTimestampMs": t.string().optional(),
            "preferredZone": t.string().optional(),
            "kind": t.string().optional(),
            "binLogCoordinates": t.proxy(renames["BinLogCoordinatesOut"]).optional(),
            "databaseNames": t.array(t.string()).optional(),
            "allocatedIpRange": t.string().optional(),
            "pointInTime": t.string().optional(),
            "destinationInstanceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloneContextOut"])
    types["SqlOutOfDiskReportIn"] = t.struct(
        {
            "sqlMinRecommendedIncreaseSizeGb": t.integer().optional(),
            "sqlOutOfDiskState": t.string().optional(),
        }
    ).named(renames["SqlOutOfDiskReportIn"])
    types["SqlOutOfDiskReportOut"] = t.struct(
        {
            "sqlMinRecommendedIncreaseSizeGb": t.integer().optional(),
            "sqlOutOfDiskState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlOutOfDiskReportOut"])
    types["MySqlReplicaConfigurationIn"] = t.struct(
        {
            "verifyServerCertificate": t.boolean().optional(),
            "masterHeartbeatPeriod": t.string().optional(),
            "sslCipher": t.string().optional(),
            "clientKey": t.string().optional(),
            "password": t.string().optional(),
            "caCertificate": t.string().optional(),
            "kind": t.string().optional(),
            "connectRetryInterval": t.integer().optional(),
            "dumpFilePath": t.string().optional(),
            "clientCertificate": t.string().optional(),
            "username": t.string().optional(),
        }
    ).named(renames["MySqlReplicaConfigurationIn"])
    types["MySqlReplicaConfigurationOut"] = t.struct(
        {
            "verifyServerCertificate": t.boolean().optional(),
            "masterHeartbeatPeriod": t.string().optional(),
            "sslCipher": t.string().optional(),
            "clientKey": t.string().optional(),
            "password": t.string().optional(),
            "caCertificate": t.string().optional(),
            "kind": t.string().optional(),
            "connectRetryInterval": t.integer().optional(),
            "dumpFilePath": t.string().optional(),
            "clientCertificate": t.string().optional(),
            "username": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MySqlReplicaConfigurationOut"])
    types["ConnectSettingsIn"] = t.struct(
        {
            "backendType": t.string().optional(),
            "serverCaCert": t.proxy(renames["SslCertIn"]).optional(),
            "region": t.string().optional(),
            "databaseVersion": t.string().optional(),
            "ipAddresses": t.array(t.proxy(renames["IpMappingIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ConnectSettingsIn"])
    types["ConnectSettingsOut"] = t.struct(
        {
            "backendType": t.string().optional(),
            "serverCaCert": t.proxy(renames["SslCertOut"]).optional(),
            "region": t.string().optional(),
            "databaseVersion": t.string().optional(),
            "ipAddresses": t.array(t.proxy(renames["IpMappingOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectSettingsOut"])
    types["InstancesExportRequestIn"] = t.struct(
        {"exportContext": t.proxy(renames["ExportContextIn"]).optional()}
    ).named(renames["InstancesExportRequestIn"])
    types["InstancesExportRequestOut"] = t.struct(
        {
            "exportContext": t.proxy(renames["ExportContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesExportRequestOut"])
    types["ApiWarningIn"] = t.struct(
        {
            "code": t.string().optional(),
            "message": t.string().optional(),
            "region": t.string().optional(),
        }
    ).named(renames["ApiWarningIn"])
    types["ApiWarningOut"] = t.struct(
        {
            "code": t.string().optional(),
            "message": t.string().optional(),
            "region": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiWarningOut"])
    types["SqlServerDatabaseDetailsIn"] = t.struct(
        {
            "recoveryModel": t.string().optional(),
            "compatibilityLevel": t.integer().optional(),
        }
    ).named(renames["SqlServerDatabaseDetailsIn"])
    types["SqlServerDatabaseDetailsOut"] = t.struct(
        {
            "recoveryModel": t.string().optional(),
            "compatibilityLevel": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlServerDatabaseDetailsOut"])
    types["IpConfigurationIn"] = t.struct(
        {
            "requireSsl": t.boolean().optional(),
            "allocatedIpRange": t.string().optional(),
            "enablePrivatePathForGoogleCloudServices": t.boolean().optional(),
            "privateNetwork": t.string().optional(),
            "authorizedNetworks": t.array(t.proxy(renames["AclEntryIn"])).optional(),
            "ipv4Enabled": t.boolean().optional(),
        }
    ).named(renames["IpConfigurationIn"])
    types["IpConfigurationOut"] = t.struct(
        {
            "requireSsl": t.boolean().optional(),
            "allocatedIpRange": t.string().optional(),
            "enablePrivatePathForGoogleCloudServices": t.boolean().optional(),
            "privateNetwork": t.string().optional(),
            "authorizedNetworks": t.array(t.proxy(renames["AclEntryOut"])).optional(),
            "ipv4Enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IpConfigurationOut"])
    types["SqlInstancesRescheduleMaintenanceRequestBodyIn"] = t.struct(
        {"reschedule": t.proxy(renames["RescheduleIn"])}
    ).named(renames["SqlInstancesRescheduleMaintenanceRequestBodyIn"])
    types["SqlInstancesRescheduleMaintenanceRequestBodyOut"] = t.struct(
        {
            "reschedule": t.proxy(renames["RescheduleOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlInstancesRescheduleMaintenanceRequestBodyOut"])
    types["DatabaseFlagsIn"] = t.struct(
        {"name": t.string().optional(), "value": t.string().optional()}
    ).named(renames["DatabaseFlagsIn"])
    types["DatabaseFlagsOut"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseFlagsOut"])
    types["SqlServerAuditConfigIn"] = t.struct(
        {
            "uploadInterval": t.string().optional(),
            "bucket": t.string().optional(),
            "kind": t.string().optional(),
            "retentionInterval": t.string().optional(),
        }
    ).named(renames["SqlServerAuditConfigIn"])
    types["SqlServerAuditConfigOut"] = t.struct(
        {
            "uploadInterval": t.string().optional(),
            "bucket": t.string().optional(),
            "kind": t.string().optional(),
            "retentionInterval": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlServerAuditConfigOut"])
    types["LocationPreferenceIn"] = t.struct(
        {
            "followGaeApplication": t.string().optional(),
            "kind": t.string().optional(),
            "secondaryZone": t.string().optional(),
            "zone": t.string().optional(),
        }
    ).named(renames["LocationPreferenceIn"])
    types["LocationPreferenceOut"] = t.struct(
        {
            "followGaeApplication": t.string().optional(),
            "kind": t.string().optional(),
            "secondaryZone": t.string().optional(),
            "zone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationPreferenceOut"])
    types["GenerateEphemeralCertResponseIn"] = t.struct(
        {"ephemeralCert": t.proxy(renames["SslCertIn"]).optional()}
    ).named(renames["GenerateEphemeralCertResponseIn"])
    types["GenerateEphemeralCertResponseOut"] = t.struct(
        {
            "ephemeralCert": t.proxy(renames["SslCertOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateEphemeralCertResponseOut"])
    types["SqlScheduledMaintenanceIn"] = t.struct(
        {
            "canDefer": t.boolean(),
            "canReschedule": t.boolean().optional(),
            "startTime": t.string().optional(),
            "scheduleDeadlineTime": t.string().optional(),
        }
    ).named(renames["SqlScheduledMaintenanceIn"])
    types["SqlScheduledMaintenanceOut"] = t.struct(
        {
            "canDefer": t.boolean(),
            "canReschedule": t.boolean().optional(),
            "startTime": t.string().optional(),
            "scheduleDeadlineTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlScheduledMaintenanceOut"])
    types["RotateServerCaContextIn"] = t.struct(
        {"nextVersion": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["RotateServerCaContextIn"])
    types["RotateServerCaContextOut"] = t.struct(
        {
            "nextVersion": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RotateServerCaContextOut"])
    types["SqlActiveDirectoryConfigIn"] = t.struct(
        {"kind": t.string().optional(), "domain": t.string().optional()}
    ).named(renames["SqlActiveDirectoryConfigIn"])
    types["SqlActiveDirectoryConfigOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "domain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlActiveDirectoryConfigOut"])
    types["SqlInstancesResetReplicaSizeRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SqlInstancesResetReplicaSizeRequestIn"])
    types["SqlInstancesResetReplicaSizeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SqlInstancesResetReplicaSizeRequestOut"])
    types["RestoreBackupContextIn"] = t.struct(
        {
            "backupRunId": t.string().optional(),
            "instanceId": t.string().optional(),
            "kind": t.string().optional(),
            "project": t.string().optional(),
        }
    ).named(renames["RestoreBackupContextIn"])
    types["RestoreBackupContextOut"] = t.struct(
        {
            "backupRunId": t.string().optional(),
            "instanceId": t.string().optional(),
            "kind": t.string().optional(),
            "project": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreBackupContextOut"])
    types["FlagsListResponseIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["FlagIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["FlagsListResponseIn"])
    types["FlagsListResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["FlagOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FlagsListResponseOut"])
    types["AclEntryIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "expirationTime": t.string().optional(),
            "value": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["AclEntryIn"])
    types["AclEntryOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "expirationTime": t.string().optional(),
            "value": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AclEntryOut"])
    types["OperationsListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["OperationsListResponseIn"])
    types["OperationsListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationsListResponseOut"])
    types["SettingsIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "availabilityType": t.string().optional(),
            "sqlServerAuditConfig": t.proxy(
                renames["SqlServerAuditConfigIn"]
            ).optional(),
            "backupConfiguration": t.proxy(renames["BackupConfigurationIn"]).optional(),
            "connectorEnforcement": t.string().optional(),
            "tier": t.string().optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowIn"]).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "settingsVersion": t.string().optional(),
            "crashSafeReplicationEnabled": t.boolean().optional(),
            "timeZone": t.string().optional(),
            "dataDiskSizeGb": t.string().optional(),
            "passwordValidationPolicy": t.proxy(
                renames["PasswordValidationPolicyIn"]
            ).optional(),
            "insightsConfig": t.proxy(renames["InsightsConfigIn"]).optional(),
            "databaseFlags": t.array(t.proxy(renames["DatabaseFlagsIn"])).optional(),
            "activeDirectoryConfig": t.proxy(
                renames["SqlActiveDirectoryConfigIn"]
            ).optional(),
            "deletionProtectionEnabled": t.boolean().optional(),
            "databaseReplicationEnabled": t.boolean().optional(),
            "storageAutoResize": t.boolean().optional(),
            "locationPreference": t.proxy(renames["LocationPreferenceIn"]).optional(),
            "advancedMachineFeatures": t.proxy(
                renames["AdvancedMachineFeaturesIn"]
            ).optional(),
            "activationPolicy": t.string().optional(),
            "pricingPlan": t.string().optional(),
            "storageAutoResizeLimit": t.string().optional(),
            "replicationType": t.string().optional(),
            "collation": t.string().optional(),
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodIn"])
            ).optional(),
            "ipConfiguration": t.proxy(renames["IpConfigurationIn"]).optional(),
            "dataDiskType": t.string().optional(),
            "authorizedGaeApplications": t.array(t.string()).optional(),
        }
    ).named(renames["SettingsIn"])
    types["SettingsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "availabilityType": t.string().optional(),
            "sqlServerAuditConfig": t.proxy(
                renames["SqlServerAuditConfigOut"]
            ).optional(),
            "backupConfiguration": t.proxy(
                renames["BackupConfigurationOut"]
            ).optional(),
            "connectorEnforcement": t.string().optional(),
            "tier": t.string().optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowOut"]).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "settingsVersion": t.string().optional(),
            "crashSafeReplicationEnabled": t.boolean().optional(),
            "timeZone": t.string().optional(),
            "dataDiskSizeGb": t.string().optional(),
            "passwordValidationPolicy": t.proxy(
                renames["PasswordValidationPolicyOut"]
            ).optional(),
            "insightsConfig": t.proxy(renames["InsightsConfigOut"]).optional(),
            "databaseFlags": t.array(t.proxy(renames["DatabaseFlagsOut"])).optional(),
            "activeDirectoryConfig": t.proxy(
                renames["SqlActiveDirectoryConfigOut"]
            ).optional(),
            "deletionProtectionEnabled": t.boolean().optional(),
            "databaseReplicationEnabled": t.boolean().optional(),
            "storageAutoResize": t.boolean().optional(),
            "locationPreference": t.proxy(renames["LocationPreferenceOut"]).optional(),
            "advancedMachineFeatures": t.proxy(
                renames["AdvancedMachineFeaturesOut"]
            ).optional(),
            "activationPolicy": t.string().optional(),
            "pricingPlan": t.string().optional(),
            "storageAutoResizeLimit": t.string().optional(),
            "replicationType": t.string().optional(),
            "collation": t.string().optional(),
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodOut"])
            ).optional(),
            "ipConfiguration": t.proxy(renames["IpConfigurationOut"]).optional(),
            "dataDiskType": t.string().optional(),
            "authorizedGaeApplications": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettingsOut"])
    types["SqlInstancesVerifyExternalSyncSettingsRequestIn"] = t.struct(
        {
            "verifyConnectionOnly": t.boolean().optional(),
            "mysqlSyncConfig": t.proxy(renames["MySqlSyncConfigIn"]).optional(),
            "verifyReplicationOnly": t.boolean().optional(),
            "syncMode": t.string().optional(),
        }
    ).named(renames["SqlInstancesVerifyExternalSyncSettingsRequestIn"])
    types["SqlInstancesVerifyExternalSyncSettingsRequestOut"] = t.struct(
        {
            "verifyConnectionOnly": t.boolean().optional(),
            "mysqlSyncConfig": t.proxy(renames["MySqlSyncConfigOut"]).optional(),
            "verifyReplicationOnly": t.boolean().optional(),
            "syncMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlInstancesVerifyExternalSyncSettingsRequestOut"])
    types["DatabaseInstanceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "onPremisesConfiguration": t.proxy(
                renames["OnPremisesConfigurationIn"]
            ).optional(),
            "instanceType": t.string().optional(),
            "region": t.string().optional(),
            "kind": t.string().optional(),
            "masterInstanceName": t.string().optional(),
            "gceZone": t.string().optional(),
            "ipv6Address": t.string().optional(),
            "serverCaCert": t.proxy(renames["SslCertIn"]).optional(),
            "settings": t.proxy(renames["SettingsIn"]).optional(),
            "diskEncryptionStatus": t.proxy(
                renames["DiskEncryptionStatusIn"]
            ).optional(),
            "suspensionReason": t.array(t.string()).optional(),
            "secondaryGceZone": t.string().optional(),
            "databaseVersion": t.string().optional(),
            "state": t.string().optional(),
            "project": t.string().optional(),
            "ipAddresses": t.array(t.proxy(renames["IpMappingIn"])).optional(),
            "satisfiesPzs": t.boolean().optional(),
            "scheduledMaintenance": t.proxy(
                renames["SqlScheduledMaintenanceIn"]
            ).optional(),
            "rootPassword": t.string().optional(),
            "failoverReplica": t.struct(
                {"name": t.string().optional(), "available": t.boolean().optional()}
            ).optional(),
            "maintenanceVersion": t.string().optional(),
            "outOfDiskReport": t.proxy(renames["SqlOutOfDiskReportIn"]).optional(),
            "currentDiskSize": t.string().optional(),
            "selfLink": t.string().optional(),
            "diskEncryptionConfiguration": t.proxy(
                renames["DiskEncryptionConfigurationIn"]
            ).optional(),
            "replicaNames": t.array(t.string()).optional(),
            "serviceAccountEmailAddress": t.string().optional(),
            "maxDiskSize": t.string().optional(),
            "connectionName": t.string().optional(),
            "backendType": t.string().optional(),
            "replicaConfiguration": t.proxy(
                renames["ReplicaConfigurationIn"]
            ).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["DatabaseInstanceIn"])
    types["DatabaseInstanceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "onPremisesConfiguration": t.proxy(
                renames["OnPremisesConfigurationOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "instanceType": t.string().optional(),
            "availableMaintenanceVersions": t.array(t.string()).optional(),
            "region": t.string().optional(),
            "databaseInstalledVersion": t.string().optional(),
            "kind": t.string().optional(),
            "masterInstanceName": t.string().optional(),
            "gceZone": t.string().optional(),
            "ipv6Address": t.string().optional(),
            "serverCaCert": t.proxy(renames["SslCertOut"]).optional(),
            "settings": t.proxy(renames["SettingsOut"]).optional(),
            "diskEncryptionStatus": t.proxy(
                renames["DiskEncryptionStatusOut"]
            ).optional(),
            "suspensionReason": t.array(t.string()).optional(),
            "secondaryGceZone": t.string().optional(),
            "databaseVersion": t.string().optional(),
            "state": t.string().optional(),
            "project": t.string().optional(),
            "ipAddresses": t.array(t.proxy(renames["IpMappingOut"])).optional(),
            "satisfiesPzs": t.boolean().optional(),
            "scheduledMaintenance": t.proxy(
                renames["SqlScheduledMaintenanceOut"]
            ).optional(),
            "rootPassword": t.string().optional(),
            "failoverReplica": t.struct(
                {"name": t.string().optional(), "available": t.boolean().optional()}
            ).optional(),
            "maintenanceVersion": t.string().optional(),
            "outOfDiskReport": t.proxy(renames["SqlOutOfDiskReportOut"]).optional(),
            "currentDiskSize": t.string().optional(),
            "selfLink": t.string().optional(),
            "diskEncryptionConfiguration": t.proxy(
                renames["DiskEncryptionConfigurationOut"]
            ).optional(),
            "replicaNames": t.array(t.string()).optional(),
            "serviceAccountEmailAddress": t.string().optional(),
            "maxDiskSize": t.string().optional(),
            "connectionName": t.string().optional(),
            "backendType": t.string().optional(),
            "replicaConfiguration": t.proxy(
                renames["ReplicaConfigurationOut"]
            ).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseInstanceOut"])
    types["ExportContextIn"] = t.struct(
        {
            "uri": t.string().optional(),
            "fileType": t.string().optional(),
            "offload": t.boolean().optional(),
            "sqlExportOptions": t.struct(
                {
                    "tables": t.array(t.string()).optional(),
                    "mysqlExportOptions": t.struct(
                        {"masterData": t.integer().optional()}
                    ).optional(),
                    "schemaOnly": t.boolean().optional(),
                }
            ).optional(),
            "bakExportOptions": t.struct(
                {
                    "stripeCount": t.integer().optional(),
                    "striped": t.boolean().optional(),
                }
            ).optional(),
            "csvExportOptions": t.struct(
                {
                    "fieldsTerminatedBy": t.string().optional(),
                    "quoteCharacter": t.string().optional(),
                    "escapeCharacter": t.string().optional(),
                    "selectQuery": t.string().optional(),
                    "linesTerminatedBy": t.string().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "databases": t.array(t.string()).optional(),
        }
    ).named(renames["ExportContextIn"])
    types["ExportContextOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "fileType": t.string().optional(),
            "offload": t.boolean().optional(),
            "sqlExportOptions": t.struct(
                {
                    "tables": t.array(t.string()).optional(),
                    "mysqlExportOptions": t.struct(
                        {"masterData": t.integer().optional()}
                    ).optional(),
                    "schemaOnly": t.boolean().optional(),
                }
            ).optional(),
            "bakExportOptions": t.struct(
                {
                    "stripeCount": t.integer().optional(),
                    "striped": t.boolean().optional(),
                }
            ).optional(),
            "csvExportOptions": t.struct(
                {
                    "fieldsTerminatedBy": t.string().optional(),
                    "quoteCharacter": t.string().optional(),
                    "escapeCharacter": t.string().optional(),
                    "selectQuery": t.string().optional(),
                    "linesTerminatedBy": t.string().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "databases": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportContextOut"])
    types["OperationErrorIn"] = t.struct(
        {
            "code": t.string().optional(),
            "kind": t.string().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["OperationErrorIn"])
    types["OperationErrorOut"] = t.struct(
        {
            "code": t.string().optional(),
            "kind": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationErrorOut"])
    types["TruncateLogContextIn"] = t.struct(
        {"kind": t.string().optional(), "logType": t.string().optional()}
    ).named(renames["TruncateLogContextIn"])
    types["TruncateLogContextOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "logType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TruncateLogContextOut"])
    types["SqlInstancesGetDiskShrinkConfigResponseIn"] = t.struct(
        {
            "minimalTargetSizeGb": t.string().optional(),
            "kind": t.string().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["SqlInstancesGetDiskShrinkConfigResponseIn"])
    types["SqlInstancesGetDiskShrinkConfigResponseOut"] = t.struct(
        {
            "minimalTargetSizeGb": t.string().optional(),
            "kind": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlInstancesGetDiskShrinkConfigResponseOut"])

    functions = {}
    functions["backupRunsList"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/backupRuns/{id}",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BackupRunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["backupRunsDelete"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/backupRuns/{id}",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BackupRunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["backupRunsInsert"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/backupRuns/{id}",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BackupRunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["backupRunsGet"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/backupRuns/{id}",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BackupRunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["flagsList"] = sqladmin.get(
        "v1/flags",
        t.struct(
            {"databaseVersion": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["FlagsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["databasesDelete"] = sqladmin.patch(
        "v1/projects/{project}/instances/{instance}/databases/{database}",
        t.struct(
            {
                "database": t.string().optional(),
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "charset": t.string().optional(),
                "etag": t.string().optional(),
                "sqlserverDatabaseDetails": t.proxy(
                    renames["SqlServerDatabaseDetailsIn"]
                ),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "collation": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["databasesList"] = sqladmin.patch(
        "v1/projects/{project}/instances/{instance}/databases/{database}",
        t.struct(
            {
                "database": t.string().optional(),
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "charset": t.string().optional(),
                "etag": t.string().optional(),
                "sqlserverDatabaseDetails": t.proxy(
                    renames["SqlServerDatabaseDetailsIn"]
                ),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "collation": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["databasesUpdate"] = sqladmin.patch(
        "v1/projects/{project}/instances/{instance}/databases/{database}",
        t.struct(
            {
                "database": t.string().optional(),
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "charset": t.string().optional(),
                "etag": t.string().optional(),
                "sqlserverDatabaseDetails": t.proxy(
                    renames["SqlServerDatabaseDetailsIn"]
                ),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "collation": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["databasesInsert"] = sqladmin.patch(
        "v1/projects/{project}/instances/{instance}/databases/{database}",
        t.struct(
            {
                "database": t.string().optional(),
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "charset": t.string().optional(),
                "etag": t.string().optional(),
                "sqlserverDatabaseDetails": t.proxy(
                    renames["SqlServerDatabaseDetailsIn"]
                ),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "collation": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["databasesGet"] = sqladmin.patch(
        "v1/projects/{project}/instances/{instance}/databases/{database}",
        t.struct(
            {
                "database": t.string().optional(),
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "charset": t.string().optional(),
                "etag": t.string().optional(),
                "sqlserverDatabaseDetails": t.proxy(
                    renames["SqlServerDatabaseDetailsIn"]
                ),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "collation": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["databasesPatch"] = sqladmin.patch(
        "v1/projects/{project}/instances/{instance}/databases/{database}",
        t.struct(
            {
                "database": t.string().optional(),
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "charset": t.string().optional(),
                "etag": t.string().optional(),
                "sqlserverDatabaseDetails": t.proxy(
                    renames["SqlServerDatabaseDetailsIn"]
                ),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "collation": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sslCertsInsert"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}/sslCerts/{sha1Fingerprint}",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "sha1Fingerprint": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sslCertsList"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}/sslCerts/{sha1Fingerprint}",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "sha1Fingerprint": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sslCertsCreateEphemeral"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}/sslCerts/{sha1Fingerprint}",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "sha1Fingerprint": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sslCertsGet"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}/sslCerts/{sha1Fingerprint}",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "sha1Fingerprint": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sslCertsDelete"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}/sslCerts/{sha1Fingerprint}",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "sha1Fingerprint": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tiersList"] = sqladmin.get(
        "v1/projects/{project}/tiers",
        t.struct({"project": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["TiersListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesImport"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/stopReplica",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesDemoteMaster"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/stopReplica",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesAddServerCa"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/stopReplica",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesListServerCas"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/stopReplica",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesRestart"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/stopReplica",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesInsert"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/stopReplica",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesRestoreBackup"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/stopReplica",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesUpdate"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/stopReplica",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesPatch"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/stopReplica",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesStartReplica"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/stopReplica",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesFailover"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/stopReplica",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesResetSslConfig"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/stopReplica",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesDelete"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/stopReplica",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesGet"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/stopReplica",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesRotateServerCa"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/stopReplica",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesClone"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/stopReplica",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesTruncateLog"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/stopReplica",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesPromoteReplica"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/stopReplica",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesList"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/stopReplica",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesExport"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/stopReplica",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesStopReplica"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/stopReplica",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesVerifyExternalSyncSettings"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/performDiskShrink",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "targetSizeGb": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesStartExternalSync"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/performDiskShrink",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "targetSizeGb": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesRescheduleMaintenance"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/performDiskShrink",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "targetSizeGb": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesGetDiskShrinkConfig"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/performDiskShrink",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "targetSizeGb": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesResetReplicaSize"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/performDiskShrink",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "targetSizeGb": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesPerformDiskShrink"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/performDiskShrink",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "targetSizeGb": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDelete"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/users",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "name": t.string().optional(),
                "kind": t.string().optional(),
                "sqlserverUserDetails": t.proxy(renames["SqlServerUserDetailsIn"]),
                "etag": t.string().optional(),
                "host": t.string().optional(),
                "type": t.string().optional(),
                "passwordPolicy": t.proxy(
                    renames["UserPasswordValidationPolicyIn"]
                ).optional(),
                "password": t.string().optional(),
                "dualPasswordType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersGet"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/users",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "name": t.string().optional(),
                "kind": t.string().optional(),
                "sqlserverUserDetails": t.proxy(renames["SqlServerUserDetailsIn"]),
                "etag": t.string().optional(),
                "host": t.string().optional(),
                "type": t.string().optional(),
                "passwordPolicy": t.proxy(
                    renames["UserPasswordValidationPolicyIn"]
                ).optional(),
                "password": t.string().optional(),
                "dualPasswordType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersList"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/users",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "name": t.string().optional(),
                "kind": t.string().optional(),
                "sqlserverUserDetails": t.proxy(renames["SqlServerUserDetailsIn"]),
                "etag": t.string().optional(),
                "host": t.string().optional(),
                "type": t.string().optional(),
                "passwordPolicy": t.proxy(
                    renames["UserPasswordValidationPolicyIn"]
                ).optional(),
                "password": t.string().optional(),
                "dualPasswordType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersUpdate"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/users",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "name": t.string().optional(),
                "kind": t.string().optional(),
                "sqlserverUserDetails": t.proxy(renames["SqlServerUserDetailsIn"]),
                "etag": t.string().optional(),
                "host": t.string().optional(),
                "type": t.string().optional(),
                "passwordPolicy": t.proxy(
                    renames["UserPasswordValidationPolicyIn"]
                ).optional(),
                "password": t.string().optional(),
                "dualPasswordType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersInsert"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/users",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "name": t.string().optional(),
                "kind": t.string().optional(),
                "sqlserverUserDetails": t.proxy(renames["SqlServerUserDetailsIn"]),
                "etag": t.string().optional(),
                "host": t.string().optional(),
                "type": t.string().optional(),
                "passwordPolicy": t.proxy(
                    renames["UserPasswordValidationPolicyIn"]
                ).optional(),
                "password": t.string().optional(),
                "dualPasswordType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["connectGet"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}:generateEphemeralCert",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "access_token": t.string().optional(),
                "validDuration": t.string().optional(),
                "public_key": t.string().optional(),
                "readTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateEphemeralCertResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["connectGenerateEphemeralCert"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}:generateEphemeralCert",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "access_token": t.string().optional(),
                "validDuration": t.string().optional(),
                "public_key": t.string().optional(),
                "readTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateEphemeralCertResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = sqladmin.get(
        "v1/projects/{project}/operations",
        t.struct(
            {
                "instance": t.string().optional(),
                "maxResults": t.integer().optional(),
                "project": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsList"] = sqladmin.get(
        "v1/projects/{project}/operations",
        t.struct(
            {
                "instance": t.string().optional(),
                "maxResults": t.integer().optional(),
                "project": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="sqladmin", renames=renames, types=Box(types), functions=Box(functions)
    )
