from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_logging() -> Import:
    logging = HTTPRuntime("https://logging.googleapis.com/")

    renames = {
        "ErrorResponse": "_logging_1_ErrorResponse",
        "CopyLogEntriesRequestIn": "_logging_2_CopyLogEntriesRequestIn",
        "CopyLogEntriesRequestOut": "_logging_3_CopyLogEntriesRequestOut",
        "BucketOptionsIn": "_logging_4_BucketOptionsIn",
        "BucketOptionsOut": "_logging_5_BucketOptionsOut",
        "ListLogMetricsResponseIn": "_logging_6_ListLogMetricsResponseIn",
        "ListLogMetricsResponseOut": "_logging_7_ListLogMetricsResponseOut",
        "CreateLinkRequestIn": "_logging_8_CreateLinkRequestIn",
        "CreateLinkRequestOut": "_logging_9_CreateLinkRequestOut",
        "ExplicitIn": "_logging_10_ExplicitIn",
        "ExplicitOut": "_logging_11_ExplicitOut",
        "BigQueryDatasetIn": "_logging_12_BigQueryDatasetIn",
        "BigQueryDatasetOut": "_logging_13_BigQueryDatasetOut",
        "BucketMetadataIn": "_logging_14_BucketMetadataIn",
        "BucketMetadataOut": "_logging_15_BucketMetadataOut",
        "ListViewsResponseIn": "_logging_16_ListViewsResponseIn",
        "ListViewsResponseOut": "_logging_17_ListViewsResponseOut",
        "UndeleteBucketRequestIn": "_logging_18_UndeleteBucketRequestIn",
        "UndeleteBucketRequestOut": "_logging_19_UndeleteBucketRequestOut",
        "StatusIn": "_logging_20_StatusIn",
        "StatusOut": "_logging_21_StatusOut",
        "LocationIn": "_logging_22_LocationIn",
        "LocationOut": "_logging_23_LocationOut",
        "LinearIn": "_logging_24_LinearIn",
        "LinearOut": "_logging_25_LinearOut",
        "LogBucketIn": "_logging_26_LogBucketIn",
        "LogBucketOut": "_logging_27_LogBucketOut",
        "IndexConfigIn": "_logging_28_IndexConfigIn",
        "IndexConfigOut": "_logging_29_IndexConfigOut",
        "LogSinkIn": "_logging_30_LogSinkIn",
        "LogSinkOut": "_logging_31_LogSinkOut",
        "SourceReferenceIn": "_logging_32_SourceReferenceIn",
        "SourceReferenceOut": "_logging_33_SourceReferenceOut",
        "DeleteLinkRequestIn": "_logging_34_DeleteLinkRequestIn",
        "DeleteLinkRequestOut": "_logging_35_DeleteLinkRequestOut",
        "CancelOperationRequestIn": "_logging_36_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_logging_37_CancelOperationRequestOut",
        "CopyLogEntriesMetadataIn": "_logging_38_CopyLogEntriesMetadataIn",
        "CopyLogEntriesMetadataOut": "_logging_39_CopyLogEntriesMetadataOut",
        "SourceLocationIn": "_logging_40_SourceLocationIn",
        "SourceLocationOut": "_logging_41_SourceLocationOut",
        "ListLocationsResponseIn": "_logging_42_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_logging_43_ListLocationsResponseOut",
        "EmptyIn": "_logging_44_EmptyIn",
        "EmptyOut": "_logging_45_EmptyOut",
        "HttpRequestIn": "_logging_46_HttpRequestIn",
        "HttpRequestOut": "_logging_47_HttpRequestOut",
        "ExponentialIn": "_logging_48_ExponentialIn",
        "ExponentialOut": "_logging_49_ExponentialOut",
        "TailLogEntriesRequestIn": "_logging_50_TailLogEntriesRequestIn",
        "TailLogEntriesRequestOut": "_logging_51_TailLogEntriesRequestOut",
        "LogLineIn": "_logging_52_LogLineIn",
        "LogLineOut": "_logging_53_LogLineOut",
        "CmekSettingsIn": "_logging_54_CmekSettingsIn",
        "CmekSettingsOut": "_logging_55_CmekSettingsOut",
        "ListExclusionsResponseIn": "_logging_56_ListExclusionsResponseIn",
        "ListExclusionsResponseOut": "_logging_57_ListExclusionsResponseOut",
        "SuppressionInfoIn": "_logging_58_SuppressionInfoIn",
        "SuppressionInfoOut": "_logging_59_SuppressionInfoOut",
        "LogSplitIn": "_logging_60_LogSplitIn",
        "LogSplitOut": "_logging_61_LogSplitOut",
        "LogViewIn": "_logging_62_LogViewIn",
        "LogViewOut": "_logging_63_LogViewOut",
        "LogEntryIn": "_logging_64_LogEntryIn",
        "LogEntryOut": "_logging_65_LogEntryOut",
        "LocationMetadataIn": "_logging_66_LocationMetadataIn",
        "LocationMetadataOut": "_logging_67_LocationMetadataOut",
        "MetricDescriptorMetadataIn": "_logging_68_MetricDescriptorMetadataIn",
        "MetricDescriptorMetadataOut": "_logging_69_MetricDescriptorMetadataOut",
        "BigQueryOptionsIn": "_logging_70_BigQueryOptionsIn",
        "BigQueryOptionsOut": "_logging_71_BigQueryOptionsOut",
        "ListLogEntriesRequestIn": "_logging_72_ListLogEntriesRequestIn",
        "ListLogEntriesRequestOut": "_logging_73_ListLogEntriesRequestOut",
        "CreateBucketRequestIn": "_logging_74_CreateBucketRequestIn",
        "CreateBucketRequestOut": "_logging_75_CreateBucketRequestOut",
        "LogEntryOperationIn": "_logging_76_LogEntryOperationIn",
        "LogEntryOperationOut": "_logging_77_LogEntryOperationOut",
        "LogEntrySourceLocationIn": "_logging_78_LogEntrySourceLocationIn",
        "LogEntrySourceLocationOut": "_logging_79_LogEntrySourceLocationOut",
        "MonitoredResourceMetadataIn": "_logging_80_MonitoredResourceMetadataIn",
        "MonitoredResourceMetadataOut": "_logging_81_MonitoredResourceMetadataOut",
        "ListMonitoredResourceDescriptorsResponseIn": "_logging_82_ListMonitoredResourceDescriptorsResponseIn",
        "ListMonitoredResourceDescriptorsResponseOut": "_logging_83_ListMonitoredResourceDescriptorsResponseOut",
        "MetricDescriptorIn": "_logging_84_MetricDescriptorIn",
        "MetricDescriptorOut": "_logging_85_MetricDescriptorOut",
        "UpdateBucketRequestIn": "_logging_86_UpdateBucketRequestIn",
        "UpdateBucketRequestOut": "_logging_87_UpdateBucketRequestOut",
        "ListSinksResponseIn": "_logging_88_ListSinksResponseIn",
        "ListSinksResponseOut": "_logging_89_ListSinksResponseOut",
        "LabelDescriptorIn": "_logging_90_LabelDescriptorIn",
        "LabelDescriptorOut": "_logging_91_LabelDescriptorOut",
        "RequestLogIn": "_logging_92_RequestLogIn",
        "RequestLogOut": "_logging_93_RequestLogOut",
        "ListLogsResponseIn": "_logging_94_ListLogsResponseIn",
        "ListLogsResponseOut": "_logging_95_ListLogsResponseOut",
        "ListBucketsResponseIn": "_logging_96_ListBucketsResponseIn",
        "ListBucketsResponseOut": "_logging_97_ListBucketsResponseOut",
        "WriteLogEntriesRequestIn": "_logging_98_WriteLogEntriesRequestIn",
        "WriteLogEntriesRequestOut": "_logging_99_WriteLogEntriesRequestOut",
        "LinkMetadataIn": "_logging_100_LinkMetadataIn",
        "LinkMetadataOut": "_logging_101_LinkMetadataOut",
        "ListOperationsResponseIn": "_logging_102_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_logging_103_ListOperationsResponseOut",
        "LogExclusionIn": "_logging_104_LogExclusionIn",
        "LogExclusionOut": "_logging_105_LogExclusionOut",
        "CopyLogEntriesResponseIn": "_logging_106_CopyLogEntriesResponseIn",
        "CopyLogEntriesResponseOut": "_logging_107_CopyLogEntriesResponseOut",
        "ListLinksResponseIn": "_logging_108_ListLinksResponseIn",
        "ListLinksResponseOut": "_logging_109_ListLinksResponseOut",
        "MonitoredResourceDescriptorIn": "_logging_110_MonitoredResourceDescriptorIn",
        "MonitoredResourceDescriptorOut": "_logging_111_MonitoredResourceDescriptorOut",
        "TailLogEntriesResponseIn": "_logging_112_TailLogEntriesResponseIn",
        "TailLogEntriesResponseOut": "_logging_113_TailLogEntriesResponseOut",
        "SettingsIn": "_logging_114_SettingsIn",
        "SettingsOut": "_logging_115_SettingsOut",
        "OperationIn": "_logging_116_OperationIn",
        "OperationOut": "_logging_117_OperationOut",
        "LogMetricIn": "_logging_118_LogMetricIn",
        "LogMetricOut": "_logging_119_LogMetricOut",
        "MonitoredResourceIn": "_logging_120_MonitoredResourceIn",
        "MonitoredResourceOut": "_logging_121_MonitoredResourceOut",
        "LinkIn": "_logging_122_LinkIn",
        "LinkOut": "_logging_123_LinkOut",
        "ListLogEntriesResponseIn": "_logging_124_ListLogEntriesResponseIn",
        "ListLogEntriesResponseOut": "_logging_125_ListLogEntriesResponseOut",
        "WriteLogEntriesResponseIn": "_logging_126_WriteLogEntriesResponseIn",
        "WriteLogEntriesResponseOut": "_logging_127_WriteLogEntriesResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["BucketOptionsIn"] = t.struct(
        {
            "explicitBuckets": t.proxy(renames["ExplicitIn"]).optional(),
            "linearBuckets": t.proxy(renames["LinearIn"]).optional(),
            "exponentialBuckets": t.proxy(renames["ExponentialIn"]).optional(),
        }
    ).named(renames["BucketOptionsIn"])
    types["BucketOptionsOut"] = t.struct(
        {
            "explicitBuckets": t.proxy(renames["ExplicitOut"]).optional(),
            "linearBuckets": t.proxy(renames["LinearOut"]).optional(),
            "exponentialBuckets": t.proxy(renames["ExponentialOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BucketOptionsOut"])
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
    types["CreateLinkRequestIn"] = t.struct(
        {"link": t.proxy(renames["LinkIn"]), "parent": t.string(), "linkId": t.string()}
    ).named(renames["CreateLinkRequestIn"])
    types["CreateLinkRequestOut"] = t.struct(
        {
            "link": t.proxy(renames["LinkOut"]),
            "parent": t.string(),
            "linkId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateLinkRequestOut"])
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
    types["BucketMetadataIn"] = t.struct(
        {
            "createBucketRequest": t.proxy(renames["CreateBucketRequestIn"]).optional(),
            "startTime": t.string().optional(),
            "updateBucketRequest": t.proxy(renames["UpdateBucketRequestIn"]).optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["BucketMetadataIn"])
    types["BucketMetadataOut"] = t.struct(
        {
            "createBucketRequest": t.proxy(
                renames["CreateBucketRequestOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "updateBucketRequest": t.proxy(
                renames["UpdateBucketRequestOut"]
            ).optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BucketMetadataOut"])
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
    types["UndeleteBucketRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UndeleteBucketRequestIn"]
    )
    types["UndeleteBucketRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteBucketRequestOut"])
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
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["LogBucketIn"] = t.struct(
        {
            "analyticsEnabled": t.boolean().optional(),
            "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
            "restrictedFields": t.array(t.string()).optional(),
            "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
            "retentionDays": t.integer().optional(),
            "locked": t.boolean().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["LogBucketIn"])
    types["LogBucketOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "lifecycleState": t.string().optional(),
            "analyticsEnabled": t.boolean().optional(),
            "indexConfigs": t.array(t.proxy(renames["IndexConfigOut"])).optional(),
            "restrictedFields": t.array(t.string()).optional(),
            "cmekSettings": t.proxy(renames["CmekSettingsOut"]).optional(),
            "retentionDays": t.integer().optional(),
            "locked": t.boolean().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogBucketOut"])
    types["IndexConfigIn"] = t.struct(
        {"fieldPath": t.string(), "type": t.string()}
    ).named(renames["IndexConfigIn"])
    types["IndexConfigOut"] = t.struct(
        {
            "fieldPath": t.string(),
            "createTime": t.string().optional(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexConfigOut"])
    types["LogSinkIn"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "description": t.string().optional(),
            "filter": t.string().optional(),
            "name": t.string(),
            "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
            "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
            "outputVersionFormat": t.string().optional(),
            "includeChildren": t.boolean().optional(),
            "destination": t.string(),
        }
    ).named(renames["LogSinkIn"])
    types["LogSinkOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "description": t.string().optional(),
            "writerIdentity": t.string().optional(),
            "filter": t.string().optional(),
            "name": t.string(),
            "bigqueryOptions": t.proxy(renames["BigQueryOptionsOut"]).optional(),
            "updateTime": t.string().optional(),
            "exclusions": t.array(t.proxy(renames["LogExclusionOut"])).optional(),
            "outputVersionFormat": t.string().optional(),
            "includeChildren": t.boolean().optional(),
            "destination": t.string(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogSinkOut"])
    types["SourceReferenceIn"] = t.struct(
        {"revisionId": t.string().optional(), "repository": t.string().optional()}
    ).named(renames["SourceReferenceIn"])
    types["SourceReferenceOut"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "repository": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceReferenceOut"])
    types["DeleteLinkRequestIn"] = t.struct({"name": t.string()}).named(
        renames["DeleteLinkRequestIn"]
    )
    types["DeleteLinkRequestOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteLinkRequestOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["CopyLogEntriesMetadataIn"] = t.struct(
        {
            "writerIdentity": t.string().optional(),
            "cancellationRequested": t.boolean().optional(),
            "startTime": t.string().optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "request": t.proxy(renames["CopyLogEntriesRequestIn"]).optional(),
            "progress": t.integer().optional(),
        }
    ).named(renames["CopyLogEntriesMetadataIn"])
    types["CopyLogEntriesMetadataOut"] = t.struct(
        {
            "writerIdentity": t.string().optional(),
            "cancellationRequested": t.boolean().optional(),
            "startTime": t.string().optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "request": t.proxy(renames["CopyLogEntriesRequestOut"]).optional(),
            "progress": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyLogEntriesMetadataOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["HttpRequestIn"] = t.struct(
        {
            "latency": t.string().optional(),
            "referer": t.string().optional(),
            "status": t.integer().optional(),
            "cacheLookup": t.boolean().optional(),
            "requestUrl": t.string().optional(),
            "responseSize": t.string().optional(),
            "remoteIp": t.string().optional(),
            "requestMethod": t.string().optional(),
            "requestSize": t.string().optional(),
            "protocol": t.string().optional(),
            "userAgent": t.string().optional(),
            "cacheHit": t.boolean().optional(),
            "cacheFillBytes": t.string().optional(),
            "serverIp": t.string().optional(),
            "cacheValidatedWithOriginServer": t.boolean().optional(),
        }
    ).named(renames["HttpRequestIn"])
    types["HttpRequestOut"] = t.struct(
        {
            "latency": t.string().optional(),
            "referer": t.string().optional(),
            "status": t.integer().optional(),
            "cacheLookup": t.boolean().optional(),
            "requestUrl": t.string().optional(),
            "responseSize": t.string().optional(),
            "remoteIp": t.string().optional(),
            "requestMethod": t.string().optional(),
            "requestSize": t.string().optional(),
            "protocol": t.string().optional(),
            "userAgent": t.string().optional(),
            "cacheHit": t.boolean().optional(),
            "cacheFillBytes": t.string().optional(),
            "serverIp": t.string().optional(),
            "cacheValidatedWithOriginServer": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRequestOut"])
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
    types["TailLogEntriesRequestIn"] = t.struct(
        {
            "bufferWindow": t.string().optional(),
            "resourceNames": t.array(t.string()),
            "filter": t.string().optional(),
        }
    ).named(renames["TailLogEntriesRequestIn"])
    types["TailLogEntriesRequestOut"] = t.struct(
        {
            "bufferWindow": t.string().optional(),
            "resourceNames": t.array(t.string()),
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TailLogEntriesRequestOut"])
    types["LogLineIn"] = t.struct(
        {
            "sourceLocation": t.proxy(renames["SourceLocationIn"]).optional(),
            "logMessage": t.string().optional(),
            "severity": t.string().optional(),
            "time": t.string().optional(),
        }
    ).named(renames["LogLineIn"])
    types["LogLineOut"] = t.struct(
        {
            "sourceLocation": t.proxy(renames["SourceLocationOut"]).optional(),
            "logMessage": t.string().optional(),
            "severity": t.string().optional(),
            "time": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogLineOut"])
    types["CmekSettingsIn"] = t.struct(
        {
            "kmsKeyVersionName": t.string().optional(),
            "kmsKeyName": t.string().optional(),
        }
    ).named(renames["CmekSettingsIn"])
    types["CmekSettingsOut"] = t.struct(
        {
            "serviceAccountId": t.string().optional(),
            "name": t.string().optional(),
            "kmsKeyVersionName": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CmekSettingsOut"])
    types["ListExclusionsResponseIn"] = t.struct(
        {
            "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListExclusionsResponseIn"])
    types["ListExclusionsResponseOut"] = t.struct(
        {
            "exclusions": t.array(t.proxy(renames["LogExclusionOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListExclusionsResponseOut"])
    types["SuppressionInfoIn"] = t.struct(
        {"reason": t.string().optional(), "suppressedCount": t.integer().optional()}
    ).named(renames["SuppressionInfoIn"])
    types["SuppressionInfoOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "suppressedCount": t.integer().optional(),
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
    types["LogViewIn"] = t.struct(
        {
            "filter": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LogViewIn"])
    types["LogViewOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "filter": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogViewOut"])
    types["LogEntryIn"] = t.struct(
        {
            "spanId": t.string().optional(),
            "sourceLocation": t.proxy(renames["LogEntrySourceLocationIn"]).optional(),
            "jsonPayload": t.struct({"_": t.string().optional()}).optional(),
            "insertId": t.string().optional(),
            "trace": t.string().optional(),
            "severity": t.string().optional(),
            "textPayload": t.string().optional(),
            "protoPayload": t.struct({"_": t.string().optional()}).optional(),
            "traceSampled": t.boolean().optional(),
            "httpRequest": t.proxy(renames["HttpRequestIn"]).optional(),
            "operation": t.proxy(renames["LogEntryOperationIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "split": t.proxy(renames["LogSplitIn"]).optional(),
            "timestamp": t.string().optional(),
            "logName": t.string(),
            "resource": t.proxy(renames["MonitoredResourceIn"]),
        }
    ).named(renames["LogEntryIn"])
    types["LogEntryOut"] = t.struct(
        {
            "receiveTimestamp": t.string().optional(),
            "spanId": t.string().optional(),
            "sourceLocation": t.proxy(renames["LogEntrySourceLocationOut"]).optional(),
            "metadata": t.proxy(renames["MonitoredResourceMetadataOut"]).optional(),
            "jsonPayload": t.struct({"_": t.string().optional()}).optional(),
            "insertId": t.string().optional(),
            "trace": t.string().optional(),
            "severity": t.string().optional(),
            "textPayload": t.string().optional(),
            "protoPayload": t.struct({"_": t.string().optional()}).optional(),
            "traceSampled": t.boolean().optional(),
            "httpRequest": t.proxy(renames["HttpRequestOut"]).optional(),
            "operation": t.proxy(renames["LogEntryOperationOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "split": t.proxy(renames["LogSplitOut"]).optional(),
            "timestamp": t.string().optional(),
            "logName": t.string(),
            "resource": t.proxy(renames["MonitoredResourceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogEntryOut"])
    types["LocationMetadataIn"] = t.struct(
        {"logAnalyticsEnabled": t.boolean().optional()}
    ).named(renames["LocationMetadataIn"])
    types["LocationMetadataOut"] = t.struct(
        {
            "logAnalyticsEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationMetadataOut"])
    types["MetricDescriptorMetadataIn"] = t.struct(
        {
            "ingestDelay": t.string().optional(),
            "samplePeriod": t.string().optional(),
            "launchStage": t.string().optional(),
        }
    ).named(renames["MetricDescriptorMetadataIn"])
    types["MetricDescriptorMetadataOut"] = t.struct(
        {
            "ingestDelay": t.string().optional(),
            "samplePeriod": t.string().optional(),
            "launchStage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorMetadataOut"])
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
    types["ListLogEntriesRequestIn"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "orderBy": t.string().optional(),
            "pageToken": t.string().optional(),
            "projectIds": t.array(t.string()).optional(),
            "resourceNames": t.array(t.string()),
            "filter": t.string().optional(),
        }
    ).named(renames["ListLogEntriesRequestIn"])
    types["ListLogEntriesRequestOut"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "orderBy": t.string().optional(),
            "pageToken": t.string().optional(),
            "projectIds": t.array(t.string()).optional(),
            "resourceNames": t.array(t.string()),
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLogEntriesRequestOut"])
    types["CreateBucketRequestIn"] = t.struct(
        {
            "parent": t.string(),
            "bucket": t.proxy(renames["LogBucketIn"]),
            "bucketId": t.string(),
        }
    ).named(renames["CreateBucketRequestIn"])
    types["CreateBucketRequestOut"] = t.struct(
        {
            "parent": t.string(),
            "bucket": t.proxy(renames["LogBucketOut"]),
            "bucketId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateBucketRequestOut"])
    types["LogEntryOperationIn"] = t.struct(
        {
            "first": t.boolean().optional(),
            "id": t.string().optional(),
            "last": t.boolean().optional(),
            "producer": t.string().optional(),
        }
    ).named(renames["LogEntryOperationIn"])
    types["LogEntryOperationOut"] = t.struct(
        {
            "first": t.boolean().optional(),
            "id": t.string().optional(),
            "last": t.boolean().optional(),
            "producer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogEntryOperationOut"])
    types["LogEntrySourceLocationIn"] = t.struct(
        {
            "function": t.string().optional(),
            "line": t.string().optional(),
            "file": t.string().optional(),
        }
    ).named(renames["LogEntrySourceLocationIn"])
    types["LogEntrySourceLocationOut"] = t.struct(
        {
            "function": t.string().optional(),
            "line": t.string().optional(),
            "file": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogEntrySourceLocationOut"])
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
    types["MetricDescriptorIn"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "metricKind": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
            "unit": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "valueType": t.string().optional(),
        }
    ).named(renames["MetricDescriptorIn"])
    types["MetricDescriptorOut"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "metricKind": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataOut"]).optional(),
            "unit": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "valueType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorOut"])
    types["UpdateBucketRequestIn"] = t.struct(
        {
            "bucket": t.proxy(renames["LogBucketIn"]),
            "updateMask": t.string(),
            "name": t.string(),
        }
    ).named(renames["UpdateBucketRequestIn"])
    types["UpdateBucketRequestOut"] = t.struct(
        {
            "bucket": t.proxy(renames["LogBucketOut"]),
            "updateMask": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateBucketRequestOut"])
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
    types["LabelDescriptorIn"] = t.struct(
        {
            "key": t.string().optional(),
            "valueType": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["LabelDescriptorIn"])
    types["LabelDescriptorOut"] = t.struct(
        {
            "key": t.string().optional(),
            "valueType": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelDescriptorOut"])
    types["RequestLogIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "traceId": t.string().optional(),
            "startTime": t.string().optional(),
            "wasLoadingRequest": t.boolean().optional(),
            "host": t.string().optional(),
            "status": t.integer().optional(),
            "megaCycles": t.string().optional(),
            "pendingTime": t.string().optional(),
            "traceSampled": t.boolean().optional(),
            "appEngineRelease": t.string().optional(),
            "ip": t.string().optional(),
            "resource": t.string().optional(),
            "appId": t.string().optional(),
            "first": t.boolean().optional(),
            "nickname": t.string().optional(),
            "moduleId": t.string().optional(),
            "requestId": t.string().optional(),
            "versionId": t.string().optional(),
            "latency": t.string().optional(),
            "httpVersion": t.string().optional(),
            "responseSize": t.string().optional(),
            "userAgent": t.string().optional(),
            "taskQueueName": t.string().optional(),
            "instanceId": t.string().optional(),
            "sourceReference": t.array(
                t.proxy(renames["SourceReferenceIn"])
            ).optional(),
            "spanId": t.string().optional(),
            "line": t.array(t.proxy(renames["LogLineIn"])).optional(),
            "cost": t.number().optional(),
            "referrer": t.string().optional(),
            "method": t.string().optional(),
            "urlMapEntry": t.string().optional(),
            "finished": t.boolean().optional(),
            "instanceIndex": t.integer().optional(),
            "taskName": t.string().optional(),
        }
    ).named(renames["RequestLogIn"])
    types["RequestLogOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "traceId": t.string().optional(),
            "startTime": t.string().optional(),
            "wasLoadingRequest": t.boolean().optional(),
            "host": t.string().optional(),
            "status": t.integer().optional(),
            "megaCycles": t.string().optional(),
            "pendingTime": t.string().optional(),
            "traceSampled": t.boolean().optional(),
            "appEngineRelease": t.string().optional(),
            "ip": t.string().optional(),
            "resource": t.string().optional(),
            "appId": t.string().optional(),
            "first": t.boolean().optional(),
            "nickname": t.string().optional(),
            "moduleId": t.string().optional(),
            "requestId": t.string().optional(),
            "versionId": t.string().optional(),
            "latency": t.string().optional(),
            "httpVersion": t.string().optional(),
            "responseSize": t.string().optional(),
            "userAgent": t.string().optional(),
            "taskQueueName": t.string().optional(),
            "instanceId": t.string().optional(),
            "sourceReference": t.array(
                t.proxy(renames["SourceReferenceOut"])
            ).optional(),
            "spanId": t.string().optional(),
            "line": t.array(t.proxy(renames["LogLineOut"])).optional(),
            "cost": t.number().optional(),
            "referrer": t.string().optional(),
            "method": t.string().optional(),
            "urlMapEntry": t.string().optional(),
            "finished": t.boolean().optional(),
            "instanceIndex": t.integer().optional(),
            "taskName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestLogOut"])
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
            "resource": t.proxy(renames["MonitoredResourceIn"]).optional(),
            "entries": t.array(t.proxy(renames["LogEntryIn"])),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "logName": t.string().optional(),
            "partialSuccess": t.boolean().optional(),
        }
    ).named(renames["WriteLogEntriesRequestIn"])
    types["WriteLogEntriesRequestOut"] = t.struct(
        {
            "dryRun": t.boolean().optional(),
            "resource": t.proxy(renames["MonitoredResourceOut"]).optional(),
            "entries": t.array(t.proxy(renames["LogEntryOut"])),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "logName": t.string().optional(),
            "partialSuccess": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteLogEntriesRequestOut"])
    types["LinkMetadataIn"] = t.struct(
        {
            "createLinkRequest": t.proxy(renames["CreateLinkRequestIn"]).optional(),
            "deleteLinkRequest": t.proxy(renames["DeleteLinkRequestIn"]).optional(),
            "state": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["LinkMetadataIn"])
    types["LinkMetadataOut"] = t.struct(
        {
            "createLinkRequest": t.proxy(renames["CreateLinkRequestOut"]).optional(),
            "deleteLinkRequest": t.proxy(renames["DeleteLinkRequestOut"]).optional(),
            "state": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkMetadataOut"])
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
    types["LogExclusionIn"] = t.struct(
        {
            "description": t.string().optional(),
            "disabled": t.boolean().optional(),
            "filter": t.string(),
            "name": t.string(),
        }
    ).named(renames["LogExclusionIn"])
    types["LogExclusionOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "disabled": t.boolean().optional(),
            "createTime": t.string().optional(),
            "filter": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogExclusionOut"])
    types["CopyLogEntriesResponseIn"] = t.struct(
        {"logEntriesCopiedCount": t.string().optional()}
    ).named(renames["CopyLogEntriesResponseIn"])
    types["CopyLogEntriesResponseOut"] = t.struct(
        {
            "logEntriesCopiedCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyLogEntriesResponseOut"])
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
    types["MonitoredResourceDescriptorIn"] = t.struct(
        {
            "name": t.string().optional(),
            "description": t.string().optional(),
            "type": t.string(),
            "displayName": t.string().optional(),
            "launchStage": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])),
        }
    ).named(renames["MonitoredResourceDescriptorIn"])
    types["MonitoredResourceDescriptorOut"] = t.struct(
        {
            "name": t.string().optional(),
            "description": t.string().optional(),
            "type": t.string(),
            "displayName": t.string().optional(),
            "launchStage": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceDescriptorOut"])
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
    types["SettingsIn"] = t.struct(
        {
            "storageLocation": t.string().optional(),
            "disableDefaultSink": t.boolean().optional(),
            "kmsKeyName": t.string().optional(),
        }
    ).named(renames["SettingsIn"])
    types["SettingsOut"] = t.struct(
        {
            "kmsServiceAccountId": t.string().optional(),
            "storageLocation": t.string().optional(),
            "name": t.string().optional(),
            "disableDefaultSink": t.boolean().optional(),
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettingsOut"])
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
    types["LogMetricIn"] = t.struct(
        {
            "valueExtractor": t.string().optional(),
            "bucketName": t.string().optional(),
            "filter": t.string(),
            "version": t.string().optional(),
            "name": t.string(),
            "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "disabled": t.boolean().optional(),
            "metricDescriptor": t.proxy(renames["MetricDescriptorIn"]).optional(),
            "bucketOptions": t.proxy(renames["BucketOptionsIn"]).optional(),
        }
    ).named(renames["LogMetricIn"])
    types["LogMetricOut"] = t.struct(
        {
            "valueExtractor": t.string().optional(),
            "bucketName": t.string().optional(),
            "filter": t.string(),
            "version": t.string().optional(),
            "name": t.string(),
            "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "disabled": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "metricDescriptor": t.proxy(renames["MetricDescriptorOut"]).optional(),
            "bucketOptions": t.proxy(renames["BucketOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogMetricOut"])
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
    types["LinkIn"] = t.struct(
        {
            "bigqueryDataset": t.proxy(renames["BigQueryDatasetIn"]).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "lifecycleState": t.string().optional(),
            "bigqueryDataset": t.proxy(renames["BigQueryDatasetOut"]).optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
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
    types["WriteLogEntriesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WriteLogEntriesResponseIn"]
    )
    types["WriteLogEntriesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WriteLogEntriesResponseOut"])

    functions = {}
    functions["v2GetCmekSettings"] = logging.get(
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
    functions["v2UpdateSettings"] = logging.get(
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
    functions["exclusionsList"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["exclusionsCreate"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["exclusionsPatch"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["exclusionsDelete"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["exclusionsGet"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogExclusionOut"]),
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
    functions["billingAccountsSinksGet"] = logging.patch(
        "v2/{sinkName}",
        t.struct(
            {
                "uniqueWriterIdentity": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "sinkName": t.string(),
                "disabled": t.boolean().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "outputVersionFormat": t.string().optional(),
                "includeChildren": t.boolean().optional(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsSinksUpdate"] = logging.patch(
        "v2/{sinkName}",
        t.struct(
            {
                "uniqueWriterIdentity": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "sinkName": t.string(),
                "disabled": t.boolean().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "outputVersionFormat": t.string().optional(),
                "includeChildren": t.boolean().optional(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsSinksDelete"] = logging.patch(
        "v2/{sinkName}",
        t.struct(
            {
                "uniqueWriterIdentity": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "sinkName": t.string(),
                "disabled": t.boolean().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "outputVersionFormat": t.string().optional(),
                "includeChildren": t.boolean().optional(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsSinksCreate"] = logging.patch(
        "v2/{sinkName}",
        t.struct(
            {
                "uniqueWriterIdentity": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "sinkName": t.string(),
                "disabled": t.boolean().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "outputVersionFormat": t.string().optional(),
                "includeChildren": t.boolean().optional(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsSinksList"] = logging.patch(
        "v2/{sinkName}",
        t.struct(
            {
                "uniqueWriterIdentity": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "sinkName": t.string(),
                "disabled": t.boolean().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "outputVersionFormat": t.string().optional(),
                "includeChildren": t.boolean().optional(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsSinksPatch"] = logging.patch(
        "v2/{sinkName}",
        t.struct(
            {
                "uniqueWriterIdentity": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "sinkName": t.string(),
                "disabled": t.boolean().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "outputVersionFormat": t.string().optional(),
                "includeChildren": t.boolean().optional(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
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
                "filter": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsCreateAsync"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "analyticsEnabled": t.boolean().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "retentionDays": t.integer().optional(),
                "locked": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsDelete"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "analyticsEnabled": t.boolean().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "retentionDays": t.integer().optional(),
                "locked": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsGet"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "analyticsEnabled": t.boolean().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "retentionDays": t.integer().optional(),
                "locked": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsList"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "analyticsEnabled": t.boolean().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "retentionDays": t.integer().optional(),
                "locked": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsUndelete"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "analyticsEnabled": t.boolean().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "retentionDays": t.integer().optional(),
                "locked": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsCreate"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "analyticsEnabled": t.boolean().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "retentionDays": t.integer().optional(),
                "locked": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsUpdateAsync"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "analyticsEnabled": t.boolean().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "retentionDays": t.integer().optional(),
                "locked": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsPatch"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "analyticsEnabled": t.boolean().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "retentionDays": t.integer().optional(),
                "locked": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsLinksGet"] = logging.post(
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
    functions["billingAccountsLocationsBucketsLinksList"] = logging.post(
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
    functions["billingAccountsLocationsBucketsLinksDelete"] = logging.post(
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
    functions["billingAccountsLocationsBucketsLinksCreate"] = logging.post(
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
    functions["billingAccountsLocationsBucketsViewsPatch"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsViewsCreate"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsViewsDelete"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsViewsList"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsViewsGet"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsBucketsViewsLogsList"] = logging.get(
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
    functions["billingAccountsExclusionsList"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["entriesCopy"] = logging.post(
        "v2/entries:write",
        t.struct(
            {
                "dryRun": t.boolean().optional(),
                "resource": t.proxy(renames["MonitoredResourceIn"]).optional(),
                "entries": t.array(t.proxy(renames["LogEntryIn"])),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "logName": t.string().optional(),
                "partialSuccess": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WriteLogEntriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["entriesList"] = logging.post(
        "v2/entries:write",
        t.struct(
            {
                "dryRun": t.boolean().optional(),
                "resource": t.proxy(renames["MonitoredResourceIn"]).optional(),
                "entries": t.array(t.proxy(renames["LogEntryIn"])),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "logName": t.string().optional(),
                "partialSuccess": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WriteLogEntriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["entriesTail"] = logging.post(
        "v2/entries:write",
        t.struct(
            {
                "dryRun": t.boolean().optional(),
                "resource": t.proxy(renames["MonitoredResourceIn"]).optional(),
                "entries": t.array(t.proxy(renames["LogEntryIn"])),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "logName": t.string().optional(),
                "partialSuccess": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WriteLogEntriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["entriesWrite"] = logging.post(
        "v2/entries:write",
        t.struct(
            {
                "dryRun": t.boolean().optional(),
                "resource": t.proxy(renames["MonitoredResourceIn"]).optional(),
                "entries": t.array(t.proxy(renames["LogEntryIn"])),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "logName": t.string().optional(),
                "partialSuccess": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WriteLogEntriesResponseOut"]),
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
    functions["sinksUpdate"] = logging.delete(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["sinksList"] = logging.delete(
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
    functions["sinksDelete"] = logging.delete(
        "v2/{sinkName}",
        t.struct({"sinkName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["projectsLocationsGet"] = logging.get(
        "v2/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = logging.post(
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
    functions["projectsLocationsOperationsList"] = logging.post(
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
    functions["projectsLocationsOperationsCancel"] = logging.post(
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
    functions["projectsLocationsBucketsPatch"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsCreate"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsCreateAsync"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsUpdateAsync"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsGet"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsUndelete"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsList"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsDelete"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsLinksList"] = logging.post(
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
    functions["projectsLocationsBucketsLinksDelete"] = logging.post(
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
    functions["projectsLocationsBucketsLinksGet"] = logging.post(
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
    functions["projectsLocationsBucketsLinksCreate"] = logging.post(
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
    functions["projectsLocationsBucketsViewsCreate"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsViewsList"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsViewsPatch"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsViewsGet"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsViewsDelete"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBucketsViewsLogsList"] = logging.get(
        "v2/{parent}/logs",
        t.struct(
            {
                "resourceNames": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsExclusionsDelete"] = logging.patch(
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
    functions["projectsExclusionsGet"] = logging.patch(
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
    functions["projectsExclusionsCreate"] = logging.patch(
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
    functions["projectsExclusionsList"] = logging.patch(
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
    functions["projectsExclusionsPatch"] = logging.patch(
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
    functions["projectsMetricsList"] = logging.put(
        "v2/{metricName}",
        t.struct(
            {
                "metricName": t.string(),
                "valueExtractor": t.string().optional(),
                "bucketName": t.string().optional(),
                "filter": t.string(),
                "version": t.string().optional(),
                "name": t.string(),
                "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "disabled": t.boolean().optional(),
                "metricDescriptor": t.proxy(renames["MetricDescriptorIn"]).optional(),
                "bucketOptions": t.proxy(renames["BucketOptionsIn"]).optional(),
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
                "valueExtractor": t.string().optional(),
                "bucketName": t.string().optional(),
                "filter": t.string(),
                "version": t.string().optional(),
                "name": t.string(),
                "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "disabled": t.boolean().optional(),
                "metricDescriptor": t.proxy(renames["MetricDescriptorIn"]).optional(),
                "bucketOptions": t.proxy(renames["BucketOptionsIn"]).optional(),
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
                "valueExtractor": t.string().optional(),
                "bucketName": t.string().optional(),
                "filter": t.string(),
                "version": t.string().optional(),
                "name": t.string(),
                "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "disabled": t.boolean().optional(),
                "metricDescriptor": t.proxy(renames["MetricDescriptorIn"]).optional(),
                "bucketOptions": t.proxy(renames["BucketOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogMetricOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMetricsCreate"] = logging.put(
        "v2/{metricName}",
        t.struct(
            {
                "metricName": t.string(),
                "valueExtractor": t.string().optional(),
                "bucketName": t.string().optional(),
                "filter": t.string(),
                "version": t.string().optional(),
                "name": t.string(),
                "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "disabled": t.boolean().optional(),
                "metricDescriptor": t.proxy(renames["MetricDescriptorIn"]).optional(),
                "bucketOptions": t.proxy(renames["BucketOptionsIn"]).optional(),
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
                "valueExtractor": t.string().optional(),
                "bucketName": t.string().optional(),
                "filter": t.string(),
                "version": t.string().optional(),
                "name": t.string(),
                "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "disabled": t.boolean().optional(),
                "metricDescriptor": t.proxy(renames["MetricDescriptorIn"]).optional(),
                "bucketOptions": t.proxy(renames["BucketOptionsIn"]).optional(),
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
    functions["projectsLogsList"] = logging.get(
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
    functions["projectsSinksDelete"] = logging.put(
        "v2/{sinkName}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "uniqueWriterIdentity": t.boolean().optional(),
                "sinkName": t.string(),
                "disabled": t.boolean().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "outputVersionFormat": t.string().optional(),
                "includeChildren": t.boolean().optional(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSinksGet"] = logging.put(
        "v2/{sinkName}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "uniqueWriterIdentity": t.boolean().optional(),
                "sinkName": t.string(),
                "disabled": t.boolean().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "outputVersionFormat": t.string().optional(),
                "includeChildren": t.boolean().optional(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSinksList"] = logging.put(
        "v2/{sinkName}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "uniqueWriterIdentity": t.boolean().optional(),
                "sinkName": t.string(),
                "disabled": t.boolean().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "outputVersionFormat": t.string().optional(),
                "includeChildren": t.boolean().optional(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSinksCreate"] = logging.put(
        "v2/{sinkName}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "uniqueWriterIdentity": t.boolean().optional(),
                "sinkName": t.string(),
                "disabled": t.boolean().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "outputVersionFormat": t.string().optional(),
                "includeChildren": t.boolean().optional(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSinksPatch"] = logging.put(
        "v2/{sinkName}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "uniqueWriterIdentity": t.boolean().optional(),
                "sinkName": t.string(),
                "disabled": t.boolean().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "outputVersionFormat": t.string().optional(),
                "includeChildren": t.boolean().optional(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSinksUpdate"] = logging.put(
        "v2/{sinkName}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "uniqueWriterIdentity": t.boolean().optional(),
                "sinkName": t.string(),
                "disabled": t.boolean().optional(),
                "description": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string(),
                "bigqueryOptions": t.proxy(renames["BigQueryOptionsIn"]).optional(),
                "exclusions": t.array(t.proxy(renames["LogExclusionIn"])).optional(),
                "outputVersionFormat": t.string().optional(),
                "includeChildren": t.boolean().optional(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogSinkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsGet"] = logging.get(
        "v2/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
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
    functions["locationsOperationsList"] = logging.get(
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
    functions["locationsBucketsUndelete"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "analyticsEnabled": t.boolean().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "retentionDays": t.integer().optional(),
                "locked": t.boolean().optional(),
                "description": t.string().optional(),
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
                "name": t.string(),
                "updateMask": t.string(),
                "analyticsEnabled": t.boolean().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "retentionDays": t.integer().optional(),
                "locked": t.boolean().optional(),
                "description": t.string().optional(),
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
                "name": t.string(),
                "updateMask": t.string(),
                "analyticsEnabled": t.boolean().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "retentionDays": t.integer().optional(),
                "locked": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsDelete"] = logging.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "analyticsEnabled": t.boolean().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "retentionDays": t.integer().optional(),
                "locked": t.boolean().optional(),
                "description": t.string().optional(),
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
                "name": t.string(),
                "updateMask": t.string(),
                "analyticsEnabled": t.boolean().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "retentionDays": t.integer().optional(),
                "locked": t.boolean().optional(),
                "description": t.string().optional(),
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
                "name": t.string(),
                "updateMask": t.string(),
                "analyticsEnabled": t.boolean().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "retentionDays": t.integer().optional(),
                "locked": t.boolean().optional(),
                "description": t.string().optional(),
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
                "name": t.string(),
                "updateMask": t.string(),
                "analyticsEnabled": t.boolean().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "retentionDays": t.integer().optional(),
                "locked": t.boolean().optional(),
                "description": t.string().optional(),
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
                "name": t.string(),
                "updateMask": t.string(),
                "analyticsEnabled": t.boolean().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "retentionDays": t.integer().optional(),
                "locked": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBucketsLinksDelete"] = logging.post(
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
    functions["locationsBucketsLinksList"] = logging.post(
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
    functions["locationsBucketsLinksGet"] = logging.post(
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
    functions["locationsBucketsLinksCreate"] = logging.post(
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
    functions["locationsBucketsViewsGet"] = logging.post(
        "v2/{parent}/views",
        t.struct(
            {
                "viewId": t.string(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
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
                "description": t.string().optional(),
                "name": t.string().optional(),
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
                "description": t.string().optional(),
                "name": t.string().optional(),
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
                "description": t.string().optional(),
                "name": t.string().optional(),
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
                "description": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogViewOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGetCmekSettings"] = logging.patch(
        "v2/{name}/settings",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "storageLocation": t.string().optional(),
                "disableDefaultSink": t.boolean().optional(),
                "kmsKeyName": t.string().optional(),
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
                "storageLocation": t.string().optional(),
                "disableDefaultSink": t.boolean().optional(),
                "kmsKeyName": t.string().optional(),
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
                "storageLocation": t.string().optional(),
                "disableDefaultSink": t.boolean().optional(),
                "kmsKeyName": t.string().optional(),
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
                "storageLocation": t.string().optional(),
                "disableDefaultSink": t.boolean().optional(),
                "kmsKeyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SettingsOut"]),
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
    functions["organizationsSinksDelete"] = logging.get(
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
    functions["organizationsSinksCreate"] = logging.get(
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
    functions["organizationsExclusionsList"] = logging.post(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "disabled": t.boolean().optional(),
                "filter": t.string(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsExclusionsGet"] = logging.post(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "disabled": t.boolean().optional(),
                "filter": t.string(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsExclusionsDelete"] = logging.post(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "disabled": t.boolean().optional(),
                "filter": t.string(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsExclusionsPatch"] = logging.post(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "disabled": t.boolean().optional(),
                "filter": t.string(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogExclusionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsExclusionsCreate"] = logging.post(
        "v2/{parent}/exclusions",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "disabled": t.boolean().optional(),
                "filter": t.string(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogExclusionOut"]),
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
    functions["organizationsLocationsBucketsUndelete"] = logging.post(
        "v2/{parent}/buckets",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "analyticsEnabled": t.boolean().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "retentionDays": t.integer().optional(),
                "locked": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsCreateAsync"] = logging.post(
        "v2/{parent}/buckets",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "analyticsEnabled": t.boolean().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "retentionDays": t.integer().optional(),
                "locked": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsDelete"] = logging.post(
        "v2/{parent}/buckets",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "analyticsEnabled": t.boolean().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "retentionDays": t.integer().optional(),
                "locked": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsPatch"] = logging.post(
        "v2/{parent}/buckets",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "analyticsEnabled": t.boolean().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "retentionDays": t.integer().optional(),
                "locked": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsGet"] = logging.post(
        "v2/{parent}/buckets",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "analyticsEnabled": t.boolean().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "retentionDays": t.integer().optional(),
                "locked": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsList"] = logging.post(
        "v2/{parent}/buckets",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "analyticsEnabled": t.boolean().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "retentionDays": t.integer().optional(),
                "locked": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsUpdateAsync"] = logging.post(
        "v2/{parent}/buckets",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "analyticsEnabled": t.boolean().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "retentionDays": t.integer().optional(),
                "locked": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsCreate"] = logging.post(
        "v2/{parent}/buckets",
        t.struct(
            {
                "bucketId": t.string(),
                "parent": t.string(),
                "analyticsEnabled": t.boolean().optional(),
                "indexConfigs": t.array(t.proxy(renames["IndexConfigIn"])).optional(),
                "restrictedFields": t.array(t.string()).optional(),
                "cmekSettings": t.proxy(renames["CmekSettingsIn"]).optional(),
                "retentionDays": t.integer().optional(),
                "locked": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LogBucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsViewsGet"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsViewsCreate"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsViewsList"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsViewsPatch"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsViewsDelete"] = logging.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsBucketsViewsLogsList"] = logging.get(
        "v2/{parent}/logs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "resourceNames": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLogsResponseOut"]),
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
    functions["foldersGetCmekSettings"] = logging.patch(
        "v2/{name}/settings",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "storageLocation": t.string().optional(),
                "disableDefaultSink": t.boolean().optional(),
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
                "storageLocation": t.string().optional(),
                "disableDefaultSink": t.boolean().optional(),
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
                "storageLocation": t.string().optional(),
                "disableDefaultSink": t.boolean().optional(),
                "kmsKeyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SettingsOut"]),
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
    functions["foldersExclusionsCreate"] = logging.get(
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
    functions["foldersExclusionsPatch"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogExclusionOut"]),
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
    functions["foldersExclusionsGet"] = logging.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LogExclusionOut"]),
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
    functions["foldersLocationsBucketsViewsCreate"] = logging.get(
        "v2/{parent}/views",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListViewsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsViewsDelete"] = logging.get(
        "v2/{parent}/views",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
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
    functions["foldersLocationsBucketsLinksCreate"] = logging.get(
        "v2/{parent}/links",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLinksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsLinksGet"] = logging.get(
        "v2/{parent}/links",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLinksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsLinksDelete"] = logging.get(
        "v2/{parent}/links",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLinksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsBucketsLinksList"] = logging.get(
        "v2/{parent}/links",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLinksResponseOut"]),
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
    functions["foldersSinksDelete"] = logging.get(
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
    functions["foldersSinksCreate"] = logging.get(
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
    functions["foldersSinksUpdate"] = logging.get(
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
    functions["foldersSinksPatch"] = logging.get(
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
    functions["foldersSinksGet"] = logging.get(
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
    functions["foldersSinksList"] = logging.get(
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

    return Import(
        importer="logging", renames=renames, types=Box(types), functions=Box(functions)
    )
