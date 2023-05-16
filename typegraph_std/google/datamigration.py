from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_datamigration() -> Import:
    datamigration = HTTPRuntime("https://datamigration.googleapis.com/")

    renames = {
        "ErrorResponse": "_datamigration_1_ErrorResponse",
        "GoogleCloudClouddmsV1OperationMetadataIn": "_datamigration_2_GoogleCloudClouddmsV1OperationMetadataIn",
        "GoogleCloudClouddmsV1OperationMetadataOut": "_datamigration_3_GoogleCloudClouddmsV1OperationMetadataOut",
        "GenerateSshScriptRequestIn": "_datamigration_4_GenerateSshScriptRequestIn",
        "GenerateSshScriptRequestOut": "_datamigration_5_GenerateSshScriptRequestOut",
        "StopMigrationJobRequestIn": "_datamigration_6_StopMigrationJobRequestIn",
        "StopMigrationJobRequestOut": "_datamigration_7_StopMigrationJobRequestOut",
        "CloudSqlConnectionProfileIn": "_datamigration_8_CloudSqlConnectionProfileIn",
        "CloudSqlConnectionProfileOut": "_datamigration_9_CloudSqlConnectionProfileOut",
        "SqlIpConfigIn": "_datamigration_10_SqlIpConfigIn",
        "SqlIpConfigOut": "_datamigration_11_SqlIpConfigOut",
        "EncryptionConfigIn": "_datamigration_12_EncryptionConfigIn",
        "EncryptionConfigOut": "_datamigration_13_EncryptionConfigOut",
        "OperationIn": "_datamigration_14_OperationIn",
        "OperationOut": "_datamigration_15_OperationOut",
        "SslConfigIn": "_datamigration_16_SslConfigIn",
        "SslConfigOut": "_datamigration_17_SslConfigOut",
        "AlloyDbConnectionProfileIn": "_datamigration_18_AlloyDbConnectionProfileIn",
        "AlloyDbConnectionProfileOut": "_datamigration_19_AlloyDbConnectionProfileOut",
        "ResumeMigrationJobRequestIn": "_datamigration_20_ResumeMigrationJobRequestIn",
        "ResumeMigrationJobRequestOut": "_datamigration_21_ResumeMigrationJobRequestOut",
        "ConvertConversionWorkspaceRequestIn": "_datamigration_22_ConvertConversionWorkspaceRequestIn",
        "ConvertConversionWorkspaceRequestOut": "_datamigration_23_ConvertConversionWorkspaceRequestOut",
        "PrimaryInstanceSettingsIn": "_datamigration_24_PrimaryInstanceSettingsIn",
        "PrimaryInstanceSettingsOut": "_datamigration_25_PrimaryInstanceSettingsOut",
        "SetIamPolicyRequestIn": "_datamigration_26_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_datamigration_27_SetIamPolicyRequestOut",
        "PackageEntityIn": "_datamigration_28_PackageEntityIn",
        "PackageEntityOut": "_datamigration_29_PackageEntityOut",
        "ListMigrationJobsResponseIn": "_datamigration_30_ListMigrationJobsResponseIn",
        "ListMigrationJobsResponseOut": "_datamigration_31_ListMigrationJobsResponseOut",
        "ListConversionWorkspacesResponseIn": "_datamigration_32_ListConversionWorkspacesResponseIn",
        "ListConversionWorkspacesResponseOut": "_datamigration_33_ListConversionWorkspacesResponseOut",
        "TestIamPermissionsResponseIn": "_datamigration_34_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_datamigration_35_TestIamPermissionsResponseOut",
        "StoredProcedureEntityIn": "_datamigration_36_StoredProcedureEntityIn",
        "StoredProcedureEntityOut": "_datamigration_37_StoredProcedureEntityOut",
        "ConversionWorkspaceInfoIn": "_datamigration_38_ConversionWorkspaceInfoIn",
        "ConversionWorkspaceInfoOut": "_datamigration_39_ConversionWorkspaceInfoOut",
        "DatabaseEngineInfoIn": "_datamigration_40_DatabaseEngineInfoIn",
        "DatabaseEngineInfoOut": "_datamigration_41_DatabaseEngineInfoOut",
        "SynonymEntityIn": "_datamigration_42_SynonymEntityIn",
        "SynonymEntityOut": "_datamigration_43_SynonymEntityOut",
        "AuditConfigIn": "_datamigration_44_AuditConfigIn",
        "AuditConfigOut": "_datamigration_45_AuditConfigOut",
        "SchemaEntityIn": "_datamigration_46_SchemaEntityIn",
        "SchemaEntityOut": "_datamigration_47_SchemaEntityOut",
        "ForwardSshTunnelConnectivityIn": "_datamigration_48_ForwardSshTunnelConnectivityIn",
        "ForwardSshTunnelConnectivityOut": "_datamigration_49_ForwardSshTunnelConnectivityOut",
        "RestartMigrationJobRequestIn": "_datamigration_50_RestartMigrationJobRequestIn",
        "RestartMigrationJobRequestOut": "_datamigration_51_RestartMigrationJobRequestOut",
        "SeedConversionWorkspaceRequestIn": "_datamigration_52_SeedConversionWorkspaceRequestIn",
        "SeedConversionWorkspaceRequestOut": "_datamigration_53_SeedConversionWorkspaceRequestOut",
        "SqlAclEntryIn": "_datamigration_54_SqlAclEntryIn",
        "SqlAclEntryOut": "_datamigration_55_SqlAclEntryOut",
        "VerifyMigrationJobRequestIn": "_datamigration_56_VerifyMigrationJobRequestIn",
        "VerifyMigrationJobRequestOut": "_datamigration_57_VerifyMigrationJobRequestOut",
        "PostgreSqlConnectionProfileIn": "_datamigration_58_PostgreSqlConnectionProfileIn",
        "PostgreSqlConnectionProfileOut": "_datamigration_59_PostgreSqlConnectionProfileOut",
        "TestIamPermissionsRequestIn": "_datamigration_60_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_datamigration_61_TestIamPermissionsRequestOut",
        "BackgroundJobLogEntryIn": "_datamigration_62_BackgroundJobLogEntryIn",
        "BackgroundJobLogEntryOut": "_datamigration_63_BackgroundJobLogEntryOut",
        "ListLocationsResponseIn": "_datamigration_64_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_datamigration_65_ListLocationsResponseOut",
        "CloudSqlSettingsIn": "_datamigration_66_CloudSqlSettingsIn",
        "CloudSqlSettingsOut": "_datamigration_67_CloudSqlSettingsOut",
        "EntityMappingLogEntryIn": "_datamigration_68_EntityMappingLogEntryIn",
        "EntityMappingLogEntryOut": "_datamigration_69_EntityMappingLogEntryOut",
        "VpcPeeringConnectivityIn": "_datamigration_70_VpcPeeringConnectivityIn",
        "VpcPeeringConnectivityOut": "_datamigration_71_VpcPeeringConnectivityOut",
        "ApplyConversionWorkspaceRequestIn": "_datamigration_72_ApplyConversionWorkspaceRequestIn",
        "ApplyConversionWorkspaceRequestOut": "_datamigration_73_ApplyConversionWorkspaceRequestOut",
        "MySqlConnectionProfileIn": "_datamigration_74_MySqlConnectionProfileIn",
        "MySqlConnectionProfileOut": "_datamigration_75_MySqlConnectionProfileOut",
        "MachineConfigIn": "_datamigration_76_MachineConfigIn",
        "MachineConfigOut": "_datamigration_77_MachineConfigOut",
        "BindingIn": "_datamigration_78_BindingIn",
        "BindingOut": "_datamigration_79_BindingOut",
        "SequenceEntityIn": "_datamigration_80_SequenceEntityIn",
        "SequenceEntityOut": "_datamigration_81_SequenceEntityOut",
        "EntityMappingIn": "_datamigration_82_EntityMappingIn",
        "EntityMappingOut": "_datamigration_83_EntityMappingOut",
        "StaticIpConnectivityIn": "_datamigration_84_StaticIpConnectivityIn",
        "StaticIpConnectivityOut": "_datamigration_85_StaticIpConnectivityOut",
        "ConvertJobDetailsIn": "_datamigration_86_ConvertJobDetailsIn",
        "ConvertJobDetailsOut": "_datamigration_87_ConvertJobDetailsOut",
        "SeedJobDetailsIn": "_datamigration_88_SeedJobDetailsIn",
        "SeedJobDetailsOut": "_datamigration_89_SeedJobDetailsOut",
        "ImportMappingRulesRequestIn": "_datamigration_90_ImportMappingRulesRequestIn",
        "ImportMappingRulesRequestOut": "_datamigration_91_ImportMappingRulesRequestOut",
        "ExprIn": "_datamigration_92_ExprIn",
        "ExprOut": "_datamigration_93_ExprOut",
        "OracleConnectionProfileIn": "_datamigration_94_OracleConnectionProfileIn",
        "OracleConnectionProfileOut": "_datamigration_95_OracleConnectionProfileOut",
        "RulesFileIn": "_datamigration_96_RulesFileIn",
        "RulesFileOut": "_datamigration_97_RulesFileOut",
        "ApplyJobDetailsIn": "_datamigration_98_ApplyJobDetailsIn",
        "ApplyJobDetailsOut": "_datamigration_99_ApplyJobDetailsOut",
        "VmSelectionConfigIn": "_datamigration_100_VmSelectionConfigIn",
        "VmSelectionConfigOut": "_datamigration_101_VmSelectionConfigOut",
        "DescribeConversionWorkspaceRevisionsResponseIn": "_datamigration_102_DescribeConversionWorkspaceRevisionsResponseIn",
        "DescribeConversionWorkspaceRevisionsResponseOut": "_datamigration_103_DescribeConversionWorkspaceRevisionsResponseOut",
        "CancelOperationRequestIn": "_datamigration_104_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_datamigration_105_CancelOperationRequestOut",
        "PrivateConnectionIn": "_datamigration_106_PrivateConnectionIn",
        "PrivateConnectionOut": "_datamigration_107_PrivateConnectionOut",
        "SshScriptIn": "_datamigration_108_SshScriptIn",
        "SshScriptOut": "_datamigration_109_SshScriptOut",
        "RollbackConversionWorkspaceRequestIn": "_datamigration_110_RollbackConversionWorkspaceRequestIn",
        "RollbackConversionWorkspaceRequestOut": "_datamigration_111_RollbackConversionWorkspaceRequestOut",
        "FetchStaticIpsResponseIn": "_datamigration_112_FetchStaticIpsResponseIn",
        "FetchStaticIpsResponseOut": "_datamigration_113_FetchStaticIpsResponseOut",
        "VmCreationConfigIn": "_datamigration_114_VmCreationConfigIn",
        "VmCreationConfigOut": "_datamigration_115_VmCreationConfigOut",
        "PolicyIn": "_datamigration_116_PolicyIn",
        "PolicyOut": "_datamigration_117_PolicyOut",
        "SearchBackgroundJobsResponseIn": "_datamigration_118_SearchBackgroundJobsResponseIn",
        "SearchBackgroundJobsResponseOut": "_datamigration_119_SearchBackgroundJobsResponseOut",
        "StartMigrationJobRequestIn": "_datamigration_120_StartMigrationJobRequestIn",
        "StartMigrationJobRequestOut": "_datamigration_121_StartMigrationJobRequestOut",
        "ColumnEntityIn": "_datamigration_122_ColumnEntityIn",
        "ColumnEntityOut": "_datamigration_123_ColumnEntityOut",
        "DatabaseTypeIn": "_datamigration_124_DatabaseTypeIn",
        "DatabaseTypeOut": "_datamigration_125_DatabaseTypeOut",
        "AlloyDbSettingsIn": "_datamigration_126_AlloyDbSettingsIn",
        "AlloyDbSettingsOut": "_datamigration_127_AlloyDbSettingsOut",
        "DumpFlagIn": "_datamigration_128_DumpFlagIn",
        "DumpFlagOut": "_datamigration_129_DumpFlagOut",
        "AuditLogConfigIn": "_datamigration_130_AuditLogConfigIn",
        "AuditLogConfigOut": "_datamigration_131_AuditLogConfigOut",
        "ListOperationsResponseIn": "_datamigration_132_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_datamigration_133_ListOperationsResponseOut",
        "ReverseSshConnectivityIn": "_datamigration_134_ReverseSshConnectivityIn",
        "ReverseSshConnectivityOut": "_datamigration_135_ReverseSshConnectivityOut",
        "PromoteMigrationJobRequestIn": "_datamigration_136_PromoteMigrationJobRequestIn",
        "PromoteMigrationJobRequestOut": "_datamigration_137_PromoteMigrationJobRequestOut",
        "StaticServiceIpConnectivityIn": "_datamigration_138_StaticServiceIpConnectivityIn",
        "StaticServiceIpConnectivityOut": "_datamigration_139_StaticServiceIpConnectivityOut",
        "EmptyIn": "_datamigration_140_EmptyIn",
        "EmptyOut": "_datamigration_141_EmptyOut",
        "StatusIn": "_datamigration_142_StatusIn",
        "StatusOut": "_datamigration_143_StatusOut",
        "ImportRulesJobDetailsIn": "_datamigration_144_ImportRulesJobDetailsIn",
        "ImportRulesJobDetailsOut": "_datamigration_145_ImportRulesJobDetailsOut",
        "TriggerEntityIn": "_datamigration_146_TriggerEntityIn",
        "TriggerEntityOut": "_datamigration_147_TriggerEntityOut",
        "VpcPeeringConfigIn": "_datamigration_148_VpcPeeringConfigIn",
        "VpcPeeringConfigOut": "_datamigration_149_VpcPeeringConfigOut",
        "ListConnectionProfilesResponseIn": "_datamigration_150_ListConnectionProfilesResponseIn",
        "ListConnectionProfilesResponseOut": "_datamigration_151_ListConnectionProfilesResponseOut",
        "UserPasswordIn": "_datamigration_152_UserPasswordIn",
        "UserPasswordOut": "_datamigration_153_UserPasswordOut",
        "MigrationJobIn": "_datamigration_154_MigrationJobIn",
        "MigrationJobOut": "_datamigration_155_MigrationJobOut",
        "CommitConversionWorkspaceRequestIn": "_datamigration_156_CommitConversionWorkspaceRequestIn",
        "CommitConversionWorkspaceRequestOut": "_datamigration_157_CommitConversionWorkspaceRequestOut",
        "ListPrivateConnectionsResponseIn": "_datamigration_158_ListPrivateConnectionsResponseIn",
        "ListPrivateConnectionsResponseOut": "_datamigration_159_ListPrivateConnectionsResponseOut",
        "FunctionEntityIn": "_datamigration_160_FunctionEntityIn",
        "FunctionEntityOut": "_datamigration_161_FunctionEntityOut",
        "PrivateServiceConnectConnectivityIn": "_datamigration_162_PrivateServiceConnectConnectivityIn",
        "PrivateServiceConnectConnectivityOut": "_datamigration_163_PrivateServiceConnectConnectivityOut",
        "PrivateConnectivityIn": "_datamigration_164_PrivateConnectivityIn",
        "PrivateConnectivityOut": "_datamigration_165_PrivateConnectivityOut",
        "DatabaseEntityIn": "_datamigration_166_DatabaseEntityIn",
        "DatabaseEntityOut": "_datamigration_167_DatabaseEntityOut",
        "ConstraintEntityIn": "_datamigration_168_ConstraintEntityIn",
        "ConstraintEntityOut": "_datamigration_169_ConstraintEntityOut",
        "DescribeDatabaseEntitiesResponseIn": "_datamigration_170_DescribeDatabaseEntitiesResponseIn",
        "DescribeDatabaseEntitiesResponseOut": "_datamigration_171_DescribeDatabaseEntitiesResponseOut",
        "LocationIn": "_datamigration_172_LocationIn",
        "LocationOut": "_datamigration_173_LocationOut",
        "MigrationJobVerificationErrorIn": "_datamigration_174_MigrationJobVerificationErrorIn",
        "MigrationJobVerificationErrorOut": "_datamigration_175_MigrationJobVerificationErrorOut",
        "DumpFlagsIn": "_datamigration_176_DumpFlagsIn",
        "DumpFlagsOut": "_datamigration_177_DumpFlagsOut",
        "ViewEntityIn": "_datamigration_178_ViewEntityIn",
        "ViewEntityOut": "_datamigration_179_ViewEntityOut",
        "ConversionWorkspaceIn": "_datamigration_180_ConversionWorkspaceIn",
        "ConversionWorkspaceOut": "_datamigration_181_ConversionWorkspaceOut",
        "TableEntityIn": "_datamigration_182_TableEntityIn",
        "TableEntityOut": "_datamigration_183_TableEntityOut",
        "ConnectionProfileIn": "_datamigration_184_ConnectionProfileIn",
        "ConnectionProfileOut": "_datamigration_185_ConnectionProfileOut",
        "IndexEntityIn": "_datamigration_186_IndexEntityIn",
        "IndexEntityOut": "_datamigration_187_IndexEntityOut",
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
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "verb": t.string().optional(),
            "statusMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudClouddmsV1OperationMetadataOut"])
    types["GenerateSshScriptRequestIn"] = t.struct(
        {
            "vmPort": t.integer().optional(),
            "vmCreationConfig": t.proxy(renames["VmCreationConfigIn"]).optional(),
            "vmSelectionConfig": t.proxy(renames["VmSelectionConfigIn"]).optional(),
            "vm": t.string(),
        }
    ).named(renames["GenerateSshScriptRequestIn"])
    types["GenerateSshScriptRequestOut"] = t.struct(
        {
            "vmPort": t.integer().optional(),
            "vmCreationConfig": t.proxy(renames["VmCreationConfigOut"]).optional(),
            "vmSelectionConfig": t.proxy(renames["VmSelectionConfigOut"]).optional(),
            "vm": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateSshScriptRequestOut"])
    types["StopMigrationJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StopMigrationJobRequestIn"]
    )
    types["StopMigrationJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StopMigrationJobRequestOut"])
    types["CloudSqlConnectionProfileIn"] = t.struct(
        {"settings": t.proxy(renames["CloudSqlSettingsIn"]).optional()}
    ).named(renames["CloudSqlConnectionProfileIn"])
    types["CloudSqlConnectionProfileOut"] = t.struct(
        {
            "publicIp": t.string().optional(),
            "cloudSqlId": t.string().optional(),
            "additionalPublicIp": t.string().optional(),
            "settings": t.proxy(renames["CloudSqlSettingsOut"]).optional(),
            "privateIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudSqlConnectionProfileOut"])
    types["SqlIpConfigIn"] = t.struct(
        {
            "enableIpv4": t.boolean().optional(),
            "allocatedIpRange": t.string().optional(),
            "privateNetwork": t.string().optional(),
            "requireSsl": t.boolean().optional(),
            "authorizedNetworks": t.array(t.proxy(renames["SqlAclEntryIn"])).optional(),
        }
    ).named(renames["SqlIpConfigIn"])
    types["SqlIpConfigOut"] = t.struct(
        {
            "enableIpv4": t.boolean().optional(),
            "allocatedIpRange": t.string().optional(),
            "privateNetwork": t.string().optional(),
            "requireSsl": t.boolean().optional(),
            "authorizedNetworks": t.array(
                t.proxy(renames["SqlAclEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlIpConfigOut"])
    types["EncryptionConfigIn"] = t.struct({"kmsKeyName": t.string().optional()}).named(
        renames["EncryptionConfigIn"]
    )
    types["EncryptionConfigOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionConfigOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
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
    types["AlloyDbConnectionProfileIn"] = t.struct(
        {
            "clusterId": t.string(),
            "settings": t.proxy(renames["AlloyDbSettingsIn"]).optional(),
        }
    ).named(renames["AlloyDbConnectionProfileIn"])
    types["AlloyDbConnectionProfileOut"] = t.struct(
        {
            "clusterId": t.string(),
            "settings": t.proxy(renames["AlloyDbSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlloyDbConnectionProfileOut"])
    types["ResumeMigrationJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResumeMigrationJobRequestIn"]
    )
    types["ResumeMigrationJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumeMigrationJobRequestOut"])
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
    types["PrimaryInstanceSettingsIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "machineConfig": t.proxy(renames["MachineConfigIn"]).optional(),
            "databaseFlags": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string(),
        }
    ).named(renames["PrimaryInstanceSettingsIn"])
    types["PrimaryInstanceSettingsOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "machineConfig": t.proxy(renames["MachineConfigOut"]).optional(),
            "privateIp": t.string().optional(),
            "databaseFlags": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrimaryInstanceSettingsOut"])
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
    types["PackageEntityIn"] = t.struct(
        {
            "packageBody": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "packageSqlCode": t.string().optional(),
        }
    ).named(renames["PackageEntityIn"])
    types["PackageEntityOut"] = t.struct(
        {
            "packageBody": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "packageSqlCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageEntityOut"])
    types["ListMigrationJobsResponseIn"] = t.struct(
        {
            "migrationJobs": t.array(t.proxy(renames["MigrationJobIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListMigrationJobsResponseIn"])
    types["ListMigrationJobsResponseOut"] = t.struct(
        {
            "migrationJobs": t.array(t.proxy(renames["MigrationJobOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMigrationJobsResponseOut"])
    types["ListConversionWorkspacesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "conversionWorkspaces": t.array(
                t.proxy(renames["ConversionWorkspaceIn"])
            ).optional(),
        }
    ).named(renames["ListConversionWorkspacesResponseIn"])
    types["ListConversionWorkspacesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "conversionWorkspaces": t.array(
                t.proxy(renames["ConversionWorkspaceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConversionWorkspacesResponseOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["StoredProcedureEntityIn"] = t.struct(
        {
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "sqlCode": t.string().optional(),
        }
    ).named(renames["StoredProcedureEntityIn"])
    types["StoredProcedureEntityOut"] = t.struct(
        {
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "sqlCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StoredProcedureEntityOut"])
    types["ConversionWorkspaceInfoIn"] = t.struct(
        {"name": t.string().optional(), "commitId": t.string().optional()}
    ).named(renames["ConversionWorkspaceInfoIn"])
    types["ConversionWorkspaceInfoOut"] = t.struct(
        {
            "name": t.string().optional(),
            "commitId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConversionWorkspaceInfoOut"])
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
    types["SynonymEntityIn"] = t.struct(
        {
            "sourceEntity": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "sourceType": t.string().optional(),
        }
    ).named(renames["SynonymEntityIn"])
    types["SynonymEntityOut"] = t.struct(
        {
            "sourceEntity": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "sourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SynonymEntityOut"])
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
    types["SchemaEntityIn"] = t.struct(
        {"customFeatures": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["SchemaEntityIn"])
    types["SchemaEntityOut"] = t.struct(
        {
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaEntityOut"])
    types["ForwardSshTunnelConnectivityIn"] = t.struct(
        {
            "privateKey": t.string().optional(),
            "password": t.string().optional(),
            "port": t.integer().optional(),
            "hostname": t.string(),
            "username": t.string(),
        }
    ).named(renames["ForwardSshTunnelConnectivityIn"])
    types["ForwardSshTunnelConnectivityOut"] = t.struct(
        {
            "privateKey": t.string().optional(),
            "password": t.string().optional(),
            "port": t.integer().optional(),
            "hostname": t.string(),
            "username": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ForwardSshTunnelConnectivityOut"])
    types["RestartMigrationJobRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RestartMigrationJobRequestIn"])
    types["RestartMigrationJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RestartMigrationJobRequestOut"])
    types["SeedConversionWorkspaceRequestIn"] = t.struct(
        {
            "destinationConnectionProfile": t.string().optional(),
            "sourceConnectionProfile": t.string().optional(),
            "autoCommit": t.boolean().optional(),
        }
    ).named(renames["SeedConversionWorkspaceRequestIn"])
    types["SeedConversionWorkspaceRequestOut"] = t.struct(
        {
            "destinationConnectionProfile": t.string().optional(),
            "sourceConnectionProfile": t.string().optional(),
            "autoCommit": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SeedConversionWorkspaceRequestOut"])
    types["SqlAclEntryIn"] = t.struct(
        {
            "label": t.string().optional(),
            "ttl": t.string().optional(),
            "expireTime": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["SqlAclEntryIn"])
    types["SqlAclEntryOut"] = t.struct(
        {
            "label": t.string().optional(),
            "ttl": t.string().optional(),
            "expireTime": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlAclEntryOut"])
    types["VerifyMigrationJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VerifyMigrationJobRequestIn"]
    )
    types["VerifyMigrationJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VerifyMigrationJobRequestOut"])
    types["PostgreSqlConnectionProfileIn"] = t.struct(
        {
            "password": t.string(),
            "staticIpConnectivity": t.proxy(
                renames["StaticIpConnectivityIn"]
            ).optional(),
            "privateServiceConnectConnectivity": t.proxy(
                renames["PrivateServiceConnectConnectivityIn"]
            ).optional(),
            "host": t.string(),
            "port": t.integer(),
            "username": t.string(),
            "cloudSqlId": t.string().optional(),
            "ssl": t.proxy(renames["SslConfigIn"]).optional(),
        }
    ).named(renames["PostgreSqlConnectionProfileIn"])
    types["PostgreSqlConnectionProfileOut"] = t.struct(
        {
            "password": t.string(),
            "staticIpConnectivity": t.proxy(
                renames["StaticIpConnectivityOut"]
            ).optional(),
            "privateServiceConnectConnectivity": t.proxy(
                renames["PrivateServiceConnectConnectivityOut"]
            ).optional(),
            "host": t.string(),
            "port": t.integer(),
            "username": t.string(),
            "cloudSqlId": t.string().optional(),
            "ssl": t.proxy(renames["SslConfigOut"]).optional(),
            "passwordSet": t.boolean().optional(),
            "networkArchitecture": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostgreSqlConnectionProfileOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["BackgroundJobLogEntryIn"] = t.struct(
        {
            "requestAutocommit": t.boolean().optional(),
            "seedJobDetails": t.proxy(renames["SeedJobDetailsIn"]).optional(),
            "completionComment": t.string().optional(),
            "id": t.string().optional(),
            "finishTime": t.string().optional(),
            "convertJobDetails": t.proxy(renames["ConvertJobDetailsIn"]).optional(),
            "completionState": t.string().optional(),
            "applyJobDetails": t.proxy(renames["ApplyJobDetailsIn"]).optional(),
            "importRulesJobDetails": t.proxy(
                renames["ImportRulesJobDetailsIn"]
            ).optional(),
            "startTime": t.string().optional(),
            "jobType": t.string().optional(),
        }
    ).named(renames["BackgroundJobLogEntryIn"])
    types["BackgroundJobLogEntryOut"] = t.struct(
        {
            "requestAutocommit": t.boolean().optional(),
            "seedJobDetails": t.proxy(renames["SeedJobDetailsOut"]).optional(),
            "completionComment": t.string().optional(),
            "id": t.string().optional(),
            "finishTime": t.string().optional(),
            "convertJobDetails": t.proxy(renames["ConvertJobDetailsOut"]).optional(),
            "completionState": t.string().optional(),
            "applyJobDetails": t.proxy(renames["ApplyJobDetailsOut"]).optional(),
            "importRulesJobDetails": t.proxy(
                renames["ImportRulesJobDetailsOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "jobType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackgroundJobLogEntryOut"])
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
    types["CloudSqlSettingsIn"] = t.struct(
        {
            "autoStorageIncrease": t.boolean().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "dataDiskType": t.string().optional(),
            "sourceId": t.string().optional(),
            "activationPolicy": t.string().optional(),
            "secondaryZone": t.string().optional(),
            "rootPassword": t.string().optional(),
            "ipConfig": t.proxy(renames["SqlIpConfigIn"]).optional(),
            "availabilityType": t.string().optional(),
            "databaseVersion": t.string().optional(),
            "storageAutoResizeLimit": t.string().optional(),
            "collation": t.string().optional(),
            "cmekKeyName": t.string().optional(),
            "zone": t.string().optional(),
            "dataDiskSizeGb": t.string().optional(),
            "databaseFlags": t.struct({"_": t.string().optional()}).optional(),
            "tier": t.string().optional(),
        }
    ).named(renames["CloudSqlSettingsIn"])
    types["CloudSqlSettingsOut"] = t.struct(
        {
            "autoStorageIncrease": t.boolean().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "dataDiskType": t.string().optional(),
            "sourceId": t.string().optional(),
            "activationPolicy": t.string().optional(),
            "secondaryZone": t.string().optional(),
            "rootPassword": t.string().optional(),
            "ipConfig": t.proxy(renames["SqlIpConfigOut"]).optional(),
            "rootPasswordSet": t.boolean().optional(),
            "availabilityType": t.string().optional(),
            "databaseVersion": t.string().optional(),
            "storageAutoResizeLimit": t.string().optional(),
            "collation": t.string().optional(),
            "cmekKeyName": t.string().optional(),
            "zone": t.string().optional(),
            "dataDiskSizeGb": t.string().optional(),
            "databaseFlags": t.struct({"_": t.string().optional()}).optional(),
            "tier": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudSqlSettingsOut"])
    types["EntityMappingLogEntryIn"] = t.struct(
        {
            "ruleId": t.string().optional(),
            "ruleRevisionId": t.string().optional(),
            "mappingComment": t.string().optional(),
        }
    ).named(renames["EntityMappingLogEntryIn"])
    types["EntityMappingLogEntryOut"] = t.struct(
        {
            "ruleId": t.string().optional(),
            "ruleRevisionId": t.string().optional(),
            "mappingComment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityMappingLogEntryOut"])
    types["VpcPeeringConnectivityIn"] = t.struct({"vpc": t.string().optional()}).named(
        renames["VpcPeeringConnectivityIn"]
    )
    types["VpcPeeringConnectivityOut"] = t.struct(
        {
            "vpc": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VpcPeeringConnectivityOut"])
    types["ApplyConversionWorkspaceRequestIn"] = t.struct(
        {"filter": t.string().optional(), "connectionProfile": t.string().optional()}
    ).named(renames["ApplyConversionWorkspaceRequestIn"])
    types["ApplyConversionWorkspaceRequestOut"] = t.struct(
        {
            "filter": t.string().optional(),
            "connectionProfile": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplyConversionWorkspaceRequestOut"])
    types["MySqlConnectionProfileIn"] = t.struct(
        {
            "password": t.string(),
            "username": t.string(),
            "host": t.string(),
            "ssl": t.proxy(renames["SslConfigIn"]).optional(),
            "port": t.integer(),
            "cloudSqlId": t.string().optional(),
        }
    ).named(renames["MySqlConnectionProfileIn"])
    types["MySqlConnectionProfileOut"] = t.struct(
        {
            "passwordSet": t.boolean().optional(),
            "password": t.string(),
            "username": t.string(),
            "host": t.string(),
            "ssl": t.proxy(renames["SslConfigOut"]).optional(),
            "port": t.integer(),
            "cloudSqlId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MySqlConnectionProfileOut"])
    types["MachineConfigIn"] = t.struct({"cpuCount": t.integer().optional()}).named(
        renames["MachineConfigIn"]
    )
    types["MachineConfigOut"] = t.struct(
        {
            "cpuCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MachineConfigOut"])
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
    types["SequenceEntityIn"] = t.struct(
        {
            "startValue": t.string().optional(),
            "cycle": t.boolean().optional(),
            "cache": t.string().optional(),
            "increment": t.string().optional(),
            "minValue": t.string().optional(),
            "maxValue": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SequenceEntityIn"])
    types["SequenceEntityOut"] = t.struct(
        {
            "startValue": t.string().optional(),
            "cycle": t.boolean().optional(),
            "cache": t.string().optional(),
            "increment": t.string().optional(),
            "minValue": t.string().optional(),
            "maxValue": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SequenceEntityOut"])
    types["EntityMappingIn"] = t.struct(
        {
            "sourceEntity": t.string().optional(),
            "draftType": t.string().optional(),
            "draftEntity": t.string().optional(),
            "sourceType": t.string().optional(),
            "mappingLog": t.array(
                t.proxy(renames["EntityMappingLogEntryIn"])
            ).optional(),
        }
    ).named(renames["EntityMappingIn"])
    types["EntityMappingOut"] = t.struct(
        {
            "sourceEntity": t.string().optional(),
            "draftType": t.string().optional(),
            "draftEntity": t.string().optional(),
            "sourceType": t.string().optional(),
            "mappingLog": t.array(
                t.proxy(renames["EntityMappingLogEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityMappingOut"])
    types["StaticIpConnectivityIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StaticIpConnectivityIn"]
    )
    types["StaticIpConnectivityOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StaticIpConnectivityOut"])
    types["ConvertJobDetailsIn"] = t.struct({"filter": t.string().optional()}).named(
        renames["ConvertJobDetailsIn"]
    )
    types["ConvertJobDetailsOut"] = t.struct(
        {
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConvertJobDetailsOut"])
    types["SeedJobDetailsIn"] = t.struct(
        {"connectionProfile": t.string().optional()}
    ).named(renames["SeedJobDetailsIn"])
    types["SeedJobDetailsOut"] = t.struct(
        {
            "connectionProfile": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SeedJobDetailsOut"])
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
    types["OracleConnectionProfileIn"] = t.struct(
        {
            "password": t.string(),
            "host": t.string(),
            "forwardSshConnectivity": t.proxy(
                renames["ForwardSshTunnelConnectivityIn"]
            ).optional(),
            "databaseService": t.string(),
            "privateConnectivity": t.proxy(renames["PrivateConnectivityIn"]).optional(),
            "port": t.integer(),
            "staticServiceIpConnectivity": t.proxy(
                renames["StaticServiceIpConnectivityIn"]
            ).optional(),
            "username": t.string(),
        }
    ).named(renames["OracleConnectionProfileIn"])
    types["OracleConnectionProfileOut"] = t.struct(
        {
            "password": t.string(),
            "passwordSet": t.boolean().optional(),
            "host": t.string(),
            "forwardSshConnectivity": t.proxy(
                renames["ForwardSshTunnelConnectivityOut"]
            ).optional(),
            "databaseService": t.string(),
            "privateConnectivity": t.proxy(
                renames["PrivateConnectivityOut"]
            ).optional(),
            "port": t.integer(),
            "staticServiceIpConnectivity": t.proxy(
                renames["StaticServiceIpConnectivityOut"]
            ).optional(),
            "username": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OracleConnectionProfileOut"])
    types["RulesFileIn"] = t.struct(
        {
            "rulesSourceFilename": t.string().optional(),
            "rulesContent": t.string().optional(),
        }
    ).named(renames["RulesFileIn"])
    types["RulesFileOut"] = t.struct(
        {
            "rulesSourceFilename": t.string().optional(),
            "rulesContent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RulesFileOut"])
    types["ApplyJobDetailsIn"] = t.struct(
        {"connectionProfile": t.string().optional(), "filter": t.string().optional()}
    ).named(renames["ApplyJobDetailsIn"])
    types["ApplyJobDetailsOut"] = t.struct(
        {
            "connectionProfile": t.string().optional(),
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplyJobDetailsOut"])
    types["VmSelectionConfigIn"] = t.struct({"vmZone": t.string()}).named(
        renames["VmSelectionConfigIn"]
    )
    types["VmSelectionConfigOut"] = t.struct(
        {"vmZone": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VmSelectionConfigOut"])
    types["DescribeConversionWorkspaceRevisionsResponseIn"] = t.struct(
        {"revisions": t.array(t.proxy(renames["ConversionWorkspaceIn"])).optional()}
    ).named(renames["DescribeConversionWorkspaceRevisionsResponseIn"])
    types["DescribeConversionWorkspaceRevisionsResponseOut"] = t.struct(
        {
            "revisions": t.array(t.proxy(renames["ConversionWorkspaceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DescribeConversionWorkspaceRevisionsResponseOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["PrivateConnectionIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "vpcPeeringConfig": t.proxy(renames["VpcPeeringConfigIn"]).optional(),
        }
    ).named(renames["PrivateConnectionIn"])
    types["PrivateConnectionOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "vpcPeeringConfig": t.proxy(renames["VpcPeeringConfigOut"]).optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["PrivateConnectionOut"])
    types["SshScriptIn"] = t.struct({"script": t.string().optional()}).named(
        renames["SshScriptIn"]
    )
    types["SshScriptOut"] = t.struct(
        {
            "script": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SshScriptOut"])
    types["RollbackConversionWorkspaceRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RollbackConversionWorkspaceRequestIn"])
    types["RollbackConversionWorkspaceRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RollbackConversionWorkspaceRequestOut"])
    types["FetchStaticIpsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "staticIps": t.array(t.string()).optional(),
        }
    ).named(renames["FetchStaticIpsResponseIn"])
    types["FetchStaticIpsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "staticIps": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchStaticIpsResponseOut"])
    types["VmCreationConfigIn"] = t.struct(
        {
            "vmZone": t.string().optional(),
            "subnet": t.string().optional(),
            "vmMachineType": t.string(),
        }
    ).named(renames["VmCreationConfigIn"])
    types["VmCreationConfigOut"] = t.struct(
        {
            "vmZone": t.string().optional(),
            "subnet": t.string().optional(),
            "vmMachineType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmCreationConfigOut"])
    types["PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["SearchBackgroundJobsResponseIn"] = t.struct(
        {"jobs": t.array(t.proxy(renames["BackgroundJobLogEntryIn"])).optional()}
    ).named(renames["SearchBackgroundJobsResponseIn"])
    types["SearchBackgroundJobsResponseOut"] = t.struct(
        {
            "jobs": t.array(t.proxy(renames["BackgroundJobLogEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchBackgroundJobsResponseOut"])
    types["StartMigrationJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StartMigrationJobRequestIn"]
    )
    types["StartMigrationJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StartMigrationJobRequestOut"])
    types["ColumnEntityIn"] = t.struct(
        {
            "comment": t.string().optional(),
            "name": t.string().optional(),
            "setValues": t.array(t.string()).optional(),
            "collation": t.string().optional(),
            "charset": t.string().optional(),
            "udt": t.boolean().optional(),
            "dataType": t.string().optional(),
            "autoGenerated": t.boolean().optional(),
            "defaultValue": t.string().optional(),
            "precision": t.integer().optional(),
            "nullable": t.boolean().optional(),
            "scale": t.integer().optional(),
            "arrayLength": t.integer().optional(),
            "ordinalPosition": t.integer().optional(),
            "array": t.boolean().optional(),
            "fractionalSecondsPrecision": t.integer().optional(),
            "length": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ColumnEntityIn"])
    types["ColumnEntityOut"] = t.struct(
        {
            "comment": t.string().optional(),
            "name": t.string().optional(),
            "setValues": t.array(t.string()).optional(),
            "collation": t.string().optional(),
            "charset": t.string().optional(),
            "udt": t.boolean().optional(),
            "dataType": t.string().optional(),
            "autoGenerated": t.boolean().optional(),
            "defaultValue": t.string().optional(),
            "precision": t.integer().optional(),
            "nullable": t.boolean().optional(),
            "scale": t.integer().optional(),
            "arrayLength": t.integer().optional(),
            "ordinalPosition": t.integer().optional(),
            "array": t.boolean().optional(),
            "fractionalSecondsPrecision": t.integer().optional(),
            "length": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColumnEntityOut"])
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
    types["AlloyDbSettingsIn"] = t.struct(
        {
            "initialUser": t.proxy(renames["UserPasswordIn"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "primaryInstanceSettings": t.proxy(renames["PrimaryInstanceSettingsIn"]),
            "encryptionConfig": t.proxy(renames["EncryptionConfigIn"]).optional(),
            "vpcNetwork": t.string(),
        }
    ).named(renames["AlloyDbSettingsIn"])
    types["AlloyDbSettingsOut"] = t.struct(
        {
            "initialUser": t.proxy(renames["UserPasswordOut"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "primaryInstanceSettings": t.proxy(renames["PrimaryInstanceSettingsOut"]),
            "encryptionConfig": t.proxy(renames["EncryptionConfigOut"]).optional(),
            "vpcNetwork": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlloyDbSettingsOut"])
    types["DumpFlagIn"] = t.struct(
        {"name": t.string().optional(), "value": t.string().optional()}
    ).named(renames["DumpFlagIn"])
    types["DumpFlagOut"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DumpFlagOut"])
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
    types["ReverseSshConnectivityIn"] = t.struct(
        {
            "vmPort": t.integer(),
            "vmIp": t.string(),
            "vm": t.string().optional(),
            "vpc": t.string().optional(),
        }
    ).named(renames["ReverseSshConnectivityIn"])
    types["ReverseSshConnectivityOut"] = t.struct(
        {
            "vmPort": t.integer(),
            "vmIp": t.string(),
            "vm": t.string().optional(),
            "vpc": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReverseSshConnectivityOut"])
    types["PromoteMigrationJobRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["PromoteMigrationJobRequestIn"])
    types["PromoteMigrationJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PromoteMigrationJobRequestOut"])
    types["StaticServiceIpConnectivityIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["StaticServiceIpConnectivityIn"])
    types["StaticServiceIpConnectivityOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StaticServiceIpConnectivityOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["TriggerEntityIn"] = t.struct(
        {
            "triggeringEvents": t.array(t.string()).optional(),
            "triggerType": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "sqlCode": t.string().optional(),
        }
    ).named(renames["TriggerEntityIn"])
    types["TriggerEntityOut"] = t.struct(
        {
            "triggeringEvents": t.array(t.string()).optional(),
            "triggerType": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "sqlCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TriggerEntityOut"])
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
    types["ListConnectionProfilesResponseIn"] = t.struct(
        {
            "connectionProfiles": t.array(
                t.proxy(renames["ConnectionProfileIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListConnectionProfilesResponseIn"])
    types["ListConnectionProfilesResponseOut"] = t.struct(
        {
            "connectionProfiles": t.array(
                t.proxy(renames["ConnectionProfileOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConnectionProfilesResponseOut"])
    types["UserPasswordIn"] = t.struct(
        {"user": t.string().optional(), "password": t.string().optional()}
    ).named(renames["UserPasswordIn"])
    types["UserPasswordOut"] = t.struct(
        {
            "user": t.string().optional(),
            "passwordSet": t.boolean().optional(),
            "password": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserPasswordOut"])
    types["MigrationJobIn"] = t.struct(
        {
            "type": t.string(),
            "name": t.string().optional(),
            "destinationDatabase": t.proxy(renames["DatabaseTypeIn"]).optional(),
            "conversionWorkspace": t.proxy(
                renames["ConversionWorkspaceInfoIn"]
            ).optional(),
            "sourceDatabase": t.proxy(renames["DatabaseTypeIn"]).optional(),
            "reverseSshConnectivity": t.proxy(
                renames["ReverseSshConnectivityIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "vpcPeeringConnectivity": t.proxy(
                renames["VpcPeeringConnectivityIn"]
            ).optional(),
            "cmekKeyName": t.string().optional(),
            "source": t.string(),
            "filter": t.string().optional(),
            "state": t.string().optional(),
            "staticIpConnectivity": t.proxy(
                renames["StaticIpConnectivityIn"]
            ).optional(),
            "dumpPath": t.string().optional(),
            "destination": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "dumpFlags": t.proxy(renames["DumpFlagsIn"]).optional(),
        }
    ).named(renames["MigrationJobIn"])
    types["MigrationJobOut"] = t.struct(
        {
            "type": t.string(),
            "name": t.string().optional(),
            "endTime": t.string().optional(),
            "destinationDatabase": t.proxy(renames["DatabaseTypeOut"]).optional(),
            "conversionWorkspace": t.proxy(
                renames["ConversionWorkspaceInfoOut"]
            ).optional(),
            "sourceDatabase": t.proxy(renames["DatabaseTypeOut"]).optional(),
            "reverseSshConnectivity": t.proxy(
                renames["ReverseSshConnectivityOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "displayName": t.string().optional(),
            "vpcPeeringConnectivity": t.proxy(
                renames["VpcPeeringConnectivityOut"]
            ).optional(),
            "cmekKeyName": t.string().optional(),
            "source": t.string(),
            "filter": t.string().optional(),
            "duration": t.string().optional(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "staticIpConnectivity": t.proxy(
                renames["StaticIpConnectivityOut"]
            ).optional(),
            "phase": t.string().optional(),
            "dumpPath": t.string().optional(),
            "destination": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "dumpFlags": t.proxy(renames["DumpFlagsOut"]).optional(),
        }
    ).named(renames["MigrationJobOut"])
    types["CommitConversionWorkspaceRequestIn"] = t.struct(
        {"commitName": t.string().optional()}
    ).named(renames["CommitConversionWorkspaceRequestIn"])
    types["CommitConversionWorkspaceRequestOut"] = t.struct(
        {
            "commitName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitConversionWorkspaceRequestOut"])
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
    types["FunctionEntityIn"] = t.struct(
        {
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "sqlCode": t.string().optional(),
        }
    ).named(renames["FunctionEntityIn"])
    types["FunctionEntityOut"] = t.struct(
        {
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "sqlCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FunctionEntityOut"])
    types["PrivateServiceConnectConnectivityIn"] = t.struct(
        {"serviceAttachment": t.string()}
    ).named(renames["PrivateServiceConnectConnectivityIn"])
    types["PrivateServiceConnectConnectivityOut"] = t.struct(
        {
            "serviceAttachment": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateServiceConnectConnectivityOut"])
    types["PrivateConnectivityIn"] = t.struct({"privateConnection": t.string()}).named(
        renames["PrivateConnectivityIn"]
    )
    types["PrivateConnectivityOut"] = t.struct(
        {
            "privateConnection": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateConnectivityOut"])
    types["DatabaseEntityIn"] = t.struct(
        {
            "shortName": t.string().optional(),
            "entityType": t.string().optional(),
            "synonym": t.proxy(renames["SynonymEntityIn"]).optional(),
            "view": t.proxy(renames["ViewEntityIn"]).optional(),
            "databaseFunction": t.proxy(renames["FunctionEntityIn"]).optional(),
            "databasePackage": t.proxy(renames["PackageEntityIn"]).optional(),
            "tree": t.string().optional(),
            "schema": t.proxy(renames["SchemaEntityIn"]).optional(),
            "mappings": t.array(t.proxy(renames["EntityMappingIn"])).optional(),
            "sequence": t.proxy(renames["SequenceEntityIn"]).optional(),
            "storedProcedure": t.proxy(renames["StoredProcedureEntityIn"]).optional(),
            "table": t.proxy(renames["TableEntityIn"]).optional(),
            "parentEntity": t.string().optional(),
        }
    ).named(renames["DatabaseEntityIn"])
    types["DatabaseEntityOut"] = t.struct(
        {
            "shortName": t.string().optional(),
            "entityType": t.string().optional(),
            "synonym": t.proxy(renames["SynonymEntityOut"]).optional(),
            "view": t.proxy(renames["ViewEntityOut"]).optional(),
            "databaseFunction": t.proxy(renames["FunctionEntityOut"]).optional(),
            "databasePackage": t.proxy(renames["PackageEntityOut"]).optional(),
            "tree": t.string().optional(),
            "schema": t.proxy(renames["SchemaEntityOut"]).optional(),
            "mappings": t.array(t.proxy(renames["EntityMappingOut"])).optional(),
            "sequence": t.proxy(renames["SequenceEntityOut"]).optional(),
            "storedProcedure": t.proxy(renames["StoredProcedureEntityOut"]).optional(),
            "table": t.proxy(renames["TableEntityOut"]).optional(),
            "parentEntity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseEntityOut"])
    types["ConstraintEntityIn"] = t.struct(
        {
            "name": t.string().optional(),
            "tableName": t.string().optional(),
            "referenceTable": t.string().optional(),
            "type": t.string().optional(),
            "tableColumns": t.array(t.string()).optional(),
            "referenceColumns": t.array(t.string()).optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ConstraintEntityIn"])
    types["ConstraintEntityOut"] = t.struct(
        {
            "name": t.string().optional(),
            "tableName": t.string().optional(),
            "referenceTable": t.string().optional(),
            "type": t.string().optional(),
            "tableColumns": t.array(t.string()).optional(),
            "referenceColumns": t.array(t.string()).optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConstraintEntityOut"])
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
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["MigrationJobVerificationErrorIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["MigrationJobVerificationErrorIn"])
    types["MigrationJobVerificationErrorOut"] = t.struct(
        {
            "errorDetailMessage": t.string().optional(),
            "errorCode": t.string().optional(),
            "errorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MigrationJobVerificationErrorOut"])
    types["DumpFlagsIn"] = t.struct(
        {"dumpFlags": t.array(t.proxy(renames["DumpFlagIn"])).optional()}
    ).named(renames["DumpFlagsIn"])
    types["DumpFlagsOut"] = t.struct(
        {
            "dumpFlags": t.array(t.proxy(renames["DumpFlagOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DumpFlagsOut"])
    types["ViewEntityIn"] = t.struct(
        {
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "sqlCode": t.string().optional(),
            "constraints": t.array(t.proxy(renames["ConstraintEntityIn"])).optional(),
        }
    ).named(renames["ViewEntityIn"])
    types["ViewEntityOut"] = t.struct(
        {
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "sqlCode": t.string().optional(),
            "constraints": t.array(t.proxy(renames["ConstraintEntityOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViewEntityOut"])
    types["ConversionWorkspaceIn"] = t.struct(
        {
            "destination": t.proxy(renames["DatabaseEngineInfoIn"]),
            "displayName": t.string().optional(),
            "source": t.proxy(renames["DatabaseEngineInfoIn"]),
            "name": t.string().optional(),
            "globalSettings": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ConversionWorkspaceIn"])
    types["ConversionWorkspaceOut"] = t.struct(
        {
            "destination": t.proxy(renames["DatabaseEngineInfoOut"]),
            "latestCommitTime": t.string().optional(),
            "latestCommitId": t.string().optional(),
            "displayName": t.string().optional(),
            "updateTime": t.string().optional(),
            "source": t.proxy(renames["DatabaseEngineInfoOut"]),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "hasUncommittedChanges": t.boolean().optional(),
            "globalSettings": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConversionWorkspaceOut"])
    types["TableEntityIn"] = t.struct(
        {
            "comment": t.string().optional(),
            "indices": t.array(t.proxy(renames["IndexEntityIn"])).optional(),
            "triggers": t.array(t.proxy(renames["TriggerEntityIn"])).optional(),
            "columns": t.array(t.proxy(renames["ColumnEntityIn"])).optional(),
            "constraints": t.array(t.proxy(renames["ConstraintEntityIn"])).optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["TableEntityIn"])
    types["TableEntityOut"] = t.struct(
        {
            "comment": t.string().optional(),
            "indices": t.array(t.proxy(renames["IndexEntityOut"])).optional(),
            "triggers": t.array(t.proxy(renames["TriggerEntityOut"])).optional(),
            "columns": t.array(t.proxy(renames["ColumnEntityOut"])).optional(),
            "constraints": t.array(t.proxy(renames["ConstraintEntityOut"])).optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableEntityOut"])
    types["ConnectionProfileIn"] = t.struct(
        {
            "mysql": t.proxy(renames["MySqlConnectionProfileIn"]).optional(),
            "name": t.string().optional(),
            "cloudsql": t.proxy(renames["CloudSqlConnectionProfileIn"]).optional(),
            "state": t.string().optional(),
            "provider": t.string().optional(),
            "displayName": t.string().optional(),
            "oracle": t.proxy(renames["OracleConnectionProfileIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "postgresql": t.proxy(renames["PostgreSqlConnectionProfileIn"]).optional(),
            "alloydb": t.proxy(renames["AlloyDbConnectionProfileIn"]).optional(),
        }
    ).named(renames["ConnectionProfileIn"])
    types["ConnectionProfileOut"] = t.struct(
        {
            "mysql": t.proxy(renames["MySqlConnectionProfileOut"]).optional(),
            "name": t.string().optional(),
            "cloudsql": t.proxy(renames["CloudSqlConnectionProfileOut"]).optional(),
            "state": t.string().optional(),
            "provider": t.string().optional(),
            "displayName": t.string().optional(),
            "oracle": t.proxy(renames["OracleConnectionProfileOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "postgresql": t.proxy(renames["PostgreSqlConnectionProfileOut"]).optional(),
            "alloydb": t.proxy(renames["AlloyDbConnectionProfileOut"]).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["ConnectionProfileOut"])
    types["IndexEntityIn"] = t.struct(
        {
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
            "unique": t.boolean().optional(),
            "tableColumns": t.array(t.string()).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["IndexEntityIn"])
    types["IndexEntityOut"] = t.struct(
        {
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
            "unique": t.boolean().optional(),
            "tableColumns": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexEntityOut"])

    functions = {}
    functions["projectsLocationsList"] = datamigration.get(
        "v1/{name}:fetchStaticIps",
        t.struct(
            {
                "name": t.string(),
                "pageSize": t.integer().optional(),
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
                "name": t.string(),
                "pageSize": t.integer().optional(),
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
                "name": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FetchStaticIpsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsDelete"] = datamigration.post(
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
    functions["projectsLocationsPrivateConnectionsCreate"] = datamigration.post(
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
    functions["projectsLocationsPrivateConnectionsList"] = datamigration.post(
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
    functions["projectsLocationsPrivateConnectionsGetIamPolicy"] = datamigration.post(
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
    functions["projectsLocationsPrivateConnectionsSetIamPolicy"] = datamigration.post(
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
    functions["projectsLocationsPrivateConnectionsGet"] = datamigration.post(
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
    functions[
        "projectsLocationsPrivateConnectionsTestIamPermissions"
    ] = datamigration.post(
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
    functions["projectsLocationsMigrationJobsPatch"] = datamigration.post(
        "v1/{name}:stop",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsDelete"] = datamigration.post(
        "v1/{name}:stop",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsGetIamPolicy"] = datamigration.post(
        "v1/{name}:stop",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsList"] = datamigration.post(
        "v1/{name}:stop",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsGet"] = datamigration.post(
        "v1/{name}:stop",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsRestart"] = datamigration.post(
        "v1/{name}:stop",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsSetIamPolicy"] = datamigration.post(
        "v1/{name}:stop",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsGenerateSshScript"] = datamigration.post(
        "v1/{name}:stop",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsPromote"] = datamigration.post(
        "v1/{name}:stop",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsTestIamPermissions"] = datamigration.post(
        "v1/{name}:stop",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsResume"] = datamigration.post(
        "v1/{name}:stop",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsVerify"] = datamigration.post(
        "v1/{name}:stop",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsCreate"] = datamigration.post(
        "v1/{name}:stop",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsStart"] = datamigration.post(
        "v1/{name}:stop",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsStop"] = datamigration.post(
        "v1/{name}:stop",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesGet"] = datamigration.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "force": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesGetIamPolicy"] = datamigration.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "force": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesList"] = datamigration.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "force": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesCreate"] = datamigration.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "force": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesPatch"] = datamigration.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "force": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConnectionProfilesTestIamPermissions"
    ] = datamigration.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "force": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesSetIamPolicy"] = datamigration.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "force": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesDelete"] = datamigration.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "force": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = datamigration.get(
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
    functions["projectsLocationsOperationsCancel"] = datamigration.get(
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
    functions["projectsLocationsOperationsGet"] = datamigration.get(
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
    functions["projectsLocationsOperationsList"] = datamigration.get(
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
    functions["projectsLocationsConversionWorkspacesRollback"] = datamigration.get(
        "v1/{parent}/conversionWorkspaces",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListConversionWorkspacesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesGetIamPolicy"] = datamigration.get(
        "v1/{parent}/conversionWorkspaces",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListConversionWorkspacesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesConvert"] = datamigration.get(
        "v1/{parent}/conversionWorkspaces",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListConversionWorkspacesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConversionWorkspacesSearchBackgroundJobs"
    ] = datamigration.get(
        "v1/{parent}/conversionWorkspaces",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListConversionWorkspacesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesCreate"] = datamigration.get(
        "v1/{parent}/conversionWorkspaces",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListConversionWorkspacesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesPatch"] = datamigration.get(
        "v1/{parent}/conversionWorkspaces",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListConversionWorkspacesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesCommit"] = datamigration.get(
        "v1/{parent}/conversionWorkspaces",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListConversionWorkspacesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConversionWorkspacesDescribeConversionWorkspaceRevisions"
    ] = datamigration.get(
        "v1/{parent}/conversionWorkspaces",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListConversionWorkspacesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesGet"] = datamigration.get(
        "v1/{parent}/conversionWorkspaces",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListConversionWorkspacesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesApply"] = datamigration.get(
        "v1/{parent}/conversionWorkspaces",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListConversionWorkspacesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesDelete"] = datamigration.get(
        "v1/{parent}/conversionWorkspaces",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListConversionWorkspacesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesSeed"] = datamigration.get(
        "v1/{parent}/conversionWorkspaces",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListConversionWorkspacesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConversionWorkspacesDescribeDatabaseEntities"
    ] = datamigration.get(
        "v1/{parent}/conversionWorkspaces",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListConversionWorkspacesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesSetIamPolicy"] = datamigration.get(
        "v1/{parent}/conversionWorkspaces",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListConversionWorkspacesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConversionWorkspacesTestIamPermissions"
    ] = datamigration.get(
        "v1/{parent}/conversionWorkspaces",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListConversionWorkspacesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesList"] = datamigration.get(
        "v1/{parent}/conversionWorkspaces",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListConversionWorkspacesResponseOut"]),
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

    return Import(
        importer="datamigration",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
