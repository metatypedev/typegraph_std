from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_datastream() -> Import:
    datastream = HTTPRuntime("https://datastream.googleapis.com/")

    renames = {
        "ErrorResponse": "_datastream_1_ErrorResponse",
        "BigQueryProfileIn": "_datastream_2_BigQueryProfileIn",
        "BigQueryProfileOut": "_datastream_3_BigQueryProfileOut",
        "ListRoutesResponseIn": "_datastream_4_ListRoutesResponseIn",
        "ListRoutesResponseOut": "_datastream_5_ListRoutesResponseOut",
        "SourceObjectIdentifierIn": "_datastream_6_SourceObjectIdentifierIn",
        "SourceObjectIdentifierOut": "_datastream_7_SourceObjectIdentifierOut",
        "ValidationResultIn": "_datastream_8_ValidationResultIn",
        "ValidationResultOut": "_datastream_9_ValidationResultOut",
        "ForwardSshTunnelConnectivityIn": "_datastream_10_ForwardSshTunnelConnectivityIn",
        "ForwardSshTunnelConnectivityOut": "_datastream_11_ForwardSshTunnelConnectivityOut",
        "ListPrivateConnectionsResponseIn": "_datastream_12_ListPrivateConnectionsResponseIn",
        "ListPrivateConnectionsResponseOut": "_datastream_13_ListPrivateConnectionsResponseOut",
        "StopBackfillJobRequestIn": "_datastream_14_StopBackfillJobRequestIn",
        "StopBackfillJobRequestOut": "_datastream_15_StopBackfillJobRequestOut",
        "OracleRdbmsIn": "_datastream_16_OracleRdbmsIn",
        "OracleRdbmsOut": "_datastream_17_OracleRdbmsOut",
        "DiscoverConnectionProfileResponseIn": "_datastream_18_DiscoverConnectionProfileResponseIn",
        "DiscoverConnectionProfileResponseOut": "_datastream_19_DiscoverConnectionProfileResponseOut",
        "LookupStreamObjectRequestIn": "_datastream_20_LookupStreamObjectRequestIn",
        "LookupStreamObjectRequestOut": "_datastream_21_LookupStreamObjectRequestOut",
        "ListConnectionProfilesResponseIn": "_datastream_22_ListConnectionProfilesResponseIn",
        "ListConnectionProfilesResponseOut": "_datastream_23_ListConnectionProfilesResponseOut",
        "SourceConfigIn": "_datastream_24_SourceConfigIn",
        "SourceConfigOut": "_datastream_25_SourceConfigOut",
        "JsonFileFormatIn": "_datastream_26_JsonFileFormatIn",
        "JsonFileFormatOut": "_datastream_27_JsonFileFormatOut",
        "ConnectionProfileIn": "_datastream_28_ConnectionProfileIn",
        "ConnectionProfileOut": "_datastream_29_ConnectionProfileOut",
        "ValidationIn": "_datastream_30_ValidationIn",
        "ValidationOut": "_datastream_31_ValidationOut",
        "StartBackfillJobRequestIn": "_datastream_32_StartBackfillJobRequestIn",
        "StartBackfillJobRequestOut": "_datastream_33_StartBackfillJobRequestOut",
        "ErrorIn": "_datastream_34_ErrorIn",
        "ErrorOut": "_datastream_35_ErrorOut",
        "MysqlObjectIdentifierIn": "_datastream_36_MysqlObjectIdentifierIn",
        "MysqlObjectIdentifierOut": "_datastream_37_MysqlObjectIdentifierOut",
        "PrivateConnectivityIn": "_datastream_38_PrivateConnectivityIn",
        "PrivateConnectivityOut": "_datastream_39_PrivateConnectivityOut",
        "OperationMetadataIn": "_datastream_40_OperationMetadataIn",
        "OperationMetadataOut": "_datastream_41_OperationMetadataOut",
        "CancelOperationRequestIn": "_datastream_42_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_datastream_43_CancelOperationRequestOut",
        "PostgresqlSchemaIn": "_datastream_44_PostgresqlSchemaIn",
        "PostgresqlSchemaOut": "_datastream_45_PostgresqlSchemaOut",
        "MysqlProfileIn": "_datastream_46_MysqlProfileIn",
        "MysqlProfileOut": "_datastream_47_MysqlProfileOut",
        "OracleProfileIn": "_datastream_48_OracleProfileIn",
        "OracleProfileOut": "_datastream_49_OracleProfileOut",
        "OracleTableIn": "_datastream_50_OracleTableIn",
        "OracleTableOut": "_datastream_51_OracleTableOut",
        "GcsDestinationConfigIn": "_datastream_52_GcsDestinationConfigIn",
        "GcsDestinationConfigOut": "_datastream_53_GcsDestinationConfigOut",
        "AvroFileFormatIn": "_datastream_54_AvroFileFormatIn",
        "AvroFileFormatOut": "_datastream_55_AvroFileFormatOut",
        "StartBackfillJobResponseIn": "_datastream_56_StartBackfillJobResponseIn",
        "StartBackfillJobResponseOut": "_datastream_57_StartBackfillJobResponseOut",
        "PrivateConnectionIn": "_datastream_58_PrivateConnectionIn",
        "PrivateConnectionOut": "_datastream_59_PrivateConnectionOut",
        "VpcPeeringConfigIn": "_datastream_60_VpcPeeringConfigIn",
        "VpcPeeringConfigOut": "_datastream_61_VpcPeeringConfigOut",
        "BackfillAllStrategyIn": "_datastream_62_BackfillAllStrategyIn",
        "BackfillAllStrategyOut": "_datastream_63_BackfillAllStrategyOut",
        "BigQueryDestinationConfigIn": "_datastream_64_BigQueryDestinationConfigIn",
        "BigQueryDestinationConfigOut": "_datastream_65_BigQueryDestinationConfigOut",
        "StopBackfillJobResponseIn": "_datastream_66_StopBackfillJobResponseIn",
        "StopBackfillJobResponseOut": "_datastream_67_StopBackfillJobResponseOut",
        "BackfillNoneStrategyIn": "_datastream_68_BackfillNoneStrategyIn",
        "BackfillNoneStrategyOut": "_datastream_69_BackfillNoneStrategyOut",
        "DropLargeObjectsIn": "_datastream_70_DropLargeObjectsIn",
        "DropLargeObjectsOut": "_datastream_71_DropLargeObjectsOut",
        "PostgresqlRdbmsIn": "_datastream_72_PostgresqlRdbmsIn",
        "PostgresqlRdbmsOut": "_datastream_73_PostgresqlRdbmsOut",
        "LocationIn": "_datastream_74_LocationIn",
        "LocationOut": "_datastream_75_LocationOut",
        "DatasetTemplateIn": "_datastream_76_DatasetTemplateIn",
        "DatasetTemplateOut": "_datastream_77_DatasetTemplateOut",
        "PostgresqlTableIn": "_datastream_78_PostgresqlTableIn",
        "PostgresqlTableOut": "_datastream_79_PostgresqlTableOut",
        "DiscoverConnectionProfileRequestIn": "_datastream_80_DiscoverConnectionProfileRequestIn",
        "DiscoverConnectionProfileRequestOut": "_datastream_81_DiscoverConnectionProfileRequestOut",
        "OracleObjectIdentifierIn": "_datastream_82_OracleObjectIdentifierIn",
        "OracleObjectIdentifierOut": "_datastream_83_OracleObjectIdentifierOut",
        "PostgresqlSourceConfigIn": "_datastream_84_PostgresqlSourceConfigIn",
        "PostgresqlSourceConfigOut": "_datastream_85_PostgresqlSourceConfigOut",
        "ListLocationsResponseIn": "_datastream_86_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_datastream_87_ListLocationsResponseOut",
        "StreamIn": "_datastream_88_StreamIn",
        "StreamOut": "_datastream_89_StreamOut",
        "EmptyIn": "_datastream_90_EmptyIn",
        "EmptyOut": "_datastream_91_EmptyOut",
        "MysqlColumnIn": "_datastream_92_MysqlColumnIn",
        "MysqlColumnOut": "_datastream_93_MysqlColumnOut",
        "OracleSourceConfigIn": "_datastream_94_OracleSourceConfigIn",
        "OracleSourceConfigOut": "_datastream_95_OracleSourceConfigOut",
        "OracleColumnIn": "_datastream_96_OracleColumnIn",
        "OracleColumnOut": "_datastream_97_OracleColumnOut",
        "OperationIn": "_datastream_98_OperationIn",
        "OperationOut": "_datastream_99_OperationOut",
        "MysqlSourceConfigIn": "_datastream_100_MysqlSourceConfigIn",
        "MysqlSourceConfigOut": "_datastream_101_MysqlSourceConfigOut",
        "OracleSchemaIn": "_datastream_102_OracleSchemaIn",
        "OracleSchemaOut": "_datastream_103_OracleSchemaOut",
        "MysqlRdbmsIn": "_datastream_104_MysqlRdbmsIn",
        "MysqlRdbmsOut": "_datastream_105_MysqlRdbmsOut",
        "SourceHierarchyDatasetsIn": "_datastream_106_SourceHierarchyDatasetsIn",
        "SourceHierarchyDatasetsOut": "_datastream_107_SourceHierarchyDatasetsOut",
        "StatusIn": "_datastream_108_StatusIn",
        "StatusOut": "_datastream_109_StatusOut",
        "GcsProfileIn": "_datastream_110_GcsProfileIn",
        "GcsProfileOut": "_datastream_111_GcsProfileOut",
        "StaticServiceIpConnectivityIn": "_datastream_112_StaticServiceIpConnectivityIn",
        "StaticServiceIpConnectivityOut": "_datastream_113_StaticServiceIpConnectivityOut",
        "PostgresqlProfileIn": "_datastream_114_PostgresqlProfileIn",
        "PostgresqlProfileOut": "_datastream_115_PostgresqlProfileOut",
        "DestinationConfigIn": "_datastream_116_DestinationConfigIn",
        "DestinationConfigOut": "_datastream_117_DestinationConfigOut",
        "MysqlSslConfigIn": "_datastream_118_MysqlSslConfigIn",
        "MysqlSslConfigOut": "_datastream_119_MysqlSslConfigOut",
        "ListOperationsResponseIn": "_datastream_120_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_datastream_121_ListOperationsResponseOut",
        "ListStreamObjectsResponseIn": "_datastream_122_ListStreamObjectsResponseIn",
        "ListStreamObjectsResponseOut": "_datastream_123_ListStreamObjectsResponseOut",
        "SingleTargetDatasetIn": "_datastream_124_SingleTargetDatasetIn",
        "SingleTargetDatasetOut": "_datastream_125_SingleTargetDatasetOut",
        "MysqlTableIn": "_datastream_126_MysqlTableIn",
        "MysqlTableOut": "_datastream_127_MysqlTableOut",
        "StreamLargeObjectsIn": "_datastream_128_StreamLargeObjectsIn",
        "StreamLargeObjectsOut": "_datastream_129_StreamLargeObjectsOut",
        "ListStreamsResponseIn": "_datastream_130_ListStreamsResponseIn",
        "ListStreamsResponseOut": "_datastream_131_ListStreamsResponseOut",
        "PostgresqlColumnIn": "_datastream_132_PostgresqlColumnIn",
        "PostgresqlColumnOut": "_datastream_133_PostgresqlColumnOut",
        "MysqlDatabaseIn": "_datastream_134_MysqlDatabaseIn",
        "MysqlDatabaseOut": "_datastream_135_MysqlDatabaseOut",
        "BackfillJobIn": "_datastream_136_BackfillJobIn",
        "BackfillJobOut": "_datastream_137_BackfillJobOut",
        "FetchStaticIpsResponseIn": "_datastream_138_FetchStaticIpsResponseIn",
        "FetchStaticIpsResponseOut": "_datastream_139_FetchStaticIpsResponseOut",
        "StreamObjectIn": "_datastream_140_StreamObjectIn",
        "StreamObjectOut": "_datastream_141_StreamObjectOut",
        "ValidationMessageIn": "_datastream_142_ValidationMessageIn",
        "ValidationMessageOut": "_datastream_143_ValidationMessageOut",
        "PostgresqlObjectIdentifierIn": "_datastream_144_PostgresqlObjectIdentifierIn",
        "PostgresqlObjectIdentifierOut": "_datastream_145_PostgresqlObjectIdentifierOut",
        "RouteIn": "_datastream_146_RouteIn",
        "RouteOut": "_datastream_147_RouteOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["BigQueryProfileIn"] = t.struct({"_": t.string().optional()}).named(
        renames["BigQueryProfileIn"]
    )
    types["BigQueryProfileOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["BigQueryProfileOut"])
    types["ListRoutesResponseIn"] = t.struct(
        {
            "routes": t.array(t.proxy(renames["RouteIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListRoutesResponseIn"])
    types["ListRoutesResponseOut"] = t.struct(
        {
            "routes": t.array(t.proxy(renames["RouteOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRoutesResponseOut"])
    types["SourceObjectIdentifierIn"] = t.struct(
        {
            "postgresqlIdentifier": t.proxy(
                renames["PostgresqlObjectIdentifierIn"]
            ).optional(),
            "mysqlIdentifier": t.proxy(renames["MysqlObjectIdentifierIn"]).optional(),
            "oracleIdentifier": t.proxy(renames["OracleObjectIdentifierIn"]).optional(),
        }
    ).named(renames["SourceObjectIdentifierIn"])
    types["SourceObjectIdentifierOut"] = t.struct(
        {
            "postgresqlIdentifier": t.proxy(
                renames["PostgresqlObjectIdentifierOut"]
            ).optional(),
            "mysqlIdentifier": t.proxy(renames["MysqlObjectIdentifierOut"]).optional(),
            "oracleIdentifier": t.proxy(
                renames["OracleObjectIdentifierOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceObjectIdentifierOut"])
    types["ValidationResultIn"] = t.struct(
        {"validations": t.array(t.proxy(renames["ValidationIn"])).optional()}
    ).named(renames["ValidationResultIn"])
    types["ValidationResultOut"] = t.struct(
        {
            "validations": t.array(t.proxy(renames["ValidationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationResultOut"])
    types["ForwardSshTunnelConnectivityIn"] = t.struct(
        {
            "port": t.integer().optional(),
            "password": t.string().optional(),
            "hostname": t.string(),
            "username": t.string(),
            "privateKey": t.string().optional(),
        }
    ).named(renames["ForwardSshTunnelConnectivityIn"])
    types["ForwardSshTunnelConnectivityOut"] = t.struct(
        {
            "port": t.integer().optional(),
            "password": t.string().optional(),
            "hostname": t.string(),
            "username": t.string(),
            "privateKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ForwardSshTunnelConnectivityOut"])
    types["ListPrivateConnectionsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "privateConnections": t.array(
                t.proxy(renames["PrivateConnectionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListPrivateConnectionsResponseIn"])
    types["ListPrivateConnectionsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "privateConnections": t.array(
                t.proxy(renames["PrivateConnectionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPrivateConnectionsResponseOut"])
    types["StopBackfillJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StopBackfillJobRequestIn"]
    )
    types["StopBackfillJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StopBackfillJobRequestOut"])
    types["OracleRdbmsIn"] = t.struct(
        {"oracleSchemas": t.array(t.proxy(renames["OracleSchemaIn"])).optional()}
    ).named(renames["OracleRdbmsIn"])
    types["OracleRdbmsOut"] = t.struct(
        {
            "oracleSchemas": t.array(t.proxy(renames["OracleSchemaOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OracleRdbmsOut"])
    types["DiscoverConnectionProfileResponseIn"] = t.struct(
        {
            "mysqlRdbms": t.proxy(renames["MysqlRdbmsIn"]).optional(),
            "oracleRdbms": t.proxy(renames["OracleRdbmsIn"]).optional(),
            "postgresqlRdbms": t.proxy(renames["PostgresqlRdbmsIn"]).optional(),
        }
    ).named(renames["DiscoverConnectionProfileResponseIn"])
    types["DiscoverConnectionProfileResponseOut"] = t.struct(
        {
            "mysqlRdbms": t.proxy(renames["MysqlRdbmsOut"]).optional(),
            "oracleRdbms": t.proxy(renames["OracleRdbmsOut"]).optional(),
            "postgresqlRdbms": t.proxy(renames["PostgresqlRdbmsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiscoverConnectionProfileResponseOut"])
    types["LookupStreamObjectRequestIn"] = t.struct(
        {"sourceObjectIdentifier": t.proxy(renames["SourceObjectIdentifierIn"])}
    ).named(renames["LookupStreamObjectRequestIn"])
    types["LookupStreamObjectRequestOut"] = t.struct(
        {
            "sourceObjectIdentifier": t.proxy(renames["SourceObjectIdentifierOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LookupStreamObjectRequestOut"])
    types["ListConnectionProfilesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "connectionProfiles": t.array(
                t.proxy(renames["ConnectionProfileIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListConnectionProfilesResponseIn"])
    types["ListConnectionProfilesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "connectionProfiles": t.array(
                t.proxy(renames["ConnectionProfileOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConnectionProfilesResponseOut"])
    types["SourceConfigIn"] = t.struct(
        {
            "oracleSourceConfig": t.proxy(renames["OracleSourceConfigIn"]).optional(),
            "mysqlSourceConfig": t.proxy(renames["MysqlSourceConfigIn"]).optional(),
            "sourceConnectionProfile": t.string(),
            "postgresqlSourceConfig": t.proxy(
                renames["PostgresqlSourceConfigIn"]
            ).optional(),
        }
    ).named(renames["SourceConfigIn"])
    types["SourceConfigOut"] = t.struct(
        {
            "oracleSourceConfig": t.proxy(renames["OracleSourceConfigOut"]).optional(),
            "mysqlSourceConfig": t.proxy(renames["MysqlSourceConfigOut"]).optional(),
            "sourceConnectionProfile": t.string(),
            "postgresqlSourceConfig": t.proxy(
                renames["PostgresqlSourceConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceConfigOut"])
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
    types["ConnectionProfileIn"] = t.struct(
        {
            "forwardSshConnectivity": t.proxy(
                renames["ForwardSshTunnelConnectivityIn"]
            ).optional(),
            "mysqlProfile": t.proxy(renames["MysqlProfileIn"]).optional(),
            "bigqueryProfile": t.proxy(renames["BigQueryProfileIn"]).optional(),
            "privateConnectivity": t.proxy(renames["PrivateConnectivityIn"]).optional(),
            "displayName": t.string(),
            "gcsProfile": t.proxy(renames["GcsProfileIn"]).optional(),
            "staticServiceIpConnectivity": t.proxy(
                renames["StaticServiceIpConnectivityIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "postgresqlProfile": t.proxy(renames["PostgresqlProfileIn"]).optional(),
            "oracleProfile": t.proxy(renames["OracleProfileIn"]).optional(),
        }
    ).named(renames["ConnectionProfileIn"])
    types["ConnectionProfileOut"] = t.struct(
        {
            "forwardSshConnectivity": t.proxy(
                renames["ForwardSshTunnelConnectivityOut"]
            ).optional(),
            "mysqlProfile": t.proxy(renames["MysqlProfileOut"]).optional(),
            "bigqueryProfile": t.proxy(renames["BigQueryProfileOut"]).optional(),
            "privateConnectivity": t.proxy(
                renames["PrivateConnectivityOut"]
            ).optional(),
            "displayName": t.string(),
            "gcsProfile": t.proxy(renames["GcsProfileOut"]).optional(),
            "staticServiceIpConnectivity": t.proxy(
                renames["StaticServiceIpConnectivityOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "postgresqlProfile": t.proxy(renames["PostgresqlProfileOut"]).optional(),
            "oracleProfile": t.proxy(renames["OracleProfileOut"]).optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionProfileOut"])
    types["ValidationIn"] = t.struct(
        {
            "description": t.string().optional(),
            "code": t.string().optional(),
            "message": t.array(t.proxy(renames["ValidationMessageIn"])).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["ValidationIn"])
    types["ValidationOut"] = t.struct(
        {
            "description": t.string().optional(),
            "code": t.string().optional(),
            "message": t.array(t.proxy(renames["ValidationMessageOut"])).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationOut"])
    types["StartBackfillJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StartBackfillJobRequestIn"]
    )
    types["StartBackfillJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StartBackfillJobRequestOut"])
    types["ErrorIn"] = t.struct(
        {
            "message": t.string().optional(),
            "errorUuid": t.string().optional(),
            "reason": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "errorTime": t.string().optional(),
        }
    ).named(renames["ErrorIn"])
    types["ErrorOut"] = t.struct(
        {
            "message": t.string().optional(),
            "errorUuid": t.string().optional(),
            "reason": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "errorTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorOut"])
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
    types["PrivateConnectivityIn"] = t.struct({"privateConnection": t.string()}).named(
        renames["PrivateConnectivityIn"]
    )
    types["PrivateConnectivityOut"] = t.struct(
        {
            "privateConnection": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateConnectivityOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "validationResult": t.proxy(renames["ValidationResultOut"]).optional(),
            "apiVersion": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "statusMessage": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["PostgresqlSchemaIn"] = t.struct(
        {
            "schema": t.string().optional(),
            "postgresqlTables": t.array(
                t.proxy(renames["PostgresqlTableIn"])
            ).optional(),
        }
    ).named(renames["PostgresqlSchemaIn"])
    types["PostgresqlSchemaOut"] = t.struct(
        {
            "schema": t.string().optional(),
            "postgresqlTables": t.array(
                t.proxy(renames["PostgresqlTableOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostgresqlSchemaOut"])
    types["MysqlProfileIn"] = t.struct(
        {
            "sslConfig": t.proxy(renames["MysqlSslConfigIn"]).optional(),
            "username": t.string(),
            "port": t.integer().optional(),
            "password": t.string(),
            "hostname": t.string(),
        }
    ).named(renames["MysqlProfileIn"])
    types["MysqlProfileOut"] = t.struct(
        {
            "sslConfig": t.proxy(renames["MysqlSslConfigOut"]).optional(),
            "username": t.string(),
            "port": t.integer().optional(),
            "password": t.string(),
            "hostname": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MysqlProfileOut"])
    types["OracleProfileIn"] = t.struct(
        {
            "hostname": t.string(),
            "databaseService": t.string(),
            "port": t.integer().optional(),
            "connectionAttributes": t.struct({"_": t.string().optional()}).optional(),
            "username": t.string(),
            "password": t.string(),
        }
    ).named(renames["OracleProfileIn"])
    types["OracleProfileOut"] = t.struct(
        {
            "hostname": t.string(),
            "databaseService": t.string(),
            "port": t.integer().optional(),
            "connectionAttributes": t.struct({"_": t.string().optional()}).optional(),
            "username": t.string(),
            "password": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OracleProfileOut"])
    types["OracleTableIn"] = t.struct(
        {
            "table": t.string().optional(),
            "oracleColumns": t.array(t.proxy(renames["OracleColumnIn"])).optional(),
        }
    ).named(renames["OracleTableIn"])
    types["OracleTableOut"] = t.struct(
        {
            "table": t.string().optional(),
            "oracleColumns": t.array(t.proxy(renames["OracleColumnOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OracleTableOut"])
    types["GcsDestinationConfigIn"] = t.struct(
        {
            "avroFileFormat": t.proxy(renames["AvroFileFormatIn"]).optional(),
            "fileRotationMb": t.integer().optional(),
            "path": t.string().optional(),
            "fileRotationInterval": t.string().optional(),
            "jsonFileFormat": t.proxy(renames["JsonFileFormatIn"]).optional(),
        }
    ).named(renames["GcsDestinationConfigIn"])
    types["GcsDestinationConfigOut"] = t.struct(
        {
            "avroFileFormat": t.proxy(renames["AvroFileFormatOut"]).optional(),
            "fileRotationMb": t.integer().optional(),
            "path": t.string().optional(),
            "fileRotationInterval": t.string().optional(),
            "jsonFileFormat": t.proxy(renames["JsonFileFormatOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsDestinationConfigOut"])
    types["AvroFileFormatIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AvroFileFormatIn"]
    )
    types["AvroFileFormatOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AvroFileFormatOut"])
    types["StartBackfillJobResponseIn"] = t.struct(
        {"object": t.proxy(renames["StreamObjectIn"]).optional()}
    ).named(renames["StartBackfillJobResponseIn"])
    types["StartBackfillJobResponseOut"] = t.struct(
        {
            "object": t.proxy(renames["StreamObjectOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartBackfillJobResponseOut"])
    types["PrivateConnectionIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string(),
            "vpcPeeringConfig": t.proxy(renames["VpcPeeringConfigIn"]).optional(),
        }
    ).named(renames["PrivateConnectionIn"])
    types["PrivateConnectionOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string(),
            "createTime": t.string().optional(),
            "vpcPeeringConfig": t.proxy(renames["VpcPeeringConfigOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["PrivateConnectionOut"])
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
    types["BackfillAllStrategyIn"] = t.struct(
        {
            "oracleExcludedObjects": t.proxy(renames["OracleRdbmsIn"]).optional(),
            "mysqlExcludedObjects": t.proxy(renames["MysqlRdbmsIn"]).optional(),
            "postgresqlExcludedObjects": t.proxy(
                renames["PostgresqlRdbmsIn"]
            ).optional(),
        }
    ).named(renames["BackfillAllStrategyIn"])
    types["BackfillAllStrategyOut"] = t.struct(
        {
            "oracleExcludedObjects": t.proxy(renames["OracleRdbmsOut"]).optional(),
            "mysqlExcludedObjects": t.proxy(renames["MysqlRdbmsOut"]).optional(),
            "postgresqlExcludedObjects": t.proxy(
                renames["PostgresqlRdbmsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackfillAllStrategyOut"])
    types["BigQueryDestinationConfigIn"] = t.struct(
        {
            "sourceHierarchyDatasets": t.proxy(
                renames["SourceHierarchyDatasetsIn"]
            ).optional(),
            "dataFreshness": t.string().optional(),
            "singleTargetDataset": t.proxy(renames["SingleTargetDatasetIn"]).optional(),
        }
    ).named(renames["BigQueryDestinationConfigIn"])
    types["BigQueryDestinationConfigOut"] = t.struct(
        {
            "sourceHierarchyDatasets": t.proxy(
                renames["SourceHierarchyDatasetsOut"]
            ).optional(),
            "dataFreshness": t.string().optional(),
            "singleTargetDataset": t.proxy(
                renames["SingleTargetDatasetOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryDestinationConfigOut"])
    types["StopBackfillJobResponseIn"] = t.struct(
        {"object": t.proxy(renames["StreamObjectIn"]).optional()}
    ).named(renames["StopBackfillJobResponseIn"])
    types["StopBackfillJobResponseOut"] = t.struct(
        {
            "object": t.proxy(renames["StreamObjectOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StopBackfillJobResponseOut"])
    types["BackfillNoneStrategyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["BackfillNoneStrategyIn"]
    )
    types["BackfillNoneStrategyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["BackfillNoneStrategyOut"])
    types["DropLargeObjectsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DropLargeObjectsIn"]
    )
    types["DropLargeObjectsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DropLargeObjectsOut"])
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
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["DatasetTemplateIn"] = t.struct(
        {
            "datasetIdPrefix": t.string().optional(),
            "location": t.string(),
            "kmsKeyName": t.string().optional(),
        }
    ).named(renames["DatasetTemplateIn"])
    types["DatasetTemplateOut"] = t.struct(
        {
            "datasetIdPrefix": t.string().optional(),
            "location": t.string(),
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatasetTemplateOut"])
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
    types["DiscoverConnectionProfileRequestIn"] = t.struct(
        {
            "hierarchyDepth": t.integer().optional(),
            "mysqlRdbms": t.proxy(renames["MysqlRdbmsIn"]).optional(),
            "connectionProfileName": t.string().optional(),
            "oracleRdbms": t.proxy(renames["OracleRdbmsIn"]).optional(),
            "fullHierarchy": t.boolean().optional(),
            "postgresqlRdbms": t.proxy(renames["PostgresqlRdbmsIn"]).optional(),
            "connectionProfile": t.proxy(renames["ConnectionProfileIn"]).optional(),
        }
    ).named(renames["DiscoverConnectionProfileRequestIn"])
    types["DiscoverConnectionProfileRequestOut"] = t.struct(
        {
            "hierarchyDepth": t.integer().optional(),
            "mysqlRdbms": t.proxy(renames["MysqlRdbmsOut"]).optional(),
            "connectionProfileName": t.string().optional(),
            "oracleRdbms": t.proxy(renames["OracleRdbmsOut"]).optional(),
            "fullHierarchy": t.boolean().optional(),
            "postgresqlRdbms": t.proxy(renames["PostgresqlRdbmsOut"]).optional(),
            "connectionProfile": t.proxy(renames["ConnectionProfileOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiscoverConnectionProfileRequestOut"])
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
    types["PostgresqlSourceConfigIn"] = t.struct(
        {
            "publication": t.string(),
            "includeObjects": t.proxy(renames["PostgresqlRdbmsIn"]).optional(),
            "maxConcurrentBackfillTasks": t.integer().optional(),
            "excludeObjects": t.proxy(renames["PostgresqlRdbmsIn"]).optional(),
            "replicationSlot": t.string(),
        }
    ).named(renames["PostgresqlSourceConfigIn"])
    types["PostgresqlSourceConfigOut"] = t.struct(
        {
            "publication": t.string(),
            "includeObjects": t.proxy(renames["PostgresqlRdbmsOut"]).optional(),
            "maxConcurrentBackfillTasks": t.integer().optional(),
            "excludeObjects": t.proxy(renames["PostgresqlRdbmsOut"]).optional(),
            "replicationSlot": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostgresqlSourceConfigOut"])
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
    types["StreamIn"] = t.struct(
        {
            "displayName": t.string(),
            "backfillAll": t.proxy(renames["BackfillAllStrategyIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "sourceConfig": t.proxy(renames["SourceConfigIn"]),
            "customerManagedEncryptionKey": t.string().optional(),
            "backfillNone": t.proxy(renames["BackfillNoneStrategyIn"]).optional(),
            "destinationConfig": t.proxy(renames["DestinationConfigIn"]),
        }
    ).named(renames["StreamIn"])
    types["StreamOut"] = t.struct(
        {
            "displayName": t.string(),
            "backfillAll": t.proxy(renames["BackfillAllStrategyOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "sourceConfig": t.proxy(renames["SourceConfigOut"]),
            "customerManagedEncryptionKey": t.string().optional(),
            "errors": t.array(t.proxy(renames["ErrorOut"])).optional(),
            "createTime": t.string().optional(),
            "backfillNone": t.proxy(renames["BackfillNoneStrategyOut"]).optional(),
            "destinationConfig": t.proxy(renames["DestinationConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["MysqlColumnIn"] = t.struct(
        {
            "dataType": t.string().optional(),
            "nullable": t.boolean().optional(),
            "primaryKey": t.boolean().optional(),
            "ordinalPosition": t.integer().optional(),
            "collation": t.string().optional(),
            "column": t.string().optional(),
            "length": t.integer().optional(),
        }
    ).named(renames["MysqlColumnIn"])
    types["MysqlColumnOut"] = t.struct(
        {
            "dataType": t.string().optional(),
            "nullable": t.boolean().optional(),
            "primaryKey": t.boolean().optional(),
            "ordinalPosition": t.integer().optional(),
            "collation": t.string().optional(),
            "column": t.string().optional(),
            "length": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MysqlColumnOut"])
    types["OracleSourceConfigIn"] = t.struct(
        {
            "maxConcurrentCdcTasks": t.integer().optional(),
            "includeObjects": t.proxy(renames["OracleRdbmsIn"]).optional(),
            "dropLargeObjects": t.proxy(renames["DropLargeObjectsIn"]).optional(),
            "streamLargeObjects": t.proxy(renames["StreamLargeObjectsIn"]).optional(),
            "excludeObjects": t.proxy(renames["OracleRdbmsIn"]).optional(),
            "maxConcurrentBackfillTasks": t.integer().optional(),
        }
    ).named(renames["OracleSourceConfigIn"])
    types["OracleSourceConfigOut"] = t.struct(
        {
            "maxConcurrentCdcTasks": t.integer().optional(),
            "includeObjects": t.proxy(renames["OracleRdbmsOut"]).optional(),
            "dropLargeObjects": t.proxy(renames["DropLargeObjectsOut"]).optional(),
            "streamLargeObjects": t.proxy(renames["StreamLargeObjectsOut"]).optional(),
            "excludeObjects": t.proxy(renames["OracleRdbmsOut"]).optional(),
            "maxConcurrentBackfillTasks": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OracleSourceConfigOut"])
    types["OracleColumnIn"] = t.struct(
        {
            "primaryKey": t.boolean().optional(),
            "encoding": t.string().optional(),
            "precision": t.integer().optional(),
            "nullable": t.boolean().optional(),
            "column": t.string().optional(),
            "scale": t.integer().optional(),
            "ordinalPosition": t.integer().optional(),
            "dataType": t.string().optional(),
            "length": t.integer().optional(),
        }
    ).named(renames["OracleColumnIn"])
    types["OracleColumnOut"] = t.struct(
        {
            "primaryKey": t.boolean().optional(),
            "encoding": t.string().optional(),
            "precision": t.integer().optional(),
            "nullable": t.boolean().optional(),
            "column": t.string().optional(),
            "scale": t.integer().optional(),
            "ordinalPosition": t.integer().optional(),
            "dataType": t.string().optional(),
            "length": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OracleColumnOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["MysqlSourceConfigIn"] = t.struct(
        {
            "maxConcurrentCdcTasks": t.integer().optional(),
            "includeObjects": t.proxy(renames["MysqlRdbmsIn"]).optional(),
            "maxConcurrentBackfillTasks": t.integer().optional(),
            "excludeObjects": t.proxy(renames["MysqlRdbmsIn"]).optional(),
        }
    ).named(renames["MysqlSourceConfigIn"])
    types["MysqlSourceConfigOut"] = t.struct(
        {
            "maxConcurrentCdcTasks": t.integer().optional(),
            "includeObjects": t.proxy(renames["MysqlRdbmsOut"]).optional(),
            "maxConcurrentBackfillTasks": t.integer().optional(),
            "excludeObjects": t.proxy(renames["MysqlRdbmsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MysqlSourceConfigOut"])
    types["OracleSchemaIn"] = t.struct(
        {
            "schema": t.string().optional(),
            "oracleTables": t.array(t.proxy(renames["OracleTableIn"])).optional(),
        }
    ).named(renames["OracleSchemaIn"])
    types["OracleSchemaOut"] = t.struct(
        {
            "schema": t.string().optional(),
            "oracleTables": t.array(t.proxy(renames["OracleTableOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OracleSchemaOut"])
    types["MysqlRdbmsIn"] = t.struct(
        {"mysqlDatabases": t.array(t.proxy(renames["MysqlDatabaseIn"])).optional()}
    ).named(renames["MysqlRdbmsIn"])
    types["MysqlRdbmsOut"] = t.struct(
        {
            "mysqlDatabases": t.array(t.proxy(renames["MysqlDatabaseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MysqlRdbmsOut"])
    types["SourceHierarchyDatasetsIn"] = t.struct(
        {"datasetTemplate": t.proxy(renames["DatasetTemplateIn"]).optional()}
    ).named(renames["SourceHierarchyDatasetsIn"])
    types["SourceHierarchyDatasetsOut"] = t.struct(
        {
            "datasetTemplate": t.proxy(renames["DatasetTemplateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceHierarchyDatasetsOut"])
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
    types["StaticServiceIpConnectivityIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["StaticServiceIpConnectivityIn"])
    types["StaticServiceIpConnectivityOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StaticServiceIpConnectivityOut"])
    types["PostgresqlProfileIn"] = t.struct(
        {
            "port": t.integer().optional(),
            "database": t.string(),
            "password": t.string(),
            "username": t.string(),
            "hostname": t.string(),
        }
    ).named(renames["PostgresqlProfileIn"])
    types["PostgresqlProfileOut"] = t.struct(
        {
            "port": t.integer().optional(),
            "database": t.string(),
            "password": t.string(),
            "username": t.string(),
            "hostname": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostgresqlProfileOut"])
    types["DestinationConfigIn"] = t.struct(
        {
            "gcsDestinationConfig": t.proxy(
                renames["GcsDestinationConfigIn"]
            ).optional(),
            "destinationConnectionProfile": t.string(),
            "bigqueryDestinationConfig": t.proxy(
                renames["BigQueryDestinationConfigIn"]
            ).optional(),
        }
    ).named(renames["DestinationConfigIn"])
    types["DestinationConfigOut"] = t.struct(
        {
            "gcsDestinationConfig": t.proxy(
                renames["GcsDestinationConfigOut"]
            ).optional(),
            "destinationConnectionProfile": t.string(),
            "bigqueryDestinationConfig": t.proxy(
                renames["BigQueryDestinationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationConfigOut"])
    types["MysqlSslConfigIn"] = t.struct(
        {
            "clientKey": t.string().optional(),
            "clientCertificate": t.string().optional(),
            "caCertificate": t.string().optional(),
        }
    ).named(renames["MysqlSslConfigIn"])
    types["MysqlSslConfigOut"] = t.struct(
        {
            "clientKey": t.string().optional(),
            "clientCertificate": t.string().optional(),
            "caCertificateSet": t.boolean().optional(),
            "clientCertificateSet": t.boolean().optional(),
            "clientKeySet": t.boolean().optional(),
            "caCertificate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MysqlSslConfigOut"])
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
    types["SingleTargetDatasetIn"] = t.struct(
        {"datasetId": t.string().optional()}
    ).named(renames["SingleTargetDatasetIn"])
    types["SingleTargetDatasetOut"] = t.struct(
        {
            "datasetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SingleTargetDatasetOut"])
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
    types["StreamLargeObjectsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StreamLargeObjectsIn"]
    )
    types["StreamLargeObjectsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StreamLargeObjectsOut"])
    types["ListStreamsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "streams": t.array(t.proxy(renames["StreamIn"])).optional(),
        }
    ).named(renames["ListStreamsResponseIn"])
    types["ListStreamsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "streams": t.array(t.proxy(renames["StreamOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListStreamsResponseOut"])
    types["PostgresqlColumnIn"] = t.struct(
        {
            "length": t.integer().optional(),
            "dataType": t.string().optional(),
            "primaryKey": t.boolean().optional(),
            "ordinalPosition": t.integer().optional(),
            "scale": t.integer().optional(),
            "nullable": t.boolean().optional(),
            "column": t.string().optional(),
            "precision": t.integer().optional(),
        }
    ).named(renames["PostgresqlColumnIn"])
    types["PostgresqlColumnOut"] = t.struct(
        {
            "length": t.integer().optional(),
            "dataType": t.string().optional(),
            "primaryKey": t.boolean().optional(),
            "ordinalPosition": t.integer().optional(),
            "scale": t.integer().optional(),
            "nullable": t.boolean().optional(),
            "column": t.string().optional(),
            "precision": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostgresqlColumnOut"])
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
    types["BackfillJobIn"] = t.struct(
        {"trigger": t.string().optional(), "state": t.string().optional()}
    ).named(renames["BackfillJobIn"])
    types["BackfillJobOut"] = t.struct(
        {
            "trigger": t.string().optional(),
            "errors": t.array(t.proxy(renames["ErrorOut"])).optional(),
            "lastEndTime": t.string().optional(),
            "state": t.string().optional(),
            "lastStartTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackfillJobOut"])
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
    types["StreamObjectIn"] = t.struct(
        {
            "displayName": t.string(),
            "sourceObject": t.proxy(renames["SourceObjectIdentifierIn"]).optional(),
            "backfillJob": t.proxy(renames["BackfillJobIn"]).optional(),
        }
    ).named(renames["StreamObjectIn"])
    types["StreamObjectOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "displayName": t.string(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "sourceObject": t.proxy(renames["SourceObjectIdentifierOut"]).optional(),
            "backfillJob": t.proxy(renames["BackfillJobOut"]).optional(),
            "errors": t.array(t.proxy(renames["ErrorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamObjectOut"])
    types["ValidationMessageIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "code": t.string().optional(),
            "message": t.string().optional(),
            "level": t.string().optional(),
        }
    ).named(renames["ValidationMessageIn"])
    types["ValidationMessageOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "code": t.string().optional(),
            "message": t.string().optional(),
            "level": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationMessageOut"])
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
    types["RouteIn"] = t.struct(
        {
            "destinationAddress": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "destinationPort": t.integer().optional(),
            "displayName": t.string(),
        }
    ).named(renames["RouteIn"])
    types["RouteOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "destinationAddress": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "destinationPort": t.integer().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RouteOut"])

    functions = {}
    functions["projectsLocationsGet"] = datastream.get(
        "v1/{name}:fetchStaticIps",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FetchStaticIpsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesGet"] = datastream.patch(
        "v1/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "force": t.boolean().optional(),
                "requestId": t.string().optional(),
                "forwardSshConnectivity": t.proxy(
                    renames["ForwardSshTunnelConnectivityIn"]
                ).optional(),
                "mysqlProfile": t.proxy(renames["MysqlProfileIn"]).optional(),
                "bigqueryProfile": t.proxy(renames["BigQueryProfileIn"]).optional(),
                "privateConnectivity": t.proxy(
                    renames["PrivateConnectivityIn"]
                ).optional(),
                "displayName": t.string(),
                "gcsProfile": t.proxy(renames["GcsProfileIn"]).optional(),
                "staticServiceIpConnectivity": t.proxy(
                    renames["StaticServiceIpConnectivityIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "postgresqlProfile": t.proxy(renames["PostgresqlProfileIn"]).optional(),
                "oracleProfile": t.proxy(renames["OracleProfileIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesList"] = datastream.patch(
        "v1/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "force": t.boolean().optional(),
                "requestId": t.string().optional(),
                "forwardSshConnectivity": t.proxy(
                    renames["ForwardSshTunnelConnectivityIn"]
                ).optional(),
                "mysqlProfile": t.proxy(renames["MysqlProfileIn"]).optional(),
                "bigqueryProfile": t.proxy(renames["BigQueryProfileIn"]).optional(),
                "privateConnectivity": t.proxy(
                    renames["PrivateConnectivityIn"]
                ).optional(),
                "displayName": t.string(),
                "gcsProfile": t.proxy(renames["GcsProfileIn"]).optional(),
                "staticServiceIpConnectivity": t.proxy(
                    renames["StaticServiceIpConnectivityIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "postgresqlProfile": t.proxy(renames["PostgresqlProfileIn"]).optional(),
                "oracleProfile": t.proxy(renames["OracleProfileIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesDiscover"] = datastream.patch(
        "v1/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "force": t.boolean().optional(),
                "requestId": t.string().optional(),
                "forwardSshConnectivity": t.proxy(
                    renames["ForwardSshTunnelConnectivityIn"]
                ).optional(),
                "mysqlProfile": t.proxy(renames["MysqlProfileIn"]).optional(),
                "bigqueryProfile": t.proxy(renames["BigQueryProfileIn"]).optional(),
                "privateConnectivity": t.proxy(
                    renames["PrivateConnectivityIn"]
                ).optional(),
                "displayName": t.string(),
                "gcsProfile": t.proxy(renames["GcsProfileIn"]).optional(),
                "staticServiceIpConnectivity": t.proxy(
                    renames["StaticServiceIpConnectivityIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "postgresqlProfile": t.proxy(renames["PostgresqlProfileIn"]).optional(),
                "oracleProfile": t.proxy(renames["OracleProfileIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesDelete"] = datastream.patch(
        "v1/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "force": t.boolean().optional(),
                "requestId": t.string().optional(),
                "forwardSshConnectivity": t.proxy(
                    renames["ForwardSshTunnelConnectivityIn"]
                ).optional(),
                "mysqlProfile": t.proxy(renames["MysqlProfileIn"]).optional(),
                "bigqueryProfile": t.proxy(renames["BigQueryProfileIn"]).optional(),
                "privateConnectivity": t.proxy(
                    renames["PrivateConnectivityIn"]
                ).optional(),
                "displayName": t.string(),
                "gcsProfile": t.proxy(renames["GcsProfileIn"]).optional(),
                "staticServiceIpConnectivity": t.proxy(
                    renames["StaticServiceIpConnectivityIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "postgresqlProfile": t.proxy(renames["PostgresqlProfileIn"]).optional(),
                "oracleProfile": t.proxy(renames["OracleProfileIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesCreate"] = datastream.patch(
        "v1/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "force": t.boolean().optional(),
                "requestId": t.string().optional(),
                "forwardSshConnectivity": t.proxy(
                    renames["ForwardSshTunnelConnectivityIn"]
                ).optional(),
                "mysqlProfile": t.proxy(renames["MysqlProfileIn"]).optional(),
                "bigqueryProfile": t.proxy(renames["BigQueryProfileIn"]).optional(),
                "privateConnectivity": t.proxy(
                    renames["PrivateConnectivityIn"]
                ).optional(),
                "displayName": t.string(),
                "gcsProfile": t.proxy(renames["GcsProfileIn"]).optional(),
                "staticServiceIpConnectivity": t.proxy(
                    renames["StaticServiceIpConnectivityIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "postgresqlProfile": t.proxy(renames["PostgresqlProfileIn"]).optional(),
                "oracleProfile": t.proxy(renames["OracleProfileIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesPatch"] = datastream.patch(
        "v1/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "force": t.boolean().optional(),
                "requestId": t.string().optional(),
                "forwardSshConnectivity": t.proxy(
                    renames["ForwardSshTunnelConnectivityIn"]
                ).optional(),
                "mysqlProfile": t.proxy(renames["MysqlProfileIn"]).optional(),
                "bigqueryProfile": t.proxy(renames["BigQueryProfileIn"]).optional(),
                "privateConnectivity": t.proxy(
                    renames["PrivateConnectivityIn"]
                ).optional(),
                "displayName": t.string(),
                "gcsProfile": t.proxy(renames["GcsProfileIn"]).optional(),
                "staticServiceIpConnectivity": t.proxy(
                    renames["StaticServiceIpConnectivityIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "postgresqlProfile": t.proxy(renames["PostgresqlProfileIn"]).optional(),
                "oracleProfile": t.proxy(renames["OracleProfileIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
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
    functions["projectsLocationsStreamsDelete"] = datastream.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["StreamOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsPatch"] = datastream.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["StreamOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsList"] = datastream.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["StreamOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsCreate"] = datastream.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["StreamOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsGet"] = datastream.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["StreamOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsObjectsStopBackfillJob"] = datastream.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["StreamObjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsObjectsLookup"] = datastream.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["StreamObjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsObjectsList"] = datastream.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["StreamObjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsObjectsStartBackfillJob"] = datastream.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["StreamObjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsObjectsGet"] = datastream.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["StreamObjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsCreate"] = datastream.get(
        "v1/{parent}/privateConnections",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPrivateConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsDelete"] = datastream.get(
        "v1/{parent}/privateConnections",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPrivateConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsGet"] = datastream.get(
        "v1/{parent}/privateConnections",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPrivateConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsList"] = datastream.get(
        "v1/{parent}/privateConnections",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPrivateConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsRoutesList"] = datastream.post(
        "v1/{parent}/routes",
        t.struct(
            {
                "parent": t.string(),
                "routeId": t.string(),
                "requestId": t.string().optional(),
                "destinationAddress": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "destinationPort": t.integer().optional(),
                "displayName": t.string(),
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
                "parent": t.string(),
                "routeId": t.string(),
                "requestId": t.string().optional(),
                "destinationAddress": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "destinationPort": t.integer().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsRoutesDelete"] = datastream.post(
        "v1/{parent}/routes",
        t.struct(
            {
                "parent": t.string(),
                "routeId": t.string(),
                "requestId": t.string().optional(),
                "destinationAddress": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "destinationPort": t.integer().optional(),
                "displayName": t.string(),
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
                "parent": t.string(),
                "routeId": t.string(),
                "requestId": t.string().optional(),
                "destinationAddress": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "destinationPort": t.integer().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="datastream", renames=renames, types=types, functions=functions
    )
