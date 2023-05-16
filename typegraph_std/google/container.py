from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_container() -> Import:
    container = HTTPRuntime("https://container.googleapis.com/")

    renames = {
        "ErrorResponse": "_container_1_ErrorResponse",
        "MetricIn": "_container_2_MetricIn",
        "MetricOut": "_container_3_MetricOut",
        "StartIPRotationRequestIn": "_container_4_StartIPRotationRequestIn",
        "StartIPRotationRequestOut": "_container_5_StartIPRotationRequestOut",
        "FastSocketIn": "_container_6_FastSocketIn",
        "FastSocketOut": "_container_7_FastSocketOut",
        "ServiceExternalIPsConfigIn": "_container_8_ServiceExternalIPsConfigIn",
        "ServiceExternalIPsConfigOut": "_container_9_ServiceExternalIPsConfigOut",
        "ReservationAffinityIn": "_container_10_ReservationAffinityIn",
        "ReservationAffinityOut": "_container_11_ReservationAffinityOut",
        "CancelOperationRequestIn": "_container_12_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_container_13_CancelOperationRequestOut",
        "ResourceUsageExportConfigIn": "_container_14_ResourceUsageExportConfigIn",
        "ResourceUsageExportConfigOut": "_container_15_ResourceUsageExportConfigOut",
        "ShieldedNodesIn": "_container_16_ShieldedNodesIn",
        "ShieldedNodesOut": "_container_17_ShieldedNodesOut",
        "SetAddonsConfigRequestIn": "_container_18_SetAddonsConfigRequestIn",
        "SetAddonsConfigRequestOut": "_container_19_SetAddonsConfigRequestOut",
        "WorkloadIdentityConfigIn": "_container_20_WorkloadIdentityConfigIn",
        "WorkloadIdentityConfigOut": "_container_21_WorkloadIdentityConfigOut",
        "ReleaseChannelIn": "_container_22_ReleaseChannelIn",
        "ReleaseChannelOut": "_container_23_ReleaseChannelOut",
        "GetOpenIDConfigResponseIn": "_container_24_GetOpenIDConfigResponseIn",
        "GetOpenIDConfigResponseOut": "_container_25_GetOpenIDConfigResponseOut",
        "JwkIn": "_container_26_JwkIn",
        "JwkOut": "_container_27_JwkOut",
        "NodeTaintIn": "_container_28_NodeTaintIn",
        "NodeTaintOut": "_container_29_NodeTaintOut",
        "ResourceLimitIn": "_container_30_ResourceLimitIn",
        "ResourceLimitOut": "_container_31_ResourceLimitOut",
        "MaintenanceExclusionOptionsIn": "_container_32_MaintenanceExclusionOptionsIn",
        "MaintenanceExclusionOptionsOut": "_container_33_MaintenanceExclusionOptionsOut",
        "GkeBackupAgentConfigIn": "_container_34_GkeBackupAgentConfigIn",
        "GkeBackupAgentConfigOut": "_container_35_GkeBackupAgentConfigOut",
        "MaintenancePolicyIn": "_container_36_MaintenancePolicyIn",
        "MaintenancePolicyOut": "_container_37_MaintenancePolicyOut",
        "MasterAuthorizedNetworksConfigIn": "_container_38_MasterAuthorizedNetworksConfigIn",
        "MasterAuthorizedNetworksConfigOut": "_container_39_MasterAuthorizedNetworksConfigOut",
        "SetMonitoringServiceRequestIn": "_container_40_SetMonitoringServiceRequestIn",
        "SetMonitoringServiceRequestOut": "_container_41_SetMonitoringServiceRequestOut",
        "UpgradeSettingsIn": "_container_42_UpgradeSettingsIn",
        "UpgradeSettingsOut": "_container_43_UpgradeSettingsOut",
        "DailyMaintenanceWindowIn": "_container_44_DailyMaintenanceWindowIn",
        "DailyMaintenanceWindowOut": "_container_45_DailyMaintenanceWindowOut",
        "CostManagementConfigIn": "_container_46_CostManagementConfigIn",
        "CostManagementConfigOut": "_container_47_CostManagementConfigOut",
        "CreateClusterRequestIn": "_container_48_CreateClusterRequestIn",
        "CreateClusterRequestOut": "_container_49_CreateClusterRequestOut",
        "NetworkPolicyIn": "_container_50_NetworkPolicyIn",
        "NetworkPolicyOut": "_container_51_NetworkPolicyOut",
        "HttpLoadBalancingIn": "_container_52_HttpLoadBalancingIn",
        "HttpLoadBalancingOut": "_container_53_HttpLoadBalancingOut",
        "NodeManagementIn": "_container_54_NodeManagementIn",
        "NodeManagementOut": "_container_55_NodeManagementOut",
        "WindowsNodeConfigIn": "_container_56_WindowsNodeConfigIn",
        "WindowsNodeConfigOut": "_container_57_WindowsNodeConfigOut",
        "AdvancedMachineFeaturesIn": "_container_58_AdvancedMachineFeaturesIn",
        "AdvancedMachineFeaturesOut": "_container_59_AdvancedMachineFeaturesOut",
        "GatewayAPIConfigIn": "_container_60_GatewayAPIConfigIn",
        "GatewayAPIConfigOut": "_container_61_GatewayAPIConfigOut",
        "DefaultSnatStatusIn": "_container_62_DefaultSnatStatusIn",
        "DefaultSnatStatusOut": "_container_63_DefaultSnatStatusOut",
        "ListClustersResponseIn": "_container_64_ListClustersResponseIn",
        "ListClustersResponseOut": "_container_65_ListClustersResponseOut",
        "MonitoringComponentConfigIn": "_container_66_MonitoringComponentConfigIn",
        "MonitoringComponentConfigOut": "_container_67_MonitoringComponentConfigOut",
        "GcePersistentDiskCsiDriverConfigIn": "_container_68_GcePersistentDiskCsiDriverConfigIn",
        "GcePersistentDiskCsiDriverConfigOut": "_container_69_GcePersistentDiskCsiDriverConfigOut",
        "DnsCacheConfigIn": "_container_70_DnsCacheConfigIn",
        "DnsCacheConfigOut": "_container_71_DnsCacheConfigOut",
        "ClusterAutoscalingIn": "_container_72_ClusterAutoscalingIn",
        "ClusterAutoscalingOut": "_container_73_ClusterAutoscalingOut",
        "ClusterUpdateIn": "_container_74_ClusterUpdateIn",
        "ClusterUpdateOut": "_container_75_ClusterUpdateOut",
        "SetNodePoolManagementRequestIn": "_container_76_SetNodePoolManagementRequestIn",
        "SetNodePoolManagementRequestOut": "_container_77_SetNodePoolManagementRequestOut",
        "NodeLabelsIn": "_container_78_NodeLabelsIn",
        "NodeLabelsOut": "_container_79_NodeLabelsOut",
        "RecurringTimeWindowIn": "_container_80_RecurringTimeWindowIn",
        "RecurringTimeWindowOut": "_container_81_RecurringTimeWindowOut",
        "LoggingComponentConfigIn": "_container_82_LoggingComponentConfigIn",
        "LoggingComponentConfigOut": "_container_83_LoggingComponentConfigOut",
        "IntraNodeVisibilityConfigIn": "_container_84_IntraNodeVisibilityConfigIn",
        "IntraNodeVisibilityConfigOut": "_container_85_IntraNodeVisibilityConfigOut",
        "NetworkPerformanceConfigIn": "_container_86_NetworkPerformanceConfigIn",
        "NetworkPerformanceConfigOut": "_container_87_NetworkPerformanceConfigOut",
        "NodeTaintsIn": "_container_88_NodeTaintsIn",
        "NodeTaintsOut": "_container_89_NodeTaintsOut",
        "OperationIn": "_container_90_OperationIn",
        "OperationOut": "_container_91_OperationOut",
        "UpdateNodePoolRequestIn": "_container_92_UpdateNodePoolRequestIn",
        "UpdateNodePoolRequestOut": "_container_93_UpdateNodePoolRequestOut",
        "BlueGreenSettingsIn": "_container_94_BlueGreenSettingsIn",
        "BlueGreenSettingsOut": "_container_95_BlueGreenSettingsOut",
        "LoggingConfigIn": "_container_96_LoggingConfigIn",
        "LoggingConfigOut": "_container_97_LoggingConfigOut",
        "ListUsableSubnetworksResponseIn": "_container_98_ListUsableSubnetworksResponseIn",
        "ListUsableSubnetworksResponseOut": "_container_99_ListUsableSubnetworksResponseOut",
        "UsableSubnetworkSecondaryRangeIn": "_container_100_UsableSubnetworkSecondaryRangeIn",
        "UsableSubnetworkSecondaryRangeOut": "_container_101_UsableSubnetworkSecondaryRangeOut",
        "AuthenticatorGroupsConfigIn": "_container_102_AuthenticatorGroupsConfigIn",
        "AuthenticatorGroupsConfigOut": "_container_103_AuthenticatorGroupsConfigOut",
        "StatusIn": "_container_104_StatusIn",
        "StatusOut": "_container_105_StatusOut",
        "NodePoolAutoConfigIn": "_container_106_NodePoolAutoConfigIn",
        "NodePoolAutoConfigOut": "_container_107_NodePoolAutoConfigOut",
        "CidrBlockIn": "_container_108_CidrBlockIn",
        "CidrBlockOut": "_container_109_CidrBlockOut",
        "DNSConfigIn": "_container_110_DNSConfigIn",
        "DNSConfigOut": "_container_111_DNSConfigOut",
        "NotificationConfigIn": "_container_112_NotificationConfigIn",
        "NotificationConfigOut": "_container_113_NotificationConfigOut",
        "ResourceLabelsIn": "_container_114_ResourceLabelsIn",
        "ResourceLabelsOut": "_container_115_ResourceLabelsOut",
        "MaintenanceWindowIn": "_container_116_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_container_117_MaintenanceWindowOut",
        "PrivateClusterConfigIn": "_container_118_PrivateClusterConfigIn",
        "PrivateClusterConfigOut": "_container_119_PrivateClusterConfigOut",
        "GetJSONWebKeysResponseIn": "_container_120_GetJSONWebKeysResponseIn",
        "GetJSONWebKeysResponseOut": "_container_121_GetJSONWebKeysResponseOut",
        "NodeConfigDefaultsIn": "_container_122_NodeConfigDefaultsIn",
        "NodeConfigDefaultsOut": "_container_123_NodeConfigDefaultsOut",
        "SetNodePoolSizeRequestIn": "_container_124_SetNodePoolSizeRequestIn",
        "SetNodePoolSizeRequestOut": "_container_125_SetNodePoolSizeRequestOut",
        "ILBSubsettingConfigIn": "_container_126_ILBSubsettingConfigIn",
        "ILBSubsettingConfigOut": "_container_127_ILBSubsettingConfigOut",
        "ConfigConnectorConfigIn": "_container_128_ConfigConnectorConfigIn",
        "ConfigConnectorConfigOut": "_container_129_ConfigConnectorConfigOut",
        "EphemeralStorageLocalSsdConfigIn": "_container_130_EphemeralStorageLocalSsdConfigIn",
        "EphemeralStorageLocalSsdConfigOut": "_container_131_EphemeralStorageLocalSsdConfigOut",
        "PrivateClusterMasterGlobalAccessConfigIn": "_container_132_PrivateClusterMasterGlobalAccessConfigIn",
        "PrivateClusterMasterGlobalAccessConfigOut": "_container_133_PrivateClusterMasterGlobalAccessConfigOut",
        "ListNodePoolsResponseIn": "_container_134_ListNodePoolsResponseIn",
        "ListNodePoolsResponseOut": "_container_135_ListNodePoolsResponseOut",
        "NodeConfigIn": "_container_136_NodeConfigIn",
        "NodeConfigOut": "_container_137_NodeConfigOut",
        "IdentityServiceConfigIn": "_container_138_IdentityServiceConfigIn",
        "IdentityServiceConfigOut": "_container_139_IdentityServiceConfigOut",
        "ConfidentialNodesIn": "_container_140_ConfidentialNodesIn",
        "ConfidentialNodesOut": "_container_141_ConfidentialNodesOut",
        "FleetIn": "_container_142_FleetIn",
        "FleetOut": "_container_143_FleetOut",
        "OperationProgressIn": "_container_144_OperationProgressIn",
        "OperationProgressOut": "_container_145_OperationProgressOut",
        "BinaryAuthorizationIn": "_container_146_BinaryAuthorizationIn",
        "BinaryAuthorizationOut": "_container_147_BinaryAuthorizationOut",
        "PodCIDROverprovisionConfigIn": "_container_148_PodCIDROverprovisionConfigIn",
        "PodCIDROverprovisionConfigOut": "_container_149_PodCIDROverprovisionConfigOut",
        "LocalNvmeSsdBlockConfigIn": "_container_150_LocalNvmeSsdBlockConfigIn",
        "LocalNvmeSsdBlockConfigOut": "_container_151_LocalNvmeSsdBlockConfigOut",
        "NodePoolLoggingConfigIn": "_container_152_NodePoolLoggingConfigIn",
        "NodePoolLoggingConfigOut": "_container_153_NodePoolLoggingConfigOut",
        "MaxPodsConstraintIn": "_container_154_MaxPodsConstraintIn",
        "MaxPodsConstraintOut": "_container_155_MaxPodsConstraintOut",
        "AdditionalPodRangesConfigIn": "_container_156_AdditionalPodRangesConfigIn",
        "AdditionalPodRangesConfigOut": "_container_157_AdditionalPodRangesConfigOut",
        "MonitoringConfigIn": "_container_158_MonitoringConfigIn",
        "MonitoringConfigOut": "_container_159_MonitoringConfigOut",
        "NetworkConfigIn": "_container_160_NetworkConfigIn",
        "NetworkConfigOut": "_container_161_NetworkConfigOut",
        "MeshCertificatesIn": "_container_162_MeshCertificatesIn",
        "MeshCertificatesOut": "_container_163_MeshCertificatesOut",
        "SetMaintenancePolicyRequestIn": "_container_164_SetMaintenancePolicyRequestIn",
        "SetMaintenancePolicyRequestOut": "_container_165_SetMaintenancePolicyRequestOut",
        "ListOperationsResponseIn": "_container_166_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_container_167_ListOperationsResponseOut",
        "NetworkTagsIn": "_container_168_NetworkTagsIn",
        "NetworkTagsOut": "_container_169_NetworkTagsOut",
        "NodePoolIn": "_container_170_NodePoolIn",
        "NodePoolOut": "_container_171_NodePoolOut",
        "SetLocationsRequestIn": "_container_172_SetLocationsRequestIn",
        "SetLocationsRequestOut": "_container_173_SetLocationsRequestOut",
        "UsableSubnetworkIn": "_container_174_UsableSubnetworkIn",
        "UsableSubnetworkOut": "_container_175_UsableSubnetworkOut",
        "WorkloadMetadataConfigIn": "_container_176_WorkloadMetadataConfigIn",
        "WorkloadMetadataConfigOut": "_container_177_WorkloadMetadataConfigOut",
        "NodePoolAutoscalingIn": "_container_178_NodePoolAutoscalingIn",
        "NodePoolAutoscalingOut": "_container_179_NodePoolAutoscalingOut",
        "ConsumptionMeteringConfigIn": "_container_180_ConsumptionMeteringConfigIn",
        "ConsumptionMeteringConfigOut": "_container_181_ConsumptionMeteringConfigOut",
        "SetLoggingServiceRequestIn": "_container_182_SetLoggingServiceRequestIn",
        "SetLoggingServiceRequestOut": "_container_183_SetLoggingServiceRequestOut",
        "ClusterIn": "_container_184_ClusterIn",
        "ClusterOut": "_container_185_ClusterOut",
        "LoggingVariantConfigIn": "_container_186_LoggingVariantConfigIn",
        "LoggingVariantConfigOut": "_container_187_LoggingVariantConfigOut",
        "SetLegacyAbacRequestIn": "_container_188_SetLegacyAbacRequestIn",
        "SetLegacyAbacRequestOut": "_container_189_SetLegacyAbacRequestOut",
        "UpdateInfoIn": "_container_190_UpdateInfoIn",
        "UpdateInfoOut": "_container_191_UpdateInfoOut",
        "AcceleratorConfigIn": "_container_192_AcceleratorConfigIn",
        "AcceleratorConfigOut": "_container_193_AcceleratorConfigOut",
        "SandboxConfigIn": "_container_194_SandboxConfigIn",
        "SandboxConfigOut": "_container_195_SandboxConfigOut",
        "DatabaseEncryptionIn": "_container_196_DatabaseEncryptionIn",
        "DatabaseEncryptionOut": "_container_197_DatabaseEncryptionOut",
        "TimeWindowIn": "_container_198_TimeWindowIn",
        "TimeWindowOut": "_container_199_TimeWindowOut",
        "CreateNodePoolRequestIn": "_container_200_CreateNodePoolRequestIn",
        "CreateNodePoolRequestOut": "_container_201_CreateNodePoolRequestOut",
        "NodeKubeletConfigIn": "_container_202_NodeKubeletConfigIn",
        "NodeKubeletConfigOut": "_container_203_NodeKubeletConfigOut",
        "GcpFilestoreCsiDriverConfigIn": "_container_204_GcpFilestoreCsiDriverConfigIn",
        "GcpFilestoreCsiDriverConfigOut": "_container_205_GcpFilestoreCsiDriverConfigOut",
        "HttpCacheControlResponseHeaderIn": "_container_206_HttpCacheControlResponseHeaderIn",
        "HttpCacheControlResponseHeaderOut": "_container_207_HttpCacheControlResponseHeaderOut",
        "ServerConfigIn": "_container_208_ServerConfigIn",
        "ServerConfigOut": "_container_209_ServerConfigOut",
        "UpdateMasterRequestIn": "_container_210_UpdateMasterRequestIn",
        "UpdateMasterRequestOut": "_container_211_UpdateMasterRequestOut",
        "AutopilotIn": "_container_212_AutopilotIn",
        "AutopilotOut": "_container_213_AutopilotOut",
        "GcfsConfigIn": "_container_214_GcfsConfigIn",
        "GcfsConfigOut": "_container_215_GcfsConfigOut",
        "SetNodePoolAutoscalingRequestIn": "_container_216_SetNodePoolAutoscalingRequestIn",
        "SetNodePoolAutoscalingRequestOut": "_container_217_SetNodePoolAutoscalingRequestOut",
        "LegacyAbacIn": "_container_218_LegacyAbacIn",
        "LegacyAbacOut": "_container_219_LegacyAbacOut",
        "CloudRunConfigIn": "_container_220_CloudRunConfigIn",
        "CloudRunConfigOut": "_container_221_CloudRunConfigOut",
        "StandardRolloutPolicyIn": "_container_222_StandardRolloutPolicyIn",
        "StandardRolloutPolicyOut": "_container_223_StandardRolloutPolicyOut",
        "ShieldedInstanceConfigIn": "_container_224_ShieldedInstanceConfigIn",
        "ShieldedInstanceConfigOut": "_container_225_ShieldedInstanceConfigOut",
        "HorizontalPodAutoscalingIn": "_container_226_HorizontalPodAutoscalingIn",
        "HorizontalPodAutoscalingOut": "_container_227_HorizontalPodAutoscalingOut",
        "AddonsConfigIn": "_container_228_AddonsConfigIn",
        "AddonsConfigOut": "_container_229_AddonsConfigOut",
        "PlacementPolicyIn": "_container_230_PlacementPolicyIn",
        "PlacementPolicyOut": "_container_231_PlacementPolicyOut",
        "CompleteNodePoolUpgradeRequestIn": "_container_232_CompleteNodePoolUpgradeRequestIn",
        "CompleteNodePoolUpgradeRequestOut": "_container_233_CompleteNodePoolUpgradeRequestOut",
        "MasterAuthIn": "_container_234_MasterAuthIn",
        "MasterAuthOut": "_container_235_MasterAuthOut",
        "SetMasterAuthRequestIn": "_container_236_SetMasterAuthRequestIn",
        "SetMasterAuthRequestOut": "_container_237_SetMasterAuthRequestOut",
        "VerticalPodAutoscalingIn": "_container_238_VerticalPodAutoscalingIn",
        "VerticalPodAutoscalingOut": "_container_239_VerticalPodAutoscalingOut",
        "SetNetworkPolicyRequestIn": "_container_240_SetNetworkPolicyRequestIn",
        "SetNetworkPolicyRequestOut": "_container_241_SetNetworkPolicyRequestOut",
        "KubernetesDashboardIn": "_container_242_KubernetesDashboardIn",
        "KubernetesDashboardOut": "_container_243_KubernetesDashboardOut",
        "BlueGreenInfoIn": "_container_244_BlueGreenInfoIn",
        "BlueGreenInfoOut": "_container_245_BlueGreenInfoOut",
        "ManagedPrometheusConfigIn": "_container_246_ManagedPrometheusConfigIn",
        "ManagedPrometheusConfigOut": "_container_247_ManagedPrometheusConfigOut",
        "VirtualNICIn": "_container_248_VirtualNICIn",
        "VirtualNICOut": "_container_249_VirtualNICOut",
        "StatusConditionIn": "_container_250_StatusConditionIn",
        "StatusConditionOut": "_container_251_StatusConditionOut",
        "SetLabelsRequestIn": "_container_252_SetLabelsRequestIn",
        "SetLabelsRequestOut": "_container_253_SetLabelsRequestOut",
        "NodeNetworkConfigIn": "_container_254_NodeNetworkConfigIn",
        "NodeNetworkConfigOut": "_container_255_NodeNetworkConfigOut",
        "FilterIn": "_container_256_FilterIn",
        "FilterOut": "_container_257_FilterOut",
        "LinuxNodeConfigIn": "_container_258_LinuxNodeConfigIn",
        "LinuxNodeConfigOut": "_container_259_LinuxNodeConfigOut",
        "AutoprovisioningNodePoolDefaultsIn": "_container_260_AutoprovisioningNodePoolDefaultsIn",
        "AutoprovisioningNodePoolDefaultsOut": "_container_261_AutoprovisioningNodePoolDefaultsOut",
        "ClientCertificateConfigIn": "_container_262_ClientCertificateConfigIn",
        "ClientCertificateConfigOut": "_container_263_ClientCertificateConfigOut",
        "GPUSharingConfigIn": "_container_264_GPUSharingConfigIn",
        "GPUSharingConfigOut": "_container_265_GPUSharingConfigOut",
        "UpgradeEventIn": "_container_266_UpgradeEventIn",
        "UpgradeEventOut": "_container_267_UpgradeEventOut",
        "AutoUpgradeOptionsIn": "_container_268_AutoUpgradeOptionsIn",
        "AutoUpgradeOptionsOut": "_container_269_AutoUpgradeOptionsOut",
        "UpgradeAvailableEventIn": "_container_270_UpgradeAvailableEventIn",
        "UpgradeAvailableEventOut": "_container_271_UpgradeAvailableEventOut",
        "CompleteIPRotationRequestIn": "_container_272_CompleteIPRotationRequestIn",
        "CompleteIPRotationRequestOut": "_container_273_CompleteIPRotationRequestOut",
        "IPAllocationPolicyIn": "_container_274_IPAllocationPolicyIn",
        "IPAllocationPolicyOut": "_container_275_IPAllocationPolicyOut",
        "UpdateClusterRequestIn": "_container_276_UpdateClusterRequestIn",
        "UpdateClusterRequestOut": "_container_277_UpdateClusterRequestOut",
        "EmptyIn": "_container_278_EmptyIn",
        "EmptyOut": "_container_279_EmptyOut",
        "PubSubIn": "_container_280_PubSubIn",
        "PubSubOut": "_container_281_PubSubOut",
        "NodePoolDefaultsIn": "_container_282_NodePoolDefaultsIn",
        "NodePoolDefaultsOut": "_container_283_NodePoolDefaultsOut",
        "ReleaseChannelConfigIn": "_container_284_ReleaseChannelConfigIn",
        "ReleaseChannelConfigOut": "_container_285_ReleaseChannelConfigOut",
        "SecurityBulletinEventIn": "_container_286_SecurityBulletinEventIn",
        "SecurityBulletinEventOut": "_container_287_SecurityBulletinEventOut",
        "NetworkPolicyConfigIn": "_container_288_NetworkPolicyConfigIn",
        "NetworkPolicyConfigOut": "_container_289_NetworkPolicyConfigOut",
        "RollbackNodePoolUpgradeRequestIn": "_container_290_RollbackNodePoolUpgradeRequestIn",
        "RollbackNodePoolUpgradeRequestOut": "_container_291_RollbackNodePoolUpgradeRequestOut",
        "BigQueryDestinationIn": "_container_292_BigQueryDestinationIn",
        "BigQueryDestinationOut": "_container_293_BigQueryDestinationOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["MetricIn"] = t.struct(
        {
            "stringValue": t.string().optional(),
            "doubleValue": t.number().optional(),
            "intValue": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["MetricIn"])
    types["MetricOut"] = t.struct(
        {
            "stringValue": t.string().optional(),
            "doubleValue": t.number().optional(),
            "intValue": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricOut"])
    types["StartIPRotationRequestIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "clusterId": t.string().optional(),
            "rotateCredentials": t.boolean().optional(),
            "name": t.string().optional(),
            "zone": t.string().optional(),
        }
    ).named(renames["StartIPRotationRequestIn"])
    types["StartIPRotationRequestOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "clusterId": t.string().optional(),
            "rotateCredentials": t.boolean().optional(),
            "name": t.string().optional(),
            "zone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartIPRotationRequestOut"])
    types["FastSocketIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["FastSocketIn"]
    )
    types["FastSocketOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FastSocketOut"])
    types["ServiceExternalIPsConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["ServiceExternalIPsConfigIn"])
    types["ServiceExternalIPsConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceExternalIPsConfigOut"])
    types["ReservationAffinityIn"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "key": t.string().optional(),
            "consumeReservationType": t.string().optional(),
        }
    ).named(renames["ReservationAffinityIn"])
    types["ReservationAffinityOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "key": t.string().optional(),
            "consumeReservationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReservationAffinityOut"])
    types["CancelOperationRequestIn"] = t.struct(
        {
            "operationId": t.string().optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
        }
    ).named(renames["CancelOperationRequestIn"])
    types["CancelOperationRequestOut"] = t.struct(
        {
            "operationId": t.string().optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CancelOperationRequestOut"])
    types["ResourceUsageExportConfigIn"] = t.struct(
        {
            "enableNetworkEgressMetering": t.boolean().optional(),
            "consumptionMeteringConfig": t.proxy(
                renames["ConsumptionMeteringConfigIn"]
            ).optional(),
            "bigqueryDestination": t.proxy(renames["BigQueryDestinationIn"]).optional(),
        }
    ).named(renames["ResourceUsageExportConfigIn"])
    types["ResourceUsageExportConfigOut"] = t.struct(
        {
            "enableNetworkEgressMetering": t.boolean().optional(),
            "consumptionMeteringConfig": t.proxy(
                renames["ConsumptionMeteringConfigOut"]
            ).optional(),
            "bigqueryDestination": t.proxy(
                renames["BigQueryDestinationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceUsageExportConfigOut"])
    types["ShieldedNodesIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["ShieldedNodesIn"]
    )
    types["ShieldedNodesOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShieldedNodesOut"])
    types["SetAddonsConfigRequestIn"] = t.struct(
        {
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "addonsConfig": t.proxy(renames["AddonsConfigIn"]),
            "clusterId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SetAddonsConfigRequestIn"])
    types["SetAddonsConfigRequestOut"] = t.struct(
        {
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "addonsConfig": t.proxy(renames["AddonsConfigOut"]),
            "clusterId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetAddonsConfigRequestOut"])
    types["WorkloadIdentityConfigIn"] = t.struct(
        {"workloadPool": t.string().optional()}
    ).named(renames["WorkloadIdentityConfigIn"])
    types["WorkloadIdentityConfigOut"] = t.struct(
        {
            "workloadPool": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkloadIdentityConfigOut"])
    types["ReleaseChannelIn"] = t.struct({"channel": t.string().optional()}).named(
        renames["ReleaseChannelIn"]
    )
    types["ReleaseChannelOut"] = t.struct(
        {
            "channel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseChannelOut"])
    types["GetOpenIDConfigResponseIn"] = t.struct(
        {
            "grant_types": t.array(t.string()).optional(),
            "issuer": t.string().optional(),
            "claims_supported": t.array(t.string()).optional(),
            "response_types_supported": t.array(t.string()).optional(),
            "jwks_uri": t.string().optional(),
            "id_token_signing_alg_values_supported": t.array(t.string()).optional(),
            "cacheHeader": t.proxy(
                renames["HttpCacheControlResponseHeaderIn"]
            ).optional(),
            "subject_types_supported": t.array(t.string()).optional(),
        }
    ).named(renames["GetOpenIDConfigResponseIn"])
    types["GetOpenIDConfigResponseOut"] = t.struct(
        {
            "grant_types": t.array(t.string()).optional(),
            "issuer": t.string().optional(),
            "claims_supported": t.array(t.string()).optional(),
            "response_types_supported": t.array(t.string()).optional(),
            "jwks_uri": t.string().optional(),
            "id_token_signing_alg_values_supported": t.array(t.string()).optional(),
            "cacheHeader": t.proxy(
                renames["HttpCacheControlResponseHeaderOut"]
            ).optional(),
            "subject_types_supported": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetOpenIDConfigResponseOut"])
    types["JwkIn"] = t.struct(
        {
            "y": t.string().optional(),
            "n": t.string().optional(),
            "crv": t.string().optional(),
            "kty": t.string().optional(),
            "use": t.string().optional(),
            "alg": t.string().optional(),
            "kid": t.string().optional(),
            "e": t.string().optional(),
            "x": t.string().optional(),
        }
    ).named(renames["JwkIn"])
    types["JwkOut"] = t.struct(
        {
            "y": t.string().optional(),
            "n": t.string().optional(),
            "crv": t.string().optional(),
            "kty": t.string().optional(),
            "use": t.string().optional(),
            "alg": t.string().optional(),
            "kid": t.string().optional(),
            "e": t.string().optional(),
            "x": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwkOut"])
    types["NodeTaintIn"] = t.struct(
        {
            "effect": t.string().optional(),
            "value": t.string().optional(),
            "key": t.string().optional(),
        }
    ).named(renames["NodeTaintIn"])
    types["NodeTaintOut"] = t.struct(
        {
            "effect": t.string().optional(),
            "value": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeTaintOut"])
    types["ResourceLimitIn"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "maximum": t.string().optional(),
            "minimum": t.string().optional(),
        }
    ).named(renames["ResourceLimitIn"])
    types["ResourceLimitOut"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "maximum": t.string().optional(),
            "minimum": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceLimitOut"])
    types["MaintenanceExclusionOptionsIn"] = t.struct(
        {"scope": t.string().optional()}
    ).named(renames["MaintenanceExclusionOptionsIn"])
    types["MaintenanceExclusionOptionsOut"] = t.struct(
        {
            "scope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceExclusionOptionsOut"])
    types["GkeBackupAgentConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["GkeBackupAgentConfigIn"])
    types["GkeBackupAgentConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GkeBackupAgentConfigOut"])
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
    types["MasterAuthorizedNetworksConfigIn"] = t.struct(
        {
            "gcpPublicCidrsAccessEnabled": t.boolean().optional(),
            "enabled": t.boolean().optional(),
            "cidrBlocks": t.array(t.proxy(renames["CidrBlockIn"])).optional(),
        }
    ).named(renames["MasterAuthorizedNetworksConfigIn"])
    types["MasterAuthorizedNetworksConfigOut"] = t.struct(
        {
            "gcpPublicCidrsAccessEnabled": t.boolean().optional(),
            "enabled": t.boolean().optional(),
            "cidrBlocks": t.array(t.proxy(renames["CidrBlockOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MasterAuthorizedNetworksConfigOut"])
    types["SetMonitoringServiceRequestIn"] = t.struct(
        {
            "name": t.string().optional(),
            "monitoringService": t.string(),
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["SetMonitoringServiceRequestIn"])
    types["SetMonitoringServiceRequestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "monitoringService": t.string(),
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetMonitoringServiceRequestOut"])
    types["UpgradeSettingsIn"] = t.struct(
        {
            "maxUnavailable": t.integer().optional(),
            "strategy": t.string().optional(),
            "blueGreenSettings": t.proxy(renames["BlueGreenSettingsIn"]).optional(),
            "maxSurge": t.integer().optional(),
        }
    ).named(renames["UpgradeSettingsIn"])
    types["UpgradeSettingsOut"] = t.struct(
        {
            "maxUnavailable": t.integer().optional(),
            "strategy": t.string().optional(),
            "blueGreenSettings": t.proxy(renames["BlueGreenSettingsOut"]).optional(),
            "maxSurge": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeSettingsOut"])
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
    types["CostManagementConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["CostManagementConfigIn"])
    types["CostManagementConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CostManagementConfigOut"])
    types["CreateClusterRequestIn"] = t.struct(
        {
            "cluster": t.proxy(renames["ClusterIn"]),
            "projectId": t.string().optional(),
            "parent": t.string().optional(),
            "zone": t.string().optional(),
        }
    ).named(renames["CreateClusterRequestIn"])
    types["CreateClusterRequestOut"] = t.struct(
        {
            "cluster": t.proxy(renames["ClusterOut"]),
            "projectId": t.string().optional(),
            "parent": t.string().optional(),
            "zone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateClusterRequestOut"])
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
    types["HttpLoadBalancingIn"] = t.struct({"disabled": t.boolean().optional()}).named(
        renames["HttpLoadBalancingIn"]
    )
    types["HttpLoadBalancingOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpLoadBalancingOut"])
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
    types["WindowsNodeConfigIn"] = t.struct({"osVersion": t.string().optional()}).named(
        renames["WindowsNodeConfigIn"]
    )
    types["WindowsNodeConfigOut"] = t.struct(
        {
            "osVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WindowsNodeConfigOut"])
    types["AdvancedMachineFeaturesIn"] = t.struct(
        {"threadsPerCore": t.string().optional()}
    ).named(renames["AdvancedMachineFeaturesIn"])
    types["AdvancedMachineFeaturesOut"] = t.struct(
        {
            "threadsPerCore": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvancedMachineFeaturesOut"])
    types["GatewayAPIConfigIn"] = t.struct({"channel": t.string().optional()}).named(
        renames["GatewayAPIConfigIn"]
    )
    types["GatewayAPIConfigOut"] = t.struct(
        {
            "channel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GatewayAPIConfigOut"])
    types["DefaultSnatStatusIn"] = t.struct({"disabled": t.boolean().optional()}).named(
        renames["DefaultSnatStatusIn"]
    )
    types["DefaultSnatStatusOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DefaultSnatStatusOut"])
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
    types["MonitoringComponentConfigIn"] = t.struct(
        {"enableComponents": t.array(t.string()).optional()}
    ).named(renames["MonitoringComponentConfigIn"])
    types["MonitoringComponentConfigOut"] = t.struct(
        {
            "enableComponents": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoringComponentConfigOut"])
    types["GcePersistentDiskCsiDriverConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["GcePersistentDiskCsiDriverConfigIn"])
    types["GcePersistentDiskCsiDriverConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcePersistentDiskCsiDriverConfigOut"])
    types["DnsCacheConfigIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["DnsCacheConfigIn"]
    )
    types["DnsCacheConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsCacheConfigOut"])
    types["ClusterAutoscalingIn"] = t.struct(
        {
            "autoprovisioningLocations": t.array(t.string()).optional(),
            "enableNodeAutoprovisioning": t.boolean().optional(),
            "autoprovisioningNodePoolDefaults": t.proxy(
                renames["AutoprovisioningNodePoolDefaultsIn"]
            ).optional(),
            "resourceLimits": t.array(t.proxy(renames["ResourceLimitIn"])).optional(),
            "autoscalingProfile": t.string().optional(),
        }
    ).named(renames["ClusterAutoscalingIn"])
    types["ClusterAutoscalingOut"] = t.struct(
        {
            "autoprovisioningLocations": t.array(t.string()).optional(),
            "enableNodeAutoprovisioning": t.boolean().optional(),
            "autoprovisioningNodePoolDefaults": t.proxy(
                renames["AutoprovisioningNodePoolDefaultsOut"]
            ).optional(),
            "resourceLimits": t.array(t.proxy(renames["ResourceLimitOut"])).optional(),
            "autoscalingProfile": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterAutoscalingOut"])
    types["ClusterUpdateIn"] = t.struct(
        {
            "desiredCostManagementConfig": t.proxy(
                renames["CostManagementConfigIn"]
            ).optional(),
            "desiredMasterVersion": t.string().optional(),
            "desiredReleaseChannel": t.proxy(renames["ReleaseChannelIn"]).optional(),
            "etag": t.string().optional(),
            "desiredIntraNodeVisibilityConfig": t.proxy(
                renames["IntraNodeVisibilityConfigIn"]
            ).optional(),
            "desiredNodePoolLoggingConfig": t.proxy(
                renames["NodePoolLoggingConfigIn"]
            ).optional(),
            "desiredDatabaseEncryption": t.proxy(
                renames["DatabaseEncryptionIn"]
            ).optional(),
            "desiredImageType": t.string().optional(),
            "desiredNotificationConfig": t.proxy(
                renames["NotificationConfigIn"]
            ).optional(),
            "desiredNodePoolAutoscaling": t.proxy(
                renames["NodePoolAutoscalingIn"]
            ).optional(),
            "desiredMasterAuthorizedNetworksConfig": t.proxy(
                renames["MasterAuthorizedNetworksConfigIn"]
            ).optional(),
            "desiredDnsConfig": t.proxy(renames["DNSConfigIn"]).optional(),
            "desiredClusterAutoscaling": t.proxy(
                renames["ClusterAutoscalingIn"]
            ).optional(),
            "desiredLoggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "desiredNodeVersion": t.string().optional(),
            "desiredServiceExternalIpsConfig": t.proxy(
                renames["ServiceExternalIPsConfigIn"]
            ).optional(),
            "desiredBinaryAuthorization": t.proxy(
                renames["BinaryAuthorizationIn"]
            ).optional(),
            "desiredNodePoolAutoConfigNetworkTags": t.proxy(
                renames["NetworkTagsIn"]
            ).optional(),
            "desiredGatewayApiConfig": t.proxy(
                renames["GatewayAPIConfigIn"]
            ).optional(),
            "desiredL4ilbSubsettingConfig": t.proxy(
                renames["ILBSubsettingConfigIn"]
            ).optional(),
            "removedAdditionalPodRangesConfig": t.proxy(
                renames["AdditionalPodRangesConfigIn"]
            ).optional(),
            "desiredDefaultSnatStatus": t.proxy(
                renames["DefaultSnatStatusIn"]
            ).optional(),
            "desiredShieldedNodes": t.proxy(renames["ShieldedNodesIn"]).optional(),
            "desiredVerticalPodAutoscaling": t.proxy(
                renames["VerticalPodAutoscalingIn"]
            ).optional(),
            "desiredIdentityServiceConfig": t.proxy(
                renames["IdentityServiceConfigIn"]
            ).optional(),
            "desiredResourceUsageExportConfig": t.proxy(
                renames["ResourceUsageExportConfigIn"]
            ).optional(),
            "desiredGcfsConfig": t.proxy(renames["GcfsConfigIn"]).optional(),
            "desiredStackType": t.string().optional(),
            "desiredAuthenticatorGroupsConfig": t.proxy(
                renames["AuthenticatorGroupsConfigIn"]
            ).optional(),
            "desiredDatapathProvider": t.string().optional(),
            "desiredMeshCertificates": t.proxy(
                renames["MeshCertificatesIn"]
            ).optional(),
            "additionalPodRangesConfig": t.proxy(
                renames["AdditionalPodRangesConfigIn"]
            ).optional(),
            "desiredEnablePrivateEndpoint": t.boolean().optional(),
            "desiredLocations": t.array(t.string()).optional(),
            "desiredFleet": t.proxy(renames["FleetIn"]).optional(),
            "desiredPrivateClusterConfig": t.proxy(
                renames["PrivateClusterConfigIn"]
            ).optional(),
            "desiredAddonsConfig": t.proxy(renames["AddonsConfigIn"]).optional(),
            "desiredPrivateIpv6GoogleAccess": t.string().optional(),
            "desiredMonitoringConfig": t.proxy(
                renames["MonitoringConfigIn"]
            ).optional(),
            "desiredNodePoolId": t.string().optional(),
            "desiredLoggingService": t.string().optional(),
            "desiredMonitoringService": t.string().optional(),
            "desiredWorkloadIdentityConfig": t.proxy(
                renames["WorkloadIdentityConfigIn"]
            ).optional(),
        }
    ).named(renames["ClusterUpdateIn"])
    types["ClusterUpdateOut"] = t.struct(
        {
            "desiredCostManagementConfig": t.proxy(
                renames["CostManagementConfigOut"]
            ).optional(),
            "desiredMasterVersion": t.string().optional(),
            "desiredReleaseChannel": t.proxy(renames["ReleaseChannelOut"]).optional(),
            "etag": t.string().optional(),
            "desiredIntraNodeVisibilityConfig": t.proxy(
                renames["IntraNodeVisibilityConfigOut"]
            ).optional(),
            "desiredNodePoolLoggingConfig": t.proxy(
                renames["NodePoolLoggingConfigOut"]
            ).optional(),
            "desiredDatabaseEncryption": t.proxy(
                renames["DatabaseEncryptionOut"]
            ).optional(),
            "desiredImageType": t.string().optional(),
            "desiredNotificationConfig": t.proxy(
                renames["NotificationConfigOut"]
            ).optional(),
            "desiredNodePoolAutoscaling": t.proxy(
                renames["NodePoolAutoscalingOut"]
            ).optional(),
            "desiredMasterAuthorizedNetworksConfig": t.proxy(
                renames["MasterAuthorizedNetworksConfigOut"]
            ).optional(),
            "desiredDnsConfig": t.proxy(renames["DNSConfigOut"]).optional(),
            "desiredClusterAutoscaling": t.proxy(
                renames["ClusterAutoscalingOut"]
            ).optional(),
            "desiredLoggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "desiredNodeVersion": t.string().optional(),
            "desiredServiceExternalIpsConfig": t.proxy(
                renames["ServiceExternalIPsConfigOut"]
            ).optional(),
            "desiredBinaryAuthorization": t.proxy(
                renames["BinaryAuthorizationOut"]
            ).optional(),
            "desiredNodePoolAutoConfigNetworkTags": t.proxy(
                renames["NetworkTagsOut"]
            ).optional(),
            "desiredGatewayApiConfig": t.proxy(
                renames["GatewayAPIConfigOut"]
            ).optional(),
            "desiredL4ilbSubsettingConfig": t.proxy(
                renames["ILBSubsettingConfigOut"]
            ).optional(),
            "removedAdditionalPodRangesConfig": t.proxy(
                renames["AdditionalPodRangesConfigOut"]
            ).optional(),
            "desiredDefaultSnatStatus": t.proxy(
                renames["DefaultSnatStatusOut"]
            ).optional(),
            "desiredShieldedNodes": t.proxy(renames["ShieldedNodesOut"]).optional(),
            "desiredVerticalPodAutoscaling": t.proxy(
                renames["VerticalPodAutoscalingOut"]
            ).optional(),
            "desiredIdentityServiceConfig": t.proxy(
                renames["IdentityServiceConfigOut"]
            ).optional(),
            "desiredResourceUsageExportConfig": t.proxy(
                renames["ResourceUsageExportConfigOut"]
            ).optional(),
            "desiredGcfsConfig": t.proxy(renames["GcfsConfigOut"]).optional(),
            "desiredStackType": t.string().optional(),
            "desiredAuthenticatorGroupsConfig": t.proxy(
                renames["AuthenticatorGroupsConfigOut"]
            ).optional(),
            "desiredDatapathProvider": t.string().optional(),
            "desiredMeshCertificates": t.proxy(
                renames["MeshCertificatesOut"]
            ).optional(),
            "additionalPodRangesConfig": t.proxy(
                renames["AdditionalPodRangesConfigOut"]
            ).optional(),
            "desiredEnablePrivateEndpoint": t.boolean().optional(),
            "desiredLocations": t.array(t.string()).optional(),
            "desiredFleet": t.proxy(renames["FleetOut"]).optional(),
            "desiredPrivateClusterConfig": t.proxy(
                renames["PrivateClusterConfigOut"]
            ).optional(),
            "desiredAddonsConfig": t.proxy(renames["AddonsConfigOut"]).optional(),
            "desiredPrivateIpv6GoogleAccess": t.string().optional(),
            "desiredMonitoringConfig": t.proxy(
                renames["MonitoringConfigOut"]
            ).optional(),
            "desiredNodePoolId": t.string().optional(),
            "desiredLoggingService": t.string().optional(),
            "desiredMonitoringService": t.string().optional(),
            "desiredWorkloadIdentityConfig": t.proxy(
                renames["WorkloadIdentityConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterUpdateOut"])
    types["SetNodePoolManagementRequestIn"] = t.struct(
        {
            "nodePoolId": t.string().optional(),
            "zone": t.string().optional(),
            "management": t.proxy(renames["NodeManagementIn"]),
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
        }
    ).named(renames["SetNodePoolManagementRequestIn"])
    types["SetNodePoolManagementRequestOut"] = t.struct(
        {
            "nodePoolId": t.string().optional(),
            "zone": t.string().optional(),
            "management": t.proxy(renames["NodeManagementOut"]),
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetNodePoolManagementRequestOut"])
    types["NodeLabelsIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["NodeLabelsIn"])
    types["NodeLabelsOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeLabelsOut"])
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
    types["LoggingComponentConfigIn"] = t.struct(
        {"enableComponents": t.array(t.string()).optional()}
    ).named(renames["LoggingComponentConfigIn"])
    types["LoggingComponentConfigOut"] = t.struct(
        {
            "enableComponents": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoggingComponentConfigOut"])
    types["IntraNodeVisibilityConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["IntraNodeVisibilityConfigIn"])
    types["IntraNodeVisibilityConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntraNodeVisibilityConfigOut"])
    types["NetworkPerformanceConfigIn"] = t.struct(
        {"totalEgressBandwidthTier": t.string().optional()}
    ).named(renames["NetworkPerformanceConfigIn"])
    types["NetworkPerformanceConfigOut"] = t.struct(
        {
            "totalEgressBandwidthTier": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkPerformanceConfigOut"])
    types["NodeTaintsIn"] = t.struct(
        {"taints": t.array(t.proxy(renames["NodeTaintIn"])).optional()}
    ).named(renames["NodeTaintsIn"])
    types["NodeTaintsOut"] = t.struct(
        {
            "taints": t.array(t.proxy(renames["NodeTaintOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeTaintsOut"])
    types["OperationIn"] = t.struct(
        {
            "targetLink": t.string().optional(),
            "startTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "nodepoolConditions": t.array(
                t.proxy(renames["StatusConditionIn"])
            ).optional(),
            "endTime": t.string().optional(),
            "location": t.string().optional(),
            "status": t.string().optional(),
            "zone": t.string().optional(),
            "operationType": t.string().optional(),
            "clusterConditions": t.array(
                t.proxy(renames["StatusConditionIn"])
            ).optional(),
            "detail": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "targetLink": t.string().optional(),
            "startTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "nodepoolConditions": t.array(
                t.proxy(renames["StatusConditionOut"])
            ).optional(),
            "endTime": t.string().optional(),
            "location": t.string().optional(),
            "status": t.string().optional(),
            "zone": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "statusMessage": t.string().optional(),
            "operationType": t.string().optional(),
            "clusterConditions": t.array(
                t.proxy(renames["StatusConditionOut"])
            ).optional(),
            "detail": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["UpdateNodePoolRequestIn"] = t.struct(
        {
            "locations": t.array(t.string()).optional(),
            "nodePoolId": t.string().optional(),
            "resourceLabels": t.proxy(renames["ResourceLabelsIn"]).optional(),
            "loggingConfig": t.proxy(renames["NodePoolLoggingConfigIn"]).optional(),
            "gvnic": t.proxy(renames["VirtualNICIn"]).optional(),
            "imageType": t.string(),
            "fastSocket": t.proxy(renames["FastSocketIn"]).optional(),
            "nodeVersion": t.string(),
            "upgradeSettings": t.proxy(renames["UpgradeSettingsIn"]).optional(),
            "taints": t.proxy(renames["NodeTaintsIn"]).optional(),
            "tags": t.proxy(renames["NetworkTagsIn"]).optional(),
            "labels": t.proxy(renames["NodeLabelsIn"]).optional(),
            "clusterId": t.string().optional(),
            "gcfsConfig": t.proxy(renames["GcfsConfigIn"]).optional(),
            "kubeletConfig": t.proxy(renames["NodeKubeletConfigIn"]).optional(),
            "workloadMetadataConfig": t.proxy(
                renames["WorkloadMetadataConfigIn"]
            ).optional(),
            "nodeNetworkConfig": t.proxy(renames["NodeNetworkConfigIn"]).optional(),
            "zone": t.string().optional(),
            "windowsNodeConfig": t.proxy(renames["WindowsNodeConfigIn"]).optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "linuxNodeConfig": t.proxy(renames["LinuxNodeConfigIn"]).optional(),
            "confidentialNodes": t.proxy(renames["ConfidentialNodesIn"]).optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["UpdateNodePoolRequestIn"])
    types["UpdateNodePoolRequestOut"] = t.struct(
        {
            "locations": t.array(t.string()).optional(),
            "nodePoolId": t.string().optional(),
            "resourceLabels": t.proxy(renames["ResourceLabelsOut"]).optional(),
            "loggingConfig": t.proxy(renames["NodePoolLoggingConfigOut"]).optional(),
            "gvnic": t.proxy(renames["VirtualNICOut"]).optional(),
            "imageType": t.string(),
            "fastSocket": t.proxy(renames["FastSocketOut"]).optional(),
            "nodeVersion": t.string(),
            "upgradeSettings": t.proxy(renames["UpgradeSettingsOut"]).optional(),
            "taints": t.proxy(renames["NodeTaintsOut"]).optional(),
            "tags": t.proxy(renames["NetworkTagsOut"]).optional(),
            "labels": t.proxy(renames["NodeLabelsOut"]).optional(),
            "clusterId": t.string().optional(),
            "gcfsConfig": t.proxy(renames["GcfsConfigOut"]).optional(),
            "kubeletConfig": t.proxy(renames["NodeKubeletConfigOut"]).optional(),
            "workloadMetadataConfig": t.proxy(
                renames["WorkloadMetadataConfigOut"]
            ).optional(),
            "nodeNetworkConfig": t.proxy(renames["NodeNetworkConfigOut"]).optional(),
            "zone": t.string().optional(),
            "windowsNodeConfig": t.proxy(renames["WindowsNodeConfigOut"]).optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "linuxNodeConfig": t.proxy(renames["LinuxNodeConfigOut"]).optional(),
            "confidentialNodes": t.proxy(renames["ConfidentialNodesOut"]).optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateNodePoolRequestOut"])
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
    types["LoggingConfigIn"] = t.struct(
        {"componentConfig": t.proxy(renames["LoggingComponentConfigIn"]).optional()}
    ).named(renames["LoggingConfigIn"])
    types["LoggingConfigOut"] = t.struct(
        {
            "componentConfig": t.proxy(renames["LoggingComponentConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoggingConfigOut"])
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
    types["NodePoolAutoConfigIn"] = t.struct(
        {"networkTags": t.proxy(renames["NetworkTagsIn"]).optional()}
    ).named(renames["NodePoolAutoConfigIn"])
    types["NodePoolAutoConfigOut"] = t.struct(
        {
            "networkTags": t.proxy(renames["NetworkTagsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodePoolAutoConfigOut"])
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
    types["DNSConfigIn"] = t.struct(
        {
            "clusterDns": t.string().optional(),
            "clusterDnsDomain": t.string().optional(),
            "clusterDnsScope": t.string().optional(),
        }
    ).named(renames["DNSConfigIn"])
    types["DNSConfigOut"] = t.struct(
        {
            "clusterDns": t.string().optional(),
            "clusterDnsDomain": t.string().optional(),
            "clusterDnsScope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DNSConfigOut"])
    types["NotificationConfigIn"] = t.struct(
        {"pubsub": t.proxy(renames["PubSubIn"]).optional()}
    ).named(renames["NotificationConfigIn"])
    types["NotificationConfigOut"] = t.struct(
        {
            "pubsub": t.proxy(renames["PubSubOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationConfigOut"])
    types["ResourceLabelsIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["ResourceLabelsIn"])
    types["ResourceLabelsOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceLabelsOut"])
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
    types["PrivateClusterConfigIn"] = t.struct(
        {
            "privateEndpointSubnetwork": t.string().optional(),
            "privateEndpoint": t.string().optional(),
            "enablePrivateEndpoint": t.boolean().optional(),
            "masterGlobalAccessConfig": t.proxy(
                renames["PrivateClusterMasterGlobalAccessConfigIn"]
            ).optional(),
            "masterIpv4CidrBlock": t.string().optional(),
            "peeringName": t.string().optional(),
            "publicEndpoint": t.string().optional(),
            "enablePrivateNodes": t.boolean().optional(),
        }
    ).named(renames["PrivateClusterConfigIn"])
    types["PrivateClusterConfigOut"] = t.struct(
        {
            "privateEndpointSubnetwork": t.string().optional(),
            "privateEndpoint": t.string().optional(),
            "enablePrivateEndpoint": t.boolean().optional(),
            "masterGlobalAccessConfig": t.proxy(
                renames["PrivateClusterMasterGlobalAccessConfigOut"]
            ).optional(),
            "masterIpv4CidrBlock": t.string().optional(),
            "peeringName": t.string().optional(),
            "publicEndpoint": t.string().optional(),
            "enablePrivateNodes": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateClusterConfigOut"])
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
    types["SetNodePoolSizeRequestIn"] = t.struct(
        {
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "nodeCount": t.integer(),
            "projectId": t.string().optional(),
            "nodePoolId": t.string().optional(),
            "zone": t.string().optional(),
        }
    ).named(renames["SetNodePoolSizeRequestIn"])
    types["SetNodePoolSizeRequestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "nodeCount": t.integer(),
            "projectId": t.string().optional(),
            "nodePoolId": t.string().optional(),
            "zone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetNodePoolSizeRequestOut"])
    types["ILBSubsettingConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["ILBSubsettingConfigIn"])
    types["ILBSubsettingConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ILBSubsettingConfigOut"])
    types["ConfigConnectorConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["ConfigConnectorConfigIn"])
    types["ConfigConnectorConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigConnectorConfigOut"])
    types["EphemeralStorageLocalSsdConfigIn"] = t.struct(
        {"localSsdCount": t.integer().optional()}
    ).named(renames["EphemeralStorageLocalSsdConfigIn"])
    types["EphemeralStorageLocalSsdConfigOut"] = t.struct(
        {
            "localSsdCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EphemeralStorageLocalSsdConfigOut"])
    types["PrivateClusterMasterGlobalAccessConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["PrivateClusterMasterGlobalAccessConfigIn"])
    types["PrivateClusterMasterGlobalAccessConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateClusterMasterGlobalAccessConfigOut"])
    types["ListNodePoolsResponseIn"] = t.struct(
        {"nodePools": t.array(t.proxy(renames["NodePoolIn"])).optional()}
    ).named(renames["ListNodePoolsResponseIn"])
    types["ListNodePoolsResponseOut"] = t.struct(
        {
            "nodePools": t.array(t.proxy(renames["NodePoolOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNodePoolsResponseOut"])
    types["NodeConfigIn"] = t.struct(
        {
            "localNvmeSsdBlockConfig": t.proxy(
                renames["LocalNvmeSsdBlockConfigIn"]
            ).optional(),
            "machineType": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "nodeGroup": t.string().optional(),
            "imageType": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "reservationAffinity": t.proxy(renames["ReservationAffinityIn"]).optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorConfigIn"])).optional(),
            "fastSocket": t.proxy(renames["FastSocketIn"]).optional(),
            "windowsNodeConfig": t.proxy(renames["WindowsNodeConfigIn"]).optional(),
            "ephemeralStorageLocalSsdConfig": t.proxy(
                renames["EphemeralStorageLocalSsdConfigIn"]
            ).optional(),
            "taints": t.array(t.proxy(renames["NodeTaintIn"])).optional(),
            "diskType": t.string().optional(),
            "sandboxConfig": t.proxy(renames["SandboxConfigIn"]).optional(),
            "gcfsConfig": t.proxy(renames["GcfsConfigIn"]).optional(),
            "serviceAccount": t.string().optional(),
            "resourceLabels": t.struct({"_": t.string().optional()}).optional(),
            "kubeletConfig": t.proxy(renames["NodeKubeletConfigIn"]).optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigIn"]
            ).optional(),
            "preemptible": t.boolean().optional(),
            "confidentialNodes": t.proxy(renames["ConfidentialNodesIn"]).optional(),
            "localSsdCount": t.integer().optional(),
            "loggingConfig": t.proxy(renames["NodePoolLoggingConfigIn"]).optional(),
            "diskSizeGb": t.integer().optional(),
            "advancedMachineFeatures": t.proxy(
                renames["AdvancedMachineFeaturesIn"]
            ).optional(),
            "minCpuPlatform": t.string().optional(),
            "spot": t.boolean().optional(),
            "linuxNodeConfig": t.proxy(renames["LinuxNodeConfigIn"]).optional(),
            "workloadMetadataConfig": t.proxy(
                renames["WorkloadMetadataConfigIn"]
            ).optional(),
            "bootDiskKmsKey": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "gvnic": t.proxy(renames["VirtualNICIn"]).optional(),
            "oauthScopes": t.array(t.string()).optional(),
        }
    ).named(renames["NodeConfigIn"])
    types["NodeConfigOut"] = t.struct(
        {
            "localNvmeSsdBlockConfig": t.proxy(
                renames["LocalNvmeSsdBlockConfigOut"]
            ).optional(),
            "machineType": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "nodeGroup": t.string().optional(),
            "imageType": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "reservationAffinity": t.proxy(
                renames["ReservationAffinityOut"]
            ).optional(),
            "accelerators": t.array(
                t.proxy(renames["AcceleratorConfigOut"])
            ).optional(),
            "fastSocket": t.proxy(renames["FastSocketOut"]).optional(),
            "windowsNodeConfig": t.proxy(renames["WindowsNodeConfigOut"]).optional(),
            "ephemeralStorageLocalSsdConfig": t.proxy(
                renames["EphemeralStorageLocalSsdConfigOut"]
            ).optional(),
            "taints": t.array(t.proxy(renames["NodeTaintOut"])).optional(),
            "diskType": t.string().optional(),
            "sandboxConfig": t.proxy(renames["SandboxConfigOut"]).optional(),
            "gcfsConfig": t.proxy(renames["GcfsConfigOut"]).optional(),
            "serviceAccount": t.string().optional(),
            "resourceLabels": t.struct({"_": t.string().optional()}).optional(),
            "kubeletConfig": t.proxy(renames["NodeKubeletConfigOut"]).optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigOut"]
            ).optional(),
            "preemptible": t.boolean().optional(),
            "confidentialNodes": t.proxy(renames["ConfidentialNodesOut"]).optional(),
            "localSsdCount": t.integer().optional(),
            "loggingConfig": t.proxy(renames["NodePoolLoggingConfigOut"]).optional(),
            "diskSizeGb": t.integer().optional(),
            "advancedMachineFeatures": t.proxy(
                renames["AdvancedMachineFeaturesOut"]
            ).optional(),
            "minCpuPlatform": t.string().optional(),
            "spot": t.boolean().optional(),
            "linuxNodeConfig": t.proxy(renames["LinuxNodeConfigOut"]).optional(),
            "workloadMetadataConfig": t.proxy(
                renames["WorkloadMetadataConfigOut"]
            ).optional(),
            "bootDiskKmsKey": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "gvnic": t.proxy(renames["VirtualNICOut"]).optional(),
            "oauthScopes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeConfigOut"])
    types["IdentityServiceConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["IdentityServiceConfigIn"])
    types["IdentityServiceConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityServiceConfigOut"])
    types["ConfidentialNodesIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["ConfidentialNodesIn"]
    )
    types["ConfidentialNodesOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfidentialNodesOut"])
    types["FleetIn"] = t.struct(
        {
            "project": t.string().optional(),
            "membership": t.string().optional(),
            "preRegistered": t.boolean().optional(),
        }
    ).named(renames["FleetIn"])
    types["FleetOut"] = t.struct(
        {
            "project": t.string().optional(),
            "membership": t.string().optional(),
            "preRegistered": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FleetOut"])
    types["OperationProgressIn"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "name": t.string().optional(),
            "stages": t.array(t.proxy(renames["OperationProgressIn"])).optional(),
            "status": t.string().optional(),
        }
    ).named(renames["OperationProgressIn"])
    types["OperationProgressOut"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "name": t.string().optional(),
            "stages": t.array(t.proxy(renames["OperationProgressOut"])).optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationProgressOut"])
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
    types["PodCIDROverprovisionConfigIn"] = t.struct(
        {"disable": t.boolean().optional()}
    ).named(renames["PodCIDROverprovisionConfigIn"])
    types["PodCIDROverprovisionConfigOut"] = t.struct(
        {
            "disable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PodCIDROverprovisionConfigOut"])
    types["LocalNvmeSsdBlockConfigIn"] = t.struct(
        {"localSsdCount": t.integer().optional()}
    ).named(renames["LocalNvmeSsdBlockConfigIn"])
    types["LocalNvmeSsdBlockConfigOut"] = t.struct(
        {
            "localSsdCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalNvmeSsdBlockConfigOut"])
    types["NodePoolLoggingConfigIn"] = t.struct(
        {"variantConfig": t.proxy(renames["LoggingVariantConfigIn"]).optional()}
    ).named(renames["NodePoolLoggingConfigIn"])
    types["NodePoolLoggingConfigOut"] = t.struct(
        {
            "variantConfig": t.proxy(renames["LoggingVariantConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodePoolLoggingConfigOut"])
    types["MaxPodsConstraintIn"] = t.struct(
        {"maxPodsPerNode": t.string().optional()}
    ).named(renames["MaxPodsConstraintIn"])
    types["MaxPodsConstraintOut"] = t.struct(
        {
            "maxPodsPerNode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaxPodsConstraintOut"])
    types["AdditionalPodRangesConfigIn"] = t.struct(
        {"podRangeNames": t.array(t.string()).optional()}
    ).named(renames["AdditionalPodRangesConfigIn"])
    types["AdditionalPodRangesConfigOut"] = t.struct(
        {
            "podRangeNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdditionalPodRangesConfigOut"])
    types["MonitoringConfigIn"] = t.struct(
        {
            "componentConfig": t.proxy(
                renames["MonitoringComponentConfigIn"]
            ).optional(),
            "managedPrometheusConfig": t.proxy(
                renames["ManagedPrometheusConfigIn"]
            ).optional(),
        }
    ).named(renames["MonitoringConfigIn"])
    types["MonitoringConfigOut"] = t.struct(
        {
            "componentConfig": t.proxy(
                renames["MonitoringComponentConfigOut"]
            ).optional(),
            "managedPrometheusConfig": t.proxy(
                renames["ManagedPrometheusConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoringConfigOut"])
    types["NetworkConfigIn"] = t.struct(
        {
            "enableIntraNodeVisibility": t.boolean().optional(),
            "enableL4ilbSubsetting": t.boolean().optional(),
            "privateIpv6GoogleAccess": t.string().optional(),
            "gatewayApiConfig": t.proxy(renames["GatewayAPIConfigIn"]).optional(),
            "defaultSnatStatus": t.proxy(renames["DefaultSnatStatusIn"]).optional(),
            "dnsConfig": t.proxy(renames["DNSConfigIn"]).optional(),
            "network": t.string().optional(),
            "datapathProvider": t.string().optional(),
            "subnetwork": t.string().optional(),
            "serviceExternalIpsConfig": t.proxy(
                renames["ServiceExternalIPsConfigIn"]
            ).optional(),
        }
    ).named(renames["NetworkConfigIn"])
    types["NetworkConfigOut"] = t.struct(
        {
            "enableIntraNodeVisibility": t.boolean().optional(),
            "enableL4ilbSubsetting": t.boolean().optional(),
            "privateIpv6GoogleAccess": t.string().optional(),
            "gatewayApiConfig": t.proxy(renames["GatewayAPIConfigOut"]).optional(),
            "defaultSnatStatus": t.proxy(renames["DefaultSnatStatusOut"]).optional(),
            "dnsConfig": t.proxy(renames["DNSConfigOut"]).optional(),
            "network": t.string().optional(),
            "datapathProvider": t.string().optional(),
            "subnetwork": t.string().optional(),
            "serviceExternalIpsConfig": t.proxy(
                renames["ServiceExternalIPsConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConfigOut"])
    types["MeshCertificatesIn"] = t.struct(
        {"enableCertificates": t.boolean().optional()}
    ).named(renames["MeshCertificatesIn"])
    types["MeshCertificatesOut"] = t.struct(
        {
            "enableCertificates": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MeshCertificatesOut"])
    types["SetMaintenancePolicyRequestIn"] = t.struct(
        {
            "projectId": t.string(),
            "name": t.string().optional(),
            "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
            "clusterId": t.string(),
            "zone": t.string(),
        }
    ).named(renames["SetMaintenancePolicyRequestIn"])
    types["SetMaintenancePolicyRequestOut"] = t.struct(
        {
            "projectId": t.string(),
            "name": t.string().optional(),
            "maintenancePolicy": t.proxy(renames["MaintenancePolicyOut"]),
            "clusterId": t.string(),
            "zone": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetMaintenancePolicyRequestOut"])
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
    types["NetworkTagsIn"] = t.struct({"tags": t.array(t.string()).optional()}).named(
        renames["NetworkTagsIn"]
    )
    types["NetworkTagsOut"] = t.struct(
        {
            "tags": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkTagsOut"])
    types["NodePoolIn"] = t.struct(
        {
            "instanceGroupUrls": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "maxPodsConstraint": t.proxy(renames["MaxPodsConstraintIn"]).optional(),
            "autoscaling": t.proxy(renames["NodePoolAutoscalingIn"]).optional(),
            "upgradeSettings": t.proxy(renames["UpgradeSettingsIn"]).optional(),
            "initialNodeCount": t.integer().optional(),
            "config": t.proxy(renames["NodeConfigIn"]).optional(),
            "placementPolicy": t.proxy(renames["PlacementPolicyIn"]).optional(),
            "networkConfig": t.proxy(renames["NodeNetworkConfigIn"]).optional(),
            "conditions": t.array(t.proxy(renames["StatusConditionIn"])).optional(),
            "podIpv4CidrSize": t.integer().optional(),
            "status": t.string().optional(),
            "management": t.proxy(renames["NodeManagementIn"]).optional(),
            "selfLink": t.string().optional(),
            "statusMessage": t.string().optional(),
            "etag": t.string().optional(),
            "locations": t.array(t.string()).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["NodePoolIn"])
    types["NodePoolOut"] = t.struct(
        {
            "instanceGroupUrls": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "maxPodsConstraint": t.proxy(renames["MaxPodsConstraintOut"]).optional(),
            "autoscaling": t.proxy(renames["NodePoolAutoscalingOut"]).optional(),
            "updateInfo": t.proxy(renames["UpdateInfoOut"]).optional(),
            "upgradeSettings": t.proxy(renames["UpgradeSettingsOut"]).optional(),
            "initialNodeCount": t.integer().optional(),
            "config": t.proxy(renames["NodeConfigOut"]).optional(),
            "placementPolicy": t.proxy(renames["PlacementPolicyOut"]).optional(),
            "networkConfig": t.proxy(renames["NodeNetworkConfigOut"]).optional(),
            "conditions": t.array(t.proxy(renames["StatusConditionOut"])).optional(),
            "podIpv4CidrSize": t.integer().optional(),
            "status": t.string().optional(),
            "management": t.proxy(renames["NodeManagementOut"]).optional(),
            "selfLink": t.string().optional(),
            "statusMessage": t.string().optional(),
            "etag": t.string().optional(),
            "locations": t.array(t.string()).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodePoolOut"])
    types["SetLocationsRequestIn"] = t.struct(
        {
            "name": t.string().optional(),
            "zone": t.string().optional(),
            "locations": t.array(t.string()),
            "projectId": t.string().optional(),
            "clusterId": t.string().optional(),
        }
    ).named(renames["SetLocationsRequestIn"])
    types["SetLocationsRequestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "zone": t.string().optional(),
            "locations": t.array(t.string()),
            "projectId": t.string().optional(),
            "clusterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetLocationsRequestOut"])
    types["UsableSubnetworkIn"] = t.struct(
        {
            "subnetwork": t.string().optional(),
            "network": t.string().optional(),
            "secondaryIpRanges": t.array(
                t.proxy(renames["UsableSubnetworkSecondaryRangeIn"])
            ).optional(),
            "ipCidrRange": t.string().optional(),
            "statusMessage": t.string().optional(),
        }
    ).named(renames["UsableSubnetworkIn"])
    types["UsableSubnetworkOut"] = t.struct(
        {
            "subnetwork": t.string().optional(),
            "network": t.string().optional(),
            "secondaryIpRanges": t.array(
                t.proxy(renames["UsableSubnetworkSecondaryRangeOut"])
            ).optional(),
            "ipCidrRange": t.string().optional(),
            "statusMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsableSubnetworkOut"])
    types["WorkloadMetadataConfigIn"] = t.struct({"mode": t.string().optional()}).named(
        renames["WorkloadMetadataConfigIn"]
    )
    types["WorkloadMetadataConfigOut"] = t.struct(
        {
            "mode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkloadMetadataConfigOut"])
    types["NodePoolAutoscalingIn"] = t.struct(
        {
            "totalMaxNodeCount": t.integer().optional(),
            "totalMinNodeCount": t.integer().optional(),
            "maxNodeCount": t.integer().optional(),
            "autoprovisioned": t.boolean().optional(),
            "locationPolicy": t.string().optional(),
            "enabled": t.boolean().optional(),
            "minNodeCount": t.integer().optional(),
        }
    ).named(renames["NodePoolAutoscalingIn"])
    types["NodePoolAutoscalingOut"] = t.struct(
        {
            "totalMaxNodeCount": t.integer().optional(),
            "totalMinNodeCount": t.integer().optional(),
            "maxNodeCount": t.integer().optional(),
            "autoprovisioned": t.boolean().optional(),
            "locationPolicy": t.string().optional(),
            "enabled": t.boolean().optional(),
            "minNodeCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodePoolAutoscalingOut"])
    types["ConsumptionMeteringConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["ConsumptionMeteringConfigIn"])
    types["ConsumptionMeteringConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsumptionMeteringConfigOut"])
    types["SetLoggingServiceRequestIn"] = t.struct(
        {
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "loggingService": t.string(),
        }
    ).named(renames["SetLoggingServiceRequestIn"])
    types["SetLoggingServiceRequestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "loggingService": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetLoggingServiceRequestOut"])
    types["ClusterIn"] = t.struct(
        {
            "initialNodeCount": t.integer().optional(),
            "location": t.string().optional(),
            "instanceGroupUrls": t.array(t.string()).optional(),
            "shieldedNodes": t.proxy(renames["ShieldedNodesIn"]).optional(),
            "enableKubernetesAlpha": t.boolean().optional(),
            "fleet": t.proxy(renames["FleetIn"]).optional(),
            "costManagementConfig": t.proxy(
                renames["CostManagementConfigIn"]
            ).optional(),
            "nodeConfig": t.proxy(renames["NodeConfigIn"]).optional(),
            "workloadIdentityConfig": t.proxy(
                renames["WorkloadIdentityConfigIn"]
            ).optional(),
            "tpuIpv4CidrBlock": t.string().optional(),
            "currentNodeVersion": t.string().optional(),
            "subnetwork": t.string().optional(),
            "locations": t.array(t.string()).optional(),
            "verticalPodAutoscaling": t.proxy(
                renames["VerticalPodAutoscalingIn"]
            ).optional(),
            "nodeIpv4CidrSize": t.integer().optional(),
            "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
            "resourceUsageExportConfig": t.proxy(
                renames["ResourceUsageExportConfigIn"]
            ).optional(),
            "addonsConfig": t.proxy(renames["AddonsConfigIn"]).optional(),
            "network": t.string().optional(),
            "meshCertificates": t.proxy(renames["MeshCertificatesIn"]).optional(),
            "createTime": t.string().optional(),
            "initialClusterVersion": t.string().optional(),
            "enableTpu": t.boolean().optional(),
            "clusterIpv4Cidr": t.string().optional(),
            "masterAuthorizedNetworksConfig": t.proxy(
                renames["MasterAuthorizedNetworksConfigIn"]
            ).optional(),
            "loggingService": t.string().optional(),
            "confidentialNodes": t.proxy(renames["ConfidentialNodesIn"]).optional(),
            "masterAuth": t.proxy(renames["MasterAuthIn"]).optional(),
            "endpoint": t.string().optional(),
            "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]).optional(),
            "expireTime": t.string().optional(),
            "autoscaling": t.proxy(renames["ClusterAutoscalingIn"]).optional(),
            "identityServiceConfig": t.proxy(
                renames["IdentityServiceConfigIn"]
            ).optional(),
            "nodePools": t.array(t.proxy(renames["NodePoolIn"])).optional(),
            "nodePoolAutoConfig": t.proxy(renames["NodePoolAutoConfigIn"]).optional(),
            "conditions": t.array(t.proxy(renames["StatusConditionIn"])).optional(),
            "notificationConfig": t.proxy(renames["NotificationConfigIn"]).optional(),
            "description": t.string().optional(),
            "monitoringConfig": t.proxy(renames["MonitoringConfigIn"]).optional(),
            "monitoringService": t.string().optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigIn"]).optional(),
            "defaultMaxPodsConstraint": t.proxy(
                renames["MaxPodsConstraintIn"]
            ).optional(),
            "zone": t.string().optional(),
            "legacyAbac": t.proxy(renames["LegacyAbacIn"]).optional(),
            "labelFingerprint": t.string().optional(),
            "ipAllocationPolicy": t.proxy(renames["IPAllocationPolicyIn"]).optional(),
            "nodePoolDefaults": t.proxy(renames["NodePoolDefaultsIn"]).optional(),
            "currentNodeCount": t.integer().optional(),
            "autopilot": t.proxy(renames["AutopilotIn"]).optional(),
            "servicesIpv4Cidr": t.string().optional(),
            "databaseEncryption": t.proxy(renames["DatabaseEncryptionIn"]).optional(),
            "currentMasterVersion": t.string().optional(),
            "authenticatorGroupsConfig": t.proxy(
                renames["AuthenticatorGroupsConfigIn"]
            ).optional(),
            "networkPolicy": t.proxy(renames["NetworkPolicyIn"]).optional(),
            "releaseChannel": t.proxy(renames["ReleaseChannelIn"]).optional(),
            "etag": t.string().optional(),
            "status": t.string().optional(),
            "name": t.string().optional(),
            "privateClusterConfig": t.proxy(
                renames["PrivateClusterConfigIn"]
            ).optional(),
            "statusMessage": t.string().optional(),
            "selfLink": t.string().optional(),
            "binaryAuthorization": t.proxy(renames["BinaryAuthorizationIn"]).optional(),
            "resourceLabels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ClusterIn"])
    types["ClusterOut"] = t.struct(
        {
            "initialNodeCount": t.integer().optional(),
            "location": t.string().optional(),
            "instanceGroupUrls": t.array(t.string()).optional(),
            "shieldedNodes": t.proxy(renames["ShieldedNodesOut"]).optional(),
            "enableKubernetesAlpha": t.boolean().optional(),
            "fleet": t.proxy(renames["FleetOut"]).optional(),
            "costManagementConfig": t.proxy(
                renames["CostManagementConfigOut"]
            ).optional(),
            "nodeConfig": t.proxy(renames["NodeConfigOut"]).optional(),
            "workloadIdentityConfig": t.proxy(
                renames["WorkloadIdentityConfigOut"]
            ).optional(),
            "tpuIpv4CidrBlock": t.string().optional(),
            "currentNodeVersion": t.string().optional(),
            "subnetwork": t.string().optional(),
            "locations": t.array(t.string()).optional(),
            "verticalPodAutoscaling": t.proxy(
                renames["VerticalPodAutoscalingOut"]
            ).optional(),
            "nodeIpv4CidrSize": t.integer().optional(),
            "networkConfig": t.proxy(renames["NetworkConfigOut"]).optional(),
            "resourceUsageExportConfig": t.proxy(
                renames["ResourceUsageExportConfigOut"]
            ).optional(),
            "addonsConfig": t.proxy(renames["AddonsConfigOut"]).optional(),
            "network": t.string().optional(),
            "meshCertificates": t.proxy(renames["MeshCertificatesOut"]).optional(),
            "createTime": t.string().optional(),
            "initialClusterVersion": t.string().optional(),
            "enableTpu": t.boolean().optional(),
            "clusterIpv4Cidr": t.string().optional(),
            "masterAuthorizedNetworksConfig": t.proxy(
                renames["MasterAuthorizedNetworksConfigOut"]
            ).optional(),
            "loggingService": t.string().optional(),
            "confidentialNodes": t.proxy(renames["ConfidentialNodesOut"]).optional(),
            "masterAuth": t.proxy(renames["MasterAuthOut"]).optional(),
            "endpoint": t.string().optional(),
            "maintenancePolicy": t.proxy(renames["MaintenancePolicyOut"]).optional(),
            "expireTime": t.string().optional(),
            "autoscaling": t.proxy(renames["ClusterAutoscalingOut"]).optional(),
            "identityServiceConfig": t.proxy(
                renames["IdentityServiceConfigOut"]
            ).optional(),
            "nodePools": t.array(t.proxy(renames["NodePoolOut"])).optional(),
            "nodePoolAutoConfig": t.proxy(renames["NodePoolAutoConfigOut"]).optional(),
            "conditions": t.array(t.proxy(renames["StatusConditionOut"])).optional(),
            "notificationConfig": t.proxy(renames["NotificationConfigOut"]).optional(),
            "description": t.string().optional(),
            "monitoringConfig": t.proxy(renames["MonitoringConfigOut"]).optional(),
            "monitoringService": t.string().optional(),
            "id": t.string().optional(),
            "loggingConfig": t.proxy(renames["LoggingConfigOut"]).optional(),
            "defaultMaxPodsConstraint": t.proxy(
                renames["MaxPodsConstraintOut"]
            ).optional(),
            "zone": t.string().optional(),
            "legacyAbac": t.proxy(renames["LegacyAbacOut"]).optional(),
            "labelFingerprint": t.string().optional(),
            "ipAllocationPolicy": t.proxy(renames["IPAllocationPolicyOut"]).optional(),
            "nodePoolDefaults": t.proxy(renames["NodePoolDefaultsOut"]).optional(),
            "currentNodeCount": t.integer().optional(),
            "autopilot": t.proxy(renames["AutopilotOut"]).optional(),
            "servicesIpv4Cidr": t.string().optional(),
            "databaseEncryption": t.proxy(renames["DatabaseEncryptionOut"]).optional(),
            "currentMasterVersion": t.string().optional(),
            "authenticatorGroupsConfig": t.proxy(
                renames["AuthenticatorGroupsConfigOut"]
            ).optional(),
            "networkPolicy": t.proxy(renames["NetworkPolicyOut"]).optional(),
            "releaseChannel": t.proxy(renames["ReleaseChannelOut"]).optional(),
            "etag": t.string().optional(),
            "status": t.string().optional(),
            "name": t.string().optional(),
            "privateClusterConfig": t.proxy(
                renames["PrivateClusterConfigOut"]
            ).optional(),
            "statusMessage": t.string().optional(),
            "selfLink": t.string().optional(),
            "binaryAuthorization": t.proxy(
                renames["BinaryAuthorizationOut"]
            ).optional(),
            "resourceLabels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterOut"])
    types["LoggingVariantConfigIn"] = t.struct(
        {"variant": t.string().optional()}
    ).named(renames["LoggingVariantConfigIn"])
    types["LoggingVariantConfigOut"] = t.struct(
        {
            "variant": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoggingVariantConfigOut"])
    types["SetLegacyAbacRequestIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
            "enabled": t.boolean(),
            "name": t.string().optional(),
        }
    ).named(renames["SetLegacyAbacRequestIn"])
    types["SetLegacyAbacRequestOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
            "enabled": t.boolean(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetLegacyAbacRequestOut"])
    types["UpdateInfoIn"] = t.struct(
        {"blueGreenInfo": t.proxy(renames["BlueGreenInfoIn"]).optional()}
    ).named(renames["UpdateInfoIn"])
    types["UpdateInfoOut"] = t.struct(
        {
            "blueGreenInfo": t.proxy(renames["BlueGreenInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateInfoOut"])
    types["AcceleratorConfigIn"] = t.struct(
        {
            "gpuSharingConfig": t.proxy(renames["GPUSharingConfigIn"]).optional(),
            "acceleratorType": t.string().optional(),
            "acceleratorCount": t.string().optional(),
            "gpuPartitionSize": t.string().optional(),
        }
    ).named(renames["AcceleratorConfigIn"])
    types["AcceleratorConfigOut"] = t.struct(
        {
            "gpuSharingConfig": t.proxy(renames["GPUSharingConfigOut"]).optional(),
            "acceleratorType": t.string().optional(),
            "acceleratorCount": t.string().optional(),
            "gpuPartitionSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceleratorConfigOut"])
    types["SandboxConfigIn"] = t.struct({"type": t.string().optional()}).named(
        renames["SandboxConfigIn"]
    )
    types["SandboxConfigOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SandboxConfigOut"])
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
    types["TimeWindowIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "maintenanceExclusionOptions": t.proxy(
                renames["MaintenanceExclusionOptionsIn"]
            ).optional(),
        }
    ).named(renames["TimeWindowIn"])
    types["TimeWindowOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "maintenanceExclusionOptions": t.proxy(
                renames["MaintenanceExclusionOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeWindowOut"])
    types["CreateNodePoolRequestIn"] = t.struct(
        {
            "nodePool": t.proxy(renames["NodePoolIn"]),
            "clusterId": t.string().optional(),
            "parent": t.string().optional(),
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
        }
    ).named(renames["CreateNodePoolRequestIn"])
    types["CreateNodePoolRequestOut"] = t.struct(
        {
            "nodePool": t.proxy(renames["NodePoolOut"]),
            "clusterId": t.string().optional(),
            "parent": t.string().optional(),
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateNodePoolRequestOut"])
    types["NodeKubeletConfigIn"] = t.struct(
        {
            "cpuCfsQuota": t.boolean().optional(),
            "cpuCfsQuotaPeriod": t.string().optional(),
            "cpuManagerPolicy": t.string().optional(),
            "podPidsLimit": t.string().optional(),
        }
    ).named(renames["NodeKubeletConfigIn"])
    types["NodeKubeletConfigOut"] = t.struct(
        {
            "cpuCfsQuota": t.boolean().optional(),
            "cpuCfsQuotaPeriod": t.string().optional(),
            "cpuManagerPolicy": t.string().optional(),
            "podPidsLimit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeKubeletConfigOut"])
    types["GcpFilestoreCsiDriverConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["GcpFilestoreCsiDriverConfigIn"])
    types["GcpFilestoreCsiDriverConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcpFilestoreCsiDriverConfigOut"])
    types["HttpCacheControlResponseHeaderIn"] = t.struct(
        {
            "directive": t.string().optional(),
            "expires": t.string().optional(),
            "age": t.string().optional(),
        }
    ).named(renames["HttpCacheControlResponseHeaderIn"])
    types["HttpCacheControlResponseHeaderOut"] = t.struct(
        {
            "directive": t.string().optional(),
            "expires": t.string().optional(),
            "age": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpCacheControlResponseHeaderOut"])
    types["ServerConfigIn"] = t.struct(
        {
            "validMasterVersions": t.array(t.string()).optional(),
            "validNodeVersions": t.array(t.string()).optional(),
            "channels": t.array(t.proxy(renames["ReleaseChannelConfigIn"])).optional(),
            "defaultClusterVersion": t.string().optional(),
            "validImageTypes": t.array(t.string()).optional(),
            "defaultImageType": t.string().optional(),
        }
    ).named(renames["ServerConfigIn"])
    types["ServerConfigOut"] = t.struct(
        {
            "validMasterVersions": t.array(t.string()).optional(),
            "validNodeVersions": t.array(t.string()).optional(),
            "channels": t.array(t.proxy(renames["ReleaseChannelConfigOut"])).optional(),
            "defaultClusterVersion": t.string().optional(),
            "validImageTypes": t.array(t.string()).optional(),
            "defaultImageType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServerConfigOut"])
    types["UpdateMasterRequestIn"] = t.struct(
        {
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "masterVersion": t.string(),
        }
    ).named(renames["UpdateMasterRequestIn"])
    types["UpdateMasterRequestOut"] = t.struct(
        {
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "masterVersion": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateMasterRequestOut"])
    types["AutopilotIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["AutopilotIn"]
    )
    types["AutopilotOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutopilotOut"])
    types["GcfsConfigIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["GcfsConfigIn"]
    )
    types["GcfsConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcfsConfigOut"])
    types["SetNodePoolAutoscalingRequestIn"] = t.struct(
        {
            "nodePoolId": t.string().optional(),
            "autoscaling": t.proxy(renames["NodePoolAutoscalingIn"]),
            "clusterId": t.string().optional(),
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "zone": t.string().optional(),
        }
    ).named(renames["SetNodePoolAutoscalingRequestIn"])
    types["SetNodePoolAutoscalingRequestOut"] = t.struct(
        {
            "nodePoolId": t.string().optional(),
            "autoscaling": t.proxy(renames["NodePoolAutoscalingOut"]),
            "clusterId": t.string().optional(),
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "zone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetNodePoolAutoscalingRequestOut"])
    types["LegacyAbacIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["LegacyAbacIn"]
    )
    types["LegacyAbacOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LegacyAbacOut"])
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
    types["StandardRolloutPolicyIn"] = t.struct(
        {
            "batchNodeCount": t.integer().optional(),
            "batchPercentage": t.number().optional(),
            "batchSoakDuration": t.string().optional(),
        }
    ).named(renames["StandardRolloutPolicyIn"])
    types["StandardRolloutPolicyOut"] = t.struct(
        {
            "batchNodeCount": t.integer().optional(),
            "batchPercentage": t.number().optional(),
            "batchSoakDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StandardRolloutPolicyOut"])
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
    types["HorizontalPodAutoscalingIn"] = t.struct(
        {"disabled": t.boolean().optional()}
    ).named(renames["HorizontalPodAutoscalingIn"])
    types["HorizontalPodAutoscalingOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HorizontalPodAutoscalingOut"])
    types["AddonsConfigIn"] = t.struct(
        {
            "horizontalPodAutoscaling": t.proxy(
                renames["HorizontalPodAutoscalingIn"]
            ).optional(),
            "networkPolicyConfig": t.proxy(renames["NetworkPolicyConfigIn"]).optional(),
            "gcpFilestoreCsiDriverConfig": t.proxy(
                renames["GcpFilestoreCsiDriverConfigIn"]
            ).optional(),
            "gkeBackupAgentConfig": t.proxy(
                renames["GkeBackupAgentConfigIn"]
            ).optional(),
            "cloudRunConfig": t.proxy(renames["CloudRunConfigIn"]).optional(),
            "configConnectorConfig": t.proxy(
                renames["ConfigConnectorConfigIn"]
            ).optional(),
            "kubernetesDashboard": t.proxy(renames["KubernetesDashboardIn"]).optional(),
            "dnsCacheConfig": t.proxy(renames["DnsCacheConfigIn"]).optional(),
            "gcePersistentDiskCsiDriverConfig": t.proxy(
                renames["GcePersistentDiskCsiDriverConfigIn"]
            ).optional(),
            "httpLoadBalancing": t.proxy(renames["HttpLoadBalancingIn"]).optional(),
        }
    ).named(renames["AddonsConfigIn"])
    types["AddonsConfigOut"] = t.struct(
        {
            "horizontalPodAutoscaling": t.proxy(
                renames["HorizontalPodAutoscalingOut"]
            ).optional(),
            "networkPolicyConfig": t.proxy(
                renames["NetworkPolicyConfigOut"]
            ).optional(),
            "gcpFilestoreCsiDriverConfig": t.proxy(
                renames["GcpFilestoreCsiDriverConfigOut"]
            ).optional(),
            "gkeBackupAgentConfig": t.proxy(
                renames["GkeBackupAgentConfigOut"]
            ).optional(),
            "cloudRunConfig": t.proxy(renames["CloudRunConfigOut"]).optional(),
            "configConnectorConfig": t.proxy(
                renames["ConfigConnectorConfigOut"]
            ).optional(),
            "kubernetesDashboard": t.proxy(
                renames["KubernetesDashboardOut"]
            ).optional(),
            "dnsCacheConfig": t.proxy(renames["DnsCacheConfigOut"]).optional(),
            "gcePersistentDiskCsiDriverConfig": t.proxy(
                renames["GcePersistentDiskCsiDriverConfigOut"]
            ).optional(),
            "httpLoadBalancing": t.proxy(renames["HttpLoadBalancingOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddonsConfigOut"])
    types["PlacementPolicyIn"] = t.struct({"type": t.string().optional()}).named(
        renames["PlacementPolicyIn"]
    )
    types["PlacementPolicyOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacementPolicyOut"])
    types["CompleteNodePoolUpgradeRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CompleteNodePoolUpgradeRequestIn"])
    types["CompleteNodePoolUpgradeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CompleteNodePoolUpgradeRequestOut"])
    types["MasterAuthIn"] = t.struct(
        {
            "clientCertificate": t.string().optional(),
            "clientKey": t.string().optional(),
            "clusterCaCertificate": t.string().optional(),
            "password": t.string().optional(),
            "clientCertificateConfig": t.proxy(
                renames["ClientCertificateConfigIn"]
            ).optional(),
            "username": t.string().optional(),
        }
    ).named(renames["MasterAuthIn"])
    types["MasterAuthOut"] = t.struct(
        {
            "clientCertificate": t.string().optional(),
            "clientKey": t.string().optional(),
            "clusterCaCertificate": t.string().optional(),
            "password": t.string().optional(),
            "clientCertificateConfig": t.proxy(
                renames["ClientCertificateConfigOut"]
            ).optional(),
            "username": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MasterAuthOut"])
    types["SetMasterAuthRequestIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "action": t.string(),
            "clusterId": t.string().optional(),
            "update": t.proxy(renames["MasterAuthIn"]),
        }
    ).named(renames["SetMasterAuthRequestIn"])
    types["SetMasterAuthRequestOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "action": t.string(),
            "clusterId": t.string().optional(),
            "update": t.proxy(renames["MasterAuthOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetMasterAuthRequestOut"])
    types["VerticalPodAutoscalingIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["VerticalPodAutoscalingIn"])
    types["VerticalPodAutoscalingOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerticalPodAutoscalingOut"])
    types["SetNetworkPolicyRequestIn"] = t.struct(
        {
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "networkPolicy": t.proxy(renames["NetworkPolicyIn"]),
            "clusterId": t.string().optional(),
        }
    ).named(renames["SetNetworkPolicyRequestIn"])
    types["SetNetworkPolicyRequestOut"] = t.struct(
        {
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "networkPolicy": t.proxy(renames["NetworkPolicyOut"]),
            "clusterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetNetworkPolicyRequestOut"])
    types["KubernetesDashboardIn"] = t.struct(
        {"disabled": t.boolean().optional()}
    ).named(renames["KubernetesDashboardIn"])
    types["KubernetesDashboardOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KubernetesDashboardOut"])
    types["BlueGreenInfoIn"] = t.struct(
        {
            "phase": t.string().optional(),
            "greenPoolVersion": t.string().optional(),
            "blueInstanceGroupUrls": t.array(t.string()).optional(),
            "bluePoolDeletionStartTime": t.string().optional(),
            "greenInstanceGroupUrls": t.array(t.string()).optional(),
        }
    ).named(renames["BlueGreenInfoIn"])
    types["BlueGreenInfoOut"] = t.struct(
        {
            "phase": t.string().optional(),
            "greenPoolVersion": t.string().optional(),
            "blueInstanceGroupUrls": t.array(t.string()).optional(),
            "bluePoolDeletionStartTime": t.string().optional(),
            "greenInstanceGroupUrls": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BlueGreenInfoOut"])
    types["ManagedPrometheusConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["ManagedPrometheusConfigIn"])
    types["ManagedPrometheusConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedPrometheusConfigOut"])
    types["VirtualNICIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["VirtualNICIn"]
    )
    types["VirtualNICOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VirtualNICOut"])
    types["StatusConditionIn"] = t.struct(
        {
            "canonicalCode": t.string().optional(),
            "message": t.string().optional(),
            "code": t.string().optional(),
        }
    ).named(renames["StatusConditionIn"])
    types["StatusConditionOut"] = t.struct(
        {
            "canonicalCode": t.string().optional(),
            "message": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusConditionOut"])
    types["SetLabelsRequestIn"] = t.struct(
        {
            "resourceLabels": t.struct({"_": t.string().optional()}),
            "name": t.string().optional(),
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
            "labelFingerprint": t.string(),
            "projectId": t.string().optional(),
        }
    ).named(renames["SetLabelsRequestIn"])
    types["SetLabelsRequestOut"] = t.struct(
        {
            "resourceLabels": t.struct({"_": t.string().optional()}),
            "name": t.string().optional(),
            "zone": t.string().optional(),
            "clusterId": t.string().optional(),
            "labelFingerprint": t.string(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetLabelsRequestOut"])
    types["NodeNetworkConfigIn"] = t.struct(
        {
            "podCidrOverprovisionConfig": t.proxy(
                renames["PodCIDROverprovisionConfigIn"]
            ).optional(),
            "networkPerformanceConfig": t.proxy(
                renames["NetworkPerformanceConfigIn"]
            ).optional(),
            "createPodRange": t.boolean().optional(),
            "podRange": t.string().optional(),
            "enablePrivateNodes": t.boolean().optional(),
            "podIpv4CidrBlock": t.string().optional(),
        }
    ).named(renames["NodeNetworkConfigIn"])
    types["NodeNetworkConfigOut"] = t.struct(
        {
            "podCidrOverprovisionConfig": t.proxy(
                renames["PodCIDROverprovisionConfigOut"]
            ).optional(),
            "networkPerformanceConfig": t.proxy(
                renames["NetworkPerformanceConfigOut"]
            ).optional(),
            "createPodRange": t.boolean().optional(),
            "podRange": t.string().optional(),
            "enablePrivateNodes": t.boolean().optional(),
            "podIpv4CidrBlock": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeNetworkConfigOut"])
    types["FilterIn"] = t.struct({"eventType": t.array(t.string()).optional()}).named(
        renames["FilterIn"]
    )
    types["FilterOut"] = t.struct(
        {
            "eventType": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterOut"])
    types["LinuxNodeConfigIn"] = t.struct(
        {
            "sysctls": t.struct({"_": t.string().optional()}).optional(),
            "cgroupMode": t.string().optional(),
        }
    ).named(renames["LinuxNodeConfigIn"])
    types["LinuxNodeConfigOut"] = t.struct(
        {
            "sysctls": t.struct({"_": t.string().optional()}).optional(),
            "cgroupMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinuxNodeConfigOut"])
    types["AutoprovisioningNodePoolDefaultsIn"] = t.struct(
        {
            "diskType": t.string().optional(),
            "upgradeSettings": t.proxy(renames["UpgradeSettingsIn"]).optional(),
            "diskSizeGb": t.integer().optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigIn"]
            ).optional(),
            "bootDiskKmsKey": t.string().optional(),
            "management": t.proxy(renames["NodeManagementIn"]).optional(),
            "serviceAccount": t.string().optional(),
            "minCpuPlatform": t.string().optional(),
            "imageType": t.string().optional(),
            "oauthScopes": t.array(t.string()).optional(),
        }
    ).named(renames["AutoprovisioningNodePoolDefaultsIn"])
    types["AutoprovisioningNodePoolDefaultsOut"] = t.struct(
        {
            "diskType": t.string().optional(),
            "upgradeSettings": t.proxy(renames["UpgradeSettingsOut"]).optional(),
            "diskSizeGb": t.integer().optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["ShieldedInstanceConfigOut"]
            ).optional(),
            "bootDiskKmsKey": t.string().optional(),
            "management": t.proxy(renames["NodeManagementOut"]).optional(),
            "serviceAccount": t.string().optional(),
            "minCpuPlatform": t.string().optional(),
            "imageType": t.string().optional(),
            "oauthScopes": t.array(t.string()).optional(),
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
    types["UpgradeEventIn"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "operationStartTime": t.string().optional(),
            "currentVersion": t.string().optional(),
            "targetVersion": t.string().optional(),
            "resource": t.string().optional(),
            "operation": t.string().optional(),
        }
    ).named(renames["UpgradeEventIn"])
    types["UpgradeEventOut"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "operationStartTime": t.string().optional(),
            "currentVersion": t.string().optional(),
            "targetVersion": t.string().optional(),
            "resource": t.string().optional(),
            "operation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeEventOut"])
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
    types["UpgradeAvailableEventIn"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "resource": t.string().optional(),
            "releaseChannel": t.proxy(renames["ReleaseChannelIn"]).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["UpgradeAvailableEventIn"])
    types["UpgradeAvailableEventOut"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "resource": t.string().optional(),
            "releaseChannel": t.proxy(renames["ReleaseChannelOut"]).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeAvailableEventOut"])
    types["CompleteIPRotationRequestIn"] = t.struct(
        {
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
        }
    ).named(renames["CompleteIPRotationRequestIn"])
    types["CompleteIPRotationRequestOut"] = t.struct(
        {
            "zone": t.string().optional(),
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "clusterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompleteIPRotationRequestOut"])
    types["IPAllocationPolicyIn"] = t.struct(
        {
            "nodeIpv4CidrBlock": t.string().optional(),
            "useIpAliases": t.boolean().optional(),
            "servicesIpv4CidrBlock": t.string().optional(),
            "servicesIpv4Cidr": t.string().optional(),
            "createSubnetwork": t.boolean().optional(),
            "useRoutes": t.boolean().optional(),
            "clusterIpv4Cidr": t.string().optional(),
            "stackType": t.string().optional(),
            "subnetworkName": t.string().optional(),
            "servicesSecondaryRangeName": t.string().optional(),
            "ipv6AccessType": t.string().optional(),
            "clusterSecondaryRangeName": t.string().optional(),
            "podCidrOverprovisionConfig": t.proxy(
                renames["PodCIDROverprovisionConfigIn"]
            ).optional(),
            "clusterIpv4CidrBlock": t.string().optional(),
            "nodeIpv4Cidr": t.string().optional(),
            "tpuIpv4CidrBlock": t.string().optional(),
        }
    ).named(renames["IPAllocationPolicyIn"])
    types["IPAllocationPolicyOut"] = t.struct(
        {
            "nodeIpv4CidrBlock": t.string().optional(),
            "useIpAliases": t.boolean().optional(),
            "servicesIpv4CidrBlock": t.string().optional(),
            "servicesIpv4Cidr": t.string().optional(),
            "createSubnetwork": t.boolean().optional(),
            "useRoutes": t.boolean().optional(),
            "clusterIpv4Cidr": t.string().optional(),
            "servicesIpv6CidrBlock": t.string().optional(),
            "subnetIpv6CidrBlock": t.string().optional(),
            "stackType": t.string().optional(),
            "subnetworkName": t.string().optional(),
            "servicesSecondaryRangeName": t.string().optional(),
            "ipv6AccessType": t.string().optional(),
            "additionalPodRangesConfig": t.proxy(
                renames["AdditionalPodRangesConfigOut"]
            ).optional(),
            "clusterSecondaryRangeName": t.string().optional(),
            "podCidrOverprovisionConfig": t.proxy(
                renames["PodCIDROverprovisionConfigOut"]
            ).optional(),
            "clusterIpv4CidrBlock": t.string().optional(),
            "nodeIpv4Cidr": t.string().optional(),
            "tpuIpv4CidrBlock": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IPAllocationPolicyOut"])
    types["UpdateClusterRequestIn"] = t.struct(
        {
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "update": t.proxy(renames["ClusterUpdateIn"]),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
        }
    ).named(renames["UpdateClusterRequestIn"])
    types["UpdateClusterRequestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "update": t.proxy(renames["ClusterUpdateOut"]),
            "clusterId": t.string().optional(),
            "zone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateClusterRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["PubSubIn"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "filter": t.proxy(renames["FilterIn"]).optional(),
            "topic": t.string().optional(),
        }
    ).named(renames["PubSubIn"])
    types["PubSubOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "filter": t.proxy(renames["FilterOut"]).optional(),
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubSubOut"])
    types["NodePoolDefaultsIn"] = t.struct(
        {"nodeConfigDefaults": t.proxy(renames["NodeConfigDefaultsIn"]).optional()}
    ).named(renames["NodePoolDefaultsIn"])
    types["NodePoolDefaultsOut"] = t.struct(
        {
            "nodeConfigDefaults": t.proxy(renames["NodeConfigDefaultsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodePoolDefaultsOut"])
    types["ReleaseChannelConfigIn"] = t.struct(
        {
            "defaultVersion": t.string().optional(),
            "channel": t.string().optional(),
            "validVersions": t.array(t.string()).optional(),
        }
    ).named(renames["ReleaseChannelConfigIn"])
    types["ReleaseChannelConfigOut"] = t.struct(
        {
            "defaultVersion": t.string().optional(),
            "channel": t.string().optional(),
            "validVersions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseChannelConfigOut"])
    types["SecurityBulletinEventIn"] = t.struct(
        {
            "affectedSupportedMinors": t.array(t.string()).optional(),
            "bulletinId": t.string().optional(),
            "patchedVersions": t.array(t.string()).optional(),
            "resourceTypeAffected": t.string().optional(),
            "cveIds": t.array(t.string()).optional(),
            "bulletinUri": t.string().optional(),
            "briefDescription": t.string().optional(),
            "severity": t.string().optional(),
            "manualStepsRequired": t.boolean().optional(),
            "suggestedUpgradeTarget": t.string().optional(),
        }
    ).named(renames["SecurityBulletinEventIn"])
    types["SecurityBulletinEventOut"] = t.struct(
        {
            "affectedSupportedMinors": t.array(t.string()).optional(),
            "bulletinId": t.string().optional(),
            "patchedVersions": t.array(t.string()).optional(),
            "resourceTypeAffected": t.string().optional(),
            "cveIds": t.array(t.string()).optional(),
            "bulletinUri": t.string().optional(),
            "briefDescription": t.string().optional(),
            "severity": t.string().optional(),
            "manualStepsRequired": t.boolean().optional(),
            "suggestedUpgradeTarget": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecurityBulletinEventOut"])
    types["NetworkPolicyConfigIn"] = t.struct(
        {"disabled": t.boolean().optional()}
    ).named(renames["NetworkPolicyConfigIn"])
    types["NetworkPolicyConfigOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkPolicyConfigOut"])
    types["RollbackNodePoolUpgradeRequestIn"] = t.struct(
        {
            "clusterId": t.string().optional(),
            "respectPdb": t.boolean().optional(),
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "nodePoolId": t.string().optional(),
        }
    ).named(renames["RollbackNodePoolUpgradeRequestIn"])
    types["RollbackNodePoolUpgradeRequestOut"] = t.struct(
        {
            "clusterId": t.string().optional(),
            "respectPdb": t.boolean().optional(),
            "projectId": t.string().optional(),
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "nodePoolId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RollbackNodePoolUpgradeRequestOut"])
    types["BigQueryDestinationIn"] = t.struct(
        {"datasetId": t.string().optional()}
    ).named(renames["BigQueryDestinationIn"])
    types["BigQueryDestinationOut"] = t.struct(
        {
            "datasetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryDestinationOut"])

    functions = {}
    functions["projectsAggregatedUsableSubnetworksList"] = container.get(
        "v1/{parent}/aggregated/usableSubnetworks",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
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
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "parent": t.string().optional(),
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
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "parent": t.string().optional(),
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
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersDelete"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersGet"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersMonitoring"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersResourceLabels"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersSetMaintenancePolicy"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersUpdate"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersMaster"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersCreate"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersStartIpRotation"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersSetNetworkPolicy"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersLegacyAbac"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersLocations"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersSetMasterAuth"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersLogging"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersAddons"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersCompleteIpRotation"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersList"] = container.get(
        "v1/projects/{projectId}/zones/{zone}/clusters",
        t.struct(
            {
                "parent": t.string().optional(),
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsUpdate"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/setManagement",
        t.struct(
            {
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "clusterId": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "management": t.proxy(renames["NodeManagementIn"]),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsGet"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/setManagement",
        t.struct(
            {
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "clusterId": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "management": t.proxy(renames["NodeManagementIn"]),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsCreate"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/setManagement",
        t.struct(
            {
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "clusterId": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "management": t.proxy(renames["NodeManagementIn"]),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsSetSize"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/setManagement",
        t.struct(
            {
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "clusterId": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "management": t.proxy(renames["NodeManagementIn"]),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsAutoscaling"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/setManagement",
        t.struct(
            {
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "clusterId": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "management": t.proxy(renames["NodeManagementIn"]),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsList"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/setManagement",
        t.struct(
            {
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "clusterId": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "management": t.proxy(renames["NodeManagementIn"]),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsDelete"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/setManagement",
        t.struct(
            {
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "clusterId": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "management": t.proxy(renames["NodeManagementIn"]),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsRollback"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/setManagement",
        t.struct(
            {
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "clusterId": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "management": t.proxy(renames["NodeManagementIn"]),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsZonesClustersNodePoolsSetManagement"] = container.post(
        "v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/setManagement",
        t.struct(
            {
                "projectId": t.string().optional(),
                "zone": t.string().optional(),
                "clusterId": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "management": t.proxy(renames["NodeManagementIn"]),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
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
    functions["projectsLocationsOperationsList"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "operationId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "operationId": t.string().optional(),
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
                "projectId": t.string().optional(),
                "operationId": t.string().optional(),
                "zone": t.string().optional(),
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
                "projectId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "clusterId": t.string(),
                "zone": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersSetLogging"] = container.post(
        "v1/{name}:setMaintenancePolicy",
        t.struct(
            {
                "name": t.string().optional(),
                "projectId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "clusterId": t.string(),
                "zone": t.string(),
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
                "projectId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "clusterId": t.string(),
                "zone": t.string(),
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
                "projectId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "clusterId": t.string(),
                "zone": t.string(),
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
                "projectId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "clusterId": t.string(),
                "zone": t.string(),
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
                "projectId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "clusterId": t.string(),
                "zone": t.string(),
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
                "projectId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "clusterId": t.string(),
                "zone": t.string(),
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
                "projectId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "clusterId": t.string(),
                "zone": t.string(),
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
                "projectId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "clusterId": t.string(),
                "zone": t.string(),
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
                "projectId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "clusterId": t.string(),
                "zone": t.string(),
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
                "projectId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "clusterId": t.string(),
                "zone": t.string(),
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
                "projectId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "clusterId": t.string(),
                "zone": t.string(),
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
                "projectId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "clusterId": t.string(),
                "zone": t.string(),
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
                "projectId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "clusterId": t.string(),
                "zone": t.string(),
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
                "projectId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "clusterId": t.string(),
                "zone": t.string(),
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
                "projectId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "clusterId": t.string(),
                "zone": t.string(),
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
                "projectId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "clusterId": t.string(),
                "zone": t.string(),
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
                "projectId": t.string(),
                "maintenancePolicy": t.proxy(renames["MaintenancePolicyIn"]),
                "clusterId": t.string(),
                "zone": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsList"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NodePoolOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsCompleteUpgrade"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NodePoolOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsSetSize"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NodePoolOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsUpdate"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NodePoolOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsRollback"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NodePoolOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsSetAutoscaling"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NodePoolOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsDelete"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NodePoolOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsSetManagement"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NodePoolOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsCreate"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NodePoolOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClustersNodePoolsGet"] = container.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "nodePoolId": t.string().optional(),
                "projectId": t.string().optional(),
                "clusterId": t.string().optional(),
                "zone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NodePoolOut"]),
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

    return Import(
        importer="container",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
