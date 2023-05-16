from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_monitoring() -> Import:
    monitoring = HTTPRuntime("https://monitoring.googleapis.com/")

    renames = {
        "ErrorResponse": "_monitoring_1_ErrorResponse",
        "ListUptimeCheckIpsResponseIn": "_monitoring_2_ListUptimeCheckIpsResponseIn",
        "ListUptimeCheckIpsResponseOut": "_monitoring_3_ListUptimeCheckIpsResponseOut",
        "ListSnoozesResponseIn": "_monitoring_4_ListSnoozesResponseIn",
        "ListSnoozesResponseOut": "_monitoring_5_ListSnoozesResponseOut",
        "MonitoringQueryLanguageConditionIn": "_monitoring_6_MonitoringQueryLanguageConditionIn",
        "MonitoringQueryLanguageConditionOut": "_monitoring_7_MonitoringQueryLanguageConditionOut",
        "ListServicesResponseIn": "_monitoring_8_ListServicesResponseIn",
        "ListServicesResponseOut": "_monitoring_9_ListServicesResponseOut",
        "DocumentationIn": "_monitoring_10_DocumentationIn",
        "DocumentationOut": "_monitoring_11_DocumentationOut",
        "FieldIn": "_monitoring_12_FieldIn",
        "FieldOut": "_monitoring_13_FieldOut",
        "CollectdValueIn": "_monitoring_14_CollectdValueIn",
        "CollectdValueOut": "_monitoring_15_CollectdValueOut",
        "MutationRecordIn": "_monitoring_16_MutationRecordIn",
        "MutationRecordOut": "_monitoring_17_MutationRecordOut",
        "ListNotificationChannelDescriptorsResponseIn": "_monitoring_18_ListNotificationChannelDescriptorsResponseIn",
        "ListNotificationChannelDescriptorsResponseOut": "_monitoring_19_ListNotificationChannelDescriptorsResponseOut",
        "CloudRunIn": "_monitoring_20_CloudRunIn",
        "CloudRunOut": "_monitoring_21_CloudRunOut",
        "NotificationChannelStrategyIn": "_monitoring_22_NotificationChannelStrategyIn",
        "NotificationChannelStrategyOut": "_monitoring_23_NotificationChannelStrategyOut",
        "SnoozeIn": "_monitoring_24_SnoozeIn",
        "SnoozeOut": "_monitoring_25_SnoozeOut",
        "CollectdPayloadErrorIn": "_monitoring_26_CollectdPayloadErrorIn",
        "CollectdPayloadErrorOut": "_monitoring_27_CollectdPayloadErrorOut",
        "BasicServiceIn": "_monitoring_28_BasicServiceIn",
        "BasicServiceOut": "_monitoring_29_BasicServiceOut",
        "ListMonitoredResourceDescriptorsResponseIn": "_monitoring_30_ListMonitoredResourceDescriptorsResponseIn",
        "ListMonitoredResourceDescriptorsResponseOut": "_monitoring_31_ListMonitoredResourceDescriptorsResponseOut",
        "CriteriaIn": "_monitoring_32_CriteriaIn",
        "CriteriaOut": "_monitoring_33_CriteriaOut",
        "TimeSeriesDescriptorIn": "_monitoring_34_TimeSeriesDescriptorIn",
        "TimeSeriesDescriptorOut": "_monitoring_35_TimeSeriesDescriptorOut",
        "MeshIstioIn": "_monitoring_36_MeshIstioIn",
        "MeshIstioOut": "_monitoring_37_MeshIstioOut",
        "AlertStrategyIn": "_monitoring_38_AlertStrategyIn",
        "AlertStrategyOut": "_monitoring_39_AlertStrategyOut",
        "TypedValueIn": "_monitoring_40_TypedValueIn",
        "TypedValueOut": "_monitoring_41_TypedValueOut",
        "BasicSliIn": "_monitoring_42_BasicSliIn",
        "BasicSliOut": "_monitoring_43_BasicSliOut",
        "HttpCheckIn": "_monitoring_44_HttpCheckIn",
        "HttpCheckOut": "_monitoring_45_HttpCheckOut",
        "SourceContextIn": "_monitoring_46_SourceContextIn",
        "SourceContextOut": "_monitoring_47_SourceContextOut",
        "ServiceIn": "_monitoring_48_ServiceIn",
        "ServiceOut": "_monitoring_49_ServiceOut",
        "ListUptimeCheckConfigsResponseIn": "_monitoring_50_ListUptimeCheckConfigsResponseIn",
        "ListUptimeCheckConfigsResponseOut": "_monitoring_51_ListUptimeCheckConfigsResponseOut",
        "ListAlertPoliciesResponseIn": "_monitoring_52_ListAlertPoliciesResponseIn",
        "ListAlertPoliciesResponseOut": "_monitoring_53_ListAlertPoliciesResponseOut",
        "NotificationChannelIn": "_monitoring_54_NotificationChannelIn",
        "NotificationChannelOut": "_monitoring_55_NotificationChannelOut",
        "ForecastOptionsIn": "_monitoring_56_ForecastOptionsIn",
        "ForecastOptionsOut": "_monitoring_57_ForecastOptionsOut",
        "MonitoredResourceIn": "_monitoring_58_MonitoredResourceIn",
        "MonitoredResourceOut": "_monitoring_59_MonitoredResourceOut",
        "MetricRangeIn": "_monitoring_60_MetricRangeIn",
        "MetricRangeOut": "_monitoring_61_MetricRangeOut",
        "ServiceLevelObjectiveIn": "_monitoring_62_ServiceLevelObjectiveIn",
        "ServiceLevelObjectiveOut": "_monitoring_63_ServiceLevelObjectiveOut",
        "ExemplarIn": "_monitoring_64_ExemplarIn",
        "ExemplarOut": "_monitoring_65_ExemplarOut",
        "MetricAbsenceIn": "_monitoring_66_MetricAbsenceIn",
        "MetricAbsenceOut": "_monitoring_67_MetricAbsenceOut",
        "TypeIn": "_monitoring_68_TypeIn",
        "TypeOut": "_monitoring_69_TypeOut",
        "DistributionIn": "_monitoring_70_DistributionIn",
        "DistributionOut": "_monitoring_71_DistributionOut",
        "OperationMetadataIn": "_monitoring_72_OperationMetadataIn",
        "OperationMetadataOut": "_monitoring_73_OperationMetadataOut",
        "WindowsBasedSliIn": "_monitoring_74_WindowsBasedSliIn",
        "WindowsBasedSliOut": "_monitoring_75_WindowsBasedSliOut",
        "GkeNamespaceIn": "_monitoring_76_GkeNamespaceIn",
        "GkeNamespaceOut": "_monitoring_77_GkeNamespaceOut",
        "NotificationRateLimitIn": "_monitoring_78_NotificationRateLimitIn",
        "NotificationRateLimitOut": "_monitoring_79_NotificationRateLimitOut",
        "MonitoredResourceDescriptorIn": "_monitoring_80_MonitoredResourceDescriptorIn",
        "MonitoredResourceDescriptorOut": "_monitoring_81_MonitoredResourceDescriptorOut",
        "MonitoredResourceMetadataIn": "_monitoring_82_MonitoredResourceMetadataIn",
        "MonitoredResourceMetadataOut": "_monitoring_83_MonitoredResourceMetadataOut",
        "CreateTimeSeriesRequestIn": "_monitoring_84_CreateTimeSeriesRequestIn",
        "CreateTimeSeriesRequestOut": "_monitoring_85_CreateTimeSeriesRequestOut",
        "LogMatchIn": "_monitoring_86_LogMatchIn",
        "LogMatchOut": "_monitoring_87_LogMatchOut",
        "TimeSeriesIn": "_monitoring_88_TimeSeriesIn",
        "TimeSeriesOut": "_monitoring_89_TimeSeriesOut",
        "CloudEndpointsIn": "_monitoring_90_CloudEndpointsIn",
        "CloudEndpointsOut": "_monitoring_91_CloudEndpointsOut",
        "MetricDescriptorMetadataIn": "_monitoring_92_MetricDescriptorMetadataIn",
        "MetricDescriptorMetadataOut": "_monitoring_93_MetricDescriptorMetadataOut",
        "TimeSeriesDataIn": "_monitoring_94_TimeSeriesDataIn",
        "TimeSeriesDataOut": "_monitoring_95_TimeSeriesDataOut",
        "CreateCollectdTimeSeriesResponseIn": "_monitoring_96_CreateCollectdTimeSeriesResponseIn",
        "CreateCollectdTimeSeriesResponseOut": "_monitoring_97_CreateCollectdTimeSeriesResponseOut",
        "ListGroupMembersResponseIn": "_monitoring_98_ListGroupMembersResponseIn",
        "ListGroupMembersResponseOut": "_monitoring_99_ListGroupMembersResponseOut",
        "ResponseStatusCodeIn": "_monitoring_100_ResponseStatusCodeIn",
        "ResponseStatusCodeOut": "_monitoring_101_ResponseStatusCodeOut",
        "VerifyNotificationChannelRequestIn": "_monitoring_102_VerifyNotificationChannelRequestIn",
        "VerifyNotificationChannelRequestOut": "_monitoring_103_VerifyNotificationChannelRequestOut",
        "GkeServiceIn": "_monitoring_104_GkeServiceIn",
        "GkeServiceOut": "_monitoring_105_GkeServiceOut",
        "InternalCheckerIn": "_monitoring_106_InternalCheckerIn",
        "InternalCheckerOut": "_monitoring_107_InternalCheckerOut",
        "SendNotificationChannelVerificationCodeRequestIn": "_monitoring_108_SendNotificationChannelVerificationCodeRequestIn",
        "SendNotificationChannelVerificationCodeRequestOut": "_monitoring_109_SendNotificationChannelVerificationCodeRequestOut",
        "StatusIn": "_monitoring_110_StatusIn",
        "StatusOut": "_monitoring_111_StatusOut",
        "GroupIn": "_monitoring_112_GroupIn",
        "GroupOut": "_monitoring_113_GroupOut",
        "MetricDescriptorIn": "_monitoring_114_MetricDescriptorIn",
        "MetricDescriptorOut": "_monitoring_115_MetricDescriptorOut",
        "CreateCollectdTimeSeriesRequestIn": "_monitoring_116_CreateCollectdTimeSeriesRequestIn",
        "CreateCollectdTimeSeriesRequestOut": "_monitoring_117_CreateCollectdTimeSeriesRequestOut",
        "BucketOptionsIn": "_monitoring_118_BucketOptionsIn",
        "BucketOptionsOut": "_monitoring_119_BucketOptionsOut",
        "TcpCheckIn": "_monitoring_120_TcpCheckIn",
        "TcpCheckOut": "_monitoring_121_TcpCheckOut",
        "OptionIn": "_monitoring_122_OptionIn",
        "OptionOut": "_monitoring_123_OptionOut",
        "CustomIn": "_monitoring_124_CustomIn",
        "CustomOut": "_monitoring_125_CustomOut",
        "ListTimeSeriesResponseIn": "_monitoring_126_ListTimeSeriesResponseIn",
        "ListTimeSeriesResponseOut": "_monitoring_127_ListTimeSeriesResponseOut",
        "LabelDescriptorIn": "_monitoring_128_LabelDescriptorIn",
        "LabelDescriptorOut": "_monitoring_129_LabelDescriptorOut",
        "QueryTimeSeriesResponseIn": "_monitoring_130_QueryTimeSeriesResponseIn",
        "QueryTimeSeriesResponseOut": "_monitoring_131_QueryTimeSeriesResponseOut",
        "EmptyIn": "_monitoring_132_EmptyIn",
        "EmptyOut": "_monitoring_133_EmptyOut",
        "CollectdPayloadIn": "_monitoring_134_CollectdPayloadIn",
        "CollectdPayloadOut": "_monitoring_135_CollectdPayloadOut",
        "ListMetricDescriptorsResponseIn": "_monitoring_136_ListMetricDescriptorsResponseIn",
        "ListMetricDescriptorsResponseOut": "_monitoring_137_ListMetricDescriptorsResponseOut",
        "ListGroupsResponseIn": "_monitoring_138_ListGroupsResponseIn",
        "ListGroupsResponseOut": "_monitoring_139_ListGroupsResponseOut",
        "UptimeCheckIpIn": "_monitoring_140_UptimeCheckIpIn",
        "UptimeCheckIpOut": "_monitoring_141_UptimeCheckIpOut",
        "JsonPathMatcherIn": "_monitoring_142_JsonPathMatcherIn",
        "JsonPathMatcherOut": "_monitoring_143_JsonPathMatcherOut",
        "ErrorIn": "_monitoring_144_ErrorIn",
        "ErrorOut": "_monitoring_145_ErrorOut",
        "ListServiceLevelObjectivesResponseIn": "_monitoring_146_ListServiceLevelObjectivesResponseIn",
        "ListServiceLevelObjectivesResponseOut": "_monitoring_147_ListServiceLevelObjectivesResponseOut",
        "ConditionIn": "_monitoring_148_ConditionIn",
        "ConditionOut": "_monitoring_149_ConditionOut",
        "MetricIn": "_monitoring_150_MetricIn",
        "MetricOut": "_monitoring_151_MetricOut",
        "DistributionCutIn": "_monitoring_152_DistributionCutIn",
        "DistributionCutOut": "_monitoring_153_DistributionCutOut",
        "PerformanceThresholdIn": "_monitoring_154_PerformanceThresholdIn",
        "PerformanceThresholdOut": "_monitoring_155_PerformanceThresholdOut",
        "ClusterIstioIn": "_monitoring_156_ClusterIstioIn",
        "ClusterIstioOut": "_monitoring_157_ClusterIstioOut",
        "ServiceLevelIndicatorIn": "_monitoring_158_ServiceLevelIndicatorIn",
        "ServiceLevelIndicatorOut": "_monitoring_159_ServiceLevelIndicatorOut",
        "AggregationIn": "_monitoring_160_AggregationIn",
        "AggregationOut": "_monitoring_161_AggregationOut",
        "LabelValueIn": "_monitoring_162_LabelValueIn",
        "LabelValueOut": "_monitoring_163_LabelValueOut",
        "ValueDescriptorIn": "_monitoring_164_ValueDescriptorIn",
        "ValueDescriptorOut": "_monitoring_165_ValueDescriptorOut",
        "AppEngineIn": "_monitoring_166_AppEngineIn",
        "AppEngineOut": "_monitoring_167_AppEngineOut",
        "ContentMatcherIn": "_monitoring_168_ContentMatcherIn",
        "ContentMatcherOut": "_monitoring_169_ContentMatcherOut",
        "TimeSeriesRatioIn": "_monitoring_170_TimeSeriesRatioIn",
        "TimeSeriesRatioOut": "_monitoring_171_TimeSeriesRatioOut",
        "GoogleMonitoringV3RangeIn": "_monitoring_172_GoogleMonitoringV3RangeIn",
        "GoogleMonitoringV3RangeOut": "_monitoring_173_GoogleMonitoringV3RangeOut",
        "RangeIn": "_monitoring_174_RangeIn",
        "RangeOut": "_monitoring_175_RangeOut",
        "PointDataIn": "_monitoring_176_PointDataIn",
        "PointDataOut": "_monitoring_177_PointDataOut",
        "GetNotificationChannelVerificationCodeResponseIn": "_monitoring_178_GetNotificationChannelVerificationCodeResponseIn",
        "GetNotificationChannelVerificationCodeResponseOut": "_monitoring_179_GetNotificationChannelVerificationCodeResponseOut",
        "GkeWorkloadIn": "_monitoring_180_GkeWorkloadIn",
        "GkeWorkloadOut": "_monitoring_181_GkeWorkloadOut",
        "AvailabilityCriteriaIn": "_monitoring_182_AvailabilityCriteriaIn",
        "AvailabilityCriteriaOut": "_monitoring_183_AvailabilityCriteriaOut",
        "TimeIntervalIn": "_monitoring_184_TimeIntervalIn",
        "TimeIntervalOut": "_monitoring_185_TimeIntervalOut",
        "PointIn": "_monitoring_186_PointIn",
        "PointOut": "_monitoring_187_PointOut",
        "ResourceGroupIn": "_monitoring_188_ResourceGroupIn",
        "ResourceGroupOut": "_monitoring_189_ResourceGroupOut",
        "LatencyCriteriaIn": "_monitoring_190_LatencyCriteriaIn",
        "LatencyCriteriaOut": "_monitoring_191_LatencyCriteriaOut",
        "NotificationChannelDescriptorIn": "_monitoring_192_NotificationChannelDescriptorIn",
        "NotificationChannelDescriptorOut": "_monitoring_193_NotificationChannelDescriptorOut",
        "AlertPolicyIn": "_monitoring_194_AlertPolicyIn",
        "AlertPolicyOut": "_monitoring_195_AlertPolicyOut",
        "MetricThresholdIn": "_monitoring_196_MetricThresholdIn",
        "MetricThresholdOut": "_monitoring_197_MetricThresholdOut",
        "LinearIn": "_monitoring_198_LinearIn",
        "LinearOut": "_monitoring_199_LinearOut",
        "TelemetryIn": "_monitoring_200_TelemetryIn",
        "TelemetryOut": "_monitoring_201_TelemetryOut",
        "ExponentialIn": "_monitoring_202_ExponentialIn",
        "ExponentialOut": "_monitoring_203_ExponentialOut",
        "ExplicitIn": "_monitoring_204_ExplicitIn",
        "ExplicitOut": "_monitoring_205_ExplicitOut",
        "DroppedLabelsIn": "_monitoring_206_DroppedLabelsIn",
        "DroppedLabelsOut": "_monitoring_207_DroppedLabelsOut",
        "BasicAuthenticationIn": "_monitoring_208_BasicAuthenticationIn",
        "BasicAuthenticationOut": "_monitoring_209_BasicAuthenticationOut",
        "RequestBasedSliIn": "_monitoring_210_RequestBasedSliIn",
        "RequestBasedSliOut": "_monitoring_211_RequestBasedSliOut",
        "QueryTimeSeriesRequestIn": "_monitoring_212_QueryTimeSeriesRequestIn",
        "QueryTimeSeriesRequestOut": "_monitoring_213_QueryTimeSeriesRequestOut",
        "CreateTimeSeriesSummaryIn": "_monitoring_214_CreateTimeSeriesSummaryIn",
        "CreateTimeSeriesSummaryOut": "_monitoring_215_CreateTimeSeriesSummaryOut",
        "TriggerIn": "_monitoring_216_TriggerIn",
        "TriggerOut": "_monitoring_217_TriggerOut",
        "PingConfigIn": "_monitoring_218_PingConfigIn",
        "PingConfigOut": "_monitoring_219_PingConfigOut",
        "GetNotificationChannelVerificationCodeRequestIn": "_monitoring_220_GetNotificationChannelVerificationCodeRequestIn",
        "GetNotificationChannelVerificationCodeRequestOut": "_monitoring_221_GetNotificationChannelVerificationCodeRequestOut",
        "SpanContextIn": "_monitoring_222_SpanContextIn",
        "SpanContextOut": "_monitoring_223_SpanContextOut",
        "IstioCanonicalServiceIn": "_monitoring_224_IstioCanonicalServiceIn",
        "IstioCanonicalServiceOut": "_monitoring_225_IstioCanonicalServiceOut",
        "ListNotificationChannelsResponseIn": "_monitoring_226_ListNotificationChannelsResponseIn",
        "ListNotificationChannelsResponseOut": "_monitoring_227_ListNotificationChannelsResponseOut",
        "UptimeCheckConfigIn": "_monitoring_228_UptimeCheckConfigIn",
        "UptimeCheckConfigOut": "_monitoring_229_UptimeCheckConfigOut",
        "CollectdValueErrorIn": "_monitoring_230_CollectdValueErrorIn",
        "CollectdValueErrorOut": "_monitoring_231_CollectdValueErrorOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["MonitoringQueryLanguageConditionIn"] = t.struct(
        {
            "evaluationMissingData": t.string().optional(),
            "duration": t.string().optional(),
            "query": t.string().optional(),
            "trigger": t.proxy(renames["TriggerIn"]).optional(),
        }
    ).named(renames["MonitoringQueryLanguageConditionIn"])
    types["MonitoringQueryLanguageConditionOut"] = t.struct(
        {
            "evaluationMissingData": t.string().optional(),
            "duration": t.string().optional(),
            "query": t.string().optional(),
            "trigger": t.proxy(renames["TriggerOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoringQueryLanguageConditionOut"])
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
    types["FieldIn"] = t.struct(
        {
            "defaultValue": t.string().optional(),
            "number": t.integer().optional(),
            "name": t.string().optional(),
            "cardinality": t.string().optional(),
            "jsonName": t.string().optional(),
            "oneofIndex": t.integer().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "packed": t.boolean().optional(),
            "typeUrl": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "defaultValue": t.string().optional(),
            "number": t.integer().optional(),
            "name": t.string().optional(),
            "cardinality": t.string().optional(),
            "jsonName": t.string().optional(),
            "oneofIndex": t.integer().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "packed": t.boolean().optional(),
            "typeUrl": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
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
    types["MutationRecordIn"] = t.struct(
        {"mutatedBy": t.string().optional(), "mutateTime": t.string().optional()}
    ).named(renames["MutationRecordIn"])
    types["MutationRecordOut"] = t.struct(
        {
            "mutatedBy": t.string().optional(),
            "mutateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MutationRecordOut"])
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
    types["SnoozeIn"] = t.struct(
        {
            "displayName": t.string(),
            "name": t.string(),
            "interval": t.proxy(renames["TimeIntervalIn"]),
            "criteria": t.proxy(renames["CriteriaIn"]),
        }
    ).named(renames["SnoozeIn"])
    types["SnoozeOut"] = t.struct(
        {
            "displayName": t.string(),
            "name": t.string(),
            "interval": t.proxy(renames["TimeIntervalOut"]),
            "criteria": t.proxy(renames["CriteriaOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnoozeOut"])
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
    types["CriteriaIn"] = t.struct({"policies": t.array(t.string()).optional()}).named(
        renames["CriteriaIn"]
    )
    types["CriteriaOut"] = t.struct(
        {
            "policies": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CriteriaOut"])
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
    types["MeshIstioIn"] = t.struct(
        {
            "serviceName": t.string().optional(),
            "serviceNamespace": t.string().optional(),
            "meshUid": t.string().optional(),
        }
    ).named(renames["MeshIstioIn"])
    types["MeshIstioOut"] = t.struct(
        {
            "serviceName": t.string().optional(),
            "serviceNamespace": t.string().optional(),
            "meshUid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MeshIstioOut"])
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
    types["TypedValueIn"] = t.struct(
        {
            "int64Value": t.string().optional(),
            "doubleValue": t.number().optional(),
            "stringValue": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "distributionValue": t.proxy(renames["DistributionIn"]).optional(),
        }
    ).named(renames["TypedValueIn"])
    types["TypedValueOut"] = t.struct(
        {
            "int64Value": t.string().optional(),
            "doubleValue": t.number().optional(),
            "stringValue": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "distributionValue": t.proxy(renames["DistributionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypedValueOut"])
    types["BasicSliIn"] = t.struct(
        {
            "latency": t.proxy(renames["LatencyCriteriaIn"]).optional(),
            "version": t.array(t.string()).optional(),
            "method": t.array(t.string()).optional(),
            "location": t.array(t.string()).optional(),
            "availability": t.proxy(renames["AvailabilityCriteriaIn"]).optional(),
        }
    ).named(renames["BasicSliIn"])
    types["BasicSliOut"] = t.struct(
        {
            "latency": t.proxy(renames["LatencyCriteriaOut"]).optional(),
            "version": t.array(t.string()).optional(),
            "method": t.array(t.string()).optional(),
            "location": t.array(t.string()).optional(),
            "availability": t.proxy(renames["AvailabilityCriteriaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicSliOut"])
    types["HttpCheckIn"] = t.struct(
        {
            "contentType": t.string().optional(),
            "useSsl": t.boolean().optional(),
            "validateSsl": t.boolean().optional(),
            "port": t.integer().optional(),
            "requestMethod": t.string().optional(),
            "pingConfig": t.proxy(renames["PingConfigIn"]).optional(),
            "customContentType": t.string().optional(),
            "path": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "authInfo": t.proxy(renames["BasicAuthenticationIn"]).optional(),
            "maskHeaders": t.boolean().optional(),
            "body": t.string().optional(),
            "acceptedResponseStatusCodes": t.array(
                t.proxy(renames["ResponseStatusCodeIn"])
            ).optional(),
        }
    ).named(renames["HttpCheckIn"])
    types["HttpCheckOut"] = t.struct(
        {
            "contentType": t.string().optional(),
            "useSsl": t.boolean().optional(),
            "validateSsl": t.boolean().optional(),
            "port": t.integer().optional(),
            "requestMethod": t.string().optional(),
            "pingConfig": t.proxy(renames["PingConfigOut"]).optional(),
            "customContentType": t.string().optional(),
            "path": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "authInfo": t.proxy(renames["BasicAuthenticationOut"]).optional(),
            "maskHeaders": t.boolean().optional(),
            "body": t.string().optional(),
            "acceptedResponseStatusCodes": t.array(
                t.proxy(renames["ResponseStatusCodeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpCheckOut"])
    types["SourceContextIn"] = t.struct({"fileName": t.string().optional()}).named(
        renames["SourceContextIn"]
    )
    types["SourceContextOut"] = t.struct(
        {
            "fileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceContextOut"])
    types["ServiceIn"] = t.struct(
        {
            "telemetry": t.proxy(renames["TelemetryIn"]).optional(),
            "istioCanonicalService": t.proxy(
                renames["IstioCanonicalServiceIn"]
            ).optional(),
            "cloudRun": t.proxy(renames["CloudRunIn"]).optional(),
            "gkeWorkload": t.proxy(renames["GkeWorkloadIn"]).optional(),
            "custom": t.proxy(renames["CustomIn"]).optional(),
            "gkeService": t.proxy(renames["GkeServiceIn"]).optional(),
            "meshIstio": t.proxy(renames["MeshIstioIn"]).optional(),
            "displayName": t.string().optional(),
            "clusterIstio": t.proxy(renames["ClusterIstioIn"]).optional(),
            "cloudEndpoints": t.proxy(renames["CloudEndpointsIn"]).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "basicService": t.proxy(renames["BasicServiceIn"]).optional(),
            "gkeNamespace": t.proxy(renames["GkeNamespaceIn"]).optional(),
            "appEngine": t.proxy(renames["AppEngineIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "telemetry": t.proxy(renames["TelemetryOut"]).optional(),
            "istioCanonicalService": t.proxy(
                renames["IstioCanonicalServiceOut"]
            ).optional(),
            "cloudRun": t.proxy(renames["CloudRunOut"]).optional(),
            "gkeWorkload": t.proxy(renames["GkeWorkloadOut"]).optional(),
            "custom": t.proxy(renames["CustomOut"]).optional(),
            "gkeService": t.proxy(renames["GkeServiceOut"]).optional(),
            "meshIstio": t.proxy(renames["MeshIstioOut"]).optional(),
            "displayName": t.string().optional(),
            "clusterIstio": t.proxy(renames["ClusterIstioOut"]).optional(),
            "cloudEndpoints": t.proxy(renames["CloudEndpointsOut"]).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "basicService": t.proxy(renames["BasicServiceOut"]).optional(),
            "gkeNamespace": t.proxy(renames["GkeNamespaceOut"]).optional(),
            "appEngine": t.proxy(renames["AppEngineOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
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
    types["ListAlertPoliciesResponseIn"] = t.struct(
        {
            "alertPolicies": t.array(t.proxy(renames["AlertPolicyIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["ListAlertPoliciesResponseIn"])
    types["ListAlertPoliciesResponseOut"] = t.struct(
        {
            "alertPolicies": t.array(t.proxy(renames["AlertPolicyOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAlertPoliciesResponseOut"])
    types["NotificationChannelIn"] = t.struct(
        {
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "verificationStatus": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "creationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
            "enabled": t.boolean().optional(),
            "mutationRecords": t.array(t.proxy(renames["MutationRecordIn"])).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["NotificationChannelIn"])
    types["NotificationChannelOut"] = t.struct(
        {
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "verificationStatus": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "creationRecord": t.proxy(renames["MutationRecordOut"]).optional(),
            "enabled": t.boolean().optional(),
            "mutationRecords": t.array(
                t.proxy(renames["MutationRecordOut"])
            ).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationChannelOut"])
    types["ForecastOptionsIn"] = t.struct({"forecastHorizon": t.string()}).named(
        renames["ForecastOptionsIn"]
    )
    types["ForecastOptionsOut"] = t.struct(
        {
            "forecastHorizon": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ForecastOptionsOut"])
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
    types["ServiceLevelObjectiveIn"] = t.struct(
        {
            "goal": t.number().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "rollingPeriod": t.string().optional(),
            "serviceLevelIndicator": t.proxy(
                renames["ServiceLevelIndicatorIn"]
            ).optional(),
            "calendarPeriod": t.string().optional(),
        }
    ).named(renames["ServiceLevelObjectiveIn"])
    types["ServiceLevelObjectiveOut"] = t.struct(
        {
            "goal": t.number().optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "rollingPeriod": t.string().optional(),
            "serviceLevelIndicator": t.proxy(
                renames["ServiceLevelIndicatorOut"]
            ).optional(),
            "calendarPeriod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceLevelObjectiveOut"])
    types["ExemplarIn"] = t.struct(
        {
            "timestamp": t.string().optional(),
            "value": t.number().optional(),
            "attachments": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["ExemplarIn"])
    types["ExemplarOut"] = t.struct(
        {
            "timestamp": t.string().optional(),
            "value": t.number().optional(),
            "attachments": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExemplarOut"])
    types["MetricAbsenceIn"] = t.struct(
        {
            "duration": t.string().optional(),
            "aggregations": t.array(t.proxy(renames["AggregationIn"])).optional(),
            "trigger": t.proxy(renames["TriggerIn"]).optional(),
            "filter": t.string(),
        }
    ).named(renames["MetricAbsenceIn"])
    types["MetricAbsenceOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "aggregations": t.array(t.proxy(renames["AggregationOut"])).optional(),
            "trigger": t.proxy(renames["TriggerOut"]).optional(),
            "filter": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricAbsenceOut"])
    types["TypeIn"] = t.struct(
        {
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "name": t.string().optional(),
            "oneofs": t.array(t.string()).optional(),
            "edition": t.string().optional(),
            "syntax": t.string().optional(),
            "fields": t.array(t.proxy(renames["FieldIn"])).optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "name": t.string().optional(),
            "oneofs": t.array(t.string()).optional(),
            "edition": t.string().optional(),
            "syntax": t.string().optional(),
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
    types["DistributionIn"] = t.struct(
        {
            "count": t.string().optional(),
            "bucketOptions": t.proxy(renames["BucketOptionsIn"]),
            "bucketCounts": t.array(t.string()),
            "range": t.proxy(renames["RangeIn"]).optional(),
            "exemplars": t.array(t.proxy(renames["ExemplarIn"])).optional(),
            "sumOfSquaredDeviation": t.number().optional(),
            "mean": t.number().optional(),
        }
    ).named(renames["DistributionIn"])
    types["DistributionOut"] = t.struct(
        {
            "count": t.string().optional(),
            "bucketOptions": t.proxy(renames["BucketOptionsOut"]),
            "bucketCounts": t.array(t.string()),
            "range": t.proxy(renames["RangeOut"]).optional(),
            "exemplars": t.array(t.proxy(renames["ExemplarOut"])).optional(),
            "sumOfSquaredDeviation": t.number().optional(),
            "mean": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DistributionOut"])
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
    types["WindowsBasedSliIn"] = t.struct(
        {
            "metricMeanInRange": t.proxy(renames["MetricRangeIn"]).optional(),
            "goodTotalRatioThreshold": t.proxy(
                renames["PerformanceThresholdIn"]
            ).optional(),
            "windowPeriod": t.string().optional(),
            "goodBadMetricFilter": t.string().optional(),
            "metricSumInRange": t.proxy(renames["MetricRangeIn"]).optional(),
        }
    ).named(renames["WindowsBasedSliIn"])
    types["WindowsBasedSliOut"] = t.struct(
        {
            "metricMeanInRange": t.proxy(renames["MetricRangeOut"]).optional(),
            "goodTotalRatioThreshold": t.proxy(
                renames["PerformanceThresholdOut"]
            ).optional(),
            "windowPeriod": t.string().optional(),
            "goodBadMetricFilter": t.string().optional(),
            "metricSumInRange": t.proxy(renames["MetricRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsBasedSliOut"])
    types["GkeNamespaceIn"] = t.struct(
        {
            "clusterName": t.string().optional(),
            "namespaceName": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["GkeNamespaceIn"])
    types["GkeNamespaceOut"] = t.struct(
        {
            "clusterName": t.string().optional(),
            "namespaceName": t.string().optional(),
            "location": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeNamespaceOut"])
    types["NotificationRateLimitIn"] = t.struct(
        {"period": t.string().optional()}
    ).named(renames["NotificationRateLimitIn"])
    types["NotificationRateLimitOut"] = t.struct(
        {
            "period": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationRateLimitOut"])
    types["MonitoredResourceDescriptorIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "launchStage": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])),
            "displayName": t.string().optional(),
            "type": t.string(),
        }
    ).named(renames["MonitoredResourceDescriptorIn"])
    types["MonitoredResourceDescriptorOut"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "launchStage": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])),
            "displayName": t.string().optional(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceDescriptorOut"])
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
    types["CreateTimeSeriesRequestIn"] = t.struct(
        {"timeSeries": t.array(t.proxy(renames["TimeSeriesIn"]))}
    ).named(renames["CreateTimeSeriesRequestIn"])
    types["CreateTimeSeriesRequestOut"] = t.struct(
        {
            "timeSeries": t.array(t.proxy(renames["TimeSeriesOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateTimeSeriesRequestOut"])
    types["LogMatchIn"] = t.struct(
        {
            "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
            "filter": t.string(),
        }
    ).named(renames["LogMatchIn"])
    types["LogMatchOut"] = t.struct(
        {
            "labelExtractors": t.struct({"_": t.string().optional()}).optional(),
            "filter": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogMatchOut"])
    types["TimeSeriesIn"] = t.struct(
        {
            "points": t.array(t.proxy(renames["PointIn"])).optional(),
            "unit": t.string().optional(),
            "valueType": t.string().optional(),
            "metricKind": t.string().optional(),
            "metadata": t.proxy(renames["MonitoredResourceMetadataIn"]).optional(),
            "resource": t.proxy(renames["MonitoredResourceIn"]).optional(),
            "metric": t.proxy(renames["MetricIn"]).optional(),
        }
    ).named(renames["TimeSeriesIn"])
    types["TimeSeriesOut"] = t.struct(
        {
            "points": t.array(t.proxy(renames["PointOut"])).optional(),
            "unit": t.string().optional(),
            "valueType": t.string().optional(),
            "metricKind": t.string().optional(),
            "metadata": t.proxy(renames["MonitoredResourceMetadataOut"]).optional(),
            "resource": t.proxy(renames["MonitoredResourceOut"]).optional(),
            "metric": t.proxy(renames["MetricOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeSeriesOut"])
    types["CloudEndpointsIn"] = t.struct({"service": t.string().optional()}).named(
        renames["CloudEndpointsIn"]
    )
    types["CloudEndpointsOut"] = t.struct(
        {
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudEndpointsOut"])
    types["MetricDescriptorMetadataIn"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "samplePeriod": t.string().optional(),
            "ingestDelay": t.string().optional(),
        }
    ).named(renames["MetricDescriptorMetadataIn"])
    types["MetricDescriptorMetadataOut"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "samplePeriod": t.string().optional(),
            "ingestDelay": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorMetadataOut"])
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
    types["VerifyNotificationChannelRequestIn"] = t.struct({"code": t.string()}).named(
        renames["VerifyNotificationChannelRequestIn"]
    )
    types["VerifyNotificationChannelRequestOut"] = t.struct(
        {"code": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VerifyNotificationChannelRequestOut"])
    types["GkeServiceIn"] = t.struct(
        {
            "serviceName": t.string().optional(),
            "clusterName": t.string().optional(),
            "namespaceName": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["GkeServiceIn"])
    types["GkeServiceOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "serviceName": t.string().optional(),
            "clusterName": t.string().optional(),
            "namespaceName": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeServiceOut"])
    types["InternalCheckerIn"] = t.struct(
        {
            "state": t.string().optional(),
            "gcpZone": t.string().optional(),
            "name": t.string().optional(),
            "peerProjectId": t.string().optional(),
            "displayName": t.string().optional(),
            "network": t.string().optional(),
        }
    ).named(renames["InternalCheckerIn"])
    types["InternalCheckerOut"] = t.struct(
        {
            "state": t.string().optional(),
            "gcpZone": t.string().optional(),
            "name": t.string().optional(),
            "peerProjectId": t.string().optional(),
            "displayName": t.string().optional(),
            "network": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InternalCheckerOut"])
    types["SendNotificationChannelVerificationCodeRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SendNotificationChannelVerificationCodeRequestIn"])
    types["SendNotificationChannelVerificationCodeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SendNotificationChannelVerificationCodeRequestOut"])
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
    types["GroupIn"] = t.struct(
        {
            "parentName": t.string().optional(),
            "name": t.string().optional(),
            "isCluster": t.boolean().optional(),
            "displayName": t.string().optional(),
            "filter": t.string().optional(),
        }
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "parentName": t.string().optional(),
            "name": t.string().optional(),
            "isCluster": t.boolean().optional(),
            "displayName": t.string().optional(),
            "filter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
    types["MetricDescriptorIn"] = t.struct(
        {
            "name": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "unit": t.string().optional(),
            "displayName": t.string().optional(),
            "metricKind": t.string().optional(),
            "launchStage": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
            "description": t.string().optional(),
            "valueType": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["MetricDescriptorIn"])
    types["MetricDescriptorOut"] = t.struct(
        {
            "name": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "unit": t.string().optional(),
            "displayName": t.string().optional(),
            "metricKind": t.string().optional(),
            "launchStage": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataOut"]).optional(),
            "description": t.string().optional(),
            "valueType": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorOut"])
    types["CreateCollectdTimeSeriesRequestIn"] = t.struct(
        {
            "collectdVersion": t.string().optional(),
            "resource": t.proxy(renames["MonitoredResourceIn"]).optional(),
            "collectdPayloads": t.array(
                t.proxy(renames["CollectdPayloadIn"])
            ).optional(),
        }
    ).named(renames["CreateCollectdTimeSeriesRequestIn"])
    types["CreateCollectdTimeSeriesRequestOut"] = t.struct(
        {
            "collectdVersion": t.string().optional(),
            "resource": t.proxy(renames["MonitoredResourceOut"]).optional(),
            "collectdPayloads": t.array(
                t.proxy(renames["CollectdPayloadOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateCollectdTimeSeriesRequestOut"])
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
    types["TcpCheckIn"] = t.struct(
        {
            "port": t.integer().optional(),
            "pingConfig": t.proxy(renames["PingConfigIn"]).optional(),
        }
    ).named(renames["TcpCheckIn"])
    types["TcpCheckOut"] = t.struct(
        {
            "port": t.integer().optional(),
            "pingConfig": t.proxy(renames["PingConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TcpCheckOut"])
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
    types["CustomIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CustomIn"]
    )
    types["CustomOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CustomOut"])
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
    types["QueryTimeSeriesResponseIn"] = t.struct(
        {
            "timeSeriesDescriptor": t.proxy(
                renames["TimeSeriesDescriptorIn"]
            ).optional(),
            "nextPageToken": t.string().optional(),
            "partialErrors": t.array(t.proxy(renames["StatusIn"])).optional(),
            "timeSeriesData": t.array(t.proxy(renames["TimeSeriesDataIn"])).optional(),
        }
    ).named(renames["QueryTimeSeriesResponseIn"])
    types["QueryTimeSeriesResponseOut"] = t.struct(
        {
            "timeSeriesDescriptor": t.proxy(
                renames["TimeSeriesDescriptorOut"]
            ).optional(),
            "nextPageToken": t.string().optional(),
            "partialErrors": t.array(t.proxy(renames["StatusOut"])).optional(),
            "timeSeriesData": t.array(t.proxy(renames["TimeSeriesDataOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryTimeSeriesResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["CollectdPayloadIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "typeInstance": t.string().optional(),
            "plugin": t.string().optional(),
            "pluginInstance": t.string().optional(),
            "type": t.string().optional(),
            "values": t.array(t.proxy(renames["CollectdValueIn"])).optional(),
        }
    ).named(renames["CollectdPayloadIn"])
    types["CollectdPayloadOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "typeInstance": t.string().optional(),
            "plugin": t.string().optional(),
            "pluginInstance": t.string().optional(),
            "type": t.string().optional(),
            "values": t.array(t.proxy(renames["CollectdValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CollectdPayloadOut"])
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
    types["ConditionIn"] = t.struct(
        {
            "conditionMatchedLog": t.proxy(renames["LogMatchIn"]).optional(),
            "name": t.string(),
            "conditionAbsent": t.proxy(renames["MetricAbsenceIn"]).optional(),
            "conditionThreshold": t.proxy(renames["MetricThresholdIn"]).optional(),
            "displayName": t.string().optional(),
            "conditionMonitoringQueryLanguage": t.proxy(
                renames["MonitoringQueryLanguageConditionIn"]
            ).optional(),
        }
    ).named(renames["ConditionIn"])
    types["ConditionOut"] = t.struct(
        {
            "conditionMatchedLog": t.proxy(renames["LogMatchOut"]).optional(),
            "name": t.string(),
            "conditionAbsent": t.proxy(renames["MetricAbsenceOut"]).optional(),
            "conditionThreshold": t.proxy(renames["MetricThresholdOut"]).optional(),
            "displayName": t.string().optional(),
            "conditionMonitoringQueryLanguage": t.proxy(
                renames["MonitoringQueryLanguageConditionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionOut"])
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
            "basicSliPerformance": t.proxy(renames["BasicSliIn"]).optional(),
            "performance": t.proxy(renames["RequestBasedSliIn"]).optional(),
            "threshold": t.number().optional(),
        }
    ).named(renames["PerformanceThresholdIn"])
    types["PerformanceThresholdOut"] = t.struct(
        {
            "basicSliPerformance": t.proxy(renames["BasicSliOut"]).optional(),
            "performance": t.proxy(renames["RequestBasedSliOut"]).optional(),
            "threshold": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerformanceThresholdOut"])
    types["ClusterIstioIn"] = t.struct(
        {
            "location": t.string().optional(),
            "serviceName": t.string().optional(),
            "clusterName": t.string().optional(),
            "serviceNamespace": t.string().optional(),
        }
    ).named(renames["ClusterIstioIn"])
    types["ClusterIstioOut"] = t.struct(
        {
            "location": t.string().optional(),
            "serviceName": t.string().optional(),
            "clusterName": t.string().optional(),
            "serviceNamespace": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterIstioOut"])
    types["ServiceLevelIndicatorIn"] = t.struct(
        {
            "windowsBased": t.proxy(renames["WindowsBasedSliIn"]).optional(),
            "requestBased": t.proxy(renames["RequestBasedSliIn"]).optional(),
            "basicSli": t.proxy(renames["BasicSliIn"]).optional(),
        }
    ).named(renames["ServiceLevelIndicatorIn"])
    types["ServiceLevelIndicatorOut"] = t.struct(
        {
            "windowsBased": t.proxy(renames["WindowsBasedSliOut"]).optional(),
            "requestBased": t.proxy(renames["RequestBasedSliOut"]).optional(),
            "basicSli": t.proxy(renames["BasicSliOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceLevelIndicatorOut"])
    types["AggregationIn"] = t.struct(
        {
            "crossSeriesReducer": t.string().optional(),
            "perSeriesAligner": t.string().optional(),
            "alignmentPeriod": t.string().optional(),
            "groupByFields": t.array(t.string()).optional(),
        }
    ).named(renames["AggregationIn"])
    types["AggregationOut"] = t.struct(
        {
            "crossSeriesReducer": t.string().optional(),
            "perSeriesAligner": t.string().optional(),
            "alignmentPeriod": t.string().optional(),
            "groupByFields": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationOut"])
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
    types["AppEngineIn"] = t.struct({"moduleId": t.string().optional()}).named(
        renames["AppEngineIn"]
    )
    types["AppEngineOut"] = t.struct(
        {
            "moduleId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEngineOut"])
    types["ContentMatcherIn"] = t.struct(
        {
            "matcher": t.string().optional(),
            "content": t.string().optional(),
            "jsonPathMatcher": t.proxy(renames["JsonPathMatcherIn"]).optional(),
        }
    ).named(renames["ContentMatcherIn"])
    types["ContentMatcherOut"] = t.struct(
        {
            "matcher": t.string().optional(),
            "content": t.string().optional(),
            "jsonPathMatcher": t.proxy(renames["JsonPathMatcherOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentMatcherOut"])
    types["TimeSeriesRatioIn"] = t.struct(
        {
            "goodServiceFilter": t.string().optional(),
            "badServiceFilter": t.string().optional(),
            "totalServiceFilter": t.string().optional(),
        }
    ).named(renames["TimeSeriesRatioIn"])
    types["TimeSeriesRatioOut"] = t.struct(
        {
            "goodServiceFilter": t.string().optional(),
            "badServiceFilter": t.string().optional(),
            "totalServiceFilter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeSeriesRatioOut"])
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
    types["GkeWorkloadIn"] = t.struct(
        {
            "clusterName": t.string().optional(),
            "topLevelControllerName": t.string().optional(),
            "namespaceName": t.string().optional(),
            "location": t.string().optional(),
            "topLevelControllerType": t.string().optional(),
        }
    ).named(renames["GkeWorkloadIn"])
    types["GkeWorkloadOut"] = t.struct(
        {
            "clusterName": t.string().optional(),
            "topLevelControllerName": t.string().optional(),
            "namespaceName": t.string().optional(),
            "location": t.string().optional(),
            "projectId": t.string().optional(),
            "topLevelControllerType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeWorkloadOut"])
    types["AvailabilityCriteriaIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AvailabilityCriteriaIn"]
    )
    types["AvailabilityCriteriaOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AvailabilityCriteriaOut"])
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
    types["LatencyCriteriaIn"] = t.struct({"threshold": t.string().optional()}).named(
        renames["LatencyCriteriaIn"]
    )
    types["LatencyCriteriaOut"] = t.struct(
        {
            "threshold": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LatencyCriteriaOut"])
    types["NotificationChannelDescriptorIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "type": t.string().optional(),
            "supportedTiers": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "launchStage": t.string().optional(),
        }
    ).named(renames["NotificationChannelDescriptorIn"])
    types["NotificationChannelDescriptorOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "type": t.string().optional(),
            "supportedTiers": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "launchStage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationChannelDescriptorOut"])
    types["AlertPolicyIn"] = t.struct(
        {
            "mutationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "alertStrategy": t.proxy(renames["AlertStrategyIn"]).optional(),
            "conditions": t.array(t.proxy(renames["ConditionIn"])).optional(),
            "validity": t.proxy(renames["StatusIn"]).optional(),
            "creationRecord": t.proxy(renames["MutationRecordIn"]).optional(),
            "name": t.string(),
            "notificationChannels": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "documentation": t.proxy(renames["DocumentationIn"]).optional(),
            "enabled": t.boolean().optional(),
            "combiner": t.string().optional(),
        }
    ).named(renames["AlertPolicyIn"])
    types["AlertPolicyOut"] = t.struct(
        {
            "mutationRecord": t.proxy(renames["MutationRecordOut"]).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "alertStrategy": t.proxy(renames["AlertStrategyOut"]).optional(),
            "conditions": t.array(t.proxy(renames["ConditionOut"])).optional(),
            "validity": t.proxy(renames["StatusOut"]).optional(),
            "creationRecord": t.proxy(renames["MutationRecordOut"]).optional(),
            "name": t.string(),
            "notificationChannels": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "documentation": t.proxy(renames["DocumentationOut"]).optional(),
            "enabled": t.boolean().optional(),
            "combiner": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlertPolicyOut"])
    types["MetricThresholdIn"] = t.struct(
        {
            "denominatorFilter": t.string().optional(),
            "evaluationMissingData": t.string().optional(),
            "trigger": t.proxy(renames["TriggerIn"]).optional(),
            "duration": t.string().optional(),
            "denominatorAggregations": t.array(
                t.proxy(renames["AggregationIn"])
            ).optional(),
            "thresholdValue": t.number().optional(),
            "forecastOptions": t.proxy(renames["ForecastOptionsIn"]).optional(),
            "comparison": t.string().optional(),
            "aggregations": t.array(t.proxy(renames["AggregationIn"])).optional(),
            "filter": t.string(),
        }
    ).named(renames["MetricThresholdIn"])
    types["MetricThresholdOut"] = t.struct(
        {
            "denominatorFilter": t.string().optional(),
            "evaluationMissingData": t.string().optional(),
            "trigger": t.proxy(renames["TriggerOut"]).optional(),
            "duration": t.string().optional(),
            "denominatorAggregations": t.array(
                t.proxy(renames["AggregationOut"])
            ).optional(),
            "thresholdValue": t.number().optional(),
            "forecastOptions": t.proxy(renames["ForecastOptionsOut"]).optional(),
            "comparison": t.string().optional(),
            "aggregations": t.array(t.proxy(renames["AggregationOut"])).optional(),
            "filter": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricThresholdOut"])
    types["LinearIn"] = t.struct(
        {
            "offset": t.number().optional(),
            "width": t.number().optional(),
            "numFiniteBuckets": t.integer().optional(),
        }
    ).named(renames["LinearIn"])
    types["LinearOut"] = t.struct(
        {
            "offset": t.number().optional(),
            "width": t.number().optional(),
            "numFiniteBuckets": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinearOut"])
    types["TelemetryIn"] = t.struct({"resourceName": t.string().optional()}).named(
        renames["TelemetryIn"]
    )
    types["TelemetryOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TelemetryOut"])
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
    types["ExplicitIn"] = t.struct({"bounds": t.array(t.number()).optional()}).named(
        renames["ExplicitIn"]
    )
    types["ExplicitOut"] = t.struct(
        {
            "bounds": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExplicitOut"])
    types["DroppedLabelsIn"] = t.struct(
        {"label": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["DroppedLabelsIn"])
    types["DroppedLabelsOut"] = t.struct(
        {
            "label": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DroppedLabelsOut"])
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
    types["QueryTimeSeriesRequestIn"] = t.struct(
        {
            "query": t.string(),
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
        }
    ).named(renames["QueryTimeSeriesRequestIn"])
    types["QueryTimeSeriesRequestOut"] = t.struct(
        {
            "query": t.string(),
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryTimeSeriesRequestOut"])
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
    types["PingConfigIn"] = t.struct({"pingsCount": t.integer().optional()}).named(
        renames["PingConfigIn"]
    )
    types["PingConfigOut"] = t.struct(
        {
            "pingsCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PingConfigOut"])
    types["GetNotificationChannelVerificationCodeRequestIn"] = t.struct(
        {"expireTime": t.string().optional()}
    ).named(renames["GetNotificationChannelVerificationCodeRequestIn"])
    types["GetNotificationChannelVerificationCodeRequestOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetNotificationChannelVerificationCodeRequestOut"])
    types["SpanContextIn"] = t.struct({"spanName": t.string().optional()}).named(
        renames["SpanContextIn"]
    )
    types["SpanContextOut"] = t.struct(
        {
            "spanName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpanContextOut"])
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
    types["UptimeCheckConfigIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "contentMatchers": t.array(t.proxy(renames["ContentMatcherIn"])).optional(),
            "isInternal": t.boolean().optional(),
            "selectedRegions": t.array(t.string()).optional(),
            "checkerType": t.string().optional(),
            "internalCheckers": t.array(
                t.proxy(renames["InternalCheckerIn"])
            ).optional(),
            "resourceGroup": t.proxy(renames["ResourceGroupIn"]).optional(),
            "tcpCheck": t.proxy(renames["TcpCheckIn"]).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "period": t.string().optional(),
            "name": t.string().optional(),
            "httpCheck": t.proxy(renames["HttpCheckIn"]).optional(),
            "monitoredResource": t.proxy(renames["MonitoredResourceIn"]).optional(),
            "timeout": t.string().optional(),
        }
    ).named(renames["UptimeCheckConfigIn"])
    types["UptimeCheckConfigOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "contentMatchers": t.array(
                t.proxy(renames["ContentMatcherOut"])
            ).optional(),
            "isInternal": t.boolean().optional(),
            "selectedRegions": t.array(t.string()).optional(),
            "checkerType": t.string().optional(),
            "internalCheckers": t.array(
                t.proxy(renames["InternalCheckerOut"])
            ).optional(),
            "resourceGroup": t.proxy(renames["ResourceGroupOut"]).optional(),
            "tcpCheck": t.proxy(renames["TcpCheckOut"]).optional(),
            "userLabels": t.struct({"_": t.string().optional()}).optional(),
            "period": t.string().optional(),
            "name": t.string().optional(),
            "httpCheck": t.proxy(renames["HttpCheckOut"]).optional(),
            "monitoredResource": t.proxy(renames["MonitoredResourceOut"]).optional(),
            "timeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UptimeCheckConfigOut"])
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

    functions = {}
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
    functions["projectsCollectdTimeSeriesCreate"] = monitoring.post(
        "v3/{name}/collectdTimeSeries",
        t.struct(
            {
                "name": t.string().optional(),
                "collectdVersion": t.string().optional(),
                "resource": t.proxy(renames["MonitoredResourceIn"]).optional(),
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
    functions["projectsNotificationChannelDescriptorsGet"] = monitoring.get(
        "v3/{name}/notificationChannelDescriptors",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNotificationChannelDescriptorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnoozesPatch"] = monitoring.post(
        "v3/{parent}/snoozes",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string(),
                "name": t.string(),
                "interval": t.proxy(renames["TimeIntervalIn"]),
                "criteria": t.proxy(renames["CriteriaIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnoozeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnoozesGet"] = monitoring.post(
        "v3/{parent}/snoozes",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string(),
                "name": t.string(),
                "interval": t.proxy(renames["TimeIntervalIn"]),
                "criteria": t.proxy(renames["CriteriaIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnoozeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnoozesList"] = monitoring.post(
        "v3/{parent}/snoozes",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string(),
                "name": t.string(),
                "interval": t.proxy(renames["TimeIntervalIn"]),
                "criteria": t.proxy(renames["CriteriaIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnoozeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnoozesCreate"] = monitoring.post(
        "v3/{parent}/snoozes",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string(),
                "name": t.string(),
                "interval": t.proxy(renames["TimeIntervalIn"]),
                "criteria": t.proxy(renames["CriteriaIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnoozeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTimeSeriesList"] = monitoring.post(
        "v3/{name}/timeSeries:query",
        t.struct(
            {
                "name": t.string(),
                "query": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "query": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryTimeSeriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTimeSeriesCreate"] = monitoring.post(
        "v3/{name}/timeSeries:query",
        t.struct(
            {
                "name": t.string(),
                "query": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "query": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryTimeSeriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUptimeCheckConfigsGet"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "contentMatchers": t.array(
                    t.proxy(renames["ContentMatcherIn"])
                ).optional(),
                "isInternal": t.boolean().optional(),
                "selectedRegions": t.array(t.string()).optional(),
                "checkerType": t.string().optional(),
                "internalCheckers": t.array(
                    t.proxy(renames["InternalCheckerIn"])
                ).optional(),
                "resourceGroup": t.proxy(renames["ResourceGroupIn"]).optional(),
                "tcpCheck": t.proxy(renames["TcpCheckIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "period": t.string().optional(),
                "httpCheck": t.proxy(renames["HttpCheckIn"]).optional(),
                "monitoredResource": t.proxy(renames["MonitoredResourceIn"]).optional(),
                "timeout": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UptimeCheckConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUptimeCheckConfigsList"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "contentMatchers": t.array(
                    t.proxy(renames["ContentMatcherIn"])
                ).optional(),
                "isInternal": t.boolean().optional(),
                "selectedRegions": t.array(t.string()).optional(),
                "checkerType": t.string().optional(),
                "internalCheckers": t.array(
                    t.proxy(renames["InternalCheckerIn"])
                ).optional(),
                "resourceGroup": t.proxy(renames["ResourceGroupIn"]).optional(),
                "tcpCheck": t.proxy(renames["TcpCheckIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "period": t.string().optional(),
                "httpCheck": t.proxy(renames["HttpCheckIn"]).optional(),
                "monitoredResource": t.proxy(renames["MonitoredResourceIn"]).optional(),
                "timeout": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UptimeCheckConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUptimeCheckConfigsDelete"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "contentMatchers": t.array(
                    t.proxy(renames["ContentMatcherIn"])
                ).optional(),
                "isInternal": t.boolean().optional(),
                "selectedRegions": t.array(t.string()).optional(),
                "checkerType": t.string().optional(),
                "internalCheckers": t.array(
                    t.proxy(renames["InternalCheckerIn"])
                ).optional(),
                "resourceGroup": t.proxy(renames["ResourceGroupIn"]).optional(),
                "tcpCheck": t.proxy(renames["TcpCheckIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "period": t.string().optional(),
                "httpCheck": t.proxy(renames["HttpCheckIn"]).optional(),
                "monitoredResource": t.proxy(renames["MonitoredResourceIn"]).optional(),
                "timeout": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UptimeCheckConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUptimeCheckConfigsCreate"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "contentMatchers": t.array(
                    t.proxy(renames["ContentMatcherIn"])
                ).optional(),
                "isInternal": t.boolean().optional(),
                "selectedRegions": t.array(t.string()).optional(),
                "checkerType": t.string().optional(),
                "internalCheckers": t.array(
                    t.proxy(renames["InternalCheckerIn"])
                ).optional(),
                "resourceGroup": t.proxy(renames["ResourceGroupIn"]).optional(),
                "tcpCheck": t.proxy(renames["TcpCheckIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "period": t.string().optional(),
                "httpCheck": t.proxy(renames["HttpCheckIn"]).optional(),
                "monitoredResource": t.proxy(renames["MonitoredResourceIn"]).optional(),
                "timeout": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UptimeCheckConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUptimeCheckConfigsPatch"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "contentMatchers": t.array(
                    t.proxy(renames["ContentMatcherIn"])
                ).optional(),
                "isInternal": t.boolean().optional(),
                "selectedRegions": t.array(t.string()).optional(),
                "checkerType": t.string().optional(),
                "internalCheckers": t.array(
                    t.proxy(renames["InternalCheckerIn"])
                ).optional(),
                "resourceGroup": t.proxy(renames["ResourceGroupIn"]).optional(),
                "tcpCheck": t.proxy(renames["TcpCheckIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "period": t.string().optional(),
                "httpCheck": t.proxy(renames["HttpCheckIn"]).optional(),
                "monitoredResource": t.proxy(renames["MonitoredResourceIn"]).optional(),
                "timeout": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UptimeCheckConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMetricDescriptorsList"] = monitoring.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMetricDescriptorsGet"] = monitoring.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMetricDescriptorsCreate"] = monitoring.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMetricDescriptorsDelete"] = monitoring.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAlertPoliciesPatch"] = monitoring.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAlertPoliciesGet"] = monitoring.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAlertPoliciesCreate"] = monitoring.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAlertPoliciesList"] = monitoring.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAlertPoliciesDelete"] = monitoring.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["projectsNotificationChannelsSendVerificationCode"] = monitoring.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NotificationChannelOut"]),
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
    functions["projectsNotificationChannelsVerify"] = monitoring.get(
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
    functions["projectsGroupsGet"] = monitoring.delete(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "recursive": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsList"] = monitoring.delete(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "recursive": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsCreate"] = monitoring.delete(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "recursive": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsUpdate"] = monitoring.delete(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "recursive": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsDelete"] = monitoring.delete(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "recursive": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsMembersList"] = monitoring.get(
        "v3/{name}/members",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "interval.endTime": t.string(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "interval.startTime": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGroupMembersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsTimeSeriesList"] = monitoring.get(
        "v3/{name}/timeSeries",
        t.struct(
            {
                "name": t.string(),
                "aggregation.crossSeriesReducer": t.string().optional(),
                "pageToken": t.string().optional(),
                "secondaryAggregation.groupByFields": t.string().optional(),
                "secondaryAggregation.crossSeriesReducer": t.string().optional(),
                "interval.startTime": t.string().optional(),
                "filter": t.string(),
                "pageSize": t.integer().optional(),
                "view": t.string(),
                "secondaryAggregation.perSeriesAligner": t.string().optional(),
                "aggregation.alignmentPeriod": t.string().optional(),
                "aggregation.perSeriesAligner": t.string().optional(),
                "interval.endTime": t.string(),
                "aggregation.groupByFields": t.string().optional(),
                "secondaryAggregation.alignmentPeriod": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTimeSeriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesCreate"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "telemetry": t.proxy(renames["TelemetryIn"]).optional(),
                "istioCanonicalService": t.proxy(
                    renames["IstioCanonicalServiceIn"]
                ).optional(),
                "cloudRun": t.proxy(renames["CloudRunIn"]).optional(),
                "gkeWorkload": t.proxy(renames["GkeWorkloadIn"]).optional(),
                "custom": t.proxy(renames["CustomIn"]).optional(),
                "gkeService": t.proxy(renames["GkeServiceIn"]).optional(),
                "meshIstio": t.proxy(renames["MeshIstioIn"]).optional(),
                "displayName": t.string().optional(),
                "clusterIstio": t.proxy(renames["ClusterIstioIn"]).optional(),
                "cloudEndpoints": t.proxy(renames["CloudEndpointsIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "basicService": t.proxy(renames["BasicServiceIn"]).optional(),
                "gkeNamespace": t.proxy(renames["GkeNamespaceIn"]).optional(),
                "appEngine": t.proxy(renames["AppEngineIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesDelete"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "telemetry": t.proxy(renames["TelemetryIn"]).optional(),
                "istioCanonicalService": t.proxy(
                    renames["IstioCanonicalServiceIn"]
                ).optional(),
                "cloudRun": t.proxy(renames["CloudRunIn"]).optional(),
                "gkeWorkload": t.proxy(renames["GkeWorkloadIn"]).optional(),
                "custom": t.proxy(renames["CustomIn"]).optional(),
                "gkeService": t.proxy(renames["GkeServiceIn"]).optional(),
                "meshIstio": t.proxy(renames["MeshIstioIn"]).optional(),
                "displayName": t.string().optional(),
                "clusterIstio": t.proxy(renames["ClusterIstioIn"]).optional(),
                "cloudEndpoints": t.proxy(renames["CloudEndpointsIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "basicService": t.proxy(renames["BasicServiceIn"]).optional(),
                "gkeNamespace": t.proxy(renames["GkeNamespaceIn"]).optional(),
                "appEngine": t.proxy(renames["AppEngineIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesList"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "telemetry": t.proxy(renames["TelemetryIn"]).optional(),
                "istioCanonicalService": t.proxy(
                    renames["IstioCanonicalServiceIn"]
                ).optional(),
                "cloudRun": t.proxy(renames["CloudRunIn"]).optional(),
                "gkeWorkload": t.proxy(renames["GkeWorkloadIn"]).optional(),
                "custom": t.proxy(renames["CustomIn"]).optional(),
                "gkeService": t.proxy(renames["GkeServiceIn"]).optional(),
                "meshIstio": t.proxy(renames["MeshIstioIn"]).optional(),
                "displayName": t.string().optional(),
                "clusterIstio": t.proxy(renames["ClusterIstioIn"]).optional(),
                "cloudEndpoints": t.proxy(renames["CloudEndpointsIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "basicService": t.proxy(renames["BasicServiceIn"]).optional(),
                "gkeNamespace": t.proxy(renames["GkeNamespaceIn"]).optional(),
                "appEngine": t.proxy(renames["AppEngineIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesGet"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "telemetry": t.proxy(renames["TelemetryIn"]).optional(),
                "istioCanonicalService": t.proxy(
                    renames["IstioCanonicalServiceIn"]
                ).optional(),
                "cloudRun": t.proxy(renames["CloudRunIn"]).optional(),
                "gkeWorkload": t.proxy(renames["GkeWorkloadIn"]).optional(),
                "custom": t.proxy(renames["CustomIn"]).optional(),
                "gkeService": t.proxy(renames["GkeServiceIn"]).optional(),
                "meshIstio": t.proxy(renames["MeshIstioIn"]).optional(),
                "displayName": t.string().optional(),
                "clusterIstio": t.proxy(renames["ClusterIstioIn"]).optional(),
                "cloudEndpoints": t.proxy(renames["CloudEndpointsIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "basicService": t.proxy(renames["BasicServiceIn"]).optional(),
                "gkeNamespace": t.proxy(renames["GkeNamespaceIn"]).optional(),
                "appEngine": t.proxy(renames["AppEngineIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesPatch"] = monitoring.patch(
        "v3/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "telemetry": t.proxy(renames["TelemetryIn"]).optional(),
                "istioCanonicalService": t.proxy(
                    renames["IstioCanonicalServiceIn"]
                ).optional(),
                "cloudRun": t.proxy(renames["CloudRunIn"]).optional(),
                "gkeWorkload": t.proxy(renames["GkeWorkloadIn"]).optional(),
                "custom": t.proxy(renames["CustomIn"]).optional(),
                "gkeService": t.proxy(renames["GkeServiceIn"]).optional(),
                "meshIstio": t.proxy(renames["MeshIstioIn"]).optional(),
                "displayName": t.string().optional(),
                "clusterIstio": t.proxy(renames["ClusterIstioIn"]).optional(),
                "cloudEndpoints": t.proxy(renames["CloudEndpointsIn"]).optional(),
                "userLabels": t.struct({"_": t.string().optional()}).optional(),
                "basicService": t.proxy(renames["BasicServiceIn"]).optional(),
                "gkeNamespace": t.proxy(renames["GkeNamespaceIn"]).optional(),
                "appEngine": t.proxy(renames["AppEngineIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
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
    functions["foldersTimeSeriesList"] = monitoring.get(
        "v3/{name}/timeSeries",
        t.struct(
            {
                "aggregation.alignmentPeriod": t.string().optional(),
                "interval.endTime": t.string(),
                "aggregation.crossSeriesReducer": t.string().optional(),
                "aggregation.perSeriesAligner": t.string().optional(),
                "orderBy": t.string().optional(),
                "view": t.string(),
                "secondaryAggregation.groupByFields": t.string().optional(),
                "name": t.string(),
                "filter": t.string(),
                "secondaryAggregation.perSeriesAligner": t.string().optional(),
                "secondaryAggregation.crossSeriesReducer": t.string().optional(),
                "aggregation.groupByFields": t.string().optional(),
                "interval.startTime": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "secondaryAggregation.alignmentPeriod": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTimeSeriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="monitoring",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
