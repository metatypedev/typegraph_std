from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_firestore() -> Import:
    firestore = HTTPRuntime("https://firestore.googleapis.com/")

    renames = {
        "ErrorResponse": "_firestore_1_ErrorResponse",
        "ListenRequestIn": "_firestore_2_ListenRequestIn",
        "ListenRequestOut": "_firestore_3_ListenRequestOut",
        "DocumentChangeIn": "_firestore_4_DocumentChangeIn",
        "DocumentChangeOut": "_firestore_5_DocumentChangeOut",
        "BeginTransactionRequestIn": "_firestore_6_BeginTransactionRequestIn",
        "BeginTransactionRequestOut": "_firestore_7_BeginTransactionRequestOut",
        "GoogleFirestoreAdminV1StatsIn": "_firestore_8_GoogleFirestoreAdminV1StatsIn",
        "GoogleFirestoreAdminV1StatsOut": "_firestore_9_GoogleFirestoreAdminV1StatsOut",
        "StatusIn": "_firestore_10_StatusIn",
        "StatusOut": "_firestore_11_StatusOut",
        "GoogleFirestoreAdminV1BackupIn": "_firestore_12_GoogleFirestoreAdminV1BackupIn",
        "GoogleFirestoreAdminV1BackupOut": "_firestore_13_GoogleFirestoreAdminV1BackupOut",
        "GoogleLongrunningListOperationsResponseIn": "_firestore_14_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_firestore_15_GoogleLongrunningListOperationsResponseOut",
        "TransactionOptionsIn": "_firestore_16_TransactionOptionsIn",
        "TransactionOptionsOut": "_firestore_17_TransactionOptionsOut",
        "LatLngIn": "_firestore_18_LatLngIn",
        "LatLngOut": "_firestore_19_LatLngOut",
        "ValueIn": "_firestore_20_ValueIn",
        "ValueOut": "_firestore_21_ValueOut",
        "ListCollectionIdsRequestIn": "_firestore_22_ListCollectionIdsRequestIn",
        "ListCollectionIdsRequestOut": "_firestore_23_ListCollectionIdsRequestOut",
        "GoogleFirestoreAdminV1ExportDocumentsMetadataIn": "_firestore_24_GoogleFirestoreAdminV1ExportDocumentsMetadataIn",
        "GoogleFirestoreAdminV1ExportDocumentsMetadataOut": "_firestore_25_GoogleFirestoreAdminV1ExportDocumentsMetadataOut",
        "GoogleFirestoreAdminV1IndexConfigDeltaIn": "_firestore_26_GoogleFirestoreAdminV1IndexConfigDeltaIn",
        "GoogleFirestoreAdminV1IndexConfigDeltaOut": "_firestore_27_GoogleFirestoreAdminV1IndexConfigDeltaOut",
        "GoogleFirestoreAdminV1WeeklyRecurrenceIn": "_firestore_28_GoogleFirestoreAdminV1WeeklyRecurrenceIn",
        "GoogleFirestoreAdminV1WeeklyRecurrenceOut": "_firestore_29_GoogleFirestoreAdminV1WeeklyRecurrenceOut",
        "PartitionQueryRequestIn": "_firestore_30_PartitionQueryRequestIn",
        "PartitionQueryRequestOut": "_firestore_31_PartitionQueryRequestOut",
        "StructuredAggregationQueryIn": "_firestore_32_StructuredAggregationQueryIn",
        "StructuredAggregationQueryOut": "_firestore_33_StructuredAggregationQueryOut",
        "GoogleLongrunningCancelOperationRequestIn": "_firestore_34_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_firestore_35_GoogleLongrunningCancelOperationRequestOut",
        "EmptyIn": "_firestore_36_EmptyIn",
        "EmptyOut": "_firestore_37_EmptyOut",
        "BloomFilterIn": "_firestore_38_BloomFilterIn",
        "BloomFilterOut": "_firestore_39_BloomFilterOut",
        "GoogleFirestoreAdminV1IndexIn": "_firestore_40_GoogleFirestoreAdminV1IndexIn",
        "GoogleFirestoreAdminV1IndexOut": "_firestore_41_GoogleFirestoreAdminV1IndexOut",
        "GoogleFirestoreAdminV1ImportDocumentsMetadataIn": "_firestore_42_GoogleFirestoreAdminV1ImportDocumentsMetadataIn",
        "GoogleFirestoreAdminV1ImportDocumentsMetadataOut": "_firestore_43_GoogleFirestoreAdminV1ImportDocumentsMetadataOut",
        "GoogleFirestoreAdminV1ExportDocumentsResponseIn": "_firestore_44_GoogleFirestoreAdminV1ExportDocumentsResponseIn",
        "GoogleFirestoreAdminV1ExportDocumentsResponseOut": "_firestore_45_GoogleFirestoreAdminV1ExportDocumentsResponseOut",
        "ProjectionIn": "_firestore_46_ProjectionIn",
        "ProjectionOut": "_firestore_47_ProjectionOut",
        "FieldTransformIn": "_firestore_48_FieldTransformIn",
        "FieldTransformOut": "_firestore_49_FieldTransformOut",
        "CollectionSelectorIn": "_firestore_50_CollectionSelectorIn",
        "CollectionSelectorOut": "_firestore_51_CollectionSelectorOut",
        "BatchWriteRequestIn": "_firestore_52_BatchWriteRequestIn",
        "BatchWriteRequestOut": "_firestore_53_BatchWriteRequestOut",
        "GoogleFirestoreAdminV1LocationMetadataIn": "_firestore_54_GoogleFirestoreAdminV1LocationMetadataIn",
        "GoogleFirestoreAdminV1LocationMetadataOut": "_firestore_55_GoogleFirestoreAdminV1LocationMetadataOut",
        "GoogleFirestoreAdminV1TtlConfigDeltaIn": "_firestore_56_GoogleFirestoreAdminV1TtlConfigDeltaIn",
        "GoogleFirestoreAdminV1TtlConfigDeltaOut": "_firestore_57_GoogleFirestoreAdminV1TtlConfigDeltaOut",
        "DocumentMaskIn": "_firestore_58_DocumentMaskIn",
        "DocumentMaskOut": "_firestore_59_DocumentMaskOut",
        "FilterIn": "_firestore_60_FilterIn",
        "FilterOut": "_firestore_61_FilterOut",
        "StructuredQueryIn": "_firestore_62_StructuredQueryIn",
        "StructuredQueryOut": "_firestore_63_StructuredQueryOut",
        "RollbackRequestIn": "_firestore_64_RollbackRequestIn",
        "RollbackRequestOut": "_firestore_65_RollbackRequestOut",
        "GoogleFirestoreAdminV1UpdateDatabaseMetadataIn": "_firestore_66_GoogleFirestoreAdminV1UpdateDatabaseMetadataIn",
        "GoogleFirestoreAdminV1UpdateDatabaseMetadataOut": "_firestore_67_GoogleFirestoreAdminV1UpdateDatabaseMetadataOut",
        "BatchGetDocumentsResponseIn": "_firestore_68_BatchGetDocumentsResponseIn",
        "BatchGetDocumentsResponseOut": "_firestore_69_BatchGetDocumentsResponseOut",
        "OrderIn": "_firestore_70_OrderIn",
        "OrderOut": "_firestore_71_OrderOut",
        "ListCollectionIdsResponseIn": "_firestore_72_ListCollectionIdsResponseIn",
        "ListCollectionIdsResponseOut": "_firestore_73_ListCollectionIdsResponseOut",
        "WriteResponseIn": "_firestore_74_WriteResponseIn",
        "WriteResponseOut": "_firestore_75_WriteResponseOut",
        "GoogleFirestoreAdminV1IndexConfigIn": "_firestore_76_GoogleFirestoreAdminV1IndexConfigIn",
        "GoogleFirestoreAdminV1IndexConfigOut": "_firestore_77_GoogleFirestoreAdminV1IndexConfigOut",
        "GoogleFirestoreAdminV1FieldOperationMetadataIn": "_firestore_78_GoogleFirestoreAdminV1FieldOperationMetadataIn",
        "GoogleFirestoreAdminV1FieldOperationMetadataOut": "_firestore_79_GoogleFirestoreAdminV1FieldOperationMetadataOut",
        "ExistenceFilterIn": "_firestore_80_ExistenceFilterIn",
        "ExistenceFilterOut": "_firestore_81_ExistenceFilterOut",
        "GoogleFirestoreAdminV1BackupScheduleIn": "_firestore_82_GoogleFirestoreAdminV1BackupScheduleIn",
        "GoogleFirestoreAdminV1BackupScheduleOut": "_firestore_83_GoogleFirestoreAdminV1BackupScheduleOut",
        "WriteIn": "_firestore_84_WriteIn",
        "WriteOut": "_firestore_85_WriteOut",
        "BatchGetDocumentsRequestIn": "_firestore_86_BatchGetDocumentsRequestIn",
        "BatchGetDocumentsRequestOut": "_firestore_87_BatchGetDocumentsRequestOut",
        "WriteRequestIn": "_firestore_88_WriteRequestIn",
        "WriteRequestOut": "_firestore_89_WriteRequestOut",
        "CountIn": "_firestore_90_CountIn",
        "CountOut": "_firestore_91_CountOut",
        "LocationIn": "_firestore_92_LocationIn",
        "LocationOut": "_firestore_93_LocationOut",
        "BatchWriteResponseIn": "_firestore_94_BatchWriteResponseIn",
        "BatchWriteResponseOut": "_firestore_95_BatchWriteResponseOut",
        "TargetChangeIn": "_firestore_96_TargetChangeIn",
        "TargetChangeOut": "_firestore_97_TargetChangeOut",
        "ArrayValueIn": "_firestore_98_ArrayValueIn",
        "ArrayValueOut": "_firestore_99_ArrayValueOut",
        "GoogleFirestoreAdminV1ProgressIn": "_firestore_100_GoogleFirestoreAdminV1ProgressIn",
        "GoogleFirestoreAdminV1ProgressOut": "_firestore_101_GoogleFirestoreAdminV1ProgressOut",
        "FieldFilterIn": "_firestore_102_FieldFilterIn",
        "FieldFilterOut": "_firestore_103_FieldFilterOut",
        "GoogleFirestoreAdminV1ListIndexesResponseIn": "_firestore_104_GoogleFirestoreAdminV1ListIndexesResponseIn",
        "GoogleFirestoreAdminV1ListIndexesResponseOut": "_firestore_105_GoogleFirestoreAdminV1ListIndexesResponseOut",
        "DocumentRemoveIn": "_firestore_106_DocumentRemoveIn",
        "DocumentRemoveOut": "_firestore_107_DocumentRemoveOut",
        "GoogleFirestoreAdminV1ListBackupsResponseIn": "_firestore_108_GoogleFirestoreAdminV1ListBackupsResponseIn",
        "GoogleFirestoreAdminV1ListBackupsResponseOut": "_firestore_109_GoogleFirestoreAdminV1ListBackupsResponseOut",
        "GoogleFirestoreAdminV1RestoreDatabaseRequestIn": "_firestore_110_GoogleFirestoreAdminV1RestoreDatabaseRequestIn",
        "GoogleFirestoreAdminV1RestoreDatabaseRequestOut": "_firestore_111_GoogleFirestoreAdminV1RestoreDatabaseRequestOut",
        "BitSequenceIn": "_firestore_112_BitSequenceIn",
        "BitSequenceOut": "_firestore_113_BitSequenceOut",
        "PreconditionIn": "_firestore_114_PreconditionIn",
        "PreconditionOut": "_firestore_115_PreconditionOut",
        "ListenResponseIn": "_firestore_116_ListenResponseIn",
        "ListenResponseOut": "_firestore_117_ListenResponseOut",
        "GoogleFirestoreAdminV1FieldIn": "_firestore_118_GoogleFirestoreAdminV1FieldIn",
        "GoogleFirestoreAdminV1FieldOut": "_firestore_119_GoogleFirestoreAdminV1FieldOut",
        "GoogleFirestoreAdminV1TtlConfigIn": "_firestore_120_GoogleFirestoreAdminV1TtlConfigIn",
        "GoogleFirestoreAdminV1TtlConfigOut": "_firestore_121_GoogleFirestoreAdminV1TtlConfigOut",
        "PartitionQueryResponseIn": "_firestore_122_PartitionQueryResponseIn",
        "PartitionQueryResponseOut": "_firestore_123_PartitionQueryResponseOut",
        "DocumentsTargetIn": "_firestore_124_DocumentsTargetIn",
        "DocumentsTargetOut": "_firestore_125_DocumentsTargetOut",
        "RunQueryRequestIn": "_firestore_126_RunQueryRequestIn",
        "RunQueryRequestOut": "_firestore_127_RunQueryRequestOut",
        "GoogleFirestoreAdminV1ListDatabasesResponseIn": "_firestore_128_GoogleFirestoreAdminV1ListDatabasesResponseIn",
        "GoogleFirestoreAdminV1ListDatabasesResponseOut": "_firestore_129_GoogleFirestoreAdminV1ListDatabasesResponseOut",
        "ReadWriteIn": "_firestore_130_ReadWriteIn",
        "ReadWriteOut": "_firestore_131_ReadWriteOut",
        "UnaryFilterIn": "_firestore_132_UnaryFilterIn",
        "UnaryFilterOut": "_firestore_133_UnaryFilterOut",
        "QueryTargetIn": "_firestore_134_QueryTargetIn",
        "QueryTargetOut": "_firestore_135_QueryTargetOut",
        "RunAggregationQueryResponseIn": "_firestore_136_RunAggregationQueryResponseIn",
        "RunAggregationQueryResponseOut": "_firestore_137_RunAggregationQueryResponseOut",
        "RunAggregationQueryRequestIn": "_firestore_138_RunAggregationQueryRequestIn",
        "RunAggregationQueryRequestOut": "_firestore_139_RunAggregationQueryRequestOut",
        "GoogleFirestoreAdminV1ExportDocumentsRequestIn": "_firestore_140_GoogleFirestoreAdminV1ExportDocumentsRequestIn",
        "GoogleFirestoreAdminV1ExportDocumentsRequestOut": "_firestore_141_GoogleFirestoreAdminV1ExportDocumentsRequestOut",
        "GoogleFirestoreAdminV1ListFieldsResponseIn": "_firestore_142_GoogleFirestoreAdminV1ListFieldsResponseIn",
        "GoogleFirestoreAdminV1ListFieldsResponseOut": "_firestore_143_GoogleFirestoreAdminV1ListFieldsResponseOut",
        "GoogleFirestoreAdminV1ImportDocumentsRequestIn": "_firestore_144_GoogleFirestoreAdminV1ImportDocumentsRequestIn",
        "GoogleFirestoreAdminV1ImportDocumentsRequestOut": "_firestore_145_GoogleFirestoreAdminV1ImportDocumentsRequestOut",
        "GoogleFirestoreAdminV1DailyRecurrenceIn": "_firestore_146_GoogleFirestoreAdminV1DailyRecurrenceIn",
        "GoogleFirestoreAdminV1DailyRecurrenceOut": "_firestore_147_GoogleFirestoreAdminV1DailyRecurrenceOut",
        "ListLocationsResponseIn": "_firestore_148_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_firestore_149_ListLocationsResponseOut",
        "GoogleFirestoreAdminV1ListBackupSchedulesResponseIn": "_firestore_150_GoogleFirestoreAdminV1ListBackupSchedulesResponseIn",
        "GoogleFirestoreAdminV1ListBackupSchedulesResponseOut": "_firestore_151_GoogleFirestoreAdminV1ListBackupSchedulesResponseOut",
        "AggregationResultIn": "_firestore_152_AggregationResultIn",
        "AggregationResultOut": "_firestore_153_AggregationResultOut",
        "GoogleFirestoreAdminV1DatabaseIn": "_firestore_154_GoogleFirestoreAdminV1DatabaseIn",
        "GoogleFirestoreAdminV1DatabaseOut": "_firestore_155_GoogleFirestoreAdminV1DatabaseOut",
        "CommitResponseIn": "_firestore_156_CommitResponseIn",
        "CommitResponseOut": "_firestore_157_CommitResponseOut",
        "TargetIn": "_firestore_158_TargetIn",
        "TargetOut": "_firestore_159_TargetOut",
        "DocumentDeleteIn": "_firestore_160_DocumentDeleteIn",
        "DocumentDeleteOut": "_firestore_161_DocumentDeleteOut",
        "CursorIn": "_firestore_162_CursorIn",
        "CursorOut": "_firestore_163_CursorOut",
        "DocumentIn": "_firestore_164_DocumentIn",
        "DocumentOut": "_firestore_165_DocumentOut",
        "RunQueryResponseIn": "_firestore_166_RunQueryResponseIn",
        "RunQueryResponseOut": "_firestore_167_RunQueryResponseOut",
        "GoogleFirestoreAdminV1IndexOperationMetadataIn": "_firestore_168_GoogleFirestoreAdminV1IndexOperationMetadataIn",
        "GoogleFirestoreAdminV1IndexOperationMetadataOut": "_firestore_169_GoogleFirestoreAdminV1IndexOperationMetadataOut",
        "MapValueIn": "_firestore_170_MapValueIn",
        "MapValueOut": "_firestore_171_MapValueOut",
        "DocumentTransformIn": "_firestore_172_DocumentTransformIn",
        "DocumentTransformOut": "_firestore_173_DocumentTransformOut",
        "CommitRequestIn": "_firestore_174_CommitRequestIn",
        "CommitRequestOut": "_firestore_175_CommitRequestOut",
        "BeginTransactionResponseIn": "_firestore_176_BeginTransactionResponseIn",
        "BeginTransactionResponseOut": "_firestore_177_BeginTransactionResponseOut",
        "GoogleFirestoreAdminV1IndexFieldIn": "_firestore_178_GoogleFirestoreAdminV1IndexFieldIn",
        "GoogleFirestoreAdminV1IndexFieldOut": "_firestore_179_GoogleFirestoreAdminV1IndexFieldOut",
        "CompositeFilterIn": "_firestore_180_CompositeFilterIn",
        "CompositeFilterOut": "_firestore_181_CompositeFilterOut",
        "FieldReferenceIn": "_firestore_182_FieldReferenceIn",
        "FieldReferenceOut": "_firestore_183_FieldReferenceOut",
        "AggregationIn": "_firestore_184_AggregationIn",
        "AggregationOut": "_firestore_185_AggregationOut",
        "ReadOnlyIn": "_firestore_186_ReadOnlyIn",
        "ReadOnlyOut": "_firestore_187_ReadOnlyOut",
        "GoogleLongrunningOperationIn": "_firestore_188_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_firestore_189_GoogleLongrunningOperationOut",
        "WriteResultIn": "_firestore_190_WriteResultIn",
        "WriteResultOut": "_firestore_191_WriteResultOut",
        "ListDocumentsResponseIn": "_firestore_192_ListDocumentsResponseIn",
        "ListDocumentsResponseOut": "_firestore_193_ListDocumentsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ListenRequestIn"] = t.struct(
        {
            "addTarget": t.proxy(renames["TargetIn"]).optional(),
            "removeTarget": t.integer().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ListenRequestIn"])
    types["ListenRequestOut"] = t.struct(
        {
            "addTarget": t.proxy(renames["TargetOut"]).optional(),
            "removeTarget": t.integer().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListenRequestOut"])
    types["DocumentChangeIn"] = t.struct(
        {
            "targetIds": t.array(t.integer()).optional(),
            "document": t.proxy(renames["DocumentIn"]).optional(),
            "removedTargetIds": t.array(t.integer()).optional(),
        }
    ).named(renames["DocumentChangeIn"])
    types["DocumentChangeOut"] = t.struct(
        {
            "targetIds": t.array(t.integer()).optional(),
            "document": t.proxy(renames["DocumentOut"]).optional(),
            "removedTargetIds": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentChangeOut"])
    types["BeginTransactionRequestIn"] = t.struct(
        {"options": t.proxy(renames["TransactionOptionsIn"]).optional()}
    ).named(renames["BeginTransactionRequestIn"])
    types["BeginTransactionRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["TransactionOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BeginTransactionRequestOut"])
    types["GoogleFirestoreAdminV1StatsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1StatsIn"])
    types["GoogleFirestoreAdminV1StatsOut"] = t.struct(
        {
            "indexCount": t.string().optional(),
            "documentCount": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1StatsOut"])
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
    types["GoogleFirestoreAdminV1BackupIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1BackupIn"])
    types["GoogleFirestoreAdminV1BackupOut"] = t.struct(
        {
            "databaseUid": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "snapshotTime": t.string().optional(),
            "expireTime": t.string().optional(),
            "stats": t.proxy(renames["GoogleFirestoreAdminV1StatsOut"]).optional(),
            "database": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1BackupOut"])
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
    types["ValueIn"] = t.struct(
        {
            "referenceValue": t.string().optional(),
            "nullValue": t.string().optional(),
            "arrayValue": t.proxy(renames["ArrayValueIn"]).optional(),
            "geoPointValue": t.proxy(renames["LatLngIn"]).optional(),
            "stringValue": t.string().optional(),
            "integerValue": t.string().optional(),
            "booleanValue": t.boolean().optional(),
            "bytesValue": t.string().optional(),
            "mapValue": t.proxy(renames["MapValueIn"]).optional(),
            "timestampValue": t.string().optional(),
            "doubleValue": t.number().optional(),
        }
    ).named(renames["ValueIn"])
    types["ValueOut"] = t.struct(
        {
            "referenceValue": t.string().optional(),
            "nullValue": t.string().optional(),
            "arrayValue": t.proxy(renames["ArrayValueOut"]).optional(),
            "geoPointValue": t.proxy(renames["LatLngOut"]).optional(),
            "stringValue": t.string().optional(),
            "integerValue": t.string().optional(),
            "booleanValue": t.boolean().optional(),
            "bytesValue": t.string().optional(),
            "mapValue": t.proxy(renames["MapValueOut"]).optional(),
            "timestampValue": t.string().optional(),
            "doubleValue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueOut"])
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
    types["GoogleFirestoreAdminV1ExportDocumentsMetadataIn"] = t.struct(
        {
            "collectionIds": t.array(t.string()).optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
            "operationState": t.string().optional(),
            "outputUriPrefix": t.string().optional(),
            "namespaceIds": t.array(t.string()).optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ExportDocumentsMetadataIn"])
    types["GoogleFirestoreAdminV1ExportDocumentsMetadataOut"] = t.struct(
        {
            "collectionIds": t.array(t.string()).optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "operationState": t.string().optional(),
            "outputUriPrefix": t.string().optional(),
            "namespaceIds": t.array(t.string()).optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ExportDocumentsMetadataOut"])
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
    types["GoogleFirestoreAdminV1WeeklyRecurrenceIn"] = t.struct(
        {"day": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1WeeklyRecurrenceIn"])
    types["GoogleFirestoreAdminV1WeeklyRecurrenceOut"] = t.struct(
        {
            "day": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1WeeklyRecurrenceOut"])
    types["PartitionQueryRequestIn"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "readTime": t.string().optional(),
            "partitionCount": t.string().optional(),
            "structuredQuery": t.proxy(renames["StructuredQueryIn"]).optional(),
        }
    ).named(renames["PartitionQueryRequestIn"])
    types["PartitionQueryRequestOut"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "readTime": t.string().optional(),
            "partitionCount": t.string().optional(),
            "structuredQuery": t.proxy(renames["StructuredQueryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionQueryRequestOut"])
    types["StructuredAggregationQueryIn"] = t.struct(
        {
            "aggregations": t.array(t.proxy(renames["AggregationIn"])).optional(),
            "structuredQuery": t.proxy(renames["StructuredQueryIn"]).optional(),
        }
    ).named(renames["StructuredAggregationQueryIn"])
    types["StructuredAggregationQueryOut"] = t.struct(
        {
            "aggregations": t.array(t.proxy(renames["AggregationOut"])).optional(),
            "structuredQuery": t.proxy(renames["StructuredQueryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructuredAggregationQueryOut"])
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["BloomFilterIn"] = t.struct(
        {
            "bits": t.proxy(renames["BitSequenceIn"]).optional(),
            "hashCount": t.integer().optional(),
        }
    ).named(renames["BloomFilterIn"])
    types["BloomFilterOut"] = t.struct(
        {
            "bits": t.proxy(renames["BitSequenceOut"]).optional(),
            "hashCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BloomFilterOut"])
    types["GoogleFirestoreAdminV1IndexIn"] = t.struct(
        {
            "apiScope": t.string().optional(),
            "state": t.string().optional(),
            "fields": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexFieldIn"])
            ).optional(),
            "name": t.string().optional(),
            "queryScope": t.string().optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexIn"])
    types["GoogleFirestoreAdminV1IndexOut"] = t.struct(
        {
            "apiScope": t.string().optional(),
            "state": t.string().optional(),
            "fields": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexFieldOut"])
            ).optional(),
            "name": t.string().optional(),
            "queryScope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexOut"])
    types["GoogleFirestoreAdminV1ImportDocumentsMetadataIn"] = t.struct(
        {
            "inputUriPrefix": t.string().optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
            "collectionIds": t.array(t.string()).optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
            "namespaceIds": t.array(t.string()).optional(),
            "operationState": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ImportDocumentsMetadataIn"])
    types["GoogleFirestoreAdminV1ImportDocumentsMetadataOut"] = t.struct(
        {
            "inputUriPrefix": t.string().optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "collectionIds": t.array(t.string()).optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "namespaceIds": t.array(t.string()).optional(),
            "operationState": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ImportDocumentsMetadataOut"])
    types["GoogleFirestoreAdminV1ExportDocumentsResponseIn"] = t.struct(
        {"outputUriPrefix": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1ExportDocumentsResponseIn"])
    types["GoogleFirestoreAdminV1ExportDocumentsResponseOut"] = t.struct(
        {
            "outputUriPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ExportDocumentsResponseOut"])
    types["ProjectionIn"] = t.struct(
        {"fields": t.array(t.proxy(renames["FieldReferenceIn"])).optional()}
    ).named(renames["ProjectionIn"])
    types["ProjectionOut"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["FieldReferenceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectionOut"])
    types["FieldTransformIn"] = t.struct(
        {
            "fieldPath": t.string().optional(),
            "appendMissingElements": t.proxy(renames["ArrayValueIn"]).optional(),
            "setToServerValue": t.string().optional(),
            "maximum": t.proxy(renames["ValueIn"]).optional(),
            "increment": t.proxy(renames["ValueIn"]).optional(),
            "removeAllFromArray": t.proxy(renames["ArrayValueIn"]).optional(),
            "minimum": t.proxy(renames["ValueIn"]).optional(),
        }
    ).named(renames["FieldTransformIn"])
    types["FieldTransformOut"] = t.struct(
        {
            "fieldPath": t.string().optional(),
            "appendMissingElements": t.proxy(renames["ArrayValueOut"]).optional(),
            "setToServerValue": t.string().optional(),
            "maximum": t.proxy(renames["ValueOut"]).optional(),
            "increment": t.proxy(renames["ValueOut"]).optional(),
            "removeAllFromArray": t.proxy(renames["ArrayValueOut"]).optional(),
            "minimum": t.proxy(renames["ValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldTransformOut"])
    types["CollectionSelectorIn"] = t.struct(
        {
            "collectionId": t.string().optional(),
            "allDescendants": t.boolean().optional(),
        }
    ).named(renames["CollectionSelectorIn"])
    types["CollectionSelectorOut"] = t.struct(
        {
            "collectionId": t.string().optional(),
            "allDescendants": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CollectionSelectorOut"])
    types["BatchWriteRequestIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "writes": t.array(t.proxy(renames["WriteIn"])).optional(),
        }
    ).named(renames["BatchWriteRequestIn"])
    types["BatchWriteRequestOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "writes": t.array(t.proxy(renames["WriteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchWriteRequestOut"])
    types["GoogleFirestoreAdminV1LocationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1LocationMetadataIn"])
    types["GoogleFirestoreAdminV1LocationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleFirestoreAdminV1LocationMetadataOut"])
    types["GoogleFirestoreAdminV1TtlConfigDeltaIn"] = t.struct(
        {"changeType": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1TtlConfigDeltaIn"])
    types["GoogleFirestoreAdminV1TtlConfigDeltaOut"] = t.struct(
        {
            "changeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1TtlConfigDeltaOut"])
    types["DocumentMaskIn"] = t.struct(
        {"fieldPaths": t.array(t.string()).optional()}
    ).named(renames["DocumentMaskIn"])
    types["DocumentMaskOut"] = t.struct(
        {
            "fieldPaths": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentMaskOut"])
    types["FilterIn"] = t.struct(
        {
            "unaryFilter": t.proxy(renames["UnaryFilterIn"]).optional(),
            "compositeFilter": t.proxy(renames["CompositeFilterIn"]).optional(),
            "fieldFilter": t.proxy(renames["FieldFilterIn"]).optional(),
        }
    ).named(renames["FilterIn"])
    types["FilterOut"] = t.struct(
        {
            "unaryFilter": t.proxy(renames["UnaryFilterOut"]).optional(),
            "compositeFilter": t.proxy(renames["CompositeFilterOut"]).optional(),
            "fieldFilter": t.proxy(renames["FieldFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterOut"])
    types["StructuredQueryIn"] = t.struct(
        {
            "limit": t.integer().optional(),
            "startAt": t.proxy(renames["CursorIn"]).optional(),
            "orderBy": t.array(t.proxy(renames["OrderIn"])).optional(),
            "endAt": t.proxy(renames["CursorIn"]).optional(),
            "from": t.array(t.proxy(renames["CollectionSelectorIn"])).optional(),
            "offset": t.integer().optional(),
            "where": t.proxy(renames["FilterIn"]).optional(),
            "select": t.proxy(renames["ProjectionIn"]).optional(),
        }
    ).named(renames["StructuredQueryIn"])
    types["StructuredQueryOut"] = t.struct(
        {
            "limit": t.integer().optional(),
            "startAt": t.proxy(renames["CursorOut"]).optional(),
            "orderBy": t.array(t.proxy(renames["OrderOut"])).optional(),
            "endAt": t.proxy(renames["CursorOut"]).optional(),
            "from": t.array(t.proxy(renames["CollectionSelectorOut"])).optional(),
            "offset": t.integer().optional(),
            "where": t.proxy(renames["FilterOut"]).optional(),
            "select": t.proxy(renames["ProjectionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructuredQueryOut"])
    types["RollbackRequestIn"] = t.struct({"transaction": t.string()}).named(
        renames["RollbackRequestIn"]
    )
    types["RollbackRequestOut"] = t.struct(
        {
            "transaction": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RollbackRequestOut"])
    types["GoogleFirestoreAdminV1UpdateDatabaseMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1UpdateDatabaseMetadataIn"])
    types["GoogleFirestoreAdminV1UpdateDatabaseMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleFirestoreAdminV1UpdateDatabaseMetadataOut"])
    types["BatchGetDocumentsResponseIn"] = t.struct(
        {
            "found": t.proxy(renames["DocumentIn"]).optional(),
            "transaction": t.string().optional(),
            "missing": t.string().optional(),
            "readTime": t.string().optional(),
        }
    ).named(renames["BatchGetDocumentsResponseIn"])
    types["BatchGetDocumentsResponseOut"] = t.struct(
        {
            "found": t.proxy(renames["DocumentOut"]).optional(),
            "transaction": t.string().optional(),
            "missing": t.string().optional(),
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetDocumentsResponseOut"])
    types["OrderIn"] = t.struct(
        {
            "direction": t.string().optional(),
            "field": t.proxy(renames["FieldReferenceIn"]).optional(),
        }
    ).named(renames["OrderIn"])
    types["OrderOut"] = t.struct(
        {
            "direction": t.string().optional(),
            "field": t.proxy(renames["FieldReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderOut"])
    types["ListCollectionIdsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "collectionIds": t.array(t.string()).optional(),
        }
    ).named(renames["ListCollectionIdsResponseIn"])
    types["ListCollectionIdsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "collectionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCollectionIdsResponseOut"])
    types["WriteResponseIn"] = t.struct(
        {
            "commitTime": t.string().optional(),
            "streamToken": t.string().optional(),
            "writeResults": t.array(t.proxy(renames["WriteResultIn"])).optional(),
            "streamId": t.string().optional(),
        }
    ).named(renames["WriteResponseIn"])
    types["WriteResponseOut"] = t.struct(
        {
            "commitTime": t.string().optional(),
            "streamToken": t.string().optional(),
            "writeResults": t.array(t.proxy(renames["WriteResultOut"])).optional(),
            "streamId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteResponseOut"])
    types["GoogleFirestoreAdminV1IndexConfigIn"] = t.struct(
        {
            "indexes": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexIn"])
            ).optional(),
            "reverting": t.boolean().optional(),
            "usesAncestorConfig": t.boolean().optional(),
            "ancestorField": t.string().optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexConfigIn"])
    types["GoogleFirestoreAdminV1IndexConfigOut"] = t.struct(
        {
            "indexes": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexOut"])
            ).optional(),
            "reverting": t.boolean().optional(),
            "usesAncestorConfig": t.boolean().optional(),
            "ancestorField": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexConfigOut"])
    types["GoogleFirestoreAdminV1FieldOperationMetadataIn"] = t.struct(
        {
            "field": t.string().optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
            "endTime": t.string().optional(),
            "indexConfigDeltas": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexConfigDeltaIn"])
            ).optional(),
            "ttlConfigDelta": t.proxy(
                renames["GoogleFirestoreAdminV1TtlConfigDeltaIn"]
            ).optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
            "startTime": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1FieldOperationMetadataIn"])
    types["GoogleFirestoreAdminV1FieldOperationMetadataOut"] = t.struct(
        {
            "field": t.string().optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "endTime": t.string().optional(),
            "indexConfigDeltas": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexConfigDeltaOut"])
            ).optional(),
            "ttlConfigDelta": t.proxy(
                renames["GoogleFirestoreAdminV1TtlConfigDeltaOut"]
            ).optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1FieldOperationMetadataOut"])
    types["ExistenceFilterIn"] = t.struct(
        {
            "targetId": t.integer().optional(),
            "count": t.integer().optional(),
            "unchangedNames": t.proxy(renames["BloomFilterIn"]).optional(),
        }
    ).named(renames["ExistenceFilterIn"])
    types["ExistenceFilterOut"] = t.struct(
        {
            "targetId": t.integer().optional(),
            "count": t.integer().optional(),
            "unchangedNames": t.proxy(renames["BloomFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExistenceFilterOut"])
    types["GoogleFirestoreAdminV1BackupScheduleIn"] = t.struct(
        {
            "weeklyRecurrence": t.proxy(
                renames["GoogleFirestoreAdminV1WeeklyRecurrenceIn"]
            ).optional(),
            "retention": t.string().optional(),
            "dailyRecurrence": t.proxy(
                renames["GoogleFirestoreAdminV1DailyRecurrenceIn"]
            ).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1BackupScheduleIn"])
    types["GoogleFirestoreAdminV1BackupScheduleOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "weeklyRecurrence": t.proxy(
                renames["GoogleFirestoreAdminV1WeeklyRecurrenceOut"]
            ).optional(),
            "retention": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "dailyRecurrence": t.proxy(
                renames["GoogleFirestoreAdminV1DailyRecurrenceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1BackupScheduleOut"])
    types["WriteIn"] = t.struct(
        {
            "update": t.proxy(renames["DocumentIn"]).optional(),
            "currentDocument": t.proxy(renames["PreconditionIn"]).optional(),
            "delete": t.string().optional(),
            "updateMask": t.proxy(renames["DocumentMaskIn"]).optional(),
            "updateTransforms": t.array(
                t.proxy(renames["FieldTransformIn"])
            ).optional(),
            "transform": t.proxy(renames["DocumentTransformIn"]).optional(),
        }
    ).named(renames["WriteIn"])
    types["WriteOut"] = t.struct(
        {
            "update": t.proxy(renames["DocumentOut"]).optional(),
            "currentDocument": t.proxy(renames["PreconditionOut"]).optional(),
            "delete": t.string().optional(),
            "updateMask": t.proxy(renames["DocumentMaskOut"]).optional(),
            "updateTransforms": t.array(
                t.proxy(renames["FieldTransformOut"])
            ).optional(),
            "transform": t.proxy(renames["DocumentTransformOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteOut"])
    types["BatchGetDocumentsRequestIn"] = t.struct(
        {
            "documents": t.array(t.string()).optional(),
            "transaction": t.string().optional(),
            "readTime": t.string().optional(),
            "mask": t.proxy(renames["DocumentMaskIn"]).optional(),
            "newTransaction": t.proxy(renames["TransactionOptionsIn"]).optional(),
        }
    ).named(renames["BatchGetDocumentsRequestIn"])
    types["BatchGetDocumentsRequestOut"] = t.struct(
        {
            "documents": t.array(t.string()).optional(),
            "transaction": t.string().optional(),
            "readTime": t.string().optional(),
            "mask": t.proxy(renames["DocumentMaskOut"]).optional(),
            "newTransaction": t.proxy(renames["TransactionOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetDocumentsRequestOut"])
    types["WriteRequestIn"] = t.struct(
        {
            "streamId": t.string().optional(),
            "streamToken": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "writes": t.array(t.proxy(renames["WriteIn"])).optional(),
        }
    ).named(renames["WriteRequestIn"])
    types["WriteRequestOut"] = t.struct(
        {
            "streamId": t.string().optional(),
            "streamToken": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "writes": t.array(t.proxy(renames["WriteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteRequestOut"])
    types["CountIn"] = t.struct({"upTo": t.string().optional()}).named(
        renames["CountIn"]
    )
    types["CountOut"] = t.struct(
        {
            "upTo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CountOut"])
    types["LocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["TargetChangeIn"] = t.struct(
        {
            "targetIds": t.array(t.integer()).optional(),
            "resumeToken": t.string().optional(),
            "targetChangeType": t.string().optional(),
            "cause": t.proxy(renames["StatusIn"]).optional(),
            "readTime": t.string().optional(),
        }
    ).named(renames["TargetChangeIn"])
    types["TargetChangeOut"] = t.struct(
        {
            "targetIds": t.array(t.integer()).optional(),
            "resumeToken": t.string().optional(),
            "targetChangeType": t.string().optional(),
            "cause": t.proxy(renames["StatusOut"]).optional(),
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetChangeOut"])
    types["ArrayValueIn"] = t.struct(
        {"values": t.array(t.proxy(renames["ValueIn"])).optional()}
    ).named(renames["ArrayValueIn"])
    types["ArrayValueOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["ValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArrayValueOut"])
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
    types["FieldFilterIn"] = t.struct(
        {
            "field": t.proxy(renames["FieldReferenceIn"]).optional(),
            "value": t.proxy(renames["ValueIn"]).optional(),
            "op": t.string().optional(),
        }
    ).named(renames["FieldFilterIn"])
    types["FieldFilterOut"] = t.struct(
        {
            "field": t.proxy(renames["FieldReferenceOut"]).optional(),
            "value": t.proxy(renames["ValueOut"]).optional(),
            "op": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldFilterOut"])
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
    types["DocumentRemoveIn"] = t.struct(
        {
            "removedTargetIds": t.array(t.integer()).optional(),
            "document": t.string().optional(),
            "readTime": t.string().optional(),
        }
    ).named(renames["DocumentRemoveIn"])
    types["DocumentRemoveOut"] = t.struct(
        {
            "removedTargetIds": t.array(t.integer()).optional(),
            "document": t.string().optional(),
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentRemoveOut"])
    types["GoogleFirestoreAdminV1ListBackupsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "backups": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1BackupIn"])
            ).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ListBackupsResponseIn"])
    types["GoogleFirestoreAdminV1ListBackupsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "backups": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1BackupOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ListBackupsResponseOut"])
    types["GoogleFirestoreAdminV1RestoreDatabaseRequestIn"] = t.struct(
        {"backup": t.string(), "databaseId": t.string()}
    ).named(renames["GoogleFirestoreAdminV1RestoreDatabaseRequestIn"])
    types["GoogleFirestoreAdminV1RestoreDatabaseRequestOut"] = t.struct(
        {
            "backup": t.string(),
            "databaseId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1RestoreDatabaseRequestOut"])
    types["BitSequenceIn"] = t.struct(
        {"bitmap": t.string().optional(), "padding": t.integer().optional()}
    ).named(renames["BitSequenceIn"])
    types["BitSequenceOut"] = t.struct(
        {
            "bitmap": t.string().optional(),
            "padding": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BitSequenceOut"])
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
    types["ListenResponseIn"] = t.struct(
        {
            "documentChange": t.proxy(renames["DocumentChangeIn"]).optional(),
            "targetChange": t.proxy(renames["TargetChangeIn"]).optional(),
            "documentRemove": t.proxy(renames["DocumentRemoveIn"]).optional(),
            "documentDelete": t.proxy(renames["DocumentDeleteIn"]).optional(),
            "filter": t.proxy(renames["ExistenceFilterIn"]).optional(),
        }
    ).named(renames["ListenResponseIn"])
    types["ListenResponseOut"] = t.struct(
        {
            "documentChange": t.proxy(renames["DocumentChangeOut"]).optional(),
            "targetChange": t.proxy(renames["TargetChangeOut"]).optional(),
            "documentRemove": t.proxy(renames["DocumentRemoveOut"]).optional(),
            "documentDelete": t.proxy(renames["DocumentDeleteOut"]).optional(),
            "filter": t.proxy(renames["ExistenceFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListenResponseOut"])
    types["GoogleFirestoreAdminV1FieldIn"] = t.struct(
        {
            "indexConfig": t.proxy(
                renames["GoogleFirestoreAdminV1IndexConfigIn"]
            ).optional(),
            "name": t.string(),
            "ttlConfig": t.proxy(
                renames["GoogleFirestoreAdminV1TtlConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1FieldIn"])
    types["GoogleFirestoreAdminV1FieldOut"] = t.struct(
        {
            "indexConfig": t.proxy(
                renames["GoogleFirestoreAdminV1IndexConfigOut"]
            ).optional(),
            "name": t.string(),
            "ttlConfig": t.proxy(
                renames["GoogleFirestoreAdminV1TtlConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1FieldOut"])
    types["GoogleFirestoreAdminV1TtlConfigIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1TtlConfigIn"])
    types["GoogleFirestoreAdminV1TtlConfigOut"] = t.struct(
        {
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1TtlConfigOut"])
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
    types["DocumentsTargetIn"] = t.struct(
        {"documents": t.array(t.string()).optional()}
    ).named(renames["DocumentsTargetIn"])
    types["DocumentsTargetOut"] = t.struct(
        {
            "documents": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentsTargetOut"])
    types["RunQueryRequestIn"] = t.struct(
        {
            "transaction": t.string().optional(),
            "structuredQuery": t.proxy(renames["StructuredQueryIn"]).optional(),
            "newTransaction": t.proxy(renames["TransactionOptionsIn"]).optional(),
            "readTime": t.string().optional(),
        }
    ).named(renames["RunQueryRequestIn"])
    types["RunQueryRequestOut"] = t.struct(
        {
            "transaction": t.string().optional(),
            "structuredQuery": t.proxy(renames["StructuredQueryOut"]).optional(),
            "newTransaction": t.proxy(renames["TransactionOptionsOut"]).optional(),
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunQueryRequestOut"])
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
    types["ReadWriteIn"] = t.struct({"retryTransaction": t.string().optional()}).named(
        renames["ReadWriteIn"]
    )
    types["ReadWriteOut"] = t.struct(
        {
            "retryTransaction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadWriteOut"])
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
    types["RunAggregationQueryResponseIn"] = t.struct(
        {
            "result": t.proxy(renames["AggregationResultIn"]).optional(),
            "transaction": t.string().optional(),
            "readTime": t.string().optional(),
        }
    ).named(renames["RunAggregationQueryResponseIn"])
    types["RunAggregationQueryResponseOut"] = t.struct(
        {
            "result": t.proxy(renames["AggregationResultOut"]).optional(),
            "transaction": t.string().optional(),
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunAggregationQueryResponseOut"])
    types["RunAggregationQueryRequestIn"] = t.struct(
        {
            "transaction": t.string().optional(),
            "readTime": t.string().optional(),
            "structuredAggregationQuery": t.proxy(
                renames["StructuredAggregationQueryIn"]
            ).optional(),
            "newTransaction": t.proxy(renames["TransactionOptionsIn"]).optional(),
        }
    ).named(renames["RunAggregationQueryRequestIn"])
    types["RunAggregationQueryRequestOut"] = t.struct(
        {
            "transaction": t.string().optional(),
            "readTime": t.string().optional(),
            "structuredAggregationQuery": t.proxy(
                renames["StructuredAggregationQueryOut"]
            ).optional(),
            "newTransaction": t.proxy(renames["TransactionOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunAggregationQueryRequestOut"])
    types["GoogleFirestoreAdminV1ExportDocumentsRequestIn"] = t.struct(
        {
            "namespaceIds": t.array(t.string()).optional(),
            "outputUriPrefix": t.string().optional(),
            "collectionIds": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ExportDocumentsRequestIn"])
    types["GoogleFirestoreAdminV1ExportDocumentsRequestOut"] = t.struct(
        {
            "namespaceIds": t.array(t.string()).optional(),
            "outputUriPrefix": t.string().optional(),
            "collectionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ExportDocumentsRequestOut"])
    types["GoogleFirestoreAdminV1ListFieldsResponseIn"] = t.struct(
        {
            "fields": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1FieldIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ListFieldsResponseIn"])
    types["GoogleFirestoreAdminV1ListFieldsResponseOut"] = t.struct(
        {
            "fields": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1FieldOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ListFieldsResponseOut"])
    types["GoogleFirestoreAdminV1ImportDocumentsRequestIn"] = t.struct(
        {
            "inputUriPrefix": t.string().optional(),
            "collectionIds": t.array(t.string()).optional(),
            "namespaceIds": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ImportDocumentsRequestIn"])
    types["GoogleFirestoreAdminV1ImportDocumentsRequestOut"] = t.struct(
        {
            "inputUriPrefix": t.string().optional(),
            "collectionIds": t.array(t.string()).optional(),
            "namespaceIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ImportDocumentsRequestOut"])
    types["GoogleFirestoreAdminV1DailyRecurrenceIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1DailyRecurrenceIn"])
    types["GoogleFirestoreAdminV1DailyRecurrenceOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleFirestoreAdminV1DailyRecurrenceOut"])
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
    types["GoogleFirestoreAdminV1ListBackupSchedulesResponseIn"] = t.struct(
        {
            "backupSchedules": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1BackupScheduleIn"])
            ).optional()
        }
    ).named(renames["GoogleFirestoreAdminV1ListBackupSchedulesResponseIn"])
    types["GoogleFirestoreAdminV1ListBackupSchedulesResponseOut"] = t.struct(
        {
            "backupSchedules": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1BackupScheduleOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ListBackupSchedulesResponseOut"])
    types["AggregationResultIn"] = t.struct(
        {"aggregateFields": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["AggregationResultIn"])
    types["AggregationResultOut"] = t.struct(
        {
            "aggregateFields": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationResultOut"])
    types["GoogleFirestoreAdminV1DatabaseIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "deleteProtectionState": t.string().optional(),
            "concurrencyMode": t.string().optional(),
            "appEngineIntegrationMode": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1DatabaseIn"])
    types["GoogleFirestoreAdminV1DatabaseOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "updateTime": t.string().optional(),
            "keyPrefix": t.string().optional(),
            "createTime": t.string().optional(),
            "uid": t.string().optional(),
            "deleteProtectionState": t.string().optional(),
            "concurrencyMode": t.string().optional(),
            "appEngineIntegrationMode": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
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
    types["TargetIn"] = t.struct(
        {
            "expectedCount": t.integer().optional(),
            "query": t.proxy(renames["QueryTargetIn"]).optional(),
            "readTime": t.string().optional(),
            "documents": t.proxy(renames["DocumentsTargetIn"]).optional(),
            "targetId": t.integer().optional(),
            "resumeToken": t.string().optional(),
            "once": t.boolean().optional(),
        }
    ).named(renames["TargetIn"])
    types["TargetOut"] = t.struct(
        {
            "expectedCount": t.integer().optional(),
            "query": t.proxy(renames["QueryTargetOut"]).optional(),
            "readTime": t.string().optional(),
            "documents": t.proxy(renames["DocumentsTargetOut"]).optional(),
            "targetId": t.integer().optional(),
            "resumeToken": t.string().optional(),
            "once": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetOut"])
    types["DocumentDeleteIn"] = t.struct(
        {
            "readTime": t.string().optional(),
            "removedTargetIds": t.array(t.integer()).optional(),
            "document": t.string().optional(),
        }
    ).named(renames["DocumentDeleteIn"])
    types["DocumentDeleteOut"] = t.struct(
        {
            "readTime": t.string().optional(),
            "removedTargetIds": t.array(t.integer()).optional(),
            "document": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentDeleteOut"])
    types["CursorIn"] = t.struct(
        {
            "before": t.boolean().optional(),
            "values": t.array(t.proxy(renames["ValueIn"])).optional(),
        }
    ).named(renames["CursorIn"])
    types["CursorOut"] = t.struct(
        {
            "before": t.boolean().optional(),
            "values": t.array(t.proxy(renames["ValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CursorOut"])
    types["DocumentIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "fields": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["DocumentIn"])
    types["DocumentOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "fields": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentOut"])
    types["RunQueryResponseIn"] = t.struct(
        {
            "readTime": t.string().optional(),
            "done": t.boolean().optional(),
            "document": t.proxy(renames["DocumentIn"]).optional(),
            "transaction": t.string().optional(),
            "skippedResults": t.integer().optional(),
        }
    ).named(renames["RunQueryResponseIn"])
    types["RunQueryResponseOut"] = t.struct(
        {
            "readTime": t.string().optional(),
            "done": t.boolean().optional(),
            "document": t.proxy(renames["DocumentOut"]).optional(),
            "transaction": t.string().optional(),
            "skippedResults": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunQueryResponseOut"])
    types["GoogleFirestoreAdminV1IndexOperationMetadataIn"] = t.struct(
        {
            "state": t.string().optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
            "index": t.string().optional(),
            "endTime": t.string().optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexOperationMetadataIn"])
    types["GoogleFirestoreAdminV1IndexOperationMetadataOut"] = t.struct(
        {
            "state": t.string().optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "index": t.string().optional(),
            "endTime": t.string().optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexOperationMetadataOut"])
    types["MapValueIn"] = t.struct(
        {"fields": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["MapValueIn"])
    types["MapValueOut"] = t.struct(
        {
            "fields": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MapValueOut"])
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
    types["CommitRequestIn"] = t.struct(
        {
            "writes": t.array(t.proxy(renames["WriteIn"])).optional(),
            "transaction": t.string().optional(),
        }
    ).named(renames["CommitRequestIn"])
    types["CommitRequestOut"] = t.struct(
        {
            "writes": t.array(t.proxy(renames["WriteOut"])).optional(),
            "transaction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitRequestOut"])
    types["BeginTransactionResponseIn"] = t.struct(
        {"transaction": t.string().optional()}
    ).named(renames["BeginTransactionResponseIn"])
    types["BeginTransactionResponseOut"] = t.struct(
        {
            "transaction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BeginTransactionResponseOut"])
    types["GoogleFirestoreAdminV1IndexFieldIn"] = t.struct(
        {
            "order": t.string().optional(),
            "arrayConfig": t.string().optional(),
            "fieldPath": t.string().optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexFieldIn"])
    types["GoogleFirestoreAdminV1IndexFieldOut"] = t.struct(
        {
            "order": t.string().optional(),
            "arrayConfig": t.string().optional(),
            "fieldPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexFieldOut"])
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
    types["FieldReferenceIn"] = t.struct({"fieldPath": t.string().optional()}).named(
        renames["FieldReferenceIn"]
    )
    types["FieldReferenceOut"] = t.struct(
        {
            "fieldPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldReferenceOut"])
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
    types["ReadOnlyIn"] = t.struct({"readTime": t.string().optional()}).named(
        renames["ReadOnlyIn"]
    )
    types["ReadOnlyOut"] = t.struct(
        {
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadOnlyOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["WriteResultIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "transformResults": t.array(t.proxy(renames["ValueIn"])).optional(),
        }
    ).named(renames["WriteResultIn"])
    types["WriteResultOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "transformResults": t.array(t.proxy(renames["ValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteResultOut"])
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

    functions = {}
    functions["projectsDatabasesGet"] = firestore.post(
        "v1/{name}:importDocuments",
        t.struct(
            {
                "name": t.string(),
                "inputUriPrefix": t.string().optional(),
                "collectionIds": t.array(t.string()).optional(),
                "namespaceIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesRestore"] = firestore.post(
        "v1/{name}:importDocuments",
        t.struct(
            {
                "name": t.string(),
                "inputUriPrefix": t.string().optional(),
                "collectionIds": t.array(t.string()).optional(),
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
                "inputUriPrefix": t.string().optional(),
                "collectionIds": t.array(t.string()).optional(),
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
                "inputUriPrefix": t.string().optional(),
                "collectionIds": t.array(t.string()).optional(),
                "namespaceIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesExportDocuments"] = firestore.post(
        "v1/{name}:importDocuments",
        t.struct(
            {
                "name": t.string(),
                "inputUriPrefix": t.string().optional(),
                "collectionIds": t.array(t.string()).optional(),
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
                "inputUriPrefix": t.string().optional(),
                "collectionIds": t.array(t.string()).optional(),
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
                "inputUriPrefix": t.string().optional(),
                "collectionIds": t.array(t.string()).optional(),
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
                "inputUriPrefix": t.string().optional(),
                "collectionIds": t.array(t.string()).optional(),
                "namespaceIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesBackupSchedulesDelete"] = firestore.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "weeklyRecurrence": t.proxy(
                    renames["GoogleFirestoreAdminV1WeeklyRecurrenceIn"]
                ).optional(),
                "retention": t.string().optional(),
                "dailyRecurrence": t.proxy(
                    renames["GoogleFirestoreAdminV1DailyRecurrenceIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirestoreAdminV1BackupScheduleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesBackupSchedulesCreate"] = firestore.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "weeklyRecurrence": t.proxy(
                    renames["GoogleFirestoreAdminV1WeeklyRecurrenceIn"]
                ).optional(),
                "retention": t.string().optional(),
                "dailyRecurrence": t.proxy(
                    renames["GoogleFirestoreAdminV1DailyRecurrenceIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirestoreAdminV1BackupScheduleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesBackupSchedulesGet"] = firestore.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "weeklyRecurrence": t.proxy(
                    renames["GoogleFirestoreAdminV1WeeklyRecurrenceIn"]
                ).optional(),
                "retention": t.string().optional(),
                "dailyRecurrence": t.proxy(
                    renames["GoogleFirestoreAdminV1DailyRecurrenceIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirestoreAdminV1BackupScheduleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesBackupSchedulesList"] = firestore.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "weeklyRecurrence": t.proxy(
                    renames["GoogleFirestoreAdminV1WeeklyRecurrenceIn"]
                ).optional(),
                "retention": t.string().optional(),
                "dailyRecurrence": t.proxy(
                    renames["GoogleFirestoreAdminV1DailyRecurrenceIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirestoreAdminV1BackupScheduleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesBackupSchedulesPatch"] = firestore.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "weeklyRecurrence": t.proxy(
                    renames["GoogleFirestoreAdminV1WeeklyRecurrenceIn"]
                ).optional(),
                "retention": t.string().optional(),
                "dailyRecurrence": t.proxy(
                    renames["GoogleFirestoreAdminV1DailyRecurrenceIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirestoreAdminV1BackupScheduleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesOperationsDelete"] = firestore.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesOperationsGet"] = firestore.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesOperationsCancel"] = firestore.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesOperationsList"] = firestore.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
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
    functions["projectsDatabasesCollectionGroupsFieldsPatch"] = firestore.get(
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
    functions["projectsDatabasesCollectionGroupsIndexesGet"] = firestore.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesCollectionGroupsIndexesCreate"] = firestore.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesCollectionGroupsIndexesList"] = firestore.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesCollectionGroupsIndexesDelete"] = firestore.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsPatch"] = firestore.post(
        "v1/{parent}:listCollectionIds",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "readTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCollectionIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsPartitionQuery"] = firestore.post(
        "v1/{parent}:listCollectionIds",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "readTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCollectionIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsListDocuments"] = firestore.post(
        "v1/{parent}:listCollectionIds",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "readTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCollectionIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsCreateDocument"] = firestore.post(
        "v1/{parent}:listCollectionIds",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "readTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCollectionIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsList"] = firestore.post(
        "v1/{parent}:listCollectionIds",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "readTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCollectionIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsRunAggregationQuery"] = firestore.post(
        "v1/{parent}:listCollectionIds",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "readTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCollectionIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsCommit"] = firestore.post(
        "v1/{parent}:listCollectionIds",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "readTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCollectionIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsRollback"] = firestore.post(
        "v1/{parent}:listCollectionIds",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "readTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCollectionIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsGet"] = firestore.post(
        "v1/{parent}:listCollectionIds",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "readTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCollectionIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsWrite"] = firestore.post(
        "v1/{parent}:listCollectionIds",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "readTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCollectionIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsBatchGet"] = firestore.post(
        "v1/{parent}:listCollectionIds",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "readTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCollectionIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsBeginTransaction"] = firestore.post(
        "v1/{parent}:listCollectionIds",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "readTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCollectionIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsRunQuery"] = firestore.post(
        "v1/{parent}:listCollectionIds",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "readTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCollectionIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsListen"] = firestore.post(
        "v1/{parent}:listCollectionIds",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "readTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCollectionIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsDelete"] = firestore.post(
        "v1/{parent}:listCollectionIds",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "readTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCollectionIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsBatchWrite"] = firestore.post(
        "v1/{parent}:listCollectionIds",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "readTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCollectionIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsListCollectionIds"] = firestore.post(
        "v1/{parent}:listCollectionIds",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "readTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCollectionIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = firestore.get(
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
    functions["projectsLocationsList"] = firestore.get(
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
    functions["projectsLocationsBackupsGet"] = firestore.get(
        "v1/{parent}/backups",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirestoreAdminV1ListBackupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupsDelete"] = firestore.get(
        "v1/{parent}/backups",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirestoreAdminV1ListBackupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupsList"] = firestore.get(
        "v1/{parent}/backups",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirestoreAdminV1ListBackupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="firestore",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
