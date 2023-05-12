from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_logging() -> Import:
    logging = HTTPRuntime("https://logging.googleapis.com/")

    renames = {
        "ErrorResponse": "_logging_1_ErrorResponse",
        "MonitoredResourceIn": "_logging_2_MonitoredResourceIn",
        "MonitoredResourceOut": "_logging_3_MonitoredResourceOut",
        "CopyLogEntriesRequestIn": "_logging_4_CopyLogEntriesRequestIn",
        "CopyLogEntriesRequestOut": "_logging_5_CopyLogEntriesRequestOut",
        "LogEntryOperationIn": "_logging_6_LogEntryOperationIn",
        "LogEntryOperationOut": "_logging_7_LogEntryOperationOut",
        "ListBucketsResponseIn": "_logging_8_ListBucketsResponseIn",
        "ListBucketsResponseOut": "_logging_9_ListBucketsResponseOut",
        "WriteLogEntriesRequestIn": "_logging_10_WriteLogEntriesRequestIn",
        "WriteLogEntriesRequestOut": "_logging_11_WriteLogEntriesRequestOut",
        "LocationMetadataIn": "_logging_12_LocationMetadataIn",
        "LocationMetadataOut": "_logging_13_LocationMetadataOut",
        "BigQueryDatasetIn": "_logging_14_BigQueryDatasetIn",
        "BigQueryDatasetOut": "_logging_15_BigQueryDatasetOut",
        "SourceReferenceIn": "_logging_16_SourceReferenceIn",
        "SourceReferenceOut": "_logging_17_SourceReferenceOut",
        "LinearIn": "_logging_18_LinearIn",
        "LinearOut": "_logging_19_LinearOut",
        "SuppressionInfoIn": "_logging_20_SuppressionInfoIn",
        "SuppressionInfoOut": "_logging_21_SuppressionInfoOut",
        "LinkMetadataIn": "_logging_22_LinkMetadataIn",
        "LinkMetadataOut": "_logging_23_LinkMetadataOut",
        "CreateBucketRequestIn": "_logging_24_CreateBucketRequestIn",
        "CreateBucketRequestOut": "_logging_25_CreateBucketRequestOut",
        "LogExclusionIn": "_logging_26_LogExclusionIn",
        "LogExclusionOut": "_logging_27_LogExclusionOut",
        "DeleteLinkRequestIn": "_logging_28_DeleteLinkRequestIn",
        "DeleteLinkRequestOut": "_logging_29_DeleteLinkRequestOut",
        "ListLogMetricsResponseIn": "_logging_30_ListLogMetricsResponseIn",
        "ListLogMetricsResponseOut": "_logging_31_ListLogMetricsResponseOut",
        "LogLineIn": "_logging_32_LogLineIn",
        "LogLineOut": "_logging_33_LogLineOut",
        "ExponentialIn": "_logging_34_ExponentialIn",
        "ExponentialOut": "_logging_35_ExponentialOut",
        "LogSplitIn": "_logging_36_LogSplitIn",
        "LogSplitOut": "_logging_37_LogSplitOut",
        "ExplicitIn": "_logging_38_ExplicitIn",
        "ExplicitOut": "_logging_39_ExplicitOut",
        "CopyLogEntriesResponseIn": "_logging_40_CopyLogEntriesResponseIn",
        "CopyLogEntriesResponseOut": "_logging_41_CopyLogEntriesResponseOut",
        "ListOperationsResponseIn": "_logging_42_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_logging_43_ListOperationsResponseOut",
        "LogViewIn": "_logging_44_LogViewIn",
        "LogViewOut": "_logging_45_LogViewOut",
        "MonitoredResourceMetadataIn": "_logging_46_MonitoredResourceMetadataIn",
        "MonitoredResourceMetadataOut": "_logging_47_MonitoredResourceMetadataOut",
        "ListLogEntriesRequestIn": "_logging_48_ListLogEntriesRequestIn",
        "ListLogEntriesRequestOut": "_logging_49_ListLogEntriesRequestOut",
        "BucketOptionsIn": "_logging_50_BucketOptionsIn",
        "BucketOptionsOut": "_logging_51_BucketOptionsOut",
        "LogSinkIn": "_logging_52_LogSinkIn",
        "LogSinkOut": "_logging_53_LogSinkOut",
        "LogEntryIn": "_logging_54_LogEntryIn",
        "LogEntryOut": "_logging_55_LogEntryOut",
        "MonitoredResourceDescriptorIn": "_logging_56_MonitoredResourceDescriptorIn",
        "MonitoredResourceDescriptorOut": "_logging_57_MonitoredResourceDescriptorOut",
        "UpdateBucketRequestIn": "_logging_58_UpdateBucketRequestIn",
        "UpdateBucketRequestOut": "_logging_59_UpdateBucketRequestOut",
        "LinkIn": "_logging_60_LinkIn",
        "LinkOut": "_logging_61_LinkOut",
        "WriteLogEntriesResponseIn": "_logging_62_WriteLogEntriesResponseIn",
        "WriteLogEntriesResponseOut": "_logging_63_WriteLogEntriesResponseOut",
        "LabelDescriptorIn": "_logging_64_LabelDescriptorIn",
        "LabelDescriptorOut": "_logging_65_LabelDescriptorOut",
        "ListSinksResponseIn": "_logging_66_ListSinksResponseIn",
        "ListSinksResponseOut": "_logging_67_ListSinksResponseOut",
        "IndexConfigIn": "_logging_68_IndexConfigIn",
        "IndexConfigOut": "_logging_69_IndexConfigOut",
        "BigQueryOptionsIn": "_logging_70_BigQueryOptionsIn",
        "BigQueryOptionsOut": "_logging_71_BigQueryOptionsOut",
        "LocationIn": "_logging_72_LocationIn",
        "LocationOut": "_logging_73_LocationOut",
        "MetricDescriptorMetadataIn": "_logging_74_MetricDescriptorMetadataIn",
        "MetricDescriptorMetadataOut": "_logging_75_MetricDescriptorMetadataOut",
        "ListLocationsResponseIn": "_logging_76_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_logging_77_ListLocationsResponseOut",
        "OperationIn": "_logging_78_OperationIn",
        "OperationOut": "_logging_79_OperationOut",
        "ListLogsResponseIn": "_logging_80_ListLogsResponseIn",
        "ListLogsResponseOut": "_logging_81_ListLogsResponseOut",
        "LogMetricIn": "_logging_82_LogMetricIn",
        "LogMetricOut": "_logging_83_LogMetricOut",
        "RequestLogIn": "_logging_84_RequestLogIn",
        "RequestLogOut": "_logging_85_RequestLogOut",
        "SourceLocationIn": "_logging_86_SourceLocationIn",
        "SourceLocationOut": "_logging_87_SourceLocationOut",
        "CreateLinkRequestIn": "_logging_88_CreateLinkRequestIn",
        "CreateLinkRequestOut": "_logging_89_CreateLinkRequestOut",
        "CopyLogEntriesMetadataIn": "_logging_90_CopyLogEntriesMetadataIn",
        "CopyLogEntriesMetadataOut": "_logging_91_CopyLogEntriesMetadataOut",
        "ListMonitoredResourceDescriptorsResponseIn": "_logging_92_ListMonitoredResourceDescriptorsResponseIn",
        "ListMonitoredResourceDescriptorsResponseOut": "_logging_93_ListMonitoredResourceDescriptorsResponseOut",
        "LogEntrySourceLocationIn": "_logging_94_LogEntrySourceLocationIn",
        "LogEntrySourceLocationOut": "_logging_95_LogEntrySourceLocationOut",
        "SettingsIn": "_logging_96_SettingsIn",
        "SettingsOut": "_logging_97_SettingsOut",
        "CmekSettingsIn": "_logging_98_CmekSettingsIn",
        "CmekSettingsOut": "_logging_99_CmekSettingsOut",
        "BucketMetadataIn": "_logging_100_BucketMetadataIn",
        "BucketMetadataOut": "_logging_101_BucketMetadataOut",
        "ListLinksResponseIn": "_logging_102_ListLinksResponseIn",
        "ListLinksResponseOut": "_logging_103_ListLinksResponseOut",
        "ListExclusionsResponseIn": "_logging_104_ListExclusionsResponseIn",
        "ListExclusionsResponseOut": "_logging_105_ListExclusionsResponseOut",
        "EmptyIn": "_logging_106_EmptyIn",
        "EmptyOut": "_logging_107_EmptyOut",
        "TailLogEntriesRequestIn": "_logging_108_TailLogEntriesRequestIn",
        "TailLogEntriesRequestOut": "_logging_109_TailLogEntriesRequestOut",
        "StatusIn": "_logging_110_StatusIn",
        "StatusOut": "_logging_111_StatusOut",
        "MetricDescriptorIn": "_logging_112_MetricDescriptorIn",
        "MetricDescriptorOut": "_logging_113_MetricDescriptorOut",
        "CancelOperationRequestIn": "_logging_114_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_logging_115_CancelOperationRequestOut",
        "ListViewsResponseIn": "_logging_116_ListViewsResponseIn",
        "ListViewsResponseOut": "_logging_117_ListViewsResponseOut",
        "TailLogEntriesResponseIn": "_logging_118_TailLogEntriesResponseIn",
        "TailLogEntriesResponseOut": "_logging_119_TailLogEntriesResponseOut",
        "LogBucketIn": "_logging_120_LogBucketIn",
        "LogBucketOut": "_logging_121_LogBucketOut",
        "UndeleteBucketRequestIn": "_logging_122_UndeleteBucketRequestIn",
        "UndeleteBucketRequestOut": "_logging_123_UndeleteBucketRequestOut",
        "ListLogEntriesResponseIn": "_logging_124_ListLogEntriesResponseIn",
        "ListLogEntriesResponseOut": "_logging_125_ListLogEntriesResponseOut",
        "HttpRequestIn": "_logging_126_HttpRequestIn",
        "HttpRequestOut": "_logging_127_HttpRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["MonitoredResourceIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}), "type": t.string()}
    ).named(renames["MonitoredResourceIn"])
    types["MonitoredResourceOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceOut"])
    types["CopyLogEntriesRequestIn"] = t.struct(
        {"destination": t.string(), "name": t.string(), "filter": t.string().optional()}
    ).named(renames["CopyLogEntriesRequestIn"])
    types["CopyLogEntriesRequestOut"] = t.struct(
        {
            "destination": t.string(),
            "name": t.string(),
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyLogEntriesRequestOut"])
    types["LogEntryOperationIn"] = t.struct(
        {
            "id": t.string().optional(),
            "last": t.boolean().optional(),
            "first": t.boolean().optional(),
            "producer": t.string().optional(),
        }
    ).named(renames["LogEntryOperationIn"])
    types["LogEntryOperationOut"] = t.struct(
        {
            "id": t.string().optional(),
            "last": t.boolean().optional(),
            "first": t.boolean().optional(),
            "producer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogEntryOperationOut"])
    types["ListBucketsResponseIn"] = t.struct(
        {
            "buckets": t.array(t.proxy(renames["LogBucketIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListBucketsResponseIn"])
    types["ListBucketsResponseOut"] = t.struct(
        {
            "buckets": t.array(t.proxy(renames["LogBucketOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBucketsResponseOut"])
    types["WriteLogEntriesRequestIn"] = t.struct(
        {
            "dryRun": t.boolean().optional(),
            "entries": t.array(t.proxy(renames["LogEntryIn"])),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "partialSuccess": t.boolean().optional(),
            "logName": t.string().optional(),
            "resource": t.proxy(renames["MonitoredResourceIn"]).optional(),
        }
    ).named(renames["WriteLogEntriesRequestIn"])
    types["WriteLogEntriesRequestOut"] = t.struct(
        {
            "dryRun": t.boolean().optional(),
            "entries": t.array(t.proxy(renames["LogEntryOut"])),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "partialSuccess": t.boolean().optional(),
            "logName": t.string().optional(),
            "resource": t.proxy(renames["MonitoredResourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteLogEntriesRequestOut"])
    types["LocationMetadataIn"] = t.struct(
        {"logAnalyticsEnabled": t.boolean().optional()}
    ).named(renames["LocationMetadataIn"])
    types["LocationMetadataOut"] = t.struct(
        {
            "logAnalyticsEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationMetadataOut"])
    types["BigQueryDatasetIn"] = t.struct({"_": t.string().optional()}).named(
        renames["BigQueryDatasetIn"]
    )
    types["BigQueryDatasetOut"] = t.struct(
        {
            "datasetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryDatasetOut"])
    types["SourceReferenceIn"] = t.struct(
        {"repository": t.string().optional(), "revisionId": t.string().optional()}
    ).named(renames["SourceReferenceIn"])
    types["SourceReferenceOut"] = t.struct(
        {
            "repository": t.string().optional(),
            "revisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceReferenceOut"])
    types["LinearIn"] = t.struct(
        {
            "numFiniteBuckets": t.integer().optional(),
            "width": t.number().optional(),
            "offset": t.number().optional(),
        }
    ).named(renames["LinearIn"])
    types["LinearOut"] = t.struct(
        {
            "numFiniteBuckets": t.integer().optional(),
            "width": t.number().optional(),
            "offset": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinearOut"])
    types["SuppressionInfoIn"] = t.struct(
        {"suppressedCount": t.integer().optional(), "reason": t.string().optional()}
    ).named(renames["SuppressionInfoIn"])
    types["SuppressionInfoOut"] = t.struct(
        {
            "suppressedCount": t.integer().optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuppressionInfoOut"])
    types["LinkMetadataIn"] = t.struct(
        {
            "createLinkRequest": t.proxy(renames["CreateLinkRequestIn"]).optional(),
            "state": t.string().optional(),
            "deleteLinkRequest": t.proxy(renames["DeleteLinkRequestIn"]).optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["LinkMetadataIn"])
    types["LinkMetadataOut"] = t.struct(
        {
            "createLinkRequest": t.proxy(renames["CreateLinkRequestOut"]).optional(),
            "state": t.string().optional(),
            "deleteLinkRequest": t.proxy(renames["DeleteLinkRequestOut"]).optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkMetadataOut"])
    types["CreateBucketRequestIn"] = t.struct(
        {
            "bucketId": t.string(),
            "parent": t.string(),
            "bucket": t.proxy(renames["LogBucketIn"]),
        }
    ).named(renames["CreateBucketRequestIn"])
    types["CreateBucketRequestOut"] = t.struct(
        {
            "bucketId": t.string(),
            "parent": t.string(),
            "bucket": t.proxy(renames["LogBucketOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateBucketRequestOut"])
    types["LogExclusionIn"] = t.struct(
        {
            "filter": t.string(),
            "name": t.string(),
            "disabled": t.boolean().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["LogExclusionIn"])
    types["LogExclusionOut"] = t.struct(
        {
            "filter": t.string(),
            "name": t.string(),
            "disabled": t.boolean().optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogExclusionOut"])
    types["DeleteLinkRequestIn"] = t.struct({"name": t.string()}).named(
        renames["DeleteLinkRequestIn"]
    )
    types["DeleteLinkRequestOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteLinkRequestOut"])
    types["ListLogMetricsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "metrics": t.array(t.proxy(renames["LogMetricIn"])).optional(),
        }
    ).named(renames["ListLogMetricsResponseIn"])
    types["ListLogMetricsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "metrics": t.array(t.proxy(renames["LogMetricOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLogMetricsResponseOut"])
    types["LogLineIn"] = t.struct(
        {
            "logMessage": t.string().optional(),
            "sourceLocation": t.proxy(renames["SourceLocationIn"]).optional(),
            "time": t.string().optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["LogLineIn"])
    types["LogLineOut"] = t.struct(
        {
            "logMessage": t.string().optional(),
            "sourceLocation": t.proxy(renames["SourceLocationOut"]).optional(),
            "time": t.string().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogLineOut"])
    types["ExponentialIn"] = t.struct(
        {
            "scale": t.number().optional(),
            "numFiniteBuckets": t.integer().optional(),
            "growthFactor": t.number().optional(),
        }
    ).named(renames["ExponentialIn"])
    types["ExponentialOut"] = t.struct(
        {
            "scale": t.number().optional(),
            "numFiniteBuckets": t.integer().optional(),
            "growthFactor": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExponentialOut"])
    types["LogSplitIn"] = t.struct(
        {
            "uid": t.string().optional(),
            "index": t.integer().optional(),
            "totalSplits": t.integer().optional(),
        }
    ).named(renames["LogSplitIn"])
    types["LogSplitOut"] = t.struct(
        {
            "uid": t.string().optional(),
            "index": t.integer().optional(),
            "totalSplits": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogSplitOut"])
    types["ExplicitIn"] = t.struct({"bounds": t.array(t.number()).optional()}).named(
        renames["ExplicitIn"]
    )
    types["ExplicitOut"] = t.struct(
        {
            "bounds": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExplicitOut"])
    types["CopyLogEntriesResponseIn"] = t.struct(
        {"logEntriesCopiedCount": t.string().optional()}
    ).named(renames["CopyLogEntriesResponseIn"])
    types["CopyLogEntriesResponseOut"] = t.struct(
        {
            "logEntriesCopiedCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyLogEntriesResponseOut"])
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
    types["LogViewIn"] = t.struct(
        {
            "filter": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["LogViewIn"])
    types["LogViewOut"] = t.struct(
        {
            "filter": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogViewOut"])
    types["MonitoredResourceMetadataIn"] = t.struct(
        {
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "systemLabels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["MonitoredResourceMetadataIn"])
    types["MonitoredResourceMetadataOut"] = t.struct(
        {
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "systemLabels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceMetadataOut"])
    types["ListLogEntriesRequestIn"] = t.struct(
        {
            "filter": t.string().optional(),
            "orderBy": t.string().optional(),
            "pageToken": t.string().optional(),
            "resourceNames": t.array(t.string()),
            "pageSize": t.integer().optional(),
            "projectIds": t.array(t.string()).optional(),
        }
    ).named(renames["ListLogEntriesRequestIn"])
    types["ListLogEntriesRequestOut"] = t.struct(
        {
            "filter": t.string().optional(),
            "orderBy": t.string().optional(),
            "pageToken": t.string().optional(),
            "resourceNames": t.array(t.string()),
            "pageSize": t.integer().optional(),
            "projectIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLogEntriesRequestOut"])
    types["BucketOptionsIn"] = t.struct(
        {
            "linearBuckets": t.proxy(renames["LinearIn"]).optional(),
            "exponentialBuckets": t.proxy(renames["ExponentialIn"]).optional(),
            "explicitBuckets": t.proxy(renames["ExplicitIn"]).optional(),
        }
    ).named(renames["BucketOptionsIn"])
    types["BucketOptionsOut"] = t.struct(
        {
            "linearBuckets": t.proxy(renames["LinearOut"]).optional(),
            "exponentialBuckets": t.proxy(renames["ExponentialOut"]).optional(),
            "explicitBuckets": t.proxy(renames["ExplicitOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BucketOptionsOut"])
    types["LogSinkIn"] = t.struct(
        {
            "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
            "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
            "includeChildren": t.boolean().optional(),
            "disabled": t.boolean().optional(),
            "destination": t.string(),
            "description": t.string().optional(),
            "outputVersionFormat": t.string().optional(),
            "name": t.string(),
            "filter": t.string().optional(),
        }
    ).named(renames["LogSinkIn"])
    types["LogSinkOut"] = t.struct(
        {
            "exclusions": t.array(t.proxy(renames["LogExclusionOut"])).optional(),
            "bigqueryOptions": t.proxy(renames["BigQueryOptionsOut"]).optional(),
            "includeChildren": t.boolean().optional(),
            "disabled": t.boolean().optional(),
            "destination": t.string(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "writerIdentity": t.string().optional(),
            "description": t.string().optional(),
            "outputVersionFormat": t.string().optional(),
            "name": t.string(),
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogSinkOut"])
    types["LogEntryIn"] = t.struct(
        {
            "insertId": t.string().optional(),
            "httpRequest": t.proxy(renames["HttpRequestIn"]).optional(),
            "logName": t.string(),
            "operation": t.proxy(renames["LogEntryOperationIn"]).optional(),
            "sourceLocation": t.proxy(renames["LogEntrySourceLocationIn"]).optional(),
            "timestamp": t.string().optional(),
            "spanId": t.string().optional(),
            "textPayload": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "jsonPayload": t.struct({"_": t.string().optional()}).optional(),
            "split": t.proxy(renames["LogSplitIn"]).optional(),
            "protoPayload": t.struct({"_": t.string().optional()}).optional(),
            "trace": t.string().optional(),
            "severity": t.string().optional(),
            "resource": t.proxy(renames["MonitoredResourceIn"]),
            "traceSampled": t.boolean().optional(),
        }
    ).named(renames["LogEntryIn"])
    types["LogEntryOut"] = t.struct(
        {
            "insertId": t.string().optional(),
            "httpRequest": t.proxy(renames["HttpRequestOut"]).optional(),
            "logName": t.string(),
            "operation": t.proxy(renames["LogEntryOperationOut"]).optional(),
            "sourceLocation": t.proxy(renames["LogEntrySourceLocationOut"]).optional(),
            "timestamp": t.string().optional(),
            "spanId": t.string().optional(),
            "receiveTimestamp": t.string().optional(),
            "metadata": t.proxy(renames["MonitoredResourceMetadataOut"]).optional(),
            "textPayload": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "jsonPayload": t.struct({"_": t.string().optional()}).optional(),
            "split": t.proxy(renames["LogSplitOut"]).optional(),
            "protoPayload": t.struct({"_": t.string().optional()}).optional(),
            "trace": t.string().optional(),
            "severity": t.string().optional(),
            "resource": t.proxy(renames["MonitoredResourceOut"]),
            "traceSampled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogEntryOut"])
    types["MonitoredResourceDescriptorIn"] = t.struct(
        {
            "name": t.string().optional(),
            "launchStage": t.string().optional(),
            "description": t.string().optional(),
            "type": t.string(),
            "displayName": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])),
        }
    ).named(renames["MonitoredResourceDescriptorIn"])
    types["MonitoredResourceDescriptorOut"] = t.struct(
        {
            "name": t.string().optional(),
            "launchStage": t.string().optional(),
            "description": t.string().optional(),
            "type": t.string(),
            "displayName": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceDescriptorOut"])
    types["UpdateBucketRequestIn"] = t.struct(
        {
            "name": t.string(),
            "bucket": t.proxy(renames["LogBucketIn"]),
            "updateMask": t.string(),
        }
    ).named(renames["UpdateBucketRequestIn"])
    types["UpdateBucketRequestOut"] = t.struct(
        {
            "name": t.string(),
            "bucket": t.proxy(renames["LogBucketOut"]),
            "updateMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateBucketRequestOut"])
    types["LinkIn"] = t.struct(
        {
            "bigqueryDataset": t.proxy(renames["BigQueryDatasetIn"]).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "bigqueryDataset": t.proxy(renames["BigQueryDatasetOut"]).optional(),
            "lifecycleState": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
    types["WriteLogEntriesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WriteLogEntriesResponseIn"]
    )
    types["WriteLogEntriesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WriteLogEntriesResponseOut"])
    types["LabelDescriptorIn"] = t.struct(
        {
            "valueType": t.string().optional(),
            "description": t.string().optional(),
            "key": t.string().optional(),
        }
    ).named(renames["LabelDescriptorIn"])
    types["LabelDescriptorOut"] = t.struct(
        {
            "valueType": t.string().optional(),
            "description": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelDescriptorOut"])
    types["ListSinksResponseIn"] = t.struct(
        {
            "sinks": t.array(t.proxy(renames["LogSinkIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListSinksResponseIn"])
    types["ListSinksResponseOut"] = t.struct(
        {
            "sinks": t.array(t.proxy(renames["LogSinkOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSinksResponseOut"])
    types["IndexConfigIn"] = t.struct(
        {"type": t.string(), "fieldPath": t.string()}
    ).named(renames["IndexConfigIn"])
    types["IndexConfigOut"] = t.struct(
        {
            "type": t.string(),
            "createTime": t.string().optional(),
            "fieldPath": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexConfigOut"])
    types["BigQueryOptionsIn"] = t.struct(
        {"usePartitionedTables": t.boolean().optional()}
    ).named(renames["BigQueryOptionsIn"])
    types["BigQueryOptionsOut"] = t.struct(
        {
            "usePartitionedTables": t.boolean().optional(),
            "usesTimestampColumnPartitioning": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryOptionsOut"])
    types["LocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["MetricDescriptorMetadataIn"] = t.struct(
        {
            "ingestDelay": t.string().optional(),
            "launchStage": t.string().optional(),
            "samplePeriod": t.string().optional(),
        }
    ).named(renames["MetricDescriptorMetadataIn"])
    types["MetricDescriptorMetadataOut"] = t.struct(
        {
            "ingestDelay": t.string().optional(),
            "launchStage": t.string().optional(),
            "samplePeriod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorMetadataOut"])
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
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["ListLogsResponseIn"] = t.struct(
        {
            "logNames": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLogsResponseIn"])
    types["ListLogsResponseOut"] = t.struct(
        {
            "logNames": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLogsResponseOut"])
    types["LogMetricIn"] = t.struct(
        {
            "bucketName": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string(),
            "valueExtractor": t.string().optional(),
            "metricDescriptor": t.proxy(renames["MetricDescriptorIn"]).optional(),
            "version": t.string().optional(),
            "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
            "disabled": t.boolean().optional(),
            "bucketOptions": t.proxy(renames["BucketOptionsIn"]).optional(),
            "filter": t.string(),
        }
    ).named(renames["LogMetricIn"])
    types["LogMetricOut"] = t.struct(
        {
            "bucketName": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string(),
            "updateTime": t.string().optional(),
            "valueExtractor": t.string().optional(),
            "metricDescriptor": t.proxy(renames["MetricDescriptorOut"]).optional(),
            "version": t.string().optional(),
            "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
            "disabled": t.boolean().optional(),
            "createTime": t.string().optional(),
            "bucketOptions": t.proxy(renames["BucketOptionsOut"]).optional(),
            "filter": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogMetricOut"])
    types["RequestLogIn"] = t.struct(
        {
            "traceId": t.string().optional(),
            "latency": t.string().optional(),
            "taskName": t.string().optional(),
            "first": t.boolean().optional(),
            "line": t.array(t.proxy(renames["LogLineIn"])).optional(),
            "cost": t.number().optional(),
            "instanceId": t.string().optional(),
            "megaCycles": t.string().optional(),
            "requestId": t.string().optional(),
            "wasLoadingRequest": t.boolean().optional(),
            "endTime": t.string().optional(),
            "resource": t.string().optional(),
            "appId": t.string().optional(),
            "urlMapEntry": t.string().optional(),
            "taskQueueName": t.string().optional(),
            "sourceReference": t.array(
                t.proxy(renames["SourceReferenceIn"])
            ).optional(),
            "versionId": t.string().optional(),
            "userAgent": t.string().optional(),
            "nickname": t.string().optional(),
            "instanceIndex": t.integer().optional(),
            "appEngineRelease": t.string().optional(),
            "finished": t.boolean().optional(),
            "host": t.string().optional(),
            "pendingTime": t.string().optional(),
            "responseSize": t.string().optional(),
            "status": t.integer().optional(),
            "moduleId": t.string().optional(),
            "startTime": t.string().optional(),
            "referrer": t.string().optional(),
            "method": t.string().optional(),
            "spanId": t.string().optional(),
            "httpVersion": t.string().optional(),
            "traceSampled": t.boolean().optional(),
            "ip": t.string().optional(),
        }
    ).named(renames["RequestLogIn"])
    types["RequestLogOut"] = t.struct(
        {
            "traceId": t.string().optional(),
            "latency": t.string().optional(),
            "taskName": t.string().optional(),
            "first": t.boolean().optional(),
            "line": t.array(t.proxy(renames["LogLineOut"])).optional(),
            "cost": t.number().optional(),
            "instanceId": t.string().optional(),
            "megaCycles": t.string().optional(),
            "requestId": t.string().optional(),
            "wasLoadingRequest": t.boolean().optional(),
            "endTime": t.string().optional(),
            "resource": t.string().optional(),
            "appId": t.string().optional(),
            "urlMapEntry": t.string().optional(),
            "taskQueueName": t.string().optional(),
            "sourceReference": t.array(
                t.proxy(renames["SourceReferenceOut"])
            ).optional(),
            "versionId": t.string().optional(),
            "userAgent": t.string().optional(),
            "nickname": t.string().optional(),
            "instanceIndex": t.integer().optional(),
            "appEngineRelease": t.string().optional(),
            "finished": t.boolean().optional(),
            "host": t.string().optional(),
            "pendingTime": t.string().optional(),
            "responseSize": t.string().optional(),
            "status": t.integer().optional(),
            "moduleId": t.string().optional(),
            "startTime": t.string().optional(),
            "referrer": t.string().optional(),
            "method": t.string().optional(),
            "spanId": t.string().optional(),
            "httpVersion": t.string().optional(),
            "traceSampled": t.boolean().optional(),
            "ip": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestLogOut"])
    types["SourceLocationIn"] = t.struct(
        {
            "file": t.string().optional(),
            "functionName": t.string().optional(),
            "line": t.string().optional(),
        }
    ).named(renames["SourceLocationIn"])
    types["SourceLocationOut"] = t.struct(
        {
            "file": t.string().optional(),
            "functionName": t.string().optional(),
            "line": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceLocationOut"])
    types["CreateLinkRequestIn"] = t.struct(
        {"parent": t.string(), "link": t.proxy(renames["LinkIn"]), "linkId": t.string()}
    ).named(renames["CreateLinkRequestIn"])
    types["CreateLinkRequestOut"] = t.struct(
        {
            "parent": t.string(),
            "link": t.proxy(renames["LinkOut"]),
            "linkId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateLinkRequestOut"])
    types["CopyLogEntriesMetadataIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "progress": t.integer().optional(),
            "writerIdentity": t.string().optional(),
            "request": t.proxy(renames["CopyLogEntriesRequestIn"]).optional(),
            "cancellationRequested": t.boolean().optional(),
            "startTime": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["CopyLogEntriesMetadataIn"])
    types["CopyLogEntriesMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "progress": t.integer().optional(),
            "writerIdentity": t.string().optional(),
            "request": t.proxy(renames["CopyLogEntriesRequestOut"]).optional(),
            "cancellationRequested": t.boolean().optional(),
            "startTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyLogEntriesMetadataOut"])
    types["ListMonitoredResourceDescriptorsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "resourceDescriptors": t.array(
                t.proxy(renames["MonitoredResourceDescriptorIn"])
            ).optional(),
        }
    ).named(renames["ListMonitoredResourceDescriptorsResponseIn"])
    types["ListMonitoredResourceDescriptorsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "resourceDescriptors": t.array(
                t.proxy(renames["MonitoredResourceDescriptorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMonitoredResourceDescriptorsResponseOut"])
    types["LogEntrySourceLocationIn"] = t.struct(
        {
            "file": t.string().optional(),
            "function": t.string().optional(),
            "line": t.string().optional(),
        }
    ).named(renames["LogEntrySourceLocationIn"])
    types["LogEntrySourceLocationOut"] = t.struct(
        {
            "file": t.string().optional(),
            "function": t.string().optional(),
            "line": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogEntrySourceLocationOut"])
    types["SettingsIn"] = t.struct(
        {
            "disableDefaultSink": t.boolean().optional(),
            "kmsKeyName": t.string().optional(),
            "storageLocation": t.string().optional(),
        }
    ).named(renames["SettingsIn"])
    types["SettingsOut"] = t.struct(
        {
            "name": t.string().optional(),
            "disableDefaultSink": t.boolean().optional(),
            "kmsKeyName": t.string().optional(),
            "kmsServiceAccountId": t.string().optional(),
            "storageLocation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettingsOut"])
    types["CmekSettingsIn"] = t.struct(
        {
            "kmsKeyVersionName": t.string().optional(),
            "kmsKeyName": t.string().optional(),
        }
    ).named(renames["CmekSettingsIn"])
    types["CmekSettingsOut"] = t.struct(
        {
            "kmsKeyVersionName": t.string().optional(),
            "name": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "serviceAccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CmekSettingsOut"])
    types["BucketMetadataIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "updateBucketRequest": t.proxy(renames["UpdateBucketRequestIn"]).optional(),
            "createBucketRequest": t.proxy(renames["CreateBucketRequestIn"]).optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["BucketMetadataIn"])
    types["BucketMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "updateBucketRequest": t.proxy(
                renames["UpdateBucketRequestOut"]
            ).optional(),
            "createBucketRequest": t.proxy(
                renames["CreateBucketRequestOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BucketMetadataOut"])
    types["ListLinksResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "links": t.array(t.proxy(renames["LinkIn"])).optional(),
        }
    ).named(renames["ListLinksResponseIn"])
    types["ListLinksResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "links": t.array(t.proxy(renames["LinkOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLinksResponseOut"])
    types["ListExclusionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
        }
    ).named(renames["ListExclusionsResponseIn"])
    types["ListExclusionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "exclusions": t.array(t.proxy(renames["LogExclusionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListExclusionsResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["TailLogEntriesRequestIn"] = t.struct(
        {
            "filter": t.string().optional(),
            "bufferWindow": t.string().optional(),
            "resourceNames": t.array(t.string()),
        }
    ).named(renames["TailLogEntriesRequestIn"])
    types["TailLogEntriesRequestOut"] = t.struct(
        {
            "filter": t.string().optional(),
            "bufferWindow": t.string().optional(),
            "resourceNames": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TailLogEntriesRequestOut"])
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
    types["MetricDescriptorIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "valueType": t.string().optional(),
            "type": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
            "launchStage": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "unit": t.string().optional(),
            "metricKind": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
        }
    ).named(renames["MetricDescriptorIn"])
    types["MetricDescriptorOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "valueType": t.string().optional(),
            "type": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataOut"]).optional(),
            "launchStage": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "unit": t.string().optional(),
            "metricKind": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["ListViewsResponseIn"] = t.struct(
        {
            "views": t.array(t.proxy(renames["LogViewIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListViewsResponseIn"])
    types["ListViewsResponseOut"] = t.struct(
        {
            "views": t.array(t.proxy(renames["LogViewOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListViewsResponseOut"])
    types["TailLogEntriesResponseIn"] = t.struct(
        {
            "suppressionInfo": t.array(
                t.proxy(renames["SuppressionInfoIn"])
            ).optional(),
            "entries": t.array(t.proxy(renames["LogEntryIn"])).optional(),
        }
    ).named(renames["TailLogEntriesResponseIn"])
    types["TailLogEntriesResponseOut"] = t.struct(
        {
            "suppressionInfo": t.array(
                t.proxy(renames["SuppressionInfoOut"])
            ).optional(),
            "entries": t.array(t.proxy(renames["LogEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TailLogEntriesResponseOut"])
    types["LogBucketIn"] = t.struct(
        {
            "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
            "locked": t.boolean().optional(),
            "retentionDays": t.integer().optional(),
            "description": t.string().optional(),
            "restrictedFields": t.array(t.string()).optional(),
            "analyticsEnabled": t.boolean().optional(),
            "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
        }
    ).named(renames["LogBucketIn"])
    types["LogBucketOut"] = t.struct(
        {
            "indexConfigs": t.array(t.proxy(renames["IndexConfigOut"])).optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "locked": t.boolean().optional(),
            "retentionDays": t.integer().optional(),
            "description": t.string().optional(),
            "lifecycleState": t.string().optional(),
            "restrictedFields": t.array(t.string()).optional(),
            "analyticsEnabled": t.boolean().optional(),
            "cmekSettings": t.proxy(renames["CmekSettingsOut"]).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogBucketOut"])
    types["UndeleteBucketRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UndeleteBucketRequestIn"]
    )
    types["UndeleteBucketRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteBucketRequestOut"])
    types["ListLogEntriesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "entries": t.array(t.proxy(renames["LogEntryIn"])).optional(),
        }
    ).named(renames["ListLogEntriesResponseIn"])
    types["ListLogEntriesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "entries": t.array(t.proxy(renames["LogEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLogEntriesResponseOut"])
    types["HttpRequestIn"] = t.struct(
        {
            "responseSize": t.string().optional(),
            "status": t.integer().optional(),
            "cacheValidatedWithOriginServer": t.boolean().optional(),
            "protocol": t.string().optional(),
            "requestUrl": t.string().optional(),
            "cacheLookup": t.boolean().optional(),
            "requestMethod": t.string().optional(),
            "referer": t.string().optional(),
            "requestSize": t.string().optional(),
            "latency": t.string().optional(),
            "remoteIp": t.string().optional(),
            "userAgent": t.string().optional(),
            "cacheHit": t.boolean().optional(),
            "serverIp": t.string().optional(),
            "cacheFillBytes": t.string().optional(),
        }
    ).named(renames["HttpRequestIn"])
    types["HttpRequestOut"] = t.struct(
        {
            "responseSize": t.string().optional(),
            "status": t.integer().optional(),
            "cacheValidatedWithOriginServer": t.boolean().optional(),
            "protocol": t.string().optional(),
            "requestUrl": t.string().optional(),
            "cacheLookup": t.boolean().optional(),
            "requestMethod": t.string().optional(),
            "referer": t.string().optional(),
            "requestSize": t.string().optional(),
            "latency": t.string().optional(),
            "remoteIp": t.string().optional(),
            "userAgent": t.string().optional(),
            "cacheHit": t.boolean().optional(),
            "serverIp": t.string().optional(),
            "cacheFillBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRequestOut"])

    functions = {}
    functions["entriesWrite"] = logging.post(
        "v2/entries:copy",
        t.struct(
            {
                "destination": t.string(),
                "name": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["entriesTail"] = logging.post(
        "v2/entries:copy",
        t.struct(
            {
                "destination": t.string(),
                "name": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["entriesList"] = logging.post(
        "v2/entries:copy",
        t.struct(
            {
                "destination": t.string(),
                "name": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["entriesCopy"] = logging.post(
        "v2/entries:copy",
        t.struct(
            {
                "destination": t.string(),
                "name": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsGetCmekSettings"] = logging.get(
        "v2/{name}/settings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsGetSettings"] = logging.get(
        "v2/{name}/settings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsExclusionsPatch"] = logging.get(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExclusionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsExclusionsDelete"] = logging.get(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExclusionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsExclusionsGet"] = logging.get(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExclusionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsExclusionsCreate"] = logging.get(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExclusionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsExclusionsList"] = logging.get(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExclusionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsSinksPatch"] = logging.get(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsSinksDelete"] = logging.get(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsSinksCreate"] = logging.get(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsSinksUpdate"] = logging.get(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsSinksList"] = logging.get(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsSinksGet"] = logging.get(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsGet"] = logging.get(
        "v2/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsList"] = logging.get(
        "v2/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsOperationsList"] = logging.post(
        "v2/{name}:cancel",
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
    functions["billingAccountsLocationsOperationsGet"] = logging.post(
        "v2/{name}:cancel",
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
    functions["billingAccountsLocationsOperationsCancel"] = logging.post(
        "v2/{name}:cancel",
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
    functions["billingAccountsLocationsBucketsCreate"] = logging.post(
        "v2/{name}:updateAsync",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "description": t.string().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsList"] = logging.post(
        "v2/{name}:updateAsync",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "description": t.string().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsUndelete"] = logging.post(
        "v2/{name}:updateAsync",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "description": t.string().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsDelete"] = logging.post(
        "v2/{name}:updateAsync",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "description": t.string().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsPatch"] = logging.post(
        "v2/{name}:updateAsync",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "description": t.string().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsCreateAsync"] = logging.post(
        "v2/{name}:updateAsync",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "description": t.string().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsGet"] = logging.post(
        "v2/{name}:updateAsync",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "description": t.string().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsUpdateAsync"] = logging.post(
        "v2/{name}:updateAsync",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "description": t.string().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsViewsCreate"] = logging.get(
        "v2/{parent}/views",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListViewsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsViewsDelete"] = logging.get(
        "v2/{parent}/views",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListViewsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsViewsGet"] = logging.get(
        "v2/{parent}/views",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListViewsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsViewsPatch"] = logging.get(
        "v2/{parent}/views",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListViewsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsViewsList"] = logging.get(
        "v2/{parent}/views",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListViewsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsViewsLogsList"] = logging.get(
        "v2/{parent}/logs",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "resourceNames": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsLinksList"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsLinksCreate"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsLinksDelete"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsLinksGet"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLogsDelete"] = logging.get(
        "v2/{parent}/logs",
        t.struct(
            {
                "resourceNames": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLogsList"] = logging.get(
        "v2/{parent}/logs",
        t.struct(
            {
                "resourceNames": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsList"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsGet"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsDelete"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "description": t.string().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsUndelete"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "description": t.string().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsCreateAsync"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "description": t.string().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsCreate"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "description": t.string().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsUpdateAsync"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "description": t.string().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsGet"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "description": t.string().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsList"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "description": t.string().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsPatch"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "description": t.string().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsViewsGet"] = logging.post(
        "v2/{parent}/views",
        t.struct(
            {
                "viewId": t.string(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsViewsDelete"] = logging.post(
        "v2/{parent}/views",
        t.struct(
            {
                "viewId": t.string(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsViewsList"] = logging.post(
        "v2/{parent}/views",
        t.struct(
            {
                "viewId": t.string(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsViewsPatch"] = logging.post(
        "v2/{parent}/views",
        t.struct(
            {
                "viewId": t.string(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsViewsCreate"] = logging.post(
        "v2/{parent}/views",
        t.struct(
            {
                "viewId": t.string(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsLinksDelete"] = logging.post(
        "v2/{parent}/links",
        t.struct(
            {
                "parent": t.string(),
                "linkId": t.string(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetIn"]).optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsLinksList"] = logging.post(
        "v2/{parent}/links",
        t.struct(
            {
                "parent": t.string(),
                "linkId": t.string(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetIn"]).optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsLinksGet"] = logging.post(
        "v2/{parent}/links",
        t.struct(
            {
                "parent": t.string(),
                "linkId": t.string(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetIn"]).optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsLinksCreate"] = logging.post(
        "v2/{parent}/links",
        t.struct(
            {
                "parent": t.string(),
                "linkId": t.string(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetIn"]).optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsOperationsList"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsOperationsCancel"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsOperationsGet"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["monitoredResourceDescriptorsList"] = logging.get(
        "v2/monitoredResourceDescriptors",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMonitoredResourceDescriptorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sinksCreate"] = logging.delete(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sinksGet"] = logging.delete(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sinksList"] = logging.delete(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sinksUpdate"] = logging.delete(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sinksDelete"] = logging.delete(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersUpdateSettings"] = logging.get(
        "v2/{name}/cmekSettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CmekSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersGetSettings"] = logging.get(
        "v2/{name}/cmekSettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CmekSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersGetCmekSettings"] = logging.get(
        "v2/{name}/cmekSettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CmekSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSinksCreate"] = logging.patch(
        "v2/{sinkName}",
        t.struct(
            {
                "uniqueWriterIdentity": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "sinkName": t.string(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "includeChildren": t.boolean().optional(),
                "disabled": t.boolean().optional(),
                "destination": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "name": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSinksGet"] = logging.patch(
        "v2/{sinkName}",
        t.struct(
            {
                "uniqueWriterIdentity": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "sinkName": t.string(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "includeChildren": t.boolean().optional(),
                "disabled": t.boolean().optional(),
                "destination": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "name": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSinksUpdate"] = logging.patch(
        "v2/{sinkName}",
        t.struct(
            {
                "uniqueWriterIdentity": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "sinkName": t.string(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "includeChildren": t.boolean().optional(),
                "disabled": t.boolean().optional(),
                "destination": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "name": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSinksDelete"] = logging.patch(
        "v2/{sinkName}",
        t.struct(
            {
                "uniqueWriterIdentity": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "sinkName": t.string(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "includeChildren": t.boolean().optional(),
                "disabled": t.boolean().optional(),
                "destination": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "name": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSinksList"] = logging.patch(
        "v2/{sinkName}",
        t.struct(
            {
                "uniqueWriterIdentity": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "sinkName": t.string(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "includeChildren": t.boolean().optional(),
                "disabled": t.boolean().optional(),
                "destination": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "name": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSinksPatch"] = logging.patch(
        "v2/{sinkName}",
        t.struct(
            {
                "uniqueWriterIdentity": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "sinkName": t.string(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "includeChildren": t.boolean().optional(),
                "disabled": t.boolean().optional(),
                "destination": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "name": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersExclusionsDelete"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "filter": t.string(),
                "disabled": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersExclusionsCreate"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "filter": t.string(),
                "disabled": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersExclusionsList"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "filter": t.string(),
                "disabled": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersExclusionsGet"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "filter": t.string(),
                "disabled": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersExclusionsPatch"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "filter": t.string(),
                "disabled": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsGet"] = logging.get(
        "v2/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsList"] = logging.get(
        "v2/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsOperationsList"] = logging.post(
        "v2/{name}:cancel",
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
    functions["foldersLocationsOperationsGet"] = logging.post(
        "v2/{name}:cancel",
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
    functions["foldersLocationsOperationsCancel"] = logging.post(
        "v2/{name}:cancel",
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
    functions["foldersLocationsBucketsUpdateAsync"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsUndelete"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsCreate"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsList"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsGet"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsPatch"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsCreateAsync"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsDelete"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsLinksGet"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsLinksList"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsLinksCreate"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsLinksDelete"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsViewsGet"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsViewsCreate"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsViewsPatch"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsViewsList"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsViewsDelete"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsViewsLogsList"] = logging.get(
        "v2/{parent}/logs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "resourceNames": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLogsDelete"] = logging.get(
        "v2/{parent}/logs",
        t.struct(
            {
                "parent": t.string(),
                "resourceNames": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLogsList"] = logging.get(
        "v2/{parent}/logs",
        t.struct(
            {
                "parent": t.string(),
                "resourceNames": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["logsDelete"] = logging.get(
        "v2/{parent}/logs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "resourceNames": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["logsList"] = logging.get(
        "v2/{parent}/logs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "resourceNames": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetCmekSettings"] = logging.get(
        "v2/{name}/settings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetSettings"] = logging.get(
        "v2/{name}/settings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = logging.get(
        "v2/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = logging.get(
        "v2/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = logging.get(
        "v2/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsDelete"] = logging.post(
        "v2/{parent}/buckets:createAsync",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "description": t.string().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsCreate"] = logging.post(
        "v2/{parent}/buckets:createAsync",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "description": t.string().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsGet"] = logging.post(
        "v2/{parent}/buckets:createAsync",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "description": t.string().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsUpdateAsync"] = logging.post(
        "v2/{parent}/buckets:createAsync",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "description": t.string().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsList"] = logging.post(
        "v2/{parent}/buckets:createAsync",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "description": t.string().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsPatch"] = logging.post(
        "v2/{parent}/buckets:createAsync",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "description": t.string().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsUndelete"] = logging.post(
        "v2/{parent}/buckets:createAsync",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "description": t.string().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsCreateAsync"] = logging.post(
        "v2/{parent}/buckets:createAsync",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "description": t.string().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsLinksCreate"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsLinksList"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsLinksGet"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsLinksDelete"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsViewsCreate"] = logging.get(
        "v2/{parent}/views",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListViewsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsViewsGet"] = logging.get(
        "v2/{parent}/views",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListViewsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsViewsDelete"] = logging.get(
        "v2/{parent}/views",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListViewsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsViewsPatch"] = logging.get(
        "v2/{parent}/views",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListViewsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsViewsList"] = logging.get(
        "v2/{parent}/views",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListViewsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsViewsLogsList"] = logging.get(
        "v2/{parent}/logs",
        t.struct(
            {
                "resourceNames": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsExclusionsDelete"] = logging.post(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string(),
                "name": t.string(),
                "disabled": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsExclusionsList"] = logging.post(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string(),
                "name": t.string(),
                "disabled": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsExclusionsGet"] = logging.post(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string(),
                "name": t.string(),
                "disabled": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsExclusionsPatch"] = logging.post(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string(),
                "name": t.string(),
                "disabled": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsExclusionsCreate"] = logging.post(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string(),
                "name": t.string(),
                "disabled": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSinksPatch"] = logging.get(
        "v2/{parent}/sinks",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSinksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSinksDelete"] = logging.get(
        "v2/{parent}/sinks",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSinksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSinksGet"] = logging.get(
        "v2/{parent}/sinks",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSinksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSinksUpdate"] = logging.get(
        "v2/{parent}/sinks",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSinksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSinksCreate"] = logging.get(
        "v2/{parent}/sinks",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSinksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSinksList"] = logging.get(
        "v2/{parent}/sinks",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSinksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMetricsCreate"] = logging.put(
        "v2/{metricName}",
        t.struct(
            {
                "metricName": t.string(),
                "bucketName": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string(),
                "valueExtractor": t.string().optional(),
                "metricDescriptor": t.proxy(renames["MetricDescriptorIn"]).optional(),
                "version": t.string().optional(),
                "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
                "disabled": t.boolean().optional(),
                "bucketOptions": t.proxy(renames["BucketOptionsIn"]).optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogMetricOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMetricsGet"] = logging.put(
        "v2/{metricName}",
        t.struct(
            {
                "metricName": t.string(),
                "bucketName": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string(),
                "valueExtractor": t.string().optional(),
                "metricDescriptor": t.proxy(renames["MetricDescriptorIn"]).optional(),
                "version": t.string().optional(),
                "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
                "disabled": t.boolean().optional(),
                "bucketOptions": t.proxy(renames["BucketOptionsIn"]).optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogMetricOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMetricsList"] = logging.put(
        "v2/{metricName}",
        t.struct(
            {
                "metricName": t.string(),
                "bucketName": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string(),
                "valueExtractor": t.string().optional(),
                "metricDescriptor": t.proxy(renames["MetricDescriptorIn"]).optional(),
                "version": t.string().optional(),
                "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
                "disabled": t.boolean().optional(),
                "bucketOptions": t.proxy(renames["BucketOptionsIn"]).optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogMetricOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMetricsDelete"] = logging.put(
        "v2/{metricName}",
        t.struct(
            {
                "metricName": t.string(),
                "bucketName": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string(),
                "valueExtractor": t.string().optional(),
                "metricDescriptor": t.proxy(renames["MetricDescriptorIn"]).optional(),
                "version": t.string().optional(),
                "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
                "disabled": t.boolean().optional(),
                "bucketOptions": t.proxy(renames["BucketOptionsIn"]).optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogMetricOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMetricsUpdate"] = logging.put(
        "v2/{metricName}",
        t.struct(
            {
                "metricName": t.string(),
                "bucketName": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string(),
                "valueExtractor": t.string().optional(),
                "metricDescriptor": t.proxy(renames["MetricDescriptorIn"]).optional(),
                "version": t.string().optional(),
                "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
                "disabled": t.boolean().optional(),
                "bucketOptions": t.proxy(renames["BucketOptionsIn"]).optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogMetricOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLogsList"] = logging.delete(
        "v2/{logName}",
        t.struct({"logName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLogsDelete"] = logging.delete(
        "v2/{logName}",
        t.struct({"logName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["exclusionsDelete"] = logging.get(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExclusionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["exclusionsPatch"] = logging.get(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExclusionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["exclusionsGet"] = logging.get(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExclusionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["exclusionsCreate"] = logging.get(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExclusionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["exclusionsList"] = logging.get(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExclusionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGetCmekSettings"] = logging.patch(
        "v2/{name}/settings",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "disableDefaultSink": t.boolean().optional(),
                "kmsKeyName": t.string().optional(),
                "storageLocation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGetSettings"] = logging.patch(
        "v2/{name}/settings",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "disableDefaultSink": t.boolean().optional(),
                "kmsKeyName": t.string().optional(),
                "storageLocation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsUpdateCmekSettings"] = logging.patch(
        "v2/{name}/settings",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "disableDefaultSink": t.boolean().optional(),
                "kmsKeyName": t.string().optional(),
                "storageLocation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsUpdateSettings"] = logging.patch(
        "v2/{name}/settings",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "disableDefaultSink": t.boolean().optional(),
                "kmsKeyName": t.string().optional(),
                "storageLocation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsExclusionsCreate"] = logging.get(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExclusionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsExclusionsDelete"] = logging.get(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExclusionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsExclusionsGet"] = logging.get(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExclusionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsExclusionsPatch"] = logging.get(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExclusionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsExclusionsList"] = logging.get(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExclusionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLogsList"] = logging.delete(
        "v2/{logName}",
        t.struct({"logName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLogsDelete"] = logging.delete(
        "v2/{logName}",
        t.struct({"logName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSinksCreate"] = logging.put(
        "v2/{sinkName}",
        t.struct(
            {
                "sinkName": t.string(),
                "uniqueWriterIdentity": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "includeChildren": t.boolean().optional(),
                "disabled": t.boolean().optional(),
                "destination": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "name": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSinksDelete"] = logging.put(
        "v2/{sinkName}",
        t.struct(
            {
                "sinkName": t.string(),
                "uniqueWriterIdentity": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "includeChildren": t.boolean().optional(),
                "disabled": t.boolean().optional(),
                "destination": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "name": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSinksList"] = logging.put(
        "v2/{sinkName}",
        t.struct(
            {
                "sinkName": t.string(),
                "uniqueWriterIdentity": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "includeChildren": t.boolean().optional(),
                "disabled": t.boolean().optional(),
                "destination": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "name": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSinksGet"] = logging.put(
        "v2/{sinkName}",
        t.struct(
            {
                "sinkName": t.string(),
                "uniqueWriterIdentity": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "includeChildren": t.boolean().optional(),
                "disabled": t.boolean().optional(),
                "destination": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "name": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSinksPatch"] = logging.put(
        "v2/{sinkName}",
        t.struct(
            {
                "sinkName": t.string(),
                "uniqueWriterIdentity": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "includeChildren": t.boolean().optional(),
                "disabled": t.boolean().optional(),
                "destination": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "name": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSinksUpdate"] = logging.put(
        "v2/{sinkName}",
        t.struct(
            {
                "sinkName": t.string(),
                "uniqueWriterIdentity": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "includeChildren": t.boolean().optional(),
                "disabled": t.boolean().optional(),
                "destination": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "name": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsList"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsGet"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsOperationsCancel"] = logging.get(
        "v2/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsOperationsGet"] = logging.get(
        "v2/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsOperationsList"] = logging.get(
        "v2/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsUpdateAsync"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsDelete"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsList"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsCreate"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsCreateAsync"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsUndelete"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsPatch"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsGet"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsLinksList"] = logging.post(
        "v2/{parent}/links",
        t.struct(
            {
                "linkId": t.string(),
                "parent": t.string(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetIn"]).optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsLinksGet"] = logging.post(
        "v2/{parent}/links",
        t.struct(
            {
                "linkId": t.string(),
                "parent": t.string(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetIn"]).optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsLinksDelete"] = logging.post(
        "v2/{parent}/links",
        t.struct(
            {
                "linkId": t.string(),
                "parent": t.string(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetIn"]).optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsLinksCreate"] = logging.post(
        "v2/{parent}/links",
        t.struct(
            {
                "linkId": t.string(),
                "parent": t.string(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetIn"]).optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsViewsPatch"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsViewsDelete"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsViewsCreate"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsViewsList"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsViewsGet"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsViewsLogsList"] = logging.get(
        "v2/{parent}/logs",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "resourceNames": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v2GetCmekSettings"] = logging.get(
        "v2/{name}/settings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v2UpdateSettings"] = logging.get(
        "v2/{name}/settings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v2UpdateCmekSettings"] = logging.get(
        "v2/{name}/settings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v2GetSettings"] = logging.get(
        "v2/{name}/settings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="logging", renames=renames, types=Box(types), functions=Box(functions)
    )
