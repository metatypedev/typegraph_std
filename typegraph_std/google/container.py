from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_container() -> Import:
    container = HTTPRuntime("https://container.googleapis.com/")

    renames = {
        "ErrorResponse": "_container_1_ErrorResponse",
        "UsableSubnetworkSecondaryRangeIn": "_container_2_UsableSubnetworkSecondaryRangeIn",
        "UsableSubnetworkSecondaryRangeOut": "_container_3_UsableSubnetworkSecondaryRangeOut",
        "BigQueryDestinationIn": "_container_4_BigQueryDestinationIn",
        "BigQueryDestinationOut": "_container_5_BigQueryDestinationOut",
        "UpdateInfoIn": "_container_6_UpdateInfoIn",
        "UpdateInfoOut": "_container_7_UpdateInfoOut",
        "SecurityBulletinEventIn": "_container_8_SecurityBulletinEventIn",
        "SecurityBulletinEventOut": "_container_9_SecurityBulletinEventOut",
        "MonitoringComponentConfigIn": "_container_10_MonitoringComponentConfigIn",
        "MonitoringComponentConfigOut": "_container_11_MonitoringComponentConfigOut",
        "OperationIn": "_container_12_OperationIn",
        "OperationOut": "_container_13_OperationOut",
        "SetMasterAuthRequestIn": "_container_14_SetMasterAuthRequestIn",
        "SetMasterAuthRequestOut": "_container_15_SetMasterAuthRequestOut",
        "TimeWindowIn": "_container_16_TimeWindowIn",
        "TimeWindowOut": "_container_17_TimeWindowOut",
        "MaintenancePolicyIn": "_container_18_MaintenancePolicyIn",
        "MaintenancePolicyOut": "_container_19_MaintenancePolicyOut",
        "LoggingConfigIn": "_container_20_LoggingConfigIn",
        "LoggingConfigOut": "_container_21_LoggingConfigOut",
        "MaintenanceWindowIn": "_container_22_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_container_23_MaintenanceWindowOut",
        "IPAllocationPolicyIn": "_container_24_IPAllocationPolicyIn",
        "IPAllocationPolicyOut": "_container_25_IPAllocationPolicyOut",
        "OperationProgressIn": "_container_26_OperationProgressIn",
        "OperationProgressOut": "_container_27_OperationProgressOut",
        "GcfsConfigIn": "_container_28_GcfsConfigIn",
        "GcfsConfigOut": "_container_29_GcfsConfigOut",
        "ConfigConnectorConfigIn": "_container_30_ConfigConnectorConfigIn",
        "ConfigConnectorConfigOut": "_container_31_ConfigConnectorConfigOut",
        "GetJSONWebKeysResponseIn": "_container_32_GetJSONWebKeysResponseIn",
        "GetJSONWebKeysResponseOut": "_container_33_GetJSONWebKeysResponseOut",
        "ResourceUsageExportConfigIn": "_container_34_ResourceUsageExportConfigIn",
        "ResourceUsageExportConfigOut": "_container_35_ResourceUsageExportConfigOut",
        "CidrBlockIn": "_container_36_CidrBlockIn",
        "CidrBlockOut": "_container_37_CidrBlockOut",
        "BinaryAuthorizationIn": "_container_38_BinaryAuthorizationIn",
        "BinaryAuthorizationOut": "_container_39_BinaryAuthorizationOut",
        "RollbackNodePoolUpgradeRequestIn": "_container_40_RollbackNodePoolUpgradeRequestIn",
        "RollbackNodePoolUpgradeRequestOut": "_container_41_RollbackNodePoolUpgradeRequestOut",
        "CostManagementConfigIn": "_container_42_CostManagementConfigIn",
        "CostManagementConfigOut": "_container_43_CostManagementConfigOut",
        "DnsCacheConfigIn": "_container_44_DnsCacheConfigIn",
        "DnsCacheConfigOut": "_container_45_DnsCacheConfigOut",
        "FleetIn": "_container_46_FleetIn",
        "FleetOut": "_container_47_FleetOut",
        "PodCIDROverprovisionConfigIn": "_container_48_PodCIDROverprovisionConfigIn",
        "PodCIDROverprovisionConfigOut": "_container_49_PodCIDROverprovisionConfigOut",
        "NodeKubeletConfigIn": "_container_50_NodeKubeletConfigIn",
        "NodeKubeletConfigOut": "_container_51_NodeKubeletConfigOut",
        "NodeLabelsIn": "_container_52_NodeLabelsIn",
        "NodeLabelsOut": "_container_53_NodeLabelsOut",
        "ListOperationsResponseIn": "_container_54_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_container_55_ListOperationsResponseOut",
        "NodePoolAutoscalingIn": "_container_56_NodePoolAutoscalingIn",
        "NodePoolAutoscalingOut": "_container_57_NodePoolAutoscalingOut",
        "HorizontalPodAutoscalingIn": "_container_58_HorizontalPodAutoscalingIn",
        "HorizontalPodAutoscalingOut": "_container_59_HorizontalPodAutoscalingOut",
        "MasterAuthorizedNetworksConfigIn": "_container_60_MasterAuthorizedNetworksConfigIn",
        "MasterAuthorizedNetworksConfigOut": "_container_61_MasterAuthorizedNetworksConfigOut",
        "AutoprovisioningNodePoolDefaultsIn": "_container_62_AutoprovisioningNodePoolDefaultsIn",
        "AutoprovisioningNodePoolDefaultsOut": "_container_63_AutoprovisioningNodePoolDefaultsOut",
        "AutopilotIn": "_container_64_AutopilotIn",
        "AutopilotOut": "_container_65_AutopilotOut",
        "LinuxNodeConfigIn": "_container_66_LinuxNodeConfigIn",
        "LinuxNodeConfigOut": "_container_67_LinuxNodeConfigOut",
        "ILBSubsettingConfigIn": "_container_68_ILBSubsettingConfigIn",
        "ILBSubsettingConfigOut": "_container_69_ILBSubsettingConfigOut",
        "VerticalPodAutoscalingIn": "_container_70_VerticalPodAutoscalingIn",
        "VerticalPodAutoscalingOut": "_container_71_VerticalPodAutoscalingOut",
        "CompleteIPRotationRequestIn": "_container_72_CompleteIPRotationRequestIn",
        "CompleteIPRotationRequestOut": "_container_73_CompleteIPRotationRequestOut",
        "NodeTaintIn": "_container_74_NodeTaintIn",
        "NodeTaintOut": "_container_75_NodeTaintOut",
        "HttpCacheControlResponseHeaderIn": "_container_76_HttpCacheControlResponseHeaderIn",
        "HttpCacheControlResponseHeaderOut": "_container_77_HttpCacheControlResponseHeaderOut",
        "CreateClusterRequestIn": "_container_78_CreateClusterRequestIn",
        "CreateClusterRequestOut": "_container_79_CreateClusterRequestOut",
        "JwkIn": "_container_80_JwkIn",
        "JwkOut": "_container_81_JwkOut",
        "PrivateClusterMasterGlobalAccessConfigIn": "_container_82_PrivateClusterMasterGlobalAccessConfigIn",
        "PrivateClusterMasterGlobalAccessConfigOut": "_container_83_PrivateClusterMasterGlobalAccessConfigOut",
        "SetLocationsRequestIn": "_container_84_SetLocationsRequestIn",
        "SetLocationsRequestOut": "_container_85_SetLocationsRequestOut",
        "ManagedPrometheusConfigIn": "_container_86_ManagedPrometheusConfigIn",
        "ManagedPrometheusConfigOut": "_container_87_ManagedPrometheusConfigOut",
        "IntraNodeVisibilityConfigIn": "_container_88_IntraNodeVisibilityConfigIn",
        "IntraNodeVisibilityConfigOut": "_container_89_IntraNodeVisibilityConfigOut",
        "EphemeralStorageLocalSsdConfigIn": "_container_90_EphemeralStorageLocalSsdConfigIn",
        "EphemeralStorageLocalSsdConfigOut": "_container_91_EphemeralStorageLocalSsdConfigOut",
        "ClusterAutoscalingIn": "_container_92_ClusterAutoscalingIn",
        "ClusterAutoscalingOut": "_container_93_ClusterAutoscalingOut",
        "PrivateClusterConfigIn": "_container_94_PrivateClusterConfigIn",
        "PrivateClusterConfigOut": "_container_95_PrivateClusterConfigOut",
        "DatabaseEncryptionIn": "_container_96_DatabaseEncryptionIn",
        "DatabaseEncryptionOut": "_container_97_DatabaseEncryptionOut",
        "KubernetesDashboardIn": "_container_98_KubernetesDashboardIn",
        "KubernetesDashboardOut": "_container_99_KubernetesDashboardOut",
        "SetNodePoolSizeRequestIn": "_container_100_SetNodePoolSizeRequestIn",
        "SetNodePoolSizeRequestOut": "_container_101_SetNodePoolSizeRequestOut",
        "LoggingVariantConfigIn": "_container_102_LoggingVariantConfigIn",
        "LoggingVariantConfigOut": "_container_103_LoggingVariantConfigOut",
        "ConfidentialNodesIn": "_container_104_ConfidentialNodesIn",
        "ConfidentialNodesOut": "_container_105_ConfidentialNodesOut",
        "ClientCertificateConfigIn": "_container_106_ClientCertificateConfigIn",
        "ClientCertificateConfigOut": "_container_107_ClientCertificateConfigOut",
        "ReleaseChannelIn": "_container_108_ReleaseChannelIn",
        "ReleaseChannelOut": "_container_109_ReleaseChannelOut",
        "ServerConfigIn": "_container_110_ServerConfigIn",
        "ServerConfigOut": "_container_111_ServerConfigOut",
        "UpdateNodePoolRequestIn": "_container_112_UpdateNodePoolRequestIn",
        "UpdateNodePoolRequestOut": "_container_113_UpdateNodePoolRequestOut",
        "WorkloadIdentityConfigIn": "_container_114_WorkloadIdentityConfigIn",
        "WorkloadIdentityConfigOut": "_container_115_WorkloadIdentityConfigOut",
        "LegacyAbacIn": "_container_116_LegacyAbacIn",
        "LegacyAbacOut": "_container_117_LegacyAbacOut",
        "UpdateClusterRequestIn": "_container_118_UpdateClusterRequestIn",
        "UpdateClusterRequestOut": "_container_119_UpdateClusterRequestOut",
        "IdentityServiceConfigIn": "_container_120_IdentityServiceConfigIn",
        "IdentityServiceConfigOut": "_container_121_IdentityServiceConfigOut",
        "ListNodePoolsResponseIn": "_container_122_ListNodePoolsResponseIn",
        "ListNodePoolsResponseOut": "_container_123_ListNodePoolsResponseOut",
        "SetNodePoolManagementRequestIn": "_container_124_SetNodePoolManagementRequestIn",
        "SetNodePoolManagementRequestOut": "_container_125_SetNodePoolManagementRequestOut",
        "MaxPodsConstraintIn": "_container_126_MaxPodsConstraintIn",
        "MaxPodsConstraintOut": "_container_127_MaxPodsConstraintOut",
        "MetricIn": "_container_128_MetricIn",
        "MetricOut": "_container_129_MetricOut",
        "ResourceLabelsIn": "_container_130_ResourceLabelsIn",
        "ResourceLabelsOut": "_container_131_ResourceLabelsOut",
        "SetAddonsConfigRequestIn": "_container_132_SetAddonsConfigRequestIn",
        "SetAddonsConfigRequestOut": "_container_133_SetAddonsConfigRequestOut",
        "LoggingComponentConfigIn": "_container_134_LoggingComponentConfigIn",
        "LoggingComponentConfigOut": "_container_135_LoggingComponentConfigOut",
        "NodePoolDefaultsIn": "_container_136_NodePoolDefaultsIn",
        "NodePoolDefaultsOut": "_container_137_NodePoolDefaultsOut",
        "ClusterUpdateIn": "_container_138_ClusterUpdateIn",
        "ClusterUpdateOut": "_container_139_ClusterUpdateOut",
        "NetworkPerformanceConfigIn": "_container_140_NetworkPerformanceConfigIn",
        "NetworkPerformanceConfigOut": "_container_141_NetworkPerformanceConfigOut",
        "GatewayAPIConfigIn": "_container_142_GatewayAPIConfigIn",
        "GatewayAPIConfigOut": "_container_143_GatewayAPIConfigOut",
        "NetworkConfigIn": "_container_144_NetworkConfigIn",
        "NetworkConfigOut": "_container_145_NetworkConfigOut",
        "MasterAuthIn": "_container_146_MasterAuthIn",
        "MasterAuthOut": "_container_147_MasterAuthOut",
        "AutoUpgradeOptionsIn": "_container_148_AutoUpgradeOptionsIn",
        "AutoUpgradeOptionsOut": "_container_149_AutoUpgradeOptionsOut",
        "StatusConditionIn": "_container_150_StatusConditionIn",
        "StatusConditionOut": "_container_151_StatusConditionOut",
        "NetworkTagsIn": "_container_152_NetworkTagsIn",
        "NetworkTagsOut": "_container_153_NetworkTagsOut",
        "FilterIn": "_container_154_FilterIn",
        "FilterOut": "_container_155_FilterOut",
        "ListUsableSubnetworksResponseIn": "_container_156_ListUsableSubnetworksResponseIn",
        "ListUsableSubnetworksResponseOut": "_container_157_ListUsableSubnetworksResponseOut",
        "NodeNetworkConfigIn": "_container_158_NodeNetworkConfigIn",
        "NodeNetworkConfigOut": "_container_159_NodeNetworkConfigOut",
        "WindowsNodeConfigIn": "_container_160_WindowsNodeConfigIn",
        "WindowsNodeConfigOut": "_container_161_WindowsNodeConfigOut",
        "WorkloadMetadataConfigIn": "_container_162_WorkloadMetadataConfigIn",
        "WorkloadMetadataConfigOut": "_container_163_WorkloadMetadataConfigOut",
        "NodeTaintsIn": "_container_164_NodeTaintsIn",
        "NodeTaintsOut": "_container_165_NodeTaintsOut",
        "DailyMaintenanceWindowIn": "_container_166_DailyMaintenanceWindowIn",
        "DailyMaintenanceWindowOut": "_container_167_DailyMaintenanceWindowOut",
        "GPUSharingConfigIn": "_container_168_GPUSharingConfigIn",
        "GPUSharingConfigOut": "_container_169_GPUSharingConfigOut",
        "ListClustersResponseIn": "_container_170_ListClustersResponseIn",
        "ListClustersResponseOut": "_container_171_ListClustersResponseOut",
        "ShieldedNodesIn": "_container_172_ShieldedNodesIn",
        "ShieldedNodesOut": "_container_173_ShieldedNodesOut",
        "SandboxConfigIn": "_container_174_SandboxConfigIn",
        "SandboxConfigOut": "_container_175_SandboxConfigOut",
        "AddonsConfigIn": "_container_176_AddonsConfigIn",
        "AddonsConfigOut": "_container_177_AddonsConfigOut",
        "StandardRolloutPolicyIn": "_container_178_StandardRolloutPolicyIn",
        "StandardRolloutPolicyOut": "_container_179_StandardRolloutPolicyOut",
        "CloudRunConfigIn": "_container_180_CloudRunConfigIn",
        "CloudRunConfigOut": "_container_181_CloudRunConfigOut",
        "CancelOperationRequestIn": "_container_182_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_container_183_CancelOperationRequestOut",
        "DNSConfigIn": "_container_184_DNSConfigIn",
        "DNSConfigOut": "_container_185_DNSConfigOut",
        "UsableSubnetworkIn": "_container_186_UsableSubnetworkIn",
        "UsableSubnetworkOut": "_container_187_UsableSubnetworkOut",
        "SetMaintenancePolicyRequestIn": "_container_188_SetMaintenancePolicyRequestIn",
        "SetMaintenancePolicyRequestOut": "_container_189_SetMaintenancePolicyRequestOut",
        "CreateNodePoolRequestIn": "_container_190_CreateNodePoolRequestIn",
        "CreateNodePoolRequestOut": "_container_191_CreateNodePoolRequestOut",
        "StartIPRotationRequestIn": "_container_192_StartIPRotationRequestIn",
        "StartIPRotationRequestOut": "_container_193_StartIPRotationRequestOut",
        "GetOpenIDConfigResponseIn": "_container_194_GetOpenIDConfigResponseIn",
        "GetOpenIDConfigResponseOut": "_container_195_GetOpenIDConfigResponseOut",
        "BlueGreenInfoIn": "_container_196_BlueGreenInfoIn",
        "BlueGreenInfoOut": "_container_197_BlueGreenInfoOut",
        "SetLabelsRequestIn": "_container_198_SetLabelsRequestIn",
        "SetLabelsRequestOut": "_container_199_SetLabelsRequestOut",
        "MonitoringConfigIn": "_container_200_MonitoringConfigIn",
        "MonitoringConfigOut": "_container_201_MonitoringConfigOut",
        "NodePoolAutoConfigIn": "_container_202_NodePoolAutoConfigIn",
        "NodePoolAutoConfigOut": "_container_203_NodePoolAutoConfigOut",
        "UpdateMasterRequestIn": "_container_204_UpdateMasterRequestIn",
        "UpdateMasterRequestOut": "_container_205_UpdateMasterRequestOut",
        "CompleteNodePoolUpgradeRequestIn": "_container_206_CompleteNodePoolUpgradeRequestIn",
        "CompleteNodePoolUpgradeRequestOut": "_container_207_CompleteNodePoolUpgradeRequestOut",
        "ShieldedInstanceConfigIn": "_container_208_ShieldedInstanceConfigIn",
        "ShieldedInstanceConfigOut": "_container_209_ShieldedInstanceConfigOut",
        "FastSocketIn": "_container_210_FastSocketIn",
        "FastSocketOut": "_container_211_FastSocketOut",
        "GcpFilestoreCsiDriverConfigIn": "_container_212_GcpFilestoreCsiDriverConfigIn",
        "GcpFilestoreCsiDriverConfigOut": "_container_213_GcpFilestoreCsiDriverConfigOut",
        "NotificationConfigIn": "_container_214_NotificationConfigIn",
        "NotificationConfigOut": "_container_215_NotificationConfigOut",
        "NodeConfigDefaultsIn": "_container_216_NodeConfigDefaultsIn",
        "NodeConfigDefaultsOut": "_container_217_NodeConfigDefaultsOut",
        "ReservationAffinityIn": "_container_218_ReservationAffinityIn",
        "ReservationAffinityOut": "_container_219_ReservationAffinityOut",
        "HttpLoadBalancingIn": "_container_220_HttpLoadBalancingIn",
        "HttpLoadBalancingOut": "_container_221_HttpLoadBalancingOut",
        "ReleaseChannelConfigIn": "_container_222_ReleaseChannelConfigIn",
        "ReleaseChannelConfigOut": "_container_223_ReleaseChannelConfigOut",
        "PlacementPolicyIn": "_container_224_PlacementPolicyIn",
        "PlacementPolicyOut": "_container_225_PlacementPolicyOut",
        "AuthenticatorGroupsConfigIn": "_container_226_AuthenticatorGroupsConfigIn",
        "AuthenticatorGroupsConfigOut": "_container_227_AuthenticatorGroupsConfigOut",
        "GcePersistentDiskCsiDriverConfigIn": "_container_228_GcePersistentDiskCsiDriverConfigIn",
        "GcePersistentDiskCsiDriverConfigOut": "_container_229_GcePersistentDiskCsiDriverConfigOut",
        "StatusIn": "_container_230_StatusIn",
        "StatusOut": "_container_231_StatusOut",
        "ClusterIn": "_container_232_ClusterIn",
        "ClusterOut": "_container_233_ClusterOut",
        "VirtualNICIn": "_container_234_VirtualNICIn",
        "VirtualNICOut": "_container_235_VirtualNICOut",
        "NetworkPolicyIn": "_container_236_NetworkPolicyIn",
        "NetworkPolicyOut": "_container_237_NetworkPolicyOut",
        "AdvancedMachineFeaturesIn": "_container_238_AdvancedMachineFeaturesIn",
        "AdvancedMachineFeaturesOut": "_container_239_AdvancedMachineFeaturesOut",
        "GkeBackupAgentConfigIn": "_container_240_GkeBackupAgentConfigIn",
        "GkeBackupAgentConfigOut": "_container_241_GkeBackupAgentConfigOut",
        "PubSubIn": "_container_242_PubSubIn",
        "PubSubOut": "_container_243_PubSubOut",
        "NodeManagementIn": "_container_244_NodeManagementIn",
        "NodeManagementOut": "_container_245_NodeManagementOut",
        "ServiceExternalIPsConfigIn": "_container_246_ServiceExternalIPsConfigIn",
        "ServiceExternalIPsConfigOut": "_container_247_ServiceExternalIPsConfigOut",
        "DefaultSnatStatusIn": "_container_248_DefaultSnatStatusIn",
        "DefaultSnatStatusOut": "_container_249_DefaultSnatStatusOut",
        "SetMonitoringServiceRequestIn": "_container_250_SetMonitoringServiceRequestIn",
        "SetMonitoringServiceRequestOut": "_container_251_SetMonitoringServiceRequestOut",
        "BlueGreenSettingsIn": "_container_252_BlueGreenSettingsIn",
        "BlueGreenSettingsOut": "_container_253_BlueGreenSettingsOut",
        "NetworkPolicyConfigIn": "_container_254_NetworkPolicyConfigIn",
        "NetworkPolicyConfigOut": "_container_255_NetworkPolicyConfigOut",
        "UpgradeAvailableEventIn": "_container_256_UpgradeAvailableEventIn",
        "UpgradeAvailableEventOut": "_container_257_UpgradeAvailableEventOut",
        "MeshCertificatesIn": "_container_258_MeshCertificatesIn",
        "MeshCertificatesOut": "_container_259_MeshCertificatesOut",
        "AcceleratorConfigIn": "_container_260_AcceleratorConfigIn",
        "AcceleratorConfigOut": "_container_261_AcceleratorConfigOut",
        "EmptyIn": "_container_262_EmptyIn",
        "EmptyOut": "_container_263_EmptyOut",
        "MaintenanceExclusionOptionsIn": "_container_264_MaintenanceExclusionOptionsIn",
        "MaintenanceExclusionOptionsOut": "_container_265_MaintenanceExclusionOptionsOut",
        "ResourceLimitIn": "_container_266_ResourceLimitIn",
        "ResourceLimitOut": "_container_267_ResourceLimitOut",
        "NodePoolLoggingConfigIn": "_container_268_NodePoolLoggingConfigIn",
        "NodePoolLoggingConfigOut": "_container_269_NodePoolLoggingConfigOut",
        "NodePoolIn": "_container_270_NodePoolIn",
        "NodePoolOut": "_container_271_NodePoolOut",
        "AdditionalPodRangesConfigIn": "_container_272_AdditionalPodRangesConfigIn",
        "AdditionalPodRangesConfigOut": "_container_273_AdditionalPodRangesConfigOut",
        "RecurringTimeWindowIn": "_container_274_RecurringTimeWindowIn",
        "RecurringTimeWindowOut": "_container_275_RecurringTimeWindowOut",
        "UpgradeSettingsIn": "_container_276_UpgradeSettingsIn",
        "UpgradeSettingsOut": "_container_277_UpgradeSettingsOut",
        "UpgradeEventIn": "_container_278_UpgradeEventIn",
        "UpgradeEventOut": "_container_279_UpgradeEventOut",
        "SetNodePoolAutoscalingRequestIn": "_container_280_SetNodePoolAutoscalingRequestIn",
        "SetNodePoolAutoscalingRequestOut": "_container_281_SetNodePoolAutoscalingRequestOut",
        "SetLegacyAbacRequestIn": "_container_282_SetLegacyAbacRequestIn",
        "SetLegacyAbacRequestOut": "_container_283_SetLegacyAbacRequestOut",
        "LocalNvmeSsdBlockConfigIn": "_container_284_LocalNvmeSsdBlockConfigIn",
        "LocalNvmeSsdBlockConfigOut": "_container_285_LocalNvmeSsdBlockConfigOut",
        "ConsumptionMeteringConfigIn": "_container_286_ConsumptionMeteringConfigIn",
        "ConsumptionMeteringConfigOut": "_container_287_ConsumptionMeteringConfigOut",
        "NodeConfigIn": "_container_288_NodeConfigIn",
        "NodeConfigOut": "_container_289_NodeConfigOut",
        "SetLoggingServiceRequestIn": "_container_290_SetLoggingServiceRequestIn",
        "SetLoggingServiceRequestOut": "_container_291_SetLoggingServiceRequestOut",
        "SetNetworkPolicyRequestIn": "_container_292_SetNetworkPolicyRequestIn",
        "SetNetworkPolicyRequestOut": "_container_293_SetNetworkPolicyRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["UsableSubnetworkSecondaryRangeIn"] = t.struct(
        {
            "rangeName": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["UsableSubnetworkSecondaryRangeIn"])
    types["UsableSubnetworkSecondaryRangeOut"] = t.struct(
        {
            "rangeName": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsableSubnetworkSecondaryRangeOut"])
    types["BigQueryDestinationIn"] = t.struct(
        {"datasetId": t.string().optional()}
    ).named(renames["BigQueryDestinationIn"])
    types["BigQueryDestinationOut"] = t.struct(
        {
            "datasetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryDestinationOut"])
    types["UpdateInfoIn"] = t.struct(
        {"blueGreenInfo": t.proxy(renames["BlueGreenInfoIn"]).optional()}
    ).named(renames["UpdateInfoIn"])
    types["UpdateInfoOut"] = t.struct(
        {
            "blueGreenInfo": t.proxy(renames["BlueGreenInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateInfoOut"])
    types["SecurityBulletinEventIn"] = t.struct(
        {
            "briefDescription": t.string().optional(),
            "cveIds": t.array(t.string()).optional(),
            "bulletinUri": t.string().optional(),
            "bulletinId": t.string().optional(),
            "affectedSupportedMinors": t.array(t.string()).optional(),
            "severity": t.string().optional(),
            "suggestedUpgradeTarget": t.string().optional(),
            "resourceTypeAffected": t.string().optional(),
            "patchedVersions": t.array(t.string()).optional(),
            "manualStepsRequired": t.boolean().optional(),
        }
    ).named(renames["SecurityBulletinEventIn"])
    types["SecurityBulletinEventOut"] = t.struct(
        {
            "briefDescription": t.string().optional(),
            "cveIds": t.array(t.string()).optional(),
            "bulletinUri": t.string().optional(),
            "bulletinId": t.string().optional(),
            "affectedSupportedMinors": t.array(t.string()).optional(),
            "severity": t.string().optional(),
            "suggestedUpgradeTarget": t.string().optional(),
            "resourceTypeAffected": t.string().optional(),
            "patchedVersions": t.array(t.string()).optional(),
            "manualStepsRequired": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecurityBulletinEventOut"])
    types["MonitoringComponentConfigIn"] = t.struct(
        {"enableComponents": t.array(t.string()).optional()}
    ).named(renames["MonitoringComponentConfigIn"])
    types["MonitoringComponentConfigOut"] = t.struct(
        {
            "enableComponents": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoringComponentConfigOut"])
    types["OperationIn"] = t.struct(
        {
            "zone": t.string().optional(),
            "operationType": t.string().optional(),
            "status": t.string().optional(),
            "clusterConditions": t.array(
                t.proxy(renames["StatusConditionIn"])
            ).optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "detail": t.string().optional(),
            "location": t.string().optional(),
            "targetLink": t.string().optional(),
            "name": t.string().optional(),
            "nodepoolConditions": t.array(
                t.proxy(renames["StatusConditionIn"])
            ).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "zone": t.string().optional(),
            "operationType": t.string().optional(),
            "statusMessage": t.string().optional(),
            "status": t.string().optional(),
            "clusterConditions": t.array(
                t.proxy(renames["StatusConditionOut"])
            ).optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "detail": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "location": t.string().optional(),
            "targetLink": t.string().optional(),
            "name": t.string().optional(),
            "nodepoolConditions": t.array(
                t.proxy(renames["StatusConditionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["SetMasterAuthRequestIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "action": t.string(),
            "update": t.proxy(renames["MasterAuthIn"]),
        }
    ).named(renames["SetMasterAuthRequestIn"])
    types["SetMasterAuthRequestOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "action": t.string(),
            "update": t.proxy(renames["MasterAuthOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetMasterAuthRequestOut"])
    types["TimeWindowIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "maintenanceExclusionOptions": t.proxy(
                renames["MaintenanceExclusionOptionsIn"]
            ).optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["TimeWindowIn"])
    types["TimeWindowOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "maintenanceExclusionOptions": t.proxy(
                renames["MaintenanceExclusionOptionsOut"]
            ).optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeWindowOut"])
    types["MaintenancePolicyIn"] = t.struct(
        {
            "window": t.proxy(renames["MaintenanceWindowIn"]).optional(),
            "resourceVersion": t.string().optional(),
        }
    ).named(renames["MaintenancePolicyIn"])
    types["MaintenancePolicyOut"] = t.struct(
        {
            "window": t.proxy(renames["MaintenanceWindowOut"]).optional(),
            "resourceVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenancePolicyOut"])
    types["LoggingConfigIn"] = t.struct(
        {"componentConfig": t.proxy(renames["LoggingComponentConfigIn"]).optional()}
    ).named(renames["LoggingConfigIn"])
    types["LoggingConfigOut"] = t.struct(
        {
            "componentConfig": t.proxy(renames["LoggingComponentConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoggingConfigOut"])
    types["MaintenanceWindowIn"] = t.struct(
        {
            "recurringWindow": t.proxy(renames["RecurringTimeWindowIn"]).optional(),
            "dailyMaintenanceWindow": t.proxy(
                renames["DailyMaintenanceWindowIn"]
            ).optional(),
            "maintenanceExclusions": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["MaintenanceWindowIn"])
    types["MaintenanceWindowOut"] = t.struct(
        {
            "recurringWindow": t.proxy(renames["RecurringTimeWindowOut"]).optional(),
            "dailyMaintenanceWindow": t.proxy(
                renames["DailyMaintenanceWindowOut"]
            ).optional(),
            "maintenanceExclusions": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceWindowOut"])
    types["IPAllocationPolicyIn"] = t.struct(
        {
            "podCidrOverprovisionConfig": t.proxy(
                renames["PodCIDROverprovisionConfigIn"]
            ).optional(),
            "useIpAliases": t.boolean().optional(),
            "createSubnetwork": t.boolean().optional(),
            "stackType": t.string().optional(),
            "servicesIpv4CidrBlock": t.string().optional(),
            "useRoutes": t.boolean().optional(),
            "clusterSecondaryRangeName": t.string().optional(),
            "tpuIpv4CidrBlock": t.string().optional(),
            "nodeIpv4CidrBlock": t.string().optional(),
            "clusterIpv4Cidr": t.string().optional(),
            "servicesIpv4Cidr": t.string().optional(),
            "nodeIpv4Cidr": t.string().optional(),
            "servicesSecondaryRangeName": t.string().optional(),
            "ipv6AccessType": t.string().optional(),
            "clusterIpv4CidrBlock": t.string().optional(),
            "subnetworkName": t.string().optional(),
        }
    ).named(renames["IPAllocationPolicyIn"])
    types["IPAllocationPolicyOut"] = t.struct(
        {
            "podCidrOverprovisionConfig": t.proxy(
                renames["PodCIDROverprovisionConfigOut"]
            ).optional(),
            "subnetIpv6CidrBlock": t.string().optional(),
            "useIpAliases": t.boolean().optional(),
            "createSubnetwork": t.boolean().optional(),
            "stackType": t.string().optional(),
            "servicesIpv4CidrBlock": t.string().optional(),
            "useRoutes": t.boolean().optional(),
            "clusterSecondaryRangeName": t.string().optional(),
            "tpuIpv4CidrBlock": t.string().optional(),
            "nodeIpv4CidrBlock": t.string().optional(),
            "clusterIpv4Cidr": t.string().optional(),
            "servicesIpv4Cidr": t.string().optional(),
            "nodeIpv4Cidr": t.string().optional(),
            "servicesSecondaryRangeName": t.string().optional(),
            "servicesIpv6CidrBlock": t.string().optional(),
            "ipv6AccessType": t.string().optional(),
            "additionalPodRangesConfig": t.proxy(
                renames["AdditionalPodRangesConfigOut"]
            ).optional(),
            "clusterIpv4CidrBlock": t.string().optional(),
            "subnetworkName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IPAllocationPolicyOut"])
    types["OperationProgressIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "stages": t.array(t.proxy(renames["OperationProgressIn"])).optional(),
            "status": t.string().optional(),
        }
    ).named(renames["OperationProgressIn"])
    types["OperationProgressOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "stages": t.array(t.proxy(renames["OperationProgressOut"])).optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationProgressOut"])
    types["GcfsConfigIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["GcfsConfigIn"]
    )
    types["GcfsConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcfsConfigOut"])
    types["ConfigConnectorConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["ConfigConnectorConfigIn"])
    types["ConfigConnectorConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigConnectorConfigOut"])
    types["GetJSONWebKeysResponseIn"] = t.struct(
        {
            "keys": t.array(t.proxy(renames["JwkIn"])).optional(),
            "cacheHeader": t.proxy(
                renames["HttpCacheControlResponseHeaderIn"]
            ).optional(),
        }
    ).named(renames["GetJSONWebKeysResponseIn"])
    types["GetJSONWebKeysResponseOut"] = t.struct(
        {
            "keys": t.array(t.proxy(renames["JwkOut"])).optional(),
            "cacheHeader": t.proxy(
                renames["HttpCacheControlResponseHeaderOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetJSONWebKeysResponseOut"])
    types["ResourceUsageExportConfigIn"] = t.struct(
        {
            "consumptionMeteringConfig": t.proxy(
                renames["ConsumptionMeteringConfigIn"]
            ).optional(),
            "bigqueryDestination": t.proxy(renames["BigQueryDestinationIn"]).optional(),
            "enableNetworkEgressMetering": t.boolean().optional(),
        }
    ).named(renames["ResourceUsageExportConfigIn"])
    types["ResourceUsageExportConfigOut"] = t.struct(
        {
            "consumptionMeteringConfig": t.proxy(
                renames["ConsumptionMeteringConfigOut"]
            ).optional(),
            "bigqueryDestination": t.proxy(
                renames["BigQueryDestinationOut"]
            ).optional(),
            "enableNetworkEgressMetering": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceUsageExportConfigOut"])
    types["CidrBlockIn"] = t.struct(
        {"cidrBlock": t.string().optional(), "displayName": t.string().optional()}
    ).named(renames["CidrBlockIn"])
    types["CidrBlockOut"] = t.struct(
        {
            "cidrBlock": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CidrBlockOut"])
    types["BinaryAuthorizationIn"] = t.struct(
        {"enabled": t.boolean().optional(), "evaluationMode": t.string().optional()}
    ).named(renames["BinaryAuthorizationIn"])
    types["BinaryAuthorizationOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "evaluationMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BinaryAuthorizationOut"])
    types["RollbackNodePoolUpgradeRequestIn"] = t.struct(
        {
            "name": t.string().optional(),
            "nodePoolId": t.string().optional(),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "respectPdb": t.boolean().optional(),
        }
    ).named(renames["RollbackNodePoolUpgradeRequestIn"])
    types["RollbackNodePoolUpgradeRequestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "nodePoolId": t.string().optional(),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "respectPdb": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RollbackNodePoolUpgradeRequestOut"])
    types["CostManagementConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["CostManagementConfigIn"])
    types["CostManagementConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CostManagementConfigOut"])
    types["DnsCacheConfigIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["DnsCacheConfigIn"]
    )
    types["DnsCacheConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsCacheConfigOut"])
    types["FleetIn"] = t.struct(
        {
            "preRegistered": t.boolean().optional(),
            "project": t.string().optional(),
            "membership": t.string().optional(),
        }
    ).named(renames["FleetIn"])
    types["FleetOut"] = t.struct(
        {
            "preRegistered": t.boolean().optional(),
            "project": t.string().optional(),
            "membership": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FleetOut"])
    types["PodCIDROverprovisionConfigIn"] = t.struct(
        {"disable": t.boolean().optional()}
    ).named(renames["PodCIDROverprovisionConfigIn"])
    types["PodCIDROverprovisionConfigOut"] = t.struct(
        {
            "disable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PodCIDROverprovisionConfigOut"])
    types["NodeKubeletConfigIn"] = t.struct(
        {
            "podPidsLimit": t.string().optional(),
            "cpuManagerPolicy": t.string().optional(),
            "cpuCfsQuota": t.boolean().optional(),
            "cpuCfsQuotaPeriod": t.string().optional(),
        }
    ).named(renames["NodeKubeletConfigIn"])
    types["NodeKubeletConfigOut"] = t.struct(
        {
            "podPidsLimit": t.string().optional(),
            "cpuManagerPolicy": t.string().optional(),
            "cpuCfsQuota": t.boolean().optional(),
            "cpuCfsQuotaPeriod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeKubeletConfigOut"])
    types["NodeLabelsIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["NodeLabelsIn"])
    types["NodeLabelsOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeLabelsOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "missingZones": t.array(t.string()).optional(),
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "missingZones": t.array(t.string()).optional(),
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["NodePoolAutoscalingIn"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "maxNodeCount": t.integer().optional(),
            "totalMaxNodeCount": t.integer().optional(),
            "minNodeCount": t.integer().optional(),
            "autoprovisioned": t.boolean().optional(),
            "totalMinNodeCount": t.integer().optional(),
            "locationPolicy": t.string().optional(),
        }
    ).named(renames["NodePoolAutoscalingIn"])
    types["NodePoolAutoscalingOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "maxNodeCount": t.integer().optional(),
            "totalMaxNodeCount": t.integer().optional(),
            "minNodeCount": t.integer().optional(),
            "autoprovisioned": t.boolean().optional(),
            "totalMinNodeCount": t.integer().optional(),
            "locationPolicy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodePoolAutoscalingOut"])
    types["HorizontalPodAutoscalingIn"] = t.struct(
        {"disabled": t.boolean().optional()}
    ).named(renames["HorizontalPodAutoscalingIn"])
    types["HorizontalPodAutoscalingOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HorizontalPodAutoscalingOut"])
    types["MasterAuthorizedNetworksConfigIn"] = t.struct(
        {
            "cidrBlocks": t.array(t.proxy(renames["CidrBlockIn"])).optional(),
            "gcpPublicCidrsAccessEnabled": t.boolean().optional(),
            "enabled": t.boolean().optional(),
        }
    ).named(renames["MasterAuthorizedNetworksConfigIn"])
    types["MasterAuthorizedNetworksConfigOut"] = t.struct(
        {
            "cidrBlocks": t.array(t.proxy(renames["CidrBlockOut"])).optional(),
            "gcpPublicCidrsAccessEnabled": t.boolean().optional(),
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MasterAuthorizedNetworksConfigOut"])
    types["AutoprovisioningNodePoolDefaultsIn"] = t.struct(
        {
            "minCpuPlatform": t.string().optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "management": t.proxy(renames["NodeManagementIn"]).optional(),
            "serviceAccount": t.string().optional(),
            "imageType": t.string().optional(),
            "diskSizeGb": t.integer().optional(),
            "bootDiskKmsKey": t.string().optional(),
            "upgradeSettings": t.proxy(renames["UpgradeSettingsIn"]).optional(),
            "diskType": t.string().optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigIn"]
            ).optional(),
        }
    ).named(renames["AutoprovisioningNodePoolDefaultsIn"])
    types["AutoprovisioningNodePoolDefaultsOut"] = t.struct(
        {
            "minCpuPlatform": t.string().optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "management": t.proxy(renames["NodeManagementOut"]).optional(),
            "serviceAccount": t.string().optional(),
            "imageType": t.string().optional(),
            "diskSizeGb": t.integer().optional(),
            "bootDiskKmsKey": t.string().optional(),
            "upgradeSettings": t.proxy(renames["UpgradeSettingsOut"]).optional(),
            "diskType": t.string().optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoprovisioningNodePoolDefaultsOut"])
    types["AutopilotIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["AutopilotIn"]
    )
    types["AutopilotOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutopilotOut"])
    types["LinuxNodeConfigIn"] = t.struct(
        {
            "cgroupMode": t.string().optional(),
            "sysctls": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LinuxNodeConfigIn"])
    types["LinuxNodeConfigOut"] = t.struct(
        {
            "cgroupMode": t.string().optional(),
            "sysctls": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinuxNodeConfigOut"])
    types["ILBSubsettingConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["ILBSubsettingConfigIn"])
    types["ILBSubsettingConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ILBSubsettingConfigOut"])
    types["VerticalPodAutoscalingIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["VerticalPodAutoscalingIn"])
    types["VerticalPodAutoscalingOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerticalPodAutoscalingOut"])
    types["CompleteIPRotationRequestIn"] = t.struct(
        {
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "clusterId": t.string().optional(),
        }
    ).named(renames["CompleteIPRotationRequestIn"])
    types["CompleteIPRotationRequestOut"] = t.struct(
        {
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "clusterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompleteIPRotationRequestOut"])
    types["NodeTaintIn"] = t.struct(
        {
            "value": t.string().optional(),
            "key": t.string().optional(),
            "effect": t.string().optional(),
        }
    ).named(renames["NodeTaintIn"])
    types["NodeTaintOut"] = t.struct(
        {
            "value": t.string().optional(),
            "key": t.string().optional(),
            "effect": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeTaintOut"])
    types["HttpCacheControlResponseHeaderIn"] = t.struct(
        {
            "age": t.string().optional(),
            "expires": t.string().optional(),
            "directive": t.string().optional(),
        }
    ).named(renames["HttpCacheControlResponseHeaderIn"])
    types["HttpCacheControlResponseHeaderOut"] = t.struct(
        {
            "age": t.string().optional(),
            "expires": t.string().optional(),
            "directive": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpCacheControlResponseHeaderOut"])
    types["CreateClusterRequestIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "parent": t.string().optional(),
            "zone": t.string().optional(),
            "cluster": t.proxy(renames["ClusterIn"]),
        }
    ).named(renames["CreateClusterRequestIn"])
    types["CreateClusterRequestOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "parent": t.string().optional(),
            "zone": t.string().optional(),
            "cluster": t.proxy(renames["ClusterOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateClusterRequestOut"])
    types["JwkIn"] = t.struct(
        {
            "x": t.string().optional(),
            "kid": t.string().optional(),
            "crv": t.string().optional(),
            "n": t.string().optional(),
            "e": t.string().optional(),
            "alg": t.string().optional(),
            "y": t.string().optional(),
            "use": t.string().optional(),
            "kty": t.string().optional(),
        }
    ).named(renames["JwkIn"])
    types["JwkOut"] = t.struct(
        {
            "x": t.string().optional(),
            "kid": t.string().optional(),
            "crv": t.string().optional(),
            "n": t.string().optional(),
            "e": t.string().optional(),
            "alg": t.string().optional(),
            "y": t.string().optional(),
            "use": t.string().optional(),
            "kty": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwkOut"])
    types["PrivateClusterMasterGlobalAccessConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["PrivateClusterMasterGlobalAccessConfigIn"])
    types["PrivateClusterMasterGlobalAccessConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateClusterMasterGlobalAccessConfigOut"])
    types["SetLocationsRequestIn"] = t.struct(
        {
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "locations": t.array(t.string()),
        }
    ).named(renames["SetLocationsRequestIn"])
    types["SetLocationsRequestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "locations": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetLocationsRequestOut"])
    types["ManagedPrometheusConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["ManagedPrometheusConfigIn"])
    types["ManagedPrometheusConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedPrometheusConfigOut"])
    types["IntraNodeVisibilityConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["IntraNodeVisibilityConfigIn"])
    types["IntraNodeVisibilityConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntraNodeVisibilityConfigOut"])
    types["EphemeralStorageLocalSsdConfigIn"] = t.struct(
        {"localSsdCount": t.integer().optional()}
    ).named(renames["EphemeralStorageLocalSsdConfigIn"])
    types["EphemeralStorageLocalSsdConfigOut"] = t.struct(
        {
            "localSsdCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EphemeralStorageLocalSsdConfigOut"])
    types["ClusterAutoscalingIn"] = t.struct(
        {
            "autoscalingProfile": t.string().optional(),
            "enableNodeAutoprovisioning": t.boolean().optional(),
            "autoprovisioningLocations": t.array(t.string()).optional(),
            "resourceLimits": t.array(t.proxy(renames["ResourceLimitIn"])).optional(),
            "autoprovisioningNodePoolDefaults": t.proxy(
                renames["AutoprovisioningNodePoolDefaultsIn"]
            ).optional(),
        }
    ).named(renames["ClusterAutoscalingIn"])
    types["ClusterAutoscalingOut"] = t.struct(
        {
            "autoscalingProfile": t.string().optional(),
            "enableNodeAutoprovisioning": t.boolean().optional(),
            "autoprovisioningLocations": t.array(t.string()).optional(),
            "resourceLimits": t.array(t.proxy(renames["ResourceLimitOut"])).optional(),
            "autoprovisioningNodePoolDefaults": t.proxy(
                renames["AutoprovisioningNodePoolDefaultsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterAutoscalingOut"])
    types["PrivateClusterConfigIn"] = t.struct(
        {
            "enablePrivateNodes": t.boolean().optional(),
            "enablePrivateEndpoint": t.boolean().optional(),
            "masterIpv4CidrBlock": t.string().optional(),
            "publicEndpoint": t.string().optional(),
            "peeringName": t.string().optional(),
            "privateEndpoint": t.string().optional(),
            "masterGlobalAccessConfig": t.proxy(
                renames["PrivateClusterMasterGlobalAccessConfigIn"]
            ).optional(),
            "privateEndpointSubnetwork": t.string().optional(),
        }
    ).named(renames["PrivateClusterConfigIn"])
    types["PrivateClusterConfigOut"] = t.struct(
        {
            "enablePrivateNodes": t.boolean().optional(),
            "enablePrivateEndpoint": t.boolean().optional(),
            "masterIpv4CidrBlock": t.string().optional(),
            "publicEndpoint": t.string().optional(),
            "peeringName": t.string().optional(),
            "privateEndpoint": t.string().optional(),
            "masterGlobalAccessConfig": t.proxy(
                renames["PrivateClusterMasterGlobalAccessConfigOut"]
            ).optional(),
            "privateEndpointSubnetwork": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateClusterConfigOut"])
    types["DatabaseEncryptionIn"] = t.struct(
        {"keyName": t.string().optional(), "state": t.string().optional()}
    ).named(renames["DatabaseEncryptionIn"])
    types["DatabaseEncryptionOut"] = t.struct(
        {
            "keyName": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseEncryptionOut"])
    types["KubernetesDashboardIn"] = t.struct(
        {"disabled": t.boolean().optional()}
    ).named(renames["KubernetesDashboardIn"])
    types["KubernetesDashboardOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KubernetesDashboardOut"])
    types["SetNodePoolSizeRequestIn"] = t.struct(
        {
            "nodeCount": t.integer(),
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "projectId": t.string().optional(),
            "nodePoolId": t.string().optional(),
            "zone": t.string().optional(),
        }
    ).named(renames["SetNodePoolSizeRequestIn"])
    types["SetNodePoolSizeRequestOut"] = t.struct(
        {
            "nodeCount": t.integer(),
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "projectId": t.string().optional(),
            "nodePoolId": t.string().optional(),
            "zone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetNodePoolSizeRequestOut"])
    types["LoggingVariantConfigIn"] = t.struct(
        {"variant": t.string().optional()}
    ).named(renames["LoggingVariantConfigIn"])
    types["LoggingVariantConfigOut"] = t.struct(
        {
            "variant": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoggingVariantConfigOut"])
    types["ConfidentialNodesIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["ConfidentialNodesIn"]
    )
    types["ConfidentialNodesOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfidentialNodesOut"])
    types["ClientCertificateConfigIn"] = t.struct(
        {"issueClientCertificate": t.boolean().optional()}
    ).named(renames["ClientCertificateConfigIn"])
    types["ClientCertificateConfigOut"] = t.struct(
        {
            "issueClientCertificate": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientCertificateConfigOut"])
    types["ReleaseChannelIn"] = t.struct({"channel": t.string().optional()}).named(
        renames["ReleaseChannelIn"]
    )
    types["ReleaseChannelOut"] = t.struct(
        {
            "channel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseChannelOut"])
    types["ServerConfigIn"] = t.struct(
        {
            "defaultClusterVersion": t.string().optional(),
            "validNodeVersions": t.array(t.string()).optional(),
            "channels": t.array(t.proxy(renames["ReleaseChannelConfigIn"])).optional(),
            "defaultImageType": t.string().optional(),
            "validMasterVersions": t.array(t.string()).optional(),
            "validImageTypes": t.array(t.string()).optional(),
        }
    ).named(renames["ServerConfigIn"])
    types["ServerConfigOut"] = t.struct(
        {
            "defaultClusterVersion": t.string().optional(),
            "validNodeVersions": t.array(t.string()).optional(),
            "channels": t.array(t.proxy(renames["ReleaseChannelConfigOut"])).optional(),
            "defaultImageType": t.string().optional(),
            "validMasterVersions": t.array(t.string()).optional(),
            "validImageTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServerConfigOut"])
    types["UpdateNodePoolRequestIn"] = t.struct(
        {
            "kubeletConfig": t.proxy(renames["NodeKubeletConfigIn"]).optional(),
            "nodePoolId": t.string().optional(),
            "resourceLabels": t.proxy(renames["ResourceLabelsIn"]).optional(),
            "confidentialNodes": t.proxy(renames["ConfidentialNodesIn"]).optional(),
            "nodeVersion": t.string(),
            "clusterId": t.string().optional(),
            "gcfsConfig": t.proxy(renames["GcfsConfigIn"]).optional(),
            "upgradeSettings": t.proxy(renames["UpgradeSettingsIn"]).optional(),
            "etag": t.string().optional(),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "fastSocket": t.proxy(renames["FastSocketIn"]).optional(),
            "windowsNodeConfig": t.proxy(renames["WindowsNodeConfigIn"]).optional(),
            "tags": t.proxy(renames["NetworkTagsIn"]).optional(),
            "labels": t.proxy(renames["NodeLabelsIn"]).optional(),
            "imageType": t.string(),
            "linuxNodeConfig": t.proxy(renames["LinuxNodeConfigIn"]).optional(),
            "nodeNetworkConfig": t.proxy(renames["NodeNetworkConfigIn"]).optional(),
            "locations": t.array(t.string()).optional(),
            "workloadMetadataConfig": t.proxy(
                renames["WorkloadMetadataConfigIn"]
            ).optional(),
            "taints": t.proxy(renames["NodeTaintsIn"]).optional(),
            "name": t.string().optional(),
            "loggingConfig": t.proxy(renames["NodePoolLoggingConfigIn"]).optional(),
            "gvnic": t.proxy(renames["VirtualNICIn"]).optional(),
        }
    ).named(renames["UpdateNodePoolRequestIn"])
    types["UpdateNodePoolRequestOut"] = t.struct(
        {
            "kubeletConfig": t.proxy(renames["NodeKubeletConfigOut"]).optional(),
            "nodePoolId": t.string().optional(),
            "resourceLabels": t.proxy(renames["ResourceLabelsOut"]).optional(),
            "confidentialNodes": t.proxy(renames["ConfidentialNodesOut"]).optional(),
            "nodeVersion": t.string(),
            "clusterId": t.string().optional(),
            "gcfsConfig": t.proxy(renames["GcfsConfigOut"]).optional(),
            "upgradeSettings": t.proxy(renames["UpgradeSettingsOut"]).optional(),
            "etag": t.string().optional(),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "fastSocket": t.proxy(renames["FastSocketOut"]).optional(),
            "windowsNodeConfig": t.proxy(renames["WindowsNodeConfigOut"]).optional(),
            "tags": t.proxy(renames["NetworkTagsOut"]).optional(),
            "labels": t.proxy(renames["NodeLabelsOut"]).optional(),
            "imageType": t.string(),
            "linuxNodeConfig": t.proxy(renames["LinuxNodeConfigOut"]).optional(),
            "nodeNetworkConfig": t.proxy(renames["NodeNetworkConfigOut"]).optional(),
            "locations": t.array(t.string()).optional(),
            "workloadMetadataConfig": t.proxy(
                renames["WorkloadMetadataConfigOut"]
            ).optional(),
            "taints": t.proxy(renames["NodeTaintsOut"]).optional(),
            "name": t.string().optional(),
            "loggingConfig": t.proxy(renames["NodePoolLoggingConfigOut"]).optional(),
            "gvnic": t.proxy(renames["VirtualNICOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateNodePoolRequestOut"])
    types["WorkloadIdentityConfigIn"] = t.struct(
        {"workloadPool": t.string().optional()}
    ).named(renames["WorkloadIdentityConfigIn"])
    types["WorkloadIdentityConfigOut"] = t.struct(
        {
            "workloadPool": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkloadIdentityConfigOut"])
    types["LegacyAbacIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["LegacyAbacIn"]
    )
    types["LegacyAbacOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LegacyAbacOut"])
    types["UpdateClusterRequestIn"] = t.struct(
        {
            "clusterId": t.string().optional(),
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "update": t.proxy(renames["ClusterUpdateIn"]),
        }
    ).named(renames["UpdateClusterRequestIn"])
    types["UpdateClusterRequestOut"] = t.struct(
        {
            "clusterId": t.string().optional(),
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "update": t.proxy(renames["ClusterUpdateOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateClusterRequestOut"])
    types["IdentityServiceConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["IdentityServiceConfigIn"])
    types["IdentityServiceConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityServiceConfigOut"])
    types["ListNodePoolsResponseIn"] = t.struct(
        {"nodePools": t.array(t.proxy(renames["NodePoolIn"])).optional()}
    ).named(renames["ListNodePoolsResponseIn"])
    types["ListNodePoolsResponseOut"] = t.struct(
        {
            "nodePools": t.array(t.proxy(renames["NodePoolOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNodePoolsResponseOut"])
    types["SetNodePoolManagementRequestIn"] = t.struct(
        {
            "nodePoolId": t.string().optional(),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "management": t.proxy(renames["NodeManagementIn"]),
        }
    ).named(renames["SetNodePoolManagementRequestIn"])
    types["SetNodePoolManagementRequestOut"] = t.struct(
        {
            "nodePoolId": t.string().optional(),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "management": t.proxy(renames["NodeManagementOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetNodePoolManagementRequestOut"])
    types["MaxPodsConstraintIn"] = t.struct(
        {"maxPodsPerNode": t.string().optional()}
    ).named(renames["MaxPodsConstraintIn"])
    types["MaxPodsConstraintOut"] = t.struct(
        {
            "maxPodsPerNode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaxPodsConstraintOut"])
    types["MetricIn"] = t.struct(
        {
            "stringValue": t.string().optional(),
            "name": t.string(),
            "doubleValue": t.number().optional(),
            "intValue": t.string().optional(),
        }
    ).named(renames["MetricIn"])
    types["MetricOut"] = t.struct(
        {
            "stringValue": t.string().optional(),
            "name": t.string(),
            "doubleValue": t.number().optional(),
            "intValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricOut"])
    types["ResourceLabelsIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["ResourceLabelsIn"])
    types["ResourceLabelsOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceLabelsOut"])
    types["SetAddonsConfigRequestIn"] = t.struct(
        {
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "addonsConfig": t.proxy(renames["AddonsConfigIn"]),
            "name": t.string().optional(),
        }
    ).named(renames["SetAddonsConfigRequestIn"])
    types["SetAddonsConfigRequestOut"] = t.struct(
        {
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "addonsConfig": t.proxy(renames["AddonsConfigOut"]),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetAddonsConfigRequestOut"])
    types["LoggingComponentConfigIn"] = t.struct(
        {"enableComponents": t.array(t.string()).optional()}
    ).named(renames["LoggingComponentConfigIn"])
    types["LoggingComponentConfigOut"] = t.struct(
        {
            "enableComponents": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoggingComponentConfigOut"])
    types["NodePoolDefaultsIn"] = t.struct(
        {"nodeConfigDefaults": t.proxy(renames["NodeConfigDefaultsIn"]).optional()}
    ).named(renames["NodePoolDefaultsIn"])
    types["NodePoolDefaultsOut"] = t.struct(
        {
            "nodeConfigDefaults": t.proxy(renames["NodeConfigDefaultsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodePoolDefaultsOut"])
    types["ClusterUpdateIn"] = t.struct(
        {
            "desiredNodePoolLoggingConfig": t.proxy(
                renames["NodePoolLoggingConfigIn"]
            ).optional(),
            "desiredWorkloadIdentityConfig": t.proxy(
                renames["WorkloadIdentityConfigIn"]
            ).optional(),
            "removedAdditionalPodRangesConfig": t.proxy(
                renames["AdditionalPodRangesConfigIn"]
            ).optional(),
            "desiredBinaryAuthorization": t.proxy(
                renames["BinaryAuthorizationIn"]
            ).optional(),
            "desiredAddonsConfig": t.proxy(renames["AddonsConfigIn"]).optional(),
            "desiredServiceExternalIpsConfig": t.proxy(
                renames["ServiceExternalIPsConfigIn"]
            ).optional(),
            "desiredLoggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "desiredReleaseChannel": t.proxy(renames["ReleaseChannelIn"]).optional(),
            "desiredDnsConfig": t.proxy(renames["DNSConfigIn"]).optional(),
            "desiredIntraNodeVisibilityConfig": t.proxy(
                renames["IntraNodeVisibilityConfigIn"]
            ).optional(),
            "desiredMasterVersion": t.string().optional(),
            "desiredMeshCertificates": t.proxy(
                renames["MeshCertificatesIn"]
            ).optional(),
            "desiredClusterAutoscaling": t.proxy(
                renames["ClusterAutoscalingIn"]
            ).optional(),
            "desiredMonitoringConfig": t.proxy(
                renames["MonitoringConfigIn"]
            ).optional(),
            "desiredLocations": t.array(t.string()).optional(),
            "desiredNodePoolAutoConfigNetworkTags": t.proxy(
                renames["NetworkTagsIn"]
            ).optional(),
            "desiredShieldedNodes": t.proxy(renames["ShieldedNodesIn"]).optional(),
            "desiredNodeVersion": t.string().optional(),
            "desiredMasterAuthorizedNetworksConfig": t.proxy(
                renames["MasterAuthorizedNetworksConfigIn"]
            ).optional(),
            "desiredPrivateIpv6GoogleAccess": t.string().optional(),
            "desiredDatapathProvider": t.string().optional(),
            "desiredStackType": t.string().optional(),
            "desiredNotificationConfig": t.proxy(
                renames["NotificationConfigIn"]
            ).optional(),
            "desiredPrivateClusterConfig": t.proxy(
                renames["PrivateClusterConfigIn"]
            ).optional(),
            "desiredEnablePrivateEndpoint": t.boolean().optional(),
            "desiredFleet": t.proxy(renames["FleetIn"]).optional(),
            "desiredDefaultSnatStatus": t.proxy(
                renames["DefaultSnatStatusIn"]
            ).optional(),
            "desiredGcfsConfig": t.proxy(renames["GcfsConfigIn"]).optional(),
            "desiredAuthenticatorGroupsConfig": t.proxy(
                renames["AuthenticatorGroupsConfigIn"]
            ).optional(),
            "additionalPodRangesConfig": t.proxy(
                renames["AdditionalPodRangesConfigIn"]
            ).optional(),
            "desiredNodePoolAutoscaling": t.proxy(
                renames["NodePoolAutoscalingIn"]
            ).optional(),
            "desiredGatewayApiConfig": t.proxy(
                renames["GatewayAPIConfigIn"]
            ).optional(),
            "desiredLoggingService": t.string().optional(),
            "etag": t.string().optional(),
            "desiredImageType": t.string().optional(),
            "desiredVerticalPodAutoscaling": t.proxy(
                renames["VerticalPodAutoscalingIn"]
            ).optional(),
            "desiredIdentityServiceConfig": t.proxy(
                renames["IdentityServiceConfigIn"]
            ).optional(),
            "desiredMonitoringService": t.string().optional(),
            "desiredDatabaseEncryption": t.proxy(
                renames["DatabaseEncryptionIn"]
            ).optional(),
            "desiredCostManagementConfig": t.proxy(
                renames["CostManagementConfigIn"]
            ).optional(),
            "desiredResourceUsageExportConfig": t.proxy(
                renames["ResourceUsageExportConfigIn"]
            ).optional(),
            "desiredNodePoolId": t.string().optional(),
            "desiredL4ilbSubsettingConfig": t.proxy(
                renames["ILBSubsettingConfigIn"]
            ).optional(),
        }
    ).named(renames["ClusterUpdateIn"])
    types["ClusterUpdateOut"] = t.struct(
        {
            "desiredNodePoolLoggingConfig": t.proxy(
                renames["NodePoolLoggingConfigOut"]
            ).optional(),
            "desiredWorkloadIdentityConfig": t.proxy(
                renames["WorkloadIdentityConfigOut"]
            ).optional(),
            "removedAdditionalPodRangesConfig": t.proxy(
                renames["AdditionalPodRangesConfigOut"]
            ).optional(),
            "desiredBinaryAuthorization": t.proxy(
                renames["BinaryAuthorizationOut"]
            ).optional(),
            "desiredAddonsConfig": t.proxy(renames["AddonsConfigOut"]).optional(),
            "desiredServiceExternalIpsConfig": t.proxy(
                renames["ServiceExternalIPsConfigOut"]
            ).optional(),
            "desiredLoggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "desiredReleaseChannel": t.proxy(renames["ReleaseChannelOut"]).optional(),
            "desiredDnsConfig": t.proxy(renames["DNSConfigOut"]).optional(),
            "desiredIntraNodeVisibilityConfig": t.proxy(
                renames["IntraNodeVisibilityConfigOut"]
            ).optional(),
            "desiredMasterVersion": t.string().optional(),
            "desiredMeshCertificates": t.proxy(
                renames["MeshCertificatesOut"]
            ).optional(),
            "desiredClusterAutoscaling": t.proxy(
                renames["ClusterAutoscalingOut"]
            ).optional(),
            "desiredMonitoringConfig": t.proxy(
                renames["MonitoringConfigOut"]
            ).optional(),
            "desiredLocations": t.array(t.string()).optional(),
            "desiredNodePoolAutoConfigNetworkTags": t.proxy(
                renames["NetworkTagsOut"]
            ).optional(),
            "desiredShieldedNodes": t.proxy(renames["ShieldedNodesOut"]).optional(),
            "desiredNodeVersion": t.string().optional(),
            "desiredMasterAuthorizedNetworksConfig": t.proxy(
                renames["MasterAuthorizedNetworksConfigOut"]
            ).optional(),
            "desiredPrivateIpv6GoogleAccess": t.string().optional(),
            "desiredDatapathProvider": t.string().optional(),
            "desiredStackType": t.string().optional(),
            "desiredNotificationConfig": t.proxy(
                renames["NotificationConfigOut"]
            ).optional(),
            "desiredPrivateClusterConfig": t.proxy(
                renames["PrivateClusterConfigOut"]
            ).optional(),
            "desiredEnablePrivateEndpoint": t.boolean().optional(),
            "desiredFleet": t.proxy(renames["FleetOut"]).optional(),
            "desiredDefaultSnatStatus": t.proxy(
                renames["DefaultSnatStatusOut"]
            ).optional(),
            "desiredGcfsConfig": t.proxy(renames["GcfsConfigOut"]).optional(),
            "desiredAuthenticatorGroupsConfig": t.proxy(
                renames["AuthenticatorGroupsConfigOut"]
            ).optional(),
            "additionalPodRangesConfig": t.proxy(
                renames["AdditionalPodRangesConfigOut"]
            ).optional(),
            "desiredNodePoolAutoscaling": t.proxy(
                renames["NodePoolAutoscalingOut"]
            ).optional(),
            "desiredGatewayApiConfig": t.proxy(
                renames["GatewayAPIConfigOut"]
            ).optional(),
            "desiredLoggingService": t.string().optional(),
            "etag": t.string().optional(),
            "desiredImageType": t.string().optional(),
            "desiredVerticalPodAutoscaling": t.proxy(
                renames["VerticalPodAutoscalingOut"]
            ).optional(),
            "desiredIdentityServiceConfig": t.proxy(
                renames["IdentityServiceConfigOut"]
            ).optional(),
            "desiredMonitoringService": t.string().optional(),
            "desiredDatabaseEncryption": t.proxy(
                renames["DatabaseEncryptionOut"]
            ).optional(),
            "desiredCostManagementConfig": t.proxy(
                renames["CostManagementConfigOut"]
            ).optional(),
            "desiredResourceUsageExportConfig": t.proxy(
                renames["ResourceUsageExportConfigOut"]
            ).optional(),
            "desiredNodePoolId": t.string().optional(),
            "desiredL4ilbSubsettingConfig": t.proxy(
                renames["ILBSubsettingConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterUpdateOut"])
    types["NetworkPerformanceConfigIn"] = t.struct(
        {"totalEgressBandwidthTier": t.string().optional()}
    ).named(renames["NetworkPerformanceConfigIn"])
    types["NetworkPerformanceConfigOut"] = t.struct(
        {
            "totalEgressBandwidthTier": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkPerformanceConfigOut"])
    types["GatewayAPIConfigIn"] = t.struct({"channel": t.string().optional()}).named(
        renames["GatewayAPIConfigIn"]
    )
    types["GatewayAPIConfigOut"] = t.struct(
        {
            "channel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GatewayAPIConfigOut"])
    types["NetworkConfigIn"] = t.struct(
        {
            "serviceExternalIpsConfig": t.proxy(
                renames["ServiceExternalIPsConfigIn"]
            ).optional(),
            "dnsConfig": t.proxy(renames["DNSConfigIn"]).optional(),
            "enableL4ilbSubsetting": t.boolean().optional(),
            "network": t.string().optional(),
            "defaultSnatStatus": t.proxy(renames["DefaultSnatStatusIn"]).optional(),
            "gatewayApiConfig": t.proxy(renames["GatewayAPIConfigIn"]).optional(),
            "enableIntraNodeVisibility": t.boolean().optional(),
            "privateIpv6GoogleAccess": t.string().optional(),
            "datapathProvider": t.string().optional(),
            "subnetwork": t.string().optional(),
        }
    ).named(renames["NetworkConfigIn"])
    types["NetworkConfigOut"] = t.struct(
        {
            "serviceExternalIpsConfig": t.proxy(
                renames["ServiceExternalIPsConfigOut"]
            ).optional(),
            "dnsConfig": t.proxy(renames["DNSConfigOut"]).optional(),
            "enableL4ilbSubsetting": t.boolean().optional(),
            "network": t.string().optional(),
            "defaultSnatStatus": t.proxy(renames["DefaultSnatStatusOut"]).optional(),
            "gatewayApiConfig": t.proxy(renames["GatewayAPIConfigOut"]).optional(),
            "enableIntraNodeVisibility": t.boolean().optional(),
            "privateIpv6GoogleAccess": t.string().optional(),
            "datapathProvider": t.string().optional(),
            "subnetwork": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConfigOut"])
    types["MasterAuthIn"] = t.struct(
        {
            "clientKey": t.string().optional(),
            "password": t.string().optional(),
            "username": t.string().optional(),
            "clientCertificateConfig": t.proxy(
                renames["ClientCertificateConfigIn"]
            ).optional(),
            "clusterCaCertificate": t.string().optional(),
            "clientCertificate": t.string().optional(),
        }
    ).named(renames["MasterAuthIn"])
    types["MasterAuthOut"] = t.struct(
        {
            "clientKey": t.string().optional(),
            "password": t.string().optional(),
            "username": t.string().optional(),
            "clientCertificateConfig": t.proxy(
                renames["ClientCertificateConfigOut"]
            ).optional(),
            "clusterCaCertificate": t.string().optional(),
            "clientCertificate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MasterAuthOut"])
    types["AutoUpgradeOptionsIn"] = t.struct(
        {
            "autoUpgradeStartTime": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["AutoUpgradeOptionsIn"])
    types["AutoUpgradeOptionsOut"] = t.struct(
        {
            "autoUpgradeStartTime": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoUpgradeOptionsOut"])
    types["StatusConditionIn"] = t.struct(
        {
            "code": t.string().optional(),
            "message": t.string().optional(),
            "canonicalCode": t.string().optional(),
        }
    ).named(renames["StatusConditionIn"])
    types["StatusConditionOut"] = t.struct(
        {
            "code": t.string().optional(),
            "message": t.string().optional(),
            "canonicalCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusConditionOut"])
    types["NetworkTagsIn"] = t.struct({"tags": t.array(t.string()).optional()}).named(
        renames["NetworkTagsIn"]
    )
    types["NetworkTagsOut"] = t.struct(
        {
            "tags": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkTagsOut"])
    types["FilterIn"] = t.struct({"eventType": t.array(t.string()).optional()}).named(
        renames["FilterIn"]
    )
    types["FilterOut"] = t.struct(
        {
            "eventType": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterOut"])
    types["ListUsableSubnetworksResponseIn"] = t.struct(
        {
            "subnetworks": t.array(t.proxy(renames["UsableSubnetworkIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListUsableSubnetworksResponseIn"])
    types["ListUsableSubnetworksResponseOut"] = t.struct(
        {
            "subnetworks": t.array(t.proxy(renames["UsableSubnetworkOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUsableSubnetworksResponseOut"])
    types["NodeNetworkConfigIn"] = t.struct(
        {
            "createPodRange": t.boolean().optional(),
            "podIpv4CidrBlock": t.string().optional(),
            "podRange": t.string().optional(),
            "networkPerformanceConfig": t.proxy(
                renames["NetworkPerformanceConfigIn"]
            ).optional(),
            "enablePrivateNodes": t.boolean().optional(),
            "podCidrOverprovisionConfig": t.proxy(
                renames["PodCIDROverprovisionConfigIn"]
            ).optional(),
        }
    ).named(renames["NodeNetworkConfigIn"])
    types["NodeNetworkConfigOut"] = t.struct(
        {
            "createPodRange": t.boolean().optional(),
            "podIpv4CidrBlock": t.string().optional(),
            "podRange": t.string().optional(),
            "networkPerformanceConfig": t.proxy(
                renames["NetworkPerformanceConfigOut"]
            ).optional(),
            "enablePrivateNodes": t.boolean().optional(),
            "podCidrOverprovisionConfig": t.proxy(
                renames["PodCIDROverprovisionConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeNetworkConfigOut"])
    types["WindowsNodeConfigIn"] = t.struct({"osVersion": t.string().optional()}).named(
        renames["WindowsNodeConfigIn"]
    )
    types["WindowsNodeConfigOut"] = t.struct(
        {
            "osVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsNodeConfigOut"])
    types["WorkloadMetadataConfigIn"] = t.struct({"mode": t.string().optional()}).named(
        renames["WorkloadMetadataConfigIn"]
    )
    types["WorkloadMetadataConfigOut"] = t.struct(
        {
            "mode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkloadMetadataConfigOut"])
    types["NodeTaintsIn"] = t.struct(
        {"taints": t.array(t.proxy(renames["NodeTaintIn"])).optional()}
    ).named(renames["NodeTaintsIn"])
    types["NodeTaintsOut"] = t.struct(
        {
            "taints": t.array(t.proxy(renames["NodeTaintOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeTaintsOut"])
    types["DailyMaintenanceWindowIn"] = t.struct(
        {"duration": t.string().optional(), "startTime": t.string().optional()}
    ).named(renames["DailyMaintenanceWindowIn"])
    types["DailyMaintenanceWindowOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DailyMaintenanceWindowOut"])
    types["GPUSharingConfigIn"] = t.struct(
        {
            "gpuSharingStrategy": t.string().optional(),
            "maxSharedClientsPerGpu": t.string().optional(),
        }
    ).named(renames["GPUSharingConfigIn"])
    types["GPUSharingConfigOut"] = t.struct(
        {
            "gpuSharingStrategy": t.string().optional(),
            "maxSharedClientsPerGpu": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GPUSharingConfigOut"])
    types["ListClustersResponseIn"] = t.struct(
        {
            "clusters": t.array(t.proxy(renames["ClusterIn"])).optional(),
            "missingZones": t.array(t.string()).optional(),
        }
    ).named(renames["ListClustersResponseIn"])
    types["ListClustersResponseOut"] = t.struct(
        {
            "clusters": t.array(t.proxy(renames["ClusterOut"])).optional(),
            "missingZones": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListClustersResponseOut"])
    types["ShieldedNodesIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["ShieldedNodesIn"]
    )
    types["ShieldedNodesOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShieldedNodesOut"])
    types["SandboxConfigIn"] = t.struct({"type": t.string().optional()}).named(
        renames["SandboxConfigIn"]
    )
    types["SandboxConfigOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SandboxConfigOut"])
    types["AddonsConfigIn"] = t.struct(
        {
            "networkPolicyConfig": t.proxy(renames["NetworkPolicyConfigIn"]).optional(),
            "kubernetesDashboard": t.proxy(renames["KubernetesDashboardIn"]).optional(),
            "gcePersistentDiskCsiDriverConfig": t.proxy(
                renames["GcePersistentDiskCsiDriverConfigIn"]
            ).optional(),
            "gkeBackupAgentConfig": t.proxy(
                renames["GkeBackupAgentConfigIn"]
            ).optional(),
            "horizontalPodAutoscaling": t.proxy(
                renames["HorizontalPodAutoscalingIn"]
            ).optional(),
            "httpLoadBalancing": t.proxy(renames["HttpLoadBalancingIn"]).optional(),
            "dnsCacheConfig": t.proxy(renames["DnsCacheConfigIn"]).optional(),
            "cloudRunConfig": t.proxy(renames["CloudRunConfigIn"]).optional(),
            "configConnectorConfig": t.proxy(
                renames["ConfigConnectorConfigIn"]
            ).optional(),
            "gcpFilestoreCsiDriverConfig": t.proxy(
                renames["GcpFilestoreCsiDriverConfigIn"]
            ).optional(),
        }
    ).named(renames["AddonsConfigIn"])
    types["AddonsConfigOut"] = t.struct(
        {
            "networkPolicyConfig": t.proxy(
                renames["NetworkPolicyConfigOut"]
            ).optional(),
            "kubernetesDashboard": t.proxy(
                renames["KubernetesDashboardOut"]
            ).optional(),
            "gcePersistentDiskCsiDriverConfig": t.proxy(
                renames["GcePersistentDiskCsiDriverConfigOut"]
            ).optional(),
            "gkeBackupAgentConfig": t.proxy(
                renames["GkeBackupAgentConfigOut"]
            ).optional(),
            "horizontalPodAutoscaling": t.proxy(
                renames["HorizontalPodAutoscalingOut"]
            ).optional(),
            "httpLoadBalancing": t.proxy(renames["HttpLoadBalancingOut"]).optional(),
            "dnsCacheConfig": t.proxy(renames["DnsCacheConfigOut"]).optional(),
            "cloudRunConfig": t.proxy(renames["CloudRunConfigOut"]).optional(),
            "configConnectorConfig": t.proxy(
                renames["ConfigConnectorConfigOut"]
            ).optional(),
            "gcpFilestoreCsiDriverConfig": t.proxy(
                renames["GcpFilestoreCsiDriverConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddonsConfigOut"])
    types["StandardRolloutPolicyIn"] = t.struct(
        {
            "batchSoakDuration": t.string().optional(),
            "batchPercentage": t.number().optional(),
            "batchNodeCount": t.integer().optional(),
        }
    ).named(renames["StandardRolloutPolicyIn"])
    types["StandardRolloutPolicyOut"] = t.struct(
        {
            "batchSoakDuration": t.string().optional(),
            "batchPercentage": t.number().optional(),
            "batchNodeCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StandardRolloutPolicyOut"])
    types["CloudRunConfigIn"] = t.struct(
        {"loadBalancerType": t.string().optional(), "disabled": t.boolean().optional()}
    ).named(renames["CloudRunConfigIn"])
    types["CloudRunConfigOut"] = t.struct(
        {
            "loadBalancerType": t.string().optional(),
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRunConfigOut"])
    types["CancelOperationRequestIn"] = t.struct(
        {
            "operationId": t.string().optional(),
            "name": t.string().optional(),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["CancelOperationRequestIn"])
    types["CancelOperationRequestOut"] = t.struct(
        {
            "operationId": t.string().optional(),
            "name": t.string().optional(),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CancelOperationRequestOut"])
    types["DNSConfigIn"] = t.struct(
        {
            "clusterDns": t.string().optional(),
            "clusterDnsScope": t.string().optional(),
            "clusterDnsDomain": t.string().optional(),
        }
    ).named(renames["DNSConfigIn"])
    types["DNSConfigOut"] = t.struct(
        {
            "clusterDns": t.string().optional(),
            "clusterDnsScope": t.string().optional(),
            "clusterDnsDomain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DNSConfigOut"])
    types["UsableSubnetworkIn"] = t.struct(
        {
            "statusMessage": t.string().optional(),
            "network": t.string().optional(),
            "secondaryIpRanges": t.array(
                t.proxy(renames["UsableSubnetworkSecondaryRangeIn"])
            ).optional(),
            "ipCidrRange": t.string().optional(),
            "subnetwork": t.string().optional(),
        }
    ).named(renames["UsableSubnetworkIn"])
    types["UsableSubnetworkOut"] = t.struct(
        {
            "statusMessage": t.string().optional(),
            "network": t.string().optional(),
            "secondaryIpRanges": t.array(
                t.proxy(renames["UsableSubnetworkSecondaryRangeOut"])
            ).optional(),
            "ipCidrRange": t.string().optional(),
            "subnetwork": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsableSubnetworkOut"])
    types["SetMaintenancePolicyRequestIn"] = t.struct(
        {
            "zone": t.string(),
            "clusterId": t.string(),
            "name": t.string().optional(),
            "projectId": t.string(),
            "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
        }
    ).named(renames["SetMaintenancePolicyRequestIn"])
    types["SetMaintenancePolicyRequestOut"] = t.struct(
        {
            "zone": t.string(),
            "clusterId": t.string(),
            "name": t.string().optional(),
            "projectId": t.string(),
            "maintenancePolicy": t.proxy(renames["MaintenancePolicyOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetMaintenancePolicyRequestOut"])
    types["CreateNodePoolRequestIn"] = t.struct(
        {
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
            "projectId": t.string().optional(),
            "parent": t.string().optional(),
            "nodePool": t.proxy(renames["NodePoolIn"]),
        }
    ).named(renames["CreateNodePoolRequestIn"])
    types["CreateNodePoolRequestOut"] = t.struct(
        {
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
            "projectId": t.string().optional(),
            "parent": t.string().optional(),
            "nodePool": t.proxy(renames["NodePoolOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateNodePoolRequestOut"])
    types["StartIPRotationRequestIn"] = t.struct(
        {
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "projectId": t.string().optional(),
            "rotateCredentials": t.boolean().optional(),
            "zone": t.string().optional(),
        }
    ).named(renames["StartIPRotationRequestIn"])
    types["StartIPRotationRequestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "projectId": t.string().optional(),
            "rotateCredentials": t.boolean().optional(),
            "zone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartIPRotationRequestOut"])
    types["GetOpenIDConfigResponseIn"] = t.struct(
        {
            "jwks_uri": t.string().optional(),
            "response_types_supported": t.array(t.string()).optional(),
            "subject_types_supported": t.array(t.string()).optional(),
            "id_token_signing_alg_values_supported": t.array(t.string()).optional(),
            "issuer": t.string().optional(),
            "cacheHeader": t.proxy(
                renames["HttpCacheControlResponseHeaderIn"]
            ).optional(),
            "claims_supported": t.array(t.string()).optional(),
            "grant_types": t.array(t.string()).optional(),
        }
    ).named(renames["GetOpenIDConfigResponseIn"])
    types["GetOpenIDConfigResponseOut"] = t.struct(
        {
            "jwks_uri": t.string().optional(),
            "response_types_supported": t.array(t.string()).optional(),
            "subject_types_supported": t.array(t.string()).optional(),
            "id_token_signing_alg_values_supported": t.array(t.string()).optional(),
            "issuer": t.string().optional(),
            "cacheHeader": t.proxy(
                renames["HttpCacheControlResponseHeaderOut"]
            ).optional(),
            "claims_supported": t.array(t.string()).optional(),
            "grant_types": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetOpenIDConfigResponseOut"])
    types["BlueGreenInfoIn"] = t.struct(
        {
            "blueInstanceGroupUrls": t.array(t.string()).optional(),
            "phase": t.string().optional(),
            "greenInstanceGroupUrls": t.array(t.string()).optional(),
            "bluePoolDeletionStartTime": t.string().optional(),
            "greenPoolVersion": t.string().optional(),
        }
    ).named(renames["BlueGreenInfoIn"])
    types["BlueGreenInfoOut"] = t.struct(
        {
            "blueInstanceGroupUrls": t.array(t.string()).optional(),
            "phase": t.string().optional(),
            "greenInstanceGroupUrls": t.array(t.string()).optional(),
            "bluePoolDeletionStartTime": t.string().optional(),
            "greenPoolVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BlueGreenInfoOut"])
    types["SetLabelsRequestIn"] = t.struct(
        {
            "clusterId": t.string().optional(),
            "labelFingerprint": t.string(),
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "resourceLabels": t.struct({"_": t.string().optional()}),
        }
    ).named(renames["SetLabelsRequestIn"])
    types["SetLabelsRequestOut"] = t.struct(
        {
            "clusterId": t.string().optional(),
            "labelFingerprint": t.string(),
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "resourceLabels": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetLabelsRequestOut"])
    types["MonitoringConfigIn"] = t.struct(
        {
            "managedPrometheusConfig": t.proxy(
                renames["ManagedPrometheusConfigIn"]
            ).optional(),
            "componentConfig": t.proxy(
                renames["MonitoringComponentConfigIn"]
            ).optional(),
        }
    ).named(renames["MonitoringConfigIn"])
    types["MonitoringConfigOut"] = t.struct(
        {
            "managedPrometheusConfig": t.proxy(
                renames["ManagedPrometheusConfigOut"]
            ).optional(),
            "componentConfig": t.proxy(
                renames["MonitoringComponentConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoringConfigOut"])
    types["NodePoolAutoConfigIn"] = t.struct(
        {"networkTags": t.proxy(renames["NetworkTagsIn"]).optional()}
    ).named(renames["NodePoolAutoConfigIn"])
    types["NodePoolAutoConfigOut"] = t.struct(
        {
            "networkTags": t.proxy(renames["NetworkTagsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodePoolAutoConfigOut"])
    types["UpdateMasterRequestIn"] = t.struct(
        {
            "masterVersion": t.string(),
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["UpdateMasterRequestIn"])
    types["UpdateMasterRequestOut"] = t.struct(
        {
            "masterVersion": t.string(),
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateMasterRequestOut"])
    types["CompleteNodePoolUpgradeRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CompleteNodePoolUpgradeRequestIn"])
    types["CompleteNodePoolUpgradeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CompleteNodePoolUpgradeRequestOut"])
    types["ShieldedInstanceConfigIn"] = t.struct(
        {
            "enableSecureBoot": t.boolean().optional(),
            "enableIntegrityMonitoring": t.boolean().optional(),
        }
    ).named(renames["ShieldedInstanceConfigIn"])
    types["ShieldedInstanceConfigOut"] = t.struct(
        {
            "enableSecureBoot": t.boolean().optional(),
            "enableIntegrityMonitoring": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShieldedInstanceConfigOut"])
    types["FastSocketIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["FastSocketIn"]
    )
    types["FastSocketOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FastSocketOut"])
    types["GcpFilestoreCsiDriverConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["GcpFilestoreCsiDriverConfigIn"])
    types["GcpFilestoreCsiDriverConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcpFilestoreCsiDriverConfigOut"])
    types["NotificationConfigIn"] = t.struct(
        {"pubsub": t.proxy(renames["PubSubIn"]).optional()}
    ).named(renames["NotificationConfigIn"])
    types["NotificationConfigOut"] = t.struct(
        {
            "pubsub": t.proxy(renames["PubSubOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationConfigOut"])
    types["NodeConfigDefaultsIn"] = t.struct(
        {
            "loggingConfig": t.proxy(renames["NodePoolLoggingConfigIn"]).optional(),
            "gcfsConfig": t.proxy(renames["GcfsConfigIn"]).optional(),
        }
    ).named(renames["NodeConfigDefaultsIn"])
    types["NodeConfigDefaultsOut"] = t.struct(
        {
            "loggingConfig": t.proxy(renames["NodePoolLoggingConfigOut"]).optional(),
            "gcfsConfig": t.proxy(renames["GcfsConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeConfigDefaultsOut"])
    types["ReservationAffinityIn"] = t.struct(
        {
            "key": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "consumeReservationType": t.string().optional(),
        }
    ).named(renames["ReservationAffinityIn"])
    types["ReservationAffinityOut"] = t.struct(
        {
            "key": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "consumeReservationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReservationAffinityOut"])
    types["HttpLoadBalancingIn"] = t.struct({"disabled": t.boolean().optional()}).named(
        renames["HttpLoadBalancingIn"]
    )
    types["HttpLoadBalancingOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpLoadBalancingOut"])
    types["ReleaseChannelConfigIn"] = t.struct(
        {
            "channel": t.string().optional(),
            "validVersions": t.array(t.string()).optional(),
            "defaultVersion": t.string().optional(),
        }
    ).named(renames["ReleaseChannelConfigIn"])
    types["ReleaseChannelConfigOut"] = t.struct(
        {
            "channel": t.string().optional(),
            "validVersions": t.array(t.string()).optional(),
            "defaultVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseChannelConfigOut"])
    types["PlacementPolicyIn"] = t.struct({"type": t.string().optional()}).named(
        renames["PlacementPolicyIn"]
    )
    types["PlacementPolicyOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacementPolicyOut"])
    types["AuthenticatorGroupsConfigIn"] = t.struct(
        {"enabled": t.boolean().optional(), "securityGroup": t.string().optional()}
    ).named(renames["AuthenticatorGroupsConfigIn"])
    types["AuthenticatorGroupsConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "securityGroup": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthenticatorGroupsConfigOut"])
    types["GcePersistentDiskCsiDriverConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["GcePersistentDiskCsiDriverConfigIn"])
    types["GcePersistentDiskCsiDriverConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcePersistentDiskCsiDriverConfigOut"])
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
    types["ClusterIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "resourceLabels": t.struct({"_": t.string().optional()}).optional(),
            "shieldedNodes": t.proxy(renames["ShieldedNodesIn"]).optional(),
            "enableTpu": t.boolean().optional(),
            "locations": t.array(t.string()).optional(),
            "networkPolicy": t.proxy(renames["NetworkPolicyIn"]).optional(),
            "endpoint": t.string().optional(),
            "ipAllocationPolicy": t.proxy(renames["IPAllocationPolicyIn"]).optional(),
            "meshCertificates": t.proxy(renames["MeshCertificatesIn"]).optional(),
            "verticalPodAutoscaling": t.proxy(
                renames["VerticalPodAutoscalingIn"]
            ).optional(),
            "expireTime": t.string().optional(),
            "masterAuth": t.proxy(renames["MasterAuthIn"]).optional(),
            "enableKubernetesAlpha": t.boolean().optional(),
            "nodePoolDefaults": t.proxy(renames["NodePoolDefaultsIn"]).optional(),
            "tpuIpv4CidrBlock": t.string().optional(),
            "instanceGroupUrls": t.array(t.string()).optional(),
            "releaseChannel": t.proxy(renames["ReleaseChannelIn"]).optional(),
            "location": t.string().optional(),
            "subnetwork": t.string().optional(),
            "clusterIpv4Cidr": t.string().optional(),
            "workloadIdentityConfig": t.proxy(
                renames["WorkloadIdentityConfigIn"]
            ).optional(),
            "binaryAuthorization": t.proxy(renames["BinaryAuthorizationIn"]).optional(),
            "loggingService": t.string().optional(),
            "network": t.string().optional(),
            "autoscaling": t.proxy(renames["ClusterAutoscalingIn"]).optional(),
            "nodeConfig": t.proxy(renames["NodeConfigIn"]).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "databaseEncryption": t.proxy(renames["DatabaseEncryptionIn"]).optional(),
            "notificationConfig": t.proxy(renames["NotificationConfigIn"]).optional(),
            "currentMasterVersion": t.string().optional(),
            "legacyAbac": t.proxy(renames["LegacyAbacIn"]).optional(),
            "selfLink": t.string().optional(),
            "autopilot": t.proxy(renames["AutopilotIn"]).optional(),
            "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]).optional(),
            "nodePoolAutoConfig": t.proxy(renames["NodePoolAutoConfigIn"]).optional(),
            "conditions": t.array(t.proxy(renames["StatusConditionIn"])).optional(),
            "currentNodeCount": t.integer().optional(),
            "servicesIpv4Cidr": t.string().optional(),
            "authenticatorGroupsConfig": t.proxy(
                renames["AuthenticatorGroupsConfigIn"]
            ).optional(),
            "initialClusterVersion": t.string().optional(),
            "fleet": t.proxy(renames["FleetIn"]).optional(),
            "statusMessage": t.string().optional(),
            "status": t.string().optional(),
            "monitoringService": t.string().optional(),
            "createTime": t.string().optional(),
            "identityServiceConfig": t.proxy(
                renames["IdentityServiceConfigIn"]
            ).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "resourceUsageExportConfig": t.proxy(
                renames["ResourceUsageExportConfigIn"]
            ).optional(),
            "nodePools": t.array(t.proxy(renames["NodePoolIn"])).optional(),
            "zone": t.string().optional(),
            "initialNodeCount": t.integer().optional(),
            "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
            "currentNodeVersion": t.string().optional(),
            "addonsConfig": t.proxy(renames["AddonsConfigIn"]).optional(),
            "costManagementConfig": t.proxy(
                renames["CostManagementConfigIn"]
            ).optional(),
            "privateClusterConfig": t.proxy(
                renames["PrivateClusterConfigIn"]
            ).optional(),
            "nodeIpv4CidrSize": t.integer().optional(),
            "labelFingerprint": t.string().optional(),
            "monitoringConfig": t.proxy(renames["MonitoringConfigIn"]).optional(),
            "confidentialNodes": t.proxy(renames["ConfidentialNodesIn"]).optional(),
            "masterAuthorizedNetworksConfig": t.proxy(
                renames["MasterAuthorizedNetworksConfigIn"]
            ).optional(),
            "defaultMaxPodsConstraint": t.proxy(
                renames["MaxPodsConstraintIn"]
            ).optional(),
        }
    ).named(renames["ClusterIn"])
    types["ClusterOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "resourceLabels": t.struct({"_": t.string().optional()}).optional(),
            "shieldedNodes": t.proxy(renames["ShieldedNodesOut"]).optional(),
            "enableTpu": t.boolean().optional(),
            "locations": t.array(t.string()).optional(),
            "networkPolicy": t.proxy(renames["NetworkPolicyOut"]).optional(),
            "endpoint": t.string().optional(),
            "ipAllocationPolicy": t.proxy(renames["IPAllocationPolicyOut"]).optional(),
            "meshCertificates": t.proxy(renames["MeshCertificatesOut"]).optional(),
            "id": t.string().optional(),
            "verticalPodAutoscaling": t.proxy(
                renames["VerticalPodAutoscalingOut"]
            ).optional(),
            "expireTime": t.string().optional(),
            "masterAuth": t.proxy(renames["MasterAuthOut"]).optional(),
            "enableKubernetesAlpha": t.boolean().optional(),
            "nodePoolDefaults": t.proxy(renames["NodePoolDefaultsOut"]).optional(),
            "tpuIpv4CidrBlock": t.string().optional(),
            "instanceGroupUrls": t.array(t.string()).optional(),
            "releaseChannel": t.proxy(renames["ReleaseChannelOut"]).optional(),
            "location": t.string().optional(),
            "subnetwork": t.string().optional(),
            "clusterIpv4Cidr": t.string().optional(),
            "workloadIdentityConfig": t.proxy(
                renames["WorkloadIdentityConfigOut"]
            ).optional(),
            "binaryAuthorization": t.proxy(
                renames["BinaryAuthorizationOut"]
            ).optional(),
            "loggingService": t.string().optional(),
            "network": t.string().optional(),
            "autoscaling": t.proxy(renames["ClusterAutoscalingOut"]).optional(),
            "nodeConfig": t.proxy(renames["NodeConfigOut"]).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "databaseEncryption": t.proxy(renames["DatabaseEncryptionOut"]).optional(),
            "notificationConfig": t.proxy(renames["NotificationConfigOut"]).optional(),
            "currentMasterVersion": t.string().optional(),
            "legacyAbac": t.proxy(renames["LegacyAbacOut"]).optional(),
            "selfLink": t.string().optional(),
            "autopilot": t.proxy(renames["AutopilotOut"]).optional(),
            "maintenancePolicy": t.proxy(renames["MaintenancePolicyOut"]).optional(),
            "nodePoolAutoConfig": t.proxy(renames["NodePoolAutoConfigOut"]).optional(),
            "conditions": t.array(t.proxy(renames["StatusConditionOut"])).optional(),
            "currentNodeCount": t.integer().optional(),
            "servicesIpv4Cidr": t.string().optional(),
            "authenticatorGroupsConfig": t.proxy(
                renames["AuthenticatorGroupsConfigOut"]
            ).optional(),
            "initialClusterVersion": t.string().optional(),
            "fleet": t.proxy(renames["FleetOut"]).optional(),
            "statusMessage": t.string().optional(),
            "status": t.string().optional(),
            "monitoringService": t.string().optional(),
            "createTime": t.string().optional(),
            "identityServiceConfig": t.proxy(
                renames["IdentityServiceConfigOut"]
            ).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "resourceUsageExportConfig": t.proxy(
                renames["ResourceUsageExportConfigOut"]
            ).optional(),
            "nodePools": t.array(t.proxy(renames["NodePoolOut"])).optional(),
            "zone": t.string().optional(),
            "initialNodeCount": t.integer().optional(),
            "networkConfig": t.proxy(renames["NetworkConfigOut"]).optional(),
            "currentNodeVersion": t.string().optional(),
            "addonsConfig": t.proxy(renames["AddonsConfigOut"]).optional(),
            "costManagementConfig": t.proxy(
                renames["CostManagementConfigOut"]
            ).optional(),
            "privateClusterConfig": t.proxy(
                renames["PrivateClusterConfigOut"]
            ).optional(),
            "nodeIpv4CidrSize": t.integer().optional(),
            "labelFingerprint": t.string().optional(),
            "monitoringConfig": t.proxy(renames["MonitoringConfigOut"]).optional(),
            "confidentialNodes": t.proxy(renames["ConfidentialNodesOut"]).optional(),
            "masterAuthorizedNetworksConfig": t.proxy(
                renames["MasterAuthorizedNetworksConfigOut"]
            ).optional(),
            "defaultMaxPodsConstraint": t.proxy(
                renames["MaxPodsConstraintOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterOut"])
    types["VirtualNICIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["VirtualNICIn"]
    )
    types["VirtualNICOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualNICOut"])
    types["NetworkPolicyIn"] = t.struct(
        {"provider": t.string().optional(), "enabled": t.boolean().optional()}
    ).named(renames["NetworkPolicyIn"])
    types["NetworkPolicyOut"] = t.struct(
        {
            "provider": t.string().optional(),
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkPolicyOut"])
    types["AdvancedMachineFeaturesIn"] = t.struct(
        {"threadsPerCore": t.string().optional()}
    ).named(renames["AdvancedMachineFeaturesIn"])
    types["AdvancedMachineFeaturesOut"] = t.struct(
        {
            "threadsPerCore": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvancedMachineFeaturesOut"])
    types["GkeBackupAgentConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["GkeBackupAgentConfigIn"])
    types["GkeBackupAgentConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeBackupAgentConfigOut"])
    types["PubSubIn"] = t.struct(
        {
            "filter": t.proxy(renames["FilterIn"]).optional(),
            "enabled": t.boolean().optional(),
            "topic": t.string().optional(),
        }
    ).named(renames["PubSubIn"])
    types["PubSubOut"] = t.struct(
        {
            "filter": t.proxy(renames["FilterOut"]).optional(),
            "enabled": t.boolean().optional(),
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubSubOut"])
    types["NodeManagementIn"] = t.struct(
        {
            "autoUpgrade": t.boolean().optional(),
            "upgradeOptions": t.proxy(renames["AutoUpgradeOptionsIn"]).optional(),
            "autoRepair": t.boolean().optional(),
        }
    ).named(renames["NodeManagementIn"])
    types["NodeManagementOut"] = t.struct(
        {
            "autoUpgrade": t.boolean().optional(),
            "upgradeOptions": t.proxy(renames["AutoUpgradeOptionsOut"]).optional(),
            "autoRepair": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeManagementOut"])
    types["ServiceExternalIPsConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["ServiceExternalIPsConfigIn"])
    types["ServiceExternalIPsConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceExternalIPsConfigOut"])
    types["DefaultSnatStatusIn"] = t.struct({"disabled": t.boolean().optional()}).named(
        renames["DefaultSnatStatusIn"]
    )
    types["DefaultSnatStatusOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DefaultSnatStatusOut"])
    types["SetMonitoringServiceRequestIn"] = t.struct(
        {
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "monitoringService": t.string(),
            "projectId": t.string().optional(),
        }
    ).named(renames["SetMonitoringServiceRequestIn"])
    types["SetMonitoringServiceRequestOut"] = t.struct(
        {
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "monitoringService": t.string(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetMonitoringServiceRequestOut"])
    types["BlueGreenSettingsIn"] = t.struct(
        {
            "nodePoolSoakDuration": t.string().optional(),
            "standardRolloutPolicy": t.proxy(
                renames["StandardRolloutPolicyIn"]
            ).optional(),
        }
    ).named(renames["BlueGreenSettingsIn"])
    types["BlueGreenSettingsOut"] = t.struct(
        {
            "nodePoolSoakDuration": t.string().optional(),
            "standardRolloutPolicy": t.proxy(
                renames["StandardRolloutPolicyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BlueGreenSettingsOut"])
    types["NetworkPolicyConfigIn"] = t.struct(
        {"disabled": t.boolean().optional()}
    ).named(renames["NetworkPolicyConfigIn"])
    types["NetworkPolicyConfigOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkPolicyConfigOut"])
    types["UpgradeAvailableEventIn"] = t.struct(
        {
            "resource": t.string().optional(),
            "releaseChannel": t.proxy(renames["ReleaseChannelIn"]).optional(),
            "version": t.string().optional(),
            "resourceType": t.string().optional(),
        }
    ).named(renames["UpgradeAvailableEventIn"])
    types["UpgradeAvailableEventOut"] = t.struct(
        {
            "resource": t.string().optional(),
            "releaseChannel": t.proxy(renames["ReleaseChannelOut"]).optional(),
            "version": t.string().optional(),
            "resourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeAvailableEventOut"])
    types["MeshCertificatesIn"] = t.struct(
        {"enableCertificates": t.boolean().optional()}
    ).named(renames["MeshCertificatesIn"])
    types["MeshCertificatesOut"] = t.struct(
        {
            "enableCertificates": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MeshCertificatesOut"])
    types["AcceleratorConfigIn"] = t.struct(
        {
            "gpuPartitionSize": t.string().optional(),
            "acceleratorCount": t.string().optional(),
            "gpuSharingConfig": t.proxy(renames["GPUSharingConfigIn"]).optional(),
            "acceleratorType": t.string().optional(),
        }
    ).named(renames["AcceleratorConfigIn"])
    types["AcceleratorConfigOut"] = t.struct(
        {
            "gpuPartitionSize": t.string().optional(),
            "acceleratorCount": t.string().optional(),
            "gpuSharingConfig": t.proxy(renames["GPUSharingConfigOut"]).optional(),
            "acceleratorType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceleratorConfigOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["MaintenanceExclusionOptionsIn"] = t.struct(
        {"scope": t.string().optional()}
    ).named(renames["MaintenanceExclusionOptionsIn"])
    types["MaintenanceExclusionOptionsOut"] = t.struct(
        {
            "scope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceExclusionOptionsOut"])
    types["ResourceLimitIn"] = t.struct(
        {
            "minimum": t.string().optional(),
            "resourceType": t.string().optional(),
            "maximum": t.string().optional(),
        }
    ).named(renames["ResourceLimitIn"])
    types["ResourceLimitOut"] = t.struct(
        {
            "minimum": t.string().optional(),
            "resourceType": t.string().optional(),
            "maximum": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceLimitOut"])
    types["NodePoolLoggingConfigIn"] = t.struct(
        {"variantConfig": t.proxy(renames["LoggingVariantConfigIn"]).optional()}
    ).named(renames["NodePoolLoggingConfigIn"])
    types["NodePoolLoggingConfigOut"] = t.struct(
        {
            "variantConfig": t.proxy(renames["LoggingVariantConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodePoolLoggingConfigOut"])
    types["NodePoolIn"] = t.struct(
        {
            "upgradeSettings": t.proxy(renames["UpgradeSettingsIn"]).optional(),
            "etag": t.string().optional(),
            "placementPolicy": t.proxy(renames["PlacementPolicyIn"]).optional(),
            "selfLink": t.string().optional(),
            "podIpv4CidrSize": t.integer().optional(),
            "config": t.proxy(renames["NodeConfigIn"]).optional(),
            "instanceGroupUrls": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "networkConfig": t.proxy(renames["NodeNetworkConfigIn"]).optional(),
            "initialNodeCount": t.integer().optional(),
            "management": t.proxy(renames["NodeManagementIn"]).optional(),
            "conditions": t.array(t.proxy(renames["StatusConditionIn"])).optional(),
            "name": t.string().optional(),
            "version": t.string().optional(),
            "locations": t.array(t.string()).optional(),
            "autoscaling": t.proxy(renames["NodePoolAutoscalingIn"]).optional(),
            "statusMessage": t.string().optional(),
            "maxPodsConstraint": t.proxy(renames["MaxPodsConstraintIn"]).optional(),
        }
    ).named(renames["NodePoolIn"])
    types["NodePoolOut"] = t.struct(
        {
            "upgradeSettings": t.proxy(renames["UpgradeSettingsOut"]).optional(),
            "etag": t.string().optional(),
            "placementPolicy": t.proxy(renames["PlacementPolicyOut"]).optional(),
            "selfLink": t.string().optional(),
            "podIpv4CidrSize": t.integer().optional(),
            "config": t.proxy(renames["NodeConfigOut"]).optional(),
            "instanceGroupUrls": t.array(t.string()).optional(),
            "status": t.string().optional(),
            "networkConfig": t.proxy(renames["NodeNetworkConfigOut"]).optional(),
            "initialNodeCount": t.integer().optional(),
            "management": t.proxy(renames["NodeManagementOut"]).optional(),
            "conditions": t.array(t.proxy(renames["StatusConditionOut"])).optional(),
            "updateInfo": t.proxy(renames["UpdateInfoOut"]).optional(),
            "name": t.string().optional(),
            "version": t.string().optional(),
            "locations": t.array(t.string()).optional(),
            "autoscaling": t.proxy(renames["NodePoolAutoscalingOut"]).optional(),
            "statusMessage": t.string().optional(),
            "maxPodsConstraint": t.proxy(renames["MaxPodsConstraintOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodePoolOut"])
    types["AdditionalPodRangesConfigIn"] = t.struct(
        {"podRangeNames": t.array(t.string()).optional()}
    ).named(renames["AdditionalPodRangesConfigIn"])
    types["AdditionalPodRangesConfigOut"] = t.struct(
        {
            "podRangeNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdditionalPodRangesConfigOut"])
    types["RecurringTimeWindowIn"] = t.struct(
        {
            "recurrence": t.string().optional(),
            "window": t.proxy(renames["TimeWindowIn"]).optional(),
        }
    ).named(renames["RecurringTimeWindowIn"])
    types["RecurringTimeWindowOut"] = t.struct(
        {
            "recurrence": t.string().optional(),
            "window": t.proxy(renames["TimeWindowOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecurringTimeWindowOut"])
    types["UpgradeSettingsIn"] = t.struct(
        {
            "strategy": t.string().optional(),
            "maxSurge": t.integer().optional(),
            "maxUnavailable": t.integer().optional(),
            "blueGreenSettings": t.proxy(renames["BlueGreenSettingsIn"]).optional(),
        }
    ).named(renames["UpgradeSettingsIn"])
    types["UpgradeSettingsOut"] = t.struct(
        {
            "strategy": t.string().optional(),
            "maxSurge": t.integer().optional(),
            "maxUnavailable": t.integer().optional(),
            "blueGreenSettings": t.proxy(renames["BlueGreenSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeSettingsOut"])
    types["UpgradeEventIn"] = t.struct(
        {
            "operationStartTime": t.string().optional(),
            "operation": t.string().optional(),
            "currentVersion": t.string().optional(),
            "resource": t.string().optional(),
            "resourceType": t.string().optional(),
            "targetVersion": t.string().optional(),
        }
    ).named(renames["UpgradeEventIn"])
    types["UpgradeEventOut"] = t.struct(
        {
            "operationStartTime": t.string().optional(),
            "operation": t.string().optional(),
            "currentVersion": t.string().optional(),
            "resource": t.string().optional(),
            "resourceType": t.string().optional(),
            "targetVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeEventOut"])
    types["SetNodePoolAutoscalingRequestIn"] = t.struct(
        {
            "name": t.string().optional(),
            "nodePoolId": t.string().optional(),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "clusterId": t.string().optional(),
            "autoscaling": t.proxy(renames["NodePoolAutoscalingIn"]),
        }
    ).named(renames["SetNodePoolAutoscalingRequestIn"])
    types["SetNodePoolAutoscalingRequestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "nodePoolId": t.string().optional(),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "clusterId": t.string().optional(),
            "autoscaling": t.proxy(renames["NodePoolAutoscalingOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetNodePoolAutoscalingRequestOut"])
    types["SetLegacyAbacRequestIn"] = t.struct(
        {
            "enabled": t.boolean(),
            "clusterId": t.string().optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
        }
    ).named(renames["SetLegacyAbacRequestIn"])
    types["SetLegacyAbacRequestOut"] = t.struct(
        {
            "enabled": t.boolean(),
            "clusterId": t.string().optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetLegacyAbacRequestOut"])
    types["LocalNvmeSsdBlockConfigIn"] = t.struct(
        {"localSsdCount": t.integer().optional()}
    ).named(renames["LocalNvmeSsdBlockConfigIn"])
    types["LocalNvmeSsdBlockConfigOut"] = t.struct(
        {
            "localSsdCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalNvmeSsdBlockConfigOut"])
    types["ConsumptionMeteringConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["ConsumptionMeteringConfigIn"])
    types["ConsumptionMeteringConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsumptionMeteringConfigOut"])
    types["NodeConfigIn"] = t.struct(
        {
            "spot": t.boolean().optional(),
            "nodeGroup": t.string().optional(),
            "linuxNodeConfig": t.proxy(renames["LinuxNodeConfigIn"]).optional(),
            "localNvmeSsdBlockConfig": t.proxy(
                renames["LocalNvmeSsdBlockConfigIn"]
            ).optional(),
            "diskSizeGb": t.integer().optional(),
            "localSsdCount": t.integer().optional(),
            "ephemeralStorageLocalSsdConfig": t.proxy(
                renames["EphemeralStorageLocalSsdConfigIn"]
            ).optional(),
            "sandboxConfig": t.proxy(renames["SandboxConfigIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "minCpuPlatform": t.string().optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigIn"]
            ).optional(),
            "advancedMachineFeatures": t.proxy(
                renames["AdvancedMachineFeaturesIn"]
            ).optional(),
            "windowsNodeConfig": t.proxy(renames["WindowsNodeConfigIn"]).optional(),
            "kubeletConfig": t.proxy(renames["NodeKubeletConfigIn"]).optional(),
            "bootDiskKmsKey": t.string().optional(),
            "gvnic": t.proxy(renames["VirtualNICIn"]).optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "taints": t.array(t.proxy(renames["NodeTaintIn"])).optional(),
            "imageType": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "resourceLabels": t.struct({"_": t.string().optional()}).optional(),
            "confidentialNodes": t.proxy(renames["ConfidentialNodesIn"]).optional(),
            "fastSocket": t.proxy(renames["FastSocketIn"]).optional(),
            "serviceAccount": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "preemptible": t.boolean().optional(),
            "loggingConfig": t.proxy(renames["NodePoolLoggingConfigIn"]).optional(),
            "gcfsConfig": t.proxy(renames["GcfsConfigIn"]).optional(),
            "workloadMetadataConfig": t.proxy(
                renames["WorkloadMetadataConfigIn"]
            ).optional(),
            "reservationAffinity": t.proxy(renames["ReservationAffinityIn"]).optional(),
            "machineType": t.string().optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorConfigIn"])).optional(),
            "diskType": t.string().optional(),
        }
    ).named(renames["NodeConfigIn"])
    types["NodeConfigOut"] = t.struct(
        {
            "spot": t.boolean().optional(),
            "nodeGroup": t.string().optional(),
            "linuxNodeConfig": t.proxy(renames["LinuxNodeConfigOut"]).optional(),
            "localNvmeSsdBlockConfig": t.proxy(
                renames["LocalNvmeSsdBlockConfigOut"]
            ).optional(),
            "diskSizeGb": t.integer().optional(),
            "localSsdCount": t.integer().optional(),
            "ephemeralStorageLocalSsdConfig": t.proxy(
                renames["EphemeralStorageLocalSsdConfigOut"]
            ).optional(),
            "sandboxConfig": t.proxy(renames["SandboxConfigOut"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "minCpuPlatform": t.string().optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigOut"]
            ).optional(),
            "advancedMachineFeatures": t.proxy(
                renames["AdvancedMachineFeaturesOut"]
            ).optional(),
            "windowsNodeConfig": t.proxy(renames["WindowsNodeConfigOut"]).optional(),
            "kubeletConfig": t.proxy(renames["NodeKubeletConfigOut"]).optional(),
            "bootDiskKmsKey": t.string().optional(),
            "gvnic": t.proxy(renames["VirtualNICOut"]).optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "taints": t.array(t.proxy(renames["NodeTaintOut"])).optional(),
            "imageType": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "resourceLabels": t.struct({"_": t.string().optional()}).optional(),
            "confidentialNodes": t.proxy(renames["ConfidentialNodesOut"]).optional(),
            "fastSocket": t.proxy(renames["FastSocketOut"]).optional(),
            "serviceAccount": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "preemptible": t.boolean().optional(),
            "loggingConfig": t.proxy(renames["NodePoolLoggingConfigOut"]).optional(),
            "gcfsConfig": t.proxy(renames["GcfsConfigOut"]).optional(),
            "workloadMetadataConfig": t.proxy(
                renames["WorkloadMetadataConfigOut"]
            ).optional(),
            "reservationAffinity": t.proxy(
                renames["ReservationAffinityOut"]
            ).optional(),
            "machineType": t.string().optional(),
            "accelerators": t.array(
                t.proxy(renames["AcceleratorConfigOut"])
            ).optional(),
            "diskType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeConfigOut"])
    types["SetLoggingServiceRequestIn"] = t.struct(
        {
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "loggingService": t.string(),
        }
    ).named(renames["SetLoggingServiceRequestIn"])
    types["SetLoggingServiceRequestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "loggingService": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetLoggingServiceRequestOut"])
    types["SetNetworkPolicyRequestIn"] = t.struct(
        {
            "clusterId": t.string().optional(),
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "networkPolicy": t.proxy(renames["NetworkPolicyIn"]),
        }
    ).named(renames["SetNetworkPolicyRequestIn"])
    types["SetNetworkPolicyRequestOut"] = t.struct(
        {
            "clusterId": t.string().optional(),
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "networkPolicy": t.proxy(renames["NetworkPolicyOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetNetworkPolicyRequestOut"])

    functions = {}
    functions["projectsLocationsGetServerConfig"] = container.get(
        "v1/{name}/serverConfig",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServerConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersStartIpRotation"] = container.post(
        "v1/{name}:setLegacyAbac",
        t.struct(
            {
                "name": t.string().optional(),
                "enabled": t.boolean(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersDelete"] = container.post(
        "v1/{name}:setLegacyAbac",
        t.struct(
            {
                "name": t.string().optional(),
                "enabled": t.boolean(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetResourceLabels"] = container.post(
        "v1/{name}:setLegacyAbac",
        t.struct(
            {
                "name": t.string().optional(),
                "enabled": t.boolean(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersUpdate"] = container.post(
        "v1/{name}:setLegacyAbac",
        t.struct(
            {
                "name": t.string().optional(),
                "enabled": t.boolean(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetMonitoring"] = container.post(
        "v1/{name}:setLegacyAbac",
        t.struct(
            {
                "name": t.string().optional(),
                "enabled": t.boolean(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersCompleteIpRotation"] = container.post(
        "v1/{name}:setLegacyAbac",
        t.struct(
            {
                "name": t.string().optional(),
                "enabled": t.boolean(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersCreate"] = container.post(
        "v1/{name}:setLegacyAbac",
        t.struct(
            {
                "name": t.string().optional(),
                "enabled": t.boolean(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersGetJwks"] = container.post(
        "v1/{name}:setLegacyAbac",
        t.struct(
            {
                "name": t.string().optional(),
                "enabled": t.boolean(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetMasterAuth"] = container.post(
        "v1/{name}:setLegacyAbac",
        t.struct(
            {
                "name": t.string().optional(),
                "enabled": t.boolean(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersList"] = container.post(
        "v1/{name}:setLegacyAbac",
        t.struct(
            {
                "name": t.string().optional(),
                "enabled": t.boolean(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetNetworkPolicy"] = container.post(
        "v1/{name}:setLegacyAbac",
        t.struct(
            {
                "name": t.string().optional(),
                "enabled": t.boolean(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetLogging"] = container.post(
        "v1/{name}:setLegacyAbac",
        t.struct(
            {
                "name": t.string().optional(),
                "enabled": t.boolean(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersGet"] = container.post(
        "v1/{name}:setLegacyAbac",
        t.struct(
            {
                "name": t.string().optional(),
                "enabled": t.boolean(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetAddons"] = container.post(
        "v1/{name}:setLegacyAbac",
        t.struct(
            {
                "name": t.string().optional(),
                "enabled": t.boolean(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetLocations"] = container.post(
        "v1/{name}:setLegacyAbac",
        t.struct(
            {
                "name": t.string().optional(),
                "enabled": t.boolean(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetMaintenancePolicy"] = container.post(
        "v1/{name}:setLegacyAbac",
        t.struct(
            {
                "name": t.string().optional(),
                "enabled": t.boolean(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersUpdateMaster"] = container.post(
        "v1/{name}:setLegacyAbac",
        t.struct(
            {
                "name": t.string().optional(),
                "enabled": t.boolean(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetLegacyAbac"] = container.post(
        "v1/{name}:setLegacyAbac",
        t.struct(
            {
                "name": t.string().optional(),
                "enabled": t.boolean(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsCreate"] = container.get(
        "v1/{parent}/nodePools",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsSetManagement"] = container.get(
        "v1/{parent}/nodePools",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsSetSize"] = container.get(
        "v1/{parent}/nodePools",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsRollback"] = container.get(
        "v1/{parent}/nodePools",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsSetAutoscaling"] = container.get(
        "v1/{parent}/nodePools",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsDelete"] = container.get(
        "v1/{parent}/nodePools",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsCompleteUpgrade"] = container.get(
        "v1/{parent}/nodePools",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsGet"] = container.get(
        "v1/{parent}/nodePools",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsUpdate"] = container.get(
        "v1/{parent}/nodePools",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsList"] = container.get(
        "v1/{parent}/nodePools",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsClustersWell-knownGetOpenid-configuration"
    ] = container.get(
        "v1/{parent}/.well-known/openid-configuration",
        t.struct({"parent": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GetOpenIDConfigResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = container.get(
        "v1/{parent}/operations",
        t.struct(
            {
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = container.get(
        "v1/{parent}/operations",
        t.struct(
            {
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = container.get(
        "v1/{parent}/operations",
        t.struct(
            {
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAggregatedUsableSubnetworksList"] = container.get(
        "v1/{parent}/aggregated/usableSubnetworks",
        t.struct(
            {
                "parent": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUsableSubnetworksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesGetServerconfig"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/serverconfig",
        t.struct(
            {
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServerConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesOperationsCancel"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/operations",
        t.struct(
            {
                "parent": t.string().optional(),
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesOperationsGet"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/operations",
        t.struct(
            {
                "parent": t.string().optional(),
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesOperationsList"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/operations",
        t.struct(
            {
                "parent": t.string().optional(),
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersLocations"] = container.put(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}",
        t.struct(
            {
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "update": t.proxy(renames["ClusterUpdateIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersLogging"] = container.put(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}",
        t.struct(
            {
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "update": t.proxy(renames["ClusterUpdateIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersMaster"] = container.put(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}",
        t.struct(
            {
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "update": t.proxy(renames["ClusterUpdateIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersSetMasterAuth"] = container.put(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}",
        t.struct(
            {
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "update": t.proxy(renames["ClusterUpdateIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersMonitoring"] = container.put(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}",
        t.struct(
            {
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "update": t.proxy(renames["ClusterUpdateIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersCreate"] = container.put(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}",
        t.struct(
            {
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "update": t.proxy(renames["ClusterUpdateIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersAddons"] = container.put(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}",
        t.struct(
            {
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "update": t.proxy(renames["ClusterUpdateIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersLegacyAbac"] = container.put(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}",
        t.struct(
            {
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "update": t.proxy(renames["ClusterUpdateIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersStartIpRotation"] = container.put(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}",
        t.struct(
            {
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "update": t.proxy(renames["ClusterUpdateIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersSetNetworkPolicy"] = container.put(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}",
        t.struct(
            {
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "update": t.proxy(renames["ClusterUpdateIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersDelete"] = container.put(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}",
        t.struct(
            {
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "update": t.proxy(renames["ClusterUpdateIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersGet"] = container.put(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}",
        t.struct(
            {
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "update": t.proxy(renames["ClusterUpdateIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersList"] = container.put(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}",
        t.struct(
            {
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "update": t.proxy(renames["ClusterUpdateIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersCompleteIpRotation"] = container.put(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}",
        t.struct(
            {
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "update": t.proxy(renames["ClusterUpdateIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersSetMaintenancePolicy"] = container.put(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}",
        t.struct(
            {
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "update": t.proxy(renames["ClusterUpdateIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersResourceLabels"] = container.put(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}",
        t.struct(
            {
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "update": t.proxy(renames["ClusterUpdateIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersUpdate"] = container.put(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}",
        t.struct(
            {
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "update": t.proxy(renames["ClusterUpdateIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsList"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/autoscaling",
        t.struct(
            {
                "nodePoolId": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "autoscaling": t.proxy(renames["NodePoolAutoscalingIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsCreate"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/autoscaling",
        t.struct(
            {
                "nodePoolId": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "autoscaling": t.proxy(renames["NodePoolAutoscalingIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsSetSize"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/autoscaling",
        t.struct(
            {
                "nodePoolId": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "autoscaling": t.proxy(renames["NodePoolAutoscalingIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsUpdate"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/autoscaling",
        t.struct(
            {
                "nodePoolId": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "autoscaling": t.proxy(renames["NodePoolAutoscalingIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsDelete"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/autoscaling",
        t.struct(
            {
                "nodePoolId": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "autoscaling": t.proxy(renames["NodePoolAutoscalingIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsSetManagement"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/autoscaling",
        t.struct(
            {
                "nodePoolId": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "autoscaling": t.proxy(renames["NodePoolAutoscalingIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsGet"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/autoscaling",
        t.struct(
            {
                "nodePoolId": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "autoscaling": t.proxy(renames["NodePoolAutoscalingIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsRollback"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/autoscaling",
        t.struct(
            {
                "nodePoolId": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "autoscaling": t.proxy(renames["NodePoolAutoscalingIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsAutoscaling"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/autoscaling",
        t.struct(
            {
                "nodePoolId": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "autoscaling": t.proxy(renames["NodePoolAutoscalingIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="container", renames=renames, types=types, functions=functions
    )
