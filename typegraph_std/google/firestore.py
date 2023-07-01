from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_firestore():
    firestore = HTTPRuntime("https://firestore.googleapis.com/")

    renames = {
        "ErrorResponse": "_firestore_1_ErrorResponse",
        "GoogleFirestoreAdminV1ListIndexesResponseIn": "_firestore_2_GoogleFirestoreAdminV1ListIndexesResponseIn",
        "GoogleFirestoreAdminV1ListIndexesResponseOut": "_firestore_3_GoogleFirestoreAdminV1ListIndexesResponseOut",
        "PartitionQueryRequestIn": "_firestore_4_PartitionQueryRequestIn",
        "PartitionQueryRequestOut": "_firestore_5_PartitionQueryRequestOut",
        "TargetChangeIn": "_firestore_6_TargetChangeIn",
        "TargetChangeOut": "_firestore_7_TargetChangeOut",
        "GoogleFirestoreAdminV1ListDatabasesResponseIn": "_firestore_8_GoogleFirestoreAdminV1ListDatabasesResponseIn",
        "GoogleFirestoreAdminV1ListDatabasesResponseOut": "_firestore_9_GoogleFirestoreAdminV1ListDatabasesResponseOut",
        "GoogleFirestoreAdminV1ImportDocumentsMetadataIn": "_firestore_10_GoogleFirestoreAdminV1ImportDocumentsMetadataIn",
        "GoogleFirestoreAdminV1ImportDocumentsMetadataOut": "_firestore_11_GoogleFirestoreAdminV1ImportDocumentsMetadataOut",
        "CountIn": "_firestore_12_CountIn",
        "CountOut": "_firestore_13_CountOut",
        "GoogleFirestoreAdminV1ListFieldsResponseIn": "_firestore_14_GoogleFirestoreAdminV1ListFieldsResponseIn",
        "GoogleFirestoreAdminV1ListFieldsResponseOut": "_firestore_15_GoogleFirestoreAdminV1ListFieldsResponseOut",
        "GoogleFirestoreAdminV1ListBackupsResponseIn": "_firestore_16_GoogleFirestoreAdminV1ListBackupsResponseIn",
        "GoogleFirestoreAdminV1ListBackupsResponseOut": "_firestore_17_GoogleFirestoreAdminV1ListBackupsResponseOut",
        "BitSequenceIn": "_firestore_18_BitSequenceIn",
        "BitSequenceOut": "_firestore_19_BitSequenceOut",
        "CommitResponseIn": "_firestore_20_CommitResponseIn",
        "CommitResponseOut": "_firestore_21_CommitResponseOut",
        "ValueIn": "_firestore_22_ValueIn",
        "ValueOut": "_firestore_23_ValueOut",
        "ListenRequestIn": "_firestore_24_ListenRequestIn",
        "ListenRequestOut": "_firestore_25_ListenRequestOut",
        "GoogleFirestoreAdminV1StatsIn": "_firestore_26_GoogleFirestoreAdminV1StatsIn",
        "GoogleFirestoreAdminV1StatsOut": "_firestore_27_GoogleFirestoreAdminV1StatsOut",
        "GoogleFirestoreAdminV1ListBackupSchedulesResponseIn": "_firestore_28_GoogleFirestoreAdminV1ListBackupSchedulesResponseIn",
        "GoogleFirestoreAdminV1ListBackupSchedulesResponseOut": "_firestore_29_GoogleFirestoreAdminV1ListBackupSchedulesResponseOut",
        "GoogleFirestoreAdminV1IndexIn": "_firestore_30_GoogleFirestoreAdminV1IndexIn",
        "GoogleFirestoreAdminV1IndexOut": "_firestore_31_GoogleFirestoreAdminV1IndexOut",
        "StructuredAggregationQueryIn": "_firestore_32_StructuredAggregationQueryIn",
        "StructuredAggregationQueryOut": "_firestore_33_StructuredAggregationQueryOut",
        "FieldTransformIn": "_firestore_34_FieldTransformIn",
        "FieldTransformOut": "_firestore_35_FieldTransformOut",
        "GoogleFirestoreAdminV1ProgressIn": "_firestore_36_GoogleFirestoreAdminV1ProgressIn",
        "GoogleFirestoreAdminV1ProgressOut": "_firestore_37_GoogleFirestoreAdminV1ProgressOut",
        "GoogleFirestoreAdminV1LocationMetadataIn": "_firestore_38_GoogleFirestoreAdminV1LocationMetadataIn",
        "GoogleFirestoreAdminV1LocationMetadataOut": "_firestore_39_GoogleFirestoreAdminV1LocationMetadataOut",
        "AggregationResultIn": "_firestore_40_AggregationResultIn",
        "AggregationResultOut": "_firestore_41_AggregationResultOut",
        "ListCollectionIdsResponseIn": "_firestore_42_ListCollectionIdsResponseIn",
        "ListCollectionIdsResponseOut": "_firestore_43_ListCollectionIdsResponseOut",
        "ListenResponseIn": "_firestore_44_ListenResponseIn",
        "ListenResponseOut": "_firestore_45_ListenResponseOut",
        "ReadWriteIn": "_firestore_46_ReadWriteIn",
        "ReadWriteOut": "_firestore_47_ReadWriteOut",
        "RollbackRequestIn": "_firestore_48_RollbackRequestIn",
        "RollbackRequestOut": "_firestore_49_RollbackRequestOut",
        "TargetIn": "_firestore_50_TargetIn",
        "TargetOut": "_firestore_51_TargetOut",
        "CommitRequestIn": "_firestore_52_CommitRequestIn",
        "CommitRequestOut": "_firestore_53_CommitRequestOut",
        "GoogleLongrunningOperationIn": "_firestore_54_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_firestore_55_GoogleLongrunningOperationOut",
        "ListDocumentsResponseIn": "_firestore_56_ListDocumentsResponseIn",
        "ListDocumentsResponseOut": "_firestore_57_ListDocumentsResponseOut",
        "GoogleFirestoreAdminV1IndexConfigDeltaIn": "_firestore_58_GoogleFirestoreAdminV1IndexConfigDeltaIn",
        "GoogleFirestoreAdminV1IndexConfigDeltaOut": "_firestore_59_GoogleFirestoreAdminV1IndexConfigDeltaOut",
        "GoogleFirestoreAdminV1FieldOperationMetadataIn": "_firestore_60_GoogleFirestoreAdminV1FieldOperationMetadataIn",
        "GoogleFirestoreAdminV1FieldOperationMetadataOut": "_firestore_61_GoogleFirestoreAdminV1FieldOperationMetadataOut",
        "GoogleFirestoreAdminV1BackupIn": "_firestore_62_GoogleFirestoreAdminV1BackupIn",
        "GoogleFirestoreAdminV1BackupOut": "_firestore_63_GoogleFirestoreAdminV1BackupOut",
        "CollectionSelectorIn": "_firestore_64_CollectionSelectorIn",
        "CollectionSelectorOut": "_firestore_65_CollectionSelectorOut",
        "GoogleFirestoreAdminV1TtlConfigDeltaIn": "_firestore_66_GoogleFirestoreAdminV1TtlConfigDeltaIn",
        "GoogleFirestoreAdminV1TtlConfigDeltaOut": "_firestore_67_GoogleFirestoreAdminV1TtlConfigDeltaOut",
        "BatchGetDocumentsResponseIn": "_firestore_68_BatchGetDocumentsResponseIn",
        "BatchGetDocumentsResponseOut": "_firestore_69_BatchGetDocumentsResponseOut",
        "MapValueIn": "_firestore_70_MapValueIn",
        "MapValueOut": "_firestore_71_MapValueOut",
        "WriteResponseIn": "_firestore_72_WriteResponseIn",
        "WriteResponseOut": "_firestore_73_WriteResponseOut",
        "GoogleFirestoreAdminV1TtlConfigIn": "_firestore_74_GoogleFirestoreAdminV1TtlConfigIn",
        "GoogleFirestoreAdminV1TtlConfigOut": "_firestore_75_GoogleFirestoreAdminV1TtlConfigOut",
        "UnaryFilterIn": "_firestore_76_UnaryFilterIn",
        "UnaryFilterOut": "_firestore_77_UnaryFilterOut",
        "OrderIn": "_firestore_78_OrderIn",
        "OrderOut": "_firestore_79_OrderOut",
        "DocumentMaskIn": "_firestore_80_DocumentMaskIn",
        "DocumentMaskOut": "_firestore_81_DocumentMaskOut",
        "QueryTargetIn": "_firestore_82_QueryTargetIn",
        "QueryTargetOut": "_firestore_83_QueryTargetOut",
        "FilterIn": "_firestore_84_FilterIn",
        "FilterOut": "_firestore_85_FilterOut",
        "GoogleFirestoreAdminV1DatabaseIn": "_firestore_86_GoogleFirestoreAdminV1DatabaseIn",
        "GoogleFirestoreAdminV1DatabaseOut": "_firestore_87_GoogleFirestoreAdminV1DatabaseOut",
        "WriteRequestIn": "_firestore_88_WriteRequestIn",
        "WriteRequestOut": "_firestore_89_WriteRequestOut",
        "CompositeFilterIn": "_firestore_90_CompositeFilterIn",
        "CompositeFilterOut": "_firestore_91_CompositeFilterOut",
        "ProjectionIn": "_firestore_92_ProjectionIn",
        "ProjectionOut": "_firestore_93_ProjectionOut",
        "DocumentsTargetIn": "_firestore_94_DocumentsTargetIn",
        "DocumentsTargetOut": "_firestore_95_DocumentsTargetOut",
        "GoogleFirestoreAdminV1WeeklyRecurrenceIn": "_firestore_96_GoogleFirestoreAdminV1WeeklyRecurrenceIn",
        "GoogleFirestoreAdminV1WeeklyRecurrenceOut": "_firestore_97_GoogleFirestoreAdminV1WeeklyRecurrenceOut",
        "LocationIn": "_firestore_98_LocationIn",
        "LocationOut": "_firestore_99_LocationOut",
        "TransactionOptionsIn": "_firestore_100_TransactionOptionsIn",
        "TransactionOptionsOut": "_firestore_101_TransactionOptionsOut",
        "PreconditionIn": "_firestore_102_PreconditionIn",
        "PreconditionOut": "_firestore_103_PreconditionOut",
        "BeginTransactionRequestIn": "_firestore_104_BeginTransactionRequestIn",
        "BeginTransactionRequestOut": "_firestore_105_BeginTransactionRequestOut",
        "RunAggregationQueryResponseIn": "_firestore_106_RunAggregationQueryResponseIn",
        "RunAggregationQueryResponseOut": "_firestore_107_RunAggregationQueryResponseOut",
        "FieldReferenceIn": "_firestore_108_FieldReferenceIn",
        "FieldReferenceOut": "_firestore_109_FieldReferenceOut",
        "GoogleFirestoreAdminV1IndexConfigIn": "_firestore_110_GoogleFirestoreAdminV1IndexConfigIn",
        "GoogleFirestoreAdminV1IndexConfigOut": "_firestore_111_GoogleFirestoreAdminV1IndexConfigOut",
        "WriteIn": "_firestore_112_WriteIn",
        "WriteOut": "_firestore_113_WriteOut",
        "WriteResultIn": "_firestore_114_WriteResultIn",
        "WriteResultOut": "_firestore_115_WriteResultOut",
        "DocumentChangeIn": "_firestore_116_DocumentChangeIn",
        "DocumentChangeOut": "_firestore_117_DocumentChangeOut",
        "GoogleLongrunningCancelOperationRequestIn": "_firestore_118_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_firestore_119_GoogleLongrunningCancelOperationRequestOut",
        "BatchWriteResponseIn": "_firestore_120_BatchWriteResponseIn",
        "BatchWriteResponseOut": "_firestore_121_BatchWriteResponseOut",
        "DocumentIn": "_firestore_122_DocumentIn",
        "DocumentOut": "_firestore_123_DocumentOut",
        "GoogleLongrunningListOperationsResponseIn": "_firestore_124_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_firestore_125_GoogleLongrunningListOperationsResponseOut",
        "GoogleFirestoreAdminV1ExportDocumentsRequestIn": "_firestore_126_GoogleFirestoreAdminV1ExportDocumentsRequestIn",
        "GoogleFirestoreAdminV1ExportDocumentsRequestOut": "_firestore_127_GoogleFirestoreAdminV1ExportDocumentsRequestOut",
        "FieldFilterIn": "_firestore_128_FieldFilterIn",
        "FieldFilterOut": "_firestore_129_FieldFilterOut",
        "ReadOnlyIn": "_firestore_130_ReadOnlyIn",
        "ReadOnlyOut": "_firestore_131_ReadOnlyOut",
        "GoogleFirestoreAdminV1ImportDocumentsRequestIn": "_firestore_132_GoogleFirestoreAdminV1ImportDocumentsRequestIn",
        "GoogleFirestoreAdminV1ImportDocumentsRequestOut": "_firestore_133_GoogleFirestoreAdminV1ImportDocumentsRequestOut",
        "PartitionQueryResponseIn": "_firestore_134_PartitionQueryResponseIn",
        "PartitionQueryResponseOut": "_firestore_135_PartitionQueryResponseOut",
        "GoogleFirestoreAdminV1FieldIn": "_firestore_136_GoogleFirestoreAdminV1FieldIn",
        "GoogleFirestoreAdminV1FieldOut": "_firestore_137_GoogleFirestoreAdminV1FieldOut",
        "DocumentRemoveIn": "_firestore_138_DocumentRemoveIn",
        "DocumentRemoveOut": "_firestore_139_DocumentRemoveOut",
        "DocumentDeleteIn": "_firestore_140_DocumentDeleteIn",
        "DocumentDeleteOut": "_firestore_141_DocumentDeleteOut",
        "ExistenceFilterIn": "_firestore_142_ExistenceFilterIn",
        "ExistenceFilterOut": "_firestore_143_ExistenceFilterOut",
        "GoogleFirestoreAdminV1IndexFieldIn": "_firestore_144_GoogleFirestoreAdminV1IndexFieldIn",
        "GoogleFirestoreAdminV1IndexFieldOut": "_firestore_145_GoogleFirestoreAdminV1IndexFieldOut",
        "GoogleFirestoreAdminV1UpdateDatabaseMetadataIn": "_firestore_146_GoogleFirestoreAdminV1UpdateDatabaseMetadataIn",
        "GoogleFirestoreAdminV1UpdateDatabaseMetadataOut": "_firestore_147_GoogleFirestoreAdminV1UpdateDatabaseMetadataOut",
        "RunQueryResponseIn": "_firestore_148_RunQueryResponseIn",
        "RunQueryResponseOut": "_firestore_149_RunQueryResponseOut",
        "GoogleFirestoreAdminV1RestoreDatabaseRequestIn": "_firestore_150_GoogleFirestoreAdminV1RestoreDatabaseRequestIn",
        "GoogleFirestoreAdminV1RestoreDatabaseRequestOut": "_firestore_151_GoogleFirestoreAdminV1RestoreDatabaseRequestOut",
        "ListCollectionIdsRequestIn": "_firestore_152_ListCollectionIdsRequestIn",
        "ListCollectionIdsRequestOut": "_firestore_153_ListCollectionIdsRequestOut",
        "StatusIn": "_firestore_154_StatusIn",
        "StatusOut": "_firestore_155_StatusOut",
        "LatLngIn": "_firestore_156_LatLngIn",
        "LatLngOut": "_firestore_157_LatLngOut",
        "RunQueryRequestIn": "_firestore_158_RunQueryRequestIn",
        "RunQueryRequestOut": "_firestore_159_RunQueryRequestOut",
        "EmptyIn": "_firestore_160_EmptyIn",
        "EmptyOut": "_firestore_161_EmptyOut",
        "DocumentTransformIn": "_firestore_162_DocumentTransformIn",
        "DocumentTransformOut": "_firestore_163_DocumentTransformOut",
        "GoogleFirestoreAdminV1ExportDocumentsResponseIn": "_firestore_164_GoogleFirestoreAdminV1ExportDocumentsResponseIn",
        "GoogleFirestoreAdminV1ExportDocumentsResponseOut": "_firestore_165_GoogleFirestoreAdminV1ExportDocumentsResponseOut",
        "ListLocationsResponseIn": "_firestore_166_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_firestore_167_ListLocationsResponseOut",
        "BatchGetDocumentsRequestIn": "_firestore_168_BatchGetDocumentsRequestIn",
        "BatchGetDocumentsRequestOut": "_firestore_169_BatchGetDocumentsRequestOut",
        "ArrayValueIn": "_firestore_170_ArrayValueIn",
        "ArrayValueOut": "_firestore_171_ArrayValueOut",
        "RunAggregationQueryRequestIn": "_firestore_172_RunAggregationQueryRequestIn",
        "RunAggregationQueryRequestOut": "_firestore_173_RunAggregationQueryRequestOut",
        "GoogleFirestoreAdminV1DailyRecurrenceIn": "_firestore_174_GoogleFirestoreAdminV1DailyRecurrenceIn",
        "GoogleFirestoreAdminV1DailyRecurrenceOut": "_firestore_175_GoogleFirestoreAdminV1DailyRecurrenceOut",
        "StructuredQueryIn": "_firestore_176_StructuredQueryIn",
        "StructuredQueryOut": "_firestore_177_StructuredQueryOut",
        "GoogleFirestoreAdminV1IndexOperationMetadataIn": "_firestore_178_GoogleFirestoreAdminV1IndexOperationMetadataIn",
        "GoogleFirestoreAdminV1IndexOperationMetadataOut": "_firestore_179_GoogleFirestoreAdminV1IndexOperationMetadataOut",
        "AggregationIn": "_firestore_180_AggregationIn",
        "AggregationOut": "_firestore_181_AggregationOut",
        "GoogleFirestoreAdminV1ExportDocumentsMetadataIn": "_firestore_182_GoogleFirestoreAdminV1ExportDocumentsMetadataIn",
        "GoogleFirestoreAdminV1ExportDocumentsMetadataOut": "_firestore_183_GoogleFirestoreAdminV1ExportDocumentsMetadataOut",
        "BeginTransactionResponseIn": "_firestore_184_BeginTransactionResponseIn",
        "BeginTransactionResponseOut": "_firestore_185_BeginTransactionResponseOut",
        "BloomFilterIn": "_firestore_186_BloomFilterIn",
        "BloomFilterOut": "_firestore_187_BloomFilterOut",
        "GoogleFirestoreAdminV1BackupScheduleIn": "_firestore_188_GoogleFirestoreAdminV1BackupScheduleIn",
        "GoogleFirestoreAdminV1BackupScheduleOut": "_firestore_189_GoogleFirestoreAdminV1BackupScheduleOut",
        "CursorIn": "_firestore_190_CursorIn",
        "CursorOut": "_firestore_191_CursorOut",
        "GoogleFirestoreAdminV1RestoreDatabaseMetadataIn": "_firestore_192_GoogleFirestoreAdminV1RestoreDatabaseMetadataIn",
        "GoogleFirestoreAdminV1RestoreDatabaseMetadataOut": "_firestore_193_GoogleFirestoreAdminV1RestoreDatabaseMetadataOut",
        "BatchWriteRequestIn": "_firestore_194_BatchWriteRequestIn",
        "BatchWriteRequestOut": "_firestore_195_BatchWriteRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["PartitionQueryRequestIn"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "readTime": t.string().optional(),
            "pageSize": t.integer().optional(),
            "partitionCount": t.string().optional(),
            "structuredQuery": t.proxy(renames["StructuredQueryIn"]).optional(),
        }
    ).named(renames["PartitionQueryRequestIn"])
    types["PartitionQueryRequestOut"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "readTime": t.string().optional(),
            "pageSize": t.integer().optional(),
            "partitionCount": t.string().optional(),
            "structuredQuery": t.proxy(renames["StructuredQueryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionQueryRequestOut"])
    types["TargetChangeIn"] = t.struct(
        {
            "cause": t.proxy(renames["StatusIn"]).optional(),
            "targetChangeType": t.string().optional(),
            "readTime": t.string().optional(),
            "targetIds": t.array(t.integer()).optional(),
            "resumeToken": t.string().optional(),
        }
    ).named(renames["TargetChangeIn"])
    types["TargetChangeOut"] = t.struct(
        {
            "cause": t.proxy(renames["StatusOut"]).optional(),
            "targetChangeType": t.string().optional(),
            "readTime": t.string().optional(),
            "targetIds": t.array(t.integer()).optional(),
            "resumeToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetChangeOut"])
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
    types["GoogleFirestoreAdminV1ImportDocumentsMetadataIn"] = t.struct(
        {
            "namespaceIds": t.array(t.string()).optional(),
            "operationState": t.string().optional(),
            "endTime": t.string().optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
            "startTime": t.string().optional(),
            "collectionIds": t.array(t.string()).optional(),
            "inputUriPrefix": t.string().optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ImportDocumentsMetadataIn"])
    types["GoogleFirestoreAdminV1ImportDocumentsMetadataOut"] = t.struct(
        {
            "namespaceIds": t.array(t.string()).optional(),
            "operationState": t.string().optional(),
            "endTime": t.string().optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "collectionIds": t.array(t.string()).optional(),
            "inputUriPrefix": t.string().optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ImportDocumentsMetadataOut"])
    types["CountIn"] = t.struct({"upTo": t.string().optional()}).named(
        renames["CountIn"]
    )
    types["CountOut"] = t.struct(
        {
            "upTo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CountOut"])
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
    types["ValueIn"] = t.struct(
        {
            "booleanValue": t.boolean().optional(),
            "stringValue": t.string().optional(),
            "arrayValue": t.proxy(renames["ArrayValueIn"]).optional(),
            "bytesValue": t.string().optional(),
            "integerValue": t.string().optional(),
            "mapValue": t.proxy(renames["MapValueIn"]).optional(),
            "referenceValue": t.string().optional(),
            "geoPointValue": t.proxy(renames["LatLngIn"]).optional(),
            "nullValue": t.string().optional(),
            "doubleValue": t.number().optional(),
            "timestampValue": t.string().optional(),
        }
    ).named(renames["ValueIn"])
    types["ValueOut"] = t.struct(
        {
            "booleanValue": t.boolean().optional(),
            "stringValue": t.string().optional(),
            "arrayValue": t.proxy(renames["ArrayValueOut"]).optional(),
            "bytesValue": t.string().optional(),
            "integerValue": t.string().optional(),
            "mapValue": t.proxy(renames["MapValueOut"]).optional(),
            "referenceValue": t.string().optional(),
            "geoPointValue": t.proxy(renames["LatLngOut"]).optional(),
            "nullValue": t.string().optional(),
            "doubleValue": t.number().optional(),
            "timestampValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueOut"])
    types["ListenRequestIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "removeTarget": t.integer().optional(),
            "addTarget": t.proxy(renames["TargetIn"]).optional(),
        }
    ).named(renames["ListenRequestIn"])
    types["ListenRequestOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "removeTarget": t.integer().optional(),
            "addTarget": t.proxy(renames["TargetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListenRequestOut"])
    types["GoogleFirestoreAdminV1StatsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1StatsIn"])
    types["GoogleFirestoreAdminV1StatsOut"] = t.struct(
        {
            "sizeBytes": t.string().optional(),
            "indexCount": t.string().optional(),
            "documentCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1StatsOut"])
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
    types["GoogleFirestoreAdminV1IndexIn"] = t.struct(
        {
            "name": t.string().optional(),
            "queryScope": t.string().optional(),
            "apiScope": t.string().optional(),
            "state": t.string().optional(),
            "fields": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexFieldIn"])
            ).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexIn"])
    types["GoogleFirestoreAdminV1IndexOut"] = t.struct(
        {
            "name": t.string().optional(),
            "queryScope": t.string().optional(),
            "apiScope": t.string().optional(),
            "state": t.string().optional(),
            "fields": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexFieldOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexOut"])
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
    types["FieldTransformIn"] = t.struct(
        {
            "fieldPath": t.string().optional(),
            "appendMissingElements": t.proxy(renames["ArrayValueIn"]).optional(),
            "setToServerValue": t.string().optional(),
            "removeAllFromArray": t.proxy(renames["ArrayValueIn"]).optional(),
            "maximum": t.proxy(renames["ValueIn"]).optional(),
            "minimum": t.proxy(renames["ValueIn"]).optional(),
            "increment": t.proxy(renames["ValueIn"]).optional(),
        }
    ).named(renames["FieldTransformIn"])
    types["FieldTransformOut"] = t.struct(
        {
            "fieldPath": t.string().optional(),
            "appendMissingElements": t.proxy(renames["ArrayValueOut"]).optional(),
            "setToServerValue": t.string().optional(),
            "removeAllFromArray": t.proxy(renames["ArrayValueOut"]).optional(),
            "maximum": t.proxy(renames["ValueOut"]).optional(),
            "minimum": t.proxy(renames["ValueOut"]).optional(),
            "increment": t.proxy(renames["ValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldTransformOut"])
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
    types["GoogleFirestoreAdminV1LocationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1LocationMetadataIn"])
    types["GoogleFirestoreAdminV1LocationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleFirestoreAdminV1LocationMetadataOut"])
    types["AggregationResultIn"] = t.struct(
        {"aggregateFields": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["AggregationResultIn"])
    types["AggregationResultOut"] = t.struct(
        {
            "aggregateFields": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationResultOut"])
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
    types["ListenResponseIn"] = t.struct(
        {
            "documentChange": t.proxy(renames["DocumentChangeIn"]).optional(),
            "documentDelete": t.proxy(renames["DocumentDeleteIn"]).optional(),
            "documentRemove": t.proxy(renames["DocumentRemoveIn"]).optional(),
            "targetChange": t.proxy(renames["TargetChangeIn"]).optional(),
            "filter": t.proxy(renames["ExistenceFilterIn"]).optional(),
        }
    ).named(renames["ListenResponseIn"])
    types["ListenResponseOut"] = t.struct(
        {
            "documentChange": t.proxy(renames["DocumentChangeOut"]).optional(),
            "documentDelete": t.proxy(renames["DocumentDeleteOut"]).optional(),
            "documentRemove": t.proxy(renames["DocumentRemoveOut"]).optional(),
            "targetChange": t.proxy(renames["TargetChangeOut"]).optional(),
            "filter": t.proxy(renames["ExistenceFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListenResponseOut"])
    types["ReadWriteIn"] = t.struct({"retryTransaction": t.string().optional()}).named(
        renames["ReadWriteIn"]
    )
    types["ReadWriteOut"] = t.struct(
        {
            "retryTransaction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadWriteOut"])
    types["RollbackRequestIn"] = t.struct({"transaction": t.string()}).named(
        renames["RollbackRequestIn"]
    )
    types["RollbackRequestOut"] = t.struct(
        {
            "transaction": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RollbackRequestOut"])
    types["TargetIn"] = t.struct(
        {
            "documents": t.proxy(renames["DocumentsTargetIn"]).optional(),
            "query": t.proxy(renames["QueryTargetIn"]).optional(),
            "resumeToken": t.string().optional(),
            "once": t.boolean().optional(),
            "readTime": t.string().optional(),
            "targetId": t.integer().optional(),
            "expectedCount": t.integer().optional(),
        }
    ).named(renames["TargetIn"])
    types["TargetOut"] = t.struct(
        {
            "documents": t.proxy(renames["DocumentsTargetOut"]).optional(),
            "query": t.proxy(renames["QueryTargetOut"]).optional(),
            "resumeToken": t.string().optional(),
            "once": t.boolean().optional(),
            "readTime": t.string().optional(),
            "targetId": t.integer().optional(),
            "expectedCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetOut"])
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
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["ListDocumentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "documents": t.array(t.proxy(renames["DocumentIn"])).optional(),
        }
    ).named(renames["ListDocumentsResponseIn"])
    types["ListDocumentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "documents": t.array(t.proxy(renames["DocumentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDocumentsResponseOut"])
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
    types["GoogleFirestoreAdminV1FieldOperationMetadataIn"] = t.struct(
        {
            "state": t.string().optional(),
            "indexConfigDeltas": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexConfigDeltaIn"])
            ).optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "ttlConfigDelta": t.proxy(
                renames["GoogleFirestoreAdminV1TtlConfigDeltaIn"]
            ).optional(),
            "field": t.string().optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1FieldOperationMetadataIn"])
    types["GoogleFirestoreAdminV1FieldOperationMetadataOut"] = t.struct(
        {
            "state": t.string().optional(),
            "indexConfigDeltas": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexConfigDeltaOut"])
            ).optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "ttlConfigDelta": t.proxy(
                renames["GoogleFirestoreAdminV1TtlConfigDeltaOut"]
            ).optional(),
            "field": t.string().optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1FieldOperationMetadataOut"])
    types["GoogleFirestoreAdminV1BackupIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1BackupIn"])
    types["GoogleFirestoreAdminV1BackupOut"] = t.struct(
        {
            "state": t.string().optional(),
            "expireTime": t.string().optional(),
            "databaseUid": t.string().optional(),
            "name": t.string().optional(),
            "snapshotTime": t.string().optional(),
            "database": t.string().optional(),
            "stats": t.proxy(renames["GoogleFirestoreAdminV1StatsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1BackupOut"])
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
    types["GoogleFirestoreAdminV1TtlConfigDeltaIn"] = t.struct(
        {"changeType": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1TtlConfigDeltaIn"])
    types["GoogleFirestoreAdminV1TtlConfigDeltaOut"] = t.struct(
        {
            "changeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1TtlConfigDeltaOut"])
    types["BatchGetDocumentsResponseIn"] = t.struct(
        {
            "transaction": t.string().optional(),
            "found": t.proxy(renames["DocumentIn"]).optional(),
            "readTime": t.string().optional(),
            "missing": t.string().optional(),
        }
    ).named(renames["BatchGetDocumentsResponseIn"])
    types["BatchGetDocumentsResponseOut"] = t.struct(
        {
            "transaction": t.string().optional(),
            "found": t.proxy(renames["DocumentOut"]).optional(),
            "readTime": t.string().optional(),
            "missing": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetDocumentsResponseOut"])
    types["MapValueIn"] = t.struct(
        {"fields": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["MapValueIn"])
    types["MapValueOut"] = t.struct(
        {
            "fields": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MapValueOut"])
    types["WriteResponseIn"] = t.struct(
        {
            "streamId": t.string().optional(),
            "writeResults": t.array(t.proxy(renames["WriteResultIn"])).optional(),
            "streamToken": t.string().optional(),
            "commitTime": t.string().optional(),
        }
    ).named(renames["WriteResponseIn"])
    types["WriteResponseOut"] = t.struct(
        {
            "streamId": t.string().optional(),
            "writeResults": t.array(t.proxy(renames["WriteResultOut"])).optional(),
            "streamToken": t.string().optional(),
            "commitTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteResponseOut"])
    types["GoogleFirestoreAdminV1TtlConfigIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1TtlConfigIn"])
    types["GoogleFirestoreAdminV1TtlConfigOut"] = t.struct(
        {
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1TtlConfigOut"])
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
    types["DocumentMaskIn"] = t.struct(
        {"fieldPaths": t.array(t.string()).optional()}
    ).named(renames["DocumentMaskIn"])
    types["DocumentMaskOut"] = t.struct(
        {
            "fieldPaths": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentMaskOut"])
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
    types["FilterIn"] = t.struct(
        {
            "fieldFilter": t.proxy(renames["FieldFilterIn"]).optional(),
            "unaryFilter": t.proxy(renames["UnaryFilterIn"]).optional(),
            "compositeFilter": t.proxy(renames["CompositeFilterIn"]).optional(),
        }
    ).named(renames["FilterIn"])
    types["FilterOut"] = t.struct(
        {
            "fieldFilter": t.proxy(renames["FieldFilterOut"]).optional(),
            "unaryFilter": t.proxy(renames["UnaryFilterOut"]).optional(),
            "compositeFilter": t.proxy(renames["CompositeFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterOut"])
    types["GoogleFirestoreAdminV1DatabaseIn"] = t.struct(
        {
            "name": t.string().optional(),
            "concurrencyMode": t.string().optional(),
            "appEngineIntegrationMode": t.string().optional(),
            "deleteProtectionState": t.string().optional(),
            "type": t.string().optional(),
            "etag": t.string().optional(),
            "pointInTimeRecoveryEnablement": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1DatabaseIn"])
    types["GoogleFirestoreAdminV1DatabaseOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "keyPrefix": t.string().optional(),
            "name": t.string().optional(),
            "concurrencyMode": t.string().optional(),
            "versionRetentionPeriod": t.string().optional(),
            "createTime": t.string().optional(),
            "appEngineIntegrationMode": t.string().optional(),
            "deleteProtectionState": t.string().optional(),
            "type": t.string().optional(),
            "etag": t.string().optional(),
            "earliestVersionTime": t.string().optional(),
            "pointInTimeRecoveryEnablement": t.string().optional(),
            "locationId": t.string().optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1DatabaseOut"])
    types["WriteRequestIn"] = t.struct(
        {
            "streamToken": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "streamId": t.string().optional(),
            "writes": t.array(t.proxy(renames["WriteIn"])).optional(),
        }
    ).named(renames["WriteRequestIn"])
    types["WriteRequestOut"] = t.struct(
        {
            "streamToken": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "streamId": t.string().optional(),
            "writes": t.array(t.proxy(renames["WriteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteRequestOut"])
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
    types["ProjectionIn"] = t.struct(
        {"fields": t.array(t.proxy(renames["FieldReferenceIn"])).optional()}
    ).named(renames["ProjectionIn"])
    types["ProjectionOut"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["FieldReferenceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectionOut"])
    types["DocumentsTargetIn"] = t.struct(
        {"documents": t.array(t.string()).optional()}
    ).named(renames["DocumentsTargetIn"])
    types["DocumentsTargetOut"] = t.struct(
        {
            "documents": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentsTargetOut"])
    types["GoogleFirestoreAdminV1WeeklyRecurrenceIn"] = t.struct(
        {"day": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1WeeklyRecurrenceIn"])
    types["GoogleFirestoreAdminV1WeeklyRecurrenceOut"] = t.struct(
        {
            "day": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1WeeklyRecurrenceOut"])
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["PreconditionIn"] = t.struct(
        {"exists": t.boolean().optional(), "updateTime": t.string().optional()}
    ).named(renames["PreconditionIn"])
    types["PreconditionOut"] = t.struct(
        {
            "exists": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PreconditionOut"])
    types["BeginTransactionRequestIn"] = t.struct(
        {"options": t.proxy(renames["TransactionOptionsIn"]).optional()}
    ).named(renames["BeginTransactionRequestIn"])
    types["BeginTransactionRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["TransactionOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BeginTransactionRequestOut"])
    types["RunAggregationQueryResponseIn"] = t.struct(
        {
            "transaction": t.string().optional(),
            "readTime": t.string().optional(),
            "result": t.proxy(renames["AggregationResultIn"]).optional(),
        }
    ).named(renames["RunAggregationQueryResponseIn"])
    types["RunAggregationQueryResponseOut"] = t.struct(
        {
            "transaction": t.string().optional(),
            "readTime": t.string().optional(),
            "result": t.proxy(renames["AggregationResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunAggregationQueryResponseOut"])
    types["FieldReferenceIn"] = t.struct({"fieldPath": t.string().optional()}).named(
        renames["FieldReferenceIn"]
    )
    types["FieldReferenceOut"] = t.struct(
        {
            "fieldPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldReferenceOut"])
    types["GoogleFirestoreAdminV1IndexConfigIn"] = t.struct(
        {
            "usesAncestorConfig": t.boolean().optional(),
            "reverting": t.boolean().optional(),
            "ancestorField": t.string().optional(),
            "indexes": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexIn"])
            ).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexConfigIn"])
    types["GoogleFirestoreAdminV1IndexConfigOut"] = t.struct(
        {
            "usesAncestorConfig": t.boolean().optional(),
            "reverting": t.boolean().optional(),
            "ancestorField": t.string().optional(),
            "indexes": t.array(
                t.proxy(renames["GoogleFirestoreAdminV1IndexOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexConfigOut"])
    types["WriteIn"] = t.struct(
        {
            "currentDocument": t.proxy(renames["PreconditionIn"]).optional(),
            "updateTransforms": t.array(
                t.proxy(renames["FieldTransformIn"])
            ).optional(),
            "delete": t.string().optional(),
            "transform": t.proxy(renames["DocumentTransformIn"]).optional(),
            "updateMask": t.proxy(renames["DocumentMaskIn"]).optional(),
            "update": t.proxy(renames["DocumentIn"]).optional(),
        }
    ).named(renames["WriteIn"])
    types["WriteOut"] = t.struct(
        {
            "currentDocument": t.proxy(renames["PreconditionOut"]).optional(),
            "updateTransforms": t.array(
                t.proxy(renames["FieldTransformOut"])
            ).optional(),
            "delete": t.string().optional(),
            "transform": t.proxy(renames["DocumentTransformOut"]).optional(),
            "updateMask": t.proxy(renames["DocumentMaskOut"]).optional(),
            "update": t.proxy(renames["DocumentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteOut"])
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
    types["DocumentChangeIn"] = t.struct(
        {
            "removedTargetIds": t.array(t.integer()).optional(),
            "targetIds": t.array(t.integer()).optional(),
            "document": t.proxy(renames["DocumentIn"]).optional(),
        }
    ).named(renames["DocumentChangeIn"])
    types["DocumentChangeOut"] = t.struct(
        {
            "removedTargetIds": t.array(t.integer()).optional(),
            "targetIds": t.array(t.integer()).optional(),
            "document": t.proxy(renames["DocumentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentChangeOut"])
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
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
    types["DocumentIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "fields": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["DocumentIn"])
    types["DocumentOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "fields": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentOut"])
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
    types["GoogleFirestoreAdminV1ExportDocumentsRequestIn"] = t.struct(
        {
            "outputUriPrefix": t.string().optional(),
            "namespaceIds": t.array(t.string()).optional(),
            "collectionIds": t.array(t.string()).optional(),
            "snapshotTime": t.string().optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ExportDocumentsRequestIn"])
    types["GoogleFirestoreAdminV1ExportDocumentsRequestOut"] = t.struct(
        {
            "outputUriPrefix": t.string().optional(),
            "namespaceIds": t.array(t.string()).optional(),
            "collectionIds": t.array(t.string()).optional(),
            "snapshotTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ExportDocumentsRequestOut"])
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
    types["ReadOnlyIn"] = t.struct({"readTime": t.string().optional()}).named(
        renames["ReadOnlyIn"]
    )
    types["ReadOnlyOut"] = t.struct(
        {
            "readTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadOnlyOut"])
    types["GoogleFirestoreAdminV1ImportDocumentsRequestIn"] = t.struct(
        {
            "inputUriPrefix": t.string().optional(),
            "namespaceIds": t.array(t.string()).optional(),
            "collectionIds": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ImportDocumentsRequestIn"])
    types["GoogleFirestoreAdminV1ImportDocumentsRequestOut"] = t.struct(
        {
            "inputUriPrefix": t.string().optional(),
            "namespaceIds": t.array(t.string()).optional(),
            "collectionIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ImportDocumentsRequestOut"])
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
    types["GoogleFirestoreAdminV1FieldIn"] = t.struct(
        {
            "ttlConfig": t.proxy(
                renames["GoogleFirestoreAdminV1TtlConfigIn"]
            ).optional(),
            "name": t.string(),
            "indexConfig": t.proxy(
                renames["GoogleFirestoreAdminV1IndexConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1FieldIn"])
    types["GoogleFirestoreAdminV1FieldOut"] = t.struct(
        {
            "ttlConfig": t.proxy(
                renames["GoogleFirestoreAdminV1TtlConfigOut"]
            ).optional(),
            "name": t.string(),
            "indexConfig": t.proxy(
                renames["GoogleFirestoreAdminV1IndexConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1FieldOut"])
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
    types["ExistenceFilterIn"] = t.struct(
        {
            "targetId": t.integer().optional(),
            "unchangedNames": t.proxy(renames["BloomFilterIn"]).optional(),
            "count": t.integer().optional(),
        }
    ).named(renames["ExistenceFilterIn"])
    types["ExistenceFilterOut"] = t.struct(
        {
            "targetId": t.integer().optional(),
            "unchangedNames": t.proxy(renames["BloomFilterOut"]).optional(),
            "count": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExistenceFilterOut"])
    types["GoogleFirestoreAdminV1IndexFieldIn"] = t.struct(
        {
            "arrayConfig": t.string().optional(),
            "fieldPath": t.string().optional(),
            "order": t.string().optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexFieldIn"])
    types["GoogleFirestoreAdminV1IndexFieldOut"] = t.struct(
        {
            "arrayConfig": t.string().optional(),
            "fieldPath": t.string().optional(),
            "order": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexFieldOut"])
    types["GoogleFirestoreAdminV1UpdateDatabaseMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1UpdateDatabaseMetadataIn"])
    types["GoogleFirestoreAdminV1UpdateDatabaseMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleFirestoreAdminV1UpdateDatabaseMetadataOut"])
    types["RunQueryResponseIn"] = t.struct(
        {
            "transaction": t.string().optional(),
            "document": t.proxy(renames["DocumentIn"]).optional(),
            "readTime": t.string().optional(),
            "skippedResults": t.integer().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["RunQueryResponseIn"])
    types["RunQueryResponseOut"] = t.struct(
        {
            "transaction": t.string().optional(),
            "document": t.proxy(renames["DocumentOut"]).optional(),
            "readTime": t.string().optional(),
            "skippedResults": t.integer().optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunQueryResponseOut"])
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
    types["ListCollectionIdsRequestIn"] = t.struct(
        {
            "readTime": t.string().optional(),
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
        }
    ).named(renames["ListCollectionIdsRequestIn"])
    types["ListCollectionIdsRequestOut"] = t.struct(
        {
            "readTime": t.string().optional(),
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCollectionIdsRequestOut"])
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
    types["RunQueryRequestIn"] = t.struct(
        {
            "newTransaction": t.proxy(renames["TransactionOptionsIn"]).optional(),
            "transaction": t.string().optional(),
            "readTime": t.string().optional(),
            "structuredQuery": t.proxy(renames["StructuredQueryIn"]).optional(),
        }
    ).named(renames["RunQueryRequestIn"])
    types["RunQueryRequestOut"] = t.struct(
        {
            "newTransaction": t.proxy(renames["TransactionOptionsOut"]).optional(),
            "transaction": t.string().optional(),
            "readTime": t.string().optional(),
            "structuredQuery": t.proxy(renames["StructuredQueryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunQueryRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["GoogleFirestoreAdminV1ExportDocumentsResponseIn"] = t.struct(
        {"outputUriPrefix": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1ExportDocumentsResponseIn"])
    types["GoogleFirestoreAdminV1ExportDocumentsResponseOut"] = t.struct(
        {
            "outputUriPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ExportDocumentsResponseOut"])
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
    types["BatchGetDocumentsRequestIn"] = t.struct(
        {
            "mask": t.proxy(renames["DocumentMaskIn"]).optional(),
            "transaction": t.string().optional(),
            "readTime": t.string().optional(),
            "documents": t.array(t.string()).optional(),
            "newTransaction": t.proxy(renames["TransactionOptionsIn"]).optional(),
        }
    ).named(renames["BatchGetDocumentsRequestIn"])
    types["BatchGetDocumentsRequestOut"] = t.struct(
        {
            "mask": t.proxy(renames["DocumentMaskOut"]).optional(),
            "transaction": t.string().optional(),
            "readTime": t.string().optional(),
            "documents": t.array(t.string()).optional(),
            "newTransaction": t.proxy(renames["TransactionOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetDocumentsRequestOut"])
    types["ArrayValueIn"] = t.struct(
        {"values": t.array(t.proxy(renames["ValueIn"])).optional()}
    ).named(renames["ArrayValueIn"])
    types["ArrayValueOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["ValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArrayValueOut"])
    types["RunAggregationQueryRequestIn"] = t.struct(
        {
            "readTime": t.string().optional(),
            "structuredAggregationQuery": t.proxy(
                renames["StructuredAggregationQueryIn"]
            ).optional(),
            "newTransaction": t.proxy(renames["TransactionOptionsIn"]).optional(),
            "transaction": t.string().optional(),
        }
    ).named(renames["RunAggregationQueryRequestIn"])
    types["RunAggregationQueryRequestOut"] = t.struct(
        {
            "readTime": t.string().optional(),
            "structuredAggregationQuery": t.proxy(
                renames["StructuredAggregationQueryOut"]
            ).optional(),
            "newTransaction": t.proxy(renames["TransactionOptionsOut"]).optional(),
            "transaction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunAggregationQueryRequestOut"])
    types["GoogleFirestoreAdminV1DailyRecurrenceIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirestoreAdminV1DailyRecurrenceIn"])
    types["GoogleFirestoreAdminV1DailyRecurrenceOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleFirestoreAdminV1DailyRecurrenceOut"])
    types["StructuredQueryIn"] = t.struct(
        {
            "from": t.array(t.proxy(renames["CollectionSelectorIn"])).optional(),
            "endAt": t.proxy(renames["CursorIn"]).optional(),
            "select": t.proxy(renames["ProjectionIn"]).optional(),
            "where": t.proxy(renames["FilterIn"]).optional(),
            "limit": t.integer().optional(),
            "offset": t.integer().optional(),
            "orderBy": t.array(t.proxy(renames["OrderIn"])).optional(),
            "startAt": t.proxy(renames["CursorIn"]).optional(),
        }
    ).named(renames["StructuredQueryIn"])
    types["StructuredQueryOut"] = t.struct(
        {
            "from": t.array(t.proxy(renames["CollectionSelectorOut"])).optional(),
            "endAt": t.proxy(renames["CursorOut"]).optional(),
            "select": t.proxy(renames["ProjectionOut"]).optional(),
            "where": t.proxy(renames["FilterOut"]).optional(),
            "limit": t.integer().optional(),
            "offset": t.integer().optional(),
            "orderBy": t.array(t.proxy(renames["OrderOut"])).optional(),
            "startAt": t.proxy(renames["CursorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructuredQueryOut"])
    types["GoogleFirestoreAdminV1IndexOperationMetadataIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "index": t.string().optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
            "state": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexOperationMetadataIn"])
    types["GoogleFirestoreAdminV1IndexOperationMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "index": t.string().optional(),
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "state": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1IndexOperationMetadataOut"])
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
    types["GoogleFirestoreAdminV1ExportDocumentsMetadataIn"] = t.struct(
        {
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
            "outputUriPrefix": t.string().optional(),
            "startTime": t.string().optional(),
            "operationState": t.string().optional(),
            "namespaceIds": t.array(t.string()).optional(),
            "collectionIds": t.array(t.string()).optional(),
            "endTime": t.string().optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressIn"]
            ).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ExportDocumentsMetadataIn"])
    types["GoogleFirestoreAdminV1ExportDocumentsMetadataOut"] = t.struct(
        {
            "progressDocuments": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "outputUriPrefix": t.string().optional(),
            "startTime": t.string().optional(),
            "operationState": t.string().optional(),
            "namespaceIds": t.array(t.string()).optional(),
            "collectionIds": t.array(t.string()).optional(),
            "endTime": t.string().optional(),
            "progressBytes": t.proxy(
                renames["GoogleFirestoreAdminV1ProgressOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1ExportDocumentsMetadataOut"])
    types["BeginTransactionResponseIn"] = t.struct(
        {"transaction": t.string().optional()}
    ).named(renames["BeginTransactionResponseIn"])
    types["BeginTransactionResponseOut"] = t.struct(
        {
            "transaction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BeginTransactionResponseOut"])
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
    types["GoogleFirestoreAdminV1BackupScheduleIn"] = t.struct(
        {
            "dailyRecurrence": t.proxy(
                renames["GoogleFirestoreAdminV1DailyRecurrenceIn"]
            ).optional(),
            "weeklyRecurrence": t.proxy(
                renames["GoogleFirestoreAdminV1WeeklyRecurrenceIn"]
            ).optional(),
            "retention": t.string().optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1BackupScheduleIn"])
    types["GoogleFirestoreAdminV1BackupScheduleOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "dailyRecurrence": t.proxy(
                renames["GoogleFirestoreAdminV1DailyRecurrenceOut"]
            ).optional(),
            "weeklyRecurrence": t.proxy(
                renames["GoogleFirestoreAdminV1WeeklyRecurrenceOut"]
            ).optional(),
            "retention": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1BackupScheduleOut"])
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
    types["GoogleFirestoreAdminV1RestoreDatabaseMetadataIn"] = t.struct(
        {
            "backup": t.string().optional(),
            "operationState": t.string().optional(),
            "database": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1RestoreDatabaseMetadataIn"])
    types["GoogleFirestoreAdminV1RestoreDatabaseMetadataOut"] = t.struct(
        {
            "backup": t.string().optional(),
            "operationState": t.string().optional(),
            "database": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirestoreAdminV1RestoreDatabaseMetadataOut"])
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
    functions["projectsDatabasesImportDocuments"] = firestore.post(
        "v1/{parent}/databases:restore",
        t.struct(
            {
                "parent": t.string(),
                "databaseId": t.string(),
                "backup": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDelete"] = firestore.post(
        "v1/{parent}/databases:restore",
        t.struct(
            {
                "parent": t.string(),
                "databaseId": t.string(),
                "backup": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesExportDocuments"] = firestore.post(
        "v1/{parent}/databases:restore",
        t.struct(
            {
                "parent": t.string(),
                "databaseId": t.string(),
                "backup": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesList"] = firestore.post(
        "v1/{parent}/databases:restore",
        t.struct(
            {
                "parent": t.string(),
                "databaseId": t.string(),
                "backup": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesGet"] = firestore.post(
        "v1/{parent}/databases:restore",
        t.struct(
            {
                "parent": t.string(),
                "databaseId": t.string(),
                "backup": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesCreate"] = firestore.post(
        "v1/{parent}/databases:restore",
        t.struct(
            {
                "parent": t.string(),
                "databaseId": t.string(),
                "backup": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesPatch"] = firestore.post(
        "v1/{parent}/databases:restore",
        t.struct(
            {
                "parent": t.string(),
                "databaseId": t.string(),
                "backup": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesRestore"] = firestore.post(
        "v1/{parent}/databases:restore",
        t.struct(
            {
                "parent": t.string(),
                "databaseId": t.string(),
                "backup": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsList"] = firestore.post(
        "v1/{database}/documents:write",
        t.struct(
            {
                "database": t.string(),
                "streamToken": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "streamId": t.string().optional(),
                "writes": t.array(t.proxy(renames["WriteIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WriteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsRunQuery"] = firestore.post(
        "v1/{database}/documents:write",
        t.struct(
            {
                "database": t.string(),
                "streamToken": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "streamId": t.string().optional(),
                "writes": t.array(t.proxy(renames["WriteIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WriteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsCommit"] = firestore.post(
        "v1/{database}/documents:write",
        t.struct(
            {
                "database": t.string(),
                "streamToken": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "streamId": t.string().optional(),
                "writes": t.array(t.proxy(renames["WriteIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WriteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsGet"] = firestore.post(
        "v1/{database}/documents:write",
        t.struct(
            {
                "database": t.string(),
                "streamToken": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "streamId": t.string().optional(),
                "writes": t.array(t.proxy(renames["WriteIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WriteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsListCollectionIds"] = firestore.post(
        "v1/{database}/documents:write",
        t.struct(
            {
                "database": t.string(),
                "streamToken": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "streamId": t.string().optional(),
                "writes": t.array(t.proxy(renames["WriteIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WriteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsBeginTransaction"] = firestore.post(
        "v1/{database}/documents:write",
        t.struct(
            {
                "database": t.string(),
                "streamToken": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "streamId": t.string().optional(),
                "writes": t.array(t.proxy(renames["WriteIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WriteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsBatchWrite"] = firestore.post(
        "v1/{database}/documents:write",
        t.struct(
            {
                "database": t.string(),
                "streamToken": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "streamId": t.string().optional(),
                "writes": t.array(t.proxy(renames["WriteIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WriteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsPatch"] = firestore.post(
        "v1/{database}/documents:write",
        t.struct(
            {
                "database": t.string(),
                "streamToken": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "streamId": t.string().optional(),
                "writes": t.array(t.proxy(renames["WriteIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WriteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsBatchGet"] = firestore.post(
        "v1/{database}/documents:write",
        t.struct(
            {
                "database": t.string(),
                "streamToken": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "streamId": t.string().optional(),
                "writes": t.array(t.proxy(renames["WriteIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WriteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsCreateDocument"] = firestore.post(
        "v1/{database}/documents:write",
        t.struct(
            {
                "database": t.string(),
                "streamToken": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "streamId": t.string().optional(),
                "writes": t.array(t.proxy(renames["WriteIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WriteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsPartitionQuery"] = firestore.post(
        "v1/{database}/documents:write",
        t.struct(
            {
                "database": t.string(),
                "streamToken": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "streamId": t.string().optional(),
                "writes": t.array(t.proxy(renames["WriteIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WriteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsDelete"] = firestore.post(
        "v1/{database}/documents:write",
        t.struct(
            {
                "database": t.string(),
                "streamToken": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "streamId": t.string().optional(),
                "writes": t.array(t.proxy(renames["WriteIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WriteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsRunAggregationQuery"] = firestore.post(
        "v1/{database}/documents:write",
        t.struct(
            {
                "database": t.string(),
                "streamToken": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "streamId": t.string().optional(),
                "writes": t.array(t.proxy(renames["WriteIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WriteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsListDocuments"] = firestore.post(
        "v1/{database}/documents:write",
        t.struct(
            {
                "database": t.string(),
                "streamToken": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "streamId": t.string().optional(),
                "writes": t.array(t.proxy(renames["WriteIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WriteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsRollback"] = firestore.post(
        "v1/{database}/documents:write",
        t.struct(
            {
                "database": t.string(),
                "streamToken": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "streamId": t.string().optional(),
                "writes": t.array(t.proxy(renames["WriteIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WriteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsListen"] = firestore.post(
        "v1/{database}/documents:write",
        t.struct(
            {
                "database": t.string(),
                "streamToken": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "streamId": t.string().optional(),
                "writes": t.array(t.proxy(renames["WriteIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WriteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesDocumentsWrite"] = firestore.post(
        "v1/{database}/documents:write",
        t.struct(
            {
                "database": t.string(),
                "streamToken": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "streamId": t.string().optional(),
                "writes": t.array(t.proxy(renames["WriteIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WriteResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesCollectionGroupsFieldsGet"] = firestore.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "ttlConfig": t.proxy(
                    renames["GoogleFirestoreAdminV1TtlConfigIn"]
                ).optional(),
                "indexConfig": t.proxy(
                    renames["GoogleFirestoreAdminV1IndexConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesCollectionGroupsFieldsList"] = firestore.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "ttlConfig": t.proxy(
                    renames["GoogleFirestoreAdminV1TtlConfigIn"]
                ).optional(),
                "indexConfig": t.proxy(
                    renames["GoogleFirestoreAdminV1IndexConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesCollectionGroupsFieldsPatch"] = firestore.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "ttlConfig": t.proxy(
                    renames["GoogleFirestoreAdminV1TtlConfigIn"]
                ).optional(),
                "indexConfig": t.proxy(
                    renames["GoogleFirestoreAdminV1IndexConfigIn"]
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
                "name": t.string().optional(),
                "queryScope": t.string().optional(),
                "apiScope": t.string().optional(),
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
    functions["projectsDatabasesCollectionGroupsIndexesGet"] = firestore.post(
        "v1/{parent}/indexes",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "queryScope": t.string().optional(),
                "apiScope": t.string().optional(),
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
                "name": t.string().optional(),
                "queryScope": t.string().optional(),
                "apiScope": t.string().optional(),
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
                "name": t.string().optional(),
                "queryScope": t.string().optional(),
                "apiScope": t.string().optional(),
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
    functions["projectsDatabasesBackupSchedulesCreate"] = firestore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirestoreAdminV1BackupScheduleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesBackupSchedulesList"] = firestore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirestoreAdminV1BackupScheduleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesBackupSchedulesPatch"] = firestore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirestoreAdminV1BackupScheduleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesBackupSchedulesDelete"] = firestore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirestoreAdminV1BackupScheduleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDatabasesBackupSchedulesGet"] = firestore.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirestoreAdminV1BackupScheduleOut"]),
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
    functions["projectsLocationsBackupsDelete"] = firestore.get(
        "v1/{parent}/backups",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirestoreAdminV1ListBackupsResponseOut"]),
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
