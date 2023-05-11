from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_firestore() -> Import:
    firestore = HTTPRuntime("https://firestore.googleapis.com/")

    renames = {
        "ErrorResponse": "_firestore_1_ErrorResponse",
        "GoogleFirestoreAdminV1TtlConfigIn": "_firestore_2_GoogleFirestoreAdminV1TtlConfigIn",
        "GoogleFirestoreAdminV1TtlConfigOut": "_firestore_3_GoogleFirestoreAdminV1TtlConfigOut",
        "DocumentChangeIn": "_firestore_4_DocumentChangeIn",
        "DocumentChangeOut": "_firestore_5_DocumentChangeOut",
        "FieldTransformIn": "_firestore_6_FieldTransformIn",
        "FieldTransformOut": "_firestore_7_FieldTransformOut",
        "GoogleFirestoreAdminV1UpdateDatabaseMetadataIn": "_firestore_8_GoogleFirestoreAdminV1UpdateDatabaseMetadataIn",
        "GoogleFirestoreAdminV1UpdateDatabaseMetadataOut": "_firestore_9_GoogleFirestoreAdminV1UpdateDatabaseMetadataOut",
        "GoogleFirestoreAdminV1ListFieldsResponseIn": "_firestore_10_GoogleFirestoreAdminV1ListFieldsResponseIn",
        "GoogleFirestoreAdminV1ListFieldsResponseOut": "_firestore_11_GoogleFirestoreAdminV1ListFieldsResponseOut",
        "ListenResponseIn": "_firestore_12_ListenResponseIn",
        "ListenResponseOut": "_firestore_13_ListenResponseOut",
        "ProjectionIn": "_firestore_14_ProjectionIn",
        "ProjectionOut": "_firestore_15_ProjectionOut",
        "TransactionOptionsIn": "_firestore_16_TransactionOptionsIn",
        "TransactionOptionsOut": "_firestore_17_TransactionOptionsOut",
        "FieldReferenceIn": "_firestore_18_FieldReferenceIn",
        "FieldReferenceOut": "_firestore_19_FieldReferenceOut",
        "RunQueryRequestIn": "_firestore_20_RunQueryRequestIn",
        "RunQueryRequestOut": "_firestore_21_RunQueryRequestOut",
        "GoogleFirestoreAdminV1IndexOperationMetadataIn": "_firestore_22_GoogleFirestoreAdminV1IndexOperationMetadataIn",
        "GoogleFirestoreAdminV1IndexOperationMetadataOut": "_firestore_23_GoogleFirestoreAdminV1IndexOperationMetadataOut",
        "GoogleFirestoreAdminV1IndexConfigDeltaIn": "_firestore_24_GoogleFirestoreAdminV1IndexConfigDeltaIn",
        "GoogleFirestoreAdminV1IndexConfigDeltaOut": "_firestore_25_GoogleFirestoreAdminV1IndexConfigDeltaOut",
        "ListenRequestIn": "_firestore_26_ListenRequestIn",
        "ListenRequestOut": "_firestore_27_ListenRequestOut",
        "GoogleLongrunningCancelOperationRequestIn": "_firestore_28_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_firestore_29_GoogleLongrunningCancelOperationRequestOut",
        "GoogleFirestoreAdminV1ImportDocumentsRequestIn": "_firestore_30_GoogleFirestoreAdminV1ImportDocumentsRequestIn",
        "GoogleFirestoreAdminV1ImportDocumentsRequestOut": "_firestore_31_GoogleFirestoreAdminV1ImportDocumentsRequestOut",
        "FieldFilterIn": "_firestore_32_FieldFilterIn",
        "FieldFilterOut": "_firestore_33_FieldFilterOut",
        "PartitionQueryRequestIn": "_firestore_34_PartitionQueryRequestIn",
        "PartitionQueryRequestOut": "_firestore_35_PartitionQueryRequestOut",
        "WriteResponseIn": "_firestore_36_WriteResponseIn",
        "WriteResponseOut": "_firestore_37_WriteResponseOut",
        "StatusIn": "_firestore_38_StatusIn",
        "StatusOut": "_firestore_39_StatusOut",
        "WriteResultIn": "_firestore_40_WriteResultIn",
        "WriteResultOut": "_firestore_41_WriteResultOut",
        "BatchWriteRequestIn": "_firestore_42_BatchWriteRequestIn",
        "BatchWriteRequestOut": "_firestore_43_BatchWriteRequestOut",
        "CursorIn": "_firestore_44_CursorIn",
        "CursorOut": "_firestore_45_CursorOut",
        "BeginTransactionResponseIn": "_firestore_46_BeginTransactionResponseIn",
        "BeginTransactionResponseOut": "_firestore_47_BeginTransactionResponseOut",
        "GoogleFirestoreAdminV1ProgressIn": "_firestore_48_GoogleFirestoreAdminV1ProgressIn",
        "GoogleFirestoreAdminV1ProgressOut": "_firestore_49_GoogleFirestoreAdminV1ProgressOut",
        "CompositeFilterIn": "_firestore_50_CompositeFilterIn",
        "CompositeFilterOut": "_firestore_51_CompositeFilterOut",
        "GoogleFirestoreAdminV1TtlConfigDeltaIn": "_firestore_52_GoogleFirestoreAdminV1TtlConfigDeltaIn",
        "GoogleFirestoreAdminV1TtlConfigDeltaOut": "_firestore_53_GoogleFirestoreAdminV1TtlConfigDeltaOut",
        "CommitRequestIn": "_firestore_54_CommitRequestIn",
        "CommitRequestOut": "_firestore_55_CommitRequestOut",
        "DocumentTransformIn": "_firestore_56_DocumentTransformIn",
        "DocumentTransformOut": "_firestore_57_DocumentTransformOut",
        "GoogleFirestoreAdminV1FieldOperationMetadataIn": "_firestore_58_GoogleFirestoreAdminV1FieldOperationMetadataIn",
        "GoogleFirestoreAdminV1FieldOperationMetadataOut": "_firestore_59_GoogleFirestoreAdminV1FieldOperationMetadataOut",
        "GoogleFirestoreAdminV1FieldIn": "_firestore_60_GoogleFirestoreAdminV1FieldIn",
        "GoogleFirestoreAdminV1FieldOut": "_firestore_61_GoogleFirestoreAdminV1FieldOut",
        "GoogleFirestoreAdminV1ExportDocumentsMetadataIn": "_firestore_62_GoogleFirestoreAdminV1ExportDocumentsMetadataIn",
        "GoogleFirestoreAdminV1ExportDocumentsMetadataOut": "_firestore_63_GoogleFirestoreAdminV1ExportDocumentsMetadataOut",
        "TargetIn": "_firestore_64_TargetIn",
        "TargetOut": "_firestore_65_TargetOut",
        "LatLngIn": "_firestore_66_LatLngIn",
        "LatLngOut": "_firestore_67_LatLngOut",
        "GoogleFirestoreAdminV1ExportDocumentsRequestIn": "_firestore_68_GoogleFirestoreAdminV1ExportDocumentsRequestIn",
        "GoogleFirestoreAdminV1ExportDocumentsRequestOut": "_firestore_69_GoogleFirestoreAdminV1ExportDocumentsRequestOut",
        "GoogleFirestoreAdminV1ExportDocumentsResponseIn": "_firestore_70_GoogleFirestoreAdminV1ExportDocumentsResponseIn",
        "GoogleFirestoreAdminV1ExportDocumentsResponseOut": "_firestore_71_GoogleFirestoreAdminV1ExportDocumentsResponseOut",
        "GoogleFirestoreAdminV1IndexFieldIn": "_firestore_72_GoogleFirestoreAdminV1IndexFieldIn",
        "GoogleFirestoreAdminV1IndexFieldOut": "_firestore_73_GoogleFirestoreAdminV1IndexFieldOut",
        "BatchWriteResponseIn": "_firestore_74_BatchWriteResponseIn",
        "BatchWriteResponseOut": "_firestore_75_BatchWriteResponseOut",
        "LocationIn": "_firestore_76_LocationIn",
        "LocationOut": "_firestore_77_LocationOut",
        "PartitionQueryResponseIn": "_firestore_78_PartitionQueryResponseIn",
        "PartitionQueryResponseOut": "_firestore_79_PartitionQueryResponseOut",
        "GoogleLongrunningOperationIn": "_firestore_80_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_firestore_81_GoogleLongrunningOperationOut",
        "GoogleFirestoreAdminV1DatabaseIn": "_firestore_82_GoogleFirestoreAdminV1DatabaseIn",
        "GoogleFirestoreAdminV1DatabaseOut": "_firestore_83_GoogleFirestoreAdminV1DatabaseOut",
        "CommitResponseIn": "_firestore_84_CommitResponseIn",
        "CommitResponseOut": "_firestore_85_CommitResponseOut",
        "CollectionSelectorIn": "_firestore_86_CollectionSelectorIn",
        "CollectionSelectorOut": "_firestore_87_CollectionSelectorOut",
        "EmptyIn": "_firestore_88_EmptyIn",
        "EmptyOut": "_firestore_89_EmptyOut",
        "StructuredAggregationQueryIn": "_firestore_90_StructuredAggregationQueryIn",
        "StructuredAggregationQueryOut": "_firestore_91_StructuredAggregationQueryOut",
        "ReadWriteIn": "_firestore_92_ReadWriteIn",
        "ReadWriteOut": "_firestore_93_ReadWriteOut",
        "StructuredQueryIn": "_firestore_94_StructuredQueryIn",
        "StructuredQueryOut": "_firestore_95_StructuredQueryOut",
        "RunAggregationQueryRequestIn": "_firestore_96_RunAggregationQueryRequestIn",
        "RunAggregationQueryRequestOut": "_firestore_97_RunAggregationQueryRequestOut",
        "PreconditionIn": "_firestore_98_PreconditionIn",
        "PreconditionOut": "_firestore_99_PreconditionOut",
        "DocumentDeleteIn": "_firestore_100_DocumentDeleteIn",
        "DocumentDeleteOut": "_firestore_101_DocumentDeleteOut",
        "MapValueIn": "_firestore_102_MapValueIn",
        "MapValueOut": "_firestore_103_MapValueOut",
        "GoogleFirestoreAdminV1ListIndexesResponseIn": "_firestore_104_GoogleFirestoreAdminV1ListIndexesResponseIn",
        "GoogleFirestoreAdminV1ListIndexesResponseOut": "_firestore_105_GoogleFirestoreAdminV1ListIndexesResponseOut",
        "GoogleFirestoreAdminV1LocationMetadataIn": "_firestore_106_GoogleFirestoreAdminV1LocationMetadataIn",
        "GoogleFirestoreAdminV1LocationMetadataOut": "_firestore_107_GoogleFirestoreAdminV1LocationMetadataOut",
        "UnaryFilterIn": "_firestore_108_UnaryFilterIn",
        "UnaryFilterOut": "_firestore_109_UnaryFilterOut",
        "DocumentMaskIn": "_firestore_110_DocumentMaskIn",
        "DocumentMaskOut": "_firestore_111_DocumentMaskOut",
        "ListCollectionIdsResponseIn": "_firestore_112_ListCollectionIdsResponseIn",
        "ListCollectionIdsResponseOut": "_firestore_113_ListCollectionIdsResponseOut",
        "GoogleFirestoreAdminV1IndexIn": "_firestore_114_GoogleFirestoreAdminV1IndexIn",
        "GoogleFirestoreAdminV1IndexOut": "_firestore_115_GoogleFirestoreAdminV1IndexOut",
        "DocumentsTargetIn": "_firestore_116_DocumentsTargetIn",
        "DocumentsTargetOut": "_firestore_117_DocumentsTargetOut",
        "GoogleFirestoreAdminV1IndexConfigIn": "_firestore_118_GoogleFirestoreAdminV1IndexConfigIn",
        "GoogleFirestoreAdminV1IndexConfigOut": "_firestore_119_GoogleFirestoreAdminV1IndexConfigOut",
        "ListCollectionIdsRequestIn": "_firestore_120_ListCollectionIdsRequestIn",
        "ListCollectionIdsRequestOut": "_firestore_121_ListCollectionIdsRequestOut",
        "QueryTargetIn": "_firestore_122_QueryTargetIn",
        "QueryTargetOut": "_firestore_123_QueryTargetOut",
        "GoogleFirestoreAdminV1ImportDocumentsMetadataIn": "_firestore_124_GoogleFirestoreAdminV1ImportDocumentsMetadataIn",
        "GoogleFirestoreAdminV1ImportDocumentsMetadataOut": "_firestore_125_GoogleFirestoreAdminV1ImportDocumentsMetadataOut",
        "AggregationResultIn": "_firestore_126_AggregationResultIn",
        "AggregationResultOut": "_firestore_127_AggregationResultOut",
        "RunQueryResponseIn": "_firestore_128_RunQueryResponseIn",
        "RunQueryResponseOut": "_firestore_129_RunQueryResponseOut",
        "ExistenceFilterIn": "_firestore_130_ExistenceFilterIn",
        "ExistenceFilterOut": "_firestore_131_ExistenceFilterOut",
        "DocumentIn": "_firestore_132_DocumentIn",
        "DocumentOut": "_firestore_133_DocumentOut",
        "RunAggregationQueryResponseIn": "_firestore_134_RunAggregationQueryResponseIn",
        "RunAggregationQueryResponseOut": "_firestore_135_RunAggregationQueryResponseOut",
        "FilterIn": "_firestore_136_FilterIn",
        "FilterOut": "_firestore_137_FilterOut",
        "DocumentRemoveIn": "_firestore_138_DocumentRemoveIn",
        "DocumentRemoveOut": "_firestore_139_DocumentRemoveOut",
        "WriteRequestIn": "_firestore_140_WriteRequestIn",
        "WriteRequestOut": "_firestore_141_WriteRequestOut",
        "GoogleFirestoreAdminV1ListDatabasesResponseIn": "_firestore_142_GoogleFirestoreAdminV1ListDatabasesResponseIn",
        "GoogleFirestoreAdminV1ListDatabasesResponseOut": "_firestore_143_GoogleFirestoreAdminV1ListDatabasesResponseOut",
        "BeginTransactionRequestIn": "_firestore_144_BeginTransactionRequestIn",
        "BeginTransactionRequestOut": "_firestore_145_BeginTransactionRequestOut",
        "TargetChangeIn": "_firestore_146_TargetChangeIn",
        "TargetChangeOut": "_firestore_147_TargetChangeOut",
        "ReadOnlyIn": "_firestore_148_ReadOnlyIn",
        "ReadOnlyOut": "_firestore_149_ReadOnlyOut",
        "ArrayValueIn": "_firestore_150_ArrayValueIn",
        "ArrayValueOut": "_firestore_151_ArrayValueOut",
        "ListDocumentsResponseIn": "_firestore_152_ListDocumentsResponseIn",
        "ListDocumentsResponseOut": "_firestore_153_ListDocumentsResponseOut",
        "ValueIn": "_firestore_154_ValueIn",
        "ValueOut": "_firestore_155_ValueOut",
        "WriteIn": "_firestore_156_WriteIn",
        "WriteOut": "_firestore_157_WriteOut",
        "ListLocationsResponseIn": "_firestore_158_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_firestore_159_ListLocationsResponseOut",
        "CountIn": "_firestore_160_CountIn",
        "CountOut": "_firestore_161_CountOut",
        "RollbackRequestIn": "_firestore_162_RollbackRequestIn",
        "RollbackRequestOut": "_firestore_163_RollbackRequestOut",
        "GoogleLongrunningListOperationsResponseIn": "_firestore_164_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_firestore_165_GoogleLongrunningListOperationsResponseOut",
        "OrderIn": "_firestore_166_OrderIn",
        "OrderOut": "_firestore_167_OrderOut",
        "AggregationIn": "_firestore_168_AggregationIn",
        "AggregationOut": "_firestore_169_AggregationOut",
        "BatchGetDocumentsResponseIn": "_firestore_170_BatchGetDocumentsResponseIn",
        "BatchGetDocumentsResponseOut": "_firestore_171_BatchGetDocumentsResponseOut",
        "BatchGetDocumentsRequestIn": "_firestore_172_BatchGetDocumentsRequestIn",
        "BatchGetDocumentsRequestOut": "_firestore_173_BatchGetDocumentsRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleFirestoreAdminV1TtlConfigIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1TtlConfigIn"])
    types["GoogleFirestoreAdminV1TtlConfigOut"] = t.struct(
        {
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1TtlConfigOut"])
    types["DocumentChangeIn"] = t.struct(
        {
            "document": t.proxy(renames["DocumentIn"]).optional(),
            "targetIds": t.array(t.integer()).optional(),
            "removedTargetIds": t.array(t.integer()).optional(),
        }
    ).named(renames["DocumentChangeIn"])
    types["DocumentChangeOut"] = t.struct(
        {
            "document": t.proxy(renames["DocumentOut"]).optional(),
            "targetIds": t.array(t.integer()).optional(),
            "removedTargetIds": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentChangeOut"])
    types["FieldTransformIn"] = t.struct(
        {
            "increment": t.proxy(renames["ValueIn"]).optional(),
            "removeAllFromArray": t.proxy(renames["ArrayValueIn"]).optional(),
            "appendMissingElements": t.proxy(renames["ArrayValueIn"]).optional(),
            "setToServerValue": t.string().optional(),
            "maximum": t.proxy(renames["ValueIn"]).optional(),
            "minimum": t.proxy(renames["ValueIn"]).optional(),
            "fieldPath": t.string().optional(),
        }
    ).named(renames["FieldTransformIn"])
    types["FieldTransformOut"] = t.struct(
        {
            "increment": t.proxy(renames["ValueOut"]).optional(),
            "removeAllFromArray": t.proxy(renames["ArrayValueOut"]).optional(),
            "appendMissingElements": t.proxy(renames["ArrayValueOut"]).optional(),
            "setToServerValue": t.string().optional(),
            "maximum": t.proxy(renames["ValueOut"]).optional(),
            "minimum": t.proxy(renames["ValueOut"]).optional(),
            "fieldPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldTransformOut"])
    types["GoogleFirestoreAdminV1UpdateDatabaseMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1UpdateDatabaseMetadataIn"])
    types["GoogleFirestoreAdminV1UpdateDatabaseMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleFirestoreAdminV1UpdateDatabaseMetadataOut"])
    types["GoogleFirestoreAdminV1ListFieldsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "fields": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1FieldIn"])
            ).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ListFieldsResponseIn"])
    types["GoogleFirestoreAdminV1ListFieldsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "fields": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1FieldOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ListFieldsResponseOut"])
    types["ListenResponseIn"] = t.struct(
        {
            "documentDelete": t.proxy(renames["DocumentDeleteIn"]).optional(),
            "documentChange": t.proxy(renames["DocumentChangeIn"]).optional(),
            "targetChange": t.proxy(renames["TargetChangeIn"]).optional(),
            "filter": t.proxy(renames["ExistenceFilterIn"]).optional(),
            "documentRemove": t.proxy(renames["DocumentRemoveIn"]).optional(),
        }
    ).named(renames["ListenResponseIn"])
    types["ListenResponseOut"] = t.struct(
        {
            "documentDelete": t.proxy(renames["DocumentDeleteOut"]).optional(),
            "documentChange": t.proxy(renames["DocumentChangeOut"]).optional(),
            "targetChange": t.proxy(renames["TargetChangeOut"]).optional(),
            "filter": t.proxy(renames["ExistenceFilterOut"]).optional(),
            "documentRemove": t.proxy(renames["DocumentRemoveOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListenResponseOut"])
    types["ProjectionIn"] = t.struct(
        {"fields": t.array(t.proxy(renames["FieldReferenceIn"])).optional()}
    ).named(renames["ProjectionIn"])
    types["ProjectionOut"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["FieldReferenceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectionOut"])
    types["TransactionOptionsIn"] = t.struct(
        {
            "readWrite": t.proxy(renames["ReadWriteIn"]).optional(),
            "readOnly": t.proxy(renames["ReadOnlyIn"]).optional(),
        }
    ).named(renames["TransactionOptionsIn"])
    types["TransactionOptionsOut"] = t.struct(
        {
            "readWrite": t.proxy(renames["ReadWriteOut"]).optional(),
            "readOnly": t.proxy(renames["ReadOnlyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransactionOptionsOut"])
    types["FieldReferenceIn"] = t.struct({"fieldPath": t.string().optional()}).named(
        renames["FieldReferenceIn"]
    )
    types["FieldReferenceOut"] = t.struct(
        {
            "fieldPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldReferenceOut"])
    types["RunQueryRequestIn"] = t.struct(
        {
            "structuredQuery": t.proxy(renames["StructuredQueryIn"]).optional(),
            "transaction": t.string().optional(),
            "readTime": t.string().optional(),
            "newTransaction": t.proxy(renames["TransactionOptionsIn"]).optional(),
        }
    ).named(renames["RunQueryRequestIn"])
    types["RunQueryRequestOut"] = t.struct(
        {
            "structuredQuery": t.proxy(renames["StructuredQueryOut"]).optional(),
            "transaction": t.string().optional(),
            "readTime": t.string().optional(),
            "newTransaction": t.proxy(renames["TransactionOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunQueryRequestOut"])
    types["GoogleFirestoreAdminV1IndexOperationMetadataIn"] = t.struct(
        {
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
            "state": t.string().optional(),
            "index": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexOperationMetadataIn"])
    types["GoogleFirestoreAdminV1IndexOperationMetadataOut"] = t.struct(
        {
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "state": t.string().optional(),
            "index": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexOperationMetadataOut"])
    types["GoogleFirestoreAdminV1IndexConfigDeltaIn"] = t.struct(
        {
            "changeType": t.string().optional(),
            "index": t.proxy(renames["GoogleFirestoreAdminV1IndexIn"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexConfigDeltaIn"])
    types["GoogleFirestoreAdminV1IndexConfigDeltaOut"] = t.struct(
        {
            "changeType": t.string().optional(),
            "index": t.proxy(renames["GoogleFirestoreAdminV1IndexOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexConfigDeltaOut"])
    types["ListenRequestIn"] = t.struct(
        {
            "addTarget": t.proxy(renames["TargetIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "removeTarget": t.integer().optional(),
        }
    ).named(renames["ListenRequestIn"])
    types["ListenRequestOut"] = t.struct(
        {
            "addTarget": t.proxy(renames["TargetOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "removeTarget": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListenRequestOut"])
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
    types["GoogleFirestoreAdminV1ImportDocumentsRequestIn"] = t.struct(
        {
            "collectionIds": t.array(t.string()).optional(),
            "inputUriPrefix": t.string().optional(),
            "namespaceIds": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ImportDocumentsRequestIn"])
    types["GoogleFirestoreAdminV1ImportDocumentsRequestOut"] = t.struct(
        {
            "collectionIds": t.array(t.string()).optional(),
            "inputUriPrefix": t.string().optional(),
            "namespaceIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ImportDocumentsRequestOut"])
    types["FieldFilterIn"] = t.struct(
        {
            "op": t.string().optional(),
            "field": t.proxy(renames["FieldReferenceIn"]).optional(),
            "value": t.proxy(renames["ValueIn"]).optional(),
        }
    ).named(renames["FieldFilterIn"])
    types["FieldFilterOut"] = t.struct(
        {
            "op": t.string().optional(),
            "field": t.proxy(renames["FieldReferenceOut"]).optional(),
            "value": t.proxy(renames["ValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldFilterOut"])
    types["PartitionQueryRequestIn"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "partitionCount": t.string().optional(),
            "structuredQuery": t.proxy(renames["StructuredQueryIn"]).optional(),
            "readTime": t.string().optional(),
        }
    ).named(renames["PartitionQueryRequestIn"])
    types["PartitionQueryRequestOut"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "partitionCount": t.string().optional(),
            "structuredQuery": t.proxy(renames["StructuredQueryOut"]).optional(),
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionQueryRequestOut"])
    types["WriteResponseIn"] = t.struct(
        {
            "commitTime": t.string().optional(),
            "writeResults": t.array(t.proxy(renames["WriteResultIn"])).optional(),
            "streamId": t.string().optional(),
            "streamToken": t.string().optional(),
        }
    ).named(renames["WriteResponseIn"])
    types["WriteResponseOut"] = t.struct(
        {
            "commitTime": t.string().optional(),
            "writeResults": t.array(t.proxy(renames["WriteResultOut"])).optional(),
            "streamId": t.string().optional(),
            "streamToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteResponseOut"])
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
    types["WriteResultIn"] = t.struct(
        {
            "transformResults": t.array(t.proxy(renames["ValueIn"])).optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["WriteResultIn"])
    types["WriteResultOut"] = t.struct(
        {
            "transformResults": t.array(t.proxy(renames["ValueOut"])).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteResultOut"])
    types["BatchWriteRequestIn"] = t.struct(
        {
            "writes": t.array(t.proxy(renames["WriteIn"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["BatchWriteRequestIn"])
    types["BatchWriteRequestOut"] = t.struct(
        {
            "writes": t.array(t.proxy(renames["WriteOut"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchWriteRequestOut"])
    types["CursorIn"] = t.struct(
        {
            "values": t.array(t.proxy(renames["ValueIn"])).optional(),
            "before": t.boolean().optional(),
        }
    ).named(renames["CursorIn"])
    types["CursorOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["ValueOut"])).optional(),
            "before": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CursorOut"])
    types["BeginTransactionResponseIn"] = t.struct(
        {"transaction": t.string().optional()}
    ).named(renames["BeginTransactionResponseIn"])
    types["BeginTransactionResponseOut"] = t.struct(
        {
            "transaction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BeginTransactionResponseOut"])
    types["GoogleFirestoreAdminV1ProgressIn"] = t.struct(
        {"completedWork": t.string().optional(), "estimatedWork": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1ProgressIn"])
    types["GoogleFirestoreAdminV1ProgressOut"] = t.struct(
        {
            "completedWork": t.string().optional(),
            "estimatedWork": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ProgressOut"])
    types["CompositeFilterIn"] = t.struct(
        {
            "op": t.string().optional(),
            "filters": t.array(t.proxy(renames["FilterIn"])).optional(),
        }
    ).named(renames["CompositeFilterIn"])
    types["CompositeFilterOut"] = t.struct(
        {
            "op": t.string().optional(),
            "filters": t.array(t.proxy(renames["FilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompositeFilterOut"])
    types["GoogleFirestoreAdminV1TtlConfigDeltaIn"] = t.struct(
        {"changeType": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1TtlConfigDeltaIn"])
    types["GoogleFirestoreAdminV1TtlConfigDeltaOut"] = t.struct(
        {
            "changeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1TtlConfigDeltaOut"])
    types["CommitRequestIn"] = t.struct(
        {
            "transaction": t.string().optional(),
            "writes": t.array(t.proxy(renames["WriteIn"])).optional(),
        }
    ).named(renames["CommitRequestIn"])
    types["CommitRequestOut"] = t.struct(
        {
            "transaction": t.string().optional(),
            "writes": t.array(t.proxy(renames["WriteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitRequestOut"])
    types["DocumentTransformIn"] = t.struct(
        {
            "document": t.string().optional(),
            "fieldTransforms": t.array(t.proxy(renames["FieldTransformIn"])).optional(),
        }
    ).named(renames["DocumentTransformIn"])
    types["DocumentTransformOut"] = t.struct(
        {
            "document": t.string().optional(),
            "fieldTransforms": t.array(
                t.proxy(renames["FieldTransformOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentTransformOut"])
    types["GoogleFirestoreAdminV1FieldOperationMetadataIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "state": t.string().optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
            "field": t.string().optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
            "endTime": t.string().optional(),
            "ttlConfigDelta": t.proxy(
                renames["GoogleFirestoreAdminV1TtlConfigDeltaIn"]
            ).optional(),
            "indexConfigDeltas": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexConfigDeltaIn"])
            ).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1FieldOperationMetadataIn"])
    types["GoogleFirestoreAdminV1FieldOperationMetadataOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "state": t.string().optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "field": t.string().optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "endTime": t.string().optional(),
            "ttlConfigDelta": t.proxy(
                renames["GoogleFirestoreAdminV1TtlConfigDeltaOut"]
            ).optional(),
            "indexConfigDeltas": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexConfigDeltaOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1FieldOperationMetadataOut"])
    types["GoogleFirestoreAdminV1FieldIn"] = t.struct(
        {
            "indexConfig": t.proxy(
                renames["GoogleFirestoreAdminV1IndexConfigIn"]
            ).optional(),
            "ttlConfig": t.proxy(
                renames["GoogleFirestoreAdminV1TtlConfigIn"]
            ).optional(),
            "name": t.string(),
        }
    ).named(renames["GoogleFirestoreAdminV1FieldIn"])
    types["GoogleFirestoreAdminV1FieldOut"] = t.struct(
        {
            "indexConfig": t.proxy(
                renames["GoogleFirestoreAdminV1IndexConfigOut"]
            ).optional(),
            "ttlConfig": t.proxy(
                renames["GoogleFirestoreAdminV1TtlConfigOut"]
            ).optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1FieldOut"])
    types["GoogleFirestoreAdminV1ExportDocumentsMetadataIn"] = t.struct(
        {
            "operationState": t.string().optional(),
            "outputUriPrefix": t.string().optional(),
            "collectionIds": t.array(t.string()).optional(),
            "namespaceIds": t.array(t.string()).optional(),
            "startTime": t.string().optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
            "endTime": t.string().optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ExportDocumentsMetadataIn"])
    types["GoogleFirestoreAdminV1ExportDocumentsMetadataOut"] = t.struct(
        {
            "operationState": t.string().optional(),
            "outputUriPrefix": t.string().optional(),
            "collectionIds": t.array(t.string()).optional(),
            "namespaceIds": t.array(t.string()).optional(),
            "startTime": t.string().optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "endTime": t.string().optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ExportDocumentsMetadataOut"])
    types["TargetIn"] = t.struct(
        {
            "targetId": t.integer().optional(),
            "resumeToken": t.string().optional(),
            "query": t.proxy(renames["QueryTargetIn"]).optional(),
            "once": t.boolean().optional(),
            "readTime": t.string().optional(),
            "documents": t.proxy(renames["DocumentsTargetIn"]).optional(),
        }
    ).named(renames["TargetIn"])
    types["TargetOut"] = t.struct(
        {
            "targetId": t.integer().optional(),
            "resumeToken": t.string().optional(),
            "query": t.proxy(renames["QueryTargetOut"]).optional(),
            "once": t.boolean().optional(),
            "readTime": t.string().optional(),
            "documents": t.proxy(renames["DocumentsTargetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetOut"])
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
    types["GoogleFirestoreAdminV1ExportDocumentsRequestIn"] = t.struct(
        {
            "collectionIds": t.array(t.string()).optional(),
            "namespaceIds": t.array(t.string()).optional(),
            "outputUriPrefix": t.string().optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ExportDocumentsRequestIn"])
    types["GoogleFirestoreAdminV1ExportDocumentsRequestOut"] = t.struct(
        {
            "collectionIds": t.array(t.string()).optional(),
            "namespaceIds": t.array(t.string()).optional(),
            "outputUriPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ExportDocumentsRequestOut"])
    types["GoogleFirestoreAdminV1ExportDocumentsResponseIn"] = t.struct(
        {"outputUriPrefix": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1ExportDocumentsResponseIn"])
    types["GoogleFirestoreAdminV1ExportDocumentsResponseOut"] = t.struct(
        {
            "outputUriPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ExportDocumentsResponseOut"])
    types["GoogleFirestoreAdminV1IndexFieldIn"] = t.struct(
        {
            "arrayConfig": t.string().optional(),
            "order": t.string().optional(),
            "fieldPath": t.string().optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexFieldIn"])
    types["GoogleFirestoreAdminV1IndexFieldOut"] = t.struct(
        {
            "arrayConfig": t.string().optional(),
            "order": t.string().optional(),
            "fieldPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexFieldOut"])
    types["BatchWriteResponseIn"] = t.struct(
        {
            "writeResults": t.array(t.proxy(renames["WriteResultIn"])).optional(),
            "status": t.array(t.proxy(renames["StatusIn"])).optional(),
        }
    ).named(renames["BatchWriteResponseIn"])
    types["BatchWriteResponseOut"] = t.struct(
        {
            "writeResults": t.array(t.proxy(renames["WriteResultOut"])).optional(),
            "status": t.array(t.proxy(renames["StatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchWriteResponseOut"])
    types["LocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["PartitionQueryResponseIn"] = t.struct(
        {
            "partitions": t.array(t.proxy(renames["CursorIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["PartitionQueryResponseIn"])
    types["PartitionQueryResponseOut"] = t.struct(
        {
            "partitions": t.array(t.proxy(renames["CursorOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionQueryResponseOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleFirestoreAdminV1DatabaseIn"] = t.struct(
        {
            "concurrencyMode": t.string().optional(),
            "etag": t.string().optional(),
            "locationId": t.string().optional(),
            "appEngineIntegrationMode": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "deleteProtectionState": t.string().optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1DatabaseIn"])
    types["GoogleFirestoreAdminV1DatabaseOut"] = t.struct(
        {
            "concurrencyMode": t.string().optional(),
            "etag": t.string().optional(),
            "keyPrefix": t.string().optional(),
            "createTime": t.string().optional(),
            "locationId": t.string().optional(),
            "appEngineIntegrationMode": t.string().optional(),
            "uid": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "deleteProtectionState": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1DatabaseOut"])
    types["CommitResponseIn"] = t.struct(
        {
            "writeResults": t.array(t.proxy(renames["WriteResultIn"])).optional(),
            "commitTime": t.string().optional(),
        }
    ).named(renames["CommitResponseIn"])
    types["CommitResponseOut"] = t.struct(
        {
            "writeResults": t.array(t.proxy(renames["WriteResultOut"])).optional(),
            "commitTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitResponseOut"])
    types["CollectionSelectorIn"] = t.struct(
        {
            "allDescendants": t.boolean().optional(),
            "collectionId": t.string().optional(),
        }
    ).named(renames["CollectionSelectorIn"])
    types["CollectionSelectorOut"] = t.struct(
        {
            "allDescendants": t.boolean().optional(),
            "collectionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CollectionSelectorOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["StructuredAggregationQueryIn"] = t.struct(
        {
            "structuredQuery": t.proxy(renames["StructuredQueryIn"]).optional(),
            "aggregations": t.array(t.proxy(renames["AggregationIn"])).optional(),
        }
    ).named(renames["StructuredAggregationQueryIn"])
    types["StructuredAggregationQueryOut"] = t.struct(
        {
            "structuredQuery": t.proxy(renames["StructuredQueryOut"]).optional(),
            "aggregations": t.array(t.proxy(renames["AggregationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructuredAggregationQueryOut"])
    types["ReadWriteIn"] = t.struct({"retryTransaction": t.string().optional()}).named(
        renames["ReadWriteIn"]
    )
    types["ReadWriteOut"] = t.struct(
        {
            "retryTransaction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadWriteOut"])
    types["StructuredQueryIn"] = t.struct(
        {
            "endAt": t.proxy(renames["CursorIn"]).optional(),
            "offset": t.integer().optional(),
            "limit": t.integer().optional(),
            "startAt": t.proxy(renames["CursorIn"]).optional(),
            "orderBy": t.array(t.proxy(renames["OrderIn"])).optional(),
            "select": t.proxy(renames["ProjectionIn"]).optional(),
            "where": t.proxy(renames["FilterIn"]).optional(),
            "from": t.array(t.proxy(renames["CollectionSelectorIn"])).optional(),
        }
    ).named(renames["StructuredQueryIn"])
    types["StructuredQueryOut"] = t.struct(
        {
            "endAt": t.proxy(renames["CursorOut"]).optional(),
            "offset": t.integer().optional(),
            "limit": t.integer().optional(),
            "startAt": t.proxy(renames["CursorOut"]).optional(),
            "orderBy": t.array(t.proxy(renames["OrderOut"])).optional(),
            "select": t.proxy(renames["ProjectionOut"]).optional(),
            "where": t.proxy(renames["FilterOut"]).optional(),
            "from": t.array(t.proxy(renames["CollectionSelectorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructuredQueryOut"])
    types["RunAggregationQueryRequestIn"] = t.struct(
        {
            "transaction": t.string().optional(),
            "newTransaction": t.proxy(renames["TransactionOptionsIn"]).optional(),
            "readTime": t.string().optional(),
            "structuredAggregationQuery": t.proxy(
                renames["StructuredAggregationQueryIn"]
            ).optional(),
        }
    ).named(renames["RunAggregationQueryRequestIn"])
    types["RunAggregationQueryRequestOut"] = t.struct(
        {
            "transaction": t.string().optional(),
            "newTransaction": t.proxy(renames["TransactionOptionsOut"]).optional(),
            "readTime": t.string().optional(),
            "structuredAggregationQuery": t.proxy(
                renames["StructuredAggregationQueryOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunAggregationQueryRequestOut"])
    types["PreconditionIn"] = t.struct(
        {"updateTime": t.string().optional(), "exists": t.boolean().optional()}
    ).named(renames["PreconditionIn"])
    types["PreconditionOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "exists": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PreconditionOut"])
    types["DocumentDeleteIn"] = t.struct(
        {
            "removedTargetIds": t.array(t.integer()).optional(),
            "document": t.string().optional(),
            "readTime": t.string().optional(),
        }
    ).named(renames["DocumentDeleteIn"])
    types["DocumentDeleteOut"] = t.struct(
        {
            "removedTargetIds": t.array(t.integer()).optional(),
            "document": t.string().optional(),
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentDeleteOut"])
    types["MapValueIn"] = t.struct(
        {"fields": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["MapValueIn"])
    types["MapValueOut"] = t.struct(
        {
            "fields": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MapValueOut"])
    types["GoogleFirestoreAdminV1ListIndexesResponseIn"] = t.struct(
        {
            "indexes": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ListIndexesResponseIn"])
    types["GoogleFirestoreAdminV1ListIndexesResponseOut"] = t.struct(
        {
            "indexes": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ListIndexesResponseOut"])
    types["GoogleFirestoreAdminV1LocationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1LocationMetadataIn"])
    types["GoogleFirestoreAdminV1LocationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleFirestoreAdminV1LocationMetadataOut"])
    types["UnaryFilterIn"] = t.struct(
        {
            "op": t.string().optional(),
            "field": t.proxy(renames["FieldReferenceIn"]).optional(),
        }
    ).named(renames["UnaryFilterIn"])
    types["UnaryFilterOut"] = t.struct(
        {
            "op": t.string().optional(),
            "field": t.proxy(renames["FieldReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnaryFilterOut"])
    types["DocumentMaskIn"] = t.struct(
        {"fieldPaths": t.array(t.string()).optional()}
    ).named(renames["DocumentMaskIn"])
    types["DocumentMaskOut"] = t.struct(
        {
            "fieldPaths": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentMaskOut"])
    types["ListCollectionIdsResponseIn"] = t.struct(
        {
            "collectionIds": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCollectionIdsResponseIn"])
    types["ListCollectionIdsResponseOut"] = t.struct(
        {
            "collectionIds": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCollectionIdsResponseOut"])
    types["GoogleFirestoreAdminV1IndexIn"] = t.struct(
        {
            "name": t.string().optional(),
            "state": t.string().optional(),
            "apiScope": t.string().optional(),
            "queryScope": t.string().optional(),
            "fields": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexFieldIn"])
            ).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexIn"])
    types["GoogleFirestoreAdminV1IndexOut"] = t.struct(
        {
            "name": t.string().optional(),
            "state": t.string().optional(),
            "apiScope": t.string().optional(),
            "queryScope": t.string().optional(),
            "fields": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexFieldOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexOut"])
    types["DocumentsTargetIn"] = t.struct(
        {"documents": t.array(t.string()).optional()}
    ).named(renames["DocumentsTargetIn"])
    types["DocumentsTargetOut"] = t.struct(
        {
            "documents": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentsTargetOut"])
    types["GoogleFirestoreAdminV1IndexConfigIn"] = t.struct(
        {
            "usesAncestorConfig": t.boolean().optional(),
            "ancestorField": t.string().optional(),
            "reverting": t.boolean().optional(),
            "indexes": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexIn"])
            ).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexConfigIn"])
    types["GoogleFirestoreAdminV1IndexConfigOut"] = t.struct(
        {
            "usesAncestorConfig": t.boolean().optional(),
            "ancestorField": t.string().optional(),
            "reverting": t.boolean().optional(),
            "indexes": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexConfigOut"])
    types["ListCollectionIdsRequestIn"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "readTime": t.string().optional(),
        }
    ).named(renames["ListCollectionIdsRequestIn"])
    types["ListCollectionIdsRequestOut"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCollectionIdsRequestOut"])
    types["QueryTargetIn"] = t.struct(
        {
            "structuredQuery": t.proxy(renames["StructuredQueryIn"]).optional(),
            "parent": t.string().optional(),
        }
    ).named(renames["QueryTargetIn"])
    types["QueryTargetOut"] = t.struct(
        {
            "structuredQuery": t.proxy(renames["StructuredQueryOut"]).optional(),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryTargetOut"])
    types["GoogleFirestoreAdminV1ImportDocumentsMetadataIn"] = t.struct(
        {
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
            "startTime": t.string().optional(),
            "collectionIds": t.array(t.string()).optional(),
            "inputUriPrefix": t.string().optional(),
            "namespaceIds": t.array(t.string()).optional(),
            "operationState": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ImportDocumentsMetadataIn"])
    types["GoogleFirestoreAdminV1ImportDocumentsMetadataOut"] = t.struct(
        {
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "collectionIds": t.array(t.string()).optional(),
            "inputUriPrefix": t.string().optional(),
            "namespaceIds": t.array(t.string()).optional(),
            "operationState": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ImportDocumentsMetadataOut"])
    types["AggregationResultIn"] = t.struct(
        {"aggregateFields": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["AggregationResultIn"])
    types["AggregationResultOut"] = t.struct(
        {
            "aggregateFields": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationResultOut"])
    types["RunQueryResponseIn"] = t.struct(
        {
            "readTime": t.string().optional(),
            "transaction": t.string().optional(),
            "done": t.boolean().optional(),
            "skippedResults": t.integer().optional(),
            "document": t.proxy(renames["DocumentIn"]).optional(),
        }
    ).named(renames["RunQueryResponseIn"])
    types["RunQueryResponseOut"] = t.struct(
        {
            "readTime": t.string().optional(),
            "transaction": t.string().optional(),
            "done": t.boolean().optional(),
            "skippedResults": t.integer().optional(),
            "document": t.proxy(renames["DocumentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunQueryResponseOut"])
    types["ExistenceFilterIn"] = t.struct(
        {"count": t.integer().optional(), "targetId": t.integer().optional()}
    ).named(renames["ExistenceFilterIn"])
    types["ExistenceFilterOut"] = t.struct(
        {
            "count": t.integer().optional(),
            "targetId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExistenceFilterOut"])
    types["DocumentIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "fields": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DocumentIn"])
    types["DocumentOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "fields": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentOut"])
    types["RunAggregationQueryResponseIn"] = t.struct(
        {
            "result": t.proxy(renames["AggregationResultIn"]).optional(),
            "readTime": t.string().optional(),
            "transaction": t.string().optional(),
        }
    ).named(renames["RunAggregationQueryResponseIn"])
    types["RunAggregationQueryResponseOut"] = t.struct(
        {
            "result": t.proxy(renames["AggregationResultOut"]).optional(),
            "readTime": t.string().optional(),
            "transaction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunAggregationQueryResponseOut"])
    types["FilterIn"] = t.struct(
        {
            "unaryFilter": t.proxy(renames["UnaryFilterIn"]).optional(),
            "fieldFilter": t.proxy(renames["FieldFilterIn"]).optional(),
            "compositeFilter": t.proxy(renames["CompositeFilterIn"]).optional(),
        }
    ).named(renames["FilterIn"])
    types["FilterOut"] = t.struct(
        {
            "unaryFilter": t.proxy(renames["UnaryFilterOut"]).optional(),
            "fieldFilter": t.proxy(renames["FieldFilterOut"]).optional(),
            "compositeFilter": t.proxy(renames["CompositeFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterOut"])
    types["DocumentRemoveIn"] = t.struct(
        {
            "document": t.string().optional(),
            "removedTargetIds": t.array(t.integer()).optional(),
            "readTime": t.string().optional(),
        }
    ).named(renames["DocumentRemoveIn"])
    types["DocumentRemoveOut"] = t.struct(
        {
            "document": t.string().optional(),
            "removedTargetIds": t.array(t.integer()).optional(),
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentRemoveOut"])
    types["WriteRequestIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "writes": t.array(t.proxy(renames["WriteIn"])).optional(),
            "streamToken": t.string().optional(),
            "streamId": t.string().optional(),
        }
    ).named(renames["WriteRequestIn"])
    types["WriteRequestOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "writes": t.array(t.proxy(renames["WriteOut"])).optional(),
            "streamToken": t.string().optional(),
            "streamId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteRequestOut"])
    types["GoogleFirestoreAdminV1ListDatabasesResponseIn"] = t.struct(
        {
            "databases": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1DatabaseIn"])
            ).optional()
        }
    ).named(renames["GoogleFirestoreAdminV1ListDatabasesResponseIn"])
    types["GoogleFirestoreAdminV1ListDatabasesResponseOut"] = t.struct(
        {
            "databases": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1DatabaseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ListDatabasesResponseOut"])
    types["BeginTransactionRequestIn"] = t.struct(
        {"options": t.proxy(renames["TransactionOptionsIn"]).optional()}
    ).named(renames["BeginTransactionRequestIn"])
    types["BeginTransactionRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["TransactionOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BeginTransactionRequestOut"])
    types["TargetChangeIn"] = t.struct(
        {
            "resumeToken": t.string().optional(),
            "cause": t.proxy(renames["StatusIn"]).optional(),
            "readTime": t.string().optional(),
            "targetIds": t.array(t.integer()).optional(),
            "targetChangeType": t.string().optional(),
        }
    ).named(renames["TargetChangeIn"])
    types["TargetChangeOut"] = t.struct(
        {
            "resumeToken": t.string().optional(),
            "cause": t.proxy(renames["StatusOut"]).optional(),
            "readTime": t.string().optional(),
            "targetIds": t.array(t.integer()).optional(),
            "targetChangeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetChangeOut"])
    types["ReadOnlyIn"] = t.struct({"readTime": t.string().optional()}).named(
        renames["ReadOnlyIn"]
    )
    types["ReadOnlyOut"] = t.struct(
        {
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadOnlyOut"])
    types["ArrayValueIn"] = t.struct(
        {"values": t.array(t.proxy(renames["ValueIn"])).optional()}
    ).named(renames["ArrayValueIn"])
    types["ArrayValueOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["ValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArrayValueOut"])
    types["ListDocumentsResponseIn"] = t.struct(
        {
            "documents": t.array(t.proxy(renames["DocumentIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListDocumentsResponseIn"])
    types["ListDocumentsResponseOut"] = t.struct(
        {
            "documents": t.array(t.proxy(renames["DocumentOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDocumentsResponseOut"])
    types["ValueIn"] = t.struct(
        {
            "referenceValue": t.string().optional(),
            "doubleValue": t.number().optional(),
            "stringValue": t.string().optional(),
            "arrayValue": t.proxy(renames["ArrayValueIn"]).optional(),
            "timestampValue": t.string().optional(),
            "booleanValue": t.boolean().optional(),
            "integerValue": t.string().optional(),
            "mapValue": t.proxy(renames["MapValueIn"]).optional(),
            "bytesValue": t.string().optional(),
            "nullValue": t.string().optional(),
            "geoPointValue": t.proxy(renames["LatLngIn"]).optional(),
        }
    ).named(renames["ValueIn"])
    types["ValueOut"] = t.struct(
        {
            "referenceValue": t.string().optional(),
            "doubleValue": t.number().optional(),
            "stringValue": t.string().optional(),
            "arrayValue": t.proxy(renames["ArrayValueOut"]).optional(),
            "timestampValue": t.string().optional(),
            "booleanValue": t.boolean().optional(),
            "integerValue": t.string().optional(),
            "mapValue": t.proxy(renames["MapValueOut"]).optional(),
            "bytesValue": t.string().optional(),
            "nullValue": t.string().optional(),
            "geoPointValue": t.proxy(renames["LatLngOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueOut"])
    types["WriteIn"] = t.struct(
        {
            "delete": t.string().optional(),
            "transform": t.proxy(renames["DocumentTransformIn"]).optional(),
            "updateTransforms": t.array(
                t.proxy(renames["FieldTransformIn"])
            ).optional(),
            "update": t.proxy(renames["DocumentIn"]).optional(),
            "updateMask": t.proxy(renames["DocumentMaskIn"]).optional(),
            "currentDocument": t.proxy(renames["PreconditionIn"]).optional(),
        }
    ).named(renames["WriteIn"])
    types["WriteOut"] = t.struct(
        {
            "delete": t.string().optional(),
            "transform": t.proxy(renames["DocumentTransformOut"]).optional(),
            "updateTransforms": t.array(
                t.proxy(renames["FieldTransformOut"])
            ).optional(),
            "update": t.proxy(renames["DocumentOut"]).optional(),
            "updateMask": t.proxy(renames["DocumentMaskOut"]).optional(),
            "currentDocument": t.proxy(renames["PreconditionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteOut"])
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
    types["CountIn"] = t.struct({"upTo": t.string().optional()}).named(
        renames["CountIn"]
    )
    types["CountOut"] = t.struct(
        {
            "upTo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CountOut"])
    types["RollbackRequestIn"] = t.struct({"transaction": t.string()}).named(
        renames["RollbackRequestIn"]
    )
    types["RollbackRequestOut"] = t.struct(
        {
            "transaction": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RollbackRequestOut"])
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
    types["OrderIn"] = t.struct(
        {
            "field": t.proxy(renames["FieldReferenceIn"]).optional(),
            "direction": t.string().optional(),
        }
    ).named(renames["OrderIn"])
    types["OrderOut"] = t.struct(
        {
            "field": t.proxy(renames["FieldReferenceOut"]).optional(),
            "direction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderOut"])
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
    types["BatchGetDocumentsResponseIn"] = t.struct(
        {
            "missing": t.string().optional(),
            "transaction": t.string().optional(),
            "readTime": t.string().optional(),
            "found": t.proxy(renames["DocumentIn"]).optional(),
        }
    ).named(renames["BatchGetDocumentsResponseIn"])
    types["BatchGetDocumentsResponseOut"] = t.struct(
        {
            "missing": t.string().optional(),
            "transaction": t.string().optional(),
            "readTime": t.string().optional(),
            "found": t.proxy(renames["DocumentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetDocumentsResponseOut"])
    types["BatchGetDocumentsRequestIn"] = t.struct(
        {
            "readTime": t.string().optional(),
            "mask": t.proxy(renames["DocumentMaskIn"]).optional(),
            "newTransaction": t.proxy(renames["TransactionOptionsIn"]).optional(),
            "documents": t.array(t.string()).optional(),
            "transaction": t.string().optional(),
        }
    ).named(renames["BatchGetDocumentsRequestIn"])
    types["BatchGetDocumentsRequestOut"] = t.struct(
        {
            "readTime": t.string().optional(),
            "mask": t.proxy(renames["DocumentMaskOut"]).optional(),
            "newTransaction": t.proxy(renames["TransactionOptionsOut"]).optional(),
            "documents": t.array(t.string()).optional(),
            "transaction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetDocumentsRequestOut"])

    functions = {}
    functions["projectsLocationsList"] = firestore.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = firestore.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesExportDocuments"] = firestore.post(
        "v1/{name}:importDocuments",
        t.struct(
            {
                "name": t.string(),
                "collectionIds": t.array(t.string()).optional(),
                "inputUriPrefix": t.string().optional(),
                "namespaceIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesGet"] = firestore.post(
        "v1/{name}:importDocuments",
        t.struct(
            {
                "name": t.string(),
                "collectionIds": t.array(t.string()).optional(),
                "inputUriPrefix": t.string().optional(),
                "namespaceIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDelete"] = firestore.post(
        "v1/{name}:importDocuments",
        t.struct(
            {
                "name": t.string(),
                "collectionIds": t.array(t.string()).optional(),
                "inputUriPrefix": t.string().optional(),
                "namespaceIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesList"] = firestore.post(
        "v1/{name}:importDocuments",
        t.struct(
            {
                "name": t.string(),
                "collectionIds": t.array(t.string()).optional(),
                "inputUriPrefix": t.string().optional(),
                "namespaceIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesPatch"] = firestore.post(
        "v1/{name}:importDocuments",
        t.struct(
            {
                "name": t.string(),
                "collectionIds": t.array(t.string()).optional(),
                "inputUriPrefix": t.string().optional(),
                "namespaceIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesCreate"] = firestore.post(
        "v1/{name}:importDocuments",
        t.struct(
            {
                "name": t.string(),
                "collectionIds": t.array(t.string()).optional(),
                "inputUriPrefix": t.string().optional(),
                "namespaceIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesImportDocuments"] = firestore.post(
        "v1/{name}:importDocuments",
        t.struct(
            {
                "name": t.string(),
                "collectionIds": t.array(t.string()).optional(),
                "inputUriPrefix": t.string().optional(),
                "namespaceIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsBatchGet"] = firestore.post(
        "v1/{parent}/{collectionId}",
        t.struct(
            {
                "collectionId": t.string(),
                "parent": t.string(),
                "documentId": t.string().optional(),
                "mask.fieldPaths": t.string().optional(),
                "createTime": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}).optional(),
                "updateTime": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsPatch"] = firestore.post(
        "v1/{parent}/{collectionId}",
        t.struct(
            {
                "collectionId": t.string(),
                "parent": t.string(),
                "documentId": t.string().optional(),
                "mask.fieldPaths": t.string().optional(),
                "createTime": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}).optional(),
                "updateTime": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsBatchWrite"] = firestore.post(
        "v1/{parent}/{collectionId}",
        t.struct(
            {
                "collectionId": t.string(),
                "parent": t.string(),
                "documentId": t.string().optional(),
                "mask.fieldPaths": t.string().optional(),
                "createTime": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}).optional(),
                "updateTime": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsListDocuments"] = firestore.post(
        "v1/{parent}/{collectionId}",
        t.struct(
            {
                "collectionId": t.string(),
                "parent": t.string(),
                "documentId": t.string().optional(),
                "mask.fieldPaths": t.string().optional(),
                "createTime": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}).optional(),
                "updateTime": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsGet"] = firestore.post(
        "v1/{parent}/{collectionId}",
        t.struct(
            {
                "collectionId": t.string(),
                "parent": t.string(),
                "documentId": t.string().optional(),
                "mask.fieldPaths": t.string().optional(),
                "createTime": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}).optional(),
                "updateTime": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsListen"] = firestore.post(
        "v1/{parent}/{collectionId}",
        t.struct(
            {
                "collectionId": t.string(),
                "parent": t.string(),
                "documentId": t.string().optional(),
                "mask.fieldPaths": t.string().optional(),
                "createTime": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}).optional(),
                "updateTime": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsRunQuery"] = firestore.post(
        "v1/{parent}/{collectionId}",
        t.struct(
            {
                "collectionId": t.string(),
                "parent": t.string(),
                "documentId": t.string().optional(),
                "mask.fieldPaths": t.string().optional(),
                "createTime": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}).optional(),
                "updateTime": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsList"] = firestore.post(
        "v1/{parent}/{collectionId}",
        t.struct(
            {
                "collectionId": t.string(),
                "parent": t.string(),
                "documentId": t.string().optional(),
                "mask.fieldPaths": t.string().optional(),
                "createTime": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}).optional(),
                "updateTime": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsCommit"] = firestore.post(
        "v1/{parent}/{collectionId}",
        t.struct(
            {
                "collectionId": t.string(),
                "parent": t.string(),
                "documentId": t.string().optional(),
                "mask.fieldPaths": t.string().optional(),
                "createTime": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}).optional(),
                "updateTime": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsRollback"] = firestore.post(
        "v1/{parent}/{collectionId}",
        t.struct(
            {
                "collectionId": t.string(),
                "parent": t.string(),
                "documentId": t.string().optional(),
                "mask.fieldPaths": t.string().optional(),
                "createTime": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}).optional(),
                "updateTime": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsWrite"] = firestore.post(
        "v1/{parent}/{collectionId}",
        t.struct(
            {
                "collectionId": t.string(),
                "parent": t.string(),
                "documentId": t.string().optional(),
                "mask.fieldPaths": t.string().optional(),
                "createTime": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}).optional(),
                "updateTime": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsListCollectionIds"] = firestore.post(
        "v1/{parent}/{collectionId}",
        t.struct(
            {
                "collectionId": t.string(),
                "parent": t.string(),
                "documentId": t.string().optional(),
                "mask.fieldPaths": t.string().optional(),
                "createTime": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}).optional(),
                "updateTime": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsDelete"] = firestore.post(
        "v1/{parent}/{collectionId}",
        t.struct(
            {
                "collectionId": t.string(),
                "parent": t.string(),
                "documentId": t.string().optional(),
                "mask.fieldPaths": t.string().optional(),
                "createTime": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}).optional(),
                "updateTime": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsBeginTransaction"] = firestore.post(
        "v1/{parent}/{collectionId}",
        t.struct(
            {
                "collectionId": t.string(),
                "parent": t.string(),
                "documentId": t.string().optional(),
                "mask.fieldPaths": t.string().optional(),
                "createTime": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}).optional(),
                "updateTime": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsPartitionQuery"] = firestore.post(
        "v1/{parent}/{collectionId}",
        t.struct(
            {
                "collectionId": t.string(),
                "parent": t.string(),
                "documentId": t.string().optional(),
                "mask.fieldPaths": t.string().optional(),
                "createTime": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}).optional(),
                "updateTime": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsRunAggregationQuery"] = firestore.post(
        "v1/{parent}/{collectionId}",
        t.struct(
            {
                "collectionId": t.string(),
                "parent": t.string(),
                "documentId": t.string().optional(),
                "mask.fieldPaths": t.string().optional(),
                "createTime": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}).optional(),
                "updateTime": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsCreateDocument"] = firestore.post(
        "v1/{parent}/{collectionId}",
        t.struct(
            {
                "collectionId": t.string(),
                "parent": t.string(),
                "documentId": t.string().optional(),
                "mask.fieldPaths": t.string().optional(),
                "createTime": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}).optional(),
                "updateTime": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DocumentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesCollectionGroupsFieldsPatch"] = firestore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirestoreAdminV1FieldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesCollectionGroupsFieldsList"] = firestore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirestoreAdminV1FieldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesCollectionGroupsFieldsGet"] = firestore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirestoreAdminV1FieldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesCollectionGroupsIndexesGet"] = firestore.get(
        "v1/{parent}/indexes",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirestoreAdminV1ListIndexesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesCollectionGroupsIndexesDelete"] = firestore.get(
        "v1/{parent}/indexes",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirestoreAdminV1ListIndexesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesCollectionGroupsIndexesCreate"] = firestore.get(
        "v1/{parent}/indexes",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirestoreAdminV1ListIndexesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesCollectionGroupsIndexesList"] = firestore.get(
        "v1/{parent}/indexes",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirestoreAdminV1ListIndexesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesOperationsDelete"] = firestore.post(
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
    functions["projectsDatabasesOperationsGet"] = firestore.post(
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
    functions["projectsDatabasesOperationsList"] = firestore.post(
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
    functions["projectsDatabasesOperationsCancel"] = firestore.post(
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

    return Import(
        importer="firestore", renames=renames, types=types, functions=functions
    )
