from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_sqladmin() -> Import:
    sqladmin = HTTPRuntime("https://sqladmin.googleapis.com/")

    renames = {
        "ErrorResponse": "_sqladmin_1_ErrorResponse",
        "SettingsIn": "_sqladmin_2_SettingsIn",
        "SettingsOut": "_sqladmin_3_SettingsOut",
        "SslCertIn": "_sqladmin_4_SslCertIn",
        "SslCertOut": "_sqladmin_5_SslCertOut",
        "FlagIn": "_sqladmin_6_FlagIn",
        "FlagOut": "_sqladmin_7_FlagOut",
        "DemoteMasterConfigurationIn": "_sqladmin_8_DemoteMasterConfigurationIn",
        "DemoteMasterConfigurationOut": "_sqladmin_9_DemoteMasterConfigurationOut",
        "DiskEncryptionStatusIn": "_sqladmin_10_DiskEncryptionStatusIn",
        "DiskEncryptionStatusOut": "_sqladmin_11_DiskEncryptionStatusOut",
        "AdvancedMachineFeaturesIn": "_sqladmin_12_AdvancedMachineFeaturesIn",
        "AdvancedMachineFeaturesOut": "_sqladmin_13_AdvancedMachineFeaturesOut",
        "ConnectSettingsIn": "_sqladmin_14_ConnectSettingsIn",
        "ConnectSettingsOut": "_sqladmin_15_ConnectSettingsOut",
        "CloneContextIn": "_sqladmin_16_CloneContextIn",
        "CloneContextOut": "_sqladmin_17_CloneContextOut",
        "InstancesRestoreBackupRequestIn": "_sqladmin_18_InstancesRestoreBackupRequestIn",
        "InstancesRestoreBackupRequestOut": "_sqladmin_19_InstancesRestoreBackupRequestOut",
        "SqlInstancesRescheduleMaintenanceRequestBodyIn": "_sqladmin_20_SqlInstancesRescheduleMaintenanceRequestBodyIn",
        "SqlInstancesRescheduleMaintenanceRequestBodyOut": "_sqladmin_21_SqlInstancesRescheduleMaintenanceRequestBodyOut",
        "RotateServerCaContextIn": "_sqladmin_22_RotateServerCaContextIn",
        "RotateServerCaContextOut": "_sqladmin_23_RotateServerCaContextOut",
        "LocationPreferenceIn": "_sqladmin_24_LocationPreferenceIn",
        "LocationPreferenceOut": "_sqladmin_25_LocationPreferenceOut",
        "BackupRetentionSettingsIn": "_sqladmin_26_BackupRetentionSettingsIn",
        "BackupRetentionSettingsOut": "_sqladmin_27_BackupRetentionSettingsOut",
        "DatabaseIn": "_sqladmin_28_DatabaseIn",
        "DatabaseOut": "_sqladmin_29_DatabaseOut",
        "PasswordStatusIn": "_sqladmin_30_PasswordStatusIn",
        "PasswordStatusOut": "_sqladmin_31_PasswordStatusOut",
        "SqlInstancesVerifyExternalSyncSettingsResponseIn": "_sqladmin_32_SqlInstancesVerifyExternalSyncSettingsResponseIn",
        "SqlInstancesVerifyExternalSyncSettingsResponseOut": "_sqladmin_33_SqlInstancesVerifyExternalSyncSettingsResponseOut",
        "InstancesRotateServerCaRequestIn": "_sqladmin_34_InstancesRotateServerCaRequestIn",
        "InstancesRotateServerCaRequestOut": "_sqladmin_35_InstancesRotateServerCaRequestOut",
        "SyncFlagsIn": "_sqladmin_36_SyncFlagsIn",
        "SyncFlagsOut": "_sqladmin_37_SyncFlagsOut",
        "SslCertsInsertResponseIn": "_sqladmin_38_SslCertsInsertResponseIn",
        "SslCertsInsertResponseOut": "_sqladmin_39_SslCertsInsertResponseOut",
        "InstanceReferenceIn": "_sqladmin_40_InstanceReferenceIn",
        "InstanceReferenceOut": "_sqladmin_41_InstanceReferenceOut",
        "DiskEncryptionConfigurationIn": "_sqladmin_42_DiskEncryptionConfigurationIn",
        "DiskEncryptionConfigurationOut": "_sqladmin_43_DiskEncryptionConfigurationOut",
        "BackupRunsListResponseIn": "_sqladmin_44_BackupRunsListResponseIn",
        "BackupRunsListResponseOut": "_sqladmin_45_BackupRunsListResponseOut",
        "TierIn": "_sqladmin_46_TierIn",
        "TierOut": "_sqladmin_47_TierOut",
        "UserPasswordValidationPolicyIn": "_sqladmin_48_UserPasswordValidationPolicyIn",
        "UserPasswordValidationPolicyOut": "_sqladmin_49_UserPasswordValidationPolicyOut",
        "InstancesListServerCasResponseIn": "_sqladmin_50_InstancesListServerCasResponseIn",
        "InstancesListServerCasResponseOut": "_sqladmin_51_InstancesListServerCasResponseOut",
        "SslCertsListResponseIn": "_sqladmin_52_SslCertsListResponseIn",
        "SslCertsListResponseOut": "_sqladmin_53_SslCertsListResponseOut",
        "DatabasesListResponseIn": "_sqladmin_54_DatabasesListResponseIn",
        "DatabasesListResponseOut": "_sqladmin_55_DatabasesListResponseOut",
        "UserIn": "_sqladmin_56_UserIn",
        "UserOut": "_sqladmin_57_UserOut",
        "SslCertsCreateEphemeralRequestIn": "_sqladmin_58_SslCertsCreateEphemeralRequestIn",
        "SslCertsCreateEphemeralRequestOut": "_sqladmin_59_SslCertsCreateEphemeralRequestOut",
        "BinLogCoordinatesIn": "_sqladmin_60_BinLogCoordinatesIn",
        "BinLogCoordinatesOut": "_sqladmin_61_BinLogCoordinatesOut",
        "DemoteMasterMySqlReplicaConfigurationIn": "_sqladmin_62_DemoteMasterMySqlReplicaConfigurationIn",
        "DemoteMasterMySqlReplicaConfigurationOut": "_sqladmin_63_DemoteMasterMySqlReplicaConfigurationOut",
        "ReplicaConfigurationIn": "_sqladmin_64_ReplicaConfigurationIn",
        "ReplicaConfigurationOut": "_sqladmin_65_ReplicaConfigurationOut",
        "SslCertsInsertRequestIn": "_sqladmin_66_SslCertsInsertRequestIn",
        "SslCertsInsertRequestOut": "_sqladmin_67_SslCertsInsertRequestOut",
        "TruncateLogContextIn": "_sqladmin_68_TruncateLogContextIn",
        "TruncateLogContextOut": "_sqladmin_69_TruncateLogContextOut",
        "SqlInstancesGetDiskShrinkConfigResponseIn": "_sqladmin_70_SqlInstancesGetDiskShrinkConfigResponseIn",
        "SqlInstancesGetDiskShrinkConfigResponseOut": "_sqladmin_71_SqlInstancesGetDiskShrinkConfigResponseOut",
        "MaintenanceWindowIn": "_sqladmin_72_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_sqladmin_73_MaintenanceWindowOut",
        "RescheduleIn": "_sqladmin_74_RescheduleIn",
        "RescheduleOut": "_sqladmin_75_RescheduleOut",
        "DatabaseInstanceIn": "_sqladmin_76_DatabaseInstanceIn",
        "DatabaseInstanceOut": "_sqladmin_77_DatabaseInstanceOut",
        "InstancesDemoteMasterRequestIn": "_sqladmin_78_InstancesDemoteMasterRequestIn",
        "InstancesDemoteMasterRequestOut": "_sqladmin_79_InstancesDemoteMasterRequestOut",
        "ExportContextIn": "_sqladmin_80_ExportContextIn",
        "ExportContextOut": "_sqladmin_81_ExportContextOut",
        "IpConfigurationIn": "_sqladmin_82_IpConfigurationIn",
        "IpConfigurationOut": "_sqladmin_83_IpConfigurationOut",
        "RestoreBackupContextIn": "_sqladmin_84_RestoreBackupContextIn",
        "RestoreBackupContextOut": "_sqladmin_85_RestoreBackupContextOut",
        "AclEntryIn": "_sqladmin_86_AclEntryIn",
        "AclEntryOut": "_sqladmin_87_AclEntryOut",
        "FlagsListResponseIn": "_sqladmin_88_FlagsListResponseIn",
        "FlagsListResponseOut": "_sqladmin_89_FlagsListResponseOut",
        "SqlExternalSyncSettingErrorIn": "_sqladmin_90_SqlExternalSyncSettingErrorIn",
        "SqlExternalSyncSettingErrorOut": "_sqladmin_91_SqlExternalSyncSettingErrorOut",
        "OperationErrorIn": "_sqladmin_92_OperationErrorIn",
        "OperationErrorOut": "_sqladmin_93_OperationErrorOut",
        "OperationIn": "_sqladmin_94_OperationIn",
        "OperationOut": "_sqladmin_95_OperationOut",
        "DemoteMasterContextIn": "_sqladmin_96_DemoteMasterContextIn",
        "DemoteMasterContextOut": "_sqladmin_97_DemoteMasterContextOut",
        "FailoverContextIn": "_sqladmin_98_FailoverContextIn",
        "FailoverContextOut": "_sqladmin_99_FailoverContextOut",
        "SqlServerUserDetailsIn": "_sqladmin_100_SqlServerUserDetailsIn",
        "SqlServerUserDetailsOut": "_sqladmin_101_SqlServerUserDetailsOut",
        "MySqlSyncConfigIn": "_sqladmin_102_MySqlSyncConfigIn",
        "MySqlSyncConfigOut": "_sqladmin_103_MySqlSyncConfigOut",
        "OperationsListResponseIn": "_sqladmin_104_OperationsListResponseIn",
        "OperationsListResponseOut": "_sqladmin_105_OperationsListResponseOut",
        "PasswordValidationPolicyIn": "_sqladmin_106_PasswordValidationPolicyIn",
        "PasswordValidationPolicyOut": "_sqladmin_107_PasswordValidationPolicyOut",
        "OperationErrorsIn": "_sqladmin_108_OperationErrorsIn",
        "OperationErrorsOut": "_sqladmin_109_OperationErrorsOut",
        "SqlInstancesStartExternalSyncRequestIn": "_sqladmin_110_SqlInstancesStartExternalSyncRequestIn",
        "SqlInstancesStartExternalSyncRequestOut": "_sqladmin_111_SqlInstancesStartExternalSyncRequestOut",
        "OnPremisesConfigurationIn": "_sqladmin_112_OnPremisesConfigurationIn",
        "OnPremisesConfigurationOut": "_sqladmin_113_OnPremisesConfigurationOut",
        "InsightsConfigIn": "_sqladmin_114_InsightsConfigIn",
        "InsightsConfigOut": "_sqladmin_115_InsightsConfigOut",
        "GenerateEphemeralCertResponseIn": "_sqladmin_116_GenerateEphemeralCertResponseIn",
        "GenerateEphemeralCertResponseOut": "_sqladmin_117_GenerateEphemeralCertResponseOut",
        "InstancesListResponseIn": "_sqladmin_118_InstancesListResponseIn",
        "InstancesListResponseOut": "_sqladmin_119_InstancesListResponseOut",
        "TiersListResponseIn": "_sqladmin_120_TiersListResponseIn",
        "TiersListResponseOut": "_sqladmin_121_TiersListResponseOut",
        "SqlServerDatabaseDetailsIn": "_sqladmin_122_SqlServerDatabaseDetailsIn",
        "SqlServerDatabaseDetailsOut": "_sqladmin_123_SqlServerDatabaseDetailsOut",
        "BackupConfigurationIn": "_sqladmin_124_BackupConfigurationIn",
        "BackupConfigurationOut": "_sqladmin_125_BackupConfigurationOut",
        "BackupRunIn": "_sqladmin_126_BackupRunIn",
        "BackupRunOut": "_sqladmin_127_BackupRunOut",
        "SqlActiveDirectoryConfigIn": "_sqladmin_128_SqlActiveDirectoryConfigIn",
        "SqlActiveDirectoryConfigOut": "_sqladmin_129_SqlActiveDirectoryConfigOut",
        "SqlServerAuditConfigIn": "_sqladmin_130_SqlServerAuditConfigIn",
        "SqlServerAuditConfigOut": "_sqladmin_131_SqlServerAuditConfigOut",
        "PerformDiskShrinkContextIn": "_sqladmin_132_PerformDiskShrinkContextIn",
        "PerformDiskShrinkContextOut": "_sqladmin_133_PerformDiskShrinkContextOut",
        "GenerateEphemeralCertRequestIn": "_sqladmin_134_GenerateEphemeralCertRequestIn",
        "GenerateEphemeralCertRequestOut": "_sqladmin_135_GenerateEphemeralCertRequestOut",
        "DatabaseFlagsIn": "_sqladmin_136_DatabaseFlagsIn",
        "DatabaseFlagsOut": "_sqladmin_137_DatabaseFlagsOut",
        "InstancesImportRequestIn": "_sqladmin_138_InstancesImportRequestIn",
        "InstancesImportRequestOut": "_sqladmin_139_InstancesImportRequestOut",
        "SqlOutOfDiskReportIn": "_sqladmin_140_SqlOutOfDiskReportIn",
        "SqlOutOfDiskReportOut": "_sqladmin_141_SqlOutOfDiskReportOut",
        "InstancesFailoverRequestIn": "_sqladmin_142_InstancesFailoverRequestIn",
        "InstancesFailoverRequestOut": "_sqladmin_143_InstancesFailoverRequestOut",
        "SslCertDetailIn": "_sqladmin_144_SslCertDetailIn",
        "SslCertDetailOut": "_sqladmin_145_SslCertDetailOut",
        "SqlInstancesVerifyExternalSyncSettingsRequestIn": "_sqladmin_146_SqlInstancesVerifyExternalSyncSettingsRequestIn",
        "SqlInstancesVerifyExternalSyncSettingsRequestOut": "_sqladmin_147_SqlInstancesVerifyExternalSyncSettingsRequestOut",
        "ApiWarningIn": "_sqladmin_148_ApiWarningIn",
        "ApiWarningOut": "_sqladmin_149_ApiWarningOut",
        "OperationMetadataIn": "_sqladmin_150_OperationMetadataIn",
        "OperationMetadataOut": "_sqladmin_151_OperationMetadataOut",
        "InstancesTruncateLogRequestIn": "_sqladmin_152_InstancesTruncateLogRequestIn",
        "InstancesTruncateLogRequestOut": "_sqladmin_153_InstancesTruncateLogRequestOut",
        "IpMappingIn": "_sqladmin_154_IpMappingIn",
        "IpMappingOut": "_sqladmin_155_IpMappingOut",
        "DenyMaintenancePeriodIn": "_sqladmin_156_DenyMaintenancePeriodIn",
        "DenyMaintenancePeriodOut": "_sqladmin_157_DenyMaintenancePeriodOut",
        "BackupContextIn": "_sqladmin_158_BackupContextIn",
        "BackupContextOut": "_sqladmin_159_BackupContextOut",
        "MySqlReplicaConfigurationIn": "_sqladmin_160_MySqlReplicaConfigurationIn",
        "MySqlReplicaConfigurationOut": "_sqladmin_161_MySqlReplicaConfigurationOut",
        "ImportContextIn": "_sqladmin_162_ImportContextIn",
        "ImportContextOut": "_sqladmin_163_ImportContextOut",
        "SqlInstancesResetReplicaSizeRequestIn": "_sqladmin_164_SqlInstancesResetReplicaSizeRequestIn",
        "SqlInstancesResetReplicaSizeRequestOut": "_sqladmin_165_SqlInstancesResetReplicaSizeRequestOut",
        "InstancesExportRequestIn": "_sqladmin_166_InstancesExportRequestIn",
        "InstancesExportRequestOut": "_sqladmin_167_InstancesExportRequestOut",
        "UsersListResponseIn": "_sqladmin_168_UsersListResponseIn",
        "UsersListResponseOut": "_sqladmin_169_UsersListResponseOut",
        "InstancesCloneRequestIn": "_sqladmin_170_InstancesCloneRequestIn",
        "InstancesCloneRequestOut": "_sqladmin_171_InstancesCloneRequestOut",
        "SqlScheduledMaintenanceIn": "_sqladmin_172_SqlScheduledMaintenanceIn",
        "SqlScheduledMaintenanceOut": "_sqladmin_173_SqlScheduledMaintenanceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SettingsIn"] = t.struct(
        {
            "availabilityType": t.string().optional(),
            "ipConfiguration": t.proxy(renames["IpConfigurationIn"]).optional(),
            "authorizedGaeApplications": t.array(t.string()).optional(),
            "locationPreference": t.proxy(renames["LocationPreferenceIn"]).optional(),
            "timeZone": t.string().optional(),
            "settingsVersion": t.string().optional(),
            "collation": t.string().optional(),
            "sqlServerAuditConfig": t.proxy(
                renames["SqlServerAuditConfigIn"]
            ).optional(),
            "dataDiskType": t.string().optional(),
            "kind": t.string().optional(),
            "databaseFlags": t.array(t.proxy(renames["DatabaseFlagsIn"])).optional(),
            "replicationType": t.string().optional(),
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodIn"])
            ).optional(),
            "pricingPlan": t.string().optional(),
            "advancedMachineFeatures": t.proxy(
                renames["AdvancedMachineFeaturesIn"]
            ).optional(),
            "activationPolicy": t.string().optional(),
            "storageAutoResize": t.boolean().optional(),
            "databaseReplicationEnabled": t.boolean().optional(),
            "backupConfiguration": t.proxy(renames["BackupConfigurationIn"]).optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowIn"]).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "deletionProtectionEnabled": t.boolean().optional(),
            "connectorEnforcement": t.string().optional(),
            "insightsConfig": t.proxy(renames["InsightsConfigIn"]).optional(),
            "dataDiskSizeGb": t.string().optional(),
            "storageAutoResizeLimit": t.string().optional(),
            "crashSafeReplicationEnabled": t.boolean().optional(),
            "passwordValidationPolicy": t.proxy(
                renames["PasswordValidationPolicyIn"]
            ).optional(),
            "tier": t.string().optional(),
            "activeDirectoryConfig": t.proxy(
                renames["SqlActiveDirectoryConfigIn"]
            ).optional(),
        }
    ).named(renames["SettingsIn"])
    types["SettingsOut"] = t.struct(
        {
            "availabilityType": t.string().optional(),
            "ipConfiguration": t.proxy(renames["IpConfigurationOut"]).optional(),
            "authorizedGaeApplications": t.array(t.string()).optional(),
            "locationPreference": t.proxy(renames["LocationPreferenceOut"]).optional(),
            "timeZone": t.string().optional(),
            "settingsVersion": t.string().optional(),
            "collation": t.string().optional(),
            "sqlServerAuditConfig": t.proxy(
                renames["SqlServerAuditConfigOut"]
            ).optional(),
            "dataDiskType": t.string().optional(),
            "kind": t.string().optional(),
            "databaseFlags": t.array(t.proxy(renames["DatabaseFlagsOut"])).optional(),
            "replicationType": t.string().optional(),
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodOut"])
            ).optional(),
            "pricingPlan": t.string().optional(),
            "advancedMachineFeatures": t.proxy(
                renames["AdvancedMachineFeaturesOut"]
            ).optional(),
            "activationPolicy": t.string().optional(),
            "storageAutoResize": t.boolean().optional(),
            "databaseReplicationEnabled": t.boolean().optional(),
            "backupConfiguration": t.proxy(
                renames["BackupConfigurationOut"]
            ).optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowOut"]).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "deletionProtectionEnabled": t.boolean().optional(),
            "connectorEnforcement": t.string().optional(),
            "insightsConfig": t.proxy(renames["InsightsConfigOut"]).optional(),
            "dataDiskSizeGb": t.string().optional(),
            "storageAutoResizeLimit": t.string().optional(),
            "crashSafeReplicationEnabled": t.boolean().optional(),
            "passwordValidationPolicy": t.proxy(
                renames["PasswordValidationPolicyOut"]
            ).optional(),
            "tier": t.string().optional(),
            "activeDirectoryConfig": t.proxy(
                renames["SqlActiveDirectoryConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettingsOut"])
    types["SslCertIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "expirationTime": t.string().optional(),
            "certSerialNumber": t.string().optional(),
            "cert": t.string().optional(),
            "commonName": t.string().optional(),
            "sha1Fingerprint": t.string().optional(),
            "instance": t.string().optional(),
            "createTime": t.string().optional(),
            "selfLink": t.string().optional(),
        }
    ).named(renames["SslCertIn"])
    types["SslCertOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "expirationTime": t.string().optional(),
            "certSerialNumber": t.string().optional(),
            "cert": t.string().optional(),
            "commonName": t.string().optional(),
            "sha1Fingerprint": t.string().optional(),
            "instance": t.string().optional(),
            "createTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SslCertOut"])
    types["FlagIn"] = t.struct(
        {
            "allowedIntValues": t.array(t.string()).optional(),
            "appliesTo": t.array(t.string()).optional(),
            "allowedStringValues": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "requiresRestart": t.boolean().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "inBeta": t.boolean().optional(),
            "minValue": t.string().optional(),
            "maxValue": t.string().optional(),
        }
    ).named(renames["FlagIn"])
    types["FlagOut"] = t.struct(
        {
            "allowedIntValues": t.array(t.string()).optional(),
            "appliesTo": t.array(t.string()).optional(),
            "allowedStringValues": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "requiresRestart": t.boolean().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "inBeta": t.boolean().optional(),
            "minValue": t.string().optional(),
            "maxValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FlagOut"])
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
    types["AdvancedMachineFeaturesIn"] = t.struct(
        {"threadsPerCore": t.integer().optional()}
    ).named(renames["AdvancedMachineFeaturesIn"])
    types["AdvancedMachineFeaturesOut"] = t.struct(
        {
            "threadsPerCore": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvancedMachineFeaturesOut"])
    types["ConnectSettingsIn"] = t.struct(
        {
            "serverCaCert": t.proxy(renames["SslCertIn"]).optional(),
            "ipAddresses": t.array(t.proxy(renames["IpMappingIn"])).optional(),
            "region": t.string().optional(),
            "databaseVersion": t.string().optional(),
            "kind": t.string().optional(),
            "backendType": t.string().optional(),
        }
    ).named(renames["ConnectSettingsIn"])
    types["ConnectSettingsOut"] = t.struct(
        {
            "serverCaCert": t.proxy(renames["SslCertOut"]).optional(),
            "ipAddresses": t.array(t.proxy(renames["IpMappingOut"])).optional(),
            "region": t.string().optional(),
            "databaseVersion": t.string().optional(),
            "kind": t.string().optional(),
            "backendType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectSettingsOut"])
    types["CloneContextIn"] = t.struct(
        {
            "destinationInstanceName": t.string().optional(),
            "preferredZone": t.string().optional(),
            "binLogCoordinates": t.proxy(renames["BinLogCoordinatesIn"]).optional(),
            "databaseNames": t.array(t.string()).optional(),
            "allocatedIpRange": t.string().optional(),
            "kind": t.string().optional(),
            "pitrTimestampMs": t.string().optional(),
            "pointInTime": t.string().optional(),
        }
    ).named(renames["CloneContextIn"])
    types["CloneContextOut"] = t.struct(
        {
            "destinationInstanceName": t.string().optional(),
            "preferredZone": t.string().optional(),
            "binLogCoordinates": t.proxy(renames["BinLogCoordinatesOut"]).optional(),
            "databaseNames": t.array(t.string()).optional(),
            "allocatedIpRange": t.string().optional(),
            "kind": t.string().optional(),
            "pitrTimestampMs": t.string().optional(),
            "pointInTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloneContextOut"])
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
    types["SqlInstancesRescheduleMaintenanceRequestBodyIn"] = t.struct(
        {"reschedule": t.proxy(renames["RescheduleIn"])}
    ).named(renames["SqlInstancesRescheduleMaintenanceRequestBodyIn"])
    types["SqlInstancesRescheduleMaintenanceRequestBodyOut"] = t.struct(
        {
            "reschedule": t.proxy(renames["RescheduleOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlInstancesRescheduleMaintenanceRequestBodyOut"])
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
    types["DatabaseIn"] = t.struct(
        {
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "collation": t.string().optional(),
            "selfLink": t.string().optional(),
            "project": t.string().optional(),
            "sqlserverDatabaseDetails": t.proxy(renames["SqlServerDatabaseDetailsIn"]),
            "instance": t.string().optional(),
            "charset": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["DatabaseIn"])
    types["DatabaseOut"] = t.struct(
        {
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "collation": t.string().optional(),
            "selfLink": t.string().optional(),
            "project": t.string().optional(),
            "sqlserverDatabaseDetails": t.proxy(renames["SqlServerDatabaseDetailsOut"]),
            "instance": t.string().optional(),
            "charset": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseOut"])
    types["PasswordStatusIn"] = t.struct(
        {
            "locked": t.boolean().optional(),
            "passwordExpirationTime": t.string().optional(),
        }
    ).named(renames["PasswordStatusIn"])
    types["PasswordStatusOut"] = t.struct(
        {
            "locked": t.boolean().optional(),
            "passwordExpirationTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PasswordStatusOut"])
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
    types["SslCertsInsertResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "serverCaCert": t.proxy(renames["SslCertIn"]).optional(),
            "operation": t.proxy(renames["OperationIn"]).optional(),
            "clientCert": t.proxy(renames["SslCertDetailIn"]).optional(),
        }
    ).named(renames["SslCertsInsertResponseIn"])
    types["SslCertsInsertResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "serverCaCert": t.proxy(renames["SslCertOut"]).optional(),
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "clientCert": t.proxy(renames["SslCertDetailOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SslCertsInsertResponseOut"])
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
    types["TierIn"] = t.struct(
        {
            "tier": t.string().optional(),
            "region": t.array(t.string()).optional(),
            "RAM": t.string().optional(),
            "kind": t.string().optional(),
            "DiskQuota": t.string().optional(),
        }
    ).named(renames["TierIn"])
    types["TierOut"] = t.struct(
        {
            "tier": t.string().optional(),
            "region": t.array(t.string()).optional(),
            "RAM": t.string().optional(),
            "kind": t.string().optional(),
            "DiskQuota": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TierOut"])
    types["UserPasswordValidationPolicyIn"] = t.struct(
        {
            "allowedFailedAttempts": t.integer().optional(),
            "enablePasswordVerification": t.boolean().optional(),
            "enableFailedAttemptsCheck": t.boolean().optional(),
            "passwordExpirationDuration": t.string().optional(),
        }
    ).named(renames["UserPasswordValidationPolicyIn"])
    types["UserPasswordValidationPolicyOut"] = t.struct(
        {
            "allowedFailedAttempts": t.integer().optional(),
            "enablePasswordVerification": t.boolean().optional(),
            "enableFailedAttemptsCheck": t.boolean().optional(),
            "status": t.proxy(renames["PasswordStatusOut"]).optional(),
            "passwordExpirationDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserPasswordValidationPolicyOut"])
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
    types["DatabasesListResponseIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["DatabaseIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["DatabasesListResponseIn"])
    types["DatabasesListResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["DatabaseOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabasesListResponseOut"])
    types["UserIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "project": t.string().optional(),
            "dualPasswordType": t.string().optional(),
            "sqlserverUserDetails": t.proxy(renames["SqlServerUserDetailsIn"]),
            "instance": t.string().optional(),
            "passwordPolicy": t.proxy(
                renames["UserPasswordValidationPolicyIn"]
            ).optional(),
            "type": t.string().optional(),
            "password": t.string().optional(),
            "host": t.string().optional(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "project": t.string().optional(),
            "dualPasswordType": t.string().optional(),
            "sqlserverUserDetails": t.proxy(renames["SqlServerUserDetailsOut"]),
            "instance": t.string().optional(),
            "passwordPolicy": t.proxy(
                renames["UserPasswordValidationPolicyOut"]
            ).optional(),
            "type": t.string().optional(),
            "password": t.string().optional(),
            "host": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
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
    types["BinLogCoordinatesIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "binLogFileName": t.string().optional(),
            "binLogPosition": t.string().optional(),
        }
    ).named(renames["BinLogCoordinatesIn"])
    types["BinLogCoordinatesOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "binLogFileName": t.string().optional(),
            "binLogPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BinLogCoordinatesOut"])
    types["DemoteMasterMySqlReplicaConfigurationIn"] = t.struct(
        {
            "username": t.string().optional(),
            "clientKey": t.string().optional(),
            "caCertificate": t.string().optional(),
            "clientCertificate": t.string().optional(),
            "password": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["DemoteMasterMySqlReplicaConfigurationIn"])
    types["DemoteMasterMySqlReplicaConfigurationOut"] = t.struct(
        {
            "username": t.string().optional(),
            "clientKey": t.string().optional(),
            "caCertificate": t.string().optional(),
            "clientCertificate": t.string().optional(),
            "password": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DemoteMasterMySqlReplicaConfigurationOut"])
    types["ReplicaConfigurationIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "mysqlReplicaConfiguration": t.proxy(
                renames["MySqlReplicaConfigurationIn"]
            ).optional(),
            "failoverTarget": t.boolean().optional(),
        }
    ).named(renames["ReplicaConfigurationIn"])
    types["ReplicaConfigurationOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "mysqlReplicaConfiguration": t.proxy(
                renames["MySqlReplicaConfigurationOut"]
            ).optional(),
            "failoverTarget": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplicaConfigurationOut"])
    types["SslCertsInsertRequestIn"] = t.struct(
        {"commonName": t.string().optional()}
    ).named(renames["SslCertsInsertRequestIn"])
    types["SslCertsInsertRequestOut"] = t.struct(
        {
            "commonName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SslCertsInsertRequestOut"])
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
    types["MaintenanceWindowIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "day": t.integer().optional(),
            "hour": t.integer().optional(),
            "updateTrack": t.string().optional(),
        }
    ).named(renames["MaintenanceWindowIn"])
    types["MaintenanceWindowOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "day": t.integer().optional(),
            "hour": t.integer().optional(),
            "updateTrack": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceWindowOut"])
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
    types["DatabaseInstanceIn"] = t.struct(
        {
            "serviceAccountEmailAddress": t.string().optional(),
            "project": t.string().optional(),
            "onPremisesConfiguration": t.proxy(
                renames["OnPremisesConfigurationIn"]
            ).optional(),
            "kind": t.string().optional(),
            "diskEncryptionStatus": t.proxy(
                renames["DiskEncryptionStatusIn"]
            ).optional(),
            "currentDiskSize": t.string().optional(),
            "backendType": t.string().optional(),
            "ipv6Address": t.string().optional(),
            "maintenanceVersion": t.string().optional(),
            "failoverReplica": t.struct(
                {"available": t.boolean().optional(), "name": t.string().optional()}
            ).optional(),
            "diskEncryptionConfiguration": t.proxy(
                renames["DiskEncryptionConfigurationIn"]
            ).optional(),
            "maxDiskSize": t.string().optional(),
            "region": t.string().optional(),
            "settings": t.proxy(renames["SettingsIn"]).optional(),
            "rootPassword": t.string().optional(),
            "masterInstanceName": t.string().optional(),
            "etag": t.string().optional(),
            "ipAddresses": t.array(t.proxy(renames["IpMappingIn"])).optional(),
            "state": t.string().optional(),
            "gceZone": t.string().optional(),
            "serverCaCert": t.proxy(renames["SslCertIn"]).optional(),
            "instanceType": t.string().optional(),
            "scheduledMaintenance": t.proxy(
                renames["SqlScheduledMaintenanceIn"]
            ).optional(),
            "selfLink": t.string().optional(),
            "replicaNames": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "secondaryGceZone": t.string().optional(),
            "replicaConfiguration": t.proxy(
                renames["ReplicaConfigurationIn"]
            ).optional(),
            "connectionName": t.string().optional(),
            "databaseVersion": t.string().optional(),
            "suspensionReason": t.array(t.string()).optional(),
            "satisfiesPzs": t.boolean().optional(),
            "outOfDiskReport": t.proxy(renames["SqlOutOfDiskReportIn"]).optional(),
        }
    ).named(renames["DatabaseInstanceIn"])
    types["DatabaseInstanceOut"] = t.struct(
        {
            "serviceAccountEmailAddress": t.string().optional(),
            "project": t.string().optional(),
            "onPremisesConfiguration": t.proxy(
                renames["OnPremisesConfigurationOut"]
            ).optional(),
            "kind": t.string().optional(),
            "databaseInstalledVersion": t.string().optional(),
            "diskEncryptionStatus": t.proxy(
                renames["DiskEncryptionStatusOut"]
            ).optional(),
            "currentDiskSize": t.string().optional(),
            "backendType": t.string().optional(),
            "ipv6Address": t.string().optional(),
            "maintenanceVersion": t.string().optional(),
            "failoverReplica": t.struct(
                {"available": t.boolean().optional(), "name": t.string().optional()}
            ).optional(),
            "availableMaintenanceVersions": t.array(t.string()).optional(),
            "diskEncryptionConfiguration": t.proxy(
                renames["DiskEncryptionConfigurationOut"]
            ).optional(),
            "maxDiskSize": t.string().optional(),
            "region": t.string().optional(),
            "settings": t.proxy(renames["SettingsOut"]).optional(),
            "rootPassword": t.string().optional(),
            "masterInstanceName": t.string().optional(),
            "createTime": t.string().optional(),
            "etag": t.string().optional(),
            "ipAddresses": t.array(t.proxy(renames["IpMappingOut"])).optional(),
            "state": t.string().optional(),
            "gceZone": t.string().optional(),
            "serverCaCert": t.proxy(renames["SslCertOut"]).optional(),
            "instanceType": t.string().optional(),
            "scheduledMaintenance": t.proxy(
                renames["SqlScheduledMaintenanceOut"]
            ).optional(),
            "selfLink": t.string().optional(),
            "replicaNames": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "secondaryGceZone": t.string().optional(),
            "replicaConfiguration": t.proxy(
                renames["ReplicaConfigurationOut"]
            ).optional(),
            "connectionName": t.string().optional(),
            "databaseVersion": t.string().optional(),
            "suspensionReason": t.array(t.string()).optional(),
            "satisfiesPzs": t.boolean().optional(),
            "outOfDiskReport": t.proxy(renames["SqlOutOfDiskReportOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseInstanceOut"])
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
    types["ExportContextIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "sqlExportOptions": t.struct(
                {
                    "schemaOnly": t.boolean().optional(),
                    "mysqlExportOptions": t.struct(
                        {"masterData": t.integer().optional()}
                    ).optional(),
                    "tables": t.array(t.string()).optional(),
                }
            ).optional(),
            "databases": t.array(t.string()).optional(),
            "bakExportOptions": t.struct(
                {
                    "striped": t.boolean().optional(),
                    "stripeCount": t.integer().optional(),
                }
            ).optional(),
            "fileType": t.string().optional(),
            "uri": t.string().optional(),
            "csvExportOptions": t.struct(
                {
                    "fieldsTerminatedBy": t.string().optional(),
                    "quoteCharacter": t.string().optional(),
                    "selectQuery": t.string().optional(),
                    "escapeCharacter": t.string().optional(),
                    "linesTerminatedBy": t.string().optional(),
                }
            ).optional(),
            "offload": t.boolean().optional(),
        }
    ).named(renames["ExportContextIn"])
    types["ExportContextOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "sqlExportOptions": t.struct(
                {
                    "schemaOnly": t.boolean().optional(),
                    "mysqlExportOptions": t.struct(
                        {"masterData": t.integer().optional()}
                    ).optional(),
                    "tables": t.array(t.string()).optional(),
                }
            ).optional(),
            "databases": t.array(t.string()).optional(),
            "bakExportOptions": t.struct(
                {
                    "striped": t.boolean().optional(),
                    "stripeCount": t.integer().optional(),
                }
            ).optional(),
            "fileType": t.string().optional(),
            "uri": t.string().optional(),
            "csvExportOptions": t.struct(
                {
                    "fieldsTerminatedBy": t.string().optional(),
                    "quoteCharacter": t.string().optional(),
                    "selectQuery": t.string().optional(),
                    "escapeCharacter": t.string().optional(),
                    "linesTerminatedBy": t.string().optional(),
                }
            ).optional(),
            "offload": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportContextOut"])
    types["IpConfigurationIn"] = t.struct(
        {
            "requireSsl": t.boolean().optional(),
            "privateNetwork": t.string().optional(),
            "authorizedNetworks": t.array(t.proxy(renames["AclEntryIn"])).optional(),
            "enablePrivatePathForGoogleCloudServices": t.boolean().optional(),
            "ipv4Enabled": t.boolean().optional(),
            "allocatedIpRange": t.string().optional(),
        }
    ).named(renames["IpConfigurationIn"])
    types["IpConfigurationOut"] = t.struct(
        {
            "requireSsl": t.boolean().optional(),
            "privateNetwork": t.string().optional(),
            "authorizedNetworks": t.array(t.proxy(renames["AclEntryOut"])).optional(),
            "enablePrivatePathForGoogleCloudServices": t.boolean().optional(),
            "ipv4Enabled": t.boolean().optional(),
            "allocatedIpRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IpConfigurationOut"])
    types["RestoreBackupContextIn"] = t.struct(
        {
            "project": t.string().optional(),
            "kind": t.string().optional(),
            "instanceId": t.string().optional(),
            "backupRunId": t.string().optional(),
        }
    ).named(renames["RestoreBackupContextIn"])
    types["RestoreBackupContextOut"] = t.struct(
        {
            "project": t.string().optional(),
            "kind": t.string().optional(),
            "instanceId": t.string().optional(),
            "backupRunId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreBackupContextOut"])
    types["AclEntryIn"] = t.struct(
        {
            "expirationTime": t.string().optional(),
            "kind": t.string().optional(),
            "value": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["AclEntryIn"])
    types["AclEntryOut"] = t.struct(
        {
            "expirationTime": t.string().optional(),
            "kind": t.string().optional(),
            "value": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AclEntryOut"])
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
    types["OperationErrorIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["OperationErrorIn"])
    types["OperationErrorOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationErrorOut"])
    types["OperationIn"] = t.struct(
        {
            "targetProject": t.string().optional(),
            "importContext": t.proxy(renames["ImportContextIn"]).optional(),
            "kind": t.string().optional(),
            "operationType": t.string().optional(),
            "selfLink": t.string().optional(),
            "targetLink": t.string(),
            "endTime": t.string().optional(),
            "user": t.string().optional(),
            "status": t.string().optional(),
            "name": t.string().optional(),
            "exportContext": t.proxy(renames["ExportContextIn"]).optional(),
            "error": t.proxy(renames["OperationErrorsIn"]).optional(),
            "insertTime": t.string().optional(),
            "targetId": t.string().optional(),
            "startTime": t.string().optional(),
            "backupContext": t.proxy(renames["BackupContextIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "targetProject": t.string().optional(),
            "importContext": t.proxy(renames["ImportContextOut"]).optional(),
            "kind": t.string().optional(),
            "operationType": t.string().optional(),
            "selfLink": t.string().optional(),
            "targetLink": t.string(),
            "endTime": t.string().optional(),
            "user": t.string().optional(),
            "status": t.string().optional(),
            "name": t.string().optional(),
            "exportContext": t.proxy(renames["ExportContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "insertTime": t.string().optional(),
            "targetId": t.string().optional(),
            "startTime": t.string().optional(),
            "backupContext": t.proxy(renames["BackupContextOut"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["DemoteMasterContextIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "verifyGtidConsistency": t.boolean().optional(),
            "skipReplicationSetup": t.boolean().optional(),
            "masterInstanceName": t.string().optional(),
            "replicaConfiguration": t.proxy(
                renames["DemoteMasterConfigurationIn"]
            ).optional(),
        }
    ).named(renames["DemoteMasterContextIn"])
    types["DemoteMasterContextOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "verifyGtidConsistency": t.boolean().optional(),
            "skipReplicationSetup": t.boolean().optional(),
            "masterInstanceName": t.string().optional(),
            "replicaConfiguration": t.proxy(
                renames["DemoteMasterConfigurationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DemoteMasterContextOut"])
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
    types["MySqlSyncConfigIn"] = t.struct(
        {"initialSyncFlags": t.array(t.proxy(renames["SyncFlagsIn"])).optional()}
    ).named(renames["MySqlSyncConfigIn"])
    types["MySqlSyncConfigOut"] = t.struct(
        {
            "initialSyncFlags": t.array(t.proxy(renames["SyncFlagsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MySqlSyncConfigOut"])
    types["OperationsListResponseIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["OperationsListResponseIn"])
    types["OperationsListResponseOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationsListResponseOut"])
    types["PasswordValidationPolicyIn"] = t.struct(
        {
            "minLength": t.integer().optional(),
            "enablePasswordPolicy": t.boolean().optional(),
            "reuseInterval": t.integer().optional(),
            "complexity": t.string().optional(),
            "passwordChangeInterval": t.string().optional(),
            "disallowUsernameSubstring": t.boolean().optional(),
        }
    ).named(renames["PasswordValidationPolicyIn"])
    types["PasswordValidationPolicyOut"] = t.struct(
        {
            "minLength": t.integer().optional(),
            "enablePasswordPolicy": t.boolean().optional(),
            "reuseInterval": t.integer().optional(),
            "complexity": t.string().optional(),
            "passwordChangeInterval": t.string().optional(),
            "disallowUsernameSubstring": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PasswordValidationPolicyOut"])
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
    types["SqlInstancesStartExternalSyncRequestIn"] = t.struct(
        {
            "skipVerification": t.boolean().optional(),
            "syncMode": t.string().optional(),
            "mysqlSyncConfig": t.proxy(renames["MySqlSyncConfigIn"]).optional(),
        }
    ).named(renames["SqlInstancesStartExternalSyncRequestIn"])
    types["SqlInstancesStartExternalSyncRequestOut"] = t.struct(
        {
            "skipVerification": t.boolean().optional(),
            "syncMode": t.string().optional(),
            "mysqlSyncConfig": t.proxy(renames["MySqlSyncConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlInstancesStartExternalSyncRequestOut"])
    types["OnPremisesConfigurationIn"] = t.struct(
        {
            "clientCertificate": t.string().optional(),
            "clientKey": t.string().optional(),
            "kind": t.string().optional(),
            "username": t.string().optional(),
            "dumpFilePath": t.string().optional(),
            "sourceInstance": t.proxy(renames["InstanceReferenceIn"]).optional(),
            "password": t.string().optional(),
            "hostPort": t.string().optional(),
            "caCertificate": t.string().optional(),
        }
    ).named(renames["OnPremisesConfigurationIn"])
    types["OnPremisesConfigurationOut"] = t.struct(
        {
            "clientCertificate": t.string().optional(),
            "clientKey": t.string().optional(),
            "kind": t.string().optional(),
            "username": t.string().optional(),
            "dumpFilePath": t.string().optional(),
            "sourceInstance": t.proxy(renames["InstanceReferenceOut"]).optional(),
            "password": t.string().optional(),
            "hostPort": t.string().optional(),
            "caCertificate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OnPremisesConfigurationOut"])
    types["InsightsConfigIn"] = t.struct(
        {
            "queryInsightsEnabled": t.boolean().optional(),
            "recordApplicationTags": t.boolean().optional(),
            "queryStringLength": t.integer().optional(),
            "queryPlansPerMinute": t.integer().optional(),
            "recordClientAddress": t.boolean().optional(),
        }
    ).named(renames["InsightsConfigIn"])
    types["InsightsConfigOut"] = t.struct(
        {
            "queryInsightsEnabled": t.boolean().optional(),
            "recordApplicationTags": t.boolean().optional(),
            "queryStringLength": t.integer().optional(),
            "queryPlansPerMinute": t.integer().optional(),
            "recordClientAddress": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsightsConfigOut"])
    types["GenerateEphemeralCertResponseIn"] = t.struct(
        {"ephemeralCert": t.proxy(renames["SslCertIn"]).optional()}
    ).named(renames["GenerateEphemeralCertResponseIn"])
    types["GenerateEphemeralCertResponseOut"] = t.struct(
        {
            "ephemeralCert": t.proxy(renames["SslCertOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateEphemeralCertResponseOut"])
    types["InstancesListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "warnings": t.array(t.proxy(renames["ApiWarningIn"])).optional(),
            "items": t.array(t.proxy(renames["DatabaseInstanceIn"])).optional(),
        }
    ).named(renames["InstancesListResponseIn"])
    types["InstancesListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "warnings": t.array(t.proxy(renames["ApiWarningOut"])).optional(),
            "items": t.array(t.proxy(renames["DatabaseInstanceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesListResponseOut"])
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
    types["BackupConfigurationIn"] = t.struct(
        {
            "location": t.string().optional(),
            "replicationLogArchivingEnabled": t.boolean().optional(),
            "backupRetentionSettings": t.proxy(
                renames["BackupRetentionSettingsIn"]
            ).optional(),
            "transactionLogRetentionDays": t.integer().optional(),
            "binaryLogEnabled": t.boolean().optional(),
            "enabled": t.boolean().optional(),
            "startTime": t.string().optional(),
            "pointInTimeRecoveryEnabled": t.boolean().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["BackupConfigurationIn"])
    types["BackupConfigurationOut"] = t.struct(
        {
            "location": t.string().optional(),
            "replicationLogArchivingEnabled": t.boolean().optional(),
            "backupRetentionSettings": t.proxy(
                renames["BackupRetentionSettingsOut"]
            ).optional(),
            "transactionLogRetentionDays": t.integer().optional(),
            "binaryLogEnabled": t.boolean().optional(),
            "enabled": t.boolean().optional(),
            "startTime": t.string().optional(),
            "pointInTimeRecoveryEnabled": t.boolean().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupConfigurationOut"])
    types["BackupRunIn"] = t.struct(
        {
            "status": t.string().optional(),
            "endTime": t.string().optional(),
            "timeZone": t.string().optional(),
            "kind": t.string().optional(),
            "diskEncryptionStatus": t.proxy(
                renames["DiskEncryptionStatusIn"]
            ).optional(),
            "selfLink": t.string().optional(),
            "windowStartTime": t.string().optional(),
            "type": t.string().optional(),
            "startTime": t.string().optional(),
            "instance": t.string().optional(),
            "diskEncryptionConfiguration": t.proxy(
                renames["DiskEncryptionConfigurationIn"]
            ).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["OperationErrorIn"]).optional(),
            "backupKind": t.string().optional(),
            "enqueuedTime": t.string().optional(),
            "id": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["BackupRunIn"])
    types["BackupRunOut"] = t.struct(
        {
            "status": t.string().optional(),
            "endTime": t.string().optional(),
            "timeZone": t.string().optional(),
            "kind": t.string().optional(),
            "diskEncryptionStatus": t.proxy(
                renames["DiskEncryptionStatusOut"]
            ).optional(),
            "selfLink": t.string().optional(),
            "windowStartTime": t.string().optional(),
            "type": t.string().optional(),
            "startTime": t.string().optional(),
            "instance": t.string().optional(),
            "diskEncryptionConfiguration": t.proxy(
                renames["DiskEncryptionConfigurationOut"]
            ).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "backupKind": t.string().optional(),
            "enqueuedTime": t.string().optional(),
            "id": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["BackupRunOut"])
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
    types["SqlServerAuditConfigIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "retentionInterval": t.string().optional(),
            "bucket": t.string().optional(),
            "uploadInterval": t.string().optional(),
        }
    ).named(renames["SqlServerAuditConfigIn"])
    types["SqlServerAuditConfigOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "retentionInterval": t.string().optional(),
            "bucket": t.string().optional(),
            "uploadInterval": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlServerAuditConfigOut"])
    types["PerformDiskShrinkContextIn"] = t.struct(
        {"targetSizeGb": t.string().optional()}
    ).named(renames["PerformDiskShrinkContextIn"])
    types["PerformDiskShrinkContextOut"] = t.struct(
        {
            "targetSizeGb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerformDiskShrinkContextOut"])
    types["GenerateEphemeralCertRequestIn"] = t.struct(
        {
            "public_key": t.string().optional(),
            "readTime": t.string().optional(),
            "validDuration": t.string().optional(),
            "access_token": t.string().optional(),
        }
    ).named(renames["GenerateEphemeralCertRequestIn"])
    types["GenerateEphemeralCertRequestOut"] = t.struct(
        {
            "public_key": t.string().optional(),
            "readTime": t.string().optional(),
            "validDuration": t.string().optional(),
            "access_token": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateEphemeralCertRequestOut"])
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
    types["InstancesImportRequestIn"] = t.struct(
        {"importContext": t.proxy(renames["ImportContextIn"]).optional()}
    ).named(renames["InstancesImportRequestIn"])
    types["InstancesImportRequestOut"] = t.struct(
        {
            "importContext": t.proxy(renames["ImportContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesImportRequestOut"])
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
    types["InstancesFailoverRequestIn"] = t.struct(
        {"failoverContext": t.proxy(renames["FailoverContextIn"]).optional()}
    ).named(renames["InstancesFailoverRequestIn"])
    types["InstancesFailoverRequestOut"] = t.struct(
        {
            "failoverContext": t.proxy(renames["FailoverContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesFailoverRequestOut"])
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
    types["SqlInstancesVerifyExternalSyncSettingsRequestIn"] = t.struct(
        {
            "verifyReplicationOnly": t.boolean().optional(),
            "mysqlSyncConfig": t.proxy(renames["MySqlSyncConfigIn"]).optional(),
            "syncMode": t.string().optional(),
            "verifyConnectionOnly": t.boolean().optional(),
        }
    ).named(renames["SqlInstancesVerifyExternalSyncSettingsRequestIn"])
    types["SqlInstancesVerifyExternalSyncSettingsRequestOut"] = t.struct(
        {
            "verifyReplicationOnly": t.boolean().optional(),
            "mysqlSyncConfig": t.proxy(renames["MySqlSyncConfigOut"]).optional(),
            "syncMode": t.string().optional(),
            "verifyConnectionOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlInstancesVerifyExternalSyncSettingsRequestOut"])
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
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "statusDetail": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["InstancesTruncateLogRequestIn"] = t.struct(
        {"truncateLogContext": t.proxy(renames["TruncateLogContextIn"]).optional()}
    ).named(renames["InstancesTruncateLogRequestIn"])
    types["InstancesTruncateLogRequestOut"] = t.struct(
        {
            "truncateLogContext": t.proxy(renames["TruncateLogContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesTruncateLogRequestOut"])
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
    types["MySqlReplicaConfigurationIn"] = t.struct(
        {
            "dumpFilePath": t.string().optional(),
            "sslCipher": t.string().optional(),
            "caCertificate": t.string().optional(),
            "verifyServerCertificate": t.boolean().optional(),
            "masterHeartbeatPeriod": t.string().optional(),
            "connectRetryInterval": t.integer().optional(),
            "password": t.string().optional(),
            "clientCertificate": t.string().optional(),
            "username": t.string().optional(),
            "kind": t.string().optional(),
            "clientKey": t.string().optional(),
        }
    ).named(renames["MySqlReplicaConfigurationIn"])
    types["MySqlReplicaConfigurationOut"] = t.struct(
        {
            "dumpFilePath": t.string().optional(),
            "sslCipher": t.string().optional(),
            "caCertificate": t.string().optional(),
            "verifyServerCertificate": t.boolean().optional(),
            "masterHeartbeatPeriod": t.string().optional(),
            "connectRetryInterval": t.integer().optional(),
            "password": t.string().optional(),
            "clientCertificate": t.string().optional(),
            "username": t.string().optional(),
            "kind": t.string().optional(),
            "clientKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MySqlReplicaConfigurationOut"])
    types["ImportContextIn"] = t.struct(
        {
            "uri": t.string().optional(),
            "csvImportOptions": t.struct(
                {
                    "fieldsTerminatedBy": t.string().optional(),
                    "quoteCharacter": t.string().optional(),
                    "table": t.string().optional(),
                    "escapeCharacter": t.string().optional(),
                    "columns": t.array(t.string()).optional(),
                    "linesTerminatedBy": t.string().optional(),
                }
            ).optional(),
            "database": t.string().optional(),
            "importUser": t.string().optional(),
            "fileType": t.string().optional(),
            "kind": t.string().optional(),
            "bakImportOptions": t.struct(
                {
                    "striped": t.boolean().optional(),
                    "encryptionOptions": t.struct(
                        {
                            "pvkPassword": t.string().optional(),
                            "pvkPath": t.string().optional(),
                            "certPath": t.string().optional(),
                        }
                    ),
                }
            ).optional(),
        }
    ).named(renames["ImportContextIn"])
    types["ImportContextOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "csvImportOptions": t.struct(
                {
                    "fieldsTerminatedBy": t.string().optional(),
                    "quoteCharacter": t.string().optional(),
                    "table": t.string().optional(),
                    "escapeCharacter": t.string().optional(),
                    "columns": t.array(t.string()).optional(),
                    "linesTerminatedBy": t.string().optional(),
                }
            ).optional(),
            "database": t.string().optional(),
            "importUser": t.string().optional(),
            "fileType": t.string().optional(),
            "kind": t.string().optional(),
            "bakImportOptions": t.struct(
                {
                    "striped": t.boolean().optional(),
                    "encryptionOptions": t.struct(
                        {
                            "pvkPassword": t.string().optional(),
                            "pvkPath": t.string().optional(),
                            "certPath": t.string().optional(),
                        }
                    ),
                }
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportContextOut"])
    types["SqlInstancesResetReplicaSizeRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SqlInstancesResetReplicaSizeRequestIn"])
    types["SqlInstancesResetReplicaSizeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SqlInstancesResetReplicaSizeRequestOut"])
    types["InstancesExportRequestIn"] = t.struct(
        {"exportContext": t.proxy(renames["ExportContextIn"]).optional()}
    ).named(renames["InstancesExportRequestIn"])
    types["InstancesExportRequestOut"] = t.struct(
        {
            "exportContext": t.proxy(renames["ExportContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesExportRequestOut"])
    types["UsersListResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["UserIn"])).optional(),
        }
    ).named(renames["UsersListResponseIn"])
    types["UsersListResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["UserOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsersListResponseOut"])
    types["InstancesCloneRequestIn"] = t.struct(
        {"cloneContext": t.proxy(renames["CloneContextIn"]).optional()}
    ).named(renames["InstancesCloneRequestIn"])
    types["InstancesCloneRequestOut"] = t.struct(
        {
            "cloneContext": t.proxy(renames["CloneContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstancesCloneRequestOut"])
    types["SqlScheduledMaintenanceIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "scheduleDeadlineTime": t.string().optional(),
            "canDefer": t.boolean(),
            "canReschedule": t.boolean().optional(),
        }
    ).named(renames["SqlScheduledMaintenanceIn"])
    types["SqlScheduledMaintenanceOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "scheduleDeadlineTime": t.string().optional(),
            "canDefer": t.boolean(),
            "canReschedule": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlScheduledMaintenanceOut"])

    functions = {}
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
    functions["usersUpdate"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/users",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UsersListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDelete"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/users",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UsersListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersInsert"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/users",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UsersListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersGet"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/users",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UsersListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersList"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/users",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UsersListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["connectGenerateEphemeralCert"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/connectSettings",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "readTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConnectSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["connectGet"] = sqladmin.get(
        "v1/projects/{project}/instances/{instance}/connectSettings",
        t.struct(
            {
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "readTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConnectSettingsOut"]),
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
    functions["backupRunsList"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}/backupRuns/{id}",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["backupRunsInsert"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}/backupRuns/{id}",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["backupRunsGet"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}/backupRuns/{id}",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["backupRunsDelete"] = sqladmin.delete(
        "v1/projects/{project}/instances/{instance}/backupRuns/{id}",
        t.struct(
            {
                "instance": t.string().optional(),
                "project": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
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
    functions["operationsList"] = sqladmin.get(
        "v1/projects/{project}/operations/{operation}",
        t.struct(
            {
                "operation": t.string().optional(),
                "project": t.string().optional(),
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
                "operation": t.string().optional(),
                "project": t.string().optional(),
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
    functions["databasesGet"] = sqladmin.put(
        "v1/projects/{project}/instances/{instance}/databases/{database}",
        t.struct(
            {
                "database": t.string().optional(),
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "collation": t.string().optional(),
                "selfLink": t.string().optional(),
                "sqlserverDatabaseDetails": t.proxy(
                    renames["SqlServerDatabaseDetailsIn"]
                ),
                "charset": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["databasesDelete"] = sqladmin.put(
        "v1/projects/{project}/instances/{instance}/databases/{database}",
        t.struct(
            {
                "database": t.string().optional(),
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "collation": t.string().optional(),
                "selfLink": t.string().optional(),
                "sqlserverDatabaseDetails": t.proxy(
                    renames["SqlServerDatabaseDetailsIn"]
                ),
                "charset": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["databasesList"] = sqladmin.put(
        "v1/projects/{project}/instances/{instance}/databases/{database}",
        t.struct(
            {
                "database": t.string().optional(),
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "collation": t.string().optional(),
                "selfLink": t.string().optional(),
                "sqlserverDatabaseDetails": t.proxy(
                    renames["SqlServerDatabaseDetailsIn"]
                ),
                "charset": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["databasesPatch"] = sqladmin.put(
        "v1/projects/{project}/instances/{instance}/databases/{database}",
        t.struct(
            {
                "database": t.string().optional(),
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "collation": t.string().optional(),
                "selfLink": t.string().optional(),
                "sqlserverDatabaseDetails": t.proxy(
                    renames["SqlServerDatabaseDetailsIn"]
                ),
                "charset": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["databasesInsert"] = sqladmin.put(
        "v1/projects/{project}/instances/{instance}/databases/{database}",
        t.struct(
            {
                "database": t.string().optional(),
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "collation": t.string().optional(),
                "selfLink": t.string().optional(),
                "sqlserverDatabaseDetails": t.proxy(
                    renames["SqlServerDatabaseDetailsIn"]
                ),
                "charset": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["databasesUpdate"] = sqladmin.put(
        "v1/projects/{project}/instances/{instance}/databases/{database}",
        t.struct(
            {
                "database": t.string().optional(),
                "project": t.string().optional(),
                "instance": t.string().optional(),
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "collation": t.string().optional(),
                "selfLink": t.string().optional(),
                "sqlserverDatabaseDetails": t.proxy(
                    renames["SqlServerDatabaseDetailsIn"]
                ),
                "charset": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesListServerCas"] = sqladmin.get(
        "v1/projects/{project}/instances",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstancesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesRestart"] = sqladmin.get(
        "v1/projects/{project}/instances",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstancesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesPatch"] = sqladmin.get(
        "v1/projects/{project}/instances",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstancesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesDemoteMaster"] = sqladmin.get(
        "v1/projects/{project}/instances",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstancesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesDelete"] = sqladmin.get(
        "v1/projects/{project}/instances",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstancesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesImport"] = sqladmin.get(
        "v1/projects/{project}/instances",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstancesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesGet"] = sqladmin.get(
        "v1/projects/{project}/instances",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstancesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesTruncateLog"] = sqladmin.get(
        "v1/projects/{project}/instances",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstancesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesStopReplica"] = sqladmin.get(
        "v1/projects/{project}/instances",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstancesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesAddServerCa"] = sqladmin.get(
        "v1/projects/{project}/instances",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstancesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesUpdate"] = sqladmin.get(
        "v1/projects/{project}/instances",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstancesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesFailover"] = sqladmin.get(
        "v1/projects/{project}/instances",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstancesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesInsert"] = sqladmin.get(
        "v1/projects/{project}/instances",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstancesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesExport"] = sqladmin.get(
        "v1/projects/{project}/instances",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstancesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesResetSslConfig"] = sqladmin.get(
        "v1/projects/{project}/instances",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstancesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesClone"] = sqladmin.get(
        "v1/projects/{project}/instances",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstancesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesRestoreBackup"] = sqladmin.get(
        "v1/projects/{project}/instances",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstancesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesStartReplica"] = sqladmin.get(
        "v1/projects/{project}/instances",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstancesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesPromoteReplica"] = sqladmin.get(
        "v1/projects/{project}/instances",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstancesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesRotateServerCa"] = sqladmin.get(
        "v1/projects/{project}/instances",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstancesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["instancesList"] = sqladmin.get(
        "v1/projects/{project}/instances",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstancesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="sqladmin", renames=renames, types=Box(types), functions=Box(functions)
    )
