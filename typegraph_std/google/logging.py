from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_logging():
    logging = HTTPRuntime("https://logging.googleapis.com/")

    renames = {
        "ErrorResponse": "_logging_1_ErrorResponse",
        "ListBucketsResponseIn": "_logging_2_ListBucketsResponseIn",
        "ListBucketsResponseOut": "_logging_3_ListBucketsResponseOut",
        "CopyLogEntriesRequestIn": "_logging_4_CopyLogEntriesRequestIn",
        "CopyLogEntriesRequestOut": "_logging_5_CopyLogEntriesRequestOut",
        "MonitoredResourceMetadataIn": "_logging_6_MonitoredResourceMetadataIn",
        "MonitoredResourceMetadataOut": "_logging_7_MonitoredResourceMetadataOut",
        "TailLogEntriesResponseIn": "_logging_8_TailLogEntriesResponseIn",
        "TailLogEntriesResponseOut": "_logging_9_TailLogEntriesResponseOut",
        "TailLogEntriesRequestIn": "_logging_10_TailLogEntriesRequestIn",
        "TailLogEntriesRequestOut": "_logging_11_TailLogEntriesRequestOut",
        "SourceLocationIn": "_logging_12_SourceLocationIn",
        "SourceLocationOut": "_logging_13_SourceLocationOut",
        "LocationMetadataIn": "_logging_14_LocationMetadataIn",
        "LocationMetadataOut": "_logging_15_LocationMetadataOut",
        "LogEntryIn": "_logging_16_LogEntryIn",
        "LogEntryOut": "_logging_17_LogEntryOut",
        "BucketOptionsIn": "_logging_18_BucketOptionsIn",
        "BucketOptionsOut": "_logging_19_BucketOptionsOut",
        "IndexConfigIn": "_logging_20_IndexConfigIn",
        "IndexConfigOut": "_logging_21_IndexConfigOut",
        "LogExclusionIn": "_logging_22_LogExclusionIn",
        "LogExclusionOut": "_logging_23_LogExclusionOut",
        "ListLinksResponseIn": "_logging_24_ListLinksResponseIn",
        "ListLinksResponseOut": "_logging_25_ListLinksResponseOut",
        "CreateLinkRequestIn": "_logging_26_CreateLinkRequestIn",
        "CreateLinkRequestOut": "_logging_27_CreateLinkRequestOut",
        "ListLogMetricsResponseIn": "_logging_28_ListLogMetricsResponseIn",
        "ListLogMetricsResponseOut": "_logging_29_ListLogMetricsResponseOut",
        "ExplicitIn": "_logging_30_ExplicitIn",
        "ExplicitOut": "_logging_31_ExplicitOut",
        "BigQueryDatasetIn": "_logging_32_BigQueryDatasetIn",
        "BigQueryDatasetOut": "_logging_33_BigQueryDatasetOut",
        "StatusIn": "_logging_34_StatusIn",
        "StatusOut": "_logging_35_StatusOut",
        "SuppressionInfoIn": "_logging_36_SuppressionInfoIn",
        "SuppressionInfoOut": "_logging_37_SuppressionInfoOut",
        "CreateBucketRequestIn": "_logging_38_CreateBucketRequestIn",
        "CreateBucketRequestOut": "_logging_39_CreateBucketRequestOut",
        "UpdateBucketRequestIn": "_logging_40_UpdateBucketRequestIn",
        "UpdateBucketRequestOut": "_logging_41_UpdateBucketRequestOut",
        "ListViewsResponseIn": "_logging_42_ListViewsResponseIn",
        "ListViewsResponseOut": "_logging_43_ListViewsResponseOut",
        "ListLogsResponseIn": "_logging_44_ListLogsResponseIn",
        "ListLogsResponseOut": "_logging_45_ListLogsResponseOut",
        "ListMonitoredResourceDescriptorsResponseIn": "_logging_46_ListMonitoredResourceDescriptorsResponseIn",
        "ListMonitoredResourceDescriptorsResponseOut": "_logging_47_ListMonitoredResourceDescriptorsResponseOut",
        "LogBucketIn": "_logging_48_LogBucketIn",
        "LogBucketOut": "_logging_49_LogBucketOut",
        "ListExclusionsResponseIn": "_logging_50_ListExclusionsResponseIn",
        "ListExclusionsResponseOut": "_logging_51_ListExclusionsResponseOut",
        "HttpRequestIn": "_logging_52_HttpRequestIn",
        "HttpRequestOut": "_logging_53_HttpRequestOut",
        "LinkIn": "_logging_54_LinkIn",
        "LinkOut": "_logging_55_LinkOut",
        "DeleteLinkRequestIn": "_logging_56_DeleteLinkRequestIn",
        "DeleteLinkRequestOut": "_logging_57_DeleteLinkRequestOut",
        "CopyLogEntriesResponseIn": "_logging_58_CopyLogEntriesResponseIn",
        "CopyLogEntriesResponseOut": "_logging_59_CopyLogEntriesResponseOut",
        "LabelDescriptorIn": "_logging_60_LabelDescriptorIn",
        "LabelDescriptorOut": "_logging_61_LabelDescriptorOut",
        "LocationIn": "_logging_62_LocationIn",
        "LocationOut": "_logging_63_LocationOut",
        "LogEntrySourceLocationIn": "_logging_64_LogEntrySourceLocationIn",
        "LogEntrySourceLocationOut": "_logging_65_LogEntrySourceLocationOut",
        "MetricDescriptorIn": "_logging_66_MetricDescriptorIn",
        "MetricDescriptorOut": "_logging_67_MetricDescriptorOut",
        "OperationIn": "_logging_68_OperationIn",
        "OperationOut": "_logging_69_OperationOut",
        "WriteLogEntriesRequestIn": "_logging_70_WriteLogEntriesRequestIn",
        "WriteLogEntriesRequestOut": "_logging_71_WriteLogEntriesRequestOut",
        "MetricDescriptorMetadataIn": "_logging_72_MetricDescriptorMetadataIn",
        "MetricDescriptorMetadataOut": "_logging_73_MetricDescriptorMetadataOut",
        "ListSinksResponseIn": "_logging_74_ListSinksResponseIn",
        "ListSinksResponseOut": "_logging_75_ListSinksResponseOut",
        "LinkMetadataIn": "_logging_76_LinkMetadataIn",
        "LinkMetadataOut": "_logging_77_LinkMetadataOut",
        "LinearIn": "_logging_78_LinearIn",
        "LinearOut": "_logging_79_LinearOut",
        "ListLogEntriesResponseIn": "_logging_80_ListLogEntriesResponseIn",
        "ListLogEntriesResponseOut": "_logging_81_ListLogEntriesResponseOut",
        "BucketMetadataIn": "_logging_82_BucketMetadataIn",
        "BucketMetadataOut": "_logging_83_BucketMetadataOut",
        "ListOperationsResponseIn": "_logging_84_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_logging_85_ListOperationsResponseOut",
        "CancelOperationRequestIn": "_logging_86_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_logging_87_CancelOperationRequestOut",
        "WriteLogEntriesResponseIn": "_logging_88_WriteLogEntriesResponseIn",
        "WriteLogEntriesResponseOut": "_logging_89_WriteLogEntriesResponseOut",
        "CmekSettingsIn": "_logging_90_CmekSettingsIn",
        "CmekSettingsOut": "_logging_91_CmekSettingsOut",
        "LogViewIn": "_logging_92_LogViewIn",
        "LogViewOut": "_logging_93_LogViewOut",
        "RequestLogIn": "_logging_94_RequestLogIn",
        "RequestLogOut": "_logging_95_RequestLogOut",
        "LogLineIn": "_logging_96_LogLineIn",
        "LogLineOut": "_logging_97_LogLineOut",
        "SettingsIn": "_logging_98_SettingsIn",
        "SettingsOut": "_logging_99_SettingsOut",
        "MonitoredResourceIn": "_logging_100_MonitoredResourceIn",
        "MonitoredResourceOut": "_logging_101_MonitoredResourceOut",
        "ExponentialIn": "_logging_102_ExponentialIn",
        "ExponentialOut": "_logging_103_ExponentialOut",
        "LogSinkIn": "_logging_104_LogSinkIn",
        "LogSinkOut": "_logging_105_LogSinkOut",
        "CopyLogEntriesMetadataIn": "_logging_106_CopyLogEntriesMetadataIn",
        "CopyLogEntriesMetadataOut": "_logging_107_CopyLogEntriesMetadataOut",
        "EmptyIn": "_logging_108_EmptyIn",
        "EmptyOut": "_logging_109_EmptyOut",
        "SourceReferenceIn": "_logging_110_SourceReferenceIn",
        "SourceReferenceOut": "_logging_111_SourceReferenceOut",
        "ListLogEntriesRequestIn": "_logging_112_ListLogEntriesRequestIn",
        "ListLogEntriesRequestOut": "_logging_113_ListLogEntriesRequestOut",
        "LogEntryOperationIn": "_logging_114_LogEntryOperationIn",
        "LogEntryOperationOut": "_logging_115_LogEntryOperationOut",
        "UndeleteBucketRequestIn": "_logging_116_UndeleteBucketRequestIn",
        "UndeleteBucketRequestOut": "_logging_117_UndeleteBucketRequestOut",
        "ListLocationsResponseIn": "_logging_118_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_logging_119_ListLocationsResponseOut",
        "LogMetricIn": "_logging_120_LogMetricIn",
        "LogMetricOut": "_logging_121_LogMetricOut",
        "MonitoredResourceDescriptorIn": "_logging_122_MonitoredResourceDescriptorIn",
        "MonitoredResourceDescriptorOut": "_logging_123_MonitoredResourceDescriptorOut",
        "LogSplitIn": "_logging_124_LogSplitIn",
        "LogSplitOut": "_logging_125_LogSplitOut",
        "BigQueryOptionsIn": "_logging_126_BigQueryOptionsIn",
        "BigQueryOptionsOut": "_logging_127_BigQueryOptionsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ListBucketsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "buckets": t.array(t.proxy(renames["LogBucketIn"])).optional(),
        }
    ).named(renames["ListBucketsResponseIn"])
    types["ListBucketsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "buckets": t.array(t.proxy(renames["LogBucketOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBucketsResponseOut"])
    types["CopyLogEntriesRequestIn"] = t.struct(
        {"filter": t.string().optional(), "destination": t.string(), "name": t.string()}
    ).named(renames["CopyLogEntriesRequestIn"])
    types["CopyLogEntriesRequestOut"] = t.struct(
        {
            "filter": t.string().optional(),
            "destination": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyLogEntriesRequestOut"])
    types["MonitoredResourceMetadataIn"] = t.struct(
        {
            "systemLabels": t.struct({"_": t.string().optional()}).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["MonitoredResourceMetadataIn"])
    types["MonitoredResourceMetadataOut"] = t.struct(
        {
            "systemLabels": t.struct({"_": t.string().optional()}).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceMetadataOut"])
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
    types["TailLogEntriesRequestIn"] = t.struct(
        {
            "resourceNames": t.array(t.string()),
            "filter": t.string().optional(),
            "bufferWindow": t.string().optional(),
        }
    ).named(renames["TailLogEntriesRequestIn"])
    types["TailLogEntriesRequestOut"] = t.struct(
        {
            "resourceNames": t.array(t.string()),
            "filter": t.string().optional(),
            "bufferWindow": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TailLogEntriesRequestOut"])
    types["SourceLocationIn"] = t.struct(
        {
            "functionName": t.string().optional(),
            "line": t.string().optional(),
            "file": t.string().optional(),
        }
    ).named(renames["SourceLocationIn"])
    types["SourceLocationOut"] = t.struct(
        {
            "functionName": t.string().optional(),
            "line": t.string().optional(),
            "file": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceLocationOut"])
    types["LocationMetadataIn"] = t.struct(
        {"logAnalyticsEnabled": t.boolean().optional()}
    ).named(renames["LocationMetadataIn"])
    types["LocationMetadataOut"] = t.struct(
        {
            "logAnalyticsEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationMetadataOut"])
    types["LogEntryIn"] = t.struct(
        {
            "logName": t.string(),
            "httpRequest": t.proxy(renames["HttpRequestIn"]).optional(),
            "operation": t.proxy(renames["LogEntryOperationIn"]).optional(),
            "insertId": t.string().optional(),
            "sourceLocation": t.proxy(renames["LogEntrySourceLocationIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "textPayload": t.string().optional(),
            "spanId": t.string().optional(),
            "trace": t.string().optional(),
            "timestamp": t.string().optional(),
            "split": t.proxy(renames["LogSplitIn"]).optional(),
            "jsonPayload": t.struct({"_": t.string().optional()}).optional(),
            "resource": t.proxy(renames["MonitoredResourceIn"]),
            "traceSampled": t.boolean().optional(),
            "protoPayload": t.struct({"_": t.string().optional()}).optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["LogEntryIn"])
    types["LogEntryOut"] = t.struct(
        {
            "logName": t.string(),
            "httpRequest": t.proxy(renames["HttpRequestOut"]).optional(),
            "operation": t.proxy(renames["LogEntryOperationOut"]).optional(),
            "insertId": t.string().optional(),
            "receiveTimestamp": t.string().optional(),
            "sourceLocation": t.proxy(renames["LogEntrySourceLocationOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "textPayload": t.string().optional(),
            "spanId": t.string().optional(),
            "metadata": t.proxy(renames["MonitoredResourceMetadataOut"]).optional(),
            "trace": t.string().optional(),
            "timestamp": t.string().optional(),
            "split": t.proxy(renames["LogSplitOut"]).optional(),
            "jsonPayload": t.struct({"_": t.string().optional()}).optional(),
            "resource": t.proxy(renames["MonitoredResourceOut"]),
            "traceSampled": t.boolean().optional(),
            "protoPayload": t.struct({"_": t.string().optional()}).optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogEntryOut"])
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
    types["IndexConfigIn"] = t.struct(
        {"fieldPath": t.string(), "type": t.string()}
    ).named(renames["IndexConfigIn"])
    types["IndexConfigOut"] = t.struct(
        {
            "fieldPath": t.string(),
            "type": t.string(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexConfigOut"])
    types["LogExclusionIn"] = t.struct(
        {
            "filter": t.string(),
            "name": t.string(),
            "description": t.string().optional(),
            "disabled": t.boolean().optional(),
        }
    ).named(renames["LogExclusionIn"])
    types["LogExclusionOut"] = t.struct(
        {
            "filter": t.string(),
            "name": t.string(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogExclusionOut"])
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
    types["ListLogMetricsResponseIn"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["LogMetricIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLogMetricsResponseIn"])
    types["ListLogMetricsResponseOut"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["LogMetricOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLogMetricsResponseOut"])
    types["ExplicitIn"] = t.struct({"bounds": t.array(t.number()).optional()}).named(
        renames["ExplicitIn"]
    )
    types["ExplicitOut"] = t.struct(
        {
            "bounds": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExplicitOut"])
    types["BigQueryDatasetIn"] = t.struct({"_": t.string().optional()}).named(
        renames["BigQueryDatasetIn"]
    )
    types["BigQueryDatasetOut"] = t.struct(
        {
            "datasetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryDatasetOut"])
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
    types["CreateBucketRequestIn"] = t.struct(
        {
            "bucket": t.proxy(renames["LogBucketIn"]),
            "bucketId": t.string(),
            "parent": t.string(),
        }
    ).named(renames["CreateBucketRequestIn"])
    types["CreateBucketRequestOut"] = t.struct(
        {
            "bucket": t.proxy(renames["LogBucketOut"]),
            "bucketId": t.string(),
            "parent": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateBucketRequestOut"])
    types["UpdateBucketRequestIn"] = t.struct(
        {
            "name": t.string(),
            "updateMask": t.string(),
            "bucket": t.proxy(renames["LogBucketIn"]),
        }
    ).named(renames["UpdateBucketRequestIn"])
    types["UpdateBucketRequestOut"] = t.struct(
        {
            "name": t.string(),
            "updateMask": t.string(),
            "bucket": t.proxy(renames["LogBucketOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateBucketRequestOut"])
    types["ListViewsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "views": t.array(t.proxy(renames["LogViewIn"])).optional(),
        }
    ).named(renames["ListViewsResponseIn"])
    types["ListViewsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "views": t.array(t.proxy(renames["LogViewOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListViewsResponseOut"])
    types["ListLogsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "logNames": t.array(t.string()).optional(),
        }
    ).named(renames["ListLogsResponseIn"])
    types["ListLogsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "logNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLogsResponseOut"])
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
    types["LogBucketIn"] = t.struct(
        {
            "restrictedFields": t.array(t.string()).optional(),
            "locked": t.boolean().optional(),
            "retentionDays": t.integer().optional(),
            "analyticsEnabled": t.boolean().optional(),
            "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
            "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["LogBucketIn"])
    types["LogBucketOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "restrictedFields": t.array(t.string()).optional(),
            "locked": t.boolean().optional(),
            "retentionDays": t.integer().optional(),
            "analyticsEnabled": t.boolean().optional(),
            "cmekSettings": t.proxy(renames["CmekSettingsOut"]).optional(),
            "indexConfigs": t.array(t.proxy(renames["IndexConfigOut"])).optional(),
            "name": t.string().optional(),
            "lifecycleState": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogBucketOut"])
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
    types["HttpRequestIn"] = t.struct(
        {
            "status": t.integer().optional(),
            "responseSize": t.string().optional(),
            "referer": t.string().optional(),
            "userAgent": t.string().optional(),
            "remoteIp": t.string().optional(),
            "requestMethod": t.string().optional(),
            "cacheFillBytes": t.string().optional(),
            "cacheValidatedWithOriginServer": t.boolean().optional(),
            "cacheHit": t.boolean().optional(),
            "requestUrl": t.string().optional(),
            "protocol": t.string().optional(),
            "requestSize": t.string().optional(),
            "cacheLookup": t.boolean().optional(),
            "serverIp": t.string().optional(),
            "latency": t.string().optional(),
        }
    ).named(renames["HttpRequestIn"])
    types["HttpRequestOut"] = t.struct(
        {
            "status": t.integer().optional(),
            "responseSize": t.string().optional(),
            "referer": t.string().optional(),
            "userAgent": t.string().optional(),
            "remoteIp": t.string().optional(),
            "requestMethod": t.string().optional(),
            "cacheFillBytes": t.string().optional(),
            "cacheValidatedWithOriginServer": t.boolean().optional(),
            "cacheHit": t.boolean().optional(),
            "requestUrl": t.string().optional(),
            "protocol": t.string().optional(),
            "requestSize": t.string().optional(),
            "cacheLookup": t.boolean().optional(),
            "serverIp": t.string().optional(),
            "latency": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRequestOut"])
    types["LinkIn"] = t.struct(
        {
            "name": t.string().optional(),
            "description": t.string().optional(),
            "bigqueryDataset": t.proxy(renames["BigQueryDatasetIn"]).optional(),
        }
    ).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "bigqueryDataset": t.proxy(renames["BigQueryDatasetOut"]).optional(),
            "lifecycleState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
    types["DeleteLinkRequestIn"] = t.struct({"name": t.string()}).named(
        renames["DeleteLinkRequestIn"]
    )
    types["DeleteLinkRequestOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteLinkRequestOut"])
    types["CopyLogEntriesResponseIn"] = t.struct(
        {"logEntriesCopiedCount": t.string().optional()}
    ).named(renames["CopyLogEntriesResponseIn"])
    types["CopyLogEntriesResponseOut"] = t.struct(
        {
            "logEntriesCopiedCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyLogEntriesResponseOut"])
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
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["LogEntrySourceLocationIn"] = t.struct(
        {
            "line": t.string().optional(),
            "function": t.string().optional(),
            "file": t.string().optional(),
        }
    ).named(renames["LogEntrySourceLocationIn"])
    types["LogEntrySourceLocationOut"] = t.struct(
        {
            "line": t.string().optional(),
            "function": t.string().optional(),
            "file": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogEntrySourceLocationOut"])
    types["MetricDescriptorIn"] = t.struct(
        {
            "unit": t.string().optional(),
            "description": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
            "valueType": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "metricKind": t.string().optional(),
            "displayName": t.string().optional(),
            "launchStage": t.string().optional(),
        }
    ).named(renames["MetricDescriptorIn"])
    types["MetricDescriptorOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "description": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataOut"]).optional(),
            "valueType": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "metricKind": t.string().optional(),
            "displayName": t.string().optional(),
            "launchStage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["WriteLogEntriesRequestIn"] = t.struct(
        {
            "logName": t.string().optional(),
            "dryRun": t.boolean().optional(),
            "partialSuccess": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "resource": t.proxy(renames["MonitoredResourceIn"]).optional(),
            "entries": t.array(t.proxy(renames["LogEntryIn"])),
        }
    ).named(renames["WriteLogEntriesRequestIn"])
    types["WriteLogEntriesRequestOut"] = t.struct(
        {
            "logName": t.string().optional(),
            "dryRun": t.boolean().optional(),
            "partialSuccess": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "resource": t.proxy(renames["MonitoredResourceOut"]).optional(),
            "entries": t.array(t.proxy(renames["LogEntryOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteLogEntriesRequestOut"])
    types["MetricDescriptorMetadataIn"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "ingestDelay": t.string().optional(),
            "samplePeriod": t.string().optional(),
        }
    ).named(renames["MetricDescriptorMetadataIn"])
    types["MetricDescriptorMetadataOut"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "ingestDelay": t.string().optional(),
            "samplePeriod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorMetadataOut"])
    types["ListSinksResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "sinks": t.array(t.proxy(renames["LogSinkIn"])).optional(),
        }
    ).named(renames["ListSinksResponseIn"])
    types["ListSinksResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "sinks": t.array(t.proxy(renames["LogSinkOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSinksResponseOut"])
    types["LinkMetadataIn"] = t.struct(
        {
            "createLinkRequest": t.proxy(renames["CreateLinkRequestIn"]).optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "deleteLinkRequest": t.proxy(renames["DeleteLinkRequestIn"]).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["LinkMetadataIn"])
    types["LinkMetadataOut"] = t.struct(
        {
            "createLinkRequest": t.proxy(renames["CreateLinkRequestOut"]).optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "deleteLinkRequest": t.proxy(renames["DeleteLinkRequestOut"]).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkMetadataOut"])
    types["LinearIn"] = t.struct(
        {
            "offset": t.number().optional(),
            "numFiniteBuckets": t.integer().optional(),
            "width": t.number().optional(),
        }
    ).named(renames["LinearIn"])
    types["LinearOut"] = t.struct(
        {
            "offset": t.number().optional(),
            "numFiniteBuckets": t.integer().optional(),
            "width": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinearOut"])
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
    types["BucketMetadataIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "updateBucketRequest": t.proxy(renames["UpdateBucketRequestIn"]).optional(),
            "createBucketRequest": t.proxy(renames["CreateBucketRequestIn"]).optional(),
            "startTime": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["BucketMetadataIn"])
    types["BucketMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "updateBucketRequest": t.proxy(
                renames["UpdateBucketRequestOut"]
            ).optional(),
            "createBucketRequest": t.proxy(
                renames["CreateBucketRequestOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BucketMetadataOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["WriteLogEntriesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WriteLogEntriesResponseIn"]
    )
    types["WriteLogEntriesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WriteLogEntriesResponseOut"])
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
            "serviceAccountId": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CmekSettingsOut"])
    types["LogViewIn"] = t.struct(
        {
            "name": t.string().optional(),
            "filter": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["LogViewIn"])
    types["LogViewOut"] = t.struct(
        {
            "name": t.string().optional(),
            "filter": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogViewOut"])
    types["RequestLogIn"] = t.struct(
        {
            "host": t.string().optional(),
            "latency": t.string().optional(),
            "responseSize": t.string().optional(),
            "appId": t.string().optional(),
            "status": t.integer().optional(),
            "first": t.boolean().optional(),
            "traceId": t.string().optional(),
            "startTime": t.string().optional(),
            "megaCycles": t.string().optional(),
            "pendingTime": t.string().optional(),
            "versionId": t.string().optional(),
            "finished": t.boolean().optional(),
            "urlMapEntry": t.string().optional(),
            "ip": t.string().optional(),
            "line": t.array(t.proxy(renames["LogLineIn"])).optional(),
            "resource": t.string().optional(),
            "instanceIndex": t.integer().optional(),
            "wasLoadingRequest": t.boolean().optional(),
            "spanId": t.string().optional(),
            "method": t.string().optional(),
            "taskName": t.string().optional(),
            "traceSampled": t.boolean().optional(),
            "httpVersion": t.string().optional(),
            "requestId": t.string().optional(),
            "instanceId": t.string().optional(),
            "endTime": t.string().optional(),
            "nickname": t.string().optional(),
            "referrer": t.string().optional(),
            "appEngineRelease": t.string().optional(),
            "cost": t.number().optional(),
            "userAgent": t.string().optional(),
            "moduleId": t.string().optional(),
            "sourceReference": t.array(
                t.proxy(renames["SourceReferenceIn"])
            ).optional(),
            "taskQueueName": t.string().optional(),
        }
    ).named(renames["RequestLogIn"])
    types["RequestLogOut"] = t.struct(
        {
            "host": t.string().optional(),
            "latency": t.string().optional(),
            "responseSize": t.string().optional(),
            "appId": t.string().optional(),
            "status": t.integer().optional(),
            "first": t.boolean().optional(),
            "traceId": t.string().optional(),
            "startTime": t.string().optional(),
            "megaCycles": t.string().optional(),
            "pendingTime": t.string().optional(),
            "versionId": t.string().optional(),
            "finished": t.boolean().optional(),
            "urlMapEntry": t.string().optional(),
            "ip": t.string().optional(),
            "line": t.array(t.proxy(renames["LogLineOut"])).optional(),
            "resource": t.string().optional(),
            "instanceIndex": t.integer().optional(),
            "wasLoadingRequest": t.boolean().optional(),
            "spanId": t.string().optional(),
            "method": t.string().optional(),
            "taskName": t.string().optional(),
            "traceSampled": t.boolean().optional(),
            "httpVersion": t.string().optional(),
            "requestId": t.string().optional(),
            "instanceId": t.string().optional(),
            "endTime": t.string().optional(),
            "nickname": t.string().optional(),
            "referrer": t.string().optional(),
            "appEngineRelease": t.string().optional(),
            "cost": t.number().optional(),
            "userAgent": t.string().optional(),
            "moduleId": t.string().optional(),
            "sourceReference": t.array(
                t.proxy(renames["SourceReferenceOut"])
            ).optional(),
            "taskQueueName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestLogOut"])
    types["LogLineIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "sourceLocation": t.proxy(renames["SourceLocationIn"]).optional(),
            "logMessage": t.string().optional(),
            "time": t.string().optional(),
        }
    ).named(renames["LogLineIn"])
    types["LogLineOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "sourceLocation": t.proxy(renames["SourceLocationOut"]).optional(),
            "logMessage": t.string().optional(),
            "time": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogLineOut"])
    types["SettingsIn"] = t.struct(
        {
            "disableDefaultSink": t.boolean().optional(),
            "storageLocation": t.string().optional(),
            "kmsKeyName": t.string().optional(),
        }
    ).named(renames["SettingsIn"])
    types["SettingsOut"] = t.struct(
        {
            "disableDefaultSink": t.boolean().optional(),
            "name": t.string().optional(),
            "storageLocation": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "loggingServiceAccountId": t.string().optional(),
            "kmsServiceAccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettingsOut"])
    types["MonitoredResourceIn"] = t.struct(
        {"type": t.string(), "labels": t.struct({"_": t.string().optional()})}
    ).named(renames["MonitoredResourceIn"])
    types["MonitoredResourceOut"] = t.struct(
        {
            "type": t.string(),
            "labels": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceOut"])
    types["ExponentialIn"] = t.struct(
        {
            "numFiniteBuckets": t.integer().optional(),
            "scale": t.number().optional(),
            "growthFactor": t.number().optional(),
        }
    ).named(renames["ExponentialIn"])
    types["ExponentialOut"] = t.struct(
        {
            "numFiniteBuckets": t.integer().optional(),
            "scale": t.number().optional(),
            "growthFactor": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExponentialOut"])
    types["LogSinkIn"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "outputVersionFormat": t.string().optional(),
            "destination": t.string(),
            "includeChildren": t.boolean().optional(),
            "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
            "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
            "filter": t.string().optional(),
        }
    ).named(renames["LogSinkIn"])
    types["LogSinkOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "disabled": t.boolean().optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "outputVersionFormat": t.string().optional(),
            "destination": t.string(),
            "includeChildren": t.boolean().optional(),
            "bigqueryOptions": t.proxy(renames["BigQueryOptionsOut"]).optional(),
            "exclusions": t.array(t.proxy(renames["LogExclusionOut"])).optional(),
            "filter": t.string().optional(),
            "writerIdentity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogSinkOut"])
    types["CopyLogEntriesMetadataIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "progress": t.integer().optional(),
            "cancellationRequested": t.boolean().optional(),
            "state": t.string().optional(),
            "writerIdentity": t.string().optional(),
            "endTime": t.string().optional(),
            "request": t.proxy(renames["CopyLogEntriesRequestIn"]).optional(),
        }
    ).named(renames["CopyLogEntriesMetadataIn"])
    types["CopyLogEntriesMetadataOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "progress": t.integer().optional(),
            "cancellationRequested": t.boolean().optional(),
            "state": t.string().optional(),
            "writerIdentity": t.string().optional(),
            "endTime": t.string().optional(),
            "request": t.proxy(renames["CopyLogEntriesRequestOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyLogEntriesMetadataOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["ListLogEntriesRequestIn"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "projectIds": t.array(t.string()).optional(),
            "resourceNames": t.array(t.string()),
            "orderBy": t.string().optional(),
            "filter": t.string().optional(),
        }
    ).named(renames["ListLogEntriesRequestIn"])
    types["ListLogEntriesRequestOut"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "projectIds": t.array(t.string()).optional(),
            "resourceNames": t.array(t.string()),
            "orderBy": t.string().optional(),
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLogEntriesRequestOut"])
    types["LogEntryOperationIn"] = t.struct(
        {
            "producer": t.string().optional(),
            "last": t.boolean().optional(),
            "first": t.boolean().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["LogEntryOperationIn"])
    types["LogEntryOperationOut"] = t.struct(
        {
            "producer": t.string().optional(),
            "last": t.boolean().optional(),
            "first": t.boolean().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogEntryOperationOut"])
    types["UndeleteBucketRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UndeleteBucketRequestIn"]
    )
    types["UndeleteBucketRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteBucketRequestOut"])
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
    types["LogMetricIn"] = t.struct(
        {
            "bucketName": t.string().optional(),
            "description": t.string().optional(),
            "valueExtractor": t.string().optional(),
            "metricDescriptor": t.proxy(renames["MetricDescriptorIn"]).optional(),
            "bucketOptions": t.proxy(renames["BucketOptionsIn"]).optional(),
            "version": t.string().optional(),
            "name": t.string(),
            "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
            "filter": t.string(),
            "disabled": t.boolean().optional(),
        }
    ).named(renames["LogMetricIn"])
    types["LogMetricOut"] = t.struct(
        {
            "bucketName": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "valueExtractor": t.string().optional(),
            "metricDescriptor": t.proxy(renames["MetricDescriptorOut"]).optional(),
            "bucketOptions": t.proxy(renames["BucketOptionsOut"]).optional(),
            "version": t.string().optional(),
            "name": t.string(),
            "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
            "filter": t.string(),
            "createTime": t.string().optional(),
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogMetricOut"])
    types["MonitoredResourceDescriptorIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])),
            "type": t.string(),
            "name": t.string().optional(),
            "launchStage": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["MonitoredResourceDescriptorIn"])
    types["MonitoredResourceDescriptorOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])),
            "type": t.string(),
            "name": t.string().optional(),
            "launchStage": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceDescriptorOut"])
    types["LogSplitIn"] = t.struct(
        {
            "index": t.integer().optional(),
            "totalSplits": t.integer().optional(),
            "uid": t.string().optional(),
        }
    ).named(renames["LogSplitIn"])
    types["LogSplitOut"] = t.struct(
        {
            "index": t.integer().optional(),
            "totalSplits": t.integer().optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogSplitOut"])
    types["BigQueryOptionsIn"] = t.struct(
        {"usePartitionedTables": t.boolean().optional()}
    ).named(renames["BigQueryOptionsIn"])
    types["BigQueryOptionsOut"] = t.struct(
        {
            "usesTimestampColumnPartitioning": t.boolean().optional(),
            "usePartitionedTables": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryOptionsOut"])

    functions = {}
    functions["entriesWrite"] = logging.post(
        "v2/entries:tail",
        t.struct(
            {
                "resourceNames": t.array(t.string()),
                "filter": t.string().optional(),
                "bufferWindow": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TailLogEntriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["entriesCopy"] = logging.post(
        "v2/entries:tail",
        t.struct(
            {
                "resourceNames": t.array(t.string()),
                "filter": t.string().optional(),
                "bufferWindow": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TailLogEntriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["entriesList"] = logging.post(
        "v2/entries:tail",
        t.struct(
            {
                "resourceNames": t.array(t.string()),
                "filter": t.string().optional(),
                "bufferWindow": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TailLogEntriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["entriesTail"] = logging.post(
        "v2/entries:tail",
        t.struct(
            {
                "resourceNames": t.array(t.string()),
                "filter": t.string().optional(),
                "bufferWindow": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TailLogEntriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sinksDelete"] = logging.post(
        "v2/{parent}/sinks",
        t.struct(
            {
                "uniqueWriterIdentity": t.boolean().optional(),
                "customWriterIdentity": t.string().optional(),
                "parent": t.string(),
                "disabled": t.boolean().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "destination": t.string(),
                "includeChildren": t.boolean().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sinksList"] = logging.post(
        "v2/{parent}/sinks",
        t.struct(
            {
                "uniqueWriterIdentity": t.boolean().optional(),
                "customWriterIdentity": t.string().optional(),
                "parent": t.string(),
                "disabled": t.boolean().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "destination": t.string(),
                "includeChildren": t.boolean().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sinksGet"] = logging.post(
        "v2/{parent}/sinks",
        t.struct(
            {
                "uniqueWriterIdentity": t.boolean().optional(),
                "customWriterIdentity": t.string().optional(),
                "parent": t.string(),
                "disabled": t.boolean().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "destination": t.string(),
                "includeChildren": t.boolean().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sinksUpdate"] = logging.post(
        "v2/{parent}/sinks",
        t.struct(
            {
                "uniqueWriterIdentity": t.boolean().optional(),
                "customWriterIdentity": t.string().optional(),
                "parent": t.string(),
                "disabled": t.boolean().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "destination": t.string(),
                "includeChildren": t.boolean().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sinksCreate"] = logging.post(
        "v2/{parent}/sinks",
        t.struct(
            {
                "uniqueWriterIdentity": t.boolean().optional(),
                "customWriterIdentity": t.string().optional(),
                "parent": t.string(),
                "disabled": t.boolean().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "destination": t.string(),
                "includeChildren": t.boolean().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["logsList"] = logging.delete(
        "v2/{logName}",
        t.struct({"logName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["logsDelete"] = logging.delete(
        "v2/{logName}",
        t.struct({"logName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsUpdateSettings"] = logging.get(
        "v2/{name}/cmekSettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CmekSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsUpdateCmekSettings"] = logging.get(
        "v2/{name}/cmekSettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CmekSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGetSettings"] = logging.get(
        "v2/{name}/cmekSettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CmekSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGetCmekSettings"] = logging.get(
        "v2/{name}/cmekSettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CmekSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsGet"] = logging.get(
        "v2/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsList"] = logging.get(
        "v2/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsPatch"] = logging.post(
        "v2/{name}:updateAsync",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "restrictedFields": t.array(t.string()).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsCreate"] = logging.post(
        "v2/{name}:updateAsync",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "restrictedFields": t.array(t.string()).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsUndelete"] = logging.post(
        "v2/{name}:updateAsync",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "restrictedFields": t.array(t.string()).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsDelete"] = logging.post(
        "v2/{name}:updateAsync",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "restrictedFields": t.array(t.string()).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsList"] = logging.post(
        "v2/{name}:updateAsync",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "restrictedFields": t.array(t.string()).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsCreateAsync"] = logging.post(
        "v2/{name}:updateAsync",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "restrictedFields": t.array(t.string()).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsGet"] = logging.post(
        "v2/{name}:updateAsync",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "restrictedFields": t.array(t.string()).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsUpdateAsync"] = logging.post(
        "v2/{name}:updateAsync",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "restrictedFields": t.array(t.string()).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
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
    functions["organizationsLocationsBucketsViewsList"] = logging.get(
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
                "pageSize": t.integer().optional(),
                "resourceNames": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsLinksList"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsLinksCreate"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsLinksDelete"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsLinksGet"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsOperationsList"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsOperationsCancel"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsOperationsGet"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLogsDelete"] = logging.get(
        "v2/{parent}/logs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "resourceNames": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLogsList"] = logging.get(
        "v2/{parent}/logs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "resourceNames": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSinksDelete"] = logging.get(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSinksCreate"] = logging.get(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSinksPatch"] = logging.get(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSinksList"] = logging.get(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSinksUpdate"] = logging.get(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSinksGet"] = logging.get(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsExclusionsCreate"] = logging.get(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExclusionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["exclusionsGet"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["exclusionsCreate"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["exclusionsPatch"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["exclusionsList"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["exclusionsDelete"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsGet"] = logging.get(
        "v2/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsList"] = logging.get(
        "v2/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsCreateAsync"] = logging.post(
        "v2/{parent}/buckets",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "restrictedFields": t.array(t.string()).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsList"] = logging.post(
        "v2/{parent}/buckets",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "restrictedFields": t.array(t.string()).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsUndelete"] = logging.post(
        "v2/{parent}/buckets",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "restrictedFields": t.array(t.string()).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsUpdateAsync"] = logging.post(
        "v2/{parent}/buckets",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "restrictedFields": t.array(t.string()).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsPatch"] = logging.post(
        "v2/{parent}/buckets",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "restrictedFields": t.array(t.string()).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsDelete"] = logging.post(
        "v2/{parent}/buckets",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "restrictedFields": t.array(t.string()).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsGet"] = logging.post(
        "v2/{parent}/buckets",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "restrictedFields": t.array(t.string()).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsCreate"] = logging.post(
        "v2/{parent}/buckets",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "restrictedFields": t.array(t.string()).optional(),
                "locked": t.boolean().optional(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsLinksCreate"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsLinksDelete"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsLinksList"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsLinksGet"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsViewsDelete"] = logging.post(
        "v2/{parent}/views",
        t.struct(
            {
                "viewId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
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
                "name": t.string().optional(),
                "filter": t.string().optional(),
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
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsViewsGet"] = logging.post(
        "v2/{parent}/views",
        t.struct(
            {
                "viewId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
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
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsOperationsGet"] = logging.post(
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
    functions["locationsOperationsList"] = logging.post(
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
    functions["locationsOperationsCancel"] = logging.post(
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
    functions["foldersSinksGet"] = logging.patch(
        "v2/{sinkName}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "sinkName": t.string(),
                "uniqueWriterIdentity": t.boolean().optional(),
                "customWriterIdentity": t.string().optional(),
                "disabled": t.boolean().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "destination": t.string(),
                "includeChildren": t.boolean().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
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
                "updateMask": t.string().optional(),
                "sinkName": t.string(),
                "uniqueWriterIdentity": t.boolean().optional(),
                "customWriterIdentity": t.string().optional(),
                "disabled": t.boolean().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "destination": t.string(),
                "includeChildren": t.boolean().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
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
                "updateMask": t.string().optional(),
                "sinkName": t.string(),
                "uniqueWriterIdentity": t.boolean().optional(),
                "customWriterIdentity": t.string().optional(),
                "disabled": t.boolean().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "destination": t.string(),
                "includeChildren": t.boolean().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
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
                "updateMask": t.string().optional(),
                "sinkName": t.string(),
                "uniqueWriterIdentity": t.boolean().optional(),
                "customWriterIdentity": t.string().optional(),
                "disabled": t.boolean().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "destination": t.string(),
                "includeChildren": t.boolean().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSinksCreate"] = logging.patch(
        "v2/{sinkName}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "sinkName": t.string(),
                "uniqueWriterIdentity": t.boolean().optional(),
                "customWriterIdentity": t.string().optional(),
                "disabled": t.boolean().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "destination": t.string(),
                "includeChildren": t.boolean().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
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
                "updateMask": t.string().optional(),
                "sinkName": t.string(),
                "uniqueWriterIdentity": t.boolean().optional(),
                "customWriterIdentity": t.string().optional(),
                "disabled": t.boolean().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "destination": t.string(),
                "includeChildren": t.boolean().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsGet"] = logging.get(
        "v2/{name}/locations",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsOperationsList"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsOperationsCancel"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsOperationsGet"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsCreateAsync"] = logging.post(
        "v2/{name}:undelete",
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
    functions["foldersLocationsBucketsUpdateAsync"] = logging.post(
        "v2/{name}:undelete",
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
    functions["foldersLocationsBucketsDelete"] = logging.post(
        "v2/{name}:undelete",
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
    functions["foldersLocationsBucketsCreate"] = logging.post(
        "v2/{name}:undelete",
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
    functions["foldersLocationsBucketsList"] = logging.post(
        "v2/{name}:undelete",
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
    functions["foldersLocationsBucketsPatch"] = logging.post(
        "v2/{name}:undelete",
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
    functions["foldersLocationsBucketsGet"] = logging.post(
        "v2/{name}:undelete",
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
    functions["foldersLocationsBucketsUndelete"] = logging.post(
        "v2/{name}:undelete",
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
    functions["foldersLocationsBucketsLinksGet"] = logging.post(
        "v2/{parent}/links",
        t.struct(
            {
                "linkId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsLinksList"] = logging.post(
        "v2/{parent}/links",
        t.struct(
            {
                "linkId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsLinksDelete"] = logging.post(
        "v2/{parent}/links",
        t.struct(
            {
                "linkId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsLinksCreate"] = logging.post(
        "v2/{parent}/links",
        t.struct(
            {
                "linkId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsViewsDelete"] = logging.get(
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
    functions["foldersLocationsBucketsViewsGet"] = logging.get(
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
    functions["foldersLocationsBucketsViewsCreate"] = logging.get(
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
    functions["foldersLocationsBucketsViewsPatch"] = logging.get(
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
    functions["foldersLocationsBucketsViewsList"] = logging.get(
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
    functions["foldersLocationsBucketsViewsLogsList"] = logging.get(
        "v2/{parent}/logs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "resourceNames": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
    functions["foldersLogsList"] = logging.get(
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
    functions["foldersExclusionsList"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersExclusionsCreate"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersExclusionsPatch"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersExclusionsDelete"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersExclusionsGet"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogExclusionOut"]),
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
    functions["v2UpdateSettings"] = logging.patch(
        "v2/{name}/cmekSettings",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "kmsKeyVersionName": t.string().optional(),
                "kmsKeyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CmekSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v2GetSettings"] = logging.patch(
        "v2/{name}/cmekSettings",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "kmsKeyVersionName": t.string().optional(),
                "kmsKeyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CmekSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v2GetCmekSettings"] = logging.patch(
        "v2/{name}/cmekSettings",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "kmsKeyVersionName": t.string().optional(),
                "kmsKeyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CmekSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v2UpdateCmekSettings"] = logging.patch(
        "v2/{name}/cmekSettings",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "kmsKeyVersionName": t.string().optional(),
                "kmsKeyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CmekSettingsOut"]),
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
    functions["projectsSinksUpdate"] = logging.patch(
        "v2/{sinkName}",
        t.struct(
            {
                "uniqueWriterIdentity": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "customWriterIdentity": t.string().optional(),
                "sinkName": t.string(),
                "disabled": t.boolean().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "destination": t.string(),
                "includeChildren": t.boolean().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSinksList"] = logging.patch(
        "v2/{sinkName}",
        t.struct(
            {
                "uniqueWriterIdentity": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "customWriterIdentity": t.string().optional(),
                "sinkName": t.string(),
                "disabled": t.boolean().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "destination": t.string(),
                "includeChildren": t.boolean().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSinksCreate"] = logging.patch(
        "v2/{sinkName}",
        t.struct(
            {
                "uniqueWriterIdentity": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "customWriterIdentity": t.string().optional(),
                "sinkName": t.string(),
                "disabled": t.boolean().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "destination": t.string(),
                "includeChildren": t.boolean().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSinksGet"] = logging.patch(
        "v2/{sinkName}",
        t.struct(
            {
                "uniqueWriterIdentity": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "customWriterIdentity": t.string().optional(),
                "sinkName": t.string(),
                "disabled": t.boolean().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "destination": t.string(),
                "includeChildren": t.boolean().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSinksDelete"] = logging.patch(
        "v2/{sinkName}",
        t.struct(
            {
                "uniqueWriterIdentity": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "customWriterIdentity": t.string().optional(),
                "sinkName": t.string(),
                "disabled": t.boolean().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "destination": t.string(),
                "includeChildren": t.boolean().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSinksPatch"] = logging.patch(
        "v2/{sinkName}",
        t.struct(
            {
                "uniqueWriterIdentity": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "customWriterIdentity": t.string().optional(),
                "sinkName": t.string(),
                "disabled": t.boolean().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "outputVersionFormat": t.string().optional(),
                "destination": t.string(),
                "includeChildren": t.boolean().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = logging.get(
        "v2/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = logging.get(
        "v2/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsUpdateAsync"] = logging.get(
        "v2/{parent}/buckets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBucketsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsPatch"] = logging.get(
        "v2/{parent}/buckets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBucketsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsUndelete"] = logging.get(
        "v2/{parent}/buckets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBucketsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsCreateAsync"] = logging.get(
        "v2/{parent}/buckets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBucketsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsCreate"] = logging.get(
        "v2/{parent}/buckets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBucketsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsGet"] = logging.get(
        "v2/{parent}/buckets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBucketsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsDelete"] = logging.get(
        "v2/{parent}/buckets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBucketsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsList"] = logging.get(
        "v2/{parent}/buckets",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBucketsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsViewsList"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "filter": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsViewsDelete"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "filter": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsViewsCreate"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "filter": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsViewsGet"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "filter": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsViewsPatch"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "filter": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsViewsLogsList"] = logging.get(
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
    functions["projectsLocationsBucketsLinksList"] = logging.post(
        "v2/{parent}/links",
        t.struct(
            {
                "linkId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsLinksGet"] = logging.post(
        "v2/{parent}/links",
        t.struct(
            {
                "linkId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsLinksDelete"] = logging.post(
        "v2/{parent}/links",
        t.struct(
            {
                "linkId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsLinksCreate"] = logging.post(
        "v2/{parent}/links",
        t.struct(
            {
                "linkId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsExclusionsPatch"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsExclusionsList"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsExclusionsCreate"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsExclusionsGet"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsExclusionsDelete"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
                "valueExtractor": t.string().optional(),
                "metricDescriptor": t.proxy(renames["MetricDescriptorIn"]).optional(),
                "bucketOptions": t.proxy(renames["BucketOptionsIn"]).optional(),
                "version": t.string().optional(),
                "name": t.string(),
                "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
                "filter": t.string(),
                "disabled": t.boolean().optional(),
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
                "valueExtractor": t.string().optional(),
                "metricDescriptor": t.proxy(renames["MetricDescriptorIn"]).optional(),
                "bucketOptions": t.proxy(renames["BucketOptionsIn"]).optional(),
                "version": t.string().optional(),
                "name": t.string(),
                "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
                "filter": t.string(),
                "disabled": t.boolean().optional(),
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
                "valueExtractor": t.string().optional(),
                "metricDescriptor": t.proxy(renames["MetricDescriptorIn"]).optional(),
                "bucketOptions": t.proxy(renames["BucketOptionsIn"]).optional(),
                "version": t.string().optional(),
                "name": t.string(),
                "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
                "filter": t.string(),
                "disabled": t.boolean().optional(),
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
                "valueExtractor": t.string().optional(),
                "metricDescriptor": t.proxy(renames["MetricDescriptorIn"]).optional(),
                "bucketOptions": t.proxy(renames["BucketOptionsIn"]).optional(),
                "version": t.string().optional(),
                "name": t.string(),
                "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
                "filter": t.string(),
                "disabled": t.boolean().optional(),
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
                "valueExtractor": t.string().optional(),
                "metricDescriptor": t.proxy(renames["MetricDescriptorIn"]).optional(),
                "bucketOptions": t.proxy(renames["BucketOptionsIn"]).optional(),
                "version": t.string().optional(),
                "name": t.string(),
                "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
                "filter": t.string(),
                "disabled": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogMetricOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLogsDelete"] = logging.get(
        "v2/{parent}/logs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "resourceNames": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLogsList"] = logging.get(
        "v2/{parent}/logs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "resourceNames": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsGetSettings"] = logging.get(
        "v2/{name}/cmekSettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CmekSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsGetCmekSettings"] = logging.get(
        "v2/{name}/cmekSettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CmekSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsExclusionsGet"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsExclusionsList"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsExclusionsCreate"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsExclusionsPatch"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsExclusionsDelete"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsGet"] = logging.get(
        "v2/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsOperationsGet"] = logging.get(
        "v2/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsOperationsCancel"] = logging.get(
        "v2/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsOperationsList"] = logging.get(
        "v2/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsList"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsCreateAsync"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsUndelete"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsDelete"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsUpdateAsync"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsPatch"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsCreate"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsGet"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsViewsPatch"] = logging.post(
        "v2/{parent}/views",
        t.struct(
            {
                "viewId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsViewsList"] = logging.post(
        "v2/{parent}/views",
        t.struct(
            {
                "viewId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsViewsDelete"] = logging.post(
        "v2/{parent}/views",
        t.struct(
            {
                "viewId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsViewsGet"] = logging.post(
        "v2/{parent}/views",
        t.struct(
            {
                "viewId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsViewsCreate"] = logging.post(
        "v2/{parent}/views",
        t.struct(
            {
                "viewId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsViewsLogsList"] = logging.get(
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
    functions["billingAccountsLocationsBucketsLinksList"] = logging.post(
        "v2/{parent}/links",
        t.struct(
            {
                "linkId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsLinksGet"] = logging.post(
        "v2/{parent}/links",
        t.struct(
            {
                "linkId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsLinksDelete"] = logging.post(
        "v2/{parent}/links",
        t.struct(
            {
                "linkId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsLinksCreate"] = logging.post(
        "v2/{parent}/links",
        t.struct(
            {
                "linkId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "bigqueryDataset": t.proxy(renames["BigQueryDatasetIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsSinksUpdate"] = logging.delete(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsSinksPatch"] = logging.delete(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsSinksList"] = logging.delete(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsSinksCreate"] = logging.delete(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsSinksGet"] = logging.delete(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsSinksDelete"] = logging.delete(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLogsList"] = logging.delete(
        "v2/{logName}",
        t.struct({"logName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLogsDelete"] = logging.delete(
        "v2/{logName}",
        t.struct({"logName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="logging", renames=renames, types=Box(types), functions=Box(functions)
    )
