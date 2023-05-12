from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_datamigration() -> Import:
    datamigration = HTTPRuntime("https://datamigration.googleapis.com/")

    renames = {
        "ErrorResponse": "_datamigration_1_ErrorResponse",
        "BackgroundJobLogEntryIn": "_datamigration_2_BackgroundJobLogEntryIn",
        "BackgroundJobLogEntryOut": "_datamigration_3_BackgroundJobLogEntryOut",
        "SeedJobDetailsIn": "_datamigration_4_SeedJobDetailsIn",
        "SeedJobDetailsOut": "_datamigration_5_SeedJobDetailsOut",
        "EmptyIn": "_datamigration_6_EmptyIn",
        "EmptyOut": "_datamigration_7_EmptyOut",
        "ExprIn": "_datamigration_8_ExprIn",
        "ExprOut": "_datamigration_9_ExprOut",
        "ColumnEntityIn": "_datamigration_10_ColumnEntityIn",
        "ColumnEntityOut": "_datamigration_11_ColumnEntityOut",
        "ResumeMigrationJobRequestIn": "_datamigration_12_ResumeMigrationJobRequestIn",
        "ResumeMigrationJobRequestOut": "_datamigration_13_ResumeMigrationJobRequestOut",
        "SynonymEntityIn": "_datamigration_14_SynonymEntityIn",
        "SynonymEntityOut": "_datamigration_15_SynonymEntityOut",
        "ReverseSshConnectivityIn": "_datamigration_16_ReverseSshConnectivityIn",
        "ReverseSshConnectivityOut": "_datamigration_17_ReverseSshConnectivityOut",
        "RestartMigrationJobRequestIn": "_datamigration_18_RestartMigrationJobRequestIn",
        "RestartMigrationJobRequestOut": "_datamigration_19_RestartMigrationJobRequestOut",
        "PrivateConnectionIn": "_datamigration_20_PrivateConnectionIn",
        "PrivateConnectionOut": "_datamigration_21_PrivateConnectionOut",
        "DumpFlagsIn": "_datamigration_22_DumpFlagsIn",
        "DumpFlagsOut": "_datamigration_23_DumpFlagsOut",
        "DescribeDatabaseEntitiesResponseIn": "_datamigration_24_DescribeDatabaseEntitiesResponseIn",
        "DescribeDatabaseEntitiesResponseOut": "_datamigration_25_DescribeDatabaseEntitiesResponseOut",
        "AlloyDbSettingsIn": "_datamigration_26_AlloyDbSettingsIn",
        "AlloyDbSettingsOut": "_datamigration_27_AlloyDbSettingsOut",
        "GenerateSshScriptRequestIn": "_datamigration_28_GenerateSshScriptRequestIn",
        "GenerateSshScriptRequestOut": "_datamigration_29_GenerateSshScriptRequestOut",
        "ForwardSshTunnelConnectivityIn": "_datamigration_30_ForwardSshTunnelConnectivityIn",
        "ForwardSshTunnelConnectivityOut": "_datamigration_31_ForwardSshTunnelConnectivityOut",
        "DumpFlagIn": "_datamigration_32_DumpFlagIn",
        "DumpFlagOut": "_datamigration_33_DumpFlagOut",
        "OracleConnectionProfileIn": "_datamigration_34_OracleConnectionProfileIn",
        "OracleConnectionProfileOut": "_datamigration_35_OracleConnectionProfileOut",
        "PrimaryInstanceSettingsIn": "_datamigration_36_PrimaryInstanceSettingsIn",
        "PrimaryInstanceSettingsOut": "_datamigration_37_PrimaryInstanceSettingsOut",
        "BindingIn": "_datamigration_38_BindingIn",
        "BindingOut": "_datamigration_39_BindingOut",
        "ConnectionProfileIn": "_datamigration_40_ConnectionProfileIn",
        "ConnectionProfileOut": "_datamigration_41_ConnectionProfileOut",
        "ConvertConversionWorkspaceRequestIn": "_datamigration_42_ConvertConversionWorkspaceRequestIn",
        "ConvertConversionWorkspaceRequestOut": "_datamigration_43_ConvertConversionWorkspaceRequestOut",
        "DatabaseTypeIn": "_datamigration_44_DatabaseTypeIn",
        "DatabaseTypeOut": "_datamigration_45_DatabaseTypeOut",
        "MachineConfigIn": "_datamigration_46_MachineConfigIn",
        "MachineConfigOut": "_datamigration_47_MachineConfigOut",
        "CommitConversionWorkspaceRequestIn": "_datamigration_48_CommitConversionWorkspaceRequestIn",
        "CommitConversionWorkspaceRequestOut": "_datamigration_49_CommitConversionWorkspaceRequestOut",
        "ConversionWorkspaceIn": "_datamigration_50_ConversionWorkspaceIn",
        "ConversionWorkspaceOut": "_datamigration_51_ConversionWorkspaceOut",
        "ImportRulesJobDetailsIn": "_datamigration_52_ImportRulesJobDetailsIn",
        "ImportRulesJobDetailsOut": "_datamigration_53_ImportRulesJobDetailsOut",
        "RollbackConversionWorkspaceRequestIn": "_datamigration_54_RollbackConversionWorkspaceRequestIn",
        "RollbackConversionWorkspaceRequestOut": "_datamigration_55_RollbackConversionWorkspaceRequestOut",
        "SeedConversionWorkspaceRequestIn": "_datamigration_56_SeedConversionWorkspaceRequestIn",
        "SeedConversionWorkspaceRequestOut": "_datamigration_57_SeedConversionWorkspaceRequestOut",
        "FunctionEntityIn": "_datamigration_58_FunctionEntityIn",
        "FunctionEntityOut": "_datamigration_59_FunctionEntityOut",
        "EntityMappingLogEntryIn": "_datamigration_60_EntityMappingLogEntryIn",
        "EntityMappingLogEntryOut": "_datamigration_61_EntityMappingLogEntryOut",
        "StartMigrationJobRequestIn": "_datamigration_62_StartMigrationJobRequestIn",
        "StartMigrationJobRequestOut": "_datamigration_63_StartMigrationJobRequestOut",
        "TestIamPermissionsResponseIn": "_datamigration_64_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_datamigration_65_TestIamPermissionsResponseOut",
        "TestIamPermissionsRequestIn": "_datamigration_66_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_datamigration_67_TestIamPermissionsRequestOut",
        "ImportMappingRulesRequestIn": "_datamigration_68_ImportMappingRulesRequestIn",
        "ImportMappingRulesRequestOut": "_datamigration_69_ImportMappingRulesRequestOut",
        "DatabaseEntityIn": "_datamigration_70_DatabaseEntityIn",
        "DatabaseEntityOut": "_datamigration_71_DatabaseEntityOut",
        "IndexEntityIn": "_datamigration_72_IndexEntityIn",
        "IndexEntityOut": "_datamigration_73_IndexEntityOut",
        "ViewEntityIn": "_datamigration_74_ViewEntityIn",
        "ViewEntityOut": "_datamigration_75_ViewEntityOut",
        "ListPrivateConnectionsResponseIn": "_datamigration_76_ListPrivateConnectionsResponseIn",
        "ListPrivateConnectionsResponseOut": "_datamigration_77_ListPrivateConnectionsResponseOut",
        "ListConnectionProfilesResponseIn": "_datamigration_78_ListConnectionProfilesResponseIn",
        "ListConnectionProfilesResponseOut": "_datamigration_79_ListConnectionProfilesResponseOut",
        "AuditLogConfigIn": "_datamigration_80_AuditLogConfigIn",
        "AuditLogConfigOut": "_datamigration_81_AuditLogConfigOut",
        "ConversionWorkspaceInfoIn": "_datamigration_82_ConversionWorkspaceInfoIn",
        "ConversionWorkspaceInfoOut": "_datamigration_83_ConversionWorkspaceInfoOut",
        "AlloyDbConnectionProfileIn": "_datamigration_84_AlloyDbConnectionProfileIn",
        "AlloyDbConnectionProfileOut": "_datamigration_85_AlloyDbConnectionProfileOut",
        "TriggerEntityIn": "_datamigration_86_TriggerEntityIn",
        "TriggerEntityOut": "_datamigration_87_TriggerEntityOut",
        "PrivateServiceConnectConnectivityIn": "_datamigration_88_PrivateServiceConnectConnectivityIn",
        "PrivateServiceConnectConnectivityOut": "_datamigration_89_PrivateServiceConnectConnectivityOut",
        "CloudSqlSettingsIn": "_datamigration_90_CloudSqlSettingsIn",
        "CloudSqlSettingsOut": "_datamigration_91_CloudSqlSettingsOut",
        "SearchBackgroundJobsResponseIn": "_datamigration_92_SearchBackgroundJobsResponseIn",
        "SearchBackgroundJobsResponseOut": "_datamigration_93_SearchBackgroundJobsResponseOut",
        "TableEntityIn": "_datamigration_94_TableEntityIn",
        "TableEntityOut": "_datamigration_95_TableEntityOut",
        "ListLocationsResponseIn": "_datamigration_96_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_datamigration_97_ListLocationsResponseOut",
        "StopMigrationJobRequestIn": "_datamigration_98_StopMigrationJobRequestIn",
        "StopMigrationJobRequestOut": "_datamigration_99_StopMigrationJobRequestOut",
        "SqlIpConfigIn": "_datamigration_100_SqlIpConfigIn",
        "SqlIpConfigOut": "_datamigration_101_SqlIpConfigOut",
        "VpcPeeringConnectivityIn": "_datamigration_102_VpcPeeringConnectivityIn",
        "VpcPeeringConnectivityOut": "_datamigration_103_VpcPeeringConnectivityOut",
        "ListMigrationJobsResponseIn": "_datamigration_104_ListMigrationJobsResponseIn",
        "ListMigrationJobsResponseOut": "_datamigration_105_ListMigrationJobsResponseOut",
        "SetIamPolicyRequestIn": "_datamigration_106_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_datamigration_107_SetIamPolicyRequestOut",
        "GoogleCloudClouddmsV1OperationMetadataIn": "_datamigration_108_GoogleCloudClouddmsV1OperationMetadataIn",
        "GoogleCloudClouddmsV1OperationMetadataOut": "_datamigration_109_GoogleCloudClouddmsV1OperationMetadataOut",
        "VmCreationConfigIn": "_datamigration_110_VmCreationConfigIn",
        "VmCreationConfigOut": "_datamigration_111_VmCreationConfigOut",
        "PrivateConnectivityIn": "_datamigration_112_PrivateConnectivityIn",
        "PrivateConnectivityOut": "_datamigration_113_PrivateConnectivityOut",
        "EncryptionConfigIn": "_datamigration_114_EncryptionConfigIn",
        "EncryptionConfigOut": "_datamigration_115_EncryptionConfigOut",
        "VpcPeeringConfigIn": "_datamigration_116_VpcPeeringConfigIn",
        "VpcPeeringConfigOut": "_datamigration_117_VpcPeeringConfigOut",
        "DatabaseEngineInfoIn": "_datamigration_118_DatabaseEngineInfoIn",
        "DatabaseEngineInfoOut": "_datamigration_119_DatabaseEngineInfoOut",
        "PromoteMigrationJobRequestIn": "_datamigration_120_PromoteMigrationJobRequestIn",
        "PromoteMigrationJobRequestOut": "_datamigration_121_PromoteMigrationJobRequestOut",
        "CloudSqlConnectionProfileIn": "_datamigration_122_CloudSqlConnectionProfileIn",
        "CloudSqlConnectionProfileOut": "_datamigration_123_CloudSqlConnectionProfileOut",
        "SchemaEntityIn": "_datamigration_124_SchemaEntityIn",
        "SchemaEntityOut": "_datamigration_125_SchemaEntityOut",
        "UserPasswordIn": "_datamigration_126_UserPasswordIn",
        "UserPasswordOut": "_datamigration_127_UserPasswordOut",
        "ConstraintEntityIn": "_datamigration_128_ConstraintEntityIn",
        "ConstraintEntityOut": "_datamigration_129_ConstraintEntityOut",
        "SequenceEntityIn": "_datamigration_130_SequenceEntityIn",
        "SequenceEntityOut": "_datamigration_131_SequenceEntityOut",
        "LocationIn": "_datamigration_132_LocationIn",
        "LocationOut": "_datamigration_133_LocationOut",
        "StatusIn": "_datamigration_134_StatusIn",
        "StatusOut": "_datamigration_135_StatusOut",
        "ConvertJobDetailsIn": "_datamigration_136_ConvertJobDetailsIn",
        "ConvertJobDetailsOut": "_datamigration_137_ConvertJobDetailsOut",
        "PostgreSqlConnectionProfileIn": "_datamigration_138_PostgreSqlConnectionProfileIn",
        "PostgreSqlConnectionProfileOut": "_datamigration_139_PostgreSqlConnectionProfileOut",
        "EntityMappingIn": "_datamigration_140_EntityMappingIn",
        "EntityMappingOut": "_datamigration_141_EntityMappingOut",
        "StaticServiceIpConnectivityIn": "_datamigration_142_StaticServiceIpConnectivityIn",
        "StaticServiceIpConnectivityOut": "_datamigration_143_StaticServiceIpConnectivityOut",
        "VmSelectionConfigIn": "_datamigration_144_VmSelectionConfigIn",
        "VmSelectionConfigOut": "_datamigration_145_VmSelectionConfigOut",
        "MigrationJobIn": "_datamigration_146_MigrationJobIn",
        "MigrationJobOut": "_datamigration_147_MigrationJobOut",
        "VerifyMigrationJobRequestIn": "_datamigration_148_VerifyMigrationJobRequestIn",
        "VerifyMigrationJobRequestOut": "_datamigration_149_VerifyMigrationJobRequestOut",
        "SslConfigIn": "_datamigration_150_SslConfigIn",
        "SslConfigOut": "_datamigration_151_SslConfigOut",
        "StaticIpConnectivityIn": "_datamigration_152_StaticIpConnectivityIn",
        "StaticIpConnectivityOut": "_datamigration_153_StaticIpConnectivityOut",
        "PackageEntityIn": "_datamigration_154_PackageEntityIn",
        "PackageEntityOut": "_datamigration_155_PackageEntityOut",
        "ListOperationsResponseIn": "_datamigration_156_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_datamigration_157_ListOperationsResponseOut",
        "PolicyIn": "_datamigration_158_PolicyIn",
        "PolicyOut": "_datamigration_159_PolicyOut",
        "OperationIn": "_datamigration_160_OperationIn",
        "OperationOut": "_datamigration_161_OperationOut",
        "SqlAclEntryIn": "_datamigration_162_SqlAclEntryIn",
        "SqlAclEntryOut": "_datamigration_163_SqlAclEntryOut",
        "ApplyConversionWorkspaceRequestIn": "_datamigration_164_ApplyConversionWorkspaceRequestIn",
        "ApplyConversionWorkspaceRequestOut": "_datamigration_165_ApplyConversionWorkspaceRequestOut",
        "MigrationJobVerificationErrorIn": "_datamigration_166_MigrationJobVerificationErrorIn",
        "MigrationJobVerificationErrorOut": "_datamigration_167_MigrationJobVerificationErrorOut",
        "ApplyJobDetailsIn": "_datamigration_168_ApplyJobDetailsIn",
        "ApplyJobDetailsOut": "_datamigration_169_ApplyJobDetailsOut",
        "ListConversionWorkspacesResponseIn": "_datamigration_170_ListConversionWorkspacesResponseIn",
        "ListConversionWorkspacesResponseOut": "_datamigration_171_ListConversionWorkspacesResponseOut",
        "MySqlConnectionProfileIn": "_datamigration_172_MySqlConnectionProfileIn",
        "MySqlConnectionProfileOut": "_datamigration_173_MySqlConnectionProfileOut",
        "StoredProcedureEntityIn": "_datamigration_174_StoredProcedureEntityIn",
        "StoredProcedureEntityOut": "_datamigration_175_StoredProcedureEntityOut",
        "FetchStaticIpsResponseIn": "_datamigration_176_FetchStaticIpsResponseIn",
        "FetchStaticIpsResponseOut": "_datamigration_177_FetchStaticIpsResponseOut",
        "AuditConfigIn": "_datamigration_178_AuditConfigIn",
        "AuditConfigOut": "_datamigration_179_AuditConfigOut",
        "RulesFileIn": "_datamigration_180_RulesFileIn",
        "RulesFileOut": "_datamigration_181_RulesFileOut",
        "DescribeConversionWorkspaceRevisionsResponseIn": "_datamigration_182_DescribeConversionWorkspaceRevisionsResponseIn",
        "DescribeConversionWorkspaceRevisionsResponseOut": "_datamigration_183_DescribeConversionWorkspaceRevisionsResponseOut",
        "CancelOperationRequestIn": "_datamigration_184_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_datamigration_185_CancelOperationRequestOut",
        "SshScriptIn": "_datamigration_186_SshScriptIn",
        "SshScriptOut": "_datamigration_187_SshScriptOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["BackgroundJobLogEntryIn"] = t.struct(
        {
            "importRulesJobDetails": t.proxy(
                renames["ImportRulesJobDetailsIn"]
            ).optional(),
            "convertJobDetails": t.proxy(renames["ConvertJobDetailsIn"]).optional(),
            "completionState": t.string().optional(),
            "completionComment": t.string().optional(),
            "finishTime": t.string().optional(),
            "startTime": t.string().optional(),
            "id": t.string().optional(),
            "applyJobDetails": t.proxy(renames["ApplyJobDetailsIn"]).optional(),
            "seedJobDetails": t.proxy(renames["SeedJobDetailsIn"]).optional(),
            "requestAutocommit": t.boolean().optional(),
            "jobType": t.string().optional(),
        }
    ).named(renames["BackgroundJobLogEntryIn"])
    types["BackgroundJobLogEntryOut"] = t.struct(
        {
            "importRulesJobDetails": t.proxy(
                renames["ImportRulesJobDetailsOut"]
            ).optional(),
            "convertJobDetails": t.proxy(renames["ConvertJobDetailsOut"]).optional(),
            "completionState": t.string().optional(),
            "completionComment": t.string().optional(),
            "finishTime": t.string().optional(),
            "startTime": t.string().optional(),
            "id": t.string().optional(),
            "applyJobDetails": t.proxy(renames["ApplyJobDetailsOut"]).optional(),
            "seedJobDetails": t.proxy(renames["SeedJobDetailsOut"]).optional(),
            "requestAutocommit": t.boolean().optional(),
            "jobType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackgroundJobLogEntryOut"])
    types["SeedJobDetailsIn"] = t.struct(
        {"connectionProfile": t.string().optional()}
    ).named(renames["SeedJobDetailsIn"])
    types["SeedJobDetailsOut"] = t.struct(
        {
            "connectionProfile": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SeedJobDetailsOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["ColumnEntityIn"] = t.struct(
        {
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "fractionalSecondsPrecision": t.integer().optional(),
            "comment": t.string().optional(),
            "dataType": t.string().optional(),
            "length": t.string().optional(),
            "defaultValue": t.string().optional(),
            "array": t.boolean().optional(),
            "setValues": t.array(t.string()).optional(),
            "collation": t.string().optional(),
            "arrayLength": t.integer().optional(),
            "precision": t.integer().optional(),
            "charset": t.string().optional(),
            "scale": t.integer().optional(),
            "autoGenerated": t.boolean().optional(),
            "ordinalPosition": t.integer().optional(),
            "nullable": t.boolean().optional(),
            "udt": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ColumnEntityIn"])
    types["ColumnEntityOut"] = t.struct(
        {
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "fractionalSecondsPrecision": t.integer().optional(),
            "comment": t.string().optional(),
            "dataType": t.string().optional(),
            "length": t.string().optional(),
            "defaultValue": t.string().optional(),
            "array": t.boolean().optional(),
            "setValues": t.array(t.string()).optional(),
            "collation": t.string().optional(),
            "arrayLength": t.integer().optional(),
            "precision": t.integer().optional(),
            "charset": t.string().optional(),
            "scale": t.integer().optional(),
            "autoGenerated": t.boolean().optional(),
            "ordinalPosition": t.integer().optional(),
            "nullable": t.boolean().optional(),
            "udt": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColumnEntityOut"])
    types["ResumeMigrationJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResumeMigrationJobRequestIn"]
    )
    types["ResumeMigrationJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumeMigrationJobRequestOut"])
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
    types["ReverseSshConnectivityIn"] = t.struct(
        {
            "vmPort": t.integer(),
            "vpc": t.string().optional(),
            "vm": t.string().optional(),
            "vmIp": t.string(),
        }
    ).named(renames["ReverseSshConnectivityIn"])
    types["ReverseSshConnectivityOut"] = t.struct(
        {
            "vmPort": t.integer(),
            "vpc": t.string().optional(),
            "vm": t.string().optional(),
            "vmIp": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReverseSshConnectivityOut"])
    types["RestartMigrationJobRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RestartMigrationJobRequestIn"])
    types["RestartMigrationJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RestartMigrationJobRequestOut"])
    types["PrivateConnectionIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "vpcPeeringConfig": t.proxy(renames["VpcPeeringConfigIn"]).optional(),
        }
    ).named(renames["PrivateConnectionIn"])
    types["PrivateConnectionOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "vpcPeeringConfig": t.proxy(renames["VpcPeeringConfigOut"]).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["PrivateConnectionOut"])
    types["DumpFlagsIn"] = t.struct(
        {"dumpFlags": t.array(t.proxy(renames["DumpFlagIn"])).optional()}
    ).named(renames["DumpFlagsIn"])
    types["DumpFlagsOut"] = t.struct(
        {
            "dumpFlags": t.array(t.proxy(renames["DumpFlagOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DumpFlagsOut"])
    types["DescribeDatabaseEntitiesResponseIn"] = t.struct(
        {
            "databaseEntities": t.array(
                t.proxy(renames["DatabaseEntityIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["DescribeDatabaseEntitiesResponseIn"])
    types["DescribeDatabaseEntitiesResponseOut"] = t.struct(
        {
            "databaseEntities": t.array(
                t.proxy(renames["DatabaseEntityOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DescribeDatabaseEntitiesResponseOut"])
    types["AlloyDbSettingsIn"] = t.struct(
        {
            "primaryInstanceSettings": t.proxy(renames["PrimaryInstanceSettingsIn"]),
            "initialUser": t.proxy(renames["UserPasswordIn"]),
            "encryptionConfig": t.proxy(renames["EncryptionConfigIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "vpcNetwork": t.string(),
        }
    ).named(renames["AlloyDbSettingsIn"])
    types["AlloyDbSettingsOut"] = t.struct(
        {
            "primaryInstanceSettings": t.proxy(renames["PrimaryInstanceSettingsOut"]),
            "initialUser": t.proxy(renames["UserPasswordOut"]),
            "encryptionConfig": t.proxy(renames["EncryptionConfigOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "vpcNetwork": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlloyDbSettingsOut"])
    types["GenerateSshScriptRequestIn"] = t.struct(
        {
            "vmPort": t.integer().optional(),
            "vm": t.string(),
            "vmCreationConfig": t.proxy(renames["VmCreationConfigIn"]).optional(),
            "vmSelectionConfig": t.proxy(renames["VmSelectionConfigIn"]).optional(),
        }
    ).named(renames["GenerateSshScriptRequestIn"])
    types["GenerateSshScriptRequestOut"] = t.struct(
        {
            "vmPort": t.integer().optional(),
            "vm": t.string(),
            "vmCreationConfig": t.proxy(renames["VmCreationConfigOut"]).optional(),
            "vmSelectionConfig": t.proxy(renames["VmSelectionConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateSshScriptRequestOut"])
    types["ForwardSshTunnelConnectivityIn"] = t.struct(
        {
            "password": t.string().optional(),
            "hostname": t.string(),
            "username": t.string(),
            "port": t.integer().optional(),
            "privateKey": t.string().optional(),
        }
    ).named(renames["ForwardSshTunnelConnectivityIn"])
    types["ForwardSshTunnelConnectivityOut"] = t.struct(
        {
            "password": t.string().optional(),
            "hostname": t.string(),
            "username": t.string(),
            "port": t.integer().optional(),
            "privateKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ForwardSshTunnelConnectivityOut"])
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
    types["OracleConnectionProfileIn"] = t.struct(
        {
            "username": t.string(),
            "password": t.string(),
            "port": t.integer(),
            "host": t.string(),
            "staticServiceIpConnectivity": t.proxy(
                renames["StaticServiceIpConnectivityIn"]
            ).optional(),
            "forwardSshConnectivity": t.proxy(
                renames["ForwardSshTunnelConnectivityIn"]
            ).optional(),
            "databaseService": t.string(),
            "privateConnectivity": t.proxy(renames["PrivateConnectivityIn"]).optional(),
        }
    ).named(renames["OracleConnectionProfileIn"])
    types["OracleConnectionProfileOut"] = t.struct(
        {
            "username": t.string(),
            "password": t.string(),
            "port": t.integer(),
            "passwordSet": t.boolean().optional(),
            "host": t.string(),
            "staticServiceIpConnectivity": t.proxy(
                renames["StaticServiceIpConnectivityOut"]
            ).optional(),
            "forwardSshConnectivity": t.proxy(
                renames["ForwardSshTunnelConnectivityOut"]
            ).optional(),
            "databaseService": t.string(),
            "privateConnectivity": t.proxy(
                renames["PrivateConnectivityOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OracleConnectionProfileOut"])
    types["PrimaryInstanceSettingsIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "machineConfig": t.proxy(renames["MachineConfigIn"]).optional(),
            "id": t.string(),
            "databaseFlags": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PrimaryInstanceSettingsIn"])
    types["PrimaryInstanceSettingsOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "machineConfig": t.proxy(renames["MachineConfigOut"]).optional(),
            "id": t.string(),
            "privateIp": t.string().optional(),
            "databaseFlags": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrimaryInstanceSettingsOut"])
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["ConnectionProfileIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "provider": t.string().optional(),
            "postgresql": t.proxy(renames["PostgreSqlConnectionProfileIn"]).optional(),
            "state": t.string().optional(),
            "cloudsql": t.proxy(renames["CloudSqlConnectionProfileIn"]).optional(),
            "mysql": t.proxy(renames["MySqlConnectionProfileIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "oracle": t.proxy(renames["OracleConnectionProfileIn"]).optional(),
            "alloydb": t.proxy(renames["AlloyDbConnectionProfileIn"]).optional(),
        }
    ).named(renames["ConnectionProfileIn"])
    types["ConnectionProfileOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "provider": t.string().optional(),
            "postgresql": t.proxy(renames["PostgreSqlConnectionProfileOut"]).optional(),
            "state": t.string().optional(),
            "cloudsql": t.proxy(renames["CloudSqlConnectionProfileOut"]).optional(),
            "mysql": t.proxy(renames["MySqlConnectionProfileOut"]).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "oracle": t.proxy(renames["OracleConnectionProfileOut"]).optional(),
            "alloydb": t.proxy(renames["AlloyDbConnectionProfileOut"]).optional(),
        }
    ).named(renames["ConnectionProfileOut"])
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
    types["DatabaseTypeIn"] = t.struct(
        {"provider": t.string().optional(), "engine": t.string().optional()}
    ).named(renames["DatabaseTypeIn"])
    types["DatabaseTypeOut"] = t.struct(
        {
            "provider": t.string().optional(),
            "engine": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseTypeOut"])
    types["MachineConfigIn"] = t.struct({"cpuCount": t.integer().optional()}).named(
        renames["MachineConfigIn"]
    )
    types["MachineConfigOut"] = t.struct(
        {
            "cpuCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MachineConfigOut"])
    types["CommitConversionWorkspaceRequestIn"] = t.struct(
        {"commitName": t.string().optional()}
    ).named(renames["CommitConversionWorkspaceRequestIn"])
    types["CommitConversionWorkspaceRequestOut"] = t.struct(
        {
            "commitName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitConversionWorkspaceRequestOut"])
    types["ConversionWorkspaceIn"] = t.struct(
        {
            "globalSettings": t.struct({"_": t.string().optional()}).optional(),
            "destination": t.proxy(renames["DatabaseEngineInfoIn"]),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "source": t.proxy(renames["DatabaseEngineInfoIn"]),
        }
    ).named(renames["ConversionWorkspaceIn"])
    types["ConversionWorkspaceOut"] = t.struct(
        {
            "globalSettings": t.struct({"_": t.string().optional()}).optional(),
            "destination": t.proxy(renames["DatabaseEngineInfoOut"]),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "latestCommitId": t.string().optional(),
            "hasUncommittedChanges": t.boolean().optional(),
            "displayName": t.string().optional(),
            "source": t.proxy(renames["DatabaseEngineInfoOut"]),
            "createTime": t.string().optional(),
            "latestCommitTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConversionWorkspaceOut"])
    types["ImportRulesJobDetailsIn"] = t.struct(
        {"fileFormat": t.string().optional(), "files": t.array(t.string()).optional()}
    ).named(renames["ImportRulesJobDetailsIn"])
    types["ImportRulesJobDetailsOut"] = t.struct(
        {
            "fileFormat": t.string().optional(),
            "files": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportRulesJobDetailsOut"])
    types["RollbackConversionWorkspaceRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RollbackConversionWorkspaceRequestIn"])
    types["RollbackConversionWorkspaceRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RollbackConversionWorkspaceRequestOut"])
    types["SeedConversionWorkspaceRequestIn"] = t.struct(
        {
            "autoCommit": t.boolean().optional(),
            "destinationConnectionProfile": t.string().optional(),
            "sourceConnectionProfile": t.string().optional(),
        }
    ).named(renames["SeedConversionWorkspaceRequestIn"])
    types["SeedConversionWorkspaceRequestOut"] = t.struct(
        {
            "autoCommit": t.boolean().optional(),
            "destinationConnectionProfile": t.string().optional(),
            "sourceConnectionProfile": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SeedConversionWorkspaceRequestOut"])
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
    types["StartMigrationJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StartMigrationJobRequestIn"]
    )
    types["StartMigrationJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StartMigrationJobRequestOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["DatabaseEntityIn"] = t.struct(
        {
            "table": t.proxy(renames["TableEntityIn"]).optional(),
            "view": t.proxy(renames["ViewEntityIn"]).optional(),
            "storedProcedure": t.proxy(renames["StoredProcedureEntityIn"]).optional(),
            "sequence": t.proxy(renames["SequenceEntityIn"]).optional(),
            "shortName": t.string().optional(),
            "mappings": t.array(t.proxy(renames["EntityMappingIn"])).optional(),
            "databaseFunction": t.proxy(renames["FunctionEntityIn"]).optional(),
            "schema": t.proxy(renames["SchemaEntityIn"]).optional(),
            "parentEntity": t.string().optional(),
            "databasePackage": t.proxy(renames["PackageEntityIn"]).optional(),
            "tree": t.string().optional(),
            "entityType": t.string().optional(),
            "synonym": t.proxy(renames["SynonymEntityIn"]).optional(),
        }
    ).named(renames["DatabaseEntityIn"])
    types["DatabaseEntityOut"] = t.struct(
        {
            "table": t.proxy(renames["TableEntityOut"]).optional(),
            "view": t.proxy(renames["ViewEntityOut"]).optional(),
            "storedProcedure": t.proxy(renames["StoredProcedureEntityOut"]).optional(),
            "sequence": t.proxy(renames["SequenceEntityOut"]).optional(),
            "shortName": t.string().optional(),
            "mappings": t.array(t.proxy(renames["EntityMappingOut"])).optional(),
            "databaseFunction": t.proxy(renames["FunctionEntityOut"]).optional(),
            "schema": t.proxy(renames["SchemaEntityOut"]).optional(),
            "parentEntity": t.string().optional(),
            "databasePackage": t.proxy(renames["PackageEntityOut"]).optional(),
            "tree": t.string().optional(),
            "entityType": t.string().optional(),
            "synonym": t.proxy(renames["SynonymEntityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseEntityOut"])
    types["IndexEntityIn"] = t.struct(
        {
            "unique": t.boolean().optional(),
            "tableColumns": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["IndexEntityIn"])
    types["IndexEntityOut"] = t.struct(
        {
            "unique": t.boolean().optional(),
            "tableColumns": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexEntityOut"])
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
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "privateConnections": t.array(
                t.proxy(renames["PrivateConnectionIn"])
            ).optional(),
        }
    ).named(renames["ListPrivateConnectionsResponseIn"])
    types["ListPrivateConnectionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "privateConnections": t.array(
                t.proxy(renames["PrivateConnectionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPrivateConnectionsResponseOut"])
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
    types["TriggerEntityIn"] = t.struct(
        {
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "triggerType": t.string().optional(),
            "triggeringEvents": t.array(t.string()).optional(),
            "sqlCode": t.string().optional(),
        }
    ).named(renames["TriggerEntityIn"])
    types["TriggerEntityOut"] = t.struct(
        {
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "triggerType": t.string().optional(),
            "triggeringEvents": t.array(t.string()).optional(),
            "sqlCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TriggerEntityOut"])
    types["PrivateServiceConnectConnectivityIn"] = t.struct(
        {"serviceAttachment": t.string()}
    ).named(renames["PrivateServiceConnectConnectivityIn"])
    types["PrivateServiceConnectConnectivityOut"] = t.struct(
        {
            "serviceAttachment": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateServiceConnectConnectivityOut"])
    types["CloudSqlSettingsIn"] = t.struct(
        {
            "sourceId": t.string().optional(),
            "rootPassword": t.string().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "zone": t.string().optional(),
            "secondaryZone": t.string().optional(),
            "collation": t.string().optional(),
            "cmekKeyName": t.string().optional(),
            "databaseVersion": t.string().optional(),
            "tier": t.string().optional(),
            "availabilityType": t.string().optional(),
            "ipConfig": t.proxy(renames["SqlIpConfigIn"]).optional(),
            "activationPolicy": t.string().optional(),
            "storageAutoResizeLimit": t.string().optional(),
            "autoStorageIncrease": t.boolean().optional(),
            "databaseFlags": t.struct({"_": t.string().optional()}).optional(),
            "dataDiskSizeGb": t.string().optional(),
            "dataDiskType": t.string().optional(),
        }
    ).named(renames["CloudSqlSettingsIn"])
    types["CloudSqlSettingsOut"] = t.struct(
        {
            "sourceId": t.string().optional(),
            "rootPassword": t.string().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "zone": t.string().optional(),
            "secondaryZone": t.string().optional(),
            "collation": t.string().optional(),
            "cmekKeyName": t.string().optional(),
            "databaseVersion": t.string().optional(),
            "tier": t.string().optional(),
            "availabilityType": t.string().optional(),
            "ipConfig": t.proxy(renames["SqlIpConfigOut"]).optional(),
            "activationPolicy": t.string().optional(),
            "storageAutoResizeLimit": t.string().optional(),
            "autoStorageIncrease": t.boolean().optional(),
            "databaseFlags": t.struct({"_": t.string().optional()}).optional(),
            "rootPasswordSet": t.boolean().optional(),
            "dataDiskSizeGb": t.string().optional(),
            "dataDiskType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudSqlSettingsOut"])
    types["SearchBackgroundJobsResponseIn"] = t.struct(
        {"jobs": t.array(t.proxy(renames["BackgroundJobLogEntryIn"])).optional()}
    ).named(renames["SearchBackgroundJobsResponseIn"])
    types["SearchBackgroundJobsResponseOut"] = t.struct(
        {
            "jobs": t.array(t.proxy(renames["BackgroundJobLogEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchBackgroundJobsResponseOut"])
    types["TableEntityIn"] = t.struct(
        {
            "constraints": t.array(t.proxy(renames["ConstraintEntityIn"])).optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "columns": t.array(t.proxy(renames["ColumnEntityIn"])).optional(),
            "triggers": t.array(t.proxy(renames["TriggerEntityIn"])).optional(),
            "comment": t.string().optional(),
            "indices": t.array(t.proxy(renames["IndexEntityIn"])).optional(),
        }
    ).named(renames["TableEntityIn"])
    types["TableEntityOut"] = t.struct(
        {
            "constraints": t.array(t.proxy(renames["ConstraintEntityOut"])).optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "columns": t.array(t.proxy(renames["ColumnEntityOut"])).optional(),
            "triggers": t.array(t.proxy(renames["TriggerEntityOut"])).optional(),
            "comment": t.string().optional(),
            "indices": t.array(t.proxy(renames["IndexEntityOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableEntityOut"])
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
    types["StopMigrationJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StopMigrationJobRequestIn"]
    )
    types["StopMigrationJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StopMigrationJobRequestOut"])
    types["SqlIpConfigIn"] = t.struct(
        {
            "enableIpv4": t.boolean().optional(),
            "requireSsl": t.boolean().optional(),
            "privateNetwork": t.string().optional(),
            "authorizedNetworks": t.array(t.proxy(renames["SqlAclEntryIn"])).optional(),
            "allocatedIpRange": t.string().optional(),
        }
    ).named(renames["SqlIpConfigIn"])
    types["SqlIpConfigOut"] = t.struct(
        {
            "enableIpv4": t.boolean().optional(),
            "requireSsl": t.boolean().optional(),
            "privateNetwork": t.string().optional(),
            "authorizedNetworks": t.array(
                t.proxy(renames["SqlAclEntryOut"])
            ).optional(),
            "allocatedIpRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlIpConfigOut"])
    types["VpcPeeringConnectivityIn"] = t.struct({"vpc": t.string().optional()}).named(
        renames["VpcPeeringConnectivityIn"]
    )
    types["VpcPeeringConnectivityOut"] = t.struct(
        {
            "vpc": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VpcPeeringConnectivityOut"])
    types["ListMigrationJobsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "migrationJobs": t.array(t.proxy(renames["MigrationJobIn"])).optional(),
        }
    ).named(renames["ListMigrationJobsResponseIn"])
    types["ListMigrationJobsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "migrationJobs": t.array(t.proxy(renames["MigrationJobOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMigrationJobsResponseOut"])
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
    types["GoogleCloudClouddmsV1OperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudClouddmsV1OperationMetadataIn"])
    types["GoogleCloudClouddmsV1OperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "statusMessage": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudClouddmsV1OperationMetadataOut"])
    types["VmCreationConfigIn"] = t.struct(
        {
            "vmZone": t.string().optional(),
            "vmMachineType": t.string(),
            "subnet": t.string().optional(),
        }
    ).named(renames["VmCreationConfigIn"])
    types["VmCreationConfigOut"] = t.struct(
        {
            "vmZone": t.string().optional(),
            "vmMachineType": t.string(),
            "subnet": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmCreationConfigOut"])
    types["PrivateConnectivityIn"] = t.struct({"privateConnection": t.string()}).named(
        renames["PrivateConnectivityIn"]
    )
    types["PrivateConnectivityOut"] = t.struct(
        {
            "privateConnection": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateConnectivityOut"])
    types["EncryptionConfigIn"] = t.struct({"kmsKeyName": t.string().optional()}).named(
        renames["EncryptionConfigIn"]
    )
    types["EncryptionConfigOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionConfigOut"])
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
    types["DatabaseEngineInfoIn"] = t.struct(
        {"version": t.string(), "engine": t.string()}
    ).named(renames["DatabaseEngineInfoIn"])
    types["DatabaseEngineInfoOut"] = t.struct(
        {
            "version": t.string(),
            "engine": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseEngineInfoOut"])
    types["PromoteMigrationJobRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["PromoteMigrationJobRequestIn"])
    types["PromoteMigrationJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PromoteMigrationJobRequestOut"])
    types["CloudSqlConnectionProfileIn"] = t.struct(
        {"settings": t.proxy(renames["CloudSqlSettingsIn"]).optional()}
    ).named(renames["CloudSqlConnectionProfileIn"])
    types["CloudSqlConnectionProfileOut"] = t.struct(
        {
            "privateIp": t.string().optional(),
            "publicIp": t.string().optional(),
            "settings": t.proxy(renames["CloudSqlSettingsOut"]).optional(),
            "additionalPublicIp": t.string().optional(),
            "cloudSqlId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudSqlConnectionProfileOut"])
    types["SchemaEntityIn"] = t.struct(
        {"customFeatures": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["SchemaEntityIn"])
    types["SchemaEntityOut"] = t.struct(
        {
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaEntityOut"])
    types["UserPasswordIn"] = t.struct(
        {"user": t.string().optional(), "password": t.string().optional()}
    ).named(renames["UserPasswordIn"])
    types["UserPasswordOut"] = t.struct(
        {
            "user": t.string().optional(),
            "password": t.string().optional(),
            "passwordSet": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserPasswordOut"])
    types["ConstraintEntityIn"] = t.struct(
        {
            "type": t.string().optional(),
            "tableColumns": t.array(t.string()).optional(),
            "tableName": t.string().optional(),
            "referenceTable": t.string().optional(),
            "referenceColumns": t.array(t.string()).optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ConstraintEntityIn"])
    types["ConstraintEntityOut"] = t.struct(
        {
            "type": t.string().optional(),
            "tableColumns": t.array(t.string()).optional(),
            "tableName": t.string().optional(),
            "referenceTable": t.string().optional(),
            "referenceColumns": t.array(t.string()).optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConstraintEntityOut"])
    types["SequenceEntityIn"] = t.struct(
        {
            "cache": t.string().optional(),
            "minValue": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "cycle": t.boolean().optional(),
            "maxValue": t.string().optional(),
            "startValue": t.string().optional(),
            "increment": t.string().optional(),
        }
    ).named(renames["SequenceEntityIn"])
    types["SequenceEntityOut"] = t.struct(
        {
            "cache": t.string().optional(),
            "minValue": t.string().optional(),
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "cycle": t.boolean().optional(),
            "maxValue": t.string().optional(),
            "startValue": t.string().optional(),
            "increment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SequenceEntityOut"])
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["ConvertJobDetailsIn"] = t.struct({"filter": t.string().optional()}).named(
        renames["ConvertJobDetailsIn"]
    )
    types["ConvertJobDetailsOut"] = t.struct(
        {
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConvertJobDetailsOut"])
    types["PostgreSqlConnectionProfileIn"] = t.struct(
        {
            "port": t.integer(),
            "staticIpConnectivity": t.proxy(
                renames["StaticIpConnectivityIn"]
            ).optional(),
            "username": t.string(),
            "ssl": t.proxy(renames["SslConfigIn"]).optional(),
            "privateServiceConnectConnectivity": t.proxy(
                renames["PrivateServiceConnectConnectivityIn"]
            ).optional(),
            "password": t.string(),
            "host": t.string(),
            "cloudSqlId": t.string().optional(),
        }
    ).named(renames["PostgreSqlConnectionProfileIn"])
    types["PostgreSqlConnectionProfileOut"] = t.struct(
        {
            "port": t.integer(),
            "staticIpConnectivity": t.proxy(
                renames["StaticIpConnectivityOut"]
            ).optional(),
            "username": t.string(),
            "ssl": t.proxy(renames["SslConfigOut"]).optional(),
            "privateServiceConnectConnectivity": t.proxy(
                renames["PrivateServiceConnectConnectivityOut"]
            ).optional(),
            "networkArchitecture": t.string().optional(),
            "password": t.string(),
            "host": t.string(),
            "cloudSqlId": t.string().optional(),
            "passwordSet": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostgreSqlConnectionProfileOut"])
    types["EntityMappingIn"] = t.struct(
        {
            "draftType": t.string().optional(),
            "sourceType": t.string().optional(),
            "draftEntity": t.string().optional(),
            "sourceEntity": t.string().optional(),
            "mappingLog": t.array(
                t.proxy(renames["EntityMappingLogEntryIn"])
            ).optional(),
        }
    ).named(renames["EntityMappingIn"])
    types["EntityMappingOut"] = t.struct(
        {
            "draftType": t.string().optional(),
            "sourceType": t.string().optional(),
            "draftEntity": t.string().optional(),
            "sourceEntity": t.string().optional(),
            "mappingLog": t.array(
                t.proxy(renames["EntityMappingLogEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityMappingOut"])
    types["StaticServiceIpConnectivityIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["StaticServiceIpConnectivityIn"])
    types["StaticServiceIpConnectivityOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StaticServiceIpConnectivityOut"])
    types["VmSelectionConfigIn"] = t.struct({"vmZone": t.string()}).named(
        renames["VmSelectionConfigIn"]
    )
    types["VmSelectionConfigOut"] = t.struct(
        {"vmZone": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VmSelectionConfigOut"])
    types["MigrationJobIn"] = t.struct(
        {
            "staticIpConnectivity": t.proxy(
                renames["StaticIpConnectivityIn"]
            ).optional(),
            "dumpPath": t.string().optional(),
            "displayName": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "sourceDatabase": t.proxy(renames["DatabaseTypeIn"]).optional(),
            "reverseSshConnectivity": t.proxy(
                renames["ReverseSshConnectivityIn"]
            ).optional(),
            "vpcPeeringConnectivity": t.proxy(
                renames["VpcPeeringConnectivityIn"]
            ).optional(),
            "source": t.string(),
            "filter": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "conversionWorkspace": t.proxy(
                renames["ConversionWorkspaceInfoIn"]
            ).optional(),
            "destination": t.string(),
            "type": t.string(),
            "cmekKeyName": t.string().optional(),
            "dumpFlags": t.proxy(renames["DumpFlagsIn"]).optional(),
            "destinationDatabase": t.proxy(renames["DatabaseTypeIn"]).optional(),
        }
    ).named(renames["MigrationJobIn"])
    types["MigrationJobOut"] = t.struct(
        {
            "staticIpConnectivity": t.proxy(
                renames["StaticIpConnectivityOut"]
            ).optional(),
            "dumpPath": t.string().optional(),
            "displayName": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "sourceDatabase": t.proxy(renames["DatabaseTypeOut"]).optional(),
            "reverseSshConnectivity": t.proxy(
                renames["ReverseSshConnectivityOut"]
            ).optional(),
            "vpcPeeringConnectivity": t.proxy(
                renames["VpcPeeringConnectivityOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "source": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "filter": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "endTime": t.string().optional(),
            "conversionWorkspace": t.proxy(
                renames["ConversionWorkspaceInfoOut"]
            ).optional(),
            "duration": t.string().optional(),
            "destination": t.string(),
            "type": t.string(),
            "cmekKeyName": t.string().optional(),
            "dumpFlags": t.proxy(renames["DumpFlagsOut"]).optional(),
            "destinationDatabase": t.proxy(renames["DatabaseTypeOut"]).optional(),
            "phase": t.string().optional(),
        }
    ).named(renames["MigrationJobOut"])
    types["VerifyMigrationJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VerifyMigrationJobRequestIn"]
    )
    types["VerifyMigrationJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VerifyMigrationJobRequestOut"])
    types["SslConfigIn"] = t.struct(
        {
            "caCertificate": t.string(),
            "clientCertificate": t.string().optional(),
            "clientKey": t.string().optional(),
        }
    ).named(renames["SslConfigIn"])
    types["SslConfigOut"] = t.struct(
        {
            "type": t.string().optional(),
            "caCertificate": t.string(),
            "clientCertificate": t.string().optional(),
            "clientKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SslConfigOut"])
    types["StaticIpConnectivityIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StaticIpConnectivityIn"]
    )
    types["StaticIpConnectivityOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StaticIpConnectivityOut"])
    types["PackageEntityIn"] = t.struct(
        {
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "packageBody": t.string().optional(),
            "packageSqlCode": t.string().optional(),
        }
    ).named(renames["PackageEntityIn"])
    types["PackageEntityOut"] = t.struct(
        {
            "customFeatures": t.struct({"_": t.string().optional()}).optional(),
            "packageBody": t.string().optional(),
            "packageSqlCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageEntityOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["SqlAclEntryIn"] = t.struct(
        {
            "label": t.string().optional(),
            "expireTime": t.string().optional(),
            "value": t.string().optional(),
            "ttl": t.string().optional(),
        }
    ).named(renames["SqlAclEntryIn"])
    types["SqlAclEntryOut"] = t.struct(
        {
            "label": t.string().optional(),
            "expireTime": t.string().optional(),
            "value": t.string().optional(),
            "ttl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlAclEntryOut"])
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
    types["ListConversionWorkspacesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "conversionWorkspaces": t.array(
                t.proxy(renames["ConversionWorkspaceIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListConversionWorkspacesResponseIn"])
    types["ListConversionWorkspacesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "conversionWorkspaces": t.array(
                t.proxy(renames["ConversionWorkspaceOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConversionWorkspacesResponseOut"])
    types["MySqlConnectionProfileIn"] = t.struct(
        {
            "port": t.integer(),
            "cloudSqlId": t.string().optional(),
            "ssl": t.proxy(renames["SslConfigIn"]).optional(),
            "password": t.string(),
            "username": t.string(),
            "host": t.string(),
        }
    ).named(renames["MySqlConnectionProfileIn"])
    types["MySqlConnectionProfileOut"] = t.struct(
        {
            "passwordSet": t.boolean().optional(),
            "port": t.integer(),
            "cloudSqlId": t.string().optional(),
            "ssl": t.proxy(renames["SslConfigOut"]).optional(),
            "password": t.string(),
            "username": t.string(),
            "host": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MySqlConnectionProfileOut"])
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
    types["SshScriptIn"] = t.struct({"script": t.string().optional()}).named(
        renames["SshScriptIn"]
    )
    types["SshScriptOut"] = t.struct(
        {
            "script": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SshScriptOut"])

    functions = {}
    functions["projectsLocationsFetchStaticIps"] = datamigration.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = datamigration.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = datamigration.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsCreate"] = datamigration.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsPrivateConnectionsTestIamPermissions"
    ] = datamigration.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsDelete"] = datamigration.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsSetIamPolicy"] = datamigration.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsGet"] = datamigration.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsList"] = datamigration.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsGetIamPolicy"] = datamigration.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = datamigration.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMigrationJobsCreate"] = datamigration.delete(
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
    functions["projectsLocationsMigrationJobsGet"] = datamigration.delete(
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
    functions["projectsLocationsMigrationJobsGetIamPolicy"] = datamigration.delete(
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
    functions["projectsLocationsMigrationJobsVerify"] = datamigration.delete(
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
    functions["projectsLocationsMigrationJobsList"] = datamigration.delete(
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
    functions["projectsLocationsMigrationJobsPromote"] = datamigration.delete(
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
    functions["projectsLocationsMigrationJobsStop"] = datamigration.delete(
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
    functions["projectsLocationsMigrationJobsStart"] = datamigration.delete(
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
    functions["projectsLocationsMigrationJobsRestart"] = datamigration.delete(
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
    functions["projectsLocationsMigrationJobsPatch"] = datamigration.delete(
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
    functions["projectsLocationsMigrationJobsGenerateSshScript"] = datamigration.delete(
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
    functions["projectsLocationsMigrationJobsSetIamPolicy"] = datamigration.delete(
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
    functions["projectsLocationsMigrationJobsResume"] = datamigration.delete(
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
        "projectsLocationsMigrationJobsTestIamPermissions"
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
    functions["projectsLocationsMigrationJobsDelete"] = datamigration.delete(
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
    functions["projectsLocationsConversionWorkspacesCreate"] = datamigration.get(
        "v1/{conversionWorkspace}:describeConversionWorkspaceRevisions",
        t.struct(
            {
                "conversionWorkspace": t.string(),
                "commitId": t.string().optional(),
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
                "conversionWorkspace": t.string(),
                "commitId": t.string().optional(),
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
                "conversionWorkspace": t.string(),
                "commitId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DescribeConversionWorkspaceRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConversionWorkspacesSeed"] = datamigration.get(
        "v1/{conversionWorkspace}:describeConversionWorkspaceRevisions",
        t.struct(
            {
                "conversionWorkspace": t.string(),
                "commitId": t.string().optional(),
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
                "conversionWorkspace": t.string(),
                "commitId": t.string().optional(),
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
                "conversionWorkspace": t.string(),
                "commitId": t.string().optional(),
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
                "conversionWorkspace": t.string(),
                "commitId": t.string().optional(),
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
                "conversionWorkspace": t.string(),
                "commitId": t.string().optional(),
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
                "conversionWorkspace": t.string(),
                "commitId": t.string().optional(),
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
                "conversionWorkspace": t.string(),
                "commitId": t.string().optional(),
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
                "conversionWorkspace": t.string(),
                "commitId": t.string().optional(),
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
                "conversionWorkspace": t.string(),
                "commitId": t.string().optional(),
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
                "conversionWorkspace": t.string(),
                "commitId": t.string().optional(),
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
                "conversionWorkspace": t.string(),
                "commitId": t.string().optional(),
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
                "conversionWorkspace": t.string(),
                "commitId": t.string().optional(),
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
                "conversionWorkspace": t.string(),
                "commitId": t.string().optional(),
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
    functions[
        "projectsLocationsConnectionProfilesTestIamPermissions"
    ] = datamigration.get(
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
    functions["projectsLocationsConnectionProfilesCreate"] = datamigration.get(
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
