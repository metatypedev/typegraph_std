from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_logging() -> Import:
    logging = HTTPRuntime("https://logging.googleapis.com/")

    renames = {
        "ErrorResponse": "_logging_1_ErrorResponse",
        "MetricDescriptorIn": "_logging_2_MetricDescriptorIn",
        "MetricDescriptorOut": "_logging_3_MetricDescriptorOut",
        "MetricDescriptorMetadataIn": "_logging_4_MetricDescriptorMetadataIn",
        "MetricDescriptorMetadataOut": "_logging_5_MetricDescriptorMetadataOut",
        "LogMetricIn": "_logging_6_LogMetricIn",
        "LogMetricOut": "_logging_7_LogMetricOut",
        "ListOperationsResponseIn": "_logging_8_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_logging_9_ListOperationsResponseOut",
        "SuppressionInfoIn": "_logging_10_SuppressionInfoIn",
        "SuppressionInfoOut": "_logging_11_SuppressionInfoOut",
        "LogSplitIn": "_logging_12_LogSplitIn",
        "LogSplitOut": "_logging_13_LogSplitOut",
        "OperationIn": "_logging_14_OperationIn",
        "OperationOut": "_logging_15_OperationOut",
        "ExponentialIn": "_logging_16_ExponentialIn",
        "ExponentialOut": "_logging_17_ExponentialOut",
        "BucketOptionsIn": "_logging_18_BucketOptionsIn",
        "BucketOptionsOut": "_logging_19_BucketOptionsOut",
        "ListExclusionsResponseIn": "_logging_20_ListExclusionsResponseIn",
        "ListExclusionsResponseOut": "_logging_21_ListExclusionsResponseOut",
        "CopyLogEntriesMetadataIn": "_logging_22_CopyLogEntriesMetadataIn",
        "CopyLogEntriesMetadataOut": "_logging_23_CopyLogEntriesMetadataOut",
        "LogLineIn": "_logging_24_LogLineIn",
        "LogLineOut": "_logging_25_LogLineOut",
        "MonitoredResourceIn": "_logging_26_MonitoredResourceIn",
        "MonitoredResourceOut": "_logging_27_MonitoredResourceOut",
        "CopyLogEntriesRequestIn": "_logging_28_CopyLogEntriesRequestIn",
        "CopyLogEntriesRequestOut": "_logging_29_CopyLogEntriesRequestOut",
        "ListSinksResponseIn": "_logging_30_ListSinksResponseIn",
        "ListSinksResponseOut": "_logging_31_ListSinksResponseOut",
        "LogViewIn": "_logging_32_LogViewIn",
        "LogViewOut": "_logging_33_LogViewOut",
        "WriteLogEntriesResponseIn": "_logging_34_WriteLogEntriesResponseIn",
        "WriteLogEntriesResponseOut": "_logging_35_WriteLogEntriesResponseOut",
        "StatusIn": "_logging_36_StatusIn",
        "StatusOut": "_logging_37_StatusOut",
        "ListLogsResponseIn": "_logging_38_ListLogsResponseIn",
        "ListLogsResponseOut": "_logging_39_ListLogsResponseOut",
        "CmekSettingsIn": "_logging_40_CmekSettingsIn",
        "CmekSettingsOut": "_logging_41_CmekSettingsOut",
        "DeleteLinkRequestIn": "_logging_42_DeleteLinkRequestIn",
        "DeleteLinkRequestOut": "_logging_43_DeleteLinkRequestOut",
        "BigQueryOptionsIn": "_logging_44_BigQueryOptionsIn",
        "BigQueryOptionsOut": "_logging_45_BigQueryOptionsOut",
        "MonitoredResourceDescriptorIn": "_logging_46_MonitoredResourceDescriptorIn",
        "MonitoredResourceDescriptorOut": "_logging_47_MonitoredResourceDescriptorOut",
        "CreateBucketRequestIn": "_logging_48_CreateBucketRequestIn",
        "CreateBucketRequestOut": "_logging_49_CreateBucketRequestOut",
        "CreateLinkRequestIn": "_logging_50_CreateLinkRequestIn",
        "CreateLinkRequestOut": "_logging_51_CreateLinkRequestOut",
        "ListLogEntriesResponseIn": "_logging_52_ListLogEntriesResponseIn",
        "ListLogEntriesResponseOut": "_logging_53_ListLogEntriesResponseOut",
        "LogBucketIn": "_logging_54_LogBucketIn",
        "LogBucketOut": "_logging_55_LogBucketOut",
        "LogExclusionIn": "_logging_56_LogExclusionIn",
        "LogExclusionOut": "_logging_57_LogExclusionOut",
        "ExplicitIn": "_logging_58_ExplicitIn",
        "ExplicitOut": "_logging_59_ExplicitOut",
        "ListLogMetricsResponseIn": "_logging_60_ListLogMetricsResponseIn",
        "ListLogMetricsResponseOut": "_logging_61_ListLogMetricsResponseOut",
        "ListLogEntriesRequestIn": "_logging_62_ListLogEntriesRequestIn",
        "ListLogEntriesRequestOut": "_logging_63_ListLogEntriesRequestOut",
        "HttpRequestIn": "_logging_64_HttpRequestIn",
        "HttpRequestOut": "_logging_65_HttpRequestOut",
        "WriteLogEntriesRequestIn": "_logging_66_WriteLogEntriesRequestIn",
        "WriteLogEntriesRequestOut": "_logging_67_WriteLogEntriesRequestOut",
        "LinearIn": "_logging_68_LinearIn",
        "LinearOut": "_logging_69_LinearOut",
        "LinkIn": "_logging_70_LinkIn",
        "LinkOut": "_logging_71_LinkOut",
        "LogEntrySourceLocationIn": "_logging_72_LogEntrySourceLocationIn",
        "LogEntrySourceLocationOut": "_logging_73_LogEntrySourceLocationOut",
        "LogEntryOperationIn": "_logging_74_LogEntryOperationIn",
        "LogEntryOperationOut": "_logging_75_LogEntryOperationOut",
        "TailLogEntriesRequestIn": "_logging_76_TailLogEntriesRequestIn",
        "TailLogEntriesRequestOut": "_logging_77_TailLogEntriesRequestOut",
        "ListViewsResponseIn": "_logging_78_ListViewsResponseIn",
        "ListViewsResponseOut": "_logging_79_ListViewsResponseOut",
        "LogSinkIn": "_logging_80_LogSinkIn",
        "LogSinkOut": "_logging_81_LogSinkOut",
        "EmptyIn": "_logging_82_EmptyIn",
        "EmptyOut": "_logging_83_EmptyOut",
        "ListBucketsResponseIn": "_logging_84_ListBucketsResponseIn",
        "ListBucketsResponseOut": "_logging_85_ListBucketsResponseOut",
        "MonitoredResourceMetadataIn": "_logging_86_MonitoredResourceMetadataIn",
        "MonitoredResourceMetadataOut": "_logging_87_MonitoredResourceMetadataOut",
        "LocationIn": "_logging_88_LocationIn",
        "LocationOut": "_logging_89_LocationOut",
        "ListLocationsResponseIn": "_logging_90_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_logging_91_ListLocationsResponseOut",
        "BucketMetadataIn": "_logging_92_BucketMetadataIn",
        "BucketMetadataOut": "_logging_93_BucketMetadataOut",
        "TailLogEntriesResponseIn": "_logging_94_TailLogEntriesResponseIn",
        "TailLogEntriesResponseOut": "_logging_95_TailLogEntriesResponseOut",
        "RequestLogIn": "_logging_96_RequestLogIn",
        "RequestLogOut": "_logging_97_RequestLogOut",
        "LogEntryIn": "_logging_98_LogEntryIn",
        "LogEntryOut": "_logging_99_LogEntryOut",
        "ListMonitoredResourceDescriptorsResponseIn": "_logging_100_ListMonitoredResourceDescriptorsResponseIn",
        "ListMonitoredResourceDescriptorsResponseOut": "_logging_101_ListMonitoredResourceDescriptorsResponseOut",
        "UndeleteBucketRequestIn": "_logging_102_UndeleteBucketRequestIn",
        "UndeleteBucketRequestOut": "_logging_103_UndeleteBucketRequestOut",
        "CancelOperationRequestIn": "_logging_104_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_logging_105_CancelOperationRequestOut",
        "BigQueryDatasetIn": "_logging_106_BigQueryDatasetIn",
        "BigQueryDatasetOut": "_logging_107_BigQueryDatasetOut",
        "CopyLogEntriesResponseIn": "_logging_108_CopyLogEntriesResponseIn",
        "CopyLogEntriesResponseOut": "_logging_109_CopyLogEntriesResponseOut",
        "LocationMetadataIn": "_logging_110_LocationMetadataIn",
        "LocationMetadataOut": "_logging_111_LocationMetadataOut",
        "LabelDescriptorIn": "_logging_112_LabelDescriptorIn",
        "LabelDescriptorOut": "_logging_113_LabelDescriptorOut",
        "SourceLocationIn": "_logging_114_SourceLocationIn",
        "SourceLocationOut": "_logging_115_SourceLocationOut",
        "SourceReferenceIn": "_logging_116_SourceReferenceIn",
        "SourceReferenceOut": "_logging_117_SourceReferenceOut",
        "ListLinksResponseIn": "_logging_118_ListLinksResponseIn",
        "ListLinksResponseOut": "_logging_119_ListLinksResponseOut",
        "LinkMetadataIn": "_logging_120_LinkMetadataIn",
        "LinkMetadataOut": "_logging_121_LinkMetadataOut",
        "SettingsIn": "_logging_122_SettingsIn",
        "SettingsOut": "_logging_123_SettingsOut",
        "IndexConfigIn": "_logging_124_IndexConfigIn",
        "IndexConfigOut": "_logging_125_IndexConfigOut",
        "UpdateBucketRequestIn": "_logging_126_UpdateBucketRequestIn",
        "UpdateBucketRequestOut": "_logging_127_UpdateBucketRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["MetricDescriptorIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
            "valueType": t.string().optional(),
            "launchStage": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "unit": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "metricKind": t.string().optional(),
        }
    ).named(renames["MetricDescriptorIn"])
    types["MetricDescriptorOut"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataOut"]).optional(),
            "valueType": t.string().optional(),
            "launchStage": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "unit": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "metricKind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorOut"])
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
    types["LogMetricIn"] = t.struct(
        {
            "name": t.string(),
            "metricDescriptor": t.proxy(renames["MetricDescriptorIn"]).optional(),
            "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
            "bucketOptions": t.proxy(renames["BucketOptionsIn"]).optional(),
            "description": t.string().optional(),
            "version": t.string().optional(),
            "valueExtractor": t.string().optional(),
            "disabled": t.boolean().optional(),
            "filter": t.string(),
            "bucketName": t.string().optional(),
        }
    ).named(renames["LogMetricIn"])
    types["LogMetricOut"] = t.struct(
        {
            "name": t.string(),
            "metricDescriptor": t.proxy(renames["MetricDescriptorOut"]).optional(),
            "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
            "bucketOptions": t.proxy(renames["BucketOptionsOut"]).optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "version": t.string().optional(),
            "valueExtractor": t.string().optional(),
            "disabled": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "filter": t.string(),
            "bucketName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogMetricOut"])
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
    types["LogSplitIn"] = t.struct(
        {
            "index": t.integer().optional(),
            "uid": t.string().optional(),
            "totalSplits": t.integer().optional(),
        }
    ).named(renames["LogSplitIn"])
    types["LogSplitOut"] = t.struct(
        {
            "index": t.integer().optional(),
            "uid": t.string().optional(),
            "totalSplits": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogSplitOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["BucketOptionsIn"] = t.struct(
        {
            "exponentialBuckets": t.proxy(renames["ExponentialIn"]).optional(),
            "linearBuckets": t.proxy(renames["LinearIn"]).optional(),
            "explicitBuckets": t.proxy(renames["ExplicitIn"]).optional(),
        }
    ).named(renames["BucketOptionsIn"])
    types["BucketOptionsOut"] = t.struct(
        {
            "exponentialBuckets": t.proxy(renames["ExponentialOut"]).optional(),
            "linearBuckets": t.proxy(renames["LinearOut"]).optional(),
            "explicitBuckets": t.proxy(renames["ExplicitOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BucketOptionsOut"])
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
    types["CopyLogEntriesMetadataIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "state": t.string().optional(),
            "request": t.proxy(renames["CopyLogEntriesRequestIn"]).optional(),
            "endTime": t.string().optional(),
            "progress": t.integer().optional(),
            "writerIdentity": t.string().optional(),
            "cancellationRequested": t.boolean().optional(),
        }
    ).named(renames["CopyLogEntriesMetadataIn"])
    types["CopyLogEntriesMetadataOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "state": t.string().optional(),
            "request": t.proxy(renames["CopyLogEntriesRequestOut"]).optional(),
            "endTime": t.string().optional(),
            "progress": t.integer().optional(),
            "writerIdentity": t.string().optional(),
            "cancellationRequested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyLogEntriesMetadataOut"])
    types["LogLineIn"] = t.struct(
        {
            "logMessage": t.string().optional(),
            "time": t.string().optional(),
            "severity": t.string().optional(),
            "sourceLocation": t.proxy(renames["SourceLocationIn"]).optional(),
        }
    ).named(renames["LogLineIn"])
    types["LogLineOut"] = t.struct(
        {
            "logMessage": t.string().optional(),
            "time": t.string().optional(),
            "severity": t.string().optional(),
            "sourceLocation": t.proxy(renames["SourceLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogLineOut"])
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
        {"destination": t.string(), "filter": t.string().optional(), "name": t.string()}
    ).named(renames["CopyLogEntriesRequestIn"])
    types["CopyLogEntriesRequestOut"] = t.struct(
        {
            "destination": t.string(),
            "filter": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyLogEntriesRequestOut"])
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
    types["LogViewIn"] = t.struct(
        {
            "name": t.string().optional(),
            "description": t.string().optional(),
            "filter": t.string().optional(),
        }
    ).named(renames["LogViewIn"])
    types["LogViewOut"] = t.struct(
        {
            "name": t.string().optional(),
            "description": t.string().optional(),
            "filter": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogViewOut"])
    types["WriteLogEntriesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WriteLogEntriesResponseIn"]
    )
    types["WriteLogEntriesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WriteLogEntriesResponseOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["CmekSettingsIn"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "kmsKeyVersionName": t.string().optional(),
        }
    ).named(renames["CmekSettingsIn"])
    types["CmekSettingsOut"] = t.struct(
        {
            "name": t.string().optional(),
            "serviceAccountId": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "kmsKeyVersionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CmekSettingsOut"])
    types["DeleteLinkRequestIn"] = t.struct({"name": t.string()}).named(
        renames["DeleteLinkRequestIn"]
    )
    types["DeleteLinkRequestOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteLinkRequestOut"])
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
    types["MonitoredResourceDescriptorIn"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "type": t.string(),
        }
    ).named(renames["MonitoredResourceDescriptorIn"])
    types["MonitoredResourceDescriptorOut"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceDescriptorOut"])
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
    types["CreateLinkRequestIn"] = t.struct(
        {"linkId": t.string(), "link": t.proxy(renames["LinkIn"]), "parent": t.string()}
    ).named(renames["CreateLinkRequestIn"])
    types["CreateLinkRequestOut"] = t.struct(
        {
            "linkId": t.string(),
            "link": t.proxy(renames["LinkOut"]),
            "parent": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateLinkRequestOut"])
    types["ListLogEntriesResponseIn"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["LogEntryIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLogEntriesResponseIn"])
    types["ListLogEntriesResponseOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["LogEntryOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLogEntriesResponseOut"])
    types["LogBucketIn"] = t.struct(
        {
            "retentionDays": t.integer().optional(),
            "analyticsEnabled": t.boolean().optional(),
            "locked": t.boolean().optional(),
            "restrictedFields": t.array(t.string()).optional(),
            "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
            "description": t.string().optional(),
            "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
        }
    ).named(renames["LogBucketIn"])
    types["LogBucketOut"] = t.struct(
        {
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "retentionDays": t.integer().optional(),
            "analyticsEnabled": t.boolean().optional(),
            "lifecycleState": t.string().optional(),
            "locked": t.boolean().optional(),
            "restrictedFields": t.array(t.string()).optional(),
            "cmekSettings": t.proxy(renames["CmekSettingsOut"]).optional(),
            "description": t.string().optional(),
            "indexConfigs": t.array(t.proxy(renames["IndexConfigOut"])).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogBucketOut"])
    types["LogExclusionIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string(),
            "disabled": t.boolean().optional(),
            "filter": t.string(),
        }
    ).named(renames["LogExclusionIn"])
    types["LogExclusionOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string(),
            "disabled": t.boolean().optional(),
            "filter": t.string(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogExclusionOut"])
    types["ExplicitIn"] = t.struct({"bounds": t.array(t.number()).optional()}).named(
        renames["ExplicitIn"]
    )
    types["ExplicitOut"] = t.struct(
        {
            "bounds": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExplicitOut"])
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
    types["ListLogEntriesRequestIn"] = t.struct(
        {
            "projectIds": t.array(t.string()).optional(),
            "pageToken": t.string().optional(),
            "resourceNames": t.array(t.string()),
            "orderBy": t.string().optional(),
            "filter": t.string().optional(),
            "pageSize": t.integer().optional(),
        }
    ).named(renames["ListLogEntriesRequestIn"])
    types["ListLogEntriesRequestOut"] = t.struct(
        {
            "projectIds": t.array(t.string()).optional(),
            "pageToken": t.string().optional(),
            "resourceNames": t.array(t.string()),
            "orderBy": t.string().optional(),
            "filter": t.string().optional(),
            "pageSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLogEntriesRequestOut"])
    types["HttpRequestIn"] = t.struct(
        {
            "requestUrl": t.string().optional(),
            "remoteIp": t.string().optional(),
            "responseSize": t.string().optional(),
            "latency": t.string().optional(),
            "protocol": t.string().optional(),
            "referer": t.string().optional(),
            "cacheFillBytes": t.string().optional(),
            "requestMethod": t.string().optional(),
            "requestSize": t.string().optional(),
            "cacheValidatedWithOriginServer": t.boolean().optional(),
            "cacheHit": t.boolean().optional(),
            "status": t.integer().optional(),
            "serverIp": t.string().optional(),
            "cacheLookup": t.boolean().optional(),
            "userAgent": t.string().optional(),
        }
    ).named(renames["HttpRequestIn"])
    types["HttpRequestOut"] = t.struct(
        {
            "requestUrl": t.string().optional(),
            "remoteIp": t.string().optional(),
            "responseSize": t.string().optional(),
            "latency": t.string().optional(),
            "protocol": t.string().optional(),
            "referer": t.string().optional(),
            "cacheFillBytes": t.string().optional(),
            "requestMethod": t.string().optional(),
            "requestSize": t.string().optional(),
            "cacheValidatedWithOriginServer": t.boolean().optional(),
            "cacheHit": t.boolean().optional(),
            "status": t.integer().optional(),
            "serverIp": t.string().optional(),
            "cacheLookup": t.boolean().optional(),
            "userAgent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRequestOut"])
    types["WriteLogEntriesRequestIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "entries": t.array(t.proxy(renames["LogEntryIn"])),
            "dryRun": t.boolean().optional(),
            "resource": t.proxy(renames["MonitoredResourceIn"]).optional(),
            "partialSuccess": t.boolean().optional(),
            "logName": t.string().optional(),
        }
    ).named(renames["WriteLogEntriesRequestIn"])
    types["WriteLogEntriesRequestOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "entries": t.array(t.proxy(renames["LogEntryOut"])),
            "dryRun": t.boolean().optional(),
            "resource": t.proxy(renames["MonitoredResourceOut"]).optional(),
            "partialSuccess": t.boolean().optional(),
            "logName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteLogEntriesRequestOut"])
    types["LinearIn"] = t.struct(
        {
            "width": t.number().optional(),
            "offset": t.number().optional(),
            "numFiniteBuckets": t.integer().optional(),
        }
    ).named(renames["LinearIn"])
    types["LinearOut"] = t.struct(
        {
            "width": t.number().optional(),
            "offset": t.number().optional(),
            "numFiniteBuckets": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinearOut"])
    types["LinkIn"] = t.struct(
        {
            "bigqueryDataset": t.proxy(renames["BigQueryDatasetIn"]).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "bigqueryDataset": t.proxy(renames["BigQueryDatasetOut"]).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "lifecycleState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
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
    types["LogEntryOperationIn"] = t.struct(
        {
            "first": t.boolean().optional(),
            "producer": t.string().optional(),
            "id": t.string().optional(),
            "last": t.boolean().optional(),
        }
    ).named(renames["LogEntryOperationIn"])
    types["LogEntryOperationOut"] = t.struct(
        {
            "first": t.boolean().optional(),
            "producer": t.string().optional(),
            "id": t.string().optional(),
            "last": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogEntryOperationOut"])
    types["TailLogEntriesRequestIn"] = t.struct(
        {
            "bufferWindow": t.string().optional(),
            "filter": t.string().optional(),
            "resourceNames": t.array(t.string()),
        }
    ).named(renames["TailLogEntriesRequestIn"])
    types["TailLogEntriesRequestOut"] = t.struct(
        {
            "bufferWindow": t.string().optional(),
            "filter": t.string().optional(),
            "resourceNames": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TailLogEntriesRequestOut"])
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
    types["LogSinkIn"] = t.struct(
        {
            "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
            "description": t.string().optional(),
            "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
            "disabled": t.boolean().optional(),
            "destination": t.string(),
            "name": t.string(),
            "outputVersionFormat": t.string().optional(),
            "includeChildren": t.boolean().optional(),
            "filter": t.string().optional(),
        }
    ).named(renames["LogSinkIn"])
    types["LogSinkOut"] = t.struct(
        {
            "exclusions": t.array(t.proxy(renames["LogExclusionOut"])).optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "bigqueryOptions": t.proxy(renames["BigQueryOptionsOut"]).optional(),
            "disabled": t.boolean().optional(),
            "destination": t.string(),
            "name": t.string(),
            "outputVersionFormat": t.string().optional(),
            "includeChildren": t.boolean().optional(),
            "writerIdentity": t.string().optional(),
            "filter": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogSinkOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["BucketMetadataIn"] = t.struct(
        {
            "state": t.string().optional(),
            "updateBucketRequest": t.proxy(renames["UpdateBucketRequestIn"]).optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "createBucketRequest": t.proxy(renames["CreateBucketRequestIn"]).optional(),
        }
    ).named(renames["BucketMetadataIn"])
    types["BucketMetadataOut"] = t.struct(
        {
            "state": t.string().optional(),
            "updateBucketRequest": t.proxy(
                renames["UpdateBucketRequestOut"]
            ).optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "createBucketRequest": t.proxy(
                renames["CreateBucketRequestOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BucketMetadataOut"])
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
    types["RequestLogIn"] = t.struct(
        {
            "appId": t.string().optional(),
            "endTime": t.string().optional(),
            "host": t.string().optional(),
            "ip": t.string().optional(),
            "requestId": t.string().optional(),
            "resource": t.string().optional(),
            "responseSize": t.string().optional(),
            "instanceIndex": t.integer().optional(),
            "latency": t.string().optional(),
            "nickname": t.string().optional(),
            "pendingTime": t.string().optional(),
            "sourceReference": t.array(
                t.proxy(renames["SourceReferenceIn"])
            ).optional(),
            "moduleId": t.string().optional(),
            "traceId": t.string().optional(),
            "referrer": t.string().optional(),
            "traceSampled": t.boolean().optional(),
            "startTime": t.string().optional(),
            "megaCycles": t.string().optional(),
            "wasLoadingRequest": t.boolean().optional(),
            "appEngineRelease": t.string().optional(),
            "status": t.integer().optional(),
            "first": t.boolean().optional(),
            "instanceId": t.string().optional(),
            "spanId": t.string().optional(),
            "urlMapEntry": t.string().optional(),
            "finished": t.boolean().optional(),
            "userAgent": t.string().optional(),
            "cost": t.number().optional(),
            "httpVersion": t.string().optional(),
            "versionId": t.string().optional(),
            "line": t.array(t.proxy(renames["LogLineIn"])).optional(),
            "taskName": t.string().optional(),
            "taskQueueName": t.string().optional(),
            "method": t.string().optional(),
        }
    ).named(renames["RequestLogIn"])
    types["RequestLogOut"] = t.struct(
        {
            "appId": t.string().optional(),
            "endTime": t.string().optional(),
            "host": t.string().optional(),
            "ip": t.string().optional(),
            "requestId": t.string().optional(),
            "resource": t.string().optional(),
            "responseSize": t.string().optional(),
            "instanceIndex": t.integer().optional(),
            "latency": t.string().optional(),
            "nickname": t.string().optional(),
            "pendingTime": t.string().optional(),
            "sourceReference": t.array(
                t.proxy(renames["SourceReferenceOut"])
            ).optional(),
            "moduleId": t.string().optional(),
            "traceId": t.string().optional(),
            "referrer": t.string().optional(),
            "traceSampled": t.boolean().optional(),
            "startTime": t.string().optional(),
            "megaCycles": t.string().optional(),
            "wasLoadingRequest": t.boolean().optional(),
            "appEngineRelease": t.string().optional(),
            "status": t.integer().optional(),
            "first": t.boolean().optional(),
            "instanceId": t.string().optional(),
            "spanId": t.string().optional(),
            "urlMapEntry": t.string().optional(),
            "finished": t.boolean().optional(),
            "userAgent": t.string().optional(),
            "cost": t.number().optional(),
            "httpVersion": t.string().optional(),
            "versionId": t.string().optional(),
            "line": t.array(t.proxy(renames["LogLineOut"])).optional(),
            "taskName": t.string().optional(),
            "taskQueueName": t.string().optional(),
            "method": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestLogOut"])
    types["LogEntryIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "insertId": t.string().optional(),
            "httpRequest": t.proxy(renames["HttpRequestIn"]).optional(),
            "spanId": t.string().optional(),
            "trace": t.string().optional(),
            "operation": t.proxy(renames["LogEntryOperationIn"]).optional(),
            "resource": t.proxy(renames["MonitoredResourceIn"]),
            "severity": t.string().optional(),
            "jsonPayload": t.struct({"_": t.string().optional()}).optional(),
            "sourceLocation": t.proxy(renames["LogEntrySourceLocationIn"]).optional(),
            "split": t.proxy(renames["LogSplitIn"]).optional(),
            "textPayload": t.string().optional(),
            "logName": t.string(),
            "traceSampled": t.boolean().optional(),
            "timestamp": t.string().optional(),
            "protoPayload": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LogEntryIn"])
    types["LogEntryOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "insertId": t.string().optional(),
            "receiveTimestamp": t.string().optional(),
            "httpRequest": t.proxy(renames["HttpRequestOut"]).optional(),
            "spanId": t.string().optional(),
            "trace": t.string().optional(),
            "operation": t.proxy(renames["LogEntryOperationOut"]).optional(),
            "metadata": t.proxy(renames["MonitoredResourceMetadataOut"]).optional(),
            "resource": t.proxy(renames["MonitoredResourceOut"]),
            "severity": t.string().optional(),
            "jsonPayload": t.struct({"_": t.string().optional()}).optional(),
            "sourceLocation": t.proxy(renames["LogEntrySourceLocationOut"]).optional(),
            "split": t.proxy(renames["LogSplitOut"]).optional(),
            "textPayload": t.string().optional(),
            "logName": t.string(),
            "traceSampled": t.boolean().optional(),
            "timestamp": t.string().optional(),
            "protoPayload": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogEntryOut"])
    types["ListMonitoredResourceDescriptorsResponseIn"] = t.struct(
        {
            "resourceDescriptors": t.array(
                t.proxy(renames["MonitoredResourceDescriptorIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListMonitoredResourceDescriptorsResponseIn"])
    types["ListMonitoredResourceDescriptorsResponseOut"] = t.struct(
        {
            "resourceDescriptors": t.array(
                t.proxy(renames["MonitoredResourceDescriptorOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMonitoredResourceDescriptorsResponseOut"])
    types["UndeleteBucketRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UndeleteBucketRequestIn"]
    )
    types["UndeleteBucketRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteBucketRequestOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["BigQueryDatasetIn"] = t.struct({"_": t.string().optional()}).named(
        renames["BigQueryDatasetIn"]
    )
    types["BigQueryDatasetOut"] = t.struct(
        {
            "datasetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryDatasetOut"])
    types["CopyLogEntriesResponseIn"] = t.struct(
        {"logEntriesCopiedCount": t.string().optional()}
    ).named(renames["CopyLogEntriesResponseIn"])
    types["CopyLogEntriesResponseOut"] = t.struct(
        {
            "logEntriesCopiedCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyLogEntriesResponseOut"])
    types["LocationMetadataIn"] = t.struct(
        {"logAnalyticsEnabled": t.boolean().optional()}
    ).named(renames["LocationMetadataIn"])
    types["LocationMetadataOut"] = t.struct(
        {
            "logAnalyticsEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationMetadataOut"])
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
    types["SourceLocationIn"] = t.struct(
        {
            "line": t.string().optional(),
            "file": t.string().optional(),
            "functionName": t.string().optional(),
        }
    ).named(renames["SourceLocationIn"])
    types["SourceLocationOut"] = t.struct(
        {
            "line": t.string().optional(),
            "file": t.string().optional(),
            "functionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceLocationOut"])
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
    types["LinkMetadataIn"] = t.struct(
        {
            "state": t.string().optional(),
            "deleteLinkRequest": t.proxy(renames["DeleteLinkRequestIn"]).optional(),
            "createLinkRequest": t.proxy(renames["CreateLinkRequestIn"]).optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["LinkMetadataIn"])
    types["LinkMetadataOut"] = t.struct(
        {
            "state": t.string().optional(),
            "deleteLinkRequest": t.proxy(renames["DeleteLinkRequestOut"]).optional(),
            "createLinkRequest": t.proxy(renames["CreateLinkRequestOut"]).optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkMetadataOut"])
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
            "kmsServiceAccountId": t.string().optional(),
            "storageLocation": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettingsOut"])
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
    types["UpdateBucketRequestIn"] = t.struct(
        {
            "bucket": t.proxy(renames["LogBucketIn"]),
            "name": t.string(),
            "updateMask": t.string(),
        }
    ).named(renames["UpdateBucketRequestIn"])
    types["UpdateBucketRequestOut"] = t.struct(
        {
            "bucket": t.proxy(renames["LogBucketOut"]),
            "name": t.string(),
            "updateMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateBucketRequestOut"])

    functions = {}
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
    functions["billingAccountsLogsDelete"] = logging.get(
        "v2/{parent}/logs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "resourceNames": t.string().optional(),
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
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "resourceNames": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLogsResponseOut"]),
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
    functions["billingAccountsExclusionsPatch"] = logging.delete(
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
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
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsUpdateAsync"] = logging.post(
        "v2/{parent}/buckets:createAsync",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "locked": t.boolean().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "description": t.string().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsUndelete"] = logging.post(
        "v2/{parent}/buckets:createAsync",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "locked": t.boolean().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "description": t.string().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsGet"] = logging.post(
        "v2/{parent}/buckets:createAsync",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "locked": t.boolean().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "description": t.string().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsCreate"] = logging.post(
        "v2/{parent}/buckets:createAsync",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "locked": t.boolean().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "description": t.string().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsDelete"] = logging.post(
        "v2/{parent}/buckets:createAsync",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "locked": t.boolean().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "description": t.string().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsPatch"] = logging.post(
        "v2/{parent}/buckets:createAsync",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "locked": t.boolean().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "description": t.string().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsList"] = logging.post(
        "v2/{parent}/buckets:createAsync",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "locked": t.boolean().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "description": t.string().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsCreateAsync"] = logging.post(
        "v2/{parent}/buckets:createAsync",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "locked": t.boolean().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "description": t.string().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsViewsGet"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsViewsList"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsViewsCreate"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsViewsDelete"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsViewsPatch"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLogsResponseOut"]),
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
    functions["billingAccountsLocationsBucketsLinksCreate"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LinkOut"]),
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
    functions["billingAccountsLocationsBucketsLinksGet"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LinkOut"]),
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
    functions["billingAccountsSinksPatch"] = logging.delete(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["billingAccountsSinksDelete"] = logging.delete(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersGetCmekSettings"] = logging.patch(
        "v2/{name}/settings",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "disableDefaultSink": t.boolean().optional(),
                "storageLocation": t.string().optional(),
                "kmsKeyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersGetSettings"] = logging.patch(
        "v2/{name}/settings",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "disableDefaultSink": t.boolean().optional(),
                "storageLocation": t.string().optional(),
                "kmsKeyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersUpdateSettings"] = logging.patch(
        "v2/{name}/settings",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "disableDefaultSink": t.boolean().optional(),
                "storageLocation": t.string().optional(),
                "kmsKeyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSinksUpdate"] = logging.delete(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSinksGet"] = logging.delete(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSinksPatch"] = logging.delete(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSinksCreate"] = logging.delete(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSinksList"] = logging.delete(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSinksDelete"] = logging.delete(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersExclusionsDelete"] = logging.post(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "name": t.string(),
                "disabled": t.boolean().optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersExclusionsList"] = logging.post(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "name": t.string(),
                "disabled": t.boolean().optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersExclusionsPatch"] = logging.post(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "name": t.string(),
                "disabled": t.boolean().optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersExclusionsGet"] = logging.post(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "name": t.string(),
                "disabled": t.boolean().optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersExclusionsCreate"] = logging.post(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "name": t.string(),
                "disabled": t.boolean().optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLogsList"] = logging.delete(
        "v2/{logName}",
        t.struct({"logName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLogsDelete"] = logging.delete(
        "v2/{logName}",
        t.struct({"logName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsList"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsGet"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsOperationsCancel"] = logging.get(
        "v2/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsOperationsGet"] = logging.get(
        "v2/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsOperationsList"] = logging.get(
        "v2/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsCreateAsync"] = logging.post(
        "v2/{name}:updateAsync",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "locked": t.boolean().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "description": t.string().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsUndelete"] = logging.post(
        "v2/{name}:updateAsync",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "locked": t.boolean().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "description": t.string().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsPatch"] = logging.post(
        "v2/{name}:updateAsync",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "locked": t.boolean().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "description": t.string().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsGet"] = logging.post(
        "v2/{name}:updateAsync",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "locked": t.boolean().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "description": t.string().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsCreate"] = logging.post(
        "v2/{name}:updateAsync",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "locked": t.boolean().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "description": t.string().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsDelete"] = logging.post(
        "v2/{name}:updateAsync",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "locked": t.boolean().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "description": t.string().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsList"] = logging.post(
        "v2/{name}:updateAsync",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "locked": t.boolean().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "description": t.string().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsUpdateAsync"] = logging.post(
        "v2/{name}:updateAsync",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "locked": t.boolean().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "description": t.string().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsViewsCreate"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsViewsList"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsViewsPatch"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsViewsDelete"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsViewsGet"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsViewsLogsList"] = logging.get(
        "v2/{parent}/logs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "resourceNames": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLogsResponseOut"]),
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
    functions["monitoredResourceDescriptorsList"] = logging.get(
        "v2/monitoredResourceDescriptors",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMonitoredResourceDescriptorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetSettings"] = logging.get(
        "v2/{name}/cmekSettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CmekSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetCmekSettings"] = logging.get(
        "v2/{name}/cmekSettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CmekSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSinksDelete"] = logging.patch(
        "v2/{sinkName}",
        t.struct(
            {
                "uniqueWriterIdentity": t.boolean().optional(),
                "sinkName": t.string(),
                "updateMask": t.string().optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "description": t.string().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "disabled": t.boolean().optional(),
                "destination": t.string(),
                "name": t.string(),
                "outputVersionFormat": t.string().optional(),
                "includeChildren": t.boolean().optional(),
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
                "sinkName": t.string(),
                "updateMask": t.string().optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "description": t.string().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "disabled": t.boolean().optional(),
                "destination": t.string(),
                "name": t.string(),
                "outputVersionFormat": t.string().optional(),
                "includeChildren": t.boolean().optional(),
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
                "sinkName": t.string(),
                "updateMask": t.string().optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "description": t.string().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "disabled": t.boolean().optional(),
                "destination": t.string(),
                "name": t.string(),
                "outputVersionFormat": t.string().optional(),
                "includeChildren": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSinksUpdate"] = logging.patch(
        "v2/{sinkName}",
        t.struct(
            {
                "uniqueWriterIdentity": t.boolean().optional(),
                "sinkName": t.string(),
                "updateMask": t.string().optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "description": t.string().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "disabled": t.boolean().optional(),
                "destination": t.string(),
                "name": t.string(),
                "outputVersionFormat": t.string().optional(),
                "includeChildren": t.boolean().optional(),
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
                "sinkName": t.string(),
                "updateMask": t.string().optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "description": t.string().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "disabled": t.boolean().optional(),
                "destination": t.string(),
                "name": t.string(),
                "outputVersionFormat": t.string().optional(),
                "includeChildren": t.boolean().optional(),
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
                "sinkName": t.string(),
                "updateMask": t.string().optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "description": t.string().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "disabled": t.boolean().optional(),
                "destination": t.string(),
                "name": t.string(),
                "outputVersionFormat": t.string().optional(),
                "includeChildren": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsExclusionsCreate"] = logging.get(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExclusionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsExclusionsPatch"] = logging.get(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExclusionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsExclusionsDelete"] = logging.get(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExclusionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsExclusionsGet"] = logging.get(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExclusionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsExclusionsList"] = logging.get(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExclusionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = logging.get(
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
    functions["projectsLocationsList"] = logging.get(
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
    functions["projectsLocationsOperationsCancel"] = logging.get(
        "v2/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsCreateAsync"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsPatch"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsList"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsUndelete"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsCreate"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsUpdateAsync"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsDelete"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsGet"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsViewsGet"] = logging.post(
        "v2/{parent}/views",
        t.struct(
            {
                "viewId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsViewsDelete"] = logging.post(
        "v2/{parent}/views",
        t.struct(
            {
                "viewId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsViewsPatch"] = logging.post(
        "v2/{parent}/views",
        t.struct(
            {
                "viewId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsViewsList"] = logging.post(
        "v2/{parent}/views",
        t.struct(
            {
                "viewId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsViewsCreate"] = logging.post(
        "v2/{parent}/views",
        t.struct(
            {
                "viewId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "resourceNames": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLogsResponseOut"]),
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
    functions["projectsLocationsBucketsLinksCreate"] = logging.delete(
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
    functions["projectsMetricsList"] = logging.delete(
        "v2/{metricName}",
        t.struct({"metricName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMetricsGet"] = logging.delete(
        "v2/{metricName}",
        t.struct({"metricName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMetricsUpdate"] = logging.delete(
        "v2/{metricName}",
        t.struct({"metricName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMetricsCreate"] = logging.delete(
        "v2/{metricName}",
        t.struct({"metricName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMetricsDelete"] = logging.delete(
        "v2/{metricName}",
        t.struct({"metricName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["logsDelete"] = logging.get(
        "v2/{parent}/logs",
        t.struct(
            {
                "resourceNames": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "resourceNames": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["exclusionsCreate"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "disabled": t.boolean().optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["exclusionsDelete"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "disabled": t.boolean().optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["exclusionsList"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "disabled": t.boolean().optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["exclusionsGet"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "disabled": t.boolean().optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["exclusionsPatch"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "disabled": t.boolean().optional(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogExclusionOut"]),
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
    functions["organizationsUpdateSettings"] = logging.get(
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
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
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
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsDelete"] = logging.post(
        "v2/{name}:updateAsync",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "locked": t.boolean().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "description": t.string().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
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
                "name": t.string(),
                "updateMask": t.string(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "locked": t.boolean().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "description": t.string().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsPatch"] = logging.post(
        "v2/{name}:updateAsync",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "locked": t.boolean().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "description": t.string().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
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
                "name": t.string(),
                "updateMask": t.string(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "locked": t.boolean().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "description": t.string().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
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
                "name": t.string(),
                "updateMask": t.string(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "locked": t.boolean().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "description": t.string().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
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
                "name": t.string(),
                "updateMask": t.string(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "locked": t.boolean().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "description": t.string().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
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
                "name": t.string(),
                "updateMask": t.string(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "locked": t.boolean().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "description": t.string().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
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
                "name": t.string(),
                "updateMask": t.string(),
                "retentionDays": t.integer().optional(),
                "analyticsEnabled": t.boolean().optional(),
                "locked": t.boolean().optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "description": t.string().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
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
    functions["organizationsLocationsBucketsLinksGet"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsViewsPatch"] = logging.post(
        "v2/{parent}/views",
        t.struct(
            {
                "parent": t.string(),
                "viewId": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsViewsGet"] = logging.post(
        "v2/{parent}/views",
        t.struct(
            {
                "parent": t.string(),
                "viewId": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsViewsList"] = logging.post(
        "v2/{parent}/views",
        t.struct(
            {
                "parent": t.string(),
                "viewId": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsViewsDelete"] = logging.post(
        "v2/{parent}/views",
        t.struct(
            {
                "parent": t.string(),
                "viewId": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsViewsCreate"] = logging.post(
        "v2/{parent}/views",
        t.struct(
            {
                "parent": t.string(),
                "viewId": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsViewsLogsList"] = logging.get(
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
    functions["organizationsLocationsOperationsList"] = logging.post(
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
    functions["organizationsLocationsOperationsGet"] = logging.post(
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
    functions["organizationsLocationsOperationsCancel"] = logging.post(
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
    functions["organizationsSinksDelete"] = logging.post(
        "v2/{parent}/sinks",
        t.struct(
            {
                "parent": t.string(),
                "uniqueWriterIdentity": t.boolean().optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "description": t.string().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "disabled": t.boolean().optional(),
                "destination": t.string(),
                "name": t.string(),
                "outputVersionFormat": t.string().optional(),
                "includeChildren": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSinksPatch"] = logging.post(
        "v2/{parent}/sinks",
        t.struct(
            {
                "parent": t.string(),
                "uniqueWriterIdentity": t.boolean().optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "description": t.string().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "disabled": t.boolean().optional(),
                "destination": t.string(),
                "name": t.string(),
                "outputVersionFormat": t.string().optional(),
                "includeChildren": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSinksList"] = logging.post(
        "v2/{parent}/sinks",
        t.struct(
            {
                "parent": t.string(),
                "uniqueWriterIdentity": t.boolean().optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "description": t.string().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "disabled": t.boolean().optional(),
                "destination": t.string(),
                "name": t.string(),
                "outputVersionFormat": t.string().optional(),
                "includeChildren": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSinksGet"] = logging.post(
        "v2/{parent}/sinks",
        t.struct(
            {
                "parent": t.string(),
                "uniqueWriterIdentity": t.boolean().optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "description": t.string().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "disabled": t.boolean().optional(),
                "destination": t.string(),
                "name": t.string(),
                "outputVersionFormat": t.string().optional(),
                "includeChildren": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSinksUpdate"] = logging.post(
        "v2/{parent}/sinks",
        t.struct(
            {
                "parent": t.string(),
                "uniqueWriterIdentity": t.boolean().optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "description": t.string().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "disabled": t.boolean().optional(),
                "destination": t.string(),
                "name": t.string(),
                "outputVersionFormat": t.string().optional(),
                "includeChildren": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSinksCreate"] = logging.post(
        "v2/{parent}/sinks",
        t.struct(
            {
                "parent": t.string(),
                "uniqueWriterIdentity": t.boolean().optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "description": t.string().optional(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "disabled": t.boolean().optional(),
                "destination": t.string(),
                "name": t.string(),
                "outputVersionFormat": t.string().optional(),
                "includeChildren": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLogsDelete"] = logging.get(
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
    functions["organizationsLogsList"] = logging.get(
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
    functions["sinksUpdate"] = logging.get(
        "v2/{parent}/sinks",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSinksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sinksGet"] = logging.get(
        "v2/{parent}/sinks",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSinksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sinksCreate"] = logging.get(
        "v2/{parent}/sinks",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSinksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sinksDelete"] = logging.get(
        "v2/{parent}/sinks",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSinksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["sinksList"] = logging.get(
        "v2/{parent}/sinks",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSinksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v2UpdateCmekSettings"] = logging.patch(
        "v2/{name}/settings",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "disableDefaultSink": t.boolean().optional(),
                "storageLocation": t.string().optional(),
                "kmsKeyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v2GetSettings"] = logging.patch(
        "v2/{name}/settings",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "disableDefaultSink": t.boolean().optional(),
                "storageLocation": t.string().optional(),
                "kmsKeyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v2GetCmekSettings"] = logging.patch(
        "v2/{name}/settings",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "disableDefaultSink": t.boolean().optional(),
                "storageLocation": t.string().optional(),
                "kmsKeyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v2UpdateSettings"] = logging.patch(
        "v2/{name}/settings",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "disableDefaultSink": t.boolean().optional(),
                "storageLocation": t.string().optional(),
                "kmsKeyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["entriesTail"] = logging.post(
        "v2/entries:copy",
        t.struct(
            {
                "destination": t.string(),
                "filter": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["entriesWrite"] = logging.post(
        "v2/entries:copy",
        t.struct(
            {
                "destination": t.string(),
                "filter": t.string().optional(),
                "name": t.string(),
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
                "filter": t.string().optional(),
                "name": t.string(),
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
                "filter": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
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
    functions["locationsOperationsGet"] = logging.get(
        "v2/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsOperationsCancel"] = logging.get(
        "v2/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsOperationsList"] = logging.get(
        "v2/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsDelete"] = logging.get(
        "v2/{parent}/buckets",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBucketsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsCreateAsync"] = logging.get(
        "v2/{parent}/buckets",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBucketsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsUndelete"] = logging.get(
        "v2/{parent}/buckets",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBucketsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsPatch"] = logging.get(
        "v2/{parent}/buckets",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBucketsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsGet"] = logging.get(
        "v2/{parent}/buckets",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBucketsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsCreate"] = logging.get(
        "v2/{parent}/buckets",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBucketsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsUpdateAsync"] = logging.get(
        "v2/{parent}/buckets",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBucketsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsList"] = logging.get(
        "v2/{parent}/buckets",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBucketsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsViewsGet"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsViewsDelete"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsViewsCreate"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsViewsList"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsViewsPatch"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsLinksCreate"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsLinksGet"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsLinksList"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsLinksDelete"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="logging", renames=renames, types=types, functions=functions)
