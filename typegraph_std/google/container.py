from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_container():
    container = HTTPRuntime("https://container.googleapis.com/")

    renames = {
        "ErrorResponse": "_container_1_ErrorResponse",
        "VirtualNICIn": "_container_2_VirtualNICIn",
        "VirtualNICOut": "_container_3_VirtualNICOut",
        "SandboxConfigIn": "_container_4_SandboxConfigIn",
        "SandboxConfigOut": "_container_5_SandboxConfigOut",
        "GetJSONWebKeysResponseIn": "_container_6_GetJSONWebKeysResponseIn",
        "GetJSONWebKeysResponseOut": "_container_7_GetJSONWebKeysResponseOut",
        "WorkloadPolicyConfigIn": "_container_8_WorkloadPolicyConfigIn",
        "WorkloadPolicyConfigOut": "_container_9_WorkloadPolicyConfigOut",
        "SecurityPostureConfigIn": "_container_10_SecurityPostureConfigIn",
        "SecurityPostureConfigOut": "_container_11_SecurityPostureConfigOut",
        "AutopilotIn": "_container_12_AutopilotIn",
        "AutopilotOut": "_container_13_AutopilotOut",
        "CidrBlockIn": "_container_14_CidrBlockIn",
        "CidrBlockOut": "_container_15_CidrBlockOut",
        "HttpLoadBalancingIn": "_container_16_HttpLoadBalancingIn",
        "HttpLoadBalancingOut": "_container_17_HttpLoadBalancingOut",
        "NodeNetworkConfigIn": "_container_18_NodeNetworkConfigIn",
        "NodeNetworkConfigOut": "_container_19_NodeNetworkConfigOut",
        "AutopilotCompatibilityIssueIn": "_container_20_AutopilotCompatibilityIssueIn",
        "AutopilotCompatibilityIssueOut": "_container_21_AutopilotCompatibilityIssueOut",
        "CreateNodePoolRequestIn": "_container_22_CreateNodePoolRequestIn",
        "CreateNodePoolRequestOut": "_container_23_CreateNodePoolRequestOut",
        "UpgradeSettingsIn": "_container_24_UpgradeSettingsIn",
        "UpgradeSettingsOut": "_container_25_UpgradeSettingsOut",
        "AddonsConfigIn": "_container_26_AddonsConfigIn",
        "AddonsConfigOut": "_container_27_AddonsConfigOut",
        "ShieldedInstanceConfigIn": "_container_28_ShieldedInstanceConfigIn",
        "ShieldedInstanceConfigOut": "_container_29_ShieldedInstanceConfigOut",
        "ConfigConnectorConfigIn": "_container_30_ConfigConnectorConfigIn",
        "ConfigConnectorConfigOut": "_container_31_ConfigConnectorConfigOut",
        "WindowsNodeConfigIn": "_container_32_WindowsNodeConfigIn",
        "WindowsNodeConfigOut": "_container_33_WindowsNodeConfigOut",
        "StatusConditionIn": "_container_34_StatusConditionIn",
        "StatusConditionOut": "_container_35_StatusConditionOut",
        "ResourceLabelsIn": "_container_36_ResourceLabelsIn",
        "ResourceLabelsOut": "_container_37_ResourceLabelsOut",
        "AdditionalPodRangesConfigIn": "_container_38_AdditionalPodRangesConfigIn",
        "AdditionalPodRangesConfigOut": "_container_39_AdditionalPodRangesConfigOut",
        "NodeKubeletConfigIn": "_container_40_NodeKubeletConfigIn",
        "NodeKubeletConfigOut": "_container_41_NodeKubeletConfigOut",
        "LegacyAbacIn": "_container_42_LegacyAbacIn",
        "LegacyAbacOut": "_container_43_LegacyAbacOut",
        "RangeInfoIn": "_container_44_RangeInfoIn",
        "RangeInfoOut": "_container_45_RangeInfoOut",
        "JwkIn": "_container_46_JwkIn",
        "JwkOut": "_container_47_JwkOut",
        "ServiceExternalIPsConfigIn": "_container_48_ServiceExternalIPsConfigIn",
        "ServiceExternalIPsConfigOut": "_container_49_ServiceExternalIPsConfigOut",
        "HorizontalPodAutoscalingIn": "_container_50_HorizontalPodAutoscalingIn",
        "HorizontalPodAutoscalingOut": "_container_51_HorizontalPodAutoscalingOut",
        "MonitoringComponentConfigIn": "_container_52_MonitoringComponentConfigIn",
        "MonitoringComponentConfigOut": "_container_53_MonitoringComponentConfigOut",
        "SetAddonsConfigRequestIn": "_container_54_SetAddonsConfigRequestIn",
        "SetAddonsConfigRequestOut": "_container_55_SetAddonsConfigRequestOut",
        "HttpCacheControlResponseHeaderIn": "_container_56_HttpCacheControlResponseHeaderIn",
        "HttpCacheControlResponseHeaderOut": "_container_57_HttpCacheControlResponseHeaderOut",
        "CompleteIPRotationRequestIn": "_container_58_CompleteIPRotationRequestIn",
        "CompleteIPRotationRequestOut": "_container_59_CompleteIPRotationRequestOut",
        "MeshCertificatesIn": "_container_60_MeshCertificatesIn",
        "MeshCertificatesOut": "_container_61_MeshCertificatesOut",
        "SetMasterAuthRequestIn": "_container_62_SetMasterAuthRequestIn",
        "SetMasterAuthRequestOut": "_container_63_SetMasterAuthRequestOut",
        "ServerConfigIn": "_container_64_ServerConfigIn",
        "ServerConfigOut": "_container_65_ServerConfigOut",
        "AdvancedMachineFeaturesIn": "_container_66_AdvancedMachineFeaturesIn",
        "AdvancedMachineFeaturesOut": "_container_67_AdvancedMachineFeaturesOut",
        "VerticalPodAutoscalingIn": "_container_68_VerticalPodAutoscalingIn",
        "VerticalPodAutoscalingOut": "_container_69_VerticalPodAutoscalingOut",
        "EmptyIn": "_container_70_EmptyIn",
        "EmptyOut": "_container_71_EmptyOut",
        "DnsCacheConfigIn": "_container_72_DnsCacheConfigIn",
        "DnsCacheConfigOut": "_container_73_DnsCacheConfigOut",
        "EphemeralStorageLocalSsdConfigIn": "_container_74_EphemeralStorageLocalSsdConfigIn",
        "EphemeralStorageLocalSsdConfigOut": "_container_75_EphemeralStorageLocalSsdConfigOut",
        "MaintenanceWindowIn": "_container_76_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_container_77_MaintenanceWindowOut",
        "NetworkPerformanceConfigIn": "_container_78_NetworkPerformanceConfigIn",
        "NetworkPerformanceConfigOut": "_container_79_NetworkPerformanceConfigOut",
        "CostManagementConfigIn": "_container_80_CostManagementConfigIn",
        "CostManagementConfigOut": "_container_81_CostManagementConfigOut",
        "NodeConfigIn": "_container_82_NodeConfigIn",
        "NodeConfigOut": "_container_83_NodeConfigOut",
        "ILBSubsettingConfigIn": "_container_84_ILBSubsettingConfigIn",
        "ILBSubsettingConfigOut": "_container_85_ILBSubsettingConfigOut",
        "NodeManagementIn": "_container_86_NodeManagementIn",
        "NodeManagementOut": "_container_87_NodeManagementOut",
        "NodePoolLoggingConfigIn": "_container_88_NodePoolLoggingConfigIn",
        "NodePoolLoggingConfigOut": "_container_89_NodePoolLoggingConfigOut",
        "LoggingComponentConfigIn": "_container_90_LoggingComponentConfigIn",
        "LoggingComponentConfigOut": "_container_91_LoggingComponentConfigOut",
        "ReleaseChannelConfigIn": "_container_92_ReleaseChannelConfigIn",
        "ReleaseChannelConfigOut": "_container_93_ReleaseChannelConfigOut",
        "BigQueryDestinationIn": "_container_94_BigQueryDestinationIn",
        "BigQueryDestinationOut": "_container_95_BigQueryDestinationOut",
        "RollbackNodePoolUpgradeRequestIn": "_container_96_RollbackNodePoolUpgradeRequestIn",
        "RollbackNodePoolUpgradeRequestOut": "_container_97_RollbackNodePoolUpgradeRequestOut",
        "FastSocketIn": "_container_98_FastSocketIn",
        "FastSocketOut": "_container_99_FastSocketOut",
        "MaxPodsConstraintIn": "_container_100_MaxPodsConstraintIn",
        "MaxPodsConstraintOut": "_container_101_MaxPodsConstraintOut",
        "ClusterAutoscalingIn": "_container_102_ClusterAutoscalingIn",
        "ClusterAutoscalingOut": "_container_103_ClusterAutoscalingOut",
        "CreateClusterRequestIn": "_container_104_CreateClusterRequestIn",
        "CreateClusterRequestOut": "_container_105_CreateClusterRequestOut",
        "GcpFilestoreCsiDriverConfigIn": "_container_106_GcpFilestoreCsiDriverConfigIn",
        "GcpFilestoreCsiDriverConfigOut": "_container_107_GcpFilestoreCsiDriverConfigOut",
        "SetNetworkPolicyRequestIn": "_container_108_SetNetworkPolicyRequestIn",
        "SetNetworkPolicyRequestOut": "_container_109_SetNetworkPolicyRequestOut",
        "NetworkPolicyConfigIn": "_container_110_NetworkPolicyConfigIn",
        "NetworkPolicyConfigOut": "_container_111_NetworkPolicyConfigOut",
        "CheckAutopilotCompatibilityResponseIn": "_container_112_CheckAutopilotCompatibilityResponseIn",
        "CheckAutopilotCompatibilityResponseOut": "_container_113_CheckAutopilotCompatibilityResponseOut",
        "UsableSubnetworkIn": "_container_114_UsableSubnetworkIn",
        "UsableSubnetworkOut": "_container_115_UsableSubnetworkOut",
        "GetOpenIDConfigResponseIn": "_container_116_GetOpenIDConfigResponseIn",
        "GetOpenIDConfigResponseOut": "_container_117_GetOpenIDConfigResponseOut",
        "MasterAuthorizedNetworksConfigIn": "_container_118_MasterAuthorizedNetworksConfigIn",
        "MasterAuthorizedNetworksConfigOut": "_container_119_MasterAuthorizedNetworksConfigOut",
        "FleetIn": "_container_120_FleetIn",
        "FleetOut": "_container_121_FleetOut",
        "OperationProgressIn": "_container_122_OperationProgressIn",
        "OperationProgressOut": "_container_123_OperationProgressOut",
        "ReservationAffinityIn": "_container_124_ReservationAffinityIn",
        "ReservationAffinityOut": "_container_125_ReservationAffinityOut",
        "SetNodePoolSizeRequestIn": "_container_126_SetNodePoolSizeRequestIn",
        "SetNodePoolSizeRequestOut": "_container_127_SetNodePoolSizeRequestOut",
        "CancelOperationRequestIn": "_container_128_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_container_129_CancelOperationRequestOut",
        "SetMonitoringServiceRequestIn": "_container_130_SetMonitoringServiceRequestIn",
        "SetMonitoringServiceRequestOut": "_container_131_SetMonitoringServiceRequestOut",
        "StatusIn": "_container_132_StatusIn",
        "StatusOut": "_container_133_StatusOut",
        "WorkloadIdentityConfigIn": "_container_134_WorkloadIdentityConfigIn",
        "WorkloadIdentityConfigOut": "_container_135_WorkloadIdentityConfigOut",
        "NodeTaintsIn": "_container_136_NodeTaintsIn",
        "NodeTaintsOut": "_container_137_NodeTaintsOut",
        "WorkloadMetadataConfigIn": "_container_138_WorkloadMetadataConfigIn",
        "WorkloadMetadataConfigOut": "_container_139_WorkloadMetadataConfigOut",
        "ResourceLimitIn": "_container_140_ResourceLimitIn",
        "ResourceLimitOut": "_container_141_ResourceLimitOut",
        "AutoUpgradeOptionsIn": "_container_142_AutoUpgradeOptionsIn",
        "AutoUpgradeOptionsOut": "_container_143_AutoUpgradeOptionsOut",
        "LoggingVariantConfigIn": "_container_144_LoggingVariantConfigIn",
        "LoggingVariantConfigOut": "_container_145_LoggingVariantConfigOut",
        "ReleaseChannelIn": "_container_146_ReleaseChannelIn",
        "ReleaseChannelOut": "_container_147_ReleaseChannelOut",
        "GkeBackupAgentConfigIn": "_container_148_GkeBackupAgentConfigIn",
        "GkeBackupAgentConfigOut": "_container_149_GkeBackupAgentConfigOut",
        "MetricIn": "_container_150_MetricIn",
        "MetricOut": "_container_151_MetricOut",
        "BlueGreenInfoIn": "_container_152_BlueGreenInfoIn",
        "BlueGreenInfoOut": "_container_153_BlueGreenInfoOut",
        "PlacementPolicyIn": "_container_154_PlacementPolicyIn",
        "PlacementPolicyOut": "_container_155_PlacementPolicyOut",
        "MaintenancePolicyIn": "_container_156_MaintenancePolicyIn",
        "MaintenancePolicyOut": "_container_157_MaintenancePolicyOut",
        "ClusterNetworkPerformanceConfigIn": "_container_158_ClusterNetworkPerformanceConfigIn",
        "ClusterNetworkPerformanceConfigOut": "_container_159_ClusterNetworkPerformanceConfigOut",
        "K8sBetaAPIConfigIn": "_container_160_K8sBetaAPIConfigIn",
        "K8sBetaAPIConfigOut": "_container_161_K8sBetaAPIConfigOut",
        "LocalNvmeSsdBlockConfigIn": "_container_162_LocalNvmeSsdBlockConfigIn",
        "LocalNvmeSsdBlockConfigOut": "_container_163_LocalNvmeSsdBlockConfigOut",
        "ConsumptionMeteringConfigIn": "_container_164_ConsumptionMeteringConfigIn",
        "ConsumptionMeteringConfigOut": "_container_165_ConsumptionMeteringConfigOut",
        "ListUsableSubnetworksResponseIn": "_container_166_ListUsableSubnetworksResponseIn",
        "ListUsableSubnetworksResponseOut": "_container_167_ListUsableSubnetworksResponseOut",
        "SetLabelsRequestIn": "_container_168_SetLabelsRequestIn",
        "SetLabelsRequestOut": "_container_169_SetLabelsRequestOut",
        "UpdateClusterRequestIn": "_container_170_UpdateClusterRequestIn",
        "UpdateClusterRequestOut": "_container_171_UpdateClusterRequestOut",
        "ListClustersResponseIn": "_container_172_ListClustersResponseIn",
        "ListClustersResponseOut": "_container_173_ListClustersResponseOut",
        "DailyMaintenanceWindowIn": "_container_174_DailyMaintenanceWindowIn",
        "DailyMaintenanceWindowOut": "_container_175_DailyMaintenanceWindowOut",
        "CloudRunConfigIn": "_container_176_CloudRunConfigIn",
        "CloudRunConfigOut": "_container_177_CloudRunConfigOut",
        "BlueGreenSettingsIn": "_container_178_BlueGreenSettingsIn",
        "BlueGreenSettingsOut": "_container_179_BlueGreenSettingsOut",
        "LoggingConfigIn": "_container_180_LoggingConfigIn",
        "LoggingConfigOut": "_container_181_LoggingConfigOut",
        "SetLoggingServiceRequestIn": "_container_182_SetLoggingServiceRequestIn",
        "SetLoggingServiceRequestOut": "_container_183_SetLoggingServiceRequestOut",
        "IPAllocationPolicyIn": "_container_184_IPAllocationPolicyIn",
        "IPAllocationPolicyOut": "_container_185_IPAllocationPolicyOut",
        "UsableSubnetworkSecondaryRangeIn": "_container_186_UsableSubnetworkSecondaryRangeIn",
        "UsableSubnetworkSecondaryRangeOut": "_container_187_UsableSubnetworkSecondaryRangeOut",
        "NetworkConfigIn": "_container_188_NetworkConfigIn",
        "NetworkConfigOut": "_container_189_NetworkConfigOut",
        "ResourceUsageExportConfigIn": "_container_190_ResourceUsageExportConfigIn",
        "ResourceUsageExportConfigOut": "_container_191_ResourceUsageExportConfigOut",
        "PrivateClusterConfigIn": "_container_192_PrivateClusterConfigIn",
        "PrivateClusterConfigOut": "_container_193_PrivateClusterConfigOut",
        "NodePoolAutoscalingIn": "_container_194_NodePoolAutoscalingIn",
        "NodePoolAutoscalingOut": "_container_195_NodePoolAutoscalingOut",
        "DNSConfigIn": "_container_196_DNSConfigIn",
        "DNSConfigOut": "_container_197_DNSConfigOut",
        "SetNodePoolManagementRequestIn": "_container_198_SetNodePoolManagementRequestIn",
        "SetNodePoolManagementRequestOut": "_container_199_SetNodePoolManagementRequestOut",
        "UpdateInfoIn": "_container_200_UpdateInfoIn",
        "UpdateInfoOut": "_container_201_UpdateInfoOut",
        "SetLegacyAbacRequestIn": "_container_202_SetLegacyAbacRequestIn",
        "SetLegacyAbacRequestOut": "_container_203_SetLegacyAbacRequestOut",
        "IdentityServiceConfigIn": "_container_204_IdentityServiceConfigIn",
        "IdentityServiceConfigOut": "_container_205_IdentityServiceConfigOut",
        "KubernetesDashboardIn": "_container_206_KubernetesDashboardIn",
        "KubernetesDashboardOut": "_container_207_KubernetesDashboardOut",
        "NodeAffinityIn": "_container_208_NodeAffinityIn",
        "NodeAffinityOut": "_container_209_NodeAffinityOut",
        "MasterAuthIn": "_container_210_MasterAuthIn",
        "MasterAuthOut": "_container_211_MasterAuthOut",
        "DatabaseEncryptionIn": "_container_212_DatabaseEncryptionIn",
        "DatabaseEncryptionOut": "_container_213_DatabaseEncryptionOut",
        "GPUDriverInstallationConfigIn": "_container_214_GPUDriverInstallationConfigIn",
        "GPUDriverInstallationConfigOut": "_container_215_GPUDriverInstallationConfigOut",
        "ListNodePoolsResponseIn": "_container_216_ListNodePoolsResponseIn",
        "ListNodePoolsResponseOut": "_container_217_ListNodePoolsResponseOut",
        "SoleTenantConfigIn": "_container_218_SoleTenantConfigIn",
        "SoleTenantConfigOut": "_container_219_SoleTenantConfigOut",
        "CompleteNodePoolUpgradeRequestIn": "_container_220_CompleteNodePoolUpgradeRequestIn",
        "CompleteNodePoolUpgradeRequestOut": "_container_221_CompleteNodePoolUpgradeRequestOut",
        "UpdateNodePoolRequestIn": "_container_222_UpdateNodePoolRequestIn",
        "UpdateNodePoolRequestOut": "_container_223_UpdateNodePoolRequestOut",
        "NodeTaintIn": "_container_224_NodeTaintIn",
        "NodeTaintOut": "_container_225_NodeTaintOut",
        "MonitoringConfigIn": "_container_226_MonitoringConfigIn",
        "MonitoringConfigOut": "_container_227_MonitoringConfigOut",
        "ShieldedNodesIn": "_container_228_ShieldedNodesIn",
        "ShieldedNodesOut": "_container_229_ShieldedNodesOut",
        "UpgradeAvailableEventIn": "_container_230_UpgradeAvailableEventIn",
        "UpgradeAvailableEventOut": "_container_231_UpgradeAvailableEventOut",
        "UpgradeEventIn": "_container_232_UpgradeEventIn",
        "UpgradeEventOut": "_container_233_UpgradeEventOut",
        "ClusterUpdateIn": "_container_234_ClusterUpdateIn",
        "ClusterUpdateOut": "_container_235_ClusterUpdateOut",
        "PubSubIn": "_container_236_PubSubIn",
        "PubSubOut": "_container_237_PubSubOut",
        "RecurringTimeWindowIn": "_container_238_RecurringTimeWindowIn",
        "RecurringTimeWindowOut": "_container_239_RecurringTimeWindowOut",
        "SecurityBulletinEventIn": "_container_240_SecurityBulletinEventIn",
        "SecurityBulletinEventOut": "_container_241_SecurityBulletinEventOut",
        "NodeLabelsIn": "_container_242_NodeLabelsIn",
        "NodeLabelsOut": "_container_243_NodeLabelsOut",
        "BinaryAuthorizationIn": "_container_244_BinaryAuthorizationIn",
        "BinaryAuthorizationOut": "_container_245_BinaryAuthorizationOut",
        "ManagedPrometheusConfigIn": "_container_246_ManagedPrometheusConfigIn",
        "ManagedPrometheusConfigOut": "_container_247_ManagedPrometheusConfigOut",
        "GcePersistentDiskCsiDriverConfigIn": "_container_248_GcePersistentDiskCsiDriverConfigIn",
        "GcePersistentDiskCsiDriverConfigOut": "_container_249_GcePersistentDiskCsiDriverConfigOut",
        "AcceleratorConfigIn": "_container_250_AcceleratorConfigIn",
        "AcceleratorConfigOut": "_container_251_AcceleratorConfigOut",
        "PodCIDROverprovisionConfigIn": "_container_252_PodCIDROverprovisionConfigIn",
        "PodCIDROverprovisionConfigOut": "_container_253_PodCIDROverprovisionConfigOut",
        "AuthenticatorGroupsConfigIn": "_container_254_AuthenticatorGroupsConfigIn",
        "AuthenticatorGroupsConfigOut": "_container_255_AuthenticatorGroupsConfigOut",
        "NodeConfigDefaultsIn": "_container_256_NodeConfigDefaultsIn",
        "NodeConfigDefaultsOut": "_container_257_NodeConfigDefaultsOut",
        "NetworkPolicyIn": "_container_258_NetworkPolicyIn",
        "NetworkPolicyOut": "_container_259_NetworkPolicyOut",
        "SetMaintenancePolicyRequestIn": "_container_260_SetMaintenancePolicyRequestIn",
        "SetMaintenancePolicyRequestOut": "_container_261_SetMaintenancePolicyRequestOut",
        "BestEffortProvisioningIn": "_container_262_BestEffortProvisioningIn",
        "BestEffortProvisioningOut": "_container_263_BestEffortProvisioningOut",
        "StandardRolloutPolicyIn": "_container_264_StandardRolloutPolicyIn",
        "StandardRolloutPolicyOut": "_container_265_StandardRolloutPolicyOut",
        "ConfidentialNodesIn": "_container_266_ConfidentialNodesIn",
        "ConfidentialNodesOut": "_container_267_ConfidentialNodesOut",
        "MaintenanceExclusionOptionsIn": "_container_268_MaintenanceExclusionOptionsIn",
        "MaintenanceExclusionOptionsOut": "_container_269_MaintenanceExclusionOptionsOut",
        "IntraNodeVisibilityConfigIn": "_container_270_IntraNodeVisibilityConfigIn",
        "IntraNodeVisibilityConfigOut": "_container_271_IntraNodeVisibilityConfigOut",
        "OperationIn": "_container_272_OperationIn",
        "OperationOut": "_container_273_OperationOut",
        "GPUSharingConfigIn": "_container_274_GPUSharingConfigIn",
        "GPUSharingConfigOut": "_container_275_GPUSharingConfigOut",
        "GatewayAPIConfigIn": "_container_276_GatewayAPIConfigIn",
        "GatewayAPIConfigOut": "_container_277_GatewayAPIConfigOut",
        "SetLocationsRequestIn": "_container_278_SetLocationsRequestIn",
        "SetLocationsRequestOut": "_container_279_SetLocationsRequestOut",
        "StartIPRotationRequestIn": "_container_280_StartIPRotationRequestIn",
        "StartIPRotationRequestOut": "_container_281_StartIPRotationRequestOut",
        "SetNodePoolAutoscalingRequestIn": "_container_282_SetNodePoolAutoscalingRequestIn",
        "SetNodePoolAutoscalingRequestOut": "_container_283_SetNodePoolAutoscalingRequestOut",
        "GcsFuseCsiDriverConfigIn": "_container_284_GcsFuseCsiDriverConfigIn",
        "GcsFuseCsiDriverConfigOut": "_container_285_GcsFuseCsiDriverConfigOut",
        "NetworkTagsIn": "_container_286_NetworkTagsIn",
        "NetworkTagsOut": "_container_287_NetworkTagsOut",
        "ListOperationsResponseIn": "_container_288_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_container_289_ListOperationsResponseOut",
        "TimeWindowIn": "_container_290_TimeWindowIn",
        "TimeWindowOut": "_container_291_TimeWindowOut",
        "NodePoolAutoConfigIn": "_container_292_NodePoolAutoConfigIn",
        "NodePoolAutoConfigOut": "_container_293_NodePoolAutoConfigOut",
        "DefaultSnatStatusIn": "_container_294_DefaultSnatStatusIn",
        "DefaultSnatStatusOut": "_container_295_DefaultSnatStatusOut",
        "UpdateMasterRequestIn": "_container_296_UpdateMasterRequestIn",
        "UpdateMasterRequestOut": "_container_297_UpdateMasterRequestOut",
        "LinuxNodeConfigIn": "_container_298_LinuxNodeConfigIn",
        "LinuxNodeConfigOut": "_container_299_LinuxNodeConfigOut",
        "NodePoolIn": "_container_300_NodePoolIn",
        "NodePoolOut": "_container_301_NodePoolOut",
        "NodePoolDefaultsIn": "_container_302_NodePoolDefaultsIn",
        "NodePoolDefaultsOut": "_container_303_NodePoolDefaultsOut",
        "AutoprovisioningNodePoolDefaultsIn": "_container_304_AutoprovisioningNodePoolDefaultsIn",
        "AutoprovisioningNodePoolDefaultsOut": "_container_305_AutoprovisioningNodePoolDefaultsOut",
        "ClientCertificateConfigIn": "_container_306_ClientCertificateConfigIn",
        "ClientCertificateConfigOut": "_container_307_ClientCertificateConfigOut",
        "PrivateClusterMasterGlobalAccessConfigIn": "_container_308_PrivateClusterMasterGlobalAccessConfigIn",
        "PrivateClusterMasterGlobalAccessConfigOut": "_container_309_PrivateClusterMasterGlobalAccessConfigOut",
        "GcfsConfigIn": "_container_310_GcfsConfigIn",
        "GcfsConfigOut": "_container_311_GcfsConfigOut",
        "ClusterIn": "_container_312_ClusterIn",
        "ClusterOut": "_container_313_ClusterOut",
        "NotificationConfigIn": "_container_314_NotificationConfigIn",
        "NotificationConfigOut": "_container_315_NotificationConfigOut",
        "FilterIn": "_container_316_FilterIn",
        "FilterOut": "_container_317_FilterOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["VirtualNICIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["VirtualNICIn"]
    )
    types["VirtualNICOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualNICOut"])
    types["SandboxConfigIn"] = t.struct({"type": t.string().optional()}).named(
        renames["SandboxConfigIn"]
    )
    types["SandboxConfigOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SandboxConfigOut"])
    types["GetJSONWebKeysResponseIn"] = t.struct(
        {
            "cacheHeader": t.proxy(
                renames["HttpCacheControlResponseHeaderIn"]
            ).optional(),
            "keys": t.array(t.proxy(renames["JwkIn"])).optional(),
        }
    ).named(renames["GetJSONWebKeysResponseIn"])
    types["GetJSONWebKeysResponseOut"] = t.struct(
        {
            "cacheHeader": t.proxy(
                renames["HttpCacheControlResponseHeaderOut"]
            ).optional(),
            "keys": t.array(t.proxy(renames["JwkOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetJSONWebKeysResponseOut"])
    types["WorkloadPolicyConfigIn"] = t.struct(
        {"allowNetAdmin": t.boolean().optional()}
    ).named(renames["WorkloadPolicyConfigIn"])
    types["WorkloadPolicyConfigOut"] = t.struct(
        {
            "allowNetAdmin": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkloadPolicyConfigOut"])
    types["SecurityPostureConfigIn"] = t.struct(
        {"vulnerabilityMode": t.string().optional(), "mode": t.string().optional()}
    ).named(renames["SecurityPostureConfigIn"])
    types["SecurityPostureConfigOut"] = t.struct(
        {
            "vulnerabilityMode": t.string().optional(),
            "mode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecurityPostureConfigOut"])
    types["AutopilotIn"] = t.struct(
        {
            "workloadPolicyConfig": t.proxy(
                renames["WorkloadPolicyConfigIn"]
            ).optional(),
            "enabled": t.boolean().optional(),
        }
    ).named(renames["AutopilotIn"])
    types["AutopilotOut"] = t.struct(
        {
            "workloadPolicyConfig": t.proxy(
                renames["WorkloadPolicyConfigOut"]
            ).optional(),
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutopilotOut"])
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
    types["HttpLoadBalancingIn"] = t.struct({"disabled": t.boolean().optional()}).named(
        renames["HttpLoadBalancingIn"]
    )
    types["HttpLoadBalancingOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpLoadBalancingOut"])
    types["NodeNetworkConfigIn"] = t.struct(
        {
            "podIpv4CidrBlock": t.string().optional(),
            "enablePrivateNodes": t.boolean().optional(),
            "createPodRange": t.boolean().optional(),
            "podRange": t.string().optional(),
            "networkPerformanceConfig": t.proxy(
                renames["NetworkPerformanceConfigIn"]
            ).optional(),
            "podCidrOverprovisionConfig": t.proxy(
                renames["PodCIDROverprovisionConfigIn"]
            ).optional(),
        }
    ).named(renames["NodeNetworkConfigIn"])
    types["NodeNetworkConfigOut"] = t.struct(
        {
            "podIpv4CidrBlock": t.string().optional(),
            "enablePrivateNodes": t.boolean().optional(),
            "podIpv4RangeUtilization": t.number().optional(),
            "createPodRange": t.boolean().optional(),
            "podRange": t.string().optional(),
            "networkPerformanceConfig": t.proxy(
                renames["NetworkPerformanceConfigOut"]
            ).optional(),
            "podCidrOverprovisionConfig": t.proxy(
                renames["PodCIDROverprovisionConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeNetworkConfigOut"])
    types["AutopilotCompatibilityIssueIn"] = t.struct(
        {
            "subjects": t.array(t.string()).optional(),
            "constraintType": t.string().optional(),
            "documentationUrl": t.string().optional(),
            "incompatibilityType": t.string().optional(),
            "lastObservation": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["AutopilotCompatibilityIssueIn"])
    types["AutopilotCompatibilityIssueOut"] = t.struct(
        {
            "subjects": t.array(t.string()).optional(),
            "constraintType": t.string().optional(),
            "documentationUrl": t.string().optional(),
            "incompatibilityType": t.string().optional(),
            "lastObservation": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutopilotCompatibilityIssueOut"])
    types["CreateNodePoolRequestIn"] = t.struct(
        {
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "nodePool": t.proxy(renames["NodePoolIn"]),
            "parent": t.string().optional(),
        }
    ).named(renames["CreateNodePoolRequestIn"])
    types["CreateNodePoolRequestOut"] = t.struct(
        {
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "nodePool": t.proxy(renames["NodePoolOut"]),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateNodePoolRequestOut"])
    types["UpgradeSettingsIn"] = t.struct(
        {
            "blueGreenSettings": t.proxy(renames["BlueGreenSettingsIn"]).optional(),
            "strategy": t.string().optional(),
            "maxUnavailable": t.integer().optional(),
            "maxSurge": t.integer().optional(),
        }
    ).named(renames["UpgradeSettingsIn"])
    types["UpgradeSettingsOut"] = t.struct(
        {
            "blueGreenSettings": t.proxy(renames["BlueGreenSettingsOut"]).optional(),
            "strategy": t.string().optional(),
            "maxUnavailable": t.integer().optional(),
            "maxSurge": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeSettingsOut"])
    types["AddonsConfigIn"] = t.struct(
        {
            "gcePersistentDiskCsiDriverConfig": t.proxy(
                renames["GcePersistentDiskCsiDriverConfigIn"]
            ).optional(),
            "gkeBackupAgentConfig": t.proxy(
                renames["GkeBackupAgentConfigIn"]
            ).optional(),
            "kubernetesDashboard": t.proxy(renames["KubernetesDashboardIn"]).optional(),
            "httpLoadBalancing": t.proxy(renames["HttpLoadBalancingIn"]).optional(),
            "networkPolicyConfig": t.proxy(renames["NetworkPolicyConfigIn"]).optional(),
            "dnsCacheConfig": t.proxy(renames["DnsCacheConfigIn"]).optional(),
            "gcsFuseCsiDriverConfig": t.proxy(
                renames["GcsFuseCsiDriverConfigIn"]
            ).optional(),
            "cloudRunConfig": t.proxy(renames["CloudRunConfigIn"]).optional(),
            "horizontalPodAutoscaling": t.proxy(
                renames["HorizontalPodAutoscalingIn"]
            ).optional(),
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
            "gcePersistentDiskCsiDriverConfig": t.proxy(
                renames["GcePersistentDiskCsiDriverConfigOut"]
            ).optional(),
            "gkeBackupAgentConfig": t.proxy(
                renames["GkeBackupAgentConfigOut"]
            ).optional(),
            "kubernetesDashboard": t.proxy(
                renames["KubernetesDashboardOut"]
            ).optional(),
            "httpLoadBalancing": t.proxy(renames["HttpLoadBalancingOut"]).optional(),
            "networkPolicyConfig": t.proxy(
                renames["NetworkPolicyConfigOut"]
            ).optional(),
            "dnsCacheConfig": t.proxy(renames["DnsCacheConfigOut"]).optional(),
            "gcsFuseCsiDriverConfig": t.proxy(
                renames["GcsFuseCsiDriverConfigOut"]
            ).optional(),
            "cloudRunConfig": t.proxy(renames["CloudRunConfigOut"]).optional(),
            "horizontalPodAutoscaling": t.proxy(
                renames["HorizontalPodAutoscalingOut"]
            ).optional(),
            "configConnectorConfig": t.proxy(
                renames["ConfigConnectorConfigOut"]
            ).optional(),
            "gcpFilestoreCsiDriverConfig": t.proxy(
                renames["GcpFilestoreCsiDriverConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddonsConfigOut"])
    types["ShieldedInstanceConfigIn"] = t.struct(
        {
            "enableIntegrityMonitoring": t.boolean().optional(),
            "enableSecureBoot": t.boolean().optional(),
        }
    ).named(renames["ShieldedInstanceConfigIn"])
    types["ShieldedInstanceConfigOut"] = t.struct(
        {
            "enableIntegrityMonitoring": t.boolean().optional(),
            "enableSecureBoot": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShieldedInstanceConfigOut"])
    types["ConfigConnectorConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["ConfigConnectorConfigIn"])
    types["ConfigConnectorConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigConnectorConfigOut"])
    types["WindowsNodeConfigIn"] = t.struct({"osVersion": t.string().optional()}).named(
        renames["WindowsNodeConfigIn"]
    )
    types["WindowsNodeConfigOut"] = t.struct(
        {
            "osVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsNodeConfigOut"])
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
    types["ResourceLabelsIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["ResourceLabelsIn"])
    types["ResourceLabelsOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceLabelsOut"])
    types["AdditionalPodRangesConfigIn"] = t.struct(
        {"podRangeNames": t.array(t.string()).optional()}
    ).named(renames["AdditionalPodRangesConfigIn"])
    types["AdditionalPodRangesConfigOut"] = t.struct(
        {
            "podRangeInfo": t.array(t.proxy(renames["RangeInfoOut"])).optional(),
            "podRangeNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdditionalPodRangesConfigOut"])
    types["NodeKubeletConfigIn"] = t.struct(
        {
            "podPidsLimit": t.string().optional(),
            "cpuCfsQuota": t.boolean().optional(),
            "cpuCfsQuotaPeriod": t.string().optional(),
            "cpuManagerPolicy": t.string().optional(),
            "insecureKubeletReadonlyPortEnabled": t.boolean().optional(),
        }
    ).named(renames["NodeKubeletConfigIn"])
    types["NodeKubeletConfigOut"] = t.struct(
        {
            "podPidsLimit": t.string().optional(),
            "cpuCfsQuota": t.boolean().optional(),
            "cpuCfsQuotaPeriod": t.string().optional(),
            "cpuManagerPolicy": t.string().optional(),
            "insecureKubeletReadonlyPortEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeKubeletConfigOut"])
    types["LegacyAbacIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["LegacyAbacIn"]
    )
    types["LegacyAbacOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LegacyAbacOut"])
    types["RangeInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RangeInfoIn"]
    )
    types["RangeInfoOut"] = t.struct(
        {
            "utilization": t.number().optional(),
            "rangeName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RangeInfoOut"])
    types["JwkIn"] = t.struct(
        {
            "use": t.string().optional(),
            "e": t.string().optional(),
            "y": t.string().optional(),
            "x": t.string().optional(),
            "alg": t.string().optional(),
            "kid": t.string().optional(),
            "n": t.string().optional(),
            "kty": t.string().optional(),
            "crv": t.string().optional(),
        }
    ).named(renames["JwkIn"])
    types["JwkOut"] = t.struct(
        {
            "use": t.string().optional(),
            "e": t.string().optional(),
            "y": t.string().optional(),
            "x": t.string().optional(),
            "alg": t.string().optional(),
            "kid": t.string().optional(),
            "n": t.string().optional(),
            "kty": t.string().optional(),
            "crv": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwkOut"])
    types["ServiceExternalIPsConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["ServiceExternalIPsConfigIn"])
    types["ServiceExternalIPsConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceExternalIPsConfigOut"])
    types["HorizontalPodAutoscalingIn"] = t.struct(
        {"disabled": t.boolean().optional()}
    ).named(renames["HorizontalPodAutoscalingIn"])
    types["HorizontalPodAutoscalingOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HorizontalPodAutoscalingOut"])
    types["MonitoringComponentConfigIn"] = t.struct(
        {"enableComponents": t.array(t.string()).optional()}
    ).named(renames["MonitoringComponentConfigIn"])
    types["MonitoringComponentConfigOut"] = t.struct(
        {
            "enableComponents": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoringComponentConfigOut"])
    types["SetAddonsConfigRequestIn"] = t.struct(
        {
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "addonsConfig": t.proxy(renames["AddonsConfigIn"]),
        }
    ).named(renames["SetAddonsConfigRequestIn"])
    types["SetAddonsConfigRequestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "addonsConfig": t.proxy(renames["AddonsConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetAddonsConfigRequestOut"])
    types["HttpCacheControlResponseHeaderIn"] = t.struct(
        {
            "directive": t.string().optional(),
            "age": t.string().optional(),
            "expires": t.string().optional(),
        }
    ).named(renames["HttpCacheControlResponseHeaderIn"])
    types["HttpCacheControlResponseHeaderOut"] = t.struct(
        {
            "directive": t.string().optional(),
            "age": t.string().optional(),
            "expires": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpCacheControlResponseHeaderOut"])
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
    types["MeshCertificatesIn"] = t.struct(
        {"enableCertificates": t.boolean().optional()}
    ).named(renames["MeshCertificatesIn"])
    types["MeshCertificatesOut"] = t.struct(
        {
            "enableCertificates": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MeshCertificatesOut"])
    types["SetMasterAuthRequestIn"] = t.struct(
        {
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "action": t.string(),
            "update": t.proxy(renames["MasterAuthIn"]),
        }
    ).named(renames["SetMasterAuthRequestIn"])
    types["SetMasterAuthRequestOut"] = t.struct(
        {
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "action": t.string(),
            "update": t.proxy(renames["MasterAuthOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetMasterAuthRequestOut"])
    types["ServerConfigIn"] = t.struct(
        {
            "validMasterVersions": t.array(t.string()).optional(),
            "validImageTypes": t.array(t.string()).optional(),
            "validNodeVersions": t.array(t.string()).optional(),
            "channels": t.array(t.proxy(renames["ReleaseChannelConfigIn"])).optional(),
            "defaultClusterVersion": t.string().optional(),
            "defaultImageType": t.string().optional(),
        }
    ).named(renames["ServerConfigIn"])
    types["ServerConfigOut"] = t.struct(
        {
            "validMasterVersions": t.array(t.string()).optional(),
            "validImageTypes": t.array(t.string()).optional(),
            "validNodeVersions": t.array(t.string()).optional(),
            "channels": t.array(t.proxy(renames["ReleaseChannelConfigOut"])).optional(),
            "defaultClusterVersion": t.string().optional(),
            "defaultImageType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServerConfigOut"])
    types["AdvancedMachineFeaturesIn"] = t.struct(
        {"threadsPerCore": t.string().optional()}
    ).named(renames["AdvancedMachineFeaturesIn"])
    types["AdvancedMachineFeaturesOut"] = t.struct(
        {
            "threadsPerCore": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvancedMachineFeaturesOut"])
    types["VerticalPodAutoscalingIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["VerticalPodAutoscalingIn"])
    types["VerticalPodAutoscalingOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerticalPodAutoscalingOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["DnsCacheConfigIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["DnsCacheConfigIn"]
    )
    types["DnsCacheConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsCacheConfigOut"])
    types["EphemeralStorageLocalSsdConfigIn"] = t.struct(
        {"localSsdCount": t.integer().optional()}
    ).named(renames["EphemeralStorageLocalSsdConfigIn"])
    types["EphemeralStorageLocalSsdConfigOut"] = t.struct(
        {
            "localSsdCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EphemeralStorageLocalSsdConfigOut"])
    types["MaintenanceWindowIn"] = t.struct(
        {
            "recurringWindow": t.proxy(renames["RecurringTimeWindowIn"]).optional(),
            "maintenanceExclusions": t.struct({"_": t.string().optional()}).optional(),
            "dailyMaintenanceWindow": t.proxy(
                renames["DailyMaintenanceWindowIn"]
            ).optional(),
        }
    ).named(renames["MaintenanceWindowIn"])
    types["MaintenanceWindowOut"] = t.struct(
        {
            "recurringWindow": t.proxy(renames["RecurringTimeWindowOut"]).optional(),
            "maintenanceExclusions": t.struct({"_": t.string().optional()}).optional(),
            "dailyMaintenanceWindow": t.proxy(
                renames["DailyMaintenanceWindowOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceWindowOut"])
    types["NetworkPerformanceConfigIn"] = t.struct(
        {"totalEgressBandwidthTier": t.string().optional()}
    ).named(renames["NetworkPerformanceConfigIn"])
    types["NetworkPerformanceConfigOut"] = t.struct(
        {
            "totalEgressBandwidthTier": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkPerformanceConfigOut"])
    types["CostManagementConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["CostManagementConfigIn"])
    types["CostManagementConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CostManagementConfigOut"])
    types["NodeConfigIn"] = t.struct(
        {
            "tags": t.array(t.string()).optional(),
            "windowsNodeConfig": t.proxy(renames["WindowsNodeConfigIn"]).optional(),
            "serviceAccount": t.string().optional(),
            "localNvmeSsdBlockConfig": t.proxy(
                renames["LocalNvmeSsdBlockConfigIn"]
            ).optional(),
            "workloadMetadataConfig": t.proxy(
                renames["WorkloadMetadataConfigIn"]
            ).optional(),
            "resourceLabels": t.struct({"_": t.string().optional()}).optional(),
            "sandboxConfig": t.proxy(renames["SandboxConfigIn"]).optional(),
            "preemptible": t.boolean().optional(),
            "machineType": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "gcfsConfig": t.proxy(renames["GcfsConfigIn"]).optional(),
            "advancedMachineFeatures": t.proxy(
                renames["AdvancedMachineFeaturesIn"]
            ).optional(),
            "nodeGroup": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "localSsdCount": t.integer().optional(),
            "reservationAffinity": t.proxy(renames["ReservationAffinityIn"]).optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "minCpuPlatform": t.string().optional(),
            "fastSocket": t.proxy(renames["FastSocketIn"]).optional(),
            "gvnic": t.proxy(renames["VirtualNICIn"]).optional(),
            "taints": t.array(t.proxy(renames["NodeTaintIn"])).optional(),
            "confidentialNodes": t.proxy(renames["ConfidentialNodesIn"]).optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorConfigIn"])).optional(),
            "diskSizeGb": t.integer().optional(),
            "imageType": t.string().optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigIn"]
            ).optional(),
            "ephemeralStorageLocalSsdConfig": t.proxy(
                renames["EphemeralStorageLocalSsdConfigIn"]
            ).optional(),
            "spot": t.boolean().optional(),
            "soleTenantConfig": t.proxy(renames["SoleTenantConfigIn"]).optional(),
            "loggingConfig": t.proxy(renames["NodePoolLoggingConfigIn"]).optional(),
            "bootDiskKmsKey": t.string().optional(),
            "diskType": t.string().optional(),
            "linuxNodeConfig": t.proxy(renames["LinuxNodeConfigIn"]).optional(),
            "kubeletConfig": t.proxy(renames["NodeKubeletConfigIn"]).optional(),
        }
    ).named(renames["NodeConfigIn"])
    types["NodeConfigOut"] = t.struct(
        {
            "tags": t.array(t.string()).optional(),
            "windowsNodeConfig": t.proxy(renames["WindowsNodeConfigOut"]).optional(),
            "serviceAccount": t.string().optional(),
            "localNvmeSsdBlockConfig": t.proxy(
                renames["LocalNvmeSsdBlockConfigOut"]
            ).optional(),
            "workloadMetadataConfig": t.proxy(
                renames["WorkloadMetadataConfigOut"]
            ).optional(),
            "resourceLabels": t.struct({"_": t.string().optional()}).optional(),
            "sandboxConfig": t.proxy(renames["SandboxConfigOut"]).optional(),
            "preemptible": t.boolean().optional(),
            "machineType": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "gcfsConfig": t.proxy(renames["GcfsConfigOut"]).optional(),
            "advancedMachineFeatures": t.proxy(
                renames["AdvancedMachineFeaturesOut"]
            ).optional(),
            "nodeGroup": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "localSsdCount": t.integer().optional(),
            "reservationAffinity": t.proxy(
                renames["ReservationAffinityOut"]
            ).optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "minCpuPlatform": t.string().optional(),
            "fastSocket": t.proxy(renames["FastSocketOut"]).optional(),
            "gvnic": t.proxy(renames["VirtualNICOut"]).optional(),
            "taints": t.array(t.proxy(renames["NodeTaintOut"])).optional(),
            "confidentialNodes": t.proxy(renames["ConfidentialNodesOut"]).optional(),
            "accelerators": t.array(
                t.proxy(renames["AcceleratorConfigOut"])
            ).optional(),
            "diskSizeGb": t.integer().optional(),
            "imageType": t.string().optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigOut"]
            ).optional(),
            "ephemeralStorageLocalSsdConfig": t.proxy(
                renames["EphemeralStorageLocalSsdConfigOut"]
            ).optional(),
            "spot": t.boolean().optional(),
            "soleTenantConfig": t.proxy(renames["SoleTenantConfigOut"]).optional(),
            "loggingConfig": t.proxy(renames["NodePoolLoggingConfigOut"]).optional(),
            "bootDiskKmsKey": t.string().optional(),
            "diskType": t.string().optional(),
            "linuxNodeConfig": t.proxy(renames["LinuxNodeConfigOut"]).optional(),
            "kubeletConfig": t.proxy(renames["NodeKubeletConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeConfigOut"])
    types["ILBSubsettingConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["ILBSubsettingConfigIn"])
    types["ILBSubsettingConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ILBSubsettingConfigOut"])
    types["NodeManagementIn"] = t.struct(
        {
            "upgradeOptions": t.proxy(renames["AutoUpgradeOptionsIn"]).optional(),
            "autoUpgrade": t.boolean().optional(),
            "autoRepair": t.boolean().optional(),
        }
    ).named(renames["NodeManagementIn"])
    types["NodeManagementOut"] = t.struct(
        {
            "upgradeOptions": t.proxy(renames["AutoUpgradeOptionsOut"]).optional(),
            "autoUpgrade": t.boolean().optional(),
            "autoRepair": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeManagementOut"])
    types["NodePoolLoggingConfigIn"] = t.struct(
        {"variantConfig": t.proxy(renames["LoggingVariantConfigIn"]).optional()}
    ).named(renames["NodePoolLoggingConfigIn"])
    types["NodePoolLoggingConfigOut"] = t.struct(
        {
            "variantConfig": t.proxy(renames["LoggingVariantConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodePoolLoggingConfigOut"])
    types["LoggingComponentConfigIn"] = t.struct(
        {"enableComponents": t.array(t.string()).optional()}
    ).named(renames["LoggingComponentConfigIn"])
    types["LoggingComponentConfigOut"] = t.struct(
        {
            "enableComponents": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoggingComponentConfigOut"])
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
    types["BigQueryDestinationIn"] = t.struct(
        {"datasetId": t.string().optional()}
    ).named(renames["BigQueryDestinationIn"])
    types["BigQueryDestinationOut"] = t.struct(
        {
            "datasetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryDestinationOut"])
    types["RollbackNodePoolUpgradeRequestIn"] = t.struct(
        {
            "clusterId": t.string().optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "respectPdb": t.boolean().optional(),
            "nodePoolId": t.string().optional(),
            "zone": t.string().optional(),
        }
    ).named(renames["RollbackNodePoolUpgradeRequestIn"])
    types["RollbackNodePoolUpgradeRequestOut"] = t.struct(
        {
            "clusterId": t.string().optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "respectPdb": t.boolean().optional(),
            "nodePoolId": t.string().optional(),
            "zone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RollbackNodePoolUpgradeRequestOut"])
    types["FastSocketIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["FastSocketIn"]
    )
    types["FastSocketOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FastSocketOut"])
    types["MaxPodsConstraintIn"] = t.struct(
        {"maxPodsPerNode": t.string().optional()}
    ).named(renames["MaxPodsConstraintIn"])
    types["MaxPodsConstraintOut"] = t.struct(
        {
            "maxPodsPerNode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaxPodsConstraintOut"])
    types["ClusterAutoscalingIn"] = t.struct(
        {
            "enableNodeAutoprovisioning": t.boolean().optional(),
            "autoprovisioningLocations": t.array(t.string()).optional(),
            "autoscalingProfile": t.string().optional(),
            "resourceLimits": t.array(t.proxy(renames["ResourceLimitIn"])).optional(),
            "autoprovisioningNodePoolDefaults": t.proxy(
                renames["AutoprovisioningNodePoolDefaultsIn"]
            ).optional(),
        }
    ).named(renames["ClusterAutoscalingIn"])
    types["ClusterAutoscalingOut"] = t.struct(
        {
            "enableNodeAutoprovisioning": t.boolean().optional(),
            "autoprovisioningLocations": t.array(t.string()).optional(),
            "autoscalingProfile": t.string().optional(),
            "resourceLimits": t.array(t.proxy(renames["ResourceLimitOut"])).optional(),
            "autoprovisioningNodePoolDefaults": t.proxy(
                renames["AutoprovisioningNodePoolDefaultsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterAutoscalingOut"])
    types["CreateClusterRequestIn"] = t.struct(
        {
            "cluster": t.proxy(renames["ClusterIn"]),
            "zone": t.string().optional(),
            "parent": t.string().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["CreateClusterRequestIn"])
    types["CreateClusterRequestOut"] = t.struct(
        {
            "cluster": t.proxy(renames["ClusterOut"]),
            "zone": t.string().optional(),
            "parent": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateClusterRequestOut"])
    types["GcpFilestoreCsiDriverConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["GcpFilestoreCsiDriverConfigIn"])
    types["GcpFilestoreCsiDriverConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcpFilestoreCsiDriverConfigOut"])
    types["SetNetworkPolicyRequestIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "networkPolicy": t.proxy(renames["NetworkPolicyIn"]),
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
        }
    ).named(renames["SetNetworkPolicyRequestIn"])
    types["SetNetworkPolicyRequestOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "networkPolicy": t.proxy(renames["NetworkPolicyOut"]),
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetNetworkPolicyRequestOut"])
    types["NetworkPolicyConfigIn"] = t.struct(
        {"disabled": t.boolean().optional()}
    ).named(renames["NetworkPolicyConfigIn"])
    types["NetworkPolicyConfigOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkPolicyConfigOut"])
    types["CheckAutopilotCompatibilityResponseIn"] = t.struct(
        {
            "issues": t.array(
                t.proxy(renames["AutopilotCompatibilityIssueIn"])
            ).optional(),
            "summary": t.string().optional(),
        }
    ).named(renames["CheckAutopilotCompatibilityResponseIn"])
    types["CheckAutopilotCompatibilityResponseOut"] = t.struct(
        {
            "issues": t.array(
                t.proxy(renames["AutopilotCompatibilityIssueOut"])
            ).optional(),
            "summary": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckAutopilotCompatibilityResponseOut"])
    types["UsableSubnetworkIn"] = t.struct(
        {
            "subnetwork": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "secondaryIpRanges": t.array(
                t.proxy(renames["UsableSubnetworkSecondaryRangeIn"])
            ).optional(),
            "network": t.string().optional(),
            "statusMessage": t.string().optional(),
        }
    ).named(renames["UsableSubnetworkIn"])
    types["UsableSubnetworkOut"] = t.struct(
        {
            "subnetwork": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "secondaryIpRanges": t.array(
                t.proxy(renames["UsableSubnetworkSecondaryRangeOut"])
            ).optional(),
            "network": t.string().optional(),
            "statusMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsableSubnetworkOut"])
    types["GetOpenIDConfigResponseIn"] = t.struct(
        {
            "claims_supported": t.array(t.string()).optional(),
            "jwks_uri": t.string().optional(),
            "id_token_signing_alg_values_supported": t.array(t.string()).optional(),
            "cacheHeader": t.proxy(
                renames["HttpCacheControlResponseHeaderIn"]
            ).optional(),
            "issuer": t.string().optional(),
            "grant_types": t.array(t.string()).optional(),
            "response_types_supported": t.array(t.string()).optional(),
            "subject_types_supported": t.array(t.string()).optional(),
        }
    ).named(renames["GetOpenIDConfigResponseIn"])
    types["GetOpenIDConfigResponseOut"] = t.struct(
        {
            "claims_supported": t.array(t.string()).optional(),
            "jwks_uri": t.string().optional(),
            "id_token_signing_alg_values_supported": t.array(t.string()).optional(),
            "cacheHeader": t.proxy(
                renames["HttpCacheControlResponseHeaderOut"]
            ).optional(),
            "issuer": t.string().optional(),
            "grant_types": t.array(t.string()).optional(),
            "response_types_supported": t.array(t.string()).optional(),
            "subject_types_supported": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetOpenIDConfigResponseOut"])
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
    types["FleetIn"] = t.struct(
        {
            "membership": t.string().optional(),
            "project": t.string().optional(),
            "preRegistered": t.boolean().optional(),
        }
    ).named(renames["FleetIn"])
    types["FleetOut"] = t.struct(
        {
            "membership": t.string().optional(),
            "project": t.string().optional(),
            "preRegistered": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FleetOut"])
    types["OperationProgressIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "status": t.string().optional(),
            "stages": t.array(t.proxy(renames["OperationProgressIn"])).optional(),
        }
    ).named(renames["OperationProgressIn"])
    types["OperationProgressOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "status": t.string().optional(),
            "stages": t.array(t.proxy(renames["OperationProgressOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationProgressOut"])
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
    types["SetNodePoolSizeRequestIn"] = t.struct(
        {
            "nodePoolId": t.string().optional(),
            "nodeCount": t.integer(),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "clusterId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SetNodePoolSizeRequestIn"])
    types["SetNodePoolSizeRequestOut"] = t.struct(
        {
            "nodePoolId": t.string().optional(),
            "nodeCount": t.integer(),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "clusterId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetNodePoolSizeRequestOut"])
    types["CancelOperationRequestIn"] = t.struct(
        {
            "zone": t.string().optional(),
            "operationId": t.string().optional(),
            "projectId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["CancelOperationRequestIn"])
    types["CancelOperationRequestOut"] = t.struct(
        {
            "zone": t.string().optional(),
            "operationId": t.string().optional(),
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CancelOperationRequestOut"])
    types["SetMonitoringServiceRequestIn"] = t.struct(
        {
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
            "projectId": t.string().optional(),
            "monitoringService": t.string(),
            "name": t.string().optional(),
        }
    ).named(renames["SetMonitoringServiceRequestIn"])
    types["SetMonitoringServiceRequestOut"] = t.struct(
        {
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
            "projectId": t.string().optional(),
            "monitoringService": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetMonitoringServiceRequestOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["WorkloadIdentityConfigIn"] = t.struct(
        {"workloadPool": t.string().optional()}
    ).named(renames["WorkloadIdentityConfigIn"])
    types["WorkloadIdentityConfigOut"] = t.struct(
        {
            "workloadPool": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkloadIdentityConfigOut"])
    types["NodeTaintsIn"] = t.struct(
        {"taints": t.array(t.proxy(renames["NodeTaintIn"])).optional()}
    ).named(renames["NodeTaintsIn"])
    types["NodeTaintsOut"] = t.struct(
        {
            "taints": t.array(t.proxy(renames["NodeTaintOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeTaintsOut"])
    types["WorkloadMetadataConfigIn"] = t.struct({"mode": t.string().optional()}).named(
        renames["WorkloadMetadataConfigIn"]
    )
    types["WorkloadMetadataConfigOut"] = t.struct(
        {
            "mode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkloadMetadataConfigOut"])
    types["ResourceLimitIn"] = t.struct(
        {
            "maximum": t.string().optional(),
            "resourceType": t.string().optional(),
            "minimum": t.string().optional(),
        }
    ).named(renames["ResourceLimitIn"])
    types["ResourceLimitOut"] = t.struct(
        {
            "maximum": t.string().optional(),
            "resourceType": t.string().optional(),
            "minimum": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceLimitOut"])
    types["AutoUpgradeOptionsIn"] = t.struct(
        {
            "description": t.string().optional(),
            "autoUpgradeStartTime": t.string().optional(),
        }
    ).named(renames["AutoUpgradeOptionsIn"])
    types["AutoUpgradeOptionsOut"] = t.struct(
        {
            "description": t.string().optional(),
            "autoUpgradeStartTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoUpgradeOptionsOut"])
    types["LoggingVariantConfigIn"] = t.struct(
        {"variant": t.string().optional()}
    ).named(renames["LoggingVariantConfigIn"])
    types["LoggingVariantConfigOut"] = t.struct(
        {
            "variant": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoggingVariantConfigOut"])
    types["ReleaseChannelIn"] = t.struct({"channel": t.string().optional()}).named(
        renames["ReleaseChannelIn"]
    )
    types["ReleaseChannelOut"] = t.struct(
        {
            "channel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseChannelOut"])
    types["GkeBackupAgentConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["GkeBackupAgentConfigIn"])
    types["GkeBackupAgentConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeBackupAgentConfigOut"])
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
    types["BlueGreenInfoIn"] = t.struct(
        {
            "greenInstanceGroupUrls": t.array(t.string()).optional(),
            "phase": t.string().optional(),
            "bluePoolDeletionStartTime": t.string().optional(),
            "blueInstanceGroupUrls": t.array(t.string()).optional(),
            "greenPoolVersion": t.string().optional(),
        }
    ).named(renames["BlueGreenInfoIn"])
    types["BlueGreenInfoOut"] = t.struct(
        {
            "greenInstanceGroupUrls": t.array(t.string()).optional(),
            "phase": t.string().optional(),
            "bluePoolDeletionStartTime": t.string().optional(),
            "blueInstanceGroupUrls": t.array(t.string()).optional(),
            "greenPoolVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BlueGreenInfoOut"])
    types["PlacementPolicyIn"] = t.struct({"type": t.string().optional()}).named(
        renames["PlacementPolicyIn"]
    )
    types["PlacementPolicyOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacementPolicyOut"])
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
    types["ClusterNetworkPerformanceConfigIn"] = t.struct(
        {"totalEgressBandwidthTier": t.string().optional()}
    ).named(renames["ClusterNetworkPerformanceConfigIn"])
    types["ClusterNetworkPerformanceConfigOut"] = t.struct(
        {
            "totalEgressBandwidthTier": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterNetworkPerformanceConfigOut"])
    types["K8sBetaAPIConfigIn"] = t.struct(
        {"enabledApis": t.array(t.string()).optional()}
    ).named(renames["K8sBetaAPIConfigIn"])
    types["K8sBetaAPIConfigOut"] = t.struct(
        {
            "enabledApis": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["K8sBetaAPIConfigOut"])
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
    types["SetLabelsRequestIn"] = t.struct(
        {
            "name": t.string().optional(),
            "resourceLabels": t.struct({"_": t.string().optional()}),
            "clusterId": t.string().optional(),
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
            "labelFingerprint": t.string(),
        }
    ).named(renames["SetLabelsRequestIn"])
    types["SetLabelsRequestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "resourceLabels": t.struct({"_": t.string().optional()}),
            "clusterId": t.string().optional(),
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
            "labelFingerprint": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetLabelsRequestOut"])
    types["UpdateClusterRequestIn"] = t.struct(
        {
            "name": t.string().optional(),
            "zone": t.string().optional(),
            "update": t.proxy(renames["ClusterUpdateIn"]),
            "projectId": t.string().optional(),
            "clusterId": t.string().optional(),
        }
    ).named(renames["UpdateClusterRequestIn"])
    types["UpdateClusterRequestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "zone": t.string().optional(),
            "update": t.proxy(renames["ClusterUpdateOut"]),
            "projectId": t.string().optional(),
            "clusterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateClusterRequestOut"])
    types["ListClustersResponseIn"] = t.struct(
        {
            "missingZones": t.array(t.string()).optional(),
            "clusters": t.array(t.proxy(renames["ClusterIn"])).optional(),
        }
    ).named(renames["ListClustersResponseIn"])
    types["ListClustersResponseOut"] = t.struct(
        {
            "missingZones": t.array(t.string()).optional(),
            "clusters": t.array(t.proxy(renames["ClusterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListClustersResponseOut"])
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
    types["LoggingConfigIn"] = t.struct(
        {"componentConfig": t.proxy(renames["LoggingComponentConfigIn"]).optional()}
    ).named(renames["LoggingConfigIn"])
    types["LoggingConfigOut"] = t.struct(
        {
            "componentConfig": t.proxy(renames["LoggingComponentConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoggingConfigOut"])
    types["SetLoggingServiceRequestIn"] = t.struct(
        {
            "zone": t.string().optional(),
            "loggingService": t.string(),
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
        }
    ).named(renames["SetLoggingServiceRequestIn"])
    types["SetLoggingServiceRequestOut"] = t.struct(
        {
            "zone": t.string().optional(),
            "loggingService": t.string(),
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetLoggingServiceRequestOut"])
    types["IPAllocationPolicyIn"] = t.struct(
        {
            "clusterIpv4Cidr": t.string().optional(),
            "clusterSecondaryRangeName": t.string().optional(),
            "stackType": t.string().optional(),
            "subnetworkName": t.string().optional(),
            "createSubnetwork": t.boolean().optional(),
            "nodeIpv4CidrBlock": t.string().optional(),
            "podCidrOverprovisionConfig": t.proxy(
                renames["PodCIDROverprovisionConfigIn"]
            ).optional(),
            "useIpAliases": t.boolean().optional(),
            "servicesIpv4Cidr": t.string().optional(),
            "servicesSecondaryRangeName": t.string().optional(),
            "servicesIpv4CidrBlock": t.string().optional(),
            "tpuIpv4CidrBlock": t.string().optional(),
            "useRoutes": t.boolean().optional(),
            "clusterIpv4CidrBlock": t.string().optional(),
            "nodeIpv4Cidr": t.string().optional(),
            "ipv6AccessType": t.string().optional(),
        }
    ).named(renames["IPAllocationPolicyIn"])
    types["IPAllocationPolicyOut"] = t.struct(
        {
            "clusterIpv4Cidr": t.string().optional(),
            "clusterSecondaryRangeName": t.string().optional(),
            "stackType": t.string().optional(),
            "additionalPodRangesConfig": t.proxy(
                renames["AdditionalPodRangesConfigOut"]
            ).optional(),
            "subnetworkName": t.string().optional(),
            "createSubnetwork": t.boolean().optional(),
            "servicesIpv6CidrBlock": t.string().optional(),
            "defaultPodIpv4RangeUtilization": t.number().optional(),
            "nodeIpv4CidrBlock": t.string().optional(),
            "podCidrOverprovisionConfig": t.proxy(
                renames["PodCIDROverprovisionConfigOut"]
            ).optional(),
            "useIpAliases": t.boolean().optional(),
            "servicesIpv4Cidr": t.string().optional(),
            "servicesSecondaryRangeName": t.string().optional(),
            "subnetIpv6CidrBlock": t.string().optional(),
            "servicesIpv4CidrBlock": t.string().optional(),
            "tpuIpv4CidrBlock": t.string().optional(),
            "useRoutes": t.boolean().optional(),
            "clusterIpv4CidrBlock": t.string().optional(),
            "nodeIpv4Cidr": t.string().optional(),
            "ipv6AccessType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IPAllocationPolicyOut"])
    types["UsableSubnetworkSecondaryRangeIn"] = t.struct(
        {
            "status": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "rangeName": t.string().optional(),
        }
    ).named(renames["UsableSubnetworkSecondaryRangeIn"])
    types["UsableSubnetworkSecondaryRangeOut"] = t.struct(
        {
            "status": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "rangeName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsableSubnetworkSecondaryRangeOut"])
    types["NetworkConfigIn"] = t.struct(
        {
            "network": t.string().optional(),
            "privateIpv6GoogleAccess": t.string().optional(),
            "subnetwork": t.string().optional(),
            "enableFqdnNetworkPolicy": t.boolean().optional(),
            "dnsConfig": t.proxy(renames["DNSConfigIn"]).optional(),
            "gatewayApiConfig": t.proxy(renames["GatewayAPIConfigIn"]).optional(),
            "defaultSnatStatus": t.proxy(renames["DefaultSnatStatusIn"]).optional(),
            "serviceExternalIpsConfig": t.proxy(
                renames["ServiceExternalIPsConfigIn"]
            ).optional(),
            "enableIntraNodeVisibility": t.boolean().optional(),
            "networkPerformanceConfig": t.proxy(
                renames["ClusterNetworkPerformanceConfigIn"]
            ).optional(),
            "enableL4ilbSubsetting": t.boolean().optional(),
            "datapathProvider": t.string().optional(),
        }
    ).named(renames["NetworkConfigIn"])
    types["NetworkConfigOut"] = t.struct(
        {
            "network": t.string().optional(),
            "privateIpv6GoogleAccess": t.string().optional(),
            "subnetwork": t.string().optional(),
            "enableFqdnNetworkPolicy": t.boolean().optional(),
            "dnsConfig": t.proxy(renames["DNSConfigOut"]).optional(),
            "gatewayApiConfig": t.proxy(renames["GatewayAPIConfigOut"]).optional(),
            "defaultSnatStatus": t.proxy(renames["DefaultSnatStatusOut"]).optional(),
            "serviceExternalIpsConfig": t.proxy(
                renames["ServiceExternalIPsConfigOut"]
            ).optional(),
            "enableIntraNodeVisibility": t.boolean().optional(),
            "networkPerformanceConfig": t.proxy(
                renames["ClusterNetworkPerformanceConfigOut"]
            ).optional(),
            "enableL4ilbSubsetting": t.boolean().optional(),
            "datapathProvider": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConfigOut"])
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
    types["PrivateClusterConfigIn"] = t.struct(
        {
            "privateEndpointSubnetwork": t.string().optional(),
            "enablePrivateNodes": t.boolean().optional(),
            "masterGlobalAccessConfig": t.proxy(
                renames["PrivateClusterMasterGlobalAccessConfigIn"]
            ).optional(),
            "publicEndpoint": t.string().optional(),
            "enablePrivateEndpoint": t.boolean().optional(),
            "peeringName": t.string().optional(),
            "privateEndpoint": t.string().optional(),
            "masterIpv4CidrBlock": t.string().optional(),
        }
    ).named(renames["PrivateClusterConfigIn"])
    types["PrivateClusterConfigOut"] = t.struct(
        {
            "privateEndpointSubnetwork": t.string().optional(),
            "enablePrivateNodes": t.boolean().optional(),
            "masterGlobalAccessConfig": t.proxy(
                renames["PrivateClusterMasterGlobalAccessConfigOut"]
            ).optional(),
            "publicEndpoint": t.string().optional(),
            "enablePrivateEndpoint": t.boolean().optional(),
            "peeringName": t.string().optional(),
            "privateEndpoint": t.string().optional(),
            "masterIpv4CidrBlock": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateClusterConfigOut"])
    types["NodePoolAutoscalingIn"] = t.struct(
        {
            "maxNodeCount": t.integer().optional(),
            "minNodeCount": t.integer().optional(),
            "locationPolicy": t.string().optional(),
            "totalMinNodeCount": t.integer().optional(),
            "totalMaxNodeCount": t.integer().optional(),
            "autoprovisioned": t.boolean().optional(),
            "enabled": t.boolean().optional(),
        }
    ).named(renames["NodePoolAutoscalingIn"])
    types["NodePoolAutoscalingOut"] = t.struct(
        {
            "maxNodeCount": t.integer().optional(),
            "minNodeCount": t.integer().optional(),
            "locationPolicy": t.string().optional(),
            "totalMinNodeCount": t.integer().optional(),
            "totalMaxNodeCount": t.integer().optional(),
            "autoprovisioned": t.boolean().optional(),
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodePoolAutoscalingOut"])
    types["DNSConfigIn"] = t.struct(
        {
            "clusterDnsDomain": t.string().optional(),
            "clusterDns": t.string().optional(),
            "clusterDnsScope": t.string().optional(),
        }
    ).named(renames["DNSConfigIn"])
    types["DNSConfigOut"] = t.struct(
        {
            "clusterDnsDomain": t.string().optional(),
            "clusterDns": t.string().optional(),
            "clusterDnsScope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DNSConfigOut"])
    types["SetNodePoolManagementRequestIn"] = t.struct(
        {
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "management": t.proxy(renames["NodeManagementIn"]),
            "nodePoolId": t.string().optional(),
        }
    ).named(renames["SetNodePoolManagementRequestIn"])
    types["SetNodePoolManagementRequestOut"] = t.struct(
        {
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "management": t.proxy(renames["NodeManagementOut"]),
            "nodePoolId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetNodePoolManagementRequestOut"])
    types["UpdateInfoIn"] = t.struct(
        {"blueGreenInfo": t.proxy(renames["BlueGreenInfoIn"]).optional()}
    ).named(renames["UpdateInfoIn"])
    types["UpdateInfoOut"] = t.struct(
        {
            "blueGreenInfo": t.proxy(renames["BlueGreenInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateInfoOut"])
    types["SetLegacyAbacRequestIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "enabled": t.boolean(),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SetLegacyAbacRequestIn"])
    types["SetLegacyAbacRequestOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "enabled": t.boolean(),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetLegacyAbacRequestOut"])
    types["IdentityServiceConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["IdentityServiceConfigIn"])
    types["IdentityServiceConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityServiceConfigOut"])
    types["KubernetesDashboardIn"] = t.struct(
        {"disabled": t.boolean().optional()}
    ).named(renames["KubernetesDashboardIn"])
    types["KubernetesDashboardOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KubernetesDashboardOut"])
    types["NodeAffinityIn"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "key": t.string().optional(),
            "operator": t.string().optional(),
        }
    ).named(renames["NodeAffinityIn"])
    types["NodeAffinityOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "key": t.string().optional(),
            "operator": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeAffinityOut"])
    types["MasterAuthIn"] = t.struct(
        {
            "username": t.string().optional(),
            "clientCertificateConfig": t.proxy(
                renames["ClientCertificateConfigIn"]
            ).optional(),
            "clusterCaCertificate": t.string().optional(),
            "clientCertificate": t.string().optional(),
            "password": t.string().optional(),
            "clientKey": t.string().optional(),
        }
    ).named(renames["MasterAuthIn"])
    types["MasterAuthOut"] = t.struct(
        {
            "username": t.string().optional(),
            "clientCertificateConfig": t.proxy(
                renames["ClientCertificateConfigOut"]
            ).optional(),
            "clusterCaCertificate": t.string().optional(),
            "clientCertificate": t.string().optional(),
            "password": t.string().optional(),
            "clientKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MasterAuthOut"])
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
    types["GPUDriverInstallationConfigIn"] = t.struct(
        {"gpuDriverVersion": t.string().optional()}
    ).named(renames["GPUDriverInstallationConfigIn"])
    types["GPUDriverInstallationConfigOut"] = t.struct(
        {
            "gpuDriverVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GPUDriverInstallationConfigOut"])
    types["ListNodePoolsResponseIn"] = t.struct(
        {"nodePools": t.array(t.proxy(renames["NodePoolIn"])).optional()}
    ).named(renames["ListNodePoolsResponseIn"])
    types["ListNodePoolsResponseOut"] = t.struct(
        {
            "nodePools": t.array(t.proxy(renames["NodePoolOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNodePoolsResponseOut"])
    types["SoleTenantConfigIn"] = t.struct(
        {"nodeAffinities": t.array(t.proxy(renames["NodeAffinityIn"])).optional()}
    ).named(renames["SoleTenantConfigIn"])
    types["SoleTenantConfigOut"] = t.struct(
        {
            "nodeAffinities": t.array(t.proxy(renames["NodeAffinityOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SoleTenantConfigOut"])
    types["CompleteNodePoolUpgradeRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CompleteNodePoolUpgradeRequestIn"])
    types["CompleteNodePoolUpgradeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CompleteNodePoolUpgradeRequestOut"])
    types["UpdateNodePoolRequestIn"] = t.struct(
        {
            "name": t.string().optional(),
            "loggingConfig": t.proxy(renames["NodePoolLoggingConfigIn"]).optional(),
            "clusterId": t.string().optional(),
            "linuxNodeConfig": t.proxy(renames["LinuxNodeConfigIn"]).optional(),
            "upgradeSettings": t.proxy(renames["UpgradeSettingsIn"]).optional(),
            "etag": t.string().optional(),
            "kubeletConfig": t.proxy(renames["NodeKubeletConfigIn"]).optional(),
            "resourceLabels": t.proxy(renames["ResourceLabelsIn"]).optional(),
            "confidentialNodes": t.proxy(renames["ConfidentialNodesIn"]).optional(),
            "fastSocket": t.proxy(renames["FastSocketIn"]).optional(),
            "nodeNetworkConfig": t.proxy(renames["NodeNetworkConfigIn"]).optional(),
            "taints": t.proxy(renames["NodeTaintsIn"]).optional(),
            "tags": t.proxy(renames["NetworkTagsIn"]).optional(),
            "nodeVersion": t.string(),
            "nodePoolId": t.string().optional(),
            "gvnic": t.proxy(renames["VirtualNICIn"]).optional(),
            "imageType": t.string(),
            "zone": t.string().optional(),
            "gcfsConfig": t.proxy(renames["GcfsConfigIn"]).optional(),
            "windowsNodeConfig": t.proxy(renames["WindowsNodeConfigIn"]).optional(),
            "locations": t.array(t.string()).optional(),
            "projectId": t.string().optional(),
            "workloadMetadataConfig": t.proxy(
                renames["WorkloadMetadataConfigIn"]
            ).optional(),
            "labels": t.proxy(renames["NodeLabelsIn"]).optional(),
        }
    ).named(renames["UpdateNodePoolRequestIn"])
    types["UpdateNodePoolRequestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "loggingConfig": t.proxy(renames["NodePoolLoggingConfigOut"]).optional(),
            "clusterId": t.string().optional(),
            "linuxNodeConfig": t.proxy(renames["LinuxNodeConfigOut"]).optional(),
            "upgradeSettings": t.proxy(renames["UpgradeSettingsOut"]).optional(),
            "etag": t.string().optional(),
            "kubeletConfig": t.proxy(renames["NodeKubeletConfigOut"]).optional(),
            "resourceLabels": t.proxy(renames["ResourceLabelsOut"]).optional(),
            "confidentialNodes": t.proxy(renames["ConfidentialNodesOut"]).optional(),
            "fastSocket": t.proxy(renames["FastSocketOut"]).optional(),
            "nodeNetworkConfig": t.proxy(renames["NodeNetworkConfigOut"]).optional(),
            "taints": t.proxy(renames["NodeTaintsOut"]).optional(),
            "tags": t.proxy(renames["NetworkTagsOut"]).optional(),
            "nodeVersion": t.string(),
            "nodePoolId": t.string().optional(),
            "gvnic": t.proxy(renames["VirtualNICOut"]).optional(),
            "imageType": t.string(),
            "zone": t.string().optional(),
            "gcfsConfig": t.proxy(renames["GcfsConfigOut"]).optional(),
            "windowsNodeConfig": t.proxy(renames["WindowsNodeConfigOut"]).optional(),
            "locations": t.array(t.string()).optional(),
            "projectId": t.string().optional(),
            "workloadMetadataConfig": t.proxy(
                renames["WorkloadMetadataConfigOut"]
            ).optional(),
            "labels": t.proxy(renames["NodeLabelsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateNodePoolRequestOut"])
    types["NodeTaintIn"] = t.struct(
        {
            "value": t.string().optional(),
            "effect": t.string().optional(),
            "key": t.string().optional(),
        }
    ).named(renames["NodeTaintIn"])
    types["NodeTaintOut"] = t.struct(
        {
            "value": t.string().optional(),
            "effect": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeTaintOut"])
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
    types["ShieldedNodesIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["ShieldedNodesIn"]
    )
    types["ShieldedNodesOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShieldedNodesOut"])
    types["UpgradeAvailableEventIn"] = t.struct(
        {
            "releaseChannel": t.proxy(renames["ReleaseChannelIn"]).optional(),
            "resourceType": t.string().optional(),
            "resource": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["UpgradeAvailableEventIn"])
    types["UpgradeAvailableEventOut"] = t.struct(
        {
            "releaseChannel": t.proxy(renames["ReleaseChannelOut"]).optional(),
            "resourceType": t.string().optional(),
            "resource": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeAvailableEventOut"])
    types["UpgradeEventIn"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "targetVersion": t.string().optional(),
            "operationStartTime": t.string().optional(),
            "currentVersion": t.string().optional(),
            "resource": t.string().optional(),
            "operation": t.string().optional(),
        }
    ).named(renames["UpgradeEventIn"])
    types["UpgradeEventOut"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "targetVersion": t.string().optional(),
            "operationStartTime": t.string().optional(),
            "currentVersion": t.string().optional(),
            "resource": t.string().optional(),
            "operation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeEventOut"])
    types["ClusterUpdateIn"] = t.struct(
        {
            "desiredMasterVersion": t.string().optional(),
            "desiredNodePoolAutoscaling": t.proxy(
                renames["NodePoolAutoscalingIn"]
            ).optional(),
            "desiredClusterAutoscaling": t.proxy(
                renames["ClusterAutoscalingIn"]
            ).optional(),
            "desiredPrivateClusterConfig": t.proxy(
                renames["PrivateClusterConfigIn"]
            ).optional(),
            "desiredDnsConfig": t.proxy(renames["DNSConfigIn"]).optional(),
            "desiredShieldedNodes": t.proxy(renames["ShieldedNodesIn"]).optional(),
            "desiredGcfsConfig": t.proxy(renames["GcfsConfigIn"]).optional(),
            "desiredServiceExternalIpsConfig": t.proxy(
                renames["ServiceExternalIPsConfigIn"]
            ).optional(),
            "desiredGatewayApiConfig": t.proxy(
                renames["GatewayAPIConfigIn"]
            ).optional(),
            "desiredCostManagementConfig": t.proxy(
                renames["CostManagementConfigIn"]
            ).optional(),
            "desiredNodePoolId": t.string().optional(),
            "desiredStackType": t.string().optional(),
            "additionalPodRangesConfig": t.proxy(
                renames["AdditionalPodRangesConfigIn"]
            ).optional(),
            "desiredEnablePrivateEndpoint": t.boolean().optional(),
            "desiredLocations": t.array(t.string()).optional(),
            "desiredL4ilbSubsettingConfig": t.proxy(
                renames["ILBSubsettingConfigIn"]
            ).optional(),
            "desiredNetworkPerformanceConfig": t.proxy(
                renames["ClusterNetworkPerformanceConfigIn"]
            ).optional(),
            "desiredEnableFqdnNetworkPolicy": t.boolean().optional(),
            "desiredDatapathProvider": t.string().optional(),
            "desiredNodeVersion": t.string().optional(),
            "desiredImageType": t.string().optional(),
            "desiredMasterAuthorizedNetworksConfig": t.proxy(
                renames["MasterAuthorizedNetworksConfigIn"]
            ).optional(),
            "desiredAutopilotWorkloadPolicyConfig": t.proxy(
                renames["WorkloadPolicyConfigIn"]
            ).optional(),
            "desiredNodePoolAutoConfigNetworkTags": t.proxy(
                renames["NetworkTagsIn"]
            ).optional(),
            "desiredAuthenticatorGroupsConfig": t.proxy(
                renames["AuthenticatorGroupsConfigIn"]
            ).optional(),
            "desiredBinaryAuthorization": t.proxy(
                renames["BinaryAuthorizationIn"]
            ).optional(),
            "desiredMeshCertificates": t.proxy(
                renames["MeshCertificatesIn"]
            ).optional(),
            "desiredK8sBetaApis": t.proxy(renames["K8sBetaAPIConfigIn"]).optional(),
            "desiredFleet": t.proxy(renames["FleetIn"]).optional(),
            "desiredLoggingService": t.string().optional(),
            "desiredIntraNodeVisibilityConfig": t.proxy(
                renames["IntraNodeVisibilityConfigIn"]
            ).optional(),
            "desiredPrivateIpv6GoogleAccess": t.string().optional(),
            "desiredAddonsConfig": t.proxy(renames["AddonsConfigIn"]).optional(),
            "desiredDatabaseEncryption": t.proxy(
                renames["DatabaseEncryptionIn"]
            ).optional(),
            "removedAdditionalPodRangesConfig": t.proxy(
                renames["AdditionalPodRangesConfigIn"]
            ).optional(),
            "etag": t.string().optional(),
            "desiredLoggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "desiredVerticalPodAutoscaling": t.proxy(
                renames["VerticalPodAutoscalingIn"]
            ).optional(),
            "desiredMonitoringConfig": t.proxy(
                renames["MonitoringConfigIn"]
            ).optional(),
            "desiredMonitoringService": t.string().optional(),
            "desiredReleaseChannel": t.proxy(renames["ReleaseChannelIn"]).optional(),
            "desiredDefaultSnatStatus": t.proxy(
                renames["DefaultSnatStatusIn"]
            ).optional(),
            "desiredNotificationConfig": t.proxy(
                renames["NotificationConfigIn"]
            ).optional(),
            "desiredSecurityPostureConfig": t.proxy(
                renames["SecurityPostureConfigIn"]
            ).optional(),
            "enableK8sBetaApis": t.proxy(renames["K8sBetaAPIConfigIn"]).optional(),
            "desiredWorkloadIdentityConfig": t.proxy(
                renames["WorkloadIdentityConfigIn"]
            ).optional(),
            "desiredNodePoolLoggingConfig": t.proxy(
                renames["NodePoolLoggingConfigIn"]
            ).optional(),
            "desiredResourceUsageExportConfig": t.proxy(
                renames["ResourceUsageExportConfigIn"]
            ).optional(),
            "desiredIdentityServiceConfig": t.proxy(
                renames["IdentityServiceConfigIn"]
            ).optional(),
        }
    ).named(renames["ClusterUpdateIn"])
    types["ClusterUpdateOut"] = t.struct(
        {
            "desiredMasterVersion": t.string().optional(),
            "desiredNodePoolAutoscaling": t.proxy(
                renames["NodePoolAutoscalingOut"]
            ).optional(),
            "desiredClusterAutoscaling": t.proxy(
                renames["ClusterAutoscalingOut"]
            ).optional(),
            "desiredPrivateClusterConfig": t.proxy(
                renames["PrivateClusterConfigOut"]
            ).optional(),
            "desiredDnsConfig": t.proxy(renames["DNSConfigOut"]).optional(),
            "desiredShieldedNodes": t.proxy(renames["ShieldedNodesOut"]).optional(),
            "desiredGcfsConfig": t.proxy(renames["GcfsConfigOut"]).optional(),
            "desiredServiceExternalIpsConfig": t.proxy(
                renames["ServiceExternalIPsConfigOut"]
            ).optional(),
            "desiredGatewayApiConfig": t.proxy(
                renames["GatewayAPIConfigOut"]
            ).optional(),
            "desiredCostManagementConfig": t.proxy(
                renames["CostManagementConfigOut"]
            ).optional(),
            "desiredNodePoolId": t.string().optional(),
            "desiredStackType": t.string().optional(),
            "additionalPodRangesConfig": t.proxy(
                renames["AdditionalPodRangesConfigOut"]
            ).optional(),
            "desiredEnablePrivateEndpoint": t.boolean().optional(),
            "desiredLocations": t.array(t.string()).optional(),
            "desiredL4ilbSubsettingConfig": t.proxy(
                renames["ILBSubsettingConfigOut"]
            ).optional(),
            "desiredNetworkPerformanceConfig": t.proxy(
                renames["ClusterNetworkPerformanceConfigOut"]
            ).optional(),
            "desiredEnableFqdnNetworkPolicy": t.boolean().optional(),
            "desiredDatapathProvider": t.string().optional(),
            "desiredNodeVersion": t.string().optional(),
            "desiredImageType": t.string().optional(),
            "desiredMasterAuthorizedNetworksConfig": t.proxy(
                renames["MasterAuthorizedNetworksConfigOut"]
            ).optional(),
            "desiredAutopilotWorkloadPolicyConfig": t.proxy(
                renames["WorkloadPolicyConfigOut"]
            ).optional(),
            "desiredNodePoolAutoConfigNetworkTags": t.proxy(
                renames["NetworkTagsOut"]
            ).optional(),
            "desiredAuthenticatorGroupsConfig": t.proxy(
                renames["AuthenticatorGroupsConfigOut"]
            ).optional(),
            "desiredBinaryAuthorization": t.proxy(
                renames["BinaryAuthorizationOut"]
            ).optional(),
            "desiredMeshCertificates": t.proxy(
                renames["MeshCertificatesOut"]
            ).optional(),
            "desiredK8sBetaApis": t.proxy(renames["K8sBetaAPIConfigOut"]).optional(),
            "desiredFleet": t.proxy(renames["FleetOut"]).optional(),
            "desiredLoggingService": t.string().optional(),
            "desiredIntraNodeVisibilityConfig": t.proxy(
                renames["IntraNodeVisibilityConfigOut"]
            ).optional(),
            "desiredPrivateIpv6GoogleAccess": t.string().optional(),
            "desiredAddonsConfig": t.proxy(renames["AddonsConfigOut"]).optional(),
            "desiredDatabaseEncryption": t.proxy(
                renames["DatabaseEncryptionOut"]
            ).optional(),
            "removedAdditionalPodRangesConfig": t.proxy(
                renames["AdditionalPodRangesConfigOut"]
            ).optional(),
            "etag": t.string().optional(),
            "desiredLoggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "desiredVerticalPodAutoscaling": t.proxy(
                renames["VerticalPodAutoscalingOut"]
            ).optional(),
            "desiredMonitoringConfig": t.proxy(
                renames["MonitoringConfigOut"]
            ).optional(),
            "desiredMonitoringService": t.string().optional(),
            "desiredReleaseChannel": t.proxy(renames["ReleaseChannelOut"]).optional(),
            "desiredDefaultSnatStatus": t.proxy(
                renames["DefaultSnatStatusOut"]
            ).optional(),
            "desiredNotificationConfig": t.proxy(
                renames["NotificationConfigOut"]
            ).optional(),
            "desiredSecurityPostureConfig": t.proxy(
                renames["SecurityPostureConfigOut"]
            ).optional(),
            "enableK8sBetaApis": t.proxy(renames["K8sBetaAPIConfigOut"]).optional(),
            "desiredWorkloadIdentityConfig": t.proxy(
                renames["WorkloadIdentityConfigOut"]
            ).optional(),
            "desiredNodePoolLoggingConfig": t.proxy(
                renames["NodePoolLoggingConfigOut"]
            ).optional(),
            "desiredResourceUsageExportConfig": t.proxy(
                renames["ResourceUsageExportConfigOut"]
            ).optional(),
            "desiredIdentityServiceConfig": t.proxy(
                renames["IdentityServiceConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterUpdateOut"])
    types["PubSubIn"] = t.struct(
        {
            "topic": t.string().optional(),
            "enabled": t.boolean().optional(),
            "filter": t.proxy(renames["FilterIn"]).optional(),
        }
    ).named(renames["PubSubIn"])
    types["PubSubOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "enabled": t.boolean().optional(),
            "filter": t.proxy(renames["FilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubSubOut"])
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
    types["SecurityBulletinEventIn"] = t.struct(
        {
            "bulletinId": t.string().optional(),
            "resourceTypeAffected": t.string().optional(),
            "patchedVersions": t.array(t.string()).optional(),
            "affectedSupportedMinors": t.array(t.string()).optional(),
            "bulletinUri": t.string().optional(),
            "suggestedUpgradeTarget": t.string().optional(),
            "cveIds": t.array(t.string()).optional(),
            "manualStepsRequired": t.boolean().optional(),
            "briefDescription": t.string().optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["SecurityBulletinEventIn"])
    types["SecurityBulletinEventOut"] = t.struct(
        {
            "bulletinId": t.string().optional(),
            "resourceTypeAffected": t.string().optional(),
            "patchedVersions": t.array(t.string()).optional(),
            "affectedSupportedMinors": t.array(t.string()).optional(),
            "bulletinUri": t.string().optional(),
            "suggestedUpgradeTarget": t.string().optional(),
            "cveIds": t.array(t.string()).optional(),
            "manualStepsRequired": t.boolean().optional(),
            "briefDescription": t.string().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecurityBulletinEventOut"])
    types["NodeLabelsIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["NodeLabelsIn"])
    types["NodeLabelsOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeLabelsOut"])
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
    types["ManagedPrometheusConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["ManagedPrometheusConfigIn"])
    types["ManagedPrometheusConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedPrometheusConfigOut"])
    types["GcePersistentDiskCsiDriverConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["GcePersistentDiskCsiDriverConfigIn"])
    types["GcePersistentDiskCsiDriverConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcePersistentDiskCsiDriverConfigOut"])
    types["AcceleratorConfigIn"] = t.struct(
        {
            "gpuDriverInstallationConfig": t.proxy(
                renames["GPUDriverInstallationConfigIn"]
            ).optional(),
            "acceleratorType": t.string().optional(),
            "acceleratorCount": t.string().optional(),
            "gpuPartitionSize": t.string().optional(),
            "gpuSharingConfig": t.proxy(renames["GPUSharingConfigIn"]).optional(),
        }
    ).named(renames["AcceleratorConfigIn"])
    types["AcceleratorConfigOut"] = t.struct(
        {
            "gpuDriverInstallationConfig": t.proxy(
                renames["GPUDriverInstallationConfigOut"]
            ).optional(),
            "acceleratorType": t.string().optional(),
            "acceleratorCount": t.string().optional(),
            "gpuPartitionSize": t.string().optional(),
            "gpuSharingConfig": t.proxy(renames["GPUSharingConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceleratorConfigOut"])
    types["PodCIDROverprovisionConfigIn"] = t.struct(
        {"disable": t.boolean().optional()}
    ).named(renames["PodCIDROverprovisionConfigIn"])
    types["PodCIDROverprovisionConfigOut"] = t.struct(
        {
            "disable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PodCIDROverprovisionConfigOut"])
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
    types["NodeConfigDefaultsIn"] = t.struct(
        {
            "gcfsConfig": t.proxy(renames["GcfsConfigIn"]).optional(),
            "loggingConfig": t.proxy(renames["NodePoolLoggingConfigIn"]).optional(),
        }
    ).named(renames["NodeConfigDefaultsIn"])
    types["NodeConfigDefaultsOut"] = t.struct(
        {
            "gcfsConfig": t.proxy(renames["GcfsConfigOut"]).optional(),
            "loggingConfig": t.proxy(renames["NodePoolLoggingConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeConfigDefaultsOut"])
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
    types["SetMaintenancePolicyRequestIn"] = t.struct(
        {
            "clusterId": t.string(),
            "name": t.string().optional(),
            "projectId": t.string(),
            "zone": t.string(),
            "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
        }
    ).named(renames["SetMaintenancePolicyRequestIn"])
    types["SetMaintenancePolicyRequestOut"] = t.struct(
        {
            "clusterId": t.string(),
            "name": t.string().optional(),
            "projectId": t.string(),
            "zone": t.string(),
            "maintenancePolicy": t.proxy(renames["MaintenancePolicyOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetMaintenancePolicyRequestOut"])
    types["BestEffortProvisioningIn"] = t.struct(
        {"minProvisionNodes": t.integer().optional(), "enabled": t.boolean().optional()}
    ).named(renames["BestEffortProvisioningIn"])
    types["BestEffortProvisioningOut"] = t.struct(
        {
            "minProvisionNodes": t.integer().optional(),
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BestEffortProvisioningOut"])
    types["StandardRolloutPolicyIn"] = t.struct(
        {
            "batchSoakDuration": t.string().optional(),
            "batchNodeCount": t.integer().optional(),
            "batchPercentage": t.number().optional(),
        }
    ).named(renames["StandardRolloutPolicyIn"])
    types["StandardRolloutPolicyOut"] = t.struct(
        {
            "batchSoakDuration": t.string().optional(),
            "batchNodeCount": t.integer().optional(),
            "batchPercentage": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StandardRolloutPolicyOut"])
    types["ConfidentialNodesIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["ConfidentialNodesIn"]
    )
    types["ConfidentialNodesOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfidentialNodesOut"])
    types["MaintenanceExclusionOptionsIn"] = t.struct(
        {"scope": t.string().optional()}
    ).named(renames["MaintenanceExclusionOptionsIn"])
    types["MaintenanceExclusionOptionsOut"] = t.struct(
        {
            "scope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceExclusionOptionsOut"])
    types["IntraNodeVisibilityConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["IntraNodeVisibilityConfigIn"])
    types["IntraNodeVisibilityConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntraNodeVisibilityConfigOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "selfLink": t.string().optional(),
            "operationType": t.string().optional(),
            "endTime": t.string().optional(),
            "zone": t.string().optional(),
            "nodepoolConditions": t.array(
                t.proxy(renames["StatusConditionIn"])
            ).optional(),
            "startTime": t.string().optional(),
            "clusterConditions": t.array(
                t.proxy(renames["StatusConditionIn"])
            ).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "detail": t.string().optional(),
            "targetLink": t.string().optional(),
            "location": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "selfLink": t.string().optional(),
            "operationType": t.string().optional(),
            "endTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "zone": t.string().optional(),
            "nodepoolConditions": t.array(
                t.proxy(renames["StatusConditionOut"])
            ).optional(),
            "startTime": t.string().optional(),
            "clusterConditions": t.array(
                t.proxy(renames["StatusConditionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "detail": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "targetLink": t.string().optional(),
            "location": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["GPUSharingConfigIn"] = t.struct(
        {
            "maxSharedClientsPerGpu": t.string().optional(),
            "gpuSharingStrategy": t.string().optional(),
        }
    ).named(renames["GPUSharingConfigIn"])
    types["GPUSharingConfigOut"] = t.struct(
        {
            "maxSharedClientsPerGpu": t.string().optional(),
            "gpuSharingStrategy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GPUSharingConfigOut"])
    types["GatewayAPIConfigIn"] = t.struct({"channel": t.string().optional()}).named(
        renames["GatewayAPIConfigIn"]
    )
    types["GatewayAPIConfigOut"] = t.struct(
        {
            "channel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GatewayAPIConfigOut"])
    types["SetLocationsRequestIn"] = t.struct(
        {
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "locations": t.array(t.string()),
            "projectId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SetLocationsRequestIn"])
    types["SetLocationsRequestOut"] = t.struct(
        {
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "locations": t.array(t.string()),
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetLocationsRequestOut"])
    types["StartIPRotationRequestIn"] = t.struct(
        {
            "clusterId": t.string().optional(),
            "rotateCredentials": t.boolean().optional(),
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["StartIPRotationRequestIn"])
    types["StartIPRotationRequestOut"] = t.struct(
        {
            "clusterId": t.string().optional(),
            "rotateCredentials": t.boolean().optional(),
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartIPRotationRequestOut"])
    types["SetNodePoolAutoscalingRequestIn"] = t.struct(
        {
            "nodePoolId": t.string().optional(),
            "projectId": t.string().optional(),
            "autoscaling": t.proxy(renames["NodePoolAutoscalingIn"]),
            "name": t.string().optional(),
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
        }
    ).named(renames["SetNodePoolAutoscalingRequestIn"])
    types["SetNodePoolAutoscalingRequestOut"] = t.struct(
        {
            "nodePoolId": t.string().optional(),
            "projectId": t.string().optional(),
            "autoscaling": t.proxy(renames["NodePoolAutoscalingOut"]),
            "name": t.string().optional(),
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetNodePoolAutoscalingRequestOut"])
    types["GcsFuseCsiDriverConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["GcsFuseCsiDriverConfigIn"])
    types["GcsFuseCsiDriverConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcsFuseCsiDriverConfigOut"])
    types["NetworkTagsIn"] = t.struct({"tags": t.array(t.string()).optional()}).named(
        renames["NetworkTagsIn"]
    )
    types["NetworkTagsOut"] = t.struct(
        {
            "tags": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkTagsOut"])
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
    types["TimeWindowIn"] = t.struct(
        {
            "maintenanceExclusionOptions": t.proxy(
                renames["MaintenanceExclusionOptionsIn"]
            ).optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["TimeWindowIn"])
    types["TimeWindowOut"] = t.struct(
        {
            "maintenanceExclusionOptions": t.proxy(
                renames["MaintenanceExclusionOptionsOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeWindowOut"])
    types["NodePoolAutoConfigIn"] = t.struct(
        {"networkTags": t.proxy(renames["NetworkTagsIn"]).optional()}
    ).named(renames["NodePoolAutoConfigIn"])
    types["NodePoolAutoConfigOut"] = t.struct(
        {
            "networkTags": t.proxy(renames["NetworkTagsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodePoolAutoConfigOut"])
    types["DefaultSnatStatusIn"] = t.struct({"disabled": t.boolean().optional()}).named(
        renames["DefaultSnatStatusIn"]
    )
    types["DefaultSnatStatusOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DefaultSnatStatusOut"])
    types["UpdateMasterRequestIn"] = t.struct(
        {
            "clusterId": t.string().optional(),
            "masterVersion": t.string(),
            "name": t.string().optional(),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["UpdateMasterRequestIn"])
    types["UpdateMasterRequestOut"] = t.struct(
        {
            "clusterId": t.string().optional(),
            "masterVersion": t.string(),
            "name": t.string().optional(),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateMasterRequestOut"])
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
    types["NodePoolIn"] = t.struct(
        {
            "version": t.string().optional(),
            "locations": t.array(t.string()).optional(),
            "config": t.proxy(renames["NodeConfigIn"]).optional(),
            "bestEffortProvisioning": t.proxy(
                renames["BestEffortProvisioningIn"]
            ).optional(),
            "statusMessage": t.string().optional(),
            "podIpv4CidrSize": t.integer().optional(),
            "selfLink": t.string().optional(),
            "management": t.proxy(renames["NodeManagementIn"]).optional(),
            "initialNodeCount": t.integer().optional(),
            "upgradeSettings": t.proxy(renames["UpgradeSettingsIn"]).optional(),
            "maxPodsConstraint": t.proxy(renames["MaxPodsConstraintIn"]).optional(),
            "conditions": t.array(t.proxy(renames["StatusConditionIn"])).optional(),
            "status": t.string().optional(),
            "name": t.string().optional(),
            "instanceGroupUrls": t.array(t.string()).optional(),
            "autoscaling": t.proxy(renames["NodePoolAutoscalingIn"]).optional(),
            "placementPolicy": t.proxy(renames["PlacementPolicyIn"]).optional(),
            "networkConfig": t.proxy(renames["NodeNetworkConfigIn"]).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["NodePoolIn"])
    types["NodePoolOut"] = t.struct(
        {
            "version": t.string().optional(),
            "locations": t.array(t.string()).optional(),
            "config": t.proxy(renames["NodeConfigOut"]).optional(),
            "bestEffortProvisioning": t.proxy(
                renames["BestEffortProvisioningOut"]
            ).optional(),
            "statusMessage": t.string().optional(),
            "podIpv4CidrSize": t.integer().optional(),
            "selfLink": t.string().optional(),
            "management": t.proxy(renames["NodeManagementOut"]).optional(),
            "initialNodeCount": t.integer().optional(),
            "upgradeSettings": t.proxy(renames["UpgradeSettingsOut"]).optional(),
            "maxPodsConstraint": t.proxy(renames["MaxPodsConstraintOut"]).optional(),
            "updateInfo": t.proxy(renames["UpdateInfoOut"]).optional(),
            "conditions": t.array(t.proxy(renames["StatusConditionOut"])).optional(),
            "status": t.string().optional(),
            "name": t.string().optional(),
            "instanceGroupUrls": t.array(t.string()).optional(),
            "autoscaling": t.proxy(renames["NodePoolAutoscalingOut"]).optional(),
            "placementPolicy": t.proxy(renames["PlacementPolicyOut"]).optional(),
            "networkConfig": t.proxy(renames["NodeNetworkConfigOut"]).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodePoolOut"])
    types["NodePoolDefaultsIn"] = t.struct(
        {"nodeConfigDefaults": t.proxy(renames["NodeConfigDefaultsIn"]).optional()}
    ).named(renames["NodePoolDefaultsIn"])
    types["NodePoolDefaultsOut"] = t.struct(
        {
            "nodeConfigDefaults": t.proxy(renames["NodeConfigDefaultsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodePoolDefaultsOut"])
    types["AutoprovisioningNodePoolDefaultsIn"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "insecureKubeletReadonlyPortEnabled": t.boolean().optional(),
            "minCpuPlatform": t.string().optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "management": t.proxy(renames["NodeManagementIn"]).optional(),
            "upgradeSettings": t.proxy(renames["UpgradeSettingsIn"]).optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigIn"]
            ).optional(),
            "diskSizeGb": t.integer().optional(),
            "imageType": t.string().optional(),
            "diskType": t.string().optional(),
            "bootDiskKmsKey": t.string().optional(),
        }
    ).named(renames["AutoprovisioningNodePoolDefaultsIn"])
    types["AutoprovisioningNodePoolDefaultsOut"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "insecureKubeletReadonlyPortEnabled": t.boolean().optional(),
            "minCpuPlatform": t.string().optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "management": t.proxy(renames["NodeManagementOut"]).optional(),
            "upgradeSettings": t.proxy(renames["UpgradeSettingsOut"]).optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigOut"]
            ).optional(),
            "diskSizeGb": t.integer().optional(),
            "imageType": t.string().optional(),
            "diskType": t.string().optional(),
            "bootDiskKmsKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoprovisioningNodePoolDefaultsOut"])
    types["ClientCertificateConfigIn"] = t.struct(
        {"issueClientCertificate": t.boolean().optional()}
    ).named(renames["ClientCertificateConfigIn"])
    types["ClientCertificateConfigOut"] = t.struct(
        {
            "issueClientCertificate": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientCertificateConfigOut"])
    types["PrivateClusterMasterGlobalAccessConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["PrivateClusterMasterGlobalAccessConfigIn"])
    types["PrivateClusterMasterGlobalAccessConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateClusterMasterGlobalAccessConfigOut"])
    types["GcfsConfigIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["GcfsConfigIn"]
    )
    types["GcfsConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcfsConfigOut"])
    types["ClusterIn"] = t.struct(
        {
            "authenticatorGroupsConfig": t.proxy(
                renames["AuthenticatorGroupsConfigIn"]
            ).optional(),
            "nodePoolAutoConfig": t.proxy(renames["NodePoolAutoConfigIn"]).optional(),
            "fleet": t.proxy(renames["FleetIn"]).optional(),
            "masterAuthorizedNetworksConfig": t.proxy(
                renames["MasterAuthorizedNetworksConfigIn"]
            ).optional(),
            "etag": t.string().optional(),
            "releaseChannel": t.proxy(renames["ReleaseChannelIn"]).optional(),
            "locations": t.array(t.string()).optional(),
            "selfLink": t.string().optional(),
            "zone": t.string().optional(),
            "networkPolicy": t.proxy(renames["NetworkPolicyIn"]).optional(),
            "loggingService": t.string().optional(),
            "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]).optional(),
            "privateClusterConfig": t.proxy(
                renames["PrivateClusterConfigIn"]
            ).optional(),
            "network": t.string().optional(),
            "description": t.string().optional(),
            "meshCertificates": t.proxy(renames["MeshCertificatesIn"]).optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "currentNodeCount": t.integer().optional(),
            "resourceLabels": t.struct({"_": t.string().optional()}).optional(),
            "nodeIpv4CidrSize": t.integer().optional(),
            "ipAllocationPolicy": t.proxy(renames["IPAllocationPolicyIn"]).optional(),
            "enableKubernetesAlpha": t.boolean().optional(),
            "statusMessage": t.string().optional(),
            "initialNodeCount": t.integer().optional(),
            "verticalPodAutoscaling": t.proxy(
                renames["VerticalPodAutoscalingIn"]
            ).optional(),
            "currentMasterVersion": t.string().optional(),
            "binaryAuthorization": t.proxy(renames["BinaryAuthorizationIn"]).optional(),
            "addonsConfig": t.proxy(renames["AddonsConfigIn"]).optional(),
            "databaseEncryption": t.proxy(renames["DatabaseEncryptionIn"]).optional(),
            "tpuIpv4CidrBlock": t.string().optional(),
            "defaultMaxPodsConstraint": t.proxy(
                renames["MaxPodsConstraintIn"]
            ).optional(),
            "createTime": t.string().optional(),
            "identityServiceConfig": t.proxy(
                renames["IdentityServiceConfigIn"]
            ).optional(),
            "nodeConfig": t.proxy(renames["NodeConfigIn"]).optional(),
            "masterAuth": t.proxy(renames["MasterAuthIn"]).optional(),
            "name": t.string().optional(),
            "enableTpu": t.boolean().optional(),
            "enableK8sBetaApis": t.proxy(renames["K8sBetaAPIConfigIn"]).optional(),
            "notificationConfig": t.proxy(renames["NotificationConfigIn"]).optional(),
            "legacyAbac": t.proxy(renames["LegacyAbacIn"]).optional(),
            "subnetwork": t.string().optional(),
            "initialClusterVersion": t.string().optional(),
            "labelFingerprint": t.string().optional(),
            "nodePools": t.array(t.proxy(renames["NodePoolIn"])).optional(),
            "autopilot": t.proxy(renames["AutopilotIn"]).optional(),
            "instanceGroupUrls": t.array(t.string()).optional(),
            "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
            "workloadIdentityConfig": t.proxy(
                renames["WorkloadIdentityConfigIn"]
            ).optional(),
            "location": t.string().optional(),
            "nodePoolDefaults": t.proxy(renames["NodePoolDefaultsIn"]).optional(),
            "autoscaling": t.proxy(renames["ClusterAutoscalingIn"]).optional(),
            "confidentialNodes": t.proxy(renames["ConfidentialNodesIn"]).optional(),
            "resourceUsageExportConfig": t.proxy(
                renames["ResourceUsageExportConfigIn"]
            ).optional(),
            "clusterIpv4Cidr": t.string().optional(),
            "costManagementConfig": t.proxy(
                renames["CostManagementConfigIn"]
            ).optional(),
            "monitoringService": t.string().optional(),
            "conditions": t.array(t.proxy(renames["StatusConditionIn"])).optional(),
            "status": t.string().optional(),
            "expireTime": t.string().optional(),
            "endpoint": t.string().optional(),
            "securityPostureConfig": t.proxy(
                renames["SecurityPostureConfigIn"]
            ).optional(),
            "monitoringConfig": t.proxy(renames["MonitoringConfigIn"]).optional(),
            "shieldedNodes": t.proxy(renames["ShieldedNodesIn"]).optional(),
            "currentNodeVersion": t.string().optional(),
            "servicesIpv4Cidr": t.string().optional(),
        }
    ).named(renames["ClusterIn"])
    types["ClusterOut"] = t.struct(
        {
            "authenticatorGroupsConfig": t.proxy(
                renames["AuthenticatorGroupsConfigOut"]
            ).optional(),
            "nodePoolAutoConfig": t.proxy(renames["NodePoolAutoConfigOut"]).optional(),
            "fleet": t.proxy(renames["FleetOut"]).optional(),
            "masterAuthorizedNetworksConfig": t.proxy(
                renames["MasterAuthorizedNetworksConfigOut"]
            ).optional(),
            "etag": t.string().optional(),
            "releaseChannel": t.proxy(renames["ReleaseChannelOut"]).optional(),
            "locations": t.array(t.string()).optional(),
            "selfLink": t.string().optional(),
            "zone": t.string().optional(),
            "networkPolicy": t.proxy(renames["NetworkPolicyOut"]).optional(),
            "loggingService": t.string().optional(),
            "maintenancePolicy": t.proxy(renames["MaintenancePolicyOut"]).optional(),
            "privateClusterConfig": t.proxy(
                renames["PrivateClusterConfigOut"]
            ).optional(),
            "network": t.string().optional(),
            "description": t.string().optional(),
            "meshCertificates": t.proxy(renames["MeshCertificatesOut"]).optional(),
            "id": t.string().optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "currentNodeCount": t.integer().optional(),
            "resourceLabels": t.struct({"_": t.string().optional()}).optional(),
            "nodeIpv4CidrSize": t.integer().optional(),
            "ipAllocationPolicy": t.proxy(renames["IPAllocationPolicyOut"]).optional(),
            "enableKubernetesAlpha": t.boolean().optional(),
            "statusMessage": t.string().optional(),
            "initialNodeCount": t.integer().optional(),
            "verticalPodAutoscaling": t.proxy(
                renames["VerticalPodAutoscalingOut"]
            ).optional(),
            "currentMasterVersion": t.string().optional(),
            "binaryAuthorization": t.proxy(
                renames["BinaryAuthorizationOut"]
            ).optional(),
            "addonsConfig": t.proxy(renames["AddonsConfigOut"]).optional(),
            "databaseEncryption": t.proxy(renames["DatabaseEncryptionOut"]).optional(),
            "tpuIpv4CidrBlock": t.string().optional(),
            "defaultMaxPodsConstraint": t.proxy(
                renames["MaxPodsConstraintOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "identityServiceConfig": t.proxy(
                renames["IdentityServiceConfigOut"]
            ).optional(),
            "nodeConfig": t.proxy(renames["NodeConfigOut"]).optional(),
            "masterAuth": t.proxy(renames["MasterAuthOut"]).optional(),
            "name": t.string().optional(),
            "enableTpu": t.boolean().optional(),
            "enableK8sBetaApis": t.proxy(renames["K8sBetaAPIConfigOut"]).optional(),
            "notificationConfig": t.proxy(renames["NotificationConfigOut"]).optional(),
            "legacyAbac": t.proxy(renames["LegacyAbacOut"]).optional(),
            "subnetwork": t.string().optional(),
            "initialClusterVersion": t.string().optional(),
            "labelFingerprint": t.string().optional(),
            "nodePools": t.array(t.proxy(renames["NodePoolOut"])).optional(),
            "autopilot": t.proxy(renames["AutopilotOut"]).optional(),
            "instanceGroupUrls": t.array(t.string()).optional(),
            "networkConfig": t.proxy(renames["NetworkConfigOut"]).optional(),
            "workloadIdentityConfig": t.proxy(
                renames["WorkloadIdentityConfigOut"]
            ).optional(),
            "location": t.string().optional(),
            "nodePoolDefaults": t.proxy(renames["NodePoolDefaultsOut"]).optional(),
            "autoscaling": t.proxy(renames["ClusterAutoscalingOut"]).optional(),
            "confidentialNodes": t.proxy(renames["ConfidentialNodesOut"]).optional(),
            "resourceUsageExportConfig": t.proxy(
                renames["ResourceUsageExportConfigOut"]
            ).optional(),
            "clusterIpv4Cidr": t.string().optional(),
            "costManagementConfig": t.proxy(
                renames["CostManagementConfigOut"]
            ).optional(),
            "monitoringService": t.string().optional(),
            "conditions": t.array(t.proxy(renames["StatusConditionOut"])).optional(),
            "status": t.string().optional(),
            "expireTime": t.string().optional(),
            "endpoint": t.string().optional(),
            "securityPostureConfig": t.proxy(
                renames["SecurityPostureConfigOut"]
            ).optional(),
            "monitoringConfig": t.proxy(renames["MonitoringConfigOut"]).optional(),
            "shieldedNodes": t.proxy(renames["ShieldedNodesOut"]).optional(),
            "currentNodeVersion": t.string().optional(),
            "servicesIpv4Cidr": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterOut"])
    types["NotificationConfigIn"] = t.struct(
        {"pubsub": t.proxy(renames["PubSubIn"]).optional()}
    ).named(renames["NotificationConfigIn"])
    types["NotificationConfigOut"] = t.struct(
        {
            "pubsub": t.proxy(renames["PubSubOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationConfigOut"])
    types["FilterIn"] = t.struct({"eventType": t.array(t.string()).optional()}).named(
        renames["FilterIn"]
    )
    types["FilterOut"] = t.struct(
        {
            "eventType": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterOut"])

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
    functions["projectsLocationsClustersSetMasterAuth"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersUpdate"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetNetworkPolicy"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetMaintenancePolicy"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetAddons"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersCreate"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersStartIpRotation"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetResourceLabels"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetLocations"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersDelete"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetLegacyAbac"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetLogging"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersList"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersUpdateMaster"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetMonitoring"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersGetJwks"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersCheckAutopilotCompatibility"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersCompleteIpRotation"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersGet"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsClustersWell_knownGetOpenid_configuration"
    ] = container.get(
        "v1/{parent}/.well-known/openid-configuration",
        t.struct({"parent": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GetOpenIDConfigResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsSetSize"] = container.post(
        "v1/{name}:completeUpgrade",
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
    functions["projectsLocationsClustersNodePoolsSetAutoscaling"] = container.post(
        "v1/{name}:completeUpgrade",
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
    functions["projectsLocationsClustersNodePoolsSetManagement"] = container.post(
        "v1/{name}:completeUpgrade",
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
    functions["projectsLocationsClustersNodePoolsRollback"] = container.post(
        "v1/{name}:completeUpgrade",
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
    functions["projectsLocationsClustersNodePoolsCreate"] = container.post(
        "v1/{name}:completeUpgrade",
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
    functions["projectsLocationsClustersNodePoolsList"] = container.post(
        "v1/{name}:completeUpgrade",
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
    functions["projectsLocationsClustersNodePoolsUpdate"] = container.post(
        "v1/{name}:completeUpgrade",
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
    functions["projectsLocationsClustersNodePoolsDelete"] = container.post(
        "v1/{name}:completeUpgrade",
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
    functions["projectsLocationsClustersNodePoolsGet"] = container.post(
        "v1/{name}:completeUpgrade",
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
    functions["projectsLocationsClustersNodePoolsCompleteUpgrade"] = container.post(
        "v1/{name}:completeUpgrade",
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
    functions["projectsLocationsOperationsCancel"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "operationId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "operationId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "operationId": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAggregatedUsableSubnetworksList"] = container.get(
        "v1/{parent}/aggregated/usableSubnetworks",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "filter": t.string().optional(),
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
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServerConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersAddons"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "cluster": t.proxy(renames["ClusterIn"]),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersLegacyAbac"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "cluster": t.proxy(renames["ClusterIn"]),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersLocations"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "cluster": t.proxy(renames["ClusterIn"]),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersCompleteIpRotation"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "cluster": t.proxy(renames["ClusterIn"]),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersList"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "cluster": t.proxy(renames["ClusterIn"]),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersSetMasterAuth"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "cluster": t.proxy(renames["ClusterIn"]),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersLogging"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "cluster": t.proxy(renames["ClusterIn"]),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersResourceLabels"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "cluster": t.proxy(renames["ClusterIn"]),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersSetMaintenancePolicy"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "cluster": t.proxy(renames["ClusterIn"]),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersUpdate"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "cluster": t.proxy(renames["ClusterIn"]),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersGet"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "cluster": t.proxy(renames["ClusterIn"]),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersSetNetworkPolicy"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "cluster": t.proxy(renames["ClusterIn"]),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersMonitoring"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "cluster": t.proxy(renames["ClusterIn"]),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersMaster"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "cluster": t.proxy(renames["ClusterIn"]),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersDelete"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "cluster": t.proxy(renames["ClusterIn"]),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersStartIpRotation"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "cluster": t.proxy(renames["ClusterIn"]),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersCreate"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "zone": t.string().optional(),
                "projectId": t.string().optional(),
                "cluster": t.proxy(renames["ClusterIn"]),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsUpdate"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools",
        t.struct(
            {
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "parent": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsSetManagement"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools",
        t.struct(
            {
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "parent": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsRollback"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools",
        t.struct(
            {
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "parent": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsCreate"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools",
        t.struct(
            {
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "parent": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsGet"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools",
        t.struct(
            {
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "parent": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsSetSize"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools",
        t.struct(
            {
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "parent": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsDelete"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools",
        t.struct(
            {
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "parent": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsAutoscaling"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools",
        t.struct(
            {
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "parent": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsList"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools",
        t.struct(
            {
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "parent": t.string().optional(),
                "clusterId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListNodePoolsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesOperationsCancel"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/operations/{operationId}",
        t.struct(
            {
                "zone": t.string().optional(),
                "operationId": t.string().optional(),
                "projectId": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesOperationsList"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/operations/{operationId}",
        t.struct(
            {
                "zone": t.string().optional(),
                "operationId": t.string().optional(),
                "projectId": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesOperationsGet"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/operations/{operationId}",
        t.struct(
            {
                "zone": t.string().optional(),
                "operationId": t.string().optional(),
                "projectId": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="container",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
