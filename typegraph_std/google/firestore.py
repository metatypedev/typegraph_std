from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_firestore() -> Import:
    firestore = HTTPRuntime("https://firestore.googleapis.com/")

    renames = {
        "ErrorResponse": "_firestore_1_ErrorResponse",
        "TargetIn": "_firestore_2_TargetIn",
        "TargetOut": "_firestore_3_TargetOut",
        "GoogleFirestoreAdminV1ListIndexesResponseIn": "_firestore_4_GoogleFirestoreAdminV1ListIndexesResponseIn",
        "GoogleFirestoreAdminV1ListIndexesResponseOut": "_firestore_5_GoogleFirestoreAdminV1ListIndexesResponseOut",
        "GoogleLongrunningListOperationsResponseIn": "_firestore_6_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_firestore_7_GoogleLongrunningListOperationsResponseOut",
        "OrderIn": "_firestore_8_OrderIn",
        "OrderOut": "_firestore_9_OrderOut",
        "GoogleFirestoreAdminV1IndexIn": "_firestore_10_GoogleFirestoreAdminV1IndexIn",
        "GoogleFirestoreAdminV1IndexOut": "_firestore_11_GoogleFirestoreAdminV1IndexOut",
        "GoogleFirestoreAdminV1ListBackupSchedulesResponseIn": "_firestore_12_GoogleFirestoreAdminV1ListBackupSchedulesResponseIn",
        "GoogleFirestoreAdminV1ListBackupSchedulesResponseOut": "_firestore_13_GoogleFirestoreAdminV1ListBackupSchedulesResponseOut",
        "BeginTransactionResponseIn": "_firestore_14_BeginTransactionResponseIn",
        "BeginTransactionResponseOut": "_firestore_15_BeginTransactionResponseOut",
        "ListLocationsResponseIn": "_firestore_16_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_firestore_17_ListLocationsResponseOut",
        "RunQueryRequestIn": "_firestore_18_RunQueryRequestIn",
        "RunQueryRequestOut": "_firestore_19_RunQueryRequestOut",
        "EmptyIn": "_firestore_20_EmptyIn",
        "EmptyOut": "_firestore_21_EmptyOut",
        "RunAggregationQueryResponseIn": "_firestore_22_RunAggregationQueryResponseIn",
        "RunAggregationQueryResponseOut": "_firestore_23_RunAggregationQueryResponseOut",
        "DocumentRemoveIn": "_firestore_24_DocumentRemoveIn",
        "DocumentRemoveOut": "_firestore_25_DocumentRemoveOut",
        "FieldReferenceIn": "_firestore_26_FieldReferenceIn",
        "FieldReferenceOut": "_firestore_27_FieldReferenceOut",
        "RunAggregationQueryRequestIn": "_firestore_28_RunAggregationQueryRequestIn",
        "RunAggregationQueryRequestOut": "_firestore_29_RunAggregationQueryRequestOut",
        "GoogleFirestoreAdminV1IndexConfigIn": "_firestore_30_GoogleFirestoreAdminV1IndexConfigIn",
        "GoogleFirestoreAdminV1IndexConfigOut": "_firestore_31_GoogleFirestoreAdminV1IndexConfigOut",
        "BloomFilterIn": "_firestore_32_BloomFilterIn",
        "BloomFilterOut": "_firestore_33_BloomFilterOut",
        "ListenResponseIn": "_firestore_34_ListenResponseIn",
        "ListenResponseOut": "_firestore_35_ListenResponseOut",
        "CommitRequestIn": "_firestore_36_CommitRequestIn",
        "CommitRequestOut": "_firestore_37_CommitRequestOut",
        "CommitResponseIn": "_firestore_38_CommitResponseIn",
        "CommitResponseOut": "_firestore_39_CommitResponseOut",
        "LatLngIn": "_firestore_40_LatLngIn",
        "LatLngOut": "_firestore_41_LatLngOut",
        "FilterIn": "_firestore_42_FilterIn",
        "FilterOut": "_firestore_43_FilterOut",
        "GoogleFirestoreAdminV1TtlConfigDeltaIn": "_firestore_44_GoogleFirestoreAdminV1TtlConfigDeltaIn",
        "GoogleFirestoreAdminV1TtlConfigDeltaOut": "_firestore_45_GoogleFirestoreAdminV1TtlConfigDeltaOut",
        "CollectionSelectorIn": "_firestore_46_CollectionSelectorIn",
        "CollectionSelectorOut": "_firestore_47_CollectionSelectorOut",
        "DocumentDeleteIn": "_firestore_48_DocumentDeleteIn",
        "DocumentDeleteOut": "_firestore_49_DocumentDeleteOut",
        "GoogleFirestoreAdminV1ListDatabasesResponseIn": "_firestore_50_GoogleFirestoreAdminV1ListDatabasesResponseIn",
        "GoogleFirestoreAdminV1ListDatabasesResponseOut": "_firestore_51_GoogleFirestoreAdminV1ListDatabasesResponseOut",
        "GoogleFirestoreAdminV1BackupIn": "_firestore_52_GoogleFirestoreAdminV1BackupIn",
        "GoogleFirestoreAdminV1BackupOut": "_firestore_53_GoogleFirestoreAdminV1BackupOut",
        "BitSequenceIn": "_firestore_54_BitSequenceIn",
        "BitSequenceOut": "_firestore_55_BitSequenceOut",
        "FieldFilterIn": "_firestore_56_FieldFilterIn",
        "FieldFilterOut": "_firestore_57_FieldFilterOut",
        "DocumentIn": "_firestore_58_DocumentIn",
        "DocumentOut": "_firestore_59_DocumentOut",
        "GoogleFirestoreAdminV1IndexFieldIn": "_firestore_60_GoogleFirestoreAdminV1IndexFieldIn",
        "GoogleFirestoreAdminV1IndexFieldOut": "_firestore_61_GoogleFirestoreAdminV1IndexFieldOut",
        "StatusIn": "_firestore_62_StatusIn",
        "StatusOut": "_firestore_63_StatusOut",
        "DocumentChangeIn": "_firestore_64_DocumentChangeIn",
        "DocumentChangeOut": "_firestore_65_DocumentChangeOut",
        "UnaryFilterIn": "_firestore_66_UnaryFilterIn",
        "UnaryFilterOut": "_firestore_67_UnaryFilterOut",
        "WriteResponseIn": "_firestore_68_WriteResponseIn",
        "WriteResponseOut": "_firestore_69_WriteResponseOut",
        "DocumentsTargetIn": "_firestore_70_DocumentsTargetIn",
        "DocumentsTargetOut": "_firestore_71_DocumentsTargetOut",
        "GoogleFirestoreAdminV1IndexOperationMetadataIn": "_firestore_72_GoogleFirestoreAdminV1IndexOperationMetadataIn",
        "GoogleFirestoreAdminV1IndexOperationMetadataOut": "_firestore_73_GoogleFirestoreAdminV1IndexOperationMetadataOut",
        "DocumentMaskIn": "_firestore_74_DocumentMaskIn",
        "DocumentMaskOut": "_firestore_75_DocumentMaskOut",
        "GoogleLongrunningOperationIn": "_firestore_76_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_firestore_77_GoogleLongrunningOperationOut",
        "StructuredAggregationQueryIn": "_firestore_78_StructuredAggregationQueryIn",
        "StructuredAggregationQueryOut": "_firestore_79_StructuredAggregationQueryOut",
        "GoogleFirestoreAdminV1FieldIn": "_firestore_80_GoogleFirestoreAdminV1FieldIn",
        "GoogleFirestoreAdminV1FieldOut": "_firestore_81_GoogleFirestoreAdminV1FieldOut",
        "ListCollectionIdsRequestIn": "_firestore_82_ListCollectionIdsRequestIn",
        "ListCollectionIdsRequestOut": "_firestore_83_ListCollectionIdsRequestOut",
        "FieldTransformIn": "_firestore_84_FieldTransformIn",
        "FieldTransformOut": "_firestore_85_FieldTransformOut",
        "ProjectionIn": "_firestore_86_ProjectionIn",
        "ProjectionOut": "_firestore_87_ProjectionOut",
        "GoogleLongrunningCancelOperationRequestIn": "_firestore_88_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_firestore_89_GoogleLongrunningCancelOperationRequestOut",
        "PartitionQueryRequestIn": "_firestore_90_PartitionQueryRequestIn",
        "PartitionQueryRequestOut": "_firestore_91_PartitionQueryRequestOut",
        "GoogleFirestoreAdminV1ImportDocumentsMetadataIn": "_firestore_92_GoogleFirestoreAdminV1ImportDocumentsMetadataIn",
        "GoogleFirestoreAdminV1ImportDocumentsMetadataOut": "_firestore_93_GoogleFirestoreAdminV1ImportDocumentsMetadataOut",
        "WriteIn": "_firestore_94_WriteIn",
        "WriteOut": "_firestore_95_WriteOut",
        "GoogleFirestoreAdminV1ExportDocumentsMetadataIn": "_firestore_96_GoogleFirestoreAdminV1ExportDocumentsMetadataIn",
        "GoogleFirestoreAdminV1ExportDocumentsMetadataOut": "_firestore_97_GoogleFirestoreAdminV1ExportDocumentsMetadataOut",
        "GoogleFirestoreAdminV1TtlConfigIn": "_firestore_98_GoogleFirestoreAdminV1TtlConfigIn",
        "GoogleFirestoreAdminV1TtlConfigOut": "_firestore_99_GoogleFirestoreAdminV1TtlConfigOut",
        "ReadOnlyIn": "_firestore_100_ReadOnlyIn",
        "ReadOnlyOut": "_firestore_101_ReadOnlyOut",
        "PartitionQueryResponseIn": "_firestore_102_PartitionQueryResponseIn",
        "PartitionQueryResponseOut": "_firestore_103_PartitionQueryResponseOut",
        "TargetChangeIn": "_firestore_104_TargetChangeIn",
        "TargetChangeOut": "_firestore_105_TargetChangeOut",
        "RunQueryResponseIn": "_firestore_106_RunQueryResponseIn",
        "RunQueryResponseOut": "_firestore_107_RunQueryResponseOut",
        "BeginTransactionRequestIn": "_firestore_108_BeginTransactionRequestIn",
        "BeginTransactionRequestOut": "_firestore_109_BeginTransactionRequestOut",
        "GoogleFirestoreAdminV1WeeklyRecurrenceIn": "_firestore_110_GoogleFirestoreAdminV1WeeklyRecurrenceIn",
        "GoogleFirestoreAdminV1WeeklyRecurrenceOut": "_firestore_111_GoogleFirestoreAdminV1WeeklyRecurrenceOut",
        "GoogleFirestoreAdminV1LocationMetadataIn": "_firestore_112_GoogleFirestoreAdminV1LocationMetadataIn",
        "GoogleFirestoreAdminV1LocationMetadataOut": "_firestore_113_GoogleFirestoreAdminV1LocationMetadataOut",
        "ListDocumentsResponseIn": "_firestore_114_ListDocumentsResponseIn",
        "ListDocumentsResponseOut": "_firestore_115_ListDocumentsResponseOut",
        "GoogleFirestoreAdminV1BackupScheduleIn": "_firestore_116_GoogleFirestoreAdminV1BackupScheduleIn",
        "GoogleFirestoreAdminV1BackupScheduleOut": "_firestore_117_GoogleFirestoreAdminV1BackupScheduleOut",
        "BatchGetDocumentsRequestIn": "_firestore_118_BatchGetDocumentsRequestIn",
        "BatchGetDocumentsRequestOut": "_firestore_119_BatchGetDocumentsRequestOut",
        "GoogleFirestoreAdminV1FieldOperationMetadataIn": "_firestore_120_GoogleFirestoreAdminV1FieldOperationMetadataIn",
        "GoogleFirestoreAdminV1FieldOperationMetadataOut": "_firestore_121_GoogleFirestoreAdminV1FieldOperationMetadataOut",
        "BatchGetDocumentsResponseIn": "_firestore_122_BatchGetDocumentsResponseIn",
        "BatchGetDocumentsResponseOut": "_firestore_123_BatchGetDocumentsResponseOut",
        "ReadWriteIn": "_firestore_124_ReadWriteIn",
        "ReadWriteOut": "_firestore_125_ReadWriteOut",
        "GoogleFirestoreAdminV1ProgressIn": "_firestore_126_GoogleFirestoreAdminV1ProgressIn",
        "GoogleFirestoreAdminV1ProgressOut": "_firestore_127_GoogleFirestoreAdminV1ProgressOut",
        "RollbackRequestIn": "_firestore_128_RollbackRequestIn",
        "RollbackRequestOut": "_firestore_129_RollbackRequestOut",
        "GoogleFirestoreAdminV1ImportDocumentsRequestIn": "_firestore_130_GoogleFirestoreAdminV1ImportDocumentsRequestIn",
        "GoogleFirestoreAdminV1ImportDocumentsRequestOut": "_firestore_131_GoogleFirestoreAdminV1ImportDocumentsRequestOut",
        "AggregationResultIn": "_firestore_132_AggregationResultIn",
        "AggregationResultOut": "_firestore_133_AggregationResultOut",
        "GoogleFirestoreAdminV1IndexConfigDeltaIn": "_firestore_134_GoogleFirestoreAdminV1IndexConfigDeltaIn",
        "GoogleFirestoreAdminV1IndexConfigDeltaOut": "_firestore_135_GoogleFirestoreAdminV1IndexConfigDeltaOut",
        "TransactionOptionsIn": "_firestore_136_TransactionOptionsIn",
        "TransactionOptionsOut": "_firestore_137_TransactionOptionsOut",
        "GoogleFirestoreAdminV1RestoreDatabaseRequestIn": "_firestore_138_GoogleFirestoreAdminV1RestoreDatabaseRequestIn",
        "GoogleFirestoreAdminV1RestoreDatabaseRequestOut": "_firestore_139_GoogleFirestoreAdminV1RestoreDatabaseRequestOut",
        "GoogleFirestoreAdminV1ExportDocumentsResponseIn": "_firestore_140_GoogleFirestoreAdminV1ExportDocumentsResponseIn",
        "GoogleFirestoreAdminV1ExportDocumentsResponseOut": "_firestore_141_GoogleFirestoreAdminV1ExportDocumentsResponseOut",
        "GoogleFirestoreAdminV1ExportDocumentsRequestIn": "_firestore_142_GoogleFirestoreAdminV1ExportDocumentsRequestIn",
        "GoogleFirestoreAdminV1ExportDocumentsRequestOut": "_firestore_143_GoogleFirestoreAdminV1ExportDocumentsRequestOut",
        "QueryTargetIn": "_firestore_144_QueryTargetIn",
        "QueryTargetOut": "_firestore_145_QueryTargetOut",
        "WriteRequestIn": "_firestore_146_WriteRequestIn",
        "WriteRequestOut": "_firestore_147_WriteRequestOut",
        "GoogleFirestoreAdminV1DatabaseIn": "_firestore_148_GoogleFirestoreAdminV1DatabaseIn",
        "GoogleFirestoreAdminV1DatabaseOut": "_firestore_149_GoogleFirestoreAdminV1DatabaseOut",
        "GoogleFirestoreAdminV1DailyRecurrenceIn": "_firestore_150_GoogleFirestoreAdminV1DailyRecurrenceIn",
        "GoogleFirestoreAdminV1DailyRecurrenceOut": "_firestore_151_GoogleFirestoreAdminV1DailyRecurrenceOut",
        "ExistenceFilterIn": "_firestore_152_ExistenceFilterIn",
        "ExistenceFilterOut": "_firestore_153_ExistenceFilterOut",
        "GoogleFirestoreAdminV1UpdateDatabaseMetadataIn": "_firestore_154_GoogleFirestoreAdminV1UpdateDatabaseMetadataIn",
        "GoogleFirestoreAdminV1UpdateDatabaseMetadataOut": "_firestore_155_GoogleFirestoreAdminV1UpdateDatabaseMetadataOut",
        "LocationIn": "_firestore_156_LocationIn",
        "LocationOut": "_firestore_157_LocationOut",
        "CountIn": "_firestore_158_CountIn",
        "CountOut": "_firestore_159_CountOut",
        "ArrayValueIn": "_firestore_160_ArrayValueIn",
        "ArrayValueOut": "_firestore_161_ArrayValueOut",
        "StructuredQueryIn": "_firestore_162_StructuredQueryIn",
        "StructuredQueryOut": "_firestore_163_StructuredQueryOut",
        "GoogleFirestoreAdminV1StatsIn": "_firestore_164_GoogleFirestoreAdminV1StatsIn",
        "GoogleFirestoreAdminV1StatsOut": "_firestore_165_GoogleFirestoreAdminV1StatsOut",
        "CompositeFilterIn": "_firestore_166_CompositeFilterIn",
        "CompositeFilterOut": "_firestore_167_CompositeFilterOut",
        "PreconditionIn": "_firestore_168_PreconditionIn",
        "PreconditionOut": "_firestore_169_PreconditionOut",
        "DocumentTransformIn": "_firestore_170_DocumentTransformIn",
        "DocumentTransformOut": "_firestore_171_DocumentTransformOut",
        "GoogleFirestoreAdminV1ListBackupsResponseIn": "_firestore_172_GoogleFirestoreAdminV1ListBackupsResponseIn",
        "GoogleFirestoreAdminV1ListBackupsResponseOut": "_firestore_173_GoogleFirestoreAdminV1ListBackupsResponseOut",
        "WriteResultIn": "_firestore_174_WriteResultIn",
        "WriteResultOut": "_firestore_175_WriteResultOut",
        "ListenRequestIn": "_firestore_176_ListenRequestIn",
        "ListenRequestOut": "_firestore_177_ListenRequestOut",
        "CursorIn": "_firestore_178_CursorIn",
        "CursorOut": "_firestore_179_CursorOut",
        "ListCollectionIdsResponseIn": "_firestore_180_ListCollectionIdsResponseIn",
        "ListCollectionIdsResponseOut": "_firestore_181_ListCollectionIdsResponseOut",
        "AggregationIn": "_firestore_182_AggregationIn",
        "AggregationOut": "_firestore_183_AggregationOut",
        "GoogleFirestoreAdminV1ListFieldsResponseIn": "_firestore_184_GoogleFirestoreAdminV1ListFieldsResponseIn",
        "GoogleFirestoreAdminV1ListFieldsResponseOut": "_firestore_185_GoogleFirestoreAdminV1ListFieldsResponseOut",
        "BatchWriteResponseIn": "_firestore_186_BatchWriteResponseIn",
        "BatchWriteResponseOut": "_firestore_187_BatchWriteResponseOut",
        "ValueIn": "_firestore_188_ValueIn",
        "ValueOut": "_firestore_189_ValueOut",
        "MapValueIn": "_firestore_190_MapValueIn",
        "MapValueOut": "_firestore_191_MapValueOut",
        "BatchWriteRequestIn": "_firestore_192_BatchWriteRequestIn",
        "BatchWriteRequestOut": "_firestore_193_BatchWriteRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TargetIn"] = t.struct(
        {
            "readTime": t.string().optional(),
            "once": t.boolean().optional(),
            "query": t.proxy(renames["QueryTargetIn"]).optional(),
            "resumeToken": t.string().optional(),
            "documents": t.proxy(renames["DocumentsTargetIn"]).optional(),
            "expectedCount": t.integer().optional(),
            "targetId": t.integer().optional(),
        }
    ).named(renames["TargetIn"])
    types["TargetOut"] = t.struct(
        {
            "readTime": t.string().optional(),
            "once": t.boolean().optional(),
            "query": t.proxy(renames["QueryTargetOut"]).optional(),
            "resumeToken": t.string().optional(),
            "documents": t.proxy(renames["DocumentsTargetOut"]).optional(),
            "expectedCount": t.integer().optional(),
            "targetId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetOut"])
    types["GoogleFirestoreAdminV1ListIndexesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "indexes": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexIn"])
            ).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ListIndexesResponseIn"])
    types["GoogleFirestoreAdminV1ListIndexesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "indexes": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ListIndexesResponseOut"])
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
    types["GoogleFirestoreAdminV1IndexIn"] = t.struct(
        {
            "apiScope": t.string().optional(),
            "queryScope": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "fields": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexFieldIn"])
            ).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexIn"])
    types["GoogleFirestoreAdminV1IndexOut"] = t.struct(
        {
            "apiScope": t.string().optional(),
            "queryScope": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "fields": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexFieldOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexOut"])
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
    types["BeginTransactionResponseIn"] = t.struct(
        {"transaction": t.string().optional()}
    ).named(renames["BeginTransactionResponseIn"])
    types["BeginTransactionResponseOut"] = t.struct(
        {
            "transaction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BeginTransactionResponseOut"])
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
    types["RunQueryRequestIn"] = t.struct(
        {
            "transaction": t.string().optional(),
            "readTime": t.string().optional(),
            "structuredQuery": t.proxy(renames["StructuredQueryIn"]).optional(),
            "newTransaction": t.proxy(renames["TransactionOptionsIn"]).optional(),
        }
    ).named(renames["RunQueryRequestIn"])
    types["RunQueryRequestOut"] = t.struct(
        {
            "transaction": t.string().optional(),
            "readTime": t.string().optional(),
            "structuredQuery": t.proxy(renames["StructuredQueryOut"]).optional(),
            "newTransaction": t.proxy(renames["TransactionOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunQueryRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["RunAggregationQueryResponseIn"] = t.struct(
        {
            "readTime": t.string().optional(),
            "transaction": t.string().optional(),
            "result": t.proxy(renames["AggregationResultIn"]).optional(),
        }
    ).named(renames["RunAggregationQueryResponseIn"])
    types["RunAggregationQueryResponseOut"] = t.struct(
        {
            "readTime": t.string().optional(),
            "transaction": t.string().optional(),
            "result": t.proxy(renames["AggregationResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunAggregationQueryResponseOut"])
    types["DocumentRemoveIn"] = t.struct(
        {
            "document": t.string().optional(),
            "readTime": t.string().optional(),
            "removedTargetIds": t.array(t.integer()).optional(),
        }
    ).named(renames["DocumentRemoveIn"])
    types["DocumentRemoveOut"] = t.struct(
        {
            "document": t.string().optional(),
            "readTime": t.string().optional(),
            "removedTargetIds": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentRemoveOut"])
    types["FieldReferenceIn"] = t.struct({"fieldPath": t.string().optional()}).named(
        renames["FieldReferenceIn"]
    )
    types["FieldReferenceOut"] = t.struct(
        {
            "fieldPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldReferenceOut"])
    types["RunAggregationQueryRequestIn"] = t.struct(
        {
            "transaction": t.string().optional(),
            "structuredAggregationQuery": t.proxy(
                renames["StructuredAggregationQueryIn"]
            ).optional(),
            "newTransaction": t.proxy(renames["TransactionOptionsIn"]).optional(),
            "readTime": t.string().optional(),
        }
    ).named(renames["RunAggregationQueryRequestIn"])
    types["RunAggregationQueryRequestOut"] = t.struct(
        {
            "transaction": t.string().optional(),
            "structuredAggregationQuery": t.proxy(
                renames["StructuredAggregationQueryOut"]
            ).optional(),
            "newTransaction": t.proxy(renames["TransactionOptionsOut"]).optional(),
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunAggregationQueryRequestOut"])
    types["GoogleFirestoreAdminV1IndexConfigIn"] = t.struct(
        {
            "usesAncestorConfig": t.boolean().optional(),
            "ancestorField": t.string().optional(),
            "indexes": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexIn"])
            ).optional(),
            "reverting": t.boolean().optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexConfigIn"])
    types["GoogleFirestoreAdminV1IndexConfigOut"] = t.struct(
        {
            "usesAncestorConfig": t.boolean().optional(),
            "ancestorField": t.string().optional(),
            "indexes": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexOut"])
            ).optional(),
            "reverting": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexConfigOut"])
    types["BloomFilterIn"] = t.struct(
        {
            "hashCount": t.integer().optional(),
            "bits": t.proxy(renames["BitSequenceIn"]).optional(),
        }
    ).named(renames["BloomFilterIn"])
    types["BloomFilterOut"] = t.struct(
        {
            "hashCount": t.integer().optional(),
            "bits": t.proxy(renames["BitSequenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BloomFilterOut"])
    types["ListenResponseIn"] = t.struct(
        {
            "documentDelete": t.proxy(renames["DocumentDeleteIn"]).optional(),
            "documentChange": t.proxy(renames["DocumentChangeIn"]).optional(),
            "filter": t.proxy(renames["ExistenceFilterIn"]).optional(),
            "documentRemove": t.proxy(renames["DocumentRemoveIn"]).optional(),
            "targetChange": t.proxy(renames["TargetChangeIn"]).optional(),
        }
    ).named(renames["ListenResponseIn"])
    types["ListenResponseOut"] = t.struct(
        {
            "documentDelete": t.proxy(renames["DocumentDeleteOut"]).optional(),
            "documentChange": t.proxy(renames["DocumentChangeOut"]).optional(),
            "filter": t.proxy(renames["ExistenceFilterOut"]).optional(),
            "documentRemove": t.proxy(renames["DocumentRemoveOut"]).optional(),
            "targetChange": t.proxy(renames["TargetChangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListenResponseOut"])
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
    types["FilterIn"] = t.struct(
        {
            "compositeFilter": t.proxy(renames["CompositeFilterIn"]).optional(),
            "unaryFilter": t.proxy(renames["UnaryFilterIn"]).optional(),
            "fieldFilter": t.proxy(renames["FieldFilterIn"]).optional(),
        }
    ).named(renames["FilterIn"])
    types["FilterOut"] = t.struct(
        {
            "compositeFilter": t.proxy(renames["CompositeFilterOut"]).optional(),
            "unaryFilter": t.proxy(renames["UnaryFilterOut"]).optional(),
            "fieldFilter": t.proxy(renames["FieldFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterOut"])
    types["GoogleFirestoreAdminV1TtlConfigDeltaIn"] = t.struct(
        {"changeType": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1TtlConfigDeltaIn"])
    types["GoogleFirestoreAdminV1TtlConfigDeltaOut"] = t.struct(
        {
            "changeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1TtlConfigDeltaOut"])
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
    types["DocumentDeleteIn"] = t.struct(
        {
            "removedTargetIds": t.array(t.integer()).optional(),
            "readTime": t.string().optional(),
            "document": t.string().optional(),
        }
    ).named(renames["DocumentDeleteIn"])
    types["DocumentDeleteOut"] = t.struct(
        {
            "removedTargetIds": t.array(t.integer()).optional(),
            "readTime": t.string().optional(),
            "document": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentDeleteOut"])
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
    types["GoogleFirestoreAdminV1BackupIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1BackupIn"])
    types["GoogleFirestoreAdminV1BackupOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "database": t.string().optional(),
            "stats": t.proxy(renames["GoogleFirestoreAdminV1StatsOut"]).optional(),
            "state": t.string().optional(),
            "snapshotTime": t.string().optional(),
            "databaseUid": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1BackupOut"])
    types["BitSequenceIn"] = t.struct(
        {"padding": t.integer().optional(), "bitmap": t.string().optional()}
    ).named(renames["BitSequenceIn"])
    types["BitSequenceOut"] = t.struct(
        {
            "padding": t.integer().optional(),
            "bitmap": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BitSequenceOut"])
    types["FieldFilterIn"] = t.struct(
        {
            "field": t.proxy(renames["FieldReferenceIn"]).optional(),
            "op": t.string().optional(),
            "value": t.proxy(renames["ValueIn"]).optional(),
        }
    ).named(renames["FieldFilterIn"])
    types["FieldFilterOut"] = t.struct(
        {
            "field": t.proxy(renames["FieldReferenceOut"]).optional(),
            "op": t.string().optional(),
            "value": t.proxy(renames["ValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldFilterOut"])
    types["DocumentIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "fields": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["DocumentIn"])
    types["DocumentOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "fields": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentOut"])
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
    types["DocumentChangeIn"] = t.struct(
        {
            "removedTargetIds": t.array(t.integer()).optional(),
            "document": t.proxy(renames["DocumentIn"]).optional(),
            "targetIds": t.array(t.integer()).optional(),
        }
    ).named(renames["DocumentChangeIn"])
    types["DocumentChangeOut"] = t.struct(
        {
            "removedTargetIds": t.array(t.integer()).optional(),
            "document": t.proxy(renames["DocumentOut"]).optional(),
            "targetIds": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentChangeOut"])
    types["UnaryFilterIn"] = t.struct(
        {
            "field": t.proxy(renames["FieldReferenceIn"]).optional(),
            "op": t.string().optional(),
        }
    ).named(renames["UnaryFilterIn"])
    types["UnaryFilterOut"] = t.struct(
        {
            "field": t.proxy(renames["FieldReferenceOut"]).optional(),
            "op": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnaryFilterOut"])
    types["WriteResponseIn"] = t.struct(
        {
            "streamId": t.string().optional(),
            "streamToken": t.string().optional(),
            "writeResults": t.array(t.proxy(renames["WriteResultIn"])).optional(),
            "commitTime": t.string().optional(),
        }
    ).named(renames["WriteResponseIn"])
    types["WriteResponseOut"] = t.struct(
        {
            "streamId": t.string().optional(),
            "streamToken": t.string().optional(),
            "writeResults": t.array(t.proxy(renames["WriteResultOut"])).optional(),
            "commitTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteResponseOut"])
    types["DocumentsTargetIn"] = t.struct(
        {"documents": t.array(t.string()).optional()}
    ).named(renames["DocumentsTargetIn"])
    types["DocumentsTargetOut"] = t.struct(
        {
            "documents": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentsTargetOut"])
    types["GoogleFirestoreAdminV1IndexOperationMetadataIn"] = t.struct(
        {
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "index": t.string().optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexOperationMetadataIn"])
    types["GoogleFirestoreAdminV1IndexOperationMetadataOut"] = t.struct(
        {
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "index": t.string().optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexOperationMetadataOut"])
    types["DocumentMaskIn"] = t.struct(
        {"fieldPaths": t.array(t.string()).optional()}
    ).named(renames["DocumentMaskIn"])
    types["DocumentMaskOut"] = t.struct(
        {
            "fieldPaths": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentMaskOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
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
    types["ListCollectionIdsRequestIn"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "readTime": t.string().optional(),
        }
    ).named(renames["ListCollectionIdsRequestIn"])
    types["ListCollectionIdsRequestOut"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCollectionIdsRequestOut"])
    types["FieldTransformIn"] = t.struct(
        {
            "fieldPath": t.string().optional(),
            "appendMissingElements": t.proxy(renames["ArrayValueIn"]).optional(),
            "removeAllFromArray": t.proxy(renames["ArrayValueIn"]).optional(),
            "minimum": t.proxy(renames["ValueIn"]).optional(),
            "maximum": t.proxy(renames["ValueIn"]).optional(),
            "increment": t.proxy(renames["ValueIn"]).optional(),
            "setToServerValue": t.string().optional(),
        }
    ).named(renames["FieldTransformIn"])
    types["FieldTransformOut"] = t.struct(
        {
            "fieldPath": t.string().optional(),
            "appendMissingElements": t.proxy(renames["ArrayValueOut"]).optional(),
            "removeAllFromArray": t.proxy(renames["ArrayValueOut"]).optional(),
            "minimum": t.proxy(renames["ValueOut"]).optional(),
            "maximum": t.proxy(renames["ValueOut"]).optional(),
            "increment": t.proxy(renames["ValueOut"]).optional(),
            "setToServerValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldTransformOut"])
    types["ProjectionIn"] = t.struct(
        {"fields": t.array(t.proxy(renames["FieldReferenceIn"])).optional()}
    ).named(renames["ProjectionIn"])
    types["ProjectionOut"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["FieldReferenceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectionOut"])
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
    types["PartitionQueryRequestIn"] = t.struct(
        {
            "partitionCount": t.string().optional(),
            "structuredQuery": t.proxy(renames["StructuredQueryIn"]).optional(),
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "readTime": t.string().optional(),
        }
    ).named(renames["PartitionQueryRequestIn"])
    types["PartitionQueryRequestOut"] = t.struct(
        {
            "partitionCount": t.string().optional(),
            "structuredQuery": t.proxy(renames["StructuredQueryOut"]).optional(),
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionQueryRequestOut"])
    types["GoogleFirestoreAdminV1ImportDocumentsMetadataIn"] = t.struct(
        {
            "collectionIds": t.array(t.string()).optional(),
            "startTime": t.string().optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
            "operationState": t.string().optional(),
            "inputUriPrefix": t.string().optional(),
            "namespaceIds": t.array(t.string()).optional(),
            "endTime": t.string().optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ImportDocumentsMetadataIn"])
    types["GoogleFirestoreAdminV1ImportDocumentsMetadataOut"] = t.struct(
        {
            "collectionIds": t.array(t.string()).optional(),
            "startTime": t.string().optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "operationState": t.string().optional(),
            "inputUriPrefix": t.string().optional(),
            "namespaceIds": t.array(t.string()).optional(),
            "endTime": t.string().optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ImportDocumentsMetadataOut"])
    types["WriteIn"] = t.struct(
        {
            "updateMask": t.proxy(renames["DocumentMaskIn"]).optional(),
            "updateTransforms": t.array(
                t.proxy(renames["FieldTransformIn"])
            ).optional(),
            "delete": t.string().optional(),
            "transform": t.proxy(renames["DocumentTransformIn"]).optional(),
            "currentDocument": t.proxy(renames["PreconditionIn"]).optional(),
            "update": t.proxy(renames["DocumentIn"]).optional(),
        }
    ).named(renames["WriteIn"])
    types["WriteOut"] = t.struct(
        {
            "updateMask": t.proxy(renames["DocumentMaskOut"]).optional(),
            "updateTransforms": t.array(
                t.proxy(renames["FieldTransformOut"])
            ).optional(),
            "delete": t.string().optional(),
            "transform": t.proxy(renames["DocumentTransformOut"]).optional(),
            "currentDocument": t.proxy(renames["PreconditionOut"]).optional(),
            "update": t.proxy(renames["DocumentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteOut"])
    types["GoogleFirestoreAdminV1ExportDocumentsMetadataIn"] = t.struct(
        {
            "operationState": t.string().optional(),
            "outputUriPrefix": t.string().optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
            "endTime": t.string().optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
            "namespaceIds": t.array(t.string()).optional(),
            "collectionIds": t.array(t.string()).optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ExportDocumentsMetadataIn"])
    types["GoogleFirestoreAdminV1ExportDocumentsMetadataOut"] = t.struct(
        {
            "operationState": t.string().optional(),
            "outputUriPrefix": t.string().optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "endTime": t.string().optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "namespaceIds": t.array(t.string()).optional(),
            "collectionIds": t.array(t.string()).optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ExportDocumentsMetadataOut"])
    types["GoogleFirestoreAdminV1TtlConfigIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1TtlConfigIn"])
    types["GoogleFirestoreAdminV1TtlConfigOut"] = t.struct(
        {
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1TtlConfigOut"])
    types["ReadOnlyIn"] = t.struct({"readTime": t.string().optional()}).named(
        renames["ReadOnlyIn"]
    )
    types["ReadOnlyOut"] = t.struct(
        {
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadOnlyOut"])
    types["PartitionQueryResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "partitions": t.array(t.proxy(renames["CursorIn"])).optional(),
        }
    ).named(renames["PartitionQueryResponseIn"])
    types["PartitionQueryResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "partitions": t.array(t.proxy(renames["CursorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionQueryResponseOut"])
    types["TargetChangeIn"] = t.struct(
        {
            "readTime": t.string().optional(),
            "targetIds": t.array(t.integer()).optional(),
            "cause": t.proxy(renames["StatusIn"]).optional(),
            "targetChangeType": t.string().optional(),
            "resumeToken": t.string().optional(),
        }
    ).named(renames["TargetChangeIn"])
    types["TargetChangeOut"] = t.struct(
        {
            "readTime": t.string().optional(),
            "targetIds": t.array(t.integer()).optional(),
            "cause": t.proxy(renames["StatusOut"]).optional(),
            "targetChangeType": t.string().optional(),
            "resumeToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetChangeOut"])
    types["RunQueryResponseIn"] = t.struct(
        {
            "skippedResults": t.integer().optional(),
            "done": t.boolean().optional(),
            "document": t.proxy(renames["DocumentIn"]).optional(),
            "readTime": t.string().optional(),
            "transaction": t.string().optional(),
        }
    ).named(renames["RunQueryResponseIn"])
    types["RunQueryResponseOut"] = t.struct(
        {
            "skippedResults": t.integer().optional(),
            "done": t.boolean().optional(),
            "document": t.proxy(renames["DocumentOut"]).optional(),
            "readTime": t.string().optional(),
            "transaction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunQueryResponseOut"])
    types["BeginTransactionRequestIn"] = t.struct(
        {"options": t.proxy(renames["TransactionOptionsIn"]).optional()}
    ).named(renames["BeginTransactionRequestIn"])
    types["BeginTransactionRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["TransactionOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BeginTransactionRequestOut"])
    types["GoogleFirestoreAdminV1WeeklyRecurrenceIn"] = t.struct(
        {"day": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1WeeklyRecurrenceIn"])
    types["GoogleFirestoreAdminV1WeeklyRecurrenceOut"] = t.struct(
        {
            "day": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1WeeklyRecurrenceOut"])
    types["GoogleFirestoreAdminV1LocationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1LocationMetadataIn"])
    types["GoogleFirestoreAdminV1LocationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleFirestoreAdminV1LocationMetadataOut"])
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
            "weeklyRecurrence": t.proxy(
                renames["GoogleFirestoreAdminV1WeeklyRecurrenceOut"]
            ).optional(),
            "retention": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "dailyRecurrence": t.proxy(
                renames["GoogleFirestoreAdminV1DailyRecurrenceOut"]
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1BackupScheduleOut"])
    types["BatchGetDocumentsRequestIn"] = t.struct(
        {
            "documents": t.array(t.string()).optional(),
            "mask": t.proxy(renames["DocumentMaskIn"]).optional(),
            "transaction": t.string().optional(),
            "readTime": t.string().optional(),
            "newTransaction": t.proxy(renames["TransactionOptionsIn"]).optional(),
        }
    ).named(renames["BatchGetDocumentsRequestIn"])
    types["BatchGetDocumentsRequestOut"] = t.struct(
        {
            "documents": t.array(t.string()).optional(),
            "mask": t.proxy(renames["DocumentMaskOut"]).optional(),
            "transaction": t.string().optional(),
            "readTime": t.string().optional(),
            "newTransaction": t.proxy(renames["TransactionOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetDocumentsRequestOut"])
    types["GoogleFirestoreAdminV1FieldOperationMetadataIn"] = t.struct(
        {
            "state": t.string().optional(),
            "ttlConfigDelta": t.proxy(
                renames["GoogleFirestoreAdminV1TtlConfigDeltaIn"]
            ).optional(),
            "indexConfigDeltas": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexConfigDeltaIn"])
            ).optional(),
            "startTime": t.string().optional(),
            "field": t.string().optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
            "endTime": t.string().optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1FieldOperationMetadataIn"])
    types["GoogleFirestoreAdminV1FieldOperationMetadataOut"] = t.struct(
        {
            "state": t.string().optional(),
            "ttlConfigDelta": t.proxy(
                renames["GoogleFirestoreAdminV1TtlConfigDeltaOut"]
            ).optional(),
            "indexConfigDeltas": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexConfigDeltaOut"])
            ).optional(),
            "startTime": t.string().optional(),
            "field": t.string().optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "endTime": t.string().optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1FieldOperationMetadataOut"])
    types["BatchGetDocumentsResponseIn"] = t.struct(
        {
            "readTime": t.string().optional(),
            "missing": t.string().optional(),
            "transaction": t.string().optional(),
            "found": t.proxy(renames["DocumentIn"]).optional(),
        }
    ).named(renames["BatchGetDocumentsResponseIn"])
    types["BatchGetDocumentsResponseOut"] = t.struct(
        {
            "readTime": t.string().optional(),
            "missing": t.string().optional(),
            "transaction": t.string().optional(),
            "found": t.proxy(renames["DocumentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetDocumentsResponseOut"])
    types["ReadWriteIn"] = t.struct({"retryTransaction": t.string().optional()}).named(
        renames["ReadWriteIn"]
    )
    types["ReadWriteOut"] = t.struct(
        {
            "retryTransaction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadWriteOut"])
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
    types["RollbackRequestIn"] = t.struct({"transaction": t.string()}).named(
        renames["RollbackRequestIn"]
    )
    types["RollbackRequestOut"] = t.struct(
        {
            "transaction": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RollbackRequestOut"])
    types["GoogleFirestoreAdminV1ImportDocumentsRequestIn"] = t.struct(
        {
            "collectionIds": t.array(t.string()).optional(),
            "namespaceIds": t.array(t.string()).optional(),
            "inputUriPrefix": t.string().optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ImportDocumentsRequestIn"])
    types["GoogleFirestoreAdminV1ImportDocumentsRequestOut"] = t.struct(
        {
            "collectionIds": t.array(t.string()).optional(),
            "namespaceIds": t.array(t.string()).optional(),
            "inputUriPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ImportDocumentsRequestOut"])
    types["AggregationResultIn"] = t.struct(
        {"aggregateFields": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["AggregationResultIn"])
    types["AggregationResultOut"] = t.struct(
        {
            "aggregateFields": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationResultOut"])
    types["GoogleFirestoreAdminV1IndexConfigDeltaIn"] = t.struct(
        {
            "index": t.proxy(renames["GoogleFirestoreAdminV1IndexIn"]).optional(),
            "changeType": t.string().optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexConfigDeltaIn"])
    types["GoogleFirestoreAdminV1IndexConfigDeltaOut"] = t.struct(
        {
            "index": t.proxy(renames["GoogleFirestoreAdminV1IndexOut"]).optional(),
            "changeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexConfigDeltaOut"])
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
    types["GoogleFirestoreAdminV1RestoreDatabaseRequestIn"] = t.struct(
        {"databaseId": t.string(), "backup": t.string()}
    ).named(renames["GoogleFirestoreAdminV1RestoreDatabaseRequestIn"])
    types["GoogleFirestoreAdminV1RestoreDatabaseRequestOut"] = t.struct(
        {
            "databaseId": t.string(),
            "backup": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1RestoreDatabaseRequestOut"])
    types["GoogleFirestoreAdminV1ExportDocumentsResponseIn"] = t.struct(
        {"outputUriPrefix": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1ExportDocumentsResponseIn"])
    types["GoogleFirestoreAdminV1ExportDocumentsResponseOut"] = t.struct(
        {
            "outputUriPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ExportDocumentsResponseOut"])
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
    types["QueryTargetIn"] = t.struct(
        {
            "parent": t.string().optional(),
            "structuredQuery": t.proxy(renames["StructuredQueryIn"]).optional(),
        }
    ).named(renames["QueryTargetIn"])
    types["QueryTargetOut"] = t.struct(
        {
            "parent": t.string().optional(),
            "structuredQuery": t.proxy(renames["StructuredQueryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryTargetOut"])
    types["WriteRequestIn"] = t.struct(
        {
            "streamId": t.string().optional(),
            "writes": t.array(t.proxy(renames["WriteIn"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "streamToken": t.string().optional(),
        }
    ).named(renames["WriteRequestIn"])
    types["WriteRequestOut"] = t.struct(
        {
            "streamId": t.string().optional(),
            "writes": t.array(t.proxy(renames["WriteOut"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "streamToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteRequestOut"])
    types["GoogleFirestoreAdminV1DatabaseIn"] = t.struct(
        {
            "deleteProtectionState": t.string().optional(),
            "concurrencyMode": t.string().optional(),
            "appEngineIntegrationMode": t.string().optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "type": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1DatabaseIn"])
    types["GoogleFirestoreAdminV1DatabaseOut"] = t.struct(
        {
            "deleteProtectionState": t.string().optional(),
            "concurrencyMode": t.string().optional(),
            "appEngineIntegrationMode": t.string().optional(),
            "uid": t.string().optional(),
            "keyPrefix": t.string().optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "type": t.string().optional(),
            "etag": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1DatabaseOut"])
    types["GoogleFirestoreAdminV1DailyRecurrenceIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1DailyRecurrenceIn"])
    types["GoogleFirestoreAdminV1DailyRecurrenceOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleFirestoreAdminV1DailyRecurrenceOut"])
    types["ExistenceFilterIn"] = t.struct(
        {
            "unchangedNames": t.proxy(renames["BloomFilterIn"]).optional(),
            "count": t.integer().optional(),
            "targetId": t.integer().optional(),
        }
    ).named(renames["ExistenceFilterIn"])
    types["ExistenceFilterOut"] = t.struct(
        {
            "unchangedNames": t.proxy(renames["BloomFilterOut"]).optional(),
            "count": t.integer().optional(),
            "targetId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExistenceFilterOut"])
    types["GoogleFirestoreAdminV1UpdateDatabaseMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1UpdateDatabaseMetadataIn"])
    types["GoogleFirestoreAdminV1UpdateDatabaseMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleFirestoreAdminV1UpdateDatabaseMetadataOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["CountIn"] = t.struct({"upTo": t.string().optional()}).named(
        renames["CountIn"]
    )
    types["CountOut"] = t.struct(
        {
            "upTo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CountOut"])
    types["ArrayValueIn"] = t.struct(
        {"values": t.array(t.proxy(renames["ValueIn"])).optional()}
    ).named(renames["ArrayValueIn"])
    types["ArrayValueOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["ValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArrayValueOut"])
    types["StructuredQueryIn"] = t.struct(
        {
            "select": t.proxy(renames["ProjectionIn"]).optional(),
            "endAt": t.proxy(renames["CursorIn"]).optional(),
            "startAt": t.proxy(renames["CursorIn"]).optional(),
            "offset": t.integer().optional(),
            "where": t.proxy(renames["FilterIn"]).optional(),
            "from": t.array(t.proxy(renames["CollectionSelectorIn"])).optional(),
            "limit": t.integer().optional(),
            "orderBy": t.array(t.proxy(renames["OrderIn"])).optional(),
        }
    ).named(renames["StructuredQueryIn"])
    types["StructuredQueryOut"] = t.struct(
        {
            "select": t.proxy(renames["ProjectionOut"]).optional(),
            "endAt": t.proxy(renames["CursorOut"]).optional(),
            "startAt": t.proxy(renames["CursorOut"]).optional(),
            "offset": t.integer().optional(),
            "where": t.proxy(renames["FilterOut"]).optional(),
            "from": t.array(t.proxy(renames["CollectionSelectorOut"])).optional(),
            "limit": t.integer().optional(),
            "orderBy": t.array(t.proxy(renames["OrderOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructuredQueryOut"])
    types["GoogleFirestoreAdminV1StatsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1StatsIn"])
    types["GoogleFirestoreAdminV1StatsOut"] = t.struct(
        {
            "indexCount": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "documentCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1StatsOut"])
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
    types["DocumentTransformIn"] = t.struct(
        {
            "fieldTransforms": t.array(t.proxy(renames["FieldTransformIn"])).optional(),
            "document": t.string().optional(),
        }
    ).named(renames["DocumentTransformIn"])
    types["DocumentTransformOut"] = t.struct(
        {
            "fieldTransforms": t.array(
                t.proxy(renames["FieldTransformOut"])
            ).optional(),
            "document": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentTransformOut"])
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
    types["ListenRequestIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "addTarget": t.proxy(renames["TargetIn"]).optional(),
            "removeTarget": t.integer().optional(),
        }
    ).named(renames["ListenRequestIn"])
    types["ListenRequestOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "addTarget": t.proxy(renames["TargetOut"]).optional(),
            "removeTarget": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListenRequestOut"])
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
    types["ValueIn"] = t.struct(
        {
            "arrayValue": t.proxy(renames["ArrayValueIn"]).optional(),
            "geoPointValue": t.proxy(renames["LatLngIn"]).optional(),
            "stringValue": t.string().optional(),
            "referenceValue": t.string().optional(),
            "mapValue": t.proxy(renames["MapValueIn"]).optional(),
            "timestampValue": t.string().optional(),
            "doubleValue": t.number().optional(),
            "integerValue": t.string().optional(),
            "booleanValue": t.boolean().optional(),
            "nullValue": t.string().optional(),
            "bytesValue": t.string().optional(),
        }
    ).named(renames["ValueIn"])
    types["ValueOut"] = t.struct(
        {
            "arrayValue": t.proxy(renames["ArrayValueOut"]).optional(),
            "geoPointValue": t.proxy(renames["LatLngOut"]).optional(),
            "stringValue": t.string().optional(),
            "referenceValue": t.string().optional(),
            "mapValue": t.proxy(renames["MapValueOut"]).optional(),
            "timestampValue": t.string().optional(),
            "doubleValue": t.number().optional(),
            "integerValue": t.string().optional(),
            "booleanValue": t.boolean().optional(),
            "nullValue": t.string().optional(),
            "bytesValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueOut"])
    types["MapValueIn"] = t.struct(
        {"fields": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["MapValueIn"])
    types["MapValueOut"] = t.struct(
        {
            "fields": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MapValueOut"])
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

    functions = {}
    functions["projectsLocationsGet"] = firestore.get(
        "v1/{name}/locations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupsList"] = firestore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirestoreAdminV1BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupsDelete"] = firestore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirestoreAdminV1BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupsGet"] = firestore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirestoreAdminV1BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesRestore"] = firestore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirestoreAdminV1DatabaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesPatch"] = firestore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirestoreAdminV1DatabaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesExportDocuments"] = firestore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirestoreAdminV1DatabaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesList"] = firestore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirestoreAdminV1DatabaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesCreate"] = firestore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirestoreAdminV1DatabaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDelete"] = firestore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirestoreAdminV1DatabaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesImportDocuments"] = firestore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirestoreAdminV1DatabaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesGet"] = firestore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirestoreAdminV1DatabaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesOperationsList"] = firestore.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesOperationsGet"] = firestore.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesOperationsCancel"] = firestore.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesOperationsDelete"] = firestore.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesBackupSchedulesDelete"] = firestore.post(
        "v1/{parent}/backupSchedules",
        t.struct(
            {
                "parent": t.string(),
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
    functions["projectsDatabasesBackupSchedulesList"] = firestore.post(
        "v1/{parent}/backupSchedules",
        t.struct(
            {
                "parent": t.string(),
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
    functions["projectsDatabasesBackupSchedulesPatch"] = firestore.post(
        "v1/{parent}/backupSchedules",
        t.struct(
            {
                "parent": t.string(),
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
    functions["projectsDatabasesBackupSchedulesGet"] = firestore.post(
        "v1/{parent}/backupSchedules",
        t.struct(
            {
                "parent": t.string(),
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
    functions["projectsDatabasesBackupSchedulesCreate"] = firestore.post(
        "v1/{parent}/backupSchedules",
        t.struct(
            {
                "parent": t.string(),
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
    functions["projectsDatabasesCollectionGroupsFieldsPatch"] = firestore.get(
        "v1/{parent}/fields",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirestoreAdminV1ListFieldsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesCollectionGroupsFieldsGet"] = firestore.get(
        "v1/{parent}/fields",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirestoreAdminV1ListFieldsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesCollectionGroupsFieldsList"] = firestore.get(
        "v1/{parent}/fields",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirestoreAdminV1ListFieldsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesCollectionGroupsIndexesGet"] = firestore.post(
        "v1/{parent}/indexes",
        t.struct(
            {
                "parent": t.string(),
                "apiScope": t.string().optional(),
                "queryScope": t.string().optional(),
                "name": t.string().optional(),
                "state": t.string().optional(),
                "fields": t.array(
                    t.proxy(renames["GoogleFirestoreAdminV1IndexFieldIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesCollectionGroupsIndexesList"] = firestore.post(
        "v1/{parent}/indexes",
        t.struct(
            {
                "parent": t.string(),
                "apiScope": t.string().optional(),
                "queryScope": t.string().optional(),
                "name": t.string().optional(),
                "state": t.string().optional(),
                "fields": t.array(
                    t.proxy(renames["GoogleFirestoreAdminV1IndexFieldIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesCollectionGroupsIndexesDelete"] = firestore.post(
        "v1/{parent}/indexes",
        t.struct(
            {
                "parent": t.string(),
                "apiScope": t.string().optional(),
                "queryScope": t.string().optional(),
                "name": t.string().optional(),
                "state": t.string().optional(),
                "fields": t.array(
                    t.proxy(renames["GoogleFirestoreAdminV1IndexFieldIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesCollectionGroupsIndexesCreate"] = firestore.post(
        "v1/{parent}/indexes",
        t.struct(
            {
                "parent": t.string(),
                "apiScope": t.string().optional(),
                "queryScope": t.string().optional(),
                "name": t.string().optional(),
                "state": t.string().optional(),
                "fields": t.array(
                    t.proxy(renames["GoogleFirestoreAdminV1IndexFieldIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsDelete"] = firestore.post(
        "v1/{parent}:listCollectionIds",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "readTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCollectionIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsPatch"] = firestore.post(
        "v1/{parent}:listCollectionIds",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "readTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCollectionIdsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="firestore",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
