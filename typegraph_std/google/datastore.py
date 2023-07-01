from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_datastore():
    datastore = HTTPRuntime("https://datastore.googleapis.com/")

    renames = {
        "ErrorResponse": "_datastore_1_ErrorResponse",
        "EmptyIn": "_datastore_2_EmptyIn",
        "EmptyOut": "_datastore_3_EmptyOut",
        "CountIn": "_datastore_4_CountIn",
        "CountOut": "_datastore_5_CountOut",
        "EntityIn": "_datastore_6_EntityIn",
        "EntityOut": "_datastore_7_EntityOut",
        "RollbackRequestIn": "_datastore_8_RollbackRequestIn",
        "RollbackRequestOut": "_datastore_9_RollbackRequestOut",
        "LookupResponseIn": "_datastore_10_LookupResponseIn",
        "LookupResponseOut": "_datastore_11_LookupResponseOut",
        "QueryIn": "_datastore_12_QueryIn",
        "QueryOut": "_datastore_13_QueryOut",
        "AggregationResultBatchIn": "_datastore_14_AggregationResultBatchIn",
        "AggregationResultBatchOut": "_datastore_15_AggregationResultBatchOut",
        "MutationIn": "_datastore_16_MutationIn",
        "MutationOut": "_datastore_17_MutationOut",
        "MutationResultIn": "_datastore_18_MutationResultIn",
        "MutationResultOut": "_datastore_19_MutationResultOut",
        "GoogleDatastoreAdminV1beta1CommonMetadataIn": "_datastore_20_GoogleDatastoreAdminV1beta1CommonMetadataIn",
        "GoogleDatastoreAdminV1beta1CommonMetadataOut": "_datastore_21_GoogleDatastoreAdminV1beta1CommonMetadataOut",
        "PropertyFilterIn": "_datastore_22_PropertyFilterIn",
        "PropertyFilterOut": "_datastore_23_PropertyFilterOut",
        "GoogleDatastoreAdminV1ExportEntitiesRequestIn": "_datastore_24_GoogleDatastoreAdminV1ExportEntitiesRequestIn",
        "GoogleDatastoreAdminV1ExportEntitiesRequestOut": "_datastore_25_GoogleDatastoreAdminV1ExportEntitiesRequestOut",
        "AggregationResultIn": "_datastore_26_AggregationResultIn",
        "AggregationResultOut": "_datastore_27_AggregationResultOut",
        "GoogleDatastoreAdminV1DatastoreFirestoreMigrationMetadataIn": "_datastore_28_GoogleDatastoreAdminV1DatastoreFirestoreMigrationMetadataIn",
        "GoogleDatastoreAdminV1DatastoreFirestoreMigrationMetadataOut": "_datastore_29_GoogleDatastoreAdminV1DatastoreFirestoreMigrationMetadataOut",
        "ValueIn": "_datastore_30_ValueIn",
        "ValueOut": "_datastore_31_ValueOut",
        "BeginTransactionResponseIn": "_datastore_32_BeginTransactionResponseIn",
        "BeginTransactionResponseOut": "_datastore_33_BeginTransactionResponseOut",
        "GoogleDatastoreAdminV1MigrationStateEventIn": "_datastore_34_GoogleDatastoreAdminV1MigrationStateEventIn",
        "GoogleDatastoreAdminV1MigrationStateEventOut": "_datastore_35_GoogleDatastoreAdminV1MigrationStateEventOut",
        "AllocateIdsResponseIn": "_datastore_36_AllocateIdsResponseIn",
        "AllocateIdsResponseOut": "_datastore_37_AllocateIdsResponseOut",
        "BeginTransactionRequestIn": "_datastore_38_BeginTransactionRequestIn",
        "BeginTransactionRequestOut": "_datastore_39_BeginTransactionRequestOut",
        "StatusIn": "_datastore_40_StatusIn",
        "StatusOut": "_datastore_41_StatusOut",
        "RunAggregationQueryResponseIn": "_datastore_42_RunAggregationQueryResponseIn",
        "RunAggregationQueryResponseOut": "_datastore_43_RunAggregationQueryResponseOut",
        "GoogleDatastoreAdminV1ExportEntitiesResponseIn": "_datastore_44_GoogleDatastoreAdminV1ExportEntitiesResponseIn",
        "GoogleDatastoreAdminV1ExportEntitiesResponseOut": "_datastore_45_GoogleDatastoreAdminV1ExportEntitiesResponseOut",
        "GoogleDatastoreAdminV1ProgressIn": "_datastore_46_GoogleDatastoreAdminV1ProgressIn",
        "GoogleDatastoreAdminV1ProgressOut": "_datastore_47_GoogleDatastoreAdminV1ProgressOut",
        "AllocateIdsRequestIn": "_datastore_48_AllocateIdsRequestIn",
        "AllocateIdsRequestOut": "_datastore_49_AllocateIdsRequestOut",
        "GoogleDatastoreAdminV1MigrationProgressEventIn": "_datastore_50_GoogleDatastoreAdminV1MigrationProgressEventIn",
        "GoogleDatastoreAdminV1MigrationProgressEventOut": "_datastore_51_GoogleDatastoreAdminV1MigrationProgressEventOut",
        "GoogleLongrunningOperationIn": "_datastore_52_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_datastore_53_GoogleLongrunningOperationOut",
        "GoogleDatastoreAdminV1ListIndexesResponseIn": "_datastore_54_GoogleDatastoreAdminV1ListIndexesResponseIn",
        "GoogleDatastoreAdminV1ListIndexesResponseOut": "_datastore_55_GoogleDatastoreAdminV1ListIndexesResponseOut",
        "PropertyOrderIn": "_datastore_56_PropertyOrderIn",
        "PropertyOrderOut": "_datastore_57_PropertyOrderOut",
        "ReadWriteIn": "_datastore_58_ReadWriteIn",
        "ReadWriteOut": "_datastore_59_ReadWriteOut",
        "GoogleDatastoreAdminV1IndexOperationMetadataIn": "_datastore_60_GoogleDatastoreAdminV1IndexOperationMetadataIn",
        "GoogleDatastoreAdminV1IndexOperationMetadataOut": "_datastore_61_GoogleDatastoreAdminV1IndexOperationMetadataOut",
        "GoogleDatastoreAdminV1beta1ImportEntitiesMetadataIn": "_datastore_62_GoogleDatastoreAdminV1beta1ImportEntitiesMetadataIn",
        "GoogleDatastoreAdminV1beta1ImportEntitiesMetadataOut": "_datastore_63_GoogleDatastoreAdminV1beta1ImportEntitiesMetadataOut",
        "PathElementIn": "_datastore_64_PathElementIn",
        "PathElementOut": "_datastore_65_PathElementOut",
        "ReserveIdsRequestIn": "_datastore_66_ReserveIdsRequestIn",
        "ReserveIdsRequestOut": "_datastore_67_ReserveIdsRequestOut",
        "GoogleDatastoreAdminV1EntityFilterIn": "_datastore_68_GoogleDatastoreAdminV1EntityFilterIn",
        "GoogleDatastoreAdminV1EntityFilterOut": "_datastore_69_GoogleDatastoreAdminV1EntityFilterOut",
        "CommitRequestIn": "_datastore_70_CommitRequestIn",
        "CommitRequestOut": "_datastore_71_CommitRequestOut",
        "GoogleDatastoreAdminV1IndexIn": "_datastore_72_GoogleDatastoreAdminV1IndexIn",
        "GoogleDatastoreAdminV1IndexOut": "_datastore_73_GoogleDatastoreAdminV1IndexOut",
        "ArrayValueIn": "_datastore_74_ArrayValueIn",
        "ArrayValueOut": "_datastore_75_ArrayValueOut",
        "KeyIn": "_datastore_76_KeyIn",
        "KeyOut": "_datastore_77_KeyOut",
        "GoogleLongrunningListOperationsResponseIn": "_datastore_78_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_datastore_79_GoogleLongrunningListOperationsResponseOut",
        "GoogleDatastoreAdminV1ImportEntitiesRequestIn": "_datastore_80_GoogleDatastoreAdminV1ImportEntitiesRequestIn",
        "GoogleDatastoreAdminV1ImportEntitiesRequestOut": "_datastore_81_GoogleDatastoreAdminV1ImportEntitiesRequestOut",
        "EntityResultIn": "_datastore_82_EntityResultIn",
        "EntityResultOut": "_datastore_83_EntityResultOut",
        "PropertyReferenceIn": "_datastore_84_PropertyReferenceIn",
        "PropertyReferenceOut": "_datastore_85_PropertyReferenceOut",
        "TransactionOptionsIn": "_datastore_86_TransactionOptionsIn",
        "TransactionOptionsOut": "_datastore_87_TransactionOptionsOut",
        "CommitResponseIn": "_datastore_88_CommitResponseIn",
        "CommitResponseOut": "_datastore_89_CommitResponseOut",
        "LookupRequestIn": "_datastore_90_LookupRequestIn",
        "LookupRequestOut": "_datastore_91_LookupRequestOut",
        "AggregationIn": "_datastore_92_AggregationIn",
        "AggregationOut": "_datastore_93_AggregationOut",
        "GoogleDatastoreAdminV1beta1EntityFilterIn": "_datastore_94_GoogleDatastoreAdminV1beta1EntityFilterIn",
        "GoogleDatastoreAdminV1beta1EntityFilterOut": "_datastore_95_GoogleDatastoreAdminV1beta1EntityFilterOut",
        "ReserveIdsResponseIn": "_datastore_96_ReserveIdsResponseIn",
        "ReserveIdsResponseOut": "_datastore_97_ReserveIdsResponseOut",
        "ReadOptionsIn": "_datastore_98_ReadOptionsIn",
        "ReadOptionsOut": "_datastore_99_ReadOptionsOut",
        "LatLngIn": "_datastore_100_LatLngIn",
        "LatLngOut": "_datastore_101_LatLngOut",
        "QueryResultBatchIn": "_datastore_102_QueryResultBatchIn",
        "QueryResultBatchOut": "_datastore_103_QueryResultBatchOut",
        "GoogleDatastoreAdminV1RedirectWritesStepDetailsIn": "_datastore_104_GoogleDatastoreAdminV1RedirectWritesStepDetailsIn",
        "GoogleDatastoreAdminV1RedirectWritesStepDetailsOut": "_datastore_105_GoogleDatastoreAdminV1RedirectWritesStepDetailsOut",
        "GqlQueryParameterIn": "_datastore_106_GqlQueryParameterIn",
        "GqlQueryParameterOut": "_datastore_107_GqlQueryParameterOut",
        "GoogleDatastoreAdminV1ImportEntitiesMetadataIn": "_datastore_108_GoogleDatastoreAdminV1ImportEntitiesMetadataIn",
        "GoogleDatastoreAdminV1ImportEntitiesMetadataOut": "_datastore_109_GoogleDatastoreAdminV1ImportEntitiesMetadataOut",
        "PartitionIdIn": "_datastore_110_PartitionIdIn",
        "PartitionIdOut": "_datastore_111_PartitionIdOut",
        "GoogleDatastoreAdminV1CommonMetadataIn": "_datastore_112_GoogleDatastoreAdminV1CommonMetadataIn",
        "GoogleDatastoreAdminV1CommonMetadataOut": "_datastore_113_GoogleDatastoreAdminV1CommonMetadataOut",
        "GoogleDatastoreAdminV1IndexedPropertyIn": "_datastore_114_GoogleDatastoreAdminV1IndexedPropertyIn",
        "GoogleDatastoreAdminV1IndexedPropertyOut": "_datastore_115_GoogleDatastoreAdminV1IndexedPropertyOut",
        "ReadOnlyIn": "_datastore_116_ReadOnlyIn",
        "ReadOnlyOut": "_datastore_117_ReadOnlyOut",
        "FilterIn": "_datastore_118_FilterIn",
        "FilterOut": "_datastore_119_FilterOut",
        "GoogleDatastoreAdminV1ExportEntitiesMetadataIn": "_datastore_120_GoogleDatastoreAdminV1ExportEntitiesMetadataIn",
        "GoogleDatastoreAdminV1ExportEntitiesMetadataOut": "_datastore_121_GoogleDatastoreAdminV1ExportEntitiesMetadataOut",
        "RunQueryResponseIn": "_datastore_122_RunQueryResponseIn",
        "RunQueryResponseOut": "_datastore_123_RunQueryResponseOut",
        "KindExpressionIn": "_datastore_124_KindExpressionIn",
        "KindExpressionOut": "_datastore_125_KindExpressionOut",
        "ProjectionIn": "_datastore_126_ProjectionIn",
        "ProjectionOut": "_datastore_127_ProjectionOut",
        "RunQueryRequestIn": "_datastore_128_RunQueryRequestIn",
        "RunQueryRequestOut": "_datastore_129_RunQueryRequestOut",
        "CompositeFilterIn": "_datastore_130_CompositeFilterIn",
        "CompositeFilterOut": "_datastore_131_CompositeFilterOut",
        "GoogleDatastoreAdminV1PrepareStepDetailsIn": "_datastore_132_GoogleDatastoreAdminV1PrepareStepDetailsIn",
        "GoogleDatastoreAdminV1PrepareStepDetailsOut": "_datastore_133_GoogleDatastoreAdminV1PrepareStepDetailsOut",
        "GoogleDatastoreAdminV1beta1ProgressIn": "_datastore_134_GoogleDatastoreAdminV1beta1ProgressIn",
        "GoogleDatastoreAdminV1beta1ProgressOut": "_datastore_135_GoogleDatastoreAdminV1beta1ProgressOut",
        "RunAggregationQueryRequestIn": "_datastore_136_RunAggregationQueryRequestIn",
        "RunAggregationQueryRequestOut": "_datastore_137_RunAggregationQueryRequestOut",
        "GqlQueryIn": "_datastore_138_GqlQueryIn",
        "GqlQueryOut": "_datastore_139_GqlQueryOut",
        "GoogleDatastoreAdminV1beta1ExportEntitiesMetadataIn": "_datastore_140_GoogleDatastoreAdminV1beta1ExportEntitiesMetadataIn",
        "GoogleDatastoreAdminV1beta1ExportEntitiesMetadataOut": "_datastore_141_GoogleDatastoreAdminV1beta1ExportEntitiesMetadataOut",
        "GoogleDatastoreAdminV1beta1ExportEntitiesResponseIn": "_datastore_142_GoogleDatastoreAdminV1beta1ExportEntitiesResponseIn",
        "GoogleDatastoreAdminV1beta1ExportEntitiesResponseOut": "_datastore_143_GoogleDatastoreAdminV1beta1ExportEntitiesResponseOut",
        "RollbackResponseIn": "_datastore_144_RollbackResponseIn",
        "RollbackResponseOut": "_datastore_145_RollbackResponseOut",
        "AggregationQueryIn": "_datastore_146_AggregationQueryIn",
        "AggregationQueryOut": "_datastore_147_AggregationQueryOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["CountIn"] = t.struct({"upTo": t.string().optional()}).named(
        renames["CountIn"]
    )
    types["CountOut"] = t.struct(
        {
            "upTo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CountOut"])
    types["EntityIn"] = t.struct(
        {
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "key": t.proxy(renames["KeyIn"]).optional(),
        }
    ).named(renames["EntityIn"])
    types["EntityOut"] = t.struct(
        {
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "key": t.proxy(renames["KeyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityOut"])
    types["RollbackRequestIn"] = t.struct(
        {"transaction": t.string(), "databaseId": t.string().optional()}
    ).named(renames["RollbackRequestIn"])
    types["RollbackRequestOut"] = t.struct(
        {
            "transaction": t.string(),
            "databaseId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RollbackRequestOut"])
    types["LookupResponseIn"] = t.struct(
        {
            "found": t.array(t.proxy(renames["EntityResultIn"])).optional(),
            "readTime": t.string().optional(),
            "transaction": t.string().optional(),
            "deferred": t.array(t.proxy(renames["KeyIn"])).optional(),
            "missing": t.array(t.proxy(renames["EntityResultIn"])).optional(),
        }
    ).named(renames["LookupResponseIn"])
    types["LookupResponseOut"] = t.struct(
        {
            "found": t.array(t.proxy(renames["EntityResultOut"])).optional(),
            "readTime": t.string().optional(),
            "transaction": t.string().optional(),
            "deferred": t.array(t.proxy(renames["KeyOut"])).optional(),
            "missing": t.array(t.proxy(renames["EntityResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LookupResponseOut"])
    types["QueryIn"] = t.struct(
        {
            "startCursor": t.string().optional(),
            "projection": t.array(t.proxy(renames["ProjectionIn"])).optional(),
            "endCursor": t.string().optional(),
            "distinctOn": t.array(t.proxy(renames["PropertyReferenceIn"])).optional(),
            "filter": t.proxy(renames["FilterIn"]).optional(),
            "kind": t.array(t.proxy(renames["KindExpressionIn"])).optional(),
            "limit": t.integer().optional(),
            "order": t.array(t.proxy(renames["PropertyOrderIn"])).optional(),
            "offset": t.integer().optional(),
        }
    ).named(renames["QueryIn"])
    types["QueryOut"] = t.struct(
        {
            "startCursor": t.string().optional(),
            "projection": t.array(t.proxy(renames["ProjectionOut"])).optional(),
            "endCursor": t.string().optional(),
            "distinctOn": t.array(t.proxy(renames["PropertyReferenceOut"])).optional(),
            "filter": t.proxy(renames["FilterOut"]).optional(),
            "kind": t.array(t.proxy(renames["KindExpressionOut"])).optional(),
            "limit": t.integer().optional(),
            "order": t.array(t.proxy(renames["PropertyOrderOut"])).optional(),
            "offset": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryOut"])
    types["AggregationResultBatchIn"] = t.struct(
        {
            "aggregationResults": t.array(
                t.proxy(renames["AggregationResultIn"])
            ).optional(),
            "readTime": t.string().optional(),
            "moreResults": t.string().optional(),
        }
    ).named(renames["AggregationResultBatchIn"])
    types["AggregationResultBatchOut"] = t.struct(
        {
            "aggregationResults": t.array(
                t.proxy(renames["AggregationResultOut"])
            ).optional(),
            "readTime": t.string().optional(),
            "moreResults": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationResultBatchOut"])
    types["MutationIn"] = t.struct(
        {
            "baseVersion": t.string().optional(),
            "insert": t.proxy(renames["EntityIn"]).optional(),
            "update": t.proxy(renames["EntityIn"]).optional(),
            "updateTime": t.string().optional(),
            "delete": t.proxy(renames["KeyIn"]).optional(),
            "upsert": t.proxy(renames["EntityIn"]).optional(),
        }
    ).named(renames["MutationIn"])
    types["MutationOut"] = t.struct(
        {
            "baseVersion": t.string().optional(),
            "insert": t.proxy(renames["EntityOut"]).optional(),
            "update": t.proxy(renames["EntityOut"]).optional(),
            "updateTime": t.string().optional(),
            "delete": t.proxy(renames["KeyOut"]).optional(),
            "upsert": t.proxy(renames["EntityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MutationOut"])
    types["MutationResultIn"] = t.struct(
        {
            "version": t.string().optional(),
            "conflictDetected": t.boolean().optional(),
            "createTime": t.string().optional(),
            "key": t.proxy(renames["KeyIn"]).optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["MutationResultIn"])
    types["MutationResultOut"] = t.struct(
        {
            "version": t.string().optional(),
            "conflictDetected": t.boolean().optional(),
            "createTime": t.string().optional(),
            "key": t.proxy(renames["KeyOut"]).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MutationResultOut"])
    types["GoogleDatastoreAdminV1beta1CommonMetadataIn"] = t.struct(
        {
            "operationType": t.string().optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1beta1CommonMetadataIn"])
    types["GoogleDatastoreAdminV1beta1CommonMetadataOut"] = t.struct(
        {
            "operationType": t.string().optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1beta1CommonMetadataOut"])
    types["PropertyFilterIn"] = t.struct(
        {
            "op": t.string().optional(),
            "value": t.proxy(renames["ValueIn"]).optional(),
            "property": t.proxy(renames["PropertyReferenceIn"]).optional(),
        }
    ).named(renames["PropertyFilterIn"])
    types["PropertyFilterOut"] = t.struct(
        {
            "op": t.string().optional(),
            "value": t.proxy(renames["ValueOut"]).optional(),
            "property": t.proxy(renames["PropertyReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PropertyFilterOut"])
    types["GoogleDatastoreAdminV1ExportEntitiesRequestIn"] = t.struct(
        {
            "entityFilter": t.proxy(
                renames["GoogleDatastoreAdminV1EntityFilterIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "outputUrlPrefix": t.string(),
        }
    ).named(renames["GoogleDatastoreAdminV1ExportEntitiesRequestIn"])
    types["GoogleDatastoreAdminV1ExportEntitiesRequestOut"] = t.struct(
        {
            "entityFilter": t.proxy(
                renames["GoogleDatastoreAdminV1EntityFilterOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "outputUrlPrefix": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1ExportEntitiesRequestOut"])
    types["AggregationResultIn"] = t.struct(
        {"aggregateProperties": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["AggregationResultIn"])
    types["AggregationResultOut"] = t.struct(
        {
            "aggregateProperties": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationResultOut"])
    types["GoogleDatastoreAdminV1DatastoreFirestoreMigrationMetadataIn"] = t.struct(
        {
            "migrationState": t.string().optional(),
            "migrationStep": t.string().optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1DatastoreFirestoreMigrationMetadataIn"])
    types["GoogleDatastoreAdminV1DatastoreFirestoreMigrationMetadataOut"] = t.struct(
        {
            "migrationState": t.string().optional(),
            "migrationStep": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1DatastoreFirestoreMigrationMetadataOut"])
    types["ValueIn"] = t.struct(
        {
            "doubleValue": t.number().optional(),
            "integerValue": t.string().optional(),
            "entityValue": t.proxy(renames["EntityIn"]).optional(),
            "blobValue": t.string().optional(),
            "geoPointValue": t.proxy(renames["LatLngIn"]).optional(),
            "nullValue": t.string().optional(),
            "stringValue": t.string().optional(),
            "booleanValue": t.boolean().optional(),
            "keyValue": t.proxy(renames["KeyIn"]).optional(),
            "timestampValue": t.string().optional(),
            "arrayValue": t.proxy(renames["ArrayValueIn"]).optional(),
            "meaning": t.integer().optional(),
            "excludeFromIndexes": t.boolean().optional(),
        }
    ).named(renames["ValueIn"])
    types["ValueOut"] = t.struct(
        {
            "doubleValue": t.number().optional(),
            "integerValue": t.string().optional(),
            "entityValue": t.proxy(renames["EntityOut"]).optional(),
            "blobValue": t.string().optional(),
            "geoPointValue": t.proxy(renames["LatLngOut"]).optional(),
            "nullValue": t.string().optional(),
            "stringValue": t.string().optional(),
            "booleanValue": t.boolean().optional(),
            "keyValue": t.proxy(renames["KeyOut"]).optional(),
            "timestampValue": t.string().optional(),
            "arrayValue": t.proxy(renames["ArrayValueOut"]).optional(),
            "meaning": t.integer().optional(),
            "excludeFromIndexes": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueOut"])
    types["BeginTransactionResponseIn"] = t.struct(
        {"transaction": t.string().optional()}
    ).named(renames["BeginTransactionResponseIn"])
    types["BeginTransactionResponseOut"] = t.struct(
        {
            "transaction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BeginTransactionResponseOut"])
    types["GoogleDatastoreAdminV1MigrationStateEventIn"] = t.struct(
        {"state": t.string().optional()}
    ).named(renames["GoogleDatastoreAdminV1MigrationStateEventIn"])
    types["GoogleDatastoreAdminV1MigrationStateEventOut"] = t.struct(
        {
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1MigrationStateEventOut"])
    types["AllocateIdsResponseIn"] = t.struct(
        {"keys": t.array(t.proxy(renames["KeyIn"])).optional()}
    ).named(renames["AllocateIdsResponseIn"])
    types["AllocateIdsResponseOut"] = t.struct(
        {
            "keys": t.array(t.proxy(renames["KeyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AllocateIdsResponseOut"])
    types["BeginTransactionRequestIn"] = t.struct(
        {
            "transactionOptions": t.proxy(renames["TransactionOptionsIn"]).optional(),
            "databaseId": t.string().optional(),
        }
    ).named(renames["BeginTransactionRequestIn"])
    types["BeginTransactionRequestOut"] = t.struct(
        {
            "transactionOptions": t.proxy(renames["TransactionOptionsOut"]).optional(),
            "databaseId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BeginTransactionRequestOut"])
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
    types["RunAggregationQueryResponseIn"] = t.struct(
        {
            "batch": t.proxy(renames["AggregationResultBatchIn"]).optional(),
            "transaction": t.string().optional(),
            "query": t.proxy(renames["AggregationQueryIn"]).optional(),
        }
    ).named(renames["RunAggregationQueryResponseIn"])
    types["RunAggregationQueryResponseOut"] = t.struct(
        {
            "batch": t.proxy(renames["AggregationResultBatchOut"]).optional(),
            "transaction": t.string().optional(),
            "query": t.proxy(renames["AggregationQueryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunAggregationQueryResponseOut"])
    types["GoogleDatastoreAdminV1ExportEntitiesResponseIn"] = t.struct(
        {"outputUrl": t.string().optional()}
    ).named(renames["GoogleDatastoreAdminV1ExportEntitiesResponseIn"])
    types["GoogleDatastoreAdminV1ExportEntitiesResponseOut"] = t.struct(
        {
            "outputUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1ExportEntitiesResponseOut"])
    types["GoogleDatastoreAdminV1ProgressIn"] = t.struct(
        {"workEstimated": t.string().optional(), "workCompleted": t.string().optional()}
    ).named(renames["GoogleDatastoreAdminV1ProgressIn"])
    types["GoogleDatastoreAdminV1ProgressOut"] = t.struct(
        {
            "workEstimated": t.string().optional(),
            "workCompleted": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1ProgressOut"])
    types["AllocateIdsRequestIn"] = t.struct(
        {
            "databaseId": t.string().optional(),
            "keys": t.array(t.proxy(renames["KeyIn"])),
        }
    ).named(renames["AllocateIdsRequestIn"])
    types["AllocateIdsRequestOut"] = t.struct(
        {
            "databaseId": t.string().optional(),
            "keys": t.array(t.proxy(renames["KeyOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AllocateIdsRequestOut"])
    types["GoogleDatastoreAdminV1MigrationProgressEventIn"] = t.struct(
        {
            "redirectWritesStepDetails": t.proxy(
                renames["GoogleDatastoreAdminV1RedirectWritesStepDetailsIn"]
            ).optional(),
            "prepareStepDetails": t.proxy(
                renames["GoogleDatastoreAdminV1PrepareStepDetailsIn"]
            ).optional(),
            "step": t.string().optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1MigrationProgressEventIn"])
    types["GoogleDatastoreAdminV1MigrationProgressEventOut"] = t.struct(
        {
            "redirectWritesStepDetails": t.proxy(
                renames["GoogleDatastoreAdminV1RedirectWritesStepDetailsOut"]
            ).optional(),
            "prepareStepDetails": t.proxy(
                renames["GoogleDatastoreAdminV1PrepareStepDetailsOut"]
            ).optional(),
            "step": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1MigrationProgressEventOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleDatastoreAdminV1ListIndexesResponseIn"] = t.struct(
        {
            "indexes": t.array(
                t.proxy(renames["GoogleDatastoreAdminV1IndexIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1ListIndexesResponseIn"])
    types["GoogleDatastoreAdminV1ListIndexesResponseOut"] = t.struct(
        {
            "indexes": t.array(
                t.proxy(renames["GoogleDatastoreAdminV1IndexOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1ListIndexesResponseOut"])
    types["PropertyOrderIn"] = t.struct(
        {
            "direction": t.string().optional(),
            "property": t.proxy(renames["PropertyReferenceIn"]).optional(),
        }
    ).named(renames["PropertyOrderIn"])
    types["PropertyOrderOut"] = t.struct(
        {
            "direction": t.string().optional(),
            "property": t.proxy(renames["PropertyReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PropertyOrderOut"])
    types["ReadWriteIn"] = t.struct(
        {"previousTransaction": t.string().optional()}
    ).named(renames["ReadWriteIn"])
    types["ReadWriteOut"] = t.struct(
        {
            "previousTransaction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadWriteOut"])
    types["GoogleDatastoreAdminV1IndexOperationMetadataIn"] = t.struct(
        {
            "common": t.proxy(
                renames["GoogleDatastoreAdminV1CommonMetadataIn"]
            ).optional(),
            "progressEntities": t.proxy(
                renames["GoogleDatastoreAdminV1ProgressIn"]
            ).optional(),
            "indexId": t.string().optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1IndexOperationMetadataIn"])
    types["GoogleDatastoreAdminV1IndexOperationMetadataOut"] = t.struct(
        {
            "common": t.proxy(
                renames["GoogleDatastoreAdminV1CommonMetadataOut"]
            ).optional(),
            "progressEntities": t.proxy(
                renames["GoogleDatastoreAdminV1ProgressOut"]
            ).optional(),
            "indexId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1IndexOperationMetadataOut"])
    types["GoogleDatastoreAdminV1beta1ImportEntitiesMetadataIn"] = t.struct(
        {
            "common": t.proxy(
                renames["GoogleDatastoreAdminV1beta1CommonMetadataIn"]
            ).optional(),
            "inputUrl": t.string().optional(),
            "progressEntities": t.proxy(
                renames["GoogleDatastoreAdminV1beta1ProgressIn"]
            ).optional(),
            "entityFilter": t.proxy(
                renames["GoogleDatastoreAdminV1beta1EntityFilterIn"]
            ).optional(),
            "progressBytes": t.proxy(
                renames["GoogleDatastoreAdminV1beta1ProgressIn"]
            ).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1beta1ImportEntitiesMetadataIn"])
    types["GoogleDatastoreAdminV1beta1ImportEntitiesMetadataOut"] = t.struct(
        {
            "common": t.proxy(
                renames["GoogleDatastoreAdminV1beta1CommonMetadataOut"]
            ).optional(),
            "inputUrl": t.string().optional(),
            "progressEntities": t.proxy(
                renames["GoogleDatastoreAdminV1beta1ProgressOut"]
            ).optional(),
            "entityFilter": t.proxy(
                renames["GoogleDatastoreAdminV1beta1EntityFilterOut"]
            ).optional(),
            "progressBytes": t.proxy(
                renames["GoogleDatastoreAdminV1beta1ProgressOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1beta1ImportEntitiesMetadataOut"])
    types["PathElementIn"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PathElementIn"])
    types["PathElementOut"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PathElementOut"])
    types["ReserveIdsRequestIn"] = t.struct(
        {
            "keys": t.array(t.proxy(renames["KeyIn"])),
            "databaseId": t.string().optional(),
        }
    ).named(renames["ReserveIdsRequestIn"])
    types["ReserveIdsRequestOut"] = t.struct(
        {
            "keys": t.array(t.proxy(renames["KeyOut"])),
            "databaseId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReserveIdsRequestOut"])
    types["GoogleDatastoreAdminV1EntityFilterIn"] = t.struct(
        {
            "namespaceIds": t.array(t.string()).optional(),
            "kinds": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1EntityFilterIn"])
    types["GoogleDatastoreAdminV1EntityFilterOut"] = t.struct(
        {
            "namespaceIds": t.array(t.string()).optional(),
            "kinds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1EntityFilterOut"])
    types["CommitRequestIn"] = t.struct(
        {
            "transaction": t.string().optional(),
            "mode": t.string().optional(),
            "databaseId": t.string().optional(),
            "singleUseTransaction": t.proxy(renames["TransactionOptionsIn"]).optional(),
            "mutations": t.array(t.proxy(renames["MutationIn"])).optional(),
        }
    ).named(renames["CommitRequestIn"])
    types["CommitRequestOut"] = t.struct(
        {
            "transaction": t.string().optional(),
            "mode": t.string().optional(),
            "databaseId": t.string().optional(),
            "singleUseTransaction": t.proxy(
                renames["TransactionOptionsOut"]
            ).optional(),
            "mutations": t.array(t.proxy(renames["MutationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitRequestOut"])
    types["GoogleDatastoreAdminV1IndexIn"] = t.struct(
        {
            "properties": t.array(
                t.proxy(renames["GoogleDatastoreAdminV1IndexedPropertyIn"])
            ),
            "ancestor": t.string(),
            "kind": t.string(),
        }
    ).named(renames["GoogleDatastoreAdminV1IndexIn"])
    types["GoogleDatastoreAdminV1IndexOut"] = t.struct(
        {
            "properties": t.array(
                t.proxy(renames["GoogleDatastoreAdminV1IndexedPropertyOut"])
            ),
            "state": t.string().optional(),
            "indexId": t.string().optional(),
            "ancestor": t.string(),
            "kind": t.string(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1IndexOut"])
    types["ArrayValueIn"] = t.struct(
        {"values": t.array(t.proxy(renames["ValueIn"])).optional()}
    ).named(renames["ArrayValueIn"])
    types["ArrayValueOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["ValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArrayValueOut"])
    types["KeyIn"] = t.struct(
        {
            "partitionId": t.proxy(renames["PartitionIdIn"]).optional(),
            "path": t.array(t.proxy(renames["PathElementIn"])).optional(),
        }
    ).named(renames["KeyIn"])
    types["KeyOut"] = t.struct(
        {
            "partitionId": t.proxy(renames["PartitionIdOut"]).optional(),
            "path": t.array(t.proxy(renames["PathElementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyOut"])
    types["GoogleLongrunningListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationIn"])
            ).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseIn"])
    types["GoogleLongrunningListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseOut"])
    types["GoogleDatastoreAdminV1ImportEntitiesRequestIn"] = t.struct(
        {
            "entityFilter": t.proxy(
                renames["GoogleDatastoreAdminV1EntityFilterIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "inputUrl": t.string(),
        }
    ).named(renames["GoogleDatastoreAdminV1ImportEntitiesRequestIn"])
    types["GoogleDatastoreAdminV1ImportEntitiesRequestOut"] = t.struct(
        {
            "entityFilter": t.proxy(
                renames["GoogleDatastoreAdminV1EntityFilterOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "inputUrl": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1ImportEntitiesRequestOut"])
    types["EntityResultIn"] = t.struct(
        {
            "cursor": t.string().optional(),
            "createTime": t.string().optional(),
            "entity": t.proxy(renames["EntityIn"]).optional(),
            "version": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["EntityResultIn"])
    types["EntityResultOut"] = t.struct(
        {
            "cursor": t.string().optional(),
            "createTime": t.string().optional(),
            "entity": t.proxy(renames["EntityOut"]).optional(),
            "version": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityResultOut"])
    types["PropertyReferenceIn"] = t.struct({"name": t.string().optional()}).named(
        renames["PropertyReferenceIn"]
    )
    types["PropertyReferenceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PropertyReferenceOut"])
    types["TransactionOptionsIn"] = t.struct(
        {
            "readOnly": t.proxy(renames["ReadOnlyIn"]).optional(),
            "readWrite": t.proxy(renames["ReadWriteIn"]).optional(),
        }
    ).named(renames["TransactionOptionsIn"])
    types["TransactionOptionsOut"] = t.struct(
        {
            "readOnly": t.proxy(renames["ReadOnlyOut"]).optional(),
            "readWrite": t.proxy(renames["ReadWriteOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransactionOptionsOut"])
    types["CommitResponseIn"] = t.struct(
        {
            "indexUpdates": t.integer().optional(),
            "mutationResults": t.array(t.proxy(renames["MutationResultIn"])).optional(),
            "commitTime": t.string().optional(),
        }
    ).named(renames["CommitResponseIn"])
    types["CommitResponseOut"] = t.struct(
        {
            "indexUpdates": t.integer().optional(),
            "mutationResults": t.array(
                t.proxy(renames["MutationResultOut"])
            ).optional(),
            "commitTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitResponseOut"])
    types["LookupRequestIn"] = t.struct(
        {
            "readOptions": t.proxy(renames["ReadOptionsIn"]).optional(),
            "databaseId": t.string().optional(),
            "keys": t.array(t.proxy(renames["KeyIn"])),
        }
    ).named(renames["LookupRequestIn"])
    types["LookupRequestOut"] = t.struct(
        {
            "readOptions": t.proxy(renames["ReadOptionsOut"]).optional(),
            "databaseId": t.string().optional(),
            "keys": t.array(t.proxy(renames["KeyOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LookupRequestOut"])
    types["AggregationIn"] = t.struct(
        {
            "alias": t.string().optional(),
            "count": t.proxy(renames["CountIn"]).optional(),
        }
    ).named(renames["AggregationIn"])
    types["AggregationOut"] = t.struct(
        {
            "alias": t.string().optional(),
            "count": t.proxy(renames["CountOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationOut"])
    types["GoogleDatastoreAdminV1beta1EntityFilterIn"] = t.struct(
        {
            "namespaceIds": t.array(t.string()).optional(),
            "kinds": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1beta1EntityFilterIn"])
    types["GoogleDatastoreAdminV1beta1EntityFilterOut"] = t.struct(
        {
            "namespaceIds": t.array(t.string()).optional(),
            "kinds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1beta1EntityFilterOut"])
    types["ReserveIdsResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReserveIdsResponseIn"]
    )
    types["ReserveIdsResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReserveIdsResponseOut"])
    types["ReadOptionsIn"] = t.struct(
        {
            "transaction": t.string().optional(),
            "readConsistency": t.string().optional(),
            "newTransaction": t.proxy(renames["TransactionOptionsIn"]).optional(),
            "readTime": t.string().optional(),
        }
    ).named(renames["ReadOptionsIn"])
    types["ReadOptionsOut"] = t.struct(
        {
            "transaction": t.string().optional(),
            "readConsistency": t.string().optional(),
            "newTransaction": t.proxy(renames["TransactionOptionsOut"]).optional(),
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadOptionsOut"])
    types["LatLngIn"] = t.struct(
        {"latitude": t.number().optional(), "longitude": t.number().optional()}
    ).named(renames["LatLngIn"])
    types["LatLngOut"] = t.struct(
        {
            "latitude": t.number().optional(),
            "longitude": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LatLngOut"])
    types["QueryResultBatchIn"] = t.struct(
        {
            "snapshotVersion": t.string().optional(),
            "entityResults": t.array(t.proxy(renames["EntityResultIn"])).optional(),
            "moreResults": t.string().optional(),
            "entityResultType": t.string().optional(),
            "readTime": t.string().optional(),
            "skippedCursor": t.string().optional(),
            "endCursor": t.string().optional(),
            "skippedResults": t.integer().optional(),
        }
    ).named(renames["QueryResultBatchIn"])
    types["QueryResultBatchOut"] = t.struct(
        {
            "snapshotVersion": t.string().optional(),
            "entityResults": t.array(t.proxy(renames["EntityResultOut"])).optional(),
            "moreResults": t.string().optional(),
            "entityResultType": t.string().optional(),
            "readTime": t.string().optional(),
            "skippedCursor": t.string().optional(),
            "endCursor": t.string().optional(),
            "skippedResults": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryResultBatchOut"])
    types["GoogleDatastoreAdminV1RedirectWritesStepDetailsIn"] = t.struct(
        {"concurrencyMode": t.string().optional()}
    ).named(renames["GoogleDatastoreAdminV1RedirectWritesStepDetailsIn"])
    types["GoogleDatastoreAdminV1RedirectWritesStepDetailsOut"] = t.struct(
        {
            "concurrencyMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1RedirectWritesStepDetailsOut"])
    types["GqlQueryParameterIn"] = t.struct(
        {
            "cursor": t.string().optional(),
            "value": t.proxy(renames["ValueIn"]).optional(),
        }
    ).named(renames["GqlQueryParameterIn"])
    types["GqlQueryParameterOut"] = t.struct(
        {
            "cursor": t.string().optional(),
            "value": t.proxy(renames["ValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GqlQueryParameterOut"])
    types["GoogleDatastoreAdminV1ImportEntitiesMetadataIn"] = t.struct(
        {
            "entityFilter": t.proxy(
                renames["GoogleDatastoreAdminV1EntityFilterIn"]
            ).optional(),
            "progressEntities": t.proxy(
                renames["GoogleDatastoreAdminV1ProgressIn"]
            ).optional(),
            "common": t.proxy(
                renames["GoogleDatastoreAdminV1CommonMetadataIn"]
            ).optional(),
            "progressBytes": t.proxy(
                renames["GoogleDatastoreAdminV1ProgressIn"]
            ).optional(),
            "inputUrl": t.string().optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1ImportEntitiesMetadataIn"])
    types["GoogleDatastoreAdminV1ImportEntitiesMetadataOut"] = t.struct(
        {
            "entityFilter": t.proxy(
                renames["GoogleDatastoreAdminV1EntityFilterOut"]
            ).optional(),
            "progressEntities": t.proxy(
                renames["GoogleDatastoreAdminV1ProgressOut"]
            ).optional(),
            "common": t.proxy(
                renames["GoogleDatastoreAdminV1CommonMetadataOut"]
            ).optional(),
            "progressBytes": t.proxy(
                renames["GoogleDatastoreAdminV1ProgressOut"]
            ).optional(),
            "inputUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1ImportEntitiesMetadataOut"])
    types["PartitionIdIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "namespaceId": t.string().optional(),
            "databaseId": t.string().optional(),
        }
    ).named(renames["PartitionIdIn"])
    types["PartitionIdOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "namespaceId": t.string().optional(),
            "databaseId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionIdOut"])
    types["GoogleDatastoreAdminV1CommonMetadataIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "operationType": t.string().optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1CommonMetadataIn"])
    types["GoogleDatastoreAdminV1CommonMetadataOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "operationType": t.string().optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1CommonMetadataOut"])
    types["GoogleDatastoreAdminV1IndexedPropertyIn"] = t.struct(
        {"direction": t.string(), "name": t.string()}
    ).named(renames["GoogleDatastoreAdminV1IndexedPropertyIn"])
    types["GoogleDatastoreAdminV1IndexedPropertyOut"] = t.struct(
        {
            "direction": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1IndexedPropertyOut"])
    types["ReadOnlyIn"] = t.struct({"readTime": t.string().optional()}).named(
        renames["ReadOnlyIn"]
    )
    types["ReadOnlyOut"] = t.struct(
        {
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadOnlyOut"])
    types["FilterIn"] = t.struct(
        {
            "propertyFilter": t.proxy(renames["PropertyFilterIn"]).optional(),
            "compositeFilter": t.proxy(renames["CompositeFilterIn"]).optional(),
        }
    ).named(renames["FilterIn"])
    types["FilterOut"] = t.struct(
        {
            "propertyFilter": t.proxy(renames["PropertyFilterOut"]).optional(),
            "compositeFilter": t.proxy(renames["CompositeFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterOut"])
    types["GoogleDatastoreAdminV1ExportEntitiesMetadataIn"] = t.struct(
        {
            "progressEntities": t.proxy(
                renames["GoogleDatastoreAdminV1ProgressIn"]
            ).optional(),
            "common": t.proxy(
                renames["GoogleDatastoreAdminV1CommonMetadataIn"]
            ).optional(),
            "entityFilter": t.proxy(
                renames["GoogleDatastoreAdminV1EntityFilterIn"]
            ).optional(),
            "outputUrlPrefix": t.string().optional(),
            "progressBytes": t.proxy(
                renames["GoogleDatastoreAdminV1ProgressIn"]
            ).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1ExportEntitiesMetadataIn"])
    types["GoogleDatastoreAdminV1ExportEntitiesMetadataOut"] = t.struct(
        {
            "progressEntities": t.proxy(
                renames["GoogleDatastoreAdminV1ProgressOut"]
            ).optional(),
            "common": t.proxy(
                renames["GoogleDatastoreAdminV1CommonMetadataOut"]
            ).optional(),
            "entityFilter": t.proxy(
                renames["GoogleDatastoreAdminV1EntityFilterOut"]
            ).optional(),
            "outputUrlPrefix": t.string().optional(),
            "progressBytes": t.proxy(
                renames["GoogleDatastoreAdminV1ProgressOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1ExportEntitiesMetadataOut"])
    types["RunQueryResponseIn"] = t.struct(
        {
            "transaction": t.string().optional(),
            "batch": t.proxy(renames["QueryResultBatchIn"]).optional(),
            "query": t.proxy(renames["QueryIn"]).optional(),
        }
    ).named(renames["RunQueryResponseIn"])
    types["RunQueryResponseOut"] = t.struct(
        {
            "transaction": t.string().optional(),
            "batch": t.proxy(renames["QueryResultBatchOut"]).optional(),
            "query": t.proxy(renames["QueryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunQueryResponseOut"])
    types["KindExpressionIn"] = t.struct({"name": t.string().optional()}).named(
        renames["KindExpressionIn"]
    )
    types["KindExpressionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KindExpressionOut"])
    types["ProjectionIn"] = t.struct(
        {"property": t.proxy(renames["PropertyReferenceIn"]).optional()}
    ).named(renames["ProjectionIn"])
    types["ProjectionOut"] = t.struct(
        {
            "property": t.proxy(renames["PropertyReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectionOut"])
    types["RunQueryRequestIn"] = t.struct(
        {
            "databaseId": t.string().optional(),
            "partitionId": t.proxy(renames["PartitionIdIn"]).optional(),
            "query": t.proxy(renames["QueryIn"]).optional(),
            "gqlQuery": t.proxy(renames["GqlQueryIn"]).optional(),
            "readOptions": t.proxy(renames["ReadOptionsIn"]).optional(),
        }
    ).named(renames["RunQueryRequestIn"])
    types["RunQueryRequestOut"] = t.struct(
        {
            "databaseId": t.string().optional(),
            "partitionId": t.proxy(renames["PartitionIdOut"]).optional(),
            "query": t.proxy(renames["QueryOut"]).optional(),
            "gqlQuery": t.proxy(renames["GqlQueryOut"]).optional(),
            "readOptions": t.proxy(renames["ReadOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunQueryRequestOut"])
    types["CompositeFilterIn"] = t.struct(
        {
            "filters": t.array(t.proxy(renames["FilterIn"])).optional(),
            "op": t.string().optional(),
        }
    ).named(renames["CompositeFilterIn"])
    types["CompositeFilterOut"] = t.struct(
        {
            "filters": t.array(t.proxy(renames["FilterOut"])).optional(),
            "op": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompositeFilterOut"])
    types["GoogleDatastoreAdminV1PrepareStepDetailsIn"] = t.struct(
        {"concurrencyMode": t.string().optional()}
    ).named(renames["GoogleDatastoreAdminV1PrepareStepDetailsIn"])
    types["GoogleDatastoreAdminV1PrepareStepDetailsOut"] = t.struct(
        {
            "concurrencyMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1PrepareStepDetailsOut"])
    types["GoogleDatastoreAdminV1beta1ProgressIn"] = t.struct(
        {"workEstimated": t.string().optional(), "workCompleted": t.string().optional()}
    ).named(renames["GoogleDatastoreAdminV1beta1ProgressIn"])
    types["GoogleDatastoreAdminV1beta1ProgressOut"] = t.struct(
        {
            "workEstimated": t.string().optional(),
            "workCompleted": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1beta1ProgressOut"])
    types["RunAggregationQueryRequestIn"] = t.struct(
        {
            "databaseId": t.string().optional(),
            "readOptions": t.proxy(renames["ReadOptionsIn"]).optional(),
            "gqlQuery": t.proxy(renames["GqlQueryIn"]).optional(),
            "aggregationQuery": t.proxy(renames["AggregationQueryIn"]).optional(),
            "partitionId": t.proxy(renames["PartitionIdIn"]).optional(),
        }
    ).named(renames["RunAggregationQueryRequestIn"])
    types["RunAggregationQueryRequestOut"] = t.struct(
        {
            "databaseId": t.string().optional(),
            "readOptions": t.proxy(renames["ReadOptionsOut"]).optional(),
            "gqlQuery": t.proxy(renames["GqlQueryOut"]).optional(),
            "aggregationQuery": t.proxy(renames["AggregationQueryOut"]).optional(),
            "partitionId": t.proxy(renames["PartitionIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunAggregationQueryRequestOut"])
    types["GqlQueryIn"] = t.struct(
        {
            "allowLiterals": t.boolean().optional(),
            "namedBindings": t.struct({"_": t.string().optional()}).optional(),
            "positionalBindings": t.array(
                t.proxy(renames["GqlQueryParameterIn"])
            ).optional(),
            "queryString": t.string().optional(),
        }
    ).named(renames["GqlQueryIn"])
    types["GqlQueryOut"] = t.struct(
        {
            "allowLiterals": t.boolean().optional(),
            "namedBindings": t.struct({"_": t.string().optional()}).optional(),
            "positionalBindings": t.array(
                t.proxy(renames["GqlQueryParameterOut"])
            ).optional(),
            "queryString": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GqlQueryOut"])
    types["GoogleDatastoreAdminV1beta1ExportEntitiesMetadataIn"] = t.struct(
        {
            "common": t.proxy(
                renames["GoogleDatastoreAdminV1beta1CommonMetadataIn"]
            ).optional(),
            "entityFilter": t.proxy(
                renames["GoogleDatastoreAdminV1beta1EntityFilterIn"]
            ).optional(),
            "progressEntities": t.proxy(
                renames["GoogleDatastoreAdminV1beta1ProgressIn"]
            ).optional(),
            "outputUrlPrefix": t.string().optional(),
            "progressBytes": t.proxy(
                renames["GoogleDatastoreAdminV1beta1ProgressIn"]
            ).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1beta1ExportEntitiesMetadataIn"])
    types["GoogleDatastoreAdminV1beta1ExportEntitiesMetadataOut"] = t.struct(
        {
            "common": t.proxy(
                renames["GoogleDatastoreAdminV1beta1CommonMetadataOut"]
            ).optional(),
            "entityFilter": t.proxy(
                renames["GoogleDatastoreAdminV1beta1EntityFilterOut"]
            ).optional(),
            "progressEntities": t.proxy(
                renames["GoogleDatastoreAdminV1beta1ProgressOut"]
            ).optional(),
            "outputUrlPrefix": t.string().optional(),
            "progressBytes": t.proxy(
                renames["GoogleDatastoreAdminV1beta1ProgressOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1beta1ExportEntitiesMetadataOut"])
    types["GoogleDatastoreAdminV1beta1ExportEntitiesResponseIn"] = t.struct(
        {"outputUrl": t.string().optional()}
    ).named(renames["GoogleDatastoreAdminV1beta1ExportEntitiesResponseIn"])
    types["GoogleDatastoreAdminV1beta1ExportEntitiesResponseOut"] = t.struct(
        {
            "outputUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1beta1ExportEntitiesResponseOut"])
    types["RollbackResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RollbackResponseIn"]
    )
    types["RollbackResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RollbackResponseOut"])
    types["AggregationQueryIn"] = t.struct(
        {
            "nestedQuery": t.proxy(renames["QueryIn"]).optional(),
            "aggregations": t.array(t.proxy(renames["AggregationIn"])).optional(),
        }
    ).named(renames["AggregationQueryIn"])
    types["AggregationQueryOut"] = t.struct(
        {
            "nestedQuery": t.proxy(renames["QueryOut"]).optional(),
            "aggregations": t.array(t.proxy(renames["AggregationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationQueryOut"])

    functions = {}
    functions["projectsCommit"] = datastore.post(
        "v1/projects/{projectId}:allocateIds",
        t.struct(
            {
                "projectId": t.string(),
                "databaseId": t.string().optional(),
                "keys": t.array(t.proxy(renames["KeyIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AllocateIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRunAggregationQuery"] = datastore.post(
        "v1/projects/{projectId}:allocateIds",
        t.struct(
            {
                "projectId": t.string(),
                "databaseId": t.string().optional(),
                "keys": t.array(t.proxy(renames["KeyIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AllocateIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRunQuery"] = datastore.post(
        "v1/projects/{projectId}:allocateIds",
        t.struct(
            {
                "projectId": t.string(),
                "databaseId": t.string().optional(),
                "keys": t.array(t.proxy(renames["KeyIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AllocateIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsExport"] = datastore.post(
        "v1/projects/{projectId}:allocateIds",
        t.struct(
            {
                "projectId": t.string(),
                "databaseId": t.string().optional(),
                "keys": t.array(t.proxy(renames["KeyIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AllocateIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBeginTransaction"] = datastore.post(
        "v1/projects/{projectId}:allocateIds",
        t.struct(
            {
                "projectId": t.string(),
                "databaseId": t.string().optional(),
                "keys": t.array(t.proxy(renames["KeyIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AllocateIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsImport"] = datastore.post(
        "v1/projects/{projectId}:allocateIds",
        t.struct(
            {
                "projectId": t.string(),
                "databaseId": t.string().optional(),
                "keys": t.array(t.proxy(renames["KeyIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AllocateIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReserveIds"] = datastore.post(
        "v1/projects/{projectId}:allocateIds",
        t.struct(
            {
                "projectId": t.string(),
                "databaseId": t.string().optional(),
                "keys": t.array(t.proxy(renames["KeyIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AllocateIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLookup"] = datastore.post(
        "v1/projects/{projectId}:allocateIds",
        t.struct(
            {
                "projectId": t.string(),
                "databaseId": t.string().optional(),
                "keys": t.array(t.proxy(renames["KeyIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AllocateIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRollback"] = datastore.post(
        "v1/projects/{projectId}:allocateIds",
        t.struct(
            {
                "projectId": t.string(),
                "databaseId": t.string().optional(),
                "keys": t.array(t.proxy(renames["KeyIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AllocateIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAllocateIds"] = datastore.post(
        "v1/projects/{projectId}:allocateIds",
        t.struct(
            {
                "projectId": t.string(),
                "databaseId": t.string().optional(),
                "keys": t.array(t.proxy(renames["KeyIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AllocateIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsDelete"] = datastore.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsCancel"] = datastore.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsList"] = datastore.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsGet"] = datastore.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIndexesGet"] = datastore.get(
        "v1/projects/{projectId}/indexes",
        t.struct(
            {
                "projectId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleDatastoreAdminV1ListIndexesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIndexesCreate"] = datastore.get(
        "v1/projects/{projectId}/indexes",
        t.struct(
            {
                "projectId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleDatastoreAdminV1ListIndexesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIndexesDelete"] = datastore.get(
        "v1/projects/{projectId}/indexes",
        t.struct(
            {
                "projectId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleDatastoreAdminV1ListIndexesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIndexesList"] = datastore.get(
        "v1/projects/{projectId}/indexes",
        t.struct(
            {
                "projectId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleDatastoreAdminV1ListIndexesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="datastore",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
