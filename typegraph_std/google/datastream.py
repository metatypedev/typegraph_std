from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_datastream() -> Import:
    datastream = HTTPRuntime("https://datastream.googleapis.com/")

    renames = {
        "ErrorResponse": "_datastream_1_ErrorResponse",
        "OracleSchemaIn": "_datastream_2_OracleSchemaIn",
        "OracleSchemaOut": "_datastream_3_OracleSchemaOut",
        "SourceHierarchyDatasetsIn": "_datastream_4_SourceHierarchyDatasetsIn",
        "SourceHierarchyDatasetsOut": "_datastream_5_SourceHierarchyDatasetsOut",
        "ErrorIn": "_datastream_6_ErrorIn",
        "ErrorOut": "_datastream_7_ErrorOut",
        "MysqlTableIn": "_datastream_8_MysqlTableIn",
        "MysqlTableOut": "_datastream_9_MysqlTableOut",
        "OracleRdbmsIn": "_datastream_10_OracleRdbmsIn",
        "OracleRdbmsOut": "_datastream_11_OracleRdbmsOut",
        "OracleColumnIn": "_datastream_12_OracleColumnIn",
        "OracleColumnOut": "_datastream_13_OracleColumnOut",
        "CancelOperationRequestIn": "_datastream_14_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_datastream_15_CancelOperationRequestOut",
        "ValidationIn": "_datastream_16_ValidationIn",
        "ValidationOut": "_datastream_17_ValidationOut",
        "MysqlDatabaseIn": "_datastream_18_MysqlDatabaseIn",
        "MysqlDatabaseOut": "_datastream_19_MysqlDatabaseOut",
        "StaticServiceIpConnectivityIn": "_datastream_20_StaticServiceIpConnectivityIn",
        "StaticServiceIpConnectivityOut": "_datastream_21_StaticServiceIpConnectivityOut",
        "MysqlSslConfigIn": "_datastream_22_MysqlSslConfigIn",
        "MysqlSslConfigOut": "_datastream_23_MysqlSslConfigOut",
        "MysqlProfileIn": "_datastream_24_MysqlProfileIn",
        "MysqlProfileOut": "_datastream_25_MysqlProfileOut",
        "StopBackfillJobResponseIn": "_datastream_26_StopBackfillJobResponseIn",
        "StopBackfillJobResponseOut": "_datastream_27_StopBackfillJobResponseOut",
        "LookupStreamObjectRequestIn": "_datastream_28_LookupStreamObjectRequestIn",
        "LookupStreamObjectRequestOut": "_datastream_29_LookupStreamObjectRequestOut",
        "OracleSourceConfigIn": "_datastream_30_OracleSourceConfigIn",
        "OracleSourceConfigOut": "_datastream_31_OracleSourceConfigOut",
        "BigQueryDestinationConfigIn": "_datastream_32_BigQueryDestinationConfigIn",
        "BigQueryDestinationConfigOut": "_datastream_33_BigQueryDestinationConfigOut",
        "FetchStaticIpsResponseIn": "_datastream_34_FetchStaticIpsResponseIn",
        "FetchStaticIpsResponseOut": "_datastream_35_FetchStaticIpsResponseOut",
        "OperationIn": "_datastream_36_OperationIn",
        "OperationOut": "_datastream_37_OperationOut",
        "OracleObjectIdentifierIn": "_datastream_38_OracleObjectIdentifierIn",
        "OracleObjectIdentifierOut": "_datastream_39_OracleObjectIdentifierOut",
        "SingleTargetDatasetIn": "_datastream_40_SingleTargetDatasetIn",
        "SingleTargetDatasetOut": "_datastream_41_SingleTargetDatasetOut",
        "MysqlObjectIdentifierIn": "_datastream_42_MysqlObjectIdentifierIn",
        "MysqlObjectIdentifierOut": "_datastream_43_MysqlObjectIdentifierOut",
        "PostgresqlColumnIn": "_datastream_44_PostgresqlColumnIn",
        "PostgresqlColumnOut": "_datastream_45_PostgresqlColumnOut",
        "MysqlRdbmsIn": "_datastream_46_MysqlRdbmsIn",
        "MysqlRdbmsOut": "_datastream_47_MysqlRdbmsOut",
        "EmptyIn": "_datastream_48_EmptyIn",
        "EmptyOut": "_datastream_49_EmptyOut",
        "ListConnectionProfilesResponseIn": "_datastream_50_ListConnectionProfilesResponseIn",
        "ListConnectionProfilesResponseOut": "_datastream_51_ListConnectionProfilesResponseOut",
        "PostgresqlRdbmsIn": "_datastream_52_PostgresqlRdbmsIn",
        "PostgresqlRdbmsOut": "_datastream_53_PostgresqlRdbmsOut",
        "ValidationResultIn": "_datastream_54_ValidationResultIn",
        "ValidationResultOut": "_datastream_55_ValidationResultOut",
        "PostgresqlSourceConfigIn": "_datastream_56_PostgresqlSourceConfigIn",
        "PostgresqlSourceConfigOut": "_datastream_57_PostgresqlSourceConfigOut",
        "JsonFileFormatIn": "_datastream_58_JsonFileFormatIn",
        "JsonFileFormatOut": "_datastream_59_JsonFileFormatOut",
        "GcsProfileIn": "_datastream_60_GcsProfileIn",
        "GcsProfileOut": "_datastream_61_GcsProfileOut",
        "DiscoverConnectionProfileRequestIn": "_datastream_62_DiscoverConnectionProfileRequestIn",
        "DiscoverConnectionProfileRequestOut": "_datastream_63_DiscoverConnectionProfileRequestOut",
        "GcsDestinationConfigIn": "_datastream_64_GcsDestinationConfigIn",
        "GcsDestinationConfigOut": "_datastream_65_GcsDestinationConfigOut",
        "ListRoutesResponseIn": "_datastream_66_ListRoutesResponseIn",
        "ListRoutesResponseOut": "_datastream_67_ListRoutesResponseOut",
        "ListStreamsResponseIn": "_datastream_68_ListStreamsResponseIn",
        "ListStreamsResponseOut": "_datastream_69_ListStreamsResponseOut",
        "PostgresqlTableIn": "_datastream_70_PostgresqlTableIn",
        "PostgresqlTableOut": "_datastream_71_PostgresqlTableOut",
        "ListStreamObjectsResponseIn": "_datastream_72_ListStreamObjectsResponseIn",
        "ListStreamObjectsResponseOut": "_datastream_73_ListStreamObjectsResponseOut",
        "OracleProfileIn": "_datastream_74_OracleProfileIn",
        "OracleProfileOut": "_datastream_75_OracleProfileOut",
        "SourceObjectIdentifierIn": "_datastream_76_SourceObjectIdentifierIn",
        "SourceObjectIdentifierOut": "_datastream_77_SourceObjectIdentifierOut",
        "DatasetTemplateIn": "_datastream_78_DatasetTemplateIn",
        "DatasetTemplateOut": "_datastream_79_DatasetTemplateOut",
        "RouteIn": "_datastream_80_RouteIn",
        "RouteOut": "_datastream_81_RouteOut",
        "OracleTableIn": "_datastream_82_OracleTableIn",
        "OracleTableOut": "_datastream_83_OracleTableOut",
        "StartBackfillJobRequestIn": "_datastream_84_StartBackfillJobRequestIn",
        "StartBackfillJobRequestOut": "_datastream_85_StartBackfillJobRequestOut",
        "ForwardSshTunnelConnectivityIn": "_datastream_86_ForwardSshTunnelConnectivityIn",
        "ForwardSshTunnelConnectivityOut": "_datastream_87_ForwardSshTunnelConnectivityOut",
        "PostgresqlObjectIdentifierIn": "_datastream_88_PostgresqlObjectIdentifierIn",
        "PostgresqlObjectIdentifierOut": "_datastream_89_PostgresqlObjectIdentifierOut",
        "ListOperationsResponseIn": "_datastream_90_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_datastream_91_ListOperationsResponseOut",
        "StreamObjectIn": "_datastream_92_StreamObjectIn",
        "StreamObjectOut": "_datastream_93_StreamObjectOut",
        "ListPrivateConnectionsResponseIn": "_datastream_94_ListPrivateConnectionsResponseIn",
        "ListPrivateConnectionsResponseOut": "_datastream_95_ListPrivateConnectionsResponseOut",
        "BigQueryProfileIn": "_datastream_96_BigQueryProfileIn",
        "BigQueryProfileOut": "_datastream_97_BigQueryProfileOut",
        "StopBackfillJobRequestIn": "_datastream_98_StopBackfillJobRequestIn",
        "StopBackfillJobRequestOut": "_datastream_99_StopBackfillJobRequestOut",
        "StreamLargeObjectsIn": "_datastream_100_StreamLargeObjectsIn",
        "StreamLargeObjectsOut": "_datastream_101_StreamLargeObjectsOut",
        "LocationIn": "_datastream_102_LocationIn",
        "LocationOut": "_datastream_103_LocationOut",
        "MysqlSourceConfigIn": "_datastream_104_MysqlSourceConfigIn",
        "MysqlSourceConfigOut": "_datastream_105_MysqlSourceConfigOut",
        "MysqlColumnIn": "_datastream_106_MysqlColumnIn",
        "MysqlColumnOut": "_datastream_107_MysqlColumnOut",
        "SourceConfigIn": "_datastream_108_SourceConfigIn",
        "SourceConfigOut": "_datastream_109_SourceConfigOut",
        "ListLocationsResponseIn": "_datastream_110_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_datastream_111_ListLocationsResponseOut",
        "ValidationMessageIn": "_datastream_112_ValidationMessageIn",
        "ValidationMessageOut": "_datastream_113_ValidationMessageOut",
        "PostgresqlSchemaIn": "_datastream_114_PostgresqlSchemaIn",
        "PostgresqlSchemaOut": "_datastream_115_PostgresqlSchemaOut",
        "DiscoverConnectionProfileResponseIn": "_datastream_116_DiscoverConnectionProfileResponseIn",
        "DiscoverConnectionProfileResponseOut": "_datastream_117_DiscoverConnectionProfileResponseOut",
        "StreamIn": "_datastream_118_StreamIn",
        "StreamOut": "_datastream_119_StreamOut",
        "BackfillJobIn": "_datastream_120_BackfillJobIn",
        "BackfillJobOut": "_datastream_121_BackfillJobOut",
        "VpcPeeringConfigIn": "_datastream_122_VpcPeeringConfigIn",
        "VpcPeeringConfigOut": "_datastream_123_VpcPeeringConfigOut",
        "DestinationConfigIn": "_datastream_124_DestinationConfigIn",
        "DestinationConfigOut": "_datastream_125_DestinationConfigOut",
        "DropLargeObjectsIn": "_datastream_126_DropLargeObjectsIn",
        "DropLargeObjectsOut": "_datastream_127_DropLargeObjectsOut",
        "StartBackfillJobResponseIn": "_datastream_128_StartBackfillJobResponseIn",
        "StartBackfillJobResponseOut": "_datastream_129_StartBackfillJobResponseOut",
        "AvroFileFormatIn": "_datastream_130_AvroFileFormatIn",
        "AvroFileFormatOut": "_datastream_131_AvroFileFormatOut",
        "BackfillNoneStrategyIn": "_datastream_132_BackfillNoneStrategyIn",
        "BackfillNoneStrategyOut": "_datastream_133_BackfillNoneStrategyOut",
        "PostgresqlProfileIn": "_datastream_134_PostgresqlProfileIn",
        "PostgresqlProfileOut": "_datastream_135_PostgresqlProfileOut",
        "OperationMetadataIn": "_datastream_136_OperationMetadataIn",
        "OperationMetadataOut": "_datastream_137_OperationMetadataOut",
        "StatusIn": "_datastream_138_StatusIn",
        "StatusOut": "_datastream_139_StatusOut",
        "ConnectionProfileIn": "_datastream_140_ConnectionProfileIn",
        "ConnectionProfileOut": "_datastream_141_ConnectionProfileOut",
        "PrivateConnectivityIn": "_datastream_142_PrivateConnectivityIn",
        "PrivateConnectivityOut": "_datastream_143_PrivateConnectivityOut",
        "BackfillAllStrategyIn": "_datastream_144_BackfillAllStrategyIn",
        "BackfillAllStrategyOut": "_datastream_145_BackfillAllStrategyOut",
        "PrivateConnectionIn": "_datastream_146_PrivateConnectionIn",
        "PrivateConnectionOut": "_datastream_147_PrivateConnectionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["OracleSchemaIn"] = t.struct(
        {
            "oracleTables": t.array(t.proxy(renames["OracleTableIn"])).optional(),
            "schema": t.string().optional(),
        }
    ).named(renames["OracleSchemaIn"])
    types["OracleSchemaOut"] = t.struct(
        {
            "oracleTables": t.array(t.proxy(renames["OracleTableOut"])).optional(),
            "schema": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OracleSchemaOut"])
    types["SourceHierarchyDatasetsIn"] = t.struct(
        {"datasetTemplate": t.proxy(renames["DatasetTemplateIn"]).optional()}
    ).named(renames["SourceHierarchyDatasetsIn"])
    types["SourceHierarchyDatasetsOut"] = t.struct(
        {
            "datasetTemplate": t.proxy(renames["DatasetTemplateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceHierarchyDatasetsOut"])
    types["ErrorIn"] = t.struct(
        {
            "reason": t.string().optional(),
            "errorUuid": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "errorTime": t.string().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["ErrorIn"])
    types["ErrorOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "errorUuid": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "errorTime": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorOut"])
    types["MysqlTableIn"] = t.struct(
        {
            "table": t.string().optional(),
            "mysqlColumns": t.array(t.proxy(renames["MysqlColumnIn"])).optional(),
        }
    ).named(renames["MysqlTableIn"])
    types["MysqlTableOut"] = t.struct(
        {
            "table": t.string().optional(),
            "mysqlColumns": t.array(t.proxy(renames["MysqlColumnOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MysqlTableOut"])
    types["OracleRdbmsIn"] = t.struct(
        {"oracleSchemas": t.array(t.proxy(renames["OracleSchemaIn"])).optional()}
    ).named(renames["OracleRdbmsIn"])
    types["OracleRdbmsOut"] = t.struct(
        {
            "oracleSchemas": t.array(t.proxy(renames["OracleSchemaOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OracleRdbmsOut"])
    types["OracleColumnIn"] = t.struct(
        {
            "encoding": t.string().optional(),
            "ordinalPosition": t.integer().optional(),
            "column": t.string().optional(),
            "length": t.integer().optional(),
            "primaryKey": t.boolean().optional(),
            "nullable": t.boolean().optional(),
            "precision": t.integer().optional(),
            "dataType": t.string().optional(),
            "scale": t.integer().optional(),
        }
    ).named(renames["OracleColumnIn"])
    types["OracleColumnOut"] = t.struct(
        {
            "encoding": t.string().optional(),
            "ordinalPosition": t.integer().optional(),
            "column": t.string().optional(),
            "length": t.integer().optional(),
            "primaryKey": t.boolean().optional(),
            "nullable": t.boolean().optional(),
            "precision": t.integer().optional(),
            "dataType": t.string().optional(),
            "scale": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OracleColumnOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["ValidationIn"] = t.struct(
        {
            "code": t.string().optional(),
            "message": t.array(t.proxy(renames["ValidationMessageIn"])).optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["ValidationIn"])
    types["ValidationOut"] = t.struct(
        {
            "code": t.string().optional(),
            "message": t.array(t.proxy(renames["ValidationMessageOut"])).optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationOut"])
    types["MysqlDatabaseIn"] = t.struct(
        {
            "database": t.string().optional(),
            "mysqlTables": t.array(t.proxy(renames["MysqlTableIn"])).optional(),
        }
    ).named(renames["MysqlDatabaseIn"])
    types["MysqlDatabaseOut"] = t.struct(
        {
            "database": t.string().optional(),
            "mysqlTables": t.array(t.proxy(renames["MysqlTableOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MysqlDatabaseOut"])
    types["StaticServiceIpConnectivityIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["StaticServiceIpConnectivityIn"])
    types["StaticServiceIpConnectivityOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StaticServiceIpConnectivityOut"])
    types["MysqlSslConfigIn"] = t.struct(
        {
            "caCertificate": t.string().optional(),
            "clientKey": t.string().optional(),
            "clientCertificate": t.string().optional(),
        }
    ).named(renames["MysqlSslConfigIn"])
    types["MysqlSslConfigOut"] = t.struct(
        {
            "caCertificate": t.string().optional(),
            "clientCertificateSet": t.boolean().optional(),
            "clientKeySet": t.boolean().optional(),
            "clientKey": t.string().optional(),
            "caCertificateSet": t.boolean().optional(),
            "clientCertificate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MysqlSslConfigOut"])
    types["MysqlProfileIn"] = t.struct(
        {
            "port": t.integer().optional(),
            "sslConfig": t.proxy(renames["MysqlSslConfigIn"]).optional(),
            "hostname": t.string(),
            "username": t.string(),
            "password": t.string(),
        }
    ).named(renames["MysqlProfileIn"])
    types["MysqlProfileOut"] = t.struct(
        {
            "port": t.integer().optional(),
            "sslConfig": t.proxy(renames["MysqlSslConfigOut"]).optional(),
            "hostname": t.string(),
            "username": t.string(),
            "password": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MysqlProfileOut"])
    types["StopBackfillJobResponseIn"] = t.struct(
        {"object": t.proxy(renames["StreamObjectIn"]).optional()}
    ).named(renames["StopBackfillJobResponseIn"])
    types["StopBackfillJobResponseOut"] = t.struct(
        {
            "object": t.proxy(renames["StreamObjectOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StopBackfillJobResponseOut"])
    types["LookupStreamObjectRequestIn"] = t.struct(
        {"sourceObjectIdentifier": t.proxy(renames["SourceObjectIdentifierIn"])}
    ).named(renames["LookupStreamObjectRequestIn"])
    types["LookupStreamObjectRequestOut"] = t.struct(
        {
            "sourceObjectIdentifier": t.proxy(renames["SourceObjectIdentifierOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LookupStreamObjectRequestOut"])
    types["OracleSourceConfigIn"] = t.struct(
        {
            "excludeObjects": t.proxy(renames["OracleRdbmsIn"]).optional(),
            "maxConcurrentCdcTasks": t.integer().optional(),
            "dropLargeObjects": t.proxy(renames["DropLargeObjectsIn"]).optional(),
            "streamLargeObjects": t.proxy(renames["StreamLargeObjectsIn"]).optional(),
            "includeObjects": t.proxy(renames["OracleRdbmsIn"]).optional(),
            "maxConcurrentBackfillTasks": t.integer().optional(),
        }
    ).named(renames["OracleSourceConfigIn"])
    types["OracleSourceConfigOut"] = t.struct(
        {
            "excludeObjects": t.proxy(renames["OracleRdbmsOut"]).optional(),
            "maxConcurrentCdcTasks": t.integer().optional(),
            "dropLargeObjects": t.proxy(renames["DropLargeObjectsOut"]).optional(),
            "streamLargeObjects": t.proxy(renames["StreamLargeObjectsOut"]).optional(),
            "includeObjects": t.proxy(renames["OracleRdbmsOut"]).optional(),
            "maxConcurrentBackfillTasks": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OracleSourceConfigOut"])
    types["BigQueryDestinationConfigIn"] = t.struct(
        {
            "singleTargetDataset": t.proxy(renames["SingleTargetDatasetIn"]).optional(),
            "dataFreshness": t.string().optional(),
            "sourceHierarchyDatasets": t.proxy(
                renames["SourceHierarchyDatasetsIn"]
            ).optional(),
        }
    ).named(renames["BigQueryDestinationConfigIn"])
    types["BigQueryDestinationConfigOut"] = t.struct(
        {
            "singleTargetDataset": t.proxy(
                renames["SingleTargetDatasetOut"]
            ).optional(),
            "dataFreshness": t.string().optional(),
            "sourceHierarchyDatasets": t.proxy(
                renames["SourceHierarchyDatasetsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryDestinationConfigOut"])
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
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["OracleObjectIdentifierIn"] = t.struct(
        {"schema": t.string(), "table": t.string()}
    ).named(renames["OracleObjectIdentifierIn"])
    types["OracleObjectIdentifierOut"] = t.struct(
        {
            "schema": t.string(),
            "table": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OracleObjectIdentifierOut"])
    types["SingleTargetDatasetIn"] = t.struct(
        {"datasetId": t.string().optional()}
    ).named(renames["SingleTargetDatasetIn"])
    types["SingleTargetDatasetOut"] = t.struct(
        {
            "datasetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SingleTargetDatasetOut"])
    types["MysqlObjectIdentifierIn"] = t.struct(
        {"table": t.string(), "database": t.string()}
    ).named(renames["MysqlObjectIdentifierIn"])
    types["MysqlObjectIdentifierOut"] = t.struct(
        {
            "table": t.string(),
            "database": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MysqlObjectIdentifierOut"])
    types["PostgresqlColumnIn"] = t.struct(
        {
            "nullable": t.boolean().optional(),
            "ordinalPosition": t.integer().optional(),
            "column": t.string().optional(),
            "primaryKey": t.boolean().optional(),
            "dataType": t.string().optional(),
            "scale": t.integer().optional(),
            "length": t.integer().optional(),
            "precision": t.integer().optional(),
        }
    ).named(renames["PostgresqlColumnIn"])
    types["PostgresqlColumnOut"] = t.struct(
        {
            "nullable": t.boolean().optional(),
            "ordinalPosition": t.integer().optional(),
            "column": t.string().optional(),
            "primaryKey": t.boolean().optional(),
            "dataType": t.string().optional(),
            "scale": t.integer().optional(),
            "length": t.integer().optional(),
            "precision": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostgresqlColumnOut"])
    types["MysqlRdbmsIn"] = t.struct(
        {"mysqlDatabases": t.array(t.proxy(renames["MysqlDatabaseIn"])).optional()}
    ).named(renames["MysqlRdbmsIn"])
    types["MysqlRdbmsOut"] = t.struct(
        {
            "mysqlDatabases": t.array(t.proxy(renames["MysqlDatabaseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MysqlRdbmsOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["PostgresqlRdbmsIn"] = t.struct(
        {
            "postgresqlSchemas": t.array(
                t.proxy(renames["PostgresqlSchemaIn"])
            ).optional()
        }
    ).named(renames["PostgresqlRdbmsIn"])
    types["PostgresqlRdbmsOut"] = t.struct(
        {
            "postgresqlSchemas": t.array(
                t.proxy(renames["PostgresqlSchemaOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostgresqlRdbmsOut"])
    types["ValidationResultIn"] = t.struct(
        {"validations": t.array(t.proxy(renames["ValidationIn"])).optional()}
    ).named(renames["ValidationResultIn"])
    types["ValidationResultOut"] = t.struct(
        {
            "validations": t.array(t.proxy(renames["ValidationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationResultOut"])
    types["PostgresqlSourceConfigIn"] = t.struct(
        {
            "replicationSlot": t.string(),
            "maxConcurrentBackfillTasks": t.integer().optional(),
            "includeObjects": t.proxy(renames["PostgresqlRdbmsIn"]).optional(),
            "excludeObjects": t.proxy(renames["PostgresqlRdbmsIn"]).optional(),
            "publication": t.string(),
        }
    ).named(renames["PostgresqlSourceConfigIn"])
    types["PostgresqlSourceConfigOut"] = t.struct(
        {
            "replicationSlot": t.string(),
            "maxConcurrentBackfillTasks": t.integer().optional(),
            "includeObjects": t.proxy(renames["PostgresqlRdbmsOut"]).optional(),
            "excludeObjects": t.proxy(renames["PostgresqlRdbmsOut"]).optional(),
            "publication": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostgresqlSourceConfigOut"])
    types["JsonFileFormatIn"] = t.struct(
        {
            "compression": t.string().optional(),
            "schemaFileFormat": t.string().optional(),
        }
    ).named(renames["JsonFileFormatIn"])
    types["JsonFileFormatOut"] = t.struct(
        {
            "compression": t.string().optional(),
            "schemaFileFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JsonFileFormatOut"])
    types["GcsProfileIn"] = t.struct(
        {"bucket": t.string(), "rootPath": t.string().optional()}
    ).named(renames["GcsProfileIn"])
    types["GcsProfileOut"] = t.struct(
        {
            "bucket": t.string(),
            "rootPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsProfileOut"])
    types["DiscoverConnectionProfileRequestIn"] = t.struct(
        {
            "mysqlRdbms": t.proxy(renames["MysqlRdbmsIn"]).optional(),
            "connectionProfile": t.proxy(renames["ConnectionProfileIn"]).optional(),
            "fullHierarchy": t.boolean().optional(),
            "oracleRdbms": t.proxy(renames["OracleRdbmsIn"]).optional(),
            "connectionProfileName": t.string().optional(),
            "hierarchyDepth": t.integer().optional(),
            "postgresqlRdbms": t.proxy(renames["PostgresqlRdbmsIn"]).optional(),
        }
    ).named(renames["DiscoverConnectionProfileRequestIn"])
    types["DiscoverConnectionProfileRequestOut"] = t.struct(
        {
            "mysqlRdbms": t.proxy(renames["MysqlRdbmsOut"]).optional(),
            "connectionProfile": t.proxy(renames["ConnectionProfileOut"]).optional(),
            "fullHierarchy": t.boolean().optional(),
            "oracleRdbms": t.proxy(renames["OracleRdbmsOut"]).optional(),
            "connectionProfileName": t.string().optional(),
            "hierarchyDepth": t.integer().optional(),
            "postgresqlRdbms": t.proxy(renames["PostgresqlRdbmsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiscoverConnectionProfileRequestOut"])
    types["GcsDestinationConfigIn"] = t.struct(
        {
            "avroFileFormat": t.proxy(renames["AvroFileFormatIn"]).optional(),
            "jsonFileFormat": t.proxy(renames["JsonFileFormatIn"]).optional(),
            "path": t.string().optional(),
            "fileRotationMb": t.integer().optional(),
            "fileRotationInterval": t.string().optional(),
        }
    ).named(renames["GcsDestinationConfigIn"])
    types["GcsDestinationConfigOut"] = t.struct(
        {
            "avroFileFormat": t.proxy(renames["AvroFileFormatOut"]).optional(),
            "jsonFileFormat": t.proxy(renames["JsonFileFormatOut"]).optional(),
            "path": t.string().optional(),
            "fileRotationMb": t.integer().optional(),
            "fileRotationInterval": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsDestinationConfigOut"])
    types["ListRoutesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "routes": t.array(t.proxy(renames["RouteIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListRoutesResponseIn"])
    types["ListRoutesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "routes": t.array(t.proxy(renames["RouteOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRoutesResponseOut"])
    types["ListStreamsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "streams": t.array(t.proxy(renames["StreamIn"])).optional(),
        }
    ).named(renames["ListStreamsResponseIn"])
    types["ListStreamsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "streams": t.array(t.proxy(renames["StreamOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListStreamsResponseOut"])
    types["PostgresqlTableIn"] = t.struct(
        {
            "table": t.string().optional(),
            "postgresqlColumns": t.array(
                t.proxy(renames["PostgresqlColumnIn"])
            ).optional(),
        }
    ).named(renames["PostgresqlTableIn"])
    types["PostgresqlTableOut"] = t.struct(
        {
            "table": t.string().optional(),
            "postgresqlColumns": t.array(
                t.proxy(renames["PostgresqlColumnOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostgresqlTableOut"])
    types["ListStreamObjectsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "streamObjects": t.array(t.proxy(renames["StreamObjectIn"])).optional(),
        }
    ).named(renames["ListStreamObjectsResponseIn"])
    types["ListStreamObjectsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "streamObjects": t.array(t.proxy(renames["StreamObjectOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListStreamObjectsResponseOut"])
    types["OracleProfileIn"] = t.struct(
        {
            "password": t.string(),
            "hostname": t.string(),
            "connectionAttributes": t.struct({"_": t.string().optional()}).optional(),
            "databaseService": t.string(),
            "port": t.integer().optional(),
            "username": t.string(),
        }
    ).named(renames["OracleProfileIn"])
    types["OracleProfileOut"] = t.struct(
        {
            "password": t.string(),
            "hostname": t.string(),
            "connectionAttributes": t.struct({"_": t.string().optional()}).optional(),
            "databaseService": t.string(),
            "port": t.integer().optional(),
            "username": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OracleProfileOut"])
    types["SourceObjectIdentifierIn"] = t.struct(
        {
            "postgresqlIdentifier": t.proxy(
                renames["PostgresqlObjectIdentifierIn"]
            ).optional(),
            "oracleIdentifier": t.proxy(renames["OracleObjectIdentifierIn"]).optional(),
            "mysqlIdentifier": t.proxy(renames["MysqlObjectIdentifierIn"]).optional(),
        }
    ).named(renames["SourceObjectIdentifierIn"])
    types["SourceObjectIdentifierOut"] = t.struct(
        {
            "postgresqlIdentifier": t.proxy(
                renames["PostgresqlObjectIdentifierOut"]
            ).optional(),
            "oracleIdentifier": t.proxy(
                renames["OracleObjectIdentifierOut"]
            ).optional(),
            "mysqlIdentifier": t.proxy(renames["MysqlObjectIdentifierOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceObjectIdentifierOut"])
    types["DatasetTemplateIn"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "location": t.string(),
            "datasetIdPrefix": t.string().optional(),
        }
    ).named(renames["DatasetTemplateIn"])
    types["DatasetTemplateOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "location": t.string(),
            "datasetIdPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatasetTemplateOut"])
    types["RouteIn"] = t.struct(
        {
            "destinationAddress": t.string(),
            "destinationPort": t.integer().optional(),
            "displayName": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["RouteIn"])
    types["RouteOut"] = t.struct(
        {
            "name": t.string().optional(),
            "destinationAddress": t.string(),
            "updateTime": t.string().optional(),
            "destinationPort": t.integer().optional(),
            "displayName": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RouteOut"])
    types["OracleTableIn"] = t.struct(
        {
            "oracleColumns": t.array(t.proxy(renames["OracleColumnIn"])).optional(),
            "table": t.string().optional(),
        }
    ).named(renames["OracleTableIn"])
    types["OracleTableOut"] = t.struct(
        {
            "oracleColumns": t.array(t.proxy(renames["OracleColumnOut"])).optional(),
            "table": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OracleTableOut"])
    types["StartBackfillJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StartBackfillJobRequestIn"]
    )
    types["StartBackfillJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StartBackfillJobRequestOut"])
    types["ForwardSshTunnelConnectivityIn"] = t.struct(
        {
            "port": t.integer().optional(),
            "username": t.string(),
            "privateKey": t.string().optional(),
            "hostname": t.string(),
            "password": t.string().optional(),
        }
    ).named(renames["ForwardSshTunnelConnectivityIn"])
    types["ForwardSshTunnelConnectivityOut"] = t.struct(
        {
            "port": t.integer().optional(),
            "username": t.string(),
            "privateKey": t.string().optional(),
            "hostname": t.string(),
            "password": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ForwardSshTunnelConnectivityOut"])
    types["PostgresqlObjectIdentifierIn"] = t.struct(
        {"table": t.string(), "schema": t.string()}
    ).named(renames["PostgresqlObjectIdentifierIn"])
    types["PostgresqlObjectIdentifierOut"] = t.struct(
        {
            "table": t.string(),
            "schema": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostgresqlObjectIdentifierOut"])
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
    types["StreamObjectIn"] = t.struct(
        {
            "sourceObject": t.proxy(renames["SourceObjectIdentifierIn"]).optional(),
            "backfillJob": t.proxy(renames["BackfillJobIn"]).optional(),
            "displayName": t.string(),
        }
    ).named(renames["StreamObjectIn"])
    types["StreamObjectOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "sourceObject": t.proxy(renames["SourceObjectIdentifierOut"]).optional(),
            "errors": t.array(t.proxy(renames["ErrorOut"])).optional(),
            "backfillJob": t.proxy(renames["BackfillJobOut"]).optional(),
            "displayName": t.string(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamObjectOut"])
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
    types["BigQueryProfileIn"] = t.struct({"_": t.string().optional()}).named(
        renames["BigQueryProfileIn"]
    )
    types["BigQueryProfileOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["BigQueryProfileOut"])
    types["StopBackfillJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StopBackfillJobRequestIn"]
    )
    types["StopBackfillJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StopBackfillJobRequestOut"])
    types["StreamLargeObjectsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StreamLargeObjectsIn"]
    )
    types["StreamLargeObjectsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StreamLargeObjectsOut"])
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["MysqlSourceConfigIn"] = t.struct(
        {
            "includeObjects": t.proxy(renames["MysqlRdbmsIn"]).optional(),
            "maxConcurrentBackfillTasks": t.integer().optional(),
            "maxConcurrentCdcTasks": t.integer().optional(),
            "excludeObjects": t.proxy(renames["MysqlRdbmsIn"]).optional(),
        }
    ).named(renames["MysqlSourceConfigIn"])
    types["MysqlSourceConfigOut"] = t.struct(
        {
            "includeObjects": t.proxy(renames["MysqlRdbmsOut"]).optional(),
            "maxConcurrentBackfillTasks": t.integer().optional(),
            "maxConcurrentCdcTasks": t.integer().optional(),
            "excludeObjects": t.proxy(renames["MysqlRdbmsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MysqlSourceConfigOut"])
    types["MysqlColumnIn"] = t.struct(
        {
            "primaryKey": t.boolean().optional(),
            "collation": t.string().optional(),
            "dataType": t.string().optional(),
            "nullable": t.boolean().optional(),
            "column": t.string().optional(),
            "ordinalPosition": t.integer().optional(),
            "length": t.integer().optional(),
        }
    ).named(renames["MysqlColumnIn"])
    types["MysqlColumnOut"] = t.struct(
        {
            "primaryKey": t.boolean().optional(),
            "collation": t.string().optional(),
            "dataType": t.string().optional(),
            "nullable": t.boolean().optional(),
            "column": t.string().optional(),
            "ordinalPosition": t.integer().optional(),
            "length": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MysqlColumnOut"])
    types["SourceConfigIn"] = t.struct(
        {
            "sourceConnectionProfile": t.string(),
            "oracleSourceConfig": t.proxy(renames["OracleSourceConfigIn"]).optional(),
            "mysqlSourceConfig": t.proxy(renames["MysqlSourceConfigIn"]).optional(),
            "postgresqlSourceConfig": t.proxy(
                renames["PostgresqlSourceConfigIn"]
            ).optional(),
        }
    ).named(renames["SourceConfigIn"])
    types["SourceConfigOut"] = t.struct(
        {
            "sourceConnectionProfile": t.string(),
            "oracleSourceConfig": t.proxy(renames["OracleSourceConfigOut"]).optional(),
            "mysqlSourceConfig": t.proxy(renames["MysqlSourceConfigOut"]).optional(),
            "postgresqlSourceConfig": t.proxy(
                renames["PostgresqlSourceConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceConfigOut"])
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
    types["ValidationMessageIn"] = t.struct(
        {
            "code": t.string().optional(),
            "message": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "level": t.string().optional(),
        }
    ).named(renames["ValidationMessageIn"])
    types["ValidationMessageOut"] = t.struct(
        {
            "code": t.string().optional(),
            "message": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "level": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationMessageOut"])
    types["PostgresqlSchemaIn"] = t.struct(
        {
            "postgresqlTables": t.array(
                t.proxy(renames["PostgresqlTableIn"])
            ).optional(),
            "schema": t.string().optional(),
        }
    ).named(renames["PostgresqlSchemaIn"])
    types["PostgresqlSchemaOut"] = t.struct(
        {
            "postgresqlTables": t.array(
                t.proxy(renames["PostgresqlTableOut"])
            ).optional(),
            "schema": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostgresqlSchemaOut"])
    types["DiscoverConnectionProfileResponseIn"] = t.struct(
        {
            "postgresqlRdbms": t.proxy(renames["PostgresqlRdbmsIn"]).optional(),
            "mysqlRdbms": t.proxy(renames["MysqlRdbmsIn"]).optional(),
            "oracleRdbms": t.proxy(renames["OracleRdbmsIn"]).optional(),
        }
    ).named(renames["DiscoverConnectionProfileResponseIn"])
    types["DiscoverConnectionProfileResponseOut"] = t.struct(
        {
            "postgresqlRdbms": t.proxy(renames["PostgresqlRdbmsOut"]).optional(),
            "mysqlRdbms": t.proxy(renames["MysqlRdbmsOut"]).optional(),
            "oracleRdbms": t.proxy(renames["OracleRdbmsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiscoverConnectionProfileResponseOut"])
    types["StreamIn"] = t.struct(
        {
            "state": t.string().optional(),
            "destinationConfig": t.proxy(renames["DestinationConfigIn"]),
            "displayName": t.string(),
            "backfillNone": t.proxy(renames["BackfillNoneStrategyIn"]).optional(),
            "customerManagedEncryptionKey": t.string().optional(),
            "sourceConfig": t.proxy(renames["SourceConfigIn"]),
            "backfillAll": t.proxy(renames["BackfillAllStrategyIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["StreamIn"])
    types["StreamOut"] = t.struct(
        {
            "state": t.string().optional(),
            "destinationConfig": t.proxy(renames["DestinationConfigOut"]),
            "displayName": t.string(),
            "backfillNone": t.proxy(renames["BackfillNoneStrategyOut"]).optional(),
            "errors": t.array(t.proxy(renames["ErrorOut"])).optional(),
            "customerManagedEncryptionKey": t.string().optional(),
            "name": t.string().optional(),
            "sourceConfig": t.proxy(renames["SourceConfigOut"]),
            "backfillAll": t.proxy(renames["BackfillAllStrategyOut"]).optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamOut"])
    types["BackfillJobIn"] = t.struct(
        {"trigger": t.string().optional(), "state": t.string().optional()}
    ).named(renames["BackfillJobIn"])
    types["BackfillJobOut"] = t.struct(
        {
            "lastEndTime": t.string().optional(),
            "lastStartTime": t.string().optional(),
            "trigger": t.string().optional(),
            "errors": t.array(t.proxy(renames["ErrorOut"])).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackfillJobOut"])
    types["VpcPeeringConfigIn"] = t.struct(
        {"vpc": t.string(), "subnet": t.string()}
    ).named(renames["VpcPeeringConfigIn"])
    types["VpcPeeringConfigOut"] = t.struct(
        {
            "vpc": t.string(),
            "subnet": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VpcPeeringConfigOut"])
    types["DestinationConfigIn"] = t.struct(
        {
            "bigqueryDestinationConfig": t.proxy(
                renames["BigQueryDestinationConfigIn"]
            ).optional(),
            "gcsDestinationConfig": t.proxy(
                renames["GcsDestinationConfigIn"]
            ).optional(),
            "destinationConnectionProfile": t.string(),
        }
    ).named(renames["DestinationConfigIn"])
    types["DestinationConfigOut"] = t.struct(
        {
            "bigqueryDestinationConfig": t.proxy(
                renames["BigQueryDestinationConfigOut"]
            ).optional(),
            "gcsDestinationConfig": t.proxy(
                renames["GcsDestinationConfigOut"]
            ).optional(),
            "destinationConnectionProfile": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationConfigOut"])
    types["DropLargeObjectsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DropLargeObjectsIn"]
    )
    types["DropLargeObjectsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DropLargeObjectsOut"])
    types["StartBackfillJobResponseIn"] = t.struct(
        {"object": t.proxy(renames["StreamObjectIn"]).optional()}
    ).named(renames["StartBackfillJobResponseIn"])
    types["StartBackfillJobResponseOut"] = t.struct(
        {
            "object": t.proxy(renames["StreamObjectOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartBackfillJobResponseOut"])
    types["AvroFileFormatIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AvroFileFormatIn"]
    )
    types["AvroFileFormatOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AvroFileFormatOut"])
    types["BackfillNoneStrategyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["BackfillNoneStrategyIn"]
    )
    types["BackfillNoneStrategyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["BackfillNoneStrategyOut"])
    types["PostgresqlProfileIn"] = t.struct(
        {
            "password": t.string(),
            "username": t.string(),
            "port": t.integer().optional(),
            "hostname": t.string(),
            "database": t.string(),
        }
    ).named(renames["PostgresqlProfileIn"])
    types["PostgresqlProfileOut"] = t.struct(
        {
            "password": t.string(),
            "username": t.string(),
            "port": t.integer().optional(),
            "hostname": t.string(),
            "database": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostgresqlProfileOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "validationResult": t.proxy(renames["ValidationResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["ConnectionProfileIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "privateConnectivity": t.proxy(renames["PrivateConnectivityIn"]).optional(),
            "postgresqlProfile": t.proxy(renames["PostgresqlProfileIn"]).optional(),
            "displayName": t.string(),
            "forwardSshConnectivity": t.proxy(
                renames["ForwardSshTunnelConnectivityIn"]
            ).optional(),
            "staticServiceIpConnectivity": t.proxy(
                renames["StaticServiceIpConnectivityIn"]
            ).optional(),
            "gcsProfile": t.proxy(renames["GcsProfileIn"]).optional(),
            "mysqlProfile": t.proxy(renames["MysqlProfileIn"]).optional(),
            "oracleProfile": t.proxy(renames["OracleProfileIn"]).optional(),
            "bigqueryProfile": t.proxy(renames["BigQueryProfileIn"]).optional(),
        }
    ).named(renames["ConnectionProfileIn"])
    types["ConnectionProfileOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "privateConnectivity": t.proxy(
                renames["PrivateConnectivityOut"]
            ).optional(),
            "postgresqlProfile": t.proxy(renames["PostgresqlProfileOut"]).optional(),
            "displayName": t.string(),
            "updateTime": t.string().optional(),
            "forwardSshConnectivity": t.proxy(
                renames["ForwardSshTunnelConnectivityOut"]
            ).optional(),
            "staticServiceIpConnectivity": t.proxy(
                renames["StaticServiceIpConnectivityOut"]
            ).optional(),
            "gcsProfile": t.proxy(renames["GcsProfileOut"]).optional(),
            "mysqlProfile": t.proxy(renames["MysqlProfileOut"]).optional(),
            "oracleProfile": t.proxy(renames["OracleProfileOut"]).optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "bigqueryProfile": t.proxy(renames["BigQueryProfileOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionProfileOut"])
    types["PrivateConnectivityIn"] = t.struct({"privateConnection": t.string()}).named(
        renames["PrivateConnectivityIn"]
    )
    types["PrivateConnectivityOut"] = t.struct(
        {
            "privateConnection": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateConnectivityOut"])
    types["BackfillAllStrategyIn"] = t.struct(
        {
            "mysqlExcludedObjects": t.proxy(renames["MysqlRdbmsIn"]).optional(),
            "oracleExcludedObjects": t.proxy(renames["OracleRdbmsIn"]).optional(),
            "postgresqlExcludedObjects": t.proxy(
                renames["PostgresqlRdbmsIn"]
            ).optional(),
        }
    ).named(renames["BackfillAllStrategyIn"])
    types["BackfillAllStrategyOut"] = t.struct(
        {
            "mysqlExcludedObjects": t.proxy(renames["MysqlRdbmsOut"]).optional(),
            "oracleExcludedObjects": t.proxy(renames["OracleRdbmsOut"]).optional(),
            "postgresqlExcludedObjects": t.proxy(
                renames["PostgresqlRdbmsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackfillAllStrategyOut"])
    types["PrivateConnectionIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "vpcPeeringConfig": t.proxy(renames["VpcPeeringConfigIn"]).optional(),
            "displayName": t.string(),
        }
    ).named(renames["PrivateConnectionIn"])
    types["PrivateConnectionOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "vpcPeeringConfig": t.proxy(renames["VpcPeeringConfigOut"]).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string(),
        }
    ).named(renames["PrivateConnectionOut"])

    functions = {}
    functions["projectsLocationsGet"] = datastream.get(
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
    functions["projectsLocationsList"] = datastream.get(
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
    functions["projectsLocationsFetchStaticIps"] = datastream.get(
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
    functions["projectsLocationsStreamsCreate"] = datastream.get(
        "v1/{parent}/streams",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListStreamsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsDelete"] = datastream.get(
        "v1/{parent}/streams",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListStreamsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsGet"] = datastream.get(
        "v1/{parent}/streams",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListStreamsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsPatch"] = datastream.get(
        "v1/{parent}/streams",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListStreamsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsList"] = datastream.get(
        "v1/{parent}/streams",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListStreamsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsObjectsGet"] = datastream.post(
        "v1/{object}:stopBackfillJob",
        t.struct(
            {
                "object": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StopBackfillJobResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsObjectsLookup"] = datastream.post(
        "v1/{object}:stopBackfillJob",
        t.struct(
            {
                "object": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StopBackfillJobResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsObjectsList"] = datastream.post(
        "v1/{object}:stopBackfillJob",
        t.struct(
            {
                "object": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StopBackfillJobResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsObjectsStartBackfillJob"] = datastream.post(
        "v1/{object}:stopBackfillJob",
        t.struct(
            {
                "object": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StopBackfillJobResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsObjectsStopBackfillJob"] = datastream.post(
        "v1/{object}:stopBackfillJob",
        t.struct(
            {
                "object": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StopBackfillJobResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = datastream.post(
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
    functions["projectsLocationsOperationsList"] = datastream.post(
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
    functions["projectsLocationsOperationsGet"] = datastream.post(
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
    functions["projectsLocationsOperationsCancel"] = datastream.post(
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
    functions["projectsLocationsConnectionProfilesDiscover"] = datastream.post(
        "v1/{parent}/connectionProfiles",
        t.struct(
            {
                "force": t.boolean().optional(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "connectionProfileId": t.string(),
                "validateOnly": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "privateConnectivity": t.proxy(
                    renames["PrivateConnectivityIn"]
                ).optional(),
                "postgresqlProfile": t.proxy(renames["PostgresqlProfileIn"]).optional(),
                "displayName": t.string(),
                "forwardSshConnectivity": t.proxy(
                    renames["ForwardSshTunnelConnectivityIn"]
                ).optional(),
                "staticServiceIpConnectivity": t.proxy(
                    renames["StaticServiceIpConnectivityIn"]
                ).optional(),
                "gcsProfile": t.proxy(renames["GcsProfileIn"]).optional(),
                "mysqlProfile": t.proxy(renames["MysqlProfileIn"]).optional(),
                "oracleProfile": t.proxy(renames["OracleProfileIn"]).optional(),
                "bigqueryProfile": t.proxy(renames["BigQueryProfileIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesList"] = datastream.post(
        "v1/{parent}/connectionProfiles",
        t.struct(
            {
                "force": t.boolean().optional(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "connectionProfileId": t.string(),
                "validateOnly": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "privateConnectivity": t.proxy(
                    renames["PrivateConnectivityIn"]
                ).optional(),
                "postgresqlProfile": t.proxy(renames["PostgresqlProfileIn"]).optional(),
                "displayName": t.string(),
                "forwardSshConnectivity": t.proxy(
                    renames["ForwardSshTunnelConnectivityIn"]
                ).optional(),
                "staticServiceIpConnectivity": t.proxy(
                    renames["StaticServiceIpConnectivityIn"]
                ).optional(),
                "gcsProfile": t.proxy(renames["GcsProfileIn"]).optional(),
                "mysqlProfile": t.proxy(renames["MysqlProfileIn"]).optional(),
                "oracleProfile": t.proxy(renames["OracleProfileIn"]).optional(),
                "bigqueryProfile": t.proxy(renames["BigQueryProfileIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesGet"] = datastream.post(
        "v1/{parent}/connectionProfiles",
        t.struct(
            {
                "force": t.boolean().optional(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "connectionProfileId": t.string(),
                "validateOnly": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "privateConnectivity": t.proxy(
                    renames["PrivateConnectivityIn"]
                ).optional(),
                "postgresqlProfile": t.proxy(renames["PostgresqlProfileIn"]).optional(),
                "displayName": t.string(),
                "forwardSshConnectivity": t.proxy(
                    renames["ForwardSshTunnelConnectivityIn"]
                ).optional(),
                "staticServiceIpConnectivity": t.proxy(
                    renames["StaticServiceIpConnectivityIn"]
                ).optional(),
                "gcsProfile": t.proxy(renames["GcsProfileIn"]).optional(),
                "mysqlProfile": t.proxy(renames["MysqlProfileIn"]).optional(),
                "oracleProfile": t.proxy(renames["OracleProfileIn"]).optional(),
                "bigqueryProfile": t.proxy(renames["BigQueryProfileIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesDelete"] = datastream.post(
        "v1/{parent}/connectionProfiles",
        t.struct(
            {
                "force": t.boolean().optional(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "connectionProfileId": t.string(),
                "validateOnly": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "privateConnectivity": t.proxy(
                    renames["PrivateConnectivityIn"]
                ).optional(),
                "postgresqlProfile": t.proxy(renames["PostgresqlProfileIn"]).optional(),
                "displayName": t.string(),
                "forwardSshConnectivity": t.proxy(
                    renames["ForwardSshTunnelConnectivityIn"]
                ).optional(),
                "staticServiceIpConnectivity": t.proxy(
                    renames["StaticServiceIpConnectivityIn"]
                ).optional(),
                "gcsProfile": t.proxy(renames["GcsProfileIn"]).optional(),
                "mysqlProfile": t.proxy(renames["MysqlProfileIn"]).optional(),
                "oracleProfile": t.proxy(renames["OracleProfileIn"]).optional(),
                "bigqueryProfile": t.proxy(renames["BigQueryProfileIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesPatch"] = datastream.post(
        "v1/{parent}/connectionProfiles",
        t.struct(
            {
                "force": t.boolean().optional(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "connectionProfileId": t.string(),
                "validateOnly": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "privateConnectivity": t.proxy(
                    renames["PrivateConnectivityIn"]
                ).optional(),
                "postgresqlProfile": t.proxy(renames["PostgresqlProfileIn"]).optional(),
                "displayName": t.string(),
                "forwardSshConnectivity": t.proxy(
                    renames["ForwardSshTunnelConnectivityIn"]
                ).optional(),
                "staticServiceIpConnectivity": t.proxy(
                    renames["StaticServiceIpConnectivityIn"]
                ).optional(),
                "gcsProfile": t.proxy(renames["GcsProfileIn"]).optional(),
                "mysqlProfile": t.proxy(renames["MysqlProfileIn"]).optional(),
                "oracleProfile": t.proxy(renames["OracleProfileIn"]).optional(),
                "bigqueryProfile": t.proxy(renames["BigQueryProfileIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesCreate"] = datastream.post(
        "v1/{parent}/connectionProfiles",
        t.struct(
            {
                "force": t.boolean().optional(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "connectionProfileId": t.string(),
                "validateOnly": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "privateConnectivity": t.proxy(
                    renames["PrivateConnectivityIn"]
                ).optional(),
                "postgresqlProfile": t.proxy(renames["PostgresqlProfileIn"]).optional(),
                "displayName": t.string(),
                "forwardSshConnectivity": t.proxy(
                    renames["ForwardSshTunnelConnectivityIn"]
                ).optional(),
                "staticServiceIpConnectivity": t.proxy(
                    renames["StaticServiceIpConnectivityIn"]
                ).optional(),
                "gcsProfile": t.proxy(renames["GcsProfileIn"]).optional(),
                "mysqlProfile": t.proxy(renames["MysqlProfileIn"]).optional(),
                "oracleProfile": t.proxy(renames["OracleProfileIn"]).optional(),
                "bigqueryProfile": t.proxy(renames["BigQueryProfileIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsCreate"] = datastream.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["PrivateConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsDelete"] = datastream.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["PrivateConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsList"] = datastream.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["PrivateConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsGet"] = datastream.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["PrivateConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsRoutesDelete"] = datastream.post(
        "v1/{parent}/routes",
        t.struct(
            {
                "routeId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "destinationAddress": t.string(),
                "destinationPort": t.integer().optional(),
                "displayName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsRoutesGet"] = datastream.post(
        "v1/{parent}/routes",
        t.struct(
            {
                "routeId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "destinationAddress": t.string(),
                "destinationPort": t.integer().optional(),
                "displayName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsRoutesList"] = datastream.post(
        "v1/{parent}/routes",
        t.struct(
            {
                "routeId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "destinationAddress": t.string(),
                "destinationPort": t.integer().optional(),
                "displayName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsRoutesCreate"] = datastream.post(
        "v1/{parent}/routes",
        t.struct(
            {
                "routeId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "destinationAddress": t.string(),
                "destinationPort": t.integer().optional(),
                "displayName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="datastream",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
