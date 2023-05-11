from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_monitoring() -> Import:
    monitoring = HTTPRuntime("https://monitoring.googleapis.com/")

    renames = {
        "ErrorResponse": "_monitoring_1_ErrorResponse",
        "DistributionCutIn": "_monitoring_2_DistributionCutIn",
        "DistributionCutOut": "_monitoring_3_DistributionCutOut",
        "PingConfigIn": "_monitoring_4_PingConfigIn",
        "PingConfigOut": "_monitoring_5_PingConfigOut",
        "NotificationChannelStrategyIn": "_monitoring_6_NotificationChannelStrategyIn",
        "NotificationChannelStrategyOut": "_monitoring_7_NotificationChannelStrategyOut",
        "DocumentationIn": "_monitoring_8_DocumentationIn",
        "DocumentationOut": "_monitoring_9_DocumentationOut",
        "GetNotificationChannelVerificationCodeResponseIn": "_monitoring_10_GetNotificationChannelVerificationCodeResponseIn",
        "GetNotificationChannelVerificationCodeResponseOut": "_monitoring_11_GetNotificationChannelVerificationCodeResponseOut",
        "ServiceLevelObjectiveIn": "_monitoring_12_ServiceLevelObjectiveIn",
        "ServiceLevelObjectiveOut": "_monitoring_13_ServiceLevelObjectiveOut",
        "ListServicesResponseIn": "_monitoring_14_ListServicesResponseIn",
        "ListServicesResponseOut": "_monitoring_15_ListServicesResponseOut",
        "TypedValueIn": "_monitoring_16_TypedValueIn",
        "TypedValueOut": "_monitoring_17_TypedValueOut",
        "ListTimeSeriesResponseIn": "_monitoring_18_ListTimeSeriesResponseIn",
        "ListTimeSeriesResponseOut": "_monitoring_19_ListTimeSeriesResponseOut",
        "SendNotificationChannelVerificationCodeRequestIn": "_monitoring_20_SendNotificationChannelVerificationCodeRequestIn",
        "SendNotificationChannelVerificationCodeRequestOut": "_monitoring_21_SendNotificationChannelVerificationCodeRequestOut",
        "TimeIntervalIn": "_monitoring_22_TimeIntervalIn",
        "TimeIntervalOut": "_monitoring_23_TimeIntervalOut",
        "CreateTimeSeriesSummaryIn": "_monitoring_24_CreateTimeSeriesSummaryIn",
        "CreateTimeSeriesSummaryOut": "_monitoring_25_CreateTimeSeriesSummaryOut",
        "DistributionIn": "_monitoring_26_DistributionIn",
        "DistributionOut": "_monitoring_27_DistributionOut",
        "TimeSeriesDescriptorIn": "_monitoring_28_TimeSeriesDescriptorIn",
        "TimeSeriesDescriptorOut": "_monitoring_29_TimeSeriesDescriptorOut",
        "HttpCheckIn": "_monitoring_30_HttpCheckIn",
        "HttpCheckOut": "_monitoring_31_HttpCheckOut",
        "ConditionIn": "_monitoring_32_ConditionIn",
        "ConditionOut": "_monitoring_33_ConditionOut",
        "SnoozeIn": "_monitoring_34_SnoozeIn",
        "SnoozeOut": "_monitoring_35_SnoozeOut",
        "CollectdValueErrorIn": "_monitoring_36_CollectdValueErrorIn",
        "CollectdValueErrorOut": "_monitoring_37_CollectdValueErrorOut",
        "QueryTimeSeriesRequestIn": "_monitoring_38_QueryTimeSeriesRequestIn",
        "QueryTimeSeriesRequestOut": "_monitoring_39_QueryTimeSeriesRequestOut",
        "OptionIn": "_monitoring_40_OptionIn",
        "OptionOut": "_monitoring_41_OptionOut",
        "MonitoredResourceMetadataIn": "_monitoring_42_MonitoredResourceMetadataIn",
        "MonitoredResourceMetadataOut": "_monitoring_43_MonitoredResourceMetadataOut",
        "LinearIn": "_monitoring_44_LinearIn",
        "LinearOut": "_monitoring_45_LinearOut",
        "MonitoredResourceIn": "_monitoring_46_MonitoredResourceIn",
        "MonitoredResourceOut": "_monitoring_47_MonitoredResourceOut",
        "AvailabilityCriteriaIn": "_monitoring_48_AvailabilityCriteriaIn",
        "AvailabilityCriteriaOut": "_monitoring_49_AvailabilityCriteriaOut",
        "PerformanceThresholdIn": "_monitoring_50_PerformanceThresholdIn",
        "PerformanceThresholdOut": "_monitoring_51_PerformanceThresholdOut",
        "InternalCheckerIn": "_monitoring_52_InternalCheckerIn",
        "InternalCheckerOut": "_monitoring_53_InternalCheckerOut",
        "CustomIn": "_monitoring_54_CustomIn",
        "CustomOut": "_monitoring_55_CustomOut",
        "ExemplarIn": "_monitoring_56_ExemplarIn",
        "ExemplarOut": "_monitoring_57_ExemplarOut",
        "UptimeCheckConfigIn": "_monitoring_58_UptimeCheckConfigIn",
        "UptimeCheckConfigOut": "_monitoring_59_UptimeCheckConfigOut",
        "NotificationRateLimitIn": "_monitoring_60_NotificationRateLimitIn",
        "NotificationRateLimitOut": "_monitoring_61_NotificationRateLimitOut",
        "ListGroupsResponseIn": "_monitoring_62_ListGroupsResponseIn",
        "ListGroupsResponseOut": "_monitoring_63_ListGroupsResponseOut",
        "TimeSeriesDataIn": "_monitoring_64_TimeSeriesDataIn",
        "TimeSeriesDataOut": "_monitoring_65_TimeSeriesDataOut",
        "CriteriaIn": "_monitoring_66_CriteriaIn",
        "CriteriaOut": "_monitoring_67_CriteriaOut",
        "NotificationChannelIn": "_monitoring_68_NotificationChannelIn",
        "NotificationChannelOut": "_monitoring_69_NotificationChannelOut",
        "TypeIn": "_monitoring_70_TypeIn",
        "TypeOut": "_monitoring_71_TypeOut",
        "ExplicitIn": "_monitoring_72_ExplicitIn",
        "ExplicitOut": "_monitoring_73_ExplicitOut",
        "JsonPathMatcherIn": "_monitoring_74_JsonPathMatcherIn",
        "JsonPathMatcherOut": "_monitoring_75_JsonPathMatcherOut",
        "GkeServiceIn": "_monitoring_76_GkeServiceIn",
        "GkeServiceOut": "_monitoring_77_GkeServiceOut",
        "TcpCheckIn": "_monitoring_78_TcpCheckIn",
        "TcpCheckOut": "_monitoring_79_TcpCheckOut",
        "LabelDescriptorIn": "_monitoring_80_LabelDescriptorIn",
        "LabelDescriptorOut": "_monitoring_81_LabelDescriptorOut",
        "QueryTimeSeriesResponseIn": "_monitoring_82_QueryTimeSeriesResponseIn",
        "QueryTimeSeriesResponseOut": "_monitoring_83_QueryTimeSeriesResponseOut",
        "CollectdPayloadErrorIn": "_monitoring_84_CollectdPayloadErrorIn",
        "CollectdPayloadErrorOut": "_monitoring_85_CollectdPayloadErrorOut",
        "CloudRunIn": "_monitoring_86_CloudRunIn",
        "CloudRunOut": "_monitoring_87_CloudRunOut",
        "BasicServiceIn": "_monitoring_88_BasicServiceIn",
        "BasicServiceOut": "_monitoring_89_BasicServiceOut",
        "GoogleMonitoringV3RangeIn": "_monitoring_90_GoogleMonitoringV3RangeIn",
        "GoogleMonitoringV3RangeOut": "_monitoring_91_GoogleMonitoringV3RangeOut",
        "MetricAbsenceIn": "_monitoring_92_MetricAbsenceIn",
        "MetricAbsenceOut": "_monitoring_93_MetricAbsenceOut",
        "FieldIn": "_monitoring_94_FieldIn",
        "FieldOut": "_monitoring_95_FieldOut",
        "ResponseStatusCodeIn": "_monitoring_96_ResponseStatusCodeIn",
        "ResponseStatusCodeOut": "_monitoring_97_ResponseStatusCodeOut",
        "ListSnoozesResponseIn": "_monitoring_98_ListSnoozesResponseIn",
        "ListSnoozesResponseOut": "_monitoring_99_ListSnoozesResponseOut",
        "GkeWorkloadIn": "_monitoring_100_GkeWorkloadIn",
        "GkeWorkloadOut": "_monitoring_101_GkeWorkloadOut",
        "ListNotificationChannelDescriptorsResponseIn": "_monitoring_102_ListNotificationChannelDescriptorsResponseIn",
        "ListNotificationChannelDescriptorsResponseOut": "_monitoring_103_ListNotificationChannelDescriptorsResponseOut",
        "LatencyCriteriaIn": "_monitoring_104_LatencyCriteriaIn",
        "LatencyCriteriaOut": "_monitoring_105_LatencyCriteriaOut",
        "GroupIn": "_monitoring_106_GroupIn",
        "GroupOut": "_monitoring_107_GroupOut",
        "LogMatchIn": "_monitoring_108_LogMatchIn",
        "LogMatchOut": "_monitoring_109_LogMatchOut",
        "MetricThresholdIn": "_monitoring_110_MetricThresholdIn",
        "MetricThresholdOut": "_monitoring_111_MetricThresholdOut",
        "MonitoredResourceDescriptorIn": "_monitoring_112_MonitoredResourceDescriptorIn",
        "MonitoredResourceDescriptorOut": "_monitoring_113_MonitoredResourceDescriptorOut",
        "PointIn": "_monitoring_114_PointIn",
        "PointOut": "_monitoring_115_PointOut",
        "ExponentialIn": "_monitoring_116_ExponentialIn",
        "ExponentialOut": "_monitoring_117_ExponentialOut",
        "CollectdValueIn": "_monitoring_118_CollectdValueIn",
        "CollectdValueOut": "_monitoring_119_CollectdValueOut",
        "MeshIstioIn": "_monitoring_120_MeshIstioIn",
        "MeshIstioOut": "_monitoring_121_MeshIstioOut",
        "ClusterIstioIn": "_monitoring_122_ClusterIstioIn",
        "ClusterIstioOut": "_monitoring_123_ClusterIstioOut",
        "MutationRecordIn": "_monitoring_124_MutationRecordIn",
        "MutationRecordOut": "_monitoring_125_MutationRecordOut",
        "AppEngineIn": "_monitoring_126_AppEngineIn",
        "AppEngineOut": "_monitoring_127_AppEngineOut",
        "TriggerIn": "_monitoring_128_TriggerIn",
        "TriggerOut": "_monitoring_129_TriggerOut",
        "DroppedLabelsIn": "_monitoring_130_DroppedLabelsIn",
        "DroppedLabelsOut": "_monitoring_131_DroppedLabelsOut",
        "ListNotificationChannelsResponseIn": "_monitoring_132_ListNotificationChannelsResponseIn",
        "ListNotificationChannelsResponseOut": "_monitoring_133_ListNotificationChannelsResponseOut",
        "ErrorIn": "_monitoring_134_ErrorIn",
        "ErrorOut": "_monitoring_135_ErrorOut",
        "GetNotificationChannelVerificationCodeRequestIn": "_monitoring_136_GetNotificationChannelVerificationCodeRequestIn",
        "GetNotificationChannelVerificationCodeRequestOut": "_monitoring_137_GetNotificationChannelVerificationCodeRequestOut",
        "ServiceIn": "_monitoring_138_ServiceIn",
        "ServiceOut": "_monitoring_139_ServiceOut",
        "ListServiceLevelObjectivesResponseIn": "_monitoring_140_ListServiceLevelObjectivesResponseIn",
        "ListServiceLevelObjectivesResponseOut": "_monitoring_141_ListServiceLevelObjectivesResponseOut",
        "CreateTimeSeriesRequestIn": "_monitoring_142_CreateTimeSeriesRequestIn",
        "CreateTimeSeriesRequestOut": "_monitoring_143_CreateTimeSeriesRequestOut",
        "RequestBasedSliIn": "_monitoring_144_RequestBasedSliIn",
        "RequestBasedSliOut": "_monitoring_145_RequestBasedSliOut",
        "ListAlertPoliciesResponseIn": "_monitoring_146_ListAlertPoliciesResponseIn",
        "ListAlertPoliciesResponseOut": "_monitoring_147_ListAlertPoliciesResponseOut",
        "ListUptimeCheckIpsResponseIn": "_monitoring_148_ListUptimeCheckIpsResponseIn",
        "ListUptimeCheckIpsResponseOut": "_monitoring_149_ListUptimeCheckIpsResponseOut",
        "MetricDescriptorIn": "_monitoring_150_MetricDescriptorIn",
        "MetricDescriptorOut": "_monitoring_151_MetricDescriptorOut",
        "ForecastOptionsIn": "_monitoring_152_ForecastOptionsIn",
        "ForecastOptionsOut": "_monitoring_153_ForecastOptionsOut",
        "AlertPolicyIn": "_monitoring_154_AlertPolicyIn",
        "AlertPolicyOut": "_monitoring_155_AlertPolicyOut",
        "ListUptimeCheckConfigsResponseIn": "_monitoring_156_ListUptimeCheckConfigsResponseIn",
        "ListUptimeCheckConfigsResponseOut": "_monitoring_157_ListUptimeCheckConfigsResponseOut",
        "ListMonitoredResourceDescriptorsResponseIn": "_monitoring_158_ListMonitoredResourceDescriptorsResponseIn",
        "ListMonitoredResourceDescriptorsResponseOut": "_monitoring_159_ListMonitoredResourceDescriptorsResponseOut",
        "EmptyIn": "_monitoring_160_EmptyIn",
        "EmptyOut": "_monitoring_161_EmptyOut",
        "RangeIn": "_monitoring_162_RangeIn",
        "RangeOut": "_monitoring_163_RangeOut",
        "SourceContextIn": "_monitoring_164_SourceContextIn",
        "SourceContextOut": "_monitoring_165_SourceContextOut",
        "BasicSliIn": "_monitoring_166_BasicSliIn",
        "BasicSliOut": "_monitoring_167_BasicSliOut",
        "MetricDescriptorMetadataIn": "_monitoring_168_MetricDescriptorMetadataIn",
        "MetricDescriptorMetadataOut": "_monitoring_169_MetricDescriptorMetadataOut",
        "SpanContextIn": "_monitoring_170_SpanContextIn",
        "SpanContextOut": "_monitoring_171_SpanContextOut",
        "GkeNamespaceIn": "_monitoring_172_GkeNamespaceIn",
        "GkeNamespaceOut": "_monitoring_173_GkeNamespaceOut",
        "ServiceLevelIndicatorIn": "_monitoring_174_ServiceLevelIndicatorIn",
        "ServiceLevelIndicatorOut": "_monitoring_175_ServiceLevelIndicatorOut",
        "CloudEndpointsIn": "_monitoring_176_CloudEndpointsIn",
        "CloudEndpointsOut": "_monitoring_177_CloudEndpointsOut",
        "MetricRangeIn": "_monitoring_178_MetricRangeIn",
        "MetricRangeOut": "_monitoring_179_MetricRangeOut",
        "MonitoringQueryLanguageConditionIn": "_monitoring_180_MonitoringQueryLanguageConditionIn",
        "MonitoringQueryLanguageConditionOut": "_monitoring_181_MonitoringQueryLanguageConditionOut",
        "CollectdPayloadIn": "_monitoring_182_CollectdPayloadIn",
        "CollectdPayloadOut": "_monitoring_183_CollectdPayloadOut",
        "CreateCollectdTimeSeriesRequestIn": "_monitoring_184_CreateCollectdTimeSeriesRequestIn",
        "CreateCollectdTimeSeriesRequestOut": "_monitoring_185_CreateCollectdTimeSeriesRequestOut",
        "PointDataIn": "_monitoring_186_PointDataIn",
        "PointDataOut": "_monitoring_187_PointDataOut",
        "AlertStrategyIn": "_monitoring_188_AlertStrategyIn",
        "AlertStrategyOut": "_monitoring_189_AlertStrategyOut",
        "TimeSeriesIn": "_monitoring_190_TimeSeriesIn",
        "TimeSeriesOut": "_monitoring_191_TimeSeriesOut",
        "BasicAuthenticationIn": "_monitoring_192_BasicAuthenticationIn",
        "BasicAuthenticationOut": "_monitoring_193_BasicAuthenticationOut",
        "WindowsBasedSliIn": "_monitoring_194_WindowsBasedSliIn",
        "WindowsBasedSliOut": "_monitoring_195_WindowsBasedSliOut",
        "AggregationIn": "_monitoring_196_AggregationIn",
        "AggregationOut": "_monitoring_197_AggregationOut",
        "ListGroupMembersResponseIn": "_monitoring_198_ListGroupMembersResponseIn",
        "ListGroupMembersResponseOut": "_monitoring_199_ListGroupMembersResponseOut",
        "TimeSeriesRatioIn": "_monitoring_200_TimeSeriesRatioIn",
        "TimeSeriesRatioOut": "_monitoring_201_TimeSeriesRatioOut",
        "LabelValueIn": "_monitoring_202_LabelValueIn",
        "LabelValueOut": "_monitoring_203_LabelValueOut",
        "UptimeCheckIpIn": "_monitoring_204_UptimeCheckIpIn",
        "UptimeCheckIpOut": "_monitoring_205_UptimeCheckIpOut",
        "ValueDescriptorIn": "_monitoring_206_ValueDescriptorIn",
        "ValueDescriptorOut": "_monitoring_207_ValueDescriptorOut",
        "ContentMatcherIn": "_monitoring_208_ContentMatcherIn",
        "ContentMatcherOut": "_monitoring_209_ContentMatcherOut",
        "BucketOptionsIn": "_monitoring_210_BucketOptionsIn",
        "BucketOptionsOut": "_monitoring_211_BucketOptionsOut",
        "NotificationChannelDescriptorIn": "_monitoring_212_NotificationChannelDescriptorIn",
        "NotificationChannelDescriptorOut": "_monitoring_213_NotificationChannelDescriptorOut",
        "OperationMetadataIn": "_monitoring_214_OperationMetadataIn",
        "OperationMetadataOut": "_monitoring_215_OperationMetadataOut",
        "IstioCanonicalServiceIn": "_monitoring_216_IstioCanonicalServiceIn",
        "IstioCanonicalServiceOut": "_monitoring_217_IstioCanonicalServiceOut",
        "ListMetricDescriptorsResponseIn": "_monitoring_218_ListMetricDescriptorsResponseIn",
        "ListMetricDescriptorsResponseOut": "_monitoring_219_ListMetricDescriptorsResponseOut",
        "CreateCollectdTimeSeriesResponseIn": "_monitoring_220_CreateCollectdTimeSeriesResponseIn",
        "CreateCollectdTimeSeriesResponseOut": "_monitoring_221_CreateCollectdTimeSeriesResponseOut",
        "VerifyNotificationChannelRequestIn": "_monitoring_222_VerifyNotificationChannelRequestIn",
        "VerifyNotificationChannelRequestOut": "_monitoring_223_VerifyNotificationChannelRequestOut",
        "TelemetryIn": "_monitoring_224_TelemetryIn",
        "TelemetryOut": "_monitoring_225_TelemetryOut",
        "StatusIn": "_monitoring_226_StatusIn",
        "StatusOut": "_monitoring_227_StatusOut",
        "ResourceGroupIn": "_monitoring_228_ResourceGroupIn",
        "ResourceGroupOut": "_monitoring_229_ResourceGroupOut",
        "MetricIn": "_monitoring_230_MetricIn",
        "MetricOut": "_monitoring_231_MetricOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["DistributionCutIn"] = t.struct(
        {
            "range": t.proxy(renames["GoogleMonitoringV3RangeIn"]).optional(),
            "distributionFilter": t.string().optional(),
        }
    ).named(renames["DistributionCutIn"])
    types["DistributionCutOut"] = t.struct(
        {
            "range": t.proxy(renames["GoogleMonitoringV3RangeOut"]).optional(),
            "distributionFilter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DistributionCutOut"])
    types["PingConfigIn"] = t.struct({"pingsCount": t.integer().optional()}).named(
        renames["PingConfigIn"]
    )
    types["PingConfigOut"] = t.struct(
        {
            "pingsCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PingConfigOut"])
    types["NotificationChannelStrategyIn"] = t.struct(
        {
            "renotifyInterval": t.string().optional(),
            "notificationChannelNames": t.array(t.string()).optional(),
        }
    ).named(renames["NotificationChannelStrategyIn"])
    types["NotificationChannelStrategyOut"] = t.struct(
        {
            "renotifyInterval": t.string().optional(),
            "notificationChannelNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationChannelStrategyOut"])
    types["DocumentationIn"] = t.struct(
        {"content": t.string().optional(), "mimeType": t.string().optional()}
    ).named(renames["DocumentationIn"])
    types["DocumentationOut"] = t.struct(
        {
            "content": t.string().optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationOut"])
    types["GetNotificationChannelVerificationCodeResponseIn"] = t.struct(
        {"expireTime": t.string().optional(), "code": t.string().optional()}
    ).named(renames["GetNotificationChannelVerificationCodeResponseIn"])
    types["GetNotificationChannelVerificationCodeResponseOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetNotificationChannelVerificationCodeResponseOut"])
    types["ServiceLevelObjectiveIn"] = t.struct(
        {
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "serviceLevelIndicator": t.proxy(
                renames["ServiceLevelIndicatorIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "goal": t.number().optional(),
            "rollingPeriod": t.string().optional(),
            "calendarPeriod": t.string().optional(),
        }
    ).named(renames["ServiceLevelObjectiveIn"])
    types["ServiceLevelObjectiveOut"] = t.struct(
        {
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "serviceLevelIndicator": t.proxy(
                renames["ServiceLevelIndicatorOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "goal": t.number().optional(),
            "rollingPeriod": t.string().optional(),
            "calendarPeriod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceLevelObjectiveOut"])
    types["ListServicesResponseIn"] = t.struct(
        {
            "services": t.array(t.proxy(renames["ServiceIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListServicesResponseIn"])
    types["ListServicesResponseOut"] = t.struct(
        {
            "services": t.array(t.proxy(renames["ServiceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServicesResponseOut"])
    types["TypedValueIn"] = t.struct(
        {
            "doubleValue": t.number().optional(),
            "distributionValue": t.proxy(renames["DistributionIn"]).optional(),
            "boolValue": t.boolean().optional(),
            "stringValue": t.string().optional(),
            "int64Value": t.string().optional(),
        }
    ).named(renames["TypedValueIn"])
    types["TypedValueOut"] = t.struct(
        {
            "doubleValue": t.number().optional(),
            "distributionValue": t.proxy(renames["DistributionOut"]).optional(),
            "boolValue": t.boolean().optional(),
            "stringValue": t.string().optional(),
            "int64Value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypedValueOut"])
    types["ListTimeSeriesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "timeSeries": t.array(t.proxy(renames["TimeSeriesIn"])).optional(),
            "executionErrors": t.array(t.proxy(renames["StatusIn"])).optional(),
            "unit": t.string().optional(),
        }
    ).named(renames["ListTimeSeriesResponseIn"])
    types["ListTimeSeriesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "timeSeries": t.array(t.proxy(renames["TimeSeriesOut"])).optional(),
            "executionErrors": t.array(t.proxy(renames["StatusOut"])).optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTimeSeriesResponseOut"])
    types["SendNotificationChannelVerificationCodeRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SendNotificationChannelVerificationCodeRequestIn"])
    types["SendNotificationChannelVerificationCodeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SendNotificationChannelVerificationCodeRequestOut"])
    types["TimeIntervalIn"] = t.struct(
        {"startTime": t.string().optional(), "endTime": t.string()}
    ).named(renames["TimeIntervalIn"])
    types["TimeIntervalOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeIntervalOut"])
    types["CreateTimeSeriesSummaryIn"] = t.struct(
        {
            "totalPointCount": t.integer().optional(),
            "successPointCount": t.integer().optional(),
            "errors": t.array(t.proxy(renames["ErrorIn"])).optional(),
        }
    ).named(renames["CreateTimeSeriesSummaryIn"])
    types["CreateTimeSeriesSummaryOut"] = t.struct(
        {
            "totalPointCount": t.integer().optional(),
            "successPointCount": t.integer().optional(),
            "errors": t.array(t.proxy(renames["ErrorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateTimeSeriesSummaryOut"])
    types["DistributionIn"] = t.struct(
        {
            "range": t.proxy(renames["RangeIn"]).optional(),
            "bucketOptions": t.proxy(renames["BucketOptionsIn"]),
            "mean": t.number().optional(),
            "count": t.string().optional(),
            "sumOfSquaredDeviation": t.number().optional(),
            "bucketCounts": t.array(t.string()),
            "exemplars": t.array(t.proxy(renames["ExemplarIn"])).optional(),
        }
    ).named(renames["DistributionIn"])
    types["DistributionOut"] = t.struct(
        {
            "range": t.proxy(renames["RangeOut"]).optional(),
            "bucketOptions": t.proxy(renames["BucketOptionsOut"]),
            "mean": t.number().optional(),
            "count": t.string().optional(),
            "sumOfSquaredDeviation": t.number().optional(),
            "bucketCounts": t.array(t.string()),
            "exemplars": t.array(t.proxy(renames["ExemplarOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DistributionOut"])
    types["TimeSeriesDescriptorIn"] = t.struct(
        {
            "pointDescriptors": t.array(
                t.proxy(renames["ValueDescriptorIn"])
            ).optional(),
            "labelDescriptors": t.array(
                t.proxy(renames["LabelDescriptorIn"])
            ).optional(),
        }
    ).named(renames["TimeSeriesDescriptorIn"])
    types["TimeSeriesDescriptorOut"] = t.struct(
        {
            "pointDescriptors": t.array(
                t.proxy(renames["ValueDescriptorOut"])
            ).optional(),
            "labelDescriptors": t.array(
                t.proxy(renames["LabelDescriptorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeSeriesDescriptorOut"])
    types["HttpCheckIn"] = t.struct(
        {
            "requestMethod": t.string().optional(),
            "validateSsl": t.boolean().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "path": t.string().optional(),
            "port": t.integer().optional(),
            "acceptedResponseStatusCodes": t.array(
                t.proxy(renames["ResponseStatusCodeIn"])
            ).optional(),
            "useSsl": t.boolean().optional(),
            "contentType": t.string().optional(),
            "customContentType": t.string().optional(),
            "authInfo": t.proxy(renames["BasicAuthenticationIn"]).optional(),
            "pingConfig": t.proxy(renames["PingConfigIn"]).optional(),
            "body": t.string().optional(),
            "maskHeaders": t.boolean().optional(),
        }
    ).named(renames["HttpCheckIn"])
    types["HttpCheckOut"] = t.struct(
        {
            "requestMethod": t.string().optional(),
            "validateSsl": t.boolean().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "path": t.string().optional(),
            "port": t.integer().optional(),
            "acceptedResponseStatusCodes": t.array(
                t.proxy(renames["ResponseStatusCodeOut"])
            ).optional(),
            "useSsl": t.boolean().optional(),
            "contentType": t.string().optional(),
            "customContentType": t.string().optional(),
            "authInfo": t.proxy(renames["BasicAuthenticationOut"]).optional(),
            "pingConfig": t.proxy(renames["PingConfigOut"]).optional(),
            "body": t.string().optional(),
            "maskHeaders": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpCheckOut"])
    types["ConditionIn"] = t.struct(
        {
            "conditionAbsent": t.proxy(renames["MetricAbsenceIn"]).optional(),
            "conditionMatchedLog": t.proxy(renames["LogMatchIn"]).optional(),
            "name": t.string(),
            "conditionMonitoringQueryLanguage": t.proxy(
                renames["MonitoringQueryLanguageConditionIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "conditionThreshold": t.proxy(renames["MetricThresholdIn"]).optional(),
        }
    ).named(renames["ConditionIn"])
    types["ConditionOut"] = t.struct(
        {
            "conditionAbsent": t.proxy(renames["MetricAbsenceOut"]).optional(),
            "conditionMatchedLog": t.proxy(renames["LogMatchOut"]).optional(),
            "name": t.string(),
            "conditionMonitoringQueryLanguage": t.proxy(
                renames["MonitoringQueryLanguageConditionOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "conditionThreshold": t.proxy(renames["MetricThresholdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionOut"])
    types["SnoozeIn"] = t.struct(
        {
            "name": t.string(),
            "displayName": t.string(),
            "interval": t.proxy(renames["TimeIntervalIn"]),
            "criteria": t.proxy(renames["CriteriaIn"]),
        }
    ).named(renames["SnoozeIn"])
    types["SnoozeOut"] = t.struct(
        {
            "name": t.string(),
            "displayName": t.string(),
            "interval": t.proxy(renames["TimeIntervalOut"]),
            "criteria": t.proxy(renames["CriteriaOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnoozeOut"])
    types["CollectdValueErrorIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "index": t.integer().optional(),
        }
    ).named(renames["CollectdValueErrorIn"])
    types["CollectdValueErrorOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "index": t.integer().optional(),
        }
    ).named(renames["CollectdValueErrorOut"])
    types["QueryTimeSeriesRequestIn"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "query": t.string(),
        }
    ).named(renames["QueryTimeSeriesRequestIn"])
    types["QueryTimeSeriesRequestOut"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "query": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryTimeSeriesRequestOut"])
    types["OptionIn"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OptionIn"])
    types["OptionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptionOut"])
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
    types["LinearIn"] = t.struct(
        {
            "numFiniteBuckets": t.integer().optional(),
            "offset": t.number().optional(),
            "width": t.number().optional(),
        }
    ).named(renames["LinearIn"])
    types["LinearOut"] = t.struct(
        {
            "numFiniteBuckets": t.integer().optional(),
            "offset": t.number().optional(),
            "width": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinearOut"])
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
    types["AvailabilityCriteriaIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AvailabilityCriteriaIn"]
    )
    types["AvailabilityCriteriaOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AvailabilityCriteriaOut"])
    types["PerformanceThresholdIn"] = t.struct(
        {
            "basicSliPerformance": t.proxy(renames["BasicSliIn"]).optional(),
            "threshold": t.number().optional(),
            "performance": t.proxy(renames["RequestBasedSliIn"]).optional(),
        }
    ).named(renames["PerformanceThresholdIn"])
    types["PerformanceThresholdOut"] = t.struct(
        {
            "basicSliPerformance": t.proxy(renames["BasicSliOut"]).optional(),
            "threshold": t.number().optional(),
            "performance": t.proxy(renames["RequestBasedSliOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerformanceThresholdOut"])
    types["InternalCheckerIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "gcpZone": t.string().optional(),
            "peerProjectId": t.string().optional(),
            "network": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["InternalCheckerIn"])
    types["InternalCheckerOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "gcpZone": t.string().optional(),
            "peerProjectId": t.string().optional(),
            "network": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InternalCheckerOut"])
    types["CustomIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CustomIn"]
    )
    types["CustomOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CustomOut"])
    types["ExemplarIn"] = t.struct(
        {
            "timestamp": t.string().optional(),
            "attachments": t.array(t.struct({"_": t.string().optional()})).optional(),
            "value": t.number().optional(),
        }
    ).named(renames["ExemplarIn"])
    types["ExemplarOut"] = t.struct(
        {
            "timestamp": t.string().optional(),
            "attachments": t.array(t.struct({"_": t.string().optional()})).optional(),
            "value": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExemplarOut"])
    types["UptimeCheckConfigIn"] = t.struct(
        {
            "selectedRegions": t.array(t.string()).optional(),
            "checkerType": t.string().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "contentMatchers": t.array(t.proxy(renames["ContentMatcherIn"])).optional(),
            "internalCheckers": t.array(
                t.proxy(renames["InternalCheckerIn"])
            ).optional(),
            "period": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "monitoredResource": t.proxy(renames["MonitoredResourceIn"]).optional(),
            "httpCheck": t.proxy(renames["HttpCheckIn"]).optional(),
            "isInternal": t.boolean().optional(),
            "tcpCheck": t.proxy(renames["TcpCheckIn"]).optional(),
            "timeout": t.string().optional(),
            "resourceGroup": t.proxy(renames["ResourceGroupIn"]).optional(),
        }
    ).named(renames["UptimeCheckConfigIn"])
    types["UptimeCheckConfigOut"] = t.struct(
        {
            "selectedRegions": t.array(t.string()).optional(),
            "checkerType": t.string().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "contentMatchers": t.array(
                t.proxy(renames["ContentMatcherOut"])
            ).optional(),
            "internalCheckers": t.array(
                t.proxy(renames["InternalCheckerOut"])
            ).optional(),
            "period": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "monitoredResource": t.proxy(renames["MonitoredResourceOut"]).optional(),
            "httpCheck": t.proxy(renames["HttpCheckOut"]).optional(),
            "isInternal": t.boolean().optional(),
            "tcpCheck": t.proxy(renames["TcpCheckOut"]).optional(),
            "timeout": t.string().optional(),
            "resourceGroup": t.proxy(renames["ResourceGroupOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UptimeCheckConfigOut"])
    types["NotificationRateLimitIn"] = t.struct(
        {"period": t.string().optional()}
    ).named(renames["NotificationRateLimitIn"])
    types["NotificationRateLimitOut"] = t.struct(
        {
            "period": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationRateLimitOut"])
    types["ListGroupsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "group": t.array(t.proxy(renames["GroupIn"])).optional(),
        }
    ).named(renames["ListGroupsResponseIn"])
    types["ListGroupsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "group": t.array(t.proxy(renames["GroupOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGroupsResponseOut"])
    types["TimeSeriesDataIn"] = t.struct(
        {
            "labelValues": t.array(t.proxy(renames["LabelValueIn"])).optional(),
            "pointData": t.array(t.proxy(renames["PointDataIn"])).optional(),
        }
    ).named(renames["TimeSeriesDataIn"])
    types["TimeSeriesDataOut"] = t.struct(
        {
            "labelValues": t.array(t.proxy(renames["LabelValueOut"])).optional(),
            "pointData": t.array(t.proxy(renames["PointDataOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeSeriesDataOut"])
    types["CriteriaIn"] = t.struct({"policies": t.array(t.string()).optional()}).named(
        renames["CriteriaIn"]
    )
    types["CriteriaOut"] = t.struct(
        {
            "policies": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CriteriaOut"])
    types["NotificationChannelIn"] = t.struct(
        {
            "name": t.string().optional(),
            "enabled": t.boolean().optional(),
            "description": t.string().optional(),
            "verificationStatus": t.string().optional(),
            "creationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "mutationRecords": t.array(t.proxy(renames["MutationRecordIn"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["NotificationChannelIn"])
    types["NotificationChannelOut"] = t.struct(
        {
            "name": t.string().optional(),
            "enabled": t.boolean().optional(),
            "description": t.string().optional(),
            "verificationStatus": t.string().optional(),
            "creationRecord": t.proxy(renames["MutationRecordOut"]).optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "mutationRecords": t.array(
                t.proxy(renames["MutationRecordOut"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationChannelOut"])
    types["TypeIn"] = t.struct(
        {
            "syntax": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "oneofs": t.array(t.string()).optional(),
            "fields": t.array(t.proxy(renames["FieldIn"])).optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "edition": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "syntax": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "oneofs": t.array(t.string()).optional(),
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "edition": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
    types["ExplicitIn"] = t.struct({"bounds": t.array(t.number()).optional()}).named(
        renames["ExplicitIn"]
    )
    types["ExplicitOut"] = t.struct(
        {
            "bounds": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExplicitOut"])
    types["JsonPathMatcherIn"] = t.struct(
        {"jsonPath": t.string().optional(), "jsonMatcher": t.string().optional()}
    ).named(renames["JsonPathMatcherIn"])
    types["JsonPathMatcherOut"] = t.struct(
        {
            "jsonPath": t.string().optional(),
            "jsonMatcher": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JsonPathMatcherOut"])
    types["GkeServiceIn"] = t.struct(
        {
            "serviceName": t.string().optional(),
            "namespaceName": t.string().optional(),
            "clusterName": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["GkeServiceIn"])
    types["GkeServiceOut"] = t.struct(
        {
            "serviceName": t.string().optional(),
            "namespaceName": t.string().optional(),
            "projectId": t.string().optional(),
            "clusterName": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeServiceOut"])
    types["TcpCheckIn"] = t.struct(
        {
            "pingConfig": t.proxy(renames["PingConfigIn"]).optional(),
            "port": t.integer().optional(),
        }
    ).named(renames["TcpCheckIn"])
    types["TcpCheckOut"] = t.struct(
        {
            "pingConfig": t.proxy(renames["PingConfigOut"]).optional(),
            "port": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TcpCheckOut"])
    types["LabelDescriptorIn"] = t.struct(
        {
            "description": t.string().optional(),
            "key": t.string().optional(),
            "valueType": t.string().optional(),
        }
    ).named(renames["LabelDescriptorIn"])
    types["LabelDescriptorOut"] = t.struct(
        {
            "description": t.string().optional(),
            "key": t.string().optional(),
            "valueType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelDescriptorOut"])
    types["QueryTimeSeriesResponseIn"] = t.struct(
        {
            "timeSeriesData": t.array(t.proxy(renames["TimeSeriesDataIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "partialErrors": t.array(t.proxy(renames["StatusIn"])).optional(),
            "timeSeriesDescriptor": t.proxy(
                renames["TimeSeriesDescriptorIn"]
            ).optional(),
        }
    ).named(renames["QueryTimeSeriesResponseIn"])
    types["QueryTimeSeriesResponseOut"] = t.struct(
        {
            "timeSeriesData": t.array(t.proxy(renames["TimeSeriesDataOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "partialErrors": t.array(t.proxy(renames["StatusOut"])).optional(),
            "timeSeriesDescriptor": t.proxy(
                renames["TimeSeriesDescriptorOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryTimeSeriesResponseOut"])
    types["CollectdPayloadErrorIn"] = t.struct(
        {
            "valueErrors": t.array(t.proxy(renames["CollectdValueErrorIn"])).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "index": t.integer().optional(),
        }
    ).named(renames["CollectdPayloadErrorIn"])
    types["CollectdPayloadErrorOut"] = t.struct(
        {
            "valueErrors": t.array(
                t.proxy(renames["CollectdValueErrorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "index": t.integer().optional(),
        }
    ).named(renames["CollectdPayloadErrorOut"])
    types["CloudRunIn"] = t.struct(
        {"location": t.string().optional(), "serviceName": t.string().optional()}
    ).named(renames["CloudRunIn"])
    types["CloudRunOut"] = t.struct(
        {
            "location": t.string().optional(),
            "serviceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRunOut"])
    types["BasicServiceIn"] = t.struct(
        {
            "serviceType": t.string().optional(),
            "serviceLabels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["BasicServiceIn"])
    types["BasicServiceOut"] = t.struct(
        {
            "serviceType": t.string().optional(),
            "serviceLabels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicServiceOut"])
    types["GoogleMonitoringV3RangeIn"] = t.struct(
        {"min": t.number().optional(), "max": t.number().optional()}
    ).named(renames["GoogleMonitoringV3RangeIn"])
    types["GoogleMonitoringV3RangeOut"] = t.struct(
        {
            "min": t.number().optional(),
            "max": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleMonitoringV3RangeOut"])
    types["MetricAbsenceIn"] = t.struct(
        {
            "duration": t.string().optional(),
            "filter": t.string(),
            "aggregations": t.array(t.proxy(renames["AggregationIn"])).optional(),
            "trigger": t.proxy(renames["TriggerIn"]).optional(),
        }
    ).named(renames["MetricAbsenceIn"])
    types["MetricAbsenceOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "filter": t.string(),
            "aggregations": t.array(t.proxy(renames["AggregationOut"])).optional(),
            "trigger": t.proxy(renames["TriggerOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricAbsenceOut"])
    types["FieldIn"] = t.struct(
        {
            "number": t.integer().optional(),
            "jsonName": t.string().optional(),
            "cardinality": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "typeUrl": t.string().optional(),
            "packed": t.boolean().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "defaultValue": t.string().optional(),
            "oneofIndex": t.integer().optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "number": t.integer().optional(),
            "jsonName": t.string().optional(),
            "cardinality": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "typeUrl": t.string().optional(),
            "packed": t.boolean().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "defaultValue": t.string().optional(),
            "oneofIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
    types["ResponseStatusCodeIn"] = t.struct(
        {"statusValue": t.integer().optional(), "statusClass": t.string().optional()}
    ).named(renames["ResponseStatusCodeIn"])
    types["ResponseStatusCodeOut"] = t.struct(
        {
            "statusValue": t.integer().optional(),
            "statusClass": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseStatusCodeOut"])
    types["ListSnoozesResponseIn"] = t.struct(
        {
            "snoozes": t.array(t.proxy(renames["SnoozeIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListSnoozesResponseIn"])
    types["ListSnoozesResponseOut"] = t.struct(
        {
            "snoozes": t.array(t.proxy(renames["SnoozeOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSnoozesResponseOut"])
    types["GkeWorkloadIn"] = t.struct(
        {
            "namespaceName": t.string().optional(),
            "topLevelControllerName": t.string().optional(),
            "clusterName": t.string().optional(),
            "location": t.string().optional(),
            "topLevelControllerType": t.string().optional(),
        }
    ).named(renames["GkeWorkloadIn"])
    types["GkeWorkloadOut"] = t.struct(
        {
            "namespaceName": t.string().optional(),
            "topLevelControllerName": t.string().optional(),
            "projectId": t.string().optional(),
            "clusterName": t.string().optional(),
            "location": t.string().optional(),
            "topLevelControllerType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeWorkloadOut"])
    types["ListNotificationChannelDescriptorsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "channelDescriptors": t.array(
                t.proxy(renames["NotificationChannelDescriptorIn"])
            ).optional(),
        }
    ).named(renames["ListNotificationChannelDescriptorsResponseIn"])
    types["ListNotificationChannelDescriptorsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "channelDescriptors": t.array(
                t.proxy(renames["NotificationChannelDescriptorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNotificationChannelDescriptorsResponseOut"])
    types["LatencyCriteriaIn"] = t.struct({"threshold": t.string().optional()}).named(
        renames["LatencyCriteriaIn"]
    )
    types["LatencyCriteriaOut"] = t.struct(
        {
            "threshold": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LatencyCriteriaOut"])
    types["GroupIn"] = t.struct(
        {
            "name": t.string().optional(),
            "parentName": t.string().optional(),
            "displayName": t.string().optional(),
            "isCluster": t.boolean().optional(),
            "filter": t.string().optional(),
        }
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "name": t.string().optional(),
            "parentName": t.string().optional(),
            "displayName": t.string().optional(),
            "isCluster": t.boolean().optional(),
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
    types["LogMatchIn"] = t.struct(
        {
            "filter": t.string(),
            "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LogMatchIn"])
    types["LogMatchOut"] = t.struct(
        {
            "filter": t.string(),
            "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogMatchOut"])
    types["MetricThresholdIn"] = t.struct(
        {
            "thresholdValue": t.number().optional(),
            "aggregations": t.array(t.proxy(renames["AggregationIn"])).optional(),
            "filter": t.string(),
            "comparison": t.string().optional(),
            "trigger": t.proxy(renames["TriggerIn"]).optional(),
            "denominatorAggregations": t.array(
                t.proxy(renames["AggregationIn"])
            ).optional(),
            "denominatorFilter": t.string().optional(),
            "forecastOptions": t.proxy(renames["ForecastOptionsIn"]).optional(),
            "evaluationMissingData": t.string().optional(),
            "duration": t.string().optional(),
        }
    ).named(renames["MetricThresholdIn"])
    types["MetricThresholdOut"] = t.struct(
        {
            "thresholdValue": t.number().optional(),
            "aggregations": t.array(t.proxy(renames["AggregationOut"])).optional(),
            "filter": t.string(),
            "comparison": t.string().optional(),
            "trigger": t.proxy(renames["TriggerOut"]).optional(),
            "denominatorAggregations": t.array(
                t.proxy(renames["AggregationOut"])
            ).optional(),
            "denominatorFilter": t.string().optional(),
            "forecastOptions": t.proxy(renames["ForecastOptionsOut"]).optional(),
            "evaluationMissingData": t.string().optional(),
            "duration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricThresholdOut"])
    types["MonitoredResourceDescriptorIn"] = t.struct(
        {
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])),
            "type": t.string(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "launchStage": t.string().optional(),
        }
    ).named(renames["MonitoredResourceDescriptorIn"])
    types["MonitoredResourceDescriptorOut"] = t.struct(
        {
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])),
            "type": t.string(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "launchStage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceDescriptorOut"])
    types["PointIn"] = t.struct(
        {
            "value": t.proxy(renames["TypedValueIn"]).optional(),
            "interval": t.proxy(renames["TimeIntervalIn"]).optional(),
        }
    ).named(renames["PointIn"])
    types["PointOut"] = t.struct(
        {
            "value": t.proxy(renames["TypedValueOut"]).optional(),
            "interval": t.proxy(renames["TimeIntervalOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PointOut"])
    types["ExponentialIn"] = t.struct(
        {
            "growthFactor": t.number().optional(),
            "numFiniteBuckets": t.integer().optional(),
            "scale": t.number().optional(),
        }
    ).named(renames["ExponentialIn"])
    types["ExponentialOut"] = t.struct(
        {
            "growthFactor": t.number().optional(),
            "numFiniteBuckets": t.integer().optional(),
            "scale": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExponentialOut"])
    types["CollectdValueIn"] = t.struct(
        {
            "dataSourceType": t.string().optional(),
            "dataSourceName": t.string().optional(),
            "value": t.proxy(renames["TypedValueIn"]).optional(),
        }
    ).named(renames["CollectdValueIn"])
    types["CollectdValueOut"] = t.struct(
        {
            "dataSourceType": t.string().optional(),
            "dataSourceName": t.string().optional(),
            "value": t.proxy(renames["TypedValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CollectdValueOut"])
    types["MeshIstioIn"] = t.struct(
        {
            "serviceNamespace": t.string().optional(),
            "serviceName": t.string().optional(),
            "meshUid": t.string().optional(),
        }
    ).named(renames["MeshIstioIn"])
    types["MeshIstioOut"] = t.struct(
        {
            "serviceNamespace": t.string().optional(),
            "serviceName": t.string().optional(),
            "meshUid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MeshIstioOut"])
    types["ClusterIstioIn"] = t.struct(
        {
            "serviceNamespace": t.string().optional(),
            "clusterName": t.string().optional(),
            "location": t.string().optional(),
            "serviceName": t.string().optional(),
        }
    ).named(renames["ClusterIstioIn"])
    types["ClusterIstioOut"] = t.struct(
        {
            "serviceNamespace": t.string().optional(),
            "clusterName": t.string().optional(),
            "location": t.string().optional(),
            "serviceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterIstioOut"])
    types["MutationRecordIn"] = t.struct(
        {"mutateTime": t.string().optional(), "mutatedBy": t.string().optional()}
    ).named(renames["MutationRecordIn"])
    types["MutationRecordOut"] = t.struct(
        {
            "mutateTime": t.string().optional(),
            "mutatedBy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MutationRecordOut"])
    types["AppEngineIn"] = t.struct({"moduleId": t.string().optional()}).named(
        renames["AppEngineIn"]
    )
    types["AppEngineOut"] = t.struct(
        {
            "moduleId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEngineOut"])
    types["TriggerIn"] = t.struct(
        {"count": t.integer().optional(), "percent": t.number().optional()}
    ).named(renames["TriggerIn"])
    types["TriggerOut"] = t.struct(
        {
            "count": t.integer().optional(),
            "percent": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TriggerOut"])
    types["DroppedLabelsIn"] = t.struct(
        {"label": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["DroppedLabelsIn"])
    types["DroppedLabelsOut"] = t.struct(
        {
            "label": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DroppedLabelsOut"])
    types["ListNotificationChannelsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "notificationChannels": t.array(
                t.proxy(renames["NotificationChannelIn"])
            ).optional(),
        }
    ).named(renames["ListNotificationChannelsResponseIn"])
    types["ListNotificationChannelsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "notificationChannels": t.array(
                t.proxy(renames["NotificationChannelOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNotificationChannelsResponseOut"])
    types["ErrorIn"] = t.struct(
        {
            "status": t.proxy(renames["StatusIn"]).optional(),
            "pointCount": t.integer().optional(),
        }
    ).named(renames["ErrorIn"])
    types["ErrorOut"] = t.struct(
        {
            "status": t.proxy(renames["StatusOut"]).optional(),
            "pointCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorOut"])
    types["GetNotificationChannelVerificationCodeRequestIn"] = t.struct(
        {"expireTime": t.string().optional()}
    ).named(renames["GetNotificationChannelVerificationCodeRequestIn"])
    types["GetNotificationChannelVerificationCodeRequestOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetNotificationChannelVerificationCodeRequestOut"])
    types["ServiceIn"] = t.struct(
        {
            "gkeWorkload": t.proxy(renames["GkeWorkloadIn"]).optional(),
            "clusterIstio": t.proxy(renames["ClusterIstioIn"]).optional(),
            "cloudEndpoints": t.proxy(renames["CloudEndpointsIn"]).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "appEngine": t.proxy(renames["AppEngineIn"]).optional(),
            "cloudRun": t.proxy(renames["CloudRunIn"]).optional(),
            "gkeNamespace": t.proxy(renames["GkeNamespaceIn"]).optional(),
            "meshIstio": t.proxy(renames["MeshIstioIn"]).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "istioCanonicalService": t.proxy(
                renames["IstioCanonicalServiceIn"]
            ).optional(),
            "gkeService": t.proxy(renames["GkeServiceIn"]).optional(),
            "basicService": t.proxy(renames["BasicServiceIn"]).optional(),
            "telemetry": t.proxy(renames["TelemetryIn"]).optional(),
            "custom": t.proxy(renames["CustomIn"]).optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "gkeWorkload": t.proxy(renames["GkeWorkloadOut"]).optional(),
            "clusterIstio": t.proxy(renames["ClusterIstioOut"]).optional(),
            "cloudEndpoints": t.proxy(renames["CloudEndpointsOut"]).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "appEngine": t.proxy(renames["AppEngineOut"]).optional(),
            "cloudRun": t.proxy(renames["CloudRunOut"]).optional(),
            "gkeNamespace": t.proxy(renames["GkeNamespaceOut"]).optional(),
            "meshIstio": t.proxy(renames["MeshIstioOut"]).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "istioCanonicalService": t.proxy(
                renames["IstioCanonicalServiceOut"]
            ).optional(),
            "gkeService": t.proxy(renames["GkeServiceOut"]).optional(),
            "basicService": t.proxy(renames["BasicServiceOut"]).optional(),
            "telemetry": t.proxy(renames["TelemetryOut"]).optional(),
            "custom": t.proxy(renames["CustomOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
    types["ListServiceLevelObjectivesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "serviceLevelObjectives": t.array(
                t.proxy(renames["ServiceLevelObjectiveIn"])
            ).optional(),
        }
    ).named(renames["ListServiceLevelObjectivesResponseIn"])
    types["ListServiceLevelObjectivesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "serviceLevelObjectives": t.array(
                t.proxy(renames["ServiceLevelObjectiveOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServiceLevelObjectivesResponseOut"])
    types["CreateTimeSeriesRequestIn"] = t.struct(
        {"timeSeries": t.array(t.proxy(renames["TimeSeriesIn"]))}
    ).named(renames["CreateTimeSeriesRequestIn"])
    types["CreateTimeSeriesRequestOut"] = t.struct(
        {
            "timeSeries": t.array(t.proxy(renames["TimeSeriesOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateTimeSeriesRequestOut"])
    types["RequestBasedSliIn"] = t.struct(
        {
            "distributionCut": t.proxy(renames["DistributionCutIn"]).optional(),
            "goodTotalRatio": t.proxy(renames["TimeSeriesRatioIn"]).optional(),
        }
    ).named(renames["RequestBasedSliIn"])
    types["RequestBasedSliOut"] = t.struct(
        {
            "distributionCut": t.proxy(renames["DistributionCutOut"]).optional(),
            "goodTotalRatio": t.proxy(renames["TimeSeriesRatioOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestBasedSliOut"])
    types["ListAlertPoliciesResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "alertPolicies": t.array(t.proxy(renames["AlertPolicyIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAlertPoliciesResponseIn"])
    types["ListAlertPoliciesResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "alertPolicies": t.array(t.proxy(renames["AlertPolicyOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAlertPoliciesResponseOut"])
    types["ListUptimeCheckIpsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "uptimeCheckIps": t.array(t.proxy(renames["UptimeCheckIpIn"])).optional(),
        }
    ).named(renames["ListUptimeCheckIpsResponseIn"])
    types["ListUptimeCheckIpsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "uptimeCheckIps": t.array(t.proxy(renames["UptimeCheckIpOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUptimeCheckIpsResponseOut"])
    types["MetricDescriptorIn"] = t.struct(
        {
            "type": t.string().optional(),
            "unit": t.string().optional(),
            "metricKind": t.string().optional(),
            "valueType": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "description": t.string().optional(),
            "launchStage": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
        }
    ).named(renames["MetricDescriptorIn"])
    types["MetricDescriptorOut"] = t.struct(
        {
            "type": t.string().optional(),
            "unit": t.string().optional(),
            "metricKind": t.string().optional(),
            "valueType": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataOut"]).optional(),
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "description": t.string().optional(),
            "launchStage": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorOut"])
    types["ForecastOptionsIn"] = t.struct({"forecastHorizon": t.string()}).named(
        renames["ForecastOptionsIn"]
    )
    types["ForecastOptionsOut"] = t.struct(
        {
            "forecastHorizon": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ForecastOptionsOut"])
    types["AlertPolicyIn"] = t.struct(
        {
            "name": t.string(),
            "combiner": t.string().optional(),
            "creationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "enabled": t.boolean().optional(),
            "documentation": t.proxy(renames["DocumentationIn"]).optional(),
            "alertStrategy": t.proxy(renames["AlertStrategyIn"]).optional(),
            "conditions": t.array(t.proxy(renames["ConditionIn"])).optional(),
            "notificationChannels": t.array(t.string()).optional(),
            "validity": t.proxy(renames["StatusIn"]).optional(),
            "displayName": t.string().optional(),
            "mutationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
        }
    ).named(renames["AlertPolicyIn"])
    types["AlertPolicyOut"] = t.struct(
        {
            "name": t.string(),
            "combiner": t.string().optional(),
            "creationRecord": t.proxy(renames["MutationRecordOut"]).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "enabled": t.boolean().optional(),
            "documentation": t.proxy(renames["DocumentationOut"]).optional(),
            "alertStrategy": t.proxy(renames["AlertStrategyOut"]).optional(),
            "conditions": t.array(t.proxy(renames["ConditionOut"])).optional(),
            "notificationChannels": t.array(t.string()).optional(),
            "validity": t.proxy(renames["StatusOut"]).optional(),
            "displayName": t.string().optional(),
            "mutationRecord": t.proxy(renames["MutationRecordOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlertPolicyOut"])
    types["ListUptimeCheckConfigsResponseIn"] = t.struct(
        {
            "uptimeCheckConfigs": t.array(
                t.proxy(renames["UptimeCheckConfigIn"])
            ).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListUptimeCheckConfigsResponseIn"])
    types["ListUptimeCheckConfigsResponseOut"] = t.struct(
        {
            "uptimeCheckConfigs": t.array(
                t.proxy(renames["UptimeCheckConfigOut"])
            ).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUptimeCheckConfigsResponseOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["RangeIn"] = t.struct(
        {"max": t.number().optional(), "min": t.number().optional()}
    ).named(renames["RangeIn"])
    types["RangeOut"] = t.struct(
        {
            "max": t.number().optional(),
            "min": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RangeOut"])
    types["SourceContextIn"] = t.struct({"fileName": t.string().optional()}).named(
        renames["SourceContextIn"]
    )
    types["SourceContextOut"] = t.struct(
        {
            "fileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceContextOut"])
    types["BasicSliIn"] = t.struct(
        {
            "location": t.array(t.string()).optional(),
            "version": t.array(t.string()).optional(),
            "latency": t.proxy(renames["LatencyCriteriaIn"]).optional(),
            "method": t.array(t.string()).optional(),
            "availability": t.proxy(renames["AvailabilityCriteriaIn"]).optional(),
        }
    ).named(renames["BasicSliIn"])
    types["BasicSliOut"] = t.struct(
        {
            "location": t.array(t.string()).optional(),
            "version": t.array(t.string()).optional(),
            "latency": t.proxy(renames["LatencyCriteriaOut"]).optional(),
            "method": t.array(t.string()).optional(),
            "availability": t.proxy(renames["AvailabilityCriteriaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicSliOut"])
    types["MetricDescriptorMetadataIn"] = t.struct(
        {
            "samplePeriod": t.string().optional(),
            "launchStage": t.string().optional(),
            "ingestDelay": t.string().optional(),
        }
    ).named(renames["MetricDescriptorMetadataIn"])
    types["MetricDescriptorMetadataOut"] = t.struct(
        {
            "samplePeriod": t.string().optional(),
            "launchStage": t.string().optional(),
            "ingestDelay": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorMetadataOut"])
    types["SpanContextIn"] = t.struct({"spanName": t.string().optional()}).named(
        renames["SpanContextIn"]
    )
    types["SpanContextOut"] = t.struct(
        {
            "spanName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpanContextOut"])
    types["GkeNamespaceIn"] = t.struct(
        {
            "clusterName": t.string().optional(),
            "location": t.string().optional(),
            "namespaceName": t.string().optional(),
        }
    ).named(renames["GkeNamespaceIn"])
    types["GkeNamespaceOut"] = t.struct(
        {
            "clusterName": t.string().optional(),
            "location": t.string().optional(),
            "namespaceName": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeNamespaceOut"])
    types["ServiceLevelIndicatorIn"] = t.struct(
        {
            "windowsBased": t.proxy(renames["WindowsBasedSliIn"]).optional(),
            "basicSli": t.proxy(renames["BasicSliIn"]).optional(),
            "requestBased": t.proxy(renames["RequestBasedSliIn"]).optional(),
        }
    ).named(renames["ServiceLevelIndicatorIn"])
    types["ServiceLevelIndicatorOut"] = t.struct(
        {
            "windowsBased": t.proxy(renames["WindowsBasedSliOut"]).optional(),
            "basicSli": t.proxy(renames["BasicSliOut"]).optional(),
            "requestBased": t.proxy(renames["RequestBasedSliOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceLevelIndicatorOut"])
    types["CloudEndpointsIn"] = t.struct({"service": t.string().optional()}).named(
        renames["CloudEndpointsIn"]
    )
    types["CloudEndpointsOut"] = t.struct(
        {
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudEndpointsOut"])
    types["MetricRangeIn"] = t.struct(
        {
            "timeSeries": t.string().optional(),
            "range": t.proxy(renames["GoogleMonitoringV3RangeIn"]).optional(),
        }
    ).named(renames["MetricRangeIn"])
    types["MetricRangeOut"] = t.struct(
        {
            "timeSeries": t.string().optional(),
            "range": t.proxy(renames["GoogleMonitoringV3RangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricRangeOut"])
    types["MonitoringQueryLanguageConditionIn"] = t.struct(
        {
            "duration": t.string().optional(),
            "evaluationMissingData": t.string().optional(),
            "trigger": t.proxy(renames["TriggerIn"]).optional(),
            "query": t.string().optional(),
        }
    ).named(renames["MonitoringQueryLanguageConditionIn"])
    types["MonitoringQueryLanguageConditionOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "evaluationMissingData": t.string().optional(),
            "trigger": t.proxy(renames["TriggerOut"]).optional(),
            "query": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoringQueryLanguageConditionOut"])
    types["CollectdPayloadIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "plugin": t.string().optional(),
            "type": t.string().optional(),
            "startTime": t.string().optional(),
            "pluginInstance": t.string().optional(),
            "endTime": t.string().optional(),
            "typeInstance": t.string().optional(),
            "values": t.array(t.proxy(renames["CollectdValueIn"])).optional(),
        }
    ).named(renames["CollectdPayloadIn"])
    types["CollectdPayloadOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "plugin": t.string().optional(),
            "type": t.string().optional(),
            "startTime": t.string().optional(),
            "pluginInstance": t.string().optional(),
            "endTime": t.string().optional(),
            "typeInstance": t.string().optional(),
            "values": t.array(t.proxy(renames["CollectdValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CollectdPayloadOut"])
    types["CreateCollectdTimeSeriesRequestIn"] = t.struct(
        {
            "collectdVersion": t.string().optional(),
            "collectdPayloads": t.array(
                t.proxy(renames["CollectdPayloadIn"])
            ).optional(),
            "resource": t.proxy(renames["MonitoredResourceIn"]).optional(),
        }
    ).named(renames["CreateCollectdTimeSeriesRequestIn"])
    types["CreateCollectdTimeSeriesRequestOut"] = t.struct(
        {
            "collectdVersion": t.string().optional(),
            "collectdPayloads": t.array(
                t.proxy(renames["CollectdPayloadOut"])
            ).optional(),
            "resource": t.proxy(renames["MonitoredResourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateCollectdTimeSeriesRequestOut"])
    types["PointDataIn"] = t.struct(
        {
            "timeInterval": t.proxy(renames["TimeIntervalIn"]).optional(),
            "values": t.array(t.proxy(renames["TypedValueIn"])).optional(),
        }
    ).named(renames["PointDataIn"])
    types["PointDataOut"] = t.struct(
        {
            "timeInterval": t.proxy(renames["TimeIntervalOut"]).optional(),
            "values": t.array(t.proxy(renames["TypedValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PointDataOut"])
    types["AlertStrategyIn"] = t.struct(
        {
            "autoClose": t.string().optional(),
            "notificationRateLimit": t.proxy(renames["NotificationRateLimitIn"]),
            "notificationChannelStrategy": t.array(
                t.proxy(renames["NotificationChannelStrategyIn"])
            ).optional(),
        }
    ).named(renames["AlertStrategyIn"])
    types["AlertStrategyOut"] = t.struct(
        {
            "autoClose": t.string().optional(),
            "notificationRateLimit": t.proxy(renames["NotificationRateLimitOut"]),
            "notificationChannelStrategy": t.array(
                t.proxy(renames["NotificationChannelStrategyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlertStrategyOut"])
    types["TimeSeriesIn"] = t.struct(
        {
            "metricKind": t.string().optional(),
            "metric": t.proxy(renames["MetricIn"]).optional(),
            "metadata": t.proxy(renames["MonitoredResourceMetadataIn"]).optional(),
            "valueType": t.string().optional(),
            "points": t.array(t.proxy(renames["PointIn"])).optional(),
            "resource": t.proxy(renames["MonitoredResourceIn"]).optional(),
            "unit": t.string().optional(),
        }
    ).named(renames["TimeSeriesIn"])
    types["TimeSeriesOut"] = t.struct(
        {
            "metricKind": t.string().optional(),
            "metric": t.proxy(renames["MetricOut"]).optional(),
            "metadata": t.proxy(renames["MonitoredResourceMetadataOut"]).optional(),
            "valueType": t.string().optional(),
            "points": t.array(t.proxy(renames["PointOut"])).optional(),
            "resource": t.proxy(renames["MonitoredResourceOut"]).optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeSeriesOut"])
    types["BasicAuthenticationIn"] = t.struct(
        {"username": t.string().optional(), "password": t.string().optional()}
    ).named(renames["BasicAuthenticationIn"])
    types["BasicAuthenticationOut"] = t.struct(
        {
            "username": t.string().optional(),
            "password": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicAuthenticationOut"])
    types["WindowsBasedSliIn"] = t.struct(
        {
            "windowPeriod": t.string().optional(),
            "metricMeanInRange": t.proxy(renames["MetricRangeIn"]).optional(),
            "metricSumInRange": t.proxy(renames["MetricRangeIn"]).optional(),
            "goodTotalRatioThreshold": t.proxy(
                renames["PerformanceThresholdIn"]
            ).optional(),
            "goodBadMetricFilter": t.string().optional(),
        }
    ).named(renames["WindowsBasedSliIn"])
    types["WindowsBasedSliOut"] = t.struct(
        {
            "windowPeriod": t.string().optional(),
            "metricMeanInRange": t.proxy(renames["MetricRangeOut"]).optional(),
            "metricSumInRange": t.proxy(renames["MetricRangeOut"]).optional(),
            "goodTotalRatioThreshold": t.proxy(
                renames["PerformanceThresholdOut"]
            ).optional(),
            "goodBadMetricFilter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsBasedSliOut"])
    types["AggregationIn"] = t.struct(
        {
            "groupByFields": t.array(t.string()).optional(),
            "crossSeriesReducer": t.string().optional(),
            "alignmentPeriod": t.string().optional(),
            "perSeriesAligner": t.string().optional(),
        }
    ).named(renames["AggregationIn"])
    types["AggregationOut"] = t.struct(
        {
            "groupByFields": t.array(t.string()).optional(),
            "crossSeriesReducer": t.string().optional(),
            "alignmentPeriod": t.string().optional(),
            "perSeriesAligner": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationOut"])
    types["ListGroupMembersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "members": t.array(t.proxy(renames["MonitoredResourceIn"])).optional(),
        }
    ).named(renames["ListGroupMembersResponseIn"])
    types["ListGroupMembersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "members": t.array(t.proxy(renames["MonitoredResourceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGroupMembersResponseOut"])
    types["TimeSeriesRatioIn"] = t.struct(
        {
            "totalServiceFilter": t.string().optional(),
            "goodServiceFilter": t.string().optional(),
            "badServiceFilter": t.string().optional(),
        }
    ).named(renames["TimeSeriesRatioIn"])
    types["TimeSeriesRatioOut"] = t.struct(
        {
            "totalServiceFilter": t.string().optional(),
            "goodServiceFilter": t.string().optional(),
            "badServiceFilter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeSeriesRatioOut"])
    types["LabelValueIn"] = t.struct(
        {
            "stringValue": t.string().optional(),
            "int64Value": t.string().optional(),
            "boolValue": t.boolean().optional(),
        }
    ).named(renames["LabelValueIn"])
    types["LabelValueOut"] = t.struct(
        {
            "stringValue": t.string().optional(),
            "int64Value": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelValueOut"])
    types["UptimeCheckIpIn"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "region": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["UptimeCheckIpIn"])
    types["UptimeCheckIpOut"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "region": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UptimeCheckIpOut"])
    types["ValueDescriptorIn"] = t.struct(
        {
            "metricKind": t.string().optional(),
            "valueType": t.string().optional(),
            "key": t.string().optional(),
            "unit": t.string().optional(),
        }
    ).named(renames["ValueDescriptorIn"])
    types["ValueDescriptorOut"] = t.struct(
        {
            "metricKind": t.string().optional(),
            "valueType": t.string().optional(),
            "key": t.string().optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueDescriptorOut"])
    types["ContentMatcherIn"] = t.struct(
        {
            "jsonPathMatcher": t.proxy(renames["JsonPathMatcherIn"]).optional(),
            "matcher": t.string().optional(),
            "content": t.string().optional(),
        }
    ).named(renames["ContentMatcherIn"])
    types["ContentMatcherOut"] = t.struct(
        {
            "jsonPathMatcher": t.proxy(renames["JsonPathMatcherOut"]).optional(),
            "matcher": t.string().optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentMatcherOut"])
    types["BucketOptionsIn"] = t.struct(
        {
            "exponentialBuckets": t.proxy(renames["ExponentialIn"]).optional(),
            "explicitBuckets": t.proxy(renames["ExplicitIn"]).optional(),
            "linearBuckets": t.proxy(renames["LinearIn"]).optional(),
        }
    ).named(renames["BucketOptionsIn"])
    types["BucketOptionsOut"] = t.struct(
        {
            "exponentialBuckets": t.proxy(renames["ExponentialOut"]).optional(),
            "explicitBuckets": t.proxy(renames["ExplicitOut"]).optional(),
            "linearBuckets": t.proxy(renames["LinearOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BucketOptionsOut"])
    types["NotificationChannelDescriptorIn"] = t.struct(
        {
            "supportedTiers": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "launchStage": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["NotificationChannelDescriptorIn"])
    types["NotificationChannelDescriptorOut"] = t.struct(
        {
            "supportedTiers": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "launchStage": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationChannelDescriptorOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["IstioCanonicalServiceIn"] = t.struct(
        {
            "canonicalService": t.string().optional(),
            "canonicalServiceNamespace": t.string().optional(),
            "meshUid": t.string().optional(),
        }
    ).named(renames["IstioCanonicalServiceIn"])
    types["IstioCanonicalServiceOut"] = t.struct(
        {
            "canonicalService": t.string().optional(),
            "canonicalServiceNamespace": t.string().optional(),
            "meshUid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IstioCanonicalServiceOut"])
    types["ListMetricDescriptorsResponseIn"] = t.struct(
        {
            "metricDescriptors": t.array(
                t.proxy(renames["MetricDescriptorIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListMetricDescriptorsResponseIn"])
    types["ListMetricDescriptorsResponseOut"] = t.struct(
        {
            "metricDescriptors": t.array(
                t.proxy(renames["MetricDescriptorOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMetricDescriptorsResponseOut"])
    types["CreateCollectdTimeSeriesResponseIn"] = t.struct(
        {
            "payloadErrors": t.array(
                t.proxy(renames["CollectdPayloadErrorIn"])
            ).optional(),
            "summary": t.proxy(renames["CreateTimeSeriesSummaryIn"]).optional(),
        }
    ).named(renames["CreateCollectdTimeSeriesResponseIn"])
    types["CreateCollectdTimeSeriesResponseOut"] = t.struct(
        {
            "payloadErrors": t.array(
                t.proxy(renames["CollectdPayloadErrorOut"])
            ).optional(),
            "summary": t.proxy(renames["CreateTimeSeriesSummaryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateCollectdTimeSeriesResponseOut"])
    types["VerifyNotificationChannelRequestIn"] = t.struct({"code": t.string()}).named(
        renames["VerifyNotificationChannelRequestIn"]
    )
    types["VerifyNotificationChannelRequestOut"] = t.struct(
        {"code": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VerifyNotificationChannelRequestOut"])
    types["TelemetryIn"] = t.struct({"resourceName": t.string().optional()}).named(
        renames["TelemetryIn"]
    )
    types["TelemetryOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TelemetryOut"])
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
    types["ResourceGroupIn"] = t.struct(
        {"resourceType": t.string().optional(), "groupId": t.string().optional()}
    ).named(renames["ResourceGroupIn"])
    types["ResourceGroupOut"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "groupId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceGroupOut"])
    types["MetricIn"] = t.struct(
        {
            "type": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["MetricIn"])
    types["MetricOut"] = t.struct(
        {
            "type": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricOut"])

    functions = {}
    functions["projectsTimeSeriesCreate"] = monitoring.post(
        "v3/{name}/timeSeries:query",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryTimeSeriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTimeSeriesCreateService"] = monitoring.post(
        "v3/{name}/timeSeries:query",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryTimeSeriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTimeSeriesList"] = monitoring.post(
        "v3/{name}/timeSeries:query",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryTimeSeriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTimeSeriesQuery"] = monitoring.post(
        "v3/{name}/timeSeries:query",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryTimeSeriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelDescriptorsGet"] = monitoring.get(
        "v3/{name}/notificationChannelDescriptors",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNotificationChannelDescriptorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelDescriptorsList"] = monitoring.get(
        "v3/{name}/notificationChannelDescriptors",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNotificationChannelDescriptorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUptimeCheckConfigsGet"] = monitoring.post(
        "v3/{parent}/uptimeCheckConfigs",
        t.struct(
            {
                "parent": t.string(),
                "selectedRegions": t.array(t.string()).optional(),
                "checkerType": t.string().optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "contentMatchers": t.array(
                    t.proxy(renames["ContentMatcherIn"])
                ).optional(),
                "internalCheckers": t.array(
                    t.proxy(renames["InternalCheckerIn"])
                ).optional(),
                "period": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "monitoredResource": t.proxy(renames["MonitoredResourceIn"]).optional(),
                "httpCheck": t.proxy(renames["HttpCheckIn"]).optional(),
                "isInternal": t.boolean().optional(),
                "tcpCheck": t.proxy(renames["TcpCheckIn"]).optional(),
                "timeout": t.string().optional(),
                "resourceGroup": t.proxy(renames["ResourceGroupIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UptimeCheckConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUptimeCheckConfigsPatch"] = monitoring.post(
        "v3/{parent}/uptimeCheckConfigs",
        t.struct(
            {
                "parent": t.string(),
                "selectedRegions": t.array(t.string()).optional(),
                "checkerType": t.string().optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "contentMatchers": t.array(
                    t.proxy(renames["ContentMatcherIn"])
                ).optional(),
                "internalCheckers": t.array(
                    t.proxy(renames["InternalCheckerIn"])
                ).optional(),
                "period": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "monitoredResource": t.proxy(renames["MonitoredResourceIn"]).optional(),
                "httpCheck": t.proxy(renames["HttpCheckIn"]).optional(),
                "isInternal": t.boolean().optional(),
                "tcpCheck": t.proxy(renames["TcpCheckIn"]).optional(),
                "timeout": t.string().optional(),
                "resourceGroup": t.proxy(renames["ResourceGroupIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UptimeCheckConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUptimeCheckConfigsList"] = monitoring.post(
        "v3/{parent}/uptimeCheckConfigs",
        t.struct(
            {
                "parent": t.string(),
                "selectedRegions": t.array(t.string()).optional(),
                "checkerType": t.string().optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "contentMatchers": t.array(
                    t.proxy(renames["ContentMatcherIn"])
                ).optional(),
                "internalCheckers": t.array(
                    t.proxy(renames["InternalCheckerIn"])
                ).optional(),
                "period": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "monitoredResource": t.proxy(renames["MonitoredResourceIn"]).optional(),
                "httpCheck": t.proxy(renames["HttpCheckIn"]).optional(),
                "isInternal": t.boolean().optional(),
                "tcpCheck": t.proxy(renames["TcpCheckIn"]).optional(),
                "timeout": t.string().optional(),
                "resourceGroup": t.proxy(renames["ResourceGroupIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UptimeCheckConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUptimeCheckConfigsDelete"] = monitoring.post(
        "v3/{parent}/uptimeCheckConfigs",
        t.struct(
            {
                "parent": t.string(),
                "selectedRegions": t.array(t.string()).optional(),
                "checkerType": t.string().optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "contentMatchers": t.array(
                    t.proxy(renames["ContentMatcherIn"])
                ).optional(),
                "internalCheckers": t.array(
                    t.proxy(renames["InternalCheckerIn"])
                ).optional(),
                "period": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "monitoredResource": t.proxy(renames["MonitoredResourceIn"]).optional(),
                "httpCheck": t.proxy(renames["HttpCheckIn"]).optional(),
                "isInternal": t.boolean().optional(),
                "tcpCheck": t.proxy(renames["TcpCheckIn"]).optional(),
                "timeout": t.string().optional(),
                "resourceGroup": t.proxy(renames["ResourceGroupIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UptimeCheckConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUptimeCheckConfigsCreate"] = monitoring.post(
        "v3/{parent}/uptimeCheckConfigs",
        t.struct(
            {
                "parent": t.string(),
                "selectedRegions": t.array(t.string()).optional(),
                "checkerType": t.string().optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "contentMatchers": t.array(
                    t.proxy(renames["ContentMatcherIn"])
                ).optional(),
                "internalCheckers": t.array(
                    t.proxy(renames["InternalCheckerIn"])
                ).optional(),
                "period": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "monitoredResource": t.proxy(renames["MonitoredResourceIn"]).optional(),
                "httpCheck": t.proxy(renames["HttpCheckIn"]).optional(),
                "isInternal": t.boolean().optional(),
                "tcpCheck": t.proxy(renames["TcpCheckIn"]).optional(),
                "timeout": t.string().optional(),
                "resourceGroup": t.proxy(renames["ResourceGroupIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UptimeCheckConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMonitoredResourceDescriptorsList"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MonitoredResourceDescriptorOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMonitoredResourceDescriptorsGet"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MonitoredResourceDescriptorOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAlertPoliciesDelete"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "combiner": t.string().optional(),
                "creationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "enabled": t.boolean().optional(),
                "documentation": t.proxy(renames["DocumentationIn"]).optional(),
                "alertStrategy": t.proxy(renames["AlertStrategyIn"]).optional(),
                "conditions": t.array(t.proxy(renames["ConditionIn"])).optional(),
                "notificationChannels": t.array(t.string()).optional(),
                "validity": t.proxy(renames["StatusIn"]).optional(),
                "displayName": t.string().optional(),
                "mutationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AlertPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAlertPoliciesCreate"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "combiner": t.string().optional(),
                "creationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "enabled": t.boolean().optional(),
                "documentation": t.proxy(renames["DocumentationIn"]).optional(),
                "alertStrategy": t.proxy(renames["AlertStrategyIn"]).optional(),
                "conditions": t.array(t.proxy(renames["ConditionIn"])).optional(),
                "notificationChannels": t.array(t.string()).optional(),
                "validity": t.proxy(renames["StatusIn"]).optional(),
                "displayName": t.string().optional(),
                "mutationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AlertPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAlertPoliciesGet"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "combiner": t.string().optional(),
                "creationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "enabled": t.boolean().optional(),
                "documentation": t.proxy(renames["DocumentationIn"]).optional(),
                "alertStrategy": t.proxy(renames["AlertStrategyIn"]).optional(),
                "conditions": t.array(t.proxy(renames["ConditionIn"])).optional(),
                "notificationChannels": t.array(t.string()).optional(),
                "validity": t.proxy(renames["StatusIn"]).optional(),
                "displayName": t.string().optional(),
                "mutationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AlertPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAlertPoliciesList"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "combiner": t.string().optional(),
                "creationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "enabled": t.boolean().optional(),
                "documentation": t.proxy(renames["DocumentationIn"]).optional(),
                "alertStrategy": t.proxy(renames["AlertStrategyIn"]).optional(),
                "conditions": t.array(t.proxy(renames["ConditionIn"])).optional(),
                "notificationChannels": t.array(t.string()).optional(),
                "validity": t.proxy(renames["StatusIn"]).optional(),
                "displayName": t.string().optional(),
                "mutationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AlertPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAlertPoliciesPatch"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "combiner": t.string().optional(),
                "creationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "enabled": t.boolean().optional(),
                "documentation": t.proxy(renames["DocumentationIn"]).optional(),
                "alertStrategy": t.proxy(renames["AlertStrategyIn"]).optional(),
                "conditions": t.array(t.proxy(renames["ConditionIn"])).optional(),
                "notificationChannels": t.array(t.string()).optional(),
                "validity": t.proxy(renames["StatusIn"]).optional(),
                "displayName": t.string().optional(),
                "mutationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AlertPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelsDelete"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NotificationChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelsSendVerificationCode"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NotificationChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelsVerify"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NotificationChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelsCreate"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NotificationChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelsList"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NotificationChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelsGetVerificationCode"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NotificationChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelsPatch"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NotificationChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelsGet"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NotificationChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsCollectdTimeSeriesCreate"] = monitoring.post(
        "v3/{name}/collectdTimeSeries",
        t.struct(
            {
                "name": t.string().optional(),
                "collectdVersion": t.string().optional(),
                "collectdPayloads": t.array(
                    t.proxy(renames["CollectdPayloadIn"])
                ).optional(),
                "resource": t.proxy(renames["MonitoredResourceIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreateCollectdTimeSeriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsDelete"] = monitoring.get(
        "v3/{name}/groups",
        t.struct(
            {
                "descendantsOfGroup": t.string().optional(),
                "ancestorsOfGroup": t.string().optional(),
                "pageSize": t.integer().optional(),
                "childrenOfGroup": t.string().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsCreate"] = monitoring.get(
        "v3/{name}/groups",
        t.struct(
            {
                "descendantsOfGroup": t.string().optional(),
                "ancestorsOfGroup": t.string().optional(),
                "pageSize": t.integer().optional(),
                "childrenOfGroup": t.string().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsUpdate"] = monitoring.get(
        "v3/{name}/groups",
        t.struct(
            {
                "descendantsOfGroup": t.string().optional(),
                "ancestorsOfGroup": t.string().optional(),
                "pageSize": t.integer().optional(),
                "childrenOfGroup": t.string().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsGet"] = monitoring.get(
        "v3/{name}/groups",
        t.struct(
            {
                "descendantsOfGroup": t.string().optional(),
                "ancestorsOfGroup": t.string().optional(),
                "pageSize": t.integer().optional(),
                "childrenOfGroup": t.string().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsList"] = monitoring.get(
        "v3/{name}/groups",
        t.struct(
            {
                "descendantsOfGroup": t.string().optional(),
                "ancestorsOfGroup": t.string().optional(),
                "pageSize": t.integer().optional(),
                "childrenOfGroup": t.string().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsMembersList"] = monitoring.get(
        "v3/{name}/members",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "interval.endTime": t.string(),
                "interval.startTime": t.string().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGroupMembersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnoozesGet"] = monitoring.get(
        "v3/{parent}/snoozes",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSnoozesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnoozesCreate"] = monitoring.get(
        "v3/{parent}/snoozes",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSnoozesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnoozesPatch"] = monitoring.get(
        "v3/{parent}/snoozes",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSnoozesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnoozesList"] = monitoring.get(
        "v3/{parent}/snoozes",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSnoozesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMetricDescriptorsCreate"] = monitoring.get(
        "v3/{name}/metricDescriptors",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMetricDescriptorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMetricDescriptorsDelete"] = monitoring.get(
        "v3/{name}/metricDescriptors",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMetricDescriptorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMetricDescriptorsGet"] = monitoring.get(
        "v3/{name}/metricDescriptors",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMetricDescriptorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMetricDescriptorsList"] = monitoring.get(
        "v3/{name}/metricDescriptors",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMetricDescriptorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesList"] = monitoring.post(
        "v3/{parent}/services",
        t.struct(
            {
                "serviceId": t.string().optional(),
                "parent": t.string(),
                "gkeWorkload": t.proxy(renames["GkeWorkloadIn"]).optional(),
                "clusterIstio": t.proxy(renames["ClusterIstioIn"]).optional(),
                "cloudEndpoints": t.proxy(renames["CloudEndpointsIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "appEngine": t.proxy(renames["AppEngineIn"]).optional(),
                "cloudRun": t.proxy(renames["CloudRunIn"]).optional(),
                "gkeNamespace": t.proxy(renames["GkeNamespaceIn"]).optional(),
                "meshIstio": t.proxy(renames["MeshIstioIn"]).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "istioCanonicalService": t.proxy(
                    renames["IstioCanonicalServiceIn"]
                ).optional(),
                "gkeService": t.proxy(renames["GkeServiceIn"]).optional(),
                "basicService": t.proxy(renames["BasicServiceIn"]).optional(),
                "telemetry": t.proxy(renames["TelemetryIn"]).optional(),
                "custom": t.proxy(renames["CustomIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesPatch"] = monitoring.post(
        "v3/{parent}/services",
        t.struct(
            {
                "serviceId": t.string().optional(),
                "parent": t.string(),
                "gkeWorkload": t.proxy(renames["GkeWorkloadIn"]).optional(),
                "clusterIstio": t.proxy(renames["ClusterIstioIn"]).optional(),
                "cloudEndpoints": t.proxy(renames["CloudEndpointsIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "appEngine": t.proxy(renames["AppEngineIn"]).optional(),
                "cloudRun": t.proxy(renames["CloudRunIn"]).optional(),
                "gkeNamespace": t.proxy(renames["GkeNamespaceIn"]).optional(),
                "meshIstio": t.proxy(renames["MeshIstioIn"]).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "istioCanonicalService": t.proxy(
                    renames["IstioCanonicalServiceIn"]
                ).optional(),
                "gkeService": t.proxy(renames["GkeServiceIn"]).optional(),
                "basicService": t.proxy(renames["BasicServiceIn"]).optional(),
                "telemetry": t.proxy(renames["TelemetryIn"]).optional(),
                "custom": t.proxy(renames["CustomIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesDelete"] = monitoring.post(
        "v3/{parent}/services",
        t.struct(
            {
                "serviceId": t.string().optional(),
                "parent": t.string(),
                "gkeWorkload": t.proxy(renames["GkeWorkloadIn"]).optional(),
                "clusterIstio": t.proxy(renames["ClusterIstioIn"]).optional(),
                "cloudEndpoints": t.proxy(renames["CloudEndpointsIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "appEngine": t.proxy(renames["AppEngineIn"]).optional(),
                "cloudRun": t.proxy(renames["CloudRunIn"]).optional(),
                "gkeNamespace": t.proxy(renames["GkeNamespaceIn"]).optional(),
                "meshIstio": t.proxy(renames["MeshIstioIn"]).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "istioCanonicalService": t.proxy(
                    renames["IstioCanonicalServiceIn"]
                ).optional(),
                "gkeService": t.proxy(renames["GkeServiceIn"]).optional(),
                "basicService": t.proxy(renames["BasicServiceIn"]).optional(),
                "telemetry": t.proxy(renames["TelemetryIn"]).optional(),
                "custom": t.proxy(renames["CustomIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesGet"] = monitoring.post(
        "v3/{parent}/services",
        t.struct(
            {
                "serviceId": t.string().optional(),
                "parent": t.string(),
                "gkeWorkload": t.proxy(renames["GkeWorkloadIn"]).optional(),
                "clusterIstio": t.proxy(renames["ClusterIstioIn"]).optional(),
                "cloudEndpoints": t.proxy(renames["CloudEndpointsIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "appEngine": t.proxy(renames["AppEngineIn"]).optional(),
                "cloudRun": t.proxy(renames["CloudRunIn"]).optional(),
                "gkeNamespace": t.proxy(renames["GkeNamespaceIn"]).optional(),
                "meshIstio": t.proxy(renames["MeshIstioIn"]).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "istioCanonicalService": t.proxy(
                    renames["IstioCanonicalServiceIn"]
                ).optional(),
                "gkeService": t.proxy(renames["GkeServiceIn"]).optional(),
                "basicService": t.proxy(renames["BasicServiceIn"]).optional(),
                "telemetry": t.proxy(renames["TelemetryIn"]).optional(),
                "custom": t.proxy(renames["CustomIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesCreate"] = monitoring.post(
        "v3/{parent}/services",
        t.struct(
            {
                "serviceId": t.string().optional(),
                "parent": t.string(),
                "gkeWorkload": t.proxy(renames["GkeWorkloadIn"]).optional(),
                "clusterIstio": t.proxy(renames["ClusterIstioIn"]).optional(),
                "cloudEndpoints": t.proxy(renames["CloudEndpointsIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "appEngine": t.proxy(renames["AppEngineIn"]).optional(),
                "cloudRun": t.proxy(renames["CloudRunIn"]).optional(),
                "gkeNamespace": t.proxy(renames["GkeNamespaceIn"]).optional(),
                "meshIstio": t.proxy(renames["MeshIstioIn"]).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "istioCanonicalService": t.proxy(
                    renames["IstioCanonicalServiceIn"]
                ).optional(),
                "gkeService": t.proxy(renames["GkeServiceIn"]).optional(),
                "basicService": t.proxy(renames["BasicServiceIn"]).optional(),
                "telemetry": t.proxy(renames["TelemetryIn"]).optional(),
                "custom": t.proxy(renames["CustomIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesServiceLevelObjectivesPatch"] = monitoring.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesServiceLevelObjectivesList"] = monitoring.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesServiceLevelObjectivesGet"] = monitoring.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesServiceLevelObjectivesCreate"] = monitoring.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesServiceLevelObjectivesDelete"] = monitoring.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsTimeSeriesList"] = monitoring.get(
        "v3/{name}/timeSeries",
        t.struct(
            {
                "secondaryAggregation.groupByFields": t.string().optional(),
                "aggregation.alignmentPeriod": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string(),
                "aggregation.crossSeriesReducer": t.string().optional(),
                "pageSize": t.integer().optional(),
                "aggregation.perSeriesAligner": t.string().optional(),
                "pageToken": t.string().optional(),
                "secondaryAggregation.perSeriesAligner": t.string().optional(),
                "secondaryAggregation.crossSeriesReducer": t.string().optional(),
                "secondaryAggregation.alignmentPeriod": t.string().optional(),
                "interval.startTime": t.string().optional(),
                "view": t.string(),
                "name": t.string(),
                "interval.endTime": t.string(),
                "aggregation.groupByFields": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTimeSeriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["uptimeCheckIpsList"] = monitoring.get(
        "v3/uptimeCheckIps",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUptimeCheckIpsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersTimeSeriesList"] = monitoring.get(
        "v3/{name}/timeSeries",
        t.struct(
            {
                "aggregation.perSeriesAligner": t.string().optional(),
                "name": t.string(),
                "interval.endTime": t.string(),
                "aggregation.alignmentPeriod": t.string().optional(),
                "secondaryAggregation.crossSeriesReducer": t.string().optional(),
                "secondaryAggregation.groupByFields": t.string().optional(),
                "filter": t.string(),
                "orderBy": t.string().optional(),
                "secondaryAggregation.alignmentPeriod": t.string().optional(),
                "aggregation.crossSeriesReducer": t.string().optional(),
                "secondaryAggregation.perSeriesAligner": t.string().optional(),
                "pageSize": t.integer().optional(),
                "view": t.string(),
                "pageToken": t.string().optional(),
                "aggregation.groupByFields": t.string().optional(),
                "interval.startTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTimeSeriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="monitoring", renames=renames, types=types, functions=functions
    )
