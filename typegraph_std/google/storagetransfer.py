from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_storagetransfer() -> Import:
    storagetransfer = HTTPRuntime("https://storagetransfer.googleapis.com/")

    renames = {
        "ErrorResponse": "_storagetransfer_1_ErrorResponse",
        "HttpDataIn": "_storagetransfer_2_HttpDataIn",
        "HttpDataOut": "_storagetransfer_3_HttpDataOut",
        "TimeOfDayIn": "_storagetransfer_4_TimeOfDayIn",
        "TimeOfDayOut": "_storagetransfer_5_TimeOfDayOut",
        "TransferOperationIn": "_storagetransfer_6_TransferOperationIn",
        "TransferOperationOut": "_storagetransfer_7_TransferOperationOut",
        "CancelOperationRequestIn": "_storagetransfer_8_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_storagetransfer_9_CancelOperationRequestOut",
        "AwsAccessKeyIn": "_storagetransfer_10_AwsAccessKeyIn",
        "AwsAccessKeyOut": "_storagetransfer_11_AwsAccessKeyOut",
        "AzureBlobStorageDataIn": "_storagetransfer_12_AzureBlobStorageDataIn",
        "AzureBlobStorageDataOut": "_storagetransfer_13_AzureBlobStorageDataOut",
        "S3CompatibleMetadataIn": "_storagetransfer_14_S3CompatibleMetadataIn",
        "S3CompatibleMetadataOut": "_storagetransfer_15_S3CompatibleMetadataOut",
        "TransferJobIn": "_storagetransfer_16_TransferJobIn",
        "TransferJobOut": "_storagetransfer_17_TransferJobOut",
        "ObjectConditionsIn": "_storagetransfer_18_ObjectConditionsIn",
        "ObjectConditionsOut": "_storagetransfer_19_ObjectConditionsOut",
        "AgentPoolIn": "_storagetransfer_20_AgentPoolIn",
        "AgentPoolOut": "_storagetransfer_21_AgentPoolOut",
        "RunTransferJobRequestIn": "_storagetransfer_22_RunTransferJobRequestIn",
        "RunTransferJobRequestOut": "_storagetransfer_23_RunTransferJobRequestOut",
        "ErrorLogEntryIn": "_storagetransfer_24_ErrorLogEntryIn",
        "ErrorLogEntryOut": "_storagetransfer_25_ErrorLogEntryOut",
        "NotificationConfigIn": "_storagetransfer_26_NotificationConfigIn",
        "NotificationConfigOut": "_storagetransfer_27_NotificationConfigOut",
        "ErrorSummaryIn": "_storagetransfer_28_ErrorSummaryIn",
        "ErrorSummaryOut": "_storagetransfer_29_ErrorSummaryOut",
        "GcsDataIn": "_storagetransfer_30_GcsDataIn",
        "GcsDataOut": "_storagetransfer_31_GcsDataOut",
        "PosixFilesystemIn": "_storagetransfer_32_PosixFilesystemIn",
        "PosixFilesystemOut": "_storagetransfer_33_PosixFilesystemOut",
        "ListAgentPoolsResponseIn": "_storagetransfer_34_ListAgentPoolsResponseIn",
        "ListAgentPoolsResponseOut": "_storagetransfer_35_ListAgentPoolsResponseOut",
        "MetadataOptionsIn": "_storagetransfer_36_MetadataOptionsIn",
        "MetadataOptionsOut": "_storagetransfer_37_MetadataOptionsOut",
        "ListTransferJobsResponseIn": "_storagetransfer_38_ListTransferJobsResponseIn",
        "ListTransferJobsResponseOut": "_storagetransfer_39_ListTransferJobsResponseOut",
        "EventStreamIn": "_storagetransfer_40_EventStreamIn",
        "EventStreamOut": "_storagetransfer_41_EventStreamOut",
        "ListOperationsResponseIn": "_storagetransfer_42_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_storagetransfer_43_ListOperationsResponseOut",
        "GoogleServiceAccountIn": "_storagetransfer_44_GoogleServiceAccountIn",
        "GoogleServiceAccountOut": "_storagetransfer_45_GoogleServiceAccountOut",
        "StatusIn": "_storagetransfer_46_StatusIn",
        "StatusOut": "_storagetransfer_47_StatusOut",
        "TransferManifestIn": "_storagetransfer_48_TransferManifestIn",
        "TransferManifestOut": "_storagetransfer_49_TransferManifestOut",
        "DateIn": "_storagetransfer_50_DateIn",
        "DateOut": "_storagetransfer_51_DateOut",
        "AwsS3CompatibleDataIn": "_storagetransfer_52_AwsS3CompatibleDataIn",
        "AwsS3CompatibleDataOut": "_storagetransfer_53_AwsS3CompatibleDataOut",
        "AwsS3DataIn": "_storagetransfer_54_AwsS3DataIn",
        "AwsS3DataOut": "_storagetransfer_55_AwsS3DataOut",
        "TransferSpecIn": "_storagetransfer_56_TransferSpecIn",
        "TransferSpecOut": "_storagetransfer_57_TransferSpecOut",
        "LoggingConfigIn": "_storagetransfer_58_LoggingConfigIn",
        "LoggingConfigOut": "_storagetransfer_59_LoggingConfigOut",
        "UpdateTransferJobRequestIn": "_storagetransfer_60_UpdateTransferJobRequestIn",
        "UpdateTransferJobRequestOut": "_storagetransfer_61_UpdateTransferJobRequestOut",
        "ScheduleIn": "_storagetransfer_62_ScheduleIn",
        "ScheduleOut": "_storagetransfer_63_ScheduleOut",
        "BandwidthLimitIn": "_storagetransfer_64_BandwidthLimitIn",
        "BandwidthLimitOut": "_storagetransfer_65_BandwidthLimitOut",
        "EmptyIn": "_storagetransfer_66_EmptyIn",
        "EmptyOut": "_storagetransfer_67_EmptyOut",
        "TransferCountersIn": "_storagetransfer_68_TransferCountersIn",
        "TransferCountersOut": "_storagetransfer_69_TransferCountersOut",
        "AzureCredentialsIn": "_storagetransfer_70_AzureCredentialsIn",
        "AzureCredentialsOut": "_storagetransfer_71_AzureCredentialsOut",
        "PauseTransferOperationRequestIn": "_storagetransfer_72_PauseTransferOperationRequestIn",
        "PauseTransferOperationRequestOut": "_storagetransfer_73_PauseTransferOperationRequestOut",
        "OperationIn": "_storagetransfer_74_OperationIn",
        "OperationOut": "_storagetransfer_75_OperationOut",
        "ResumeTransferOperationRequestIn": "_storagetransfer_76_ResumeTransferOperationRequestIn",
        "ResumeTransferOperationRequestOut": "_storagetransfer_77_ResumeTransferOperationRequestOut",
        "TransferOptionsIn": "_storagetransfer_78_TransferOptionsIn",
        "TransferOptionsOut": "_storagetransfer_79_TransferOptionsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["HttpDataIn"] = t.struct({"listUrl": t.string()}).named(renames["HttpDataIn"])
    types["HttpDataOut"] = t.struct(
        {"listUrl": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["HttpDataOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["TransferOperationIn"] = t.struct(
        {
            "counters": t.proxy(renames["TransferCountersIn"]).optional(),
            "transferJobName": t.string().optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "transferSpec": t.proxy(renames["TransferSpecIn"]).optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "status": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "notificationConfig": t.proxy(renames["NotificationConfigIn"]).optional(),
            "errorBreakdowns": t.array(t.proxy(renames["ErrorSummaryIn"])).optional(),
        }
    ).named(renames["TransferOperationIn"])
    types["TransferOperationOut"] = t.struct(
        {
            "counters": t.proxy(renames["TransferCountersOut"]).optional(),
            "transferJobName": t.string().optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "transferSpec": t.proxy(renames["TransferSpecOut"]).optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "status": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "notificationConfig": t.proxy(renames["NotificationConfigOut"]).optional(),
            "errorBreakdowns": t.array(t.proxy(renames["ErrorSummaryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferOperationOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["AzureBlobStorageDataIn"] = t.struct(
        {
            "azureCredentials": t.proxy(renames["AzureCredentialsIn"]),
            "path": t.string().optional(),
            "container": t.string(),
            "storageAccount": t.string(),
        }
    ).named(renames["AzureBlobStorageDataIn"])
    types["AzureBlobStorageDataOut"] = t.struct(
        {
            "azureCredentials": t.proxy(renames["AzureCredentialsOut"]),
            "path": t.string().optional(),
            "container": t.string(),
            "storageAccount": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AzureBlobStorageDataOut"])
    types["S3CompatibleMetadataIn"] = t.struct(
        {
            "requestModel": t.string().optional(),
            "protocol": t.string().optional(),
            "listApi": t.string().optional(),
            "authMethod": t.string().optional(),
        }
    ).named(renames["S3CompatibleMetadataIn"])
    types["S3CompatibleMetadataOut"] = t.struct(
        {
            "requestModel": t.string().optional(),
            "protocol": t.string().optional(),
            "listApi": t.string().optional(),
            "authMethod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["S3CompatibleMetadataOut"])
    types["TransferJobIn"] = t.struct(
        {
            "description": t.string().optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "schedule": t.proxy(renames["ScheduleIn"]).optional(),
            "status": t.string().optional(),
            "transferSpec": t.proxy(renames["TransferSpecIn"]).optional(),
            "projectId": t.string().optional(),
            "latestOperationName": t.string().optional(),
            "name": t.string().optional(),
            "notificationConfig": t.proxy(renames["NotificationConfigIn"]).optional(),
            "eventStream": t.proxy(renames["EventStreamIn"]).optional(),
        }
    ).named(renames["TransferJobIn"])
    types["TransferJobOut"] = t.struct(
        {
            "deletionTime": t.string().optional(),
            "description": t.string().optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "schedule": t.proxy(renames["ScheduleOut"]).optional(),
            "status": t.string().optional(),
            "transferSpec": t.proxy(renames["TransferSpecOut"]).optional(),
            "creationTime": t.string().optional(),
            "projectId": t.string().optional(),
            "latestOperationName": t.string().optional(),
            "lastModificationTime": t.string().optional(),
            "name": t.string().optional(),
            "notificationConfig": t.proxy(renames["NotificationConfigOut"]).optional(),
            "eventStream": t.proxy(renames["EventStreamOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferJobOut"])
    types["ObjectConditionsIn"] = t.struct(
        {
            "includePrefixes": t.array(t.string()).optional(),
            "lastModifiedBefore": t.string().optional(),
            "lastModifiedSince": t.string().optional(),
            "minTimeElapsedSinceLastModification": t.string().optional(),
            "maxTimeElapsedSinceLastModification": t.string().optional(),
            "excludePrefixes": t.array(t.string()).optional(),
        }
    ).named(renames["ObjectConditionsIn"])
    types["ObjectConditionsOut"] = t.struct(
        {
            "includePrefixes": t.array(t.string()).optional(),
            "lastModifiedBefore": t.string().optional(),
            "lastModifiedSince": t.string().optional(),
            "minTimeElapsedSinceLastModification": t.string().optional(),
            "maxTimeElapsedSinceLastModification": t.string().optional(),
            "excludePrefixes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectConditionsOut"])
    types["AgentPoolIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string(),
            "bandwidthLimit": t.proxy(renames["BandwidthLimitIn"]).optional(),
        }
    ).named(renames["AgentPoolIn"])
    types["AgentPoolOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string(),
            "bandwidthLimit": t.proxy(renames["BandwidthLimitOut"]).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentPoolOut"])
    types["RunTransferJobRequestIn"] = t.struct({"projectId": t.string()}).named(
        renames["RunTransferJobRequestIn"]
    )
    types["RunTransferJobRequestOut"] = t.struct(
        {"projectId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RunTransferJobRequestOut"])
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
    types["NotificationConfigIn"] = t.struct(
        {
            "pubsubTopic": t.string(),
            "eventTypes": t.array(t.string()).optional(),
            "payloadFormat": t.string(),
        }
    ).named(renames["NotificationConfigIn"])
    types["NotificationConfigOut"] = t.struct(
        {
            "pubsubTopic": t.string(),
            "eventTypes": t.array(t.string()).optional(),
            "payloadFormat": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationConfigOut"])
    types["ErrorSummaryIn"] = t.struct(
        {
            "errorLogEntries": t.array(t.proxy(renames["ErrorLogEntryIn"])).optional(),
            "errorCode": t.string(),
            "errorCount": t.string(),
        }
    ).named(renames["ErrorSummaryIn"])
    types["ErrorSummaryOut"] = t.struct(
        {
            "errorLogEntries": t.array(t.proxy(renames["ErrorLogEntryOut"])).optional(),
            "errorCode": t.string(),
            "errorCount": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorSummaryOut"])
    types["GcsDataIn"] = t.struct(
        {"bucketName": t.string(), "path": t.string().optional()}
    ).named(renames["GcsDataIn"])
    types["GcsDataOut"] = t.struct(
        {
            "bucketName": t.string(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsDataOut"])
    types["PosixFilesystemIn"] = t.struct(
        {"rootDirectory": t.string().optional()}
    ).named(renames["PosixFilesystemIn"])
    types["PosixFilesystemOut"] = t.struct(
        {
            "rootDirectory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosixFilesystemOut"])
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
    types["MetadataOptionsIn"] = t.struct(
        {
            "storageClass": t.string().optional(),
            "gid": t.string().optional(),
            "acl": t.string().optional(),
            "symlink": t.string().optional(),
            "timeCreated": t.string().optional(),
            "mode": t.string().optional(),
            "temporaryHold": t.string().optional(),
            "kmsKey": t.string().optional(),
            "uid": t.string().optional(),
        }
    ).named(renames["MetadataOptionsIn"])
    types["MetadataOptionsOut"] = t.struct(
        {
            "storageClass": t.string().optional(),
            "gid": t.string().optional(),
            "acl": t.string().optional(),
            "symlink": t.string().optional(),
            "timeCreated": t.string().optional(),
            "mode": t.string().optional(),
            "temporaryHold": t.string().optional(),
            "kmsKey": t.string().optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOptionsOut"])
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
    types["EventStreamIn"] = t.struct(
        {
            "eventStreamExpirationTime": t.string().optional(),
            "name": t.string(),
            "eventStreamStartTime": t.string().optional(),
        }
    ).named(renames["EventStreamIn"])
    types["EventStreamOut"] = t.struct(
        {
            "eventStreamExpirationTime": t.string().optional(),
            "name": t.string(),
            "eventStreamStartTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventStreamOut"])
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
    types["GoogleServiceAccountIn"] = t.struct(
        {"accountEmail": t.string().optional(), "subjectId": t.string().optional()}
    ).named(renames["GoogleServiceAccountIn"])
    types["GoogleServiceAccountOut"] = t.struct(
        {
            "accountEmail": t.string().optional(),
            "subjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleServiceAccountOut"])
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
    types["TransferManifestIn"] = t.struct({"location": t.string().optional()}).named(
        renames["TransferManifestIn"]
    )
    types["TransferManifestOut"] = t.struct(
        {
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferManifestOut"])
    types["DateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["AwsS3CompatibleDataIn"] = t.struct(
        {
            "endpoint": t.string(),
            "path": t.string().optional(),
            "s3Metadata": t.proxy(renames["S3CompatibleMetadataIn"]).optional(),
            "region": t.string().optional(),
            "bucketName": t.string(),
        }
    ).named(renames["AwsS3CompatibleDataIn"])
    types["AwsS3CompatibleDataOut"] = t.struct(
        {
            "endpoint": t.string(),
            "path": t.string().optional(),
            "s3Metadata": t.proxy(renames["S3CompatibleMetadataOut"]).optional(),
            "region": t.string().optional(),
            "bucketName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AwsS3CompatibleDataOut"])
    types["AwsS3DataIn"] = t.struct(
        {
            "awsAccessKey": t.proxy(renames["AwsAccessKeyIn"]).optional(),
            "bucketName": t.string(),
            "roleArn": t.string().optional(),
            "path": t.string().optional(),
        }
    ).named(renames["AwsS3DataIn"])
    types["AwsS3DataOut"] = t.struct(
        {
            "awsAccessKey": t.proxy(renames["AwsAccessKeyOut"]).optional(),
            "bucketName": t.string(),
            "roleArn": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AwsS3DataOut"])
    types["TransferSpecIn"] = t.struct(
        {
            "awsS3DataSource": t.proxy(renames["AwsS3DataIn"]).optional(),
            "gcsIntermediateDataLocation": t.proxy(renames["GcsDataIn"]).optional(),
            "posixDataSource": t.proxy(renames["PosixFilesystemIn"]).optional(),
            "transferOptions": t.proxy(renames["TransferOptionsIn"]).optional(),
            "azureBlobStorageDataSource": t.proxy(
                renames["AzureBlobStorageDataIn"]
            ).optional(),
            "objectConditions": t.proxy(renames["ObjectConditionsIn"]).optional(),
            "awsS3CompatibleDataSource": t.proxy(
                renames["AwsS3CompatibleDataIn"]
            ).optional(),
            "sourceAgentPoolName": t.string().optional(),
            "sinkAgentPoolName": t.string().optional(),
            "transferManifest": t.proxy(renames["TransferManifestIn"]).optional(),
            "gcsDataSink": t.proxy(renames["GcsDataIn"]).optional(),
            "httpDataSource": t.proxy(renames["HttpDataIn"]).optional(),
            "gcsDataSource": t.proxy(renames["GcsDataIn"]).optional(),
            "posixDataSink": t.proxy(renames["PosixFilesystemIn"]).optional(),
        }
    ).named(renames["TransferSpecIn"])
    types["TransferSpecOut"] = t.struct(
        {
            "awsS3DataSource": t.proxy(renames["AwsS3DataOut"]).optional(),
            "gcsIntermediateDataLocation": t.proxy(renames["GcsDataOut"]).optional(),
            "posixDataSource": t.proxy(renames["PosixFilesystemOut"]).optional(),
            "transferOptions": t.proxy(renames["TransferOptionsOut"]).optional(),
            "azureBlobStorageDataSource": t.proxy(
                renames["AzureBlobStorageDataOut"]
            ).optional(),
            "objectConditions": t.proxy(renames["ObjectConditionsOut"]).optional(),
            "awsS3CompatibleDataSource": t.proxy(
                renames["AwsS3CompatibleDataOut"]
            ).optional(),
            "sourceAgentPoolName": t.string().optional(),
            "sinkAgentPoolName": t.string().optional(),
            "transferManifest": t.proxy(renames["TransferManifestOut"]).optional(),
            "gcsDataSink": t.proxy(renames["GcsDataOut"]).optional(),
            "httpDataSource": t.proxy(renames["HttpDataOut"]).optional(),
            "gcsDataSource": t.proxy(renames["GcsDataOut"]).optional(),
            "posixDataSink": t.proxy(renames["PosixFilesystemOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferSpecOut"])
    types["LoggingConfigIn"] = t.struct(
        {
            "enableOnpremGcsTransferLogs": t.boolean().optional(),
            "logActionStates": t.array(t.string()).optional(),
            "logActions": t.array(t.string()).optional(),
        }
    ).named(renames["LoggingConfigIn"])
    types["LoggingConfigOut"] = t.struct(
        {
            "enableOnpremGcsTransferLogs": t.boolean().optional(),
            "logActionStates": t.array(t.string()).optional(),
            "logActions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoggingConfigOut"])
    types["UpdateTransferJobRequestIn"] = t.struct(
        {
            "transferJob": t.proxy(renames["TransferJobIn"]),
            "updateTransferJobFieldMask": t.string().optional(),
            "projectId": t.string(),
        }
    ).named(renames["UpdateTransferJobRequestIn"])
    types["UpdateTransferJobRequestOut"] = t.struct(
        {
            "transferJob": t.proxy(renames["TransferJobOut"]),
            "updateTransferJobFieldMask": t.string().optional(),
            "projectId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTransferJobRequestOut"])
    types["ScheduleIn"] = t.struct(
        {
            "repeatInterval": t.string().optional(),
            "scheduleEndDate": t.proxy(renames["DateIn"]).optional(),
            "scheduleStartDate": t.proxy(renames["DateIn"]),
            "startTimeOfDay": t.proxy(renames["TimeOfDayIn"]).optional(),
            "endTimeOfDay": t.proxy(renames["TimeOfDayIn"]).optional(),
        }
    ).named(renames["ScheduleIn"])
    types["ScheduleOut"] = t.struct(
        {
            "repeatInterval": t.string().optional(),
            "scheduleEndDate": t.proxy(renames["DateOut"]).optional(),
            "scheduleStartDate": t.proxy(renames["DateOut"]),
            "startTimeOfDay": t.proxy(renames["TimeOfDayOut"]).optional(),
            "endTimeOfDay": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduleOut"])
    types["BandwidthLimitIn"] = t.struct({"limitMbps": t.string().optional()}).named(
        renames["BandwidthLimitIn"]
    )
    types["BandwidthLimitOut"] = t.struct(
        {
            "limitMbps": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BandwidthLimitOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["TransferCountersIn"] = t.struct(
        {
            "objectsFoundOnlyFromSink": t.string().optional(),
            "objectsFromSourceFailed": t.string().optional(),
            "bytesDeletedFromSink": t.string().optional(),
            "bytesDeletedFromSource": t.string().optional(),
            "intermediateObjectsFailedCleanedUp": t.string().optional(),
            "objectsDeletedFromSink": t.string().optional(),
            "bytesFailedToDeleteFromSink": t.string().optional(),
            "bytesFromSourceFailed": t.string().optional(),
            "objectsFailedToDeleteFromSink": t.string().optional(),
            "objectsDeletedFromSource": t.string().optional(),
            "objectsFoundFromSource": t.string().optional(),
            "objectsFromSourceSkippedBySync": t.string().optional(),
            "bytesFoundOnlyFromSink": t.string().optional(),
            "objectsCopiedToSink": t.string().optional(),
            "bytesCopiedToSink": t.string().optional(),
            "directoriesFoundFromSource": t.string().optional(),
            "bytesFromSourceSkippedBySync": t.string().optional(),
            "directoriesFailedToListFromSource": t.string().optional(),
            "directoriesSuccessfullyListedFromSource": t.string().optional(),
            "intermediateObjectsCleanedUp": t.string().optional(),
            "bytesFoundFromSource": t.string().optional(),
        }
    ).named(renames["TransferCountersIn"])
    types["TransferCountersOut"] = t.struct(
        {
            "objectsFoundOnlyFromSink": t.string().optional(),
            "objectsFromSourceFailed": t.string().optional(),
            "bytesDeletedFromSink": t.string().optional(),
            "bytesDeletedFromSource": t.string().optional(),
            "intermediateObjectsFailedCleanedUp": t.string().optional(),
            "objectsDeletedFromSink": t.string().optional(),
            "bytesFailedToDeleteFromSink": t.string().optional(),
            "bytesFromSourceFailed": t.string().optional(),
            "objectsFailedToDeleteFromSink": t.string().optional(),
            "objectsDeletedFromSource": t.string().optional(),
            "objectsFoundFromSource": t.string().optional(),
            "objectsFromSourceSkippedBySync": t.string().optional(),
            "bytesFoundOnlyFromSink": t.string().optional(),
            "objectsCopiedToSink": t.string().optional(),
            "bytesCopiedToSink": t.string().optional(),
            "directoriesFoundFromSource": t.string().optional(),
            "bytesFromSourceSkippedBySync": t.string().optional(),
            "directoriesFailedToListFromSource": t.string().optional(),
            "directoriesSuccessfullyListedFromSource": t.string().optional(),
            "intermediateObjectsCleanedUp": t.string().optional(),
            "bytesFoundFromSource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferCountersOut"])
    types["AzureCredentialsIn"] = t.struct({"sasToken": t.string()}).named(
        renames["AzureCredentialsIn"]
    )
    types["AzureCredentialsOut"] = t.struct(
        {"sasToken": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AzureCredentialsOut"])
    types["PauseTransferOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["PauseTransferOperationRequestIn"])
    types["PauseTransferOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PauseTransferOperationRequestOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["ResumeTransferOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ResumeTransferOperationRequestIn"])
    types["ResumeTransferOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumeTransferOperationRequestOut"])
    types["TransferOptionsIn"] = t.struct(
        {
            "overwriteWhen": t.string().optional(),
            "overwriteObjectsAlreadyExistingInSink": t.boolean().optional(),
            "deleteObjectsUniqueInSink": t.boolean().optional(),
            "metadataOptions": t.proxy(renames["MetadataOptionsIn"]).optional(),
            "deleteObjectsFromSourceAfterTransfer": t.boolean().optional(),
        }
    ).named(renames["TransferOptionsIn"])
    types["TransferOptionsOut"] = t.struct(
        {
            "overwriteWhen": t.string().optional(),
            "overwriteObjectsAlreadyExistingInSink": t.boolean().optional(),
            "deleteObjectsUniqueInSink": t.boolean().optional(),
            "metadataOptions": t.proxy(renames["MetadataOptionsOut"]).optional(),
            "deleteObjectsFromSourceAfterTransfer": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferOptionsOut"])

    functions = {}
    functions["transferJobsDelete"] = storagetransfer.post(
        "v1/{jobName}:run",
        t.struct(
            {
                "jobName": t.string(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["transferJobsCreate"] = storagetransfer.post(
        "v1/{jobName}:run",
        t.struct(
            {
                "jobName": t.string(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["transferJobsList"] = storagetransfer.post(
        "v1/{jobName}:run",
        t.struct(
            {
                "jobName": t.string(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["transferJobsGet"] = storagetransfer.post(
        "v1/{jobName}:run",
        t.struct(
            {
                "jobName": t.string(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["transferJobsPatch"] = storagetransfer.post(
        "v1/{jobName}:run",
        t.struct(
            {
                "jobName": t.string(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["transferJobsRun"] = storagetransfer.post(
        "v1/{jobName}:run",
        t.struct(
            {
                "jobName": t.string(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAgentPoolsDelete"] = storagetransfer.post(
        "v1/projects/{projectId}/agentPools",
        t.struct(
            {
                "projectId": t.string(),
                "agentPoolId": t.string(),
                "displayName": t.string().optional(),
                "name": t.string(),
                "bandwidthLimit": t.proxy(renames["BandwidthLimitIn"]).optional(),
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
                "displayName": t.string().optional(),
                "name": t.string(),
                "bandwidthLimit": t.proxy(renames["BandwidthLimitIn"]).optional(),
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
                "displayName": t.string().optional(),
                "name": t.string(),
                "bandwidthLimit": t.proxy(renames["BandwidthLimitIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AgentPoolOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAgentPoolsGet"] = storagetransfer.post(
        "v1/projects/{projectId}/agentPools",
        t.struct(
            {
                "projectId": t.string(),
                "agentPoolId": t.string(),
                "displayName": t.string().optional(),
                "name": t.string(),
                "bandwidthLimit": t.proxy(renames["BandwidthLimitIn"]).optional(),
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
                "displayName": t.string().optional(),
                "name": t.string(),
                "bandwidthLimit": t.proxy(renames["BandwidthLimitIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AgentPoolOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["transferOperationsGet"] = storagetransfer.post(
        "v1/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["transferOperationsList"] = storagetransfer.post(
        "v1/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["transferOperationsPause"] = storagetransfer.post(
        "v1/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["transferOperationsCancel"] = storagetransfer.post(
        "v1/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["transferOperationsResume"] = storagetransfer.post(
        "v1/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
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
