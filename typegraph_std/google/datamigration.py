from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_datamigration() -> Import:
    datamigration = HTTPRuntime("https://datamigration.googleapis.com/")

    renames = {
        "ErrorResponse": "_datamigration_1_ErrorResponse",
        "AlloyDbSettingsIn": "_datamigration_2_AlloyDbSettingsIn",
        "AlloyDbSettingsOut": "_datamigration_3_AlloyDbSettingsOut",
        "ColumnEntityIn": "_datamigration_4_ColumnEntityIn",
        "ColumnEntityOut": "_datamigration_5_ColumnEntityOut",
        "StartMigrationJobRequestIn": "_datamigration_6_StartMigrationJobRequestIn",
        "StartMigrationJobRequestOut": "_datamigration_7_StartMigrationJobRequestOut",
        "ListConnectionProfilesResponseIn": "_datamigration_8_ListConnectionProfilesResponseIn",
        "ListConnectionProfilesResponseOut": "_datamigration_9_ListConnectionProfilesResponseOut",
        "SqlIpConfigIn": "_datamigration_10_SqlIpConfigIn",
        "SqlIpConfigOut": "_datamigration_11_SqlIpConfigOut",
        "ForwardSshTunnelConnectivityIn": "_datamigration_12_ForwardSshTunnelConnectivityIn",
        "ForwardSshTunnelConnectivityOut": "_datamigration_13_ForwardSshTunnelConnectivityOut",
        "SchemaEntityIn": "_datamigration_14_SchemaEntityIn",
        "SchemaEntityOut": "_datamigration_15_SchemaEntityOut",
        "VmSelectionConfigIn": "_datamigration_16_VmSelectionConfigIn",
        "VmSelectionConfigOut": "_datamigration_17_VmSelectionConfigOut",
        "GenerateSshScriptRequestIn": "_datamigration_18_GenerateSshScriptRequestIn",
        "GenerateSshScriptRequestOut": "_datamigration_19_GenerateSshScriptRequestOut",
        "ListMigrationJobsResponseIn": "_datamigration_20_ListMigrationJobsResponseIn",
        "ListMigrationJobsResponseOut": "_datamigration_21_ListMigrationJobsResponseOut",
        "OperationIn": "_datamigration_22_OperationIn",
        "OperationOut": "_datamigration_23_OperationOut",
        "PrimaryInstanceSettingsIn": "_datamigration_24_PrimaryInstanceSettingsIn",
        "PrimaryInstanceSettingsOut": "_datamigration_25_PrimaryInstanceSettingsOut",
        "ConvertJobDetailsIn": "_datamigration_26_ConvertJobDetailsIn",
        "ConvertJobDetailsOut": "_datamigration_27_ConvertJobDetailsOut",
        "GoogleCloudClouddmsV1OperationMetadataIn": "_datamigration_28_GoogleCloudClouddmsV1OperationMetadataIn",
        "GoogleCloudClouddmsV1OperationMetadataOut": "_datamigration_29_GoogleCloudClouddmsV1OperationMetadataOut",
        "SshScriptIn": "_datamigration_30_SshScriptIn",
        "SshScriptOut": "_datamigration_31_SshScriptOut",
        "VpcPeeringConnectivityIn": "_datamigration_32_VpcPeeringConnectivityIn",
        "VpcPeeringConnectivityOut": "_datamigration_33_VpcPeeringConnectivityOut",
        "MigrationJobIn": "_datamigration_34_MigrationJobIn",
        "MigrationJobOut": "_datamigration_35_MigrationJobOut",
        "StaticIpConnectivityIn": "_datamigration_36_StaticIpConnectivityIn",
        "StaticIpConnectivityOut": "_datamigration_37_StaticIpConnectivityOut",
        "MachineConfigIn": "_datamigration_38_MachineConfigIn",
        "MachineConfigOut": "_datamigration_39_MachineConfigOut",
        "TableEntityIn": "_datamigration_40_TableEntityIn",
        "TableEntityOut": "_datamigration_41_TableEntityOut",
        "PostgreSqlConnectionProfileIn": "_datamigration_42_PostgreSqlConnectionProfileIn",
        "PostgreSqlConnectionProfileOut": "_datamigration_43_PostgreSqlConnectionProfileOut",
        "ListOperationsResponseIn": "_datamigration_44_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_datamigration_45_ListOperationsResponseOut",
        "StoredProcedureEntityIn": "_datamigration_46_StoredProcedureEntityIn",
        "StoredProcedureEntityOut": "_datamigration_47_StoredProcedureEntityOut",
        "ConvertConversionWorkspaceRequestIn": "_datamigration_48_ConvertConversionWorkspaceRequestIn",
        "ConvertConversionWorkspaceRequestOut": "_datamigration_49_ConvertConversionWorkspaceRequestOut",
        "VmCreationConfigIn": "_datamigration_50_VmCreationConfigIn",
        "VmCreationConfigOut": "_datamigration_51_VmCreationConfigOut",
        "FunctionEntityIn": "_datamigration_52_FunctionEntityIn",
        "FunctionEntityOut": "_datamigration_53_FunctionEntityOut",
        "SearchBackgroundJobsResponseIn": "_datamigration_54_SearchBackgroundJobsResponseIn",
        "SearchBackgroundJobsResponseOut": "_datamigration_55_SearchBackgroundJobsResponseOut",
        "SynonymEntityIn": "_datamigration_56_SynonymEntityIn",
        "SynonymEntityOut": "_datamigration_57_SynonymEntityOut",
        "AlloyDbConnectionProfileIn": "_datamigration_58_AlloyDbConnectionProfileIn",
        "AlloyDbConnectionProfileOut": "_datamigration_59_AlloyDbConnectionProfileOut",
        "DescribeDatabaseEntitiesResponseIn": "_datamigration_60_DescribeDatabaseEntitiesResponseIn",
        "DescribeDatabaseEntitiesResponseOut": "_datamigration_61_DescribeDatabaseEntitiesResponseOut",
        "PrivateServiceConnectConnectivityIn": "_datamigration_62_PrivateServiceConnectConnectivityIn",
        "PrivateServiceConnectConnectivityOut": "_datamigration_63_PrivateServiceConnectConnectivityOut",
        "MigrationJobVerificationErrorIn": "_datamigration_64_MigrationJobVerificationErrorIn",
        "MigrationJobVerificationErrorOut": "_datamigration_65_MigrationJobVerificationErrorOut",
        "ListConversionWorkspacesResponseIn": "_datamigration_66_ListConversionWorkspacesResponseIn",
        "ListConversionWorkspacesResponseOut": "_datamigration_67_ListConversionWorkspacesResponseOut",
        "AuditConfigIn": "_datamigration_68_AuditConfigIn",
        "AuditConfigOut": "_datamigration_69_AuditConfigOut",
        "ApplyConversionWorkspaceRequestIn": "_datamigration_70_ApplyConversionWorkspaceRequestIn",
        "ApplyConversionWorkspaceRequestOut": "_datamigration_71_ApplyConversionWorkspaceRequestOut",
        "AuditLogConfigIn": "_datamigration_72_AuditLogConfigIn",
        "AuditLogConfigOut": "_datamigration_73_AuditLogConfigOut",
        "UserPasswordIn": "_datamigration_74_UserPasswordIn",
        "UserPasswordOut": "_datamigration_75_UserPasswordOut",
        "MySqlConnectionProfileIn": "_datamigration_76_MySqlConnectionProfileIn",
        "MySqlConnectionProfileOut": "_datamigration_77_MySqlConnectionProfileOut",
        "LocationIn": "_datamigration_78_LocationIn",
        "LocationOut": "_datamigration_79_LocationOut",
        "StopMigrationJobRequestIn": "_datamigration_80_StopMigrationJobRequestIn",
        "StopMigrationJobRequestOut": "_datamigration_81_StopMigrationJobRequestOut",
        "EncryptionConfigIn": "_datamigration_82_EncryptionConfigIn",
        "EncryptionConfigOut": "_datamigration_83_EncryptionConfigOut",
        "SetIamPolicyRequestIn": "_datamigration_84_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_datamigration_85_SetIamPolicyRequestOut",
        "PrivateConnectionIn": "_datamigration_86_PrivateConnectionIn",
        "PrivateConnectionOut": "_datamigration_87_PrivateConnectionOut",
        "EntityMappingLogEntryIn": "_datamigration_88_EntityMappingLogEntryIn",
        "EntityMappingLogEntryOut": "_datamigration_89_EntityMappingLogEntryOut",
        "ConversionWorkspaceIn": "_datamigration_90_ConversionWorkspaceIn",
        "ConversionWorkspaceOut": "_datamigration_91_ConversionWorkspaceOut",
        "ResumeMigrationJobRequestIn": "_datamigration_92_ResumeMigrationJobRequestIn",
        "ResumeMigrationJobRequestOut": "_datamigration_93_ResumeMigrationJobRequestOut",
        "ExprIn": "_datamigration_94_ExprIn",
        "ExprOut": "_datamigration_95_ExprOut",
        "ListLocationsResponseIn": "_datamigration_96_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_datamigration_97_ListLocationsResponseOut",
        "TestIamPermissionsResponseIn": "_datamigration_98_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_datamigration_99_TestIamPermissionsResponseOut",
        "FetchStaticIpsResponseIn": "_datamigration_100_FetchStaticIpsResponseIn",
        "FetchStaticIpsResponseOut": "_datamigration_101_FetchStaticIpsResponseOut",
        "DumpFlagsIn": "_datamigration_102_DumpFlagsIn",
        "DumpFlagsOut": "_datamigration_103_DumpFlagsOut",
        "ConnectionProfileIn": "_datamigration_104_ConnectionProfileIn",
        "ConnectionProfileOut": "_datamigration_105_ConnectionProfileOut",
        "CommitConversionWorkspaceRequestIn": "_datamigration_106_CommitConversionWorkspaceRequestIn",
        "CommitConversionWorkspaceRequestOut": "_datamigration_107_CommitConversionWorkspaceRequestOut",
        "CloudSqlSettingsIn": "_datamigration_108_CloudSqlSettingsIn",
        "CloudSqlSettingsOut": "_datamigration_109_CloudSqlSettingsOut",
        "TestIamPermissionsRequestIn": "_datamigration_110_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_datamigration_111_TestIamPermissionsRequestOut",
        "CloudSqlConnectionProfileIn": "_datamigration_112_CloudSqlConnectionProfileIn",
        "CloudSqlConnectionProfileOut": "_datamigration_113_CloudSqlConnectionProfileOut",
        "CancelOperationRequestIn": "_datamigration_114_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_datamigration_115_CancelOperationRequestOut",
        "ConstraintEntityIn": "_datamigration_116_ConstraintEntityIn",
        "ConstraintEntityOut": "_datamigration_117_ConstraintEntityOut",
        "VerifyMigrationJobRequestIn": "_datamigration_118_VerifyMigrationJobRequestIn",
        "VerifyMigrationJobRequestOut": "_datamigration_119_VerifyMigrationJobRequestOut",
        "SslConfigIn": "_datamigration_120_SslConfigIn",
        "SslConfigOut": "_datamigration_121_SslConfigOut",
        "DumpFlagIn": "_datamigration_122_DumpFlagIn",
        "DumpFlagOut": "_datamigration_123_DumpFlagOut",
        "RulesFileIn": "_datamigration_124_RulesFileIn",
        "RulesFileOut": "_datamigration_125_RulesFileOut",
        "SequenceEntityIn": "_datamigration_126_SequenceEntityIn",
        "SequenceEntityOut": "_datamigration_127_SequenceEntityOut",
        "ImportRulesJobDetailsIn": "_datamigration_128_ImportRulesJobDetailsIn",
        "ImportRulesJobDetailsOut": "_datamigration_129_ImportRulesJobDetailsOut",
        "ApplyJobDetailsIn": "_datamigration_130_ApplyJobDetailsIn",
        "ApplyJobDetailsOut": "_datamigration_131_ApplyJobDetailsOut",
        "ReverseSshConnectivityIn": "_datamigration_132_ReverseSshConnectivityIn",
        "ReverseSshConnectivityOut": "_datamigration_133_ReverseSshConnectivityOut",
        "ConversionWorkspaceInfoIn": "_datamigration_134_ConversionWorkspaceInfoIn",
        "ConversionWorkspaceInfoOut": "_datamigration_135_ConversionWorkspaceInfoOut",
        "BindingIn": "_datamigration_136_BindingIn",
        "BindingOut": "_datamigration_137_BindingOut",
        "SeedConversionWorkspaceRequestIn": "_datamigration_138_SeedConversionWorkspaceRequestIn",
        "SeedConversionWorkspaceRequestOut": "_datamigration_139_SeedConversionWorkspaceRequestOut",
        "ViewEntityIn": "_datamigration_140_ViewEntityIn",
        "ViewEntityOut": "_datamigration_141_ViewEntityOut",
        "ListPrivateConnectionsResponseIn": "_datamigration_142_ListPrivateConnectionsResponseIn",
        "ListPrivateConnectionsResponseOut": "_datamigration_143_ListPrivateConnectionsResponseOut",
        "SqlAclEntryIn": "_datamigration_144_SqlAclEntryIn",
        "SqlAclEntryOut": "_datamigration_145_SqlAclEntryOut",
        "DescribeConversionWorkspaceRevisionsResponseIn": "_datamigration_146_DescribeConversionWorkspaceRevisionsResponseIn",
        "DescribeConversionWorkspaceRevisionsResponseOut": "_datamigration_147_DescribeConversionWorkspaceRevisionsResponseOut",
        "PolicyIn": "_datamigration_148_PolicyIn",
        "PolicyOut": "_datamigration_149_PolicyOut",
        "OracleConnectionProfileIn": "_datamigration_150_OracleConnectionProfileIn",
        "OracleConnectionProfileOut": "_datamigration_151_OracleConnectionProfileOut",
        "DatabaseEngineInfoIn": "_datamigration_152_DatabaseEngineInfoIn",
        "DatabaseEngineInfoOut": "_datamigration_153_DatabaseEngineInfoOut",
        "StaticServiceIpConnectivityIn": "_datamigration_154_StaticServiceIpConnectivityIn",
        "StaticServiceIpConnectivityOut": "_datamigration_155_StaticServiceIpConnectivityOut",
        "IndexEntityIn": "_datamigration_156_IndexEntityIn",
        "IndexEntityOut": "_datamigration_157_IndexEntityOut",
        "RollbackConversionWorkspaceRequestIn": "_datamigration_158_RollbackConversionWorkspaceRequestIn",
        "RollbackConversionWorkspaceRequestOut": "_datamigration_159_RollbackConversionWorkspaceRequestOut",
        "PromoteMigrationJobRequestIn": "_datamigration_160_PromoteMigrationJobRequestIn",
        "PromoteMigrationJobRequestOut": "_datamigration_161_PromoteMigrationJobRequestOut",
        "ImportMappingRulesRequestIn": "_datamigration_162_ImportMappingRulesRequestIn",
        "ImportMappingRulesRequestOut": "_datamigration_163_ImportMappingRulesRequestOut",
        "SeedJobDetailsIn": "_datamigration_164_SeedJobDetailsIn",
        "SeedJobDetailsOut": "_datamigration_165_SeedJobDetailsOut",
        "DatabaseTypeIn": "_datamigration_166_DatabaseTypeIn",
        "DatabaseTypeOut": "_datamigration_167_DatabaseTypeOut",
        "EmptyIn": "_datamigration_168_EmptyIn",
        "EmptyOut": "_datamigration_169_EmptyOut",
        "TriggerEntityIn": "_datamigration_170_TriggerEntityIn",
        "TriggerEntityOut": "_datamigration_171_TriggerEntityOut",
        "RestartMigrationJobRequestIn": "_datamigration_172_RestartMigrationJobRequestIn",
        "RestartMigrationJobRequestOut": "_datamigration_173_RestartMigrationJobRequestOut",
        "PrivateConnectivityIn": "_datamigration_174_PrivateConnectivityIn",
        "PrivateConnectivityOut": "_datamigration_175_PrivateConnectivityOut",
        "VpcPeeringConfigIn": "_datamigration_176_VpcPeeringConfigIn",
        "VpcPeeringConfigOut": "_datamigration_177_VpcPeeringConfigOut",
        "DatabaseEntityIn": "_datamigration_178_DatabaseEntityIn",
        "DatabaseEntityOut": "_datamigration_179_DatabaseEntityOut",
        "EntityMappingIn": "_datamigration_180_EntityMappingIn",
        "EntityMappingOut": "_datamigration_181_EntityMappingOut",
        "PackageEntityIn": "_datamigration_182_PackageEntityIn",
        "PackageEntityOut": "_datamigration_183_PackageEntityOut",
        "BackgroundJobLogEntryIn": "_datamigration_184_BackgroundJobLogEntryIn",
        "BackgroundJobLogEntryOut": "_datamigration_185_BackgroundJobLogEntryOut",
        "StatusIn": "_datamigration_186_StatusIn",
        "StatusOut": "_datamigration_187_StatusOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AlloyDbSettingsIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "primaryInstanceSettings": t.proxy(renames["PrimaryInstanceSettingsIn"]),
            "vpcNetwork": t.string(),
            "initialUser": t.proxy(renames["UserPasswordIn"]),
            "encryptionConfig": t.proxy(renames["EncryptionConfigIn"]).optional(),
        }
    ).named(renames["AlloyDbSettingsIn"])
    types["AlloyDbSettingsOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "primaryInstanceSettings": t.proxy(renames["PrimaryInstanceSettingsOut"]),
            "vpcNetwork": t.string(),
            "initialUser": t.proxy(renames["UserPasswordOut"]),
            "encryptionConfig": t.proxy(renames["EncryptionConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlloyDbSettingsOut"])
    types["ColumnEntityIn"] = t.struct(
        {
            "precision": t.integer().optional(),
            "collation": t.string().optional(),
            "array": t.boolean().optional(),
            "length": t.string().optional(),
            "ordinalPosition": t.integer().optional(),
            "arrayLength": t.integer().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "comment": t.string().optional(),
            "udt": t.boolean().optional(),
            "autoGenerated": t.boolean().optional(),
            "fractionalSecondsPrecision": t.integer().optional(),
            "charset": t.string().optional(),
            "setValues": t.array(t.string()).optional(),
            "nullable": t.boolean().optional(),
            "dataType": t.string().optional(),
            "scale": t.integer().optional(),
            "defaultValue": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ColumnEntityIn"])
    types["ColumnEntityOut"] = t.struct(
        {
            "precision": t.integer().optional(),
            "collation": t.string().optional(),
            "array": t.boolean().optional(),
            "length": t.string().optional(),
            "ordinalPosition": t.integer().optional(),
            "arrayLength": t.integer().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "comment": t.string().optional(),
            "udt": t.boolean().optional(),
            "autoGenerated": t.boolean().optional(),
            "fractionalSecondsPrecision": t.integer().optional(),
            "charset": t.string().optional(),
            "setValues": t.array(t.string()).optional(),
            "nullable": t.boolean().optional(),
            "dataType": t.string().optional(),
            "scale": t.integer().optional(),
            "defaultValue": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColumnEntityOut"])
    types["StartMigrationJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StartMigrationJobRequestIn"]
    )
    types["StartMigrationJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StartMigrationJobRequestOut"])
    types["ListConnectionProfilesResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "connectionProfiles": t.array(
                t.proxy(renames["ConnectionProfileIn"])
            ).optional(),
        }
    ).named(renames["ListConnectionProfilesResponseIn"])
    types["ListConnectionProfilesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "connectionProfiles": t.array(
                t.proxy(renames["ConnectionProfileOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConnectionProfilesResponseOut"])
    types["SqlIpConfigIn"] = t.struct(
        {
            "authorizedNetworks": t.array(t.proxy(renames["SqlAclEntryIn"])).optional(),
            "enableIpv4": t.boolean().optional(),
            "allocatedIpRange": t.string().optional(),
            "privateNetwork": t.string().optional(),
            "requireSsl": t.boolean().optional(),
        }
    ).named(renames["SqlIpConfigIn"])
    types["SqlIpConfigOut"] = t.struct(
        {
            "authorizedNetworks": t.array(
                t.proxy(renames["SqlAclEntryOut"])
            ).optional(),
            "enableIpv4": t.boolean().optional(),
            "allocatedIpRange": t.string().optional(),
            "privateNetwork": t.string().optional(),
            "requireSsl": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlIpConfigOut"])
    types["ForwardSshTunnelConnectivityIn"] = t.struct(
        {
            "privateKey": t.string().optional(),
            "hostname": t.string(),
            "password": t.string().optional(),
            "port": t.integer().optional(),
            "username": t.string(),
        }
    ).named(renames["ForwardSshTunnelConnectivityIn"])
    types["ForwardSshTunnelConnectivityOut"] = t.struct(
        {
            "privateKey": t.string().optional(),
            "hostname": t.string(),
            "password": t.string().optional(),
            "port": t.integer().optional(),
            "username": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ForwardSshTunnelConnectivityOut"])
    types["SchemaEntityIn"] = t.struct(
        {"customFeatures": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["SchemaEntityIn"])
    types["SchemaEntityOut"] = t.struct(
        {
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaEntityOut"])
    types["VmSelectionConfigIn"] = t.struct({"vmZone": t.string()}).named(
        renames["VmSelectionConfigIn"]
    )
    types["VmSelectionConfigOut"] = t.struct(
        {"vmZone": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VmSelectionConfigOut"])
    types["GenerateSshScriptRequestIn"] = t.struct(
        {
            "vm": t.string(),
            "vmPort": t.integer().optional(),
            "vmCreationConfig": t.proxy(renames["VmCreationConfigIn"]).optional(),
            "vmSelectionConfig": t.proxy(renames["VmSelectionConfigIn"]).optional(),
        }
    ).named(renames["GenerateSshScriptRequestIn"])
    types["GenerateSshScriptRequestOut"] = t.struct(
        {
            "vm": t.string(),
            "vmPort": t.integer().optional(),
            "vmCreationConfig": t.proxy(renames["VmCreationConfigOut"]).optional(),
            "vmSelectionConfig": t.proxy(renames["VmSelectionConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateSshScriptRequestOut"])
    types["ListMigrationJobsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "migrationJobs": t.array(t.proxy(renames["MigrationJobIn"])).optional(),
        }
    ).named(renames["ListMigrationJobsResponseIn"])
    types["ListMigrationJobsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "migrationJobs": t.array(t.proxy(renames["MigrationJobOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMigrationJobsResponseOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["PrimaryInstanceSettingsIn"] = t.struct(
        {
            "machineConfig": t.proxy(renames["MachineConfigIn"]).optional(),
            "id": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "databaseFlags": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PrimaryInstanceSettingsIn"])
    types["PrimaryInstanceSettingsOut"] = t.struct(
        {
            "machineConfig": t.proxy(renames["MachineConfigOut"]).optional(),
            "id": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "databaseFlags": t.struct({"_": t.string().optional()}).optional(),
            "privateIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrimaryInstanceSettingsOut"])
    types["ConvertJobDetailsIn"] = t.struct({"filter": t.string().optional()}).named(
        renames["ConvertJobDetailsIn"]
    )
    types["ConvertJobDetailsOut"] = t.struct(
        {
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConvertJobDetailsOut"])
    types["GoogleCloudClouddmsV1OperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudClouddmsV1OperationMetadataIn"])
    types["GoogleCloudClouddmsV1OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "statusMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudClouddmsV1OperationMetadataOut"])
    types["SshScriptIn"] = t.struct({"script": t.string().optional()}).named(
        renames["SshScriptIn"]
    )
    types["SshScriptOut"] = t.struct(
        {
            "script": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SshScriptOut"])
    types["VpcPeeringConnectivityIn"] = t.struct({"vpc": t.string().optional()}).named(
        renames["VpcPeeringConnectivityIn"]
    )
    types["VpcPeeringConnectivityOut"] = t.struct(
        {
            "vpc": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VpcPeeringConnectivityOut"])
    types["MigrationJobIn"] = t.struct(
        {
            "destination": t.string(),
            "staticIpConnectivity": t.proxy(
                renames["StaticIpConnectivityIn"]
            ).optional(),
            "vpcPeeringConnectivity": t.proxy(
                renames["VpcPeeringConnectivityIn"]
            ).optional(),
            "dumpFlags": t.proxy(renames["DumpFlagsIn"]).optional(),
            "type": t.string(),
            "source": t.string(),
            "name": t.string().optional(),
            "dumpPath": t.string().optional(),
            "reverseSshConnectivity": t.proxy(
                renames["ReverseSshConnectivityIn"]
            ).optional(),
            "destinationDatabase": t.proxy(renames["DatabaseTypeIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "conversionWorkspace": t.proxy(
                renames["ConversionWorkspaceInfoIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "state": t.string().optional(),
            "filter": t.string().optional(),
            "sourceDatabase": t.proxy(renames["DatabaseTypeIn"]).optional(),
        }
    ).named(renames["MigrationJobIn"])
    types["MigrationJobOut"] = t.struct(
        {
            "destination": t.string(),
            "updateTime": t.string().optional(),
            "duration": t.string().optional(),
            "staticIpConnectivity": t.proxy(
                renames["StaticIpConnectivityOut"]
            ).optional(),
            "vpcPeeringConnectivity": t.proxy(
                renames["VpcPeeringConnectivityOut"]
            ).optional(),
            "dumpFlags": t.proxy(renames["DumpFlagsOut"]).optional(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "source": t.string(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "dumpPath": t.string().optional(),
            "reverseSshConnectivity": t.proxy(
                renames["ReverseSshConnectivityOut"]
            ).optional(),
            "destinationDatabase": t.proxy(renames["DatabaseTypeOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "phase": t.string().optional(),
            "conversionWorkspace": t.proxy(
                renames["ConversionWorkspaceInfoOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "filter": t.string().optional(),
            "sourceDatabase": t.proxy(renames["DatabaseTypeOut"]).optional(),
        }
    ).named(renames["MigrationJobOut"])
    types["StaticIpConnectivityIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StaticIpConnectivityIn"]
    )
    types["StaticIpConnectivityOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StaticIpConnectivityOut"])
    types["MachineConfigIn"] = t.struct({"cpuCount": t.integer().optional()}).named(
        renames["MachineConfigIn"]
    )
    types["MachineConfigOut"] = t.struct(
        {
            "cpuCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MachineConfigOut"])
    types["TableEntityIn"] = t.struct(
        {
            "triggers": t.array(t.proxy(renames["TriggerEntityIn"])).optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "columns": t.array(t.proxy(renames["ColumnEntityIn"])).optional(),
            "comment": t.string().optional(),
            "constraints": t.array(t.proxy(renames["ConstraintEntityIn"])).optional(),
            "indices": t.array(t.proxy(renames["IndexEntityIn"])).optional(),
        }
    ).named(renames["TableEntityIn"])
    types["TableEntityOut"] = t.struct(
        {
            "triggers": t.array(t.proxy(renames["TriggerEntityOut"])).optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "columns": t.array(t.proxy(renames["ColumnEntityOut"])).optional(),
            "comment": t.string().optional(),
            "constraints": t.array(t.proxy(renames["ConstraintEntityOut"])).optional(),
            "indices": t.array(t.proxy(renames["IndexEntityOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableEntityOut"])
    types["PostgreSqlConnectionProfileIn"] = t.struct(
        {
            "ssl": t.proxy(renames["SslConfigIn"]).optional(),
            "password": t.string(),
            "port": t.integer(),
            "staticIpConnectivity": t.proxy(
                renames["StaticIpConnectivityIn"]
            ).optional(),
            "username": t.string(),
            "cloudSqlId": t.string().optional(),
            "host": t.string(),
            "privateServiceConnectConnectivity": t.proxy(
                renames["PrivateServiceConnectConnectivityIn"]
            ).optional(),
        }
    ).named(renames["PostgreSqlConnectionProfileIn"])
    types["PostgreSqlConnectionProfileOut"] = t.struct(
        {
            "ssl": t.proxy(renames["SslConfigOut"]).optional(),
            "password": t.string(),
            "port": t.integer(),
            "staticIpConnectivity": t.proxy(
                renames["StaticIpConnectivityOut"]
            ).optional(),
            "networkArchitecture": t.string().optional(),
            "username": t.string(),
            "cloudSqlId": t.string().optional(),
            "host": t.string(),
            "passwordSet": t.boolean().optional(),
            "privateServiceConnectConnectivity": t.proxy(
                renames["PrivateServiceConnectConnectivityOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostgreSqlConnectionProfileOut"])
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
    types["SearchBackgroundJobsResponseIn"] = t.struct(
        {"jobs": t.array(t.proxy(renames["BackgroundJobLogEntryIn"])).optional()}
    ).named(renames["SearchBackgroundJobsResponseIn"])
    types["SearchBackgroundJobsResponseOut"] = t.struct(
        {
            "jobs": t.array(t.proxy(renames["BackgroundJobLogEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchBackgroundJobsResponseOut"])
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
    types["PrivateServiceConnectConnectivityIn"] = t.struct(
        {"serviceAttachment": t.string()}
    ).named(renames["PrivateServiceConnectConnectivityIn"])
    types["PrivateServiceConnectConnectivityOut"] = t.struct(
        {
            "serviceAttachment": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateServiceConnectConnectivityOut"])
    types["MigrationJobVerificationErrorIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["MigrationJobVerificationErrorIn"])
    types["MigrationJobVerificationErrorOut"] = t.struct(
        {
            "errorCode": t.string().optional(),
            "errorDetailMessage": t.string().optional(),
            "errorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MigrationJobVerificationErrorOut"])
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
    types["MySqlConnectionProfileIn"] = t.struct(
        {
            "ssl": t.proxy(renames["SslConfigIn"]).optional(),
            "password": t.string(),
            "port": t.integer(),
            "host": t.string(),
            "username": t.string(),
            "cloudSqlId": t.string().optional(),
        }
    ).named(renames["MySqlConnectionProfileIn"])
    types["MySqlConnectionProfileOut"] = t.struct(
        {
            "ssl": t.proxy(renames["SslConfigOut"]).optional(),
            "password": t.string(),
            "port": t.integer(),
            "passwordSet": t.boolean().optional(),
            "host": t.string(),
            "username": t.string(),
            "cloudSqlId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MySqlConnectionProfileOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["StopMigrationJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StopMigrationJobRequestIn"]
    )
    types["StopMigrationJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StopMigrationJobRequestOut"])
    types["EncryptionConfigIn"] = t.struct({"kmsKeyName": t.string().optional()}).named(
        renames["EncryptionConfigIn"]
    )
    types["EncryptionConfigOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionConfigOut"])
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
    types["PrivateConnectionIn"] = t.struct(
        {
            "vpcPeeringConfig": t.proxy(renames["VpcPeeringConfigIn"]).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PrivateConnectionIn"])
    types["PrivateConnectionOut"] = t.struct(
        {
            "vpcPeeringConfig": t.proxy(renames["VpcPeeringConfigOut"]).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PrivateConnectionOut"])
    types["EntityMappingLogEntryIn"] = t.struct(
        {
            "mappingComment": t.string().optional(),
            "ruleRevisionId": t.string().optional(),
            "ruleId": t.string().optional(),
        }
    ).named(renames["EntityMappingLogEntryIn"])
    types["EntityMappingLogEntryOut"] = t.struct(
        {
            "mappingComment": t.string().optional(),
            "ruleRevisionId": t.string().optional(),
            "ruleId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityMappingLogEntryOut"])
    types["ConversionWorkspaceIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "destination": t.proxy(renames["DatabaseEngineInfoIn"]),
            "source": t.proxy(renames["DatabaseEngineInfoIn"]),
            "globalSettings": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ConversionWorkspaceIn"])
    types["ConversionWorkspaceOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "destination": t.proxy(renames["DatabaseEngineInfoOut"]),
            "updateTime": t.string().optional(),
            "hasUncommittedChanges": t.boolean().optional(),
            "latestCommitId": t.string().optional(),
            "createTime": t.string().optional(),
            "source": t.proxy(renames["DatabaseEngineInfoOut"]),
            "globalSettings": t.struct({"_": t.string().optional()}).optional(),
            "latestCommitTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConversionWorkspaceOut"])
    types["ResumeMigrationJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResumeMigrationJobRequestIn"]
    )
    types["ResumeMigrationJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumeMigrationJobRequestOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "postgresql": t.proxy(renames["PostgreSqlConnectionProfileIn"]).optional(),
            "provider": t.string().optional(),
            "cloudsql": t.proxy(renames["CloudSqlConnectionProfileIn"]).optional(),
            "mysql": t.proxy(renames["MySqlConnectionProfileIn"]).optional(),
            "oracle": t.proxy(renames["OracleConnectionProfileIn"]).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "state": t.string().optional(),
            "alloydb": t.proxy(renames["AlloyDbConnectionProfileIn"]).optional(),
        }
    ).named(renames["ConnectionProfileIn"])
    types["ConnectionProfileOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "postgresql": t.proxy(renames["PostgreSqlConnectionProfileOut"]).optional(),
            "provider": t.string().optional(),
            "cloudsql": t.proxy(renames["CloudSqlConnectionProfileOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "updateTime": t.string().optional(),
            "mysql": t.proxy(renames["MySqlConnectionProfileOut"]).optional(),
            "oracle": t.proxy(renames["OracleConnectionProfileOut"]).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "state": t.string().optional(),
            "alloydb": t.proxy(renames["AlloyDbConnectionProfileOut"]).optional(),
        }
    ).named(renames["ConnectionProfileOut"])
    types["CommitConversionWorkspaceRequestIn"] = t.struct(
        {"commitName": t.string().optional()}
    ).named(renames["CommitConversionWorkspaceRequestIn"])
    types["CommitConversionWorkspaceRequestOut"] = t.struct(
        {
            "commitName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitConversionWorkspaceRequestOut"])
    types["CloudSqlSettingsIn"] = t.struct(
        {
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "tier": t.string().optional(),
            "databaseFlags": t.struct({"_": t.string().optional()}).optional(),
            "availabilityType": t.string().optional(),
            "rootPassword": t.string().optional(),
            "ipConfig": t.proxy(renames["SqlIpConfigIn"]).optional(),
            "autoStorageIncrease": t.boolean().optional(),
            "dataDiskSizeGb": t.string().optional(),
            "cmekKeyName": t.string().optional(),
            "databaseVersion": t.string().optional(),
            "collation": t.string().optional(),
            "zone": t.string().optional(),
            "secondaryZone": t.string().optional(),
            "sourceId": t.string().optional(),
            "dataDiskType": t.string().optional(),
            "storageAutoResizeLimit": t.string().optional(),
            "activationPolicy": t.string().optional(),
        }
    ).named(renames["CloudSqlSettingsIn"])
    types["CloudSqlSettingsOut"] = t.struct(
        {
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "tier": t.string().optional(),
            "databaseFlags": t.struct({"_": t.string().optional()}).optional(),
            "availabilityType": t.string().optional(),
            "rootPassword": t.string().optional(),
            "ipConfig": t.proxy(renames["SqlIpConfigOut"]).optional(),
            "autoStorageIncrease": t.boolean().optional(),
            "dataDiskSizeGb": t.string().optional(),
            "cmekKeyName": t.string().optional(),
            "databaseVersion": t.string().optional(),
            "rootPasswordSet": t.boolean().optional(),
            "collation": t.string().optional(),
            "zone": t.string().optional(),
            "secondaryZone": t.string().optional(),
            "sourceId": t.string().optional(),
            "dataDiskType": t.string().optional(),
            "storageAutoResizeLimit": t.string().optional(),
            "activationPolicy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudSqlSettingsOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["CloudSqlConnectionProfileIn"] = t.struct(
        {"settings": t.proxy(renames["CloudSqlSettingsIn"]).optional()}
    ).named(renames["CloudSqlConnectionProfileIn"])
    types["CloudSqlConnectionProfileOut"] = t.struct(
        {
            "cloudSqlId": t.string().optional(),
            "additionalPublicIp": t.string().optional(),
            "privateIp": t.string().optional(),
            "publicIp": t.string().optional(),
            "settings": t.proxy(renames["CloudSqlSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudSqlConnectionProfileOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["ConstraintEntityIn"] = t.struct(
        {
            "tableColumns": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "referenceColumns": t.array(t.string()).optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "tableName": t.string().optional(),
            "referenceTable": t.string().optional(),
        }
    ).named(renames["ConstraintEntityIn"])
    types["ConstraintEntityOut"] = t.struct(
        {
            "tableColumns": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "referenceColumns": t.array(t.string()).optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "tableName": t.string().optional(),
            "referenceTable": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConstraintEntityOut"])
    types["VerifyMigrationJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VerifyMigrationJobRequestIn"]
    )
    types["VerifyMigrationJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VerifyMigrationJobRequestOut"])
    types["SslConfigIn"] = t.struct(
        {
            "caCertificate": t.string(),
            "clientKey": t.string().optional(),
            "clientCertificate": t.string().optional(),
        }
    ).named(renames["SslConfigIn"])
    types["SslConfigOut"] = t.struct(
        {
            "caCertificate": t.string(),
            "type": t.string().optional(),
            "clientKey": t.string().optional(),
            "clientCertificate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SslConfigOut"])
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
    types["SequenceEntityIn"] = t.struct(
        {
            "cache": t.string().optional(),
            "increment": t.string().optional(),
            "startValue": t.string().optional(),
            "minValue": t.string().optional(),
            "maxValue": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "cycle": t.boolean().optional(),
        }
    ).named(renames["SequenceEntityIn"])
    types["SequenceEntityOut"] = t.struct(
        {
            "cache": t.string().optional(),
            "increment": t.string().optional(),
            "startValue": t.string().optional(),
            "minValue": t.string().optional(),
            "maxValue": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "cycle": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SequenceEntityOut"])
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
    types["ReverseSshConnectivityIn"] = t.struct(
        {
            "vmIp": t.string(),
            "vpc": t.string().optional(),
            "vm": t.string().optional(),
            "vmPort": t.integer(),
        }
    ).named(renames["ReverseSshConnectivityIn"])
    types["ReverseSshConnectivityOut"] = t.struct(
        {
            "vmIp": t.string(),
            "vpc": t.string().optional(),
            "vm": t.string().optional(),
            "vmPort": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReverseSshConnectivityOut"])
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
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["SeedConversionWorkspaceRequestIn"] = t.struct(
        {
            "sourceConnectionProfile": t.string().optional(),
            "destinationConnectionProfile": t.string().optional(),
            "autoCommit": t.boolean().optional(),
        }
    ).named(renames["SeedConversionWorkspaceRequestIn"])
    types["SeedConversionWorkspaceRequestOut"] = t.struct(
        {
            "sourceConnectionProfile": t.string().optional(),
            "destinationConnectionProfile": t.string().optional(),
            "autoCommit": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SeedConversionWorkspaceRequestOut"])
    types["ViewEntityIn"] = t.struct(
        {
            "constraints": t.array(t.proxy(renames["ConstraintEntityIn"])).optional(),
            "sqlCode": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ViewEntityIn"])
    types["ViewEntityOut"] = t.struct(
        {
            "constraints": t.array(t.proxy(renames["ConstraintEntityOut"])).optional(),
            "sqlCode": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViewEntityOut"])
    types["ListPrivateConnectionsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "privateConnections": t.array(
                t.proxy(renames["PrivateConnectionIn"])
            ).optional(),
        }
    ).named(renames["ListPrivateConnectionsResponseIn"])
    types["ListPrivateConnectionsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "privateConnections": t.array(
                t.proxy(renames["PrivateConnectionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPrivateConnectionsResponseOut"])
    types["SqlAclEntryIn"] = t.struct(
        {
            "value": t.string().optional(),
            "label": t.string().optional(),
            "ttl": t.string().optional(),
            "expireTime": t.string().optional(),
        }
    ).named(renames["SqlAclEntryIn"])
    types["SqlAclEntryOut"] = t.struct(
        {
            "value": t.string().optional(),
            "label": t.string().optional(),
            "ttl": t.string().optional(),
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlAclEntryOut"])
    types["DescribeConversionWorkspaceRevisionsResponseIn"] = t.struct(
        {"revisions": t.array(t.proxy(renames["ConversionWorkspaceIn"])).optional()}
    ).named(renames["DescribeConversionWorkspaceRevisionsResponseIn"])
    types["DescribeConversionWorkspaceRevisionsResponseOut"] = t.struct(
        {
            "revisions": t.array(t.proxy(renames["ConversionWorkspaceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DescribeConversionWorkspaceRevisionsResponseOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["OracleConnectionProfileIn"] = t.struct(
        {
            "privateConnectivity": t.proxy(renames["PrivateConnectivityIn"]).optional(),
            "databaseService": t.string(),
            "host": t.string(),
            "port": t.integer(),
            "password": t.string(),
            "staticServiceIpConnectivity": t.proxy(
                renames["StaticServiceIpConnectivityIn"]
            ).optional(),
            "username": t.string(),
            "forwardSshConnectivity": t.proxy(
                renames["ForwardSshTunnelConnectivityIn"]
            ).optional(),
        }
    ).named(renames["OracleConnectionProfileIn"])
    types["OracleConnectionProfileOut"] = t.struct(
        {
            "privateConnectivity": t.proxy(
                renames["PrivateConnectivityOut"]
            ).optional(),
            "databaseService": t.string(),
            "host": t.string(),
            "port": t.integer(),
            "passwordSet": t.boolean().optional(),
            "password": t.string(),
            "staticServiceIpConnectivity": t.proxy(
                renames["StaticServiceIpConnectivityOut"]
            ).optional(),
            "username": t.string(),
            "forwardSshConnectivity": t.proxy(
                renames["ForwardSshTunnelConnectivityOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OracleConnectionProfileOut"])
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
    types["StaticServiceIpConnectivityIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["StaticServiceIpConnectivityIn"])
    types["StaticServiceIpConnectivityOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StaticServiceIpConnectivityOut"])
    types["IndexEntityIn"] = t.struct(
        {
            "type": t.string().optional(),
            "name": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "unique": t.boolean().optional(),
            "tableColumns": t.array(t.string()).optional(),
        }
    ).named(renames["IndexEntityIn"])
    types["IndexEntityOut"] = t.struct(
        {
            "type": t.string().optional(),
            "name": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "unique": t.boolean().optional(),
            "tableColumns": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexEntityOut"])
    types["RollbackConversionWorkspaceRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RollbackConversionWorkspaceRequestIn"])
    types["RollbackConversionWorkspaceRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RollbackConversionWorkspaceRequestOut"])
    types["PromoteMigrationJobRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["PromoteMigrationJobRequestIn"])
    types["PromoteMigrationJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PromoteMigrationJobRequestOut"])
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
    types["SeedJobDetailsIn"] = t.struct(
        {"connectionProfile": t.string().optional()}
    ).named(renames["SeedJobDetailsIn"])
    types["SeedJobDetailsOut"] = t.struct(
        {
            "connectionProfile": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SeedJobDetailsOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["TriggerEntityIn"] = t.struct(
        {
            "triggeringEvents": t.array(t.string()).optional(),
            "sqlCode": t.string().optional(),
            "triggerType": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["TriggerEntityIn"])
    types["TriggerEntityOut"] = t.struct(
        {
            "triggeringEvents": t.array(t.string()).optional(),
            "sqlCode": t.string().optional(),
            "triggerType": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TriggerEntityOut"])
    types["RestartMigrationJobRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RestartMigrationJobRequestIn"])
    types["RestartMigrationJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RestartMigrationJobRequestOut"])
    types["PrivateConnectivityIn"] = t.struct({"privateConnection": t.string()}).named(
        renames["PrivateConnectivityIn"]
    )
    types["PrivateConnectivityOut"] = t.struct(
        {
            "privateConnection": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateConnectivityOut"])
    types["VpcPeeringConfigIn"] = t.struct(
        {"vpcName": t.string(), "subnet": t.string()}
    ).named(renames["VpcPeeringConfigIn"])
    types["VpcPeeringConfigOut"] = t.struct(
        {
            "vpcName": t.string(),
            "subnet": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VpcPeeringConfigOut"])
    types["DatabaseEntityIn"] = t.struct(
        {
            "synonym": t.proxy(renames["SynonymEntityIn"]).optional(),
            "storedProcedure": t.proxy(renames["StoredProcedureEntityIn"]).optional(),
            "databaseFunction": t.proxy(renames["FunctionEntityIn"]).optional(),
            "table": t.proxy(renames["TableEntityIn"]).optional(),
            "mappings": t.array(t.proxy(renames["EntityMappingIn"])).optional(),
            "shortName": t.string().optional(),
            "sequence": t.proxy(renames["SequenceEntityIn"]).optional(),
            "schema": t.proxy(renames["SchemaEntityIn"]).optional(),
            "entityType": t.string().optional(),
            "tree": t.string().optional(),
            "parentEntity": t.string().optional(),
            "view": t.proxy(renames["ViewEntityIn"]).optional(),
            "databasePackage": t.proxy(renames["PackageEntityIn"]).optional(),
        }
    ).named(renames["DatabaseEntityIn"])
    types["DatabaseEntityOut"] = t.struct(
        {
            "synonym": t.proxy(renames["SynonymEntityOut"]).optional(),
            "storedProcedure": t.proxy(renames["StoredProcedureEntityOut"]).optional(),
            "databaseFunction": t.proxy(renames["FunctionEntityOut"]).optional(),
            "table": t.proxy(renames["TableEntityOut"]).optional(),
            "mappings": t.array(t.proxy(renames["EntityMappingOut"])).optional(),
            "shortName": t.string().optional(),
            "sequence": t.proxy(renames["SequenceEntityOut"]).optional(),
            "schema": t.proxy(renames["SchemaEntityOut"]).optional(),
            "entityType": t.string().optional(),
            "tree": t.string().optional(),
            "parentEntity": t.string().optional(),
            "view": t.proxy(renames["ViewEntityOut"]).optional(),
            "databasePackage": t.proxy(renames["PackageEntityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseEntityOut"])
    types["EntityMappingIn"] = t.struct(
        {
            "draftType": t.string().optional(),
            "sourceEntity": t.string().optional(),
            "mappingLog": t.array(
                t.proxy(renames["EntityMappingLogEntryIn"])
            ).optional(),
            "sourceType": t.string().optional(),
            "draftEntity": t.string().optional(),
        }
    ).named(renames["EntityMappingIn"])
    types["EntityMappingOut"] = t.struct(
        {
            "draftType": t.string().optional(),
            "sourceEntity": t.string().optional(),
            "mappingLog": t.array(
                t.proxy(renames["EntityMappingLogEntryOut"])
            ).optional(),
            "sourceType": t.string().optional(),
            "draftEntity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityMappingOut"])
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
    types["BackgroundJobLogEntryIn"] = t.struct(
        {
            "requestAutocommit": t.boolean().optional(),
            "seedJobDetails": t.proxy(renames["SeedJobDetailsIn"]).optional(),
            "id": t.string().optional(),
            "jobType": t.string().optional(),
            "completionState": t.string().optional(),
            "finishTime": t.string().optional(),
            "convertJobDetails": t.proxy(renames["ConvertJobDetailsIn"]).optional(),
            "importRulesJobDetails": t.proxy(
                renames["ImportRulesJobDetailsIn"]
            ).optional(),
            "startTime": t.string().optional(),
            "completionComment": t.string().optional(),
            "applyJobDetails": t.proxy(renames["ApplyJobDetailsIn"]).optional(),
        }
    ).named(renames["BackgroundJobLogEntryIn"])
    types["BackgroundJobLogEntryOut"] = t.struct(
        {
            "requestAutocommit": t.boolean().optional(),
            "seedJobDetails": t.proxy(renames["SeedJobDetailsOut"]).optional(),
            "id": t.string().optional(),
            "jobType": t.string().optional(),
            "completionState": t.string().optional(),
            "finishTime": t.string().optional(),
            "convertJobDetails": t.proxy(renames["ConvertJobDetailsOut"]).optional(),
            "importRulesJobDetails": t.proxy(
                renames["ImportRulesJobDetailsOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "completionComment": t.string().optional(),
            "applyJobDetails": t.proxy(renames["ApplyJobDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackgroundJobLogEntryOut"])
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

    functions = {}
    functions["projectsLocationsList"] = datamigration.get(
        "v1/{name}:fetchStaticIps",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FetchStaticIpsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsCreate"] = datamigration.post(
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
    functions["projectsLocationsPrivateConnectionsGetIamPolicy"] = datamigration.post(
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
    functions["projectsLocationsPrivateConnectionsList"] = datamigration.post(
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
    functions[
        "projectsLocationsPrivateConnectionsTestIamPermissions"
    ] = datamigration.post(
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
    functions["projectsLocationsPrivateConnectionsGet"] = datamigration.post(
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
    functions["projectsLocationsPrivateConnectionsDelete"] = datamigration.post(
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
    functions["projectsLocationsPrivateConnectionsSetIamPolicy"] = datamigration.post(
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
    functions["projectsLocationsMigrationJobsRestart"] = datamigration.post(
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
    functions["projectsLocationsMigrationJobsResume"] = datamigration.post(
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
    functions["projectsLocationsMigrationJobsList"] = datamigration.post(
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
    functions["projectsLocationsMigrationJobsPromote"] = datamigration.post(
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
    functions["projectsLocationsMigrationJobsDelete"] = datamigration.post(
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
    functions["projectsLocationsMigrationJobsCreate"] = datamigration.post(
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
    functions["projectsLocationsMigrationJobsSetIamPolicy"] = datamigration.post(
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
    functions["projectsLocationsMigrationJobsGenerateSshScript"] = datamigration.post(
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
    functions["projectsLocationsMigrationJobsGetIamPolicy"] = datamigration.post(
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
    functions["projectsLocationsMigrationJobsVerify"] = datamigration.post(
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
    functions["projectsLocationsMigrationJobsStart"] = datamigration.post(
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
    functions["projectsLocationsMigrationJobsGet"] = datamigration.post(
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
    functions["projectsLocationsMigrationJobsStop"] = datamigration.post(
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
    functions["projectsLocationsMigrationJobsTestIamPermissions"] = datamigration.post(
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
    functions["projectsLocationsConversionWorkspacesCreate"] = datamigration.post(
        "v1/{name}:convert",
        t.struct(
            {
                "name": t.string().optional(),
                "autoCommit": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesGetIamPolicy"] = datamigration.post(
        "v1/{name}:convert",
        t.struct(
            {
                "name": t.string().optional(),
                "autoCommit": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesCommit"] = datamigration.post(
        "v1/{name}:convert",
        t.struct(
            {
                "name": t.string().optional(),
                "autoCommit": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConversionWorkspacesSearchBackgroundJobs"
    ] = datamigration.post(
        "v1/{name}:convert",
        t.struct(
            {
                "name": t.string().optional(),
                "autoCommit": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesSeed"] = datamigration.post(
        "v1/{name}:convert",
        t.struct(
            {
                "name": t.string().optional(),
                "autoCommit": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesGet"] = datamigration.post(
        "v1/{name}:convert",
        t.struct(
            {
                "name": t.string().optional(),
                "autoCommit": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesPatch"] = datamigration.post(
        "v1/{name}:convert",
        t.struct(
            {
                "name": t.string().optional(),
                "autoCommit": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesRollback"] = datamigration.post(
        "v1/{name}:convert",
        t.struct(
            {
                "name": t.string().optional(),
                "autoCommit": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesSetIamPolicy"] = datamigration.post(
        "v1/{name}:convert",
        t.struct(
            {
                "name": t.string().optional(),
                "autoCommit": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConversionWorkspacesTestIamPermissions"
    ] = datamigration.post(
        "v1/{name}:convert",
        t.struct(
            {
                "name": t.string().optional(),
                "autoCommit": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesDelete"] = datamigration.post(
        "v1/{name}:convert",
        t.struct(
            {
                "name": t.string().optional(),
                "autoCommit": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesApply"] = datamigration.post(
        "v1/{name}:convert",
        t.struct(
            {
                "name": t.string().optional(),
                "autoCommit": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesList"] = datamigration.post(
        "v1/{name}:convert",
        t.struct(
            {
                "name": t.string().optional(),
                "autoCommit": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConversionWorkspacesDescribeDatabaseEntities"
    ] = datamigration.post(
        "v1/{name}:convert",
        t.struct(
            {
                "name": t.string().optional(),
                "autoCommit": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConversionWorkspacesDescribeConversionWorkspaceRevisions"
    ] = datamigration.post(
        "v1/{name}:convert",
        t.struct(
            {
                "name": t.string().optional(),
                "autoCommit": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesConvert"] = datamigration.post(
        "v1/{name}:convert",
        t.struct(
            {
                "name": t.string().optional(),
                "autoCommit": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
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
    functions["projectsLocationsOperationsGet"] = datamigration.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = datamigration.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesSetIamPolicy"] = datamigration.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "skipValidation": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "postgresql": t.proxy(
                    renames["PostgreSqlConnectionProfileIn"]
                ).optional(),
                "provider": t.string().optional(),
                "cloudsql": t.proxy(renames["CloudSqlConnectionProfileIn"]).optional(),
                "mysql": t.proxy(renames["MySqlConnectionProfileIn"]).optional(),
                "oracle": t.proxy(renames["OracleConnectionProfileIn"]).optional(),
                "displayName": t.string().optional(),
                "state": t.string().optional(),
                "alloydb": t.proxy(renames["AlloyDbConnectionProfileIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesGet"] = datamigration.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "skipValidation": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "postgresql": t.proxy(
                    renames["PostgreSqlConnectionProfileIn"]
                ).optional(),
                "provider": t.string().optional(),
                "cloudsql": t.proxy(renames["CloudSqlConnectionProfileIn"]).optional(),
                "mysql": t.proxy(renames["MySqlConnectionProfileIn"]).optional(),
                "oracle": t.proxy(renames["OracleConnectionProfileIn"]).optional(),
                "displayName": t.string().optional(),
                "state": t.string().optional(),
                "alloydb": t.proxy(renames["AlloyDbConnectionProfileIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesCreate"] = datamigration.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "skipValidation": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "postgresql": t.proxy(
                    renames["PostgreSqlConnectionProfileIn"]
                ).optional(),
                "provider": t.string().optional(),
                "cloudsql": t.proxy(renames["CloudSqlConnectionProfileIn"]).optional(),
                "mysql": t.proxy(renames["MySqlConnectionProfileIn"]).optional(),
                "oracle": t.proxy(renames["OracleConnectionProfileIn"]).optional(),
                "displayName": t.string().optional(),
                "state": t.string().optional(),
                "alloydb": t.proxy(renames["AlloyDbConnectionProfileIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesDelete"] = datamigration.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "skipValidation": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "postgresql": t.proxy(
                    renames["PostgreSqlConnectionProfileIn"]
                ).optional(),
                "provider": t.string().optional(),
                "cloudsql": t.proxy(renames["CloudSqlConnectionProfileIn"]).optional(),
                "mysql": t.proxy(renames["MySqlConnectionProfileIn"]).optional(),
                "oracle": t.proxy(renames["OracleConnectionProfileIn"]).optional(),
                "displayName": t.string().optional(),
                "state": t.string().optional(),
                "alloydb": t.proxy(renames["AlloyDbConnectionProfileIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConnectionProfilesTestIamPermissions"
    ] = datamigration.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "skipValidation": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "postgresql": t.proxy(
                    renames["PostgreSqlConnectionProfileIn"]
                ).optional(),
                "provider": t.string().optional(),
                "cloudsql": t.proxy(renames["CloudSqlConnectionProfileIn"]).optional(),
                "mysql": t.proxy(renames["MySqlConnectionProfileIn"]).optional(),
                "oracle": t.proxy(renames["OracleConnectionProfileIn"]).optional(),
                "displayName": t.string().optional(),
                "state": t.string().optional(),
                "alloydb": t.proxy(renames["AlloyDbConnectionProfileIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesList"] = datamigration.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "skipValidation": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "postgresql": t.proxy(
                    renames["PostgreSqlConnectionProfileIn"]
                ).optional(),
                "provider": t.string().optional(),
                "cloudsql": t.proxy(renames["CloudSqlConnectionProfileIn"]).optional(),
                "mysql": t.proxy(renames["MySqlConnectionProfileIn"]).optional(),
                "oracle": t.proxy(renames["OracleConnectionProfileIn"]).optional(),
                "displayName": t.string().optional(),
                "state": t.string().optional(),
                "alloydb": t.proxy(renames["AlloyDbConnectionProfileIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesGetIamPolicy"] = datamigration.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "skipValidation": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "postgresql": t.proxy(
                    renames["PostgreSqlConnectionProfileIn"]
                ).optional(),
                "provider": t.string().optional(),
                "cloudsql": t.proxy(renames["CloudSqlConnectionProfileIn"]).optional(),
                "mysql": t.proxy(renames["MySqlConnectionProfileIn"]).optional(),
                "oracle": t.proxy(renames["OracleConnectionProfileIn"]).optional(),
                "displayName": t.string().optional(),
                "state": t.string().optional(),
                "alloydb": t.proxy(renames["AlloyDbConnectionProfileIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesPatch"] = datamigration.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "skipValidation": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "postgresql": t.proxy(
                    renames["PostgreSqlConnectionProfileIn"]
                ).optional(),
                "provider": t.string().optional(),
                "cloudsql": t.proxy(renames["CloudSqlConnectionProfileIn"]).optional(),
                "mysql": t.proxy(renames["MySqlConnectionProfileIn"]).optional(),
                "oracle": t.proxy(renames["OracleConnectionProfileIn"]).optional(),
                "displayName": t.string().optional(),
                "state": t.string().optional(),
                "alloydb": t.proxy(renames["AlloyDbConnectionProfileIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="datamigration", renames=renames, types=types, functions=functions
    )
