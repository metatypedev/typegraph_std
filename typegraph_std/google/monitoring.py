from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_monitoring():
    monitoring = HTTPRuntime("https://monitoring.googleapis.com/")

    renames = {
        "ErrorResponse": "_monitoring_1_ErrorResponse",
        "SpanContextIn": "_monitoring_2_SpanContextIn",
        "SpanContextOut": "_monitoring_3_SpanContextOut",
        "MetricIn": "_monitoring_4_MetricIn",
        "MetricOut": "_monitoring_5_MetricOut",
        "AvailabilityCriteriaIn": "_monitoring_6_AvailabilityCriteriaIn",
        "AvailabilityCriteriaOut": "_monitoring_7_AvailabilityCriteriaOut",
        "ListNotificationChannelsResponseIn": "_monitoring_8_ListNotificationChannelsResponseIn",
        "ListNotificationChannelsResponseOut": "_monitoring_9_ListNotificationChannelsResponseOut",
        "GroupIn": "_monitoring_10_GroupIn",
        "GroupOut": "_monitoring_11_GroupOut",
        "ContentMatcherIn": "_monitoring_12_ContentMatcherIn",
        "ContentMatcherOut": "_monitoring_13_ContentMatcherOut",
        "LatencyCriteriaIn": "_monitoring_14_LatencyCriteriaIn",
        "LatencyCriteriaOut": "_monitoring_15_LatencyCriteriaOut",
        "JsonPathMatcherIn": "_monitoring_16_JsonPathMatcherIn",
        "JsonPathMatcherOut": "_monitoring_17_JsonPathMatcherOut",
        "SendNotificationChannelVerificationCodeRequestIn": "_monitoring_18_SendNotificationChannelVerificationCodeRequestIn",
        "SendNotificationChannelVerificationCodeRequestOut": "_monitoring_19_SendNotificationChannelVerificationCodeRequestOut",
        "ListNotificationChannelDescriptorsResponseIn": "_monitoring_20_ListNotificationChannelDescriptorsResponseIn",
        "ListNotificationChannelDescriptorsResponseOut": "_monitoring_21_ListNotificationChannelDescriptorsResponseOut",
        "ResponseStatusCodeIn": "_monitoring_22_ResponseStatusCodeIn",
        "ResponseStatusCodeOut": "_monitoring_23_ResponseStatusCodeOut",
        "TriggerIn": "_monitoring_24_TriggerIn",
        "TriggerOut": "_monitoring_25_TriggerOut",
        "ValueDescriptorIn": "_monitoring_26_ValueDescriptorIn",
        "ValueDescriptorOut": "_monitoring_27_ValueDescriptorOut",
        "ErrorIn": "_monitoring_28_ErrorIn",
        "ErrorOut": "_monitoring_29_ErrorOut",
        "LogMatchIn": "_monitoring_30_LogMatchIn",
        "LogMatchOut": "_monitoring_31_LogMatchOut",
        "ListServiceLevelObjectivesResponseIn": "_monitoring_32_ListServiceLevelObjectivesResponseIn",
        "ListServiceLevelObjectivesResponseOut": "_monitoring_33_ListServiceLevelObjectivesResponseOut",
        "TimeSeriesIn": "_monitoring_34_TimeSeriesIn",
        "TimeSeriesOut": "_monitoring_35_TimeSeriesOut",
        "CreateTimeSeriesRequestIn": "_monitoring_36_CreateTimeSeriesRequestIn",
        "CreateTimeSeriesRequestOut": "_monitoring_37_CreateTimeSeriesRequestOut",
        "ListUptimeCheckConfigsResponseIn": "_monitoring_38_ListUptimeCheckConfigsResponseIn",
        "ListUptimeCheckConfigsResponseOut": "_monitoring_39_ListUptimeCheckConfigsResponseOut",
        "OptionIn": "_monitoring_40_OptionIn",
        "OptionOut": "_monitoring_41_OptionOut",
        "MonitoredResourceDescriptorIn": "_monitoring_42_MonitoredResourceDescriptorIn",
        "MonitoredResourceDescriptorOut": "_monitoring_43_MonitoredResourceDescriptorOut",
        "TypeIn": "_monitoring_44_TypeIn",
        "TypeOut": "_monitoring_45_TypeOut",
        "AlertPolicyIn": "_monitoring_46_AlertPolicyIn",
        "AlertPolicyOut": "_monitoring_47_AlertPolicyOut",
        "PingConfigIn": "_monitoring_48_PingConfigIn",
        "PingConfigOut": "_monitoring_49_PingConfigOut",
        "PointIn": "_monitoring_50_PointIn",
        "PointOut": "_monitoring_51_PointOut",
        "RangeIn": "_monitoring_52_RangeIn",
        "RangeOut": "_monitoring_53_RangeOut",
        "NotificationChannelStrategyIn": "_monitoring_54_NotificationChannelStrategyIn",
        "NotificationChannelStrategyOut": "_monitoring_55_NotificationChannelStrategyOut",
        "NotificationChannelIn": "_monitoring_56_NotificationChannelIn",
        "NotificationChannelOut": "_monitoring_57_NotificationChannelOut",
        "BasicServiceIn": "_monitoring_58_BasicServiceIn",
        "BasicServiceOut": "_monitoring_59_BasicServiceOut",
        "FieldIn": "_monitoring_60_FieldIn",
        "FieldOut": "_monitoring_61_FieldOut",
        "AlertStrategyIn": "_monitoring_62_AlertStrategyIn",
        "AlertStrategyOut": "_monitoring_63_AlertStrategyOut",
        "TimeSeriesDataIn": "_monitoring_64_TimeSeriesDataIn",
        "TimeSeriesDataOut": "_monitoring_65_TimeSeriesDataOut",
        "TypedValueIn": "_monitoring_66_TypedValueIn",
        "TypedValueOut": "_monitoring_67_TypedValueOut",
        "LabelDescriptorIn": "_monitoring_68_LabelDescriptorIn",
        "LabelDescriptorOut": "_monitoring_69_LabelDescriptorOut",
        "TimeIntervalIn": "_monitoring_70_TimeIntervalIn",
        "TimeIntervalOut": "_monitoring_71_TimeIntervalOut",
        "TimeSeriesDescriptorIn": "_monitoring_72_TimeSeriesDescriptorIn",
        "TimeSeriesDescriptorOut": "_monitoring_73_TimeSeriesDescriptorOut",
        "AppEngineIn": "_monitoring_74_AppEngineIn",
        "AppEngineOut": "_monitoring_75_AppEngineOut",
        "CreateCollectdTimeSeriesResponseIn": "_monitoring_76_CreateCollectdTimeSeriesResponseIn",
        "CreateCollectdTimeSeriesResponseOut": "_monitoring_77_CreateCollectdTimeSeriesResponseOut",
        "ListMetricDescriptorsResponseIn": "_monitoring_78_ListMetricDescriptorsResponseIn",
        "ListMetricDescriptorsResponseOut": "_monitoring_79_ListMetricDescriptorsResponseOut",
        "ServiceLevelObjectiveIn": "_monitoring_80_ServiceLevelObjectiveIn",
        "ServiceLevelObjectiveOut": "_monitoring_81_ServiceLevelObjectiveOut",
        "MonitoringQueryLanguageConditionIn": "_monitoring_82_MonitoringQueryLanguageConditionIn",
        "MonitoringQueryLanguageConditionOut": "_monitoring_83_MonitoringQueryLanguageConditionOut",
        "CollectdValueIn": "_monitoring_84_CollectdValueIn",
        "CollectdValueOut": "_monitoring_85_CollectdValueOut",
        "BucketOptionsIn": "_monitoring_86_BucketOptionsIn",
        "BucketOptionsOut": "_monitoring_87_BucketOptionsOut",
        "AggregationIn": "_monitoring_88_AggregationIn",
        "AggregationOut": "_monitoring_89_AggregationOut",
        "NotificationRateLimitIn": "_monitoring_90_NotificationRateLimitIn",
        "NotificationRateLimitOut": "_monitoring_91_NotificationRateLimitOut",
        "EmptyIn": "_monitoring_92_EmptyIn",
        "EmptyOut": "_monitoring_93_EmptyOut",
        "CollectdPayloadIn": "_monitoring_94_CollectdPayloadIn",
        "CollectdPayloadOut": "_monitoring_95_CollectdPayloadOut",
        "ListMonitoredResourceDescriptorsResponseIn": "_monitoring_96_ListMonitoredResourceDescriptorsResponseIn",
        "ListMonitoredResourceDescriptorsResponseOut": "_monitoring_97_ListMonitoredResourceDescriptorsResponseOut",
        "CreateTimeSeriesSummaryIn": "_monitoring_98_CreateTimeSeriesSummaryIn",
        "CreateTimeSeriesSummaryOut": "_monitoring_99_CreateTimeSeriesSummaryOut",
        "TelemetryIn": "_monitoring_100_TelemetryIn",
        "TelemetryOut": "_monitoring_101_TelemetryOut",
        "CollectdPayloadErrorIn": "_monitoring_102_CollectdPayloadErrorIn",
        "CollectdPayloadErrorOut": "_monitoring_103_CollectdPayloadErrorOut",
        "ClusterIstioIn": "_monitoring_104_ClusterIstioIn",
        "ClusterIstioOut": "_monitoring_105_ClusterIstioOut",
        "DistributionIn": "_monitoring_106_DistributionIn",
        "DistributionOut": "_monitoring_107_DistributionOut",
        "InternalCheckerIn": "_monitoring_108_InternalCheckerIn",
        "InternalCheckerOut": "_monitoring_109_InternalCheckerOut",
        "CloudEndpointsIn": "_monitoring_110_CloudEndpointsIn",
        "CloudEndpointsOut": "_monitoring_111_CloudEndpointsOut",
        "VerifyNotificationChannelRequestIn": "_monitoring_112_VerifyNotificationChannelRequestIn",
        "VerifyNotificationChannelRequestOut": "_monitoring_113_VerifyNotificationChannelRequestOut",
        "TcpCheckIn": "_monitoring_114_TcpCheckIn",
        "TcpCheckOut": "_monitoring_115_TcpCheckOut",
        "MonitoredResourceMetadataIn": "_monitoring_116_MonitoredResourceMetadataIn",
        "MonitoredResourceMetadataOut": "_monitoring_117_MonitoredResourceMetadataOut",
        "CriteriaIn": "_monitoring_118_CriteriaIn",
        "CriteriaOut": "_monitoring_119_CriteriaOut",
        "RequestBasedSliIn": "_monitoring_120_RequestBasedSliIn",
        "RequestBasedSliOut": "_monitoring_121_RequestBasedSliOut",
        "PointDataIn": "_monitoring_122_PointDataIn",
        "PointDataOut": "_monitoring_123_PointDataOut",
        "MetricRangeIn": "_monitoring_124_MetricRangeIn",
        "MetricRangeOut": "_monitoring_125_MetricRangeOut",
        "ExponentialIn": "_monitoring_126_ExponentialIn",
        "ExponentialOut": "_monitoring_127_ExponentialOut",
        "UptimeCheckConfigIn": "_monitoring_128_UptimeCheckConfigIn",
        "UptimeCheckConfigOut": "_monitoring_129_UptimeCheckConfigOut",
        "MeshIstioIn": "_monitoring_130_MeshIstioIn",
        "MeshIstioOut": "_monitoring_131_MeshIstioOut",
        "CollectdValueErrorIn": "_monitoring_132_CollectdValueErrorIn",
        "CollectdValueErrorOut": "_monitoring_133_CollectdValueErrorOut",
        "ListServicesResponseIn": "_monitoring_134_ListServicesResponseIn",
        "ListServicesResponseOut": "_monitoring_135_ListServicesResponseOut",
        "ListGroupsResponseIn": "_monitoring_136_ListGroupsResponseIn",
        "ListGroupsResponseOut": "_monitoring_137_ListGroupsResponseOut",
        "HttpCheckIn": "_monitoring_138_HttpCheckIn",
        "HttpCheckOut": "_monitoring_139_HttpCheckOut",
        "LinearIn": "_monitoring_140_LinearIn",
        "LinearOut": "_monitoring_141_LinearOut",
        "SnoozeIn": "_monitoring_142_SnoozeIn",
        "SnoozeOut": "_monitoring_143_SnoozeOut",
        "CloudRunIn": "_monitoring_144_CloudRunIn",
        "CloudRunOut": "_monitoring_145_CloudRunOut",
        "ServiceLevelIndicatorIn": "_monitoring_146_ServiceLevelIndicatorIn",
        "ServiceLevelIndicatorOut": "_monitoring_147_ServiceLevelIndicatorOut",
        "CustomIn": "_monitoring_148_CustomIn",
        "CustomOut": "_monitoring_149_CustomOut",
        "ForecastOptionsIn": "_monitoring_150_ForecastOptionsIn",
        "ForecastOptionsOut": "_monitoring_151_ForecastOptionsOut",
        "GetNotificationChannelVerificationCodeRequestIn": "_monitoring_152_GetNotificationChannelVerificationCodeRequestIn",
        "GetNotificationChannelVerificationCodeRequestOut": "_monitoring_153_GetNotificationChannelVerificationCodeRequestOut",
        "MetricDescriptorMetadataIn": "_monitoring_154_MetricDescriptorMetadataIn",
        "MetricDescriptorMetadataOut": "_monitoring_155_MetricDescriptorMetadataOut",
        "SourceContextIn": "_monitoring_156_SourceContextIn",
        "SourceContextOut": "_monitoring_157_SourceContextOut",
        "MetricDescriptorIn": "_monitoring_158_MetricDescriptorIn",
        "MetricDescriptorOut": "_monitoring_159_MetricDescriptorOut",
        "GoogleMonitoringV3RangeIn": "_monitoring_160_GoogleMonitoringV3RangeIn",
        "GoogleMonitoringV3RangeOut": "_monitoring_161_GoogleMonitoringV3RangeOut",
        "BasicSliIn": "_monitoring_162_BasicSliIn",
        "BasicSliOut": "_monitoring_163_BasicSliOut",
        "StatusIn": "_monitoring_164_StatusIn",
        "StatusOut": "_monitoring_165_StatusOut",
        "GetNotificationChannelVerificationCodeResponseIn": "_monitoring_166_GetNotificationChannelVerificationCodeResponseIn",
        "GetNotificationChannelVerificationCodeResponseOut": "_monitoring_167_GetNotificationChannelVerificationCodeResponseOut",
        "ListTimeSeriesResponseIn": "_monitoring_168_ListTimeSeriesResponseIn",
        "ListTimeSeriesResponseOut": "_monitoring_169_ListTimeSeriesResponseOut",
        "CreateCollectdTimeSeriesRequestIn": "_monitoring_170_CreateCollectdTimeSeriesRequestIn",
        "CreateCollectdTimeSeriesRequestOut": "_monitoring_171_CreateCollectdTimeSeriesRequestOut",
        "ExemplarIn": "_monitoring_172_ExemplarIn",
        "ExemplarOut": "_monitoring_173_ExemplarOut",
        "DistributionCutIn": "_monitoring_174_DistributionCutIn",
        "DistributionCutOut": "_monitoring_175_DistributionCutOut",
        "PerformanceThresholdIn": "_monitoring_176_PerformanceThresholdIn",
        "PerformanceThresholdOut": "_monitoring_177_PerformanceThresholdOut",
        "OperationMetadataIn": "_monitoring_178_OperationMetadataIn",
        "OperationMetadataOut": "_monitoring_179_OperationMetadataOut",
        "ResourceGroupIn": "_monitoring_180_ResourceGroupIn",
        "ResourceGroupOut": "_monitoring_181_ResourceGroupOut",
        "GkeServiceIn": "_monitoring_182_GkeServiceIn",
        "GkeServiceOut": "_monitoring_183_GkeServiceOut",
        "ExplicitIn": "_monitoring_184_ExplicitIn",
        "ExplicitOut": "_monitoring_185_ExplicitOut",
        "GkeWorkloadIn": "_monitoring_186_GkeWorkloadIn",
        "GkeWorkloadOut": "_monitoring_187_GkeWorkloadOut",
        "UptimeCheckIpIn": "_monitoring_188_UptimeCheckIpIn",
        "UptimeCheckIpOut": "_monitoring_189_UptimeCheckIpOut",
        "IstioCanonicalServiceIn": "_monitoring_190_IstioCanonicalServiceIn",
        "IstioCanonicalServiceOut": "_monitoring_191_IstioCanonicalServiceOut",
        "DroppedLabelsIn": "_monitoring_192_DroppedLabelsIn",
        "DroppedLabelsOut": "_monitoring_193_DroppedLabelsOut",
        "ListGroupMembersResponseIn": "_monitoring_194_ListGroupMembersResponseIn",
        "ListGroupMembersResponseOut": "_monitoring_195_ListGroupMembersResponseOut",
        "QueryTimeSeriesResponseIn": "_monitoring_196_QueryTimeSeriesResponseIn",
        "QueryTimeSeriesResponseOut": "_monitoring_197_QueryTimeSeriesResponseOut",
        "QueryTimeSeriesRequestIn": "_monitoring_198_QueryTimeSeriesRequestIn",
        "QueryTimeSeriesRequestOut": "_monitoring_199_QueryTimeSeriesRequestOut",
        "WindowsBasedSliIn": "_monitoring_200_WindowsBasedSliIn",
        "WindowsBasedSliOut": "_monitoring_201_WindowsBasedSliOut",
        "TimeSeriesRatioIn": "_monitoring_202_TimeSeriesRatioIn",
        "TimeSeriesRatioOut": "_monitoring_203_TimeSeriesRatioOut",
        "ListAlertPoliciesResponseIn": "_monitoring_204_ListAlertPoliciesResponseIn",
        "ListAlertPoliciesResponseOut": "_monitoring_205_ListAlertPoliciesResponseOut",
        "MonitoredResourceIn": "_monitoring_206_MonitoredResourceIn",
        "MonitoredResourceOut": "_monitoring_207_MonitoredResourceOut",
        "ConditionIn": "_monitoring_208_ConditionIn",
        "ConditionOut": "_monitoring_209_ConditionOut",
        "DocumentationIn": "_monitoring_210_DocumentationIn",
        "DocumentationOut": "_monitoring_211_DocumentationOut",
        "MetricAbsenceIn": "_monitoring_212_MetricAbsenceIn",
        "MetricAbsenceOut": "_monitoring_213_MetricAbsenceOut",
        "BasicAuthenticationIn": "_monitoring_214_BasicAuthenticationIn",
        "BasicAuthenticationOut": "_monitoring_215_BasicAuthenticationOut",
        "GkeNamespaceIn": "_monitoring_216_GkeNamespaceIn",
        "GkeNamespaceOut": "_monitoring_217_GkeNamespaceOut",
        "MutationRecordIn": "_monitoring_218_MutationRecordIn",
        "MutationRecordOut": "_monitoring_219_MutationRecordOut",
        "ListSnoozesResponseIn": "_monitoring_220_ListSnoozesResponseIn",
        "ListSnoozesResponseOut": "_monitoring_221_ListSnoozesResponseOut",
        "LabelValueIn": "_monitoring_222_LabelValueIn",
        "LabelValueOut": "_monitoring_223_LabelValueOut",
        "ListUptimeCheckIpsResponseIn": "_monitoring_224_ListUptimeCheckIpsResponseIn",
        "ListUptimeCheckIpsResponseOut": "_monitoring_225_ListUptimeCheckIpsResponseOut",
        "ServiceIn": "_monitoring_226_ServiceIn",
        "ServiceOut": "_monitoring_227_ServiceOut",
        "MetricThresholdIn": "_monitoring_228_MetricThresholdIn",
        "MetricThresholdOut": "_monitoring_229_MetricThresholdOut",
        "NotificationChannelDescriptorIn": "_monitoring_230_NotificationChannelDescriptorIn",
        "NotificationChannelDescriptorOut": "_monitoring_231_NotificationChannelDescriptorOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SpanContextIn"] = t.struct({"spanName": t.string().optional()}).named(
        renames["SpanContextIn"]
    )
    types["SpanContextOut"] = t.struct(
        {
            "spanName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpanContextOut"])
    types["MetricIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["MetricIn"])
    types["MetricOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricOut"])
    types["AvailabilityCriteriaIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AvailabilityCriteriaIn"]
    )
    types["AvailabilityCriteriaOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AvailabilityCriteriaOut"])
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
    types["GroupIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "parentName": t.string().optional(),
            "isCluster": t.boolean().optional(),
            "filter": t.string().optional(),
        }
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "parentName": t.string().optional(),
            "isCluster": t.boolean().optional(),
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
    types["ContentMatcherIn"] = t.struct(
        {
            "jsonPathMatcher": t.proxy(renames["JsonPathMatcherIn"]).optional(),
            "content": t.string().optional(),
            "matcher": t.string().optional(),
        }
    ).named(renames["ContentMatcherIn"])
    types["ContentMatcherOut"] = t.struct(
        {
            "jsonPathMatcher": t.proxy(renames["JsonPathMatcherOut"]).optional(),
            "content": t.string().optional(),
            "matcher": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentMatcherOut"])
    types["LatencyCriteriaIn"] = t.struct({"threshold": t.string().optional()}).named(
        renames["LatencyCriteriaIn"]
    )
    types["LatencyCriteriaOut"] = t.struct(
        {
            "threshold": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LatencyCriteriaOut"])
    types["JsonPathMatcherIn"] = t.struct(
        {"jsonMatcher": t.string().optional(), "jsonPath": t.string().optional()}
    ).named(renames["JsonPathMatcherIn"])
    types["JsonPathMatcherOut"] = t.struct(
        {
            "jsonMatcher": t.string().optional(),
            "jsonPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JsonPathMatcherOut"])
    types["SendNotificationChannelVerificationCodeRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SendNotificationChannelVerificationCodeRequestIn"])
    types["SendNotificationChannelVerificationCodeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SendNotificationChannelVerificationCodeRequestOut"])
    types["ListNotificationChannelDescriptorsResponseIn"] = t.struct(
        {
            "channelDescriptors": t.array(
                t.proxy(renames["NotificationChannelDescriptorIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListNotificationChannelDescriptorsResponseIn"])
    types["ListNotificationChannelDescriptorsResponseOut"] = t.struct(
        {
            "channelDescriptors": t.array(
                t.proxy(renames["NotificationChannelDescriptorOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNotificationChannelDescriptorsResponseOut"])
    types["ResponseStatusCodeIn"] = t.struct(
        {"statusClass": t.string().optional(), "statusValue": t.integer().optional()}
    ).named(renames["ResponseStatusCodeIn"])
    types["ResponseStatusCodeOut"] = t.struct(
        {
            "statusClass": t.string().optional(),
            "statusValue": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseStatusCodeOut"])
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
    types["ValueDescriptorIn"] = t.struct(
        {
            "unit": t.string().optional(),
            "metricKind": t.string().optional(),
            "key": t.string().optional(),
            "valueType": t.string().optional(),
        }
    ).named(renames["ValueDescriptorIn"])
    types["ValueDescriptorOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "metricKind": t.string().optional(),
            "key": t.string().optional(),
            "valueType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueDescriptorOut"])
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
    types["ListServiceLevelObjectivesResponseIn"] = t.struct(
        {
            "serviceLevelObjectives": t.array(
                t.proxy(renames["ServiceLevelObjectiveIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListServiceLevelObjectivesResponseIn"])
    types["ListServiceLevelObjectivesResponseOut"] = t.struct(
        {
            "serviceLevelObjectives": t.array(
                t.proxy(renames["ServiceLevelObjectiveOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServiceLevelObjectivesResponseOut"])
    types["TimeSeriesIn"] = t.struct(
        {
            "unit": t.string().optional(),
            "metricKind": t.string().optional(),
            "resource": t.proxy(renames["MonitoredResourceIn"]).optional(),
            "metric": t.proxy(renames["MetricIn"]).optional(),
            "valueType": t.string().optional(),
            "points": t.array(t.proxy(renames["PointIn"])).optional(),
            "metadata": t.proxy(renames["MonitoredResourceMetadataIn"]).optional(),
        }
    ).named(renames["TimeSeriesIn"])
    types["TimeSeriesOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "metricKind": t.string().optional(),
            "resource": t.proxy(renames["MonitoredResourceOut"]).optional(),
            "metric": t.proxy(renames["MetricOut"]).optional(),
            "valueType": t.string().optional(),
            "points": t.array(t.proxy(renames["PointOut"])).optional(),
            "metadata": t.proxy(renames["MonitoredResourceMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeSeriesOut"])
    types["CreateTimeSeriesRequestIn"] = t.struct(
        {"timeSeries": t.array(t.proxy(renames["TimeSeriesIn"]))}
    ).named(renames["CreateTimeSeriesRequestIn"])
    types["CreateTimeSeriesRequestOut"] = t.struct(
        {
            "timeSeries": t.array(t.proxy(renames["TimeSeriesOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateTimeSeriesRequestOut"])
    types["ListUptimeCheckConfigsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "uptimeCheckConfigs": t.array(
                t.proxy(renames["UptimeCheckConfigIn"])
            ).optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["ListUptimeCheckConfigsResponseIn"])
    types["ListUptimeCheckConfigsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "uptimeCheckConfigs": t.array(
                t.proxy(renames["UptimeCheckConfigOut"])
            ).optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUptimeCheckConfigsResponseOut"])
    types["OptionIn"] = t.struct(
        {
            "value": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OptionIn"])
    types["OptionOut"] = t.struct(
        {
            "value": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptionOut"])
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
    types["TypeIn"] = t.struct(
        {
            "edition": t.string().optional(),
            "syntax": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "name": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "oneofs": t.array(t.string()).optional(),
            "fields": t.array(t.proxy(renames["FieldIn"])).optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "edition": t.string().optional(),
            "syntax": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "name": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "oneofs": t.array(t.string()).optional(),
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
    types["AlertPolicyIn"] = t.struct(
        {
            "creationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
            "conditions": t.array(t.proxy(renames["ConditionIn"])).optional(),
            "mutationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
            "validity": t.proxy(renames["StatusIn"]).optional(),
            "alertStrategy": t.proxy(renames["AlertStrategyIn"]).optional(),
            "name": t.string(),
            "combiner": t.string().optional(),
            "enabled": t.boolean().optional(),
            "notificationChannels": t.array(t.string()).optional(),
            "documentation": t.proxy(renames["DocumentationIn"]).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["AlertPolicyIn"])
    types["AlertPolicyOut"] = t.struct(
        {
            "creationRecord": t.proxy(renames["MutationRecordOut"]).optional(),
            "conditions": t.array(t.proxy(renames["ConditionOut"])).optional(),
            "mutationRecord": t.proxy(renames["MutationRecordOut"]).optional(),
            "validity": t.proxy(renames["StatusOut"]).optional(),
            "alertStrategy": t.proxy(renames["AlertStrategyOut"]).optional(),
            "name": t.string(),
            "combiner": t.string().optional(),
            "enabled": t.boolean().optional(),
            "notificationChannels": t.array(t.string()).optional(),
            "documentation": t.proxy(renames["DocumentationOut"]).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlertPolicyOut"])
    types["PingConfigIn"] = t.struct({"pingsCount": t.integer().optional()}).named(
        renames["PingConfigIn"]
    )
    types["PingConfigOut"] = t.struct(
        {
            "pingsCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PingConfigOut"])
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
    types["RangeIn"] = t.struct(
        {"min": t.number().optional(), "max": t.number().optional()}
    ).named(renames["RangeIn"])
    types["RangeOut"] = t.struct(
        {
            "min": t.number().optional(),
            "max": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RangeOut"])
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
    types["NotificationChannelIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "creationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
            "mutationRecords": t.array(t.proxy(renames["MutationRecordIn"])).optional(),
            "enabled": t.boolean().optional(),
            "verificationStatus": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["NotificationChannelIn"])
    types["NotificationChannelOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "creationRecord": t.proxy(renames["MutationRecordOut"]).optional(),
            "mutationRecords": t.array(
                t.proxy(renames["MutationRecordOut"])
            ).optional(),
            "enabled": t.boolean().optional(),
            "verificationStatus": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationChannelOut"])
    types["BasicServiceIn"] = t.struct(
        {
            "serviceLabels": t.struct({"_": t.string().optional()}).optional(),
            "serviceType": t.string().optional(),
        }
    ).named(renames["BasicServiceIn"])
    types["BasicServiceOut"] = t.struct(
        {
            "serviceLabels": t.struct({"_": t.string().optional()}).optional(),
            "serviceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicServiceOut"])
    types["FieldIn"] = t.struct(
        {
            "jsonName": t.string().optional(),
            "oneofIndex": t.integer().optional(),
            "cardinality": t.string().optional(),
            "number": t.integer().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "defaultValue": t.string().optional(),
            "packed": t.boolean().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "typeUrl": t.string().optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "jsonName": t.string().optional(),
            "oneofIndex": t.integer().optional(),
            "cardinality": t.string().optional(),
            "number": t.integer().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "defaultValue": t.string().optional(),
            "packed": t.boolean().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "typeUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
    types["AlertStrategyIn"] = t.struct(
        {
            "autoClose": t.string().optional(),
            "notificationChannelStrategy": t.array(
                t.proxy(renames["NotificationChannelStrategyIn"])
            ).optional(),
            "notificationRateLimit": t.proxy(renames["NotificationRateLimitIn"]),
        }
    ).named(renames["AlertStrategyIn"])
    types["AlertStrategyOut"] = t.struct(
        {
            "autoClose": t.string().optional(),
            "notificationChannelStrategy": t.array(
                t.proxy(renames["NotificationChannelStrategyOut"])
            ).optional(),
            "notificationRateLimit": t.proxy(renames["NotificationRateLimitOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlertStrategyOut"])
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
    types["TypedValueIn"] = t.struct(
        {
            "int64Value": t.string().optional(),
            "stringValue": t.string().optional(),
            "doubleValue": t.number().optional(),
            "distributionValue": t.proxy(renames["DistributionIn"]).optional(),
            "boolValue": t.boolean().optional(),
        }
    ).named(renames["TypedValueIn"])
    types["TypedValueOut"] = t.struct(
        {
            "int64Value": t.string().optional(),
            "stringValue": t.string().optional(),
            "doubleValue": t.number().optional(),
            "distributionValue": t.proxy(renames["DistributionOut"]).optional(),
            "boolValue": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypedValueOut"])
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
    types["AppEngineIn"] = t.struct({"moduleId": t.string().optional()}).named(
        renames["AppEngineIn"]
    )
    types["AppEngineOut"] = t.struct(
        {
            "moduleId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEngineOut"])
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
    types["ListMetricDescriptorsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "metricDescriptors": t.array(
                t.proxy(renames["MetricDescriptorIn"])
            ).optional(),
        }
    ).named(renames["ListMetricDescriptorsResponseIn"])
    types["ListMetricDescriptorsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "metricDescriptors": t.array(
                t.proxy(renames["MetricDescriptorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMetricDescriptorsResponseOut"])
    types["ServiceLevelObjectiveIn"] = t.struct(
        {
            "name": t.string().optional(),
            "calendarPeriod": t.string().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "serviceLevelIndicator": t.proxy(
                renames["ServiceLevelIndicatorIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "goal": t.number().optional(),
            "rollingPeriod": t.string().optional(),
        }
    ).named(renames["ServiceLevelObjectiveIn"])
    types["ServiceLevelObjectiveOut"] = t.struct(
        {
            "name": t.string().optional(),
            "calendarPeriod": t.string().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "serviceLevelIndicator": t.proxy(
                renames["ServiceLevelIndicatorOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "goal": t.number().optional(),
            "rollingPeriod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceLevelObjectiveOut"])
    types["MonitoringQueryLanguageConditionIn"] = t.struct(
        {
            "trigger": t.proxy(renames["TriggerIn"]).optional(),
            "duration": t.string().optional(),
            "evaluationMissingData": t.string().optional(),
            "query": t.string().optional(),
        }
    ).named(renames["MonitoringQueryLanguageConditionIn"])
    types["MonitoringQueryLanguageConditionOut"] = t.struct(
        {
            "trigger": t.proxy(renames["TriggerOut"]).optional(),
            "duration": t.string().optional(),
            "evaluationMissingData": t.string().optional(),
            "query": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoringQueryLanguageConditionOut"])
    types["CollectdValueIn"] = t.struct(
        {
            "value": t.proxy(renames["TypedValueIn"]).optional(),
            "dataSourceType": t.string().optional(),
            "dataSourceName": t.string().optional(),
        }
    ).named(renames["CollectdValueIn"])
    types["CollectdValueOut"] = t.struct(
        {
            "value": t.proxy(renames["TypedValueOut"]).optional(),
            "dataSourceType": t.string().optional(),
            "dataSourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CollectdValueOut"])
    types["BucketOptionsIn"] = t.struct(
        {
            "linearBuckets": t.proxy(renames["LinearIn"]).optional(),
            "explicitBuckets": t.proxy(renames["ExplicitIn"]).optional(),
            "exponentialBuckets": t.proxy(renames["ExponentialIn"]).optional(),
        }
    ).named(renames["BucketOptionsIn"])
    types["BucketOptionsOut"] = t.struct(
        {
            "linearBuckets": t.proxy(renames["LinearOut"]).optional(),
            "explicitBuckets": t.proxy(renames["ExplicitOut"]).optional(),
            "exponentialBuckets": t.proxy(renames["ExponentialOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BucketOptionsOut"])
    types["AggregationIn"] = t.struct(
        {
            "crossSeriesReducer": t.string().optional(),
            "perSeriesAligner": t.string().optional(),
            "groupByFields": t.array(t.string()).optional(),
            "alignmentPeriod": t.string().optional(),
        }
    ).named(renames["AggregationIn"])
    types["AggregationOut"] = t.struct(
        {
            "crossSeriesReducer": t.string().optional(),
            "perSeriesAligner": t.string().optional(),
            "groupByFields": t.array(t.string()).optional(),
            "alignmentPeriod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationOut"])
    types["NotificationRateLimitIn"] = t.struct(
        {"period": t.string().optional()}
    ).named(renames["NotificationRateLimitIn"])
    types["NotificationRateLimitOut"] = t.struct(
        {
            "period": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationRateLimitOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["CollectdPayloadIn"] = t.struct(
        {
            "values": t.array(t.proxy(renames["CollectdValueIn"])).optional(),
            "pluginInstance": t.string().optional(),
            "plugin": t.string().optional(),
            "type": t.string().optional(),
            "startTime": t.string().optional(),
            "typeInstance": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["CollectdPayloadIn"])
    types["CollectdPayloadOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["CollectdValueOut"])).optional(),
            "pluginInstance": t.string().optional(),
            "plugin": t.string().optional(),
            "type": t.string().optional(),
            "startTime": t.string().optional(),
            "typeInstance": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CollectdPayloadOut"])
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
    types["CreateTimeSeriesSummaryIn"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["ErrorIn"])).optional(),
            "totalPointCount": t.integer().optional(),
            "successPointCount": t.integer().optional(),
        }
    ).named(renames["CreateTimeSeriesSummaryIn"])
    types["CreateTimeSeriesSummaryOut"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["ErrorOut"])).optional(),
            "totalPointCount": t.integer().optional(),
            "successPointCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateTimeSeriesSummaryOut"])
    types["TelemetryIn"] = t.struct({"resourceName": t.string().optional()}).named(
        renames["TelemetryIn"]
    )
    types["TelemetryOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TelemetryOut"])
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
    types["ClusterIstioIn"] = t.struct(
        {
            "serviceName": t.string().optional(),
            "clusterName": t.string().optional(),
            "serviceNamespace": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ClusterIstioIn"])
    types["ClusterIstioOut"] = t.struct(
        {
            "serviceName": t.string().optional(),
            "clusterName": t.string().optional(),
            "serviceNamespace": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterIstioOut"])
    types["DistributionIn"] = t.struct(
        {
            "exemplars": t.array(t.proxy(renames["ExemplarIn"])).optional(),
            "bucketCounts": t.array(t.string()),
            "bucketOptions": t.proxy(renames["BucketOptionsIn"]),
            "range": t.proxy(renames["RangeIn"]).optional(),
            "count": t.string().optional(),
            "sumOfSquaredDeviation": t.number().optional(),
            "mean": t.number().optional(),
        }
    ).named(renames["DistributionIn"])
    types["DistributionOut"] = t.struct(
        {
            "exemplars": t.array(t.proxy(renames["ExemplarOut"])).optional(),
            "bucketCounts": t.array(t.string()),
            "bucketOptions": t.proxy(renames["BucketOptionsOut"]),
            "range": t.proxy(renames["RangeOut"]).optional(),
            "count": t.string().optional(),
            "sumOfSquaredDeviation": t.number().optional(),
            "mean": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DistributionOut"])
    types["InternalCheckerIn"] = t.struct(
        {
            "state": t.string().optional(),
            "peerProjectId": t.string().optional(),
            "gcpZone": t.string().optional(),
            "network": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["InternalCheckerIn"])
    types["InternalCheckerOut"] = t.struct(
        {
            "state": t.string().optional(),
            "peerProjectId": t.string().optional(),
            "gcpZone": t.string().optional(),
            "network": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InternalCheckerOut"])
    types["CloudEndpointsIn"] = t.struct({"service": t.string().optional()}).named(
        renames["CloudEndpointsIn"]
    )
    types["CloudEndpointsOut"] = t.struct(
        {
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudEndpointsOut"])
    types["VerifyNotificationChannelRequestIn"] = t.struct({"code": t.string()}).named(
        renames["VerifyNotificationChannelRequestIn"]
    )
    types["VerifyNotificationChannelRequestOut"] = t.struct(
        {"code": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VerifyNotificationChannelRequestOut"])
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
    types["CriteriaIn"] = t.struct({"policies": t.array(t.string()).optional()}).named(
        renames["CriteriaIn"]
    )
    types["CriteriaOut"] = t.struct(
        {
            "policies": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CriteriaOut"])
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
    types["MetricRangeIn"] = t.struct(
        {
            "range": t.proxy(renames["GoogleMonitoringV3RangeIn"]).optional(),
            "timeSeries": t.string().optional(),
        }
    ).named(renames["MetricRangeIn"])
    types["MetricRangeOut"] = t.struct(
        {
            "range": t.proxy(renames["GoogleMonitoringV3RangeOut"]).optional(),
            "timeSeries": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricRangeOut"])
    types["ExponentialIn"] = t.struct(
        {
            "growthFactor": t.number().optional(),
            "scale": t.number().optional(),
            "numFiniteBuckets": t.integer().optional(),
        }
    ).named(renames["ExponentialIn"])
    types["ExponentialOut"] = t.struct(
        {
            "growthFactor": t.number().optional(),
            "scale": t.number().optional(),
            "numFiniteBuckets": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExponentialOut"])
    types["UptimeCheckConfigIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "httpCheck": t.proxy(renames["HttpCheckIn"]).optional(),
            "resourceGroup": t.proxy(renames["ResourceGroupIn"]).optional(),
            "internalCheckers": t.array(
                t.proxy(renames["InternalCheckerIn"])
            ).optional(),
            "period": t.string().optional(),
            "name": t.string().optional(),
            "monitoredResource": t.proxy(renames["MonitoredResourceIn"]).optional(),
            "contentMatchers": t.array(t.proxy(renames["ContentMatcherIn"])).optional(),
            "isInternal": t.boolean().optional(),
            "timeout": t.string().optional(),
            "selectedRegions": t.array(t.string()).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "checkerType": t.string().optional(),
            "tcpCheck": t.proxy(renames["TcpCheckIn"]).optional(),
        }
    ).named(renames["UptimeCheckConfigIn"])
    types["UptimeCheckConfigOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "httpCheck": t.proxy(renames["HttpCheckOut"]).optional(),
            "resourceGroup": t.proxy(renames["ResourceGroupOut"]).optional(),
            "internalCheckers": t.array(
                t.proxy(renames["InternalCheckerOut"])
            ).optional(),
            "period": t.string().optional(),
            "name": t.string().optional(),
            "monitoredResource": t.proxy(renames["MonitoredResourceOut"]).optional(),
            "contentMatchers": t.array(
                t.proxy(renames["ContentMatcherOut"])
            ).optional(),
            "isInternal": t.boolean().optional(),
            "timeout": t.string().optional(),
            "selectedRegions": t.array(t.string()).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "checkerType": t.string().optional(),
            "tcpCheck": t.proxy(renames["TcpCheckOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UptimeCheckConfigOut"])
    types["MeshIstioIn"] = t.struct(
        {
            "meshUid": t.string().optional(),
            "serviceNamespace": t.string().optional(),
            "serviceName": t.string().optional(),
        }
    ).named(renames["MeshIstioIn"])
    types["MeshIstioOut"] = t.struct(
        {
            "meshUid": t.string().optional(),
            "serviceNamespace": t.string().optional(),
            "serviceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MeshIstioOut"])
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
    types["HttpCheckIn"] = t.struct(
        {
            "port": t.integer().optional(),
            "authInfo": t.proxy(renames["BasicAuthenticationIn"]).optional(),
            "path": t.string().optional(),
            "body": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "useSsl": t.boolean().optional(),
            "acceptedResponseStatusCodes": t.array(
                t.proxy(renames["ResponseStatusCodeIn"])
            ).optional(),
            "requestMethod": t.string().optional(),
            "validateSsl": t.boolean().optional(),
            "maskHeaders": t.boolean().optional(),
            "contentType": t.string().optional(),
            "customContentType": t.string().optional(),
            "pingConfig": t.proxy(renames["PingConfigIn"]).optional(),
        }
    ).named(renames["HttpCheckIn"])
    types["HttpCheckOut"] = t.struct(
        {
            "port": t.integer().optional(),
            "authInfo": t.proxy(renames["BasicAuthenticationOut"]).optional(),
            "path": t.string().optional(),
            "body": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "useSsl": t.boolean().optional(),
            "acceptedResponseStatusCodes": t.array(
                t.proxy(renames["ResponseStatusCodeOut"])
            ).optional(),
            "requestMethod": t.string().optional(),
            "validateSsl": t.boolean().optional(),
            "maskHeaders": t.boolean().optional(),
            "contentType": t.string().optional(),
            "customContentType": t.string().optional(),
            "pingConfig": t.proxy(renames["PingConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpCheckOut"])
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
    types["SnoozeIn"] = t.struct(
        {
            "displayName": t.string(),
            "interval": t.proxy(renames["TimeIntervalIn"]),
            "criteria": t.proxy(renames["CriteriaIn"]),
            "name": t.string(),
        }
    ).named(renames["SnoozeIn"])
    types["SnoozeOut"] = t.struct(
        {
            "displayName": t.string(),
            "interval": t.proxy(renames["TimeIntervalOut"]),
            "criteria": t.proxy(renames["CriteriaOut"]),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnoozeOut"])
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
    types["ServiceLevelIndicatorIn"] = t.struct(
        {
            "requestBased": t.proxy(renames["RequestBasedSliIn"]).optional(),
            "basicSli": t.proxy(renames["BasicSliIn"]).optional(),
            "windowsBased": t.proxy(renames["WindowsBasedSliIn"]).optional(),
        }
    ).named(renames["ServiceLevelIndicatorIn"])
    types["ServiceLevelIndicatorOut"] = t.struct(
        {
            "requestBased": t.proxy(renames["RequestBasedSliOut"]).optional(),
            "basicSli": t.proxy(renames["BasicSliOut"]).optional(),
            "windowsBased": t.proxy(renames["WindowsBasedSliOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceLevelIndicatorOut"])
    types["CustomIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CustomIn"]
    )
    types["CustomOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CustomOut"])
    types["ForecastOptionsIn"] = t.struct({"forecastHorizon": t.string()}).named(
        renames["ForecastOptionsIn"]
    )
    types["ForecastOptionsOut"] = t.struct(
        {
            "forecastHorizon": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ForecastOptionsOut"])
    types["GetNotificationChannelVerificationCodeRequestIn"] = t.struct(
        {"expireTime": t.string().optional()}
    ).named(renames["GetNotificationChannelVerificationCodeRequestIn"])
    types["GetNotificationChannelVerificationCodeRequestOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetNotificationChannelVerificationCodeRequestOut"])
    types["MetricDescriptorMetadataIn"] = t.struct(
        {
            "samplePeriod": t.string().optional(),
            "ingestDelay": t.string().optional(),
            "launchStage": t.string().optional(),
        }
    ).named(renames["MetricDescriptorMetadataIn"])
    types["MetricDescriptorMetadataOut"] = t.struct(
        {
            "samplePeriod": t.string().optional(),
            "ingestDelay": t.string().optional(),
            "launchStage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorMetadataOut"])
    types["SourceContextIn"] = t.struct({"fileName": t.string().optional()}).named(
        renames["SourceContextIn"]
    )
    types["SourceContextOut"] = t.struct(
        {
            "fileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceContextOut"])
    types["MetricDescriptorIn"] = t.struct(
        {
            "name": t.string().optional(),
            "launchStage": t.string().optional(),
            "description": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "unit": t.string().optional(),
            "valueType": t.string().optional(),
            "metricKind": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "displayName": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
        }
    ).named(renames["MetricDescriptorIn"])
    types["MetricDescriptorOut"] = t.struct(
        {
            "name": t.string().optional(),
            "launchStage": t.string().optional(),
            "description": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "unit": t.string().optional(),
            "valueType": t.string().optional(),
            "metricKind": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "displayName": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorOut"])
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
    types["BasicSliIn"] = t.struct(
        {
            "latency": t.proxy(renames["LatencyCriteriaIn"]).optional(),
            "availability": t.proxy(renames["AvailabilityCriteriaIn"]).optional(),
            "method": t.array(t.string()).optional(),
            "location": t.array(t.string()).optional(),
            "version": t.array(t.string()).optional(),
        }
    ).named(renames["BasicSliIn"])
    types["BasicSliOut"] = t.struct(
        {
            "latency": t.proxy(renames["LatencyCriteriaOut"]).optional(),
            "availability": t.proxy(renames["AvailabilityCriteriaOut"]).optional(),
            "method": t.array(t.string()).optional(),
            "location": t.array(t.string()).optional(),
            "version": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicSliOut"])
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
    types["GetNotificationChannelVerificationCodeResponseIn"] = t.struct(
        {"code": t.string().optional(), "expireTime": t.string().optional()}
    ).named(renames["GetNotificationChannelVerificationCodeResponseIn"])
    types["GetNotificationChannelVerificationCodeResponseOut"] = t.struct(
        {
            "code": t.string().optional(),
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetNotificationChannelVerificationCodeResponseOut"])
    types["ListTimeSeriesResponseIn"] = t.struct(
        {
            "unit": t.string().optional(),
            "timeSeries": t.array(t.proxy(renames["TimeSeriesIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "executionErrors": t.array(t.proxy(renames["StatusIn"])).optional(),
        }
    ).named(renames["ListTimeSeriesResponseIn"])
    types["ListTimeSeriesResponseOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "timeSeries": t.array(t.proxy(renames["TimeSeriesOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "executionErrors": t.array(t.proxy(renames["StatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTimeSeriesResponseOut"])
    types["CreateCollectdTimeSeriesRequestIn"] = t.struct(
        {
            "resource": t.proxy(renames["MonitoredResourceIn"]).optional(),
            "collectdVersion": t.string().optional(),
            "collectdPayloads": t.array(
                t.proxy(renames["CollectdPayloadIn"])
            ).optional(),
        }
    ).named(renames["CreateCollectdTimeSeriesRequestIn"])
    types["CreateCollectdTimeSeriesRequestOut"] = t.struct(
        {
            "resource": t.proxy(renames["MonitoredResourceOut"]).optional(),
            "collectdVersion": t.string().optional(),
            "collectdPayloads": t.array(
                t.proxy(renames["CollectdPayloadOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateCollectdTimeSeriesRequestOut"])
    types["ExemplarIn"] = t.struct(
        {
            "value": t.number().optional(),
            "timestamp": t.string().optional(),
            "attachments": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["ExemplarIn"])
    types["ExemplarOut"] = t.struct(
        {
            "value": t.number().optional(),
            "timestamp": t.string().optional(),
            "attachments": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExemplarOut"])
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
    types["PerformanceThresholdIn"] = t.struct(
        {
            "performance": t.proxy(renames["RequestBasedSliIn"]).optional(),
            "threshold": t.number().optional(),
            "basicSliPerformance": t.proxy(renames["BasicSliIn"]).optional(),
        }
    ).named(renames["PerformanceThresholdIn"])
    types["PerformanceThresholdOut"] = t.struct(
        {
            "performance": t.proxy(renames["RequestBasedSliOut"]).optional(),
            "threshold": t.number().optional(),
            "basicSliPerformance": t.proxy(renames["BasicSliOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerformanceThresholdOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["ResourceGroupIn"] = t.struct(
        {"groupId": t.string().optional(), "resourceType": t.string().optional()}
    ).named(renames["ResourceGroupIn"])
    types["ResourceGroupOut"] = t.struct(
        {
            "groupId": t.string().optional(),
            "resourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceGroupOut"])
    types["GkeServiceIn"] = t.struct(
        {
            "clusterName": t.string().optional(),
            "namespaceName": t.string().optional(),
            "location": t.string().optional(),
            "serviceName": t.string().optional(),
        }
    ).named(renames["GkeServiceIn"])
    types["GkeServiceOut"] = t.struct(
        {
            "clusterName": t.string().optional(),
            "namespaceName": t.string().optional(),
            "projectId": t.string().optional(),
            "location": t.string().optional(),
            "serviceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeServiceOut"])
    types["ExplicitIn"] = t.struct({"bounds": t.array(t.number()).optional()}).named(
        renames["ExplicitIn"]
    )
    types["ExplicitOut"] = t.struct(
        {
            "bounds": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExplicitOut"])
    types["GkeWorkloadIn"] = t.struct(
        {
            "topLevelControllerType": t.string().optional(),
            "namespaceName": t.string().optional(),
            "clusterName": t.string().optional(),
            "topLevelControllerName": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["GkeWorkloadIn"])
    types["GkeWorkloadOut"] = t.struct(
        {
            "topLevelControllerType": t.string().optional(),
            "namespaceName": t.string().optional(),
            "projectId": t.string().optional(),
            "clusterName": t.string().optional(),
            "topLevelControllerName": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeWorkloadOut"])
    types["UptimeCheckIpIn"] = t.struct(
        {
            "location": t.string().optional(),
            "region": t.string().optional(),
            "ipAddress": t.string().optional(),
        }
    ).named(renames["UptimeCheckIpIn"])
    types["UptimeCheckIpOut"] = t.struct(
        {
            "location": t.string().optional(),
            "region": t.string().optional(),
            "ipAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UptimeCheckIpOut"])
    types["IstioCanonicalServiceIn"] = t.struct(
        {
            "canonicalServiceNamespace": t.string().optional(),
            "canonicalService": t.string().optional(),
            "meshUid": t.string().optional(),
        }
    ).named(renames["IstioCanonicalServiceIn"])
    types["IstioCanonicalServiceOut"] = t.struct(
        {
            "canonicalServiceNamespace": t.string().optional(),
            "canonicalService": t.string().optional(),
            "meshUid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IstioCanonicalServiceOut"])
    types["DroppedLabelsIn"] = t.struct(
        {"label": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["DroppedLabelsIn"])
    types["DroppedLabelsOut"] = t.struct(
        {
            "label": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DroppedLabelsOut"])
    types["ListGroupMembersResponseIn"] = t.struct(
        {
            "members": t.array(t.proxy(renames["MonitoredResourceIn"])).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListGroupMembersResponseIn"])
    types["ListGroupMembersResponseOut"] = t.struct(
        {
            "members": t.array(t.proxy(renames["MonitoredResourceOut"])).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGroupMembersResponseOut"])
    types["QueryTimeSeriesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "timeSeriesData": t.array(t.proxy(renames["TimeSeriesDataIn"])).optional(),
            "partialErrors": t.array(t.proxy(renames["StatusIn"])).optional(),
            "timeSeriesDescriptor": t.proxy(
                renames["TimeSeriesDescriptorIn"]
            ).optional(),
        }
    ).named(renames["QueryTimeSeriesResponseIn"])
    types["QueryTimeSeriesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "timeSeriesData": t.array(t.proxy(renames["TimeSeriesDataOut"])).optional(),
            "partialErrors": t.array(t.proxy(renames["StatusOut"])).optional(),
            "timeSeriesDescriptor": t.proxy(
                renames["TimeSeriesDescriptorOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryTimeSeriesResponseOut"])
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
    types["WindowsBasedSliIn"] = t.struct(
        {
            "metricMeanInRange": t.proxy(renames["MetricRangeIn"]).optional(),
            "metricSumInRange": t.proxy(renames["MetricRangeIn"]).optional(),
            "goodTotalRatioThreshold": t.proxy(
                renames["PerformanceThresholdIn"]
            ).optional(),
            "windowPeriod": t.string().optional(),
            "goodBadMetricFilter": t.string().optional(),
        }
    ).named(renames["WindowsBasedSliIn"])
    types["WindowsBasedSliOut"] = t.struct(
        {
            "metricMeanInRange": t.proxy(renames["MetricRangeOut"]).optional(),
            "metricSumInRange": t.proxy(renames["MetricRangeOut"]).optional(),
            "goodTotalRatioThreshold": t.proxy(
                renames["PerformanceThresholdOut"]
            ).optional(),
            "windowPeriod": t.string().optional(),
            "goodBadMetricFilter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsBasedSliOut"])
    types["TimeSeriesRatioIn"] = t.struct(
        {
            "goodServiceFilter": t.string().optional(),
            "totalServiceFilter": t.string().optional(),
            "badServiceFilter": t.string().optional(),
        }
    ).named(renames["TimeSeriesRatioIn"])
    types["TimeSeriesRatioOut"] = t.struct(
        {
            "goodServiceFilter": t.string().optional(),
            "totalServiceFilter": t.string().optional(),
            "badServiceFilter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeSeriesRatioOut"])
    types["ListAlertPoliciesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "alertPolicies": t.array(t.proxy(renames["AlertPolicyIn"])).optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["ListAlertPoliciesResponseIn"])
    types["ListAlertPoliciesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "alertPolicies": t.array(t.proxy(renames["AlertPolicyOut"])).optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAlertPoliciesResponseOut"])
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
    types["ConditionIn"] = t.struct(
        {
            "conditionMatchedLog": t.proxy(renames["LogMatchIn"]).optional(),
            "displayName": t.string().optional(),
            "name": t.string(),
            "conditionThreshold": t.proxy(renames["MetricThresholdIn"]).optional(),
            "conditionMonitoringQueryLanguage": t.proxy(
                renames["MonitoringQueryLanguageConditionIn"]
            ).optional(),
            "conditionAbsent": t.proxy(renames["MetricAbsenceIn"]).optional(),
        }
    ).named(renames["ConditionIn"])
    types["ConditionOut"] = t.struct(
        {
            "conditionMatchedLog": t.proxy(renames["LogMatchOut"]).optional(),
            "displayName": t.string().optional(),
            "name": t.string(),
            "conditionThreshold": t.proxy(renames["MetricThresholdOut"]).optional(),
            "conditionMonitoringQueryLanguage": t.proxy(
                renames["MonitoringQueryLanguageConditionOut"]
            ).optional(),
            "conditionAbsent": t.proxy(renames["MetricAbsenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionOut"])
    types["DocumentationIn"] = t.struct(
        {"mimeType": t.string().optional(), "content": t.string().optional()}
    ).named(renames["DocumentationIn"])
    types["DocumentationOut"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationOut"])
    types["MetricAbsenceIn"] = t.struct(
        {
            "trigger": t.proxy(renames["TriggerIn"]).optional(),
            "aggregations": t.array(t.proxy(renames["AggregationIn"])).optional(),
            "filter": t.string(),
            "duration": t.string().optional(),
        }
    ).named(renames["MetricAbsenceIn"])
    types["MetricAbsenceOut"] = t.struct(
        {
            "trigger": t.proxy(renames["TriggerOut"]).optional(),
            "aggregations": t.array(t.proxy(renames["AggregationOut"])).optional(),
            "filter": t.string(),
            "duration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricAbsenceOut"])
    types["BasicAuthenticationIn"] = t.struct(
        {"password": t.string().optional(), "username": t.string().optional()}
    ).named(renames["BasicAuthenticationIn"])
    types["BasicAuthenticationOut"] = t.struct(
        {
            "password": t.string().optional(),
            "username": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicAuthenticationOut"])
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
            "projectId": t.string().optional(),
            "location": t.string().optional(),
            "namespaceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeNamespaceOut"])
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
    types["ListSnoozesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "snoozes": t.array(t.proxy(renames["SnoozeIn"])).optional(),
        }
    ).named(renames["ListSnoozesResponseIn"])
    types["ListSnoozesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "snoozes": t.array(t.proxy(renames["SnoozeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSnoozesResponseOut"])
    types["LabelValueIn"] = t.struct(
        {
            "boolValue": t.boolean().optional(),
            "int64Value": t.string().optional(),
            "stringValue": t.string().optional(),
        }
    ).named(renames["LabelValueIn"])
    types["LabelValueOut"] = t.struct(
        {
            "boolValue": t.boolean().optional(),
            "int64Value": t.string().optional(),
            "stringValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelValueOut"])
    types["ListUptimeCheckIpsResponseIn"] = t.struct(
        {
            "uptimeCheckIps": t.array(t.proxy(renames["UptimeCheckIpIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListUptimeCheckIpsResponseIn"])
    types["ListUptimeCheckIpsResponseOut"] = t.struct(
        {
            "uptimeCheckIps": t.array(t.proxy(renames["UptimeCheckIpOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUptimeCheckIpsResponseOut"])
    types["ServiceIn"] = t.struct(
        {
            "istioCanonicalService": t.proxy(
                renames["IstioCanonicalServiceIn"]
            ).optional(),
            "appEngine": t.proxy(renames["AppEngineIn"]).optional(),
            "gkeService": t.proxy(renames["GkeServiceIn"]).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "custom": t.proxy(renames["CustomIn"]).optional(),
            "clusterIstio": t.proxy(renames["ClusterIstioIn"]).optional(),
            "cloudRun": t.proxy(renames["CloudRunIn"]).optional(),
            "telemetry": t.proxy(renames["TelemetryIn"]).optional(),
            "meshIstio": t.proxy(renames["MeshIstioIn"]).optional(),
            "gkeNamespace": t.proxy(renames["GkeNamespaceIn"]).optional(),
            "displayName": t.string().optional(),
            "cloudEndpoints": t.proxy(renames["CloudEndpointsIn"]).optional(),
            "gkeWorkload": t.proxy(renames["GkeWorkloadIn"]).optional(),
            "name": t.string().optional(),
            "basicService": t.proxy(renames["BasicServiceIn"]).optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "istioCanonicalService": t.proxy(
                renames["IstioCanonicalServiceOut"]
            ).optional(),
            "appEngine": t.proxy(renames["AppEngineOut"]).optional(),
            "gkeService": t.proxy(renames["GkeServiceOut"]).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "custom": t.proxy(renames["CustomOut"]).optional(),
            "clusterIstio": t.proxy(renames["ClusterIstioOut"]).optional(),
            "cloudRun": t.proxy(renames["CloudRunOut"]).optional(),
            "telemetry": t.proxy(renames["TelemetryOut"]).optional(),
            "meshIstio": t.proxy(renames["MeshIstioOut"]).optional(),
            "gkeNamespace": t.proxy(renames["GkeNamespaceOut"]).optional(),
            "displayName": t.string().optional(),
            "cloudEndpoints": t.proxy(renames["CloudEndpointsOut"]).optional(),
            "gkeWorkload": t.proxy(renames["GkeWorkloadOut"]).optional(),
            "name": t.string().optional(),
            "basicService": t.proxy(renames["BasicServiceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
    types["MetricThresholdIn"] = t.struct(
        {
            "denominatorFilter": t.string().optional(),
            "aggregations": t.array(t.proxy(renames["AggregationIn"])).optional(),
            "denominatorAggregations": t.array(
                t.proxy(renames["AggregationIn"])
            ).optional(),
            "filter": t.string(),
            "trigger": t.proxy(renames["TriggerIn"]).optional(),
            "evaluationMissingData": t.string().optional(),
            "duration": t.string().optional(),
            "thresholdValue": t.number().optional(),
            "comparison": t.string().optional(),
            "forecastOptions": t.proxy(renames["ForecastOptionsIn"]).optional(),
        }
    ).named(renames["MetricThresholdIn"])
    types["MetricThresholdOut"] = t.struct(
        {
            "denominatorFilter": t.string().optional(),
            "aggregations": t.array(t.proxy(renames["AggregationOut"])).optional(),
            "denominatorAggregations": t.array(
                t.proxy(renames["AggregationOut"])
            ).optional(),
            "filter": t.string(),
            "trigger": t.proxy(renames["TriggerOut"]).optional(),
            "evaluationMissingData": t.string().optional(),
            "duration": t.string().optional(),
            "thresholdValue": t.number().optional(),
            "comparison": t.string().optional(),
            "forecastOptions": t.proxy(renames["ForecastOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricThresholdOut"])
    types["NotificationChannelDescriptorIn"] = t.struct(
        {
            "supportedTiers": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "launchStage": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
        }
    ).named(renames["NotificationChannelDescriptorIn"])
    types["NotificationChannelDescriptorOut"] = t.struct(
        {
            "supportedTiers": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "launchStage": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationChannelDescriptorOut"])

    functions = {}
    functions["projectsSnoozesList"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "displayName": t.string(),
                "interval": t.proxy(renames["TimeIntervalIn"]),
                "criteria": t.proxy(renames["CriteriaIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnoozeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnoozesCreate"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "displayName": t.string(),
                "interval": t.proxy(renames["TimeIntervalIn"]),
                "criteria": t.proxy(renames["CriteriaIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnoozeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnoozesGet"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "displayName": t.string(),
                "interval": t.proxy(renames["TimeIntervalIn"]),
                "criteria": t.proxy(renames["CriteriaIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnoozeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnoozesPatch"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "displayName": t.string(),
                "interval": t.proxy(renames["TimeIntervalIn"]),
                "criteria": t.proxy(renames["CriteriaIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnoozeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTimeSeriesQuery"] = monitoring.post(
        "v3/{name}/timeSeries:createService",
        t.struct(
            {
                "name": t.string(),
                "timeSeries": t.array(t.proxy(renames["TimeSeriesIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTimeSeriesList"] = monitoring.post(
        "v3/{name}/timeSeries:createService",
        t.struct(
            {
                "name": t.string(),
                "timeSeries": t.array(t.proxy(renames["TimeSeriesIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTimeSeriesCreate"] = monitoring.post(
        "v3/{name}/timeSeries:createService",
        t.struct(
            {
                "name": t.string(),
                "timeSeries": t.array(t.proxy(renames["TimeSeriesIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTimeSeriesCreateService"] = monitoring.post(
        "v3/{name}/timeSeries:createService",
        t.struct(
            {
                "name": t.string(),
                "timeSeries": t.array(t.proxy(renames["TimeSeriesIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsCollectdTimeSeriesCreate"] = monitoring.post(
        "v3/{name}/collectdTimeSeries",
        t.struct(
            {
                "name": t.string().optional(),
                "resource": t.proxy(renames["MonitoredResourceIn"]).optional(),
                "collectdVersion": t.string().optional(),
                "collectdPayloads": t.array(
                    t.proxy(renames["CollectdPayloadIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreateCollectdTimeSeriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMetricDescriptorsList"] = monitoring.post(
        "v3/{name}/metricDescriptors",
        t.struct(
            {
                "name": t.string().optional(),
                "launchStage": t.string().optional(),
                "description": t.string().optional(),
                "monitoredResourceTypes": t.array(t.string()).optional(),
                "type": t.string().optional(),
                "unit": t.string().optional(),
                "valueType": t.string().optional(),
                "metricKind": t.string().optional(),
                "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
                "displayName": t.string().optional(),
                "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MetricDescriptorOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMetricDescriptorsDelete"] = monitoring.post(
        "v3/{name}/metricDescriptors",
        t.struct(
            {
                "name": t.string().optional(),
                "launchStage": t.string().optional(),
                "description": t.string().optional(),
                "monitoredResourceTypes": t.array(t.string()).optional(),
                "type": t.string().optional(),
                "unit": t.string().optional(),
                "valueType": t.string().optional(),
                "metricKind": t.string().optional(),
                "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
                "displayName": t.string().optional(),
                "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MetricDescriptorOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMetricDescriptorsGet"] = monitoring.post(
        "v3/{name}/metricDescriptors",
        t.struct(
            {
                "name": t.string().optional(),
                "launchStage": t.string().optional(),
                "description": t.string().optional(),
                "monitoredResourceTypes": t.array(t.string()).optional(),
                "type": t.string().optional(),
                "unit": t.string().optional(),
                "valueType": t.string().optional(),
                "metricKind": t.string().optional(),
                "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
                "displayName": t.string().optional(),
                "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MetricDescriptorOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMetricDescriptorsCreate"] = monitoring.post(
        "v3/{name}/metricDescriptors",
        t.struct(
            {
                "name": t.string().optional(),
                "launchStage": t.string().optional(),
                "description": t.string().optional(),
                "monitoredResourceTypes": t.array(t.string()).optional(),
                "type": t.string().optional(),
                "unit": t.string().optional(),
                "valueType": t.string().optional(),
                "metricKind": t.string().optional(),
                "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
                "displayName": t.string().optional(),
                "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MetricDescriptorOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMonitoredResourceDescriptorsGet"] = monitoring.get(
        "v3/{name}/monitoredResourceDescriptors",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMonitoredResourceDescriptorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMonitoredResourceDescriptorsList"] = monitoring.get(
        "v3/{name}/monitoredResourceDescriptors",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMonitoredResourceDescriptorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelsList"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "type": t.string().optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "creationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "mutationRecords": t.array(
                    t.proxy(renames["MutationRecordIn"])
                ).optional(),
                "enabled": t.boolean().optional(),
                "verificationStatus": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NotificationChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelsVerify"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "type": t.string().optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "creationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "mutationRecords": t.array(
                    t.proxy(renames["MutationRecordIn"])
                ).optional(),
                "enabled": t.boolean().optional(),
                "verificationStatus": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NotificationChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelsDelete"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "type": t.string().optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "creationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "mutationRecords": t.array(
                    t.proxy(renames["MutationRecordIn"])
                ).optional(),
                "enabled": t.boolean().optional(),
                "verificationStatus": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NotificationChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelsCreate"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "type": t.string().optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "creationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "mutationRecords": t.array(
                    t.proxy(renames["MutationRecordIn"])
                ).optional(),
                "enabled": t.boolean().optional(),
                "verificationStatus": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NotificationChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelsSendVerificationCode"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "type": t.string().optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "creationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "mutationRecords": t.array(
                    t.proxy(renames["MutationRecordIn"])
                ).optional(),
                "enabled": t.boolean().optional(),
                "verificationStatus": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NotificationChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelsGet"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "type": t.string().optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "creationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "mutationRecords": t.array(
                    t.proxy(renames["MutationRecordIn"])
                ).optional(),
                "enabled": t.boolean().optional(),
                "verificationStatus": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NotificationChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelsGetVerificationCode"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "type": t.string().optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "creationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "mutationRecords": t.array(
                    t.proxy(renames["MutationRecordIn"])
                ).optional(),
                "enabled": t.boolean().optional(),
                "verificationStatus": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NotificationChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelsPatch"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "type": t.string().optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "creationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "mutationRecords": t.array(
                    t.proxy(renames["MutationRecordIn"])
                ).optional(),
                "enabled": t.boolean().optional(),
                "verificationStatus": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NotificationChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelDescriptorsList"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NotificationChannelDescriptorOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelDescriptorsGet"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NotificationChannelDescriptorOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUptimeCheckConfigsCreate"] = monitoring.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUptimeCheckConfigsList"] = monitoring.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUptimeCheckConfigsPatch"] = monitoring.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUptimeCheckConfigsGet"] = monitoring.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUptimeCheckConfigsDelete"] = monitoring.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAlertPoliciesDelete"] = monitoring.get(
        "v3/{name}/alertPolicies",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAlertPoliciesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAlertPoliciesGet"] = monitoring.get(
        "v3/{name}/alertPolicies",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAlertPoliciesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAlertPoliciesCreate"] = monitoring.get(
        "v3/{name}/alertPolicies",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAlertPoliciesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAlertPoliciesPatch"] = monitoring.get(
        "v3/{name}/alertPolicies",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAlertPoliciesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAlertPoliciesList"] = monitoring.get(
        "v3/{name}/alertPolicies",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAlertPoliciesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsDelete"] = monitoring.put(
        "v3/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "parentName": t.string().optional(),
                "isCluster": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsCreate"] = monitoring.put(
        "v3/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "parentName": t.string().optional(),
                "isCluster": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsGet"] = monitoring.put(
        "v3/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "parentName": t.string().optional(),
                "isCluster": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsList"] = monitoring.put(
        "v3/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "parentName": t.string().optional(),
                "isCluster": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsUpdate"] = monitoring.put(
        "v3/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "parentName": t.string().optional(),
                "isCluster": t.boolean().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsMembersList"] = monitoring.get(
        "v3/{name}/members",
        t.struct(
            {
                "name": t.string(),
                "pageSize": t.integer().optional(),
                "interval.startTime": t.string().optional(),
                "filter": t.string().optional(),
                "interval.endTime": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGroupMembersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesDelete"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesPatch"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesCreate"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesList"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesGet"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesServiceLevelObjectivesPatch"] = monitoring.get(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceLevelObjectiveOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesServiceLevelObjectivesCreate"] = monitoring.get(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceLevelObjectiveOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesServiceLevelObjectivesDelete"] = monitoring.get(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceLevelObjectiveOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesServiceLevelObjectivesList"] = monitoring.get(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceLevelObjectiveOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesServiceLevelObjectivesGet"] = monitoring.get(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceLevelObjectiveOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersTimeSeriesList"] = monitoring.get(
        "v3/{name}/timeSeries",
        t.struct(
            {
                "secondaryAggregation.groupByFields": t.string().optional(),
                "aggregation.crossSeriesReducer": t.string().optional(),
                "orderBy": t.string().optional(),
                "secondaryAggregation.alignmentPeriod": t.string().optional(),
                "aggregation.perSeriesAligner": t.string().optional(),
                "name": t.string(),
                "view": t.string(),
                "pageSize": t.integer().optional(),
                "aggregation.groupByFields": t.string().optional(),
                "secondaryAggregation.crossSeriesReducer": t.string().optional(),
                "filter": t.string(),
                "pageToken": t.string().optional(),
                "interval.startTime": t.string().optional(),
                "interval.endTime": t.string(),
                "secondaryAggregation.perSeriesAligner": t.string().optional(),
                "aggregation.alignmentPeriod": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTimeSeriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsTimeSeriesList"] = monitoring.get(
        "v3/{name}/timeSeries",
        t.struct(
            {
                "filter": t.string(),
                "aggregation.alignmentPeriod": t.string().optional(),
                "secondaryAggregation.alignmentPeriod": t.string().optional(),
                "interval.startTime": t.string().optional(),
                "pageToken": t.string().optional(),
                "aggregation.crossSeriesReducer": t.string().optional(),
                "orderBy": t.string().optional(),
                "aggregation.groupByFields": t.string().optional(),
                "secondaryAggregation.groupByFields": t.string().optional(),
                "secondaryAggregation.crossSeriesReducer": t.string().optional(),
                "secondaryAggregation.perSeriesAligner": t.string().optional(),
                "interval.endTime": t.string(),
                "pageSize": t.integer().optional(),
                "aggregation.perSeriesAligner": t.string().optional(),
                "name": t.string(),
                "view": t.string(),
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

    return Import(
        importer="monitoring",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
