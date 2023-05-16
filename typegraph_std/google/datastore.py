from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_datastore() -> Import:
    datastore = HTTPRuntime("https://datastore.googleapis.com/")

    renames = {
        "ErrorResponse": "_datastore_1_ErrorResponse",
        "CommitRequestIn": "_datastore_2_CommitRequestIn",
        "CommitRequestOut": "_datastore_3_CommitRequestOut",
        "GoogleDatastoreAdminV1ProgressIn": "_datastore_4_GoogleDatastoreAdminV1ProgressIn",
        "GoogleDatastoreAdminV1ProgressOut": "_datastore_5_GoogleDatastoreAdminV1ProgressOut",
        "PathElementIn": "_datastore_6_PathElementIn",
        "PathElementOut": "_datastore_7_PathElementOut",
        "BeginTransactionRequestIn": "_datastore_8_BeginTransactionRequestIn",
        "BeginTransactionRequestOut": "_datastore_9_BeginTransactionRequestOut",
        "CommitResponseIn": "_datastore_10_CommitResponseIn",
        "CommitResponseOut": "_datastore_11_CommitResponseOut",
        "QueryResultBatchIn": "_datastore_12_QueryResultBatchIn",
        "QueryResultBatchOut": "_datastore_13_QueryResultBatchOut",
        "MutationIn": "_datastore_14_MutationIn",
        "MutationOut": "_datastore_15_MutationOut",
        "ReadOptionsIn": "_datastore_16_ReadOptionsIn",
        "ReadOptionsOut": "_datastore_17_ReadOptionsOut",
        "QueryIn": "_datastore_18_QueryIn",
        "QueryOut": "_datastore_19_QueryOut",
        "PartitionIdIn": "_datastore_20_PartitionIdIn",
        "PartitionIdOut": "_datastore_21_PartitionIdOut",
        "AggregationResultBatchIn": "_datastore_22_AggregationResultBatchIn",
        "AggregationResultBatchOut": "_datastore_23_AggregationResultBatchOut",
        "ArrayValueIn": "_datastore_24_ArrayValueIn",
        "ArrayValueOut": "_datastore_25_ArrayValueOut",
        "PropertyOrderIn": "_datastore_26_PropertyOrderIn",
        "PropertyOrderOut": "_datastore_27_PropertyOrderOut",
        "AllocateIdsResponseIn": "_datastore_28_AllocateIdsResponseIn",
        "AllocateIdsResponseOut": "_datastore_29_AllocateIdsResponseOut",
        "MutationResultIn": "_datastore_30_MutationResultIn",
        "MutationResultOut": "_datastore_31_MutationResultOut",
        "GoogleDatastoreAdminV1MigrationStateEventIn": "_datastore_32_GoogleDatastoreAdminV1MigrationStateEventIn",
        "GoogleDatastoreAdminV1MigrationStateEventOut": "_datastore_33_GoogleDatastoreAdminV1MigrationStateEventOut",
        "GoogleLongrunningListOperationsResponseIn": "_datastore_34_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_datastore_35_GoogleLongrunningListOperationsResponseOut",
        "GoogleDatastoreAdminV1beta1EntityFilterIn": "_datastore_36_GoogleDatastoreAdminV1beta1EntityFilterIn",
        "GoogleDatastoreAdminV1beta1EntityFilterOut": "_datastore_37_GoogleDatastoreAdminV1beta1EntityFilterOut",
        "LookupResponseIn": "_datastore_38_LookupResponseIn",
        "LookupResponseOut": "_datastore_39_LookupResponseOut",
        "GoogleDatastoreAdminV1PrepareStepDetailsIn": "_datastore_40_GoogleDatastoreAdminV1PrepareStepDetailsIn",
        "GoogleDatastoreAdminV1PrepareStepDetailsOut": "_datastore_41_GoogleDatastoreAdminV1PrepareStepDetailsOut",
        "AggregationQueryIn": "_datastore_42_AggregationQueryIn",
        "AggregationQueryOut": "_datastore_43_AggregationQueryOut",
        "RunQueryResponseIn": "_datastore_44_RunQueryResponseIn",
        "RunQueryResponseOut": "_datastore_45_RunQueryResponseOut",
        "GoogleLongrunningOperationIn": "_datastore_46_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_datastore_47_GoogleLongrunningOperationOut",
        "GoogleDatastoreAdminV1beta1CommonMetadataIn": "_datastore_48_GoogleDatastoreAdminV1beta1CommonMetadataIn",
        "GoogleDatastoreAdminV1beta1CommonMetadataOut": "_datastore_49_GoogleDatastoreAdminV1beta1CommonMetadataOut",
        "CountIn": "_datastore_50_CountIn",
        "CountOut": "_datastore_51_CountOut",
        "StatusIn": "_datastore_52_StatusIn",
        "StatusOut": "_datastore_53_StatusOut",
        "GoogleDatastoreAdminV1EntityFilterIn": "_datastore_54_GoogleDatastoreAdminV1EntityFilterIn",
        "GoogleDatastoreAdminV1EntityFilterOut": "_datastore_55_GoogleDatastoreAdminV1EntityFilterOut",
        "AggregationResultIn": "_datastore_56_AggregationResultIn",
        "AggregationResultOut": "_datastore_57_AggregationResultOut",
        "ProjectionIn": "_datastore_58_ProjectionIn",
        "ProjectionOut": "_datastore_59_ProjectionOut",
        "GoogleDatastoreAdminV1beta1ExportEntitiesMetadataIn": "_datastore_60_GoogleDatastoreAdminV1beta1ExportEntitiesMetadataIn",
        "GoogleDatastoreAdminV1beta1ExportEntitiesMetadataOut": "_datastore_61_GoogleDatastoreAdminV1beta1ExportEntitiesMetadataOut",
        "ReserveIdsRequestIn": "_datastore_62_ReserveIdsRequestIn",
        "ReserveIdsRequestOut": "_datastore_63_ReserveIdsRequestOut",
        "GqlQueryIn": "_datastore_64_GqlQueryIn",
        "GqlQueryOut": "_datastore_65_GqlQueryOut",
        "GoogleDatastoreAdminV1beta1ImportEntitiesMetadataIn": "_datastore_66_GoogleDatastoreAdminV1beta1ImportEntitiesMetadataIn",
        "GoogleDatastoreAdminV1beta1ImportEntitiesMetadataOut": "_datastore_67_GoogleDatastoreAdminV1beta1ImportEntitiesMetadataOut",
        "AggregationIn": "_datastore_68_AggregationIn",
        "AggregationOut": "_datastore_69_AggregationOut",
        "GoogleDatastoreAdminV1ListIndexesResponseIn": "_datastore_70_GoogleDatastoreAdminV1ListIndexesResponseIn",
        "GoogleDatastoreAdminV1ListIndexesResponseOut": "_datastore_71_GoogleDatastoreAdminV1ListIndexesResponseOut",
        "AllocateIdsRequestIn": "_datastore_72_AllocateIdsRequestIn",
        "AllocateIdsRequestOut": "_datastore_73_AllocateIdsRequestOut",
        "FilterIn": "_datastore_74_FilterIn",
        "FilterOut": "_datastore_75_FilterOut",
        "LookupRequestIn": "_datastore_76_LookupRequestIn",
        "LookupRequestOut": "_datastore_77_LookupRequestOut",
        "ReadWriteIn": "_datastore_78_ReadWriteIn",
        "ReadWriteOut": "_datastore_79_ReadWriteOut",
        "KeyIn": "_datastore_80_KeyIn",
        "KeyOut": "_datastore_81_KeyOut",
        "EntityResultIn": "_datastore_82_EntityResultIn",
        "EntityResultOut": "_datastore_83_EntityResultOut",
        "PropertyReferenceIn": "_datastore_84_PropertyReferenceIn",
        "PropertyReferenceOut": "_datastore_85_PropertyReferenceOut",
        "GoogleDatastoreAdminV1DatastoreFirestoreMigrationMetadataIn": "_datastore_86_GoogleDatastoreAdminV1DatastoreFirestoreMigrationMetadataIn",
        "GoogleDatastoreAdminV1DatastoreFirestoreMigrationMetadataOut": "_datastore_87_GoogleDatastoreAdminV1DatastoreFirestoreMigrationMetadataOut",
        "EmptyIn": "_datastore_88_EmptyIn",
        "EmptyOut": "_datastore_89_EmptyOut",
        "TransactionOptionsIn": "_datastore_90_TransactionOptionsIn",
        "TransactionOptionsOut": "_datastore_91_TransactionOptionsOut",
        "GoogleDatastoreAdminV1ExportEntitiesMetadataIn": "_datastore_92_GoogleDatastoreAdminV1ExportEntitiesMetadataIn",
        "GoogleDatastoreAdminV1ExportEntitiesMetadataOut": "_datastore_93_GoogleDatastoreAdminV1ExportEntitiesMetadataOut",
        "RunAggregationQueryResponseIn": "_datastore_94_RunAggregationQueryResponseIn",
        "RunAggregationQueryResponseOut": "_datastore_95_RunAggregationQueryResponseOut",
        "GoogleDatastoreAdminV1MigrationProgressEventIn": "_datastore_96_GoogleDatastoreAdminV1MigrationProgressEventIn",
        "GoogleDatastoreAdminV1MigrationProgressEventOut": "_datastore_97_GoogleDatastoreAdminV1MigrationProgressEventOut",
        "RollbackRequestIn": "_datastore_98_RollbackRequestIn",
        "RollbackRequestOut": "_datastore_99_RollbackRequestOut",
        "KindExpressionIn": "_datastore_100_KindExpressionIn",
        "KindExpressionOut": "_datastore_101_KindExpressionOut",
        "GoogleDatastoreAdminV1ExportEntitiesResponseIn": "_datastore_102_GoogleDatastoreAdminV1ExportEntitiesResponseIn",
        "GoogleDatastoreAdminV1ExportEntitiesResponseOut": "_datastore_103_GoogleDatastoreAdminV1ExportEntitiesResponseOut",
        "GoogleDatastoreAdminV1IndexedPropertyIn": "_datastore_104_GoogleDatastoreAdminV1IndexedPropertyIn",
        "GoogleDatastoreAdminV1IndexedPropertyOut": "_datastore_105_GoogleDatastoreAdminV1IndexedPropertyOut",
        "RollbackResponseIn": "_datastore_106_RollbackResponseIn",
        "RollbackResponseOut": "_datastore_107_RollbackResponseOut",
        "GoogleDatastoreAdminV1IndexOperationMetadataIn": "_datastore_108_GoogleDatastoreAdminV1IndexOperationMetadataIn",
        "GoogleDatastoreAdminV1IndexOperationMetadataOut": "_datastore_109_GoogleDatastoreAdminV1IndexOperationMetadataOut",
        "GoogleDatastoreAdminV1CommonMetadataIn": "_datastore_110_GoogleDatastoreAdminV1CommonMetadataIn",
        "GoogleDatastoreAdminV1CommonMetadataOut": "_datastore_111_GoogleDatastoreAdminV1CommonMetadataOut",
        "GqlQueryParameterIn": "_datastore_112_GqlQueryParameterIn",
        "GqlQueryParameterOut": "_datastore_113_GqlQueryParameterOut",
        "GoogleDatastoreAdminV1ImportEntitiesMetadataIn": "_datastore_114_GoogleDatastoreAdminV1ImportEntitiesMetadataIn",
        "GoogleDatastoreAdminV1ImportEntitiesMetadataOut": "_datastore_115_GoogleDatastoreAdminV1ImportEntitiesMetadataOut",
        "GoogleDatastoreAdminV1beta1ProgressIn": "_datastore_116_GoogleDatastoreAdminV1beta1ProgressIn",
        "GoogleDatastoreAdminV1beta1ProgressOut": "_datastore_117_GoogleDatastoreAdminV1beta1ProgressOut",
        "RunQueryRequestIn": "_datastore_118_RunQueryRequestIn",
        "RunQueryRequestOut": "_datastore_119_RunQueryRequestOut",
        "EntityIn": "_datastore_120_EntityIn",
        "EntityOut": "_datastore_121_EntityOut",
        "CompositeFilterIn": "_datastore_122_CompositeFilterIn",
        "CompositeFilterOut": "_datastore_123_CompositeFilterOut",
        "PropertyFilterIn": "_datastore_124_PropertyFilterIn",
        "PropertyFilterOut": "_datastore_125_PropertyFilterOut",
        "GoogleDatastoreAdminV1ExportEntitiesRequestIn": "_datastore_126_GoogleDatastoreAdminV1ExportEntitiesRequestIn",
        "GoogleDatastoreAdminV1ExportEntitiesRequestOut": "_datastore_127_GoogleDatastoreAdminV1ExportEntitiesRequestOut",
        "ReserveIdsResponseIn": "_datastore_128_ReserveIdsResponseIn",
        "ReserveIdsResponseOut": "_datastore_129_ReserveIdsResponseOut",
        "LatLngIn": "_datastore_130_LatLngIn",
        "LatLngOut": "_datastore_131_LatLngOut",
        "ValueIn": "_datastore_132_ValueIn",
        "ValueOut": "_datastore_133_ValueOut",
        "GoogleDatastoreAdminV1beta1ExportEntitiesResponseIn": "_datastore_134_GoogleDatastoreAdminV1beta1ExportEntitiesResponseIn",
        "GoogleDatastoreAdminV1beta1ExportEntitiesResponseOut": "_datastore_135_GoogleDatastoreAdminV1beta1ExportEntitiesResponseOut",
        "RunAggregationQueryRequestIn": "_datastore_136_RunAggregationQueryRequestIn",
        "RunAggregationQueryRequestOut": "_datastore_137_RunAggregationQueryRequestOut",
        "GoogleDatastoreAdminV1ImportEntitiesRequestIn": "_datastore_138_GoogleDatastoreAdminV1ImportEntitiesRequestIn",
        "GoogleDatastoreAdminV1ImportEntitiesRequestOut": "_datastore_139_GoogleDatastoreAdminV1ImportEntitiesRequestOut",
        "GoogleDatastoreAdminV1IndexIn": "_datastore_140_GoogleDatastoreAdminV1IndexIn",
        "GoogleDatastoreAdminV1IndexOut": "_datastore_141_GoogleDatastoreAdminV1IndexOut",
        "GoogleDatastoreAdminV1RedirectWritesStepDetailsIn": "_datastore_142_GoogleDatastoreAdminV1RedirectWritesStepDetailsIn",
        "GoogleDatastoreAdminV1RedirectWritesStepDetailsOut": "_datastore_143_GoogleDatastoreAdminV1RedirectWritesStepDetailsOut",
        "ReadOnlyIn": "_datastore_144_ReadOnlyIn",
        "ReadOnlyOut": "_datastore_145_ReadOnlyOut",
        "BeginTransactionResponseIn": "_datastore_146_BeginTransactionResponseIn",
        "BeginTransactionResponseOut": "_datastore_147_BeginTransactionResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CommitRequestIn"] = t.struct(
        {
            "transaction": t.string().optional(),
            "mutations": t.array(t.proxy(renames["MutationIn"])).optional(),
            "mode": t.string().optional(),
            "singleUseTransaction": t.proxy(renames["TransactionOptionsIn"]).optional(),
            "databaseId": t.string().optional(),
        }
    ).named(renames["CommitRequestIn"])
    types["CommitRequestOut"] = t.struct(
        {
            "transaction": t.string().optional(),
            "mutations": t.array(t.proxy(renames["MutationOut"])).optional(),
            "mode": t.string().optional(),
            "singleUseTransaction": t.proxy(
                renames["TransactionOptionsOut"]
            ).optional(),
            "databaseId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitRequestOut"])
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
    types["PathElementIn"] = t.struct(
        {
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["PathElementIn"])
    types["PathElementOut"] = t.struct(
        {
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PathElementOut"])
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
    types["CommitResponseIn"] = t.struct(
        {
            "commitTime": t.string().optional(),
            "mutationResults": t.array(t.proxy(renames["MutationResultIn"])).optional(),
            "indexUpdates": t.integer().optional(),
        }
    ).named(renames["CommitResponseIn"])
    types["CommitResponseOut"] = t.struct(
        {
            "commitTime": t.string().optional(),
            "mutationResults": t.array(
                t.proxy(renames["MutationResultOut"])
            ).optional(),
            "indexUpdates": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitResponseOut"])
    types["QueryResultBatchIn"] = t.struct(
        {
            "readTime": t.string().optional(),
            "skippedCursor": t.string().optional(),
            "snapshotVersion": t.string().optional(),
            "moreResults": t.string().optional(),
            "entityResultType": t.string().optional(),
            "entityResults": t.array(t.proxy(renames["EntityResultIn"])).optional(),
            "endCursor": t.string().optional(),
            "skippedResults": t.integer().optional(),
        }
    ).named(renames["QueryResultBatchIn"])
    types["QueryResultBatchOut"] = t.struct(
        {
            "readTime": t.string().optional(),
            "skippedCursor": t.string().optional(),
            "snapshotVersion": t.string().optional(),
            "moreResults": t.string().optional(),
            "entityResultType": t.string().optional(),
            "entityResults": t.array(t.proxy(renames["EntityResultOut"])).optional(),
            "endCursor": t.string().optional(),
            "skippedResults": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryResultBatchOut"])
    types["MutationIn"] = t.struct(
        {
            "update": t.proxy(renames["EntityIn"]).optional(),
            "baseVersion": t.string().optional(),
            "insert": t.proxy(renames["EntityIn"]).optional(),
            "delete": t.proxy(renames["KeyIn"]).optional(),
            "updateTime": t.string().optional(),
            "upsert": t.proxy(renames["EntityIn"]).optional(),
        }
    ).named(renames["MutationIn"])
    types["MutationOut"] = t.struct(
        {
            "update": t.proxy(renames["EntityOut"]).optional(),
            "baseVersion": t.string().optional(),
            "insert": t.proxy(renames["EntityOut"]).optional(),
            "delete": t.proxy(renames["KeyOut"]).optional(),
            "updateTime": t.string().optional(),
            "upsert": t.proxy(renames["EntityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MutationOut"])
    types["ReadOptionsIn"] = t.struct(
        {
            "newTransaction": t.proxy(renames["TransactionOptionsIn"]).optional(),
            "readConsistency": t.string().optional(),
            "readTime": t.string().optional(),
            "transaction": t.string().optional(),
        }
    ).named(renames["ReadOptionsIn"])
    types["ReadOptionsOut"] = t.struct(
        {
            "newTransaction": t.proxy(renames["TransactionOptionsOut"]).optional(),
            "readConsistency": t.string().optional(),
            "readTime": t.string().optional(),
            "transaction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadOptionsOut"])
    types["QueryIn"] = t.struct(
        {
            "projection": t.array(t.proxy(renames["ProjectionIn"])).optional(),
            "distinctOn": t.array(t.proxy(renames["PropertyReferenceIn"])).optional(),
            "endCursor": t.string().optional(),
            "startCursor": t.string().optional(),
            "limit": t.integer().optional(),
            "offset": t.integer().optional(),
            "filter": t.proxy(renames["FilterIn"]).optional(),
            "order": t.array(t.proxy(renames["PropertyOrderIn"])).optional(),
            "kind": t.array(t.proxy(renames["KindExpressionIn"])).optional(),
        }
    ).named(renames["QueryIn"])
    types["QueryOut"] = t.struct(
        {
            "projection": t.array(t.proxy(renames["ProjectionOut"])).optional(),
            "distinctOn": t.array(t.proxy(renames["PropertyReferenceOut"])).optional(),
            "endCursor": t.string().optional(),
            "startCursor": t.string().optional(),
            "limit": t.integer().optional(),
            "offset": t.integer().optional(),
            "filter": t.proxy(renames["FilterOut"]).optional(),
            "order": t.array(t.proxy(renames["PropertyOrderOut"])).optional(),
            "kind": t.array(t.proxy(renames["KindExpressionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryOut"])
    types["PartitionIdIn"] = t.struct(
        {
            "namespaceId": t.string().optional(),
            "projectId": t.string().optional(),
            "databaseId": t.string().optional(),
        }
    ).named(renames["PartitionIdIn"])
    types["PartitionIdOut"] = t.struct(
        {
            "namespaceId": t.string().optional(),
            "projectId": t.string().optional(),
            "databaseId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionIdOut"])
    types["AggregationResultBatchIn"] = t.struct(
        {
            "moreResults": t.string().optional(),
            "readTime": t.string().optional(),
            "aggregationResults": t.array(
                t.proxy(renames["AggregationResultIn"])
            ).optional(),
        }
    ).named(renames["AggregationResultBatchIn"])
    types["AggregationResultBatchOut"] = t.struct(
        {
            "moreResults": t.string().optional(),
            "readTime": t.string().optional(),
            "aggregationResults": t.array(
                t.proxy(renames["AggregationResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationResultBatchOut"])
    types["ArrayValueIn"] = t.struct(
        {"values": t.array(t.proxy(renames["ValueIn"])).optional()}
    ).named(renames["ArrayValueIn"])
    types["ArrayValueOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["ValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArrayValueOut"])
    types["PropertyOrderIn"] = t.struct(
        {
            "property": t.proxy(renames["PropertyReferenceIn"]).optional(),
            "direction": t.string().optional(),
        }
    ).named(renames["PropertyOrderIn"])
    types["PropertyOrderOut"] = t.struct(
        {
            "property": t.proxy(renames["PropertyReferenceOut"]).optional(),
            "direction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PropertyOrderOut"])
    types["AllocateIdsResponseIn"] = t.struct(
        {"keys": t.array(t.proxy(renames["KeyIn"])).optional()}
    ).named(renames["AllocateIdsResponseIn"])
    types["AllocateIdsResponseOut"] = t.struct(
        {
            "keys": t.array(t.proxy(renames["KeyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AllocateIdsResponseOut"])
    types["MutationResultIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "conflictDetected": t.boolean().optional(),
            "key": t.proxy(renames["KeyIn"]).optional(),
            "updateTime": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["MutationResultIn"])
    types["MutationResultOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "conflictDetected": t.boolean().optional(),
            "key": t.proxy(renames["KeyOut"]).optional(),
            "updateTime": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MutationResultOut"])
    types["GoogleDatastoreAdminV1MigrationStateEventIn"] = t.struct(
        {"state": t.string().optional()}
    ).named(renames["GoogleDatastoreAdminV1MigrationStateEventIn"])
    types["GoogleDatastoreAdminV1MigrationStateEventOut"] = t.struct(
        {
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1MigrationStateEventOut"])
    types["GoogleLongrunningListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseIn"])
    types["GoogleLongrunningListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseOut"])
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
    types["LookupResponseIn"] = t.struct(
        {
            "readTime": t.string().optional(),
            "deferred": t.array(t.proxy(renames["KeyIn"])).optional(),
            "missing": t.array(t.proxy(renames["EntityResultIn"])).optional(),
            "found": t.array(t.proxy(renames["EntityResultIn"])).optional(),
            "transaction": t.string().optional(),
        }
    ).named(renames["LookupResponseIn"])
    types["LookupResponseOut"] = t.struct(
        {
            "readTime": t.string().optional(),
            "deferred": t.array(t.proxy(renames["KeyOut"])).optional(),
            "missing": t.array(t.proxy(renames["EntityResultOut"])).optional(),
            "found": t.array(t.proxy(renames["EntityResultOut"])).optional(),
            "transaction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LookupResponseOut"])
    types["GoogleDatastoreAdminV1PrepareStepDetailsIn"] = t.struct(
        {"concurrencyMode": t.string().optional()}
    ).named(renames["GoogleDatastoreAdminV1PrepareStepDetailsIn"])
    types["GoogleDatastoreAdminV1PrepareStepDetailsOut"] = t.struct(
        {
            "concurrencyMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1PrepareStepDetailsOut"])
    types["AggregationQueryIn"] = t.struct(
        {
            "aggregations": t.array(t.proxy(renames["AggregationIn"])).optional(),
            "nestedQuery": t.proxy(renames["QueryIn"]).optional(),
        }
    ).named(renames["AggregationQueryIn"])
    types["AggregationQueryOut"] = t.struct(
        {
            "aggregations": t.array(t.proxy(renames["AggregationOut"])).optional(),
            "nestedQuery": t.proxy(renames["QueryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationQueryOut"])
    types["RunQueryResponseIn"] = t.struct(
        {
            "batch": t.proxy(renames["QueryResultBatchIn"]).optional(),
            "query": t.proxy(renames["QueryIn"]).optional(),
            "transaction": t.string().optional(),
        }
    ).named(renames["RunQueryResponseIn"])
    types["RunQueryResponseOut"] = t.struct(
        {
            "batch": t.proxy(renames["QueryResultBatchOut"]).optional(),
            "query": t.proxy(renames["QueryOut"]).optional(),
            "transaction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunQueryResponseOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleDatastoreAdminV1beta1CommonMetadataIn"] = t.struct(
        {
            "operationType": t.string().optional(),
            "endTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1beta1CommonMetadataIn"])
    types["GoogleDatastoreAdminV1beta1CommonMetadataOut"] = t.struct(
        {
            "operationType": t.string().optional(),
            "endTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1beta1CommonMetadataOut"])
    types["CountIn"] = t.struct({"upTo": t.string().optional()}).named(
        renames["CountIn"]
    )
    types["CountOut"] = t.struct(
        {
            "upTo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CountOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["GoogleDatastoreAdminV1EntityFilterIn"] = t.struct(
        {
            "kinds": t.array(t.string()).optional(),
            "namespaceIds": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1EntityFilterIn"])
    types["GoogleDatastoreAdminV1EntityFilterOut"] = t.struct(
        {
            "kinds": t.array(t.string()).optional(),
            "namespaceIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1EntityFilterOut"])
    types["AggregationResultIn"] = t.struct(
        {"aggregateProperties": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["AggregationResultIn"])
    types["AggregationResultOut"] = t.struct(
        {
            "aggregateProperties": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationResultOut"])
    types["ProjectionIn"] = t.struct(
        {"property": t.proxy(renames["PropertyReferenceIn"]).optional()}
    ).named(renames["ProjectionIn"])
    types["ProjectionOut"] = t.struct(
        {
            "property": t.proxy(renames["PropertyReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectionOut"])
    types["GoogleDatastoreAdminV1beta1ExportEntitiesMetadataIn"] = t.struct(
        {
            "progressEntities": t.proxy(
                renames["GoogleDatastoreAdminV1beta1ProgressIn"]
            ).optional(),
            "outputUrlPrefix": t.string().optional(),
            "common": t.proxy(
                renames["GoogleDatastoreAdminV1beta1CommonMetadataIn"]
            ).optional(),
            "progressBytes": t.proxy(
                renames["GoogleDatastoreAdminV1beta1ProgressIn"]
            ).optional(),
            "entityFilter": t.proxy(
                renames["GoogleDatastoreAdminV1beta1EntityFilterIn"]
            ).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1beta1ExportEntitiesMetadataIn"])
    types["GoogleDatastoreAdminV1beta1ExportEntitiesMetadataOut"] = t.struct(
        {
            "progressEntities": t.proxy(
                renames["GoogleDatastoreAdminV1beta1ProgressOut"]
            ).optional(),
            "outputUrlPrefix": t.string().optional(),
            "common": t.proxy(
                renames["GoogleDatastoreAdminV1beta1CommonMetadataOut"]
            ).optional(),
            "progressBytes": t.proxy(
                renames["GoogleDatastoreAdminV1beta1ProgressOut"]
            ).optional(),
            "entityFilter": t.proxy(
                renames["GoogleDatastoreAdminV1beta1EntityFilterOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1beta1ExportEntitiesMetadataOut"])
    types["ReserveIdsRequestIn"] = t.struct(
        {
            "databaseId": t.string().optional(),
            "keys": t.array(t.proxy(renames["KeyIn"])),
        }
    ).named(renames["ReserveIdsRequestIn"])
    types["ReserveIdsRequestOut"] = t.struct(
        {
            "databaseId": t.string().optional(),
            "keys": t.array(t.proxy(renames["KeyOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReserveIdsRequestOut"])
    types["GqlQueryIn"] = t.struct(
        {
            "allowLiterals": t.boolean().optional(),
            "positionalBindings": t.array(
                t.proxy(renames["GqlQueryParameterIn"])
            ).optional(),
            "namedBindings": t.struct({"_": t.string().optional()}).optional(),
            "queryString": t.string().optional(),
        }
    ).named(renames["GqlQueryIn"])
    types["GqlQueryOut"] = t.struct(
        {
            "allowLiterals": t.boolean().optional(),
            "positionalBindings": t.array(
                t.proxy(renames["GqlQueryParameterOut"])
            ).optional(),
            "namedBindings": t.struct({"_": t.string().optional()}).optional(),
            "queryString": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GqlQueryOut"])
    types["GoogleDatastoreAdminV1beta1ImportEntitiesMetadataIn"] = t.struct(
        {
            "progressEntities": t.proxy(
                renames["GoogleDatastoreAdminV1beta1ProgressIn"]
            ).optional(),
            "progressBytes": t.proxy(
                renames["GoogleDatastoreAdminV1beta1ProgressIn"]
            ).optional(),
            "inputUrl": t.string().optional(),
            "entityFilter": t.proxy(
                renames["GoogleDatastoreAdminV1beta1EntityFilterIn"]
            ).optional(),
            "common": t.proxy(
                renames["GoogleDatastoreAdminV1beta1CommonMetadataIn"]
            ).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1beta1ImportEntitiesMetadataIn"])
    types["GoogleDatastoreAdminV1beta1ImportEntitiesMetadataOut"] = t.struct(
        {
            "progressEntities": t.proxy(
                renames["GoogleDatastoreAdminV1beta1ProgressOut"]
            ).optional(),
            "progressBytes": t.proxy(
                renames["GoogleDatastoreAdminV1beta1ProgressOut"]
            ).optional(),
            "inputUrl": t.string().optional(),
            "entityFilter": t.proxy(
                renames["GoogleDatastoreAdminV1beta1EntityFilterOut"]
            ).optional(),
            "common": t.proxy(
                renames["GoogleDatastoreAdminV1beta1CommonMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1beta1ImportEntitiesMetadataOut"])
    types["AggregationIn"] = t.struct(
        {
            "count": t.proxy(renames["CountIn"]).optional(),
            "alias": t.string().optional(),
        }
    ).named(renames["AggregationIn"])
    types["AggregationOut"] = t.struct(
        {
            "count": t.proxy(renames["CountOut"]).optional(),
            "alias": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationOut"])
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
    types["LookupRequestIn"] = t.struct(
        {
            "keys": t.array(t.proxy(renames["KeyIn"])),
            "readOptions": t.proxy(renames["ReadOptionsIn"]).optional(),
            "databaseId": t.string().optional(),
        }
    ).named(renames["LookupRequestIn"])
    types["LookupRequestOut"] = t.struct(
        {
            "keys": t.array(t.proxy(renames["KeyOut"])),
            "readOptions": t.proxy(renames["ReadOptionsOut"]).optional(),
            "databaseId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LookupRequestOut"])
    types["ReadWriteIn"] = t.struct(
        {"previousTransaction": t.string().optional()}
    ).named(renames["ReadWriteIn"])
    types["ReadWriteOut"] = t.struct(
        {
            "previousTransaction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadWriteOut"])
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
    types["EntityResultIn"] = t.struct(
        {
            "cursor": t.string().optional(),
            "version": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "entity": t.proxy(renames["EntityIn"]).optional(),
        }
    ).named(renames["EntityResultIn"])
    types["EntityResultOut"] = t.struct(
        {
            "cursor": t.string().optional(),
            "version": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "entity": t.proxy(renames["EntityOut"]).optional(),
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
    types["GoogleDatastoreAdminV1DatastoreFirestoreMigrationMetadataIn"] = t.struct(
        {
            "migrationStep": t.string().optional(),
            "migrationState": t.string().optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1DatastoreFirestoreMigrationMetadataIn"])
    types["GoogleDatastoreAdminV1DatastoreFirestoreMigrationMetadataOut"] = t.struct(
        {
            "migrationStep": t.string().optional(),
            "migrationState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1DatastoreFirestoreMigrationMetadataOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["GoogleDatastoreAdminV1ExportEntitiesMetadataIn"] = t.struct(
        {
            "progressBytes": t.proxy(
                renames["GoogleDatastoreAdminV1ProgressIn"]
            ).optional(),
            "common": t.proxy(
                renames["GoogleDatastoreAdminV1CommonMetadataIn"]
            ).optional(),
            "outputUrlPrefix": t.string().optional(),
            "entityFilter": t.proxy(
                renames["GoogleDatastoreAdminV1EntityFilterIn"]
            ).optional(),
            "progressEntities": t.proxy(
                renames["GoogleDatastoreAdminV1ProgressIn"]
            ).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1ExportEntitiesMetadataIn"])
    types["GoogleDatastoreAdminV1ExportEntitiesMetadataOut"] = t.struct(
        {
            "progressBytes": t.proxy(
                renames["GoogleDatastoreAdminV1ProgressOut"]
            ).optional(),
            "common": t.proxy(
                renames["GoogleDatastoreAdminV1CommonMetadataOut"]
            ).optional(),
            "outputUrlPrefix": t.string().optional(),
            "entityFilter": t.proxy(
                renames["GoogleDatastoreAdminV1EntityFilterOut"]
            ).optional(),
            "progressEntities": t.proxy(
                renames["GoogleDatastoreAdminV1ProgressOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1ExportEntitiesMetadataOut"])
    types["RunAggregationQueryResponseIn"] = t.struct(
        {
            "query": t.proxy(renames["AggregationQueryIn"]).optional(),
            "transaction": t.string().optional(),
            "batch": t.proxy(renames["AggregationResultBatchIn"]).optional(),
        }
    ).named(renames["RunAggregationQueryResponseIn"])
    types["RunAggregationQueryResponseOut"] = t.struct(
        {
            "query": t.proxy(renames["AggregationQueryOut"]).optional(),
            "transaction": t.string().optional(),
            "batch": t.proxy(renames["AggregationResultBatchOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunAggregationQueryResponseOut"])
    types["GoogleDatastoreAdminV1MigrationProgressEventIn"] = t.struct(
        {
            "step": t.string().optional(),
            "redirectWritesStepDetails": t.proxy(
                renames["GoogleDatastoreAdminV1RedirectWritesStepDetailsIn"]
            ).optional(),
            "prepareStepDetails": t.proxy(
                renames["GoogleDatastoreAdminV1PrepareStepDetailsIn"]
            ).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1MigrationProgressEventIn"])
    types["GoogleDatastoreAdminV1MigrationProgressEventOut"] = t.struct(
        {
            "step": t.string().optional(),
            "redirectWritesStepDetails": t.proxy(
                renames["GoogleDatastoreAdminV1RedirectWritesStepDetailsOut"]
            ).optional(),
            "prepareStepDetails": t.proxy(
                renames["GoogleDatastoreAdminV1PrepareStepDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1MigrationProgressEventOut"])
    types["RollbackRequestIn"] = t.struct(
        {"databaseId": t.string().optional(), "transaction": t.string()}
    ).named(renames["RollbackRequestIn"])
    types["RollbackRequestOut"] = t.struct(
        {
            "databaseId": t.string().optional(),
            "transaction": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RollbackRequestOut"])
    types["KindExpressionIn"] = t.struct({"name": t.string().optional()}).named(
        renames["KindExpressionIn"]
    )
    types["KindExpressionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KindExpressionOut"])
    types["GoogleDatastoreAdminV1ExportEntitiesResponseIn"] = t.struct(
        {"outputUrl": t.string().optional()}
    ).named(renames["GoogleDatastoreAdminV1ExportEntitiesResponseIn"])
    types["GoogleDatastoreAdminV1ExportEntitiesResponseOut"] = t.struct(
        {
            "outputUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1ExportEntitiesResponseOut"])
    types["GoogleDatastoreAdminV1IndexedPropertyIn"] = t.struct(
        {"name": t.string(), "direction": t.string()}
    ).named(renames["GoogleDatastoreAdminV1IndexedPropertyIn"])
    types["GoogleDatastoreAdminV1IndexedPropertyOut"] = t.struct(
        {
            "name": t.string(),
            "direction": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1IndexedPropertyOut"])
    types["RollbackResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RollbackResponseIn"]
    )
    types["RollbackResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RollbackResponseOut"])
    types["GoogleDatastoreAdminV1IndexOperationMetadataIn"] = t.struct(
        {
            "progressEntities": t.proxy(
                renames["GoogleDatastoreAdminV1ProgressIn"]
            ).optional(),
            "common": t.proxy(
                renames["GoogleDatastoreAdminV1CommonMetadataIn"]
            ).optional(),
            "indexId": t.string().optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1IndexOperationMetadataIn"])
    types["GoogleDatastoreAdminV1IndexOperationMetadataOut"] = t.struct(
        {
            "progressEntities": t.proxy(
                renames["GoogleDatastoreAdminV1ProgressOut"]
            ).optional(),
            "common": t.proxy(
                renames["GoogleDatastoreAdminV1CommonMetadataOut"]
            ).optional(),
            "indexId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1IndexOperationMetadataOut"])
    types["GoogleDatastoreAdminV1CommonMetadataIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "operationType": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1CommonMetadataIn"])
    types["GoogleDatastoreAdminV1CommonMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "operationType": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1CommonMetadataOut"])
    types["GqlQueryParameterIn"] = t.struct(
        {
            "value": t.proxy(renames["ValueIn"]).optional(),
            "cursor": t.string().optional(),
        }
    ).named(renames["GqlQueryParameterIn"])
    types["GqlQueryParameterOut"] = t.struct(
        {
            "value": t.proxy(renames["ValueOut"]).optional(),
            "cursor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GqlQueryParameterOut"])
    types["GoogleDatastoreAdminV1ImportEntitiesMetadataIn"] = t.struct(
        {
            "progressBytes": t.proxy(
                renames["GoogleDatastoreAdminV1ProgressIn"]
            ).optional(),
            "inputUrl": t.string().optional(),
            "entityFilter": t.proxy(
                renames["GoogleDatastoreAdminV1EntityFilterIn"]
            ).optional(),
            "common": t.proxy(
                renames["GoogleDatastoreAdminV1CommonMetadataIn"]
            ).optional(),
            "progressEntities": t.proxy(
                renames["GoogleDatastoreAdminV1ProgressIn"]
            ).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1ImportEntitiesMetadataIn"])
    types["GoogleDatastoreAdminV1ImportEntitiesMetadataOut"] = t.struct(
        {
            "progressBytes": t.proxy(
                renames["GoogleDatastoreAdminV1ProgressOut"]
            ).optional(),
            "inputUrl": t.string().optional(),
            "entityFilter": t.proxy(
                renames["GoogleDatastoreAdminV1EntityFilterOut"]
            ).optional(),
            "common": t.proxy(
                renames["GoogleDatastoreAdminV1CommonMetadataOut"]
            ).optional(),
            "progressEntities": t.proxy(
                renames["GoogleDatastoreAdminV1ProgressOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1ImportEntitiesMetadataOut"])
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
    types["RunQueryRequestIn"] = t.struct(
        {
            "partitionId": t.proxy(renames["PartitionIdIn"]).optional(),
            "gqlQuery": t.proxy(renames["GqlQueryIn"]).optional(),
            "query": t.proxy(renames["QueryIn"]).optional(),
            "databaseId": t.string().optional(),
            "readOptions": t.proxy(renames["ReadOptionsIn"]).optional(),
        }
    ).named(renames["RunQueryRequestIn"])
    types["RunQueryRequestOut"] = t.struct(
        {
            "partitionId": t.proxy(renames["PartitionIdOut"]).optional(),
            "gqlQuery": t.proxy(renames["GqlQueryOut"]).optional(),
            "query": t.proxy(renames["QueryOut"]).optional(),
            "databaseId": t.string().optional(),
            "readOptions": t.proxy(renames["ReadOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunQueryRequestOut"])
    types["EntityIn"] = t.struct(
        {
            "key": t.proxy(renames["KeyIn"]).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["EntityIn"])
    types["EntityOut"] = t.struct(
        {
            "key": t.proxy(renames["KeyOut"]).optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityOut"])
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
    types["PropertyFilterIn"] = t.struct(
        {
            "value": t.proxy(renames["ValueIn"]).optional(),
            "op": t.string().optional(),
            "property": t.proxy(renames["PropertyReferenceIn"]).optional(),
        }
    ).named(renames["PropertyFilterIn"])
    types["PropertyFilterOut"] = t.struct(
        {
            "value": t.proxy(renames["ValueOut"]).optional(),
            "op": t.string().optional(),
            "property": t.proxy(renames["PropertyReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PropertyFilterOut"])
    types["GoogleDatastoreAdminV1ExportEntitiesRequestIn"] = t.struct(
        {
            "outputUrlPrefix": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "entityFilter": t.proxy(
                renames["GoogleDatastoreAdminV1EntityFilterIn"]
            ).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1ExportEntitiesRequestIn"])
    types["GoogleDatastoreAdminV1ExportEntitiesRequestOut"] = t.struct(
        {
            "outputUrlPrefix": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "entityFilter": t.proxy(
                renames["GoogleDatastoreAdminV1EntityFilterOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1ExportEntitiesRequestOut"])
    types["ReserveIdsResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReserveIdsResponseIn"]
    )
    types["ReserveIdsResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReserveIdsResponseOut"])
    types["LatLngIn"] = t.struct(
        {"longitude": t.number().optional(), "latitude": t.number().optional()}
    ).named(renames["LatLngIn"])
    types["LatLngOut"] = t.struct(
        {
            "longitude": t.number().optional(),
            "latitude": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LatLngOut"])
    types["ValueIn"] = t.struct(
        {
            "integerValue": t.string().optional(),
            "arrayValue": t.proxy(renames["ArrayValueIn"]).optional(),
            "nullValue": t.string().optional(),
            "excludeFromIndexes": t.boolean().optional(),
            "geoPointValue": t.proxy(renames["LatLngIn"]).optional(),
            "meaning": t.integer().optional(),
            "doubleValue": t.number().optional(),
            "blobValue": t.string().optional(),
            "keyValue": t.proxy(renames["KeyIn"]).optional(),
            "entityValue": t.proxy(renames["EntityIn"]).optional(),
            "timestampValue": t.string().optional(),
            "booleanValue": t.boolean().optional(),
            "stringValue": t.string().optional(),
        }
    ).named(renames["ValueIn"])
    types["ValueOut"] = t.struct(
        {
            "integerValue": t.string().optional(),
            "arrayValue": t.proxy(renames["ArrayValueOut"]).optional(),
            "nullValue": t.string().optional(),
            "excludeFromIndexes": t.boolean().optional(),
            "geoPointValue": t.proxy(renames["LatLngOut"]).optional(),
            "meaning": t.integer().optional(),
            "doubleValue": t.number().optional(),
            "blobValue": t.string().optional(),
            "keyValue": t.proxy(renames["KeyOut"]).optional(),
            "entityValue": t.proxy(renames["EntityOut"]).optional(),
            "timestampValue": t.string().optional(),
            "booleanValue": t.boolean().optional(),
            "stringValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueOut"])
    types["GoogleDatastoreAdminV1beta1ExportEntitiesResponseIn"] = t.struct(
        {"outputUrl": t.string().optional()}
    ).named(renames["GoogleDatastoreAdminV1beta1ExportEntitiesResponseIn"])
    types["GoogleDatastoreAdminV1beta1ExportEntitiesResponseOut"] = t.struct(
        {
            "outputUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1beta1ExportEntitiesResponseOut"])
    types["RunAggregationQueryRequestIn"] = t.struct(
        {
            "databaseId": t.string().optional(),
            "aggregationQuery": t.proxy(renames["AggregationQueryIn"]).optional(),
            "readOptions": t.proxy(renames["ReadOptionsIn"]).optional(),
            "gqlQuery": t.proxy(renames["GqlQueryIn"]).optional(),
            "partitionId": t.proxy(renames["PartitionIdIn"]).optional(),
        }
    ).named(renames["RunAggregationQueryRequestIn"])
    types["RunAggregationQueryRequestOut"] = t.struct(
        {
            "databaseId": t.string().optional(),
            "aggregationQuery": t.proxy(renames["AggregationQueryOut"]).optional(),
            "readOptions": t.proxy(renames["ReadOptionsOut"]).optional(),
            "gqlQuery": t.proxy(renames["GqlQueryOut"]).optional(),
            "partitionId": t.proxy(renames["PartitionIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunAggregationQueryRequestOut"])
    types["GoogleDatastoreAdminV1ImportEntitiesRequestIn"] = t.struct(
        {
            "inputUrl": t.string(),
            "entityFilter": t.proxy(
                renames["GoogleDatastoreAdminV1EntityFilterIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1ImportEntitiesRequestIn"])
    types["GoogleDatastoreAdminV1ImportEntitiesRequestOut"] = t.struct(
        {
            "inputUrl": t.string(),
            "entityFilter": t.proxy(
                renames["GoogleDatastoreAdminV1EntityFilterOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1ImportEntitiesRequestOut"])
    types["GoogleDatastoreAdminV1IndexIn"] = t.struct(
        {
            "ancestor": t.string(),
            "kind": t.string(),
            "properties": t.array(
                t.proxy(renames["GoogleDatastoreAdminV1IndexedPropertyIn"])
            ),
        }
    ).named(renames["GoogleDatastoreAdminV1IndexIn"])
    types["GoogleDatastoreAdminV1IndexOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "indexId": t.string().optional(),
            "ancestor": t.string(),
            "kind": t.string(),
            "properties": t.array(
                t.proxy(renames["GoogleDatastoreAdminV1IndexedPropertyOut"])
            ),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1IndexOut"])
    types["GoogleDatastoreAdminV1RedirectWritesStepDetailsIn"] = t.struct(
        {"concurrencyMode": t.string().optional()}
    ).named(renames["GoogleDatastoreAdminV1RedirectWritesStepDetailsIn"])
    types["GoogleDatastoreAdminV1RedirectWritesStepDetailsOut"] = t.struct(
        {
            "concurrencyMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDatastoreAdminV1RedirectWritesStepDetailsOut"])
    types["ReadOnlyIn"] = t.struct({"readTime": t.string().optional()}).named(
        renames["ReadOnlyIn"]
    )
    types["ReadOnlyOut"] = t.struct(
        {
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadOnlyOut"])
    types["BeginTransactionResponseIn"] = t.struct(
        {"transaction": t.string().optional()}
    ).named(renames["BeginTransactionResponseIn"])
    types["BeginTransactionResponseOut"] = t.struct(
        {
            "transaction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BeginTransactionResponseOut"])

    functions = {}
    functions["projectsBeginTransaction"] = datastore.post(
        "v1/projects/{projectId}:export",
        t.struct(
            {
                "projectId": t.string(),
                "outputUrlPrefix": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "entityFilter": t.proxy(
                    renames["GoogleDatastoreAdminV1EntityFilterIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLookup"] = datastore.post(
        "v1/projects/{projectId}:export",
        t.struct(
            {
                "projectId": t.string(),
                "outputUrlPrefix": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "entityFilter": t.proxy(
                    renames["GoogleDatastoreAdminV1EntityFilterIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRunAggregationQuery"] = datastore.post(
        "v1/projects/{projectId}:export",
        t.struct(
            {
                "projectId": t.string(),
                "outputUrlPrefix": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "entityFilter": t.proxy(
                    renames["GoogleDatastoreAdminV1EntityFilterIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsCommit"] = datastore.post(
        "v1/projects/{projectId}:export",
        t.struct(
            {
                "projectId": t.string(),
                "outputUrlPrefix": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "entityFilter": t.proxy(
                    renames["GoogleDatastoreAdminV1EntityFilterIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRollback"] = datastore.post(
        "v1/projects/{projectId}:export",
        t.struct(
            {
                "projectId": t.string(),
                "outputUrlPrefix": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "entityFilter": t.proxy(
                    renames["GoogleDatastoreAdminV1EntityFilterIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReserveIds"] = datastore.post(
        "v1/projects/{projectId}:export",
        t.struct(
            {
                "projectId": t.string(),
                "outputUrlPrefix": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "entityFilter": t.proxy(
                    renames["GoogleDatastoreAdminV1EntityFilterIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRunQuery"] = datastore.post(
        "v1/projects/{projectId}:export",
        t.struct(
            {
                "projectId": t.string(),
                "outputUrlPrefix": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "entityFilter": t.proxy(
                    renames["GoogleDatastoreAdminV1EntityFilterIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAllocateIds"] = datastore.post(
        "v1/projects/{projectId}:export",
        t.struct(
            {
                "projectId": t.string(),
                "outputUrlPrefix": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "entityFilter": t.proxy(
                    renames["GoogleDatastoreAdminV1EntityFilterIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsImport"] = datastore.post(
        "v1/projects/{projectId}:export",
        t.struct(
            {
                "projectId": t.string(),
                "outputUrlPrefix": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "entityFilter": t.proxy(
                    renames["GoogleDatastoreAdminV1EntityFilterIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsExport"] = datastore.post(
        "v1/projects/{projectId}:export",
        t.struct(
            {
                "projectId": t.string(),
                "outputUrlPrefix": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "entityFilter": t.proxy(
                    renames["GoogleDatastoreAdminV1EntityFilterIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIndexesList"] = datastore.delete(
        "v1/projects/{projectId}/indexes/{indexId}",
        t.struct(
            {
                "projectId": t.string().optional(),
                "indexId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIndexesGet"] = datastore.delete(
        "v1/projects/{projectId}/indexes/{indexId}",
        t.struct(
            {
                "projectId": t.string().optional(),
                "indexId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIndexesCreate"] = datastore.delete(
        "v1/projects/{projectId}/indexes/{indexId}",
        t.struct(
            {
                "projectId": t.string().optional(),
                "indexId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIndexesDelete"] = datastore.delete(
        "v1/projects/{projectId}/indexes/{indexId}",
        t.struct(
            {
                "projectId": t.string().optional(),
                "indexId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsCancel"] = datastore.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsGet"] = datastore.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsList"] = datastore.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsDelete"] = datastore.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="datastore",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
