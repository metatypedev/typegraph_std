from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_datamigration():
    datamigration = HTTPRuntime("https://datamigration.googleapis.com/")

    renames = {
        "ErrorResponse": "_datamigration_1_ErrorResponse",
        "GoogleCloudClouddmsV1OperationMetadataIn": "_datamigration_2_GoogleCloudClouddmsV1OperationMetadataIn",
        "GoogleCloudClouddmsV1OperationMetadataOut": "_datamigration_3_GoogleCloudClouddmsV1OperationMetadataOut",
        "MySqlConnectionProfileIn": "_datamigration_4_MySqlConnectionProfileIn",
        "MySqlConnectionProfileOut": "_datamigration_5_MySqlConnectionProfileOut",
        "AlloyDbConnectionProfileIn": "_datamigration_6_AlloyDbConnectionProfileIn",
        "AlloyDbConnectionProfileOut": "_datamigration_7_AlloyDbConnectionProfileOut",
        "PrivateConnectionIn": "_datamigration_8_PrivateConnectionIn",
        "PrivateConnectionOut": "_datamigration_9_PrivateConnectionOut",
        "StopMigrationJobRequestIn": "_datamigration_10_StopMigrationJobRequestIn",
        "StopMigrationJobRequestOut": "_datamigration_11_StopMigrationJobRequestOut",
        "ResumeMigrationJobRequestIn": "_datamigration_12_ResumeMigrationJobRequestIn",
        "ResumeMigrationJobRequestOut": "_datamigration_13_ResumeMigrationJobRequestOut",
        "VmCreationConfigIn": "_datamigration_14_VmCreationConfigIn",
        "VmCreationConfigOut": "_datamigration_15_VmCreationConfigOut",
        "CloudSqlConnectionProfileIn": "_datamigration_16_CloudSqlConnectionProfileIn",
        "CloudSqlConnectionProfileOut": "_datamigration_17_CloudSqlConnectionProfileOut",
        "StaticServiceIpConnectivityIn": "_datamigration_18_StaticServiceIpConnectivityIn",
        "StaticServiceIpConnectivityOut": "_datamigration_19_StaticServiceIpConnectivityOut",
        "SearchBackgroundJobsResponseIn": "_datamigration_20_SearchBackgroundJobsResponseIn",
        "SearchBackgroundJobsResponseOut": "_datamigration_21_SearchBackgroundJobsResponseOut",
        "ForwardSshTunnelConnectivityIn": "_datamigration_22_ForwardSshTunnelConnectivityIn",
        "ForwardSshTunnelConnectivityOut": "_datamigration_23_ForwardSshTunnelConnectivityOut",
        "EncryptionConfigIn": "_datamigration_24_EncryptionConfigIn",
        "EncryptionConfigOut": "_datamigration_25_EncryptionConfigOut",
        "DescribeDatabaseEntitiesResponseIn": "_datamigration_26_DescribeDatabaseEntitiesResponseIn",
        "DescribeDatabaseEntitiesResponseOut": "_datamigration_27_DescribeDatabaseEntitiesResponseOut",
        "SequenceEntityIn": "_datamigration_28_SequenceEntityIn",
        "SequenceEntityOut": "_datamigration_29_SequenceEntityOut",
        "AuditConfigIn": "_datamigration_30_AuditConfigIn",
        "AuditConfigOut": "_datamigration_31_AuditConfigOut",
        "RollbackConversionWorkspaceRequestIn": "_datamigration_32_RollbackConversionWorkspaceRequestIn",
        "RollbackConversionWorkspaceRequestOut": "_datamigration_33_RollbackConversionWorkspaceRequestOut",
        "StaticIpConnectivityIn": "_datamigration_34_StaticIpConnectivityIn",
        "StaticIpConnectivityOut": "_datamigration_35_StaticIpConnectivityOut",
        "VpcPeeringConnectivityIn": "_datamigration_36_VpcPeeringConnectivityIn",
        "VpcPeeringConnectivityOut": "_datamigration_37_VpcPeeringConnectivityOut",
        "PrimaryInstanceSettingsIn": "_datamigration_38_PrimaryInstanceSettingsIn",
        "PrimaryInstanceSettingsOut": "_datamigration_39_PrimaryInstanceSettingsOut",
        "UserPasswordIn": "_datamigration_40_UserPasswordIn",
        "UserPasswordOut": "_datamigration_41_UserPasswordOut",
        "BackgroundJobLogEntryIn": "_datamigration_42_BackgroundJobLogEntryIn",
        "BackgroundJobLogEntryOut": "_datamigration_43_BackgroundJobLogEntryOut",
        "FetchStaticIpsResponseIn": "_datamigration_44_FetchStaticIpsResponseIn",
        "FetchStaticIpsResponseOut": "_datamigration_45_FetchStaticIpsResponseOut",
        "StatusIn": "_datamigration_46_StatusIn",
        "StatusOut": "_datamigration_47_StatusOut",
        "SynonymEntityIn": "_datamigration_48_SynonymEntityIn",
        "SynonymEntityOut": "_datamigration_49_SynonymEntityOut",
        "CloudSqlSettingsIn": "_datamigration_50_CloudSqlSettingsIn",
        "CloudSqlSettingsOut": "_datamigration_51_CloudSqlSettingsOut",
        "PostgreSqlConnectionProfileIn": "_datamigration_52_PostgreSqlConnectionProfileIn",
        "PostgreSqlConnectionProfileOut": "_datamigration_53_PostgreSqlConnectionProfileOut",
        "TestIamPermissionsResponseIn": "_datamigration_54_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_datamigration_55_TestIamPermissionsResponseOut",
        "SqlIpConfigIn": "_datamigration_56_SqlIpConfigIn",
        "SqlIpConfigOut": "_datamigration_57_SqlIpConfigOut",
        "ListConversionWorkspacesResponseIn": "_datamigration_58_ListConversionWorkspacesResponseIn",
        "ListConversionWorkspacesResponseOut": "_datamigration_59_ListConversionWorkspacesResponseOut",
        "DatabaseEntityIn": "_datamigration_60_DatabaseEntityIn",
        "DatabaseEntityOut": "_datamigration_61_DatabaseEntityOut",
        "ViewEntityIn": "_datamigration_62_ViewEntityIn",
        "ViewEntityOut": "_datamigration_63_ViewEntityOut",
        "MachineConfigIn": "_datamigration_64_MachineConfigIn",
        "MachineConfigOut": "_datamigration_65_MachineConfigOut",
        "ImportMappingRulesRequestIn": "_datamigration_66_ImportMappingRulesRequestIn",
        "ImportMappingRulesRequestOut": "_datamigration_67_ImportMappingRulesRequestOut",
        "AuditLogConfigIn": "_datamigration_68_AuditLogConfigIn",
        "AuditLogConfigOut": "_datamigration_69_AuditLogConfigOut",
        "StartMigrationJobRequestIn": "_datamigration_70_StartMigrationJobRequestIn",
        "StartMigrationJobRequestOut": "_datamigration_71_StartMigrationJobRequestOut",
        "ReverseSshConnectivityIn": "_datamigration_72_ReverseSshConnectivityIn",
        "ReverseSshConnectivityOut": "_datamigration_73_ReverseSshConnectivityOut",
        "VpcPeeringConfigIn": "_datamigration_74_VpcPeeringConfigIn",
        "VpcPeeringConfigOut": "_datamigration_75_VpcPeeringConfigOut",
        "SetIamPolicyRequestIn": "_datamigration_76_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_datamigration_77_SetIamPolicyRequestOut",
        "SeedJobDetailsIn": "_datamigration_78_SeedJobDetailsIn",
        "SeedJobDetailsOut": "_datamigration_79_SeedJobDetailsOut",
        "MigrationJobIn": "_datamigration_80_MigrationJobIn",
        "MigrationJobOut": "_datamigration_81_MigrationJobOut",
        "OperationIn": "_datamigration_82_OperationIn",
        "OperationOut": "_datamigration_83_OperationOut",
        "DatabaseTypeIn": "_datamigration_84_DatabaseTypeIn",
        "DatabaseTypeOut": "_datamigration_85_DatabaseTypeOut",
        "ListLocationsResponseIn": "_datamigration_86_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_datamigration_87_ListLocationsResponseOut",
        "EmptyIn": "_datamigration_88_EmptyIn",
        "EmptyOut": "_datamigration_89_EmptyOut",
        "CommitConversionWorkspaceRequestIn": "_datamigration_90_CommitConversionWorkspaceRequestIn",
        "CommitConversionWorkspaceRequestOut": "_datamigration_91_CommitConversionWorkspaceRequestOut",
        "ConvertConversionWorkspaceRequestIn": "_datamigration_92_ConvertConversionWorkspaceRequestIn",
        "ConvertConversionWorkspaceRequestOut": "_datamigration_93_ConvertConversionWorkspaceRequestOut",
        "ImportRulesJobDetailsIn": "_datamigration_94_ImportRulesJobDetailsIn",
        "ImportRulesJobDetailsOut": "_datamigration_95_ImportRulesJobDetailsOut",
        "SchemaEntityIn": "_datamigration_96_SchemaEntityIn",
        "SchemaEntityOut": "_datamigration_97_SchemaEntityOut",
        "IndexEntityIn": "_datamigration_98_IndexEntityIn",
        "IndexEntityOut": "_datamigration_99_IndexEntityOut",
        "RestartMigrationJobRequestIn": "_datamigration_100_RestartMigrationJobRequestIn",
        "RestartMigrationJobRequestOut": "_datamigration_101_RestartMigrationJobRequestOut",
        "ConversionWorkspaceIn": "_datamigration_102_ConversionWorkspaceIn",
        "ConversionWorkspaceOut": "_datamigration_103_ConversionWorkspaceOut",
        "ConvertJobDetailsIn": "_datamigration_104_ConvertJobDetailsIn",
        "ConvertJobDetailsOut": "_datamigration_105_ConvertJobDetailsOut",
        "ColumnEntityIn": "_datamigration_106_ColumnEntityIn",
        "ColumnEntityOut": "_datamigration_107_ColumnEntityOut",
        "SeedConversionWorkspaceRequestIn": "_datamigration_108_SeedConversionWorkspaceRequestIn",
        "SeedConversionWorkspaceRequestOut": "_datamigration_109_SeedConversionWorkspaceRequestOut",
        "ListPrivateConnectionsResponseIn": "_datamigration_110_ListPrivateConnectionsResponseIn",
        "ListPrivateConnectionsResponseOut": "_datamigration_111_ListPrivateConnectionsResponseOut",
        "LocationIn": "_datamigration_112_LocationIn",
        "LocationOut": "_datamigration_113_LocationOut",
        "ApplyConversionWorkspaceRequestIn": "_datamigration_114_ApplyConversionWorkspaceRequestIn",
        "ApplyConversionWorkspaceRequestOut": "_datamigration_115_ApplyConversionWorkspaceRequestOut",
        "EntityMappingIn": "_datamigration_116_EntityMappingIn",
        "EntityMappingOut": "_datamigration_117_EntityMappingOut",
        "FunctionEntityIn": "_datamigration_118_FunctionEntityIn",
        "FunctionEntityOut": "_datamigration_119_FunctionEntityOut",
        "GenerateSshScriptRequestIn": "_datamigration_120_GenerateSshScriptRequestIn",
        "GenerateSshScriptRequestOut": "_datamigration_121_GenerateSshScriptRequestOut",
        "PrivateConnectivityIn": "_datamigration_122_PrivateConnectivityIn",
        "PrivateConnectivityOut": "_datamigration_123_PrivateConnectivityOut",
        "SshScriptIn": "_datamigration_124_SshScriptIn",
        "SshScriptOut": "_datamigration_125_SshScriptOut",
        "AlloyDbSettingsIn": "_datamigration_126_AlloyDbSettingsIn",
        "AlloyDbSettingsOut": "_datamigration_127_AlloyDbSettingsOut",
        "RulesFileIn": "_datamigration_128_RulesFileIn",
        "RulesFileOut": "_datamigration_129_RulesFileOut",
        "VmSelectionConfigIn": "_datamigration_130_VmSelectionConfigIn",
        "VmSelectionConfigOut": "_datamigration_131_VmSelectionConfigOut",
        "PromoteMigrationJobRequestIn": "_datamigration_132_PromoteMigrationJobRequestIn",
        "PromoteMigrationJobRequestOut": "_datamigration_133_PromoteMigrationJobRequestOut",
        "ListMigrationJobsResponseIn": "_datamigration_134_ListMigrationJobsResponseIn",
        "ListMigrationJobsResponseOut": "_datamigration_135_ListMigrationJobsResponseOut",
        "ConversionWorkspaceInfoIn": "_datamigration_136_ConversionWorkspaceInfoIn",
        "ConversionWorkspaceInfoOut": "_datamigration_137_ConversionWorkspaceInfoOut",
        "ExprIn": "_datamigration_138_ExprIn",
        "ExprOut": "_datamigration_139_ExprOut",
        "TableEntityIn": "_datamigration_140_TableEntityIn",
        "TableEntityOut": "_datamigration_141_TableEntityOut",
        "OracleConnectionProfileIn": "_datamigration_142_OracleConnectionProfileIn",
        "OracleConnectionProfileOut": "_datamigration_143_OracleConnectionProfileOut",
        "ConstraintEntityIn": "_datamigration_144_ConstraintEntityIn",
        "ConstraintEntityOut": "_datamigration_145_ConstraintEntityOut",
        "SslConfigIn": "_datamigration_146_SslConfigIn",
        "SslConfigOut": "_datamigration_147_SslConfigOut",
        "ApplyJobDetailsIn": "_datamigration_148_ApplyJobDetailsIn",
        "ApplyJobDetailsOut": "_datamigration_149_ApplyJobDetailsOut",
        "ListOperationsResponseIn": "_datamigration_150_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_datamigration_151_ListOperationsResponseOut",
        "DatabaseEngineInfoIn": "_datamigration_152_DatabaseEngineInfoIn",
        "DatabaseEngineInfoOut": "_datamigration_153_DatabaseEngineInfoOut",
        "TriggerEntityIn": "_datamigration_154_TriggerEntityIn",
        "TriggerEntityOut": "_datamigration_155_TriggerEntityOut",
        "CancelOperationRequestIn": "_datamigration_156_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_datamigration_157_CancelOperationRequestOut",
        "TestIamPermissionsRequestIn": "_datamigration_158_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_datamigration_159_TestIamPermissionsRequestOut",
        "BindingIn": "_datamigration_160_BindingIn",
        "BindingOut": "_datamigration_161_BindingOut",
        "PrivateServiceConnectConnectivityIn": "_datamigration_162_PrivateServiceConnectConnectivityIn",
        "PrivateServiceConnectConnectivityOut": "_datamigration_163_PrivateServiceConnectConnectivityOut",
        "DescribeConversionWorkspaceRevisionsResponseIn": "_datamigration_164_DescribeConversionWorkspaceRevisionsResponseIn",
        "DescribeConversionWorkspaceRevisionsResponseOut": "_datamigration_165_DescribeConversionWorkspaceRevisionsResponseOut",
        "DumpFlagIn": "_datamigration_166_DumpFlagIn",
        "DumpFlagOut": "_datamigration_167_DumpFlagOut",
        "PolicyIn": "_datamigration_168_PolicyIn",
        "PolicyOut": "_datamigration_169_PolicyOut",
        "VerifyMigrationJobRequestIn": "_datamigration_170_VerifyMigrationJobRequestIn",
        "VerifyMigrationJobRequestOut": "_datamigration_171_VerifyMigrationJobRequestOut",
        "ListConnectionProfilesResponseIn": "_datamigration_172_ListConnectionProfilesResponseIn",
        "ListConnectionProfilesResponseOut": "_datamigration_173_ListConnectionProfilesResponseOut",
        "PackageEntityIn": "_datamigration_174_PackageEntityIn",
        "PackageEntityOut": "_datamigration_175_PackageEntityOut",
        "DumpFlagsIn": "_datamigration_176_DumpFlagsIn",
        "DumpFlagsOut": "_datamigration_177_DumpFlagsOut",
        "ConnectionProfileIn": "_datamigration_178_ConnectionProfileIn",
        "ConnectionProfileOut": "_datamigration_179_ConnectionProfileOut",
        "MigrationJobVerificationErrorIn": "_datamigration_180_MigrationJobVerificationErrorIn",
        "MigrationJobVerificationErrorOut": "_datamigration_181_MigrationJobVerificationErrorOut",
        "StoredProcedureEntityIn": "_datamigration_182_StoredProcedureEntityIn",
        "StoredProcedureEntityOut": "_datamigration_183_StoredProcedureEntityOut",
        "EntityMappingLogEntryIn": "_datamigration_184_EntityMappingLogEntryIn",
        "EntityMappingLogEntryOut": "_datamigration_185_EntityMappingLogEntryOut",
        "SqlAclEntryIn": "_datamigration_186_SqlAclEntryIn",
        "SqlAclEntryOut": "_datamigration_187_SqlAclEntryOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudClouddmsV1OperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudClouddmsV1OperationMetadataIn"])
    types["GoogleCloudClouddmsV1OperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudClouddmsV1OperationMetadataOut"])
    types["MySqlConnectionProfileIn"] = t.struct(
        {
            "username": t.string(),
            "cloudSqlId": t.string().optional(),
            "host": t.string(),
            "port": t.integer(),
            "password": t.string(),
            "ssl": t.proxy(renames["SslConfigIn"]).optional(),
        }
    ).named(renames["MySqlConnectionProfileIn"])
    types["MySqlConnectionProfileOut"] = t.struct(
        {
            "passwordSet": t.boolean().optional(),
            "username": t.string(),
            "cloudSqlId": t.string().optional(),
            "host": t.string(),
            "port": t.integer(),
            "password": t.string(),
            "ssl": t.proxy(renames["SslConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MySqlConnectionProfileOut"])
    types["AlloyDbConnectionProfileIn"] = t.struct(
        {
            "settings": t.proxy(renames["AlloyDbSettingsIn"]).optional(),
            "clusterId": t.string(),
        }
    ).named(renames["AlloyDbConnectionProfileIn"])
    types["AlloyDbConnectionProfileOut"] = t.struct(
        {
            "settings": t.proxy(renames["AlloyDbSettingsOut"]).optional(),
            "clusterId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlloyDbConnectionProfileOut"])
    types["PrivateConnectionIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "vpcPeeringConfig": t.proxy(renames["VpcPeeringConfigIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PrivateConnectionIn"])
    types["PrivateConnectionOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "vpcPeeringConfig": t.proxy(renames["VpcPeeringConfigOut"]).optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateConnectionOut"])
    types["StopMigrationJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StopMigrationJobRequestIn"]
    )
    types["StopMigrationJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StopMigrationJobRequestOut"])
    types["ResumeMigrationJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResumeMigrationJobRequestIn"]
    )
    types["ResumeMigrationJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumeMigrationJobRequestOut"])
    types["VmCreationConfigIn"] = t.struct(
        {
            "vmMachineType": t.string(),
            "vmZone": t.string().optional(),
            "subnet": t.string().optional(),
        }
    ).named(renames["VmCreationConfigIn"])
    types["VmCreationConfigOut"] = t.struct(
        {
            "vmMachineType": t.string(),
            "vmZone": t.string().optional(),
            "subnet": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmCreationConfigOut"])
    types["CloudSqlConnectionProfileIn"] = t.struct(
        {"settings": t.proxy(renames["CloudSqlSettingsIn"]).optional()}
    ).named(renames["CloudSqlConnectionProfileIn"])
    types["CloudSqlConnectionProfileOut"] = t.struct(
        {
            "privateIp": t.string().optional(),
            "cloudSqlId": t.string().optional(),
            "publicIp": t.string().optional(),
            "settings": t.proxy(renames["CloudSqlSettingsOut"]).optional(),
            "additionalPublicIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudSqlConnectionProfileOut"])
    types["StaticServiceIpConnectivityIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["StaticServiceIpConnectivityIn"])
    types["StaticServiceIpConnectivityOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StaticServiceIpConnectivityOut"])
    types["SearchBackgroundJobsResponseIn"] = t.struct(
        {"jobs": t.array(t.proxy(renames["BackgroundJobLogEntryIn"])).optional()}
    ).named(renames["SearchBackgroundJobsResponseIn"])
    types["SearchBackgroundJobsResponseOut"] = t.struct(
        {
            "jobs": t.array(t.proxy(renames["BackgroundJobLogEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchBackgroundJobsResponseOut"])
    types["ForwardSshTunnelConnectivityIn"] = t.struct(
        {
            "username": t.string(),
            "privateKey": t.string().optional(),
            "password": t.string().optional(),
            "hostname": t.string(),
            "port": t.integer().optional(),
        }
    ).named(renames["ForwardSshTunnelConnectivityIn"])
    types["ForwardSshTunnelConnectivityOut"] = t.struct(
        {
            "username": t.string(),
            "privateKey": t.string().optional(),
            "password": t.string().optional(),
            "hostname": t.string(),
            "port": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ForwardSshTunnelConnectivityOut"])
    types["EncryptionConfigIn"] = t.struct({"kmsKeyName": t.string().optional()}).named(
        renames["EncryptionConfigIn"]
    )
    types["EncryptionConfigOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionConfigOut"])
    types["DescribeDatabaseEntitiesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "databaseEntities": t.array(
                t.proxy(renames["DatabaseEntityIn"])
            ).optional(),
        }
    ).named(renames["DescribeDatabaseEntitiesResponseIn"])
    types["DescribeDatabaseEntitiesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "databaseEntities": t.array(
                t.proxy(renames["DatabaseEntityOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DescribeDatabaseEntitiesResponseOut"])
    types["SequenceEntityIn"] = t.struct(
        {
            "cycle": t.boolean().optional(),
            "minValue": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "maxValue": t.string().optional(),
            "increment": t.string().optional(),
            "startValue": t.string().optional(),
            "cache": t.string().optional(),
        }
    ).named(renames["SequenceEntityIn"])
    types["SequenceEntityOut"] = t.struct(
        {
            "cycle": t.boolean().optional(),
            "minValue": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "maxValue": t.string().optional(),
            "increment": t.string().optional(),
            "startValue": t.string().optional(),
            "cache": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SequenceEntityOut"])
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
    types["RollbackConversionWorkspaceRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RollbackConversionWorkspaceRequestIn"])
    types["RollbackConversionWorkspaceRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RollbackConversionWorkspaceRequestOut"])
    types["StaticIpConnectivityIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StaticIpConnectivityIn"]
    )
    types["StaticIpConnectivityOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StaticIpConnectivityOut"])
    types["VpcPeeringConnectivityIn"] = t.struct({"vpc": t.string().optional()}).named(
        renames["VpcPeeringConnectivityIn"]
    )
    types["VpcPeeringConnectivityOut"] = t.struct(
        {
            "vpc": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VpcPeeringConnectivityOut"])
    types["PrimaryInstanceSettingsIn"] = t.struct(
        {
            "databaseFlags": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string(),
            "machineConfig": t.proxy(renames["MachineConfigIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PrimaryInstanceSettingsIn"])
    types["PrimaryInstanceSettingsOut"] = t.struct(
        {
            "privateIp": t.string().optional(),
            "databaseFlags": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string(),
            "machineConfig": t.proxy(renames["MachineConfigOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrimaryInstanceSettingsOut"])
    types["UserPasswordIn"] = t.struct(
        {"password": t.string().optional(), "user": t.string().optional()}
    ).named(renames["UserPasswordIn"])
    types["UserPasswordOut"] = t.struct(
        {
            "password": t.string().optional(),
            "passwordSet": t.boolean().optional(),
            "user": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserPasswordOut"])
    types["BackgroundJobLogEntryIn"] = t.struct(
        {
            "finishTime": t.string().optional(),
            "completionComment": t.string().optional(),
            "jobType": t.string().optional(),
            "startTime": t.string().optional(),
            "convertJobDetails": t.proxy(renames["ConvertJobDetailsIn"]).optional(),
            "seedJobDetails": t.proxy(renames["SeedJobDetailsIn"]).optional(),
            "id": t.string().optional(),
            "importRulesJobDetails": t.proxy(
                renames["ImportRulesJobDetailsIn"]
            ).optional(),
            "completionState": t.string().optional(),
            "requestAutocommit": t.boolean().optional(),
            "applyJobDetails": t.proxy(renames["ApplyJobDetailsIn"]).optional(),
        }
    ).named(renames["BackgroundJobLogEntryIn"])
    types["BackgroundJobLogEntryOut"] = t.struct(
        {
            "finishTime": t.string().optional(),
            "completionComment": t.string().optional(),
            "jobType": t.string().optional(),
            "startTime": t.string().optional(),
            "convertJobDetails": t.proxy(renames["ConvertJobDetailsOut"]).optional(),
            "seedJobDetails": t.proxy(renames["SeedJobDetailsOut"]).optional(),
            "id": t.string().optional(),
            "importRulesJobDetails": t.proxy(
                renames["ImportRulesJobDetailsOut"]
            ).optional(),
            "completionState": t.string().optional(),
            "requestAutocommit": t.boolean().optional(),
            "applyJobDetails": t.proxy(renames["ApplyJobDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackgroundJobLogEntryOut"])
    types["FetchStaticIpsResponseIn"] = t.struct(
        {
            "staticIps": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["FetchStaticIpsResponseIn"])
    types["FetchStaticIpsResponseOut"] = t.struct(
        {
            "staticIps": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchStaticIpsResponseOut"])
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
    types["SynonymEntityIn"] = t.struct(
        {
            "sourceType": t.string().optional(),
            "sourceEntity": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SynonymEntityIn"])
    types["SynonymEntityOut"] = t.struct(
        {
            "sourceType": t.string().optional(),
            "sourceEntity": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SynonymEntityOut"])
    types["CloudSqlSettingsIn"] = t.struct(
        {
            "dataDiskType": t.string().optional(),
            "databaseFlags": t.struct({"_": t.string().optional()}).optional(),
            "rootPassword": t.string().optional(),
            "collation": t.string().optional(),
            "ipConfig": t.proxy(renames["SqlIpConfigIn"]).optional(),
            "autoStorageIncrease": t.boolean().optional(),
            "zone": t.string().optional(),
            "tier": t.string().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "storageAutoResizeLimit": t.string().optional(),
            "activationPolicy": t.string().optional(),
            "cmekKeyName": t.string().optional(),
            "sourceId": t.string().optional(),
            "edition": t.string().optional(),
            "availabilityType": t.string().optional(),
            "databaseVersion": t.string().optional(),
            "dataDiskSizeGb": t.string().optional(),
            "secondaryZone": t.string().optional(),
        }
    ).named(renames["CloudSqlSettingsIn"])
    types["CloudSqlSettingsOut"] = t.struct(
        {
            "dataDiskType": t.string().optional(),
            "databaseFlags": t.struct({"_": t.string().optional()}).optional(),
            "rootPassword": t.string().optional(),
            "collation": t.string().optional(),
            "ipConfig": t.proxy(renames["SqlIpConfigOut"]).optional(),
            "autoStorageIncrease": t.boolean().optional(),
            "zone": t.string().optional(),
            "tier": t.string().optional(),
            "rootPasswordSet": t.boolean().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "storageAutoResizeLimit": t.string().optional(),
            "activationPolicy": t.string().optional(),
            "cmekKeyName": t.string().optional(),
            "sourceId": t.string().optional(),
            "edition": t.string().optional(),
            "availabilityType": t.string().optional(),
            "databaseVersion": t.string().optional(),
            "dataDiskSizeGb": t.string().optional(),
            "secondaryZone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudSqlSettingsOut"])
    types["PostgreSqlConnectionProfileIn"] = t.struct(
        {
            "privateServiceConnectConnectivity": t.proxy(
                renames["PrivateServiceConnectConnectivityIn"]
            ).optional(),
            "host": t.string(),
            "username": t.string(),
            "port": t.integer(),
            "cloudSqlId": t.string().optional(),
            "ssl": t.proxy(renames["SslConfigIn"]).optional(),
            "password": t.string(),
            "staticIpConnectivity": t.proxy(
                renames["StaticIpConnectivityIn"]
            ).optional(),
        }
    ).named(renames["PostgreSqlConnectionProfileIn"])
    types["PostgreSqlConnectionProfileOut"] = t.struct(
        {
            "passwordSet": t.boolean().optional(),
            "privateServiceConnectConnectivity": t.proxy(
                renames["PrivateServiceConnectConnectivityOut"]
            ).optional(),
            "host": t.string(),
            "username": t.string(),
            "port": t.integer(),
            "cloudSqlId": t.string().optional(),
            "ssl": t.proxy(renames["SslConfigOut"]).optional(),
            "password": t.string(),
            "networkArchitecture": t.string().optional(),
            "staticIpConnectivity": t.proxy(
                renames["StaticIpConnectivityOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostgreSqlConnectionProfileOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["SqlIpConfigIn"] = t.struct(
        {
            "allocatedIpRange": t.string().optional(),
            "authorizedNetworks": t.array(t.proxy(renames["SqlAclEntryIn"])).optional(),
            "enableIpv4": t.boolean().optional(),
            "requireSsl": t.boolean().optional(),
            "privateNetwork": t.string().optional(),
        }
    ).named(renames["SqlIpConfigIn"])
    types["SqlIpConfigOut"] = t.struct(
        {
            "allocatedIpRange": t.string().optional(),
            "authorizedNetworks": t.array(
                t.proxy(renames["SqlAclEntryOut"])
            ).optional(),
            "enableIpv4": t.boolean().optional(),
            "requireSsl": t.boolean().optional(),
            "privateNetwork": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlIpConfigOut"])
    types["ListConversionWorkspacesResponseIn"] = t.struct(
        {
            "conversionWorkspaces": t.array(
                t.proxy(renames["ConversionWorkspaceIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListConversionWorkspacesResponseIn"])
    types["ListConversionWorkspacesResponseOut"] = t.struct(
        {
            "conversionWorkspaces": t.array(
                t.proxy(renames["ConversionWorkspaceOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConversionWorkspacesResponseOut"])
    types["DatabaseEntityIn"] = t.struct(
        {
            "parentEntity": t.string().optional(),
            "tree": t.string().optional(),
            "storedProcedure": t.proxy(renames["StoredProcedureEntityIn"]).optional(),
            "view": t.proxy(renames["ViewEntityIn"]).optional(),
            "table": t.proxy(renames["TableEntityIn"]).optional(),
            "databasePackage": t.proxy(renames["PackageEntityIn"]).optional(),
            "entityType": t.string().optional(),
            "mappings": t.array(t.proxy(renames["EntityMappingIn"])).optional(),
            "shortName": t.string().optional(),
            "schema": t.proxy(renames["SchemaEntityIn"]).optional(),
            "databaseFunction": t.proxy(renames["FunctionEntityIn"]).optional(),
            "synonym": t.proxy(renames["SynonymEntityIn"]).optional(),
            "sequence": t.proxy(renames["SequenceEntityIn"]).optional(),
        }
    ).named(renames["DatabaseEntityIn"])
    types["DatabaseEntityOut"] = t.struct(
        {
            "parentEntity": t.string().optional(),
            "tree": t.string().optional(),
            "storedProcedure": t.proxy(renames["StoredProcedureEntityOut"]).optional(),
            "view": t.proxy(renames["ViewEntityOut"]).optional(),
            "table": t.proxy(renames["TableEntityOut"]).optional(),
            "databasePackage": t.proxy(renames["PackageEntityOut"]).optional(),
            "entityType": t.string().optional(),
            "mappings": t.array(t.proxy(renames["EntityMappingOut"])).optional(),
            "shortName": t.string().optional(),
            "schema": t.proxy(renames["SchemaEntityOut"]).optional(),
            "databaseFunction": t.proxy(renames["FunctionEntityOut"]).optional(),
            "synonym": t.proxy(renames["SynonymEntityOut"]).optional(),
            "sequence": t.proxy(renames["SequenceEntityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseEntityOut"])
    types["ViewEntityIn"] = t.struct(
        {
            "constraints": t.array(t.proxy(renames["ConstraintEntityIn"])).optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "sqlCode": t.string().optional(),
        }
    ).named(renames["ViewEntityIn"])
    types["ViewEntityOut"] = t.struct(
        {
            "constraints": t.array(t.proxy(renames["ConstraintEntityOut"])).optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "sqlCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViewEntityOut"])
    types["MachineConfigIn"] = t.struct({"cpuCount": t.integer().optional()}).named(
        renames["MachineConfigIn"]
    )
    types["MachineConfigOut"] = t.struct(
        {
            "cpuCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MachineConfigOut"])
    types["ImportMappingRulesRequestIn"] = t.struct(
        {
            "rulesFormat": t.string().optional(),
            "autoCommit": t.boolean().optional(),
            "rulesFiles": t.array(t.proxy(renames["RulesFileIn"])).optional(),
        }
    ).named(renames["ImportMappingRulesRequestIn"])
    types["ImportMappingRulesRequestOut"] = t.struct(
        {
            "rulesFormat": t.string().optional(),
            "autoCommit": t.boolean().optional(),
            "rulesFiles": t.array(t.proxy(renames["RulesFileOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportMappingRulesRequestOut"])
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
    types["StartMigrationJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StartMigrationJobRequestIn"]
    )
    types["StartMigrationJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StartMigrationJobRequestOut"])
    types["ReverseSshConnectivityIn"] = t.struct(
        {
            "vmPort": t.integer(),
            "vpc": t.string().optional(),
            "vmIp": t.string(),
            "vm": t.string().optional(),
        }
    ).named(renames["ReverseSshConnectivityIn"])
    types["ReverseSshConnectivityOut"] = t.struct(
        {
            "vmPort": t.integer(),
            "vpc": t.string().optional(),
            "vmIp": t.string(),
            "vm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReverseSshConnectivityOut"])
    types["VpcPeeringConfigIn"] = t.struct(
        {"subnet": t.string(), "vpcName": t.string()}
    ).named(renames["VpcPeeringConfigIn"])
    types["VpcPeeringConfigOut"] = t.struct(
        {
            "subnet": t.string(),
            "vpcName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VpcPeeringConfigOut"])
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
    types["SeedJobDetailsIn"] = t.struct(
        {"connectionProfile": t.string().optional()}
    ).named(renames["SeedJobDetailsIn"])
    types["SeedJobDetailsOut"] = t.struct(
        {
            "connectionProfile": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SeedJobDetailsOut"])
    types["MigrationJobIn"] = t.struct(
        {
            "destinationDatabase": t.proxy(renames["DatabaseTypeIn"]).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "dumpPath": t.string().optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "staticIpConnectivity": t.proxy(
                renames["StaticIpConnectivityIn"]
            ).optional(),
            "sourceDatabase": t.proxy(renames["DatabaseTypeIn"]).optional(),
            "conversionWorkspace": t.proxy(
                renames["ConversionWorkspaceInfoIn"]
            ).optional(),
            "vpcPeeringConnectivity": t.proxy(
                renames["VpcPeeringConnectivityIn"]
            ).optional(),
            "reverseSshConnectivity": t.proxy(
                renames["ReverseSshConnectivityIn"]
            ).optional(),
            "filter": t.string().optional(),
            "source": t.string(),
            "type": t.string(),
            "destination": t.string(),
            "cmekKeyName": t.string().optional(),
            "dumpFlags": t.proxy(renames["DumpFlagsIn"]).optional(),
        }
    ).named(renames["MigrationJobIn"])
    types["MigrationJobOut"] = t.struct(
        {
            "destinationDatabase": t.proxy(renames["DatabaseTypeOut"]).optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "dumpPath": t.string().optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "staticIpConnectivity": t.proxy(
                renames["StaticIpConnectivityOut"]
            ).optional(),
            "sourceDatabase": t.proxy(renames["DatabaseTypeOut"]).optional(),
            "conversionWorkspace": t.proxy(
                renames["ConversionWorkspaceInfoOut"]
            ).optional(),
            "vpcPeeringConnectivity": t.proxy(
                renames["VpcPeeringConnectivityOut"]
            ).optional(),
            "reverseSshConnectivity": t.proxy(
                renames["ReverseSshConnectivityOut"]
            ).optional(),
            "filter": t.string().optional(),
            "source": t.string(),
            "type": t.string(),
            "duration": t.string().optional(),
            "createTime": t.string().optional(),
            "destination": t.string(),
            "cmekKeyName": t.string().optional(),
            "dumpFlags": t.proxy(renames["DumpFlagsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "endTime": t.string().optional(),
            "phase": t.string().optional(),
        }
    ).named(renames["MigrationJobOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["DatabaseTypeIn"] = t.struct(
        {"engine": t.string().optional(), "provider": t.string().optional()}
    ).named(renames["DatabaseTypeIn"])
    types["DatabaseTypeOut"] = t.struct(
        {
            "engine": t.string().optional(),
            "provider": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseTypeOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["CommitConversionWorkspaceRequestIn"] = t.struct(
        {"commitName": t.string().optional()}
    ).named(renames["CommitConversionWorkspaceRequestIn"])
    types["CommitConversionWorkspaceRequestOut"] = t.struct(
        {
            "commitName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitConversionWorkspaceRequestOut"])
    types["ConvertConversionWorkspaceRequestIn"] = t.struct(
        {"autoCommit": t.boolean().optional(), "filter": t.string().optional()}
    ).named(renames["ConvertConversionWorkspaceRequestIn"])
    types["ConvertConversionWorkspaceRequestOut"] = t.struct(
        {
            "autoCommit": t.boolean().optional(),
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConvertConversionWorkspaceRequestOut"])
    types["ImportRulesJobDetailsIn"] = t.struct(
        {"files": t.array(t.string()).optional(), "fileFormat": t.string().optional()}
    ).named(renames["ImportRulesJobDetailsIn"])
    types["ImportRulesJobDetailsOut"] = t.struct(
        {
            "files": t.array(t.string()).optional(),
            "fileFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportRulesJobDetailsOut"])
    types["SchemaEntityIn"] = t.struct(
        {"customFeatures": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["SchemaEntityIn"])
    types["SchemaEntityOut"] = t.struct(
        {
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaEntityOut"])
    types["IndexEntityIn"] = t.struct(
        {
            "unique": t.boolean().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "tableColumns": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["IndexEntityIn"])
    types["IndexEntityOut"] = t.struct(
        {
            "unique": t.boolean().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "tableColumns": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexEntityOut"])
    types["RestartMigrationJobRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RestartMigrationJobRequestIn"])
    types["RestartMigrationJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RestartMigrationJobRequestOut"])
    types["ConversionWorkspaceIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "globalSettings": t.struct({"_": t.string().optional()}).optional(),
            "source": t.proxy(renames["DatabaseEngineInfoIn"]),
            "destination": t.proxy(renames["DatabaseEngineInfoIn"]),
            "name": t.string().optional(),
        }
    ).named(renames["ConversionWorkspaceIn"])
    types["ConversionWorkspaceOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "latestCommitTime": t.string().optional(),
            "globalSettings": t.struct({"_": t.string().optional()}).optional(),
            "source": t.proxy(renames["DatabaseEngineInfoOut"]),
            "latestCommitId": t.string().optional(),
            "createTime": t.string().optional(),
            "destination": t.proxy(renames["DatabaseEngineInfoOut"]),
            "hasUncommittedChanges": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConversionWorkspaceOut"])
    types["ConvertJobDetailsIn"] = t.struct({"filter": t.string().optional()}).named(
        renames["ConvertJobDetailsIn"]
    )
    types["ConvertJobDetailsOut"] = t.struct(
        {
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConvertJobDetailsOut"])
    types["ColumnEntityIn"] = t.struct(
        {
            "scale": t.integer().optional(),
            "autoGenerated": t.boolean().optional(),
            "length": t.string().optional(),
            "comment": t.string().optional(),
            "name": t.string().optional(),
            "arrayLength": t.integer().optional(),
            "defaultValue": t.string().optional(),
            "udt": t.boolean().optional(),
            "collation": t.string().optional(),
            "nullable": t.boolean().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "array": t.boolean().optional(),
            "setValues": t.array(t.string()).optional(),
            "dataType": t.string().optional(),
            "precision": t.integer().optional(),
            "charset": t.string().optional(),
            "ordinalPosition": t.integer().optional(),
            "fractionalSecondsPrecision": t.integer().optional(),
        }
    ).named(renames["ColumnEntityIn"])
    types["ColumnEntityOut"] = t.struct(
        {
            "scale": t.integer().optional(),
            "autoGenerated": t.boolean().optional(),
            "length": t.string().optional(),
            "comment": t.string().optional(),
            "name": t.string().optional(),
            "arrayLength": t.integer().optional(),
            "defaultValue": t.string().optional(),
            "udt": t.boolean().optional(),
            "collation": t.string().optional(),
            "nullable": t.boolean().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "array": t.boolean().optional(),
            "setValues": t.array(t.string()).optional(),
            "dataType": t.string().optional(),
            "precision": t.integer().optional(),
            "charset": t.string().optional(),
            "ordinalPosition": t.integer().optional(),
            "fractionalSecondsPrecision": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColumnEntityOut"])
    types["SeedConversionWorkspaceRequestIn"] = t.struct(
        {
            "destinationConnectionProfile": t.string().optional(),
            "autoCommit": t.boolean().optional(),
            "sourceConnectionProfile": t.string().optional(),
        }
    ).named(renames["SeedConversionWorkspaceRequestIn"])
    types["SeedConversionWorkspaceRequestOut"] = t.struct(
        {
            "destinationConnectionProfile": t.string().optional(),
            "autoCommit": t.boolean().optional(),
            "sourceConnectionProfile": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SeedConversionWorkspaceRequestOut"])
    types["ListPrivateConnectionsResponseIn"] = t.struct(
        {
            "privateConnections": t.array(
                t.proxy(renames["PrivateConnectionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListPrivateConnectionsResponseIn"])
    types["ListPrivateConnectionsResponseOut"] = t.struct(
        {
            "privateConnections": t.array(
                t.proxy(renames["PrivateConnectionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPrivateConnectionsResponseOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["ApplyConversionWorkspaceRequestIn"] = t.struct(
        {"connectionProfile": t.string().optional(), "filter": t.string().optional()}
    ).named(renames["ApplyConversionWorkspaceRequestIn"])
    types["ApplyConversionWorkspaceRequestOut"] = t.struct(
        {
            "connectionProfile": t.string().optional(),
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplyConversionWorkspaceRequestOut"])
    types["EntityMappingIn"] = t.struct(
        {
            "sourceType": t.string().optional(),
            "draftEntity": t.string().optional(),
            "mappingLog": t.array(
                t.proxy(renames["EntityMappingLogEntryIn"])
            ).optional(),
            "sourceEntity": t.string().optional(),
            "draftType": t.string().optional(),
        }
    ).named(renames["EntityMappingIn"])
    types["EntityMappingOut"] = t.struct(
        {
            "sourceType": t.string().optional(),
            "draftEntity": t.string().optional(),
            "mappingLog": t.array(
                t.proxy(renames["EntityMappingLogEntryOut"])
            ).optional(),
            "sourceEntity": t.string().optional(),
            "draftType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityMappingOut"])
    types["FunctionEntityIn"] = t.struct(
        {
            "sqlCode": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["FunctionEntityIn"])
    types["FunctionEntityOut"] = t.struct(
        {
            "sqlCode": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FunctionEntityOut"])
    types["GenerateSshScriptRequestIn"] = t.struct(
        {
            "vmCreationConfig": t.proxy(renames["VmCreationConfigIn"]).optional(),
            "vmSelectionConfig": t.proxy(renames["VmSelectionConfigIn"]).optional(),
            "vmPort": t.integer().optional(),
            "vm": t.string(),
        }
    ).named(renames["GenerateSshScriptRequestIn"])
    types["GenerateSshScriptRequestOut"] = t.struct(
        {
            "vmCreationConfig": t.proxy(renames["VmCreationConfigOut"]).optional(),
            "vmSelectionConfig": t.proxy(renames["VmSelectionConfigOut"]).optional(),
            "vmPort": t.integer().optional(),
            "vm": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateSshScriptRequestOut"])
    types["PrivateConnectivityIn"] = t.struct({"privateConnection": t.string()}).named(
        renames["PrivateConnectivityIn"]
    )
    types["PrivateConnectivityOut"] = t.struct(
        {
            "privateConnection": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateConnectivityOut"])
    types["SshScriptIn"] = t.struct({"script": t.string().optional()}).named(
        renames["SshScriptIn"]
    )
    types["SshScriptOut"] = t.struct(
        {
            "script": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SshScriptOut"])
    types["AlloyDbSettingsIn"] = t.struct(
        {
            "encryptionConfig": t.proxy(renames["EncryptionConfigIn"]).optional(),
            "primaryInstanceSettings": t.proxy(renames["PrimaryInstanceSettingsIn"]),
            "vpcNetwork": t.string(),
            "initialUser": t.proxy(renames["UserPasswordIn"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["AlloyDbSettingsIn"])
    types["AlloyDbSettingsOut"] = t.struct(
        {
            "encryptionConfig": t.proxy(renames["EncryptionConfigOut"]).optional(),
            "primaryInstanceSettings": t.proxy(renames["PrimaryInstanceSettingsOut"]),
            "vpcNetwork": t.string(),
            "initialUser": t.proxy(renames["UserPasswordOut"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlloyDbSettingsOut"])
    types["RulesFileIn"] = t.struct(
        {
            "rulesContent": t.string().optional(),
            "rulesSourceFilename": t.string().optional(),
        }
    ).named(renames["RulesFileIn"])
    types["RulesFileOut"] = t.struct(
        {
            "rulesContent": t.string().optional(),
            "rulesSourceFilename": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RulesFileOut"])
    types["VmSelectionConfigIn"] = t.struct({"vmZone": t.string()}).named(
        renames["VmSelectionConfigIn"]
    )
    types["VmSelectionConfigOut"] = t.struct(
        {"vmZone": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VmSelectionConfigOut"])
    types["PromoteMigrationJobRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["PromoteMigrationJobRequestIn"])
    types["PromoteMigrationJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PromoteMigrationJobRequestOut"])
    types["ListMigrationJobsResponseIn"] = t.struct(
        {
            "migrationJobs": t.array(t.proxy(renames["MigrationJobIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListMigrationJobsResponseIn"])
    types["ListMigrationJobsResponseOut"] = t.struct(
        {
            "migrationJobs": t.array(t.proxy(renames["MigrationJobOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMigrationJobsResponseOut"])
    types["ConversionWorkspaceInfoIn"] = t.struct(
        {"commitId": t.string().optional(), "name": t.string().optional()}
    ).named(renames["ConversionWorkspaceInfoIn"])
    types["ConversionWorkspaceInfoOut"] = t.struct(
        {
            "commitId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConversionWorkspaceInfoOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["TableEntityIn"] = t.struct(
        {
            "triggers": t.array(t.proxy(renames["TriggerEntityIn"])).optional(),
            "columns": t.array(t.proxy(renames["ColumnEntityIn"])).optional(),
            "constraints": t.array(t.proxy(renames["ConstraintEntityIn"])).optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "indices": t.array(t.proxy(renames["IndexEntityIn"])).optional(),
            "comment": t.string().optional(),
        }
    ).named(renames["TableEntityIn"])
    types["TableEntityOut"] = t.struct(
        {
            "triggers": t.array(t.proxy(renames["TriggerEntityOut"])).optional(),
            "columns": t.array(t.proxy(renames["ColumnEntityOut"])).optional(),
            "constraints": t.array(t.proxy(renames["ConstraintEntityOut"])).optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "indices": t.array(t.proxy(renames["IndexEntityOut"])).optional(),
            "comment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableEntityOut"])
    types["OracleConnectionProfileIn"] = t.struct(
        {
            "staticServiceIpConnectivity": t.proxy(
                renames["StaticServiceIpConnectivityIn"]
            ).optional(),
            "privateConnectivity": t.proxy(renames["PrivateConnectivityIn"]).optional(),
            "username": t.string(),
            "forwardSshConnectivity": t.proxy(
                renames["ForwardSshTunnelConnectivityIn"]
            ).optional(),
            "databaseService": t.string(),
            "host": t.string(),
            "ssl": t.proxy(renames["SslConfigIn"]).optional(),
            "password": t.string(),
            "port": t.integer(),
        }
    ).named(renames["OracleConnectionProfileIn"])
    types["OracleConnectionProfileOut"] = t.struct(
        {
            "staticServiceIpConnectivity": t.proxy(
                renames["StaticServiceIpConnectivityOut"]
            ).optional(),
            "privateConnectivity": t.proxy(
                renames["PrivateConnectivityOut"]
            ).optional(),
            "username": t.string(),
            "forwardSshConnectivity": t.proxy(
                renames["ForwardSshTunnelConnectivityOut"]
            ).optional(),
            "databaseService": t.string(),
            "host": t.string(),
            "ssl": t.proxy(renames["SslConfigOut"]).optional(),
            "password": t.string(),
            "passwordSet": t.boolean().optional(),
            "port": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OracleConnectionProfileOut"])
    types["ConstraintEntityIn"] = t.struct(
        {
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "tableName": t.string().optional(),
            "type": t.string().optional(),
            "referenceColumns": t.array(t.string()).optional(),
            "tableColumns": t.array(t.string()).optional(),
            "referenceTable": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ConstraintEntityIn"])
    types["ConstraintEntityOut"] = t.struct(
        {
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "tableName": t.string().optional(),
            "type": t.string().optional(),
            "referenceColumns": t.array(t.string()).optional(),
            "tableColumns": t.array(t.string()).optional(),
            "referenceTable": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConstraintEntityOut"])
    types["SslConfigIn"] = t.struct(
        {
            "clientKey": t.string().optional(),
            "caCertificate": t.string(),
            "clientCertificate": t.string().optional(),
        }
    ).named(renames["SslConfigIn"])
    types["SslConfigOut"] = t.struct(
        {
            "clientKey": t.string().optional(),
            "caCertificate": t.string(),
            "type": t.string().optional(),
            "clientCertificate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SslConfigOut"])
    types["ApplyJobDetailsIn"] = t.struct(
        {"filter": t.string().optional(), "connectionProfile": t.string().optional()}
    ).named(renames["ApplyJobDetailsIn"])
    types["ApplyJobDetailsOut"] = t.struct(
        {
            "filter": t.string().optional(),
            "connectionProfile": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplyJobDetailsOut"])
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
    types["DatabaseEngineInfoIn"] = t.struct(
        {"engine": t.string(), "version": t.string()}
    ).named(renames["DatabaseEngineInfoIn"])
    types["DatabaseEngineInfoOut"] = t.struct(
        {
            "engine": t.string(),
            "version": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseEngineInfoOut"])
    types["TriggerEntityIn"] = t.struct(
        {
            "sqlCode": t.string().optional(),
            "triggerType": t.string().optional(),
            "name": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "triggeringEvents": t.array(t.string()).optional(),
        }
    ).named(renames["TriggerEntityIn"])
    types["TriggerEntityOut"] = t.struct(
        {
            "sqlCode": t.string().optional(),
            "triggerType": t.string().optional(),
            "name": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "triggeringEvents": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TriggerEntityOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["PrivateServiceConnectConnectivityIn"] = t.struct(
        {"serviceAttachment": t.string()}
    ).named(renames["PrivateServiceConnectConnectivityIn"])
    types["PrivateServiceConnectConnectivityOut"] = t.struct(
        {
            "serviceAttachment": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateServiceConnectConnectivityOut"])
    types["DescribeConversionWorkspaceRevisionsResponseIn"] = t.struct(
        {"revisions": t.array(t.proxy(renames["ConversionWorkspaceIn"])).optional()}
    ).named(renames["DescribeConversionWorkspaceRevisionsResponseIn"])
    types["DescribeConversionWorkspaceRevisionsResponseOut"] = t.struct(
        {
            "revisions": t.array(t.proxy(renames["ConversionWorkspaceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DescribeConversionWorkspaceRevisionsResponseOut"])
    types["DumpFlagIn"] = t.struct(
        {"value": t.string().optional(), "name": t.string().optional()}
    ).named(renames["DumpFlagIn"])
    types["DumpFlagOut"] = t.struct(
        {
            "value": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DumpFlagOut"])
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["VerifyMigrationJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VerifyMigrationJobRequestIn"]
    )
    types["VerifyMigrationJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VerifyMigrationJobRequestOut"])
    types["ListConnectionProfilesResponseIn"] = t.struct(
        {
            "connectionProfiles": t.array(
                t.proxy(renames["ConnectionProfileIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListConnectionProfilesResponseIn"])
    types["ListConnectionProfilesResponseOut"] = t.struct(
        {
            "connectionProfiles": t.array(
                t.proxy(renames["ConnectionProfileOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConnectionProfilesResponseOut"])
    types["PackageEntityIn"] = t.struct(
        {
            "packageSqlCode": t.string().optional(),
            "packageBody": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PackageEntityIn"])
    types["PackageEntityOut"] = t.struct(
        {
            "packageSqlCode": t.string().optional(),
            "packageBody": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageEntityOut"])
    types["DumpFlagsIn"] = t.struct(
        {"dumpFlags": t.array(t.proxy(renames["DumpFlagIn"])).optional()}
    ).named(renames["DumpFlagsIn"])
    types["DumpFlagsOut"] = t.struct(
        {
            "dumpFlags": t.array(t.proxy(renames["DumpFlagOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DumpFlagsOut"])
    types["ConnectionProfileIn"] = t.struct(
        {
            "oracle": t.proxy(renames["OracleConnectionProfileIn"]).optional(),
            "state": t.string().optional(),
            "mysql": t.proxy(renames["MySqlConnectionProfileIn"]).optional(),
            "name": t.string().optional(),
            "alloydb": t.proxy(renames["AlloyDbConnectionProfileIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "cloudsql": t.proxy(renames["CloudSqlConnectionProfileIn"]).optional(),
            "displayName": t.string().optional(),
            "provider": t.string().optional(),
            "postgresql": t.proxy(renames["PostgreSqlConnectionProfileIn"]).optional(),
        }
    ).named(renames["ConnectionProfileIn"])
    types["ConnectionProfileOut"] = t.struct(
        {
            "oracle": t.proxy(renames["OracleConnectionProfileOut"]).optional(),
            "state": t.string().optional(),
            "mysql": t.proxy(renames["MySqlConnectionProfileOut"]).optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "alloydb": t.proxy(renames["AlloyDbConnectionProfileOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "cloudsql": t.proxy(renames["CloudSqlConnectionProfileOut"]).optional(),
            "displayName": t.string().optional(),
            "updateTime": t.string().optional(),
            "provider": t.string().optional(),
            "postgresql": t.proxy(renames["PostgreSqlConnectionProfileOut"]).optional(),
        }
    ).named(renames["ConnectionProfileOut"])
    types["MigrationJobVerificationErrorIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["MigrationJobVerificationErrorIn"])
    types["MigrationJobVerificationErrorOut"] = t.struct(
        {
            "errorCode": t.string().optional(),
            "errorMessage": t.string().optional(),
            "errorDetailMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MigrationJobVerificationErrorOut"])
    types["StoredProcedureEntityIn"] = t.struct(
        {
            "sqlCode": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["StoredProcedureEntityIn"])
    types["StoredProcedureEntityOut"] = t.struct(
        {
            "sqlCode": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StoredProcedureEntityOut"])
    types["EntityMappingLogEntryIn"] = t.struct(
        {
            "ruleRevisionId": t.string().optional(),
            "ruleId": t.string().optional(),
            "mappingComment": t.string().optional(),
        }
    ).named(renames["EntityMappingLogEntryIn"])
    types["EntityMappingLogEntryOut"] = t.struct(
        {
            "ruleRevisionId": t.string().optional(),
            "ruleId": t.string().optional(),
            "mappingComment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityMappingLogEntryOut"])
    types["SqlAclEntryIn"] = t.struct(
        {
            "label": t.string().optional(),
            "value": t.string().optional(),
            "ttl": t.string().optional(),
            "expireTime": t.string().optional(),
        }
    ).named(renames["SqlAclEntryIn"])
    types["SqlAclEntryOut"] = t.struct(
        {
            "label": t.string().optional(),
            "value": t.string().optional(),
            "ttl": t.string().optional(),
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlAclEntryOut"])

    functions = {}
    functions["projectsLocationsList"] = datamigration.get(
        "v1/{name}:fetchStaticIps",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FetchStaticIpsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = datamigration.get(
        "v1/{name}:fetchStaticIps",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FetchStaticIpsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFetchStaticIps"] = datamigration.get(
        "v1/{name}:fetchStaticIps",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FetchStaticIpsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = datamigration.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = datamigration.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = datamigration.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = datamigration.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsSetIamPolicy"] = datamigration.get(
        "v1/{parent}/privateConnections",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPrivateConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsGetIamPolicy"] = datamigration.get(
        "v1/{parent}/privateConnections",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPrivateConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsPrivateConnectionsTestIamPermissions"
    ] = datamigration.get(
        "v1/{parent}/privateConnections",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPrivateConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsCreate"] = datamigration.get(
        "v1/{parent}/privateConnections",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPrivateConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsGet"] = datamigration.get(
        "v1/{parent}/privateConnections",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPrivateConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsDelete"] = datamigration.get(
        "v1/{parent}/privateConnections",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPrivateConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsList"] = datamigration.get(
        "v1/{parent}/privateConnections",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPrivateConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesSeed"] = datamigration.get(
        "v1/{conversionWorkspace}:describeConversionWorkspaceRevisions",
        t.struct(
            {
                "commitId": t.string().optional(),
                "conversionWorkspace": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DescribeConversionWorkspaceRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesList"] = datamigration.get(
        "v1/{conversionWorkspace}:describeConversionWorkspaceRevisions",
        t.struct(
            {
                "commitId": t.string().optional(),
                "conversionWorkspace": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DescribeConversionWorkspaceRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesCommit"] = datamigration.get(
        "v1/{conversionWorkspace}:describeConversionWorkspaceRevisions",
        t.struct(
            {
                "commitId": t.string().optional(),
                "conversionWorkspace": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DescribeConversionWorkspaceRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesApply"] = datamigration.get(
        "v1/{conversionWorkspace}:describeConversionWorkspaceRevisions",
        t.struct(
            {
                "commitId": t.string().optional(),
                "conversionWorkspace": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DescribeConversionWorkspaceRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesCreate"] = datamigration.get(
        "v1/{conversionWorkspace}:describeConversionWorkspaceRevisions",
        t.struct(
            {
                "commitId": t.string().optional(),
                "conversionWorkspace": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DescribeConversionWorkspaceRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesSetIamPolicy"] = datamigration.get(
        "v1/{conversionWorkspace}:describeConversionWorkspaceRevisions",
        t.struct(
            {
                "commitId": t.string().optional(),
                "conversionWorkspace": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DescribeConversionWorkspaceRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConversionWorkspacesSearchBackgroundJobs"
    ] = datamigration.get(
        "v1/{conversionWorkspace}:describeConversionWorkspaceRevisions",
        t.struct(
            {
                "commitId": t.string().optional(),
                "conversionWorkspace": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DescribeConversionWorkspaceRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesConvert"] = datamigration.get(
        "v1/{conversionWorkspace}:describeConversionWorkspaceRevisions",
        t.struct(
            {
                "commitId": t.string().optional(),
                "conversionWorkspace": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DescribeConversionWorkspaceRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesRollback"] = datamigration.get(
        "v1/{conversionWorkspace}:describeConversionWorkspaceRevisions",
        t.struct(
            {
                "commitId": t.string().optional(),
                "conversionWorkspace": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DescribeConversionWorkspaceRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConversionWorkspacesTestIamPermissions"
    ] = datamigration.get(
        "v1/{conversionWorkspace}:describeConversionWorkspaceRevisions",
        t.struct(
            {
                "commitId": t.string().optional(),
                "conversionWorkspace": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DescribeConversionWorkspaceRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesDelete"] = datamigration.get(
        "v1/{conversionWorkspace}:describeConversionWorkspaceRevisions",
        t.struct(
            {
                "commitId": t.string().optional(),
                "conversionWorkspace": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DescribeConversionWorkspaceRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesGet"] = datamigration.get(
        "v1/{conversionWorkspace}:describeConversionWorkspaceRevisions",
        t.struct(
            {
                "commitId": t.string().optional(),
                "conversionWorkspace": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DescribeConversionWorkspaceRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConversionWorkspacesDescribeDatabaseEntities"
    ] = datamigration.get(
        "v1/{conversionWorkspace}:describeConversionWorkspaceRevisions",
        t.struct(
            {
                "commitId": t.string().optional(),
                "conversionWorkspace": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DescribeConversionWorkspaceRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesPatch"] = datamigration.get(
        "v1/{conversionWorkspace}:describeConversionWorkspaceRevisions",
        t.struct(
            {
                "commitId": t.string().optional(),
                "conversionWorkspace": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DescribeConversionWorkspaceRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesGetIamPolicy"] = datamigration.get(
        "v1/{conversionWorkspace}:describeConversionWorkspaceRevisions",
        t.struct(
            {
                "commitId": t.string().optional(),
                "conversionWorkspace": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DescribeConversionWorkspaceRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConversionWorkspacesDescribeConversionWorkspaceRevisions"
    ] = datamigration.get(
        "v1/{conversionWorkspace}:describeConversionWorkspaceRevisions",
        t.struct(
            {
                "commitId": t.string().optional(),
                "conversionWorkspace": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DescribeConversionWorkspaceRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConversionWorkspacesMappingRulesImport"
    ] = datamigration.post(
        "v1/{parent}/mappingRules:import",
        t.struct(
            {
                "parent": t.string(),
                "rulesFormat": t.string().optional(),
                "autoCommit": t.boolean().optional(),
                "rulesFiles": t.array(t.proxy(renames["RulesFileIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsGetIamPolicy"] = datamigration.get(
        "v1/{parent}/migrationJobs",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMigrationJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsCreate"] = datamigration.get(
        "v1/{parent}/migrationJobs",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMigrationJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsGet"] = datamigration.get(
        "v1/{parent}/migrationJobs",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMigrationJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsStop"] = datamigration.get(
        "v1/{parent}/migrationJobs",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMigrationJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsDelete"] = datamigration.get(
        "v1/{parent}/migrationJobs",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMigrationJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsTestIamPermissions"] = datamigration.get(
        "v1/{parent}/migrationJobs",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMigrationJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsPatch"] = datamigration.get(
        "v1/{parent}/migrationJobs",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMigrationJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsVerify"] = datamigration.get(
        "v1/{parent}/migrationJobs",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMigrationJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsPromote"] = datamigration.get(
        "v1/{parent}/migrationJobs",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMigrationJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsResume"] = datamigration.get(
        "v1/{parent}/migrationJobs",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMigrationJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsGenerateSshScript"] = datamigration.get(
        "v1/{parent}/migrationJobs",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMigrationJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsSetIamPolicy"] = datamigration.get(
        "v1/{parent}/migrationJobs",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMigrationJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsRestart"] = datamigration.get(
        "v1/{parent}/migrationJobs",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMigrationJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsStart"] = datamigration.get(
        "v1/{parent}/migrationJobs",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMigrationJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsList"] = datamigration.get(
        "v1/{parent}/migrationJobs",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMigrationJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesCreate"] = datamigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConnectionProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesPatch"] = datamigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConnectionProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesList"] = datamigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConnectionProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConnectionProfilesTestIamPermissions"
    ] = datamigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConnectionProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesSetIamPolicy"] = datamigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConnectionProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesGetIamPolicy"] = datamigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConnectionProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesDelete"] = datamigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConnectionProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesGet"] = datamigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConnectionProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="datamigration",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
