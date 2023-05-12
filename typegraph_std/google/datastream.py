from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_datastream() -> Import:
    datastream = HTTPRuntime("https://datastream.googleapis.com/")

    renames = {
        "ErrorResponse": "_datastream_1_ErrorResponse",
        "PostgresqlTableIn": "_datastream_2_PostgresqlTableIn",
        "PostgresqlTableOut": "_datastream_3_PostgresqlTableOut",
        "DiscoverConnectionProfileResponseIn": "_datastream_4_DiscoverConnectionProfileResponseIn",
        "DiscoverConnectionProfileResponseOut": "_datastream_5_DiscoverConnectionProfileResponseOut",
        "StaticServiceIpConnectivityIn": "_datastream_6_StaticServiceIpConnectivityIn",
        "StaticServiceIpConnectivityOut": "_datastream_7_StaticServiceIpConnectivityOut",
        "AvroFileFormatIn": "_datastream_8_AvroFileFormatIn",
        "AvroFileFormatOut": "_datastream_9_AvroFileFormatOut",
        "ValidationMessageIn": "_datastream_10_ValidationMessageIn",
        "ValidationMessageOut": "_datastream_11_ValidationMessageOut",
        "DiscoverConnectionProfileRequestIn": "_datastream_12_DiscoverConnectionProfileRequestIn",
        "DiscoverConnectionProfileRequestOut": "_datastream_13_DiscoverConnectionProfileRequestOut",
        "PostgresqlSchemaIn": "_datastream_14_PostgresqlSchemaIn",
        "PostgresqlSchemaOut": "_datastream_15_PostgresqlSchemaOut",
        "StopBackfillJobResponseIn": "_datastream_16_StopBackfillJobResponseIn",
        "StopBackfillJobResponseOut": "_datastream_17_StopBackfillJobResponseOut",
        "ListConnectionProfilesResponseIn": "_datastream_18_ListConnectionProfilesResponseIn",
        "ListConnectionProfilesResponseOut": "_datastream_19_ListConnectionProfilesResponseOut",
        "RouteIn": "_datastream_20_RouteIn",
        "RouteOut": "_datastream_21_RouteOut",
        "StatusIn": "_datastream_22_StatusIn",
        "StatusOut": "_datastream_23_StatusOut",
        "OracleColumnIn": "_datastream_24_OracleColumnIn",
        "OracleColumnOut": "_datastream_25_OracleColumnOut",
        "PostgresqlColumnIn": "_datastream_26_PostgresqlColumnIn",
        "PostgresqlColumnOut": "_datastream_27_PostgresqlColumnOut",
        "OracleProfileIn": "_datastream_28_OracleProfileIn",
        "OracleProfileOut": "_datastream_29_OracleProfileOut",
        "SingleTargetDatasetIn": "_datastream_30_SingleTargetDatasetIn",
        "SingleTargetDatasetOut": "_datastream_31_SingleTargetDatasetOut",
        "MysqlRdbmsIn": "_datastream_32_MysqlRdbmsIn",
        "MysqlRdbmsOut": "_datastream_33_MysqlRdbmsOut",
        "VpcPeeringConfigIn": "_datastream_34_VpcPeeringConfigIn",
        "VpcPeeringConfigOut": "_datastream_35_VpcPeeringConfigOut",
        "ListStreamObjectsResponseIn": "_datastream_36_ListStreamObjectsResponseIn",
        "ListStreamObjectsResponseOut": "_datastream_37_ListStreamObjectsResponseOut",
        "CancelOperationRequestIn": "_datastream_38_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_datastream_39_CancelOperationRequestOut",
        "MysqlDatabaseIn": "_datastream_40_MysqlDatabaseIn",
        "MysqlDatabaseOut": "_datastream_41_MysqlDatabaseOut",
        "BigQueryProfileIn": "_datastream_42_BigQueryProfileIn",
        "BigQueryProfileOut": "_datastream_43_BigQueryProfileOut",
        "DatasetTemplateIn": "_datastream_44_DatasetTemplateIn",
        "DatasetTemplateOut": "_datastream_45_DatasetTemplateOut",
        "OracleSchemaIn": "_datastream_46_OracleSchemaIn",
        "OracleSchemaOut": "_datastream_47_OracleSchemaOut",
        "LookupStreamObjectRequestIn": "_datastream_48_LookupStreamObjectRequestIn",
        "LookupStreamObjectRequestOut": "_datastream_49_LookupStreamObjectRequestOut",
        "PrivateConnectionIn": "_datastream_50_PrivateConnectionIn",
        "PrivateConnectionOut": "_datastream_51_PrivateConnectionOut",
        "ListStreamsResponseIn": "_datastream_52_ListStreamsResponseIn",
        "ListStreamsResponseOut": "_datastream_53_ListStreamsResponseOut",
        "MysqlProfileIn": "_datastream_54_MysqlProfileIn",
        "MysqlProfileOut": "_datastream_55_MysqlProfileOut",
        "OracleObjectIdentifierIn": "_datastream_56_OracleObjectIdentifierIn",
        "OracleObjectIdentifierOut": "_datastream_57_OracleObjectIdentifierOut",
        "PostgresqlRdbmsIn": "_datastream_58_PostgresqlRdbmsIn",
        "PostgresqlRdbmsOut": "_datastream_59_PostgresqlRdbmsOut",
        "OracleTableIn": "_datastream_60_OracleTableIn",
        "OracleTableOut": "_datastream_61_OracleTableOut",
        "MysqlSourceConfigIn": "_datastream_62_MysqlSourceConfigIn",
        "MysqlSourceConfigOut": "_datastream_63_MysqlSourceConfigOut",
        "FetchStaticIpsResponseIn": "_datastream_64_FetchStaticIpsResponseIn",
        "FetchStaticIpsResponseOut": "_datastream_65_FetchStaticIpsResponseOut",
        "ForwardSshTunnelConnectivityIn": "_datastream_66_ForwardSshTunnelConnectivityIn",
        "ForwardSshTunnelConnectivityOut": "_datastream_67_ForwardSshTunnelConnectivityOut",
        "PrivateConnectivityIn": "_datastream_68_PrivateConnectivityIn",
        "PrivateConnectivityOut": "_datastream_69_PrivateConnectivityOut",
        "StreamObjectIn": "_datastream_70_StreamObjectIn",
        "StreamObjectOut": "_datastream_71_StreamObjectOut",
        "BackfillNoneStrategyIn": "_datastream_72_BackfillNoneStrategyIn",
        "BackfillNoneStrategyOut": "_datastream_73_BackfillNoneStrategyOut",
        "PostgresqlProfileIn": "_datastream_74_PostgresqlProfileIn",
        "PostgresqlProfileOut": "_datastream_75_PostgresqlProfileOut",
        "ConnectionProfileIn": "_datastream_76_ConnectionProfileIn",
        "ConnectionProfileOut": "_datastream_77_ConnectionProfileOut",
        "OracleSourceConfigIn": "_datastream_78_OracleSourceConfigIn",
        "OracleSourceConfigOut": "_datastream_79_OracleSourceConfigOut",
        "StreamIn": "_datastream_80_StreamIn",
        "StreamOut": "_datastream_81_StreamOut",
        "SourceObjectIdentifierIn": "_datastream_82_SourceObjectIdentifierIn",
        "SourceObjectIdentifierOut": "_datastream_83_SourceObjectIdentifierOut",
        "SourceHierarchyDatasetsIn": "_datastream_84_SourceHierarchyDatasetsIn",
        "SourceHierarchyDatasetsOut": "_datastream_85_SourceHierarchyDatasetsOut",
        "GcsProfileIn": "_datastream_86_GcsProfileIn",
        "GcsProfileOut": "_datastream_87_GcsProfileOut",
        "OperationMetadataIn": "_datastream_88_OperationMetadataIn",
        "OperationMetadataOut": "_datastream_89_OperationMetadataOut",
        "StreamLargeObjectsIn": "_datastream_90_StreamLargeObjectsIn",
        "StreamLargeObjectsOut": "_datastream_91_StreamLargeObjectsOut",
        "LocationIn": "_datastream_92_LocationIn",
        "LocationOut": "_datastream_93_LocationOut",
        "OperationIn": "_datastream_94_OperationIn",
        "OperationOut": "_datastream_95_OperationOut",
        "MysqlColumnIn": "_datastream_96_MysqlColumnIn",
        "MysqlColumnOut": "_datastream_97_MysqlColumnOut",
        "MysqlTableIn": "_datastream_98_MysqlTableIn",
        "MysqlTableOut": "_datastream_99_MysqlTableOut",
        "StartBackfillJobResponseIn": "_datastream_100_StartBackfillJobResponseIn",
        "StartBackfillJobResponseOut": "_datastream_101_StartBackfillJobResponseOut",
        "MysqlObjectIdentifierIn": "_datastream_102_MysqlObjectIdentifierIn",
        "MysqlObjectIdentifierOut": "_datastream_103_MysqlObjectIdentifierOut",
        "StopBackfillJobRequestIn": "_datastream_104_StopBackfillJobRequestIn",
        "StopBackfillJobRequestOut": "_datastream_105_StopBackfillJobRequestOut",
        "PostgresqlObjectIdentifierIn": "_datastream_106_PostgresqlObjectIdentifierIn",
        "PostgresqlObjectIdentifierOut": "_datastream_107_PostgresqlObjectIdentifierOut",
        "ListOperationsResponseIn": "_datastream_108_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_datastream_109_ListOperationsResponseOut",
        "ValidationResultIn": "_datastream_110_ValidationResultIn",
        "ValidationResultOut": "_datastream_111_ValidationResultOut",
        "BackfillJobIn": "_datastream_112_BackfillJobIn",
        "BackfillJobOut": "_datastream_113_BackfillJobOut",
        "ListRoutesResponseIn": "_datastream_114_ListRoutesResponseIn",
        "ListRoutesResponseOut": "_datastream_115_ListRoutesResponseOut",
        "JsonFileFormatIn": "_datastream_116_JsonFileFormatIn",
        "JsonFileFormatOut": "_datastream_117_JsonFileFormatOut",
        "ErrorIn": "_datastream_118_ErrorIn",
        "ErrorOut": "_datastream_119_ErrorOut",
        "BigQueryDestinationConfigIn": "_datastream_120_BigQueryDestinationConfigIn",
        "BigQueryDestinationConfigOut": "_datastream_121_BigQueryDestinationConfigOut",
        "StartBackfillJobRequestIn": "_datastream_122_StartBackfillJobRequestIn",
        "StartBackfillJobRequestOut": "_datastream_123_StartBackfillJobRequestOut",
        "GcsDestinationConfigIn": "_datastream_124_GcsDestinationConfigIn",
        "GcsDestinationConfigOut": "_datastream_125_GcsDestinationConfigOut",
        "EmptyIn": "_datastream_126_EmptyIn",
        "EmptyOut": "_datastream_127_EmptyOut",
        "OracleRdbmsIn": "_datastream_128_OracleRdbmsIn",
        "OracleRdbmsOut": "_datastream_129_OracleRdbmsOut",
        "SourceConfigIn": "_datastream_130_SourceConfigIn",
        "SourceConfigOut": "_datastream_131_SourceConfigOut",
        "ValidationIn": "_datastream_132_ValidationIn",
        "ValidationOut": "_datastream_133_ValidationOut",
        "ListLocationsResponseIn": "_datastream_134_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_datastream_135_ListLocationsResponseOut",
        "ListPrivateConnectionsResponseIn": "_datastream_136_ListPrivateConnectionsResponseIn",
        "ListPrivateConnectionsResponseOut": "_datastream_137_ListPrivateConnectionsResponseOut",
        "DestinationConfigIn": "_datastream_138_DestinationConfigIn",
        "DestinationConfigOut": "_datastream_139_DestinationConfigOut",
        "DropLargeObjectsIn": "_datastream_140_DropLargeObjectsIn",
        "DropLargeObjectsOut": "_datastream_141_DropLargeObjectsOut",
        "BackfillAllStrategyIn": "_datastream_142_BackfillAllStrategyIn",
        "BackfillAllStrategyOut": "_datastream_143_BackfillAllStrategyOut",
        "PostgresqlSourceConfigIn": "_datastream_144_PostgresqlSourceConfigIn",
        "PostgresqlSourceConfigOut": "_datastream_145_PostgresqlSourceConfigOut",
        "MysqlSslConfigIn": "_datastream_146_MysqlSslConfigIn",
        "MysqlSslConfigOut": "_datastream_147_MysqlSslConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["DiscoverConnectionProfileResponseIn"] = t.struct(
        {
            "postgresqlRdbms": t.proxy(renames["PostgresqlRdbmsIn"]).optional(),
            "oracleRdbms": t.proxy(renames["OracleRdbmsIn"]).optional(),
            "mysqlRdbms": t.proxy(renames["MysqlRdbmsIn"]).optional(),
        }
    ).named(renames["DiscoverConnectionProfileResponseIn"])
    types["DiscoverConnectionProfileResponseOut"] = t.struct(
        {
            "postgresqlRdbms": t.proxy(renames["PostgresqlRdbmsOut"]).optional(),
            "oracleRdbms": t.proxy(renames["OracleRdbmsOut"]).optional(),
            "mysqlRdbms": t.proxy(renames["MysqlRdbmsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiscoverConnectionProfileResponseOut"])
    types["StaticServiceIpConnectivityIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["StaticServiceIpConnectivityIn"])
    types["StaticServiceIpConnectivityOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StaticServiceIpConnectivityOut"])
    types["AvroFileFormatIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AvroFileFormatIn"]
    )
    types["AvroFileFormatOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AvroFileFormatOut"])
    types["ValidationMessageIn"] = t.struct(
        {
            "code": t.string().optional(),
            "message": t.string().optional(),
            "level": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ValidationMessageIn"])
    types["ValidationMessageOut"] = t.struct(
        {
            "code": t.string().optional(),
            "message": t.string().optional(),
            "level": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationMessageOut"])
    types["DiscoverConnectionProfileRequestIn"] = t.struct(
        {
            "mysqlRdbms": t.proxy(renames["MysqlRdbmsIn"]).optional(),
            "oracleRdbms": t.proxy(renames["OracleRdbmsIn"]).optional(),
            "fullHierarchy": t.boolean().optional(),
            "postgresqlRdbms": t.proxy(renames["PostgresqlRdbmsIn"]).optional(),
            "connectionProfile": t.proxy(renames["ConnectionProfileIn"]).optional(),
            "hierarchyDepth": t.integer().optional(),
            "connectionProfileName": t.string().optional(),
        }
    ).named(renames["DiscoverConnectionProfileRequestIn"])
    types["DiscoverConnectionProfileRequestOut"] = t.struct(
        {
            "mysqlRdbms": t.proxy(renames["MysqlRdbmsOut"]).optional(),
            "oracleRdbms": t.proxy(renames["OracleRdbmsOut"]).optional(),
            "fullHierarchy": t.boolean().optional(),
            "postgresqlRdbms": t.proxy(renames["PostgresqlRdbmsOut"]).optional(),
            "connectionProfile": t.proxy(renames["ConnectionProfileOut"]).optional(),
            "hierarchyDepth": t.integer().optional(),
            "connectionProfileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiscoverConnectionProfileRequestOut"])
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
    types["RouteIn"] = t.struct(
        {
            "destinationAddress": t.string(),
            "displayName": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "destinationPort": t.integer().optional(),
        }
    ).named(renames["RouteIn"])
    types["RouteOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "destinationAddress": t.string(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "destinationPort": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RouteOut"])
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
    types["OracleColumnIn"] = t.struct(
        {
            "encoding": t.string().optional(),
            "ordinalPosition": t.integer().optional(),
            "dataType": t.string().optional(),
            "scale": t.integer().optional(),
            "precision": t.integer().optional(),
            "length": t.integer().optional(),
            "nullable": t.boolean().optional(),
            "column": t.string().optional(),
            "primaryKey": t.boolean().optional(),
        }
    ).named(renames["OracleColumnIn"])
    types["OracleColumnOut"] = t.struct(
        {
            "encoding": t.string().optional(),
            "ordinalPosition": t.integer().optional(),
            "dataType": t.string().optional(),
            "scale": t.integer().optional(),
            "precision": t.integer().optional(),
            "length": t.integer().optional(),
            "nullable": t.boolean().optional(),
            "column": t.string().optional(),
            "primaryKey": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OracleColumnOut"])
    types["PostgresqlColumnIn"] = t.struct(
        {
            "dataType": t.string().optional(),
            "primaryKey": t.boolean().optional(),
            "column": t.string().optional(),
            "nullable": t.boolean().optional(),
            "length": t.integer().optional(),
            "scale": t.integer().optional(),
            "ordinalPosition": t.integer().optional(),
            "precision": t.integer().optional(),
        }
    ).named(renames["PostgresqlColumnIn"])
    types["PostgresqlColumnOut"] = t.struct(
        {
            "dataType": t.string().optional(),
            "primaryKey": t.boolean().optional(),
            "column": t.string().optional(),
            "nullable": t.boolean().optional(),
            "length": t.integer().optional(),
            "scale": t.integer().optional(),
            "ordinalPosition": t.integer().optional(),
            "precision": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostgresqlColumnOut"])
    types["OracleProfileIn"] = t.struct(
        {
            "port": t.integer().optional(),
            "username": t.string(),
            "connectionAttributes": t.struct({"_": t.string().optional()}).optional(),
            "databaseService": t.string(),
            "password": t.string(),
            "hostname": t.string(),
        }
    ).named(renames["OracleProfileIn"])
    types["OracleProfileOut"] = t.struct(
        {
            "port": t.integer().optional(),
            "username": t.string(),
            "connectionAttributes": t.struct({"_": t.string().optional()}).optional(),
            "databaseService": t.string(),
            "password": t.string(),
            "hostname": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OracleProfileOut"])
    types["SingleTargetDatasetIn"] = t.struct(
        {"datasetId": t.string().optional()}
    ).named(renames["SingleTargetDatasetIn"])
    types["SingleTargetDatasetOut"] = t.struct(
        {
            "datasetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SingleTargetDatasetOut"])
    types["MysqlRdbmsIn"] = t.struct(
        {"mysqlDatabases": t.array(t.proxy(renames["MysqlDatabaseIn"])).optional()}
    ).named(renames["MysqlRdbmsIn"])
    types["MysqlRdbmsOut"] = t.struct(
        {
            "mysqlDatabases": t.array(t.proxy(renames["MysqlDatabaseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MysqlRdbmsOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["BigQueryProfileIn"] = t.struct({"_": t.string().optional()}).named(
        renames["BigQueryProfileIn"]
    )
    types["BigQueryProfileOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["BigQueryProfileOut"])
    types["DatasetTemplateIn"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "datasetIdPrefix": t.string().optional(),
            "location": t.string(),
        }
    ).named(renames["DatasetTemplateIn"])
    types["DatasetTemplateOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "datasetIdPrefix": t.string().optional(),
            "location": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatasetTemplateOut"])
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
    types["LookupStreamObjectRequestIn"] = t.struct(
        {"sourceObjectIdentifier": t.proxy(renames["SourceObjectIdentifierIn"])}
    ).named(renames["LookupStreamObjectRequestIn"])
    types["LookupStreamObjectRequestOut"] = t.struct(
        {
            "sourceObjectIdentifier": t.proxy(renames["SourceObjectIdentifierOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LookupStreamObjectRequestOut"])
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
            "displayName": t.string(),
            "vpcPeeringConfig": t.proxy(renames["VpcPeeringConfigOut"]).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["PrivateConnectionOut"])
    types["ListStreamsResponseIn"] = t.struct(
        {
            "streams": t.array(t.proxy(renames["StreamIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListStreamsResponseIn"])
    types["ListStreamsResponseOut"] = t.struct(
        {
            "streams": t.array(t.proxy(renames["StreamOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListStreamsResponseOut"])
    types["MysqlProfileIn"] = t.struct(
        {
            "sslConfig": t.proxy(renames["MysqlSslConfigIn"]).optional(),
            "hostname": t.string(),
            "username": t.string(),
            "port": t.integer().optional(),
            "password": t.string(),
        }
    ).named(renames["MysqlProfileIn"])
    types["MysqlProfileOut"] = t.struct(
        {
            "sslConfig": t.proxy(renames["MysqlSslConfigOut"]).optional(),
            "hostname": t.string(),
            "username": t.string(),
            "port": t.integer().optional(),
            "password": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MysqlProfileOut"])
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
    types["MysqlSourceConfigIn"] = t.struct(
        {
            "maxConcurrentBackfillTasks": t.integer().optional(),
            "excludeObjects": t.proxy(renames["MysqlRdbmsIn"]).optional(),
            "includeObjects": t.proxy(renames["MysqlRdbmsIn"]).optional(),
            "maxConcurrentCdcTasks": t.integer().optional(),
        }
    ).named(renames["MysqlSourceConfigIn"])
    types["MysqlSourceConfigOut"] = t.struct(
        {
            "maxConcurrentBackfillTasks": t.integer().optional(),
            "excludeObjects": t.proxy(renames["MysqlRdbmsOut"]).optional(),
            "includeObjects": t.proxy(renames["MysqlRdbmsOut"]).optional(),
            "maxConcurrentCdcTasks": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MysqlSourceConfigOut"])
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
    types["ForwardSshTunnelConnectivityIn"] = t.struct(
        {
            "hostname": t.string(),
            "password": t.string().optional(),
            "username": t.string(),
            "port": t.integer().optional(),
            "privateKey": t.string().optional(),
        }
    ).named(renames["ForwardSshTunnelConnectivityIn"])
    types["ForwardSshTunnelConnectivityOut"] = t.struct(
        {
            "hostname": t.string(),
            "password": t.string().optional(),
            "username": t.string(),
            "port": t.integer().optional(),
            "privateKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ForwardSshTunnelConnectivityOut"])
    types["PrivateConnectivityIn"] = t.struct({"privateConnection": t.string()}).named(
        renames["PrivateConnectivityIn"]
    )
    types["PrivateConnectivityOut"] = t.struct(
        {
            "privateConnection": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateConnectivityOut"])
    types["StreamObjectIn"] = t.struct(
        {
            "displayName": t.string(),
            "backfillJob": t.proxy(renames["BackfillJobIn"]).optional(),
            "sourceObject": t.proxy(renames["SourceObjectIdentifierIn"]).optional(),
        }
    ).named(renames["StreamObjectIn"])
    types["StreamObjectOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string(),
            "errors": t.array(t.proxy(renames["ErrorOut"])).optional(),
            "backfillJob": t.proxy(renames["BackfillJobOut"]).optional(),
            "sourceObject": t.proxy(renames["SourceObjectIdentifierOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamObjectOut"])
    types["BackfillNoneStrategyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["BackfillNoneStrategyIn"]
    )
    types["BackfillNoneStrategyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["BackfillNoneStrategyOut"])
    types["PostgresqlProfileIn"] = t.struct(
        {
            "hostname": t.string(),
            "database": t.string(),
            "password": t.string(),
            "port": t.integer().optional(),
            "username": t.string(),
        }
    ).named(renames["PostgresqlProfileIn"])
    types["PostgresqlProfileOut"] = t.struct(
        {
            "hostname": t.string(),
            "database": t.string(),
            "password": t.string(),
            "port": t.integer().optional(),
            "username": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostgresqlProfileOut"])
    types["ConnectionProfileIn"] = t.struct(
        {
            "postgresqlProfile": t.proxy(renames["PostgresqlProfileIn"]).optional(),
            "gcsProfile": t.proxy(renames["GcsProfileIn"]).optional(),
            "forwardSshConnectivity": t.proxy(
                renames["ForwardSshTunnelConnectivityIn"]
            ).optional(),
            "oracleProfile": t.proxy(renames["OracleProfileIn"]).optional(),
            "bigqueryProfile": t.proxy(renames["BigQueryProfileIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "staticServiceIpConnectivity": t.proxy(
                renames["StaticServiceIpConnectivityIn"]
            ).optional(),
            "privateConnectivity": t.proxy(renames["PrivateConnectivityIn"]).optional(),
            "mysqlProfile": t.proxy(renames["MysqlProfileIn"]).optional(),
            "displayName": t.string(),
        }
    ).named(renames["ConnectionProfileIn"])
    types["ConnectionProfileOut"] = t.struct(
        {
            "postgresqlProfile": t.proxy(renames["PostgresqlProfileOut"]).optional(),
            "gcsProfile": t.proxy(renames["GcsProfileOut"]).optional(),
            "forwardSshConnectivity": t.proxy(
                renames["ForwardSshTunnelConnectivityOut"]
            ).optional(),
            "name": t.string().optional(),
            "oracleProfile": t.proxy(renames["OracleProfileOut"]).optional(),
            "bigqueryProfile": t.proxy(renames["BigQueryProfileOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "staticServiceIpConnectivity": t.proxy(
                renames["StaticServiceIpConnectivityOut"]
            ).optional(),
            "privateConnectivity": t.proxy(
                renames["PrivateConnectivityOut"]
            ).optional(),
            "mysqlProfile": t.proxy(renames["MysqlProfileOut"]).optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionProfileOut"])
    types["OracleSourceConfigIn"] = t.struct(
        {
            "includeObjects": t.proxy(renames["OracleRdbmsIn"]).optional(),
            "maxConcurrentCdcTasks": t.integer().optional(),
            "dropLargeObjects": t.proxy(renames["DropLargeObjectsIn"]).optional(),
            "maxConcurrentBackfillTasks": t.integer().optional(),
            "streamLargeObjects": t.proxy(renames["StreamLargeObjectsIn"]).optional(),
            "excludeObjects": t.proxy(renames["OracleRdbmsIn"]).optional(),
        }
    ).named(renames["OracleSourceConfigIn"])
    types["OracleSourceConfigOut"] = t.struct(
        {
            "includeObjects": t.proxy(renames["OracleRdbmsOut"]).optional(),
            "maxConcurrentCdcTasks": t.integer().optional(),
            "dropLargeObjects": t.proxy(renames["DropLargeObjectsOut"]).optional(),
            "maxConcurrentBackfillTasks": t.integer().optional(),
            "streamLargeObjects": t.proxy(renames["StreamLargeObjectsOut"]).optional(),
            "excludeObjects": t.proxy(renames["OracleRdbmsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OracleSourceConfigOut"])
    types["StreamIn"] = t.struct(
        {
            "state": t.string().optional(),
            "backfillNone": t.proxy(renames["BackfillNoneStrategyIn"]).optional(),
            "sourceConfig": t.proxy(renames["SourceConfigIn"]),
            "customerManagedEncryptionKey": t.string().optional(),
            "displayName": t.string(),
            "backfillAll": t.proxy(renames["BackfillAllStrategyIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "destinationConfig": t.proxy(renames["DestinationConfigIn"]),
        }
    ).named(renames["StreamIn"])
    types["StreamOut"] = t.struct(
        {
            "name": t.string().optional(),
            "state": t.string().optional(),
            "backfillNone": t.proxy(renames["BackfillNoneStrategyOut"]).optional(),
            "sourceConfig": t.proxy(renames["SourceConfigOut"]),
            "errors": t.array(t.proxy(renames["ErrorOut"])).optional(),
            "createTime": t.string().optional(),
            "customerManagedEncryptionKey": t.string().optional(),
            "displayName": t.string(),
            "backfillAll": t.proxy(renames["BackfillAllStrategyOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "destinationConfig": t.proxy(renames["DestinationConfigOut"]),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamOut"])
    types["SourceObjectIdentifierIn"] = t.struct(
        {
            "mysqlIdentifier": t.proxy(renames["MysqlObjectIdentifierIn"]).optional(),
            "oracleIdentifier": t.proxy(renames["OracleObjectIdentifierIn"]).optional(),
            "postgresqlIdentifier": t.proxy(
                renames["PostgresqlObjectIdentifierIn"]
            ).optional(),
        }
    ).named(renames["SourceObjectIdentifierIn"])
    types["SourceObjectIdentifierOut"] = t.struct(
        {
            "mysqlIdentifier": t.proxy(renames["MysqlObjectIdentifierOut"]).optional(),
            "oracleIdentifier": t.proxy(
                renames["OracleObjectIdentifierOut"]
            ).optional(),
            "postgresqlIdentifier": t.proxy(
                renames["PostgresqlObjectIdentifierOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceObjectIdentifierOut"])
    types["SourceHierarchyDatasetsIn"] = t.struct(
        {"datasetTemplate": t.proxy(renames["DatasetTemplateIn"]).optional()}
    ).named(renames["SourceHierarchyDatasetsIn"])
    types["SourceHierarchyDatasetsOut"] = t.struct(
        {
            "datasetTemplate": t.proxy(renames["DatasetTemplateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceHierarchyDatasetsOut"])
    types["GcsProfileIn"] = t.struct(
        {"rootPath": t.string().optional(), "bucket": t.string()}
    ).named(renames["GcsProfileIn"])
    types["GcsProfileOut"] = t.struct(
        {
            "rootPath": t.string().optional(),
            "bucket": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsProfileOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "validationResult": t.proxy(renames["ValidationResultOut"]).optional(),
            "statusMessage": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["StreamLargeObjectsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StreamLargeObjectsIn"]
    )
    types["StreamLargeObjectsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StreamLargeObjectsOut"])
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["MysqlColumnIn"] = t.struct(
        {
            "column": t.string().optional(),
            "nullable": t.boolean().optional(),
            "collation": t.string().optional(),
            "primaryKey": t.boolean().optional(),
            "ordinalPosition": t.integer().optional(),
            "dataType": t.string().optional(),
            "length": t.integer().optional(),
        }
    ).named(renames["MysqlColumnIn"])
    types["MysqlColumnOut"] = t.struct(
        {
            "column": t.string().optional(),
            "nullable": t.boolean().optional(),
            "collation": t.string().optional(),
            "primaryKey": t.boolean().optional(),
            "ordinalPosition": t.integer().optional(),
            "dataType": t.string().optional(),
            "length": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MysqlColumnOut"])
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
    types["StartBackfillJobResponseIn"] = t.struct(
        {"object": t.proxy(renames["StreamObjectIn"]).optional()}
    ).named(renames["StartBackfillJobResponseIn"])
    types["StartBackfillJobResponseOut"] = t.struct(
        {
            "object": t.proxy(renames["StreamObjectOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartBackfillJobResponseOut"])
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
    types["StopBackfillJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StopBackfillJobRequestIn"]
    )
    types["StopBackfillJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StopBackfillJobRequestOut"])
    types["PostgresqlObjectIdentifierIn"] = t.struct(
        {"schema": t.string(), "table": t.string()}
    ).named(renames["PostgresqlObjectIdentifierIn"])
    types["PostgresqlObjectIdentifierOut"] = t.struct(
        {
            "schema": t.string(),
            "table": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostgresqlObjectIdentifierOut"])
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
    types["ValidationResultIn"] = t.struct(
        {"validations": t.array(t.proxy(renames["ValidationIn"])).optional()}
    ).named(renames["ValidationResultIn"])
    types["ValidationResultOut"] = t.struct(
        {
            "validations": t.array(t.proxy(renames["ValidationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationResultOut"])
    types["BackfillJobIn"] = t.struct(
        {"state": t.string().optional(), "trigger": t.string().optional()}
    ).named(renames["BackfillJobIn"])
    types["BackfillJobOut"] = t.struct(
        {
            "lastStartTime": t.string().optional(),
            "state": t.string().optional(),
            "trigger": t.string().optional(),
            "errors": t.array(t.proxy(renames["ErrorOut"])).optional(),
            "lastEndTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackfillJobOut"])
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
    types["ErrorIn"] = t.struct(
        {
            "reason": t.string().optional(),
            "message": t.string().optional(),
            "errorUuid": t.string().optional(),
            "errorTime": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ErrorIn"])
    types["ErrorOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "message": t.string().optional(),
            "errorUuid": t.string().optional(),
            "errorTime": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorOut"])
    types["BigQueryDestinationConfigIn"] = t.struct(
        {
            "dataFreshness": t.string().optional(),
            "sourceHierarchyDatasets": t.proxy(
                renames["SourceHierarchyDatasetsIn"]
            ).optional(),
            "singleTargetDataset": t.proxy(renames["SingleTargetDatasetIn"]).optional(),
        }
    ).named(renames["BigQueryDestinationConfigIn"])
    types["BigQueryDestinationConfigOut"] = t.struct(
        {
            "dataFreshness": t.string().optional(),
            "sourceHierarchyDatasets": t.proxy(
                renames["SourceHierarchyDatasetsOut"]
            ).optional(),
            "singleTargetDataset": t.proxy(
                renames["SingleTargetDatasetOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryDestinationConfigOut"])
    types["StartBackfillJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StartBackfillJobRequestIn"]
    )
    types["StartBackfillJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StartBackfillJobRequestOut"])
    types["GcsDestinationConfigIn"] = t.struct(
        {
            "path": t.string().optional(),
            "fileRotationMb": t.integer().optional(),
            "jsonFileFormat": t.proxy(renames["JsonFileFormatIn"]).optional(),
            "fileRotationInterval": t.string().optional(),
            "avroFileFormat": t.proxy(renames["AvroFileFormatIn"]).optional(),
        }
    ).named(renames["GcsDestinationConfigIn"])
    types["GcsDestinationConfigOut"] = t.struct(
        {
            "path": t.string().optional(),
            "fileRotationMb": t.integer().optional(),
            "jsonFileFormat": t.proxy(renames["JsonFileFormatOut"]).optional(),
            "fileRotationInterval": t.string().optional(),
            "avroFileFormat": t.proxy(renames["AvroFileFormatOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsDestinationConfigOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["OracleRdbmsIn"] = t.struct(
        {"oracleSchemas": t.array(t.proxy(renames["OracleSchemaIn"])).optional()}
    ).named(renames["OracleRdbmsIn"])
    types["OracleRdbmsOut"] = t.struct(
        {
            "oracleSchemas": t.array(t.proxy(renames["OracleSchemaOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OracleRdbmsOut"])
    types["SourceConfigIn"] = t.struct(
        {
            "oracleSourceConfig": t.proxy(renames["OracleSourceConfigIn"]).optional(),
            "postgresqlSourceConfig": t.proxy(
                renames["PostgresqlSourceConfigIn"]
            ).optional(),
            "mysqlSourceConfig": t.proxy(renames["MysqlSourceConfigIn"]).optional(),
            "sourceConnectionProfile": t.string(),
        }
    ).named(renames["SourceConfigIn"])
    types["SourceConfigOut"] = t.struct(
        {
            "oracleSourceConfig": t.proxy(renames["OracleSourceConfigOut"]).optional(),
            "postgresqlSourceConfig": t.proxy(
                renames["PostgresqlSourceConfigOut"]
            ).optional(),
            "mysqlSourceConfig": t.proxy(renames["MysqlSourceConfigOut"]).optional(),
            "sourceConnectionProfile": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceConfigOut"])
    types["ValidationIn"] = t.struct(
        {
            "state": t.string().optional(),
            "code": t.string().optional(),
            "message": t.array(t.proxy(renames["ValidationMessageIn"])).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ValidationIn"])
    types["ValidationOut"] = t.struct(
        {
            "state": t.string().optional(),
            "code": t.string().optional(),
            "message": t.array(t.proxy(renames["ValidationMessageOut"])).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationOut"])
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
            "nextPageToken": t.string().optional(),
            "privateConnections": t.array(
                t.proxy(renames["PrivateConnectionIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListPrivateConnectionsResponseIn"])
    types["ListPrivateConnectionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "privateConnections": t.array(
                t.proxy(renames["PrivateConnectionOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPrivateConnectionsResponseOut"])
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
    types["DropLargeObjectsIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DropLargeObjectsIn"]
    )
    types["DropLargeObjectsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DropLargeObjectsOut"])
    types["BackfillAllStrategyIn"] = t.struct(
        {
            "postgresqlExcludedObjects": t.proxy(
                renames["PostgresqlRdbmsIn"]
            ).optional(),
            "mysqlExcludedObjects": t.proxy(renames["MysqlRdbmsIn"]).optional(),
            "oracleExcludedObjects": t.proxy(renames["OracleRdbmsIn"]).optional(),
        }
    ).named(renames["BackfillAllStrategyIn"])
    types["BackfillAllStrategyOut"] = t.struct(
        {
            "postgresqlExcludedObjects": t.proxy(
                renames["PostgresqlRdbmsOut"]
            ).optional(),
            "mysqlExcludedObjects": t.proxy(renames["MysqlRdbmsOut"]).optional(),
            "oracleExcludedObjects": t.proxy(renames["OracleRdbmsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackfillAllStrategyOut"])
    types["PostgresqlSourceConfigIn"] = t.struct(
        {
            "maxConcurrentBackfillTasks": t.integer().optional(),
            "includeObjects": t.proxy(renames["PostgresqlRdbmsIn"]).optional(),
            "excludeObjects": t.proxy(renames["PostgresqlRdbmsIn"]).optional(),
            "publication": t.string(),
            "replicationSlot": t.string(),
        }
    ).named(renames["PostgresqlSourceConfigIn"])
    types["PostgresqlSourceConfigOut"] = t.struct(
        {
            "maxConcurrentBackfillTasks": t.integer().optional(),
            "includeObjects": t.proxy(renames["PostgresqlRdbmsOut"]).optional(),
            "excludeObjects": t.proxy(renames["PostgresqlRdbmsOut"]).optional(),
            "publication": t.string(),
            "replicationSlot": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostgresqlSourceConfigOut"])
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
            "clientKey": t.string().optional(),
            "clientCertificateSet": t.boolean().optional(),
            "clientCertificate": t.string().optional(),
            "clientKeySet": t.boolean().optional(),
            "caCertificate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MysqlSslConfigOut"])

    functions = {}
    functions["projectsLocationsFetchStaticIps"] = datastream.get(
        "v1/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = datastream.get(
        "v1/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = datastream.get(
        "v1/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsDelete"] = datastream.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "force": t.boolean().optional(),
                "name": t.string().optional(),
                "requestId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "state": t.string().optional(),
                "backfillNone": t.proxy(renames["BackfillNoneStrategyIn"]).optional(),
                "sourceConfig": t.proxy(renames["SourceConfigIn"]),
                "customerManagedEncryptionKey": t.string().optional(),
                "displayName": t.string(),
                "backfillAll": t.proxy(renames["BackfillAllStrategyIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "destinationConfig": t.proxy(renames["DestinationConfigIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsGet"] = datastream.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "force": t.boolean().optional(),
                "name": t.string().optional(),
                "requestId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "state": t.string().optional(),
                "backfillNone": t.proxy(renames["BackfillNoneStrategyIn"]).optional(),
                "sourceConfig": t.proxy(renames["SourceConfigIn"]),
                "customerManagedEncryptionKey": t.string().optional(),
                "displayName": t.string(),
                "backfillAll": t.proxy(renames["BackfillAllStrategyIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "destinationConfig": t.proxy(renames["DestinationConfigIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsList"] = datastream.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "force": t.boolean().optional(),
                "name": t.string().optional(),
                "requestId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "state": t.string().optional(),
                "backfillNone": t.proxy(renames["BackfillNoneStrategyIn"]).optional(),
                "sourceConfig": t.proxy(renames["SourceConfigIn"]),
                "customerManagedEncryptionKey": t.string().optional(),
                "displayName": t.string(),
                "backfillAll": t.proxy(renames["BackfillAllStrategyIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "destinationConfig": t.proxy(renames["DestinationConfigIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsCreate"] = datastream.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "force": t.boolean().optional(),
                "name": t.string().optional(),
                "requestId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "state": t.string().optional(),
                "backfillNone": t.proxy(renames["BackfillNoneStrategyIn"]).optional(),
                "sourceConfig": t.proxy(renames["SourceConfigIn"]),
                "customerManagedEncryptionKey": t.string().optional(),
                "displayName": t.string(),
                "backfillAll": t.proxy(renames["BackfillAllStrategyIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "destinationConfig": t.proxy(renames["DestinationConfigIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsPatch"] = datastream.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "force": t.boolean().optional(),
                "name": t.string().optional(),
                "requestId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "state": t.string().optional(),
                "backfillNone": t.proxy(renames["BackfillNoneStrategyIn"]).optional(),
                "sourceConfig": t.proxy(renames["SourceConfigIn"]),
                "customerManagedEncryptionKey": t.string().optional(),
                "displayName": t.string(),
                "backfillAll": t.proxy(renames["BackfillAllStrategyIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "destinationConfig": t.proxy(renames["DestinationConfigIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsObjectsLookup"] = datastream.post(
        "v1/{object}:startBackfillJob",
        t.struct(
            {
                "object": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StartBackfillJobResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsObjectsStopBackfillJob"] = datastream.post(
        "v1/{object}:startBackfillJob",
        t.struct(
            {
                "object": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StartBackfillJobResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsObjectsGet"] = datastream.post(
        "v1/{object}:startBackfillJob",
        t.struct(
            {
                "object": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StartBackfillJobResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsObjectsList"] = datastream.post(
        "v1/{object}:startBackfillJob",
        t.struct(
            {
                "object": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StartBackfillJobResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStreamsObjectsStartBackfillJob"] = datastream.post(
        "v1/{object}:startBackfillJob",
        t.struct(
            {
                "object": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StartBackfillJobResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesDiscover"] = datastream.get(
        "v1/{parent}/connectionProfiles",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListConnectionProfilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesPatch"] = datastream.get(
        "v1/{parent}/connectionProfiles",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListConnectionProfilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesCreate"] = datastream.get(
        "v1/{parent}/connectionProfiles",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListConnectionProfilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesGet"] = datastream.get(
        "v1/{parent}/connectionProfiles",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListConnectionProfilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesDelete"] = datastream.get(
        "v1/{parent}/connectionProfiles",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListConnectionProfilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionProfilesList"] = datastream.get(
        "v1/{parent}/connectionProfiles",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListConnectionProfilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsDelete"] = datastream.get(
        "v1/{parent}/privateConnections",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPrivateConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsCreate"] = datastream.get(
        "v1/{parent}/privateConnections",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPrivateConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPrivateConnectionsRoutesGet"] = datastream.delete(
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
    functions["projectsLocationsPrivateConnectionsRoutesCreate"] = datastream.delete(
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
    functions["projectsLocationsPrivateConnectionsRoutesList"] = datastream.delete(
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
    functions["projectsLocationsPrivateConnectionsRoutesDelete"] = datastream.delete(
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
