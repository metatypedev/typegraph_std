from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_gkeonprem() -> Import:
    gkeonprem = HTTPRuntime("https://gkeonprem.googleapis.com/")

    renames = {
        "ErrorResponse": "_gkeonprem_1_ErrorResponse",
        "VmwareAdminVCenterConfigIn": "_gkeonprem_2_VmwareAdminVCenterConfigIn",
        "VmwareAdminVCenterConfigOut": "_gkeonprem_3_VmwareAdminVCenterConfigOut",
        "BareMetalNodeConfigIn": "_gkeonprem_4_BareMetalNodeConfigIn",
        "BareMetalNodeConfigOut": "_gkeonprem_5_BareMetalNodeConfigOut",
        "VmwareHostIpIn": "_gkeonprem_6_VmwareHostIpIn",
        "VmwareHostIpOut": "_gkeonprem_7_VmwareHostIpOut",
        "EnrollBareMetalAdminClusterRequestIn": "_gkeonprem_8_EnrollBareMetalAdminClusterRequestIn",
        "EnrollBareMetalAdminClusterRequestOut": "_gkeonprem_9_EnrollBareMetalAdminClusterRequestOut",
        "BareMetalAdminControlPlaneConfigIn": "_gkeonprem_10_BareMetalAdminControlPlaneConfigIn",
        "BareMetalAdminControlPlaneConfigOut": "_gkeonprem_11_BareMetalAdminControlPlaneConfigOut",
        "BareMetalAdminVipConfigIn": "_gkeonprem_12_BareMetalAdminVipConfigIn",
        "BareMetalAdminVipConfigOut": "_gkeonprem_13_BareMetalAdminVipConfigOut",
        "OperationMetadataIn": "_gkeonprem_14_OperationMetadataIn",
        "OperationMetadataOut": "_gkeonprem_15_OperationMetadataOut",
        "VmwareVersionInfoIn": "_gkeonprem_16_VmwareVersionInfoIn",
        "VmwareVersionInfoOut": "_gkeonprem_17_VmwareVersionInfoOut",
        "BareMetalWorkloadNodeConfigIn": "_gkeonprem_18_BareMetalWorkloadNodeConfigIn",
        "BareMetalWorkloadNodeConfigOut": "_gkeonprem_19_BareMetalWorkloadNodeConfigOut",
        "ListBareMetalNodePoolsResponseIn": "_gkeonprem_20_ListBareMetalNodePoolsResponseIn",
        "ListBareMetalNodePoolsResponseOut": "_gkeonprem_21_ListBareMetalNodePoolsResponseOut",
        "BareMetalStorageConfigIn": "_gkeonprem_22_BareMetalStorageConfigIn",
        "BareMetalStorageConfigOut": "_gkeonprem_23_BareMetalStorageConfigOut",
        "BareMetalAdminManualLbConfigIn": "_gkeonprem_24_BareMetalAdminManualLbConfigIn",
        "BareMetalAdminManualLbConfigOut": "_gkeonprem_25_BareMetalAdminManualLbConfigOut",
        "BareMetalProxyConfigIn": "_gkeonprem_26_BareMetalProxyConfigIn",
        "BareMetalProxyConfigOut": "_gkeonprem_27_BareMetalProxyConfigOut",
        "EnrollVmwareAdminClusterRequestIn": "_gkeonprem_28_EnrollVmwareAdminClusterRequestIn",
        "EnrollVmwareAdminClusterRequestOut": "_gkeonprem_29_EnrollVmwareAdminClusterRequestOut",
        "BareMetalIslandModeCidrConfigIn": "_gkeonprem_30_BareMetalIslandModeCidrConfigIn",
        "BareMetalIslandModeCidrConfigOut": "_gkeonprem_31_BareMetalIslandModeCidrConfigOut",
        "ResourceConditionIn": "_gkeonprem_32_ResourceConditionIn",
        "ResourceConditionOut": "_gkeonprem_33_ResourceConditionOut",
        "VmwareMetalLbConfigIn": "_gkeonprem_34_VmwareMetalLbConfigIn",
        "VmwareMetalLbConfigOut": "_gkeonprem_35_VmwareMetalLbConfigOut",
        "FleetIn": "_gkeonprem_36_FleetIn",
        "FleetOut": "_gkeonprem_37_FleetOut",
        "VmwareIpBlockIn": "_gkeonprem_38_VmwareIpBlockIn",
        "VmwareIpBlockOut": "_gkeonprem_39_VmwareIpBlockOut",
        "EnrollVmwareNodePoolRequestIn": "_gkeonprem_40_EnrollVmwareNodePoolRequestIn",
        "EnrollVmwareNodePoolRequestOut": "_gkeonprem_41_EnrollVmwareNodePoolRequestOut",
        "VmwareAdminMetalLbConfigIn": "_gkeonprem_42_VmwareAdminMetalLbConfigIn",
        "VmwareAdminMetalLbConfigOut": "_gkeonprem_43_VmwareAdminMetalLbConfigOut",
        "VmwareControlPlaneV2ConfigIn": "_gkeonprem_44_VmwareControlPlaneV2ConfigIn",
        "VmwareControlPlaneV2ConfigOut": "_gkeonprem_45_VmwareControlPlaneV2ConfigOut",
        "BareMetalAdminDrainedMachineIn": "_gkeonprem_46_BareMetalAdminDrainedMachineIn",
        "BareMetalAdminDrainedMachineOut": "_gkeonprem_47_BareMetalAdminDrainedMachineOut",
        "VmwareDataplaneV2ConfigIn": "_gkeonprem_48_VmwareDataplaneV2ConfigIn",
        "VmwareDataplaneV2ConfigOut": "_gkeonprem_49_VmwareDataplaneV2ConfigOut",
        "VmwareNetworkConfigIn": "_gkeonprem_50_VmwareNetworkConfigIn",
        "VmwareNetworkConfigOut": "_gkeonprem_51_VmwareNetworkConfigOut",
        "VmwareVipConfigIn": "_gkeonprem_52_VmwareVipConfigIn",
        "VmwareVipConfigOut": "_gkeonprem_53_VmwareVipConfigOut",
        "QueryBareMetalAdminVersionConfigResponseIn": "_gkeonprem_54_QueryBareMetalAdminVersionConfigResponseIn",
        "QueryBareMetalAdminVersionConfigResponseOut": "_gkeonprem_55_QueryBareMetalAdminVersionConfigResponseOut",
        "PolicyIn": "_gkeonprem_56_PolicyIn",
        "PolicyOut": "_gkeonprem_57_PolicyOut",
        "BareMetalAdminNodeAccessConfigIn": "_gkeonprem_58_BareMetalAdminNodeAccessConfigIn",
        "BareMetalAdminNodeAccessConfigOut": "_gkeonprem_59_BareMetalAdminNodeAccessConfigOut",
        "BareMetalAdminDrainingMachineIn": "_gkeonprem_60_BareMetalAdminDrainingMachineIn",
        "BareMetalAdminDrainingMachineOut": "_gkeonprem_61_BareMetalAdminDrainingMachineOut",
        "VmwareLoadBalancerConfigIn": "_gkeonprem_62_VmwareLoadBalancerConfigIn",
        "VmwareLoadBalancerConfigOut": "_gkeonprem_63_VmwareLoadBalancerConfigOut",
        "BareMetalLoadBalancerConfigIn": "_gkeonprem_64_BareMetalLoadBalancerConfigIn",
        "BareMetalLoadBalancerConfigOut": "_gkeonprem_65_BareMetalLoadBalancerConfigOut",
        "VmwareHostConfigIn": "_gkeonprem_66_VmwareHostConfigIn",
        "VmwareHostConfigOut": "_gkeonprem_67_VmwareHostConfigOut",
        "BareMetalAdminMaintenanceStatusIn": "_gkeonprem_68_BareMetalAdminMaintenanceStatusIn",
        "BareMetalAdminMaintenanceStatusOut": "_gkeonprem_69_BareMetalAdminMaintenanceStatusOut",
        "ListBareMetalClustersResponseIn": "_gkeonprem_70_ListBareMetalClustersResponseIn",
        "ListBareMetalClustersResponseOut": "_gkeonprem_71_ListBareMetalClustersResponseOut",
        "ValidationCheckIn": "_gkeonprem_72_ValidationCheckIn",
        "ValidationCheckOut": "_gkeonprem_73_ValidationCheckOut",
        "BareMetalAdminNetworkConfigIn": "_gkeonprem_74_BareMetalAdminNetworkConfigIn",
        "BareMetalAdminNetworkConfigOut": "_gkeonprem_75_BareMetalAdminNetworkConfigOut",
        "BareMetalLvpConfigIn": "_gkeonprem_76_BareMetalLvpConfigIn",
        "BareMetalLvpConfigOut": "_gkeonprem_77_BareMetalLvpConfigOut",
        "BareMetalAdminSecurityConfigIn": "_gkeonprem_78_BareMetalAdminSecurityConfigIn",
        "BareMetalAdminSecurityConfigOut": "_gkeonprem_79_BareMetalAdminSecurityConfigOut",
        "BareMetalNodePoolConfigIn": "_gkeonprem_80_BareMetalNodePoolConfigIn",
        "BareMetalNodePoolConfigOut": "_gkeonprem_81_BareMetalNodePoolConfigOut",
        "BareMetalClusterIn": "_gkeonprem_82_BareMetalClusterIn",
        "BareMetalClusterOut": "_gkeonprem_83_BareMetalClusterOut",
        "VmwareVsphereTagIn": "_gkeonprem_84_VmwareVsphereTagIn",
        "VmwareVsphereTagOut": "_gkeonprem_85_VmwareVsphereTagOut",
        "BareMetalLoadBalancerAddressPoolIn": "_gkeonprem_86_BareMetalLoadBalancerAddressPoolIn",
        "BareMetalLoadBalancerAddressPoolOut": "_gkeonprem_87_BareMetalLoadBalancerAddressPoolOut",
        "BareMetalKubeletConfigIn": "_gkeonprem_88_BareMetalKubeletConfigIn",
        "BareMetalKubeletConfigOut": "_gkeonprem_89_BareMetalKubeletConfigOut",
        "ExprIn": "_gkeonprem_90_ExprIn",
        "ExprOut": "_gkeonprem_91_ExprOut",
        "OperationIn": "_gkeonprem_92_OperationIn",
        "OperationOut": "_gkeonprem_93_OperationOut",
        "VmwareBundleConfigIn": "_gkeonprem_94_VmwareBundleConfigIn",
        "VmwareBundleConfigOut": "_gkeonprem_95_VmwareBundleConfigOut",
        "ValidationCheckStatusIn": "_gkeonprem_96_ValidationCheckStatusIn",
        "ValidationCheckStatusOut": "_gkeonprem_97_ValidationCheckStatusOut",
        "BareMetalAdminMachineDrainStatusIn": "_gkeonprem_98_BareMetalAdminMachineDrainStatusIn",
        "BareMetalAdminMachineDrainStatusOut": "_gkeonprem_99_BareMetalAdminMachineDrainStatusOut",
        "LocationIn": "_gkeonprem_100_LocationIn",
        "LocationOut": "_gkeonprem_101_LocationOut",
        "BareMetalMetalLbConfigIn": "_gkeonprem_102_BareMetalMetalLbConfigIn",
        "BareMetalMetalLbConfigOut": "_gkeonprem_103_BareMetalMetalLbConfigOut",
        "VmwareAdminControlPlaneNodeConfigIn": "_gkeonprem_104_VmwareAdminControlPlaneNodeConfigIn",
        "VmwareAdminControlPlaneNodeConfigOut": "_gkeonprem_105_VmwareAdminControlPlaneNodeConfigOut",
        "VmwareAdminAddonNodeConfigIn": "_gkeonprem_106_VmwareAdminAddonNodeConfigIn",
        "VmwareAdminAddonNodeConfigOut": "_gkeonprem_107_VmwareAdminAddonNodeConfigOut",
        "BindingIn": "_gkeonprem_108_BindingIn",
        "BindingOut": "_gkeonprem_109_BindingOut",
        "BareMetalAdminControlPlaneNodePoolConfigIn": "_gkeonprem_110_BareMetalAdminControlPlaneNodePoolConfigIn",
        "BareMetalAdminControlPlaneNodePoolConfigOut": "_gkeonprem_111_BareMetalAdminControlPlaneNodePoolConfigOut",
        "StatusIn": "_gkeonprem_112_StatusIn",
        "StatusOut": "_gkeonprem_113_StatusOut",
        "BareMetalAdminLoadBalancerConfigIn": "_gkeonprem_114_BareMetalAdminLoadBalancerConfigIn",
        "BareMetalAdminLoadBalancerConfigOut": "_gkeonprem_115_BareMetalAdminLoadBalancerConfigOut",
        "VmwareNodePoolIn": "_gkeonprem_116_VmwareNodePoolIn",
        "VmwareNodePoolOut": "_gkeonprem_117_VmwareNodePoolOut",
        "BareMetalVipConfigIn": "_gkeonprem_118_BareMetalVipConfigIn",
        "BareMetalVipConfigOut": "_gkeonprem_119_BareMetalVipConfigOut",
        "EnrollBareMetalNodePoolRequestIn": "_gkeonprem_120_EnrollBareMetalNodePoolRequestIn",
        "EnrollBareMetalNodePoolRequestOut": "_gkeonprem_121_EnrollBareMetalNodePoolRequestOut",
        "NodeTaintIn": "_gkeonprem_122_NodeTaintIn",
        "NodeTaintOut": "_gkeonprem_123_NodeTaintOut",
        "VmwareManualLbConfigIn": "_gkeonprem_124_VmwareManualLbConfigIn",
        "VmwareManualLbConfigOut": "_gkeonprem_125_VmwareManualLbConfigOut",
        "BareMetalAdminClusterIn": "_gkeonprem_126_BareMetalAdminClusterIn",
        "BareMetalAdminClusterOut": "_gkeonprem_127_BareMetalAdminClusterOut",
        "BareMetalPortConfigIn": "_gkeonprem_128_BareMetalPortConfigIn",
        "BareMetalPortConfigOut": "_gkeonprem_129_BareMetalPortConfigOut",
        "BareMetalSecurityConfigIn": "_gkeonprem_130_BareMetalSecurityConfigIn",
        "BareMetalSecurityConfigOut": "_gkeonprem_131_BareMetalSecurityConfigOut",
        "SetIamPolicyRequestIn": "_gkeonprem_132_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_gkeonprem_133_SetIamPolicyRequestOut",
        "ValidationCheckResultIn": "_gkeonprem_134_ValidationCheckResultIn",
        "ValidationCheckResultOut": "_gkeonprem_135_ValidationCheckResultOut",
        "BareMetalBgpLbConfigIn": "_gkeonprem_136_BareMetalBgpLbConfigIn",
        "BareMetalBgpLbConfigOut": "_gkeonprem_137_BareMetalBgpLbConfigOut",
        "BareMetalDrainedMachineIn": "_gkeonprem_138_BareMetalDrainedMachineIn",
        "BareMetalDrainedMachineOut": "_gkeonprem_139_BareMetalDrainedMachineOut",
        "ListLocationsResponseIn": "_gkeonprem_140_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_gkeonprem_141_ListLocationsResponseOut",
        "ListVmwareNodePoolsResponseIn": "_gkeonprem_142_ListVmwareNodePoolsResponseIn",
        "ListVmwareNodePoolsResponseOut": "_gkeonprem_143_ListVmwareNodePoolsResponseOut",
        "BareMetalLoadBalancerNodePoolConfigIn": "_gkeonprem_144_BareMetalLoadBalancerNodePoolConfigIn",
        "BareMetalLoadBalancerNodePoolConfigOut": "_gkeonprem_145_BareMetalLoadBalancerNodePoolConfigOut",
        "BareMetalAdminIslandModeCidrConfigIn": "_gkeonprem_146_BareMetalAdminIslandModeCidrConfigIn",
        "BareMetalAdminIslandModeCidrConfigOut": "_gkeonprem_147_BareMetalAdminIslandModeCidrConfigOut",
        "EnrollVmwareClusterRequestIn": "_gkeonprem_148_EnrollVmwareClusterRequestIn",
        "EnrollVmwareClusterRequestOut": "_gkeonprem_149_EnrollVmwareClusterRequestOut",
        "VmwareControlPlaneVsphereConfigIn": "_gkeonprem_150_VmwareControlPlaneVsphereConfigIn",
        "VmwareControlPlaneVsphereConfigOut": "_gkeonprem_151_VmwareControlPlaneVsphereConfigOut",
        "BareMetalMachineDrainStatusIn": "_gkeonprem_152_BareMetalMachineDrainStatusIn",
        "BareMetalMachineDrainStatusOut": "_gkeonprem_153_BareMetalMachineDrainStatusOut",
        "BareMetalAdminClusterOperationsConfigIn": "_gkeonprem_154_BareMetalAdminClusterOperationsConfigIn",
        "BareMetalAdminClusterOperationsConfigOut": "_gkeonprem_155_BareMetalAdminClusterOperationsConfigOut",
        "VmwareAdminManualLbConfigIn": "_gkeonprem_156_VmwareAdminManualLbConfigIn",
        "VmwareAdminManualLbConfigOut": "_gkeonprem_157_VmwareAdminManualLbConfigOut",
        "VmwareAAGConfigIn": "_gkeonprem_158_VmwareAAGConfigIn",
        "VmwareAAGConfigOut": "_gkeonprem_159_VmwareAAGConfigOut",
        "VmwareAddressPoolIn": "_gkeonprem_160_VmwareAddressPoolIn",
        "VmwareAddressPoolOut": "_gkeonprem_161_VmwareAddressPoolOut",
        "VmwareAutoRepairConfigIn": "_gkeonprem_162_VmwareAutoRepairConfigIn",
        "VmwareAutoRepairConfigOut": "_gkeonprem_163_VmwareAutoRepairConfigOut",
        "BareMetalBgpPeerConfigIn": "_gkeonprem_164_BareMetalBgpPeerConfigIn",
        "BareMetalBgpPeerConfigOut": "_gkeonprem_165_BareMetalBgpPeerConfigOut",
        "VmwareVCenterConfigIn": "_gkeonprem_166_VmwareVCenterConfigIn",
        "VmwareVCenterConfigOut": "_gkeonprem_167_VmwareVCenterConfigOut",
        "BareMetalAdminWorkloadNodeConfigIn": "_gkeonprem_168_BareMetalAdminWorkloadNodeConfigIn",
        "BareMetalAdminWorkloadNodeConfigOut": "_gkeonprem_169_BareMetalAdminWorkloadNodeConfigOut",
        "VmwareNodeConfigIn": "_gkeonprem_170_VmwareNodeConfigIn",
        "VmwareNodeConfigOut": "_gkeonprem_171_VmwareNodeConfigOut",
        "VmwareAdminNetworkConfigIn": "_gkeonprem_172_VmwareAdminNetworkConfigIn",
        "VmwareAdminNetworkConfigOut": "_gkeonprem_173_VmwareAdminNetworkConfigOut",
        "BareMetalLvpShareConfigIn": "_gkeonprem_174_BareMetalLvpShareConfigIn",
        "BareMetalLvpShareConfigOut": "_gkeonprem_175_BareMetalLvpShareConfigOut",
        "BareMetalControlPlaneNodePoolConfigIn": "_gkeonprem_176_BareMetalControlPlaneNodePoolConfigIn",
        "BareMetalControlPlaneNodePoolConfigOut": "_gkeonprem_177_BareMetalControlPlaneNodePoolConfigOut",
        "TestIamPermissionsRequestIn": "_gkeonprem_178_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_gkeonprem_179_TestIamPermissionsRequestOut",
        "QueryBareMetalVersionConfigResponseIn": "_gkeonprem_180_QueryBareMetalVersionConfigResponseIn",
        "QueryBareMetalVersionConfigResponseOut": "_gkeonprem_181_QueryBareMetalVersionConfigResponseOut",
        "VmwarePlatformConfigIn": "_gkeonprem_182_VmwarePlatformConfigIn",
        "VmwarePlatformConfigOut": "_gkeonprem_183_VmwarePlatformConfigOut",
        "BareMetalNodePoolIn": "_gkeonprem_184_BareMetalNodePoolIn",
        "BareMetalNodePoolOut": "_gkeonprem_185_BareMetalNodePoolOut",
        "BareMetalManualLbConfigIn": "_gkeonprem_186_BareMetalManualLbConfigIn",
        "BareMetalManualLbConfigOut": "_gkeonprem_187_BareMetalManualLbConfigOut",
        "BareMetalAdminApiServerArgumentIn": "_gkeonprem_188_BareMetalAdminApiServerArgumentIn",
        "BareMetalAdminApiServerArgumentOut": "_gkeonprem_189_BareMetalAdminApiServerArgumentOut",
        "BareMetalAdminProxyConfigIn": "_gkeonprem_190_BareMetalAdminProxyConfigIn",
        "BareMetalAdminProxyConfigOut": "_gkeonprem_191_BareMetalAdminProxyConfigOut",
        "EnrollBareMetalClusterRequestIn": "_gkeonprem_192_EnrollBareMetalClusterRequestIn",
        "EnrollBareMetalClusterRequestOut": "_gkeonprem_193_EnrollBareMetalClusterRequestOut",
        "VmwareVsphereConfigIn": "_gkeonprem_194_VmwareVsphereConfigIn",
        "VmwareVsphereConfigOut": "_gkeonprem_195_VmwareVsphereConfigOut",
        "ResourceStatusIn": "_gkeonprem_196_ResourceStatusIn",
        "ResourceStatusOut": "_gkeonprem_197_ResourceStatusOut",
        "BareMetalVersionInfoIn": "_gkeonprem_198_BareMetalVersionInfoIn",
        "BareMetalVersionInfoOut": "_gkeonprem_199_BareMetalVersionInfoOut",
        "ListBareMetalAdminClustersResponseIn": "_gkeonprem_200_ListBareMetalAdminClustersResponseIn",
        "ListBareMetalAdminClustersResponseOut": "_gkeonprem_201_ListBareMetalAdminClustersResponseOut",
        "VmwareNodePoolAutoscalingConfigIn": "_gkeonprem_202_VmwareNodePoolAutoscalingConfigIn",
        "VmwareNodePoolAutoscalingConfigOut": "_gkeonprem_203_VmwareNodePoolAutoscalingConfigOut",
        "VmwareStorageConfigIn": "_gkeonprem_204_VmwareStorageConfigIn",
        "VmwareStorageConfigOut": "_gkeonprem_205_VmwareStorageConfigOut",
        "TestIamPermissionsResponseIn": "_gkeonprem_206_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_gkeonprem_207_TestIamPermissionsResponseOut",
        "VmwareAdminLoadBalancerConfigIn": "_gkeonprem_208_VmwareAdminLoadBalancerConfigIn",
        "VmwareAdminLoadBalancerConfigOut": "_gkeonprem_209_VmwareAdminLoadBalancerConfigOut",
        "QueryVmwareVersionConfigResponseIn": "_gkeonprem_210_QueryVmwareVersionConfigResponseIn",
        "QueryVmwareVersionConfigResponseOut": "_gkeonprem_211_QueryVmwareVersionConfigResponseOut",
        "ClusterUserIn": "_gkeonprem_212_ClusterUserIn",
        "ClusterUserOut": "_gkeonprem_213_ClusterUserOut",
        "AuthorizationIn": "_gkeonprem_214_AuthorizationIn",
        "AuthorizationOut": "_gkeonprem_215_AuthorizationOut",
        "BareMetalDrainingMachineIn": "_gkeonprem_216_BareMetalDrainingMachineIn",
        "BareMetalDrainingMachineOut": "_gkeonprem_217_BareMetalDrainingMachineOut",
        "VmwareAutoResizeConfigIn": "_gkeonprem_218_VmwareAutoResizeConfigIn",
        "VmwareAutoResizeConfigOut": "_gkeonprem_219_VmwareAutoResizeConfigOut",
        "BareMetalAdminPortConfigIn": "_gkeonprem_220_BareMetalAdminPortConfigIn",
        "BareMetalAdminPortConfigOut": "_gkeonprem_221_BareMetalAdminPortConfigOut",
        "BareMetalMultipleNetworkInterfacesConfigIn": "_gkeonprem_222_BareMetalMultipleNetworkInterfacesConfigIn",
        "BareMetalMultipleNetworkInterfacesConfigOut": "_gkeonprem_223_BareMetalMultipleNetworkInterfacesConfigOut",
        "BareMetalNetworkConfigIn": "_gkeonprem_224_BareMetalNetworkConfigIn",
        "BareMetalNetworkConfigOut": "_gkeonprem_225_BareMetalNetworkConfigOut",
        "BareMetalAdminOsEnvironmentConfigIn": "_gkeonprem_226_BareMetalAdminOsEnvironmentConfigIn",
        "BareMetalAdminOsEnvironmentConfigOut": "_gkeonprem_227_BareMetalAdminOsEnvironmentConfigOut",
        "VmwareControlPlaneNodeConfigIn": "_gkeonprem_228_VmwareControlPlaneNodeConfigIn",
        "VmwareControlPlaneNodeConfigOut": "_gkeonprem_229_VmwareControlPlaneNodeConfigOut",
        "BareMetalMaintenanceStatusIn": "_gkeonprem_230_BareMetalMaintenanceStatusIn",
        "BareMetalMaintenanceStatusOut": "_gkeonprem_231_BareMetalMaintenanceStatusOut",
        "BareMetalClusterOperationsConfigIn": "_gkeonprem_232_BareMetalClusterOperationsConfigIn",
        "BareMetalClusterOperationsConfigOut": "_gkeonprem_233_BareMetalClusterOperationsConfigOut",
        "BareMetalMaintenanceConfigIn": "_gkeonprem_234_BareMetalMaintenanceConfigIn",
        "BareMetalMaintenanceConfigOut": "_gkeonprem_235_BareMetalMaintenanceConfigOut",
        "ListOperationsResponseIn": "_gkeonprem_236_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_gkeonprem_237_ListOperationsResponseOut",
        "BareMetalAdminStorageConfigIn": "_gkeonprem_238_BareMetalAdminStorageConfigIn",
        "BareMetalAdminStorageConfigOut": "_gkeonprem_239_BareMetalAdminStorageConfigOut",
        "VmwareDhcpIpConfigIn": "_gkeonprem_240_VmwareDhcpIpConfigIn",
        "VmwareDhcpIpConfigOut": "_gkeonprem_241_VmwareDhcpIpConfigOut",
        "CancelOperationRequestIn": "_gkeonprem_242_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_gkeonprem_243_CancelOperationRequestOut",
        "ListVmwareAdminClustersResponseIn": "_gkeonprem_244_ListVmwareAdminClustersResponseIn",
        "ListVmwareAdminClustersResponseOut": "_gkeonprem_245_ListVmwareAdminClustersResponseOut",
        "BareMetalApiServerArgumentIn": "_gkeonprem_246_BareMetalApiServerArgumentIn",
        "BareMetalApiServerArgumentOut": "_gkeonprem_247_BareMetalApiServerArgumentOut",
        "BareMetalNodeAccessConfigIn": "_gkeonprem_248_BareMetalNodeAccessConfigIn",
        "BareMetalNodeAccessConfigOut": "_gkeonprem_249_BareMetalNodeAccessConfigOut",
        "VmwareAdminVipConfigIn": "_gkeonprem_250_VmwareAdminVipConfigIn",
        "VmwareAdminVipConfigOut": "_gkeonprem_251_VmwareAdminVipConfigOut",
        "BareMetalControlPlaneConfigIn": "_gkeonprem_252_BareMetalControlPlaneConfigIn",
        "BareMetalControlPlaneConfigOut": "_gkeonprem_253_BareMetalControlPlaneConfigOut",
        "VmwareStaticIpConfigIn": "_gkeonprem_254_VmwareStaticIpConfigIn",
        "VmwareStaticIpConfigOut": "_gkeonprem_255_VmwareStaticIpConfigOut",
        "VmwareAdminF5BigIpConfigIn": "_gkeonprem_256_VmwareAdminF5BigIpConfigIn",
        "VmwareAdminF5BigIpConfigOut": "_gkeonprem_257_VmwareAdminF5BigIpConfigOut",
        "VmwareAdminClusterIn": "_gkeonprem_258_VmwareAdminClusterIn",
        "VmwareAdminClusterOut": "_gkeonprem_259_VmwareAdminClusterOut",
        "BareMetalAdminMaintenanceConfigIn": "_gkeonprem_260_BareMetalAdminMaintenanceConfigIn",
        "BareMetalAdminMaintenanceConfigOut": "_gkeonprem_261_BareMetalAdminMaintenanceConfigOut",
        "BareMetalSrIovConfigIn": "_gkeonprem_262_BareMetalSrIovConfigIn",
        "BareMetalSrIovConfigOut": "_gkeonprem_263_BareMetalSrIovConfigOut",
        "VmwareClusterIn": "_gkeonprem_264_VmwareClusterIn",
        "VmwareClusterOut": "_gkeonprem_265_VmwareClusterOut",
        "EmptyIn": "_gkeonprem_266_EmptyIn",
        "EmptyOut": "_gkeonprem_267_EmptyOut",
        "BareMetalOsEnvironmentConfigIn": "_gkeonprem_268_BareMetalOsEnvironmentConfigIn",
        "BareMetalOsEnvironmentConfigOut": "_gkeonprem_269_BareMetalOsEnvironmentConfigOut",
        "VmwareF5BigIpConfigIn": "_gkeonprem_270_VmwareF5BigIpConfigIn",
        "VmwareF5BigIpConfigOut": "_gkeonprem_271_VmwareF5BigIpConfigOut",
        "ListVmwareClustersResponseIn": "_gkeonprem_272_ListVmwareClustersResponseIn",
        "ListVmwareClustersResponseOut": "_gkeonprem_273_ListVmwareClustersResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["VmwareAdminVCenterConfigIn"] = t.struct(
        {
            "caCertData": t.string().optional(),
            "dataDisk": t.string().optional(),
            "resourcePool": t.string().optional(),
            "address": t.string().optional(),
            "datacenter": t.string().optional(),
            "datastore": t.string().optional(),
            "folder": t.string().optional(),
            "cluster": t.string().optional(),
        }
    ).named(renames["VmwareAdminVCenterConfigIn"])
    types["VmwareAdminVCenterConfigOut"] = t.struct(
        {
            "caCertData": t.string().optional(),
            "dataDisk": t.string().optional(),
            "resourcePool": t.string().optional(),
            "address": t.string().optional(),
            "datacenter": t.string().optional(),
            "datastore": t.string().optional(),
            "folder": t.string().optional(),
            "cluster": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAdminVCenterConfigOut"])
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
    types["VmwareHostIpIn"] = t.struct(
        {"ip": t.string().optional(), "hostname": t.string().optional()}
    ).named(renames["VmwareHostIpIn"])
    types["VmwareHostIpOut"] = t.struct(
        {
            "ip": t.string().optional(),
            "hostname": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareHostIpOut"])
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
    types["BareMetalAdminControlPlaneConfigIn"] = t.struct(
        {
            "apiServerArgs": t.array(
                t.proxy(renames["BareMetalAdminApiServerArgumentIn"])
            ).optional(),
            "controlPlaneNodePoolConfig": t.proxy(
                renames["BareMetalAdminControlPlaneNodePoolConfigIn"]
            ).optional(),
        }
    ).named(renames["BareMetalAdminControlPlaneConfigIn"])
    types["BareMetalAdminControlPlaneConfigOut"] = t.struct(
        {
            "apiServerArgs": t.array(
                t.proxy(renames["BareMetalAdminApiServerArgumentOut"])
            ).optional(),
            "controlPlaneNodePoolConfig": t.proxy(
                renames["BareMetalAdminControlPlaneNodePoolConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminControlPlaneConfigOut"])
    types["BareMetalAdminVipConfigIn"] = t.struct(
        {"controlPlaneVip": t.string().optional()}
    ).named(renames["BareMetalAdminVipConfigIn"])
    types["BareMetalAdminVipConfigOut"] = t.struct(
        {
            "controlPlaneVip": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminVipConfigOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "type": t.string().optional(),
            "statusMessage": t.string().optional(),
            "apiVersion": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["VmwareVersionInfoIn"] = t.struct(
        {
            "isInstalled": t.boolean().optional(),
            "version": t.string().optional(),
            "hasDependencies": t.boolean().optional(),
        }
    ).named(renames["VmwareVersionInfoIn"])
    types["VmwareVersionInfoOut"] = t.struct(
        {
            "isInstalled": t.boolean().optional(),
            "version": t.string().optional(),
            "hasDependencies": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareVersionInfoOut"])
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
    types["ListBareMetalNodePoolsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "bareMetalNodePools": t.array(
                t.proxy(renames["BareMetalNodePoolIn"])
            ).optional(),
        }
    ).named(renames["ListBareMetalNodePoolsResponseIn"])
    types["ListBareMetalNodePoolsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "bareMetalNodePools": t.array(
                t.proxy(renames["BareMetalNodePoolOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBareMetalNodePoolsResponseOut"])
    types["BareMetalStorageConfigIn"] = t.struct(
        {
            "lvpShareConfig": t.proxy(renames["BareMetalLvpShareConfigIn"]),
            "lvpNodeMountsConfig": t.proxy(renames["BareMetalLvpConfigIn"]),
        }
    ).named(renames["BareMetalStorageConfigIn"])
    types["BareMetalStorageConfigOut"] = t.struct(
        {
            "lvpShareConfig": t.proxy(renames["BareMetalLvpShareConfigOut"]),
            "lvpNodeMountsConfig": t.proxy(renames["BareMetalLvpConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalStorageConfigOut"])
    types["BareMetalAdminManualLbConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["BareMetalAdminManualLbConfigIn"])
    types["BareMetalAdminManualLbConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminManualLbConfigOut"])
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
    types["EnrollVmwareAdminClusterRequestIn"] = t.struct(
        {
            "membership": t.string(),
            "localName": t.string().optional(),
            "vmwareAdminClusterId": t.string().optional(),
        }
    ).named(renames["EnrollVmwareAdminClusterRequestIn"])
    types["EnrollVmwareAdminClusterRequestOut"] = t.struct(
        {
            "membership": t.string(),
            "localName": t.string().optional(),
            "vmwareAdminClusterId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollVmwareAdminClusterRequestOut"])
    types["BareMetalIslandModeCidrConfigIn"] = t.struct(
        {
            "podAddressCidrBlocks": t.array(t.string()),
            "serviceAddressCidrBlocks": t.array(t.string()),
        }
    ).named(renames["BareMetalIslandModeCidrConfigIn"])
    types["BareMetalIslandModeCidrConfigOut"] = t.struct(
        {
            "podAddressCidrBlocks": t.array(t.string()),
            "serviceAddressCidrBlocks": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalIslandModeCidrConfigOut"])
    types["ResourceConditionIn"] = t.struct(
        {
            "message": t.string().optional(),
            "lastTransitionTime": t.string().optional(),
            "reason": t.string().optional(),
            "type": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["ResourceConditionIn"])
    types["ResourceConditionOut"] = t.struct(
        {
            "message": t.string().optional(),
            "lastTransitionTime": t.string().optional(),
            "reason": t.string().optional(),
            "type": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceConditionOut"])
    types["VmwareMetalLbConfigIn"] = t.struct(
        {"addressPools": t.array(t.proxy(renames["VmwareAddressPoolIn"]))}
    ).named(renames["VmwareMetalLbConfigIn"])
    types["VmwareMetalLbConfigOut"] = t.struct(
        {
            "addressPools": t.array(t.proxy(renames["VmwareAddressPoolOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareMetalLbConfigOut"])
    types["FleetIn"] = t.struct({"_": t.string().optional()}).named(renames["FleetIn"])
    types["FleetOut"] = t.struct(
        {
            "membership": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FleetOut"])
    types["VmwareIpBlockIn"] = t.struct(
        {
            "ips": t.array(t.proxy(renames["VmwareHostIpIn"])).optional(),
            "gateway": t.string().optional(),
            "netmask": t.string().optional(),
        }
    ).named(renames["VmwareIpBlockIn"])
    types["VmwareIpBlockOut"] = t.struct(
        {
            "ips": t.array(t.proxy(renames["VmwareHostIpOut"])).optional(),
            "gateway": t.string().optional(),
            "netmask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareIpBlockOut"])
    types["EnrollVmwareNodePoolRequestIn"] = t.struct(
        {"vmwareNodePoolId": t.string().optional()}
    ).named(renames["EnrollVmwareNodePoolRequestIn"])
    types["EnrollVmwareNodePoolRequestOut"] = t.struct(
        {
            "vmwareNodePoolId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollVmwareNodePoolRequestOut"])
    types["VmwareAdminMetalLbConfigIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VmwareAdminMetalLbConfigIn"]
    )
    types["VmwareAdminMetalLbConfigOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["VmwareAdminMetalLbConfigOut"])
    types["VmwareControlPlaneV2ConfigIn"] = t.struct(
        {"controlPlaneIpBlock": t.proxy(renames["VmwareIpBlockIn"]).optional()}
    ).named(renames["VmwareControlPlaneV2ConfigIn"])
    types["VmwareControlPlaneV2ConfigOut"] = t.struct(
        {
            "controlPlaneIpBlock": t.proxy(renames["VmwareIpBlockOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareControlPlaneV2ConfigOut"])
    types["BareMetalAdminDrainedMachineIn"] = t.struct(
        {"nodeIp": t.string().optional()}
    ).named(renames["BareMetalAdminDrainedMachineIn"])
    types["BareMetalAdminDrainedMachineOut"] = t.struct(
        {
            "nodeIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminDrainedMachineOut"])
    types["VmwareDataplaneV2ConfigIn"] = t.struct(
        {
            "windowsDataplaneV2Enabled": t.boolean().optional(),
            "dataplaneV2Enabled": t.boolean().optional(),
            "advancedNetworking": t.boolean().optional(),
        }
    ).named(renames["VmwareDataplaneV2ConfigIn"])
    types["VmwareDataplaneV2ConfigOut"] = t.struct(
        {
            "windowsDataplaneV2Enabled": t.boolean().optional(),
            "dataplaneV2Enabled": t.boolean().optional(),
            "advancedNetworking": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareDataplaneV2ConfigOut"])
    types["VmwareNetworkConfigIn"] = t.struct(
        {
            "hostConfig": t.proxy(renames["VmwareHostConfigIn"]).optional(),
            "serviceAddressCidrBlocks": t.array(t.string()),
            "staticIpConfig": t.proxy(renames["VmwareStaticIpConfigIn"]).optional(),
            "podAddressCidrBlocks": t.array(t.string()),
            "dhcpIpConfig": t.proxy(renames["VmwareDhcpIpConfigIn"]).optional(),
            "controlPlaneV2Config": t.proxy(
                renames["VmwareControlPlaneV2ConfigIn"]
            ).optional(),
        }
    ).named(renames["VmwareNetworkConfigIn"])
    types["VmwareNetworkConfigOut"] = t.struct(
        {
            "hostConfig": t.proxy(renames["VmwareHostConfigOut"]).optional(),
            "serviceAddressCidrBlocks": t.array(t.string()),
            "staticIpConfig": t.proxy(renames["VmwareStaticIpConfigOut"]).optional(),
            "podAddressCidrBlocks": t.array(t.string()),
            "dhcpIpConfig": t.proxy(renames["VmwareDhcpIpConfigOut"]).optional(),
            "vcenterNetwork": t.string().optional(),
            "controlPlaneV2Config": t.proxy(
                renames["VmwareControlPlaneV2ConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareNetworkConfigOut"])
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
    types["QueryBareMetalAdminVersionConfigResponseIn"] = t.struct(
        {"versions": t.array(t.proxy(renames["BareMetalVersionInfoIn"])).optional()}
    ).named(renames["QueryBareMetalAdminVersionConfigResponseIn"])
    types["QueryBareMetalAdminVersionConfigResponseOut"] = t.struct(
        {
            "versions": t.array(t.proxy(renames["BareMetalVersionInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryBareMetalAdminVersionConfigResponseOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["BareMetalAdminNodeAccessConfigIn"] = t.struct(
        {"loginUser": t.string()}
    ).named(renames["BareMetalAdminNodeAccessConfigIn"])
    types["BareMetalAdminNodeAccessConfigOut"] = t.struct(
        {"loginUser": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["BareMetalAdminNodeAccessConfigOut"])
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
    types["VmwareLoadBalancerConfigIn"] = t.struct(
        {
            "metalLbConfig": t.proxy(renames["VmwareMetalLbConfigIn"]).optional(),
            "f5Config": t.proxy(renames["VmwareF5BigIpConfigIn"]).optional(),
            "vipConfig": t.proxy(renames["VmwareVipConfigIn"]).optional(),
            "manualLbConfig": t.proxy(renames["VmwareManualLbConfigIn"]).optional(),
        }
    ).named(renames["VmwareLoadBalancerConfigIn"])
    types["VmwareLoadBalancerConfigOut"] = t.struct(
        {
            "metalLbConfig": t.proxy(renames["VmwareMetalLbConfigOut"]).optional(),
            "f5Config": t.proxy(renames["VmwareF5BigIpConfigOut"]).optional(),
            "vipConfig": t.proxy(renames["VmwareVipConfigOut"]).optional(),
            "manualLbConfig": t.proxy(renames["VmwareManualLbConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareLoadBalancerConfigOut"])
    types["BareMetalLoadBalancerConfigIn"] = t.struct(
        {
            "portConfig": t.proxy(renames["BareMetalPortConfigIn"]).optional(),
            "metalLbConfig": t.proxy(renames["BareMetalMetalLbConfigIn"]).optional(),
            "bgpLbConfig": t.proxy(renames["BareMetalBgpLbConfigIn"]).optional(),
            "manualLbConfig": t.proxy(renames["BareMetalManualLbConfigIn"]).optional(),
            "vipConfig": t.proxy(renames["BareMetalVipConfigIn"]).optional(),
        }
    ).named(renames["BareMetalLoadBalancerConfigIn"])
    types["BareMetalLoadBalancerConfigOut"] = t.struct(
        {
            "portConfig": t.proxy(renames["BareMetalPortConfigOut"]).optional(),
            "metalLbConfig": t.proxy(renames["BareMetalMetalLbConfigOut"]).optional(),
            "bgpLbConfig": t.proxy(renames["BareMetalBgpLbConfigOut"]).optional(),
            "manualLbConfig": t.proxy(renames["BareMetalManualLbConfigOut"]).optional(),
            "vipConfig": t.proxy(renames["BareMetalVipConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalLoadBalancerConfigOut"])
    types["VmwareHostConfigIn"] = t.struct(
        {
            "dnsSearchDomains": t.array(t.string()).optional(),
            "dnsServers": t.array(t.string()).optional(),
            "ntpServers": t.array(t.string()).optional(),
        }
    ).named(renames["VmwareHostConfigIn"])
    types["VmwareHostConfigOut"] = t.struct(
        {
            "dnsSearchDomains": t.array(t.string()).optional(),
            "dnsServers": t.array(t.string()).optional(),
            "ntpServers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareHostConfigOut"])
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
    types["ListBareMetalClustersResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "bareMetalClusters": t.array(
                t.proxy(renames["BareMetalClusterIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListBareMetalClustersResponseIn"])
    types["ListBareMetalClustersResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "bareMetalClusters": t.array(
                t.proxy(renames["BareMetalClusterOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBareMetalClustersResponseOut"])
    types["ValidationCheckIn"] = t.struct({"option": t.string().optional()}).named(
        renames["ValidationCheckIn"]
    )
    types["ValidationCheckOut"] = t.struct(
        {
            "scenario": t.string().optional(),
            "status": t.proxy(renames["ValidationCheckStatusOut"]).optional(),
            "option": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationCheckOut"])
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
    types["BareMetalLvpConfigIn"] = t.struct(
        {"path": t.string(), "storageClass": t.string()}
    ).named(renames["BareMetalLvpConfigIn"])
    types["BareMetalLvpConfigOut"] = t.struct(
        {
            "path": t.string(),
            "storageClass": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalLvpConfigOut"])
    types["BareMetalAdminSecurityConfigIn"] = t.struct(
        {"authorization": t.proxy(renames["AuthorizationIn"]).optional()}
    ).named(renames["BareMetalAdminSecurityConfigIn"])
    types["BareMetalAdminSecurityConfigOut"] = t.struct(
        {
            "authorization": t.proxy(renames["AuthorizationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminSecurityConfigOut"])
    types["BareMetalNodePoolConfigIn"] = t.struct(
        {
            "taints": t.array(t.proxy(renames["NodeTaintIn"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "operatingSystem": t.string().optional(),
            "kubeletConfig": t.proxy(renames["BareMetalKubeletConfigIn"]).optional(),
            "nodeConfigs": t.array(t.proxy(renames["BareMetalNodeConfigIn"])),
        }
    ).named(renames["BareMetalNodePoolConfigIn"])
    types["BareMetalNodePoolConfigOut"] = t.struct(
        {
            "taints": t.array(t.proxy(renames["NodeTaintOut"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "operatingSystem": t.string().optional(),
            "kubeletConfig": t.proxy(renames["BareMetalKubeletConfigOut"]).optional(),
            "nodeConfigs": t.array(t.proxy(renames["BareMetalNodeConfigOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalNodePoolConfigOut"])
    types["BareMetalClusterIn"] = t.struct(
        {
            "description": t.string().optional(),
            "networkConfig": t.proxy(renames["BareMetalNetworkConfigIn"]),
            "proxy": t.proxy(renames["BareMetalProxyConfigIn"]).optional(),
            "loadBalancer": t.proxy(renames["BareMetalLoadBalancerConfigIn"]),
            "maintenanceConfig": t.proxy(
                renames["BareMetalMaintenanceConfigIn"]
            ).optional(),
            "nodeAccessConfig": t.proxy(
                renames["BareMetalNodeAccessConfigIn"]
            ).optional(),
            "osEnvironmentConfig": t.proxy(
                renames["BareMetalOsEnvironmentConfigIn"]
            ).optional(),
            "bareMetalVersion": t.string(),
            "adminClusterMembership": t.string(),
            "securityConfig": t.proxy(renames["BareMetalSecurityConfigIn"]).optional(),
            "storage": t.proxy(renames["BareMetalStorageConfigIn"]),
            "nodeConfig": t.proxy(renames["BareMetalWorkloadNodeConfigIn"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "controlPlane": t.proxy(renames["BareMetalControlPlaneConfigIn"]),
            "clusterOperations": t.proxy(
                renames["BareMetalClusterOperationsConfigIn"]
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["BareMetalClusterIn"])
    types["BareMetalClusterOut"] = t.struct(
        {
            "localName": t.string().optional(),
            "description": t.string().optional(),
            "validationCheck": t.proxy(renames["ValidationCheckOut"]).optional(),
            "maintenanceStatus": t.proxy(
                renames["BareMetalMaintenanceStatusOut"]
            ).optional(),
            "networkConfig": t.proxy(renames["BareMetalNetworkConfigOut"]),
            "proxy": t.proxy(renames["BareMetalProxyConfigOut"]).optional(),
            "loadBalancer": t.proxy(renames["BareMetalLoadBalancerConfigOut"]),
            "maintenanceConfig": t.proxy(
                renames["BareMetalMaintenanceConfigOut"]
            ).optional(),
            "adminClusterName": t.string().optional(),
            "uid": t.string().optional(),
            "etag": t.string().optional(),
            "nodeAccessConfig": t.proxy(
                renames["BareMetalNodeAccessConfigOut"]
            ).optional(),
            "osEnvironmentConfig": t.proxy(
                renames["BareMetalOsEnvironmentConfigOut"]
            ).optional(),
            "bareMetalVersion": t.string(),
            "adminClusterMembership": t.string(),
            "securityConfig": t.proxy(renames["BareMetalSecurityConfigOut"]).optional(),
            "storage": t.proxy(renames["BareMetalStorageConfigOut"]),
            "deleteTime": t.string().optional(),
            "fleet": t.proxy(renames["FleetOut"]).optional(),
            "nodeConfig": t.proxy(renames["BareMetalWorkloadNodeConfigOut"]).optional(),
            "createTime": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "reconciling": t.boolean().optional(),
            "endpoint": t.string().optional(),
            "controlPlane": t.proxy(renames["BareMetalControlPlaneConfigOut"]),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "clusterOperations": t.proxy(
                renames["BareMetalClusterOperationsConfigOut"]
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalClusterOut"])
    types["VmwareVsphereTagIn"] = t.struct(
        {"tag": t.string().optional(), "category": t.string().optional()}
    ).named(renames["VmwareVsphereTagIn"])
    types["VmwareVsphereTagOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "category": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareVsphereTagOut"])
    types["BareMetalLoadBalancerAddressPoolIn"] = t.struct(
        {
            "manualAssign": t.boolean().optional(),
            "pool": t.string(),
            "avoidBuggyIps": t.boolean().optional(),
            "addresses": t.array(t.string()),
        }
    ).named(renames["BareMetalLoadBalancerAddressPoolIn"])
    types["BareMetalLoadBalancerAddressPoolOut"] = t.struct(
        {
            "manualAssign": t.boolean().optional(),
            "pool": t.string(),
            "avoidBuggyIps": t.boolean().optional(),
            "addresses": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalLoadBalancerAddressPoolOut"])
    types["BareMetalKubeletConfigIn"] = t.struct(
        {
            "serializeImagePullsDisabled": t.boolean().optional(),
            "registryBurst": t.integer().optional(),
            "registryPullQps": t.integer().optional(),
        }
    ).named(renames["BareMetalKubeletConfigIn"])
    types["BareMetalKubeletConfigOut"] = t.struct(
        {
            "serializeImagePullsDisabled": t.boolean().optional(),
            "registryBurst": t.integer().optional(),
            "registryPullQps": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalKubeletConfigOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["VmwareBundleConfigIn"] = t.struct({"version": t.string().optional()}).named(
        renames["VmwareBundleConfigIn"]
    )
    types["VmwareBundleConfigOut"] = t.struct(
        {
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareBundleConfigOut"])
    types["ValidationCheckStatusIn"] = t.struct(
        {"result": t.array(t.proxy(renames["ValidationCheckResultIn"])).optional()}
    ).named(renames["ValidationCheckStatusIn"])
    types["ValidationCheckStatusOut"] = t.struct(
        {
            "result": t.array(t.proxy(renames["ValidationCheckResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationCheckStatusOut"])
    types["BareMetalAdminMachineDrainStatusIn"] = t.struct(
        {
            "drainingMachines": t.array(
                t.proxy(renames["BareMetalAdminDrainingMachineIn"])
            ).optional(),
            "drainedMachines": t.array(
                t.proxy(renames["BareMetalAdminDrainedMachineIn"])
            ).optional(),
        }
    ).named(renames["BareMetalAdminMachineDrainStatusIn"])
    types["BareMetalAdminMachineDrainStatusOut"] = t.struct(
        {
            "drainingMachines": t.array(
                t.proxy(renames["BareMetalAdminDrainingMachineOut"])
            ).optional(),
            "drainedMachines": t.array(
                t.proxy(renames["BareMetalAdminDrainedMachineOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminMachineDrainStatusOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["BareMetalAdminControlPlaneNodePoolConfigIn"] = t.struct(
        {"nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigIn"]).optional()}
    ).named(renames["BareMetalAdminControlPlaneNodePoolConfigIn"])
    types["BareMetalAdminControlPlaneNodePoolConfigOut"] = t.struct(
        {
            "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminControlPlaneNodePoolConfigOut"])
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
    types["BareMetalAdminLoadBalancerConfigIn"] = t.struct(
        {
            "manualLbConfig": t.proxy(
                renames["BareMetalAdminManualLbConfigIn"]
            ).optional(),
            "portConfig": t.proxy(renames["BareMetalAdminPortConfigIn"]).optional(),
            "vipConfig": t.proxy(renames["BareMetalAdminVipConfigIn"]).optional(),
        }
    ).named(renames["BareMetalAdminLoadBalancerConfigIn"])
    types["BareMetalAdminLoadBalancerConfigOut"] = t.struct(
        {
            "manualLbConfig": t.proxy(
                renames["BareMetalAdminManualLbConfigOut"]
            ).optional(),
            "portConfig": t.proxy(renames["BareMetalAdminPortConfigOut"]).optional(),
            "vipConfig": t.proxy(renames["BareMetalAdminVipConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminLoadBalancerConfigOut"])
    types["VmwareNodePoolIn"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "config": t.proxy(renames["VmwareNodeConfigIn"]),
            "displayName": t.string().optional(),
            "onPremVersion": t.string().optional(),
            "nodePoolAutoscaling": t.proxy(
                renames["VmwareNodePoolAutoscalingConfigIn"]
            ).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["VmwareNodePoolIn"])
    types["VmwareNodePoolOut"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "config": t.proxy(renames["VmwareNodeConfigOut"]),
            "uid": t.string().optional(),
            "deleteTime": t.string().optional(),
            "displayName": t.string().optional(),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "onPremVersion": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "nodePoolAutoscaling": t.proxy(
                renames["VmwareNodePoolAutoscalingConfigOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareNodePoolOut"])
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
    types["EnrollBareMetalNodePoolRequestIn"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "bareMetalNodePoolId": t.string().optional(),
        }
    ).named(renames["EnrollBareMetalNodePoolRequestIn"])
    types["EnrollBareMetalNodePoolRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "bareMetalNodePoolId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollBareMetalNodePoolRequestOut"])
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
    types["VmwareManualLbConfigIn"] = t.struct(
        {
            "ingressHttpsNodePort": t.integer().optional(),
            "konnectivityServerNodePort": t.integer().optional(),
            "controlPlaneNodePort": t.integer().optional(),
            "ingressHttpNodePort": t.integer().optional(),
        }
    ).named(renames["VmwareManualLbConfigIn"])
    types["VmwareManualLbConfigOut"] = t.struct(
        {
            "ingressHttpsNodePort": t.integer().optional(),
            "konnectivityServerNodePort": t.integer().optional(),
            "controlPlaneNodePort": t.integer().optional(),
            "ingressHttpNodePort": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareManualLbConfigOut"])
    types["BareMetalAdminClusterIn"] = t.struct(
        {
            "controlPlane": t.proxy(
                renames["BareMetalAdminControlPlaneConfigIn"]
            ).optional(),
            "etag": t.string().optional(),
            "bareMetalVersion": t.string().optional(),
            "storage": t.proxy(renames["BareMetalAdminStorageConfigIn"]).optional(),
            "clusterOperations": t.proxy(
                renames["BareMetalAdminClusterOperationsConfigIn"]
            ).optional(),
            "osEnvironmentConfig": t.proxy(
                renames["BareMetalAdminOsEnvironmentConfigIn"]
            ).optional(),
            "loadBalancer": t.proxy(
                renames["BareMetalAdminLoadBalancerConfigIn"]
            ).optional(),
            "proxy": t.proxy(renames["BareMetalAdminProxyConfigIn"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "securityConfig": t.proxy(
                renames["BareMetalAdminSecurityConfigIn"]
            ).optional(),
            "nodeAccessConfig": t.proxy(
                renames["BareMetalAdminNodeAccessConfigIn"]
            ).optional(),
            "maintenanceConfig": t.proxy(
                renames["BareMetalAdminMaintenanceConfigIn"]
            ).optional(),
            "networkConfig": t.proxy(
                renames["BareMetalAdminNetworkConfigIn"]
            ).optional(),
            "name": t.string().optional(),
            "nodeConfig": t.proxy(
                renames["BareMetalAdminWorkloadNodeConfigIn"]
            ).optional(),
        }
    ).named(renames["BareMetalAdminClusterIn"])
    types["BareMetalAdminClusterOut"] = t.struct(
        {
            "controlPlane": t.proxy(
                renames["BareMetalAdminControlPlaneConfigOut"]
            ).optional(),
            "validationCheck": t.proxy(renames["ValidationCheckOut"]).optional(),
            "etag": t.string().optional(),
            "state": t.string().optional(),
            "maintenanceStatus": t.proxy(
                renames["BareMetalAdminMaintenanceStatusOut"]
            ).optional(),
            "bareMetalVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "storage": t.proxy(renames["BareMetalAdminStorageConfigOut"]).optional(),
            "clusterOperations": t.proxy(
                renames["BareMetalAdminClusterOperationsConfigOut"]
            ).optional(),
            "osEnvironmentConfig": t.proxy(
                renames["BareMetalAdminOsEnvironmentConfigOut"]
            ).optional(),
            "loadBalancer": t.proxy(
                renames["BareMetalAdminLoadBalancerConfigOut"]
            ).optional(),
            "deleteTime": t.string().optional(),
            "proxy": t.proxy(renames["BareMetalAdminProxyConfigOut"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "securityConfig": t.proxy(
                renames["BareMetalAdminSecurityConfigOut"]
            ).optional(),
            "nodeAccessConfig": t.proxy(
                renames["BareMetalAdminNodeAccessConfigOut"]
            ).optional(),
            "maintenanceConfig": t.proxy(
                renames["BareMetalAdminMaintenanceConfigOut"]
            ).optional(),
            "localName": t.string().optional(),
            "networkConfig": t.proxy(
                renames["BareMetalAdminNetworkConfigOut"]
            ).optional(),
            "endpoint": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "fleet": t.proxy(renames["FleetOut"]).optional(),
            "nodeConfig": t.proxy(
                renames["BareMetalAdminWorkloadNodeConfigOut"]
            ).optional(),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "reconciling": t.boolean().optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminClusterOut"])
    types["BareMetalPortConfigIn"] = t.struct(
        {"controlPlaneLoadBalancerPort": t.integer().optional()}
    ).named(renames["BareMetalPortConfigIn"])
    types["BareMetalPortConfigOut"] = t.struct(
        {
            "controlPlaneLoadBalancerPort": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalPortConfigOut"])
    types["BareMetalSecurityConfigIn"] = t.struct(
        {"authorization": t.proxy(renames["AuthorizationIn"]).optional()}
    ).named(renames["BareMetalSecurityConfigIn"])
    types["BareMetalSecurityConfigOut"] = t.struct(
        {
            "authorization": t.proxy(renames["AuthorizationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalSecurityConfigOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["ValidationCheckResultIn"] = t.struct(
        {
            "details": t.string().optional(),
            "reason": t.string().optional(),
            "state": t.string().optional(),
            "category": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ValidationCheckResultIn"])
    types["ValidationCheckResultOut"] = t.struct(
        {
            "details": t.string().optional(),
            "reason": t.string().optional(),
            "state": t.string().optional(),
            "category": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationCheckResultOut"])
    types["BareMetalBgpLbConfigIn"] = t.struct(
        {
            "bgpPeerConfigs": t.array(t.proxy(renames["BareMetalBgpPeerConfigIn"])),
            "asn": t.string(),
            "addressPools": t.array(
                t.proxy(renames["BareMetalLoadBalancerAddressPoolIn"])
            ),
            "loadBalancerNodePoolConfig": t.proxy(
                renames["BareMetalLoadBalancerNodePoolConfigIn"]
            ).optional(),
        }
    ).named(renames["BareMetalBgpLbConfigIn"])
    types["BareMetalBgpLbConfigOut"] = t.struct(
        {
            "bgpPeerConfigs": t.array(t.proxy(renames["BareMetalBgpPeerConfigOut"])),
            "asn": t.string(),
            "addressPools": t.array(
                t.proxy(renames["BareMetalLoadBalancerAddressPoolOut"])
            ),
            "loadBalancerNodePoolConfig": t.proxy(
                renames["BareMetalLoadBalancerNodePoolConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalBgpLbConfigOut"])
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
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["ListVmwareNodePoolsResponseIn"] = t.struct(
        {
            "vmwareNodePools": t.array(t.proxy(renames["VmwareNodePoolIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListVmwareNodePoolsResponseIn"])
    types["ListVmwareNodePoolsResponseOut"] = t.struct(
        {
            "vmwareNodePools": t.array(
                t.proxy(renames["VmwareNodePoolOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVmwareNodePoolsResponseOut"])
    types["BareMetalLoadBalancerNodePoolConfigIn"] = t.struct(
        {"nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigIn"]).optional()}
    ).named(renames["BareMetalLoadBalancerNodePoolConfigIn"])
    types["BareMetalLoadBalancerNodePoolConfigOut"] = t.struct(
        {
            "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalLoadBalancerNodePoolConfigOut"])
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
    types["EnrollVmwareClusterRequestIn"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "adminClusterMembership": t.string(),
            "vmwareClusterId": t.string().optional(),
            "localName": t.string().optional(),
        }
    ).named(renames["EnrollVmwareClusterRequestIn"])
    types["EnrollVmwareClusterRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "adminClusterMembership": t.string(),
            "vmwareClusterId": t.string().optional(),
            "localName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollVmwareClusterRequestOut"])
    types["VmwareControlPlaneVsphereConfigIn"] = t.struct(
        {"datastore": t.string().optional()}
    ).named(renames["VmwareControlPlaneVsphereConfigIn"])
    types["VmwareControlPlaneVsphereConfigOut"] = t.struct(
        {
            "datastore": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareControlPlaneVsphereConfigOut"])
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
    types["BareMetalAdminClusterOperationsConfigIn"] = t.struct(
        {"enableApplicationLogs": t.boolean().optional()}
    ).named(renames["BareMetalAdminClusterOperationsConfigIn"])
    types["BareMetalAdminClusterOperationsConfigOut"] = t.struct(
        {
            "enableApplicationLogs": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminClusterOperationsConfigOut"])
    types["VmwareAdminManualLbConfigIn"] = t.struct(
        {
            "addonsNodePort": t.integer().optional(),
            "konnectivityServerNodePort": t.integer().optional(),
            "ingressHttpNodePort": t.integer().optional(),
            "controlPlaneNodePort": t.integer().optional(),
            "ingressHttpsNodePort": t.integer().optional(),
        }
    ).named(renames["VmwareAdminManualLbConfigIn"])
    types["VmwareAdminManualLbConfigOut"] = t.struct(
        {
            "addonsNodePort": t.integer().optional(),
            "konnectivityServerNodePort": t.integer().optional(),
            "ingressHttpNodePort": t.integer().optional(),
            "controlPlaneNodePort": t.integer().optional(),
            "ingressHttpsNodePort": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAdminManualLbConfigOut"])
    types["VmwareAAGConfigIn"] = t.struct(
        {"aagConfigDisabled": t.boolean().optional()}
    ).named(renames["VmwareAAGConfigIn"])
    types["VmwareAAGConfigOut"] = t.struct(
        {
            "aagConfigDisabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAAGConfigOut"])
    types["VmwareAddressPoolIn"] = t.struct(
        {
            "addresses": t.array(t.string()),
            "pool": t.string(),
            "avoidBuggyIps": t.boolean().optional(),
            "manualAssign": t.boolean().optional(),
        }
    ).named(renames["VmwareAddressPoolIn"])
    types["VmwareAddressPoolOut"] = t.struct(
        {
            "addresses": t.array(t.string()),
            "pool": t.string(),
            "avoidBuggyIps": t.boolean().optional(),
            "manualAssign": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAddressPoolOut"])
    types["VmwareAutoRepairConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["VmwareAutoRepairConfigIn"])
    types["VmwareAutoRepairConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAutoRepairConfigOut"])
    types["BareMetalBgpPeerConfigIn"] = t.struct(
        {
            "ipAddress": t.string(),
            "controlPlaneNodes": t.array(t.string()).optional(),
            "asn": t.string(),
        }
    ).named(renames["BareMetalBgpPeerConfigIn"])
    types["BareMetalBgpPeerConfigOut"] = t.struct(
        {
            "ipAddress": t.string(),
            "controlPlaneNodes": t.array(t.string()).optional(),
            "asn": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalBgpPeerConfigOut"])
    types["VmwareVCenterConfigIn"] = t.struct(
        {
            "address": t.string().optional(),
            "resourcePool": t.string().optional(),
            "folder": t.string().optional(),
            "datastore": t.string().optional(),
            "cluster": t.string().optional(),
            "datacenter": t.string().optional(),
            "caCertData": t.string().optional(),
        }
    ).named(renames["VmwareVCenterConfigIn"])
    types["VmwareVCenterConfigOut"] = t.struct(
        {
            "address": t.string().optional(),
            "resourcePool": t.string().optional(),
            "folder": t.string().optional(),
            "datastore": t.string().optional(),
            "cluster": t.string().optional(),
            "datacenter": t.string().optional(),
            "caCertData": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareVCenterConfigOut"])
    types["BareMetalAdminWorkloadNodeConfigIn"] = t.struct(
        {"maxPodsPerNode": t.string().optional()}
    ).named(renames["BareMetalAdminWorkloadNodeConfigIn"])
    types["BareMetalAdminWorkloadNodeConfigOut"] = t.struct(
        {
            "maxPodsPerNode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminWorkloadNodeConfigOut"])
    types["VmwareNodeConfigIn"] = t.struct(
        {
            "cpus": t.string().optional(),
            "taints": t.array(t.proxy(renames["NodeTaintIn"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "enableLoadBalancer": t.boolean().optional(),
            "memoryMb": t.string().optional(),
            "bootDiskSizeGb": t.string().optional(),
            "replicas": t.string().optional(),
            "image": t.string().optional(),
            "imageType": t.string(),
        }
    ).named(renames["VmwareNodeConfigIn"])
    types["VmwareNodeConfigOut"] = t.struct(
        {
            "cpus": t.string().optional(),
            "taints": t.array(t.proxy(renames["NodeTaintOut"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "enableLoadBalancer": t.boolean().optional(),
            "memoryMb": t.string().optional(),
            "bootDiskSizeGb": t.string().optional(),
            "replicas": t.string().optional(),
            "image": t.string().optional(),
            "imageType": t.string(),
            "vsphereConfig": t.proxy(renames["VmwareVsphereConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareNodeConfigOut"])
    types["VmwareAdminNetworkConfigIn"] = t.struct(
        {
            "staticIpConfig": t.proxy(renames["VmwareStaticIpConfigIn"]).optional(),
            "serviceAddressCidrBlocks": t.array(t.string()),
            "vcenterNetwork": t.string().optional(),
            "podAddressCidrBlocks": t.array(t.string()),
            "dhcpIpConfig": t.proxy(renames["VmwareDhcpIpConfigIn"]).optional(),
            "hostConfig": t.proxy(renames["VmwareHostConfigIn"]).optional(),
        }
    ).named(renames["VmwareAdminNetworkConfigIn"])
    types["VmwareAdminNetworkConfigOut"] = t.struct(
        {
            "staticIpConfig": t.proxy(renames["VmwareStaticIpConfigOut"]).optional(),
            "serviceAddressCidrBlocks": t.array(t.string()),
            "vcenterNetwork": t.string().optional(),
            "podAddressCidrBlocks": t.array(t.string()),
            "dhcpIpConfig": t.proxy(renames["VmwareDhcpIpConfigOut"]).optional(),
            "hostConfig": t.proxy(renames["VmwareHostConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAdminNetworkConfigOut"])
    types["BareMetalLvpShareConfigIn"] = t.struct(
        {
            "lvpConfig": t.proxy(renames["BareMetalLvpConfigIn"]),
            "sharedPathPvCount": t.integer().optional(),
        }
    ).named(renames["BareMetalLvpShareConfigIn"])
    types["BareMetalLvpShareConfigOut"] = t.struct(
        {
            "lvpConfig": t.proxy(renames["BareMetalLvpConfigOut"]),
            "sharedPathPvCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalLvpShareConfigOut"])
    types["BareMetalControlPlaneNodePoolConfigIn"] = t.struct(
        {"nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigIn"])}
    ).named(renames["BareMetalControlPlaneNodePoolConfigIn"])
    types["BareMetalControlPlaneNodePoolConfigOut"] = t.struct(
        {
            "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalControlPlaneNodePoolConfigOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["QueryBareMetalVersionConfigResponseIn"] = t.struct(
        {"versions": t.array(t.proxy(renames["BareMetalVersionInfoIn"])).optional()}
    ).named(renames["QueryBareMetalVersionConfigResponseIn"])
    types["QueryBareMetalVersionConfigResponseOut"] = t.struct(
        {
            "versions": t.array(t.proxy(renames["BareMetalVersionInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryBareMetalVersionConfigResponseOut"])
    types["VmwarePlatformConfigIn"] = t.struct(
        {"requiredPlatformVersion": t.string().optional()}
    ).named(renames["VmwarePlatformConfigIn"])
    types["VmwarePlatformConfigOut"] = t.struct(
        {
            "platformVersion": t.string().optional(),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "bundles": t.array(t.proxy(renames["VmwareBundleConfigOut"])).optional(),
            "requiredPlatformVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwarePlatformConfigOut"])
    types["BareMetalNodePoolIn"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "displayName": t.string().optional(),
            "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigIn"]),
            "name": t.string().optional(),
        }
    ).named(renames["BareMetalNodePoolIn"])
    types["BareMetalNodePoolOut"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "uid": t.string().optional(),
            "etag": t.string().optional(),
            "deleteTime": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "nodePoolConfig": t.proxy(renames["BareMetalNodePoolConfigOut"]),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "name": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalNodePoolOut"])
    types["BareMetalManualLbConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["BareMetalManualLbConfigIn"])
    types["BareMetalManualLbConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalManualLbConfigOut"])
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
    types["BareMetalAdminProxyConfigIn"] = t.struct(
        {"noProxy": t.array(t.string()).optional(), "uri": t.string()}
    ).named(renames["BareMetalAdminProxyConfigIn"])
    types["BareMetalAdminProxyConfigOut"] = t.struct(
        {
            "noProxy": t.array(t.string()).optional(),
            "uri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminProxyConfigOut"])
    types["EnrollBareMetalClusterRequestIn"] = t.struct(
        {
            "adminClusterMembership": t.string(),
            "bareMetalClusterId": t.string().optional(),
            "localName": t.string().optional(),
        }
    ).named(renames["EnrollBareMetalClusterRequestIn"])
    types["EnrollBareMetalClusterRequestOut"] = t.struct(
        {
            "adminClusterMembership": t.string(),
            "bareMetalClusterId": t.string().optional(),
            "localName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollBareMetalClusterRequestOut"])
    types["VmwareVsphereConfigIn"] = t.struct(
        {
            "tags": t.array(t.proxy(renames["VmwareVsphereTagIn"])).optional(),
            "datastore": t.string().optional(),
        }
    ).named(renames["VmwareVsphereConfigIn"])
    types["VmwareVsphereConfigOut"] = t.struct(
        {
            "tags": t.array(t.proxy(renames["VmwareVsphereTagOut"])).optional(),
            "datastore": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareVsphereConfigOut"])
    types["ResourceStatusIn"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "conditions": t.array(t.proxy(renames["ResourceConditionIn"])).optional(),
        }
    ).named(renames["ResourceStatusIn"])
    types["ResourceStatusOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "conditions": t.array(t.proxy(renames["ResourceConditionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceStatusOut"])
    types["BareMetalVersionInfoIn"] = t.struct(
        {"version": t.string().optional(), "hasDependencies": t.boolean().optional()}
    ).named(renames["BareMetalVersionInfoIn"])
    types["BareMetalVersionInfoOut"] = t.struct(
        {
            "version": t.string().optional(),
            "hasDependencies": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalVersionInfoOut"])
    types["ListBareMetalAdminClustersResponseIn"] = t.struct(
        {
            "bareMetalAdminClusters": t.array(
                t.proxy(renames["BareMetalAdminClusterIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListBareMetalAdminClustersResponseIn"])
    types["ListBareMetalAdminClustersResponseOut"] = t.struct(
        {
            "bareMetalAdminClusters": t.array(
                t.proxy(renames["BareMetalAdminClusterOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBareMetalAdminClustersResponseOut"])
    types["VmwareNodePoolAutoscalingConfigIn"] = t.struct(
        {"maxReplicas": t.integer().optional(), "minReplicas": t.integer().optional()}
    ).named(renames["VmwareNodePoolAutoscalingConfigIn"])
    types["VmwareNodePoolAutoscalingConfigOut"] = t.struct(
        {
            "maxReplicas": t.integer().optional(),
            "minReplicas": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareNodePoolAutoscalingConfigOut"])
    types["VmwareStorageConfigIn"] = t.struct(
        {"vsphereCsiDisabled": t.boolean().optional()}
    ).named(renames["VmwareStorageConfigIn"])
    types["VmwareStorageConfigOut"] = t.struct(
        {
            "vsphereCsiDisabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareStorageConfigOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["VmwareAdminLoadBalancerConfigIn"] = t.struct(
        {
            "metalLbConfig": t.proxy(renames["VmwareAdminMetalLbConfigIn"]).optional(),
            "f5Config": t.proxy(renames["VmwareAdminF5BigIpConfigIn"]).optional(),
            "manualLbConfig": t.proxy(
                renames["VmwareAdminManualLbConfigIn"]
            ).optional(),
            "vipConfig": t.proxy(renames["VmwareAdminVipConfigIn"]).optional(),
        }
    ).named(renames["VmwareAdminLoadBalancerConfigIn"])
    types["VmwareAdminLoadBalancerConfigOut"] = t.struct(
        {
            "metalLbConfig": t.proxy(renames["VmwareAdminMetalLbConfigOut"]).optional(),
            "f5Config": t.proxy(renames["VmwareAdminF5BigIpConfigOut"]).optional(),
            "manualLbConfig": t.proxy(
                renames["VmwareAdminManualLbConfigOut"]
            ).optional(),
            "vipConfig": t.proxy(renames["VmwareAdminVipConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAdminLoadBalancerConfigOut"])
    types["QueryVmwareVersionConfigResponseIn"] = t.struct(
        {"versions": t.array(t.proxy(renames["VmwareVersionInfoIn"])).optional()}
    ).named(renames["QueryVmwareVersionConfigResponseIn"])
    types["QueryVmwareVersionConfigResponseOut"] = t.struct(
        {
            "versions": t.array(t.proxy(renames["VmwareVersionInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryVmwareVersionConfigResponseOut"])
    types["ClusterUserIn"] = t.struct({"username": t.string()}).named(
        renames["ClusterUserIn"]
    )
    types["ClusterUserOut"] = t.struct(
        {"username": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ClusterUserOut"])
    types["AuthorizationIn"] = t.struct(
        {"adminUsers": t.array(t.proxy(renames["ClusterUserIn"]))}
    ).named(renames["AuthorizationIn"])
    types["AuthorizationOut"] = t.struct(
        {
            "adminUsers": t.array(t.proxy(renames["ClusterUserOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizationOut"])
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
    types["VmwareAutoResizeConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["VmwareAutoResizeConfigIn"])
    types["VmwareAutoResizeConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAutoResizeConfigOut"])
    types["BareMetalAdminPortConfigIn"] = t.struct(
        {"controlPlaneLoadBalancerPort": t.integer().optional()}
    ).named(renames["BareMetalAdminPortConfigIn"])
    types["BareMetalAdminPortConfigOut"] = t.struct(
        {
            "controlPlaneLoadBalancerPort": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminPortConfigOut"])
    types["BareMetalMultipleNetworkInterfacesConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["BareMetalMultipleNetworkInterfacesConfigIn"])
    types["BareMetalMultipleNetworkInterfacesConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalMultipleNetworkInterfacesConfigOut"])
    types["BareMetalNetworkConfigIn"] = t.struct(
        {
            "islandModeCidr": t.proxy(
                renames["BareMetalIslandModeCidrConfigIn"]
            ).optional(),
            "srIovConfig": t.proxy(renames["BareMetalSrIovConfigIn"]).optional(),
            "advancedNetworking": t.boolean().optional(),
            "multipleNetworkInterfacesConfig": t.proxy(
                renames["BareMetalMultipleNetworkInterfacesConfigIn"]
            ).optional(),
        }
    ).named(renames["BareMetalNetworkConfigIn"])
    types["BareMetalNetworkConfigOut"] = t.struct(
        {
            "islandModeCidr": t.proxy(
                renames["BareMetalIslandModeCidrConfigOut"]
            ).optional(),
            "srIovConfig": t.proxy(renames["BareMetalSrIovConfigOut"]).optional(),
            "advancedNetworking": t.boolean().optional(),
            "multipleNetworkInterfacesConfig": t.proxy(
                renames["BareMetalMultipleNetworkInterfacesConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalNetworkConfigOut"])
    types["BareMetalAdminOsEnvironmentConfigIn"] = t.struct(
        {"packageRepoExcluded": t.boolean().optional()}
    ).named(renames["BareMetalAdminOsEnvironmentConfigIn"])
    types["BareMetalAdminOsEnvironmentConfigOut"] = t.struct(
        {
            "packageRepoExcluded": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminOsEnvironmentConfigOut"])
    types["VmwareControlPlaneNodeConfigIn"] = t.struct(
        {
            "memory": t.string().optional(),
            "autoResizeConfig": t.proxy(renames["VmwareAutoResizeConfigIn"]).optional(),
            "cpus": t.string().optional(),
            "replicas": t.string().optional(),
        }
    ).named(renames["VmwareControlPlaneNodeConfigIn"])
    types["VmwareControlPlaneNodeConfigOut"] = t.struct(
        {
            "memory": t.string().optional(),
            "autoResizeConfig": t.proxy(
                renames["VmwareAutoResizeConfigOut"]
            ).optional(),
            "vsphereConfig": t.proxy(
                renames["VmwareControlPlaneVsphereConfigOut"]
            ).optional(),
            "cpus": t.string().optional(),
            "replicas": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareControlPlaneNodeConfigOut"])
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
    types["BareMetalClusterOperationsConfigIn"] = t.struct(
        {"enableApplicationLogs": t.boolean().optional()}
    ).named(renames["BareMetalClusterOperationsConfigIn"])
    types["BareMetalClusterOperationsConfigOut"] = t.struct(
        {
            "enableApplicationLogs": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalClusterOperationsConfigOut"])
    types["BareMetalMaintenanceConfigIn"] = t.struct(
        {"maintenanceAddressCidrBlocks": t.array(t.string())}
    ).named(renames["BareMetalMaintenanceConfigIn"])
    types["BareMetalMaintenanceConfigOut"] = t.struct(
        {
            "maintenanceAddressCidrBlocks": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalMaintenanceConfigOut"])
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
    types["VmwareDhcpIpConfigIn"] = t.struct({"enabled": t.boolean().optional()}).named(
        renames["VmwareDhcpIpConfigIn"]
    )
    types["VmwareDhcpIpConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareDhcpIpConfigOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["ListVmwareAdminClustersResponseIn"] = t.struct(
        {
            "vmwareAdminClusters": t.array(
                t.proxy(renames["VmwareAdminClusterIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListVmwareAdminClustersResponseIn"])
    types["ListVmwareAdminClustersResponseOut"] = t.struct(
        {
            "vmwareAdminClusters": t.array(
                t.proxy(renames["VmwareAdminClusterOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVmwareAdminClustersResponseOut"])
    types["BareMetalApiServerArgumentIn"] = t.struct(
        {"value": t.string(), "argument": t.string()}
    ).named(renames["BareMetalApiServerArgumentIn"])
    types["BareMetalApiServerArgumentOut"] = t.struct(
        {
            "value": t.string(),
            "argument": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalApiServerArgumentOut"])
    types["BareMetalNodeAccessConfigIn"] = t.struct(
        {"loginUser": t.string().optional()}
    ).named(renames["BareMetalNodeAccessConfigIn"])
    types["BareMetalNodeAccessConfigOut"] = t.struct(
        {
            "loginUser": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalNodeAccessConfigOut"])
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
    types["VmwareStaticIpConfigIn"] = t.struct(
        {"ipBlocks": t.array(t.proxy(renames["VmwareIpBlockIn"])).optional()}
    ).named(renames["VmwareStaticIpConfigIn"])
    types["VmwareStaticIpConfigOut"] = t.struct(
        {
            "ipBlocks": t.array(t.proxy(renames["VmwareIpBlockOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareStaticIpConfigOut"])
    types["VmwareAdminF5BigIpConfigIn"] = t.struct(
        {
            "snatPool": t.string().optional(),
            "address": t.string().optional(),
            "partition": t.string().optional(),
        }
    ).named(renames["VmwareAdminF5BigIpConfigIn"])
    types["VmwareAdminF5BigIpConfigOut"] = t.struct(
        {
            "snatPool": t.string().optional(),
            "address": t.string().optional(),
            "partition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAdminF5BigIpConfigOut"])
    types["VmwareAdminClusterIn"] = t.struct(
        {
            "controlPlaneNode": t.proxy(
                renames["VmwareAdminControlPlaneNodeConfigIn"]
            ).optional(),
            "onPremVersion": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
            "networkConfig": t.proxy(renames["VmwareAdminNetworkConfigIn"]).optional(),
            "etag": t.string().optional(),
            "description": t.string().optional(),
            "vcenter": t.proxy(renames["VmwareAdminVCenterConfigIn"]).optional(),
            "autoRepairConfig": t.proxy(renames["VmwareAutoRepairConfigIn"]).optional(),
            "addonNode": t.proxy(renames["VmwareAdminAddonNodeConfigIn"]).optional(),
            "name": t.string().optional(),
            "platformConfig": t.proxy(renames["VmwarePlatformConfigIn"]).optional(),
            "imageType": t.string().optional(),
            "bootstrapClusterMembership": t.string().optional(),
            "loadBalancer": t.proxy(
                renames["VmwareAdminLoadBalancerConfigIn"]
            ).optional(),
        }
    ).named(renames["VmwareAdminClusterIn"])
    types["VmwareAdminClusterOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "controlPlaneNode": t.proxy(
                renames["VmwareAdminControlPlaneNodeConfigOut"]
            ).optional(),
            "onPremVersion": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigOut"]).optional(),
            "networkConfig": t.proxy(renames["VmwareAdminNetworkConfigOut"]).optional(),
            "etag": t.string().optional(),
            "description": t.string().optional(),
            "endpoint": t.string().optional(),
            "vcenter": t.proxy(renames["VmwareAdminVCenterConfigOut"]).optional(),
            "autoRepairConfig": t.proxy(
                renames["VmwareAutoRepairConfigOut"]
            ).optional(),
            "fleet": t.proxy(renames["FleetOut"]).optional(),
            "updateTime": t.string().optional(),
            "addonNode": t.proxy(renames["VmwareAdminAddonNodeConfigOut"]).optional(),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "name": t.string().optional(),
            "localName": t.string().optional(),
            "platformConfig": t.proxy(renames["VmwarePlatformConfigOut"]).optional(),
            "imageType": t.string().optional(),
            "uid": t.string().optional(),
            "bootstrapClusterMembership": t.string().optional(),
            "loadBalancer": t.proxy(
                renames["VmwareAdminLoadBalancerConfigOut"]
            ).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareAdminClusterOut"])
    types["BareMetalAdminMaintenanceConfigIn"] = t.struct(
        {"maintenanceAddressCidrBlocks": t.array(t.string())}
    ).named(renames["BareMetalAdminMaintenanceConfigIn"])
    types["BareMetalAdminMaintenanceConfigOut"] = t.struct(
        {
            "maintenanceAddressCidrBlocks": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalAdminMaintenanceConfigOut"])
    types["BareMetalSrIovConfigIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["BareMetalSrIovConfigIn"])
    types["BareMetalSrIovConfigOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalSrIovConfigOut"])
    types["VmwareClusterIn"] = t.struct(
        {
            "controlPlaneNode": t.proxy(
                renames["VmwareControlPlaneNodeConfigIn"]
            ).optional(),
            "etag": t.string().optional(),
            "authorization": t.proxy(renames["AuthorizationIn"]).optional(),
            "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigIn"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "onPremVersion": t.string().optional(),
            "adminClusterMembership": t.string(),
            "vmTrackingEnabled": t.boolean().optional(),
            "autoRepairConfig": t.proxy(renames["VmwareAutoRepairConfigIn"]).optional(),
            "loadBalancer": t.proxy(renames["VmwareLoadBalancerConfigIn"]).optional(),
            "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "enableControlPlaneV2": t.boolean().optional(),
            "storage": t.proxy(renames["VmwareStorageConfigIn"]).optional(),
            "networkConfig": t.proxy(renames["VmwareNetworkConfigIn"]).optional(),
        }
    ).named(renames["VmwareClusterIn"])
    types["VmwareClusterOut"] = t.struct(
        {
            "controlPlaneNode": t.proxy(
                renames["VmwareControlPlaneNodeConfigOut"]
            ).optional(),
            "etag": t.string().optional(),
            "validationCheck": t.proxy(renames["ValidationCheckOut"]).optional(),
            "authorization": t.proxy(renames["AuthorizationOut"]).optional(),
            "reconciling": t.boolean().optional(),
            "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigOut"]).optional(),
            "uid": t.string().optional(),
            "vcenter": t.proxy(renames["VmwareVCenterConfigOut"]).optional(),
            "status": t.proxy(renames["ResourceStatusOut"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "endpoint": t.string().optional(),
            "onPremVersion": t.string().optional(),
            "deleteTime": t.string().optional(),
            "adminClusterName": t.string().optional(),
            "adminClusterMembership": t.string(),
            "vmTrackingEnabled": t.boolean().optional(),
            "autoRepairConfig": t.proxy(
                renames["VmwareAutoRepairConfigOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "loadBalancer": t.proxy(renames["VmwareLoadBalancerConfigOut"]).optional(),
            "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigOut"]).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "enableControlPlaneV2": t.boolean().optional(),
            "localName": t.string().optional(),
            "state": t.string().optional(),
            "storage": t.proxy(renames["VmwareStorageConfigOut"]).optional(),
            "fleet": t.proxy(renames["FleetOut"]).optional(),
            "networkConfig": t.proxy(renames["VmwareNetworkConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareClusterOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["BareMetalOsEnvironmentConfigIn"] = t.struct(
        {"packageRepoExcluded": t.boolean().optional()}
    ).named(renames["BareMetalOsEnvironmentConfigIn"])
    types["BareMetalOsEnvironmentConfigOut"] = t.struct(
        {
            "packageRepoExcluded": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BareMetalOsEnvironmentConfigOut"])
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
    types["ListVmwareClustersResponseIn"] = t.struct(
        {
            "vmwareClusters": t.array(t.proxy(renames["VmwareClusterIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListVmwareClustersResponseIn"])
    types["ListVmwareClustersResponseOut"] = t.struct(
        {
            "vmwareClusters": t.array(t.proxy(renames["VmwareClusterOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVmwareClustersResponseOut"])

    functions = {}
    functions["projectsLocationsGet"] = gkeonprem.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
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
                "controlPlane": t.proxy(
                    renames["BareMetalAdminControlPlaneConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "bareMetalVersion": t.string().optional(),
                "storage": t.proxy(renames["BareMetalAdminStorageConfigIn"]).optional(),
                "clusterOperations": t.proxy(
                    renames["BareMetalAdminClusterOperationsConfigIn"]
                ).optional(),
                "osEnvironmentConfig": t.proxy(
                    renames["BareMetalAdminOsEnvironmentConfigIn"]
                ).optional(),
                "loadBalancer": t.proxy(
                    renames["BareMetalAdminLoadBalancerConfigIn"]
                ).optional(),
                "proxy": t.proxy(renames["BareMetalAdminProxyConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "securityConfig": t.proxy(
                    renames["BareMetalAdminSecurityConfigIn"]
                ).optional(),
                "nodeAccessConfig": t.proxy(
                    renames["BareMetalAdminNodeAccessConfigIn"]
                ).optional(),
                "maintenanceConfig": t.proxy(
                    renames["BareMetalAdminMaintenanceConfigIn"]
                ).optional(),
                "networkConfig": t.proxy(
                    renames["BareMetalAdminNetworkConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "nodeConfig": t.proxy(
                    renames["BareMetalAdminWorkloadNodeConfigIn"]
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
                "controlPlane": t.proxy(
                    renames["BareMetalAdminControlPlaneConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "bareMetalVersion": t.string().optional(),
                "storage": t.proxy(renames["BareMetalAdminStorageConfigIn"]).optional(),
                "clusterOperations": t.proxy(
                    renames["BareMetalAdminClusterOperationsConfigIn"]
                ).optional(),
                "osEnvironmentConfig": t.proxy(
                    renames["BareMetalAdminOsEnvironmentConfigIn"]
                ).optional(),
                "loadBalancer": t.proxy(
                    renames["BareMetalAdminLoadBalancerConfigIn"]
                ).optional(),
                "proxy": t.proxy(renames["BareMetalAdminProxyConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "securityConfig": t.proxy(
                    renames["BareMetalAdminSecurityConfigIn"]
                ).optional(),
                "nodeAccessConfig": t.proxy(
                    renames["BareMetalAdminNodeAccessConfigIn"]
                ).optional(),
                "maintenanceConfig": t.proxy(
                    renames["BareMetalAdminMaintenanceConfigIn"]
                ).optional(),
                "networkConfig": t.proxy(
                    renames["BareMetalAdminNetworkConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "nodeConfig": t.proxy(
                    renames["BareMetalAdminWorkloadNodeConfigIn"]
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
                "controlPlane": t.proxy(
                    renames["BareMetalAdminControlPlaneConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "bareMetalVersion": t.string().optional(),
                "storage": t.proxy(renames["BareMetalAdminStorageConfigIn"]).optional(),
                "clusterOperations": t.proxy(
                    renames["BareMetalAdminClusterOperationsConfigIn"]
                ).optional(),
                "osEnvironmentConfig": t.proxy(
                    renames["BareMetalAdminOsEnvironmentConfigIn"]
                ).optional(),
                "loadBalancer": t.proxy(
                    renames["BareMetalAdminLoadBalancerConfigIn"]
                ).optional(),
                "proxy": t.proxy(renames["BareMetalAdminProxyConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "securityConfig": t.proxy(
                    renames["BareMetalAdminSecurityConfigIn"]
                ).optional(),
                "nodeAccessConfig": t.proxy(
                    renames["BareMetalAdminNodeAccessConfigIn"]
                ).optional(),
                "maintenanceConfig": t.proxy(
                    renames["BareMetalAdminMaintenanceConfigIn"]
                ).optional(),
                "networkConfig": t.proxy(
                    renames["BareMetalAdminNetworkConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "nodeConfig": t.proxy(
                    renames["BareMetalAdminWorkloadNodeConfigIn"]
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
                "controlPlane": t.proxy(
                    renames["BareMetalAdminControlPlaneConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "bareMetalVersion": t.string().optional(),
                "storage": t.proxy(renames["BareMetalAdminStorageConfigIn"]).optional(),
                "clusterOperations": t.proxy(
                    renames["BareMetalAdminClusterOperationsConfigIn"]
                ).optional(),
                "osEnvironmentConfig": t.proxy(
                    renames["BareMetalAdminOsEnvironmentConfigIn"]
                ).optional(),
                "loadBalancer": t.proxy(
                    renames["BareMetalAdminLoadBalancerConfigIn"]
                ).optional(),
                "proxy": t.proxy(renames["BareMetalAdminProxyConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "securityConfig": t.proxy(
                    renames["BareMetalAdminSecurityConfigIn"]
                ).optional(),
                "nodeAccessConfig": t.proxy(
                    renames["BareMetalAdminNodeAccessConfigIn"]
                ).optional(),
                "maintenanceConfig": t.proxy(
                    renames["BareMetalAdminMaintenanceConfigIn"]
                ).optional(),
                "networkConfig": t.proxy(
                    renames["BareMetalAdminNetworkConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "nodeConfig": t.proxy(
                    renames["BareMetalAdminWorkloadNodeConfigIn"]
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
                "controlPlane": t.proxy(
                    renames["BareMetalAdminControlPlaneConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "bareMetalVersion": t.string().optional(),
                "storage": t.proxy(renames["BareMetalAdminStorageConfigIn"]).optional(),
                "clusterOperations": t.proxy(
                    renames["BareMetalAdminClusterOperationsConfigIn"]
                ).optional(),
                "osEnvironmentConfig": t.proxy(
                    renames["BareMetalAdminOsEnvironmentConfigIn"]
                ).optional(),
                "loadBalancer": t.proxy(
                    renames["BareMetalAdminLoadBalancerConfigIn"]
                ).optional(),
                "proxy": t.proxy(renames["BareMetalAdminProxyConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "securityConfig": t.proxy(
                    renames["BareMetalAdminSecurityConfigIn"]
                ).optional(),
                "nodeAccessConfig": t.proxy(
                    renames["BareMetalAdminNodeAccessConfigIn"]
                ).optional(),
                "maintenanceConfig": t.proxy(
                    renames["BareMetalAdminMaintenanceConfigIn"]
                ).optional(),
                "networkConfig": t.proxy(
                    renames["BareMetalAdminNetworkConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "nodeConfig": t.proxy(
                    renames["BareMetalAdminWorkloadNodeConfigIn"]
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
                "controlPlane": t.proxy(
                    renames["BareMetalAdminControlPlaneConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "bareMetalVersion": t.string().optional(),
                "storage": t.proxy(renames["BareMetalAdminStorageConfigIn"]).optional(),
                "clusterOperations": t.proxy(
                    renames["BareMetalAdminClusterOperationsConfigIn"]
                ).optional(),
                "osEnvironmentConfig": t.proxy(
                    renames["BareMetalAdminOsEnvironmentConfigIn"]
                ).optional(),
                "loadBalancer": t.proxy(
                    renames["BareMetalAdminLoadBalancerConfigIn"]
                ).optional(),
                "proxy": t.proxy(renames["BareMetalAdminProxyConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "securityConfig": t.proxy(
                    renames["BareMetalAdminSecurityConfigIn"]
                ).optional(),
                "nodeAccessConfig": t.proxy(
                    renames["BareMetalAdminNodeAccessConfigIn"]
                ).optional(),
                "maintenanceConfig": t.proxy(
                    renames["BareMetalAdminMaintenanceConfigIn"]
                ).optional(),
                "networkConfig": t.proxy(
                    renames["BareMetalAdminNetworkConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "nodeConfig": t.proxy(
                    renames["BareMetalAdminWorkloadNodeConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
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
                "controlPlane": t.proxy(
                    renames["BareMetalAdminControlPlaneConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "bareMetalVersion": t.string().optional(),
                "storage": t.proxy(renames["BareMetalAdminStorageConfigIn"]).optional(),
                "clusterOperations": t.proxy(
                    renames["BareMetalAdminClusterOperationsConfigIn"]
                ).optional(),
                "osEnvironmentConfig": t.proxy(
                    renames["BareMetalAdminOsEnvironmentConfigIn"]
                ).optional(),
                "loadBalancer": t.proxy(
                    renames["BareMetalAdminLoadBalancerConfigIn"]
                ).optional(),
                "proxy": t.proxy(renames["BareMetalAdminProxyConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "securityConfig": t.proxy(
                    renames["BareMetalAdminSecurityConfigIn"]
                ).optional(),
                "nodeAccessConfig": t.proxy(
                    renames["BareMetalAdminNodeAccessConfigIn"]
                ).optional(),
                "maintenanceConfig": t.proxy(
                    renames["BareMetalAdminMaintenanceConfigIn"]
                ).optional(),
                "networkConfig": t.proxy(
                    renames["BareMetalAdminNetworkConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "nodeConfig": t.proxy(
                    renames["BareMetalAdminWorkloadNodeConfigIn"]
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
                "controlPlane": t.proxy(
                    renames["BareMetalAdminControlPlaneConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "bareMetalVersion": t.string().optional(),
                "storage": t.proxy(renames["BareMetalAdminStorageConfigIn"]).optional(),
                "clusterOperations": t.proxy(
                    renames["BareMetalAdminClusterOperationsConfigIn"]
                ).optional(),
                "osEnvironmentConfig": t.proxy(
                    renames["BareMetalAdminOsEnvironmentConfigIn"]
                ).optional(),
                "loadBalancer": t.proxy(
                    renames["BareMetalAdminLoadBalancerConfigIn"]
                ).optional(),
                "proxy": t.proxy(renames["BareMetalAdminProxyConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "securityConfig": t.proxy(
                    renames["BareMetalAdminSecurityConfigIn"]
                ).optional(),
                "nodeAccessConfig": t.proxy(
                    renames["BareMetalAdminNodeAccessConfigIn"]
                ).optional(),
                "maintenanceConfig": t.proxy(
                    renames["BareMetalAdminMaintenanceConfigIn"]
                ).optional(),
                "networkConfig": t.proxy(
                    renames["BareMetalAdminNetworkConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "nodeConfig": t.proxy(
                    renames["BareMetalAdminWorkloadNodeConfigIn"]
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
                "controlPlane": t.proxy(
                    renames["BareMetalAdminControlPlaneConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "bareMetalVersion": t.string().optional(),
                "storage": t.proxy(renames["BareMetalAdminStorageConfigIn"]).optional(),
                "clusterOperations": t.proxy(
                    renames["BareMetalAdminClusterOperationsConfigIn"]
                ).optional(),
                "osEnvironmentConfig": t.proxy(
                    renames["BareMetalAdminOsEnvironmentConfigIn"]
                ).optional(),
                "loadBalancer": t.proxy(
                    renames["BareMetalAdminLoadBalancerConfigIn"]
                ).optional(),
                "proxy": t.proxy(renames["BareMetalAdminProxyConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "securityConfig": t.proxy(
                    renames["BareMetalAdminSecurityConfigIn"]
                ).optional(),
                "nodeAccessConfig": t.proxy(
                    renames["BareMetalAdminNodeAccessConfigIn"]
                ).optional(),
                "maintenanceConfig": t.proxy(
                    renames["BareMetalAdminMaintenanceConfigIn"]
                ).optional(),
                "networkConfig": t.proxy(
                    renames["BareMetalAdminNetworkConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "nodeConfig": t.proxy(
                    renames["BareMetalAdminWorkloadNodeConfigIn"]
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
                "controlPlane": t.proxy(
                    renames["BareMetalAdminControlPlaneConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "bareMetalVersion": t.string().optional(),
                "storage": t.proxy(renames["BareMetalAdminStorageConfigIn"]).optional(),
                "clusterOperations": t.proxy(
                    renames["BareMetalAdminClusterOperationsConfigIn"]
                ).optional(),
                "osEnvironmentConfig": t.proxy(
                    renames["BareMetalAdminOsEnvironmentConfigIn"]
                ).optional(),
                "loadBalancer": t.proxy(
                    renames["BareMetalAdminLoadBalancerConfigIn"]
                ).optional(),
                "proxy": t.proxy(renames["BareMetalAdminProxyConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "securityConfig": t.proxy(
                    renames["BareMetalAdminSecurityConfigIn"]
                ).optional(),
                "nodeAccessConfig": t.proxy(
                    renames["BareMetalAdminNodeAccessConfigIn"]
                ).optional(),
                "maintenanceConfig": t.proxy(
                    renames["BareMetalAdminMaintenanceConfigIn"]
                ).optional(),
                "networkConfig": t.proxy(
                    renames["BareMetalAdminNetworkConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "nodeConfig": t.proxy(
                    renames["BareMetalAdminWorkloadNodeConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalAdminClustersOperationsList"] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalAdminClustersOperationsGet"] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersCreate"] = gkeonprem.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "validateOnly": t.boolean().optional(),
                "controlPlaneNode": t.proxy(
                    renames["VmwareControlPlaneNodeConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "authorization": t.proxy(renames["AuthorizationIn"]).optional(),
                "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "onPremVersion": t.string().optional(),
                "adminClusterMembership": t.string(),
                "vmTrackingEnabled": t.boolean().optional(),
                "autoRepairConfig": t.proxy(
                    renames["VmwareAutoRepairConfigIn"]
                ).optional(),
                "loadBalancer": t.proxy(
                    renames["VmwareLoadBalancerConfigIn"]
                ).optional(),
                "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
                "description": t.string().optional(),
                "enableControlPlaneV2": t.boolean().optional(),
                "storage": t.proxy(renames["VmwareStorageConfigIn"]).optional(),
                "networkConfig": t.proxy(renames["VmwareNetworkConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersGetIamPolicy"] = gkeonprem.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "validateOnly": t.boolean().optional(),
                "controlPlaneNode": t.proxy(
                    renames["VmwareControlPlaneNodeConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "authorization": t.proxy(renames["AuthorizationIn"]).optional(),
                "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "onPremVersion": t.string().optional(),
                "adminClusterMembership": t.string(),
                "vmTrackingEnabled": t.boolean().optional(),
                "autoRepairConfig": t.proxy(
                    renames["VmwareAutoRepairConfigIn"]
                ).optional(),
                "loadBalancer": t.proxy(
                    renames["VmwareLoadBalancerConfigIn"]
                ).optional(),
                "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
                "description": t.string().optional(),
                "enableControlPlaneV2": t.boolean().optional(),
                "storage": t.proxy(renames["VmwareStorageConfigIn"]).optional(),
                "networkConfig": t.proxy(renames["VmwareNetworkConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersSetIamPolicy"] = gkeonprem.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "validateOnly": t.boolean().optional(),
                "controlPlaneNode": t.proxy(
                    renames["VmwareControlPlaneNodeConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "authorization": t.proxy(renames["AuthorizationIn"]).optional(),
                "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "onPremVersion": t.string().optional(),
                "adminClusterMembership": t.string(),
                "vmTrackingEnabled": t.boolean().optional(),
                "autoRepairConfig": t.proxy(
                    renames["VmwareAutoRepairConfigIn"]
                ).optional(),
                "loadBalancer": t.proxy(
                    renames["VmwareLoadBalancerConfigIn"]
                ).optional(),
                "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
                "description": t.string().optional(),
                "enableControlPlaneV2": t.boolean().optional(),
                "storage": t.proxy(renames["VmwareStorageConfigIn"]).optional(),
                "networkConfig": t.proxy(renames["VmwareNetworkConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersEnroll"] = gkeonprem.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "validateOnly": t.boolean().optional(),
                "controlPlaneNode": t.proxy(
                    renames["VmwareControlPlaneNodeConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "authorization": t.proxy(renames["AuthorizationIn"]).optional(),
                "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "onPremVersion": t.string().optional(),
                "adminClusterMembership": t.string(),
                "vmTrackingEnabled": t.boolean().optional(),
                "autoRepairConfig": t.proxy(
                    renames["VmwareAutoRepairConfigIn"]
                ).optional(),
                "loadBalancer": t.proxy(
                    renames["VmwareLoadBalancerConfigIn"]
                ).optional(),
                "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
                "description": t.string().optional(),
                "enableControlPlaneV2": t.boolean().optional(),
                "storage": t.proxy(renames["VmwareStorageConfigIn"]).optional(),
                "networkConfig": t.proxy(renames["VmwareNetworkConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersTestIamPermissions"] = gkeonprem.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "validateOnly": t.boolean().optional(),
                "controlPlaneNode": t.proxy(
                    renames["VmwareControlPlaneNodeConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "authorization": t.proxy(renames["AuthorizationIn"]).optional(),
                "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "onPremVersion": t.string().optional(),
                "adminClusterMembership": t.string(),
                "vmTrackingEnabled": t.boolean().optional(),
                "autoRepairConfig": t.proxy(
                    renames["VmwareAutoRepairConfigIn"]
                ).optional(),
                "loadBalancer": t.proxy(
                    renames["VmwareLoadBalancerConfigIn"]
                ).optional(),
                "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
                "description": t.string().optional(),
                "enableControlPlaneV2": t.boolean().optional(),
                "storage": t.proxy(renames["VmwareStorageConfigIn"]).optional(),
                "networkConfig": t.proxy(renames["VmwareNetworkConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersDelete"] = gkeonprem.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "validateOnly": t.boolean().optional(),
                "controlPlaneNode": t.proxy(
                    renames["VmwareControlPlaneNodeConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "authorization": t.proxy(renames["AuthorizationIn"]).optional(),
                "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "onPremVersion": t.string().optional(),
                "adminClusterMembership": t.string(),
                "vmTrackingEnabled": t.boolean().optional(),
                "autoRepairConfig": t.proxy(
                    renames["VmwareAutoRepairConfigIn"]
                ).optional(),
                "loadBalancer": t.proxy(
                    renames["VmwareLoadBalancerConfigIn"]
                ).optional(),
                "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
                "description": t.string().optional(),
                "enableControlPlaneV2": t.boolean().optional(),
                "storage": t.proxy(renames["VmwareStorageConfigIn"]).optional(),
                "networkConfig": t.proxy(renames["VmwareNetworkConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersQueryVersionConfig"] = gkeonprem.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "validateOnly": t.boolean().optional(),
                "controlPlaneNode": t.proxy(
                    renames["VmwareControlPlaneNodeConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "authorization": t.proxy(renames["AuthorizationIn"]).optional(),
                "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "onPremVersion": t.string().optional(),
                "adminClusterMembership": t.string(),
                "vmTrackingEnabled": t.boolean().optional(),
                "autoRepairConfig": t.proxy(
                    renames["VmwareAutoRepairConfigIn"]
                ).optional(),
                "loadBalancer": t.proxy(
                    renames["VmwareLoadBalancerConfigIn"]
                ).optional(),
                "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
                "description": t.string().optional(),
                "enableControlPlaneV2": t.boolean().optional(),
                "storage": t.proxy(renames["VmwareStorageConfigIn"]).optional(),
                "networkConfig": t.proxy(renames["VmwareNetworkConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersList"] = gkeonprem.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "validateOnly": t.boolean().optional(),
                "controlPlaneNode": t.proxy(
                    renames["VmwareControlPlaneNodeConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "authorization": t.proxy(renames["AuthorizationIn"]).optional(),
                "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "onPremVersion": t.string().optional(),
                "adminClusterMembership": t.string(),
                "vmTrackingEnabled": t.boolean().optional(),
                "autoRepairConfig": t.proxy(
                    renames["VmwareAutoRepairConfigIn"]
                ).optional(),
                "loadBalancer": t.proxy(
                    renames["VmwareLoadBalancerConfigIn"]
                ).optional(),
                "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
                "description": t.string().optional(),
                "enableControlPlaneV2": t.boolean().optional(),
                "storage": t.proxy(renames["VmwareStorageConfigIn"]).optional(),
                "networkConfig": t.proxy(renames["VmwareNetworkConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersUnenroll"] = gkeonprem.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "validateOnly": t.boolean().optional(),
                "controlPlaneNode": t.proxy(
                    renames["VmwareControlPlaneNodeConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "authorization": t.proxy(renames["AuthorizationIn"]).optional(),
                "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "onPremVersion": t.string().optional(),
                "adminClusterMembership": t.string(),
                "vmTrackingEnabled": t.boolean().optional(),
                "autoRepairConfig": t.proxy(
                    renames["VmwareAutoRepairConfigIn"]
                ).optional(),
                "loadBalancer": t.proxy(
                    renames["VmwareLoadBalancerConfigIn"]
                ).optional(),
                "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
                "description": t.string().optional(),
                "enableControlPlaneV2": t.boolean().optional(),
                "storage": t.proxy(renames["VmwareStorageConfigIn"]).optional(),
                "networkConfig": t.proxy(renames["VmwareNetworkConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersGet"] = gkeonprem.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "validateOnly": t.boolean().optional(),
                "controlPlaneNode": t.proxy(
                    renames["VmwareControlPlaneNodeConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "authorization": t.proxy(renames["AuthorizationIn"]).optional(),
                "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "onPremVersion": t.string().optional(),
                "adminClusterMembership": t.string(),
                "vmTrackingEnabled": t.boolean().optional(),
                "autoRepairConfig": t.proxy(
                    renames["VmwareAutoRepairConfigIn"]
                ).optional(),
                "loadBalancer": t.proxy(
                    renames["VmwareLoadBalancerConfigIn"]
                ).optional(),
                "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
                "description": t.string().optional(),
                "enableControlPlaneV2": t.boolean().optional(),
                "storage": t.proxy(renames["VmwareStorageConfigIn"]).optional(),
                "networkConfig": t.proxy(renames["VmwareNetworkConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersPatch"] = gkeonprem.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "validateOnly": t.boolean().optional(),
                "controlPlaneNode": t.proxy(
                    renames["VmwareControlPlaneNodeConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "authorization": t.proxy(renames["AuthorizationIn"]).optional(),
                "dataplaneV2": t.proxy(renames["VmwareDataplaneV2ConfigIn"]).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "onPremVersion": t.string().optional(),
                "adminClusterMembership": t.string(),
                "vmTrackingEnabled": t.boolean().optional(),
                "autoRepairConfig": t.proxy(
                    renames["VmwareAutoRepairConfigIn"]
                ).optional(),
                "loadBalancer": t.proxy(
                    renames["VmwareLoadBalancerConfigIn"]
                ).optional(),
                "antiAffinityGroups": t.proxy(renames["VmwareAAGConfigIn"]).optional(),
                "description": t.string().optional(),
                "enableControlPlaneV2": t.boolean().optional(),
                "storage": t.proxy(renames["VmwareStorageConfigIn"]).optional(),
                "networkConfig": t.proxy(renames["VmwareNetworkConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsVmwareClustersVmwareNodePoolsDelete"
    ] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersVmwareNodePoolsGet"] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsVmwareClustersVmwareNodePoolsCreate"
    ] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsVmwareClustersVmwareNodePoolsSetIamPolicy"
    ] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersVmwareNodePoolsPatch"] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsVmwareClustersVmwareNodePoolsEnroll"
    ] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersVmwareNodePoolsList"] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsVmwareClustersVmwareNodePoolsTestIamPermissions"
    ] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsVmwareClustersVmwareNodePoolsGetIamPolicy"
    ] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsVmwareClustersVmwareNodePoolsUnenroll"
    ] = gkeonprem.delete(
        "v1/{name}:unenroll",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsVmwareClustersVmwareNodePoolsOperationsGet"
    ] = gkeonprem.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsVmwareClustersVmwareNodePoolsOperationsList"
    ] = gkeonprem.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersOperationsGet"] = gkeonprem.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareClustersOperationsList"] = gkeonprem.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareAdminClustersUnenroll"] = gkeonprem.get(
        "v1/{parent}/vmwareAdminClusters",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVmwareAdminClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareAdminClustersEnroll"] = gkeonprem.get(
        "v1/{parent}/vmwareAdminClusters",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVmwareAdminClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareAdminClustersPatch"] = gkeonprem.get(
        "v1/{parent}/vmwareAdminClusters",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVmwareAdminClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareAdminClustersGet"] = gkeonprem.get(
        "v1/{parent}/vmwareAdminClusters",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVmwareAdminClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareAdminClustersGetIamPolicy"] = gkeonprem.get(
        "v1/{parent}/vmwareAdminClusters",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVmwareAdminClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareAdminClustersSetIamPolicy"] = gkeonprem.get(
        "v1/{parent}/vmwareAdminClusters",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVmwareAdminClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareAdminClustersTestIamPermissions"] = gkeonprem.get(
        "v1/{parent}/vmwareAdminClusters",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVmwareAdminClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareAdminClustersList"] = gkeonprem.get(
        "v1/{parent}/vmwareAdminClusters",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVmwareAdminClustersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareAdminClustersOperationsGet"] = gkeonprem.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVmwareAdminClustersOperationsList"] = gkeonprem.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersPatch"] = gkeonprem.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersUnenroll"] = gkeonprem.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersEnroll"] = gkeonprem.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersList"] = gkeonprem.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersGet"] = gkeonprem.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersCreate"] = gkeonprem.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersQueryVersionConfig"] = gkeonprem.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersDelete"] = gkeonprem.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersSetIamPolicy"] = gkeonprem.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersTestIamPermissions"] = gkeonprem.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersGetIamPolicy"] = gkeonprem.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersOperationsList"] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBareMetalClustersOperationsGet"] = gkeonprem.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsList"
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
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsEnroll"
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
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsCreate"
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
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsDelete"
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
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsPatch"
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
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsGetIamPolicy"
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
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsGet"
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
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsSetIamPolicy"
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
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsUnenroll"
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
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsTestIamPermissions"
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
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsOperationsGet"
    ] = gkeonprem.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBareMetalClustersBareMetalNodePoolsOperationsList"
    ] = gkeonprem.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="gkeonprem",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
