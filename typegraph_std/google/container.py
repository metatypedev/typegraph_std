from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_container() -> Import:
    container = HTTPRuntime("https://container.googleapis.com/")

    renames = {
        "ErrorResponse": "_container_1_ErrorResponse",
        "DatabaseEncryptionIn": "_container_2_DatabaseEncryptionIn",
        "DatabaseEncryptionOut": "_container_3_DatabaseEncryptionOut",
        "ServerConfigIn": "_container_4_ServerConfigIn",
        "ServerConfigOut": "_container_5_ServerConfigOut",
        "GcePersistentDiskCsiDriverConfigIn": "_container_6_GcePersistentDiskCsiDriverConfigIn",
        "GcePersistentDiskCsiDriverConfigOut": "_container_7_GcePersistentDiskCsiDriverConfigOut",
        "ResourceLabelsIn": "_container_8_ResourceLabelsIn",
        "ResourceLabelsOut": "_container_9_ResourceLabelsOut",
        "ServiceExternalIPsConfigIn": "_container_10_ServiceExternalIPsConfigIn",
        "ServiceExternalIPsConfigOut": "_container_11_ServiceExternalIPsConfigOut",
        "NodeLabelsIn": "_container_12_NodeLabelsIn",
        "NodeLabelsOut": "_container_13_NodeLabelsOut",
        "SetAddonsConfigRequestIn": "_container_14_SetAddonsConfigRequestIn",
        "SetAddonsConfigRequestOut": "_container_15_SetAddonsConfigRequestOut",
        "MaintenanceWindowIn": "_container_16_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_container_17_MaintenanceWindowOut",
        "NodeConfigIn": "_container_18_NodeConfigIn",
        "NodeConfigOut": "_container_19_NodeConfigOut",
        "ShieldedNodesIn": "_container_20_ShieldedNodesIn",
        "ShieldedNodesOut": "_container_21_ShieldedNodesOut",
        "DNSConfigIn": "_container_22_DNSConfigIn",
        "DNSConfigOut": "_container_23_DNSConfigOut",
        "HttpCacheControlResponseHeaderIn": "_container_24_HttpCacheControlResponseHeaderIn",
        "HttpCacheControlResponseHeaderOut": "_container_25_HttpCacheControlResponseHeaderOut",
        "CompleteNodePoolUpgradeRequestIn": "_container_26_CompleteNodePoolUpgradeRequestIn",
        "CompleteNodePoolUpgradeRequestOut": "_container_27_CompleteNodePoolUpgradeRequestOut",
        "VerticalPodAutoscalingIn": "_container_28_VerticalPodAutoscalingIn",
        "VerticalPodAutoscalingOut": "_container_29_VerticalPodAutoscalingOut",
        "AutoprovisioningNodePoolDefaultsIn": "_container_30_AutoprovisioningNodePoolDefaultsIn",
        "AutoprovisioningNodePoolDefaultsOut": "_container_31_AutoprovisioningNodePoolDefaultsOut",
        "VirtualNICIn": "_container_32_VirtualNICIn",
        "VirtualNICOut": "_container_33_VirtualNICOut",
        "NodePoolAutoscalingIn": "_container_34_NodePoolAutoscalingIn",
        "NodePoolAutoscalingOut": "_container_35_NodePoolAutoscalingOut",
        "CidrBlockIn": "_container_36_CidrBlockIn",
        "CidrBlockOut": "_container_37_CidrBlockOut",
        "SetMaintenancePolicyRequestIn": "_container_38_SetMaintenancePolicyRequestIn",
        "SetMaintenancePolicyRequestOut": "_container_39_SetMaintenancePolicyRequestOut",
        "BigQueryDestinationIn": "_container_40_BigQueryDestinationIn",
        "BigQueryDestinationOut": "_container_41_BigQueryDestinationOut",
        "AutoUpgradeOptionsIn": "_container_42_AutoUpgradeOptionsIn",
        "AutoUpgradeOptionsOut": "_container_43_AutoUpgradeOptionsOut",
        "OperationProgressIn": "_container_44_OperationProgressIn",
        "OperationProgressOut": "_container_45_OperationProgressOut",
        "AuthenticatorGroupsConfigIn": "_container_46_AuthenticatorGroupsConfigIn",
        "AuthenticatorGroupsConfigOut": "_container_47_AuthenticatorGroupsConfigOut",
        "PrivateClusterConfigIn": "_container_48_PrivateClusterConfigIn",
        "PrivateClusterConfigOut": "_container_49_PrivateClusterConfigOut",
        "ClusterIn": "_container_50_ClusterIn",
        "ClusterOut": "_container_51_ClusterOut",
        "CancelOperationRequestIn": "_container_52_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_container_53_CancelOperationRequestOut",
        "UsableSubnetworkSecondaryRangeIn": "_container_54_UsableSubnetworkSecondaryRangeIn",
        "UsableSubnetworkSecondaryRangeOut": "_container_55_UsableSubnetworkSecondaryRangeOut",
        "SetMonitoringServiceRequestIn": "_container_56_SetMonitoringServiceRequestIn",
        "SetMonitoringServiceRequestOut": "_container_57_SetMonitoringServiceRequestOut",
        "AdditionalPodRangesConfigIn": "_container_58_AdditionalPodRangesConfigIn",
        "AdditionalPodRangesConfigOut": "_container_59_AdditionalPodRangesConfigOut",
        "CostManagementConfigIn": "_container_60_CostManagementConfigIn",
        "CostManagementConfigOut": "_container_61_CostManagementConfigOut",
        "CreateNodePoolRequestIn": "_container_62_CreateNodePoolRequestIn",
        "CreateNodePoolRequestOut": "_container_63_CreateNodePoolRequestOut",
        "WorkloadMetadataConfigIn": "_container_64_WorkloadMetadataConfigIn",
        "WorkloadMetadataConfigOut": "_container_65_WorkloadMetadataConfigOut",
        "ListClustersResponseIn": "_container_66_ListClustersResponseIn",
        "ListClustersResponseOut": "_container_67_ListClustersResponseOut",
        "MonitoringConfigIn": "_container_68_MonitoringConfigIn",
        "MonitoringConfigOut": "_container_69_MonitoringConfigOut",
        "DailyMaintenanceWindowIn": "_container_70_DailyMaintenanceWindowIn",
        "DailyMaintenanceWindowOut": "_container_71_DailyMaintenanceWindowOut",
        "SecurityBulletinEventIn": "_container_72_SecurityBulletinEventIn",
        "SecurityBulletinEventOut": "_container_73_SecurityBulletinEventOut",
        "BinaryAuthorizationIn": "_container_74_BinaryAuthorizationIn",
        "BinaryAuthorizationOut": "_container_75_BinaryAuthorizationOut",
        "ClientCertificateConfigIn": "_container_76_ClientCertificateConfigIn",
        "ClientCertificateConfigOut": "_container_77_ClientCertificateConfigOut",
        "MasterAuthorizedNetworksConfigIn": "_container_78_MasterAuthorizedNetworksConfigIn",
        "MasterAuthorizedNetworksConfigOut": "_container_79_MasterAuthorizedNetworksConfigOut",
        "NodePoolDefaultsIn": "_container_80_NodePoolDefaultsIn",
        "NodePoolDefaultsOut": "_container_81_NodePoolDefaultsOut",
        "ShieldedInstanceConfigIn": "_container_82_ShieldedInstanceConfigIn",
        "ShieldedInstanceConfigOut": "_container_83_ShieldedInstanceConfigOut",
        "AdvancedMachineFeaturesIn": "_container_84_AdvancedMachineFeaturesIn",
        "AdvancedMachineFeaturesOut": "_container_85_AdvancedMachineFeaturesOut",
        "IdentityServiceConfigIn": "_container_86_IdentityServiceConfigIn",
        "IdentityServiceConfigOut": "_container_87_IdentityServiceConfigOut",
        "CompleteIPRotationRequestIn": "_container_88_CompleteIPRotationRequestIn",
        "CompleteIPRotationRequestOut": "_container_89_CompleteIPRotationRequestOut",
        "ListNodePoolsResponseIn": "_container_90_ListNodePoolsResponseIn",
        "ListNodePoolsResponseOut": "_container_91_ListNodePoolsResponseOut",
        "ResourceUsageExportConfigIn": "_container_92_ResourceUsageExportConfigIn",
        "ResourceUsageExportConfigOut": "_container_93_ResourceUsageExportConfigOut",
        "WorkloadIdentityConfigIn": "_container_94_WorkloadIdentityConfigIn",
        "WorkloadIdentityConfigOut": "_container_95_WorkloadIdentityConfigOut",
        "ResourceLimitIn": "_container_96_ResourceLimitIn",
        "ResourceLimitOut": "_container_97_ResourceLimitOut",
        "GkeBackupAgentConfigIn": "_container_98_GkeBackupAgentConfigIn",
        "GkeBackupAgentConfigOut": "_container_99_GkeBackupAgentConfigOut",
        "StandardRolloutPolicyIn": "_container_100_StandardRolloutPolicyIn",
        "StandardRolloutPolicyOut": "_container_101_StandardRolloutPolicyOut",
        "NetworkPolicyIn": "_container_102_NetworkPolicyIn",
        "NetworkPolicyOut": "_container_103_NetworkPolicyOut",
        "NodeNetworkConfigIn": "_container_104_NodeNetworkConfigIn",
        "NodeNetworkConfigOut": "_container_105_NodeNetworkConfigOut",
        "UpdateClusterRequestIn": "_container_106_UpdateClusterRequestIn",
        "UpdateClusterRequestOut": "_container_107_UpdateClusterRequestOut",
        "NodeTaintsIn": "_container_108_NodeTaintsIn",
        "NodeTaintsOut": "_container_109_NodeTaintsOut",
        "ListUsableSubnetworksResponseIn": "_container_110_ListUsableSubnetworksResponseIn",
        "ListUsableSubnetworksResponseOut": "_container_111_ListUsableSubnetworksResponseOut",
        "GPUSharingConfigIn": "_container_112_GPUSharingConfigIn",
        "GPUSharingConfigOut": "_container_113_GPUSharingConfigOut",
        "SetNetworkPolicyRequestIn": "_container_114_SetNetworkPolicyRequestIn",
        "SetNetworkPolicyRequestOut": "_container_115_SetNetworkPolicyRequestOut",
        "GcfsConfigIn": "_container_116_GcfsConfigIn",
        "GcfsConfigOut": "_container_117_GcfsConfigOut",
        "PlacementPolicyIn": "_container_118_PlacementPolicyIn",
        "PlacementPolicyOut": "_container_119_PlacementPolicyOut",
        "UpdateMasterRequestIn": "_container_120_UpdateMasterRequestIn",
        "UpdateMasterRequestOut": "_container_121_UpdateMasterRequestOut",
        "ReleaseChannelConfigIn": "_container_122_ReleaseChannelConfigIn",
        "ReleaseChannelConfigOut": "_container_123_ReleaseChannelConfigOut",
        "TimeWindowIn": "_container_124_TimeWindowIn",
        "TimeWindowOut": "_container_125_TimeWindowOut",
        "NodePoolLoggingConfigIn": "_container_126_NodePoolLoggingConfigIn",
        "NodePoolLoggingConfigOut": "_container_127_NodePoolLoggingConfigOut",
        "PodCIDROverprovisionConfigIn": "_container_128_PodCIDROverprovisionConfigIn",
        "PodCIDROverprovisionConfigOut": "_container_129_PodCIDROverprovisionConfigOut",
        "JwkIn": "_container_130_JwkIn",
        "JwkOut": "_container_131_JwkOut",
        "AcceleratorConfigIn": "_container_132_AcceleratorConfigIn",
        "AcceleratorConfigOut": "_container_133_AcceleratorConfigOut",
        "ConsumptionMeteringConfigIn": "_container_134_ConsumptionMeteringConfigIn",
        "ConsumptionMeteringConfigOut": "_container_135_ConsumptionMeteringConfigOut",
        "SandboxConfigIn": "_container_136_SandboxConfigIn",
        "SandboxConfigOut": "_container_137_SandboxConfigOut",
        "MonitoringComponentConfigIn": "_container_138_MonitoringComponentConfigIn",
        "MonitoringComponentConfigOut": "_container_139_MonitoringComponentConfigOut",
        "PrivateClusterMasterGlobalAccessConfigIn": "_container_140_PrivateClusterMasterGlobalAccessConfigIn",
        "PrivateClusterMasterGlobalAccessConfigOut": "_container_141_PrivateClusterMasterGlobalAccessConfigOut",
        "UsableSubnetworkIn": "_container_142_UsableSubnetworkIn",
        "UsableSubnetworkOut": "_container_143_UsableSubnetworkOut",
        "EphemeralStorageLocalSsdConfigIn": "_container_144_EphemeralStorageLocalSsdConfigIn",
        "EphemeralStorageLocalSsdConfigOut": "_container_145_EphemeralStorageLocalSsdConfigOut",
        "GetOpenIDConfigResponseIn": "_container_146_GetOpenIDConfigResponseIn",
        "GetOpenIDConfigResponseOut": "_container_147_GetOpenIDConfigResponseOut",
        "LegacyAbacIn": "_container_148_LegacyAbacIn",
        "LegacyAbacOut": "_container_149_LegacyAbacOut",
        "LoggingVariantConfigIn": "_container_150_LoggingVariantConfigIn",
        "LoggingVariantConfigOut": "_container_151_LoggingVariantConfigOut",
        "CloudRunConfigIn": "_container_152_CloudRunConfigIn",
        "CloudRunConfigOut": "_container_153_CloudRunConfigOut",
        "PubSubIn": "_container_154_PubSubIn",
        "PubSubOut": "_container_155_PubSubOut",
        "UpdateNodePoolRequestIn": "_container_156_UpdateNodePoolRequestIn",
        "UpdateNodePoolRequestOut": "_container_157_UpdateNodePoolRequestOut",
        "SetLabelsRequestIn": "_container_158_SetLabelsRequestIn",
        "SetLabelsRequestOut": "_container_159_SetLabelsRequestOut",
        "NotificationConfigIn": "_container_160_NotificationConfigIn",
        "NotificationConfigOut": "_container_161_NotificationConfigOut",
        "MasterAuthIn": "_container_162_MasterAuthIn",
        "MasterAuthOut": "_container_163_MasterAuthOut",
        "SetMasterAuthRequestIn": "_container_164_SetMasterAuthRequestIn",
        "SetMasterAuthRequestOut": "_container_165_SetMasterAuthRequestOut",
        "ClusterAutoscalingIn": "_container_166_ClusterAutoscalingIn",
        "ClusterAutoscalingOut": "_container_167_ClusterAutoscalingOut",
        "FilterIn": "_container_168_FilterIn",
        "FilterOut": "_container_169_FilterOut",
        "MaintenancePolicyIn": "_container_170_MaintenancePolicyIn",
        "MaintenancePolicyOut": "_container_171_MaintenancePolicyOut",
        "SetNodePoolAutoscalingRequestIn": "_container_172_SetNodePoolAutoscalingRequestIn",
        "SetNodePoolAutoscalingRequestOut": "_container_173_SetNodePoolAutoscalingRequestOut",
        "ReleaseChannelIn": "_container_174_ReleaseChannelIn",
        "ReleaseChannelOut": "_container_175_ReleaseChannelOut",
        "SetLegacyAbacRequestIn": "_container_176_SetLegacyAbacRequestIn",
        "SetLegacyAbacRequestOut": "_container_177_SetLegacyAbacRequestOut",
        "KubernetesDashboardIn": "_container_178_KubernetesDashboardIn",
        "KubernetesDashboardOut": "_container_179_KubernetesDashboardOut",
        "CreateClusterRequestIn": "_container_180_CreateClusterRequestIn",
        "CreateClusterRequestOut": "_container_181_CreateClusterRequestOut",
        "BlueGreenInfoIn": "_container_182_BlueGreenInfoIn",
        "BlueGreenInfoOut": "_container_183_BlueGreenInfoOut",
        "NodeManagementIn": "_container_184_NodeManagementIn",
        "NodeManagementOut": "_container_185_NodeManagementOut",
        "ManagedPrometheusConfigIn": "_container_186_ManagedPrometheusConfigIn",
        "ManagedPrometheusConfigOut": "_container_187_ManagedPrometheusConfigOut",
        "SetNodePoolSizeRequestIn": "_container_188_SetNodePoolSizeRequestIn",
        "SetNodePoolSizeRequestOut": "_container_189_SetNodePoolSizeRequestOut",
        "BlueGreenSettingsIn": "_container_190_BlueGreenSettingsIn",
        "BlueGreenSettingsOut": "_container_191_BlueGreenSettingsOut",
        "NodePoolAutoConfigIn": "_container_192_NodePoolAutoConfigIn",
        "NodePoolAutoConfigOut": "_container_193_NodePoolAutoConfigOut",
        "IntraNodeVisibilityConfigIn": "_container_194_IntraNodeVisibilityConfigIn",
        "IntraNodeVisibilityConfigOut": "_container_195_IntraNodeVisibilityConfigOut",
        "WindowsNodeConfigIn": "_container_196_WindowsNodeConfigIn",
        "WindowsNodeConfigOut": "_container_197_WindowsNodeConfigOut",
        "HorizontalPodAutoscalingIn": "_container_198_HorizontalPodAutoscalingIn",
        "HorizontalPodAutoscalingOut": "_container_199_HorizontalPodAutoscalingOut",
        "NodeKubeletConfigIn": "_container_200_NodeKubeletConfigIn",
        "NodeKubeletConfigOut": "_container_201_NodeKubeletConfigOut",
        "EmptyIn": "_container_202_EmptyIn",
        "EmptyOut": "_container_203_EmptyOut",
        "NodePoolIn": "_container_204_NodePoolIn",
        "NodePoolOut": "_container_205_NodePoolOut",
        "UpgradeEventIn": "_container_206_UpgradeEventIn",
        "UpgradeEventOut": "_container_207_UpgradeEventOut",
        "UpgradeAvailableEventIn": "_container_208_UpgradeAvailableEventIn",
        "UpgradeAvailableEventOut": "_container_209_UpgradeAvailableEventOut",
        "ReservationAffinityIn": "_container_210_ReservationAffinityIn",
        "ReservationAffinityOut": "_container_211_ReservationAffinityOut",
        "NetworkConfigIn": "_container_212_NetworkConfigIn",
        "NetworkConfigOut": "_container_213_NetworkConfigOut",
        "IPAllocationPolicyIn": "_container_214_IPAllocationPolicyIn",
        "IPAllocationPolicyOut": "_container_215_IPAllocationPolicyOut",
        "GetJSONWebKeysResponseIn": "_container_216_GetJSONWebKeysResponseIn",
        "GetJSONWebKeysResponseOut": "_container_217_GetJSONWebKeysResponseOut",
        "FastSocketIn": "_container_218_FastSocketIn",
        "FastSocketOut": "_container_219_FastSocketOut",
        "FleetIn": "_container_220_FleetIn",
        "FleetOut": "_container_221_FleetOut",
        "DnsCacheConfigIn": "_container_222_DnsCacheConfigIn",
        "DnsCacheConfigOut": "_container_223_DnsCacheConfigOut",
        "LoggingComponentConfigIn": "_container_224_LoggingComponentConfigIn",
        "LoggingComponentConfigOut": "_container_225_LoggingComponentConfigOut",
        "RecurringTimeWindowIn": "_container_226_RecurringTimeWindowIn",
        "RecurringTimeWindowOut": "_container_227_RecurringTimeWindowOut",
        "UpdateInfoIn": "_container_228_UpdateInfoIn",
        "UpdateInfoOut": "_container_229_UpdateInfoOut",
        "ILBSubsettingConfigIn": "_container_230_ILBSubsettingConfigIn",
        "ILBSubsettingConfigOut": "_container_231_ILBSubsettingConfigOut",
        "LocalNvmeSsdBlockConfigIn": "_container_232_LocalNvmeSsdBlockConfigIn",
        "LocalNvmeSsdBlockConfigOut": "_container_233_LocalNvmeSsdBlockConfigOut",
        "SetNodePoolManagementRequestIn": "_container_234_SetNodePoolManagementRequestIn",
        "SetNodePoolManagementRequestOut": "_container_235_SetNodePoolManagementRequestOut",
        "GatewayAPIConfigIn": "_container_236_GatewayAPIConfigIn",
        "GatewayAPIConfigOut": "_container_237_GatewayAPIConfigOut",
        "NodeConfigDefaultsIn": "_container_238_NodeConfigDefaultsIn",
        "NodeConfigDefaultsOut": "_container_239_NodeConfigDefaultsOut",
        "ConfidentialNodesIn": "_container_240_ConfidentialNodesIn",
        "ConfidentialNodesOut": "_container_241_ConfidentialNodesOut",
        "NetworkPerformanceConfigIn": "_container_242_NetworkPerformanceConfigIn",
        "NetworkPerformanceConfigOut": "_container_243_NetworkPerformanceConfigOut",
        "ListOperationsResponseIn": "_container_244_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_container_245_ListOperationsResponseOut",
        "UpgradeSettingsIn": "_container_246_UpgradeSettingsIn",
        "UpgradeSettingsOut": "_container_247_UpgradeSettingsOut",
        "StatusConditionIn": "_container_248_StatusConditionIn",
        "StatusConditionOut": "_container_249_StatusConditionOut",
        "ConfigConnectorConfigIn": "_container_250_ConfigConnectorConfigIn",
        "ConfigConnectorConfigOut": "_container_251_ConfigConnectorConfigOut",
        "LinuxNodeConfigIn": "_container_252_LinuxNodeConfigIn",
        "LinuxNodeConfigOut": "_container_253_LinuxNodeConfigOut",
        "AutopilotIn": "_container_254_AutopilotIn",
        "AutopilotOut": "_container_255_AutopilotOut",
        "RollbackNodePoolUpgradeRequestIn": "_container_256_RollbackNodePoolUpgradeRequestIn",
        "RollbackNodePoolUpgradeRequestOut": "_container_257_RollbackNodePoolUpgradeRequestOut",
        "NodeTaintIn": "_container_258_NodeTaintIn",
        "NodeTaintOut": "_container_259_NodeTaintOut",
        "DefaultSnatStatusIn": "_container_260_DefaultSnatStatusIn",
        "DefaultSnatStatusOut": "_container_261_DefaultSnatStatusOut",
        "LoggingConfigIn": "_container_262_LoggingConfigIn",
        "LoggingConfigOut": "_container_263_LoggingConfigOut",
        "StatusIn": "_container_264_StatusIn",
        "StatusOut": "_container_265_StatusOut",
        "SetLoggingServiceRequestIn": "_container_266_SetLoggingServiceRequestIn",
        "SetLoggingServiceRequestOut": "_container_267_SetLoggingServiceRequestOut",
        "MetricIn": "_container_268_MetricIn",
        "MetricOut": "_container_269_MetricOut",
        "ClusterUpdateIn": "_container_270_ClusterUpdateIn",
        "ClusterUpdateOut": "_container_271_ClusterUpdateOut",
        "HttpLoadBalancingIn": "_container_272_HttpLoadBalancingIn",
        "HttpLoadBalancingOut": "_container_273_HttpLoadBalancingOut",
        "GcpFilestoreCsiDriverConfigIn": "_container_274_GcpFilestoreCsiDriverConfigIn",
        "GcpFilestoreCsiDriverConfigOut": "_container_275_GcpFilestoreCsiDriverConfigOut",
        "MaintenanceExclusionOptionsIn": "_container_276_MaintenanceExclusionOptionsIn",
        "MaintenanceExclusionOptionsOut": "_container_277_MaintenanceExclusionOptionsOut",
        "NetworkPolicyConfigIn": "_container_278_NetworkPolicyConfigIn",
        "NetworkPolicyConfigOut": "_container_279_NetworkPolicyConfigOut",
        "AddonsConfigIn": "_container_280_AddonsConfigIn",
        "AddonsConfigOut": "_container_281_AddonsConfigOut",
        "MaxPodsConstraintIn": "_container_282_MaxPodsConstraintIn",
        "MaxPodsConstraintOut": "_container_283_MaxPodsConstraintOut",
        "OperationIn": "_container_284_OperationIn",
        "OperationOut": "_container_285_OperationOut",
        "StartIPRotationRequestIn": "_container_286_StartIPRotationRequestIn",
        "StartIPRotationRequestOut": "_container_287_StartIPRotationRequestOut",
        "NetworkTagsIn": "_container_288_NetworkTagsIn",
        "NetworkTagsOut": "_container_289_NetworkTagsOut",
        "MeshCertificatesIn": "_container_290_MeshCertificatesIn",
        "MeshCertificatesOut": "_container_291_MeshCertificatesOut",
        "SetLocationsRequestIn": "_container_292_SetLocationsRequestIn",
        "SetLocationsRequestOut": "_container_293_SetLocationsRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["DatabaseEncryptionIn"] = t.struct(
        {"state": t.string().optional(), "keyName": t.string().optional()}
    ).named(renames["DatabaseEncryptionIn"])
    types["DatabaseEncryptionOut"] = t.struct(
        {
            "state": t.string().optional(),
            "keyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseEncryptionOut"])
    types["ServerConfigIn"] = t.struct(
        {
            "defaultImageType": t.string().optional(),
            "validNodeVersions": t.array(t.string()).optional(),
            "channels": t.array(t.proxy(renames["ReleaseChannelConfigIn"])).optional(),
            "validMasterVersions": t.array(t.string()).optional(),
            "defaultClusterVersion": t.string().optional(),
            "validImageTypes": t.array(t.string()).optional(),
        }
    ).named(renames["ServerConfigIn"])
    types["ServerConfigOut"] = t.struct(
        {
            "defaultImageType": t.string().optional(),
            "validNodeVersions": t.array(t.string()).optional(),
            "channels": t.array(t.proxy(renames["ReleaseChannelConfigOut"])).optional(),
            "validMasterVersions": t.array(t.string()).optional(),
            "defaultClusterVersion": t.string().optional(),
            "validImageTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServerConfigOut"])
    types["GcePersistentDiskCsiDriverConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["GcePersistentDiskCsiDriverConfigIn"])
    types["GcePersistentDiskCsiDriverConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcePersistentDiskCsiDriverConfigOut"])
    types["ResourceLabelsIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["ResourceLabelsIn"])
    types["ResourceLabelsOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceLabelsOut"])
    types["ServiceExternalIPsConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["ServiceExternalIPsConfigIn"])
    types["ServiceExternalIPsConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceExternalIPsConfigOut"])
    types["NodeLabelsIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["NodeLabelsIn"])
    types["NodeLabelsOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeLabelsOut"])
    types["SetAddonsConfigRequestIn"] = t.struct(
        {
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "addonsConfig": t.proxy(renames["AddonsConfigIn"]),
            "projectId": t.string().optional(),
        }
    ).named(renames["SetAddonsConfigRequestIn"])
    types["SetAddonsConfigRequestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "addonsConfig": t.proxy(renames["AddonsConfigOut"]),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetAddonsConfigRequestOut"])
    types["MaintenanceWindowIn"] = t.struct(
        {
            "maintenanceExclusions": t.struct({"_": t.string().optional()}).optional(),
            "recurringWindow": t.proxy(renames["RecurringTimeWindowIn"]).optional(),
            "dailyMaintenanceWindow": t.proxy(
                renames["DailyMaintenanceWindowIn"]
            ).optional(),
        }
    ).named(renames["MaintenanceWindowIn"])
    types["MaintenanceWindowOut"] = t.struct(
        {
            "maintenanceExclusions": t.struct({"_": t.string().optional()}).optional(),
            "recurringWindow": t.proxy(renames["RecurringTimeWindowOut"]).optional(),
            "dailyMaintenanceWindow": t.proxy(
                renames["DailyMaintenanceWindowOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceWindowOut"])
    types["NodeConfigIn"] = t.struct(
        {
            "gvnic": t.proxy(renames["VirtualNICIn"]).optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigIn"]
            ).optional(),
            "localNvmeSsdBlockConfig": t.proxy(
                renames["LocalNvmeSsdBlockConfigIn"]
            ).optional(),
            "machineType": t.string().optional(),
            "localSsdCount": t.integer().optional(),
            "spot": t.boolean().optional(),
            "kubeletConfig": t.proxy(renames["NodeKubeletConfigIn"]).optional(),
            "advancedMachineFeatures": t.proxy(
                renames["AdvancedMachineFeaturesIn"]
            ).optional(),
            "minCpuPlatform": t.string().optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorConfigIn"])).optional(),
            "fastSocket": t.proxy(renames["FastSocketIn"]).optional(),
            "windowsNodeConfig": t.proxy(renames["WindowsNodeConfigIn"]).optional(),
            "bootDiskKmsKey": t.string().optional(),
            "ephemeralStorageLocalSsdConfig": t.proxy(
                renames["EphemeralStorageLocalSsdConfigIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccount": t.string().optional(),
            "taints": t.array(t.proxy(renames["NodeTaintIn"])).optional(),
            "linuxNodeConfig": t.proxy(renames["LinuxNodeConfigIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "confidentialNodes": t.proxy(renames["ConfidentialNodesIn"]).optional(),
            "tags": t.array(t.string()).optional(),
            "nodeGroup": t.string().optional(),
            "gcfsConfig": t.proxy(renames["GcfsConfigIn"]).optional(),
            "resourceLabels": t.struct({"_": t.string().optional()}).optional(),
            "diskSizeGb": t.integer().optional(),
            "loggingConfig": t.proxy(renames["NodePoolLoggingConfigIn"]).optional(),
            "sandboxConfig": t.proxy(renames["SandboxConfigIn"]).optional(),
            "reservationAffinity": t.proxy(renames["ReservationAffinityIn"]).optional(),
            "workloadMetadataConfig": t.proxy(
                renames["WorkloadMetadataConfigIn"]
            ).optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "imageType": t.string().optional(),
            "preemptible": t.boolean().optional(),
            "diskType": t.string().optional(),
        }
    ).named(renames["NodeConfigIn"])
    types["NodeConfigOut"] = t.struct(
        {
            "gvnic": t.proxy(renames["VirtualNICOut"]).optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigOut"]
            ).optional(),
            "localNvmeSsdBlockConfig": t.proxy(
                renames["LocalNvmeSsdBlockConfigOut"]
            ).optional(),
            "machineType": t.string().optional(),
            "localSsdCount": t.integer().optional(),
            "spot": t.boolean().optional(),
            "kubeletConfig": t.proxy(renames["NodeKubeletConfigOut"]).optional(),
            "advancedMachineFeatures": t.proxy(
                renames["AdvancedMachineFeaturesOut"]
            ).optional(),
            "minCpuPlatform": t.string().optional(),
            "accelerators": t.array(
                t.proxy(renames["AcceleratorConfigOut"])
            ).optional(),
            "fastSocket": t.proxy(renames["FastSocketOut"]).optional(),
            "windowsNodeConfig": t.proxy(renames["WindowsNodeConfigOut"]).optional(),
            "bootDiskKmsKey": t.string().optional(),
            "ephemeralStorageLocalSsdConfig": t.proxy(
                renames["EphemeralStorageLocalSsdConfigOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccount": t.string().optional(),
            "taints": t.array(t.proxy(renames["NodeTaintOut"])).optional(),
            "linuxNodeConfig": t.proxy(renames["LinuxNodeConfigOut"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "confidentialNodes": t.proxy(renames["ConfidentialNodesOut"]).optional(),
            "tags": t.array(t.string()).optional(),
            "nodeGroup": t.string().optional(),
            "gcfsConfig": t.proxy(renames["GcfsConfigOut"]).optional(),
            "resourceLabels": t.struct({"_": t.string().optional()}).optional(),
            "diskSizeGb": t.integer().optional(),
            "loggingConfig": t.proxy(renames["NodePoolLoggingConfigOut"]).optional(),
            "sandboxConfig": t.proxy(renames["SandboxConfigOut"]).optional(),
            "reservationAffinity": t.proxy(
                renames["ReservationAffinityOut"]
            ).optional(),
            "workloadMetadataConfig": t.proxy(
                renames["WorkloadMetadataConfigOut"]
            ).optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "imageType": t.string().optional(),
            "preemptible": t.boolean().optional(),
            "diskType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeConfigOut"])
    types["ShieldedNodesIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["ShieldedNodesIn"]
    )
    types["ShieldedNodesOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShieldedNodesOut"])
    types["DNSConfigIn"] = t.struct(
        {
            "clusterDnsScope": t.string().optional(),
            "clusterDnsDomain": t.string().optional(),
            "clusterDns": t.string().optional(),
        }
    ).named(renames["DNSConfigIn"])
    types["DNSConfigOut"] = t.struct(
        {
            "clusterDnsScope": t.string().optional(),
            "clusterDnsDomain": t.string().optional(),
            "clusterDns": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DNSConfigOut"])
    types["HttpCacheControlResponseHeaderIn"] = t.struct(
        {
            "expires": t.string().optional(),
            "age": t.string().optional(),
            "directive": t.string().optional(),
        }
    ).named(renames["HttpCacheControlResponseHeaderIn"])
    types["HttpCacheControlResponseHeaderOut"] = t.struct(
        {
            "expires": t.string().optional(),
            "age": t.string().optional(),
            "directive": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpCacheControlResponseHeaderOut"])
    types["CompleteNodePoolUpgradeRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CompleteNodePoolUpgradeRequestIn"])
    types["CompleteNodePoolUpgradeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CompleteNodePoolUpgradeRequestOut"])
    types["VerticalPodAutoscalingIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["VerticalPodAutoscalingIn"])
    types["VerticalPodAutoscalingOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerticalPodAutoscalingOut"])
    types["AutoprovisioningNodePoolDefaultsIn"] = t.struct(
        {
            "imageType": t.string().optional(),
            "diskType": t.string().optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigIn"]
            ).optional(),
            "serviceAccount": t.string().optional(),
            "diskSizeGb": t.integer().optional(),
            "management": t.proxy(renames["NodeManagementIn"]).optional(),
            "upgradeSettings": t.proxy(renames["UpgradeSettingsIn"]).optional(),
            "bootDiskKmsKey": t.string().optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "minCpuPlatform": t.string().optional(),
        }
    ).named(renames["AutoprovisioningNodePoolDefaultsIn"])
    types["AutoprovisioningNodePoolDefaultsOut"] = t.struct(
        {
            "imageType": t.string().optional(),
            "diskType": t.string().optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigOut"]
            ).optional(),
            "serviceAccount": t.string().optional(),
            "diskSizeGb": t.integer().optional(),
            "management": t.proxy(renames["NodeManagementOut"]).optional(),
            "upgradeSettings": t.proxy(renames["UpgradeSettingsOut"]).optional(),
            "bootDiskKmsKey": t.string().optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "minCpuPlatform": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoprovisioningNodePoolDefaultsOut"])
    types["VirtualNICIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["VirtualNICIn"]
    )
    types["VirtualNICOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualNICOut"])
    types["NodePoolAutoscalingIn"] = t.struct(
        {
            "locationPolicy": t.string().optional(),
            "minNodeCount": t.integer().optional(),
            "totalMaxNodeCount": t.integer().optional(),
            "enabled": t.boolean().optional(),
            "maxNodeCount": t.integer().optional(),
            "autoprovisioned": t.boolean().optional(),
            "totalMinNodeCount": t.integer().optional(),
        }
    ).named(renames["NodePoolAutoscalingIn"])
    types["NodePoolAutoscalingOut"] = t.struct(
        {
            "locationPolicy": t.string().optional(),
            "minNodeCount": t.integer().optional(),
            "totalMaxNodeCount": t.integer().optional(),
            "enabled": t.boolean().optional(),
            "maxNodeCount": t.integer().optional(),
            "autoprovisioned": t.boolean().optional(),
            "totalMinNodeCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodePoolAutoscalingOut"])
    types["CidrBlockIn"] = t.struct(
        {"displayName": t.string().optional(), "cidrBlock": t.string().optional()}
    ).named(renames["CidrBlockIn"])
    types["CidrBlockOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "cidrBlock": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CidrBlockOut"])
    types["SetMaintenancePolicyRequestIn"] = t.struct(
        {
            "zone": t.string(),
            "projectId": t.string(),
            "clusterId": t.string(),
            "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
            "name": t.string().optional(),
        }
    ).named(renames["SetMaintenancePolicyRequestIn"])
    types["SetMaintenancePolicyRequestOut"] = t.struct(
        {
            "zone": t.string(),
            "projectId": t.string(),
            "clusterId": t.string(),
            "maintenancePolicy": t.proxy(renames["MaintenancePolicyOut"]),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetMaintenancePolicyRequestOut"])
    types["BigQueryDestinationIn"] = t.struct(
        {"datasetId": t.string().optional()}
    ).named(renames["BigQueryDestinationIn"])
    types["BigQueryDestinationOut"] = t.struct(
        {
            "datasetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryDestinationOut"])
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
    types["OperationProgressIn"] = t.struct(
        {
            "stages": t.array(t.proxy(renames["OperationProgressIn"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "name": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["OperationProgressIn"])
    types["OperationProgressOut"] = t.struct(
        {
            "stages": t.array(t.proxy(renames["OperationProgressOut"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "name": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationProgressOut"])
    types["AuthenticatorGroupsConfigIn"] = t.struct(
        {"securityGroup": t.string().optional(), "enabled": t.boolean().optional()}
    ).named(renames["AuthenticatorGroupsConfigIn"])
    types["AuthenticatorGroupsConfigOut"] = t.struct(
        {
            "securityGroup": t.string().optional(),
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthenticatorGroupsConfigOut"])
    types["PrivateClusterConfigIn"] = t.struct(
        {
            "privateEndpointSubnetwork": t.string().optional(),
            "enablePrivateNodes": t.boolean().optional(),
            "privateEndpoint": t.string().optional(),
            "masterGlobalAccessConfig": t.proxy(
                renames["PrivateClusterMasterGlobalAccessConfigIn"]
            ).optional(),
            "enablePrivateEndpoint": t.boolean().optional(),
            "masterIpv4CidrBlock": t.string().optional(),
            "publicEndpoint": t.string().optional(),
            "peeringName": t.string().optional(),
        }
    ).named(renames["PrivateClusterConfigIn"])
    types["PrivateClusterConfigOut"] = t.struct(
        {
            "privateEndpointSubnetwork": t.string().optional(),
            "enablePrivateNodes": t.boolean().optional(),
            "privateEndpoint": t.string().optional(),
            "masterGlobalAccessConfig": t.proxy(
                renames["PrivateClusterMasterGlobalAccessConfigOut"]
            ).optional(),
            "enablePrivateEndpoint": t.boolean().optional(),
            "masterIpv4CidrBlock": t.string().optional(),
            "publicEndpoint": t.string().optional(),
            "peeringName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateClusterConfigOut"])
    types["ClusterIn"] = t.struct(
        {
            "ipAllocationPolicy": t.proxy(renames["IPAllocationPolicyIn"]).optional(),
            "defaultMaxPodsConstraint": t.proxy(
                renames["MaxPodsConstraintIn"]
            ).optional(),
            "location": t.string().optional(),
            "tpuIpv4CidrBlock": t.string().optional(),
            "identityServiceConfig": t.proxy(
                renames["IdentityServiceConfigIn"]
            ).optional(),
            "notificationConfig": t.proxy(renames["NotificationConfigIn"]).optional(),
            "initialClusterVersion": t.string().optional(),
            "masterAuthorizedNetworksConfig": t.proxy(
                renames["MasterAuthorizedNetworksConfigIn"]
            ).optional(),
            "clusterIpv4Cidr": t.string().optional(),
            "fleet": t.proxy(renames["FleetIn"]).optional(),
            "status": t.string().optional(),
            "endpoint": t.string().optional(),
            "network": t.string().optional(),
            "resourceUsageExportConfig": t.proxy(
                renames["ResourceUsageExportConfigIn"]
            ).optional(),
            "confidentialNodes": t.proxy(renames["ConfidentialNodesIn"]).optional(),
            "expireTime": t.string().optional(),
            "autoscaling": t.proxy(renames["ClusterAutoscalingIn"]).optional(),
            "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "labelFingerprint": t.string().optional(),
            "legacyAbac": t.proxy(renames["LegacyAbacIn"]).optional(),
            "workloadIdentityConfig": t.proxy(
                renames["WorkloadIdentityConfigIn"]
            ).optional(),
            "nodePools": t.array(t.proxy(renames["NodePoolIn"])).optional(),
            "loggingService": t.string().optional(),
            "resourceLabels": t.struct({"_": t.string().optional()}).optional(),
            "networkPolicy": t.proxy(renames["NetworkPolicyIn"]).optional(),
            "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
            "autopilot": t.proxy(renames["AutopilotIn"]).optional(),
            "description": t.string().optional(),
            "enableKubernetesAlpha": t.boolean().optional(),
            "enableTpu": t.boolean().optional(),
            "name": t.string().optional(),
            "monitoringService": t.string().optional(),
            "verticalPodAutoscaling": t.proxy(
                renames["VerticalPodAutoscalingIn"]
            ).optional(),
            "initialNodeCount": t.integer().optional(),
            "authenticatorGroupsConfig": t.proxy(
                renames["AuthenticatorGroupsConfigIn"]
            ).optional(),
            "privateClusterConfig": t.proxy(
                renames["PrivateClusterConfigIn"]
            ).optional(),
            "meshCertificates": t.proxy(renames["MeshCertificatesIn"]).optional(),
            "etag": t.string().optional(),
            "nodePoolAutoConfig": t.proxy(renames["NodePoolAutoConfigIn"]).optional(),
            "statusMessage": t.string().optional(),
            "masterAuth": t.proxy(renames["MasterAuthIn"]).optional(),
            "createTime": t.string().optional(),
            "currentNodeVersion": t.string().optional(),
            "shieldedNodes": t.proxy(renames["ShieldedNodesIn"]).optional(),
            "monitoringConfig": t.proxy(renames["MonitoringConfigIn"]).optional(),
            "currentNodeCount": t.integer().optional(),
            "currentMasterVersion": t.string().optional(),
            "selfLink": t.string().optional(),
            "conditions": t.array(t.proxy(renames["StatusConditionIn"])).optional(),
            "databaseEncryption": t.proxy(renames["DatabaseEncryptionIn"]).optional(),
            "nodePoolDefaults": t.proxy(renames["NodePoolDefaultsIn"]).optional(),
            "costManagementConfig": t.proxy(
                renames["CostManagementConfigIn"]
            ).optional(),
            "servicesIpv4Cidr": t.string().optional(),
            "binaryAuthorization": t.proxy(renames["BinaryAuthorizationIn"]).optional(),
            "nodeConfig": t.proxy(renames["NodeConfigIn"]).optional(),
            "locations": t.array(t.string()).optional(),
            "zone": t.string().optional(),
            "subnetwork": t.string().optional(),
            "nodeIpv4CidrSize": t.integer().optional(),
            "instanceGroupUrls": t.array(t.string()).optional(),
            "releaseChannel": t.proxy(renames["ReleaseChannelIn"]).optional(),
            "addonsConfig": t.proxy(renames["AddonsConfigIn"]).optional(),
        }
    ).named(renames["ClusterIn"])
    types["ClusterOut"] = t.struct(
        {
            "ipAllocationPolicy": t.proxy(renames["IPAllocationPolicyOut"]).optional(),
            "defaultMaxPodsConstraint": t.proxy(
                renames["MaxPodsConstraintOut"]
            ).optional(),
            "location": t.string().optional(),
            "tpuIpv4CidrBlock": t.string().optional(),
            "id": t.string().optional(),
            "identityServiceConfig": t.proxy(
                renames["IdentityServiceConfigOut"]
            ).optional(),
            "notificationConfig": t.proxy(renames["NotificationConfigOut"]).optional(),
            "initialClusterVersion": t.string().optional(),
            "masterAuthorizedNetworksConfig": t.proxy(
                renames["MasterAuthorizedNetworksConfigOut"]
            ).optional(),
            "clusterIpv4Cidr": t.string().optional(),
            "fleet": t.proxy(renames["FleetOut"]).optional(),
            "status": t.string().optional(),
            "endpoint": t.string().optional(),
            "network": t.string().optional(),
            "resourceUsageExportConfig": t.proxy(
                renames["ResourceUsageExportConfigOut"]
            ).optional(),
            "confidentialNodes": t.proxy(renames["ConfidentialNodesOut"]).optional(),
            "expireTime": t.string().optional(),
            "autoscaling": t.proxy(renames["ClusterAutoscalingOut"]).optional(),
            "maintenancePolicy": t.proxy(renames["MaintenancePolicyOut"]).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "labelFingerprint": t.string().optional(),
            "legacyAbac": t.proxy(renames["LegacyAbacOut"]).optional(),
            "workloadIdentityConfig": t.proxy(
                renames["WorkloadIdentityConfigOut"]
            ).optional(),
            "nodePools": t.array(t.proxy(renames["NodePoolOut"])).optional(),
            "loggingService": t.string().optional(),
            "resourceLabels": t.struct({"_": t.string().optional()}).optional(),
            "networkPolicy": t.proxy(renames["NetworkPolicyOut"]).optional(),
            "networkConfig": t.proxy(renames["NetworkConfigOut"]).optional(),
            "autopilot": t.proxy(renames["AutopilotOut"]).optional(),
            "description": t.string().optional(),
            "enableKubernetesAlpha": t.boolean().optional(),
            "enableTpu": t.boolean().optional(),
            "name": t.string().optional(),
            "monitoringService": t.string().optional(),
            "verticalPodAutoscaling": t.proxy(
                renames["VerticalPodAutoscalingOut"]
            ).optional(),
            "initialNodeCount": t.integer().optional(),
            "authenticatorGroupsConfig": t.proxy(
                renames["AuthenticatorGroupsConfigOut"]
            ).optional(),
            "privateClusterConfig": t.proxy(
                renames["PrivateClusterConfigOut"]
            ).optional(),
            "meshCertificates": t.proxy(renames["MeshCertificatesOut"]).optional(),
            "etag": t.string().optional(),
            "nodePoolAutoConfig": t.proxy(renames["NodePoolAutoConfigOut"]).optional(),
            "statusMessage": t.string().optional(),
            "masterAuth": t.proxy(renames["MasterAuthOut"]).optional(),
            "createTime": t.string().optional(),
            "currentNodeVersion": t.string().optional(),
            "shieldedNodes": t.proxy(renames["ShieldedNodesOut"]).optional(),
            "monitoringConfig": t.proxy(renames["MonitoringConfigOut"]).optional(),
            "currentNodeCount": t.integer().optional(),
            "currentMasterVersion": t.string().optional(),
            "selfLink": t.string().optional(),
            "conditions": t.array(t.proxy(renames["StatusConditionOut"])).optional(),
            "databaseEncryption": t.proxy(renames["DatabaseEncryptionOut"]).optional(),
            "nodePoolDefaults": t.proxy(renames["NodePoolDefaultsOut"]).optional(),
            "costManagementConfig": t.proxy(
                renames["CostManagementConfigOut"]
            ).optional(),
            "servicesIpv4Cidr": t.string().optional(),
            "binaryAuthorization": t.proxy(
                renames["BinaryAuthorizationOut"]
            ).optional(),
            "nodeConfig": t.proxy(renames["NodeConfigOut"]).optional(),
            "locations": t.array(t.string()).optional(),
            "zone": t.string().optional(),
            "subnetwork": t.string().optional(),
            "nodeIpv4CidrSize": t.integer().optional(),
            "instanceGroupUrls": t.array(t.string()).optional(),
            "releaseChannel": t.proxy(renames["ReleaseChannelOut"]).optional(),
            "addonsConfig": t.proxy(renames["AddonsConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterOut"])
    types["CancelOperationRequestIn"] = t.struct(
        {
            "operationId": t.string().optional(),
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["CancelOperationRequestIn"])
    types["CancelOperationRequestOut"] = t.struct(
        {
            "operationId": t.string().optional(),
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CancelOperationRequestOut"])
    types["UsableSubnetworkSecondaryRangeIn"] = t.struct(
        {
            "rangeName": t.string().optional(),
            "status": t.string().optional(),
            "ipCidrRange": t.string().optional(),
        }
    ).named(renames["UsableSubnetworkSecondaryRangeIn"])
    types["UsableSubnetworkSecondaryRangeOut"] = t.struct(
        {
            "rangeName": t.string().optional(),
            "status": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsableSubnetworkSecondaryRangeOut"])
    types["SetMonitoringServiceRequestIn"] = t.struct(
        {
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "projectId": t.string().optional(),
            "monitoringService": t.string(),
            "zone": t.string().optional(),
        }
    ).named(renames["SetMonitoringServiceRequestIn"])
    types["SetMonitoringServiceRequestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "projectId": t.string().optional(),
            "monitoringService": t.string(),
            "zone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetMonitoringServiceRequestOut"])
    types["AdditionalPodRangesConfigIn"] = t.struct(
        {"podRangeNames": t.array(t.string()).optional()}
    ).named(renames["AdditionalPodRangesConfigIn"])
    types["AdditionalPodRangesConfigOut"] = t.struct(
        {
            "podRangeNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdditionalPodRangesConfigOut"])
    types["CostManagementConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["CostManagementConfigIn"])
    types["CostManagementConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CostManagementConfigOut"])
    types["CreateNodePoolRequestIn"] = t.struct(
        {
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
            "parent": t.string().optional(),
            "nodePool": t.proxy(renames["NodePoolIn"]),
            "projectId": t.string().optional(),
        }
    ).named(renames["CreateNodePoolRequestIn"])
    types["CreateNodePoolRequestOut"] = t.struct(
        {
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
            "parent": t.string().optional(),
            "nodePool": t.proxy(renames["NodePoolOut"]),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateNodePoolRequestOut"])
    types["WorkloadMetadataConfigIn"] = t.struct({"mode": t.string().optional()}).named(
        renames["WorkloadMetadataConfigIn"]
    )
    types["WorkloadMetadataConfigOut"] = t.struct(
        {
            "mode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkloadMetadataConfigOut"])
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
    types["DailyMaintenanceWindowIn"] = t.struct(
        {"startTime": t.string().optional(), "duration": t.string().optional()}
    ).named(renames["DailyMaintenanceWindowIn"])
    types["DailyMaintenanceWindowOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "duration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DailyMaintenanceWindowOut"])
    types["SecurityBulletinEventIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "resourceTypeAffected": t.string().optional(),
            "patchedVersions": t.array(t.string()).optional(),
            "bulletinId": t.string().optional(),
            "suggestedUpgradeTarget": t.string().optional(),
            "cveIds": t.array(t.string()).optional(),
            "affectedSupportedMinors": t.array(t.string()).optional(),
            "briefDescription": t.string().optional(),
            "manualStepsRequired": t.boolean().optional(),
            "bulletinUri": t.string().optional(),
        }
    ).named(renames["SecurityBulletinEventIn"])
    types["SecurityBulletinEventOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "resourceTypeAffected": t.string().optional(),
            "patchedVersions": t.array(t.string()).optional(),
            "bulletinId": t.string().optional(),
            "suggestedUpgradeTarget": t.string().optional(),
            "cveIds": t.array(t.string()).optional(),
            "affectedSupportedMinors": t.array(t.string()).optional(),
            "briefDescription": t.string().optional(),
            "manualStepsRequired": t.boolean().optional(),
            "bulletinUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecurityBulletinEventOut"])
    types["BinaryAuthorizationIn"] = t.struct(
        {"evaluationMode": t.string().optional(), "enabled": t.boolean().optional()}
    ).named(renames["BinaryAuthorizationIn"])
    types["BinaryAuthorizationOut"] = t.struct(
        {
            "evaluationMode": t.string().optional(),
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BinaryAuthorizationOut"])
    types["ClientCertificateConfigIn"] = t.struct(
        {"issueClientCertificate": t.boolean().optional()}
    ).named(renames["ClientCertificateConfigIn"])
    types["ClientCertificateConfigOut"] = t.struct(
        {
            "issueClientCertificate": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientCertificateConfigOut"])
    types["MasterAuthorizedNetworksConfigIn"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "cidrBlocks": t.array(t.proxy(renames["CidrBlockIn"])).optional(),
            "gcpPublicCidrsAccessEnabled": t.boolean().optional(),
        }
    ).named(renames["MasterAuthorizedNetworksConfigIn"])
    types["MasterAuthorizedNetworksConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "cidrBlocks": t.array(t.proxy(renames["CidrBlockOut"])).optional(),
            "gcpPublicCidrsAccessEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MasterAuthorizedNetworksConfigOut"])
    types["NodePoolDefaultsIn"] = t.struct(
        {"nodeConfigDefaults": t.proxy(renames["NodeConfigDefaultsIn"]).optional()}
    ).named(renames["NodePoolDefaultsIn"])
    types["NodePoolDefaultsOut"] = t.struct(
        {
            "nodeConfigDefaults": t.proxy(renames["NodeConfigDefaultsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodePoolDefaultsOut"])
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
    types["AdvancedMachineFeaturesIn"] = t.struct(
        {"threadsPerCore": t.string().optional()}
    ).named(renames["AdvancedMachineFeaturesIn"])
    types["AdvancedMachineFeaturesOut"] = t.struct(
        {
            "threadsPerCore": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvancedMachineFeaturesOut"])
    types["IdentityServiceConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["IdentityServiceConfigIn"])
    types["IdentityServiceConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityServiceConfigOut"])
    types["CompleteIPRotationRequestIn"] = t.struct(
        {
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
        }
    ).named(renames["CompleteIPRotationRequestIn"])
    types["CompleteIPRotationRequestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompleteIPRotationRequestOut"])
    types["ListNodePoolsResponseIn"] = t.struct(
        {"nodePools": t.array(t.proxy(renames["NodePoolIn"])).optional()}
    ).named(renames["ListNodePoolsResponseIn"])
    types["ListNodePoolsResponseOut"] = t.struct(
        {
            "nodePools": t.array(t.proxy(renames["NodePoolOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNodePoolsResponseOut"])
    types["ResourceUsageExportConfigIn"] = t.struct(
        {
            "bigqueryDestination": t.proxy(renames["BigQueryDestinationIn"]).optional(),
            "enableNetworkEgressMetering": t.boolean().optional(),
            "consumptionMeteringConfig": t.proxy(
                renames["ConsumptionMeteringConfigIn"]
            ).optional(),
        }
    ).named(renames["ResourceUsageExportConfigIn"])
    types["ResourceUsageExportConfigOut"] = t.struct(
        {
            "bigqueryDestination": t.proxy(
                renames["BigQueryDestinationOut"]
            ).optional(),
            "enableNetworkEgressMetering": t.boolean().optional(),
            "consumptionMeteringConfig": t.proxy(
                renames["ConsumptionMeteringConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceUsageExportConfigOut"])
    types["WorkloadIdentityConfigIn"] = t.struct(
        {"workloadPool": t.string().optional()}
    ).named(renames["WorkloadIdentityConfigIn"])
    types["WorkloadIdentityConfigOut"] = t.struct(
        {
            "workloadPool": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkloadIdentityConfigOut"])
    types["ResourceLimitIn"] = t.struct(
        {
            "maximum": t.string().optional(),
            "minimum": t.string().optional(),
            "resourceType": t.string().optional(),
        }
    ).named(renames["ResourceLimitIn"])
    types["ResourceLimitOut"] = t.struct(
        {
            "maximum": t.string().optional(),
            "minimum": t.string().optional(),
            "resourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceLimitOut"])
    types["GkeBackupAgentConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["GkeBackupAgentConfigIn"])
    types["GkeBackupAgentConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeBackupAgentConfigOut"])
    types["StandardRolloutPolicyIn"] = t.struct(
        {
            "batchNodeCount": t.integer().optional(),
            "batchSoakDuration": t.string().optional(),
            "batchPercentage": t.number().optional(),
        }
    ).named(renames["StandardRolloutPolicyIn"])
    types["StandardRolloutPolicyOut"] = t.struct(
        {
            "batchNodeCount": t.integer().optional(),
            "batchSoakDuration": t.string().optional(),
            "batchPercentage": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StandardRolloutPolicyOut"])
    types["NetworkPolicyIn"] = t.struct(
        {"enabled": t.boolean().optional(), "provider": t.string().optional()}
    ).named(renames["NetworkPolicyIn"])
    types["NetworkPolicyOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "provider": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkPolicyOut"])
    types["NodeNetworkConfigIn"] = t.struct(
        {
            "createPodRange": t.boolean().optional(),
            "networkPerformanceConfig": t.proxy(
                renames["NetworkPerformanceConfigIn"]
            ).optional(),
            "podIpv4CidrBlock": t.string().optional(),
            "podRange": t.string().optional(),
            "enablePrivateNodes": t.boolean().optional(),
            "podCidrOverprovisionConfig": t.proxy(
                renames["PodCIDROverprovisionConfigIn"]
            ).optional(),
        }
    ).named(renames["NodeNetworkConfigIn"])
    types["NodeNetworkConfigOut"] = t.struct(
        {
            "createPodRange": t.boolean().optional(),
            "networkPerformanceConfig": t.proxy(
                renames["NetworkPerformanceConfigOut"]
            ).optional(),
            "podIpv4CidrBlock": t.string().optional(),
            "podRange": t.string().optional(),
            "enablePrivateNodes": t.boolean().optional(),
            "podCidrOverprovisionConfig": t.proxy(
                renames["PodCIDROverprovisionConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeNetworkConfigOut"])
    types["UpdateClusterRequestIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "update": t.proxy(renames["ClusterUpdateIn"]),
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
        }
    ).named(renames["UpdateClusterRequestIn"])
    types["UpdateClusterRequestOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "update": t.proxy(renames["ClusterUpdateOut"]),
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateClusterRequestOut"])
    types["NodeTaintsIn"] = t.struct(
        {"taints": t.array(t.proxy(renames["NodeTaintIn"])).optional()}
    ).named(renames["NodeTaintsIn"])
    types["NodeTaintsOut"] = t.struct(
        {
            "taints": t.array(t.proxy(renames["NodeTaintOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeTaintsOut"])
    types["ListUsableSubnetworksResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "subnetworks": t.array(t.proxy(renames["UsableSubnetworkIn"])).optional(),
        }
    ).named(renames["ListUsableSubnetworksResponseIn"])
    types["ListUsableSubnetworksResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "subnetworks": t.array(t.proxy(renames["UsableSubnetworkOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUsableSubnetworksResponseOut"])
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
    types["SetNetworkPolicyRequestIn"] = t.struct(
        {
            "name": t.string().optional(),
            "networkPolicy": t.proxy(renames["NetworkPolicyIn"]),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["SetNetworkPolicyRequestIn"])
    types["SetNetworkPolicyRequestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "networkPolicy": t.proxy(renames["NetworkPolicyOut"]),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetNetworkPolicyRequestOut"])
    types["GcfsConfigIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["GcfsConfigIn"]
    )
    types["GcfsConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcfsConfigOut"])
    types["PlacementPolicyIn"] = t.struct({"type": t.string().optional()}).named(
        renames["PlacementPolicyIn"]
    )
    types["PlacementPolicyOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacementPolicyOut"])
    types["UpdateMasterRequestIn"] = t.struct(
        {
            "name": t.string().optional(),
            "masterVersion": t.string(),
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
        }
    ).named(renames["UpdateMasterRequestIn"])
    types["UpdateMasterRequestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "masterVersion": t.string(),
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateMasterRequestOut"])
    types["ReleaseChannelConfigIn"] = t.struct(
        {
            "channel": t.string().optional(),
            "defaultVersion": t.string().optional(),
            "validVersions": t.array(t.string()).optional(),
        }
    ).named(renames["ReleaseChannelConfigIn"])
    types["ReleaseChannelConfigOut"] = t.struct(
        {
            "channel": t.string().optional(),
            "defaultVersion": t.string().optional(),
            "validVersions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseChannelConfigOut"])
    types["TimeWindowIn"] = t.struct(
        {
            "maintenanceExclusionOptions": t.proxy(
                renames["MaintenanceExclusionOptionsIn"]
            ).optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["TimeWindowIn"])
    types["TimeWindowOut"] = t.struct(
        {
            "maintenanceExclusionOptions": t.proxy(
                renames["MaintenanceExclusionOptionsOut"]
            ).optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeWindowOut"])
    types["NodePoolLoggingConfigIn"] = t.struct(
        {"variantConfig": t.proxy(renames["LoggingVariantConfigIn"]).optional()}
    ).named(renames["NodePoolLoggingConfigIn"])
    types["NodePoolLoggingConfigOut"] = t.struct(
        {
            "variantConfig": t.proxy(renames["LoggingVariantConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodePoolLoggingConfigOut"])
    types["PodCIDROverprovisionConfigIn"] = t.struct(
        {"disable": t.boolean().optional()}
    ).named(renames["PodCIDROverprovisionConfigIn"])
    types["PodCIDROverprovisionConfigOut"] = t.struct(
        {
            "disable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PodCIDROverprovisionConfigOut"])
    types["JwkIn"] = t.struct(
        {
            "x": t.string().optional(),
            "use": t.string().optional(),
            "kid": t.string().optional(),
            "e": t.string().optional(),
            "n": t.string().optional(),
            "alg": t.string().optional(),
            "crv": t.string().optional(),
            "kty": t.string().optional(),
            "y": t.string().optional(),
        }
    ).named(renames["JwkIn"])
    types["JwkOut"] = t.struct(
        {
            "x": t.string().optional(),
            "use": t.string().optional(),
            "kid": t.string().optional(),
            "e": t.string().optional(),
            "n": t.string().optional(),
            "alg": t.string().optional(),
            "crv": t.string().optional(),
            "kty": t.string().optional(),
            "y": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwkOut"])
    types["AcceleratorConfigIn"] = t.struct(
        {
            "acceleratorType": t.string().optional(),
            "acceleratorCount": t.string().optional(),
            "gpuPartitionSize": t.string().optional(),
            "gpuSharingConfig": t.proxy(renames["GPUSharingConfigIn"]).optional(),
        }
    ).named(renames["AcceleratorConfigIn"])
    types["AcceleratorConfigOut"] = t.struct(
        {
            "acceleratorType": t.string().optional(),
            "acceleratorCount": t.string().optional(),
            "gpuPartitionSize": t.string().optional(),
            "gpuSharingConfig": t.proxy(renames["GPUSharingConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceleratorConfigOut"])
    types["ConsumptionMeteringConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["ConsumptionMeteringConfigIn"])
    types["ConsumptionMeteringConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsumptionMeteringConfigOut"])
    types["SandboxConfigIn"] = t.struct({"type": t.string().optional()}).named(
        renames["SandboxConfigIn"]
    )
    types["SandboxConfigOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SandboxConfigOut"])
    types["MonitoringComponentConfigIn"] = t.struct(
        {"enableComponents": t.array(t.string()).optional()}
    ).named(renames["MonitoringComponentConfigIn"])
    types["MonitoringComponentConfigOut"] = t.struct(
        {
            "enableComponents": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoringComponentConfigOut"])
    types["PrivateClusterMasterGlobalAccessConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["PrivateClusterMasterGlobalAccessConfigIn"])
    types["PrivateClusterMasterGlobalAccessConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateClusterMasterGlobalAccessConfigOut"])
    types["UsableSubnetworkIn"] = t.struct(
        {
            "subnetwork": t.string().optional(),
            "network": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "secondaryIpRanges": t.array(
                t.proxy(renames["UsableSubnetworkSecondaryRangeIn"])
            ).optional(),
            "statusMessage": t.string().optional(),
        }
    ).named(renames["UsableSubnetworkIn"])
    types["UsableSubnetworkOut"] = t.struct(
        {
            "subnetwork": t.string().optional(),
            "network": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "secondaryIpRanges": t.array(
                t.proxy(renames["UsableSubnetworkSecondaryRangeOut"])
            ).optional(),
            "statusMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsableSubnetworkOut"])
    types["EphemeralStorageLocalSsdConfigIn"] = t.struct(
        {"localSsdCount": t.integer().optional()}
    ).named(renames["EphemeralStorageLocalSsdConfigIn"])
    types["EphemeralStorageLocalSsdConfigOut"] = t.struct(
        {
            "localSsdCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EphemeralStorageLocalSsdConfigOut"])
    types["GetOpenIDConfigResponseIn"] = t.struct(
        {
            "response_types_supported": t.array(t.string()).optional(),
            "id_token_signing_alg_values_supported": t.array(t.string()).optional(),
            "grant_types": t.array(t.string()).optional(),
            "jwks_uri": t.string().optional(),
            "subject_types_supported": t.array(t.string()).optional(),
            "cacheHeader": t.proxy(
                renames["HttpCacheControlResponseHeaderIn"]
            ).optional(),
            "issuer": t.string().optional(),
            "claims_supported": t.array(t.string()).optional(),
        }
    ).named(renames["GetOpenIDConfigResponseIn"])
    types["GetOpenIDConfigResponseOut"] = t.struct(
        {
            "response_types_supported": t.array(t.string()).optional(),
            "id_token_signing_alg_values_supported": t.array(t.string()).optional(),
            "grant_types": t.array(t.string()).optional(),
            "jwks_uri": t.string().optional(),
            "subject_types_supported": t.array(t.string()).optional(),
            "cacheHeader": t.proxy(
                renames["HttpCacheControlResponseHeaderOut"]
            ).optional(),
            "issuer": t.string().optional(),
            "claims_supported": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetOpenIDConfigResponseOut"])
    types["LegacyAbacIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["LegacyAbacIn"]
    )
    types["LegacyAbacOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LegacyAbacOut"])
    types["LoggingVariantConfigIn"] = t.struct(
        {"variant": t.string().optional()}
    ).named(renames["LoggingVariantConfigIn"])
    types["LoggingVariantConfigOut"] = t.struct(
        {
            "variant": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoggingVariantConfigOut"])
    types["CloudRunConfigIn"] = t.struct(
        {"disabled": t.boolean().optional(), "loadBalancerType": t.string().optional()}
    ).named(renames["CloudRunConfigIn"])
    types["CloudRunConfigOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "loadBalancerType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRunConfigOut"])
    types["PubSubIn"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "topic": t.string().optional(),
            "filter": t.proxy(renames["FilterIn"]).optional(),
        }
    ).named(renames["PubSubIn"])
    types["PubSubOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "topic": t.string().optional(),
            "filter": t.proxy(renames["FilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubSubOut"])
    types["UpdateNodePoolRequestIn"] = t.struct(
        {
            "upgradeSettings": t.proxy(renames["UpgradeSettingsIn"]).optional(),
            "resourceLabels": t.proxy(renames["ResourceLabelsIn"]).optional(),
            "confidentialNodes": t.proxy(renames["ConfidentialNodesIn"]).optional(),
            "linuxNodeConfig": t.proxy(renames["LinuxNodeConfigIn"]).optional(),
            "nodeVersion": t.string(),
            "imageType": t.string(),
            "kubeletConfig": t.proxy(renames["NodeKubeletConfigIn"]).optional(),
            "loggingConfig": t.proxy(renames["NodePoolLoggingConfigIn"]).optional(),
            "labels": t.proxy(renames["NodeLabelsIn"]).optional(),
            "gcfsConfig": t.proxy(renames["GcfsConfigIn"]).optional(),
            "name": t.string().optional(),
            "workloadMetadataConfig": t.proxy(
                renames["WorkloadMetadataConfigIn"]
            ).optional(),
            "zone": t.string().optional(),
            "tags": t.proxy(renames["NetworkTagsIn"]).optional(),
            "fastSocket": t.proxy(renames["FastSocketIn"]).optional(),
            "nodePoolId": t.string().optional(),
            "windowsNodeConfig": t.proxy(renames["WindowsNodeConfigIn"]).optional(),
            "nodeNetworkConfig": t.proxy(renames["NodeNetworkConfigIn"]).optional(),
            "taints": t.proxy(renames["NodeTaintsIn"]).optional(),
            "locations": t.array(t.string()).optional(),
            "clusterId": t.string().optional(),
            "projectId": t.string().optional(),
            "gvnic": t.proxy(renames["VirtualNICIn"]).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["UpdateNodePoolRequestIn"])
    types["UpdateNodePoolRequestOut"] = t.struct(
        {
            "upgradeSettings": t.proxy(renames["UpgradeSettingsOut"]).optional(),
            "resourceLabels": t.proxy(renames["ResourceLabelsOut"]).optional(),
            "confidentialNodes": t.proxy(renames["ConfidentialNodesOut"]).optional(),
            "linuxNodeConfig": t.proxy(renames["LinuxNodeConfigOut"]).optional(),
            "nodeVersion": t.string(),
            "imageType": t.string(),
            "kubeletConfig": t.proxy(renames["NodeKubeletConfigOut"]).optional(),
            "loggingConfig": t.proxy(renames["NodePoolLoggingConfigOut"]).optional(),
            "labels": t.proxy(renames["NodeLabelsOut"]).optional(),
            "gcfsConfig": t.proxy(renames["GcfsConfigOut"]).optional(),
            "name": t.string().optional(),
            "workloadMetadataConfig": t.proxy(
                renames["WorkloadMetadataConfigOut"]
            ).optional(),
            "zone": t.string().optional(),
            "tags": t.proxy(renames["NetworkTagsOut"]).optional(),
            "fastSocket": t.proxy(renames["FastSocketOut"]).optional(),
            "nodePoolId": t.string().optional(),
            "windowsNodeConfig": t.proxy(renames["WindowsNodeConfigOut"]).optional(),
            "nodeNetworkConfig": t.proxy(renames["NodeNetworkConfigOut"]).optional(),
            "taints": t.proxy(renames["NodeTaintsOut"]).optional(),
            "locations": t.array(t.string()).optional(),
            "clusterId": t.string().optional(),
            "projectId": t.string().optional(),
            "gvnic": t.proxy(renames["VirtualNICOut"]).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateNodePoolRequestOut"])
    types["SetLabelsRequestIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "resourceLabels": t.struct({"_": t.string().optional()}),
            "labelFingerprint": t.string(),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SetLabelsRequestIn"])
    types["SetLabelsRequestOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "resourceLabels": t.struct({"_": t.string().optional()}),
            "labelFingerprint": t.string(),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetLabelsRequestOut"])
    types["NotificationConfigIn"] = t.struct(
        {"pubsub": t.proxy(renames["PubSubIn"]).optional()}
    ).named(renames["NotificationConfigIn"])
    types["NotificationConfigOut"] = t.struct(
        {
            "pubsub": t.proxy(renames["PubSubOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationConfigOut"])
    types["MasterAuthIn"] = t.struct(
        {
            "clientCertificate": t.string().optional(),
            "clientKey": t.string().optional(),
            "clientCertificateConfig": t.proxy(
                renames["ClientCertificateConfigIn"]
            ).optional(),
            "username": t.string().optional(),
            "clusterCaCertificate": t.string().optional(),
            "password": t.string().optional(),
        }
    ).named(renames["MasterAuthIn"])
    types["MasterAuthOut"] = t.struct(
        {
            "clientCertificate": t.string().optional(),
            "clientKey": t.string().optional(),
            "clientCertificateConfig": t.proxy(
                renames["ClientCertificateConfigOut"]
            ).optional(),
            "username": t.string().optional(),
            "clusterCaCertificate": t.string().optional(),
            "password": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MasterAuthOut"])
    types["SetMasterAuthRequestIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "action": t.string(),
            "name": t.string().optional(),
            "update": t.proxy(renames["MasterAuthIn"]),
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
        }
    ).named(renames["SetMasterAuthRequestIn"])
    types["SetMasterAuthRequestOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "action": t.string(),
            "name": t.string().optional(),
            "update": t.proxy(renames["MasterAuthOut"]),
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetMasterAuthRequestOut"])
    types["ClusterAutoscalingIn"] = t.struct(
        {
            "resourceLimits": t.array(t.proxy(renames["ResourceLimitIn"])).optional(),
            "enableNodeAutoprovisioning": t.boolean().optional(),
            "autoprovisioningNodePoolDefaults": t.proxy(
                renames["AutoprovisioningNodePoolDefaultsIn"]
            ).optional(),
            "autoprovisioningLocations": t.array(t.string()).optional(),
            "autoscalingProfile": t.string().optional(),
        }
    ).named(renames["ClusterAutoscalingIn"])
    types["ClusterAutoscalingOut"] = t.struct(
        {
            "resourceLimits": t.array(t.proxy(renames["ResourceLimitOut"])).optional(),
            "enableNodeAutoprovisioning": t.boolean().optional(),
            "autoprovisioningNodePoolDefaults": t.proxy(
                renames["AutoprovisioningNodePoolDefaultsOut"]
            ).optional(),
            "autoprovisioningLocations": t.array(t.string()).optional(),
            "autoscalingProfile": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterAutoscalingOut"])
    types["FilterIn"] = t.struct({"eventType": t.array(t.string()).optional()}).named(
        renames["FilterIn"]
    )
    types["FilterOut"] = t.struct(
        {
            "eventType": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterOut"])
    types["MaintenancePolicyIn"] = t.struct(
        {
            "resourceVersion": t.string().optional(),
            "window": t.proxy(renames["MaintenanceWindowIn"]).optional(),
        }
    ).named(renames["MaintenancePolicyIn"])
    types["MaintenancePolicyOut"] = t.struct(
        {
            "resourceVersion": t.string().optional(),
            "window": t.proxy(renames["MaintenanceWindowOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenancePolicyOut"])
    types["SetNodePoolAutoscalingRequestIn"] = t.struct(
        {
            "clusterId": t.string().optional(),
            "autoscaling": t.proxy(renames["NodePoolAutoscalingIn"]),
            "zone": t.string().optional(),
            "nodePoolId": t.string().optional(),
            "projectId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SetNodePoolAutoscalingRequestIn"])
    types["SetNodePoolAutoscalingRequestOut"] = t.struct(
        {
            "clusterId": t.string().optional(),
            "autoscaling": t.proxy(renames["NodePoolAutoscalingOut"]),
            "zone": t.string().optional(),
            "nodePoolId": t.string().optional(),
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetNodePoolAutoscalingRequestOut"])
    types["ReleaseChannelIn"] = t.struct({"channel": t.string().optional()}).named(
        renames["ReleaseChannelIn"]
    )
    types["ReleaseChannelOut"] = t.struct(
        {
            "channel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseChannelOut"])
    types["SetLegacyAbacRequestIn"] = t.struct(
        {
            "zone": t.string().optional(),
            "enabled": t.boolean(),
            "clusterId": t.string().optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["SetLegacyAbacRequestIn"])
    types["SetLegacyAbacRequestOut"] = t.struct(
        {
            "zone": t.string().optional(),
            "enabled": t.boolean(),
            "clusterId": t.string().optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetLegacyAbacRequestOut"])
    types["KubernetesDashboardIn"] = t.struct(
        {"disabled": t.boolean().optional()}
    ).named(renames["KubernetesDashboardIn"])
    types["KubernetesDashboardOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KubernetesDashboardOut"])
    types["CreateClusterRequestIn"] = t.struct(
        {
            "cluster": t.proxy(renames["ClusterIn"]),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "parent": t.string().optional(),
        }
    ).named(renames["CreateClusterRequestIn"])
    types["CreateClusterRequestOut"] = t.struct(
        {
            "cluster": t.proxy(renames["ClusterOut"]),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateClusterRequestOut"])
    types["BlueGreenInfoIn"] = t.struct(
        {
            "greenPoolVersion": t.string().optional(),
            "bluePoolDeletionStartTime": t.string().optional(),
            "greenInstanceGroupUrls": t.array(t.string()).optional(),
            "blueInstanceGroupUrls": t.array(t.string()).optional(),
            "phase": t.string().optional(),
        }
    ).named(renames["BlueGreenInfoIn"])
    types["BlueGreenInfoOut"] = t.struct(
        {
            "greenPoolVersion": t.string().optional(),
            "bluePoolDeletionStartTime": t.string().optional(),
            "greenInstanceGroupUrls": t.array(t.string()).optional(),
            "blueInstanceGroupUrls": t.array(t.string()).optional(),
            "phase": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BlueGreenInfoOut"])
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
    types["ManagedPrometheusConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["ManagedPrometheusConfigIn"])
    types["ManagedPrometheusConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedPrometheusConfigOut"])
    types["SetNodePoolSizeRequestIn"] = t.struct(
        {
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "nodeCount": t.integer(),
            "nodePoolId": t.string().optional(),
        }
    ).named(renames["SetNodePoolSizeRequestIn"])
    types["SetNodePoolSizeRequestOut"] = t.struct(
        {
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "nodeCount": t.integer(),
            "nodePoolId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetNodePoolSizeRequestOut"])
    types["BlueGreenSettingsIn"] = t.struct(
        {
            "standardRolloutPolicy": t.proxy(
                renames["StandardRolloutPolicyIn"]
            ).optional(),
            "nodePoolSoakDuration": t.string().optional(),
        }
    ).named(renames["BlueGreenSettingsIn"])
    types["BlueGreenSettingsOut"] = t.struct(
        {
            "standardRolloutPolicy": t.proxy(
                renames["StandardRolloutPolicyOut"]
            ).optional(),
            "nodePoolSoakDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BlueGreenSettingsOut"])
    types["NodePoolAutoConfigIn"] = t.struct(
        {"networkTags": t.proxy(renames["NetworkTagsIn"]).optional()}
    ).named(renames["NodePoolAutoConfigIn"])
    types["NodePoolAutoConfigOut"] = t.struct(
        {
            "networkTags": t.proxy(renames["NetworkTagsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodePoolAutoConfigOut"])
    types["IntraNodeVisibilityConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["IntraNodeVisibilityConfigIn"])
    types["IntraNodeVisibilityConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntraNodeVisibilityConfigOut"])
    types["WindowsNodeConfigIn"] = t.struct({"osVersion": t.string().optional()}).named(
        renames["WindowsNodeConfigIn"]
    )
    types["WindowsNodeConfigOut"] = t.struct(
        {
            "osVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsNodeConfigOut"])
    types["HorizontalPodAutoscalingIn"] = t.struct(
        {"disabled": t.boolean().optional()}
    ).named(renames["HorizontalPodAutoscalingIn"])
    types["HorizontalPodAutoscalingOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HorizontalPodAutoscalingOut"])
    types["NodeKubeletConfigIn"] = t.struct(
        {
            "cpuCfsQuotaPeriod": t.string().optional(),
            "cpuManagerPolicy": t.string().optional(),
            "cpuCfsQuota": t.boolean().optional(),
            "podPidsLimit": t.string().optional(),
        }
    ).named(renames["NodeKubeletConfigIn"])
    types["NodeKubeletConfigOut"] = t.struct(
        {
            "cpuCfsQuotaPeriod": t.string().optional(),
            "cpuManagerPolicy": t.string().optional(),
            "cpuCfsQuota": t.boolean().optional(),
            "podPidsLimit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeKubeletConfigOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["NodePoolIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "initialNodeCount": t.integer().optional(),
            "upgradeSettings": t.proxy(renames["UpgradeSettingsIn"]).optional(),
            "maxPodsConstraint": t.proxy(renames["MaxPodsConstraintIn"]).optional(),
            "podIpv4CidrSize": t.integer().optional(),
            "version": t.string().optional(),
            "placementPolicy": t.proxy(renames["PlacementPolicyIn"]).optional(),
            "statusMessage": t.string().optional(),
            "selfLink": t.string().optional(),
            "locations": t.array(t.string()).optional(),
            "conditions": t.array(t.proxy(renames["StatusConditionIn"])).optional(),
            "status": t.string().optional(),
            "management": t.proxy(renames["NodeManagementIn"]).optional(),
            "networkConfig": t.proxy(renames["NodeNetworkConfigIn"]).optional(),
            "instanceGroupUrls": t.array(t.string()).optional(),
            "autoscaling": t.proxy(renames["NodePoolAutoscalingIn"]).optional(),
            "config": t.proxy(renames["NodeConfigIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["NodePoolIn"])
    types["NodePoolOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "initialNodeCount": t.integer().optional(),
            "upgradeSettings": t.proxy(renames["UpgradeSettingsOut"]).optional(),
            "maxPodsConstraint": t.proxy(renames["MaxPodsConstraintOut"]).optional(),
            "updateInfo": t.proxy(renames["UpdateInfoOut"]).optional(),
            "podIpv4CidrSize": t.integer().optional(),
            "version": t.string().optional(),
            "placementPolicy": t.proxy(renames["PlacementPolicyOut"]).optional(),
            "statusMessage": t.string().optional(),
            "selfLink": t.string().optional(),
            "locations": t.array(t.string()).optional(),
            "conditions": t.array(t.proxy(renames["StatusConditionOut"])).optional(),
            "status": t.string().optional(),
            "management": t.proxy(renames["NodeManagementOut"]).optional(),
            "networkConfig": t.proxy(renames["NodeNetworkConfigOut"]).optional(),
            "instanceGroupUrls": t.array(t.string()).optional(),
            "autoscaling": t.proxy(renames["NodePoolAutoscalingOut"]).optional(),
            "config": t.proxy(renames["NodeConfigOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodePoolOut"])
    types["UpgradeEventIn"] = t.struct(
        {
            "currentVersion": t.string().optional(),
            "operation": t.string().optional(),
            "targetVersion": t.string().optional(),
            "resourceType": t.string().optional(),
            "operationStartTime": t.string().optional(),
            "resource": t.string().optional(),
        }
    ).named(renames["UpgradeEventIn"])
    types["UpgradeEventOut"] = t.struct(
        {
            "currentVersion": t.string().optional(),
            "operation": t.string().optional(),
            "targetVersion": t.string().optional(),
            "resourceType": t.string().optional(),
            "operationStartTime": t.string().optional(),
            "resource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeEventOut"])
    types["UpgradeAvailableEventIn"] = t.struct(
        {
            "resource": t.string().optional(),
            "resourceType": t.string().optional(),
            "version": t.string().optional(),
            "releaseChannel": t.proxy(renames["ReleaseChannelIn"]).optional(),
        }
    ).named(renames["UpgradeAvailableEventIn"])
    types["UpgradeAvailableEventOut"] = t.struct(
        {
            "resource": t.string().optional(),
            "resourceType": t.string().optional(),
            "version": t.string().optional(),
            "releaseChannel": t.proxy(renames["ReleaseChannelOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeAvailableEventOut"])
    types["ReservationAffinityIn"] = t.struct(
        {
            "consumeReservationType": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "key": t.string().optional(),
        }
    ).named(renames["ReservationAffinityIn"])
    types["ReservationAffinityOut"] = t.struct(
        {
            "consumeReservationType": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReservationAffinityOut"])
    types["NetworkConfigIn"] = t.struct(
        {
            "enableL4ilbSubsetting": t.boolean().optional(),
            "enableIntraNodeVisibility": t.boolean().optional(),
            "datapathProvider": t.string().optional(),
            "defaultSnatStatus": t.proxy(renames["DefaultSnatStatusIn"]).optional(),
            "serviceExternalIpsConfig": t.proxy(
                renames["ServiceExternalIPsConfigIn"]
            ).optional(),
            "subnetwork": t.string().optional(),
            "dnsConfig": t.proxy(renames["DNSConfigIn"]).optional(),
            "network": t.string().optional(),
            "privateIpv6GoogleAccess": t.string().optional(),
            "gatewayApiConfig": t.proxy(renames["GatewayAPIConfigIn"]).optional(),
        }
    ).named(renames["NetworkConfigIn"])
    types["NetworkConfigOut"] = t.struct(
        {
            "enableL4ilbSubsetting": t.boolean().optional(),
            "enableIntraNodeVisibility": t.boolean().optional(),
            "datapathProvider": t.string().optional(),
            "defaultSnatStatus": t.proxy(renames["DefaultSnatStatusOut"]).optional(),
            "serviceExternalIpsConfig": t.proxy(
                renames["ServiceExternalIPsConfigOut"]
            ).optional(),
            "subnetwork": t.string().optional(),
            "dnsConfig": t.proxy(renames["DNSConfigOut"]).optional(),
            "network": t.string().optional(),
            "privateIpv6GoogleAccess": t.string().optional(),
            "gatewayApiConfig": t.proxy(renames["GatewayAPIConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConfigOut"])
    types["IPAllocationPolicyIn"] = t.struct(
        {
            "nodeIpv4CidrBlock": t.string().optional(),
            "servicesSecondaryRangeName": t.string().optional(),
            "ipv6AccessType": t.string().optional(),
            "stackType": t.string().optional(),
            "podCidrOverprovisionConfig": t.proxy(
                renames["PodCIDROverprovisionConfigIn"]
            ).optional(),
            "servicesIpv4CidrBlock": t.string().optional(),
            "nodeIpv4Cidr": t.string().optional(),
            "useIpAliases": t.boolean().optional(),
            "clusterIpv4CidrBlock": t.string().optional(),
            "clusterSecondaryRangeName": t.string().optional(),
            "useRoutes": t.boolean().optional(),
            "tpuIpv4CidrBlock": t.string().optional(),
            "clusterIpv4Cidr": t.string().optional(),
            "createSubnetwork": t.boolean().optional(),
            "subnetworkName": t.string().optional(),
            "servicesIpv4Cidr": t.string().optional(),
        }
    ).named(renames["IPAllocationPolicyIn"])
    types["IPAllocationPolicyOut"] = t.struct(
        {
            "nodeIpv4CidrBlock": t.string().optional(),
            "additionalPodRangesConfig": t.proxy(
                renames["AdditionalPodRangesConfigOut"]
            ).optional(),
            "servicesSecondaryRangeName": t.string().optional(),
            "ipv6AccessType": t.string().optional(),
            "stackType": t.string().optional(),
            "podCidrOverprovisionConfig": t.proxy(
                renames["PodCIDROverprovisionConfigOut"]
            ).optional(),
            "servicesIpv4CidrBlock": t.string().optional(),
            "nodeIpv4Cidr": t.string().optional(),
            "useIpAliases": t.boolean().optional(),
            "clusterIpv4CidrBlock": t.string().optional(),
            "subnetIpv6CidrBlock": t.string().optional(),
            "servicesIpv6CidrBlock": t.string().optional(),
            "clusterSecondaryRangeName": t.string().optional(),
            "useRoutes": t.boolean().optional(),
            "tpuIpv4CidrBlock": t.string().optional(),
            "clusterIpv4Cidr": t.string().optional(),
            "createSubnetwork": t.boolean().optional(),
            "subnetworkName": t.string().optional(),
            "servicesIpv4Cidr": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IPAllocationPolicyOut"])
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
    types["FastSocketIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["FastSocketIn"]
    )
    types["FastSocketOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FastSocketOut"])
    types["FleetIn"] = t.struct(
        {
            "membership": t.string().optional(),
            "preRegistered": t.boolean().optional(),
            "project": t.string().optional(),
        }
    ).named(renames["FleetIn"])
    types["FleetOut"] = t.struct(
        {
            "membership": t.string().optional(),
            "preRegistered": t.boolean().optional(),
            "project": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FleetOut"])
    types["DnsCacheConfigIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["DnsCacheConfigIn"]
    )
    types["DnsCacheConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsCacheConfigOut"])
    types["LoggingComponentConfigIn"] = t.struct(
        {"enableComponents": t.array(t.string()).optional()}
    ).named(renames["LoggingComponentConfigIn"])
    types["LoggingComponentConfigOut"] = t.struct(
        {
            "enableComponents": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoggingComponentConfigOut"])
    types["RecurringTimeWindowIn"] = t.struct(
        {
            "window": t.proxy(renames["TimeWindowIn"]).optional(),
            "recurrence": t.string().optional(),
        }
    ).named(renames["RecurringTimeWindowIn"])
    types["RecurringTimeWindowOut"] = t.struct(
        {
            "window": t.proxy(renames["TimeWindowOut"]).optional(),
            "recurrence": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecurringTimeWindowOut"])
    types["UpdateInfoIn"] = t.struct(
        {"blueGreenInfo": t.proxy(renames["BlueGreenInfoIn"]).optional()}
    ).named(renames["UpdateInfoIn"])
    types["UpdateInfoOut"] = t.struct(
        {
            "blueGreenInfo": t.proxy(renames["BlueGreenInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateInfoOut"])
    types["ILBSubsettingConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["ILBSubsettingConfigIn"])
    types["ILBSubsettingConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ILBSubsettingConfigOut"])
    types["LocalNvmeSsdBlockConfigIn"] = t.struct(
        {"localSsdCount": t.integer().optional()}
    ).named(renames["LocalNvmeSsdBlockConfigIn"])
    types["LocalNvmeSsdBlockConfigOut"] = t.struct(
        {
            "localSsdCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalNvmeSsdBlockConfigOut"])
    types["SetNodePoolManagementRequestIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "management": t.proxy(renames["NodeManagementIn"]),
            "zone": t.string().optional(),
            "nodePoolId": t.string().optional(),
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
        }
    ).named(renames["SetNodePoolManagementRequestIn"])
    types["SetNodePoolManagementRequestOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "management": t.proxy(renames["NodeManagementOut"]),
            "zone": t.string().optional(),
            "nodePoolId": t.string().optional(),
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetNodePoolManagementRequestOut"])
    types["GatewayAPIConfigIn"] = t.struct({"channel": t.string().optional()}).named(
        renames["GatewayAPIConfigIn"]
    )
    types["GatewayAPIConfigOut"] = t.struct(
        {
            "channel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GatewayAPIConfigOut"])
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
    types["ConfidentialNodesIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["ConfidentialNodesIn"]
    )
    types["ConfidentialNodesOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfidentialNodesOut"])
    types["NetworkPerformanceConfigIn"] = t.struct(
        {"totalEgressBandwidthTier": t.string().optional()}
    ).named(renames["NetworkPerformanceConfigIn"])
    types["NetworkPerformanceConfigOut"] = t.struct(
        {
            "totalEgressBandwidthTier": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkPerformanceConfigOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
            "missingZones": t.array(t.string()).optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "missingZones": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["UpgradeSettingsIn"] = t.struct(
        {
            "blueGreenSettings": t.proxy(renames["BlueGreenSettingsIn"]).optional(),
            "maxUnavailable": t.integer().optional(),
            "maxSurge": t.integer().optional(),
            "strategy": t.string().optional(),
        }
    ).named(renames["UpgradeSettingsIn"])
    types["UpgradeSettingsOut"] = t.struct(
        {
            "blueGreenSettings": t.proxy(renames["BlueGreenSettingsOut"]).optional(),
            "maxUnavailable": t.integer().optional(),
            "maxSurge": t.integer().optional(),
            "strategy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeSettingsOut"])
    types["StatusConditionIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.string().optional(),
            "canonicalCode": t.string().optional(),
        }
    ).named(renames["StatusConditionIn"])
    types["StatusConditionOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.string().optional(),
            "canonicalCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusConditionOut"])
    types["ConfigConnectorConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["ConfigConnectorConfigIn"])
    types["ConfigConnectorConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigConnectorConfigOut"])
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
    types["AutopilotIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["AutopilotIn"]
    )
    types["AutopilotOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutopilotOut"])
    types["RollbackNodePoolUpgradeRequestIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "respectPdb": t.boolean().optional(),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "nodePoolId": t.string().optional(),
        }
    ).named(renames["RollbackNodePoolUpgradeRequestIn"])
    types["RollbackNodePoolUpgradeRequestOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "respectPdb": t.boolean().optional(),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "nodePoolId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RollbackNodePoolUpgradeRequestOut"])
    types["NodeTaintIn"] = t.struct(
        {
            "key": t.string().optional(),
            "effect": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["NodeTaintIn"])
    types["NodeTaintOut"] = t.struct(
        {
            "key": t.string().optional(),
            "effect": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeTaintOut"])
    types["DefaultSnatStatusIn"] = t.struct({"disabled": t.boolean().optional()}).named(
        renames["DefaultSnatStatusIn"]
    )
    types["DefaultSnatStatusOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DefaultSnatStatusOut"])
    types["LoggingConfigIn"] = t.struct(
        {"componentConfig": t.proxy(renames["LoggingComponentConfigIn"]).optional()}
    ).named(renames["LoggingConfigIn"])
    types["LoggingConfigOut"] = t.struct(
        {
            "componentConfig": t.proxy(renames["LoggingComponentConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoggingConfigOut"])
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
    types["SetLoggingServiceRequestIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "loggingService": t.string(),
        }
    ).named(renames["SetLoggingServiceRequestIn"])
    types["SetLoggingServiceRequestOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "loggingService": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetLoggingServiceRequestOut"])
    types["MetricIn"] = t.struct(
        {
            "doubleValue": t.number().optional(),
            "stringValue": t.string().optional(),
            "name": t.string(),
            "intValue": t.string().optional(),
        }
    ).named(renames["MetricIn"])
    types["MetricOut"] = t.struct(
        {
            "doubleValue": t.number().optional(),
            "stringValue": t.string().optional(),
            "name": t.string(),
            "intValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricOut"])
    types["ClusterUpdateIn"] = t.struct(
        {
            "desiredMonitoringConfig": t.proxy(
                renames["MonitoringConfigIn"]
            ).optional(),
            "desiredGcfsConfig": t.proxy(renames["GcfsConfigIn"]).optional(),
            "desiredMasterVersion": t.string().optional(),
            "desiredDatapathProvider": t.string().optional(),
            "desiredIdentityServiceConfig": t.proxy(
                renames["IdentityServiceConfigIn"]
            ).optional(),
            "desiredWorkloadIdentityConfig": t.proxy(
                renames["WorkloadIdentityConfigIn"]
            ).optional(),
            "desiredFleet": t.proxy(renames["FleetIn"]).optional(),
            "desiredVerticalPodAutoscaling": t.proxy(
                renames["VerticalPodAutoscalingIn"]
            ).optional(),
            "desiredDnsConfig": t.proxy(renames["DNSConfigIn"]).optional(),
            "etag": t.string().optional(),
            "desiredMonitoringService": t.string().optional(),
            "desiredAuthenticatorGroupsConfig": t.proxy(
                renames["AuthenticatorGroupsConfigIn"]
            ).optional(),
            "desiredMasterAuthorizedNetworksConfig": t.proxy(
                renames["MasterAuthorizedNetworksConfigIn"]
            ).optional(),
            "desiredNodePoolAutoscaling": t.proxy(
                renames["NodePoolAutoscalingIn"]
            ).optional(),
            "desiredDatabaseEncryption": t.proxy(
                renames["DatabaseEncryptionIn"]
            ).optional(),
            "desiredClusterAutoscaling": t.proxy(
                renames["ClusterAutoscalingIn"]
            ).optional(),
            "desiredPrivateIpv6GoogleAccess": t.string().optional(),
            "desiredNotificationConfig": t.proxy(
                renames["NotificationConfigIn"]
            ).optional(),
            "desiredL4ilbSubsettingConfig": t.proxy(
                renames["ILBSubsettingConfigIn"]
            ).optional(),
            "desiredPrivateClusterConfig": t.proxy(
                renames["PrivateClusterConfigIn"]
            ).optional(),
            "desiredMeshCertificates": t.proxy(
                renames["MeshCertificatesIn"]
            ).optional(),
            "additionalPodRangesConfig": t.proxy(
                renames["AdditionalPodRangesConfigIn"]
            ).optional(),
            "desiredNodePoolAutoConfigNetworkTags": t.proxy(
                renames["NetworkTagsIn"]
            ).optional(),
            "desiredServiceExternalIpsConfig": t.proxy(
                renames["ServiceExternalIPsConfigIn"]
            ).optional(),
            "desiredGatewayApiConfig": t.proxy(
                renames["GatewayAPIConfigIn"]
            ).optional(),
            "removedAdditionalPodRangesConfig": t.proxy(
                renames["AdditionalPodRangesConfigIn"]
            ).optional(),
            "desiredStackType": t.string().optional(),
            "desiredBinaryAuthorization": t.proxy(
                renames["BinaryAuthorizationIn"]
            ).optional(),
            "desiredDefaultSnatStatus": t.proxy(
                renames["DefaultSnatStatusIn"]
            ).optional(),
            "desiredNodePoolId": t.string().optional(),
            "desiredIntraNodeVisibilityConfig": t.proxy(
                renames["IntraNodeVisibilityConfigIn"]
            ).optional(),
            "desiredImageType": t.string().optional(),
            "desiredAddonsConfig": t.proxy(renames["AddonsConfigIn"]).optional(),
            "desiredLocations": t.array(t.string()).optional(),
            "desiredReleaseChannel": t.proxy(renames["ReleaseChannelIn"]).optional(),
            "desiredEnablePrivateEndpoint": t.boolean().optional(),
            "desiredNodeVersion": t.string().optional(),
            "desiredLoggingService": t.string().optional(),
            "desiredNodePoolLoggingConfig": t.proxy(
                renames["NodePoolLoggingConfigIn"]
            ).optional(),
            "desiredShieldedNodes": t.proxy(renames["ShieldedNodesIn"]).optional(),
            "desiredCostManagementConfig": t.proxy(
                renames["CostManagementConfigIn"]
            ).optional(),
            "desiredLoggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "desiredResourceUsageExportConfig": t.proxy(
                renames["ResourceUsageExportConfigIn"]
            ).optional(),
        }
    ).named(renames["ClusterUpdateIn"])
    types["ClusterUpdateOut"] = t.struct(
        {
            "desiredMonitoringConfig": t.proxy(
                renames["MonitoringConfigOut"]
            ).optional(),
            "desiredGcfsConfig": t.proxy(renames["GcfsConfigOut"]).optional(),
            "desiredMasterVersion": t.string().optional(),
            "desiredDatapathProvider": t.string().optional(),
            "desiredIdentityServiceConfig": t.proxy(
                renames["IdentityServiceConfigOut"]
            ).optional(),
            "desiredWorkloadIdentityConfig": t.proxy(
                renames["WorkloadIdentityConfigOut"]
            ).optional(),
            "desiredFleet": t.proxy(renames["FleetOut"]).optional(),
            "desiredVerticalPodAutoscaling": t.proxy(
                renames["VerticalPodAutoscalingOut"]
            ).optional(),
            "desiredDnsConfig": t.proxy(renames["DNSConfigOut"]).optional(),
            "etag": t.string().optional(),
            "desiredMonitoringService": t.string().optional(),
            "desiredAuthenticatorGroupsConfig": t.proxy(
                renames["AuthenticatorGroupsConfigOut"]
            ).optional(),
            "desiredMasterAuthorizedNetworksConfig": t.proxy(
                renames["MasterAuthorizedNetworksConfigOut"]
            ).optional(),
            "desiredNodePoolAutoscaling": t.proxy(
                renames["NodePoolAutoscalingOut"]
            ).optional(),
            "desiredDatabaseEncryption": t.proxy(
                renames["DatabaseEncryptionOut"]
            ).optional(),
            "desiredClusterAutoscaling": t.proxy(
                renames["ClusterAutoscalingOut"]
            ).optional(),
            "desiredPrivateIpv6GoogleAccess": t.string().optional(),
            "desiredNotificationConfig": t.proxy(
                renames["NotificationConfigOut"]
            ).optional(),
            "desiredL4ilbSubsettingConfig": t.proxy(
                renames["ILBSubsettingConfigOut"]
            ).optional(),
            "desiredPrivateClusterConfig": t.proxy(
                renames["PrivateClusterConfigOut"]
            ).optional(),
            "desiredMeshCertificates": t.proxy(
                renames["MeshCertificatesOut"]
            ).optional(),
            "additionalPodRangesConfig": t.proxy(
                renames["AdditionalPodRangesConfigOut"]
            ).optional(),
            "desiredNodePoolAutoConfigNetworkTags": t.proxy(
                renames["NetworkTagsOut"]
            ).optional(),
            "desiredServiceExternalIpsConfig": t.proxy(
                renames["ServiceExternalIPsConfigOut"]
            ).optional(),
            "desiredGatewayApiConfig": t.proxy(
                renames["GatewayAPIConfigOut"]
            ).optional(),
            "removedAdditionalPodRangesConfig": t.proxy(
                renames["AdditionalPodRangesConfigOut"]
            ).optional(),
            "desiredStackType": t.string().optional(),
            "desiredBinaryAuthorization": t.proxy(
                renames["BinaryAuthorizationOut"]
            ).optional(),
            "desiredDefaultSnatStatus": t.proxy(
                renames["DefaultSnatStatusOut"]
            ).optional(),
            "desiredNodePoolId": t.string().optional(),
            "desiredIntraNodeVisibilityConfig": t.proxy(
                renames["IntraNodeVisibilityConfigOut"]
            ).optional(),
            "desiredImageType": t.string().optional(),
            "desiredAddonsConfig": t.proxy(renames["AddonsConfigOut"]).optional(),
            "desiredLocations": t.array(t.string()).optional(),
            "desiredReleaseChannel": t.proxy(renames["ReleaseChannelOut"]).optional(),
            "desiredEnablePrivateEndpoint": t.boolean().optional(),
            "desiredNodeVersion": t.string().optional(),
            "desiredLoggingService": t.string().optional(),
            "desiredNodePoolLoggingConfig": t.proxy(
                renames["NodePoolLoggingConfigOut"]
            ).optional(),
            "desiredShieldedNodes": t.proxy(renames["ShieldedNodesOut"]).optional(),
            "desiredCostManagementConfig": t.proxy(
                renames["CostManagementConfigOut"]
            ).optional(),
            "desiredLoggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "desiredResourceUsageExportConfig": t.proxy(
                renames["ResourceUsageExportConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterUpdateOut"])
    types["HttpLoadBalancingIn"] = t.struct({"disabled": t.boolean().optional()}).named(
        renames["HttpLoadBalancingIn"]
    )
    types["HttpLoadBalancingOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpLoadBalancingOut"])
    types["GcpFilestoreCsiDriverConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["GcpFilestoreCsiDriverConfigIn"])
    types["GcpFilestoreCsiDriverConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcpFilestoreCsiDriverConfigOut"])
    types["MaintenanceExclusionOptionsIn"] = t.struct(
        {"scope": t.string().optional()}
    ).named(renames["MaintenanceExclusionOptionsIn"])
    types["MaintenanceExclusionOptionsOut"] = t.struct(
        {
            "scope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceExclusionOptionsOut"])
    types["NetworkPolicyConfigIn"] = t.struct(
        {"disabled": t.boolean().optional()}
    ).named(renames["NetworkPolicyConfigIn"])
    types["NetworkPolicyConfigOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkPolicyConfigOut"])
    types["AddonsConfigIn"] = t.struct(
        {
            "cloudRunConfig": t.proxy(renames["CloudRunConfigIn"]).optional(),
            "gkeBackupAgentConfig": t.proxy(
                renames["GkeBackupAgentConfigIn"]
            ).optional(),
            "horizontalPodAutoscaling": t.proxy(
                renames["HorizontalPodAutoscalingIn"]
            ).optional(),
            "networkPolicyConfig": t.proxy(renames["NetworkPolicyConfigIn"]).optional(),
            "gcePersistentDiskCsiDriverConfig": t.proxy(
                renames["GcePersistentDiskCsiDriverConfigIn"]
            ).optional(),
            "dnsCacheConfig": t.proxy(renames["DnsCacheConfigIn"]).optional(),
            "gcpFilestoreCsiDriverConfig": t.proxy(
                renames["GcpFilestoreCsiDriverConfigIn"]
            ).optional(),
            "configConnectorConfig": t.proxy(
                renames["ConfigConnectorConfigIn"]
            ).optional(),
            "httpLoadBalancing": t.proxy(renames["HttpLoadBalancingIn"]).optional(),
            "kubernetesDashboard": t.proxy(renames["KubernetesDashboardIn"]).optional(),
        }
    ).named(renames["AddonsConfigIn"])
    types["AddonsConfigOut"] = t.struct(
        {
            "cloudRunConfig": t.proxy(renames["CloudRunConfigOut"]).optional(),
            "gkeBackupAgentConfig": t.proxy(
                renames["GkeBackupAgentConfigOut"]
            ).optional(),
            "horizontalPodAutoscaling": t.proxy(
                renames["HorizontalPodAutoscalingOut"]
            ).optional(),
            "networkPolicyConfig": t.proxy(
                renames["NetworkPolicyConfigOut"]
            ).optional(),
            "gcePersistentDiskCsiDriverConfig": t.proxy(
                renames["GcePersistentDiskCsiDriverConfigOut"]
            ).optional(),
            "dnsCacheConfig": t.proxy(renames["DnsCacheConfigOut"]).optional(),
            "gcpFilestoreCsiDriverConfig": t.proxy(
                renames["GcpFilestoreCsiDriverConfigOut"]
            ).optional(),
            "configConnectorConfig": t.proxy(
                renames["ConfigConnectorConfigOut"]
            ).optional(),
            "httpLoadBalancing": t.proxy(renames["HttpLoadBalancingOut"]).optional(),
            "kubernetesDashboard": t.proxy(
                renames["KubernetesDashboardOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddonsConfigOut"])
    types["MaxPodsConstraintIn"] = t.struct(
        {"maxPodsPerNode": t.string().optional()}
    ).named(renames["MaxPodsConstraintIn"])
    types["MaxPodsConstraintOut"] = t.struct(
        {
            "maxPodsPerNode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaxPodsConstraintOut"])
    types["OperationIn"] = t.struct(
        {
            "nodepoolConditions": t.array(
                t.proxy(renames["StatusConditionIn"])
            ).optional(),
            "status": t.string().optional(),
            "selfLink": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "operationType": t.string().optional(),
            "zone": t.string().optional(),
            "detail": t.string().optional(),
            "clusterConditions": t.array(
                t.proxy(renames["StatusConditionIn"])
            ).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "targetLink": t.string().optional(),
            "location": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "nodepoolConditions": t.array(
                t.proxy(renames["StatusConditionOut"])
            ).optional(),
            "status": t.string().optional(),
            "selfLink": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "operationType": t.string().optional(),
            "statusMessage": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "zone": t.string().optional(),
            "detail": t.string().optional(),
            "clusterConditions": t.array(
                t.proxy(renames["StatusConditionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "targetLink": t.string().optional(),
            "location": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["StartIPRotationRequestIn"] = t.struct(
        {
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
            "rotateCredentials": t.boolean().optional(),
            "clusterId": t.string().optional(),
        }
    ).named(renames["StartIPRotationRequestIn"])
    types["StartIPRotationRequestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
            "rotateCredentials": t.boolean().optional(),
            "clusterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartIPRotationRequestOut"])
    types["NetworkTagsIn"] = t.struct({"tags": t.array(t.string()).optional()}).named(
        renames["NetworkTagsIn"]
    )
    types["NetworkTagsOut"] = t.struct(
        {
            "tags": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkTagsOut"])
    types["MeshCertificatesIn"] = t.struct(
        {"enableCertificates": t.boolean().optional()}
    ).named(renames["MeshCertificatesIn"])
    types["MeshCertificatesOut"] = t.struct(
        {
            "enableCertificates": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MeshCertificatesOut"])
    types["SetLocationsRequestIn"] = t.struct(
        {
            "locations": t.array(t.string()),
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SetLocationsRequestIn"])
    types["SetLocationsRequestOut"] = t.struct(
        {
            "locations": t.array(t.string()),
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetLocationsRequestOut"])

    functions = {}
    functions["projectsLocationsGetServerConfig"] = container.get(
        "v1/{name}/serverConfig",
        t.struct(
            {
                "projectId": t.string().optional(),
                "name": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServerConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetLogging"] = container.post(
        "v1/{name}:setMaintenancePolicy",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string(),
                "projectId": t.string(),
                "clusterId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetNetworkPolicy"] = container.post(
        "v1/{name}:setMaintenancePolicy",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string(),
                "projectId": t.string(),
                "clusterId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetMonitoring"] = container.post(
        "v1/{name}:setMaintenancePolicy",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string(),
                "projectId": t.string(),
                "clusterId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetAddons"] = container.post(
        "v1/{name}:setMaintenancePolicy",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string(),
                "projectId": t.string(),
                "clusterId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetLegacyAbac"] = container.post(
        "v1/{name}:setMaintenancePolicy",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string(),
                "projectId": t.string(),
                "clusterId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersList"] = container.post(
        "v1/{name}:setMaintenancePolicy",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string(),
                "projectId": t.string(),
                "clusterId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetMasterAuth"] = container.post(
        "v1/{name}:setMaintenancePolicy",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string(),
                "projectId": t.string(),
                "clusterId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersCompleteIpRotation"] = container.post(
        "v1/{name}:setMaintenancePolicy",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string(),
                "projectId": t.string(),
                "clusterId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersStartIpRotation"] = container.post(
        "v1/{name}:setMaintenancePolicy",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string(),
                "projectId": t.string(),
                "clusterId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetResourceLabels"] = container.post(
        "v1/{name}:setMaintenancePolicy",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string(),
                "projectId": t.string(),
                "clusterId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersDelete"] = container.post(
        "v1/{name}:setMaintenancePolicy",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string(),
                "projectId": t.string(),
                "clusterId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersUpdate"] = container.post(
        "v1/{name}:setMaintenancePolicy",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string(),
                "projectId": t.string(),
                "clusterId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersGetJwks"] = container.post(
        "v1/{name}:setMaintenancePolicy",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string(),
                "projectId": t.string(),
                "clusterId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersGet"] = container.post(
        "v1/{name}:setMaintenancePolicy",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string(),
                "projectId": t.string(),
                "clusterId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersUpdateMaster"] = container.post(
        "v1/{name}:setMaintenancePolicy",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string(),
                "projectId": t.string(),
                "clusterId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersCreate"] = container.post(
        "v1/{name}:setMaintenancePolicy",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string(),
                "projectId": t.string(),
                "clusterId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetLocations"] = container.post(
        "v1/{name}:setMaintenancePolicy",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string(),
                "projectId": t.string(),
                "clusterId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetMaintenancePolicy"] = container.post(
        "v1/{name}:setMaintenancePolicy",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string(),
                "projectId": t.string(),
                "clusterId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
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
    functions["projectsLocationsClustersNodePoolsSetManagement"] = container.delete(
        "v1/{name}",
        t.struct(
            {
                "zone": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "name": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsUpdate"] = container.delete(
        "v1/{name}",
        t.struct(
            {
                "zone": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "name": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsCompleteUpgrade"] = container.delete(
        "v1/{name}",
        t.struct(
            {
                "zone": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "name": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsSetAutoscaling"] = container.delete(
        "v1/{name}",
        t.struct(
            {
                "zone": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "name": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsGet"] = container.delete(
        "v1/{name}",
        t.struct(
            {
                "zone": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "name": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsRollback"] = container.delete(
        "v1/{name}",
        t.struct(
            {
                "zone": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "name": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsCreate"] = container.delete(
        "v1/{name}",
        t.struct(
            {
                "zone": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "name": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsList"] = container.delete(
        "v1/{name}",
        t.struct(
            {
                "zone": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "name": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsSetSize"] = container.delete(
        "v1/{name}",
        t.struct(
            {
                "zone": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "name": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsDelete"] = container.delete(
        "v1/{name}",
        t.struct(
            {
                "zone": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "name": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string().optional(),
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
                "name": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServerConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersMaster"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/monitoring",
        t.struct(
            {
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "monitoringService": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersSetMasterAuth"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/monitoring",
        t.struct(
            {
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "monitoringService": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersCreate"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/monitoring",
        t.struct(
            {
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "monitoringService": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersLocations"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/monitoring",
        t.struct(
            {
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "monitoringService": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersSetMaintenancePolicy"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/monitoring",
        t.struct(
            {
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "monitoringService": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersCompleteIpRotation"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/monitoring",
        t.struct(
            {
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "monitoringService": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersUpdate"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/monitoring",
        t.struct(
            {
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "monitoringService": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersAddons"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/monitoring",
        t.struct(
            {
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "monitoringService": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersLogging"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/monitoring",
        t.struct(
            {
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "monitoringService": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersStartIpRotation"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/monitoring",
        t.struct(
            {
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "monitoringService": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersList"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/monitoring",
        t.struct(
            {
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "monitoringService": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersResourceLabels"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/monitoring",
        t.struct(
            {
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "monitoringService": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersGet"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/monitoring",
        t.struct(
            {
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "monitoringService": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersSetNetworkPolicy"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/monitoring",
        t.struct(
            {
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "monitoringService": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersLegacyAbac"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/monitoring",
        t.struct(
            {
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "monitoringService": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersDelete"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/monitoring",
        t.struct(
            {
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "monitoringService": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersMonitoring"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/monitoring",
        t.struct(
            {
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "monitoringService": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsGet"] = container.delete(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}",
        t.struct(
            {
                "zone": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsSetManagement"] = container.delete(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}",
        t.struct(
            {
                "zone": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsSetSize"] = container.delete(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}",
        t.struct(
            {
                "zone": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsList"] = container.delete(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}",
        t.struct(
            {
                "zone": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsAutoscaling"] = container.delete(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}",
        t.struct(
            {
                "zone": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsRollback"] = container.delete(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}",
        t.struct(
            {
                "zone": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsUpdate"] = container.delete(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}",
        t.struct(
            {
                "zone": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsCreate"] = container.delete(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}",
        t.struct(
            {
                "zone": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsDelete"] = container.delete(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}",
        t.struct(
            {
                "zone": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "clusterId": t.string().optional(),
                "projectId": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesOperationsList"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/operations/{operationId}:cancel",
        t.struct(
            {
                "projectId": t.string().optional(),
                "operationId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesOperationsGet"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/operations/{operationId}:cancel",
        t.struct(
            {
                "projectId": t.string().optional(),
                "operationId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesOperationsCancel"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/operations/{operationId}:cancel",
        t.struct(
            {
                "projectId": t.string().optional(),
                "operationId": t.string().optional(),
                "zone": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="container",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
