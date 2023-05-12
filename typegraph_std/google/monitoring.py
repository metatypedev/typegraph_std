from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_monitoring() -> Import:
    monitoring = HTTPRuntime("https://monitoring.googleapis.com/")

    renames = {
        "ErrorResponse": "_monitoring_1_ErrorResponse",
        "CloudRunIn": "_monitoring_2_CloudRunIn",
        "CloudRunOut": "_monitoring_3_CloudRunOut",
        "VerifyNotificationChannelRequestIn": "_monitoring_4_VerifyNotificationChannelRequestIn",
        "VerifyNotificationChannelRequestOut": "_monitoring_5_VerifyNotificationChannelRequestOut",
        "GkeServiceIn": "_monitoring_6_GkeServiceIn",
        "GkeServiceOut": "_monitoring_7_GkeServiceOut",
        "QueryTimeSeriesResponseIn": "_monitoring_8_QueryTimeSeriesResponseIn",
        "QueryTimeSeriesResponseOut": "_monitoring_9_QueryTimeSeriesResponseOut",
        "UptimeCheckConfigIn": "_monitoring_10_UptimeCheckConfigIn",
        "UptimeCheckConfigOut": "_monitoring_11_UptimeCheckConfigOut",
        "MetricAbsenceIn": "_monitoring_12_MetricAbsenceIn",
        "MetricAbsenceOut": "_monitoring_13_MetricAbsenceOut",
        "ServiceLevelObjectiveIn": "_monitoring_14_ServiceLevelObjectiveIn",
        "ServiceLevelObjectiveOut": "_monitoring_15_ServiceLevelObjectiveOut",
        "MonitoredResourceIn": "_monitoring_16_MonitoredResourceIn",
        "MonitoredResourceOut": "_monitoring_17_MonitoredResourceOut",
        "CollectdValueIn": "_monitoring_18_CollectdValueIn",
        "CollectdValueOut": "_monitoring_19_CollectdValueOut",
        "ResponseStatusCodeIn": "_monitoring_20_ResponseStatusCodeIn",
        "ResponseStatusCodeOut": "_monitoring_21_ResponseStatusCodeOut",
        "ExemplarIn": "_monitoring_22_ExemplarIn",
        "ExemplarOut": "_monitoring_23_ExemplarOut",
        "CreateTimeSeriesRequestIn": "_monitoring_24_CreateTimeSeriesRequestIn",
        "CreateTimeSeriesRequestOut": "_monitoring_25_CreateTimeSeriesRequestOut",
        "ExponentialIn": "_monitoring_26_ExponentialIn",
        "ExponentialOut": "_monitoring_27_ExponentialOut",
        "AlertPolicyIn": "_monitoring_28_AlertPolicyIn",
        "AlertPolicyOut": "_monitoring_29_AlertPolicyOut",
        "NotificationChannelIn": "_monitoring_30_NotificationChannelIn",
        "NotificationChannelOut": "_monitoring_31_NotificationChannelOut",
        "LabelDescriptorIn": "_monitoring_32_LabelDescriptorIn",
        "LabelDescriptorOut": "_monitoring_33_LabelDescriptorOut",
        "ListGroupsResponseIn": "_monitoring_34_ListGroupsResponseIn",
        "ListGroupsResponseOut": "_monitoring_35_ListGroupsResponseOut",
        "TypedValueIn": "_monitoring_36_TypedValueIn",
        "TypedValueOut": "_monitoring_37_TypedValueOut",
        "InternalCheckerIn": "_monitoring_38_InternalCheckerIn",
        "InternalCheckerOut": "_monitoring_39_InternalCheckerOut",
        "MetricThresholdIn": "_monitoring_40_MetricThresholdIn",
        "MetricThresholdOut": "_monitoring_41_MetricThresholdOut",
        "CreateTimeSeriesSummaryIn": "_monitoring_42_CreateTimeSeriesSummaryIn",
        "CreateTimeSeriesSummaryOut": "_monitoring_43_CreateTimeSeriesSummaryOut",
        "MonitoredResourceMetadataIn": "_monitoring_44_MonitoredResourceMetadataIn",
        "MonitoredResourceMetadataOut": "_monitoring_45_MonitoredResourceMetadataOut",
        "ExplicitIn": "_monitoring_46_ExplicitIn",
        "ExplicitOut": "_monitoring_47_ExplicitOut",
        "IstioCanonicalServiceIn": "_monitoring_48_IstioCanonicalServiceIn",
        "IstioCanonicalServiceOut": "_monitoring_49_IstioCanonicalServiceOut",
        "AppEngineIn": "_monitoring_50_AppEngineIn",
        "AppEngineOut": "_monitoring_51_AppEngineOut",
        "ListGroupMembersResponseIn": "_monitoring_52_ListGroupMembersResponseIn",
        "ListGroupMembersResponseOut": "_monitoring_53_ListGroupMembersResponseOut",
        "JsonPathMatcherIn": "_monitoring_54_JsonPathMatcherIn",
        "JsonPathMatcherOut": "_monitoring_55_JsonPathMatcherOut",
        "MetricRangeIn": "_monitoring_56_MetricRangeIn",
        "MetricRangeOut": "_monitoring_57_MetricRangeOut",
        "WindowsBasedSliIn": "_monitoring_58_WindowsBasedSliIn",
        "WindowsBasedSliOut": "_monitoring_59_WindowsBasedSliOut",
        "ListUptimeCheckConfigsResponseIn": "_monitoring_60_ListUptimeCheckConfigsResponseIn",
        "ListUptimeCheckConfigsResponseOut": "_monitoring_61_ListUptimeCheckConfigsResponseOut",
        "ErrorIn": "_monitoring_62_ErrorIn",
        "ErrorOut": "_monitoring_63_ErrorOut",
        "MutationRecordIn": "_monitoring_64_MutationRecordIn",
        "MutationRecordOut": "_monitoring_65_MutationRecordOut",
        "ListNotificationChannelsResponseIn": "_monitoring_66_ListNotificationChannelsResponseIn",
        "ListNotificationChannelsResponseOut": "_monitoring_67_ListNotificationChannelsResponseOut",
        "ListMonitoredResourceDescriptorsResponseIn": "_monitoring_68_ListMonitoredResourceDescriptorsResponseIn",
        "ListMonitoredResourceDescriptorsResponseOut": "_monitoring_69_ListMonitoredResourceDescriptorsResponseOut",
        "AvailabilityCriteriaIn": "_monitoring_70_AvailabilityCriteriaIn",
        "AvailabilityCriteriaOut": "_monitoring_71_AvailabilityCriteriaOut",
        "QueryTimeSeriesRequestIn": "_monitoring_72_QueryTimeSeriesRequestIn",
        "QueryTimeSeriesRequestOut": "_monitoring_73_QueryTimeSeriesRequestOut",
        "CollectdPayloadIn": "_monitoring_74_CollectdPayloadIn",
        "CollectdPayloadOut": "_monitoring_75_CollectdPayloadOut",
        "ForecastOptionsIn": "_monitoring_76_ForecastOptionsIn",
        "ForecastOptionsOut": "_monitoring_77_ForecastOptionsOut",
        "MetricIn": "_monitoring_78_MetricIn",
        "MetricOut": "_monitoring_79_MetricOut",
        "MonitoringQueryLanguageConditionIn": "_monitoring_80_MonitoringQueryLanguageConditionIn",
        "MonitoringQueryLanguageConditionOut": "_monitoring_81_MonitoringQueryLanguageConditionOut",
        "PerformanceThresholdIn": "_monitoring_82_PerformanceThresholdIn",
        "PerformanceThresholdOut": "_monitoring_83_PerformanceThresholdOut",
        "ServiceIn": "_monitoring_84_ServiceIn",
        "ServiceOut": "_monitoring_85_ServiceOut",
        "ClusterIstioIn": "_monitoring_86_ClusterIstioIn",
        "ClusterIstioOut": "_monitoring_87_ClusterIstioOut",
        "CreateCollectdTimeSeriesRequestIn": "_monitoring_88_CreateCollectdTimeSeriesRequestIn",
        "CreateCollectdTimeSeriesRequestOut": "_monitoring_89_CreateCollectdTimeSeriesRequestOut",
        "ServiceLevelIndicatorIn": "_monitoring_90_ServiceLevelIndicatorIn",
        "ServiceLevelIndicatorOut": "_monitoring_91_ServiceLevelIndicatorOut",
        "CreateCollectdTimeSeriesResponseIn": "_monitoring_92_CreateCollectdTimeSeriesResponseIn",
        "CreateCollectdTimeSeriesResponseOut": "_monitoring_93_CreateCollectdTimeSeriesResponseOut",
        "GroupIn": "_monitoring_94_GroupIn",
        "GroupOut": "_monitoring_95_GroupOut",
        "CollectdValueErrorIn": "_monitoring_96_CollectdValueErrorIn",
        "CollectdValueErrorOut": "_monitoring_97_CollectdValueErrorOut",
        "ResourceGroupIn": "_monitoring_98_ResourceGroupIn",
        "ResourceGroupOut": "_monitoring_99_ResourceGroupOut",
        "LogMatchIn": "_monitoring_100_LogMatchIn",
        "LogMatchOut": "_monitoring_101_LogMatchOut",
        "DroppedLabelsIn": "_monitoring_102_DroppedLabelsIn",
        "DroppedLabelsOut": "_monitoring_103_DroppedLabelsOut",
        "HttpCheckIn": "_monitoring_104_HttpCheckIn",
        "HttpCheckOut": "_monitoring_105_HttpCheckOut",
        "ListServiceLevelObjectivesResponseIn": "_monitoring_106_ListServiceLevelObjectivesResponseIn",
        "ListServiceLevelObjectivesResponseOut": "_monitoring_107_ListServiceLevelObjectivesResponseOut",
        "LatencyCriteriaIn": "_monitoring_108_LatencyCriteriaIn",
        "LatencyCriteriaOut": "_monitoring_109_LatencyCriteriaOut",
        "BasicAuthenticationIn": "_monitoring_110_BasicAuthenticationIn",
        "BasicAuthenticationOut": "_monitoring_111_BasicAuthenticationOut",
        "DocumentationIn": "_monitoring_112_DocumentationIn",
        "DocumentationOut": "_monitoring_113_DocumentationOut",
        "DistributionIn": "_monitoring_114_DistributionIn",
        "DistributionOut": "_monitoring_115_DistributionOut",
        "PointDataIn": "_monitoring_116_PointDataIn",
        "PointDataOut": "_monitoring_117_PointDataOut",
        "ListUptimeCheckIpsResponseIn": "_monitoring_118_ListUptimeCheckIpsResponseIn",
        "ListUptimeCheckIpsResponseOut": "_monitoring_119_ListUptimeCheckIpsResponseOut",
        "SpanContextIn": "_monitoring_120_SpanContextIn",
        "SpanContextOut": "_monitoring_121_SpanContextOut",
        "NotificationRateLimitIn": "_monitoring_122_NotificationRateLimitIn",
        "NotificationRateLimitOut": "_monitoring_123_NotificationRateLimitOut",
        "ValueDescriptorIn": "_monitoring_124_ValueDescriptorIn",
        "ValueDescriptorOut": "_monitoring_125_ValueDescriptorOut",
        "ContentMatcherIn": "_monitoring_126_ContentMatcherIn",
        "ContentMatcherOut": "_monitoring_127_ContentMatcherOut",
        "MeshIstioIn": "_monitoring_128_MeshIstioIn",
        "MeshIstioOut": "_monitoring_129_MeshIstioOut",
        "TelemetryIn": "_monitoring_130_TelemetryIn",
        "TelemetryOut": "_monitoring_131_TelemetryOut",
        "NotificationChannelDescriptorIn": "_monitoring_132_NotificationChannelDescriptorIn",
        "NotificationChannelDescriptorOut": "_monitoring_133_NotificationChannelDescriptorOut",
        "SnoozeIn": "_monitoring_134_SnoozeIn",
        "SnoozeOut": "_monitoring_135_SnoozeOut",
        "CollectdPayloadErrorIn": "_monitoring_136_CollectdPayloadErrorIn",
        "CollectdPayloadErrorOut": "_monitoring_137_CollectdPayloadErrorOut",
        "UptimeCheckIpIn": "_monitoring_138_UptimeCheckIpIn",
        "UptimeCheckIpOut": "_monitoring_139_UptimeCheckIpOut",
        "MonitoredResourceDescriptorIn": "_monitoring_140_MonitoredResourceDescriptorIn",
        "MonitoredResourceDescriptorOut": "_monitoring_141_MonitoredResourceDescriptorOut",
        "BasicSliIn": "_monitoring_142_BasicSliIn",
        "BasicSliOut": "_monitoring_143_BasicSliOut",
        "LabelValueIn": "_monitoring_144_LabelValueIn",
        "LabelValueOut": "_monitoring_145_LabelValueOut",
        "SendNotificationChannelVerificationCodeRequestIn": "_monitoring_146_SendNotificationChannelVerificationCodeRequestIn",
        "SendNotificationChannelVerificationCodeRequestOut": "_monitoring_147_SendNotificationChannelVerificationCodeRequestOut",
        "AggregationIn": "_monitoring_148_AggregationIn",
        "AggregationOut": "_monitoring_149_AggregationOut",
        "StatusIn": "_monitoring_150_StatusIn",
        "StatusOut": "_monitoring_151_StatusOut",
        "TypeIn": "_monitoring_152_TypeIn",
        "TypeOut": "_monitoring_153_TypeOut",
        "ListTimeSeriesResponseIn": "_monitoring_154_ListTimeSeriesResponseIn",
        "ListTimeSeriesResponseOut": "_monitoring_155_ListTimeSeriesResponseOut",
        "NotificationChannelStrategyIn": "_monitoring_156_NotificationChannelStrategyIn",
        "NotificationChannelStrategyOut": "_monitoring_157_NotificationChannelStrategyOut",
        "TimeSeriesDataIn": "_monitoring_158_TimeSeriesDataIn",
        "TimeSeriesDataOut": "_monitoring_159_TimeSeriesDataOut",
        "OperationMetadataIn": "_monitoring_160_OperationMetadataIn",
        "OperationMetadataOut": "_monitoring_161_OperationMetadataOut",
        "RangeIn": "_monitoring_162_RangeIn",
        "RangeOut": "_monitoring_163_RangeOut",
        "CriteriaIn": "_monitoring_164_CriteriaIn",
        "CriteriaOut": "_monitoring_165_CriteriaOut",
        "MetricDescriptorIn": "_monitoring_166_MetricDescriptorIn",
        "MetricDescriptorOut": "_monitoring_167_MetricDescriptorOut",
        "TriggerIn": "_monitoring_168_TriggerIn",
        "TriggerOut": "_monitoring_169_TriggerOut",
        "ConditionIn": "_monitoring_170_ConditionIn",
        "ConditionOut": "_monitoring_171_ConditionOut",
        "RequestBasedSliIn": "_monitoring_172_RequestBasedSliIn",
        "RequestBasedSliOut": "_monitoring_173_RequestBasedSliOut",
        "ListServicesResponseIn": "_monitoring_174_ListServicesResponseIn",
        "ListServicesResponseOut": "_monitoring_175_ListServicesResponseOut",
        "GetNotificationChannelVerificationCodeResponseIn": "_monitoring_176_GetNotificationChannelVerificationCodeResponseIn",
        "GetNotificationChannelVerificationCodeResponseOut": "_monitoring_177_GetNotificationChannelVerificationCodeResponseOut",
        "GetNotificationChannelVerificationCodeRequestIn": "_monitoring_178_GetNotificationChannelVerificationCodeRequestIn",
        "GetNotificationChannelVerificationCodeRequestOut": "_monitoring_179_GetNotificationChannelVerificationCodeRequestOut",
        "LinearIn": "_monitoring_180_LinearIn",
        "LinearOut": "_monitoring_181_LinearOut",
        "CloudEndpointsIn": "_monitoring_182_CloudEndpointsIn",
        "CloudEndpointsOut": "_monitoring_183_CloudEndpointsOut",
        "TimeSeriesRatioIn": "_monitoring_184_TimeSeriesRatioIn",
        "TimeSeriesRatioOut": "_monitoring_185_TimeSeriesRatioOut",
        "GkeNamespaceIn": "_monitoring_186_GkeNamespaceIn",
        "GkeNamespaceOut": "_monitoring_187_GkeNamespaceOut",
        "ListMetricDescriptorsResponseIn": "_monitoring_188_ListMetricDescriptorsResponseIn",
        "ListMetricDescriptorsResponseOut": "_monitoring_189_ListMetricDescriptorsResponseOut",
        "GkeWorkloadIn": "_monitoring_190_GkeWorkloadIn",
        "GkeWorkloadOut": "_monitoring_191_GkeWorkloadOut",
        "FieldIn": "_monitoring_192_FieldIn",
        "FieldOut": "_monitoring_193_FieldOut",
        "ListAlertPoliciesResponseIn": "_monitoring_194_ListAlertPoliciesResponseIn",
        "ListAlertPoliciesResponseOut": "_monitoring_195_ListAlertPoliciesResponseOut",
        "BucketOptionsIn": "_monitoring_196_BucketOptionsIn",
        "BucketOptionsOut": "_monitoring_197_BucketOptionsOut",
        "ListSnoozesResponseIn": "_monitoring_198_ListSnoozesResponseIn",
        "ListSnoozesResponseOut": "_monitoring_199_ListSnoozesResponseOut",
        "PingConfigIn": "_monitoring_200_PingConfigIn",
        "PingConfigOut": "_monitoring_201_PingConfigOut",
        "ListNotificationChannelDescriptorsResponseIn": "_monitoring_202_ListNotificationChannelDescriptorsResponseIn",
        "ListNotificationChannelDescriptorsResponseOut": "_monitoring_203_ListNotificationChannelDescriptorsResponseOut",
        "GoogleMonitoringV3RangeIn": "_monitoring_204_GoogleMonitoringV3RangeIn",
        "GoogleMonitoringV3RangeOut": "_monitoring_205_GoogleMonitoringV3RangeOut",
        "AlertStrategyIn": "_monitoring_206_AlertStrategyIn",
        "AlertStrategyOut": "_monitoring_207_AlertStrategyOut",
        "DistributionCutIn": "_monitoring_208_DistributionCutIn",
        "DistributionCutOut": "_monitoring_209_DistributionCutOut",
        "OptionIn": "_monitoring_210_OptionIn",
        "OptionOut": "_monitoring_211_OptionOut",
        "CustomIn": "_monitoring_212_CustomIn",
        "CustomOut": "_monitoring_213_CustomOut",
        "PointIn": "_monitoring_214_PointIn",
        "PointOut": "_monitoring_215_PointOut",
        "TcpCheckIn": "_monitoring_216_TcpCheckIn",
        "TcpCheckOut": "_monitoring_217_TcpCheckOut",
        "TimeSeriesIn": "_monitoring_218_TimeSeriesIn",
        "TimeSeriesOut": "_monitoring_219_TimeSeriesOut",
        "EmptyIn": "_monitoring_220_EmptyIn",
        "EmptyOut": "_monitoring_221_EmptyOut",
        "TimeSeriesDescriptorIn": "_monitoring_222_TimeSeriesDescriptorIn",
        "TimeSeriesDescriptorOut": "_monitoring_223_TimeSeriesDescriptorOut",
        "SourceContextIn": "_monitoring_224_SourceContextIn",
        "SourceContextOut": "_monitoring_225_SourceContextOut",
        "MetricDescriptorMetadataIn": "_monitoring_226_MetricDescriptorMetadataIn",
        "MetricDescriptorMetadataOut": "_monitoring_227_MetricDescriptorMetadataOut",
        "BasicServiceIn": "_monitoring_228_BasicServiceIn",
        "BasicServiceOut": "_monitoring_229_BasicServiceOut",
        "TimeIntervalIn": "_monitoring_230_TimeIntervalIn",
        "TimeIntervalOut": "_monitoring_231_TimeIntervalOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CloudRunIn"] = t.struct(
        {"serviceName": t.string().optional(), "location": t.string().optional()}
    ).named(renames["CloudRunIn"])
    types["CloudRunOut"] = t.struct(
        {
            "serviceName": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRunOut"])
    types["VerifyNotificationChannelRequestIn"] = t.struct({"code": t.string()}).named(
        renames["VerifyNotificationChannelRequestIn"]
    )
    types["VerifyNotificationChannelRequestOut"] = t.struct(
        {"code": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VerifyNotificationChannelRequestOut"])
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
            "projectId": t.string().optional(),
            "namespaceName": t.string().optional(),
            "clusterName": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeServiceOut"])
    types["QueryTimeSeriesResponseIn"] = t.struct(
        {
            "timeSeriesData": t.array(t.proxy(renames["TimeSeriesDataIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "timeSeriesDescriptor": t.proxy(
                renames["TimeSeriesDescriptorIn"]
            ).optional(),
            "partialErrors": t.array(t.proxy(renames["StatusIn"])).optional(),
        }
    ).named(renames["QueryTimeSeriesResponseIn"])
    types["QueryTimeSeriesResponseOut"] = t.struct(
        {
            "timeSeriesData": t.array(t.proxy(renames["TimeSeriesDataOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "timeSeriesDescriptor": t.proxy(
                renames["TimeSeriesDescriptorOut"]
            ).optional(),
            "partialErrors": t.array(t.proxy(renames["StatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryTimeSeriesResponseOut"])
    types["UptimeCheckConfigIn"] = t.struct(
        {
            "isInternal": t.boolean().optional(),
            "name": t.string().optional(),
            "tcpCheck": t.proxy(renames["TcpCheckIn"]).optional(),
            "httpCheck": t.proxy(renames["HttpCheckIn"]).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "period": t.string().optional(),
            "displayName": t.string().optional(),
            "checkerType": t.string().optional(),
            "internalCheckers": t.array(
                t.proxy(renames["InternalCheckerIn"])
            ).optional(),
            "contentMatchers": t.array(t.proxy(renames["ContentMatcherIn"])).optional(),
            "resourceGroup": t.proxy(renames["ResourceGroupIn"]).optional(),
            "timeout": t.string().optional(),
            "monitoredResource": t.proxy(renames["MonitoredResourceIn"]).optional(),
            "selectedRegions": t.array(t.string()).optional(),
        }
    ).named(renames["UptimeCheckConfigIn"])
    types["UptimeCheckConfigOut"] = t.struct(
        {
            "isInternal": t.boolean().optional(),
            "name": t.string().optional(),
            "tcpCheck": t.proxy(renames["TcpCheckOut"]).optional(),
            "httpCheck": t.proxy(renames["HttpCheckOut"]).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "period": t.string().optional(),
            "displayName": t.string().optional(),
            "checkerType": t.string().optional(),
            "internalCheckers": t.array(
                t.proxy(renames["InternalCheckerOut"])
            ).optional(),
            "contentMatchers": t.array(
                t.proxy(renames["ContentMatcherOut"])
            ).optional(),
            "resourceGroup": t.proxy(renames["ResourceGroupOut"]).optional(),
            "timeout": t.string().optional(),
            "monitoredResource": t.proxy(renames["MonitoredResourceOut"]).optional(),
            "selectedRegions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UptimeCheckConfigOut"])
    types["MetricAbsenceIn"] = t.struct(
        {
            "duration": t.string().optional(),
            "aggregations": t.array(t.proxy(renames["AggregationIn"])).optional(),
            "filter": t.string(),
            "trigger": t.proxy(renames["TriggerIn"]).optional(),
        }
    ).named(renames["MetricAbsenceIn"])
    types["MetricAbsenceOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "aggregations": t.array(t.proxy(renames["AggregationOut"])).optional(),
            "filter": t.string(),
            "trigger": t.proxy(renames["TriggerOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricAbsenceOut"])
    types["ServiceLevelObjectiveIn"] = t.struct(
        {
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "serviceLevelIndicator": t.proxy(
                renames["ServiceLevelIndicatorIn"]
            ).optional(),
            "goal": t.number().optional(),
            "calendarPeriod": t.string().optional(),
            "displayName": t.string().optional(),
            "rollingPeriod": t.string().optional(),
        }
    ).named(renames["ServiceLevelObjectiveIn"])
    types["ServiceLevelObjectiveOut"] = t.struct(
        {
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "serviceLevelIndicator": t.proxy(
                renames["ServiceLevelIndicatorOut"]
            ).optional(),
            "goal": t.number().optional(),
            "calendarPeriod": t.string().optional(),
            "displayName": t.string().optional(),
            "rollingPeriod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceLevelObjectiveOut"])
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
    types["CollectdValueIn"] = t.struct(
        {
            "dataSourceName": t.string().optional(),
            "dataSourceType": t.string().optional(),
            "value": t.proxy(renames["TypedValueIn"]).optional(),
        }
    ).named(renames["CollectdValueIn"])
    types["CollectdValueOut"] = t.struct(
        {
            "dataSourceName": t.string().optional(),
            "dataSourceType": t.string().optional(),
            "value": t.proxy(renames["TypedValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CollectdValueOut"])
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
    types["ExemplarIn"] = t.struct(
        {
            "value": t.number().optional(),
            "attachments": t.array(t.struct({"_": t.string().optional()})).optional(),
            "timestamp": t.string().optional(),
        }
    ).named(renames["ExemplarIn"])
    types["ExemplarOut"] = t.struct(
        {
            "value": t.number().optional(),
            "attachments": t.array(t.struct({"_": t.string().optional()})).optional(),
            "timestamp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExemplarOut"])
    types["CreateTimeSeriesRequestIn"] = t.struct(
        {"timeSeries": t.array(t.proxy(renames["TimeSeriesIn"]))}
    ).named(renames["CreateTimeSeriesRequestIn"])
    types["CreateTimeSeriesRequestOut"] = t.struct(
        {
            "timeSeries": t.array(t.proxy(renames["TimeSeriesOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateTimeSeriesRequestOut"])
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
    types["AlertPolicyIn"] = t.struct(
        {
            "combiner": t.string().optional(),
            "name": t.string(),
            "displayName": t.string().optional(),
            "creationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
            "documentation": t.proxy(renames["DocumentationIn"]).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "validity": t.proxy(renames["StatusIn"]).optional(),
            "notificationChannels": t.array(t.string()).optional(),
            "conditions": t.array(t.proxy(renames["ConditionIn"])).optional(),
            "enabled": t.boolean().optional(),
            "alertStrategy": t.proxy(renames["AlertStrategyIn"]).optional(),
            "mutationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
        }
    ).named(renames["AlertPolicyIn"])
    types["AlertPolicyOut"] = t.struct(
        {
            "combiner": t.string().optional(),
            "name": t.string(),
            "displayName": t.string().optional(),
            "creationRecord": t.proxy(renames["MutationRecordOut"]).optional(),
            "documentation": t.proxy(renames["DocumentationOut"]).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "validity": t.proxy(renames["StatusOut"]).optional(),
            "notificationChannels": t.array(t.string()).optional(),
            "conditions": t.array(t.proxy(renames["ConditionOut"])).optional(),
            "enabled": t.boolean().optional(),
            "alertStrategy": t.proxy(renames["AlertStrategyOut"]).optional(),
            "mutationRecord": t.proxy(renames["MutationRecordOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlertPolicyOut"])
    types["NotificationChannelIn"] = t.struct(
        {
            "type": t.string().optional(),
            "description": t.string().optional(),
            "mutationRecords": t.array(t.proxy(renames["MutationRecordIn"])).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "enabled": t.boolean().optional(),
            "creationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
            "name": t.string().optional(),
            "verificationStatus": t.string().optional(),
        }
    ).named(renames["NotificationChannelIn"])
    types["NotificationChannelOut"] = t.struct(
        {
            "type": t.string().optional(),
            "description": t.string().optional(),
            "mutationRecords": t.array(
                t.proxy(renames["MutationRecordOut"])
            ).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "enabled": t.boolean().optional(),
            "creationRecord": t.proxy(renames["MutationRecordOut"]).optional(),
            "name": t.string().optional(),
            "verificationStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationChannelOut"])
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
    types["ListGroupsResponseIn"] = t.struct(
        {
            "group": t.array(t.proxy(renames["GroupIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListGroupsResponseIn"])
    types["ListGroupsResponseOut"] = t.struct(
        {
            "group": t.array(t.proxy(renames["GroupOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGroupsResponseOut"])
    types["TypedValueIn"] = t.struct(
        {
            "boolValue": t.boolean().optional(),
            "distributionValue": t.proxy(renames["DistributionIn"]).optional(),
            "stringValue": t.string().optional(),
            "int64Value": t.string().optional(),
            "doubleValue": t.number().optional(),
        }
    ).named(renames["TypedValueIn"])
    types["TypedValueOut"] = t.struct(
        {
            "boolValue": t.boolean().optional(),
            "distributionValue": t.proxy(renames["DistributionOut"]).optional(),
            "stringValue": t.string().optional(),
            "int64Value": t.string().optional(),
            "doubleValue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypedValueOut"])
    types["InternalCheckerIn"] = t.struct(
        {
            "peerProjectId": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "network": t.string().optional(),
            "gcpZone": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["InternalCheckerIn"])
    types["InternalCheckerOut"] = t.struct(
        {
            "peerProjectId": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "network": t.string().optional(),
            "gcpZone": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InternalCheckerOut"])
    types["MetricThresholdIn"] = t.struct(
        {
            "aggregations": t.array(t.proxy(renames["AggregationIn"])).optional(),
            "denominatorAggregations": t.array(
                t.proxy(renames["AggregationIn"])
            ).optional(),
            "comparison": t.string().optional(),
            "thresholdValue": t.number().optional(),
            "trigger": t.proxy(renames["TriggerIn"]).optional(),
            "duration": t.string().optional(),
            "evaluationMissingData": t.string().optional(),
            "forecastOptions": t.proxy(renames["ForecastOptionsIn"]).optional(),
            "filter": t.string(),
            "denominatorFilter": t.string().optional(),
        }
    ).named(renames["MetricThresholdIn"])
    types["MetricThresholdOut"] = t.struct(
        {
            "aggregations": t.array(t.proxy(renames["AggregationOut"])).optional(),
            "denominatorAggregations": t.array(
                t.proxy(renames["AggregationOut"])
            ).optional(),
            "comparison": t.string().optional(),
            "thresholdValue": t.number().optional(),
            "trigger": t.proxy(renames["TriggerOut"]).optional(),
            "duration": t.string().optional(),
            "evaluationMissingData": t.string().optional(),
            "forecastOptions": t.proxy(renames["ForecastOptionsOut"]).optional(),
            "filter": t.string(),
            "denominatorFilter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricThresholdOut"])
    types["CreateTimeSeriesSummaryIn"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["ErrorIn"])).optional(),
            "successPointCount": t.integer().optional(),
            "totalPointCount": t.integer().optional(),
        }
    ).named(renames["CreateTimeSeriesSummaryIn"])
    types["CreateTimeSeriesSummaryOut"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["ErrorOut"])).optional(),
            "successPointCount": t.integer().optional(),
            "totalPointCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateTimeSeriesSummaryOut"])
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
    types["ExplicitIn"] = t.struct({"bounds": t.array(t.number()).optional()}).named(
        renames["ExplicitIn"]
    )
    types["ExplicitOut"] = t.struct(
        {
            "bounds": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExplicitOut"])
    types["IstioCanonicalServiceIn"] = t.struct(
        {
            "meshUid": t.string().optional(),
            "canonicalService": t.string().optional(),
            "canonicalServiceNamespace": t.string().optional(),
        }
    ).named(renames["IstioCanonicalServiceIn"])
    types["IstioCanonicalServiceOut"] = t.struct(
        {
            "meshUid": t.string().optional(),
            "canonicalService": t.string().optional(),
            "canonicalServiceNamespace": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IstioCanonicalServiceOut"])
    types["AppEngineIn"] = t.struct({"moduleId": t.string().optional()}).named(
        renames["AppEngineIn"]
    )
    types["AppEngineOut"] = t.struct(
        {
            "moduleId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEngineOut"])
    types["ListGroupMembersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "members": t.array(t.proxy(renames["MonitoredResourceIn"])).optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["ListGroupMembersResponseIn"])
    types["ListGroupMembersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "members": t.array(t.proxy(renames["MonitoredResourceOut"])).optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGroupMembersResponseOut"])
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
    types["WindowsBasedSliIn"] = t.struct(
        {
            "metricSumInRange": t.proxy(renames["MetricRangeIn"]).optional(),
            "goodBadMetricFilter": t.string().optional(),
            "windowPeriod": t.string().optional(),
            "goodTotalRatioThreshold": t.proxy(
                renames["PerformanceThresholdIn"]
            ).optional(),
            "metricMeanInRange": t.proxy(renames["MetricRangeIn"]).optional(),
        }
    ).named(renames["WindowsBasedSliIn"])
    types["WindowsBasedSliOut"] = t.struct(
        {
            "metricSumInRange": t.proxy(renames["MetricRangeOut"]).optional(),
            "goodBadMetricFilter": t.string().optional(),
            "windowPeriod": t.string().optional(),
            "goodTotalRatioThreshold": t.proxy(
                renames["PerformanceThresholdOut"]
            ).optional(),
            "metricMeanInRange": t.proxy(renames["MetricRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsBasedSliOut"])
    types["ListUptimeCheckConfigsResponseIn"] = t.struct(
        {
            "uptimeCheckConfigs": t.array(
                t.proxy(renames["UptimeCheckConfigIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["ListUptimeCheckConfigsResponseIn"])
    types["ListUptimeCheckConfigsResponseOut"] = t.struct(
        {
            "uptimeCheckConfigs": t.array(
                t.proxy(renames["UptimeCheckConfigOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUptimeCheckConfigsResponseOut"])
    types["ErrorIn"] = t.struct(
        {
            "pointCount": t.integer().optional(),
            "status": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["ErrorIn"])
    types["ErrorOut"] = t.struct(
        {
            "pointCount": t.integer().optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorOut"])
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
    types["ListNotificationChannelsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "notificationChannels": t.array(
                t.proxy(renames["NotificationChannelIn"])
            ).optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["ListNotificationChannelsResponseIn"])
    types["ListNotificationChannelsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "notificationChannels": t.array(
                t.proxy(renames["NotificationChannelOut"])
            ).optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNotificationChannelsResponseOut"])
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
    types["AvailabilityCriteriaIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AvailabilityCriteriaIn"]
    )
    types["AvailabilityCriteriaOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AvailabilityCriteriaOut"])
    types["QueryTimeSeriesRequestIn"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "query": t.string(),
        }
    ).named(renames["QueryTimeSeriesRequestIn"])
    types["QueryTimeSeriesRequestOut"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "query": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryTimeSeriesRequestOut"])
    types["CollectdPayloadIn"] = t.struct(
        {
            "values": t.array(t.proxy(renames["CollectdValueIn"])).optional(),
            "plugin": t.string().optional(),
            "endTime": t.string().optional(),
            "pluginInstance": t.string().optional(),
            "type": t.string().optional(),
            "typeInstance": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["CollectdPayloadIn"])
    types["CollectdPayloadOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["CollectdValueOut"])).optional(),
            "plugin": t.string().optional(),
            "endTime": t.string().optional(),
            "pluginInstance": t.string().optional(),
            "type": t.string().optional(),
            "typeInstance": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CollectdPayloadOut"])
    types["ForecastOptionsIn"] = t.struct({"forecastHorizon": t.string()}).named(
        renames["ForecastOptionsIn"]
    )
    types["ForecastOptionsOut"] = t.struct(
        {
            "forecastHorizon": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ForecastOptionsOut"])
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
    types["MonitoringQueryLanguageConditionIn"] = t.struct(
        {
            "query": t.string().optional(),
            "trigger": t.proxy(renames["TriggerIn"]).optional(),
            "duration": t.string().optional(),
            "evaluationMissingData": t.string().optional(),
        }
    ).named(renames["MonitoringQueryLanguageConditionIn"])
    types["MonitoringQueryLanguageConditionOut"] = t.struct(
        {
            "query": t.string().optional(),
            "trigger": t.proxy(renames["TriggerOut"]).optional(),
            "duration": t.string().optional(),
            "evaluationMissingData": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoringQueryLanguageConditionOut"])
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
    types["ServiceIn"] = t.struct(
        {
            "gkeService": t.proxy(renames["GkeServiceIn"]).optional(),
            "clusterIstio": t.proxy(renames["ClusterIstioIn"]).optional(),
            "telemetry": t.proxy(renames["TelemetryIn"]).optional(),
            "cloudEndpoints": t.proxy(renames["CloudEndpointsIn"]).optional(),
            "appEngine": t.proxy(renames["AppEngineIn"]).optional(),
            "gkeNamespace": t.proxy(renames["GkeNamespaceIn"]).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "basicService": t.proxy(renames["BasicServiceIn"]).optional(),
            "gkeWorkload": t.proxy(renames["GkeWorkloadIn"]).optional(),
            "meshIstio": t.proxy(renames["MeshIstioIn"]).optional(),
            "displayName": t.string().optional(),
            "istioCanonicalService": t.proxy(
                renames["IstioCanonicalServiceIn"]
            ).optional(),
            "custom": t.proxy(renames["CustomIn"]).optional(),
            "name": t.string().optional(),
            "cloudRun": t.proxy(renames["CloudRunIn"]).optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "gkeService": t.proxy(renames["GkeServiceOut"]).optional(),
            "clusterIstio": t.proxy(renames["ClusterIstioOut"]).optional(),
            "telemetry": t.proxy(renames["TelemetryOut"]).optional(),
            "cloudEndpoints": t.proxy(renames["CloudEndpointsOut"]).optional(),
            "appEngine": t.proxy(renames["AppEngineOut"]).optional(),
            "gkeNamespace": t.proxy(renames["GkeNamespaceOut"]).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "basicService": t.proxy(renames["BasicServiceOut"]).optional(),
            "gkeWorkload": t.proxy(renames["GkeWorkloadOut"]).optional(),
            "meshIstio": t.proxy(renames["MeshIstioOut"]).optional(),
            "displayName": t.string().optional(),
            "istioCanonicalService": t.proxy(
                renames["IstioCanonicalServiceOut"]
            ).optional(),
            "custom": t.proxy(renames["CustomOut"]).optional(),
            "name": t.string().optional(),
            "cloudRun": t.proxy(renames["CloudRunOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
    types["ClusterIstioIn"] = t.struct(
        {
            "serviceNamespace": t.string().optional(),
            "serviceName": t.string().optional(),
            "clusterName": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ClusterIstioIn"])
    types["ClusterIstioOut"] = t.struct(
        {
            "serviceNamespace": t.string().optional(),
            "serviceName": t.string().optional(),
            "clusterName": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterIstioOut"])
    types["CreateCollectdTimeSeriesRequestIn"] = t.struct(
        {
            "resource": t.proxy(renames["MonitoredResourceIn"]).optional(),
            "collectdPayloads": t.array(
                t.proxy(renames["CollectdPayloadIn"])
            ).optional(),
            "collectdVersion": t.string().optional(),
        }
    ).named(renames["CreateCollectdTimeSeriesRequestIn"])
    types["CreateCollectdTimeSeriesRequestOut"] = t.struct(
        {
            "resource": t.proxy(renames["MonitoredResourceOut"]).optional(),
            "collectdPayloads": t.array(
                t.proxy(renames["CollectdPayloadOut"])
            ).optional(),
            "collectdVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateCollectdTimeSeriesRequestOut"])
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
    types["CreateCollectdTimeSeriesResponseIn"] = t.struct(
        {
            "summary": t.proxy(renames["CreateTimeSeriesSummaryIn"]).optional(),
            "payloadErrors": t.array(
                t.proxy(renames["CollectdPayloadErrorIn"])
            ).optional(),
        }
    ).named(renames["CreateCollectdTimeSeriesResponseIn"])
    types["CreateCollectdTimeSeriesResponseOut"] = t.struct(
        {
            "summary": t.proxy(renames["CreateTimeSeriesSummaryOut"]).optional(),
            "payloadErrors": t.array(
                t.proxy(renames["CollectdPayloadErrorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateCollectdTimeSeriesResponseOut"])
    types["GroupIn"] = t.struct(
        {
            "parentName": t.string().optional(),
            "isCluster": t.boolean().optional(),
            "name": t.string().optional(),
            "filter": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "parentName": t.string().optional(),
            "isCluster": t.boolean().optional(),
            "name": t.string().optional(),
            "filter": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
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
    types["DroppedLabelsIn"] = t.struct(
        {"label": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["DroppedLabelsIn"])
    types["DroppedLabelsOut"] = t.struct(
        {
            "label": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DroppedLabelsOut"])
    types["HttpCheckIn"] = t.struct(
        {
            "contentType": t.string().optional(),
            "maskHeaders": t.boolean().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "customContentType": t.string().optional(),
            "requestMethod": t.string().optional(),
            "path": t.string().optional(),
            "useSsl": t.boolean().optional(),
            "validateSsl": t.boolean().optional(),
            "port": t.integer().optional(),
            "authInfo": t.proxy(renames["BasicAuthenticationIn"]).optional(),
            "pingConfig": t.proxy(renames["PingConfigIn"]).optional(),
            "body": t.string().optional(),
            "acceptedResponseStatusCodes": t.array(
                t.proxy(renames["ResponseStatusCodeIn"])
            ).optional(),
        }
    ).named(renames["HttpCheckIn"])
    types["HttpCheckOut"] = t.struct(
        {
            "contentType": t.string().optional(),
            "maskHeaders": t.boolean().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "customContentType": t.string().optional(),
            "requestMethod": t.string().optional(),
            "path": t.string().optional(),
            "useSsl": t.boolean().optional(),
            "validateSsl": t.boolean().optional(),
            "port": t.integer().optional(),
            "authInfo": t.proxy(renames["BasicAuthenticationOut"]).optional(),
            "pingConfig": t.proxy(renames["PingConfigOut"]).optional(),
            "body": t.string().optional(),
            "acceptedResponseStatusCodes": t.array(
                t.proxy(renames["ResponseStatusCodeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpCheckOut"])
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
    types["LatencyCriteriaIn"] = t.struct({"threshold": t.string().optional()}).named(
        renames["LatencyCriteriaIn"]
    )
    types["LatencyCriteriaOut"] = t.struct(
        {
            "threshold": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LatencyCriteriaOut"])
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
    types["DistributionIn"] = t.struct(
        {
            "range": t.proxy(renames["RangeIn"]).optional(),
            "bucketCounts": t.array(t.string()),
            "bucketOptions": t.proxy(renames["BucketOptionsIn"]),
            "count": t.string().optional(),
            "sumOfSquaredDeviation": t.number().optional(),
            "mean": t.number().optional(),
            "exemplars": t.array(t.proxy(renames["ExemplarIn"])).optional(),
        }
    ).named(renames["DistributionIn"])
    types["DistributionOut"] = t.struct(
        {
            "range": t.proxy(renames["RangeOut"]).optional(),
            "bucketCounts": t.array(t.string()),
            "bucketOptions": t.proxy(renames["BucketOptionsOut"]),
            "count": t.string().optional(),
            "sumOfSquaredDeviation": t.number().optional(),
            "mean": t.number().optional(),
            "exemplars": t.array(t.proxy(renames["ExemplarOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DistributionOut"])
    types["PointDataIn"] = t.struct(
        {
            "values": t.array(t.proxy(renames["TypedValueIn"])).optional(),
            "timeInterval": t.proxy(renames["TimeIntervalIn"]).optional(),
        }
    ).named(renames["PointDataIn"])
    types["PointDataOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["TypedValueOut"])).optional(),
            "timeInterval": t.proxy(renames["TimeIntervalOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PointDataOut"])
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
    types["SpanContextIn"] = t.struct({"spanName": t.string().optional()}).named(
        renames["SpanContextIn"]
    )
    types["SpanContextOut"] = t.struct(
        {
            "spanName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpanContextOut"])
    types["NotificationRateLimitIn"] = t.struct(
        {"period": t.string().optional()}
    ).named(renames["NotificationRateLimitIn"])
    types["NotificationRateLimitOut"] = t.struct(
        {
            "period": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationRateLimitOut"])
    types["ValueDescriptorIn"] = t.struct(
        {
            "valueType": t.string().optional(),
            "key": t.string().optional(),
            "metricKind": t.string().optional(),
            "unit": t.string().optional(),
        }
    ).named(renames["ValueDescriptorIn"])
    types["ValueDescriptorOut"] = t.struct(
        {
            "valueType": t.string().optional(),
            "key": t.string().optional(),
            "metricKind": t.string().optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueDescriptorOut"])
    types["ContentMatcherIn"] = t.struct(
        {
            "content": t.string().optional(),
            "jsonPathMatcher": t.proxy(renames["JsonPathMatcherIn"]).optional(),
            "matcher": t.string().optional(),
        }
    ).named(renames["ContentMatcherIn"])
    types["ContentMatcherOut"] = t.struct(
        {
            "content": t.string().optional(),
            "jsonPathMatcher": t.proxy(renames["JsonPathMatcherOut"]).optional(),
            "matcher": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentMatcherOut"])
    types["MeshIstioIn"] = t.struct(
        {
            "serviceName": t.string().optional(),
            "meshUid": t.string().optional(),
            "serviceNamespace": t.string().optional(),
        }
    ).named(renames["MeshIstioIn"])
    types["MeshIstioOut"] = t.struct(
        {
            "serviceName": t.string().optional(),
            "meshUid": t.string().optional(),
            "serviceNamespace": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MeshIstioOut"])
    types["TelemetryIn"] = t.struct({"resourceName": t.string().optional()}).named(
        renames["TelemetryIn"]
    )
    types["TelemetryOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TelemetryOut"])
    types["NotificationChannelDescriptorIn"] = t.struct(
        {
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "supportedTiers": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "launchStage": t.string().optional(),
            "description": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["NotificationChannelDescriptorIn"])
    types["NotificationChannelDescriptorOut"] = t.struct(
        {
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "supportedTiers": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "launchStage": t.string().optional(),
            "description": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationChannelDescriptorOut"])
    types["SnoozeIn"] = t.struct(
        {
            "interval": t.proxy(renames["TimeIntervalIn"]),
            "name": t.string(),
            "criteria": t.proxy(renames["CriteriaIn"]),
            "displayName": t.string(),
        }
    ).named(renames["SnoozeIn"])
    types["SnoozeOut"] = t.struct(
        {
            "interval": t.proxy(renames["TimeIntervalOut"]),
            "name": t.string(),
            "criteria": t.proxy(renames["CriteriaOut"]),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnoozeOut"])
    types["CollectdPayloadErrorIn"] = t.struct(
        {
            "index": t.integer().optional(),
            "valueErrors": t.array(t.proxy(renames["CollectdValueErrorIn"])).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["CollectdPayloadErrorIn"])
    types["CollectdPayloadErrorOut"] = t.struct(
        {
            "index": t.integer().optional(),
            "valueErrors": t.array(
                t.proxy(renames["CollectdValueErrorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CollectdPayloadErrorOut"])
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
    types["MonitoredResourceDescriptorIn"] = t.struct(
        {
            "type": t.string(),
            "description": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])),
            "displayName": t.string().optional(),
            "launchStage": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["MonitoredResourceDescriptorIn"])
    types["MonitoredResourceDescriptorOut"] = t.struct(
        {
            "type": t.string(),
            "description": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])),
            "displayName": t.string().optional(),
            "launchStage": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceDescriptorOut"])
    types["BasicSliIn"] = t.struct(
        {
            "latency": t.proxy(renames["LatencyCriteriaIn"]).optional(),
            "location": t.array(t.string()).optional(),
            "availability": t.proxy(renames["AvailabilityCriteriaIn"]).optional(),
            "version": t.array(t.string()).optional(),
            "method": t.array(t.string()).optional(),
        }
    ).named(renames["BasicSliIn"])
    types["BasicSliOut"] = t.struct(
        {
            "latency": t.proxy(renames["LatencyCriteriaOut"]).optional(),
            "location": t.array(t.string()).optional(),
            "availability": t.proxy(renames["AvailabilityCriteriaOut"]).optional(),
            "version": t.array(t.string()).optional(),
            "method": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicSliOut"])
    types["LabelValueIn"] = t.struct(
        {
            "int64Value": t.string().optional(),
            "stringValue": t.string().optional(),
            "boolValue": t.boolean().optional(),
        }
    ).named(renames["LabelValueIn"])
    types["LabelValueOut"] = t.struct(
        {
            "int64Value": t.string().optional(),
            "stringValue": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelValueOut"])
    types["SendNotificationChannelVerificationCodeRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SendNotificationChannelVerificationCodeRequestIn"])
    types["SendNotificationChannelVerificationCodeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SendNotificationChannelVerificationCodeRequestOut"])
    types["AggregationIn"] = t.struct(
        {
            "perSeriesAligner": t.string().optional(),
            "crossSeriesReducer": t.string().optional(),
            "alignmentPeriod": t.string().optional(),
            "groupByFields": t.array(t.string()).optional(),
        }
    ).named(renames["AggregationIn"])
    types["AggregationOut"] = t.struct(
        {
            "perSeriesAligner": t.string().optional(),
            "crossSeriesReducer": t.string().optional(),
            "alignmentPeriod": t.string().optional(),
            "groupByFields": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationOut"])
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
    types["TypeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "fields": t.array(t.proxy(renames["FieldIn"])).optional(),
            "edition": t.string().optional(),
            "oneofs": t.array(t.string()).optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "edition": t.string().optional(),
            "oneofs": t.array(t.string()).optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
    types["ListTimeSeriesResponseIn"] = t.struct(
        {
            "executionErrors": t.array(t.proxy(renames["StatusIn"])).optional(),
            "timeSeries": t.array(t.proxy(renames["TimeSeriesIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unit": t.string().optional(),
        }
    ).named(renames["ListTimeSeriesResponseIn"])
    types["ListTimeSeriesResponseOut"] = t.struct(
        {
            "executionErrors": t.array(t.proxy(renames["StatusOut"])).optional(),
            "timeSeries": t.array(t.proxy(renames["TimeSeriesOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTimeSeriesResponseOut"])
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
    types["OperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["CriteriaIn"] = t.struct({"policies": t.array(t.string()).optional()}).named(
        renames["CriteriaIn"]
    )
    types["CriteriaOut"] = t.struct(
        {
            "policies": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CriteriaOut"])
    types["MetricDescriptorIn"] = t.struct(
        {
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "unit": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "launchStage": t.string().optional(),
            "type": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
            "name": t.string().optional(),
            "metricKind": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "valueType": t.string().optional(),
        }
    ).named(renames["MetricDescriptorIn"])
    types["MetricDescriptorOut"] = t.struct(
        {
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "unit": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "launchStage": t.string().optional(),
            "type": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataOut"]).optional(),
            "name": t.string().optional(),
            "metricKind": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "valueType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorOut"])
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
    types["ConditionIn"] = t.struct(
        {
            "name": t.string(),
            "conditionMonitoringQueryLanguage": t.proxy(
                renames["MonitoringQueryLanguageConditionIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "conditionAbsent": t.proxy(renames["MetricAbsenceIn"]).optional(),
            "conditionMatchedLog": t.proxy(renames["LogMatchIn"]).optional(),
            "conditionThreshold": t.proxy(renames["MetricThresholdIn"]).optional(),
        }
    ).named(renames["ConditionIn"])
    types["ConditionOut"] = t.struct(
        {
            "name": t.string(),
            "conditionMonitoringQueryLanguage": t.proxy(
                renames["MonitoringQueryLanguageConditionOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "conditionAbsent": t.proxy(renames["MetricAbsenceOut"]).optional(),
            "conditionMatchedLog": t.proxy(renames["LogMatchOut"]).optional(),
            "conditionThreshold": t.proxy(renames["MetricThresholdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionOut"])
    types["RequestBasedSliIn"] = t.struct(
        {
            "goodTotalRatio": t.proxy(renames["TimeSeriesRatioIn"]).optional(),
            "distributionCut": t.proxy(renames["DistributionCutIn"]).optional(),
        }
    ).named(renames["RequestBasedSliIn"])
    types["RequestBasedSliOut"] = t.struct(
        {
            "goodTotalRatio": t.proxy(renames["TimeSeriesRatioOut"]).optional(),
            "distributionCut": t.proxy(renames["DistributionCutOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestBasedSliOut"])
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
    types["GetNotificationChannelVerificationCodeRequestIn"] = t.struct(
        {"expireTime": t.string().optional()}
    ).named(renames["GetNotificationChannelVerificationCodeRequestIn"])
    types["GetNotificationChannelVerificationCodeRequestOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetNotificationChannelVerificationCodeRequestOut"])
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
    types["CloudEndpointsIn"] = t.struct({"service": t.string().optional()}).named(
        renames["CloudEndpointsIn"]
    )
    types["CloudEndpointsOut"] = t.struct(
        {
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudEndpointsOut"])
    types["TimeSeriesRatioIn"] = t.struct(
        {
            "badServiceFilter": t.string().optional(),
            "goodServiceFilter": t.string().optional(),
            "totalServiceFilter": t.string().optional(),
        }
    ).named(renames["TimeSeriesRatioIn"])
    types["TimeSeriesRatioOut"] = t.struct(
        {
            "badServiceFilter": t.string().optional(),
            "goodServiceFilter": t.string().optional(),
            "totalServiceFilter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeSeriesRatioOut"])
    types["GkeNamespaceIn"] = t.struct(
        {
            "namespaceName": t.string().optional(),
            "location": t.string().optional(),
            "clusterName": t.string().optional(),
        }
    ).named(renames["GkeNamespaceIn"])
    types["GkeNamespaceOut"] = t.struct(
        {
            "namespaceName": t.string().optional(),
            "projectId": t.string().optional(),
            "location": t.string().optional(),
            "clusterName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeNamespaceOut"])
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
    types["GkeWorkloadIn"] = t.struct(
        {
            "topLevelControllerName": t.string().optional(),
            "clusterName": t.string().optional(),
            "namespaceName": t.string().optional(),
            "location": t.string().optional(),
            "topLevelControllerType": t.string().optional(),
        }
    ).named(renames["GkeWorkloadIn"])
    types["GkeWorkloadOut"] = t.struct(
        {
            "topLevelControllerName": t.string().optional(),
            "projectId": t.string().optional(),
            "clusterName": t.string().optional(),
            "namespaceName": t.string().optional(),
            "location": t.string().optional(),
            "topLevelControllerType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeWorkloadOut"])
    types["FieldIn"] = t.struct(
        {
            "cardinality": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "packed": t.boolean().optional(),
            "name": t.string().optional(),
            "defaultValue": t.string().optional(),
            "kind": t.string().optional(),
            "number": t.integer().optional(),
            "typeUrl": t.string().optional(),
            "oneofIndex": t.integer().optional(),
            "jsonName": t.string().optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "cardinality": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "packed": t.boolean().optional(),
            "name": t.string().optional(),
            "defaultValue": t.string().optional(),
            "kind": t.string().optional(),
            "number": t.integer().optional(),
            "typeUrl": t.string().optional(),
            "oneofIndex": t.integer().optional(),
            "jsonName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
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
    types["PingConfigIn"] = t.struct({"pingsCount": t.integer().optional()}).named(
        renames["PingConfigIn"]
    )
    types["PingConfigOut"] = t.struct(
        {
            "pingsCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PingConfigOut"])
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
    types["AlertStrategyIn"] = t.struct(
        {
            "notificationChannelStrategy": t.array(
                t.proxy(renames["NotificationChannelStrategyIn"])
            ).optional(),
            "autoClose": t.string().optional(),
            "notificationRateLimit": t.proxy(renames["NotificationRateLimitIn"]),
        }
    ).named(renames["AlertStrategyIn"])
    types["AlertStrategyOut"] = t.struct(
        {
            "notificationChannelStrategy": t.array(
                t.proxy(renames["NotificationChannelStrategyOut"])
            ).optional(),
            "autoClose": t.string().optional(),
            "notificationRateLimit": t.proxy(renames["NotificationRateLimitOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlertStrategyOut"])
    types["DistributionCutIn"] = t.struct(
        {
            "distributionFilter": t.string().optional(),
            "range": t.proxy(renames["GoogleMonitoringV3RangeIn"]).optional(),
        }
    ).named(renames["DistributionCutIn"])
    types["DistributionCutOut"] = t.struct(
        {
            "distributionFilter": t.string().optional(),
            "range": t.proxy(renames["GoogleMonitoringV3RangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DistributionCutOut"])
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
    types["CustomIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CustomIn"]
    )
    types["CustomOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CustomOut"])
    types["PointIn"] = t.struct(
        {
            "interval": t.proxy(renames["TimeIntervalIn"]).optional(),
            "value": t.proxy(renames["TypedValueIn"]).optional(),
        }
    ).named(renames["PointIn"])
    types["PointOut"] = t.struct(
        {
            "interval": t.proxy(renames["TimeIntervalOut"]).optional(),
            "value": t.proxy(renames["TypedValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PointOut"])
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
    types["TimeSeriesIn"] = t.struct(
        {
            "resource": t.proxy(renames["MonitoredResourceIn"]).optional(),
            "points": t.array(t.proxy(renames["PointIn"])).optional(),
            "metricKind": t.string().optional(),
            "valueType": t.string().optional(),
            "metadata": t.proxy(renames["MonitoredResourceMetadataIn"]).optional(),
            "metric": t.proxy(renames["MetricIn"]).optional(),
            "unit": t.string().optional(),
        }
    ).named(renames["TimeSeriesIn"])
    types["TimeSeriesOut"] = t.struct(
        {
            "resource": t.proxy(renames["MonitoredResourceOut"]).optional(),
            "points": t.array(t.proxy(renames["PointOut"])).optional(),
            "metricKind": t.string().optional(),
            "valueType": t.string().optional(),
            "metadata": t.proxy(renames["MonitoredResourceMetadataOut"]).optional(),
            "metric": t.proxy(renames["MetricOut"]).optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeSeriesOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["TimeSeriesDescriptorIn"] = t.struct(
        {
            "labelDescriptors": t.array(
                t.proxy(renames["LabelDescriptorIn"])
            ).optional(),
            "pointDescriptors": t.array(
                t.proxy(renames["ValueDescriptorIn"])
            ).optional(),
        }
    ).named(renames["TimeSeriesDescriptorIn"])
    types["TimeSeriesDescriptorOut"] = t.struct(
        {
            "labelDescriptors": t.array(
                t.proxy(renames["LabelDescriptorOut"])
            ).optional(),
            "pointDescriptors": t.array(
                t.proxy(renames["ValueDescriptorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeSeriesDescriptorOut"])
    types["SourceContextIn"] = t.struct({"fileName": t.string().optional()}).named(
        renames["SourceContextIn"]
    )
    types["SourceContextOut"] = t.struct(
        {
            "fileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceContextOut"])
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

    functions = {}
    functions["organizationsTimeSeriesList"] = monitoring.get(
        "v3/{name}/timeSeries",
        t.struct(
            {
                "filter": t.string(),
                "interval.startTime": t.string().optional(),
                "secondaryAggregation.groupByFields": t.string().optional(),
                "secondaryAggregation.alignmentPeriod": t.string().optional(),
                "orderBy": t.string().optional(),
                "interval.endTime": t.string(),
                "pageSize": t.integer().optional(),
                "view": t.string(),
                "aggregation.groupByFields": t.string().optional(),
                "aggregation.crossSeriesReducer": t.string().optional(),
                "secondaryAggregation.crossSeriesReducer": t.string().optional(),
                "aggregation.alignmentPeriod": t.string().optional(),
                "aggregation.perSeriesAligner": t.string().optional(),
                "name": t.string(),
                "secondaryAggregation.perSeriesAligner": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTimeSeriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersTimeSeriesList"] = monitoring.get(
        "v3/{name}/timeSeries",
        t.struct(
            {
                "secondaryAggregation.groupByFields": t.string().optional(),
                "pageToken": t.string().optional(),
                "aggregation.groupByFields": t.string().optional(),
                "secondaryAggregation.perSeriesAligner": t.string().optional(),
                "secondaryAggregation.alignmentPeriod": t.string().optional(),
                "secondaryAggregation.crossSeriesReducer": t.string().optional(),
                "orderBy": t.string().optional(),
                "interval.startTime": t.string().optional(),
                "interval.endTime": t.string(),
                "aggregation.alignmentPeriod": t.string().optional(),
                "aggregation.crossSeriesReducer": t.string().optional(),
                "pageSize": t.integer().optional(),
                "aggregation.perSeriesAligner": t.string().optional(),
                "filter": t.string(),
                "view": t.string(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTimeSeriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsCreate"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsUpdate"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsDelete"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsList"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsGet"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsMembersList"] = monitoring.get(
        "v3/{name}/members",
        t.struct(
            {
                "interval.endTime": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string(),
                "interval.startTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGroupMembersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelsPatch"] = monitoring.post(
        "v3/{name}:verify",
        t.struct(
            {"name": t.string(), "code": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["NotificationChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelsList"] = monitoring.post(
        "v3/{name}:verify",
        t.struct(
            {"name": t.string(), "code": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["NotificationChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelsCreate"] = monitoring.post(
        "v3/{name}:verify",
        t.struct(
            {"name": t.string(), "code": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["NotificationChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelsGetVerificationCode"] = monitoring.post(
        "v3/{name}:verify",
        t.struct(
            {"name": t.string(), "code": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["NotificationChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelsDelete"] = monitoring.post(
        "v3/{name}:verify",
        t.struct(
            {"name": t.string(), "code": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["NotificationChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelsGet"] = monitoring.post(
        "v3/{name}:verify",
        t.struct(
            {"name": t.string(), "code": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["NotificationChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelsSendVerificationCode"] = monitoring.post(
        "v3/{name}:verify",
        t.struct(
            {"name": t.string(), "code": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["NotificationChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsNotificationChannelsVerify"] = monitoring.post(
        "v3/{name}:verify",
        t.struct(
            {"name": t.string(), "code": t.string(), "auth": t.string().optional()}
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
    functions["projectsTimeSeriesCreateService"] = monitoring.post(
        "v3/{name}/timeSeries",
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
        "v3/{name}/timeSeries",
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
    functions["projectsTimeSeriesQuery"] = monitoring.post(
        "v3/{name}/timeSeries",
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
        "v3/{name}/timeSeries",
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
    functions["projectsSnoozesPatch"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SnoozeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnoozesList"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SnoozeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnoozesCreate"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SnoozeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnoozesGet"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SnoozeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMetricDescriptorsDelete"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MetricDescriptorOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMetricDescriptorsList"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MetricDescriptorOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMetricDescriptorsCreate"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MetricDescriptorOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMetricDescriptorsGet"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MetricDescriptorOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsCollectdTimeSeriesCreate"] = monitoring.post(
        "v3/{name}/collectdTimeSeries",
        t.struct(
            {
                "name": t.string().optional(),
                "resource": t.proxy(renames["MonitoredResourceIn"]).optional(),
                "collectdPayloads": t.array(
                    t.proxy(renames["CollectdPayloadIn"])
                ).optional(),
                "collectdVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreateCollectdTimeSeriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAlertPoliciesGet"] = monitoring.post(
        "v3/{name}/alertPolicies",
        t.struct(
            {
                "name": t.string(),
                "combiner": t.string().optional(),
                "displayName": t.string().optional(),
                "creationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "documentation": t.proxy(renames["DocumentationIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "validity": t.proxy(renames["StatusIn"]).optional(),
                "notificationChannels": t.array(t.string()).optional(),
                "conditions": t.array(t.proxy(renames["ConditionIn"])).optional(),
                "enabled": t.boolean().optional(),
                "alertStrategy": t.proxy(renames["AlertStrategyIn"]).optional(),
                "mutationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AlertPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAlertPoliciesDelete"] = monitoring.post(
        "v3/{name}/alertPolicies",
        t.struct(
            {
                "name": t.string(),
                "combiner": t.string().optional(),
                "displayName": t.string().optional(),
                "creationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "documentation": t.proxy(renames["DocumentationIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "validity": t.proxy(renames["StatusIn"]).optional(),
                "notificationChannels": t.array(t.string()).optional(),
                "conditions": t.array(t.proxy(renames["ConditionIn"])).optional(),
                "enabled": t.boolean().optional(),
                "alertStrategy": t.proxy(renames["AlertStrategyIn"]).optional(),
                "mutationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AlertPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAlertPoliciesList"] = monitoring.post(
        "v3/{name}/alertPolicies",
        t.struct(
            {
                "name": t.string(),
                "combiner": t.string().optional(),
                "displayName": t.string().optional(),
                "creationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "documentation": t.proxy(renames["DocumentationIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "validity": t.proxy(renames["StatusIn"]).optional(),
                "notificationChannels": t.array(t.string()).optional(),
                "conditions": t.array(t.proxy(renames["ConditionIn"])).optional(),
                "enabled": t.boolean().optional(),
                "alertStrategy": t.proxy(renames["AlertStrategyIn"]).optional(),
                "mutationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AlertPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAlertPoliciesPatch"] = monitoring.post(
        "v3/{name}/alertPolicies",
        t.struct(
            {
                "name": t.string(),
                "combiner": t.string().optional(),
                "displayName": t.string().optional(),
                "creationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "documentation": t.proxy(renames["DocumentationIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "validity": t.proxy(renames["StatusIn"]).optional(),
                "notificationChannels": t.array(t.string()).optional(),
                "conditions": t.array(t.proxy(renames["ConditionIn"])).optional(),
                "enabled": t.boolean().optional(),
                "alertStrategy": t.proxy(renames["AlertStrategyIn"]).optional(),
                "mutationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AlertPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAlertPoliciesCreate"] = monitoring.post(
        "v3/{name}/alertPolicies",
        t.struct(
            {
                "name": t.string(),
                "combiner": t.string().optional(),
                "displayName": t.string().optional(),
                "creationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "documentation": t.proxy(renames["DocumentationIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "validity": t.proxy(renames["StatusIn"]).optional(),
                "notificationChannels": t.array(t.string()).optional(),
                "conditions": t.array(t.proxy(renames["ConditionIn"])).optional(),
                "enabled": t.boolean().optional(),
                "alertStrategy": t.proxy(renames["AlertStrategyIn"]).optional(),
                "mutationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AlertPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUptimeCheckConfigsGet"] = monitoring.post(
        "v3/{parent}/uptimeCheckConfigs",
        t.struct(
            {
                "parent": t.string(),
                "isInternal": t.boolean().optional(),
                "name": t.string().optional(),
                "tcpCheck": t.proxy(renames["TcpCheckIn"]).optional(),
                "httpCheck": t.proxy(renames["HttpCheckIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "period": t.string().optional(),
                "displayName": t.string().optional(),
                "checkerType": t.string().optional(),
                "internalCheckers": t.array(
                    t.proxy(renames["InternalCheckerIn"])
                ).optional(),
                "contentMatchers": t.array(
                    t.proxy(renames["ContentMatcherIn"])
                ).optional(),
                "resourceGroup": t.proxy(renames["ResourceGroupIn"]).optional(),
                "timeout": t.string().optional(),
                "monitoredResource": t.proxy(renames["MonitoredResourceIn"]).optional(),
                "selectedRegions": t.array(t.string()).optional(),
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
                "isInternal": t.boolean().optional(),
                "name": t.string().optional(),
                "tcpCheck": t.proxy(renames["TcpCheckIn"]).optional(),
                "httpCheck": t.proxy(renames["HttpCheckIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "period": t.string().optional(),
                "displayName": t.string().optional(),
                "checkerType": t.string().optional(),
                "internalCheckers": t.array(
                    t.proxy(renames["InternalCheckerIn"])
                ).optional(),
                "contentMatchers": t.array(
                    t.proxy(renames["ContentMatcherIn"])
                ).optional(),
                "resourceGroup": t.proxy(renames["ResourceGroupIn"]).optional(),
                "timeout": t.string().optional(),
                "monitoredResource": t.proxy(renames["MonitoredResourceIn"]).optional(),
                "selectedRegions": t.array(t.string()).optional(),
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
                "isInternal": t.boolean().optional(),
                "name": t.string().optional(),
                "tcpCheck": t.proxy(renames["TcpCheckIn"]).optional(),
                "httpCheck": t.proxy(renames["HttpCheckIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "period": t.string().optional(),
                "displayName": t.string().optional(),
                "checkerType": t.string().optional(),
                "internalCheckers": t.array(
                    t.proxy(renames["InternalCheckerIn"])
                ).optional(),
                "contentMatchers": t.array(
                    t.proxy(renames["ContentMatcherIn"])
                ).optional(),
                "resourceGroup": t.proxy(renames["ResourceGroupIn"]).optional(),
                "timeout": t.string().optional(),
                "monitoredResource": t.proxy(renames["MonitoredResourceIn"]).optional(),
                "selectedRegions": t.array(t.string()).optional(),
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
                "isInternal": t.boolean().optional(),
                "name": t.string().optional(),
                "tcpCheck": t.proxy(renames["TcpCheckIn"]).optional(),
                "httpCheck": t.proxy(renames["HttpCheckIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "period": t.string().optional(),
                "displayName": t.string().optional(),
                "checkerType": t.string().optional(),
                "internalCheckers": t.array(
                    t.proxy(renames["InternalCheckerIn"])
                ).optional(),
                "contentMatchers": t.array(
                    t.proxy(renames["ContentMatcherIn"])
                ).optional(),
                "resourceGroup": t.proxy(renames["ResourceGroupIn"]).optional(),
                "timeout": t.string().optional(),
                "monitoredResource": t.proxy(renames["MonitoredResourceIn"]).optional(),
                "selectedRegions": t.array(t.string()).optional(),
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
                "isInternal": t.boolean().optional(),
                "name": t.string().optional(),
                "tcpCheck": t.proxy(renames["TcpCheckIn"]).optional(),
                "httpCheck": t.proxy(renames["HttpCheckIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "period": t.string().optional(),
                "displayName": t.string().optional(),
                "checkerType": t.string().optional(),
                "internalCheckers": t.array(
                    t.proxy(renames["InternalCheckerIn"])
                ).optional(),
                "contentMatchers": t.array(
                    t.proxy(renames["ContentMatcherIn"])
                ).optional(),
                "resourceGroup": t.proxy(renames["ResourceGroupIn"]).optional(),
                "timeout": t.string().optional(),
                "monitoredResource": t.proxy(renames["MonitoredResourceIn"]).optional(),
                "selectedRegions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UptimeCheckConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesPatch"] = monitoring.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesList"] = monitoring.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesGet"] = monitoring.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesCreate"] = monitoring.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesDelete"] = monitoring.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesServiceLevelObjectivesPatch"] = monitoring.get(
        "v3/{name}",
        t.struct(
            {
                "view": t.string().optional(),
                "name": t.string(),
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
                "view": t.string().optional(),
                "name": t.string(),
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
                "view": t.string().optional(),
                "name": t.string(),
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
                "view": t.string().optional(),
                "name": t.string(),
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
                "view": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceLevelObjectiveOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["uptimeCheckIpsList"] = monitoring.get(
        "v3/uptimeCheckIps",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
