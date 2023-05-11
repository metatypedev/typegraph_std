from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_sqladmin() -> Import:
    sqladmin = HTTPRuntime("https://sqladmin.googleapis.com/")

    renames = {
        "ErrorResponse": "_sqladmin_1_ErrorResponse",
        "InstancesDemoteMasterRequestIn": "_sqladmin_2_InstancesDemoteMasterRequestIn",
        "InstancesDemoteMasterRequestOut": "_sqladmin_3_InstancesDemoteMasterRequestOut",
        "UserPasswordValidationPolicyIn": "_sqladmin_4_UserPasswordValidationPolicyIn",
        "UserPasswordValidationPolicyOut": "_sqladmin_5_UserPasswordValidationPolicyOut",
        "DatabaseIn": "_sqladmin_6_DatabaseIn",
        "DatabaseOut": "_sqladmin_7_DatabaseOut",
        "TiersListResponseIn": "_sqladmin_8_TiersListResponseIn",
        "TiersListResponseOut": "_sqladmin_9_TiersListResponseOut",
        "RescheduleIn": "_sqladmin_10_RescheduleIn",
        "RescheduleOut": "_sqladmin_11_RescheduleOut",
        "GenerateEphemeralCertRequestIn": "_sqladmin_12_GenerateEphemeralCertRequestIn",
        "GenerateEphemeralCertRequestOut": "_sqladmin_13_GenerateEphemeralCertRequestOut",
        "SqlInstancesVerifyExternalSyncSettingsRequestIn": "_sqladmin_14_SqlInstancesVerifyExternalSyncSettingsRequestIn",
        "SqlInstancesVerifyExternalSyncSettingsRequestOut": "_sqladmin_15_SqlInstancesVerifyExternalSyncSettingsRequestOut",
        "TierIn": "_sqladmin_16_TierIn",
        "TierOut": "_sqladmin_17_TierOut",
        "InstancesListServerCasResponseIn": "_sqladmin_18_InstancesListServerCasResponseIn",
        "InstancesListServerCasResponseOut": "_sqladmin_19_InstancesListServerCasResponseOut",
        "PasswordStatusIn": "_sqladmin_20_PasswordStatusIn",
        "PasswordStatusOut": "_sqladmin_21_PasswordStatusOut",
        "SqlInstancesRescheduleMaintenanceRequestBodyIn": "_sqladmin_22_SqlInstancesRescheduleMaintenanceRequestBodyIn",
        "SqlInstancesRescheduleMaintenanceRequestBodyOut": "_sqladmin_23_SqlInstancesRescheduleMaintenanceRequestBodyOut",
        "ExportContextIn": "_sqladmin_24_ExportContextIn",
        "ExportContextOut": "_sqladmin_25_ExportContextOut",
        "PasswordValidationPolicyIn": "_sqladmin_26_PasswordValidationPolicyIn",
        "PasswordValidationPolicyOut": "_sqladmin_27_PasswordValidationPolicyOut",
        "InstancesRestoreBackupRequestIn": "_sqladmin_28_InstancesRestoreBackupRequestIn",
        "InstancesRestoreBackupRequestOut": "_sqladmin_29_InstancesRestoreBackupRequestOut",
        "LocationPreferenceIn": "_sqladmin_30_LocationPreferenceIn",
        "LocationPreferenceOut": "_sqladmin_31_LocationPreferenceOut",
        "InstancesImportRequestIn": "_sqladmin_32_InstancesImportRequestIn",
        "InstancesImportRequestOut": "_sqladmin_33_InstancesImportRequestOut",
        "SqlActiveDirectoryConfigIn": "_sqladmin_34_SqlActiveDirectoryConfigIn",
        "SqlActiveDirectoryConfigOut": "_sqladmin_35_SqlActiveDirectoryConfigOut",
        "InstancesListResponseIn": "_sqladmin_36_InstancesListResponseIn",
        "InstancesListResponseOut": "_sqladmin_37_InstancesListResponseOut",
        "MySqlSyncConfigIn": "_sqladmin_38_MySqlSyncConfigIn",
        "MySqlSyncConfigOut": "_sqladmin_39_MySqlSyncConfigOut",
        "DatabaseFlagsIn": "_sqladmin_40_DatabaseFlagsIn",
        "DatabaseFlagsOut": "_sqladmin_41_DatabaseFlagsOut",
        "SettingsIn": "_sqladmin_42_SettingsIn",
        "SettingsOut": "_sqladmin_43_SettingsOut",
        "SqlServerUserDetailsIn": "_sqladmin_44_SqlServerUserDetailsIn",
        "SqlServerUserDetailsOut": "_sqladmin_45_SqlServerUserDetailsOut",
        "ApiWarningIn": "_sqladmin_46_ApiWarningIn",
        "ApiWarningOut": "_sqladmin_47_ApiWarningOut",
        "SqlOutOfDiskReportIn": "_sqladmin_48_SqlOutOfDiskReportIn",
        "SqlOutOfDiskReportOut": "_sqladmin_49_SqlOutOfDiskReportOut",
        "SslCertIn": "_sqladmin_50_SslCertIn",
        "SslCertOut": "_sqladmin_51_SslCertOut",
        "UserIn": "_sqladmin_52_UserIn",
        "UserOut": "_sqladmin_53_UserOut",
        "SslCertsInsertRequestIn": "_sqladmin_54_SslCertsInsertRequestIn",
        "SslCertsInsertRequestOut": "_sqladmin_55_SslCertsInsertRequestOut",
        "SqlScheduledMaintenanceIn": "_sqladmin_56_SqlScheduledMaintenanceIn",
        "SqlScheduledMaintenanceOut": "_sqladmin_57_SqlScheduledMaintenanceOut",
        "DemoteMasterMySqlReplicaConfigurationIn": "_sqladmin_58_DemoteMasterMySqlReplicaConfigurationIn",
        "DemoteMasterMySqlReplicaConfigurationOut": "_sqladmin_59_DemoteMasterMySqlReplicaConfigurationOut",
        "GenerateEphemeralCertResponseIn": "_sqladmin_60_GenerateEphemeralCertResponseIn",
        "GenerateEphemeralCertResponseOut": "_sqladmin_61_GenerateEphemeralCertResponseOut",
        "AclEntryIn": "_sqladmin_62_AclEntryIn",
        "AclEntryOut": "_sqladmin_63_AclEntryOut",
        "DemoteMasterConfigurationIn": "_sqladmin_64_DemoteMasterConfigurationIn",
        "DemoteMasterConfigurationOut": "_sqladmin_65_DemoteMasterConfigurationOut",
        "PerformDiskShrinkContextIn": "_sqladmin_66_PerformDiskShrinkContextIn",
        "PerformDiskShrinkContextOut": "_sqladmin_67_PerformDiskShrinkContextOut",
        "DenyMaintenancePeriodIn": "_sqladmin_68_DenyMaintenancePeriodIn",
        "DenyMaintenancePeriodOut": "_sqladmin_69_DenyMaintenancePeriodOut",
        "SslCertsCreateEphemeralRequestIn": "_sqladmin_70_SslCertsCreateEphemeralRequestIn",
        "SslCertsCreateEphemeralRequestOut": "_sqladmin_71_SslCertsCreateEphemeralRequestOut",
        "OperationErrorIn": "_sqladmin_72_OperationErrorIn",
        "OperationErrorOut": "_sqladmin_73_OperationErrorOut",
        "BackupRetentionSettingsIn": "_sqladmin_74_BackupRetentionSettingsIn",
        "BackupRetentionSettingsOut": "_sqladmin_75_BackupRetentionSettingsOut",
        "MySqlReplicaConfigurationIn": "_sqladmin_76_MySqlReplicaConfigurationIn",
        "MySqlReplicaConfigurationOut": "_sqladmin_77_MySqlReplicaConfigurationOut",
        "DatabasesListResponseIn": "_sqladmin_78_DatabasesListResponseIn",
        "DatabasesListResponseOut": "_sqladmin_79_DatabasesListResponseOut",
        "OperationsListResponseIn": "_sqladmin_80_OperationsListResponseIn",
        "OperationsListResponseOut": "_sqladmin_81_OperationsListResponseOut",
        "BackupConfigurationIn": "_sqladmin_82_BackupConfigurationIn",
        "BackupConfigurationOut": "_sqladmin_83_BackupConfigurationOut",
        "SslCertsInsertResponseIn": "_sqladmin_84_SslCertsInsertResponseIn",
        "SslCertsInsertResponseOut": "_sqladmin_85_SslCertsInsertResponseOut",
        "OperationIn": "_sqladmin_86_OperationIn",
        "OperationOut": "_sqladmin_87_OperationOut",
        "MaintenanceWindowIn": "_sqladmin_88_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_sqladmin_89_MaintenanceWindowOut",
        "InstancesTruncateLogRequestIn": "_sqladmin_90_InstancesTruncateLogRequestIn",
        "InstancesTruncateLogRequestOut": "_sqladmin_91_InstancesTruncateLogRequestOut",
        "InstancesFailoverRequestIn": "_sqladmin_92_InstancesFailoverRequestIn",
        "InstancesFailoverRequestOut": "_sqladmin_93_InstancesFailoverRequestOut",
        "SqlInstancesResetReplicaSizeRequestIn": "_sqladmin_94_SqlInstancesResetReplicaSizeRequestIn",
        "SqlInstancesResetReplicaSizeRequestOut": "_sqladmin_95_SqlInstancesResetReplicaSizeRequestOut",
        "SyncFlagsIn": "_sqladmin_96_SyncFlagsIn",
        "SyncFlagsOut": "_sqladmin_97_SyncFlagsOut",
        "SqlInstancesStartExternalSyncRequestIn": "_sqladmin_98_SqlInstancesStartExternalSyncRequestIn",
        "SqlInstancesStartExternalSyncRequestOut": "_sqladmin_99_SqlInstancesStartExternalSyncRequestOut",
        "BackupRunsListResponseIn": "_sqladmin_100_BackupRunsListResponseIn",
        "BackupRunsListResponseOut": "_sqladmin_101_BackupRunsListResponseOut",
        "UsersListResponseIn": "_sqladmin_102_UsersListResponseIn",
        "UsersListResponseOut": "_sqladmin_103_UsersListResponseOut",
        "SqlExternalSyncSettingErrorIn": "_sqladmin_104_SqlExternalSyncSettingErrorIn",
        "SqlExternalSyncSettingErrorOut": "_sqladmin_105_SqlExternalSyncSettingErrorOut",
        "InsightsConfigIn": "_sqladmin_106_InsightsConfigIn",
        "InsightsConfigOut": "_sqladmin_107_InsightsConfigOut",
        "InstanceReferenceIn": "_sqladmin_108_InstanceReferenceIn",
        "InstanceReferenceOut": "_sqladmin_109_InstanceReferenceOut",
        "AdvancedMachineFeaturesIn": "_sqladmin_110_AdvancedMachineFeaturesIn",
        "AdvancedMachineFeaturesOut": "_sqladmin_111_AdvancedMachineFeaturesOut",
        "SqlServerAuditConfigIn": "_sqladmin_112_SqlServerAuditConfigIn",
        "SqlServerAuditConfigOut": "_sqladmin_113_SqlServerAuditConfigOut",
        "BackupContextIn": "_sqladmin_114_BackupContextIn",
        "BackupContextOut": "_sqladmin_115_BackupContextOut",
        "DemoteMasterContextIn": "_sqladmin_116_DemoteMasterContextIn",
        "DemoteMasterContextOut": "_sqladmin_117_DemoteMasterContextOut",
        "SqlInstancesGetDiskShrinkConfigResponseIn": "_sqladmin_118_SqlInstancesGetDiskShrinkConfigResponseIn",
        "SqlInstancesGetDiskShrinkConfigResponseOut": "_sqladmin_119_SqlInstancesGetDiskShrinkConfigResponseOut",
        "IpMappingIn": "_sqladmin_120_IpMappingIn",
        "IpMappingOut": "_sqladmin_121_IpMappingOut",
        "SqlInstancesVerifyExternalSyncSettingsResponseIn": "_sqladmin_122_SqlInstancesVerifyExternalSyncSettingsResponseIn",
        "SqlInstancesVerifyExternalSyncSettingsResponseOut": "_sqladmin_123_SqlInstancesVerifyExternalSyncSettingsResponseOut",
        "RotateServerCaContextIn": "_sqladmin_124_RotateServerCaContextIn",
        "RotateServerCaContextOut": "_sqladmin_125_RotateServerCaContextOut",
        "OperationErrorsIn": "_sqladmin_126_OperationErrorsIn",
        "OperationErrorsOut": "_sqladmin_127_OperationErrorsOut",
        "OnPremisesConfigurationIn": "_sqladmin_128_OnPremisesConfigurationIn",
        "OnPremisesConfigurationOut": "_sqladmin_129_OnPremisesConfigurationOut",
        "SslCertDetailIn": "_sqladmin_130_SslCertDetailIn",
        "SslCertDetailOut": "_sqladmin_131_SslCertDetailOut",
        "RestoreBackupContextIn": "_sqladmin_132_RestoreBackupContextIn",
        "RestoreBackupContextOut": "_sqladmin_133_RestoreBackupContextOut",
        "InstancesExportRequestIn": "_sqladmin_134_InstancesExportRequestIn",
        "InstancesExportRequestOut": "_sqladmin_135_InstancesExportRequestOut",
        "BackupRunIn": "_sqladmin_136_BackupRunIn",
        "BackupRunOut": "_sqladmin_137_BackupRunOut",
        "InstancesCloneRequestIn": "_sqladmin_138_InstancesCloneRequestIn",
        "InstancesCloneRequestOut": "_sqladmin_139_InstancesCloneRequestOut",
        "BinLogCoordinatesIn": "_sqladmin_140_BinLogCoordinatesIn",
        "BinLogCoordinatesOut": "_sqladmin_141_BinLogCoordinatesOut",
        "SqlServerDatabaseDetailsIn": "_sqladmin_142_SqlServerDatabaseDetailsIn",
        "SqlServerDatabaseDetailsOut": "_sqladmin_143_SqlServerDatabaseDetailsOut",
        "SslCertsListResponseIn": "_sqladmin_144_SslCertsListResponseIn",
        "SslCertsListResponseOut": "_sqladmin_145_SslCertsListResponseOut",
        "ImportContextIn": "_sqladmin_146_ImportContextIn",
        "ImportContextOut": "_sqladmin_147_ImportContextOut",
        "FlagsListResponseIn": "_sqladmin_148_FlagsListResponseIn",
        "FlagsListResponseOut": "_sqladmin_149_FlagsListResponseOut",
        "FlagIn": "_sqladmin_150_FlagIn",
        "FlagOut": "_sqladmin_151_FlagOut",
        "IpConfigurationIn": "_sqladmin_152_IpConfigurationIn",
        "IpConfigurationOut": "_sqladmin_153_IpConfigurationOut",
        "CloneContextIn": "_sqladmin_154_CloneContextIn",
        "CloneContextOut": "_sqladmin_155_CloneContextOut",
        "FailoverContextIn": "_sqladmin_156_FailoverContextIn",
        "FailoverContextOut": "_sqladmin_157_FailoverContextOut",
        "InstancesRotateServerCaRequestIn": "_sqladmin_158_InstancesRotateServerCaRequestIn",
        "InstancesRotateServerCaRequestOut": "_sqladmin_159_InstancesRotateServerCaRequestOut",
        "OperationMetadataIn": "_sqladmin_160_OperationMetadataIn",
        "OperationMetadataOut": "_sqladmin_161_OperationMetadataOut",
        "ReplicaConfigurationIn": "_sqladmin_162_ReplicaConfigurationIn",
        "ReplicaConfigurationOut": "_sqladmin_163_ReplicaConfigurationOut",
        "DiskEncryptionStatusIn": "_sqladmin_164_DiskEncryptionStatusIn",
        "DiskEncryptionStatusOut": "_sqladmin_165_DiskEncryptionStatusOut",
        "DiskEncryptionConfigurationIn": "_sqladmin_166_DiskEncryptionConfigurationIn",
        "DiskEncryptionConfigurationOut": "_sqladmin_167_DiskEncryptionConfigurationOut",
        "DatabaseInstanceIn": "_sqladmin_168_DatabaseInstanceIn",
        "DatabaseInstanceOut": "_sqladmin_169_DatabaseInstanceOut",
        "TruncateLogContextIn": "_sqladmin_170_TruncateLogContextIn",
        "TruncateLogContextOut": "_sqladmin_171_TruncateLogContextOut",
        "ConnectSettingsIn": "_sqladmin_172_ConnectSettingsIn",
        "ConnectSettingsOut": "_sqladmin_173_ConnectSettingsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["UserPasswordValidationPolicyIn"] = t.struct(
        {
            "enableFailedAttemptsCheck": t.boolean().optional(),
            "passwordExpirationDuration": t.string().optional(),
            "allowedFailedAttempts": t.integer().optional(),
            "enablePasswordVerification": t.boolean().optional(),
        }
    ).named(renames["UserPasswordValidationPolicyIn"])
    types["UserPasswordValidationPolicyOut"] = t.struct(
        {
            "enableFailedAttemptsCheck": t.boolean().optional(),
            "passwordExpirationDuration": t.string().optional(),
            "status": t.proxy(renames["PasswordStatusOut"]).optional(),
            "allowedFailedAttempts": t.integer().optional(),
            "enablePasswordVerification": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserPasswordValidationPolicyOut"])
    types["DatabaseIn"] = t.struct(
        {
            "sqlserverDatabaseDetails": t.proxy(renames["SqlServerDatabaseDetailsIn"]),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "charset": t.string().optional(),
            "project": t.string().optional(),
            "collation": t.string().optional(),
            "instance": t.string().optional(),
            "etag": t.string().optional(),
            "selfLink": t.string().optional(),
        }
    ).named(renames["DatabaseIn"])
    types["DatabaseOut"] = t.struct(
        {
            "sqlserverDatabaseDetails": t.proxy(renames["SqlServerDatabaseDetailsOut"]),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "charset": t.string().optional(),
            "project": t.string().optional(),
            "collation": t.string().optional(),
            "instance": t.string().optional(),
            "etag": t.string().optional(),
            "selfLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseOut"])
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
    types["GenerateEphemeralCertRequestIn"] = t.struct(
        {
            "public_key": t.string().optional(),
            "validDuration": t.string().optional(),
            "access_token": t.string().optional(),
            "readTime": t.string().optional(),
        }
    ).named(renames["GenerateEphemeralCertRequestIn"])
    types["GenerateEphemeralCertRequestOut"] = t.struct(
        {
            "public_key": t.string().optional(),
            "validDuration": t.string().optional(),
            "access_token": t.string().optional(),
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateEphemeralCertRequestOut"])
    types["SqlInstancesVerifyExternalSyncSettingsRequestIn"] = t.struct(
        {
            "mysqlSyncConfig": t.proxy(renames["MySqlSyncConfigIn"]).optional(),
            "verifyConnectionOnly": t.boolean().optional(),
            "verifyReplicationOnly": t.boolean().optional(),
            "syncMode": t.string().optional(),
        }
    ).named(renames["SqlInstancesVerifyExternalSyncSettingsRequestIn"])
    types["SqlInstancesVerifyExternalSyncSettingsRequestOut"] = t.struct(
        {
            "mysqlSyncConfig": t.proxy(renames["MySqlSyncConfigOut"]).optional(),
            "verifyConnectionOnly": t.boolean().optional(),
            "verifyReplicationOnly": t.boolean().optional(),
            "syncMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlInstancesVerifyExternalSyncSettingsRequestOut"])
    types["TierIn"] = t.struct(
        {
            "DiskQuota": t.string().optional(),
            "region": t.array(t.string()).optional(),
            "tier": t.string().optional(),
            "kind": t.string().optional(),
            "RAM": t.string().optional(),
        }
    ).named(renames["TierIn"])
    types["TierOut"] = t.struct(
        {
            "DiskQuota": t.string().optional(),
            "region": t.array(t.string()).optional(),
            "tier": t.string().optional(),
            "kind": t.string().optional(),
            "RAM": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TierOut"])
    types["InstancesListServerCasResponseIn"] = t.struct(
        {
            "activeVersion": t.string(),
            "kind": t.string().optional(),
            "certs": t.array(t.proxy(renames["SslCertIn"])).optional(),
        }
    ).named(renames["InstancesListServerCasResponseIn"])
    types["InstancesListServerCasResponseOut"] = t.struct(
        {
            "activeVersion": t.string(),
            "kind": t.string().optional(),
            "certs": t.array(t.proxy(renames["SslCertOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesListServerCasResponseOut"])
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
    types["SqlInstancesRescheduleMaintenanceRequestBodyIn"] = t.struct(
        {"reschedule": t.proxy(renames["RescheduleIn"])}
    ).named(renames["SqlInstancesRescheduleMaintenanceRequestBodyIn"])
    types["SqlInstancesRescheduleMaintenanceRequestBodyOut"] = t.struct(
        {
            "reschedule": t.proxy(renames["RescheduleOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlInstancesRescheduleMaintenanceRequestBodyOut"])
    types["ExportContextIn"] = t.struct(
        {
            "offload": t.boolean().optional(),
            "kind": t.string().optional(),
            "fileType": t.string().optional(),
            "sqlExportOptions": t.struct(
                {
                    "schemaOnly": t.boolean().optional(),
                    "tables": t.array(t.string()).optional(),
                    "mysqlExportOptions": t.struct(
                        {"masterData": t.integer().optional()}
                    ).optional(),
                }
            ).optional(),
            "uri": t.string().optional(),
            "bakExportOptions": t.struct(
                {
                    "stripeCount": t.integer().optional(),
                    "striped": t.boolean().optional(),
                }
            ).optional(),
            "databases": t.array(t.string()).optional(),
            "csvExportOptions": t.struct(
                {
                    "linesTerminatedBy": t.string().optional(),
                    "quoteCharacter": t.string().optional(),
                    "escapeCharacter": t.string().optional(),
                    "selectQuery": t.string().optional(),
                    "fieldsTerminatedBy": t.string().optional(),
                }
            ).optional(),
        }
    ).named(renames["ExportContextIn"])
    types["ExportContextOut"] = t.struct(
        {
            "offload": t.boolean().optional(),
            "kind": t.string().optional(),
            "fileType": t.string().optional(),
            "sqlExportOptions": t.struct(
                {
                    "schemaOnly": t.boolean().optional(),
                    "tables": t.array(t.string()).optional(),
                    "mysqlExportOptions": t.struct(
                        {"masterData": t.integer().optional()}
                    ).optional(),
                }
            ).optional(),
            "uri": t.string().optional(),
            "bakExportOptions": t.struct(
                {
                    "stripeCount": t.integer().optional(),
                    "striped": t.boolean().optional(),
                }
            ).optional(),
            "databases": t.array(t.string()).optional(),
            "csvExportOptions": t.struct(
                {
                    "linesTerminatedBy": t.string().optional(),
                    "quoteCharacter": t.string().optional(),
                    "escapeCharacter": t.string().optional(),
                    "selectQuery": t.string().optional(),
                    "fieldsTerminatedBy": t.string().optional(),
                }
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportContextOut"])
    types["PasswordValidationPolicyIn"] = t.struct(
        {
            "minLength": t.integer().optional(),
            "enablePasswordPolicy": t.boolean().optional(),
            "passwordChangeInterval": t.string().optional(),
            "complexity": t.string().optional(),
            "reuseInterval": t.integer().optional(),
            "disallowUsernameSubstring": t.boolean().optional(),
        }
    ).named(renames["PasswordValidationPolicyIn"])
    types["PasswordValidationPolicyOut"] = t.struct(
        {
            "minLength": t.integer().optional(),
            "enablePasswordPolicy": t.boolean().optional(),
            "passwordChangeInterval": t.string().optional(),
            "complexity": t.string().optional(),
            "reuseInterval": t.integer().optional(),
            "disallowUsernameSubstring": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PasswordValidationPolicyOut"])
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
    types["LocationPreferenceIn"] = t.struct(
        {
            "followGaeApplication": t.string().optional(),
            "zone": t.string().optional(),
            "secondaryZone": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["LocationPreferenceIn"])
    types["LocationPreferenceOut"] = t.struct(
        {
            "followGaeApplication": t.string().optional(),
            "zone": t.string().optional(),
            "secondaryZone": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationPreferenceOut"])
    types["InstancesImportRequestIn"] = t.struct(
        {"importContext": t.proxy(renames["ImportContextIn"]).optional()}
    ).named(renames["InstancesImportRequestIn"])
    types["InstancesImportRequestOut"] = t.struct(
        {
            "importContext": t.proxy(renames["ImportContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesImportRequestOut"])
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
    types["InstancesListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["DatabaseInstanceIn"])).optional(),
            "warnings": t.array(t.proxy(renames["ApiWarningIn"])).optional(),
        }
    ).named(renames["InstancesListResponseIn"])
    types["InstancesListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["DatabaseInstanceOut"])).optional(),
            "warnings": t.array(t.proxy(renames["ApiWarningOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesListResponseOut"])
    types["MySqlSyncConfigIn"] = t.struct(
        {"initialSyncFlags": t.array(t.proxy(renames["SyncFlagsIn"])).optional()}
    ).named(renames["MySqlSyncConfigIn"])
    types["MySqlSyncConfigOut"] = t.struct(
        {
            "initialSyncFlags": t.array(t.proxy(renames["SyncFlagsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MySqlSyncConfigOut"])
    types["DatabaseFlagsIn"] = t.struct(
        {"value": t.string().optional(), "name": t.string().optional()}
    ).named(renames["DatabaseFlagsIn"])
    types["DatabaseFlagsOut"] = t.struct(
        {
            "value": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseFlagsOut"])
    types["SettingsIn"] = t.struct(
        {
            "pricingPlan": t.string().optional(),
            "dataDiskType": t.string().optional(),
            "timeZone": t.string().optional(),
            "activationPolicy": t.string().optional(),
            "backupConfiguration": t.proxy(renames["BackupConfigurationIn"]).optional(),
            "collation": t.string().optional(),
            "insightsConfig": t.proxy(renames["InsightsConfigIn"]).optional(),
            "settingsVersion": t.string().optional(),
            "deletionProtectionEnabled": t.boolean().optional(),
            "passwordValidationPolicy": t.proxy(
                renames["PasswordValidationPolicyIn"]
            ).optional(),
            "locationPreference": t.proxy(renames["LocationPreferenceIn"]).optional(),
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodIn"])
            ).optional(),
            "authorizedGaeApplications": t.array(t.string()).optional(),
            "dataDiskSizeGb": t.string().optional(),
            "connectorEnforcement": t.string().optional(),
            "storageAutoResize": t.boolean().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "replicationType": t.string().optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowIn"]).optional(),
            "kind": t.string().optional(),
            "ipConfiguration": t.proxy(renames["IpConfigurationIn"]).optional(),
            "crashSafeReplicationEnabled": t.boolean().optional(),
            "databaseFlags": t.array(t.proxy(renames["DatabaseFlagsIn"])).optional(),
            "advancedMachineFeatures": t.proxy(
                renames["AdvancedMachineFeaturesIn"]
            ).optional(),
            "activeDirectoryConfig": t.proxy(
                renames["SqlActiveDirectoryConfigIn"]
            ).optional(),
            "storageAutoResizeLimit": t.string().optional(),
            "tier": t.string().optional(),
            "databaseReplicationEnabled": t.boolean().optional(),
            "sqlServerAuditConfig": t.proxy(
                renames["SqlServerAuditConfigIn"]
            ).optional(),
            "availabilityType": t.string().optional(),
        }
    ).named(renames["SettingsIn"])
    types["SettingsOut"] = t.struct(
        {
            "pricingPlan": t.string().optional(),
            "dataDiskType": t.string().optional(),
            "timeZone": t.string().optional(),
            "activationPolicy": t.string().optional(),
            "backupConfiguration": t.proxy(
                renames["BackupConfigurationOut"]
            ).optional(),
            "collation": t.string().optional(),
            "insightsConfig": t.proxy(renames["InsightsConfigOut"]).optional(),
            "settingsVersion": t.string().optional(),
            "deletionProtectionEnabled": t.boolean().optional(),
            "passwordValidationPolicy": t.proxy(
                renames["PasswordValidationPolicyOut"]
            ).optional(),
            "locationPreference": t.proxy(renames["LocationPreferenceOut"]).optional(),
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodOut"])
            ).optional(),
            "authorizedGaeApplications": t.array(t.string()).optional(),
            "dataDiskSizeGb": t.string().optional(),
            "connectorEnforcement": t.string().optional(),
            "storageAutoResize": t.boolean().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "replicationType": t.string().optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowOut"]).optional(),
            "kind": t.string().optional(),
            "ipConfiguration": t.proxy(renames["IpConfigurationOut"]).optional(),
            "crashSafeReplicationEnabled": t.boolean().optional(),
            "databaseFlags": t.array(t.proxy(renames["DatabaseFlagsOut"])).optional(),
            "advancedMachineFeatures": t.proxy(
                renames["AdvancedMachineFeaturesOut"]
            ).optional(),
            "activeDirectoryConfig": t.proxy(
                renames["SqlActiveDirectoryConfigOut"]
            ).optional(),
            "storageAutoResizeLimit": t.string().optional(),
            "tier": t.string().optional(),
            "databaseReplicationEnabled": t.boolean().optional(),
            "sqlServerAuditConfig": t.proxy(
                renames["SqlServerAuditConfigOut"]
            ).optional(),
            "availabilityType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettingsOut"])
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
    types["ApiWarningIn"] = t.struct(
        {
            "region": t.string().optional(),
            "message": t.string().optional(),
            "code": t.string().optional(),
        }
    ).named(renames["ApiWarningIn"])
    types["ApiWarningOut"] = t.struct(
        {
            "region": t.string().optional(),
            "message": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiWarningOut"])
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
    types["SslCertIn"] = t.struct(
        {
            "selfLink": t.string().optional(),
            "expirationTime": t.string().optional(),
            "sha1Fingerprint": t.string().optional(),
            "createTime": t.string().optional(),
            "instance": t.string().optional(),
            "commonName": t.string().optional(),
            "cert": t.string().optional(),
            "kind": t.string().optional(),
            "certSerialNumber": t.string().optional(),
        }
    ).named(renames["SslCertIn"])
    types["SslCertOut"] = t.struct(
        {
            "selfLink": t.string().optional(),
            "expirationTime": t.string().optional(),
            "sha1Fingerprint": t.string().optional(),
            "createTime": t.string().optional(),
            "instance": t.string().optional(),
            "commonName": t.string().optional(),
            "cert": t.string().optional(),
            "kind": t.string().optional(),
            "certSerialNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SslCertOut"])
    types["UserIn"] = t.struct(
        {
            "instance": t.string().optional(),
            "passwordPolicy": t.proxy(
                renames["UserPasswordValidationPolicyIn"]
            ).optional(),
            "host": t.string().optional(),
            "password": t.string().optional(),
            "etag": t.string().optional(),
            "dualPasswordType": t.string().optional(),
            "kind": t.string().optional(),
            "project": t.string().optional(),
            "type": t.string().optional(),
            "sqlserverUserDetails": t.proxy(renames["SqlServerUserDetailsIn"]),
            "name": t.string().optional(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "instance": t.string().optional(),
            "passwordPolicy": t.proxy(
                renames["UserPasswordValidationPolicyOut"]
            ).optional(),
            "host": t.string().optional(),
            "password": t.string().optional(),
            "etag": t.string().optional(),
            "dualPasswordType": t.string().optional(),
            "kind": t.string().optional(),
            "project": t.string().optional(),
            "type": t.string().optional(),
            "sqlserverUserDetails": t.proxy(renames["SqlServerUserDetailsOut"]),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["SslCertsInsertRequestIn"] = t.struct(
        {"commonName": t.string().optional()}
    ).named(renames["SslCertsInsertRequestIn"])
    types["SslCertsInsertRequestOut"] = t.struct(
        {
            "commonName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SslCertsInsertRequestOut"])
    types["SqlScheduledMaintenanceIn"] = t.struct(
        {
            "canReschedule": t.boolean().optional(),
            "scheduleDeadlineTime": t.string().optional(),
            "canDefer": t.boolean(),
            "startTime": t.string().optional(),
        }
    ).named(renames["SqlScheduledMaintenanceIn"])
    types["SqlScheduledMaintenanceOut"] = t.struct(
        {
            "canReschedule": t.boolean().optional(),
            "scheduleDeadlineTime": t.string().optional(),
            "canDefer": t.boolean(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlScheduledMaintenanceOut"])
    types["DemoteMasterMySqlReplicaConfigurationIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "username": t.string().optional(),
            "clientCertificate": t.string().optional(),
            "password": t.string().optional(),
            "clientKey": t.string().optional(),
            "caCertificate": t.string().optional(),
        }
    ).named(renames["DemoteMasterMySqlReplicaConfigurationIn"])
    types["DemoteMasterMySqlReplicaConfigurationOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "username": t.string().optional(),
            "clientCertificate": t.string().optional(),
            "password": t.string().optional(),
            "clientKey": t.string().optional(),
            "caCertificate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DemoteMasterMySqlReplicaConfigurationOut"])
    types["GenerateEphemeralCertResponseIn"] = t.struct(
        {"ephemeralCert": t.proxy(renames["SslCertIn"]).optional()}
    ).named(renames["GenerateEphemeralCertResponseIn"])
    types["GenerateEphemeralCertResponseOut"] = t.struct(
        {
            "ephemeralCert": t.proxy(renames["SslCertOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateEphemeralCertResponseOut"])
    types["AclEntryIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "expirationTime": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["AclEntryIn"])
    types["AclEntryOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "expirationTime": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AclEntryOut"])
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
    types["PerformDiskShrinkContextIn"] = t.struct(
        {"targetSizeGb": t.string().optional()}
    ).named(renames["PerformDiskShrinkContextIn"])
    types["PerformDiskShrinkContextOut"] = t.struct(
        {
            "targetSizeGb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerformDiskShrinkContextOut"])
    types["DenyMaintenancePeriodIn"] = t.struct(
        {
            "endDate": t.string().optional(),
            "startDate": t.string().optional(),
            "time": t.string().optional(),
        }
    ).named(renames["DenyMaintenancePeriodIn"])
    types["DenyMaintenancePeriodOut"] = t.struct(
        {
            "endDate": t.string().optional(),
            "startDate": t.string().optional(),
            "time": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DenyMaintenancePeriodOut"])
    types["SslCertsCreateEphemeralRequestIn"] = t.struct(
        {"public_key": t.string().optional(), "access_token": t.string().optional()}
    ).named(renames["SslCertsCreateEphemeralRequestIn"])
    types["SslCertsCreateEphemeralRequestOut"] = t.struct(
        {
            "public_key": t.string().optional(),
            "access_token": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SslCertsCreateEphemeralRequestOut"])
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
    types["MySqlReplicaConfigurationIn"] = t.struct(
        {
            "connectRetryInterval": t.integer().optional(),
            "sslCipher": t.string().optional(),
            "masterHeartbeatPeriod": t.string().optional(),
            "clientCertificate": t.string().optional(),
            "verifyServerCertificate": t.boolean().optional(),
            "username": t.string().optional(),
            "caCertificate": t.string().optional(),
            "clientKey": t.string().optional(),
            "dumpFilePath": t.string().optional(),
            "kind": t.string().optional(),
            "password": t.string().optional(),
        }
    ).named(renames["MySqlReplicaConfigurationIn"])
    types["MySqlReplicaConfigurationOut"] = t.struct(
        {
            "connectRetryInterval": t.integer().optional(),
            "sslCipher": t.string().optional(),
            "masterHeartbeatPeriod": t.string().optional(),
            "clientCertificate": t.string().optional(),
            "verifyServerCertificate": t.boolean().optional(),
            "username": t.string().optional(),
            "caCertificate": t.string().optional(),
            "clientKey": t.string().optional(),
            "dumpFilePath": t.string().optional(),
            "kind": t.string().optional(),
            "password": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MySqlReplicaConfigurationOut"])
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
    types["OperationsListResponseIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["OperationIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["OperationsListResponseIn"])
    types["OperationsListResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["OperationOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationsListResponseOut"])
    types["BackupConfigurationIn"] = t.struct(
        {
            "replicationLogArchivingEnabled": t.boolean().optional(),
            "transactionLogRetentionDays": t.integer().optional(),
            "pointInTimeRecoveryEnabled": t.boolean().optional(),
            "backupRetentionSettings": t.proxy(
                renames["BackupRetentionSettingsIn"]
            ).optional(),
            "kind": t.string().optional(),
            "location": t.string().optional(),
            "enabled": t.boolean().optional(),
            "binaryLogEnabled": t.boolean().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["BackupConfigurationIn"])
    types["BackupConfigurationOut"] = t.struct(
        {
            "replicationLogArchivingEnabled": t.boolean().optional(),
            "transactionLogRetentionDays": t.integer().optional(),
            "pointInTimeRecoveryEnabled": t.boolean().optional(),
            "backupRetentionSettings": t.proxy(
                renames["BackupRetentionSettingsOut"]
            ).optional(),
            "kind": t.string().optional(),
            "location": t.string().optional(),
            "enabled": t.boolean().optional(),
            "binaryLogEnabled": t.boolean().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupConfigurationOut"])
    types["SslCertsInsertResponseIn"] = t.struct(
        {
            "clientCert": t.proxy(renames["SslCertDetailIn"]).optional(),
            "kind": t.string().optional(),
            "operation": t.proxy(renames["OperationIn"]).optional(),
            "serverCaCert": t.proxy(renames["SslCertIn"]).optional(),
        }
    ).named(renames["SslCertsInsertResponseIn"])
    types["SslCertsInsertResponseOut"] = t.struct(
        {
            "clientCert": t.proxy(renames["SslCertDetailOut"]).optional(),
            "kind": t.string().optional(),
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "serverCaCert": t.proxy(renames["SslCertOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SslCertsInsertResponseOut"])
    types["OperationIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "error": t.proxy(renames["OperationErrorsIn"]).optional(),
            "targetId": t.string().optional(),
            "exportContext": t.proxy(renames["ExportContextIn"]).optional(),
            "backupContext": t.proxy(renames["BackupContextIn"]).optional(),
            "insertTime": t.string().optional(),
            "operationType": t.string().optional(),
            "status": t.string().optional(),
            "name": t.string().optional(),
            "endTime": t.string().optional(),
            "targetProject": t.string().optional(),
            "importContext": t.proxy(renames["ImportContextIn"]).optional(),
            "selfLink": t.string().optional(),
            "kind": t.string().optional(),
            "user": t.string().optional(),
            "targetLink": t.string(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "targetId": t.string().optional(),
            "exportContext": t.proxy(renames["ExportContextOut"]).optional(),
            "backupContext": t.proxy(renames["BackupContextOut"]).optional(),
            "insertTime": t.string().optional(),
            "operationType": t.string().optional(),
            "status": t.string().optional(),
            "name": t.string().optional(),
            "endTime": t.string().optional(),
            "targetProject": t.string().optional(),
            "importContext": t.proxy(renames["ImportContextOut"]).optional(),
            "selfLink": t.string().optional(),
            "kind": t.string().optional(),
            "user": t.string().optional(),
            "targetLink": t.string(),
        }
    ).named(renames["OperationOut"])
    types["MaintenanceWindowIn"] = t.struct(
        {
            "updateTrack": t.string().optional(),
            "day": t.integer().optional(),
            "hour": t.integer().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["MaintenanceWindowIn"])
    types["MaintenanceWindowOut"] = t.struct(
        {
            "updateTrack": t.string().optional(),
            "day": t.integer().optional(),
            "hour": t.integer().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceWindowOut"])
    types["InstancesTruncateLogRequestIn"] = t.struct(
        {"truncateLogContext": t.proxy(renames["TruncateLogContextIn"]).optional()}
    ).named(renames["InstancesTruncateLogRequestIn"])
    types["InstancesTruncateLogRequestOut"] = t.struct(
        {
            "truncateLogContext": t.proxy(renames["TruncateLogContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesTruncateLogRequestOut"])
    types["InstancesFailoverRequestIn"] = t.struct(
        {"failoverContext": t.proxy(renames["FailoverContextIn"]).optional()}
    ).named(renames["InstancesFailoverRequestIn"])
    types["InstancesFailoverRequestOut"] = t.struct(
        {
            "failoverContext": t.proxy(renames["FailoverContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesFailoverRequestOut"])
    types["SqlInstancesResetReplicaSizeRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SqlInstancesResetReplicaSizeRequestIn"])
    types["SqlInstancesResetReplicaSizeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SqlInstancesResetReplicaSizeRequestOut"])
    types["SyncFlagsIn"] = t.struct(
        {"value": t.string().optional(), "name": t.string().optional()}
    ).named(renames["SyncFlagsIn"])
    types["SyncFlagsOut"] = t.struct(
        {
            "value": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SyncFlagsOut"])
    types["SqlInstancesStartExternalSyncRequestIn"] = t.struct(
        {
            "mysqlSyncConfig": t.proxy(renames["MySqlSyncConfigIn"]).optional(),
            "syncMode": t.string().optional(),
            "skipVerification": t.boolean().optional(),
        }
    ).named(renames["SqlInstancesStartExternalSyncRequestIn"])
    types["SqlInstancesStartExternalSyncRequestOut"] = t.struct(
        {
            "mysqlSyncConfig": t.proxy(renames["MySqlSyncConfigOut"]).optional(),
            "syncMode": t.string().optional(),
            "skipVerification": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlInstancesStartExternalSyncRequestOut"])
    types["BackupRunsListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["BackupRunIn"])).optional(),
        }
    ).named(renames["BackupRunsListResponseIn"])
    types["BackupRunsListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["BackupRunOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupRunsListResponseOut"])
    types["UsersListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["UserIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["UsersListResponseIn"])
    types["UsersListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["UserOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsersListResponseOut"])
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
    types["InsightsConfigIn"] = t.struct(
        {
            "queryInsightsEnabled": t.boolean().optional(),
            "queryPlansPerMinute": t.integer().optional(),
            "recordApplicationTags": t.boolean().optional(),
            "recordClientAddress": t.boolean().optional(),
            "queryStringLength": t.integer().optional(),
        }
    ).named(renames["InsightsConfigIn"])
    types["InsightsConfigOut"] = t.struct(
        {
            "queryInsightsEnabled": t.boolean().optional(),
            "queryPlansPerMinute": t.integer().optional(),
            "recordApplicationTags": t.boolean().optional(),
            "recordClientAddress": t.boolean().optional(),
            "queryStringLength": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsightsConfigOut"])
    types["InstanceReferenceIn"] = t.struct(
        {
            "project": t.string().optional(),
            "name": t.string().optional(),
            "region": t.string().optional(),
        }
    ).named(renames["InstanceReferenceIn"])
    types["InstanceReferenceOut"] = t.struct(
        {
            "project": t.string().optional(),
            "name": t.string().optional(),
            "region": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceReferenceOut"])
    types["AdvancedMachineFeaturesIn"] = t.struct(
        {"threadsPerCore": t.integer().optional()}
    ).named(renames["AdvancedMachineFeaturesIn"])
    types["AdvancedMachineFeaturesOut"] = t.struct(
        {
            "threadsPerCore": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvancedMachineFeaturesOut"])
    types["SqlServerAuditConfigIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "uploadInterval": t.string().optional(),
            "bucket": t.string().optional(),
            "retentionInterval": t.string().optional(),
        }
    ).named(renames["SqlServerAuditConfigIn"])
    types["SqlServerAuditConfigOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "uploadInterval": t.string().optional(),
            "bucket": t.string().optional(),
            "retentionInterval": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlServerAuditConfigOut"])
    types["BackupContextIn"] = t.struct(
        {"kind": t.string().optional(), "backupId": t.string().optional()}
    ).named(renames["BackupContextIn"])
    types["BackupContextOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "backupId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupContextOut"])
    types["DemoteMasterContextIn"] = t.struct(
        {
            "verifyGtidConsistency": t.boolean().optional(),
            "masterInstanceName": t.string().optional(),
            "replicaConfiguration": t.proxy(
                renames["DemoteMasterConfigurationIn"]
            ).optional(),
            "skipReplicationSetup": t.boolean().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["DemoteMasterContextIn"])
    types["DemoteMasterContextOut"] = t.struct(
        {
            "verifyGtidConsistency": t.boolean().optional(),
            "masterInstanceName": t.string().optional(),
            "replicaConfiguration": t.proxy(
                renames["DemoteMasterConfigurationOut"]
            ).optional(),
            "skipReplicationSetup": t.boolean().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DemoteMasterContextOut"])
    types["SqlInstancesGetDiskShrinkConfigResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "message": t.string().optional(),
            "minimalTargetSizeGb": t.string().optional(),
        }
    ).named(renames["SqlInstancesGetDiskShrinkConfigResponseIn"])
    types["SqlInstancesGetDiskShrinkConfigResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "message": t.string().optional(),
            "minimalTargetSizeGb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlInstancesGetDiskShrinkConfigResponseOut"])
    types["IpMappingIn"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "type": t.string().optional(),
            "timeToRetire": t.string().optional(),
        }
    ).named(renames["IpMappingIn"])
    types["IpMappingOut"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "type": t.string().optional(),
            "timeToRetire": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IpMappingOut"])
    types["SqlInstancesVerifyExternalSyncSettingsResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "errors": t.array(
                t.proxy(renames["SqlExternalSyncSettingErrorIn"])
            ).optional(),
            "warnings": t.array(
                t.proxy(renames["SqlExternalSyncSettingErrorIn"])
            ).optional(),
        }
    ).named(renames["SqlInstancesVerifyExternalSyncSettingsResponseIn"])
    types["SqlInstancesVerifyExternalSyncSettingsResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "errors": t.array(
                t.proxy(renames["SqlExternalSyncSettingErrorOut"])
            ).optional(),
            "warnings": t.array(
                t.proxy(renames["SqlExternalSyncSettingErrorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlInstancesVerifyExternalSyncSettingsResponseOut"])
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
    types["OperationErrorsIn"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["OperationErrorIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["OperationErrorsIn"])
    types["OperationErrorsOut"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["OperationErrorOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationErrorsOut"])
    types["OnPremisesConfigurationIn"] = t.struct(
        {
            "dumpFilePath": t.string().optional(),
            "kind": t.string().optional(),
            "clientCertificate": t.string().optional(),
            "username": t.string().optional(),
            "sourceInstance": t.proxy(renames["InstanceReferenceIn"]).optional(),
            "password": t.string().optional(),
            "clientKey": t.string().optional(),
            "hostPort": t.string().optional(),
            "caCertificate": t.string().optional(),
        }
    ).named(renames["OnPremisesConfigurationIn"])
    types["OnPremisesConfigurationOut"] = t.struct(
        {
            "dumpFilePath": t.string().optional(),
            "kind": t.string().optional(),
            "clientCertificate": t.string().optional(),
            "username": t.string().optional(),
            "sourceInstance": t.proxy(renames["InstanceReferenceOut"]).optional(),
            "password": t.string().optional(),
            "clientKey": t.string().optional(),
            "hostPort": t.string().optional(),
            "caCertificate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OnPremisesConfigurationOut"])
    types["SslCertDetailIn"] = t.struct(
        {
            "certPrivateKey": t.string().optional(),
            "certInfo": t.proxy(renames["SslCertIn"]).optional(),
        }
    ).named(renames["SslCertDetailIn"])
    types["SslCertDetailOut"] = t.struct(
        {
            "certPrivateKey": t.string().optional(),
            "certInfo": t.proxy(renames["SslCertOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SslCertDetailOut"])
    types["RestoreBackupContextIn"] = t.struct(
        {
            "instanceId": t.string().optional(),
            "kind": t.string().optional(),
            "backupRunId": t.string().optional(),
            "project": t.string().optional(),
        }
    ).named(renames["RestoreBackupContextIn"])
    types["RestoreBackupContextOut"] = t.struct(
        {
            "instanceId": t.string().optional(),
            "kind": t.string().optional(),
            "backupRunId": t.string().optional(),
            "project": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreBackupContextOut"])
    types["InstancesExportRequestIn"] = t.struct(
        {"exportContext": t.proxy(renames["ExportContextIn"]).optional()}
    ).named(renames["InstancesExportRequestIn"])
    types["InstancesExportRequestOut"] = t.struct(
        {
            "exportContext": t.proxy(renames["ExportContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesExportRequestOut"])
    types["BackupRunIn"] = t.struct(
        {
            "windowStartTime": t.string().optional(),
            "endTime": t.string().optional(),
            "location": t.string().optional(),
            "status": t.string().optional(),
            "type": t.string().optional(),
            "description": t.string().optional(),
            "instance": t.string().optional(),
            "diskEncryptionConfiguration": t.proxy(
                renames["DiskEncryptionConfigurationIn"]
            ).optional(),
            "enqueuedTime": t.string().optional(),
            "timeZone": t.string().optional(),
            "diskEncryptionStatus": t.proxy(
                renames["DiskEncryptionStatusIn"]
            ).optional(),
            "startTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "error": t.proxy(renames["OperationErrorIn"]).optional(),
            "id": t.string().optional(),
            "backupKind": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["BackupRunIn"])
    types["BackupRunOut"] = t.struct(
        {
            "windowStartTime": t.string().optional(),
            "endTime": t.string().optional(),
            "location": t.string().optional(),
            "status": t.string().optional(),
            "type": t.string().optional(),
            "description": t.string().optional(),
            "instance": t.string().optional(),
            "diskEncryptionConfiguration": t.proxy(
                renames["DiskEncryptionConfigurationOut"]
            ).optional(),
            "enqueuedTime": t.string().optional(),
            "timeZone": t.string().optional(),
            "diskEncryptionStatus": t.proxy(
                renames["DiskEncryptionStatusOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "id": t.string().optional(),
            "backupKind": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["BackupRunOut"])
    types["InstancesCloneRequestIn"] = t.struct(
        {"cloneContext": t.proxy(renames["CloneContextIn"]).optional()}
    ).named(renames["InstancesCloneRequestIn"])
    types["InstancesCloneRequestOut"] = t.struct(
        {
            "cloneContext": t.proxy(renames["CloneContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesCloneRequestOut"])
    types["BinLogCoordinatesIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "binLogPosition": t.string().optional(),
            "binLogFileName": t.string().optional(),
        }
    ).named(renames["BinLogCoordinatesIn"])
    types["BinLogCoordinatesOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "binLogPosition": t.string().optional(),
            "binLogFileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BinLogCoordinatesOut"])
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
    types["SslCertsListResponseIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["SslCertIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["SslCertsListResponseIn"])
    types["SslCertsListResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["SslCertOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SslCertsListResponseOut"])
    types["ImportContextIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "database": t.string().optional(),
            "bakImportOptions": t.struct(
                {
                    "striped": t.boolean().optional(),
                    "encryptionOptions": t.struct(
                        {
                            "pvkPath": t.string().optional(),
                            "certPath": t.string().optional(),
                            "pvkPassword": t.string().optional(),
                        }
                    ),
                }
            ).optional(),
            "importUser": t.string().optional(),
            "fileType": t.string().optional(),
            "csvImportOptions": t.struct(
                {
                    "escapeCharacter": t.string().optional(),
                    "fieldsTerminatedBy": t.string().optional(),
                    "columns": t.array(t.string()).optional(),
                    "table": t.string().optional(),
                    "linesTerminatedBy": t.string().optional(),
                    "quoteCharacter": t.string().optional(),
                }
            ).optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["ImportContextIn"])
    types["ImportContextOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "database": t.string().optional(),
            "bakImportOptions": t.struct(
                {
                    "striped": t.boolean().optional(),
                    "encryptionOptions": t.struct(
                        {
                            "pvkPath": t.string().optional(),
                            "certPath": t.string().optional(),
                            "pvkPassword": t.string().optional(),
                        }
                    ),
                }
            ).optional(),
            "importUser": t.string().optional(),
            "fileType": t.string().optional(),
            "csvImportOptions": t.struct(
                {
                    "escapeCharacter": t.string().optional(),
                    "fieldsTerminatedBy": t.string().optional(),
                    "columns": t.array(t.string()).optional(),
                    "table": t.string().optional(),
                    "linesTerminatedBy": t.string().optional(),
                    "quoteCharacter": t.string().optional(),
                }
            ).optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportContextOut"])
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
    types["FlagIn"] = t.struct(
        {
            "appliesTo": t.array(t.string()).optional(),
            "requiresRestart": t.boolean().optional(),
            "minValue": t.string().optional(),
            "kind": t.string().optional(),
            "inBeta": t.boolean().optional(),
            "allowedIntValues": t.array(t.string()).optional(),
            "maxValue": t.string().optional(),
            "allowedStringValues": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["FlagIn"])
    types["FlagOut"] = t.struct(
        {
            "appliesTo": t.array(t.string()).optional(),
            "requiresRestart": t.boolean().optional(),
            "minValue": t.string().optional(),
            "kind": t.string().optional(),
            "inBeta": t.boolean().optional(),
            "allowedIntValues": t.array(t.string()).optional(),
            "maxValue": t.string().optional(),
            "allowedStringValues": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FlagOut"])
    types["IpConfigurationIn"] = t.struct(
        {
            "ipv4Enabled": t.boolean().optional(),
            "privateNetwork": t.string().optional(),
            "enablePrivatePathForGoogleCloudServices": t.boolean().optional(),
            "authorizedNetworks": t.array(t.proxy(renames["AclEntryIn"])).optional(),
            "requireSsl": t.boolean().optional(),
            "allocatedIpRange": t.string().optional(),
        }
    ).named(renames["IpConfigurationIn"])
    types["IpConfigurationOut"] = t.struct(
        {
            "ipv4Enabled": t.boolean().optional(),
            "privateNetwork": t.string().optional(),
            "enablePrivatePathForGoogleCloudServices": t.boolean().optional(),
            "authorizedNetworks": t.array(t.proxy(renames["AclEntryOut"])).optional(),
            "requireSsl": t.boolean().optional(),
            "allocatedIpRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IpConfigurationOut"])
    types["CloneContextIn"] = t.struct(
        {
            "destinationInstanceName": t.string().optional(),
            "pitrTimestampMs": t.string().optional(),
            "allocatedIpRange": t.string().optional(),
            "databaseNames": t.array(t.string()).optional(),
            "pointInTime": t.string().optional(),
            "binLogCoordinates": t.proxy(renames["BinLogCoordinatesIn"]).optional(),
            "kind": t.string().optional(),
            "preferredZone": t.string().optional(),
        }
    ).named(renames["CloneContextIn"])
    types["CloneContextOut"] = t.struct(
        {
            "destinationInstanceName": t.string().optional(),
            "pitrTimestampMs": t.string().optional(),
            "allocatedIpRange": t.string().optional(),
            "databaseNames": t.array(t.string()).optional(),
            "pointInTime": t.string().optional(),
            "binLogCoordinates": t.proxy(renames["BinLogCoordinatesOut"]).optional(),
            "kind": t.string().optional(),
            "preferredZone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloneContextOut"])
    types["FailoverContextIn"] = t.struct(
        {"settingsVersion": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["FailoverContextIn"])
    types["FailoverContextOut"] = t.struct(
        {
            "settingsVersion": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FailoverContextOut"])
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
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "statusDetail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["ReplicaConfigurationIn"] = t.struct(
        {
            "mysqlReplicaConfiguration": t.proxy(
                renames["MySqlReplicaConfigurationIn"]
            ).optional(),
            "kind": t.string().optional(),
            "failoverTarget": t.boolean().optional(),
        }
    ).named(renames["ReplicaConfigurationIn"])
    types["ReplicaConfigurationOut"] = t.struct(
        {
            "mysqlReplicaConfiguration": t.proxy(
                renames["MySqlReplicaConfigurationOut"]
            ).optional(),
            "kind": t.string().optional(),
            "failoverTarget": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplicaConfigurationOut"])
    types["DiskEncryptionStatusIn"] = t.struct(
        {"kind": t.string().optional(), "kmsKeyVersionName": t.string().optional()}
    ).named(renames["DiskEncryptionStatusIn"])
    types["DiskEncryptionStatusOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "kmsKeyVersionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskEncryptionStatusOut"])
    types["DiskEncryptionConfigurationIn"] = t.struct(
        {"kind": t.string().optional(), "kmsKeyName": t.string().optional()}
    ).named(renames["DiskEncryptionConfigurationIn"])
    types["DiskEncryptionConfigurationOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskEncryptionConfigurationOut"])
    types["DatabaseInstanceIn"] = t.struct(
        {
            "diskEncryptionConfiguration": t.proxy(
                renames["DiskEncryptionConfigurationIn"]
            ).optional(),
            "ipv6Address": t.string().optional(),
            "secondaryGceZone": t.string().optional(),
            "kind": t.string().optional(),
            "failoverReplica": t.struct(
                {"name": t.string().optional(), "available": t.boolean().optional()}
            ).optional(),
            "connectionName": t.string().optional(),
            "scheduledMaintenance": t.proxy(
                renames["SqlScheduledMaintenanceIn"]
            ).optional(),
            "diskEncryptionStatus": t.proxy(
                renames["DiskEncryptionStatusIn"]
            ).optional(),
            "outOfDiskReport": t.proxy(renames["SqlOutOfDiskReportIn"]).optional(),
            "rootPassword": t.string().optional(),
            "gceZone": t.string().optional(),
            "serverCaCert": t.proxy(renames["SslCertIn"]).optional(),
            "region": t.string().optional(),
            "instanceType": t.string().optional(),
            "masterInstanceName": t.string().optional(),
            "currentDiskSize": t.string().optional(),
            "maintenanceVersion": t.string().optional(),
            "project": t.string().optional(),
            "replicaNames": t.array(t.string()).optional(),
            "satisfiesPzs": t.boolean().optional(),
            "settings": t.proxy(renames["SettingsIn"]).optional(),
            "maxDiskSize": t.string().optional(),
            "serviceAccountEmailAddress": t.string().optional(),
            "databaseVersion": t.string().optional(),
            "suspensionReason": t.array(t.string()).optional(),
            "state": t.string().optional(),
            "backendType": t.string().optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "selfLink": t.string().optional(),
            "replicaConfiguration": t.proxy(
                renames["ReplicaConfigurationIn"]
            ).optional(),
            "ipAddresses": t.array(t.proxy(renames["IpMappingIn"])).optional(),
            "onPremisesConfiguration": t.proxy(
                renames["OnPremisesConfigurationIn"]
            ).optional(),
        }
    ).named(renames["DatabaseInstanceIn"])
    types["DatabaseInstanceOut"] = t.struct(
        {
            "diskEncryptionConfiguration": t.proxy(
                renames["DiskEncryptionConfigurationOut"]
            ).optional(),
            "ipv6Address": t.string().optional(),
            "secondaryGceZone": t.string().optional(),
            "kind": t.string().optional(),
            "createTime": t.string().optional(),
            "failoverReplica": t.struct(
                {"name": t.string().optional(), "available": t.boolean().optional()}
            ).optional(),
            "connectionName": t.string().optional(),
            "databaseInstalledVersion": t.string().optional(),
            "scheduledMaintenance": t.proxy(
                renames["SqlScheduledMaintenanceOut"]
            ).optional(),
            "diskEncryptionStatus": t.proxy(
                renames["DiskEncryptionStatusOut"]
            ).optional(),
            "outOfDiskReport": t.proxy(renames["SqlOutOfDiskReportOut"]).optional(),
            "rootPassword": t.string().optional(),
            "gceZone": t.string().optional(),
            "serverCaCert": t.proxy(renames["SslCertOut"]).optional(),
            "region": t.string().optional(),
            "instanceType": t.string().optional(),
            "masterInstanceName": t.string().optional(),
            "currentDiskSize": t.string().optional(),
            "maintenanceVersion": t.string().optional(),
            "project": t.string().optional(),
            "replicaNames": t.array(t.string()).optional(),
            "satisfiesPzs": t.boolean().optional(),
            "settings": t.proxy(renames["SettingsOut"]).optional(),
            "maxDiskSize": t.string().optional(),
            "serviceAccountEmailAddress": t.string().optional(),
            "databaseVersion": t.string().optional(),
            "suspensionReason": t.array(t.string()).optional(),
            "state": t.string().optional(),
            "backendType": t.string().optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "selfLink": t.string().optional(),
            "availableMaintenanceVersions": t.array(t.string()).optional(),
            "replicaConfiguration": t.proxy(
                renames["ReplicaConfigurationOut"]
            ).optional(),
            "ipAddresses": t.array(t.proxy(renames["IpMappingOut"])).optional(),
            "onPremisesConfiguration": t.proxy(
                renames["OnPremisesConfigurationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseInstanceOut"])
    types["TruncateLogContextIn"] = t.struct(
        {"logType": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["TruncateLogContextIn"])
    types["TruncateLogContextOut"] = t.struct(
        {
            "logType": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TruncateLogContextOut"])
    types["ConnectSettingsIn"] = t.struct(
        {
            "region": t.string().optional(),
            "databaseVersion": t.string().optional(),
            "ipAddresses": t.array(t.proxy(renames["IpMappingIn"])).optional(),
            "kind": t.string().optional(),
            "backendType": t.string().optional(),
            "serverCaCert": t.proxy(renames["SslCertIn"]).optional(),
        }
    ).named(renames["ConnectSettingsIn"])
    types["ConnectSettingsOut"] = t.struct(
        {
            "region": t.string().optional(),
            "databaseVersion": t.string().optional(),
            "ipAddresses": t.array(t.proxy(renames["IpMappingOut"])).optional(),
            "kind": t.string().optional(),
            "backendType": t.string().optional(),
            "serverCaCert": t.proxy(renames["SslCertOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectSettingsOut"])

    functions = {}
    functions["backupRunsInsert"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/backupRuns/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "project": t.string().optional(),
                "instance": t.string().optional(),
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
                "id": t.string().optional(),
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BackupRunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["backupRunsList"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/backupRuns/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "project": t.string().optional(),
                "instance": t.string().optional(),
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
                "id": t.string().optional(),
                "project": t.string().optional(),
                "instance": t.string().optional(),
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
    functions["sslCertsDelete"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/sslCerts",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SslCertsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sslCertsInsert"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/sslCerts",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SslCertsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sslCertsCreateEphemeral"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/sslCerts",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SslCertsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sslCertsGet"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/sslCerts",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SslCertsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sslCertsList"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/sslCerts",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SslCertsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["connectGet"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}:generateEphemeralCert",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "public_key": t.string().optional(),
                "validDuration": t.string().optional(),
                "access_token": t.string().optional(),
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
                "public_key": t.string().optional(),
                "validDuration": t.string().optional(),
                "access_token": t.string().optional(),
                "readTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateEphemeralCertResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesResetReplicaSize"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/getDiskShrinkConfig",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SqlInstancesGetDiskShrinkConfigResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesStartExternalSync"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/getDiskShrinkConfig",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SqlInstancesGetDiskShrinkConfigResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesPerformDiskShrink"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/getDiskShrinkConfig",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SqlInstancesGetDiskShrinkConfigResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesVerifyExternalSyncSettings"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/getDiskShrinkConfig",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SqlInstancesGetDiskShrinkConfigResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesRescheduleMaintenance"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/getDiskShrinkConfig",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SqlInstancesGetDiskShrinkConfigResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesGetDiskShrinkConfig"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/getDiskShrinkConfig",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SqlInstancesGetDiskShrinkConfigResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsList"] = sqladmin.get(
        "v1/projects/{project}/operations/{operation}",
        t.struct(
            {
                "project": t.string().optional(),
                "operation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = sqladmin.get(
        "v1/projects/{project}/operations/{operation}",
        t.struct(
            {
                "project": t.string().optional(),
                "operation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersUpdate"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}/users",
        t.struct(
            {
                "project": t.string().optional(),
                "name": t.string().optional(),
                "instance": t.string().optional(),
                "host": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersGet"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}/users",
        t.struct(
            {
                "project": t.string().optional(),
                "name": t.string().optional(),
                "instance": t.string().optional(),
                "host": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersInsert"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}/users",
        t.struct(
            {
                "project": t.string().optional(),
                "name": t.string().optional(),
                "instance": t.string().optional(),
                "host": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersList"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}/users",
        t.struct(
            {
                "project": t.string().optional(),
                "name": t.string().optional(),
                "instance": t.string().optional(),
                "host": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDelete"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}/users",
        t.struct(
            {
                "project": t.string().optional(),
                "name": t.string().optional(),
                "instance": t.string().optional(),
                "host": t.string().optional(),
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
    functions["databasesDelete"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/databases",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatabasesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["databasesUpdate"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/databases",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatabasesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["databasesGet"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/databases",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatabasesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["databasesInsert"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/databases",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatabasesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["databasesPatch"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/databases",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatabasesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["databasesList"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/databases",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatabasesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesGet"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}",
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
    functions["instancesStopReplica"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}",
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
    functions["instancesFailover"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}",
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
    functions["instancesDemoteMaster"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}",
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
    functions["instancesClone"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}",
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
    functions["instancesRestart"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}",
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
    functions["instancesResetSslConfig"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}",
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
    functions["instancesStartReplica"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}",
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
    functions["instancesRestoreBackup"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}",
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
    functions["instancesPatch"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}",
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
    functions["instancesExport"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}",
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
    functions["instancesImport"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}",
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
    functions["instancesAddServerCa"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}",
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
    functions["instancesUpdate"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}",
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
    functions["instancesTruncateLog"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}",
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
    functions["instancesList"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}",
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
    functions["instancesListServerCas"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}",
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
    functions["instancesInsert"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}",
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
    functions["instancesRotateServerCa"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}",
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
    functions["instancesPromoteReplica"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}",
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
    functions["instancesDelete"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}",
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

    return Import(
        importer="sqladmin", renames=renames, types=types, functions=functions
    )
