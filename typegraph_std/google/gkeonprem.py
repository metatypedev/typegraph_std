from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_gkeonprem():
    gkeonprem = HTTPRuntime("https://gkeonprem.googleapis.com/")

    renames = {
        "ErrorResponse": "_gkeonprem_1_ErrorResponse",
        "BareMetalAdminDrainingMachineIn": "_gkeonprem_2_BareMetalAdminDrainingMachineIn",
        "BareMetalAdminDrainingMachineOut": "_gkeonprem_3_BareMetalAdminDrainingMachineOut",
        "BareMetalMaintenanceStatusIn": "_gkeonprem_4_BareMetalMaintenanceStatusIn",
        "BareMetalMaintenanceStatusOut": "_gkeonprem_5_BareMetalMaintenanceStatusOut",
        "VmwareAddressPoolIn": "_gkeonprem_6_VmwareAddressPoolIn",
        "VmwareAddressPoolOut": "_gkeonprem_7_VmwareAddressPoolOut",
        "BareMetalDrainedMachineIn": "_gkeonprem_8_BareMetalDrainedMachineIn",
        "BareMetalDrainedMachineOut": "_gkeonprem_9_BareMetalDrainedMachineOut",
        "ListLocationsResponseIn": "_gkeonprem_10_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_gkeonprem_11_ListLocationsResponseOut",
        "BareMetalBgpLbConfigIn": "_gkeonprem_12_BareMetalBgpLbConfigIn",
        "BareMetalBgpLbConfigOut": "_gkeonprem_13_BareMetalBgpLbConfigOut",
        "BareMetalAdminStorageConfigIn": "_gkeonprem_14_BareMetalAdminStorageConfigIn",
        "BareMetalAdminStorageConfigOut": "_gkeonprem_15_BareMetalAdminStorageConfigOut",
        "VmwareAdminMetalLbConfigIn": "_gkeonprem_16_VmwareAdminMetalLbConfigIn",
        "VmwareAdminMetalLbConfigOut": "_gkeonprem_17_VmwareAdminMetalLbConfigOut",
        "BareMetalAdminNetworkConfigIn": "_gkeonprem_18_BareMetalAdminNetworkConfigIn",
        "BareMetalAdminNetworkConfigOut": "_gkeonprem_19_BareMetalAdminNetworkConfigOut",
        "VmwareStaticIpConfigIn": "_gkeonprem_20_VmwareStaticIpConfigIn",
        "VmwareStaticIpConfigOut": "_gkeonprem_21_VmwareStaticIpConfigOut",
        "ListBareMetalNodePoolsResponseIn": "_gkeonprem_22_ListBareMetalNodePoolsResponseIn",
        "ListBareMetalNodePoolsResponseOut": "_gkeonprem_23_ListBareMetalNodePoolsResponseOut",
        "TestIamPermissionsResponseIn": "_gkeonprem_24_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_gkeonprem_25_TestIamPermissionsResponseOut",
        "VmwareVsphereTagIn": "_gkeonprem_26_VmwareVsphereTagIn",
        "VmwareVsphereTagOut": "_gkeonprem_27_VmwareVsphereTagOut",
        "ValidationCheckStatusIn": "_gkeonprem_28_ValidationCheckStatusIn",
        "ValidationCheckStatusOut": "_gkeonprem_29_ValidationCheckStatusOut",
        "BareMetalAdminMaintenanceStatusIn": "_gkeonprem_30_BareMetalAdminMaintenanceStatusIn",
        "BareMetalAdminMaintenanceStatusOut": "_gkeonprem_31_BareMetalAdminMaintenanceStatusOut",
        "BareMetalAdminLoadBalancerConfigIn": "_gkeonprem_32_BareMetalAdminLoadBalancerConfigIn",
        "BareMetalAdminLoadBalancerConfigOut": "_gkeonprem_33_BareMetalAdminLoadBalancerConfigOut",
        "VmwareControlPlaneVsphereConfigIn": "_gkeonprem_34_VmwareControlPlaneVsphereConfigIn",
        "VmwareControlPlaneVsphereConfigOut": "_gkeonprem_35_VmwareControlPlaneVsphereConfigOut",
        "CancelOperationRequestIn": "_gkeonprem_36_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_gkeonprem_37_CancelOperationRequestOut",
        "VmwareHostConfigIn": "_gkeonprem_38_VmwareHostConfigIn",
        "VmwareHostConfigOut": "_gkeonprem_39_VmwareHostConfigOut",
        "ListOperationsResponseIn": "_gkeonprem_40_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_gkeonprem_41_ListOperationsResponseOut",
        "BareMetalAdminControlPlaneNodePoolConfigIn": "_gkeonprem_42_BareMetalAdminControlPlaneNodePoolConfigIn",
        "BareMetalAdminControlPlaneNodePoolConfigOut": "_gkeonprem_43_BareMetalAdminControlPlaneNodePoolConfigOut",
        "VmwareNodePoolIn": "_gkeonprem_44_VmwareNodePoolIn",
        "VmwareNodePoolOut": "_gkeonprem_45_VmwareNodePoolOut",
        "VmwareStorageConfigIn": "_gkeonprem_46_VmwareStorageConfigIn",
        "VmwareStorageConfigOut": "_gkeonprem_47_VmwareStorageConfigOut",
        "ClusterUserIn": "_gkeonprem_48_ClusterUserIn",
        "ClusterUserOut": "_gkeonprem_49_ClusterUserOut",
        "VmwareAdminManualLbConfigIn": "_gkeonprem_50_VmwareAdminManualLbConfigIn",
        "VmwareAdminManualLbConfigOut": "_gkeonprem_51_VmwareAdminManualLbConfigOut",
        "QueryVmwareVersionConfigResponseIn": "_gkeonprem_52_QueryVmwareVersionConfigResponseIn",
        "QueryVmwareVersionConfigResponseOut": "_gkeonprem_53_QueryVmwareVersionConfigResponseOut",
        "BareMetalAdminNodeAccessConfigIn": "_gkeonprem_54_BareMetalAdminNodeAccessConfigIn",
        "BareMetalAdminNodeAccessConfigOut": "_gkeonprem_55_BareMetalAdminNodeAccessConfigOut",
        "BareMetalKubeletConfigIn": "_gkeonprem_56_BareMetalKubeletConfigIn",
        "BareMetalKubeletConfigOut": "_gkeonprem_57_BareMetalKubeletConfigOut",
        "ResourceStatusIn": "_gkeonprem_58_ResourceStatusIn",
        "ResourceStatusOut": "_gkeonprem_59_ResourceStatusOut",
        "BareMetalNodePoolUpgradePolicyIn": "_gkeonprem_60_BareMetalNodePoolUpgradePolicyIn",
        "BareMetalNodePoolUpgradePolicyOut": "_gkeonprem_61_BareMetalNodePoolUpgradePolicyOut",
        "VmwareAdminNetworkConfigIn": "_gkeonprem_62_VmwareAdminNetworkConfigIn",
        "VmwareAdminNetworkConfigOut": "_gkeonprem_63_VmwareAdminNetworkConfigOut",
        "FleetIn": "_gkeonprem_64_FleetIn",
        "FleetOut": "_gkeonprem_65_FleetOut",
        "BareMetalNodeConfigIn": "_gkeonprem_66_BareMetalNodeConfigIn",
        "BareMetalNodeConfigOut": "_gkeonprem_67_BareMetalNodeConfigOut",
        "BareMetalNodeAccessConfigIn": "_gkeonprem_68_BareMetalNodeAccessConfigIn",
        "BareMetalNodeAccessConfigOut": "_gkeonprem_69_BareMetalNodeAccessConfigOut",
        "BareMetalProxyConfigIn": "_gkeonprem_70_BareMetalProxyConfigIn",
        "BareMetalProxyConfigOut": "_gkeonprem_71_BareMetalProxyConfigOut",
        "BareMetalWorkloadNodeConfigIn": "_gkeonprem_72_BareMetalWorkloadNodeConfigIn",
        "BareMetalWorkloadNodeConfigOut": "_gkeonprem_73_BareMetalWorkloadNodeConfigOut",
        "VmwareAdminControlPlaneNodeConfigIn": "_gkeonprem_74_VmwareAdminControlPlaneNodeConfigIn",
        "VmwareAdminControlPlaneNodeConfigOut": "_gkeonprem_75_VmwareAdminControlPlaneNodeConfigOut",
        "BareMetalAdminDrainedMachineIn": "_gkeonprem_76_BareMetalAdminDrainedMachineIn",
        "BareMetalAdminDrainedMachineOut": "_gkeonprem_77_BareMetalAdminDrainedMachineOut",
        "UpgradeDependencyIn": "_gkeonprem_78_UpgradeDependencyIn",
        "UpgradeDependencyOut": "_gkeonprem_79_UpgradeDependencyOut",
        "BareMetalLoadBalancerNodePoolConfigIn": "_gkeonprem_80_BareMetalLoadBalancerNodePoolConfigIn",
        "BareMetalLoadBalancerNodePoolConfigOut": "_gkeonprem_81_BareMetalLoadBalancerNodePoolConfigOut",
        "BareMetalNodePoolConfigIn": "_gkeonprem_82_BareMetalNodePoolConfigIn",
        "BareMetalNodePoolConfigOut": "_gkeonprem_83_BareMetalNodePoolConfigOut",
        "BareMetalLoadBalancerConfigIn": "_gkeonprem_84_BareMetalLoadBalancerConfigIn",
        "BareMetalLoadBalancerConfigOut": "_gkeonprem_85_BareMetalLoadBalancerConfigOut",
        "BareMetalNetworkConfigIn": "_gkeonprem_86_BareMetalNetworkConfigIn",
        "BareMetalNetworkConfigOut": "_gkeonprem_87_BareMetalNetworkConfigOut",
        "EnrollBareMetalNodePoolRequestIn": "_gkeonprem_88_EnrollBareMetalNodePoolRequestIn",
        "EnrollBareMetalNodePoolRequestOut": "_gkeonprem_89_EnrollBareMetalNodePoolRequestOut",
        "ListBareMetalClustersResponseIn": "_gkeonprem_90_ListBareMetalClustersResponseIn",
        "ListBareMetalClustersResponseOut": "_gkeonprem_91_ListBareMetalClustersResponseOut",
        "TestIamPermissionsRequestIn": "_gkeonprem_92_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_gkeonprem_93_TestIamPermissionsRequestOut",
        "BareMetalBgpPeerConfigIn": "_gkeonprem_94_BareMetalBgpPeerConfigIn",
        "BareMetalBgpPeerConfigOut": "_gkeonprem_95_BareMetalBgpPeerConfigOut",
        "BareMetalAdminVipConfigIn": "_gkeonprem_96_BareMetalAdminVipConfigIn",
        "BareMetalAdminVipConfigOut": "_gkeonprem_97_BareMetalAdminVipConfigOut",
        "BareMetalControlPlaneNodePoolConfigIn": "_gkeonprem_98_BareMetalControlPlaneNodePoolConfigIn",
        "BareMetalControlPlaneNodePoolConfigOut": "_gkeonprem_99_BareMetalControlPlaneNodePoolConfigOut",
        "BareMetalVersionInfoIn": "_gkeonprem_100_BareMetalVersionInfoIn",
        "BareMetalVersionInfoOut": "_gkeonprem_101_BareMetalVersionInfoOut",
        "EmptyIn": "_gkeonprem_102_EmptyIn",
        "EmptyOut": "_gkeonprem_103_EmptyOut",
        "VmwareAdminVCenterConfigIn": "_gkeonprem_104_VmwareAdminVCenterConfigIn",
        "VmwareAdminVCenterConfigOut": "_gkeonprem_105_VmwareAdminVCenterConfigOut",
        "VmwareAdminAddonNodeConfigIn": "_gkeonprem_106_VmwareAdminAddonNodeConfigIn",
        "VmwareAdminAddonNodeConfigOut": "_gkeonprem_107_VmwareAdminAddonNodeConfigOut",
        "PolicyIn": "_gkeonprem_108_PolicyIn",
        "PolicyOut": "_gkeonprem_109_PolicyOut",
        "VmwareNodeConfigIn": "_gkeonprem_110_VmwareNodeConfigIn",
        "VmwareNodeConfigOut": "_gkeonprem_111_VmwareNodeConfigOut",
        "VmwareBundleConfigIn": "_gkeonprem_112_VmwareBundleConfigIn",
        "VmwareBundleConfigOut": "_gkeonprem_113_VmwareBundleConfigOut",
        "VmwareAdminLoadBalancerConfigIn": "_gkeonprem_114_VmwareAdminLoadBalancerConfigIn",
        "VmwareAdminLoadBalancerConfigOut": "_gkeonprem_115_VmwareAdminLoadBalancerConfigOut",
        "ValidationCheckIn": "_gkeonprem_116_ValidationCheckIn",
        "ValidationCheckOut": "_gkeonprem_117_ValidationCheckOut",
        "ResourceConditionIn": "_gkeonprem_118_ResourceConditionIn",
        "ResourceConditionOut": "_gkeonprem_119_ResourceConditionOut",
        "VmwareF5BigIpConfigIn": "_gkeonprem_120_VmwareF5BigIpConfigIn",
        "VmwareF5BigIpConfigOut": "_gkeonprem_121_VmwareF5BigIpConfigOut",
        "BareMetalAdminSecurityConfigIn": "_gkeonprem_122_BareMetalAdminSecurityConfigIn",
        "BareMetalAdminSecurityConfigOut": "_gkeonprem_123_BareMetalAdminSecurityConfigOut",
        "BareMetalAdminMaintenanceConfigIn": "_gkeonprem_124_BareMetalAdminMaintenanceConfigIn",
        "BareMetalAdminMaintenanceConfigOut": "_gkeonprem_125_BareMetalAdminMaintenanceConfigOut",
        "BareMetalMaintenanceConfigIn": "_gkeonprem_126_BareMetalMaintenanceConfigIn",
        "BareMetalMaintenanceConfigOut": "_gkeonprem_127_BareMetalMaintenanceConfigOut",
        "VmwareDataplaneV2ConfigIn": "_gkeonprem_128_VmwareDataplaneV2ConfigIn",
        "VmwareDataplaneV2ConfigOut": "_gkeonprem_129_VmwareDataplaneV2ConfigOut",
        "BareMetalAdminManualLbConfigIn": "_gkeonprem_130_BareMetalAdminManualLbConfigIn",
        "BareMetalAdminManualLbConfigOut": "_gkeonprem_131_BareMetalAdminManualLbConfigOut",
        "VmwareClusterIn": "_gkeonprem_132_VmwareClusterIn",
        "VmwareClusterOut": "_gkeonprem_133_VmwareClusterOut",
        "VmwareHostIpIn": "_gkeonprem_134_VmwareHostIpIn",
        "VmwareHostIpOut": "_gkeonprem_135_VmwareHostIpOut",
        "BareMetalLoadBalancerAddressPoolIn": "_gkeonprem_136_BareMetalLoadBalancerAddressPoolIn",
        "BareMetalLoadBalancerAddressPoolOut": "_gkeonprem_137_BareMetalLoadBalancerAddressPoolOut",
        "SetIamPolicyRequestIn": "_gkeonprem_138_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_gkeonprem_139_SetIamPolicyRequestOut",
        "VmwareAdminF5BigIpConfigIn": "_gkeonprem_140_VmwareAdminF5BigIpConfigIn",
        "VmwareAdminF5BigIpConfigOut": "_gkeonprem_141_VmwareAdminF5BigIpConfigOut",
        "BareMetalDrainingMachineIn": "_gkeonprem_142_BareMetalDrainingMachineIn",
        "BareMetalDrainingMachineOut": "_gkeonprem_143_BareMetalDrainingMachineOut",
        "BareMetalSecurityConfigIn": "_gkeonprem_144_BareMetalSecurityConfigIn",
        "BareMetalSecurityConfigOut": "_gkeonprem_145_BareMetalSecurityConfigOut",
        "VmwareAdminVipConfigIn": "_gkeonprem_146_VmwareAdminVipConfigIn",
        "VmwareAdminVipConfigOut": "_gkeonprem_147_VmwareAdminVipConfigOut",
        "EnrollVmwareNodePoolRequestIn": "_gkeonprem_148_EnrollVmwareNodePoolRequestIn",
        "EnrollVmwareNodePoolRequestOut": "_gkeonprem_149_EnrollVmwareNodePoolRequestOut",
        "BareMetalMetalLbConfigIn": "_gkeonprem_150_BareMetalMetalLbConfigIn",
        "BareMetalMetalLbConfigOut": "_gkeonprem_151_BareMetalMetalLbConfigOut",
        "BareMetalAdminProxyConfigIn": "_gkeonprem_152_BareMetalAdminProxyConfigIn",
        "BareMetalAdminProxyConfigOut": "_gkeonprem_153_BareMetalAdminProxyConfigOut",
        "QueryBareMetalAdminVersionConfigResponseIn": "_gkeonprem_154_QueryBareMetalAdminVersionConfigResponseIn",
        "QueryBareMetalAdminVersionConfigResponseOut": "_gkeonprem_155_QueryBareMetalAdminVersionConfigResponseOut",
        "OperationIn": "_gkeonprem_156_OperationIn",
        "OperationOut": "_gkeonprem_157_OperationOut",
        "BareMetalMachineDrainStatusIn": "_gkeonprem_158_BareMetalMachineDrainStatusIn",
        "BareMetalMachineDrainStatusOut": "_gkeonprem_159_BareMetalMachineDrainStatusOut",
        "BareMetalIslandModeCidrConfigIn": "_gkeonprem_160_BareMetalIslandModeCidrConfigIn",
        "BareMetalIslandModeCidrConfigOut": "_gkeonprem_161_BareMetalIslandModeCidrConfigOut",
        "EnrollVmwareClusterRequestIn": "_gkeonprem_162_EnrollVmwareClusterRequestIn",
        "EnrollVmwareClusterRequestOut": "_gkeonprem_163_EnrollVmwareClusterRequestOut",
        "BareMetalAdminWorkloadNodeConfigIn": "_gkeonprem_164_BareMetalAdminWorkloadNodeConfigIn",
        "BareMetalAdminWorkloadNodeConfigOut": "_gkeonprem_165_BareMetalAdminWorkloadNodeConfigOut",
        "VmwareManualLbConfigIn": "_gkeonprem_166_VmwareManualLbConfigIn",
        "VmwareManualLbConfigOut": "_gkeonprem_167_VmwareManualLbConfigOut",
        "BareMetalApiServerArgumentIn": "_gkeonprem_168_BareMetalApiServerArgumentIn",
        "BareMetalApiServerArgumentOut": "_gkeonprem_169_BareMetalApiServerArgumentOut",
        "VmwareAAGConfigIn": "_gkeonprem_170_VmwareAAGConfigIn",
        "VmwareAAGConfigOut": "_gkeonprem_171_VmwareAAGConfigOut",
        "BareMetalAdminControlPlaneConfigIn": "_gkeonprem_172_BareMetalAdminControlPlaneConfigIn",
        "BareMetalAdminControlPlaneConfigOut": "_gkeonprem_173_BareMetalAdminControlPlaneConfigOut",
        "BareMetalAdminMachineDrainStatusIn": "_gkeonprem_174_BareMetalAdminMachineDrainStatusIn",
        "BareMetalAdminMachineDrainStatusOut": "_gkeonprem_175_BareMetalAdminMachineDrainStatusOut",
        "EnrollVmwareAdminClusterRequestIn": "_gkeonprem_176_EnrollVmwareAdminClusterRequestIn",
        "EnrollVmwareAdminClusterRequestOut": "_gkeonprem_177_EnrollVmwareAdminClusterRequestOut",
        "ListVmwareAdminClustersResponseIn": "_gkeonprem_178_ListVmwareAdminClustersResponseIn",
        "ListVmwareAdminClustersResponseOut": "_gkeonprem_179_ListVmwareAdminClustersResponseOut",
        "BareMetalSrIovConfigIn": "_gkeonprem_180_BareMetalSrIovConfigIn",
        "BareMetalSrIovConfigOut": "_gkeonprem_181_BareMetalSrIovConfigOut",
        "ListVmwareNodePoolsResponseIn": "_gkeonprem_182_ListVmwareNodePoolsResponseIn",
        "ListVmwareNodePoolsResponseOut": "_gkeonprem_183_ListVmwareNodePoolsResponseOut",
        "BareMetalPortConfigIn": "_gkeonprem_184_BareMetalPortConfigIn",
        "BareMetalPortConfigOut": "_gkeonprem_185_BareMetalPortConfigOut",
        "EnrollBareMetalAdminClusterRequestIn": "_gkeonprem_186_EnrollBareMetalAdminClusterRequestIn",
        "EnrollBareMetalAdminClusterRequestOut": "_gkeonprem_187_EnrollBareMetalAdminClusterRequestOut",
        "BareMetalVipConfigIn": "_gkeonprem_188_BareMetalVipConfigIn",
        "BareMetalVipConfigOut": "_gkeonprem_189_BareMetalVipConfigOut",
        "VmwareNetworkConfigIn": "_gkeonprem_190_VmwareNetworkConfigIn",
        "VmwareNetworkConfigOut": "_gkeonprem_191_VmwareNetworkConfigOut",
        "BareMetalClusterIn": "_gkeonprem_192_BareMetalClusterIn",
        "BareMetalClusterOut": "_gkeonprem_193_BareMetalClusterOut",
        "AuthorizationIn": "_gkeonprem_194_AuthorizationIn",
        "AuthorizationOut": "_gkeonprem_195_AuthorizationOut",
        "BareMetalAdminPortConfigIn": "_gkeonprem_196_BareMetalAdminPortConfigIn",
        "BareMetalAdminPortConfigOut": "_gkeonprem_197_BareMetalAdminPortConfigOut",
        "VmwareIpBlockIn": "_gkeonprem_198_VmwareIpBlockIn",
        "VmwareIpBlockOut": "_gkeonprem_199_VmwareIpBlockOut",
        "VmwareControlPlaneV2ConfigIn": "_gkeonprem_200_VmwareControlPlaneV2ConfigIn",
        "VmwareControlPlaneV2ConfigOut": "_gkeonprem_201_VmwareControlPlaneV2ConfigOut",
        "VmwareVCenterConfigIn": "_gkeonprem_202_VmwareVCenterConfigIn",
        "VmwareVCenterConfigOut": "_gkeonprem_203_VmwareVCenterConfigOut",
        "VmwareControlPlaneNodeConfigIn": "_gkeonprem_204_VmwareControlPlaneNodeConfigIn",
        "VmwareControlPlaneNodeConfigOut": "_gkeonprem_205_VmwareControlPlaneNodeConfigOut",
        "BareMetalManualLbConfigIn": "_gkeonprem_206_BareMetalManualLbConfigIn",
        "BareMetalManualLbConfigOut": "_gkeonprem_207_BareMetalManualLbConfigOut",
        "BareMetalAdminClusterIn": "_gkeonprem_208_BareMetalAdminClusterIn",
        "BareMetalAdminClusterOut": "_gkeonprem_209_BareMetalAdminClusterOut",
        "ExprIn": "_gkeonprem_210_ExprIn",
        "ExprOut": "_gkeonprem_211_ExprOut",
        "BareMetalAdminClusterOperationsConfigIn": "_gkeonprem_212_BareMetalAdminClusterOperationsConfigIn",
        "BareMetalAdminClusterOperationsConfigOut": "_gkeonprem_213_BareMetalAdminClusterOperationsConfigOut",
        "VmwareAdminClusterIn": "_gkeonprem_214_VmwareAdminClusterIn",
        "VmwareAdminClusterOut": "_gkeonprem_215_VmwareAdminClusterOut",
        "VmwareNodePoolAutoscalingConfigIn": "_gkeonprem_216_VmwareNodePoolAutoscalingConfigIn",
        "VmwareNodePoolAutoscalingConfigOut": "_gkeonprem_217_VmwareNodePoolAutoscalingConfigOut",
        "BindingIn": "_gkeonprem_218_BindingIn",
        "BindingOut": "_gkeonprem_219_BindingOut",
        "BareMetalParallelUpgradeConfigIn": "_gkeonprem_220_BareMetalParallelUpgradeConfigIn",
        "BareMetalParallelUpgradeConfigOut": "_gkeonprem_221_BareMetalParallelUpgradeConfigOut",
        "VmwareAutoRepairConfigIn": "_gkeonprem_222_VmwareAutoRepairConfigIn",
        "VmwareAutoRepairConfigOut": "_gkeonprem_223_VmwareAutoRepairConfigOut",
        "VmwarePlatformConfigIn": "_gkeonprem_224_VmwarePlatformConfigIn",
        "VmwarePlatformConfigOut": "_gkeonprem_225_VmwarePlatformConfigOut",
        "VmwareVsphereConfigIn": "_gkeonprem_226_VmwareVsphereConfigIn",
        "VmwareVsphereConfigOut": "_gkeonprem_227_VmwareVsphereConfigOut",
        "VmwareVipConfigIn": "_gkeonprem_228_VmwareVipConfigIn",
        "VmwareVipConfigOut": "_gkeonprem_229_VmwareVipConfigOut",
        "ValidationCheckResultIn": "_gkeonprem_230_ValidationCheckResultIn",
        "ValidationCheckResultOut": "_gkeonprem_231_ValidationCheckResultOut",
        "NodeTaintIn": "_gkeonprem_232_NodeTaintIn",
        "NodeTaintOut": "_gkeonprem_233_NodeTaintOut",
        "ListVmwareClustersResponseIn": "_gkeonprem_234_ListVmwareClustersResponseIn",
        "ListVmwareClustersResponseOut": "_gkeonprem_235_ListVmwareClustersResponseOut",
        "BareMetalAdminOsEnvironmentConfigIn": "_gkeonprem_236_BareMetalAdminOsEnvironmentConfigIn",
        "BareMetalAdminOsEnvironmentConfigOut": "_gkeonprem_237_BareMetalAdminOsEnvironmentConfigOut",
        "BareMetalMultipleNetworkInterfacesConfigIn": "_gkeonprem_238_BareMetalMultipleNetworkInterfacesConfigIn",
        "BareMetalMultipleNetworkInterfacesConfigOut": "_gkeonprem_239_BareMetalMultipleNetworkInterfacesConfigOut",
        "BareMetalOsEnvironmentConfigIn": "_gkeonprem_240_BareMetalOsEnvironmentConfigIn",
        "BareMetalOsEnvironmentConfigOut": "_gkeonprem_241_BareMetalOsEnvironmentConfigOut",
        "BareMetalLvpConfigIn": "_gkeonprem_242_BareMetalLvpConfigIn",
        "BareMetalLvpConfigOut": "_gkeonprem_243_BareMetalLvpConfigOut",
        "BareMetalLvpShareConfigIn": "_gkeonprem_244_BareMetalLvpShareConfigIn",
        "BareMetalLvpShareConfigOut": "_gkeonprem_245_BareMetalLvpShareConfigOut",
        "BareMetalNodePoolIn": "_gkeonprem_246_BareMetalNodePoolIn",
        "BareMetalNodePoolOut": "_gkeonprem_247_BareMetalNodePoolOut",
        "BareMetalControlPlaneConfigIn": "_gkeonprem_248_BareMetalControlPlaneConfigIn",
        "BareMetalControlPlaneConfigOut": "_gkeonprem_249_BareMetalControlPlaneConfigOut",
        "OperationMetadataIn": "_gkeonprem_250_OperationMetadataIn",
        "OperationMetadataOut": "_gkeonprem_251_OperationMetadataOut",
        "VmwareDhcpIpConfigIn": "_gkeonprem_252_VmwareDhcpIpConfigIn",
        "VmwareDhcpIpConfigOut": "_gkeonprem_253_VmwareDhcpIpConfigOut",
        "OperationStageIn": "_gkeonprem_254_OperationStageIn",
        "OperationStageOut": "_gkeonprem_255_OperationStageOut",
        "MetricIn": "_gkeonprem_256_MetricIn",
        "MetricOut": "_gkeonprem_257_MetricOut",
        "EnrollBareMetalClusterRequestIn": "_gkeonprem_258_EnrollBareMetalClusterRequestIn",
        "EnrollBareMetalClusterRequestOut": "_gkeonprem_259_EnrollBareMetalClusterRequestOut",
        "BareMetalStorageConfigIn": "_gkeonprem_260_BareMetalStorageConfigIn",
        "BareMetalStorageConfigOut": "_gkeonprem_261_BareMetalStorageConfigOut",
        "BareMetalClusterOperationsConfigIn": "_gkeonprem_262_BareMetalClusterOperationsConfigIn",
        "BareMetalClusterOperationsConfigOut": "_gkeonprem_263_BareMetalClusterOperationsConfigOut",
        "VmwareLoadBalancerConfigIn": "_gkeonprem_264_VmwareLoadBalancerConfigIn",
        "VmwareLoadBalancerConfigOut": "_gkeonprem_265_VmwareLoadBalancerConfigOut",
        "StatusIn": "_gkeonprem_266_StatusIn",
        "StatusOut": "_gkeonprem_267_StatusOut",
        "QueryBareMetalVersionConfigResponseIn": "_gkeonprem_268_QueryBareMetalVersionConfigResponseIn",
        "QueryBareMetalVersionConfigResponseOut": "_gkeonprem_269_QueryBareMetalVersionConfigResponseOut",
        "ListBareMetalAdminClustersResponseIn": "_gkeonprem_270_ListBareMetalAdminClustersResponseIn",
        "ListBareMetalAdminClustersResponseOut": "_gkeonprem_271_ListBareMetalAdminClustersResponseOut",
        "LocationIn": "_gkeonprem_272_LocationIn",
        "LocationOut": "_gkeonprem_273_LocationOut",
        "BareMetalAdminIslandModeCidrConfigIn": "_gkeonprem_274_BareMetalAdminIslandModeCidrConfigIn",
        "BareMetalAdminIslandModeCidrConfigOut": "_gkeonprem_275_BareMetalAdminIslandModeCidrConfigOut",
        "VmwareAutoResizeConfigIn": "_gkeonprem_276_VmwareAutoResizeConfigIn",
        "VmwareAutoResizeConfigOut": "_gkeonprem_277_VmwareAutoResizeConfigOut",
        "VmwareMetalLbConfigIn": "_gkeonprem_278_VmwareMetalLbConfigIn",
        "VmwareMetalLbConfigOut": "_gkeonprem_279_VmwareMetalLbConfigOut",
        "BareMetalAdminApiServerArgumentIn": "_gkeonprem_280_BareMetalAdminApiServerArgumentIn",
        "BareMetalAdminApiServerArgumentOut": "_gkeonprem_281_BareMetalAdminApiServerArgumentOut",
        "OperationProgressIn": "_gkeonprem_282_OperationProgressIn",
        "OperationProgressOut": "_gkeonprem_283_OperationProgressOut",
        "VmwareVersionInfoIn": "_gkeonprem_284_VmwareVersionInfoIn",
        "VmwareVersionInfoOut": "_gkeonprem_285_VmwareVersionInfoOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["BareMetalAdminDrainingMachineIn"] = t.struct(
        {"nodeIp": t.string().optional(), "podCount": t.integer().optional()}
    ).named(renames["BareMetalAdminDrainingMachineIn"])
    types["BareMetalAdminDrainingMachineOut"] = t.struct(
        {
            "nodeIp": t.string().optional(),
            "podCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminDrainingMachineOut"])
    types["BareMetalMaintenanceStatusIn"] = t.struct(
        {
            "machineDrainStatus": t.proxy(
                renames["BareMetalMachineDrainStatusIn"]
            ).optional()
        }
    ).named(renames["BareMetalMaintenanceStatusIn"])
    types["BareMetalMaintenanceStatusOut"] = t.struct(
        {
            "machineDrainStatus": t.proxy(
                renames["BareMetalMachineDrainStatusOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalMaintenanceStatusOut"])
    types["VmwareAddressPoolIn"] = t.struct(
        {
            "addresses": t.array(t.string()),
            "avoidBuggyIps": t.boolean().optional(),
            "manualAssign": t.boolean().optional(),
            "pool": t.string(),
        }
    ).named(renames["VmwareAddressPoolIn"])
    types["VmwareAddressPoolOut"] = t.struct(
        {
            "addresses": t.array(t.string()),
            "avoidBuggyIps": t.boolean().optional(),
            "manualAssign": t.boolean().optional(),
            "pool": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAddressPoolOut"])
    types["BareMetalDrainedMachineIn"] = t.struct(
        {"nodeIp": t.string().optional()}
    ).named(renames["BareMetalDrainedMachineIn"])
    types["BareMetalDrainedMachineOut"] = t.struct(
        {
            "nodeIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalDrainedMachineOut"])
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
    types["BareMetalBgpLbConfigIn"] = t.struct(
        {
            "addressPools": t.array(
                t.proxy(renames["BareMetalLoadBalancerAddressPoolIn"])
            ),
            "bgpPeerConfigs": t.array(t.proxy(renames["BareMetalBgpPeerConfigIn"])),
            "asn": t.string(),
            "loadBalancerNodePoolConfig": t.proxy(
                renames["BareMetalLoadBalancerNodePoolConfigIn"]
            ).optional(),
        }
    ).named(renames["BareMetalBgpLbConfigIn"])
    types["BareMetalBgpLbConfigOut"] = t.struct(
        {
            "addressPools": t.array(
                t.proxy(renames["BareMetalLoadBalancerAddressPoolOut"])
            ),
            "bgpPeerConfigs": t.array(t.proxy(renames["BareMetalBgpPeerConfigOut"])),
            "asn": t.string(),
            "loadBalancerNodePoolConfig": t.proxy(
                renames["BareMetalLoadBalancerNodePoolConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalBgpLbConfigOut"])
    types["BareMetalAdminStorageConfigIn"] = t.struct(
        {
            "lvpNodeMountsConfig": t.proxy(renames["BareMetalLvpConfigIn"]),
            "lvpShareConfig": t.proxy(renames["BareMetalLvpShareConfigIn"]),
        }
    ).named(renames["BareMetalAdminStorageConfigIn"])
    types["BareMetalAdminStorageConfigOut"] = t.struct(
        {
            "lvpNodeMountsConfig": t.proxy(renames["BareMetalLvpConfigOut"]),
            "lvpShareConfig": t.proxy(renames["BareMetalLvpShareConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminStorageConfigOut"])
    types["VmwareAdminMetalLbConfigIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VmwareAdminMetalLbConfigIn"]
    )
    types["VmwareAdminMetalLbConfigOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VmwareAdminMetalLbConfigOut"])
    types["BareMetalAdminNetworkConfigIn"] = t.struct(
        {
            "islandModeCidr": t.proxy(
                renames["BareMetalAdminIslandModeCidrConfigIn"]
            ).optional()
        }
    ).named(renames["BareMetalAdminNetworkConfigIn"])
    types["BareMetalAdminNetworkConfigOut"] = t.struct(
        {
            "islandModeCidr": t.proxy(
                renames["BareMetalAdminIslandModeCidrConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminNetworkConfigOut"])
    types["VmwareStaticIpConfigIn"] = t.struct(
        {"ipBlocks": t.array(t.proxy(renames["VmwareIpBlockIn"])).optional()}
    ).named(renames["VmwareStaticIpConfigIn"])
    types["VmwareStaticIpConfigOut"] = t.struct(
        {
            "ipBlocks": t.array(t.proxy(renames["VmwareIpBlockOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareStaticIpConfigOut"])
    types["ListBareMetalNodePoolsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "bareMetalNodePools": t.array(
                t.proxy(renames["BareMetalNodePoolIn"])
            ).optional(),
        }
    ).named(renames["ListBareMetalNodePoolsResponseIn"])
    types["ListBareMetalNodePoolsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "bareMetalNodePools": t.array(
                t.proxy(renames["BareMetalNodePoolOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBareMetalNodePoolsResponseOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["VmwareVsphereTagIn"] = t.struct(
        {"category": t.string().optional(), "tag": t.string().optional()}
    ).named(renames["VmwareVsphereTagIn"])
    types["VmwareVsphereTagOut"] = t.struct(
        {
            "category": t.string().optional(),
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareVsphereTagOut"])
    types["ValidationCheckStatusIn"] = t.struct(
        {"result": t.array(t.proxy(renames["ValidationCheckResultIn"])).optional()}
    ).named(renames["ValidationCheckStatusIn"])
    types["ValidationCheckStatusOut"] = t.struct(
        {
            "result": t.array(t.proxy(renames["ValidationCheckResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationCheckStatusOut"])
    types["BareMetalAdminMaintenanceStatusIn"] = t.struct(
        {
            "machineDrainStatus": t.proxy(
                renames["BareMetalAdminMachineDrainStatusIn"]
            ).optional()
        }
    ).named(renames["BareMetalAdminMaintenanceStatusIn"])
    types["BareMetalAdminMaintenanceStatusOut"] = t.struct(
        {
            "machineDrainStatus": t.proxy(
                renames["BareMetalAdminMachineDrainStatusOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminMaintenanceStatusOut"])
    types["BareMetalAdminLoadBalancerConfigIn"] = t.struct(
        {
            "manualLbConfig": t.proxy(
                renames["BareMetalAdminManualLbConfigIn"]
            ).optional(),
            "vipConfig": t.proxy(renames["BareMetalAdminVipConfigIn"]).optional(),
            "portConfig": t.proxy(renames["BareMetalAdminPortConfigIn"]).optional(),
        }
    ).named(renames["BareMetalAdminLoadBalancerConfigIn"])
    types["BareMetalAdminLoadBalancerConfigOut"] = t.struct(
        {
            "manualLbConfig": t.proxy(
                renames["BareMetalAdminManualLbConfigOut"]
            ).optional(),
            "vipConfig": t.proxy(renames["BareMetalAdminVipConfigOut"]).optional(),
            "portConfig": t.proxy(renames["BareMetalAdminPortConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminLoadBalancerConfigOut"])
    types["VmwareControlPlaneVsphereConfigIn"] = t.struct(
        {"storagePolicyName": t.string().optional(), "datastore": t.string().optional()}
    ).named(renames["VmwareControlPlaneVsphereConfigIn"])
    types["VmwareControlPlaneVsphereConfigOut"] = t.struct(
        {
            "storagePolicyName": t.string().optional(),
            "datastore": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareControlPlaneVsphereConfigOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["VmwareHostConfigIn"] = t.struct(
        {
            "dnsServers": t.array(t.string()).optional(),
            "dnsSearchDomains": t.array(t.string()).optional(),
            "ntpServers": t.array(t.string()).optional(),
        }
    ).named(renames["VmwareHostConfigIn"])
    types["VmwareHostConfigOut"] = t.struct(
        {
            "dnsServers": t.array(t.string()).optional(),
            "dnsSearchDomains": t.array(t.string()).optional(),
            "ntpServers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareHostConfigOut"])
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
    types["BareMetalAdminControlPlaneNodePoolConfigIn"] = t.struct(
        {"nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigIn"]).optional()}
    ).named(renames["BareMetalAdminControlPlaneNodePoolConfigIn"])
    types["BareMetalAdminControlPlaneNodePoolConfigOut"] = t.struct(
        {
            "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminControlPlaneNodePoolConfigOut"])
    types["VmwareNodePoolIn"] = t.struct(
        {
            "nodePoolAutoscaling": t.proxy(
                renames["VmwareNodePoolAutoscalingConfigIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "config": t.proxy(renames["VmwareNodeConfigIn"]),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "onPremVersion": t.string().optional(),
        }
    ).named(renames["VmwareNodePoolIn"])
    types["VmwareNodePoolOut"] = t.struct(
        {
            "nodePoolAutoscaling": t.proxy(
                renames["VmwareNodePoolAutoscalingConfigOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "uid": t.string().optional(),
            "deleteTime": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "etag": t.string().optional(),
            "config": t.proxy(renames["VmwareNodeConfigOut"]),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "onPremVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareNodePoolOut"])
    types["VmwareStorageConfigIn"] = t.struct(
        {"vsphereCsiDisabled": t.boolean().optional()}
    ).named(renames["VmwareStorageConfigIn"])
    types["VmwareStorageConfigOut"] = t.struct(
        {
            "vsphereCsiDisabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareStorageConfigOut"])
    types["ClusterUserIn"] = t.struct({"username": t.string()}).named(
        renames["ClusterUserIn"]
    )
    types["ClusterUserOut"] = t.struct(
        {"username": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ClusterUserOut"])
    types["VmwareAdminManualLbConfigIn"] = t.struct(
        {
            "controlPlaneNodePort": t.integer().optional(),
            "konnectivityServerNodePort": t.integer().optional(),
            "ingressHttpsNodePort": t.integer().optional(),
            "addonsNodePort": t.integer().optional(),
            "ingressHttpNodePort": t.integer().optional(),
        }
    ).named(renames["VmwareAdminManualLbConfigIn"])
    types["VmwareAdminManualLbConfigOut"] = t.struct(
        {
            "controlPlaneNodePort": t.integer().optional(),
            "konnectivityServerNodePort": t.integer().optional(),
            "ingressHttpsNodePort": t.integer().optional(),
            "addonsNodePort": t.integer().optional(),
            "ingressHttpNodePort": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAdminManualLbConfigOut"])
    types["QueryVmwareVersionConfigResponseIn"] = t.struct(
        {"versions": t.array(t.proxy(renames["VmwareVersionInfoIn"])).optional()}
    ).named(renames["QueryVmwareVersionConfigResponseIn"])
    types["QueryVmwareVersionConfigResponseOut"] = t.struct(
        {
            "versions": t.array(t.proxy(renames["VmwareVersionInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryVmwareVersionConfigResponseOut"])
    types["BareMetalAdminNodeAccessConfigIn"] = t.struct(
        {"loginUser": t.string()}
    ).named(renames["BareMetalAdminNodeAccessConfigIn"])
    types["BareMetalAdminNodeAccessConfigOut"] = t.struct(
        {"loginUser": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["BareMetalAdminNodeAccessConfigOut"])
    types["BareMetalKubeletConfigIn"] = t.struct(
        {
            "serializeImagePullsDisabled": t.boolean().optional(),
            "registryPullQps": t.integer().optional(),
            "registryBurst": t.integer().optional(),
        }
    ).named(renames["BareMetalKubeletConfigIn"])
    types["BareMetalKubeletConfigOut"] = t.struct(
        {
            "serializeImagePullsDisabled": t.boolean().optional(),
            "registryPullQps": t.integer().optional(),
            "registryBurst": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalKubeletConfigOut"])
    types["ResourceStatusIn"] = t.struct(
        {
            "conditions": t.array(t.proxy(renames["ResourceConditionIn"])).optional(),
            "errorMessage": t.string().optional(),
        }
    ).named(renames["ResourceStatusIn"])
    types["ResourceStatusOut"] = t.struct(
        {
            "conditions": t.array(t.proxy(renames["ResourceConditionOut"])).optional(),
            "errorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceStatusOut"])
    types["BareMetalNodePoolUpgradePolicyIn"] = t.struct(
        {
            "parallelUpgradeConfig": t.proxy(
                renames["BareMetalParallelUpgradeConfigIn"]
            ).optional()
        }
    ).named(renames["BareMetalNodePoolUpgradePolicyIn"])
    types["BareMetalNodePoolUpgradePolicyOut"] = t.struct(
        {
            "parallelUpgradeConfig": t.proxy(
                renames["BareMetalParallelUpgradeConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalNodePoolUpgradePolicyOut"])
    types["VmwareAdminNetworkConfigIn"] = t.struct(
        {
            "serviceAddressCidrBlocks": t.array(t.string()),
            "podAddressCidrBlocks": t.array(t.string()),
            "hostConfig": t.proxy(renames["VmwareHostConfigIn"]).optional(),
            "staticIpConfig": t.proxy(renames["VmwareStaticIpConfigIn"]).optional(),
            "dhcpIpConfig": t.proxy(renames["VmwareDhcpIpConfigIn"]).optional(),
            "vcenterNetwork": t.string().optional(),
        }
    ).named(renames["VmwareAdminNetworkConfigIn"])
    types["VmwareAdminNetworkConfigOut"] = t.struct(
        {
            "serviceAddressCidrBlocks": t.array(t.string()),
            "podAddressCidrBlocks": t.array(t.string()),
            "hostConfig": t.proxy(renames["VmwareHostConfigOut"]).optional(),
            "staticIpConfig": t.proxy(renames["VmwareStaticIpConfigOut"]).optional(),
            "dhcpIpConfig": t.proxy(renames["VmwareDhcpIpConfigOut"]).optional(),
            "vcenterNetwork": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAdminNetworkConfigOut"])
    types["FleetIn"] = t.struct({"_": t.string().optional()}).named(renames["FleetIn"])
    types["FleetOut"] = t.struct(
        {
            "membership": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FleetOut"])
    types["BareMetalNodeConfigIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "nodeIp": t.string().optional(),
        }
    ).named(renames["BareMetalNodeConfigIn"])
    types["BareMetalNodeConfigOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "nodeIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalNodeConfigOut"])
    types["BareMetalNodeAccessConfigIn"] = t.struct(
        {"loginUser": t.string().optional()}
    ).named(renames["BareMetalNodeAccessConfigIn"])
    types["BareMetalNodeAccessConfigOut"] = t.struct(
        {
            "loginUser": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalNodeAccessConfigOut"])
    types["BareMetalProxyConfigIn"] = t.struct(
        {"noProxy": t.array(t.string()).optional(), "uri": t.string()}
    ).named(renames["BareMetalProxyConfigIn"])
    types["BareMetalProxyConfigOut"] = t.struct(
        {
            "noProxy": t.array(t.string()).optional(),
            "uri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalProxyConfigOut"])
    types["BareMetalWorkloadNodeConfigIn"] = t.struct(
        {
            "containerRuntime": t.string().optional(),
            "maxPodsPerNode": t.string().optional(),
        }
    ).named(renames["BareMetalWorkloadNodeConfigIn"])
    types["BareMetalWorkloadNodeConfigOut"] = t.struct(
        {
            "containerRuntime": t.string().optional(),
            "maxPodsPerNode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalWorkloadNodeConfigOut"])
    types["VmwareAdminControlPlaneNodeConfigIn"] = t.struct(
        {"memory": t.string().optional(), "cpus": t.string().optional()}
    ).named(renames["VmwareAdminControlPlaneNodeConfigIn"])
    types["VmwareAdminControlPlaneNodeConfigOut"] = t.struct(
        {
            "memory": t.string().optional(),
            "cpus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAdminControlPlaneNodeConfigOut"])
    types["BareMetalAdminDrainedMachineIn"] = t.struct(
        {"nodeIp": t.string().optional()}
    ).named(renames["BareMetalAdminDrainedMachineIn"])
    types["BareMetalAdminDrainedMachineOut"] = t.struct(
        {
            "nodeIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminDrainedMachineOut"])
    types["UpgradeDependencyIn"] = t.struct(
        {
            "currentVersion": t.string().optional(),
            "resourceName": t.string().optional(),
            "localName": t.string().optional(),
            "targetVersion": t.string().optional(),
        }
    ).named(renames["UpgradeDependencyIn"])
    types["UpgradeDependencyOut"] = t.struct(
        {
            "currentVersion": t.string().optional(),
            "resourceName": t.string().optional(),
            "localName": t.string().optional(),
            "targetVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeDependencyOut"])
    types["BareMetalLoadBalancerNodePoolConfigIn"] = t.struct(
        {"nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigIn"]).optional()}
    ).named(renames["BareMetalLoadBalancerNodePoolConfigIn"])
    types["BareMetalLoadBalancerNodePoolConfigOut"] = t.struct(
        {
            "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalLoadBalancerNodePoolConfigOut"])
    types["BareMetalNodePoolConfigIn"] = t.struct(
        {
            "nodeConfigs": t.array(t.proxy(renames["BareMetalNodeConfigIn"])),
            "kubeletConfig": t.proxy(renames["BareMetalKubeletConfigIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "taints": t.array(t.proxy(renames["NodeTaintIn"])).optional(),
            "operatingSystem": t.string().optional(),
        }
    ).named(renames["BareMetalNodePoolConfigIn"])
    types["BareMetalNodePoolConfigOut"] = t.struct(
        {
            "nodeConfigs": t.array(t.proxy(renames["BareMetalNodeConfigOut"])),
            "kubeletConfig": t.proxy(renames["BareMetalKubeletConfigOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "taints": t.array(t.proxy(renames["NodeTaintOut"])).optional(),
            "operatingSystem": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalNodePoolConfigOut"])
    types["BareMetalLoadBalancerConfigIn"] = t.struct(
        {
            "manualLbConfig": t.proxy(renames["BareMetalManualLbConfigIn"]).optional(),
            "bgpLbConfig": t.proxy(renames["BareMetalBgpLbConfigIn"]).optional(),
            "metalLbConfig": t.proxy(renames["BareMetalMetalLbConfigIn"]).optional(),
            "vipConfig": t.proxy(renames["BareMetalVipConfigIn"]).optional(),
            "portConfig": t.proxy(renames["BareMetalPortConfigIn"]).optional(),
        }
    ).named(renames["BareMetalLoadBalancerConfigIn"])
    types["BareMetalLoadBalancerConfigOut"] = t.struct(
        {
            "manualLbConfig": t.proxy(renames["BareMetalManualLbConfigOut"]).optional(),
            "bgpLbConfig": t.proxy(renames["BareMetalBgpLbConfigOut"]).optional(),
            "metalLbConfig": t.proxy(renames["BareMetalMetalLbConfigOut"]).optional(),
            "vipConfig": t.proxy(renames["BareMetalVipConfigOut"]).optional(),
            "portConfig": t.proxy(renames["BareMetalPortConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalLoadBalancerConfigOut"])
    types["BareMetalNetworkConfigIn"] = t.struct(
        {
            "multipleNetworkInterfacesConfig": t.proxy(
                renames["BareMetalMultipleNetworkInterfacesConfigIn"]
            ).optional(),
            "islandModeCidr": t.proxy(
                renames["BareMetalIslandModeCidrConfigIn"]
            ).optional(),
            "advancedNetworking": t.boolean().optional(),
            "srIovConfig": t.proxy(renames["BareMetalSrIovConfigIn"]).optional(),
        }
    ).named(renames["BareMetalNetworkConfigIn"])
    types["BareMetalNetworkConfigOut"] = t.struct(
        {
            "multipleNetworkInterfacesConfig": t.proxy(
                renames["BareMetalMultipleNetworkInterfacesConfigOut"]
            ).optional(),
            "islandModeCidr": t.proxy(
                renames["BareMetalIslandModeCidrConfigOut"]
            ).optional(),
            "advancedNetworking": t.boolean().optional(),
            "srIovConfig": t.proxy(renames["BareMetalSrIovConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalNetworkConfigOut"])
    types["EnrollBareMetalNodePoolRequestIn"] = t.struct(
        {
            "bareMetalNodePoolId": t.string().optional(),
            "validateOnly": t.boolean().optional(),
        }
    ).named(renames["EnrollBareMetalNodePoolRequestIn"])
    types["EnrollBareMetalNodePoolRequestOut"] = t.struct(
        {
            "bareMetalNodePoolId": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollBareMetalNodePoolRequestOut"])
    types["ListBareMetalClustersResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "bareMetalClusters": t.array(
                t.proxy(renames["BareMetalClusterIn"])
            ).optional(),
        }
    ).named(renames["ListBareMetalClustersResponseIn"])
    types["ListBareMetalClustersResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "bareMetalClusters": t.array(
                t.proxy(renames["BareMetalClusterOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBareMetalClustersResponseOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["BareMetalBgpPeerConfigIn"] = t.struct(
        {
            "controlPlaneNodes": t.array(t.string()).optional(),
            "asn": t.string(),
            "ipAddress": t.string(),
        }
    ).named(renames["BareMetalBgpPeerConfigIn"])
    types["BareMetalBgpPeerConfigOut"] = t.struct(
        {
            "controlPlaneNodes": t.array(t.string()).optional(),
            "asn": t.string(),
            "ipAddress": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalBgpPeerConfigOut"])
    types["BareMetalAdminVipConfigIn"] = t.struct(
        {"controlPlaneVip": t.string().optional()}
    ).named(renames["BareMetalAdminVipConfigIn"])
    types["BareMetalAdminVipConfigOut"] = t.struct(
        {
            "controlPlaneVip": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminVipConfigOut"])
    types["BareMetalControlPlaneNodePoolConfigIn"] = t.struct(
        {"nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigIn"])}
    ).named(renames["BareMetalControlPlaneNodePoolConfigIn"])
    types["BareMetalControlPlaneNodePoolConfigOut"] = t.struct(
        {
            "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalControlPlaneNodePoolConfigOut"])
    types["BareMetalVersionInfoIn"] = t.struct(
        {
            "dependencies": t.array(t.proxy(renames["UpgradeDependencyIn"])).optional(),
            "version": t.string().optional(),
            "hasDependencies": t.boolean().optional(),
        }
    ).named(renames["BareMetalVersionInfoIn"])
    types["BareMetalVersionInfoOut"] = t.struct(
        {
            "dependencies": t.array(
                t.proxy(renames["UpgradeDependencyOut"])
            ).optional(),
            "version": t.string().optional(),
            "hasDependencies": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalVersionInfoOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["VmwareAdminVCenterConfigIn"] = t.struct(
        {
            "datastore": t.string().optional(),
            "address": t.string().optional(),
            "caCertData": t.string().optional(),
            "folder": t.string().optional(),
            "cluster": t.string().optional(),
            "resourcePool": t.string().optional(),
            "datacenter": t.string().optional(),
            "dataDisk": t.string().optional(),
        }
    ).named(renames["VmwareAdminVCenterConfigIn"])
    types["VmwareAdminVCenterConfigOut"] = t.struct(
        {
            "datastore": t.string().optional(),
            "address": t.string().optional(),
            "caCertData": t.string().optional(),
            "folder": t.string().optional(),
            "cluster": t.string().optional(),
            "resourcePool": t.string().optional(),
            "datacenter": t.string().optional(),
            "dataDisk": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAdminVCenterConfigOut"])
    types["VmwareAdminAddonNodeConfigIn"] = t.struct(
        {"autoResizeConfig": t.proxy(renames["VmwareAutoResizeConfigIn"]).optional()}
    ).named(renames["VmwareAdminAddonNodeConfigIn"])
    types["VmwareAdminAddonNodeConfigOut"] = t.struct(
        {
            "autoResizeConfig": t.proxy(
                renames["VmwareAutoResizeConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAdminAddonNodeConfigOut"])
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["VmwareNodeConfigIn"] = t.struct(
        {
            "image": t.string().optional(),
            "imageType": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "bootDiskSizeGb": t.string().optional(),
            "replicas": t.string().optional(),
            "taints": t.array(t.proxy(renames["NodeTaintIn"])).optional(),
            "cpus": t.string().optional(),
            "enableLoadBalancer": t.boolean().optional(),
            "memoryMb": t.string().optional(),
        }
    ).named(renames["VmwareNodeConfigIn"])
    types["VmwareNodeConfigOut"] = t.struct(
        {
            "image": t.string().optional(),
            "imageType": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "vsphereConfig": t.proxy(renames["VmwareVsphereConfigOut"]).optional(),
            "bootDiskSizeGb": t.string().optional(),
            "replicas": t.string().optional(),
            "taints": t.array(t.proxy(renames["NodeTaintOut"])).optional(),
            "cpus": t.string().optional(),
            "enableLoadBalancer": t.boolean().optional(),
            "memoryMb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareNodeConfigOut"])
    types["VmwareBundleConfigIn"] = t.struct({"version": t.string().optional()}).named(
        renames["VmwareBundleConfigIn"]
    )
    types["VmwareBundleConfigOut"] = t.struct(
        {
            "version": t.string().optional(),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareBundleConfigOut"])
    types["VmwareAdminLoadBalancerConfigIn"] = t.struct(
        {
            "manualLbConfig": t.proxy(
                renames["VmwareAdminManualLbConfigIn"]
            ).optional(),
            "metalLbConfig": t.proxy(renames["VmwareAdminMetalLbConfigIn"]).optional(),
            "vipConfig": t.proxy(renames["VmwareAdminVipConfigIn"]).optional(),
            "f5Config": t.proxy(renames["VmwareAdminF5BigIpConfigIn"]).optional(),
        }
    ).named(renames["VmwareAdminLoadBalancerConfigIn"])
    types["VmwareAdminLoadBalancerConfigOut"] = t.struct(
        {
            "manualLbConfig": t.proxy(
                renames["VmwareAdminManualLbConfigOut"]
            ).optional(),
            "metalLbConfig": t.proxy(renames["VmwareAdminMetalLbConfigOut"]).optional(),
            "vipConfig": t.proxy(renames["VmwareAdminVipConfigOut"]).optional(),
            "f5Config": t.proxy(renames["VmwareAdminF5BigIpConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAdminLoadBalancerConfigOut"])
    types["ValidationCheckIn"] = t.struct({"option": t.string().optional()}).named(
        renames["ValidationCheckIn"]
    )
    types["ValidationCheckOut"] = t.struct(
        {
            "scenario": t.string().optional(),
            "option": t.string().optional(),
            "status": t.proxy(renames["ValidationCheckStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationCheckOut"])
    types["ResourceConditionIn"] = t.struct(
        {
            "reason": t.string().optional(),
            "state": t.string().optional(),
            "lastTransitionTime": t.string().optional(),
            "type": t.string().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["ResourceConditionIn"])
    types["ResourceConditionOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "state": t.string().optional(),
            "lastTransitionTime": t.string().optional(),
            "type": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceConditionOut"])
    types["VmwareF5BigIpConfigIn"] = t.struct(
        {
            "partition": t.string().optional(),
            "address": t.string().optional(),
            "snatPool": t.string().optional(),
        }
    ).named(renames["VmwareF5BigIpConfigIn"])
    types["VmwareF5BigIpConfigOut"] = t.struct(
        {
            "partition": t.string().optional(),
            "address": t.string().optional(),
            "snatPool": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareF5BigIpConfigOut"])
    types["BareMetalAdminSecurityConfigIn"] = t.struct(
        {"authorization": t.proxy(renames["AuthorizationIn"]).optional()}
    ).named(renames["BareMetalAdminSecurityConfigIn"])
    types["BareMetalAdminSecurityConfigOut"] = t.struct(
        {
            "authorization": t.proxy(renames["AuthorizationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminSecurityConfigOut"])
    types["BareMetalAdminMaintenanceConfigIn"] = t.struct(
        {"maintenanceAddressCidrBlocks": t.array(t.string())}
    ).named(renames["BareMetalAdminMaintenanceConfigIn"])
    types["BareMetalAdminMaintenanceConfigOut"] = t.struct(
        {
            "maintenanceAddressCidrBlocks": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminMaintenanceConfigOut"])
    types["BareMetalMaintenanceConfigIn"] = t.struct(
        {"maintenanceAddressCidrBlocks": t.array(t.string())}
    ).named(renames["BareMetalMaintenanceConfigIn"])
    types["BareMetalMaintenanceConfigOut"] = t.struct(
        {
            "maintenanceAddressCidrBlocks": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalMaintenanceConfigOut"])
    types["VmwareDataplaneV2ConfigIn"] = t.struct(
        {
            "windowsDataplaneV2Enabled": t.boolean().optional(),
            "advancedNetworking": t.boolean().optional(),
            "dataplaneV2Enabled": t.boolean().optional(),
        }
    ).named(renames["VmwareDataplaneV2ConfigIn"])
    types["VmwareDataplaneV2ConfigOut"] = t.struct(
        {
            "windowsDataplaneV2Enabled": t.boolean().optional(),
            "advancedNetworking": t.boolean().optional(),
            "dataplaneV2Enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareDataplaneV2ConfigOut"])
    types["BareMetalAdminManualLbConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["BareMetalAdminManualLbConfigIn"])
    types["BareMetalAdminManualLbConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminManualLbConfigOut"])
    types["VmwareClusterIn"] = t.struct(
        {
            "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigIn"]).optional(),
            "loadBalancer": t.proxy(renames["VmwareLoadBalancerConfigIn"]).optional(),
            "adminClusterMembership": t.string(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "authorization": t.proxy(renames["AuthorizationIn"]).optional(),
            "vmTrackingEnabled": t.boolean().optional(),
            "autoRepairConfig": t.proxy(renames["VmwareAutoRepairConfigIn"]).optional(),
            "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "controlPlaneNode": t.proxy(
                renames["VmwareControlPlaneNodeConfigIn"]
            ).optional(),
            "storage": t.proxy(renames["VmwareStorageConfigIn"]).optional(),
            "enableControlPlaneV2": t.boolean().optional(),
            "onPremVersion": t.string(),
            "networkConfig": t.proxy(renames["VmwareNetworkConfigIn"]).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["VmwareClusterIn"])
    types["VmwareClusterOut"] = t.struct(
        {
            "reconciling": t.boolean().optional(),
            "adminClusterName": t.string().optional(),
            "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigOut"]).optional(),
            "loadBalancer": t.proxy(renames["VmwareLoadBalancerConfigOut"]).optional(),
            "adminClusterMembership": t.string(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "authorization": t.proxy(renames["AuthorizationOut"]).optional(),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "vmTrackingEnabled": t.boolean().optional(),
            "createTime": t.string().optional(),
            "autoRepairConfig": t.proxy(
                renames["VmwareAutoRepairConfigOut"]
            ).optional(),
            "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigOut"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "endpoint": t.string().optional(),
            "fleet": t.proxy(renames["FleetOut"]).optional(),
            "state": t.string().optional(),
            "uid": t.string().optional(),
            "controlPlaneNode": t.proxy(
                renames["VmwareControlPlaneNodeConfigOut"]
            ).optional(),
            "localName": t.string().optional(),
            "vcenter": t.proxy(renames["VmwareVCenterConfigOut"]).optional(),
            "storage": t.proxy(renames["VmwareStorageConfigOut"]).optional(),
            "enableControlPlaneV2": t.boolean().optional(),
            "onPremVersion": t.string(),
            "networkConfig": t.proxy(renames["VmwareNetworkConfigOut"]).optional(),
            "validationCheck": t.proxy(renames["ValidationCheckOut"]).optional(),
            "description": t.string().optional(),
            "deleteTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareClusterOut"])
    types["VmwareHostIpIn"] = t.struct(
        {"hostname": t.string().optional(), "ip": t.string().optional()}
    ).named(renames["VmwareHostIpIn"])
    types["VmwareHostIpOut"] = t.struct(
        {
            "hostname": t.string().optional(),
            "ip": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareHostIpOut"])
    types["BareMetalLoadBalancerAddressPoolIn"] = t.struct(
        {
            "avoidBuggyIps": t.boolean().optional(),
            "addresses": t.array(t.string()),
            "pool": t.string(),
            "manualAssign": t.boolean().optional(),
        }
    ).named(renames["BareMetalLoadBalancerAddressPoolIn"])
    types["BareMetalLoadBalancerAddressPoolOut"] = t.struct(
        {
            "avoidBuggyIps": t.boolean().optional(),
            "addresses": t.array(t.string()),
            "pool": t.string(),
            "manualAssign": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalLoadBalancerAddressPoolOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["VmwareAdminF5BigIpConfigIn"] = t.struct(
        {
            "address": t.string().optional(),
            "partition": t.string().optional(),
            "snatPool": t.string().optional(),
        }
    ).named(renames["VmwareAdminF5BigIpConfigIn"])
    types["VmwareAdminF5BigIpConfigOut"] = t.struct(
        {
            "address": t.string().optional(),
            "partition": t.string().optional(),
            "snatPool": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAdminF5BigIpConfigOut"])
    types["BareMetalDrainingMachineIn"] = t.struct(
        {"podCount": t.integer().optional(), "nodeIp": t.string().optional()}
    ).named(renames["BareMetalDrainingMachineIn"])
    types["BareMetalDrainingMachineOut"] = t.struct(
        {
            "podCount": t.integer().optional(),
            "nodeIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalDrainingMachineOut"])
    types["BareMetalSecurityConfigIn"] = t.struct(
        {"authorization": t.proxy(renames["AuthorizationIn"]).optional()}
    ).named(renames["BareMetalSecurityConfigIn"])
    types["BareMetalSecurityConfigOut"] = t.struct(
        {
            "authorization": t.proxy(renames["AuthorizationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalSecurityConfigOut"])
    types["VmwareAdminVipConfigIn"] = t.struct(
        {"controlPlaneVip": t.string().optional(), "addonsVip": t.string().optional()}
    ).named(renames["VmwareAdminVipConfigIn"])
    types["VmwareAdminVipConfigOut"] = t.struct(
        {
            "controlPlaneVip": t.string().optional(),
            "addonsVip": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAdminVipConfigOut"])
    types["EnrollVmwareNodePoolRequestIn"] = t.struct(
        {"vmwareNodePoolId": t.string().optional()}
    ).named(renames["EnrollVmwareNodePoolRequestIn"])
    types["EnrollVmwareNodePoolRequestOut"] = t.struct(
        {
            "vmwareNodePoolId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollVmwareNodePoolRequestOut"])
    types["BareMetalMetalLbConfigIn"] = t.struct(
        {
            "addressPools": t.array(
                t.proxy(renames["BareMetalLoadBalancerAddressPoolIn"])
            ),
            "loadBalancerNodePoolConfig": t.proxy(
                renames["BareMetalLoadBalancerNodePoolConfigIn"]
            ).optional(),
        }
    ).named(renames["BareMetalMetalLbConfigIn"])
    types["BareMetalMetalLbConfigOut"] = t.struct(
        {
            "addressPools": t.array(
                t.proxy(renames["BareMetalLoadBalancerAddressPoolOut"])
            ),
            "loadBalancerNodePoolConfig": t.proxy(
                renames["BareMetalLoadBalancerNodePoolConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalMetalLbConfigOut"])
    types["BareMetalAdminProxyConfigIn"] = t.struct(
        {"uri": t.string(), "noProxy": t.array(t.string()).optional()}
    ).named(renames["BareMetalAdminProxyConfigIn"])
    types["BareMetalAdminProxyConfigOut"] = t.struct(
        {
            "uri": t.string(),
            "noProxy": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminProxyConfigOut"])
    types["QueryBareMetalAdminVersionConfigResponseIn"] = t.struct(
        {"versions": t.array(t.proxy(renames["BareMetalVersionInfoIn"])).optional()}
    ).named(renames["QueryBareMetalAdminVersionConfigResponseIn"])
    types["QueryBareMetalAdminVersionConfigResponseOut"] = t.struct(
        {
            "versions": t.array(t.proxy(renames["BareMetalVersionInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryBareMetalAdminVersionConfigResponseOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["BareMetalMachineDrainStatusIn"] = t.struct(
        {
            "drainedMachines": t.array(
                t.proxy(renames["BareMetalDrainedMachineIn"])
            ).optional(),
            "drainingMachines": t.array(
                t.proxy(renames["BareMetalDrainingMachineIn"])
            ).optional(),
        }
    ).named(renames["BareMetalMachineDrainStatusIn"])
    types["BareMetalMachineDrainStatusOut"] = t.struct(
        {
            "drainedMachines": t.array(
                t.proxy(renames["BareMetalDrainedMachineOut"])
            ).optional(),
            "drainingMachines": t.array(
                t.proxy(renames["BareMetalDrainingMachineOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalMachineDrainStatusOut"])
    types["BareMetalIslandModeCidrConfigIn"] = t.struct(
        {
            "serviceAddressCidrBlocks": t.array(t.string()),
            "podAddressCidrBlocks": t.array(t.string()),
        }
    ).named(renames["BareMetalIslandModeCidrConfigIn"])
    types["BareMetalIslandModeCidrConfigOut"] = t.struct(
        {
            "serviceAddressCidrBlocks": t.array(t.string()),
            "podAddressCidrBlocks": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalIslandModeCidrConfigOut"])
    types["EnrollVmwareClusterRequestIn"] = t.struct(
        {
            "vmwareClusterId": t.string().optional(),
            "adminClusterMembership": t.string(),
            "localName": t.string().optional(),
            "validateOnly": t.boolean().optional(),
        }
    ).named(renames["EnrollVmwareClusterRequestIn"])
    types["EnrollVmwareClusterRequestOut"] = t.struct(
        {
            "vmwareClusterId": t.string().optional(),
            "adminClusterMembership": t.string(),
            "localName": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollVmwareClusterRequestOut"])
    types["BareMetalAdminWorkloadNodeConfigIn"] = t.struct(
        {"maxPodsPerNode": t.string().optional()}
    ).named(renames["BareMetalAdminWorkloadNodeConfigIn"])
    types["BareMetalAdminWorkloadNodeConfigOut"] = t.struct(
        {
            "maxPodsPerNode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminWorkloadNodeConfigOut"])
    types["VmwareManualLbConfigIn"] = t.struct(
        {
            "ingressHttpNodePort": t.integer().optional(),
            "ingressHttpsNodePort": t.integer().optional(),
            "controlPlaneNodePort": t.integer().optional(),
            "konnectivityServerNodePort": t.integer().optional(),
        }
    ).named(renames["VmwareManualLbConfigIn"])
    types["VmwareManualLbConfigOut"] = t.struct(
        {
            "ingressHttpNodePort": t.integer().optional(),
            "ingressHttpsNodePort": t.integer().optional(),
            "controlPlaneNodePort": t.integer().optional(),
            "konnectivityServerNodePort": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareManualLbConfigOut"])
    types["BareMetalApiServerArgumentIn"] = t.struct(
        {"argument": t.string(), "value": t.string()}
    ).named(renames["BareMetalApiServerArgumentIn"])
    types["BareMetalApiServerArgumentOut"] = t.struct(
        {
            "argument": t.string(),
            "value": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalApiServerArgumentOut"])
    types["VmwareAAGConfigIn"] = t.struct(
        {"aagConfigDisabled": t.boolean().optional()}
    ).named(renames["VmwareAAGConfigIn"])
    types["VmwareAAGConfigOut"] = t.struct(
        {
            "aagConfigDisabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAAGConfigOut"])
    types["BareMetalAdminControlPlaneConfigIn"] = t.struct(
        {
            "controlPlaneNodePoolConfig": t.proxy(
                renames["BareMetalAdminControlPlaneNodePoolConfigIn"]
            ).optional(),
            "apiServerArgs": t.array(
                t.proxy(renames["BareMetalAdminApiServerArgumentIn"])
            ).optional(),
        }
    ).named(renames["BareMetalAdminControlPlaneConfigIn"])
    types["BareMetalAdminControlPlaneConfigOut"] = t.struct(
        {
            "controlPlaneNodePoolConfig": t.proxy(
                renames["BareMetalAdminControlPlaneNodePoolConfigOut"]
            ).optional(),
            "apiServerArgs": t.array(
                t.proxy(renames["BareMetalAdminApiServerArgumentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminControlPlaneConfigOut"])
    types["BareMetalAdminMachineDrainStatusIn"] = t.struct(
        {
            "drainedMachines": t.array(
                t.proxy(renames["BareMetalAdminDrainedMachineIn"])
            ).optional(),
            "drainingMachines": t.array(
                t.proxy(renames["BareMetalAdminDrainingMachineIn"])
            ).optional(),
        }
    ).named(renames["BareMetalAdminMachineDrainStatusIn"])
    types["BareMetalAdminMachineDrainStatusOut"] = t.struct(
        {
            "drainedMachines": t.array(
                t.proxy(renames["BareMetalAdminDrainedMachineOut"])
            ).optional(),
            "drainingMachines": t.array(
                t.proxy(renames["BareMetalAdminDrainingMachineOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminMachineDrainStatusOut"])
    types["EnrollVmwareAdminClusterRequestIn"] = t.struct(
        {"vmwareAdminClusterId": t.string().optional(), "membership": t.string()}
    ).named(renames["EnrollVmwareAdminClusterRequestIn"])
    types["EnrollVmwareAdminClusterRequestOut"] = t.struct(
        {
            "vmwareAdminClusterId": t.string().optional(),
            "membership": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollVmwareAdminClusterRequestOut"])
    types["ListVmwareAdminClustersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "vmwareAdminClusters": t.array(
                t.proxy(renames["VmwareAdminClusterIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListVmwareAdminClustersResponseIn"])
    types["ListVmwareAdminClustersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "vmwareAdminClusters": t.array(
                t.proxy(renames["VmwareAdminClusterOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVmwareAdminClustersResponseOut"])
    types["BareMetalSrIovConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["BareMetalSrIovConfigIn"])
    types["BareMetalSrIovConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalSrIovConfigOut"])
    types["ListVmwareNodePoolsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "vmwareNodePools": t.array(t.proxy(renames["VmwareNodePoolIn"])).optional(),
        }
    ).named(renames["ListVmwareNodePoolsResponseIn"])
    types["ListVmwareNodePoolsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "vmwareNodePools": t.array(
                t.proxy(renames["VmwareNodePoolOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVmwareNodePoolsResponseOut"])
    types["BareMetalPortConfigIn"] = t.struct(
        {"controlPlaneLoadBalancerPort": t.integer().optional()}
    ).named(renames["BareMetalPortConfigIn"])
    types["BareMetalPortConfigOut"] = t.struct(
        {
            "controlPlaneLoadBalancerPort": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalPortConfigOut"])
    types["EnrollBareMetalAdminClusterRequestIn"] = t.struct(
        {"membership": t.string(), "bareMetalAdminClusterId": t.string().optional()}
    ).named(renames["EnrollBareMetalAdminClusterRequestIn"])
    types["EnrollBareMetalAdminClusterRequestOut"] = t.struct(
        {
            "membership": t.string(),
            "bareMetalAdminClusterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollBareMetalAdminClusterRequestOut"])
    types["BareMetalVipConfigIn"] = t.struct(
        {"ingressVip": t.string().optional(), "controlPlaneVip": t.string().optional()}
    ).named(renames["BareMetalVipConfigIn"])
    types["BareMetalVipConfigOut"] = t.struct(
        {
            "ingressVip": t.string().optional(),
            "controlPlaneVip": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalVipConfigOut"])
    types["VmwareNetworkConfigIn"] = t.struct(
        {
            "podAddressCidrBlocks": t.array(t.string()),
            "hostConfig": t.proxy(renames["VmwareHostConfigIn"]).optional(),
            "dhcpIpConfig": t.proxy(renames["VmwareDhcpIpConfigIn"]).optional(),
            "staticIpConfig": t.proxy(renames["VmwareStaticIpConfigIn"]).optional(),
            "serviceAddressCidrBlocks": t.array(t.string()),
            "controlPlaneV2Config": t.proxy(
                renames["VmwareControlPlaneV2ConfigIn"]
            ).optional(),
        }
    ).named(renames["VmwareNetworkConfigIn"])
    types["VmwareNetworkConfigOut"] = t.struct(
        {
            "podAddressCidrBlocks": t.array(t.string()),
            "hostConfig": t.proxy(renames["VmwareHostConfigOut"]).optional(),
            "dhcpIpConfig": t.proxy(renames["VmwareDhcpIpConfigOut"]).optional(),
            "vcenterNetwork": t.string().optional(),
            "staticIpConfig": t.proxy(renames["VmwareStaticIpConfigOut"]).optional(),
            "serviceAddressCidrBlocks": t.array(t.string()),
            "controlPlaneV2Config": t.proxy(
                renames["VmwareControlPlaneV2ConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareNetworkConfigOut"])
    types["BareMetalClusterIn"] = t.struct(
        {
            "osEnvironmentConfig": t.proxy(
                renames["BareMetalOsEnvironmentConfigIn"]
            ).optional(),
            "bareMetalVersion": t.string(),
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "maintenanceConfig": t.proxy(
                renames["BareMetalMaintenanceConfigIn"]
            ).optional(),
            "storage": t.proxy(renames["BareMetalStorageConfigIn"]),
            "proxy": t.proxy(renames["BareMetalProxyConfigIn"]).optional(),
            "loadBalancer": t.proxy(renames["BareMetalLoadBalancerConfigIn"]),
            "description": t.string().optional(),
            "nodeAccessConfig": t.proxy(
                renames["BareMetalNodeAccessConfigIn"]
            ).optional(),
            "controlPlane": t.proxy(renames["BareMetalControlPlaneConfigIn"]),
            "networkConfig": t.proxy(renames["BareMetalNetworkConfigIn"]),
            "nodeConfig": t.proxy(renames["BareMetalWorkloadNodeConfigIn"]).optional(),
            "securityConfig": t.proxy(renames["BareMetalSecurityConfigIn"]).optional(),
            "adminClusterMembership": t.string(),
            "clusterOperations": t.proxy(
                renames["BareMetalClusterOperationsConfigIn"]
            ).optional(),
        }
    ).named(renames["BareMetalClusterIn"])
    types["BareMetalClusterOut"] = t.struct(
        {
            "osEnvironmentConfig": t.proxy(
                renames["BareMetalOsEnvironmentConfigOut"]
            ).optional(),
            "bareMetalVersion": t.string(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "maintenanceStatus": t.proxy(
                renames["BareMetalMaintenanceStatusOut"]
            ).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "maintenanceConfig": t.proxy(
                renames["BareMetalMaintenanceConfigOut"]
            ).optional(),
            "endpoint": t.string().optional(),
            "uid": t.string().optional(),
            "storage": t.proxy(renames["BareMetalStorageConfigOut"]),
            "state": t.string().optional(),
            "deleteTime": t.string().optional(),
            "proxy": t.proxy(renames["BareMetalProxyConfigOut"]).optional(),
            "loadBalancer": t.proxy(renames["BareMetalLoadBalancerConfigOut"]),
            "etag": t.string().optional(),
            "description": t.string().optional(),
            "adminClusterName": t.string().optional(),
            "nodeAccessConfig": t.proxy(
                renames["BareMetalNodeAccessConfigOut"]
            ).optional(),
            "controlPlane": t.proxy(renames["BareMetalControlPlaneConfigOut"]),
            "networkConfig": t.proxy(renames["BareMetalNetworkConfigOut"]),
            "localName": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "nodeConfig": t.proxy(renames["BareMetalWorkloadNodeConfigOut"]).optional(),
            "securityConfig": t.proxy(renames["BareMetalSecurityConfigOut"]).optional(),
            "adminClusterMembership": t.string(),
            "validationCheck": t.proxy(renames["ValidationCheckOut"]).optional(),
            "fleet": t.proxy(renames["FleetOut"]).optional(),
            "clusterOperations": t.proxy(
                renames["BareMetalClusterOperationsConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalClusterOut"])
    types["AuthorizationIn"] = t.struct(
        {"adminUsers": t.array(t.proxy(renames["ClusterUserIn"]))}
    ).named(renames["AuthorizationIn"])
    types["AuthorizationOut"] = t.struct(
        {
            "adminUsers": t.array(t.proxy(renames["ClusterUserOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizationOut"])
    types["BareMetalAdminPortConfigIn"] = t.struct(
        {"controlPlaneLoadBalancerPort": t.integer().optional()}
    ).named(renames["BareMetalAdminPortConfigIn"])
    types["BareMetalAdminPortConfigOut"] = t.struct(
        {
            "controlPlaneLoadBalancerPort": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminPortConfigOut"])
    types["VmwareIpBlockIn"] = t.struct(
        {
            "netmask": t.string().optional(),
            "gateway": t.string().optional(),
            "ips": t.array(t.proxy(renames["VmwareHostIpIn"])).optional(),
        }
    ).named(renames["VmwareIpBlockIn"])
    types["VmwareIpBlockOut"] = t.struct(
        {
            "netmask": t.string().optional(),
            "gateway": t.string().optional(),
            "ips": t.array(t.proxy(renames["VmwareHostIpOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareIpBlockOut"])
    types["VmwareControlPlaneV2ConfigIn"] = t.struct(
        {"controlPlaneIpBlock": t.proxy(renames["VmwareIpBlockIn"]).optional()}
    ).named(renames["VmwareControlPlaneV2ConfigIn"])
    types["VmwareControlPlaneV2ConfigOut"] = t.struct(
        {
            "controlPlaneIpBlock": t.proxy(renames["VmwareIpBlockOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareControlPlaneV2ConfigOut"])
    types["VmwareVCenterConfigIn"] = t.struct(
        {
            "caCertData": t.string().optional(),
            "resourcePool": t.string().optional(),
            "folder": t.string().optional(),
            "storagePolicyName": t.string().optional(),
            "address": t.string().optional(),
            "datastore": t.string().optional(),
            "cluster": t.string().optional(),
            "datacenter": t.string().optional(),
        }
    ).named(renames["VmwareVCenterConfigIn"])
    types["VmwareVCenterConfigOut"] = t.struct(
        {
            "caCertData": t.string().optional(),
            "resourcePool": t.string().optional(),
            "folder": t.string().optional(),
            "storagePolicyName": t.string().optional(),
            "address": t.string().optional(),
            "datastore": t.string().optional(),
            "cluster": t.string().optional(),
            "datacenter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareVCenterConfigOut"])
    types["VmwareControlPlaneNodeConfigIn"] = t.struct(
        {
            "autoResizeConfig": t.proxy(renames["VmwareAutoResizeConfigIn"]).optional(),
            "memory": t.string().optional(),
            "replicas": t.string().optional(),
            "cpus": t.string().optional(),
        }
    ).named(renames["VmwareControlPlaneNodeConfigIn"])
    types["VmwareControlPlaneNodeConfigOut"] = t.struct(
        {
            "autoResizeConfig": t.proxy(
                renames["VmwareAutoResizeConfigOut"]
            ).optional(),
            "memory": t.string().optional(),
            "vsphereConfig": t.proxy(
                renames["VmwareControlPlaneVsphereConfigOut"]
            ).optional(),
            "replicas": t.string().optional(),
            "cpus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareControlPlaneNodeConfigOut"])
    types["BareMetalManualLbConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["BareMetalManualLbConfigIn"])
    types["BareMetalManualLbConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalManualLbConfigOut"])
    types["BareMetalAdminClusterIn"] = t.struct(
        {
            "proxy": t.proxy(renames["BareMetalAdminProxyConfigIn"]).optional(),
            "loadBalancer": t.proxy(
                renames["BareMetalAdminLoadBalancerConfigIn"]
            ).optional(),
            "networkConfig": t.proxy(
                renames["BareMetalAdminNetworkConfigIn"]
            ).optional(),
            "maintenanceConfig": t.proxy(
                renames["BareMetalAdminMaintenanceConfigIn"]
            ).optional(),
            "nodeConfig": t.proxy(
                renames["BareMetalAdminWorkloadNodeConfigIn"]
            ).optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "storage": t.proxy(renames["BareMetalAdminStorageConfigIn"]).optional(),
            "nodeAccessConfig": t.proxy(
                renames["BareMetalAdminNodeAccessConfigIn"]
            ).optional(),
            "description": t.string().optional(),
            "osEnvironmentConfig": t.proxy(
                renames["BareMetalAdminOsEnvironmentConfigIn"]
            ).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "securityConfig": t.proxy(
                renames["BareMetalAdminSecurityConfigIn"]
            ).optional(),
            "clusterOperations": t.proxy(
                renames["BareMetalAdminClusterOperationsConfigIn"]
            ).optional(),
            "bareMetalVersion": t.string().optional(),
            "controlPlane": t.proxy(
                renames["BareMetalAdminControlPlaneConfigIn"]
            ).optional(),
        }
    ).named(renames["BareMetalAdminClusterIn"])
    types["BareMetalAdminClusterOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "proxy": t.proxy(renames["BareMetalAdminProxyConfigOut"]).optional(),
            "loadBalancer": t.proxy(
                renames["BareMetalAdminLoadBalancerConfigOut"]
            ).optional(),
            "networkConfig": t.proxy(
                renames["BareMetalAdminNetworkConfigOut"]
            ).optional(),
            "maintenanceConfig": t.proxy(
                renames["BareMetalAdminMaintenanceConfigOut"]
            ).optional(),
            "nodeConfig": t.proxy(
                renames["BareMetalAdminWorkloadNodeConfigOut"]
            ).optional(),
            "etag": t.string().optional(),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "uid": t.string().optional(),
            "maintenanceStatus": t.proxy(
                renames["BareMetalAdminMaintenanceStatusOut"]
            ).optional(),
            "name": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "storage": t.proxy(renames["BareMetalAdminStorageConfigOut"]).optional(),
            "fleet": t.proxy(renames["FleetOut"]).optional(),
            "deleteTime": t.string().optional(),
            "validationCheck": t.proxy(renames["ValidationCheckOut"]).optional(),
            "nodeAccessConfig": t.proxy(
                renames["BareMetalAdminNodeAccessConfigOut"]
            ).optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "localName": t.string().optional(),
            "osEnvironmentConfig": t.proxy(
                renames["BareMetalAdminOsEnvironmentConfigOut"]
            ).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "endpoint": t.string().optional(),
            "securityConfig": t.proxy(
                renames["BareMetalAdminSecurityConfigOut"]
            ).optional(),
            "clusterOperations": t.proxy(
                renames["BareMetalAdminClusterOperationsConfigOut"]
            ).optional(),
            "bareMetalVersion": t.string().optional(),
            "controlPlane": t.proxy(
                renames["BareMetalAdminControlPlaneConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminClusterOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["BareMetalAdminClusterOperationsConfigIn"] = t.struct(
        {"enableApplicationLogs": t.boolean().optional()}
    ).named(renames["BareMetalAdminClusterOperationsConfigIn"])
    types["BareMetalAdminClusterOperationsConfigOut"] = t.struct(
        {
            "enableApplicationLogs": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminClusterOperationsConfigOut"])
    types["VmwareAdminClusterIn"] = t.struct(
        {
            "vcenter": t.proxy(renames["VmwareAdminVCenterConfigIn"]).optional(),
            "autoRepairConfig": t.proxy(renames["VmwareAutoRepairConfigIn"]).optional(),
            "etag": t.string().optional(),
            "onPremVersion": t.string().optional(),
            "platformConfig": t.proxy(renames["VmwarePlatformConfigIn"]).optional(),
            "loadBalancer": t.proxy(
                renames["VmwareAdminLoadBalancerConfigIn"]
            ).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "imageType": t.string().optional(),
            "bootstrapClusterMembership": t.string().optional(),
            "addonNode": t.proxy(renames["VmwareAdminAddonNodeConfigIn"]).optional(),
            "name": t.string().optional(),
            "networkConfig": t.proxy(renames["VmwareAdminNetworkConfigIn"]).optional(),
            "controlPlaneNode": t.proxy(
                renames["VmwareAdminControlPlaneNodeConfigIn"]
            ).optional(),
            "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["VmwareAdminClusterIn"])
    types["VmwareAdminClusterOut"] = t.struct(
        {
            "endpoint": t.string().optional(),
            "fleet": t.proxy(renames["FleetOut"]).optional(),
            "vcenter": t.proxy(renames["VmwareAdminVCenterConfigOut"]).optional(),
            "autoRepairConfig": t.proxy(
                renames["VmwareAutoRepairConfigOut"]
            ).optional(),
            "etag": t.string().optional(),
            "onPremVersion": t.string().optional(),
            "platformConfig": t.proxy(renames["VmwarePlatformConfigOut"]).optional(),
            "loadBalancer": t.proxy(
                renames["VmwareAdminLoadBalancerConfigOut"]
            ).optional(),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "imageType": t.string().optional(),
            "bootstrapClusterMembership": t.string().optional(),
            "addonNode": t.proxy(renames["VmwareAdminAddonNodeConfigOut"]).optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "localName": t.string().optional(),
            "uid": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "name": t.string().optional(),
            "networkConfig": t.proxy(renames["VmwareAdminNetworkConfigOut"]).optional(),
            "controlPlaneNode": t.proxy(
                renames["VmwareAdminControlPlaneNodeConfigOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigOut"]).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAdminClusterOut"])
    types["VmwareNodePoolAutoscalingConfigIn"] = t.struct(
        {"minReplicas": t.integer().optional(), "maxReplicas": t.integer().optional()}
    ).named(renames["VmwareNodePoolAutoscalingConfigIn"])
    types["VmwareNodePoolAutoscalingConfigOut"] = t.struct(
        {
            "minReplicas": t.integer().optional(),
            "maxReplicas": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareNodePoolAutoscalingConfigOut"])
    types["BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["BareMetalParallelUpgradeConfigIn"] = t.struct(
        {
            "minimumAvailableNodes": t.integer().optional(),
            "concurrentNodes": t.integer(),
        }
    ).named(renames["BareMetalParallelUpgradeConfigIn"])
    types["BareMetalParallelUpgradeConfigOut"] = t.struct(
        {
            "minimumAvailableNodes": t.integer().optional(),
            "concurrentNodes": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalParallelUpgradeConfigOut"])
    types["VmwareAutoRepairConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["VmwareAutoRepairConfigIn"])
    types["VmwareAutoRepairConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAutoRepairConfigOut"])
    types["VmwarePlatformConfigIn"] = t.struct(
        {"requiredPlatformVersion": t.string().optional()}
    ).named(renames["VmwarePlatformConfigIn"])
    types["VmwarePlatformConfigOut"] = t.struct(
        {
            "platformVersion": t.string().optional(),
            "requiredPlatformVersion": t.string().optional(),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "bundles": t.array(t.proxy(renames["VmwareBundleConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwarePlatformConfigOut"])
    types["VmwareVsphereConfigIn"] = t.struct(
        {
            "storagePolicyName": t.string().optional(),
            "tags": t.array(t.proxy(renames["VmwareVsphereTagIn"])).optional(),
            "datastore": t.string().optional(),
        }
    ).named(renames["VmwareVsphereConfigIn"])
    types["VmwareVsphereConfigOut"] = t.struct(
        {
            "storagePolicyName": t.string().optional(),
            "tags": t.array(t.proxy(renames["VmwareVsphereTagOut"])).optional(),
            "datastore": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareVsphereConfigOut"])
    types["VmwareVipConfigIn"] = t.struct(
        {"controlPlaneVip": t.string().optional(), "ingressVip": t.string().optional()}
    ).named(renames["VmwareVipConfigIn"])
    types["VmwareVipConfigOut"] = t.struct(
        {
            "controlPlaneVip": t.string().optional(),
            "ingressVip": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareVipConfigOut"])
    types["ValidationCheckResultIn"] = t.struct(
        {
            "description": t.string().optional(),
            "category": t.string().optional(),
            "reason": t.string().optional(),
            "state": t.string().optional(),
            "details": t.string().optional(),
        }
    ).named(renames["ValidationCheckResultIn"])
    types["ValidationCheckResultOut"] = t.struct(
        {
            "description": t.string().optional(),
            "category": t.string().optional(),
            "reason": t.string().optional(),
            "state": t.string().optional(),
            "details": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationCheckResultOut"])
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
    types["ListVmwareClustersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "vmwareClusters": t.array(t.proxy(renames["VmwareClusterIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListVmwareClustersResponseIn"])
    types["ListVmwareClustersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "vmwareClusters": t.array(t.proxy(renames["VmwareClusterOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVmwareClustersResponseOut"])
    types["BareMetalAdminOsEnvironmentConfigIn"] = t.struct(
        {"packageRepoExcluded": t.boolean().optional()}
    ).named(renames["BareMetalAdminOsEnvironmentConfigIn"])
    types["BareMetalAdminOsEnvironmentConfigOut"] = t.struct(
        {
            "packageRepoExcluded": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminOsEnvironmentConfigOut"])
    types["BareMetalMultipleNetworkInterfacesConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["BareMetalMultipleNetworkInterfacesConfigIn"])
    types["BareMetalMultipleNetworkInterfacesConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalMultipleNetworkInterfacesConfigOut"])
    types["BareMetalOsEnvironmentConfigIn"] = t.struct(
        {"packageRepoExcluded": t.boolean().optional()}
    ).named(renames["BareMetalOsEnvironmentConfigIn"])
    types["BareMetalOsEnvironmentConfigOut"] = t.struct(
        {
            "packageRepoExcluded": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalOsEnvironmentConfigOut"])
    types["BareMetalLvpConfigIn"] = t.struct(
        {"storageClass": t.string(), "path": t.string()}
    ).named(renames["BareMetalLvpConfigIn"])
    types["BareMetalLvpConfigOut"] = t.struct(
        {
            "storageClass": t.string(),
            "path": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalLvpConfigOut"])
    types["BareMetalLvpShareConfigIn"] = t.struct(
        {
            "sharedPathPvCount": t.integer().optional(),
            "lvpConfig": t.proxy(renames["BareMetalLvpConfigIn"]),
        }
    ).named(renames["BareMetalLvpShareConfigIn"])
    types["BareMetalLvpShareConfigOut"] = t.struct(
        {
            "sharedPathPvCount": t.integer().optional(),
            "lvpConfig": t.proxy(renames["BareMetalLvpConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalLvpShareConfigOut"])
    types["BareMetalNodePoolIn"] = t.struct(
        {
            "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigIn"]),
            "upgradePolicy": t.proxy(
                renames["BareMetalNodePoolUpgradePolicyIn"]
            ).optional(),
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["BareMetalNodePoolIn"])
    types["BareMetalNodePoolOut"] = t.struct(
        {
            "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigOut"]),
            "upgradePolicy": t.proxy(
                renames["BareMetalNodePoolUpgradePolicyOut"]
            ).optional(),
            "uid": t.string().optional(),
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "deleteTime": t.string().optional(),
            "state": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "etag": t.string().optional(),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalNodePoolOut"])
    types["BareMetalControlPlaneConfigIn"] = t.struct(
        {
            "controlPlaneNodePoolConfig": t.proxy(
                renames["BareMetalControlPlaneNodePoolConfigIn"]
            ),
            "apiServerArgs": t.array(
                t.proxy(renames["BareMetalApiServerArgumentIn"])
            ).optional(),
        }
    ).named(renames["BareMetalControlPlaneConfigIn"])
    types["BareMetalControlPlaneConfigOut"] = t.struct(
        {
            "controlPlaneNodePoolConfig": t.proxy(
                renames["BareMetalControlPlaneNodePoolConfigOut"]
            ),
            "apiServerArgs": t.array(
                t.proxy(renames["BareMetalApiServerArgumentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalControlPlaneConfigOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "statusMessage": t.string().optional(),
            "controlPlaneDisconnected": t.boolean().optional(),
            "type": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["VmwareDhcpIpConfigIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["VmwareDhcpIpConfigIn"]
    )
    types["VmwareDhcpIpConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareDhcpIpConfigOut"])
    types["OperationStageIn"] = t.struct(
        {
            "stage": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
        }
    ).named(renames["OperationStageIn"])
    types["OperationStageOut"] = t.struct(
        {
            "stage": t.string().optional(),
            "state": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationStageOut"])
    types["MetricIn"] = t.struct(
        {
            "metric": t.string(),
            "doubleValue": t.number().optional(),
            "stringValue": t.string().optional(),
            "intValue": t.string().optional(),
        }
    ).named(renames["MetricIn"])
    types["MetricOut"] = t.struct(
        {
            "metric": t.string(),
            "doubleValue": t.number().optional(),
            "stringValue": t.string().optional(),
            "intValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricOut"])
    types["EnrollBareMetalClusterRequestIn"] = t.struct(
        {
            "localName": t.string().optional(),
            "adminClusterMembership": t.string(),
            "bareMetalClusterId": t.string().optional(),
        }
    ).named(renames["EnrollBareMetalClusterRequestIn"])
    types["EnrollBareMetalClusterRequestOut"] = t.struct(
        {
            "localName": t.string().optional(),
            "adminClusterMembership": t.string(),
            "bareMetalClusterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollBareMetalClusterRequestOut"])
    types["BareMetalStorageConfigIn"] = t.struct(
        {
            "lvpNodeMountsConfig": t.proxy(renames["BareMetalLvpConfigIn"]),
            "lvpShareConfig": t.proxy(renames["BareMetalLvpShareConfigIn"]),
        }
    ).named(renames["BareMetalStorageConfigIn"])
    types["BareMetalStorageConfigOut"] = t.struct(
        {
            "lvpNodeMountsConfig": t.proxy(renames["BareMetalLvpConfigOut"]),
            "lvpShareConfig": t.proxy(renames["BareMetalLvpShareConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalStorageConfigOut"])
    types["BareMetalClusterOperationsConfigIn"] = t.struct(
        {"enableApplicationLogs": t.boolean().optional()}
    ).named(renames["BareMetalClusterOperationsConfigIn"])
    types["BareMetalClusterOperationsConfigOut"] = t.struct(
        {
            "enableApplicationLogs": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalClusterOperationsConfigOut"])
    types["VmwareLoadBalancerConfigIn"] = t.struct(
        {
            "vipConfig": t.proxy(renames["VmwareVipConfigIn"]).optional(),
            "f5Config": t.proxy(renames["VmwareF5BigIpConfigIn"]).optional(),
            "metalLbConfig": t.proxy(renames["VmwareMetalLbConfigIn"]).optional(),
            "manualLbConfig": t.proxy(renames["VmwareManualLbConfigIn"]).optional(),
        }
    ).named(renames["VmwareLoadBalancerConfigIn"])
    types["VmwareLoadBalancerConfigOut"] = t.struct(
        {
            "vipConfig": t.proxy(renames["VmwareVipConfigOut"]).optional(),
            "f5Config": t.proxy(renames["VmwareF5BigIpConfigOut"]).optional(),
            "metalLbConfig": t.proxy(renames["VmwareMetalLbConfigOut"]).optional(),
            "manualLbConfig": t.proxy(renames["VmwareManualLbConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareLoadBalancerConfigOut"])
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
    types["QueryBareMetalVersionConfigResponseIn"] = t.struct(
        {"versions": t.array(t.proxy(renames["BareMetalVersionInfoIn"])).optional()}
    ).named(renames["QueryBareMetalVersionConfigResponseIn"])
    types["QueryBareMetalVersionConfigResponseOut"] = t.struct(
        {
            "versions": t.array(t.proxy(renames["BareMetalVersionInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryBareMetalVersionConfigResponseOut"])
    types["ListBareMetalAdminClustersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "bareMetalAdminClusters": t.array(
                t.proxy(renames["BareMetalAdminClusterIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListBareMetalAdminClustersResponseIn"])
    types["ListBareMetalAdminClustersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "bareMetalAdminClusters": t.array(
                t.proxy(renames["BareMetalAdminClusterOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBareMetalAdminClustersResponseOut"])
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
    types["BareMetalAdminIslandModeCidrConfigIn"] = t.struct(
        {
            "podAddressCidrBlocks": t.array(t.string()),
            "serviceAddressCidrBlocks": t.array(t.string()),
        }
    ).named(renames["BareMetalAdminIslandModeCidrConfigIn"])
    types["BareMetalAdminIslandModeCidrConfigOut"] = t.struct(
        {
            "podAddressCidrBlocks": t.array(t.string()),
            "serviceAddressCidrBlocks": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminIslandModeCidrConfigOut"])
    types["VmwareAutoResizeConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["VmwareAutoResizeConfigIn"])
    types["VmwareAutoResizeConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAutoResizeConfigOut"])
    types["VmwareMetalLbConfigIn"] = t.struct(
        {"addressPools": t.array(t.proxy(renames["VmwareAddressPoolIn"]))}
    ).named(renames["VmwareMetalLbConfigIn"])
    types["VmwareMetalLbConfigOut"] = t.struct(
        {
            "addressPools": t.array(t.proxy(renames["VmwareAddressPoolOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareMetalLbConfigOut"])
    types["BareMetalAdminApiServerArgumentIn"] = t.struct(
        {"argument": t.string(), "value": t.string()}
    ).named(renames["BareMetalAdminApiServerArgumentIn"])
    types["BareMetalAdminApiServerArgumentOut"] = t.struct(
        {
            "argument": t.string(),
            "value": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminApiServerArgumentOut"])
    types["OperationProgressIn"] = t.struct(
        {"stages": t.array(t.proxy(renames["OperationStageIn"])).optional()}
    ).named(renames["OperationProgressIn"])
    types["OperationProgressOut"] = t.struct(
        {
            "stages": t.array(t.proxy(renames["OperationStageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationProgressOut"])
    types["VmwareVersionInfoIn"] = t.struct(
        {
            "hasDependencies": t.boolean().optional(),
            "isInstalled": t.boolean().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["VmwareVersionInfoIn"])
    types["VmwareVersionInfoOut"] = t.struct(
        {
            "hasDependencies": t.boolean().optional(),
            "isInstalled": t.boolean().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareVersionInfoOut"])

    functions = {}
    functions["projectsLocationsGet"] = gkeonprem.get(
        "v1/{name}/locations",
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
    functions["projectsLocationsList"] = gkeonprem.get(
        "v1/{name}/locations",
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
    functions["projectsLocationsOperationsDelete"] = gkeonprem.post(
        "v1/{name}:cancel",
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
    functions["projectsLocationsOperationsGet"] = gkeonprem.post(
        "v1/{name}:cancel",
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
    functions["projectsLocationsOperationsList"] = gkeonprem.post(
        "v1/{name}:cancel",
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
    functions["projectsLocationsOperationsCancel"] = gkeonprem.post(
        "v1/{name}:cancel",
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
    functions["projectsLocationsVmwareAdminClustersList"] = gkeonprem.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareAdminClustersUnenroll"] = gkeonprem.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareAdminClustersPatch"] = gkeonprem.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareAdminClustersGet"] = gkeonprem.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareAdminClustersSetIamPolicy"] = gkeonprem.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareAdminClustersGetIamPolicy"] = gkeonprem.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareAdminClustersEnroll"] = gkeonprem.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsVmwareAdminClustersTestIamPermissions"
    ] = gkeonprem.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareAdminClustersOperationsList"] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareAdminClustersOperationsGet"] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalAdminClustersTestIamPermissions"
    ] = gkeonprem.post(
        "v1/{parent}/bareMetalAdminClusters",
        t.struct(
            {
                "bareMetalAdminClusterId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "proxy": t.proxy(renames["BareMetalAdminProxyConfigIn"]).optional(),
                "loadBalancer": t.proxy(
                    renames["BareMetalAdminLoadBalancerConfigIn"]
                ).optional(),
                "networkConfig": t.proxy(
                    renames["BareMetalAdminNetworkConfigIn"]
                ).optional(),
                "maintenanceConfig": t.proxy(
                    renames["BareMetalAdminMaintenanceConfigIn"]
                ).optional(),
                "nodeConfig": t.proxy(
                    renames["BareMetalAdminWorkloadNodeConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "storage": t.proxy(renames["BareMetalAdminStorageConfigIn"]).optional(),
                "nodeAccessConfig": t.proxy(
                    renames["BareMetalAdminNodeAccessConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "osEnvironmentConfig": t.proxy(
                    renames["BareMetalAdminOsEnvironmentConfigIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "securityConfig": t.proxy(
                    renames["BareMetalAdminSecurityConfigIn"]
                ).optional(),
                "clusterOperations": t.proxy(
                    renames["BareMetalAdminClusterOperationsConfigIn"]
                ).optional(),
                "bareMetalVersion": t.string().optional(),
                "controlPlane": t.proxy(
                    renames["BareMetalAdminControlPlaneConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalAdminClustersGet"] = gkeonprem.post(
        "v1/{parent}/bareMetalAdminClusters",
        t.struct(
            {
                "bareMetalAdminClusterId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "proxy": t.proxy(renames["BareMetalAdminProxyConfigIn"]).optional(),
                "loadBalancer": t.proxy(
                    renames["BareMetalAdminLoadBalancerConfigIn"]
                ).optional(),
                "networkConfig": t.proxy(
                    renames["BareMetalAdminNetworkConfigIn"]
                ).optional(),
                "maintenanceConfig": t.proxy(
                    renames["BareMetalAdminMaintenanceConfigIn"]
                ).optional(),
                "nodeConfig": t.proxy(
                    renames["BareMetalAdminWorkloadNodeConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "storage": t.proxy(renames["BareMetalAdminStorageConfigIn"]).optional(),
                "nodeAccessConfig": t.proxy(
                    renames["BareMetalAdminNodeAccessConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "osEnvironmentConfig": t.proxy(
                    renames["BareMetalAdminOsEnvironmentConfigIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "securityConfig": t.proxy(
                    renames["BareMetalAdminSecurityConfigIn"]
                ).optional(),
                "clusterOperations": t.proxy(
                    renames["BareMetalAdminClusterOperationsConfigIn"]
                ).optional(),
                "bareMetalVersion": t.string().optional(),
                "controlPlane": t.proxy(
                    renames["BareMetalAdminControlPlaneConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalAdminClustersQueryVersionConfig"
    ] = gkeonprem.post(
        "v1/{parent}/bareMetalAdminClusters",
        t.struct(
            {
                "bareMetalAdminClusterId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "proxy": t.proxy(renames["BareMetalAdminProxyConfigIn"]).optional(),
                "loadBalancer": t.proxy(
                    renames["BareMetalAdminLoadBalancerConfigIn"]
                ).optional(),
                "networkConfig": t.proxy(
                    renames["BareMetalAdminNetworkConfigIn"]
                ).optional(),
                "maintenanceConfig": t.proxy(
                    renames["BareMetalAdminMaintenanceConfigIn"]
                ).optional(),
                "nodeConfig": t.proxy(
                    renames["BareMetalAdminWorkloadNodeConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "storage": t.proxy(renames["BareMetalAdminStorageConfigIn"]).optional(),
                "nodeAccessConfig": t.proxy(
                    renames["BareMetalAdminNodeAccessConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "osEnvironmentConfig": t.proxy(
                    renames["BareMetalAdminOsEnvironmentConfigIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "securityConfig": t.proxy(
                    renames["BareMetalAdminSecurityConfigIn"]
                ).optional(),
                "clusterOperations": t.proxy(
                    renames["BareMetalAdminClusterOperationsConfigIn"]
                ).optional(),
                "bareMetalVersion": t.string().optional(),
                "controlPlane": t.proxy(
                    renames["BareMetalAdminControlPlaneConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalAdminClustersList"] = gkeonprem.post(
        "v1/{parent}/bareMetalAdminClusters",
        t.struct(
            {
                "bareMetalAdminClusterId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "proxy": t.proxy(renames["BareMetalAdminProxyConfigIn"]).optional(),
                "loadBalancer": t.proxy(
                    renames["BareMetalAdminLoadBalancerConfigIn"]
                ).optional(),
                "networkConfig": t.proxy(
                    renames["BareMetalAdminNetworkConfigIn"]
                ).optional(),
                "maintenanceConfig": t.proxy(
                    renames["BareMetalAdminMaintenanceConfigIn"]
                ).optional(),
                "nodeConfig": t.proxy(
                    renames["BareMetalAdminWorkloadNodeConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "storage": t.proxy(renames["BareMetalAdminStorageConfigIn"]).optional(),
                "nodeAccessConfig": t.proxy(
                    renames["BareMetalAdminNodeAccessConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "osEnvironmentConfig": t.proxy(
                    renames["BareMetalAdminOsEnvironmentConfigIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "securityConfig": t.proxy(
                    renames["BareMetalAdminSecurityConfigIn"]
                ).optional(),
                "clusterOperations": t.proxy(
                    renames["BareMetalAdminClusterOperationsConfigIn"]
                ).optional(),
                "bareMetalVersion": t.string().optional(),
                "controlPlane": t.proxy(
                    renames["BareMetalAdminControlPlaneConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalAdminClustersPatch"] = gkeonprem.post(
        "v1/{parent}/bareMetalAdminClusters",
        t.struct(
            {
                "bareMetalAdminClusterId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "proxy": t.proxy(renames["BareMetalAdminProxyConfigIn"]).optional(),
                "loadBalancer": t.proxy(
                    renames["BareMetalAdminLoadBalancerConfigIn"]
                ).optional(),
                "networkConfig": t.proxy(
                    renames["BareMetalAdminNetworkConfigIn"]
                ).optional(),
                "maintenanceConfig": t.proxy(
                    renames["BareMetalAdminMaintenanceConfigIn"]
                ).optional(),
                "nodeConfig": t.proxy(
                    renames["BareMetalAdminWorkloadNodeConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "storage": t.proxy(renames["BareMetalAdminStorageConfigIn"]).optional(),
                "nodeAccessConfig": t.proxy(
                    renames["BareMetalAdminNodeAccessConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "osEnvironmentConfig": t.proxy(
                    renames["BareMetalAdminOsEnvironmentConfigIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "securityConfig": t.proxy(
                    renames["BareMetalAdminSecurityConfigIn"]
                ).optional(),
                "clusterOperations": t.proxy(
                    renames["BareMetalAdminClusterOperationsConfigIn"]
                ).optional(),
                "bareMetalVersion": t.string().optional(),
                "controlPlane": t.proxy(
                    renames["BareMetalAdminControlPlaneConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalAdminClustersSetIamPolicy"] = gkeonprem.post(
        "v1/{parent}/bareMetalAdminClusters",
        t.struct(
            {
                "bareMetalAdminClusterId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "proxy": t.proxy(renames["BareMetalAdminProxyConfigIn"]).optional(),
                "loadBalancer": t.proxy(
                    renames["BareMetalAdminLoadBalancerConfigIn"]
                ).optional(),
                "networkConfig": t.proxy(
                    renames["BareMetalAdminNetworkConfigIn"]
                ).optional(),
                "maintenanceConfig": t.proxy(
                    renames["BareMetalAdminMaintenanceConfigIn"]
                ).optional(),
                "nodeConfig": t.proxy(
                    renames["BareMetalAdminWorkloadNodeConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "storage": t.proxy(renames["BareMetalAdminStorageConfigIn"]).optional(),
                "nodeAccessConfig": t.proxy(
                    renames["BareMetalAdminNodeAccessConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "osEnvironmentConfig": t.proxy(
                    renames["BareMetalAdminOsEnvironmentConfigIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "securityConfig": t.proxy(
                    renames["BareMetalAdminSecurityConfigIn"]
                ).optional(),
                "clusterOperations": t.proxy(
                    renames["BareMetalAdminClusterOperationsConfigIn"]
                ).optional(),
                "bareMetalVersion": t.string().optional(),
                "controlPlane": t.proxy(
                    renames["BareMetalAdminControlPlaneConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalAdminClustersGetIamPolicy"] = gkeonprem.post(
        "v1/{parent}/bareMetalAdminClusters",
        t.struct(
            {
                "bareMetalAdminClusterId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "proxy": t.proxy(renames["BareMetalAdminProxyConfigIn"]).optional(),
                "loadBalancer": t.proxy(
                    renames["BareMetalAdminLoadBalancerConfigIn"]
                ).optional(),
                "networkConfig": t.proxy(
                    renames["BareMetalAdminNetworkConfigIn"]
                ).optional(),
                "maintenanceConfig": t.proxy(
                    renames["BareMetalAdminMaintenanceConfigIn"]
                ).optional(),
                "nodeConfig": t.proxy(
                    renames["BareMetalAdminWorkloadNodeConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "storage": t.proxy(renames["BareMetalAdminStorageConfigIn"]).optional(),
                "nodeAccessConfig": t.proxy(
                    renames["BareMetalAdminNodeAccessConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "osEnvironmentConfig": t.proxy(
                    renames["BareMetalAdminOsEnvironmentConfigIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "securityConfig": t.proxy(
                    renames["BareMetalAdminSecurityConfigIn"]
                ).optional(),
                "clusterOperations": t.proxy(
                    renames["BareMetalAdminClusterOperationsConfigIn"]
                ).optional(),
                "bareMetalVersion": t.string().optional(),
                "controlPlane": t.proxy(
                    renames["BareMetalAdminControlPlaneConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalAdminClustersUnenroll"] = gkeonprem.post(
        "v1/{parent}/bareMetalAdminClusters",
        t.struct(
            {
                "bareMetalAdminClusterId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "proxy": t.proxy(renames["BareMetalAdminProxyConfigIn"]).optional(),
                "loadBalancer": t.proxy(
                    renames["BareMetalAdminLoadBalancerConfigIn"]
                ).optional(),
                "networkConfig": t.proxy(
                    renames["BareMetalAdminNetworkConfigIn"]
                ).optional(),
                "maintenanceConfig": t.proxy(
                    renames["BareMetalAdminMaintenanceConfigIn"]
                ).optional(),
                "nodeConfig": t.proxy(
                    renames["BareMetalAdminWorkloadNodeConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "storage": t.proxy(renames["BareMetalAdminStorageConfigIn"]).optional(),
                "nodeAccessConfig": t.proxy(
                    renames["BareMetalAdminNodeAccessConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "osEnvironmentConfig": t.proxy(
                    renames["BareMetalAdminOsEnvironmentConfigIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "securityConfig": t.proxy(
                    renames["BareMetalAdminSecurityConfigIn"]
                ).optional(),
                "clusterOperations": t.proxy(
                    renames["BareMetalAdminClusterOperationsConfigIn"]
                ).optional(),
                "bareMetalVersion": t.string().optional(),
                "controlPlane": t.proxy(
                    renames["BareMetalAdminControlPlaneConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalAdminClustersEnroll"] = gkeonprem.post(
        "v1/{parent}/bareMetalAdminClusters",
        t.struct(
            {
                "bareMetalAdminClusterId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "proxy": t.proxy(renames["BareMetalAdminProxyConfigIn"]).optional(),
                "loadBalancer": t.proxy(
                    renames["BareMetalAdminLoadBalancerConfigIn"]
                ).optional(),
                "networkConfig": t.proxy(
                    renames["BareMetalAdminNetworkConfigIn"]
                ).optional(),
                "maintenanceConfig": t.proxy(
                    renames["BareMetalAdminMaintenanceConfigIn"]
                ).optional(),
                "nodeConfig": t.proxy(
                    renames["BareMetalAdminWorkloadNodeConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "storage": t.proxy(renames["BareMetalAdminStorageConfigIn"]).optional(),
                "nodeAccessConfig": t.proxy(
                    renames["BareMetalAdminNodeAccessConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "osEnvironmentConfig": t.proxy(
                    renames["BareMetalAdminOsEnvironmentConfigIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "securityConfig": t.proxy(
                    renames["BareMetalAdminSecurityConfigIn"]
                ).optional(),
                "clusterOperations": t.proxy(
                    renames["BareMetalAdminClusterOperationsConfigIn"]
                ).optional(),
                "bareMetalVersion": t.string().optional(),
                "controlPlane": t.proxy(
                    renames["BareMetalAdminControlPlaneConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalAdminClustersCreate"] = gkeonprem.post(
        "v1/{parent}/bareMetalAdminClusters",
        t.struct(
            {
                "bareMetalAdminClusterId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "proxy": t.proxy(renames["BareMetalAdminProxyConfigIn"]).optional(),
                "loadBalancer": t.proxy(
                    renames["BareMetalAdminLoadBalancerConfigIn"]
                ).optional(),
                "networkConfig": t.proxy(
                    renames["BareMetalAdminNetworkConfigIn"]
                ).optional(),
                "maintenanceConfig": t.proxy(
                    renames["BareMetalAdminMaintenanceConfigIn"]
                ).optional(),
                "nodeConfig": t.proxy(
                    renames["BareMetalAdminWorkloadNodeConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "storage": t.proxy(renames["BareMetalAdminStorageConfigIn"]).optional(),
                "nodeAccessConfig": t.proxy(
                    renames["BareMetalAdminNodeAccessConfigIn"]
                ).optional(),
                "description": t.string().optional(),
                "osEnvironmentConfig": t.proxy(
                    renames["BareMetalAdminOsEnvironmentConfigIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "securityConfig": t.proxy(
                    renames["BareMetalAdminSecurityConfigIn"]
                ).optional(),
                "clusterOperations": t.proxy(
                    renames["BareMetalAdminClusterOperationsConfigIn"]
                ).optional(),
                "bareMetalVersion": t.string().optional(),
                "controlPlane": t.proxy(
                    renames["BareMetalAdminControlPlaneConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalAdminClustersOperationsGet"] = gkeonprem.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalAdminClustersOperationsList"] = gkeonprem.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersTestIamPermissions"
    ] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "etag": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "force": t.boolean().optional(),
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersQueryVersionConfig"
    ] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "etag": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "force": t.boolean().optional(),
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersGetIamPolicy"] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "etag": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "force": t.boolean().optional(),
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersList"] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "etag": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "force": t.boolean().optional(),
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersGet"] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "etag": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "force": t.boolean().optional(),
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersEnroll"] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "etag": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "force": t.boolean().optional(),
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersPatch"] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "etag": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "force": t.boolean().optional(),
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersSetIamPolicy"] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "etag": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "force": t.boolean().optional(),
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersDelete"] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "etag": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "force": t.boolean().optional(),
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersCreate"] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "etag": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "force": t.boolean().optional(),
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersUnenroll"] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "etag": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "force": t.boolean().optional(),
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersOperationsGet"] = gkeonprem.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersOperationsList"] = gkeonprem.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsEnroll"
    ] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsDelete"
    ] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsGetIamPolicy"
    ] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsList"
    ] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsCreate"
    ] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsPatch"
    ] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsSetIamPolicy"
    ] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsGet"
    ] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsTestIamPermissions"
    ] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsUnenroll"
    ] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "allowMissing": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsOperationsList"
    ] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsOperationsGet"
    ] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersPatch"] = gkeonprem.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersDelete"] = gkeonprem.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersQueryVersionConfig"] = gkeonprem.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersUnenroll"] = gkeonprem.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersEnroll"] = gkeonprem.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersCreate"] = gkeonprem.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersList"] = gkeonprem.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersGet"] = gkeonprem.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersTestIamPermissions"] = gkeonprem.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersGetIamPolicy"] = gkeonprem.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersSetIamPolicy"] = gkeonprem.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersVmwareNodePoolsList"] = gkeonprem.post(
        "v1/{parent}/vmwareNodePools",
        t.struct(
            {
                "vmwareNodePoolId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "nodePoolAutoscaling": t.proxy(
                    renames["VmwareNodePoolAutoscalingConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "config": t.proxy(renames["VmwareNodeConfigIn"]),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "onPremVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsVmwareClustersVmwareNodePoolsGetIamPolicy"
    ] = gkeonprem.post(
        "v1/{parent}/vmwareNodePools",
        t.struct(
            {
                "vmwareNodePoolId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "nodePoolAutoscaling": t.proxy(
                    renames["VmwareNodePoolAutoscalingConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "config": t.proxy(renames["VmwareNodeConfigIn"]),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "onPremVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersVmwareNodePoolsEnroll"] = gkeonprem.post(
        "v1/{parent}/vmwareNodePools",
        t.struct(
            {
                "vmwareNodePoolId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "nodePoolAutoscaling": t.proxy(
                    renames["VmwareNodePoolAutoscalingConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "config": t.proxy(renames["VmwareNodeConfigIn"]),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "onPremVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsVmwareClustersVmwareNodePoolsUnenroll"
    ] = gkeonprem.post(
        "v1/{parent}/vmwareNodePools",
        t.struct(
            {
                "vmwareNodePoolId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "nodePoolAutoscaling": t.proxy(
                    renames["VmwareNodePoolAutoscalingConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "config": t.proxy(renames["VmwareNodeConfigIn"]),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "onPremVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersVmwareNodePoolsGet"] = gkeonprem.post(
        "v1/{parent}/vmwareNodePools",
        t.struct(
            {
                "vmwareNodePoolId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "nodePoolAutoscaling": t.proxy(
                    renames["VmwareNodePoolAutoscalingConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "config": t.proxy(renames["VmwareNodeConfigIn"]),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "onPremVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsVmwareClustersVmwareNodePoolsTestIamPermissions"
    ] = gkeonprem.post(
        "v1/{parent}/vmwareNodePools",
        t.struct(
            {
                "vmwareNodePoolId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "nodePoolAutoscaling": t.proxy(
                    renames["VmwareNodePoolAutoscalingConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "config": t.proxy(renames["VmwareNodeConfigIn"]),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "onPremVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersVmwareNodePoolsDelete"] = gkeonprem.post(
        "v1/{parent}/vmwareNodePools",
        t.struct(
            {
                "vmwareNodePoolId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "nodePoolAutoscaling": t.proxy(
                    renames["VmwareNodePoolAutoscalingConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "config": t.proxy(renames["VmwareNodeConfigIn"]),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "onPremVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsVmwareClustersVmwareNodePoolsSetIamPolicy"
    ] = gkeonprem.post(
        "v1/{parent}/vmwareNodePools",
        t.struct(
            {
                "vmwareNodePoolId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "nodePoolAutoscaling": t.proxy(
                    renames["VmwareNodePoolAutoscalingConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "config": t.proxy(renames["VmwareNodeConfigIn"]),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "onPremVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersVmwareNodePoolsPatch"] = gkeonprem.post(
        "v1/{parent}/vmwareNodePools",
        t.struct(
            {
                "vmwareNodePoolId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "nodePoolAutoscaling": t.proxy(
                    renames["VmwareNodePoolAutoscalingConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "config": t.proxy(renames["VmwareNodeConfigIn"]),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "onPremVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersVmwareNodePoolsCreate"] = gkeonprem.post(
        "v1/{parent}/vmwareNodePools",
        t.struct(
            {
                "vmwareNodePoolId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "nodePoolAutoscaling": t.proxy(
                    renames["VmwareNodePoolAutoscalingConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "config": t.proxy(renames["VmwareNodeConfigIn"]),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "onPremVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsVmwareClustersVmwareNodePoolsOperationsList"
    ] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsVmwareClustersVmwareNodePoolsOperationsGet"
    ] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersOperationsList"] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersOperationsGet"] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="gkeonprem",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
