from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_datastream():
    datastream = HTTPRuntime("https://datastream.googleapis.com/")

    renames = {
        "ErrorResponse": "_datastream_1_ErrorResponse",
        "ValidationIn": "_datastream_2_ValidationIn",
        "ValidationOut": "_datastream_3_ValidationOut",
        "GcsProfileIn": "_datastream_4_GcsProfileIn",
        "GcsProfileOut": "_datastream_5_GcsProfileOut",
        "AvroFileFormatIn": "_datastream_6_AvroFileFormatIn",
        "AvroFileFormatOut": "_datastream_7_AvroFileFormatOut",
        "MysqlSslConfigIn": "_datastream_8_MysqlSslConfigIn",
        "MysqlSslConfigOut": "_datastream_9_MysqlSslConfigOut",
        "ListLocationsResponseIn": "_datastream_10_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_datastream_11_ListLocationsResponseOut",
        "ListPrivateConnectionsResponseIn": "_datastream_12_ListPrivateConnectionsResponseIn",
        "ListPrivateConnectionsResponseOut": "_datastream_13_ListPrivateConnectionsResponseOut",
        "OracleProfileIn": "_datastream_14_OracleProfileIn",
        "OracleProfileOut": "_datastream_15_OracleProfileOut",
        "ListRoutesResponseIn": "_datastream_16_ListRoutesResponseIn",
        "ListRoutesResponseOut": "_datastream_17_ListRoutesResponseOut",
        "StartBackfillJobRequestIn": "_datastream_18_StartBackfillJobRequestIn",
        "StartBackfillJobRequestOut": "_datastream_19_StartBackfillJobRequestOut",
        "PostgresqlProfileIn": "_datastream_20_PostgresqlProfileIn",
        "PostgresqlProfileOut": "_datastream_21_PostgresqlProfileOut",
        "PostgresqlSchemaIn": "_datastream_22_PostgresqlSchemaIn",
        "PostgresqlSchemaOut": "_datastream_23_PostgresqlSchemaOut",
        "SourceConfigIn": "_datastream_24_SourceConfigIn",
        "SourceConfigOut": "_datastream_25_SourceConfigOut",
        "ValidationMessageIn": "_datastream_26_ValidationMessageIn",
        "ValidationMessageOut": "_datastream_27_ValidationMessageOut",
        "MysqlTableIn": "_datastream_28_MysqlTableIn",
        "MysqlTableOut": "_datastream_29_MysqlTableOut",
        "MysqlDatabaseIn": "_datastream_30_MysqlDatabaseIn",
        "MysqlDatabaseOut": "_datastream_31_MysqlDatabaseOut",
        "ListStreamObjectsResponseIn": "_datastream_32_ListStreamObjectsResponseIn",
        "ListStreamObjectsResponseOut": "_datastream_33_ListStreamObjectsResponseOut",
        "StatusIn": "_datastream_34_StatusIn",
        "StatusOut": "_datastream_35_StatusOut",
        "JsonFileFormatIn": "_datastream_36_JsonFileFormatIn",
        "JsonFileFormatOut": "_datastream_37_JsonFileFormatOut",
        "ListOperationsResponseIn": "_datastream_38_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_datastream_39_ListOperationsResponseOut",
        "MysqlSourceConfigIn": "_datastream_40_MysqlSourceConfigIn",
        "MysqlSourceConfigOut": "_datastream_41_MysqlSourceConfigOut",
        "PrivateConnectionIn": "_datastream_42_PrivateConnectionIn",
        "PrivateConnectionOut": "_datastream_43_PrivateConnectionOut",
        "StopBackfillJobResponseIn": "_datastream_44_StopBackfillJobResponseIn",
        "StopBackfillJobResponseOut": "_datastream_45_StopBackfillJobResponseOut",
        "ListConnectionProfilesResponseIn": "_datastream_46_ListConnectionProfilesResponseIn",
        "ListConnectionProfilesResponseOut": "_datastream_47_ListConnectionProfilesResponseOut",
        "ForwardSshTunnelConnectivityIn": "_datastream_48_ForwardSshTunnelConnectivityIn",
        "ForwardSshTunnelConnectivityOut": "_datastream_49_ForwardSshTunnelConnectivityOut",
        "PostgresqlObjectIdentifierIn": "_datastream_50_PostgresqlObjectIdentifierIn",
        "PostgresqlObjectIdentifierOut": "_datastream_51_PostgresqlObjectIdentifierOut",
        "DiscoverConnectionProfileResponseIn": "_datastream_52_DiscoverConnectionProfileResponseIn",
        "DiscoverConnectionProfileResponseOut": "_datastream_53_DiscoverConnectionProfileResponseOut",
        "VpcPeeringConfigIn": "_datastream_54_VpcPeeringConfigIn",
        "VpcPeeringConfigOut": "_datastream_55_VpcPeeringConfigOut",
        "DatasetTemplateIn": "_datastream_56_DatasetTemplateIn",
        "DatasetTemplateOut": "_datastream_57_DatasetTemplateOut",
        "DiscoverConnectionProfileRequestIn": "_datastream_58_DiscoverConnectionProfileRequestIn",
        "DiscoverConnectionProfileRequestOut": "_datastream_59_DiscoverConnectionProfileRequestOut",
        "OracleSourceConfigIn": "_datastream_60_OracleSourceConfigIn",
        "OracleSourceConfigOut": "_datastream_61_OracleSourceConfigOut",
        "OracleObjectIdentifierIn": "_datastream_62_OracleObjectIdentifierIn",
        "OracleObjectIdentifierOut": "_datastream_63_OracleObjectIdentifierOut",
        "OracleTableIn": "_datastream_64_OracleTableIn",
        "OracleTableOut": "_datastream_65_OracleTableOut",
        "ConnectionProfileIn": "_datastream_66_ConnectionProfileIn",
        "ConnectionProfileOut": "_datastream_67_ConnectionProfileOut",
        "StaticServiceIpConnectivityIn": "_datastream_68_StaticServiceIpConnectivityIn",
        "StaticServiceIpConnectivityOut": "_datastream_69_StaticServiceIpConnectivityOut",
        "StartBackfillJobResponseIn": "_datastream_70_StartBackfillJobResponseIn",
        "StartBackfillJobResponseOut": "_datastream_71_StartBackfillJobResponseOut",
        "SourceObjectIdentifierIn": "_datastream_72_SourceObjectIdentifierIn",
        "SourceObjectIdentifierOut": "_datastream_73_SourceObjectIdentifierOut",
        "BigQueryDestinationConfigIn": "_datastream_74_BigQueryDestinationConfigIn",
        "BigQueryDestinationConfigOut": "_datastream_75_BigQueryDestinationConfigOut",
        "DestinationConfigIn": "_datastream_76_DestinationConfigIn",
        "DestinationConfigOut": "_datastream_77_DestinationConfigOut",
        "BackfillNoneStrategyIn": "_datastream_78_BackfillNoneStrategyIn",
        "BackfillNoneStrategyOut": "_datastream_79_BackfillNoneStrategyOut",
        "MysqlObjectIdentifierIn": "_datastream_80_MysqlObjectIdentifierIn",
        "MysqlObjectIdentifierOut": "_datastream_81_MysqlObjectIdentifierOut",
        "BackfillAllStrategyIn": "_datastream_82_BackfillAllStrategyIn",
        "BackfillAllStrategyOut": "_datastream_83_BackfillAllStrategyOut",
        "ErrorIn": "_datastream_84_ErrorIn",
        "ErrorOut": "_datastream_85_ErrorOut",
        "PostgresqlRdbmsIn": "_datastream_86_PostgresqlRdbmsIn",
        "PostgresqlRdbmsOut": "_datastream_87_PostgresqlRdbmsOut",
        "DropLargeObjectsIn": "_datastream_88_DropLargeObjectsIn",
        "DropLargeObjectsOut": "_datastream_89_DropLargeObjectsOut",
        "SourceHierarchyDatasetsIn": "_datastream_90_SourceHierarchyDatasetsIn",
        "SourceHierarchyDatasetsOut": "_datastream_91_SourceHierarchyDatasetsOut",
        "MysqlColumnIn": "_datastream_92_MysqlColumnIn",
        "MysqlColumnOut": "_datastream_93_MysqlColumnOut",
        "PostgresqlTableIn": "_datastream_94_PostgresqlTableIn",
        "PostgresqlTableOut": "_datastream_95_PostgresqlTableOut",
        "EmptyIn": "_datastream_96_EmptyIn",
        "EmptyOut": "_datastream_97_EmptyOut",
        "RouteIn": "_datastream_98_RouteIn",
        "RouteOut": "_datastream_99_RouteOut",
        "MysqlRdbmsIn": "_datastream_100_MysqlRdbmsIn",
        "MysqlRdbmsOut": "_datastream_101_MysqlRdbmsOut",
        "ListStreamsResponseIn": "_datastream_102_ListStreamsResponseIn",
        "ListStreamsResponseOut": "_datastream_103_ListStreamsResponseOut",
        "LookupStreamObjectRequestIn": "_datastream_104_LookupStreamObjectRequestIn",
        "LookupStreamObjectRequestOut": "_datastream_105_LookupStreamObjectRequestOut",
        "StreamObjectIn": "_datastream_106_StreamObjectIn",
        "StreamObjectOut": "_datastream_107_StreamObjectOut",
        "OracleSchemaIn": "_datastream_108_OracleSchemaIn",
        "OracleSchemaOut": "_datastream_109_OracleSchemaOut",
        "OperationMetadataIn": "_datastream_110_OperationMetadataIn",
        "OperationMetadataOut": "_datastream_111_OperationMetadataOut",
        "ValidationResultIn": "_datastream_112_ValidationResultIn",
        "ValidationResultOut": "_datastream_113_ValidationResultOut",
        "PostgresqlColumnIn": "_datastream_114_PostgresqlColumnIn",
        "PostgresqlColumnOut": "_datastream_115_PostgresqlColumnOut",
        "StreamLargeObjectsIn": "_datastream_116_StreamLargeObjectsIn",
        "StreamLargeObjectsOut": "_datastream_117_StreamLargeObjectsOut",
        "LocationIn": "_datastream_118_LocationIn",
        "LocationOut": "_datastream_119_LocationOut",
        "CancelOperationRequestIn": "_datastream_120_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_datastream_121_CancelOperationRequestOut",
        "OperationIn": "_datastream_122_OperationIn",
        "OperationOut": "_datastream_123_OperationOut",
        "GcsDestinationConfigIn": "_datastream_124_GcsDestinationConfigIn",
        "GcsDestinationConfigOut": "_datastream_125_GcsDestinationConfigOut",
        "BackfillJobIn": "_datastream_126_BackfillJobIn",
        "BackfillJobOut": "_datastream_127_BackfillJobOut",
        "SingleTargetDatasetIn": "_datastream_128_SingleTargetDatasetIn",
        "SingleTargetDatasetOut": "_datastream_129_SingleTargetDatasetOut",
        "StopBackfillJobRequestIn": "_datastream_130_StopBackfillJobRequestIn",
        "StopBackfillJobRequestOut": "_datastream_131_StopBackfillJobRequestOut",
        "PostgresqlSourceConfigIn": "_datastream_132_PostgresqlSourceConfigIn",
        "PostgresqlSourceConfigOut": "_datastream_133_PostgresqlSourceConfigOut",
        "MysqlProfileIn": "_datastream_134_MysqlProfileIn",
        "MysqlProfileOut": "_datastream_135_MysqlProfileOut",
        "OracleRdbmsIn": "_datastream_136_OracleRdbmsIn",
        "OracleRdbmsOut": "_datastream_137_OracleRdbmsOut",
        "OracleColumnIn": "_datastream_138_OracleColumnIn",
        "OracleColumnOut": "_datastream_139_OracleColumnOut",
        "PrivateConnectivityIn": "_datastream_140_PrivateConnectivityIn",
        "PrivateConnectivityOut": "_datastream_141_PrivateConnectivityOut",
        "FetchStaticIpsResponseIn": "_datastream_142_FetchStaticIpsResponseIn",
        "FetchStaticIpsResponseOut": "_datastream_143_FetchStaticIpsResponseOut",
        "BigQueryProfileIn": "_datastream_144_BigQueryProfileIn",
        "BigQueryProfileOut": "_datastream_145_BigQueryProfileOut",
        "StreamIn": "_datastream_146_StreamIn",
        "StreamOut": "_datastream_147_StreamOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ValidationIn"] = t.struct(
        {
            "message": t.array(t.proxy(renames["ValidationMessageIn"])).optional(),
            "code": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ValidationIn"])
    types["ValidationOut"] = t.struct(
        {
            "message": t.array(t.proxy(renames["ValidationMessageOut"])).optional(),
            "code": t.string().optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationOut"])
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
    types["AvroFileFormatIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AvroFileFormatIn"]
    )
    types["AvroFileFormatOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AvroFileFormatOut"])
    types["MysqlSslConfigIn"] = t.struct(
        {
            "clientKey": t.string().optional(),
            "clientCertificate": t.string().optional(),
            "caCertificate": t.string().optional(),
        }
    ).named(renames["MysqlSslConfigIn"])
    types["MysqlSslConfigOut"] = t.struct(
        {
            "caCertificateSet": t.boolean().optional(),
            "clientKeySet": t.boolean().optional(),
            "clientKey": t.string().optional(),
            "clientCertificate": t.string().optional(),
            "caCertificate": t.string().optional(),
            "clientCertificateSet": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MysqlSslConfigOut"])
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
    types["OracleProfileIn"] = t.struct(
        {
            "hostname": t.string(),
            "username": t.string(),
            "port": t.integer().optional(),
            "password": t.string(),
            "connectionAttributes": t.struct({"_": t.string().optional()}).optional(),
            "databaseService": t.string(),
        }
    ).named(renames["OracleProfileIn"])
    types["OracleProfileOut"] = t.struct(
        {
            "hostname": t.string(),
            "username": t.string(),
            "port": t.integer().optional(),
            "password": t.string(),
            "connectionAttributes": t.struct({"_": t.string().optional()}).optional(),
            "databaseService": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OracleProfileOut"])
    types["ListRoutesResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "routes": t.array(t.proxy(renames["RouteIn"])).optional(),
        }
    ).named(renames["ListRoutesResponseIn"])
    types["ListRoutesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "routes": t.array(t.proxy(renames["RouteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRoutesResponseOut"])
    types["StartBackfillJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StartBackfillJobRequestIn"]
    )
    types["StartBackfillJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StartBackfillJobRequestOut"])
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
    types["ValidationMessageIn"] = t.struct(
        {
            "code": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "level": t.string().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["ValidationMessageIn"])
    types["ValidationMessageOut"] = t.struct(
        {
            "code": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "level": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationMessageOut"])
    types["MysqlTableIn"] = t.struct(
        {
            "mysqlColumns": t.array(t.proxy(renames["MysqlColumnIn"])).optional(),
            "table": t.string().optional(),
        }
    ).named(renames["MysqlTableIn"])
    types["MysqlTableOut"] = t.struct(
        {
            "mysqlColumns": t.array(t.proxy(renames["MysqlColumnOut"])).optional(),
            "table": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MysqlTableOut"])
    types["MysqlDatabaseIn"] = t.struct(
        {
            "mysqlTables": t.array(t.proxy(renames["MysqlTableIn"])).optional(),
            "database": t.string().optional(),
        }
    ).named(renames["MysqlDatabaseIn"])
    types["MysqlDatabaseOut"] = t.struct(
        {
            "mysqlTables": t.array(t.proxy(renames["MysqlTableOut"])).optional(),
            "database": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MysqlDatabaseOut"])
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
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["JsonFileFormatIn"] = t.struct(
        {
            "schemaFileFormat": t.string().optional(),
            "compression": t.string().optional(),
        }
    ).named(renames["JsonFileFormatIn"])
    types["JsonFileFormatOut"] = t.struct(
        {
            "schemaFileFormat": t.string().optional(),
            "compression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JsonFileFormatOut"])
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
    types["MysqlSourceConfigIn"] = t.struct(
        {
            "maxConcurrentBackfillTasks": t.integer().optional(),
            "includeObjects": t.proxy(renames["MysqlRdbmsIn"]).optional(),
            "maxConcurrentCdcTasks": t.integer().optional(),
            "excludeObjects": t.proxy(renames["MysqlRdbmsIn"]).optional(),
        }
    ).named(renames["MysqlSourceConfigIn"])
    types["MysqlSourceConfigOut"] = t.struct(
        {
            "maxConcurrentBackfillTasks": t.integer().optional(),
            "includeObjects": t.proxy(renames["MysqlRdbmsOut"]).optional(),
            "maxConcurrentCdcTasks": t.integer().optional(),
            "excludeObjects": t.proxy(renames["MysqlRdbmsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MysqlSourceConfigOut"])
    types["PrivateConnectionIn"] = t.struct(
        {
            "vpcPeeringConfig": t.proxy(renames["VpcPeeringConfigIn"]).optional(),
            "displayName": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PrivateConnectionIn"])
    types["PrivateConnectionOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "vpcPeeringConfig": t.proxy(renames["VpcPeeringConfigOut"]).optional(),
            "state": t.string().optional(),
            "displayName": t.string(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["PrivateConnectionOut"])
    types["StopBackfillJobResponseIn"] = t.struct(
        {"object": t.proxy(renames["StreamObjectIn"]).optional()}
    ).named(renames["StopBackfillJobResponseIn"])
    types["StopBackfillJobResponseOut"] = t.struct(
        {
            "object": t.proxy(renames["StreamObjectOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StopBackfillJobResponseOut"])
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
    types["ForwardSshTunnelConnectivityIn"] = t.struct(
        {
            "port": t.integer().optional(),
            "username": t.string(),
            "hostname": t.string(),
            "privateKey": t.string().optional(),
            "password": t.string().optional(),
        }
    ).named(renames["ForwardSshTunnelConnectivityIn"])
    types["ForwardSshTunnelConnectivityOut"] = t.struct(
        {
            "port": t.integer().optional(),
            "username": t.string(),
            "hostname": t.string(),
            "privateKey": t.string().optional(),
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
    types["VpcPeeringConfigIn"] = t.struct(
        {"subnet": t.string(), "vpc": t.string()}
    ).named(renames["VpcPeeringConfigIn"])
    types["VpcPeeringConfigOut"] = t.struct(
        {
            "subnet": t.string(),
            "vpc": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VpcPeeringConfigOut"])
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
    types["DiscoverConnectionProfileRequestIn"] = t.struct(
        {
            "hierarchyDepth": t.integer().optional(),
            "connectionProfile": t.proxy(renames["ConnectionProfileIn"]).optional(),
            "postgresqlRdbms": t.proxy(renames["PostgresqlRdbmsIn"]).optional(),
            "oracleRdbms": t.proxy(renames["OracleRdbmsIn"]).optional(),
            "connectionProfileName": t.string().optional(),
            "fullHierarchy": t.boolean().optional(),
            "mysqlRdbms": t.proxy(renames["MysqlRdbmsIn"]).optional(),
        }
    ).named(renames["DiscoverConnectionProfileRequestIn"])
    types["DiscoverConnectionProfileRequestOut"] = t.struct(
        {
            "hierarchyDepth": t.integer().optional(),
            "connectionProfile": t.proxy(renames["ConnectionProfileOut"]).optional(),
            "postgresqlRdbms": t.proxy(renames["PostgresqlRdbmsOut"]).optional(),
            "oracleRdbms": t.proxy(renames["OracleRdbmsOut"]).optional(),
            "connectionProfileName": t.string().optional(),
            "fullHierarchy": t.boolean().optional(),
            "mysqlRdbms": t.proxy(renames["MysqlRdbmsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiscoverConnectionProfileRequestOut"])
    types["OracleSourceConfigIn"] = t.struct(
        {
            "streamLargeObjects": t.proxy(renames["StreamLargeObjectsIn"]).optional(),
            "excludeObjects": t.proxy(renames["OracleRdbmsIn"]).optional(),
            "maxConcurrentBackfillTasks": t.integer().optional(),
            "maxConcurrentCdcTasks": t.integer().optional(),
            "dropLargeObjects": t.proxy(renames["DropLargeObjectsIn"]).optional(),
            "includeObjects": t.proxy(renames["OracleRdbmsIn"]).optional(),
        }
    ).named(renames["OracleSourceConfigIn"])
    types["OracleSourceConfigOut"] = t.struct(
        {
            "streamLargeObjects": t.proxy(renames["StreamLargeObjectsOut"]).optional(),
            "excludeObjects": t.proxy(renames["OracleRdbmsOut"]).optional(),
            "maxConcurrentBackfillTasks": t.integer().optional(),
            "maxConcurrentCdcTasks": t.integer().optional(),
            "dropLargeObjects": t.proxy(renames["DropLargeObjectsOut"]).optional(),
            "includeObjects": t.proxy(renames["OracleRdbmsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OracleSourceConfigOut"])
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
    types["ConnectionProfileIn"] = t.struct(
        {
            "mysqlProfile": t.proxy(renames["MysqlProfileIn"]).optional(),
            "bigqueryProfile": t.proxy(renames["BigQueryProfileIn"]).optional(),
            "displayName": t.string(),
            "oracleProfile": t.proxy(renames["OracleProfileIn"]).optional(),
            "privateConnectivity": t.proxy(renames["PrivateConnectivityIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "gcsProfile": t.proxy(renames["GcsProfileIn"]).optional(),
            "staticServiceIpConnectivity": t.proxy(
                renames["StaticServiceIpConnectivityIn"]
            ).optional(),
            "postgresqlProfile": t.proxy(renames["PostgresqlProfileIn"]).optional(),
            "forwardSshConnectivity": t.proxy(
                renames["ForwardSshTunnelConnectivityIn"]
            ).optional(),
        }
    ).named(renames["ConnectionProfileIn"])
    types["ConnectionProfileOut"] = t.struct(
        {
            "name": t.string().optional(),
            "mysqlProfile": t.proxy(renames["MysqlProfileOut"]).optional(),
            "bigqueryProfile": t.proxy(renames["BigQueryProfileOut"]).optional(),
            "displayName": t.string(),
            "oracleProfile": t.proxy(renames["OracleProfileOut"]).optional(),
            "privateConnectivity": t.proxy(
                renames["PrivateConnectivityOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "gcsProfile": t.proxy(renames["GcsProfileOut"]).optional(),
            "updateTime": t.string().optional(),
            "staticServiceIpConnectivity": t.proxy(
                renames["StaticServiceIpConnectivityOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "postgresqlProfile": t.proxy(renames["PostgresqlProfileOut"]).optional(),
            "forwardSshConnectivity": t.proxy(
                renames["ForwardSshTunnelConnectivityOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionProfileOut"])
    types["StaticServiceIpConnectivityIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["StaticServiceIpConnectivityIn"])
    types["StaticServiceIpConnectivityOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StaticServiceIpConnectivityOut"])
    types["StartBackfillJobResponseIn"] = t.struct(
        {"object": t.proxy(renames["StreamObjectIn"]).optional()}
    ).named(renames["StartBackfillJobResponseIn"])
    types["StartBackfillJobResponseOut"] = t.struct(
        {
            "object": t.proxy(renames["StreamObjectOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartBackfillJobResponseOut"])
    types["SourceObjectIdentifierIn"] = t.struct(
        {
            "oracleIdentifier": t.proxy(renames["OracleObjectIdentifierIn"]).optional(),
            "mysqlIdentifier": t.proxy(renames["MysqlObjectIdentifierIn"]).optional(),
            "postgresqlIdentifier": t.proxy(
                renames["PostgresqlObjectIdentifierIn"]
            ).optional(),
        }
    ).named(renames["SourceObjectIdentifierIn"])
    types["SourceObjectIdentifierOut"] = t.struct(
        {
            "oracleIdentifier": t.proxy(
                renames["OracleObjectIdentifierOut"]
            ).optional(),
            "mysqlIdentifier": t.proxy(renames["MysqlObjectIdentifierOut"]).optional(),
            "postgresqlIdentifier": t.proxy(
                renames["PostgresqlObjectIdentifierOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceObjectIdentifierOut"])
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
    types["DestinationConfigIn"] = t.struct(
        {
            "gcsDestinationConfig": t.proxy(
                renames["GcsDestinationConfigIn"]
            ).optional(),
            "bigqueryDestinationConfig": t.proxy(
                renames["BigQueryDestinationConfigIn"]
            ).optional(),
            "destinationConnectionProfile": t.string(),
        }
    ).named(renames["DestinationConfigIn"])
    types["DestinationConfigOut"] = t.struct(
        {
            "gcsDestinationConfig": t.proxy(
                renames["GcsDestinationConfigOut"]
            ).optional(),
            "bigqueryDestinationConfig": t.proxy(
                renames["BigQueryDestinationConfigOut"]
            ).optional(),
            "destinationConnectionProfile": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationConfigOut"])
    types["BackfillNoneStrategyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["BackfillNoneStrategyIn"]
    )
    types["BackfillNoneStrategyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["BackfillNoneStrategyOut"])
    types["MysqlObjectIdentifierIn"] = t.struct(
        {"database": t.string(), "table": t.string()}
    ).named(renames["MysqlObjectIdentifierIn"])
    types["MysqlObjectIdentifierOut"] = t.struct(
        {
            "database": t.string(),
            "table": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MysqlObjectIdentifierOut"])
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
    types["ErrorIn"] = t.struct(
        {
            "errorUuid": t.string().optional(),
            "message": t.string().optional(),
            "reason": t.string().optional(),
            "errorTime": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ErrorIn"])
    types["ErrorOut"] = t.struct(
        {
            "errorUuid": t.string().optional(),
            "message": t.string().optional(),
            "reason": t.string().optional(),
            "errorTime": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorOut"])
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
    types["DropLargeObjectsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DropLargeObjectsIn"]
    )
    types["DropLargeObjectsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DropLargeObjectsOut"])
    types["SourceHierarchyDatasetsIn"] = t.struct(
        {"datasetTemplate": t.proxy(renames["DatasetTemplateIn"]).optional()}
    ).named(renames["SourceHierarchyDatasetsIn"])
    types["SourceHierarchyDatasetsOut"] = t.struct(
        {
            "datasetTemplate": t.proxy(renames["DatasetTemplateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceHierarchyDatasetsOut"])
    types["MysqlColumnIn"] = t.struct(
        {
            "length": t.integer().optional(),
            "dataType": t.string().optional(),
            "column": t.string().optional(),
            "nullable": t.boolean().optional(),
            "ordinalPosition": t.integer().optional(),
            "primaryKey": t.boolean().optional(),
            "collation": t.string().optional(),
        }
    ).named(renames["MysqlColumnIn"])
    types["MysqlColumnOut"] = t.struct(
        {
            "length": t.integer().optional(),
            "dataType": t.string().optional(),
            "column": t.string().optional(),
            "nullable": t.boolean().optional(),
            "ordinalPosition": t.integer().optional(),
            "primaryKey": t.boolean().optional(),
            "collation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MysqlColumnOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["RouteIn"] = t.struct(
        {
            "destinationPort": t.integer().optional(),
            "displayName": t.string(),
            "destinationAddress": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["RouteIn"])
    types["RouteOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "destinationPort": t.integer().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string(),
            "destinationAddress": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RouteOut"])
    types["MysqlRdbmsIn"] = t.struct(
        {"mysqlDatabases": t.array(t.proxy(renames["MysqlDatabaseIn"])).optional()}
    ).named(renames["MysqlRdbmsIn"])
    types["MysqlRdbmsOut"] = t.struct(
        {
            "mysqlDatabases": t.array(t.proxy(renames["MysqlDatabaseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MysqlRdbmsOut"])
    types["ListStreamsResponseIn"] = t.struct(
        {
            "streams": t.array(t.proxy(renames["StreamIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListStreamsResponseIn"])
    types["ListStreamsResponseOut"] = t.struct(
        {
            "streams": t.array(t.proxy(renames["StreamOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListStreamsResponseOut"])
    types["LookupStreamObjectRequestIn"] = t.struct(
        {"sourceObjectIdentifier": t.proxy(renames["SourceObjectIdentifierIn"])}
    ).named(renames["LookupStreamObjectRequestIn"])
    types["LookupStreamObjectRequestOut"] = t.struct(
        {
            "sourceObjectIdentifier": t.proxy(renames["SourceObjectIdentifierOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LookupStreamObjectRequestOut"])
    types["StreamObjectIn"] = t.struct(
        {
            "displayName": t.string(),
            "sourceObject": t.proxy(renames["SourceObjectIdentifierIn"]).optional(),
            "backfillJob": t.proxy(renames["BackfillJobIn"]).optional(),
        }
    ).named(renames["StreamObjectIn"])
    types["StreamObjectOut"] = t.struct(
        {
            "displayName": t.string(),
            "sourceObject": t.proxy(renames["SourceObjectIdentifierOut"]).optional(),
            "backfillJob": t.proxy(renames["BackfillJobOut"]).optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "errors": t.array(t.proxy(renames["ErrorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamObjectOut"])
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
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "statusMessage": t.string().optional(),
            "validationResult": t.proxy(renames["ValidationResultOut"]).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["ValidationResultIn"] = t.struct(
        {"validations": t.array(t.proxy(renames["ValidationIn"])).optional()}
    ).named(renames["ValidationResultIn"])
    types["ValidationResultOut"] = t.struct(
        {
            "validations": t.array(t.proxy(renames["ValidationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationResultOut"])
    types["PostgresqlColumnIn"] = t.struct(
        {
            "scale": t.integer().optional(),
            "primaryKey": t.boolean().optional(),
            "column": t.string().optional(),
            "nullable": t.boolean().optional(),
            "length": t.integer().optional(),
            "precision": t.integer().optional(),
            "ordinalPosition": t.integer().optional(),
            "dataType": t.string().optional(),
        }
    ).named(renames["PostgresqlColumnIn"])
    types["PostgresqlColumnOut"] = t.struct(
        {
            "scale": t.integer().optional(),
            "primaryKey": t.boolean().optional(),
            "column": t.string().optional(),
            "nullable": t.boolean().optional(),
            "length": t.integer().optional(),
            "precision": t.integer().optional(),
            "ordinalPosition": t.integer().optional(),
            "dataType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostgresqlColumnOut"])
    types["StreamLargeObjectsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StreamLargeObjectsIn"]
    )
    types["StreamLargeObjectsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StreamLargeObjectsOut"])
    types["LocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["GcsDestinationConfigIn"] = t.struct(
        {
            "avroFileFormat": t.proxy(renames["AvroFileFormatIn"]).optional(),
            "path": t.string().optional(),
            "fileRotationMb": t.integer().optional(),
            "fileRotationInterval": t.string().optional(),
            "jsonFileFormat": t.proxy(renames["JsonFileFormatIn"]).optional(),
        }
    ).named(renames["GcsDestinationConfigIn"])
    types["GcsDestinationConfigOut"] = t.struct(
        {
            "avroFileFormat": t.proxy(renames["AvroFileFormatOut"]).optional(),
            "path": t.string().optional(),
            "fileRotationMb": t.integer().optional(),
            "fileRotationInterval": t.string().optional(),
            "jsonFileFormat": t.proxy(renames["JsonFileFormatOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsDestinationConfigOut"])
    types["BackfillJobIn"] = t.struct({"trigger": t.string().optional()}).named(
        renames["BackfillJobIn"]
    )
    types["BackfillJobOut"] = t.struct(
        {
            "lastEndTime": t.string().optional(),
            "trigger": t.string().optional(),
            "state": t.string().optional(),
            "errors": t.array(t.proxy(renames["ErrorOut"])).optional(),
            "lastStartTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackfillJobOut"])
    types["SingleTargetDatasetIn"] = t.struct(
        {"datasetId": t.string().optional()}
    ).named(renames["SingleTargetDatasetIn"])
    types["SingleTargetDatasetOut"] = t.struct(
        {
            "datasetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SingleTargetDatasetOut"])
    types["StopBackfillJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StopBackfillJobRequestIn"]
    )
    types["StopBackfillJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StopBackfillJobRequestOut"])
    types["PostgresqlSourceConfigIn"] = t.struct(
        {
            "excludeObjects": t.proxy(renames["PostgresqlRdbmsIn"]).optional(),
            "publication": t.string(),
            "replicationSlot": t.string(),
            "maxConcurrentBackfillTasks": t.integer().optional(),
            "includeObjects": t.proxy(renames["PostgresqlRdbmsIn"]).optional(),
        }
    ).named(renames["PostgresqlSourceConfigIn"])
    types["PostgresqlSourceConfigOut"] = t.struct(
        {
            "excludeObjects": t.proxy(renames["PostgresqlRdbmsOut"]).optional(),
            "publication": t.string(),
            "replicationSlot": t.string(),
            "maxConcurrentBackfillTasks": t.integer().optional(),
            "includeObjects": t.proxy(renames["PostgresqlRdbmsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostgresqlSourceConfigOut"])
    types["MysqlProfileIn"] = t.struct(
        {
            "hostname": t.string(),
            "port": t.integer().optional(),
            "sslConfig": t.proxy(renames["MysqlSslConfigIn"]).optional(),
            "username": t.string(),
            "password": t.string(),
        }
    ).named(renames["MysqlProfileIn"])
    types["MysqlProfileOut"] = t.struct(
        {
            "hostname": t.string(),
            "port": t.integer().optional(),
            "sslConfig": t.proxy(renames["MysqlSslConfigOut"]).optional(),
            "username": t.string(),
            "password": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MysqlProfileOut"])
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
            "precision": t.integer().optional(),
            "length": t.integer().optional(),
            "scale": t.integer().optional(),
            "ordinalPosition": t.integer().optional(),
            "encoding": t.string().optional(),
            "dataType": t.string().optional(),
            "nullable": t.boolean().optional(),
            "column": t.string().optional(),
            "primaryKey": t.boolean().optional(),
        }
    ).named(renames["OracleColumnIn"])
    types["OracleColumnOut"] = t.struct(
        {
            "precision": t.integer().optional(),
            "length": t.integer().optional(),
            "scale": t.integer().optional(),
            "ordinalPosition": t.integer().optional(),
            "encoding": t.string().optional(),
            "dataType": t.string().optional(),
            "nullable": t.boolean().optional(),
            "column": t.string().optional(),
            "primaryKey": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OracleColumnOut"])
    types["PrivateConnectivityIn"] = t.struct({"privateConnection": t.string()}).named(
        renames["PrivateConnectivityIn"]
    )
    types["PrivateConnectivityOut"] = t.struct(
        {
            "privateConnection": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateConnectivityOut"])
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
    types["BigQueryProfileIn"] = t.struct({"_": t.string().optional()}).named(
        renames["BigQueryProfileIn"]
    )
    types["BigQueryProfileOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["BigQueryProfileOut"])
    types["StreamIn"] = t.struct(
        {
            "backfillAll": t.proxy(renames["BackfillAllStrategyIn"]).optional(),
            "state": t.string().optional(),
            "customerManagedEncryptionKey": t.string().optional(),
            "backfillNone": t.proxy(renames["BackfillNoneStrategyIn"]).optional(),
            "sourceConfig": t.proxy(renames["SourceConfigIn"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "destinationConfig": t.proxy(renames["DestinationConfigIn"]),
            "displayName": t.string(),
        }
    ).named(renames["StreamIn"])
    types["StreamOut"] = t.struct(
        {
            "backfillAll": t.proxy(renames["BackfillAllStrategyOut"]).optional(),
            "state": t.string().optional(),
            "customerManagedEncryptionKey": t.string().optional(),
            "backfillNone": t.proxy(renames["BackfillNoneStrategyOut"]).optional(),
            "sourceConfig": t.proxy(renames["SourceConfigOut"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "errors": t.array(t.proxy(renames["ErrorOut"])).optional(),
            "createTime": t.string().optional(),
            "destinationConfig": t.proxy(renames["DestinationConfigOut"]),
            "name": t.string().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamOut"])

    functions = {}
    functions["projectsLocationsList"] = datastream.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFetchStaticIps"] = datastream.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = datastream.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsCreate"] = datastream.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "force": t.boolean().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsGet"] = datastream.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "force": t.boolean().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsList"] = datastream.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "force": t.boolean().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsDelete"] = datastream.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "force": t.boolean().optional(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsRoutesCreate"] = datastream.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsRoutesGet"] = datastream.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsRoutesList"] = datastream.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsRoutesDelete"] = datastream.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesPatch"] = datastream.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesGet"] = datastream.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesCreate"] = datastream.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesList"] = datastream.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesDiscover"] = datastream.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesDelete"] = datastream.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsList"] = datastream.post(
        "v1/{parent}/streams",
        t.struct(
            {
                "requestId": t.string().optional(),
                "force": t.boolean().optional(),
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "streamId": t.string(),
                "backfillAll": t.proxy(renames["BackfillAllStrategyIn"]).optional(),
                "state": t.string().optional(),
                "customerManagedEncryptionKey": t.string().optional(),
                "backfillNone": t.proxy(renames["BackfillNoneStrategyIn"]).optional(),
                "sourceConfig": t.proxy(renames["SourceConfigIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "destinationConfig": t.proxy(renames["DestinationConfigIn"]),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsDelete"] = datastream.post(
        "v1/{parent}/streams",
        t.struct(
            {
                "requestId": t.string().optional(),
                "force": t.boolean().optional(),
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "streamId": t.string(),
                "backfillAll": t.proxy(renames["BackfillAllStrategyIn"]).optional(),
                "state": t.string().optional(),
                "customerManagedEncryptionKey": t.string().optional(),
                "backfillNone": t.proxy(renames["BackfillNoneStrategyIn"]).optional(),
                "sourceConfig": t.proxy(renames["SourceConfigIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "destinationConfig": t.proxy(renames["DestinationConfigIn"]),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsGet"] = datastream.post(
        "v1/{parent}/streams",
        t.struct(
            {
                "requestId": t.string().optional(),
                "force": t.boolean().optional(),
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "streamId": t.string(),
                "backfillAll": t.proxy(renames["BackfillAllStrategyIn"]).optional(),
                "state": t.string().optional(),
                "customerManagedEncryptionKey": t.string().optional(),
                "backfillNone": t.proxy(renames["BackfillNoneStrategyIn"]).optional(),
                "sourceConfig": t.proxy(renames["SourceConfigIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "destinationConfig": t.proxy(renames["DestinationConfigIn"]),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsPatch"] = datastream.post(
        "v1/{parent}/streams",
        t.struct(
            {
                "requestId": t.string().optional(),
                "force": t.boolean().optional(),
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "streamId": t.string(),
                "backfillAll": t.proxy(renames["BackfillAllStrategyIn"]).optional(),
                "state": t.string().optional(),
                "customerManagedEncryptionKey": t.string().optional(),
                "backfillNone": t.proxy(renames["BackfillNoneStrategyIn"]).optional(),
                "sourceConfig": t.proxy(renames["SourceConfigIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "destinationConfig": t.proxy(renames["DestinationConfigIn"]),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsCreate"] = datastream.post(
        "v1/{parent}/streams",
        t.struct(
            {
                "requestId": t.string().optional(),
                "force": t.boolean().optional(),
                "parent": t.string(),
                "validateOnly": t.boolean().optional(),
                "streamId": t.string(),
                "backfillAll": t.proxy(renames["BackfillAllStrategyIn"]).optional(),
                "state": t.string().optional(),
                "customerManagedEncryptionKey": t.string().optional(),
                "backfillNone": t.proxy(renames["BackfillNoneStrategyIn"]).optional(),
                "sourceConfig": t.proxy(renames["SourceConfigIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "destinationConfig": t.proxy(renames["DestinationConfigIn"]),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsObjectsStopBackfillJob"] = datastream.post(
        "v1/{parent}/objects:lookup",
        t.struct(
            {
                "parent": t.string(),
                "sourceObjectIdentifier": t.proxy(renames["SourceObjectIdentifierIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StreamObjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsObjectsList"] = datastream.post(
        "v1/{parent}/objects:lookup",
        t.struct(
            {
                "parent": t.string(),
                "sourceObjectIdentifier": t.proxy(renames["SourceObjectIdentifierIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StreamObjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsObjectsStartBackfillJob"] = datastream.post(
        "v1/{parent}/objects:lookup",
        t.struct(
            {
                "parent": t.string(),
                "sourceObjectIdentifier": t.proxy(renames["SourceObjectIdentifierIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StreamObjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsObjectsGet"] = datastream.post(
        "v1/{parent}/objects:lookup",
        t.struct(
            {
                "parent": t.string(),
                "sourceObjectIdentifier": t.proxy(renames["SourceObjectIdentifierIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StreamObjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsObjectsLookup"] = datastream.post(
        "v1/{parent}/objects:lookup",
        t.struct(
            {
                "parent": t.string(),
                "sourceObjectIdentifier": t.proxy(renames["SourceObjectIdentifierIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StreamObjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = datastream.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = datastream.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = datastream.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = datastream.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="datastream",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
