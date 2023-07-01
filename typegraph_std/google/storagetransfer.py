from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_storagetransfer():
    storagetransfer = HTTPRuntime("https://storagetransfer.googleapis.com/")

    renames = {
        "ErrorResponse": "_storagetransfer_1_ErrorResponse",
        "ResumeTransferOperationRequestIn": "_storagetransfer_2_ResumeTransferOperationRequestIn",
        "ResumeTransferOperationRequestOut": "_storagetransfer_3_ResumeTransferOperationRequestOut",
        "TransferCountersIn": "_storagetransfer_4_TransferCountersIn",
        "TransferCountersOut": "_storagetransfer_5_TransferCountersOut",
        "TransferSpecIn": "_storagetransfer_6_TransferSpecIn",
        "TransferSpecOut": "_storagetransfer_7_TransferSpecOut",
        "ListAgentPoolsResponseIn": "_storagetransfer_8_ListAgentPoolsResponseIn",
        "ListAgentPoolsResponseOut": "_storagetransfer_9_ListAgentPoolsResponseOut",
        "AzureCredentialsIn": "_storagetransfer_10_AzureCredentialsIn",
        "AzureCredentialsOut": "_storagetransfer_11_AzureCredentialsOut",
        "DateIn": "_storagetransfer_12_DateIn",
        "DateOut": "_storagetransfer_13_DateOut",
        "StatusIn": "_storagetransfer_14_StatusIn",
        "StatusOut": "_storagetransfer_15_StatusOut",
        "PauseTransferOperationRequestIn": "_storagetransfer_16_PauseTransferOperationRequestIn",
        "PauseTransferOperationRequestOut": "_storagetransfer_17_PauseTransferOperationRequestOut",
        "TransferOptionsIn": "_storagetransfer_18_TransferOptionsIn",
        "TransferOptionsOut": "_storagetransfer_19_TransferOptionsOut",
        "ObjectConditionsIn": "_storagetransfer_20_ObjectConditionsIn",
        "ObjectConditionsOut": "_storagetransfer_21_ObjectConditionsOut",
        "PosixFilesystemIn": "_storagetransfer_22_PosixFilesystemIn",
        "PosixFilesystemOut": "_storagetransfer_23_PosixFilesystemOut",
        "GcsDataIn": "_storagetransfer_24_GcsDataIn",
        "GcsDataOut": "_storagetransfer_25_GcsDataOut",
        "AwsAccessKeyIn": "_storagetransfer_26_AwsAccessKeyIn",
        "AwsAccessKeyOut": "_storagetransfer_27_AwsAccessKeyOut",
        "RunTransferJobRequestIn": "_storagetransfer_28_RunTransferJobRequestIn",
        "RunTransferJobRequestOut": "_storagetransfer_29_RunTransferJobRequestOut",
        "AgentPoolIn": "_storagetransfer_30_AgentPoolIn",
        "AgentPoolOut": "_storagetransfer_31_AgentPoolOut",
        "EmptyIn": "_storagetransfer_32_EmptyIn",
        "EmptyOut": "_storagetransfer_33_EmptyOut",
        "GoogleServiceAccountIn": "_storagetransfer_34_GoogleServiceAccountIn",
        "GoogleServiceAccountOut": "_storagetransfer_35_GoogleServiceAccountOut",
        "AzureBlobStorageDataIn": "_storagetransfer_36_AzureBlobStorageDataIn",
        "AzureBlobStorageDataOut": "_storagetransfer_37_AzureBlobStorageDataOut",
        "TransferManifestIn": "_storagetransfer_38_TransferManifestIn",
        "TransferManifestOut": "_storagetransfer_39_TransferManifestOut",
        "ScheduleIn": "_storagetransfer_40_ScheduleIn",
        "ScheduleOut": "_storagetransfer_41_ScheduleOut",
        "AwsS3CompatibleDataIn": "_storagetransfer_42_AwsS3CompatibleDataIn",
        "AwsS3CompatibleDataOut": "_storagetransfer_43_AwsS3CompatibleDataOut",
        "ErrorSummaryIn": "_storagetransfer_44_ErrorSummaryIn",
        "ErrorSummaryOut": "_storagetransfer_45_ErrorSummaryOut",
        "TimeOfDayIn": "_storagetransfer_46_TimeOfDayIn",
        "TimeOfDayOut": "_storagetransfer_47_TimeOfDayOut",
        "ErrorLogEntryIn": "_storagetransfer_48_ErrorLogEntryIn",
        "ErrorLogEntryOut": "_storagetransfer_49_ErrorLogEntryOut",
        "HttpDataIn": "_storagetransfer_50_HttpDataIn",
        "HttpDataOut": "_storagetransfer_51_HttpDataOut",
        "BandwidthLimitIn": "_storagetransfer_52_BandwidthLimitIn",
        "BandwidthLimitOut": "_storagetransfer_53_BandwidthLimitOut",
        "OperationIn": "_storagetransfer_54_OperationIn",
        "OperationOut": "_storagetransfer_55_OperationOut",
        "MetadataOptionsIn": "_storagetransfer_56_MetadataOptionsIn",
        "MetadataOptionsOut": "_storagetransfer_57_MetadataOptionsOut",
        "S3CompatibleMetadataIn": "_storagetransfer_58_S3CompatibleMetadataIn",
        "S3CompatibleMetadataOut": "_storagetransfer_59_S3CompatibleMetadataOut",
        "EventStreamIn": "_storagetransfer_60_EventStreamIn",
        "EventStreamOut": "_storagetransfer_61_EventStreamOut",
        "TransferOperationIn": "_storagetransfer_62_TransferOperationIn",
        "TransferOperationOut": "_storagetransfer_63_TransferOperationOut",
        "NotificationConfigIn": "_storagetransfer_64_NotificationConfigIn",
        "NotificationConfigOut": "_storagetransfer_65_NotificationConfigOut",
        "ListTransferJobsResponseIn": "_storagetransfer_66_ListTransferJobsResponseIn",
        "ListTransferJobsResponseOut": "_storagetransfer_67_ListTransferJobsResponseOut",
        "CancelOperationRequestIn": "_storagetransfer_68_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_storagetransfer_69_CancelOperationRequestOut",
        "TransferJobIn": "_storagetransfer_70_TransferJobIn",
        "TransferJobOut": "_storagetransfer_71_TransferJobOut",
        "AwsS3DataIn": "_storagetransfer_72_AwsS3DataIn",
        "AwsS3DataOut": "_storagetransfer_73_AwsS3DataOut",
        "ListOperationsResponseIn": "_storagetransfer_74_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_storagetransfer_75_ListOperationsResponseOut",
        "LoggingConfigIn": "_storagetransfer_76_LoggingConfigIn",
        "LoggingConfigOut": "_storagetransfer_77_LoggingConfigOut",
        "UpdateTransferJobRequestIn": "_storagetransfer_78_UpdateTransferJobRequestIn",
        "UpdateTransferJobRequestOut": "_storagetransfer_79_UpdateTransferJobRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ResumeTransferOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ResumeTransferOperationRequestIn"])
    types["ResumeTransferOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumeTransferOperationRequestOut"])
    types["TransferCountersIn"] = t.struct(
        {
            "directoriesFoundFromSource": t.string().optional(),
            "objectsCopiedToSink": t.string().optional(),
            "bytesDeletedFromSource": t.string().optional(),
            "bytesFoundFromSource": t.string().optional(),
            "intermediateObjectsCleanedUp": t.string().optional(),
            "objectsDeletedFromSink": t.string().optional(),
            "objectsFromSourceSkippedBySync": t.string().optional(),
            "objectsFoundFromSource": t.string().optional(),
            "objectsFoundOnlyFromSink": t.string().optional(),
            "bytesDeletedFromSink": t.string().optional(),
            "objectsFromSourceFailed": t.string().optional(),
            "directoriesSuccessfullyListedFromSource": t.string().optional(),
            "bytesFailedToDeleteFromSink": t.string().optional(),
            "bytesFoundOnlyFromSink": t.string().optional(),
            "directoriesFailedToListFromSource": t.string().optional(),
            "bytesFromSourceSkippedBySync": t.string().optional(),
            "bytesFromSourceFailed": t.string().optional(),
            "objectsDeletedFromSource": t.string().optional(),
            "objectsFailedToDeleteFromSink": t.string().optional(),
            "intermediateObjectsFailedCleanedUp": t.string().optional(),
            "bytesCopiedToSink": t.string().optional(),
        }
    ).named(renames["TransferCountersIn"])
    types["TransferCountersOut"] = t.struct(
        {
            "directoriesFoundFromSource": t.string().optional(),
            "objectsCopiedToSink": t.string().optional(),
            "bytesDeletedFromSource": t.string().optional(),
            "bytesFoundFromSource": t.string().optional(),
            "intermediateObjectsCleanedUp": t.string().optional(),
            "objectsDeletedFromSink": t.string().optional(),
            "objectsFromSourceSkippedBySync": t.string().optional(),
            "objectsFoundFromSource": t.string().optional(),
            "objectsFoundOnlyFromSink": t.string().optional(),
            "bytesDeletedFromSink": t.string().optional(),
            "objectsFromSourceFailed": t.string().optional(),
            "directoriesSuccessfullyListedFromSource": t.string().optional(),
            "bytesFailedToDeleteFromSink": t.string().optional(),
            "bytesFoundOnlyFromSink": t.string().optional(),
            "directoriesFailedToListFromSource": t.string().optional(),
            "bytesFromSourceSkippedBySync": t.string().optional(),
            "bytesFromSourceFailed": t.string().optional(),
            "objectsDeletedFromSource": t.string().optional(),
            "objectsFailedToDeleteFromSink": t.string().optional(),
            "intermediateObjectsFailedCleanedUp": t.string().optional(),
            "bytesCopiedToSink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferCountersOut"])
    types["TransferSpecIn"] = t.struct(
        {
            "gcsDataSink": t.proxy(renames["GcsDataIn"]).optional(),
            "sourceAgentPoolName": t.string().optional(),
            "transferManifest": t.proxy(renames["TransferManifestIn"]).optional(),
            "posixDataSink": t.proxy(renames["PosixFilesystemIn"]).optional(),
            "gcsDataSource": t.proxy(renames["GcsDataIn"]).optional(),
            "objectConditions": t.proxy(renames["ObjectConditionsIn"]).optional(),
            "httpDataSource": t.proxy(renames["HttpDataIn"]).optional(),
            "awsS3DataSource": t.proxy(renames["AwsS3DataIn"]).optional(),
            "gcsIntermediateDataLocation": t.proxy(renames["GcsDataIn"]).optional(),
            "sinkAgentPoolName": t.string().optional(),
            "posixDataSource": t.proxy(renames["PosixFilesystemIn"]).optional(),
            "awsS3CompatibleDataSource": t.proxy(
                renames["AwsS3CompatibleDataIn"]
            ).optional(),
            "transferOptions": t.proxy(renames["TransferOptionsIn"]).optional(),
            "azureBlobStorageDataSource": t.proxy(
                renames["AzureBlobStorageDataIn"]
            ).optional(),
        }
    ).named(renames["TransferSpecIn"])
    types["TransferSpecOut"] = t.struct(
        {
            "gcsDataSink": t.proxy(renames["GcsDataOut"]).optional(),
            "sourceAgentPoolName": t.string().optional(),
            "transferManifest": t.proxy(renames["TransferManifestOut"]).optional(),
            "posixDataSink": t.proxy(renames["PosixFilesystemOut"]).optional(),
            "gcsDataSource": t.proxy(renames["GcsDataOut"]).optional(),
            "objectConditions": t.proxy(renames["ObjectConditionsOut"]).optional(),
            "httpDataSource": t.proxy(renames["HttpDataOut"]).optional(),
            "awsS3DataSource": t.proxy(renames["AwsS3DataOut"]).optional(),
            "gcsIntermediateDataLocation": t.proxy(renames["GcsDataOut"]).optional(),
            "sinkAgentPoolName": t.string().optional(),
            "posixDataSource": t.proxy(renames["PosixFilesystemOut"]).optional(),
            "awsS3CompatibleDataSource": t.proxy(
                renames["AwsS3CompatibleDataOut"]
            ).optional(),
            "transferOptions": t.proxy(renames["TransferOptionsOut"]).optional(),
            "azureBlobStorageDataSource": t.proxy(
                renames["AzureBlobStorageDataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferSpecOut"])
    types["ListAgentPoolsResponseIn"] = t.struct(
        {
            "agentPools": t.array(t.proxy(renames["AgentPoolIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAgentPoolsResponseIn"])
    types["ListAgentPoolsResponseOut"] = t.struct(
        {
            "agentPools": t.array(t.proxy(renames["AgentPoolOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAgentPoolsResponseOut"])
    types["AzureCredentialsIn"] = t.struct({"sasToken": t.string()}).named(
        renames["AzureCredentialsIn"]
    )
    types["AzureCredentialsOut"] = t.struct(
        {"sasToken": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AzureCredentialsOut"])
    types["DateIn"] = t.struct(
        {
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["PauseTransferOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["PauseTransferOperationRequestIn"])
    types["PauseTransferOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PauseTransferOperationRequestOut"])
    types["TransferOptionsIn"] = t.struct(
        {
            "metadataOptions": t.proxy(renames["MetadataOptionsIn"]).optional(),
            "deleteObjectsUniqueInSink": t.boolean().optional(),
            "overwriteObjectsAlreadyExistingInSink": t.boolean().optional(),
            "deleteObjectsFromSourceAfterTransfer": t.boolean().optional(),
            "overwriteWhen": t.string().optional(),
        }
    ).named(renames["TransferOptionsIn"])
    types["TransferOptionsOut"] = t.struct(
        {
            "metadataOptions": t.proxy(renames["MetadataOptionsOut"]).optional(),
            "deleteObjectsUniqueInSink": t.boolean().optional(),
            "overwriteObjectsAlreadyExistingInSink": t.boolean().optional(),
            "deleteObjectsFromSourceAfterTransfer": t.boolean().optional(),
            "overwriteWhen": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferOptionsOut"])
    types["ObjectConditionsIn"] = t.struct(
        {
            "lastModifiedBefore": t.string().optional(),
            "minTimeElapsedSinceLastModification": t.string().optional(),
            "lastModifiedSince": t.string().optional(),
            "maxTimeElapsedSinceLastModification": t.string().optional(),
            "excludePrefixes": t.array(t.string()).optional(),
            "includePrefixes": t.array(t.string()).optional(),
        }
    ).named(renames["ObjectConditionsIn"])
    types["ObjectConditionsOut"] = t.struct(
        {
            "lastModifiedBefore": t.string().optional(),
            "minTimeElapsedSinceLastModification": t.string().optional(),
            "lastModifiedSince": t.string().optional(),
            "maxTimeElapsedSinceLastModification": t.string().optional(),
            "excludePrefixes": t.array(t.string()).optional(),
            "includePrefixes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectConditionsOut"])
    types["PosixFilesystemIn"] = t.struct(
        {"rootDirectory": t.string().optional()}
    ).named(renames["PosixFilesystemIn"])
    types["PosixFilesystemOut"] = t.struct(
        {
            "rootDirectory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosixFilesystemOut"])
    types["GcsDataIn"] = t.struct(
        {"path": t.string().optional(), "bucketName": t.string()}
    ).named(renames["GcsDataIn"])
    types["GcsDataOut"] = t.struct(
        {
            "path": t.string().optional(),
            "bucketName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsDataOut"])
    types["AwsAccessKeyIn"] = t.struct(
        {"secretAccessKey": t.string(), "accessKeyId": t.string()}
    ).named(renames["AwsAccessKeyIn"])
    types["AwsAccessKeyOut"] = t.struct(
        {
            "secretAccessKey": t.string(),
            "accessKeyId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AwsAccessKeyOut"])
    types["RunTransferJobRequestIn"] = t.struct({"projectId": t.string()}).named(
        renames["RunTransferJobRequestIn"]
    )
    types["RunTransferJobRequestOut"] = t.struct(
        {"projectId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RunTransferJobRequestOut"])
    types["AgentPoolIn"] = t.struct(
        {
            "name": t.string(),
            "bandwidthLimit": t.proxy(renames["BandwidthLimitIn"]).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["AgentPoolIn"])
    types["AgentPoolOut"] = t.struct(
        {
            "name": t.string(),
            "bandwidthLimit": t.proxy(renames["BandwidthLimitOut"]).optional(),
            "state": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentPoolOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GoogleServiceAccountIn"] = t.struct(
        {"subjectId": t.string().optional(), "accountEmail": t.string().optional()}
    ).named(renames["GoogleServiceAccountIn"])
    types["GoogleServiceAccountOut"] = t.struct(
        {
            "subjectId": t.string().optional(),
            "accountEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleServiceAccountOut"])
    types["AzureBlobStorageDataIn"] = t.struct(
        {
            "storageAccount": t.string(),
            "credentialsSecret": t.string().optional(),
            "azureCredentials": t.proxy(renames["AzureCredentialsIn"]),
            "path": t.string().optional(),
            "container": t.string(),
        }
    ).named(renames["AzureBlobStorageDataIn"])
    types["AzureBlobStorageDataOut"] = t.struct(
        {
            "storageAccount": t.string(),
            "credentialsSecret": t.string().optional(),
            "azureCredentials": t.proxy(renames["AzureCredentialsOut"]),
            "path": t.string().optional(),
            "container": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AzureBlobStorageDataOut"])
    types["TransferManifestIn"] = t.struct({"location": t.string().optional()}).named(
        renames["TransferManifestIn"]
    )
    types["TransferManifestOut"] = t.struct(
        {
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferManifestOut"])
    types["ScheduleIn"] = t.struct(
        {
            "repeatInterval": t.string().optional(),
            "endTimeOfDay": t.proxy(renames["TimeOfDayIn"]).optional(),
            "scheduleEndDate": t.proxy(renames["DateIn"]).optional(),
            "scheduleStartDate": t.proxy(renames["DateIn"]),
            "startTimeOfDay": t.proxy(renames["TimeOfDayIn"]).optional(),
        }
    ).named(renames["ScheduleIn"])
    types["ScheduleOut"] = t.struct(
        {
            "repeatInterval": t.string().optional(),
            "endTimeOfDay": t.proxy(renames["TimeOfDayOut"]).optional(),
            "scheduleEndDate": t.proxy(renames["DateOut"]).optional(),
            "scheduleStartDate": t.proxy(renames["DateOut"]),
            "startTimeOfDay": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduleOut"])
    types["AwsS3CompatibleDataIn"] = t.struct(
        {
            "endpoint": t.string(),
            "path": t.string().optional(),
            "region": t.string().optional(),
            "s3Metadata": t.proxy(renames["S3CompatibleMetadataIn"]).optional(),
            "bucketName": t.string(),
        }
    ).named(renames["AwsS3CompatibleDataIn"])
    types["AwsS3CompatibleDataOut"] = t.struct(
        {
            "endpoint": t.string(),
            "path": t.string().optional(),
            "region": t.string().optional(),
            "s3Metadata": t.proxy(renames["S3CompatibleMetadataOut"]).optional(),
            "bucketName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AwsS3CompatibleDataOut"])
    types["ErrorSummaryIn"] = t.struct(
        {
            "errorCode": t.string(),
            "errorLogEntries": t.array(t.proxy(renames["ErrorLogEntryIn"])).optional(),
            "errorCount": t.string(),
        }
    ).named(renames["ErrorSummaryIn"])
    types["ErrorSummaryOut"] = t.struct(
        {
            "errorCode": t.string(),
            "errorLogEntries": t.array(t.proxy(renames["ErrorLogEntryOut"])).optional(),
            "errorCount": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorSummaryOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["ErrorLogEntryIn"] = t.struct(
        {"url": t.string(), "errorDetails": t.array(t.string()).optional()}
    ).named(renames["ErrorLogEntryIn"])
    types["ErrorLogEntryOut"] = t.struct(
        {
            "url": t.string(),
            "errorDetails": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorLogEntryOut"])
    types["HttpDataIn"] = t.struct({"listUrl": t.string()}).named(renames["HttpDataIn"])
    types["HttpDataOut"] = t.struct(
        {"listUrl": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["HttpDataOut"])
    types["BandwidthLimitIn"] = t.struct({"limitMbps": t.string().optional()}).named(
        renames["BandwidthLimitIn"]
    )
    types["BandwidthLimitOut"] = t.struct(
        {
            "limitMbps": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BandwidthLimitOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["MetadataOptionsIn"] = t.struct(
        {
            "temporaryHold": t.string().optional(),
            "mode": t.string().optional(),
            "acl": t.string().optional(),
            "symlink": t.string().optional(),
            "timeCreated": t.string().optional(),
            "gid": t.string().optional(),
            "kmsKey": t.string().optional(),
            "storageClass": t.string().optional(),
            "uid": t.string().optional(),
        }
    ).named(renames["MetadataOptionsIn"])
    types["MetadataOptionsOut"] = t.struct(
        {
            "temporaryHold": t.string().optional(),
            "mode": t.string().optional(),
            "acl": t.string().optional(),
            "symlink": t.string().optional(),
            "timeCreated": t.string().optional(),
            "gid": t.string().optional(),
            "kmsKey": t.string().optional(),
            "storageClass": t.string().optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOptionsOut"])
    types["S3CompatibleMetadataIn"] = t.struct(
        {
            "authMethod": t.string().optional(),
            "protocol": t.string().optional(),
            "listApi": t.string().optional(),
            "requestModel": t.string().optional(),
        }
    ).named(renames["S3CompatibleMetadataIn"])
    types["S3CompatibleMetadataOut"] = t.struct(
        {
            "authMethod": t.string().optional(),
            "protocol": t.string().optional(),
            "listApi": t.string().optional(),
            "requestModel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["S3CompatibleMetadataOut"])
    types["EventStreamIn"] = t.struct(
        {
            "eventStreamExpirationTime": t.string().optional(),
            "eventStreamStartTime": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["EventStreamIn"])
    types["EventStreamOut"] = t.struct(
        {
            "eventStreamExpirationTime": t.string().optional(),
            "eventStreamStartTime": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventStreamOut"])
    types["TransferOperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "counters": t.proxy(renames["TransferCountersIn"]).optional(),
            "status": t.string().optional(),
            "transferSpec": t.proxy(renames["TransferSpecIn"]).optional(),
            "errorBreakdowns": t.array(t.proxy(renames["ErrorSummaryIn"])).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "transferJobName": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "projectId": t.string().optional(),
            "notificationConfig": t.proxy(renames["NotificationConfigIn"]).optional(),
        }
    ).named(renames["TransferOperationIn"])
    types["TransferOperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "counters": t.proxy(renames["TransferCountersOut"]).optional(),
            "status": t.string().optional(),
            "transferSpec": t.proxy(renames["TransferSpecOut"]).optional(),
            "errorBreakdowns": t.array(t.proxy(renames["ErrorSummaryOut"])).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "transferJobName": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "projectId": t.string().optional(),
            "notificationConfig": t.proxy(renames["NotificationConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferOperationOut"])
    types["NotificationConfigIn"] = t.struct(
        {
            "pubsubTopic": t.string(),
            "payloadFormat": t.string(),
            "eventTypes": t.array(t.string()).optional(),
        }
    ).named(renames["NotificationConfigIn"])
    types["NotificationConfigOut"] = t.struct(
        {
            "pubsubTopic": t.string(),
            "payloadFormat": t.string(),
            "eventTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationConfigOut"])
    types["ListTransferJobsResponseIn"] = t.struct(
        {
            "transferJobs": t.array(t.proxy(renames["TransferJobIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListTransferJobsResponseIn"])
    types["ListTransferJobsResponseOut"] = t.struct(
        {
            "transferJobs": t.array(t.proxy(renames["TransferJobOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTransferJobsResponseOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["TransferJobIn"] = t.struct(
        {
            "eventStream": t.proxy(renames["EventStreamIn"]).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "status": t.string().optional(),
            "schedule": t.proxy(renames["ScheduleIn"]).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "transferSpec": t.proxy(renames["TransferSpecIn"]).optional(),
            "latestOperationName": t.string().optional(),
            "projectId": t.string().optional(),
            "notificationConfig": t.proxy(renames["NotificationConfigIn"]).optional(),
        }
    ).named(renames["TransferJobIn"])
    types["TransferJobOut"] = t.struct(
        {
            "eventStream": t.proxy(renames["EventStreamOut"]).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "status": t.string().optional(),
            "deletionTime": t.string().optional(),
            "schedule": t.proxy(renames["ScheduleOut"]).optional(),
            "creationTime": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "transferSpec": t.proxy(renames["TransferSpecOut"]).optional(),
            "latestOperationName": t.string().optional(),
            "projectId": t.string().optional(),
            "lastModificationTime": t.string().optional(),
            "notificationConfig": t.proxy(renames["NotificationConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferJobOut"])
    types["AwsS3DataIn"] = t.struct(
        {
            "roleArn": t.string().optional(),
            "path": t.string().optional(),
            "bucketName": t.string(),
            "credentialsSecret": t.string().optional(),
            "awsAccessKey": t.proxy(renames["AwsAccessKeyIn"]).optional(),
        }
    ).named(renames["AwsS3DataIn"])
    types["AwsS3DataOut"] = t.struct(
        {
            "roleArn": t.string().optional(),
            "path": t.string().optional(),
            "bucketName": t.string(),
            "credentialsSecret": t.string().optional(),
            "awsAccessKey": t.proxy(renames["AwsAccessKeyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AwsS3DataOut"])
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
    types["LoggingConfigIn"] = t.struct(
        {
            "logActions": t.array(t.string()).optional(),
            "enableOnpremGcsTransferLogs": t.boolean().optional(),
            "logActionStates": t.array(t.string()).optional(),
        }
    ).named(renames["LoggingConfigIn"])
    types["LoggingConfigOut"] = t.struct(
        {
            "logActions": t.array(t.string()).optional(),
            "enableOnpremGcsTransferLogs": t.boolean().optional(),
            "logActionStates": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoggingConfigOut"])
    types["UpdateTransferJobRequestIn"] = t.struct(
        {
            "transferJob": t.proxy(renames["TransferJobIn"]),
            "projectId": t.string(),
            "updateTransferJobFieldMask": t.string().optional(),
        }
    ).named(renames["UpdateTransferJobRequestIn"])
    types["UpdateTransferJobRequestOut"] = t.struct(
        {
            "transferJob": t.proxy(renames["TransferJobOut"]),
            "projectId": t.string(),
            "updateTransferJobFieldMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTransferJobRequestOut"])

    functions = {}
    functions["projectsAgentPoolsGet"] = storagetransfer.post(
        "v1/projects/{projectId}/agentPools",
        t.struct(
            {
                "projectId": t.string(),
                "agentPoolId": t.string(),
                "name": t.string(),
                "bandwidthLimit": t.proxy(renames["BandwidthLimitIn"]).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AgentPoolOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAgentPoolsPatch"] = storagetransfer.post(
        "v1/projects/{projectId}/agentPools",
        t.struct(
            {
                "projectId": t.string(),
                "agentPoolId": t.string(),
                "name": t.string(),
                "bandwidthLimit": t.proxy(renames["BandwidthLimitIn"]).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AgentPoolOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAgentPoolsList"] = storagetransfer.post(
        "v1/projects/{projectId}/agentPools",
        t.struct(
            {
                "projectId": t.string(),
                "agentPoolId": t.string(),
                "name": t.string(),
                "bandwidthLimit": t.proxy(renames["BandwidthLimitIn"]).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AgentPoolOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAgentPoolsDelete"] = storagetransfer.post(
        "v1/projects/{projectId}/agentPools",
        t.struct(
            {
                "projectId": t.string(),
                "agentPoolId": t.string(),
                "name": t.string(),
                "bandwidthLimit": t.proxy(renames["BandwidthLimitIn"]).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AgentPoolOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAgentPoolsCreate"] = storagetransfer.post(
        "v1/projects/{projectId}/agentPools",
        t.struct(
            {
                "projectId": t.string(),
                "agentPoolId": t.string(),
                "name": t.string(),
                "bandwidthLimit": t.proxy(renames["BandwidthLimitIn"]).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AgentPoolOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["transferOperationsGet"] = storagetransfer.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["transferOperationsResume"] = storagetransfer.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["transferOperationsPause"] = storagetransfer.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["transferOperationsCancel"] = storagetransfer.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["transferOperationsList"] = storagetransfer.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["transferJobsList"] = storagetransfer.delete(
        "v1/{jobName}",
        t.struct(
            {
                "jobName": t.string(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["transferJobsGet"] = storagetransfer.delete(
        "v1/{jobName}",
        t.struct(
            {
                "jobName": t.string(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["transferJobsCreate"] = storagetransfer.delete(
        "v1/{jobName}",
        t.struct(
            {
                "jobName": t.string(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["transferJobsPatch"] = storagetransfer.delete(
        "v1/{jobName}",
        t.struct(
            {
                "jobName": t.string(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["transferJobsRun"] = storagetransfer.delete(
        "v1/{jobName}",
        t.struct(
            {
                "jobName": t.string(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["transferJobsDelete"] = storagetransfer.delete(
        "v1/{jobName}",
        t.struct(
            {
                "jobName": t.string(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["googleServiceAccountsGet"] = storagetransfer.get(
        "v1/googleServiceAccounts/{projectId}",
        t.struct({"projectId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleServiceAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="storagetransfer",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
