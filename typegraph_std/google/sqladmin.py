from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_sqladmin():
    sqladmin = HTTPRuntime("https://sqladmin.googleapis.com/")

    renames = {
        "ErrorResponse": "_sqladmin_1_ErrorResponse",
        "InstancesDemoteMasterRequestIn": "_sqladmin_2_InstancesDemoteMasterRequestIn",
        "InstancesDemoteMasterRequestOut": "_sqladmin_3_InstancesDemoteMasterRequestOut",
        "MySqlSyncConfigIn": "_sqladmin_4_MySqlSyncConfigIn",
        "MySqlSyncConfigOut": "_sqladmin_5_MySqlSyncConfigOut",
        "BackupReencryptionConfigIn": "_sqladmin_6_BackupReencryptionConfigIn",
        "BackupReencryptionConfigOut": "_sqladmin_7_BackupReencryptionConfigOut",
        "InstancesRestoreBackupRequestIn": "_sqladmin_8_InstancesRestoreBackupRequestIn",
        "InstancesRestoreBackupRequestOut": "_sqladmin_9_InstancesRestoreBackupRequestOut",
        "BackupRunIn": "_sqladmin_10_BackupRunIn",
        "BackupRunOut": "_sqladmin_11_BackupRunOut",
        "UserPasswordValidationPolicyIn": "_sqladmin_12_UserPasswordValidationPolicyIn",
        "UserPasswordValidationPolicyOut": "_sqladmin_13_UserPasswordValidationPolicyOut",
        "BackupRunsListResponseIn": "_sqladmin_14_BackupRunsListResponseIn",
        "BackupRunsListResponseOut": "_sqladmin_15_BackupRunsListResponseOut",
        "SqlServerDatabaseDetailsIn": "_sqladmin_16_SqlServerDatabaseDetailsIn",
        "SqlServerDatabaseDetailsOut": "_sqladmin_17_SqlServerDatabaseDetailsOut",
        "AclEntryIn": "_sqladmin_18_AclEntryIn",
        "AclEntryOut": "_sqladmin_19_AclEntryOut",
        "InstancesImportRequestIn": "_sqladmin_20_InstancesImportRequestIn",
        "InstancesImportRequestOut": "_sqladmin_21_InstancesImportRequestOut",
        "SqlInstancesVerifyExternalSyncSettingsResponseIn": "_sqladmin_22_SqlInstancesVerifyExternalSyncSettingsResponseIn",
        "SqlInstancesVerifyExternalSyncSettingsResponseOut": "_sqladmin_23_SqlInstancesVerifyExternalSyncSettingsResponseOut",
        "RescheduleIn": "_sqladmin_24_RescheduleIn",
        "RescheduleOut": "_sqladmin_25_RescheduleOut",
        "IpMappingIn": "_sqladmin_26_IpMappingIn",
        "IpMappingOut": "_sqladmin_27_IpMappingOut",
        "SyncFlagsIn": "_sqladmin_28_SyncFlagsIn",
        "SyncFlagsOut": "_sqladmin_29_SyncFlagsOut",
        "InstancesFailoverRequestIn": "_sqladmin_30_InstancesFailoverRequestIn",
        "InstancesFailoverRequestOut": "_sqladmin_31_InstancesFailoverRequestOut",
        "OperationErrorIn": "_sqladmin_32_OperationErrorIn",
        "OperationErrorOut": "_sqladmin_33_OperationErrorOut",
        "SqlInstancesStartExternalSyncRequestIn": "_sqladmin_34_SqlInstancesStartExternalSyncRequestIn",
        "SqlInstancesStartExternalSyncRequestOut": "_sqladmin_35_SqlInstancesStartExternalSyncRequestOut",
        "InstancesListServerCasResponseIn": "_sqladmin_36_InstancesListServerCasResponseIn",
        "InstancesListServerCasResponseOut": "_sqladmin_37_InstancesListServerCasResponseOut",
        "SqlServerAuditConfigIn": "_sqladmin_38_SqlServerAuditConfigIn",
        "SqlServerAuditConfigOut": "_sqladmin_39_SqlServerAuditConfigOut",
        "AdvancedMachineFeaturesIn": "_sqladmin_40_AdvancedMachineFeaturesIn",
        "AdvancedMachineFeaturesOut": "_sqladmin_41_AdvancedMachineFeaturesOut",
        "OperationMetadataIn": "_sqladmin_42_OperationMetadataIn",
        "OperationMetadataOut": "_sqladmin_43_OperationMetadataOut",
        "SqlActiveDirectoryConfigIn": "_sqladmin_44_SqlActiveDirectoryConfigIn",
        "SqlActiveDirectoryConfigOut": "_sqladmin_45_SqlActiveDirectoryConfigOut",
        "InstanceReferenceIn": "_sqladmin_46_InstanceReferenceIn",
        "InstanceReferenceOut": "_sqladmin_47_InstanceReferenceOut",
        "MySqlReplicaConfigurationIn": "_sqladmin_48_MySqlReplicaConfigurationIn",
        "MySqlReplicaConfigurationOut": "_sqladmin_49_MySqlReplicaConfigurationOut",
        "ReplicaConfigurationIn": "_sqladmin_50_ReplicaConfigurationIn",
        "ReplicaConfigurationOut": "_sqladmin_51_ReplicaConfigurationOut",
        "ApiWarningIn": "_sqladmin_52_ApiWarningIn",
        "ApiWarningOut": "_sqladmin_53_ApiWarningOut",
        "PasswordValidationPolicyIn": "_sqladmin_54_PasswordValidationPolicyIn",
        "PasswordValidationPolicyOut": "_sqladmin_55_PasswordValidationPolicyOut",
        "IpConfigurationIn": "_sqladmin_56_IpConfigurationIn",
        "IpConfigurationOut": "_sqladmin_57_IpConfigurationOut",
        "SqlScheduledMaintenanceIn": "_sqladmin_58_SqlScheduledMaintenanceIn",
        "SqlScheduledMaintenanceOut": "_sqladmin_59_SqlScheduledMaintenanceOut",
        "DemoteMasterContextIn": "_sqladmin_60_DemoteMasterContextIn",
        "DemoteMasterContextOut": "_sqladmin_61_DemoteMasterContextOut",
        "UsersListResponseIn": "_sqladmin_62_UsersListResponseIn",
        "UsersListResponseOut": "_sqladmin_63_UsersListResponseOut",
        "OperationErrorsIn": "_sqladmin_64_OperationErrorsIn",
        "OperationErrorsOut": "_sqladmin_65_OperationErrorsOut",
        "OperationIn": "_sqladmin_66_OperationIn",
        "OperationOut": "_sqladmin_67_OperationOut",
        "SslCertsInsertRequestIn": "_sqladmin_68_SslCertsInsertRequestIn",
        "SslCertsInsertRequestOut": "_sqladmin_69_SslCertsInsertRequestOut",
        "BackupContextIn": "_sqladmin_70_BackupContextIn",
        "BackupContextOut": "_sqladmin_71_BackupContextOut",
        "SqlInstancesVerifyExternalSyncSettingsRequestIn": "_sqladmin_72_SqlInstancesVerifyExternalSyncSettingsRequestIn",
        "SqlInstancesVerifyExternalSyncSettingsRequestOut": "_sqladmin_73_SqlInstancesVerifyExternalSyncSettingsRequestOut",
        "GenerateEphemeralCertRequestIn": "_sqladmin_74_GenerateEphemeralCertRequestIn",
        "GenerateEphemeralCertRequestOut": "_sqladmin_75_GenerateEphemeralCertRequestOut",
        "DiskEncryptionStatusIn": "_sqladmin_76_DiskEncryptionStatusIn",
        "DiskEncryptionStatusOut": "_sqladmin_77_DiskEncryptionStatusOut",
        "DatabasesListResponseIn": "_sqladmin_78_DatabasesListResponseIn",
        "DatabasesListResponseOut": "_sqladmin_79_DatabasesListResponseOut",
        "SslCertsInsertResponseIn": "_sqladmin_80_SslCertsInsertResponseIn",
        "SslCertsInsertResponseOut": "_sqladmin_81_SslCertsInsertResponseOut",
        "SqlInstancesGetDiskShrinkConfigResponseIn": "_sqladmin_82_SqlInstancesGetDiskShrinkConfigResponseIn",
        "SqlInstancesGetDiskShrinkConfigResponseOut": "_sqladmin_83_SqlInstancesGetDiskShrinkConfigResponseOut",
        "SettingsIn": "_sqladmin_84_SettingsIn",
        "SettingsOut": "_sqladmin_85_SettingsOut",
        "SslCertIn": "_sqladmin_86_SslCertIn",
        "SslCertOut": "_sqladmin_87_SslCertOut",
        "DemoteMasterConfigurationIn": "_sqladmin_88_DemoteMasterConfigurationIn",
        "DemoteMasterConfigurationOut": "_sqladmin_89_DemoteMasterConfigurationOut",
        "SqlInstancesResetReplicaSizeRequestIn": "_sqladmin_90_SqlInstancesResetReplicaSizeRequestIn",
        "SqlInstancesResetReplicaSizeRequestOut": "_sqladmin_91_SqlInstancesResetReplicaSizeRequestOut",
        "DatabaseInstanceIn": "_sqladmin_92_DatabaseInstanceIn",
        "DatabaseInstanceOut": "_sqladmin_93_DatabaseInstanceOut",
        "CloneContextIn": "_sqladmin_94_CloneContextIn",
        "CloneContextOut": "_sqladmin_95_CloneContextOut",
        "BinLogCoordinatesIn": "_sqladmin_96_BinLogCoordinatesIn",
        "BinLogCoordinatesOut": "_sqladmin_97_BinLogCoordinatesOut",
        "EmptyIn": "_sqladmin_98_EmptyIn",
        "EmptyOut": "_sqladmin_99_EmptyOut",
        "MaintenanceWindowIn": "_sqladmin_100_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_sqladmin_101_MaintenanceWindowOut",
        "RestoreBackupContextIn": "_sqladmin_102_RestoreBackupContextIn",
        "RestoreBackupContextOut": "_sqladmin_103_RestoreBackupContextOut",
        "PasswordStatusIn": "_sqladmin_104_PasswordStatusIn",
        "PasswordStatusOut": "_sqladmin_105_PasswordStatusOut",
        "SslCertsListResponseIn": "_sqladmin_106_SslCertsListResponseIn",
        "SslCertsListResponseOut": "_sqladmin_107_SslCertsListResponseOut",
        "InstancesExportRequestIn": "_sqladmin_108_InstancesExportRequestIn",
        "InstancesExportRequestOut": "_sqladmin_109_InstancesExportRequestOut",
        "InstancesCloneRequestIn": "_sqladmin_110_InstancesCloneRequestIn",
        "InstancesCloneRequestOut": "_sqladmin_111_InstancesCloneRequestOut",
        "InstancesRotateServerCaRequestIn": "_sqladmin_112_InstancesRotateServerCaRequestIn",
        "InstancesRotateServerCaRequestOut": "_sqladmin_113_InstancesRotateServerCaRequestOut",
        "BackupConfigurationIn": "_sqladmin_114_BackupConfigurationIn",
        "BackupConfigurationOut": "_sqladmin_115_BackupConfigurationOut",
        "TierIn": "_sqladmin_116_TierIn",
        "TierOut": "_sqladmin_117_TierOut",
        "ExportContextIn": "_sqladmin_118_ExportContextIn",
        "ExportContextOut": "_sqladmin_119_ExportContextOut",
        "GenerateEphemeralCertResponseIn": "_sqladmin_120_GenerateEphemeralCertResponseIn",
        "GenerateEphemeralCertResponseOut": "_sqladmin_121_GenerateEphemeralCertResponseOut",
        "ImportContextIn": "_sqladmin_122_ImportContextIn",
        "ImportContextOut": "_sqladmin_123_ImportContextOut",
        "OperationsListResponseIn": "_sqladmin_124_OperationsListResponseIn",
        "OperationsListResponseOut": "_sqladmin_125_OperationsListResponseOut",
        "DiskEncryptionConfigurationIn": "_sqladmin_126_DiskEncryptionConfigurationIn",
        "DiskEncryptionConfigurationOut": "_sqladmin_127_DiskEncryptionConfigurationOut",
        "SslCertsCreateEphemeralRequestIn": "_sqladmin_128_SslCertsCreateEphemeralRequestIn",
        "SslCertsCreateEphemeralRequestOut": "_sqladmin_129_SslCertsCreateEphemeralRequestOut",
        "SqlOutOfDiskReportIn": "_sqladmin_130_SqlOutOfDiskReportIn",
        "SqlOutOfDiskReportOut": "_sqladmin_131_SqlOutOfDiskReportOut",
        "TiersListResponseIn": "_sqladmin_132_TiersListResponseIn",
        "TiersListResponseOut": "_sqladmin_133_TiersListResponseOut",
        "LocationPreferenceIn": "_sqladmin_134_LocationPreferenceIn",
        "LocationPreferenceOut": "_sqladmin_135_LocationPreferenceOut",
        "PerformDiskShrinkContextIn": "_sqladmin_136_PerformDiskShrinkContextIn",
        "PerformDiskShrinkContextOut": "_sqladmin_137_PerformDiskShrinkContextOut",
        "SqlInstancesRescheduleMaintenanceRequestBodyIn": "_sqladmin_138_SqlInstancesRescheduleMaintenanceRequestBodyIn",
        "SqlInstancesRescheduleMaintenanceRequestBodyOut": "_sqladmin_139_SqlInstancesRescheduleMaintenanceRequestBodyOut",
        "DatabaseIn": "_sqladmin_140_DatabaseIn",
        "DatabaseOut": "_sqladmin_141_DatabaseOut",
        "DatabaseFlagsIn": "_sqladmin_142_DatabaseFlagsIn",
        "DatabaseFlagsOut": "_sqladmin_143_DatabaseFlagsOut",
        "ConnectSettingsIn": "_sqladmin_144_ConnectSettingsIn",
        "ConnectSettingsOut": "_sqladmin_145_ConnectSettingsOut",
        "FlagsListResponseIn": "_sqladmin_146_FlagsListResponseIn",
        "FlagsListResponseOut": "_sqladmin_147_FlagsListResponseOut",
        "InstancesTruncateLogRequestIn": "_sqladmin_148_InstancesTruncateLogRequestIn",
        "InstancesTruncateLogRequestOut": "_sqladmin_149_InstancesTruncateLogRequestOut",
        "TruncateLogContextIn": "_sqladmin_150_TruncateLogContextIn",
        "TruncateLogContextOut": "_sqladmin_151_TruncateLogContextOut",
        "DemoteMasterMySqlReplicaConfigurationIn": "_sqladmin_152_DemoteMasterMySqlReplicaConfigurationIn",
        "DemoteMasterMySqlReplicaConfigurationOut": "_sqladmin_153_DemoteMasterMySqlReplicaConfigurationOut",
        "DenyMaintenancePeriodIn": "_sqladmin_154_DenyMaintenancePeriodIn",
        "DenyMaintenancePeriodOut": "_sqladmin_155_DenyMaintenancePeriodOut",
        "OnPremisesConfigurationIn": "_sqladmin_156_OnPremisesConfigurationIn",
        "OnPremisesConfigurationOut": "_sqladmin_157_OnPremisesConfigurationOut",
        "InstancesReencryptRequestIn": "_sqladmin_158_InstancesReencryptRequestIn",
        "InstancesReencryptRequestOut": "_sqladmin_159_InstancesReencryptRequestOut",
        "InstancesListResponseIn": "_sqladmin_160_InstancesListResponseIn",
        "InstancesListResponseOut": "_sqladmin_161_InstancesListResponseOut",
        "SqlServerUserDetailsIn": "_sqladmin_162_SqlServerUserDetailsIn",
        "SqlServerUserDetailsOut": "_sqladmin_163_SqlServerUserDetailsOut",
        "SslCertDetailIn": "_sqladmin_164_SslCertDetailIn",
        "SslCertDetailOut": "_sqladmin_165_SslCertDetailOut",
        "RotateServerCaContextIn": "_sqladmin_166_RotateServerCaContextIn",
        "RotateServerCaContextOut": "_sqladmin_167_RotateServerCaContextOut",
        "FlagIn": "_sqladmin_168_FlagIn",
        "FlagOut": "_sqladmin_169_FlagOut",
        "UserIn": "_sqladmin_170_UserIn",
        "UserOut": "_sqladmin_171_UserOut",
        "SqlExternalSyncSettingErrorIn": "_sqladmin_172_SqlExternalSyncSettingErrorIn",
        "SqlExternalSyncSettingErrorOut": "_sqladmin_173_SqlExternalSyncSettingErrorOut",
        "FailoverContextIn": "_sqladmin_174_FailoverContextIn",
        "FailoverContextOut": "_sqladmin_175_FailoverContextOut",
        "InsightsConfigIn": "_sqladmin_176_InsightsConfigIn",
        "InsightsConfigOut": "_sqladmin_177_InsightsConfigOut",
        "BackupRetentionSettingsIn": "_sqladmin_178_BackupRetentionSettingsIn",
        "BackupRetentionSettingsOut": "_sqladmin_179_BackupRetentionSettingsOut",
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
    types["MySqlSyncConfigIn"] = t.struct(
        {"initialSyncFlags": t.array(t.proxy(renames["SyncFlagsIn"])).optional()}
    ).named(renames["MySqlSyncConfigIn"])
    types["MySqlSyncConfigOut"] = t.struct(
        {
            "initialSyncFlags": t.array(t.proxy(renames["SyncFlagsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MySqlSyncConfigOut"])
    types["BackupReencryptionConfigIn"] = t.struct(
        {"backupLimit": t.integer().optional(), "backupType": t.string().optional()}
    ).named(renames["BackupReencryptionConfigIn"])
    types["BackupReencryptionConfigOut"] = t.struct(
        {
            "backupLimit": t.integer().optional(),
            "backupType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupReencryptionConfigOut"])
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
    types["BackupRunIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "enqueuedTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "backupKind": t.string().optional(),
            "windowStartTime": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["OperationErrorIn"]).optional(),
            "type": t.string().optional(),
            "timeZone": t.string().optional(),
            "diskEncryptionConfiguration": t.proxy(
                renames["DiskEncryptionConfigurationIn"]
            ).optional(),
            "description": t.string().optional(),
            "kind": t.string().optional(),
            "location": t.string().optional(),
            "id": t.string().optional(),
            "instance": t.string().optional(),
            "startTime": t.string().optional(),
            "diskEncryptionStatus": t.proxy(
                renames["DiskEncryptionStatusIn"]
            ).optional(),
        }
    ).named(renames["BackupRunIn"])
    types["BackupRunOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "enqueuedTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "backupKind": t.string().optional(),
            "windowStartTime": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "type": t.string().optional(),
            "timeZone": t.string().optional(),
            "diskEncryptionConfiguration": t.proxy(
                renames["DiskEncryptionConfigurationOut"]
            ).optional(),
            "description": t.string().optional(),
            "kind": t.string().optional(),
            "location": t.string().optional(),
            "id": t.string().optional(),
            "instance": t.string().optional(),
            "startTime": t.string().optional(),
            "diskEncryptionStatus": t.proxy(
                renames["DiskEncryptionStatusOut"]
            ).optional(),
        }
    ).named(renames["BackupRunOut"])
    types["UserPasswordValidationPolicyIn"] = t.struct(
        {
            "passwordExpirationDuration": t.string().optional(),
            "allowedFailedAttempts": t.integer().optional(),
            "enablePasswordVerification": t.boolean().optional(),
            "enableFailedAttemptsCheck": t.boolean().optional(),
        }
    ).named(renames["UserPasswordValidationPolicyIn"])
    types["UserPasswordValidationPolicyOut"] = t.struct(
        {
            "passwordExpirationDuration": t.string().optional(),
            "allowedFailedAttempts": t.integer().optional(),
            "status": t.proxy(renames["PasswordStatusOut"]).optional(),
            "enablePasswordVerification": t.boolean().optional(),
            "enableFailedAttemptsCheck": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserPasswordValidationPolicyOut"])
    types["BackupRunsListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["BackupRunIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["BackupRunsListResponseIn"])
    types["BackupRunsListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["BackupRunOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupRunsListResponseOut"])
    types["SqlServerDatabaseDetailsIn"] = t.struct(
        {
            "compatibilityLevel": t.integer().optional(),
            "recoveryModel": t.string().optional(),
        }
    ).named(renames["SqlServerDatabaseDetailsIn"])
    types["SqlServerDatabaseDetailsOut"] = t.struct(
        {
            "compatibilityLevel": t.integer().optional(),
            "recoveryModel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlServerDatabaseDetailsOut"])
    types["AclEntryIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "value": t.string().optional(),
            "expirationTime": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["AclEntryIn"])
    types["AclEntryOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "value": t.string().optional(),
            "expirationTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AclEntryOut"])
    types["InstancesImportRequestIn"] = t.struct(
        {"importContext": t.proxy(renames["ImportContextIn"]).optional()}
    ).named(renames["InstancesImportRequestIn"])
    types["InstancesImportRequestOut"] = t.struct(
        {
            "importContext": t.proxy(renames["ImportContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesImportRequestOut"])
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
    types["RescheduleIn"] = t.struct(
        {"rescheduleType": t.string(), "scheduleTime": t.string().optional()}
    ).named(renames["RescheduleIn"])
    types["RescheduleOut"] = t.struct(
        {
            "rescheduleType": t.string(),
            "scheduleTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RescheduleOut"])
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
    types["InstancesFailoverRequestIn"] = t.struct(
        {"failoverContext": t.proxy(renames["FailoverContextIn"]).optional()}
    ).named(renames["InstancesFailoverRequestIn"])
    types["InstancesFailoverRequestOut"] = t.struct(
        {
            "failoverContext": t.proxy(renames["FailoverContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesFailoverRequestOut"])
    types["OperationErrorIn"] = t.struct(
        {
            "code": t.string().optional(),
            "message": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["OperationErrorIn"])
    types["OperationErrorOut"] = t.struct(
        {
            "code": t.string().optional(),
            "message": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationErrorOut"])
    types["SqlInstancesStartExternalSyncRequestIn"] = t.struct(
        {
            "mysqlSyncConfig": t.proxy(renames["MySqlSyncConfigIn"]).optional(),
            "syncParallelLevel": t.string().optional(),
            "skipVerification": t.boolean().optional(),
            "syncMode": t.string().optional(),
        }
    ).named(renames["SqlInstancesStartExternalSyncRequestIn"])
    types["SqlInstancesStartExternalSyncRequestOut"] = t.struct(
        {
            "mysqlSyncConfig": t.proxy(renames["MySqlSyncConfigOut"]).optional(),
            "syncParallelLevel": t.string().optional(),
            "skipVerification": t.boolean().optional(),
            "syncMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlInstancesStartExternalSyncRequestOut"])
    types["InstancesListServerCasResponseIn"] = t.struct(
        {
            "certs": t.array(t.proxy(renames["SslCertIn"])).optional(),
            "kind": t.string().optional(),
            "activeVersion": t.string(),
        }
    ).named(renames["InstancesListServerCasResponseIn"])
    types["InstancesListServerCasResponseOut"] = t.struct(
        {
            "certs": t.array(t.proxy(renames["SslCertOut"])).optional(),
            "kind": t.string().optional(),
            "activeVersion": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesListServerCasResponseOut"])
    types["SqlServerAuditConfigIn"] = t.struct(
        {
            "retentionInterval": t.string().optional(),
            "kind": t.string().optional(),
            "uploadInterval": t.string().optional(),
            "bucket": t.string().optional(),
        }
    ).named(renames["SqlServerAuditConfigIn"])
    types["SqlServerAuditConfigOut"] = t.struct(
        {
            "retentionInterval": t.string().optional(),
            "kind": t.string().optional(),
            "uploadInterval": t.string().optional(),
            "bucket": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlServerAuditConfigOut"])
    types["AdvancedMachineFeaturesIn"] = t.struct(
        {"threadsPerCore": t.integer().optional()}
    ).named(renames["AdvancedMachineFeaturesIn"])
    types["AdvancedMachineFeaturesOut"] = t.struct(
        {
            "threadsPerCore": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvancedMachineFeaturesOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "statusDetail": t.string().optional(),
            "endTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["InstanceReferenceIn"] = t.struct(
        {
            "project": t.string().optional(),
            "region": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["InstanceReferenceIn"])
    types["InstanceReferenceOut"] = t.struct(
        {
            "project": t.string().optional(),
            "region": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceReferenceOut"])
    types["MySqlReplicaConfigurationIn"] = t.struct(
        {
            "clientCertificate": t.string().optional(),
            "username": t.string().optional(),
            "dumpFilePath": t.string().optional(),
            "caCertificate": t.string().optional(),
            "sslCipher": t.string().optional(),
            "clientKey": t.string().optional(),
            "connectRetryInterval": t.integer().optional(),
            "password": t.string().optional(),
            "masterHeartbeatPeriod": t.string().optional(),
            "verifyServerCertificate": t.boolean().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["MySqlReplicaConfigurationIn"])
    types["MySqlReplicaConfigurationOut"] = t.struct(
        {
            "clientCertificate": t.string().optional(),
            "username": t.string().optional(),
            "dumpFilePath": t.string().optional(),
            "caCertificate": t.string().optional(),
            "sslCipher": t.string().optional(),
            "clientKey": t.string().optional(),
            "connectRetryInterval": t.integer().optional(),
            "password": t.string().optional(),
            "masterHeartbeatPeriod": t.string().optional(),
            "verifyServerCertificate": t.boolean().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MySqlReplicaConfigurationOut"])
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
    types["ApiWarningIn"] = t.struct(
        {
            "code": t.string().optional(),
            "region": t.string().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["ApiWarningIn"])
    types["ApiWarningOut"] = t.struct(
        {
            "code": t.string().optional(),
            "region": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiWarningOut"])
    types["PasswordValidationPolicyIn"] = t.struct(
        {
            "complexity": t.string().optional(),
            "disallowUsernameSubstring": t.boolean().optional(),
            "enablePasswordPolicy": t.boolean().optional(),
            "passwordChangeInterval": t.string().optional(),
            "reuseInterval": t.integer().optional(),
            "minLength": t.integer().optional(),
        }
    ).named(renames["PasswordValidationPolicyIn"])
    types["PasswordValidationPolicyOut"] = t.struct(
        {
            "complexity": t.string().optional(),
            "disallowUsernameSubstring": t.boolean().optional(),
            "enablePasswordPolicy": t.boolean().optional(),
            "passwordChangeInterval": t.string().optional(),
            "reuseInterval": t.integer().optional(),
            "minLength": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PasswordValidationPolicyOut"])
    types["IpConfigurationIn"] = t.struct(
        {
            "ipv4Enabled": t.boolean().optional(),
            "allocatedIpRange": t.string().optional(),
            "privateNetwork": t.string().optional(),
            "requireSsl": t.boolean().optional(),
            "authorizedNetworks": t.array(t.proxy(renames["AclEntryIn"])).optional(),
            "enablePrivatePathForGoogleCloudServices": t.boolean().optional(),
        }
    ).named(renames["IpConfigurationIn"])
    types["IpConfigurationOut"] = t.struct(
        {
            "ipv4Enabled": t.boolean().optional(),
            "allocatedIpRange": t.string().optional(),
            "privateNetwork": t.string().optional(),
            "requireSsl": t.boolean().optional(),
            "authorizedNetworks": t.array(t.proxy(renames["AclEntryOut"])).optional(),
            "enablePrivatePathForGoogleCloudServices": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IpConfigurationOut"])
    types["SqlScheduledMaintenanceIn"] = t.struct(
        {
            "canReschedule": t.boolean().optional(),
            "canDefer": t.boolean(),
            "startTime": t.string().optional(),
            "scheduleDeadlineTime": t.string().optional(),
        }
    ).named(renames["SqlScheduledMaintenanceIn"])
    types["SqlScheduledMaintenanceOut"] = t.struct(
        {
            "canReschedule": t.boolean().optional(),
            "canDefer": t.boolean(),
            "startTime": t.string().optional(),
            "scheduleDeadlineTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlScheduledMaintenanceOut"])
    types["DemoteMasterContextIn"] = t.struct(
        {
            "skipReplicationSetup": t.boolean().optional(),
            "kind": t.string().optional(),
            "masterInstanceName": t.string().optional(),
            "replicaConfiguration": t.proxy(
                renames["DemoteMasterConfigurationIn"]
            ).optional(),
            "verifyGtidConsistency": t.boolean().optional(),
        }
    ).named(renames["DemoteMasterContextIn"])
    types["DemoteMasterContextOut"] = t.struct(
        {
            "skipReplicationSetup": t.boolean().optional(),
            "kind": t.string().optional(),
            "masterInstanceName": t.string().optional(),
            "replicaConfiguration": t.proxy(
                renames["DemoteMasterConfigurationOut"]
            ).optional(),
            "verifyGtidConsistency": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DemoteMasterContextOut"])
    types["UsersListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["UserIn"])).optional(),
        }
    ).named(renames["UsersListResponseIn"])
    types["UsersListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["UserOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsersListResponseOut"])
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
    types["OperationIn"] = t.struct(
        {
            "operationType": t.string().optional(),
            "backupContext": t.proxy(renames["BackupContextIn"]).optional(),
            "selfLink": t.string().optional(),
            "startTime": t.string().optional(),
            "user": t.string().optional(),
            "exportContext": t.proxy(renames["ExportContextIn"]).optional(),
            "importContext": t.proxy(renames["ImportContextIn"]).optional(),
            "insertTime": t.string().optional(),
            "kind": t.string().optional(),
            "targetProject": t.string().optional(),
            "targetLink": t.string(),
            "targetId": t.string().optional(),
            "endTime": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["OperationErrorsIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "operationType": t.string().optional(),
            "backupContext": t.proxy(renames["BackupContextOut"]).optional(),
            "selfLink": t.string().optional(),
            "startTime": t.string().optional(),
            "user": t.string().optional(),
            "exportContext": t.proxy(renames["ExportContextOut"]).optional(),
            "importContext": t.proxy(renames["ImportContextOut"]).optional(),
            "insertTime": t.string().optional(),
            "kind": t.string().optional(),
            "targetProject": t.string().optional(),
            "targetLink": t.string(),
            "targetId": t.string().optional(),
            "endTime": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["SslCertsInsertRequestIn"] = t.struct(
        {"commonName": t.string().optional()}
    ).named(renames["SslCertsInsertRequestIn"])
    types["SslCertsInsertRequestOut"] = t.struct(
        {
            "commonName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SslCertsInsertRequestOut"])
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
    types["SqlInstancesVerifyExternalSyncSettingsRequestIn"] = t.struct(
        {
            "verifyConnectionOnly": t.boolean().optional(),
            "syncMode": t.string().optional(),
            "mysqlSyncConfig": t.proxy(renames["MySqlSyncConfigIn"]).optional(),
            "verifyReplicationOnly": t.boolean().optional(),
        }
    ).named(renames["SqlInstancesVerifyExternalSyncSettingsRequestIn"])
    types["SqlInstancesVerifyExternalSyncSettingsRequestOut"] = t.struct(
        {
            "verifyConnectionOnly": t.boolean().optional(),
            "syncMode": t.string().optional(),
            "mysqlSyncConfig": t.proxy(renames["MySqlSyncConfigOut"]).optional(),
            "verifyReplicationOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlInstancesVerifyExternalSyncSettingsRequestOut"])
    types["GenerateEphemeralCertRequestIn"] = t.struct(
        {
            "public_key": t.string().optional(),
            "validDuration": t.string().optional(),
            "readTime": t.string().optional(),
            "access_token": t.string().optional(),
        }
    ).named(renames["GenerateEphemeralCertRequestIn"])
    types["GenerateEphemeralCertRequestOut"] = t.struct(
        {
            "public_key": t.string().optional(),
            "validDuration": t.string().optional(),
            "readTime": t.string().optional(),
            "access_token": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateEphemeralCertRequestOut"])
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
    types["SslCertsInsertResponseIn"] = t.struct(
        {
            "serverCaCert": t.proxy(renames["SslCertIn"]).optional(),
            "clientCert": t.proxy(renames["SslCertDetailIn"]).optional(),
            "kind": t.string().optional(),
            "operation": t.proxy(renames["OperationIn"]).optional(),
        }
    ).named(renames["SslCertsInsertResponseIn"])
    types["SslCertsInsertResponseOut"] = t.struct(
        {
            "serverCaCert": t.proxy(renames["SslCertOut"]).optional(),
            "clientCert": t.proxy(renames["SslCertDetailOut"]).optional(),
            "kind": t.string().optional(),
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SslCertsInsertResponseOut"])
    types["SqlInstancesGetDiskShrinkConfigResponseIn"] = t.struct(
        {
            "message": t.string().optional(),
            "minimalTargetSizeGb": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["SqlInstancesGetDiskShrinkConfigResponseIn"])
    types["SqlInstancesGetDiskShrinkConfigResponseOut"] = t.struct(
        {
            "message": t.string().optional(),
            "minimalTargetSizeGb": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlInstancesGetDiskShrinkConfigResponseOut"])
    types["SettingsIn"] = t.struct(
        {
            "settingsVersion": t.string().optional(),
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodIn"])
            ).optional(),
            "replicationType": t.string().optional(),
            "passwordValidationPolicy": t.proxy(
                renames["PasswordValidationPolicyIn"]
            ).optional(),
            "activeDirectoryConfig": t.proxy(
                renames["SqlActiveDirectoryConfigIn"]
            ).optional(),
            "activationPolicy": t.string().optional(),
            "deletionProtectionEnabled": t.boolean().optional(),
            "connectorEnforcement": t.string().optional(),
            "pricingPlan": t.string().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "timeZone": t.string().optional(),
            "advancedMachineFeatures": t.proxy(
                renames["AdvancedMachineFeaturesIn"]
            ).optional(),
            "ipConfiguration": t.proxy(renames["IpConfigurationIn"]).optional(),
            "dataDiskSizeGb": t.string().optional(),
            "backupConfiguration": t.proxy(renames["BackupConfigurationIn"]).optional(),
            "storageAutoResizeLimit": t.string().optional(),
            "locationPreference": t.proxy(renames["LocationPreferenceIn"]).optional(),
            "dataDiskType": t.string().optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowIn"]).optional(),
            "crashSafeReplicationEnabled": t.boolean().optional(),
            "tier": t.string().optional(),
            "authorizedGaeApplications": t.array(t.string()).optional(),
            "storageAutoResize": t.boolean().optional(),
            "kind": t.string().optional(),
            "availabilityType": t.string().optional(),
            "databaseFlags": t.array(t.proxy(renames["DatabaseFlagsIn"])).optional(),
            "sqlServerAuditConfig": t.proxy(
                renames["SqlServerAuditConfigIn"]
            ).optional(),
            "collation": t.string().optional(),
            "databaseReplicationEnabled": t.boolean().optional(),
            "insightsConfig": t.proxy(renames["InsightsConfigIn"]).optional(),
        }
    ).named(renames["SettingsIn"])
    types["SettingsOut"] = t.struct(
        {
            "settingsVersion": t.string().optional(),
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodOut"])
            ).optional(),
            "replicationType": t.string().optional(),
            "passwordValidationPolicy": t.proxy(
                renames["PasswordValidationPolicyOut"]
            ).optional(),
            "activeDirectoryConfig": t.proxy(
                renames["SqlActiveDirectoryConfigOut"]
            ).optional(),
            "activationPolicy": t.string().optional(),
            "deletionProtectionEnabled": t.boolean().optional(),
            "connectorEnforcement": t.string().optional(),
            "pricingPlan": t.string().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "timeZone": t.string().optional(),
            "advancedMachineFeatures": t.proxy(
                renames["AdvancedMachineFeaturesOut"]
            ).optional(),
            "ipConfiguration": t.proxy(renames["IpConfigurationOut"]).optional(),
            "dataDiskSizeGb": t.string().optional(),
            "backupConfiguration": t.proxy(
                renames["BackupConfigurationOut"]
            ).optional(),
            "storageAutoResizeLimit": t.string().optional(),
            "locationPreference": t.proxy(renames["LocationPreferenceOut"]).optional(),
            "dataDiskType": t.string().optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowOut"]).optional(),
            "crashSafeReplicationEnabled": t.boolean().optional(),
            "tier": t.string().optional(),
            "authorizedGaeApplications": t.array(t.string()).optional(),
            "storageAutoResize": t.boolean().optional(),
            "kind": t.string().optional(),
            "availabilityType": t.string().optional(),
            "databaseFlags": t.array(t.proxy(renames["DatabaseFlagsOut"])).optional(),
            "sqlServerAuditConfig": t.proxy(
                renames["SqlServerAuditConfigOut"]
            ).optional(),
            "collation": t.string().optional(),
            "databaseReplicationEnabled": t.boolean().optional(),
            "insightsConfig": t.proxy(renames["InsightsConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettingsOut"])
    types["SslCertIn"] = t.struct(
        {
            "selfLink": t.string().optional(),
            "createTime": t.string().optional(),
            "cert": t.string().optional(),
            "instance": t.string().optional(),
            "commonName": t.string().optional(),
            "sha1Fingerprint": t.string().optional(),
            "expirationTime": t.string().optional(),
            "certSerialNumber": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["SslCertIn"])
    types["SslCertOut"] = t.struct(
        {
            "selfLink": t.string().optional(),
            "createTime": t.string().optional(),
            "cert": t.string().optional(),
            "instance": t.string().optional(),
            "commonName": t.string().optional(),
            "sha1Fingerprint": t.string().optional(),
            "expirationTime": t.string().optional(),
            "certSerialNumber": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SslCertOut"])
    types["DemoteMasterConfigurationIn"] = t.struct(
        {
            "mysqlReplicaConfiguration": t.proxy(
                renames["DemoteMasterMySqlReplicaConfigurationIn"]
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["DemoteMasterConfigurationIn"])
    types["DemoteMasterConfigurationOut"] = t.struct(
        {
            "mysqlReplicaConfiguration": t.proxy(
                renames["DemoteMasterMySqlReplicaConfigurationOut"]
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DemoteMasterConfigurationOut"])
    types["SqlInstancesResetReplicaSizeRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SqlInstancesResetReplicaSizeRequestIn"])
    types["SqlInstancesResetReplicaSizeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SqlInstancesResetReplicaSizeRequestOut"])
    types["DatabaseInstanceIn"] = t.struct(
        {
            "satisfiesPzs": t.boolean().optional(),
            "gceZone": t.string().optional(),
            "serviceAccountEmailAddress": t.string().optional(),
            "region": t.string().optional(),
            "instanceType": t.string().optional(),
            "secondaryGceZone": t.string().optional(),
            "maxDiskSize": t.string().optional(),
            "serverCaCert": t.proxy(renames["SslCertIn"]).optional(),
            "settings": t.proxy(renames["SettingsIn"]).optional(),
            "outOfDiskReport": t.proxy(renames["SqlOutOfDiskReportIn"]).optional(),
            "selfLink": t.string().optional(),
            "ipAddresses": t.array(t.proxy(renames["IpMappingIn"])).optional(),
            "maintenanceVersion": t.string().optional(),
            "masterInstanceName": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "diskEncryptionStatus": t.proxy(
                renames["DiskEncryptionStatusIn"]
            ).optional(),
            "kind": t.string().optional(),
            "backendType": t.string().optional(),
            "connectionName": t.string().optional(),
            "diskEncryptionConfiguration": t.proxy(
                renames["DiskEncryptionConfigurationIn"]
            ).optional(),
            "replicaNames": t.array(t.string()).optional(),
            "databaseVersion": t.string().optional(),
            "project": t.string().optional(),
            "ipv6Address": t.string().optional(),
            "rootPassword": t.string().optional(),
            "suspensionReason": t.array(t.string()).optional(),
            "state": t.string().optional(),
            "currentDiskSize": t.string().optional(),
            "onPremisesConfiguration": t.proxy(
                renames["OnPremisesConfigurationIn"]
            ).optional(),
            "failoverReplica": t.struct(
                {"name": t.string().optional(), "available": t.boolean().optional()}
            ).optional(),
            "replicaConfiguration": t.proxy(
                renames["ReplicaConfigurationIn"]
            ).optional(),
            "scheduledMaintenance": t.proxy(
                renames["SqlScheduledMaintenanceIn"]
            ).optional(),
        }
    ).named(renames["DatabaseInstanceIn"])
    types["DatabaseInstanceOut"] = t.struct(
        {
            "satisfiesPzs": t.boolean().optional(),
            "gceZone": t.string().optional(),
            "serviceAccountEmailAddress": t.string().optional(),
            "createTime": t.string().optional(),
            "region": t.string().optional(),
            "instanceType": t.string().optional(),
            "availableMaintenanceVersions": t.array(t.string()).optional(),
            "secondaryGceZone": t.string().optional(),
            "maxDiskSize": t.string().optional(),
            "serverCaCert": t.proxy(renames["SslCertOut"]).optional(),
            "settings": t.proxy(renames["SettingsOut"]).optional(),
            "outOfDiskReport": t.proxy(renames["SqlOutOfDiskReportOut"]).optional(),
            "selfLink": t.string().optional(),
            "ipAddresses": t.array(t.proxy(renames["IpMappingOut"])).optional(),
            "maintenanceVersion": t.string().optional(),
            "masterInstanceName": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "diskEncryptionStatus": t.proxy(
                renames["DiskEncryptionStatusOut"]
            ).optional(),
            "kind": t.string().optional(),
            "backendType": t.string().optional(),
            "connectionName": t.string().optional(),
            "diskEncryptionConfiguration": t.proxy(
                renames["DiskEncryptionConfigurationOut"]
            ).optional(),
            "replicaNames": t.array(t.string()).optional(),
            "databaseVersion": t.string().optional(),
            "project": t.string().optional(),
            "ipv6Address": t.string().optional(),
            "rootPassword": t.string().optional(),
            "suspensionReason": t.array(t.string()).optional(),
            "state": t.string().optional(),
            "currentDiskSize": t.string().optional(),
            "onPremisesConfiguration": t.proxy(
                renames["OnPremisesConfigurationOut"]
            ).optional(),
            "databaseInstalledVersion": t.string().optional(),
            "failoverReplica": t.struct(
                {"name": t.string().optional(), "available": t.boolean().optional()}
            ).optional(),
            "replicaConfiguration": t.proxy(
                renames["ReplicaConfigurationOut"]
            ).optional(),
            "scheduledMaintenance": t.proxy(
                renames["SqlScheduledMaintenanceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseInstanceOut"])
    types["CloneContextIn"] = t.struct(
        {
            "binLogCoordinates": t.proxy(renames["BinLogCoordinatesIn"]).optional(),
            "allocatedIpRange": t.string().optional(),
            "pointInTime": t.string().optional(),
            "destinationInstanceName": t.string().optional(),
            "kind": t.string().optional(),
            "databaseNames": t.array(t.string()).optional(),
            "pitrTimestampMs": t.string().optional(),
        }
    ).named(renames["CloneContextIn"])
    types["CloneContextOut"] = t.struct(
        {
            "binLogCoordinates": t.proxy(renames["BinLogCoordinatesOut"]).optional(),
            "allocatedIpRange": t.string().optional(),
            "pointInTime": t.string().optional(),
            "destinationInstanceName": t.string().optional(),
            "kind": t.string().optional(),
            "databaseNames": t.array(t.string()).optional(),
            "pitrTimestampMs": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloneContextOut"])
    types["BinLogCoordinatesIn"] = t.struct(
        {
            "binLogPosition": t.string().optional(),
            "kind": t.string().optional(),
            "binLogFileName": t.string().optional(),
        }
    ).named(renames["BinLogCoordinatesIn"])
    types["BinLogCoordinatesOut"] = t.struct(
        {
            "binLogPosition": t.string().optional(),
            "kind": t.string().optional(),
            "binLogFileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BinLogCoordinatesOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["MaintenanceWindowIn"] = t.struct(
        {
            "hour": t.integer().optional(),
            "day": t.integer().optional(),
            "kind": t.string().optional(),
            "updateTrack": t.string().optional(),
        }
    ).named(renames["MaintenanceWindowIn"])
    types["MaintenanceWindowOut"] = t.struct(
        {
            "hour": t.integer().optional(),
            "day": t.integer().optional(),
            "kind": t.string().optional(),
            "updateTrack": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceWindowOut"])
    types["RestoreBackupContextIn"] = t.struct(
        {
            "project": t.string().optional(),
            "backupRunId": t.string().optional(),
            "instanceId": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["RestoreBackupContextIn"])
    types["RestoreBackupContextOut"] = t.struct(
        {
            "project": t.string().optional(),
            "backupRunId": t.string().optional(),
            "instanceId": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreBackupContextOut"])
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
    types["InstancesExportRequestIn"] = t.struct(
        {"exportContext": t.proxy(renames["ExportContextIn"]).optional()}
    ).named(renames["InstancesExportRequestIn"])
    types["InstancesExportRequestOut"] = t.struct(
        {
            "exportContext": t.proxy(renames["ExportContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesExportRequestOut"])
    types["InstancesCloneRequestIn"] = t.struct(
        {"cloneContext": t.proxy(renames["CloneContextIn"]).optional()}
    ).named(renames["InstancesCloneRequestIn"])
    types["InstancesCloneRequestOut"] = t.struct(
        {
            "cloneContext": t.proxy(renames["CloneContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesCloneRequestOut"])
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
    types["BackupConfigurationIn"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "kind": t.string().optional(),
            "transactionLogRetentionDays": t.integer().optional(),
            "location": t.string().optional(),
            "startTime": t.string().optional(),
            "binaryLogEnabled": t.boolean().optional(),
            "pointInTimeRecoveryEnabled": t.boolean().optional(),
            "replicationLogArchivingEnabled": t.boolean().optional(),
            "backupRetentionSettings": t.proxy(
                renames["BackupRetentionSettingsIn"]
            ).optional(),
        }
    ).named(renames["BackupConfigurationIn"])
    types["BackupConfigurationOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "kind": t.string().optional(),
            "transactionLogRetentionDays": t.integer().optional(),
            "location": t.string().optional(),
            "startTime": t.string().optional(),
            "binaryLogEnabled": t.boolean().optional(),
            "pointInTimeRecoveryEnabled": t.boolean().optional(),
            "replicationLogArchivingEnabled": t.boolean().optional(),
            "backupRetentionSettings": t.proxy(
                renames["BackupRetentionSettingsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupConfigurationOut"])
    types["TierIn"] = t.struct(
        {
            "RAM": t.string().optional(),
            "kind": t.string().optional(),
            "tier": t.string().optional(),
            "region": t.array(t.string()).optional(),
            "DiskQuota": t.string().optional(),
        }
    ).named(renames["TierIn"])
    types["TierOut"] = t.struct(
        {
            "RAM": t.string().optional(),
            "kind": t.string().optional(),
            "tier": t.string().optional(),
            "region": t.array(t.string()).optional(),
            "DiskQuota": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TierOut"])
    types["ExportContextIn"] = t.struct(
        {
            "fileType": t.string().optional(),
            "databases": t.array(t.string()).optional(),
            "offload": t.boolean().optional(),
            "uri": t.string().optional(),
            "bakExportOptions": t.struct(
                {
                    "striped": t.boolean().optional(),
                    "bakType": t.string().optional(),
                    "stripeCount": t.integer().optional(),
                    "copyOnly": t.boolean().optional(),
                    "differentialBase": t.boolean().optional(),
                }
            ).optional(),
            "csvExportOptions": t.struct(
                {
                    "linesTerminatedBy": t.string().optional(),
                    "quoteCharacter": t.string().optional(),
                    "selectQuery": t.string().optional(),
                    "fieldsTerminatedBy": t.string().optional(),
                    "escapeCharacter": t.string().optional(),
                }
            ).optional(),
            "sqlExportOptions": t.struct(
                {
                    "mysqlExportOptions": t.struct(
                        {"masterData": t.integer().optional()}
                    ).optional(),
                    "schemaOnly": t.boolean().optional(),
                    "tables": t.array(t.string()).optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ExportContextIn"])
    types["ExportContextOut"] = t.struct(
        {
            "fileType": t.string().optional(),
            "databases": t.array(t.string()).optional(),
            "offload": t.boolean().optional(),
            "uri": t.string().optional(),
            "bakExportOptions": t.struct(
                {
                    "striped": t.boolean().optional(),
                    "bakType": t.string().optional(),
                    "stripeCount": t.integer().optional(),
                    "copyOnly": t.boolean().optional(),
                    "differentialBase": t.boolean().optional(),
                }
            ).optional(),
            "csvExportOptions": t.struct(
                {
                    "linesTerminatedBy": t.string().optional(),
                    "quoteCharacter": t.string().optional(),
                    "selectQuery": t.string().optional(),
                    "fieldsTerminatedBy": t.string().optional(),
                    "escapeCharacter": t.string().optional(),
                }
            ).optional(),
            "sqlExportOptions": t.struct(
                {
                    "mysqlExportOptions": t.struct(
                        {"masterData": t.integer().optional()}
                    ).optional(),
                    "schemaOnly": t.boolean().optional(),
                    "tables": t.array(t.string()).optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportContextOut"])
    types["GenerateEphemeralCertResponseIn"] = t.struct(
        {"ephemeralCert": t.proxy(renames["SslCertIn"]).optional()}
    ).named(renames["GenerateEphemeralCertResponseIn"])
    types["GenerateEphemeralCertResponseOut"] = t.struct(
        {
            "ephemeralCert": t.proxy(renames["SslCertOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateEphemeralCertResponseOut"])
    types["ImportContextIn"] = t.struct(
        {
            "fileType": t.string().optional(),
            "uri": t.string().optional(),
            "importUser": t.string().optional(),
            "kind": t.string().optional(),
            "database": t.string().optional(),
            "csvImportOptions": t.struct(
                {
                    "quoteCharacter": t.string().optional(),
                    "linesTerminatedBy": t.string().optional(),
                    "escapeCharacter": t.string().optional(),
                    "table": t.string().optional(),
                    "columns": t.array(t.string()).optional(),
                    "fieldsTerminatedBy": t.string().optional(),
                }
            ).optional(),
            "bakImportOptions": t.struct(
                {
                    "recoveryOnly": t.boolean().optional(),
                    "striped": t.boolean().optional(),
                    "encryptionOptions": t.struct(
                        {
                            "certPath": t.string().optional(),
                            "pvkPassword": t.string().optional(),
                            "pvkPath": t.string().optional(),
                        }
                    ),
                    "bakType": t.string().optional(),
                    "noRecovery": t.boolean().optional(),
                }
            ).optional(),
        }
    ).named(renames["ImportContextIn"])
    types["ImportContextOut"] = t.struct(
        {
            "fileType": t.string().optional(),
            "uri": t.string().optional(),
            "importUser": t.string().optional(),
            "kind": t.string().optional(),
            "database": t.string().optional(),
            "csvImportOptions": t.struct(
                {
                    "quoteCharacter": t.string().optional(),
                    "linesTerminatedBy": t.string().optional(),
                    "escapeCharacter": t.string().optional(),
                    "table": t.string().optional(),
                    "columns": t.array(t.string()).optional(),
                    "fieldsTerminatedBy": t.string().optional(),
                }
            ).optional(),
            "bakImportOptions": t.struct(
                {
                    "recoveryOnly": t.boolean().optional(),
                    "striped": t.boolean().optional(),
                    "encryptionOptions": t.struct(
                        {
                            "certPath": t.string().optional(),
                            "pvkPassword": t.string().optional(),
                            "pvkPath": t.string().optional(),
                        }
                    ),
                    "bakType": t.string().optional(),
                    "noRecovery": t.boolean().optional(),
                }
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportContextOut"])
    types["OperationsListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["OperationIn"])).optional(),
        }
    ).named(renames["OperationsListResponseIn"])
    types["OperationsListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["OperationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationsListResponseOut"])
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
    types["LocationPreferenceIn"] = t.struct(
        {
            "secondaryZone": t.string().optional(),
            "followGaeApplication": t.string().optional(),
            "zone": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["LocationPreferenceIn"])
    types["LocationPreferenceOut"] = t.struct(
        {
            "secondaryZone": t.string().optional(),
            "followGaeApplication": t.string().optional(),
            "zone": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationPreferenceOut"])
    types["PerformDiskShrinkContextIn"] = t.struct(
        {"targetSizeGb": t.string().optional()}
    ).named(renames["PerformDiskShrinkContextIn"])
    types["PerformDiskShrinkContextOut"] = t.struct(
        {
            "targetSizeGb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerformDiskShrinkContextOut"])
    types["SqlInstancesRescheduleMaintenanceRequestBodyIn"] = t.struct(
        {"reschedule": t.proxy(renames["RescheduleIn"])}
    ).named(renames["SqlInstancesRescheduleMaintenanceRequestBodyIn"])
    types["SqlInstancesRescheduleMaintenanceRequestBodyOut"] = t.struct(
        {
            "reschedule": t.proxy(renames["RescheduleOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlInstancesRescheduleMaintenanceRequestBodyOut"])
    types["DatabaseIn"] = t.struct(
        {
            "selfLink": t.string().optional(),
            "etag": t.string().optional(),
            "sqlserverDatabaseDetails": t.proxy(renames["SqlServerDatabaseDetailsIn"]),
            "name": t.string().optional(),
            "charset": t.string().optional(),
            "instance": t.string().optional(),
            "kind": t.string().optional(),
            "project": t.string().optional(),
            "collation": t.string().optional(),
        }
    ).named(renames["DatabaseIn"])
    types["DatabaseOut"] = t.struct(
        {
            "selfLink": t.string().optional(),
            "etag": t.string().optional(),
            "sqlserverDatabaseDetails": t.proxy(renames["SqlServerDatabaseDetailsOut"]),
            "name": t.string().optional(),
            "charset": t.string().optional(),
            "instance": t.string().optional(),
            "kind": t.string().optional(),
            "project": t.string().optional(),
            "collation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseOut"])
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
    types["ConnectSettingsIn"] = t.struct(
        {
            "dnsName": t.string().optional(),
            "backendType": t.string().optional(),
            "databaseVersion": t.string().optional(),
            "kind": t.string().optional(),
            "ipAddresses": t.array(t.proxy(renames["IpMappingIn"])).optional(),
            "region": t.string().optional(),
            "serverCaCert": t.proxy(renames["SslCertIn"]).optional(),
        }
    ).named(renames["ConnectSettingsIn"])
    types["ConnectSettingsOut"] = t.struct(
        {
            "dnsName": t.string().optional(),
            "backendType": t.string().optional(),
            "databaseVersion": t.string().optional(),
            "kind": t.string().optional(),
            "ipAddresses": t.array(t.proxy(renames["IpMappingOut"])).optional(),
            "region": t.string().optional(),
            "serverCaCert": t.proxy(renames["SslCertOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectSettingsOut"])
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
    types["InstancesTruncateLogRequestIn"] = t.struct(
        {"truncateLogContext": t.proxy(renames["TruncateLogContextIn"]).optional()}
    ).named(renames["InstancesTruncateLogRequestIn"])
    types["InstancesTruncateLogRequestOut"] = t.struct(
        {
            "truncateLogContext": t.proxy(renames["TruncateLogContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesTruncateLogRequestOut"])
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
    types["DemoteMasterMySqlReplicaConfigurationIn"] = t.struct(
        {
            "clientKey": t.string().optional(),
            "password": t.string().optional(),
            "username": t.string().optional(),
            "caCertificate": t.string().optional(),
            "kind": t.string().optional(),
            "clientCertificate": t.string().optional(),
        }
    ).named(renames["DemoteMasterMySqlReplicaConfigurationIn"])
    types["DemoteMasterMySqlReplicaConfigurationOut"] = t.struct(
        {
            "clientKey": t.string().optional(),
            "password": t.string().optional(),
            "username": t.string().optional(),
            "caCertificate": t.string().optional(),
            "kind": t.string().optional(),
            "clientCertificate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DemoteMasterMySqlReplicaConfigurationOut"])
    types["DenyMaintenancePeriodIn"] = t.struct(
        {
            "time": t.string().optional(),
            "endDate": t.string().optional(),
            "startDate": t.string().optional(),
        }
    ).named(renames["DenyMaintenancePeriodIn"])
    types["DenyMaintenancePeriodOut"] = t.struct(
        {
            "time": t.string().optional(),
            "endDate": t.string().optional(),
            "startDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DenyMaintenancePeriodOut"])
    types["OnPremisesConfigurationIn"] = t.struct(
        {
            "clientCertificate": t.string().optional(),
            "caCertificate": t.string().optional(),
            "kind": t.string().optional(),
            "clientKey": t.string().optional(),
            "username": t.string().optional(),
            "sourceInstance": t.proxy(renames["InstanceReferenceIn"]).optional(),
            "dumpFilePath": t.string().optional(),
            "password": t.string().optional(),
            "hostPort": t.string().optional(),
        }
    ).named(renames["OnPremisesConfigurationIn"])
    types["OnPremisesConfigurationOut"] = t.struct(
        {
            "clientCertificate": t.string().optional(),
            "caCertificate": t.string().optional(),
            "kind": t.string().optional(),
            "clientKey": t.string().optional(),
            "username": t.string().optional(),
            "sourceInstance": t.proxy(renames["InstanceReferenceOut"]).optional(),
            "dumpFilePath": t.string().optional(),
            "password": t.string().optional(),
            "hostPort": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OnPremisesConfigurationOut"])
    types["InstancesReencryptRequestIn"] = t.struct(
        {
            "backupReencryptionConfig": t.proxy(
                renames["BackupReencryptionConfigIn"]
            ).optional()
        }
    ).named(renames["InstancesReencryptRequestIn"])
    types["InstancesReencryptRequestOut"] = t.struct(
        {
            "backupReencryptionConfig": t.proxy(
                renames["BackupReencryptionConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesReencryptRequestOut"])
    types["InstancesListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["DatabaseInstanceIn"])).optional(),
            "warnings": t.array(t.proxy(renames["ApiWarningIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["InstancesListResponseIn"])
    types["InstancesListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["DatabaseInstanceOut"])).optional(),
            "warnings": t.array(t.proxy(renames["ApiWarningOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesListResponseOut"])
    types["SqlServerUserDetailsIn"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "serverRoles": t.array(t.string()).optional(),
        }
    ).named(renames["SqlServerUserDetailsIn"])
    types["SqlServerUserDetailsOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "serverRoles": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlServerUserDetailsOut"])
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
    types["RotateServerCaContextIn"] = t.struct(
        {"kind": t.string().optional(), "nextVersion": t.string().optional()}
    ).named(renames["RotateServerCaContextIn"])
    types["RotateServerCaContextOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RotateServerCaContextOut"])
    types["FlagIn"] = t.struct(
        {
            "maxValue": t.string().optional(),
            "allowedIntValues": t.array(t.string()).optional(),
            "allowedStringValues": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "requiresRestart": t.boolean().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "appliesTo": t.array(t.string()).optional(),
            "inBeta": t.boolean().optional(),
            "minValue": t.string().optional(),
        }
    ).named(renames["FlagIn"])
    types["FlagOut"] = t.struct(
        {
            "maxValue": t.string().optional(),
            "allowedIntValues": t.array(t.string()).optional(),
            "allowedStringValues": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "requiresRestart": t.boolean().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "appliesTo": t.array(t.string()).optional(),
            "inBeta": t.boolean().optional(),
            "minValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FlagOut"])
    types["UserIn"] = t.struct(
        {
            "type": t.string().optional(),
            "password": t.string().optional(),
            "sqlserverUserDetails": t.proxy(renames["SqlServerUserDetailsIn"]),
            "dualPasswordType": t.string().optional(),
            "host": t.string().optional(),
            "instance": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "passwordPolicy": t.proxy(
                renames["UserPasswordValidationPolicyIn"]
            ).optional(),
            "project": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "type": t.string().optional(),
            "password": t.string().optional(),
            "sqlserverUserDetails": t.proxy(renames["SqlServerUserDetailsOut"]),
            "dualPasswordType": t.string().optional(),
            "host": t.string().optional(),
            "instance": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "passwordPolicy": t.proxy(
                renames["UserPasswordValidationPolicyOut"]
            ).optional(),
            "project": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["SqlExternalSyncSettingErrorIn"] = t.struct(
        {
            "detail": t.string().optional(),
            "kind": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["SqlExternalSyncSettingErrorIn"])
    types["SqlExternalSyncSettingErrorOut"] = t.struct(
        {
            "detail": t.string().optional(),
            "kind": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlExternalSyncSettingErrorOut"])
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
    types["InsightsConfigIn"] = t.struct(
        {
            "queryStringLength": t.integer().optional(),
            "recordApplicationTags": t.boolean().optional(),
            "queryPlansPerMinute": t.integer().optional(),
            "queryInsightsEnabled": t.boolean().optional(),
            "recordClientAddress": t.boolean().optional(),
        }
    ).named(renames["InsightsConfigIn"])
    types["InsightsConfigOut"] = t.struct(
        {
            "queryStringLength": t.integer().optional(),
            "recordApplicationTags": t.boolean().optional(),
            "queryPlansPerMinute": t.integer().optional(),
            "queryInsightsEnabled": t.boolean().optional(),
            "recordClientAddress": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsightsConfigOut"])
    types["BackupRetentionSettingsIn"] = t.struct(
        {
            "retentionUnit": t.string().optional(),
            "retainedBackups": t.integer().optional(),
        }
    ).named(renames["BackupRetentionSettingsIn"])
    types["BackupRetentionSettingsOut"] = t.struct(
        {
            "retentionUnit": t.string().optional(),
            "retainedBackups": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupRetentionSettingsOut"])

    functions = {}
    functions["projectsInstancesStartExternalSync"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/getDiskShrinkConfig",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
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
                "project": t.string().optional(),
                "instance": t.string().optional(),
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
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SqlInstancesGetDiskShrinkConfigResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesResetReplicaSize"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/getDiskShrinkConfig",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
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
                "project": t.string().optional(),
                "instance": t.string().optional(),
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
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SqlInstancesGetDiskShrinkConfigResponseOut"]),
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
    functions["backupRunsDelete"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/backupRuns",
        t.struct(
            {
                "project": t.string().optional(),
                "pageToken": t.string().optional(),
                "instance": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BackupRunsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["backupRunsInsert"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/backupRuns",
        t.struct(
            {
                "project": t.string().optional(),
                "pageToken": t.string().optional(),
                "instance": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BackupRunsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["backupRunsGet"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/backupRuns",
        t.struct(
            {
                "project": t.string().optional(),
                "pageToken": t.string().optional(),
                "instance": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BackupRunsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["backupRunsList"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/backupRuns",
        t.struct(
            {
                "project": t.string().optional(),
                "pageToken": t.string().optional(),
                "instance": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BackupRunsListResponseOut"]),
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
    functions["instancesGet"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/export",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "exportContext": t.proxy(renames["ExportContextIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesDemoteMaster"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/export",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "exportContext": t.proxy(renames["ExportContextIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesUpdate"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/export",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "exportContext": t.proxy(renames["ExportContextIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesFailover"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/export",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "exportContext": t.proxy(renames["ExportContextIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesClone"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/export",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "exportContext": t.proxy(renames["ExportContextIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesList"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/export",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "exportContext": t.proxy(renames["ExportContextIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesPromoteReplica"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/export",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "exportContext": t.proxy(renames["ExportContextIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesRestoreBackup"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/export",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "exportContext": t.proxy(renames["ExportContextIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesRotateServerCa"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/export",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "exportContext": t.proxy(renames["ExportContextIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesReencrypt"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/export",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "exportContext": t.proxy(renames["ExportContextIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesListServerCas"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/export",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "exportContext": t.proxy(renames["ExportContextIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesInsert"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/export",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "exportContext": t.proxy(renames["ExportContextIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesAddServerCa"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/export",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "exportContext": t.proxy(renames["ExportContextIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesResetSslConfig"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/export",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "exportContext": t.proxy(renames["ExportContextIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesTruncateLog"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/export",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "exportContext": t.proxy(renames["ExportContextIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesRestart"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/export",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "exportContext": t.proxy(renames["ExportContextIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesPatch"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/export",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "exportContext": t.proxy(renames["ExportContextIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesStopReplica"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/export",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "exportContext": t.proxy(renames["ExportContextIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesDelete"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/export",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "exportContext": t.proxy(renames["ExportContextIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesStartReplica"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/export",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "exportContext": t.proxy(renames["ExportContextIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesImport"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/export",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "exportContext": t.proxy(renames["ExportContextIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesExport"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/export",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "exportContext": t.proxy(renames["ExportContextIn"]).optional(),
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
                "type": t.string().optional(),
                "password": t.string().optional(),
                "sqlserverUserDetails": t.proxy(renames["SqlServerUserDetailsIn"]),
                "dualPasswordType": t.string().optional(),
                "host": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "passwordPolicy": t.proxy(
                    renames["UserPasswordValidationPolicyIn"]
                ).optional(),
                "etag": t.string().optional(),
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
                "type": t.string().optional(),
                "password": t.string().optional(),
                "sqlserverUserDetails": t.proxy(renames["SqlServerUserDetailsIn"]),
                "dualPasswordType": t.string().optional(),
                "host": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "passwordPolicy": t.proxy(
                    renames["UserPasswordValidationPolicyIn"]
                ).optional(),
                "etag": t.string().optional(),
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
                "type": t.string().optional(),
                "password": t.string().optional(),
                "sqlserverUserDetails": t.proxy(renames["SqlServerUserDetailsIn"]),
                "dualPasswordType": t.string().optional(),
                "host": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "passwordPolicy": t.proxy(
                    renames["UserPasswordValidationPolicyIn"]
                ).optional(),
                "etag": t.string().optional(),
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
                "type": t.string().optional(),
                "password": t.string().optional(),
                "sqlserverUserDetails": t.proxy(renames["SqlServerUserDetailsIn"]),
                "dualPasswordType": t.string().optional(),
                "host": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "passwordPolicy": t.proxy(
                    renames["UserPasswordValidationPolicyIn"]
                ).optional(),
                "etag": t.string().optional(),
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
                "type": t.string().optional(),
                "password": t.string().optional(),
                "sqlserverUserDetails": t.proxy(renames["SqlServerUserDetailsIn"]),
                "dualPasswordType": t.string().optional(),
                "host": t.string().optional(),
                "kind": t.string().optional(),
                "name": t.string().optional(),
                "passwordPolicy": t.proxy(
                    renames["UserPasswordValidationPolicyIn"]
                ).optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sslCertsInsert"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/createEphemeral",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "public_key": t.string().optional(),
                "access_token": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SslCertOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sslCertsDelete"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/createEphemeral",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "public_key": t.string().optional(),
                "access_token": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SslCertOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sslCertsList"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/createEphemeral",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "public_key": t.string().optional(),
                "access_token": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SslCertOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sslCertsGet"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/createEphemeral",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "public_key": t.string().optional(),
                "access_token": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SslCertOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sslCertsCreateEphemeral"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}/createEphemeral",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "public_key": t.string().optional(),
                "access_token": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SslCertOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsList"] = sqladmin.post(
        "v1/projects/{project}/operations/{operation}/cancel",
        t.struct(
            {
                "operation": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = sqladmin.post(
        "v1/projects/{project}/operations/{operation}/cancel",
        t.struct(
            {
                "operation": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsCancel"] = sqladmin.post(
        "v1/projects/{project}/operations/{operation}/cancel",
        t.struct(
            {
                "operation": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["databasesUpdate"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/databases/{database}",
        t.struct(
            {
                "instance": t.string().optional(),
                "database": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatabaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["databasesList"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/databases/{database}",
        t.struct(
            {
                "instance": t.string().optional(),
                "database": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatabaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["databasesDelete"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/databases/{database}",
        t.struct(
            {
                "instance": t.string().optional(),
                "database": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatabaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["databasesInsert"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/databases/{database}",
        t.struct(
            {
                "instance": t.string().optional(),
                "database": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatabaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["databasesPatch"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/databases/{database}",
        t.struct(
            {
                "instance": t.string().optional(),
                "database": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatabaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["databasesGet"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/databases/{database}",
        t.struct(
            {
                "instance": t.string().optional(),
                "database": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatabaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["connectGet"] = sqladmin.post(
        "v1/projects/{project}/instances/{instance}:generateEphemeralCert",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "public_key": t.string().optional(),
                "validDuration": t.string().optional(),
                "readTime": t.string().optional(),
                "access_token": t.string().optional(),
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
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "public_key": t.string().optional(),
                "validDuration": t.string().optional(),
                "readTime": t.string().optional(),
                "access_token": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateEphemeralCertResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="sqladmin", renames=renames, types=Box(types), functions=Box(functions)
    )
